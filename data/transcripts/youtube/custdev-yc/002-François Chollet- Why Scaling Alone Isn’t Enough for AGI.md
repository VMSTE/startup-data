---
source: https://www.youtube.com/watch?v=k2ZLQC8P7dc
title: "François Chollet: Why Scaling Alone Isn’t Enough for AGI"
author: Y Combinator
date: 2026-03-27
views: 31776
description: >-
  François Chollet has spent years asking a different question than most of the
  AI world. Instead of scaling what already works, he’s trying to understand
  what intelligence actually is—and how to build it from first principles. In
  this episode of Lightcone, he traces that path from his early work on deep
  learning to the creation of the ARC prize, and the launch of ARC V3, a new
  benchmark designed to measure something deeper than performance: the ability
  to learn, adapt, and reason efficiently in entirely new environments. He
  explains why today’s systems may be hitting limits, what recent breakthroughs
  really mean, and why reaching true general intelligence may require a
  fundamentally different approach.


  00:00 - AGI by 2030?

  00:31 - Introducing Ndea: A New Path Beyond Deep Learning

  01:08 - A New ML Paradigm 

  01:30 - Replacing neural nets with compact symbolic programs

  03:04 - Why Ndea Isn’t Competing With Coding Agents

  05:20 - Why Everyone Might Be Wrong About Scaling LLMs

  07:22 - Why Coding Agents Suddenly Work So Well

  08:50 - The Limits of LLMs in Non-Verifiable Domains

  10:48 - What AGI Actually Means (And Why Most Definitions Are Wrong)

  13:30 - Why Deep Learning Hits a Wall 

  14:00 - ARC’s Origin Story

  18:20 - ARC Benchmarks Explained: From V1 to V3

  22:49 - The RL Loop Powering Coding Agents Today

  27:03 - ARC-AGI V3: Measuring “Agentic Intelligence”

  31:14 - Inside the ARC Game Studio

  35:31 - Could AGI Fit in 10,000 Lines of Code?

  44:01 - Building Ndea: From Idea to Compounding Research Stack

  46:46 - The Future of ARC: Benchmarks That Evolve With AI

  47:21 - Why There’s Still Huge Opportunity for New AI Paradigms

  53:37 - How to Build a Breakout Open Source Project - Lessons From Kera

  56:39 - Advice For How To Think About AI


  Apply to Y Combinator: https://www.ycombinator.com/apply

  Work at a startup: https://www.ycombinator.com/jobs
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:37:18.078Z
---

# François Chollet: Why Scaling Alone Isn’t Enough for AGI

## 00:00 - 45:00

I think we're probably looking at AGI

## 45:00 - 100:00

2030 around the time uh that we're going

## 100:00 - 150:00

to be releasing like maybe AR 6 or AR 7.

## 150:00 - 200:00

You're not going to stop uh AI progress.

## 200:00 - 230:00

I think I think it's too late for that.

## 230:00 - 265:00

And so the next question is okay like AI

## 265:00 - 300:00

progress is here. Uh it's actually going

## 300:00 - 325:00

to keep accelerating. How do you make

## 325:00 - 350:00

use of it? How do you leverage? How do

## 350:00 - 380:00

you ride the wave? That's the question

## 380:00 - 515:00

to ask.

## 515:00 - 550:00

Today we're lucky to be joined by France

## 550:00 - 590:00

Chole, founder of the ARK Prize, a

## 590:00 - 645:00

global competition to solve the ARC AGI

## 645:00 - 700:00

benchmark. His latest project is NDIA, a

## 700:00 - 740:00

lab exploring a new paradigm in frontier

## 740:00 - 790:00

AI research. Francois is one of the best

## 790:00 - 810:00

people in the world to help us

## 810:00 - 855:00

understand the current AI moment and

## 855:00 - 890:00

where all of this is going. Franuis,

## 890:00 - 915:00

thank you so much for joining us today

## 915:00 - 960:00

and congrats on the launch of Arc AGI

## 960:00 - 975:00

V3.

## 975:00 - 995:00

>> Thanks so much for having me. I'm super

## 995:00 - 1025:00

excited to be here. Super exciting time

## 1025:00 - 1040:00

to talk about AI.

## 1040:00 - 1075:00

>> So Fran, tell us a little bit about

## 1075:00 - 1110:00

India. So what exactly is it and what

## 1110:00 - 1140:00

are you guys trying to achieve,

## 1140:00 - 1190:00

>> right? So NDI is this new AGI research

## 1190:00 - 1230:00

lab and we are trying some very

## 1230:00 - 1270:00

different ideas and so our goal is

## 1270:00 - 1300:00

basically to build this new branch of

## 1300:00 - 1330:00

machine learning that will be much

## 1330:00 - 1385:00

closer to optimal unlike unlike deep

## 1385:00 - 1390:00

learning.

## 1390:00 - 1435:00

>> All of us right now are sort of taken by

## 1435:00 - 1475:00

what's going on with code. Uh I have

## 1475:00 - 1505:00

sort of this viral moment right now

## 1505:00 - 1555:00

where I got to 40,000 stars this morning

## 1555:00 - 1595:00

>> on uh GStack. So it's like, oh, this is

## 1595:00 - 1625:00

an open source project that now is one

## 1625:00 - 1660:00

of the biggest ones and I have more than

## 1660:00 - 1705:00

a 100 PRs from contributors to deal

## 1705:00 - 1740:00

with. I guess you're, you know, one of

## 1740:00 - 1765:00

the best people to talk to about this

## 1765:00 - 1800:00

because you're you're actually literally

## 1800:00 - 1825:00

coming up with something that is a

## 1825:00 - 1855:00

totally different pathway.

## 1855:00 - 1895:00

>> That's right. That's right. So uh what

## 1895:00 - 1925:00

we're doing at India is uh we're doing

## 1925:00 - 1970:00

program synthesis research. And when I

## 1970:00 - 1990:00

talk about program synthesis, often

## 1990:00 - 2020:00

people ask me, oh, so are you doing like

## 2020:00 - 2055:00

codegen? are you building an alternative

## 2055:00 - 2085:00

to coding agents and that's actually not

## 2085:00 - 2115:00

at all what we are doing. We are working

## 2115:00 - 2165:00

at a much much more uh much lower level

## 2165:00 - 2190:00

than that. Uh what we're actually doing

## 2190:00 - 2225:00

is that we are trying to build a new

## 2225:00 - 2260:00

branch of machine learning an

## 2260:00 - 2305:00

alternative to deep learning itself uh

## 2305:00 - 2330:00

rather than like coding agents. Coding

## 2330:00 - 2350:00

agents are like this very very high

## 2350:00 - 2395:00

level last layer piece of the stack and

## 2395:00 - 2430:00

we're actually trying to rebuild the

## 2430:00 - 2450:00

whole stack on top of different

## 2450:00 - 2490:00

foundations. So we're building a new

## 2490:00 - 2540:00

learning substrate that's very different

## 2540:00 - 2580:00

from you know parametric learning deep

## 2580:00 - 2630:00

learning. So if you go back to uh the

## 2630:00 - 2665:00

problem of machine learning you have

## 2665:00 - 2705:00

some input data some target data and

## 2705:00 - 2740:00

you're trying to find a function that

## 2740:00 - 2780:00

will map the inputs to the targets that

## 2780:00 - 2835:00

will hopefully generalize to new inputs.

## 2835:00 - 2870:00

And uh if you're doing deep learning

## 2870:00 - 2900:00

what you're doing is that you have this

## 2900:00 - 2935:00

parametric curve that serves as your as

## 2935:00 - 2955:00

your function as your model and you're

## 2955:00 - 2990:00

trying to fit the parameters of the

## 2990:00 - 3030:00

curve via cron descent. And this is

## 3030:00 - 3070:00

basically what we're doing uh except

## 3070:00 - 3100:00

we're replacing the parametric curve

## 3100:00 - 3155:00

with a symbolic model that is meant to

## 3155:00 - 3200:00

be as small as possible. It's like the

## 3200:00 - 3260:00

simplest uh possible uh model to explain

## 3260:00 - 3295:00

the data to model what's going on. uh

## 3295:00 - 3325:00

and of course if you're doing that you

## 3325:00 - 3370:00

cannot apply descent anymore. So we are

## 3370:00 - 3405:00

building something that we call symbolic

## 3405:00 - 3445:00

descent which is like the symbolic space

## 3445:00 - 3490:00

equivalent of grand descent. The idea is

## 3490:00 - 3525:00

to build this new machine learning

## 3525:00 - 3595:00

engine that's giving you uh extremely

## 3595:00 - 3645:00

concise symbolic models of the data

## 3645:00 - 3675:00

you're feeding into it and then we're

## 3675:00 - 3705:00

going to make it scale. And so

## 3705:00 - 3725:00

everything you're doing with machine

## 3725:00 - 3760:00

learning today with parametric curves,

## 3760:00 - 3795:00

we should be able to do it uh with

## 3795:00 - 3850:00

symbolic models in the future in a in a

## 3850:00 - 3900:00

way that will be much much closer to

## 3900:00 - 3945:00

optimality. Much closer to optimality in

## 3945:00 - 3975:00

the sense that you're going to need much

## 3975:00 - 4015:00

less data to obtain the models. The

## 4015:00 - 4045:00

models are going to run much more

## 4045:00 - 4080:00

efficiently at at inference time because

## 4080:00 - 4105:00

they're going to be so small. And

## 4105:00 - 4130:00

because they're so small, they will also

## 4130:00 - 4160:00

generalize much better and compose much

## 4160:00 - 4190:00

better. you know the the minimum

## 4190:00 - 4230:00

description length principle that the

## 4230:00 - 4260:00

model of the data that is most likely to

## 4260:00 - 4300:00

generalize is the shortest and I think

## 4300:00 - 4330:00

you cannot find a model like this if

## 4330:00 - 4350:00

you're doing parametric learning you

## 4350:00 - 4385:00

need to you need to try symbolic

## 4385:00 - 4410:00

>> that's fascinating

## 4410:00 - 4440:00

>> so the rest of the industry is just

## 4440:00 - 4460:00

pouring more and more billions of

## 4460:00 - 4505:00

dollars down an approach that was set

## 4505:00 - 4545:00

years ago can you like help make the

## 4545:00 - 4575:00

case for why you think that it's the

## 4575:00 - 4600:00

right thing to explore alternate

## 4600:00 - 4620:00

approaches instead of just to keep

## 4620:00 - 4645:00

putting more money into the current

## 4645:00 - 4650:00

approach

## 4650:00 - 4690:00

>> I mean everybody body is uh is uh uh you

## 4690:00 - 4720:00

know building on top of the LLM stack

## 4720:00 - 4755:00

these days which makes sense because you

## 4755:00 - 4790:00

know the the returns are there like it's

## 4790:00 - 4825:00

actually working so it would seem very

## 4825:00 - 4875:00

sensible for everybody to just be doing

## 4875:00 - 4900:00

uh what seems to be the the the

## 4900:00 - 4940:00

currently most productive path uh but

## 4940:00 - 4975:00

artic it's it's counterproductive to

## 4975:00 - 5010:00

have everybody working on the same thing

## 5010:00 - 5050:00

like I personally don't think that uh

## 5050:00 - 5100:00

machine learning or AI in 50 years is

## 5100:00 - 5120:00

still going to be built on this stag I

## 5120:00 - 5155:00

think this is a stag that is uh very

## 5155:00 - 5195:00

price maybe it even gets us to ag but

## 5195:00 - 5245:00

it's not as efficient as it should be. I

## 5245:00 - 5285:00

think it's inevitable that uh the world

## 5285:00 - 5340:00

of AI will trend over time towards

## 5340:00 - 5375:00

optimality and so I'm trying to sort of

## 5375:00 - 5435:00

like leaprog directly uh to optimality

## 5435:00 - 5465:00

like to build to build the foundations

## 5465:00 - 5505:00

of optimal AI today but in general you

## 5505:00 - 5555:00

know our vision is very ambitious and

## 5555:00 - 5575:00

I'm not saying that we're going to be

## 5575:00 - 5610:00

successful like we have maybe a 10 or

## 5610:00 - 5660:00

15% chance of success uh but that is

## 5660:00 - 5710:00

enough uh that it's worth trying right

## 5710:00 - 5740:00

and I think in general like among among

## 5740:00 - 5795:00

listeners. If you have uh a big idea and

## 5795:00 - 5825:00

it has very low chance of success, but

## 5825:00 - 5865:00

uh if it works, it's going to be big and

## 5865:00 - 5890:00

no one else is going to be working on

## 5890:00 - 5910:00

