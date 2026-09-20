# Upstream sync, and the pr skill ported as to-pull-request

**Supersedes:** [2026-09-20-0959-tier-agents-across-harnesses.md](2026-09-20-0959-tier-agents-across-harnesses.md)

The previous handoff closed the delegation-policy work. This session did something unrelated to it: the first upstream synchronisation since the fork, driven by one goal, `origin/main` should never read as behind `upstream/main`.

Everything below is **committed and pushed to `main`** unless stated otherwise. Two commits: `0acda1b` (ours-merge) and `cfe880d` (the port, amended to carry this handoff). Their messages hold the detail; this document holds what the messages cannot.

## What upstream had

`mattpocock/skills` was ten commits ahead of the merge base `959a8e9`, and every one of them touched a single new skill, `skills/in-progress/pr`. Nothing upstream changed touched a file this fork maintains, so there were no conflicts and `/resolve-merge-conflicts` was never needed. The full delta was three paths: the skill, a changeset for it, and one line in a bucket `README.md` for a bucket this fork no longer has.

## Decisions settled this session

Do not relitigate these without new information.

- **Ancestry by ours-merge, adoption by deliberate port.** These are two separate commits on purpose. `git merge -s ours upstream/main` records the ancestor and changes no file; the port is its own commit that reads the diff. Architecture decision record 0001's Consequences now states this, replacing the bullet that said upstream is never merged at all. That bullet was written before anyone needed the branch comparison to read clean, and the repository was about to contradict it either way.
- **The `pr` skill was worth porting.** The user chose `workflow/`, promoted, over `reference/` or `experimental/`. The flow genuinely ended at a commit, so this fills a gap rather than adding a sibling.
- **Named `to-pull-request`**, matching `to-specifications` and `to-tickets`, full words per the repository's language rule. The body is neutral between a pull request and a merge request throughout, because this fork supports GitLab and Jira and upstream assumed GitHub.
- **Left model-invoked**, unlike the rest of the `to-*` family, which is user-invoked. `implement-all` opens a request during its run, and a body format only a human can fire is unreachable at the one moment it is wanted. The documentation page answers this question explicitly, because it looks like an inconsistency and is not.
- **Purpose comes from the primary source, not the diff.** Upstream's own proposal (issue #938) made this the skill's defining constraint and the shipped `SKILL.md` had lost it. Reinstated, in this fork's existing `primary source` vocabulary.
- **Attribution travels with the port.** The Summary shapes originate in Dex Horthy's `show-me`, copied in rather than depended on, so `CREDITS.md` sits beside the `SKILL.md`. This is the only `CREDITS.md` in the repository; it is deliberate, not a stray upstream file.
- **Upstream's changeset is archived, not dropped.** `.upstream/changeset/add-pr-skill.md`, byte-for-byte. Architecture decision record 0001 now says post-fork upstream material that is not ported goes there on the same terms as the fork-point archives.

## Facts established by inspection

- Upstream's component-tree example was **mangled by a formatter** into invalid JSX (`<SessionPage>(apps / example / src / routes / session.tsx);`). Rewritten as a plain annotated tree in a `text` block. If a future sync pulls that region again, it is still broken upstream.
- Upstream issues **#521, #938, #509, #915** are the skill's design history, read via the public GitHub API. #521 proposed a paired `/to-commit` that was never built, which is why `implement` still commits on one line of its own guidance. #915 is the request that this fork already answers with `experimental/address-feedback`. The documentation page's Common questions section is sourced from these, not invented.
- **`gh` is not installed on this machine.** `curl` against `api.github.com` worked unauthenticated for the four issue reads. Anything scripted against the tracker has to account for this.
- `claude plugin validate . --strict` validates **`marketplace.json` only** in this repository, never `plugin.json`, because the repository is its own marketplace. Manifest paths were checked separately in Python; all 29 resolve.

## Machine state, outside the repository

`scripts/link-skills.sh` was re-run to link the new skill. This **closed open item 4 of the superseded handoff** as a side effect: `~/.agents/skills` now holds 38 symlinks into this repository (plus 26 unrelated third-party skill directories), where the previous session found stale copies that `git pull` could not reach. `~/.claude/skills` holds 64 symlinks. The repository's edits now reach installed skills again, on both harnesses.

This was a machine-wide change, taken because the script is the repository's documented way to install a new skill and the previous session had flagged the copies as the wrong state, not as a state to preserve.

## Open, and why

1. **The skill has never been run.** It was ported, wired, and validated, never invoked against a real branch. The first real use is the test of whether the Summary shape menu produces something a reviewer wants, or a wall of diagrams.
2. **No `/to-commit` companion.** Upstream proposed the pair, so the commit message and the request body would interlock. Only the request half exists here. Worth deciding on its own merits rather than because upstream sketched it.
3. **No synchronisation cadence.** Nothing schedules the next ours-merge, and nothing watches upstream. Currently it happens when someone remembers.
4. Carried over and still open: the Codex CLI row in `setup-git-guardrails`, promotion criteria for experimental skills, and the Gemini and ZCode tier bindings that remain unverified end to end (see the superseded handoff for detail).

## Suggested skills

- `/writing-for-agents` before editing `skills/workflow/to-pull-request/SKILL.md`. It is model-invoked, so its `description` is always-loaded context and the body is all reference; both are the constrained resources.
- `/to-pull-request` itself, on the next branch that goes up for review. That is open item 1.
- `/code-review` against `3be4f78..HEAD` if the port wants a second pair of eyes.
