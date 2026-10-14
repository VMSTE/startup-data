---
source: https://www.youtube.com/watch?v=GmcTq0Zo8kM
title: "Anthropic Chief Product Officer: Why AI Model Development Is Accelerating"
author: Alex Kantrowitz
date: 2025-10-08
views: 12846
description: >-
  Mike Krieger is the chief product officer at Anthropic and co-founder of
  Instagram. Krieger joins Big Technology Podcast to discuss Anthropic's Sonnet
  4.5 launch and how the company's been able to speed up AI model development.
  Tune in to hear how Anthropic is using internal tools to move fast, where the
  next generations of model improvements will look like, and whether model
  orchestration will be the core  differentiator between labs. We also cover how
  AI development compares to social media, whether AI content will ever take
  off, and enterprise AI's path ahead. 


  Chapters


  00:00 – Why AI releases are speeding up

  03:38 – Scale vs algorithms: what drives progress

  06:27 – From code assist to proactive agents

  08:49 – Defining agents: autonomy, tools, memory

  11:27 – Orchestration vs output: hitting quality bar

  13:06 – Sonnet 4.5 gains: cost and performance

  15:27 – How 4.5 undercuts Opus on cost

  26:17 – Memory built into the base model

  43:48 – Coding race versus OpenAI: real tasks

  46:27 – Enterprise adoption: from pilots to production


  ---


  Want a discount for Big Technology on Substack + Discord? Here’s 25% off for
  the first year: https://www.bigtechnology.com/subscribe?coupon=0843016b

  Enjoying Big Technology Podcast? Please rate us five stars ⭐⭐⭐⭐⭐ in your
  podcast app of choice.

  Questions? Feedback? Write to: bigtechnologypodcast@gmail.com
tags:
  - Anthropic
  - Claude 4.5
  - machine learning
  - product development
  - customer feedback
  - automation
  - coding
  - enterprise AI
  - social media
  - user engagement
  - AI
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:48:03.501Z
---

# Anthropic Chief Product Officer: Why AI Model Development Is Accelerating

## 00:00 - 35:00

Anthropic product head Mike Kger joins

## 35:00 - 70:00

us to talk about how AI model

## 70:00 - 110:00

development is accelerating and what we

## 110:00 - 145:00

should look out for as things continue

## 145:00 - 185:00

to move faster. That's coming up right

## 185:00 - 225:00

after this. Welcome to Big Technology

## 225:00 - 255:00

Podcast, a show for coolheaded and

## 255:00 - 300:00

nuanced conversation of the tech world

## 300:00 - 345:00

and beyond. Well, Anthropic has a new

## 345:00 - 400:00

model out, Sonnet 4.5, just months after

## 400:00 - 450:00

the series of uh Claude 4 models came

## 450:00 - 485:00

out. So things are moving fast and we're

## 485:00 - 515:00

going to figure out why they're moving

## 515:00 - 550:00

much faster and what the implications

## 550:00 - 610:00

are for the AI industry and businesses

## 610:00 - 635:00

as a whole. And we're joined today by

## 635:00 - 670:00

the perfect guest to do it. Anthropic

## 670:00 - 705:00

product head Mike Kger is here with us.

## 705:00 - 720:00

Mike, it's good to see you again.

## 720:00 - 735:00

Welcome to the show.

## 735:00 - 770:00

>> It's good to be here. Thanks, Alex.

## 770:00 - 815:00

>> So I remember sitting in the audience

## 815:00 - 875:00

for Anthropic's first developer day. And

## 875:00 - 910:00

it's funny because in the AI world, you

## 910:00 - 950:00

sort of you go and what is it? cat years

## 950:00 - 995:00

or dog years, I don't even know. Every

## 995:00 - 1035:00

every month feels like a year. And uh

## 1035:00 - 1090:00

this was in May, May 2025. And I

## 1090:00 - 1125:00

remember yourself and Dario were on

## 1125:00 - 1165:00

stage saying, "Yes, we're we releasing

## 1165:00 - 1205:00

Claude 4 uh but you know, we're going to

## 1205:00 - 1250:00

release the next iterations much faster

## 1250:00 - 1280:00

than we ever have uh previously and

## 1280:00 - 1325:00

we're already at 4.5. How is it

## 1325:00 - 1345:00

happening?"

## 1345:00 - 1370:00

>> I think there's a couple of things that

## 1370:00 - 1400:00

we're seeing. I mean even just thinking

## 1400:00 - 1435:00

about I mean May again feels like a year

## 1435:00 - 1470:00

ago I think doggeears is about right. I

## 1470:00 - 1510:00

think there's a couple of things. One is

## 1510:00 - 1555:00

um we've been working much more with

## 1555:00 - 1600:00

sort of enduser sort of customers of for

## 1600:00 - 1640:00

example of our platform. Um and with

## 1640:00 - 1680:00

that we can hear like a much faster

## 1680:00 - 1720:00

feedback loop of hey signet 4 is great

## 1720:00 - 1745:00

in these ways. We wish it was better in

## 1745:00 - 1770:00

these ways. And you're starting to get

## 1770:00 - 1805:00

customers that really push the models in

## 1805:00 - 1830:00

really interesting ways. And that ends

## 1830:00 - 1855:00

up being very helpful for us on the

## 1855:00 - 1880:00

research side because then we can say

## 1880:00 - 1905:00

all right these are problems to be

## 1905:00 - 1950:00

tackled in the next uh version of cloud.

## 1950:00 - 1995:00

So for example uh one of them was uh you

## 1995:00 - 2025:00

know claude you know sonet 4 and even

## 2025:00 - 2075:00

opus for opus is our biggest model um is

## 2075:00 - 2105:00

good at writing code but you know tends

## 2105:00 - 2135:00

to get sidetracked or lost if it's

## 2135:00 - 2165:00

working over longer time horizons. that

## 2165:00 - 2225:00

was a real emphasis uh of sonnet 4.5 or

## 2225:00 - 2265:00

you know we you know put a lot of data

## 2265:00 - 2295:00

into the context basically how the model

## 2295:00 - 2320:00

is what it's thinking about in a given

## 2320:00 - 2350:00

point but at some point that gets filled

## 2350:00 - 2375:00

up and how do you then manage you know

## 2375:00 - 2410:00

to keep working on those things so

## 2410:00 - 2440:00

having that feedback loop really helps

## 2440:00 - 2470:00

and also gives us a lot of urgency

## 2470:00 - 2505:00

because it means that there's sort of

## 2505:00 - 2545:00

sort of almost like bugs in some ways

## 2545:00 - 2570:00

out you know that you want to go fix or

## 2570:00 - 2595:00

at least like feature requests that you

## 2595:00 - 2620:00

want to go fix. So that's that's one

## 2620:00 - 2640:00

piece. The other one is we've just

## 2640:00 - 2670:00

streamlined a lot more of our model

## 2670:00 - 2720:00

release story. So um I think uh having

## 2720:00 - 2755:00

now seen you know I joined shortly

## 2755:00 - 2815:00

before sonnet 3.5 which was back in like

## 2815:00 - 2845:00

May of last year. So really long time

## 2845:00 - 2900:00

ago in AI years um uh from then to now

## 2900:00 - 2945:00

just the sort of operational upleveling

## 2945:00 - 2975:00

that I think we've seen in terms of you

## 2975:00 - 3010:00

know how do we do how do we get uh early

## 3010:00 - 3040:00

access feedback from customers? How do

## 3040:00 - 3085:00

we give like the remainder of customers

## 3085:00 - 3115:00

uh like a good heads up so they can la

## 3115:00 - 3145:00

they can co-launch on launch day? What

## 3145:00 - 3170:00

does even that morning look like on roll

## 3170:00 - 3195:00

out? I was talking to a customer. He's

## 3195:00 - 3225:00

like, I've seen a lot of lab rollouts of

## 3225:00 - 3245:00

of models and this was like the

## 3245:00 - 3280:00

smoothest I've seen which I like took as

## 3280:00 - 3315:00

like a big endorsement of how much we've

## 3315:00 - 3340:00

like streamlined that model release

## 3340:00 - 3375:00

process. That just makes it so that like

## 3375:00 - 3405:00

every release doesn't feel like, you

## 3405:00 - 3450:00

know, this very, you know, bespoke, very

## 3450:00 - 3485:00

difficult process. It can be much more a

## 3485:00 - 3510:00

great like we know what we're doing.

## 3510:00 - 3535:00

Here's the date. to the extent that

## 3535:00 - 3555:00

research can be predictable which it

## 3555:00 - 3585:00

can't be but within that domain uh how

## 3585:00 - 3610:00

do we actually make that as smooth as

## 3610:00 - 3625:00

possible

## 3625:00 - 3700:00

>> right and maybe um I'm looking at this

## 3700:00 - 3765:00

from a dumb outsers perspective but the

## 3765:00 - 3785:00

one thing that I didn't hear you mention

## 3785:00 - 3845:00

was scale and you know hearing so much

## 3845:00 - 3880:00

about the scaling laws especially from

## 3880:00 - 3915:00

anthropic you know part of me believe

## 3915:00 - 3970:00

that like okay four is you know cloud 4

## 3970:00 - 4025:00

is x number of GPUs and 4.5 is I number

## 4025:00 - 4070:00

of GPUs and five will be Z number of

## 4070:00 - 4130:00

GPUs. So does the numbers in your model

## 4130:00 - 4195:00

release you know um uh rubric correlate

## 4195:00 - 4245:00

at all with the scale of the data

## 4245:00 - 4265:00

centers that you're trading on and the

## 4265:00 - 4305:00

scale of the data. I mean I think what's

## 4305:00 - 4340:00

been interesting is um at different

## 4340:00 - 4370:00

points and if you talk to to Jared

## 4370:00 - 4395:00

Cavlin who's our chief scientist he'll

## 4395:00 - 4435:00

he'll I think tell you much the same is

## 4435:00 - 4480:00

um the scaling laws I think paint a

## 4480:00 - 4520:00

picture of what is possible but is not

## 4520:00 - 4550:00

predetermined like to actually get there

## 4550:00 - 4575:00

there's a lot of actually really

## 4575:00 - 4595:00

difficult both machine learning and

## 4595:00 - 4625:00

engineering work. So I think one thing

## 4625:00 - 4650:00

that's been notable to your question

## 4650:00 - 4680:00

about scale over the last you know 6

## 4680:00 - 4715:00

months is how much it's been really

## 4715:00 - 4745:00

engineering like if you're going to do

## 4745:00 - 4780:00

both pre-training and post-training on

## 4780:00 - 4825:00

an increasingly large number of uh of

## 4825:00 - 4850:00

accelerators how do you make that

## 4850:00 - 4885:00

reliable how do you keep that um you

## 4885:00 - 4920:00

know how you keep that run as we call it

## 4920:00 - 4950:00

like going even if you know some portion

## 4950:00 - 5010:00

of it uh has an issue so a lot of the uh

## 5010:00 - 5035:00

I think to your question a lot of the

## 5035:00 - 5060:00

the improvement in our ability to

## 5060:00 - 5085:00

deliver these models really has come

## 5085:00 - 5105:00

from our ability to run these large

## 5105:00 - 5145:00

training runs at scale which you know

## 5145:00 - 5170:00

again fundamentally an engineering and

## 5170:00 - 5195:00

machine learning problem I think both

## 5195:00 - 5240:00

have improved uh I think if I pointed at

## 5240:00 - 5270:00

something between sonnet 4 and 45 a lot

## 5270:00 - 5290:00

of it really has been on the engineering

## 5290:00 - 5320:00

side to just be able to scale up um

## 5320:00 - 5340:00

especially a lot of the post- training

## 5340:00 - 5345:00

work

## 5345:00 - 5360:00

