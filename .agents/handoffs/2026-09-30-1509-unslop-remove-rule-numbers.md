# Unslop rule numbering removed

**Supersedes:** none. This is a small, separate thread from [2026-09-30-1455-code-review-and-refactor.md](./2026-09-30-1455-code-review-and-refactor.md), whose work is unrelated and complete.

## Completed work and user decisions

The user asked whether numbering the patterns in [unslop](../../skills/reference/unslop/SKILL.md) is useful, then told the agent to fix it.
The agent found that the line "Rule numbers are stable ids that other skills cite" was false.
No skill in this repository, `~/.claude/skills`, or `~/.agents/skills` cites a rule by number.
`publish-review` and `publish-message` call `unslop` by name.
The only numeric citation is "rule 33" in the historical handoff [2026-09-23-1220-unslop-and-documentation-skills.md](./2026-09-23-1220-unslop-and-documentation-skills.md), which is a record and stays unchanged.

The agent removed the numbering in `skills/reference/unslop/SKILL.md`:

- The numbered patterns are now bullets, so the bold pattern names are the only handles.
- The sentence "Rule numbers are stable ids that other skills cite. A removed rule leaves a gap." is deleted.
- The Mannered prose pattern used to end with "Rule 26 covers the metaphor nouns." It now ends with "The Abstract metaphor nouns pattern covers metaphor nouns."

The documentation page `documentation/skills/reference/unslop.md`, both promoted listings, and `what-is-next` never mention rule numbers, so none needed a change.

One tradeoff the user did not weigh in on: the numbers made merges with the upstream skill cleaner, and the fork does port upstream changes.
Expect a small conflict in this file the next time the upstream `unslop` is ported, and resolve it by keeping bullets.

## Verification

- `git diff --stat` shows one file changed, `skills/reference/unslop/SKILL.md`, with 28 insertions and 30 deletions.
- A search for `rule`, `stable`, and leftover numeric prefixes in the file found nothing outstanding after the edits.
- Nothing else was run. There was no lint, link scan, or plugin validation, and none is needed for a change inside one skill body.

## Git state and next session

The change is uncommitted on `main` in `/Users/dgerrits/Codelab/Dyrits/SKILLS`, with `skills/reference/unslop/SKILL.md` showing as modified.
The user passed "commit and push" as the focus of the next session, so the next agent should:

1. Run `git status --short --branch` and `git diff` to confirm only the `unslop` change and this handoff are pending.
2. Commit both with a message such as "Remove rule numbering from unslop". End it with the co-author line the session's attribution reminder specifies.
3. Push to `origin/main` and confirm with `git log -1 --oneline` and `git status --short --branch`.

No pull or merge request was requested. Neither the commit nor the push has happened yet.

## Suggested skills

- Call the Skill tool with `unslop` for any repository prose, including the commit message.
- Call the Skill tool with `writing-for-agents` before any further change to skill instructions.
