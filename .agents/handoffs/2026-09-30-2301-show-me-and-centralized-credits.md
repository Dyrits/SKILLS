# Show-me skill and centralized credits

**Supersedes:** none.
This is a separate thread from [2026-09-30-1509-unslop-remove-rule-numbers.md](./2026-09-30-1509-unslop-remove-rule-numbers.md), whose change is already committed as `8beeace`.

## User decisions

The user supplied a `show-me` draft and asked to add it to this repository, adapting it with `writing-for-agents`.
They pointed out the existing visual guidance in `to-pull-request` and explicitly allowed agent invocation of the new skill.
They then requested attribution in the top-level README instead of separate credits files, including the source of `unslop`.
The final instruction was to write this handoff without committing.
No commit or push was performed in this session.

## Completed work

- [show-me](../../skills/productivity/show-me/SKILL.md) is a new model-invoked Productivity skill with a compact format guide and two examples.
- [HTML.md](../../skills/productivity/show-me/HTML.md) holds the HTML branch, including responsive layout, preview, opening, and file-link guidance.
- [Codex metadata](../../skills/productivity/show-me/agents/openai.yaml) enables implicit invocation by omitting the policy block.
- [to-pull-request](../../skills/workflow/to-pull-request/SKILL.md) calls the Skill tool with `show-me` for an inline Summary visual, replacing its duplicated examples.
  It retains a brief fallback for standalone installation when `show-me` is unavailable.
- Promotion, both listings, the router, and human-facing documentation were updated.
  See [.claude-plugin/plugin.json](../../.claude-plugin/plugin.json), [README.md](../../README.md), [Productivity listing](../../skills/productivity/README.md), [what-is-next](../../skills/getting-started/what-is-next/SKILL.md), and [show-me documentation](../../documentation/skills/productivity/show-me.md).
  The documentation pages for [what-is-next](../../documentation/skills/getting-started/what-is-next.md) and [to-pull-request](../../documentation/skills/workflow/to-pull-request.md) were synchronized.
- Attribution for `show-me`, `to-pull-request`, and `unslop` now lives in the Credits section of the top-level README.
  Both skill-local `CREDITS.md` files were removed.
  The `unslop` source supplied by the user was verified at <https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md>.

The current files and Git diff are the authority for the detailed changes.

## Local installation

`~/.claude/skills/show-me` and `~/.agents/skills/show-me` are symlinks to the new skill directory and were verified to resolve correctly.
The general linking script was not run because its replacement logic would delete seven existing non-symlink directories under `~/.agents/skills`.
Only the new skill links were created, using approved filesystem escalation.

## Verification and limits

- `claude plugin validate . --strict` passed, but its output shows it validated the marketplace manifest.
- `claude plugin validate .claude-plugin/plugin.json` passed with an existing warning that the root `CLAUDE.md` is not loaded as plugin project context.
  The same direct command with `--strict` fails because strict mode treats that warning as an error.
- `npm run check-plugin-version` passed, with version `0.1.1` synchronized.
- Ruby's YAML parser verified the new frontmatter and Codex metadata, including model invocation.
- Focused checks verified promotion, documentation section order, relative links, absence of em dashes in the new skill files, and whitespace.
- After centralizing attribution, README credit links and the absence of active references to removed credits files were verified.
- `git diff --check` passed.

No behavioural evaluation or generated HTML preview was run because this task created instructions rather than an HTML artifact.
Python's optional `yaml` module was unavailable, so YAML verification used Ruby's existing standard library instead.

## Working tree and next session

All work described above remains uncommitted.
The working tree also contains changes outside this thread involving `publish-message`, removal of `publish-review`, and `code-review-and-refactor`, including shared edits to the README and router.
Those changes were present during handoff preparation and were not authored or independently verified in this conversation.
Inspect the current `git status --short --branch` and diff before taking further action, and preserve that other work.

No further implementation task was specified.
The next session can review or continue the changes as directed by the user.
Commit and push require a new user instruction; this handoff does not authorize either.
Handoff history already exists as tracked repository files, so the existing shared-history convention was preserved.

## Suggested skills

- Call the Skill tool with `writing-for-agents` before changing skill instructions.
- Call the Skill tool with `unslop` for repository prose.
- Call the Skill tool with `show-me` when a visual explanation of the changes is useful.
