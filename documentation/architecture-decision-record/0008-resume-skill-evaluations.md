# Resume skill evaluations in a repository-level folder

Status: accepted.

This supersedes the "Evaluation pause" section of [0005: Make skills autonomous](./0005-make-skills-autonomous.md). The rest of 0005 stands. The retirement of `setup-delegation-policy` that 0005 decided is now done: the rule and the tier agent guide live in [documentation/delegation](../delegation/) as files to copy by hand.

## Context

0005 paused per-skill evaluations and removed the `evals/` trees inside skill folders. Most of what the earlier evaluations found came from writing them, not from rerunning them, and full behavioral suites for every skill cost hundreds of agent runs per pass. Interactive skills (`interview`, `specify`, `teach`) and judgement skills (`architect`, `prioritize`) also have no objective expected output without a simulated user or a subjective grader.

Two kinds of evaluation still pay. Triggering evaluations are cheap and objective, and they catch overlapping descriptions. Behavioral evaluations pay where the result can be checked mechanically and a mistake is costly.

## Decisions

### Evaluations are allowed, not required

A skill may have an evaluation suite. None is required, and `scripts/check-skills.py` does not demand one. Priority goes to:

- Triggering evaluations, for any skill: prompts that should and should not invoke it.
- Behavioral evaluations, for skills whose result can be checked from the resulting state: `rebase`, `sync-tree`, `resolve-merge-conflicts`, `work-in-tree`, `memorize`, and `setup`.

### Suites live in `evaluations/` at the repository root

Suites sit under `evaluations/<bucket>/<skill>/`, outside the skill folders, so they never ship with an installed skill. No tool fixes the folder name: `claude plugin eval` reads it from the plugin manifest's `experimental.evals` value, and skill-creator takes its workspace as a path. The manifest sets `experimental.evals` to `evaluations`, and the folder uses the repository's full-word naming. Run results under `evaluations/results/` stay local and are ignored by Git.

### Reports and claims

Reports worth keeping follow [documentation/evaluations/README.md](../evaluations/README.md). Do not claim behavioral improvement from checks that only validate structure, or from an evaluation that was not run.

## Consequences

Suites cost maintenance: a change to a skill's behavior or description may need its cases updated. A skill with no suite stays acceptable, and an evaluation run stays a deliberate, paid action rather than part of every check.
