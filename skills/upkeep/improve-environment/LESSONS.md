# Filing a project lesson

Adapted from the `memorize` skill. A project lesson is a convention, command, rule, or navigation pointer that would apply to the next task too, not a change to one result.

| Lesson | Home | How |
| --- | --- | --- |
| A project convention, command, gotcha, or navigation pointer agents keep missing | The nearest `AGENTS.md` at the boundary where it applies | Follow [AGENT-INSTRUCTIONS.md](AGENT-INSTRUCTIONS.md) |
| A code convention no tool enforces | The project's conventions file (`documentation/conventions.md` unless the project keeps it elsewhere) | Follow [CONVENTIONS-FORMAT.md](CONVENTIONS-FORMAT.md) |

The environment is a home too: a `package.json` script, a configuration file, or `--help` output already states its fact. Leave those facts there.

1. State the lesson in one sentence, with its reason when the reason is not obvious.
2. Pick its home from the table: the place that is read at the moment the lesson matters.
3. Read that home first. Update an existing entry instead of adding a second one, and remove an entry the lesson proves wrong.
4. Write it, then tell the user in one line what was saved and where.

Keep secrets, one-conversation context, and facts the environment already states out of every home.

Completion: the lesson exists in exactly one home, and the user knows where.
