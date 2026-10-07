# Design format

A capability's design, `documentation/capabilities/<capability>/design.md`, says how the code delivers that capability's specifications inside the system's architecture. It uses the vocabulary in [MODULES.md](MODULES.md) and the glossary's terms.

## Structure

```md
# {Capability} design

{One paragraph: the approach, and the architecture parts it lives in.}

## Modules

- **{Module}** ({where in the code}): {what it hides}. Interface: {entry points, with invariants, error modes, and ordering constraints a caller must know}.

## Data

{The entities or records this capability owns or changes, their key fields and states, and where they are stored. Data another capability owns is reached through that capability's module, named here.}

## Seams

- **{Seam}**: {what varies across it}; adapters: {production adapter}, {test adapter}.

## Acceptance

| Acceptance criterion | Module and test seam |
| --- | --- |
| {criterion, as in the specifications} | {the module that delivers it and the interface the test drives} |

## Requirements

| Requirement | How the design meets it |
| --- | --- |
| {Short name} | {the module, data choice, or seam that satisfies it} |

## Alternatives

- **{Option not taken}**: {why not}

## Open

- {Unresolved design question, with its recommendation}
```

## Rules

- **Design inside the architecture.** Use the parts, stack, and data ownership the architecture document sets. A design that needs them changed records a proposed decision instead; see the skill's escalation rule.
- **Prefer deep modules**: a small interface over a lot of behavior. Introduce a seam only where something varies (at least two adapters, usually production and test).
- **Trace every acceptance criterion and requirement** to the module that delivers it. A criterion with no module is a gap; list it under Open.
- **Leave out code**: no full implementations. A short interface signature or type is fine where it is clearer than prose.
- **Keep it current**: update the design when the implementation departs from it for a good reason, instead of letting the two drift.
- **Omit empty sections.** A small capability may need only the approach, its modules, and the acceptance table.
