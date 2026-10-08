Upstream skill: `git-guardrails-claude-code`, adapted here as `setup-git-guardrails`. Commit `f85ffd7` rewrote the entrypoint to cover multiple agents and moved the bundled script; the fork later replaced its outright block with a confirmation. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the original at `d81f3a1:skills/misc/git-guardrails-claude-code/`.

## What it does

Puts a human decision in front of git commands that can lose work or rewrite shared history, so you approve each one instead of the agent running it unchecked. It does not assume an agent: a bundled script, `detect-harnesses.py`, lists the harnesses it finds on disk, and the skill asks which of them you use and wires each one by the strongest mechanism that harness documents.

It asks four things in one round: the guard level, the scope (this project or every project), the harnesses, and the protected branches.

| Level | Guards |
| --- | --- |
| 1. Shared history | Pushes to a protected branch (`main`, `master`, the remote's default branch, and any you add), plain force pushes, pushes that delete or mirror, `--no-verify` on a push |
| 2. Local work | Level 1, plus `reset --hard`, `clean -f`, `branch -D`, `checkout` or `switch` that discards changes, `restore` on the working tree, `stash drop` and `clear`, `worktree remove --force`, `reflog expire`, `gc --prune` |
| 3. Strict | Level 2, plus every push, `rebase`, any `reset`, `commit --amend`, any branch or tag deletion, `filter-branch` |

Routine work passes at levels 1 and 2: commits, pushes to feature branches, `--force-with-lease` to a feature branch, dry runs, and `git restore --staged`. The command guard reads the command being run, across chains, `sudo`, `xargs`, `command`, `bash -c`, `$(...)`, and `git -C`, so `echo "git push"` or a commit message that mentions a push is not caught.

Upstream covered Claude Code only and denied outright. This fork asks instead of denying, and no longer names the harnesses it supports.

## When to reach for it

Type `/setup-git-guardrails`, or an agent can reach for it when you want to guard against destructive git operations by coding agents.

## The two layers

| Layer | What it is | What it covers |
| --- | --- | --- |
| Portable | A git `pre-push` hook installed in the repository's hooks directory | Pushes by any agent or person: protected branches and remote deletions, and at level 3 any non-fast-forward. Git has no hook for local commands |
| Agent | [guard-git.py](../../../skills/setup/setup-git-guardrails/scripts/guard-git.py), wired into the harness | Every command in the guard table, through a pre-command hook when the harness has one, through permission rules when it has those, and not at all when it has neither |

[EXAMPLES.md](../../../skills/setup/setup-git-guardrails/EXAMPLES.md) shows one hookup of each mechanism.

## Common questions

**What happens when the agent tries a guarded command?**

With a hook that can ask, you get the harness's permission prompt with the reason (for example "This pushes to the protected branch `main`"). With a blocking hook, the command is stopped and the agent is told why.

**What about non-interactive sessions?**

Nobody can answer a prompt there, so expect the guarded command to be refused.

**What if my harness has no hooks or rules?**

The portable layer still guards pushes, and the skill tells you which level 2 and 3 commands stay unguarded.

**Is this a sandbox?**

No. It reads command text, so aliases, scripts that run git, and `eval` get past it. It catches mistakes. Branch protection on the remote is the only hard stop.

**Can I change the level later?**

Run the skill again with new answers. Files are overwritten in place and settings entries replaced, not duplicated.

## It's working if

- Piping `git push origin main` into the guard exits 2 with a reason, and piping `echo "git push origin main"` exits 0 silently.
- Pushing a feature branch goes through without a prompt.
- Each harness you chose prompts or blocks on a guarded command in a fresh session, or the report says it could not be checked.
- Your existing hooks and permission rules are still present.

## Where it fits

Run-once safety setup per project or per machine, run on its own request. [setup-git-hooks](./setup-git-hooks.md) manages the same hooks directory, so the two coexist. [guide](../productivity/guide.md) routes the rest.
