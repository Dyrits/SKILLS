---
description: A bug with an unknown cause should get a reproduction that fails before the fix, then a fix and a regression check.
tags: [upkeep, debug]
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Debug this: in our checkout service, the first customer using the code SAVE10 pays 90 for a 100 basket, as expected. But later customers who use no code at all also get a discount. The code is in pricing.py.
