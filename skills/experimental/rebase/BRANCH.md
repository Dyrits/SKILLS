# Rebase one branch

Work in the branch's assigned checkout, on the branch itself. Update the branch's record file at each phase boundary; it lives outside the checkout, so the tree stays clean. Return evidence; pushing belongs to the coordinator.

## Rebase and resolve

1. Verify that the checkout is on `refs/heads/<name>` at the recorded start, with a clean index and working tree and no Git operation in progress. Verify that the target pin exists as a commit.
2. Run `GIT_EDITOR=true git -c rebase.updateRefs=false rebase --no-autostash "$target_pin"`. Add `--rebase-merges` or, for an approved stack, `--update-refs` in place of the `-c` override, when the record says so. The override keeps user configuration from moving other local branches.
3. When Git stops on conflicts, call the Skill tool with `resolve-merge-conflicts`. Give it the target pin as the goal and both histories. It owns intent-led resolution and continuation through the remaining commits. Keep `GIT_EDITOR=true` on every command that can open an editor.
4. Replace that skill's final "stage everything and commit" with: stage only the reviewed conflict paths and run `git rebase --continue`, which keeps each commit's own message and order. Missing tracker access is not a Git failure: use commit messages, diffs, and local specifications where they establish intent. When intent stays uncertain or needs a product decision, stop with a precise question and leave the rebase in progress, so the user can resume from that exact commit.

Completion: every commit is accounted for and Git reports no unfinished rebase and no unmerged entries. Otherwise record `blocked` with the current commit and the question.

## Validate the new tip

Validation applies to every rebased branch, conflicts or not. Record the new tip and establish all of the following:

- The target pin is an ancestor of the new tip. Review `git range-diff "$old_base..$start" "$target_pin..$new_tip"` and explain every changed or dropped patch, including patches already present in the target. For `--rebase-merges`, also inspect the graph and each merge resolution, which `range-diff` does not cover.
- The original intent of the branch and the target's relevant changes both survive. Add focused regression coverage when a resolution changes behaviour. A passing test suite does not explain a lost patch.
- The repository's relevant checks pass on the new tip, conflict-sensitive tests included. Discover them from repository instructions and configuration. Install dependencies and write generated output inside this checkout only.
- `git diff --check "$target_pin..$new_tip"` passes. Commit any fix the checks require and validate the new tip again.

When a check fails, find out whether it already fails at the start or at the target pin, in a separate worktree, and record the evidence. A failure stays a failure in the report, whatever its origin; only the user can waive it.

Completion: the new tip has intent-preservation evidence and passing checks, recorded as `rebased and validated`. Otherwise record `rebased, checks failing` with the failing or missing checks.

## Return

Report the start and new tip, the conflicts and each decision, the `range-diff` explanation, each check with its result, and the status.
