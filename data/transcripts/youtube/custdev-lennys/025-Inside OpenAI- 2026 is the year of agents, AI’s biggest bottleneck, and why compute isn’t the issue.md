---
source: https://www.youtube.com/watch?v=z1ISq9Ty4Cg
title: "Inside OpenAI: 2026 is the year of agents, AI’s biggest bottleneck, and
  why compute isn’t the issue"
author: Lenny's Podcast
date: 2025-12-14
views: 28904
description: |-
  Alexander Embiricos leads product on Codex, OpenAI’s powerful coding agent, which has grown 20x since August and now serves trillions of tokens weekly. Before joining OpenAI, Alexander spent five years building a pair programming product for engineers. He now works at the frontier of AI-led software development, building what he describes as a software engineering teammate—an AI agent designed to participate across the entire development lifecycle.

  *We discuss:*
  1. Why Codex has grown 20x since launch and what product decisions unlocked this growth
  2. How OpenAI built the Sora Android app in just 18 days using Codex
  3. Why the real bottleneck to AGI-level productivity isn’t model capability—it’s human typing speed
  4. The vision of AI as a proactive teammate, not just a tool you prompt
  5. The bottleneck shifting from building to reviewing AI-generated work
  6. Why coding will be a core competency for every AI agent—because writing code is how agents use computers best

  *Brought to you by:*
  WorkOS—Modern identity platform for B2B SaaS, free up to 1 million MAUs: https://workos.com/lenny
  Fin—The #1 AI agent for customer service: https://fin.ai/lenny
  Jira Product Discovery—Confidence to build the right thing: https://atlassian.com/lenny

  *Transcript:* https://www.lennysnewsletter.com/p/why-humans-are-ais-biggest-bottleneck

  *My biggest takeaways (for paid newsletter subscribers):* https://www.lennysnewsletter.com/i/180365355/my-biggest-takeaways-from-this-conversation

  *Where to find Alexander Embiricos:*
  • X: https://x.com/embirico
  • LinkedIn: https://www.linkedin.com/in/embirico

  *Where to find Lenny:*
  • Newsletter: https://www.lennysnewsletter.com
  • X: https://twitter.com/lennysan
  • LinkedIn: https://www.linkedin.com/in/lennyrachitsky/

  *In this episode, we cover:*
  (00:00) Introduction to Alexander Embiricos 
  (05:13) The speed and ambition at OpenAI
  (11:34) Codex: OpenAI’s coding agent
  (15:43) Codex’s explosive growth
  (24:59) The future of AI and coding agents
  (33:11) The impact of AI on engineering
  (44:08) How Codex has impacted the way PMs operate
  (45:40) Throwaway code and ubiquitous coding
  (47:10) Shipping the Sora Android app
  (49:01) Building the Atlas browser
  (53:34) Codex’s impact on productivity
  (55:35) Measuring progress on Codex
  (58:09) Why they are building a web browser
  (01:01:58) Non-engineering use cases for Codex
  (01:02:53) Codex’s capabilities
  (01:04:49) Tips for getting started with Codex
  (01:05:37) Skills to lean into in the AI age
  (01:10:36) How far are we from a human version of AI?
  (01:13:31) Hiring and team growth at Codex
  (01:15:47) Lightning round and final thoughts

  *Referenced:*
  • OpenAI: https://openai.com
  • Codex: https://openai.com/codex
  • Inside ChatGPT: The fastest-growing product in history | Nick Turley (Head of ChatGPT at OpenAI): https://www.lennysnewsletter.com/p/inside-chatgpt-nick-turley
  • Dropbox: http://dropbox.com
  • Datadog: https://www.datadoghq.com
  • Andrej Karpathy on X: https://x.com/karpathy
  • The rise of Cursor: The $300M ARR AI tool that engineers can’t stop using | Michael Truell (co-founder and CEO): https://www.lennysnewsletter.com/p/the-rise-of-cursor-michael-truell
  • Atlas: https://openai.com/index/introducing-chatgpt-atlas
  • How Block is becoming the most AI-native enterprise in the world | Dhanji R. Prasanna: https://www.lennysnewsletter.com/p/how-block-is-becoming-the-most-ai-native
  • Goose: https://block.xyz/inside/block-open-source-introduces-codename-goose
  • Lessons on building product sense, navigating AI, optimizing the first mile, and making it through the messy middle | Scott Belsky (Adobe, Behance): https://www.lennysnewsletter.com/p/lessons-on-building-product-sense
  • Sora Android app: https://play.google.com/store/apps/details?id=com.openai.sora&hl=en_US&pli=1
  • The OpenAI Podcast—ChatGPT Atlas and the next era of web browsing: https://www.youtube.com/watch?v=WdbgNC80PMw&list=PLOXw6I10VTv9GAOCZjUAAkSVyW2cDXs4u&index=2
  • How to measure AI developer productivity in 2025 | Nicole Forsgren: https://www.lennysnewsletter.com/p/how-to-measure-ai-developer-productivity
  • Compiling: https://3d.xkcd.com/303
  • Jujutsu Kaisen on Netflix: https://www.netflix.com/title/81278456
  • Tesla: https://www.tesla.com
  • Radical Candor: From theory to practice with author Kim Scott: https://www.lennysnewsletter.com/p/radical-candor-from-theory-to-practice
  • Andreas Embirikos: https://en.wikipedia.org/wiki/Andreas_Embirikos
  • George Embiricos: https://en.wikipedia.org/wiki/George_Embiricos: https://en.wikipedia.org/wiki/George_Embiricos
  ...Resources continued at: https://www.lennysnewsletter.com/p/why-humans-are-ais-biggest-bottleneck

  _Production and marketing by https://penname.co/._
  _For inquiries about sponsoring the podcast, email podcast@lennyrachitsky.com._

  Lenny may be an investor in the companies discussed.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:39:59.019Z
---

# Inside OpenAI: 2026 is the year of agents, AI’s biggest bottleneck, and why compute isn’t the issue

## 00:00 - 35:00

Who lead work on Codex? Codex is

## 35:00 - 65:00

OpenAI's coding agent. We think of Codex

## 65:00 - 85:00

as just the beginning [music]

## 85:00 - 110:00

of a software engineering teammate. It's

## 110:00 - 145:00

a bit like this really smart intern that

## 145:00 - 180:00

refuses to read Slack, doesn't check

## 180:00 - 190:00

DataDog [music]

## 190:00 - 215:00

unless you ask it to. I remember

## 215:00 - 235:00

Karpathy

## 235:00 - 270:00

>> gnarliest bugs that he runs into that he

## 270:00 - 300:00

just spends hours trying to figure out

## 300:00 - 325:00

nothing else is solved. He gives it to

## 325:00 - 350:00

Codex, lets it run for an hour and it

## 350:00 - 360:00

solves it.

## 360:00 - 380:00

>> Starting to see glimpses of the future

## 380:00 - 400:00

where we're actually starting to have

## 400:00 - 435:00

Codex be on call for its own training.

## 435:00 - 455:00

Codex writes a lot of the code that

## 455:00 - 485:00

helps like manage its training run, the

## 485:00 - 510:00

game infrastructure. And [music] so we

## 510:00 - 540:00

have a Codex code review is like

## 540:00 - 560:00

catching a lot of mistakes. It's

## 560:00 - 570:00

actually caught some like pretty

## 570:00 - 600:00

interesting configuration mistakes. One

## 600:00 - 625:00

of the most mind-blowing examples of

## 625:00 - 655:00

acceleration the Sora Android app, like

## 655:00 - 700:00

a fully new app. We built it in 18 days

## 700:00 - 740:00

and then 10 days later, so 28 days total

## 740:00 - 765:00

we went to the public. How do you think

## 765:00 - 790:00

you win [music] in this space?

## 790:00 - 815:00

>> One of our major goals with Codex is to

## 815:00 - 835:00

get to productivity.

## 835:00 - 845:00

>> If we're going to build a super

## 845:00 - 860:00

assistant, it has to be able to [music]

## 860:00 - 880:00

do things. One of the learnings over the

## 880:00 - 910:00

past year is that for models to do

## 910:00 - 935:00

stuff, they're much more effective when

## 935:00 - 955:00

they can use a computer. It turns out

## 955:00 - 980:00

the best way for models to use computers

## 980:00 - 1005:00

[music] is simply to write code. And so

## 1005:00 - 1030:00

we're kind of getting to this idea where

## 1030:00 - 1050:00

if you want to build any agent, maybe

## 1050:00 - 1080:00

you should be building a coding agent.

## 1080:00 - 1115:00

>> When you think about progress on Codex,

## 1115:00 - 1140:00

I imagine you have a bunch of evals and

## 1140:00 - 1170:00

there's all these public benchmarks.

## 1170:00 - 1195:00

>> A few of us are like constantly on

## 1195:00 - 1215:00

Reddit. You know, there's a there's

## 1215:00 - 1235:00

praise up there and there's a lot of

## 1235:00 - 1260:00

complaints. What we can do as we as a

## 1260:00 - 1280:00

product team is just try [music] to

## 1280:00 - 1300:00

always think about how are we building a

## 1300:00 - 1320:00

tool so that it feels like we're

## 1320:00 - 1350:00

maximally accelerating people rather

## 1350:00 - 1375:00

than building a tool that makes it more

## 1375:00 - 1400:00

unclear what you should do as the human.

## 1400:00 - 1440:00

>> Being at OpenAI, I can't not ask about

## 1440:00 - 1465:00

how far you think we are from AGI. The

## 1465:00 - 1485:00

current under appreciated limiting

## 1485:00 - 1515:00

[music] factor is literally human typing

## 1515:00 - 1585:00

speed or human multitasking speed.

## 1585:00 - 1625:00

Today my guest is Alexander Imbiricos,

## 1625:00 - 1660:00

product lead for Codex, OpenAI's

## 1660:00 - 1695:00

incredibly popular and powerful coding

## 1695:00 - 1730:00

agent. In the words of Nick Turley, head

## 1730:00 - 1765:00

of ChatGPT and former podcast guest,

## 1765:00 - 1800:00

Alex is one of my all-time favorite

## 1800:00 - 1830:00

humans I've ever worked with and

## 1830:00 - 1860:00

bringing him and his company into OpenAI

## 1860:00 - 1890:00

ended up being one of the best decisions

## 1890:00 - 1930:00

we've ever made. Similarly, Kevin Weil,

## 1930:00 - 1970:00

OpenAI CPO, said Alex is simply the

## 1970:00 - 2005:00

best. In our conversation, we chat about

## 2005:00 - 2040:00

what it's truly like to build product at

## 2040:00 - 2085:00

OpenAI, how Codex allowed the Sora team

## 2085:00 - 2115:00

to ship the Sora app, which became the

## 2115:00 - 2145:00

number one app in the App Store in under

## 2145:00 - 2195:00

1 month. Also, the 20x growth Codex is

## 2195:00 - 2215:00

seeing right now and what they did to

## 2215:00 - 2255:00

make it so good at coding, why his team

## 2255:00 - 2285:00

is now focused on making it easier to

## 2285:00 - 2325:00

review code, not just write code, his

## 2325:00 - 2360:00

AGI timelines, his thoughts on when AI

## 2360:00 - 2395:00

agents will actually be really useful,

## 2395:00 - 2430:00

and so much more. A huge thank you to Ed

## 2430:00 - 2465:00

Bay, Nick Turley, and Dennis Yang for

## 2465:00 - 2495:00

suggesting topics for this conversation.

## 2495:00 - 2515:00

If you enjoy this podcast, don't forget

## 2515:00 - 2545:00

to subscribe and follow it in your

## 2545:00 - 2585:00

favorite podcasting app or YouTube. And

## 2585:00 - 2615:00

if you become an annual subscriber of my

## 2615:00 - 2665:00

newsletter, you get a year free of 19

## 2665:00 - 2700:00

incredible products, including a year

## 2700:00 - 2740:00

free of Devin, Lovable, Replit, Bolt,

## 2740:00 - 2795:00

Linear, Superhuman, Descript, Warp,

## 2795:00 - 2815:00

Granola, Magic Patterns, Raycast,

## 2815:00 - 2850:00

Jasper, D Mob, and Posthog, and Stripe

## 2850:00 - 2875:00

Atlas. Head on over to Lenny's

## 2875:00 - 2915:00

Newsletter.com and click product pass.

## 2915:00 - 2940:00

With that, I bring you Alexander

## 2940:00 - 2970:00

Imbiricos after a short word from our

## 2970:00 - 3000:00

sponsors.

## 3000:00 - 3040:00

Here's a puzzle for you. What do OpenAI,

## 3040:00 - 3085:00

Cursor, Perplexity, Vercel, Plaid, and

## 3085:00 - 3115:00

hundreds of other winning companies have

## 3115:00 - 3150:00

in common? The answer is they're all

## 3150:00 - 3200:00

powered by today's sponsor, WorkOS. If

## 3200:00 - 3220:00

you're building software for

## 3220:00 - 3245:00

enterprises, you've probably felt the

## 3245:00 - 3280:00

pain of integrating single sign-on,

## 3280:00 - 3320:00

SCIM, RBAC, audit logs, and other

## 3320:00 - 3360:00

features required by big customers.

## 3360:00 - 3395:00

WorkOS turns those deal blockers into

## 3395:00 - 3435:00

drop-in APIs with a modern developer

## 3435:00 - 3465:00

platform built specifically for B2B

## 3465:00 - 3505:00

SaaS. Whether you're seed stage startup

## 3505:00 - 3525:00

trying to land your first enterprise

## 3525:00 - 3560:00

customer or a unicorn expanding

## 3560:00 - 3595:00

globally, WorkOS is the fastest [music]

## 3595:00 - 3630:00

path to becoming enterprise ready and

## 3630:00 - 3660:00

unlocking growth. They're essentially

## 3660:00 - 3705:00

Stripe for enterprise features. Visit

## 3705:00 - 3745:00

workos.com to get started or just hit up

## 3745:00 - 3770:00

their Slack support where they have real

## 3770:00 - 3795:00

engineers in there who answer your

## 3795:00 - 3835:00

questions super fast. WorkOS allows you

## 3835:00 - 3870:00

to build like the best with delightful

## 3870:00 - 3915:00

APIs, comprehensive docs, and a smooth

## 3915:00 - 3965:00

developer experience. Go to workos.com

## 3965:00 - 4015:00

to make your app enterprise ready today.

## 4015:00 - 4050:00

This episode is brought to you by Finn,

## 4050:00 - 4085:00

the number one AI agent for customer

## 4085:00 - 4115:00

service. If your customer support

## 4115:00 - 4145:00

tickets are piling up, then you need

## 4145:00 - 4185:00

Finn. Finn is the highest performing AI

## 4185:00 - 4230:00

agent on the market with a 65% average

## 4230:00 - 4265:00

resolution rate. Finn resolves even the

## 4265:00 - 4310:00

most complex customer queries. No other

## 4310:00 - 4340:00

AI agent performs better. In

## 4340:00 - 4365:00

head-to-head bake-offs with competitors,

## 4365:00 - 4420:00

Finn wins every time. Yes, switching to

## 4420:00 - 4455:00

a new tool can be scary, but Finn works

## 4455:00 - 4485:00

on any help desk with no migration

## 4485:00 - 4510:00

needed, which means you don't have to

## 4510:00 - 4540:00

overhaul your current system or deal

## 4540:00 - 4560:00

with delays in service for your

## 4560:00 - 4570:00

customers.

## 4570:00 - 4575:00

>> [music]

## 4575:00 - 4605:00

>> And Finn is trusted by over 6,000

## 4605:00 - 4635:00

customer service leaders and top

## 4635:00 - 4670:00

companies like Anthropic, Shutterstock,

## 4670:00 - 4700:00

Synthesia, Clay, Vanta, Lovable,

## 4700:00 - 4730:00

monday.com, and more. And because Finn

## 4730:00 - 4770:00

is powered by the Finn AI engine, which

## 4770:00 - 4800:00

is a continuously improving system that

## 4800:00 - 4830:00

allows you to analyze, train, test, and

## 4830:00 - 4870:00

deploy with ease, Finn can continuously

## 4870:00 - 4900:00

improve your results, too. So if you're

## 4900:00 - 4930:00

ready to transform your customer service

## 4930:00 - 4965:00

and scale your support, give Finn a try

## 4965:00 - 5010:00

for only 99 cents per resolution. Plus,

## 5010:00 - 5040:00

Finn comes with a 90-day money-back

## 5040:00 - 5070:00

guarantee. Find out how Finn can work

## 5070:00 - 5130:00

for your team at fin.ai/lenny.

## 5130:00 - 5230:00

That's fin.ai/lenny.

## 5230:00 - 5270:00

Alexander, thank you so much for being

## 5270:00 - 5300:00

here and welcome to the podcast. Thank

## 5300:00 - 5320:00

you so much. I've been following for

## 5320:00 - 5355:00

ages and I'm excited to be here. I'm

## 5355:00 - 5380:00

even more excited. I really appreciate

## 5380:00 - 5400:00

that.

## 5400:00 - 5430:00

I'm going to start with your time at

## 5430:00 - 5450:00

OpenAI.

## 5450:00 - 5495:00

So you joined OpenAI about a year ago.

## 5495:00 - 5520:00

Before that, you had your own startup

## 5520:00 - 5550:00

for about 5 years.

## 5550:00 - 5575:00

Before that, you were a product manager

## 5575:00 - 5600:00

at Dropbox.

## 5600:00 - 5635:00

I imagine OpenAI is very different from

## 5635:00 - 5675:00

every other place you've worked.

## 5675:00 - 5715:00

Let me just ask you this. What is most

## 5715:00 - 5750:00

different about how OpenAI operates and

## 5750:00 - 5770:00

what's something that you've learned

## 5770:00 - 5785:00

there that you think you're going to

## 5785:00 - 5810:00

take with you wherever you go, assuming

## 5810:00 - 5850:00

you ever leave? By far, I would say the

## 5850:00 - 5900:00

speed and ambition of working at OpenAI

## 5900:00 - 5925:00

are just like dramatically more than

## 5925:00 - 5965:00

what I can imagine. And you know, I

## 5965:00 - 5980:00

guess it's kind of an embarrassing thing

## 5980:00 - 6005:00

to say because you you know, everyone

## 6005:00 - 6025:00

who's a startup founder thinks like, "Oh

## 6025:00 - 6060:00

yeah, my startup moves super fast and

## 6060:00 - 6080:00

the talent bar is super high and we're

## 6080:00 - 6120:00

super ambitious." But I have to say like

## 6120:00 - 6145:00

working at OpenAI just kind of like made

## 6145:00 - 6175:00

me reimagine what it what that even

## 6175:00 - 6205:00

means. We hear this a lot about, you

## 6205:00 - 6230:00

know, feels like every AI company is

## 6230:00 - 6260:00

just like, "Oh my god, I can't believe

## 6260:00 - 6280:00

how fast they're moving."

## 6280:00 - 6305:00

Is there an example of just like, "Wow,

## 6305:00 - 6330:00

that wouldn't have happened this quickly

## 6330:00 - 6350:00

anywhere else?" The most obvious thing

## 6350:00 - 6380:00

that comes to mind is just like the the

## 6380:00 - 6435:00

explosive growth of Codex itself.

## 6435:00 - 6455:00

I think it's wild since we bumped our

## 6455:00 - 6470:00

thermal number of it, like you know,

## 6470:00 - 6515:00

it's like the the 10x thing of Codex's

## 6515:00 - 6555:00

scale was just like super fast in a

## 6555:00 - 6590:00

matter of months. And it's like well

## 6590:00 - 6610:00

more since then.

## 6610:00 - 6640:00

And you know, like once you've lived

## 6640:00 - 6660:00

through that or at least in speaking for

## 6660:00 - 6685:00

myself, like having lived through that

## 6685:00 - 6720:00

now, I feel like anytime I'm going to

## 6720:00 - 6740:00

spend

## 6740:00 - 6785:00

my time on like, you know, building tech

## 6785:00 - 6825:00

product, there's that kind of that speed

## 6825:00 - 6870:00

and scale that I now need to to to meet.

## 6870:00 - 6895:00

If I think of like what I was doing at

## 6895:00 - 6930:00

my startup, it moved like way slower.

## 6930:00 - 6950:00

And I

## 6950:00 - 6965:00

you know, there's always this balance

## 6965:00 - 7005:00

with startups of like how much do you

## 7005:00 - 7035:00

commit to an idea that you have versus

## 7035:00 - 7070:00

like find out that it's not working

## 7070:00 - 7110:00

uh and then pivot. But I think one thing

## 7110:00 - 7140:00

I've realized at OpenAI is like the the

## 7140:00 - 7165:00

amount of impact that we can have and in

## 7165:00 - 7200:00

fact need to have to do a good job is so

## 7200:00 - 7230:00

high that it is a I have to be like way

## 7230:00 - 7250:00

more ruthless with how I spend my time

## 7250:00 - 7290:00

now. Before we get to Codex, is there a

## 7290:00 - 7330:00

way that they've structured the org or I

## 7330:00 - 7355:00

don't know, the way that OpenAI operates

## 7355:00 - 7380:00

that allows the team to move this

## 7380:00 - 7405:00

quickly? Because everyone everyone wants

## 7405:00 - 7435:00

to move super fast. I imagine there's a

## 7435:00 - 7475:00

structural approach to allowing this to

## 7475:00 - 7500:00

happen. I mean, so one thing is just the

## 7500:00 - 7530:00

technology

## 7530:00 - 7555:00

that we're building with has like just

## 7555:00 - 7595:00

transformed so many things, you know,

## 7595:00 - 7625:00

from like both how we build, but also

## 7625:00 - 7665:00

like what kinds of things we can enable

## 7665:00 - 7685:00

for users.

## 7685:00 - 7720:00

And you know, we spend most of our time

## 7720:00 - 7750:00

talking about like the sort of

## 7750:00 - 7775:00

improvements in the foundation models,

## 7775:00 - 7810:00

but I I believe that even if we had no

## 7810:00 - 7835:00

more progress today with models, which

## 7835:00 - 7860:00

is absolutely not the case, but if even

## 7860:00 - 7890:00

if we had no more progress,

## 7890:00 - 7920:00

we are way behind on product. There's so

## 7920:00 - 7950:00

much more product to build. So I think

## 7950:00 - 8000:00

like just like the moment is right, if

## 8000:00 - 8030:00

that makes sense. Mhm. But I think

## 8030:00 - 8045:00

there's a lot of sort of

## 8045:00 - 8075:00

counterintuitive things that surprised

## 8075:00 - 8095:00

me when I arrived as far as like how

## 8095:00 - 8120:00

things are structured.

## 8120:00 - 8155:00

One example that comes to mind is like

## 8155:00 - 8180:00

when I was working at my startup and and

## 8180:00 - 8200:00

before that when I was at Dropbox, it

## 8200:00 - 8225:00

was like very important, you know,

## 8225:00 - 8250:00

