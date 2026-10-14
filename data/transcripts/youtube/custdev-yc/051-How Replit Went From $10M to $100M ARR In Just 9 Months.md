---
source: https://www.youtube.com/watch?v=kOyIjt6FUrw
title: How Replit Went From $10M to $100M ARR In Just 9 Months
author: Y Combinator
date: 2025-07-17
views: 37715
description: >-
  Amjad Masad started Replit to make programming accessible to anyone, anywhere.
  What began as a tool for learning to code has grown into a platform pushing
  the limits of AI-assisted software creation and recently surpassed $100M in
  ARR.


  On The Breakdown with Tom and Dave, Amjad shares the journey from his early
  days in Jordan, working on open-source projects, to leading Replit through
  major pivots from "teach a billion people to code" to "let anyone build
  software." He discusses the evolving nature of programming, the future of
  work, and the next generation of human-computer collaboration.


  Apply to Y Combinator: https://ycombinator.com/apply

  Work at a startup: https://workatastartup.com


  Chapters:

  00:38 - From YC to Replit: The Early Days

  02:00 - A Billion Developers: Pre-LLM Vision

  02:58 - Betting the Company on Agents

  04:20 - AI Autonomy Jumps (Claude 3.x → 4.0)

  05:22 - Computer Use: The Last Mile

  06:40 - Sampling & Branching for Reliability

  10:00 - Non-Engineers Shipping Software

  12:10 - Security & Safe Components

  17:40 - Where Replit Fits (Cursor ↔ No-Code)

  18:50 - Ambient Building & Mobile Workflows

  23:00 - AI in Meetings & Granola Maximalism

  32:00 - Should Kids Still Learn to Code?

  33:52 - DIY SaaS & The Vertical SaaS Crunch

  34:46 - Final Advice for Founders
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:43:50.524Z
---

# How Replit Went From $10M to $100M ARR In Just 9 Months

## 00:00 - 55:00

I think the like dystopian view of AI or

## 55:00 - 100:00

AI as like taking all our jobs and all

## 100:00 - 140:00

of that is like not correct. And I think

## 140:00 - 185:00

the future of work is more human, is

## 185:00 - 225:00

more interactive, is more multimodal.

## 225:00 - 270:00

Once the making of things gets easier,

## 270:00 - 315:00

the bottleneck goes back to to to like

## 315:00 - 350:00

how many ideas you can have. I wouldn't

## 350:00 - 390:00

put learning to code as the top thing. I

## 390:00 - 425:00

would put learn to make things. Learn to

## 425:00 - 450:00

make things with code. Learn to make

## 450:00 - 485:00

things with video. learn to make like

## 485:00 - 540:00

anything with AI.

## 540:00 - 620:00

[Music]

## 620:00 - 650:00

>> Welcome back to the breakdown. I'm Dave.

## 650:00 - 680:00

This is Tom. And today we're joined by

## 680:00 - 725:00

Amjad Msad. Amjad is founder and CEO of

## 725:00 - 780:00

Replet, which was a YC 2018 company. Uh

## 780:00 - 790:00

welcome to the show.

## 790:00 - 805:00

>> Thank you.

## 805:00 - 835:00

>> So today, uh we want to talk about kind

## 835:00 - 875:00

of your beginnings in helping people

## 875:00 - 915:00

learn to code. what you're doing now in

## 915:00 - 950:00

replacing a lot of that work and then

## 950:00 - 980:00

where we see the future going in terms

## 980:00 - 1020:00

of how people make things. So, Replet

## 1020:00 - 1060:00

started um I guess in 2016, you were in

## 1060:00 - 1120:00

YC in 2018. You started out as a tool to

## 1120:00 - 1150:00

make it really easy for people learning

## 1150:00 - 1185:00

to program to set up development

## 1185:00 - 1235:00

environments purely on the web. Um but

## 1235:00 - 1270:00

now you're really taking off in AI

## 1270:00 - 1300:00

assisted coding. Tell us tell us the

## 1300:00 - 1345:00

latest. Yeah. So, um the mission has

## 1345:00 - 1370:00

always been to make programming more

## 1370:00 - 1420:00

accessible. Uh then we sort of uh you

## 1420:00 - 1450:00

know after YC we sort of updated it to

## 1450:00 - 1485:00

be a little more ambitious. We started

## 1485:00 - 1520:00

talking about a billion software

## 1520:00 - 1555:00

developers and it just sounded absurd at

## 1555:00 - 1565:00

the time and

## 1565:00 - 1585:00

>> this is all prel right.

## 1585:00 - 1630:00

>> Yeah. Prelm. There was a moment of time

## 1630:00 - 1650:00

I don't know if you remember that but

## 1650:00 - 1700:00

like 20 in the like 2015 AI hype. There

## 1700:00 - 1750:00

was like a bit of a NLP natural language

## 1750:00 - 1780:00

hype as well. There's a bunch of AI

## 1780:00 - 1810:00

companies that ended up being just like

## 1810:00 - 1830:00

humans behind the scene. They all went

## 1830:00 - 1885:00

broke, but um there was like a a glimpse

## 1885:00 - 1950:00

of potentially doing NLP on code. So, we

## 1950:00 - 1980:00

had an idea that, you know, it's it's

## 1980:00 - 2010:00

probably coming. I I even had it in my

## 2010:00 - 2055:00

in my seed deck that like at some point

## 2055:00 - 2080:00

like we'll collect enough data to like

## 2080:00 - 2135:00

train models. It wasn't until like GPG2

## 2135:00 - 2185:00

in 2020 that I felt like it was was

## 2185:00 - 2220:00

going to be possible. So we you know we

## 2220:00 - 2275:00

had we had built all these um primitives

## 2275:00 - 2300:00

like the development environment the

## 2300:00 - 2330:00

sort of hosting environment all the

## 2330:00 - 2370:00

other stuff around it. Uh and I felt

## 2370:00 - 2425:00

like if if we just like added um like AI

## 2425:00 - 2455:00

agents like it will be able to

## 2455:00 - 2480:00

orchestrate all the stuff and it'll be

## 2480:00 - 2520:00

it'll be really great. agents were like

## 2520:00 - 2560:00

every time we tried them. Uh I think the

## 2560:00 - 2590:00

first time we tried it like 2021 didn't

## 2590:00 - 2655:00

work, 22 it didn't work and then 2024

## 2655:00 - 2700:00

like early early in the in the year we

## 2700:00 - 2735:00

just felt like it's getting close.

## 2735:00 - 2790:00

>> Even GPT40 could like be coherent for

## 2790:00 - 2865:00

like um 2 minutes somehow just ended up

## 2865:00 - 2900:00

doing a big bat. The company was not

## 2900:00 - 2920:00

doing super well.

## 2920:00 - 2940:00

>> Yeah. was I was about to ask was there

## 2940:00 - 2960:00

like a bet the company moment where it's

## 2960:00 - 2990:00

like we were teaching people to code now

## 2990:00 - 3015:00

we're no longer doing that now we're

## 3015:00 - 3035:00

going to enable everyone to build apps

## 3035:00 - 3060:00

>> yeah yeah yeah we had grown the company

## 3060:00 - 3125:00

quite a bit um and we were burning way

## 3125:00 - 3180:00

too much money uh and we decided to do a

## 3180:00 - 3195:00

layoff

## 3195:00 - 3245:00

>> and so we we um cut like perhaps 50

## 3245:00 - 3280:00

people and then like another like 15 20

## 3280:00 - 3305:00

people left and so we were like less

## 3305:00 - 3350:00

than half of the company and so I just

## 3350:00 - 3380:00

put everything on on replet agents I

## 3380:00 - 3415:00

just felt like this is the thing it has

## 3415:00 - 3455:00

to work. It felt like it was close.

## 3455:00 - 3485:00

Yeah. I don't know. I was just like burn

## 3485:00 - 3510:00

the boat boats kind of moments. It's

## 3510:00 - 3540:00

just like we got to do this. I mean,

## 3540:00 - 3590:00

it's I felt like this was the this was

## 3590:00 - 3615:00

the the thing that would make the

## 3615:00 - 3665:00

company work. And honestly, like if claw

## 3665:00 - 3725:00

3.5 hadn't come out mid US building

## 3725:00 - 3755:00

agent, we would have probably failed.

## 3755:00 - 3765:00

>> Yeah.

## 3765:00 - 3800:00

>> Because um like I said, like GPT40 would

## 3800:00 - 3840:00

like stay coherent for 2 3 minutes. Quad

## 3840:00 - 3875:00

