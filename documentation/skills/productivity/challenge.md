Fork-specific skill, created for this collection to review choices on any topic and retain the reasoning across rounds.

## What it does

`challenge` tests a choice against your goals, assumptions, alternatives, and consequences.
It gives candid feedback, asks focused questions, and updates its assessment as you answer.
You retain the decision, including the option to accept a tradeoff the agent would avoid.

The review tracks concerns as open, resolved by evidence, mitigated, or accepted by you.
This record lets a later round or session continue without repeating settled objections.
The outcome can be to keep, change, or defer the choice.

## When to reach for it

Type `/challenge` with a choice and your reasons, or ask the agent to challenge a decision or play devil's advocate.
It applies to personal, professional, creative, technical, and other decisions, whether you are leaning toward an option or have already acted.
For example: "Challenge my decision to take a management role; I want more influence, but I enjoy hands-on work."

Start with a choice you want examined.
[interview](../shaping/interview.md) is for settling an open plan or idea through rounds of recommended questions; `challenge` starts with your position and tests its reasoning and consequences.

## The decision review

The agent first states the strongest fair case for your choice, then concentrates on concerns that could change the decision.
It compares feasible alternatives against the same goals and makes costs, affected people, recovery options, and later effects explicit.
Questions about concrete situations help establish which consequences you understand and are willing to accept.

The review stays in the conversation by default.
For project decisions or when you ask to save it, the agent creates a dated record in the appropriate document home and makes project records discoverable through `AGENTS.md`.
Personal reviews stay out of unrelated project files.

## Common questions

**Can it cover any topic?**

Yes.
It needs neither code nor a repository and adapts its questions to your goals and the stakes.
Where a decision depends on specialist knowledge, it identifies the evidence or qualified advice still needed and marks uncertain claims.

**Will it argue until I change my mind?**

No.
It withdraws objections your answers resolve and can conclude that your original choice holds up.
You can accept a known cost, ask for a single-pass review, or stop with concerns still open.
The record distinguishes these outcomes from demonstrated understanding or resolved uncertainty.

**Can it guarantee the decision is right?**

No.
It can expose weak assumptions and misunderstood consequences, but uncertainty may remain.
It records what would justify reconsidering the choice and does not execute or publish the decision.

## It's working if

- Feedback names a concrete assumption or consequence and explains what would address it.
- Your answers change the assessment, and resolved objections stop recurring.
- You can see which costs you accepted and which facts remain uncertain.
- The final review distinguishes your decision from the agent's assessment and gives a reason to revisit it if circumstances change.

## Where it fits

`challenge` is a standalone productivity skill.
Its decision review can inform personal action, a project decision record, or a later conversation.
[optimize-process](./optimize-process.md) focuses specifically on estimating the impact of a recurring process change.
