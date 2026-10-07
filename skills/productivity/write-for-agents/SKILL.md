---
name: write-for-agents
description: "Write documents for agents: skills, AGENTS.md, and documents reached by a pointer. Use when creating or editing skills, or modifying AGENTS.md."
metadata:
  forks: "mattpocock/skills/skills/productivity/writing-for-agents"
---

Reference for writing any document an agent consumes: a skill, an `AGENTS.md`, a document reached by a pointer. The packaging differs; the writing principles aim for a predictable process across runs rather than identical output.

Before creating or editing a skill or its description, read [Anthropic's skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) for the current authoring and frontmatter guidance, and [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md) for this collection's invocation conventions, splitting, and router skills. If the official page cannot be accessed, report that limitation rather than claiming to have checked its current requirements.

## Context pointers

A **context pointer** is a reference held in the agent's context that names some out-of-context material and encodes the condition for reaching it. A skill's description is one; a line in `AGENTS.md` naming a document is the same object. The pointer's _wording_, not its target, decides when the agent reaches the material, and how reliably. A must-have target behind a weakly worded pointer is a variance bug: sharpen the wording first, and inline the material only if sharpening fails.

A pointer does two jobs: state what the material is, and list the **branches** that should trigger reaching it (a branch is a distinct case the document handles, so different runs take different paths through it). Every word of an always-loaded pointer costs on every turn, so it earns even harder pruning than the body:

- **Front-load the leading word**: the pointer is where it does its triggering work.
- **One trigger per branch.** Synonyms that rename a single branch are one branch written twice; collapse them and keep only genuinely distinct branches.
- **Cut identity the body already carries.**

## The two loads

Every document and pointer you add spends one of two budgets:

- **Context load** is the cost of always-loaded material on the agent's window: an `AGENTS.md` line, a skill description, anything sitting in context every turn, spending tokens and attention whether or not it fires.
- **Cognitive load** is the cost on the human: which documents exist and when to reach for each. The human is the index. Not a cost to minimize: it is the price of human agency; spend it where human judgment matters, remove it where it does not.

Material reached only through a pointer escapes context load at the price of the pointer's own line; material with no pointer at all rides entirely on cognitive load.

## Information hierarchy

A document is built from two content types: **steps** (the ordered actions the agent performs) and **reference** (definitions, rules, facts consulted on demand). The two mix freely: all steps (a recipe), all reference (a review's rules, this skill), or both. The **information hierarchy** orders material by how immediately the agent needs it:

1. **In-file step** is the primary tier: what the agent does, in order.
2. **In-file reference** is consulted on demand. A set of related rules can stay together without further subdivision.
3. **Disclosed reference** is pushed out into a separate file, reached by a context pointer, loaded only when the pointer fires. It ranges from a sibling file in the same folder to an external document that any file can point at.

Push too little down and the top bloats; push too much and you hide material the agent actually needs. That tension is the whole decision.

**Progressive disclosure** moves conditional reference out of the main file and behind a pointer. Inline what every branch needs, and disclose what only some branches reach. This keeps the common steps visible without making each run read unrelated material.

**Co-location** keeps a concept's definition, rules, and caveats under one heading, so reading a rule also exposes its exceptions. This differs from duplication: duplication repeats one meaning in several places; scattering separates parts needed to understand it.

**Sprawl** is a document too long to use effectively, even when each line is relevant and unique. Disclose conditional reference and split by branch or sequence when that makes each path easier to follow. Length alone is not a reason to remove a requirement.

## Steps and completion criteria

Every step ends on a **completion criterion**, the condition that tells the agent the work is done. Check two properties:

- **Clarity**: can the agent tell done from not-done? A vague bound ("understanding reached") lets the agent end the step early: **premature completion**. Sharpen the bound first. Separate the later steps only if runs still rush a clearly bounded step, and only across a real context boundary (a handoff or a subagent dispatch): text under another heading, or an inline skill call, stays in context.
- **Demand**: how much it requires. "Every modified model accounted for" defines coverage; "produce a change list" only names an output. State the coverage the task needs. This applies to reference rules as well as sequences of steps.

The strongest criteria are both checkable and exhaustive.

## When to split

Splitting one document into two spends one of the two loads, so split only when the cut earns it:

- **By sequence**: split when observed runs skip required work despite clear completion criteria. Give each phase the information it needs, and confirm on the next runs that the split helped.
- **By invocation**, skill-specific: see [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md).

## Leading words

A **leading word** is a familiar term the agent thinks with while running the document (_lesson_, _fog of war_, _tracer bullets_). Define it once, then repeat the word instead of the definition. Prefer an existing word to a coined one: the model already knows what a familiar word means, so its definition can stay short. Use the same word in the pointer as in your prompts, documentation, and code, so the agent recognizes the shared term when deciding whether to reach the material.

When the same idea is spelled out at two or more sites, define it once and refer back with a leading word, keeping any requirement the shorter term would lose. For example:

- _Tight_ for a loop already defined as fast, deterministic, and low-overhead.
- _Red_ for a test failing for the intended reason, rather than "a loop you believe in."

Make the substitution only where the repetition exists. Stop when the identified repetitions are addressed; leaving the text unchanged is a valid result.

**Negation**: state the desired behavior rather than only the prohibition, since naming the banned action can prime it. Keep explicit prohibitions for hard guardrails and pair each with the permitted action, for example: "Do not publish before approval. Show the exact text and destination, then wait for the user's confirmation."

## Pruning

- Keep each meaning in a **single source of truth**: one authoritative place, so changing the behavior is a one-place edit. **Duplication** repeats the same rule in multiple places, increasing maintenance and the chance of disagreement. A leading word instead refers back to the rule without restating it.
- The **environment** is a source of truth too (`package.json` scripts, config files, the directory layout, `--help` output), and a document that restates it is a **cache**: a copy of a lookup, earning its load only when the lookup is expensive. Cache what the agent cannot find by looking: the unwritten convention, the reason behind a choice, the gotcha no config confesses. Leave the one-file, one-command lookups to the environment, where they cannot go stale.
- Check every line for **relevance**: does it still bear on what the document does? Verify suspected stale material against its source before removing it. Disclose conditional detail rather than treating it as irrelevant. Preserve requirements, approval boundaries, exceptions, and recovery instructions when shortening or moving text.
- A **no-op** is an instruction that does not change the model's behavior compared with its absence. During an editorial review, distinguish a suspected no-op from one supported by comparative runs. Keep an obligation that only seems obvious until a comparative run shows the model meets it without the line. "No change needed" is a valid result.

When the user requests skill evaluations or a behavioral comparison of skill instructions to resolve a disputed no-op, call the Skill tool with "skill-creator". Use its evaluation workflow rather than duplicating one here. If it is missing, give the installation command `npx skills@latest add anthropics/skills --skill=skill-creator` and ask whether to install it or leave the comparison pending. Ordinary editing does not require evaluations; when they are deferred, report the change as an editorial judgment, not proven behavioral improvement.