3.5 was the first one that like could

## 3875:00 - 3905:00

work for like you know five to 10

## 3905:00 - 3930:00

minutes and actually actually work and

## 3930:00 - 3950:00

the code generations

## 3950:00 - 3970:00

>> and that's sort of the approach that I

## 3970:00 - 4000:00

think is most successful for startups

## 4000:00 - 4020:00

kind of building on the very edge of

## 4020:00 - 4045:00

what is possible you know you start out

## 4045:00 - 4075:00

on a mission it's the techn is not quite

## 4075:00 - 4100:00

there yet you start building and you

## 4100:00 - 4130:00

sort of you you skate where the puck is

## 4130:00 - 4150:00

going you know it sort of catches up

## 4150:00 - 4160:00

with you

## 4160:00 - 4185:00

>> yeah and you you want to keep keep doing

## 4185:00 - 4190:00

that

## 4190:00 - 4205:00

>> totally

## 4205:00 - 4240:00

>> yeah I remember you came to speak at YC

## 4240:00 - 4270:00

like 6 months ago and right after you

## 4270:00 - 4300:00

had launched this and at the time you

## 4300:00 - 4345:00

said we're very far from fully automated

## 4345:00 - 4370:00

software development.

## 4370:00 - 4390:00

>> Do you still feel that way?

## 4390:00 - 4430:00

>> No, not at all. I mean, I I feel like

## 4430:00 - 4460:00

I've, you know, every time I make a sort

## 4460:00 - 4485:00

of some kind of prediction, it feels

## 4485:00 - 4520:00

like bold and like, you know, but I've

## 4520:00 - 4560:00

been I've been consistently wrong and

## 4560:00 - 4600:00

like uh the way things are moving uh is

## 4600:00 - 4625:00

a lot faster. Just the level of

## 4625:00 - 4670:00

autonomy. Uh like I said, like maybe 3.5

## 4670:00 - 4715:00

was like 5 to 10 minutes. Like 3.7

## 4715:00 - 4750:00

perhaps can get up to like four five

## 4750:00 - 4805:00

minutes to an hour. The uh 4.0 No, in

## 4805:00 - 4850:00

the in the system card and opus, they

## 4850:00 - 4895:00

said they made it work for seven hours.

## 4895:00 - 4900:00

>> Wow.

## 4900:00 - 4920:00

>> 7 hours.

## 4920:00 - 4930:00

>> That's incredible.

## 4930:00 - 4955:00

>> That's always been the limiting factor

## 4955:00 - 4990:00

for making agents is like, can they stay

## 4990:00 - 5025:00

coherent? Can is the context length

## 5025:00 - 5070:00

actually useful to reason over. If an

## 5070:00 - 5110:00

LLM can work for for seven hours, that's

## 5110:00 - 5150:00

basically like a human worker.

## 5150:00 - 5180:00

>> Yeah. And presumably they're working at

## 5180:00 - 5205:00

much faster speed than a human would do.

## 5205:00 - 5230:00

So they're kind of completing perhaps a

## 5230:00 - 5250:00

week's work in those seven hours. The

## 5250:00 - 5295:00

only thing that I think is is missing

## 5295:00 - 5325:00

and a big limiting factor for actually

## 5325:00 - 5355:00

automating a lot of work is computer

## 5355:00 - 5370:00

use.

## 5370:00 - 5400:00

>> Computer use kind of sucks.

## 5400:00 - 5425:00

>> You know, I'm sure you've you've tried

## 5425:00 - 5455:00

it. And this is the difference between

## 5455:00 - 5505:00

Replet agent really uh giving it one

## 5505:00 - 5545:00

prompt going all all the way in an app

## 5545:00 - 5580:00

versus having to kind of babysit it a

## 5580:00 - 5605:00

little bit and like test with it.

## 5605:00 - 5625:00

>> And we had a company in the last batch

## 5625:00 - 5650:00

called browser use that's um that's

## 5650:00 - 5665:00

working browser automation.

## 5665:00 - 5690:00

>> Browser Use is great. And another one

## 5690:00 - 5710:00

called pig which is doing the same for

## 5710:00 - 5735:00

kind of windows desktops.

## 5735:00 - 5765:00

>> And uh I think advice I would give

## 5765:00 - 5815:00

founders today is um taking either

## 5815:00 - 5845:00

browser use or windows automation with

## 5845:00 - 5875:00

pig and trying to apply that into

## 5875:00 - 5910:00

enterprise into vertical

## 5910:00 - 5935:00

>> into a vertical industry.

## 5935:00 - 5960:00

>> The moment this technology worked those

## 5960:00 - 5985:00

two companies are just going to

## 5985:00 - 6005:00

>> totally and I think I think we're like

## 6005:00 - 6040:00

weeks or perhaps single digit months

## 6040:00 - 6060:00

away from it working really really well

## 6060:00 - 6090:00

and so now is the time to get started

## 6090:00 - 6110:00

using those technologies.

## 6110:00 - 6135:00

>> Absolutely 100%. And this is this is

## 6135:00 - 6160:00

what we're focused on. So you know

## 6160:00 - 6205:00

replet agent v1 to v2 was a huge jump in

## 6205:00 - 6255:00

autonomy. Uh v3 is the most autonomous

## 6255:00 - 6290:00

thing. So we're already working on it

## 6290:00 - 6355:00

and um the interesting thing for us is

## 6355:00 - 6385:00

the underlying technology and how it

## 6385:00 - 6420:00

would enable autonomy. There are like a

## 6420:00 - 6480:00

few important things. One is uh uh you

## 6480:00 - 6525:00

know being transactional. The ability to

## 6525:00 - 6565:00

roll back is is very important. So you

## 6565:00 - 6615:00

you would want you'd want it to be safe

## 6615:00 - 6645:00

for agents in the same way that gits

## 6645:00 - 6685:00

made it safe for human programmers to

## 6685:00 - 6720:00

kind of experiment and create branches

## 6720:00 - 6755:00

whatever you want the same thing for for

## 6755:00 - 6790:00

agents like if an agent kind of messes

## 6790:00 - 6820:00

up a DB migration it should be able to

## 6820:00 - 6860:00

roll back and also it should be able to

## 6860:00 - 6885:00

like sample

## 6885:00 - 6925:00

>> uh across different different paths. Uh

## 6925:00 - 6950:00

I think this is very very important for

## 6950:00 - 6990:00

autonomy. If you look at uh like for

## 6990:00 - 7040:00

example when when uh Anthropic publishes

## 7040:00 - 7080:00

their Swedbench score they publish one

## 7080:00 - 7115:00

with that sampling and one with sampling

## 7115:00 - 7160:00

and it goes from 70% to 80%.

## 7160:00 - 7190:00

>> And so this is the idea that you sort of

## 7190:00 - 7225:00

you spawn multiple agents each one will

## 7225:00 - 7250:00

take a a shot at it and then you figure

## 7250:00 - 7275:00

out which one works and and choose that

## 7275:00 - 7320:00

that branch effectively. We built a

## 7320:00 - 7375:00

infrastructure that is um uh fully

## 7375:00 - 7415:00

transactional and moves in lock step

## 7415:00 - 7450:00

meaning the file system is a snap

## 7450:00 - 7495:00

snapshot fail based file system the DB

## 7495:00 - 7565:00

is a snapshot based uh u DB and so a as

## 7565:00 - 7610:00

you're we're making commits uh to the

## 7610:00 - 7635:00

entire system including the virtual

## 7635:00 - 7675:00

machine as you're going uh and so what

## 7675:00 - 7700:00

we can do is also we can we can fork it

## 7700:00 - 7735:00

and branch it out. So if if we had

## 7735:00 - 7780:00

computer use that's working well you can

## 7780:00 - 7815:00

you can just like right now what they do

## 7815:00 - 7845:00

with the sampling is they do they have

## 7845:00 - 7875:00

some kind of judge that does ranking

## 7875:00 - 7915:00

>> which you know it's not a true verifier

## 7915:00 - 7955:00

a true verifier is a is a is a test

## 7955:00 - 7990:00

right and a computer use test so you you

## 7990:00 - 8025:00

can sample out and really pick the best

## 8025:00 - 8045:00

branch that's actually working

## 8045:00 - 8055:00

>> that's incredible

## 8055:00 - 8095:00

>> and and repeat that on and on and

## 8095:00 - 8130:00

reliability gets really really high

## 8130:00 - 8170:00

>> so fast forward six or 12 months you're

## 8170:00 - 8205:00

not spawning one agent you're spawning

