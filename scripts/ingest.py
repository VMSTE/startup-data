#!/usr/bin/env python3
"""Copy and normalize local collections into this dataset repo.

SOURCE_ROOT points at the machine-local ais/data cache. The public repo
keeps the output under data/ and catalog/, not this script's inputs.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import sys
import urllib.parse
from pathlib import Path

SOURCE_ROOT = Path(os.environ.get(
    "SOURCE_ROOT",
    "/Users/wegorelax/Documents/sandbox/ais/data",
))
REPO = Path(os.environ.get(
    "REPO",
    str(Path(__file__).resolve().parents[1]),
))

SKIP_YOUTUBE = {
    "predictive-history",
    "rasmic-workflow",
    "vpU9lZY69O4",
}

MERGE_YOUTUBE = {
    "belfort-redownload": "belfort",
    "belfort-retry": "belfort",
    "yamalkevich-fresh-2026-05-20": "yamalkevich",
    "yamalkevich-streams": "yamalkevich",
    "yamalkevich-streams-2026-05-20": "yamalkevich",
    "saastr-full": "saastr",
}

YOUTUBE_SOURCES = {
    "20vc": {
        "name": "20VC",
        "host": "Harry Stebbings",
        "description": "Long interviews with investors and founders about how funds actually decide, how boards work, and what a raise looks like from both sides of the table.",
        "topics": ["venture", "fundraising", "interviews"],
        "language": "en",
    },
    "a16z": {
        "name": "Andreessen Horowitz",
        "description": "Talks from the a16z orbit on markets, AI, consumer products, and the mechanics of building a company that can take a category.",
        "topics": ["venture", "markets", "company-building"],
        "language": "en",
    },
    "aaronross": {
        "name": "Aaron Ross",
        "description": "Outbound sales system behind Predictable Revenue: specialized roles, cold outreach, and how a small team books meetings without a founder doing every call.",
        "topics": ["sales", "outbound", "gtm"],
        "language": "en",
    },
    "acquired": {
        "name": "Acquired",
        "description": "Company histories told as business case studies: how a firm found its wedge, survived a near-death, and compounded into a franchise.",
        "topics": ["case-studies", "strategy", "history"],
        "language": "en",
    },
    "andrew-chen": {
        "name": "Andrew Chen",
        "description": "Network effects and the cold-start problem, from the Uber growth years to marketplace expansion. Useful when you are asking how a product gets its first users and then does not stall.",
        "topics": ["growth", "marketplaces", "network-effects"],
        "language": "en",
    },
    "april-dunford": {
        "name": "April Dunford",
        "description": "Positioning talks: how to pick a market, name the alternatives, and stop sounding like every other B2B product in the category.",
        "topics": ["positioning", "gtm", "product"],
        "language": "en",
    },
    "april-dunford-blog": {
        "name": "April Dunford (writing)",
        "description": "Blog essays on positioning, sales narratives, and the difference between a feature list and a story a buyer can repeat.",
        "topics": ["positioning", "writing", "gtm"],
        "language": "en",
        "kind_default": "article",
    },
    "belfort": {
        "name": "Jordan Belfort",
        "description": "Straight-line persuasion, tonality, and the unglamorous parts of closing. Treat as a sales-craft corpus, not a morality guide.",
        "topics": ["sales", "persuasion", "closing"],
        "language": "en",
    },
    "brad-feld": {
        "name": "Brad Feld",
        "description": "Startup boards, venture partnering, and the Boulder thesis. Feld talks like an operator who has sat on both sides of the cap table.",
        "topics": ["venture", "boards", "founders"],
        "language": "en",
    },
    "brian-balfour": {
        "name": "Brian Balfour",
        "description": "Growth loops versus funnels, product-channel fit, and the path to a $100M product. Reforge-era thinking in talk form.",
        "topics": ["growth", "loops", "product"],
        "language": "en",
    },
    "chris-voss": {
        "name": "Chris Voss",
        "description": "Negotiation from the FBI playbook: calibrated questions, tactical empathy, no-oriented questions. Maps cleanly onto sales and partnership talks.",
        "topics": ["negotiation", "sales", "communication"],
        "language": "en",
    },
    "codyschneider": {
        "name": "Cody Schneider",
        "description": "Small e-commerce and side-business ideas with concrete unit economics. Useful as a foil to venture-scale advice.",
        "topics": ["ecommerce", "small-business", "ideas"],
        "language": "en",
    },
    "custdev": {
        "name": "Customer development (mixed)",
        "description": "A small mixed set of customer-development talks that did not land in a named series.",
        "topics": ["custdev", "interviews"],
        "language": "en",
    },
    "custdev-jtbd-moesta": {
        "name": "Jobs to Be Done (Bob Moesta)",
        "description": "Switch interviews, pushing and pulling forces, and the timeline of a buying decision. The practical JTBD corpus.",
        "topics": ["jtbd", "custdev", "interviews"],
        "language": "en",
    },
    "custdev-lennys": {
        "name": "Lenny's Podcast (custdev slice)",
        "description": "Lenny Rachitsky interviews that were pulled specifically for customer-development and product-market-fit craft.",
        "topics": ["product", "pmf", "custdev"],
        "language": "en",
    },
    "custdev-mfm": {
        "name": "My First Million (custdev slice)",
        "description": "Sam Parr and Shaan Puri riffing on businesses, distribution, and the weird ideas that actually print. Pulled for customer and market instinct, not for the bits.",
        "topics": ["ideas", "distribution", "small-business"],
        "language": "en",
    },
    "custdev-momtest": {
        "name": "The Mom Test",
        "description": "Rob Fitzpatrick's method for talking to users without fooling yourself: ask about their life, not your idea.",
        "topics": ["custdev", "interviews", "validation"],
        "language": "en",
    },
    "custdev-yc": {
        "name": "Y Combinator (custdev slice)",
        "description": "YC talks and office hours that were tagged for customer development: talking to users, finding a wedge, not scaling a ghost.",
        "topics": ["yc", "custdev", "early-stage"],
        "language": "en",
    },
    "dalio": {
        "name": "Ray Dalio",
        "description": "Principles, machine-like decision making, and how Bridgewater thinks about credit, cycles, and disagreement.",
        "topics": ["decision-making", "macro", "management"],
        "language": "en",
    },
    "dankoe": {
        "name": "Dan Koe",
        "description": "One-person internet businesses, writing as distribution, and building a personal media company without a headcount.",
        "topics": ["solopreneur", "content", "personal-brand"],
        "language": "en",
    },
    "danmartell": {
        "name": "Dan Martell",
        "description": "SaaS operations, buying back time, and the coaching lens on a founder who is the bottleneck.",
        "topics": ["saas", "operations", "founder-coach"],
        "language": "en",
    },
    "david-sacks": {
        "name": "David Sacks",
        "description": "Enterprise sales, PayPal mafia operating style, and later-stage company building. Mix of craft and punditry; the sales pieces are the ones to mine.",
        "topics": ["sales", "enterprise", "operating"],
        "language": "en",
    },
    "elena-verna": {
        "name": "Elena Verna",
        "description": "Growth operator talks: loops, self-serve, and what breaks when you bolt a growth team onto a sales-led company.",
        "topics": ["growth", "plg", "saas"],
        "language": "en",
    },
    "firstround": {
        "name": "First Round Capital",
        "description": "Review and Review-adjacent talks: early-stage operating advice from founders and the First Round network, denser than most VC content.",
        "topics": ["early-stage", "operating", "venture"],
        "language": "en",
    },
    "flywheel-founders": {
        "name": "Flywheels and network effects",
        "description": "A curated set around Jim Collins' flywheel, blitzscaling, Hooked, and marketplace cold starts. One of the better strategy packs in the corpus.",
        "topics": ["flywheel", "network-effects", "blitzscaling"],
        "language": "en",
    },
    "garyvee": {
        "name": "Gary Vaynerchuk",
        "description": "Attention, day-trading social platforms, and the unromantic work of posting. Loud, repetitive, and still a primary source on distribution as a skill.",
        "topics": ["distribution", "social", "attention"],
        "language": "en",
    },
    "girard": {
        "name": "Joe Girard",
        "description": "Old-school personal selling: follow-up, volume, and treating every customer as a future referral. A contrast to modern PLG talk.",
        "topics": ["sales", "referrals", "classic"],
        "language": "en",
    },
    "hormozi": {
        "name": "Alex Hormozi",
        "description": "Offers, pricing, and gym-to-software generalizations. Best mined for how he packages a promise, not for industry specifics.",
        "topics": ["offers", "pricing", "gtm"],
        "language": "en",
    },
    "kunal-shah": {
        "name": "Kunal Shah",
        "description": "CRED and the Indian consumer: trust, status, and why some products only work in a specific social stack.",
        "topics": ["india", "consumer", "trust"],
        "language": "en",
    },
    "lencioni": {
        "name": "Patrick Lencioni",
        "description": "Teams, meetings, and the five dysfunctions. Organizational craft rather than market craft.",
        "topics": ["teams", "management", "culture"],
        "language": "en",
    },
    "lennys-podcast": {
        "name": "Lenny's Podcast",
        "description": "Product, growth, and craft interviews. One of the densest modern sources on how good product orgs actually work.",
        "topics": ["product", "growth", "craft"],
        "language": "en",
    },
    "lochhead": {
        "name": "Christopher Lochhead",
        "description": "Category design: do not join a market, make one. Play Bigger in talk form.",
        "topics": ["category-design", "positioning", "strategy"],
        "language": "en",
    },
    "markroberge": {
        "name": "Mark Roberge",
        "description": "HubSpot's sales machine: hiring scorecards, onboarding ramps, and the handoff between inbound and outbound.",
        "topics": ["sales", "hiring", "saas"],
        "language": "en",
    },
    "marktilbury": {
        "name": "Mark Tilbury",
        "description": "Youth-facing money and small-business content. Lower signal than the operator talks, kept because it shows how business advice gets packaged for beginners.",
        "topics": ["personal-finance", "beginners", "side-hustle"],
        "language": "en",
    },
    "meddicc": {
        "name": "MEDDICC",
        "description": "Enterprise qualification: metrics, economic buyer, decision process, paper process, implicate the pain, champion. The standard B2B close framework.",
        "topics": ["sales", "enterprise", "qualification"],
        "language": "en",
    },
    "nfx": {
        "name": "NFX",
        "description": "The network-effects manual: types of nfx, defensibility, and why most 'community' products do not have one.",
        "topics": ["network-effects", "defensibility", "marketplaces"],
        "language": "en",
    },
    "paul-graham": {
        "name": "Paul Graham",
        "description": "Essays and talks on startups, wealth, and what YC selects for. The closest thing this corpus has to a canon.",
        "topics": ["yc", "essays", "early-stage"],
        "language": "en",
    },
    "productled": {
        "name": "ProductLed",
        "description": "Product-led growth teardowns, time-to-value, and what a self-serve motion looks like when it is not a slide.",
        "topics": ["plg", "onboarding", "saas"],
        "language": "en",
    },
    "profitwell": {
        "name": "ProfitWell / Paddle",
        "description": "Retention, pricing research, and SaaS metrics from Patrick Campbell's orbit.",
        "topics": ["pricing", "retention", "saas-metrics"],
        "language": "en",
    },
    "saastr": {
        "name": "SaaStr",
        "description": "Jason Lemkin and guests on the operating reality of B2B SaaS: sales hiring, burn, expansion, and the years after product-market fit.",
        "topics": ["saas", "sales", "operating"],
        "language": "en",
    },
    "sales-cognism": {
        "name": "Cognism",
        "description": "Modern B2B outbound: data, sequences, and how a sales-intel company teaches prospecting.",
        "topics": ["sales", "outbound", "b2b"],
        "language": "en",
    },
    "sales-miner": {
        "name": "Sales Miner",
        "description": "High-volume sales training clips. Noisy, repetitive, and still a usable sample of how outbound is taught at scale.",
        "topics": ["sales", "outbound", "training"],
        "language": "en",
    },
    "sales-patrickdang": {
        "name": "Patrick Dang",
        "description": "B2B closing and discovery, closer to SMB/mid-market than MEDDICC enterprise.",
        "topics": ["sales", "closing", "discovery"],
        "language": "en",
    },
    "sales-scripter": {
        "name": "Sales Scripter",
        "description": "Cold-call scripts, objection handling, and appointment setting. One of the largest slices in the corpus; treat it as a script library, not as strategy.",
        "topics": ["sales", "scripts", "cold-call"],
        "language": "en",
    },
    "sales-superhuman": {
        "name": "Superhuman selling",
        "description": "High-tempo sales training. Pair with the MEDDICC and Cognism sets if you are comparing methodologies.",
        "topics": ["sales", "training", "outbound"],
        "language": "en",
    },
    "sam-blond": {
        "name": "Sam Blond",
        "description": "Operator-level sales leadership: hiring AEs, forecasting, and running a team that does not live in the CRM.",
        "topics": ["sales", "leadership", "hiring"],
        "language": "en",
    },
    "stephfrance": {
        "name": "Steph France",
        "description": "Founder-facing growth: Meta ads tests, hidden SaaS niches, and later AI-agent use cases. Practical more than theoretical.",
        "topics": ["ads", "saas", "growth"],
        "language": "en",
    },
    "stratechery": {
        "name": "Stratechery (Ben Thompson)",
        "description": "Aggregation theory and the structural pieces behind consumer internet businesses. Short set, high density.",
        "topics": ["strategy", "aggregation", "platforms"],
        "language": "en",
    },
    "wolfofwallst": {
        "name": "Wolf of Wall Street (Belfort talks)",
        "description": "Another Belfort-branded slice of sales and persuasion talks, kept separate because it was collected as its own session.",
        "topics": ["sales", "persuasion", "closing"],
        "language": "en",
    },
    "yamalkevich": {
        "name": "Egor Yamalkevich",
        "description": "Russian-language founder talks from the VMSTE orbit: building in public, community, and the CIS path from employee to founder.",
        "topics": ["cis", "founders", "community"],
        "language": "ru",
    },
    "ycombinator": {
        "name": "Y Combinator",
        "description": "How to Start a Startup and later YC talks: the official early-stage playbook, from talking to users to not dying.",
        "topics": ["yc", "early-stage", "company-building"],
        "language": "en",
    },
}

PODCAST_SOURCES = {
    "custdev-indiehackers": {
        "id": "indie-hackers",
        "name": "Indie Hackers Podcast",
        "host": "Courtland Allen",
        "description": "Interviews with bootstrapped and mostly-bootstrapped founders who share revenue, distribution, and the unglamorous middle years. One of the best sources in this repo for pattern-hunting across many small businesses.",
        "topics": ["bootstrapped", "revenue", "interviews"],
        "language": "en",
        "homepage": "https://www.indiehackers.com/podcasts",
    },
    "custdev-practical-product": {
        "id": "practical-product",
        "name": "Practical Product",
        "host": "Jason Evanish",
        "description": "Product-management craft: first PM problems, specs people will read, hiring, and remote product leadership.",
        "topics": ["product", "pm", "hiring"],
        "language": "en",
    },
}

COMPANY_SOURCES = {
    "yc-companies": {
        "name": "Y Combinator companies",
        "description": "Public YC directory snapshot: name, batch, location, team size, tags, status. The cleanest structured company table in the set.",
        "origin": "https://www.ycombinator.com/companies",
        "license_note": "Public directory. Facts about companies; YC owns the presentation.",
    },
    "sec-edgar": {
        "name": "SEC EDGAR (Form D and related)",
        "description": "US private placement filings. Amounts, dates, and exemption types for companies raising under Regulation D.",
        "origin": "https://www.sec.gov/search-filings",
        "license_note": "US government public records.",
    },
    "fund-holdings": {
        "name": "Fund holdings inferred from Form D",
        "description": "Attempt to roll Form D filings up to funds and their recent deals. Many rows still have unresolved names; treat as a raw join table, not a finished Crunchbase.",
        "origin": "https://www.sec.gov/search-filings",
        "license_note": "Derived from US government public records.",
    },
    "companies-house": {
        "name": "UK Companies House",
        "description": "UK registered companies relevant to the collection: names, locations, and status from the public register.",
        "origin": "https://www.gov.uk/government/organisations/companies-house",
        "license_note": "UK Open Government Licence.",
    },
    "openbook-vc": {
        "name": "OpenVC / public fund profiles",
        "description": "Publicly listed funds with thesis, cheque size, and geography. Small but usable as a fund rolodex.",
        "origin": "https://www.openvc.app",
        "license_note": "Public profiles; original site owns the presentation.",
    },
    "product-hunt": {
        "name": "Product Hunt launches",
        "description": "A thin slice of product launches. Not a full PH dump; enough to join a launch date to a company.",
        "origin": "https://www.producthunt.com",
        "license_note": "Public launch pages.",
    },
    "techcrunch-rss": {
        "name": "TechCrunch funding RSS",
        "description": "Funding headlines from the TechCrunch feed, kept as a news tick, not as a complete round database.",
        "origin": "https://techcrunch.com",
        "license_note": "Headlines and links; full articles stay on TechCrunch.",
    },
    "cis-curated": {
        "name": "Hand-curated CIS / Israel / GCC lists",
        "description": "Small lists of notable Russian, Ukrainian, Israeli, and GCC tech companies plus CIS funds and accelerators. Hand-built, not scraped at scale.",
        "origin": "curated",
        "license_note": "Facts compiled from public sources.",
    },
    "corp-cis": {
        "name": "CIS corporates",
        "description": "Larger CIS tech and internet companies, used as incumbents against which startups in the region are compared.",
        "origin": "public company pages",
        "license_note": "Public company facts.",
    },
    "corp-eu": {
        "name": "European corporates",
        "description": "A short list of European incumbents for regional context.",
        "origin": "public company pages",
        "license_note": "Public company facts.",
    },
    "corp-giant": {
        "name": "Global giants",
        "description": "A handful of global tech incumbents, kept as reference points, not as a market map.",
        "origin": "public company pages",
        "license_note": "Public company facts.",
    },
    "corp-israel": {
        "name": "Israeli tech companies",
        "description": "Notable Israeli firms for the high-trust / deep-tech side of the regional set.",
        "origin": "public company pages",
        "license_note": "Public company facts.",
    },
    "corp-mena": {
        "name": "MENA corporates",
        "description": "A short MENA incumbent list for regional comparison.",
        "origin": "public company pages",
        "license_note": "Public company facts.",
    },
    "corp-midsize": {
        "name": "Mid-size corporates",
        "description": "Mid-size firms that sit between startup and giant. Useful when a founder story needs a realistic acquirer or competitor.",
        "origin": "public company pages",
        "license_note": "Public company facts.",
    },
    "geo-enrichment": {
        "name": "Geographic enrichment",
        "description": "Lat/lon and region tags joined onto companies in the set. Use it to plot, not as a gazetteer.",
        "origin": "derived",
        "license_note": "Derived from public location strings.",
    },
    "events": {
        "name": "Company events",
        "description": "A timeline of public signals (YC batch, recognition, and similar) keyed to company ids. Join to yc-companies and sec-edgar.",
        "origin": "derived from the company sources above",
        "license_note": "Derived from public records.",
    },
}

STARTER_STORY = {
    "id": "starter-story",
    "name": "Starter Story",
    "description": "Founder write-ups of real businesses: how the idea appeared, what it cost, what it earns, which channel worked. The structured metadata is often empty; the body text is where the numbers live. Original interviews remain copyright Starter Story; they are here for research and pattern analysis, with a link back to each page.",
    "homepage": "https://www.starterstory.com",
    "topics": ["bootstrapped", "case-studies", "revenue"],
    "language": "en",
}


def sanitize(name: str) -> str:
    name = name.replace("\x00", "")
    for ch in '<>:"|?*':
        name = name.replace(ch, "-")
    name = name.strip(" .")
    return name[:180] or "untitled"


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    raw = text[3:end]
    body = text[end + 4 :].lstrip("\n")
    meta: dict[str, str] = {}
    pending = None
    chunks: list[str] = []
    for line in raw.splitlines():
        if pending and (line.startswith("  ") or line.startswith("\t") or line == ""):
            chunks.append(line.strip())
            continue
        if pending:
            meta[pending] = " ".join(c for c in chunks if c)
            pending = None
            chunks = []
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if val in (">-", ">", "|", ""):
            pending = key
            chunks = []
        else:
            meta[key] = val
    if pending:
        meta[pending] = " ".join(c for c in chunks if c)
    return meta, body


def youtube_id(url: str | None) -> str | None:
    if not url:
        return None
    if "youtu.be/" in url:
        return url.split("youtu.be/", 1)[1].split("?", 1)[0].split("&", 1)[0]
    parsed = urllib.parse.urlparse(url)
    if "youtube.com" in parsed.netloc:
        qs = urllib.parse.parse_qs(parsed.query)
        if "v" in qs:
            return qs["v"][0]
        parts = parsed.path.strip("/").split("/")
        if parts and parts[0] in {"shorts", "embed", "live"} and len(parts) > 1:
            return parts[1]
    return None


def guess_kind(meta: dict, fallback: str) -> str:
    blob = " ".join(str(v) for v in meta.values()).lower()
    if "youtube" in blob:
        return "youtube_transcript"
    if "whisper" in blob or "podcast" in blob or "audio_url" in blob:
        return "podcast_transcript"
    if meta.get("extraction_method") == "blog" or fallback == "article":
        return "article"
    return fallback


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def ingest_youtube(docs: list[dict], sources_out: dict) -> dict:
    root = SOURCE_ROOT / "youtube-downloader" / "sessions"
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    stats = {"copied": 0, "skipped_dup": 0, "skipped_source": 0}
    sessions = sorted(p for p in root.iterdir() if p.is_dir())
    # Canonical folders first so merges lose to the main session.
    sessions.sort(key=lambda p: (p.name in MERGE_YOUTUBE, p.name))
    for session in sessions:
        raw_id = session.name
        if raw_id in SKIP_YOUTUBE:
            stats["skipped_source"] += 1
            continue
        source_id = MERGE_YOUTUBE.get(raw_id, raw_id)
        info = YOUTUBE_SOURCES.get(source_id, {
            "name": source_id.replace("-", " ").title(),
            "description": f"Collected talks filed under {source_id}.",
            "topics": ["business"],
            "language": "en",
        })
        sources_out[source_id] = {
            "id": source_id,
            "kind": "talks",
            **info,
        }
        dest_dir = REPO / "data" / "transcripts" / "youtube" / source_id
        for md in sorted(session.glob("*.md")):
            text = md.read_text(encoding="utf-8", errors="replace")
            meta, _ = parse_frontmatter(text)
            url = meta.get("source") or ""
            vid = youtube_id(url)
            dudupe_key = vid or sha(url or str(md))
            if dudupe_key in seen_ids:
                stats["skipped_dup"] += 1
                continue
            seen_ids.add(dudupe_key)
            filename = sanitize(md.name)
            rel = f"data/transcripts/youtube/{source_id}/{filename}"
            if rel in seen_paths:
                filename = f"{sanitize(md.stem)}-{dudupe_key[:8]}.md"
                rel = f"data/transcripts/youtube/{source_id}/{filename}"
            seen_paths.add(rel)
            copy_file(md, REPO / rel)
            kind = guess_kind(meta, info.get("kind_default", "youtube_transcript"))
            docs.append({
                "id": sha(rel),
                "kind": kind,
                "source_id": source_id,
                "title": meta.get("title") or md.stem,
                "url": url or None,
                "video_id": vid,
                "creator": meta.get("author") or info.get("host"),
                "date": meta.get("date") or None,
                "language": info.get("language", "en"),
                "topics": info.get("topics", []),
                "path": rel,
                "bytes": md.stat().st_size,
            })
            stats["copied"] += 1
    return stats


def ingest_podcasts(docs: list[dict], sources_out: dict) -> dict:
    root = SOURCE_ROOT / "podcast-transcriber" / "sessions"
    stats = {"copied": 0, "skipped_empty": 0}
    for session in sorted(p for p in root.iterdir() if p.is_dir()):
        files = list(session.glob("*.md"))
        if not files:
            stats["skipped_empty"] += 1
            continue
        info = PODCAST_SOURCES.get(session.name)
        if not info:
            info = {
                "id": session.name,
                "name": session.name,
                "description": f"Podcast session {session.name}.",
                "topics": ["podcast"],
                "language": "en",
            }
        source_id = info["id"]
        sources_out[source_id] = {"kind": "podcast", **info}
        for md in sorted(files):
            text = md.read_text(encoding="utf-8", errors="replace")
            meta, _ = parse_frontmatter(text)
            filename = sanitize(md.name)
            rel = f"data/transcripts/podcasts/{source_id}/{filename}"
            copy_file(md, REPO / rel)
            docs.append({
                "id": sha(rel),
                "kind": "podcast_transcript",
                "source_id": source_id,
                "title": meta.get("title") or md.stem,
                "url": meta.get("episode_url") or meta.get("source") or None,
                "audio_url": meta.get("audio_url") or None,
                "creator": meta.get("podcast") or info.get("host"),
                "date": meta.get("date") or None,
                "language": meta.get("language") or info.get("language", "en"),
                "topics": info.get("topics", []),
                "path": rel,
                "bytes": md.stat().st_size,
            })
            stats["copied"] += 1
    return stats


def ingest_starter_story(docs: list[dict], sources_out: dict) -> dict:
    root = SOURCE_ROOT / "starter-story-scrapper" / "output"
    sources_out["starter-story"] = {"kind": "founder-stories", **STARTER_STORY}
    stats = {"stories": 0, "ideas": 0, "ideas_deduped": 0}
    story_slugs: set[str] = set()

    for story_dir in sorted((root / "stories").iterdir()):
        if not story_dir.is_dir():
            continue
        meta_path = story_dir / "metadata.json"
        body_path = story_dir / "content.md"
        if not meta_path.exists() or not body_path.exists():
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        body = body_path.read_text(encoding="utf-8", errors="replace")
        slug = meta.get("slug") or story_dir.name
        story_slugs.add(slug.split("/")[-1])
        record = {
            **meta,
            "body_markdown": body,
            "collection": "stories",
        }
        rel = f"data/founder-stories/starter-story/stories/{sanitize(slug)}.json"
        dest = REPO / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        docs.append({
            "id": sha(rel),
            "kind": "founder_story",
            "source_id": "starter-story",
            "title": meta.get("title") or slug,
            "url": meta.get("url"),
            "slug": slug,
            "collection": "stories",
            "language": "en",
            "topics": STARTER_STORY["topics"],
            "path": rel,
            "bytes": dest.stat().st_size,
        })
        stats["stories"] += 1

    ideas_root = root / "ideas"
    if ideas_root.exists():
        for meta_path in sorted(ideas_root.rglob("metadata.json")):
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            body_path = meta_path.parent / "content.md"
            slug = (meta.get("slug") or meta_path.parent.name).split("/")[-1]
            if slug in story_slugs:
                stats["ideas_deduped"] += 1
                continue
            body = ""
            if body_path.exists():
                body = body_path.read_text(encoding="utf-8", errors="replace")
            category = meta.get("category") or meta_path.parent.parent.name
            record = {
                **meta,
                "body_markdown": body,
                "collection": "ideas",
                "category": category,
            }
            rel = f"data/founder-stories/starter-story/ideas/{sanitize(category)}/{sanitize(slug)}.json"
            dest = REPO / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            docs.append({
                "id": sha(rel),
                "kind": "founder_story",
                "source_id": "starter-story",
                "title": meta.get("title") or slug,
                "url": meta.get("url"),
                "slug": slug,
                "collection": "ideas",
                "category": category,
                "language": "en",
                "topics": STARTER_STORY["topics"] + ["ideas"],
                "path": rel,
                "bytes": dest.stat().st_size,
            })
            stats["ideas"] += 1
    return stats


def ingest_companies(docs: list[dict], sources_out: dict) -> dict:
    root = SOURCE_ROOT / "startup-data" / "data"
    stats: dict[str, int] = {}
    skip = {"reports"}
    for source_id, info in COMPANY_SOURCES.items():
        src_dir = root / source_id
        if not src_dir.exists():
            continue
        sources_out[source_id] = {"id": source_id, "kind": "structured", **info}
        dest_dir = REPO / "data" / "companies" / source_id
        dest_dir.mkdir(parents=True, exist_ok=True)
        count = 0
        if source_id == "events":
            for src in sorted(src_dir.glob("*.ndjson")):
                rel_name = src.name
                copy_file(src, dest_dir / rel_name)
                with src.open(encoding="utf-8") as fh:
                    for i, line in enumerate(fh):
                        if not line.strip():
                            continue
                        count += 1
                        if i == 0:
                            try:
                                sample = json.loads(line)
                            except json.JSONDecodeError:
                                sample = {}
                docs.append({
                    "id": sha(f"events/{src.name}"),
                    "kind": "event_shard",
                    "source_id": source_id,
                    "title": f"Events {src.stem}",
                    "url": None,
                    "path": f"data/companies/events/{src.name}",
                    "language": "en",
                    "topics": ["timeline"],
                    "bytes": src.stat().st_size,
                })
            stats[source_id] = count
            continue
        for src in sorted(src_dir.glob("*.json")):
            copy_file(src, dest_dir / src.name)
            try:
                payload = json.loads(src.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                payload = []
            n = len(payload) if isinstance(payload, list) else 1
            count += n
            docs.append({
                "id": sha(f"{source_id}/{src.name}"),
                "kind": "company_shard",
                "source_id": source_id,
                "title": f"{info['name']} / {src.name}",
                "url": info.get("origin"),
                "path": f"data/companies/{source_id}/{src.name}",
                "language": "en",
                "topics": ["companies"],
                "record_count": n,
                "bytes": src.stat().st_size,
            })
        stats[source_id] = count
    for extra in root.iterdir():
        if extra.name in skip or extra.name in COMPANY_SOURCES or not extra.is_dir():
            continue
        # ignore unknown dirs
    return stats


def write_outputs(docs: list[dict], sources_out: dict, extra_stats: dict) -> Path:
    catalog = REPO / "catalog"
    catalog.mkdir(parents=True, exist_ok=True)
    docs_path = catalog / "documents.jsonl"
    with docs_path.open("w", encoding="utf-8") as fh:
        for row in docs:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    sources_path = catalog / "sources.json"
    sources_path.write_text(
        json.dumps(sources_out, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    by_kind: dict[str, int] = {}
    by_source: dict[str, int] = {}
    total_bytes = 0
    for row in docs:
        by_kind[row["kind"]] = by_kind.get(row["kind"], 0) + 1
        by_source[row["source_id"]] = by_source.get(row["source_id"], 0) + 1
        total_bytes += int(row.get("bytes") or 0)
    summary = {
        "document_count": len(docs),
        "source_count": len(sources_out),
        "bytes": total_bytes,
        "by_kind": dict(sorted(by_kind.items())),
        "by_source": dict(sorted(by_source.items(), key=lambda kv: -kv[1])),
        "extra": extra_stats,
    }
    (catalog / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return catalog / "summary.json"


def main() -> int:
    if not SOURCE_ROOT.exists():
        print(f"missing SOURCE_ROOT: {SOURCE_ROOT}", file=sys.stderr)
        return 1
    docs: list[dict] = []
    sources_out: dict = {}
    print("youtube...")
    yt = ingest_youtube(docs, sources_out)
    print("  ", yt)
    print("podcasts...")
    pod = ingest_podcasts(docs, sources_out)
    print("  ", pod)
    print("founder stories...")
    ss = ingest_starter_story(docs, sources_out)
    print("  ", ss)
    print("companies...")
    co = ingest_companies(docs, sources_out)
    print("  ", co)
    summary_path = write_outputs(docs, sources_out, {"youtube": yt, "podcasts": pod, "starter_story": ss, "companies": co})
    print("wrote", summary_path)
    print("documents", len(docs), "sources", len(sources_out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
