---
source: https://www.youtube.com/watch?v=UPGB-hsAoVY
title: The Powerful Alternative To Fine-Tuning
author: Y Combinator
date: 2026-02-27
views: 51102
description: >-
  Poetiq is a new startup founded by former DeepMind researchers that recently
  achieved a major jump on the ARC-AGI benchmark by layering a recursive
  self-improvement system on top of existing models. In this episode of
  Lightcone, Poetiq's Founder & CEO Ian Fischer joined us to discuss how small
  teams can build “reasoning harnesses” that outperform base models, what that
  means for startups and why automating prompt engineering may be one of the
  most powerful levers in AI today.


  Chapters:

  00:00 – Intro

  00:40 – What Is Poetiq?

  01:07 – Recursive Self-Improvement Explained

  02:07 – The Fine-Tuning Trap

  02:59 – “Stilts” for LLMs

  03:14 – Recursive Self-Improvement vs. Fine-Tuning

  05:05 – Taking the Top Spot on ARC-AGI

  06:37 – Beating Claude on Humanity’s Last Exam

  08:40 – How the Meta-System Works

  10:26 – Beyond RL: A New S-Curve

  11:32 – Automating Prompt Engineering

  13:37 – From 5% to 95% Performance

  14:50 – Early Access & Putting Your Agent on Stilts

  16:17 – From YC Founder to DeepMind Researcher

  18:29 – Advice for Engineers in the AI Era



  Apply to Y Combinator: https://www.ycombinator.com/apply

  Work at a startup: https://www.ycombinator.com/jobs
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:38:00.515Z
---

# The Powerful Alternative To Fine-Tuning

## 00:00 - 30:00

The world is changing so quickly. This

## 30:00 - 60:00

is probably a little bit obvious, but

## 60:00 - 105:00

you should just try things and and like

## 105:00 - 150:00

every day do something with AI. Last

## 150:00 - 215:00

summer, I took a weekend and used um

## 215:00 - 265:00

GPT5 to help me build an iPhone app. I

## 265:00 - 305:00

hadn't done that in a decade. And yeah,

## 305:00 - 335:00

it's so fast and so easy. And that was,

## 335:00 - 360:00

you know, an age ago. That was like 8

## 360:00 - 395:00

months ago. Uh now it's even faster and

## 395:00 - 430:00

easier. Don't limit yourself. like

## 430:00 - 455:00

anything that you imagine, you should

## 455:00 - 485:00

just try to use AI and see how far you

## 485:00 - 525:00

can get with it and you'll be, you know,

## 525:00 - 665:00

making the world better.

## 665:00 - 700:00

Welcome to another episode of the Light

## 700:00 - 740:00

Cone. Ian Fischer is the co-founder and

## 740:00 - 790:00

co-CEO of Poetic, which is building

## 790:00 - 835:00

recursively self-improving AI reasoning

## 835:00 - 880:00

harnesses for LLMs. Previously, he spent

## 880:00 - 905:00

a decade as a researcher at Google

## 905:00 - 955:00

DeepMind and founded a mobile devtools

## 955:00 - 995:00

company through YC years ago. Welcome,

## 995:00 - 1000:00

Ian.

## 1000:00 - 1030:00

>> Thank you. I'm so happy to be here.

## 1030:00 - 1065:00

>> What is Poetic? How's it different than

## 1065:00 - 1095:00

RL? You know, how's it different than

## 1095:00 - 1115:00

context engineering?

## 1115:00 - 1155:00

>> At Poetic, what we're building is a

## 1155:00 - 1185:00

recursively self-improving system. And

## 1185:00 - 1230:00

so, recursive self-improvement is this

## 1230:00 - 1255:00

uh, you know, kind of the holy grail of

## 1255:00 - 1290:00

AI where the AI is making itself

## 1290:00 - 1330:00

smarter. The core insight that we had is

## 1330:00 - 1360:00

that uh we could do recursive

## 1360:00 - 1400:00

self-improvement far faster and cheaper

## 1400:00 - 1440:00

than all of the other ways that people

## 1440:00 - 1485:00

had been proposing to do this. Uh and so

## 1485:00 - 1510:00

obviously I'm I can't go into details

## 1510:00 - 1555:00

about what that what that is um what our

## 1555:00 - 1595:00

particular approach is but um most of

## 1595:00 - 1640:00

the approaches out there involve you

## 1640:00 - 1705:00

know they require you to train a new LLM

## 1705:00 - 1745:00

from scratch and training LLMs from

## 1745:00 - 1775:00

scratch costs you know hundreds of

## 1775:00 - 1805:00

