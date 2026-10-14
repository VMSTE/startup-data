#!/usr/bin/env python3
"""Load the catalog and print a few useful cuts. Stdlib only."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_docs() -> list[dict]:
    path = ROOT / "catalog" / "documents.jsonl"
    return [json.loads(line) for line in path.open(encoding="utf-8") if line.strip()]


def main() -> None:
    docs = load_docs()
    print(f"{len(docs)} documents in catalog/documents.jsonl")
    print("by kind:")
    for kind, n in Counter(d["kind"] for d in docs).most_common():
        print(f"  {kind:24s} {n:6d}")

    tagged = [d for d in docs if "network-effects" in (d.get("topics") or [])]
    print(f"\n{len(tagged)} files tagged network-effects")
    for row in tagged[:5]:
        print(f"  - {row['title'][:80]}")
        print(f"    {row['path']}")

    yc_dir = ROOT / "data" / "companies" / "yc-companies"
    shards = sorted(yc_dir.glob("shard-*.json"))
    if shards:
        first = json.loads(shards[0].read_text(encoding="utf-8"))
        print(f"\nYC shard {shards[0].name}: {len(first)} companies")
        sample = first[0]
        print(f"  e.g. {sample.get('name')} - {sample.get('description', '')[:80]}")

    books = json.loads((ROOT / "data" / "books" / "catalog.json").read_text(encoding="utf-8"))
    quotes = json.loads((ROOT / "data" / "books" / "quotes.json").read_text(encoding="utf-8"))
    print(f"\n{len(books)} books in the catalog, {len(quotes)} quotes")
    nfx = [b for b in books if "network-effects" in b.get("topics", [])]
    print("network-effects books:")
    for b in nfx:
        print(f"  - {b['title']} ({b['year']})")


if __name__ == "__main__":
    main()