it, right? It's it's not something

## 5910:00 - 5940:00

popular. It's not something if you don't

## 5940:00 - 5970:00

do it, no one else will do it. And this

## 5970:00 - 6005:00

is basically our situation. If you're in

## 6005:00 - 6040:00

this situation, then then you should you

## 6040:00 - 6060:00

should should try a chance, you know,

## 6060:00 - 6075:00

should should go and work on it.

## 6075:00 - 6100:00

>> I mean, that's almost like the mission

## 6100:00 - 6125:00

statement of why cominator, the thing

## 6125:00 - 6140:00

that you just said.

## 6140:00 - 6150:00

>> Yeah.

## 6150:00 - 6175:00

>> Yeah. The reason it's important is that

## 6175:00 - 6200:00

again, if we don't do it, no one else

## 6200:00 - 6230:00

will do it, right? So it's worth trying.

## 6230:00 - 6255:00

Even if we don't succeed, it's worth

## 6255:00 - 6265:00

trying.

## 6265:00 - 6300:00

>> Has the success well very specifically

## 6300:00 - 6325:00

of the coding agents I guess built on

## 6325:00 - 6365:00

top of the LLM stack like has their

## 6365:00 - 6405:00

success surprised you at all in

## 6405:00 - 6430:00

particular like say over the last 6

## 6430:00 - 6440:00

months or so?

## 6440:00 - 6460:00

>> Yeah, absolutely. I think it has

## 6460:00 - 6490:00

surprised many people. It definitely did

## 6490:00 - 6525:00

surprise me. If you look at why

## 6525:00 - 6550:00

everything is is starting to work so

## 6550:00 - 6580:00

well with squinging agents, it's really

## 6580:00 - 6630:00

because uh code provides you with a

## 6630:00 - 6665:00

verifiable reward signal. And I think

## 6665:00 - 6695:00

right now we're in this situation where

## 6695:00 - 6735:00

any problem where the solutions you

## 6735:00 - 6770:00

propose can be uh uh formally verified

## 6770:00 - 6795:00

and you can actually trust the reward

## 6795:00 - 6825:00

signal. It's not just some guess made by

## 6825:00 - 6875:00

a model. Any domain like this uh can be

## 6875:00 - 6905:00

fully automated with current technology

## 6905:00 - 6960:00

with with the LM based stack and uh code

## 6960:00 - 6990:00

is sort of like the first domain to fall

## 6990:00 - 7015:00

but there will be many others in the

## 7015:00 - 7050:00

future. I think mathematics is also is

## 7050:00 - 7100:00

also primed to see a revolution in next

## 7100:00 - 7130:00

few years for the same reasons again

## 7130:00 - 7160:00

because the domain just gives you

## 7160:00 - 7200:00

verifiable rewards. I guess the

## 7200:00 - 7240:00

challenge for a formally verified domain

## 7240:00 - 7290:00

is you have to

## 7290:00 - 7325:00

somehow take a domain and make it

## 7325:00 - 7355:00

verifiable which is the trick I mean

## 7355:00 - 7390:00

code is very natural you could test

## 7390:00 - 7420:00

there's bugs compiles etc and

## 7420:00 - 7455:00

mathematics as well where there all the

## 7455:00 - 7500:00

theorems and proofs work out I guess it

## 7500:00 - 7540:00

becomes more nebulous when you go couple

## 7540:00 - 7585:00

degrees off where there fields that are

## 7585:00 - 7635:00

not naturally formally verified and you

## 7635:00 - 7655:00

need to come up with a

## 7655:00 - 7705:00

>> again with some sort of a function

## 7705:00 - 7765:00

to come up with that reward that makes

## 7765:00 - 7795:00

it verifiable with very fuzzy things

## 7795:00 - 7840:00

like let's say English language and

## 7840:00 - 7880:00

composing the perfect essay.

## 7880:00 - 7900:00

>> How do you make that formally

## 7900:00 - 7915:00

verifiable?

## 7915:00 - 7955:00

>> Yeah. Yeah. Absolutely. I mean writing

## 7955:00 - 7995:00

essays is you know the typical example

## 7995:00 - 8040:00

of a domain that's not verifiable. And

## 8040:00 - 8065:00

so what you're going to see is that

## 8065:00 - 8100:00

progress of reasoning models and and

## 8100:00 - 8145:00

basel on this type of of of domain is is

## 8145:00 - 8175:00

you know is going to be very slow

## 8175:00 - 8205:00

because the stack we're using like the

## 8205:00 - 8250:00

LM stack is very very reliant on its

## 8250:00 - 8280:00

training data. It's basically just

## 8280:00 - 8340:00

operationalizing the train data and for

## 8340:00 - 8370:00

writing essays the train data is coming

## 8370:00 - 8430:00

from uh human experts like annotating uh

## 8430:00 - 8475:00

answers and that's costly. So you're

## 8475:00 - 8495:00

going to see this very very slow

## 8495:00 - 8520:00

progress. Maybe maybe it's even going to

## 8520:00 - 8555:00

stall. But but for any any verifiable

## 8555:00 - 8590:00

domain like take code for instance what

## 8590:00 - 8640:00

was the big unlock is uh when uh when

## 8640:00 - 8675:00

people started creating this codebased

## 8675:00 - 8715:00

like training environment uh for for

## 8715:00 - 8765:00

post training uh where the the the

## 8765:00 - 8795:00

reward signal the verification signal is

## 8795:00 - 8835:00

provided by things like uh unit tests

## 8835:00 - 8870:00

and so on. And so that means that uh the

## 8870:00 - 8910:00

model was not just working from human

## 8910:00 - 8945:00

pro annotations. It was actually trying

## 8945:00 - 9000:00

its own things uh verifying the answer

## 9000:00 - 9040:00

and uh and generating a lot lot more

## 9040:00 - 9070:00

string data in the process. So a much

## 9070:00 - 9120:00

denser coverage of the problem space and

## 9120:00 - 9160:00

not just coverage in terms of like is is

## 9160:00 - 9200:00

the answer right or wrong but also

## 9200:00 - 9240:00

starting to build uh models of the

## 9240:00 - 9285:00

execution traces right. uh so that the

## 9285:00 - 9325:00

models could start incorporating a an

## 9325:00 - 9355:00

execution model very much the way that

## 9355:00 - 9390:00

uh uh human programmers you know when

## 9390:00 - 9415:00

they look at code they're sort of like

## 9415:00 - 9445:00

executing the code in their minds they

## 9445:00 - 9475:00

they keep track of value variables and

## 9475:00 - 9505:00

so on is also what the models are trying

## 9505:00 - 9525:00

to do now and this is why it's working

## 9525:00 - 9565:00

so well and it's possible because you're

## 9565:00 - 9600:00

working with this very formal fully

## 9600:00 - 9630:00

verifiable environment you cannot do

## 9630:00 - 9655:00

that with assess you cannot do that with

## 9655:00 - 9695:00

you know law or or many other problems

## 9695:00 - 9730:00

>> I think I really like how you define

## 9730:00 - 9785:00

intelligence and how we measure it which

## 9785:00 - 9815:00

brings to the question of uh also

## 9815:00 - 9855:00

sharing having you share the history of

## 9855:00 - 9880:00

uh ARGI.

## 9880:00 - 9925:00

>> Yeah. So my my definition of uh general

## 9925:00 - 9965:00

intelligence you know many people around

## 9965:00 - 10010:00

the industry these days they say uh AGI

## 10010:00 - 10035:00

is going to be a system that can

## 10035:00 - 10085:00

automate most economically economically

## 10085:00 - 10135:00

valuable tasks and to me that definition

## 10135:00 - 10185:00

is it's about automation it's not about

## 10185:00 - 10205:00

intelligence not about general

## 10205:00 - 10270:00

intelligence so my definition is uh AGI

## 10270:00 - 10295:00

is basically going to be a system that

## 10295:00 - 10335:00

can approach any new problem any new

## 10335:00 - 10390:00

task any new domain and make sense of it

## 10390:00 - 10465:00

like model it become competent at it uh

## 10465:00 - 10510:00

with the same degree of efficiency as a

## 10510:00 - 10535:00

human could. So meaning it's going to

## 10535:00 - 10565:00

need basically the same amount of

## 10565:00 - 10605:00

training data uh and training computes

## 10605:00 - 10630:00

as as a human would which is which is

## 10630:00 - 10660:00

very little like humans are really

## 10660:00 - 10715:00

really uh data efficient. So general

## 10715:00 - 10760:00

intelligence is human level skill

## 10760:00 - 10790:00

acquisition efficiency on the on the

## 10790:00 - 10830:00

same scope of tasks that uh humans could

## 10830:00 - 10880:00

potentially uh round to do.

## 10880:00 - 10900:00

>> Do you think it's possible that we will

## 10900:00 - 10945:00

accomplish the first definition of AGI,

## 10945:00 - 10975:00

the automate most economically useful

## 10975:00 - 11020:00

work before we accomplish your

## 11020:00 - 11025:00

definition?

## 11025:00 - 11040:00

>> Absolutely. I think that's that's a

## 11040:00 - 11080:00

trajectory that we're on right now. And

## 11080:00 - 11115:00

I think it's already true that in

## 11115:00 - 11150:00

principle current technology can fully

## 11150:00 - 11205:00

automate at human level or beyond any

## 11205:00 - 11235:00

domain where you have uh verifiable

## 11235:00 - 11270:00

rewards, right? And code code being the

## 11270:00 - 11310:00

first one. And I think figuring out AGI,

## 11310:00 - 11360:00

figuring out like human level uh you

## 11360:00 - 11390:00

know learning efficiency over arbitrary

## 11390:00 - 11440:00

tasks that's probably going to take a

## 11440:00 - 11465:00

different sort of technology different a

## 11465:00 - 11495:00

different mindset different approach. Do

## 11495:00 - 11530:00

you think that LMS can be bent to have

## 11530:00 - 11585:00

the same sample efficiency as humans or

## 11585:00 - 11610:00

do you think it's like fundamentally

## 11610:00 - 11645:00

just impossible and we need a new

## 11645:00 - 11670:00

approach and that's that's the thing

## 11670:00 - 11690:00

that you're hoping hoping to solve

## 11690:00 - 11720:00

>> with enough comput everything starts

## 11720:00 - 11755:00

looking like everything else every like

## 11755:00 - 11775:00

computer is a great equalizer every

## 11775:00 - 11810:00

approach starts looking the same and I

## 11810:00 - 11860:00

think it's possible in principle to

## 11860:00 - 11885:00

build something that looks a lot like a

## 11885:00 - 11945:00

GI on top of the LLM stack uh but it's

## 11945:00 - 11980:00

not going to be LLMs per se it's going

## 11980:00 - 11990:00

to

## 11990:00 - 12015:00

this new layer perhaps you know it's

## 12015:00 - 12050:00

going to be even a few layers above not

## 12050:00 - 12080:00

just one layer above but a few layers

## 12080:00 - 12130:00

above uh but you can build it on top of

## 12130:00 - 12165:00

LLM because LM are kind of computer

## 12165:00 - 12180:00

right I see

## 12180:00 - 12215:00

>> uh I do believe however this would be

## 12215:00 - 12250:00

the wrong thing to do because it would

## 12250:00 - 12295:00

be very inefficient I think AI AI

## 12295:00 - 12335:00

research will have to trend towards not

## 12335:00 - 12370:00

just efficiency but in fact optimality

## 12370:00 - 12420:00

over time and for this reason future AI

## 12420:00 - 12460:00

in a few decades uh it's not going to be

## 12460:00 - 12510:00

this harness on top of a reasoning model

## 12510:00 - 12560:00

on top of a basel is going to be much

## 12560:00 - 12585:00

much lower than that.

## 12585:00 - 12620:00

>> To Diana's question, do you want to talk

## 12620:00 - 12655:00

about how you actually designed ARGI and

## 12655:00 - 12680:00

why it's a good barometer of that?

## 12680:00 - 12705:00

>> I mean I you know I've been doing deep

## 12705:00 - 12740:00

learning for a very very long time and

## 12740:00 - 12790:00

initially my my my tech my mindset was

## 12790:00 - 12815:00

that deep learning was going to be able

## 12815:00 - 12835:00

to do everything.

## 12835:00 - 12875:00

>> You were the creative at KAS before even

## 12875:00 - 12905:00

all the other frameworks became very

## 12905:00 - 12920:00

popular.

## 12920:00 - 12940:00

>> That that's right. That's right. I was a

## 12940:00 - 12985:00

trained deploying model uh uh for

## 12985:00 - 13015:00

natural language processing in fact

## 13015:00 - 13100:00