>> if I'm reading you're right it's not

## 5360:00 - 5390:00

necessarily gains that anthropic is

## 5390:00 - 5435:00

seeing from scaling up the data centers

## 5435:00 - 5480:00

it is algorithmic work that is being

## 5480:00 - 5510:00

done by your teams to make the models

## 5510:00 - 5520:00

better

## 5520:00 - 5545:00

>> they really come together I think it's

## 5545:00 - 5570:00

the algorithmic work and then the

## 5570:00 - 5605:00

ability to maximize the amount of uh

## 5605:00 - 5640:00

compute that we can use like on those

## 5640:00 - 5665:00

algorithmic improvements. So they really

## 5665:00 - 5695:00

kind of go hand inand sometimes directly

## 5695:00 - 5735:00

hand inand in that um you know either uh

## 5735:00 - 5765:00

an idea that works at small scale when

## 5765:00 - 5795:00

you scale it up doesn't work as well and

## 5795:00 - 5830:00

then other times an idea only works when

## 5830:00 - 5855:00

you get enough data and scale in there

## 5855:00 - 5880:00

as well. So it really becomes, you know,

## 5880:00 - 5910:00

when we when I think about our our team,

## 5910:00 - 5945:00

we actually just brought in um a new

## 5945:00 - 6005:00

CTO. Um and uh a lot of I think his

## 6005:00 - 6045:00

remit will be how do you really partner

## 6045:00 - 6080:00

research and our like kind of core

## 6080:00 - 6110:00

engineering teams together to achieve

## 6110:00 - 6135:00

that kind of scale.

## 6135:00 - 6165:00

>> Okay. And another thing I was expecting

## 6165:00 - 6190:00

you to say, which I'm not sure if I've

## 6190:00 - 6225:00

heard yet, is that teams within

## 6225:00 - 6285:00

Anthropic have used the uh coding

## 6285:00 - 6320:00

capabilities of your AI models to be

## 6320:00 - 6365:00

able to ship faster. Is that a sort of

## 6365:00 - 6405:00

supporting character here or is it is it

## 6405:00 - 6425:00

the star?

## 6425:00 - 6485:00

>> I think it's um it's a good I'll have to

## 6485:00 - 6505:00

think about that for a sec. I think it's

## 6505:00 - 6530:00

a little bit of both. I would actually

## 6530:00 - 6565:00

say there's there's a thing that is

## 6565:00 - 6595:00

emergent even beyond the coding

## 6595:00 - 6625:00

capabilities which is the ability of

## 6625:00 - 6670:00

Claude to be a really active participant

## 6670:00 - 6700:00

in the process. And here's what I mean

## 6700:00 - 6740:00

by that. Um you know I think about the

## 6740:00 - 6765:00

way Claude was being used around even

## 6765:00 - 6830:00

sonnet 4. um was uh you know help write

## 6830:00 - 6875:00

code you know to to launch these models

## 6875:00 - 6915:00

help write the product code for sure

## 6915:00 - 6940:00

contribute really strongly to cloud code

## 6940:00 - 6965:00

you can imagine cloud code itself is

## 6965:00 - 7010:00

like a very sort of uh we use cloud code

## 7010:00 - 7035:00

to develop cloud code very much in a

## 7035:00 - 7075:00

loop I think that the biggest delta

## 7075:00 - 7100:00

between four and four five is that now

## 7100:00 - 7155:00

we have much more of uh claude as an

## 7155:00 - 7205:00

agent or almost like a co-orker in for

## 7205:00 - 7240:00

example our slack channels so for

## 7240:00 - 7280:00

example we have um uh something we built

## 7280:00 - 7310:00

that's clawed on call. So if you've been

## 7310:00 - 7340:00

an engineer uh one of the things you

## 7340:00 - 7365:00

have to do is you know you take the

## 7365:00 - 7400:00

metaphorical pager uh which is basically

## 7400:00 - 7425:00

you're on call for a week or two to

## 7425:00 - 7475:00

manage a system and you know if you get

## 7475:00 - 7510:00

paged um you'll show up and say like all

## 7510:00 - 7540:00

right there's certain number of things

## 7540:00 - 7560:00

that could be wrong. I got to go check

## 7560:00 - 7590:00

these graphs. I got to maybe try this

## 7590:00 - 7630:00

out. And uh one thing that we've built

## 7630:00 - 7665:00

using uh the cloud agent SDK, which we

## 7665:00 - 7705:00

also released alongside its sonet 4.5

## 7705:00 - 7720:00

publicly, but we've been using

## 7720:00 - 7755:00

internally for a while, is the ability

## 7755:00 - 7785:00

for for cloud to basically show up first

## 7785:00 - 7820:00

in those incident channels and already

## 7820:00 - 7855:00

have a sense of what might be going on

## 7855:00 - 7880:00

and be able to answer really quickly,

## 7880:00 - 7910:00

hey, can you do some data diving while I

## 7910:00 - 7945:00

work on something else? Um and so we've

## 7945:00 - 7985:00

increasingly had Claude play these sort

## 7985:00 - 8025:00

of um yeah, these really collaborative

## 8025:00 - 8070:00

roles within our company even beyond the

## 8070:00 - 8095:00

ability to code. And it's again using

## 8095:00 - 8125:00

the same technology as cloud code under

## 8125:00 - 8155:00

the hood but it's accelerating the

## 8155:00 - 8205:00

company in being more efficient or

## 8205:00 - 8230:00

better able to scale up or better able

## 8230:00 - 8255:00

to understand it. So I think the answer

## 8255:00 - 8285:00

to your question is it's support it's a

## 8285:00 - 8310:00

supporting role on the sort of building

## 8310:00 - 8340:00

side but it's playing a much more

## 8340:00 - 8370:00

fundamental role in terms of the actual

## 8370:00 - 8405:00

operational side. So let me see if I can

## 8405:00 - 8435:00

zero into it. So instead of basically

## 8435:00 - 8485:00

being autocomplete for coding this is

## 8485:00 - 8515:00

actually going out and being proactive

## 8515:00 - 8545:00

examining things and then coming back

## 8545:00 - 8585:00

with insights. Exactly. And we have

## 8585:00 - 8625:00

similar sort of um you know agents is

## 8625:00 - 8650:00

the I guess the industry term of art

## 8650:00 - 8690:00

now. But um I feel like agents can mean

## 8690:00 - 8710:00

so many things to different people right

## 8710:00 - 8720:00

now.

## 8720:00 - 8745:00

>> What does agents mean to you if you're

## 8745:00 - 8765:00

going to if we're going to start talking

## 8765:00 - 8795:00

about agents? I I need a definition of

## 8795:00 - 8820:00

this word because I'm struggling to

## 8820:00 - 8835:00

figure it out.

## 8835:00 - 8870:00

>> I think the purest definition and this

## 8870:00 - 8890:00

is not so pure because I'm probably

## 8890:00 - 8920:00

going to use like 20 words to do it. So

## 8920:00 - 8950:00

maybe we can edit it down together. But

## 8950:00 - 8980:00

it's going

## 8980:00 - 9060:00

>> Yeah. AI systems um that can um plan um

## 9060:00 - 9105:00

and and and sort of run actions over

## 9105:00 - 9140:00

long time horizons using a variety of

## 9140:00 - 9180:00

tools where the kind of steps are not

## 9180:00 - 9225:00

predetermined. They're able to um solve

## 9225:00 - 9275:00

problems dynamically based on um what

## 9275:00 - 9305:00

information emerges on it. So there's,

## 9305:00 - 9335:00

you know, I I I I end up having this

## 9335:00 - 9410:00

sort of um agent um uh kind of scorecard

## 9410:00 - 9435:00

that I've been using internally as we

## 9435:00 - 9455:00

think about our own products. And

## 9455:00 - 9475:00

there's a bunch of characteristics that

## 9475:00 - 9505:00

I look at. This is way more than 20

## 9505:00 - 9545:00

words, Alex. So, uh, as attributes I

## 9545:00 - 9570:00

look at are things like autonomy. So,

## 9570:00 - 9600:00

how long can the can the agent run

## 9600:00 - 9630:00

unconstrained? So, Sonic 4.5 is a big

## 9630:00 - 9665:00

leap there. Proactivity, like is the

## 9665:00 - 9700:00

agent able to not just react to

## 9700:00 - 9735:00

questions, but actually start to sort of

## 9735:00 - 9785:00

suggest either ideas or or or interject.

## 9785:00 - 9830:00

Um, ability to use tools. Um, and often

## 9830:00 - 9850:00

a variety of tools. Some of them might

## 9850:00 - 9885:00

be research tools. Some of them might be

## 9885:00 - 9905:00

uh, you know, being able to write to a

## 9905:00 - 9955:00

database. Um, memory. So can the agent

## 9955:00 - 9990:00

sort of learn over time and and improve

## 9990:00 - 10040:00

its ability to uh to perform a task? I

## 10040:00 - 10065:00

always say like the hundth task with an

## 10065:00 - 10085:00

agent should be much better than the

## 10085:00 - 10110:00

first because that should be the case

## 10110:00 - 10160:00

for uh human employees as well. Um and

## 10160:00 - 10185:00

then communication is it showing up in

## 10185:00 - 10210:00

all the right places, right? And so for

## 10210:00 - 10250:00

us we think you know these these

## 10250:00 - 10275:00

entities these agents are going to start

## 10275:00 - 10305:00

showing up in all places where you do

## 10305:00 - 10360:00

work whether that's your um uh your

## 10360:00 - 10395:00

Slack or your teams. For example, we

## 10395:00 - 10425:00

launched a research preview of cloud in

## 10425:00 - 10460:00

Chrome. Like we think of cloud, you need

## 10460:00 - 10485:00

to be in all of these places where

## 10485:00 - 10505:00

you're doing work so that you can

## 10505:00 - 10535:00

actually bring it to work rather than

## 10535:00 - 10570:00

having to bring work to it. So I even

## 10570:00 - 10600:00

have this like spider, you know, spider

## 10600:00 - 10620:00

chart of like attributes. So for any

## 10620:00 - 10635:00

given agent that we're building

## 10635:00 - 10670:00

internally, we sort of like grade it on

## 10670:00 - 10690:00

all these different attributes and we

## 10690:00 - 10715:00

can say, "All right, great. For our the

## 10715:00 - 10740:00

next quarter, our investment is going to

## 10740:00 - 10770:00

be on autonomy or it's going to be on

## 10770:00 - 10790:00

memory." And we can kind of kind of pick

## 10790:00 - 10820:00

our pick our attributes that we're

## 10820:00 - 10830:00

working on.

## 10830:00 - 10860:00

>> No, that that was a good definition of

## 10860:00 - 10885:00

agents actually. I think that's the most

## 10885:00 - 10920:00

complete definition I've heard. So

## 10920:00 - 10940:00

here's like an overriding question

## 10940:00 - 10990:00

that's coming up as we talk. Is the

## 10990:00 - 11015:00

improvement that much most of the

## 11015:00 - 11035:00

improvement that we're going to see at

## 11035:00 - 11080:00

least in the near term in AI is it just

## 11080:00 - 11115:00

going to be coming on the like or back

## 11115:00 - 11150:00

of the orchestration of these models

## 11150:00 - 11180:00

getting them to be able to take multiple

## 11180:00 - 11220:00

steps as opposed to I think what was

## 11220:00 - 11260:00

sort of the defining characteristic of

## 11260:00 - 11305:00

the earlier days of LM LMS which was

## 11305:00 - 11335:00

basically just make it bigger make it

## 11335:00 - 11370:00

generally smarter maybe get some PhDs to

## 11370:00 - 11405:00

feed some information to it in post

## 11405:00 - 11440:00

training and then you'll just you know

## 11440:00 - 11470:00

see what happens as you

