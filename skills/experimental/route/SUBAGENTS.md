# Subagents per harness

Reached from step 3 of [`SKILL.md`](SKILL.md): what each harness calls its delegation tool, where its agent definitions live, and which agents to add when a role has no home. Verify against the tool's own parameter list before dispatching, since a project can rename or replace any of these.

## Known bindings

| Role | Claude Code | OpenCode | Codex CLI |
| --- | --- | --- | --- |
| planner | `Plan` | `plan` | inline |
| explorer | `Explore` | `explore` | inline |
| reviewer | `general-purpose`, briefed to review only | `general`, briefed to review only | inline |
| implementer-fast | add one | add one | inline |
| implementer | `general-purpose` | `build` | inline |
| implementer-heavy | add one | add one | inline |

**Claude Code** delegates through the `Agent` tool, whose `subagent_type` enumerates the built-ins plus every agent defined in `.claude/agents/*.md` (project) or `~/.claude/agents/*.md` (user).

**OpenCode** delegates through the `task` tool, whose `subagent_type` covers the built-ins plus `.opencode/agent/*.md` (project) and `~/.config/opencode/agent/*.md` (user).

**Codex CLI** has no delegation tool, so every role runs inline.

## Adding the implementer tiers

Only the middle implementer ships with either harness. Tiering is the point of routing a `code change`, so a harness missing the outer two is worth a one-time fix: write the two definitions below into the project's agent directory, pinning the models the project actually pays for.

`.claude/agents/build-fast.md`, where `model` takes `haiku`, `sonnet`, `opus`, or a full model id:

```markdown
---
name: build-fast
description: Fast, cheap implementer for small, well-scoped changes.
model: haiku
---

You are a fast implementer. You handle small, well-scoped changes: renames, small
functions, tweaks, formatting, small bug fixes, test additions. Do exactly what is
asked, no refactoring beyond the request, no commentary beyond the result.
```

`.claude/agents/build-heavy.md`, the same shape with `model: opus` and this body:

```markdown
You are a heavyweight implementer for drastic changes: cross-cutting refactors,
architecture changes, large feature work, migrations, security-sensitive edits.
Read the surrounding code before changing it, keep changes coherent across files,
and verify with the project's lint, typecheck and test commands when present.
```

OpenCode takes the same two bodies under `.opencode/agent/`, with `mode: subagent` and a provider-qualified `model` (`opencode/glm-5.3-flash`, `opencode/gpt-5.1-codex-max`) in place of the `name` and bare `model` fields.