>> in uh 2014 and uh from that work uh you

## 13100:00 - 13135:00

know I actually started uh developing

## 13135:00 - 13170:00

this open source library which I I

## 13170:00 - 13220:00

released uh in fact uh exactly 11 years

## 13220:00 - 13265:00

ago uh March March 2015

## 13265:00 - 13295:00

>> uh so it was kas and and then it got

## 13295:00 - 13330:00

popular and then I'd end up uh sort of

## 13330:00 - 13370:00

like doing less of the research that I

## 13370:00 - 13410:00

that I started kas for and more of

## 13410:00 - 13435:00

working on the framework itself. just

## 13435:00 - 13455:00

because it has really really good

## 13455:00 - 13500:00

product market fit. And so my my take

## 13500:00 - 13520:00

you know around that time around like

## 13520:00 - 13565:00

2015 2016 was that deep learning was

## 13565:00 - 13595:00

extremely general that you could do

## 13595:00 - 13620:00

everything with deep learning that you

## 13620:00 - 13650:00

didn't need in anything else. It was

## 13650:00 - 13700:00

training complete. So uh my tech was

## 13700:00 - 13725:00

basically that deep learning was

## 13725:00 - 13765:00

differentiable programming. Uh so

## 13765:00 - 13790:00

anything you would do with software you

## 13790:00 - 13825:00

could in principle train a deep learning

## 13825:00 - 13860:00

model on the right inputs and outputs to

## 13860:00 - 13930:00

do the same thing. And uh in uh 2016 I

## 13930:00 - 13995:00

was doing uh research at Google brain on

## 13995:00 - 14030:00

trying to train deep learning models to

## 14030:00 - 14080:00

help with uh reasoning problems and in

## 14080:00 - 14130:00

particular uh first order logic problems

## 14130:00 - 14185:00

uh uh theorem proving and so on. And I

## 14185:00 - 14225:00

started finding that you could not

## 14225:00 - 14300:00

really get cryion descent to encode uh

## 14300:00 - 14325:00

uh sort of like cresing style

## 14325:00 - 14375:00

algorithms. It was not because the

## 14375:00 - 14410:00

models could not represent these

## 14410:00 - 14435:00

algorithms. It was because cryion

## 14435:00 - 14485:00

descent could not find them. Right? So

## 14485:00 - 14520:00

the problem was that it wasn't about

## 14520:00 - 14555:00

deep learning not being train or

## 14555:00 - 14585:00

anything like that. Like that was not

## 14585:00 - 14605:00

the problem. The problem was cryon

## 14605:00 - 14650:00

descent right descent would not find

## 14650:00 - 14690:00

generalizable programs. It would instead

## 14690:00 - 14725:00

uh end up doing uh overfeit pattern

## 14725:00 - 14775:00

matching right over over sequences of uh

## 14775:00 - 14790:00

uh input tokens

## 14790:00 - 14815:00

>> which I guess people could argue like

## 14815:00 - 14855:00

that's what's happening. I mean this see

## 14855:00 - 14885:00

what's happening today in a in a in a

## 14885:00 - 14910:00

slightly

## 14910:00 - 14945:00

>> it's it's a slightly high higher level

## 14945:00 - 14955:00

version of

## 14955:00 - 14980:00

>> it's with a lot of data so it doesn't

## 14980:00 - 15005:00

feel like overfitting because the data

## 15005:00 - 15030:00

has a lot more distribution

## 15030:00 - 15060:00

>> with a lot more data and also I think

## 15060:00 - 15090:00

models today uh they're a lot more

## 15090:00 - 15120:00

compressive of the data which is why

## 15120:00 - 15145:00

where they they generalize better

## 15145:00 - 15190:00

>> all models are wrong but some models are

## 15190:00 - 15225:00

useful and then I guess what I'm hearing

## 15225:00 - 15265:00

is like your method might find the right

## 15265:00 - 15275:00

model

## 15275:00 - 15315:00

>> that's right that's uh that's uh where

## 15315:00 - 15355:00

where the idea came from and I was like,

## 15355:00 - 15395:00

you know, at the time in back in 2016,

## 15395:00 - 15430:00

2017, I was like, okay, we're going to

## 15430:00 - 15485:00

need a a benchmark to capture the ideas.

## 15485:00 - 15505:00

>> Uh we're going to need a program

## 15505:00 - 15535:00

synthesis benchmark.

## 15535:00 - 15590:00

>> And uh my my mental model for that was

## 15590:00 - 15605:00

ImageNet.

## 15605:00 - 15630:00

>> I was like, oh, I'm going to make the

## 15630:00 - 15665:00

imageet of reasoning. So, I started

## 15665:00 - 15710:00

brainstorming a few ideas around like

## 15710:00 - 15750:00

2017. I explored many different things.

## 15750:00 - 15800:00

Uh I tried working with uh in part solar

## 15800:00 - 15850:00

automator like u a setup where you show

## 15850:00 - 15895:00

a model uh solar automator outputs and

## 15895:00 - 15930:00

it must recreate uh the program that

## 15930:00 - 15960:00

generated them like that sort of thing.

## 15960:00 - 16005:00

Uh and eventually I settled on the uh

## 16005:00 - 16065:00

RGI format uh around like early 2018.

## 16065:00 - 16095:00

You know I was doing this on the side.

## 16095:00 - 16120:00

It was a side project like my main

## 16120:00 - 16170:00

project was uh developing kas at Google.

## 16170:00 - 16205:00

I wasn't moving very that very fast uh

## 16205:00 - 16265:00

on that. Uh so summer 2018 uh I wrote

## 16265:00 - 16315:00

the ARC task editor and then I started

## 16315:00 - 16360:00

just making lots of tasks by hand and

## 16360:00 - 16390:00

about one year later I had made 10,000

## 16390:00 - 16435:00

tasks and so I wrote up uh the paper

## 16435:00 - 16475:00

that was explaining what this was about

## 16475:00 - 16505:00

what the big idea was like intelligence

## 16505:00 - 16560:00

as as skill acquisition efficiency and

## 16560:00 - 16610:00

and I published all of that in in 2019.

## 16610:00 - 16670:00

In parallel, GB3 2020 was coming out and

## 16670:00 - 16720:00

starting to show signs until the chat

## 16720:00 - 16780:00

GBD moment around 2022, end of the year

## 16780:00 - 16820:00

and the industry took off with that and

## 16820:00 - 16845:00

this was one of the benchmark that it

## 16845:00 - 16880:00

was really performing really badly and

## 16880:00 - 16905:00

it was very obscure. I don't think many

## 16905:00 - 16945:00

people knew about it. It was mostly

## 16945:00 - 16985:00

niche research communities that maybe

## 16985:00 - 17005:00

read your paper.

## 17005:00 - 17035:00

>> Yeah, people who worked on programs this

## 17035:00 - 17075:00

knew about it. uh but a lot of people

## 17075:00 - 17100:00

who worked on on deep learning on

## 17100:00 - 17125:00

scaling up LLMs they didn't really care

## 17125:00 - 17160:00

for it and part of the reason why is

## 17160:00 - 17225:00

because LMS did not work well or at all

## 17225:00 - 17270:00

on the benchmark but benchmark to

## 17270:00 - 17300:00

capture the attention of the research

## 17300:00 - 17330:00

community it needs to start working a

## 17330:00 - 17385:00

little right uh if it's too hard people

## 17385:00 - 17415:00

are are just going to dismiss it

## 17415:00 - 17440:00

>> you're just ahead of your time clearly

## 17440:00 - 17500:00

because we're not on ARC AGI one anymore

## 17500:00 - 17545:00

and then two is reaching saturation

## 17545:00 - 17565:00

And then that's right

## 17565:00 - 17590:00

>> three is out now.

## 17590:00 - 17600:00

>> Yes.

## 17600:00 - 17660:00

>> And I think the cool thing about RKGI it

## 17660:00 - 17725:00

has been a very good barometer for the

## 17725:00 - 17750:00

industry of the big changes that

## 17750:00 - 17805:00

happened because V1 was not working at

## 17805:00 - 17885:00

all for a long time until 2025

## 17885:00 - 17930:00

when reasoning models came out. Right.

## 17930:00 - 17980:00

>> Yeah. Absolutely. If you look at uh PRI

## 17980:00 - 18035:00

performance on arc v1 first and then v2

## 18035:00 - 18090:00

uh so bas uh we're scoring extremely low

## 18090:00 - 18145:00

on v1 like sub 10% basically and I mean

## 18145:00 - 18205:00

it was true of uh the original like GP3

## 18205:00 - 18250:00

scoring zero but that's even true of the

## 18250:00 - 18295:00

latest basel lamps today you know as of

## 18295:00 - 18305:00

as of March

## 18305:00 - 18325:00

>> without reason without reasoning

## 18325:00 - 18355:00

>> without reasoning yeah so the base

## 18355:00 - 18410:00

models so performance of of basel lamps

## 18410:00 - 18445:00

on on v1 stayed very very low even

## 18445:00 - 18485:00

though in the meantime you know we had

## 18485:00 - 18545:00

scaled up these models by 50,000x right

## 18545:00 - 18570:00

so it was really telling you that you

## 18570:00 - 18600:00

know more scale scaling up pre-training

## 18600:00 - 18630:00

alone was not going to crack the

## 18630:00 - 18670:00

benchmark this was not enough to

## 18670:00 - 18705:00

demonstrate that the model had fluid

## 18705:00 - 18770:00

intelligence and then uh the moment uh

## 18770:00 - 18815:00

models started performing well on ark1

## 18815:00 - 18850:00

was with the first reasoning models in

## 18850:00 - 18920:00

part uh the openi 01 and then 03 uh

## 18920:00 - 18950:00

models which by the way they were

## 18950:00 - 18990:00

demonstrated by openi on arc because it

## 18990:00 - 19025:00

was the one unsaturated reasoning

## 19025:00 - 19055:00

benchmark that was really showing that

## 19055:00 - 19095:00

this model was different that that new

## 19095:00 - 19130:00

capabilities that we had not seen before

## 19130:00 - 19170:00

and so with reasoning models you start

## 19170:00 - 19205:00

seeing this sudden like step function

## 19205:00 - 19260:00

change uh on on ark1 and so ar1 was

## 19260:00 - 19300:00

really the benchmark that signaled that

## 19300:00 - 19335:00

at this moment in time something was

## 19335:00 - 19350:00

happening and

## 19350:00 - 19360:00

>> something big

## 19360:00 - 19390:00

>> yeah something big like new capabilities

## 19390:00 - 19440:00

were emerging like reasoning was new and

## 19440:00 - 19480:00

different and it was actually not

## 19480:00 - 19510:00

obvious at the time like you know I

## 19510:00 - 19550:00

don't know if you remember when uh when

## 19550:00 - 19595:00

03 uh preview was was announced by open

## 19595:00 - 19600:00

eye

## 19600:00 - 19625:00

>> that was end of 2024 actually

## 19625:00 - 19685:00

>> yeah December 2024 and like sure it was

## 19685:00 - 19735:00

like huge like step function progress on

## 19735:00 - 19790:00

arc uh but it was very expensive we did

## 19790:00 - 19820:00

not really have product market fit

## 19820:00 - 19860:00

effectively but if you looked at uh at

## 19860:00 - 19890:00

arc results you knew that this was big

## 19890:00 - 19945:00

and important and Then we released AR2

## 19945:00 - 19980:00

which was the same format but uh more

## 19980:00 - 20015:00

difficult like with more uh uh

## 20015:00 - 20060:00

composition uh at the level of the the

## 20060:00 - 20100:00

the reasoning chains. And what happened

## 20100:00 - 20130:00

is that so the the earliest reasoning

## 20130:00 - 20180:00

models started very very low on R2 and

## 20180:00 - 20225:00

then around the same time as coding

## 20225:00 - 20270:00

agents started working you saw this

## 20270:00 - 20315:00

>> yeah so very very recent just few months

## 20315:00 - 20370:00

ago you saw this uh very very fast like

## 20370:00 - 20425:00

saturation of R2 and so again like R2

## 20425:00 - 20470:00

signaled that yes there was this this

## 20470:00 - 20500:00

new set of capabilities emerging. I

## 20500:00 - 20525:00

think the benchmark did a really good

## 20525:00 - 20560:00

job at capturing the advant of reasoning

## 20560:00 - 20600:00

models and then the advance uh of

## 20600:00 - 20630:00

agentic coding like this this new

## 20630:00 - 20675:00

paradigm where if you have uh verifiable

## 20675:00 - 20705:00

rewards then you can basically fully

## 20705:00 - 20745:00