especially as a PM to like always kind

## 8250:00 - 8270:00

of rally the ship and it was kind of

## 8270:00 - 8290:00

like make sure you're pointed in the

## 8290:00 - 8310:00

right direction and then you can like

## 8310:00 - 8350:00

accelerate in that direction.

## 8350:00 - 8400:00

But here, I think because we don't

## 8400:00 - 8435:00

exactly know like what capabilities will

## 8435:00 - 8460:00

even come up soon and we don't know

## 8460:00 - 8490:00

what's going to work

## 8490:00 - 8520:00

uh technically and then we also don't

## 8520:00 - 8540:00

know what's going to land even if it

## 8540:00 - 8570:00

works technically, it's much more

## 8570:00 - 8625:00

important for us to be very like humble

## 8625:00 - 8655:00

and learn a lot more empirically and

## 8655:00 - 8690:00

just try things quickly. And like the

## 8690:00 - 8730:00

org is is set up in that way to to be

## 8730:00 - 8765:00

incredibly bottoms up. You know, this is

## 8765:00 - 8785:00

again one of those things that like as

## 8785:00 - 8805:00

you were saying, everyone wants to move

## 8805:00 - 8830:00

fast. I think everyone likes to say that

## 8830:00 - 8845:00

they're bottoms up or at least a lot of

## 8845:00 - 8865:00

people do,

## 8865:00 - 8900:00

but OpenAI is like truly truly bottoms

## 8900:00 - 8920:00

up and that's like been a learning

## 8920:00 - 8945:00

experience for me.

## 8945:00 - 8975:00

That now like

## 8975:00 - 9000:00

it it'll be interesting if I ever work

## 9000:00 - 9015:00

at

## 9015:00 - 9035:00

I don't think that it'll ever

## 9035:00 - 9060:00

it'll even make sense to work at a

## 9060:00 - 9085:00

non-AI company in the future. I don't

## 9085:00 - 9110:00

even know what that means. But if I were

## 9110:00 - 9140:00

to imagine it or go back in time, I

## 9140:00 - 9160:00

think I would like run things totally

## 9160:00 - 9185:00

different. What I'm hearing is kind of

## 9185:00 - 9215:00

this ready

## 9215:00 - 9270:00

fire aim is the approach more than ready

## 9270:00 - 9310:00

aim fire. And there's something

## 9310:00 - 9350:00

and as you process that cuz that may not

## 9350:00 - 9375:00

come across well, but I actually have

## 9375:00 - 9405:00

heard this a lot at AI companies is

## 9405:00 - 9435:00

because you don't know and Nick Turley

## 9435:00 - 9455:00

shared I think the same sentiment.

## 9455:00 - 9480:00

Because you don't know how people will

## 9480:00 - 9510:00

use it, it doesn't make sense to spend a

## 9510:00 - 9545:00

lot of time making it perfect. It's

## 9545:00 - 9570:00

better to just get it out there in a

## 9570:00 - 9605:00

primordial way, see how people use it,

## 9605:00 - 9660:00

and then go big on that use case. Yeah.

## 9660:00 - 9685:00

It's like to to okay, to use this

## 9685:00 - 9710:00

analogy a little bit, I feel like there

## 9710:00 - 9740:00

there is an aim component, but the aim

## 9740:00 - 9765:00

component is much fuzzier. You know,

## 9765:00 - 9795:00

it's kind of like roughly

## 9795:00 - 9820:00

what do we think can happen? Like

## 9820:00 - 9855:00

someone um I've learned a ton from

## 9855:00 - 9890:00

working here is a is a research lead and

## 9890:00 - 9935:00

he likes to say that like at OpenAI,

## 9935:00 - 9960:00

we can you can have really good

## 9960:00 - 9980:00

conversations about something that's

## 9980:00 - 10015:00

like a year plus from now.

## 10015:00 - 10035:00

And you know, there's a lot of ambiguity

## 10035:00 - 10060:00

in what will happen, but but like that's

## 10060:00 - 10090:00

a right sort of timeline. And then we

## 10090:00 - 10115:00

can have really good conversations about

## 10115:00 - 10145:00

what's happening like in like low months

## 10145:00 - 10175:00

or low or weeks.

## 10175:00 - 10200:00

But there's kind of this like awkward

## 10200:00 - 10225:00

middle ground, which is like as you

## 10225:00 - 10245:00

start approaching a year, but you're not

## 10245:00 - 10280:00

at a year where it's like very difficult

## 10280:00 - 10310:00

to reason about, right? And so as far as

## 10310:00 - 10330:00

like aiming, I think we want to know

## 10330:00 - 10365:00

like, okay, what are some of the futures

## 10365:00 - 10385:00

that we're trying to build towards? And

## 10385:00 - 10410:00

like a lot of the problems we're dealing

## 10410:00 - 10435:00

with in AI like such as alignment or

## 10435:00 - 10455:00

problems you need to be thinking out

## 10455:00 - 10495:00

like really far out into the future.

## 10495:00 - 10525:00

So we're kind of aiming fuzzily there.

## 10525:00 - 10545:00

But when it comes down to the more

## 10545:00 - 10570:00

tactically like, oh yeah, like what

## 10570:00 - 10600:00

product will we build and therefore how

## 10600:00 - 10640:00

will people use that product? That's the

## 10640:00 - 10660:00

place where we're much more like, let's

## 10660:00 - 10690:00

find out empirically. That's a good way

## 10690:00 - 10710:00

of putting it.

## 10710:00 - 10735:00

Something else that when people hear

## 10735:00 - 10750:00

this,

## 10750:00 - 10765:00

they

## 10765:00 - 10795:00

people sometimes hear companies like

## 10795:00 - 10820:00

yours saying, okay, we're going to be

## 10820:00 - 10835:00

bottoms-up, we're going to try a bunch

## 10835:00 - 10860:00

of stuff, we're not going to have

## 10860:00 - 10885:00

exactly a plan of where it's going in

## 10885:00 - 10915:00

the next few months. The key is you'll

## 10915:00 - 10960:00

hire the best people in the world. And

## 10960:00 - 10985:00

so that feels like a really key

## 10985:00 - 11010:00

ingredient in order to be this

## 11010:00 - 11045:00

successful at bottoms-up work. And just

## 11045:00 - 11090:00

supervising basically. Um

## 11090:00 - 11130:00

I was just like, again, surprised or

## 11130:00 - 11155:00

even shocked when I arrived at like the

## 11155:00 - 11190:00

level of like individual like drive and

## 11190:00 - 11215:00

like

## 11215:00 - 11255:00

autonomy that everyone here has.

## 11255:00 - 11280:00

So I think like

## 11280:00 - 11315:00

the way that Open AI runs like many you

## 11315:00 - 11350:00

can't like read this or be on the listen

## 11350:00 - 11375:00

to a podcast and go like, I am I'm just

## 11375:00 - 11410:00

going to deploy this to my company.

## 11410:00 - 11440:00

Um you know, maybe this is a harsh thing

## 11440:00 - 11460:00

to say, but I think like yeah, very few

## 11460:00 - 11490:00

companies have the talent caliber to be

## 11490:00 - 11510:00

able to do that.

## 11510:00 - 11545:00

So it might need to be like

## 11545:00 - 11570:00

adjusted if you were going to implement

## 11570:00 - 11605:00

this. Okay, so let's talk Codex. You

## 11605:00 - 11650:00

lead work on Codex. How's Codex going?

## 11650:00 - 11670:00

What numbers can you share? Is there

## 11670:00 - 11700:00

anything you can share there? Also just

## 11700:00 - 11720:00

not everyone knows exactly what Codex

## 11720:00 - 11750:00

is. Explain what Codex is.

## 11750:00 - 11795:00

Totally, yeah. So I had the very lucky

## 11795:00 - 11820:00

job of of living in the future and

## 11820:00 - 11850:00

leading products on Codex.

## 11850:00 - 11885:00

Um and Codex is

## 11885:00 - 11925:00

Open AI's coding agent. So super

## 11925:00 - 11960:00

concretely that means it's an IDE

## 11960:00 - 12000:00

extension, like a VS Code extension,

## 12000:00 - 12025:00

uh that you can install or terminal tool

## 12025:00 - 12045:00

that you can install. And when you do

## 12045:00 - 12060:00

so,

## 12060:00 - 12095:00

you can then basically pair with Codex

## 12095:00 - 12120:00

to answer questions about code, write

## 12120:00 - 12140:00

code,

## 12140:00 - 12180:00

uh you know, run tests, execute code,

## 12180:00 - 12210:00

and do a bunch of the work in sort of

## 12210:00 - 12245:00

that like thick middle section of the

## 12245:00 - 12275:00

software development life cycle,

## 12275:00 - 12310:00

which is all about uh you know, writing

## 12310:00 - 12320:00

code that you're going to get into

## 12320:00 - 12340:00

production.

## 12340:00 - 12375:00

Uh more broadly,

## 12375:00 - 12410:00

we think of Codex as like it's the what

## 12410:00 - 12450:00

it currently is is just the beginning of

## 12450:00 - 12480:00

a software engineering teammate.

## 12480:00 - 12505:00

And so, you know, when we when you when

## 12505:00 - 12530:00

we use a big word like teammate, like

## 12530:00 - 12550:00

some of the things we're imagining are

## 12550:00 - 12590:00

that it's not only able to to write

## 12590:00 - 12625:00

code, but actually it participates like

## 12625:00 - 12655:00

early on in like the ideation and

## 12655:00 - 12685:00

planning phases of writing software, and

## 12685:00 - 12715:00

then further downstream in terms of like

## 12715:00 - 12740:00

validation, deploying, and like

## 12740:00 - 12770:00

maintaining code.

## 12770:00 - 12800:00

To make that a little more fun, like one

## 12800:00 - 12820:00

thing I like to imagine is like if you

## 12820:00 - 12850:00

think of what Codex is today, it's a bit

## 12850:00 - 12880:00

like this like really smart intern that

## 12880:00 - 12920:00

like refuses to read Slack, and like

## 12920:00 - 12960:00

doesn't check DataDog or like Sentry

## 12960:00 - 12990:00

unless you ask it to. And so like no

## 12990:00 - 13010:00

matter how smart it is, like how much

## 13010:00 - 13030:00

you're going to trust it to write code

## 13030:00 - 13060:00

without you also working with it, right?

## 13060:00 - 13085:00

So that's how people use it mostly today

## 13085:00 - 13105:00

is they pair with it.

## 13105:00 - 13135:00

But we want to get to the point where,

## 13135:00 - 13165:00

you know, it can work

## 13165:00 - 13185:00

like just like a new intern that you

## 13185:00 - 13205:00

hire, and you don't only ask them to

## 13205:00 - 13220:00

write code, but you ask them to

## 13220:00 - 13260:00

participate across the cycle. And so you

## 13260:00 - 13280:00

know that like even if they don't get

## 13280:00 - 13295:00

something right the first try, they're

## 13295:00 - 13315:00

eventually going to be able to iterate

## 13315:00 - 13355:00

their way there. I thought the way

## 13355:00 - 13370:00

I thought the point about not reading

## 13370:00 - 13395:00

Slack and DataDog was it's just not

## 13395:00 - 13415:00

distracted, it's just constantly

## 13415:00 - 13460:00

focused, and is always in flow. But I

## 13460:00 - 13475:00

get what you're saying there is it

## 13475:00 - 13500:00

doesn't have all the context on

## 13500:00 - 13525:00

everything that's going on.

## 13525:00 - 13550:00

And like that's not only true when it's

## 13550:00 - 13570:00

performing a task, but again, if you

## 13570:00 - 13595:00

think of like the best human teammates,

## 13595:00 - 13625:00

like you don't tell them what to do.

## 13625:00 - 13655:00

Right? Like maybe when you first hire

## 13655:00 - 13680:00

them, you have like a couple meetings

## 13680:00 - 13710:00

and you're like, hey, like you kind of

## 13710:00 - 13735:00

learn like, okay, this is this these

## 13735:00 - 13755:00

prompts work for this teammate, these

## 13755:00 - 13775:00

prompts don't, right? This is how to

## 13775:00 - 13795:00

communicate with this person. Then

## 13795:00 - 13815:00

eventually you give them some starter

## 13815:00 - 13840:00

tasks, you delegate a few tasks. But

## 13840:00 - 13860:00

then eventually you just say like, hey,

## 13860:00 - 13885:00

great, okay, you're working with this

## 13885:00 - 13920:00

set of people in this area of the code

## 13920:00 - 13930:00

base.

## 13930:00 - 13950:00

You know, feel free to work with other

## 13950:00 - 13970:00

people in other parts of the code base

## 13970:00 - 14005:00

too, even. And uh yeah, you tell me what

## 14005:00 - 14035:00

you think makes sense to be done.

## 14035:00 - 14060:00

Right? And so, you know, we think of

## 14060:00 - 14085:00

this is like proactivity, and like one

## 14085:00 - 14115:00

of our major goals with Codex is to like

## 14115:00 - 14150:00

get to proactivity.

## 14150:00 - 14175:00

I think this is

## 14175:00 - 14215:00

this is like critically important to

## 14215:00 - 14235:00

like achieve the mission of Open AI,

## 14235:00 - 14260:00

which is to deliver the benefits of AGI

## 14260:00 - 14290:00

to all humanity. You know, I like to

## 14290:00 - 14320:00

joke today that like AI products, and

## 14320:00 - 14345:00

it's it's a half joke,

## 14345:00 - 14365:00

they're actually like really hard to

## 14365:00 - 14380:00

use,

## 14380:00 - 14415:00

because you have to like be very

## 14415:00 - 14440:00

thoughtful about

## 14440:00 - 14480:00

when it could help you. And if you're

## 14480:00 - 14515:00

not prompting a model to help you, it's

## 14515:00 - 14550:00

probably not helping you at that time.

## 14550:00 - 14575:00

And if you think of how many times like

## 14575:00 - 14605:00

the average user is prompting AI today,

## 14605:00 - 14640:00

it's probably like tens of times. But if

## 14640:00 - 14665:00

you think of how many times people could

## 14665:00 - 14695:00

actually get benefit from a really

## 14695:00 - 14740:00

intelligent entity, it's thousands of

## 14740:00 - 14770:00

times per day. And so a large a large

## 14770:00 - 14795:00

part of our our goal with Codex is to

## 14795:00 - 14840:00

figure out like, what is the shape of an

## 14840:00 - 14870:00

actual teammate agent that is sort of

## 14870:00 - 14905:00

helpful by default? When people think

## 14905:00 - 14955:00

about Cursor and even Cloud Code, it's

## 14955:00 - 14990:00

like IDE that helps you code and kind of

## 14990:00 - 15025:00

auto-completes code and maybe does some

## 15025:00 - 15055:00

agentic work. What I'm hearing here is

## 15055:00 - 15090:00

the vision is is different, which is

## 15090:00 - 15125:00

it's a teammate. It's like a remote

## 15125:00 - 15140:00

teammate

## 15140:00 - 15165:00

building code for you that you talk to

## 15165:00 - 15215:00

and ask to do things. And it also does a

## 15215:00 - 15255:00

IDE auto-complete and things like that.

## 15255:00 - 15270:00

Is that is that a kind of a

## 15270:00 - 15290:00

differentiator in the way you think

## 15290:00 - 15325:00

about Codex? It's basically this idea

## 15325:00 - 15350:00

that like

## 15350:00 - 15375:00

we want the way like if you're a

## 15375:00 - 15400:00

developer and you're trying to get

## 15400:00 - 15425:00

something done, we want you to just feel

## 15425:00 - 15445:00

like you have superpowers and you're

## 15445:00 - 15490:00

able to move much, much faster. But we

## 15490:00 - 15520:00

don't think that in order for you to

## 15520:00 - 15550:00

reap those benefits,

## 15550:00 - 15575:00

you need to be sitting there constantly

## 15575:00 - 15605:00

thinking about like, how can I invoke AI

## 15605:00 - 15640:00

at this point to do this thing? We want

## 15640:00 - 15660:00

you to be able to sort of like plug it

## 15660:00 - 15690:00

in to the way that you work and have it

## 15690:00 - 15710:00

just start to do stuff without you

## 15710:00 - 15735:00

having to think about it. Okay, I have a

## 15735:00 - 15765:00

lot of questions on these lines, but

## 15765:00 - 15785:00

just how's it going? Is there any stats,

## 15785:00 - 15805:00

any numbers you can share about how

## 15805:00 - 15840:00

Codex is doing? Yeah, it's been Codex

## 15840:00 - 15855:00

has been growing like absolutely

## 15855:00 - 15880:00

explosively

## 15880:00 - 15905:00

since the launch of GPT-5 back in

## 15905:00 - 15940:00

August. Um listen, definitely some

## 15940:00 - 15965:00

interesting like product insights to

## 15965:00 - 15990:00

talk about as to like how we unlocked

## 15990:00 - 16025:00

that growth if you're interested. But

## 16025:00 - 16045:00

again, the last the last thought we

## 16045:00 - 16075:00

shared there was like we were like well

## 16075:00 - 16100:00

over 10x

## 16100:00 - 16120:00

since August. In fact, it's been like

## 16120:00 - 16145:00

20x since then.

## 16145:00 - 16180:00

Um also, the Codex models are serving

## 16180:00 - 16225:00

many many trillions of tokens a week

## 16225:00 - 16255:00

now, and it's basically like our most

## 16255:00 - 16290:00

served coding model. Um one of the

## 16290:00 - 16310:00

really cool things that we've seen is

## 16310:00 - 16325:00

that

## 16325:00 - 16350:00

the way that we decided to set up the

## 16350:00 - 16365:00

Codex team

## 16365:00 - 16395:00

uh was to build a you know, a really

## 16395:00 - 16420:00

tightly integrated

## 16420:00 - 16450:00

product and research team that are

## 16450:00 - 16470:00

iterating on the model and the harness

## 16470:00 - 16495:00

together.

## 16495:00 - 16520:00

And it turns out that lets you just do a

## 16520:00 - 16550:00

lot more and try many more experiments

## 16550:00 - 16565:00

as to how these things will work

## 16565:00 - 16585:00

together.

## 16585:00 - 16620:00

And so, we were just training these

## 16620:00 - 16650:00

models for use in our first-party

## 16650:00 - 16675:00

harness that we were very opinionated

## 16675:00 - 16705:00

about.

## 16705:00 - 16720:00

And then what we've started to see more

## 16720:00 - 16770:00

recently actually is that other major

## 16770:00 - 16795:00

sort of API coding customers are now

## 16795:00 - 16835:00

starting to adopt these models as well.

## 16835:00 - 16850:00

And so we've reached a point where

## 16850:00 - 16880:00

actually the Codex model is the most

## 16880:00 - 16930:00

served coding model in the API as well.

## 16930:00 - 16975:00

You uh hinted at this

## 16975:00 - 17000:00

what unlocked this growth. I am

## 17000:00 - 17030:00

extremely interested in hearing that. It

## 17030:00 - 17060:00

felt like before, I don't know, maybe

## 17060:00 - 17080:00

this was before you joined the team. It

## 17080:00 - 17105:00

just felt like Cloud Code was killing

## 17105:00 - 17135:00

it. Just everyone was sitting on top of

## 17135:00 - 17175:00

Cloud Code. It was by far the best way

## 17175:00 - 17200:00

to code. And then all of a sudden Codex

## 17200:00 - 17235:00

comes around. I remember Karpathy

## 17235:00 - 17285:00

tweeted that he just like has never seen

## 17285:00 - 17305:00

a model like this.

## 17305:00 - 17345:00

I think the tweet was the gnarlies bugs

## 17345:00 - 17375:00

that he runs into that he just spends

## 17375:00 - 17405:00

hours trying to figure out, nothing else

## 17405:00 - 17435:00

has solved. He gives it to Codex, lets

## 17435:00 - 17475:00

it run for an hour, and it solves it.

## 17475:00 - 17510:00

What did what did you guys do? We have

## 17510:00 - 17545:00

the strong sort of mission here at Open

## 17545:00 - 17590:00

AI to, you know, basically to build AGI.

## 17590:00 - 17650:00

Um and so we we think a lot about what

## 17650:00 - 17680:00

how can we shape the product so that it

## 17680:00 - 17705:00

can scale?

## 17705:00 - 17720:00

Right? You know, earlier I was

## 17720:00 - 17740:00

mentioning like, hey, like if you're an

## 17740:00 - 17760:00

engineer, you should be getting help

## 17760:00 - 17790:00

from an from AI like thousands of times

## 17790:00 - 17825:00

per day, right? And so

## 17825:00 - 17850:00

we thought a lot about the primitives

## 17850:00 - 17880:00

for that when we launched our first

## 17880:00 - 17905:00

version of Codex,

## 17905:00 - 17935:00

uh which was Codex Cloud.

## 17935:00 - 17955:00

And that was basically a product that

## 17955:00 - 17975:00

had its own computer, lived in the

## 17975:00 - 18005:00

cloud, you could delegate to it.

## 18005:00 - 18040:00

And you know, the sort of the coolest

## 18040:00 - 18060:00

part about that was you could run many,

## 18060:00 - 18095:00

many tasks in parallel.

## 18095:00 - 18135:00

But some of the challenges that we saw

## 18135:00 - 18190:00

are that it's a little bit harder to set

## 18190:00 - 18215:00

that up both in terms of like

## 18215:00 - 18235:00

environment configuration, like giving

## 18235:00 - 18275:00

the model the tools it needs to validate

## 18275:00 - 18305:00

its changes, and to learn how to prompt

## 18305:00 - 18350:00

in that way. And sort of my my analogy

## 18350:00 - 18370:00

for this is going back to this teammate

## 18370:00 - 18385:00

analogy. It's like if you hired a

## 18385:00 - 18430:00

teammate, but you're never allowed to

## 18430:00 - 18455:00

get on a call with them, and you can

## 18455:00 - 18480:00

only go back and forth, you know,

## 18480:00 - 18505:00

asynchronously

## 18505:00 - 18525:00

over time. Like that works for some

## 18525:00 - 18545:00

teammates.

## 18545:00 - 18565:00

And eventually that's actually how you

## 18565:00 - 18585:00

want to spend most of your time, so

## 18585:00 - 18615:00

that's still the future. But it's hard

## 18615:00 - 18645:00

to initially adopt.

## 18645:00 - 18675:00

And so we still have that vision of like

## 18675:00 - 18695:00

that's what we're trying to get you to,

## 18695:00 - 18720:00

a teammate that you delegate to and then

## 18720:00 - 18750:00

is proactive. And we're seeing that

## 18750:00 - 18780:00

growing, but

## 18780:00 - 18805:00

the key unlock is actually first you

## 18805:00 - 18835:00

need to land with users in a way that's

## 18835:00 - 18865:00

like much more intuitive and like

## 18865:00 - 18900:00

trivial to get value from.

## 18900:00 - 18940:00

So the way that most people discover

## 18940:00 - 18965:00

