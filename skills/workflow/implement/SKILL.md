---
name: implement
description: "Implement authorized work from specifications, tasks, or an agreed living work batch."
disable-model-invocation: true
---

Call the Skill tool with "document"; its terms (authorized, obligation, lazy, pointer) and rules apply throughout.

Identify the authorized behavior and its originating agreement: a task, specifications with their requirements, or a user-approved batch in `documentation/work-in-progress.md`. Read the applicable requirements. Record the starting commit and work scope for review.

Call the Skill tool with "test-first" where possible, at pre-agreed seams. Run typechecking and individual test files regularly, and the full test suite once at the end. Verify acceptance against the originating agreement, including appearance and interaction evidence when human judgment is needed, and state which checks passed, failed, or could not run.

Keep `documentation/work-in-progress.md` current with unfinished work, evidence, blockers, and resumption pointers.

Call the Skill tool with "review-and-refactor" with the starting commit, scope, originating agreement, and verification evidence. Commit the work to the current branch, and record completed agreements and deliveries in the root `CHANGELOG.md`; unfinished acceptance stays in working state.
