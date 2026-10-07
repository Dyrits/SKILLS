This audit distinguishes skills derived from `mattpocock/skills`, skills adapted from other projects, and skills created in this fork. It covers the 47 current `skills/*/*/SKILL.md` entrypoints, including 15 outside the plugin. It does not treat the archived upstream inventory as the current inventory.

## What it does

The audit uses retained Git history through fork commit `b05ce86`, the pinned upstream revision `d81f3a183412e71a5b1e84ca21bc1a35eea03a60`, the `.upstream/` archive guide and content-port record (removed on 2026-10-08), and original external source files. Current names and purpose buckets include the concurrent working-tree renames. These are not all committed at the audit baseline.

For existing tracked paths, `git log --follow -- <path>` traces renames. For pending renames and bucket moves, the committed predecessor is the starting point. First-add commits, their source text, and contemporaneous handoffs distinguish new content from rewritten imports. An addition in Git's rename detection, or absence from the `d81f3a1` tree, does not by itself prove fork authorship.

In the tables, historical paths identify `SKILL.md` unless another filename is specified. Commit links point to retained primary history. "Matt-derived" means inherited through `mattpocock/skills`, not a claim that Matt personally authored every line or all underlying ideas. Promotion is the intended current 32-path plugin set, not membership in a particular bucket. Pending manifest references were being corrected by the parent thread during this audit.

### Matt-derived retained skills

