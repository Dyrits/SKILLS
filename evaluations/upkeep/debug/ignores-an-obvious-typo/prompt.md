---
description: An error whose cause is visible in the message must not run the debug skill.
tags: [upkeep, debug]
max_turns: 5
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

Python says `NameError: name 'prnt' is not defined` for the line `prnt("hi")`. What's wrong?
