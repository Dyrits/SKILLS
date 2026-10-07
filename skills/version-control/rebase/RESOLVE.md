# Resolve rebase conflicts

Adapted from the `resolve-merge-conflicts` skill, for a rebase whose goal is the target pin.

1. **See the current state** of the rebase: the commit being applied, the history on both sides, and the conflicting files.
2. **Find the primary sources** for each conflict. Understand why each change was made and what its original intent was: read the commit messages, and check the pull or merge requests and the original issues or tickets when they are reachable.
3. **Resolve each hunk.** Preserve both intents where possible. Where they are incompatible, pick the one matching the rebase's goal and note the trade-off. A goal that names no outcome for the conflicting value ("bring the target's changes in") settles nothing. Do **not** invent new behaviour. Resolve every hunk you can. When intent stays uncertain after the primary sources, or the choice needs a product decision, stop, ask the user one precise question, and leave the rebase in progress. Never `--abort` on your own.
4. **Continue.** Stage only the conflict paths you reviewed, then run `GIT_EDITOR=true git rebase --continue`, which keeps each commit's own message and order. Repeat from step 1 for each commit that stops, until all commits are rebased.

Checks run once on the new tip, in the validation phase, not after each commit.
