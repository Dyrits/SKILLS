Fork-created skill, no upstream equivalent: added in commit `a3792dd`, as recorded in [the retained skill provenance research](../../research/2026-10-03-retained-skill-provenance.md).

## What it does

`rebase` rebases one or more local branches in place onto a single target, resolves conflicts by intent, validates every result, reports, and pushes only the branches you approve.

Its defining constraint is that nothing is published without your answer. The branch itself moves (no copy on another branch), every rebase has a backup ref, and the push uses an explicit `--force-with-lease` against the remote tip captured before work began. Plain `--force` is never used.

## When to reach for it

Type `/rebase fix/a feat/b --onto origin/develop`, or describe the branches and target in plain language. An agent or another skill can also reach for it. Because it can rewrite published history, publication stays separately approved by you.

| Your situation | Skill |
| --- | --- |
| Bring several local branches up to date with a target, then publish them | This one |
| A merge or rebase you started yourself has stopped on conflicts | [resolve-merge-conflicts](resolve-merge-conflicts.md) |
| The branch is ready and needs a description | [draft-merge-request](draft-merge-request.md) |

`--onto` names the target branch, not Git's three-argument transplant. `--remote` names the publication remote when a branch has no upstream or an ambiguous one.

## Where each branch is rebased

Where a branch is checked out decides where it is rebased:

| Branch location | Rebase location |
| --- | --- |
| Not checked out anywhere | A temporary linked worktree outside every checkout |
| Checked out in a clean checkout | That checkout, the current one included |
| Checked out with uncommitted work or an operation in progress | The skill asks whether to commit, stash, or skip |

A single branch is handled by the main agent. Several branches in worktrees are rebased in parallel by one plain subagent each, which report evidence and leave pushing to the main agent.

## Pins, backups, and validation

Before rebasing, the skill pins full commit IDs: one **target pin** shared by every branch, each branch's start, and its lease (the remote tip). It creates `refs/rebase-backup/<name>` per branch, so the undo command in the report always works.

Every rebased branch is validated, conflicts or not: the target must be an ancestor of the new tip, `git range-diff` must explain every changed or dropped patch, and the repository's own checks must pass. A failing check stays a failure in the report; only you can waive it, and only for a named check.

## Common questions

**What happens if the remote has commits my local branch lacks?**

The skill asks before rebasing. A branch pushed without those commits would delete them from the remote, so the answer is recorded and respected.

**Can I undo a rebase?**

Yes, until you delete the backup refs. The report names the command per branch: `git reset --keep refs/rebase-backup/<name>` in its checkout, or `git branch -f <name> refs/rebase-backup/<name>` when it is not checked out. The skill offers to delete the backups at the end and keeps them unless you agree.

**What if the session is interrupted?**

Per-branch records live in a batch directory outside every checkout. Resuming reads them, keeps the original pins and approved answers, and inspects each branch's actual state before continuing. A branch whose state cannot be established is marked `unknown` and you are asked.

**Does it work without a remote or tracker?**

Yes. A branch without a remote is marked local only. Missing tracker access is not a failure: commit messages, diffs, and local specifications establish intent, and the skill stops with a precise question when they do not.

**What if a skill it calls is not installed?**
It names the missing skill with its install command, carries out that step from its stated intent, and tells you the step ran without it. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/version-control/rebase/SKILL.md).

## It's working if

- You get one report table (branch, start, new tip, conflict decisions, checks, destination, status) before anything is pushed.
- Each conflict decision cites the intent it preserved, not just the side it kept.
- Branches in the push offer are only `rebased and validated`, or ones whose named failing checks you waived.
- After pushing, each branch is marked `pushed and verified` only because the remote tip read back equal to the new tip.
- Your own uncommitted work and unrelated branches are untouched.

## Where it fits

A standalone version-control skill for batches of local branches. It calls [resolve-merge-conflicts](resolve-merge-conflicts.md) whenever Git stops on a conflict. [work-in-tree](work-in-tree.md) and [sync-tree](sync-tree.md) cover the other worktree movements. [guide](../productivity/guide.md) maps the wider flow.
