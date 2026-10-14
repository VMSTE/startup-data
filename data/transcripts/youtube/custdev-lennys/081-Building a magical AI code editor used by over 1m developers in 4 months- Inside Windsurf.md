---
source: https://www.youtube.com/watch?v=5Z0RCxDZdrE
title: "Building a magical AI code editor used by over 1m developers in 4
  months: Inside Windsurf"
author: Lenny's Podcast
date: 2025-04-20
views: 64002
description: |-
  Varun Mohan is the co-founder and CEO of Windsurf (formerly Codeium), an AI-powered development environment (IDE) that has been used by over 1 million developers in just four months and has quickly emerged as a leader in transforming how developers build software. Prior to finding success with Windsurf, the company pivoted twice—first from GPU virtualization infrastructure to an IDE plugin, and then to their own standalone IDE.

  In this conversation, you'll learn:
  1. Why Windsurf walked away from a profitable GPU infrastructure business and bet the company on helping engineers code
  2. The surprising UI discovery that tripled adoption rates overnight
  3. The secret behind Windsurf's B2B enterprise plan, and why they invested early in an 80-person sales team despite conventional startup wisdom
  4. How non-technical staff at Windsurf built their own custom tools instead of purchasing SaaS products, saving them over $500k in software costs
  5. Why Varun believes 90% of code will be AI-generated, but engineering jobs will actually increase
  6. How training on millions of incomplete code samples gives Windsurf an edge, and creates a moat long-term
  7. Why agency is the most undervalued and important skill in the AI era

  Transcript: https://www.lennysnewsletter.com/p/the-untold-story-of-windsurf-varun-mohan

  Brought to you by:
  Brex—The banking solution for startups: https://www.brex.com/product/business-account?ref_code=bmk_dp_brand1H25_ln_new_fs
  Productboard—Make products that matter: https://www.productboard.com/lenny
  Coda—The all-in-one collaborative workspace: https://coda.io/lenny

  Where to find Varun Mohan:
  • X: https://x.com/_mohansolo
  • LinkedIn: https://www.linkedin.com/in/varunkmohan/

  Where to find Lenny:
  • Newsletter: https://www.lennysnewsletter.com
  • X: https://twitter.com/lennysan
  • LinkedIn: https://www.linkedin.com/in/lennyrachitsky/

  In this episode, we cover:
  (00:00) Varun’s background
  (03:57) Building and scaling Windsurf
  (12:58) Windsurf: The new purpose-built IDE to harness magic
  (17:11) The future of engineering and AI
  (21:30) Skills worth investing in
  (23:07) Hiring philosophy and company culture
  (35:22) Sales strategy and market position
  (39:37) JetBrains vs. VS Code: extensibility and enterprise adoption
  (41:20) Live demo: building an Airbnb for dogs with Windsurf
  (42:46) Tips for using Windsurf effectively
  (46:38) AI’s role in code modification and review
  (48:56) Empowering non-developers to build custom software
  (54:03) Training Windsurf  
  (01:00:43) Windsurf’s unique team structure and product strategy
  (01:06:40) The importance of continuous innovation
  (01:08:57) Final thoughts and advice for aspiring developers

  Referenced:
  • Windsurf: https://windsurf.com/
  • VS Code: https://code.visualstudio.com/
  • JetBrains: https://www.jetbrains.com/
  • Eclipse: https://eclipseide.org/
  • Visual Studio: https://visualstudio.microsoft.com/
  • Vim: https://www.vim.org/
  • Emacs: https://www.gnu.org/software/emacs/
  • Lessons from a two-time unicorn builder, 50-time startup advisor, and 20-time company board member | Uri Levine (co-founder of Waze): https://www.lennysnewsletter.com/p/lessons-from-uri-levine
  • IntelliJ: https://www.jetbrains.com/idea/
  • Julia: https://julialang.org/
  • Parallel computing: https://en.wikipedia.org/wiki/Parallel_computing
  • Douglas Chen on LinkedIn: https://www.linkedin.com/in/douglaspchen/
  • Carlos Delatorre on LinkedIn: https://www.linkedin.com/in/cadelatorre/
  • MongoDB: https://www.mongodb.com/
  • Cursor: https://www.cursor.com/
  • GitHub Copilot: https://github.com/features/copilot
  • Llama: https://www.llama.com/
  • Mistral: https://mistral.ai/
  • Building Lovable: $10M ARR in 60 days with 15 people | Anton Osika (CEO and co-founder): https://www.lennysnewsletter.com/p/building-lovable-anton-osika
  • Inside Bolt: From near-death to ~$40m ARR in 5 months—one of the fastest-growing products in history | Eric Simons (founder & CEO of StackBlitz): https://www.lennysnewsletter.com/p/inside-bolt-eric-simons
  • Behind the product: Replit | Amjad Masad (co-founder and CEO): https://www.lennysnewsletter.com/p/behind-the-product-replit-amjad-masad
  • React: https://react.dev/
  • Sonnet: https://www.anthropic.com/claude/sonnet
  • OpenAI: https://openai.com/
  • FedRamp: https://www.fedramp.gov/
  • Amdahl’s law: https://en.wikipedia.org/wiki/Amdahl%27s_law

  Recommended book:
  • Fall in Love with the Problem, Not the Solution: A Handbook for Entrepreneurs: https://www.amazon.com/Fall-Love-Problem-Solution-Entrepreneurs/dp/1637741987

  Production and marketing by https://penname.co/. For inquiries about sponsoring the podcast, email podcast@lennyrachitsky.com.

  Lenny may be an investor in the companies discussed.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:46:20.893Z
---

# Building a magical AI code editor used by over 1m developers in 4 months: Inside Windsurf

## 00:00 - 20:00

A lot of the bets we're making inside

## 20:00 - 50:00

the company are for things that are not,

## 50:00 - 80:00

you know, 3, four weeks away. We should

## 80:00 - 105:00

be cannibalizing the existing state of

## 105:00 - 140:00

our product every 6 to 12 months. Every

## 140:00 - 160:00

6 to 12 months, it should make our

## 160:00 - 190:00

existing product look silly. It should

## 190:00 - 215:00

almost make the form factor of existing

## 215:00 - 245:00

product look dump. How do you know when

## 245:00 - 275:00

it's time to hire someone? I wanted the

## 275:00 - 295:00

company to almost be like this

## 295:00 - 340:00

dehydrated entity. Every hire is like a

## 340:00 - 370:00

little bit of water and we only go back

## 370:00 - 390:00

and hire someone when we're back to

## 390:00 - 420:00

being dehydrated. Any other skills you

## 420:00 - 445:00

think people should be investing more in

## 445:00 - 470:00

with the rise of AI, building more and

## 470:00 - 505:00

more of our products? engineers are now

## 505:00 - 550:00

able to produce more technology. The ROI

## 550:00 - 580:00

of building technology has actually gone

## 580:00 - 610:00

up. This actually means you hire more.

## 610:00 - 635:00

The best thing to do is just get your

## 635:00 - 660:00

hands dirty with all of these products.

## 660:00 - 685:00

You could be a force multiplier to your

## 685:00 - 710:00

organization in ways in which they never

## 710:00 - 740:00

even

## 740:00 - 765:00

[Music]

## 765:00 - 805:00

anticipated. Today, my guest is Verun

## 805:00 - 845:00

Mohan. Baroon is the co-founder and CEO

## 845:00 - 875:00

of Windservef which has quickly become

## 875:00 - 910:00

one of people's favorite AI coding tools

## 910:00 - 940:00

and is basically the main competitor to

## 940:00 - 975:00

cursor with over 1 million users 4

## 975:00 - 1015:00

months in. In our conversation, Veroon

## 1015:00 - 1055:00

shares what makes Windsurf unique, why

## 1055:00 - 1075:00

they decided to invest heavily in

## 1075:00 - 1110:00

enterprise sales very early in their

## 1110:00 - 1145:00

history, why agency is going to be the

## 1145:00 - 1170:00

most important skill for engineers and

## 1170:00 - 1205:00

product builders to build. also the

## 1205:00 - 1235:00

story of how they started out as a GPU

## 1235:00 - 1265:00

infrastructure company and realized

## 1265:00 - 1290:00

there was a much bigger opportunity up

## 1290:00 - 1320:00

the stack and the two pivots that got

## 1320:00 - 1350:00

them to where they are today. He also

## 1350:00 - 1380:00

gives a live demo advice for being

## 1380:00 - 1420:00

successful Windsurf and so much more.

## 1420:00 - 1455:00

There's so much to learn about where

## 1455:00 - 1480:00

things are heading for engineers and

## 1480:00 - 1505:00

product builders in general in this

## 1505:00 - 1530:00

conversation and I'm really excited to

## 1530:00 - 1555:00

bring it to you. Thank you to everyone

## 1555:00 - 1575:00

on LinkedIn and Twitter and my

## 1575:00 - 1605:00

newsletter community for suggesting

## 1605:00 - 1645:00

great questions to dig into with Verun.

## 1645:00 - 1670:00

If you enjoy this podcast, don't forget

## 1670:00 - 1690:00

to subscribe and follow it in your

## 1690:00 - 1720:00

favorite podcasting app or YouTube.

## 1720:00 - 1755:00

Also, if you become a yearly subscriber

## 1755:00 - 1800:00

of my newsletter, you get a year free of

## 1800:00 - 1855:00

Perplexity Pro, Notion Plus, Linear,

## 1855:00 - 1905:00

Granola, and Superhum. Check it out at

## 1905:00 - 1935:00

lennisnewsletter.com. With that, I bring

## 1935:00 - 1975:00

you Verun

## 1975:00 - 2020:00

Mohan. This episode is brought to you by

## 2020:00 - 2070:00

Brex, the financial stack used by one in

## 2070:00 - 2120:00

every three US venture-backed startups.

## 2120:00 - 2155:00

Brex knows that nearly 40% of startups

## 2155:00 - 2195:00

fail because they run out of cash. So,

## 2195:00 - 2225:00

they built a banking experience that

## 2225:00 - 2255:00

focuses on helping founders get more

## 2255:00 - 2290:00

from every dollar. It's a stark

## 2290:00 - 2315:00

difference from traditional banking

## 2315:00 - 2345:00

options that leave a startup's cash

## 2345:00 - 2370:00

sitting idle while chipping away at it

## 2370:00 - 2415:00

with fees. To help founders protect cash

## 2415:00 - 2455:00

and extend runway, Brex combined the

## 2455:00 - 2490:00

best things about checking, treasury,

## 2490:00 - 2540:00

and FDIC insurance in one powerhouse

## 2540:00 - 2575:00

account. You can send and receive money

## 2575:00 - 2610:00

worldwide at lightning speed. You can

## 2610:00 - 2655:00

get 20x the standard FDIC protection

## 2655:00 - 2690:00

through program banks, and you can earn

## 2690:00 - 2720:00

industry-leading yield from your first

## 2720:00 - 2750:00

dollar while still being able to access

## 2750:00 - 2795:00

your funds anytime. To learn more, check

## 2795:00 - 2860:00

out Bre at

## 2860:00 - 2930:00

brex.com/banking-solutions. That's

## 2930:00 - 2955:00

brex.com/bankingsolutions. This episode

## 2955:00 - 2990:00

is brought to you by Product Board, the

## 2990:00 - 3025:00

leading product management platform for

## 3025:00 - 3055:00

the enterprise. For over 10 years,

## 3055:00 - 3085:00

ProductB has helped customer- centric

## 3085:00 - 3130:00

organizations like Zoom, Salesforce, and

## 3130:00 - 3160:00

Autodesk build the right products

## 3160:00 - 3200:00

faster. And as an end-to-end platform,

## 3200:00 - 3235:00

Product Board seamlessly supports all

## 3235:00 - 3260:00

stages of the product development life

## 3260:00 - 3295:00

cycle. From gathering customer insights

## 3295:00 - 3325:00

to planning a road map to aligning

## 3325:00 - 3365:00

stakeholders to earning customer buyin,

## 3365:00 - 3405:00

all with a single source of truth. And

## 3405:00 - 3440:00

now product leaders can get even more

## 3440:00 - 3475:00

visibility into customer needs with

## 3475:00 - 3510:00

product board pulse, a new voice of

## 3510:00 - 3545:00

customer solution. Built-in intelligence

## 3545:00 - 3575:00

helps you analyze trends across all of

## 3575:00 - 3610:00

your feedback. And then dive deeper by

## 3610:00 - 3650:00

asking AI your follow-up questions. See

## 3650:00 - 3680:00

how Product Board can help your team

## 3680:00 - 3710:00

deliver higher impact products that

## 3710:00 - 3750:00

solve real customer needs and advance

## 3750:00 - 3790:00

your business goals. For a special offer

## 3790:00 - 3850:00

and free 15-day trial, visit

## 3850:00 - 3980:00

productboard.com/lenny. That's

## 3980:00 - 4010:00

productboard.comleny. Verun, thank you

## 4010:00 - 4040:00

so much for being here and welcome to

## 4040:00 - 4070:00

the podcast. Buddy, thanks for having

## 4070:00 - 4105:00

me. Longtime listener. Oh, I really

## 4105:00 - 4125:00

appreciate that. I'm so excited to have

## 4125:00 - 4150:00

you here. I feel like just you guys have

## 4150:00 - 4190:00

become this overnight success, which is

## 4190:00 - 4215:00

definitely not an overnight success, but

## 4215:00 - 4235:00

I feel like I've been hearing about

## 4235:00 - 4270:00

Windsurf more and more as people's

## 4270:00 - 4305:00

favorite AI tool. And I just don't think

## 4305:00 - 4340:00

people know the story behind Windsurf,

## 4340:00 - 4365:00

behind Kodium, the company that you

## 4365:00 - 4400:00

built. So I thought it'd be good to

## 4400:00 - 4440:00

maybe just start there and have you just

## 4440:00 - 4480:00

briefly share the history of Kodium and

## 4480:00 - 4515:00

how Windsurf emerged out of Kodium.

## 4515:00 - 4545:00

Yeah, so the company was actually

## 4545:00 - 4580:00

started close to four years ago. Uh as

## 4580:00 - 4615:00

you as you know AI coding was not a

## 4615:00 - 4645:00

thing four years ago. Chat GPT was not

## 4645:00 - 4680:00

out four years ago. At the time we

## 4680:00 - 4710:00

actually started out building GPU

## 4710:00 - 4745:00

virtualization and compiler software

## 4745:00 - 4775:00

right uh before this I worked in

## 4775:00 - 4805:00

autonomous vehicles. My co-founder who

## 4805:00 - 4840:00

I've known since middle school uh worked

## 4840:00 - 4900:00

on ARVR at Meta. And for us we believe

## 4900:00 - 4920:00

deep learning would touch many many

## 4920:00 - 4955:00

industries right it wouldn't just touch

## 4955:00 - 4980:00

uh like sort of autonomous vehicles it

## 4980:00 - 5015:00

would touch financial services defense

## 5015:00 - 5050:00

uh healthcare. And we believe these

## 5050:00 - 5080:00

applications were hard to build these

## 5080:00 - 5110:00

deep learning applications. So we made

## 5110:00 - 5145:00

it possible for you to effectively run

## 5145:00 - 5195:00

these complex applications on computers

## 5195:00 - 5230:00

without GPUs and we would handle all the

## 5230:00 - 5255:00

complexity of being able to actually run

## 5255:00 - 5300:00

the workload on the GPUs for you, right?

## 5300:00 - 5320:00

And we were able to optimize these

## 5320:00 - 5355:00

workloads a ton. And then the middle of

## 5355:00 - 5400:00

2022 rolled around and we had a couple

## 5400:00 - 5430:00

million in revenue. We were managing

## 5430:00 - 5465:00

upwards of 10,000 sort of GPUs. We had

## 5465:00 - 5490:00

eight people at the time. We were free

## 5490:00 - 5530:00

cash flow positive. Uh but I think what

## 5530:00 - 5560:00

we felt was when once these generative

## 5560:00 - 5595:00

models started to get very good uh we

## 5595:00 - 5625:00

sort of felt a lot of what we built was

## 5625:00 - 5655:00

not as valuable and this was like a very

## 5655:00 - 5685:00

very hard moment for us at the company.

## 5685:00 - 5710:00

We were only eight people at the time

## 5710:00 - 5750:00

but we felt hey would people be training

## 5750:00 - 5795:00

these very bespoke sentiment classifier

## 5795:00 - 5825:00

models anymore that were like very very

## 5825:00 - 5860:00

custom models or would they just ask

## 5860:00 - 5900:00

GPTN is this a positive or negative

## 5900:00 - 5930:00

sentiment? probably is going to be the

## 5930:00 - 5960:00

latter, right? And in a world in which

## 5960:00 - 5985:00

everyone was going to run generative AI

## 5985:00 - 6015:00

models, why would an infrastructure

## 6015:00 - 6050:00

company be a differentiator? Because

## 6050:00 - 6080:00

everyone is going to run the same kind

## 6080:00 - 6105:00

of infrastructure down the line. So

## 6105:00 - 6135:00

instead, what we decided to do was we

## 6135:00 - 6170:00

believe generative AI was almost going

## 6170:00 - 6195:00

to be like the next internet. And in

## 6195:00 - 6215:00

that case, what we should go out and do

## 6215:00 - 6250:00

is build the next great apps like uh

## 6250:00 - 6280:00

Google, like Amazon. And we vertical

## 6280:00 - 6305:00

integrated and actually took our

## 6305:00 - 6325:00

infrastructure, our inference

## 6325:00 - 6355:00

infrastructure to go out and build

## 6355:00 - 6400:00

Kodium uh at the time. And at that time

## 6400:00 - 6430:00

we were early adopters of GitHub copilot

## 6430:00 - 6460:00

and we thought the coding space was

## 6460:00 - 6495:00

going to get tremendously disrupted in

## 6495:00 - 6520:00

the next coming years. So we actually

## 6520:00 - 6550:00

took our infrastructure we ran our own

## 6550:00 - 6580:00

models at massive scale. We even trained

## 6580:00 - 6610:00

our own models. In the very beginning it

## 6610:00 - 6635:00

was very very simple. It's purely an

## 6635:00 - 6680:00

autocomplete sort of model right which

## 6680:00 - 6705:00

basically means that as the user was

## 6705:00 - 6735:00

typing we'd complete the next one or two

## 6735:00 - 6770:00

or three or four lines of code. But we

## 6770:00 - 6805:00

provided the product entirely for free

## 6805:00 - 6855:00

in all the IDEs that developers coded.

## 6855:00 - 6890:00

Right? That meant VS Code, Jet Brains,

## 6890:00 - 6945:00

Eclipse, Visual Studio, Vim, Emacs. And

## 6945:00 - 6965:00

the reason why we were able to build it

## 6965:00 - 6980:00

for free was because of our

## 6980:00 - 7005:00

infrastructure background. We were able

## 7005:00 - 7060:00

to optimize these workloads a ton. And

## 7060:00 - 7100:00

uh I guess very quickly after that, some

