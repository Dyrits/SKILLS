# Session log: add monthly CSV export to the ledger app

Turn numbers refer to the agent transcript. Task: add a "Monthly summary" CSV export.

- Turn 4 to 19: the agent made 14 search and read calls to find where feature flags are read. They are defined in `config/flags.yaml` and loaded in `src/boot/flags.ts`. Nothing pointed to either file.
- Turn 12: asked a one-line question about a TypeScript error, the agent invoked the `debug` skill, built a mock reproduction, and answered 6 minutes later.
- Turn 31: the agent imported `formatMoney` from `src/legacy/format`. `AGENTS.md` says never to import from `src/legacy`. The reviewing agent did not flag it. The user caught it at turn 52.
- Turn 40: the agent wrote `listEntries()` so that a database error returns an empty list. The reviewing agent passed it. The user caught it at turn 55 and explained errors must reach the caller.
- Turn 60 to 68: `npm test` was run six times. Each run printed about 40,000 lines of snapshot diff and the agent paged through them.
- Turn 71: the export failed in the dev server. The agent could not see the dev server output and asked the user to paste it.
- Turn 80: after the agent finished, the user changed the CSV delimiter from comma to semicolon, because a new accounting partner requires it.