millions of dollars and takes uh months

## 1805:00 - 1825:00

of effort and so the

## 1825:00 - 1850:00

>> and then anthropic or openi will come

## 1850:00 - 1880:00

along and just eat your lunch in the

## 1880:00 - 1900:00

next model release

## 1900:00 - 1925:00

>> right right and you know of course

## 1925:00 - 1960:00

anthropic and openi and google they're

## 1960:00 - 1975:00

exploring train recursive

## 1975:00 - 2010:00

self-improvement but typically at that

## 2010:00 - 2060:00

level of um having the you know having

## 2060:00 - 2100:00

to train a new model uh for every step

## 2100:00 - 2130:00

of self-improvement that they do.

## 2130:00 - 2165:00

>> I mean that seems like actually the like

## 2165:00 - 2190:00

defining thing that a startup really

## 2190:00 - 2230:00

really wants. Like I know that I want to

## 2230:00 - 2260:00

take advantage of whatever the next

## 2260:00 - 2290:00

model is, but the second you're in

## 2290:00 - 2325:00

fine-tuning land, I'm spending, you

## 2325:00 - 2350:00

know, millions to hundreds of millions

## 2350:00 - 2385:00

of dollars and then guess what? like it

## 2385:00 - 2430:00

I just lit it on fire cuz you know the

## 2430:00 - 2455:00

next version of the frontier model comes

## 2455:00 - 2490:00

out and I'll never catch up. Whereas

## 2490:00 - 2535:00

like working with your systems means

## 2535:00 - 2570:00

that I will always have the thing that

## 2570:00 - 2610:00

is uh better than the thing that's out

## 2610:00 - 2640:00

of box and that's sort of like the holy

## 2640:00 - 2650:00

grail.

## 2650:00 - 2680:00

>> Yeah, we think that this is uh

## 2680:00 - 2705:00

incredibly valuable to anybody who's

## 2705:00 - 2745:00

building on top of uh large language

## 2745:00 - 2780:00

models and we don't view the uh you know

## 2780:00 - 2810:00

the frontier models as competitors.

## 2810:00 - 2850:00

They're, you know, they're the ones that

## 2850:00 - 2880:00

were using the stilts, you know,

## 2880:00 - 2910:00

building stilts to stand on top of, but

## 2910:00 - 2950:00

uh if we didn't have that, um that

## 2950:00 - 2975:00

foundational layer, then, you know,

## 2975:00 - 2995:00

poetic couldn't exist.

## 2995:00 - 3025:00

>> Yeah. I mean, being the smartest model,

## 3025:00 - 3055:00

uh you know, it's a game of inches

## 3055:00 - 3085:00

actually and like so those inches matter

## 3085:00 - 3090:00

a lot,

## 3090:00 - 3100:00

>> right? Right.

## 3100:00 - 3130:00

>> How do we actually get started? I mean,

## 3130:00 - 3160:00

you've built something that, uh,

## 3160:00 - 3210:00

basically any startup could use that,

## 3210:00 - 3255:00

uh, it's sort of like stilts really. We

## 3255:00 - 3305:00

have built a system that um uh can

## 3305:00 - 3345:00

automatically generate systems for your

## 3345:00 - 3390:00

particular problem that will always

## 3390:00 - 3420:00

outperform the underlying language

## 3420:00 - 3470:00

models and without kind of the massive

## 3470:00 - 3490:00

expense as you're saying about the

## 3490:00 - 3515:00

bitter lesson where you know what would

## 3515:00 - 3540:00

you what would you have done without

## 3540:00 - 3570:00

poetic you probably would have said okay

## 3570:00 - 3590:00

we're going to first collect a large

## 3590:00 - 3620:00

data set you know like tens of thousands

## 3620:00 - 3650:00

of examples for our particular problem

## 3650:00 - 3685:00

that we're working on and we're going to

## 3685:00 - 3720:00

fine-tune you know the best model we can

## 3720:00 - 3745:00

put get our hands

## 3745:00 - 3770:00

uh maybe that's you know one of the

## 3770:00 - 3795:00

frontier models or maybe it's an open

## 3795:00 - 3820:00

weights model doesn't particularly

## 3820:00 - 3850:00

matter. you're going to spend a lot of

## 3850:00 - 3875:00

money on that fine-tuning. The the

## 3875:00 - 3920:00

compute is so expensive. Uh and then at

## 3920:00 - 3945:00

the end of it, you have something that

## 3945:00 - 3975:00

uh you know works better than the thing

## 3975:00 - 4015:00

that you fine-tuned on top of, but by

## 4015:00 - 4060:00

