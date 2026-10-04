# Writing skill documentation pages

Every skill outside `deprecated/` is promoted and has a human-facing page at `documentation/skills/<bucket>/<name>.md`. Deprecated skills get no page.

Create or re-sync the page when a promoted skill is added, renamed, moved, or behaviorally changed. Remove stale pages after renames or removals. Update active cross-links, bucket listings, the top-level README, and the `guide` router together. Historical upstream archives and handoffs remain unchanged.

The page helps a reader choose and understand one skill; it does not repeat the agent's runbook. There is no H1. Installation commands live only in the top-level README, copied from [the canonical install block](./install-block.md).

## Provenance first

Start with a plain provenance sentence identifying the original upstream skill name or names. Verify them against `.upstream/` artifacts or retained Git history rather than inferring them from today's directory names.

- A renamed skill identifies its upstream name and its current name.
- A combined skill identifies the contributing upstream skills.
- A fork-added skill says so explicitly instead of inventing an upstream equivalent.
- An external source identifies its skill and project; do not imply it came from the upstream fork.

Use literal historical names only for provenance or migration explanations, not as active invocation names or aliases. A relative link to supporting provenance is allowed. Explain consequential drift and its reason on the page or in the top-level README, not merely that a rename occurred.

## Page structure

Use this order. The four sections `What it does`, `When to reach for it`, `Common questions`, and `It's working if` are required. `Where it fits` is also present on every page.

### What it does

Lead with the one-sentence job, then its defining constraint. For example, `specify` resolves only outstanding decisions and can synthesize settled context without repeating an interview. State what it actually does, not what an earlier upstream version did.

### When to reach for it

State how it is reached and the trigger boundary. Every skill can be run by the user typing `/<name>` or reached by an agent or another skill when the task fits; do not describe a skill as user-only or model-only. Say instead when it fits, and name any approval gate it keeps (for example, publication or writes outside the repository).

Where it is confusable with another skill, explain the distinction and link to that page.

### Prerequisites

Include this optional section only when the skill needs a workspace, configuration, access, or tooling. State what setup is actually required. Do not make local refinement or `iterate` depend on a remote tracker merely to maintain documents.

### Focused substance

Use one to three optional sections in the skill's own vocabulary. Explain its defining idea and artifact responsibilities without copying steps or templates. Put choices in a table or list, not a dense paragraph.

### Common questions

Use bold questions followed by plain answers. Prefer observed questions from this repository's issues, discussion, existing pages, Git history, and changelog over invented ones. The current request is primary evidence when it reveals confusion, such as the former split between interviewing and specification writing.

Keep the count proportional to useful evidence. Do not pad thin pages. Historical reports are evidence of past behavior, not proof that a bug remains unfixed after a change.

### It's working if

Use checkable signals in the reader's work or trace. A reader should not have to inspect the skill's internal compliance details to recognize success.

### Where it fits

Identify the role: a chain step, run-once setup, periodic maintenance, or standalone discipline. Link the relevant neighbors with a reason, then link to `../getting-started/guide.md`.

The planned development route is `specify → taskify → implement → review-and-refactor`. Just-in-time development uses the `iterate` skill and the same project documents. General `refine` does not force a software specification.

## Writing and links

- Follow repository language rules and apply `unslop`.
- Explain behavior and its reason, not author opinions.
- Preserve useful primary evidence and questions without repeating upstream commentary as current fact.
- Keep specialist terminology understandable and use the skill's established vocabulary.
- Link rather than duplicate requirements, specifications, or shared format rules.
- Resolve relative links from the page's actual directory. A skill link from a page under `documentation/skills/<bucket>/` starts with `../../../skills/`.
- Keep supporting links repository-relative; do not rely on an upstream website to explain this fork.

## Done when

- The page matches the promoted skill's current bucket and name; no orphan page remains.
- The first line has verified provenance or an explicit fork-specific note.
- Required sections are present in order, with the trigger boundary and defining constraint accurately stated.
- Meaningful upstream drift is explained on the page or in the README.
- Every relative target resolves and active names match installed skill identifiers.
- No installation command is copied into the page.
- `python3 scripts/check-skills.py` passes after the integrated change.