like the vast majority of users discover

## 18965:00 - 19000:00

Codex today is either they download an

## 19000:00 - 19035:00

IDE extension, or they run it in their

## 19035:00 - 19085:00

CLI, and the agent works there with you

## 19085:00 - 19120:00

on your computer interactively.

## 19120:00 - 19150:00

And uh it works within a sandbox, which

## 19150:00 - 19165:00

is actually like a really cool piece of

## 19165:00 - 19215:00

tech to to help that be safe and secure.

## 19215:00 - 19240:00

But it has access to all those

## 19240:00 - 19265:00

dependencies.

## 19265:00 - 19290:00

So if the agent needs to do something,

## 19290:00 - 19310:00

like it needs to run a command, it can

## 19310:00 - 19330:00

do so within the sandbox, we don't have

## 19330:00 - 19360:00

to set up any environment. And if it's a

## 19360:00 - 19380:00

command that doesn't work in the

## 19380:00 - 19415:00

sandbox, it can just ask you. And so you

## 19415:00 - 19440:00

can get into this like really strong

## 19440:00 - 19470:00

feedback loop using the model. And then

## 19470:00 - 19505:00

over time like our team's job is to like

## 19505:00 - 19520:00

help

## 19520:00 - 19565:00

turn that feedback loop into you sort of

## 19565:00 - 19595:00

as a byproduct of using the product

## 19595:00 - 19615:00

configuring it so that you can then be

## 19615:00 - 19645:00

delegating to it down the line. And

## 19645:00 - 19670:00

again, analogy,

## 19670:00 - 19685:00

you know, keep going back to it, but

## 19685:00 - 19715:00

like if you hire a teammate and you ask

## 19715:00 - 19735:00

them to do work, but they you just give

## 19735:00 - 19760:00

them like a fresh computer from the

## 19760:00 - 19780:00

store,

## 19780:00 - 19795:00

it's going to be hard for them to do

## 19795:00 - 19820:00

their job, right? But if as you work

## 19820:00 - 19845:00

with them side by side, you could be

## 19845:00 - 19870:00

like, oh, you don't have a password for

## 19870:00 - 19895:00

this service we use. Here's the password

## 19895:00 - 19930:00

for this service. You know, yeah, don't

## 19930:00 - 19960:00

worry. Feel free to run this command."

## 19960:00 - 19985:00

Then it's like much easier for them to

## 19985:00 - 20010:00

then go off and do work for hours

## 20010:00 - 20045:00

without you. So, what I'm hearing is the

## 20045:00 - 20070:00

initial version of Codex was almost too

## 20070:00 - 20105:00

far in the future. It's like a remote in

## 20105:00 - 20150:00

the cloud uh agent that's coding for you

## 20150:00 - 20195:00

asynchronously. And what you did is,

## 20195:00 - 20220:00

okay, let's actually come back a little

## 20220:00 - 20245:00

bit. Let's integrate into the way

## 20245:00 - 20280:00

engineers already integrate into IDEs

## 20280:00 - 20300:00

and locally

## 20300:00 - 20330:00

and help them kind of on-ramp to this

## 20330:00 - 20380:00

new world. Totally. And this is it was

## 20380:00 - 20415:00

quite interesting because

## 20415:00 - 20470:00

we we dogfood product a ton at OpenAI.

## 20470:00 - 20500:00

So, you know, dogfood we as in we use

## 20500:00 - 20530:00

our own product. And so, Codex has been

## 20530:00 - 20560:00

accelerating OpenAI

## 20560:00 - 20585:00

over the course of the entire year and

## 20585:00 - 20620:00

the cloud product was a massive

## 20620:00 - 20660:00

accelerator to the company as well.

## 20660:00 - 20675:00

Um

## 20675:00 - 20710:00

it just turns out that this is one of

## 20710:00 - 20740:00

those places where the signal we got

## 20740:00 - 20765:00

from dogfooding is a little bit

## 20765:00 - 20790:00

different from the signal you get from

## 20790:00 - 20810:00

like the general market because at

## 20810:00 - 20840:00

OpenAI, you know, we train reasoning

## 20840:00 - 20870:00

models all day and so, we're very used

## 20870:00 - 20905:00

to this kind of prompting and like, you

## 20905:00 - 20925:00

know, think up front, run things

## 20925:00 - 20960:00

massively in parallel.

## 20960:00 - 20995:00

And uh you know, it will take some time

## 20995:00 - 21010:00

and then come back to it later

## 21010:00 - 21055:00

asynchronously. And so, you know, now

## 21055:00 - 21080:00

when we build, we still get a a ton of

## 21080:00 - 21130:00

signal from dogfooding internally, but

## 21130:00 - 21165:00

uh you know, we're also very cognizant

## 21165:00 - 21185:00

of like the different ways that

## 21185:00 - 21210:00

different audiences use the product.

## 21210:00 - 21240:00

>> That's really funny. It's like live in

## 21240:00 - 21265:00

the future, but maybe not too far in the

## 21265:00 - 21300:00

future. And I could see how everyone at

## 21300:00 - 21335:00

OpenAI is living very far in the future

## 21335:00 - 21365:00

and sometimes that won't that won't work

## 21365:00 - 21390:00

for everyone. Yeah.

## 21390:00 - 21430:00

What about just like uh intelligence,

## 21430:00 - 21450:00

training data? I don't know. Is there

## 21450:00 - 21485:00

something else that helped Codex

## 21485:00 - 21525:00

accelerate its ability to actually code?

## 21525:00 - 21570:00

Is it like better, cleaner data? Is it

## 21570:00 - 21600:00

more just models advancing? Is there

## 21600:00 - 21615:00

anything else that really helped it

## 21615:00 - 21650:00

accelerate? Yeah, so there's like a few

## 21650:00 - 21685:00

components here. Um

## 21685:00 - 21710:00

I guess, you know, you were mentioning

## 21710:00 - 21730:00

models and the models have improved a

## 21730:00 - 21785:00

ton. In fact, um just last Wednesday, we

## 21785:00 - 21825:00

shipped GPT-5.1 Codex Max.

## 21825:00 - 21860:00

A very, you know, accurately named

## 21860:00 - 21885:00

model. Uh

## 21885:00 - 21920:00

that is that is awesome. It is awesome

## 21920:00 - 21970:00

both because it is um for any given task

## 21970:00 - 22015:00

that you were using GPT-5.1 Codex for,

## 22015:00 - 22060:00

it's like, you know, roughly uh 30%

## 22060:00 - 22095:00

faster at accomplishing that task.

## 22095:00 - 22115:00

But also, it unlocks a ton of

## 22115:00 - 22145:00

intelligence. So, if you use it at our

## 22145:00 - 22170:00

higher reasoning levels, it's just like

## 22170:00 - 22210:00

even smarter. Um and you know, that that

## 22210:00 - 22235:00

feedback that or that tweet you were

## 22235:00 - 22260:00

saying like Karpathy made about like,

## 22260:00 - 22295:00

"Hey, give this your gnarly bugs." like,

## 22295:00 - 22310:00

you know, obviously there's a a ton

## 22310:00 - 22335:00

going on in the market right now, but

## 22335:00 - 22365:00

like Codex Max is definitely like

## 22365:00 - 22400:00

carrying that mantle of uh you know,

## 22400:00 - 22435:00

tackling the hardest bugs. Um so, that

## 22435:00 - 22450:00

is

## 22450:00 - 22475:00

that is super cool. But, I will say it's

## 22475:00 - 22495:00

like

## 22495:00 - 22530:00

some of what how we're thinking about

## 22530:00 - 22550:00

this is evolving a little bit from being

## 22550:00 - 22565:00

like, "Yeah, we're just going to think

## 22565:00 - 22590:00

about the model and like let's just like

## 22590:00 - 22615:00

train the best model." to really

## 22615:00 - 22650:00

thinking about like what is an agent

## 22650:00 - 22680:00

actually overall.

## 22680:00 - 22700:00

Right?

## 22700:00 - 22725:00

And you know, I'm not going to try to

## 22725:00 - 22750:00

define agent exactly, but at least the

## 22750:00 - 22770:00

stack that we think of it as having is

## 22770:00 - 22805:00

just like you have this model,

## 22805:00 - 22835:00

really smart reasoning model,

## 22835:00 - 22855:00

that knows how to do a specific kind of

## 22855:00 - 22875:00

task really well, so we can talk about

## 22875:00 - 22905:00

how we make that possible. But then

## 22905:00 - 22955:00

actually, we need to serve that model

## 22955:00 - 23005:00

through an API into a harness and both

## 23005:00 - 23035:00

of those things also have a really big

## 23035:00 - 23065:00

role here. So, for instance,

## 23065:00 - 23095:00

one of the things

## 23095:00 - 23110:00

that we're really proud of is you can

## 23110:00 - 23145:00

have GPT-5.1 Codex Max work for really

## 23145:00 - 23180:00

long periods of time. That's not like

## 23180:00 - 23210:00

normal, but you can set it up to do that

## 23210:00 - 23240:00

or that might happen. But now routinely

## 23240:00 - 23260:00

we'll hear about people saying like,

## 23260:00 - 23290:00

"Yeah, it ran like overnight." or it ran

## 23290:00 - 23330:00

for 24 hours. And so, you know, for a

## 23330:00 - 23355:00

model to work continuously for that

## 23355:00 - 23380:00

amount of time, it's going to exceed its

## 23380:00 - 23410:00

context window. And so, we have a

## 23410:00 - 23430:00

solution for that which we call

## 23430:00 - 23450:00

compaction.

## 23450:00 - 23465:00

Um

## 23465:00 - 23495:00

that compaction is actually a feature

## 23495:00 - 23520:00

that uses like all three layers of that

## 23520:00 - 23550:00

stack. So,

## 23550:00 - 23595:00

you need to have a model that has a

## 23595:00 - 23620:00

concept of compaction and knows like,

## 23620:00 - 23640:00

"Okay, as I start to approach its

## 23640:00 - 23670:00

context window, I might be asked to like

## 23670:00 - 23700:00

prepare to be run in a new context

## 23700:00 - 23740:00

window." And then at the API layer, you

## 23740:00 - 23770:00

need an API that like understands this

## 23770:00 - 23790:00

concept and like has an endpoint that

## 23790:00 - 23820:00

you can hit to do this change. And at

## 23820:00 - 23840:00

the harness layer, you need a harness

## 23840:00 - 23860:00

that can like prepare the payload for

## 23860:00 - 23900:00

this to be done. And so, like shipping

## 23900:00 - 23920:00

this compaction feature that now just

## 23920:00 - 23945:00

like made this behavior possible to like

## 23945:00 - 23975:00

anyone using Codex, actually meant

## 23975:00 - 24000:00

working across all three things and I

## 24000:00 - 24020:00

think that's like increasingly going to

## 24020:00 - 24075:00

be true. Another maybe like

## 24075:00 - 24110:00

under-appreciated version of this is is

## 24110:00 - 24135:00

if you think about all the different

## 24135:00 - 24160:00

coding products out there, they all have

## 24160:00 - 24190:00

like very different tool harnesses with

## 24190:00 - 24210:00

like very different opinions on how the

## 24210:00 - 24240:00

model should work.

## 24240:00 - 24260:00

And so, if you want to train a model to

## 24260:00 - 24290:00

be good at like all the different ways

## 24290:00 - 24320:00

uh it could work, like, you know, maybe

## 24320:00 - 24345:00

you have a strong opinion that it should

## 24345:00 - 24380:00

work using semantic search. Right? Maybe

## 24380:00 - 24400:00

you have a strong opinion that it should

## 24400:00 - 24435:00

like call the spoke tools. Or maybe you

## 24435:00 - 24455:00

have like in our case a strong opinion

## 24455:00 - 24495:00

that it should just use like the shell,

## 24495:00 - 24525:00

work in the terminal.

## 24525:00 - 24545:00

You know, you can be much you can move

## 24545:00 - 24565:00

much faster if you're just optimizing

## 24565:00 - 24610:00

for one of those worlds. Right? And so,

## 24610:00 - 24630:00

the way that we built Codex is that it

## 24630:00 - 24655:00

just uses the shell, but in order to

## 24655:00 - 24705:00

make that like safer and secure, we have

## 24705:00 - 24730:00

a sandbox that the model is used to

## 24730:00 - 24755:00

operating in.

## 24755:00 - 24775:00

So, I think one of the biggest

## 24775:00 - 24795:00

accelerators to go all the way back to

## 24795:00 - 24815:00

your to your answer question is just

## 24815:00 - 24845:00

like we're building all three things in

## 24845:00 - 24880:00

parallel and like kind of tuning each

## 24880:00 - 24915:00

one and um you know, constantly

## 24915:00 - 24945:00

experimenting with how those things work

## 24945:00 - 24970:00

with like a tightly integrated product

## 24970:00 - 24990:00

and research team.

## 24990:00 - 25040:00

How do you think you win in this space?

## 25040:00 - 25075:00

Do you think it it'll even it'll always

## 25075:00 - 25105:00

be this kind of like race with other

## 25105:00 - 25135:00

models constantly kind of leapfrogging

## 25135:00 - 25160:00

each other? Do you think there's a world

## 25160:00 - 25195:00

where someone just runs away with it and

## 25195:00 - 25215:00

no one else can ever catch up? Is there

## 25215:00 - 25255:00

like a path to just we win? Again, comes

## 25255:00 - 25280:00

back to this idea of like building a

## 25280:00 - 25300:00

teammate.

## 25300:00 - 25315:00

And

## 25315:00 - 25365:00

not just a teammate that, you know, uh

## 25365:00 - 25385:00

participates in team planning and

## 25385:00 - 25410:00

prioritization. Not just a teammate

## 25410:00 - 25425:00

that,

## 25425:00 - 25450:00

you know, really tests its code and like

## 25450:00 - 25480:00

helps you maintain and deploy it.

## 25480:00 - 25500:00

But even a teammate, you know, like if

## 25500:00 - 25520:00

you think again, an engineering

## 25520:00 - 25545:00

teammate, they can also like schedule a

## 25545:00 - 25590:00

calendar invite, right? Or move standup.

## 25590:00 - 25630:00

Or do whatever, right? And so,

## 25630:00 - 25660:00

in my mind,

## 25660:00 - 25700:00

if we just imagine that

## 25700:00 - 25740:00

every day or every week some like crazy

## 25740:00 - 25760:00

new capability is just going to be

## 25760:00 - 25795:00

deployed by a research lab, it's just

## 25795:00 - 25820:00

impossible for us like, you know, as

## 25820:00 - 25850:00

humans to keep up and like use all this

## 25850:00 - 25890:00

technology. And so, I think we need to

## 25890:00 - 25920:00

get to this world where

## 25920:00 - 25955:00

you kind of just have like

## 25955:00 - 25985:00

an AI teammate or a super assistant that

## 25985:00 - 26030:00

you just talk to and it just knows how

## 26030:00 - 26070:00

to be helpful like on its own.

## 26070:00 - 26085:00

Right? And so, you don't you don't have

## 26085:00 - 26120:00

to be like reading the latest tips for

## 26120:00 - 26140:00

how to use it and you just like you plug

## 26140:00 - 26175:00

it in and it just provides help.

## 26175:00 - 26210:00

And so, that's kind of the shape of what

## 26210:00 - 26230:00

I think we're building and I think that

## 26230:00 - 26260:00

will be like a very sticky like winning

## 26260:00 - 26290:00

product if we can do so. So, the shape

## 26290:00 - 26315:00

that I'm in my head at least I have is

## 26315:00 - 26365:00

that we build, you know, maybe a fun

## 26365:00 - 26385:00

topic is like is chat the right

## 26385:00 - 26420:00

interface for AI? I think chat is a very

## 26420:00 - 26445:00

good interface

## 26445:00 - 26470:00

when you don't know what you're supposed

## 26470:00 - 26490:00

to use it for.

## 26490:00 - 26515:00

Uh in the same way that if I think of

## 26515:00 - 26545:00

like I'm like on a Teams or in Slack

## 26545:00 - 26575:00

with a teammate, chat is pretty good. I

## 26575:00 - 26600:00

can ask for whatever I want, right? It's

## 26600:00 - 26630:00

like kind of the common denominator for

## 26630:00 - 26660:00

everything. So, you can chat with a

## 26660:00 - 26695:00

super assistant about whatever topic you

## 26695:00 - 26730:00

want, whether it be coding or not.

## 26730:00 - 26750:00

And then if

## 26750:00 - 26780:00

you are like a functional expert in a

## 26780:00 - 26810:00

specific domain such as coding, there's

## 26810:00 - 26830:00

like a GUI

## 26830:00 - 26875:00

that you can pull up to go really deep

## 26875:00 - 26900:00

and like look at the code and like work

## 26900:00 - 26935:00

with the code. So, I think like what we

## 26935:00 - 26980:00

need to build as OpenAI is basically

## 26980:00 - 27005:00

this idea of like you have chat,

## 27005:00 - 27040:00

ChatGPT, and that is a tool that's like

## 27040:00 - 27070:00

ubiquitously available to like everyone.

## 27070:00 - 27100:00

You start using it even like outside of

## 27100:00 - 27135:00

work, right? To just help you. You

## 27135:00 - 27155:00

become very comfortable with the idea of

## 27155:00 - 27190:00

being accelerated with AI. And so, then

## 27190:00 - 27210:00

you get to work and you just can

## 27210:00 - 27235:00

naturally just, yeah, I'm just going to

## 27235:00 - 27265:00

ask it for this and I don't need to know

## 27265:00 - 27290:00

about all the connectors or like all the

## 27290:00 - 27315:00

different features. I'm just going to

## 27315:00 - 27350:00

ask it for help and it'll surface to me

## 27350:00 - 27375:00

the the best way that it can help at

## 27375:00 - 27400:00

this point in time. And maybe even chime

## 27400:00 - 27435:00

in when I didn't ask it for help.

## 27435:00 - 27465:00

Um so, in my mind if we can get to that,

## 27465:00 - 27500:00

I think that's, you know, that's how we

## 27500:00 - 27520:00

we really build like the winning

## 27520:00 - 27560:00

product. This is so interesting because

## 27560:00 - 27585:00

at with the my chat with Nick Charney,

## 27585:00 - 27620:00

the head of ChatGPT, I think he shared

## 27620:00 - 27655:00

that the original name for ChatGPT was

## 27655:00 - 27685:00

super assistant or something like that.

## 27685:00 - 27725:00

Yeah. And it's interesting that there's

## 27725:00 - 27760:00

like that approach to the super

## 27760:00 - 27780:00

assistant and then there's this Codex

## 27780:00 - 27810:00

approach. It's almost like the B2C

## 27810:00 - 27845:00

version and the B2B version.

## 27845:00 - 27870:00

And what I'm hearing is the idea here

## 27870:00 - 27890:00

is, okay, you start with coding and

## 27890:00 - 27920:00

building and then it's doing all this

## 27920:00 - 27935:00

other stuff for you, scheduling

## 27935:00 - 27965:00

meetings, I don't know, probably posting

## 27965:00 - 28015:00

in Slack. Uh I don't know, shipping

## 28015:00 - 28040:00

designs. I don't know. Is that Is the

## 28040:00 - 28075:00

idea there this is like the the business

## 28075:00 - 28105:00

version of ChatGPT in a sense or is

## 28105:00 - 28130:00

there or or is there something else

## 28130:00 - 28145:00

there?

## 28145:00 - 28165:00

Yeah, so you know, so we're getting to

## 28165:00 - 28185:00

the like

## 28185:00 - 28205:00

the like one-year time horizon

## 28205:00 - 28240:00

conversation. A lot of this might happen

## 28240:00 - 28265:00

sooner, but in terms of fuzziness, I

## 28265:00 - 28280:00

think we're at the one-year. So, I'll

## 28280:00 - 28305:00

give you like

## 28305:00 - 28330:00

a contention and like a plausible way to

## 28330:00 - 28355:00

get there, but as for how it happens,

## 28355:00 - 28395:00

who knows. So, basically,

## 28395:00 - 28410:00

if we're going to build a super

## 28410:00 - 28425:00

assistant, it has to be able to do

## 28425:00 - 28445:00

things,

## 28445:00 - 28470:00

right? So, like we're going to have a

## 28470:00 - 28485:00

model and it's going to be able to do

## 28485:00 - 28530:00

stuff affecting your world.

## 28530:00 - 28550:00

And one of the learnings I think we've

## 28550:00 - 28605:00

seen over the past year or so is that

## 28605:00 - 28630:00

for models to do stuff, they're much

## 28630:00 - 28650:00

more effective when they can use a

## 28650:00 - 28690:00

computer.

## 28690:00 - 28725:00

Right? Okay. So, now we're like, "Okay,

## 28725:00 - 28745:00

we need the super assistant that can use

## 28745:00 - 28785:00

a computer." Right? Or many computers.

## 28785:00 - 28805:00

And now the question is, okay, well, how

## 28805:00 - 28835:00

should it use the computer?

## 28835:00 - 28860:00

Right? And there's lots of ways to use a

## 28860:00 - 28890:00

computer. Uh you know, you could try to

## 28890:00 - 28920:00

hack the OS and like use accessibility

## 28920:00 - 28950:00

APIs. Maybe a bit easier is you could

## 28950:00 - 28975:00

point and click.

## 28975:00 - 29010:00

That's a little slow, you know, and

## 29010:00 - 29035:00

unpredictable sometimes.

## 29035:00 - 29070:00

Um and another way, it turns out the

## 29070:00 - 29095:00

best way for models to use computers is

## 29095:00 - 29125:00

simply to write code.

## 29125:00 - 29145:00

Right? And so, we're kind of getting to

## 29145:00 - 29170:00

this idea where like, "Well, if you want

## 29170:00 - 29195:00

to build any agent, maybe you should be

## 29195:00 - 29245:00

building a coding agent." And maybe

## 29245:00 - 29270:00

to the user, a non-technical user, they

## 29270:00 - 29290:00

won't even know they're using a coding

## 29290:00 - 29315:00

agent the same way that no one thinks

## 29315:00 - 29335:00

about are they using the internet or

## 29335:00 - 29350:00

not. It's just they're more just like,

## 29350:00 - 29370:00

"Is Wi-Fi on?"

## 29370:00 - 29400:00

Right? So,

## 29400:00 - 29430:00

I think that what we're doing with Codex

## 29430:00 - 29460:00

is we're building a software engineering

## 29460:00 - 29495:00

teammate and as part of that, we're kind

## 29495:00 - 29535:00

of building an agent that can use uh a

## 29535:00 - 29580:00

computer by writing code. And so, we're

## 29580:00 - 29615:00

already seeing like some pull for this.

## 29615:00 - 29635:00

It's like quite early, but we're

## 29635:00 - 29655:00

starting to see people like who are

## 29655:00 - 29695:00

using Codex for like coding-adjacent

## 29695:00 - 29730:00

product purposes.

## 29730:00 - 29765:00

And so, as that develops, I think we'll