then a new model's come out and it's

## 4060:00 - 4075:00

better than the thing that you

## 4075:00 - 4100:00

fine-tuned. You know, you fine-tuned,

## 4100:00 - 4145:00

you know, like 3 years ago on top of GPT

## 4145:00 - 4205:00

3.5 or whatever and then GPD 404 comes

## 4205:00 - 4230:00

out and it just blows you out of the

## 4230:00 - 4260:00

water. And so, are you going to do that

## 4260:00 - 4290:00

again or are you going to go out of

## 4290:00 - 4325:00

business? And like in some cases the the

## 4325:00 - 4370:00

latter with poetic uh what we end up

## 4370:00 - 4420:00

giving you is a uh you know people are

## 4420:00 - 4450:00

calling these things harnesses now but

## 4450:00 - 4480:00

you know or a gentic system or whatever

## 4480:00 - 4510:00

you want to call it that sits on top of

## 4510:00 - 4550:00

one or more language models and it just

## 4550:00 - 4590:00

performs better than them. Uh and when

## 4590:00 - 4625:00

the new model comes out that same

## 4625:00 - 4665:00

harness is uh perfectly compatible with

## 4665:00 - 4705:00

it. Uh and you don't need to change

## 4705:00 - 4745:00

anything to get the uh you know an even

## 4745:00 - 4775:00

uh bigger performance bump.

## 4775:00 - 4810:00

Additionally, we can, you know, continue

## 4810:00 - 4860:00

to optimize for this new model, whatever

## 4860:00 - 4900:00

the new model is that you want to use,

## 4900:00 - 4940:00

uh, and, you know, make it even better.

## 4940:00 - 4980:00

Uh, but you, you don't lose out on, you

## 4980:00 - 5000:00

know, hundreds of millions of dollars.

## 5000:00 - 5035:00

In fact, we do this so much more

## 5035:00 - 5085:00

cheaply, uh, than fine-tuning would cost

## 5085:00 - 5095:00

as well.

## 5095:00 - 5115:00

>> And you've done this actually a bunch of

## 5115:00 - 5140:00

times, right? Like I remember when you

## 5140:00 - 5160:00

first came out with your paper in

## 5160:00 - 5205:00

December of last year, uh you shot to

## 5205:00 - 5260:00

the top of ARC AGI V2 and then you've

## 5260:00 - 5280:00

done this a bunch of times for other

## 5280:00 - 5310:00

benchmarks too. What you know what was

## 5310:00 - 5320:00

that like?

## 5320:00 - 5380:00

>> ARGI v2 was this was kind of you us

## 5380:00 - 5400:00

coming out of stealth letting people

## 5400:00 - 5430:00

know that we could um tackle these

## 5430:00 - 5470:00

really hard problems. Uh and in

## 5470:00 - 5510:00

particular, you know, we wanted to show

## 5510:00 - 5565:00

that our system could generate these um

## 5565:00 - 5585:00

what we call, you know, we call our

## 5585:00 - 5615:00

system like the poetic meta system can

## 5615:00 - 5660:00

generate uh reasoning systems that are

## 5660:00 - 5710:00

um highly effective. Gemini 3 had deep

## 5710:00 - 5750:00

think had just come out. Uh and they

## 5750:00 - 5790:00

were, you know, really quite uh

## 5790:00 - 5815:00

dramatically at the top of the

## 5815:00 - 5870:00

leaderboard at 45%. Uh and two days

## 5870:00 - 5925:00

later we release our results where um uh

## 5925:00 - 5975:00

we were showing that we could get uh a

## 5975:00 - 6000:00

lot higher than that. Uh

## 6000:00 - 6025:00

>> so they come out with soda and then you

## 6025:00 - 6065:00

come in right above them every single

## 6065:00 - 6110:00

time which is like wild to see honestly.

## 6110:00 - 6135:00

That's what it's like to have stilt you

## 6135:00 - 6170:00

know like whatever model comes out you

## 6170:00 - 6205:00

can be taller than that one with poetic

## 6205:00 - 6230:00

which is like that's so awesome.

## 6230:00 - 6260:00

>> Yeah. So the interesting thing is that

## 6260:00 - 6305:00

uh we were half the cost of Gemini 3

## 6305:00 - 6335:00

deep think because we were building on

## 6335:00 - 6370:00

top of Gemini 3 Pro which is a much

## 6370:00 - 6420:00

cheaper model um but we still got uh in

## 6420:00 - 6450:00

the end a 9 percentage point improvement

## 6450:00 - 6495:00

on the official verification. So they

## 6495:00 - 6550:00