automate uh the domain which by the way

## 20745:00 - 20785:00

is true of arc like arc does provide a

## 20785:00 - 20800:00

verifiable reward

## 20800:00 - 20840:00

>> I guess for v2 what what caused the so

## 20840:00 - 20880:00

one was clearly reasoning two a

## 20880:00 - 20920:00

benchmark doesn't care how you solve it

## 20920:00 - 20960:00

I guess embedded in what you said like

## 20960:00 - 21030:00

were people using codegen to then solve.

## 21030:00 - 21060:00

>> That's right. So not not necessarily

## 21060:00 - 21115:00

codegen uh per se but uh the frontier

## 21115:00 - 21175:00

labs have been targeting arc v2 and uh

## 21175:00 - 21210:00

the progress you saw on arc v2 is

## 21210:00 - 21250:00

actually a result uh of this very very

## 21250:00 - 21285:00

large scale targeting. So what you can

## 21285:00 - 21330:00

do to solve RG2 is you ask your

## 21330:00 - 21390:00

reasoning model to make more tasks like

## 21390:00 - 21430:00

those in the benchmark uh and then you

## 21430:00 - 21460:00

try to solve them using let's say let's

## 21460:00 - 21505:00

say program induction for instance uh

## 21505:00 - 21530:00

still using your reasoning model then

## 21530:00 - 21560:00

you verify the solution again it's

## 21560:00 - 21600:00

verifiable so you can you can trust uh

## 21600:00 - 21655:00

the answer um and then you fine-tune the

## 21655:00 - 21690:00

model on the successful reasoning chains

## 21690:00 - 21715:00

and then you keep repeating like you

## 21715:00 - 21745:00

generate new tasks you solve them you

## 21745:00 - 21780:00

verify the solution you fine tune the

## 21780:00 - 21825:00

model on the reasoning chains and um you

## 21825:00 - 21860:00

can keep doing this millions of times

## 21860:00 - 21890:00

right like you just need to spend more

## 21890:00 - 21900:00

money

## 21900:00 - 21940:00

>> this is the RL loop that happening yeah

## 21940:00 - 21975:00

>> and the the new paradigm in AI is

## 21975:00 - 22010:00

basically that any domain where this is

## 22010:00 - 22045:00

true where you have the ability to join

## 22045:00 - 22105:00

these this true uh verification signals

## 22105:00 - 22140:00

you you can run this this kind of loop

## 22140:00 - 22165:00

right if you can run this kind of loop

## 22165:00 - 22210:00

you can mine uh you can brute force mine

## 22210:00 - 22245:00

effectively the entire space and get

## 22245:00 - 22270:00

extremely high performance. This is

## 22270:00 - 22295:00

basically the the process through which

## 22295:00 - 22335:00

AR2 was saturated. So what it tells you

## 22335:00 - 22370:00

is that it's not so much that the models

## 22370:00 - 22410:00

have higher fluid intelligence uh than

## 22410:00 - 22445:00

than they did with the with the first

## 22445:00 - 22485:00

models. It's just that you have this new

## 22485:00 - 22530:00

paradigm of post training. And this is

## 22530:00 - 22570:00

exactly what led to agency coding. So it

## 22570:00 - 22600:00

does matter. It is it is valuable. It is

## 22600:00 - 22610:00

useful.

## 22610:00 - 22655:00

>> It's not that the models are smarter.

## 22655:00 - 22700:00

It's that they're suddenly more useful.

## 22700:00 - 22735:00

It is possible to be more useful in

## 22735:00 - 22765:00

particular domains without being

## 22765:00 - 22810:00

smarter. Yeah, clearly because that's

## 22810:00 - 22830:00

means good things for me. I'm not

## 22830:00 - 22880:00

getting any smarter right now like at

## 22880:00 - 22920:00

you know age 45. But you know I can

## 22920:00 - 22960:00

learn how to do things and that's sort

## 22960:00 - 22985:00

of what's happening with the models as

## 22985:00 - 23005:00

of like late.

## 23005:00 - 23050:00

>> Yeah, absolutely. When it comes to uh

## 23050:00 - 23080:00

competency, there's always a trade-off

## 23080:00 - 23120:00

between intelligence and knowledge. If

## 23120:00 - 23140:00

you have more knowledge, if you have

## 23140:00 - 23175:00

better training, uh you need less

## 23175:00 - 23215:00

intelligence to be competent. And that's

## 23215:00 - 23265:00

exactly uh what happened with the the

## 23265:00 - 23305:00

rise of coding agents, right? The models

## 23305:00 - 23345:00

don't have higher fluid intelligence per

## 23345:00 - 23390:00

se. They don't have like a higher uh IQ,

## 23390:00 - 23420:00

so to speak. It's just that they're way

## 23420:00 - 23450:00

better trained, and they're way better

## 23450:00 - 23485:00

trained in in two ways. So, they're not

## 23485:00 - 23505:00

just trying to autocomplete code

## 23505:00 - 23540:00

anymore. They're actually trained via

## 23540:00 - 23585:00

trial and error in these

## 23585:00 - 23610:00

posturing environments with you know

## 23610:00 - 23645:00

true reward signals and also they're

## 23645:00 - 23695:00

trained uh to embed this uh model of

## 23695:00 - 23730:00

code execution right where they they

## 23730:00 - 23775:00

they they learn to keep track of the

## 23775:00 - 23815:00

value of variables uh uh over an

## 23815:00 - 23850:00

execution cycle and that's what what's

## 23850:00 - 23875:00

leading to this extremely strong product

## 23875:00 - 23915:00

market fit of agency coding today and

## 23915:00 - 23940:00

it's really it's completely changing

## 23940:00 - 23955:00

software engineering

## 23955:00 - 23990:00

>> this happened not too long ago the

## 23990:00 - 24040:00

saturation we actually at the founders

## 24040:00 - 24095:00

of poetic that came and spoke about the

## 24095:00 - 24110:00

approach

## 24110:00 - 24150:00

>> which is really sounds like this new way

## 24150:00 - 24190:00

of uh getting LM to perform is building

## 24190:00 - 24230:00

this agent hardness right and the

## 24230:00 - 24265:00

hardness is basically structuring a

## 24265:00 - 24315:00

problem domain into something that can

## 24315:00 - 24350:00

be formally verified and they did that

## 24350:00 - 24410:00

basically for ARC v2 which when they

## 24410:00 - 24440:00

released it they were at the top of the

## 24440:00 - 24470:00

benchmark but then the crazy thing is I

## 24470:00 - 24495:00

actually worked with a company in the

## 24495:00 - 24540:00

winter 26 batch not too long ago called

## 24540:00 - 24575:00

Confluence Labs which actually ended up

## 24575:00 - 24640:00

saturating the V2 results with 97% and I

## 24640:00 - 24675:00

think their task cost was uh a lot more

## 24675:00 - 24710:00

efficient too and the approach they

## 24710:00 - 24745:00

basically took is similar to this. I

## 24745:00 - 24785:00

think they built the harnesses on top of

## 24785:00 - 24860:00

it in order to get the LMS to to go and

## 24860:00 - 24905:00

build different tasks and program

## 24905:00 - 24920:00

through it.

## 24920:00 - 24965:00

>> Yeah. which then for me I was like wow

## 24965:00 - 24995:00

is this batch and during the batch they

## 24995:00 - 25040:00

only worked on it for a couple of months

## 25040:00 - 25065:00

and they were able to saturate this

## 25065:00 - 25090:00

batch that has been around for a long

## 25090:00 - 25115:00

time. It's like something special is

## 25115:00 - 25125:00

happening.

## 25125:00 - 25145:00

>> Yeah. Yeah. There's a lot of progress

## 25145:00 - 25185:00

right now. It's driven by a custom

## 25185:00 - 25220:00

harnesses around the task and the

## 25220:00 - 25260:00

harness is basically a way for the the

## 25260:00 - 25315:00

human programmer to um input into the

## 25315:00 - 25365:00

model like higher level like uh solution

## 25365:00 - 25405:00

strategies basically. I mean to me the

## 25405:00 - 25440:00

fact that you need humans to engineer

## 25440:00 - 25485:00

these harnesses is also a sign that

## 25485:00 - 25525:00

we're we're short of AGI today because

## 25525:00 - 25555:00

if we had AGI you know AI would just

## 25555:00 - 25580:00

make its own harness it would not need

## 25580:00 - 25610:00

to be told how to solve a problem it

## 25610:00 - 25650:00

will just figure it out but it is very

## 25650:00 - 25675:00

effective like harnesses I don't think

## 25675:00 - 25720:00

they get us closer to AGI in any sense

## 25720:00 - 25750:00

but it's a very valuable area of

## 25750:00 - 25790:00

research because that can lead to task

## 25790:00 - 25815:00

automation at scale

## 25815:00 - 25855:00

>> YC's next batch is now taking

## 25855:00 - 25905:00

applications got a startup in Apply at y

## 25905:00 - 25940:00

combinator.com/apply.

## 25940:00 - 25980:00

It's never too early and filling out the

## 25980:00 - 26025:00

app will level up your idea. Okay, back

## 26025:00 - 26045:00

to the video.

## 26045:00 - 26085:00

>> Can you tell us about then what V3 is

## 26085:00 - 26125:00

going to measure that's uh just got

## 26125:00 - 26140:00

released?

## 26140:00 - 26175:00

>> Yeah, absolutely. So, if you look at V1,

## 26175:00 - 26220:00

V2, uh it was really focusing on your

## 26220:00 - 26295:00

ability to uh produce like causal models

## 26295:00 - 26325:00

uh of a pattern that was just given to

## 26325:00 - 26360:00

you like the data was given to you. Uh

## 26360:00 - 26405:00

so it was static, it was uh passive and

## 26405:00 - 26480:00

really focused on uh modeling and uh v3

## 26480:00 - 26505:00

is completely different. We are trying

## 26505:00 - 26555:00

to measure uh agentic intelligence. So

## 26555:00 - 26595:00

it's interactive, it's active like the

## 26595:00 - 26630:00

data is not provided to you. You must go

## 26630:00 - 26670:00

get it. The idea is that your agent is

## 26670:00 - 26715:00

dropped into a new environment which is

## 26715:00 - 26755:00

kind of like a a mini video game. And

## 26755:00 - 26800:00

it's not provided any instructions. It's

## 26800:00 - 26840:00

not told what to do. it's not told uh

## 26840:00 - 26875:00

what the goal even is or what the

## 26875:00 - 26925:00

controls even are and it must figure out

## 26925:00 - 26970:00

everything on its own via trial and

## 26970:00 - 27010:00

error. So we are we are not just uh

## 27010:00 - 27055:00

measuring you know the uh the AI's

## 27055:00 - 27100:00

ability to model its environment we're

## 27100:00 - 27140:00

also looking at uh its exploration

## 27140:00 - 27180:00

efficiency its ability to acquire goals

## 27180:00 - 27220:00

on its own like goal setting and of

## 27220:00 - 27270:00

course its ability to plan uh through

## 27270:00 - 27295:00

the model of the environment that's

## 27295:00 - 27340:00

created and and to execute the plan. Uh

## 27340:00 - 27370:00

and so together, you know, all all of

## 27370:00 - 27405:00

these abilities, we call that agentic

## 27405:00 - 27455:00

intelligence. And we are looking for AI

## 27455:00 - 27495:00

systems that could learn to play these

## 27495:00 - 27530:00

games and and you know, crack them with

## 27530:00 - 27575:00

the same degree of action efficiency as

## 27575:00 - 27610:00

a human. If you look at the human, they

## 27610:00 - 27630:00

are dropped into this new environment.

## 27630:00 - 27660:00

They they try a few things. They start

## 27660:00 - 27700:00

understanding how things work. Uh they

## 27700:00 - 27725:00

can they can solve the environment, you

## 27725:00 - 27765:00

know, in in a few hundreds to thousands

## 27765:00 - 27795:00

factions. We're trying to look for AI

## 27795:00 - 27825:00

systems that could match uh this

## 27825:00 - 27860:00

efficiency. And by the way, we know that

## 27860:00 - 27905:00

all of these test environments in R3 are

## 27905:00 - 27935:00

solvable by humans with no prior

## 27935:00 - 27975:00

training because we actually uh tested

## 27975:00 - 28020:00

them uh on on regular people. Yeah. At

## 28020:00 - 28065:00

first, you just see this screen and you

## 28065:00 - 28090:00

you know you have these keys available,

## 28090:00 - 28120:00

but you don't know what they do and you

## 28120:00 - 28165:00

must figure out everything from scratch.

## 28165:00 - 28195:00

And humans are really good at that by

