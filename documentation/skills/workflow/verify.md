Fork-added skill: it has no upstream equivalent.

## What it does

`verify` proves that implemented work behaves as intended and leaves the proof in the repository. It turns the work into claims, one observable behavior each, and gathers evidence for every claim by whatever means the environment offers: driving the running application, sending real requests, running commands, or writing a test when nothing else reaches the behavior.

Its defining constraint is that a passing check is not enough. Each check must also be shown able to fail, either by running it against the starting commit or by deliberately breaking the code it covers. A fresh agent that never saw the implementation then reruns the proof from the file alone. A claim that skips either step stays unproven.

It observes and never fixes. A failed claim is reported, not repaired.

## When to reach for it

Type `/verify`, or an agent can reach for it when you ask whether a change really works, or want evidence before merging or shipping.

| Your situation | Skill |
| --- | --- |
| Build agreed work test-first | [implement](./implement.md) |
| Check code against standards and the agreement, and refactor | [review-and-refactor](./review-and-refactor.md) |
| Prove the finished work does what it should | This one |

## The proof

The proof is a Markdown file listing every claim with its source, the exact check, how the check was shown able to fail, the result, and who reproduced it. It also records the regression checks against the starting commit, every claim not proven and what would prove it, and the commands to rerun everything. Screenshots and logs sit beside it.

Each claim ends with one verdict: proven, failed, unproven, or awaiting human judgment. Appearance and feel always wait for a person: the skill captures screenshots or a recording but never marks them proven on its own.

## Common questions

**Is passing tests not proof enough?**

No. A test that would also pass on broken code proves nothing, so every check is shown failing before the change or under a deliberate mutation.

**Which tools does it use?**

Whatever is installed: the project's test runner, browser automation, `curl`, the application's own command-line interface, or a scratch script. When the strongest means is missing, it uses the next one and records what was unavailable.

**Does it change my code?**

Only temporarily: mutations are restored and checked against `git status` and `git diff`. Tests or scripts written for the proof are left uncommitted and listed, and production code is never edited.

**Where does the proof go?**

Where the project already keeps verification records, as `AGENTS.md` names them. Otherwise it goes to `documentation/verification/`, and a line is added to `AGENTS.md`. Existing proofs are never overwritten.

## It's working if

- Every acceptance criterion appears as a claim with a verdict.
- Each proven claim shows how its check failed before the change or under mutation.
- The proof records an independent rerun, and its reproduce commands work from a clean checkout.
- Your working tree holds only the proof and the listed new files once it finishes.

## Where it fits

A standalone check after [implement](./implement.md), [iterate](./iterate.md), or [review-and-refactor](./review-and-refactor.md), whenever you need evidence that the result works rather than a report that tests passed.
