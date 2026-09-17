# Address Feedback Skill

Supersedes: [2026-09-17-1533-code-review-setup-fallback.md](./2026-09-17-1533-code-review-setup-fallback.md)

## Outcome

Created the user-invoked experimental [`address-feedback`](../../skills/experimental/address-feedback/SKILL.md) skill for handling feedback from pull requests, merge requests, issues, and tickets.

The workflow accounts for every substantive comment, recommends a disposition and concrete change plan, waits for approval before editing, implements and validates the approved changes, drafts a response for each comment, then waits for approval of the exact replies before publishing them.

The skill distinguishes accepting, adjusting, already-addressed, declined, and blocked feedback. Thread resolution, review approval, ticket closure, and status changes remain separately listed tracker mutations.

Added the skill to the [experimental listing](../../skills/experimental/README.md), the top-level README's separate experimental section, and the [`what-is-next` router](../../skills/getting-started/what-is-next/SKILL.md). It remains outside the plugin manifest and promoted reference listing because experimental skills take externally visible actions and receive no documentation page.

Moved the inherited Matt Pocock glossary from the repository root to [`.upstream/CONTEXT.md`](../../.upstream/CONTEXT.md), where the fork keeps archived upstream material.

Ran `scripts/link-skills.sh`, which linked every active repository skill, including `address-feedback`, into both `~/.claude/skills` and `~/.agents/skills`.

## Validation

- `git diff --check` passed.
- The new frontmatter and `agents/openai.yaml` parsed successfully as YAML.
- `scripts/list-skills.sh` discovers `address-feedback`.
- `npm run check-plugin-version` passed.
- The bundled `quick_validate.py` could not start because `PyYAML` is absent from its Python environment; direct YAML parsing covered the relevant file validation.

## Suggested skills

- Use `/address-feedback <target>` to exercise the new workflow against a real pull request, merge request, issue, or ticket.
- Use `/writing-for-agents` when revising the skill after observed behavior.

## Remaining work

No implementation work remains. The next useful step is to try the skill on a real feedback thread and tighten its instructions only where observed behavior warrants it.
