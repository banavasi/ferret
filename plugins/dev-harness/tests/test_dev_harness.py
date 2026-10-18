"""Tests for dev-harness scripts and hook. Run from the repo root:
python -m unittest discover -s plugins/dev-harness/tests -v
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINT = os.path.join(ROOT, "skills", "ste-docs", "scripts", "ste_lint.py")
SCAN = os.path.join(ROOT, "skills", "exposure-check", "scripts", "exposure_scan.py")
HOOK = os.path.join(ROOT, "hooks", "straight-talk.mjs")


def run(*args, env=None, cwd=None):
    return subprocess.run(list(args), capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=env, cwd=cwd)


class SteLintTest(unittest.TestCase):
    def lint(self, text):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(text)
        try:
            return run(sys.executable, LINT, f.name)
        finally:
            os.unlink(f.name)

    def test_flags_common_violations(self):
        r = self.lint("You should utilize the script in order to ensure the app is deployed by CI.\n")
        self.assertEqual(r.returncode, 1)
        for word in ("utilize", "ensure", "in order to", "should", "passive"):
            self.assertIn(word, r.stdout)

    def test_long_procedural_step(self):
        step = "1. " + " ".join(["word"] * 22) + ".\n"
        r = self.lint(step)
        self.assertIn("max 20 for procedural", r.stdout)

    def test_clean_doc_passes(self):
        r = self.lint("# Deploy\n\n1. Open the config file.\n2. Run the migration.\n\nThe server starts.\n")
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_code_blocks_ignored(self):
        r = self.lint("Run this command.\n\n```\nutilize ensure should\n```\n")
        self.assertEqual(r.returncode, 0, r.stdout)


class ExposureScanTest(unittest.TestCase):
    def repo(self, files):
        d = tempfile.mkdtemp()
        run("git", "init", "-q", cwd=d)
        for name, body in files.items():
            os.makedirs(os.path.dirname(os.path.join(d, name)) or d, exist_ok=True)
            with open(os.path.join(d, name), "w", encoding="utf-8") as f:
                f.write(body)
        run("git", "add", ".", cwd=d)
        run("git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "x", cwd=d)
        return d

    def test_detects_secrets(self):
        d = self.repo({"k.txt": "AKIAABCDEFGHIJKLMNOP\n",
                       "a.php": "$x = ['password' => ':default', 'api_key' => 'abcd1234efgh5678'];\n"})
        r = run(sys.executable, SCAN, d)
        self.assertEqual(r.returncode, 1)
        self.assertIn("AWS access key", r.stdout)
        self.assertIn("a.php:1", r.stdout)
        self.assertNotIn("AKIAABCDEFGH", r.stdout, "secret values must be masked")

    def test_ignores_validation_rules(self):
        d = self.repo({"a.php": "'password' => 'required|string|min:8',\n'password' => Password::default(),\n"})
        r = run(sys.executable, SCAN, d)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertNotIn("Generic secret", r.stdout)

    def test_tracked_env_file(self):
        d = self.repo({".env": "APP_ENV=local\n", ".env.example": "DB_PASSWORD=changeme123\n"})
        r = run(sys.executable, SCAN, d)
        self.assertIn("secret-type file is tracked by git: .env", r.stdout)
        self.assertNotIn(".env.example", r.stdout)


class HookTest(unittest.TestCase):
    def test_injects_rules(self):
        env = dict(os.environ, CLAUDE_PLUGIN_ROOT=ROOT)
        env.pop("DEV_HARNESS_STRAIGHT_TALK", None)
        r = run("node", HOOK, env=env)
        out = json.loads(r.stdout)
        ctx = out["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Verdict first", ctx)
        self.assertNotIn("description:", ctx, "frontmatter must be stripped")

    def test_opt_out(self):
        env = dict(os.environ, CLAUDE_PLUGIN_ROOT=ROOT, DEV_HARNESS_STRAIGHT_TALK="0")
        r = run("node", HOOK, env=env)
        self.assertEqual(r.stdout, "")


if __name__ == "__main__":
    unittest.main()
