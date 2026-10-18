# Local decision graph

Use this when `AGENTS.md` points to no task tracker configuration. The graph lives in Markdown files in the repository; nothing is published.

- **Map**: `documentation/capabilities/<capability>/map.md`, holding the Notes / Decisions-so-far / Fog body. Reference it from the backlog when it represents a candidate effort.
- **Child task**: a capability task file, `documentation/capabilities/<capability>/tasks/NN-<slug>.md`, with the question in the body. A `Type:` line records the task type (`research`/`prototype`/`interview`/`task`); a `Progress:` line records `claimed`/`resolved`.
- **Blocking**: a `Blocked by: NN, NN` line near the top. A task is unblocked when every file it lists is `Progress: resolved`.
- **Frontier**: scan the capability's task files for files that are unresolved, unblocked, and carry no `Progress: claimed`; first by number wins.
- **Claim**: set `Progress: claimed` and save before any work.
- **Resolve**: append the answer under an `## Answer` heading, set `Progress: resolved`, then append a context pointer (gist + link) to the map's Decisions-so-far in `map.md`.

When a map or task folder of this kind already exists elsewhere in the repository, adopt it following [project-documents.md](project-documents.md) instead of creating a second one. When you create the first map, add one line to the nearest `AGENTS.md` saying where decision maps live and when to read them, and tell the user the graph is local.