## 8205:00 - 8235:00

is Is it five or 10 or a million? Like

## 8235:00 - 8255:00

how

## 8255:00 - 8285:00

>> I think this is where it's going to get

## 8285:00 - 8335:00

interesting, which is you'd want to give

## 8335:00 - 8370:00

the user the ability to set compute

## 8370:00 - 8395:00

budgets. I I think we're starting to see

## 8395:00 - 8435:00

that with um with the O style models of

## 8435:00 - 8465:00

like here's here's how much budget. But

## 8465:00 - 8495:00

but look, I mean, if if you give us

## 8495:00 - 8535:00

$1,000, we'll spend them if you know.

## 8535:00 - 8555:00

So, uh

## 8555:00 - 8575:00

>> that's really cool. I've not thought of

## 8575:00 - 8600:00

that before. Um but the idea of like

## 8600:00 - 8620:00

spawning multiple branches then just

## 8620:00 - 8640:00

picking the best one and being able to

## 8640:00 - 8670:00

do that in parallel. I just the human

## 8670:00 - 8700:00

brain doesn't naturally work like that.

## 8700:00 - 8730:00

We think sequentially. We can't.

## 8730:00 - 8755:00

>> It reminds me of this legend. I don't

## 8755:00 - 8770:00

know if this is actually true, but at

## 8770:00 - 8800:00

Apple when Steve was running it, he

## 8800:00 - 8825:00

would intentionally have teams doing

## 8825:00 - 8860:00

basically the same things and then see

## 8860:00 - 8885:00

which one did the best job. It's like

## 8885:00 - 8910:00

>> I've heard OpenAI does that now.

## 8910:00 - 8940:00

Interesting. Uh I I've heard that like

## 8940:00 - 8975:00

the Codeex project like had multiple

## 8975:00 - 9005:00

different different teams. So in the

## 9005:00 - 9050:00

literature, you'll see that uh small

## 9050:00 - 9120:00

small models sampled uh will beat larger

## 9120:00 - 9155:00

models. So Sonnet sampled is probably

## 9155:00 - 9195:00

better than than Opus companies. uh

## 9195:00 - 9220:00

haven't tried that where instead of

## 9220:00 - 9270:00

hiring one senior engineer you hire like

## 9270:00 - 9305:00

10 junior engineers and like give them

## 9305:00 - 9340:00

the same task and then

## 9340:00 - 9365:00

>> it's just very expensive with humans but

## 9365:00 - 9395:00

with LM it's relatively cheap you can

## 9395:00 - 9420:00

just do that do a hundred of them and

## 9420:00 - 9445:00

just pick the best one every time

## 9445:00 - 9470:00

>> so how are people using replet agent

## 9470:00 - 9510:00

like and and who are the people using it

## 9510:00 - 9540:00

>> you know it goes back to sort of our

## 9540:00 - 9565:00

early vision that if you make

## 9565:00 - 9610:00

programming easy uh then uh then more

## 9610:00 - 9635:00

and more people would want to would want

## 9635:00 - 9660:00

to do it actually this is one of the

## 9660:00 - 9695:00

first thing uh that that PG PG and I

## 9695:00 - 9735:00

sort of connected on um before we got

## 9735:00 - 9780:00

into YC actually PG um found us on

## 9780:00 - 9810:00

HackerNews and so we started this email

## 9810:00 - 9870:00

relationship um and so he he told me

## 9870:00 - 9900:00

there's like a super linear relationship

## 9900:00 - 9935:00

with how easy programming is versus how

## 9935:00 - 9970:00

many people would want to do it. The

## 9970:00 - 10000:00

optimizing function of rapid has always

## 10000:00 - 10040:00

been like just keep lowering the the

## 10040:00 - 10075:00

barrier to entry and and that's how you

## 10075:00 - 10120:00

grow users and you grow uh customers.

## 10120:00 - 10190:00

right now. Um, basically people from

## 10190:00 - 10220:00

kind of every walk of life, we've seen

## 10220:00 - 10260:00

users, product managers tend to be tend

## 10260:00 - 10325:00

to be a very a great um use case and

## 10325:00 - 10365:00

users for us and we've had customers uh

## 10365:00 - 10415:00

product managers uh who uh are able to

## 10415:00 - 10465:00

make significant impact on the business

## 10465:00 - 10500:00

without talking to engineers at all like

## 10500:00 - 10520:00

you know running AB tests or

## 10520:00 - 10550:00

optimizations or or things like that. I

## 10550:00 - 10590:00

mean it's empowering. I mean it gets us

## 10590:00 - 10650:00

to think about the really the seams

## 10650:00 - 10675:00

between these roles like you know

## 10675:00 - 10720:00

product manager, designer, engineer. We

## 10720:00 - 10750:00

actually just created a new new product

## 10750:00 - 10785:00

group and and and typically you know

## 10785:00 - 10825:00

product uh you know head of product is

## 10825:00 - 10855:00

have has a bunch of like product

## 10855:00 - 10880:00

managers reporting to them but we're

## 10880:00 - 10925:00

actually having uh this this group have

## 10925:00 - 10960:00

has designers, engineers and and PMs and

## 10960:00 - 10995:00

the the idea is they're all using AI all

## 10995:00 - 11035:00

the time to to prototype in some cases

## 11035:00 - 11065:00

go all the way to production. there

## 11065:00 - 11120:00

isn't this sort of waterfall model where

## 11120:00 - 11150:00

you know there's a lot of inefficiency

## 11150:00 - 11170:00

you know like communication problems

## 11170:00 - 11200:00

between these different teams they can

## 11200:00 - 11225:00

move incredibly fast and I think that

## 11225:00 - 11255:00

that starts to change how tech companies

## 11255:00 - 11290:00

work my experience of this was when

## 11290:00 - 11330:00

whenever I was working in a startup the

## 11330:00 - 11360:00

list of ideas and the backlog would

## 11360:00 - 11390:00

always would be infinitely long

## 11390:00 - 11405:00

basically and the bottleneck was always

## 11405:00 - 11435:00

engineering time and now I'm doing my

## 11435:00 - 11470:00

own personal projects I write my to-do

## 11470:00 - 11505:00

list or my idea list and then I get to

## 11505:00 - 11540:00

work and my the ideas just get done and

## 11540:00 - 11565:00

suddenly the bottleneck is like my

## 11565:00 - 11590:00

ability to have ideas

## 11590:00 - 11620:00

>> and it's just such a weird experience

## 11620:00 - 11640:00

looking at a to-do list. It's just empty

## 11640:00 - 11675:00

being like what do I do next? I've heard

## 11675:00 - 11715:00

from a team that has like a really large

## 11715:00 - 11740:00

uh replet deployment in their company

## 11740:00 - 11785:00

that their founders using Replet and

## 11785:00 - 11820:00

that's stressing the engineers out

## 11820:00 - 11845:00

because oh I did this in a weekend like

## 11845:00 - 11865:00

can't you do it in a

## 11865:00 - 11895:00

>> what do you guys show for yourself and

## 11895:00 - 11925:00

so are these previously technical people

## 11925:00 - 11950:00

or non techchnical people they're

## 11950:00 - 11990:00

building the first version are they

## 11990:00 - 12010:00

deploying that production or are they

## 12010:00 - 12035:00

giving to engineers and say hey build

## 12035:00 - 12065:00

this like what what do you see typically

## 12065:00 - 12100:00

>> we advise to like work with with

## 12100:00 - 12130:00

engineering but that doesn't always

## 12130:00 - 12170:00

happen I think It's um understandable

## 12170:00 - 12205:00

that a lot of PMs and designers want to

## 12205:00 - 12230:00

go straight to users. What we're seeing

## 12230:00 - 12265:00

is they go to like beta users and test

## 12265:00 - 12305:00

users and I think this works really well

## 12305:00 - 12335:00

but in some cases they just like put it

## 12335:00 - 12375:00

in production. Uh and so right now we're

## 12375:00 - 12405:00

having discussions with all these

## 12405:00 - 12425:00

companies especially the engineering

## 12425:00 - 12465:00

leaders are unhappy about this like

## 12465:00 - 12515:00

who's on call for these services you

## 12515:00 - 12535:00

>> who's responsible for the bug

## 12535:00 - 12565:00

>> who's responsible for it. There's a lot

## 12565:00 - 12600:00

of questions that are coming up. The

## 12600:00 - 12620:00

obvious answer to all these questions is

## 12620:00 - 12655:00

like agents are responsible.

## 12655:00 - 12695:00

>> So what's the limiting factor today? I

