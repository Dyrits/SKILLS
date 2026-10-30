---
description: Approved specifications should become a proposed set of verifiable tasks with blockers, awaiting approval before saving.
tags: [workflow, taskify]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

Break this approved scope into tasks. Capability: invoice reminders. Agreed behavior: an invoice unpaid 7 days after its due date triggers one reminder email to the billing contact; a second reminder is sent at 14 days; no reminders for invoices marked disputed; the owner can switch reminders off per customer. Acceptance is written per behavior in the specification. The service has an existing email sender and a customers table.
