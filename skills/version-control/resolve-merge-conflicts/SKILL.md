---
name: resolve-merge-conflicts
description: "Resolve an in-progress git merge or rebase conflict. Use when a merge, rebase, cherry-pick, or pull stops on conflict markers or unmerged paths."
---

# Resolve merge conflicts

1. **See the current state** of the operation: which one is in progress (merge, rebase, cherry-pick, or a pull that merged or rebased), the commit being applied, the history on both sides, and the conflicting files.

2. **Find the primary sources** for each conflict. Understand deeply why each change was made, and what the original intent was. Read the commit messages, and check the pull or merge requests and the original issues or tickets when they are reachable.

3. **Resolve each hunk.** Preserve both intents where possible. Where incompatible, pick the one matching the operation's stated goal and note the trade-off. A goal that names no outcome for the conflicting value ("bring main's changes in") settles nothing. Do **not** invent new behaviour. Resolve every hunk you can. When intent stays uncertain after the primary sources, or the choice needs a product decision, stop, ask the user one precise question, and leave the operation in progress. Never `--abort` on your own.

4. Discover the project's **automated checks** and run them, typically typecheck, then tests, then format. Fix anything the resolution broke.

5. **Finish the operation.** Stage only the conflict paths you reviewed, then keep `GIT_EDITOR=true` on each command so it keeps the existing message instead of opening an editor:
   - merge (including a merging pull): `git commit`;
   - rebase (including a rebasing pull): `git rebase --continue`, repeating from step 1 for each commit that stops, until all commits are rebased;
   - cherry-pick: `git cherry-pick --continue`, repeating from step 1 for each picked commit that stops.

Completion: Git reports no operation in progress and no unmerged paths, the checks from step 4 pass or each failure is reported with its evidence, and every hunk's decision and trade-off is in your report. Otherwise the operation is left in progress on one precise question to the user.
