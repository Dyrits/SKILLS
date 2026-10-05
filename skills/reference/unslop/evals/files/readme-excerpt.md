## Architecture

The substrate of Quillbox is a small event log, and it is the north star for every other module. Events are validated by the ingest layer before being persisted by the writer.

Parser rejects bad date → exit 2, no write.

Config loading is handled by the loader, and the file is parsed by it once at startup. With Quillbox, the database stays close at hand, and SQL you can read keeps everyone on the same page. The team found a clever wedge into the legacy importer, and we significantly improved how quickly it runs.