## 11470:00 - 11520:00

I think that there's going to be some uh

## 11520:00 - 11565:00

fields or disciplines where that sort of

## 11565:00 - 11610:00

um extremely

## 11610:00 - 11660:00

sort of precise depth in a particular

## 11660:00 - 11695:00

task or domain will continue to be

## 11695:00 - 11750:00

important. Um but I think I'm much more

## 11750:00 - 11790:00

excited and just like overall I think

## 11790:00 - 11810:00

we're spending a lot more of our time

## 11810:00 - 11845:00

even from the product side around that.

## 11845:00 - 11875:00

I think it's actually two pieces. one is

## 11875:00 - 11925:00

that orchestration. Um, and then two is

## 11925:00 - 11975:00

how do you take the work that Claude is

## 11975:00 - 12025:00

doing from like pretty good to great.

## 12025:00 - 12070:00

Um, and so, you know, we launched uh

## 12070:00 - 12095:00

ability for Claude to create Word and

## 12095:00 - 12120:00

PowerPoint and Excel files that you can

## 12120:00 - 12145:00

then download and and bring into those

## 12145:00 - 12210:00

apps. Um, and if you get to like 50% as

## 12210:00 - 12240:00

good as you would have done yourself, I

## 12240:00 - 12265:00

don't think that's good enough and it

## 12265:00 - 12290:00

won't speed you up. And in fact, it's

## 12290:00 - 12310:00

like I don't know, I could have just

## 12310:00 - 12340:00

done this myself and now now then at

## 12340:00 - 12365:00

least I would have known what it's done.

## 12365:00 - 12385:00

When you start clearing this sort of

## 12385:00 - 12430:00

like 75 to 80% threshold, of course, is

## 12430:00 - 12460:00

not scientific, but it's kind of like a

## 12460:00 - 12500:00

little bit of a vibes based uh thing. Um

## 12500:00 - 12525:00

then it starts actually being able to

## 12525:00 - 12555:00

really accelerate work. And so that's

## 12555:00 - 12585:00

the other emphasis too. It's and that's

## 12585:00 - 12605:00

interesting that that some of that is

## 12605:00 - 12630:00

post-trading. Some of that's actually

## 12630:00 - 12670:00

also giving um a lot of really good

## 12670:00 - 12700:00

examples to Claude and really working

## 12700:00 - 12785:00

closely to with how the um model uh is

## 12785:00 - 12815:00

producing outputs that are what we think

## 12815:00 - 12845:00

of as like professional quality.

## 12845:00 - 12865:00

>> Right. And I look I know we're 15

## 12865:00 - 12885:00

minutes in, so I think we should

## 12885:00 - 12905:00

probably take a minute to talk about the

## 12905:00 - 12950:00

concrete things that you've improved uh

## 12950:00 - 13000:00

in Claude between 4 and 4.5. Do you want

## 13000:00 - 13040:00

to just give us briefly uh a little bit

## 13040:00 - 13085:00

of a list of the things that get better

## 13085:00 - 13120:00

with the new model? Yeah, I think the

## 13120:00 - 13160:00

the ones that I think are are highlights

## 13160:00 - 13200:00

um maybe I'll I'll I'll buck it into

## 13200:00 - 13255:00

three. One is from a price performance

## 13255:00 - 13325:00

uh perspective. So 4.5 s 4.5 basically

## 13325:00 - 13365:00

outdoes Opus, our largest model in

## 13365:00 - 13415:00

effectively every category but does so

## 13415:00 - 13445:00

while running faster and at a fifth the

## 13445:00 - 13470:00

cost. So if you think about where we

## 13470:00 - 13510:00

were in May at you know code with

## 13510:00 - 13535:00

Claude, we were announcing announcing

## 13535:00 - 13570:00

Opus 4. you now have a model that is

## 13570:00 - 13600:00

better than that and even its successor

## 13600:00 - 13640:00

Opus 4.1 but does so at a flip the cost

## 13640:00 - 13675:00

which is very like you know opens up a

## 13675:00 - 13710:00

whole new set of of use cases for that

## 13710:00 - 13730:00

kind of intelligence that's that's one

## 13730:00 - 13770:00

on the price performance piece. Um the

## 13770:00 - 13810:00

second one is um on its ability not just

## 13810:00 - 13850:00

to to code for for longer but just

## 13850:00 - 13880:00

execute agentically for longer. We

## 13880:00 - 13910:00

talked a little bit about agents, but um

## 13910:00 - 13950:00

what we saw was um actually I put a fun

## 13950:00 - 13985:00

video of this uh on my ex account, which

## 13985:00 - 14025:00

is we asked every claude from Claude 1

## 14025:00 - 14080:00

to Claude, you know, 4.5 to recreate

## 14080:00 - 14110:00

claw.ai, so like our flagship AI

## 14110:00 - 14175:00

product. And um 4.5 was really the first

## 14175:00 - 14210:00

one that was able to do it and to and it

## 14210:00 - 14245:00

actually produced something of, you

## 14245:00 - 14270:00

know, quality. It actually works. You

## 14270:00 - 14300:00

can log in, you can use an API key, all

## 14300:00 - 14345:00

of those things as well. Um, and so that

## 14345:00 - 14380:00

ability to like execute agentically,

## 14380:00 - 14410:00

work for long time horizons. We had one

## 14410:00 - 14440:00

customer had it work for 30 hours. Of

## 14440:00 - 14455:00

course, that's not going to be every

## 14455:00 - 14480:00

task, but like that's the kind of upper

## 14480:00 - 14515:00

bound that we're starting to see um is

## 14515:00 - 14540:00

another big improvement. And then the

## 14540:00 - 14590:00

third one is moving some of those um

## 14590:00 - 14620:00

post- training wins beyond just code to

## 14620:00 - 14645:00

other domains we think are really

## 14645:00 - 14700:00

important. So, for example, um financial

## 14700:00 - 14730:00

um analysis is an area that we've been

## 14730:00 - 14750:00

really interested in. And we launched

## 14750:00 - 14775:00

cloud for financial services a couple of

## 14775:00 - 14810:00

months ago. Um and we incorporated that

## 14810:00 - 14845:00

into the model training in Son 4.5 as

## 14845:00 - 14870:00

well. So when you look at things like

## 14870:00 - 14905:00

benchmarks like finance agent um

## 14905:00 - 14935:00

different domains like the legal domain

## 14935:00 - 14970:00

as well the model is improving not just

## 14970:00 - 15000:00

on code which is obviously important but

## 15000:00 - 15035:00

also these other domains that are um you

## 15035:00 - 15060:00

might actually use code to solve these

## 15060:00 - 15095:00

challenges but uh the point is not to

## 15095:00 - 15115:00

write code the point is to solve a

## 15115:00 - 15145:00

financial analysis for example.

## 15145:00 - 15170:00

>> Okay. And I definitely want to get into

## 15170:00 - 15205:00

these various agents in a moment but let

## 15205:00 - 15240:00

me ask you this. Uh you mentioned that

## 15240:00 - 15300:00

the new Sonnet 4.5 model uh is more

## 15300:00 - 15340:00

performant than Opus the big model in

## 15340:00 - 15390:00

the last release or the four release and

## 15390:00 - 15430:00

uh and it's cheaper. So how how do you

## 15430:00 - 15480:00

do that? I think it's I mean we talked a

## 15480:00 - 15505:00

little bit about scale that's one piece

## 15505:00 - 15545:00

which is you know that just really being

## 15545:00 - 15595:00

training Sonnet 45 um on like

## 15595:00 - 15640:00

significant scale. Um another one is

## 15640:00 - 15670:00

improvements in the post-training work

## 15670:00 - 15715:00

that we've done um as well. On the third

## 15715:00 - 15765:00

third one is um uh really sort of

## 15765:00 - 15795:00

closing the loop on what we hear from

## 15795:00 - 15820:00

customers around what are the things

## 15820:00 - 15850:00

that they wished either Opus or Sonnet

## 15850:00 - 15880:00

were better at and then getting that

## 15880:00 - 15925:00

right. So um one we hear all the time is

## 15925:00 - 15955:00

instruction following like if I tell

## 15955:00 - 15980:00

Sonnet to do this thing I need it to do

## 15980:00 - 16015:00

the thing very reliably even if it's AI

## 16015:00 - 16040:00

even if it tries to be creative like

## 16040:00 - 16065:00

there's times where you really want it

## 16065:00 - 16100:00

to uh to be more prescriptive and we put

## 16100:00 - 16125:00

a bunch of work into instruction

## 16125:00 - 16160:00

following for for this sonnet too.

## 16160:00 - 16190:00

>> So I want to talk about these agents.

## 16190:00 - 16220:00

So, I've got a list of four different

## 16220:00 - 16255:00

types uh that you highlighted upon

## 16255:00 - 16290:00

release. Finance, personal assistant

## 16290:00 - 16325:00

agents, customer support, and deep

## 16325:00 - 16380:00

research. And I just want to talk about

## 16380:00 - 16415:00

who they're for. So, the finance agents

## 16415:00 - 16445:00

are interesting. So, it says you say you

## 16445:00 - 16470:00

could build agents that can understand

## 16470:00 - 16500:00

your portfolio and goals as well as help

## 16500:00 - 16550:00

you evaluate investments by accessing

## 16550:00 - 16590:00

external APIs. personal assistant

## 16590:00 - 16615:00

agents. Build agents that can help you

## 16615:00 - 16650:00

book travel and manage your calendar as

## 16650:00 - 16675:00

well as schedule appointments, put

## 16675:00 - 16710:00

together briefs, and more by connecting

## 16710:00 - 16745:00

your internal data sources and tracking

## 16745:00 - 16795:00

context across applications. I think to

## 16795:00 - 16825:00

set these up, it looks like it's a

## 16825:00 - 16855:00

decent amount of work. Like you'd have

## 16855:00 - 16885:00

to, for instance, with the finance agent

## 16885:00 - 16915:00

understand what an API is. So, it's not

## 16915:00 - 16955:00

going to be something that I think most

## 16955:00 - 17005:00

people would take off the shelf. So, who

## 17005:00 - 17050:00

is this set of agents for? And do you

## 17050:00 - 17090:00

have plans to make this technology more

## 17090:00 - 17125:00

accessible? So let's say, you know, I'm

## 17125:00 - 17155:00

a finance, not even a finance

## 17155:00 - 17180:00

professional. Let's just say I'm someone

## 17180:00 - 17220:00

that wants to have AI run through my

## 17220:00 - 17270:00

portfolio. Can I eventually be able to

## 17270:00 - 17310:00

easily set that up and run it without

## 17310:00 - 17340:00

having to know any of this fancy tech

## 17340:00 - 17355:00

stuff?

## 17355:00 - 17385:00

>> Yeah, I mean that that is absolutely the

## 17385:00 - 17415:00

goal. So there's agents that we'll build

## 17415:00 - 17445:00

ourselves and kind of deploy end to end.

## 17445:00 - 17465:00

And I'll talk a little bit on the

## 17465:00 - 17500:00

personal assistance side next, but I

## 17500:00 - 17540:00

think by and large these will be agents

## 17540:00 - 17580:00

that we can help power for, you know,

## 17580:00 - 17610:00

companies that have, you know, that

## 17610:00 - 17640:00

particular domain expertise that they're

## 17640:00 - 17660:00

bringing it to bear. One of the first

## 17660:00 - 17685:00

companies I ever worked with at

## 17685:00 - 17720:00

Anthropic, uh, was intuitit. We were

## 17720:00 - 17750:00

powering their sort of tax advisory

## 17750:00 - 17775:00

service. And, you know, Enthropic, we're

## 17775:00 - 17810:00

never going to build a tax product. Um,

## 17810:00 - 17845:00

