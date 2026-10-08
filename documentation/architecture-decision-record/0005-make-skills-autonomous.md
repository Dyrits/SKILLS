# Make skills autonomous and connect workflows through project artifacts

Status: accepted; implementation is incomplete.

This supersedes [0004: Skills know each other only by contract](./0004-skills-know-each-other-only-by-contract.md). It supersedes the central documentation-skill ownership in [0002](./0002-share-project-documents-across-workflows.md) and [0003](./0003-group-specifications-by-capability.md), not their shared project-document model or capability-based organization. Earlier records remain as history.

## Context

Contract-based calls reduced duplication inside this collection but made a skill depend on other installed skills to complete its advertised task. Centralizing document formats and path resolution in `document` also made ordinary artifact writing depend on a coordinator. We prefer independently installable skills, accepting the maintenance cost of bundled reference copies.

## Decisions

### Standalone skills, shared project records

Every skill must complete its advertised task when installed alone. It carries the instructions, references, templates, and artifact-writing rules it needs. It neither requires another skill nor suggests another skill as the next step. Workflows connect through discoverable project artifacts, not invocation chains.

Skills reuse the project's existing authoritative documents and respect its steering files and conventions. Autonomy does not justify competing specifications, conventions, or task lists. A skill that creates a record supplies its discovery pointer itself.

Bundle local copies of reusable disciplines where necessary. Preserve the established grilling method when renaming `interview` to `brainstorm`; do not broaden its behavior merely to match the new name. Skills needing that method can carry a reference copy. Keeping copies aligned is repository maintenance, not an installation-time dependency.

Remove `document` after redistributing its useful formats and guidance. Do not recreate the same mandatory dependency through `write-for-agents`.

### Documentation and discovery

`documentation/` serves humans and agents. `.agents/` and `AGENTS.md` serve agents only; `README.md` primarily serves humans. New shared documentation receives a concise discovery line in both `AGENTS.md` and the appropriate `README.md`. Agent-only records receive an `AGENTS.md` pointer without exposing their internal details in the human README.

Keep the shared document authority and capability-based organization from earlier records. Each skill carries enough of the relevant artifact contract to use it without a documentation coordinator. A skill finds the documents it reads through the project's `AGENTS.md`, naming the kind it needs (requirements, glossary, decision records) rather than a path another skill chose; a kind `AGENTS.md` does not name does not exist yet. A skill that creates a document uses its own default location only when `AGENTS.md` names none, and adds the document's line to `AGENTS.md`. (Added 2026-10-08 at the user's request.)

`hand-off` writes a self-contained handoff and updates the current-handoff pointer in `AGENTS.md`. The handoff itself says how to resume from it, so no reading skill is needed; `take-over` was removed on 2026-10-07 for that reason.

### Skill boundaries

- `setup-ai-workspace` focuses on project records, agent navigation, task tracking, and roles, not optional tool installation or machine configuration.
- `architect` covers high-level system architecture and technology-stack decisions: boundaries, responsibilities, data ownership and flows, integrations, deployment, alternatives, and tradeoffs. It can assess an existing system and conclude that its architecture should remain unchanged.
- `codify` covers conventions and their enforcement through formatters, linters, checks, hooks, and repository-level agent safety rules. It absorbs the useful behavior of `setup-git-hooks` and `setup-git-guardrails`. Machine-wide changes require separate authorization. Architecture choices belong to `architect`; rules for building consistently within those choices belong to `codify`.
- `reconcile` combines rebase initiation and resolution of an operation already in progress, including merge and cherry-pick conflicts. Preserve intent-based resolution, recovery records, verification, and separate publication approval.
- `brainstorm` replaces `interview` while preserving its proven questioning method.
- `script` replaces the broad `memorize` skill with a focus on finding, reusing, creating, verifying, and indexing reusable automation. Other skills own recording the lessons and decisions relevant to their tasks.

### Reuse before custom automation

Before writing a helper, check existing project automation, standard libraries, installed tools and dependencies, official service clients, and suitable maintained external libraries. Use a verified command recipe or small adapter where possible; write new logic only for the remaining gap. Assess compatibility, maintenance, licensing, security, and dependency cost.

This is not a mandate to adopt a particular shell framework or Python library. Standard-library code is preferable when sufficient. Token savings from a scriptbook are possible but unmeasured here; repeatability and avoiding reinvention are the supported reasons for it.

### Tooling is separate from skill orchestration

Move deterministic installation toward selectable, repeatable tooling rather than an agent-driven setup skill. Investigate existing installers before building a repository-specific CLI. APM is a candidate for skills and MCP installation and updates, not an adopted dependency or a verified solution for every native tool.

Retire advisory delegation-policy setup as a general-purpose skill. Classifier-based model routing is deferred, not authorized for implementation. Classification and enforcement are different responsibilities; a hook that supplies advice is not reliable model routing. Follow-up questions and research sources live in [the deferred tooling record](../../.agents/deferred-tooling.md).

### Evaluation pause

Repository-owned per-skill evaluations are paused and their `evals/` trees removed. Keep ordinary script tests, manifest validation, link checks, and generated-graph consistency checks. Installed third-party evaluation tooling and historical reports remain. Do not claim behavioral improvement from checks that only validate structure.

## Alternatives and consequences

We rejected keeping mandatory contract-based calls, retaining `document` as a shared coordinator, and replacing required dependencies with next-skill suggestions. All would keep another skill in the completion path or prescribe a workflow instead of leaving reusable project state.

Bundled references can drift and increase package size. Review and maintenance must keep the intended contracts compatible without making standalone installation depend on another skill. Existing project artifacts remain authoritative; this decision does not authorize silently relocating or rewriting them.

Acceptance records the target architecture, not completion of the migration. Renames, removals, local references, documentation pages, catalog entries, the router, and graph inputs must be synchronized as implementation proceeds. Installer selection and model-routing implementation remain deferred.
