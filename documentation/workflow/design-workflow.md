## What it does

`design-workflow` grills you into a specification for a recurring workflow, using the current directory as a stateful workspace. It runs the standard grilling discipline, but aimed at **loops**: recurring patterns in your work (a morning inbox pass, a weekly review, an onboarding routine) that are predictable enough to delegate. Its output is `workflows/*.md`, one specification per workflow, and its bar is absolute: a specification is done only when an implementer agent could build it without asking a single question.

## When to reach for it

- **Invocation mode.** You invoke this by typing `/design-workflow`, and the agent won't reach for it on its own.
- **Trigger boundary.** Reach for it when a *recurring* activity in your work wants delegating and needs designing: what fires it, where the human checkpoints sit, what the brief shows you. For a one-off piece of engineering, use `grill-with-documentation` instead; `design-workflow` is only for loops you will run again.

## The loop lens

The skill's defining idea is the **loop**: picturing your work as loops within loops reveals which activities are predictable enough to hand off. From that lens come the four vocabulary words a specification may use, mandated nowhere: **trigger** (event or schedule), **checkpoint** (a human decision point), **push right** (do maximal work before involving the human, so they decide once, late, with everything prepared), and **brief** (the decision-ready summary a checkpoint shows you, never the raw output). A workflow that needs none of these is still a workflow: nothing structural is mandated.

## Common questions

**Does every workflow need AI in it?**
No. A workflow is a specification of a loop; whether an agent, a script, or a human runs each step is decided by the grilling, not assumed.

**Where do the specifications live?**
`workflows/*.md` in the workspace you run the skill in, with `NOTES.md` alongside capturing raw notes on your world, tools, channels, and your own terms for them. Thin notes mean the skill interviews you about your world before specifying anything.

## It's working if

- Each finished `workflows/*.md` leaves no open question an implementer would have to ask.
- Checkpoints are pushed as far right as the loop allows, and each one shows you a brief rather than a draft.
- Terms you used loosely at the start have sharpened into canonical ones recorded in `NOTES.md`.

## Where it fits

A **reach-for-it-anytime standalone** on the specification side: it is `grill-with-documentation`'s shape (stateful grilling, a workspace, a paper trail) pointed at recurring operational loops instead of a codebase feature. Its nearest sibling is [grill-with-documentation](./grill-with-documentation.md) (one-off ideas, domain model); its output is consumed by whatever implementer you point at the finished specification. For the map over the whole set, see [what-is-next](../getting-started/what-is-next.md).
