---
name: sync-tree
description: "Sync a completed Git worktree branch to its corresponding branch in the original local repository. Use when the user asks to sync, land, or bring worktree work back to the original checkout."
metadata:
  delta-action: land
---

# Sync the tree

Transfer committed work to its corresponding local branch. Preserve the branch
name unless the user names a different target. Leave upstream publication,
new merge commits, and code changes to separate requests.

This skill works with linked Git worktrees and isolated local clones. The
`delta-action` metadata also makes it eligible for Delta's Land Changes button;
the workflow itself uses Git, not application-specific tools.

## 1. Identify the source and target

Read the source's Git status, branch, HEAD, remotes, common Git directory, and
`git worktree list --porcelain`.

For an isolated child session, use the originating branch and commit supplied
by the invocation. Verify that commit exists locally. If the child has only a
temporary branch and the originating identity is unavailable, ask for it.
Conversation summaries alone do not prove a live branch's identity.

Stop for a detached source, unfinished Git operation, or uncommitted intended
changes. Ask the user to commit the intended changes in the source worktree
first; this skill transfers history rather than creating it.

Find the original local repository from an explicit destination, a verified
local backlink remote, or shared Git metadata for linked worktrees. A remote
named `local` is a candidate, not proof of identity. Use filesystem destinations
only; leave network remotes untouched. Resolve a backlink's push URL to a
verified local path; stop for multiple or uncertain push destinations.

Use the explicit target or the handoff from `work-in-tree`, verifying it against
live Git state. Otherwise default to the source branch's name only when it
identifies the corresponding branch unambiguously. If a temporary branch needs
to land on a different branch, or multiple destinations are plausible, ask for
the target repository and branch. Respect the harness's workspace permissions:
request attachment or explicit direct-edit authorization before modifying a
repository outside the permitted workspace.

Completion: the source branch and commit, destination repository, and target
branch are verified.

## 2. Inspect the destination

Read the target ref directly from the destination, not a cached remote-tracking
ref. Inspect its linked worktrees and their status read-only. Stop if the target
branch is checked out with staged, unstaged, or untracked changes, or an
unfinished Git operation. Leave worktrees on other branches untouched.

Linked worktrees share refs and objects. If the source and target name the same
shared ref, commits are already available in the original repository; no
transfer is needed. For separate clones, read the ref with
`git ls-remote --heads <destination> refs/heads/<target>` and fetch that branch
into the source's `FETCH_HEAD` when needed to compare ancestry.

Capture the exact source and target commit IDs. An absent target is distinct
from a failed ref lookup.

Completion: the observed target commit or verified absence is known, and every
checkout of that branch is accounted for.

## 3. Choose the update

- Equal commits: report that the branch is already synced; perform no update.
- Target ahead of source: stop rather than remove destination commits.
- Target absent or an ancestor of source: perform a fast-forward transfer.
- Diverged histories: show both commit IDs and destination-only commits. Ask
  for explicit approval to replace that target branch, even after a rebase.

For linked worktrees with a different target branch:

- If the target is checked out and clean, fast-forward from that worktree with
  `GIT_EDITOR=true git -C <target-worktree> merge --ff-only <source-commit>`.
  Recheck its branch and HEAD immediately before running the command.
- If the target is not checked out, update the shared ref with
  `git update-ref refs/heads/<target> <source-commit> <observed-target-commit>`.
  For a new branch, use an all-zero old object ID of the repository's object
  format. This comparison prevents overwriting an intervening update.
- A history replacement requires the target to be unchecked-out first. Ask
  the user to arrange that; this skill does not switch their worktrees.

For separate clones, push the captured commit to the verified local destination:

```bash
git push <destination> <source-commit>:refs/heads/<target>
```

After explicit approval of a history replacement, use an exact lease:

```bash
git push --force-with-lease=refs/heads/<target>:<observed-target-commit> <destination> <source-commit>:refs/heads/<target>
```

Recheck the source, target ref, and target checkout state before updating. If
any changed, inspect again and obtain fresh approval for a history replacement.
If Git rejects the update, stop and explain the rejection. Preserve checkout
protections; do not change Git configuration, reset, clean, stash, or switch
the destination to bypass them.

Completion: the update succeeded or stopped with a specific reason.

## 4. Verify and report

Read the destination ref again and confirm it equals the captured source commit.
If the target is checked out, verify that worktree's HEAD and status read-only.
Report the source, target, destination, and verified commit. Keep existing test
evidence separate from transfer verification; syncing alone requires no code
changes or test rerun.

Give a plain summary for a completed transfer or a terminal failure. An
already-synced branch is a no-op, not a landing.