but in it has the largest one. And so,

## 17845:00 - 17875:00

being able to power their sort of tax

## 17875:00 - 17910:00

Q&A was really powerful. Now, you can

## 17910:00 - 17930:00

imagine all these other places, too.

## 17930:00 - 17965:00

We've um been working more closely with

## 17965:00 - 18000:00

Microsoft even for some agents even

## 18000:00 - 18045:00

within um their office suite. So being

## 18045:00 - 18075:00

able to take the financial analysis

## 18075:00 - 18100:00

capability and the financial planning

## 18100:00 - 18145:00

capability and bring it closer to um an

## 18145:00 - 18170:00

Excel user for example, I think that's

## 18170:00 - 18210:00

the way you unlock the maximal value um

## 18210:00 - 18245:00

of some of these as well. And I think

## 18245:00 - 18285:00

you'll see us sort of demonstrate these

## 18285:00 - 18320:00

capabilities, but in terms of the first

## 18320:00 - 18350:00

party products we build, we're pretty

## 18350:00 - 18375:00

thoughtful about which ones we end up

## 18375:00 - 18425:00

going deep on cuz to your point, um it's

## 18425:00 - 18450:00

to reach the scale that we I think

## 18450:00 - 18485:00

these, you know, products deserve to

## 18485:00 - 18520:00

reach. Um you want somebody who's really

## 18520:00 - 18540:00

thinking through the whole endto-end

## 18540:00 - 18565:00

user experience and probably has some of

## 18565:00 - 18595:00

the pre-existing connectors already kind

## 18595:00 - 18630:00

of set up as well. But I think it's

## 18630:00 - 18650:00

important also to build some of these

## 18650:00 - 18685:00

ourselves. So um you talked about the

## 18685:00 - 18720:00

the personal assistant case. One of the

## 18720:00 - 18745:00

things that we've had a lot of fun with

## 18745:00 - 18780:00

um on our mobile apps is using ondevice

## 18780:00 - 18820:00

capabilities as well. And so um I

## 18820:00 - 18845:00

actually just saw that Apple featured us

## 18845:00 - 18885:00

today as our you know like uh like new

## 18885:00 - 18920:00

features like for for Sonic 4.5 and one

## 18920:00 - 18935:00

of the things that they were fe

## 18935:00 - 18985:00

featuring was um on on iOS and Android

## 18985:00 - 19050:00

now. Um it can uh Claude can sort of

## 19050:00 - 19085:00

read your calendar, read your reminders,

## 19085:00 - 19120:00

like compose text messages without

## 19120:00 - 19145:00

really any setup at all. So that's

## 19145:00 - 19180:00

ideal, right? which is like you got

## 19180:00 - 19200:00

those pre-existing connectors, you're

## 19200:00 - 19230:00

not sort of spending a lot of time uh

## 19230:00 - 19265:00

sort of initializing the the just

## 19265:00 - 19295:00

getting it set up to even get any work

## 19295:00 - 19325:00

done as well. But I guess to be more

## 19325:00 - 19345:00

succinct and answer your question,

## 19345:00 - 19365:00

there's some that we'll build ourselves

## 19365:00 - 19390:00

and in those we'll try to, you know, do

## 19390:00 - 19420:00

our best to sort of simplify the setup

## 19420:00 - 19450:00

process. But I'm also very excited for

## 19450:00 - 19475:00

embedding these agents in existing

## 19475:00 - 19510:00

products that are out there that then

## 19510:00 - 19545:00

have all that data built in. And so as I

## 19545:00 - 19575:00

read through your blog post, I also

## 19575:00 - 19605:00

started to think a little bit about

## 19605:00 - 19630:00

Dario's prediction about the white

## 19630:00 - 19650:00

collar blood bath. methods like

## 19650:00 - 19690:00

impossible not to um where he says you

## 19690:00 - 19715:00

know within a few years you might see

## 19715:00 - 19785:00

50% of white collar work uh automated by

## 19785:00 - 19840:00

uh these AI bots u looking at it being

## 19840:00 - 19870:00

able to do these finance tasks or

## 19870:00 - 19900:00

customer support tasks or even be a

## 19900:00 - 19945:00

personal assistant um I'm just curious

## 19945:00 - 19970:00

from your perspective as the person

## 19970:00 - 20000:00

running product here is this something

## 20000:00 - 20035:00

that you're like merily running towards

## 20035:00 - 20065:00

trying to automate human work or like

## 20065:00 - 20115:00

how do you think about it in your role

## 20115:00 - 20150:00

>> we have um you know kind of like product

## 20150:00 - 20190:00

principles we try to work kind of

## 20190:00 - 20220:00

towards um and it's actually interesting

## 20220:00 - 20260:00

like I think we had very or different

## 20260:00 - 20290:00

not entirely different but kind of a

## 20290:00 - 20315:00

different set of product principles even

## 20315:00 - 20335:00

at Instagram I think it's important to

## 20335:00 - 20360:00

sort of like figure out what like who

## 20360:00 - 20385:00

you're building for and how and and and

## 20385:00 - 20450:00

and how you go about it and um one of

## 20450:00 - 20490:00

the uh like principles that we operate

## 20490:00 - 20540:00

you know with is if you can build things

## 20540:00 - 20585:00

that are complimentary or augmentative

## 20585:00 - 20640:00

like bias towards those first um And

## 20640:00 - 20670:00

it's not to say that in the long run

## 20670:00 - 20710:00

like overall these products like might

## 20710:00 - 20760:00

not or probably will be doing more um

## 20760:00 - 20790:00

sort of uh automation or even

## 20790:00 - 20845:00

replacement of work but um we think that

## 20845:00 - 20870:00

two things happen if you can build more

## 20870:00 - 20905:00

augmentative products right um so it's

## 20905:00 - 20930:00

like not a finance agent that like takes

## 20930:00 - 20960:00

all the work you know and does it all

## 20960:00 - 20985:00

for you but it becomes more of a back

## 20985:00 - 21015:00

and forth one is I think it helps people

## 21015:00 - 21045:00

develop an intuition of what the AI is

## 21045:00 - 21075:00

good at today and not good at so that

## 21075:00 - 21100:00

kind of helps people position even their

## 21100:00 - 21135:00

own sort of skills um against that. So I

## 21135:00 - 21165:00

think there's the intuition building. Um

## 21165:00 - 21225:00

and then the second part is um it I

## 21225:00 - 21250:00

think extends the timeline by which

## 21250:00 - 21280:00

people are making that adaptation. So I

## 21280:00 - 21305:00

think if you see Daario out there

## 21305:00 - 21360:00

talking about the you know likely labor

## 21360:00 - 21440:00

impacts, it's not to sort of um uh try

## 21440:00 - 21470:00

to accelerate towards those but more

## 21470:00 - 21495:00

around like hey we think this is coming.

## 21495:00 - 21525:00

Let's start this conversation now. And I

## 21525:00 - 21570:00

think in the products that we build um

## 21570:00 - 21620:00

can we sort of show that this is likely

## 21620:00 - 21650:00

to come but still build a bridge between

## 21650:00 - 21675:00

here and there by building more

## 21675:00 - 21705:00

augmentative products. It's definitely a

## 21705:00 - 21760:00

like a an there's art and science here.

## 21760:00 - 21780:00

is I think we debate a lot within the

## 21780:00 - 21815:00

product team as well like had a a great

## 21815:00 - 21840:00

conversation with our head of design

## 21840:00 - 21860:00

where he's like if we had a product

## 21860:00 - 21885:00

where you hit a button and it did all

## 21885:00 - 21905:00

your work for you that day like would

## 21905:00 - 21930:00

that be a good product and would that be

## 21930:00 - 21955:00

like an anthropicy product and we both

## 21955:00 - 21990:00

came to conclusion like no like one of

## 21990:00 - 22025:00

our kind of core brand tenants that

## 22025:00 - 22045:00

we've like come out is like keep

## 22045:00 - 22070:00

thinking and like we want it to be much

## 22070:00 - 22120:00

more of this uh collaborative sort of

## 22120:00 - 22150:00

accelerator of human thought rather than

## 22150:00 - 22200:00

replacement for human thought um and

## 22200:00 - 22225:00

would like to keep that the case for as

## 22225:00 - 22265:00

long as possible.

## 22265:00 - 22290:00

Yeah, I'm still trying to figure out how

## 22290:00 - 22325:00

I feel about this stuff. Uh, but I do

## 22325:00 - 22365:00

think that the conversation around

## 22365:00 - 22420:00

augmentation versus automation uh is

## 22420:00 - 22460:00

still like so elementary and honestly

## 22460:00 - 22505:00

like it's a fairly dumb way uh to look

## 22505:00 - 22535:00

at. I'm not saying what you're saying is

## 22535:00 - 22565:00

I'm just saying this the industry's you

## 22565:00 - 22590:00

know perspective on this like are you

## 22590:00 - 22630:00

automating or augmenting tasks because

## 22630:00 - 22670:00

let me give you an example. If you

## 22670:00 - 22705:00

automate, you know, some if you automate

## 22705:00 - 22740:00

a job within your company, you've

## 22740:00 - 22770:00

automated a job. The question is what

## 22770:00 - 22805:00

happens next? And if you put that person

## 22805:00 - 22845:00

who was doing that job on something

## 22845:00 - 22875:00

leading a new project, for instance, or

## 22875:00 - 22915:00

something higher value, you've now

## 22915:00 - 22945:00

augmented it in a way that the word

## 22945:00 - 22980:00

augment doesn't even come close to

## 22980:00 - 23025:00

describing. So, it's really tough, I

## 23025:00 - 23080:00

think, to to measure this stuff. And uh

## 23080:00 - 23120:00

and I don't know, I just sort of feel

## 23120:00 - 23155:00

conflicted about the way that the

## 23155:00 - 23185:00

conversation has gone so far. What do

## 23185:00 - 23225:00

you think? I think that that there's a

## 23225:00 - 23250:00

lot to what you're saying, which is

## 23250:00 - 23320:00

there's um there's the uh point in time

## 23320:00 - 23350:00

task, right? Like, oh, you know,

## 23350:00 - 23395:00

managing my calendar or, you know, uh

## 23395:00 - 23420:00

doing some research out about something

## 23420:00 - 23445:00

that I'm I'm talking about. And then

## 23445:00 - 23480:00

there's the broader context of what is

## 23480:00 - 23520:00

the sort of role uh that that person

## 23520:00 - 23560:00

even has within the company. And you

## 23560:00 - 23585:00

know a lot of the things that we think

## 23585:00 - 23635:00

about is um people end up I think people

## 23635:00 - 23665:00

end up feeling more like managers of AI

## 23665:00 - 23705:00

than just users of AI. And we think a

## 23705:00 - 23725:00

lot of it about this even with it's

## 23725:00 - 23755:00

happening in engineering right where our

## 23755:00 - 23785:00

best engineers are managing three or

## 23785:00 - 23820:00

four cloud code instances running at

## 23820:00 - 23850:00

once. Um and all of a sudden you've like

## 23850:00 - 23890:00

had to think higher level like right

## 23890:00 - 23915:00

what is the unit of task that I want

## 23915:00 - 23955:00

each of these sort of subcloud codes to

## 23955:00 - 23990:00

be doing. I think the same will be the

## 23990:00 - 24060:00

case for how we interact with AI systems

## 24060:00 - 24100:00

and there's going to be some blend of

## 24100:00 - 24130:00

automation and augmentation there as

## 24130:00 - 24180:00

well. The the way I think about this uh

## 24180:00 - 24205:00

sort of the bullc case for this is

## 24205:00 - 24265:00

twofold. One um can you bring to bear

## 24265:00 - 24310:00

sort of world expert level thinking of a

## 24310:00 - 24335:00

particular discipline into companies

