---
name: to-specifications
description: "Turn the current conversation into a specification: keep it in the configured local refinement workspace as a draft, or publish it to the project issue tracker when explicitly requested. No interview, just synthesis of what you've already discussed."
disable-model-invocation: true
---

This skill takes the current conversation context and codebase understanding and produces a specification. Do NOT interview the user; just synthesize what you already know.

The issue tracker, publication boundary, and triage label vocabulary should have been provided to you. If not, ask the user whether to run `/setup-custom-skills` now; if they decline, stop and tell them this skill needs it before continuing.

## Process

1. Resolve the destination from `documentation/agents/issue-tracker.md`:

   - When local refinement drafts are configured, write to `.refinement/<issue-key>/specification.md`, or `.refinement/<feature-slug>/specification.md` when no source issue exists. This is the default until the user explicitly requests publication.
   - When direct publication is configured, publish to the system-of-record tracker.
   - A request such as "publish", "update Jira", or "create the issue" explicitly selects the system-of-record tracker.

   When refining an existing issue, fetch its full body and comments through the configured access method before drafting. Put `Source: <issue-key> (<url or repository-relative ticket path>)` and `Status: draft` at the top of a local specification. Refinement applies to both remote and local trackers; publishing to a local tracker writes the configured specification under `backlog/` and links the draft to that authoritative artifact.

2. Explore the repository to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the specification, and respect any ADRs in the area you're touching.

3. Sketch out the seams at which you're going to test the feature. Existing seams should be preferred to new ones. Use the highest seam possible. If new seams are needed, propose them at the highest point you can. The fewer seams across the codebase, the better - the ideal number is one.

Check with the user that these seams match their expectations.

4. Write the specification using the template below, then save or publish it at the resolved destination. Apply the `ready-for-agent` triage label only when publishing to the project issue tracker. For a local draft, report its path and leave the configured tracker unchanged, including a local `backlog/`.

<specification-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A LONG, numbered list of user stories. Each user story should be in the format of:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

This list of user stories should be extremely extensive and cover all aspects of the feature.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- Prior art for the tests (i.e. similar types of tests in the codebase)

## Out of Scope

A description of the things that are out of scope for this specification.

## Further Notes

Any further notes about the feature.

</specification-template>
