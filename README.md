# startup-data

A public corpus for people who want to study how startups and small businesses work: what founders say, what they ship, and what the public record shows.

The files were collected from YouTube, podcasts, founder interviews, and open company registers while building [VMSTE](https://vmste.org). This repo is the cleaned snapshot: sources named, duplicates dropped, catalogs written so you can query the set instead of walking 9,000 filenames.

**[Sources](SOURCES.md)** | **[Books](BOOKS.md)** | **[Catalog](catalog/summary.json)** | **[Cite](CITATION.cff)**

## What's in here

| Slice | Size | What you can do with it |
|---|---|---|
| YouTube transcripts | 6,286 talks, ~295 MB | Mine playbooks for growth, sales, hiring, fundraising, positioning |
| Podcast transcripts | 301 episodes (Indie Hackers, Practical Product) | Compare how bootstrapped founders talk about revenue and distribution |
| Founder stories | 2,219 write-ups from Starter Story | Read how a business started, what it cost, what it earns |
| Company tables | ~97k rows across 16 sources | Join a talk or story to YC batches, SEC Form D filings, events |
| Book catalog | 44 titles, 22 short quotes | See what to read next, and which talks in this repo sit next to that book |

The catalog at `catalog/documents.jsonl` is the index. Each row has `kind`, `source_id`, `title`, `url`, `path`, `topics`, and `date` when we have one.

Sales-training channels (Sales Scripter, Cognism, Superhuman, Sales Miner, Patrick Dang) are the largest YouTube slice. Filter them out if you want operator talks rather than scripts. The denser strategy sets are smaller: Y Combinator, Paul Graham, Lenny's Podcast, First Round, a16z, Andrew Chen, flywheels / network effects.

Full book files are not here. [`BOOKS.md`](BOOKS.md) is the reading list with Wikipedia / Open Library / author links. Short quotes live in `data/books/quotes.json`.

## Layout

```
catalog/
  documents.jsonl   one row per file
  sources.json      70 sources with descriptions
  summary.json      counts
data/
  transcripts/youtube/<source>/
  transcripts/podcasts/<source>/
  founder-stories/starter-story/{stories,ideas}/
  companies/{yc-companies,sec-edgar,events,...}/
  books/{catalog.json,quotes.json}
BOOKS.md
examples/quickstart.py
SOURCES.md
```

## How to load it

Python, no extra packages:

```python
import json
from collections import Counter
from pathlib import Path

docs = [json.loads(line) for line in Path("catalog/documents.jsonl").open()]
print(len(docs), "files")
print(Counter(d["kind"] for d in docs))
```

Or with pandas:

```python
import pandas as pd

docs = pd.read_json("catalog/documents.jsonl", lines=True)
talks = docs[docs.kind == "youtube_transcript"]
yc = pd.read_json("data/companies/yc-companies/shard-0000.json")
```

A slightly longer walkthrough is in [`examples/quickstart.py`](examples/quickstart.py).

Founder stories are JSON objects with the original metadata plus a `body_markdown` field. The numeric fields on Starter Story metadata are often empty; the numbers live in the body text.

Company shards are JSON arrays (or NDJSON for `events/`). `fund-holdings` is inferred from Form D and many rows still have unresolved names. Treat it as a join table, not as a finished fund database.

## Languages

Mostly English. A small Russian-language set lives under `yamalkevich` (founder talks from the VMSTE orbit).

## How this was built

Sessions were downloaded as transcripts with YAML frontmatter (title, original URL, date, channel). We then:

1. Dropped full ebook files, AI-coding workflow dumps, and a geopolitics channel that does not belong in a startup corpus. The books remain as a catalog plus short quotes.
2. Merged duplicate YouTube sessions (retry folders, re-downloads of the same talks).
3. Deduped by YouTube video id (123 repeats removed).
4. Folded Starter Story "ideas" into stories when the slug already existed (1,473 overlaps).
5. Wrote `catalog/` so a new collection does not need a new folder convention.

`scripts/ingest.py` is how this snapshot was packed from a local cache. It is not a scraper.

## License and copyright

The catalog, documentation, and the way this snapshot is arranged are [CC BY 4.0](LICENSE).

Transcripts, founder stories, and third-party pages remain the property of their original authors. We host them here for research and pattern analysis, and every document keeps a link back to the source. If you own a piece and want it removed, open a [takedown issue](https://github.com/VMSTE/startup-data/issues/new?template=takedown.yml).

See [NOTICE.md](NOTICE.md) for the split.

## Citing

```
VMSTE. (2026). startup-data [Data set]. https://github.com/VMSTE/startup-data
```

Or import [`CITATION.cff`](CITATION.cff) in Zotero / GitHub.

This repository is the dataset, not the crawler. The original transcripts keep their frontmatter so you can see when each file was grabbed.
