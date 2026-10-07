# Architecture format

The architecture document, `documentation/architecture.md`, describes the system's technical shape as it stands, or as agreed when nothing is built yet: the parts it runs as, what each owns, how they talk, where they run, and how each system-wide requirement is met. Reasons for hard-to-reverse choices live in decision records; this document links them instead of repeating them.

## Structure

```md
# Architecture

{One paragraph: the system's shape in plain words, for example "a single web application with a background worker, backed by one Postgres database".}

## Stack

- **{Concern: language, framework, storage, messaging, hosting...}**: {choice}. {One line on why, or a link to its decision record.}

## Parts

- **{Part}**: {what it is (an application, a worker, a database, a library), the context or capabilities it serves, and the data it owns}

## Flows

- **{Flow name, in domain terms}**: {which parts take part, in order, and what passes between them, synchronously or not}

## Integrations

- **{External system}**: {what is exchanged, in which direction, over what, and what happens when it is unavailable}

## Deployment

{Where each part runs, how it is released, and the environments that exist.}

## Requirements

| Requirement | How the architecture meets it |
| --- | --- |
| {Short name from the requirements} | {the part, flow, or choice that satisfies it, or "Not met: ..." with the gap} |

## Decisions

- [{NNNN: title}](architecture-decision-record/NNNN-slug.md)
```

## Rules

- **Describe what is, not what was.** Update the document when the shape changes; history lives in the decision records.
- **Parts follow the domain.** Each part serves named contexts or capabilities, in glossary terms. A part that serves no context is infrastructure; say what it supports.
- **Every piece of data has one owning part.** Others reach it through that part, or hold a copy whose source and refresh are stated.
- **Every system-wide requirement has a row.** An unmet requirement stays visible with its gap until the user relaxes it or the architecture changes.
- **Leave out module-level design** (classes, interfaces inside a part, a capability's data model); it belongs to each capability's design.
- **Omit empty sections.** A small system may need only the opening paragraph, the stack, and the requirements table.
