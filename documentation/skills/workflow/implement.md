Derived from upstream `implement`, verified at revision `d81f3a1`. The [archived upstream page](../../../.upstream/snapshots/d81f3a1/files/docs/engineering/implement.md) preserves its provenance.

## What it does

`implement` builds authorized work and commits it on the current branch. Its input is settled intended behavior, not an invitation to redesign the scope. It accepts shared specifications, a task, or an explicit user-approved living work batch.

It uses test-driven development at agreed seams, diagnoses a reported bug through [debug](../upkeep/debug.md) before editing code, and reports its verification evidence. Run on its own, it keeps local documents current, with unfinished acceptance and evidence in `documentation/work-in-progress.md`, and records completed authorized agreements and deliveries in root `CHANGELOG.md` using the format owned by [document](../reference/document.md). Handed one task by a coordinating skill, it returns that evidence instead, so parallel implementers never write the same records.

It does not review its own work. The review runs once over the whole batch: [divide-and-conquer](./divide-and-conquer.md) runs it after merging, [iterate](./iterate.md) at its milestones, and a standalone run ends by recommending [review-and-refactor](./review-and-refactor.md).

## When to reach for it

Type `/implement`, or let a coordinating skill hand it a task. Use it when the behavior is agreed and the next step is code. Use [prototype](../shaping/prototype.md) only for a user-approved experiment answering an unresolved design question.

## Common questions

**Why does it not review its own work?**

So a batch gets one review, not one per task. Many parallel implementers each running a full review would multiply the cost without adding coverage, since the review compares the whole batch with its agreement.

**Do I need a standalone specification or published task?**

No. An explicit approved batch in working state can supply the agreement. Global and capability requirements still apply. A backlog candidate or unresolved draft is not authorization.

**Does passing the test suite mean acceptance is complete?**

Only for the behavior those tests establish. Appearance and interaction may need human judgment. Missing validation remains visible instead of becoming a delivery claim.

## It's working if

- The final report traces intended behavior to the originating agreement, ready for review.
- The commit includes verified work, and unfinished acceptance has evidence and a resumption pointer.
- Scope conflicts come back to you rather than becoming weaker requirements.

## Where it fits

This is the implementation chain step after [taskify](./taskify.md), following [specify](./specify.md), and before [review-and-refactor](./review-and-refactor.md). [iterate](./iterate.md) calls it for every batch. [divide-and-conquer](./divide-and-conquer.md) coordinates parallel work; [guide](../getting-started/guide.md) maps the whole system.
