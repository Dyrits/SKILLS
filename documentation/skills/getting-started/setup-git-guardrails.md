Upstream skill: `git-guardrails-claude-code`, adapted here as `setup-git-guardrails`. Commit `f85ffd7` rewrote the entrypoint to cover multiple agents and moved the bundled script unchanged. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the original at `d81f3a1:skills/misc/git-guardrails-claude-code/`.

## What it does

Blocks dangerous git commands before a coding agent runs them: any `git push`, `git reset --hard`, `git clean -f`, `git branch -D`, `git checkout .`, and `git restore .`. The block is enforced by a hook script or a deny rule, so it holds in auto-approve mode: the agent never gets an approval prompt, the command is rejected outright.

Upstream covered Claude Code only. This fork extends it to OpenCode and Codex CLI, with a different mechanism for each.

## When to reach for it

Model-invoked: you can type `/setup-git-guardrails`, and the agent can reach for it when you want to prevent destructive git operations by any coding agent. It asks whether to install for this project or globally, and for which agents.

## What each agent gets

| Agent | Mechanism |
| --- | --- |
| Claude Code | A `PreToolUse` hook on Bash running [block-dangerous-git.sh](../../../skills/getting-started/setup-git-guardrails/scripts/block-dangerous-git.sh) |
| OpenCode | `permission.deny` glob rules in `opencode.json`, with bare and wildcard-prefixed variants so chained commands are caught |
| Codex CLI | No per-command deny list exists. The skill offers a versioned `pre-push` hook and remote branch protection, and says plainly that Codex cannot be blocked at the configuration level |

## Common questions

**Can the agent push if I approve it myself?**

The rules block the agent's commands. Run the push yourself in your own terminal, or remove the pattern from the script and deny rules.

**Can I change what is blocked?**

Yes. The skill asks about customization. Keep the script's pattern list and OpenCode's deny rules in sync.

**Why is Codex handled differently?**

It has no hook runner and no deny list. A git-level `pre-push` hook (see [setup-git-hooks](./setup-git-hooks.md)) and protected remote branches apply no matter which agent pushes.

## It's working if

- Piping a sample `git push origin main` command into the hook script exits with code 2 and a BLOCKED message on standard error.
- OpenCode refuses a `git push --dry-run` in a session, or its configuration parses with the rules listed.
- Your existing hooks and permission rules are still present.

## Where it fits

Run-once safety setup per project or per machine. [setup-git-hooks](./setup-git-hooks.md) is the git-level layer that covers agents this cannot intercept. [guide](./guide.md) routes the rest.
