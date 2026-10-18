---
name: journal
description: Developer journal. Log what I did and how, record decisions (ADR-lite), capture ideas and things I learned, and generate standup notes from the log. Use for "/journal", "log this", "journal", "record this decision", "I have an idea", "what did I do yesterday", "standup notes", "weekly summary".
---

# Journal

One journal for everything: daily log, decisions, ideas, learnings, standup. Plain Markdown, so it is greppable and survives any tool change.

**Location:** `$DEV_JOURNAL` if set, else `~/dev-journal/` (create it on first use). The journal stays on this machine. On a work machine it can hold company details: do not commit it to a public repo or sync it to a personal cloud.

```
~/dev-journal/
  daily/2026-10-17.md        one file per day
  decisions/0001-<slug>.md   one file per decision
  ideas.md                   append-only
  learned.md                 append-only (concepts I had to have explained)
```

## Modes (parse from args; default is `log`)

### `log` (default) — what I did and how
1. Gather facts, do not ask for what you can find: `git log --since=midnight --author="$(git config user.name)" --stat` in the current repo, the session's work, and anything the user typed.
2. Ask the user at most 2 short questions for what git cannot show (for example: "What blocked you?" "What was the hardest part?").
3. Append to today's daily file:
```
## HH:MM — <repo> — <one-line title>
**Did:** what changed (link files / PR / ticket)
**How:** the approach, the commands, the key insight
**AI did / I did:** be honest about which parts the AI wrote and which parts the user wrote or understood
**Stuck on / open:** ...
**Next:** ...
```
4. **Push back:** if "How" is vague ("fixed the bug"), ask for the mechanism. If the AI wrote it and the user cannot say how it works, write that down plainly and suggest `/explain-back`.

### `decision` — record a decision
Write `decisions/NNNN-<slug>.md` (next number):
```
# NNNN. <Decision title>
Date: YYYY-MM-DD   Status: accepted | proposed | superseded by NNNN
## Context        what forced a choice
## Options        at least 2 real options, each with its main cost
## Decision       what we chose
## Why            the deciding reason
## Consequences   what gets harder; what we must watch
## Revisit when   a concrete trigger (load > X, team grows, lib deprecated)
```
**Push back hard here.** If only one option is listed, the user did not decide anything, they defaulted. Make them name the option they rejected and why. If the reason is "it's what I know" or "AI suggested it", say so plainly in **Why**. Do not dress it up.

### `idea` — capture an idea
Append to `ideas.md`: date, the idea in one line, the problem it solves, the cheapest way to test it. If the idea has no problem it solves, say so.

### `learned` — something I did not know
Append to `learned.md`: date, concept, a 2-3 line explanation in your own words, and a link to where it showed up in code. `/explain-back` writes here too.

### `standup` — prepare standup
Read the last working day's daily file (skip weekends) plus today's. Output:
```
Yesterday: (max 3 bullets, outcomes not activity)
Today:     (max 3 bullets)
Blockers:  (or "none")
```
Call out bullets that are activity without an outcome ("worked on X" -> "what is done?").

### `week` — weekly review
Summarize the last 7 daily files: shipped, decisions made, things learned, recurring blockers. End with one blunt observation about a pattern (for example "3 of 5 days blocked on CI; that is the real problem").

## Rules
- Never overwrite a journal file. Append only (decisions are new files).
- Use absolute dates.
- Keep entries short. A journal that takes 10 minutes to write does not get written.
