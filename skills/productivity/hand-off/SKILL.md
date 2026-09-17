---
name: hand-off
description: Compact the current conversation into a versioned handoff document in .agents/handoffs/ for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work.

## Where to save

Save to `.agents/handoffs/` in the current workspace, versioned so history accumulates:

- Filename: `YYYY-MM-DD-HHMM-<short-slug>.md` (timestamp = when written, slug = dash-case topic)
- Never overwrite an existing handoff; always write a new file
- Add `.agents/handoffs/` to `.gitignore` if the user wants local-only history, or commit them if the team wants shared history. Ask once; remember via the repository's config or AGENTS.md note
- Print the full path when done, and tell the user to paste it into the next session's first message

## Document contents

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Also include, near the top: a "supersedes" line pointing at any earlier handoff in `.agents/handoffs/` this one replaces, so the chain is traceable.

Do not duplicate content already captured in other artifacts (specifications, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
