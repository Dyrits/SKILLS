# improve-skills and capability folders

Supersedes: `.agents/handoffs/2026-10-03-2352-setup-workspace-offers-all-setups.md`

## What happened

Committed and pushed as `e5572d5` on `main`; the commit message and diff are the record. In short:

- `improve-agent-environment` became [`improve-skills`](../../skills/upkeep/improve-skills/SKILL.md): a user-invoked retrospective, held with the user, that reports skill problems as an issue on `Dyrits/SKILLS`. It tries every route to GitHub and saves the approved issue in `.agents/feedbacks/` when none works. Project lessons go through `memorize`.
- `iterate` no longer captures corrections. `memorize` owns them, and its Homes table routes a defect in a skill itself to `/improve-skills`.
- Specifications, drafts, maps, and tasks now live under `documentation/capabilities/<capability>/`, replacing `<feature>` and `<effort>`. Rules: the **Capabilities** section of [PROJECT-DOCUMENTS.md](../../skills/reference/document/PROJECT-DOCUMENTS.md). Reasoning: [architecture decision record 0003](../../documentation/architecture-decision-record/0003-group-specifications-by-capability.md).

Checks passing at commit: `npm run check-skills`, `npm run test-skills-check`, `npm run check-plugin-version`, `claude plugin validate . --strict`, `git diff --check`. No skill was executed end to end.

## User preferences learned

- Keep a concern in the skill that owns it; do not add cross-cutting hooks to one workflow skill (rejected for `iterate`).
- Do not list mechanisms an agent already knows; keep only the non-default behavior (for example, try every route before giving up).
- User-invoked skills cannot be started by the agent; only a message beginning with the slash command loads them.

## Open items

- `~/.agents/skills/improve-agent-environment` is a real directory copy, not a symlink, so the old command still works. Removal awaits the user's go-ahead.
- `gh` is not installed on this machine, so `improve-skills` will likely fall back to `.agents/feedbacks/` until a GitHub route exists.
- Version stays at 0.2.0; the user has not decided whether the rename warrants a bump.
- Architecture decision record 0002 still says "feature requirements"; left as a dated record.

## Suggested skills

- `/improve-skills` (user-invoked): run after a real session to exercise the new retrospective.
- `/guide` (user-invoked): confirm the router reads correctly after the rename.
- `write-for-agents` (model-invoked, Skill tool): before editing any `SKILL.md`.
- `document` (model-invoked, Skill tool): for any change to the capability rules.
