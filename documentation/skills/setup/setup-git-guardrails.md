Upstream skill: `git-guardrails-claude-code`, adapted here as `setup-git-guardrails`. Commit `f85ffd7` rewrote the entrypoint to cover multiple agents and moved the bundled script; the fork later replaced its outright block with a confirmation. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the original at `d81f3a1:skills/misc/git-guardrails-claude-code/`.

## What it does

Puts a confirmation in front of git commands that can lose work or rewrite shared history, so you approve each one instead of the agent running it unchecked:

- `git push` to a protected branch (`main`, `master`, the remote's default branch, and any you add), a plain force push, and pushes that delete or mirror remote branches.
- `git reset --hard`, `git clean -f`, `git branch -D`, `git checkout .` or `-- <paths>`, and `git restore` on the working tree.

Routine work passes without a prompt: commits, pushes to feature branches, `--force-with-lease` to a feature branch, dry runs, and `git restore --staged`. The Claude Code script checks only the command being run, so `grep "git push"` or a commit message that mentions a push is not caught.

Upstream covered Claude Code only and denied outright. This fork extends it to OpenCode and Codex CLI, and asks instead of denying.

## When to reach for it

Type `/setup-git-guardrails`, or an agent or another skill can reach for it when you want to guard against destructive git operations by any coding agent. It asks whether to install for this project or globally, for which agents, and which branches to protect.

## What each agent gets

| Agent | Mechanism |
| --- | --- |
| Claude Code | A `PreToolUse` hook on Bash running [confirm-dangerous-git.sh](../../../skills/setup/setup-git-guardrails/scripts/confirm-dangerous-git.sh), which answers `ask` with the reason |
| OpenCode | `permission.bash` glob rules in `opencode.json` set to `ask`, with `allow` exceptions after them (the last matching rule wins). Globs cannot read the current branch, so every non-dry-run push asks |
| Codex CLI | No per-command rules exist. The skill offers a versioned `pre-push` hook and remote branch protection, and says plainly that Codex cannot be guarded at the configuration level |

## Common questions

**What happens when the agent tries a guarded command?**

You get the normal permission prompt with the reason (for example "This pushes to the protected branch `main`"). Approve it and the command runs; refuse and the agent is told.

**What about non-interactive sessions?**

Nobody can answer the prompt there, so expect the guarded command to be refused.

**I installed the older version that blocked everything.**

Run the skill again. It replaces `block-dangerous-git.sh` and its registration with the confirming script.

**Can I change what is guarded?**

Yes. The skill asks which branches to protect and about further customization. Keep the script's checks and OpenCode's rules in sync.

**Why is Codex handled differently?**

It has no hook runner and no per-command rules. A git-level `pre-push` hook (see [setup-git-hooks](./setup-git-hooks.md)) and protected remote branches apply no matter which agent pushes.

## It's working if

- Piping a sample `git push origin main` command into the script prints JSON with `"permissionDecision": "ask"`, and piping `echo "git push origin main"` prints nothing.
- Pushing a feature branch goes through without a prompt.
- OpenCode prompts before a `git push origin main` in a session, or its configuration parses with the rules listed.
- Your existing hooks and permission rules are still present.

## Where it fits

Run-once safety setup per project or per machine, also offered as an optional stage of [setup-ai-workspace](./setup-ai-workspace.md). [setup-git-hooks](./setup-git-hooks.md) is the git-level layer that covers agents this cannot intercept. [guide](../productivity/guide.md) routes the rest.
