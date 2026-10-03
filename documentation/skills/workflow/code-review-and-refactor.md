Derived from upstream `code-review`, verified at revision `d81f3a1`, and renamed in this fork. The [archived upstream page](../../../.upstream/snapshots/d81f3a1/files/docs/engineering/code-review.md) preserves its provenance.

## What it does

`code-review-and-refactor` reviews one frozen starting diff on two independent tracks, Standards and Specifications. The coordinator checks cited evidence before applying supported refactors, then asks the same reviewers to verify the result. Missing behavior returns to implementation rather than being disguised as a refactor.

The Specifications track checks the originating behavior agreement. That can be a task, shared specifications and requirements, or an explicit user-approved living batch in working state. It does not require a standalone specification.

## When to reach for it

Type `/code-review-and-refactor`, or the agent reaches for it when a task fits. Use it after implementation or on a branch, request, or working diff with a fixed starting point. A report-only request produces findings without edits.

## Common questions

**Does it see uncommitted work?**

Yes. Scoped tracked changes and relevant untracked snapshots enter the frozen starting state. Unrelated local changes stay outside the review.

**What happens when no behavior agreement can be recovered?**

It asks you for the agreement or explicit consent to Standards alone. It does not invent requirements from the code.

**Will repeated review eventually produce no suggestions?**

Not reliably. Smells are judgment calls. This run ends after supported changes are verified or blocked, rather than looping through fresh subjective suggestions.

## It's working if

- Standards and Specifications have separate findings, citations, and dispositions.
- The starting diff, agreement, and evidence stay frozen while edits proceed.
- Open behavior gaps remain visible in working state, and incomplete acceptance is not reported as success.

## Where it fits

This is the review step after [implement](./implement.md) or [implement-all](./implement-all.md), and also a standalone review. [test-driven-development](./test-driven-development.md) handles missing behavior through red/green. [what-is-next](../getting-started/what-is-next.md) maps the whole system.
