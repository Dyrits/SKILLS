# Shared project documents

Every workflow that reads or writes the project-document roles in the layout follows this model. Callers use the terms below instead of restating these rules.

## Terms

- **Authorized**: the user approved the scope. A remote change (publication, update, priority change, or closure) also needs approval of its destination. Only the user authorizes: backlog entries, recommendations, tracker configuration, and passing builds are evidence, not approval.
- **Obligation**: a global or capability requirement, including infrastructure, legal, company, budget, service, and security constraints. An obligation binds the product and is imposed from outside the code (users, legal, operations, a client, a budget); a measurable one (a response-time budget, an uptime target) states its number, its reason, and the command that checks it. An obligation outranks a code convention: satisfy the obligation, and ask the user before relaxing either. Only the user relaxes an obligation. When one conflicts with scope or with the implementation, ask the user and continue independent work meanwhile. Within authorized scope, the implementation approach is free to change.
- **Lazy**: create a document when it carries useful information. A small batch can run on backlog, work-in-progress, and the changelog alone.
- **Pointer**: a link to the authoritative record, used in place of a copy.

## Sources of truth

Each role in the layout owns its content; every other mention of it is a pointer. Read global requirements first; capability requirements add obligations to them. Specifications live in the repository; remote discussions and records hold pointers or summaries.

## Capabilities

A **capability** is anything with lasting agreed behavior: a user-facing feature, an integration, an infrastructure area, or a concern such as performance or security. Its folder outlives the work that changes it.

- Name the folder with a kebab-case noun phrase built from glossary terms when a glossary exists (`order-checkout`, `invoice-export`), never after a ticket, date, technology, or version. In a multi-context repository, put the context name first only when two contexts would otherwise share a name.
- Keep the tree flat. A sub-area that needs its own specification becomes its own capability.
- File work under the capability it changes. A bugfix is a task there, and corrects `specifications.md` when the agreed behavior was wrong or incomplete. Work that changes no behavior usually needs no folder. An undecided effort lives in the folder of the capability it will become.
- Number tasks from `01`, with a kebab-case slug naming the outcome.
- Treat a name as fixed once anything references it. A rename is a consequential decision: move the folder, update every pointer, and record an Agreement in the changelog.

## Backlog authority

Read `.agents/issue-tracker.md` when present to find the configured tracker. With a local tracker, `documentation/backlog.md` holds candidate outcomes, priorities, dependencies, and deferrals. With a remote tracker, its backlog or board holds them, and `documentation/backlog.md` holds only its name and verified link.

Read the remote backlog when selecting or reprioritizing work. When it cannot be read, say so, ask for the records the decision needs, and continue authorized work whose agreement is recoverable locally.

## Working state and tasks

`documentation/work-in-progress.md` stays local with either tracker. It holds the selected scope, current agreements, running assignments, verification, acceptance, blockers, next actions, and pending publication, with pointers to remote records for their status. Prune an item once code, tests, or a durable record captures it; delivery history belongs in the changelog.

Tasks are optional for small batches. A task owns a coherent outcome, checkable acceptance criteria, and explicit blockers; a missing prerequisite is a blocker. Before publication a task is a local draft. After authorized publication the remote task is authoritative and the local file becomes a pointer with its title.

Local document upkeep within authorized scope is autonomous.

## Changelog

Keep one changelog and append to its history. Every record uses this heading and field order:

```markdown
## CHG-NNNN · YYYY-MM-DD · title

Type: Documentation
Event: Agreement
Scope: Sentence case display label

Summary: What changed or was authorized.
Reason: Why this agreement or delivery matters.
References: Links to the relevant authoritative records.
Validation: The authorization for an agreement, or completed checks and acceptance for a delivery.
Evidence: Durable evidence supporting the record.
```

`Type` is `Documentation`, `Code`, or `Configuration`. `Event` is `Agreement` or `Delivery`. Allocate the next free `CHG-NNNN`; when a merge brings in a record with the same number, renumber the record added later. `Scope` is a sentence case display label. Fields may continue onto following lines for lists or longer evidence.

- An **Agreement** records an authorized decision.
- A **Delivery** records that the agreed checks passed and any required human acceptance was given. While acceptance is pending, the work stays in working state.

Records come in two weights that share the heading, vocabulary, and identifier sequence, so a project moves between workflows without converting its history:

- **Full**: all five content fields. Use it in planned development (`specify`, `taskify`, `implement`) and whenever a team shares the record.
- **Light**: `Summary`, `References`, and `Validation`, adding `Reason` or `Evidence` when the references leave them unclear. Use it for just-in-time work by one person (`iterate`). Write a light Agreement only for a consequential decision (costly to reverse, or changing scope); an approved batch lives in working state until its Delivery.

Record meaningful decisions and deliveries. Executable evidence stays in tests and code, with pointers from the record.

## Review evidence

Review against the behavior authorized for the selected scope. Requirements, applicable specifications, architecture decision records, changelog agreements, and active working state establish that intent together; a batch authorized in working state is reviewable as it is. Identify the source of each obligation and compare it with the implementation and acceptance evidence. When records disagree on a consequential obligation, ask the user.
