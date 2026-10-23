---
name: resolve-merge-conflicts
description: "Resolve an in-progress git merge or rebase conflict. Use when a merge, rebase, cherry-pick, or pull stops on conflict markers or unmerged paths."
---

# Resolve merge conflicts

1. **Resolve the conflicts** following [resolve-conflicts.md](references/resolve-conflicts.md). The goal is the one stated for the operation: by the user, the branch, or the pull or merge request.

2. Before its step 4 continues each stopped commit, discover the project's **automated checks** and run them, typically typecheck, then tests, then format. Fix anything the resolution broke.

Completion: the procedure's completion holds, and the checks from step 2 pass or each failure is reported with its evidence.
