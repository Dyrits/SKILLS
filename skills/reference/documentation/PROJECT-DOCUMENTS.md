# Shared project documents

Use this model for future project work. Create documents lazily when they carry useful information; a small living-code batch can work entirely from backlog, work-in-progress, and the changelog. Read applicable requirements and existing specifications even when the batch creates neither a specification nor tasks.

Preserve historical `.refinement/`, local `backlog/`, and existing changelog records. Surface conflicting legacy inputs before treating a new document as authoritative; do not silently migrate, erase, or resolve competing obligations.

## Sources of truth

| Path | Owns |
| --- | --- |
| `CHANGELOG.md` | Authorized agreements and verified deliveries |
| `documentation/requirements.md` | Global constraints |
| `documentation/backlog.md` | Local candidate backlog, or a link to the authoritative remote backlog |
| `documentation/work-in-progress.md` | Active unfinished work and resumption state |
| `documentation/<feature>/requirements.md` | Optional additional feature constraints |
| `documentation/<feature>/specifications.md` | Living agreed behavior, design, and acceptance |
| `documentation/<feature>/draft.md` | Unresolved proposals only |
| `documentation/<feature>/tasks/<task>.md` | Local task body, or title and link to its authoritative published remote task |

Link to authoritative information rather than copying it. Specifications are always canonical in the repository. Remote discussions and records may link to or summarize them, not create a competing specification.

Read global requirements first. Feature requirements add constraints; they cannot silently override global requirements. Within approved scope, an agent may change the implementation approach, but cannot weaken requirements. Ask the user about consequential scope or obligation conflicts while continuing independent unblocked work.

## Backlog authority

Read `documentation/agents/issue-tracker.md` when present to determine the configured tracker and backlog location. Without a configured remote tracker, keep candidate outcomes, priorities, dependencies, and deferrals locally in `documentation/backlog.md`.

With a remote tracker, those records belong in its configured backlog or board. `documentation/backlog.md` is only a local entry point containing its name and verified link, not a copied queue, status table, or independently editable priority list. Preserve existing local history when changing authority; reconcile or migrate it only with authorization, not by silently replacing it with a link.

Read the remote source when selecting or reprioritizing work. If it cannot be read, state that limit and ask for the relevant records when the decision depends on them. Existing authorized work can continue when its agreement and constraints are recoverable locally. Do not claim that remote priorities or status were checked.

Local working state remains useful with either tracker. Keep current agreements, running assignments, verification, acceptance, blockers, and resumption pointers in `documentation/work-in-progress.md`, linking remote records rather than copying their authoritative status. Pending tracker publication can be recorded there as a scoped proposal or blocker; it is not a second project backlog. Remote additions, priority changes, updates, and closures require explicit publication authority.

## Working state and tasks

Backlog captures possible next work, not authorization to execute every item. Work-in-progress captures the selected active scope, unresolved blockers, next actions, and enough context to resume. Prune completed items once their evidence is captured in durable records, tests, or code; it is not a second delivery history.

Tasks are optional for small batches. When useful, each task owns a coherent outcome, checkable acceptance criteria, and explicit blockers. A missing prerequisite is a blocker, not an assumption.

Local document upkeep within authorized work is autonomous. Remote publication requires explicit approval of the destination and scope, including remote updates and closures. Before publication, a task is a local draft. After approved publication, the remote task is authoritative and the local draft becomes a pointer containing its title and link. Keep specifications canonical in the repository through that transition.

## Changelog semantics

Preserve and reconcile an existing root changelog rather than replacing its history. New semantic records use this exact heading shape:

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

`Type` is exactly `Documentation`, `Code`, or `Configuration`. `Event` is exactly `Agreement` or `Delivery`. Allocate `CHG-NNNN` identifiers without colliding with existing records. Use a sentence case human display label for `Scope`, not a mandatory path slug. The five content fields are required; they may continue onto following lines for lists or longer evidence. `Task` and `Revision` are optional additional fields.

An **Agreement** records an authorized decision, not an unresolved proposal or an agent's unapproved recommendation. A **Delivery** records satisfaction of the agreed checks and any necessary human acceptance. Distinguish measured results from pending checks and acceptance; do not declare delivery while required acceptance is pending. Preserve executable evidence in tests and code, and link it from records where useful.

Record meaningful decisions and deliveries, not mechanical edits or session transcripts.

## Review evidence

Review against the intended behavior authorized for the selected scope. Requirements, applicable specifications, authorized changelog agreements, and active working state can establish that intent together. A working-state-only batch does not need a new specification to be reviewable. Identify the source of each obligation and compare it with the implementation and acceptance evidence. If the records disagree on a consequential obligation, ask the user rather than choosing whichever makes the implementation pass.