## 29765:00 - 29790:00

just naturally see that like, "Oh, it

## 29790:00 - 29810:00

turns out like we should just always

## 29810:00 - 29835:00

have the agent write code if there is a

## 29835:00 - 29870:00

coding way to solve a problem instead of

## 29870:00 - 29885:00

you know, even if you're doing in

## 29885:00 - 29910:00

financial analysis, right? Like maybe

## 29910:00 - 29930:00

write some code for that. So basically

## 29930:00 - 29950:00

like you know, you were like, hey, is

## 29950:00 - 29985:00

this like the two ends of of

## 29985:00 - 30010:00

of this product for the super assistant,

## 30010:00 - 30045:00

right? Of ChatGPT. In my mind like just

## 30045:00 - 30080:00

coding is a core competency of any agent

## 30080:00 - 30110:00

including ChatGPT. And so like what

## 30110:00 - 30135:00

really what we think we're building is

## 30135:00 - 30175:00

like that competency. But so here's

## 30175:00 - 30195:00

here's like the really cool thing about

## 30195:00 - 30220:00

agents writing code is that you can

## 30220:00 - 30250:00

import code.

## 30250:00 - 30285:00

Right? Code is like composable.

## 30285:00 - 30305:00

Interoperable.

## 30305:00 - 30350:00

Right? Cuz if if we you know, one very

## 30350:00 - 30380:00

reductive view we could have for an

## 30380:00 - 30400:00

agent is it's just going to be given a

## 30400:00 - 30425:00

computer and it's just going to like

## 30425:00 - 30455:00

point and click and and you know,

## 30455:00 - 30490:00

go around. But

## 30490:00 - 30515:00

you know, that is the future and then

## 30515:00 - 30560:00

how we get there is difficult to sort of

## 30560:00 - 30590:00

chart a path because a lot of the

## 30590:00 - 30620:00

questions around building agents aren't

## 30620:00 - 30650:00

like can the agent do it, but it's more

## 30650:00 - 30680:00

about well,

## 30680:00 - 30710:00

how can we help the agent understand the

## 30710:00 - 30735:00

context that it's working in and like

## 30735:00 - 30760:00

the team that's using it, you know,

## 30760:00 - 30785:00

probably has a way that they like to do

## 30785:00 - 30815:00

things. They have guidelines. They

## 30815:00 - 30840:00

probably want certain deterministic

## 30840:00 - 30870:00

guarantees about what the agent can or

## 30870:00 - 30895:00

cannot do.

## 30895:00 - 30910:00

Or they want to know that the agent

## 30910:00 - 30955:00

understands sort of this detail. Like an

## 30955:00 - 30980:00

example would be,

## 30980:00 - 31015:00

you know, if we're looking at a crash

## 31015:00 - 31050:00

reporting tool hitting a connector for

## 31050:00 - 31065:00

it,

## 31065:00 - 31090:00

every sub-team is probably has a

## 31090:00 - 31120:00

different meta prompt for like how they

## 31120:00 - 31165:00

want the crashes to be analyzed.

## 31165:00 - 31195:00

Right? And so we start to get to this

## 31195:00 - 31210:00

thing where like, yeah, we have this

## 31210:00 - 31230:00

agent sitting in front of a computer,

## 31230:00 - 31265:00

but we need to make that configurable

## 31265:00 - 31300:00

for the team or for the user, right? And

## 31300:00 - 31320:00

let them like

## 31320:00 - 31345:00

stuff that the agent does often, we

## 31345:00 - 31375:00

probably just want to like build in as a

## 31375:00 - 31400:00

competency that this agent has that it

## 31400:00 - 31430:00

can do. So

## 31430:00 - 31450:00

I think

## 31450:00 - 31475:00

we end up with this generalizable thing

## 31475:00 - 31505:00

that you were saying of like an agent

## 31505:00 - 31530:00

that can just write its own scripts for

## 31530:00 - 31555:00

whatever it wants to do.

## 31555:00 - 31610:00

But I think that the the really key part

## 31610:00 - 31650:00

here is can we make it so that

## 31650:00 - 31670:00

everything that the agent has to do

## 31670:00 - 31700:00

often or that it does well, we can just

## 31700:00 - 31735:00

like remember and store

## 31735:00 - 31755:00

so that the agent doesn't have to write

## 31755:00 - 31785:00

a script for that again, right? Or maybe

## 31785:00 - 31810:00

like if I just joined a team and you are

## 31810:00 - 31840:00

already on the same team as me,

## 31840:00 - 31865:00

I can just like use all those scripts

## 31865:00 - 31890:00

that the agents have written already.

## 31890:00 - 31930:00

Yeah, it's like if this is our teammate,

## 31930:00 - 31965:00

we can they can share things that it's

## 31965:00 - 31980:00

learned from working with other people

## 31980:00 - 32010:00

at the company. Just makes sense as a

## 32010:00 - 32025:00

metaphor.

## 32025:00 - 32060:00

Yeah. It feels like you're in the

## 32060:00 - 32095:00

Karpathy camp of agents today are not

## 32095:00 - 32130:00

that great and mostly slop and maybe in

## 32130:00 - 32160:00

the future they'll be awesome. Does that

## 32160:00 - 32180:00

resonate?

## 32180:00 - 32205:00

I think so I think coding agents are

## 32205:00 - 32230:00

pretty great. I think

## 32230:00 - 32265:00

Uh that's right. Yeah.

## 32265:00 - 32305:00

>> Yep. And then I think like agent side

## 32305:00 - 32340:00

outside of coding, it's still like very

## 32340:00 - 32355:00

early.

## 32355:00 - 32380:00

And you know, this is just my opinion,

## 32380:00 - 32395:00

but I think they're going to get a whole

## 32395:00 - 32425:00

lot better once they can use coding to

## 32425:00 - 32470:00

and like in a composable way. Mhm.

## 32470:00 - 32490:00

This is it's kind of the fun part of

## 32490:00 - 32510:00

like when you're building for software

## 32510:00 - 32535:00

engineers. Like I

## 32535:00 - 32555:00

in my setup we were building for

## 32555:00 - 32580:00

software engineers too for a lot of that

## 32580:00 - 32610:00

journey and they're just such a fun

## 32610:00 - 32655:00

audience to build for because

## 32655:00 - 32680:00

you know, they also like building for

## 32680:00 - 32720:00

themselves and are often like even more

## 32720:00 - 32745:00

creative than we are in thinking about

## 32745:00 - 32775:00

how to use the technology.

## 32775:00 - 32805:00

Um and so like by building for software

## 32805:00 - 32830:00

engineers, you get to just observe a ton

## 32830:00 - 32860:00

of emergent behaviors and like

## 32860:00 - 32880:00

things that you should do and build into

## 32880:00 - 32895:00

the product.

## 32895:00 - 32925:00

I love how you you say that cuz a lot of

## 32925:00 - 32950:00

people building for engineers get really

## 32950:00 - 32985:00

annoyed cuz the engineers are so they're

## 32985:00 - 33005:00

just always complaining about stuff.

## 33005:00 - 33025:00

They're like, ah, this sucks. Why did

## 33025:00 - 33050:00

you build it this way?

## 33050:00 - 33075:00

I love that you enjoy it, but I think

## 33075:00 - 33095:00

it's probably because you're building

## 33095:00 - 33130:00

such an amazing tool for engineers that

## 33130:00 - 33160:00

can actually solve problems

## 33160:00 - 33200:00

and just you know, code for them.

## 33200:00 - 33220:00

Um kind of along those lines, you know,

## 33220:00 - 33250:00

there's always this talk of

## 33250:00 - 33285:00

what will happen to jobs, coding, do you

## 33285:00 - 33320:00

have to learn coding, all these things?

## 33320:00 - 33340:00

Clearly the way you're describing it is

## 33340:00 - 33365:00

it's a teammate. It's going to work with

## 33365:00 - 33395:00

you making more superhuman. It's not

## 33395:00 - 33420:00

going to replace you. What's the way you

## 33420:00 - 33460:00

just think about the impact on the field

## 33460:00 - 33500:00

of engineering having this super

## 33500:00 - 33545:00

intelligent engineering teammate? I

## 33545:00 - 33570:00

think there's there's two sides to it,

## 33570:00 - 33605:00

but the one we were just talking about

## 33605:00 - 33650:00

is this idea that maybe every agent

## 33650:00 - 33690:00

should actually use code and be a coding

## 33690:00 - 33710:00

agent.

## 33710:00 - 33730:00

And in my mind that's just like a small

## 33730:00 - 33760:00

part of this like broader idea that

## 33760:00 - 33790:00

like, hey, as we make code even more

## 33790:00 - 33805:00

ubiquitous. I mean, you could probably

## 33805:00 - 33835:00

claim it's ubiquitous today even pre-AI,

## 33835:00 - 33865:00

right? And as you make code even more

## 33865:00 - 33890:00

ubiquitous, it's actually just going to

## 33890:00 - 33935:00

be used for many more purposes.

## 33935:00 - 33965:00

And so there's just going to be a ton

## 33965:00 - 33995:00

more need for people with this like

## 33995:00 - 34025:00

humans with this competency.

## 34025:00 - 34040:00

So

## 34040:00 - 34075:00

that's my view. I think this is like

## 34075:00 - 34115:00

quite a complex topic. So you know, you

## 34115:00 - 34130:00

know, it's something we talk about a lot

## 34130:00 - 34150:00

and we have to kind of see how it pans

## 34150:00 - 34190:00

out, but I think what we can do

## 34190:00 - 34215:00

what we can do basically as a product

## 34215:00 - 34240:00

team building in the space is just try

## 34240:00 - 34270:00

to always think about how are we

## 34270:00 - 34290:00

building a tool so that it feels like

## 34290:00 - 34325:00

we're like maximally accelerating

## 34325:00 - 34345:00

uh people.

## 34345:00 - 34375:00

You know, rather than building a tool

## 34375:00 - 34415:00

that makes it like more unclear what you

## 34415:00 - 34450:00

should do as the human. Right? Like I

## 34450:00 - 34475:00

think like to

## 34475:00 - 34505:00

to you know, give an example right now

## 34505:00 - 34520:00

like

## 34520:00 - 34545:00

nowadays when you work with a coding

## 34545:00 - 34585:00

agent, um it writes a ton of code, but

## 34585:00 - 34605:00

it turns out writing code is actually

## 34605:00 - 34630:00

one of the most fun parts of software

## 34630:00 - 34665:00

engineering for many software engineers.

## 34665:00 - 34685:00

And so then you end up reviewing AI

## 34685:00 - 34700:00

code.

## 34700:00 - 34760:00

Right? And that's often a less fun part

## 34760:00 - 34795:00

of the job for many software engineers,

## 34795:00 - 34830:00

right? And so I actually think like we

## 34830:00 - 34855:00

see that like this this comes out plays

## 34855:00 - 34880:00

out all the time in like a ton of micro

## 34880:00 - 34900:00

decisions and so we as a product team

## 34900:00 - 34920:00

are always thinking about like, okay,

## 34920:00 - 34935:00

how do we make this more fun? How do we

## 34935:00 - 34965:00

make you feel more empowered? Where is

## 34965:00 - 34990:00

this not working? And I would argue that

## 34990:00 - 35020:00

like reviewing agent written code is

## 35020:00 - 35040:00

like a place that

## 35040:00 - 35080:00

today is like less fun and so you know,

## 35080:00 - 35105:00

then I think, okay, what can we do about

## 35105:00 - 35125:00

that? Well, we can ship a code review

## 35125:00 - 35150:00

feature that like helps you both

## 35150:00 - 35175:00

confidence the AI written code. Okay,

## 35175:00 - 35200:00

cool.

## 35200:00 - 35215:00

You know, another thing we could do is

## 35215:00 - 35235:00

we can make it so that the agent's like

## 35235:00 - 35275:00

better able to validate its work.

## 35275:00 - 35295:00

And you know, it it gets all the way

## 35295:00 - 35320:00

down into like micro decisions. Like if

## 35320:00 - 35355:00

you're going to have the an agent

## 35355:00 - 35385:00

capability to validate work and let's

## 35385:00 - 35410:00

say you have like I'm thinking of Codex

## 35410:00 - 35450:00

web right now. Like you have a a pane

## 35450:00 - 35475:00

that sort of reflects the work the agent

## 35475:00 - 35500:00

did. What do you see first? Do you see

## 35500:00 - 35525:00

the diff or do you see the image preview

## 35525:00 - 35550:00

of the code it wrote?

## 35550:00 - 35585:00

Right? And you know, I think if you're

## 35585:00 - 35605:00

thinking about this from perspective

## 35605:00 - 35625:00

like, how do I empower the human? How do

## 35625:00 - 35650:00

I make them feel like as as accelerated

## 35650:00 - 35685:00

as possible? Like you obviously see the

## 35685:00 - 35705:00

image first, right? You shouldn't be

## 35705:00 - 35745:00

reviewing the code unless first you

## 35745:00 - 35765:00

know, you've seen the image unless it's

## 35765:00 - 35790:00

maybe it's been like reviewed by an AI

## 35790:00 - 35805:00

and now it's time for you to take a

## 35805:00 - 35845:00

look. When I had Michael Turalda, CEO of

## 35845:00 - 35875:00

Cursor on the podcast, he had this kind

## 35875:00 - 35925:00

of vision of us moving to something

## 35925:00 - 35950:00

beyond code.

## 35950:00 - 35975:00

And I've seen this rise of something

## 35975:00 - 36005:00

called spec driven development where you

## 36005:00 - 36040:00

kind of just write the spec and then the

## 36040:00 - 36065:00

code, you know, the AI writes the code

## 36065:00 - 36090:00

for you and so you kind of start working

## 36090:00 - 36125:00

at this higher abstraction level.

## 36125:00 - 36150:00

Is that something you see where we're

## 36150:00 - 36180:00

going? Just like engineers not having to

## 36180:00 - 36205:00

actually write code or look at code and

## 36205:00 - 36230:00

there's going to be this higher level of

## 36230:00 - 36265:00

abstraction that we focus on.

## 36265:00 - 36295:00

Yeah, I mean, I think

## 36295:00 - 36315:00

I think there's like constantly these

## 36315:00 - 36330:00

levels of abstraction and they're

## 36330:00 - 36370:00

actually already played out today.

## 36370:00 - 36405:00

Right? Like today like coding agents

## 36405:00 - 36455:00

mostly it's like prompt to patch.

## 36455:00 - 36490:00

Right? We're starting to see people

## 36490:00 - 36520:00

doing like spec driven development or

## 36520:00 - 36545:00

like plan driven development. That's

## 36545:00 - 36570:00

actually one of the ways people ask

## 36570:00 - 36590:00

like, hey, how do you run Codex on a

## 36590:00 - 36615:00

really long task? Well, it's like often

## 36615:00 - 36645:00

collaborate with it first to write like

## 36645:00 - 36675:00

a plan.md like a markdown file that's

## 36675:00 - 36695:00

your plan.

## 36695:00 - 36720:00

And once you're happy with that, then

## 36720:00 - 36745:00

you ask it to to go off and do work and

## 36745:00 - 36775:00

if that plan has verifiable steps, it'll

## 36775:00 - 36805:00

like work for much longer.

## 36805:00 - 36845:00

Um so we're totally seeing that.

## 36845:00 - 36870:00

I think spec driven development is like

## 36870:00 - 36910:00

an interesting idea. It's not clear to

## 36910:00 - 36940:00

me that it'll work out that way cuz a

## 36940:00 - 36960:00

lot of people don't write like don't

## 36960:00 - 36995:00

like writing specs either.

## 36995:00 - 37025:00

But it it seems plausible that some some

## 37025:00 - 37050:00

people will work that way. You know,

## 37050:00 - 37075:00

like uh

## 37075:00 - 37100:00

a bit of a joke idea though is like if

## 37100:00 - 37120:00

you think of like

## 37120:00 - 37160:00

um the way that many teams work today,

## 37160:00 - 37180:00

they're they often like don't

## 37180:00 - 37215:00

necessarily have specs, but the team is

## 37215:00 - 37240:00

just really self-driven and so stuff

## 37240:00 - 37260:00

just gets done and so almost that is

## 37260:00 - 37280:00

like I'm coming up with this on the

## 37280:00 - 37305:00

spot. So it's you know, not a good name,

## 37305:00 - 37350:00

but like chatter driven development.

## 37350:00 - 37375:00

Where it's just like stuff is happening,

## 37375:00 - 37405:00

you know, on social media and like in

## 37405:00 - 37430:00

your team communications tools and then

## 37430:00 - 37460:00

as a result like code gets written and

## 37460:00 - 37480:00

deployed.

## 37480:00 - 37500:00

Right? So

## 37500:00 - 37525:00

yeah, I think I'm a little bit more

## 37525:00 - 37565:00

oriented in that way of

## 37565:00 - 37590:00

you know, I don't even necessarily want

## 37590:00 - 37615:00

to have to write a spec. Like sometimes

## 37615:00 - 37665:00

I want to only if I like writing specs.

## 37665:00 - 37680:00

Right?

## 37680:00 - 37710:00

Other times I might just want to say

## 37710:00 - 37740:00

like, hey, here's like the customer, you

## 37740:00 - 37770:00

know, service channel and like tell me

## 37770:00 - 37795:00

what's interesting to know, but if it's

## 37795:00 - 37825:00

a small bug, just fix it. I don't want

## 37825:00 - 37860:00

to have to write a spec for that,

## 37860:00 - 37895:00

I have this sort of

## 37895:00 - 37930:00

uh hypothetical future

## 37930:00 - 37960:00

uh that I like to share with sometimes

## 37960:00 - 37980:00

with people as a provocation which is

## 37980:00 - 38010:00

like in a world where we have like truly

## 38010:00 - 38035:00

amazing agents, like what does it look

## 38035:00 - 38070:00

like to be a solopreneur?

## 38070:00 - 38085:00

Um

## 38085:00 - 38130:00

and uh you know, one terrible idea for

## 38130:00 - 38155:00

how it could look is that it's actually

## 38155:00 - 38215:00

is a mobile app. And um every idea that

## 38215:00 - 38250:00

it the agent has to do is just like

## 38250:00 - 38290:00

vertical video on your phone.

## 38290:00 - 38325:00

And then you can like swipe left if you

## 38325:00 - 38350:00

think it's a bad idea and you can like

## 38350:00 - 38375:00

swipe right if it's a good idea and like

## 38375:00 - 38410:00

you can press and hold and like speak to

## 38410:00 - 38435:00

your phone if you want to give feedback

## 38435:00 - 38470:00

on the idea before you swipe.

## 38470:00 - 38490:00

You know, and in this world like

## 38490:00 - 38515:00

basically what your job is just like

## 38515:00 - 38545:00

plug in this app into like every single

## 38545:00 - 38590:00

like signal system, you know, system of

## 38590:00 - 38610:00

record and then you just sort of sit

## 38610:00 - 38650:00

back and like swipe. I don't know. I

## 38650:00 - 38680:00

love this. So this is like Tinder meets

## 38680:00 - 38715:00

TikTok meets Codex. It's pretty

## 38715:00 - 38755:00

terrible. No, this is great. So the idea

## 38755:00 - 38780:00

here is this thing is this agent is

## 38780:00 - 38815:00

watching and right listening to you,

## 38815:00 - 38840:00

paying attention to the market, your

## 38840:00 - 38865:00

users and it's like, well, I hear

## 38865:00 - 38885:00

something I should do. It's like a

## 38885:00 - 38910:00

proactive engineer. Just like, here, we

## 38910:00 - 38930:00

should build this feature or fix this

## 38930:00 - 38940:00

thing.

## 38940:00 - 38970:00

Exactly. I think it's a really good

## 38970:00 - 38995:00

idea. Communicating with you in like the

## 38995:00 - 39025:00

lowest like effort way.

## 39025:00 - 39055:00

>> the gyms, like the the modern way we

## 39055:00 - 39080:00

communicate.

## 39080:00 - 39115:00

Yeah, swipe left or right and in

## 39115:00 - 39150:00

vertical feed. And then the Sora video.

## 39150:00 - 39190:00

Okay, I see how this all connects now. I

## 39190:00 - 39195:00

see.

## 39195:00 - 39225:00

>> Yeah, to be clear, we're not building

## 39225:00 - 39245:00

that, but like, you know, it's a fun

## 39245:00 - 39275:00

idea. I mean, you can see now like in

## 39275:00 - 39300:00

this example though, like one of the

## 39300:00 - 39320:00

things that it's doing is it's consuming

## 39320:00 - 39355:00

external signals, right? I think the

## 39355:00 - 39385:00

other really interesting thing is like

## 39385:00 - 39410:00

if we think about like what is the most

## 39410:00 - 39435:00

successful like

## 39435:00 - 39475:00

AI product to date?

## 39475:00 - 39490:00

Um

## 39490:00 - 39545:00

I would argue um funny actually not to

## 39545:00 - 39575:00

confuse things at all, but like with the

## 39575:00 - 39605:00

first time we used in the the brand

## 39605:00 - 39635:00

Codex at OpenAI was actually the model

## 39635:00 - 39660:00

powering GitHub Copilot. This is like

## 39660:00 - 39690:00

way back in the day years ago.

## 39690:00 - 39720:00

Uh so we decided to reuse that that

## 39720:00 - 39755:00

brand recently um cuz it's just so good.

## 39755:00 - 39795:00

You know, Codex, code execution. But

## 39795:00 - 39830:00

I think actually like

## 39830:00 - 39855:00

auto completion in IDEs is like one of

## 39855:00 - 39905:00

the most successful AI products today.

## 39905:00 - 39935:00

And part of what's so magical about it

## 39935:00 - 39960:00

is that

## 39960:00 - 40010:00

when the it can surface like ideas for

## 40010:00 - 40030:00

helping you

## 40030:00 - 40055:00

really rapidly.

## 40055:00 - 40080:00

When it's right, you're accelerated.

## 40080:00 - 40110:00

When it's wrong, it's not like that

## 40110:00 - 40130:00

annoying. It can be annoying, but it's

## 40130:00 - 40165:00

not that annoying. Right? And so you can

## 40165:00 - 40195:00

create this like mixed initiative system

## 40195:00 - 40230:00

that's like contextually responding to

## 40230:00 - 40265:00

like what you're attempting to do.

## 40265:00 - 40310:00

And so in my mind, this is like

## 40310:00 - 40335:00

a really interesting thing for us as

## 40335:00 - 40365:00

OpenAI as we're building.

## 40365:00 - 40395:00

So for instance, you know, when I think

## 40395:00 - 40435:00

about launching a browser, which we did

## 40435:00 - 40485:00

with Atlas, right? Like in my mind,

## 40485:00 - 40500:00

one of the really interesting things we

## 40500:00 - 40535:00

can then do is we can then like

## 40535:00 - 40565:00

contextually surface like ways that we

## 40565:00 - 40595:00

can help you as you're going about your

