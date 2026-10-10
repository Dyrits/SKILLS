Derived from upstream `tdd`, renamed `test-first` in this fork, verified at revision `d81f3a1` at `skills/engineering/tdd/SKILL.md`.

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

## It's working if

- A new test fails for the expected missing behavior before implementation.
- Tests survive structural refactors because they observe public behavior.
- Unfinished cycles and verification gaps remain visible in working state.

## Where it fits

This is implementation machinery: [implement](./implement.md), [divide-and-conquer](./divide-and-conquer.md), [iterate](./iterate.md), and [address-feedback](./address-feedback.md) each carry a copy of these rules. [review-and-refactor](./review-and-refactor.md) follows red/green and handles structural refactoring.
