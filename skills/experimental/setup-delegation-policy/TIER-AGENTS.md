# Tier agents

One agent per tier, each file named for the tier it serves: `light`, `balanced`, `heavy`, `frontier`. The name is the whole routing mechanism, so it has to be the policy's word and nothing near it.

Run this once per harness present, skipping any whose agent directory does not exist. For a harness not in the table, read its own documentation first: where subagents live, and whether its delegation tool takes a model parameter.

## Where each harness keeps them

| | OpenCode | ZCode | Gemini CLI |
| --- | --- | --- | --- |
| Agent directory | `~/.config/opencode/agents/` | `~/.zcode/agents/` | `~/.gemini/agents/` |
| Required fields | `description`, `mode: subagent`, `model` | `name`, `description`, `model` | `name`, `description`, `model` |
| Field dialect | lower_snake | camelCase, case-sensitive | lower_snake |
| What `model` names | `provider/model-id` | a model id | a config alias |
| Choosing the model | **ask**, per the catalogue steps | pre-defined below | pre-defined below |

Traps, each of which fails silently rather than loudly:

- **OpenCode**: `opencode.json`'s `agent.*.model` binds the built-ins (`build` and `plan` primary, `general` and `explore` subagents). That file is the user's. Report it, change nothing in it.
- **ZCode**: `thoughtLevel` needs an explicit `model` beside it or it is dropped. No project-level subagents yet, so global is the only scope.
- **Gemini CLI**: an unrecognised `thinkingLevel` is dropped rather than rejected, and the allowed set grows between releases. Confirm the installed bundle knows the level before relying on it.

## Pre-defined ladders

Confirm each id against the harness before writing it: generations move and ids move with them. Prefer the ids an install actually uses over the ones it merely lists, which counting occurrences across its own caches separates.

**ZCode**, the GLM family under the user's coding plan, at zero marginal cost. Escalates by model, then by reasoning level:

| Tier | `model` | `thoughtLevel` |
| --- | --- | --- |
| light | `glm-5.3-flash` | default |
| balanced | `glm-5.3` | `high` |
| heavy | `glm-5.3` | `max` |

**Gemini CLI**, Gemini 3.8 Flash (`gemini-3.8-flash`) at three thinking levels, so the levels are the ladder and the model stays fixed:

| Tier | `model` | `thinkingLevel` |
| --- | --- | --- |
| light | `gemini-3.8-flash` | `LOW` |
| balanced | `gemini-3.8-flash` | `MEDIUM` |
| heavy | `gemini-3.8-flash` | `HIGH` |

Those aliases go in `~/.gemini/settings.json` under `modelConfigs.customAliases`, which merge over the built-ins:

```json
{
  "modelConfigs": {
    "customAliases": {
      "light": {
        "extends": "chat-base-3",
        "modelConfig": {
          "model": "gemini-3.8-flash",
          "generateContentConfig": { "thinkingConfig": { "thinkingLevel": "LOW" } }
        }
      }
    }
  }
}
```

Neither harness carries a Frontier rung: nothing in the GLM family sits above Heavy, the Flash generation has no Pro sibling, and `MINIMAL` is rejected outright.

## When a harness has fewer rungs than the policy

Write the tiers it can carry and no filler. Two tiers on one binding is a distinction that does not exist, and the orchestrator spends the more expensive name believing it escalated. Name the missing tier and the real ceiling in the report, so escalation stops somewhere the user knows about.

## Choosing OpenCode's ladder

### 1. Read the live catalogue

- `opencode models` is the authority on what is bindable and which providers are authenticated.
- `https://models.dev/api.json` carries the economics: `<provider>.models.<id>.cost.input` and `.cost.output` per million tokens, `.limit.context` for the window.

Rank by input price. A vendor's own ladder (flash, plus, max, pro) hints at capability but never sets the ranking.

Pull out the models costing nothing, `cost.input` and `cost.output` both zero, and tell the two kinds apart, because they fail differently:

- **Subscription-covered**: a flat-rate plan the user already pays for, reporting zero marginal cost. Stable, and the strongest candidate for any tier it can carry.
- **Free-listed**: given away for now, often marked in the id. Rotates without warning, and the agent bound to it then fails at spawn rather than at setup.

Where a subscription covers the whole ladder, keeping every tier inside it is the cheapest correct answer available.

### 2. Offer the user a model per tier

One `AskUserQuestion` call, one question per tier, each option carrying the model id and its price in and out. Recommend first:

- **Light**: the cheapest model that still writes correct code.
- **Balanced**: clearly under Heavy, code-tuned where the catalogue offers it. The workhorse, so its price is the one that compounds.
- **Heavy**: strong general reasoning near the top of the catalogue.
- **Frontier**: the most capable available, chosen on capability alone.

Offer a zero-cost model wherever it is credible, labelled with its kind: recommend a subscription-covered one outright, and state the rotation risk on a free-listed one so the user takes that trade knowingly.

Keep the tiers monotonic in price. A subscription covering several tiers is the exception: there capability ascends instead, and the bindings still have to differ.

## Writing the agents

One file per tier, in that harness's directory and dialect:

```markdown
---
description: <what this tier takes on, leading with the work, not the model>
model: <model id, or the alias carrying the reasoning level>
---

<two short paragraphs: the work this agent owns, and how it goes about it>
```

The `description` is what the orchestrator reads when choosing a subagent, which makes it a context pointer rather than documentation: lead with the kind of work, and name genuinely distinct cases rather than synonyms for one.

Where a tier file exists, rewrite its model line and leave the body. Where one survives under an older name (`fast` for Light, `general` for Balanced), rename it onto the tier: two files serving one tier gives the orchestrator a coin to flip.

## Verify

- Each directory holds the tiers that harness can carry, and no legacy duplicate.
- Every model value resolves: a raw id appears verbatim in the harness's model list, an alias in the settings defining it. A typo binds the agent to nothing and surfaces only when a spawn fails mid-task.
- The tiers ascend in capability, and in price wherever the models are metered.
- Any tier left on a free-listed model is named as such in the report, since re-running this skill is what re-checks it.

## Bodies

**light**

> You are a fast implementer. You handle small, well-scoped changes: renames, small functions, tweaks, formatting, small bug fixes, test additions. Do exactly what is asked, no refactoring beyond the request, no commentary beyond the result.

**balanced**

> You are the default implementer. You handle moderate changes: multi-step edits within a component, new functions and their call sites, ordinary feature work and bug fixes, debugging and tests.
>
> Read the surrounding code before changing it, keep the change coherent, and verify with the project's lint, typecheck and test commands when present. When the brief is read-only (explore, review, plan), report findings and change no files.

**heavy**

> You are a heavyweight implementer for drastic changes: cross-cutting refactors, architecture changes, large feature work, migrations, security-sensitive edits. Read the surrounding code before changing it, keep changes coherent across files, and verify with the project's lint, typecheck and test commands when present.

**frontier**

> You are the last resort. You take the problems a heavyweight implementer has already failed at, and the long-horizon runs where an error compounds across many steps: subtle debugging, high-risk migrations, decisions that are expensive to reverse.
>
> Read widely before you act, state the assumption behind each decision, and verify with the project's lint, typecheck and test commands when present. Say plainly when the evidence does not support a conclusion rather than guessing.
