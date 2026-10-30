---
description: A request for a handoff should write a dated handoff file with the fixed sections and add a pointer line to AGENTS.md.
tags: [productivity, hand-off]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Write a handoff for this session, we are stopping here. Keep handoffs shared and committed, no need to ask about that. Summary: we are migrating the API from Express to Fastify on branch `fastify-migration`. The `/users` and `/health` routes are ported. I ran `npm test` earlier today and it passed (41 tests), but I have not rerun it since the last change. `/orders` is not started. We decided to keep the existing Joi validation schemas instead of moving to JSON Schema, because the mobile team shares them. Open question: whether the auth middleware can stay as an Express-style plugin or must be rewritten, which the platform lead has to answer. The next session should port `/orders` first. Sources: `docs/migration-plan.md` and issue #118.
