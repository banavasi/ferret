---
name: exposure-check
description: Check that an app we build is not exposed to people who should not see it - leaked secrets, debug mode, open admin/debug routes, missing auth, public storage, weak headers, public preview/staging deploys. For a developer who is not a security or DevOps specialist. Use for "is this secure", "can people see this", "is staging public", "exposure check", "lock this down", or before sharing or deploying an app.
---

# Exposure check

Question to answer: **"Can someone who should not see this app, its data, or its secrets get to them?"** This is a fast check for common exposure. It is not a full pentest. For a deep code audit, also run `/security-review`.

> Paths below are relative to this skill's base directory (shown when the skill loads). Use `python3` on macOS/Linux, `python` on Windows.

**Scope rule:** probe only apps and URLs the user owns or is authorized to test. If the URL ownership is unclear, ask first.

## 1. Repo scan (always)

```
python <skill-dir>/scripts/exposure_scan.py <repo-path>
```
It flags: committed `.env` / keys, secret-like strings in tracked files and git history, `APP_DEBUG=true` defaults, wildcard CORS, debug tools (Telescope, Horizon, Debugbar, Ignition) without a gate, and routes outside auth middleware.

Then read and judge by hand (the script only points):
- `routes/*.php`: every route that reads or writes user data must sit inside `auth` (or a policy). List any that do not.
- `app/Providers/*ServiceProvider.php`: Telescope / Horizon `gate()` must not return `true` for everyone.
- `config/cors.php`, `config/session.php` (`secure`, `http_only`, `same_site`), `config/app.php` (`debug`).
- `storage/app/public` and `public/`: no uploads or exports that should be private.
- `.github/workflows/*` / `azure-pipelines.yml`: secrets printed with `echo`, `pull_request_target` with checkout of PR code, over-broad `permissions:`.
- For other stacks: the same ideas (debug flag, admin routes, CORS, secret files, auth on every data route).

## 2. Live probe (only if the user gives a URL they own)

```
python <skill-dir>/scripts/exposure_scan.py <repo-path> --url https://staging.example.com
```
It sends a few plain GET requests and checks: HTTPS + redirect, security headers, and whether `/.env`, `/.git/HEAD`, `/telescope`, `/horizon`, `/_ignition/health-check`, `/phpinfo.php`, `/storage/logs/laravel.log` answer with content.

Also ask the user, because the code cannot show it:
- Is staging / preview behind a login, VPN, IP allow-list, or SSO (for example Cloudflare Access)? "Nobody knows the URL" is **not** protection; URLs leak through logs, referrers, and certificate transparency.
- Is the database / Redis port open to the internet?
- Who has access to the hosting, CI secrets, and the repo? Any ex-team members?

## 3. Report

Draw the trust boundaries (internet -> edge -> app -> DB / storage / third parties) with the `diagram` skill and mark each finding where it lives.

```
EXPOSED NOW (fix today):     findings anyone on the internet can reach
EXPOSED IF (fix this week):  needs one mistake or one leaked URL
HARDENING (backlog):         headers, cookie flags, least privilege
NOT CHECKED:                 what this pass did not cover
```
For each finding: what an outsider can do with it, the evidence, and the exact fix.

## Rules
- A secret that was ever committed is compromised, even if a later commit deleted it. The fix is: **rotate it**, then clean the history. Say this plainly.
- Do not print full secret values in the report. Show the first 4 characters and the file:line.
- Do not run scanners, brute force, or high-volume requests. Few GETs only.
- Do not say "secure". Say what was checked and what was not.
