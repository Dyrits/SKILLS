Source: Anthropic's `documentation` skill in `knowledge-work-plugins`, adapted in commit `6585eba` from upstream revision `1bd42820da111e5f0206e570bf5228a1c35839c7` and extended here with the shared project document model. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the pinned original and adoption evidence.

## What it does

`documentation` writes and maintains technical documents for their intended readers. It also owns the shared model for project requirements, specifications, backlog, working state, tasks, and semantic changelog records.

Project records have distinct jobs and are created only when useful. A small batch can work from backlog, work-in-progress, and the changelog without creating specifications or tasks.

## When to reach for it

Type `/documentation`, or the agent reaches for it automatically when a task fits. Use it for a README, API reference, runbook, architecture document, onboarding guide, or project-state upkeep. Use [writing-for-agents](writing-for-agents.md) alongside it for documents that instruct an agent.

## One source for each obligation

Global requirements constrain all work. Feature requirements add constraints; they cannot silently override global ones. Specifications record agreed behavior in the repository. Drafts contain unresolved proposals. A local backlog captures candidates; a remote backlog is authoritative when configured and the local file links to it. Work-in-progress remains local for unfinished execution and recovery, not copied tracker status.

Local upkeep is autonomous within approved work. Remote publication and updates require explicit approval. Once a task is published remotely, its local draft becomes a pointer rather than a competing body.

The changelog records authorized Agreement events and verified Delivery events. It is not a transcript or a record of every mechanical edit.

## Common questions

**Must every batch create all these files?**
No. Create a file when it holds useful information. Existing applicable requirements and specifications still constrain batches that create no new specification.

**What happens to old refinement and backlog histories?**
Preserve them. The new layout governs future work; conflicting legacy inputs must be surfaced rather than silently erased or treated as settled.

**Can a completed item stay in work-in-progress for history?**
Capture durable evidence first, then prune it from unfinished state. Delivery history belongs in the changelog and linked evidence.

## It's working if

- You can find the authoritative requirement, agreement, or task without choosing between competing copies.
- Active working state tells you what remains and how to resume.
- Changelog deliveries link checks and evidence, with necessary human acceptance complete.
- The document answers its reader's task instead of dumping the session history.

## Where it fits

Documentation is a model-invoked reference used by [specify](../workflow/specify.md), [taskify](../workflow/taskify.md), and delivery workflows. [Domain-modeling](domain-modeling.md) owns active terminology and qualifying architectural decisions. [What-is-next](../getting-started/what-is-next.md) maps the surrounding flows.
