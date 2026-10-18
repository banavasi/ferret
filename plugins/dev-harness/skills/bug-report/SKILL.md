---
name: bug-report
description: Turn a vague "this is broken" into a bug report another developer can act on without asking questions. Use for "report a bug", "file a bug", "write up this bug", "create an issue for this", or after finding a defect during review or testing.
---

# Bug report

A good bug report lets a stranger reproduce the bug in 5 minutes. Write it in plain, short sentences (STE style, see `ste-docs`).

## Steps

1. **Reproduce it yourself first** if the environment allows it (run the test, hit the route, read the log). If you cannot reproduce it, say so in the report. Do not pretend.
2. **Find the narrowest trigger.** Strip steps until removing one more makes the bug go away.
3. **Locate it if cheap:** the file:line or the commit where it started (`git log -S`, `git bisect` if the user agrees). Mark this as "suspected" unless proven.
4. **Rate severity honestly:** do not inflate to get attention, do not deflate to avoid conflict.
   - S1: data loss, security exposure, or prod down
   - S2: a main feature broken, no workaround
   - S3: broken with a workaround
   - S4: cosmetic
5. Write the report:

```
## <Component>: <what goes wrong> when <trigger>
Severity: S1-S4 — <one-line reason>
Environment: branch/commit, env (local/staging/prod), browser/OS if UI

### Steps to reproduce
1. ...
2. ...

### Expected
### Actual
(exact error text, status code, screenshot path, log lines — in code blocks)

### Suspected cause
file:line + why (or "not investigated")

### Scope
Who / what else is affected. Is data already damaged?
```

6. **Output:** show the report. Create the issue only when the user says so: `gh issue create --title ... --body-file ...` (GitHub), or via the Jira/Atlassian connector if connected. Do not post without a go-ahead.

## Push back when
- The "bug" is a feature request or a spec question. Say so; it belongs with the product owner.
- The steps are "sometimes it fails". Ask what was different the times it failed, or say the report is not actionable yet.
- Severity is S1 and nobody has been told. Tell the user to raise it now, not just file it.