## 12695:00 - 12730:00

buy code a thing and I'm like yoloing it

## 12730:00 - 12750:00

into production. Like what are what do

## 12750:00 - 12790:00

the engineers typically object like?

## 12790:00 - 12805:00

What what's going wrong?

## 12805:00 - 12850:00

>> Security is is is a big one. Like um

## 12850:00 - 12910:00

LLMs are fallible like like humans are.

## 12910:00 - 12965:00

They tend to write some uh there's some

## 12965:00 - 13000:00

components that they do terribly at like

## 13000:00 - 13030:00

for example off

## 13030:00 - 13070:00

>> uh like they all kind of suck at it. all

## 13070:00 - 13110:00

use like you know old methods of of

## 13110:00 - 13150:00

assaulting and hashing and so that's

## 13150:00 - 13185:00

been that's been a big sticking point

## 13185:00 - 13230:00

and we've seen a lot of examples out

## 13230:00 - 13280:00

there right now of some catastrophes

## 13280:00 - 13325:00

luckily it hasn't been like there hasn't

## 13325:00 - 13350:00

been a major catastrophe I think it's

## 13350:00 - 13400:00

coming but uh there's been uh like solo

## 13400:00 - 13435:00

founders who would leak um you know API

## 13435:00 - 13475:00

keys or would make it really easy to get

## 13475:00 - 13525:00

around the login security protections

## 13525:00 - 13545:00

and there are a lot of tools out there

## 13545:00 - 13575:00

that are like really not trying to take

## 13575:00 - 13605:00

responsibility for that and saying, "Oh,

## 13605:00 - 13640:00

it's it's the user's problem, the user's

## 13640:00 - 13685:00

fault." For us, we think that as a

## 13685:00 - 13735:00

platform that is marketing uh for the

## 13735:00 - 13780:00

non-developer, you actually have a

## 13780:00 - 13810:00

responsibility. We're trying to take

## 13810:00 - 13835:00

away

## 13835:00 - 13885:00

uh some of the things that we think LMS

## 13885:00 - 13925:00

should not do today. Uh so O for

## 13925:00 - 13965:00

example, we have a built-in O. So if you

## 13965:00 - 14010:00

go to wrap and just say add o, it will

## 14010:00 - 14040:00

pull in an o component that we built

## 14040:00 - 14080:00

from scratch. It has capture on it. It

## 14080:00 - 14125:00

has all the security you know bells and

## 14125:00 - 14150:00

whistles. So you don't have to worry

## 14150:00 - 14175:00

about all of that.

## 14175:00 - 14205:00

>> We integrated with your database. You

## 14205:00 - 14245:00

have a user management portal on on your

## 14245:00 - 14310:00

site as much as possible. Building in

## 14310:00 - 14340:00

these components that are tricky. I

## 14340:00 - 14370:00

think payments is the other one. I don't

## 14370:00 - 14400:00

think you'd want the LLMs to kind of do

## 14400:00 - 14410:00

do the payments.

## 14410:00 - 14425:00

>> And they're not that different, right?

## 14425:00 - 14450:00

like the sort of checkout. You know, you

## 14450:00 - 14465:00

might have a one time checkout, you

## 14465:00 - 14495:00

might have subscription, pay as you go,

## 14495:00 - 14525:00

but there are not unlimited versions of

## 14525:00 - 14550:00

payments. There's like two or three or

## 14550:00 - 14600:00

four. >> And this is the analogy is today humans

## 14600:00 - 14630:00

don't write their own version of

## 14630:00 - 14655:00

payments or their own version of O. They

## 14655:00 - 14685:00

use providers that have built these

## 14685:00 - 14710:00

components already. So, seems like we're

## 14710:00 - 14730:00

seeing the same thing play out and

## 14730:00 - 14745:00

that's the best way to do it.

## 14745:00 - 14775:00

>> Yeah, 100%. And then the other thing we

## 14775:00 - 14815:00

added uh we partnered with is a a great

## 14815:00 - 14845:00

security company called Samrip. And so

## 14845:00 - 14895:00

right now uh when you go to deploy a

## 14895:00 - 14935:00

replet app, we run a security scan. We

## 14935:00 - 14980:00

run a code security scan and we give you

## 14980:00 - 15020:00

like a report of warnings and errors and

## 15020:00 - 15045:00

things like that and the agents can try

## 15045:00 - 15065:00

to fix them for you.

## 15065:00 - 15100:00

>> Okay. And so security is one of the big

## 15100:00 - 15135:00

kind of bottlenecks to fully deploying

## 15135:00 - 15170:00

to production. I can imagine there must

## 15170:00 - 15195:00

be other things that coming down the

## 15195:00 - 15220:00

line like sort of scalability, you know,

## 15220:00 - 15245:00

looking for like N plus1 database

## 15245:00 - 15285:00

queries, uh performance bottlenecks.

## 15285:00 - 15310:00

What do you have in your mind like a

## 15310:00 - 15340:00

clear set of of blockers that need to be

## 15340:00 - 15375:00

overcome before this is truly like one

## 15375:00 - 15390:00

click to deploy?

## 15390:00 - 15430:00

>> Yeah, I I mean the big the biggest one

## 15430:00 - 15475:00

is just going to be humans like social

## 15475:00 - 15500:00

like you know there's just going to be

## 15500:00 - 15530:00

mistrust and I think it's just going to

## 15530:00 - 15565:00

have has has to play out. So you know

## 15565:00 - 15605:00

leaving that aside like enterprises has

## 15605:00 - 15645:00

to adapt to all of that stuff having

## 15645:00 - 15715:00

some way to also scan for scalability

## 15715:00 - 15755:00

like figuring out you know uh like doing

## 15755:00 - 15810:00

fuzzing or whatever it is or having some

## 15810:00 - 15845:00

kind of adversarial agent that's you

## 15845:00 - 15885:00

know trying to to to break your app I

## 15885:00 - 15925:00

think um you know that's one big thing I

## 15925:00 - 15950:00

think integrating with a company's

## 15950:00 - 15980:00

ecosystem so one thing we're adding is

## 15980:00 - 16000:00

the ability to bring in your design

## 16000:00 - 16015:00

system

## 16015:00 - 16025:00

>> that's cool

## 16025:00 - 16060:00

>> so in addition to kind of us providing

## 16060:00 - 16085:00

these components if you go to any

## 16085:00 - 16110:00

company they have a lot of these

## 16110:00 - 16140:00

components built out as raplet is

## 16140:00 - 16165:00

getting deployed into these large

## 16165:00 - 16200:00

companies how can we hook into their

## 16200:00 - 16225:00

their internal systems

## 16225:00 - 16260:00

>> this makes me think about the kind of

## 16260:00 - 16290:00

spectrum of these different coding

## 16290:00 - 16320:00

tools. Um, on one end of the spectrum,

## 16320:00 - 16340:00

you have kind of what I would call the

## 16340:00 - 16375:00

the power tools, the cursors, the wind

## 16375:00 - 16420:00

surf that let developers use this as a

## 16420:00 - 16460:00

way to amplify their efforts. And on the

## 16460:00 - 16485:00

full other end of the spectrum, you have

## 16485:00 - 16520:00

more of the like consumerf facing, hey,

## 16520:00 - 16540:00

if you want to make an app, like you can

## 16540:00 - 16565:00

now make an app. And it sounds like you

## 16565:00 - 16605:00

guys are kind of in the middle. Um,

## 16605:00 - 16650:00

you're helping companies get stuff done,

## 16650:00 - 16690:00

but you're doing it for people who don't

## 16690:00 - 16725:00

look like the tra traditional developer.

## 16725:00 - 16745:00

How do you see this world playing out?

## 16745:00 - 16770:00

Are there going to be like n different

## 16770:00 - 16815:00

tools or will we converge to one place

## 16815:00 - 16835:00

on that spectrum?

## 16835:00 - 16870:00

>> AGI is convergence obviously but but

## 16870:00 - 16890:00

leaving that aside, it's really hard to

## 16890:00 - 16935:00

plan for that world. I think that the

## 16935:00 - 17000:00

battle for how to incrementally make

## 17000:00 - 17055:00

product uh engineers more productive is

## 17055:00 - 17085:00

just it's an obvious one. The market

## 17085:00 - 17110:00

there is obvious. There's a lot of

## 17110:00 - 17155:00

companies going after it. Both the

## 17155:00 - 17185:00

application companies like cursor, the

## 17185:00 - 17210:00

underlying model companies are trying to

## 17210:00 - 17260:00

go there. I mean um you know claude code

