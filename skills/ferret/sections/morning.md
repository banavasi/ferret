# Morning — standup, triage, day plan

Run at session start when the user signals morning, or when asked for standup,
triage, or a day plan. Keep it under 10 minutes of user attention.

## 1. Standup prep

Read the last working day's journal file plus today's (paths in `sections/save.md`).
Output:

```
Yesterday: (max 3 bullets, outcomes not activity)
Today:     (max 3 bullets, proposed from open work)
Blockers:  (or "none")
```

Push back on activity-without-outcome ("worked on X" → "what is done?").
Ask at most 2 short questions for what files and git cannot show
(`git log --since=yesterday --author="$(git config user.name)" --stat`).

## 2. Triage

Pull every untriaged item (tracker issues, review requests, CI failures, messages).
Move each through the state machine exactly once per session:

```
new → needs-info | accepted | rejected
accepted → ready (has owner + acceptance test) | blocked (names the blocker)
```

Rules:

- One decision per item. No item stays `new` at the end.
- `rejected` needs a one-line reason, recorded on the item.
- `accepted` without an acceptance test is not `ready`; write the test line yourself
  when it is obvious, ask when it is not.
- Apply the repo's triage labels (from the repo setup note; ask once per repo if missing).
- Batch the trivial, surface the costly: anything irreversible, cross-team, or
  >1 day gets its own decision line. The rest goes in one compact list.

## 3. Day plan

Propose the top 3 outcomes for today, each with a timebox and a done-test:

```
1. <outcome> — ~<time>. Done when: <observable test>.
```

Order by: blockers first, then highest value, then smallest effort.
Name what you are explicitly NOT doing today (one line).
End with the single first action for item 1 (router rule 1 and 3 still apply).
