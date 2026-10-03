# Resume a rebase batch

Read the batch directory. Keep its target pin, starts, leases, and approved answers: current branch names and fresh fetches are evidence, not replacement inputs.

Before writing anything, establish through the host's actual execution state that no earlier subagent can still change its checkout. A saved transcript is not a liveness signal. When a subagent's state or checkout is out of reach, mark the branch `unknown` and ask.

For each branch, inspect its rebase location, its local tip, its backup ref, and the remote destination:

| Evidence | Next action |
| --- | --- |
| Rebase in progress at its location | Continue from the recorded commit with [BRANCH.md](BRANCH.md) |
| Local tip equals the start | Rebase not started; run [BRANCH.md](BRANCH.md) |
| Local tip equals the recorded validated tip | Validation is done; keep it for the report |
| Local tip differs from both, with no rebase in progress | Validate that tip from scratch with [BRANCH.md](BRANCH.md) |
| Remote equals the new tip | Confirm with `git ls-remote --refs` and mark `pushed and verified` |
| Remote differs from both the lease and the new tip | Report the concurrent change and ask |
| Rebase location missing | Keep the backup ref and record, and ask |

Then continue from step 4 of [SKILL.md](SKILL.md), with every branch of the batch in the report.