were at 45% and we and like 70s

## 6550:00 - 6600:00

something dollars and we were at 54% and

## 6600:00 - 6630:00

$32 per problem.

## 6630:00 - 6665:00

>> So recently you guys just announced some

## 6665:00 - 6700:00

incredible results for humanity's last

## 6700:00 - 6745:00

exam. Can you tell us more about those?

## 6745:00 - 6815:00

>> Humanity's last exam is a a set of 2500

## 6815:00 - 6855:00

really really hard questions written by

## 6855:00 - 6890:00

experts in uh many different domains.

## 6890:00 - 6935:00

They're they're meant to be uh

## 6935:00 - 6980:00

challenging even for uh PhDs in those

## 6980:00 - 7020:00

fields. AI hasn't passed it yet. Uh but

## 7020:00 - 7075:00

we got to 55% which is almost two

## 7075:00 - 7105:00

percentage points higher than the the

## 7105:00 - 7150:00

previous uh state-of-the-art which came

## 7150:00 - 7220:00

out just last week uh from uh Anthropic

## 7220:00 - 7290:00

with Claude Opus 4.6. They got 53.1% and

## 7290:00 - 7315:00

we got 55% on it.

## 7315:00 - 7360:00

>> And one thing that uh humanity last exam

## 7360:00 - 7410:00

doesn't publish is the cost of getting

## 7410:00 - 7455:00

those results. In your case, this run

## 7455:00 - 7500:00

was done with less than around six

## 7500:00 - 7520:00

figure. How much was it?

## 7520:00 - 7555:00

>> We didn't publish any uh cost for this,

## 7555:00 - 7605:00

but I can say that the the optimization

## 7605:00 - 7635:00

costs us less than 100k. Yeah.

## 7635:00 - 7660:00

>> Which is impressive because each of

## 7660:00 - 7720:00

these big foundation modeled train runs

## 7720:00 - 7750:00

are in the hundreds of millions of

## 7750:00 - 7795:00

dollars. And you guys, as a company,

## 7795:00 - 7825:00

you're only seven people.

## 7825:00 - 7865:00

>> That's right. Yeah. Yeah. Seven uh seven

## 7865:00 - 7885:00

research scientists and research

## 7885:00 - 7895:00

engineers. Yeah.

## 7895:00 - 7935:00

>> That's impressive. And I think the thing

## 7935:00 - 7955:00

that's very interesting about your

## 7955:00 - 7990:00

approach is sort of taking a very

## 7990:00 - 8025:00

scientific approach to the emergent

## 8025:00 - 8050:00

behaviors that a lot of the best

## 8050:00 - 8090:00

founders are doing with models. I think

## 8090:00 - 8135:00

a lot of uh founders that get very good

## 8135:00 - 8185:00

results for agents, they treat the

## 8185:00 - 8225:00

underlying model as a common layer that

## 8225:00 - 8265:00

you can switch in between. And there's

## 8265:00 - 8315:00

certain tasks for example for GPD 5.2

## 8315:00 - 8360:00

two like very hard to verify bugs gets

## 8360:00 - 8390:00

sent to that versus architecture that

## 8390:00 - 8445:00

gets sent to claw 4.6 six, but you're

## 8445:00 - 8480:00

kind of doing this automatically instead

## 8480:00 - 8535:00

of having a human conducting is uh very

## 8535:00 - 8560:00

impressive. I think there's something

## 8560:00 - 8590:00

more special going on underneath. Can

## 8590:00 - 8620:00

you tell us a bit about how it works?

## 8620:00 - 8655:00

>> Yeah, it sounds magical. So, what can

## 8655:00 - 8665:00

you tell us?

## 8665:00 - 8685:00

>> Right. You're you're So, you're getting

## 8685:00 - 8725:00

at a core a really core thing. You know,

## 8725:00 - 8780:00

these harnesses, they are um code,

## 8780:00 - 8825:00

prompts, data, you know, built on top of

## 8825:00 - 8860:00

one or more language models, right? And

## 8860:00 - 8895:00

so this is something that in principle

## 8895:00 - 8945:00

you can build by hand um or with like

## 8945:00 - 8985:00

cloud code or whatever. But uh in in

## 8985:00 - 9025:00

practice it takes a lot of work to do

## 9025:00 - 9060:00

these to to you know have all the

## 9060:00 - 9110:00

insights uh to make this uh to make

## 9110:00 - 9150:00

these work well. And so the core

## 9150:00 - 9180:00

technology that we've developed at

## 9180:00 - 9220:00

poetic is uh recursive self-improvement.

## 9220:00 - 9245:00

