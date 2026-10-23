# Resolve conflicts

For a merge, rebase, cherry-pick, or pull that Git stopped on conflicts. The document that sends you here names the operation's **goal**; when it names none, the goal is the one the user stated for the operation.

1. **See the current state**: which operation is in progress (merge, rebase, cherry-pick, or a pull that merged or rebased), the commit being applied, the history on both sides, and the conflicting files.
2. **Find the primary sources** for each conflict. Understand why each change was made and what its original intent was: read the commit messages, and check the pull or merge requests and the original issues or tickets when they are reachable. Missing tracker access is not a Git failure; use commit messages, diffs, and local specifications where they establish intent.
3. **Resolve each hunk.** Preserve both intents where possible. Where they are incompatible, pick the one matching the goal and note the trade-off. A goal that names no outcome for the conflicting value ("bring the target's changes in") settles nothing. Do **not** invent new behaviour. Resolve every hunk you can. When intent stays uncertain after the primary sources, or the choice needs a product decision, stop, ask the user one precise question, and leave the operation in progress. Never `--abort` on your own.
4. **Continue the operation.** Stage only the conflict paths you reviewed, then keep `GIT_EDITOR=true` on each command so it keeps the existing message instead of opening an editor:
   - merge (including a merging pull): `git commit`;
   - rebase (including a rebasing pull): `git rebase --continue`, repeating from step 1 for each commit that stops, until all commits are rebased;
   - cherry-pick: `git cherry-pick --continue`, repeating from step 1 for each picked commit that stops.

Completion: Git reports no operation in progress and no unmerged paths, and every hunk's decision and trade-off is recorded for the report. Otherwise the operation is left in progress on one precise question to the user.
