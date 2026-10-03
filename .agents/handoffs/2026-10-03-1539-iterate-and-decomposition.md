# Iterate and decomposition

Supersedes: none. Earlier handoffs cover unrelated work.

## Resume here

The user asked to finalize the workflow names, remove evaluation artifacts and obsolete names, write this handoff, commit, and push. Evaluation work is deliberately paused. The development skill's final name is `iterate`. The generated workspace and both skills' `evals/` folders were removed at the user's request. The results below summarize this session; original execution artifacts are no longer retained in the repository.

## Authoritative artifacts

- `skills/experimental/iterate/SKILL.md`: experimental, user-invoked continuous development workflow.
- `skills/experimental/iterate/ARTIFACTS.md`: working state and automatic feedback rules.
- `skills/experimental/iterate/MILESTONE-REVIEW.md`: conditional standards-and-behavior review.
- `skills/experimental/divide-and-conquer/SKILL.md`: experimental, model-invoked shaping branch.
- `skills/experimental/README.md` and `skills/getting-started/what-is-next/SKILL.md`: discovery and routing.

Both skills stay outside the plugin and promoted listings. They have no human-facing promoted documentation pages. They have not been linked into global harness directories during this session.

## User intent and remaining boundaries

The user wants one solo-development workflow, not their professional specification-and-ticket process. Questions, decisions, implementation, and checks advance together. Routine internal changes are delegated; the user approves intended behavior, consequential tradeoffs, and appearance or interaction where judgment is needed.

Technology selection is neutral but favors explicit structure, meaningful early error detection, and visible failure handling. No particular language or framework is prescribed. One-command startup is required.

Large ideas use decomposition only when scope, competing capabilities, or dependencies block selection of a useful increment. The agent chooses whether to invoke the shaping branch; the user approves the focus and material deferrals. Backlog candidates are not requirements or authorization. Small clear changes skip decomposition.

The skill files own the detailed rules; consult them rather than reconstructing the workflow from this summary.

## Evaluation status

The first evaluation used the earlier name `slice-and-build` and had six completed runs with independent grading. Reported scores were:

| Scenario | With skill | Baseline |
|---|---:|---:|
| Initial approach and approval boundary | 4/5 | 3/5 |
| Approved filter implementation | 8/8 | 6/8 |
| Scope correction | 6/6 | 4/6 |

Do not treat these raw scores as proof of superiority:

- Both saved filter implementations passed independent fixture checks.
- Both correction responses made reasonable scope recommendations.
- Differences largely concern approach comparison and workflow artifacts.
- Missing independent execution evidence, asymmetric artifact instructions, and workspace synchronization failures affect interpretation.
- No reliable token or timing measurements were supplied. No token-saving claim is established.

The multi-turn trial completed the initial interview, first runnable increment, interruption, and fresh-session recovery. Four independent first-increment checks passed. Before the final scripted whitespace correction, seven of nine final checks passed; the two expected failures demonstrated that the checks detect the missing correction.

The final correction is incomplete. Its persisted subthread contains a partial source edit, but no completed result was collected or verified here. Do not claim the nine-test suite passed. The final correction task was told to stop when the user paused evaluation. The sample application was subsequently removed with the generated workspace.

Conditional research, milestone review, strengthened TDD routing, and decomposition were added after the earlier simulation began. Static review does not validate their actual invocation. Future routing tests require the harness to expose `divide-and-conquer` as a Skill tool target and retain real invocation events; manual file reading is not equivalent evidence.

## Subthreads and harness limitations

Most subthreads are completed test, grading, or review jobs. Two older persisted threads had unfinished state:

- Final correction: `ksQQ85bFypV5S_6p0RF9IXwiEZLOAAH7UJIBxBD4Hb2XjQRLFolB9uuuDumM`.
- Obsolete rename repair: `ksQQ85bFypV5S_6p0RF9IXwiEZLOAAFccJIBxBD4Hb2XjQRLFolB9uuuDumM`.

Both received stop/supersession instructions. Persisted thread snapshots are not proof that agents are currently running. Do not pull stale source or old workspace paths from the obsolete repair thread.

The edit tool's `Move to` operation reported success without moving files. Source renames therefore used explicit Add/Delete operations. Some terminal-copied untracked projects also failed to synchronize, and some commands failed materialization with "the checkout kept changing." Treat these as harness limitations, separate from application failures. `develop-incrementally` and `slice-and-build` were earlier draft names, not additional skills; their obsolete directories were removed.

## Next session

The user wants to work on evaluations later. Inspect the final skill files, then choose a bounded test goal: recreate a multi-turn trial, exercise research/review/TDD routing, or test decomposition invocation and bypass. Prepare fresh fixtures; the earlier workspace and proposed test files were intentionally removed. Keep measured execution evidence distinct from executor-authored summaries.

## Suggested skills

- Call the Skill tool with "writing-for-agents" when refining instructions.
- Call the Skill tool with "skill-creator" when resuming evaluations; use its standard viewer and preserve missing-metric limitations.
- Use "scriptbook" through the Skill tool before writing reusable helper scripts.
- The user invokes `/iterate` to develop a project. `divide-and-conquer` is model-invoked when its selection-blocker condition applies.

## Publication

The attached checkout was on `main`. `origin` points to `git@github.com:Dyrits/SKILLS.git`; the upstream push URL is disabled and is not a publication target. The parent will commit the final scoped changes and push to `origin/main` as requested. Verify the actual commit and push result in Git before describing publication as complete.
