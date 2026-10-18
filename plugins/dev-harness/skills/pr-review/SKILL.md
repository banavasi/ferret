---
name: pr-review
description: Review a pull request (mine or a teammate's) the way a strong senior reviewer would - correctness, security, exposure, design, tests - ranked by damage, with the reasoning shown so I learn to spot it myself next time. Use for "review this PR", "review PR #123", "is this ready to merge", "check my diff", or a pasted PR URL.
---

# PR review

Two goals: catch what would hurt in production, and teach the user to catch it next time.

## 1. Get the change

- GitHub: `gh pr view <n> --json title,body,files,baseRefName,headRefName` and `gh pr diff <n>`.
- Azure DevOps: `az repos pr show --id <n>`, then fetch and `git diff <target>...<source>`.
- Local: `git diff main...HEAD` plus `git diff`.

Read the PR description and the linked ticket first. Then read the **whole changed files** where needed, not only the diff hunks. Bugs hide in what the diff did not touch.

## 2. Check, in this order

1. **Does it do what the ticket says?** Missing cases, wrong behavior, scope creep.
2. **Correctness:** null / empty / zero rows, off-by-one, race conditions, error paths that swallow failures, timezones, money as float.
3. **Security and exposure:** missing auth or policy on a new route, mass assignment, injection (raw SQL, `{!! !!}` in Blade, shell), secrets in code, new public endpoints. Use the `exposure-check` skill's ideas.
4. **Data:** migrations that lock big tables or are not reversible, N+1 queries, missing indexes on new filters.
5. **Tests:** does a test fail if the main change is reverted? If not, it does not test the change.
6. **Design:** only if it will cost real time later. Not style nits a linter can catch.

## 3. Report

```
VERDICT: Approve / Approve with fixes / Request changes — one line why

BLOCKERS (must fix before merge)
1. file:line — problem — what breaks, for whom — fix

SHOULD FIX
...

NITS (max 3, optional)
...

WHAT TO LEARN FROM THIS PR
- The pattern behind the top finding, in 2 lines, so the user spots it next time.
```

- Every finding has a file:line and a concrete failure, not "consider maybe".
- If a finding is a guess, label it "unverified" and say what would confirm it.
- If the PR is good, say "Approve" and stop. Do not invent findings to look thorough.
- If the change is big or touches a flow, draw before/after with the `diagram` skill.

## 4. Posting

Do not post comments to the PR unless the user says so. When they do, write review comments in short plain sentences (STE style), blunt about the code, respectful to the author.