## 24335:00 - 24365:00

that might not have had that before,

## 24365:00 - 24400:00

right? either because that talent isn't

## 24400:00 - 24430:00

present in that local market or because

## 24430:00 - 24450:00

the company's just getting off the

## 24450:00 - 24475:00

ground and they can't afford a like

## 24475:00 - 24520:00

worldclass CPO somewhere, you know, or

## 24520:00 - 24560:00

CTO. Can you like elevate the the kind

## 24560:00 - 24575:00

of baseline there? So, I think that's

## 24575:00 - 24610:00

one piece too. Um, and then the second

## 24610:00 - 24685:00

one is um having companies that will uh

## 24685:00 - 24725:00

I think emerge and be able to scale and

## 24725:00 - 24755:00

maintain that sort of small team

## 24755:00 - 24775:00

cohesion. And I think we did this really

## 24775:00 - 24820:00

well with Instagram um without having to

## 24820:00 - 24860:00

like you know build a huge workforce

## 24860:00 - 24895:00

from day one. And I think the kinds of

## 24895:00 - 24930:00

companies that get built will change but

## 24930:00 - 24955:00

I still think there's like a tremendous

## 24955:00 - 24975:00

amount of economic opportunity

## 24975:00 - 25005:00

throughout. It just might be you know

## 25005:00 - 25045:00

more smaller companies rather than fewer

## 25045:00 - 25080:00

bigger monolithic companies.

## 25080:00 - 25110:00

>> Interesting. I mean coming from a guy

## 25110:00 - 25145:00

where you were at Instagram was what 16

## 25145:00 - 25170:00

people when you sold it for a billion

## 25170:00 - 25205:00

dollars and people said that was crazy.

## 25205:00 - 25230:00

>> Exactly. So,

## 25230:00 - 25250:00

>> I got a question once that was like,

## 25250:00 - 25275:00

"What when do you think the first single

## 25275:00 - 25305:00

person billiond dollar company will

## 25305:00 - 25330:00

emerge?" I was like, "Well, we had 13."

## 25330:00 - 25360:00

It was like, you know, we were getting

## 25360:00 - 25415:00

close. We're 13 at at uh sale and 16 at

## 25415:00 - 25445:00

close. So, basically, it was yeah, just

## 25445:00 - 25470:00

around then. So, yeah, I mean, we got a

## 25470:00 - 25495:00

lot done with a little and I think a lot

## 25495:00 - 25560:00

of that came from focus. Um, and uh, you

## 25560:00 - 25585:00

know, there's probably work that we

## 25585:00 - 25610:00

could have done even more efficiently,

## 25610:00 - 25640:00

>> right? And I mean, I think if you sold

## 25640:00 - 25680:00

waited a couple years to sell, it might

## 25680:00 - 25710:00

have been worth double or triple that.

## 25710:00 - 25740:00

So folks, if you're just uh by the way,

## 25740:00 - 25760:00

if you don't know about Mike's previous

## 25760:00 - 25790:00

work, he's the co-founder of Instagram.

## 25790:00 - 25830:00

So we are going to get to some of the

## 25830:00 - 25870:00

social media elements of of this or the

## 25870:00 - 25915:00

the comparisons uh to social media

## 25915:00 - 25945:00

building in the second half. But uh two

## 25945:00 - 25975:00

more questions for you as we round out

## 25975:00 - 26010:00

our first half. Uh you mentioned memory.

## 26010:00 - 26035:00

I think it's one of the most interesting

## 26035:00 - 26095:00

parts uh of this work that's sort of I

## 26095:00 - 26125:00

think underrated and underappreciated in

## 26125:00 - 26165:00

the common conversation. um can you talk

## 26165:00 - 26195:00

about how building better memory within

## 26195:00 - 26245:00

these bots is um how important that is

## 26245:00 - 26285:00

and how that's actually happening?

## 26285:00 - 26335:00

>> I think the biggest sort of breakthrough

## 26335:00 - 26360:00

or really key piece of what we've done

## 26360:00 - 26430:00

on memory is um rather than treat it as

## 26430:00 - 26475:00

a sort of substitute for how the model

## 26475:00 - 26510:00

might otherwise access information or

## 26510:00 - 26540:00

sort of a system built on top of the

## 26540:00 - 26560:00

model, we actually have trained it

## 26560:00 - 26605:00

deeply into the model. And so u the

## 26605:00 - 26635:00

model knows about the concept of memory

## 26635:00 - 26660:00

which I know sounds kind of funny but

## 26660:00 - 26685:00

you can really see it as you talk to it.

## 26685:00 - 26710:00

And um you can even

## 26710:00 - 26740:00

>> wait you have to what does that mean?

## 26740:00 - 26760:00

You have to talk about what that means

## 26760:00 - 26775:00

model.

## 26775:00 - 26810:00

>> So basically uh in training we give the

## 26810:00 - 26855:00

model uh effectively a series of tools

## 26855:00 - 26905:00

to let it both read from update you know

## 26905:00 - 26940:00

write memory. And what that means is it

## 26940:00 - 26990:00

understands the concept that it like uh

## 26990:00 - 27035:00

is capable of managing its own memory.

## 27035:00 - 27060:00

And then in our platform, we actually

## 27060:00 - 27100:00

now have that as a sort of, you know,

## 27100:00 - 27125:00

basic building block that you can use.

## 27125:00 - 27150:00

And what that means is as you're talking

## 27150:00 - 27185:00

to to Claude with access memory tool,

## 27185:00 - 27205:00

you can say, "Hey, Claude, can you

## 27205:00 - 27225:00

update your your memory about this?" And

## 27225:00 - 27255:00

it's it knows what that means. It'll

## 27255:00 - 27275:00

say, "Great, I'm going to update the

## 27275:00 - 27315:00

memory." Or when it's uh you performing

## 27315:00 - 27345:00

an action, if it thinks there's a good

## 27345:00 - 27375:00

chance that uh it has some memory

## 27375:00 - 27400:00

related to that, you know, action, it

## 27400:00 - 27425:00

will retrieve that memory before doing

## 27425:00 - 27465:00

the action. And previous systems, you

## 27465:00 - 27485:00

would have to either build that yourself

## 27485:00 - 27525:00

on top of it, um, or Claude or any of

## 27525:00 - 27545:00

these systems wouldn't be as good at

## 27545:00 - 27585:00

using it. And so, um, effectively, in

## 27585:00 - 27605:00

the same way that, you know, we might

## 27605:00 - 27635:00

have the thought, hey, I think I think I

## 27635:00 - 27665:00

did this before or like I think this

## 27665:00 - 27685:00

happened before. I'm going to go, you

## 27685:00 - 27705:00

know, either like think about it for a

## 27705:00 - 27745:00

sec or maybe even search my email. Um,

## 27745:00 - 27780:00

how do you we've basically given Claude

## 27780:00 - 27830:00

that same um, uh, that same ability. And

## 27830:00 - 27890:00

that can be um uh sort of memory that's

## 27890:00 - 27940:00

very uh like factbased like who are you

## 27940:00 - 27960:00

interacting with? What should you do?

## 27960:00 - 27995:00

But it can also be more task based like

## 27995:00 - 28030:00

whenever I'm doing X make sure I

## 28030:00 - 28070:00

remember to do Y.

## 28070:00 - 28100:00

That's pretty amazing. And so what what

## 28100:00 - 28140:00

will the memory get get you when you're

## 28140:00 - 28170:00

using this? like better memory will it

## 28170:00 - 28215:00

start to remember uh many more aspects

## 28215:00 - 28240:00

or like the so I'll give you one example

## 28240:00 - 28285:00

and this is so rudimentary but like if I

## 28285:00 - 28330:00

ever use claude to do a podcast

## 28330:00 - 28365:00

description I have a format prompt that

## 28365:00 - 28395:00

I drop in first sentence should be this

## 28395:00 - 28430:00

second sentence should be this and every

## 28430:00 - 28475:00

single time I you know write that prompt

## 28475:00 - 28515:00

uh I I have every time I ask for a

## 28515:00 - 28535:00

description I have to use that exact

## 28535:00 - 28570:00

prompt or else it will do whatever it

## 28570:00 - 28595:00

wants in freelances when are we going to

## 28595:00 - 28620:00

get to the point where these bots are

## 28620:00 - 28650:00

going to be smart enough where when I

## 28650:00 - 28680:00

tell it, remember this is the way that

## 28680:00 - 28715:00

we do things here, it knows. And I'm

## 28715:00 - 28740:00

sure that my problem is something that

## 28740:00 - 28775:00

people have all across the board when

## 28775:00 - 28800:00

they're trying to get these bots to work

## 28800:00 - 28825:00

on the same things for them.

## 28825:00 - 28860:00

>> Yeah. Um, very soon. So, we have a

## 28860:00 - 28885:00

launch coming up in the next like week

## 28885:00 - 28930:00

or so that's going to really like uh

## 28930:00 - 28960:00

there's both memory and then also the

## 28960:00 - 28985:00

idea of, you know, what are the

## 28985:00 - 29025:00

repeatable ways in which you want work

## 29025:00 - 29055:00

to get done. Um, and so we'll have

## 29055:00 - 29075:00

something really exciting there very

## 29075:00 - 29115:00

soon. But from the memory perspective,

## 29115:00 - 29170:00

um, beyond the sort of like very sort of

## 29170:00 - 29215:00

basic fact-based things like I'm Alex, I

## 29215:00 - 29250:00

run a podcast and a and a newsletter and

## 29250:00 - 29285:00

a site and, uh, that's somewhat helpful,

## 29285:00 - 29315:00

but I think not not sufficient. Like

## 29315:00 - 29350:00

getting to the point of, um, hey, have I

## 29350:00 - 29375:00

interacted with this person before? Like

## 29375:00 - 29400:00

what happens last time I chatted with

## 29400:00 - 29425:00

Mike? Can I like search over my memories

## 29425:00 - 29490:00

there? or it can be hey um whenever you

## 29490:00 - 29520:00

generate these summaries like make sure

## 29520:00 - 29565:00

that you always you know cite this piece

## 29565:00 - 29600:00

or lead with a punchier sort of thing

## 29600:00 - 29630:00

and it's able to sort of update and and

## 29630:00 - 29650:00

learn over time the results. So that's

## 29650:00 - 29700:00

the goal is again like um if claud is

## 29700:00 - 29735:00

like a very competent new hire, we

## 29735:00 - 29765:00

wanted to get to the point where as you

## 29765:00 - 29795:00

use it over time either on our platform

## 29795:00 - 29845:00

or using uh our kind of firstparty

## 29845:00 - 29875:00

products, it is improving and it just

## 29875:00 - 29900:00

feels like a companion that you've

## 29900:00 - 29930:00

actually helped train to your

## 29930:00 - 29950:00

preferences.

## 29950:00 - 29985:00

>> Where on the list of priorities is that

## 29985:00 - 30010:00

capability? It sounds like it's probably

## 30010:00 - 30040:00

very high for you. I know that it's high

## 30040:00 - 30065:00

for OpenAI.

## 30065:00 - 30095:00

>> Yeah, I think it's very it's really high

## 30095:00 - 30135:00

for us. I think for us it's both it's

## 30135:00 - 30160:00

high on the first party side but it's

## 30160:00 - 30190:00

also very high on the on the platform

## 30190:00 - 30215:00

piece as well.

## 30215:00 - 30240:00

>> Okay. All right. Let's go to break. I

## 30240:00 - 30285:00

want to ask you afterwards about what

## 30285:00 - 30335:00

the moment building AI uh has in common

## 30335:00 - 30375:00

and differs from uh in building social

## 30375:00 - 30410:00

media which of course we just mentioned

## 30410:00 - 30435:00

uh you were right at the center of. So

