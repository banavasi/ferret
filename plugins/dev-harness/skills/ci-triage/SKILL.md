---
name: ci-triage
description: Find out why a CI/CD pipeline run failed (GitHub Actions or Azure DevOps Pipelines) and explain it in plain terms for a non-DevOps developer. Use for "why did the build fail", "pipeline failed", "CI is red", "devops run failed", "check the workflow", or a pasted run URL or log.
---

# CI triage

The user is not a DevOps specialist. Explain the root cause, not the noise, and teach the one concept they were missing.

## 1. Get the failing logs (do not guess from the run title)

**GitHub Actions** (needs `gh`; run `! gh auth login` once if it is not logged in):
```
gh run list --limit 10                      # find the run
gh run view <run-id>                        # jobs + which step failed
gh run view <run-id> --log-failed           # only failed step logs
gh run view <run-id> --job <job-id> --log   # full job log if needed
```
For a URL like `.../actions/runs/<id>`, use that id.

**Azure DevOps** (needs `az`, `az extension add --name azure-devops` and `az login` once):
```
az pipelines runs list --top 10 -o table
az pipelines runs show --id <run-id>
az devops invoke --area build --resource timeline --route-parameters project=<proj> buildId=<run-id>   # find failed records
az devops invoke --area build --resource logs --route-parameters project=<proj> buildId=<run-id> logId=<log-id>
```
If auth fails, tell the user the exact command to run (`! az login`) and stop.

Then read the workflow file the run used (`.github/workflows/*.yml` or `azure-pipelines.yml`) at the run's commit.

## 2. Find the first real error

- Scroll to the **first** error, not the last. Later errors are usually fallout.
- Ignore warnings and deprecation notices unless they are the failure.
- Classify the failure:

| Class | Typical signs |
|---|---|
| Code / test | assertion failed, test name, stack trace into app code |
| Lint / static analysis | pint, phpstan, eslint, exit code from linter step |
| Dependency | composer / pnpm install fails, lockfile mismatch, version conflict |
| Environment | missing env var / secret, wrong PHP / Node version, service (DB) not up |
| Flaky / infra | timeout, network error, runner died; passes on re-run |
| Pipeline config | YAML error, wrong path, missing permission on token |

- Check if it is new: `gh run list --workflow <name> --limit 5` — did the same step pass on the previous commit? `git log <last-green-sha>..<failing-sha>` narrows the cause.

## 3. Report (in this shape)

```
VERDICT: <one sentence: what broke and why>
CLASS:   <class from table>   NEW?: yes (since <sha>) / no (failing since <date>)
EVIDENCE: <the 3-10 log lines that prove it>
FIX:     <the exact change or command>
CONFIDENCE: high / medium / low — and what would raise it
CONCEPT: <the one CI/DevOps idea behind this, explained in 2-3 lines>
```

Draw the pipeline (stages -> jobs -> failing step in red) with the `diagram` skill when the pipeline has more than one stage or the failure is in a dependency between jobs.

## Rules
- Do not suggest "re-run it" unless the evidence says flaky/infra. Say why you think it is flaky.
- Do not suggest disabling a test, linter, or check to make it green. If the user asks, say plainly that it hides the bug and does not fix it.
- Do not push fixes or re-run pipelines without the user's go-ahead.
- If the failure is a leaked or missing secret, also flag it to the `exposure-check` skill's concerns.
