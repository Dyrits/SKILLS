---
name: document
description: Write and maintain project documentation, and own where each shared project document lives and its format (requirements, specifications, backlog, working state, tasks, changelog, glossary, code conventions, architecture decision records). Use when documenting a system (README, API reference, runbook, onboarding guide), when writing down a settled term, convention, or decision, or when a workflow reads or updates project documents.
metadata:
  forks: "anthropics/knowledge-work-plugins/engineering/skills/documentation"
---

# Document

Shared project documents live under `documentation/`. This skill owns where each one lives and the shape it takes, so workflows name a document by its role and call this skill instead of restating its rules.

**Calls:** `write-for-agents`.

## Layout

| Role | Path | Holds | Format |
| --- | --- | --- | --- |
| Requirements | `documentation/requirements.md` | Global obligations | [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md) |
| Backlog | `documentation/backlog.md` | Local candidate backlog, or a pointer to the authoritative remote backlog | [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md) |
| Working state | `documentation/work-in-progress.md` | Active unfinished work and resumption state | [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md) |
| Changelog | `documentation/changelog.md` | Authorized agreements and verified deliveries | [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md) |
| Capability requirements | `documentation/capabilities/<capability>/requirements.md` | Optional additional capability obligations | [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md) |
| Specifications | `documentation/capabilities/<capability>/specifications.md` | Living agreed behavior, design, and acceptance | [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md) |
| Draft | `documentation/capabilities/<capability>/draft.md` | Unresolved proposals only | [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md) |
| Task | `documentation/capabilities/<capability>/tasks/NN-<slug>.md` | Local task body, or a pointer to its published remote task | [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md) |
| Glossary | `documentation/glossary.md` | Domain terms | [GLOSSARY-FORMAT.md](GLOSSARY-FORMAT.md) |
| Conventions | `documentation/conventions.md` | Project-agnostic code conventions no tool enforces | [CONVENTIONS-FORMAT.md](CONVENTIONS-FORMAT.md) |
| Decision record | `documentation/architecture-decision-record/NNNN-<slug>.md` | Hard-to-reverse decisions and their reasons | [ARCHITECTURE-DECISION-RECORD-FORMAT.md](ARCHITECTURE-DECISION-RECORD-FORMAT.md) |

A repository with several domain contexts lists them in `documentation/glossary-map.md`. Each context then keeps its own `documentation/` folder beside its code, holding its glossary and its decision records; the root folder keeps the map and the system-wide documents. When the topic's context is unclear, ask.

Read the format file before writing or checking a document, and create each document lazily: only when it carries useful information. A folder is created with its first document, never ahead of it. The project-document roles share the terms in PROJECT-DOCUMENTS.md (authorized, obligation, lazy, pointer); read it whenever a workflow reads or updates them.

Completion: every document written sits at its layout path and follows its format file.

## Other documents

For a README, runbook, API reference, or any other document:

1. Name the reader and the task the document supports; put what that task needs first.
2. Follow the repository's own writing rules and formats where they exist.
3. Check every claim against the current system before presenting it as current.
4. Link to the existing source instead of copying material that would drift.

For a document that instructs agents, call the Skill tool with "write-for-agents" as well.

## Pointer

When you create `documentation/`, or find the nearest `AGENTS.md` without this pointer, add it there once, checking for an existing one first:

> Project documents (requirements, specifications, working state, changelog, glossary, conventions, decision records) live under `documentation/`. Use the glossary's terms and respect the decision records. Call the Skill tool with "document" before creating, moving, or restructuring one.

When you create `documentation/` and the root `README.md` already has a section listing the project's documentation, add one line there linking to `documentation/`. Leave a `README.md` without such a section unchanged.
