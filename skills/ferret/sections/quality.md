# Quality — self-review, test audit, QA, security

Run for test-it, check-quality, audit-tests, QA, secure, and self-review before a PR.

## 1. Self-review the diff

Read the full diff once, top to bottom, as a stranger would. Check: does each hunk
serve the spec (scope creep dies here); are names honest; are errors actionable;
is there a test per behavior; would you approve this from someone else? Fix the
obvious, list the doubtful with file:line. Then hand genuine review to critics
(`sections/review.md`) — self-review never replaces them.

## 2. Test audit

Sweep the touched tests for ones that cost more than they protect:

- source greps and tautologies (pass by construction, never disagree with code)
- duplicates covering the same behavior through the same seam
- assertion-free probes (exercise code, verify nothing)
- test-only exports and hooks added to production code for tests

Every candidate carries an evidence card: file:line, what it costs, what would be
lost. Report-only unless the user approves a batch. Approved removals keep one
guard per behavior — audit trims fat, never coverage.

## 3. QA the changed behavior

For user-facing changes: reproduce the flow end to end in the real surface
(browser, CLI, API), write a failing regression for each bug found, fix the cause
(not the symptom), and re-verify before committing. No "should work" — show the
passing run. Record what was verified and how; unverified paths are named, not
implied.

## 4. Security checklist

Every change touching auth, input, secrets, network, or dependencies answers:

- Who can reach this, and what proves they should? (authN/Z, default-deny)
- Where does untrusted input flow, and what neutralizes it? (injection, SSRF, traversal)
- Are secrets absent from code, logs, and errors? Is the failure mode closed?
- Are dependencies pinned, and is anything newly added justified?

This is a checklist pass, not a full audit: containers, scanners, and threat
modeling are out of scope. Say that plainly when the change deserves a real audit
(auth systems, payments, PII) instead of pretending the checklist covered it.
