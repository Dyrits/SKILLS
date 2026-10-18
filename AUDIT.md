# Skill audit

Date: 2026-10-18. Scope: the 42 skills under `skills/`, read from their current files at commit `a808c6b` plus the uncommitted deletion of the previous audit.

Method: four read-only reviewers (one per group of buckets) each read every `SKILL.md`, `apm.yml`, `agents/openai.yaml`, support file, and documentation page, and judged them against the rules in `AGENTS.md`. The reviewers were told not to read any earlier audit, exploratory note, or handoff. `scripts/check-skills.py` passes. Findings are the reviewers' reports; the ones marked **checked** were re-verified by hand against the files while assembling this document, the rest are unverified.

Criteria: usefulness (does it supply a capability, state, or action the agent lacks), description (model-facing, specific, no trigger collisions), standalone (no skill calls, no next-skill hand-offs, artifacts found through `AGENTS.md`), portability (no rule only this repository follows), correctness, writing rules, safety, and consistency of manifest, documentation page, and README.

## Status

Updated 2026-10-18. Priorities 1 to 6 and the smaller defects were fixed in commit `0b019dd` (the `apm.yml` item was no defect). The user then decided:

- `optimize-process` stays, trimmed to its impact-estimating rules; `re-explain` stays as it is.
- `improve-skills` and `improve-environment` stay separate: different audiences and triggers, and the drift check now guards their shared files.
- `work-in-tree` and `sync-tree` stay separate; `work-in-tree` now records the return destination in the worktree's Git directory, and `sync-tree` reads it.

Still open: trimming `illustrate` and `unslop`, the `iterate` router question, `research`, the generic "Trim" verdicts, and the three differently named copies of the conflict procedure.

## Verdicts

| Skill | Bucket | Usefulness | Verdict |
| --- | --- | --- | --- |
| setup | getting-started | High | Fix |
| setup-delegation-policy | getting-started | High | Keep |
| graphify | shaping | Medium-high | Fix |
| research | shaping | Low-medium | Trim |
| prototype | shaping | Medium | Fix |
| prioritize | shaping | Medium | Fix |
| interview | shaping | Medium | Keep |
| design-workflow | productivity | Medium | Keep |
| hand-off | productivity | High | Keep |
| illustrate | productivity | Low-medium | Trim |
| memorize | productivity | High (scripts, recall) | Trim |
| optimize-process | productivity | Low | Remove or merge |
| publish-message | productivity | High | Fix |
| re-explain | productivity | Low | Trim or remove |
| swarm | productivity | High | Keep |
| teach | productivity | High | Fix |
| unslop | productivity | Medium | Trim |
| walk-through | productivity | High | Keep |
| write-for-agents | productivity | Medium | Fix |
| triage | upkeep | High | Fix |
| debug | upkeep | High | Trim |
| codify | upkeep | Medium-high | Trim |
| improve-codebase-architecture | upkeep | Medium | Fix |
| improve-skills | upkeep | Medium | Fix |
| improve-environment | upkeep | Medium-high | Fix, merge with improve-skills |
| monitor-ai-tooling | upkeep | Low-medium | Trim |
| rebase | version-control | High | Keep |
| resolve-merge-conflicts | version-control | Medium | Fix |
| sync-tree | version-control | Medium-high | Fix |
| work-in-tree | version-control | Medium | Trim or merge with sync-tree |
| delineate | workflow | Medium | Trim |
| architect | workflow | Medium | Keep |
| specify | workflow | Medium | Trim |
| engineer | workflow | Medium | Fix |
| taskify | workflow | Medium | Keep |
| implement | workflow | Medium | Fix |
| divide-and-conquer | workflow | High | Fix |
| test-first | workflow | Medium | Fix |
| review-and-refactor | workflow | High | Fix |
| verify | workflow | High | Keep |
| iterate | workflow | Medium | Trim |
| address-feedback | workflow | High | Keep |

## Priority problems

