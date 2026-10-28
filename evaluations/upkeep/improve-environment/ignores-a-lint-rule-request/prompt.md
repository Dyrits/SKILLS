---
description: A request for one lint rule must not run the environment retrospective.
tags: [upkeep, improve-environment]
max_turns: 5
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

Give me the ESLint flat-config entry that bans console.log. Just the snippet.
