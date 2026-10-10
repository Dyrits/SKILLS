Derived from upstream `implement`, verified at revision `d81f3a1`.

## What it does

`implement` builds authorized work and commits it on the current branch. Its input is settled intended behavior, not an invitation to redesign the scope. It accepts shared specifications, a task, or an explicit user-approved living work batch.

It uses test-driven development at agreed seams, diagnoses a reported bug before editing code, and reports its verification evidence. It carries its own copies of the [test-first](./test-first.md) rules, the [debug](../upkeep/debug.md) diagnosis loop, and the project document contract. Run on its own, it keeps local documents current, with unfinished acceptance and evidence in working state, and records completed authorized agreements and deliveries in the changelog. Handed one task by a coordinating skill, it returns that evidence instead, so parallel implementers never write the same records.

It does not review its own work. The review runs once over the whole batch: [divide-and-conquer](./divide-and-conquer.md) runs it after merging and [iterate](./iterate.md) at its milestones. A standalone run ends with the starting commit, scope, agreement, and evidence a review such as [review-and-refactor](./review-and-refactor.md) starts from; it does not start one.

## When to reach for it

Type `/implement`, or let an agent hand it a task, such as one implementer in a parallel run. Use it when the behavior is agreed and the next step is code. Use [prototype](../shaping/prototype.md) only for a user-approved experiment answering an unresolved design question.

## Common questions

**Why does it not review its own work?**

So a batch gets one review, not one per task. Many parallel implementers each running a full review would multiply the cost without adding coverage, since the review compares the whole batch with its agreement.

**Do I need a standalone specification or published task?**

No. An explicit approved batch in working state can supply the agreement. Global and capability requirements still apply. A backlog candidate or unresolved draft is not authorization.

**Does passing the test suite mean acceptance is complete?**

Only for the behavior those tests establish. Appearance and interaction may need human judgment. Missing validation remains visible instead of becoming a delivery claim.

**What if `webapp-testing` is not installed?**
It ships outside this repository, so the skill cannot assume it. When browser interaction needs verifying and the skill is missing, the agent tells you, verifies the interaction another way (a scripted browser run, for example), and reports the check as could not run if no way is available.

## It's working if

- The final report traces intended behavior to the originating agreement, ready for review.
- The commit includes verified work, and unfinished acceptance has evidence and a resumption pointer.
- Scope conflicts come back to you rather than becoming weaker requirements.

## Where it fits

This is the implementation chain step after [taskify](./taskify.md), following [specify](./specify.md), and before [review-and-refactor](./review-and-refactor.md). [iterate](./iterate.md) carries the same discipline for every batch. [divide-and-conquer](./divide-and-conquer.md) coordinates parallel work.