So we we have a recursively

## 9245:00 - 9280:00

self-improving uh system which we call

## 9280:00 - 9315:00

the poetic meta system. the output of

## 9315:00 - 9360:00

that system is systems that solve hard

## 9360:00 - 9400:00

problems. Um where a hard problem is you

## 9400:00 - 9425:00

know something that you if you gave it

## 9425:00 - 9460:00

to GPT52

## 9460:00 - 9490:00

uh it would struggle to give you a

## 9490:00 - 9530:00

reliable robust result you know just to

## 9530:00 - 9575:00

use an example. So this is a a very big

## 9575:00 - 9615:00

advantage for us. We can generate these

## 9615:00 - 9665:00

systems in a much more automated manner.

## 9665:00 - 9685:00

uh which means that we can do it much

## 9685:00 - 9710:00

more quickly and much more cheaply than

## 9710:00 - 9750:00

if you hired a team yourself to try to

## 9750:00 - 9795:00

make um your own you know your own agent

## 9795:00 - 9835:00

to solve your particular task. But not

## 9835:00 - 9885:00

only that um since you know this is

## 9885:00 - 9905:00

really an automated optimization

## 9905:00 - 9935:00

process. If you already have done that

## 9935:00 - 9975:00

work you you know you're a you're a

## 9975:00 - 10000:00

startup that's like going after a

## 10000:00 - 10025:00

particular vertical and you've put

## 10025:00 - 10040:00

together you know you think you

## 10040:00 - 10060:00

understand your your problem pretty

## 10060:00 - 10090:00

well. You've put together your agent and

## 10090:00 - 10125:00

you you uh you know maybe it's working

## 10125:00 - 10150:00

pretty well but you know you can get

## 10150:00 - 10175:00

something better or you really need

## 10175:00 - 10210:00

something better. Um then you can bring

## 10210:00 - 10270:00

that to us uh and we can optimize uh

## 10270:00 - 10310:00

that entire agent or pieces of that

## 10310:00 - 10335:00

agent. So we could optimize just the

## 10335:00 - 10365:00

prompts, just the reasoning strategies.

## 10365:00 - 10390:00

Uh there's a lot of different things

## 10390:00 - 10420:00

that we can do uh depending on your

## 10420:00 - 10440:00

particular needs.

## 10440:00 - 10460:00

>> It sounds like this is a complete

## 10460:00 - 10495:00

different paradigm than RL because we

## 10495:00 - 10530:00

went through the scurve of regular

## 10530:00 - 10560:00

pre-training

## 10560:00 - 10625:00

RL with when OpenAI released 01 and now

## 10625:00 - 10670:00

this feels like a new one. It sounds

## 10670:00 - 10710:00

special. It sounds it rhymes a lot with

## 10710:00 - 10725:00

RNN's

## 10725:00 - 10760:00

>> which is a whole different paradigm than

## 10760:00 - 10800:00

than RL, right? It's going to depend on

## 10800:00 - 10825:00

the particular task, the particular type

## 10825:00 - 10855:00

of problem that we're going after that

## 10855:00 - 10895:00

we're trying to solve. Um, and the

## 10895:00 - 10920:00

underlying models that we're working

## 10920:00 - 10975:00

with. But, uh, effectively you could say

## 10975:00 - 11015:00

like each model or each set of models

## 11015:00 - 11040:00

that we're working with will have it

## 11040:00 - 11085:00

their own uh, scurve. The poetic system,

## 11085:00 - 11125:00

the poetic meta system itself is also

## 11125:00 - 11150:00

going to have its own scurve. And so as

## 11150:00 - 11175:00

the poetic meta system gets better and

## 11175:00 - 11205:00

as the underlying models get better, you

## 11205:00 - 11235:00

you'll find that the uh you know the

## 11235:00 - 11265:00

S-curve that you're dealing with keeps

## 11265:00 - 11295:00

shifting higher and higher until

## 11295:00 - 11335:00

ultimately either you saturate or like

## 11335:00 - 11350:00

>> reach AGI.

## 11350:00 - 11380:00

>> Yeah. Reach AGI, reach super

## 11380:00 - 11405:00

intelligences. Yeah.

## 11405:00 - 11440:00

>> Given its stilts, you might like hit the

## 11440:00 - 11460:00

ceiling first then.

## 11460:00 - 11480:00

>> That's the goal, right? Yeah,

## 11480:00 - 11530:00

>> you want to hit the ceiling first with

## 11530:00 - 11555:00

>> I think a lot of startups that we work

## 11555:00 - 11605:00

with um and then in my spare time I you

