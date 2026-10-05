---
name: hand-off
description: Compact the current conversation into a versioned handoff document in .agents/handoffs/ for another agent to pick up. Use when the user asks for a handoff, at a phase boundary they name, or when a compaction gate blocks until a fresh handoff exists.
argument-hint: "What will the next session be used for?"
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work.

## Where to save

Save to `.agents/handoffs/` in the current workspace, versioned so history accumulates:

- Filename: `YYYY-MM-DD-HHMM-<short-slug>.md` (timestamp = when written, slug = dash-case topic)
- Never overwrite an existing handoff; always write a new file
- Settle whether handoffs stay local or are shared. The repository already answers it when `.agents/handoffs/` is listed in `.gitignore` (local-only), earlier handoffs are tracked (shared), or an AGENTS.md note says so; follow that without asking. Otherwise ask once: add `.agents/handoffs/` to `.gitignore` for local-only history, or commit them for shared history. Record the answer in an AGENTS.md note
- Print the full path when done, and tell the user to paste it into the next session's first message

## Document contents

Include a "suggested skills" section naming useful skills and their invocation modes. Check each name against the skills installed in this session, and drop or replace any that are missing. The next agent calls them through the Skill tool.

Also include, near the top: a "supersedes" line pointing at any earlier handoff in `.agents/handoffs/` this one replaces, so the chain is traceable.

Do not duplicate content already captured in other artifacts (specifications, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the document accordingly.