## 7100:00 - 7125:00

large businesses also wanted to work

## 7125:00 - 7155:00

with us and we built out the kind of

## 7155:00 - 7180:00

this enterprise motion to to work with

## 7180:00 - 7210:00

these large companies like Dell, JP

## 7210:00 - 7240:00

Morgan, Chase. And for them, the bigger

## 7240:00 - 7265:00

thing wasn't just, hey, could we

## 7265:00 - 7290:00

autocomplete code or could we chat with

## 7290:00 - 7320:00

the codebase, it was, could you offer us

## 7320:00 - 7350:00

a secure offering that was also

## 7350:00 - 7375:00

personalized to all the private data

## 7375:00 - 7400:00

inside the company. So, we took our

## 7400:00 - 7420:00

infrastructure and made it so that we

## 7420:00 - 7455:00

invested a ton in making sure that we

## 7455:00 - 7490:00

deeply understood these large companies

## 7490:00 - 7525:00

code bases, right? And that's what we

## 7525:00 - 7560:00

were working on until 6 months ago. And

## 7560:00 - 7585:00

it's not that we've stopped working on

## 7585:00 - 7615:00

that, but basically what we realized 6

## 7615:00 - 7645:00

months ago was we were getting limited

## 7645:00 - 7685:00

by the IDEs that we were already working

## 7685:00 - 7725:00

in. So VS Code, which is a very popular

## 7725:00 - 7765:00

ID, had a ceiling for the AI

## 7765:00 - 7785:00

capabilities we could showcase our

## 7785:00 - 7815:00

users. And because of that, we decided

## 7815:00 - 7840:00

to go out and fork VS Code and build our

## 7840:00 - 7880:00

own ID with some of these new agentic

## 7880:00 - 7910:00

capabilities. And over time, in the last

## 7910:00 - 7940:00

couple years, the model capabilities

## 7940:00 - 7980:00

have also been growing exponentially

## 7980:00 - 8005:00

year-over-year. That's that's sort of

## 8005:00 - 8035:00

where we are right now. Like I I skipped

## 8035:00 - 8070:00

a lot of pieces there. Uh but but that's

## 8070:00 - 8105:00

that's where we landed. There's so many

## 8105:00 - 8125:00

interesting threads there. One is just

## 8125:00 - 8145:00

there's always this question of just

## 8145:00 - 8185:00

where value will acrue in AI. And it's

## 8185:00 - 8210:00

so interesting you guys started almost

## 8210:00 - 8245:00

at the bottom layer of infrastructure

## 8245:00 - 8290:00

GPUs and then you went to what people uh

## 8290:00 - 8330:00

call GP a GPT wrapper not not actually

## 8330:00 - 8380:00

but uh so I guess any just like lessons

## 8380:00 - 8410:00

there just thoughts on just where you

## 8410:00 - 8445:00

think value will end up in this world of

## 8445:00 - 8485:00

AI in the stack of AI tools. Maybe I can

## 8485:00 - 8510:00

start by just saying like one thing

## 8510:00 - 8535:00

about startups that I that I think are

## 8535:00 - 8580:00

like really true. It's very unlikely the

## 8580:00 - 8605:00

first thing that you believe you should

## 8605:00 - 8635:00

go work on uh is going to be the right

## 8635:00 - 8670:00

thing which is like a very hard thing to

## 8670:00 - 8715:00

kind of wrangle with being a startup

## 8715:00 - 8750:00

founder, right? Uh you need to kind of

## 8750:00 - 8785:00

be irrationally optimistic that what

## 8785:00 - 8805:00

you're going to do is going to be

## 8805:00 - 8825:00

differentially important because

## 8825:00 - 8850:00

otherwise why would you go out and do

## 8850:00 - 8885:00

what you're doing and if it's if it's if

## 8885:00 - 8910:00

it's obvious then a bigger company would

## 8910:00 - 8940:00

have already done it, right? Uh but then

## 8940:00 - 8965:00

you also need to be really really

## 8965:00 - 9010:00

realistic because most ideas that are uh

## 9010:00 - 9045:00

that are I guess uh non-conventional are

## 9045:00 - 9090:00

usually bad ideas, right? Uh so so it's

## 9090:00 - 9130:00

it's this weird kind of tight rope you

## 9130:00 - 9170:00

need to you need to kind of uh you know

## 9170:00 - 9205:00

kind of balance on top of where you're

## 9205:00 - 9230:00

kind of pushing for a future that you

## 9230:00 - 9260:00

believe is true, but all the while

## 9260:00 - 9280:00

you're getting new information. You need

## 9280:00 - 9315:00

to kind of kill the beliefs that you

## 9315:00 - 9345:00

had. And if I were to start with the

## 9345:00 - 9380:00

infrastructure piece, we first went in

## 9380:00 - 9400:00

with the assumption that model

## 9400:00 - 9425:00

architectures were going to be really

## 9425:00 - 9460:00

really heterogeneous. Working from an

## 9460:00 - 9485:00

autonomous vehicle background, there

## 9485:00 - 9500:00

were many different types of model

## 9500:00 - 9525:00

architectures out there. There were

## 9525:00 - 9550:00

convolutional neural networks, graph

## 9550:00 - 9575:00

neural networks, recurrent neural

## 9575:00 - 9630:00

networks, LSTMs, uh sort of lighter

## 9630:00 - 9670:00

neural nets with with frustr networks,

## 9670:00 - 9695:00

right? And there were maybe like tens of

## 9695:00 - 9720:00

architectures we were dealing with. And

## 9720:00 - 9740:00

at that point we were like the

## 9740:00 - 9775:00

complexity of this is so high that it's

## 9775:00 - 9800:00

very clear if someone offloaded the

## 9800:00 - 9820:00

complexity there would be a lot of

## 9820:00 - 9845:00

value. Fast forward to the middle of

## 9845:00 - 9880:00

2023 everything looks like it's going to

## 9880:00 - 9915:00

be a transformer. So now our hypotheses

## 9915:00 - 9960:00

are just wrong. So at this point then

## 9960:00 - 9990:00

most of the value is probably not going

## 9990:00 - 10020:00

to acrew at purely the at least this is

## 10020:00 - 10045:00

our belief at the infrastructure layer.

## 10045:00 - 10070:00

It's going to acrue somewhere else.

## 10070:00 - 10090:00

Where is the layer that you can actually

## 10090:00 - 10120:00

differentiate on? And we believe the

## 10120:00 - 10155:00

application layer is a very very deep

## 10155:00 - 10180:00

layer to go out and differentiate on

## 10180:00 - 10205:00

right. What are the number of ways we

## 10205:00 - 10245:00

can build better user experiences,

## 10245:00 - 10270:00

better workflows for developers? We

## 10270:00 - 10305:00

think there's effectively no ceiling on

## 10305:00 - 10335:00

that on how much better we can make the

## 10335:00 - 10375:00

lives of developers. Basically, you

## 10375:00 - 10400:00

touched on the second thread that I

## 10400:00 - 10415:00

thought was really interesting here is

## 10415:00 - 10460:00

just how you guys pivoted uh from ideas

## 10460:00 - 10485:00

that were working like you were making

## 10485:00 - 10510:00

money, people loved it. You said you had

## 10510:00 - 10550:00

millions of dollars of ARR revenue and

## 10550:00 - 10570:00

then you just like no, we're going to

## 10570:00 - 10600:00

completely change the business. So, the

## 10600:00 - 10625:00

question there is just like how do you

## 10625:00 - 10645:00

what have you learned about knowing what

## 10645:00 - 10670:00

to follow? And one thing I heard there

## 10670:00 - 10695:00

that was really interesting is just once

## 10695:00 - 10725:00

your assumptions change about that you

## 10725:00 - 10760:00

built your idea on, it's time to rethink

## 10760:00 - 10790:00

this idea and maybe try something else.

## 10790:00 - 10825:00

You know, I I think the way we sort of

## 10825:00 - 10865:00

think about this is, you know, even when

## 10865:00 - 10900:00

we're working right now, we just accept

## 10900:00 - 10920:00

that we're going to get a lot of things

## 10920:00 - 10950:00

wrong. We're just going to get a lot of

## 10950:00 - 10990:00

things wrong. Um, obviously that's a

## 10990:00 - 11015:00

very big moment because that was a bet

## 11015:00 - 11045:00

the company moment in the sense that we

## 11045:00 - 11080:00

basically said told our investors, hey,

## 11080:00 - 11100:00

you know, we're making money on this. We

## 11100:00 - 11125:00

had already raised $28 million of

## 11125:00 - 11145:00

capital and we were just like, "Hey,

## 11145:00 - 11170:00

we're just going to pivot entirely from

## 11170:00 - 11200:00

this." And we did that overnight, right?

## 11200:00 - 11220:00

This wasn't this thing where we just

## 11220:00 - 11255:00

said, "Hey, maybe a quarter, one or two

## 11255:00 - 11280:00

quarters." Because one of the things we

## 11280:00 - 11300:00

knew that's very important for startups

## 11300:00 - 11345:00

is focus. And if you're if you're trying

## 11345:00 - 11365:00

to do another thing that you think is

## 11365:00 - 11390:00

big and you're focused on something that

## 11390:00 - 11410:00

you don't believe is valuable, you're

## 11410:00 - 11430:00

guaranteed going to fail at the thing

## 11430:00 - 11460:00

you think is going to be big, right? So

## 11460:00 - 11485:00

that's like a that's a very obvious

## 11485:00 - 11520:00

thing uh there. But I think once you go

## 11520:00 - 11540:00

in with the assumption that a lot of

## 11540:00 - 11570:00

your hypotheses are going to be wrong,

## 11570:00 - 11615:00

but you will do the most concentrated

## 11615:00 - 11645:00

work possible to go out and validate

## 11645:00 - 11675:00

these hypothesis and you won't be in

## 11675:00 - 11700:00

love with your ideas. Like I think

## 11700:00 - 11725:00

ideas, it's awesome when you have a

## 11725:00 - 11755:00

great idea, but you should never be too

## 11755:00 - 11790:00

in love with your ideas and you have an

## 11790:00 - 11815:00

organization that is very truth

## 11815:00 - 11845:00

seeeking. I think a lot of people at the

## 11845:00 - 11870:00

company have had their ideas tested over

## 11870:00 - 11900:00

and over again. Even just building

## 11900:00 - 11925:00

Windsor, that is not a complete company

## 11925:00 - 11960:00

pivot, but that's a big decision that we

## 11960:00 - 11995:00

made at the company. you kind of need to

## 11995:00 - 12040:00

make some bets and sometimes you're

## 12040:00 - 12060:00

wrong and sometimes you're right. But if

## 12060:00 - 12090:00

you have an organization that comes out

## 12090:00 - 12120:00

and you feel like morale is not going to

## 12120:00 - 12165:00

be low if you made the wrong decision um

## 12165:00 - 12190:00

that that's the best right that means

## 12190:00 - 12225:00

you have optionality for the rest of

## 12225:00 - 12260:00

time and and Lenny one thing that I try

## 12260:00 - 12320:00

to tell the company about this is this

## 12320:00 - 12345:00

year the total amount of engineering

## 12345:00 - 12385:00

output we will have is much larger than

## 12385:00 - 12420:00

the engineering output we've we've had

## 12420:00 - 12440:00

since the beginning of the company's

## 12440:00 - 12485:00

creation till now. So that almost means

## 12485:00 - 12520:00

every year is a new lease on life for

## 12520:00 - 12555:00

us, right? It's almost a new way for us

## 12555:00 - 12590:00

to test out an entirely new set of

## 12590:00 - 12625:00

hypothesis. And maybe we were wrong

## 12625:00 - 12655:00

about our original hypothesis like in

## 12655:00 - 12690:00

the in the first place. What what makes

## 12690:00 - 12730:00

us more smart than everyone else to be

## 12730:00 - 12770:00

right, you know, more times than them.

## 12770:00 - 12800:00

That's so empowering. Makes me think

## 12800:00 - 12825:00

about Ori Lavine was on the podcast,

## 12825:00 - 12860:00

Co-founder Ways, and he has this phrase

## 12860:00 - 12885:00

that he he wears on his shirt. His book

## 12885:00 - 12915:00

is called this. Fall in love with the

## 12915:00 - 12945:00

problem, not the solution. And that

## 12945:00 - 12965:00

feels like that's exactly what you're

## 12965:00 - 13000:00

describing. Okay. So let's talk about

## 13000:00 - 13035:00

windsurf. Uh what's the simplest way for

## 13035:00 - 13070:00

people to understand what is windsurf?

## 13070:00 - 13125:00

Yeah. So windsurf is an IDE, right? It's

## 13125:00 - 13165:00

an application to go out and and build

## 13165:00 - 13215:00

software and build applications. Um the

## 13215:00 - 13245:00

the you know the crazy thing is a lot of

## 13245:00 - 13280:00

people who use the product don't even

## 13280:00 - 13325:00

probably know what an IDE is. Uh which

## 13325:00 - 13350:00

is which is crazy and we'll get in we'll

## 13350:00 - 13395:00

get into that in a second. But why did

## 13395:00 - 13425:00

we go out and build windsurf and what is

## 13425:00 - 13450:00

windsurf? Maybe why couldn't we have

## 13450:00 - 13475:00

just done this on top of conventional

## 13475:00 - 13530:00

ids like visual studio code. So maybe

## 13530:00 - 13565:00

just to get into this a little bit as we

## 13565:00 - 13590:00

saw that AI was getting more and more

## 13590:00 - 13620:00

powerful the way people go out and build

## 13620:00 - 13645:00

technology we thought the interface for

## 13645:00 - 13680:00

that was going to change remarkably. It

## 13680:00 - 13705:00

was not going to be a conventional pure

## 13705:00 - 13745:00

text editor where you the user is

## 13745:00 - 13770:00

writing a handful of lines of code or

## 13770:00 - 13825:00

most of the code and the IDE provides uh

## 13825:00 - 13885:00

like maybe some basic feedback on what

## 13885:00 - 13910:00

the user is doing right or wrong and the

## 13910:00 - 13935:00

basic feedback could be hey there's a

## 13935:00 - 13965:00

bug in your software or compiler error

## 13965:00 - 13995:00

in your software. it could do much more,

## 13995:00 - 14040:00

right? It could actually go out and and

## 14040:00 - 14080:00

modify large chunks of code. And one of

## 14080:00 - 14115:00

the key pieces that we recognized was

## 14115:00 - 14160:00

with this new paradigm with with AI, AI

## 14160:00 - 14180:00

was probably going to write well over

## 14180:00 - 14210:00

90% of the software. In which case, the

## 14210:00 - 14230:00

role of a developer and what they're

## 14230:00 - 14270:00

doing in the ID is maybe reviewing code.

## 14270:00 - 14295:00

Maybe it's actually like a little bit

## 14295:00 - 14315:00

different than what it is in the past.

## 14315:00 - 14350:00

And we'll see this very soon with with

## 14350:00 - 14390:00

Windsor. um maybe you know when we were

## 14390:00 - 14425:00

using the product actually a good chunk

## 14425:00 - 14445:00

of the user's time is actually reviewing

## 14445:00 - 14480:00

what the AI is outputting so we needed

## 14480:00 - 14515:00

to build custom review flows into the

## 14515:00 - 14560:00

IDE to actually make it so that it it

## 14560:00 - 14580:00

was easier to actually go ahead and do

## 14580:00 - 14605:00

that right because the developer is not

## 14605:00 - 14635:00

spending all their time writing code and

## 14635:00 - 14665:00

this is the fundamental premise on why

## 14665:00 - 14685:00

we built the product we thought we were

## 14685:00 - 14715:00

going to get limited a ton if we had

## 14715:00 - 14760:00

very very basic UI out there and I'll

## 14760:00 - 14800:00

give you even a simple example here we

## 14800:00 - 14825:00

have this autocomplete product right

## 14825:00 - 14845:00

that completes a handful of lines of

## 14845:00 - 14880:00

code Now we've actually launched this

## 14880:00 - 14905:00

offering called windsurf tab that

## 14905:00 - 14950:00

basically shows you refactors as well

## 14950:00 - 14990:00

and these refactors are almost inline

## 14990:00 - 15015:00

refactors and we were able to build a

## 15015:00 - 15065:00

custom UI for that in windsurf but in VS

## 15065:00 - 15090:00

code we needed to because of the access

## 15090:00 - 15130:00

to the APIs we needed to dynamically

## 15130:00 - 15170:00

generate images right alongside the

## 15170:00 - 15205:00

user's cursor uh because we just didn't

## 15205:00 - 15240:00

have access to the capabilities to

## 15240:00 - 15270:00

showcase and edit properly and what we

## 15270:00 - 15300:00

realized is immediately by porting over

## 15300:00 - 15350:00

to Windsorf our acceptance rate tripled

## 15350:00 - 15395:00

same ML models it just tripled. So what

## 15395:00 - 15430:00

that I guess gave us confidence in is

## 15430:00 - 15460:00

yeah like you could argue technology is

## 15460:00 - 15485:00

very important and I think techn is very

## 15485:00 - 15515:00

important but if our users are getting

## 15515:00 - 15545:00

very little value from the technology

## 15545:00 - 15575:00

we're sort of building you need to

## 15575:00 - 15605:00

really clarify maybe we do need to build

## 15605:00 - 15635:00

a new surface and interface and that's

## 15635:00 - 15670:00

what winds surface. So the big bet you

## 15670:00 - 15695:00

took there just to make this super clear

## 15695:00 - 15735:00

is you were initially working within

## 15735:00 - 15775:00

existing IDs that everyone was familiar

## 15775:00 - 15800:00

with and then it was like this isn't

## 15800:00 - 15825:00

going to get us where we need to go.

## 15825:00 - 15850:00

We're going to try to convince people to

## 15850:00 - 15875:00

switch to something completely new

## 15875:00 - 15900:00

because it's going to be so much better.

## 15900:00 - 15955:00

It's our own IDE. I think I think maybe

## 15955:00 - 15985:00

people may not recognize just how risky

## 15985:00 - 16010:00

that is. Convincing engineers to use

## 16010:00 - 16035:00

something completely new. That's a huge

## 16035:00 - 16075:00

deal. Yeah. No, of course. And one of

## 16075:00 - 16120:00

the key pieces that I just maybe Lenny

## 16120:00 - 16170:00

that would be important to share is we a

## 16170:00 - 16200:00

lot of our developers do use Visual

## 16200:00 - 16230:00

Studio Code. Uh but there are lots of

## 16230:00 - 16265:00

people that write in languages like Java

## 16265:00 - 16305:00

uh sort of uh C++ and so on and so forth

## 16305:00 - 16330:00

and they might use the Jetrains family

## 16330:00 - 16380:00

of ids that like Intelligj and for us we

## 16380:00 - 16405:00

actually still committed to building on

## 16405:00 - 16435:00

those platforms right we just felt

## 16435:00 - 16465:00

though that one of the dominant IDs

## 16465:00 - 16500:00

which was visual studio code was

