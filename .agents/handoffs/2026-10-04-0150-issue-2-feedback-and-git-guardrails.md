# Issue #2 feedback and git guardrails that ask

Supersedes: `.agents/handoffs/2026-10-04-0025-improve-skills-and-capabilities.md`

## What happened

- [Dyrits/SKILLS#2](https://github.com/Dyrits/SKILLS/issues/2), a skill retrospective with eight findings, is addressed in `679cc3d`. The reply is [posted](https://github.com/Dyrits/SKILLS/issues/2#issuecomment-5974723239) and the issue is closed. The commit message lists each change. Notable: `hand-off` is now **model-invoked** so the `setup-auto-handoff` gate can run it.
- `setup-git-guardrails` now asks instead of blocking: `c9ea279`. The script was renamed to `confirm-dangerous-git.sh`. The user approved "ask" plus the narrowing (protected branches only, `--force-with-lease` and dry runs pass, match only the command run) and chose not to `/refine` further.
- Both commits and this handoff are pushed to `origin/main`.

Checks passing at `c9ea279`: `npm run check-skills`, `npm run test-skills-check`, `npm run check-plugin-version`, `claude plugin validate . --strict`, `git diff --check`, the auto-handoff gate simulations, and 30 sample commands through the guard script in a scratch repository.

## Unverified

- Whether a hook's `ask` still prompts under Claude Code's `bypassPermissions` mode. The hooks documentation only says hooks run in that mode. The skill claims only that non-interactive sessions refuse the command.
- The OpenCode `permission.bash` rules follow https://opencode.ai/docs/permissions/ (last match wins) but were never run in OpenCode.

## Open items

Carried from the superseded handoff, still undecided:

- `~/.agents/skills/improve-agent-environment` is a real directory copy, not a symlink; removal awaits the user's go-ahead.
- Version stays at 0.2.0; the user has not decided whether these changes (including `hand-off`'s invocation change) warrant a bump.

## Suggested skills

- `write-for-agents` (model-invoked, Skill tool): before editing any `SKILL.md`.
- `document` (model-invoked, Skill tool): for changes to project-document rules.
- `setup-git-guardrails` (model-invoked): re-run in projects that installed the old `block-dangerous-git.sh`.
- `/improve-skills` (user-invoked): report the next session's skill problems.
- `/guide` (user-invoked): confirm the router reads correctly after `hand-off` became model-invoked.