## 30435:00 - 30470:00

let's do that right after this. And

## 30470:00 - 30500:00

we're back here on Big Technology

## 30500:00 - 30530:00

Podcast with Mike Kger. He is the head

## 30530:00 - 30560:00

of product at Anthropic and the

## 30560:00 - 30590:00

co-founder of Instagram. All right,

## 30590:00 - 30625:00

let's let's talk about social media and

## 30625:00 - 30660:00

AI. Very interesting. I mean, when we

## 30660:00 - 30700:00

look around the AI industry, we see so

## 30700:00 - 30735:00

many uh folks who've come from places

## 30735:00 - 30795:00

like Facebook and Twitter uh now running

## 30795:00 - 30830:00

large parts of these AI companies. Of

## 30830:00 - 30855:00

course, yourself, co-founder of

## 30855:00 - 30895:00

Instagram, head of product at Anthropic,

## 30895:00 - 30930:00

Kevin Wheel, uh is running former head

## 30930:00 - 30965:00

of in well, head of Instagram product as

## 30965:00 - 31010:00

well, I think, uh is is running product

## 31010:00 - 31055:00

at OpenAI. Fiji Simo who came from

## 31055:00 - 31085:00

Facebook is running consumer

## 31085:00 - 31125:00

applications at OpenAI. I I mean I could

## 31125:00 - 31170:00

go on. Um what does what does building

## 31170:00 - 31190:00

these products have in common with

## 31190:00 - 31215:00

building social media and how does it

## 31215:00 - 31230:00

differ?

## 31230:00 - 31275:00

>> I think there's there's maybe the you

## 31275:00 - 31325:00

know abstracted from the actual product

## 31325:00 - 31355:00

itself like what does it take to build

## 31355:00 - 31405:00

good product? And I think that um I

## 31405:00 - 31430:00

think it's it's less that there's a lot

## 31430:00 - 31480:00

of social media um sort of oriented

## 31480:00 - 31510:00

folks that have now moved into an AI.

## 31510:00 - 31540:00

It's more that I think a lot of the best

## 31540:00 - 31575:00

product people were focused on that you

## 31575:00 - 31615:00

know even four years ago you know pre-

## 31615:00 - 31660:00

chat GPT uh you know pre the emergence

## 31660:00 - 31690:00

of a lot of these LLMs um so I think

## 31690:00 - 31715:00

it's a sort of like the most recent

## 31715:00 - 31740:00

place that concentrate I I find that

## 31740:00 - 31760:00

that often happens like the

## 31760:00 - 31780:00

concentration of talent among a

## 31780:00 - 31810:00

particular uh discipline and I think

## 31810:00 - 31830:00

that was that was social media

## 31830:00 - 31855:00

beforehand so that's partly one of them

## 31855:00 - 31890:00

and and there it's you know um all of

## 31890:00 - 31945:00

the pieces around understanding uh what

## 31945:00 - 31970:00

your data is telling you but also having

## 31970:00 - 32000:00

the intuition around like what bets you

## 32000:00 - 32020:00

want to place in terms of where you want

## 32020:00 - 32055:00

to move into next. How do you assemble a

## 32055:00 - 32075:00

great product team? How does product

## 32075:00 - 32110:00

engineering and design and marketing

## 32110:00 - 32130:00

work well together? All these different,

## 32130:00 - 32155:00

you know, sort of aspects of that. So

## 32155:00 - 32185:00

that there's that one and then I think

## 32185:00 - 32215:00

there's the the the separate question of

## 32215:00 - 32245:00

you know within social media like what

## 32245:00 - 32285:00

are the similarities and differences. Um

## 32285:00 - 32315:00

with claude it feels quite different in

## 32315:00 - 32345:00

that you know we have more of a business

## 32345:00 - 32370:00

audience like plenty of people use it

## 32370:00 - 32400:00

for their individual pieces but it has

## 32400:00 - 32450:00

less of that sort of um you know social

## 32450:00 - 32480:00

component right now. Um, it's definitely

## 32480:00 - 32520:00

more word of mouth. Like the the most

## 32520:00 - 32545:00

social thing that we've experienced is

## 32545:00 - 32585:00

how people got excited about all the the

## 32585:00 - 32610:00

merch and the pop-up we just did in New

## 32610:00 - 32630:00

York where that was like a real like

## 32630:00 - 32655:00

attractor moment where there was like

## 32655:00 - 32690:00

more of that. But in general less of the

## 32690:00 - 32745:00

sort of mechanics of uh of like capital

## 32745:00 - 32790:00

Growth, right? The you know uh how many

## 32790:00 - 32815:00

you know people did you bring in, what

## 32815:00 - 32840:00

who did they invite, all of those

## 32840:00 - 32890:00

different pieces. Um so maybe a little

## 32890:00 - 32910:00

bit different there at least for from

## 32910:00 - 32935:00

the the pieces that we're tackling with

## 32935:00 - 32975:00

Claude. But of course as a lot of these

## 32975:00 - 33020:00

uh or non-cloud tools move into more of

## 33020:00 - 33060:00

this uh generation of like images and

## 33060:00 - 33090:00

videos like there is much more of an

## 33090:00 - 33125:00

over a strong overlap with what folks

## 33125:00 - 33145:00

were were doing on the social media

## 33145:00 - 33160:00

front.

## 33160:00 - 33200:00

>> How important is engagement to you? I

## 33200:00 - 33235:00

mean I think the thing that really drove

## 33235:00 - 33285:00

Facebook decisions was engagement and of

## 33285:00 - 33310:00

course growth and maybe the two go hand

## 33310:00 - 33350:00

in hand. And we always wonder about AI

## 33350:00 - 33370:00

products. Like of course you want people

## 33370:00 - 33400:00

to use them, but you don't want

## 33400:00 - 33430:00

engagement for engagement sake cuz it's

## 33430:00 - 33465:00

pretty expensive to serve these use

## 33465:00 - 33500:00

cases. So where does engagement sit for

## 33500:00 - 33520:00

you in the terms of the metrics that

## 33520:00 - 33560:00

you're optimizing toward? We don't

## 33560:00 - 33590:00

really look at engagement, at least not

## 33590:00 - 33615:00

in the typical like at Instagram, we

## 33615:00 - 33630:00

spend a lot of time looking at things

## 33630:00 - 33675:00

like time spent, right? Um we do look at

## 33675:00 - 33725:00

things like um daily visitors as a proxy

## 33725:00 - 33755:00

for a utility. So I think that's that's

## 33755:00 - 33805:00

one piece that we look at as well. Um,

## 33805:00 - 33845:00

but it's interesting like um I I was

## 33845:00 - 33870:00

talking to our mobile team yesterday

## 33870:00 - 33900:00

like I think in the future people's

## 33900:00 - 33925:00

interactions with something like cloud

## 33925:00 - 33960:00

code might be much more mobile oriented

## 33960:00 - 33985:00

and ideally like we're right by

## 33985:00 - 34020:00

Salesforce Park or office. Like I would

## 34020:00 - 34050:00

love to be able to kick off some coding

## 34050:00 - 34085:00

task, go for a walk in Salesforce Park,

## 34085:00 - 34120:00

maybe with a co-orker. Um maybe it pings

## 34120:00 - 34140:00

me halfway through and has some

## 34140:00 - 34165:00

clarification question and get back to

## 34165:00 - 34205:00

my desk and it's done. Um it's a very

## 34205:00 - 34225:00

different discipline than being hands-

## 34225:00 - 34250:00

on keyboard. I also love that. that

## 34250:00 - 34270:00

feels like a different discipline than

## 34270:00 - 34305:00

what coding has, you know, evolved to to

## 34305:00 - 34345:00

primarily being nowadays. And now it's

## 34345:00 - 34365:00

more about like what are the creative

## 34365:00 - 34385:00

ideas that I have that I want to see

## 34385:00 - 34440:00

manifested. But in that world, I the

## 34440:00 - 34470:00

time spent was quite low, right? It was

## 34470:00 - 34495:00

maybe like kicking off the task and

## 34495:00 - 34530:00

resolving some questions, but the value

## 34530:00 - 34555:00

of what was produced was much higher.

## 34555:00 - 34585:00

And so I think the interaction paradigm

## 34585:00 - 34620:00

is just really really different in terms

## 34620:00 - 34655:00

of what we end up looking at. And so I

## 34655:00 - 34690:00

think much more about the the sort of

## 34690:00 - 34725:00

value of work getting done than the sort

## 34725:00 - 34785:00

of like interaction and and um sort of

## 34785:00 - 34855:00

uh yeah the long uh long sessions u that

## 34855:00 - 34880:00

you might see at social media.

## 34880:00 - 34910:00

>> I legitimately just had a founder that I

## 34910:00 - 34945:00

interviewed tell me that her favorite

## 34945:00 - 34980:00

use case is just using AI to get away

## 34980:00 - 35020:00

from her computer which is something

## 35020:00 - 35065:00

you've never really heard of before in

## 35065:00 - 35120:00

technology. So, um, I got to ask you,

## 35120:00 - 35140:00

what do you think Mark Zuckerberg is

## 35140:00 - 35175:00

trying to do with his very unique AI

## 35175:00 - 35200:00

strategy?

## 35200:00 - 35240:00

>> I I think I there's folks in there that

## 35240:00 - 35270:00

I've known for a long time like like Nat

## 35270:00 - 35350:00

who I really respect. So, I think um

## 35350:00 - 35400:00

what I suspect you'll see is sort of

## 35400:00 - 35450:00

more experimentation around what like AI

## 35450:00 - 35490:00

means for this kind of portfolio of

## 35490:00 - 35545:00

companies. I think the sort of uh

## 35545:00 - 35595:00

initial wave of well you know we've got

## 35595:00 - 35630:00

some chatbot type stuff in the search

## 35630:00 - 35665:00

bars was like not particularly

## 35665:00 - 35690:00

transformative and I think the teams

## 35690:00 - 35745:00

there likely know it and so um yeah I

## 35745:00 - 35775:00

think it'll or maybe what I hope we'll

## 35775:00 - 35800:00

see is more experimentation that can

## 35800:00 - 35835:00

kind of live outside of those uh of

## 35835:00 - 35870:00

those surfaces like in the same way that

## 35870:00 - 35895:00

with Instagram you know there was some

## 35895:00 - 35920:00

ideas we had that didn't really belong

## 35920:00 - 35955:00

in the app like hyperlapse or even

## 35955:00 - 35980:00

nobody remembers Bolt but Bolt was our

## 35980:00 - 36045:00

like very very fast messenger um uh you

## 36045:00 - 36080:00

know I think that experimentation once

## 36080:00 - 36110:00

you get a service as widespread as

## 36110:00 - 36140:00

Instagram or as widespread as Facebook

## 36140:00 - 36180:00

or WhatsApp it's hard to introduce a new

## 36180:00 - 36215:00

behavior there um you know we did it

## 36215:00 - 36240:00

with stories I think they've since done

## 36240:00 - 36275:00

it with reals uh but it's almost like

## 36275:00 - 36310:00

one you get one per generation and I

## 36310:00 - 36325:00

think you want to have more of an

## 36325:00 - 36365:00

experimentation kind of test bed beyond

## 36365:00 - 36405:00

that and I suspect just like given what

## 36405:00 - 36430:00

I know about how those folks think that

## 36430:00 - 36450:00

there'll be more of that sort of

## 36450:00 - 36480:00

experimentation

## 36480:00 - 36510:00

>> interesting So, as as the co-founder of

## 36510:00 - 36545:00

Instagram, I'm sure you've watched with

## 36545:00 - 36580:00

interest as AI generated images and

## 36580:00 - 36625:00

videos have filled social media feeds

## 36625:00 - 36665:00

and even propelled like was Sora the

