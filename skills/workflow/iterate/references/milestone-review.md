# Milestone review

Use this branch at an agreed milestone, before delivery, or after substantial structural or data-risk changes. Review complements executable checks and user acceptance; each supplies different evidence.

## Prepare the review

Name the capability and paths under review. Supply the starting revision and the agreed behavior, including accepted changes, open choices, and constraints. Capture that agreement before pruning working notes, so the reviewer reads intent from records instead of reconstructing it from the implementation.

Use existing requirements, specifications, test cases, working notes, architecture decision records, and recorded approvals as evidence, with pointers to them. Write a short milestone behavior record under `documentation/` only when those sources cannot recover the agreement, and add its `AGENTS.md` line as [project-documents.md](project-documents.md) describes.

In a versioned project, the goal's starting revision recorded before its first batch is the baseline for a later delivery review; record a narrower one when a milestone's first batch is agreed. Pass the chosen fixed point to the review. Restrict the review to this project's paths and owned changes, including new files, and leave unrelated workspace edits alone.

## Run and resolve

Review and refactor following [review.md](review.md), with the fixed point, review scope, behavior evidence, and documented standards.

Without a usable baseline, say so and agree a lighter review with the user, using captured starting contents and the same behavior evidence, with an independent reviewer when supported. Initializing version control is a separate choice for the user.

Keep refactors within the agreed behavior and approach. Findings that need a new product choice or technical migration go back to the user as proposed work. Routine fixes within scope proceed, followed by relevant checks.

Completion: supported findings are resolved and verified, or deferred with reasons and risks. Record the review scope, outcome, remaining concerns, and evidence pointers in working state or lasting milestone documentation. Report a review that lacked recoverable behavior evidence or independence as limited.
