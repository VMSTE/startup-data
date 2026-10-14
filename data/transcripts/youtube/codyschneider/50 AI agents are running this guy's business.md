---
source: https://www.youtube.com/watch?v=3gmUnAmfnn4
title: 50 AI agents are running this guy's business
author: Cody Schneider
date: 2025-07-10
views: 3123
description: >-
  In this episode, Adam Silverman — co-founder & CEO of Agent Ops — dives deep
  into what “AI agents” actually are, why observability matters, and the very
  real marketing & growth automations companies are shipping today. From
  social-listening bots that draft Reddit replies to multi-agent pipelines that
  rebalance seven-figure ad budgets in real time, Adam lays out a practical
  playbook for founders, heads of growth, and non-technical operators who want
  to move from hype to hands-on results.


  Guest socials

  • LinkedIn: https://www.linkedin.com/in/adamsil

  • 𝕏 / Twitter: https://x.com/AtomSilverman

  • Company: https://agentops.ai


  Timestamps


  00:00 — Defining “agents”: reasoning-powered automations, not AGI

  00:54 — Introducing Adam & the 50+ internal agents his team uses daily

  03:32 — “Vibe marketing” and why every employee will soon have an AI assistant

  05:18 — Live example: an inbound-lead-scoring agent that books calls
  automatically

  08:11 — Metric shift: revenue / agent & revenue / token

  10:45 — Three-point filter for agent ROI: expensive, repeatable, low-risk
  tasks

  12:56 — Social-listening agents for Reddit, X & forums (human-in-the-loop
  posting)

  16:14 — OrcaBase + TripleWhale: agentic ad-spend rebalancing for e-com

  21:29 — WhisperFlow → Claude to generate entire email sequences in minutes

  25:04 — Multi-agent systems & OpenAI Agents SDK (Crew AI, Llama-Index, etc.)

  40:12 — Tech stack cheat-sheet: AgentQL, BrowserBase, Composio, Anthropic
  Claude 3, Gemini 1.5 Pro

  48:07 — Internal hackathons & “minimum viable post” culture for continuous
  learning


  Key Points


  • Observability is table-stakes. Enterprises won’t deploy agents without 99.99
  % reliability, so logging, evals & debugging are critical.

  • Marketing automations that already work:

  – Social-listening + auto-response (Reddit, X “Radar”)

  – Lead-scoring & routing directly inside Superhuman

  – Real-time ad-budget re-allocation with TripleWhale’s OrcaBase agents

  – UGC ad generation at ¢-scale via HeyGen API

  • Tooling matters: mix-and-match lower-cost LLMs (Gemini/Claude) for
  chain-of-thought tasks and premium models (GPT-4o) for reasoning or code.

  • Multi-agent ≠ many prompts. Think specialized “teammates” passing JSON, each
  with its own LLM, tools & memory.

  • Hire for AI-nativity, not job titles. A VA fluent in Cursor or WhisperFlow
  can 10× output overnight.

  • Run micro-hackathons. One day a month of structured tinkering keeps teams
  ahead of vendor fluff.


  Six Practical Plays You Can Steal

  Expensive + Repeatable + Low-Risk Audit

  Map every workflow; circle anything that costs $$$, repeats weekly, and won’t
  tank the business if it fails. Start there.


  Social-Listening Agent

  Radar (X) or manual Boolean search → Agent drafts replies → human approval →
  schedule via Buffer/Zapier.


  Ad-Spend Rebalancer

  Pipe TripleWhale or GA4 ROAS data into an agent that shifts budget between
  Meta, Google & TikTok every 60 min.


  Outbound “Industry Brief” Generator

  you.com’s Ari agent → 5-page PDF tailored to the prospect’s vertical → attach
  in first-touch email.


  Auto-Follow-Up Composer

  Fathom meeting transcript + Superhuman “Ask AI” → ready-to-send recap with
  action items.


  Internal Hackathon Framework

  • 15 min YouTube tutorial

  • 45 min build using Gumloop / Lutra AI (no-code)

  • Demo & share Loom — highest-impact sprint gets pushed to prod.


  Notable Quotes


  “We’ve got more agent headcount than human headcount.” — Adam Silverman

  “Stop talking AGI. Look for tasks that are expensive, repeatable, and low-risk
  — that’s where agents print money.”

  “Your revenue per employee metric just became revenue per token.”

  “Build once, sell twice: every podcast, video or doc should spawn emails,
  tweets and a downloadable PDF.”


  2025 Takeaway: The winners won’t be the teams with the biggest models; they’ll
  be the teams that turn everyday processes into measurable, observable agent
  workflows — and iterate on them faster than their competitors can finish a
  slide deck.


  #AIAgents #AgentOps #MarketingAutomation #GrowthHacking #StartupTips
  #ArtificialIntelligence #DigitalMarketing #Automation #AdamSilverman
  #2025Trends
tags:
  - cody schneider
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T11:52:40.947Z
---

# 50 AI agents are running this guy's business

## 00:00 - 25:00

We still don't know what AI agents are,

## 25:00 - 55:00

but we'll probably figure it out at some

## 55:00 - 85:00

point. But there's still no clear

## 85:00 - 120:00

definition of what an AI agent is. But

## 120:00 - 150:00

we'll probably figure that out, I'm

## 150:00 - 170:00

guessing, by the end of the year. While

## 170:00 - 215:00

I'm thinking about it is a workflow or

## 215:00 - 245:00

automation that has some type of

## 245:00 - 280:00

thinking logic built into it. And today,

## 280:00 - 305:00

that's what we're going deep on. I'm

## 305:00 - 340:00

hosting my friend Adam from Agent Ops.

## 340:00 - 370:00

They do agent observability. He's going

## 370:00 - 405:00

to share all the different ways that

## 405:00 - 435:00

they're seeing agents being implemented

## 435:00 - 460:00

within companies that they have as

## 460:00 - 480:00

clients. And then we're going to also

## 480:00 - 520:00

talk about marketing applications. And

## 520:00 - 540:00

then we're going to also talk about how

## 540:00 - 570:00

agents can be used within marketing,

## 570:00 - 595:00

specifically the ways that he's seeing

## 595:00 - 620:00

it being used by clients to do

## 620:00 - 650:00

activities for their sales team that

## 650:00 - 675:00

create leads. And this episode is

## 675:00 - 705:00

brought to you by claim podcasting.

## 705:00 - 735:00

Founder-led marketing is the most

## 735:00 - 760:00

effective way to grow your business in

## 760:00 - 790:00

2025. And a claim can make a founder

## 790:00 - 835:00

famous in 12 months with a podcast, an

## 835:00 - 870:00

email newsletter about that podcast, and

## 870:00 - 895:00

then clips from that show. They're a

## 895:00 - 920:00

full service agency that helps with

## 920:00 - 960:00

getting your target customer onto your

## 960:00 - 990:00

podcast, all of the post production, and

## 990:00 - 1020:00

they grow an email newsletter for you by

## 1020:00 - 1050:00

about 5,000 subs per month. And when you

## 1050:00 - 1075:00

combine all that together, it helps make

## 1075:00 - 1105:00

a founder famous in their niche

## 1105:00 - 1125:00

extremely quickly. Go to

## 1125:00 - 1150:00

acclaimodcasting.com

## 1150:00 - 1175:00

to learn more or click the link in the

## 1175:00 - 1195:00

description. Let's get started with

## 1195:00 - 1365:00

today's show.

## 1365:00 - 1410:00

Adam, what's good, dude? I'm so stoked

## 1410:00 - 1450:00

to have you here. It's gonna be a good

## 1450:00 - 1455:00

one.

## 1455:00 - 1510:00

You've been, man. Um, okay. So, how how

## 1510:00 - 1540:00

many agents are running right now in the

## 1540:00 - 1565:00

background for your clients? Like, while

## 1565:00 - 1590:00

we're having this conversation,

## 1590:00 - 1620:00

like tens of thousands definitely for

## 1620:00 - 1670:00

our clients. Um, us personally, like our

## 1670:00 - 1700:00

team has like 50 plus agents we're

## 1700:00 - 1725:00

running every day, which is crazy.

## 1725:00 - 1755:00

It's like we got we got more agent

## 1755:00 - 1780:00

headcount than human headcount. And I

## 1780:00 - 1810:00

think like we are kind of on the

## 1810:00 - 1835:00

bleeding edge of this but give us like

## 1835:00 - 1865:00

give other companies a few months maybe

## 1865:00 - 1890:00

a year and I think every company's going

## 1890:00 - 1915:00

to be the same way just because every

## 1915:00 - 1940:00

person should have assistance just

## 1940:00 - 1965:00

matter of like how do you get them set

## 1965:00 - 1980:00

up? How do you actually productionize

## 1980:00 - 2000:00

them? And that that's kind of the main

## 2000:00 - 2010:00

challenge.

## 2010:00 - 2040:00

Totally. I feel like in the last week or

## 2040:00 - 2070:00

like two weeks this idea of like vibe

## 2070:00 - 2105:00

marketing has like gone I I don't know.

## 2105:00 - 2150:00

I just see it ripping everywhere. And I

## 2150:00 - 2185:00

it's funny like when you break it down

## 2185:00 - 2220:00

like we were all doing versions of this

## 2220:00 - 2245:00

like for the last you know three years

## 2245:00 - 2275:00

it's been like okay how do I write

## 2275:00 - 2315:00

software that basically is doing keyword

## 2315:00 - 2340:00

research for me to then write articles

## 2340:00 - 2375:00

to then publish those to then like you

## 2375:00 - 2410:00

know re uh like refresh the articles

## 2410:00 - 2430:00

based off of the keyword data we're

## 2430:00 - 2470:00

getting and you take any marketing flow

## 2470:00 - 2505:00

and it's that same thing like here's a

## 2505:00 - 2530:00

human process and I'm trying to automate

## 2530:00 - 2565:00

as much as I can but I feel like right

## 2565:00 - 2590:00

now we're having this moment where you

## 2590:00 - 2630:00

can finally like put a you know a game

## 2630:00 - 2670:00

to that activity which is this like vibe

## 2670:00 - 2710:00

marketing kind of idea but the actual

## 2710:00 - 2730:00

application of this is I think what

## 2730:00 - 2750:00

people are trying to figure out like

## 2750:00 - 2775:00

everybody's like oh yeah an agent well

## 2775:00 - 2800:00

what the you know what the [ __ ] is an

## 2800:00 - 2835:00

agent is I think the biggest question

## 2835:00 - 2870:00

for me how I think about it is like

## 2870:00 - 2925:00

there's some type of AI reasoning that's

## 2925:00 - 2950:00

happening within the automation so like

## 2950:00 - 2980:00

a traditional automation is just like a

## 2980:00 - 3010:00

step by step there's like no decision-m

## 3010:00 - 3050:00

that's occurring and in contrast uh you

## 3050:00 - 3100:00

know the agentic version of this is

## 3100:00 - 3130:00

where it's making some type a decision

## 3130:00 - 3160:00

based off of the data it's finding or

## 3160:00 - 3195:00

the data that it's recording etc. But

## 3195:00 - 3220:00

I'd love to hear how you like think

## 3220:00 - 3250:00

about this in in the in a marketing

## 3250:00 - 3300:00

framework like how you guys use this uh

## 3300:00 - 3335:00

you know as like agents within the

## 3335:00 - 3355:00

marketing flow and then like what what

## 3355:00 - 3385:00

does that even look like like you know

## 3385:00 - 3410:00

where where is the boundary where is the

## 3410:00 - 3440:00

line in relationship to marketing.

## 3440:00 - 3470:00

Sweet. Yeah. Uh so to give like quick

## 3470:00 - 3495:00

run of what an agent is. I think my

## 3495:00 - 3525:00

co-founder Alex he like gave a TED AI

## 3525:00 - 3560:00

talk and he had like the best most

## 3560:00 - 3585:00

succinct version like I even used to

## 3585:00 - 3620:00

like explain agents to my mom. Uh, and

## 3620:00 - 3640:00

the way to think about these agents are

## 3640:00 - 3660:00

like Whimos. So, like in San Francisco,

## 3660:00 - 3685:00

we have these like Whimos that drive you

## 3685:00 - 3715:00

from point A to point B. Um, and

## 3715:00 - 3740:00

they're, you know, these are automated

## 3740:00 - 3770:00

hardware, you know, cars that drive you

## 3770:00 - 3800:00

from place to place. Uh, you got to

## 3800:00 - 3825:00

think of these agents as like automated

## 3825:00 - 3845:00

pieces of software that take you to from

## 3845:00 - 3880:00

point A to point B. So, uh, a good

## 3880:00 - 3915:00

example, like one I use every day is we

## 3915:00 - 3955:00

get like thousands of inbound um,

## 3955:00 - 3975:00

requests every week for people wanting

## 3975:00 - 3995:00

to book meetings with us, people who

## 3995:00 - 4025:00

want us to build agents for them. Uh,

## 4025:00 - 4060:00

and I used to manually go through and

## 4060:00 - 4090:00

like look at every person who's booking

## 4090:00 - 4120:00

a meeting with me and vet them and do

## 4120:00 - 4145:00

some like lead scoring. Uh, and then I

## 4145:00 - 4175:00

had like my VA doing it for a while and

## 4175:00 - 4190:00

then we're like, "Hey, we're gonna hire

## 4190:00 - 4215:00

somebody to do this." Um, and this was

## 4215:00 - 4240:00

like a function that we just built an

## 4240:00 - 4270:00

agent for and now like every time a

## 4270:00 - 4300:00

customer comes inbound, we're doing full

## 4300:00 - 4335:00

lead scoring on them. Um, so like any of

## 4335:00 - 4365:00

the big brands reaching out to us, uh,

## 4365:00 - 4380:00

you're definitely going to get on the

## 4380:00 - 4400:00

phone with me at some point because like

## 4400:00 - 4440:00

this agent is, you know, to a te knows

## 4440:00 - 4465:00

who our current users are, knows what we

## 4465:00 - 4495:00

should be looking for, looks to see like

## 4495:00 - 4515:00

is this even the right person at a

## 4515:00 - 4535:00

company to be speaking with. And if

## 4535:00 - 4555:00

that's the case, like we'll have an

## 4555:00 - 4575:00

intro with them, but we know like the

## 4575:00 - 4600:00

next step is, hey, we need to make sure

## 4600:00 - 4625:00

that like we're multi-threading this

## 4625:00 - 4640:00

conversation properly and actually

## 4640:00 - 4655:00

talking to the right folks at the

## 4655:00 - 4690:00

organization. Um, and these are things

## 4690:00 - 4720:00

like when you think about marketing and

## 4720:00 - 4760:00

these automations overall, think like

## 4760:00 - 4785:00

what did a human do? Like I just explain

## 4785:00 - 4815:00

a process like I used to manually do

## 4815:00 - 4845:00

every day. And that's a really really

## 4845:00 - 4890:00

good stepping stone into what agents

## 4890:00 - 4915:00

should be built. And I think a lot of

## 4915:00 - 4940:00

like companies come to us and they're

## 4940:00 - 4975:00

