# Handoff: unslop rework after the skills audit

Supersedes: none. Continues the audit in `AUDIT.md` (produced in `2026-10-06-2135-remove-auto-handoff-and-skills-audit.md`); a sibling of `2026-10-07-0052-write-for-agents-tightening.md`.

## What was done

The `unslop` section of `AUDIT.md` was reviewed with the user and the skill reworked. The change itself is in the commit that adds this handoff; the `Status (2026-10-07)` line under `### unslop` in `AUDIT.md` lists what was done, kept, and left open.

Decisions and their reasons, which the diff does not show:

- **Fix the skill, not `AGENTS.md`.** The user's standing rule: skills are universal, not tied to this repository. The old "periods or commas only" rule was an upstream opinion; `AGENTS.md` is this repository's own rule. The skill now names the punctuation a sentence actually wants and defers to a project's steering file or style guide. The rule is recorded in `AGENTS.md` under "Writing skills".
- **The trigger is narrowed** to prose other people will read. The user agreed; "before a final report" and "any prose in a repository" fired on nearly every turn.
- **The no-op patterns (chatbot phrases, sycophancy, hedging, filler) were kept**: they are cheap, and weaker models still produce them. This goes against the audit.
- **The explicit calls in `publish-message` and `improve-skills` were kept** although the description alone covers them. Reasons: a description fires unreliably mid-procedure, both calls sit before an outward gate, and a call drives the `apm.yml` dependency. The user asked whether the calls are needed; the answer given was to keep them until a comparative run (via `skill-creator`) shows the description fires alone. Do not add calls to other skills.
- The audit's jargon count was judged inflated: most "harness" hits are the literal agent or test harness, and "Primitive Obsession" is a named code smell.

## Open

- Replace the metaphorical "surface" in `skills/reference/design-modules/SKILL.md` ("test surface", "surface area") and `skills/upkeep/triage/SKILL.md:14` ("request surface").
- Optional: run the `unslop` evals (especially the reworked eval 2, a team-channel message) and a with/without comparison of the two explicit calls.
- The rest of `AUDIT.md`'s "Suggested order of work".

## Suggested skills

- `write-for-agents` (Skill tool) before editing any `SKILL.md` or `AGENTS.md`.
- `skill-creator` (Skill tool) to run evals or the explicit-call comparison.
- `unslop` (Skill tool) on prose meant for readers.
- `memorize` (Skill tool) when the user states a standing rule.