## 17260:00 - 17295:00

is competing with cursor. Cursor uses a

## 17295:00 - 17320:00

cloud. I think it's a bit of a blood

## 17320:00 - 17350:00

bath there but it's the market is

## 17350:00 - 17380:00

obvious and the market is really large.

## 17380:00 - 17420:00

I would guess that there's going to be

## 17420:00 - 17450:00

more of a consolidation there.

## 17450:00 - 17485:00

>> Maybe it's not you know one but it's

## 17485:00 - 17525:00

probably two or three uh at best. I

## 17525:00 - 17575:00

think the sort of the the market we're

## 17575:00 - 17630:00

in is a lot larger. Uh so the

## 17630:00 - 17670:00

addressable humans is a lot more. You

## 17670:00 - 17685:00

know, we're talking about a billion, but

## 17685:00 - 17710:00

it could be more. Like really any

## 17710:00 - 17750:00

knowledge worker should be able to like

## 17750:00 - 17780:00

solve problems with software. My

## 17780:00 - 17820:00

conception of replet right now is the

## 17820:00 - 17850:00

what we want it to be is a universal

## 17850:00 - 17885:00

problem solver. It'll solve problems in

## 17885:00 - 17915:00

your personal lives or you know solve

## 17915:00 - 17955:00

problems in uh in your work and and all

## 17955:00 - 17985:00

of that. And so I think that that market

## 17985:00 - 18035:00

is uh will probably be like a little

## 18035:00 - 18060:00

more diverse and I think companies will

## 18060:00 - 18105:00

kind of figure out where um where they

## 18105:00 - 18155:00

slot in trying to solve uh autonomous

## 18155:00 - 18205:00

programming with the focus on the

## 18205:00 - 18230:00

non-engineer.

## 18230:00 - 18260:00

>> Uh we want you to not worry about

## 18260:00 - 18305:00

security, not worry about systems, not

## 18305:00 - 18340:00

worry about any of that. We want you to

## 18340:00 - 18370:00

really come in with your ideas to to

## 18370:00 - 18435:00

Replet and be uh an agents manager. And

## 18435:00 - 18465:00

we're trying to do it in a way that is

## 18465:00 - 18515:00

like as human as as possible and kind of

## 18515:00 - 18560:00

fits into into into the workflow. One

## 18560:00 - 18600:00

big difference between engineers and

## 18600:00 - 18625:00

sort of non-engineers, be it executives

## 18625:00 - 18670:00

or product managers, you're not on your

## 18670:00 - 18715:00

desk like 8 hours a day. Mobile is a big

## 18715:00 - 18740:00

part of that. We have like a really

## 18740:00 - 18770:00

great mobile app. And we're thinking

## 18770:00 - 18805:00

about this way of like ambient building.

## 18805:00 - 18835:00

Maybe you start an app on your uh in

## 18835:00 - 18860:00

your desktop. You go away with your

## 18860:00 - 18890:00

phone. You're in boring meeting. You get

## 18890:00 - 18925:00

a notification from the agent saying you

## 18925:00 - 18940:00

I'm done with this. Do you want

## 18940:00 - 18975:00

something else? You got texted. And so

## 18975:00 - 19010:00

we're trying to kind of build that

## 19010:00 - 19015:00

thing.

## 19015:00 - 19065:00

>> Yeah. A question I had um related to

## 19065:00 - 19100:00

that point is is about the user

## 19100:00 - 19145:00

interface. So for something like cursor

## 19145:00 - 19175:00

or wind surf, it's pretty obvious. The

## 19175:00 - 19215:00

primary UI element is like the code. You

## 19215:00 - 19240:00

you see code, you have a little chat

## 19240:00 - 19275:00

window, but primarily it's about diffs.

## 19275:00 - 19325:00

It's about kind of changes to code. And

## 19325:00 - 19350:00

for a tool like Replet, the primary

## 19350:00 - 19385:00

interface is like the graphical user

## 19385:00 - 19425:00

interface. You know, it's the it's the

## 19425:00 - 19465:00

buttons and the the wizzywig like you

## 19465:00 - 19480:00

see what you're building.

## 19480:00 - 19510:00

>> Exactly. And that's great for building

## 19510:00 - 19535:00

user interfaces, but when you're trying

## 19535:00 - 19570:00

to build more complicated sort of

## 19570:00 - 19600:00

logical flows, I found it a little bit

## 19600:00 - 19625:00

difficult cuz I couldn't there's no way

## 19625:00 - 19645:00

I couldn't see the code. I can't

## 19645:00 - 19665:00

visualize what's going on behind the

## 19665:00 - 19695:00

scenes. And it's sort of it's almost a

## 19695:00 - 19725:00

black box. Fast forwarding here, if

## 19725:00 - 19745:00

you're trying to build more complex

## 19745:00 - 19780:00

internal workflows, how do they how does

## 19780:00 - 19800:00

a product manager or an operations

## 19800:00 - 19835:00

manager at a big company visualize that

## 19835:00 - 19860:00

workflow and the kind of logical

## 19860:00 - 19875:00

branching that happens?

## 19875:00 - 19920:00

>> Yeah. So, if if you look back in the

## 19920:00 - 19955:00

history of computing, there was always

## 19955:00 - 20000:00

this vision of visual programming, it

## 20000:00 - 20060:00

never worked uh very well because

## 20060:00 - 20080:00

ultimately it's about Turing

## 20080:00 - 20120:00

completeness like these systems are not

## 20120:00 - 20170:00

universal computing devices. And now we

## 20170:00 - 20210:00

go to codegen. Obviously codegen is is

## 20210:00 - 20250:00

turing complete. Um but you're

## 20250:00 - 20280:00

interfacing with it primarily via

## 20280:00 - 20310:00

natural language. Natural language is

## 20310:00 - 20345:00

fuzzy. It's really hard to know whether

## 20345:00 - 20380:00

it's doing the right thing. I think the

## 20380:00 - 20415:00

synthesis of these two things is

## 20415:00 - 20450:00

probably coming where you are

## 20450:00 - 20485:00

interfacing with natural language but

## 20485:00 - 20515:00

you can instead of like just staring at

## 20515:00 - 20580:00

code uh there's maybe an interface or

## 20580:00 - 20615:00

like a different view on top of code.

## 20615:00 - 20670:00

You can imagine being able to do you

## 20670:00 - 20700:00

know small talk.

## 20700:00 - 20740:00

>> Yeah. So small talk is this uh

## 20740:00 - 20780:00

>> it's the first object-oriented um uh

## 20780:00 - 20845:00

programming um system and you know Alan

## 20845:00 - 20885:00

K would say it's like it is actually OP

## 20885:00 - 20915:00

where everything comes after it is not

## 20915:00 - 20950:00

um but the interesting thing about it in

## 20950:00 - 21000:00

small talk you can actually the way you

## 21000:00 - 21030:00

interact with code is not via files but

## 21030:00 - 21085:00

via objects via like logical objects and

## 21085:00 - 21115:00

so there's some kind of prior arc there

## 21115:00 - 21145:00

and I think the world we're headed in

## 21145:00 - 21175:00

where there's some kind of abstraction

## 21175:00 - 21205:00

over code that allows people to like

## 21205:00 - 21220:00

understand it.

## 21220:00 - 21240:00

>> Yeah, I think that's really interesting.

## 21240:00 - 21265:00

I there's some there's like an open

## 21265:00 - 21290:00

space there whether it's like pseudo

## 21290:00 - 21330:00

code is like looks like English but it's

## 21330:00 - 21350:00

a little bit more structured or it's a

## 21350:00 - 21375:00

visual drag and drop. I don't know. It's

## 21375:00 - 21410:00

>> Yeah, I think back to building products

## 21410:00 - 21450:00

with a team of engineers, designers, and

## 21450:00 - 21485:00

other folks. The interactions that I

## 21485:00 - 21520:00

would have as the like product lead with

## 21520:00 - 21555:00

those teams was verbal. It would be

## 21555:00 - 21605:00

written like abstracted ideas. We would

## 21605:00 - 21625:00

draw stuff on the whiteboard together.

## 21625:00 - 21670:00

We'd make system diagrams. We'd look at

## 21670:00 - 21700:00

the results of the app and we would test

## 21700:00 - 21730:00

it and point out like oh this thing is

## 21730:00 - 21760:00

broken that's too slow and it feels to

## 21760:00 - 21800:00

me like that sort of interface which is

## 21800:00 - 21845:00

very multimodal and very flexible is

## 21845:00 - 21880:00

probably the best end result like I

