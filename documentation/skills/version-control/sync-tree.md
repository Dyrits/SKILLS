Fork-created skill, no upstream equivalent: added in commit `0839ff5`, as recorded in [the retained skill provenance research](../../research/2026-10-03-retained-skill-provenance.md).

## What it does

`sync-tree` transfers the committed work of a worktree branch (or an isolated local clone) to its corresponding branch in the original local repository.

It moves history only. It makes no code changes, creates no merge commits, and does not publish to an upstream. If the destination has commits the source lacks, it never removes them: it offers to rebase the source branch onto the destination first, through [rebase](rebase.md), so the update becomes a fast-forward.

## When to reach for it

Type `/sync-tree`, usually after [work-in-tree](work-in-tree.md) has left its handoff. An agent or another skill can also reach for it when committed work is ready to land.

| Your situation | Skill |
| --- | --- |
| Committed work in a task worktree should reach the original branch | This one |
| You are starting a task and want isolation first | [work-in-tree](work-in-tree.md) |
| Branches need to move onto a new base for their own sake | [rebase](rebase.md) |

It stops for a detached source, an unfinished Git operation, or uncommitted intended changes: commit them in the source worktree first, because this skill transfers history rather than creating it.

## How the update is chosen

| Observed state | Action |
| --- | --- |
| Source and target equal | Report already synced, change nothing |
| Target ahead of source | Report the work as already landed; change nothing |
| Target absent, or an ancestor of the source | Fast-forward |
| Histories diverged | Show both tips and destination-only commits, then offer: rebase the source onto the target and fast-forward (recommended), replace the target branch (explicit approval, drops destination-only commits), or stop |

Updates compare against the exact target commit read directly from the destination. A fast-forward in a clean checkout uses `merge --ff-only`; an unchecked-out branch is updated with a compare-and-swap `update-ref`; separate clones use a push. An approved replacement uses an exact lease. After a rebase the tips are captured again, so the update is a plain fast-forward. The skill does not reset, clean, stash, or switch your worktrees to get around a protection.

## Common questions

**What if the target branch is checked out with changes?**

It stops. A target checkout with staged, unstaged, or untracked changes, or an unfinished operation, is never modified.

**What if the histories diverged?**

The target branch moved on while you worked. `sync-tree` shows both tips and offers three moves: rebase the source branch onto the target through [rebase](rebase.md) and then fast-forward (recommended, no commit is lost), replace the target branch (only on explicit approval, because the destination-only commits are dropped), or stop. A conflict during the rebase is relayed to you as a question, and nothing is updated until it is answered.

**Why not merge?**

A merge creates a new commit on the target, which is a code-combining change this skill leaves to a separate request.

**What if it cannot sync at all?**

Every stop names the state it observed, the reason, and the next move: commit in the source worktree, commit or stash in the target checkout (your own work, never touched by the skill), pick another target branch, answer the conflict question, or rerun after the target moved.

**Does it push to the upstream?**

No. Upstream publication is a separate request. Only filesystem destinations are used; network remotes are left untouched.

**What does "synced" prove?**

That the destination ref equals the source commit after the update. Existing test evidence is reported separately, because syncing alone does not rerun code.

## It's working if

- The report names the source, destination, target branch, and one verified commit ID.
- The destination ref, read again afterwards, equals that commit.
- An already-synced branch is reported as a no-op, not a landing.
- Your target checkout, if any, still has the same clean status.
- A stop ends with a stated reason and a next move, not a bare refusal.

## Where it fits

The return leg of the isolated-worktree route: [work-in-tree](work-in-tree.md) prepares and works in the checkout, this lands it. [guide](../productivity/guide.md) maps the wider flow.
