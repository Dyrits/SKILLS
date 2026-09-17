# Skills repository fork rework, session 6: experimental skills

Supersedes: `.agents/handoffs/2026-09-17-1126-fork-rework-session-5.md`

## Current state

`HEAD` and `origin/main` are `84d3479` ("Archive pristine upstream docs, add fork ADR, remove WIP writing skills"), which already includes everything session 5's handoff described: the `.upstream/` archive restoration, the fork's own first ADR, the `grill-with-docs` → `grill-with-documentation` rename, and the deliberate removal of `skills/work-in-progress/` (confirmed deliberate by the user after session 5 asked; every reference to it was also removed from `CLAUDE.md`, `.agents/writing-documentation.md`, and `scripts/link-skills.sh`). All of that landed in `84d3479`, apparently amended and pushed outside this conversation between sessions 5 and 6; nothing further to do there.

This session's work is staged but uncommitted, and is what the user asked to commit and push now.

## Decisions and completed changes

- New non-promoted bucket `skills/experimental/`: mirrors the just-removed `work-in-progress/` bucket's exact semantics (not in `.claude-plugin/plugin.json`, not in any `README.md`, no `documentation/` page, installed one at a time via `npx skills@latest add Dyrits/SKILLS --skill=<name>`, still linked locally by `scripts/link-skills.sh`), chosen because these skills take real, externally visible actions (posting comments) rather than being merely unfinished. Documented in `CLAUDE.md` and `.agents/writing-documentation.md` alongside the existing `deprecated/` exception. This was an assumption, not confirmed with the user: if promoted-by-default was actually wanted, `plugin.json` and both `README.md`s need the entries back.
- **`publish-message`** (new, `skills/experimental/publish-message/`): posts a short `[AI]`-prefixed comment to a GitHub/GitLab pull/merge request or a Jira issue, leading with the why rather than restating the diff or ticket. Resolves the tracker and posting mechanism (CLI, an available MCP tool, or another verified method) via `documentation/agents/issue-tracker.md`, the same indirection every tracker-consuming skill in this repository uses. Always confirms the drafted message before posting, unless the user supplied the literal text.
- **`publish-review`** (new, `skills/experimental/publish-review/`): publishes a finished `/code-review` report. Splits findings into concretely fixable ones (posted as inline `[AI]`-prefixed suggested changes on GitHub/GitLab, via the tracker's pull/merge request *review* flow, MCP pending-review tools preferred over CLI) and everything else (delegated to `publish-message` as one summary comment). Two separate confirmations before anything posts: `publish-message`'s own for the summary, a second one in `publish-review` for the suggestions. Hard-depends on `publish-message` being installed alongside it.
- **`code-review`** (`skills/workflow/code-review/SKILL.md`, a promoted skill) gained a new step 6, "Offer to publish": asks whether to publish the finished report and where; if yes, calls the Skill tool for `publish-review`. This is a soft dependency: if `publish-review` isn't installed, `code-review` says so and gives the install command rather than trying to replicate its logic, and `code-review`'s existing behaviour is unchanged if the user declines.
- A `/writing-for-agents` self-review of both new skills against the rest of the repository found one real structural deviation before commit: both files originally closed with a standalone `## Done when` heading summarising the whole skill. No existing skill in this repository does that; the actual convention (`ask-someone-else`, `wizard`, `debug`, `grilling`) is a `Done when:` phrase embedded inline at the end of the specific step it belongs to. Both files were restructured to match before this handoff was written. Everything else checked (description word count, `argument-hint` usage and frontmatter key order, the hard-dependency line's wording, `Call the Skill tool with` phrasing, `## Process` as the steps heading) already matched existing convention.

## Primary artifacts

- `skills/experimental/README.md`, `publish-message/SKILL.md`, `publish-review/SKILL.md` (+ each skill's `agents/openai.yaml`)
- `skills/workflow/code-review/SKILL.md`: new step 6
- `CLAUDE.md`, `.agents/writing-documentation.md`: `experimental/` bucket documented

## What is next

1. Commit and push (requested by the user; this handoff is written first, per the `hand-off` convention).
2. Confirm with the user whether `experimental/` should actually be promoted-by-default rather than opt-in (see the flagged assumption above).
3. No other prior "what is next" items outstanding; sessions 1-5 are fully superseded.

## Suggested skills

- Call the Skill tool with `take-over` when resuming from this file.
- Call the Skill tool with `writing-for-agents` before further edits to any `SKILL.md`, `AGENTS.md`, or `CLAUDE.md` (this session found a real convention deviation by doing exactly this; keep doing it).
- Call the Skill tool with `code-review` if a two-axis review of this session's diff against `84d3479` is wanted before or after commit.
