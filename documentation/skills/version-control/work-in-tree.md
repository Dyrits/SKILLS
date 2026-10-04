Fork-created skill, no upstream equivalent: added in commit `0839ff5`, as recorded in [the retained skill provenance research](../../research/2026-10-03-retained-skill-provenance.md).

## What it does

`work-in-tree` creates or reuses an isolated Git worktree and carries out the requested task there, so your original checkout and target branch stay unchanged until you ask for a sync.

Its defining constraint is verified isolation. A linked worktree on the target's own ref is not isolation, because commits there would advance the target at once; the skill creates a new task branch, or proves the current checkout is already separate.

## When to reach for it

Type `/work-in-tree` followed by the task. The agent or another skill can also reach for it when work needs an isolated checkout. Invoked with no task, it prepares the checkout and asks what to work on.

| Your situation | Skill |
| --- | --- |
| Do a task without disturbing the current checkout | This one |
| The task is committed and should land on the original branch | [sync-tree](sync-tree.md) |
| Several tickets to run, each in its own tree | [divide-and-conquer](../workflow/divide-and-conquer.md) |

## What it needs

A new worktree starts from committed history. Uncommitted edits in your current checkout stay where they are; if the task needs them, commit them first or choose another starting point. The skill stops for an unfinished Git operation, and asks which branch should receive the work when the checkout is detached.

If your file-editing tools stay rooted at the original checkout, it asks you to attach the new worktree or authorize direct edits there, and continues only when it can address the right tree.

## The return route

At the end it reports a handoff: task checkout path and branch, original repository, target branch, base and current commits, any uncommitted changes, and validation results. That is what [sync-tree](sync-tree.md) consumes. The worktree is kept for review; syncing, publication, and removal are separate requests.

## Common questions

**Where does the worktree go, and what is the branch called?**

Repository conventions win. Without any, the branch is `worktree/<task-name>` and the directory is a sibling of the repository, never nested inside tracked files. Existing paths and branches are inspected, not overwritten.

**Does it copy my secrets into the worktree?**

No. It reuses the repository's setup conventions for ignored configuration and keeps credentials out of copied or committed files.

**Can it run from inside an existing task worktree?**

Yes. It verifies the original repository through the handoff, shared Git metadata, or a local backlink, rather than treating the current task checkout as the original.

**What if a skill it hands over to is not installed?**
It gives you the install command along with the instruction to run it. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/version-control/work-in-tree/SKILL.md).

## It's working if

- `git status` in your original checkout is unchanged and its target branch has not moved.
- The task's edits, builds, tests, and commits all appear in the task worktree.
- The closing handoff lists the fields above, verified against live Git state.

## Where it fits

The opening leg of the isolated-worktree route, finished by [sync-tree](sync-tree.md). [rebase](rebase.md) handles bringing branches onto a new base. [guide](../getting-started/guide.md) maps the wider flow.
