# Skill mechanics

The skill-specific branch of [`write-for-agents`](SKILL.md): invocation conventions, splitting, and router skills. Everything else about writing it is the universal reference in `SKILL.md`.

Frontmatter requirements, name and description limits, and description voice come from the official best-practices page that `SKILL.md` links. The invocation policy below is this collection's convention, not a platform requirement.

## Invocation

Every skill here is reachable two ways: the human types its name, and the agent fires it from its description. Skills do not call each other or suggest one another as the next step: each completes its task installed alone, and workflows connect through the project artifacts one skill writes and another reads. Mechanics: omit `disable-model-invocation`, and write a model-facing description carrying the trigger branches (the pointer-writing rules in `SKILL.md` apply in full).

The description is the skill's top-level context pointer, forced to stay loaded at all times: every skill pays permanent context load in exchange for discoverability. Pay it with the shortest pointer that still triggers. Reference that several skills need is bundled into each of them as a local copy, so none depends on another being installed; keeping the copies aligned is repository maintenance.

Reach is not license. For a skill with heavy cost or outward effects (publishing, pushing, long multi-agent runs, machine-wide setup), word the trigger around the user's explicit request so it fires when asked, and keep the body's approval gates: an agent reaching the skill still stops where the skill asks.

## Splitting by invocation

The invocation cut of splitting (the sequence cut lives in `SKILL.md`): split off a new skill when you have a distinct leading word that should trigger it on its own (a trigger word you actually use in your prompts). You pay context load for the new always-loaded description, so that independent reach has to be worth it.

## Router skills

When skills multiply past what you can remember, that piled-up cognitive load is cured by a **router skill**: one skill that names the others and when to reach for each, so the human has one skill to remember instead of many. It routes by naming, leaving the choice to the human; the skills it names stay independent of one another.
