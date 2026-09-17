---
name: to-tickets
description: Break a plan, specification, or the current conversation into tracer-bullet tickets, each declaring its blocking edges, saved as local refinement drafts or published to the configured tracker when explicitly requested.
disable-model-invocation: true
---

# To Tickets

Break a plan, specification, or conversation into a set of **tickets**: tracer-bullet vertical slices, each declaring the tickets that **block** it.

The issue tracker, publication boundary, ticket-writing convention, and triage label vocabulary should have been provided to you. If not, ask the user whether to run `/setup-custom-skills` now; if they decline, stop and tell them this skill needs it before continuing.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a specification path, an issue number or URL) as an argument, fetch it and read its full body and comments.

Read the "Ticket writing convention" section of `documentation/agents/issue-tracker.md`. It names either the built-in templates below or an optional project convention such as an issue-template document or a ticket-writing skill. If the configured convention points to another source, read that source before drafting.

Confirm the convention with the user before applying it. Present the configured convention as the recommendation and the built-in `to-tickets` format as the fallback. A named skill supplies ticket structure and quality rules only; this skill still owns decomposition, blocking edges, approval of the breakdown, and the save-versus-publish boundary. If the tracker configuration predates this setting, ask which convention to use for this run, then continue without requiring the user to re-run setup.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Ticket titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

Look for opportunities to prefactor the code to make the implementation easier. "Make the change easy, then make the easy change."

### 3. Draft vertical slices

Break the work into **tracer bullet** tickets.

<vertical-slice-rules>

- Each slice cuts a narrow but COMPLETE path through every layer (schema, API, UI, tests): vertical, NOT a horizontal slice of one layer
- A completed slice is demoable or verifiable on its own
- Each slice is sized to fit in a single fresh context window
- Any prefactoring should be done first

</vertical-slice-rules>

Give each ticket its **blocking edges**: the other tickets that must complete before it can start. A ticket with no blockers can start immediately.

**Wide refactors are the exception to vertical slicing.** A **wide refactor** is one mechanical change (rename a column, retype a shared symbol) whose **blast radius** fans across the whole codebase, so a single edit breaks thousands of call sites at once and no vertical slice can land green. Don't force it into a tracer bullet; sequence it as **expand–contract**. First expand: add the new form beside the old so nothing breaks. Then migrate the call sites over in batches sized by blast radius (per package, per directory), each batch its own ticket blocked by the expand, keeping CI green batch to batch because the old form still exists. Finally contract: delete the old form once no caller remains, in a ticket blocked by every migrate batch. When even the batches can't stay green alone, keep the sequence but let them share an integration branch that all block a final integrate-and-verify ticket; green is promised only there.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each ticket, show:

- **Title**: short descriptive name
- **Blocked by**: which other tickets (if any) must complete first
- **What it delivers**: the end-to-end behaviour this ticket makes work

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct: does each ticket only depend on tickets that genuinely gate it?
- Should any tickets be merged or split further?

Iterate until the user approves the breakdown.

### 5. Save or publish the tickets

Resolve the destination from `documentation/agents/issue-tracker.md`. When local refinement drafts are configured, save there by default. Publish to the system-of-record tracker only when the user explicitly asks to publish, create, or update its issues. The tickets are the same either way; only their destination and the shape of the blocking edges change:

- **Local drafts** → write one file per ticket under `.scratch/<issue-key>/issues/<NN>-<slug>.md`, or `.scratch/<feature-slug>/issues/<NN>-<slug>.md` when no source issue exists. Number from `01` in dependency order (blockers first). Each file's "Blocked by" lists the numbers/titles it depends on. Use the per-ticket file template below: one ticket per file, never a single combined file.
- **A real issue tracker (GitHub, Linear, …)** → publish one issue per ticket in dependency order (blockers first) so each ticket's blocking edges can reference real identifiers. Use the platform's native blocking / sub-issue relationship where it has one; otherwise set each ticket's "Blocked by" to the blocking issues. Apply the `ready-for-agent` triage label unless instructed otherwise; the tickets are agent-grabbable by construction.

When saving local drafts sourced from a tracker issue, include `Source: <issue-key> (<url>)` and `Status: draft` near the top of every ticket. Report the local paths and leave the remote tracker unchanged. Render every ticket with the approved writing convention, while retaining an explicit "Blocked by" field and acceptance criteria even when the selected template uses different headings.

Work the **frontier**: any ticket whose blockers are all done. For a purely linear chain that means top to bottom.

Do NOT close or modify any parent issue.

<local-ticket-template>

# <NN>: <Ticket title>

**What to build:** the end-to-end behaviour this ticket makes work, from the user's perspective, not a layer-by-layer implementation list.

**Blocked by:** the numbers/titles of the tickets that gate this one, or "None (can start immediately)".

**Status:** ready-for-agent

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</local-ticket-template>

<issue-template>

## Parent

A reference to the parent issue on the tracker (if the source was an existing issue, otherwise omit this section).

## What to build

The end-to-end behaviour this ticket makes work, from the user's perspective, not layer-by-layer implementation.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- A reference to each blocking ticket, or "None (can start immediately)".

</issue-template>

In either form, avoid specific file paths or code snippets: they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.
