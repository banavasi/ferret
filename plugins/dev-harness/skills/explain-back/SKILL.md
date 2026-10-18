---
name: explain-back
description: Make sure I actually understand code the AI wrote for me before I ship it. Explains the change visually, then quizzes me and grades my answers honestly. Use for "/explain-back", "explain what you did", "I don't understand this code", "teach me this", "what did the AI change", or before merging AI-written code.
---

# Explain back

Goal: the user can defend this code in a PR review without the AI in the room. Explaining is not enough. The user must explain it back.

## Steps

1. **Find the scope.** Default: the current uncommitted diff plus commits on this branch not on `main` (`git diff main...HEAD` and `git diff`). Or what the user names.

2. **Map it (visual first).** Use the `diagram` skill. Draw the flow the change takes part in, with the changed parts highlighted. Then give:
   - **What it does** — 2 sentences.
   - **Why this way** — the design choice and the main alternative that was not taken.
   - **Concepts you need** — list each framework or language concept the code depends on (for example "Laravel service container binding", "Eloquent eager loading", "CSRF middleware"). One line each.
   - **Where it can break** — the top 3 failure modes, with the line that would fail.

3. **Quiz.** Ask 3-5 questions, **one at a time**, wait for the answer each time. Mix:
   - Trace: "A request with an expired token hits line X. What happens next?"
   - Change: "Product wants this to also handle Y. Which file do you touch?"
   - Break: "What happens if this query returns zero rows?"
   - Why: "Why is this in a job and not in the controller?"
   Do not ask questions answerable by reading the line aloud.

4. **Grade honestly.** For each answer: `correct` / `partly` / `wrong`, then the precise gap. No softening. "Close" is not a grade.

5. **Verdict:**
   - **Ready to ship** — all correct or partly-correct with minor gaps.
   - **Not ready** — any wrong answer on a trace or break question. Say: "You can't defend this in review yet." Re-explain only the gap, with a smaller diagram, and re-ask that one question.

6. **Log it.** Append each concept the user got wrong or did not know to `~/dev-journal/learned.md` (see the `journal` skill). Offer to add an "AI did / I did" note to today's log.

## Rules
- Never answer your own quiz question in the same message you ask it.
- If the user says "just explain it, skip the quiz", do it, but state once: "Skipping the check means you're trusting code you haven't verified you understand." Then respect their choice.
- If, while explaining, you find the code is wrong or overbuilt, say so before the quiz. Understanding bad code is not the goal.
