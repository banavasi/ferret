# Ship — PR, land, watch

Run for PR, merge, ship, deploy, release, canary, provision, credentials.
Nothing merges on a red gate or an unverified claim.

## 1. Shape the PR

PR body, in this order:

1. **Summary** — the smallest visual that makes the change clear (one snippet,
   screenshot, or diagram beats three paragraphs).
2. **Before/after evidence** — proof it works: test runs, QA notes, measured
   numbers. Link the spec or tickets it closes.
3. **Merge-danger call** — one-way door (hard to reverse: migrations, public APIs,
   data changes) or two-way door, plus blast radius (who feels it if this is wrong).

## 2. Pipeline

Sync main → run the full relevant test gate → self-review (`sections/quality.md` §1)
→ critics on the diff (`sections/review.md`) → push → open the PR. A weakened test,
raised timeout, snapshot update, or suppression anywhere in the diff is named in the
PR body by file:line — gates weakened in silence fail this step.

## 3. Land

Merge (the repo's one method, never mixed) → wait for CI → deploy → verify
production health (reachable, correct version, key flow green). "Deployed" is said
only after the verification run, never after the merge.

## 4. Watch (canary)

After landing, watch for console errors, failed checks, latency movement, and user
reports for the agreed window. Anything red pages the debug loop (`sections/debug.md`)
with the evidence attached. Report "quiet" explicitly — silence without a verdict
is not a watch.

## 5. Human-only steps (wizard)

Steps only the human can do (provisioning, credentials, CI secrets, third-party
dashboards, one-off migrations) ship as a generated bash wizard: ordered prompts,
validation per answer, dry-run where possible, and a recorded transcript appended
to the journal. Never ask the human to "just run a few commands" from chat.
