# Design — review the user-facing surface

Run for UI, layout, API shape, naming, and user-facing copy. Taste is enforced
with ratings and evidence, not vibes.

## 1. Rate each dimension 0–10

Score the dimensions that apply (UI: layout, typography, color, spacing, states,
motion, accessibility; API: naming, consistency, errors, versioning, docs). For
each score below 8, state what a 10 looks like in one concrete sentence. No
dimension passes on "looks fine" — the sentence is the review.

## 2. Slop check

Flag the generic-AI tells: lorem/placeholder text in shipped paths, purple-blue
gradients with glassmorphism on everything, identical card grids with no hierarchy,
emojis as iconography, timeouts and magic numbers without names, error strings a
user (or an agent) cannot act on. Each flag quotes the spot and names the fix.

Error strings get their own bar: say what happened, what to do next, and where to
look. An error an agent meets at 2am must be fixable from the message alone.

## 3. Decide interactively

One question per design choice, each with discrete options and a recommendation.
Never batch five taste decisions into one message. Record each decision with its
reason — decisions evaporate faster than code.

## 4. Fix with evidence

Fixes land as small commits with before/after evidence (screenshot, snippet, or
rendered output). Re-rate the touched dimensions after the fix; the rating either
moves or the fix was styling, not design. State which.
