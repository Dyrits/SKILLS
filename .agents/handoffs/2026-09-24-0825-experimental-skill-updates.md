# Experimental skill updates

Supersedes: `.agents/handoffs/2026-09-17-1213-experimental-skills.md`, `.agents/handoffs/2026-09-20-0959-tier-agents-across-harnesses.md`, and `.agents/handoffs/2026-09-23-1220-unslop-and-documentation-skills.md` for the skills changed in this session.

## Current state

The user asked whether subagents could test the experimental skills, then requested changes to `unslop`, `publish-review`, `setup-delegation-policy`, and `classify`. A read-only Balanced tier subagent (`gpt-5.6-terra`) rehearsed all five experimental skills against hypothetical prompts before edits. It identified that `publish-review` could post a summary promising inline suggestions before those suggestions were approved.

The resulting edits are staged but uncommitted. See `git diff --cached` for the authoritative changes across 11 files. The main changes are:

- `skills/reference/unslop/SKILL.md` now applies its patterns in any language, with language-appropriate punctuation and quotation marks. Its documentation page, both promoted listings, and `what-is-next` were updated.
- `skills/experimental/publish-review/SKILL.md` now drafts and obtains approval for the complete review before posting. It prefers a single review submission for summary and inline suggestions; otherwise it posts and verifies suggestions before a summary that states their actual count. `publish-message/SKILL.md` no longer says `publish-review` calls it to post the summary.
- `skills/experimental/setup-delegation-policy/` now recognizes a Codex `spawn_agent` tool with a per-call model override, instead of declaring that Codex cannot delegate. `POLICY.md`, `SKILL.md`, and `TIER-AGENTS.md` check available tools and model identifiers at runtime. `what-is-next` reflects this.
- `skills/experimental/classify/SKILL.md` now keeps classification text out of shell command strings, handles private input locally or through redaction, and leaves local fallback confidence unstated.

## Verification and limits

- `git diff --check` passed.
- Ruby parsed the edited skill frontmatter; all edited local Markdown links resolved.
- No live tracker publication, classifier API call, or global steering-file installation occurred. The Codex tool available in this session had a `spawn_agent` call with a per-call model override, and OpenAI's multi-agent documentation confirms that a Codex-based harness can expose subagent orchestration: https://developers.openai.com/api/docs/guides/agents-api/multi-agent.
- The `skill-creator` Python validator could not run because this environment lacks the `yaml` module. Equivalent frontmatter checks used Ruby.
- Earlier handoffs note that installed skills under `~/.agents/skills/` may be copies rather than links. Repository edits may therefore require a deliberate installation or synchronization step before other sessions see them.

## Next session

Review the staged diff and any new user feedback. If the user wants behavioral confidence, test `publish-review` against mock tracker fixtures covering a single review submission, separate summary publication, and a partial inline failure. If the user wants these changes to affect global Codex steering files, run the updated `setup-delegation-policy` skill in that session and verify the installed section against `POLICY.md`. Preserve the staged work unless the user asks to revise it.

Existing handoffs are tracked and `.agents/handoffs/` is not ignored, so this handoff follows the repository's shared-history convention. It is not yet staged or committed.

## Suggested skills

- Invoke `writing-for-agents` for edits to `SKILL.md`, `POLICY.md`, or the router.
- Invoke `skill-creator` if running behavioral evaluations or iterating on these skills.
- Apply `unslop` to all prose, in the source language.
- Invoke `setup-delegation-policy` only if installing the revised policy into machine-wide steering files is the next requested task.
