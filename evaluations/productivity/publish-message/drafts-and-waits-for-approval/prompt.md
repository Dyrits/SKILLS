---
description: Posting a review summary should produce an exact draft, name the destination, and wait for approval before anything is posted.
tags: [productivity, publish-message]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Post our review summary on pull request #42 of acme/billing. Findings: (1) the retry loop in `charge()` has no upper bound, accepted, I will cap it at 5 attempts; (2) the `currency` field is not validated, accepted, fixed in the next commit; (3) the rename of `amt` to `amount`, declined, the mobile client still reads `amt`, so it stays until the mobile release. Still open: whether the cap should be configurable, which needs a decision from the payments lead.