## 28195:00 - 28210:00

the way. They're really good at

## 28210:00 - 28260:00

exploring efficiently at making sense of

## 28260:00 - 28290:00

something new and eventually cracking

## 28290:00 - 28330:00

the game. And frontier models today,

## 28330:00 - 28360:00

they're not very good at it. If the

## 28360:00 - 28415:00

reasoning models cracked V1 and the like

## 28415:00 - 28435:00

reinforcement learning environments

## 28435:00 - 28495:00

cracked V2, did do we need a new advance

## 28495:00 - 28535:00

to crack V3? Did the did do even the

## 28535:00 - 28570:00

best techniques currently like not work?

## 28570:00 - 28605:00

>> Yeah, I mean, I'm pretty curious to see

## 28605:00 - 28645:00

how Frontier Labs are going to react to

## 28645:00 - 28670:00

V3 and how they're going to start to

## 28670:00 - 28720:00

target it. um it is designed to be more

## 28720:00 - 28760:00

resistant uh to the same kind of

## 28760:00 - 28795:00

darkness strategy as what we saw for V2

## 28795:00 - 28825:00

in particular. Like of course you can

## 28825:00 - 28895:00

try to just make more AR3 like games and

## 28895:00 - 28965:00

then train your agents uh in them. Um

## 28965:00 - 29010:00

but the thing is we've uh deliberately

## 29010:00 - 29060:00

tried to create a private set of

## 29060:00 - 29090:00

environments that is significantly

## 29090:00 - 29120:00

different from the public set like you

## 29120:00 - 29145:00

can look at the public set. actually

## 29145:00 - 29175:00

giving you that much information about

## 29175:00 - 29195:00

what's in the private set.

## 29195:00 - 29230:00

>> Uh in the private set you will have very

## 29230:00 - 29255:00

different games with very different

## 29255:00 - 29275:00

concepts

## 29275:00 - 29315:00

>> and also the public set is meant to be

## 29315:00 - 29360:00

substantially easier performance on the

## 29360:00 - 29385:00

public set is not actually it's not

## 29385:00 - 29415:00

representative of how well the system

## 29415:00 - 29445:00

would prioritize. So for this reason

## 29445:00 - 29475:00

it's going to be harder to target

## 29475:00 - 29510:00

>> and that makes it a better test of fluid

## 29510:00 - 29545:00

intelligence as opposed to a test of how

## 29545:00 - 29580:00

much effort you put into into cracking

## 29580:00 - 29590:00

it.

## 29590:00 - 29615:00

>> I'm so curious how do you come up with

## 29615:00 - 29645:00

these games? They're so creative.

## 29645:00 - 29700:00

>> Yeah, we set up an entire uh video game

## 29700:00 - 29740:00

studio, right, to to create them. Uh so

## 29740:00 - 29795:00

we got over 250 games. Uh and you know,

## 29795:00 - 29825:00

they they're pretty quick to play. Like

## 29825:00 - 29860:00

each game takes you maybe 10 minutes or

## 29860:00 - 29900:00

or or a bit less uh uh to play from

## 29900:00 - 29940:00

scratch, like upon first contact. And we

## 29940:00 - 29990:00

have like 250 plus. And uh we set up

## 29990:00 - 30030:00

this uh very productive game studio

## 30030:00 - 30070:00

where we had any given week we had

## 30070:00 - 30110:00

multiple games uh in progress. We're

## 30110:00 - 30150:00

like this this pipeline uh including you

## 30150:00 - 30195:00

know design implementation uh review

## 30195:00 - 30240:00

human testing and and and many many

## 30240:00 - 30280:00

iteration cycles to to to make sure that

## 30280:00 - 30315:00

the the game comes out right. Who who's

## 30315:00 - 30345:00

working in the studio?

## 30345:00 - 30400:00

>> Right. Uh we yeah we hired a team of

## 30400:00 - 30425:00

game developers and we built our own

## 30425:00 - 30445:00

game engine.

## 30445:00 - 30470:00

>> Wow. So so it's actually people who like

## 30470:00 - 30510:00

previously worked in the game in the in

## 30510:00 - 30540:00

the video game industry.

## 30540:00 - 30565:00

>> That's right. That's right. So, one

## 30565:00 - 30590:00

thing to keep in mind though is that the

## 30590:00 - 30630:00

games in Oxy are unique, right? They're

## 30630:00 - 30670:00

they're trying to not borrow elements,

## 30670:00 - 30715:00

concepts from previous video games. Uh

## 30715:00 - 30755:00

they're built entirely on top of core

## 30755:00 - 30800:00

knowledge prior like things like just

## 30800:00 - 30840:00

just you know elementary knowledge like

## 30840:00 - 30875:00

basic physics uh understanding of

## 30875:00 - 30915:00

objects uh understanding of the notion

## 30915:00 - 30965:00

of agents for instance like an agent in

## 30965:00 - 31015:00

objects with goals and int intentions.

## 31015:00 - 31055:00

Um but we we're not incorporating any

## 31055:00 - 31105:00

language any like cultural symbols like

## 31105:00 - 31150:00

you know arrows for instance uh or the

## 31150:00 - 31185:00

color green meaning go and color red

## 31185:00 - 31215:00

meaning star that sort of thing. Uh

## 31215:00 - 31250:00

there's no external knowledge that's

## 31250:00 - 31280:00

involved uh in these games.

## 31280:00 - 31310:00

>> It's like one of those uh IQ tests that

## 31310:00 - 31330:00

are just pattern matching but now it has

## 31330:00 - 31345:00

time series.

## 31345:00 - 31385:00

>> Yeah. Uh it's not just time series it's

## 31385:00 - 31445:00

interactive. must create your own path

## 31445:00 - 31500:00

through game space, right? You you must

## 31500:00 - 31555:00

>> you know in in in an acutest like

## 31555:00 - 31585:00

problem like you know what ARK one and

## 31585:00 - 31645:00

two is the data that you must model is

## 31645:00 - 31675:00

provided to you. You already have the

## 31675:00 - 31705:00

data you just you just need to find the

## 31705:00 - 31750:00

causal rule to explain it with AR3

## 31750:00 - 31785:00

actually must gather the data

## 31785:00 - 31820:00

>> uh and you must do so efficiently. Like

## 31820:00 - 31840:00

of course you could say well I'm just

## 31840:00 - 31875:00

going to you know brute force mine uh

## 31875:00 - 31920:00

the space of every possible game state

## 31920:00 - 31955:00

and then I find the solution. You cannot

## 31955:00 - 31985:00

do that because if you try to do that

## 31985:00 - 32010:00

you would score extremely low even if

## 32010:00 - 32045:00

you manage to solve the level uh because

## 32045:00 - 32075:00

you're scored on your efficiency. You

## 32075:00 - 32110:00

must match human level efficiency.

## 32110:00 - 32145:00

>> It's funny it's like almost coming full

## 32145:00 - 32185:00

circle. This level of AGI

## 32185:00 - 32230:00

with games sort of is the match pair to

## 32230:00 - 32275:00

open AI writing. I mean, you know, Tom

## 32275:00 - 32305:00

Brown, uh, one of the co-founders of

## 32305:00 - 32340:00

Anthropic, had to write like the harness

## 32340:00 - 32405:00

code to allow like the, you know, preGPT

## 32405:00 - 32455:00

AI at OpenAI to play Starcraft.

## 32455:00 - 32500:00

>> Yeah. Yeah. OpenAI worked on on uh in

## 32500:00 - 32550:00

part on on Dota 2. uh they had the

## 32550:00 - 32585:00

openi5 model which was if I recall

## 32585:00 - 32635:00

correctly. So this was like not just pre

## 32635:00 - 32695:00

GPD but also mostly pre transformers

## 32695:00 - 32720:00

because they were working with a stack

## 32720:00 - 32745:00

of LSTM

## 32745:00 - 32775:00

>> uh layers if I recall correctly and even

## 32775:00 - 32830:00

before open pony uh deep mine worked a

## 32830:00 - 32870:00

lot on video game uh uh you know solving

## 32870:00 - 32915:00

video games via deep aisle uh and they

## 32915:00 - 32960:00

were the first to do uh Atari games

## 32960:00 - 33005:00

right back in 2013 that you know they

## 33005:00 - 33035:00

were very very early very very visionary

## 33035:00 - 33070:00

in that sense to to work on on this

## 33070:00 - 33110:00

problem so early with methods which are

## 33110:00 - 33145:00

still very modern methods. So the big

## 33145:00 - 33195:00

difference is that if you look at um at

## 33195:00 - 33265:00

games for instance you're training uh on

## 33265:00 - 33305:00

on the same environment as what you use

## 33305:00 - 33350:00

for testing. So effectively you're just

## 33350:00 - 33410:00

trying to memorize the best strategies.

## 33410:00 - 33465:00

you're trying to uh at at training time

## 33465:00 - 33510:00

explore the full uh space of possible

## 33510:00 - 33570:00

game states and productionize

## 33570:00 - 33595:00

operationalize

## 33595:00 - 33635:00

uh that knowledge into into into the

## 33635:00 - 33665:00

model and then at inference time you're

## 33665:00 - 33700:00

basically just recalling that knowledge

## 33700:00 - 33740:00

and that's explicitly what we're trying

## 33740:00 - 33800:00

to avoid with AR 3. Uh you're not

## 33800:00 - 33835:00

playing games uh that you've seen

## 33835:00 - 33860:00

before. You're not playing games that

## 33860:00 - 33895:00

you've been trained on like for millions

## 33895:00 - 33935:00

of files. Like the OpenI5 model for

## 33935:00 - 33975:00

instance was playing a restricted

## 33975:00 - 34020:00

version of Dota 2 and it was trained on

## 34020:00 - 34055:00

like tens of thousands of hours of

## 34055:00 - 34085:00

gameplay effectively. I think maybe in

## 34085:00 - 34120:00

millions just an insane amount of

## 34120:00 - 34160:00

training data. With AR 3, you're being

## 34160:00 - 34185:00

evaluated on games that you're seeing

## 34185:00 - 34230:00

for the very first time and every action

## 34230:00 - 34285:00

you spend exploring is counted towards

## 34285:00 - 34325:00

your efficiency score. Right? So you're

## 34325:00 - 34360:00

really focused on measuring fluid

## 34360:00 - 34380:00

intelligence, your ability to

## 34380:00 - 34425:00

efficiently explore, efficiently produce

## 34425:00 - 34475:00

a world model uh of the environment and

## 34475:00 - 34535:00

then use this model uh to infer goals uh

## 34535:00 - 34575:00

plan towards these goals uh and and

## 34575:00 - 34605:00

eventually crack the game. One of the

## 34605:00 - 34660:00

arguments for um you know India is that

## 34660:00 - 34695:00

you're able to do all of the intelligent

## 34695:00 - 34730:00

tasks for you know an arc task might be

## 34730:00 - 34770:00

like.3

## 34770:00 - 34810:00

you know cents for an arc task but you

## 34810:00 - 34850:00

know for the same task on a foundation

## 34850:00 - 34880:00

model with LLMs it's you know a dollar

## 34880:00 - 34925:00

to $10 and then there's this other

## 34925:00 - 34960:00

aspect that we've been tracking where it

## 34960:00 - 35020:00

seems like uh more and more intelligence

## 35020:00 - 35070:00

um at least on the LLM side uh can be

## 35070:00 - 35110:00

distilled down into smaller and smaller

## 35110:00 - 35155:00

models. And so on the one hand like

## 35155:00 - 35185:00

they're scaling up but then they're like

## 35185:00 - 35225:00

distilling smarter and smarter small

## 35225:00 - 35270:00

models. I guess your approach might

## 35270:00 - 35305:00

indicate that it's not billions of

## 35305:00 - 35355:00

parameters like the you know achieving

## 35355:00 - 35415:00

AGI might not be you know sort of

## 35415:00 - 35450:00

inherently a scale thing at all. There's

## 35450:00 - 35495:00

a platonic ideal of the NDIA model that

## 35495:00 - 35525:00

achieves AGI.

## 35525:00 - 35530:00

>> Yeah. Yeah.

## 35530:00 - 35550:00

>> Do you ever think about it in terms of

## 35550:00 - 35590:00

like well it would fit on a floppy disc?

## 35590:00 - 35615:00

>> Well, okay. There there are two things

## 35615:00 - 35645:00

to separate. There's the sort of like

## 35645:00 - 35680:00

fluid intelligence engine.

## 35680:00 - 35705:00

>> I think it's going to be a very very

## 35705:00 - 35755:00

small code base uh and a very small set

## 35755:00 - 35805:00

of models associated with it and it's

