# Debug — disciplined diagnosis loop

Run for bugs, failures, regressions, slowness, flakes. Iron law: **no fix without
a hypothesis.** A patch without a named cause is a guess, not a fix.

## The loop

1. **Reproduce.** One command that shows the failure. No repro, no fix — say what
   you need to see it.
2. **Red feedback.** Build the feedback loop that goes red on this bug: a failing
   test first; logs, traces, or a minimal script when a test cannot reach it.
3. **Minimise.** Shrink the repro: smallest input, fewest steps, narrowest scope.
   Delete everything that does not change the failure.
4. **Hypothesise.** Rank candidate causes with evidence for each. Test the cheapest
   to falsify first. Say what each experiment would prove.
5. **Instrument.** Add the observation that discriminates between the top candidates.
   One experiment at a time; record the result before the next.
6. **Fix root cause.** One guard in the shared function beats a guard in every
   caller — grep the callers, fix it once where they all route through.
7. **Regression-test.** The red feedback from §2 goes green and stays in the suite,
   named after the bug it prevents.

## Stop rules

- **Three failed fixes** → stop iterating on code. Name the assumption most likely
  wrong. Ask one diagnostic question. Do not try a fourth patch first.
- **Flakes** → a rerun that passes is not a fix. Log it (what failed, both runs),
  quarantine or fix, never retry silently.
- **Performance regressions** → same loop, with numbers: baseline, current, target.
  No "feels faster". Profile before optimizing; the hotspot is guilty until measured.

After the fix lands: capture the learning (`sections/save.md`) — cause, tell, and
the test that now guards it. Offer the journal entry; do not force it.