asking for AGI. Like half the consulting

## 4975:00 - 5000:00

work we do is companies coming to us

## 5000:00 - 5025:00

saying, "Hey, we need to automate this

## 5025:00 - 5055:00

entire workflow or this entire process

## 5055:00 - 5085:00

or this entire person's job." And I have

## 5085:00 - 5105:00

to spend a lot of time with telling them

## 5105:00 - 5130:00

like we don't have AGI yet. We don't

## 5130:00 - 5155:00

have this like all-encompassing agent

## 5155:00 - 5175:00

that can just do anything. Everything

## 5175:00 - 5205:00

right now is like really purpose-built.

## 5205:00 - 5230:00

Um, there is some stuff that's more

## 5230:00 - 5255:00

generalized, but I mean like the best

## 5255:00 - 5280:00

agents, the companies we're seeing that

## 5280:00 - 5310:00

actually make the most revenue, you

## 5310:00 - 5330:00

know, per agent, for lack of better

## 5330:00 - 5355:00

words, are these ones that are going and

## 5355:00 - 5375:00

building these custom solutions from the

## 5375:00 - 5390:00

ground up.

## 5390:00 - 5410:00

No, that makes total sense. What you

## 5410:00 - 5450:00

just said just like it was crazy for me

## 5450:00 - 5470:00

to think about. Like you used to look at

## 5470:00 - 5500:00

like a revenue per employee as like a

## 5500:00 - 5530:00

metric of success for a startup and now

## 5530:00 - 5580:00

it's like a revenue revenue per agent

## 5580:00 - 5615:00

that's being deployed or I mean

## 5615:00 - 5620:00

Yeah.

## 5620:00 - 5645:00

Yeah. I don't even know how to even

## 5645:00 - 5670:00

think about that honestly. But

## 5670:00 - 5700:00

we also like revenue per token. That's

## 5700:00 - 5720:00

an interesting one. Like I think a lot

## 5720:00 - 5740:00

more companies you guys start thinking

## 5740:00 - 5770:00

through now it's like everything has an

## 5770:00 - 5800:00

LM based baked into it. It's like okay

## 5800:00 - 5820:00

what's the revenue per token we're

## 5820:00 - 5850:00

generating? I think that's a metric like

## 5850:00 - 5865:00

you'll probably see investors start

## 5865:00 - 5885:00

caring more about in the coming months.

## 5885:00 - 5910:00

Totally. I mean I'm seeing this with

## 5910:00 - 5935:00

like vibe coding in particular where

## 5935:00 - 5965:00

people are like looking at okay well how

## 5965:00 - 6000:00

how can I you know do the work up front

## 6000:00 - 6035:00

whether it's using uh like a tool like

## 6035:00 - 6070:00

what is it called? Like codeguide.dev

## 6070:00 - 6100:00

dev I think is one of them where it

## 6100:00 - 6145:00

basically does like a um PRD and like

## 6145:00 - 6175:00

kind of the the whole structure of the

## 6175:00 - 6205:00

application like what the UI should look

## 6205:00 - 6230:00

like you know here's the database

## 6230:00 - 6250:00

structures and how they're interacting

## 6250:00 - 6295:00

with each other etc up front so that the

## 6295:00 - 6330:00

tokens that are necessary to like get

## 6330:00 - 6360:00

you to the final product are are are

## 6360:00 - 6390:00

basically less and I think you know it

## 6390:00 - 6410:00

makes total sense like why wouldn't we

## 6410:00 - 6440:00

apply that in the marketing like like

## 6440:00 - 6465:00

you know sphere as well or in the growth

## 6465:00 - 6510:00

sphere so um all right so I think that

## 6510:00 - 6535:00

gives context to like you know how

## 6535:00 - 6565:00

agents like fit into

## 6565:00 - 6595:00

Um, can you talk to me about how

## 6595:00 - 6625:00

companies are like thinking about how

## 6625:00 - 6660:00

they're like this is are they replacing

## 6660:00 - 6685:00

employees? Are they just like not even

## 6685:00 - 6715:00

hiring those employees? It's probably a

## 6715:00 - 6745:00

combination of things. I imagine

## 6745:00 - 6775:00

enterprise is like, yo, this job that

## 6775:00 - 6805:00

used to take a 100 people. We're now

## 6805:00 - 6840:00

doing it with one of these agents. And

## 6840:00 - 6865:00

startups are like, "Oh, we don't need to

## 6865:00 - 6880:00

hire people. We're just going to have

## 6880:00 - 6915:00

like a crack team of five to 10 and

## 6915:00 - 6945:00

we'll get to 100 million ARR with that

## 6945:00 - 6980:00

alone." What What are you guys seeing

## 6980:00 - 7000:00

from the front lines kind of from your

## 7000:00 - 7050:00

clients on the on the marketing side? So

## 7050:00 - 7080:00

I think there's a framework that anyone

## 7080:00 - 7100:00

who's listening to this, I might have,

## 7100:00 - 7120:00

you know, post about it publicly, but

## 7120:00 - 7150:00

it's important for people to understand.

## 7150:00 - 7180:00

There's kind of three criteria we're

## 7180:00 - 7200:00

looking for when you start thinking

## 7200:00 - 7225:00

about like is an agent a good fit for

## 7225:00 - 7260:00

this particular task. Uh so first we

## 7260:00 - 7280:00

want to look for like tasks that are

## 7280:00 - 7320:00

very expensive. Um don't try and replace

## 7320:00 - 7360:00

your you know uh your lowest like level

## 7360:00 - 7385:00

employees that you know are just like

## 7385:00 - 7405:00

think about the processes in your

## 7405:00 - 7435:00

company that are really expensive um

## 7435:00 - 7465:00

that are you know I think that's the

## 7465:00 - 7490:00

first criteria. Number two is are these

## 7490:00 - 7525:00

tasks repeatable? Um I think having you

## 7525:00 - 7545:00

know a lot of companies come to us ask

## 7545:00 - 7570:00

if there's like AGI type thing that can

## 7570:00 - 7605:00

handle any scenario. Uh we spend a lot

## 7605:00 - 7635:00

of time here building evals and we can

## 7635:00 - 7665:00

talk through that. U but the whole thing

## 7665:00 - 7695:00

is if it's repeatable it's very easy to

## 7695:00 - 7725:00

build an eval set to actually test what

## 7725:00 - 7760:00

success is. Uh and then something that's

## 7760:00 - 7800:00

like low risk. So for example like we'll

## 7800:00 - 7825:00

work with a hedge fund to build out

## 7825:00 - 7860:00

agents to do financial research but it's

## 7860:00 - 7895:00

not actually executing trades right yet

## 7895:00 - 7930:00

like so far. So you got to think through

## 7930:00 - 7955:00

like what are the things in my company

## 7955:00 - 7985:00

or my marketing process or sales process

## 7985:00 - 8015:00

that are low risk enough that it's not

## 8015:00 - 8045:00

going to like lose you multi-million

## 8045:00 - 8080:00

dollar Cisco contract for example if you

## 8080:00 - 8110:00

screw it up. So just kind of reiterate

## 8110:00 - 8130:00

it's like tasks that are very expensive

## 8130:00 - 8155:00

tests that are repeatable and tasks that

## 8155:00 - 8185:00

are low risk. And if you can hit off all

## 8185:00 - 8220:00

three of those criteria you're in such a

## 8220:00 - 8250:00

good place to start automating.

## 8250:00 - 8280:00

Totally. I think what you just said was

## 8280:00 - 8310:00

like specifically about this idea of

## 8310:00 - 8345:00

it's we're almost in this curation

## 8345:00 - 8385:00

economy moment where you're the the

## 8385:00 - 8415:00

expert is just like looking over the

## 8415:00 - 8445:00

work that one of these has done right

## 8445:00 - 8465:00

like that's you know whether it's a

## 8465:00 - 8495:00

trade that needs to be made but it's all

## 8495:00 - 8530:00

of that upfront uh kind of research and

## 8530:00 - 8570:00

process and and that's getting them you

## 8570:00 - 8605:00

know 90% of the way there the last 10 I

## 8605:00 - 8635:00

mean what's funny too is like we're

## 8635:00 - 8655:00

finding that people that's actually what

## 8655:00 - 8680:00

they want to pay for right like they

## 8680:00 - 8710:00

don't want to pay for the AI the

## 8710:00 - 8735:00

solution they want to pay for that last

## 8735:00 - 8775:00

10% %. They don't care how it, you know,

## 8775:00 - 8810:00

you basically get there. But I mean,

## 8810:00 - 8860:00

just to be like blunt, like it's like,

## 8860:00 - 8890:00

okay, cool. Like, I can charge $29 a

## 8890:00 - 8915:00

month for the software that gets 90% of

## 8915:00 - 8935:00

the way there or I can charge three

## 8935:00 - 8975:00

grand a month to layer a human on that

## 8975:00 - 9025:00

last 10%. That like gets it all the way

## 9025:00 - 9045:00

there for the client and they're willing

## 9045:00 - 9080:00

to pay that 3K versus that 29. Like,

## 9080:00 - 9100:00

what are you going to go do if you're

## 9100:00 - 9120:00

going to build a company, right? Like

## 9120:00 - 9140:00

you're going to focus on that higher

## 9140:00 - 9160:00

like payout. But, um,

## 9160:00 - 9180:00

it's interesting. I think a lot of

## 9180:00 - 9205:00

people who are like first prospecting

## 9205:00 - 9225:00

the space trying to figure out what to

## 9225:00 - 9255:00

build, we're building that 90% solution.

## 9255:00 - 9290:00

Um, and a lot of the large enterprises

## 9290:00 - 9325:00

that are coming us to us now, they're

## 9325:00 - 9350:00

like, we don't even really care as much

## 9350:00 - 9375:00

about the budget. It's just like what

## 9375:00 - 9400:00

will this actually like what is like the

## 9400:00 - 9435:00

tangible business benefit here? And I

## 9435:00 - 9470:00

think um as great as it is having these

## 9470:00 - 9500:00

like kind of proof of concepts that can,

## 9500:00 - 9515:00

you know, you can go up to management

## 9515:00 - 9530:00

and say, "Hey, we're investing in

## 9530:00 - 9555:00

agents." That's great. But it's like

## 9555:00 - 9595:00

what's that last 10%. And to take even a

## 9595:00 - 9610:00

little step back here, like my

## 9610:00 - 9630:00

co-founder, Alex, we started building

## 9630:00 - 9665:00

agents in March 2023 doing data entry

## 9665:00 - 9700:00

automation. And these agents were like

## 9700:00 - 9740:00

hitting 90% accuracy. So we went to go

## 9740:00 - 9760:00

like pitch it to these massive

## 9760:00 - 9785:00

companies. They were like, "This is

## 9785:00 - 9810:00

great, but if it doesn't have four lines

## 9810:00 - 9825:00

of accuracy, we're never going to be

## 9825:00 - 9850:00

able to trust this thing in production."

## 9850:00 - 9875:00

And that's how we started building like

## 9875:00 - 9905:00

observability for agents, debugging

## 9905:00 - 9925:00

agents, and all this type of stuff. But

## 9925:00 - 9950:00

it was that exact same problem was like

## 9950:00 - 9975:00

this is great 90% of the way there.

## 9975:00 - 10000:00

Maybe for some mom and pop shop will

## 10000:00 - 10020:00

work great or something like that. But

## 10020:00 - 10045:00

like the large enterprises, they need

## 10045:00 - 10080:00

that reliability. if they can't seek it,

## 10080:00 - 10100:00

they're going to go build some internal

## 10100:00 - 10125:00

solution to actually figure out how to

## 10125:00 - 10145:00

get as high as possible.

## 10145:00 - 10200:00

100% 100%. Uh something else that you

## 10200:00 - 10220:00

mentioned I just want to circle back on

## 10220:00 - 10255:00

is this idea of like documentation of

## 10255:00 - 10295:00

the processes like nothing can be uh

## 10295:00 - 10330:00

automated or replaced or you know given

## 10330:00 - 10360:00

to offshore talent without that. I see

## 10360:00 - 10405:00

this so often in marketing like I just

## 10405:00 - 10450:00

had a guy on as an example um he's like

## 10450:00 - 10485:00

email marketing is his like his whole

## 10485:00 - 10520:00

business right and he just go basically

## 10520:00 - 10540:00

the whole conversation was going deep on

## 10540:00 - 10560:00

email marketing and I was like what's

## 10560:00 - 10595:00

the biggest mistake that you see people

## 10595:00 - 10625:00

make his immediate response is they're

## 10625:00 - 10665:00

like they try to like from like zero to

## 10665:00 - 10690:00

one write an email newsletter on a

## 10690:00 - 10715:00

weekly basis he's like just don't do

## 10715:00 - 10750:00

that number one like have a simple

## 10750:00 - 10785:00

templated framework where it's like cool

## 10785:00 - 10825:00

section one is about X section two is

## 10825:00 - 10875:00

about Y section three is about Z, right?

## 10875:00 - 10900:00

And then all you have to do is basically

## 10900:00 - 10935:00

go find content to fit into that like

## 10935:00 - 10965:00

template that you've created. And

## 10965:00 - 10985:00

without that, like you're going to

## 10985:00 - 11025:00

spend, you know, 10 hours to do this

## 11025:00 - 11045:00

email every week because you have to

## 11045:00 - 11070:00

like think, you know, actually do the

## 11070:00 - 11100:00

ideation. But when you have that

## 11100:00 - 11125:00

constraint, it actually makes it easier.

## 11125:00 - 11165:00

And I think that that is like a very

## 11165:00 - 11200:00

simple way to kind of illustrate like

## 11200:00 - 11235:00

how these like to think about agents and

## 11235:00 - 11260:00

the processes side. Like if you if there

## 11260:00 - 11280:00

if you don't have a well- definfined

## 11280:00 - 11305:00

system that you can hand off to a team

## 11305:00 - 11340:00

member or like a junior employee, an

## 11340:00 - 11365:00

agent is probably not going to be the

## 11365:00 - 11400:00

solution for you whatsoever and like it

## 11400:00 - 11450:00

from an implementation standpoint. So um

## 11450:00 - 11490:00

with that said, tell talk to me about uh

## 11490:00 - 11515:00

how people are using marketing agents

## 11515:00 - 11550:00

like what like what's the first one that

## 11550:00 - 11570:00

you're seeing and you're seeing it make

## 11570:00 - 11605:00

a lot of impact for companies. So, one

## 11605:00 - 11635:00

that we run internally as like a social

## 11635:00 - 11670:00

listening agent. So, basically, uh you

## 11670:00 - 11685:00

guys I don't know there there's a bunch

## 11685:00 - 11715:00

of companies that like tried to do this.

## 11715:00 - 11745:00

I actually used to I'll say a little

## 11745:00 - 11775:00

growth one here. This is fun, but I used

## 11775:00 - 11800:00

to run like a thousand Reddit accounts

## 11800:00 - 11820:00

and like basically be able to like

## 11820:00 - 11850:00

curate and create trends using uh these

## 11850:00 - 11885:00

different Reddit accounts. And I still

## 11885:00 - 11910:00

