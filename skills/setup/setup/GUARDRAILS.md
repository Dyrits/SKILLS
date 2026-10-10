# Git guardrails

Puts a human decision in front of destructive git commands, so the human approves each one instead of the agent running it unchecked. Routine work (commits, pushes to feature branches, dry runs) passes. The setup is agent-agnostic: two layers, and no harness is assumed.

- **Portable layer**: a git `pre-push` hook. It holds for any agent and any person, but git has no hook for local commands such as `reset --hard`, so it covers pushes only.
- **Agent layer**: [scripts/guard-git.py](scripts/guard-git.py), a command guard, wired into each harness's own way of intercepting a command. It reads the command text, so it sees chains (`&&`, `;`, `|`, `&`), `sudo`, `xargs`, `command`, `bash -c`, `$(...)`, and `git -C`.

## Guard levels

Each level includes the one above it.

| Level | Guards |
| --- | --- |
| 1. Shared history | A push to a protected branch (`main`, `master`, the remote's default branch, and any the user adds), a plain force push (`-f`, `--force`, a `+` refspec), a push that deletes or mirrors (`--delete`, `:branch`, `--mirror`, `--all`, `--prune`), `--no-verify` on a push. `--force-with-lease` and `--dry-run` pass |
| 2. Local work | `reset --hard`, `clean -f` (not a dry run), `branch -D`, `checkout` or `switch` that discards changes (`.`, `-- <paths>`, `-f`, `--discard-changes`), `restore` on the working tree (`--staged` alone passes), `stash drop` and `clear`, `worktree remove --force`, `reflog expire` and `delete`, `gc --prune`, `prune` |
| 3. Strict | Every push, plus `rebase`, `reset` in any form, `commit --amend`, any branch or tag deletion, `filter-branch`, `filter-repo`, `update-ref` |

## Steps

### 1. Ask what to set up

Ask in one round, with a recommended answer for each (use the harness's question tool when it has one, plain chat otherwise):

- **Level**: 1, 2, or 3. Recommend 2.
- **Scope**: this project only, or every project.
- **Harnesses**: which agent harnesses the user works in. Run `python3 -I scripts/detect-harnesses.py --project .` for the candidates on disk (directory, command on the path, steering files; installed-skills-only directories come back as one `skills-only` line), add the harness you are running in if it is missing, and propose the list.
- **Protected branches**: `main` and `master` stay; add others such as `develop`.

Completion: level, scope, harnesses, and protected branches are answered.

### 2. Install the portable layer

Copy [scripts/pre-push](scripts/pre-push) into the repository's hooks directory (`git rev-parse --git-path hooks`, which follows `core.hooksPath`), make it executable, and set `PROTECTED_BRANCHES` and `LEVEL` at its top. When a `pre-push` hook already exists, call the new one from it and keep the existing one working. A hook belongs to one repository, so for global scope ask which repositories get it.

Completion: the hook is executable and refuses a simulated deletion, `printf 'refs/heads/x 0000000000000000000000000000000000000000 refs/heads/feat abc\n' | <hook>`, exiting 1.

### 3. Wire the agent layer, per harness

Copy [scripts/guard-git.py](scripts/guard-git.py) to a stable path for the scope (`.agents/hooks/` in the project, `~/.agents/hooks/` globally). It needs Python 3 and git. Run `python3 --version` first; without Python 3 the hook would fail open, so skip this step and say so.

For each harness, read its current documentation for command interception, because schemas and file locations change between releases. Use the strongest mechanism it documents:

1. **A pre-command hook that can ask or block.** Point it at `python3 -I <path>/guard-git.py --level <N> --protected <branches>` with the hook payload on stdin. The default `text` format exits 2 with the reason on stderr, the usual convention for a blocking hook; `--format ask-json` prints the permission prompt decision that Claude Code-style hooks accept.
2. **Permission rules with command patterns.** Translate the guard table into ask rules. Patterns cannot see the branch or a chain, so rules ask on every non-dry-run push.
3. **Neither.** The portable layer alone. Tell the user which levels 2 and 3 commands stay unguarded.

[GUARDRAIL-WIRING.md](GUARDRAIL-WIRING.md) shows one hookup of each of the first two. Merge into the harness's existing settings and keep every entry already there.

Completion: each harness has its mechanism recorded (1, 2, or 3) and its settings file still parses.

### 4. Verify

Run the guard on three commands at the chosen level and confirm the first is guarded (exit 2) and the others pass (exit 0):

```bash
printf 'git push origin main' | python3 -I <path>/guard-git.py --level <N>
printf 'git push --force-with-lease origin feature' | python3 -I <path>/guard-git.py --level <N>
printf 'echo "git push origin main"' | python3 -I <path>/guard-git.py --level <N>
```

Then check each harness's wiring through the harness itself where it allows (a guarded command in a fresh session produces the prompt or the block).

### 5. Report

For the report, one line per layer and harness: the level, the mechanism, what was verified and what was only written, and what stays unguarded.

## Changing or removing it

Run this area again with the new answers: the files are overwritten in place and the settings entries replaced, never duplicated. To remove, name the hook, the copied script, and each settings entry, then delete them with the user's agreement.

## Limits to tell the user

- The guard reads command text. Git aliases, scripts that run git, and `eval` are not followed, so it catches mistakes, not a determined bypass. Branch protection on the remote is the only hard stop.
- A confirmation needs a human. Where nobody can answer, expect the guarded command to be refused.
- `git push --no-verify` skips the hook; at level 1 the command guard asks before it, and a person uses it deliberately to approve a push.