## 35805:00 - 35835:00

probably going to be on the order of

## 35835:00 - 35875:00

megabytes, right? And then you have the

## 35875:00 - 35925:00

knowledge base so to speak uh that's

## 35925:00 - 35980:00

going to be uh layered below this this

## 35980:00 - 36020:00

fluid intelligence engine like you know

## 36020:00 - 36055:00

fluid intelligence has to draw on some

## 36055:00 - 36085:00

knowledge and that knowledge is going to

## 36085:00 - 36120:00

take up a lot more space. I think it's

## 36120:00 - 36150:00

it's it's important to to differentiate

## 36150:00 - 36185:00

the two. I do believe that you know when

## 36185:00 - 36230:00

we create a GI retrospectively it will

## 36230:00 - 36275:00

turn out that it's a code base that's

## 36275:00 - 36310:00

less than 10,000 lines of code

## 36310:00 - 36360:00

>> and that if you had if you had known

## 36360:00 - 36410:00

about it back in the in the 1980s you

## 36410:00 - 36445:00

could have done AGI back then using the

## 36445:00 - 36470:00

comput resources available back then

## 36470:00 - 36490:00

>> wow that's a crazy prediction

## 36490:00 - 36525:00

>> that's I I think retrospectively this

## 36525:00 - 36555:00

will turn out to be to be true.

## 36555:00 - 36580:00

>> Wow. So it was just like hiding under

## 36580:00 - 36605:00

our noses in plain sight for like 40

## 36605:00 - 36635:00

years. It took us like 40 years to

## 36635:00 - 36645:00

figure it out.

## 36645:00 - 36655:00

>> That's right. That's right.

## 36655:00 - 36680:00

>> Well, that second thing sounds like

## 36680:00 - 36725:00

Douglas Lenat's like psych project. Or

## 36725:00 - 36745:00

is that the wrong way to think about it?

## 36745:00 - 36775:00

It's like there's sort of knowledge

## 36775:00 - 36800:00

about the world

## 36800:00 - 36830:00

>> and then there's methods like the

## 36830:00 - 36875:00

program what I hear is like the program

## 36875:00 - 36910:00

might be 10,000 lines and then it

## 36910:00 - 36925:00

operates on like

## 36925:00 - 36955:00

>> on knowledge base that's very large. So

## 36955:00 - 36995:00

the problem with psych uh I mean there

## 36995:00 - 37020:00

were many issues with it but one of the

## 37020:00 - 37055:00

big issues is that uh there was no

## 37055:00 - 37080:00

learning involved.

## 37080:00 - 37105:00

>> Yeah. It's just the knowledge like

## 37105:00 - 37125:00

>> the knowledge wasn't crafted.

## 37125:00 - 37150:00

>> It's like purely symbolic knowledge and

## 37150:00 - 37175:00

it was probably inaccurate.

## 37175:00 - 37220:00

>> The way you want to be building a GI is

## 37220:00 - 37270:00

that you want to be removing humans uh

## 37270:00 - 37305:00

from from the improvement loop as much

## 37305:00 - 37325:00

as possible. You don't want a system

## 37325:00 - 37370:00

where every improvement in system

## 37370:00 - 37410:00

capability has to involve a human

## 37410:00 - 37445:00

engineer doing something. And it's

## 37445:00 - 37475:00

actually the strength uh of deep

## 37475:00 - 37520:00

learning and foundation models is that

## 37520:00 - 37545:00

you can just scale up the knowledge

## 37545:00 - 37570:00

base. Like an LLM is effectively

## 37570:00 - 37620:00

knowledge base. It's a bank uh of uh of

## 37620:00 - 37665:00

you know modular uh vector programs that

## 37665:00 - 37705:00

map patterns of input tokens to patterns

## 37705:00 - 37735:00

of output tokens. And you can you can

## 37735:00 - 37755:00

scale up that knowledge base by just

## 37755:00 - 37795:00

adding training data and training

## 37795:00 - 37830:00

compute with no further human

## 37830:00 - 37850:00

involvement. I mean, of course, there's

## 37850:00 - 37880:00

still a little bit of human involvement

## 37880:00 - 37905:00

in in making sure the train job

## 37905:00 - 37945:00

completes, but it's it's minor. You've

## 37945:00 - 37990:00

managed to remove humans uh from this

## 37990:00 - 38020:00

improvement as much as possible. And

## 38020:00 - 38055:00

that's also uh what we want for our

## 38055:00 - 38085:00

system. We want a system that's uh

## 38085:00 - 38125:00

self-improving where the improvements

## 38125:00 - 38165:00

are compounding, meaning that every time

## 38165:00 - 38205:00

the system increases capabilities, it's

## 38205:00 - 38235:00

also increasing the rate at which it

## 38235:00 - 38260:00

increases its capabilities.

## 38260:00 - 38290:00

>> I think this is a PGism. It's like, I'm

## 38290:00 - 38340:00

sorry the essay is so long. uh if I had

## 38340:00 - 38370:00

more time I would make it shorter.

## 38370:00 - 38400:00

>> Yeah. When you're looking at at a hard

## 38400:00 - 38455:00

problem it's actually harder to produce

## 38455:00 - 38500:00

a short elegant concise solution than a

## 38500:00 - 38530:00

messy overengineered solution.

## 38530:00 - 38555:00

>> Yeah, you can brute force it but you

## 38555:00 - 38585:00

know the more elegant version is very

## 38585:00 - 38620:00

very short and that's kind of like what

## 38620:00 - 38660:00

you said with how this might come about.

## 38660:00 - 38690:00

This is this is yeah this is literally

## 38690:00 - 38745:00

the shape of the type of AI approach uh

## 38745:00 - 38775:00

we are creating and I think this is also

## 38775:00 - 38845:00

the shape uh of science itself like

## 38845:00 - 38900:00

science is fundamentally a a symbolic

## 38900:00 - 38940:00

compression process where you're looking

## 38940:00 - 38995:00

at a big mess of observations like you

## 38995:00 - 39020:00

know the the position of planets in the

## 39020:00 - 39045:00

sky or something like that and you're

## 39045:00 - 39105:00

compressing that down to uh a very

## 39105:00 - 39140:00

simple symbolic rule. You're saying like

## 39140:00 - 39185:00

yeah like all these you know thousands

## 39185:00 - 39220:00

of observations actually just all uh

## 39220:00 - 39250:00

this one simple equation that's symbolic

## 39250:00 - 39290:00

compression and to do this by the way uh

## 39290:00 - 39340:00

you need the model uh to be symbolic

## 39340:00 - 39380:00

like you you could not fit a curve and

## 39380:00 - 39410:00

say well you know that that curve is my

## 39410:00 - 39445:00

model that would never be optimal it

## 39445:00 - 39485:00

would never be concise or elegant enough

## 39485:00 - 39505:00

and that's not what science is doing.

## 39505:00 - 39535:00

Science is not about curve fitting.

## 39535:00 - 39565:00

Science is about finding the equation,

## 39565:00 - 39605:00

finding the most compressive symbolic

## 39605:00 - 39645:00

model of your pile of observation. And

## 39645:00 - 39670:00

that's the process that you're trying to

## 39670:00 - 39705:00

recreate in software form. Like you

## 39705:00 - 39745:00

could say that uh the NDI approach to

## 39745:00 - 39775:00

program synthesis is that we are

## 39775:00 - 39820:00

building science incarnate science the

## 39820:00 - 39855:00

scientific method in in algorithmic

## 39855:00 - 39910:00

form. I'm curious if you compare it to

## 39910:00 - 39965:00

biology. Clearly LMS don't learn the way

## 39965:00 - 39995:00

that humans do cuz no baby reads the

## 39995:00 - 40025:00

whole internet. Do you think program

## 40025:00 - 40060:00

synthesis is closer to the way that

## 40060:00 - 40095:00

humans learn or do you think that's yet

## 40095:00 - 40140:00

a third branch where even if program

## 40140:00 - 40165:00

synthesis is correct there will be some

## 40165:00 - 40200:00

yet as undiscovered third way to do it

## 40200:00 - 40225:00

which is the thing that we do

## 40225:00 - 40285:00

>> I think so uh I do think humans do some

## 40285:00 - 40315:00

amount of program synthesis I think the

## 40315:00 - 40350:00

the way humans learn and the way the the

## 40350:00 - 40395:00

human mind works is very messy it's not

## 40395:00 - 40420:00

like there's one simple elegant

## 40420:00 - 40455:00

principle behind it all it's an

## 40455:00 - 40510:00

implementation of fundamental principles

## 40510:00 - 40535:00

the fundamental principles of of

## 40535:00 - 40565:00

intelligence which you know I think we

## 40565:00 - 40620:00

can identify these principles and

## 40620:00 - 40665:00

reimplement intelligence from scratch

## 40665:00 - 40700:00

from first principles in a way that will

## 40700:00 - 40740:00

be much more efficient than the human

## 40740:00 - 40780:00

brain. I think the human brain is messy

## 40780:00 - 40805:00

and it's it can be a good source of

## 40805:00 - 40850:00

inspiration for AI but I think it would

## 40850:00 - 40900:00

be counterproductive to just try uh to

## 40900:00 - 40930:00

you know observe it and reimplement it

## 40930:00 - 40975:00

like uh and and and make it biologically

## 40975:00 - 41000:00

plausible. Uh I think that's

## 41000:00 - 41020:00

counterpart. That's not what we're

## 41020:00 - 41035:00

trying to do at India. We're really

## 41035:00 - 41065:00

trying to find what are the first

## 41065:00 - 41110:00

principles of intelligence and what is

## 41110:00 - 41150:00

the system that would best implement

## 41150:00 - 41180:00

them. But yeah, I do believe the human

## 41180:00 - 41235:00

mind does at the highest level uh

## 41235:00 - 41255:00

something that looks a lot like

## 41255:00 - 41280:00

programs. It's like we're currently

## 41280:00 - 41320:00

building causal models of our

## 41320:00 - 41350:00

surroundings like we're we're describing

## 41350:00 - 41400:00

our surroundings in our mind as you know

## 41400:00 - 41440:00

a set of objects and agents and and

## 41440:00 - 41485:00

relations uh pin objects uh that are

## 41485:00 - 41530:00

fundamentally symbolic and causal in

## 41530:00 - 41580:00

nature. This is exactly the process that

## 41580:00 - 41640:00

lets us uh generalize so well and adapt

## 41640:00 - 41680:00

so well to novelty on the fly. I'm

## 41680:00 - 41725:00

curious about NDIA the company and as

## 41725:00 - 41765:00

you're as you're building it um we've

## 41765:00 - 41800:00

all here heard of the OpenAI founding

## 41800:00 - 41825:00

story and something that's always struck

## 41825:00 - 41860:00

with me is just like both Sam and Greg

## 41860:00 - 41890:00

say that it was a little odd in the

## 41890:00 - 41910:00

early days cuz you didn't actually know

## 41910:00 - 41950:00

what to do just like bunch of people

## 41950:00 - 41980:00

like hanging out in an apartment. I

## 41980:00 - 42000:00

would love to hear kind of what's that

## 42000:00 - 42025:00

been like for India like what did like

## 42025:00 - 42075:00

the day one look like and just maybe for

## 42075:00 - 42095:00

just people who are interested in

## 42095:00 - 42130:00

starting these alternative approaches

## 42130:00 - 42160:00

who don't have sort of a researchy

## 42160:00 - 42180:00

background how should they think about

## 42180:00 - 42185:00

that

## 42185:00 - 42220:00

>> yeah so we we started on day one with

## 42220:00 - 42255:00

the symbolic learning vision like we

## 42255:00 - 42300:00

basically knew that we wanted to do uh

## 42300:00 - 42325:00

symbolic program synthesis that we

## 42325:00 - 42365:00

wanted to create a new approach to

## 42365:00 - 42400:00

machine learning where you replace

## 42400:00 - 42440:00

parameter curves with the shortest

## 42440:00 - 42470:00

possible symbolic models and And the big

## 42470:00 - 42500:00

question was okay so how do we find

## 42500:00 - 42560:00

these models? We started from uh the the

## 42560:00 - 42590:00

the base idea which is still the idea

## 42590:00 - 42615:00

that we're following today which is that

## 42615:00 - 42670:00

we are doing we are going to do uh deep

## 42670:00 - 42725:00

learning guided program search that you

## 42725:00 - 42760:00

have a a symbolic search space to

## 42760:00 - 42795:00

explore and it's big it's in fact

## 42795:00 - 42825:00

communal you're not going to make

## 42825:00 - 42870:00

progress uh if you just use brute force

## 42870:00 - 42905:00

