# Working state

Read this when recording agreed work, completing a batch, or resuming. The "document" rules apply. Write only useful state, with pointers to existing evidence. Keep secrets and sensitive data out of these files.

## Current work

`documentation/work-in-progress.md` is the working state. Update it when a batch is agreed and after its implementation or review, so an interruption needs no final handoff. Keep:

- The current goal and approved approach, with pointers to lasting decisions and relevant requirements or specifications.
- The selected outcome's backlog heading or remote pointer when decomposition was needed; priorities stay in the backlog.
- Open questions and their dependencies.
- Deferred in-scope work and explicitly out-of-scope ideas, kept apart.
- Agreed but unfinished behavior, including the current batch and its acceptance checks.
- Status of implementation, verification evidence, and user acceptance where needed.
- The goal's starting revision in a versioned project, plus milestone behavior evidence and review status when that branch applies.
- The next step and any blocker or running assignment to reconcile before resuming.

Prune finished items once code, tests, or lasting documentation captures them. Intended behavior those cannot express goes into a focused document under `documentation/`. Call the Skill tool with "model-domain" to record a consequential choice in `documentation/architecture-decision-record/`.

On resumption, compare working state with the actual code and check results, and resolve discrepancies before trusting its status. A user-invoked `hand-off` can point at this file and add session context.

## Project-wide history

Use light records in the root `CHANGELOG.md`: a Delivery when a goal or meaningful increment passes its checks and any required acceptance, and an Agreement only for a consequential decision. Unfinished batches, missing verification, blockers, and assignments stay in working state.
