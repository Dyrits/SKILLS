---
description: A specified capability should get a module design with recommendations and open decisions, and no production code.
tags: [workflow, engineer]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

Design how we build the "waitlist" capability before anyone writes code. Behavior is agreed: when a class is full a member can join its waitlist; when a spot opens, the first member on the list is offered it and has 30 minutes to accept, otherwise the next member is offered it. Acceptance: joining a full class puts you at the end of the list; an offer expires after 30 minutes; accepting an offer books the member. The system is a single Django app with one Postgres database. Where should the modules, interfaces and tests go?