see Reddit as this really incredible

## 11910:00 - 11945:00

like untapped marketing resource that so

## 11945:00 - 11970:00

many brands like want to figure out how

## 11970:00 - 11990:00

to navigate. So many brands want to like

## 11990:00 - 12010:00

know how to leverage it, but they're not

## 12010:00 - 12040:00

doing it well. Um, and there's a bunch

## 12040:00 - 12080:00

of social listening tools out there that

## 12080:00 - 12115:00

will basically, you know, for example,

## 12115:00 - 12155:00

we want to help uh Fortune 500 companies

## 12155:00 - 12175:00

build agents or we want to help with

## 12175:00 - 12205:00

agent observability. We're looking for

## 12205:00 - 12230:00

certain keywords and phrases that people

## 12230:00 - 12255:00

are looking for on the internet and

## 12255:00 - 12280:00

going and responding to that. So,

## 12280:00 - 12305:00

initially we had this as like a human

## 12305:00 - 12335:00

doing this 24/7. So, it's like, okay,

## 12335:00 - 12350:00

like here's your social listening

## 12350:00 - 12400:00

platform, you know, whatever keywords we

## 12400:00 - 12425:00

were looking for, they were populating

## 12425:00 - 12445:00

there. And we like like I'm kind of

## 12445:00 - 12465:00

going through this. You got to do this

## 12465:00 - 12485:00

process manually first before you figure

## 12485:00 - 12520:00

out automations. Uh but now what we have

## 12520:00 - 12560:00

is a way to basically look through

## 12560:00 - 12590:00

social list like take all the social

## 12590:00 - 12615:00

listing data in on one side and on the

## 12615:00 - 12645:00

other end have responses that are

## 12645:00 - 12680:00

autodrafted. Um the caveat is that we're

## 12680:00 - 12700:00

keeping a human in the loop. Like we're

## 12700:00 - 12735:00

not going in and saying hey like this

## 12735:00 - 12765:00

agent is going acting rogue and just

## 12765:00 - 12790:00

posting content left, right, and center.

## 12790:00 - 12825:00

That is it's my personal brand, it's my,

## 12825:00 - 12855:00

you know, our company's brand. It's all

## 12855:00 - 12875:00

these types of things like come into

## 12875:00 - 12895:00

play. And I think a lot of companies are

## 12895:00 - 12920:00

very like wary when it's like, hey,

## 12920:00 - 12935:00

we're just going to let this like agent

## 12935:00 - 12980:00

go run free and run wild. Um, but what

## 12980:00 - 13000:00

we've realized time and time again is

## 13000:00 - 13035:00

that like you can get 90% of the way

## 13035:00 - 13060:00

there in terms of getting a response out

## 13060:00 - 13090:00

there. And that now allows you a seat at

## 13090:00 - 13115:00

the table. Like now you're not having,

## 13115:00 - 13150:00

you know, an overseas team or or someone

## 13150:00 - 13180:00

on your team like manually writing out

## 13180:00 - 13200:00

all these requests. Like this is what I

## 13200:00 - 13220:00

used to do when I used to manage like a

## 13220:00 - 13245:00

thousand Reddit accounts. Like this was

## 13245:00 - 13280:00

pre AI, pre- agents, pre- everything.

## 13280:00 - 13305:00

Like we just had a team who was just

## 13305:00 - 13340:00

writing responses 24/7. And that was

## 13340:00 - 13360:00

great. But now it's like with these

## 13360:00 - 13380:00

agents like this is like a massive

## 13380:00 - 13405:00

massive unlock for businesses.

## 13405:00 - 13435:00

100%. Yeah. Yeah. And I mean that's a

## 13435:00 - 13465:00

perfect example of like okay cool. It

## 13465:00 - 13500:00

gets it to that last that final like you

## 13500:00 - 13530:00

know point right right before it gets

## 13530:00 - 13555:00

posted right before it goes live right

## 13555:00 - 13585:00

before it's public. And that's where the

## 13585:00 - 13610:00

humans coming in over the top and like

## 13610:00 - 13645:00

doing that last edit just really

## 13645:00 - 13680:00

gut-eing whatever the activity is that

## 13680:00 - 13715:00

it's doing. Um that that's one of them.

## 13715:00 - 13735:00

I feel like that like there's so many

## 13735:00 - 13765:00

that are in this space that are

## 13765:00 - 13770:00

Go ahead.

## 13770:00 - 13800:00

There's a company called Triple Whale. I

## 13800:00 - 13815:00

don't have you heard of them?

## 13815:00 - 13835:00

I know Triple Whale. Yeah.

## 13835:00 - 13850:00

They just launched something called

## 13850:00 - 13875:00

Orcabase. We're good friends with their

## 13875:00 - 13930:00

team there. Um we are using it now at a

## 13930:00 - 13950:00

bunch of our projects to do like

## 13950:00 - 14000:00

automatic basically uh rebalancing of ad

## 14000:00 - 14020:00

spend. So this is like something that

## 14020:00 - 14050:00

like I'm every company is going to be

## 14050:00 - 14070:00

doing and like anybody's interested in

## 14070:00 - 14085:00

trying more about this like I can

## 14085:00 - 14110:00

connect you directly with like the team

## 14110:00 - 14140:00

there. Uh, but this is such a massive

## 14140:00 - 14170:00

need. Like I used to work like in

## 14170:00 - 14205:00

marketing and you you'd have you know

## 14205:00 - 14225:00

either like an agency doing this

## 14225:00 - 14250:00

full-time or there'd be like some like

## 14250:00 - 14280:00

assassin on your team was full-time job

## 14280:00 - 14300:00

was just like managing like ad spend

## 14300:00 - 14325:00

across all these different verticals.

## 14325:00 - 14360:00

And this is like a role that like the

## 14360:00 - 14385:00

agents are actually better than humans.

## 14385:00 - 14415:00

Like often times like you know it's

## 14415:00 - 14445:00

you're crunching numbers 24/7 if you're

## 14445:00 - 14460:00

in one of these roles trying to figure

## 14460:00 - 14485:00

out where do we optimize spend. If the

## 14485:00 - 14515:00

agent can say hey you know your Bing ads

## 14515:00 - 14540:00

for whatever reason are outperforming

## 14540:00 - 14570:00

your Google ads here let's transfer

## 14570:00 - 14600:00

budget over to it. Like these are great

## 14600:00 - 14620:00

things you should be doing in real time.

## 14620:00 - 14640:00

And I think this is kind of the future

## 14640:00 - 14670:00

of basically everyone in ecom or

## 14670:00 - 14700:00

everyone in like that has SAS companies,

## 14700:00 - 14720:00

they're going to be using these agents

## 14720:00 - 14745:00

to do the rebalancing. It'll be

## 14745:00 - 14780:00

interesting to kind of see like on the

## 14780:00 - 14805:00

other end like once we kind of hit

## 14805:00 - 14825:00

critical mass of everybody using these

## 14825:00 - 14850:00

tools what actually happens, but right

## 14850:00 - 14870:00

now there's so much alpha if you just

## 14870:00 - 14900:00

like kind of lean in or build these kind

## 14900:00 - 14920:00

of systems yourself. And we've seen a

## 14920:00 - 14940:00

lot of companies also doing the same

## 14940:00 - 14950:00

thing.

## 14950:00 - 14980:00

Totally. And and it's not like anything

## 14980:00 - 15005:00

new. I think that's the thing like I I

## 15005:00 - 15035:00

just had a ads guy on recently and he's

## 15035:00 - 15090:00

like yeah it's you know nothing has

## 15090:00 - 15120:00

changed in the amount of like like the

## 15120:00 - 15145:00

process right like if you're looking at

## 15145:00 - 15165:00

a performance marketer they're

## 15165:00 - 15200:00

making$10,000 different ad variations

## 15200:00 - 15225:00

running them all against each other

## 15225:00 - 15250:00

whatever is the highest performer they

## 15250:00 - 15275:00

go and they dedicate a million dollars a

## 15275:00 - 15300:00

month in ad spend and that's how they're

## 15300:00 - 15325:00

like you know basically getting their

## 15325:00 - 15375:00

returns. Okay so that process that used

## 15375:00 - 15410:00

to be a human going or a team of people

## 15410:00 - 15435:00

going and creating all those ad

## 15435:00 - 15475:00

variations. Now this, you know, again,

## 15475:00 - 15495:00

like something that we're doing as an

## 15495:00 - 15540:00

example is you find pain points using

## 15540:00 - 15570:00

perplexity. You pull those out, turn

## 15570:00 - 15595:00

those into hooks, and I write a hundred

## 15595:00 - 15625:00

different uh script variations based off

## 15625:00 - 15660:00

of that, right? Based off of the ad

## 15660:00 - 15690:00

libraries of the competitors that we

## 15690:00 - 15715:00

scraped. And then you go, you test those

## 15715:00 - 15740:00

all against each other, and you find

## 15740:00 - 15770:00

you're just you're just doing a process

## 15770:00 - 15820:00

that has already been in uh you know,

## 15820:00 - 15855:00

used previously, but at a scale and out

## 15855:00 - 15880:00

of velocity that's so much higher. on

## 15880:00 - 15910:00

the triple whale thing just to give

## 15910:00 - 15935:00

context to what that is because I don't

## 15935:00 - 15960:00

like I I just want to go a little bit

## 15960:00 - 15980:00

deeper on it so the audience

## 15980:00 - 16005:00

understands. So triple whale is a data

## 16005:00 - 16040:00

warehousing company for ecom. It's

## 16040:00 - 16080:00

basically like uh you know it's a CDP

## 16080:00 - 16105:00

from my understanding right it's like a

## 16105:00 - 16160:00

a customer data uh uh like it basically

## 16160:00 - 16185:00

just stores it all you know every

## 16185:00 - 16215:00

everything related to your customer. So

## 16215:00 - 16245:00

they're sitting on this data lake or

## 16245:00 - 16270:00

this data warehouse of all this

## 16270:00 - 16300:00

information. They're now basically

## 16300:00 - 16330:00

allowing you to take all of that non

## 16330:00 - 16370:00

like that that insight and then go and

## 16370:00 - 16400:00

automatically run your Facebook ads,

## 16400:00 - 16440:00

your Google ads, etc. to whatever the

## 16440:00 - 16460:00

goals are that you're trying to

## 16460:00 - 16480:00

accomplish and then it's just

## 16480:00 - 16520:00

autooptimizing based off of the resource

## 16520:00 - 16550:00

constraints that you provide it and the

## 16550:00 - 16580:00

data that it has within its warehouse.

## 16580:00 - 16605:00

And when you think about like a

## 16605:00 - 16645:00

defensibility standpoint and also I know

## 16645:00 - 16675:00

um uh what's that storage company? It's

## 16675:00 - 16715:00

not uh is is it Box? I believe they're

## 16715:00 - 16735:00

doing this exact same thing where

## 16735:00 - 16760:00

they're basically like yeah we were a

## 16760:00 - 16790:00

data storage company and now like you

## 16790:00 - 16835:00

know AI comes now we're suddenly

## 16835:00 - 16865:00

basically an information like

## 16865:00 - 16915:00

decisionmaking like tool for hu you know

## 16915:00 - 16970:00

enterprise clients but um I you scale

## 16970:00 - 17000:00

this up and then you go down that chain

## 17000:00 - 17025:00

where it's like cool and maybe it just

## 17025:00 - 17060:00

starts out and it's only doing ad spend

## 17060:00 - 17095:00

right but then it gets into okay now it

## 17095:00 - 17145:00

can use icon me to make new creative now

## 17145:00 - 17190:00

it can use uh you know any of these AI

## 17190:00 - 17240:00

UGC uh like ad creators like arc ads as

## 17240:00 - 17275:00

an example to go and like have a human

## 17275:00 - 17310:00

actually say you know say the actual

## 17310:00 - 17345:00

edits or say you know do these script

## 17345:00 - 17380:00

variations and you're also scraping in

## 17380:00 - 17405:00

everything that's happening within the

## 17405:00 - 17430:00

market from the Facebook ads library

## 17430:00 - 17475:00

very API like as this scales up I think

## 17475:00 - 17520:00

it just turns into this like I I don't

## 17520:00 - 17555:00

even think I I'm over here like geeking

## 17555:00 - 17590:00

out on this and like freaking out

## 17590:00 - 17625:00

because I the the impact that this is

## 17625:00 - 17660:00

going to be able to make is like what a

## 17660:00 - 17695:00

team of 200 people that were all cracks

## 17695:00 - 17720:00

were doing previously. Now, a single

## 17720:00 - 17740:00

person's going to be able to. But

## 17740:00 - 17750:00

anyway,

## 17750:00 - 17785:00

another crazy one. So, I um I used to

## 17785:00 - 17825:00

spend like probably 30 hours a week in

## 17825:00 - 17850:00

sales calls like try to like basically

## 17850:00 - 17870:00

like meeting new prospects, doing all

## 17870:00 - 17900:00

this stuff. And my co-founder, and I

## 17900:00 - 17920:00

could probably I'll send you a link to

## 17920:00 - 17940:00

it, but he made a clone of me and like

## 17940:00 - 17960:00

it kind of went viral on like LinkedIn

## 17960:00 - 18000:00

and Twitter. Um and what I'm doing now

## 18000:00 - 18025:00

is I'm actually going into the studio

## 18025:00 - 18055:00

and I'm doing 12-hour recordings of

## 18055:00 - 18090:00

myself with perfect lighting, perfect

## 18090:00 - 18115:00

audio, and we're going to go like

## 18115:00 - 18145:00

actually make a proper clone of myself.

## 18145:00 - 18170:00

So, you know, we're an agent company.

## 18170:00 - 18190:00

The first interaction you're going to

## 18190:00 - 18215:00

have with us is talk to the agent first

## 18215:00 - 18240:00

and that's going to do like our lead

## 18240:00 - 18265:00

scoring. It's going to tell you like if

## 18265:00 - 18290:00

it's, you know, if this is a good lead

## 18290:00 - 18315:00

for us, otherwise it's going to send a

## 18315:00 - 18335:00

bunch of resources. And I'm pretty

## 18335:00 - 18350:00

transparent about it because I think

## 18350:00 - 18375:00

like people, you know, people have

## 18375:00 - 18400:00

different needs. Some people will come

## 18400:00 - 18425:00

to us like hair on fire. I need an agent

## 18425:00 - 18455:00

in the next like four weeks. Some like

## 18455:00 - 18470:00

we're like looking into the space and

## 18470:00 - 18490:00

like that's a great place for me to say,

## 18490:00 - 18510:00

hey, here are a bunch of resources to

## 18510:00 - 18530:00

get started with and when you get more

## 18530:00 - 18550:00

serious about it, you know, come our

## 18550:00 - 18585:00

way. Um, but this is like this is stuff

## 18585:00 - 18630:00

we think quite a bit about. Um, one

## 18630:00 - 18650:00

other thing, like not even agent

## 18650:00 - 18685:00

related, but like I highly recommend

## 18685:00 - 18710:00

everybody who's like listening to this

## 18710:00 - 18740:00

