---
name: spike
description: The throwaway experiment that answers one uncertain or expensive question BEFORE it becomes production code — a self-contained spike in a studies/ subfolder that renders a comparison the user chooses from, then records its verdict so nobody retries a dead end. Use when the user wants to explore or spike a direction, try several directions and choose one, test whether an idea holds up, or settle an open question before anything lands in the production tree. Use only in repos that have no study or spike skill of their own — a project-specific one always wins. Ends with a hoisted Outcome and the verdict parked where it will be found again.
---

# Running a spike

A spike is a question you can't answer by thinking, sized so the answer is
cheap next to building the wrong thing. It lives in `studies/<slug>/`, outside
the production tree, and stays there until the user chooses a direction.

Half the value is a **no**. A spike that ends DISPROVED — nothing built, and a
README that stops the next person retrying it — can be the most useful thing
you did that day. Disproving a method often surfaces the real answer next to
it, and that answer is what graduates.

## When it's a spike (and when it isn't)

- **One question, stated up front.** If you can't write the question and why
  it looked promising, you're building, not spiking.
- **The answer is uncertain or expensive to be wrong about.** Known answer →
  just build it. No spike.
- **The deliverable is a comparison the user chooses from**, not a finished
  feature. Render the directions side by side, let them choose, *then* port.
  This applies hardest to feel — UI motion, wording, visual density — where an
  argument in prose settles nothing and two rendered options settle it in
  seconds.

## The shape

1. **Spike in `studies/<slug>/`.** Self-contained: its own build scripts, its
   own throwaway data. Never wire it into the production tree while it's a
   spike. Heavy output goes in `out/` and may be `.gitignore`d per spike; the
   `README.md` and the build scripts are the committed record.
2. **Render the comparison.** The payoff is something the user can look at or
   measure — an `out/study.html` laying variants side by side, a comparison
   sheet, a table with numbers. Build the thing that makes the choice obvious.
   EVERY artefact the spike produces goes on that one sheet the moment it
   exists: a loose file in `out/` mentioned only in conversation is invisible.
   A follow-up pass goes on the same sheet, not beside it.
3. **Write the README as you go** — the skeleton is in
   [template.md](template.md). Question → why it looked promising → Method
   (exact scripts) → Results with numbers → Recommendation → Reproducing.
4. **Hand over the comparison and stop.** The choice is the user's. Present
   the directions; don't port the winner unprompted.
5. **Hoist the Outcome.** When it concludes, prepend a dated `>` blockquote to
   the top of the README with the verdict in the first two words —
   **SHIPPED**, **DISPROVED**, or **PARKED** — plus one sentence on what
   happens next. A future reader sees the verdict before the question.

   This is the step that gets skipped, and a stale README that still reads as
   an open question will later be mistaken for current. While a spike is still
   running, say so with `Status` in the same position.
6. **Park it where it'll be found.** Open or parked direction → an issue,
   linked from the README. Graduated → the commit that ported it. Either way,
   leave a note wherever this project keeps decisions, so the verdict is
   recalled next session instead of re-derived.

## Hard boundaries

- **Porting the winner is the user's call.** Comparison → they choose → then
  build. Never graduate a result unprompted.
- **Never delete a disproven spike.** The DISPROVED README is what stops the
  retry. Hoist the verdict; keep the reasoning.
- **Salvage what outlives the verdict.** If the spike needed a real utility to
  run, name it in the Outcome so it isn't thrown away with the throwaway.
- **What graduates gets rewritten, not copied.** Spike code is allowed to be
  ugly and unreviewed; the same thing landing in the production tree goes
  through whatever gates that tree has. A spike finding is not a review.
- **A spike is a record, not a plan.** It's kept because the reasoning
  outlives the work. Don't update it to match later reality; write the next
  spike.