## 21880:00 - 21900:00

think we will get to something like that

## 21900:00 - 21940:00

where the author of products will be

## 21940:00 - 21965:00

doing that but the teams they're talking

## 21965:00 - 22000:00

to are not other humans they're agents

## 22000:00 - 22020:00

doing these things. Has has there been

## 22020:00 - 22070:00

an attempt in in sort of PM land to have

## 22070:00 - 22110:00

a little more formalism around

## 22110:00 - 22140:00

communication or

## 22140:00 - 22175:00

>> Yes. And I would not say it's been good.

## 22175:00 - 22210:00

The main thing is just like the PRD,

## 22210:00 - 22245:00

right? The product spec, right? And it's

## 22245:00 - 22275:00

just become, in my opinion, uh

## 22275:00 - 22310:00

oftentimes a performative

## 22310:00 - 22350:00

>> work artifact that you create just so

## 22350:00 - 22370:00

that you can have a thing to get your

## 22370:00 - 22390:00

promotion, right? If you're at a big

## 22390:00 - 22415:00

company. Uh but they're not actually

## 22415:00 - 22450:00

that useful. To me, the most useful

## 22450:00 - 22470:00

interactions are just these like

## 22470:00 - 22510:00

whiteboard conversations, right? What do

## 22510:00 - 22530:00

we wanted to do here? Oh, we got to

## 22530:00 - 22555:00

think about that. Oh, we didn't consider

## 22555:00 - 22585:00

this. Okay, let's re rethink this whole

## 22585:00 - 22605:00

thing. Like those sorts of

## 22605:00 - 22610:00

conversations.

## 22610:00 - 22645:00

>> AI can play a role in that as well. So,

## 22645:00 - 22700:00

I um you know this startup granola uh

## 22700:00 - 22730:00

that allows you to kind of record

## 22730:00 - 22755:00

meetings and they released this like

## 22755:00 - 22800:00

team version that like all the meetings

## 22800:00 - 22835:00

uh gets transcribed and and go there and

## 22835:00 - 22860:00

they have a mobile app right now where

## 22860:00 - 22885:00

like you can put on the table and like

## 22885:00 - 22925:00

it's trying. So I I was thinking maybe

## 22925:00 - 22995:00

we should go gr granola maximalism where

## 22995:00 - 23050:00

look you shouldn't fight the trend in

## 23050:00 - 23070:00

which companies are becoming

## 23070:00 - 23100:00

increasingly oral as opposed to like

## 23100:00 - 23165:00

written um and because like you know

## 23165:00 - 23205:00

people are talking on Slack people are

## 23205:00 - 23230:00

in meetings people like are

## 23230:00 - 23265:00

communicating via prompts with with

## 23265:00 - 23310:00

agents uh but you you would want a set

## 23310:00 - 23350:00

of AI tools that is actually like

## 23350:00 - 23400:00

creating that that that record and in

## 23400:00 - 23435:00

background that's like searchable and

## 23435:00 - 23470:00

organizable and and all of that.

## 23470:00 - 23495:00

>> Yeah. I wonder when we'll have our first

## 23495:00 - 23545:00

AI in like oral meetings. You know, you

## 23545:00 - 23570:00

you're jamming with your designer and

## 23570:00 - 23610:00

you the AI like chips in and says,

## 23610:00 - 23630:00

"Well, how about this idea?"

## 23630:00 - 23670:00

>> Yeah. And and this is where I think the

## 23670:00 - 23730:00

like dystopian view of AI or AI as like

## 23730:00 - 23770:00

taking all our jobs and all that is like

## 23770:00 - 23805:00

not correct. And I think the future of

## 23805:00 - 23855:00

work is more human, is more interactive,

## 23855:00 - 23890:00

is more multimodal, is more fun in my

## 23890:00 - 23905:00

opinion.

## 23905:00 - 23940:00

>> YC's next batch is now taking

## 23940:00 - 23980:00

applications. Got a startup in you?

## 23980:00 - 24030:00

Apply at y combinator.com/apply.

## 24030:00 - 24070:00

It's never too early and filling out the

## 24070:00 - 24115:00

app will level up your idea. Okay, back

## 24115:00 - 24145:00

to the video. All right, so so last time

## 24145:00 - 24175:00

we chatted, uh, you had launched Replet

## 24175:00 - 24205:00

agent and things were growing really

## 24205:00 - 24235:00

crazy. I imagine that has continued.

## 24235:00 - 24270:00

Any, anything you can share there? Maybe

## 24270:00 - 24305:00

soon we'll we'll share some numbers but

## 24305:00 - 24340:00

uh since replet agent launch we're

## 24340:00 - 24375:00

growing 45%

## 24375:00 - 24415:00

compound monthly uh average.

## 24415:00 - 24450:00

>> These are like metrics that we tell YC

## 24450:00 - 24470:00

companies during the batch when they

## 24470:00 - 24510:00

have a base of like no users to try to

## 24510:00 - 24540:00

achieve and you're doing this at larger

## 24540:00 - 24545:00

scale.

## 24545:00 - 24575:00

>> Yes. But you know it put a lot of strain

## 24575:00 - 24600:00

strain on the company and our systems

## 24600:00 - 24645:00

were still relatively relatively small.

## 24645:00 - 24680:00

I I feel like it can get to to your head

## 24680:00 - 24725:00

and you can start optimizing for for the

## 24725:00 - 24790:00

wrong thing. It's very easy in AI to

## 24790:00 - 24845:00

increase AR while users are not happy

## 24845:00 - 24880:00

>> because they're spending a lot more and

## 24880:00 - 24920:00

like not getting the results and in some

## 24920:00 - 24960:00

cases maybe shouldn't grow that that

## 24960:00 - 24990:00

fast because like you'd want users to

## 24990:00 - 25025:00

get a better experience for less less

## 25025:00 - 25055:00

money and so it's one thing that we try

## 25055:00 - 25085:00

not to obsess we actually don't have AR

## 25085:00 - 25125:00

goals at at Replet we have like more

## 25125:00 - 25160:00

product goals retention goals just like

## 25160:00 - 25170:00

other methods

## 25170:00 - 25195:00

>> yeah because the the sort of bad pattern

## 25195:00 - 25225:00

with some AI companies you grow topline

## 25225:00 - 25250:00

revenue very very quickly the churn is

## 25250:00 - 25285:00

like approaching 100% and eventually

## 25285:00 - 25300:00

that just catches up

## 25300:00 - 25325:00

>> and the gross margins are horrible too

## 25325:00 - 25355:00

and so it's like

## 25355:00 - 25385:00

>> you know the more growth you have the

## 25385:00 - 25410:00

worse the company's doing financially

## 25410:00 - 25420:00

and so

## 25420:00 - 25460:00

>> so how do investors see this space you

## 25460:00 - 25490:00

you must have talked with a bunch can

## 25490:00 - 25505:00

they tell the difference

## 25505:00 - 25545:00

>> it's all kind of a blur for them because

## 25545:00 - 25585:00

investors when they I mean I'm just

## 25585:00 - 25610:00

going to generalize here but when they

## 25610:00 - 25645:00

start looking at the space they'll use

## 25645:00 - 25670:00

everything for three minutes and

## 25670:00 - 25695:00

everything for three minutes looks the

## 25695:00 - 25745:00

same so I I think I think it will it

## 25745:00 - 25785:00

will start to clarify and these products

## 25785:00 - 25835:00

will start to uh I suppose to converge

## 25835:00 - 25875:00

diverge more with the different focuses

## 25875:00 - 25915:00

in the areas we're talking about. I

## 25915:00 - 25955:00

think over the next year it'll be like a

## 25955:00 - 25995:00

little more clearer but I think a lot of

## 25995:00 - 26030:00

them are are just like you know super

## 26030:00 - 26045:00

when we talk to them they're super

## 26045:00 - 26065:00

confused. They don't understand these

## 26065:00 - 26090:00

systems. They don't understand where

## 26090:00 - 26105:00

they're going.

## 26105:00 - 26145:00

>> I think that's a great segue into um the

## 26145:00 - 26170:00

the sort of technology underlying some

## 26170:00 - 26195:00

of these tools. I'd love to dig in a

## 26195:00 - 26220:00

little bit deeper. We've we've seen some

## 26220:00 - 26250:00

announcements from cursor and wind surf

## 26250:00 - 26280:00

about how they're kind of layering

## 26280:00 - 26345:00

whether it's um Claude or Gemini or um

## 26345:00 - 26390:00

the OpenAI models with then their own