to go through the following exercise.

## 18740:00 - 18770:00

Um, download Whisper Flow. I don't do

## 18770:00 - 18790:00

you use Whisper Flow yet?

## 18790:00 - 18820:00

No, I haven't used it. I know I know

## 18820:00 - 18840:00

what it exists, but explain it to the

## 18840:00 - 18850:00

audience.

## 18850:00 - 18880:00

So, Whisper Flow is like this. Uh, you

## 18880:00 - 18900:00

basically just hold down like the

## 18900:00 - 18920:00

function key on your computer and you

## 18920:00 - 18955:00

can dictate incredibly quickly. So, I

## 18955:00 - 18975:00

could type like a 100 words a minute.

## 18975:00 - 19025:00

I'm uh using Whisper Flow like dictation

## 19025:00 - 19060:00

wise, I'm dictating over 200 words per

## 19060:00 - 19100:00

minute. And what I in like really

## 19100:00 - 19125:00

recommend everybody do is sit down with

## 19125:00 - 19160:00

like your team member, your co-founder,

## 19160:00 - 19195:00

your marketing lead, someone like that,

## 19195:00 - 19245:00

put Whisper Flow on, go to like a blank

## 19245:00 - 19275:00

Google doc, and just start talking about

## 19275:00 - 19305:00

problems that you're facing. Okay? Go

## 19305:00 - 19345:00

talk about my customers saying this, you

## 19345:00 - 19370:00

know, these are problems internally,

## 19370:00 - 19385:00

here's what we're seeing, you know,

## 19385:00 - 19415:00

issues people are having. Here's how I

## 19415:00 - 19435:00

think we should pitch this, you know,

## 19435:00 - 19455:00

company. And have just some

## 19455:00 - 19480:00

conversations back and forth. It's so

## 19480:00 - 19500:00

simple. You can even do a fake podcast

## 19500:00 - 19525:00

episode for for all that matters.

## 19525:00 - 19555:00

Basically, get all this text. And then

## 19555:00 - 19590:00

what you do is go to Claude or go to

## 19590:00 - 19625:00

Proplexity or whatever and say here are,

## 19625:00 - 19655:00

you know, here's this massive trove of

## 19655:00 - 19690:00

data. Go and create email sequences

## 19690:00 - 19715:00

based on it and come up with your

## 19715:00 - 19740:00

subject line, come up with the hook,

## 19740:00 - 19770:00

come up with the body text. And we did

## 19770:00 - 19805:00

this and it was game changer for us.

## 19805:00 - 19825:00

Like it's l it's like not rocket

## 19825:00 - 19855:00

science. Like you don't need to be a

## 19855:00 - 19875:00

developer at all. You could like have

## 19875:00 - 19895:00

never touched a line of code in your

## 19895:00 - 19920:00

entire life, but just learn how to

## 19920:00 - 19940:00

leverage these tools in the right way.

## 19940:00 - 19975:00

And it's an absolute gold mine. So this

## 19975:00 - 20000:00

is like someone that's so tangible like

## 20000:00 - 20020:00

after you're done this episode, you can

## 20020:00 - 20040:00

literally get going with it. It's

## 20040:00 - 20075:00

totally free basically and it's such

## 20075:00 - 20105:00

like a, you know, this is ways to

## 20105:00 - 20125:00

leverage in your marketing flow that you

## 20125:00 - 20145:00

don't need to be an expert. You don't

## 20145:00 - 20160:00

need to go spend like tens of thousands

## 20160:00 - 20175:00

of dollars building out something

## 20175:00 - 20205:00

custom. You can just do this today.

## 20205:00 - 20230:00

Totally. I mean, and that whole thing is

## 20230:00 - 20255:00

an automation, right? Like at its core,

## 20255:00 - 20285:00

like, okay, cool. You do a whisper flow

## 20285:00 - 20320:00

into a Google doc that then like I mean

## 20320:00 - 20350:00

it could just be a make.com automation

## 20350:00 - 20385:00

that goes pulls out the information from

## 20385:00 - 20405:00

using cloud, etc. And then

## 20405:00 - 20440:00

and then write into instantly and then

## 20440:00 - 20475:00

you're just setting those variations.

## 20475:00 - 20500:00

And I think that this is the actual

## 20500:00 - 20530:00

unlock for a lot of people is when they

## 20530:00 - 20560:00

realize like, oh, don't use the AI for

## 20560:00 - 20590:00

its general knowledge. Use the AI for

## 20590:00 - 20625:00

like the specialty knowledge that only

## 20625:00 - 20660:00

your company has that's related to the

## 20660:00 - 20690:00

product that you're trying to sell. When

## 20690:00 - 20720:00

you can figure out that like how do I

## 20720:00 - 20750:00

unlock the internal data that we have

## 20750:00 - 20785:00

that the insight that only we have,

## 20785:00 - 20810:00

that's where the real kind of like

## 20810:00 - 20845:00

arbitrage moment, the real alpha is

## 20845:00 - 20885:00

extracted. Because if you just ask an

## 20885:00 - 20920:00

AI, right, like you know, a simple way

## 20920:00 - 20955:00

to illustrate this is like, write me a

## 20955:00 - 21005:00

2,000word blog post about, you know, X

## 21005:00 - 21035:00

that then what it writes is going to be

## 21035:00 - 21080:00

like very average. But in contrast, if

## 21080:00 - 21110:00

you give it source material from five

## 21110:00 - 21145:00

experts that are experts in say for

## 21145:00 - 21175:00

example, hotel marketing and you're

## 21175:00 - 21200:00

like, write me a blog, you know,

## 21200:00 - 21230:00

20,000word blog post about hotel

## 21230:00 - 21265:00

marketing trends for 2025 based off of

## 21265:00 - 21300:00

the source text that I provided you. the

## 21300:00 - 21320:00

output that you're going to get from

## 21320:00 - 21355:00

that is going to be, you know, 100x than

## 21355:00 - 21370:00

what you're going to get from the

## 21370:00 - 21390:00

average from that from that general

## 21390:00 - 21420:00

knowledge of the LLM. So,

## 21420:00 - 21460:00

yeah, I think like I think a lot of

## 21460:00 - 21500:00

brands and founders we talk to, they're

## 21500:00 - 21520:00

always like in this like con they're

## 21520:00 - 21545:00

like it's so hard for me to create

## 21545:00 - 21580:00

content. Okay. And one of the barriers

## 21580:00 - 21615:00

people need to like break through is

## 21615:00 - 21655:00

kind of twofold is instead of creating,

## 21655:00 - 21705:00

go to copying and curating. So, if you

## 21705:00 - 21730:00

see something working well, like go and

## 21730:00 - 21760:00

train, you know, a GPT on it. go and

## 21760:00 - 21785:00

like leverage it so that this becomes

## 21785:00 - 21815:00

your like baseline. So it's like hey I

## 21815:00 - 21840:00

just did my whisper flow now I throw it

## 21840:00 - 21875:00

into this GPT now that understands full

## 21875:00 - 21900:00

context on all these other people and

## 21900:00 - 21930:00

rewrite it in their style and like it's

## 21930:00 - 21965:00

such a gold mine. It's a it does takes

## 21965:00 - 21995:00

no technical effort. Anybody can set

## 21995:00 - 22020:00

this up. Um and this is like a big one

## 22020:00 - 22050:00

for like that's on the copy side. The

## 22050:00 - 22070:00

other piece I always like to kind of

## 22070:00 - 22090:00

emphasize is like so many creators are

## 22090:00 - 22120:00

like oh how do I come with new ideas and

## 22120:00 - 22140:00

stuff like that. Like one thing that

## 22140:00 - 22160:00

I've been doing for a while now is

## 22160:00 - 22190:00

curation. So it's like I just see cool

## 22190:00 - 22210:00

stuff every week and I'm like here I'm

## 22210:00 - 22230:00

putting it in a list of here are all

## 22230:00 - 22245:00

like the you know things that happened

## 22245:00 - 22270:00

this week in AI agents or whatever it

## 22270:00 - 22295:00

might be. This is stuff that's just on

## 22295:00 - 22320:00

my feed. I'm literally just like looking

## 22320:00 - 22345:00

at it, bookmarking it. I literally have

## 22345:00 - 22370:00

an account where I just send it to. So I

## 22370:00 - 22400:00

just aggregate all the content. I try to

## 22400:00 - 22425:00

get an agent to like automate this whole

## 22425:00 - 22445:00

process. And at the end of the day like

## 22445:00 - 22470:00

it's my personal brand. I don't want to

## 22470:00 - 22500:00

have like an AI writing stuff for me. So

## 22500:00 - 22515:00

I'm still like we're still manually

## 22515:00 - 22545:00

doing this process. But it's one of

## 22545:00 - 22565:00

these things it's like leverage these

## 22565:00 - 22590:00

tools in the best way possible. Like you

## 22590:00 - 22620:00

leverage it to write hooks. If you see

## 22620:00 - 22650:00

someone's post does well, like just on

## 22650:00 - 22675:00

Twitter and like LinkedIn, just have

## 22675:00 - 22700:00

like a bookmark tab of like sick

## 22700:00 - 22720:00

content. Like that's what I have. It's

## 22720:00 - 22745:00

like, hey, this is really cool. I like

## 22745:00 - 22770:00

this hook. I like the imaging that he

## 22770:00 - 22800:00

used. I like how, you know, maybe had a

## 22800:00 - 22825:00

great call to action. And like leverage

## 22825:00 - 22850:00

it and then just keep this as a data

## 22850:00 - 22880:00

source. You just keep on referencing and

## 22880:00 - 22910:00

you will see a tangible impact on your

## 22910:00 - 22935:00

content. There's no question in my mind.

## 22935:00 - 22965:00

100%. And I think that like again this

## 22965:00 - 22995:00

we're not this isn't anything new. This

## 22995:00 - 23025:00

is just at a volume and a scale that's

## 23025:00 - 23070:00

like superhuman, right? Like if you're

## 23070:00 - 23100:00

good at social as an example, like what

## 23100:00 - 23120:00

are you doing? You're posting

## 23120:00 - 23145:00

consistently. You're looking at what's

## 23145:00 - 23175:00

performing best and then you go and you

## 23175:00 - 23200:00

have that influence the future content

## 23200:00 - 23225:00

that you're making. Like that is just a

## 23225:00 - 23260:00

system. That's a very basic process. And

## 23260:00 - 23285:00

you probably automate that whole thing,

## 23285:00 - 23310:00

right? It's like cool. Here's our corpus

## 23310:00 - 23335:00

of information that you can work from

## 23335:00 - 23365:00

AI. I want you to go and write, you

## 23365:00 - 23420:00

know, zits, post them to Twitter, see

## 23420:00 - 23440:00

what the data looks like from an

## 23440:00 - 23460:00

impression standpoint, and then your

## 23460:00 - 23485:00

measurement of success is how many

## 23485:00 - 23510:00

impressions you can get based off of

## 23510:00 - 23535:00

this walled garden of information that

## 23535:00 - 23560:00

we provide you. Like that right there is

## 23560:00 - 23600:00

an automation that I know tomorrow like

## 23600:00 - 23635:00

somebody would easily go pay like at

## 23635:00 - 23690:00

least 99 to 199 a month for, right? Like

## 23690:00 - 23735:00

go build that literally right now. So my

## 23735:00 - 23765:00

my two sense is like so many people are

## 23765:00 - 23785:00

so scared just taking the first step. We

## 23785:00 - 23815:00

have this like ethos at the company.

## 23815:00 - 23835:00

It's actually my co-founder who came up

## 23835:00 - 23860:00

with it, but it's like it's called MVP,

## 23860:00 - 23900:00

minimum viable post, and it's every day

## 23900:00 - 23925:00

get one post out. Okay? It doesn't

## 23925:00 - 23955:00

matter how high quality it is. I

## 23955:00 - 23980:00

sometimes spend time just drafting a

## 23980:00 - 24005:00

bunch. So, I have batch posts that are

## 24005:00 - 24030:00

like any day I can guarantee if

## 24030:00 - 24065:00

something go out, but it's such a game

## 24065:00 - 24095:00

changer when like, and I think Dave

## 24095:00 - 24120:00

Poral about this, he's like, if you're

## 24120:00 - 24150:00

the guy who like covers Tuesday night

## 24150:00 - 24175:00

football at 700 p.m. or whatever it

## 24175:00 - 24210:00

might be, you better show up for that

## 24210:00 - 24230:00

like football or baseball game and

## 24230:00 - 24260:00

record it and make your content on it.

## 24260:00 - 24285:00

And I think once people like you figure

## 24285:00 - 24305:00

out your niche and you figure out how to

## 24305:00 - 24330:00

actually scale this stuff up, it's

## 24330:00 - 24350:00

actually very rewarding and you actually

## 24350:00 - 24380:00

get a lot of cool stuff out of it. Um,

## 24380:00 - 24410:00

but I recommend so many people like

## 24410:00 - 24435:00

figure out your process. Figure out like

## 24435:00 - 24465:00

what your MVP is going to be every day.

## 24465:00 - 24490:00

Whether it's content schedule or maybe

## 24490:00 - 24510:00

it's Sunday, you just, you know, start

## 24510:00 - 24540:00

your morning off with a copy, a cup of

## 24540:00 - 24560:00

coffee, and you literally just start

## 24560:00 - 24585:00

like writing a bunch of ideas that you

## 24585:00 - 24615:00

have for the week. But like really just

## 24615:00 - 24650:00

like start posting is such an incredible

## 24650:00 - 24680:00

thing. Like our team's doing like 2 to

## 24680:00 - 24700:00

six million impressions a week

## 24700:00 - 24740:00

organically now with like not $1 paid

## 24740:00 - 24765:00

behind it. and we're getting like some

## 24765:00 - 24785:00

inbound from some of the biggest brands

## 24785:00 - 24810:00

in the world and it's just because we're

## 24810:00 - 24845:00

out there and like it's not just the the

## 24845:00 - 24870:00

one thing that's interesting and I I

## 24870:00 - 24890:00

think we're gonna do a whole episode on

## 24890:00 - 24925:00

this soon but we can chat through it but

## 24925:00 - 24950:00

it's basically we have like engineers at

## 24950:00 - 24970:00

our company but we're creating this idea

## 24970:00 - 25000:00

of influence engineers. So we're

## 25000:00 - 25035:00

basically encouraging all of our

## 25035:00 - 25065:00

engineers to post every day as well. So

## 25065:00 - 25080:00

it's like hey I just shipped this

## 25080:00 - 25110:00

feature. Hey, I just like is it the

## 25110:00 - 25150:00

building in public now like like you

## 25150:00 - 25170:00

know at a different level like I think

## 25170:00 - 25185:00

like a lot of people are building in

## 25185:00 - 25210:00

public and there's just indie depths but

## 25210:00 - 25240:00

now you see like 10 people on a single

## 25240:00 - 25270:00

team all posting every day like wow the

## 25270:00 - 25290:00

product's getting amazing. Hey, here are

## 25290:00 - 25315:00

like these little nitty-gritty things

## 25315:00 - 25350:00

