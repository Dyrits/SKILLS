# Writing agent instructions

Adapted from the `write-for-agents` skill: the rules for editing a steering file (`AGENTS.md`) or a document an agent reaches through a pointer. Where the project has its own writing rules for these files, they take precedence.

## Pointers

A line in `AGENTS.md` naming a document is a **context pointer**: its wording, not its target, decides when the agent reaches the material. It states what the material is and the distinct cases that should trigger reaching it.

- **Front-load the leading word**, where the pointer does its triggering work.
- **One trigger per case.** Synonyms renaming one case are one case written twice; keep only genuinely distinct cases.
- **Cut identity the target already carries.**

A must-have target behind a weakly worded pointer is a bug: sharpen the wording first, and inline the material only if sharpening fails.

## Load

Every always-loaded line costs tokens and attention on every turn, whether or not it fires. Put material only some cases need behind a pointer, and inline only what every case needs.

## Pruning

- Keep each rule in **one place**, so changing it is a one-place edit; refer back to it instead of repeating it.
- The **environment** is a source of truth too (`package.json` scripts, configuration, the directory layout, `--help` output). Write down what the agent cannot find by looking: the unwritten convention, the reason behind a choice, the gotcha no configuration confesses.
- Check every line for relevance, and verify suspected stale material against its source before removing it. Preserve requirements, approval boundaries, exceptions, and recovery instructions when shortening or moving text.
- State the desired behavior rather than only a prohibition; keep explicit prohibitions for hard guardrails and pair each with the permitted action.

Check for an existing line that already covers the rule before adding one, and update it instead of adding a near-duplicate.
