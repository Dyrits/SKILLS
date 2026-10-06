---
name: document
description: Write and maintain project documentation, including the shared project documents workflows rely on (requirements, specifications, backlog, work-in-progress, tasks, changelog records). Use when documenting a system (README, API reference, runbook, architecture or onboarding document) or when a workflow reads or updates project documents.
metadata:
  forks: "anthropics/knowledge-work-plugins/engineering/skills/documentation"
---

# Document

For requirements, specifications, drafts, backlog, work-in-progress, tasks, or changelog records, read [PROJECT-DOCUMENTS.md](PROJECT-DOCUMENTS.md). Workflows call this skill instead of restating its rules.

**Calls:** `write-for-agents`. If a called skill is not installed, tell the user its name and install command, `npx skills@latest add Dyrits/SKILLS --skill=<name>`, then carry out that step from its stated intent and report the step as done without the skill.

For any other document:

1. Name the reader and the task the document supports; put what that task needs first.
2. Follow the repository's own writing rules and formats where they exist.
3. Check every claim against the current system before presenting it as current.
4. Link to the existing source instead of copying material that would drift.

For a document that instructs agents, call the Skill tool with "write-for-agents" as well.
