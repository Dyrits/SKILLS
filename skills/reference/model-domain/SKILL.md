---
name: model-domain
description: Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a GLOSSARY.md, recording or editing an architecture decision record, or creating a GUIDELINES.md.
---

# Model domain

Actively build and sharpen the project's domain model as you design. This is the *active* discipline: challenging terms, inventing edge-case scenarios, and writing the glossary and decisions down the moment they crystallise. (Merely *reading* `GLOSSARY.md` for vocabulary is not this skill: that's a one-line habit any skill can do. This skill is for when you're changing the model, not just consuming it.)

## File structure

Most repositories have a single context:

```
/
├── GLOSSARY.md
├── documentation/
│   └── architecture-decision-record/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a `GLOSSARY-MAP.md` exists at the root, the repository has multiple contexts. The map points to where each one lives:

```
/
├── GLOSSARY-MAP.md
├── documentation/
│   └── architecture-decision-record/ ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── GLOSSARY.md
│   │   └── documentation/architecture-decision-record/ ← context-specific decisions
│   └── billing/
│       ├── GLOSSARY.md
│       └── documentation/architecture-decision-record/
```

Create files lazily: only when you have something to write. If no `GLOSSARY.md` exists, create one when the first term is resolved. If no `documentation/architecture-decision-record/` exists, create it when the first architecture decision record is needed.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `GLOSSARY.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account': do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"

### Update GLOSSARY.md inline

When a term is resolved, update `GLOSSARY.md` right there. Don't batch these up: capture them as they happen. Use the format in [GLOSSARY-FORMAT.md](./GLOSSARY-FORMAT.md).

`GLOSSARY.md` should be totally devoid of implementation details. Do not treat `GLOSSARY.md` as a specification, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Offer architecture decision records sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the architecture decision record. Use the format in [ARCHITECTURE-DECISION-RECORD-FORMAT.md](./ARCHITECTURE-DECISION-RECORD-FORMAT.md).

## Guidelines

`GUIDELINES.md` at the repository root holds the project's code conventions: portable rules a reviewer applies to any diff, never product behaviour. Creating it is part of this skill when a calling skill asks, or when the user wants to write down their conventions. Read [GUIDELINES-FORMAT.md](./GUIDELINES-FORMAT.md) for what belongs, the interview, the format, auditing an existing file, and declining.