## 11605:00 - 11640:00

know do a bunch of context engineering

## 11640:00 - 11670:00

and then the thing is we're sort of like

## 11670:00 - 11715:00

tuning it tuning evals tuning like we're

## 11715:00 - 11755:00

context stuffing ourselves. What does

## 11755:00 - 11790:00

that even feel like to have a you know

## 11790:00 - 11835:00

recursively self-improving version of

## 11835:00 - 11865:00

like prompt engineering and context

## 11865:00 - 11920:00

engineering? we don't spend a lot of

## 11920:00 - 11960:00

time looking at the particular data that

## 11960:00 - 12005:00

we're working with. Uh instead, we're

## 12005:00 - 12045:00

letting the poetic meta system look at

## 12045:00 - 12085:00

that data and and so like the meta

## 12085:00 - 12115:00

system, you know, if it if it thinks

## 12115:00 - 12150:00

that it needs to put more things into

## 12150:00 - 12180:00

context, it do more context stuffing or

## 12180:00 - 12215:00

whatever, it'll it'll do that. If it

## 12215:00 - 12240:00

needs to like generate a bunch of

## 12240:00 - 12310:00

examples um uh to get the get better

## 12310:00 - 12335:00

performance, it'll do that for you,

## 12335:00 - 12360:00

right? It it was pretty interesting to

## 12360:00 - 12410:00

look at the um prompt outputs in

## 12410:00 - 12470:00

particular I'd say for ArcGI in that you

## 12470:00 - 12500:00

know I think you can read those and say

## 12500:00 - 12535:00

well that's not what a human would have

## 12535:00 - 12600:00

written uh pretty clearly and and it's

## 12600:00 - 12625:00

you know there's some unexpected stuff

## 12625:00 - 12660:00

and you know it made some really simple

## 12660:00 - 12685:00

examples and one of the examples is

## 12685:00 - 12720:00

actually wrong but we didn't change it.

## 12720:00 - 12745:00

We're like well this is you know this is

## 12745:00 - 12790:00

the thing that it output we'll just

## 12790:00 - 12830:00

leave it be. um you know we don't want

## 12830:00 - 12860:00

to go in and monkey around with things

## 12860:00 - 12905:00

and so historically in machine learning

## 12905:00 - 12940:00

you always you know is like the the rule

## 12940:00 - 12970:00

was you have to know your data set

## 12970:00 - 13010:00

really well um but now we're kind of

## 13010:00 - 13055:00

outsourcing that to the AI itself where

## 13055:00 - 13095:00

the AI is it's the AI's job to

## 13095:00 - 13130:00

understand the data set and figure out

## 13130:00 - 13180:00

where are the failure modes um and where

## 13180:00 - 13205:00

are the kind of robust reasoning

## 13205:00 - 13250:00

strategies that uh the model that that

## 13250:00 - 13310:00

the agent could uh use um to get better

## 13310:00 - 13320:00

performance.

## 13320:00 - 13345:00

>> How much of it is like much you the

## 13345:00 - 13375:00

output is much better prompts and then

## 13375:00 - 13405:00

how much of it is like the harness

## 13405:00 - 13450:00

itself uh context stuffing or

## 13450:00 - 13475:00

summarizing in the right way or

## 13475:00 - 13510:00

reranking in the right way so that like

## 13510:00 - 13550:00

you you have some number of like mega

## 13550:00 - 13585:00

LLM calls and then how do you get the

## 13585:00 - 13630:00

most out of um each of those calls?

## 13630:00 - 13665:00

>> Yeah. And so that definitely varies per

## 13665:00 - 13715:00

problem. But uh what we've seen, in

## 13715:00 - 13760:00

fact, our our last paper at DeepMind was

## 13760:00 - 13790:00

not doing this recursive self-improving

## 13790:00 - 13840:00

stuff, but we were um we were showing

## 13840:00 - 13880:00

that you could build these harnesses um

## 13880:00 - 13920:00

manually to solve really hard problems.

## 13920:00 - 13965:00

And what we saw is there is that uh you

## 13965:00 - 14005:00

know, we manually optimized the prompts

## 14005:00 - 14030:00

really hard for these very hard

## 14030:00 - 14060:00

problems. And that got us a little bit

## 14060:00 - 14100:00

of the way uh in this particular case.

## 14100:00 - 14125:00

you know the the hardest the hardest

## 14125:00 - 14160:00

task we were working on we got like to

## 14160:00 - 14210:00

5% performance with Gemini 1.5 flash

## 14210:00 - 14255:00

this was a while ago and then when we

## 14255:00 - 14310:00

