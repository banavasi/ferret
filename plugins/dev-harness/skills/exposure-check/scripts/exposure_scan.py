"""Fast exposure scan for a repo (Laravel-aware, works on any repo) and an optional live URL.

Usage:
  python exposure_scan.py <repo-path> [--url https://your-app.example.com]

Only use --url against apps you own or are authorized to test.
It sends a handful of GET requests, nothing more.
"""
import argparse
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

SECRET_PATTERNS = [
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("GitHub token", re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}")),
    ("Slack token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("Stripe live key", re.compile(r"sk_live_[A-Za-z0-9]{20,}")),
    ("Anthropic/OpenAI key", re.compile(r"sk-(ant-)?[A-Za-z0-9_-]{30,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z_-]{35}")),
    ("Private key", re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("Laravel APP_KEY", re.compile(r"APP_KEY=base64:[A-Za-z0-9+/=]{30,}")),
    ("Generic secret assignment", re.compile(
        r"(?i)\b(password|passwd|secret|api_key|apikey|access_token|auth_token|client_secret)['\"]?\s*(?:=>|=|:)\s*['\"]([^\s'\"]{8,})['\"]")),
    ("Secret in env-style line", re.compile(
        r"^\s*[A-Z0-9_]*(?:PASSWORD|SECRET|TOKEN|API_KEY)=([^\s#'\"]{8,})")),
]
PLACEHOLDER = re.compile(r"(?i)(^:|\||::|\(|^\$|env\(|example|changeme|your[_-]|xxx|<|\$\{|null|secret_here|\*\*\*|password$|%s)")
SKIP_DIRS = {".git", "vendor", "node_modules", "storage", "bootstrap/cache", "public/build", "dist"}
SECRET_FILES = re.compile(r"(^|/)(\.env(\..+)?|.*\.pem|.*\.key|id_rsa|id_ed25519|.*\.p12|.*\.pfx|credentials\.json|auth\.json)$")
SAFE_ENV = re.compile(r"\.env\.(example|sample|dist|testing\.example)$")

findings = []


def add(level, area, msg):
    findings.append((level, area, msg))


def git(repo, *args):
    try:
        return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=120).stdout
    except Exception:
        return ""


def mask(s):
    return s[:4] + "..." if len(s) > 4 else "..."


def scan_tracked(repo):
    tracked = git(repo, "ls-files").splitlines()
    if not tracked:
        add("INFO", "repo", "not a git repo or no tracked files; scanning skipped")
        return
    for f in tracked:
        if SECRET_FILES.search(f) and not SAFE_ENV.search(f):
            add("HIGH", "secrets", f"secret-type file is tracked by git: {f}")
    for f in tracked:
        if any(f.startswith(d + "/") or ("/" + d + "/") in f for d in SKIP_DIRS):
            continue
        if f.endswith((".lock", ".png", ".jpg", ".svg", ".ico", ".woff", ".woff2", ".min.js", ".map")):
            continue
        path = os.path.join(repo, f)
        try:
            if os.path.getsize(path) > 1_000_000:
                continue
            with open(path, encoding="utf-8", errors="ignore") as fh:
                for n, line in enumerate(fh, 1):
                    for name, rx in SECRET_PATTERNS:
                        generic = name in ("Generic secret assignment", "Secret in env-style line")
                        for m in rx.finditer(line):
                            val = m.group(m.lastindex) if m.lastindex else m.group(0)
                            if generic and PLACEHOLDER.search(val):
                                continue
                            if SAFE_ENV.search(f) and (generic or name == "Laravel APP_KEY"):
                                continue
                            add("MED" if generic else "HIGH", "secrets", f"{name} in {f}:{n} ({mask(val)})")
                            break
        except OSError:
            pass


def scan_history(repo):
    out = git(repo, "log", "--all", "--diff-filter=D", "--name-only", "--format=")
    for f in set(out.splitlines()):
        if SECRET_FILES.search(f) and not SAFE_ENV.search(f):
            add("HIGH", "secrets", f"secret-type file existed in git history (deleted later): {f} -> rotate it")
    hist = git(repo, "log", "--all", "-p", "--no-color", "-G",
               r"(AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{36}|sk_live_|BEGIN .*PRIVATE KEY|APP_KEY=base64:)")
    commits = set(re.findall(r"^commit ([0-9a-f]{7})", hist, re.M))
    if commits:
        add("HIGH", "secrets", f"high-confidence secret patterns appear in history, commits: {', '.join(sorted(commits)[:8])}")


def read(repo, rel):
    try:
        with open(os.path.join(repo, rel), encoding="utf-8", errors="ignore") as fh:
            return fh.read()
    except OSError:
        return None


def scan_laravel(repo):
    if read(repo, "artisan") is None:
        return
    app = read(repo, "config/app.php") or ""
    if re.search(r"'debug'\s*=>\s*(true|\(bool\)\s*env\('APP_DEBUG',\s*true\))", app):
        add("MED", "config", "config/app.php: debug defaults to true when APP_DEBUG is unset")
    cors = read(repo, "config/cors.php") or ""
    if re.search(r"'allowed_origins'\s*=>\s*\[\s*'\*'\s*\]", cors):
        sup = re.search(r"'supports_credentials'\s*=>\s*true", cors)
        add("HIGH" if sup else "MED", "config", "config/cors.php: allowed_origins is '*'" + (" with credentials" if sup else ""))
    sess = read(repo, "config/session.php") or ""
    if re.search(r"'secure'\s*=>\s*false", sess):
        add("MED", "config", "config/session.php: secure cookie forced to false")
    if re.search(r"'http_only'\s*=>\s*false", sess):
        add("MED", "config", "config/session.php: http_only is false")
    gi = read(repo, ".gitignore") or ""
    if ".env" not in gi:
        add("HIGH", "secrets", ".gitignore does not ignore .env")
    composer = read(repo, "composer.json") or ""
    for pkg, label in (("laravel/telescope", "Telescope"), ("laravel/horizon", "Horizon"),
                       ("barryvdh/laravel-debugbar", "Debugbar")):
        if pkg in composer:
            add("INFO", "debug-tools", f"{label} installed: verify its gate()/enabled flag blocks non-admins in production")
    for rel in ("routes/web.php", "routes/api.php"):
        src = read(repo, rel)
        if not src:
            continue
        if "auth" not in src and re.search(r"Route::(get|post|put|patch|delete|resource|apiResource)", src):
            add("MED", "auth", f"{rel}: has routes but no 'auth' middleware anywhere in the file - check every data route")
        for m in re.finditer(r"Route::(post|put|patch|delete)\(\s*'([^']+)'", src):
            add("INFO", "auth", f"{rel}: write route {m.group(1).upper()} {m.group(2)} - confirm it is inside auth middleware")


def scan_ci(repo):
    wf_dir = os.path.join(repo, ".github", "workflows")
    files = [os.path.join(wf_dir, f) for f in os.listdir(wf_dir)] if os.path.isdir(wf_dir) else []
    if os.path.exists(os.path.join(repo, "azure-pipelines.yml")):
        files.append(os.path.join(repo, "azure-pipelines.yml"))
    for p in files:
        src = read(repo, p) or ""
        name = os.path.relpath(p, repo)
        if "pull_request_target" in src and "actions/checkout" in src:
            add("HIGH", "ci", f"{name}: pull_request_target + checkout can run untrusted PR code with secrets")
        if re.search(r"echo .*\$\{\{\s*secrets\.", src):
            add("MED", "ci", f"{name}: echoes a secret")
        if re.search(r"permissions:\s*write-all", src):
            add("MED", "ci", f"{name}: permissions: write-all")


PROBES = ["/.env", "/.git/HEAD", "/telescope", "/horizon", "/_ignition/health-check",
          "/phpinfo.php", "/storage/logs/laravel.log", "/_debugbar/open", "/server-status"]
SIGNS = {"/.env": "APP_", "/.git/HEAD": "ref:", "/storage/logs/laravel.log": "local.ERROR",
         "/_ignition/health-check": "can_execute_commands", "/phpinfo.php": "phpinfo"}
HEADERS = ["strict-transport-security", "content-security-policy", "x-content-type-options",
           "x-frame-options", "referrer-policy"]


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def fetch(url, follow=True):
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(NoRedirect)
    req = urllib.request.Request(url, headers={"User-Agent": "exposure-check/1.0"})
    try:
        r = opener.open(req, timeout=10)
        return r.status, dict((k.lower(), v) for k, v in r.headers.items()), r.read(4000).decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        return e.code, dict((k.lower(), v) for k, v in e.headers.items()), ""
    except Exception as e:
        return None, {}, str(e)


def probe(base):
    base = base.rstrip("/")
    status, headers, body = fetch(base)
    if status is None:
        add("INFO", "live", f"could not reach {base}: {body}")
        return
    add("INFO", "live", f"{base} -> HTTP {status} (reachable from this machine without login: {'yes' if status == 200 else 'check'})")
    if base.startswith("https://"):
        s, h, _ = fetch("http://" + base[len("https://"):], follow=False)
        if s == 200:
            add("MED", "live", "plain http:// serves the app instead of redirecting to https")
    else:
        add("HIGH", "live", "URL is not HTTPS")
    for h in HEADERS:
        if h not in headers:
            add("LOW", "headers", f"missing {h}")
    if "x-powered-by" in headers:
        add("LOW", "headers", f"x-powered-by leaks stack: {headers['x-powered-by']}")
    for p in PROBES:
        s, _, b = fetch(base + p)
        if s == 200:
            sign = SIGNS.get(p)
            if sign is None or sign in b:
                add("HIGH", "live", f"{p} answers 200" + (f" and contains '{sign}'" if sign else " - check if it needs a login"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--url")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    scan_tracked(repo)
    scan_history(repo)
    scan_laravel(repo)
    scan_ci(repo)
    if a.url:
        probe(a.url)
    order = {"HIGH": 0, "MED": 1, "LOW": 2, "INFO": 3}
    findings.sort(key=lambda f: order[f[0]])
    for lvl, area, msg in findings:
        print(f"[{lvl:4}] {area:11} {msg}")
    highs = sum(1 for f in findings if f[0] == "HIGH")
    print(f"\n{len(findings)} finding(s), {highs} HIGH. This is a heuristic pass; read the SKILL.md checklist for what it does not cover.")
    return 1 if highs else 0


if __name__ == "__main__":
    sys.exit(main())
