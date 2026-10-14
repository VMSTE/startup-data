#!/usr/bin/env python3
"""Build the public book catalog and cleaned quotes. No full texts."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUOTES_SRC = Path(
    "/Users/wegorelax/Documents/sandbox/ais/data/books-downloader/data/quotes/shard-0000.json"
)

BOOKS = [
    {
        "id": "zero-to-one",
        "title": "Zero to One",
        "title_ru": "От нуля к единице",
        "authors": ["Peter Thiel", "Blake Masters"],
        "year": 2014,
        "topics": ["startups", "monopoly", "secrets"],
        "why": "Thiel's case for doing something new instead of scaling a copy. Useful next to the YC and a16z talks when you want the monopoly argument in one place.",
        "related_source_ids": ["ycombinator", "paul-graham", "a16z"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Zero_to_One",
            "open_library": "https://openlibrary.org/search?q=Zero+to+One+Thiel",
        },
    },
    {
        "id": "lean-startup",
        "title": "The Lean Startup",
        "title_ru": "Бизнес с нуля",
        "authors": ["Eric Ries"],
        "year": 2011,
        "topics": ["validation", "mvp", "early-stage"],
        "why": "Build-measure-learn as a loop. The default vocabulary for 'don't scale a ghost' in this corpus.",
        "related_source_ids": ["ycombinator", "custdev-momtest", "custdev-yc"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Lean_Startup",
            "open_library": "https://openlibrary.org/search?q=The+Lean+Startup+Ries",
        },
    },
    {
        "id": "hard-thing-about-hard-things",
        "title": "The Hard Thing About Hard Things",
        "title_ru": "Легко не будет",
        "authors": ["Ben Horowitz"],
        "year": 2014,
        "topics": ["operating", "ceo", "wartime"],
        "why": "The ugly middle: firing, peacetime vs wartime CEO, not dying. Pair with First Round and SaaStr operating talks.",
        "related_source_ids": ["firstround", "a16z", "saastr"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Hard_Thing_About_Hard_Things",
            "open_library": "https://openlibrary.org/search?q=Hard+Thing+About+Hard+Things+Horowitz",
        },
    },
    {
        "id": "cold-start-problem",
        "title": "The Cold Start Problem",
        "title_ru": "Проблема холодного старта",
        "authors": ["Andrew Chen"],
        "year": 2021,
        "topics": ["network-effects", "marketplaces", "growth"],
        "why": "How a network gets its first users and then does not stall. The book behind the Andrew Chen / NFX / flywheel talks already in the transcript set.",
        "related_source_ids": ["andrew-chen", "nfx", "flywheel-founders"],
        "links": {
            "open_library": "https://openlibrary.org/search?q=The+Cold+Start+Problem+Andrew+Chen",
            "author": "https://andrewchen.com/the-cold-start-problem/",
        },
    },
    {
        "id": "blitzscaling",
        "title": "Blitzscaling",
        "title_ru": "Блиц-масштабирование",
        "authors": ["Reid Hoffman", "Chris Yeh"],
        "year": 2018,
        "topics": ["scale", "growth", "hiring"],
        "why": "When to prioritize speed over efficiency. The flywheel-founders session already has the Stanford blitzscaling lectures; this is the book form.",
        "related_source_ids": ["flywheel-founders", "ycombinator"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Blitzscaling",
            "open_library": "https://openlibrary.org/search?q=Blitzscaling+Hoffman",
        },
    },
    {
        "id": "crossing-the-chasm",
        "title": "Crossing the Chasm",
        "title_ru": "Преодоление пропасти",
        "authors": ["Geoffrey A. Moore"],
        "year": 1991,
        "topics": ["gtm", "early-adopters", "b2b"],
        "why": "Why a product that delights enthusiasts still dies in the mainstream. Still the map for B2B category passage.",
        "related_source_ids": ["april-dunford", "lochhead", "productled"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Crossing_the_Chasm",
            "open_library": "https://openlibrary.org/search?q=Crossing+the+Chasm+Moore",
        },
    },
    {
        "id": "innovators-dilemma",
        "title": "The Innovator's Dilemma",
        "title_ru": "Дилемма инноватора",
        "authors": ["Clayton M. Christensen"],
        "year": 1997,
        "topics": ["disruption", "incumbents", "strategy"],
        "why": "Why good companies miss the next curve. Read it as a warning about listening only to today's best customers.",
        "related_source_ids": ["stratechery", "a16z"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Innovator%27s_Dilemma",
            "open_library": "https://openlibrary.org/search?q=Innovators+Dilemma+Christensen",
        },
    },
    {
        "id": "hooked",
        "title": "Hooked",
        "title_ru": "На крючке",
        "authors": ["Nir Eyal"],
        "year": 2014,
        "topics": ["habits", "product", "growth"],
        "why": "Trigger-action-reward-investment. The habit loop that sits under a lot of consumer growth talk in the flywheel set.",
        "related_source_ids": ["flywheel-founders", "brian-balfour"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Hooked_(book)",
            "open_library": "https://openlibrary.org/search?q=Hooked+Nir+Eyal",
        },
    },
    {
        "id": "contagious",
        "title": "Contagious",
        "title_ru": "Заразительный",
        "authors": ["Jonah Berger"],
        "year": 2013,
        "topics": ["distribution", "word-of-mouth", "growth"],
        "why": "Why some things get talked about. STEPPS as a checklist, not as a growth department.",
        "related_source_ids": ["flywheel-founders", "garyvee"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Contagious:_Why_Things_Catch_On",
            "open_library": "https://openlibrary.org/search?q=Contagious+Jonah+Berger",
        },
    },
    {
        "id": "hacking-growth",
        "title": "Hacking Growth",
        "title_ru": "Взлом роста",
        "authors": ["Sean Ellis", "Morgan Brown"],
        "year": 2017,
        "topics": ["growth", "loops", "experimentation"],
        "why": "The growth-team version of build-measure-learn. Pair with Brian Balfour and Elena Verna talks.",
        "related_source_ids": ["brian-balfour", "elena-verna", "flywheel-founders"],
        "links": {
            "open_library": "https://openlibrary.org/search?q=Hacking+Growth+Sean+Ellis",
        },
    },
    {
        "id": "platform-revolution",
        "title": "Platform Revolution",
        "title_ru": "Революция платформ",
        "authors": ["Geoffrey G. Parker", "Marshall W. Van Alstyne", "Sangeet Paul Choudary"],
        "year": 2016,
        "topics": ["platforms", "network-effects", "marketplaces"],
        "why": "How multi-sided markets create and capture value. Complements Chen and NFX on the economics, not the cold-start tactics.",
        "related_source_ids": ["andrew-chen", "nfx", "stratechery"],
        "links": {
            "open_library": "https://openlibrary.org/search?q=Platform+Revolution+Parker",
        },
    },
    {
        "id": "hormozi-100m-offers",
        "title": "$100M Offers",
        "title_ru": "$100M Offers",
        "authors": ["Alex Hormozi"],
        "year": 2021,
        "topics": ["offers", "pricing", "gtm"],
        "why": "Value equation, grand-slam offer, guarantees. The densest offer-crafting book in the set; the Hormozi talks repeat it out loud.",
        "related_source_ids": ["hormozi"],
        "links": {
            "author": "https://www.acquisition.com/training/offers",
            "open_library": "https://openlibrary.org/search?q=100M+Offers+Hormozi",
        },
    },
    {
        "id": "influence",
        "title": "Influence",
        "title_ru": "Психология влияния",
        "authors": ["Robert Cialdini"],
        "year": 1984,
        "topics": ["persuasion", "sales", "psychology"],
        "why": "Reciprocity, commitment, social proof, authority, liking, scarcity. The shared language under a lot of the sales-training slice.",
        "related_source_ids": ["hormozi", "girard", "sales-scripter"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Influence:_The_Psychology_of_Persuasion",
            "open_library": "https://openlibrary.org/search?q=Influence+Cialdini",
        },
    },
    {
        "id": "mom-test",
        "title": "The Mom Test",
        "title_ru": "Спроси маму",
        "authors": ["Rob Fitzpatrick"],
        "year": 2013,
        "topics": ["custdev", "interviews", "validation"],
        "why": "How to talk to users without fooling yourself. The custdev-momtest session is the talk form of this book.",
        "related_source_ids": ["custdev-momtest", "custdev-yc", "indie-hackers"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Mom_Test",
            "author": "https://www.momtestbook.com/",
        },
    },
    {
        "id": "spin-selling",
        "title": "SPIN Selling",
        "title_ru": "SPIN-продажи",
        "authors": ["Neil Rackham"],
        "year": 1988,
        "topics": ["sales", "discovery", "enterprise"],
        "why": "Situation-Problem-Implication-Need-payoff. Older than MEDDICC, still the discovery spine a lot of B2B teams use.",
        "related_source_ids": ["meddicc", "markroberge", "sales-patrickdang"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/SPIN_selling",
            "open_library": "https://openlibrary.org/search?q=SPIN+Selling+Rackham",
        },
    },
    {
        "id": "challenger-sale",
        "title": "The Challenger Sale",
        "title_ru": "Чемпионы продаж",
        "authors": ["Matthew Dixon", "Brent Adamson"],
        "year": 2011,
        "topics": ["sales", "enterprise", "teaching"],
        "why": "Teach, tailor, take control. The alternative to relationship-only selling in complex B2B.",
        "related_source_ids": ["meddicc", "saastr", "markroberge"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Challenger_Sale",
            "open_library": "https://openlibrary.org/search?q=Challenger+Sale+Dixon",
        },
    },
    {
        "id": "fanatical-prospecting",
        "title": "Fanatical Prospecting",
        "title_ru": "Фанатичные продажи",
        "authors": ["Jeb Blount"],
        "year": 2015,
        "topics": ["sales", "outbound", "prospecting"],
        "why": "Volume and cadence of outbound. Explains the sales-scripter / Cognism slice better than those clips explain themselves.",
        "related_source_ids": ["sales-cognism", "sales-scripter", "aaronross"],
        "links": {
            "open_library": "https://openlibrary.org/search?q=Fanatical+Prospecting+Blount",
        },
    },
    {
        "id": "how-to-sell-anything",
        "title": "How to Sell Anything to Anybody",
        "title_ru": "Как продать что угодно кому угодно",
        "authors": ["Joe Girard"],
        "year": 1977,
        "topics": ["sales", "referrals", "classic"],
        "why": "Law of 250, follow-up, treating every buyer as a future referral. The girard talks are this book spoken.",
        "related_source_ids": ["girard"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/How_to_Sell_Anything_to_Anybody",
            "open_library": "https://openlibrary.org/search?q=How+to+Sell+Anything+to+Anybody+Girard",
        },
    },
    {
        "id": "good-strategy-bad-strategy",
        "title": "Good Strategy/Bad Strategy",
        "title_ru": "Хорошая стратегия, плохая стратегия",
        "authors": ["Richard Rumelt"],
        "year": 2011,
        "topics": ["strategy", "diagnosis", "kernel"],
        "why": "Diagnosis, guiding policy, coherent action. The cleanest test for whether a 'strategy' is just a list of goals.",
        "related_source_ids": ["stratechery", "lochhead"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Good_Strategy/Bad_Strategy",
            "open_library": "https://openlibrary.org/search?q=Good+Strategy+Bad+Strategy+Rumelt",
        },
    },
    {
        "id": "playing-to-win",
        "title": "Playing to Win",
        "title_ru": "Игра на победу",
        "authors": ["A.G. Lafley", "Roger L. Martin"],
        "year": 2013,
        "topics": ["strategy", "where-to-play", "how-to-win"],
        "why": "The five strategy questions from P&G. Useful when a founder story never names a where-to-play choice.",
        "related_source_ids": ["april-dunford", "lochhead"],
        "links": {
            "open_library": "https://openlibrary.org/search?q=Playing+to+Win+Lafley+Martin",
        },
    },
    {
        "id": "blue-ocean-strategy",
        "title": "Blue Ocean Strategy",
        "title_ru": "Стратегия голубого океана",
        "authors": ["W. Chan Kim", "Renée Mauborgne"],
        "year": 2005,
        "topics": ["strategy", "category-design", "competition"],
        "why": "Value innovation and making a market instead of joining one. Overlap with Lochhead's category design talks.",
        "related_source_ids": ["lochhead", "april-dunford"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Blue_Ocean_Strategy",
            "open_library": "https://openlibrary.org/search?q=Blue+Ocean+Strategy+Kim",
        },
    },
    {
        "id": "competitive-strategy",
        "title": "Competitive Strategy",
        "title_ru": "Конкурентная стратегия",
        "authors": ["Michael E. Porter"],
        "year": 1980,
        "topics": ["strategy", "industry", "five-forces"],
        "why": "Five forces and generic strategies. The industry-structure baseline everything later either uses or argues with.",
        "related_source_ids": ["stratechery"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Competitive_Strategy",
            "open_library": "https://openlibrary.org/search?q=Competitive+Strategy+Porter",
        },
    },
    {
        "id": "only-the-paranoid-survive",
        "title": "Only the Paranoid Survive",
        "title_ru": "Выживают только параноики",
        "authors": ["Andrew S. Grove"],
        "year": 1996,
        "topics": ["inflection", "operating", "intel"],
        "why": "Strategic inflection points from the Intel years. How an operator notices the ground moving.",
        "related_source_ids": ["firstround", "a16z"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Only_the_Paranoid_Survive",
            "open_library": "https://openlibrary.org/search?q=Only+the+Paranoid+Survive+Grove",
        },
    },
    {
        "id": "art-of-strategy",
        "title": "The Art of Strategy",
        "title_ru": "Стратегические игры",
        "authors": ["Avinash K. Dixit", "Barry J. Nalebuff"],
        "year": 2008,
        "topics": ["game-theory", "strategy", "negotiation"],
        "why": "Game theory for people who run businesses, not for exam questions. Complements Voss on the other side of a negotiation.",
        "related_source_ids": ["chris-voss"],
        "links": {
            "open_library": "https://openlibrary.org/search?q=The+Art+of+Strategy+Dixit+Nalebuff",
        },
    },
    {
        "id": "venture-deals",
        "title": "Venture Deals",
        "title_ru": "Venture Deals",
        "authors": ["Brad Feld", "Jason Mendelson"],
        "year": 2011,
        "topics": ["venture", "term-sheets", "fundraising"],
        "why": "How a term sheet is built. Pair with the Brad Feld talks and 20VC fundraising interviews.",
        "related_source_ids": ["brad-feld", "20vc", "ycombinator"],
        "links": {
            "open_library": "https://openlibrary.org/search?q=Venture+Deals+Feld+Mendelson",
            "author": "https://www.venturedeals.com/",
        },
    },
    {
        "id": "intelligent-investor",
        "title": "The Intelligent Investor",
        "title_ru": "Разумный инвестор",
        "authors": ["Benjamin Graham"],
        "year": 1949,
        "topics": ["investing", "value", "margin-of-safety"],
        "why": "Mr. Market and margin of safety. In this corpus it is background for how operators talk about not overpaying, not a trading manual.",
        "related_source_ids": ["dalio"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Intelligent_Investor",
            "open_library": "https://openlibrary.org/search?q=The+Intelligent+Investor+Graham",
        },
    },
    {
        "id": "buffett-essays",
        "title": "The Essays of Warren Buffett",
        "title_ru": "Эссе Уоррена Баффетта",
        "authors": ["Warren Buffett", "Lawrence A. Cunningham"],
        "year": 1997,
        "topics": ["investing", "capital-allocation", "governance"],
        "why": "Capital allocation in plain language. Useful next to Thorndike's Outsiders.",
        "related_source_ids": [],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Essays_of_Warren_Buffett",
            "open_library": "https://openlibrary.org/search?q=Essays+of+Warren+Buffett+Cunningham",
        },
    },
    {
        "id": "little-book-that-beats-the-market",
        "title": "The Little Book That Beats the Market",
        "title_ru": "Маленькая книга победителя рынка акций",
        "authors": ["Joel Greenblatt"],
        "year": 2005,
        "topics": ["investing", "magic-formula", "value"],
        "why": "A simple quality-plus-cheap screen. In the set as a foil to venture storytelling: some capital is allocated by formula.",
        "related_source_ids": [],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Little_Book_That_Beats_the_Market",
            "open_library": "https://openlibrary.org/search?q=Little+Book+That+Beats+the+Market+Greenblatt",
        },
    },
    {
        "id": "why-nations-fail",
        "title": "Why Nations Fail",
        "title_ru": "Почему одни страны богатые, а другие бедные",
        "authors": ["Daron Acemoglu", "James A. Robinson"],
        "year": 2012,
        "topics": ["institutions", "markets", "trust"],
        "why": "Inclusive vs extractive institutions. Context for CIS / low-trust market conversations, not a startup playbook.",
        "related_source_ids": ["kunal-shah", "yamalkevich"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Why_Nations_Fail",
            "open_library": "https://openlibrary.org/search?q=Why+Nations+Fail+Acemoglu",
        },
    },
    {
        "id": "mystery-of-capital",
        "title": "The Mystery of Capital",
        "title_ru": "Загадка капитала",
        "authors": ["Hernando de Soto"],
        "year": 2000,
        "topics": ["property", "informal-economy", "institutions"],
        "why": "Why assets that people already use still cannot become capital. Same regional lens as Why Nations Fail.",
        "related_source_ids": ["kunal-shah"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Mystery_of_Capital",
            "open_library": "https://openlibrary.org/search?q=Mystery+of+Capital+de+Soto",
        },
    },
    {
        "id": "five-dysfunctions",
        "title": "The Five Dysfunctions of a Team",
        "title_ru": "Пять пороков команды",
        "authors": ["Patrick Lencioni"],
        "year": 2002,
        "topics": ["teams", "trust", "management"],
        "why": "Trust, conflict, commitment, accountability, results. The Lencioni talks in the transcript set are this model repeated.",
        "related_source_ids": ["lencioni"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Five_Dysfunctions_of_a_Team",
            "open_library": "https://openlibrary.org/search?q=Five+Dysfunctions+of+a+Team+Lencioni",
        },
    },
    {
        "id": "measure-what-matters",
        "title": "Measure What Matters",
        "title_ru": "Измеряйте самое важное",
        "authors": ["John Doerr"],
        "year": 2018,
        "topics": ["okrs", "management", "goals"],
        "why": "OKRs as Intel and Google used them. How a company says what this quarter is for.",
        "related_source_ids": ["ycombinator", "firstround"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Measure_What_Matters",
            "open_library": "https://openlibrary.org/search?q=Measure+What+Matters+Doerr",
        },
    },
    {
        "id": "principles",
        "title": "Principles",
        "title_ru": "Принципы. Жизнь и работа",
        "authors": ["Ray Dalio"],
        "year": 2017,
        "topics": ["decision-making", "management", "culture"],
        "why": "Idea meritocracy and pain-plus-reflection. The dalio talks are the short form.",
        "related_source_ids": ["dalio"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Principles_(book)",
            "open_library": "https://openlibrary.org/search?q=Principles+Ray+Dalio",
        },
    },
    {
        "id": "team-of-teams",
        "title": "Team of Teams",
        "title_ru": "Команда команд",
        "authors": ["Stanley McChrystal"],
        "year": 2015,
        "topics": ["org-design", "trust", "decentralization"],
        "why": "Shared consciousness and empowered execution. How a large org still moves when the map changes weekly.",
        "related_source_ids": ["lencioni"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Team_of_Teams",
            "open_library": "https://openlibrary.org/search?q=Team+of+Teams+McChrystal",
        },
    },
    {
        "id": "turn-the-ship-around",
        "title": "Turn the Ship Around!",
        "title_ru": "Разверните ваш корабль",
        "authors": ["L. David Marquet"],
        "year": 2012,
        "topics": ["leadership", "intent", "navy"],
        "why": "Leader-leader instead of leader-follower. Intent-based execution from a submarine, mapped onto company teams.",
        "related_source_ids": ["lencioni"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Turn_the_Ship_Around!",
            "open_library": "https://openlibrary.org/search?q=Turn+the+Ship+Around+Marquet",
        },
    },
    {
        "id": "no-rules-rules",
        "title": "No Rules Rules",
        "title_ru": "Никаких правил",
        "authors": ["Reed Hastings", "Erin Meyer"],
        "year": 2020,
        "topics": ["culture", "netflix", "talent"],
        "why": "Density of talent, candor, and the keeper test. One company's culture written as an operating system.",
        "related_source_ids": ["flywheel-founders"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/No_Rules_Rules",
            "open_library": "https://openlibrary.org/search?q=No+Rules+Rules+Hastings",
        },
    },
    {
        "id": "toyota-way",
        "title": "The Toyota Way",
        "title_ru": "Дао Toyota",
        "authors": ["Jeffrey K. Liker"],
        "year": 2004,
        "topics": ["operations", "lean", "quality"],
        "why": "The 14 principles behind Toyota production. Operations craft, not a startup origin story.",
        "related_source_ids": [],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Toyota_Way",
            "open_library": "https://openlibrary.org/search?q=The+Toyota+Way+Liker",
        },
    },
    {
        "id": "outsiders",
        "title": "The Outsiders",
        "title_ru": "Аутсайдеры / Правила лучших CEO",
        "authors": ["William N. Thorndike"],
        "year": 2012,
        "topics": ["capital-allocation", "ceo", "compounding"],
        "why": "Eight CEOs judged by capital allocation, not charisma. A different success metric than blitzscaling.",
        "related_source_ids": [],
        "links": {
            "open_library": "https://openlibrary.org/search?q=The+Outsiders+Thorndike",
        },
    },
    {
        "id": "shoe-dog",
        "title": "Shoe Dog",
        "title_ru": "Продавец обуви",
        "authors": ["Phil Knight"],
        "year": 2016,
        "topics": ["memoir", "brand", "cash"],
        "why": "Nike's early years as a cash and distribution problem. A founder memoir that is more useful on working capital than on slogans.",
        "related_source_ids": ["acquired"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Shoe_Dog",
            "open_library": "https://openlibrary.org/search?q=Shoe+Dog+Phil+Knight",
        },
    },
    {
        "id": "alibaba-world",
        "title": "Alibaba's World",
        "title_ru": "Alibaba. История мирового восхождения от первого лица",
        "authors": ["Porter Erisman"],
        "year": 2015,
        "topics": ["memoir", "china", "platforms"],
        "why": "An insider account of Alibaba before the IPO. Regional case, not a US SaaS playbook.",
        "related_source_ids": ["acquired"],
        "links": {
            "open_library": "https://openlibrary.org/search?q=Alibaba%27s+World+Erisman",
        },
    },
    {
        "id": "design-of-everyday-things",
        "title": "The Design of Everyday Things",
        "title_ru": "Дизайн привычных вещей",
        "authors": ["Don Norman"],
        "year": 1988,
        "topics": ["product", "ux", "affordances"],
        "why": "Affordances, signifiers, error. Why a product feels obvious or hostile, independent of growth loops.",
        "related_source_ids": ["productled"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/The_Design_of_Everyday_Things",
            "open_library": "https://openlibrary.org/search?q=Design+of+Everyday+Things+Norman",
        },
    },
    {
        "id": "thinking-in-bets",
        "title": "Thinking in Bets",
        "title_ru": "Принцип ставок",
        "authors": ["Annie Duke"],
        "year": 2018,
        "topics": ["decision-making", "uncertainty", "poker"],
        "why": "Resulting vs decision quality. A founder-facing way to talk about bets without pretending the outcome was knowable.",
        "related_source_ids": ["dalio"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Thinking_in_Bets",
            "open_library": "https://openlibrary.org/search?q=Thinking+in+Bets+Annie+Duke",
        },
    },
    {
        "id": "predictably-irrational",
        "title": "Predictably Irrational",
        "title_ru": "Предсказуемая иррациональность",
        "authors": ["Dan Ariely"],
        "year": 2008,
        "topics": ["psychology", "pricing", "behavior"],
        "why": "How people misjudge price, relativity, and free. Background for offer and pricing talk.",
        "related_source_ids": ["hormozi", "profitwell"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Predictably_Irrational",
            "open_library": "https://openlibrary.org/search?q=Predictably+Irrational+Ariely",
        },
    },
    {
        "id": "antifragile",
        "title": "Antifragile",
        "title_ru": "Антихрупкость",
        "authors": ["Nassim Nicholas Taleb"],
        "year": 2012,
        "topics": ["uncertainty", "optionality", "risk"],
        "why": "Systems that gain from disorder. In this corpus it is a lens on optionality, not a market-timing guide.",
        "related_source_ids": ["dalio"],
        "links": {
            "wikipedia": "https://en.wikipedia.org/wiki/Antifragile",
            "open_library": "https://openlibrary.org/search?q=Antifragile+Taleb",
        },
    },
]

QUOTE_BOOK = {
    "«От нуля к единице»": "zero-to-one",
    "$100M Offers": "hormozi-100m-offers",
    "«Как продать что угодно кому угодно»": "how-to-sell-anything",
    "Психология влияния (Influence)": "influence",
}

GROUPS = [
    ("Company building", [
        "zero-to-one", "lean-startup", "hard-thing-about-hard-things",
        "cold-start-problem", "blitzscaling", "crossing-the-chasm",
        "innovators-dilemma",
    ]),
    ("Growth and distribution", [
        "hooked", "contagious", "hacking-growth", "platform-revolution",
    ]),
    ("Offers, sales, customer development", [
        "hormozi-100m-offers", "influence", "mom-test", "spin-selling",
        "challenger-sale", "fanatical-prospecting", "how-to-sell-anything",
    ]),
    ("Strategy", [
        "good-strategy-bad-strategy", "playing-to-win", "blue-ocean-strategy",
        "competitive-strategy", "only-the-paranoid-survive", "art-of-strategy",
    ]),
    ("Capital and institutions", [
        "venture-deals", "intelligent-investor", "buffett-essays",
        "little-book-that-beats-the-market", "why-nations-fail",
        "mystery-of-capital",
    ]),
    ("Organizations", [
        "five-dysfunctions", "measure-what-matters", "principles",
        "team-of-teams", "turn-the-ship-around", "no-rules-rules",
        "toyota-way", "outsiders",
    ]),
    ("Founder books and adjacent", [
        "shoe-dog", "alibaba-world", "design-of-everyday-things",
        "thinking-in-bets", "predictably-irrational", "antifragile",
    ]),
]


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"</?em>", "", text)
    text = text.replace("…", "...")
    return text.strip()


def load_quotes() -> list[dict]:
    raw = json.loads(QUOTES_SRC.read_text(encoding="utf-8"))
    seen: set[tuple[str, str]] = set()
    out: list[dict] = []
    counts: dict[str, int] = {}
    for row in raw:
        book_id = QUOTE_BOOK.get(row["bookTitle"])
        if not book_id:
            continue
        text = clean_text(row["text"])
        key = (book_id, text)
        if key in seen:
            continue
        seen.add(key)
        theme = row.get("theme") or ""
        theme = re.sub(r"^T\d+-", "", theme)
        counts[book_id] = counts.get(book_id, 0) + 1
        out.append({
            "id": f"{book_id}:{theme}:{counts[book_id]}",
            "book_id": book_id,
            "theme": theme,
            "text": text,
            "citation": row.get("citation"),
            "year": row.get("bookYear"),
        })
    return out


def write_books_md(books: list[dict], quote_count: int) -> str:
    by_id = {b["id"]: b for b in books}
    lines = [
        "# Books",
        "",
        "This is a reading list, not a library. Each entry is a book that showed up in the local cache we used while building this corpus. We publish the catalog and a handful of short quotes. We do not publish the files.",
        "",
        "Links go to Wikipedia, Open Library, or the author's page. That is enough to find a legal copy. We do not link to pirate mirrors.",
        "",
        f"{len(books)} books. {quote_count} quotes in `data/books/quotes.json`.",
        "",
        "Machine-readable catalog: [`data/books/catalog.json`](data/books/catalog.json).",
        "",
    ]
    for heading, ids in GROUPS:
        lines.append(f"## {heading}")
        lines.append("")
        for bid in ids:
            b = by_id[bid]
            authors = ", ".join(b["authors"])
            lines.append(f"### {b['title']} ({b['year']})")
            lines.append("")
            lines.append(f"{authors}. Russian title in the cache: {b['title_ru']}.")
            lines.append("")
            lines.append(b["why"])
            lines.append("")
            link_bits = []
            for label, url in b["links"].items():
                link_bits.append(f"[{label.replace('_', ' ')}]({url})")
            lines.append("Find it: " + " | ".join(link_bits) + ".")
            if b.get("related_source_ids"):
                rel = ", ".join(f"`{s}`" for s in b["related_source_ids"])
                lines.append("")
                lines.append(f"Related talks in this repo: {rel}.")
            lines.append("")
    lines.append("## What we left out")
    lines.append("")
    lines.append("The same cache had psychotherapy novels (Irvin Yalom), Jordan Peterson, and a few other titles that are not startup or business strategy. They stay out of this list.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    dest = ROOT / "data" / "books"
    dest.mkdir(parents=True, exist_ok=True)
    quotes = load_quotes()
    catalog = []
    for b in BOOKS:
        catalog.append({
            **b,
            "quote_count": sum(1 for q in quotes if q["book_id"] == b["id"]),
        })
    (dest / "catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (dest / "quotes.json").write_text(
        json.dumps(quotes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "BOOKS.md").write_text(write_books_md(catalog, len(quotes)), encoding="utf-8")
    print(f"books {len(catalog)} quotes {len(quotes)}")


if __name__ == "__main__":
    main()