and we're getting feedback like we'll

## 25350:00 - 25375:00

post a tweet and then people are like

## 25375:00 - 25400:00

either this is great or this is like

## 25400:00 - 25430:00

horrible like immediately and like how

## 25430:00 - 25450:00

else are you going to get that feedback

## 25450:00 - 25475:00

instead of you know I think the old days

## 25475:00 - 25505:00

of sending out like a hey here's a $50

## 25505:00 - 25530:00

gift card let me know what's going on

## 25530:00 - 25555:00

like just do that in public now and like

## 25555:00 - 25580:00

yeah you get roasted a bit but like it's

## 25580:00 - 25625:00

part of the game but that roasted like

## 25625:00 - 25655:00

it creates this engagement flywheel

## 25655:00 - 25675:00

right so it's like okay now we get more

## 25675:00 - 25700:00

reach now we get more top of funnel and

## 25700:00 - 25740:00

then it turns so I I think it serves the

## 25740:00 - 25770:00

business I it's all just dependent on

## 25770:00 - 25795:00

where you're target customer is too.

## 25795:00 - 25815:00

Like I think that's the one thing to

## 25815:00 - 25845:00

remember is like go to where your

## 25845:00 - 25875:00

audience is. Like I get asked this more

## 25875:00 - 25905:00

than any other question is like where

## 25905:00 - 25930:00

should I be marketing and I'm like where

## 25930:00 - 25965:00

are your where is your audience? And

## 25965:00 - 26015:00

like most founders have no idea like

## 26015:00 - 26050:00

especially when they're like seed series

## 26050:00 - 26070:00

A they're like we don't know. We're not

## 26070:00 - 26095:00

sure where they are. Right? It's like

## 26095:00 - 26125:00

figure that out first. Then you go and

## 26125:00 - 26145:00

you figure out what's the content that's

## 26145:00 - 26180:00

most likely to get consumed on that

## 26180:00 - 26200:00

platform by the people that I'm trying

## 26200:00 - 26225:00

to be in front of. That's what the

## 26225:00 - 26255:00

process turns into. But

## 26255:00 - 26290:00

we've totally digressed. Let's bring it

## 26290:00 - 26330:00

back to use cases. Talk to me about

## 26330:00 - 26355:00

number two. What's the other what's

## 26355:00 - 26390:00

another uh like marketing like agent

## 26390:00 - 26415:00

that you're seeing people implement um

## 26415:00 - 26445:00

that's being effective for companies or

## 26445:00 - 26460:00

you know something that you guys are

## 26460:00 - 26480:00

doing internally.

## 26480:00 - 26510:00

So I think like there's some basic like

## 26510:00 - 26525:00

they're not I wouldn't even call them

## 26525:00 - 26545:00

automations but like if you're not using

## 26545:00 - 26575:00

superhuman now as part of your sales

## 26575:00 - 26595:00

process I don't know what you're doing.

## 26595:00 - 26625:00

So like biggest advocate of superhuman.

## 26625:00 - 26650:00

I now have this like autodraft like

## 26650:00 - 26690:00

response thing in my superhuman and it's

## 26690:00 - 26735:00

like literally drafting 90% good enough

## 26735:00 - 26760:00

emails that now I just have to kind of

## 26760:00 - 26785:00

review. So like everybody's listening

## 26785:00 - 26805:00

like if you want to build a real company

## 26805:00 - 26830:00

I think you have to I I'm trying to

## 26830:00 - 26855:00

convert my whole team and everyone onto

## 26855:00 - 26870:00

it. But I think it's the biggest game

## 26870:00 - 26910:00

changer right now. Um so I use like I

## 26910:00 - 26935:00

don't write emails anymore. That's one

## 26935:00 - 26950:00

thing I think like people need to

## 26950:00 - 26980:00

understand. So I do like whisper flow

## 26980:00 - 27005:00

just directly into superhuman. Then I

## 27005:00 - 27040:00

use the ask AI feature to you know rejig

## 27040:00 - 27065:00

it just in case there's anything it

## 27065:00 - 27085:00

wants. and then I'm sending out these

## 27085:00 - 27130:00

emails and it's like it's it's it's like

## 27130:00 - 27175:00

having like a VA 247 within your email.

## 27175:00 - 27205:00

Um, couple other things I'll throw out

## 27205:00 - 27245:00

there. If you are not using Fathom like

## 27245:00 - 27265:00

as part of your workflow, like every

## 27265:00 - 27290:00

call you're on, like if you're in sales

## 27290:00 - 27330:00

or making sales, like as great as Gong

## 27330:00 - 27365:00

is like Fathom like $19 a month or

## 27365:00 - 27390:00

something like that, like use it. And

## 27390:00 - 27420:00

once it's embedded in your superhuman,

## 27420:00 - 27445:00

the cool thing is you can ask any

## 27445:00 - 27470:00

questions like you would to a virtual

## 27470:00 - 27510:00

assistant. So I have like all my call

## 27510:00 - 27545:00

history and all my email history like

## 27545:00 - 27585:00

the full ontology now in my superhuman

## 27585:00 - 27605:00

and like so now I can just ask any

## 27605:00 - 27625:00

question say what's the latest with

## 27625:00 - 27660:00

exclient like do is there any action

## 27660:00 - 27680:00

items and it literally just pulls

## 27680:00 - 27710:00

everything from fathom pulls like all

## 27710:00 - 27735:00

the you know next steps for my call

## 27735:00 - 27770:00

recording drafts an email automatically

## 27770:00 - 27810:00

and it's like I I think most com most

## 27810:00 - 27840:00

founders probably spend 10 to 20 hours a

## 27840:00 - 27870:00

week in email like if you can cut down

## 27870:00 - 27895:00

three four hours of that by just using

## 27895:00 - 27925:00

these like using a combination of these

## 27925:00 - 27950:00

softwares in the best way possible it's

## 27950:00 - 27975:00

it's an absolute gold mine so it's not

## 27975:00 - 27995:00

like as tangible in the marketing side.

## 27995:00 - 28030:00

It's like you're still doing this 24/7.

## 28030:00 - 28055:00

Totally. Yeah. I feel like a lot of the

## 28055:00 - 28085:00

use cases so far have been all of these.

## 28085:00 - 28105:00

I mean, just the first ones that feel

## 28105:00 - 28135:00

like that came to market were ton of the

## 28135:00 - 28165:00

ton of different like sales activities

## 28165:00 - 28195:00

like even, okay, I'm doing call

## 28195:00 - 28230:00

recording. Here's a templated format for

## 28230:00 - 28265:00

what that follow-up uh like needs to

## 28265:00 - 28290:00

look like so that I can, you know,

## 28290:00 - 28325:00

basically circle around with the the

## 28325:00 - 28360:00

lead that I just talked to. But I think

## 28360:00 - 28395:00

we're now just on this precipice of of

## 28395:00 - 28425:00

okay here's these like marketing

## 28425:00 - 28460:00

automations that you can implement that

## 28460:00 - 28505:00

are going to create like again a lot of

## 28505:00 - 28550:00

impacts for for the brand like to your

## 28550:00 - 28590:00

point of okay

## 28590:00 - 28620:00

we're talking about the ads creation

## 28620:00 - 28635:00

like that was happening with like a

## 28635:00 - 28660:00

triple whale or something like that

## 28660:00 - 28700:00

right like again if I wanted to go and

## 28700:00 - 28740:00

make I I say that you know I use this

## 28740:00 - 28780:00

all the time but like if UGC ads is the

## 28780:00 - 28805:00

easiest one because the dollar amount is

## 28805:00 - 28835:00

very finite like if I wanted to go make

## 28835:00 - 28875:00

aund different ads with different UGC

## 28875:00 - 28915:00

creators. Like that would cost me about

## 28915:00 - 28945:00

10 grand in, you know, the traditional

## 28945:00 - 28980:00

world using something like a billow.app

## 28980:00 - 29000:00

or any of these kind of like, you know,

## 29000:00 - 29030:00

thirdparty resellers or even if you went

## 29030:00 - 29065:00

and did the DMs yourself to actually get

## 29065:00 - 29095:00

those influencers. In contrast, you can

## 29095:00 - 29145:00

go make that with the Hey Gen API for

## 29145:00 - 29180:00

like I mean six cents I think is what we

## 29180:00 - 29215:00

did, you know, on our recent and and

## 29215:00 - 29240:00

when you think about that just from like

## 29240:00 - 29270:00

the ability to like scale up that

## 29270:00 - 29310:00

creation, that's like where all like the

## 29310:00 - 29350:00

speed is the is the is the arbitrage

## 29350:00 - 29370:00

right now. And I feel like that is what

## 29370:00 - 29410:00

all of this tooling is doing. So um you

## 29410:00 - 29430:00

got to make sure your team is open to

## 29430:00 - 29465:00

it. That's a big factor. I think so many

## 29465:00 - 29490:00

like like I have a video editor now like

## 29490:00 - 29510:00

he knows how to use a he knows how to

## 29510:00 - 29530:00

use all these tools. he didn't know how

## 29530:00 - 29550:00

to use this stuff a couple months ago,

## 29550:00 - 29575:00

but like this becomes like a game

## 29575:00 - 29600:00

changer. And I think you got to make

## 29600:00 - 29625:00

sure your team is very open to testing

## 29625:00 - 29665:00

these things. Um, and honestly, usually

## 29665:00 - 29685:00

proof is in the pudding. Like once they

## 29685:00 - 29705:00

see a tangible benefit, it's very easy

## 29705:00 - 29725:00

to get everyone across the finishing

## 29725:00 - 29760:00

line. But we see these like lite teams

## 29760:00 - 29790:00

who are just like scared to use this

## 29790:00 - 29810:00

technology, they're like, "Oh no, this

## 29810:00 - 29830:00

going to it's like, you know, there

## 29830:00 - 29860:00

literally could be 10x productivity

## 29860:00 - 29890:00

boost." And the rule is like, if you're

## 29890:00 - 29900:00

listening to this, you're already

## 29900:00 - 29925:00

probably ahead of the game, but like

## 29925:00 - 29945:00

make sure you're the one at your company

## 29945:00 - 29965:00

or if you're starting, like you're the

## 29965:00 - 29985:00

one who has a seat at the table who's

## 29985:00 - 30025:00

like the leading expert on this. And 99%

## 30025:00 - 30045:00

of it could just come from watching

## 30045:00 - 30065:00

YouTube. And like people don't realize

## 30065:00 - 30100:00

that. 100%. Yeah. So my brother owns

## 30100:00 - 30115:00

this company. It's like a talent

## 30115:00 - 30145:00

sourcing a agency, like one of those

## 30145:00 - 30185:00

offshore ones. Um it's like a BO. But I

## 30185:00 - 30210:00

mean he he told me in the last like

## 30210:00 - 30230:00

three months in particular like

## 30230:00 - 30255:00

everybody that's coming through pipeline

## 30255:00 - 30300:00

for them is basically just been entirely

## 30300:00 - 30330:00

focused on hey like I want people that

## 30330:00 - 30365:00

are like AI native with this. Like I

## 30365:00 - 30395:00

don't I don't I'm not looking for you

## 30395:00 - 30415:00

know full stack engineer. I'm looking

## 30415:00 - 30465:00

for like somebody that is has been like

## 30465:00 - 30505:00

diligently using cursor for the last

## 30505:00 - 30530:00

three years. I don't even care if they

## 30530:00 - 30580:00

know how to like do deep like basically

## 30580:00 - 30610:00

just like leaning on all of these these

## 30610:00 - 30645:00

these these tools that are out there.

## 30645:00 - 30675:00

And that's the hiring focus. That's the

## 30675:00 - 30705:00

hiring premise of any of these companies

## 30705:00 - 30740:00

because again if you have those people

## 30740:00 - 30790:00

suddenly it takes a you know it turns an

## 30790:00 - 30820:00

average person into a 10x person when

## 30820:00 - 30855:00

they have that that ability to implement

## 30855:00 - 30880:00

this tool stack you know within their

## 30880:00 - 30915:00

their whole workflow. though. Um,

## 30915:00 - 30935:00

for sure. I'm trying to think some other

## 30935:00 - 30960:00

cool stuff that like we're seeing. I

## 30960:00 - 30985:00

think a lot of companies are very much

## 30985:00 - 31020:00

on like the experiment experimentation

## 31020:00 - 31045:00

phase right now. And like that's totally

## 31045:00 - 31075:00

fine. Like I think like we do tests like

## 31075:00 - 31100:00

almost every day and like we see kind of

## 31100:00 - 31130:00

how it works. Um, this could be as

## 31130:00 - 31170:00

simple as like mass sending DMs that are

## 31170:00 - 31220:00

like very like focused on certain um

## 31220:00 - 31255:00

subjects. One interesting one that I

## 31255:00 - 31280:00

literally just started testing last week

## 31280:00 - 31310:00

and I can we on the next episode we can

## 31310:00 - 31360:00

talk about um you.com uh has this agent

## 31360:00 - 31405:00

called ARI and they gave me early access

## 31405:00 - 31425:00

to so I've been testing it for a while

## 31425:00 - 31440:00

and I was trying to figure out like

## 31440:00 - 31465:00

basically it's like deep research but

## 31465:00 - 31490:00

creates these like really in-depth

## 31490:00 - 31520:00

marketing reports or like very in-depth

## 31520:00 - 31545:00

like industry reports like similar like

## 31545:00 - 31575:00

when McKenzie like Mackenzie comes out

## 31575:00 - 31615:00

with hey industry tends on AI agents and

## 31615:00 - 31635:00

they you know go blast this out to

## 31635:00 - 31670:00

everybody. You can get Ari to do one of

## 31670:00 - 31700:00

these very in-depth reports. It'll go

## 31700:00 - 31745:00

seek like 400 different like sources. It

## 31745:00 - 31770:00

like cites everything. Makes it really

## 31770:00 - 31800:00

awesome. But this is like an amazing

## 31800:00 - 31820:00

like lead genen tool. I don't think

## 31820:00 - 31845:00

people realize it. So like I literally

## 31845:00 - 31870:00

just went on it and like a couple

## 31870:00 - 31885:00

companies reached out to us and I'm

## 31885:00 - 31910:00

like, "Hey, you're in pharmaceuticals.

## 31910:00 - 31930:00

Here are like the top ways that

## 31930:00 - 31950:00

pharmaceutical companies are using AI

## 31950:00 - 31985:00

agents today." That was basically the

## 31985:00 - 32015:00

query that I gave it to this like

## 32015:00 - 32050:00

this.com agent called Ari. And it went

## 32050:00 - 32075:00

and made a full report and it literally

## 32075:00 - 32105:00

comes out with like a PDF that you can

## 32105:00 - 32145:00

just go attach to your email. And this

## 32145:00 - 32175:00

is like like typically like I don't even

## 32175:00 - 32190:00

know how you would have done this

## 32190:00 - 32210:00

previously. Like you would have had like

## 32210:00 - 32230:00

a team of analysts go and write these

## 32230:00 - 32255:00

reports. But now it's like you're coming

## 32255:00 - 32280:00

to the table with something very

