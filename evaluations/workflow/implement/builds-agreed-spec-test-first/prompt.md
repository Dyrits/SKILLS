---
description: An agreed small specification should be built test-first, with a report of what was verified and what could not run.
tags: [workflow, implement]
max_turns: 25
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Implement this agreed specification in Python in the current directory. Behavior: `slugify(text)` lowercases the text, replaces each run of non-alphanumeric characters with a single hyphen, and strips leading and trailing hyphens. Acceptance: `slugify("Hello, World!")` returns `hello-world`; `slugify("  a  b ")` returns `a-b`; `slugify("")` returns the empty string. Nothing else is in scope.