uh it's not going to scale uh you have

## 42905:00 - 42950:00

to break the comal wall and the way to

## 42950:00 - 42990:00

do it is to add is to add uh deep

## 42990:00 - 43025:00

learning guidance it's actually very

## 43025:00 - 43070:00

similar to uh the principles that end

## 43070:00 - 43105:00

something like alpha or alpha zero. So

## 43105:00 - 43145:00

it was our our starting point. We also

## 43145:00 - 43170:00

you know didn't have very clear ideas

## 43170:00 - 43195:00

about how to how to build it. So we we

## 43195:00 - 43220:00

tried many different things. We tried

## 43220:00 - 43270:00

many many different ideas and um it took

## 43270:00 - 43335:00

us half a year roughly uh to to to get

## 43335:00 - 43380:00

to good foundations uh where we we could

## 43380:00 - 43415:00

start building a system that compounds.

## 43415:00 - 43430:00

And I think that's what's really

## 43430:00 - 43470:00

important uh when when doing a lab like

## 43470:00 - 43490:00

this that you don't want to be in a

## 43490:00 - 43525:00

situation where you're you're constantly

## 43525:00 - 43565:00

trying something new. It's not reusing

## 43565:00 - 43620:00

any learnings, any findings uh from the

## 43620:00 - 43645:00

previous approaches. You want you want a

## 43645:00 - 43685:00

compounding stack. You want to build

## 43685:00 - 43715:00

reusable foundations and then the next

## 43715:00 - 43745:00

layer and then the next layer and the

## 43745:00 - 43785:00

the the and of course you you want to be

## 43785:00 - 43810:00

building onto the right foundation. So

## 43810:00 - 43850:00

don't uh commit to the to the foundation

## 43850:00 - 43885:00

layer too early, but also make sure that

## 43885:00 - 43920:00

at some point you're building this this

## 43920:00 - 43950:00

compounding structure and that that's

## 43950:00 - 43980:00

that's the situation that that we're in

## 43980:00 - 43985:00

now.

## 43985:00 - 44030:00

>> Is ARK 3 the end or will there be an ARK

## 44030:00 - 44070:00

four, five, six? Can you keep making it

## 44070:00 - 44080:00

harder?

## 44080:00 - 44105:00

>> Yeah. Yeah. I think there there will

## 44105:00 - 44140:00

absolutely be ARK 4 and and AR five. I

## 44140:00 - 44185:00

mean, we're currently planning ARK 5. Um

## 44185:00 - 44225:00

the the point of the AKGI benchmark

## 44225:00 - 44260:00

series is not to say that well, you

## 44260:00 - 44295:00

know, here's this test. if you pass it,

## 44295:00 - 44345:00

this is a GI. Um, instead what we're

## 44345:00 - 44370:00

trying to do is we're target we're

## 44370:00 - 44425:00

targeting uh the residual gap of fair

## 44425:00 - 44470:00

capabilities like frontier is advancing

## 44470:00 - 44520:00

and we're saying well uh if you compare

## 44520:00 - 44555:00

it to to to human abilities there

## 44555:00 - 44595:00

there's all these tasks all these things

## 44595:00 - 44625:00

it's now doing well so we're going to

## 44625:00 - 44665:00

create a benchmark to target that. uh

## 44665:00 - 44700:00

and so it's a moving target, right? It's

## 44700:00 - 44720:00

it's not fixed point. It's a moving

## 44720:00 - 44755:00

target. So there will be ARK 4 which

## 44755:00 - 44805:00

will be uh in the spirit of ARK 3 but

## 44805:00 - 44840:00

more focused on continual learning and

## 44840:00 - 44885:00

and curriculum learning at longer time

## 44885:00 - 44910:00

scales. So you're you're going to have

## 44910:00 - 44945:00

fewer games uh but they're going to have

## 44945:00 - 44985:00

way more levels and the levels are going

## 44985:00 - 45020:00

to be compounding meaning that for for

## 45020:00 - 45055:00

each level you need to reuse stuff that

## 45055:00 - 45085:00

you've learned before. Then there's

## 45085:00 - 45115:00

going to be Ark 5. And I'm actually

## 45115:00 - 45135:00

really really excited about Ark 5. It's

## 45135:00 - 45175:00

very very new and different and it's all

## 45175:00 - 45225:00

about invention and I mean you will see

## 45225:00 - 45255:00

you will see what that means. Eventually

## 45255:00 - 45290:00

I expect we will we will run out of

## 45290:00 - 45335:00

things to test like as uh as we get

## 45335:00 - 45385:00

closer to AGI um eventually there will

## 45385:00 - 45430:00

be no measurable difference uh between

## 45430:00 - 45465:00

human capabilities and part human

## 45465:00 - 45515:00

learning efficiency and and frontier AI

## 45515:00 - 45540:00

and when that happens when when it

## 45540:00 - 45565:00

becomes effectively impossible to

## 45565:00 - 45610:00

measure the gap this is the GI moment.

## 45610:00 - 45640:00

Well, then the machines will take over

## 45640:00 - 45690:00

and then they will create ARC ASI one.

## 45690:00 - 45700:00

>> Yes. ARS

## 45700:00 - 45730:00

>> and then it'll continue from there.

## 45730:00 - 45735:00

Yeah.

## 45735:00 - 45780:00

>> Yeah. If you had to put a guess, I mean

## 45780:00 - 45840:00

years, decades, months.

## 45840:00 - 45895:00

uh my timeline to AGR, you know, if you

## 45895:00 - 45935:00

if you just try to to extrapolate from

## 45935:00 - 45985:00

the the current rate of progress and the

## 45985:00 - 46020:00

amount of investment that's going into

## 46020:00 - 46080:00

not just the LLM stack, but also like uh

## 46080:00 - 46120:00

side ideas, side bets that might work

## 46120:00 - 46160:00

out like you know, NDI for instance, I

## 46160:00 - 46200:00

think we're probably looking at AGI

## 46200:00 - 46225:00

2030,

## 46225:00 - 46295:00

early 2030s uh most likely. So around

## 46295:00 - 46330:00

the time uh that you are going to be

## 46330:00 - 46395:00

releasing like maybe AR 6 or AR 7 uh

## 46395:00 - 46425:00

that's probably going to be a GI.

## 46425:00 - 46465:00

>> You guys are doing a different approach

## 46465:00 - 46515:00

to LLM. Um do you think there's room for

## 46515:00 - 46550:00

more startups to explore other new

## 46550:00 - 46575:00

approaches and are there any other ones

## 46575:00 - 46605:00

that you think are promising but don't

## 46605:00 - 46630:00

have time to explore yourself?

## 46630:00 - 46655:00

>> Yeah, absolutely. I mean there are many

## 46655:00 - 46700:00

different approaches that you could try.

## 46700:00 - 46725:00

I've said like compute is is a great

## 46725:00 - 46765:00

equalizer. I think if you look at the

## 46765:00 - 46790:00

amount of comput and resources that

## 46790:00 - 46850:00

we've thrown at uh deep learning and and

## 46850:00 - 46895:00

gradient descent and and scaling that up

## 46895:00 - 46925:00

if you had thrown the same amount of

## 46925:00 - 46980:00

investment into almost anything else you

## 46980:00 - 47010:00

would also have seen extremely exciting

## 47010:00 - 47045:00

results like genetic algorithms for

## 47045:00 - 47080:00

instance uh if you try to scale up

## 47080:00 - 47105:00

genetic algorithms I mean I'm sure you

## 47105:00 - 47145:00

can do incredible things with that um

## 47145:00 - 47175:00

you could in fact probably do new

## 47175:00 - 47220:00

science uh because uh that's based on

## 47220:00 - 47250:00

search and search is the is is the best

## 47250:00 - 47290:00

fit for uh automating the scientific

## 47290:00 - 47340:00

method. uh I think so right now there's

## 47340:00 - 47380:00

also like approaches that uh build on

## 47380:00 - 47405:00

top of the current stack with their

## 47405:00 - 47445:00

slightly alternative like uh state space

## 47445:00 - 47490:00

models for instance uh there's the the

## 47490:00 - 47525:00

XLSM architecture like you you can

## 47525:00 - 47565:00

basically you know current frontier is

## 47565:00 - 47605:00

it's it's a stack of things and you you

## 47605:00 - 47640:00

can take any layer in the stack and try

## 47640:00 - 47670:00

to propose an alternative like if you

## 47670:00 - 47710:00

propose an alternative architecture uh

## 47710:00 - 47740:00

you can be doing for instance like yeah

## 47740:00 - 47770:00

like more like uh recurrent models

## 47770:00 - 47805:00

instead of transformers uh for for the

## 47805:00 - 47850:00

architecture. Uh or you can do even

## 47850:00 - 47875:00

lower level. You're going to be like,

## 47875:00 - 47920:00

okay, we're still going to be training

## 47920:00 - 47945:00

uh parametric curves, but you're going

## 47945:00 - 47970:00

to get rid of cranes descent, right?

## 47970:00 - 48000:00

We're going to use like search. Maybe

## 48000:00 - 48030:00

you're going to do new evolution. Uh

## 48030:00 - 48060:00

that's that's lower level. And the

## 48060:00 - 48110:00

lowest level is uh the the level where

## 48110:00 - 48140:00

where we're operating where we're saying

## 48140:00 - 48190:00

well actually uh forget about curves uh

## 48190:00 - 48220:00

forget about parametric, forget about

## 48220:00 - 48240:00

crown descent. We're just going to do

## 48240:00 - 48285:00

something completely different. Um and I

## 48285:00 - 48330:00

think if you want to build optimal AI,

## 48330:00 - 48375:00

you're kind of forced to go back to the

## 48375:00 - 48410:00

foundation of the stack. It cannot be

## 48410:00 - 48465:00

like uh uh one one layer added on top of

## 48465:00 - 48475:00

the pile.

## 48475:00 - 48510:00

>> So do you think for aspiring researchers

## 48510:00 - 48545:00

to want to do a new neolab with a

## 48545:00 - 48560:00

different approach, they should be

## 48560:00 - 48605:00

reading research papers from the 70s or

## 48605:00 - 48630:00

80s and

## 48630:00 - 48665:00

>> go deeply in those with approaches that

## 48665:00 - 48705:00

were not as invested nowadays. That is

## 48705:00 - 48760:00

actually a great idea because uh earlier

## 48760:00 - 48800:00

in the in the history of the EI research

## 48800:00 - 48840:00

timeline, people were exploring more

## 48840:00 - 48875:00

things and very different things. You've

## 48875:00 - 48910:00

had this sort of like collapse of

## 48910:00 - 48950:00

everything into one approach. It's

## 48950:00 - 48985:00

actually kind of a bad idea. Uh like

## 48985:00 - 49035:00

consider that not too long ago, like

## 49035:00 - 49060:00

about about 20 years ago,

## 49060:00 - 49095:00

>> we had the collapse into SVMs, too.

## 49095:00 - 49135:00

>> Yeah. I mean it wasn't I wouldn't

## 49135:00 - 49160:00

describe it as a collapse because there

## 49160:00 - 49185:00

weren't that many people doing SVMs and

## 49185:00 - 49230:00

AI was a much much uh smaller field back

## 49230:00 - 49295:00

then but there was this uh uh widespread

## 49295:00 - 49335:00

understanding that neural networks were

## 49335:00 - 49375:00

were a failed approach that neuronet

## 49375:00 - 49405:00

networks didn't work and it it was waste

## 49405:00 - 49445:00

of time to to keep trying right

## 49445:00 - 49480:00

>> yeah no even even in the in the in the

## 49480:00 - 49540:00

late 2000s this was a set of things

## 49540:00 - 49595:00

basically like when I got into into AI

## 49595:00 - 49620:00

people are telling me like hey neuronet

## 49620:00 - 49645:00

networks don't try that I was like yeah

## 49645:00 - 49685:00

but it it looks a lot like what the

## 49685:00 - 49715:00

brain is doing like I'm I'm interested

## 49715:00 - 49740:00

in that if everybody is working on

## 49740:00 - 49775:00

something you are discarding ideas that

## 49775:00 - 49815:00

will uh actually turn out to be very

## 49815:00 - 49855:00

productive ideas right and yeah like

## 49855:00 - 49890:00

back in the 70s back in the 80s people

## 49890:00 - 49915:00

are trying more things and I think

## 49915:00 - 49945:00

genetic algorithms actually a very good

## 49945:00 - 50005:00

example of that uh I think this is an

## 50005:00 - 50035:00

approach that has a tremendous amount of

## 50035:00 - 50070:00

potential but there's there's not too

## 50070:00 - 50105:00

