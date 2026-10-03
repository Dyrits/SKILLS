# Milestone review

Use this branch at an agreed milestone, before delivery, or after substantial structural or data-risk changes. Review complements executable checks and user acceptance; each supplies different evidence.

## Prepare the review

Name the capability and paths under review. Supply the starting revision and the originating agreed behavior, including accepted changes, unresolved choices, and constraints. Preserve those requirements before pruning working notes: a reviewer must not reconstruct user intent from the implementation.

Reuse existing relevant requirements and specifications, test cases, working notes, architecture decision records, and recorded approvals as evidence. Link those sources when useful. Create a short milestone behavior record under `documentation/` only when those sources cannot recover the agreement. A feature specification or task document is not a prerequisite for review. Reference implementation details instead of duplicating them.

For a versioned project, record the current goal's starting revision before its first implementation batch, even when delivery is not yet scheduled. Use that baseline for a later delivery review, or record a narrower starting revision when a milestone's first batch is agreed. Pass the chosen fixed point to the review. Restrict the review to the current project's paths and owned changes, including new files. Preserve unrelated workspace edits.

## Run and resolve

When available, call the Skill tool with "code-review-and-refactor", supplying the fixed point, review scope, behavior evidence, and documented standards. Its Standards and Specifications reviewers inspect the same starting changes; the coordinator checks findings and applies supported refactors, then reuses those reviewers for verification.

If the skill or its prerequisites are unavailable, identify the limitation. Agree a lighter bounded review using captured starting contents and the same behavior evidence, with an independent reviewer when supported. Establish a usable baseline before claiming comparison against one; initializing version control is a separate choice, not a hidden prerequisite.

Keep refactors within agreed behavior and approach. Findings requiring a new product choice or technical migration return to the user; they are proposed future work, not automatic authorization. Routine fixes within scope can proceed, followed by relevant checks.

Completion: supported findings are resolved and verified, or explicitly deferred with reasons and risks. Record the review scope, outcome, remaining concerns, and evidence pointers in working state or lasting milestone documentation. Report a review that lacked recoverable agreed-behavior evidence or independence as limited, rather than equivalent to the full discipline.
