---
description: A request to work in a worktree should create a linked worktree on a new branch, commit there, record the return route, and leave the checkout alone.
tags: [version-control, work-in-tree]
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Work in a worktree for this: add a NOTES.md file containing "Release checklist" and commit it on a new branch. Put the worktree at .worktrees/notes inside this directory, since writes outside it are blocked. Leave this checkout untouched.