1. **Credential use without designation (safety).** `skills/upkeep/improve-skills/SKILL.md:69` tells the agent to try every route to post an issue, including the credential that git's credential helper stores for `https://github.com`. The approval in the skill covers the issue text, not the credential. Checked. Remove the credential-helper route and name only routes the user has configured for the purpose.
2. **Skills that cannot run installed alone.** `setup` (`references/workspace.md` and the tracker and triage assets name `triage`, `taskify`, `graphify` and slash commands), `graphify` (hard stop without a tracker, `SKILL.md:30` names `taskify` and `prioritize` as next steps), `triage` (hard stop without tracker configuration, reads `documentation/out-of-scope/` by a fixed path), `specify` (names the capability blueprint and a separate prototype), `implement`, `iterate` and `divide-and-conquer` (the `webapp-testing` skill is named in `skills/workflow/implement/SKILL.md:16` and the two bundled `references/implement.md:13`; checked). Give each a local fallback, find homes through `AGENTS.md`, and drop the skill-name hand-offs.
3. **Seams are never delivered to the implementers.** `engineer` writes a blueprint with test seams, but `implement`, `test-first` and `divide-and-conquer` never read it, and `test-first` requires the user to confirm seams, which subagents and non-interactive runs cannot do. Have `implement` read the blueprint when `AGENTS.md` names one, and give `test-first` a no-user path that records the assumed seams and proceeds.
4. **Product and author specifics in shipped skills.** `sync-tree` (`SKILL.md:4-5,14-16`, a Delta "Land Changes" button and `delta-action` metadata), `monitor-ai-tooling` (RTK, Token Monitor, CodeGraph), `improve-skills` (hardcoded `Dyrits/SKILLS`), `divide-and-conquer/references/routing.md:14-19` (the author's model-name table), `publish-message/SKILL.md:52` (this repository's full-words rule), `write-for-agents/references/skill-mechanics.md:9-13` (repository conventions stated as general rules), `re-explain` (a personal controlled-language preference). Move each behind a "when present" condition or a project steering-file deferral.
5. **Unmanaged copies.** The bundling policy copies the same files into many skills with no check that they stay equal. Checked: `project-documents.md` has one hash across 14 skills, `interview.md` one hash across 11. `memorize` carries copies of the glossary, decision record, conventions, project documents, and wizard template. Three diverging copies of the conflict procedure exist (`resolve-merge-conflicts`, `rebase/references/resolve.md`, `sync-tree/references/rebase.md`). `graphify` and `prototype` hold near-duplicate `logic.md` and `ui.md` that already differ at one line each. Add a drift check to `scripts/check-skills.py` that compares each copy with its named original.
6. **Trigger collisions.** `graphify`, `prioritize`, `interview` ("too big, unclear", "break down an idea"); `engineer`, `architect`, `improve-codebase-architecture` (deepening, "more testable"); `delineate`, `specify`, `iterate` (all own term disputes); `review-and-refactor` against the built-in review skills; `address-feedback` against `publish-message`; `debug` ("broken, failing, slow") against `test-first` and `resolve-merge-conflicts`. Narrow each description so one skill owns each trigger.
7. **Judgement-only skills.** `optimize-process` and `re-explain` add little the agent cannot do unaided, and `illustrate` and `unslop` are mostly checklists the agent half-knows. `AGENTS.md` says not to ship such a skill. Remove or merge the first two, and trim the other two to what the agent cannot do unaided (the HTML report path in `illustrate`, the AI-specific tells in `unslop`).

## Smaller defects

Each is a single edit.

- `skills/workflow/test-first/agents/openai.yaml:3` says "Test-driven red-green-refactor" while the skill excludes refactoring. Checked.
- `skills/version-control/sync-tree/SKILL.md:125` says `rebase` resumes from the commit; the rebase there is a bundled copy, not the `rebase` skill. Checked.
- `skills/productivity/memorize/references/project-documents.md:36` links to a "requirements format" the skill does not bundle. Checked. `assets/template.sh:4` says "Generated by the /walk-through skill".
- `skills/version-control/README.md:3` still says "merge requests" after `draft-merge-request` was removed. Checked.
- `skills/productivity/teach/SKILL.md:13` and its documentation page still describe `*-FORMAT.md` files beside `SKILL.md`; the files are `references/*-format.md`, and `references/glossary-format.md` is never linked.
- `skills/upkeep/debug/assets/hitl-loop.template.sh:21` uses `read -r -p`, which stops without a terminal, and does not say the user must run it. The heading and `agents/openai.yaml` name it "Diagnosing Bugs", not `debug`.
- `resolve-merge-conflicts` lists cherry-pick but never says how to finish one; it has no H1 or completion criterion. `implement` and `review-and-refactor` have no H1.
- `skills/shaping/prototype/SKILL.md:10` and `graphify/references/prototype.md:5` say "including during specify".
- `rebase` and `divide-and-conquer` assume subagents and give no fallback when the harness has none. `verify` mutates code for its failure checks; it should do so only inside the added worktree and say who commits the proof.
- Several `apm.yml` descriptions drop the "Use when" half, and `agents/openai.yaml` short descriptions end in a period in some skills and not others.
- The documentation pages for `review-and-refactor` (publish step) and `debug` ("calls" `implement`, which actually carries a copy) are out of date.

## Overlaps worth a decision

- `improve-skills` and `improve-environment` are one retrospective with two outputs and share most of their references. Merge, or split the shared core out.
- `work-in-tree` and `sync-tree` are the two halves of one worktree round trip, and the handoff between them is only a chat message. Merge, or persist the handoff.
- `iterate` bundles 21 references (13 of them copies of other skills) in a chain four files deep. Make it a thin router or cut the unused merge-request chain.
- `research` is a 14-line judgement skill beside the built-in research tools. Keep it only if the `AGENTS.md` placement rule is the point.

## Notes on trust

- Clean runs the reviewers reported: no em-dashes, no `CLAUDE.md` mentions outside literals, no unwanted `repo`, `doc`, `spec` or `ADR` abbreviations in `SKILL.md` files, every `SKILL.md` under 500 lines, every documentation page with the four required sections, no dead links in the workflow bucket.
- Not run by any reviewer: the skills against real tasks, and `claude plugin validate`. This audit reads files; it does not measure behavior.