| Current skill | Plugin | Original source and primary evidence |
| --- | --- | --- |
| `setup-ai-workspace` | Yes | `setup-matt-pocock-skills`, `d81f3a1:skills/engineering/setup-matt-pocock-skills/`. Fork renames in `f85ffd7`, then [85d4634](https://github.com/Dyrits/SKILLS/commit/85d4634). |
| `guide` | Yes | `ask-matt`, `d81f3a1:skills/engineering/ask-matt/`; router rename to `what-is-next` in [f85ffd7](https://github.com/Dyrits/SKILLS/commit/f85ffd7), then to `guide`. |
| `setup-git-guardrails` | No | `git-guardrails-claude-code`, `d81f3a1:skills/misc/git-guardrails-claude-code/`. `f85ffd7` rewrote the entrypoint and moved its bundled script byte for byte. Its session handoff explicitly records the rename and multi-agent expansion. |
| `setup-git-hooks` | No | `setup-pre-commit`, `d81f3a1:skills/misc/setup-pre-commit/`. `f85ffd7` session handoff explicitly records the rename and replacement of Husky with `core.hooksPath`, Biome-first formatting, and a typecheck/build gate. Rewritten content is an adaptation, not an unrelated new skill. |
| `ask-someone-else` | Yes | `to-questionnaire`, `d81f3a1:skills/productivity/to-questionnaire/`; rename recorded in `f85ffd7`. |
| `hand-off` | Yes | `handoff`, `d81f3a1:skills/productivity/handoff/`; versioned handoff expansion in `f85ffd7`, current name in [b9e7f0a](https://github.com/Dyrits/SKILLS/commit/b9e7f0a). |
| `teach` | Yes | `teach`, `d81f3a1:skills/productivity/teach/`; retained `git log --follow` reaches `fadf11d`, the initial `/teach` addition. |
| `re-explain` | Yes | `wait-what`, `d81f3a1:skills/productivity/wait-what/`; current working-tree rename retains the fork's language and missing-glossary fallback. |
| `design-modules` | Yes | `codebase-design`, `d81f3a1:skills/engineering/codebase-design/`; renamed `design-modules` in this fork; moved to reference in `f85ffd7`. |
| `model-domain` | Yes | `domain-modeling`, `d81f3a1:skills/engineering/domain-modeling/`; renamed `model-domain` in this fork; moved in `f85ffd7`, glossary changes ported in [dd44788](https://github.com/Dyrits/SKILLS/commit/dd44788). |
| `refine` | Yes | `grilling` plus `grill-me`, `d81f3a1:skills/productivity/grilling/` and `skills/productivity/grill-me/`. Current merge combines the discipline and its human-invoked wrapper. It does not create two retained skills or preserve those names as active aliases. |
| `walk-through` | Yes | `wizard`, `d81f3a1:skills/engineering/wizard/`; moved in `f85ffd7`, renamed `walk-through` in this fork; earlier history reaches `850873c`. |
| `write-for-agents` | Yes | `writing-for-agents`, earlier `writing-great-skills`; renamed `write-for-agents` in this fork. `d81f3a1:skills/productivity/writing-for-agents/`; upstream rename recorded in `1fc6573` and `17f22a3`. |
| `prototype` | Yes | `prototype`, `d81f3a1:skills/engineering/prototype/`, including `LOGIC.md` and `UI.md`; moved in `f85ffd7`. |
| `research` | Yes | `research`, `d81f3a1:skills/engineering/research/`; first-add history `0d74d01`, moved in `f85ffd7`. |
| `graphify` | Yes | `wayfinder`, `d81f3a1:skills/engineering/wayfinder/`; current rename names its decision graph, not a generic visual explanation tool. |
| `debug` | Yes | `diagnosing-bugs`, `d81f3a1:skills/engineering/diagnosing-bugs/`; earlier history includes `diagnose` in `e7f0b58`. Fork rename in `b9e7f0a`. |
| `improve-agent-environment` | Yes | `retro`, `d81f3a1:skills/engineering/retro/`; initial addition `8fa1886`, fork rename `b9e7f0a`, promotion retained in the `dd44788` port. |
| `improve-codebase-architecture` | Yes | Same upstream name, `d81f3a1:skills/engineering/improve-codebase-architecture/`; moved in `f85ffd7`. |
| `resolve-merge-conflicts` | Yes | `resolving-merge-conflicts`, `skills/engineering/resolving-merge-conflicts/` before upstream removal [daa01d8](https://github.com/mattpocock/skills/commit/daa01d8). Upstream kept `d81f3a1:docs/engineering/resolving-merge-conflicts.md` as an archive. Fork history follows the source back to `81ddacb`; this was retained, not recreated from a missing tip entry. |
| `triage` | Yes | `triage`, earlier `github-triage`; `d81f3a1:skills/engineering/triage/`, rename history `7afa86d`, moved in `f85ffd7`. |
| `review-and-refactor` | Yes | `code-review`, `d81f3a1:skills/engineering/code-review/`; fork [3b01417](https://github.com/Dyrits/SKILLS/commit/3b01417) renamed it `code-review-and-refactor`, later `review-and-refactor`, and added supported refactoring plus reviewer verification. |
| `design-workflow` | Yes | `loop-me`, `d81f3a1:skills/in-progress/loop-me/`; fork rename in `b9e7f0a`. |
| `implement` | Yes | `implement`, `d81f3a1:skills/engineering/implement/`; history reaches initial implementation documentation `ffb2fa6`. |
| `implement-all` | Yes | `implement-spec`, `d81f3a1:skills/engineering/implement-spec/`, previously `in-progress/implement-spec/`; fork rename in `f85ffd7`, later integration-branch behavior ported in `dd44788`. |
| `specify` | Yes | `grill-with-docs` and `to-spec`, `d81f3a1:skills/engineering/grill-with-docs/` and `skills/engineering/to-spec/`. Earlier `to-prd` is explicitly confirmed by `d81f3a1:docs/engineering/to-spec.md`, under "Where did /to-prd go?". Current merge combines resolving outstanding decisions with synthesizing settled context. |
| `taskify` | Yes | `to-tickets`, `d81f3a1:skills/engineering/to-tickets/`; current rename preserves the task-slicing role. |
| `test-first` | Yes | `tdd`, `d81f3a1:skills/engineering/tdd/`; fork rename to `test-driven-development` in `b9e7f0a`, then to `test-first`, maintained test references ported in `dd44788`. |
| `draft-merge-request` | Yes | `pr`, `d81f3a1:skills/engineering/pr/`; fork port [0a807ae](https://github.com/Dyrits/SKILLS/commit/0a807ae) as `to-pull-request`, now `draft-merge-request`. Its visual material also had external credit, and later delegates to the separately adopted HumanLayer skill. This is not evidence that HumanLayer originated the whole `pr` skill. |

### Other external sources

| Current skill | Plugin | Source and adoption evidence |
| --- | --- | --- |
| `illustrate` | Yes | HumanLayer [`show-me`](https://github.com/humanlayer/skills/tree/main/plugins/show-me/skills/show-me), adopted as `skills/productivity/show-me/` in [c9ed16e](https://github.com/Dyrits/SKILLS/commit/c9ed16e), now renamed. The original raw `SKILL.md` was fetched successfully during this audit and contains the same visual-format family. It is not a Matt-derived skill. |
| `unslop` | Yes | Cursor pstack [`unslop`](https://github.com/cursor/plugins/tree/main/pstack/skills/unslop), adopted in [6585eba](https://github.com/Dyrits/SKILLS/commit/6585eba). The `c9ed16e` handoff records verification of this exact source URL. Live raw source was fetched successfully. Fork changes include model invocation, multilingual editing in `7c7e38e`, and removal of stable rule numbers in `8beeace`. |
| `document` | Yes | Renamed from `documentation`. Anthropic knowledge-work-plugins [`engineering/skills/documentation/SKILL.md` at `1bd42820da111e5f0206e570bf5228a1c35839c7`](https://github.com/anthropics/knowledge-work-plugins/blob/1bd42820da111e5f0206e570bf5228a1c35839c7/engineering/skills/documentation/SKILL.md), adapted in `6585eba`. Its handoff names the project, exact revision, copied Apache 2.0 license, and adaptations. Fetching the pinned original succeeded. The shared project-document model is a later fork extension, not proof that the original skill was fork-created. |

### Fork-created skills

These classifications have positive first-add and session evidence, rather than relying only on absence from an upstream tree. They describe creation in the retained fork record, not a proof that no similar instructions ever existed elsewhere.

| Current skill | Plugin | First-add evidence and scope |
| --- | --- | --- |
| `setup-auto-handoff` | No | `f85ffd7` adds the entrypoint and compaction-gate script. `.agents/handoffs/2026-09-17-0010-fork-rework-session-1.md` calls it new and separately records deleting `claude-handoff`. The latter launches a background agent with a summary; it is not this fresh-file compaction gate. |
| `take-over` | Yes | `f85ffd7` adds `skills/productivity/takeover/`; the same session handoff explicitly calls it new. `b9e7f0a` renames it to `take-over`, so that later commit is not its creation date. |
| `optimize-process` | Yes | [26542d8](https://github.com/Dyrits/SKILLS/commit/26542d8) adds `skills/productivity/optimize-process/SKILL.md`, for recurring human and agent processes. |
| `address-feedback` | No | [35b08c5](https://github.com/Dyrits/SKILLS/commit/35b08c5) adds `skills/experimental/address-feedback/SKILL.md` and its session handoff. |
| `publish-message` | No | [363809a](https://github.com/Dyrits/SKILLS/commit/363809a) adds `skills/experimental/publish-message/SKILL.md` alongside `publish-review`. `c9ed16e` later consolidates review publication into this retained skill and deletes the other entrypoint. |
| `classify` | No | [b7f83f1](https://github.com/Dyrits/SKILLS/commit/b7f83f1) explicitly turns the fork's ad hoc OpenCode router into `classify` and `route`. It adds `skills/experimental/classify/SKILL.md` as the transport and API-semantics owner. classifier.dev is the third-party service, not evidence of an imported classifier.dev skill. No external skill origin is established by the retained record. |
| `setup-delegation-policy` | No | [ed43af2](https://github.com/Dyrits/SKILLS/commit/ed43af2) deletes fork-created classifier routing entrypoints and adds `skills/experimental/setup-delegation-policy/SKILL.md`. Its commit explains the change to a standing multi-harness delegation policy. |
| `setup-ai-tooling` | No | [1394bed](https://github.com/Dyrits/SKILLS/commit/1394bed) adds `skills/experimental/setup-ai-tooling/SKILL.md`, tooling references, and a session handoff. Third-party tools it installs are not the source of this workflow. |
| `monitor-ai-tooling` | No | `1394bed` adds `skills/experimental/monitor-ai-tooling/SKILL.md` and measurement/report references. |
| `work-in-tree` | No | [0839ff5](https://github.com/Dyrits/SKILLS/commit/0839ff5) adds `skills/experimental/work-in-tree/SKILL.md` and the worktree session handoff. |
| `sync-tree` | No | `0839ff5` adds `skills/experimental/sync-tree/SKILL.md`, distinct from setup and worktree entry. |
| `memorize` | No | Fork-created. Absorbs `scriptbook`, which [4456e95](https://github.com/Dyrits/SKILLS/commit/4456e95) added as `skills/experimental/scriptbook/SKILL.md` with the reuse-scripts handoff; its steps live on in `SCRIPTS.md`. |
| `rebase` | No | [a3792dd](https://github.com/Dyrits/SKILLS/commit/a3792dd) adds `skills/experimental/rebase/SKILL.md`, `BRANCH.md`, and `RESUME.md`, with an in-place rebase session handoff. |
| `iterate` | No | [b05ce86](https://github.com/Dyrits/SKILLS/commit/b05ce86) adds `skills/experimental/iterate/SKILL.md`, artifact rules, and milestone-review instructions. |
| `prioritize` | No | Named `divide-and-conquer` until its rename. `b05ce86` adds `skills/experimental/divide-and-conquer/SKILL.md` and records it with `iterate` in the same session handoff. |

Totals are 29 Matt-derived, three other external adaptations, and 15 fork-created skills. Of the 15 non-plugin skills, two are Matt-derived and 13 are fork-created. Moving the 12 former experimental skills into purpose buckets does not promote them.

## When to reach for it

Use this report when changing credits, provenance paragraphs, migration explanations, or the retained-skill inventory. The primary history can be inspected without importing newer upstream content:

```sh
git show d81f3a1:skills/engineering/to-spec/SKILL.md
git show d81f3a1:docs/engineering/to-spec.md
git log --follow -- skills/getting-started/setup-auto-handoff/SKILL.md
git log --follow -- skills/experimental/classify/SKILL.md
git show f85ffd7:.agents/handoffs/2026-09-17-0010-fork-rework-session-1.md
git show 6585eba:.agents/handoffs/2026-09-23-1220-unslop-and-documentation-skills.md
```

The older `.upstream/` archives and the `d81f3a1` snapshot are frozen evidence, not instructions for today's fork. The [independent-fork decision](../architecture-decision-record/0001-maintain-as-an-independent-fork.md) and the port record explain why upstream ancestry does not imply adoption of every upstream file.

## Common questions

**Why is the current document model different from the archived pages?**

Archived `to-spec` publishes its specification as an issue and requires tracker setup. The current fork has a shared contract in [the document skill's source](../../skills/reference/document/SKILL.md). Relevant requirements remain constraints, the canonical living feature specification stays local, and remote task bodies remain authoritative when published. Local task documents then hold titles and links rather than duplicate remote bodies.

Current [setup templates](../../skills/getting-started/setup-ai-workspace/refinement.md) and [iterate artifact rules](../../skills/workflow/iterate/ARTIFACTS.md) apply that contract. For remote projects, the local backlog contains the tracker backlog pointer rather than copied priorities or status. Working and resumption state stays local. Just-in-time `iterate` does not require generating feature specifications or tasks before each batch; it still respects existing relevant requirements and approved scope. These are current fork decisions, not assertions about the frozen upstream release.

The current `specify` merge removes the artificial handoff between interviewing and synthesis while allowing settled context to skip repeat questions. General `refine` need not produce a software specification. The parent thread owns the detailed behavior and caller updates; this audit records provenance rather than rewriting those instructions.

**Should removed upstream skills be restored to make the inventory complete?**

No. The inventory is the retained current entrypoints, not every archived skill. `f85ffd7` explicitly deleted `claude-handoff` and `scaffold-exercises`; `b9e7f0a` removed `setup-ts-deep-modules`; [84d3479](https://github.com/Dyrits/SKILLS/commit/84d3479) archived pristine material and removed work-in-progress writing skills. These are examples of deliberate absence, not missing inventory rows. `publish-review`, `route`/`dispatch`, and `setup-routing-for-claude` also remain historical predecessors rather than active skills.

`resolve-merge-conflicts` is a different case. The fork had already retained and expanded the original before the `d81f3a1` port. The port record explicitly preserves that decision even though upstream removed the entrypoint. Its existence does not authorize restoring other removed skills.

**Which current page corrections were necessary?**

Only two first provenance paragraphs required factual correction during this audit. `documentation` was incorrectly labeled fork-added instead of adapted from Anthropic's skill. `take-over` attributed addition to `b9e7f0a`, which actually renamed the skill first added in `f85ffd7`. Other existing provenance paragraphs correctly identify the retained original names or external projects at the time inspected. No page body, source skill, manifest, listing, router, or historical file was changed by this audit.

**What remains unverified?**

This is a pinned archive and retained-history audit, not a survey of the latest live `mattpocock/skills` repository. It does not claim current upstream still contains all historical skills or uses these names. The HumanLayer and Cursor live files confirm the supplied projects and original skill names, but their adoption-time upstream commit hashes are not recorded in the inspected evidence. Their fork adoption hashes are known. Anthropic's source is pinned to an exact upstream commit.

No external original for `classify` is established; the positive local creation record is sufficient to classify the retained workflow as fork-created within this audit's scope. Absolute originality outside this history is not asserted for any fork-created skill. Similarity to a service or a tool name is not authorship evidence.

## It's working if

- Every current `skills/*/*/SKILL.md` has exactly one row, including all non-plugin skills.
- Credits distinguish Matt-derived workflows, HumanLayer, Cursor, Anthropic, and fork-created content.
- Renames and merged wrappers identify their historical originals without advertising removed names as active aliases.
- A rewritten import is not called a new fork creation merely because Git reports an added entrypoint.
- Archived removed skills remain evidence only, with no restored discovery entrypoints.
- Page corrections are limited to factual provenance, and unresolved source details stay explicit.
