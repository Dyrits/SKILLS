Derived from upstream `tdd`, renamed `test-first` in this fork, verified at revision `d81f3a1` at `skills/engineering/tdd/SKILL.md`. The [upstream port record](../../../.upstream/sync/2026-09-30.md) records its maintained counterpart.

## What it does

`test-first` builds behavior through a red/green loop at agreed seams. A seam is a public boundary where a test observes behavior without inspecting implementation details. One failing test and one minimal implementation form each vertical slice.

Expected results come from an independent originating agreement, not from restating the implementation. Shared requirements and specifications, tasks, or an approved living work batch can supply that agreement.

## When to reach for it

Type `/test-first`, or the agent reaches for it when a task fits. Use it for concrete behavior with an observable public boundary and an independent expected result. Agree the seams before writing tests.

## Common questions

**Can I use it without a full specification?**

Yes. An approved working-state agreement can establish the behavior. An unresolved draft or unapproved backlog candidate cannot.

**Should every change get a test?**

No. Tests need a useful seam and an independent expected result. Appearance and interaction may also need human acceptance; a passing suite cannot establish judgments it never exercises.

**What if a skill it calls is not installed?**
It names the missing skill with its install command, carries out that step from its stated intent, and tells you the step ran without it. Without `document` it waits instead, because its rules use that skill's terms: install it, or tell it to proceed anyway. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/workflow/test-first/SKILL.md).

## It's working if

- A new test fails for the expected missing behavior before implementation.
- Tests survive structural refactors because they observe public behavior.
- Unfinished cycles and verification gaps remain visible in working state.

## Where it fits

This is implementation machinery used by [implement](./implement.md) and [divide-and-conquer](./divide-and-conquer.md). [review-and-refactor](./review-and-refactor.md) follows red/green and handles structural refactoring. [guide](../getting-started/guide.md) maps the other routes.
