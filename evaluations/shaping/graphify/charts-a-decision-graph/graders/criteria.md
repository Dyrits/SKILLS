---
type: llm
focus: trace
---

PASS if the run created a map with a destination and several decision tasks phrased as questions to resolve (for example which provider, how sessions migrate), with blocking relationships where one decision depends on another.
FAIL if the tasks are implementation slices (for example "build the login page", "write the migration script"), if no map was written, or if the run starts implementing the change.
