---
description: A capability with open behavior decisions should get questions with recommendations on observable behavior, not a design.
tags: [workflow, specify]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

Specify the "password reset by email" capability for our web app. Users who forgot their password get a link by email. I have not decided what happens with expired links, unknown email addresses, or repeated requests, and I am not sure whether the user should be signed in afterwards.
