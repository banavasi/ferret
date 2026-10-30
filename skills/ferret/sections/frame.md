# Frame — reframe before build

Run for new features, new products, "is this worth building", and brainstorms.
No code until the frame survives. Target: 15 minutes, ending in a design note
that downstream work reads.

## 1. Listen to the pain, not the feature request

Ask for specific examples, not hypotheticals: what happened, how often, what it cost.
Push until you hear a concrete story. Vague pain ("reporting is slow") gets one
follow-up ("slow for whom, doing what, last time it hurt?"), then you proceed with
what you have and mark assumptions.

## 2. Push back on the framing

Restate what they described in your own words, then challenge it:

- Name the thing they are actually describing when it differs from what they asked
  (a "daily briefing app" that is really a "chief-of-staff AI").
- Challenge up to 4 premises. Each challenge is one line: the premise, why it may
  be wrong, what changes if it is. The user agrees, disagrees, or adjusts each.
- Extract capabilities they did not realize they were describing (numbered, max 5).

## 3. Interview until the design tree is resolved

Relentless, narrow questions: one branch at a time, each answer closing options.
No question with an obvious answer; no stacking three questions in one message.
Stop when every branch ends in a decision or a named experiment.

## 4. Sharpen the terms

Every domain term earns a one-line definition in the project's glossary
(`GLOSSARY.md`, create it if missing). Challenge fuzzy terms against edge cases:
"If X, is it still a <term>?" Terms that survive get used in code, specs, and tests
verbatim from now on.

## 5. Approaches + recommendation

Generate 2–3 implementation approaches with effort estimates (concrete units).
Recommend one: usually the narrowest wedge that teaches something real.
Say what the full vision costs so the wedge is a choice, not a default.

## 6. Write the design note

File it where the repo keeps such notes (`docs/design/<slug>.md` default):

```
# <title>   Date: <YYYY-MM-DD>   Status: proposed
## Pain          the concrete story, with frequency and cost
## Frame         what we are actually building, in one paragraph
## Non-goals     what we explicitly will not do
## Approaches    options with effort; recommendation marked
## Open          named experiments, each with a kill test
## Terms         new glossary entries
```

Then state the handoff: spec and tickets come from `sections/plan.md` when approved.