## 16500:00 - 16550:00

limiting the the sort of user interface

## 16550:00 - 16580:00

that we could give to our actual

## 16580:00 - 16615:00

customers. What is the current state of

## 16615:00 - 16650:00

traction for Windsor? You hear all these

## 16650:00 - 16675:00

crazy numbers about all the competitors

## 16675:00 - 16690:00

in your space. So what can you share

## 16690:00 - 16725:00

there for folks just to know? Yeah, so

## 16725:00 - 16760:00

maybe a handful. We launched the product

## 16760:00 - 16790:00

like a bit over four months ago and in

## 16790:00 - 16810:00

that period of time over a million

## 16810:00 - 16840:00

developers have tried the product and

## 16840:00 - 16860:00

obviously we have many hundreds of

## 16860:00 - 16895:00

thousands of monthly active users right

## 16895:00 - 16935:00

now. I love how like these days like oh

## 16935:00 - 16970:00

million no big deal like it's just the

## 16970:00 - 17005:00

numbers are absurd these days like we're

## 17005:00 - 17045:00

just getting used to just 100 million AR

## 17045:00 - 17085:00

here million users in four months there.

## 17085:00 - 17125:00

It's just like oh of course how could

## 17125:00 - 17165:00

you not have that? Uh but that's absurd.

## 17165:00 - 17205:00

It's just like an insane time right now.

## 17205:00 - 17225:00

You touched on something that I wanted

## 17225:00 - 17250:00

to get to later, but I may as well bring

## 17250:00 - 17295:00

it up now. The question of just how

## 17295:00 - 17320:00

engineering will change in the future.

## 17320:00 - 17355:00

You throw out the stat that like 90% of

## 17355:00 - 17400:00

code is going to be written by AI in the

## 17400:00 - 17430:00

future. Daario from Thropic recently

## 17430:00 - 17465:00

said the same thing. Uh you guys have a

## 17465:00 - 17500:00

really interesting glimpse into just how

## 17500:00 - 17530:00

things will look in the future. So I

## 17530:00 - 17560:00

guess the question just how do you think

## 17560:00 - 17600:00

coding specifically will look in the

## 17600:00 - 17630:00

next few years? How different will it be

## 17630:00 - 17670:00

from today? I think when when we think

## 17670:00 - 17700:00

about what is an engineer actually doing

## 17700:00 - 17725:00

it probably falls into three buckets

## 17725:00 - 17775:00

right um what should I solve for how

## 17775:00 - 17810:00

should I solve it and then solving it

## 17810:00 - 17845:00

and I guess like everyone who's working

## 17845:00 - 17870:00

in the space is probably increasingly

## 17870:00 - 17905:00

convinced that solving it which is just

## 17905:00 - 17940:00

the pure I know how I'm going to do it

## 17940:00 - 17970:00

and just going and doing it AI is going

## 17970:00 - 18015:00

to handle vast majority if not all of it

## 18015:00 - 18050:00

right um in fact it probably actually

## 18050:00 - 18075:00

with some of the work that we've done in

## 18075:00 - 18110:00

terms of deeply understanding code bases

## 18110:00 - 18140:00

how should I solve it is also going get

## 18140:00 - 18170:00

closer and closer to getting done,

## 18170:00 - 18200:00

right? If you deeply understand the

## 18200:00 - 18230:00

environment inside an organization, if

## 18230:00 - 18260:00

you deeply understand the codebase, how

## 18260:00 - 18290:00

you should solve it given best practices

## 18290:00 - 18320:00

when the company also gets solved. So I

## 18320:00 - 18355:00

think what engineering kind of goes to

## 18355:00 - 18385:00

is actually what you wanted engineers to

## 18385:00 - 18415:00

do in the first place, which is what are

## 18415:00 - 18435:00

the most important business problems

## 18435:00 - 18465:00

that we do need to solve. what are the

## 18465:00 - 18500:00

most important capabilities that we need

## 18500:00 - 18540:00

our application our product to have and

## 18540:00 - 18560:00

actually going and prioritizing those

## 18560:00 - 18585:00

and actually going and making the right

## 18585:00 - 18605:00

technical decision to go out and doing

## 18605:00 - 18645:00

it right and I think that's where

## 18645:00 - 18675:00

engineering is probably heading towards

## 18675:00 - 18705:00

now does that mean that no one needs a

## 18705:00 - 18745:00

CS degree I think I think that's maybe a

## 18745:00 - 18780:00

little bit overplayed uh a little bit

## 18780:00 - 18815:00

just because you know maybe maybe here's

## 18815:00 - 18855:00

here's maybe my argument for that a lot

## 18855:00 - 18890:00

of developers nowadays that build full

## 18890:00 - 18920:00

stack applications at least until like a

## 18920:00 - 18940:00

handful of years ago they probably went

## 18940:00 - 18960:00

to college and took an operating system

## 18960:00 - 18990:00

of course, right? And in theory, they're

## 18990:00 - 19015:00

not really like playing around with the

## 19015:00 - 19050:00

operating system like the kernel like

## 19050:00 - 19080:00

very frequently. But do those principles

## 19080:00 - 19110:00

help them in understanding why their

## 19110:00 - 19145:00

applications are slow? Do they help them

## 19145:00 - 19185:00

in understanding why why some design

## 19185:00 - 19205:00

decisions are better than the other?

## 19205:00 - 19230:00

Yeah, that makes them a much better

## 19230:00 - 19265:00

engineer than than another engineer. And

## 19265:00 - 19300:00

I think that idea and the understanding

## 19300:00 - 19335:00

of what's going on at the bottom will

## 19335:00 - 19380:00

make a good engineer even better, right?

## 19380:00 - 19410:00

Um, but also at the same time, it

## 19410:00 - 19430:00

empowers a bunch of people that never

## 19430:00 - 19460:00

understood all of those things, how to

## 19460:00 - 19485:00

actually build as well, which is another

## 19485:00 - 19530:00

remarkable sort of thing that fell out

## 19530:00 - 19555:00

through this whole process. I don't know

## 19555:00 - 19580:00

if you have kids, but just like say you

## 19580:00 - 19610:00

had kids or you had a niece or nephew

## 19610:00 - 19660:00

going into college, let's say, would you

## 19660:00 - 19700:00

suggest they do soft, they do computer

## 19700:00 - 19735:00

science, or would you suggest like

## 19735:00 - 19765:00

you're not going to have a good time if

## 19765:00 - 19790:00

that's the career you choose right now?

## 19790:00 - 19820:00

Yeah, I think you know, maybe I think

## 19820:00 - 19850:00

back a little bit. So I I went to MIT, a

## 19850:00 - 19875:00

lot of us at the at the company went to

## 19875:00 - 19915:00

MIT together uh on the engineering team

## 19915:00 - 19945:00

and uh I I think like when I think about

## 19945:00 - 19985:00

what we learned the most at at on for

## 19985:00 - 20020:00

engineering or computer science, it was

## 20020:00 - 20060:00

not exactly like how do you write code,

## 20060:00 - 20090:00

right? That's maybe that is like almost

## 20090:00 - 20120:00

a given that you can you can kind of

## 20120:00 - 20150:00

write code after after going to college.

## 20150:00 - 20180:00

It's more like the principles of how you

## 20180:00 - 20210:00

think about a problem and how you break

## 20210:00 - 20240:00

it down, right? And how you solve it in

## 20240:00 - 20265:00

an interesting way, right? So an example

## 20265:00 - 20290:00

that of a class that I really enjoyed

## 20290:00 - 20320:00

was our distributed systems class. And

## 20320:00 - 20340:00

there you're kind of reading through

## 20340:00 - 20385:00

literature and understanding how how

## 20385:00 - 20420:00

some design decisions were kind of made.

## 20420:00 - 20445:00

And I think it's more like a problem

## 20445:00 - 20490:00

solving kind of course, right? And a a

## 20490:00 - 20520:00

major. It's a major of how you solve

## 20520:00 - 20555:00

problems given some constraints of how,

## 20555:00 - 20580:00

you know, how computers today function,

## 20580:00 - 20610:00

right? Like here's the speed at which

## 20610:00 - 20635:00

memory sort of operates. Here's the

## 20635:00 - 20660:00

speed at which you know, here's how much

## 20660:00 - 20695:00

computation you can do in one one cycle

## 20695:00 - 20725:00

or one second. And and based on that,

## 20725:00 - 20745:00

you can make some trade-offs and solve a

## 20745:00 - 20790:00

solve a problem. So I I don't know if if

## 20790:00 - 20820:00

I would say that you shouldn't go get a

## 20820:00 - 20835:00

computer science degree. I think

## 20835:00 - 20855:00

computer science is almost synonymous

## 20855:00 - 20885:00

with problem solving. In that case, I

## 20885:00 - 20910:00

think it's pretty valuable. Is

## 20910:00 - 20935:00

everything you learn in your computer

## 20935:00 - 20965:00

science degree useful? I'd say a lot of

## 20965:00 - 20985:00

things that I learned in my computer

## 20985:00 - 21005:00

science degree are not useful. I'll give

## 21005:00 - 21030:00

you an example. I took a parallel

## 21030:00 - 21065:00

computing class in Julia and I don't

## 21065:00 - 21085:00

think Julia is a very popular

## 21085:00 - 21115:00

programming language anymore. Am I very

## 21115:00 - 21135:00

sad that I took the class? No. The

## 21135:00 - 21160:00

principles of parallel computing are

## 21160:00 - 21195:00

still very useful, I would say, today.

## 21195:00 - 21225:00

So what I'm hearing is skills that you

## 21225:00 - 21250:00

still want to build whether it's

## 21250:00 - 21275:00

computer science or maybe some version

## 21275:00 - 21315:00

of computer science is uh kind of like

## 21315:00 - 21355:00

building the mental model of how

## 21355:00 - 21390:00

computers and systems work parallel

## 21390:00 - 21440:00

processing memory hard drives internet

## 21440:00 - 21460:00

things like that. Okay. And then there's

## 21460:00 - 21490:00

just like problem solving skills being

## 21490:00 - 21525:00

able to solve interesting problems. Is

## 21525:00 - 21550:00

there any other skills you think people

## 21550:00 - 21575:00

should be investing more in with the

## 21575:00 - 21605:00

rise of AI building more and more of our

## 21605:00 - 21635:00

products? I think one of the things

## 21635:00 - 21675:00

that's maybe a little bit undervalued is

## 21675:00 - 21710:00

this kind of agency piece and I think

## 21710:00 - 21760:00

about this a lot which is you know you

## 21760:00 - 21775:00

have a lot of people they could go

## 21775:00 - 21795:00

through college and go through school

## 21795:00 - 21820:00

and they're basically told exactly what

## 21820:00 - 21850:00

to do on a pet and you know they're

## 21850:00 - 21895:00

given these very very I would say uh

## 21895:00 - 21920:00

well-defined paths that they need to

## 21920:00 - 21990:00

take and I think I think maybe in

## 21990:00 - 22020:00

society and just school we we don't

## 22020:00 - 22055:00

prioritize how do you how do you make

## 22055:00 - 22090:00

sure you get people with real agency

## 22090:00 - 22125:00

that want to build something, right? Uh

## 22125:00 - 22155:00

like their goal is not just to maybe

## 22155:00 - 22175:00

graduate from college and then get a job

## 22175:00 - 22210:00

at a big tech company where they're told

## 22210:00 - 22240:00

exactly what to do or where to put the

## 22240:00 - 22275:00

pixel on, you know, for for this one

## 22275:00 - 22310:00

website. Um and I think that's maybe a

## 22310:00 - 22355:00

skill set that is undervalued just right

## 22355:00 - 22385:00

now probably in the last, you know,

## 22385:00 - 22420:00

maybe 10 10 years or so. And I think

## 22420:00 - 22435:00

that's going to be really really

## 22435:00 - 22470:00

important. You know, a skill for us for

## 22470:00 - 22495:00

a startup obviously these are skills

## 22495:00 - 22535:00

that we just look for. We look for

## 22535:00 - 22560:00

people that are really high agency

## 22560:00 - 22600:00

because we just recognize that by

## 22600:00 - 22625:00

default if we don't innovate and do

## 22625:00 - 22650:00

crazy things, we're going to die. The

## 22650:00 - 22680:00

company's just going to die. So, we just

## 22680:00 - 22705:00

look for this, right? But I would say

## 22705:00 - 22740:00

like for most software engineering jobs,

## 22740:00 - 22765:00

that's probably not the case, right?

## 22765:00 - 22795:00

Just think about, you know, big company

## 22795:00 - 22825:00

X and what they're hiring for on the

## 22825:00 - 22850:00

average software engineering interview.

## 22850:00 - 22880:00

It probably doesn't look like that. I

## 22880:00 - 22910:00

love how you phrase that. If we don't uh

## 22910:00 - 22935:00

do crazy things and innovate, we're

## 22935:00 - 22965:00

going to die. Yeah, that that would be a

## 22965:00 - 22990:00

great title for this podcast episode.

## 22990:00 - 23030:00

And I think I's 100% true. There's just

## 23030:00 - 23060:00

a lot of crazy things happening and a

## 23060:00 - 23090:00

lot of innovation happening. And if you

## 23090:00 - 23135:00

can't keep up, uh, you'll die. So, let's

## 23135:00 - 23160:00

talk about hiring. You have a really

## 23160:00 - 23185:00

interesting approach to hiring. There's

## 23185:00 - 23220:00

a few questions I have here. One is just

## 23220:00 - 23260:00

how do you I know you try to stay really

## 23260:00 - 23300:00

lean. That's a common theme across all

## 23300:00 - 23340:00

the AI startups these days. How do you

## 23340:00 - 23375:00

know when it's time to hire someone? I

## 23375:00 - 23405:00

love the idea of being a lean company,

## 23405:00 - 23440:00

but I don't idolize it in the way that

## 23440:00 - 23490:00

hey, like it is a dream to be a 10% or

## 23490:00 - 23530:00

20% company that's making, you know, 50,

## 23530:00 - 23565:00

100, 200 million in revenue. That's like

## 23565:00 - 23605:00

not I think what we idolize inside the

## 23605:00 - 23645:00

company. I think what we idolize is be

## 23645:00 - 23695:00

the smallest company we can be to

## 23695:00 - 23740:00

satisfy our ambitions, right? That's

## 23740:00 - 23765:00

what the goal is. And maybe Lenny, the

## 23765:00 - 23785:00

way I would sort of put that out there

## 23785:00 - 23820:00

is if I told you, hey, I'm going to

## 23820:00 - 23850:00

build an autonomous vehicle and I said,

## 23850:00 - 23880:00

"Our team is 10 people." You should

## 23880:00 - 23910:00

rightfully say, "Hey, Verun, you're not

## 23910:00 - 23950:00

serious." And you'd be right. I'm not

## 23950:00 - 23990:00

serious at that point. So, I think the

## 23990:00 - 24025:00

answer is what is the minimum number of

## 24025:00 - 24065:00

people to go out and build the crazy

## 24065:00 - 24095:00

ambition project that you have? And I

## 24095:00 - 24120:00

think the project we are trying to go

## 24120:00 - 24145:00

out and do, which is completely

## 24145:00 - 24170:00

transform the way software gets built. I

## 24170:00 - 24190:00

we've mentioned this inside the company.

## 24190:00 - 24220:00

Our goal is to reduce the time it takes

## 24220:00 - 24265:00

to build apps and technology by 99%.

## 24265:00 - 24295:00

Right? It is a it is a tremendously sort

## 24295:00 - 24330:00

of ambitious goal and it is it's not

## 24330:00 - 24370:00

possible for us to be a 10 20 30 40

## 24370:00 - 24395:00

person engineering team in the long term

## 24395:00 - 24420:00

and actually satisfy that goal. We think

## 24420:00 - 24465:00

it's there's a very very high ceiling.

## 24465:00 - 24495:00

So that's maybe the first key piece

## 24495:00 - 24525:00

there. It's like actually you know if we

## 24525:00 - 24560:00

can crack actually being a fairly

## 24560:00 - 24600:00

sizable company but still operate as if

## 24600:00 - 24630:00

we're a startup that's the dream right

## 24630:00 - 24665:00

that's that's the that's the dream. Um,

## 24665:00 - 24690:00

in terms of hiring philosophy, the way

## 24690:00 - 24730:00

we sort of think about things is we only

## 24730:00 - 24750:00

hire for a role if we're actually

## 24750:00 - 24810:00

underwater for that function. So let's

## 24810:00 - 24825:00

say we're going out and building

## 24825:00 - 24860:00

inference technology. Unless we're

## 24860:00 - 24890:00

underwater there, we will not go out and

## 24890:00 - 24925:00

hire hire someone to go out and work

## 24925:00 - 24955:00

work for that, right? And the reason for

## 24955:00 - 24990:00

that is I actually think this is like

## 24990:00 - 25025:00

this is a this is a future, right? when

## 25025:00 - 25055:00

when you hire for a role and you already

## 25055:00 - 25090:00

have enough people there. What you you

## 25090:00 - 25115:00

know you get a lot of weird politics

## 25115:00 - 25140:00

that ultimately ends up happening and

## 25140:00 - 25170:00

it's not because people are bad people.

## 25170:00 - 25205:00

I don't I think most people are really

## 25205:00 - 25235:00

well-intentioned but what happens when

## 25235:00 - 25260:00

you have people that join a company and

## 25260:00 - 25295:00

in reality you didn't really need them.

## 25295:00 - 25325:00

they will go out and manufacture some

## 25325:00 - 25350:00

other thing that they should go work on,

## 25350:00 - 25365:00

right? right? They should they will go

## 25365:00 - 25385:00

out and figure out something else to

## 25385:00 - 25430:00

work on and realistically it's not that

## 25430:00 - 25450:00

important but they will go out and try

## 25450:00 - 25470:00

to convince the rest of the organization

## 25470:00 - 25510:00

that it is important right and I just

## 25510:00 - 25530:00

think as a startup we don't have the

## 25530:00 - 25560:00

bandwidth to go out and deal with that

## 25560:00 - 25590:00

right uh for me I would like to see

## 25590:00 - 25630:00

everyone just almost like be be like

## 25630:00 - 25655:00

raising their hands up being like I'm

## 25655:00 - 25680:00

dying like we need we need one more

## 25680:00 - 25710:00

person and that's when we go out and and

## 25710:00 - 25735:00

hire someone and one of the analogies I

## 25735:00 - 25765:00

like to give is we I wanted the company

## 25765:00 - 25810:00

to almost be like this dehydrated entity

## 25810:00 - 25845:00

right and every hire is is like a little

## 25845:00 - 25890:00

bit of water, right? And and we only go

## 25890:00 - 25915:00

back and hire someone when we're when

## 25915:00 - 25950:00

we're back to being dehydrated.

## 25950:00 - 26000:00

I love this metaphor so much. Uh and it

## 26000:00 - 26040:00

sounds uh it sounds painful. It sounds

## 26040:00 - 26065:00

painful that you need to be underwater

