# Skills repository fork rework, session 2

Supersedes: `.agents/handoffs/2026-09-17-0010-fork-rework-session-1.md`

## Current state

All work in this session is uncommitted on `main`; `HEAD` and `origin/main` remain at `f85ffd7` (`Reorganize skills into new buckets and update plugin manifest`). The working tree contains the complete change set described below, including the earlier session's path cleanup and the new handoff file.

The diff is large because the user asked to remove abbreviated `spec` and `repo` prose throughout maintained files and to remove the external AI Hero documentation dependency. Review the actual diff rather than recreating any part of it.

## Decisions made

- `documentation/agents/` is the durable per-repository configuration location; the former generated location is gone from active material.
- A remote tracker such as Jira remains the system of record, while optional refinement drafts live under `.scratch/<issue-key>/` until the user explicitly publishes them.
- Jira is a first-class setup option. An available MCP connector, CLI, or REST workflow must pass a read-only access check before setup describes access as automated; otherwise publication is manual.
- `to-spec` was renamed to `to-specifications`, including the skill directory, frontmatter, metadata, plugin entry, documentation page, router, README references, and local installed links.
- Local specification artifacts are named `specification.md` rather than `spec.md`.
- Maintained prose uses `repository` and `specification` instead of `repo` and `spec`; literal API paths, external identifiers, and historical names are retained only where required for correctness or explanation.
- AI Hero is not a publication target or documentation dependency for this fork. The sole remaining `aihero.dev` reference is the origin statement in the top-level `README.md`, which says this repository began from that source and now intentionally diverges.
- Repository documentation now uses relative links. `.agents/writing-docs.md` no longer requires external AI Hero skill links, an external dictionary, or site-rendered installation widgets.
- Plugin metadata now names Dylan J. Gerrits and `https://github.com/Dyrits/SKILLS`; the plugin and marketplace identifiers themselves remain `mattpocock-skills` and `mattpocock` for now.

## Primary artifacts

- Setup workflow: `skills/getting-started/setup-custom-skills/SKILL.md`
- New Jira template: `skills/getting-started/setup-custom-skills/issue-tracker-jira.md`
- Renamed specification skill: `skills/workflow/to-specifications/SKILL.md`
- Draft-aware ticket workflow: `skills/workflow/to-tickets/SKILL.md`
- Router: `skills/getting-started/what-is-next/SKILL.md`
- Documentation rules: `.agents/writing-docs.md`
- Repository attribution and installation copy: `README.md`
- Plugin manifests: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`
- The complete source of truth is the uncommitted `git diff` against `f85ffd7`.

## Local installation state

`scripts/link-skills.sh` was run successfully after the rename. Both `~/.agents/skills/to-specifications` and `~/.claude/skills/to-specifications` point at this repository.

The stale old installations were moved, not deleted, to `/private/tmp/to-spec-rename-backup-20260917/` as `agents-to-spec` and `claude-to-spec`.

## Verification already completed

- `git diff --check` passes.
- `claude plugin validate . --strict` passes.
- A repository-relative Markdown link check over `documentation/` and `.agents/` passes.
- A hidden-file search finds exactly one remaining AI Hero reference: the explicit origin statement in `README.md`.
- No active references remain to the old `skills/workflow/to-spec/`, `documentation/workflow/to-spec.md`, or `skills-to-spec` URL.
- Added prose contains no em dash.

## What is next

1. Review the full uncommitted diff for editorial quality and unintended consequences from the broad terminology rewrite. Pay special attention to the roughly 80 changed files and to commands or identifiers that must retain their literal spelling.
2. Decide whether the plugin identifiers `mattpocock-skills` and marketplace name `mattpocock` should remain for compatibility or be renamed to identify the fork. This was deliberately left unresolved.
3. Check whether installation commands and badges that still point at `mattpocock/skills` should instead point at `Dyrits/SKILLS`; the user only requested removal of AI Hero ownership in this session, so those were not changed.
4. If the diff is accepted, run the final validation again, commit it, and push only if the user asks for those git operations.

## Suggested skills

- Call the Skill tool with `takeover` first in the next session.
- Call the Skill tool with `writing-for-agents` before editing any skill, `AGENTS.md`, or `CLAUDE.md` material.
- Call the Skill tool with `code-review` when the editorial pass is ready to review the full diff against `f85ffd7`.