## 40595:00 - 40630:00

day. Right? And so we break out of this

## 40630:00 - 40645:00

like

## 40645:00 - 40670:00

you know, we're just looking at code or

## 40670:00 - 40705:00

we're just in your terminal um into this

## 40705:00 - 40730:00

idea that like, "Hey, like a real

## 40730:00 - 40755:00

teammate is dealing with a lot more than

## 40755:00 - 40780:00

just code, right? They're dealing with a

## 40780:00 - 40805:00

lot of things that are web content." So

## 40805:00 - 40820:00

like,

## 40820:00 - 40850:00

you know, how can we help you with that?

## 40850:00 - 40885:00

Man, there's so much there. I love this.

## 40885:00 - 40915:00

Okay, so auto complete on web with the

## 40915:00 - 40940:00

browser, that's so interesting. Just

## 40940:00 - 40970:00

like here's all the things that

## 40970:00 - 40990:00

we can help you with as you're browsing

## 40990:00 - 41000:00

and

## 41000:00 - 41025:00

going about your day. I want to talk

## 41025:00 - 41060:00

about Atlas. I'll come back to that. Uh

## 41060:00 - 41090:00

Codex, code execution, did not know

## 41090:00 - 41120:00

that. That's really clever.

## 41120:00 - 41155:00

I I get it now. Okay, and then this

## 41155:00 - 41180:00

chatter. What is a chatter driven

## 41180:00 - 41220:00

development? Uh I had a No, this is a

## 41220:00 - 41250:00

really good idea. But it reminds me I

## 41250:00 - 41290:00

had John G Donji on the podcast, CTO of

## 41290:00 - 41325:00

Block, and they they have this product

## 41325:00 - 41340:00

called Goose, which is their own

## 41340:00 - 41380:00

internal agent

## 41380:00 - 41425:00

thing. And he talked about an engineer

## 41425:00 - 41490:00

at Block just uh has Goose watch him

## 41490:00 - 41530:00

with like his screen and listens to

## 41530:00 - 41590:00

every meeting and proactively does work

## 41590:00 - 41620:00

that he should probably want to do. So

## 41620:00 - 41665:00

ships a PR, sends an email, drafts a

## 41665:00 - 41705:00

Slack message. So he's doing exactly

## 41705:00 - 41730:00

what you're describing in in kind of a

## 41730:00 - 41755:00

very early way.

## 41755:00 - 41780:00

Yeah, that's super interesting. And you

## 41780:00 - 41820:00

know, I bet you the so if we go if we

## 41820:00 - 41850:00

went and asked them what the bottleneck

## 41850:00 - 41875:00

to that productivity is, did did they

## 41875:00 - 41915:00

share what it is? Uh probably looking at

## 41915:00 - 41935:00

it and just making sure this is the

## 41935:00 - 41965:00

right the right thing to do. Yeah.

## 41965:00 - 41990:00

Yeah, so like we see this now. Like we

## 41990:00 - 42025:00

have a Slack integration for Codex.

## 42025:00 - 42045:00

People love, you know, if there's like

## 42045:00 - 42070:00

something that you need to do quickly,

## 42070:00 - 42090:00

people will just like at mention Codex.

## 42090:00 - 42115:00

Like, "Why do you think this bug is

## 42115:00 - 42140:00

happening?" Right? Doesn't have to be an

## 42140:00 - 42160:00

engineer. Even like maybe, you know,

## 42160:00 - 42195:00

data scientists often in here are using

## 42195:00 - 42220:00

Codex a ton to just like answer

## 42220:00 - 42235:00

questions. Like, "Why do you think this

## 42235:00 - 42270:00

metric moved? What happened?"

## 42270:00 - 42300:00

So questions, you know, you get the

## 42300:00 - 42320:00

answer right back in Slack, it's

## 42320:00 - 42345:00

amazing, super useful.

## 42345:00 - 42370:00

But when it's as for when it's writing

## 42370:00 - 42390:00

code,

## 42390:00 - 42405:00

then you have to go back and look at the

## 42405:00 - 42425:00

code.

## 42425:00 - 42450:00

Right? And so

## 42450:00 - 42480:00

the real like I think bottleneck right

## 42480:00 - 42510:00

now is like validating that the code

## 42510:00 - 42550:00

worked and like writing code review.

## 42550:00 - 42575:00

So in my mind, if we wanted to get to

## 42575:00 - 42615:00

something like you know, the friend you

## 42615:00 - 42655:00

were talking about's world, I think we

## 42655:00 - 42680:00

we really need to figure out how to get

## 42680:00 - 42715:00

people to configure their coding agents

## 42715:00 - 42740:00

to be much more autonomous on those

## 42740:00 - 42770:00

later stages of the work. It makes

## 42770:00 - 42800:00

sense. Like you said, writing code I

## 42800:00 - 42820:00

used to be an engineer, I was an

## 42820:00 - 42850:00

engineer for 10 years. Really fun to

## 42850:00 - 42870:00

write code, really fun to just get in

## 42870:00 - 42905:00

the flow, build, architect, test.

## 42905:00 - 42930:00

Not so fun to look at everyone else's

## 42930:00 - 42960:00

code and just have to go through and be

## 42960:00 - 42990:00

on the hook if it is doing something

## 42990:00 - 43005:00

dumb that's going to take down

## 43005:00 - 43040:00

production. And now that building has

## 43040:00 - 43065:00

become easier, what I've always heard

## 43065:00 - 43085:00

from companies that are really at the

## 43085:00 - 43115:00

cutting edge of this is the bottleneck

## 43115:00 - 43145:00

is now like figuring out what to build

## 43145:00 - 43170:00

and then it's at the end of like a Okay,

## 43170:00 - 43210:00

we have all this all 100 PRs to review.

## 43210:00 - 43240:00

Who's going to go through all that?

## 43240:00 - 43280:00

Right. Yeah.

## 43280:00 - 43310:00

This episode is brought to you by Jira

## 43310:00 - 43345:00

Product Discovery. The hardest part of

## 43345:00 - 43370:00

building products isn't actually

## 43370:00 - 43410:00

building products. It's everything else.

## 43410:00 - 43435:00

It's proving that the work matters,

## 43435:00 - 43470:00

managing stakeholders, trying to plan

## 43470:00 - 43505:00

ahead. Most teams spend more time

## 43505:00 - 43540:00

reacting than learning, chasing updates,

## 43540:00 - 43570:00

justifying roadmaps, and constantly

## 43570:00 - 43610:00

unblocking work to keep things moving.

## 43610:00 - 43645:00

Jira Product Discovery puts you back in

## 43645:00 - 43685:00

control. With Jira Product Discovery,

## 43685:00 - 43720:00

you can capture insights and prioritize

## 43720:00 - 43760:00

high impact ideas. It's flexible, so it

## 43760:00 - 43790:00

adapts to the way your team works and

## 43790:00 - 43820:00

helps you build a roadmap that drives

## 43820:00 - 43860:00

alignment, not questions. And because

## 43860:00 - 43895:00

it's built on Jira, you can track ideas

## 43895:00 - 43935:00

from strategy to delivery, all in one

## 43935:00 - 43980:00

place. Less chasing, more time to think,

## 43980:00 - 44015:00

learn, and build the right thing. Get

## 44015:00 - 44050:00

Jira Product Discovery for free at

## 44050:00 - 44095:00

atlassian.com/lenny.

## 44095:00 - 44140:00

That's atlassian.com/lenny.

## 44140:00 - 44185:00

What is the impact of Codex been on the

## 44185:00 - 44220:00

way you operate as a product person as a

## 44220:00 - 44255:00

PM? It's clear how engineering is

## 44255:00 - 44285:00

impacted. Uh

## 44285:00 - 44325:00

code is written for you.

## 44325:00 - 44350:00

What has it done to the way you operate

## 44350:00 - 44395:00

in the way PMs operate at at OpenAI?

## 44395:00 - 44430:00

Yeah, I mean I think mostly I just feel

## 44430:00 - 44465:00

like much more empowered.

## 44465:00 - 44490:00

Um

## 44490:00 - 44515:00

I've always been sort of more technical

## 44515:00 - 44545:00

leaning PM. And especially when I'm

## 44545:00 - 44565:00

working on products for engineers, I

## 44565:00 - 44590:00

feel like it's necessary to like, you

## 44590:00 - 44620:00

know, dogfood the product. But even

## 44620:00 - 44650:00

beyond that, I I I just feel like I can

## 44650:00 - 44680:00

do much much more

## 44680:00 - 44710:00

as a PM. And uh you know, Scott Belsky

## 44710:00 - 44725:00

talks about this idea of like

## 44725:00 - 44755:00

compressing the talent stack. I'm not

## 44755:00 - 44780:00

sure if I'm phrased that right.

## 44780:00 - 44805:00

But it's basically this idea that like

## 44805:00 - 44830:00

maybe the boundaries between these roles

## 44830:00 - 44870:00

are a little bit like less needed than

## 44870:00 - 44905:00

before because people can just do much

## 44905:00 - 44945:00

more. And every time you someone can do

## 44945:00 - 44970:00

more, you can like skip one

## 44970:00 - 45005:00

communication boundary and make the team

## 45005:00 - 45035:00

like that much more efficient.

## 45035:00 - 45070:00

Right? So I think

## 45070:00 - 45100:00

I think we see it

## 45100:00 - 45135:00

you know, in a bunch of functions now,

## 45135:00 - 45155:00

but I guess since you asked about like

## 45155:00 - 45185:00

product specifically,

## 45185:00 - 45210:00

uh you know, now like answering

## 45210:00 - 45250:00

questions much much easier. You you

## 45250:00 - 45270:00

know, just ask Codex for thoughts on

## 45270:00 - 45320:00

that. Uh a lot of like PM type work,

## 45320:00 - 45345:00

understanding what's changing, again,

## 45345:00 - 45395:00

just ask Codex for help with that. Um

## 45395:00 - 45435:00

prototyping is often faster than writing

## 45435:00 - 45455:00

specs. This is something that a lot of

## 45455:00 - 45485:00

people have talked about.

## 45485:00 - 45520:00

I think something that

## 45520:00 - 45540:00

I don't think it's super surprising, but

## 45540:00 - 45555:00

something that's slightly surprising is

## 45555:00 - 45580:00

like we see

## 45580:00 - 45605:00

like we're mostly building Codex for to

## 45605:00 - 45625:00

write code that's going to be deployed

## 45625:00 - 45650:00

to production.

## 45650:00 - 45675:00

But actually we see a lot of throwaway

## 45675:00 - 45710:00

code written with Codex now. It's kind

## 45710:00 - 45725:00

of going back to this idea of like, you

## 45725:00 - 45755:00

know, ubiquitous code.

## 45755:00 - 45775:00

So you'll see

## 45775:00 - 45810:00

uh you know, someone wants to do an

## 45810:00 - 45830:00

analysis. Like if I want to understand

## 45830:00 - 45850:00

something, it's like, "Okay, just give

## 45850:00 - 45875:00

Codex a bunch of data, but then ask it

## 45875:00 - 45900:00

to build like an interactive like data

## 45900:00 - 45925:00

viewer for this data." Right? You would

## 45925:00 - 45945:00

That's just like too annoying to do in

## 45945:00 - 45975:00

the past, but now it's just like totally

## 45975:00 - 46005:00

worth the time of just getting an agent

## 46005:00 - 46025:00

to go do something.

## 46025:00 - 46045:00

Um

## 46045:00 - 46075:00

similarly, I've seen like some pretty

## 46075:00 - 46100:00

cool prototypes on our design team about

## 46100:00 - 46140:00

like if you want to

## 46140:00 - 46160:00

well, like a designer basically wanted

## 46160:00 - 46185:00

to build an animation.

## 46185:00 - 46230:00

And this is the coin animation in Codex.

## 46230:00 - 46260:00

And it was like normally it'd be too

## 46260:00 - 46285:00

annoying to program this animation, so

## 46285:00 - 46340:00

they just vibe coded a animation editor.

## 46340:00 - 46360:00

And then they use the animation editor

## 46360:00 - 46380:00

to build the animation, which they then

## 46380:00 - 46410:00

checked into the repo.

## 46410:00 - 46425:00

Actually, our designers are there's a

## 46425:00 - 46455:00

ton of acceleration there and like

## 46455:00 - 46475:00

speaking of compressing the talent

## 46475:00 - 46495:00

stack, I think our designers are very

## 46495:00 - 46525:00

PM-y.

## 46525:00 - 46555:00

So, you know, they they do a ton of

## 46555:00 - 46590:00

product work and like they actually have

## 46590:00 - 46630:00

like an entire like vibe coded sort of

## 46630:00 - 46655:00

side prototype

## 46655:00 - 46680:00

of the Codex app. And so a lot of how we

## 46680:00 - 46700:00

talk about things is like we'll have

## 46700:00 - 46730:00

like a really quick jam cuz there's like

## 46730:00 - 46760:00

10,000 things going on. And then the

## 46760:00 - 46780:00

designer will like go think about how

## 46780:00 - 46800:00

this should work, but instead of like

## 46800:00 - 46815:00

talking about it again, they'll just

## 46815:00 - 46845:00

like vibe code a prototype of that in

## 46845:00 - 46875:00

their like standalone prototype. We'll

## 46875:00 - 46900:00

play with it. If we like it, they'll

## 46900:00 - 46940:00

vibe code that prototype into or vibe

## 46940:00 - 46985:00

engineer that prototype into an actual

## 46985:00 - 47020:00

PR to land. And then depending on their

## 47020:00 - 47045:00

comfort with the code base, like Codex

## 47045:00 - 47075:00

UI is in Rust, that's a little harder.

## 47075:00 - 47100:00

Maybe they'll like land it themselves or

## 47100:00 - 47120:00

they'll like get close and then an

## 47120:00 - 47160:00

engineer can help them like land the PR.

## 47160:00 - 47175:00

Um

## 47175:00 - 47205:00

you know, we recently shipped the Sora

## 47205:00 - 47225:00

Android app.

## 47225:00 - 47275:00

Um and uh that was one of the most sort

## 47275:00 - 47290:00

of

## 47290:00 - 47320:00

mind-blowing examples of acceleration

## 47320:00 - 47360:00

actually cuz the usage of Codex

## 47360:00 - 47390:00

internally at OpenAI is obviously really

## 47390:00 - 47435:00

really high, but it's been growing uh

## 47435:00 - 47460:00

over the course of the year both in

## 47460:00 - 47485:00

terms of like now it's basically like

## 47485:00 - 47520:00

all technical staff use it. Uh but even

## 47520:00 - 47545:00

like the intensity and know-how of how

## 47545:00 - 47565:00

to make the most of coding agents has

## 47565:00 - 47605:00

gone up by a ton. And so the Sora

## 47605:00 - 47625:00

Android app, right? Like a fully new

## 47625:00 - 47645:00

app,

## 47645:00 - 47670:00

we built it

## 47670:00 - 47720:00

in 18 days. It went from like zero to

## 47720:00 - 47760:00

launch to employees. And then 10 days

## 47760:00 - 47795:00

later, so 28 days total, we went to just

## 47795:00 - 47835:00

like GA to the public.

## 47835:00 - 47855:00

And that was done just like with the

## 47855:00 - 47885:00

help of Codex.

## 47885:00 - 47930:00

So pretty insane velocity. I would say

## 47930:00 - 47965:00

it was like a little bit

## 47965:00 - 48005:00

I don't want to say easy mode, but there

## 48005:00 - 48035:00

is one thing that Codex is really good

## 48035:00 - 48055:00

at if you're a company that's like

## 48055:00 - 48090:00

building software on multiple platforms.

## 48090:00 - 48115:00

So you've already figured out like some

## 48115:00 - 48150:00

of the underlying like APIs or systems.

## 48150:00 - 48185:00

Asking Codex to sit like to port things

## 48185:00 - 48230:00

over is really effective cuz it has like

## 48230:00 - 48250:00

something it can go look at. And so the

## 48250:00 - 48275:00

engineers on that team

## 48275:00 - 48310:00

uh were basically having Codex

## 48310:00 - 48350:00

go look at the iOS app, produce plans of

## 48350:00 - 48370:00

work that needed to be done, and then go

## 48370:00 - 48395:00

implement those. And it was kind of

## 48395:00 - 48415:00

looking at iOS and Android at the same

## 48415:00 - 48450:00

time. And so, you know, basically it was

## 48450:00 - 48475:00

like 2 weeks to launch to employees, 4

## 48475:00 - 48495:00

weeks total.

## 48495:00 - 48535:00

Insanely fast. What makes that even more

## 48535:00 - 48565:00

insane is it was the it became the

## 48565:00 - 48600:00

number one app in the App Store.

## 48600:00 - 48620:00

I don't

## 48620:00 - 48660:00

this just boggles the mind. Okay, so

## 48660:00 - 48680:00

Yeah, so imagine there's the number one

## 48680:00 - 48720:00

app in the App Store with like a handful

## 48720:00 - 48745:00

of engineers.

## 48745:00 - 48785:00

Uh I think it was like

## 48785:00 - 48815:00

two or three possibly

## 48815:00 - 48830:00

uh

## 48830:00 - 48855:00

in a handful of weeks.

## 48855:00 - 48880:00

Yeah.

## 48880:00 - 48925:00

This is absurd.

## 48925:00 - 48940:00

So

## 48940:00 - 48980:00

yeah, so that's a really fun um

## 48980:00 - 49020:00

example of acceleration and then like

## 49020:00 - 49060:00

Atlas is the other one that I think

## 49060:00 - 49100:00

Ben did a podcast the the the

## 49100:00 - 49125:00

engine on Atlas

## 49125:00 - 49145:00

uh sharing a little bit about how we

## 49145:00 - 49165:00

built there.

## 49165:00 - 49210:00

You know, many Atlas is is actually I

## 49210:00 - 49240:00

mean it's a it's a browser, right? And

## 49240:00 - 49280:00

building a browser is really hard. Um

## 49280:00 - 49300:00

and so

## 49300:00 - 49325:00

we uh

## 49325:00 - 49365:00

had to build a lot of difficult systems

## 49365:00 - 49410:00

in order to do that. And basically we

## 49410:00 - 49440:00

got to the point where that team has a

## 49440:00 - 49480:00

ton of power users of Codex

## 49480:00 - 49505:00

right now. And

## 49505:00 - 49520:00

you know, got to the point where they

## 49520:00 - 49545:00

they were basically we you know, we were

## 49545:00 - 49570:00

talking to them about it cuz a lot of

## 49570:00 - 49590:00

those engineers are people I I to work

## 49590:00 - 49630:00

with uh before at my startup. And so

## 49630:00 - 49650:00

they'd say, you know, before this would

## 49650:00 - 49690:00

have taken us like 2 to 3 weeks for two

## 49690:00 - 49715:00

to three engineers.

## 49715:00 - 49755:00

And now it's like one engineer, one

## 49755:00 - 49775:00

week.

## 49775:00 - 49805:00

Um so, massive acceleration there as

## 49805:00 - 49850:00

well. And what's quite cool is that uh

## 49850:00 - 49875:00

you know, we we shipped Atlas on on Mac

## 49875:00 - 49900:00

first, but now we're working on the

## 49900:00 - 49920:00

Windows version.

## 49920:00 - 49945:00

You know, that So, the team now is like

## 49945:00 - 49960:00

ramping up on Windows, and they're

## 49960:00 - 49990:00

helping us make Codex better on Windows,

## 49990:00 - 50035:00

too. Which is admittedly earlier. Like,

## 50035:00 - 50065:00

just the model we we shipped last week

## 50065:00 - 50100:00

is the first model that natively

## 50100:00 - 50135:00

understands PowerShell. So, you know,

## 50135:00 - 50155:00

PowerShell being

## 50155:00 - 50195:00

uh the native like shell language on

## 50195:00 - 50245:00

Windows. So, yeah, it's been it's been

## 50245:00 - 50265:00

really awesome to see like the whole

## 50265:00 - 50295:00

company getting accelerated by Codex

## 50295:00 - 50320:00

like from

## 50320:00 - 50365:00

And you know, most obviously also

## 50365:00 - 50390:00

research and like improving how quickly

## 50390:00 - 50420:00

we train models and how well we do it,

## 50420:00 - 50450:00

and then even like uh design as we

## 50450:00 - 50480:00

talked about and and marketing. Like,

## 50480:00 - 50510:00

actually we're at this point now where

## 50510:00 - 50540:00

uh my product marketer is often also

## 50540:00 - 50565:00

making string changes just directly from

## 50565:00 - 50600:00

Slack. Or like updating docs directly

## 50600:00 - 50650:00

from Slack. These are amazing examples.

## 50650:00 - 50685:00

You guys are living at the bleeding edge

## 50685:00 - 50720:00

of what is possible, and this is how

## 50720:00 - 50750:00

other companies are going to work. Uh

## 50750:00 - 50785:00

just shipping again, what became the

## 50785:00 - 50805:00

number one app in the App Store and just

## 50805:00 - 50830:00

beloved all over the It just like took

## 50830:00 - 50875:00

over the I don't know, the world for at

## 50875:00 - 50915:00

least a week. Uh built, you said in 28

## 50915:00 - 50960:00

days and like I don't know, 10 days, 18

## 50960:00 - 51000:00

days just to get like the core of it

## 51000:00 - 51005:00

working.

## 51005:00 - 51030:00

>> Yeah, so it's like 18 days we had a

## 51030:00 - 51055:00

thing that employees were playing with,

## 51055:00 - 51090:00

and then 10 days later we were out. And

## 51090:00 - 51130:00

you said just a couple engineers. Yeah.

## 51130:00 - 51155:00

Two or three. Okay. And then Atlas, you

## 51155:00 - 51195:00

said it was took a week to build.

## 51195:00 - 51220:00

>> No, no, no. So, Atlas is not the whole

## 51220:00 - 51250:00

week, but Atlas was like

## 51250:00 - 51290:00

a really meaty project. Yeah. Um and so

## 51290:00 - 51310:00

I was talking to one of the engineers on

## 51310:00 - 51335:00

Atlas um

## 51335:00 - 51370:00

about like, you know, just how

## 51370:00 - 51385:00

what they use Codex for. And it's

## 51385:00 - 51400:00

basically like, we use Codex for

## 51400:00 - 51430:00

absolutely everything. I was like, okay.

## 51430:00 - 51460:00

Well, like you know, how would you how

## 51460:00 - 51480:00

would you measure the acceleration? And

## 51480:00 - 51505:00

so, basically the the answer I got back

## 51505:00 - 51525:00

was

## 51525:00 - 51550:00

previously would have taken two to three

## 51550:00 - 51575:00

weeks for two to three engineers, and

## 51575:00 - 51610:00

now it's like one engineer, one week. Do

## 51610:00 - 51635:00

you think this eventually moves to

## 51635:00 - 51660:00

non-engineers doing this sort of thing?

## 51660:00 - 51680:00

Like, does it have to be an engineer

