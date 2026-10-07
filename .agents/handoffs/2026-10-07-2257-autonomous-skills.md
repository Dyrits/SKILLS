# Handoff: autonomous skills

Supersedes: `2026-10-07-1828-skill-contracts-and-document-ownership.md`
Workspace: Dyrits/SKILLS, branch `main`

## Goal

Implement the accepted move from contract-based skill dependencies to standalone skills connected through discoverable project artifacts. Completion includes the approved catalog changes, bundled references, documentation, manifests, router, and generated graph agreeing with the new architecture.

## State

- Verified by file reads: `documentation/architecture-decision-record/0005-make-skills-autonomous.md` records the accepted direction and exact supersession scope. Earlier records retain their history and link to the replacement. `AGENTS.md` and `README.md` point to it.
- Verified by the session diff: repository-owned skill evaluation trees and their mandatory checker rules were removed. Third-party evaluation tooling and historical reports remain. No skill autonomy rewrite or catalog rename has been implemented.
- Verified this session: `python3 scripts/test-check-skills.py` passed 34 tests; `python3 scripts/check-skills.py` passed for 48 skills; `python3 scripts/build-skill-graph.py --check` reported the graph current. These validate structure, not standalone skill behavior.
- Verified by file reads: `.agents/deferred-tooling.md` records installer investigation and deferred classifier-based routing. Nothing was installed and no routing implementation was started.
- The user requested this handoff, a commit, and a push. At writing, those Git operations are pending; inspect Git history and remote state rather than assuming publication succeeded.

## Decisions

The authoritative decisions are in architecture decision record 0005, not the superseded handoff's dependency-based instructions. Read that record before implementation. Its approved scope includes `architect`, the expanded `codify`, `reconcile`, `brainstorm`, and `script`; documentation discovery; reuse-first automation; and the evaluation pause.

Library examples discussed during the session are candidates, not adopted dependencies. APM compatibility testing and classifier-driven routing remain deferred as recorded in `.agents/deferred-tooling.md`.

## Next

1. Read architecture decision record 0005 and inspect the current diff/history to establish what has landed. Treat its migration as unfinished; do not resume the superseded dependency or evaluation plan.
2. Inventory current skill calls, next-skill suggestions, cross-skill reference paths, and documentation contracts. Plan bounded migration batches that preserve behavior and standalone installation.
3. Implement the approved skill boundaries and catalog changes, redistributing required references before removing their current owners. Preserve the established grilling method in local reference copies.
4. Synchronize human documentation, plugin entries, bucket and root README entries, the router, and graph inputs. Regenerate the graph and run the repository checks and applicable script tests. Validate the plugin strictly when its manifest changes. Do not recreate per-skill evaluations.
5. Report remaining gaps explicitly. Keep installer and routing implementation out of the migration unless separately authorized.

## Open questions

- Which existing installer best supports this repository's layout and desired client coverage? APM documentation was reviewed, but compatibility was not tested.
- How should bundled reference copies be maintained without introducing installation-time dependencies? Choose a maintainable implementation consistent with the accepted autonomy rule.
- The exact home and detailed process for the new architecture skill remain to be designed within its approved high-level architecture and technology-stack scope.

## Sources

- `documentation/architecture-decision-record/0005-make-skills-autonomous.md`
- `.agents/deferred-tooling.md`
- `AGENTS.md`
- `scripts/check-skills.py`
- `scripts/test-check-skills.py`
- `scripts/skill-graph/flow.json`
- `.agents/handoffs/2026-10-07-1828-skill-contracts-and-document-ownership.md` (historical context, superseded direction)
