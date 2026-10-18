# Proof: bundled-copy drift check and the human-in-the-loop template guard

- **Verdict:** proven
- **Work:** working tree on `f670877` (the audit fixes, staged)
- **Agreement:** `AUDIT.md` priority 5 (drift check) and the smaller defect on `skills/upkeep/debug/assets/hitl-loop.template.sh`
- **Environment:** macOS 26.6.2, Python 3.11.9, GNU bash 3.2.57; checks run in two scratch worktrees, `$W` at `f670877` and `$E` at `f670877` with the staged diff applied
- **Date:** 2026-10-18

## Claims

| # | Claim | Source | Verdict |
| --- | --- | --- | --- |
| C1 | `scripts/check-skills.py` fails, naming the file and every copy, when one bundled copy differs from its same-named siblings | Audit priority 5 | proven |
| C2 | The check passes on the repository as committed, where every same-named copy matches | Audit priority 5 | proven |
| C3 | The template exits with code 2 and a message, before any prompt, when run without a terminal | Smaller defect on the template | proven |
| C4 | Run in a terminal, the template still prompts and prints the captured `KEY=VALUE` lines | Existing behavior | proven |
| C5 | The four copies of the template are identical | Audit priority 5 | proven |

## Evidence

### C1: drift fails the check

- **Check:** `echo drift >> $E/skills/workflow/iterate/references/tests.md; python3 $E/scripts/check-skills.py $E`
- **Shown able to fail:** before and after. The same edit in `$W` (starting commit) gives exit 0 and no `bundled copies differ` line.
- **Result:** exit 1, `ERROR: references/tests.md: bundled copies differ (skills/workflow/address-feedback/references/tests.md, ...)`.
- **Reproduced:** by a fresh-context agent that had not seen the implementation; match.

### C2: a consistent repository passes

- **Check:** `python3 $E/scripts/check-skills.py $E` after restoring the file
- **Shown able to fail:** C1 is the failing case of the same check on the same tree.
- **Result:** exit 0, `Checked 42 skills, 42 plugin paths, 42 documentation pages, and 245 Markdown files.`
- **Reproduced:** by a fresh-context agent; match.

### C3: no terminal, early exit

- **Check:** `echo | bash $E/skills/upkeep/debug/assets/hitl-loop.template.sh; echo $?`
- **Shown able to fail:** before and after. At `$W` the same command prints the first two prompts and exits 1 when `read` hits end of input.
- **Result:** `Run this in your own terminal: it waits for your answers.`, exit 2, no prompt printed.
- **Reproduced:** by a fresh-context agent; match.

### C4: terminal run unchanged

- **Check:** `python3 documentation/verification/2026-10-18-audit-fixes/pty-run.py $E/skills/upkeep/debug/assets/hitl-loop.template.sh` (answers Enter, `y`, `boom` through a pseudo-terminal)
- **Shown able to fail:** the pseudo-terminal run reaches the guard's other branch; C3 shows the guard firing when stdin is not a terminal.
- **Result:** exit 0, ending `ERRORED=y` and `ERROR_MSG=boom`.
- **Reproduced:** by a fresh-context agent; match.

### C5: identical copies

- **Check:** `md5 -q $E/skills/*/*/assets/hitl-loop.template.sh | sort -u | wc -l`
- **Shown able to fail:** C1 shows the drift check catching any difference between same-named copies.
- **Result:** `1`.
- **Reproduced:** by a fresh-context agent; match.

## Regressions

| Check | Command | Starting commit | End state |
| --- | --- | --- | --- |
| Layout check | `python3 scripts/check-skills.py` | pass | pass |
| Script tests | `python3 scripts/test-*.py` (five files) | pass | pass (39 tests in `test-check-skills.py`, two new) |
| Manifests | `python3 .agents/scripts/generate-skill-manifests.py --check` | stale (`verify` and root `apm.yml`) | 43 manifests current |
| Plugin | `claude plugin validate . --strict` | not run | pass |

## Not proven

None. A fresh-context agent reran every command (the end-state worktree built from `HEAD` plus the staged diff, since the commit did not exist yet) and every exit code and result line matched. It also reran the regression rows; `claude plugin validate . --strict` passed with one advisory that `README.md` has no install line for `dyrits-skills`.

## Reproduce

```sh
W=$(mktemp -d)/start; E=$(mktemp -d)/end
git worktree add --detach "$W" f670877
git worktree add --detach "$E" <commit that adds this proof>
echo drift >> "$W/skills/workflow/iterate/references/tests.md"; python3 "$W/scripts/check-skills.py" "$W"; echo $?
echo drift >> "$E/skills/workflow/iterate/references/tests.md"; python3 "$E/scripts/check-skills.py" "$E"; echo $?
git -C "$E" checkout -- .; python3 "$E/scripts/check-skills.py" "$E"; echo $?
echo | bash "$W/skills/upkeep/debug/assets/hitl-loop.template.sh"; echo $?
echo | bash "$E/skills/upkeep/debug/assets/hitl-loop.template.sh"; echo $?
python3 "$E/documentation/verification/2026-10-18-audit-fixes/pty-run.py" "$E/skills/upkeep/debug/assets/hitl-loop.template.sh"
md5 -q "$E"/skills/*/*/assets/hitl-loop.template.sh | sort -u | wc -l
for t in "$E"/scripts/test-*.py; do python3 "$t"; done
git worktree remove --force "$W"; git worktree remove --force "$E"
```

## New files

`documentation/verification/2026-10-18-audit-fixes/pty-run.py`, a pseudo-terminal driver for C4.
