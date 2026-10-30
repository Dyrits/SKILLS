---
description: An authorized task graph should get a routing table with tiers and blockers, and a request for approval before anything is dispatched.
tags: [workflow, divide-and-conquer]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

The tasks below are approved and ready. Implement all of them in parallel with the cheapest agents that can do each reliably.

1. Rename the config key `timeout` to `timeout_seconds` across the service (mechanical, no blockers).
2. Add a CSV export endpoint for invoices (no blockers).
3. Make the export endpoint stream rows instead of buffering, which needs task 2.
4. Redesign the retry policy of the payment webhook handler, with unclear failure semantics (no blockers).