## 51680:00 - 51710:00

building this thing? Could sort of built

## 51710:00 - 51735:00

been built by a I don't know, a PM or a

## 51735:00 - 51765:00

designer? I think we will very much get

## 51765:00 - 51795:00

to the point where Well, basically where

## 51795:00 - 51835:00

the boundaries are a little bit blurred.

## 51835:00 - 51865:00

Right? Like

## 51865:00 - 51880:00

I think we you're going to want someone

## 51880:00 - 51910:00

who's like understands the details of

## 51910:00 - 51935:00

what they're building, but what details

## 51935:00 - 51970:00

those are will evolve. Kind of like how

## 51970:00 - 52000:00

now like, if you're writing Swift, you

## 52000:00 - 52045:00

don't have to speak assembly.

## 52045:00 - 52060:00

You know, there's a handful of people in

## 52060:00 - 52080:00

the world, and it's really important

## 52080:00 - 52125:00

that they exist and like speak assembly.

## 52125:00 - 52155:00

Uh maybe more than a handful, right? But

## 52155:00 - 52180:00

that's like a specialized function that

## 52180:00 - 52200:00

like most

## 52200:00 - 52240:00

companies don't need to have.

## 52240:00 - 52250:00

So, I think we're just going to

## 52250:00 - 52290:00

naturally see like an increase in layers

## 52290:00 - 52315:00

of abstraction.

## 52315:00 - 52340:00

And then the cool thing is now we're

## 52340:00 - 52365:00

we're entering like the language layer

## 52365:00 - 52405:00

of abstraction, like natural language.

## 52405:00 - 52425:00

And then natural language itself is

## 52425:00 - 52450:00

really flexible.

## 52450:00 - 52470:00

Right? Like, you could have engineers

## 52470:00 - 52505:00

talking about like a plan, and then you

## 52505:00 - 52520:00

could have engineers talking about a

## 52520:00 - 52540:00

spec, and then you could have engineers

## 52540:00 - 52570:00

talking about just you know, a product

## 52570:00 - 52595:00

or an idea. So, I think we can also like

## 52595:00 - 52625:00

start moving up those layers of of

## 52625:00 - 52660:00

abstraction as well.

## 52660:00 - 52675:00

But

## 52675:00 - 52695:00

you know, I I do think this is going to

## 52695:00 - 52720:00

be gradual. I don't think it's going to

## 52720:00 - 52740:00

go up to like all of a sudden like

## 52740:00 - 52765:00

nobody ever writes anything and like,

## 52765:00 - 52795:00

you know, any code and it's just specs.

## 52795:00 - 52810:00

I think it's going to be much more like,

## 52810:00 - 52840:00

okay, we've set up our coding agent to

## 52840:00 - 52880:00

be really good at like previewing the

## 52880:00 - 52910:00

build or like at running tests. Maybe

## 52910:00 - 52930:00

that's the first part, right? That most

## 52930:00 - 52955:00

people have set up. And it's like, okay,

## 52955:00 - 52985:00

now we've set it up so that it can like

## 52985:00 - 53020:00

execute the build and it can like see

## 53020:00 - 53045:00

the results of its own changes, but you

## 53045:00 - 53065:00

know, we haven't yet built a good

## 53065:00 - 53100:00

integration harness so that it can like

## 53100:00 - 53115:00

in the case of Atlas, like By the way, I

## 53115:00 - 53135:00

don't know if they've done any of this

## 53135:00 - 53155:00

or not. I think they've done a lot of

## 53155:00 - 53175:00

this, but

## 53175:00 - 53205:00

you know, maybe the next stage is like

## 53205:00 - 53240:00

enable it to like load a few sample

## 53240:00 - 53265:00

pages to see how well those work, right?

## 53265:00 - 53285:00

So, then okay, now we're going to like

## 53285:00 - 53315:00

set up set up through that. And I think

## 53315:00 - 53340:00

for some time at least we're going to

## 53340:00 - 53370:00

have humans kind of curating like which

## 53370:00 - 53390:00

of these

## 53390:00 - 53415:00

connectors or systems or components that

## 53415:00 - 53440:00

it the agent needs to be good at talking

## 53440:00 - 53460:00

to.

## 53460:00 - 53485:00

And then, you know, in the future there

## 53485:00 - 53505:00

will be an even greater unlock where

## 53505:00 - 53540:00

Codex tells you how to set it up or

## 53540:00 - 53575:00

maybe sets itself up in a repo. What a

## 53575:00 - 53605:00

wild time to be alive.

## 53605:00 - 53635:00

Wow. I'm curious just the second-order

## 53635:00 - 53655:00

effects of this sort of thing, just how

## 53655:00 - 53690:00

quickly it is to build stuff. What does

## 53690:00 - 53715:00

that do? Does that mean distribution

## 53715:00 - 53745:00

becomes much, much more important? Does

## 53745:00 - 53760:00

it mean

## 53760:00 - 53800:00

uh ideas are just worth a lot more? It's

## 53800:00 - 53840:00

interesting to think about how quick how

## 53840:00 - 53870:00

that changes. I I'm curious what you

## 53870:00 - 53890:00

think. I still don't think ideas are

## 53890:00 - 53930:00

worth as much as

## 53930:00 - 53965:00

maybe some a lot of people think.

## 53965:00 - 53990:00

I think still think execution is really

## 53990:00 - 54005:00

hard, right? Like, you can build

## 54005:00 - 54025:00

something fast, but you still need to

## 54025:00 - 54060:00

execute well on it. Still needs to make

## 54060:00 - 54100:00

sense and be a coherent thing overall.

## 54100:00 - 54140:00

Um yeah, and distribution is massive.

## 54140:00 - 54165:00

Yeah. Just feels like everything else is

## 54165:00 - 54195:00

now more important. Everything that

## 54195:00 - 54225:00

isn't the building piece, which is

## 54225:00 - 54245:00

coming up with the idea, getting to

## 54245:00 - 54290:00

market, profit,

## 54290:00 - 54300:00

all that kind of stuff.

## 54300:00 - 54335:00

>> Yeah. I I think we might have been in

## 54335:00 - 54390:00

this weird temporary phase where

## 54390:00 - 54415:00

you know, for a while like you could you

## 54415:00 - 54445:00

could just it was so hard to build

## 54445:00 - 54490:00

product that

## 54490:00 - 54515:00

you mostly just had to be really good at

## 54515:00 - 54535:00

building product, and it maybe didn't

## 54535:00 - 54565:00

matter if you like had a intimate

## 54565:00 - 54615:00

understanding of a specific customer.

## 54615:00 - 54630:00

Um

## 54630:00 - 54650:00

but now I think we're getting to this

## 54650:00 - 54675:00

point where actually like, if I could

## 54675:00 - 54695:00

only choose like one thing to

## 54695:00 - 54725:00

understand, it would be like really

## 54725:00 - 54760:00

meaningful understanding of like

## 54760:00 - 54785:00

the problems that a certain customer

## 54785:00 - 54805:00

has.

## 54805:00 - 54830:00

Right? If I could only if I could only

## 54830:00 - 54865:00

go in with one like core competency.

## 54865:00 - 54895:00

So, I think that that's

## 54895:00 - 54920:00

that's ultimately still what's going to

## 54920:00 - 54935:00

matter most, right? Like, if you're

## 54935:00 - 54975:00

starting a new company today and you

## 54975:00 - 54990:00

have

## 54990:00 - 55015:00

like a really good understanding and

## 55015:00 - 55040:00

like network of customers that are

## 55040:00 - 55070:00

currently underserved by AI tools, I

## 55070:00 - 55100:00

think you're like you're set.

## 55100:00 - 55125:00

Right? Whereas if you're like good

## 55125:00 - 55145:00

[clears throat] at building like, you

## 55145:00 - 55160:00

know,

## 55160:00 - 55185:00

websites, but you don't have any

## 55185:00 - 55205:00

specific customer to build for, I think

## 55205:00 - 55235:00

you're in in for a much harder time.

## 55235:00 - 55280:00

Bullish on vertical AI startups is what

## 55280:00 - 55300:00

I'm hearing.

## 55300:00 - 55330:00

Yeah, I completely agree. There's like,

## 55330:00 - 55350:00

you know, there's like the general thing

## 55350:00 - 55365:00

that can solve a lot of problems, and

## 55365:00 - 55385:00

then there's like, we're going to solve

## 55385:00 - 55410:00

presentations incredibly well, and we're

## 55410:00 - 55430:00

going to understand the presentation

## 55430:00 - 55470:00

problem uh better than anyone, and we're

## 55470:00 - 55500:00

going to uh

## 55500:00 - 55525:00

plug into your workflows and and all

## 55525:00 - 55545:00

these other things that matter for a

## 55545:00 - 55575:00

very specific problem.

## 55575:00 - 55605:00

Okay. Incredible.

## 55605:00 - 55655:00

When you think about progress on Codex,

## 55655:00 - 55680:00

I imagine you have a bunch of evals, and

## 55680:00 - 55710:00

there's all these public benchmarks.

## 55710:00 - 55730:00

What's something you look at to tell

## 55730:00 - 55755:00

you, okay, we're making really good

## 55755:00 - 55775:00

progress? I imagine it's not going to be

## 55775:00 - 55795:00

the one thing, but what do you focus on?

## 55795:00 - 55810:00

What's like something you're trying to

## 55810:00 - 55860:00

push? What's like a KPI or two? One of

## 55860:00 - 55885:00

the things that I'm constantly reminding

## 55885:00 - 55915:00

myself of is that

## 55915:00 - 55955:00

a tool like Codex sort of naturally is a

## 55955:00 - 55970:00

tool that you would you know, become a

## 55970:00 - 55995:00

power user of.

## 55995:00 - 56025:00

Right? And so, we can accidentally spend

## 56025:00 - 56045:00

a lot of our time thinking about

## 56045:00 - 56070:00

features that are like very deep in the

## 56070:00 - 56100:00

user adoption journey.

## 56100:00 - 56145:00

Um and so, we can kind of end up

## 56145:00 - 56175:00

over-solving for that. And so, I think

## 56175:00 - 56195:00

it's like just critically important to

## 56195:00 - 56225:00

like go look at like your like D7

## 56225:00 - 56245:00

retention.

## 56245:00 - 56275:00

Right? Just go try the product. Like,

## 56275:00 - 56305:00

sign up from scratch again.

## 56305:00 - 56335:00

Um I have a few too many like ChatGPT

## 56335:00 - 56370:00

Pro accounts that I've just like

## 56370:00 - 56400:00

in order to maximally correctly dog food

## 56400:00 - 56425:00

like sign up for on my Gmail, and they

## 56425:00 - 56450:00

charge me like 200 bucks a month. I need

## 56450:00 - 56475:00

to expense those.

## 56475:00 - 56495:00

But uh

## 56495:00 - 56510:00

uh

## 56510:00 - 56540:00

you know, like I think just like

## 56540:00 - 56570:00

the feeling of being a user and the

## 56570:00 - 56595:00

early retention stats are still like

## 56595:00 - 56635:00

super important for us because you you

## 56635:00 - 56670:00

know, as much as this category is is

## 56670:00 - 56690:00

taking off, I think we're still in the

## 56690:00 - 56715:00

very early days of like people using

## 56715:00 - 56730:00

them.

## 56730:00 - 56745:00

Um

## 56745:00 - 56785:00

another thing that we do that

## 56785:00 - 56815:00

that may might be I think we might be

## 56815:00 - 56845:00

the most

## 56845:00 - 56880:00

like user feedback {slash} social media

## 56880:00 - 56925:00

pilled team out there in this space

## 56925:00 - 56960:00

is like a few of us are like constantly

## 56960:00 - 56980:00

on Reddit

## 56980:00 - 57000:00

and Twitter.

## 57000:00 - 57035:00

And you know, there's uh there's praise

## 57035:00 - 57050:00

up there, and there's a lot of

## 57050:00 - 57070:00

complaints, but we take the complaints

## 57070:00 - 57110:00

like very seriously and look at them.

## 57110:00 - 57130:00

And I think that

## 57130:00 - 57155:00

again, because you can use a coding

## 57155:00 - 57190:00

agent for so many different things,

## 57190:00 - 57225:00

um it often is like kind of broken in

## 57225:00 - 57255:00

many sort of ways for like specific

## 57255:00 - 57280:00

behaviors.

## 57280:00 - 57305:00

Um and so, we we actually monitor a lot

## 57305:00 - 57335:00

just like what the vibes are on social

## 57335:00 - 57385:00

media pretty often. Especially I think

## 57385:00 - 57435:00

for for Twitter X, um

## 57435:00 - 57470:00

it's a little bit more hypey.

## 57470:00 - 57500:00

And then Reddit is a little more

## 57500:00 - 57545:00

negative, but real actually.

## 57545:00 - 57570:00

Um so,

## 57570:00 - 57590:00

I've started increasingly paying

## 57590:00 - 57615:00

attention to like how people are talking

## 57615:00 - 57650:00

about using Codex on Reddit actually.

## 57650:00 - 57680:00

This is uh important for people to know.

## 57680:00 - 57710:00

Which subreddits do you check most? Is

## 57710:00 - 57745:00

there like an r/Codex or I mean, the

## 57745:00 - 57765:00

algorithm's pretty good at surfacing

## 57765:00 - 57810:00

stuff, but like r/Codex is is there.

## 57810:00 - 57850:00

Okay. I'll take. Very interesting. And

## 57850:00 - 57875:00

then uh if people tag you on Twitter,

## 57875:00 - 57905:00

you still see that, but maybe not as

## 57905:00 - 57935:00

powerful as seeing it on Reddit.

## 57935:00 - 57950:00

Well, yeah, the interesting Well, the

## 57950:00 - 57970:00

thing with Twitter is it's a little bit

## 57970:00 - 57995:00

more one-to-one even if it's like in

## 57995:00 - 58015:00

public. Whereas like with Reddit,

## 58015:00 - 58030:00

there's a like really good upvoting

## 58030:00 - 58065:00

mechanics, and like maybe most people

## 58065:00 - 58105:00

are still not bots. Unclear.

## 58105:00 - 58130:00

Um so, you get you get like good signal

## 58130:00 - 58145:00

on what matters and what other people

## 58145:00 - 58175:00

think. So,

## 58175:00 - 58205:00

interestingly Atlas, I want to talk

## 58205:00 - 58225:00

about that briefly.

## 58225:00 - 58260:00

You guys launched Atlas. I tweeted

## 58260:00 - 58300:00

actually that I tried Atlas, and then

## 58300:00 - 58350:00

I I don't love the AI-only

## 58350:00 - 58380:00

search experience. I just like I just

## 58380:00 - 58410:00

want to Google sometimes or whatever.

## 58410:00 - 58435:00

Like, just waiting for the AI to give me

## 58435:00 - 58455:00

an answer. I'm like, I don't want to And

## 58455:00 - 58475:00

there was no way to switch, so I just

## 58475:00 - 58505:00

tweeted, "Hey, I'm I'm switching back. I

## 58505:00 - 58535:00

don't It's not a great." And I feel like

## 58535:00 - 58575:00

I made some PMs at OpenAI sad. And I saw

## 58575:00 - 58605:00

someone tweet, "Okay, we have this now."

## 58605:00 - 58625:00

Which I imagine was always part of the

## 58625:00 - 58650:00

plan. It's probably an example of we

## 58650:00 - 58675:00

just ship We got to ship stuff. See how

## 58675:00 - 58695:00

people use it, and then we figure it

## 58695:00 - 58710:00

out.

## 58710:00 - 58750:00

Uh so, I guess one is that

## 58750:00 - 58765:00

I don't know, is there anything there?

## 58765:00 - 58780:00

And two, I'm just curious, why are you

## 58780:00 - 58820:00

guys building a web browser? So, I I

## 58820:00 - 58850:00

worked on Atlas for a bit. Um I don't

## 58850:00 - 58895:00

work on it now. Um but

## 58895:00 - 58915:00

you know, like the a bit of the

## 58915:00 - 58940:00

narrative here for for me to tell my

## 58940:00 - 58960:00

story a bit was like, I was working on

## 58960:00 - 58990:00

this like screen sharing like pair

## 58990:00 - 59025:00

programming startup. Right? And then we

## 59025:00 - 59050:00

joined OpenAI.

## 59050:00 - 59070:00

And so, the idea was really to build a

## 59070:00 - 59110:00

contextual desktop assistant.

## 59110:00 - 59135:00

And the reason I believe that's so

## 59135:00 - 59160:00

important is because

## 59160:00 - 59185:00

I think that

## 59185:00 - 59210:00

it's really annoying to have to give all

## 59210:00 - 59235:00

your context to an assistant and then to

## 59235:00 - 59270:00

figure out how it can help you.

## 59270:00 - 59295:00

Right? And so, if it could just like

## 59295:00 - 59320:00

understand what you were trying to do,

## 59320:00 - 59360:00

then it could maximally accelerate you.

## 59360:00 - 59400:00

Um and so, I I I would you know, I still

## 59400:00 - 59420:00

think of Codex actually as like a

## 59420:00 - 59455:00

contextual assistant. Um from a little

## 59455:00 - 59475:00

bit of a different angle, like starting

## 59475:00 - 59500:00

with coding tasks.

## 59500:00 - 59535:00

But um

## 59535:00 - 59555:00

the

## 59555:00 - 59580:00

some of the some of the thinking at

## 59580:00 - 59605:00

least for me personally, I can't speak

## 59605:00 - 59645:00

for the whole product, but it was that

## 59645:00 - 59695:00

a lot of work is done in the web, and if

## 59695:00 - 59720:00

we could build a browser, then we could

## 59720:00 - 59755:00

be contextual for you, but in a much

## 59755:00 - 59785:00

more first-class way. We weren't hacking

## 59785:00 - 59815:00

like other desktop software which have

## 59815:00 - 59865:00

like very varied support for for like

## 59865:00 - 59880:00

what content they're rendering to the

## 59880:00 - 59910:00

accessibility tree. Uh, we wouldn't be

## 59910:00 - 59935:00

relying on screenshots, which are a

## 59935:00 - 59970:00

little bit slower and unreliable.

## 59970:00 - 60000:00

Instead, we we we could like be in the

## 60000:00 - 60025:00

rendering engine, right? And like

## 60025:00 - 60060:00

extract whatever we needed to to help

## 60060:00 - 60080:00

you. Um,

## 60080:00 - 60115:00

and also, I like to think of like, you

## 60115:00 - 60145:00

know, in video games, like, I don't know

## 60145:00 - 60180:00

if you've played like, I don't know, say

## 60180:00 - 60210:00

Halo, right? Like, you walk up to an

## 60210:00 - 60230:00

object. I mean, this is true for many

## 60230:00 - 60260:00

games. You press Now, it's been a long

## 60260:00 - 60310:00

time. This is embarrassing. Press X

## 60310:00 - 60345:00

and it just does the right thing, right?

## 60345:00 - 60365:00

And I was one of those guys who always

## 60365:00 - 60385:00

read the instruction manual for every

## 60385:00 - 60410:00

video game that I bought. And I remember

## 60410:00 - 60435:00

the first time I read about a contextual

## 60435:00 - 60450:00

action and I just thought it was like

## 60450:00 - 60495:00

this really cool idea. And, uh,

## 60495:00 - 60525:00

you know, the

## 60525:00 - 60545:00

the thing about a contextual action is

## 60545:00 - 60565:00

we need to know what you are attempting

## 60565:00 - 60600:00

to do. We have a little bit of context,

## 60600:00 - 60620:00

and then we can

## 60620:00 - 60665:00

and then we can help. Uh, and I think

## 60665:00 - 60700:00

this is critically important because,

## 60700:00 - 60720:00

you know, imagine this world that we

## 60720:00 - 60750:00

reach, right? Where where we have agents

## 60750:00 - 60775:00

that are helping you thousands of times

## 60775:00 - 60800:00

per day.

## 60800:00 - 60835:00

Um, imagine if the only way we could

## 60835:00 - 60855:00

tell you that we helped you is if we

## 60855:00 - 60905:00

could like push notify you.

## 60905:00 - 60930:00

So, you get a thousand push

## 60930:00 - 60960:00

notifications a day of an AI saying

## 60960:00 - 60980:00

like, "Hey, I did this thing. Do you

## 60980:00 - 61020:00

like it?" It gets super annoying, right?

## 61020:00 - 61050:00

Whereas, imagine going back to software

## 61050:00 - 61080:00

engineering, like, I was looking at a

## 61080:00 - 61115:00

dashboard and I noticed some like key

## 61115:00 - 61160:00

metric had like gone down.

## 61160:00 - 61190:00

And, you know, at that point in time, an

## 61190:00 - 61225:00

AI could like maybe go take a look and

## 61225:00 - 61250:00

then surface the fact that it has an

## 61250:00 - 61275:00

opinion on why this metric went down and

## 61275:00 - 61310:00

maybe a fix right there right when I'm

## 61310:00 - 61335:00

looking at the dashboard. Right? That

## 61335:00 - 61360:00

would be like that would much more keep

## 61360:00 - 61385:00

me in flow

## 61385:00 - 61420:00

and enable the agents to take action on

## 61420:00 - 61450:00

like many more things. So, in my mind,

## 61450:00 - 61470:00

like,

## 61470:00 - 61495:00

part of why I'm excited for us to have a

## 61495:00 - 61535:00

browser is that I think we have then

## 61535:00 - 61595:00

like much more context around like what

## 61595:00 - 61620:00

we should help with. Users have much

## 61620:00 - 61655:00

more control over what they want us to

## 61655:00 - 61675:00

look at. It's like, "Hey, if you want to

## 61675:00 - 61700:00

open If you want us to like take action

## 61700:00 - 61720:00

on something, you can open it in your AI

## 61720:00 - 61745:00

browser. If you don't, then you can open

## 61745:00 - 61765:00

it in your other browser." Right? So,

## 61765:00 - 61780:00

like really clear control and

## 61780:00 - 61830:00

boundaries. And then, we have the

## 61830:00 - 61855:00

ability to build UX that's like mixed

## 61855:00 - 61890:00

initiative so that we can surface

## 61890:00 - 61915:00

contextual actions to you like at the

## 61915:00 - 61945:00

time that they're helpful, as opposed to

## 61945:00 - 61970:00

just like randomly notifying you.

## 61970:00 - 61995:00

Hearing the vision for Codex being the

## 61995:00 - 62030:00

super assistant. It's not just there to

## 62030:00 - 62060:00

code for you. It's trying to do a lot

## 62060:00 - 62085:00

for you as a teammate and as this kind

## 62085:00 - 62115:00

of super teammate that makes you awesome

## 62115:00 - 62160:00

at work. So, I get this.

## 62160:00 - 62195:00

Speaking of that, are there other

## 62195:00 - 62220:00

non-engineering

## 62220:00 - 62255:00

common use cases for Codex? Just ways

## 62255:00 - 62280:00

that non-engineers We talked about it,

## 62280:00 - 62305:00

