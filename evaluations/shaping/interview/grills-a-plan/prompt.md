---
description: A plan to stress-test should get numbered questions with recommended answers, and no decision taken for the user.
tags: [shaping, interview]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Grill me on this plan before I commit to it. Next month we move our nightly cron jobs (invoice generation, report emails, data cleanup) from a single server to a queue-based worker system on our existing Postgres, with retries and a dead-letter table. Two developers, no downtime allowed.