many people are looking into scaling it

## 50105:00 - 50130:00

up uh deeply.

## 50130:00 - 50150:00

>> Are there any characteristics that you

## 50150:00 - 50190:00

would be looking for? I mean is it as

## 50190:00 - 50230:00

simple as like if there's a scaling law

## 50230:00 - 50285:00

that could happen then even if it's a

## 50285:00 - 50335:00

different or is it is that too like you

## 50335:00 - 50370:00

know thinking by analogy

## 50370:00 - 50420:00

>> I think you are looking for approaches

## 50420:00 - 50435:00

that scale.

## 50435:00 - 50465:00

>> Yeah. Uh I think it's it's a

## 50465:00 - 50490:00

non-starter. If you're working on

## 50490:00 - 50525:00

something but the only way to increase

## 50525:00 - 50560:00

the capabilities of the system is to

## 50560:00 - 50600:00

have uh human engineers and researchers

## 50600:00 - 50645:00

spend time on it, it will not work

## 50645:00 - 50680:00

because even if the idea is very clever

## 50680:00 - 50720:00

and very elegant and works really well,

## 50720:00 - 50745:00

capabilities are going to be bounded.

## 50745:00 - 50770:00

They're going to be bounded by human

## 50770:00 - 50815:00

investment. Right? You want to be in a

## 50815:00 - 50850:00

setup where the system can improve its

## 50850:00 - 50885:00

capabilities with no human in the loop,

## 50885:00 - 50910:00

with no human.

## 50910:00 - 50940:00

like don't just do it the way we did it

## 50940:00 - 50985:00

like 10 years ago. Do it with the idea

## 50985:00 - 51020:00

that recursive self-improvement is baked

## 51020:00 - 51040:00

in at the beginning.

## 51040:00 - 51065:00

>> Yeah. Not necessarily recursive

## 51065:00 - 51095:00

self-improvement because deep learning

## 51095:00 - 51125:00

for instance not is not recursively

## 51125:00 - 51175:00

self-improving but with the idea of

## 51175:00 - 51220:00

scaling up with no human bottlenecks.

## 51220:00 - 51245:00

You want to remove the human from from

## 51245:00 - 51270:00

the improvement loop. The great strength

## 51270:00 - 51310:00

of deep learning is that the models got

## 51310:00 - 51365:00

better and better simply by adding uh uh

## 51365:00 - 51395:00

training training compute and training

## 51395:00 - 51425:00

data. I mean it's it's a little bit of

## 51425:00 - 51470:00

caricature because of course just adding

## 51470:00 - 51500:00

these factors requires a lot of human

## 51500:00 - 51530:00

involvement but basically that's the

## 51530:00 - 51570:00

idea that you have this decoupling from

## 51570:00 - 51605:00

uh the improvement curve and the amount

## 51605:00 - 51640:00

of human effort that's needed to be

## 51640:00 - 51660:00

injected into the system.

## 51660:00 - 51690:00

>> I guess or human effort that's already

## 51690:00 - 51715:00

happened because the LMS do actually

## 51715:00 - 51735:00

require an enormous amount of human

## 51735:00 - 51755:00

effort. It's just it was the human

## 51755:00 - 51775:00

effort to build the internet and we'd

## 51775:00 - 51790:00

already built it.

## 51790:00 - 51850:00

>> Yeah. Actually less and less now uh that

## 51850:00 - 51890:00

we are doing uh training in interactive

## 51890:00 - 51920:00

verifiable environments

## 51920:00 - 51935:00

>> because then

## 51935:00 - 51965:00

>> you only need a small amount of human

## 51965:00 - 52005:00

effort to create the environment and

## 52005:00 - 52035:00

from that small amount of effort you're

## 52035:00 - 52060:00

you're creating exponentially more

## 52060:00 - 52090:00

training data. But at first I think to

## 52090:00 - 52140:00

sort of like prime the machine you need

## 52140:00 - 52215:00

this tremendous amount uh of uh of uh uh

## 52215:00 - 52250:00

human generated abstractions encoded in

## 52250:00 - 52295:00

text data and if you if you don't start

## 52295:00 - 52335:00

from that you you cannot get the system

## 52335:00 - 52370:00

into this loop. Do you have any advice

## 52370:00 - 52405:00

for me uh starting a open source

## 52405:00 - 52450:00

project? Things to do, things not to do

## 52450:00 - 52540:00

in uh in the AI space because I am uh

## 52540:00 - 52570:00

not sure how I signed up for this in the

## 52570:00 - 52625:00

last 14 days, but I think I have I don't

## 52625:00 - 52665:00

know on the order of like 10 to 30,000

## 52665:00 - 52700:00

people using GStack every day.

## 52700:00 - 52720:00

>> Yeah, it's wild.

## 52720:00 - 52805:00

>> Yeah. And I don't know like I have a job

## 52805:00 - 52830:00

I guess like you know what was it like

## 52830:00 - 52875:00

to start Keras and how did you keep

## 52875:00 - 52895:00

maintaining it? How what's a good

## 52895:00 - 52925:00

maintainer like what did you learn from

## 52925:00 - 52950:00

that? I don't know this might be a whole

## 52950:00 - 52965:00

hour.

## 52965:00 - 53010:00

>> Yeah I mean lots lots of learnings from

## 53010:00 - 53020:00

>> too many things

## 53020:00 - 53060:00

>> from growing growing kas. Uh so right

## 53060:00 - 53095:00

now I'm less involved with it. Uh

## 53095:00 - 53120:00

there's a big team at Google that's

## 53120:00 - 53145:00

working on it and they're doing an

## 53145:00 - 53185:00

amazing job. So it is possible to not

## 53185:00 - 53215:00

you know to put people together to like

## 53215:00 - 53250:00

>> it is possible to start something. It is

## 53250:00 - 53290:00

possible to start something and and and

## 53290:00 - 53320:00

then get more people involved and at

## 53320:00 - 53355:00

some point it becomes its own thing.

## 53355:00 - 53390:00

It's just you know it used to be your

## 53390:00 - 53420:00

baby but now it's all it's all grown up.

## 53420:00 - 53450:00

It's all adult and and and going on with

## 53450:00 - 53495:00

its own life. So if you ask me the the

## 53495:00 - 53535:00

factors that really made car successful

## 53535:00 - 53570:00

um I mean first of all is that there was

## 53570:00 - 53635:00

this big focus on uh making the the API

## 53635:00 - 53670:00

simple and intuitive. There was this big

## 53670:00 - 53710:00

big focus on usability and this was

## 53710:00 - 53755:00

inspired by scikitlearn like scikitlearn

## 53755:00 - 53795:00

was sort of like the og uh machine

## 53795:00 - 53835:00

learning library for python and what

## 53835:00 - 53865:00

made it successful was that it was so

## 53865:00 - 53905:00

easy to get started with it. So at first

## 53905:00 - 53950:00

I was like okay uh I'm going to package

## 53950:00 - 53980:00

uh all this functionality I've created

## 53980:00 - 54015:00

under a really really simple API going

## 54015:00 - 54055:00

to be like the second API that was like

## 54055:00 - 54095:00

the big idea. The focus on usability is

## 54095:00 - 54140:00

not just making sure the API is simple.

## 54140:00 - 54175:00

It's also making sure the entire on

## 54175:00 - 54210:00

boarding experience is nice and easy

## 54210:00 - 54235:00

like the docs should be very

## 54235:00 - 54270:00

informative. You should, you know, the

## 54270:00 - 54325:00

doc should be not just telling you about

## 54325:00 - 54355:00

how to use this thing, but they should

## 54355:00 - 54400:00

actually be teaching you about the

## 54400:00 - 54425:00

domain in the first place because the

## 54425:00 - 54465:00

the folks who land on your website,

## 54465:00 - 54490:00

they're not going to be already deep

## 54490:00 - 54505:00

learning experts. They're going to be

## 54505:00 - 54545:00

people looking to maybe start using deep

## 54545:00 - 54570:00

learning. And so you you have to teach

## 54570:00 - 54610:00

them not just how to use the tool, but

## 54610:00 - 54660:00

what the tool is good for um and and the

## 54660:00 - 54695:00

entire field around it. And then uh you

## 54695:00 - 54720:00

know you have to put a lot of investment

## 54720:00 - 54775:00

into community building. Um one thing we

## 54775:00 - 54815:00

uh we did a bit at Google in fact you

## 54815:00 - 54835:00

know Google made it kind kind of

## 54835:00 - 54870:00

difficult and and I was sad about that

## 54870:00 - 54925:00

is uh hire your power users

## 54925:00 - 54955:00

>> like hire your fans. This this is a

## 54955:00 - 54995:00

really really good idea like find find

## 54995:00 - 55050:00

the the most enthusiastic users from

## 55050:00 - 55095:00

your community and and and just hire

## 55095:00 - 55105:00

them on your team.

## 55105:00 - 55115:00

>> Amazing.

## 55115:00 - 55170:00

>> Yeah. and uh these are the always the

## 55170:00 - 55185:00

best people, right?

## 55185:00 - 55230:00

>> All right, time to start gstack.org. Uh

## 55230:00 - 55255:00

put in a bunch of my own money and then

## 55255:00 - 55285:00

hire a bunch of people to work on it.

## 55285:00 - 55315:00

That sounds good. I think you've been a

## 55315:00 - 55355:00

leader in pioneer and we're so lucky to

## 55355:00 - 55390:00

have you sit with us. There are people

## 55390:00 - 55425:00

watching who are at the beginning of

## 55425:00 - 55460:00

their, you know, adulthood even like

## 55460:00 - 55495:00

their certainly their professional

## 55495:00 - 55540:00

careers uh or actually like people just

## 55540:00 - 55560:00

around the world. They're like trying to

## 55560:00 - 55605:00

understand like what does this mean as

## 55605:00 - 55655:00

intelligence becomes broadly applicable

## 55655:00 - 55700:00

like what would you tell you know if you

## 55700:00 - 55730:00

were 18 right now what would you tell

## 55730:00 - 55740:00

them

## 55740:00 - 55780:00

>> yeah I mean there's a lot of people

## 55780:00 - 55830:00

today who are very uh pessimistic very

## 55830:00 - 55875:00

negative takes about the the rise in the

## 55875:00 - 55910:00

capabilities they say oh you know uh I'm

## 55910:00 - 55950:00

going to be out of a job soon uh there's

## 55950:00 - 55985:00

going to be mass unemployment uh AI is

## 55985:00 - 56035:00

just going to take over completely and

## 56035:00 - 56070:00

my my tech is actually you know the more

## 56070:00 - 56105:00

you know the more expertise you have but

## 56105:00 - 56140:00

things like programming for instance the

## 56140:00 - 56195:00

better you're able to use and leverage

## 56195:00 - 56245:00

these tools for your own benefit and

## 56245:00 - 56285:00

with the right kind of expertise uh all

## 56285:00 - 56325:00

this AI progress is actually empowerment

## 56325:00 - 56350:00

like it's something that you can

## 56350:00 - 56380:00

leverage for yourself I mean that's

## 56380:00 - 56405:00

that's exactly what you did with your

## 56405:00 - 56420:00

project right

## 56420:00 - 56445:00

>> and yeah more people should have this

## 56445:00 - 56490:00

mindset of trying to learn as much as

## 56490:00 - 56545:00

possible not just about AI uh but about

## 56545:00 - 56585:00

the the domain that they want uh uh to

## 56585:00 - 56630:00

apply AI to, right? So that they should

## 56630:00 - 56690:00

they should seek to turn this uh uh this

## 56690:00 - 56725:00

this new development into an opportunity

## 56725:00 - 56750:00

into into a tool they can use for

## 56750:00 - 56785:00

themselves to improve their own lives. I

## 56785:00 - 56805:00

think that's that's the right mindset

## 56805:00 - 56835:00

because you know you're not going to

## 56835:00 - 56875:00

stop uh AI progress. I think I think

## 56875:00 - 56910:00

it's too late for that. And so the next

## 56910:00 - 56940:00

question is okay like AI progress is

## 56940:00 - 56970:00

here. Uh it's actually going to keep

## 56970:00 - 57005:00

accelerating. How do you make use of it?

## 57005:00 - 57025:00

How do you leverage? How do you ride a

## 57025:00 - 57060:00

wave? That's the question to ask.

## 57060:00 - 57085:00

>> I wish we could uh keep going for a

## 57085:00 - 57115:00

couple hours cuz I'm sure we could.

## 57115:00 - 57145:00

Francois, thank you so much for spending

## 57145:00 - 57160:00

time with us.

## 57160:00+

>> Thanks so much for having me.

