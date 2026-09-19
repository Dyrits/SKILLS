---
name: dispatch
description: Bind a route recommendation to the subagent that fits it, brief it, and dispatch. Use when a fresh unit of engineering work arrives (a change, a plan, an exploration, a review) before starting any of it, when a `route:` recommendation from the auto-route hook appears in context, or when the user types `/dispatch`.
---

# Dispatch

The `setup-auto-route` hook classifies every prompt with classifier.dev before you start reasoning about it, and writes its verdict into context as a `Route:` line, but only when the verdict *changes* from the previous prompt in the session. Reading that line **before** reasoning about how to do the work is the point: reason first and the verdict bends toward whatever you already started planning, which is exactly what a hook running ahead of you is meant to prevent.

## Route at the top only

| Situation | What happens |
| --- | --- |
| A fresh unit of engineering work arrives | Route it |
| You are already running inside a subagent | Do the work you were handed |
| The turn builds on work already in this window | Continue here: a subagent starts without that context |
| The user named an agent or a skill | Use the one they named |
| The turn is a question, a chat, or a one-liner | Answer it |

The hook announces change only: a same-window follow-up whose verdict holds gets no line, and neither does a transition to `Undefined`. Silence therefore covers both continuation and the hook failing open (classifier timeout, error, or `429`). This table is what sorts the rest: only you, in-window, can tell a fresh unit of work from a continuation, a subagent, or a named target. The hook has none of that judgement, which is why it stops at a recommendation rather than dispatching itself.

## Step 1: Read the recommendation

The hook's `systemMessage` sits in context, attached to this same prompt, shaped like:

```
Route: Implementation or refactoring (0.99) | Large or risky change (1.00) (Previous route: Debugging or diagnosis | Fast and simple). Use the relevant skill. Consider /dispatch as a priority.
```

The first line of a session drops the `(Previous route: ...)` clause. Take the route from it directly. Do not reclassify: the hook already made one call to classifier.dev for this prompt, and a second verdict on the same text is a second answer to a settled question.

Derive the role from the labels:

| Verdict | Role |
| --- | --- |
| Implementation or refactoring · Fast and simple | implementer-fast |
| Implementation or refactoring · Moderate | implementer |
| Implementation or refactoring · Large or risky change | implementer-heavy |
| Debugging or diagnosis | explorer |
| Planning or design | planner |
| Specification refinement | planner, or a specification skill inline when one fits better |
| Codebase exploration | explorer |
| Code review | reviewer |

No line in context? The hook is either not installed (tell the user to run `setup-auto-route`) or it stayed silent: the verdict held, or it failed open. Either way, bind to **implementer** (the safe middle) or the matching read-only role by your own judgement, and say so in the report line.

## Step 2: Bind the role to an agent

Discover what this harness offers rather than assuming names:

1. **The delegation tool.** A tool that starts a subagent on a prompt and returns its report, taking an agent name as a parameter. Claude Code exposes `Agent` (`subagent_type`). No such tool in this harness means no binding exists: go to the inline fallback.
2. **The agent names it advertises.** The tool's own parameter lists the built-ins; project and user agent definitions add more. Read each name with its one-line description.
3. **The match.** Bind on what an agent is described as doing, not on its name resembling the role. Read [SUBAGENTS.md](SUBAGENTS.md) for the known bindings, where definitions live, and the agents to add when a role has no home.

Where an implementer tier has no agent, the machine has not been set up: run `scripts/setup-agents.sh` from this skill's directory once, which writes the missing tiers with a model pinned to each and is idempotent when they already exist. New definitions are picked up without a restart, though not instantly, so bind this turn by walking down and let the next turn get the tier.

Where a role still has no agent, walk down: **implementer-fast** and **implementer-heavy** fall back to **implementer**, **implementer** and the read-only roles fall back to the harness's general agent, and a harness with no general agent falls back to inline.

**Inline fallback.** Adopt the role yourself in this session, holding its constraint: a planner, an explorer or a reviewer reports and leaves the files alone.

## Step 3: Write the briefing

No subagent inherits or forks this conversation: it starts on a prompt and the project's own instruction files, and nothing else. Verbatim text alone loses whatever this window already knows, so compose a compact briefing instead of handing over the bare request:

- The user's request, verbatim.
- The working directory.
- Anything the request leans on without stating it: a path, a target file, a convention agreed earlier in this conversation.
- Other artifacts already produced this session (a plan, a design doc, a prior finding), referenced by path rather than duplicated in full.

This is the same compaction discipline `hand-off` applies at a session boundary, done here in miniature for one subagent dispatch, not a call to that skill.

## Step 4: Dispatch and report

Hand the bound agent the briefing from step 3. Report one line before the work starts, then the agent's result:

```
route: Implementation or refactoring (0.99) | Large or risky change (1.00) → Heavy
```

Name the fallback in that line whenever one fired (`→ inline (no delegation tool)`, `→ General (no recommendation in context, routed by judgement)`), so the route is always visible as either the hook's or yours.