you know, designers prototyping,

## 62305:00 - 62340:00

building stuff. Are there any kind of

## 62340:00 - 62370:00

other unexpected ways people are using

## 62370:00 - 62405:00

Codex that aren't engineers? I mean,

## 62405:00 - 62435:00

there's a load of a load of unexpected

## 62435:00 - 62480:00

ways, but I think like most of what

## 62480:00 - 62515:00

we're seeing like real traction with

## 62515:00 - 62540:00

people using things are still for now

## 62540:00 - 62575:00

like very like

## 62575:00 - 62610:00

I would say coding adjacent or like sort

## 62610:00 - 62645:00

of tech-oriented places where there's

## 62645:00 - 62685:00

like a mature ecosystem. Um, or, you

## 62685:00 - 62705:00

know, maybe you're doing data data

## 62705:00 - 62745:00

analysis or something like that. I

## 62745:00 - 62780:00

personally am expecting that we're going

## 62780:00 - 62820:00

to see a lot more of that over time. Um,

## 62820:00 - 62840:00

but for now, like, we're keeping the

## 62840:00 - 62865:00

team like very focused on just coding

## 62865:00 - 62885:00

for now cuz there's so much more work to

## 62885:00 - 62920:00

do. For people that are thinking about

## 62920:00 - 62960:00

trying out Codex, is there like a

## 62960:00 - 62980:00

Does it work for all kinds of code

## 62980:00 - 63020:00

bases? Uh, what what code does it

## 63020:00 - 63060:00

support? If you're like, I don't know,

## 63060:00 - 63095:00

SAP, can you add Codex and start

## 63095:00 - 63125:00

building things? What's kind of like the

## 63125:00 - 63155:00

sweet spot? Where does it start to not

## 63155:00 - 63205:00

be amazing yet? This I'm really glad you

## 63205:00 - 63230:00

asked this question, actually, because

## 63230:00 - 63260:00

the best way to try Codex is to give it

## 63260:00 - 63290:00

your hardest tasks,

## 63290:00 - 63320:00

which is a little different than some of

## 63320:00 - 63365:00

the other coding agents. Like, you know,

## 63365:00 - 63385:00

some tools you might think, "Okay, let

## 63385:00 - 63420:00

me like start easy or just like, you

## 63420:00 - 63455:00

know, like vibe code something random

## 63455:00 - 63490:00

and decide if I like the tool." Whereas,

## 63490:00 - 63530:00

like, we're really building Codex to be

## 63530:00 - 63555:00

the like professional tool that you can

## 63555:00 - 63595:00

give your like hardest problems to.

## 63595:00 - 63620:00

Um, and you know, that writes like

## 63620:00 - 63650:00

high-quality code in your like enormous

## 63650:00 - 63685:00

code base that is in fact not perfect

## 63685:00 - 63705:00

right now.

## 63705:00 - 63720:00

So, yeah, I think if you're going to try

## 63720:00 - 63760:00

Codex, you want to try it on like a real

## 63760:00 - 63805:00

task that you have, and not necessarily

## 63805:00 - 63825:00

like dumb that task down to something

## 63825:00 - 63875:00

that's like trivial, but actually like,

## 63875:00 - 63900:00

you know, like, a good one would be like

## 63900:00 - 63920:00

you have a hard bug and you don't know

## 63920:00 - 63945:00

what what's causing that bug and you ask

## 63945:00 - 63970:00

Codex to like help figure that out. Or

## 63970:00 - 63995:00

like to implement that, you know, the

## 63995:00 - 64030:00

fix. I love that answer. Just give it

## 64030:00 - 64060:00

your hardest problem. I will say like,

## 64060:00 - 64080:00

you know, if you if you're like, "Hey,

## 64080:00 - 64100:00

okay, but well, the hardest problem I

## 64100:00 - 64130:00

have is that I need to build like a new

## 64130:00 - 64155:00

unicorn business." Like, obviously,

## 64155:00 - 64175:00

that, you know,

## 64175:00 - 64195:00

it's not going to work.

## 64195:00 - 64245:00

Uh, not yet. So, I think it's like give

## 64245:00 - 64275:00

it like the hardest problem, but

## 64275:00 - 64320:00

something that is still like one like

## 64320:00 - 64360:00

question, right? Or one task, um, to

## 64360:00 - 64380:00

start. That's if you're testing, and

## 64380:00 - 64400:00

then over time, you can learn how to use

## 64400:00 - 64430:00

it for like bigger things. Yeah, what

## 64430:00 - 64455:00

languages does does it support?

## 64455:00 - 64485:00

Basically, the way we've trained Codex

## 64485:00 - 64505:00

is like there's a distribution of

## 64505:00 - 64530:00

languages that we support, and it's like

## 64530:00 - 64565:00

fairly aligned with like the frequency

## 64565:00 - 64600:00

of these languages in the world. So,

## 64600:00 - 64620:00

unless you're writing some like very

## 64620:00 - 64650:00

esoteric language or like some private

## 64650:00 - 64670:00

language, it should do fine in your

## 64670:00 - 64700:00

language. If someone was just getting

## 64700:00 - 64740:00

started, is there a tip you could share

## 64740:00 - 64765:00

to help them be successful? Like, if you

## 64765:00 - 64800:00

could just whisper a little tip into

## 64800:00 - 64820:00

someone just setting up Codex for the

## 64820:00 - 64850:00

first time to help them have a really

## 64850:00 - 64865:00

good time.

## 64865:00 - 64895:00

What's something you'd whisper?

## 64895:00 - 64920:00

I might say try a few things in

## 64920:00 - 64940:00

parallel.

## 64940:00 - 64960:00

Right? So, you could try giving it a

## 64960:00 - 65000:00

hard task. Um,

## 65000:00 - 65025:00

maybe ask it to understand the code

## 65025:00 - 65075:00

base. Uh, formulate a plan with it

## 65075:00 - 65110:00

around an idea that you have, and kind

## 65110:00 - 65130:00

of build your way up from there. And

## 65130:00 - 65165:00

like, sort of the meta idea here is it's

## 65165:00 - 65200:00

again, it's like you're building trust

## 65200:00 - 65225:00

with a new teammate.

## 65225:00 - 65250:00

Right? And so, like, you wouldn't go to

## 65250:00 - 65270:00

a new teammate and just give them like,

## 65270:00 - 65295:00

"Hey, do this thing. Here's zero

## 65295:00 - 65320:00

context." You would start by like first

## 65320:00 - 65350:00

making sure they understand the code

## 65350:00 - 65375:00

base, and then you would like maybe

## 65375:00 - 65400:00

align on a plan and approach, and then

## 65400:00 - 65420:00

you would have them go off and do it bit

## 65420:00 - 65435:00

by bit.

## 65435:00 - 65455:00

Right? And I think if you use Codex in

## 65455:00 - 65480:00

that way, you'll just sort of naturally

## 65480:00 - 65500:00

start to understand like the different

## 65500:00 - 65535:00

ways of prompting it because it is it's

## 65535:00 - 65575:00

a super powerful like agent and model,

## 65575:00 - 65600:00

but it is it is a little bit different

## 65600:00 - 65635:00

to prompt Codex than other models. Just

## 65635:00 - 65680:00

a couple more questions. One, we touched

## 65680:00 - 65710:00

on this a little bit.

## 65710:00 - 65755:00

As AI does more and more coding, there's

## 65755:00 - 65775:00

always this question of should I learn

## 65775:00 - 65805:00

to code? And what do I should I spend

## 65805:00 - 65830:00

time doing this sort of thing?

## 65830:00 - 65870:00

For people that are trying to figure out

## 65870:00 - 65890:00

what to do with their career, especially

## 65890:00 - 65915:00

if they're into software engineering,

## 65915:00 - 65945:00

computer science, do you think there are

## 65945:00 - 65980:00

specific elements of computer science

## 65980:00 - 66015:00

that are more and more important to lean

## 66015:00 - 66050:00

into? Maybe things they don't need to

## 66050:00 - 66065:00

worry about. Like, what do you think

## 66065:00 - 66110:00

people should be leaning into skill-wise

## 66110:00 - 66145:00

in as this becomes more and more of a

## 66145:00 - 66185:00

thing in our workplace?

## 66185:00 - 66215:00

I think there's like a couple

## 66215:00 - 66255:00

angles you could go at this from.

## 66255:00 - 66300:00

Um, I think the

## 66300:00 - 66340:00

Well, the easiest one to think of at

## 66340:00 - 66395:00

least is just like be a doer of things.

## 66395:00 - 66430:00

Um, I think that, you know, with coding

## 66430:00 - 66470:00

agents um, getting better and better

## 66470:00 - 66525:00

over time, it's just what you can do as

## 66525:00 - 66555:00

even like someone in college or a new

## 66555:00 - 66585:00

grad is just like so much more than what

## 66585:00 - 66620:00

that was before. And so, I think you

## 66620:00 - 66640:00

just want to be taking advantage of

## 66640:00 - 66660:00

that.

## 66660:00 - 66685:00

And definitely when I'm looking at like

## 66685:00 - 66710:00

hiring folks who are earlier career,

## 66710:00 - 66730:00

it's like definitely something that I

## 66730:00 - 66760:00

think about is how

## 66760:00 - 66790:00

how productive are they using the latest

## 66790:00 - 66805:00

tools?

## 66805:00 - 66825:00

Right? They should be like super

## 66825:00 - 66850:00

productive. And if you think of it in

## 66850:00 - 66880:00

that way, they actually have like less

## 66880:00 - 66915:00

of a handicap than before versus a a

## 66915:00 - 66950:00

more senior career person because,

## 66950:00 - 66975:00

you know, the divide is actually getting

## 66975:00 - 66990:00

smaller because they've got these

## 66990:00 - 67020:00

amazing coding agents now. Um, so,

## 67020:00 - 67040:00

that's one thing, which is just like, I

## 67040:00 - 67080:00

guess the thing the advice is just like

## 67080:00 - 67105:00

learn about whatever you want, but just

## 67105:00 - 67130:00

make sure you spend time doing things,

## 67130:00 - 67155:00

not just like fulfilling homework

## 67155:00 - 67185:00

assignments, I guess.

## 67185:00 - 67210:00

I think the other side of it, though, is

## 67210:00 - 67250:00

that it's still deeply worth

## 67250:00 - 67295:00

understanding like what makes a good

## 67295:00 - 67340:00

like overall software system. So, I

## 67340:00 - 67370:00

still think that like skills like really

## 67370:00 - 67410:00

strong systems engineering skills

## 67410:00 - 67455:00

or even like really effective like

## 67455:00 - 67480:00

communication and collaboration with

## 67480:00 - 67510:00

your team. Skills like that, I think,

## 67510:00 - 67530:00

are are important. They're going to

## 67530:00 - 67570:00

continue to matter for for quite some

## 67570:00 - 67590:00

time. Like, I don't think it's going to

## 67590:00 - 67640:00

be like all of a sudden, uh,

## 67640:00 - 67665:00

the AI coding agents are just able to

## 67665:00 - 67700:00

build like perfect systems without your

## 67700:00 - 67725:00

help. I think it's going to look much

## 67725:00 - 67765:00

more gradual, where it's like,

## 67765:00 - 67805:00

"Okay, we have these AI coding agents.

## 67805:00 - 67840:00

They're able to validate their work."

## 67840:00 - 67860:00

It's still important and like that for

## 67860:00 - 67895:00

example, like, thinking of an engineer

## 67895:00 - 67915:00

who was working on Atlas since we were

## 67915:00 - 67950:00

talking about it, he set up Codex so

## 67950:00 - 67975:00

that it can like verify its own work,

## 67975:00 - 68000:00

which is a little bit non-trivial

## 68000:00 - 68015:00

because of the the nature of the Atlas

## 68015:00 - 68040:00

product. So, the way that he did that

## 68040:00 - 68065:00

was he actually prompted Codex like,

## 68065:00 - 68095:00

"Hey, why can't you verify your work?

## 68095:00 - 68130:00

Fix it." And like did that on a loop.

## 68130:00 - 68160:00

Right? And so,

## 68160:00 - 68195:00

you still like at various phases are

## 68195:00 - 68210:00

going to want a human in the loop to

## 68210:00 - 68245:00

like help configure the coding agent to

## 68245:00 - 68295:00

be effective. And so, I think like you

## 68295:00 - 68315:00

still want to be able to reason about

## 68315:00 - 68345:00

that. So, maybe it's like less important

## 68345:00 - 68370:00

that you can like

## 68370:00 - 68400:00

type really fast and like you understand

## 68400:00 - 68430:00

exactly how to write Not that anyone

## 68430:00 - 68455:00

writes a, you know, for each loop or

## 68455:00 - 68500:00

something, right? But, it is

## 68500:00 - 68515:00

or, you know, you don't need to know how

## 68515:00 - 68540:00

to implement like a specific algorithm.

## 68540:00 - 68555:00

But, I think you need to be able to

## 68555:00 - 68575:00

reason about the different systems and

## 68575:00 - 68605:00

like what makes like effective a

## 68605:00 - 68635:00

software engineering team effective. So,

## 68635:00 - 68655:00

I think that's uh the other really

## 68655:00 - 68675:00

important thing. And then like maybe the

## 68675:00 - 68720:00

last angle that you could take is

## 68720:00 - 68755:00

I think if you're on the frontier of

## 68755:00 - 68795:00

knowledge for a given thing,

## 68795:00 - 68815:00

I still think that's like deeply

## 68815:00 - 68835:00

interesting to go down. Partially

## 68835:00 - 68870:00

because that knowledge is still going to

## 68870:00 - 68900:00

be like

## 68900:00 - 68915:00

uh,

## 68915:00 - 68935:00

you know, agents aren't going to be as

## 68935:00 - 68970:00

good at that, but also partially because

## 68970:00 - 68990:00

I think that like by trying to advance

## 68990:00 - 69015:00

the frontier of a specific thing, you'll

## 69015:00 - 69060:00

actually like end up like being forced

## 69060:00 - 69090:00

to take advantage of coding agents and

## 69090:00 - 69130:00

like using them to accelerate your own

## 69130:00 - 69160:00

workflows as you go. What's an example

## 69160:00 - 69175:00

that when you when you talk about being

## 69175:00 - 69200:00

at the frontier of something? Codex

## 69200:00 - 69225:00

writes a lot of the code that helps like

## 69225:00 - 69260:00

manage its training runs, the key

## 69260:00 - 69280:00

infrastructure.

## 69280:00 - 69315:00

Uh, you know, we move pretty fast, and

## 69315:00 - 69360:00

so we have a Codex code review is like

## 69360:00 - 69380:00

catching a lot of mistakes. It's

## 69380:00 - 69395:00

actually caught some like pretty

## 69395:00 - 69430:00

interesting configuration mistakes.

## 69430:00 - 69460:00

And, uh, you know, we're starting to see

## 69460:00 - 69495:00

glimpses of the future where

## 69495:00 - 69525:00

we're actually starting to have Codex

## 69525:00 - 69555:00

even like be on call for its own

## 69555:00 - 69595:00

training, which is pretty interesting.

## 69595:00 - 69630:00

Um so, there's lots there.

## 69630:00 - 69650:00

Uh wait, what does that mean to be on

## 69650:00 - 69670:00

call for its own training? So, it's

## 69670:00 - 69690:00

running, it's training, and it's like,

## 69690:00 - 69720:00

"Oh, something broke. Someone needs" And

## 69720:00 - 69745:00

it it does it like alert people or it's

## 69745:00 - 69760:00

like, "Here, I'm going to fix the

## 69760:00 - 69795:00

problem and re- Yeah, this is an early

## 69795:00 - 69830:00

idea that we're like figuring out. But

## 69830:00 - 69855:00

the basic idea is that, you know, during

## 69855:00 - 69875:00

a training run, there's like a bunch of

## 69875:00 - 69905:00

graphs that like today like humans are

## 69905:00 - 69920:00

looking at and it's like really

## 69920:00 - 69960:00

important to like look at those. Um we

## 69960:00 - 69980:00

call this babysitting.

## 69980:00 - 70005:00

Because it's very expensive to train, I

## 70005:00 - 70040:00

imagine, and very important to move fast

## 70040:00 - 70070:00

and Exactly. And there's a lot of

## 70070:00 - 70100:00

there's a lot of systems underlying uh

## 70100:00 - 70125:00

the training run. And so, like a system

## 70125:00 - 70150:00

could go down or there could be an error

## 70150:00 - 70180:00

somewhere that gets introduced. And so,

## 70180:00 - 70215:00

we might need to like fix it or pause

## 70215:00 - 70235:00

things or I don't know, there's lots of

## 70235:00 - 70270:00

actions we might need to take. And so,

## 70270:00 - 70295:00

basically having Codex like run on a

## 70295:00 - 70335:00

loop to like evaluate how those charts

## 70335:00 - 70360:00

are moving over time,

## 70360:00 - 70390:00

um this sort of this idea that we have

## 70390:00 - 70415:00

to like how to enable us to like train

## 70415:00 - 70445:00

like way more efficiently. I love that.

## 70445:00 - 70480:00

This is very much along the lines of

## 70480:00 - 70515:00

this is the future of agents. It's Codex

## 70515:00 - 70540:00

isn't just for building code, right?

## 70540:00 - 70580:00

It's it's a lot more than that.

## 70580:00 - 70595:00

Yeah.

## 70595:00 - 70650:00

Okay. Last question. Uh being at OpenAI,

## 70650:00 - 70690:00

uh I can't not ask about your AGI

## 70690:00 - 70720:00

timeline and how far you think we are

## 70720:00 - 70745:00

from AGI. I know this isn't what you

## 70745:00 - 70760:00

work on,

## 70760:00 - 70800:00

but there's a lot of opinions, a lot of

## 70800:00 - 70840:00

I don't know, timelines. How far do you

## 70840:00 - 70860:00

think that we are from a

## 70860:00 - 70925:00

uh humanly human version of AI, whatever

## 70925:00 - 70980:00

that means to you? For me, I think that

## 70980:00 - 71005:00

it's a little bit about like when do we

## 71005:00 - 71035:00

see the acceleration curves kind of go

## 71035:00 - 71050:00

like this or I don't know which way I'm

## 71050:00 - 71070:00

mirrored here.

## 71070:00 - 71100:00

Right? When do we see the hockey stick?

## 71100:00 - 71150:00

And I think that the current limiting

## 71150:00 - 71175:00

factor, I mean, there's many, but I

## 71175:00 - 71195:00

think a current underappreciated

## 71195:00 - 71225:00

limiting factor is like literally human

## 71225:00 - 71275:00

typing speed or human multitasking speed

## 71275:00 - 71315:00

on like writing prompts.

## 71315:00 - 71335:00

Right? And like, you know, you were

## 71335:00 - 71350:00

talking about it's like you can have an

## 71350:00 - 71370:00

agent like watch all the work you're

## 71370:00 - 71405:00

doing, but if you don't have the agent

## 71405:00 - 71440:00

uh also validating its work,

## 71440:00 - 71460:00

then you're still bottlenecked on like,

## 71460:00 - 71495:00

can you go review all that code, right?

## 71495:00 - 71560:00

So, my view is that we need to um

## 71560:00 - 71600:00

unblock those productivity loops from

## 71600:00 - 71625:00

like humans having to prompt and humans

## 71625:00 - 71650:00

having to like about manually evaluate

## 71650:00 - 71680:00

all the work. And so, if we can like

## 71680:00 - 71720:00

rebuild systems to let the agent like be

## 71720:00 - 71745:00

default useful,

## 71745:00 - 71790:00

we'll start unlocking hockey sticks.

## 71790:00 - 71805:00

Unfortunately, I don't think that's

## 71805:00 - 71830:00

going to be binary. I think it's going

## 71830:00 - 71845:00

to be very dependent on what you're

## 71845:00 - 71870:00

building, right? So, like I would

## 71870:00 - 71895:00

imagine that like next year, if you're a

## 71895:00 - 71925:00

startup,

## 71925:00 - 71950:00

and you're building a new new pieces

## 71950:00 - 71965:00

like, you know, some new app or

## 71965:00 - 71985:00

something,

## 71985:00 - 72010:00

it'll be possible for you to set it up

## 72010:00 - 72030:00

on a stack where agents are like much

## 72030:00 - 72070:00

more self-sufficient

## 72070:00 - 72105:00

than not, right? But now, let's say I I

## 72105:00 - 72130:00

don't know, you mentioned SAP, right?

## 72130:00 - 72155:00

Let's say you work in SAP. Like they

## 72155:00 - 72180:00

have many like complex systems and

## 72180:00 - 72195:00

they're not going to be able to just

## 72195:00 - 72220:00

like get the agent to be self-sufficient

## 72220:00 - 72250:00

overnight in those systems. So, they're

## 72250:00 - 72275:00

going to have to slowly like maybe

## 72275:00 - 72320:00

replace systems or update systems

## 72320:00 - 72345:00

to allow the agent to like handle more

## 72345:00 - 72375:00

of the work end to end.

## 72375:00 - 72390:00

And so,

## 72390:00 - 72420:00

basically my sort of long answer to your

## 72420:00 - 72450:00

question, maybe boring answer, is that I

## 72450:00 - 72470:00

think starting next year, we're going to

## 72470:00 - 72510:00

see like early adopters like starting to

## 72510:00 - 72550:00

like hockey stick their productivity.

## 72550:00 - 72575:00

Um and then over the years that follow,

## 72575:00 - 72595:00

we're going to see larger and larger

## 72595:00 - 72615:00

companies like hockey stick their

## 72615:00 - 72660:00

productivity. And then somewhere in that

## 72660:00 - 72695:00

fuzzy middle is like when that hockey

## 72695:00 - 72730:00

sticking will be like

## 72730:00 - 72765:00

flowing back into the AI labs and that's

## 72765:00 - 72800:00

when we'll we'll basically be at the AGI

## 72800:00 - 72825:00

tier. I love this answer. It's very

## 72825:00 - 72860:00

practical and it's something that comes

## 72860:00 - 72890:00

up a lot on this podcast, just like the

## 72890:00 - 72920:00

time to review all the things AI is

## 72920:00 - 72950:00

doing is really annoying and a big

## 72950:00 - 72975:00

bottleneck. I love that you're working

## 72975:00 - 73005:00

on this because it's one thing to just

## 73005:00 - 73040:00

make coding much more efficient and do

## 73040:00 - 73075:00

that for people, it's another to

## 73075:00 - 73105:00

take care of that final step of, okay,

## 73105:00 - 73135:00

is this actually great? And that's so

## 73135:00 - 73170:00

interesting that your sense is that's

## 73170:00 - 73195:00

the limiting factor. It comes back to

## 73195:00 - 73225:00

your earlier point of

## 73225:00 - 73265:00

even if AI did not advance anymore, we

## 73265:00 - 73305:00

have so much more potential to unlock if

## 73305:00 - 73330:00

we uh

## 73330:00 - 73370:00

