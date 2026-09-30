# Upstream material

This directory preserves material from [mattpocock/skills](https://github.com/mattpocock/skills) that this fork does not maintain under its original identity.
Original upstream files are kept byte for byte, including their historical names, branding, links, and prose conventions.
The older archives at this directory's root remain frozen at the revisions when they were captured.

## Synchronisation records

Each content port records the upstream base and tip, the fork's starting revision, and the disposition of every upstream path changed in that interval.
The accompanying JSON inventory maps upstream paths to maintained fork paths or archived sources.
An ancestry merge records the upstream tip without changing content; the following port commit adopts changes into this fork's own names and structure.

- [2026-09-30](./sync/2026-09-30.md): port through `d81f3a1`, retaining this fork's branding and custom workflows.

## Snapshots

`snapshots/<upstream-tip>/files/` holds the changed upstream distribution files exactly as they read at that tip.
`snapshots/<upstream-tip>/removed/` holds source files removed in that interval, exactly as they read at its base.
Snapshots preserve upstream changesets, documentation, manifests, and steering files while the maintained equivalents follow this fork's conventions.
Upstream skill source remains reachable through the ancestry merge; the inventory identifies its maintained counterpart.
Retired skill entrypoints stored in a snapshot use the filename `SKILL.md.source`, preserving their bytes while keeping them out of skill discovery.

For the fork's adoption policy, see [architecture decision record 0001](../documentation/architecture-decision-record/0001-maintain-as-an-independent-fork.md).
