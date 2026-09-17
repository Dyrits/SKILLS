## Refinement workspace

Every repository refines locally before it publishes, whatever its tracker.

- One workspace per source issue at `.refinement/<issue-key>/`, or `.refinement/<feature-slug>/` when no issue exists yet.
- The refined specification lives at `specification.md`; draft implementation tickets live under `issues/` as one file per ticket, numbered from `01`.
- Every draft carries `Status: draft`. A draft sourced from the tracker also carries `Source: <issue-key> (<url or repository-relative ticket path>)` at the top of `specification.md`.
- Interviews, exploratory catalogues, working playtest notes, and draft specifications or tickets stay in this workspace. A reference from a published issue does not promote a working note into the tracker.
- Reading the tracker is always allowed through the configured access method. Creating or updating its records is the **publication boundary**, crossed only on an explicit request from the user ("publish", "create the issue", "update Jira").
- Publication writes the selected specification or tickets to the tracker, then links each draft to the record it produced. Supporting notes stay in refinement.
- A tracker with its own refinement, analysis, or grooming status does not replace this workspace. Draft here, then publish into that status.
