---
description: A request to prove a change works should list claims with sources and refuse to call anything proven without observation.
tags: [workflow, verify]
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

I just changed our CLI so that `export --format json` prints valid JSON and exits with code 2 on an unknown format. Please verify it actually works before I merge. Do not just tell me it looks fine.
