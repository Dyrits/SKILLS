# Handoff: challenge decision reviews

Supersedes: none
Workspace: /Users/dgerrits/Codelab/Dyrits/SKILLS, branch `add-security-audit-skill`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Deliver a generic `challenge` skill that tests a user's choice, gives candid feedback, and helps establish whether its consequences are understood.
The user requested this shared handoff, a commit, and a push; the next session should establish publication status before any optional behavioral evaluation or revision.

## State

- Verified by file reads: `skills/productivity/challenge/` contains the instructions, decision review template, interface metadata, and APM manifest; its human documentation is `documentation/skills/productivity/challenge.md`.
- Verified by command output on 2026-10-28: `python3 scripts/check-skills.py` passes for the current working tree, `python3 .agents/scripts/generate-skill-manifests.py --check` reports 45 current manifests, and `git diff --check` passes.
- Verified by Git output: the current branch is `add-security-audit-skill`, tracking `origin/add-security-audit-skill`, with HEAD at `e543cdf` when this handoff was written.
- Verified by Git diff and status: unrelated review-history work and evaluation files coexist in the working tree, including changes to shared catalogue files; exclude them from this session's commit and preserve them locally.
- Assumed from the preceding session's tool results, not repeated for this handoff: local links were refreshed, manifest validation passed with directory warnings, and APM packaging succeeded with collection-wide warnings.
- Conversational behavior has not been evaluated; static checks establish packaging consistency, not improved decision quality.
- Commit and push are authorized but still pending at writing time; inspect Git history and the remote branch to determine their final result.

## Decisions

- Keep the skill generic and in Productivity because the request covers any topic, including personal decisions without a repository.
- Track concern status across rounds, distinguish the user's decision from the agent's assessment, and stop when concerns are addressed or explicitly accepted; the full behavior is recorded in the instructions and documentation.
- Keep reviews in the conversation by default, saving a dated record for project decisions or when requested, with personal reviews kept out of unrelated project files.
- Do not require behavioral evaluations to complete this addition; they remain optional under the repository's existing policy.

## Next

1. Inspect the commit containing this handoff and compare the branch with its remote to confirm publication; finish the authorized commit or push only if it remains incomplete.
2. If the user wants further work, agree whether to evaluate behavior or revise it from actual usage before changing the skill.
3. For optional evaluations, cover a personal choice, a technical choice, a sound decision that survives challenge, and a stopped or resumed review; keep results distinct from static validation.

## Open questions

No product decision blocks delivery.
Whether to run conversational evaluations is up to the user; there is no evidence yet that the new instructions improve outcomes over an unaided conversation.

## Sources

- `skills/productivity/challenge/SKILL.md`
- `skills/productivity/challenge/assets/decision-review.md`
- `documentation/skills/productivity/challenge.md`
- `AGENTS.md`
- `.claude-plugin/plugin.json`
- `scripts/skill-graph/flow.json`
- `scripts/check-skills.py`
- `.agents/scripts/generate-skill-manifests.py`
- `documentation/architecture-decision-record/0008-resume-skill-evaluations.md`
- `documentation/maintenance/standard-installation-wording.md`
