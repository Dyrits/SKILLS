# 2026-10-28 work-in-tree

Written 2026-10-28 (UTC). Runs took place on 2026-10-28.

## Result

The skill separates from the baseline (Δ +0.33). With the plugin, 3 of 3 runs fired `work-in-tree`, created `.worktrees/notes` on a new branch, committed `NOTES.md` there, recorded `branch=main` as the return destination, left the checkout untouched, and passed the rubric. Without the plugin, 3 of 3 runs created the worktree and left the checkout untouched, 2 of 3 passed the rubric, and none recorded a return destination. The near-miss negative passed 6 of 6.

## What was evaluated

| Item | Value |
| --- | --- |
| Skill | [`skills/version-control/work-in-tree/SKILL.md`](../../skills/version-control/work-in-tree/SKILL.md) |
| Repository state | `1f7bc18` (`main`), plugin `dyrits-skills` 0.2.0 loaded in place; the suites were uncommitted at run time |
| Cases | [`evaluations/version-control/work-in-tree/`](../../evaluations/version-control/work-in-tree/) |
| Runner | `claude plugin eval` from Claude Code 2.1.311; agent model Opus 5.5 (`claude-opus-5-5`, from the result file) |
| Judge | Claude Code's default model for `llm` graders (`haiku`, per `claude plugin eval --help`) |
| Runs | 3 with the plugin and 3 without, per case, concurrency 4 |

## Method

Real runs, not simulations: each run is a `claude -p` child in an empty temporary workspace, scaffolded by the case's `fixture.sh` where it has one, with only this plugin loaded (or no plugin, for the baseline arm). The baseline arm saw only Claude Code's built-in skills, not the skills linked into `~/.claude/skills` (checked in the init event of a smoke run the same day). Graders are the case's `graders/*.md`: `tool_used` and `regex` checks computed from the trace and files, and `llm` rubrics voted three times by the judge. A `tool_used: Skill` grader is an indicator only and is not scored in a two-arm run. Raw results (`2026-10-28-version-control.json` and its `report.html`) stayed local in the ignored `evaluations/results/`.

The suites ran from a detached worktree of `main` with the uncommitted suites copied in, so the plugin under test held exactly the skills of `main` and none of the unmerged ones. The whole `version-control` tag took 264 seconds and USD 7.44.

An earlier attempt on 2026-10-23 (in the same run as the `upkeep` suites) produced no result for this skill: every run but the `rebase` negative ended on an account session limit. A first rerun on 2026-10-28 finished, but its results were lost with the temporary directory before anyone read them.

## Results

| Case | With plugin | Without plugin | Δ |
| --- | --- | --- | --- |
| `works-in-a-new-worktree` (positive) | 1.00 (3 of 3) | 0.67 (0 of 3) | +0.33 |
| `ignores-worktree-question` (negative) | 1.00 (3 of 3) | 1.00 (3 of 3) | 0.00 |

## Limits and open points

- The `return-destination` grader checks the skill's own convention (`.git/worktrees/notes/return-destination`), which a plain agent cannot know; part of the difference is by construction. The rubric difference (2 of 3 without) is the independent signal.
- The prompt places the worktree inside the workspace because writes outside it are blocked in the evaluation sandbox; the skill's default location is not exercised.
- Runs with the plugin took about 18 turns against about 12 without.

## Reproduce

```bash
claude plugin eval evaluations/version-control/work-in-tree/works-in-a-new-worktree/prompt.md --scaffold --allow-tools Bash Write Edit --max-cost-usd 5
claude plugin eval evaluations/version-control/work-in-tree/ignores-worktree-question/prompt.md --max-cost-usd 2
```

The whole bucket: `claude plugin eval . --tag version-control --scaffold --allow-tools Bash Write Edit -j 4 --max-cost-usd 10`. `--scaffold` runs each `fixture.sh`; without it the positive cases start in an empty directory.