## 26065:00 - 26100:00

and raising your hand. I'm about to die

## 26100:00 - 26130:00

and dehydrated, but I also know that

## 26130:00 - 26170:00

it's a really exciting way to work. Like

## 26170:00 - 26210:00

it sounds hard, but if you're in it,

## 26210:00 - 26255:00

it's just like I guess talk about just

## 26255:00 - 26285:00

that side of it because I think it could

## 26285:00 - 26310:00

sound like this is terrible. I don't

## 26310:00 - 26335:00

want to work this way. You know what I

## 26335:00 - 26370:00

actually think, Lenny? It's it's it's

## 26370:00 - 26395:00

really good for a handful of reasons,

## 26395:00 - 26420:00

which is that a lot of the PE we respect

## 26420:00 - 26455:00

and trust the people that work at the

## 26455:00 - 26495:00

company. So, this forces ruthless

## 26495:00 - 26525:00

prioritization. You know, you have a

## 26525:00 - 26540:00

team that's going out and doing

## 26540:00 - 26565:00

something, they will never ask to work

## 26565:00 - 26590:00

on something that's not important. In

## 26590:00 - 26610:00

fact, if there are two things that

## 26610:00 - 26630:00

they're working on, they're just going

## 26630:00 - 26665:00

to just tell me, "Hey, there are two

## 26665:00 - 26690:00

things on my plate. I just don't have

## 26690:00 - 26715:00

the ability to do two. I can only do

## 26715:00 - 26740:00

one." And they will pick the one that's

## 26740:00 - 26765:00

most important. And this actually goes

## 26765:00 - 26790:00

back to one thing that I think is true

## 26790:00 - 26810:00

about startups and just companies in

## 26810:00 - 26850:00

general. You don't win by doing, you

## 26850:00 - 26890:00

know, 10 things kind of well. You win by

## 26890:00 - 26925:00

doing like one thing really well and

## 26925:00 - 26955:00

maybe you fail nine things. This is the

## 26955:00 - 26980:00

thing that I've told the company. This

## 26980:00 - 27015:00

is very different than school, right? In

## 27015:00 - 27050:00

school, you optimize for your total GPA,

## 27050:00 - 27080:00

but for companies, I just need to get an

## 27080:00 - 27115:00

A+ on the one class that matters and

## 27115:00 - 27140:00

then I can get an F in all the other

## 27140:00 - 27175:00

classes. Uh, and an F in all the other

## 27175:00 - 27205:00

classes doesn't mean, you know, being,

## 27205:00 - 27230:00

you know, just doing illegal things.

## 27230:00 - 27260:00

that that basically means you just depp

## 27260:00 - 27295:00

prioritize things that don't matter. you

## 27295:00 - 27320:00

know that actually forces this

## 27320:00 - 27345:00

organizational prioritization that is

## 27345:00 - 27390:00

just really really good right and you

## 27390:00 - 27420:00

know Douglas and I Douglas being my

## 27420:00 - 27445:00

co-founder we can tell the company these

## 27445:00 - 27465:00

are the two things that are the most

## 27465:00 - 27490:00

important but if we go out and tell

## 27490:00 - 27505:00

these are the two things that are the

## 27505:00 - 27535:00

most important to the company and then

## 27535:00 - 27575:00

we put the company has 20% more people

## 27575:00 - 27615:00

than necessary what do those what's

## 27615:00 - 27645:00

going to ultimately happen right it's

## 27645:00 - 27675:00

almost a forcing function for ruthless

## 27675:00 - 27720:00

prioritization to have fewer people or

## 27720:00 - 27745:00

people that just that are just

## 27745:00 - 27775:00

underwater internally at the company

## 27775:00 - 27805:00

everyone listening that works at a big

## 27805:00 - 27840:00

company uh knows exactly what you mean

## 27840:00 - 27870:00

when you describe when there's just too

## 27870:00 - 27895:00

many people. They will all find work to

## 27895:00 - 27925:00

do and they will all be pitching ideas.

## 27925:00 - 27945:00

You know, they all want to show impact.

## 27945:00 - 27965:00

They want to do well in their

## 27965:00 - 27990:00

performance reviews. That's just the

## 27990:00 - 28025:00

nature of of too many people at a

## 28025:00 - 28060:00

company. And so, I think this all really

## 28060:00 - 28100:00

resonates to even get even deeper on

## 28100:00 - 28120:00

just what it looks like when someone's

## 28120:00 - 28145:00

underwater to tell you it's time to

## 28145:00 - 28180:00

hire. Is it just someone coming to you,

## 28180:00 - 28215:00

Verun? We need I need someone on this

## 28215:00 - 28240:00

team. This is just not possible. Like,

## 28240:00 - 28265:00

what does that look like even more

## 28265:00 - 28290:00

practically? Yeah, I think it's

## 28290:00 - 28320:00

basically along those lines. It's that

## 28320:00 - 28350:00

hey, there's some pressure to get

## 28350:00 - 28385:00

something done in a in a short period of

## 28385:00 - 28410:00

time. By the way, one of the things that

## 28410:00 - 28430:00

we do believe though for software, if

## 28430:00 - 28465:00

you want to do great things, um it's not

## 28465:00 - 28485:00

possible to just say, hey, I want to get

## 28485:00 - 28515:00

it done in one month. If it is like

## 28515:00 - 28540:00

because you have to think about it from

## 28540:00 - 28565:00

this perspective, if a software project

## 28565:00 - 28595:00

could get built in two to three weeks,

## 28595:00 - 28620:00

what does that really mean about like

## 28620:00 - 28645:00

the true complexity and differentiation

## 28645:00 - 28675:00

of what you built? Like it's probably

## 28675:00 - 28705:00

not very high unless you believe you are

## 28705:00 - 28730:00

way smarter than everyone else. But I

## 28730:00 - 28765:00

think that's hubris, right? I think we

## 28765:00 - 28790:00

actually have a very exceptional

## 28790:00 - 28815:00

engineering team but also at the same

## 28815:00 - 28840:00

time I don't think our engineering team

## 28840:00 - 28870:00

is so exceptional that we can do things

## 28870:00 - 28895:00

in three weeks that the rest of the

## 28895:00 - 28915:00

world can't do in like six to nine

## 28915:00 - 28945:00

months. That's kind of stupid to believe

## 28945:00 - 28990:00

that. So I think basically it comes down

## 28990:00 - 29025:00

to that person coming out and being like

## 29025:00 - 29055:00

hey look like I don't have enough time

## 29055:00 - 29095:00

to do X. Us having a conversation to be

## 29095:00 - 29135:00

like okay uh what can you do then? And

## 29135:00 - 29170:00

if the answer is I I can only do less

## 29170:00 - 29200:00

than that then maybe we make a decision

## 29200:00 - 29235:00

actually oh wow that's great. Maybe we

## 29235:00 - 29260:00

actually should depp prioritize. Why?

## 29260:00 - 29285:00

Because this is actually also another

## 29285:00 - 29315:00

thing that's very hard even for people

## 29315:00 - 29350:00

like me and my co-founder. It's that we

## 29350:00 - 29375:00

also want to do a lot of things, right?

## 29375:00 - 29410:00

There's an urge to do a lot of things.

## 29410:00 - 29440:00

But if you if we are forced to make a

## 29440:00 - 29480:00

decision constantly on like we cannot do

## 29480:00 - 29525:00

X, it's very clarifying. It's very

## 29525:00 - 29560:00

clarifying uh because our engineering

## 29560:00 - 29590:00

interview process is also like extremely

## 29590:00 - 29620:00

low acceptance rate. So it's not very

## 29620:00 - 29645:00

easy for us to very quickly spin up

## 29645:00 - 29685:00

people and have them join the company uh

## 29685:00 - 29730:00

really really quickly either. Um, so I

## 29730:00 - 29755:00

think um I think it's clarifying for

## 29755:00 - 29775:00

everyone. It's clarifying for the person

## 29775:00 - 29805:00

that wants more people. We can just tell

## 29805:00 - 29845:00

them, hey, like look, we don't we don't

## 29845:00 - 29875:00

believe you should be doing this other

## 29875:00 - 29905:00

thing. Um, and it's also clarifying for

## 29905:00 - 29930:00

us because we can also get on the same

## 29930:00 - 29960:00

page with them, right? And sometimes we

## 29960:00 - 29995:00

just kind of agree, hey, like our teams

## 29995:00 - 30025:00

are very flexible that hey, actually we

## 30025:00 - 30050:00

do need to get something done. And one

## 30050:00 - 30075:00

of the things that we've kind of tried

## 30075:00 - 30105:00

to make sure is true on our engineering

## 30105:00 - 30140:00

team is people's value to the company

## 30140:00 - 30165:00

does not have anything to do with the

## 30165:00 - 30205:00

size of their team. There are projects

## 30205:00 - 30230:00

inside the company. There are directly

## 30230:00 - 30250:00

responsible individuals for these

## 30250:00 - 30285:00

projects um inside the company. And if

## 30285:00 - 30310:00

we feel like one project is very

## 30310:00 - 30330:00

important, then people can move from one

## 30330:00 - 30360:00

project to the next. Right? There's no

## 30360:00 - 30390:00

notion of someone owning people at the

## 30390:00 - 30430:00

company. That is a very bad and gnarly

## 30430:00 - 30465:00

idea. Right? In fact, the person that is

## 30465:00 - 30485:00

the most valuable at the company is the

## 30485:00 - 30520:00

person that can do the most crazy sort

## 30520:00 - 30550:00

of project out there with as few people

## 30550:00 - 30570:00

as possible. And that's what you should

## 30570:00 - 30605:00

be rewarding internally. How many people

## 30605:00 - 30635:00

do you have at Kodium at this point? So

## 30635:00 - 30675:00

we have we have close to 160 people and

## 30675:00 - 30700:00

the engineering team is over 50 people

## 30700:00 - 30735:00

right now. Awesome. Oh what what what's

## 30735:00 - 30765:00

the other bigger functions? So so we

## 30765:00 - 30805:00

have go to market we have a yeah oh

## 30805:00 - 30830:00

right okay I want to talk about that the

## 30830:00 - 30865:00

sales learning that you guys had. Okay.

## 30865:00 - 30890:00

Uh well let's close out this hiring

## 30890:00 - 30915:00

conversation. So we talked about what

## 30915:00 - 30950:00

you look for to tell you it's time to

## 30950:00 - 30990:00

hire. What do you look for in the people

## 30990:00 - 31025:00

that you interview and hire? One of the

## 31025:00 - 31055:00

key pieces that we look for we have a

## 31055:00 - 31080:00

very high technical bar. So assuming

## 31080:00 - 31100:00

that they actually meet the technical

## 31100:00 - 31140:00

bar, I think we sort of look for people

## 31140:00 - 31165:00

that are really really passionate about

## 31165:00 - 31185:00

the mission of what we're actually

## 31185:00 - 31215:00

trying to solve and people that are

## 31215:00 - 31250:00

willing to work very hard. Um I think

## 31250:00 - 31270:00

one of the things that we don't try to

## 31270:00 - 31320:00

do is convince people, hey look, we are,

## 31320:00 - 31345:00

you know, we're a very chill company and

## 31345:00 - 31375:00

it's great to work here. I think no,

## 31375:00 - 31405:00

this is a very exciting space. It's very

## 31405:00 - 31435:00

competitive. You should expect us to

## 31435:00 - 31465:00

lose if the people at the company are

## 31465:00 - 31505:00

not, you know, kind of uh they're not

## 31505:00 - 31530:00

working very hard. And I think one of

## 31530:00 - 31555:00

the biggest dog whistles I sort of hear

## 31555:00 - 31580:00

is when I ask people like how hard are

## 31580:00 - 31605:00

you willing to work? Some people

## 31605:00 - 31635:00

actually ultimately say, "Hey, I work

## 31635:00 - 31670:00

very smart and I basically ask them a

## 31670:00 - 31715:00

question, if we have many smart people

## 31715:00 - 31750:00

at our company that also work hard, uh

## 31750:00 - 31780:00

what's the differentiator going to be?

## 31780:00 - 31805:00

Are you just going to pull them down?"

## 31805:00 - 31825:00

Right? Because I think one of the things

## 31825:00 - 31850:00

that's true about companies is it's like

## 31850:00 - 31900:00

this massive group project. And uh and I

## 31900:00 - 31930:00

think the the thing about a person that

## 31930:00 - 31965:00

is is not pulling their weight that's

## 31965:00 - 31990:00

bad is not it's not the productivity,

## 31990:00 - 32010:00

right? At some point when the company

## 32010:00 - 32040:00

becomes many hundreds of engineers, I'm

## 32040:00 - 32060:00

not going to be thinking about the one

## 32060:00 - 32075:00

engineer that's not pulling their

## 32075:00 - 32105:00

weight. It's the team of people they

## 32105:00 - 32135:00

work with that are almost basically

## 32135:00 - 32170:00

saying, is this the bar internally at

## 32170:00 - 32205:00

the company? Is this the expectation?

## 32205:00 - 32235:00

And I guess Lenny, if I told you you

## 32235:00 - 32270:00

have a team of five people and you know

## 32270:00 - 32290:00

the four other people you're working

## 32290:00 - 32330:00

with just don't care. How much are you

## 32330:00 - 32360:00

going to feel like you should care? Not

## 32360:00 - 32410:00

too much. Exactly. So for us, for us, I

## 32410:00 - 32435:00

think that's what we more care about,

## 32435:00 - 32465:00

right? We have a culture where where

## 32465:00 - 32495:00

it's like it's very collaborative. It's

## 32495:00 - 32530:00

it's not an individual sport, but people

## 32530:00 - 32560:00

feel like they can rely on other people

## 32560:00 - 32600:00

to get complex sort of tasks done. So

## 32600:00 - 32620:00

the question you asked there just

## 32620:00 - 32650:00

basically is how hard are you willing to

## 32650:00 - 32695:00

work? How hard do you want to work? And

## 32695:00 - 32725:00

I I know some people there there's, you

## 32725:00 - 32745:00

know, this whole group of folks that are

## 32745:00 - 32775:00

just like work life balance. I don't

## 32775:00 - 32805:00

want to how dare you ask me to work

## 32805:00 - 32860:00

crazy hours. And I I I'd love just the

## 32860:00 - 32900:00

filter up front of if you work here, you

## 32900:00 - 32930:00

will work really hard. work work a lot

## 32930:00 - 32960:00

of hours. It's a crazy it's a crazy

## 32960:00 - 33000:00

space to be in and we will win by

## 33000:00 - 33035:00

working smart and also really hard.

## 33035:00 - 33075:00

Yeah. Uh you said at some point earlier

## 33075:00 - 33125:00

that your uh engineering pass rate is

## 33125:00 - 33155:00

you said it was like 6% of candidates

## 33155:00 - 33185:00

something like that. Yeah, it's probably

## 33185:00 - 33215:00

post a take-home it's probably that

## 33215:00 - 33250:00

actually. So the takehome itself filters

## 33250:00 - 33305:00

uh probably another you know 10 15x on

## 33305:00 - 33335:00

top of that. Here's a question that I've

## 33335:00 - 33355:00

been hearing more and more is just how

## 33355:00 - 33385:00

do you do interviews these days with

## 33385:00 - 33410:00

tools like Windsurf out there that solve

## 33410:00 - 33435:00

all your problems? We're okay with

## 33435:00 - 33465:00

people using the tools because I think

## 33465:00 - 33505:00

one of the worst things is like if

## 33505:00 - 33525:00

someone comes here and doesn't like

## 33525:00 - 33545:00

using these tools like we believe

## 33545:00 - 33565:00

they're massive productivity

## 33565:00 - 33595:00

improvements. We do bring people like

## 33595:00 - 33630:00

into the company like on site so we can

## 33630:00 - 33660:00

actually like see how they think through

## 33660:00 - 33700:00

problems on a on a whiteboard and all

## 33700:00 - 33730:00

these other pieces. So, so we do want to

## 33730:00 - 33755:00

see how they think on their feet and

## 33755:00 - 33780:00

hopefully they're not just like taking

## 33780:00 - 33810:00

what we're saying, putting it in a voice

## 33810:00 - 33830:00

translator and sticking it into

## 33830:00 - 33855:00

Tatsubishi and getting the answer out.

## 33855:00 - 33890:00

So, there is a way to do this. My

## 33890:00 - 33935:00

viewpoint on this is is uh the tools are

## 33935:00 - 33965:00

really really important, but I do think

## 33965:00 - 33990:00

we still look for some problems solving

## 33990:00 - 34025:00

ability, right? Like if the only way you

## 34025:00 - 34045:00

can solve a hard problem is like put it

## 34045:00 - 34080:00

into chat GBT, I think I think that's

## 34080:00 - 34130:00

like a concern to us. Today's episode is

## 34130:00 - 34170:00

brought to you by KOD. I personally use

## 34170:00 - 34215:00

KOD every single day to manage my

## 34215:00 - 34245:00

podcast and also to manage my community.

## 34245:00 - 34270:00

It's where I put the questions that I

## 34270:00 - 34300:00

plan to ask every guest that's coming on

## 34300:00 - 34325:00

the podcast. It's where I put my

## 34325:00 - 34360:00

community resources. It's how I manage

## 34360:00 - 34395:00

my workflows. Here's how KOD can help

## 34395:00 - 34435:00

you. Imagine starting a project at work

## 34435:00 - 34465:00

and your vision is clear. You know

## 34465:00 - 34495:00

exactly who's doing what and where to

## 34495:00 - 34520:00

find the data that you need to do your

## 34520:00 - 34555:00

part. In fact, you don't have to waste

## 34555:00 - 34580:00

time searching for anything because

## 34580:00 - 34610:00

everything your team needs from project

## 34610:00 - 34645:00

trackers and OKRs to documents and

## 34645:00 - 34685:00

spreadsheets lives in one tab, all in

## 34685:00 - 34725:00

KOD. With Kod's collaborative all-in-one

## 34725:00 - 34755:00

workspace, you get the flexibility of

## 34755:00 - 34800:00

docs, the structure of spreadsheets, the

## 34800:00 - 34835:00

power of applications, and the

## 34835:00 - 34880:00

intelligence of AI, all in one easy to

## 34880:00 - 34920:00

organize tab. Like I mentioned earlier,

## 34920:00 - 34955:00

I use Kota every single day. And more

## 34955:00 - 35000:00

than 50,000 teams trust KOD to keep them

## 35000:00 - 35030:00

more aligned and focused. If you're a

## 35030:00 - 35050:00

startup team looking to increase

## 35050:00 - 35085:00

alignment and agility, Kota can help you

## 35085:00 - 35120:00

move from planning to execution in

## 35120:00 - 35155:00

record time. To try it for yourself, go

## 35155:00 - 35175:00

to

## 35175:00 - 35220:00

kod.io/lenny today and get 6 months free

## 35220:00 - 35280:00

of the team plan for startups. That's

## 35280:00 - 35310:00

cooda.io/lenny to get started for free

## 35310:00 - 35350:00

