Source: Anthropic's `documentation` skill in `knowledge-work-plugins`, now `document` in this fork, adapted in commit `6585eba` from upstream revision `1bd42820da111e5f0206e570bf5228a1c35839c7` and extended here with the shared project document model. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the pinned original and adoption evidence.

## What it does

`document` owns the shared model for project requirements, specifications, backlog, working state, tasks, and semantic changelog records. Workflows call it instead of restating those rules. For any other document (a README, runbook, or API reference) it keeps four habits: write for a named reader and task, follow the repository's formats, check claims against the current system, and link instead of copying.

Project records have distinct jobs and are created only when useful. A small batch can work from backlog, work-in-progress, and the changelog without creating specifications or tasks.

## When to reach for it

Type `/document`, or the agent reaches for it automatically when a task fits. Use it for a README, API reference, runbook, architecture document, onboarding guide, or project-state upkeep. Use [write-for-agents](write-for-agents.md) alongside it for documents that instruct an agent.

## One source for each obligation

Global requirements constrain all work. Feature requirements add constraints; they cannot silently override global ones. Specifications record agreed behavior in the repository. Drafts contain unresolved proposals. A local backlog captures candidates; a remote backlog is authoritative when configured and the local file links to it. Work-in-progress remains local for unfinished execution and recovery, not copied tracker status.

Local upkeep is autonomous within approved work. Remote publication and updates require explicit approval. Once a task is published remotely, its local draft becomes a pointer rather than a competing body.

The changelog records authorized Agreement events and verified Delivery events, never a transcript or every mechanical edit. Records come in two weights with the same heading and vocabulary: full records for the planned workflow and team use, light records (summary, references, validation) for just-in-time work by one person, where an Agreement is written only for a consequential decision.

## Common questions

**Must every batch create all these files?**
No. Create a file when it holds useful information. Existing applicable requirements and specifications still constrain batches that create no new specification.

**Why does it no longer list README or runbook sections?**
The model already knows what those documents contain, so the lists changed nothing. What it adds is the reader-first habit and the check against the current system.

**Can a completed item stay in work-in-progress for history?**
Capture durable evidence first, then prune it from unfinished state. Delivery history belongs in the changelog and linked evidence.

## It's working if

- You can find the authoritative requirement, agreement, or task without choosing between competing copies.
- Active working state tells you what remains and how to resume.
- Changelog deliveries link checks and evidence, with necessary human acceptance complete.
- The document answers its reader's task instead of dumping the session history.

## Where it fits

Document is a model-invoked reference used by [specify](../workflow/specify.md), [taskify](../workflow/taskify.md), and delivery workflows. [Model-domain](model-domain.md) owns active terminology and qualifying architectural decisions. [Guide](../getting-started/guide.md) maps the surrounding flows.
