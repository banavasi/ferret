# Build — implement test-first

Run for build, implement, change, refactor, spike, prototype. Drive every change
through the red→green loop at pre-agreed seams.

## 1. Agree the seams first

A seam is the public boundary you test at: the interface where behavior is
observed without reaching inside. Before any test, write down the seams and
confirm them with the user, one line each on what it catches and what it misses.
No test at an unconfirmed seam. Use the project's glossary terms for names.

When the interface shape itself is in question, design it first: deep modules
(a lot of behavior behind a small interface), placed at a clean seam, testable
through that interface. Shallow wrappers and speculative hooks are rejected here,
not in review.

## 2. The loop

One seam, one test, one minimal implementation per cycle:

1. **Red.** Write the failing test first. It reads like a specification
   ("user can check out with a valid cart") and survives refactors because it
   touches only the seam. Expected values come from an independent source of
   truth (literal, worked example, spec) — never recomputed the way the code does.
2. **Green.** Only enough code to pass. No speculative features, no future tests.
3. **Next slice.** Each test is a tracer bullet responding to what the last cycle
   taught you. Work in vertical slices, never all-tests-then-all-code.

Refactoring is not part of the loop. It belongs to review (`sections/review.md`).

## 3. Anti-patterns (reject on sight)

- **Implementation-coupled:** mocks internal collaborators, tests privates, or
  verifies through a side channel. Tell: breaks on refactor with unchanged behavior.
- **Tautological:** asserts the code against itself (`expect(add(a,b)).toBe(a+b)`).
- **Horizontal slicing:** bulk tests for imagined behavior, insensitive to real change.

## 4. Spikes and prototypes

When the question is the design (not the code), build throwaway: one shareable
file for state/logic questions, or several radically different UI variants behind
one toggle. A spike answers its question and is deleted. Anything kept gets
rebuilt through §2. Name the question and the kill test before starting.
