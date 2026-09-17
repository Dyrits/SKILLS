# Triage Labels

The skills speak in terms of two category roles and five state roles. This file maps those roles to the actual label strings used in this repository's issue tracker.

## Category roles

| Role in Dyrits/SKILLS | Label in our tracker | Meaning                       |
| --------------------- | -------------------- | ----------------------------- |
| `bug`                 | `bug`                | Something is broken           |
| `enhancement`         | `enhancement`        | New feature or improvement    |

## State roles

| Role in Dyrits/SKILLS | Label in our tracker | Meaning                                  |
| --------------------- | -------------------- | ---------------------------------------- |
| `needs-triage`        | `needs-triage`       | Maintainer needs to evaluate this issue  |
| `needs-info`          | `needs-info`         | Waiting on reporter for more information |
| `ready-for-agent`     | `ready-for-agent`    | Fully specified, ready for an AFK agent  |
| `ready-for-human`     | `ready-for-human`    | Requires human implementation            |
| `wontfix`             | `wontfix`            | Will not be actioned                     |

When a skill mentions a role (e.g. "apply the AFK-ready triage label"), use the corresponding label string from these tables. Every triaged issue still carries exactly one category and one state role.

Edit the right-hand columns to match whatever vocabulary you actually use. The role set itself (which categories and states exist, and the transitions between them) is part of the skills and stays fixed: `to-tickets` and `to-specifications` apply `ready-for-agent`, so removing or renaming a role breaks the chain.
