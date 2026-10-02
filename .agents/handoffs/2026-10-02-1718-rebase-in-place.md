# Handoff: experimental rebase skill, rebuilt to rebase in place

Supersedes: none (the previous handoff, `2026-10-02-1331-reuse-scripts-skill.md`, covers unrelated work).

## Next session focus

The work below is committed and pushed to `origin/main` together with this file. Pick up from "Not done".

## What happened

An earlier, interrupted session had drafted `skills/experimental/rebase/` as a parallel, push-by-default design: isolated workers rebased copies of remote branches and force-pushed them without touching local branches. The user reviewed it and redirected it:

1. Rebase local branches **in place** where possible.
2. **Report, then ask** before any push.
3. A single branch is handled by the **main agent**, with no subagent.
4. **Checks stay mandatory** before a branch is offered for push.

The skill was rewritten accordingly. `WORKER.md` was replaced by `BRANCH.md`, the per-branch procedure followed by the main agent or by a subagent, with no push section.

## Decisions to keep

- Rebase location: a branch checked out in a clean checkout rebases there. A branch checked out nowhere gets a temporary `git worktree add` in the host's state directory. If the checkout has uncommitted work, the skill asks whether to commit, stash or skip.
- Subagents must be plain subagents working in the assigned worktree. A harness-managed isolated worktree would rebase a copy on another branch.
- Backup refs `refs/rebase-backup/<name>` make every rebase undoable. They are kept unless the user agrees to delete them.
- A branch whose checks fail stays rebased locally. It is offered for push only when the user waives the named failing checks.
- The push uses the lease captured before the rebase, then a `git ls-remote --refs` readback.
- If a branch is behind or has diverged from its remote, the skill asks first. A stack of branches is rebased together from its top with `--update-refs`, after asking.
- Repository conventions from earlier handoffs still apply: handoffs committed, no em-dashes, short imperative commit subjects, direct commits to `main`.

## Contents of the commit

Run `git show --stat HEAD`. Changes: the new `skills/experimental/rebase/` (`SKILL.md`, `BRANCH.md`, `RESUME.md`, `agents/openai.yaml`), plus registration in both READMEs, `what-is-next` (skill and documentation page) and `documentation/skills/upkeep/resolve-merge-conflicts.md`.

## Not done

- The skill has never been run. Try `/rebase <branch> --onto <target>` on a scratch repository: one branch checked out (current checkout), one not checked out (worktree path), one forced conflict, one failing check.
- `scripts/link-skills.sh` was run, so `~/.claude/skills/rebase` exists.

## Suggested skills

- `writing-for-agents` before editing any file in `skills/experimental/rebase/`.
- `resolve-merge-conflicts`, which the rebase skill calls on conflicts. Its final "stage everything and commit" step is overridden in `BRANCH.md`.
