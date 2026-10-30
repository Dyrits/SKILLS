---
description: A new system with stated requirements should get a decision tree with real alternatives, a simplest-fit recommendation, and questions for the user, not a settled design.
tags: [workflow, architect]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

We are starting a booking system for about 40 yoga studios. Studio owners manage classes and members book and pay online. We expect roughly 5,000 members at launch, payments must go through Stripe, member data must stay in the EU, and two developers will build and run it. Nothing is built yet. What architecture should we use?
