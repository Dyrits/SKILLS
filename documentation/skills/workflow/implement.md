Derived from upstream `implement`, verified at revision `d81f3a1`. The [archived upstream page](../../../.upstream/snapshots/d81f3a1/files/docs/engineering/implement.md) preserves its provenance.

## What it does

`implement` builds authorized work and commits it on the current branch. Its input is settled intended behavior, not an invitation to redesign the scope. It accepts shared specifications, a task, or an explicit user-approved living work batch.

It uses test-driven development at agreed seams and independent review before completion. Local documents stay current autonomously, with unfinished acceptance and evidence in `documentation/work-in-progress.md`. Completed authorized agreements and deliveries enter root `CHANGELOG.md` using the format owned by [document](../reference/document.md).

## When to reach for it

You invoke this by typing `/implement`; the agent will not reach for it on its own. Use it when the behavior is agreed and the next step is code. Use [prototype](../shaping/prototype.md) only for a user-approved experiment answering an unresolved design question.

## Common questions

**Do I need a standalone specification or published task?**

No. An explicit approved batch in working state can supply the agreement. Global and capability requirements still apply. A backlog candidate or unresolved draft is not authorization.

**Does passing the test suite mean acceptance is complete?**

Only for the behavior those tests establish. Appearance and interaction may need human judgment. Missing validation remains visible instead of becoming a delivery claim.

## It's working if

- The review can trace intended behavior to the originating agreement.
- The commit includes verified work, and unfinished acceptance has evidence and a resumption pointer.
- Scope conflicts come back to you rather than becoming weaker requirements.

## Where it fits

This is the implementation chain step after [taskify](./taskify.md), following [specify](./specify.md), and before [review-and-refactor](./review-and-refactor.md). Living iteration can reach it directly with an approved batch. [implement-all](./implement-all.md) coordinates parallel work; [guide](../getting-started/guide.md) maps the whole system.
