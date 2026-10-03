---
name: taskify
description: Decompose approved work into coherent, verifiable tasks with explicit blocking dependencies, locally or on an approved tracker.
disable-model-invocation: true
---

# Taskify

Create tracker-neutral tasks that deliver coherent outcomes. A small batch may need no tasks: recommend direct implementation or iterate when decomposition adds no value.

## Establish the source

Call the Skill tool with "documentation" and apply its shared project document model. Read the selected scope, applicable requirements and specifications, active working state, relevant code, domain vocabulary, and architectural decisions. Fetch the full body and comments of any referenced remote task.

Read configured tracker and task-writing conventions when available. Local drafting does not require tracker setup. Ask about material missing scope or conflicting obligations rather than silently choosing. Link canonical repository specifications instead of producing another copy.

## Decompose into outcomes

Prefer **tracer bullets**: narrow end-to-end slices that are independently demoable or verifiable, sized for a fresh implementation context. Group related work into a meaningful outcome rather than one task per layer or edit. Identify useful prefactoring before dependent feature slices.

For a wide mechanical refactor that cannot land in independent vertical slices, use **expand-contract**: introduce the new form compatibly, migrate bounded batches, then remove the old form after all migrations. If intermediate batches cannot stay green independently, state the integration branch and final integrate-and-verify dependency explicitly.

Every task must state:

- Its title and the outcome it delivers.
- The approved scope or canonical source it serves.
- Checkable acceptance criteria owned by this task, including how completion is demonstrated.
- Explicit blockers: task references, external prerequisites, unresolved decisions, or "None".

Check that acceptance distinguishes the intended change from the starting state and does not claim another task's result. Use native tracker dependencies where supported, body links as the fallback. Avoid incidental implementation paths or snippets; retain decision-rich prototype shapes when they express an agreed decision precisely.

## Approve and save

Present the proposed outcome breakdown, acceptance, and blocking edges. Ask the user to approve granularity and dependencies; merge or split where useful. Keep unresolved blockers visible.

Save approved local bodies or drafts at the shared model's task paths, in dependency order. Local upkeep is autonomous within authorized scope. Publish remotely only after explicit approval of the destination and publication scope, following configured conventions. Publish blockers first so later dependencies can reference real identifiers. Verify native dependency and parent links where applicable.

After approved remote publication, replace the local draft with its title and authoritative remote link. Leave specifications canonical in the repository. Do not update or close a remote parent outside publication approval.

Report saved paths or published links, remaining blockers, and the **frontier** of tasks whose prerequisites are complete. Taskify stops at decomposition and approved publication, not execution.