added on the the reasoning strategies we

## 14310:00 - 14365:00

went from 5% to 95%

## 14365:00 - 14405:00

>> uh and so this is typically what we see

## 14405:00 - 14435:00

you know like everybody's out there kind

## 14435:00 - 14460:00

of doing some amount I wouldn't say

## 14460:00 - 14485:00

everybody but many people are out there

## 14485:00 - 14510:00

kind of doing some amount of automated

## 14510:00 - 14550:00

prop pro prompt optimization you know

## 14550:00 - 14580:00

Jeepa is this very popular paper

## 14580:00 - 14605:00

everybody's kind of implementing that

## 14605:00 - 14630:00

that will get you some performance

## 14630:00 - 14695:00

improvements, but it's very far from uh

## 14695:00 - 14745:00

everything that you can get uh if you

## 14745:00 - 14770:00

actually think about these reasoning

## 14770:00 - 14795:00

strategies that are really going to be

## 14795:00 - 14825:00

written in code rather than in in just

## 14825:00 - 14840:00

better prompts.

## 14840:00 - 14905:00

>> So if startups want to use poetic to put

## 14905:00 - 14935:00

their agent on stilts, what should they

## 14935:00 - 14950:00

do?

## 14950:00 - 14985:00

>> Yeah, so right now uh we haven't

## 14985:00 - 15020:00

released anything yet, but uh if you go

## 15020:00 - 15065:00

to poetic.ai, AI. Uh there is a button

## 15065:00 - 15110:00

you can click to get uh sign up for

## 15110:00 - 15145:00

early access. And if you're a startup uh

## 15145:00 - 15185:00

or a company who has a really hard

## 15185:00 - 15215:00

problem uh and you've tried everything

## 15215:00 - 15275:00

that you can to make it uh reliable and

## 15275:00 - 15305:00

robust and you just can't get all the

## 15305:00 - 15330:00

way there, you you need something more,

## 15330:00 - 15375:00

then uh let us know. We're looking for

## 15375:00 - 15410:00

problems like that. Uh so just tell us

## 15410:00 - 15430:00

tell us what it is that you're working

## 15430:00 - 15475:00

on and uh we'll reach out. You'll be the

## 15475:00 - 15495:00

first to know when we're when we're

## 15495:00 - 15515:00

ready to work with you. I mean, if

## 15515:00 - 15545:00

you're at the top of um humanity's last

## 15545:00 - 15595:00

exam, then I mean, that's that's pretty

## 15595:00 - 15635:00

big. So, it's you're all you're already

## 15635:00 - 15675:00

all the way out there at soda and then I

## 15675:00 - 15705:00

guess the stilts basically let any

## 15705:00 - 15740:00

agentic company become soda.

## 15740:00 - 15780:00

>> That's the idea. Yeah. Yeah. And you

## 15780:00 - 15815:00

know, we view the ArcGI results and the

## 15815:00 - 15860:00

humanities last exam results as showing

## 15860:00 - 15895:00

kind of two different uh capabilities

## 15895:00 - 15920:00

that we have. We can really improve your

## 15920:00 - 15960:00

reasoning and we can really improve uh

## 15960:00 - 15990:00

deep knowledge extraction uh from these

## 15990:00 - 16000:00

models

## 16000:00 - 16030:00

>> and then you're just totally vaccinated

## 16030:00 - 16055:00

against the bitter lesson.

## 16055:00 - 16065:00

>> Exactly.

## 16065:00 - 16105:00

>> YC's next batch is now taking

## 16105:00 - 16140:00

applications. Got a startup in you?

## 16140:00 - 16190:00

Apply at y combinator.com/apply.

## 16190:00 - 16230:00

It's never too early and filling out the

## 16230:00 - 16280:00

app will level up your idea. Okay, back

## 16280:00 - 16300:00

to the video.

## 16300:00 - 16320:00

>> Slight sort of change change of topic,

## 16320:00 - 16360:00

but something I was curious about. Uh so

## 16360:00 - 16390:00

you arrived at Google over a decade ago

## 16390:00 - 16430:00

when they acquired your first YC startup

## 16430:00 - 16475:00

at portable. A portable was it's porting

## 16475:00 - 16510:00

mobile apps crossplatform right like

## 16510:00 - 16545:00

Android or or whatever. It's quite

## 16545:00 - 16600:00

different to um recursive self-improving

## 16600:00 - 16650:00

AGI. Um how did you make that leap? What

## 16650:00 - 16705:00

happened once you got to Google? Um what

## 16705:00 - 16725:00

made you think that you maybe wanted to

## 16725:00 - 16750:00

