---
name: rebase
description: "Rebase local branches in place onto one target, resolve conflicts, run checks, then push with force-with-lease on approval. Use when the user asks to rebase branches onto a target."
argument-hint: "branch... --onto target [--remote remote]"
---

# Rebase in place

Rebase each named local branch onto one target so the branch itself moves. Resolve conflicts by intent, validate every result, report, and push only the branches the user approves.

Accept branches and a target in natural language or as `/rebase fix/a feat/b --onto origin/develop`. `--remote` names the publication remote when a branch has no upstream or an ambiguous one. `--onto` names the target, not Git's three-argument transplant.

## 1. Establish the batch

Read repository instructions. Inspect `git status`, `git worktree list`, remotes, and each branch's upstream. Resolve every input to a local branch `refs/heads/<name>` and, where one exists, its publication remote and full destination ref. A remote name such as `origin/feature` maps to its local branch; ask before creating a local branch that does not exist yet. Deduplicate, drop the target from the set, and ask about anything missing or ambiguous before changing anything.

Where a branch is checked out decides where it rebases:

| Branch location | Rebase location |
| --- | --- |
| Not checked out anywhere | A new linked worktree on that branch, in the host's temporary or state directory: `git worktree add "$batch_dir/<name>" <name>` |
| Checked out in a clean checkout with no Git operation in progress | That checkout, the current one included |
| Checked out in a checkout with uncommitted work or an operation in progress | Ask whether to commit, stash, or skip; the uncommitted work stays the user's |

Completion: every branch has one rebase location and either a publication destination or a `local only` mark.

## 2. Pin the inputs

Fetch the target and every upstream. Capture full commit IDs: one **target pin** shared by every branch even if the target advances, each branch's **start** (its local tip), and its **lease** (the remote tip just fetched, when one exists).

| Local branch against its remote | Action |
| --- | --- |
| Equal, ahead, or no remote | Rebase the local branch as it is |
| Behind or diverged | Ask whether to bring the remote commits in first; a branch pushed without them deletes them from the remote, so record the answer |

Record each branch's old merge base with the target. Check its commit range for merge commits and ask whether to keep them with `--rebase-merges`. Check for branches in the batch that sit on top of each other: ask, then treat that **stack** as one unit rebased from its top with `--update-refs`.

Create a backup ref per branch with `git update-ref "refs/rebase-backup/<name>" "$start"`, so every rebase can be undone. Create a batch directory in the host's temporary or state directory, outside every checkout, with one record file per branch: location, start, lease, old merge base, approved answers, phase, new tip, check results, push result.

Completion: every ready branch has its pins, lease, backup ref, and record; every other branch is marked `blocked` with one specific question.

## 3. Rebase

For a single branch, rebase it yourself by following [BRANCH.md](references/BRANCH.md).

For several, rebase the ones located in a user checkout yourself and dispatch one subagent per worktree-located branch at the same time, bounded only by resource limits. Give each subagent its worktree path, its record path, the repository instructions, and [BRANCH.md](references/BRANCH.md) with [RESOLVE.md](references/RESOLVE.md), which it reads before acting. Dispatch plain subagents that work in the assigned worktree: a harness-managed isolated worktree would rebase a copy on another branch instead of the branch itself. Subagents report evidence and leave pushing to you.

Wait for completion notifications. A quiet subagent is unconfirmed, not running; report its last recorded phase.

Completion: every branch has a status of `rebased and validated`, `already up to date`, `rebased, checks failing`, or `blocked`.

## 4. Report and ask

Show one table: branch, start, new tip, conflicts and their key decisions, check results, push destination, status. Add the target pin, the batch directory, and the undo command for each rebased branch: `git reset --keep refs/rebase-backup/<name>` in its checkout, or `git branch -f <name> refs/rebase-backup/<name>` when it is not checked out.

Then ask which branches to push. Offer only `rebased and validated` branches with a destination, plus `rebased, checks failing` branches for which the user explicitly waives the named failing checks.

Completion: the user has answered.

## 5. Push the approved branches

For each approved branch, confirm the local branch still equals its validated tip, then push from the repository with the lease captured in step 2:

```sh
git -c push.followTags=false push \
  --force-with-lease="$destination_ref:$lease" \
  --recurse-submodules=no "$remote" "refs/heads/$name:$destination_ref"
```

`$destination_ref` is the full `refs/heads/...` ref. A branch with no remote yet uses `--force-with-lease="$destination_ref:"`, which requires the ref to be absent. The explicit lease protects the remote value captured before work began, even if a background fetch moved the tracking refs. Plain `--force` stays out of this skill.

| Result | Action |
| --- | --- |
| Push succeeds | Read the destination with `git ls-remote --refs`; mark `pushed and verified` only if it equals the new tip |
| Lease rejected | Report that the remote moved, keep the rebased branch, and ask how to reconcile |
| Authentication, hook, or policy failure | Report the actual Git error |
| Result or readback uncertain | Mark `unknown` and reconcile remote state before any retry |

Remove each worktree this skill created once its branch is done, with `git worktree remove`. Offer to delete the backup refs; keep them unless the user agrees.

Completion: every branch in the batch appears in a final table with its observed state, and the user knows where the backup refs and records are.

If execution was interrupted, read [RESUME.md](references/RESUME.md) before touching any branch.
