# Issue tracker: Local Markdown

Backlog: `documentation/backlog.md`

Local task bodies live in `documentation/capabilities/<capability>/tasks/`. The living specification is `documentation/capabilities/<capability>/specifications.md`.

## Wayfinding operations

Used by graphify. The map is a file with one child file per decision task, not an implementation plan.

- **Map**: `documentation/capabilities/<capability>/map.md` (the Destination / Notes / Decisions-so-far / Not-yet-specified / Out-of-scope body).
- **Child task**: `documentation/capabilities/<capability>/tasks/NN-<slug>.md`, numbered from `01`, with the question in the body. A `Type:` line records the task type (`research`, `prototype`, `refine`, `task`); a `Progress:` line records `claimed` or `resolved`.
- **Blocking**: a `Blocked by: NN, NN` line near the top. A task is unblocked when every file it lists is `Progress: resolved`.
- **Frontier**: files in `tasks/` that are unresolved, unblocked, and carry no `Progress: claimed`; first by number wins.
- **Claim**: set `Progress: claimed` and save before any work.
- **Resolve**: append the answer under an `## Answer` heading, set `Progress: resolved`, then append a context pointer (gist and link) to the map's Decisions-so-far.