and get six months of the team plan. k

## 35350:00 - 35405:00

cod.io/lenny / Lenny. Okay, let's talk

## 35405:00 - 35440:00

about this go to market sales experience

## 35440:00 - 35460:00

that you guys had. So, you started

## 35460:00 - 35500:00

without obviously like most people start

## 35500:00 - 35535:00

started building without sales team and

## 35535:00 - 35565:00

then you realized from what I hear that

## 35565:00 - 35585:00

that was a huge miss and a big

## 35585:00 - 35605:00

opportunity to talk about there because

## 35605:00 - 35630:00

that's that's really unique I think that

## 35630:00 - 35655:00

you guys have a large sales team and go

## 35655:00 - 35685:00

to market team. Yeah, we actually made

## 35685:00 - 35715:00

this decision pretty early in the

## 35715:00 - 35750:00

company's history. I would say like we

## 35750:00 - 35795:00

hired our VP of sales uh over a year ago

## 35795:00 - 35825:00

actually and the go to market team is

## 35825:00 - 35865:00

now over 80 people inside the company.

## 35865:00 - 35905:00

So it's a pretty sizable function inside

## 35905:00 - 35940:00

the company. Yeah. Maybe a little bit of

## 35940:00 - 35980:00

a backstory here. So when we started the

## 35980:00 - 36000:00

company actually we had a handful of

## 36000:00 - 36030:00

angels that actually were operators go

## 36030:00 - 36060:00

to market operators. So an example of

## 36060:00 - 36095:00

one was Carlos Delator who used to be

## 36095:00 - 36140:00

the CRO of MongoDB and I think for us we

## 36140:00 - 36170:00

never viewed enterprise sales and sales

## 36170:00 - 36190:00

as like a very negative thing. I think

## 36190:00 - 36220:00

this is like a interesting thing that

## 36220:00 - 36250:00

technical founders sometimes don't

## 36250:00 - 36285:00

really like. They think sales is like a

## 36285:00 - 36310:00

very negative sort of part of the

## 36310:00 - 36340:00

process. Everything should be productled

## 36340:00 - 36385:00

growth and I think it's it's it's not

## 36385:00 - 36410:00

that black and white. Like I think

## 36410:00 - 36455:00

enterprise sales is really valuable. But

## 36455:00 - 36490:00

maybe when we were a GPU virtualization

## 36490:00 - 36510:00

company and we were an infrastructure

## 36510:00 - 36535:00

company, the reason why we never hired a

## 36535:00 - 36560:00

salesperson is I didn't know how to

## 36560:00 - 36605:00

scale the function. I was the one who

## 36605:00 - 36635:00

was selling the product. So ultimately

## 36635:00 - 36660:00

speaking, if it was hard for me to sell

## 36660:00 - 36685:00

the product incrementally, I didn't know

## 36685:00 - 36730:00

how we could make that into a process

## 36730:00 - 36765:00

that we could then go and scale, right?

## 36765:00 - 36805:00

If I couldn't if I can do one like I

## 36805:00 - 36820:00

didn't know how we could take the

## 36820:00 - 36840:00

revenue of the business from a couple

## 36840:00 - 36875:00

million to hundreds of millions and I

## 36875:00 - 36910:00

let alone even tens. So if I didn't know

## 36910:00 - 36930:00

how to do that, how could I go out and

## 36930:00 - 36960:00

hire someone and make them scale it out?

## 36960:00 - 36990:00

Um on the other hand for Kodium very

## 36990:00 - 37015:00

quickly a lot of large enterprises sort

## 37015:00 - 37055:00

of reached out to us and from that alone

## 37055:00 - 37110:00

in in the middle of sort of 2023

## 37110:00 - 37145:00

uh we started I guess me and a handful

## 37145:00 - 37175:00

of other folks at the company started

## 37175:00 - 37205:00

selling the product and we were doing

## 37205:00 - 37240:00

tens of pilots concurrently with large

## 37240:00 - 37280:00

enterprises and we were very quickly

## 37280:00 - 37305:00

able to understand that there was a

## 37305:00 - 37330:00

large enterprise motion that needed to

## 37330:00 - 37375:00

be built in the space. So by the end of

## 37375:00 - 37415:00

2023, we actually hired our our VP of

## 37415:00 - 37455:00

sales and uh and very quickly after that

## 37455:00 - 37505:00

scaled a sales team and uh yeah, I mean

## 37505:00 - 37530:00

I mean look, if you want to sell to the

## 37530:00 - 37560:00

Fortune 500, it is very hard to do that

## 37560:00 - 37605:00

purely by swiping a credit card. Let's

## 37605:00 - 37630:00

talk about cursor. I hate I don't want

## 37630:00 - 37655:00

to spend too much time on competitors,

## 37655:00 - 37675:00

but that's what everyone's always

## 37675:00 - 37690:00

thinking about when they think of you

## 37690:00 - 37720:00

guys. You guys are kind of the leading

## 37720:00 - 37750:00

players, I think, in the space. Also,

## 37750:00 - 37780:00

there's co-pilot, but that's different.

## 37780:00 - 37810:00

So what's the simplest way to understand

## 37810:00 - 37840:00

how you guys are different from cursor

## 37840:00 - 37870:00

and also just how you think you win in

## 37870:00 - 37905:00

the space long term? So I think maybe

## 37905:00 - 37935:00

maybe a handful of things that I could I

## 37935:00 - 37965:00

could share. So on the product side, I

## 37965:00 - 37990:00

think we've invested a lot in making

## 37990:00 - 38015:00

sure codebase understanding for very

## 38015:00 - 38045:00

large code bases is is really high

## 38045:00 - 38070:00

quality. And that's just because of

## 38070:00 - 38095:00

where we started, right? We work with

## 38095:00 - 38120:00

some of the world's largest companies

## 38120:00 - 38150:00

like Dell, JP Market Jace, companies

## 38150:00 - 38180:00

like Dell have singular code bases that

## 38180:00 - 38205:00

are over 100 million lines of code,

## 38205:00 - 38230:00

right? So being able to understand that

## 38230:00 - 38255:00

really, really quickly to make large

## 38255:00 - 38285:00

scale changes is something that we spent

## 38285:00 - 38315:00

a lot of time doing. And that requires

## 38315:00 - 38345:00

us like actually building our own models

## 38345:00 - 38385:00

that can consume large chunks of their

## 38385:00 - 38415:00

codebase in parallel across thousands of

## 38415:00 - 38455:00

GPUs and almost rank them to be able to

## 38455:00 - 38480:00

find out what the most important sort of

## 38480:00 - 38510:00

snippets of code are for any question

## 38510:00 - 38535:00

that are asked about the codebase.

## 38535:00 - 38560:00

Right? So we've gone out and built large

## 38560:00 - 38580:00

distributed systems based on our

## 38580:00 - 38610:00

infrastructure background to go out and

## 38610:00 - 38640:00

do that. That's maybe one. Let me

## 38640:00 - 38660:00

actually follow that thread because I

## 38660:00 - 38700:00

think people may misunder underestimate

## 38700:00 - 38745:00

just how big of a deal that is. So when

## 38745:00 - 38770:00

we talk about we had the founders of

## 38770:00 - 38805:00

bolt and lovable on the podcast. So

## 38805:00 - 38830:00

those products they build something from

## 38830:00 - 38855:00

scratch. They build they write the code

## 38855:00 - 38925:00

for you. So that versus just loading say

## 38925:00 - 38985:00

windurf on your million code base say at

## 38985:00 - 39030:00

Airbnb or Uber like it understanding

## 39030:00 - 39060:00

what the hell you have and how it works

## 39060:00 - 39090:00

and where to go change things without

## 39090:00 - 39145:00

breaking it is insanely hard. And so

## 39145:00 - 39170:00

what I'm hearing is that's kind of a big

## 39170:00 - 39195:00

differentiator. You guys started there

## 39195:00 - 39225:00

actually and then Windsorf is now

## 39225:00 - 39255:00

building on that advantage. That's

## 39255:00 - 39285:00

right. Yeah. So we that's like a big

## 39285:00 - 39320:00

thing that we spent a lot of time on

## 39320:00 - 39350:00

which is just understanding sort of what

## 39350:00 - 39380:00

the what the codebase is doing and

## 39380:00 - 39405:00

actually like one of the other things is

## 39405:00 - 39440:00

what are all the user interactions with

## 39440:00 - 39465:00

respect to the codebase and happy to

## 39465:00 - 39510:00

show that also um you know in in a bit

## 39510:00 - 39550:00

here. Um the second key piece probably

## 39550:00 - 39600:00

is we're not only tied to the to

## 39600:00 - 39625:00

windsurf actually this is probably like

## 39625:00 - 39660:00

a weird statement given even we are

## 39660:00 - 39690:00

talking about windsurf which is that

## 39690:00 - 39725:00

actually we're pretty focused on

## 39725:00 - 39770:00

supporting ids like jet brains right uh

## 39770:00 - 39805:00

you know jet brains or intelligj has

## 39805:00 - 39850:00

over 70 to 80% of all java developers

## 39850:00 - 39900:00

code in in jet brains uh based ids right

## 39900:00 - 39945:00

um the reason why we don't feel as big a

## 39945:00 - 39970:00

need to almost build a competing product

## 39970:00 - 40000:00

to jetrains is jetrains is actually a

## 40000:00 - 40030:00

very sort extensible product in a way

## 40030:00 - 40070:00

that VS code is not. VS code is not very

## 40070:00 - 40100:00

extensible. So I think for us our goal

## 40100:00 - 40125:00

here is not only just to satisfy a

## 40125:00 - 40150:00

subset of users that can actually switch

## 40150:00 - 40180:00

onto our ID, but we want to give this

## 40180:00 - 40210:00

agentic sort of experience to every sort

## 40210:00 - 40240:00

of developer out there. And if that's if

## 40240:00 - 40265:00

that means they're Java developers that

## 40265:00 - 40295:00

write in Jetrains, that's fine. We work

## 40295:00 - 40320:00

with a large lot of large enterprises

## 40320:00 - 40350:00

that have 10 plus thousand developers

## 40350:00 - 40390:00

where over 50% of the developers are on

## 40390:00 - 40435:00

Jetrains, right? It's a very large large

## 40435:00 - 40460:00

product. And by the way, that company

## 40460:00 - 40485:00

itself, it's a privately held company

## 40485:00 - 40510:00

that makes many hundreds of millions of

## 40510:00 - 40545:00

dollars a year, right? So it's a very

## 40545:00 - 40580:00

very large company. So for us, that's

## 40580:00 - 40610:00

another key piece. We actually like want

## 40610:00 - 40635:00

to meet developers sort of where they

## 40635:00 - 40670:00

are and if they if they use a different

## 40670:00 - 40700:00

platform, we'll we'll work on that too.

## 40700:00 - 40725:00

The third key piece, and this probably

## 40725:00 - 40750:00

sounds another key piece for

## 40750:00 - 40800:00

enterprises, is u we we work in like a

## 40800:00 - 40830:00

lot of very secure environments, right?

## 40830:00 - 40865:00

Uh we have fed RAM compliance, right? We

## 40865:00 - 40895:00

have which means we can sell to like

## 40895:00 - 40930:00

very large government entities. uh we

## 40930:00 - 40955:00

have a hybrid mode of actually using the

## 40955:00 - 40985:00

product which means that all the code

## 40985:00 - 41015:00

that lives that is like indexed actually

## 41015:00 - 41045:00

lives on the tenant of the user right

## 41045:00 - 41070:00

code is one of the most important IP

## 41070:00 - 41110:00

pieces of IP for the company so I think

## 41110:00 - 41140:00

just if you were to look at it from like

## 41140:00 - 41170:00

a big company perspective there are many

## 41170:00 - 41200:00

reasons why like over the years of just

## 41200:00 - 41225:00

like building an enterprise product

## 41225:00 - 41255:00

we've handled a lot of complexities that

## 41255:00 - 41290:00

large companies want to see but that's

## 41290:00 - 41315:00

part of it is because of the history of

## 41315:00 - 41360:00

how we got here in the first place okay

## 41360:00 - 41390:00

Verun enough teasing let's do a live

## 41390:00 - 41425:00

demo of wind surf so folks and see what

## 41425:00 - 41445:00

it's like and then I'm just going to ask

## 41445:00 - 41465:00

you a bunch of questions as we're going

## 41465:00 - 41500:00

through it. So I'll let you pull up a

## 41500:00 - 41530:00

little shared screen where you have wind

## 41530:00 - 41575:00

surf pulled up. Great. So some context.

## 41575:00 - 41615:00

This is a very basic React project.

## 41615:00 - 41645:00

There's nothing in it right now. So if

## 41645:00 - 41675:00

you were to open any sort of file, it's

## 41675:00 - 41740:00

it's the default React app project. And

## 41740:00 - 41785:00

I have this basic image here. Uh, you

## 41785:00 - 41820:00

can pass Windsorf images of what you'd

## 41820:00 - 41855:00

like the project to kind of look like of

## 41855:00 - 41905:00

of what I would like an Airbnb for dogs

## 41905:00 - 41940:00

website to kind of look like. Beautiful.

## 41940:00 - 41970:00

Beautiful mockup. By the way, I love

## 41970:00 - 42000:00

that this is like all you need. This is

## 42000:00 - 42030:00

all you need. This is all you need. Uh,

## 42030:00 - 42075:00

so basically what we're going to do is

## 42075:00 - 42115:00

we're going to say, hey, um, this one of

## 42115:00 - 42145:00

the cool parts about windserve is it can

## 42145:00 - 42170:00

actually work in an existing project

## 42170:00 - 42215:00

already, right? So, I can basically say,

## 42215:00 - 42265:00

"Hey, change this React

## 42265:00 - 42365:00

app to show an Airbnb for dogs website

## 42365:00 - 42430:00

based on this image and preview it. So

## 42430:00 - 42455:00

now it'll just go out and start

## 42455:00 - 42495:00

executing code, reading through the

## 42495:00 - 42530:00

repository. Obviously, it doesn't know

## 42530:00 - 42565:00

what the current codebase actually looks

## 42565:00 - 42600:00

like and it'll go out and analyze the

## 42600:00 - 42635:00

codebase to actually find out the set of

## 42635:00 - 42665:00

changes necessary. So we'll go ahead and

## 42665:00 - 42695:00

wait and see what it's see what it's

## 42695:00 - 42730:00

going to do. But while we're doing that

## 42730:00 - 42750:00

um let's let's continue the

## 42750:00 - 42790:00

conversation. Awesome. Okay. So first of

## 42790:00 - 42820:00

all the you kind of start so you open up

## 42820:00 - 42865:00

Windsurf you had a boilerplate React

## 42865:00 - 42905:00

project ready to go and Windsurf had

## 42905:00 - 42930:00

never really seen this code before. You

## 42930:00 - 42975:00

ask it to do stuff on your codebase

## 42975:00 - 43015:00

which is just like change this to Airbnb

## 43015:00 - 43045:00

for dogs using this design. That's

## 43045:00 - 43075:00

right. That's exactly right. Yeah. Okay

## 43075:00 - 43100:00

cool. So we'll let it run and we'll

## 43100:00 - 43130:00

talk. So, let me ask you this question

## 43130:00 - 43155:00

that I've been asking everyone that

## 43155:00 - 43200:00

comes on that is building a product that

## 43200:00 - 43225:00

helps engineers build products and

## 43225:00 - 43250:00

product managers build products and

## 43250:00 - 43280:00

designers. Say you could sit next to

## 43280:00 - 43320:00

every single new user that uh opens up

## 43320:00 - 43345:00

Windsurf and whisper a couple tips in

## 43345:00 - 43380:00

their ear to help them be successful

## 43380:00 - 43410:00

with the product. What would be a couple

## 43410:00 - 43465:00

tips you'd share? Tip number one is just

## 43465:00 - 43520:00

be a little bit patient and both patient

## 43520:00 - 43570:00

and explicit, right? uh when you ask the

## 43570:00 - 43600:00

application to go out and make some

## 43600:00 - 43625:00

changes, it could actually go out and

## 43625:00 - 43680:00

make many irrelevant changes, right? And

## 43680:00 - 43705:00

one of the things that I think prevents

## 43705:00 - 43740:00

this the most is just be really really

## 43740:00 - 43775:00

explicit or as explicit as possible. And

## 43775:00 - 43800:00

one of the things I I sort of ask people

## 43800:00 - 43830:00

to do is in the beginning start by

## 43830:00 - 43855:00

making smaller changes, right? If

## 43855:00 - 43885:00

there's a very large directory, don't go

## 43885:00 - 43910:00

out and make it refactor the entire

## 43910:00 - 43940:00

directory, right? Uh because then if

## 43940:00 - 43975:00

it's wrong, it's going to like basically

## 43975:00 - 44020:00

destroy 20 files. And I think from

## 44020:00 - 44045:00

there, one of the key pieces I think

## 44045:00 - 44080:00

that comes from the users that use the

## 44080:00 - 44100:00

product is they sort of learn what the

## 44100:00 - 44130:00

hills and valleys of the product are.

## 44130:00 - 44165:00

And the analogy I like to give are kind

## 44165:00 - 44190:00

of similar to autocomplete, right? When

## 44190:00 - 44220:00

you use a product like autocomplete, you

## 44220:00 - 44255:00

would think a product that is suggesting

## 44255:00 - 44290:00

things but only getting accepted 30% of

## 44290:00 - 44310:00

the time would be really really

## 44310:00 - 44340:00

annoying. But the reason why it's not

## 44340:00 - 44395:00

very annoying is actually because you've

## 44395:00 - 44435:00

actually learned that hey 70% of the

## 44435:00 - 44485:00

time I don't need to accept this or or u

## 44485:00 - 44515:00

and the times that I do I know how to

## 44515:00 - 44545:00

get value from it right and you also

## 44545:00 - 44600:00

know beforehand if a if a if a if a sort

## 44600:00 - 44630:00

of command that you write is very

## 44630:00 - 44660:00

complex you just expect hey like the

## 44660:00 - 44690:00

autocomplete is not going to work for it

## 44690:00 - 44720:00

right so I think it's almost like a like

## 44720:00 - 44745:00

understand what the hills and valleys of

## 44745:00 - 44780:00

the product are the crazy thing is every

## 44780:00 - 44805:00

3 months that kind of gets changed and

## 44805:00 - 44840:00

reevaluated it right. It almost becomes

## 44840:00 - 44870:00

the case that that it becomes materially

## 44870:00 - 44905:00

better than it was in the past. So I

## 44905:00 - 44935:00

think I think maybe patience and being

## 44935:00 - 44960:00

explicit are are maybe the two important

## 44960:00 - 44995:00

key pieces I would I would tell users.

## 44995:00 - 45015:00

And I think something that was kind of

## 45015:00 - 45055:00

between the lines there is like get a

## 45055:00 - 45105:00

gut feeling of what the model is capable

## 45105:00 - 45140:00

of like how specific to be versus how

## 45140:00 - 45165:00

