Fork-created skill with no upstream equivalent, added in commit `b05ce86` (see the [provenance audit](../../research/2026-10-03-retained-skill-provenance.md)).

## What it does

`iterate` builds a living application one verified batch at a time. It settles only the decisions the current batch needs, implements the batch, checks it, and lets the result decide what comes next. The application evolves in place from its first runnable batch; replacing it is your decision.

It coordinates other skills rather than replacing them: [refine](../reference/refine.md) roots its interview in the current batch, [prioritize](../shaping/prioritize.md) picks a focus when scope is tangled, [research](../shaping/research.md) answers external facts, [test-first](./test-first.md) and [debug](../upkeep/debug.md) cover tests and stubborn failures, and [review-and-refactor](./review-and-refactor.md) runs at milestones.

## When to reach for it

You invoke this by typing `/iterate`; the agent will not reach for it on its own. Use it when you want questions, decisions, code, and checks to advance together, for a new idea or an existing project.

Use the planned route (`specify`, `taskify`, `implement`, `review-and-refactor`) when you want separate specification and task documents before code. Both routes share the same project documents, so you can switch between them without losing agreements or progress.

## Working state

`iterate` keeps light records and does not generate feature documents or tasks just to run a batch.

| Document | Holds |
| --- | --- |
| `documentation/backlog.md` | Candidate outcomes, priorities, deferrals, exclusions |
| `documentation/work-in-progress.md` | Current goal, agreed batch, open questions, evidence, next step |
| `CHANGELOG.md` | A Delivery when a meaningful increment passes its checks, an Agreement for a consequential decision |

Existing requirements and specifications are read and respected. [document](../reference/document.md) owns the formats. Corrections and process concerns go to `.agents/feedbacks/` so they survive an interrupted session.

## Common questions

**Does a passing build mean the batch is accepted?**

No. Implemented and checked is kept distinct from accepted by you. Appearance and interaction need your review, grouped into one pass.

**When does it ask me before acting?**

For intended behavior, consequential tradeoffs, paid services, publishing, destructive actions, and replacing the approach. When setup or repeated failures raise cost, it pauses with the blocker and alternatives instead of pushing on.

**Will it break every idea into tasks first?**

No. A clear small change goes straight to a batch. Decomposition through `prioritize` applies only when competing capabilities or dependencies block choosing the next increment, and each new outcome needs its own approval.

**Can I stop and resume later?**

Yes. Working state is updated when a batch is agreed and after it is implemented or reviewed, so no final handoff is needed. On resumption the agent compares the record with the actual code and check results before trusting it.

## It's working if

- Each batch ends with a report of what changed, the verification result, and how to run it.
- `documentation/work-in-progress.md` names the next step and matches the code.
- Unresolved questions stay pending and ruled-out ideas stay apart from deferred ones.
- You are asked to approve behavior and tradeoffs, not routine implementation choices.

## Where it fits

This is the just-in-time alternative to the planned route; it shares project documents with [specify](./specify.md), [taskify](./taskify.md), [implement](./implement.md), and [review-and-refactor](./review-and-refactor.md). [prioritize](../shaping/prioritize.md) is its focus-selection branch. [guide](../getting-started/guide.md) maps the whole system.
