---
name: ste-docs
description: Write or rewrite developer documentation (READMEs, runbooks, how-tos, feature docs, PR descriptions) in ASD-STE100 Simplified Technical English, then lint it. Use for "document this", "write docs", "STE", "simplified technical english", or any team-facing doc.
---

# STE docs

Write team docs in ASD-STE100. The goal: a reader who is tired, rushed, or not a native English speaker understands it on the first read.

> Paths below are relative to this skill's base directory (shown when the skill loads). Use `python3` on macOS/Linux, `python` on Windows.

## Workflow

1. **Read the code first.** Do not document from memory or from the user's description alone. Open the files. If behavior is unclear, say so in the doc as an open question. Do not invent it.
2. **Pick the doc type** and use its skeleton (below).
3. **Draft in STE** using the rules below.
4. **Add a diagram** if the doc explains a flow, a set of components, or states. Use the `diagram` skill. Use Mermaid for docs that live in the repo, because GitHub renders it.
5. **Lint:** `python <skill-dir>/scripts/ste_lint.py <file.md>`. Fix every ERROR. Fix a WARN or give a reason it must stay.
6. **Report** what you could not verify from the code.

## Core STE rules (enforce these)

| # | Rule | Bad | Good |
|---|------|-----|------|
| 1 | Procedural sentence: max **20** words. Descriptive: max **25**. | | |
| 2 | One instruction per sentence. | Open the file and change the port. | 1. Open the file. 2. Change the port. |
| 3 | Instructions use the imperative. | You should run the migration. | Run the migration. |
| 4 | Active voice. Name who or what does the action. | The token is validated by the middleware. | The middleware validates the token. |
| 5 | No `-ing` verb forms (technical names are OK). | Running this deletes the cache. | This command deletes the cache. |
| 6 | Use simple tenses: present, past, future, imperative. | The job will have been completed. | The job is complete. |
| 7 | Put the condition first. | Restart the queue if it stops. | If the queue stops, restart it. |
| 8 | Keep articles (a, an, the). Do not write in "telegraph" style. | Set value in config. | Set the value in the config file. |
| 9 | Max 3 nouns in a cluster. | user session token refresh endpoint | the endpoint that refreshes the session token |
| 10 | Max 6 sentences per paragraph. One topic per paragraph. | | |
| 11 | One word = one meaning. Do not use synonyms for the same thing. | server / host / box / machine | server (every time) |
| 12 | Warnings and cautions start with a command, then the risk. | Data could be lost if... | Do not run this on production. It deletes all rows. |

## Common word substitutions

These are the substitutions people use most. Check unclear words against the official ASD-STE100 dictionary. This list is a starting point, not the full dictionary.

| Avoid | Use |
|---|---|
| utilize, leverage | use |
| ensure | make sure |
| perform, carry out, execute (non-technical) | do |
| obtain, retrieve, fetch (non-technical) | get |
| commence, initiate | start |
| terminate | stop |
| in order to | to |
| prior to | before |
| subsequent to | after |
| approximately | about |
| sufficient | enough |
| additional | more |
| a number of | some, many (or the number) |
| should (for an instruction) | imperative, or "must" |
| please | (remove) |
| simply, just, easily, obviously | (remove; they insult a stuck reader) |

Technical names (`php artisan migrate`, `QueueWorker`, `pnpm build`) stay as they are, in code font.

## Skeletons

**How-to / runbook**
```
# <Verb> <thing>            e.g. "Deploy the API to staging"
## Before you start         (prerequisites as a list)
## Procedure                (numbered steps, one action each)
## Result                   (what the user sees when it works)
## If it fails              (symptom -> cause -> fix table)
```

**Feature / component doc**
```
# <Component name>
## Purpose                  (2-3 sentences)
## How it works             (diagram first, then short text)
## Configuration            (table: setting | default | effect)
## Limits and known problems
## Open questions           (things the code did not make clear)
```

**PR description**
```
## What this changes
## Why
## How to test             (numbered steps)
## Risk                    (what can break, and how we would see it)
```

## Honesty rules

- If the code and the existing docs disagree, report it. Do not silently pick one.
- Do not pad. A short, correct doc is better than a long, vague one.