## 32280:00 - 32315:00

tangible being like hey I did my work

## 32315:00 - 32345:00

like they don't know that it maybe one

## 32345:00 - 32365:00

day like after listening to this they're

## 32365:00 - 32380:00

going to know that it takes you know

## 32380:00 - 32410:00

like a sub a minute to make one of these

## 32410:00 - 32430:00

you know fully in-depth reports and

## 32430:00 - 32445:00

obviously you want to read it and make

## 32445:00 - 32475:00

sure like it's not uh you talking about

## 32475:00 - 32495:00

your biggest competitor or anything like

## 32495:00 - 32525:00

that but this is the type of stuff

## 32525:00 - 32555:00

that's so tangible. It's like once you

## 32555:00 - 32575:00

include it as part of your workflow like

## 32575:00 - 32600:00

there's gonna be an API available for it

## 32600:00 - 32630:00

soon. So I could see like a full like

## 32630:00 - 32660:00

clay funnel like clay pipeline going

## 32660:00 - 32690:00

from hey here's a person that I want to

## 32690:00 - 32720:00

reach out to here's now a case study

## 32720:00 - 32745:00

that we saw they mentioned in now here's

## 32745:00 - 32785:00

like a full-on like you know couple page

## 32785:00 - 32810:00

document with like full citations and

## 32810:00 - 32835:00

everything about like how we see their

## 32835:00 - 32860:00

industry going and then now you're

## 32860:00 - 32885:00

coming in as an industry expert and you

## 32885:00 - 32910:00

did no work like you didn't like you

## 32910:00 - 32935:00

didn't have like your you know BDR

## 32935:00 - 32960:00

someone go research the industry or

## 32960:00 - 32970:00

anything like that you're just

## 32970:00 - 32985:00

leveraging the tools in the best way

## 32985:00 - 33000:00

possible

## 33000:00 - 33050:00

totally I mean totally separate but

## 33050:00 - 33070:00

related to this is we've been

## 33070:00 - 33105:00

experimenting with having uh Google deep

## 33105:00 - 33150:00

research like do case study research on

## 33150:00 - 33175:00

specific companies like marketing

## 33175:00 - 33220:00

strategy. So for example like uh what

## 33220:00 - 33265:00

was uh mix panel's uh like social media

## 33265:00 - 33305:00

strategy um like what was Canvas's uh

## 33305:00 - 33350:00

you know SEO strategy and then we take

## 33350:00 - 33375:00

that source file and we go and we turn

## 33375:00 - 33420:00

it into a podcast. I did it for myself

## 33420:00 - 33450:00

just as like a way to like okay how do I

## 33450:00 - 33480:00

consume you know every case study that I

## 33480:00 - 33510:00

can find and and just try to download

## 33510:00 - 33545:00

all of it. But the quality, I mean, it's

## 33545:00 - 33575:00

not perfect, right? But like it's 80% of

## 33575:00 - 33605:00

the way there where I'm like, damn, I

## 33605:00 - 33630:00

actually like learned something. It took

## 33630:00 - 33665:00

something away from this that previously

## 33665:00 - 33685:00

that would have taken, you know, a team

## 33685:00 - 33720:00

of five researchers like a month to go

## 33720:00 - 33750:00

find and then basically to write a

## 33750:00 - 33770:00

script out. I mean, it would just be

## 33770:00 - 33795:00

impossible just like full, you know,

## 33795:00 - 33855:00

full stop. But, um, other marketing use

## 33855:00 - 33885:00

cases like what are these tactical

## 33885:00 - 33920:00

things that you're seeing companies do?

## 33920:00 - 33950:00

um and and not even marketing too, maybe

## 33950:00 - 33975:00

it's just like business operations. Like

## 33975:00 - 34005:00

what are the what are the bit like best

## 34005:00 - 34035:00

use cases right now for the agents

## 34035:00 - 34065:00

outside of the sales space um that

## 34065:00 - 34095:00

you're seeing kind of being uh being

## 34095:00 - 34120:00

implemented.

## 34120:00 - 34140:00

Cool. So you mentioned like social

## 34140:00 - 34160:00

listening, you mentioned some research

## 34160:00 - 34200:00

stuff. Uh there's this like one really

## 34200:00 - 34230:00

underutilized tool that like no one

## 34230:00 - 34270:00

realizes well some people do but within

## 34270:00 - 34285:00

Twitter they have something called

## 34285:00 - 34315:00

Radar. Have you tested it yet?

## 34315:00 - 34330:00

No, I haven't.

## 34330:00 - 34360:00

Okay. So, Radar is this like social

## 34360:00 - 34395:00

listening tool just for Twitter and it

## 34395:00 - 34425:00

is the absolute gold mine for any

## 34425:00 - 34465:00

marketer right now. So, I built we built

## 34465:00 - 34490:00

an agent that basically navigates the

## 34490:00 - 34515:00

browser and goes through it and then

## 34515:00 - 34535:00

basically comes up with a list of things

## 34535:00 - 34565:00

we should respond to. Kind of like what

## 34565:00 - 34590:00

I was talking about before. But if

## 34590:00 - 34610:00

you're paying for Twitter premium, you

## 34610:00 - 34630:00

get like a certain amount of queries.

## 34630:00 - 34645:00

They're like boolean queries. You can

## 34645:00 - 34670:00

add a bunch of different terms into it.

## 34670:00 - 34695:00

But you can just basically make like a

## 34695:00 - 34725:00

whole like for example I just want to

## 34725:00 - 34750:00

find agent developers who are building

## 34750:00 - 34785:00

with certain frameworks. like agents SDK

## 34785:00 - 34830:00

from open AI, crew AI, lane chain,

## 34830:00 - 34850:00

lawman index, like basically all the

## 34850:00 - 34870:00

companies that we're integrated with and

## 34870:00 - 34890:00

I could just have this agent that just

## 34890:00 - 34920:00

goes on the like goes and looks through

## 34920:00 - 34945:00

radar for these different keywords then

## 34945:00 - 34970:00

finds conversations that are relevant

## 34970:00 - 35005:00

and then if I want using like browser

## 35005:00 - 35025:00

use or browser base for one of these

## 35025:00 - 35045:00

tools I can actually go and have it

## 35045:00 - 35075:00

automatically do the response. So I can

## 35075:00 - 35100:00

have it like cue everything happen in

## 35100:00 - 35125:00

Google sheet. I can go edit the

## 35125:00 - 35150:00

responses. Then I can basically like

## 35150:00 - 35185:00

give it the the commands and go for it

## 35185:00 - 35210:00

and then it's going and automatically

## 35210:00 - 35245:00

responding and it's just so you know

## 35245:00 - 35275:00

like it's at our fingertips like you got

## 35275:00 - 35290:00

to just test these things and see what

## 35290:00 - 35320:00

works and what doesn't. Um that stuff's

## 35320:00 - 35375:00

super super interesting. Um one a cool

## 35375:00 - 35415:00

one that I recommend people try out and

## 35415:00 - 35440:00

like you know I'm giving all the secrets

## 35440:00 - 35460:00

here but that's I think the the fun

## 35460:00 - 35495:00

thing in life is that um course creation

## 35495:00 - 35525:00

is going crazy right now. Everybody like

## 35525:00 - 35550:00

wants to figure out okay how do I learn

## 35550:00 - 35580:00

AI? How do I learn whatever? So, let's

## 35580:00 - 35630:00

just say you want to um do a something

## 35630:00 - 35660:00

about like pet grooming for example. So,

## 35660:00 - 35690:00

you want to like create a you know a

## 35690:00 - 35725:00

lead gen for your pet grooming business.

## 35725:00 - 35760:00

What I would do is I just go on to Manis

## 35760:00 - 35805:00

or go on to Perplexity or Deep Research

## 35805:00 - 35835:00

or one of these tools and literally just

## 35835:00 - 35870:00

ask it like what are the best tips for

## 35870:00 - 35895:00

dog grooming? Go find me all the top

## 35895:00 - 35920:00

YouTube videos in the space. You take

## 35920:00 - 35960:00

this content, you put into notion, you

## 35960:00 - 35985:00

make it look somewhat nice, and then you

## 35985:00 - 36010:00

take that and you put it behind a

## 36010:00 - 36065:00

gumroad like like um like link where you

## 36065:00 - 36090:00

have to give you have to give someone

## 36090:00 - 36140:00

your email and it's so like no-brainer.

## 36140:00 - 36175:00

Like it's like you just make it super,

## 36175:00 - 36210:00

you know, direct. Here are 10 the best

## 36210:00 - 36240:00

videos on how to do doging or whatever

## 36240:00 - 36275:00

it is, but that becomes your lead genet.

## 36275:00 - 36305:00

And I think that like so many people are

## 36305:00 - 36340:00

so scared to like make content like this

## 36340:00 - 36370:00

is such lowhanging fruit. And obviously

## 36370:00 - 36395:00

like you got to test it. Like your first

## 36395:00 - 36415:00

one's probably not going to hit and be

## 36415:00 - 36445:00

like a you know drive a million dollars

## 36445:00 - 36470:00

in sales right away, but eventually you

## 36470:00 - 36495:00

will figure out okay this is what people

## 36495:00 - 36530:00

like. Um and I really recommend doing

## 36530:00 - 36550:00

this regardless of what your space

## 36550:00 - 36580:00

you're in. So it's like not rocket

## 36580:00 - 36605:00

science stuff. It's just like how are

## 36605:00 - 36635:00

you lo and I I really tried to make sure

## 36635:00 - 36655:00

like we're not talking like you're like

## 36655:00 - 36680:00

hey you need to go get your engineering

## 36680:00 - 36715:00

team to go commit like like four week

## 36715:00 - 36735:00

sprint on building all these agents.

## 36735:00 - 36755:00

Like what are the tools that exist right

## 36755:00 - 36770:00

now and how can you leverage them in the

## 36770:00 - 36795:00

best way possible?

## 36795:00 - 36835:00

Totally. Yeah. I mean I that we're using

## 36835:00 - 36875:00

a version of that for like my personal

## 36875:00 - 36905:00

email newsletter growth like we just

## 36905:00 - 36940:00

took an episode right turned it into a

## 36940:00 - 36980:00

PDF download like using a transcript and

## 36980:00 - 37020:00

then claude and then uh just have a call

## 37020:00 - 37045:00

to action basically like if you want

## 37045:00 - 37085:00

this thing like you know comment or

## 37085:00 - 37110:00

whatever get it here right and then it's

## 37110:00 - 37135:00

just it's basically just but you could

## 37135:00 - 37160:00

do that on a weekly cadence like this

## 37160:00 - 37195:00

this what we're recording right now is

## 37195:00 - 37220:00

could be turned into this exact same

## 37220:00 - 37250:00

thing right like here's the use case you

## 37250:00 - 37305:00

know the uh the 10 ways that uh AI is

## 37305:00 - 37340:00

being used within or you know agents are

## 37340:00 - 37395:00

being used um within marketing in 2025

## 37395:00 - 37425:00

right something like that it's like

## 37425:00 - 37430:00

perfect

## 37430:00 - 37480:00

both once twice like build it's like hey

## 37480:00 - 37510:00

I record this episode today when's the

## 37510:00 - 37530:00

written piece of content coming out when

## 37530:00 - 37560:00

is the clip going out like build that

## 37560:00 - 37580:00

process out and I think it's so

## 37580:00 - 37595:00

important and just try and figure out

## 37595:00 - 37620:00

what's repeatable as much as possible

## 37620:00 - 37645:00

like you don't need to reinvent the

## 37645:00 - 37665:00

wheel every week I think so many people

## 37665:00 - 37690:00

like really want to go and create some

## 37690:00 - 37715:00

crazy content like I'm all the power to

## 37715:00 - 37735:00

you but like if you're running a company

## 37735:00 - 37765:00

like how much time can I really dedicate

## 37765:00 - 37800:00

to content creation and like growing a

## 37800:00 - 37815:00

following every day. It's like at the

## 37815:00 - 37830:00

end of the day like I have to my

## 37830:00 - 37850:00

priority is running the business. So,

## 37850:00 - 37865:00

you got to figure out these automations

## 37865:00 - 37900:00

and figure out like one thing as well is

## 37900:00 - 37925:00

like how do you empower your like VA or

## 37925:00 - 37955:00

your assistant to use these tools? Um I

## 37955:00 - 37995:00

remember like I was showing my VA um

## 37995:00 - 38025:00

Auto Grid forever ago before it was like

## 38025:00 - 38050:00

publicly released and she just came to

## 38050:00 - 38075:00

me. She's like I can I show this to my

## 38075:00 - 38105:00

team like like one of my friends in the

## 38105:00 - 38125:00

Philippines. She goes like if they had

## 38125:00 - 38145:00

access to this this would like change

## 38145:00 - 38180:00

their life and there's tools like this

## 38180:00 - 38190:00

like you just need to make sure that

## 38190:00 - 38215:00

they're even aware that these tools

## 38215:00 - 38250:00

exist um and then leverage them to the

## 38250:00 - 38280:00

best of your abilities.

## 38280:00 - 38315:00

No. 100%. But I think for a lot of

## 38315:00 - 38330:00

people though, it's just like this

## 38330:00 - 38370:00

daunting task and like what you need to

## 38370:00 - 38395:00

break it down into it's like what is the

## 38395:00 - 38425:00

10% that you can automate today and then

## 38425:00 - 38455:00

how do you just automate 10% you know

## 38455:00 - 38485:00

over the next whatever month. It's not

## 38485:00 - 38515:00

like I doesn't have to be a huge

## 38515:00 - 38545:00

overhaul. And I feel like you probably

## 38545:00 - 38565:00

experienced that with a lot of the

## 38565:00 - 38590:00

enterprise like clients that you guys

## 38590:00 - 38605:00

work with where they're like yo we want

## 38605:00 - 38630:00

to automate this whole thing. Like

## 38630:00 - 38660:00

actually let's start with the smaller

## 38660:00 - 38685:00

piece and then we're going to work our

## 38685:00 - 38720:00

way up into this. Um, could you talk to

## 38720:00 - 38755:00

me about like agents uh interacting with

## 38755:00 - 38775:00

other agents and like what those

## 38775:00 - 38800:00

workflows look like? Um, again, I think

## 38800:00 - 38835:00

this is one of those things that people

## 38835:00 - 38875:00

hear they don't like what are the

## 38875:00 - 38900:00

tangible versions of this and I almost

## 38900:00 - 38930:00

just want to treat the last bit of this

## 38930:00 - 38960:00

episode where we just like rapidfire

## 38960:00 - 38985:00

sprint through all these different ways

## 38985:00 - 39015:00

that people are using in it or using

## 39015:00 - 39050:00

these agents within within like business

## 39050:00 - 39065:00

workflows. So

## 39065:00 - 39100:00

sweet. So like multi- aents are like the

## 39100:00 - 39140:00

future. We we bet on this like early on.

## 39140:00 - 39170:00

uh really the best agents across like

## 39170:00 - 39195:00

every category maybe except for like the

## 39195:00 - 39215:00

customer support all have some type of

