---
description: A request to fix an AGENTS.md that agents ignore should sharpen the pointer wording and prune what the environment already states.
tags: [productivity, write-for-agents]
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill]
---

Agents keep ignoring our testing guide. Fix this AGENTS.md:

```markdown
# AGENTS.md

This repository is a TypeScript API. Please note that it is important to read about testing somewhere.

- Run `npm test` to run the tests (the `test` script in package.json runs vitest).
- Testing information, test guidance, and testing documentation are in docs/testing.md.
- The main language is TypeScript.
- The tests are in the tests folder.
- Never mock the database; use the test containers described in docs/testing.md.
```
