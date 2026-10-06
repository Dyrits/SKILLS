# 2026-10-06 setup-ai-workspace

Written 2026-10-06 (UTC). Runs took place on 2026-10-06.

## Result

Evals 2 and 3 were run once each after the skill moved to `AGENTS.md` only (creating it when missing). Eval 2 met 8 of 8 expectations and eval 3 met 6 of 6. Both runs also exposed one gap: the skill did not say what to do with the `Conventions:` line in `.agents/domain.md` when no `CONVENTIONS.md` exists and none is agreed. The skill and eval 3 were changed to close it; the change has not been re-run. Evals 1 and 4 to 10 were not run.

## What was evaluated

| Item | Value |
| --- | --- |
| Skill | [`skills/setup/setup-ai-workspace/SKILL.md`](../../skills/setup/setup-ai-workspace/SKILL.md), before the fix below |
| Repository state | `1c83052` plus uncommitted edits to the skill and its evals (the fix below) |
| Cases | [`skills/setup/setup-ai-workspace/evals/evals.json`](../../skills/setup/setup-ai-workspace/evals/evals.json), evals 2 and 3 |
| Runner model | Sonnet 5.5, one subagent per eval |
| Grader | The coordinating session, by hand, against expectations the runners never saw |

## Method

Simulated runs. Each runner read the skill by path (the Skill tool was not used), built a scratch Git repository, and answered the interview questions itself, printing each question and answer. The runners had no access to the user, so the interactive `model-domain` interview could not run.

## Results

| Eval | Scenario | Met |
| --- | --- | --- |
| 2 | GitHub remote, existing `AGENTS.md` with an outdated block | 8 of 8 |
| 3 | No remote, no `AGENTS.md`, `triage` not installed | 6 of 6 |

## Failures and limits

- **Gap found (closed in the skill, not re-run).** In eval 3 the interview was accepted but no rule was agreed, so no `CONVENTIONS.md` existed and neither `present` nor `declined` was true; the runner removed the line. In eval 2 the interview could not run, so `{present | declined}` stayed as a literal placeholder. The skill now records `present` once the file exists, `declined` on refusal, and otherwise deletes the line. Eval 3 gained an expectation for this.
- A minor ambiguity remains: a remote tracker keeps a link in `documentation/backlog.md`, yet the skill creates only what is needed now. Eval 2's runner did not create that file.
- One run each, same session as grader, no baseline. A pass shows the text can be followed, not that it is robust.
- The `Conventions:` expectation added to eval 3 is untested.

## Not run

Evals 1 and 4 to 10; a live trigger firing; a real `model-domain` interview; the revised skill text.

## Reproduce

```sh
python3 .agents/scripts/stage-eval-run.py /tmp/skill-evals/run-N skills/setup/setup-ai-workspace behavior
```

Run one subagent per staged `eval-<id>/prompt.txt` and grade against `grading-sheet.md`. Raw outputs were kept in `/tmp/skill-evals/run-3/` and are not versioned.

## Re-run (eval 3, after the fix)

One Sonnet runner. All 7 expectations met, including the new one: the `Conventions:` line was removed from `.agents/domain.md` with no placeholder left. The runner noted that the template still said "unless the line below says otherwise" after the line is deleted; the template now reads "unless a `Conventions: declined` line below says otherwise". That wording change was not re-run. Same caveats as above: one run, same session as grader.
