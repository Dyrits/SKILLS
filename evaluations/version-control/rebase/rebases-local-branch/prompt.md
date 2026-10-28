---
description: A request to rebase a checked-out branch onto main should rebase it in place, keep a backup ref, and push nothing.
tags: [version-control, rebase]
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Rebase the feature branch onto main. There is no remote, so keep it local.
