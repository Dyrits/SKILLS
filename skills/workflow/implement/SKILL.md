---
name: implement
description: "Implement authorized work from specifications, tasks, or an agreed living work batch."
disable-model-invocation: true
---

Call the Skill tool with "documentation" for the shared project-document model before reading or updating work records.

Identify the authorized intended behavior and its originating agreement. Accept a task, shared specifications and requirements, or an explicit user-approved batch recorded in working state. A living iteration can operate from `documentation/backlog.md` and `documentation/work-in-progress.md` without creating feature specifications or tasks. Recover historical inputs where needed; preserve them rather than automatically migrating them.

Read applicable global and feature requirements. Resolve consequential scope or obligation conflicts with the user; never silently weaken requirements. Record the starting commit and work scope for review.

Call the Skill tool with "test-driven-development" where possible, at pre-agreed seams. Run typechecking and individual test files regularly, and the full test suite once at the end. Verify acceptance against the originating agreement, including appearance and interaction evidence when human judgment is needed. Distinguish passing checks from missing or blocked validation.

Maintain unfinished work, evidence, blockers, assignments, and resumption pointers in `documentation/work-in-progress.md` autonomously. Keep agreed behavior and local task records current under the shared model. After authorized publication, the remote tracker is authoritative for tasks; local task files are title/link pointers.

Call the Skill tool with "code-review-and-refactor" with the starting commit, scope, originating agreement, and verification evidence. Commit the work to the current branch. Automatically record completed authorized agreements and deliveries in root `CHANGELOG.md` using the format owned by "documentation"; leave unfinished acceptance visible in working state.
