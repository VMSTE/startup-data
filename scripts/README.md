# Scripts

`ingest.py` packed this snapshot from a local cache of collected transcripts
and tables. It is not a scraper.

```bash
SOURCE_ROOT=/path/to/ais/data python3 scripts/ingest.py
```

`build_books.py` rebuilds `data/books/` and `BOOKS.md` from the curated
list in that file plus the local quotes shard. It does not copy ebook
files.

The public dataset is the `data/` and `catalog/` folders. You do not need
these scripts to use the repo.