## 39215:00 - 39255:00

multi- aent um tendencies. So you can

## 39255:00 - 39275:00

think about these like multi- aent

## 39275:00 - 39305:00

systems as like different agents like or

## 39305:00 - 39320:00

different team members who are working

## 39320:00 - 39365:00

together to get a single job done. So

## 39365:00 - 39395:00

for example, you could have an HR agent

## 39395:00 - 39440:00

that um writes a job description then

## 39440:00 - 39470:00

pulls data from your website to make it

## 39470:00 - 39505:00

relevant then reviews it and then

## 39505:00 - 39530:00

actually has it posted on glass door.

## 39530:00 - 39555:00

Like that's an entire workflow that like

## 39555:00 - 39575:00

there's all these different agents that

## 39575:00 - 39610:00

are doing different tasks. Um, and the

## 39610:00 - 39630:00

cool thing about these agents that you

## 39630:00 - 39650:00

can give each one of them different

## 39650:00 - 39680:00

tools and different LLMs, so you're not

## 39680:00 - 39705:00

just, you know, the most expensive

## 39705:00 - 39725:00

models you don't need to be using every

## 39725:00 - 39760:00

time. Um, we use Gemini for a bunch of

## 39760:00 - 39790:00

tasks just because it's incredibly

## 39790:00 - 39830:00

effective and incredibly uh efficient um

## 39830:00 - 39865:00

when it comes down to cost. So think

## 39865:00 - 39890:00

about these like different team members,

## 39890:00 - 39910:00

different people have different brains.

## 39910:00 - 39940:00

Like you can basically get as defined as

## 39940:00 - 39960:00

you want with them and then you can

## 39960:00 - 39985:00

basically have them go do any task you

## 39985:00 - 40025:00

want. So the one framework we've been

## 40025:00 - 40050:00

really using like it just came out a

## 40050:00 - 40075:00

couple weeks ago now um is the OpenAI

## 40075:00 - 40110:00

agents SDK um so we were one of the

## 40110:00 - 40140:00

launch partners with it uh for platform

## 40140:00 - 40175:00

agent ops and it's been wild how good it

## 40175:00 - 40205:00

is. So like yes you have to be a

## 40205:00 - 40235:00

developer to use these tools but you

## 40235:00 - 40265:00

don't need to be like you know crazy

## 40265:00 - 40290:00

math wizard to get started. It's just

## 40290:00 - 40320:00

watch a couple tutorials like I there's

## 40320:00 - 40350:00

so much content out there and like just

## 40350:00 - 40385:00

start looking at like what's working. Um

## 40385:00 - 40410:00

but these multi- aent systems are insane

## 40410:00 - 40445:00

because you can basically curate like an

## 40445:00 - 40465:00

entire endto-end workflow. everything

## 40465:00 - 40485:00

from like go and interact with this

## 40485:00 - 40525:00

website to pull this data into the CRM

## 40525:00 - 40555:00

to draft this email and have it ready to

## 40555:00 - 40585:00

go into my drafts and these just become

## 40585:00 - 40605:00

little agents that are just either

## 40605:00 - 40630:00

sequential or working together to

## 40630:00 - 40665:00

actually go complete a task. U and we've

## 40665:00 - 40690:00

seen crazy automations built out with

## 40690:00 - 40710:00

with this type of stuff.

## 40710:00 - 40740:00

What what let's get into the technical

## 40740:00 - 40765:00

pieces because like this audience they

## 40765:00 - 40790:00

this is what they live for, right? So

## 40790:00 - 40820:00

it's like okay what are the stacks that

## 40820:00 - 40840:00

you're using? Is it are you using like

## 40840:00 - 40875:00

frameworks like crew? What what what is

## 40875:00 - 40900:00

actually working right now? What are the

## 40900:00 - 40930:00

models that are working right now? like

## 40930:00 - 40955:00

where where should people be like

## 40955:00 - 40985:00

investing their time based off of the

## 40985:00 - 41010:00

data you guys are seeing from the front

## 41010:00 - 41020:00

lines.

## 41020:00 - 41040:00

So yeah, we've seen like millions of

## 41040:00 - 41065:00

agent runs now. So like we have a good

## 41065:00 - 41085:00

sense of like what actually works and

## 41085:00 - 41130:00

what doesn't. Um and so a couple things

## 41130:00 - 41165:00

we built out a framework a while ago

## 41165:00 - 41185:00

called agent stack. And what it

## 41185:00 - 41205:00

basically is like you can choose any

## 41205:00 - 41240:00

LLM. You can choose and I guess I need a

## 41240:00 - 41255:00

graphic after you might be able to like

## 41255:00 - 41275:00

put it up right here or something like

## 41275:00 - 41305:00

that. Um but basically you can choose

## 41305:00 - 41325:00

what model you want. You can choose what

## 41325:00 - 41345:00

framework you want. So we're integrated

## 41345:00 - 41405:00

with like crew AI langraph um agents SDK

## 41405:00 - 41430:00

and llama index. Those are like the four

## 41430:00 - 41450:00

that we're seeing a ton of traction

## 41450:00 - 41470:00

with. There's some other cool ones like

## 41470:00 - 41495:00

Monster and a bunch of them. Um, but

## 41495:00 - 41515:00

what really makes these frameworks

## 41515:00 - 41545:00

powerful, like we are totally agnostic

## 41545:00 - 41570:00

in terms Oh, and Autogen's another one

## 41570:00 - 41600:00

from Microsoft that's really good. Um,

## 41600:00 - 41625:00

but we're totally agnostic when it comes

## 41625:00 - 41650:00

to frameworks. It's like all I care

## 41650:00 - 41670:00

about is what's going to get us the best

## 41670:00 - 41705:00

outcome. Um, and usually like each one

## 41705:00 - 41735:00

of these agent frameworks has different

## 41735:00 - 41765:00

benefits. I say like LLM really depends

## 41765:00 - 41785:00

on the use case. If you're looking more

## 41785:00 - 41830:00

coding specific, cloud from anthropic is

## 41830:00 - 41855:00

by far the best. If you're looking for

## 41855:00 - 41880:00

better like reasoning models, you know,

## 41880:00 - 41915:00

maybe the open models or the Google

## 41915:00 - 41950:00

models are the best. And it really just

## 41950:00 - 41980:00

depends on the use case. So, this is one

## 41980:00 - 42000:00

thing like it does take some trial and

## 42000:00 - 42025:00

error. We have like a whole eval testing

## 42025:00 - 42045:00

platform that like helps out with this

## 42045:00 - 42075:00

type of stuff. Um, but you kind of just

## 42075:00 - 42100:00

have to start like taking swings at bat

## 42100:00 - 42130:00

and seeing what hits is the most kind of

## 42130:00 - 42170:00

important piece. Um, but what gets these

## 42170:00 - 42210:00

agents super powerful are two things.

## 42210:00 - 42250:00

It's tools and then internal data. So,

## 42250:00 - 42285:00

um, within our agent stack framework and

## 42285:00 - 42305:00

like you can use these with any of these

## 42305:00 - 42335:00

frameworks as well. There's a whole

## 42335:00 - 42355:00

bunch of tools that crush it. So like

## 42355:00 - 42390:00

there's agent QL which is an amazing

## 42390:00 - 42420:00

like basically like web research tool

## 42420:00 - 42450:00

can pull data can take actions for you.

## 42450:00 - 42470:00

You have tools like browser based

## 42470:00 - 42500:00

browser use which I mentioned. There's

## 42500:00 - 42520:00

composio which like allows you to

## 42520:00 - 42540:00

connect to I think like a few hundred

## 42540:00 - 42570:00

apps now which is insane. So now when

## 42570:00 - 42590:00

you're building on agent you're not like

## 42590:00 - 42625:00

limited by like the LLMs or or taking

## 42625:00 - 42655:00

action. Now you can do any action on the

## 42655:00 - 42690:00

on the web which is incredible. You can

## 42690:00 - 42720:00

take any action within like any API call

## 42720:00 - 42745:00

which is great. You can do all

## 42745:00 - 42785:00

automatically. um you can do payments

## 42785:00 - 42815:00

through Stripe or Payman or one of these

## 42815:00 - 42840:00

companies. So it's really really cool to

## 42840:00 - 42860:00

like once you kind of break down this

## 42860:00 - 42885:00

whole process, it's like okay, what

## 42885:00 - 42915:00

tools do I need to accomplish this task

## 42915:00 - 42940:00

and the second piece is what internal

## 42940:00 - 42970:00

data do I need to access in order to get

## 42970:00 - 43005:00

there? Um so Nvidia last week released

## 43005:00 - 43030:00

like a whole suite of different tools

## 43030:00 - 43060:00

for actually pulling in all this data.

## 43060:00 - 43095:00

Um we've been like chatting with a bunch

## 43095:00 - 43120:00

of companies who have data in like data

## 43120:00 - 43145:00

bricks and in snowflake and all these

## 43145:00 - 43165:00

traditional places and now all these

## 43165:00 - 43190:00

companies are making all this data agent

## 43190:00 - 43230:00

accessible. So really like the the

## 43230:00 - 43270:00

structure um is as follows. Like you got

## 43270:00 - 43285:00

to figure out your LM, you got to figure

## 43285:00 - 43310:00

out what framework you want to use or

## 43310:00 - 43350:00

just build your own custom agent. Um I

## 43350:00 - 43380:00

said like agents SDK is incredibly

## 43380:00 - 43400:00

impressive right now. If you haven't

## 43400:00 - 43425:00

heard about or tested out yet, like jump

## 43425:00 - 43450:00

off this and try it. You got to figure

## 43450:00 - 43475:00

out your tools. You got to figure out

## 43475:00 - 43495:00

your internal data. And then you got to

## 43495:00 - 43525:00

figure out like your monitoring evalu.

## 43525:00 - 43540:00

And that's where we've been helping with

## 43540:00 - 43570:00

agent ops. But like that's kind of the

## 43570:00 - 43595:00

lay of the land. It's like important to

## 43595:00 - 43620:00

like test a bunch of stuff and like give

## 43620:00 - 43650:00

your team like 1 hour sprints is what I

## 43650:00 - 43680:00

recommend. Like hey, here's an hour. Go

## 43680:00 - 43705:00

watch a YouTube video for 15 minutes and

## 43705:00 - 43730:00

for 45 minutes get as far as humanly

## 43730:00 - 43760:00

possible and I'm confident you could

## 43760:00 - 43790:00

probably get 80% of the way there using

## 43790:00 - 43815:00

agent stack or using crew or using one

## 43815:00 - 43840:00

of these frameworks just by like

## 43840:00 - 43865:00

literally going into it and just trying

## 43865:00 - 43885:00

to get as much done as quickly as

## 43885:00 - 43910:00

possible. That's fascinating. Are you

## 43910:00 - 43950:00

seeing anybody build these with like I I

## 43950:00 - 43970:00

don't know how like good the

## 43970:00 - 43990:00

documentation is at this point just

## 43990:00 - 44010:00

because it's like early in the

## 44010:00 - 44035:00

frameworks but like are people like vibe

## 44035:00 - 44060:00

coding agents yet or has that happened

## 44060:00 - 44085:00

like what is because I'm just imagining

## 44085:00 - 44110:00

from like you know I'm technicalish

## 44110:00 - 44145:00

right I want to start experimenting with

## 44145:00 - 44170:00

this like and again just like small

## 44170:00 - 44190:00

stuff where it's like cool like I'm

## 44190:00 - 44210:00

going to give it access to this Twitter

## 44210:00 - 44240:00

account here's source information that

## 44240:00 - 44270:00

it can pull from go write tweets in a

## 44270:00 - 44295:00

frame you know format like this

## 44295:00 - 44325:00

optimized based off of impressions again

## 44325:00 - 44355:00

something small and dumb but like when

## 44355:00 - 44390:00

that you you compound all of those

## 44390:00 - 44410:00

things like it gets It's very

## 44410:00 - 44450:00

interesting. So talk to me about, you

## 44450:00 - 44470:00

know, if you're a technicalish and

## 44470:00 - 44490:00

you're trying to get into this, what

## 44490:00 - 44515:00

does that look like from a from a

## 44515:00 - 44530:00

process?

## 44530:00 - 44560:00

Watch YouTube. Try as much as possible

## 44560:00 - 44585:00

with cursor on these tools. Like they

## 44585:00 - 44610:00

are getting good. Uh we have a launch

## 44610:00 - 44640:00

coming up. Uh I don't have the exact

## 44640:00 - 44670:00

date, but it's going to make it a lot

## 44670:00 - 44695:00

easier to do a lot of these things. We

## 44695:00 - 44725:00

we've realized it's a huge barrier. Um

## 44725:00 - 44750:00

but this is a good time to just plug

## 44750:00 - 44780:00

like all the no code agent tools or like

## 44780:00 - 44810:00

you know AI automation tools. So like

## 44810:00 - 44840:00

you have Lutra AI which is incredible.

## 44840:00 - 44870:00

You have Gum Loop which is incredible.

## 44870:00 - 44900:00

Um you got to try those. you got to use

## 44900:00 - 44925:00

Manis. Like try this stuff out. Like

## 44925:00 - 44955:00

it's it's worth it. Um there's a bunch

## 44955:00 - 44985:00

of other ones like NAND is amazing. Zap

## 44985:00 - 45020:00

year is really powerful. Like just like

## 45020:00 - 45045:00

if you're not technical but you still

## 45045:00 - 45070:00

want to figure out how far you can go

## 45070:00 - 45095:00

with these things, just try out these

## 45095:00 - 45135:00

tools and see how far you can get. Um I

## 45135:00 - 45160:00

know it's like kind of daunting to like

## 45160:00 - 45180:00

become a developer and try and actually

## 45180:00 - 45205:00

building building out these things for

## 45205:00 - 45220:00

yourself, but

## 45220:00 - 45240:00

it's less than it's ever been. I think

## 45240:00 - 45265:00

that's the thing though. like I like as

## 45265:00 - 45305:00

a marketer it's like I I historically

## 45305:00 - 45330:00

I'd be like oh this isn't a good enough

## 45330:00 - 45360:00

investment from a time standpoint for me

## 45360:00 - 45390:00

because the impact that I can create is

## 45390:00 - 45415:00

like not high enough right but like now

## 45415:00 - 45455:00

I'm like okay cool like I needed a

## 45455:00 - 45480:00

keyword to duplication software for

## 45480:00 - 45510:00

bottom ofunnel keywords like I wrote it

## 45510:00 - 45540:00

over this weekend with like and like

## 45540:00 - 45570:00

it's deployed now my team's using it on

## 45570:00 - 45615:00

Monday right I'm like it was I did like

## 45615:00 - 45635:00

basically was like this is a pain in the

## 45635:00 - 45665:00

ass we decided that Friday and this

## 45665:00 - 45710:00

weekend built the software right it it's

## 45710:00 - 45745:00

nothing like crazy but it just saved my

## 45745:00 - 45780:00

team like you know probably three hours

## 45780:00 - 45815:00

of work a week. I mean we'll do that all

## 45815:00 - 45845:00

day long, right? I think I think now

