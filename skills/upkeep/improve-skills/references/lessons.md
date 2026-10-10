# Filing a project lesson

Adapted from the `memorize` skill. A project lesson is a convention, command, rule, or navigation pointer that would apply to the next task too, not a change to one result.

| Lesson | Home | How |
| --- | --- | --- |
| A project convention, command, gotcha, or navigation pointer agents keep missing | The nearest `AGENTS.md` at the boundary where it applies | Follow [agent-instructions.md](agent-instructions.md) |
| A code convention no tool enforces | The conventions file `AGENTS.md` names; when there is none, adopt an existing conventions document (judging by content, asking when unclear) or create `documentation/conventions.md`, never overwriting, and add its `AGENTS.md` line | Follow [conventions-format.md](conventions-format.md) |

The environment is a home too: a `package.json` script, a configuration file, or `--help` output already states its fact. Leave those facts there.

1. State the lesson in one sentence, with its reason when the reason is not obvious.
2. Pick its home from the table: the place that is read at the moment the lesson matters.
3. Read that home first. Update an existing entry instead of adding a second one, and remove an entry the lesson proves wrong.
4. Write it, then tell the user in one line what was saved and where.

Keep secrets, one-conversation context, and facts the environment already states out of every home.

Completion: the lesson exists in exactly one home, and the user knows where.