abstract it can be. And there's kind of

## 45165:00 - 45190:00

this like gut feeling you start to build

## 45190:00 - 45235:00

over time. That's right. Yeah. Um and

## 45235:00 - 45280:00

with that it feels like we have a an

## 45280:00 - 45315:00

actual preview. And guess what? We have

## 45315:00 - 45370:00

a a nice cute dogs. A nice dog app. And

## 45370:00 - 45405:00

one of the cool parts is that we've also

## 45405:00 - 45450:00

done beyond just just modifying code is

## 45450:00 - 45470:00

actually being able to point to

## 45470:00 - 45500:00

different pieces. And I guess I could

## 45500:00 - 45540:00

just kind of say I could point to

## 45540:00 - 45565:00

different elements and say, "Hey, like

## 45565:00 - 45620:00

make the background." And this is not

## 45620:00 - 45665:00

great design, but I could basically say

## 45665:00 - 45695:00

if I took this

## 45695:00 - 45770:00

element, make this background red,

## 45770:00 - 45805:00

right? and just take a particular

## 45805:00 - 45835:00

element and just change it and make it

## 45835:00 - 45865:00

red and it should go out and be able to

## 45865:00 - 45900:00

go out and do this. the preview aspect

## 45900:00 - 45930:00

of the product of being able to showcase

## 45930:00 - 45960:00

the app while it's getting built helps

## 45960:00 - 45990:00

in that now actually you can live

## 45990:00 - 46030:00

entirely in app app world right you

## 46030:00 - 46055:00

don't even maybe even need to look at

## 46055:00 - 46085:00

the code granted this looks hideous but

## 46085:00 - 46120:00

uh but in some ways if I wanted to I

## 46120:00 - 46155:00

could go out and do that right um this

## 46155:00 - 46175:00

is what happens when there's no more

## 46175:00 - 46195:00

designers like yeah when there's no more

## 46195:00 - 46230:00

designers like maybe the answer the

## 46230:00 - 46255:00

answer is like when you ask me what

## 46255:00 - 46285:00

should people be doing they should study

## 46285:00 - 46325:00

great taste having great taste because I

## 46325:00 - 46370:00

think taste is also very very hard right

## 46370:00 - 46400:00

um But maybe the other key piece, Lenny,

## 46400:00 - 46420:00

that I wanted to showcase here is like

## 46420:00 - 46445:00

obviously you could keep going here,

## 46445:00 - 46465:00

like I could I could take different

## 46465:00 - 46500:00

components and kind of change them, you

## 46500:00 - 46535:00

know, like we have like a lot of plans

## 46535:00 - 46560:00

here that are beyond just like point

## 46560:00 - 46605:00

andclick uh changing components. But one

## 46605:00 - 46645:00

of the cool pieces is the AI um they

## 46645:00 - 46675:00

there's like an AI review flow as well,

## 46675:00 - 46705:00

right? Which is kind of like what I was

## 46705:00 - 46730:00

saying, the goal of AI is now changed a

## 46730:00 - 46765:00

lot in that it is now modifying large

## 46765:00 - 46810:00

chunks of code for you. And the job of a

## 46810:00 - 46845:00

developer now is to is to actually

## 46845:00 - 46870:00

review a lot of the code that the AI is

## 46870:00 - 46905:00

generated. And granted, right now during

## 46905:00 - 46930:00

this during this podcast, I'm not going

## 46930:00 - 46950:00

to review all the code that's getting

## 46950:00 - 46970:00

generated. But let's say I want to go

## 46970:00 - 46995:00

out and modify some of this code, right?

## 46995:00 - 47020:00

And this is where if you're an actual

## 47020:00 - 47040:00

developer that actually wants to go

## 47040:00 - 47065:00

modify it, maybe I don't like my

## 47065:00 - 47090:00

variable name being called title. I want

## 47090:00 - 47125:00

it to be called title string, right?

## 47125:00 - 47170:00

Instead, like this. And if I wanted to

## 47170:00 - 47205:00

go out and make that change and make the

## 47205:00 - 47235:00

change to go out and and say title

## 47235:00 - 47255:00

string, right? And that's what I'm going

## 47255:00 - 47290:00

to do. I'm just going to tell the AI to

## 47290:00 - 47330:00

continue. And the cool part about this

## 47330:00 - 47365:00

is Windinsurf not only kind of knows

## 47365:00 - 47400:00

about what the agent has done, it also

## 47400:00 - 47425:00

knows everything that the user has done.

## 47425:00 - 47450:00

Like our goal here is to have this

## 47450:00 - 47485:00

almost flow-like state where everything

## 47485:00 - 47530:00

the user has done, the AI also knows.

## 47530:00 - 47565:00

And it it's able to predict the intent.

## 47565:00 - 47590:00

And as you can see, it said, I noticed

## 47590:00 - 47620:00

that the interface property title was

## 47620:00 - 47650:00

changed to title string. And then it now

## 47650:00 - 47680:00

has gone out and modified all the

## 47680:00 - 47715:00

locations within the app from title to

## 47715:00 - 47755:00

title string. And now it no longer says

## 47755:00 - 47790:00

that. So this is where like even if I'm

## 47790:00 - 47825:00

writing software and I want to go and

## 47825:00 - 47860:00

make point changes, the AI can go out

## 47860:00 - 47895:00

and quickly make these changes for on

## 47895:00 - 47930:00

the user's behalf. Imagine doing a

## 47930:00 - 47965:00

refactor or migration and you just

## 47965:00 - 47985:00

change one part of the code. You can

## 47985:00 - 48020:00

just tell the AI to continue the rest,

## 48020:00 - 48045:00

right? And because it deeply understands

## 48045:00 - 48080:00

the codebase, it should go out and find

## 48080:00 - 48110:00

all the corresponding places to go out

## 48110:00 - 48140:00

and make the change. And obviously now

## 48140:00 - 48170:00

when I reload my app, there's no no bug

## 48170:00 - 48195:00

in the app, right? It still loads

## 48195:00 - 48230:00

properly. I could obviously tell it to

## 48230:00 - 48265:00

do even cooler things like make the make

## 48265:00 - 48310:00

the app retro, right? Um I don't know

## 48310:00 - 48330:00

what that means, but I guess I could do

## 48330:00 - 48360:00

that and it should go ahead and make the

## 48360:00 - 48395:00

change correspondingly for me. But yeah,

## 48395:00 - 48430:00

that's maybe the you know highlevel sort

## 48430:00 - 48470:00

of parts there where the AI is not only

## 48470:00 - 48500:00

kind of able to operate entirely in

## 48500:00 - 48545:00

appspace but also on the code on the

## 48545:00 - 48575:00

code space of the users going out and

## 48575:00 - 48610:00

modifying code and to bridge the gap

## 48610:00 - 48630:00

between the two. So, it should add

## 48630:00 - 48660:00

leverage to not only non-developers that

## 48660:00 - 48690:00

are just purely building apps, but also

## 48690:00 - 48720:00

developers that are just hands- on

## 48720:00 - 48760:00

keyboard, too. Amazing. That's by the

## 48760:00 - 48785:00

way, it's if you're not on YouTube, you

## 48785:00 - 48810:00

can't see that you can just select any

## 48810:00 - 48850:00

element of the page and then uh

## 48850:00 - 48880:00

reference that in your ask of here's

## 48880:00 - 48905:00

what I want changed. Uh I didn't know

## 48905:00 - 48935:00

that was a feature and that is extremely

## 48935:00 - 48980:00

cool. So, interestingly, so having just

## 48980:00 - 49010:00

looked at lovable and bolt and replin

## 49010:00 - 49045:00

and apps like that, it's basically doing

## 49045:00 - 49070:00

all the things those apps do. Oh, wow.

## 49070:00 - 49130:00

There's the retro version. That's good.

## 49130:00 - 49165:00

I like that it built on your red and

## 49165:00 - 49190:00

made it really nice, actually. Actually,

## 49190:00 - 49215:00

the red looks way better now. Yeah, with

## 49215:00 - 49250:00

the little green button. This is great.

## 49250:00 - 49280:00

Okay, so I don't think people realize

## 49280:00 - 49310:00

this about apps like Windsurf, but it

## 49310:00 - 49340:00

could actually do a lot of agentic work

## 49340:00 - 49375:00

for you where you just tell it here, I

## 49375:00 - 49400:00

want you to do this versus it's

## 49400:00 - 49435:00

autocompleting code for you. The big

## 49435:00 - 49455:00

difference is you need to start it with

## 49455:00 - 49480:00

some codebase. You have this kind of

## 49480:00 - 49520:00

boilerplate React project. Is there a

## 49520:00 - 49555:00

reason you guys aren't taking that step

## 49555:00 - 49590:00

and just doing that automatically for

## 49590:00 - 49615:00

you? Is it because you're targeting

## 49615:00 - 49640:00

engineers and they don't need that or is

## 49640:00 - 49665:00

there other reasons? Lenny, the

## 49665:00 - 49690:00

interesting thing is like the base app

## 49690:00 - 49720:00

that you saw for this was also generated

## 49720:00 - 49755:00

by windsurf. The reason why we sort of

## 49755:00 - 49795:00

didn't generate it is installing all the

## 49795:00 - 49825:00

dependencies takes like 3 or 4 minutes

## 49825:00 - 49855:00

and for the demo I didn't want to wait

## 49855:00 - 49890:00

but totally actually most of the users

## 49890:00 - 49930:00

within within uh of the product probably

## 49930:00 - 49970:00

0 to one build these apps and if I can

## 49970:00 - 49995:00

say one interesting thing is when we

## 49995:00 - 50035:00

launched windsurf actually we tked

## 50035:00 - 50060:00

everyone at our company to go out and

## 50060:00 - 50090:00

build an app with Windsorf that included

## 50090:00 - 50125:00

our go to market team and our sales team

## 50125:00 - 50155:00

and there was a crazy stat that I think

## 50155:00 - 50180:00

people would find surprising but we've

## 50180:00 - 50215:00

saved over half a million dollars of of

## 50215:00 - 50245:00

SAS products we were going to buy

## 50245:00 - 50270:00

because our go to market team has now

## 50270:00 - 50305:00

built apps instead of buying them. Like

## 50305:00 - 50340:00

our head of partnerships instead of

## 50340:00 - 50375:00

buying a partner portal product has

## 50375:00 - 50420:00

actually built his own partner portal,

## 50420:00 - 50475:00

right? And that was that you know he had

## 50475:00 - 50525:00

never built software in the past. So and

## 50525:00 - 50550:00

we've actually come up with ways inside

## 50550:00 - 50580:00

the company to deploy these apps easily

## 50580:00 - 50620:00

in a secure way. And we're actually now

## 50620:00 - 50650:00

like building very very custom software

## 50650:00 - 50675:00

for our company to operate more

## 50675:00 - 50710:00

efficiently which is I would not have

## 50710:00 - 50740:00

expected this probably 6 months ago.

## 50740:00 - 50775:00

That is incredibly interesting. Uh you

## 50775:00 - 50805:00

don't need to name company names but I

## 50805:00 - 50830:00

guess what's a space you're least

## 50830:00 - 50850:00

bullish on that you think is going to

## 50850:00 - 50885:00

have the most problem here with company

## 50885:00 - 50905:00

people building their own version of

## 50905:00 - 50950:00

these sorts of products? You know, I

## 50950:00 - 51000:00

think maybe my viewpoint are these very

## 51000:00 - 51065:00

very verticalized niche products I think

## 51065:00 - 51110:00

are going to get they're going to get

## 51110:00 - 51155:00

competed down a ton. And I think sales

## 51155:00 - 51180:00

products are an example of one of these

## 51180:00 - 51230:00

things, right? You and and maybe this is

## 51230:00 - 51260:00

a I don't want to be like very negative,

## 51260:00 - 51295:00

but it's very hard inside a company like

## 51295:00 - 51325:00

ours to task our best engineers to build

## 51325:00 - 51360:00

a best-in-class sales product. there's

## 51360:00 - 51400:00

not enough interest to do that or to

## 51400:00 - 51445:00

build a best-in-class legal legal

## 51445:00 - 51480:00

software product or finance software

## 51480:00 - 51515:00

product. It's very very hard for us to

## 51515:00 - 51545:00

right and actually that's a very big

## 51545:00 - 51570:00

moat for these companies that they were

## 51570:00 - 51590:00

that built these products that they were

## 51590:00 - 51620:00

able to come out have an opinionated

## 51620:00 - 51655:00

stance on how to do this hire good

## 51655:00 - 51680:00

enough engineers to go out and build the

## 51680:00 - 51720:00

software and our company's unwilling to

## 51720:00 - 51745:00

do that. So previously we would go out

## 51745:00 - 51780:00

and buy the technology right uh because

## 51780:00 - 51815:00

there would be no alternative but now

## 51815:00 - 51850:00

one of the crazy things that uh is that

## 51850:00 - 51890:00

the domain specialists now have access

## 51890:00 - 51930:00

to build the tools that they ultimately

## 51930:00 - 51970:00

wanted right which is actually crazy

## 51970:00 - 52005:00

right if you think about why why were

## 52005:00 - 52040:00

these software companies able to exist

## 52040:00 - 52065:00

uh these vertical software companies the

## 52065:00 - 52095:00

reason is because they had many features

## 52095:00 - 52130:00

the kitchen sink of features worked for

## 52130:00 - 52165:00

a lot of companies but each individual

## 52165:00 - 52195:00

company only wanted 10% of the features

## 52195:00 - 52225:00

but the problem is each indiv individual

## 52225:00 - 52250:00

company was not capable of maintaining a

## 52250:00 - 52285:00

piece of software or building the custom

## 52285:00 - 52310:00

piece of software for 10% of the

## 52310:00 - 52335:00

features. But that is now changed

## 52335:00 - 52370:00

entirely. Now they can and there's

## 52370:00 - 52385:00

always Yeah, there's always been the

## 52385:00 - 52410:00

story of like why would I spend any time

## 52410:00 - 52440:00

building my own software if I could just

## 52440:00 - 52475:00

but now it's like five minutes of time

## 52475:00 - 52505:00

like it's five minutes and maybe even

## 52505:00 - 52545:00

more custom to your to your system,

## 52545:00 - 52565:00

right? Like how many times have you

## 52565:00 - 52590:00

bought a piece of bought a software and

## 52590:00 - 52620:00

you you're almost like why is there no

## 52620:00 - 52665:00

integration to X and I actually use X?

## 52665:00 - 52690:00

How annoying is that? that actually

## 52690:00 - 52720:00

makes the software less useful to you.

## 52720:00 - 52745:00

So, I think what's cool is when you go

## 52745:00 - 52770:00

back, if someone zooms back to the

## 52770:00 - 52795:00

beginning of when you started the demo,

## 52795:00 - 52840:00

it's basically a PM talking to an

## 52840:00 - 52915:00

engineer. Hey, uh, build me a Airbnb for

## 52915:00 - 52965:00

dogs. Here's a stupid mock that I made

## 52965:00 - 52995:00

like with some boxes. Like, that's

## 52995:00 - 53035:00

that's almost like a bad PM uh, talking

## 53035:00 - 53070:00

to an engineer and it just actually

## 53070:00 - 53105:00

works. That's what's insane about this.

## 53105:00 - 53130:00

And so that's why this example you're

## 53130:00 - 53170:00

sharing of go to market folks building

## 53170:00 - 53195:00

their own things. It's like they don't

## 53195:00 - 53230:00

need to know anything about product

## 53230:00 - 53260:00

building. It's just describe it in some

## 53260:00 - 53305:00

ridiculous way and draw a couple boxes

## 53305:00 - 53325:00

of what you want it to look like and it

## 53325:00 - 53350:00

makes something which shows that agency

## 53350:00 - 53370:00

is what matters. If you have a product

## 53370:00 - 53400:00

manager that has an idea, there's no

## 53400:00 - 53440:00

reason for why that idea cannot be like

## 53440:00 - 53475:00

more well fleshed out, right? Like how

## 53475:00 - 53500:00

many times do you have a product manager

## 53500:00 - 53545:00

that just continualize ideas but it just

## 53545:00 - 53585:00

feels like they are extremely unsure on

## 53585:00 - 53610:00

how to execute on it. They just want to

## 53610:00 - 53655:00

say things for the sake of saying things

## 53655:00 - 53685:00

but for the people that have ideas and a

## 53685:00 - 53715:00

lot of I guess agency they can go out

## 53715:00 - 53745:00

and like prove out what they want

## 53745:00 - 53785:00

without any sort of external resources.

## 53785:00 - 53825:00

I think uh even more acutely for product

## 53825:00 - 53865:00

folks listening to this uh it's the the

## 53865:00 - 53895:00

salesperson coming to you being like hey

## 53895:00 - 53925:00

I want this thing it's going to help me

## 53925:00 - 53950:00

with my sales team and you're like I

## 53950:00 - 53975:00

don't have a million things to build I

## 53975:00 - 54005:00

don't have time for this and so that

## 54005:00 - 54030:00

problem goes away which I think will

## 54030:00 - 54060:00

make a lot of product leaders really

## 54060:00 - 54110:00

happy the model that this is sitting on

## 54110:00 - 54165:00

is it sonnet yeah so just to break down

## 54165:00 - 54200:00

how it ultimately works we have a model

## 54200:00 - 54230:00

that does planning and I would say right

## 54230:00 - 54260:00

now sonnet is a really really good

## 54260:00 - 54310:00

planning model I OpenAI's GPT40 is also

## 54310:00 - 54360:00

good. But the crazy thing is what we try

## 54360:00 - 54405:00

to do is we try to make the the

## 54405:00 - 54435:00

anthropic based model or sonnet model

## 54435:00 - 54465:00

try to do as much of the highle planning

## 54465:00 - 54500:00

as possible. And then what we try to do

## 54500:00 - 54525:00

internally is run all the models

## 54525:00 - 54555:00

necessary to do high quality retrieval

## 54555:00 - 54585:00

for the agent. As you could see the

## 54585:00 - 54605:00

agent needed to understand what the rest

## 54605:00 - 54645:00

of the codebase ultimately did. U we

## 54645:00 - 54670:00

actually make sure we run models to

## 54670:00 - 54690:00

actually chunk up the entire codebase

## 54690:00 - 54725:00

and understand the codebase. Uh so that

## 54725:00 - 54755:00

obviously it would not be a good idea if

## 54755:00 - 54785:00

we had a 100 million line codebase to

## 54785:00 - 54820:00

send that entire codebase to anthropic.

## 54820:00 - 54845:00

First of all, you couldn't do that.

## 54845:00 - 54885:00

That's over 1.5 billion tokens of code,

## 54885:00 - 54905:00

right? So obviously that would be three

## 54905:00 - 54935:00

orders of my three or four orders of my

## 54935:00 - 54960:00

larger than the largest context lengths

## 54960:00 - 54995:00

right now. But you also wouldn't want to

## 54995:00 - 55020:00

do that from like a cost and latency

## 55020:00 - 55050:00

