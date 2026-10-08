# Tier agents

One agent per tier, each file named for the tier it serves: `light`, `balanced`, `heavy`, `frontier`. The name is the whole routing mechanism, so it has to be the policy's word and nothing near it.

Run this once per harness that binds a model to a named agent. A harness with a per-call model override needs none of it.

## Contents

- Learn the harness's agent format
- Choose the models
- When a harness has fewer rungs than the policy
- Write the agents
- Verify
- Bodies

## Learn the harness's agent format

Read the harness's current documentation for subagents. Settle four facts before writing anything:

- The directory the agent files live in, and whether it has a project scope as well as a global one.
- The required fields, and the field dialect (casing is sometimes case-sensitive).
- What the `model` field takes: a provider-qualified id, a bare model id, or an alias defined in the harness's settings.
- How reasoning effort is set, when the harness has that control. A harness that offers one model at several reasoning levels can use the levels as its ladder.

Some mistakes fail silently rather than loudly: a field dropped because a companion field is missing, an unrecognised reasoning level ignored, a model id that resolves to nothing until a spawn fails mid-task. The verify checks below exist for these.

## Choose the models

The user chooses from models the harness actually has, so the choice starts from its live catalogue.

### 1. Read the catalogue

Use the harness's model-listing command or documented list as the authority on what is bindable and which providers are signed in. Take prices per million tokens and context windows from the provider's published data or the harness's own listing, and say so when a price is unavailable. Rank by input price. A vendor's own ladder (flash, plus, max, pro) hints at capability but never sets the ranking.

Pull out the models costing nothing, and tell the two kinds apart, because they fail differently:

- **Subscription-covered**: a flat-rate plan the user already pays for, reporting zero marginal cost. Stable, and the strongest candidate for any tier it can carry.
- **Free-listed**: given away for now, often marked in the id. Rotates without warning, and the agent bound to it then fails at spawn rather than at setup.

Where a subscription covers the whole ladder, keeping every tier inside it is the cheapest correct answer available.

### 2. Offer a model per tier

Ask one round, one question per tier, each option carrying the model id and its price in and out when known. Recommend first:

- **Light**: the cheapest model that still writes correct code.
- **Balanced**: clearly under Heavy, code-tuned where the catalogue offers it. The workhorse, so its price is the one that compounds.
- **Heavy**: strong general reasoning near the top of the catalogue.
- **Frontier**: the most capable available, chosen on capability alone.

Offer a zero-cost model wherever it is credible, labelled with its kind: recommend a subscription-covered one outright, and state the rotation risk on a free-listed one so the user takes that trade knowingly. Keep the tiers monotonic in price. A subscription covering several tiers is the exception: there capability ascends instead, and the bindings still have to differ.

Apply `POLICY.md`'s model-version rule to every binding. Installed bindings and caches can show the family in use, but the live catalogue says which versions are available.

Where the user keeps an existing binding, keep it, and report whether it still resolves.

## When a harness has fewer rungs than the policy

Write the tiers it can carry and no filler. Two tiers on one binding is a distinction that does not exist, and the orchestrator spends the more expensive name believing it escalated. Name the missing tier and the real ceiling in the report, so escalation stops somewhere the user knows about.

## Write the agents

One file per tier, in the harness's directory and dialect:

```markdown
---
description: <what this tier takes on, leading with the work, not the model>
model: <model id, or the alias carrying the reasoning level>
---

<two short paragraphs: the work this agent owns, and how it goes about it>
```

The `description` is what the orchestrator reads when choosing a subagent, which makes it a context pointer rather than documentation: lead with the kind of work, and name genuinely distinct cases rather than synonyms for one.

Where a tier file exists, rewrite its model line and leave the body.

## Verify

- The directory holds the tiers the harness can carry, one file each.
- Every model value resolves: a raw id appears verbatim in the harness's model list, an alias in the settings defining it.
- Every binding satisfies `POLICY.md`'s model-version rule against the live catalogue.
- The tiers ascend in capability, and in price wherever the models are metered.
- Any tier left on a free-listed model is named as such in the report, since running this skill again is what re-checks it.

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
