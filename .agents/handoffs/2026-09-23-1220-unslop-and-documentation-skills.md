# Unslop and documentation skills

Supersedes: none. This handoff starts a separate thread from `.agents/handoffs/2026-09-22-0010-improve-agent-environment-docs.md`.

## Session outcome

- Added `unslop` and Anthropic's `documentation` skill to this repository as promoted, model-invoked skills under `skills/reference/`.
- Registered both in `.claude-plugin/plugin.json`, the top-level and reference README files, and the `what-is-next` router.
- Added human-facing pages at `documentation/skills/reference/unslop.md` and `documentation/skills/reference/documentation.md`.
- Removed `disable-model-invocation: true` and the matching Codex policy from the repository copy of `unslop` after the user pointed out that its description says it must always apply.
- Kept the repository's full-word and abbreviation convention in `AGENTS.md`; `unslop` rule 33 already gives the general advice to expand unclear abbreviations.
- Adapted the upstream `documentation` skill so its document-type lists are optional prompts, repository-specific formats take precedence, and agent-facing documents also use `writing-for-agents`.
- Copied the upstream Apache 2.0 license into `skills/reference/documentation/LICENSE`.

## Sources and boundaries

- The installed `unslop` source was `/Users/dgerrits/.agents/skills/unslop/SKILL.md`. The repository version differs only in invocation metadata.
- The `documentation` source is `https://github.com/anthropics/knowledge-work-plugins/blob/main/engineering/skills/documentation/SKILL.md`, inspected at upstream commit `1bd42820da111e5f0206e570bf5228a1c35839c7` in `/private/tmp/knowledge-work-plugins-review`.
- `/Users/dgerrits/.agents/skills/documentation` already contains an exact copy of the upstream skill, and `/Users/dgerrits/.claude/skills/documentation` links to it. The repository copy is adapted, and `scripts/link-skills.sh` would replace the existing local installation, so it was not run.
- No repository changes were committed. Existing handoffs are tracked, so this handoff follows the shared-history convention without changing `.gitignore`.

## Validation

- `claude plugin validate . --strict` passed after both additions.
- `git diff --check` passed, skill metadata was parsed with Ruby, and the new documentation page links resolved.
- The Codex `quick_validate.py` script could not run because its Python environment lacks `yaml`; equivalent frontmatter and invocation checks were done with Ruby.

## Next steps

- Review the uncommitted additions and any user feedback before committing or publishing.
- Keep the two local skill installations intact unless the user asks to replace them with repository symlinks.

## Suggested skills

- Call the Skill tool with `writing-for-agents` when editing the new skills or router.
- Call the Skill tool with `documentation` when writing or revising technical documentation.
- Apply `unslop` to all new prose.
