# Rebase the source onto the target

Adapted from the `rebase` skill, for one source branch in its own worktree. The **target pin** is the exact target commit captured in step 2: the target branch tip for linked worktrees, or the fetched target commit for separate clones. Nothing is pushed.

## Rebase and resolve

1. Verify that the source checkout is on its branch at the captured source commit, with a clean index and working tree and no Git operation in progress, and that the target pin exists as a commit.
2. Run `GIT_EDITOR=true git -c rebase.updateRefs=false rebase --no-autostash "$target_pin"`. The override keeps user configuration from moving other local branches.
3. When Git stops on conflicts, resolve them by intent:
   1. See the commit being applied, the history on both sides, and the conflicting files.
   2. Find the primary sources for each conflict: commit messages, and the pull or merge requests and issues or tickets when reachable. Missing tracker access is not a Git failure; use commit messages, diffs, and local specifications where they establish intent.
   3. Resolve each hunk. Preserve both intents where possible. Where they are incompatible, pick the one that keeps the target's commits and replays the source's intent on top of them, and note the trade-off. Do **not** invent new behaviour. When intent stays uncertain, or the choice needs a product decision, stop, ask the user one precise question, and leave the rebase in progress. Never `--abort` on your own.
   4. Stage only the conflict paths you reviewed and run `GIT_EDITOR=true git rebase --continue`, repeating until every commit is rebased.

Completion: every commit is accounted for and Git reports no unfinished rebase and no unmerged entries. Otherwise the rebase is blocked on a question, and no update is made.

## Validate the new tip

- The target pin is an ancestor of the new tip. Review `git range-diff "$(git merge-base "$target_pin" "$old_source")..$old_source" "$target_pin..$new_tip"` and explain every changed or dropped patch, including patches already present in the target.
- The source's intent and the target's relevant changes both survive. A passing test suite does not explain a lost patch.
- The repository's relevant checks pass on the new tip. Discover them from repository instructions and configuration, and write generated output inside the source checkout only.
- `git diff --check "$target_pin..$new_tip"` passes.

When a check fails, find out whether it already fails at the old source tip or at the target pin, and report the evidence. A failure stays a failure in the report; only the user can waive it.

Report the old and new source tips, each conflict and its decision, the `range-diff` explanation, and each check with its result.
