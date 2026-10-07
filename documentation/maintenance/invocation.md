# Invocation

Every `SKILL.md` in this repository is a skill, and every skill is reachable by **both** the human typing its name and the model. There is no user-only skill: omit `disable-model-invocation` from the frontmatter and the `policy` block from `agents/openai.yaml`. `scripts/check-skills.py` fails on either.

The `description` is therefore always **model-facing**: a context pointer carrying the trigger branches ("Use when the user wants…, asks for…"), written by the pointer rules in [write-for-agents](../../skills/productivity/write-for-agents/SKILL.md). Every description sits in the model's context every turn, so keep it short. For a skill with heavy cost or outward effects (publishing, pushing, long multi-agent runs, machine-wide setup), trigger on the user's explicit request so it does not fire speculatively; its body still asks before any authorized-only action.

Every skill also carries an `agents/openai.yaml` beside its `SKILL.md`, holding Codex UI metadata: `interface.display_name` and `interface.short_description` for the skill picker.

## Dependencies between them

There are none. Each skill completes its advertised task installed alone ([architecture decision record 0005](../architecture-decision-record/0005-make-skills-autonomous.md)): it carries the instructions, references, templates, and formats it needs as files in its own folder, linked by a relative path (`[INTERVIEW.md](INTERVIEW.md)`). It neither calls another skill through the Skill tool nor tells the user to run one as the next step. Workflows connect through project artifacts: one skill writes a document, and another reads it.

When several skills need the same reference (the interview method, the project document contract, a format), each carries its own copy, adapted only where its use differs, and headed with the skill it was adapted from when that is not the skill itself. Keeping the copies aligned is repository maintenance; nothing checks it yet.

The exception is a skill that ships outside this repository (`EXTERNAL_SKILLS` in `scripts/check-skills.py`, such as `webapp-testing` and `skill-creator`): a step may call it through the Skill tool, and says what to do when it is not installed. `scripts/check-skills.py` still derives a **Calls** or **Hands over to** paragraph from any other Skill tool call or "tell the user to run `/name`" line in a skill's folder, so a new one shows up as a missing dependency paragraph. The fix is to bundle the material, not to add the paragraph.

Router prose that names skills for a human to pick from (`guide`, bucket `README.md`s, documentation pages) isn't invoking anything, so it keeps `/skill`-style names as plain labels.

## Passive vs active domain work

Merely _reading_ the glossary for vocabulary is a one-line prose pointer. Settling a disputed term (challenge it against the glossary, the code, and edge-case scenarios, then write it down) is a step a skill carries itself, with its own copy of the glossary format. `delineate` is the skill for building or cleaning up the whole functional outline and glossary.
