# Handoff: agent-agnostic setup skills and audit follow-up

Supersedes: none
Workspace: Dyrits/SKILLS repository, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Work through the open priority problems of `AUDIT.md` (dated 2026-10-06) that the user ruled on: make `setup-git-guardrails` and `setup-delegation-policy` agent-agnostic, let the user pick the guard level, and spell out abbreviations. Done when the remaining priority problems in State are fixed or the user drops them.

## State

Done in the working tree and committed in the commit before this handoff (check `git log`):

- `setup-git-guardrails` rewritten. No harness is named. It asks level (1 shared history, 2 local work, 3 strict), scope, harnesses, protected branches. Two layers: a portable `scripts/pre-push` hook and a command guard `scripts/guard-git.py` that is wired into each harness by reading that harness's own documentation. `EXAMPLES.md` holds one hook example and one permission-rules example, carried over from the old skill and not re-verified against current harness releases. `scripts/confirm-dangerous-git.sh` is deleted. Verified: `python3 -I scripts/test-guard-git.py` passes (50 command cases across the three levels, hook payloads, the pre-push hook). All 12 bypasses that `AUDIT.md` lists for the old script are guarded at level 2 (test cases).
- `setup-delegation-policy` rewritten. No harness, path, model id, or ladder is hardcoded. Per harness the user chooses Configure, Reconfigure, Remove, or Skip, and picks the model per tier from that harness's own model list. `TIER-AGENTS.md` is now a harness-neutral procedure (the GLM and Gemini ladders and the legacy-rename logic are gone). Not exercised in a live session.
- `scripts/detect-harnesses.py` (identical copies in both skills) lists harness candidates found on disk with no harness named. Verified on this machine: it finds Claude, Codex, Gemini, OpenCode, ZCode, and a few unknown agent-like directories, and collapses skills-only directories onto one line. `python3 -I scripts/test-detect-harnesses.py` passes, including a check that the two copies are identical.
- Abbreviations for architecture decision record removed from `documentation/skills/productivity/hand-off.md`, `documentation/skills/shaping/research.md`, and `documentation/architecture-decision-record/0001-maintain-as-an-independent-fork.md`. The quoted Discord message in `research.md` keeps its literal "ADRs".
- Documentation pages, bucket and top-level README one-liners, the router skill's rows, manifests, and the generated `index.html` were updated.
- Checks passing at the end of the session: `python3 scripts/check-skills.py`, `python3 scripts/test-check-skills.py`, `python3 .agents/scripts/generate-skill-manifests.py --check`, `claude plugin validate . --strict`.

Status of the `AUDIT.md` priorities (checked against the files today, 2026-10-08):

- Resolved: 1 (document hard stop), 6 (stale compaction text, split handoff format).
- Fixed in this session: 3 (guardrails), 7 abbreviations, 8 delegation hardcoding.
- Still open: 2 (see below), 4, 5, 8 (partly), 9, 10.
  - 2: `test-first` and the bundled copies in `implement` and `divide-and-conquer` still require the user to confirm seams, which blocks background implementers. `test-first` and `review-and-refactor` still write working state and the changelog with no caller check. `divide-and-conquer` step 9 has an implementer subagent edit and commit after review, while `review-and-refactor` says the coordinating agent edits and leaves changes uncommitted.
  - 4: `triage` still says to run tests or commands on an external pull request. `improve-skills` still tells the agent to use the git credential helper's stored credential.
  - 5: `debug` still ships an interactive human-in-the-loop script. The `improve-codebase-architecture` report still loads Tailwind and Mermaid from CDNs. `improve-environment` and `improve-skills` still read "local agent logs" with no format.
  - 8, remaining: "Token Monitor" in `monitor-ai-tooling` and `setup-ai-tooling/TOOLS.md`; Biome settings in `setup-git-hooks` (`lineWidth 160`, `useSortedKeys`, the Biome 1.x `organizeImports` key); `delta-action: land` in `sync-tree`.
  - 9: `memorize` still fuses lesson routing and the scriptbook.
  - 10: `guide` still restates workflow bodies and carries a catalogue of skills.
  - Also: spaced hyphens in `teach/SKILL.md` (lines 9, 16, 18, 74, 80, 96, 109, 115) were not fixed because the user's ruling on 7 covered abbreviations only.

## Decisions

- Agent-agnostic setup: a setup skill names no harness. It finds harness details (steering file, hook or permission format, model list) from the harness's own documentation at run time, with a portable fallback. The user stated this twice (guardrails, then delegation).
- Guard level is the user's choice, asked in the first round with a recommendation of level 2.
- Delegation setup offers Configure, Reconfigure, Remove, or Skip per detected harness and lets the user pick among models that harness actually lists. This was the user's suggestion ("not sure"); the user has not yet exercised it.
- Detection is a bundled script plus a confirmation question, not a hardcoded list. Each skill carries its own copy of the script so it works installed alone, and a test keeps the copies identical.
- `AUDIT.md` was not updated with a follow-up section for this session. Decide with the user whether to add one.

## Next

1. Confirm with the user which open priority to take next (2 is the one they asked about first).
2. Priority 2: make seam confirmation conditional on an interactive session (or settle seams in the routing-table approval of `divide-and-conquer`), add a caller check for records ownership in `test-first` and `review-and-refactor`, and settle who edits after review.
3. Reconcile with `documentation/architecture-decision-record/0005-make-skills-autonomous.md`, which plans to fold the git guardrails into `codify` and retire the delegation setup. The work above changes skills that decision touches.
4. Try the two rewritten setup skills in a real session, in at least two harnesses, and correct what they get wrong.

## Open questions

- Should `AUDIT.md` get a follow-up section for this session, as it has for 2026-10-07? The user decides.
- Does the user want the spaced hyphens in `teach/SKILL.md` fixed now?
- Does the 0005 plan to absorb the guardrails into `codify` still stand, given the guardrails skill was just rewritten?

## Sources

- `AUDIT.md`, section "Priority problems".
- `documentation/architecture-decision-record/0005-make-skills-autonomous.md`.
- `skills/setup/setup-git-guardrails/SKILL.md`, `skills/setup/setup-git-guardrails/scripts/`, `skills/setup/setup-git-guardrails/EXAMPLES.md`.
- `skills/setup/setup-delegation-policy/SKILL.md`, `skills/setup/setup-delegation-policy/TIER-AGENTS.md`, `skills/setup/setup-delegation-policy/scripts/detect-harnesses.py`.
- Tests: `scripts/test-guard-git.py`, `scripts/test-detect-harnesses.py`.
- Previous handoffs on adjacent work: `.agents/handoffs/2026-10-08-1112-autonomous-skills.md`, `.agents/handoffs/2026-10-08-1406-remove-classify-skill.md`.