## 26390:00 - 26430:00

layers on top the fast apply APIs stuff

## 26430:00 - 26465:00

like that fast apply models I guess can

## 26465:00 - 26485:00

you give us an overview of how it works

## 26485:00 - 26500:00

at Replet?

## 26500:00 - 26545:00

>> Yeah, a lot of it is you're patching

## 26545:00 - 26575:00

problems with the underlying frontier

## 26575:00 - 26590:00

models. Yeah.

## 26590:00 - 26625:00

>> So the reason fast supply was important

## 26625:00 - 26675:00

because none of the models uh were doing

## 26675:00 - 26710:00

very well at diffs. Can you explain what

## 26710:00 - 26730:00

what supply is?

## 26730:00 - 26765:00

>> When you're trying to like edit a file

## 26765:00 - 26805:00

as an LLM, the best thing to do is to

## 26805:00 - 26855:00

like uh create a create a diff. Uh but

## 26855:00 - 26885:00

these models are actually not very good

## 26885:00 - 26905:00

at creating diffs. They're actually not

## 26905:00 - 26935:00

very good at countering the lines in the

## 26935:00 - 26970:00

source code. So they get confused about

## 26970:00 - 27015:00

a lot of these things. So for a while, a

## 27015:00 - 27035:00

lot of companies were just like

## 27035:00 - 27075:00

rewriting the entire entire file.

## 27075:00 - 27105:00

>> And so diff for for nontechnical users

## 27105:00 - 27140:00

is sort of like remove these three lines

## 27140:00 - 27175:00

and inject these other three lines

## 27175:00 - 27205:00

instead. like find and replace almost.

## 27205:00 - 27240:00

>> That's right. That's right. And so you

## 27240:00 - 27320:00

needed some way to um make the model

## 27320:00 - 27360:00

generate some something of a diff,

## 27360:00 - 27395:00

>> but it's actually not good enough to

## 27395:00 - 27430:00

merge it. And so you need another model

## 27430:00 - 27460:00

to actually do the merge. So

## 27460:00 - 27485:00

>> instead of rewriting like it's a

## 27485:00 - 27510:00

thousand line file, just like output the

## 27510:00 - 27530:00

entire thousand lines,

## 27530:00 - 27570:00

>> it's very slow. It's very expensive. So

## 27570:00 - 27605:00

you prompt the model to be as lazy as

## 27605:00 - 27620:00

possible.

## 27620:00 - 27640:00

>> But in that case, it's really hard to

## 27640:00 - 27665:00

apply. Okay, so you need another model

## 27665:00 - 27705:00

that's like doing the application. Okay,

## 27705:00 - 27730:00

>> you can train a model or you can use

## 27730:00 - 27770:00

Gemini Flash or some of these smaller

## 27770:00 - 27810:00

smaller models. And so in some cases,

## 27810:00 - 27840:00

you need to to train a model or

## 27840:00 - 27875:00

fine-tune a model to do a better job at

## 27875:00 - 27910:00

it. In other cases, you just also patch

## 27910:00 - 27940:00

a bunch of other models to to do it.

## 27940:00 - 27975:00

It's engineering. It's engineering as

## 27975:00 - 28015:00

opposed to like research, I would say.

## 28015:00 - 28070:00

>> And I noticed um you guys don't expose

## 28070:00 - 28105:00

the underlying model to the user. With

## 28105:00 - 28125:00

other tools like cursor and wind surf,

## 28125:00 - 28150:00

there's a drop down. It's like I want to

## 28150:00 - 28195:00

you know let's see what Gemini thinks of

## 28195:00 - 28225:00

this problem. You don't do that. Why is

## 28225:00 - 28230:00

that?

## 28230:00 - 28275:00

>> A a big part of our research efforts is

## 28275:00 - 28305:00

in eval

## 28305:00 - 28340:00

>> and I think this is like an underrated

## 28340:00 - 28395:00

part of like you know co AI coding. So

## 28395:00 - 28430:00

we spend a ton of time evaling new

## 28430:00 - 28490:00

models writing evals generating evals

## 28490:00 - 28520:00

just data crunching trying to figure out

## 28520:00 - 28555:00

what the users are are getting or are

## 28555:00 - 28590:00

feeling. We built a lot of systems try

## 28590:00 - 28645:00

to understand um how these systems are

## 28645:00 - 28685:00

are performing the moment a new frontier

## 28685:00 - 28745:00

model uh lands we are evaluating almost

## 28745:00 - 28785:00

immediately. Jim and I for example like

## 28785:00 - 28810:00

uh you know couple months ago were

## 28810:00 - 28850:00

making the rounds really great model

## 28850:00 - 28880:00

really awesome at like oneshotting in

## 28880:00 - 28920:00

some cases better than claude agentic

## 28920:00 - 28980:00

work wasn't at like a tool calling at

## 28980:00 - 29005:00

you know some of the things like that

## 29005:00 - 29065:00

but users just see the hype and they're

## 29065:00 - 29105:00

like oh like yeah give me Gemini that's

## 29105:00 - 29125:00

>> how much notice do you have do they like

## 29125:00 - 29150:00

drop it on you and you like scrambling

## 29150:00 - 29170:00

or do you have like days or weeks before

## 29170:00 - 29205:00

that to to try to you know test it out

## 29205:00 - 29235:00

>> well we we have good partnerships with

## 29235:00 - 29260:00

these companies we We have a great

## 29260:00 - 29285:00

partnership with Google. We have a great

## 29285:00 - 29320:00

partnership with uh with Anthropic, even

## 29320:00 - 29345:00

with OpenAI. We have a close

## 29345:00 - 29370:00

relationship. So, a lot of them give us

## 29370:00 - 29400:00

give us a heads up, give us some early

## 29400:00 - 29450:00

checkpoints and we we try we we kind of

## 29450:00 - 29475:00

play with all of them. And in the case

## 29475:00 - 29505:00

of anthropic, we're always like the

## 29505:00 - 29540:00

first day kind of launching because we

## 29540:00 - 29565:00

end up building. A lot of times we're

## 29565:00 - 29585:00

sort of anticipating where they're

## 29585:00 - 29595:00

going.

## 29595:00 - 29600:00

>> Yeah.

## 29600:00 - 29630:00

>> Because you kind of like you can tell

## 29630:00 - 29690:00

like 3.5 3.7 there there's some

## 29690:00 - 29725:00

direction you can tell like where 4.0 is

## 29725:00 - 29750:00

going to land. So you start architecting

## 29750:00 - 29780:00

the systems but you know ultimately a

## 29780:00 - 29805:00

lot of our engineering efforts still

## 29805:00 - 29855:00

infrastructure like the the distributed

## 29855:00 - 29900:00

network file system that snapshot based

## 29900:00 - 29935:00

network file system like it took us 2

## 29935:00 - 29965:00

years to build like there's nothing off

## 29965:00 - 30000:00

the shelf to do that a lot of the

## 30000:00 - 30030:00

security stuff is really really

## 30030:00 - 30070:00

difficult like replet is one of the few

## 30070:00 - 30095:00

places in the world where you can get

## 30095:00 - 30135:00

like a virtual machine in the cloud um

## 30135:00 - 30165:00

you know by just like creating an

## 30165:00 - 30205:00

account and that's like a it's really

## 30205:00 - 30240:00

hard to kind of run this and protect

## 30240:00 - 30270:00

against this. You have crypto miners,

## 30270:00 - 30310:00

you have all sorts of stuff like that.

## 30310:00 - 30375:00

And Replet also uses um uh Nyx OS under

## 30375:00 - 30405:00

the hood. Nixos is a like fully

## 30405:00 - 30455:00

declarative also transactional uh

## 30455:00 - 30495:00

operating system generator as it were.

## 30495:00 - 30545:00

Uh we have like this multi- terabyte uh

## 30545:00 - 30570:00

hard drive in all the different regions

## 30570:00 - 30615:00

that we have compute. um that that that

## 30615:00 - 30650:00

cached all the packages in the in the

## 30650:00 - 30675:00

world and that gets attached to every

## 30675:00 - 30720:00

container and and again all of that I

## 30720:00 - 30750:00

mean I keep coming back to this idea of

## 30750:00 - 30790:00

transactionality like you would want the

## 30790:00 - 30815:00

system to be fully functional. You would

## 30815:00 - 30865:00

want it to be um you would want it to be

## 30865:00 - 30905:00

safe in order to like experiment with

## 30905:00 - 30945:00

something go back do the sampling with

## 30945:00 - 30990:00

with agents. So really a lot of the a

