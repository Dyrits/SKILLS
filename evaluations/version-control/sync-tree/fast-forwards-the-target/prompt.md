---
description: A request to sync a finished worktree should fast-forward its recorded target branch without a merge commit.
tags: [version-control, sync-tree]
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Sync the worktree at .worktrees/notes back to its branch in this checkout.
