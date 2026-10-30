---
description: A request for a guided setup of third-party credentials should list the ordered stages and values, then wait for confirmation before writing the wizard.
tags: [productivity, walk-through]
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

I need to set up Stripe for our app and I always forget the clicks. Make me a script that walks me through it step by step. The app needs STRIPE_SECRET_KEY and STRIPE_WEBHOOK_SECRET in a local .env file, and CI needs STRIPE_SECRET_KEY as a GitHub Actions secret. I will be doing this in Stripe's test mode first.
