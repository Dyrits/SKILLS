# Share project documents across development workflows

Planned development and just-in-time iteration use one project-owned document model. The former interviewing, specification-snapshot, refinement-draft, and iterative-state conventions could give the same behavior multiple competing homes and made changing workflows require translating context. We keep the different development pacing but share document authority, with the format owned by the `documentation` skill.

Global and feature requirements record constraints. Repository specifications record evolving agreed behavior and design; unresolved proposals remain drafts. Local tasks contain their bodies, while published remote tasks leave local references to their authoritative tracker records. The project backlog records candidates rather than authorization, working state records unfinished execution and resumption, and root `CHANGELOG.md` distinguishes authorized agreements from validated deliveries.

For local tracking, `documentation/backlog.md` holds the backlog. For remote tracking, candidate priorities and deferrals belong in the configured tracker and that file is only its local entry point. Working state remains local for current agreements, running assignments, verification, blockers, and recovery, linking rather than copying remote status. Pending publication is explicit and does not establish a competing local queue.

`iterate` can operate from backlog, working state, and changelog without creating feature specifications or tasks for every batch. Existing relevant constraints and agreements still apply. Autonomous document maintenance does not authorize weakening an obligation or silently expanding scope. Scoped prototypes can feed production implementation after appropriate acceptance and checks, without mandatory rebuilding.

The alternative was to retain workflow-specific artifacts with translation rules or synchronized copies. That would preserve the old conventions but leave ambiguity about which agreement was current. The shared model replaces `.refinement/` and the local `backlog/` tracker layout for future work; existing histories are preserved and conflicts are surfaced before migration. Remote publication remains a separately authorized action.

Skills are organized by purpose. Removing the experimental bucket does not promote its former contents, since the plugin manifest determines publication per skill. Upstream archives and historical handoffs retain their original names; current skill pages state verified provenance and explain consequential drift.
