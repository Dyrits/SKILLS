# Promote every skill, generalize feedback and publication

Supersedes: [2026-10-03-2334-review-renames-and-memorize.md](./2026-10-03-2334-review-renames-and-memorize.md). Its pending list still applies except where noted below; its installed-copy warning has grown again.

## Resume here

This session made three changes, then committed and pushed them to `origin/main` on the user's request ("commit and push"). Check Git for the actual commit and push result; this handoff was written just before them.

1. `address-feedback` moved from `version-control/` to `workflow/` and now accepts feedback from any source: tracked (pull or merge request, issue, ticket, document comments) or untracked (pasted notes, file, email, chat, transcript). Only steps 1, 5, and 6 branch on the source kind.
2. `publish-message` moved from `version-control/` to `productivity/` and publishes to any connected service (code host, tracker, chat, documentation, email), adapting format, length, placement, mentions, and audience. Inline suggestions remain GitHub and GitLab only.
3. **Every skill outside `deprecated/` is now promoted** (user: "They are all to be promoted. There are no experimental skills anymore."). 47 skills, 47 manifest entries, 47 documentation pages. "Not in the plugin" sections and "separately installed" wording are gone everywhere active.

`version-control/` is now described as "branches, merge requests, and their history".

## Authoritative artifacts

- [CLAUDE.md](../../CLAUDE.md): the new promotion rule (four obligations per skill) and bucket descriptions.
- [scripts/check-skills.py](../../scripts/check-skills.py): now fails when a non-deprecated skill is missing from the manifest or a deprecated one is in it; tests in `scripts/test-check-skills.py`.
- [.agents/writing-documentation.md](../writing-documentation.md): non-plugin page rules removed.
- [README](../../README.md), bucket `README.md`s, and [guide](../../skills/getting-started/guide/SKILL.md): full listings.
- The 15 new pages under `documentation/skills/` (setup-ai-tooling, setup-auto-handoff, setup-delegation-policy, setup-git-guardrails, setup-git-hooks, classify, publish-message, memorize, prioritize, monitor-ai-tooling, rebase, sync-tree, work-in-tree, address-feedback, iterate), written by three Sonnet subagents. The coordinating agent spot-read four (setup-git-hooks, publish-message, iterate, rebase); the other eleven passed structural checks only. Upstream paths for setup-git-hooks and setup-git-guardrails were verified with `git cat-file` against `d81f3a1`.

## Verification and its limits

Passing before commit: `npm run check-skills`, `npm run test-skills-check` (11 tests), `npm run check-plugin-version`, `claude plugin validate . --strict`, `git diff --check`. No skill was executed; the rewritten `address-feedback` and `publish-message` have no runtime evidence. `skill-creator` evaluations were skipped, consistent with the user's earlier deferral.

## Pending, by owner

User:

- Re-run `scripts/link-skills.sh`; `address-feedback` and `publish-message` changed paths, on top of the earlier retired-name cleanup listed in the superseded handoff.

Asked, not yet answered:

- **Version bump.** Plugin is still `0.2.0` despite 15 newly promoted skills. Users with an installed plugin keep the old copy until the version changes. Recommended `0.3.0` (bump `package.json`, run `node scripts/sync-plugin-version.mjs`).
- **Invocation split.** User asked whether every skill could be both user- and model-invoked. Recommendation given: keep the distinction (context load of always-loaded descriptions, workflow entry points auto-firing, outward-facing actions), but flip seven to model-invoked: `re-explain`, `ask-someone-else`, `triage`, `design-workflow`, `work-in-tree`, `take-over`, `monitor-ai-tooling`. Each flip needs a model-facing description, the Codex `policy` removed from `agents/openai.yaml`, listing and page updates, and a check of which skills should now call it (for example `refine` calling `ask-someone-else`). See [.agents/invocation.md](../invocation.md).
- **Anthropic directory submission.** User asked how to publish to the Claude marketplace. The repository is already its own marketplace (`claude plugin marketplace add Dyrits/SKILLS`, then `claude plugin install dyrits-skills@dyrits`), undocumented by design per [.agents/install-block.md](../install-block.md). Public listing goes through the developer portal at https://claude.ai/directory/manage (paid plan, per-version review; `claude-plugins-official` takes no portal submissions). Offered preparation: bump version, replace the stale `code-review-and-refactor` keyword in `.claude-plugin/marketplace.json`, add `homepage` and `displayName` to `plugin.json`. A listing would add a second advertised install route, reversing the install-block decision; that needs README and install-block changes and ideally an architecture decision record. Sources: https://code.claude.com/docs/en/plugins/publish, https://claude.com/docs/plugins/submit.

Still open from the superseded handoff: `memorize` trigger fixes, the optional inline-script reminder hook, the `prioritize` many-small-items branch, the "README at boundaries" rule, and bounded evaluations of `iterate` and `prioritize`. (Whether to promote `memorize` is now settled: it is promoted.)

## Suggested skills and invocation modes

- Model-invoked, through the Skill tool: `write-for-agents` before editing any skill or instruction file; `memorize` before writing any script (read `.agents/scripts/INDEX.md`; `update-references.py` handles renames and moves); `document` for project-document rules; `skill-creator` if evaluations resume; `unslop` for prose.
- User-invoked, for the human to run: `/guide`, `/take-over`, `/hand-off`, `/publish-message`, `/address-feedback`.

Installed copies may lag the repository until the link refresh; check availability before claiming a moved skill is callable.

## Publication

Branch `main`, destination `origin/main` (`git@github.com:Dyrits/SKILLS.git`). Normal push only; no force, tag, version bump, or directory submission was authorized.