as we learn to use it more effectively.

## 73370:00 - 73395:00

Uh so, that is a really unique answer.

## 73395:00 - 73420:00

I've never heard that perspective on

## 73420:00 - 73455:00

what is the big unlock. Human typing

## 73455:00 - 73480:00

speed to review basically what AI is

## 73480:00 - 73545:00

doing for us. Mhm. So good. Okay. Uh

## 73545:00 - 73585:00

Alexander, we covered a lot of ground.

## 73585:00 - 73610:00

Is there anything that we haven't

## 73610:00 - 73635:00

covered? Is there anything you wanted to

## 73635:00 - 73680:00

share, maybe double down on before we

## 73680:00 - 73715:00

get to our very exciting lightning

## 73715:00 - 73730:00

round?

## 73730:00 - 73765:00

I think one thing is that the Codex team

## 73765:00 - 73785:00

is growing.

## 73785:00 - 73815:00

And uh as I was just saying, we're still

## 73815:00 - 73845:00

somewhat limited by human thinking speed

## 73845:00 - 73875:00

and human typing speed. We're working on

## 73875:00 - 73910:00

it. So, um

## 73910:00 - 73950:00

if you're an engineer um or a

## 73950:00 - 73990:00

salesperson or I'm hiring for product

## 73990:00 - 74015:00

product person,

## 74015:00 - 74050:00

uh please hit us up. I'm not sure the

## 74050:00 - 74090:00

best way to give contact info, but I

## 74090:00 - 74120:00

guess you can go to a jobs page or do

## 74120:00 - 74145:00

they have contact for you? Actually, do

## 74145:00 - 74170:00

you do listeners have contact for you?

## 74170:00 - 74195:00

Before they send me like, "Hey, I want

## 74195:00 - 74225:00

to apply to Codex." Uh I do have a

## 74225:00 - 74260:00

contact form at lennyrachitsky.com. I'm

## 74260:00 - 74290:00

afraid of all the amazing people that

## 74290:00 - 74295:00

are here

## 74295:00 - 74315:00

>> Okay. ping me, but there you go, we

## 74315:00 - 74345:00

could try that. Let's see how that goes.

## 74345:00 - 74370:00

>> yeah, or another maybe an easier way we

## 74370:00 - 74400:00

can edit all that out. Or if it's up to

## 74400:00 - 74435:00

you. But uh yeah, or I would just say

## 74435:00 - 74480:00

you can drop us a DM. Uh for example,

## 74480:00 - 74525:00

I'm amber rico on Twitter and hit me up

## 74525:00 - 74540:00

if you're interested in joining the

## 74540:00 - 74570:00

team. What a dream job for so many

## 74570:00 - 74590:00

people.

## 74590:00 - 74630:00

What's a sign they will I don't know,

## 74630:00 - 74655:00

what's like a way to filter people a

## 74655:00 - 74685:00

little bit so they're not flooding your

## 74685:00 - 74730:00

inbox? So, specifically if you want to

## 74730:00 - 74765:00

join the Codex team, then you need to be

## 74765:00 - 74815:00

a technical person who uses these tools.

## 74815:00 - 74835:00

And I think I would just ask yourself

## 74835:00 - 74855:00

the question,

## 74855:00 - 74885:00

uh hey, let's say, you know, I were to

## 74885:00 - 74925:00

join OpenAI and work on Codex

## 74925:00 - 74960:00

over the next 6 months, you know, and

## 74960:00 - 74995:00

crush it, what does the life of a

## 74995:00 - 75020:00

software engineer look like then? And I

## 75020:00 - 75040:00

think if you have an opinion on that,

## 75040:00 - 75065:00

you should apply. And if you

## 75065:00 - 75090:00

don't have an opinion on that and have

## 75090:00 - 75130:00

to think about it first,

## 75130:00 - 75145:00

you know, depending on how long you have

## 75145:00 - 75165:00

to think about it, I guess that would be

## 75165:00 - 75195:00

the filter, right? Like I think

## 75195:00 - 75215:00

there's a lot of people thinking about

## 75215:00 - 75250:00

the space and so, we're

## 75250:00 - 75290:00

we're very interested in folks who

## 75290:00 - 75335:00

sort of have already been thinking about

## 75335:00 - 75355:00

like what the future should look like

## 75355:00 - 75375:00

with agents. And like we don't have to

## 75375:00 - 75410:00

agree on where where we're going. But I

## 75410:00 - 75430:00

think we want people who like are very

## 75430:00 - 75465:00

passionate about the topic, I guess.

## 75465:00 - 75500:00

It's very rare to be working on a

## 75500:00 - 75530:00

product that has this much impact and is

## 75530:00 - 75550:00

at such a

## 75550:00 - 75600:00

bleeding edge of what's possible. It's a

## 75600:00 - 75625:00

what a cool role for the right person.

## 75625:00 - 75655:00

So, I'm it's awesome that you have an

## 75655:00 - 75700:00

opening and this audience is

## 75700:00 - 75745:00

a really good fit potentially for for

## 75745:00 - 75770:00

that role. So, I hope we find someone,

## 75770:00 - 75800:00

that would be incredible. With that,

## 75800:00 - 75835:00

we've reached our very exciting

## 75835:00 - 75865:00

lightning round. I've got five questions

## 75865:00 - 75905:00

for you, Alexander. Are you ready?

## 75905:00 - 75925:00

I don't know what these are, but I'm

## 75925:00 - 75970:00

excited. Let's do it. Uh they're uh the

## 75970:00 - 76000:00

same questions asked everyone except for

## 76000:00 - 76040:00

the last one. So, uh

## 76040:00 - 76065:00

probably not a surprise. I should

## 76065:00 - 76100:00

probably make them more more often a

## 76100:00 - 76135:00

surprise. Okay, first question, what are

## 76135:00 - 76160:00

a couple books that you recommend most

## 76160:00 - 76190:00

to other people? Two or three books that

## 76190:00 - 76210:00

come to mind.

## 76210:00 - 76250:00

I have been reading a lot of science

## 76250:00 - 76285:00

fiction recently. And I'm sure this has

## 76285:00 - 76310:00

been recommended before, but the

## 76310:00 - 76340:00

Culture.

## 76340:00 - 76370:00

I think it's Ian Banks is the name of

## 76370:00 - 76390:00

the author.

## 76390:00 - 76410:00

Part of why I love it is because it's

## 76410:00 - 76425:00

like

## 76425:00 - 76475:00

basically relatively recent writing

## 76475:00 - 76515:00

about a future with AI, but it's an

## 76515:00 - 76555:00

optimistic future with AI.

## 76555:00 - 76575:00

Um and I think, you know, a lot of

## 76575:00 - 76610:00

sci-fi is like fairly dystopian.

## 76610:00 - 76650:00

Um but this is like people uh sort of

## 76650:00 - 76680:00

the joke at least on the Culture

## 76680:00 - 76720:00

subreddit is that let me let me see if I

## 76720:00 - 76755:00

can get this right. It is a

## 76755:00 - 76800:00

like space communist utopia.

## 76800:00 - 76830:00

Or or like I think it's a gay space

## 76830:00 - 76865:00

communist utopia.

## 76865:00 - 76895:00

Um and uh I just think it's like really

## 76895:00 - 76940:00

fun to think about um like to use the

## 76940:00 - 76960:00

Culture as a way to think about like

## 76960:00 - 76985:00

what kind of world can we usher in and

## 76985:00 - 77010:00

like what decisions can we make today to

## 77010:00 - 77050:00

help usher in that world. Well, I've not

## 77050:00 - 77065:00

I I don't think anyone's recommended

## 77065:00 - 77095:00

that. I know you're reading, you

## 77095:00 - 77110:00

mentioned before we started recording,

## 77110:00 - 77150:00

Lord of the Rings right now. Uh if you

## 77150:00 - 77185:00

want another AI-ish

## 77185:00 - 77225:00

sci-fi book, uh have you read Fire Upon

## 77225:00 - 77250:00

the Deep?

## 77250:00 - 77260:00

No, I haven't.

## 77260:00 - 77310:00

>> Okay. It's uh incredibly good. It's like

## 77310:00 - 77360:00

uh a sci-fi space opera sort of epic

## 77360:00 - 77380:00

tale

## 77380:00 - 77415:00

with uh super intelligence.

## 77415:00 - 77450:00

Cool. Yeah, somewhat mostly not

## 77450:00 - 77495:00

optimistic, but somewhat optimistic.

## 77495:00 - 77530:00

Okay, next question. Is there a

## 77530:00 - 77580:00

favorite recent movie or TV show that

## 77580:00 - 77600:00

you've really enjoyed?

## 77600:00 - 77625:00

Yeah, there's an anime called Jujutsu

## 77625:00 - 77645:00

Kaisen,

## 77645:00 - 77680:00

which I really like. Um

## 77680:00 - 77705:00

again, it's got a kind of a slightly

## 77705:00 - 77750:00

dark topic of like demons.

## 77750:00 - 77785:00

Um but what I love about it is that the

## 77785:00 - 77815:00

hero is really nice. And I think there's

## 77815:00 - 77860:00

this new wave of like anime and cartoons

## 77860:00 - 77875:00

where

## 77875:00 - 77915:00

the protagonists are

## 77915:00 - 77955:00

really friendly and like people who care

## 77955:00 - 77990:00

about the world rather than being like

## 77990:00 - 78020:00

sort of like if you look at like some

## 78020:00 - 78060:00

older anime like that started the genre

## 78060:00 - 78085:00

like, you know, there was there was like

## 78085:00 - 78110:00

Evangelion

## 78110:00 - 78145:00

uh or Akira. And like those characters,

## 78145:00 - 78180:00

the protagonists are like deeply flawed,

## 78180:00 - 78215:00

like quite unhappy.

## 78215:00 - 78250:00

Um they they didn't start the genre, but

## 78250:00 - 78280:00

it was like a trend for a while to sort

## 78280:00 - 78295:00

of

## 78295:00 - 78330:00

poke fun at the idea that in these in

## 78330:00 - 78365:00

these cartoons, the protagonist was very

## 78365:00 - 78390:00

young but being given a ridiculous

## 78390:00 - 78415:00

amount of responsibility to like save

## 78415:00 - 78430:00

the world.

## 78430:00 - 78455:00

And so, there was kind of a a wave of

## 78455:00 - 78480:00

like

## 78480:00 - 78510:00

uh content that was like critiquing this

## 78510:00 - 78540:00

by making the character like basically

## 78540:00 - 78565:00

go through like serious like mental

## 78565:00 - 78605:00

issues in the middle of the show.

## 78605:00 - 78630:00

Um and I'm not saying this is better,

## 78630:00 - 78655:00

but at least it's quite fun to have like

## 78655:00 - 78700:00

these like really positive protagonists

## 78700:00 - 78720:00

or just trying to help everyone around

## 78720:00 - 78740:00

them. I love how much we're learning

## 78740:00 - 78785:00

about your personality hearing these

## 78785:00 - 78820:00

recommendations. Yeah. Nice

## 78820:00 - 78870:00

protagonists, optimistic futures. I

## 78870:00 - 78890:00

think you know, if you don't believe it,

## 78890:00 - 78930:00

you can't will it into existence. Mhm.

## 78930:00 - 78955:00

You need a balance. This is your

## 78955:00 - 78985:00

training data.

## 78985:00 - 79020:00

Is there a product you recently

## 79020:00 - 79045:00

discovered that you really love? Could

## 79045:00 - 79085:00

be an app, could be some clothing, could

## 79085:00 - 79130:00

be some kitchen gadget, tech gadget,

## 79130:00 - 79150:00

a hat.

## 79150:00 - 79210:00

Yeah, so I have been like quite into

## 79210:00 - 79250:00

uh you know, combustion engines

## 79250:00 - 79305:00

um and cars. Actually, the reason I came

## 79305:00 - 79340:00

to America initially was cuz I wanted to

## 79340:00 - 79380:00

work on like US aircraft. Um but you

## 79380:00 - 79410:00

know, now I work in software.

## 79410:00 - 79445:00

And so for the longest time I've

## 79445:00 - 79485:00

basically only had like quite old sports

## 79485:00 - 79500:00

cars.

## 79500:00 - 79535:00

Old just cuz they were more affordable.

## 79535:00 - 79605:00

And then recently

## 79605:00 - 79645:00

We got a Tesla instead.

## 79645:00 - 79680:00

And I have to say that I find the Tesla

## 79680:00 - 79715:00

software like quite inspiring.

## 79715:00 - 79745:00

In particular, it has like the

## 79745:00 - 79780:00

self-driving feature and you know, I've

## 79780:00 - 79820:00

mentioned a few times like today like I

## 79820:00 - 79840:00

think it's really interesting to think

## 79840:00 - 79865:00

about how to build like mixed initiative

## 79865:00 - 79890:00

software that makes you feel maximally

## 79890:00 - 79925:00

empowered as a human.

## 79925:00 - 79950:00

Maximally in control, but yet you're

## 79950:00 - 79975:00

getting a lot of help.

## 79975:00 - 80015:00

And I think they did a really good job.

## 80015:00 - 80050:00

With enabling sort of the car to drive

## 80050:00 - 80090:00

itself, but All these different ways

## 80090:00 - 80115:00

that you can adjust what it's doing

## 80115:00 - 80140:00

without turning off the self-driving. So

## 80140:00 - 80165:00

like you can accelerate and you know,

## 80165:00 - 80195:00

it'll like listen to that. You can turn

## 80195:00 - 80225:00

a knob to change its speed. You can

## 80225:00 - 80265:00

steer slightly. Um

## 80265:00 - 80285:00

I think it's a it's actually a master

## 80285:00 - 80335:00

class in like building an agent. That

## 80335:00 - 80360:00

Still leaves the human in control. This

## 80360:00 - 80390:00

reminds me Nick Turley's whole

## 80390:00 - 80430:00

mantra was are we maximally accelerated?

## 80430:00 - 80435:00

Yeah.

## 80435:00 - 80465:00

>> It was like it's completely infiltrated

## 80465:00 - 80500:00

everything at OpenAI which makes sense.

## 80500:00 - 80530:00

That tracks.

## 80530:00 - 80570:00

Uh two more questions. Do you have a

## 80570:00 - 80615:00

life motto that you often think about

## 80615:00 - 80640:00

come back to in work or in life that's

## 80640:00 - 80675:00

been helpful? I don't know if I have a

## 80675:00 - 80700:00

life motto, but maybe I can tell you

## 80700:00 - 80735:00

about the number one value

## 80735:00 - 80765:00

Company value from my startup. Love it.

## 80765:00 - 80790:00

Which is still something that sticks

## 80790:00 - 80850:00

with me, which is to be kind and candid.

## 80850:00 - 80885:00

That tracks.

## 80885:00 - 80925:00

Kind and candid. Wow. Yeah, and we had

## 80925:00 - 80970:00

to put them together because we

## 80970:00 - 81015:00

As founders realized that we

## 81015:00 - 81065:00

Often would be nice.

## 81065:00 - 81110:00

And it wasn't actually the right thing

## 81110:00 - 81130:00

to do.

## 81130:00 - 81145:00

We would like delay the difficult

## 81145:00 - 81180:00

conversations and we were not candid.

## 81180:00 - 81210:00

And so every time we would like remind

## 81210:00 - 81230:00

ourselves of this motto and then we

## 81230:00 - 81250:00

would become more candid and then 6

## 81250:00 - 81275:00

months later we would realize that we

## 81275:00 - 81310:00

were in fact not candid 6 months ago.

## 81310:00 - 81345:00

And we needed to be even more candid.

## 81345:00 - 81375:00

So then the question is like okay, like

## 81375:00 - 81400:00

How could how should we be candid? It's

## 81400:00 - 81430:00

like okay, well Let's let's think of

## 81430:00 - 81460:00

being candid as an act of kindness, but

## 81460:00 - 81485:00

also think of that both in terms of

## 81485:00 - 81505:00

doing it and willing ourselves to do it,

## 81505:00 - 81530:00

but also in terms of how we frame it to

## 81530:00 - 81575:00

people. That is a beautiful

## 81575:00 - 81605:00

way of summarizing how to how to lead

## 81605:00 - 81660:00

well. What's the The book about dare

## 81660:00 - 81700:00

challenge directly but care deeply.

## 81700:00 - 81730:00

Radical candor. Oh yeah, yeah, right.

## 81730:00 - 81750:00

Yeah. Yeah, so it's like another way of

## 81750:00 - 81780:00

thinking about radical candor. Okay,

## 81780:00 - 81800:00

last question. I was looking up your

## 81800:00 - 81840:00

last name just like hey, what's the

## 81840:00 - 81860:00

what's the story here? So your last name

## 81860:00 - 81895:00

is Imbrios. And I was talking to

## 81895:00 - 81920:00

ChatGPT.

## 81920:00 - 81940:00

And it told me the most famous

## 81940:00 - 81980:00

individuals with the surname are

## 81980:00 - 82010:00

The influential Greek poet and

## 82010:00 - 82065:00

psychoanalyst Andreas Imbrios.

## 82065:00 - 82095:00

And his relative the wealthy shipping

## 82095:00 - 82130:00

magnate and art collector George

## 82130:00 - 82160:00

Imbrios.

## 82160:00 - 82185:00

So the question is which of these two do

## 82185:00 - 82220:00

you most identify with?

## 82220:00 - 82265:00

The Greek poet and psychoanalyst or the

## 82265:00 - 82290:00

wealthy shipping magnate and art

## 82290:00 - 82310:00

collector?

## 82310:00 - 82335:00

I think it's it's going to have to be

## 82335:00 - 82380:00

the poet because Uh

## 82380:00 - 82400:00

He

## 82400:00 - 82435:00

He loved the island that our family's

## 82435:00 - 82475:00

from. Wait, you know these people? Okay,

## 82475:00 - 82505:00

this is not news to you. Okay.

## 82505:00 - 82530:00

>> Well, I mean it's an enormous family,

## 82530:00 - 82565:00

but it's like Greek. So you know, these

## 82565:00 - 82595:00

big families everyone like everyone's

## 82595:00 - 82620:00

your uncle. You know what I mean? Like

## 82620:00 - 82640:00

my mother's Malaysian and also like

## 82640:00 - 82680:00

everyone is my uncle or aunt in Malaysia

## 82680:00 - 82730:00

too if that makes sense. Yeah. But

## 82730:00 - 82775:00

Yeah, he he loved this island that the

## 82775:00 - 82815:00

family sort of like initiated from.

## 82815:00 - 82840:00

I believe I don't actually know where

## 82840:00 - 82870:00

that shipping magnate I think it was New

## 82870:00 - 82900:00

York or something, but anyway, we all

## 82900:00 - 82930:00

came from this island called Andros.

## 82930:00 - 82970:00

Which is a really beautiful place and

## 82970:00 - 82995:00

it's like there's more like livestock

## 82995:00 - 83030:00

there than than humans.

## 83030:00 - 83070:00

Not too many tourists go there.

## 83070:00 - 83110:00

But I think he like part of what I think

## 83110:00 - 83130:00

is really cool is like he published a

## 83130:00 - 83150:00

lot and a lot of his writing is about

## 83150:00 - 83185:00

like the beauty of that island, which I

## 83185:00 - 83210:00

think is super cool.

## 83210:00 - 83245:00

Wow, that was an amazing answer. Two

## 83245:00 - 83265:00

more questions. Where can folks find you

## 83265:00 - 83290:00

if they want to follow you online and

## 83290:00 - 83310:00

you know, maybe reach out and then how

## 83310:00 - 83340:00

can listeners be useful to you? I I'm

## 83340:00 - 83370:00

one of those people who has social media

## 83370:00 - 83400:00

only for the purposes of having work.

## 83400:00 - 83425:00

You know, my phone my phone turns black

## 83425:00 - 83460:00

and white at like 9:00 p.m. at night.

## 83460:00 - 83535:00

But yeah, so Twitter or X at nbrico.

## 83535:00 - 83560:00

And

## 83560:00 - 83585:00

yeah, if you post in r/codex I'll

## 83585:00 - 83610:00

probably see it.

## 83610:00 - 83650:00

So you know, you can go there.

## 83650:00 - 83700:00

How can listeners be useful?

## 83700:00 - 83730:00

I would say please try Codex.

## 83730:00 - 83760:00

Please share feedback. Let us know what

## 83760:00 - 83790:00

to improve. We pay a ton of ton of

## 83790:00 - 83820:00

attention to feedback. I think it's like

## 83820:00 - 83850:00

Honestly like the growth has been

## 83850:00 - 83875:00

amazing, but it's still very early

## 83875:00 - 83895:00

times.

## 83895:00 - 83925:00

So we still pay a lot of attention and

## 83925:00 - 83950:00

hope to do so forever.

## 83950:00 - 83990:00

And also I would say if you're

## 83990:00 - 84040:00

interested in in working On the future

## 84040:00 - 84060:00

of coding agents and then agents

## 84060:00 - 84090:00

generally, then please

## 84090:00 - 84140:00

Apply to our job site and or message me

## 84140:00 - 84170:00

in those social media places.

## 84170:00 - 84195:00

Alexander, this was awesome. I always

## 84195:00 - 84235:00

love meeting people working on AI

## 84235:00 - 84265:00

because it always feels like there's

## 84265:00 - 84290:00

very I don't know

## 84290:00 - 84335:00

Sterile, scary, mysterious thing. And

## 84335:00 - 84355:00

then you meet the people building these

## 84355:00 - 84385:00

tools and they're always just so

## 84385:00 - 84440:00

awesome. And you especially just so nice

## 84440:00 - 84455:00

and

## 84455:00 - 84500:00

uh As you like the examples you shared

## 84500:00 - 84535:00

optimism and kindness, you know, this is

## 84535:00 - 84570:00

what we want to be. This is these are

## 84570:00 - 84585:00

the kinds of people we want to be

## 84585:00 - 84605:00

building these tools that are going to

## 84605:00 - 84655:00

drive the future. So um I'm I'm really

## 84655:00 - 84680:00

thankful that you did this.

## 84680:00 - 84690:00

Um

## 84690:00 - 84725:00

Grateful to have met you and thank you

## 84725:00 - 84750:00

so much for being here.

## 84750:00 - 84770:00

Yeah, thanks so much for having me. This

## 84770:00 - 84810:00

is fun.

## 84810:00 - 84835:00

Thank you so much for listening. If you

## 84835:00 - 84860:00

found this valuable, you can subscribe

## 84860:00 - 84900:00

to the show on Apple podcast, Spotify,

## 84900:00 - 84940:00

or your favorite podcast app.

## 84940:00 - 84970:00

Also, please consider giving us a rating

## 84970:00 - 85010:00

or leaving a review as that really helps

## 85010:00 - 85045:00

other listeners find the podcast. You

## 85045:00 - 85080:00

can find all past episodes or learn more

## 85080:00 - 85135:00

about the show at lennyspodcast.com.

## 85135:00+

See you in the next episode.