## 36665:00 - 36705:00

Sora app to the number one spot on the

## 36705:00 - 36760:00

app store. Uh, do you think AI generated

## 36760:00 - 36800:00

content and video maybe in this Cameo

## 36800:00 - 36825:00

version where you can put yourself in

## 36825:00 - 36880:00

the videos, do you think it it threatens

## 36880:00 - 36925:00

or makes a run for replacing the human

## 36925:00 - 36970:00

generated content that we have today or

## 36970:00 - 37000:00

uh do you think that the human stuff is

## 37000:00 - 37035:00

going to stay on top and this is a flash

## 37035:00 - 37050:00

in the pan?

## 37050:00 - 37095:00

>> Yeah, I mean I think there's

## 37095:00 - 37120:00

here's what I'm not sure of yet. We saw

## 37120:00 - 37150:00

this with Instagram that there were

## 37150:00 - 37180:00

creative tools that would emerge and of

## 37180:00 - 37230:00

course these were at a much more um sort

## 37230:00 - 37270:00

of uh basic level than the kind of

## 37270:00 - 37295:00

capabilities that you're seeing with um

## 37295:00 - 37330:00

with VO and with Sora and with even some

## 37330:00 - 37365:00

of these these other models. Uh but you

## 37365:00 - 37390:00

would see an emergence of a creative

## 37390:00 - 37425:00

tool and whether they were able to sort

## 37425:00 - 37450:00

of transcend that to being a network

## 37450:00 - 37505:00

that you come back to was often not the

## 37505:00 - 37535:00

case. Um and I think that was for a

## 37535:00 - 37580:00

couple of reasons. one is um at least in

## 37580:00 - 37630:00

that generation of products like the

## 37630:00 - 37670:00

creative content or the created content

## 37670:00 - 37695:00

started getting a little bit sy over

## 37695:00 - 37715:00

time right especially if it was like a

## 37715:00 - 37750:00

very highly stylized tool um and the

## 37750:00 - 37785:00

second one it's like the dynamics that

## 37785:00 - 37810:00

make Instagram Instagram like the people

## 37810:00 - 37835:00

you already know on there the people

## 37835:00 - 37860:00

that you follow the creators that you

## 37860:00 - 37885:00

know and of course this has shifted now

## 37885:00 - 37915:00

and more of like a uh like pure

## 37915:00 - 37950:00

algorithmic realsoriented piece or maybe

## 37950:00 - 37985:00

I'm talking more about like the the the

## 37985:00 - 38015:00

previous Instagram that was still had a

## 38015:00 - 38065:00

heavy kind of follow component um ends

## 38065:00 - 38090:00

up being a thing that feels like, oh, I

## 38090:00 - 38130:00

know what I'm I know who I'm interacting

## 38130:00 - 38155:00

with here. And of course, Tik Tok has a

## 38155:00 - 38185:00

very different take on things. So, to

## 38185:00 - 38235:00

the extent that it's replacing um I

## 38235:00 - 38255:00

think the the things that would have to

## 38255:00 - 38290:00

be true is one that there's the the

## 38290:00 - 38325:00

content feels varied over time and not

## 38325:00 - 38350:00

just sort of like, yeah, okay, I've kind

## 38350:00 - 38370:00

of seen this this before. It's really

## 38370:00 - 38405:00

interesting, but I've seen it before. Um

## 38405:00 - 38465:00

and then two, is there value to being uh

## 38465:00 - 38505:00

in that network over time? And do you

## 38505:00 - 38555:00

find yourself um uh opening it because

## 38555:00 - 38585:00

there's like not just content that

## 38585:00 - 38605:00

you're interested in, but maybe people

## 38605:00 - 38655:00

that you care about um or there's um uh

## 38655:00 - 38685:00

sort of communities that form within it.

## 38685:00 - 38700:00

Cuz I think that's actually what

## 38700:00 - 38725:00

Instagram got right is that you started

## 38725:00 - 38760:00

seeing these emergent communities that

## 38760:00 - 38785:00

maybe were just around taking

## 38785:00 - 38805:00

photography, maybe they were oriented

## 38805:00 - 38845:00

around living in a particular city. Um

## 38845:00 - 38870:00

and they were very self-organizing. The

## 38870:00 - 38905:00

only tool we gave people was hashtags.

## 38905:00 - 38945:00

Um and that was enough to sort of spur

## 38945:00 - 38965:00

the these communities. So, I think

## 38965:00 - 39000:00

that's like the fundamental uh question

## 39000:00 - 39030:00

to be to be answered still.

## 39030:00 - 39050:00

>> Yeah, it's a great point and I think the

## 39050:00 - 39080:00

cameo aspect where you can put yourself

## 39080:00 - 39140:00

in the video may go some degree towards

## 39140:00 - 39170:00

making that happen in these apps. But I

## 39170:00 - 39215:00

also I'll tell you on Friday uh I

## 39215:00 - 39265:00

couldn't put Sora down and we're at

## 39265:00 - 39305:00

Wednesday and uh I don't I don't really

## 39305:00 - 39335:00

feel compelled to open it right now. I

## 39335:00 - 39380:00

think you're right that maybe all the AI

## 39380:00 - 39410:00

content creation can have that level of

## 39410:00 - 39445:00

sameness to it where you watch one

## 39445:00 - 39470:00

video, you feel like you've watched them

## 39470:00 - 39495:00

all and then maybe people come with

## 39495:00 - 39525:00

creative come up with creative prompts

## 39525:00 - 39570:00

and you know you see a new trend. But um

## 39570:00 - 39605:00

I think that's a spot-on uh point there

## 39605:00 - 39665:00

that that's the challenge.

## 39665:00 - 39705:00

>> Yeah. Well, uh, well, I mean, I think it

## 39705:00 - 39750:00

it's it's all happening very quickly in

## 39750:00 - 39785:00

terms of the the experimentation and so

## 39785:00 - 39830:00

I think there's also this like um

## 39830:00 - 39875:00

ability for these tools to adapt as well

## 39875:00 - 39965:00

and um whether it'll sort of uh open the

## 39965:00 - 40010:00

door to sort of a new Cambrian explosion

## 40010:00 - 40035:00

of social products is going to be

## 40035:00 - 40055:00

another thing that I'm tracking really

## 40055:00 - 40080:00

well. It feels like it's been very quiet

## 40080:00 - 40105:00

on the social front for the last couple

## 40105:00 - 40125:00

of years. because you know we've sort of

## 40125:00 - 40160:00

like stabilized among you know a couple

## 40160:00 - 40195:00

of really big players not a lot of new

## 40195:00 - 40265:00

experimentation and um yeah I I miss the

## 40265:00 - 40305:00

you know 2010s of you know what if what

## 40305:00 - 40330:00

if social products were like this and

## 40330:00 - 40355:00

what if we took this differentiated take

## 40355:00 - 40380:00

on things and not all most of them

## 40380:00 - 40405:00

aren't going to work but at least like

## 40405:00 - 40430:00

there is that value of like hell yeah I

## 40430:00 - 40455:00

want to try that like that that is a

## 40455:00 - 40480:00

different experience like you know even

## 40480:00 - 40520:00

if it's uh again things that feel like

## 40520:00 - 40555:00

maybe novelties like oh it's a photo app

## 40555:00 - 40585:00

that takes the front and the back camera

## 40585:00 - 40615:00

together like is that lasting network.

## 40615:00 - 40640:00

No, but it painted the way towards

## 40640:00 - 40655:00

something.

## 40655:00 - 40685:00

>> Yeah, that was fun. And I I missed that,

## 40685:00 - 40705:00

too. By the way, that happened, I think,

## 40705:00 - 40740:00

in the 2020s, but I definitely missed

## 40740:00 - 40780:00

the 2010s when I was uh you know, doing

## 40780:00 - 40810:00

social media reporting at BuzzFeed and

## 40810:00 - 40835:00

there would be a new app every every

## 40835:00 - 40855:00

week and it was like, "All right, well,

## 40855:00 - 40885:00

what's Peach? Let's try this out." And

## 40885:00 - 40910:00

then be gone, but there would be

## 40910:00 - 40920:00

something new.

## 40920:00 - 40935:00

>> Oh my god.

## 40935:00 - 40975:00

>> Peach was classic. All time classic.

## 40975:00 - 41005:00

>> It was.

## 41005:00 - 41035:00

>> So, I want to talk to you about about

## 41035:00 - 41085:00

community briefly. Um, where do you look

## 41085:00 - 41140:00

to find, I guess, a community of of

## 41140:00 - 41180:00

users and get your feedback? Um, and how

## 41180:00 - 41215:00

important is Reddit to you? Because I've

## 41215:00 - 41255:00

seen so much of the activity in the AI

## 41255:00 - 41290:00

space move on to Reddit and I'm curious,

## 41290:00 - 41340:00

are are you reading like our/Sarity or

## 41340:00 - 41370:00

how deep into it are you?

## 41370:00 - 41405:00

>> Um, that's a great question. So, it's

## 41405:00 - 41435:00

interesting being um I would say that

## 41435:00 - 41460:00

there's like sort of somewhat

## 41460:00 - 41485:00

overlapping but distinct communities

## 41485:00 - 41525:00

that we look at. one is like being a

## 41525:00 - 41565:00

platform, we have um like a strong kind

## 41565:00 - 41600:00

of customer base that often has a very

## 41600:00 - 41635:00

sort of cleareyed perspective about

## 41635:00 - 41655:00

where the models could continue to

## 41655:00 - 41675:00

improve or what we could be doing better

## 41675:00 - 41720:00

as a platform. And so um this is very

## 41720:00 - 41740:00

different than my time at Instagram

## 41740:00 - 41765:00

where, you know, there were people that

## 41765:00 - 41785:00

we talked to a bunch about how they

## 41785:00 - 41810:00

they're using Instagram, but we didn't

## 41810:00 - 41845:00

have this like more permanent notion of

## 41845:00 - 41870:00

like an advisory board that we have here

## 41870:00 - 41910:00

at Anthropic. And we just brought in uh

## 41910:00 - 41935:00

a couple months ago Paul Smith as our

## 41935:00 - 41955:00

new chief commercial officer and he's

## 41955:00 - 41985:00

brought also this sort of community of

## 41985:00 - 42020:00

more enterprise folks as well that we've

## 42020:00 - 42055:00

been talking to. So that's one kind of

## 42055:00 - 42110:00

big delta which is uh like more stable

## 42110:00 - 42140:00

uh sort of set of people that community

## 42140:00 - 42170:00

that we're we're talking to. So that's

## 42170:00 - 42210:00

one. Um we actually have a phenomenal

## 42210:00 - 42245:00

user experience research team and that's

## 42245:00 - 42270:00

a place where we end up being able to

## 42270:00 - 42310:00

stay connected to how um more of the

## 42310:00 - 42335:00

power users that I think of as like our

## 42335:00 - 42355:00

core demographic for something like

## 42355:00 - 42400:00

cloud.ai AI uh are using the product and

## 42400:00 - 42420:00

I love it. Like every month we do a

## 42420:00 - 42450:00

product all hands and then my favorite

## 42450:00 - 42485:00

chunk of that product all hands is

## 42485:00 - 42525:00

basically the UXR team doing like a

## 42525:00 - 42550:00

voice of the user piece and it's

## 42550:00 - 42585:00

surprising sometimes because you know

## 42585:00 - 42615:00

it's not necessarily who you might

## 42615:00 - 42645:00

expect being like the software engineer

## 42645:00 - 42675:00

archetype who for sure are using our

## 42675:00 - 42715:00

products but there's also hey I'm you

## 42715:00 - 42750:00

know a marketing manager I need to

## 42750:00 - 42780:00

produce 20 decks a week and now I

## 42780:00 - 42805:00

