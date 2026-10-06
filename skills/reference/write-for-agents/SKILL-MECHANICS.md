# Skill mechanics

The skill-specific branch of [`write-for-agents`](SKILL.md): invocation conventions, splitting, and router skills. Everything else about writing it is the universal reference in `SKILL.md`.

Frontmatter requirements, name and description limits, and description voice come from the official best-practices page that `SKILL.md` links. The invocation policy below is this collection's convention, not a platform requirement.

## Invocation

Every skill here is reachable three ways: the human types its name, the agent fires it from its description, and another skill calls it through the Skill tool. Mechanics: omit `disable-model-invocation`, and write a model-facing description carrying the trigger branches (the pointer-writing rules in `SKILL.md` apply in full).

The description is the skill's top-level context pointer, forced to stay loaded at all times: every skill pays permanent context load in exchange for discoverability and composability. Pay it with the shortest pointer that still triggers. A skill whose content is all reference is also one home for shared reference: any skill can invoke it, so reference needed by several skills lives in one place.

Reach is not license. For a skill with heavy cost or outward effects (publishing, pushing, long multi-agent runs, machine-wide setup), word the trigger around the user's explicit request so it fires when asked, and keep the body's approval gates: a caller reaching the skill still stops where the skill asks.

## Splitting by invocation

The invocation cut of splitting (the sequence cut lives in `SKILL.md`): split off a new skill when you have a distinct leading word that should trigger it on its own (a trigger word you actually use in your prompts), or several skills must reach the same procedure. You pay context load for the new always-loaded description, so that independent reach has to be worth it.

## Router skills

When skills multiply past what you can remember, that piled-up cognitive load is cured by a **router skill**: one skill that names the others and when to reach for each, so the human has one skill to remember instead of many. It routes by naming, leaving the choice to the human; the skills it names stay callable by any skill whose steps need them.
