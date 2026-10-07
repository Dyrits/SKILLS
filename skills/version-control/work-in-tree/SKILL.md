---
name: work-in-tree
description: "Create or reuse an isolated Git worktree and carry out the task there, preserving the original checkout. Use when the user asks to work in a worktree, or when a task must not touch the current checkout."
---

# Work in a tree

Establish an isolated checkout before editing task files, then continue the
requested work there. Keep the original checkout and target branch unchanged
until the user requests a sync.

**Hands over to:** `/sync-tree`.

## 1. Identify the starting point

Read applicable repository instructions, Git status, branch, HEAD, common Git
directory, remotes, and `git worktree list --porcelain`. Capture the original
checkout, target branch, and base commit before creating anything. If already
in an isolated checkout, verify the original repository through the supplied
handoff, shared metadata, or a local backlink rather than treating the current
task checkout as the original.

Use the current named branch as the target unless the user supplies another.
For a detached checkout or an unclear target, ask which local branch should
receive the work. Resolve the chosen target's tip as the base for a new
worktree, unless the user explicitly chooses a different base. Stop for an
unfinished Git operation.

Leave existing uncommitted changes in place. Explain that a new worktree starts
from committed history; if the task needs those edits, ask the user to commit
them or choose another starting point before continuing.

Completion: the task's base commit and eventual sync destination are known.

## 2. Reuse or create isolation

Reuse the current checkout when Git metadata or a verified local backlink
proves it is already isolated from the target branch. A linked worktree on the
target's shared ref is not branch isolation: commits there would immediately
advance the target. Reuse an existing task worktree only when its path, branch,
base, and task ownership are verified.

Otherwise create a linked worktree on a new task branch. Follow repository
branch and worktree-location conventions. If none exist, choose a unique
`worktree/<task-name>` branch and propose a sibling worktree directory rather
than nesting a checkout inside tracked project files. Ask for a task name if
the invocation supplies no task.

Confirm permission for a path outside the harness's workspace before creating
it. Check that the proposed directory and branch do not already exist; if they
do, inspect them rather than overwrite or reset them.

```bash
git worktree add -b <task-branch> <worktree-path> <base-commit>
```

Verify the new checkout's branch, HEAD, and clean status, then read its applicable
instructions and run the repository-prescribed setup there.

Completion: an editable, isolated task checkout exists at the verified base.

## 3. Work only in the task checkout

Route subsequent edits, builds, tests, and commits to the task checkout.
Use `git -C <worktree-path>` or an explicit working directory for each command;
a shell's previous `cd` is not a persistent tool setting.

If file-editing tools are still rooted at the original checkout, ask the user
to attach the new worktree or authorize direct edits there. Continue only when
the tools can address the intended checkout. Reuse existing setup conventions
for ignored configuration; keep credentials out of copied or committed files.

Perform the requested task under the repository's normal development and
validation workflow. If invoked without a task, report the prepared checkout
and ask what to work on.

Completion: all task changes and verification belong to the isolated checkout,
and the original checkout's files and target ref remain unchanged.

## 4. Leave the return route

Report a handoff with these verified fields:

- Task checkout path and branch.
- Original repository or checkout path.
- Target branch.
- Base commit and current task commit.
- Uncommitted task changes, if any, and validation results.

Tell the user to run `/sync-tree` with that destination once the intended work
is committed. Keep the worktree for review and further work; syncing, upstream
publication, and worktree removal require separate requests.