finally found a tool that I'm like using

## 42805:00 - 42845:00

to to cut it out but here's my uh here's

## 42845:00 - 42870:00

my feeling about it. Here are my fears

## 42870:00 - 42900:00

about AI. Here's the promise of AI. So

## 42900:00 - 42940:00

just a very humanizing uh kind of aspect

## 42940:00 - 42980:00

of it. Um and then for sure you know I

## 42980:00 - 43040:00

think still today I think like Twitterx

## 43040:00 - 43100:00

and Reddit have a like strong pocket of

## 43100:00 - 43150:00

uh of that AI community and we um you

## 43150:00 - 43185:00

know I think we've we've gotten better

## 43185:00 - 43220:00

at um engaging in that community than

## 43220:00 - 43240:00

before. I think there was a time period

## 43240:00 - 43275:00

where we were like well like there's a

## 43275:00 - 43305:00

lot of volume. How do we react? And then

## 43305:00 - 43325:00

like you don't want to be showing up

## 43325:00 - 43345:00

only when there's like something that

## 43345:00 - 43375:00

you want to like correct or something

## 43375:00 - 43410:00

cuz then it feels very like corpo and

## 43410:00 - 43445:00

not like authentic. And so I think we

## 43445:00 - 43470:00

have found a better like ability to

## 43470:00 - 43505:00

participate uh in some of those those

## 43505:00 - 43530:00

communities. And you know it's good.

## 43530:00 - 43555:00

It's they're they're often the like

## 43555:00 - 43585:00

power users extreme users that are

## 43585:00 - 43610:00

telling you something about the edge of

## 43610:00 - 43640:00

what's possible and then you can kind of

## 43640:00 - 43670:00

try to generalize it more more broadly

## 43670:00 - 43705:00

too but less like r/s singularity and

## 43705:00 - 43745:00

maybe more like r/cloudi.

## 43745:00 - 43775:00

It's very mundane, but it's where a lot

## 43775:00 - 43805:00

of folks are are hanging out.

## 43805:00 - 43835:00

>> All right, cool. uh we spoke this whole

## 43835:00 - 43865:00

conversation we haven't brought up the

## 43865:00 - 43905:00

fact that well I haven't and and maybe

## 43905:00 - 43935:00

this oversight on my end that that

## 43935:00 - 43965:00

openai basically has seen how well

## 43965:00 - 44000:00

anthropic has done on coding and said

## 44000:00 - 44030:00

that this is you know a number one

## 44030:00 - 44090:00

priority for the company and uh I mean

## 44090:00 - 44135:00

every day you can look at openai leaders

## 44135:00 - 44180:00

on X speaking of X trumpeting their

## 44180:00 - 44230:00

codeex product and talking about how uh

## 44230:00 - 44260:00

how advanced they are on on coding

## 44260:00 - 44295:00

skills so can you talk about how you

## 44295:00 - 44330:00

assess openai challenge and what it's

## 44330:00 - 44360:00

going to be like uh to sort of go

## 44360:00 - 44390:00

headto-head with them on what has been

## 44390:00 - 44420:00

anthropic bread and butter.

## 44420:00 - 44440:00

>> Yeah, I mean I think it's definitely

## 44440:00 - 44480:00

there was a maybe a window in the summer

## 44480:00 - 44520:00

where it was surprising to me, I guess,

## 44520:00 - 44590:00

in general how um uh sort of alone we

## 44590:00 - 44620:00

were in in sort of both paying attention

## 44620:00 - 44655:00

and having a product out there. It's

## 44655:00 - 44705:00

definitely gotten more um uh sort of

## 44705:00 - 44725:00

interesting and competitive, which I

## 44725:00 - 44745:00

love. I think that that my favorite

## 44745:00 - 44770:00

times at Instagram were also like when

## 44770:00 - 44805:00

we had interesting competitors that we I

## 44805:00 - 44830:00

think it pushes you forward in terms of

## 44830:00 - 44855:00

like what like what is the product we

## 44855:00 - 44875:00

want to build? What are the capabilities

## 44875:00 - 44905:00

that we're we're going to need to have.

## 44905:00 - 44955:00

Um so you know it's it's kind of like a

## 44955:00 - 45000:00

game on an interesting moment as well

## 45000:00 - 45050:00

for us. The coding piece beyond just the

## 45050:00 - 45080:00

fact that coding is a really high value

## 45080:00 - 45125:00

economic activity. I really see the

## 45125:00 - 45165:00

model's ability to plan, write code,

## 45165:00 - 45190:00

solve problems as not just being useful

## 45190:00 - 45210:00

for software engineering, but being

## 45210:00 - 45250:00

really critical path to the kind of like

## 45250:00 - 45275:00

agentic behavior we want to build long

## 45275:00 - 45305:00

term. So there's no way that would never

## 45305:00 - 45350:00

be anything but like one of our, you

## 45350:00 - 45385:00

know, top two or three priorities. And

## 45385:00 - 45415:00

then it's a matter of how do we make

## 45415:00 - 45435:00

sure that we're showing up with the

## 45435:00 - 45460:00

right products that like deeply solve

## 45460:00 - 45490:00

the right problems for people, right?

## 45490:00 - 45515:00

Like maybe this ties all the way back to

## 45515:00 - 45540:00

your question about like good product

## 45540:00 - 45570:00

design and how I think about products.

## 45570:00 - 45620:00

Um, it's one thing to score well on

## 45620:00 - 45645:00

software engineering bench. That's

## 45645:00 - 45675:00

important as like a benchmark, but it's

## 45675:00 - 45705:00

way more important, I think, to get the

## 45705:00 - 45735:00

feedback from people like great, those

## 45735:00 - 45770:00

are really hard tasks that I was doing

## 45770:00 - 45820:00

with Rust and in set 4 I couldn't do it.

## 45820:00 - 45855:00

Open four could barely do it. Sonet 4.5

## 45855:00 - 45880:00

can do it. Like that I get very excited

## 45880:00 - 45900:00

about because it means we're actually

## 45900:00 - 45940:00

having uh like real world impact. So I

## 45940:00 - 45975:00

think you'll see us um if we're doing

## 45975:00 - 46010:00

our jobs right on coding uh you know

## 46010:00 - 46040:00

even in the in the presence of other

## 46040:00 - 46065:00

players enter the space try to stay

## 46065:00 - 46110:00

really focused on um listening to how

## 46110:00 - 46140:00

people are using these products in the

## 46140:00 - 46175:00

wild and then uh ensuring that future

## 46175:00 - 46210:00

model versions are sort of meeting

## 46210:00 - 46240:00

people where they are in that you know

## 46240:00 - 46270:00

high utility space.

## 46270:00 - 46300:00

>> All right last one for you Mike. Uh

## 46300:00 - 46340:00

enterprises they're all interested in

## 46340:00 - 46365:00

generative AI they're not great at

## 46365:00 - 46400:00

implementing it. They'll admit it the

## 46400:00 - 46430:00

studies show it. Are they going to get

## 46430:00 - 46450:00

it together?

## 46450:00 - 46480:00

>> I think they will. I'm actually, you

## 46480:00 - 46520:00

know, we're we're um from from after our

## 46520:00 - 46555:00

our our conversation, I'm I'm having a

## 46555:00 - 46580:00

off-site with our product team and a lot

## 46580:00 - 46620:00

of the focus for next year is continue

## 46620:00 - 46655:00

to to go into the enterprise side of

## 46655:00 - 46670:00

things. And I think there's a few

## 46670:00 - 46705:00

things. There's the um and we could

## 46705:00 - 46730:00

probably do another whole like hour on

## 46730:00 - 46755:00

this. I get very excited about this as

## 46755:00 - 46790:00

well. There's a whole range from how do

## 46790:00 - 46815:00

you take a product like cloud for

## 46815:00 - 46850:00

enterprise that you know enterprises are

## 46850:00 - 46880:00

already adopting, but make it really

## 46880:00 - 46905:00

really useful. And we talked a little

## 46905:00 - 46935:00

bit before about like output quality and

## 46935:00 - 46980:00

just like how um how much it's actually

## 46980:00 - 47025:00

helping you. And like there's I think

## 47025:00 - 47055:00

part of the valley of disillusionment or

## 47055:00 - 47075:00

the trough of disillusionment that you

## 47075:00 - 47100:00

might be seeing around enterprise AI

## 47100:00 - 47145:00

adoption is the promise of these tools

## 47145:00 - 47165:00

around they're going to save you time,

## 47165:00 - 47185:00

they're going to like make like make

## 47185:00 - 47215:00

your work better just wasn't fulfilled

## 47215:00 - 47240:00

by the previous generation of products

## 47240:00 - 47265:00

and they need to be if we're going to

## 47265:00 - 47320:00

actually get like sticky adoption in the

## 47320:00 - 47345:00

enterprise, right? And so that's a lot

## 47345:00 - 47380:00

of what we're pushing on is like it's

## 47380:00 - 47430:00

not like it's not like AI produced

## 47430:00 - 47485:00

document slop. It's AI produced quality

## 47485:00 - 47525:00

stuff that you can then uh iterate on

## 47525:00 - 47555:00

and use and feel proud that you created

## 47555:00 - 47580:00

just like I think people can feel proud

## 47580:00 - 47610:00

about like here I built this thing using

## 47610:00 - 47640:00

using cloud on the coding side and then

## 47640:00 - 47670:00

there's all the way to you know beyond

## 47670:00 - 47700:00

the cloud for enterprise piece like

## 47700:00 - 47725:00

deeper integrations like internal

## 47725:00 - 47750:00

transformation and what we're learning

## 47750:00 - 47775:00

there to your question about how

## 47775:00 - 47800:00

enterprises are are thinking about and

## 47800:00 - 47830:00

adopting is um at least for the

## 47830:00 - 47860:00

foreseeable future we need to lean in

## 47860:00 - 47900:00

much more in terms of uh helping

## 47900:00 - 47930:00

enterprises get there and so we're doing

## 47930:00 - 47980:00

much more of model now where either uh

## 47980:00 - 48005:00

with our own engineers embedded in

## 48005:00 - 48040:00

enterprises in partnership with Deote

## 48040:00 - 48070:00

which we just announced this week can we

## 48070:00 - 48105:00

actually like take our technology meet

## 48105:00 - 48135:00

companies where they like what their

## 48135:00 - 48155:00

highest needs are and then just

## 48155:00 - 48185:00

co-develop and just you know lock

## 48185:00 - 48210:00

ourselves in the building until we've

## 48210:00 - 48235:00

solved their problem and then like learn

## 48235:00 - 48260:00

from that experience and move on to the

## 48260:00 - 48295:00

next enterprise. But I think uh it's

## 48295:00 - 48320:00

very different than sort of the lean

## 48320:00 - 48340:00

back sort of like we're just going to

## 48340:00 - 48360:00

have enterprise products and hope that

## 48360:00 - 48385:00

enterprises figure it out. I don't think

## 48385:00 - 48410:00

that that's the the reality. We just

## 48410:00 - 48440:00

need to lean in way harder on on both

## 48440:00 - 48470:00

ends of that spectrum.

## 48470:00 - 48515:00

>> Bud.ai is the website. Mike Kger is the

## 48515:00 - 48545:00

chief product officer at Anthropic.

## 48545:00 - 48565:00

Mike, always great to speak with you.

## 48565:00 - 48590:00

Thanks for coming on the show.

## 48590:00 - 48615:00

>> Thanks for having me, Alex. All right,

## 48615:00 - 48640:00

everybody. Thank you so much for

## 48640:00 - 48660:00

listening and watching. We will see you

## 48660:00 - 48685:00

on Friday to break down the week's news

## 48685:00 - 48720:00

and we will see you then on Big

## 48720:00+

Technology

