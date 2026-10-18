# dev-harness

A Claude Code plugin that makes you a better developer, not just a faster one.
It ships in the same marketplace as `i-have-adhd`, and the two work together.

## Install

```
/plugin marketplace add banavasi/i-have-adhd
/plugin install dev-harness@i-have-adhd
/plugin install i-have-adhd@i-have-adhd     # optional, recommended
```

Restart Claude Code after the install.

**Requirements:** `node` (for the hook), `python3` (for the linters), `git`. Optional: `gh` for GitHub, `az` with the `azure-devops` extension for Azure DevOps.

## What you get

| Skill | Use it to |
|---|---|
| `straight-talk` | Get blunt feedback: verdict first, hard pushback, verified vs guessed. **Always on** through a SessionStart hook. |
| `diagram` | Get a visual explanation: an HTML artifact, Mermaid for the repo, or FigJam/Excalidraw for a whiteboard. |
| `explain-back` | Prove you understand AI-written code. It draws the change, quizzes you, and grades the answers. |
| `journal` | Log what you did and how, decisions (ADR-lite), ideas, learnings. Also makes `standup` and `week` reports. |
| `ste-docs` | Write docs in ASD-STE100. Includes a linter. |
| `pr-review` | Review a PR by damage, and learn the pattern behind the top finding. |
| `ci-triage` | Find why a GitHub Actions or Azure DevOps run failed. |
| `exposure-check` | Find out if people who should not see the app can reach it, its data, or its secrets. |
| `bug-report` | Turn "it's broken" into a report another developer can act on. |

## Daily loop

```mermaid
flowchart LR
    A[Standup<br/>/journal standup] --> B[Work on story]
    B --> C{AI wrote it?}
    C -- yes --> D[/explain-back/]
    C -- no --> E[/pr-review/ own diff]
    D --> E
    E --> F[/ste-docs/ + /diagram/]
    F --> G[/journal/ log + decision]
    G --> A
    B -. CI red .-> H[/ci-triage/]
    B -. before deploy .-> I[/exposure-check/]
```

## Settings

| Env var | Effect |
|---|---|
| `DEV_HARNESS_STRAIGHT_TALK=0` | Turn off the always-on straight-talk hook. |
| `DEV_JOURNAL=/path` | Put the journal somewhere other than `~/dev-journal/`. |

In a session, say "soften up" to pause straight talk, and "straight talk" to turn it back on.

## Limits

- `ste_lint.py` is a heuristic. It does not contain the full ASD-STE100 dictionary.
- `exposure_scan.py` finds common exposure. It is not a pentest, and a clean result does not mean "secure".
- The journal is local Markdown. On a work machine, keep it out of public repos.

## Tests

```
python -m unittest discover -s plugins/dev-harness/tests -v
```
