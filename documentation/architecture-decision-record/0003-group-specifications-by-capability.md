# Group specifications by capability

Specifications, drafts, capability requirements, maps, and tasks live under `documentation/capabilities/<capability>/`, where a capability is anything with lasting agreed behavior: a user-facing feature, an integration, an infrastructure area, or a concern such as performance or security. The earlier `documentation/<feature>/` placeholder had no naming rule, could collide with folders the skills own (`agents/`, `architecture-decision-record/`, `out-of-scope/`), and sat beside a separate `documentation/<effort>/` tree for `graphify` with the same layout.

A parent folder removes the collisions without a list of reserved names. It is named after what persists rather than after the work: a bugfix or chore is a task under the capability it changes, so one area's behavior keeps one specification instead of spreading across folders that go stale once their work ships. An undecided `graphify` effort lives in the folder of the capability it will become, so nothing moves when its decisions settle.

## Considered options

- **`documentation/features/<feature>/`**: familiar and cheap to adopt, but not every piece of work is a feature, and the name invites one folder per bugfix.
- **`documentation/units-of-work/<unit>/`**: names the transient work instead of the lasting behavior, duplicates the role of `tasks/`, and collides with the Unit of Work persistence pattern.
- **Reserved names under `documentation/`**: no rename, but every project must remember a list that grows with each new skill-owned folder.

## Consequences

Folder names are kebab-case glossary terms, flat, and fixed once referenced; the rules live in the `document` skill's `PROJECT-DOCUMENTS.md`. Projects with existing folders directly under `documentation/` keep reading them in place and move them only with approval.
