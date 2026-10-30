# Plan — spec, tickets, huge work

Run when there is an agreed frame and the user wants a spec, tickets, or a
breakdown. Synthesize; do not re-interview what framing already settled.

## 1. Spec

Turn the conversation into a spec. Before writing, quiz: which modules are touched,
what is the seam (public boundary under change), what is explicitly out of scope.

```
# <spec title>   Date: <YYYY-MM-DD>
## Goal        one paragraph + done-test
## Seams       each public boundary touched, one line on what it exposes
## Behavior    numbered requirements, each testable
## Non-goals   carried from the frame, plus anything new
## Risks       each with a cheap kill test
## Open        questions with owners and dates, not eternal maybes
```

Publish to the issue tracker when the repo has one; otherwise file under `specs/`.
One spec per change. If the spec exceeds what one session can hold, use §3 first.

## 2. Tickets

Break the spec into tracer-bullet tickets: each ticket is one vertical slice
(test → implement → verify) with its blocking edges declared:

```
- [ ] <slice>: <done-test>   blocks: <ids>   blocked-by: <ids>
```

Rules: slices stay small enough to finish in one sitting; no ticket without a
done-test; no ticket without declared edges (write `edges: none` when true).
Write to the tracker with native blocking links when available, else a local file
the implementer reads. Order the build frontier: unblocked tickets first.

## 3. Huge work (wayfinder)

When the path itself is unclear, do not plan the work — plan the decisions.
Create one decision ticket per unknown on the tracker, each with options and a
resolution test. Resolve them one at a time, nearest-first, until the way is clear.
Only then write the spec (§1). A decision ticket never contains implementation;
it ends in a recorded decision (`sections/save.md`, decision format).