## 30990:00 - 31020:00

lot of the work is just like the

## 31020:00 - 31050:00

engineering of this infrastructure and

## 31050:00 - 31085:00

it's like not as a parent not as sexy as

## 31085:00 - 31115:00

sort of like we're trained this model

## 31115:00 - 31165:00

here's the um but but I think this is

## 31165:00 - 31215:00

where you can build like a uh a bit of a

## 31215:00 - 31225:00

lead.

## 31225:00 - 31270:00

>> Yeah. I when VCs talk about moes uh the

## 31270:00 - 31305:00

thing that I translate it to in my head

## 31305:00 - 31335:00

is what is the compounding advantage

## 31335:00 - 31360:00

that you might be able to achieve.

## 31360:00 - 31390:00

Right. It's not really a defensive mode.

## 31390:00 - 31420:00

It's more just I'm ahead and by being

## 31420:00 - 31455:00

ahead in some vector it allows me to

## 31455:00 - 31485:00

continue to move faster. That's right.

## 31485:00 - 31505:00

>> And it sounds like this is a great

## 31505:00 - 31515:00

example of that.

## 31515:00 - 31545:00

>> True modes are often not obvious until

## 31545:00 - 31580:00

like decades perhaps many decades into

## 31580:00 - 31610:00

into the company. Like you wouldn't know

## 31610:00 - 31650:00

what like Netflix's mode. Uh but

## 31650:00 - 31670:00

obviously they have one like Disney

## 31670:00 - 31700:00

tried to like compete with them and

## 31700:00 - 31735:00

everyone was like you know down on on on

## 31735:00 - 31760:00

Netflix but turned out they have a mode

## 31760:00 - 31805:00

that is this uh content production

## 31805:00 - 31830:00

system that they that they built.

## 31830:00 - 31865:00

>> So Amad you you started with the mission

## 31865:00 - 31890:00

of like making it easier for people to

## 31890:00 - 31925:00

learn to code. You've accomplished a lot

## 31925:00 - 31955:00

of that. Now you're pushing the envelope

## 31955:00 - 32000:00

of what it even means to code. I've got

## 32000:00 - 32040:00

young kids. I want them to be productive

## 32040:00 - 32075:00

creators in the world. What should I

## 32075:00 - 32110:00

tell them to do? Should they learn to

## 32110:00 - 32130:00

code? What does that even mean?

## 32130:00 - 32180:00

>> Look, I think if you want to go the like

## 32180:00 - 32225:00

professional software developer route, I

## 32225:00 - 32250:00

think getting a computer science degree

## 32250:00 - 32290:00

and like learning fundamentals makes

## 32290:00 - 32345:00

sense. But if you want to be a a

## 32345:00 - 32365:00

creator, if you want to be a generalist

## 32365:00 - 32395:00

in this world, I don't think it's

## 32395:00 - 32425:00

necessary anymore to learn to code in

## 32425:00 - 32450:00

the more like traditional ways of

## 32450:00 - 32485:00

learning to code. I think you pick it up

## 32485:00 - 32530:00

by osmosis almost like like go go go to

## 32530:00 - 32570:00

replet and you know and start using it

## 32570:00 - 32605:00

and at some point you're going going to

## 32605:00 - 32625:00

run into some issue where you're going

## 32625:00 - 32650:00

to have to look at code or you're going

## 32650:00 - 32680:00

to have to look at logs just by being

## 32680:00 - 32715:00

resourceful having to Google around and

## 32715:00 - 32735:00

all that. You'll start picking it up.

## 32735:00 - 32760:00

And by the way, this is how our

## 32760:00 - 32780:00

generation kind of learned how to code,

## 32780:00 - 32800:00

right? when you were talking I'm like

## 32800:00 - 32820:00

that's what I did.

## 32820:00 - 32875:00

>> Yeah. And somehow uh it just became very

## 32875:00 - 32915:00

industrial and very formal over the

## 32915:00 - 32955:00

years like the way we made web apps is

## 32955:00 - 32985:00

like you just like start a notepad with

## 32985:00 - 33020:00

a you know HTML file and now you have to

## 33020:00 - 33050:00

like learn like webpack or whatever you

## 33050:00 - 33100:00

know it's like so um I think the future

## 33100:00 - 33155:00

of work is not really clear what is you

## 33155:00 - 33185:00

you know we can sort of like have some

## 33185:00 - 33230:00

like you know idea of like where where

## 33230:00 - 33260:00

the world is headed and so with with my

## 33260:00 - 33310:00

children I want them to have like as

## 33310:00 - 33360:00

broad uh based knowledge as possible. Uh

## 33360:00 - 33385:00

I want them to be as generalist as

## 33385:00 - 33420:00

possible. I want them to be as

## 33420:00 - 33450:00

generative as possible like being able

## 33450:00 - 33490:00

to like create a lot of ideas because

## 33490:00 - 33540:00

once the making of things gets easier.

## 33540:00 - 33585:00

The bottleneck goes back to to to like

## 33585:00 - 33620:00

how many ideas you can have.

## 33620:00 - 33680:00

>> Um and so I I I wouldn't put learning to

## 33680:00 - 33720:00

code as the top thing. I would put learn

## 33720:00 - 33755:00

to make things. Learn to make things

## 33755:00 - 33780:00

with code. Learn to make things with

## 33780:00 - 33820:00

video. learn to make like anything with

## 33820:00 - 33830:00

AI.

## 33830:00 - 33870:00

>> And so what do you think happens with

## 33870:00 - 33910:00

SAS generally if we're very soon able to

## 33910:00 - 33950:00

say create me a version of Google

## 33950:00 - 33990:00

Calendar or clone Docyign? What happens

## 33990:00 - 34015:00

to SAS? Do you think

## 34015:00 - 34080:00

>> we have stories today of um a lot of

## 34080:00 - 34115:00

people replacing hundreds of thousands

## 34115:00 - 34175:00

of dollars worth of SAS um with Replet?

## 34175:00 - 34200:00

The other day I heard a story from

## 34200:00 - 34260:00

someone who um you know they got quoted

## 34260:00 - 34310:00

$150,000 for a piece of software. He

## 34310:00 - 34340:00

went and made it in replet sold it to

## 34340:00 - 34395:00

his employer for $32,000

## 34395:00 - 34470:00

cost him $400. Companies that have a

## 34470:00 - 34500:00

platform developer community around it

## 34500:00 - 34535:00

and and plug-in ecosystem and things

## 34535:00 - 34570:00

like that. I think those are safe.

## 34570:00 - 34595:00

>> You're not going to be able to vibe code

## 34595:00 - 34655:00

Salesforce. I think the the vertical SAS

## 34655:00 - 34710:00

is is in trouble and I think it's my

## 34710:00 - 34735:00

guess it's already probably showing in

## 34735:00 - 34755:00

some of the metrics.

## 34755:00 - 34795:00

>> Okay, last question. What advice would

## 34795:00 - 34835:00

you give to um founders starting out

## 34835:00 - 34850:00

right now?

## 34850:00 - 34895:00

>> You know the best advice is what we what

## 34895:00 - 34920:00

you what you actually pointed out

## 34920:00 - 34965:00

earlier is work on the edge of what's

## 34965:00 - 34990:00

possible.

## 34990:00 - 35060:00

uh because uh one evolution of of AI or

## 35060:00 - 35090:00

models will make your business valuable

## 35090:00 - 35120:00

and suddenly you're first on market. I

## 35120:00 - 35165:00

find it rare to see founders that are

## 35165:00 - 35190:00

actually like sitting down trying to

## 35190:00 - 35230:00

actually predict the future and and and

## 35230:00 - 35280:00

maybe that's something that was you know

## 35280:00 - 35320:00

ill advised in the past but I think

## 35320:00 - 35355:00

right now trying to actually figure out

## 35355:00 - 35390:00

where things are headed is very very

## 35390:00 - 35435:00

important uh skill to have. So like make

## 35435:00 - 35480:00

some prediction uh figure out like how

## 35480:00 - 35530:00

to create like a crappy product that

## 35530:00 - 35570:00

would get better immediately as you

## 35570:00 - 35600:00

switch switch the model. I mean computer

## 35600:00 - 35630:00

use is a is is a great example.

## 35630:00 - 35660:00

>> Oh it's been an absolute pleasure. Thank

## 35660:00 - 35675:00

you so much for coming on.

## 35675:00 - 35690:00

>> Pleasure. Thank you.

## 35690:00 - 35750:00

>> See you next time. Thanks.

## 35750:00+

[Music]

