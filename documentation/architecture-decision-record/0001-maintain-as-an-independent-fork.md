# Maintain this repository as an independently rebranded fork of `mattpocock/skills`

Through commit `f85ffd7`, this repository was `mattpocock/skills` (distributed via [AI Hero](https://aihero.dev/skills)). Starting at `f85ffd7`, Dylan J. Gerrits began maintaining `github.com/Dyrits/SKILLS` as an independent fork rather than a tracked branch feeding changes back upstream: renaming the plugin and package identity (`mattpocock-skills` → `dyrits-skills`, marketplace `mattpocock` → `dyrits`), restructuring skills into semantic buckets (`workflow/`, `shaping/`, `upkeep/`, `getting-started/`, `productivity/`, `reference/`, `work-in-progress/`, `deprecated/`), and dropping the AI Hero site as a documentation and publication dependency in favour of `skills.sh` and this repository's own `README.md`.

## Why

Upstream's naming, bucket layout, and AI Hero coupling reflect Matt Pocock's own publication needs, not this fork's. Diverging cleanly, once, at a known commit, is cheaper than carrying local patches against a moving upstream target across every rename and reorganization. Architecturally the two repositories now disagree on skill location and identity, so quietly rebasing on upstream is not an option going forward; any future upstream skill worth adopting has to be ported in deliberately.

## Consequences

- Upstream architecture decision records that predate `f85ffd7` (numbered independently), and `CHANGELOG.md`, are archived at `.upstream/` rather than deleted, alongside the pre-existing `.upstream/changeset/` and `.upstream/out-of-scope/` archives. They describe decisions and history this fork inherited, not decisions it made, and are kept byte-for-byte as they read at the fork point: this fork's own terminology and structural rewrites do not apply there, even where an in-progress rewrite already touched a file in transit before this ADR was written.
- `documentation/architecture-decision-record/` restarts its own numbering at `0001` and records only decisions made in this fork going forward.
- Historical references to `mattpocock/skills` issues and pull requests inside `.upstream/CHANGELOG.md` are accurate history of the code this fork started from and are not rewritten to this fork's identity; troubleshooting notes elsewhere in maintained documentation that cite specific upstream issue numbers are likewise left as accurate history of the code this fork started from.
- Adopting an upstream change now means reading its diff and porting it deliberately, not merging or rebasing.

## What changed, `f85ffd7`..`b9e7f0a`

The full detail lives in `.agents/handoffs/2026-09-17-*-fork-rework-session-*.md` and the three commits themselves (`f85ffd7`, `a92b55c`, `b9e7f0a`); this is the summary an architectural reader needs:

- **Identity**: `mattpocock-skills`/`mattpocock` renamed to `dyrits-skills`/`dyrits` throughout `package.json`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and installation instructions; `npx skills@latest add Dyrits/SKILLS` is now the sole documented install route, with the plugin marketplace kept only as an undocumented fallback.
- **Bucket structure**: `skills/flow/` renamed to `skills/workflow/`, `skills/in-progress/` renamed to `skills/work-in-progress/`, with documentation, plugin manifest, scripts, and cross-references updated to match.
- **Upstream archival convention**: `.upstream/` holds material inherited from upstream that this fork does not edit going forward (`changeset/`, `out-of-scope/`, now `architecture-decision-record/`), distinct from `documentation/` and `documentation/out-of-scope/`, which this fork actively maintains.
- **Language conventions**: `CLAUDE.md` (symlinked from `AGENTS.md`) now prefers full words (`repository`, `documentation`, `specification`, `architecture decision record`) over abbreviations, and forbids em dashes repository-wide; changesets tooling was removed entirely, and the changeset-generated `CHANGELOG.md` it left behind was archived to `.upstream/CHANGELOG.md` rather than continued by hand.
- **Tracker flexibility**: `setup-custom-skills` and `to-tickets` gained support for GitHub, GitLab, Jira, and local-markdown trackers, with an optional pluggable ticket-writing convention, rather than assuming GitHub issues.
- **Dependency removal**: the AI Hero website is no longer a documentation or publication dependency; `skills/reference/codebase-design`'s `setup-ts-deep-modules` companion was removed rather than ported.