## 45845:00 - 45870:00

it's like we're at that tipping point

## 45870:00 - 45900:00

where maybe it actually does make sense

## 45900:00 - 45925:00

especially if it's like oh if I can

## 45925:00 - 45960:00

figure out how to automate this task

## 45960:00 - 46005:00

that I individually had to do previously

## 46005:00 - 46040:00

or like de dedicate to a team or

## 46040:00 - 46080:00

delegate to a team member with one of

## 46080:00 - 46105:00

these agents like even if it's just like

## 46105:00 - 46145:00

customer you know competitor ad research

## 46145:00 - 46170:00

right that's like what are the common

## 46170:00 - 46195:00

threads between everything you're seeing

## 46195:00 - 46230:00

in these five like you know Facebook ad

## 46230:00 - 46265:00

libraries of these five competitors and

## 46265:00 - 46295:00

it just gives me a synopsis of that on a

## 46295:00 - 46330:00

weekly basis for all the new ads like

## 46330:00 - 46380:00

all day long. I'll do 100% that that's

## 46380:00 - 46425:00

worth it from a build standpoint. So, um

## 46425:00 - 46455:00

like I think one thing is just like go

## 46455:00 - 46475:00

through your work week over the next

## 46475:00 - 46505:00

week and literally just like write down

## 46505:00 - 46530:00

in a Google doc like here a bunch of

## 46530:00 - 46560:00

things I think I can automate and get as

## 46560:00 - 46590:00

detailed as possible, take looms of it,

## 46590:00 - 46620:00

whatever it might be and like either

## 46620:00 - 46645:00

just like tag me on social media or send

## 46645:00 - 46680:00

it to my email like Adamops.ai. I'll

## 46680:00 - 46700:00

literally just tell you like hey this is

## 46700:00 - 46730:00

possible or not. Like I love giving like

## 46730:00 - 46750:00

like I've just seen so many of these use

## 46750:00 - 46775:00

cases like I've tested like over 500

## 46775:00 - 46805:00

agents now. I have a good sense of what

## 46805:00 - 46825:00

works and what doesn't. I wish I could

## 46825:00 - 46860:00

like just once I do my 12 hours in the

## 46860:00 - 46880:00

studio of like getting everything out of

## 46880:00 - 46905:00

my brain, I promise you'll have someone

## 46905:00 - 46935:00

to talk to. Um, but this is the type of

## 46935:00 - 46960:00

thing where it's like just start trying

## 46960:00 - 46980:00

like go ask people on social media be

## 46980:00 - 47010:00

like, "Hey, I do this task every day.

## 47010:00 - 47035:00

Blur out all your, you know, personal

## 47035:00 - 47070:00

information and see like if people have

## 47070:00 - 47105:00

responses." Um, we've also been helping

## 47105:00 - 47125:00

like a bunch of companies build out

## 47125:00 - 47155:00

these custom solutions. Uh, and it's

## 47155:00 - 47185:00

it's cool to see like a lot of

## 47185:00 - 47210:00

businesses, they know these problems

## 47210:00 - 47230:00

existed. Like some companies have been

## 47230:00 - 47255:00

to, hey, we've thought about this for

## 47255:00 - 47280:00

the past 5 years, but now we're seeing

## 47280:00 - 47325:00

AI blow up. Like, is this possible now?

## 47325:00 - 47355:00

And we had one website or one company

## 47355:00 - 47380:00

that came to us, they have a bunch of

## 47380:00 - 47415:00

park domains, like insane amount of park

## 47415:00 - 47440:00

domains, and they want us to create

## 47440:00 - 47465:00

custom websites for all these different

## 47465:00 - 47500:00

park domains and basically have it based

## 47500:00 - 47535:00

on cookie history. Okay, can a new

## 47535:00 - 47560:00

programmatically generate a website come

## 47560:00 - 47585:00

up? Almost like how Amazon knows when

## 47585:00 - 47610:00

you show up, you know, hey, you want

## 47610:00 - 47630:00

these products. Can you do the same

## 47630:00 - 47665:00

thing with like news sites and like

## 47665:00 - 47690:00

e-commerce stores, a bunch of stuff like

## 47690:00 - 47710:00

that? And this is something like now

## 47710:00 - 47740:00

with agents is like very possible, but

## 47740:00 - 47755:00

they've been sitting on this idea and

## 47755:00 - 47790:00

like cooking on it for so long. And I

## 47790:00 - 47815:00

think like now with like just go and

## 47815:00 - 47845:00

like rapidly prototype or like find a

## 47845:00 - 47865:00

team like ours or someone that can like

## 47865:00 - 47895:00

actually just go build this for you cuz

## 47895:00 - 47915:00

you're not going to have a seat at the

## 47915:00 - 47935:00

table in a year from now if you haven't

## 47935:00 - 47965:00

gone and implemented this tech. And I

## 47965:00 - 47985:00

really really in my heart of hearts

## 47985:00 - 48015:00

believe that just cuz there's companies

## 48015:00 - 48035:00

who are on the bleeding edge who just

## 48035:00 - 48075:00

like all this like historical ideas that

## 48075:00 - 48100:00

you know these legacy players had great

## 48100:00 - 48120:00

we're throwing it all out and we're just

## 48120:00 - 48150:00

going like AI native day zero and it

## 48150:00 - 48190:00

really is paying dividends for them.

## 48190:00 - 48215:00

That's amazing, man. What What should I

## 48215:00 - 48245:00

be asking you that I haven't been? Like

## 48245:00 - 48275:00

what's something that like you feel like

## 48275:00 - 48305:00

is the future where all this is headed?

## 48305:00 - 48330:00

Especially something that like a head of

## 48330:00 - 48355:00

growth, a founder, like a head of

## 48355:00 - 48380:00

marketing should be focused on over the

## 48380:00 - 48425:00

next, you know, whatever nine months.

## 48425:00 - 48455:00

So, a couple things is like run internal

## 48455:00 - 48480:00

hackathons with your company. like go

## 48480:00 - 48500:00

and like actually give them access to

## 48500:00 - 48525:00

all these tools and like encourage them

## 48525:00 - 48565:00

like even if it's like one day like a

## 48565:00 - 48585:00

month or something like that just like

## 48585:00 - 48615:00

hey I saw like bookmark a bunch of stuff

## 48615:00 - 48645:00

on Twitter and be like go test this

## 48645:00 - 48695:00

stuff and like dedicate like a safe

## 48695:00 - 48720:00

space for them to go work on it where

## 48720:00 - 48745:00

it's like today we're booking off and

## 48745:00 - 48775:00

there's no like email BS you have to do

## 48775:00 - 48795:00

and all this stuff it's like I'm going

## 48795:00 - 48820:00

to go test all these tools and we've

## 48820:00 - 48845:00

seen a lot of companies have success

## 48845:00 - 48865:00

with that. We've even run some like

## 48865:00 - 48900:00

internal hackathons of like Fortune 500s

## 48900:00 - 48910:00

where it's like, "Hey, we're just going

## 48910:00 - 48930:00

to come in and bring you up to speed on

## 48930:00 - 48970:00

all this stuff." That is like you you

## 48970:00 - 49000:00

realize how bright your employees are

## 49000:00 - 49025:00

and how excited they are about it. They

## 49025:00 - 49060:00

just don't really have the like the

## 49060:00 - 49085:00

guard rails or whatever to like go and

## 49085:00 - 49115:00

experiment in like a safe way. So like

## 49115:00 - 49135:00

that that's one thing I think is super

## 49135:00 - 49185:00

important. Um couple other things is

## 49185:00 - 49205:00

just like there's a lot of fluff out

## 49205:00 - 49235:00

there. So like test like be quick to

## 49235:00 - 49260:00

test stuff, but also be okay with like

## 49260:00 - 49280:00

you know it's fine if you do like a

## 49280:00 - 49305:00

little test for 100 bucks. If it doesn't

## 49305:00 - 49325:00

work for you, go on to the next thing.

## 49325:00 - 49365:00

don't like get pigeonheld to u one thing

## 49365:00 - 49405:00

that I have an issue with is like a lot

## 49405:00 - 49430:00

of companies try agents and they have

## 49430:00 - 49455:00

really bad experiences with them and

## 49455:00 - 49480:00

then they just like write off like the

## 49480:00 - 49505:00

entire prospect of having an agent

## 49505:00 - 49535:00

strategy and that's one thing that's

## 49535:00 - 49560:00

really really tough for me to see where

## 49560:00 - 49595:00

it's like be okay like testing stuff and

## 49595:00 - 49625:00

be okay just saying okay like I made a

## 49625:00 - 49645:00

small investment in it didn't work I'm

## 49645:00 - 49695:00

on to the next thing um other things is

## 49695:00 - 49700:00

just

## 49700:00 - 49730:00

I think that's can we go can we double

## 49730:00 - 49750:00

click I know we only have a couple more

## 49750:00 - 49770:00

minutes I just want to go deeper on that

## 49770:00 - 49820:00

idea of like there is so much fluff like

## 49820:00 - 49855:00

you see so like huge promises within

## 49855:00 - 49895:00

this agent space. Like how do you filter

## 49895:00 - 49930:00

through that? Is it just try things and

## 49930:00 - 49960:00

see what works or is it is there is

## 49960:00 - 49990:00

there good resources that you would lean

## 49990:00 - 50025:00

on? Like who who is the where is the

## 50025:00 - 50060:00

best information to basically get into

## 50060:00 - 50085:00

this for the people that are trying to

## 50085:00 - 50135:00

have initiative and and you know start

## 50135:00 - 50175:00

immediately after listening to this.

## 50175:00 - 50210:00

Yeah. So uh Twitter's the best place I

## 50210:00 - 50235:00

find for like really like cutting edge

## 50235:00 - 50270:00

agent stuff. Um, I do like a weekly

## 50270:00 - 50290:00

recap and I don't want to self plug, but

## 50290:00 - 50310:00

it's like I recap everything that goes

## 50310:00 - 50345:00

on in AI agents every week. I really

## 50345:00 - 50370:00

like everything there is like I've

## 50370:00 - 50390:00

tested or I'm in the process of testing.

## 50390:00 - 50410:00

So, I'm like I'm not just putting out

## 50410:00 - 50440:00

fluff. It's it's really as you know,

## 50440:00 - 50490:00

stuff that I find interesting. Um, but I

## 50490:00 - 50545:00

think that a lot of folks like they want

## 50545:00 - 50570:00

like companies are going to like the

## 50570:00 - 50590:00

Mckenzies of the world because they want

## 50590:00 - 50620:00

like an insurance policy being like,

## 50620:00 - 50635:00

"Hey, I'm going to go bring on

## 50635:00 - 50650:00

Mackenzie. We know they're going to go

## 50650:00 - 50680:00

do good work and whatever." But I think

## 50680:00 - 50700:00

you can be your own kind of internal

## 50700:00 - 50730:00

Mackenzie now. Like it's like go test a

## 50730:00 - 50765:00

tool. Go you know ask perplexity hey

## 50765:00 - 50785:00

what are customers saying about this

## 50785:00 - 50810:00

tool and go do this like rapid

## 50810:00 - 50840:00

discovery. So instead of spending like a

## 50840:00 - 50875:00

quarter million dollars having like in

## 50875:00 - 50905:00

no the consulting person but like

## 50905:00 - 50925:00

instead of having them put together some

## 50925:00 - 50955:00

massive brief on like why you should go

## 50955:00 - 50980:00

with the software versus other software

## 50980:00 - 51010:00

go do it yourself in like a matter of

## 51010:00 - 51030:00

like minutes and hours and like leverage

## 51030:00 - 51055:00

the tech to go and actually evaluate if

## 51055:00 - 51085:00

it's a good solution. Um I think a lot

## 51085:00 - 51110:00

of people as well like if you're not

## 51110:00 - 51135:00

facing the problem there's no need to

## 51135:00 - 51165:00

find a solution for it. And you might

## 51165:00 - 51190:00

see some flashy demo like you might look

## 51190:00 - 51215:00

at icon.me me and be like, "Wow, I want

## 51215:00 - 51245:00

to make more UGC. This is great." But if

## 51245:00 - 51275:00

you weren't doing UGC to begin with, you

## 51275:00 - 51300:00

probably don't need to use that tech.

## 51300:00 - 51325:00

So, it's like find like the actual

## 51325:00 - 51340:00

problems you're facing. And that's why

## 51340:00 - 51365:00

I'm very big on like like create a list

## 51365:00 - 51390:00

of here are all the things that I'm

## 51390:00 - 51410:00

seeing. Here are all the issues that I'm

## 51410:00 - 51440:00

seeing and really leaning into that um

## 51440:00 - 51465:00

as much as possible.

## 51465:00 - 51500:00

Okay. So, last thing I I I want to ask

## 51500:00 - 51535:00

you before you jump. Um if you want to

## 51535:00 - 51570:00

go build your first agent today, what

## 51570:00 - 51595:00

does that look like? You know, you're a

## 51595:00 - 51610:00

marketer, you're a head of growth,

## 51610:00 - 51640:00

you're a founder, you're trying to, you

## 51640:00 - 51670:00

know, do something for for for your

## 51670:00 - 51705:00

company. What what's the easiest stack

## 51705:00 - 51730:00

that they can do to have something out

## 51730:00 - 51755:00

in the next two hours?

## 51755:00 - 51795:00

Oh, well like you can get 80% of the way

## 51795:00 - 51830:00

with almost any a with agent stack. Like

## 51830:00 - 51865:00

you can basically, you know, dream it

## 51865:00 - 51885:00

and you can use whatever top framework

## 51885:00 - 51905:00

you want, whatever tools you want. So

## 51905:00 - 51940:00

that's pretty quick. Um, but I really

## 51940:00 - 51970:00

recommend like anybody who's listening

## 51970:00 - 52005:00

to this like just start by documenting

## 52005:00 - 52025:00

processes. Like when you're going to

## 52025:00 - 52045:00

start building evals, when you're going

## 52045:00 - 52065:00

to start building reliable agents, you

## 52065:00 - 52095:00

have to have a very clear understanding

## 52095:00 - 52125:00

of exactly what the agent does. If you

## 52125:00 - 52145:00

don't have that, there's no point of

## 52145:00 - 52170:00

even thinking about automation. Um,

## 52170:00 - 52195:00

there's a blog post I'll link to after

## 52195:00 - 52220:00

that one of our engineers wrote about

## 52220:00 - 52240:00

like how to think through like

## 52240:00 - 52270:00

developing these agents, but it's really

## 52270:00 - 52305:00

critical. Like I can't emphasize enough

## 52305:00 - 52325:00

like think through like here's the

## 52325:00 - 52350:00

entire workflow and really jump in from

## 52350:00 - 52385:00

there. But Cody, always thank you so

## 52385:00 - 52415:00

much for having me. Um, and we'll go

## 52415:00 - 52435:00

from here, but enjoy the day.

## 52435:00 - 52455:00

Awesome, man. Thanks for coming on. I

## 52455:00 - 52475:00

appreciate you. We'll talk to you soon.

## 52475:00+

Yeah. Byebye.

