---
description: A branch review request with no fixed point should ask for one and make no findings or edits from code it has not seen.
tags: [workflow, review-and-refactor]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Review and refactor my branch feature/csv-export against its specification: the export must include a header row, escape commas and quotes, and stream rows without loading the whole table. Apply any refactors that are supported.
