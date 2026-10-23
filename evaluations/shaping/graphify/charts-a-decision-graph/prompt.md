---
description: An explicit request to chart a large effort should write a local map whose tasks are decisions, not implementation slices.
tags: [shaping, graphify]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

Graphify this effort for me: we want to replace our homegrown authentication with an external identity provider. Open questions include which provider, how existing sessions migrate, how roles map, whether local passwords survive, and how the mobile clients log in. It is too big for one session. There is no task tracker configured here, so keep the graph local. Chart the map and its decision tasks now.
