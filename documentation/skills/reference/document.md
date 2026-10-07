Source: Anthropic's `documentation` skill in `knowledge-work-plugins`, now `document` in this fork, adapted in commit `6585eba` from upstream revision `1bd42820da111e5f0206e570bf5228a1c35839c7` and extended here with the shared project document model. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the pinned original and adoption evidence.

## What it does

`document` owns every shared project document: where it lives under `documentation/` and the shape it takes. That covers requirements, specifications, backlog, working state, tasks, the changelog, the glossary, code conventions, and architecture decision records. Other skills name a document by its role ("the changelog", "the glossary") and call `document` instead of restating its rules, so the layout can change in one place ([architecture decision record 0004](../../architecture-decision-record/0004-skills-know-each-other-only-by-contract.md)). For any other document (a README, runbook, or API reference) it keeps four habits: write for a named reader and task, follow the repository's formats, check claims against the current system, and link instead of copying.

Project records have distinct jobs and are created only when useful. A small batch can work from backlog, work-in-progress, and the changelog without creating specifications or tasks.

## When to reach for it

Type `/document`, or an agent can reach for it when a task fits. Use it for a README, API reference, runbook, architecture document, onboarding guide, project-state upkeep, or to write down a settled term, convention, or decision. [delineate](../workflow/delineate.md) and [codify](../setup/codify.md) call it after settling terms and conventions with you. Use [write-for-agents](../productivity/write-for-agents.md) alongside it for documents that instruct an agent.

## One source for each obligation

Global requirements constrain all work. Capability requirements add constraints; they cannot silently override global ones. Specifications record agreed behavior in the repository. Drafts contain unresolved proposals. A local backlog captures candidates; a remote backlog is authoritative when configured and the local file links to it. Work-in-progress remains local for unfinished execution and recovery, not copied tracker status.

An obligation binds the product and is imposed from outside the code: users, legal, operations, a client, a budget. A measurable one, such as a response-time budget, states its number, its reason, and the command that checks it.

The first time it creates `documentation/`, it adds a one-line pointer to `AGENTS.md` so agents look there, and a link in the root `README.md` when that file already lists the project's documentation.

Local upkeep is autonomous within approved work. Remote publication and updates require explicit approval. Once a task is published remotely, its local draft becomes a pointer rather than a competing body.

The changelog records authorized Agreement events and verified Delivery events, never a transcript or every mechanical edit. Records come in two weights with the same heading and vocabulary: full records for planned development (specify, taskify, implement) and team use, light records (summary, references, validation) for just-in-time work by one person (iterate), where an Agreement is written only for a consequential decision.

## Glossary, decision records, and conventions

Three documents hold the project's language and judgment, each to its own bar:

| | Glossary | Decision record | Conventions |
| --- | --- | --- | --- |
| Holds | What a domain term **is**, in one or two sentences, with rejected synonyms under `_Avoid_` | One hard-to-reverse decision: context, choice, reason | How code is written here, as rules a reviewer applies to any diff |
| Bar to write | A vague term became canonical | **All three**: hard to reverse, surprising without context, the result of a real trade-off | Project-agnostic: it would still hold if the product changed entirely |
| Never holds | Implementation details, specifications, general programming concepts | A diary of every choice made in a session | Product behavior, domain terms, anything a tool can check |

A requirement and a convention answer different questions. A requirement says what the product must do and comes from outside the code; a convention says how code is written and is the team's own choice. When they seem to clash, the requirement wins and the convention shapes how it is met.

## Capabilities, not features or tickets

Specifications and tasks live under `documentation/capabilities/<capability>/`. A capability is anything with lasting agreed behavior, so the folder suits an infrastructure area or a security concern as well as a user-facing feature, and it outlives the work that changes it. A bugfix is a task under the capability it repairs, not a folder of its own. The [naming rules](../../../skills/reference/document/PROJECT-DOCUMENTS.md#capabilities) cover kebab-case glossary names, flat folders, numbered tasks, and why a name stays fixed once referenced. The [architecture decision record](../../architecture-decision-record/0003-group-specifications-by-capability.md) explains the choice.

## Common questions

**Must every batch create all these files?**
No. Create a file when it holds useful information. Existing applicable requirements and specifications still constrain batches that create no new specification.

**Why does it no longer list README or runbook sections?**
The model already knows what those documents contain, so the lists changed nothing. What it adds is the reader-first habit and the check against the current system.

**Why `capabilities/` and not `features/`?**
Not all work is a feature. A folder named after features invites a separate folder for each bugfix or chore, which spreads one area's behavior across folders that go stale once the work ships. Naming the folder after what persists keeps one specification per area.

**Why is the changelog under `documentation/` and not at the root?**
It is a log of agreements and deliveries, not release notes. Release tools such as changesets or release-please generate a root `CHANGELOG.md`, and the two would collide.

**Can a project keep its glossary or conventions at the root?**
The skill describes one layout and does not migrate. A project that keeps root files keeps them until someone moves them; new documents go under `documentation/`.

**Two branches took the same changelog number. Which one wins?**
Both records stay. When the merge brings in a record with the same `CHG-NNNN`, the record added later is renumbered.

**Can a completed item stay in work-in-progress for history?**
Capture durable evidence first, then prune it from unfinished state. Delivery history belongs in the changelog and linked evidence.

## It's working if

- You can find the authoritative requirement, agreement, or task without choosing between competing copies.
- Active working state tells you what remains and how to resume.
- Changelog deliveries link checks and evidence, with necessary human acceptance complete.
- The document answers its reader's task instead of dumping the session history.
- Every shared document sits under `documentation/`, and no other skill's instructions name its path.

## Where it fits

Document is a reference used by [specify](../workflow/specify.md), [taskify](../workflow/taskify.md), and delivery workflows. [Delineate](../workflow/delineate.md) and [codify](../setup/codify.md) settle terms and code conventions with you, then call `document` to write them down; [interview](../shaping/interview.md) settles decisions that `document` records. [Guide](../productivity/guide.md) maps the surrounding flows.
