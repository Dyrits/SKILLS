---
name: taskify
description: "Decompose approved work into verifiable tasks with explicit blocking dependencies, locally or on an approved tracker. Use when the user asks to break agreed work into tasks, or when specifications need splitting into delivery work."
metadata:
  forks: "mattpocock/skills/skills/engineering/to-tickets"
---

# Taskify

Create tracker-neutral tasks that deliver coherent outcomes. A small batch may need no tasks: say so when decomposition adds no value, and leave the batch for direct implementation.

## Establish the source

The project documents and their rules are in [PROJECT-DOCUMENTS.md](references/PROJECT-DOCUMENTS.md); its terms (authorized, obligation, lazy, pointer) apply throughout. Read the selected scope, applicable requirements and specifications, active working state, relevant code, domain vocabulary, and architectural decisions. Fetch the full body and comments of any referenced remote task.

Read configured tracker and task-writing conventions when present; local drafting works without tracker setup. Ask the user about material missing scope.

## Decompose into outcomes

Prefer **tracer bullets**: narrow end-to-end slices that are independently demoable or verifiable, sized for a fresh implementation context. Group related work into a meaningful outcome rather than one task per layer or edit. Identify useful prefactoring before dependent feature slices.

For a wide mechanical refactor that cannot land in independent vertical slices, use **expand-contract**: introduce the new form compatibly, migrate bounded batches, then remove the old form after all migrations. If intermediate batches cannot stay green independently, state the integration branch and final integrate-and-verify dependency explicitly.

Every task must state:

- Its title and the outcome it delivers.
- The approved scope or canonical source it serves.
- Checkable acceptance criteria owned by this task, including how completion is demonstrated.
- Explicit blockers: task references, external prerequisites, unresolved decisions, or "None".

Check that acceptance distinguishes the intended change from the starting state, and that each criterion can be verified with only this task's work and its blockers' results. A criterion that needs the result of any other task moves to that task, or that task becomes a blocker. Use native tracker dependencies where supported, body links as the fallback. Keep task bodies at the level of outcomes; include a decision-rich prototype shape when it expresses an agreed decision precisely.

## Approve and save

Present the proposed outcome breakdown, acceptance, and blocking edges. Ask the user to approve granularity and dependencies; merge or split where useful. Keep unresolved blockers visible.

Save approved drafts at the shared task paths, in dependency order. Once publication is authorized, publish following configured conventions: blockers first so later tasks can reference real identifiers, then verify native dependency and parent links. Each published local draft becomes a pointer. Change a remote parent only when the authorization covers it.

Report saved paths or published links, remaining blockers, and the **frontier** of tasks whose prerequisites are complete. Taskify stops at decomposition and approved publication, not execution. The frontier says which tasks can start now, one at a time or in parallel.
