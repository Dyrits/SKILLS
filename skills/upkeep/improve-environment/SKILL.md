---
name: improve-environment
description: "Hold a retrospective on a session's friction, then change the project's environment so the next run avoids it: checks, guardrails, navigation pointers, steering files, tool and information access. Use when the user asks what would have prevented a mistake, why a session was hard, or for an environment retrospective."
metadata:
  forks: "mattpocock/skills/skills/engineering/retro"
argument-hint: "Optional: the session to review, and the moment that went wrong"
---

The user has asked for a **retrospective** on the project's **environment**: everything around the code that shapes how an agent works in it. You trace each moment of **friction** in a session to the part of the environment that allowed it, and change that part, not the code, so the next run goes better.

## Steps

### 1. Trace the friction

Read the session the user names: a path, a session identifier, or a date in the local agent logs. Default to the current session. List every moment of friction:

- A long search for a file or fact.
- A mistake the agent made, and whether review caught it.
- A correction from the user, a retry, or a detour.
- An expensive or repeated tool call.
- Information the agent needed and could not reach.

Completion: each moment has a pointer into the session and a one-line account of what happened.

### 2. Read the environment

Read what the agent had to work with: the repository's and the user's global `AGENTS.md`, the project's conventions file, its own check commands (build-tool scripts such as `lint`, `check`, `typecheck`, `test`), its hooks path or pre-commit configuration, and its CI workflows.

Completion: you know which checks exist, which of them run automatically before a commit or in CI, and which exist but are unwired or broken.

### 3. Find candidates

Match each moment of friction to a category, and each candidate to the moment it would have prevented. Two candidates come from step 2 alone: a repository with no **guardrail**, and oversized steering files.

| Category | Look for | Candidate |
| --- | --- | --- |
| **Navigation** | A long search; a hidden dependency between files | A **navigation pointer** from a file the agent already reads |
| **Automated checks** | A mistake a tool could catch; a repository with no **guardrail** (no pre-commit hook and no CI job running its lint, typecheck, and test commands) | Wire the existing check first; otherwise a lint rule, type, test, hook, or CI job |
| **Coding standards** | A mistake review missed | Classify it: a **mechanical** violation (a banned API, an import shape, a file location) gets a deterministic check; only a **judgement call** becomes a conventions rule |
| **Steering files** | A large `AGENTS.md`, in the repository or global | Move each steering line out to a check or the conventions file, keeping pointers |
| **No-ops** | Steering lines that do not change the agent's behavior | Delete them |
| **Tool economy** | An expensive call for what it returned; a token-heavy CLI or MCP server | Streamline or replace the tool |
| **Information access** | Information the agent could not reach | Widen access: tee the dev server log to a file, give read-only access to a service |

A check that exists but sits unwired or broken is the finding; fix it rather than build a second one. Read the **Reference** below before placing a standard or a steering line.

Friction that a skill caused (a wrong trigger, an unclear step, a stale route) belongs to the skills repository: set it aside as a skill finding, listed for the user at the end.

Completion: every moment of friction from step 1 has a candidate, a skill finding, or a stated reason that the environment could not have prevented it.

### 4. Agree on the changes

Present the candidates in order of severity, weighing how much the mistake cost and how likely it is to recur, each with its moment in the session. Ask the user which to apply.

Completion: the user has accepted or declined every candidate.

### 5. Apply them

Apply each accepted candidate in its home:

- **A check or hook**: build it, run it against the current code to confirm it passes, and against the session's mistake when it can be reproduced to confirm it fails. When the repository has no hook mechanism at all, add one with the candidate: a versioned hooks directory that git's `core.hooksPath` points to.
- **A navigation pointer, a code convention, or a project convention**: file it following [LESSONS.md](LESSONS.md), which says where written lessons live.
- **A steering file edit or deletion**: follow [AGENT-INSTRUCTIONS.md](AGENT-INSTRUCTIONS.md).
- **A tool or access change**: make it when it sits in the repository; otherwise give the user the exact change to make.

When skill findings were set aside, list them for the user (the skill, the step, and what went wrong), so they can be reported to the skills repository.

Completion: every accepted candidate is applied and verified, or handed to the user with the exact change.

## Reference

### Implementation and review

Work passes through two stages. The implementing agent carries the most **context pressure**: it explores, writes code, and debugs failures. The reviewing agent receives a diff, so it has room to spare. Standards therefore belong to review: the review reads the conventions file, and the implementer is never asked to carry them.

### Homes

- `AGENTS.md` loads into every agent's context. Use them sparingly, mostly for navigation pointers to other files.
- The conventions file holds the code conventions a reviewer applies to any diff and no tool can enforce. Past roughly 1,000 lines, move detail into documents it points to.
- Documentation holds reference material reached through pointers. Look for an existing document before writing a new one.
- A skill suits reference whose description should trigger it, or a command the user runs.