standpoint too. So that's like one. And

## 55050:00 - 55080:00

the second piece that you saw was the

## 55080:00 - 55120:00

model is able to very quickly make edits

## 55120:00 - 55145:00

to the to the software as well. We have

## 55145:00 - 55175:00

custom models that we built that are

## 55175:00 - 55205:00

post-trained on top of popular open

## 55205:00 - 55245:00

source models that can make these edits

## 55245:00 - 55275:00

really really quickly to the codebase.

## 55275:00 - 55300:00

And and the reason why you would want to

## 55300:00 - 55345:00

do that is it's a faster and b also that

## 55345:00 - 55375:00

model can actually have more of the

## 55375:00 - 55420:00

codebase in context too. So it can be

## 55420:00 - 55455:00

better at applying changes than even

## 55455:00 - 55495:00

anthropics model too. So I think the way

## 55495:00 - 55520:00

we like to think about it is our only

## 55520:00 - 55545:00

goal is how do we build the best product

## 55545:00 - 55570:00

possible, right? How do we build the

## 55570:00 - 55595:00

best product possible and how do we how

## 55595:00 - 55620:00

do we make the ceiling as high as

## 55620:00 - 55645:00

possible? And we will go out and build

## 55645:00 - 55670:00

models and train models wherever

## 55670:00 - 55690:00

necessary. But if we're not going to be

## 55690:00 - 55720:00

good at good at a task and we think the

## 55720:00 - 55745:00

open source is better or anthropic is

## 55745:00 - 55765:00

better, we'll go and just use the open

## 55765:00 - 55805:00

source or anthropy. And so the models

## 55805:00 - 55830:00

you guys are building those are built on

## 55830:00 - 55850:00

open source models that people are

## 55850:00 - 55875:00

releasing. Yeah. Interestingly, the one

## 55875:00 - 55900:00

that does retrieval is actually

## 55900:00 - 55925:00

completely pre-trained inhouse that

## 55925:00 - 55970:00

actually does that. But yeah, for for a

## 55970:00 - 55995:00

lot of different pieces, it's it's based

## 55995:00 - 56035:00

on open source for interestingly for the

## 56035:00 - 56075:00

one that does uh that does the edits and

## 56075:00 - 56115:00

autocomplete that is also in-house. Like

## 56115:00 - 56140:00

as you're typing, we actually do some

## 56140:00 - 56165:00

autocomplete related stuff. I'm happy to

## 56165:00 - 56190:00

show that, but I think a lot of users

## 56190:00 - 56235:00

are familiar with that capability. Um so

## 56235:00 - 56255:00

I think the way we like to look at it is

## 56255:00 - 56285:00

like what could we be best at and we

## 56285:00 - 56310:00

will go ahead and trade. But if we're

## 56310:00 - 56335:00

not going to be best at it, we should

## 56335:00 - 56365:00

not just for the sake of ego go out and

## 56365:00 - 56400:00

trade something. This may be getting too

## 56400:00 - 56420:00

technical, but just is there anything

## 56420:00 - 56450:00

interesting around what you train on?

## 56450:00 - 56475:00

Yeah. So, one of the one of the

## 56475:00 - 56505:00

interesting things that we have from our

## 56505:00 - 56540:00

users, and this is like where we try to

## 56540:00 - 56575:00

think like why would we be any better?

## 56575:00 - 56625:00

It's that actually every hour we get

## 56625:00 - 56655:00

probably tens of millions of pieces of

## 56655:00 - 56685:00

feedback from our users. We get a lot of

## 56685:00 - 56715:00

feedback on what they like and what they

## 56715:00 - 56735:00

don't like. For something like

## 56735:00 - 56765:00

autocomplete, we get a lot of preference

## 56765:00 - 56805:00

data. A lot of preference data. And the

## 56805:00 - 56830:00

preference data is weird. It doesn't

## 56830:00 - 56850:00

look like data that you find on the

## 56850:00 - 56890:00

internet. It's like data as the user is

## 56890:00 - 56920:00

typing, right? Imagine you're typing

## 56920:00 - 56965:00

typing um some code in a codebase. The

## 56965:00 - 56985:00

code's going to be incomplete as you're

## 56985:00 - 57010:00

typing it, right? It's not going to be

## 57010:00 - 57040:00

in a full-fledged form. It's not like it

## 57040:00 - 57080:00

is on GitHub. But we have a lot of data

## 57080:00 - 57115:00

that looks like this. So, we are

## 57115:00 - 57140:00

uniquely well positioned to actually

## 57140:00 - 57165:00

build a good model that can complete

## 57165:00 - 57190:00

code even when it's in an incomplete

## 57190:00 - 57230:00

state when the models that are out

## 57230:00 - 57255:00

there, the frontier models that consume

## 57255:00 - 57290:00

very little code that looks like this.

## 57290:00 - 57320:00

So for that case we're like hey we can

## 57320:00 - 57345:00

go out and do a much better job

## 57345:00 - 57375:00

potentially right and we'll go out and

## 57375:00 - 57405:00

train models on all the preference data

## 57405:00 - 57430:00

we have the same is kind of true in

## 57430:00 - 57465:00

retrieval right there's a way to find

## 57465:00 - 57490:00

out are we retrieving the right data

## 57490:00 - 57510:00

right did the user accept the code

## 57510:00 - 57545:00

change after that was the retrieval

## 57545:00 - 57565:00

actually a good retrieval a signal that

## 57565:00 - 57615:00

we can get so basically the way we like

## 57615:00 - 57640:00

to look at it is if something is just

## 57640:00 - 57685:00

purely like code planning there's not a

## 57685:00 - 57710:00

great reason why we would be the best at

## 57710:00 - 57750:00

that right I think that would that would

## 57750:00 - 57785:00

not be a I can't come up with a coherent

## 57785:00 - 57810:00

argument for that. But for something

## 57810:00 - 57845:00

that looks more along the lines of, hey,

## 57845:00 - 57875:00

here's an intermediate codebase that is

## 57875:00 - 57910:00

is very gnarly and here are some changes

## 57910:00 - 57955:00

that need to get made and we we know the

## 57955:00 - 57975:00

evolution of the code or we've seen the

## 57975:00 - 58000:00

evolution of code across millions of

## 58000:00 - 58040:00

users. Um, we feel like we can do a

## 58040:00 - 58065:00

great job with it. I think what's

## 58065:00 - 58085:00

interesting about this is this is

## 58085:00 - 58125:00

another uh

## 58125:00 - 58160:00

differentiator for companies that end up

## 58160:00 - 58180:00

winning in the space is you just have

## 58180:00 - 58205:00

more and more of that data than other

## 58205:00 - 58245:00

companies if you're ahead. Yeah, this is

## 58245:00 - 58275:00

sort of why maybe at a high level like

## 58275:00 - 58310:00

we like the 0ero to1 app building

## 58310:00 - 58345:00

product space. I think it's really it's

## 58345:00 - 58370:00

like a good product space, but

## 58370:00 - 58395:00

ultimately I think it needs to boil down

## 58395:00 - 58425:00

to you understanding the code because

## 58425:00 - 58465:00

otherwise you're living at too high a

## 58465:00 - 58510:00

plane where it's not clear why you would

## 58510:00 - 58535:00

be able to be the best at that compared

## 58535:00 - 58585:00

to everyone else. It's not really clear

## 58585:00 - 58620:00

as a company. You mean as a company? It

## 58620:00 - 58645:00

feels like it might get like competitive

## 58645:00 - 58705:00

in a way that it's not clear like where

## 58705:00 - 58730:00

you would continue to differentiate over

## 58730:00 - 58765:00

and over with time. I see. Because if

## 58765:00 - 58790:00

they're just sitting on top of sonnet

## 58790:00 - 58825:00

and just doing what every other sonnet

## 58825:00 - 58870:00

rapper is doing, there's not a lot of

## 58870:00 - 58910:00

differentiation or or it depends on how

## 58910:00 - 58935:00

you do it. But maybe if I was to say

## 58935:00 - 58960:00

this, if you're if the inputs you're

## 58960:00 - 58995:00

consuming are just web elements, like

## 58995:00 - 59040:00

extremely high level web elements, then

## 59040:00 - 59075:00

then the interface might be like high

## 59075:00 - 59115:00

level enough that it's it's hard to

## 59115:00 - 59140:00

maybe get better than maybe what the

## 59140:00 - 59170:00

frontier models are doing just across

## 59170:00 - 59200:00

the board. You just better off just

## 59200:00 - 59245:00

plugging in for everything. Got it.

## 59245:00 - 59270:00

Awesome. One thing I wanted to come back

## 59270:00 - 59290:00

to that I wrote down that I think is

## 59290:00 - 59315:00

really important for people to

## 59315:00 - 59345:00

understand. You talked about how with

## 59345:00 - 59380:00

Windsurf it's not necessar there's like

## 59380:00 - 59420:00

a boilerplate code base that you you

## 59420:00 - 59445:00

want to start with because it's actually

## 59445:00 - 59480:00

because it's not a abstracted 0 to1 app

## 59480:00 - 59515:00

builder. It's a actual IDE you're coding

## 59515:00 - 59560:00

in. And you talked about how it has to

## 59560:00 - 59585:00

install dependencies which is kind of

## 59585:00 - 59615:00

this painful thing and the the reason it

## 59615:00 - 59635:00

has to do that is because it's running

## 59635:00 - 59680:00

locally on your machine versus in the

## 59680:00 - 59720:00

cloud like say lovable and replet and

## 59720:00 - 59750:00

all these guys. Although I think Bolt

## 59750:00 - 59775:00

runs in your browser in this really cool

## 59775:00 - 59805:00

way. Uh so that's an important

## 59805:00 - 59825:00

distinction. This is like you're running

## 59825:00 - 59850:00

this locally on your machine and has all

## 59850:00 - 59880:00

the all the libraries you need to

## 59880:00 - 59915:00

actually run it. No, I think that's

## 59915:00 - 59955:00

important. I think we believe a lot of

## 59955:00 - 59995:00

people sort of build software in what

## 59995:00 - 60020:00

are called like code spaces and things

## 60020:00 - 60050:00

in a remote machine. I just think it's

## 60050:00 - 60085:00

that a lot of developers like building

## 60085:00 - 60115:00

locally. for what you said. Uh like if

## 60115:00 - 60135:00

you're doing things that are more than

## 60135:00 - 60165:00

just full stack applications, you might

## 60165:00 - 60190:00

have dependencies on your machine that

## 60190:00 - 60220:00

are just like system dependencies that

## 60220:00 - 60240:00

are just gnarly to install. Let's

## 60240:00 - 60265:00

imagine you're building a GPU based

## 60265:00 - 60295:00

application and the Nvidia drivers are

## 60295:00 - 60330:00

necessary. You just want to give people

## 60330:00 - 60355:00

the flexibility to build where they can

## 60355:00 - 60400:00

build. And I think you know the IDE and

## 60400:00 - 60420:00

building locally has been a thing that

## 60420:00 - 60445:00

people have done for you know decades.

## 60445:00 - 60470:00

So probably it's not going to go away in

## 60470:00 - 60500:00

the next like couple years. I love that

## 60500:00 - 60525:00

your sales folks now are running like

## 60525:00 - 60570:00

local host servers and well with the

## 60570:00 - 60600:00

browser previews it's easier, right? You

## 60600:00 - 60620:00

kind of just like open it up on the

## 60620:00 - 60660:00

side. Yeah. Yeah. Oh my god. Okay, I

## 60660:00 - 60680:00

have a few more questions just about how

## 60680:00 - 60730:00

you think and operate at uh at Kodium.

## 60730:00 - 60760:00

So you guys are kind of at the forefront

## 60760:00 - 60800:00

of how product teams are going to

## 60800:00 - 60830:00

operate like you are seeing the future

## 60830:00 - 60865:00

every day. And so I'm curious if there's

## 60865:00 - 60890:00

ways you guys have structured your

## 60890:00 - 60930:00

teams, engineers, product design that

## 60930:00 - 60950:00

might be different from how other

## 60950:00 - 60975:00

companies are doing it or have tried

## 60975:00 - 60995:00

stuff that has worked really well or

## 60995:00 - 61015:00

tried stuff that has been a huge

## 61015:00 - 61050:00

disaster. You know, one interesting

## 61050:00 - 61085:00

decision that we kind of have for core

## 61085:00 - 61125:00

engineering is that we don't have pure

## 61125:00 - 61160:00

product managers for for the core

## 61160:00 - 61200:00

engineering side of the company. And by

## 61200:00 - 61230:00

the way, that's purely because we build

## 61230:00 - 61295:00

for developers and our our product is is

## 61295:00 - 61325:00

built by developers. So I think the

## 61325:00 - 61370:00

intuition from our own developers are

## 61370:00 - 61405:00

are is is hopefully hopefully valuable.

## 61405:00 - 61430:00

If not, we might be hiring the wrong

## 61430:00 - 61465:00

type of people. So I think like our

## 61465:00 - 61490:00

developers are in some sense flexing to

## 61490:00 - 61520:00

be like more product conventional

## 61520:00 - 61545:00

product managers. Now on the other hand,

## 61545:00 - 61560:00

if we were building something that

## 61560:00 - 61595:00

looked more like Uber or the persona was

## 61595:00 - 61625:00

very different and we didn't ourselves

## 61625:00 - 61650:00

understand it. I think we would not be

## 61650:00 - 61675:00

the organization wouldn't look the way

## 61675:00 - 61730:00

it looks. uh for the enterprise side of

## 61730:00 - 61765:00

the company because we do work with a

## 61765:00 - 61790:00

lot of large enterprises where the

## 61790:00 - 61810:00

requirements are not something that like

## 61810:00 - 61835:00

our engineers would automatically

## 61835:00 - 61855:00

understand, right? I don't think our

## 61855:00 - 61880:00

engineers wake up and they're like we

## 61880:00 - 61920:00

need Fed ramp, right? Uh like this is

## 61920:00 - 61935:00

probably something that a lot of

## 61935:00 - 61970:00

customers come to us with and tell us.

## 61970:00 - 62005:00

We have people that kind of like flex in

## 62005:00 - 62025:00

this product strategy role that

## 62025:00 - 62055:00

understand kind of what the what the

## 62055:00 - 62090:00

customer wants and understands the

## 62090:00 - 62120:00

technical capabilities that we have to

## 62120:00 - 62175:00

under to best kind of build a a product

## 62175:00 - 62200:00

uh that would that would sort of help

## 62200:00 - 62240:00

them at scale. So I think I think we

## 62240:00 - 62265:00

have an interesting organization in this

## 62265:00 - 62295:00

regard but mostly I would say because we

## 62295:00 - 62330:00

are a developer based product right um I

## 62330:00 - 62365:00

would say that's true and then also kind

## 62365:00 - 62385:00

of like what you said for the

## 62385:00 - 62430:00

engineering team itself we are you know

## 62430:00 - 62460:00

the the team structure is it's it's

## 62460:00 - 62495:00

fairly flat we try to go with two pizza

## 62495:00 - 62535:00

teams teams that are fairly small just

## 62535:00 - 62560:00

because I think the problem is when a

## 62560:00 - 62590:00

team gets too big the person leading the

## 62590:00 - 62610:00

team is no longer able to get in the

## 62610:00 - 62650:00

weeds of the technology itself and I

## 62650:00 - 62675:00

think in a space that's moving this

## 62675:00 - 62710:00

quickly I think it's dangerous to have

## 62710:00 - 62730:00

leaders that don't understand the

## 62730:00 - 62760:00

technology deeply and are like and not

## 62760:00 - 62790:00

building it's like very very dangerous

## 62790:00 - 62830:00

because there's too much like armchair

## 62830:00 - 62870:00

quarterbacking and uh so so I think I

## 62870:00 - 62915:00

think that's like maybe maybe uh maybe

## 62915:00 - 62950:00

like one other decision we made and then

## 62950:00 - 62990:00

teams are very very flexible so if we

## 62990:00 - 63030:00

decide something is a new priority we're

## 63030:00 - 63065:00

very quick to kind of like change the

## 63065:00 - 63100:00

way a team looks and and it's very

## 63100:00 - 63150:00

centrally planned in this regard the two

## 63150:00 - 63185:00

pizza team concept I saw a tweet long

## 63185:00 - 63220:00

ago where someone from in India was like

## 63220:00 - 63240:00

there's all these talk about two in

## 63240:00 - 63270:00

pizza teams but pizzas in India are much

## 63270:00 - 63300:00

smaller and so the teams end up being

## 63300:00 - 63320:00

smaller and they're like why can't we

## 63320:00 - 63355:00

build as much as these teams in the

## 63355:00 - 63430:00

US oh man okay so how many PMs do you

## 63430:00 - 63465:00

have so you said you have 150 employees

## 63465:00 - 63500:00

something like that yeah we have so in

## 63500:00 - 63520:00

terms of like the product strategy

## 63520:00 - 63550:00

function we have we have uh we have

## 63550:00 - 63585:00

three people in that role right now I

## 63585:00 - 63625:00

see so it's like product it's like there

## 63625:00 - 63650:00

and their title is like is product

## 63650:00 - 63675:00

strategy not necessarily product

## 63675:00 - 63705:00

management that's right Interesting. And

## 63705:00 - 63745:00

then 50 engineers. You said 80ish sales

## 63745:00 - 63780:00

folks. Yes, that's right. And then

## 63780:00 - 63810:00

obviously we have functions like

## 63810:00 - 63845:00

recruiting, you know, parts of GNA like

## 63845:00 - 63880:00

finance, right? We have marketing at the

## 63880:00 - 63915:00

company, right? So some other some other

## 63915:00 - 63945:00

functions internally as well. What's

## 63945:00 - 63970:00

interesting and this is something you

## 63970:00 - 64005:00

hear all the time with companies like

## 64005:00 - 64030:00

Dario for example from Anthropic talking

## 64030:00 - 64055:00

about how 90% of code is going to be

## 64055:00 - 64100:00

written by AI. Uh but all at the same

## 64100:00 - 64120:00

time all you guys are hiring engineers

## 64120:00 - 64170:00

like crazy. Yeah. Is do is there is that

## 64170:00 - 64195:00

contradictory? Is that contradictory?

## 64195:00 - 64220:00

Will there be an inflection point of

## 64220:00 - 64245:00

like, all right, now we don't need them

## 64245:00 - 64265:00

anymore. You know, I think it really

## 64265:00 - 64295:00

comes down to do you get incremental

## 64295:00 - 64320:00

value by adding more engineers

## 64320:00 - 64345:00

internally? Like I'm going to take first

## 64345:00 - 64375:00

of all, you know, maybe just to set the

## 64375:00 - 64400:00

record straight, if AI is writing over

## 64400:00 - 64440:00

90% of the code, that doesn't mean

## 64440:00 - 64485:00

engineers are 10x as productive, right?

## 64485:00 - 64505:00

Engineers spend more time than just

## 64505:00 - 64535:00

writing code. They review code, test

## 64535:00 - 64570:00

