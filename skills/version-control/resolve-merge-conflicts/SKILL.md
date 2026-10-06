---
name: resolve-merge-conflicts
description: "Resolve an in-progress git merge or rebase conflict. Use when a merge, rebase, cherry-pick, or pull stops on conflict markers or unmerged paths."
---

1. **See the current state** of the merge/rebase. Check git history, and the conflicting files.

2. **Find the primary sources** for each conflict. Understand deeply why each change was made, and what the original intent was. Read the commit messages, check the PRs, check original issues/tickets.

3. **Resolve each hunk.** Preserve both intents where possible. Where incompatible, pick the one matching the merge's stated goal and note the trade-off. A goal that names no outcome for the conflicting value ("bring main's changes in") settles nothing. Do **not** invent new behaviour. Resolve every hunk you can. When intent stays uncertain after the primary sources, or the choice needs a product decision, stop, ask the user one precise question, and leave the merge or rebase in progress. Never `--abort` on your own.

4. Discover the project's **automated checks** and run them, typically typecheck, then tests, then format. Fix anything the merge broke.

5. **Finish the merge/rebase.** Stage only the conflict paths you reviewed. For a merge, commit. For a rebase, run `git rebase --continue` (keeping `GIT_EDITOR=true` on commands that can open an editor), which keeps each commit's own message and order, until all commits are rebased.
