# GUIDELINES.md scoped to portable code conventions

Supersedes: `.agents/handoffs/2026-10-04-0150-issue-2-feedback-and-git-guardrails.md`

## What happened

- The user found that `/Volumes/APFS-G-DRIVE/Codelab/LIFELINE/GUIDELINES.md` read like specifications, decisions and workflow rather than code conventions. The cause was in `model-domain`'s `skills/reference/model-domain/GUIDELINES-FORMAT.md`: "judgement-call rules" admitted anything, and candidates were drafted from what the product does.
- Fixed in `e4f6ca2` (its message lists every file). The leading word is **portable**: a rule must still hold if the product changed and only the stack and team stayed. Non-portable candidates are routed to requirements, an architecture decision record, `GLOSSARY.md`, `AGENTS.md`, or tooling. A new "Auditing an existing file" section covers checking a file like LIFELINE's.
- Checks passing before commit: `npm run check-skills`, `claude plugin validate . --strict`, `git diff --check`.

## Out of scope

- **LIFELINE migration**: the user will handle it. The proposed moves were given in conversation only: the line invariant goes to global `documentation/requirements.md`, "built ahead without the DOM" to an architecture decision record, the visible-text rule splits (keep "no user-facing string literals in rendering code"; the language pair, French typography and "French is the source" go to global requirements), the caption voice goes to a captions capability's requirements when one exists (global otherwise) and fact confirmation to `AGENTS.md`, and screenshot verification to `AGENTS.md`. LIFELINE has neither `documentation/requirements.md` nor `documentation/capabilities/` yet.
- **Follow-up**: the routing table row in `GUIDELINES-FORMAT.md` now names both requirement levels (global `documentation/requirements.md` versus a capability's requirements or specifications), matching `skills/reference/document/PROJECT-DOCUMENTS.md`.

## Unverified

- No eval run of the new interview against a real repository; whether it now yields only portable rules is untested.
- Carried over: whether a hook's `ask` prompts under `bypassPermissions`, and the untested OpenCode permission rules (see the superseded handoff).

## Open items

Carried, still undecided by the user:

- `~/.agents/skills/improve-agent-environment` is a real directory copy, not a symlink; removal awaits go-ahead.
- Version stays at 0.2.0; no bump decided for this change or the previous ones.

## Suggested skills

- `model-domain` (model-invoked, Skill tool): run its Guidelines step to test the new interview, or its audit on an existing `GUIDELINES.md`.
- `write-for-agents` (model-invoked): before editing any `SKILL.md`.
- `skill-creator` (model-invoked): if the user wants an eval of the interview.
- `/improve-skills` (user-invoked): report problems found while using the new interview.
