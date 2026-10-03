# The spike README skeleton

Copy this into `studies/<slug>/README.md`. Write the body first (everything
below the Outcome line); add the Outcome block last, when you know the answer.
Not every section is mandatory — drop what a given spike doesn't need — but the
Question, Method, Results and Reproducing always earn their place.

```markdown
# <Spike title>

> **Outcome (<YYYY-MM-DD>). <SHIPPED | DISPROVED | PARKED> <for what>.**
> One or two sentences: what the answer is, and what happens next — the commit
> that ported it, the issue it's parked in (#N), or why nothing was built.
> If a reusable byproduct survived the throwaway (a utility, a measurement, a
> finding that became a rule), name it here so it isn't lost.

**Question.** The one thing this spike is here to answer, in plain terms —
what's uncertain, and what deciding it changes.

**Why it looked promising.** The reason this was worth the time: the data
already existed, the effect was visible in one sample, the alternative is
expensive. State it so a reader can judge whether the premise held.

## Method

The scripts, named. What each measures or renders and off which inputs, and any
choice that matters (e.g. which artefact was measured, and why that one).
Enough that the Reproducing section is just the commands.

## Results / Findings

What actually happened, with numbers where there are numbers. For a
choose-a-direction spike, describe each direction against the others. Don't
round a negative up — a DISPROVED result stated flatly is the point.

## Recommendation

What to do about it. For a comparison, which direction and why. For a
disproven idea, state plainly that nothing should be built on it, and — if it
matters — why, so nobody retries the same idea.

## Open questions

What this did not settle, and what a follow-up spike would need.

## Reproducing

The exact commands to regenerate the output from scratch.

## Unrelated defects noticed

Anything real the spike happened to surface that belongs elsewhere — filed, or
noted for filing. Optional, but cheap insurance.
```
