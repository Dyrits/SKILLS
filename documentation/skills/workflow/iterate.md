Fork-created skill with no upstream equivalent, added in commit `b05ce86` (see the [provenance audit](../../research/2026-10-03-retained-skill-provenance.md)).

## What it does

`iterate` builds a living application one verified batch at a time. It settles only the decisions the current batch needs, implements the batch, checks it, and lets the result decide what comes next. The application evolves in place from its first runnable batch; replacing it is your decision.

It carries its own copies of the disciplines it needs, so it runs with no other skill installed: the [interview](../shaping/interview.md) method rooted in the current batch, [prioritize](../shaping/prioritize.md) for picking a focus when scope is tangled, [research](../shaping/research.md) for external facts, [implement](./implement.md) for each settled batch (with the [test-first](./test-first.md) rules and the [debug](../upkeep/debug.md) loop), [divide-and-conquer](./divide-and-conquer.md) for a batch that splits into independent tasks, after you approve its routing table, and [review-and-refactor](./review-and-refactor.md) at milestones.

## When to reach for it

Type `/iterate`, or an agent can reach for it when the task fits. Use it when you want questions, decisions, code, and checks to advance together, for a new idea or an existing project.

Use the planned route (`specify`, `taskify`, `implement`, `review-and-refactor`) when you want separate specification and task documents before code. Both routes share the same project documents, so you can switch between them without losing agreements or progress.

## Working state

`iterate` keeps light records and does not generate capability documents or tasks just to run a batch.

| Document (default location) | Holds |
| --- | --- |
| `documentation/backlog.md` | Candidate outcomes, priorities, deferrals, exclusions |
| `documentation/work-in-progress.md` | Current goal, agreed batch, open questions, evidence, next step |
| Changelog | A Delivery when a meaningful increment passes its checks, an Agreement for a consequential decision |

Paths are defaults: the skill first uses the document `AGENTS.md` names. When there is none, it adopts an existing home of that kind in your project, creates one at the default only when nothing matches, never overwrites an existing file, matches the naming and style of the documents it finds, and adds its line to `AGENTS.md`.

Existing requirements and specifications are read and respected. The skill carries the formats it writes.

## Common questions

**Does a passing build mean the batch is accepted?**

No. Implemented and checked is kept distinct from accepted by you. Appearance and interaction need your review, grouped into one pass.

**When does it ask me before acting?**

For intended behavior, consequential tradeoffs, paid services, publishing, destructive actions, and replacing the approach. When setup or repeated failures raise cost, it pauses with the blocker and alternatives instead of pushing on.

**Will it break every idea into tasks first?**

No. A clear small change goes straight to a batch. Choosing a focus first applies only when competing capabilities or dependencies block choosing the next increment, and each new outcome needs its own approval.

**Can I stop and resume later?**

Yes. Working state is updated when a batch is agreed and after it is implemented or reviewed, so no final handoff is needed. On resumption the agent compares the record with the actual code and check results before trusting it.

## It's working if

- Each batch ends with a report of what changed, the verification result, and how to run it.
- Working state names the next step and matches the code.
- The changelog gains a Delivery for each completed increment and an Agreement for each consequential choice, such as a tool or a direction that is costly to reverse.
- A bug you report is reproduced before any fix lands.
- Unresolved questions stay pending and ruled-out ideas stay apart from deferred ones.
- You are asked to approve behavior and tradeoffs, not routine implementation choices.

## Where it fits

This is the just-in-time alternative to the planned route; it shares project documents with [specify](./specify.md), [taskify](./taskify.md), and [review-and-refactor](./review-and-refactor.md), and builds every batch with its own copy of [implement](./implement.md). Its focus-selection branch is a copy of [prioritize](../shaping/prioritize.md). [guide](../productivity/guide.md) maps the whole system.
