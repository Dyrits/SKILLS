## Project documents and publication

Call the Skill tool with "documentation" before reading or updating the shared project-document model. It owns canonical document roles, lazy creation, requirements constraints, authority, resumption, and the root `CHANGELOG.md` format.

Future feature work uses `documentation/<feature>/`: optional `requirements.md` for constraints, `specifications.md` for canonical living behavior/design/acceptance, `draft.md` for unresolved proposals, and `tasks/<task>.md` for local bodies or title/link references to authoritative published remote tasks.

The project-level `documentation/requirements.md` holds global obligations. Apply documentation's configured backlog authority: local tracking keeps candidate priorities and deferrals in `documentation/backlog.md`; remote tracking keeps only the verified backlog name/link there. `documentation/work-in-progress.md` stays local for active execution, pending publication, and resumption, not duplicated remote status. Create each only when useful and link authoritative material instead of copying it.

Repository specifications remain authoritative. Remote records link to or summarize them rather than becoming a competing specification. Updating local documentation within scope is autonomous; creating or updating remote records requires an explicit user request. Reading the remote is allowed through the configured access method.

Use this tree for future work. Existing `.refinement/` and `backlog/` history stays in place unless migration is separately requested.