code, debug code, design code, deploy

## 64570:00 - 64605:00

code, right? Navigate code. There's

## 64605:00 - 64625:00

probably like a lot of different things

## 64625:00 - 64660:00

engineers do. There's this one famous

## 64660:00 - 64685:00

law in parallel computing. It's called

## 64685:00 - 64715:00

Almdall's law. I don't know if I don't

## 64715:00 - 64735:00

know if you've heard about it, but it

## 64735:00 - 64755:00

basically says if you have a graph of

## 64755:00 - 64790:00

tasks and you have this critical path

## 64790:00 - 64820:00

and you take any one task and

## 64820:00 - 64850:00

parallelize it a ton, which is make it

## 64850:00 - 64880:00

almost take zero amount of time, there's

## 64880:00 - 64915:00

still limit of the amount of of how much

## 64915:00 - 64945:00

faster it made the whole process go. So

## 64945:00 - 64970:00

maybe put simply, let's say you have a

## 64970:00 - 65015:00

100 units of time and only 30 units of

## 65015:00 - 65040:00

time is being spent writing software and

## 65040:00 - 65070:00

I took the 30 and made it three. I only

## 65070:00 - 65105:00

took the 100 and made it 73. it's still

## 65105:00 - 65140:00

only 27% improvement right in the grand

## 65140:00 - 65180:00

scheme of things. So I think look we're

## 65180:00 - 65210:00

definitely seeing over 30 maybe close to

## 65210:00 - 65240:00

40% productivity improvements but I

## 65240:00 - 65260:00

think for the vision that we're solving

## 65260:00 - 65305:00

for I I think like you know even if I

## 65305:00 - 65330:00

were to say the company in the longtale

## 65330:00 - 65370:00

had 200 engineers probably be too low

## 65370:00 - 65410:00

still at that point. So the question is

## 65410:00 - 65430:00

like how much more productivity do you

## 65430:00 - 65475:00

get per person you know actually maybe

## 65475:00 - 65510:00

just to even say one other thing for

## 65510:00 - 65540:00

some of these large companies let's say

## 65540:00 - 65575:00

you took the CIO of a company like JP

## 65575:00 - 65625:00

Morgan Chase right her budget on

## 65625:00 - 65670:00

software every year is $17 billion and

## 65670:00 - 65705:00

you there's over 50,000 engineers inside

## 65705:00 - 65750:00

the company right and you told her hey

## 65750:00 - 65785:00

like each of these engineers are now

## 65785:00 - 65815:00

able to produce more technology that's

## 65815:00 - 65855:00

effectively what you've done right the

## 65855:00 - 65885:00

right calculus that JP Morgan Chase or

## 65885:00 - 65935:00

any of these companies will make is the

## 65935:00 - 65970:00

ROI of building technology has actually

## 65970:00 - 66010:00

gone up. So the opportunity cost of not

## 66010:00 - 66045:00

investing more into technology has gone

## 66045:00 - 66070:00

up which means that you should just

## 66070:00 - 66100:00

invest even more and maybe in the short

## 66100:00 - 66135:00

term you have even more engineers. Right

## 66135:00 - 66160:00

now that's not true across the board.

## 66160:00 - 66180:00

There are some companies that are happy

## 66180:00 - 66200:00

with the amount of technology they're

## 66200:00 - 66220:00

building and there's a ceiling on the

## 66220:00 - 66245:00

amount of technology they want to build.

## 66245:00 - 66270:00

But for companies that actually have a

## 66270:00 - 66315:00

very high technology technology ceiling,

## 66315:00 - 66340:00

this doesn't mean you stop. This

## 66340:00 - 66375:00

actually means you hire more. This is a

## 66375:00 - 66405:00

great bullc case for engineers. I feel

## 66405:00 - 66430:00

like there's like the canary in the coal

## 66430:00 - 66450:00

mine for the engineering profession is

## 66450:00 - 66485:00

when companies like yours slow down on

## 66485:00 - 66530:00

hiring engineers. That's not happening.

## 66530:00 - 66565:00

I think is also hiring a lot. Yeah,

## 66565:00 - 66590:00

everyone is. So, I think that's really

## 66590:00 - 66615:00

promising. I think if you're in college

## 66615:00 - 66645:00

still makes sense to get into

## 66645:00 - 66680:00

engineering at this point. Yeah. Okay.

## 66680:00 - 66710:00

Let me ask you this question as a kind

## 66710:00 - 66750:00

of a a final question maybe. What's

## 66750:00 - 66780:00

maybe the most

## 66780:00 - 66820:00

counterintuitive thing you've learned

## 66820:00 - 66865:00

about building AI products, building

## 66865:00 - 66895:00

wind surf in this just being in this

## 66895:00 - 66930:00

space? I think one of the weird things

## 66930:00 - 66970:00

is online everyone is very excited about

## 66970:00 - 67005:00

the short-term wins that we're making,

## 67005:00 - 67030:00

right? Like what we're putting out maybe

## 67030:00 - 67055:00

weekly. We do these waves every couple

## 67055:00 - 67090:00

weeks, but actually like a lot of the

## 67090:00 - 67120:00

bets we're making inside the company are

## 67120:00 - 67150:00

for things that are not, you know, 3,

## 67150:00 - 67175:00

four weeks, maybe three, six months,

## 67175:00 - 67205:00

nine months away. That's what we're

## 67205:00 - 67235:00

working on internally because I think

## 67235:00 - 67265:00

this is kind of like Lenny what I was

## 67265:00 - 67305:00

mentioning to you before like one of the

## 67305:00 - 67330:00

goals that I tell everyone at our

## 67330:00 - 67355:00

company is we should be cannibalizing

## 67355:00 - 67375:00

the existing state of our product every

## 67375:00 - 67400:00

6 to 12

## 67400:00 - 67440:00

months. Every 6 to 12 months it should

## 67440:00 - 67475:00

make our existing product look silly. It

## 67475:00 - 67500:00

should almost make the form factor of

## 67500:00 - 67540:00

existing product look dumb. So it

## 67540:00 - 67575:00

there's this weird tension where you

## 67575:00 - 67605:00

want to have a product in market and you

## 67605:00 - 67635:00

want to incrementally iterate and listen

## 67635:00 - 67665:00

to users and keep making it making it

## 67665:00 - 67700:00

better and better. But I would say we

## 67700:00 - 67735:00

were the first aentic IDE product out

## 67735:00 - 67765:00

there, right? We that's what we landed

## 67765:00 - 67815:00

with and I think that the value of that

## 67815:00 - 67835:00

is going to depreciate very quickly

## 67835:00 - 67875:00

unless we continue to reprove ourselves

## 67875:00 - 67905:00

and we will need to reprove ourselves in

## 67905:00 - 67925:00

ways in which our users are not even

## 67925:00 - 67975:00

asking. So there's this tension here

## 67975:00 - 68010:00

where incremental feels very safe,

## 68010:00 - 68045:00

right? Add this one more button. Users

## 68045:00 - 68070:00

say, "Hey, I would like to be able to

## 68070:00 - 68100:00

have this drop down to do X." But that

## 68100:00 - 68120:00

is not the reason why we're going to

## 68120:00 - 68155:00

win. That's just that's like a you know

## 68155:00 - 68180:00

that's almost table stakes. Yeah, we'll

## 68180:00 - 68205:00

decide to do some of these. We might not

## 68205:00 - 68230:00

decide to do a lot of these things, but

## 68230:00 - 68265:00

it's like it's these longer term efforts

## 68265:00 - 68295:00

inside the company that almost disrupt

## 68295:00 - 68325:00

the existing product that are ultimately

## 68325:00 - 68350:00

the reason why we're going to succeed.

## 68350:00 - 68385:00

Um, and it's this weird tension that you

## 68385:00 - 68410:00

need to have in your head of you can't

## 68410:00 - 68440:00

also not listen to your users at all

## 68440:00 - 68470:00

because they're the reasons they're the

## 68470:00 - 68505:00

reason you exist. This reminds me of a

## 68505:00 - 68540:00

recent podcast guest. We had Gar from

## 68540:00 - 68580:00

captions on the podcast and he he told

## 68580:00 - 68605:00

us that he had he has two road maps.

## 68605:00 - 68630:00

They have two road maps at the company.

## 68630:00 - 68665:00

They have the the the real road map like

## 68665:00 - 68695:00

the typical road map based on feature

## 68695:00 - 68730:00

request and user feedback and data and

## 68730:00 - 68745:00

things like that. And then they have the

## 68745:00 - 68790:00

secret road map which is completely not

## 68790:00 - 68825:00

informed by users or data. It's just

## 68825:00 - 68855:00

them making bets on where they think the

## 68855:00 - 68890:00

world is going. That's right. And I love

## 68890:00 - 68910:00

that he calls it the secret road map

## 68910:00 - 68940:00

just to make it very mysterious. That's

## 68940:00 - 68970:00

very smart. Okay. I have one more

## 68970:00 - 68990:00

question. I

## 68990:00 - 69020:00

apologize. What's one thing that you

## 69020:00 - 69050:00

wish you had known before starting

## 69050:00 - 69115:00

Kodium? Honestly, I I wish I had maybe

## 69115:00 - 69160:00

humility is like the the wrong term, but

## 69160:00 - 69200:00

this idea of just being okay with being

## 69200:00 - 69245:00

wrong faster. Um like I always think

## 69245:00 - 69275:00

about things on like when we make

## 69275:00 - 69310:00

decisions, me and my co-founder, uh we

## 69310:00 - 69335:00

always talk about it. We're almost like,

## 69335:00 - 69360:00

"Hey, I wish we had made the decision to

## 69360:00 - 69395:00

do this a couple months earlier. We

## 69395:00 - 69435:00

always talk about this." And the weird

## 69435:00 - 69460:00

thing is outside looking at everyone's

## 69460:00 - 69485:00

like, "Wow, like actually, you know, the

## 69485:00 - 69510:00

decision was made at the right time."

## 69510:00 - 69540:00

But in my head, I'm always banging my

## 69540:00 - 69565:00

head being like, what if we had made it

## 69565:00 - 69610:00

a couple months earlier? And I think

## 69610:00 - 69645:00

part of that is, you know, I I waxed

## 69645:00 - 69670:00

poetically about like, oh, you need to

## 69670:00 - 69710:00

be irrationally uh sort of optimistic

## 69710:00 - 69740:00

and uncompromisingly realistic, but it's

## 69740:00 - 69770:00

very hard to do this in practice, right?

## 69770:00 - 69795:00

Because you drink your own Kool-Aid,

## 69795:00 - 69815:00

too. It's very because if you're not

## 69815:00 - 69840:00

drinking your own Kool-Aid, you you

## 69840:00 - 69870:00

won't get up out of bed, right? The

## 69870:00 - 69890:00

answer is already solved. It's not

## 69890:00 - 69910:00

actually any of these startups. The

## 69910:00 - 69950:00

answer is Microsoft is going to be the

## 69950:00 - 69985:00

be the winner in any software category,

## 69985:00 - 70010:00

right? Isn't that isn't that the answer?

## 70010:00 - 70035:00

Uh just because of distribution,

## 70035:00 - 70070:00

resources, and capital, right? Uh

## 70070:00 - 70090:00

they're going to commoditize every

## 70090:00 - 70155:00

space. So I think I think in some ways

## 70155:00 - 70210:00

you this this amount of of just

## 70210:00 - 70250:00

understanding that hey like reevaluate

## 70250:00 - 70280:00

your hypothesis and get into an

## 70280:00 - 70325:00

uncomfortable space way more frequently

## 70325:00 - 70350:00

uh is is something I need to remind

## 70350:00 - 70385:00

myself even to this day and probably

## 70385:00 - 70410:00

something that I didn't know coming in

## 70410:00 - 70435:00

and starting the company. Right? I we

## 70435:00 - 70465:00

started the company at like peak zerp

## 70465:00 - 70500:00

time at that time probably like

## 70500:00 - 70520:00

everything seemed like it was going to

## 70520:00 - 70550:00

moon and there was probably a lot of

## 70550:00 - 70580:00

irrational confidence I would say uh

## 70580:00 - 70615:00

that we shouldn't have had maroon we

## 70615:00 - 70645:00

covered so much ground what an

## 70645:00 - 70670:00

incredible conversation I learned so

## 70670:00 - 70695:00

much just just sitting here listening

## 70695:00 - 70725:00

and asking you questions is there

## 70725:00 - 70745:00

anything else that you wanted to share

## 70745:00 - 70785:00

before or I leave listeners with any

## 70785:00 - 70820:00

last piece of nuggets or wisdom uh

## 70820:00 - 70860:00

before I let you go to to be honest I

## 70860:00 - 70890:00

could give predictions about the space

## 70890:00 - 70925:00

uh probably most of them are going to be

## 70925:00 - 70955:00

Um, I think the best thing to do is just

## 70955:00 - 70990:00

get your hands dirty with with all of

## 70990:00 - 71035:00

these products. And uh, I think one of

## 71035:00 - 71065:00

the most obvious things that's going to

## 71065:00 - 71105:00

happen is in the next year there will be

## 71105:00 - 71135:00

a tremendous amount of alpha for anyone

## 71135:00 - 71165:00

that is able to take maximum advantage

## 71165:00 - 71205:00

of these tools, right? Just imagine how

## 71205:00 - 71230:00

many of your co-workers just don't even

## 71230:00 - 71260:00

know the existence of these tools, don't

## 71260:00 - 71290:00

know what they can do, and how much less

## 71290:00 - 71335:00

productive they will be. Um, and uh, and

## 71335:00 - 71380:00

just I would just say get your hands as

## 71380:00 - 71400:00

dirty as possible, as quickly as

## 71400:00 - 71420:00

possible. And when you say get your

## 71420:00 - 71445:00

hands dirty, basically it's like

## 71445:00 - 71475:00

download with surf, start coding, ask it

## 71475:00 - 71500:00

to build things for you. Yeah. Build

## 71500:00 - 71550:00

apps, build apps. Um, start using it for

## 71550:00 - 71585:00

maybe even making making mocks,

## 71585:00 - 71625:00

modifying your existing codebase. Like

## 71625:00 - 71650:00

there's probably ways in which you could

## 71650:00 - 71670:00

be a force multiplier to your

## 71670:00 - 71695:00

organization in ways in which they never

## 71695:00 - 71735:00

even anticipated, right? Imagine if you

## 71735:00 - 71755:00

were a product manager that could

## 71755:00 - 71780:00

actually very quickly make edits to the

## 71780:00 - 71815:00

codebase and and just start pushing

## 71815:00 - 71845:00

changes yourself. You probably get a

## 71845:00 - 71865:00

tremendous amount of respect from your

## 71865:00 - 71895:00

own engineering peers. you could

## 71895:00 - 71915:00

probably get way more done because of

## 71915:00 - 71955:00

that. Um, it's just I feel like the

## 71955:00 - 71995:00

there's no there's no sort of uh ceiling

## 71995:00 - 72025:00

at that point. I think this is such an

## 72025:00 - 72060:00

under estimated point you're making

## 72060:00 - 72095:00

here. There's apps that can build things

## 72095:00 - 72130:00

from scratch and then there's apps like

## 72130:00 - 72155:00

this that can edit your existing

## 72155:00 - 72185:00

codebase if you're PM at like what's

## 72185:00 - 72210:00

what are the what's the largest company

## 72210:00 - 72250:00

you work with like people wise? Probably

## 72250:00 - 72295:00

like publicly I'd say let's just say JP

## 72295:00 - 72325:00

Morgan Chase for now. They have over

## 72325:00 - 72350:00

50,000 developers. Okay. So you could be

## 72350:00 - 72395:00

a PM at JP Morgan Chase and be like, I

## 72395:00 - 72425:00

have a I have a problem I need to solve.

## 72425:00 - 72460:00

I want to move this metric. I want to

## 72460:00 - 72500:00

change the step in the signup flow. You

## 72500:00 - 72540:00

you just open up Wind Surf and tell it

## 72540:00 - 72575:00

to do the thing you want. And then can

## 72575:00 - 72615:00

you push straight to GitHub and do a

## 72615:00 - 72660:00

Yeah, actually you could do that. Okay.

## 72660:00 - 72695:00

PR. Yeah, it could make a PR for you.

## 72695:00 - 72730:00

This is insane. Okay. The future is out

## 72730:00 - 72770:00

of control. Okay, we're doing this. That

## 72770:00 - 72785:00

was such an important point at the end

## 72785:00 - 72805:00

there because I think people may not

## 72805:00 - 72825:00

realize this. They see all these other

## 72825:00 - 72845:00

apps, they're like, "Oh, build all these

## 72845:00 - 72870:00

prototypes." But this is like

## 72870:00 - 72905:00

legitimately something a PM can actually

## 72905:00 - 72940:00

do work with. Yeah. When you think about

## 72940:00 - 72970:00

the people at least that I I don't know,

## 72970:00 - 73000:00

Lenny, who you respect the most, they

## 73000:00 - 73025:00

are the people that somehow despite

## 73025:00 - 73060:00

their title, their level of agency and

## 73060:00 - 73100:00

just output just to the all the way down

## 73100:00 - 73140:00

to the weeds to the highest level

## 73140:00 - 73175:00

strategy is just perfection, right? They

## 73175:00 - 73215:00

know when to go all the way down. And I

## 73215:00 - 73240:00

think, you know, sometimes you see

## 73240:00 - 73265:00

people that talk about roles and they

## 73265:00 - 73290:00

irrationally feel like, oh, because I'm

## 73290:00 - 73310:00

this role, I'm not allowed to touch

## 73310:00 - 73340:00

this. Well, now everything's open

## 73340:00 - 73370:00

season, right? And I think this is an

## 73370:00 - 73400:00

opportunity to almost go all the way

## 73400:00 - 73430:00

down to the weeds and all the way up to

## 73430:00 - 73460:00

the top, right? Um, and just be

## 73460:00 - 73510:00

effective on every level. Unbelievable.

## 73510:00 - 73535:00

All right. Well, with that, we'll leave

## 73535:00 - 73575:00

folks. Uh, Arun, thank you so much for

## 73575:00 - 73615:00

being here. Awesome. Thanks a lot. What

## 73615:00 - 73640:00

an incredible conversation. Thanks, Run.

## 73640:00 - 73700:00

And bye, everyone.

## 73700:00 - 73725:00

Thank you so much for listening. If you

## 73725:00 - 73750:00

found this valuable, you can subscribe

## 73750:00 - 73795:00

to the show on Apple Podcasts, Spotify,

## 73795:00 - 73840:00

or your favorite podcast app. Also,

## 73840:00 - 73870:00

please consider giving us a rating or

## 73870:00 - 73900:00

leaving a review as that really helps

## 73900:00 - 73940:00

other listeners find the podcast. You

## 73940:00 - 73975:00

can find all past episodes or learn more

## 73975:00 - 74010:00

about the show at

## 74010:00 - 74040:00

lennispodcast.com. See you in the next

## 74040:00+

episode.

