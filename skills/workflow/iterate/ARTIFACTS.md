# Working state and feedback

Read this reference when recording agreed work, completing a batch, receiving a correction or process concern, or resuming the workflow. Call the Skill tool with "documentation" for shared project-document rules. Create artifacts lazily in the current project, preserving existing content and following its instructions. Write only useful state; reference existing evidence rather than copying it. Keep secrets and sensitive data out of these files.

## Current work

Use `documentation/work-in-progress.md` as the current working state. Update it when a batch is agreed and after its implementation or review, so an interruption does not depend on a final handoff. Retain:

- The current goal and approved approach, with pointers to lasting decisions and relevant existing requirements or specifications.
- The selected outcome and local backlog heading or authoritative remote link when decomposition was needed; keep grouping and priorities in the backlog rather than duplicating them here.
- Unresolved questions and their dependencies.
- Deferred in-scope work and explicitly out-of-scope ideas, kept distinct.
- Agreed but unfinished behavior, including the current batch and relevant acceptance checks.
- Status of implementation, verification evidence, and user acceptance where needed.
- The current goal's starting revision in a versioned project, plus milestone behavior evidence and review status when that branch applies.
- The next step and any blocker or running assignment that must be reconciled before resumption.

Follow documentation's backlog-authority rule: local projects retain candidates in `documentation/backlog.md`; remote projects keep only the tracker backlog link there. Its entries never authorize implementation. Working state stays local for either tracker, referencing local headings or remote records without duplicating priorities or status. Neither feature specifications nor task documents are required for a batch; link existing relevant requirements rather than generating a new planning hierarchy.

Maintain affected documents autonomously within approved scope. Prune finished working items once their useful information is captured in code, tests, or lasting documentation. Preserve intended behavior that those artifacts cannot express in a focused document under `documentation/`. Keep consequential choices and reasons in `documentation/architecture-decision-record/`. When available, call the Skill tool with "domain-modeling" for recording those decisions. Otherwise, record the choice, alternatives, reasons, and consequences only when a real tradeoff is costly to reverse and surprising without context. Resolve consequential scope or obligation conflicts before proceeding; never weaken requirements to make current implementation appear complete.

On resumption, compare the working document with actual code and check results. Resolve discrepancies before treating its status as current. Read relevant artifacts, not every historical feedback record. This is live working state; an explicit user-invoked `hand-off` can reference it and add session-specific context.

## Project-wide history

Use the root `CHANGELOG.md` for relevant authorized decisions and completed delivery, not one entry for every mechanical edit. Apply the entry format, fields, and vocabulary supplied by "documentation".

An Agreement records an authorized decision. A Delivery records completed relevant checks and acceptance, including any required human judgment. Keep unfinished batches, missing verification, blockers, and assignments in working state. Reference evidence and relevant requirements without treating a backlog proposal or a passing build as authorization or acceptance.

## Automatic feedback

Use `.agents/feedbacks/` when the user corrects the agent, its approach goes off course, or the user expresses uncertainty about the process. Capture the observation promptly, independently of whether a batch is complete, so it survives an interrupted session.

Use a descriptive filename, such as `2026-05-20-rebuild-lost-approved-interaction.md`; update the same record for repeated observations about the same problem. Separate unrelated concerns. Each record contains:

- **Context and evidence**: the relevant task, batch, and artifact or session references. Include the user's correction or concern faithfully.
- **Observation**: what is confirmed, what is uncertain, and any suspected cause clearly labeled as a hypothesis.
- **Response**: what the agent changed, or what remains open.
- **External follow-up**, when applicable: the reusable skill, tool, or process concerned and a proposed correction if supported by evidence.

Record ordinary product corrections as product feedback. Identify a reusable workflow problem only when the evidence supports that distinction. User uncertainty is an open concern, not a verdict that the workflow is defective.

Tell the user briefly when a record is created or materially updated. Capture sufficient evidence from the current work without launching an unrelated investigation. Continue the application task; review and changes to external skills or tools belong in a separate session in their target repository. Refer to the relevant record when transferring that follow-up.
