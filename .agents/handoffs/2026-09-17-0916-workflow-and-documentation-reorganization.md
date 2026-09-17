# Workflow and documentation reorganization

Supersedes: `.agents/handoffs/2026-09-17-0901-setup-and-documentation-rework.md`

## Current state

The complete reorganization and setup workflow change set is ready to commit on `main`. The user explicitly requested that this handoff be written, then that all changes be committed and pushed to `origin`; inspect `git log` and `origin/main` for the resulting commit because those operations occur after this document is written.

The source of truth is the full diff from `f85ffd7` plus the artifacts named below. Existing work from both earlier handoffs was preserved and extended rather than recreated.

## Decisions and completed changes

- `skills/flow/` is now `skills/workflow/`, with promoted documentation mirrored under `documentation/workflow/` and every manifest, link, script, repository instruction, changelog entry, changeset, and handoff reference updated.
- `skills/in-progress/` is now `skills/work-in-progress/`; it remains public, locally linked, excluded from the plugin, and without promoted documentation pages.
- Repository architecture decisions now live under `documentation/architecture-decision-record/`; the old `.agents/adr/` files were moved there and the domain-modeling convention no longer creates `docs/adr/`.
- `skills/reference/domain-modeling/ADR-FORMAT.md` is now `ARCHITECTURE-DECISION-RECORD-FORMAT.md` and its callers use the expanded name.
- `CLAUDE.md` now carries the repository-wide language convention: prefer full words such as repository, document or documentation, specification, and architecture decision record, with exceptions for literal external names, commands, APIs, URLs, established technical terms, and defined repeated abbreviations. `AGENTS.md` is a symlink to `CLAUDE.md`, so both harnesses receive the rule.
- `setup-custom-skills` supports GitHub, GitLab, Jira, local markdown, optional local refinement drafts, and an optional ticket-writing convention. It can point at a repository template or ticket-writing skill such as `create-jira-ticket` without making that skill mandatory or handing it control of decomposition and publication.
- `to-tickets` confirms the configured ticket-writing convention, keeps its built-in format as a fallback, and retains ownership of tracer-bullet decomposition, blocking edges, approval, and the local-versus-published boundary.
- `to-spec` was renamed to `to-specifications`, and generated specification artifacts use `specification.md`.
- Active repository prose and paths use `documentation` rather than a local `docs` directory. No `docs/` directory exists.
- Local Claude and Codex skill symlinks were refreshed with `scripts/link-skills.sh` and point at the renamed bucket paths.

## Primary artifacts

- Repository agreements: `CLAUDE.md`
- Plugin manifest: `.claude-plugin/plugin.json`
- Setup workflow: `skills/getting-started/setup-custom-skills/SKILL.md`
- Jira setup seed: `skills/getting-started/setup-custom-skills/issue-tracker-jira.md`
- Ticket workflow: `skills/workflow/to-tickets/SKILL.md`
- Specification workflow: `skills/workflow/to-specifications/SKILL.md`
- Domain-modeling workflow: `skills/reference/domain-modeling/SKILL.md`
- Architecture decision record format: `skills/reference/domain-modeling/ARCHITECTURE-DECISION-RECORD-FORMAT.md`
- Architecture decisions: `documentation/architecture-decision-record/`
- Router: `skills/getting-started/what-is-next/SKILL.md`

## Verification completed

- `git diff --check` passes.
- `claude plugin validate . --strict` passes.
- Every maintained relative Markdown link resolves when illustrative links inside code examples are excluded.
- Searches find no active references to `skills/flow`, `documentation/flow`, `skills/in-progress`, `documentation/in-progress`, `docs/adr/`, `docs/agents/`, `.agents/adr/`, or `ADR-FORMAT`.
- `documentation/architecture-decision-record/` contains both existing repository decisions.
- Local Claude and Codex symlinks resolve to `skills/workflow/` and `skills/work-in-progress/`.

## What is next

1. Confirm the requested commit and push completed by inspecting `git status`, `git log -1`, and `origin/main`.
2. Review the consolidated commit if further editorial cleanup is desired; the broad terminology and path changes are intentional.
3. Decide later whether the plugin identifiers `mattpocock-skills` and marketplace name `mattpocock` should change for the fork. They remain unchanged for compatibility.

## Suggested skills

- Call the Skill tool with `takeover` when resuming from this handoff.
- Call the Skill tool with `code-review` for a two-axis review of the consolidated commit against `f85ffd7`.
- Call the Skill tool with `writing-for-agents` before further edits to skills or repository instructions.