shift out and do something different?

## 16750:00 - 16775:00

And just would love to hear that story.

## 16775:00 - 16820:00

the acquisition uh was this amazing

## 16820:00 - 16890:00

opportunity to um reflect on what I

## 16890:00 - 16930:00

really wanted to be doing next, right?

## 16930:00 - 16990:00

Like Google was in, you know, itself is

## 16990:00 - 17010:00

a place where you can do so many

## 17010:00 - 17065:00

different things. Uh so I spent some

## 17065:00 - 17135:00

time thinking about um where uh where I

## 17135:00 - 17175:00

wanted to go next in in uh in my

## 17175:00 - 17235:00

journey. I realized that the problems

## 17235:00 - 17270:00

that I was most excited about were

## 17270:00 - 17340:00

really actually AI and uh and robotics.

## 17340:00 - 17395:00

Um and the best people in the world,

## 17395:00 - 17430:00

many of them in those fields were at

## 17430:00 - 17495:00

Google at the time. Uh and so I went and

## 17495:00 - 17565:00

talked to them. they uh let me come join

## 17565:00 - 17630:00

you know a new AI robotics team uh in

## 17630:00 - 17660:00

Google research which was this amazing

## 17660:00 - 17700:00

opportunity for me since that wasn't my

## 17700:00 - 17730:00

background my background was like uh

## 17730:00 - 17755:00

computer security and then this

## 17755:00 - 17785:00

crossplatform mobile you know it's

## 17785:00 - 17830:00

systems building uh stuff I was able to

## 17830:00 - 17875:00

join this team and I I'll tell you the

## 17875:00 - 17910:00

truth that uh I very quickly realized

## 17910:00 - 17955:00

that uh hardware is hard uh and I didn't

## 17955:00 - 17990:00

really want to be doing robotics is more

## 17990:00 - 18015:00

aspirational at that moment

## 18015:00 - 18065:00

uh but I was really um uh passionate

## 18065:00 - 18120:00

about machine learning. So I just uh uh

## 18120:00 - 18155:00

made a very hard switch into just doing

## 18155:00 - 18190:00

machine learning research uh and did

## 18190:00 - 18230:00

that for you know about a decade at

## 18230:00 - 18265:00

Google and and then Google and then deep

## 18265:00 - 18275:00

mind.

## 18275:00 - 18315:00

>> What's maybe some advice that you have

## 18315:00 - 18360:00

today for engineers who want to get into

## 18360:00 - 18410:00

sort of more of the AI side probably the

## 18410:00 - 18445:00

applied AI and build startups around AI

## 18445:00 - 18475:00

like how should they think about that?

## 18475:00 - 18500:00

You know, the world is changing so

## 18500:00 - 18545:00

quickly. This is probably a little bit

## 18545:00 - 18585:00

obvious, but you should just try things

## 18585:00 - 18640:00

and and like every day uh do something

## 18640:00 - 18685:00

uh do something with AI. Always try to

## 18685:00 - 18710:00

push yourself to find the boundaries of

## 18710:00 - 18785:00

what they're capable of. Uh and uh and

## 18785:00 - 18815:00

build the things that you that you want

## 18815:00 - 18880:00

to build, right? Um, even even for me,

## 18880:00 - 18930:00

you know, last summer I took a weekend

## 18930:00 - 18995:00

and used um GPT5 to help me build an

## 18995:00 - 19030:00

iPhone app. I hadn't I hadn't done that

## 19030:00 - 19060:00

in a decade. So fast.

## 19060:00 - 19085:00

>> Yeah, it's so fast and so easy. And that

## 19085:00 - 19120:00

was, you know, that was an, you know, an

## 19120:00 - 19150:00

age ago. That was like eight months ago.

## 19150:00 - 19185:00

Uh, now it's even faster and easier.

## 19185:00 - 19215:00

Don't limit yourself. Like anything that

## 19215:00 - 19245:00

you imagine, you should just try to use

## 19245:00 - 19280:00

AI and see how far you can get with it

## 19280:00 - 19310:00

and you'll be, you know, making the

## 19310:00 - 19335:00

world better. That's all we have time

## 19335:00 - 19370:00

for today, but Ian, thank you so much

## 19370:00 - 19410:00

for giving us all Stilts. Uh, we can't

## 19410:00 - 19445:00

wait to use it at YC. I can't wait to

## 19445:00 - 19485:00

use it for Gary's list. I mean, there's

## 19485:00 - 19515:00

just so much to do. So,

## 19515:00 - 19540:00

>> yeah, thank you for having me. This was

## 19540:00+

a lot of fun.

