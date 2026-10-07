# Invocation

Every `SKILL.md` in this repository is a skill, and every skill is reachable by **both** the human typing its name and the model, including another skill calling it. There is no user-only skill: omit `disable-model-invocation` from the frontmatter and the `policy` block from `agents/openai.yaml`. `scripts/check-skills.py` fails on either.

The `description` is therefore always **model-facing**: a context pointer carrying the trigger branches ("Use when the user wants…, asks for…"), written by the pointer rules in [write-for-agents](../../skills/productivity/write-for-agents/SKILL.md). Every description sits in the model's context every turn, so keep it short. For a skill with heavy cost or outward effects (publishing, pushing, long multi-agent runs, machine-wide setup), trigger on the user's explicit request so it does not fire speculatively; its body still asks before any authorized-only action.

Every skill also carries an `agents/openai.yaml` beside its `SKILL.md`, holding Codex UI metadata: `interface.display_name` and `interface.short_description` for the skill picker.

## Dependencies between them

Dependencies are expressed as an explicit instruction to **call the Skill tool** with the named skill (`Call the Skill tool with "interview"`), not deep `../other-skill/FILE.md` cross-references, and not a bare `/skill`-style mention left for the model to interpret. Naming the tool is what gets it fired: most harnesses expose skill invocation as a tool the model calls, and spelling that out gets a higher hit rate than dropping a `/name` into prose and hoping it's read as a command. Dropping the leading `/` also keeps this harness-neutral rather than less: a skill name on its own carries no assumption about which harness's trigger syntax it belongs to. Shared reference documents live inside the skill that owns them; other skills reach that material by calling the Skill tool with it, not by linking across folders.

This is about **operative** instructions: a skill's own steps telling the agent to go run another skill right now. Router prose that just names skills for a human to pick from (`guide`, bucket `README.md`s) isn't invoking anything, so it keeps `/skill`-style names as plain labels.

The Skill tool takes one skill per call. A step that needs two skills is two calls, not one call with two names: say so (`Call the Skill tool twice, for "interview" and "delineate"`), not "call it with X and Y," which reads as a single call taking both.

Every named skill must exist in the repository (or be a listed external skill); `scripts/check-skills.py` rejects a call to an unknown name.

Dependencies install with the skill: APM reads each skill's `apm.yml`, which `.agents/scripts/generate-skill-manifests.py` derives from the skill's Skill tool calls and handovers, and installs every skill it references alongside it. Every skill that calls another carries a **Calls** paragraph right after its opening, with a **Hands over to** clause for the skills it tells the user to run: the names only, with no install command, no step for a missing skill, and no waiting for an install. `check-skills.py` owns the wording: it derives both lists from the Skill tool calls and handovers in the skill's folder (Markdown and shell scripts), leaves out external skills and the `guide` router, and prints the expected paragraph when one is missing or stale. The exception is a skill that ships outside this repository (`EXTERNAL_SKILLS` in `scripts/check-skills.py`): APM does not install it, so the step that calls it says what to do without it. Write handovers as "tell the user to run `/name`" so the generator finds them.

Calling is not always right: when the timing or the decision belongs to the human (setting up the workspace, syncing a finished worktree), hand it over as an instruction to act on, "tell the user to run `/setup-ai-workspace`", and leave the Skill tool out of it.

## Passive vs active domain work

Merely _reading_ the glossary for vocabulary is a one-line prose pointer, not the `delineate` skill. Only the active discipline (challenge a term against the glossary, the code, and edge-case scenarios, then have it written down inline through `document`) is `delineate`.
