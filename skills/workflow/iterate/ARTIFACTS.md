# Working state and feedback

Read this when recording agreed work, completing a batch, receiving a correction or process concern, or resuming. The "document" rules apply. Write only useful state, with pointers to existing evidence. Keep secrets and sensitive data out of these files.

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

On resumption, compare working state with the actual code and check results, and resolve discrepancies before trusting its status. Read the relevant records rather than the whole feedback history. A user-invoked `hand-off` can point at this file and add session context.

## Project-wide history

Use light records in the root `CHANGELOG.md`: a Delivery when a goal or meaningful increment passes its checks and any required acceptance, and an Agreement only for a consequential decision. Unfinished batches, missing verification, blockers, and assignments stay in working state.

## Automatic feedback

Use `.agents/feedbacks/` when the user corrects the agent, its approach goes off course, or the user expresses uncertainty about the process. Capture the observation promptly, whether or not a batch is complete, so it survives an interrupted session.

Use a descriptive filename, such as `2026-05-20-rebuild-lost-approved-interaction.md`, and update the same record for repeated observations about the same problem. Separate unrelated concerns. Each record contains:

- **Context and evidence**: the task, batch, and artifact or session references, with the user's correction or concern quoted faithfully.
- **Observation**: what is confirmed, what is uncertain, and any suspected cause labeled as a hypothesis.
- **Response**: what the agent changed, or what remains open.
- **External follow-up**, when applicable: the reusable skill, tool, or process concerned, and a proposed correction if the evidence supports one.

Record ordinary product corrections as product feedback; name a reusable workflow problem when the evidence supports that distinction. User uncertainty is an open concern, still unproven as a workflow defect.

Tell the user briefly when a record is created or materially updated. Capture enough evidence from the current work and continue the application task; changes to external skills or tools belong to a separate session in their own repository, with a pointer to the record.
