Fork-created skill, no upstream equivalent: added in commit `0839ff5`, as recorded in [the retained skill provenance research](../../research/2026-10-03-retained-skill-provenance.md).

## What it does

`sync-tree` transfers the committed work of a worktree branch (or an isolated local clone) to its corresponding branch in the original local repository.

It moves history only. It makes no code changes, creates no merge commits, and does not publish to an upstream. If the destination has commits the source lacks, it stops instead of removing them.

## When to reach for it

Type `/sync-tree`, usually after [work-in-tree](work-in-tree.md) has left its handoff. An agent or another skill can also reach for it when committed work is ready to land.

| Your situation | Skill |
| --- | --- |
| Committed work in a task worktree should reach the original branch | This one |
| You are starting a task and want isolation first | [work-in-tree](work-in-tree.md) |
| Branches need to move onto a new base before landing | [rebase](rebase.md) |

It stops for a detached source, an unfinished Git operation, or uncommitted intended changes: commit them in the source worktree first, because this skill transfers history rather than creating it.

## How the update is chosen

| Observed state | Action |
| --- | --- |
| Source and target equal | Report already synced, change nothing |
| Target ahead of source | Stop; destination commits are never removed |
| Target absent, or an ancestor of the source | Fast-forward |
| Histories diverged | Show both tips and destination-only commits, then ask for explicit approval to replace the target branch |

Updates compare against the exact target commit read directly from the destination. A fast-forward in a clean checkout uses `merge --ff-only`; an unchecked-out branch is updated with a compare-and-swap `update-ref`; separate clones use a push. An approved replacement uses an exact lease. The skill does not reset, clean, stash, or switch your worktrees to get around a protection.

## Common questions

**What if the target branch is checked out with changes?**

It stops. A target checkout with staged, unstaged, or untracked changes, or an unfinished operation, is never modified.

**Why not use a merge or rebase?**

Syncing is a transfer of already-committed history. Combining histories is a separate request: use [rebase](rebase.md) first, then sync.

**Does it push to the upstream?**

No. Upstream publication is a separate request. Only filesystem destinations are used; network remotes are left untouched.

**What does "synced" prove?**

That the destination ref equals the source commit after the update. Existing test evidence is reported separately, because syncing alone does not rerun code.

## It's working if

- The report names the source, destination, target branch, and one verified commit ID.
- The destination ref, read again afterwards, equals that commit.
- An already-synced branch is reported as a no-op, not a landing.
- Your target checkout, if any, still has the same clean status.

## Where it fits

The return leg of the isolated-worktree route: [work-in-tree](work-in-tree.md) prepares and works in the checkout, this lands it. [guide](../productivity/guide.md) maps the wider flow.
