# Rebase the source onto the target

Adapted from the `rebase` skill, for one source branch in its own worktree. The **target pin** is the exact target commit captured in step 2: the target branch tip for linked worktrees, or the fetched target commit for separate clones. Nothing is pushed.

## Rebase and resolve

1. Verify that the source checkout is on its branch at the captured source commit, with a clean index and working tree and no Git operation in progress, and that the target pin exists as a commit.
2. Run `GIT_EDITOR=true git -c rebase.updateRefs=false rebase --no-autostash "$target_pin"`. The override keeps user configuration from moving other local branches.
3. When Git stops on conflicts, resolve them following [resolve-conflicts.md](resolve-conflicts.md). The goal is to keep the target's commits and replay the source's intent on top of them. Checks run once on the new tip, in the validation below.

Completion: every commit is accounted for and Git reports no unfinished rebase and no unmerged entries. Otherwise the rebase is blocked on a question, and no update is made.

## Validate the new tip

- The target pin is an ancestor of the new tip. Review `git range-diff "$(git merge-base "$target_pin" "$old_source")..$old_source" "$target_pin..$new_tip"` and explain every changed or dropped patch, including patches already present in the target.
- The source's intent and the target's relevant changes both survive. A passing test suite does not explain a lost patch.
- The repository's relevant checks pass on the new tip. Discover them from repository instructions and configuration, and write generated output inside the source checkout only.
- `git diff --check "$target_pin..$new_tip"` passes.

When a check fails, find out whether it already fails at the old source tip or at the target pin, and report the evidence. A failure stays a failure in the report; only the user can waive it.

Report the old and new source tips, each conflict and its decision, the `range-diff` explanation, and each check with its result.
