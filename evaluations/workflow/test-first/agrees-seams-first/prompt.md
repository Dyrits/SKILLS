---
description: A TDD request with no agreed seams should name the seams under test before writing any test.
tags: [workflow, test-first]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

Use TDD to add a discount feature to our checkout: a code like SAVE10 takes 10 percent off the cart total, a code can be used once per customer, and expired codes are rejected. I do not have a design document for this.
