# Contributing

This repo is a snapshot of a corpus, not a live crawler. The useful
contributions are: better metadata, missing original URLs, a source
description that is wrong, or a file that should not be here.

## Takedown

If you own a transcript or story and want it removed, open an issue with
the [takedown template](.github/ISSUE_TEMPLATE/takedown.yml). Include the
path or original URL. We will delete the file and its row in
`catalog/documents.jsonl`.

## Catalog fixes

`catalog/documents.jsonl` is the index. If a row has a broken `url`, a
wrong `source_id`, or a title that is still a leftover filename, send
a pull request that touches that row and, if the file itself needs a
rename, the file.

After you change files, rebuild the summary:

```bash
python3 examples/quickstart.py
```

That script does not rewrite the catalog. For a full recount, run
`scripts/ingest.py` against a local cache, or edit `catalog/summary.json`
by hand for a small patch.

## Adding a source

A new source needs three things, in the same pull request:

1. Files under `data/transcripts/...` or `data/companies/...` or
   `data/founder-stories/...`
2. One catalog row per file, same schema as the existing JSONL
3. A short paragraph in `SOURCES.md` that says who the source is and
   what it is good for, in plain English

Do not add full books. Do not add files without an original URL unless
the source is a public register.

## Tone of the docs

Keep `SOURCES.md` as a description of the source, not a pitch. Say what
the files contain and when they mislead (sales-script libraries, unresolved
fund names, empty Starter Story numeric fields).
