---
name: documentation
description: Write and maintain technical documentation and shared project documents. Use when the user asks to document a system, create a README, API reference, runbook, architecture document, or onboarding guide, or when a workflow needs requirements, specifications, backlog, working state, tasks, or semantic changelog records.
---

# Technical documentation

Write technical documentation for its intended readers and their tasks. Follow repository-specific writing rules and document formats where they exist. Use the document-type lists below as prompts, not required sections.

For a document that instructs agents, call the Skill tool with "writing-for-agents" and apply its guidance alongside this skill.

For project requirements, specifications, drafts, backlog, work-in-progress, tasks, or changelog records, read [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md) and apply its shared source-of-truth and authorization rules. Calling workflows consume this model through the Skill tool with "documentation".

## Document types

### README

- What this is and why it exists
- Quick start that reaches a first success in under five minutes
- Configuration and usage
- Contributing guidance

### API reference

- Endpoints with request and response examples
- Authentication and error codes
- Rate limits and pagination
- Client library examples

### Runbook

- When to use the runbook
- Prerequisites and required access
- Procedure with commands and expected results
- Recovery steps when an action fails
- Escalation path

### Architecture document

- Context and goals
- Design and relevant diagrams
- Decisions and trade-offs
- Data flow and integration points

### Onboarding guide

- Environment setup
- Key systems and their connections
- Common tasks with walkthroughs
- Who to ask for what

## Principles

1. Identify the reader and the task the document must support.
2. Put the information needed for that task first.
3. Show concrete examples, commands, or screenshots where they clarify a step.
4. Check the document against the current system before presenting it as current.
5. Link to an existing source instead of copying material that would drift.
