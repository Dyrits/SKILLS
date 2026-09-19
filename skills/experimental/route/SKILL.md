---
name: route
description: Route a request to the subagent that fits it by classifying the task type and its complexity first, so a classifier picks the agent rather than your judgement. Use when a fresh unit of engineering work arrives (a change, a plan, an exploration, a review) before starting any of it, or when the user types `/route`.
---

# Route

A classifier picks the route. Classify **before** reasoning about how to do the work: reason first and the verdict bends toward whatever you already started planning.

## Route at the top only

| Situation | What happens |
| --- | --- |
| A fresh unit of engineering work arrives | Route it |
| You are already running inside a subagent | Do the work you were handed |
| The turn builds on work already in this window | Continue here: a subagent starts without that context |
| The user named an agent or a skill | Use the one they named |
| The turn is a question, a chat, or a one-liner | Answer it |

## Step 1: Classify

Call the Skill tool with "classify", passing the user's request verbatim as the text and these two dimensions in one call:

- `task`: `code change`, `planning or design`, `codebase exploration`, `code review`, `none of these`
- `complexity`: `simple small change`, `moderate change`, `large or drastic change`

with these `instructions`:

> Judge the scope and risk of the work described, not how it is worded. A rename, a small function, a config tweak, a small fix is simple. Multi-file refactors, architecture changes, migrations, anything security-sensitive are large.

Take both labels and both confidences from the verdict.

## Step 2: Read the verdict as a role

A **role** is what the work needs done, named without reference to any harness.

| `task` | Role |
| --- | --- |
| `planning or design` | **planner**: design an approach and report it, changing no files |
| `codebase exploration` | **explorer**: search and read, report findings, change no files |
| `code review` | **reviewer**: review the code and report findings, change no files |
| `none of these`, or `task` confidence below `0.7` | **none**: answer it yourself |
| `code change` | an implementer, tiered by `complexity` below |

| `complexity` | Role |
| --- | --- |
| `simple small change` | **implementer-fast**: pinned to a fast, cheap model |
| `moderate change` | **implementer**: pinned to the default model |
| `large or drastic change` | **implementer-heavy**: pinned to the strongest model |
| Confidence below `0.6` | **implementer**, the safe middle |

The role carries the model with it. Reach for the agent the role binds to and let its pinned model stand.

## Step 3: Bind the role to an agent

Discover what this harness offers rather than assuming names:

1. **The delegation tool.** A tool that starts a subagent on a prompt and returns its report, taking an agent name as a parameter. Claude Code exposes `Agent` (`subagent_type`); OpenCode exposes `task` (`subagent_type`). No such tool in this harness means no binding exists: go to the inline fallback.
2. **The agent names it advertises.** The tool's own parameter lists the built-ins; project and user agent definitions add more. Read each name with its one-line description.
3. **The match.** Bind on what an agent is described as doing, not on its name resembling the role. Read [SUBAGENTS.md](SUBAGENTS.md) for the known bindings per harness, where definitions live, and the agents to add when a role has no home.

Where a role has no agent, walk down: **implementer-fast** and **implementer-heavy** fall back to **implementer**, **implementer** and the read-only roles fall back to the harness's general agent, and a harness with no general agent falls back to inline.

**Inline fallback.** Adopt the role yourself in this session, holding its constraint: a planner, an explorer or a reviewer reports and leaves the files alone.

## Step 4: Dispatch and report

Hand the user's request **verbatim** to the bound agent, prefixed with the role's one-line brief from step 2. Paraphrasing is where the request loses the detail the agent needs.

Report one line before the work starts, then the agent's result:

```
route: code change 0.99 · large or drastic change 1.00 → build-heavy
```

Name the fallback in that line whenever one fired (`→ inline (no delegation tool)`, `→ build (classifier unavailable, routed by judgement)`), so the route is always visible as either the classifier's or yours.
