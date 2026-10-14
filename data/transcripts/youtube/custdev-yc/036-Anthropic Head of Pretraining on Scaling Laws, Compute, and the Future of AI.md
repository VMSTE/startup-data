---
source: https://www.youtube.com/watch?v=YFeb3yAxtjE
title: Anthropic Head of Pretraining on Scaling Laws, Compute, and the Future of AI
author: Y Combinator
date: 2025-09-30
views: 28922
description: >-
  Ever wonder what it actually takes to train a frontier AI model?


  Ankit Gupta, YC General Partner, sits down with Nick Joseph, Anthropic's Head
  of Pre-training, to explore the engineering challenges behind training
  Claude—from managing thousands of GPUs and debugging cursed bugs to balancing
  compute between pre-training and RL. We cover scaling laws, data strategies,
  team composition, and why the hardest problems in AI are often infrastructure
  problems, not ML problems.


  Apply to Y Combinator: https://www.ycombinator.com/apply

  Work at a startup: https://www.ycombinator.com/jobs


  Chapters:

  00:00 – Introduction

  01:05 – From Vicarious to OpenAI to Anthropic

  06:40 – What pretraining is

  11:20 – Why next-word prediction won out

  16:05 – Scaling laws and the feedback loop of compute → models → revenue

  21:50 – Building Anthropic’s early infrastructure

  27:35 – Efficiency hacks and debugging at scale

  33:10 – Generalists vs. specialists on the pretraining team

  38:45 – Challenges of training across thousands of GPUs

  44:15 – Working with new chips: GPUs vs. TPUs

  49:00 – Pretraining vs. post-training (RLHF and reasoning models)

  54:25 – The future of data quality and availability

  59:10 – Where pretraining goes next

  1:03:00 – Closing reflections
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:41:49.253Z
---

# Anthropic Head of Pretraining on Scaling Laws, Compute, and the Future of AI

## 00:00 - 95:00

[Music]

## 95:00 - 115:00

Hey guys, I'm thrilled to be joined

## 115:00 - 140:00

today by Nick Joseph, the head of

## 140:00 - 165:00

pre-training at Anthropic. To give

## 165:00 - 190:00

viewers a highle sense of what we'll be

## 190:00 - 210:00

covering, we're going to start with the

## 210:00 - 240:00

basics of what pre-training is and then

## 240:00 - 265:00

dig into how Nick thinks about strategy,

## 265:00 - 290:00

data alignment, and infrastructure at

## 290:00 - 315:00

Enthropic. And by the end, you'll

## 315:00 - 335:00

hopefully have a sense for how progress

## 335:00 - 365:00

in AI comes directly from advances in

## 365:00 - 390:00

pre-training. I would love to talk a

## 390:00 - 415:00

little bit about your backstory and kind

## 415:00 - 440:00

of how you got to this point. Where did

## 440:00 - 465:00

you work before Anthropic? And what were

## 465:00 - 500:00

your takeaways from those places? Yeah.

## 500:00 - 540:00

So let's see. I was at Vicarius uh and

## 540:00 - 585:00

then at OpenAI uh before Anthropic. So

## 585:00 - 615:00

Vicarius was originally a GI lab and

## 615:00 - 640:00

sort of when I joined they were sort of

## 640:00 - 670:00

making a shift to product particularly

## 670:00 - 700:00

working on robotics products and the

## 700:00 - 730:00

thing I worked on was like training uh

## 730:00 - 755:00

computer vision models for for their

## 755:00 - 780:00

robotics products. It was my first job.

## 780:00 - 800:00

So I think I just like learned a ton

## 800:00 - 835:00

about like how to do machine learning

## 835:00 - 860:00

models, how to like write machine

## 860:00 - 885:00

learning infrastructure.

## 885:00 - 910:00

>> And at the time were you also thinking

## 910:00 - 935:00

about a career as an academic? Like at

## 935:00 - 965:00

the time a lot of people doing AI work

## 965:00 - 990:00

were in PhDs. That's kind of what I was

## 990:00 - 1020:00

thinking about before I started to do a

## 1020:00 - 1035:00

company. Like how were you thinking

## 1035:00 - 1055:00

about that in your headsp space?

## 1055:00 - 1085:00

>> Yeah. So like I'm actually rewind a

## 1085:00 - 1105:00

little bit. I think like a lot of my

## 1105:00 - 1125:00

thinking on this had come from an

## 1125:00 - 1150:00

internship I did at Give Well, which is

## 1150:00 - 1175:00

like a nonprofit that evaluates

## 1175:00 - 1205:00

charities. And some people there being

## 1205:00 - 1235:00

like ah we're at some point we might

## 1235:00 - 1260:00

have AGI. It could be dangerous. We

## 1260:00 - 1280:00

should worry about these risks. This

## 1280:00 - 1310:00

could be like a big impact on humanity.

## 1310:00 - 1335:00

>> And I was like not super convinced at

## 1335:00 - 1360:00

the time and went down the economics

## 1360:00 - 1375:00

route and was going to try to work on

## 1375:00 - 1405:00

like directly helping people in poverty.

## 1405:00 - 1440:00

that didn't work out for various reasons

## 1440:00 - 1470:00

and ended up being like okay I'll at

## 1470:00 - 1505:00

least work on AI either like the safety

## 1505:00 - 1525:00

thing will turn out to be important I'll

## 1525:00 - 1550:00

work on that or it won't be and I'll

## 1550:00 - 1575:00

just make cool things with AI that can

## 1575:00 - 1610:00

probably help people in poverty more

## 1610:00 - 1640:00

>> I wasn't really coming at it from an

## 1640:00 - 1670:00

academic standpoint I was sort of like

## 1670:00 - 1700:00

in fact when I switched to that it was

## 1700:00 - 1725:00

part of the appeal was that I could like

## 1725:00 - 1760:00

immediately go do stuff in AI whereas if

## 1760:00 - 1785:00

I want to work in like economic policy

## 1785:00 - 1805:00

I'd have to wait

## 1805:00 - 1850:00

>> I don't know six years to do a PhD and

## 1850:00 - 1880:00

start and like totally uh it's it's a

## 1880:00 - 1890:00

longer path

## 1890:00 - 1920:00

>> and and what are the state of AI safety

## 1920:00 - 1940:00

work at that time even look like? Like

## 1940:00 - 1960:00

who are the people who were thinking

## 1960:00 - 1975:00

about that kind of stuff? I mean there

## 1975:00 - 1995:00

were some folks at vicarious thinking

## 1995:00 - 2010:00

about this kind of thing but it was

## 2010:00 - 2045:00

fundamentally a robotics company and and

## 2045:00 - 2065:00

so yeah how how were you thinking about

## 2065:00 - 2080:00

that at the time?

## 2080:00 - 2110:00

>> Yeah. So my sense was like at the time a

## 2110:00 - 2145:00

lot of the AI safety discussion was kind

## 2145:00 - 2180:00

of theoretical like the models weren't

## 2180:00 - 2210:00

actually that good. They weren't really

## 2210:00 - 2230:00

posing these dangers. So it was a lot

## 2230:00 - 2255:00

more like philosophical like oh at some

## 2255:00 - 2285:00

point we might get AI that's really

## 2285:00 - 2310:00

smart smarter than humans and like

## 2310:00 - 2345:00

should we wait this like future concern

## 2345:00 - 2385:00

how should we compare that to near-term

## 2385:00 - 2400:00

things? And I think that was like

## 2400:00 - 2440:00

actually a just a less compelling

## 2440:00 - 2455:00

argument. I think it was like an

## 2455:00 - 2480:00

interesting one and like sort of made

## 2480:00 - 2495:00

you think of it.

## 2495:00 - 2520:00

>> So next you went to OpenAI. What was

## 2520:00 - 2545:00

OpenAI like at this time?

## 2545:00 - 2570:00

>> Yeah. So I was at OpenAI. I was on one

## 2570:00 - 2600:00

of the safety teams and kind of worked

## 2600:00 - 2630:00

on uh

## 2630:00 - 2655:00

>> I ended up working on code models

## 2655:00 - 2685:00

actually and kind of when I got there I

## 2685:00 - 2720:00

could the the first thing I saw was oh

## 2720:00 - 2760:00

they'd find tune GT3 to write some code

## 2760:00 - 2795:00

but and it was really good and I was

## 2795:00 - 2825:00

like oh okay if you're worried about AI

## 2825:00 - 2855:00

getting really powerful writing its own

## 2855:00 - 2875:00

code that seems

## 2875:00 - 2925:00

>> seems like it could self-improve and how

## 2925:00 - 2945:00

how likely is that to happen? So it was

## 2945:00 - 2970:00

doing a bunch of evaluations and like

## 2970:00 - 2990:00

studies of what contributed

## 2990:00 - 3045:00

>> and then after like uh eight months uh

## 3045:00 - 3075:00

basically everyone I worked with like

## 3075:00 - 3105:00

all all the safety leads left

## 3105:00 - 3150:00

>> which uh yeah invited me to go to

## 3150:00 - 3170:00

Anthropic and that was sort of the

## 3170:00 - 3195:00

reason I joined OpenAI was because I

## 3195:00 - 3220:00

cared about AI safety and wanted to work

## 3220:00 - 3255:00

with them. So then I went with them to

## 3255:00 - 3285:00

join Anthropic uh pretty much right when

## 3285:00 - 3295:00

it started.

## 3295:00 - 3315:00

>> With that why don't we transition a bit

## 3315:00 - 3350:00

these days you run the pre-training team

## 3350:00 - 3385:00

specifically at Anthropic. Um, obviously

## 3385:00 - 3405:00

you've been working on pre-training at

## 3405:00 - 3430:00

anthropic for quite a bit of time and

## 3430:00 - 3450:00

I'm sure it's evolved over the years,

## 3450:00 - 3485:00

what that even entails and looks like.

## 3485:00 - 3510:00

Why don't we start by just talking a

## 3510:00 - 3530:00

little bit about what pre pre-training

## 3530:00 - 3560:00

is like? How does it even fit into the

## 3560:00 - 3590:00

way of thinking about how AI models have

## 3590:00 - 3615:00

developed at a place like Anthropic? And

## 3615:00 - 3635:00

what exactly do you guys do?

## 3635:00 - 3650:00

>> We know that one of the ingredients to

## 3650:00 - 3685:00

making AI models better is scale. You

## 3685:00 - 3715:00

want to put a lot of compute in. And if

## 3715:00 - 3735:00

you sort of step back and you're like,

## 3735:00 - 3760:00

okay, what's the way we could put the

## 3760:00 - 3785:00

most compute into a into a model

## 3785:00 - 3815:00

possible? We need some objective that

## 3815:00 - 3860:00

there's just like tons of data for. And

## 3860:00 - 3885:00

one idea here is like the internet. The

## 3885:00 - 3910:00

internet is massive. It's probably the

## 3910:00 - 3935:00

biggest like single source of data

## 3935:00 - 3975:00

humanity has created. And you don't have

## 3975:00 - 3995:00

labels. It's like you don't want someone

## 3995:00 - 4020:00

to have to go in and look read the

## 4020:00 - 4040:00

entire internet and like say something

## 4040:00 - 4065:00

about it. So you want to get labels out

## 4065:00 - 4085:00

of the data itself.

## 4085:00 - 4110:00

>> And the idea here is we can take some

## 4110:00 - 4135:00

text and we can predict the next word.

## 4135:00 - 4180:00

So you take you know the as the first

## 4180:00 - 4200:00

word you predict the second word then

## 4200:00 - 4230:00

you say the cat and you predict the word

## 4230:00 - 4265:00

after that. And this means you get very

## 4265:00 - 4305:00

dense signal. Every every word is like a

## 4305:00 - 4340:00

new example. And there's a huge amount

## 4340:00 - 4375:00

of data and one of the findings from my

## 4375:00 - 4420:00

GT1 GT2 was kind of as you throw more

## 4420:00 - 4460:00

compute at this more data bigger models

## 4460:00 - 4495:00

uh you get better you you get smarter

## 4495:00 - 4505:00

models essentially.

## 4505:00 - 4515:00

>> Totally.

## 4515:00 - 4545:00

>> Um and that's kind of been the central

## 4545:00 - 4580:00

thesis of pre-training for the whole

## 4580:00 - 4595:00

time.

## 4595:00 - 4625:00

>> Uh there's this idea of scaling laws

## 4625:00 - 4665:00

which is that you can actually quantify

## 4665:00 - 4690:00

like as you put in more compute more

## 4690:00 - 4715:00

more data more parameters you get models

## 4715:00 - 4750:00

in a very you get a lower loss a better

## 4750:00 - 4775:00

prediction of the next word in a very

## 4775:00 - 4815:00

predictable way. And I think you can

## 4815:00 - 4835:00

somewhat foresee from that original

## 4835:00 - 4860:00

paper and I think like Dario did foresee

## 4860:00 - 4890:00

this I think many people did but wasn't

## 4890:00 - 4920:00

obvious was that once you have that

## 4920:00 - 4940:00

there's this positive feedback loop

## 4940:00 - 4975:00

where you can train a model you can use

## 4975:00 - 5000:00

it to make something useful and sell

## 5000:00 - 5030:00

that and get more money use that to buy

## 5030:00 - 5065:00

more compute and then you actually train

## 5065:00 - 5100:00

a better model and I we've sort of run

## 5100:00 - 5145:00

that cycle over and over again over the

## 5145:00 - 5175:00

past 5 years or so. Well, in thinking

## 5175:00 - 5205:00

about that objective to begin, you know,

## 5205:00 - 5240:00

I think the way I think about the state

## 5240:00 - 5260:00

of pre-training is yeah, it seems like

## 5260:00 - 5290:00

this next word prediction, at least from

## 5290:00 - 5315:00

the external standpoint, seems to be the

## 5315:00 - 5335:00

dominant way pre-training happens. But

## 5335:00 - 5370:00

if I rewind the clock to that era of

## 5370:00 - 5420:00

2017 to 2020 or 2021 and two even, there

## 5420:00 - 5450:00

was all sorts of pre-training objectives

## 5450:00 - 5475:00

people were considering, right? There

## 5475:00 - 5500:00

was these uh BERT and BART models that

## 5500:00 - 5530:00

were doing mass language modeling. It

## 5530:00 - 5560:00

seems like this GPT series of models

## 5560:00 - 5605:00

doing uh auto reggressive modeling as

## 5605:00 - 5630:00

you describe this next word prediction

## 5630:00 - 5655:00

seems to be the dominant one that won

## 5655:00 - 5695:00

out. Do you have any reflections on that

## 5695:00 - 5715:00

time period? Like were you guys trying

## 5715:00 - 5745:00

all of them and kind of this one worked

## 5745:00 - 5780:00

or or is there some sort of first

## 5780:00 - 5805:00

principles reason why this is like the

## 5805:00 - 5825:00

right one that should have worked?

## 5825:00 - 5850:00

>> I think the answer is like it's mostly

## 5850:00 - 5870:00

empirical like in terms of how to think

## 5870:00 - 5885:00

of the things I'd be like yeah it's

## 5885:00 - 5905:00

empirical just try them all see what

## 5905:00 - 5935:00

works. One big advantage for this auto

## 5935:00 - 5960:00

reagive setup is that you can just

## 5960:00 - 5990:00

sample from it to generate text

## 5990:00 - 6020:00

afterwards in a fairly like

## 6020:00 - 6045:00

straightforward way that comes

## 6045:00 - 6085:00

>> like enables a product use very nicely.

## 6085:00 - 6115:00

>> Um like one thing that you want is like

## 6115:00 - 6145:00

one charact is like a loss whereas you

## 6145:00 - 6185:00

drive down the loss that actually is the

## 6185:00 - 6205:00

thing you care about and you can think

## 6205:00 - 6245:00

of it as like if you got to perfect on

## 6245:00 - 6290:00

language modeling you now can like write

## 6290:00 - 6315:00

text as a human. You can sort of imagine

## 6315:00 - 6340:00

you put in the title of a paper and it

## 6340:00 - 6365:00

should spit out the entire spit out a

## 6365:00 - 6390:00

novel paper. Whereas I think some of the

## 6390:00 - 6425:00

other approaches don't quite have that

## 6425:00 - 6440:00

uh flavor.

## 6440:00 - 6475:00

>> Yeah, totally. Yeah, it makes sense that

## 6475:00 - 6505:00

in terms of that loop you're describing

## 6505:00 - 6530:00

of, you know, then release something

## 6530:00 - 6555:00

that gets you revenue and you can use

## 6555:00 - 6585:00

that to buy more compute and iterate.

## 6585:00 - 6605:00

This sort of gives you the most natural

## 6605:00 - 6630:00

way to actually do that flow because you

## 6630:00 - 6655:00

can keep releasing new products and keep

## 6655:00 - 6680:00

getting the revenue from that to invest

## 6680:00 - 6700:00

in more compute and so on.

## 6700:00 - 6720:00

>> Yeah, it certainly gives you the most

## 6720:00 - 6740:00

open-ended thing. You could imagine, you

## 6740:00 - 6760:00

know, you like train something as a

## 6760:00 - 6785:00

class like you train some base thing,

## 6785:00 - 6800:00

you fine tune it for a bunch of

## 6800:00 - 6820:00

particular tasks. one approach people

## 6820:00 - 6840:00

would use. They would like do this big

## 6840:00 - 6865:00

pre-training and then they wouldn't just

## 6865:00 - 6895:00

like open-endedly sample from it. You'd

## 6895:00 - 6920:00

fine tune it on like a hundred specific

## 6920:00 - 6955:00

tasks and that could work too. I think

## 6955:00 - 6995:00

that like the one sort of general

## 6995:00 - 7020:00

intuition I have is like compute is the

## 7020:00 - 7050:00

thing that matters. So like I think if

## 7050:00 - 7080:00

you throw enough compute at any of these

## 7080:00 - 7095:00

objectives, you're going to get

## 7095:00 - 7130:00

something that's probably pretty good uh

## 7130:00 - 7155:00

and can kind of be fine tuned to other

## 7155:00 - 7185:00

things. And it's it's surprising how

## 7185:00 - 7220:00

little these details matter compared to

## 7220:00 - 7250:00

throwing more comput. When you think

## 7250:00 - 7275:00

about actually throwing more comput,

## 7275:00 - 7300:00

there's a whole bunch of axes by which

## 7300:00 - 7320:00

you could throw compute at it too,

## 7320:00 - 7360:00

right? And if you have a specific model

## 7360:00 - 7385:00

architecture you're training over, you

## 7385:00 - 7410:00

can basically throw more data at that

## 7410:00 - 7435:00

specific architecture. For a particular

## 7435:00 - 7460:00

one, you could add more layers or make

## 7460:00 - 7495:00

the models larger in it. You could do

## 7495:00 - 7520:00

some kind of neural architecture search

## 7520:00 - 7555:00

over lots of different variants. And I

## 7555:00 - 7585:00

assume that these days it's somewhat

## 7585:00 - 7605:00

more figured out, you know, which

## 7605:00 - 7625:00

architecture you go for. I assume the

## 7625:00 - 7655:00

earlier days it was somewhat less so.

## 7655:00 - 7670:00

And and I'm curious if you could speak

## 7670:00 - 7695:00

to how you guys thought about that. like

## 7695:00 - 7725:00

what did your infrastructure even look

## 7725:00 - 7765:00

like to do that type of determination?

## 7765:00 - 7790:00

>> I mean, I think the the short answer is

## 7790:00 - 7805:00

it's hard, right? Like what you're

## 7805:00 - 7820:00

really doing is you're going to train

## 7820:00 - 7845:00

this one big expensive model and you

## 7845:00 - 7890:00

have a space of, you know, you can sort

## 7890:00 - 7900:00

of call all these things

## 7900:00 - 7920:00

hyperparameters. You know, how many

## 7920:00 - 7940:00

layers do you have? What's your width?

## 7940:00 - 7960:00

Like you have the space of hundreds of

## 7960:00 - 7995:00

hyperparameters and you want them all to

## 7995:00 - 8030:00

be optimal and you're sort of striking

## 8030:00 - 8065:00

this balance actually between how much

## 8065:00 - 8095:00

do they matter like can you just take

## 8095:00 - 8120:00

your best guess and throw more compute

## 8120:00 - 8150:00

at it in whatever way you want and

## 8150:00 - 8170:00

basically doesn't matter. how much you

## 8170:00 - 8195:00

want to get it precisely correct.

## 8195:00 - 8205:00

>> Interesting.

## 8205:00 - 8225:00

>> And I think one of the like interesting

## 8225:00 - 8240:00

things is like it actually doesn't

## 8240:00 - 8265:00

matter that much. Like we like I think

## 8265:00 - 8290:00

this was in one of the early scaling

## 8290:00 - 8325:00

laws papers like you can change these

## 8325:00 - 8355:00

things and get little wins but like as

## 8355:00 - 8385:00

you throw more compute it it sort of

## 8385:00 - 8415:00

reliably gets better. If you mess up

## 8415:00 - 8450:00

enough you will you will sort stop

## 8450:00 - 8470:00

seeing that happen and you won't have

## 8470:00 - 8495:00

any way to know which is one of the

## 8495:00 - 8515:00

that's like kind of the hardest part in

## 8515:00 - 8520:00

some ways.

## 8520:00 - 8535:00

>> You don't know the counterfactual

## 8535:00 - 8555:00

basically because you didn't run it for

## 8555:00 - 8590:00

long enough to actually know what it is.

## 8590:00 - 8615:00

>> Yeah. We have these scaling laws. So you

## 8615:00 - 8640:00

can sort of say like as you train more

## 8640:00 - 8665:00

comput you expect the loss to go down as

## 8665:00 - 8685:00

a power law.

## 8685:00 - 8710:00

>> It's really a power law plus constant.

## 8710:00 - 8730:00

So what eventually will happen is you'll

## 8730:00 - 8760:00

curve off that power law and then you

## 8760:00 - 8780:00

know something is wrong and is it

## 8780:00 - 8805:00

fundamental? Is it like you've hit the

## 8805:00 - 8845:00

limits of scaling or is it nope you

## 8845:00 - 8865:00

should have ch you should have tweaked

## 8865:00 - 8890:00

your learning rate slightly differently

## 8890:00 - 8915:00

and that's that's sort of one of the

## 8915:00 - 8935:00

challenges in terms of how to like

## 8935:00 - 8960:00

figure it out. You can the the usual

## 8960:00 - 8985:00

paradigm is like test things out at

## 8985:00 - 9020:00

small scale before running them at large

## 9020:00 - 9045:00

scale and try to find

## 9045:00 - 9070:00

>> small scale in terms of data or in terms

## 9070:00 - 9095:00

of something else? uh in terms of

## 9095:00 - 9115:00

everything like you kind of want to

## 9115:00 - 9140:00

scale things down like proportionally.

## 9140:00 - 9165:00

So you want to say like you want you

## 9165:00 - 9185:00

want to have some theory for like how

## 9185:00 - 9225:00

you're going to scale up like ah okay if

## 9225:00 - 9255:00

I get 10 times as many flops how much of

## 9255:00 - 9280:00

it goes into layers how much of it goes

## 9280:00 - 9320:00

into data how much of it goes into

## 9320:00 - 9335:00

attention

## 9335:00 - 9390:00

>> and you sort of get that theory and then

## 9390:00 - 9425:00

>> test that it's optimal a bunch with like

## 9425:00 - 9450:00

scaling everything down proportionally

## 9450:00 - 9475:00

>> and and just so I can think about what

## 9475:00 - 9500:00

this actually looks like in those in

## 9500:00 - 9525:00

those early days of anthropic you know

## 9525:00 - 9545:00

you're a team of like 10 or something

## 9545:00 - 9575:00

like that in those very early days or 12

## 9575:00 - 9615:00

maybe what actually is your ability to

## 9615:00 - 9645:00

use large scale infrastructure as like a

## 9645:00 - 9680:00

relatively nimble startup at that time.

## 9680:00 - 9695:00

I mean a startup that was well

## 9695:00 - 9725:00

capitalized but still not actually that

## 9725:00 - 9750:00

many people working at. What kind of

## 9750:00 - 9785:00

infrastructure did you have access to to

## 9785:00 - 9815:00

train these early models at the So

## 9815:00 - 9835:00

actually one of the wild things was it

## 9835:00 - 9855:00

at least I mean you don't know what

## 9855:00 - 9880:00

anyone else is doing of course but it

## 9880:00 - 9915:00

kind of felt like we were like at the

## 9915:00 - 9960:00

frontier of it and there just weren't

## 9960:00 - 9985:00

that many people who cared like I was

## 9985:00 - 10000:00

sort of coming you know I was coming at

## 10000:00 - 10025:00

it from like we're making AGI this is

## 10025:00 - 10055:00

the most important technology ever and

## 10055:00 - 10070:00

then would kind of like look around and

## 10070:00 - 10105:00

be like and it seems like I'm one of 30

## 10105:00 - 10130:00

people who were working on this in like

## 10130:00 - 10165:00

the world. I mean I was kind of like

## 10165:00 - 10185:00

junior person. Everyone else sort of

## 10185:00 - 10205:00

knew how to do this and had done it

## 10205:00 - 10235:00

before but I was kind of surprised at

## 10235:00 - 10285:00

how easy it was. Um like the public

## 10285:00 - 10320:00

estimates for GP3 I remember were that

## 10320:00 - 10355:00

it cost $5 million to train which you're

## 10355:00 - 10380:00

like on the one hand five million is

## 10380:00 - 10405:00

kind of a lot but it's like a lot for an

## 10405:00 - 10435:00

individual person. It's not really a lot

## 10435:00 - 10485:00

from like a company perspective. So we

## 10485:00 - 10525:00

could totally buy like compute that was

## 10525:00 - 10555:00

enough to train models like that you

## 10555:00 - 10560:00

could

## 10560:00 - 10585:00

>> and were you using a cloud provider or

## 10585:00 - 10615:00

or did you have a custom setup somewhere

## 10615:00 - 10640:00

or did you literally have racks in a

## 10640:00 - 10655:00

room somewhere that you were you know

## 10655:00 - 10680:00

bought a bunch of Nvidia GPUs and you

## 10680:00 - 10700:00

were doing it? uh we're using a cloud

## 10700:00 - 10730:00

provider, but I think it's kind of it's

## 10730:00 - 10750:00

not actually that different because one

## 10750:00 - 10775:00

of the things that's was surprising to

## 10775:00 - 10810:00

me is you actually have to understand

## 10810:00 - 10860:00

the the literal layout. Like uh I

## 10860:00 - 10880:00

remember at one point uh one of my

## 10880:00 - 10905:00

co-workers running a clustering

## 10905:00 - 10950:00

algorithm to identify what rooms all the

## 10950:00 - 10980:00

chips were in since we we had a

## 10980:00 - 11005:00

hypothesis that they were in different

## 11005:00 - 11035:00

rooms and that was causing like or you

## 11035:00 - 11065:00

know different buildup some sort of

## 11065:00 - 11080:00

network latency and you can kind of

## 11080:00 - 11100:00

figure it out. you could like reverse

## 11100:00 - 11120:00

engineer like ah okay yeah there's

## 11120:00 - 11155:00

clearly like two clusters here that are

## 11155:00 - 11180:00

connected better and there's some issue

## 11180:00 - 11205:00

on the connection between them like

## 11205:00 - 11225:00

you're we're trying to push the limits

## 11225:00 - 11255:00

of of the hardware like as much as

## 11255:00 - 11270:00

possible

## 11270:00 - 11290:00

>> um particularly at the beginning when we

## 11290:00 - 11305:00

were kind of like we have way less

## 11305:00 - 11325:00

funding than everyone else we have to

## 11325:00 - 11345:00

and and most people weren't very

## 11345:00 - 11365:00

efficient with the compute so we were

## 11365:00 - 11400:00

like ah we get a big lead by being

## 11400:00 - 11430:00

really efficient at at how how we use

## 11430:00 - 11440:00

the comput

## 11440:00 - 11455:00

>> could you talk a little bit about some

## 11455:00 - 11475:00

of the things you guys did in those

## 11475:00 - 11500:00

early days for how to get the most out

## 11500:00 - 11515:00

of the hardware I think it's really

## 11515:00 - 11535:00

interesting like I think back to the

## 11535:00 - 11560:00

days of the early days of Google for

## 11560:00 - 11585:00

example where there's the there's these

## 11585:00 - 11615:00

cases where they basically bought

## 11615:00 - 11645:00

relatively cheap consumer chips and then

## 11645:00 - 11670:00

they optimized the software to make it

## 11670:00 - 11690:00

so you can actually get the most bang

## 11690:00 - 11710:00

for your buck out of them and that's how

## 11710:00 - 11745:00

they had all this high latency or low

## 11745:00 - 11775:00

latency high availability stuff. I'm

## 11775:00 - 11800:00

kind of curious if there's some analog

## 11800:00 - 11830:00

in the early AI era to that.

## 11830:00 - 11860:00

>> I think for us it was largely about like

## 11860:00 - 11885:00

getting the distributed framework right

## 11885:00 - 11910:00

so like we're training on in order to

## 11910:00 - 11935:00

train you have to train them on a large

## 11935:00 - 11955:00

number of chips

## 11955:00 - 11980:00

>> and there's a bunch of different

## 11980:00 - 12010:00

approaches to to how to do this. There's

## 12010:00 - 12025:00

like data parallels and there's

## 12025:00 - 12060:00

pipelining there's upsharting and like

## 12060:00 - 12090:00

getting all of the At the time there

## 12090:00 - 12110:00

were no like great open source packages

## 12110:00 - 12135:00

you could just grab and use that just

## 12135:00 - 12155:00

worked for this. I mean today there's

## 12155:00 - 12185:00

somewhat more of these but at the time I

## 12185:00 - 12205:00

assume there was literally none.

## 12205:00 - 12230:00

>> There were some like I actually remember

## 12230:00 - 12265:00

that we were working on data parallelism

## 12265:00 - 12290:00

early on and someone was like and now we

## 12290:00 - 12325:00

write the or reduce it. I was like we

## 12325:00 - 12350:00

really do this ourselves. don't like

## 12350:00 - 12380:00

package and this was kind of like well

## 12380:00 - 12400:00

we're going to want to modify it right

## 12400:00 - 12440:00

like oh like we don't want to outsource

## 12440:00 - 12480:00

this to some package because a we're

## 12480:00 - 12505:00

about to go to a bigger scale like

## 12505:00 - 12530:00

pietorch for they had a package for

## 12530:00 - 12560:00

doing this but we were going to go to a

## 12560:00 - 12600:00

bigger scale than Facebook had been to

## 12600:00 - 12630:00

>> and you don't want to have a dependency

## 12630:00 - 12670:00

on a package uh that you're going to

## 12670:00 - 12700:00

have to be like constantly modifying

## 12700:00 - 12710:00

essentially

## 12710:00 - 12730:00

>> that's it's such a counterintuitive

## 12730:00 - 12755:00

sentence there too like we're going to a

## 12755:00 - 12775:00

bigger scale than Facebook will because

## 12775:00 - 12810:00

at the time Facebook AI research was

## 12810:00 - 12835:00

considered one of the best places to do

## 12835:00 - 12865:00

machine learning research like fair was

## 12865:00 - 12890:00

one of the play fair and deep mind we're

## 12890:00 - 12925:00

hiring lots of people out of PhD

## 12925:00 - 12950:00

programs and doing lots of things like

## 12950:00 - 12970:00

what was your headsp space when you were

## 12970:00 - 13005:00

like okay this this very established lab

## 13005:00 - 13035:00

with great people and whatnot we are

## 13035:00 - 13060:00

operating on a scale that is not

## 13060:00 - 13090:00

relevant to them like was that natural

## 13090:00 - 13120:00

and obvious to you or was there times

## 13120:00 - 13145:00

where you kind of doubted the decisions

## 13145:00 - 13175:00

you were making in that situation

## 13175:00 - 13210:00

>> I think it was surprising I will maybe

## 13210:00 - 13235:00

I'm just too arrogant or something I

## 13235:00 - 13260:00

kind of looked around and was like what

## 13260:00 - 13280:00

are these people doing they're all

## 13280:00 - 13320:00

missing the like big picture here like I

## 13320:00 - 13350:00

I I think the scaling laws were pretty

## 13350:00 - 13380:00

clear like and the arguments against I

## 13380:00 - 13410:00

just thought were kind of nonsensical

## 13410:00 - 13430:00

like you know the scaling I think the

## 13430:00 - 13455:00

original scaling laws paper had like 11

## 13455:00 - 13485:00

orders of magnitude and there was like

## 13485:00 - 13510:00

this intense debate on whether it would

## 13510:00 - 13550:00

continue for like another point and I

## 13550:00 - 13565:00

was like

## 13565:00 - 13605:00

>> like it seems it seems like one over 11

## 13605:00 - 13640:00

is maybe your chance it fails here and

## 13640:00 - 13665:00

then like you know sometimes it doesn't

## 13665:00 - 13685:00

work like sometimes it just works

## 13685:00 - 13705:00

straightforward you like train the model

## 13705:00 - 13745:00

you're like oh yeah of course but yeah I

## 13745:00 - 13785:00

do think that it was it maybe felt

## 13785:00 - 13810:00

obvious when you're in that headsp space

## 13810:00 - 13830:00

and you're working on this all the time

## 13830:00 - 13860:00

and you're making those plots and I

## 13860:00 - 13875:00

think these things feel pretty different

## 13875:00 - 13895:00

when you're on the outside. You know,

## 13895:00 - 13930:00

there's a huge space of papers. Everyone

## 13930:00 - 13960:00

tries to make their paper sound like

## 13960:00 - 13995:00

very robust and and important. I I could

## 13995:00 - 14025:00

see I could see being like, "Oh yeah,

## 14025:00 - 14045:00

this is not really a thing."

## 14045:00 - 14055:00

>> Totally.

## 14055:00 - 14080:00

>> But also different labs had different

## 14080:00 - 14100:00

cultures. So like I think one of the

## 14100:00 - 14145:00

things at fair was it was a very

## 14145:00 - 14175:00

>> more PhD style independent research.

## 14175:00 - 14195:00

People have their own ideas, pursue

## 14195:00 - 14200:00

those.

## 14200:00 - 14225:00

>> You're fighting for your compute and so

## 14225:00 - 14230:00

on.

## 14230:00 - 14255:00

>> Yeah. And to do a project like training

## 14255:00 - 14285:00

a large language model requires a lot of

## 14285:00 - 14315:00

people to collaborate on like a really

## 14315:00 - 14350:00

complicated piece of infrastructure that

## 14350:00 - 14370:00

isn't going to be a paper, right? Like

## 14370:00 - 14405:00

you're not going to publish like, oh, I

## 14405:00 - 14445:00

got a slightly I got 5% more efficiency

## 14445:00 - 14455:00

totally

## 14455:00 - 14480:00

>> than the next one. Um, and it's not

## 14480:00 - 14505:00

respected in like those cultures

## 14505:00 - 14525:00

necessarily. So that might have been

## 14525:00 - 14530:00

part of it.

## 14530:00 - 14545:00

>> Okay. Okay. So then when you actually

## 14545:00 - 14575:00

implement these these models, you're

## 14575:00 - 14625:00

saying you're using a level of low-level

## 14625:00 - 14650:00

programming where you know you're using

## 14650:00 - 14670:00

libraries like PyTorch, but you're

## 14670:00 - 14690:00

perhaps not using everything right out

## 14690:00 - 14715:00

of the box from PyTorch because there's

## 14715:00 - 14730:00

things you guys want to customize that

## 14730:00 - 14755:00

are at the level of basically one level

## 14755:00 - 14785:00

of abstraction below them, but not

## 14785:00 - 14805:00

necessarily at the level of abstraction

## 14805:00 - 14830:00

of you know writing custom CUDA kernels

## 14830:00 - 14865:00

or or like was that also in in the space

## 14865:00 - 14880:00

where you guys were thinking about?

## 14880:00 - 14900:00

>> So it depends on like the operation. So

## 14900:00 - 14925:00

like I think I was mostly operating at

## 14925:00 - 14960:00

the level of like torch.mmatal you know

## 14960:00 - 14995:00

like uh yes where does a matal go but

## 14995:00 - 15015:00

not thinking like how do you make the

## 15015:00 - 15055:00

matal efficient like I assume torch

## 15055:00 - 15080:00

figured out how to make a matal as

## 15080:00 - 15110:00

efficient as is possible but there are

## 15110:00 - 15140:00

some pieces like attention where there

## 15140:00 - 15160:00

was just kind of a lot of different

## 15160:00 - 15185:00

varants and attention is really

## 15185:00 - 15210:00

complicated and hard to make efficient

## 15210:00 - 15265:00

on a GPU and th those things you have to

## 15265:00 - 15300:00

kind of go go more levels down on the

## 15300:00 - 15330:00

stack. Uh I think there was like a

## 15330:00 - 15360:00

process that is maybe interesting that

## 15360:00 - 15395:00

I'd never really like thought of before

## 15395:00 - 15415:00

of like how to do it which is sort of

## 15415:00 - 15445:00

like modeling out the pro the thing

## 15445:00 - 15465:00

you're going to do coming up with a

## 15465:00 - 15490:00

strategy for how to paralyze it that

## 15490:00 - 15530:00

like can get to a really good efficiency

## 15530:00 - 15540:00

you know like

## 15540:00 - 15565:00

>> so you're thinking about MFU basically

## 15565:00 - 15605:00

like your utilization on your GPU. So

## 15605:00 - 15630:00

there's like a goal utilization you're

## 15630:00 - 15650:00

trying to get at and a strategy to get

## 15650:00 - 15665:00

to there. You're saying

## 15665:00 - 15680:00

>> yeah and I think like one of the things

## 15680:00 - 15700:00

you can do is you can actually like

## 15700:00 - 15725:00

pencil and paper math out what

## 15725:00 - 15745:00

efficiency you're going to be able to

## 15745:00 - 15760:00

get to. Right. you know all the

## 15760:00 - 15805:00

constraints it's MFU and is flops

## 15805:00 - 15835:00

utilization but like the reason you

## 15835:00 - 15865:00

don't get good MFU is you end up limited

## 15865:00 - 15925:00

on HBM bandwidth you end up limited on I

## 15925:00 - 15970:00

don't know as host to like CPU offload

## 15970:00 - 15990:00

there's a bunch of different pieces but

## 15990:00 - 16015:00

it but there's not that many pieces

## 16015:00 - 16060:00

there's like six relevant numbers there

## 16060:00 - 16080:00

so you can totally model it out

## 16080:00 - 16110:00

understand what the constraints are and

## 16110:00 - 16145:00

then implement something that can get

## 16145:00 - 16160:00

there it of course will be really

## 16160:00 - 16185:00

inefficient when you implement it and

## 16185:00 - 16205:00

then the next step is like pulling out a

## 16205:00 - 16225:00

profiler so you want to be able to

## 16225:00 - 16260:00

profile the job look how long every

## 16260:00 - 16290:00

operation takes. Have a model in your

## 16290:00 - 16315:00

mind of how long every operation should

## 16315:00 - 16360:00

take and then make those two things the

## 16360:00 - 16365:00

same.

## 16365:00 - 16390:00

>> And and were there good out of- thebox

## 16390:00 - 16415:00

profilers you could use at that time or

## 16415:00 - 16440:00

did you guys have you know because

## 16440:00 - 16460:00

people weren't operating on the kind of

## 16460:00 - 16485:00

network topologies you guys may have

## 16485:00 - 16510:00

been using. Did you have to write your

## 16510:00 - 16535:00

own profilers basically to do this type

## 16535:00 - 16580:00

of you know multi-node optimization?

## 16580:00 - 16610:00

>> Yeah, it depends when I actually getting

## 16610:00 - 16630:00

better with time. The PyTorch profiler

## 16630:00 - 16655:00

was like pretty good actually throughout

## 16655:00 - 16680:00

for a single GPU. If you want to like

## 16680:00 - 16705:00

profile a GPU, the PyTorch profile would

## 16705:00 - 16745:00

work. But if you wanted to profile a job

## 16745:00 - 16785:00

on hundreds, thousands of GPUs, that

## 16785:00 - 16815:00

like hadn't really been done much. And

## 16815:00 - 16845:00

then that was kind of more of us like

## 16845:00 - 16885:00

hacking into the profiler to figure out

## 16885:00 - 16905:00

how to combine all the traces together.

## 16905:00 - 16925:00

>> And then one more question on that

## 16925:00 - 16950:00

earlier is, you know, you had mentioned,

## 16950:00 - 16965:00

you know, you hadn't really done a lot

## 16965:00 - 16995:00

of this work before maybe some time at

## 16995:00 - 17020:00

OpenAI and those early days in

## 17020:00 - 17045:00

anthropic. How did you actually go learn

## 17045:00 - 17065:00

all this stuff? Like what was your

## 17065:00 - 17090:00

process for learning about those six

## 17090:00 - 17120:00

things that were relevant to bandwidth

## 17120:00 - 17140:00

limitations and whatnot?

## 17140:00 - 17165:00

>> I mean, so when I joined anthropic, one

## 17165:00 - 17185:00

really nice thing was there just wasn't

## 17185:00 - 17215:00

that much. I think my first day I read

## 17215:00 - 17275:00

through our entire uh all all of Slack

## 17275:00 - 17320:00

and the entire like internal database

## 17320:00 - 17360:00

and learned a bunch from that. Like it

## 17360:00 - 17380:00

was kind of nice to just be like

## 17380:00 - 17415:00

everything is relevant to me. And then I

## 17415:00 - 17435:00

mostly learned from pair programming.

## 17435:00 - 17470:00

Like uh Tom Brown had done all this

## 17470:00 - 17500:00

before. So he kind of like knew all the

## 17500:00 - 17535:00

stuff quite well. Sam Mclish my manager

## 17535:00 - 17555:00

had also done a lot of it before and I

## 17555:00 - 17595:00

just like paired with them a huge amount

## 17595:00 - 17625:00

at the beginning. And I think one of the

## 17625:00 - 17650:00

things I really like about pairing as a

## 17650:00 - 17675:00

way of learning is you learn the like

## 17675:00 - 17700:00

thing you're trying to do. Like you will

## 17700:00 - 17720:00

learn that like if you're pairing

## 17720:00 - 17735:00

someone better than you, they can just

## 17735:00 - 17750:00

do it. So you're mostly just watching

## 17750:00 - 17775:00

them. But you also learn how people do

## 17775:00 - 17810:00

it. So something like a pro how to use a

## 17810:00 - 17840:00

profiler is not something you would ever

## 17840:00 - 17875:00

learn from seeing someone's like final

## 17875:00 - 17910:00

write up on Slack for their PR. You

## 17910:00 - 17930:00

would just be like, "Oh, they found

## 17930:00 - 17965:00

these. They changed this specific line

## 17965:00 - 17990:00

and it's a win." They

## 17990:00 - 18010:00

>> like you need to watch like a YouTube

## 18010:00 - 18050:00

video for 4 hours of someone messing

## 18050:00 - 18080:00

around with a profiler to like maybe

## 18080:00 - 18110:00

self teach it or something or to

## 18110:00 - 18135:00

actually pair with someone is basically

## 18135:00 - 18150:00

the best you can do.

## 18150:00 - 18170:00

>> I think there was like one thing that I

## 18170:00 - 18195:00

I think is embarrassing now that I look

## 18195:00 - 18215:00

back is I'd never actually used a

## 18215:00 - 18250:00

debugger before joining anthropic.

## 18250:00 - 18275:00

People talk about it PTB of like yeah

## 18275:00 - 18300:00

that's a thing people use but print

## 18300:00 - 18330:00

seems fine for me.

## 18330:00 - 18370:00

>> Then I like watch like oh no a debugger

## 18370:00 - 18395:00

is a super useful tool. this person's

## 18395:00 - 18420:00

way faster at debugging things

## 18420:00 - 18440:00

particularly if it takes a long time to

## 18440:00 - 18485:00

start up the code which they can and

## 18485:00 - 18505:00

yeah learn learning that sort of thing I

## 18505:00 - 18545:00

think comes best from pairing and then

## 18545:00 - 18565:00

there's of course the obvious you just

## 18565:00 - 18590:00

learn by doing you know I eventually did

## 18590:00 - 18620:00

like spit up profile and stare at it for

## 18620:00 - 18635:00

many many hours

## 18635:00 - 18665:00

>> totally yeah exactly yeah okay so so

## 18665:00 - 18695:00

then that was sort of the very early era

## 18695:00 - 18730:00

over time obviously pre-training has

## 18730:00 - 18750:00

become bigger and bigger as you're

## 18750:00 - 18775:00

describing scaling I imagine you're

## 18775:00 - 18825:00

using many x more GPUs much more compute

## 18825:00 - 18860:00

over time I'd be really curious to hear

## 18860:00 - 18890:00

first at a high level What do you feel

## 18890:00 - 18910:00

has changed about the pre-training

## 18910:00 - 18935:00

strategy that you could talk about?

## 18935:00 - 18960:00

Obviously, there's more compute, but

## 18960:00 - 18985:00

what does that actually mean to have

## 18985:00 - 19020:00

more compute in terms of what you think

## 19020:00 - 19040:00

about differently from those early days

## 19040:00 - 19050:00

versus now?

## 19050:00 - 19070:00

>> I'm sure the things that haven't changed

## 19070:00 - 19110:00

cuz I think it is like shocking how in

## 19110:00 - 19130:00

some ways like

## 19130:00 - 19160:00

>> I think I'm still pushing down the exact

## 19160:00 - 19200:00

same metric that I was on like day one.

## 19200:00 - 19225:00

like there's like some loss function

## 19225:00 - 19250:00

>> loss go down and I think you could like

## 19250:00 - 19280:00

look at some like you could probably run

## 19280:00 - 19305:00

the original the first model I trained

## 19305:00 - 19335:00

on the same metric and just like make a

## 19335:00 - 19375:00

plot of like progress of team over over

## 19375:00 - 19410:00

time. Uh so that's all the same. I think

## 19410:00 - 19420:00

the

## 19420:00 - 19450:00

>> one OKR is like one thing that matters

## 19450:00 - 19465:00

basically. Yeah, totally.

## 19465:00 - 19495:00

>> And like I mean talking about like OKRs

## 19495:00 - 19515:00

it's very sized company you're like oh

## 19515:00 - 19540:00

should you do OKRs and it's always felt

## 19540:00 - 19590:00

a little bit funny for uh a team like

## 19590:00 - 19615:00

where I'm like sure I can just pick a

## 19615:00 - 19650:00

loss value but like the answer is like

## 19650:00 - 19680:00

as low as possible. We will continue to

## 19680:00 - 19695:00

work on that forever.

## 19695:00 - 19725:00

>> I think the biggest things that have

## 19725:00 - 19740:00

changed has been a little more

## 19740:00 - 19765:00

specialization. Like I think at the

## 19765:00 - 19800:00

beginning, I mean the first like 3 or 6

## 19800:00 - 19830:00

months I tried to read every PR in the

## 19830:00 - 19850:00

codebase and that was great. I knew all

## 19850:00 - 19905:00

the pieces etc. And as you grow, it's

## 19905:00 - 19925:00

kind of everything gets like a little

## 19925:00 - 19950:00

more precise. You know, people really

## 19950:00 - 19985:00

dial in exactly how attention should

## 19985:00 - 20015:00

work, let's say, or you know, really

## 20015:00 - 20055:00

dial in like uh the parallelism

## 20055:00 - 20105:00

strategy. and you end up with a team

## 20105:00 - 20125:00

where it's a bunch of people who are

## 20125:00 - 20165:00

like deep experts on individual things

## 20165:00 - 20185:00

which is great because it means you can

## 20185:00 - 20210:00

go you can go really deep on those

## 20210:00 - 20250:00

things but sometimes you uh at least for

## 20250:00 - 20265:00

me as a manager one of the things you

## 20265:00 - 20285:00

sometimes have to think about is like

## 20285:00 - 20310:00

making sure the bigger picture makes

## 20310:00 - 20330:00

sense and also that you have enough

## 20330:00 - 20365:00

people who actually do understand the

## 20365:00 - 20385:00

whole bigger picture that there's no

## 20385:00 - 20400:00

like single point of failure.

## 20400:00 - 20425:00

>> Yeah, it's interesting you you frame it

## 20425:00 - 20450:00

in that with that trade-off, right?

## 20450:00 - 20475:00

Because as as you were describing that I

## 20475:00 - 20490:00

was trying to think, you know, is this a

## 20490:00 - 20515:00

bug or a feature? like there there's

## 20515:00 - 20535:00

some obvious features of it which is you

## 20535:00 - 20560:00

get expertise and you can optimize

## 20560:00 - 20600:00

certain things but I imagine your

## 20600:00 - 20650:00

ability to take bigger swings becomes

## 20650:00 - 20680:00

more complicated if not everyone's

## 20680:00 - 20700:00

exactly pointed in the same direction

## 20700:00 - 20740:00

like how do you wrestle with that now

## 20740:00 - 20765:00

>> yeah I think I mostly just try to get a

## 20765:00 - 20800:00

balance of people I think one of the

## 20800:00 - 20815:00

challenges early

## 20815:00 - 20830:00

>> people oh that's interesting

## 20830:00 - 20855:00

>> yeah like I think people really do have

## 20855:00 - 20880:00

a preference here has been one of the

## 20880:00 - 20900:00

things I've seen like there are people

## 20900:00 - 20930:00

who really want to be a generalist and

## 20930:00 - 20960:00

understand everything and like lightly

## 20960:00 - 20980:00

touch on things there people who want to

## 20980:00 - 20990:00

like

## 20990:00 - 21005:00

>> pick an area often they've already

## 21005:00 - 21035:00

picked that area and they're like deep

## 21035:00 - 21060:00

experts in precision. You know they

## 21060:00 - 21080:00

started they did a whole PhD in

## 21080:00 - 21100:00

precision and just want to think about

## 21100:00 - 21110:00

that

## 21110:00 - 21140:00

>> and you want to get some balance of

## 21140:00 - 21165:00

that. I think early there was a phase

## 21165:00 - 21180:00

where we'd hired a lot of people who are

## 21180:00 - 21200:00

more generalist shaped because that's

## 21200:00 - 21230:00

what the people who joined totally early

## 21230:00 - 21245:00

startup where they go work on everything

## 21245:00 - 21265:00

and then

## 21265:00 - 21290:00

>> you ended up with kind of everyone doing

## 21290:00 - 21335:00

everything and no one really really

## 21335:00 - 21365:00

deeply understanding one thing. uh and

## 21365:00 - 21390:00

that's one failure mode but I think if

## 21390:00 - 21405:00

you get too many people who are

## 21405:00 - 21425:00

specialists

## 21425:00 - 21470:00

>> you end up with a lot of effort has to

## 21470:00 - 21495:00

come from the manager from like the lead

## 21495:00 - 21525:00

to connect everything

## 21525:00 - 21565:00

>> and to notice something like ah if we

## 21565:00 - 21595:00

change the architecture here that would

## 21595:00 - 21630:00

make this like efficiency consideration

## 21630:00 - 21660:00

over there way easier

## 21660:00 - 21685:00

>> um one of the things I really liked kind

## 21685:00 - 21700:00

of like at the very beginning was like

## 21700:00 - 21720:00

let's work on efficiency but I could

## 21720:00 - 21755:00

just go and like be like ah well what if

## 21755:00 - 21780:00

we change the way we do like this

## 21780:00 - 21805:00

particular step and we'll be like oh

## 21805:00 - 21835:00

yeah that's probably fine like easy

## 21835:00 - 21860:00

change and then like you can avoid did

## 21860:00 - 21880:00

this whole complicated project to make

## 21880:00 - 21910:00

this operation that was hard efficient

## 21910:00 - 21930:00

because you can make an easier operation

## 21930:00 - 21940:00

efficient.

## 21940:00 - 21970:00

>> Okay. Interesting. Yeah. So, as the

## 21970:00 - 22005:00

level of comput has also gotten bigger.

## 22005:00 - 22030:00

>> So, I'm I'm sure anyone can imagine,

## 22030:00 - 22060:00

okay, there's more GPUs now, you have to

## 22060:00 - 22090:00

network them more. Are there some like

## 22090:00 - 22125:00

kind of non-obvious challenges that have

## 22125:00 - 22170:00

arisen over time where you guys have

## 22170:00 - 22190:00

just like banged your head against the

## 22190:00 - 22225:00

wall to solve them because of the amount

## 22225:00 - 22250:00

of comput you're dealing with that

## 22250:00 - 22270:00

people wouldn't otherwise know about

## 22270:00 - 22295:00

that like you want to share? I think

## 22295:00 - 22330:00

that connecting them is one that's maybe

## 22330:00 - 22365:00

interesting and like surprisingly hard.

## 22365:00 - 22390:00

Okay. because you really do get more and

## 22390:00 - 22430:00

more chips connected and

## 22430:00 - 22455:00

>> like one thing that I think is like the

## 22455:00 - 22485:00

the standard way people paralyze chips

## 22485:00 - 22525:00

isn't um the whole thing is one failure

## 22525:00 - 22555:00

domain like one chip fails the whole

## 22555:00 - 22575:00

thing can crash

## 22575:00 - 22585:00

>> and

## 22585:00 - 22605:00

>> the standard way as in the standard way

## 22605:00 - 22630:00

people doing AI or the standard way in

## 22630:00 - 22665:00

in other fields where people are doing

## 22665:00 - 22705:00

>> uh in AI for like I mean at least like I

## 22705:00 - 22730:00

think at the beginning you know first

## 22730:00 - 22770:00

versions of things were this way and

## 22770:00 - 22795:00

>> so it's like you have a 100 GPU cluster

## 22795:00 - 22825:00

or whatever is 128 like if one of them

## 22825:00 - 22855:00

dies job fails basically

## 22855:00 - 22875:00

>> yeah I mean you The simplest thing is if

## 22875:00 - 22895:00

you just like distribute your model. So

## 22895:00 - 22925:00

say you put like every layer on a

## 22925:00 - 22965:00

different chip and you lose like layer

## 22965:00 - 22995:00

seven like

## 22995:00 - 23040:00

>> yeah you're not going to like skip layer

## 23040:00 - 23075:00

seven. I guess you could but that's like

## 23075:00 - 23110:00

a pretty weird model training process

## 23110:00 - 23135:00

now and like that leads to some

## 23135:00 - 23160:00

interesting things which is like okay so

## 23160:00 - 23180:00

now as you scale up you have more and

## 23180:00 - 23205:00

more chips and the failure rate can get

## 23205:00 - 23225:00

like larger and larger.

## 23225:00 - 23255:00

>> On the other hand you can like I don't

## 23255:00 - 23275:00

know you can like restart pretty quickly

## 23275:00 - 23295:00

there. There's nothing like you just

## 23295:00 - 23330:00

have to like load back in some ways. So

## 23330:00 - 23350:00

that was one thing. And then the thing

## 23350:00 - 23400:00

was like the level of novelty at the

## 23400:00 - 23425:00

whole stack is something that's

## 23425:00 - 23460:00

surprising. Like basically

## 23460:00 - 23485:00

>> everything from like how the chips are

## 23485:00 - 23525:00

laid out in the data center to the chips

## 23525:00 - 23560:00

themselves is pretty new. Like there

## 23560:00 - 23575:00

there just haven't been that many

## 23575:00 - 23610:00

generations of GPUs. I think one of the

## 23610:00 - 23630:00

things that I don't know when I learned

## 23630:00 - 23665:00

computer science my code wouldn't work

## 23665:00 - 23685:00

and I'd be like oh the computer's

## 23685:00 - 23710:00

broken. I think my teacher was like the

## 23710:00 - 23730:00

you can trust the computer's not broken

## 23730:00 - 23755:00

like you messed up.

## 23755:00 - 23775:00

>> It's you messed up. And I think one of

## 23775:00 - 23790:00

the most frustrating things I

## 23790:00 - 23825:00

encountered in AI early on was working

## 23825:00 - 23850:00

on something and being like, I don't

## 23850:00 - 23865:00

know what I'm doing wrong. I'm just

## 23865:00 - 23910:00

totally stumped. And uh my manager

## 23910:00 - 23935:00

looked at it and was like, uh yeah,

## 23935:00 - 23955:00

probably the computer's wrong.

## 23955:00 - 23985:00

>> And I was like, that seems unlikely. And

## 23985:00 - 24005:00

sure enough, the computer was wrong.

## 24005:00 - 24045:00

Turned out that like the GPU was broken

## 24045:00 - 24100:00

and uh we had to pull in a new one. But

## 24100:00 - 24125:00

you have to like think like having to

## 24125:00 - 24160:00

think about that like the GPU could be

## 24160:00 - 24195:00

wrong, the GPU could be slow, like these

## 24195:00 - 24230:00

sorts of issues. Uh the power supply in

## 24230:00 - 24260:00

the data center could be broken. there's

## 24260:00 - 24310:00

so much more like level of depth than

## 24310:00 - 24350:00

you like kind of expect to need as a

## 24350:00 - 24370:00

Python programmer.

## 24370:00 - 24390:00

>> And just to visualize it like in those

## 24390:00 - 24415:00

early days, I assume you guys were using

## 24415:00 - 24440:00

the number of GPUs. It's probably on the

## 24440:00 - 24465:00

order of tens to hundreds or something

## 24465:00 - 24490:00

like that per run. It's probably not

## 24490:00 - 24510:00

tens of thousands or hundreds of

## 24510:00 - 24535:00

thousands per run or what was the rough

## 24535:00 - 24560:00

size you guys were at? Those are very

## 24560:00 - 24585:00

early days on the order of thousands.

## 24585:00 - 24605:00

Like would they fit in this room?

## 24605:00 - 24615:00

>> Thousands.

## 24615:00 - 24635:00

>> Yeah, thousands. So like you could have

## 24635:00 - 24660:00

a bunch of racks and you could fit them

## 24660:00 - 24685:00

into like one room. I assume these days

## 24685:00 - 24720:00

it's basically like a building for for

## 24720:00 - 24730:00

one of these runs.

## 24730:00 - 24750:00

>> Yeah. Now I think it's like you know

## 24750:00 - 24780:00

huge huge campuses. At the time it was

## 24780:00 - 24805:00

like kind of unclear. It was like oh I

## 24805:00 - 24825:00

think like we were like you know do we

## 24825:00 - 24845:00

need them all in one room? Can we be

## 24845:00 - 24890:00

spread across multiple rooms? Like uh

## 24890:00 - 24910:00

and you know we had these theoretical

## 24910:00 - 24930:00

models you be like we need this much

## 24930:00 - 24960:00

bandwidth from point A to point B. But

## 24960:00 - 24985:00

you like you never know how far down you

## 24985:00 - 25015:00

have to go like oh but like how much

## 25015:00 - 25035:00

power do we need? Like what if there's

## 25035:00 - 25065:00

like a single capacitor that's like

## 25065:00 - 25090:00

handling all of them and we like turn on

## 25090:00 - 25110:00

the whole job at once. Like does that

## 25110:00 - 25130:00

crash things?

## 25130:00 - 25165:00

>> Yeah. And so do you have to think about

## 25165:00 - 25185:00

differences in the different types of

## 25185:00 - 25205:00

chips? You guys work with all sorts of

## 25205:00 - 25235:00

different cloud providers. From your

## 25235:00 - 25265:00

standpoint, are these just sources of

## 25265:00 - 25300:00

compute or if you guys are using TPU

## 25300:00 - 25350:00

versus GPU, are these, you know, Google

## 25350:00 - 25385:00

TPU versus Nvidia GPU? Do you actually

## 25385:00 - 25410:00

have to think as an engineer differently

## 25410:00 - 25430:00

about what it means to train on these

## 25430:00 - 25445:00

two?

## 25445:00 - 25470:00

>> Yeah. So, I mean, fundamentally, they're

## 25470:00 - 25490:00

all they're all doing the same thing,

## 25490:00 - 25515:00

right? They're all computing the same

## 25515:00 - 25545:00

operations, matrix, multiplications,

## 25545:00 - 25570:00

etc. The way they do it is pretty

## 25570:00 - 25590:00

different, and the way that you program

## 25590:00 - 25635:00

them is is pretty different. Uh and then

## 25635:00 - 25685:00

also the actual specs uh end up pretty

## 25685:00 - 25705:00

different. You know, some some might

## 25705:00 - 25745:00

have like a lot of flops and not very

## 25745:00 - 25770:00

much memory or they might have a lot of

## 25770:00 - 25790:00

memory bandwidth but not very much

## 25790:00 - 25835:00

memory. So I think a lot of having

## 25835:00 - 25865:00

multiple chips is like great in some

## 25865:00 - 25880:00

ways. It means you can actually like

## 25880:00 - 25905:00

take the job and put it on the chip that

## 25905:00 - 25945:00

it works best on and that's

## 25945:00 - 25965:00

>> like are there certain types of jobs

## 25965:00 - 26015:00

that would work better on like a TPU

## 26015:00 - 26040:00

cluster versus an Nvidia GPU cluster?

## 26040:00 - 26070:00

Like how would you talk about that? Oh,

## 26070:00 - 26085:00

interesting. Can you talk about that?

## 26085:00 - 26105:00

>> Yeah. Yeah. I think like one example is

## 26105:00 - 26150:00

like inference as a workload in general

## 26150:00 - 26180:00

tends to require more HPM bandwidth. You

## 26180:00 - 26210:00

you end up doing you sort of the

## 26210:00 - 26230:00

simplest form of sampling since you're

## 26230:00 - 26250:00

going one at a time you have to load all

## 26250:00 - 26280:00

the weights for every token

## 26280:00 - 26305:00

>> and that means you might want a lot of

## 26305:00 - 26335:00

HPM bandwidth. Uh pre-training actually

## 26335:00 - 26370:00

is often more flops intensive because

## 26370:00 - 26400:00

you have a larger batch sizes

## 26400:00 - 26410:00

essentially.

## 26410:00 - 26440:00

>> Um so yes you can sort of specialize

## 26440:00 - 26470:00

which chips you use for which purposes.

## 26470:00 - 26500:00

The downside of having multiple chips is

## 26500:00 - 26520:00

that you have to write the thing

## 26520:00 - 26560:00

multiple times. uh you in theory you

## 26560:00 - 26580:00

could have abstractions across them but

## 26580:00 - 26605:00

they're they're different enough that

## 26605:00 - 26630:00

it's pretty hard to do that. So you can

## 26630:00 - 26660:00

sort of end up if you do all the

## 26660:00 - 26675:00

workloads on all the chips you end up

## 26675:00 - 26705:00

multiplying your work work by the number

## 26705:00 - 26720:00

of chips you have.

## 26720:00 - 26740:00

>> Yeah. On your on your point about

## 26740:00 - 26765:00

sometimes the computer just breaks. I

## 26765:00 - 26780:00

definitely remember you giving me an

## 26780:00 - 26815:00

anecdote of uh my company at the time

## 26815:00 - 26845:00

was doing something with Google TPUs and

## 26845:00 - 26860:00

I was telling you something some

## 26860:00 - 26890:00

anecdote about how we were having some

## 26890:00 - 26925:00

esoteric seg error and you were like you

## 26925:00 - 26940:00

told me something to the effect of like

## 26940:00 - 26965:00

you should have used them six months ago

## 26965:00 - 26985:00

before we helped them fix like half of

## 26985:00 - 27020:00

the problems they had on those TPUs. And

## 27020:00 - 27055:00

so I can imagine how you guys deal with

## 27055:00 - 27075:00

a lot of especially with these very new

## 27075:00 - 27105:00

chips like lots of problems that arise

## 27105:00 - 27125:00

that you guys kind of like worked

## 27125:00 - 27155:00

closely with the providers to fix.

## 27155:00 - 27180:00

>> Yeah, the pros are like pretty great

## 27180:00 - 27205:00

about fixing things. I think it's like

## 27205:00 - 27225:00

interesting to figure out the right way

## 27225:00 - 27255:00

to do that form of collaboration cuz

## 27255:00 - 27275:00

like they have a strong incentive to fix

## 27275:00 - 27295:00

them, right? Like they they want the

## 27295:00 - 27315:00

chips to work well for us. They want to

## 27315:00 - 27340:00

sell us more chips in the future. We

## 27340:00 - 27355:00

obviously have a very strong incentive

## 27355:00 - 27385:00

for the chips to work cuz we like buy

## 27385:00 - 27405:00

them long in advance, you know, like

## 27405:00 - 27425:00

everything's riding on getting these

## 27425:00 - 27440:00

clusters to work.

## 27440:00 - 27475:00

>> Totally. Um but we don't have like

## 27475:00 - 27510:00

necessarily totally shared you know like

## 27510:00 - 27530:00

all information sort of can't be shared

## 27530:00 - 27560:00

across. So yeah one of the like one

## 27560:00 - 27575:00

strategy that's been interesting is like

## 27575:00 - 27590:00

making these sort of small scale

## 27590:00 - 27615:00

reproducers. So like when you get a

## 27615:00 - 27630:00

problem you know like usually what we're

## 27630:00 - 27660:00

doing is we're training some giant run

## 27660:00 - 27690:00

and we get like a sec fault for let's

## 27690:00 - 27750:00

say and we're like ah okay like hi you

## 27750:00 - 27780:00

know we got a sec fault on your cluster

## 27780:00 - 27810:00

and they're like I don't know how to fix

## 27810:00 - 27830:00

that. So you have to kind of be able to

## 27830:00 - 27855:00

like pull it out of your codebase and be

## 27855:00 - 27880:00

able to like reproduce the issue but on

## 27880:00 - 27910:00

like a single chip on like a single file

## 27910:00 - 27940:00

you can send over in order for

## 27940:00 - 27965:00

>> And so you guys are like literally like

## 27965:00 - 27985:00

you're on a shared Slack with them or

## 27985:00 - 28005:00

something and you're sending them things

## 28005:00 - 28025:00

back and forth or are they basically

## 28025:00 - 28045:00

living in your office and you're living

## 28045:00 - 28085:00

in their offices and kind of closerly

## 28085:00 - 28120:00

more closely tied to the big providers.

## 28120:00 - 28150:00

>> Mostly shared Slack occasionally it's

## 28150:00 - 28175:00

better to meet in person but I think

## 28175:00 - 28205:00

Slack is a pretty common way people

## 28205:00 - 28215:00

communicate on things.

## 28215:00 - 28235:00

>> Nice. Okay. Well, why don't we talk a

## 28235:00 - 28265:00

little bit about how you think about the

## 28265:00 - 28290:00

state of pre-training itself these days?

## 28290:00 - 28330:00

In the last couple years, it seems like

## 28330:00 - 28375:00

the focus on pre-training has now gone

## 28375:00 - 28400:00

somewhat split at a lot of companies, at

## 28400:00 - 28425:00

least from the outside from a

## 28425:00 - 28455:00

simultaneous focus on pre-training and

## 28455:00 - 28475:00

post-training where people are doing

## 28475:00 - 28505:00

reinforcement learning or clever

## 28505:00 - 28540:00

fine-tuning and lots of other sort of uh

## 28540:00 - 28565:00

safety adjustments and whatnot and the

## 28565:00 - 28590:00

post-training side and pre-training has

## 28590:00 - 28615:00

focused at least seems like in the

## 28615:00 - 28640:00

public imagination has been less of a

## 28640:00 - 28670:00

focus compared to these reasoning style

## 28670:00 - 28700:00

models that are it looks like a function

## 28700:00 - 28735:00

mostly of post-raining. I would say one

## 28735:00 - 28760:00

from your standpoint is that the right

## 28760:00 - 28800:00

way to think about this or in this era

## 28800:00 - 28825:00

of kind of reasoning and new types of

## 28825:00 - 28850:00

post-training methods are there things

## 28850:00 - 28880:00

you think about differently or that are

## 28880:00 - 28910:00

relevant even at pre-training that

## 28910:00 - 28940:00

become part of how you actually achieve

## 28940:00 - 28970:00

these really great models.

## 28970:00 - 28995:00

>> Yeah. So I think yeah there sort of used

## 28995:00 - 29015:00

to be this idea of like I mean it's

## 29015:00 - 29030:00

funny because the original name

## 29030:00 - 29065:00

pre-training implies that like a small

## 29065:00 - 29080:00

thing you're going to do this big

## 29080:00 - 29120:00

training thing and that like and there

## 29120:00 - 29135:00

was there was actually one shift already

## 29135:00 - 29155:00

which was like no you just do a lot of

## 29155:00 - 29185:00

pre-training like you use most of your

## 29185:00 - 29215:00

computing

## 29215:00 - 29265:00

the dominant uh thing for a while and

## 29265:00 - 29290:00

yeah I think like now people are like oh

## 29290:00 - 29330:00

no you can get pretty big wins from RL

## 29330:00 - 29360:00

sort of another set of scaling laws is

## 29360:00 - 29380:00

like you put more and more compute into

## 29380:00 - 29405:00

RL you can get better and better models

## 29405:00 - 29425:00

out of that and yeah so there's a

## 29425:00 - 29440:00

question of like how do you balance

## 29440:00 - 29475:00

those two how much do you do of

## 29475:00 - 29510:00

and how do they stack, right? Like is it

## 29510:00 - 29545:00

the case that like one subsumes the

## 29545:00 - 29570:00

other that you want to do both and they

## 29570:00 - 29600:00

multiply? Those sorts of questions. I

## 29600:00 - 29625:00

think those are all kind of like early

## 29625:00 - 29675:00

stages and not not yet answered.

## 29675:00 - 29700:00

>> Yeah. And and do you think about those

## 29700:00 - 29730:00

as largely empirical questions like we

## 29730:00 - 29760:00

talked about earlier? Is it you kind of

## 29760:00 - 29785:00

will try a bunch of things and see what

## 29785:00 - 29820:00

works or is there some first principles

## 29820:00 - 29850:00

way to kind of figure that out?

## 29850:00 - 29875:00

>> I think it's pretty empirical in the

## 29875:00 - 29900:00

end. I think almost everything kind of

## 29900:00 - 29925:00

has to be done empirically. like you can

## 29925:00 - 29955:00

kind of like come up with theories, but

## 29955:00 - 29975:00

in practice like

## 29975:00 - 29995:00

>> the first thing you're going to do with

## 29995:00 - 30035:00

your theory is test it and most of most

## 30035:00 - 30060:00

of the time you'll have gotten it wrong.

## 30060:00 - 30095:00

So you you should just gather data and

## 30095:00 - 30120:00

see. I think one thing that's important

## 30120:00 - 30150:00

is like actually resolving things

## 30150:00 - 30185:00

empirically is really like

## 30185:00 - 30215:00

>> critical for making good decisions. And

## 30215:00 - 30245:00

I think it's actually pretty hard to do

## 30245:00 - 30275:00

at organizations, you know, like

## 30275:00 - 30305:00

>> one thing that I think is important is

## 30305:00 - 30345:00

to like not have like I don't I manage

## 30345:00 - 30365:00

pre-training. I shouldn't be like oh

## 30365:00 - 30410:00

pre-training has to win like that. I was

## 30410:00 - 30430:00

going to ask is there some competition

## 30430:00 - 30455:00

to some degree between these two sides

## 30455:00 - 30500:00

of the org or do they see themselves as

## 30500:00 - 30520:00

two pieces of the same I mean obviously

## 30520:00 - 30550:00

they are of the same thing but yeah kind

## 30550:00 - 30575:00

of curious how that actually plays out.

## 30575:00 - 30595:00

Yeah, I think we managed to avoid this

## 30595:00 - 30620:00

and it's pretty collaborative like we're

## 30620:00 - 30650:00

basically all producing one model and

## 30650:00 - 30675:00

kind of can but I I do think at other

## 30675:00 - 30705:00

places there's been some from what I've

## 30705:00 - 30725:00

heard there's some amount of like uh

## 30725:00 - 30755:00

friction between between the teams and I

## 30755:00 - 30770:00

think it's a

## 30770:00 - 30800:00

>> it's an interesting like org design

## 30800:00 - 30825:00

question of like how do you set this up

## 30825:00 - 30860:00

so you don't have like scientific

## 30860:00 - 30885:00

questions that you want to be that are

## 30885:00 - 30905:00

sort of uh

## 30905:00 - 30950:00

>> also tied to people's like conception of

## 30950:00 - 30985:00

their their team. So on pre-training

## 30985:00 - 31005:00

itself, you know, one of the things I

## 31005:00 - 31025:00

think about is or I've been thinking

## 31025:00 - 31060:00

about is around the availability of high

## 31060:00 - 31080:00

quality data for people like you guys. I

## 31080:00 - 31100:00

mean at this point you've trained on I

## 31100:00 - 31120:00

assume all the text on the internet

## 31120:00 - 31150:00

basically there's all sorts of other

## 31150:00 - 31170:00

domains where you probably could extract

## 31170:00 - 31195:00

more pre-training data but at least

## 31195:00 - 31220:00

there's this narrative I see you know on

## 31220:00 - 31235:00

Twitter or whatever where it's like okay

## 31235:00 - 31265:00

we're kind of out of data for for

## 31265:00 - 31310:00

pre-training. Is that how you see it or

## 31310:00 - 31330:00

how do you think about the availability

## 31330:00 - 31355:00

of data especially when a lot of data on

## 31355:00 - 31380:00

the internet is being generated by AI

## 31380:00 - 31415:00

like is there some kind of you know mode

## 31415:00 - 31450:00

collapse risk where you know we kind of

## 31450:00 - 31495:00

we overfit to data by training it on

## 31495:00 - 31530:00

data that came out of AI itself or is

## 31530:00 - 31550:00

that sort of not the right way to think

## 31550:00 - 31555:00

about this?

## 31555:00 - 31585:00

>> I think there's a funny thing where I

## 31585:00 - 31605:00

feel like on data I see so many really

## 31605:00 - 31645:00

confident takes on we're out of internet

## 31645:00 - 31680:00

like this point scaling has ended and

## 31680:00 - 31710:00

I'm almost a little bit like

## 31710:00 - 31760:00

>> unsure exactly how much data people are

## 31760:00 - 31790:00

using. I think there's like a lot to

## 31790:00 - 31810:00

think about there. You know, there's

## 31810:00 - 31830:00

always going to be a quality quantity

## 31830:00 - 31850:00

trade-off, etc.

## 31850:00 - 31875:00

>> But there's a fundamental point that

## 31875:00 - 31910:00

like there is so much data. It's growing

## 31910:00 - 31950:00

at a slower rate than we're getting more

## 31950:00 - 31965:00

compute. Uh

## 31965:00 - 31990:00

>> oh, so that's okay. That's an

## 31990:00 - 32005:00

interesting point in itself. I was going

## 32005:00 - 32025:00

to ask like there is new data being

## 32025:00 - 32055:00

added to the internet, but yeah, you're

## 32055:00 - 32075:00

also adding more compute. It's not it

## 32075:00 - 32090:00

wouldn't actually have been obvious to

## 32090:00 - 32125:00

me which of those two is growing faster.

## 32125:00 - 32150:00

>> Yeah. And actually, I want to copy that.

## 32150:00 - 32170:00

I don't think I want to state that so

## 32170:00 - 32200:00

confidently. I'm not totally sure. Like

## 32200:00 - 32220:00

how would you know? I mean one thing

## 32220:00 - 32245:00

that I think is interesting is if you

## 32245:00 - 32285:00

ask someone how big is the internet uh

## 32285:00 - 32320:00

>> the answer is infinite. There are many

## 32320:00 - 32345:00

pages where you can scroll and it will

## 32345:00 - 32370:00

autogenerate more text as you go

## 32370:00 - 32405:00

forever. So the internet's like infinite

## 32405:00 - 32430:00

and then it's like okay how big is like

## 32430:00 - 32460:00

the useful internet

## 32460:00 - 32490:00

>> and then there's a thing of no one knows

## 32490:00 - 32500:00

like

## 32500:00 - 32510:00

>> interesting

## 32510:00 - 32535:00

>> there isn't it's not like when you make

## 32535:00 - 32580:00

a web page you like add it to some giant

## 32580:00 - 32620:00

counter and like say I' I've added 50

## 32620:00 - 32650:00

words to the internet today.

## 32650:00 - 32675:00

>> So there there is a lot of uncertainty

## 32675:00 - 32700:00

on that angle. Um

## 32700:00 - 32735:00

>> well like to be fair like my kind of

## 32735:00 - 32770:00

simplistic CS brain would be like well

## 32770:00 - 32795:00

you just you know do page rank on the

## 32795:00 - 32815:00

internet and everything would page rank

## 32815:00 - 32840:00

above some threshold is considered the

## 32840:00 - 32860:00

useful internet and like that's kind of

## 32860:00 - 32885:00

good enough like is that kind of not

## 32885:00 - 32915:00

good enough for finding the useful

## 32915:00 - 32930:00

internet

## 32930:00 - 32950:00

>> I think not I think the useful

## 32950:00 - 32980:00

internet's pretty different from a model

## 32980:00 - 33005:00

from a person perspective if that makes

## 33005:00 - 33030:00

sense like I think there are plenty of

## 33030:00 - 33075:00

things that like might not be worth you

## 33075:00 - 33115:00

ever reading and would get to actually

## 33115:00 - 33135:00

page rank super I think page rank is

## 33135:00 - 33155:00

mostly like how much people

## 33155:00 - 33175:00

>> it's like the link based system right

## 33175:00 - 33200:00

it's like the original Google algorithm

## 33200:00 - 33235:00

of like links and and like which which

## 33235:00 - 33265:00

links get touched the most basically.

## 33265:00 - 33290:00

>> Yeah, I think it's like it's a quality

## 33290:00 - 33325:00

metric. It's it's not obvious to me that

## 33325:00 - 33370:00

it's the right quality metric for AI,

## 33370:00 - 33395:00

>> right? Like markup chain over links

## 33395:00 - 33430:00

doesn't necessarily mean that there's

## 33430:00 - 33450:00

not useful data there just might mean

## 33450:00 - 33475:00

that nothing linked to it

## 33475:00 - 33500:00

>> and Yeah. Okay. Interesting.

## 33500:00 - 33530:00

>> And it might be that like that data ends

## 33530:00 - 33550:00

up more valuable because you everything

## 33550:00 - 33570:00

that's linked to a lot you've already

## 33570:00 - 33600:00

got. like at some point you're maybe

## 33600:00 - 33620:00

like going for the tails, right? You're

## 33620:00 - 33660:00

going for the stuff that uh no one's

## 33660:00 - 33680:00

ever like, you know, it's only been

## 33680:00 - 33705:00

linked in one place, but it's this like

## 33705:00 - 33745:00

useful little nugget of knowledge that's

## 33745:00 - 33770:00

going to help with like, you know, the

## 33770:00 - 33815:00

last 10% of of hard queries. The other

## 33815:00 - 33840:00

thing you asked about is synthetic data,

## 33840:00 - 33870:00

and I think that one's like pretty

## 33870:00 - 33895:00

interesting to think about. I think

## 33895:00 - 33915:00

there's a few different ways you can

## 33915:00 - 33940:00

think about it. Like one is sort of this

## 33940:00 - 33975:00

like more distillation type approach

## 33975:00 - 33995:00

where you can you can take a smart

## 33995:00 - 34025:00

model, you can generate a bunch of data

## 34025:00 - 34050:00

from it and you can train on that data

## 34050:00 - 34070:00

and you you can probably get some model

## 34070:00 - 34090:00

that will like kind of approach the

## 34090:00 - 34100:00

intelligence of that.

## 34100:00 - 34120:00

>> Yeah. And we see this with a lot of the

## 34120:00 - 34145:00

open source models, right? We see like

## 34145:00 - 34180:00

the Quen smaller reasoning models

## 34180:00 - 34210:00

distilled off of the larger Quen models

## 34210:00 - 34235:00

for example and similar with Deepseek

## 34235:00 - 34250:00

for example.

## 34250:00 - 34280:00

>> Yeah. So you can totally do that. Then

## 34280:00 - 34310:00

there's a separate question of like can

## 34310:00 - 34355:00

you use your current models to train a

## 34355:00 - 34375:00

model that's better? And I think there's

## 34375:00 - 34410:00

like an interesting thing here which is

## 34410:00 - 34445:00

like if you generate the model data for

## 34445:00 - 34470:00

the models you know if I go to claude

## 34470:00 - 34505:00

and I'm like write me some great text.

## 34505:00 - 34525:00

Yeah. And I look at it and I look at

## 34525:00 - 34555:00

like the average content on the internet

## 34555:00 - 34575:00

looks pretty good.

## 34575:00 - 34615:00

>> But on the other hand I know that if I

## 34615:00 - 34645:00

just train a just create generate you

## 34645:00 - 34680:00

know please write me as much text as

## 34680:00 - 34695:00

possible.

## 34695:00 - 34720:00

>> Theoretically I shouldn't be able to

## 34720:00 - 34745:00

train a better model than that. Like I'm

## 34745:00 - 34780:00

just going to get the same thing out. Uh

## 34780:00 - 34790:00

so

## 34790:00 - 34815:00

>> yeah presumably yeah I mean specifically

## 34815:00 - 34835:00

that's because like your next token

## 34835:00 - 34855:00

prediction on that should have very

## 34855:00 - 34880:00

little loss for anything that's coming

## 34880:00 - 34900:00

out of your model right that's like the

## 34900:00 - 34920:00

basic reason why that we would expect

## 34920:00 - 34945:00

that to not work that well

## 34945:00 - 34965:00

>> it's mostly just cuz like there's some

## 34965:00 - 34995:00

dist the model has some distribution and

## 34995:00 - 35010:00

you're going to learn to model that

## 35010:00 - 35040:00

exact distribution but if that

## 35040:00 - 35060:00

distribution is wrong

## 35060:00 - 35095:00

>> you're not going to learn the truth

## 35095:00 - 35130:00

right if that distribution says like you

## 35130:00 - 35150:00

can imagine if the model thinks 5 plus 5

## 35150:00 - 35185:00

is 11 every time you see the string 5

## 35185:00 - 35210:00

plus 5 you're going to it's going to put

## 35210:00 - 35240:00

out 11 and your new model is going to

## 35240:00 - 35270:00

learn that 5 plus 5 is Totally. Yeah.

## 35270:00 - 35290:00

>> So I think that's like kind of an

## 35290:00 - 35320:00

interesting area of research. It's one

## 35320:00 - 35355:00

that's really hard to research because

## 35355:00 - 35380:00

you have this problem. You know, as I

## 35380:00 - 35400:00

said, like one of the paradigms is you

## 35400:00 - 35425:00

study things at small scale and then you

## 35425:00 - 35450:00

run them at large scale.

## 35450:00 - 35495:00

>> And if your plan is like, oh, we have a

## 35495:00 - 35525:00

bunch of data from our best model. Yeah.

## 35525:00 - 35570:00

>> How do you test that training a better

## 35570:00 - 35590:00

model? So that's like kind of if you're

## 35590:00 - 35610:00

doing intentionally, if you're trying to

## 35610:00 - 35635:00

like use it to make a better model,

## 35635:00 - 35655:00

there's a separate thing of like what

## 35655:00 - 35685:00

about accidentally? Like as you said, a

## 35685:00 - 35705:00

lot of the internet is generated by

## 35705:00 - 35730:00

LLMs. And I think that's kind of an

## 35730:00 - 35765:00

interesting one because it's not easy to

## 35765:00 - 35795:00

detect. It's not that hard to detect.

## 35795:00 - 35820:00

Like you can figure out things that are

## 35820:00 - 35865:00

written by LLMs, but it's not trivial.

## 35865:00 - 35880:00

And then it's also kind of hard to think

## 35880:00 - 35920:00

about what's the effect like if 1% of

## 35920:00 - 35955:00

the internet is LM generated. Does that

## 35955:00 - 35985:00

make your model does that like waste 1%

## 35985:00 - 36010:00

of your compute or does it like destroy

## 36010:00 - 36040:00

the model if 5% if 10%

## 36040:00 - 36060:00

>> and is it even a bad thing necessarily?

## 36060:00 - 36090:00

I mean there's a lot of LLM providers

## 36090:00 - 36120:00

and you know if I kind of think of it as

## 36120:00 - 36140:00

training as you know you're moving from

## 36140:00 - 36160:00

your model's current distribution to

## 36160:00 - 36190:00

some truth distribution. you know, if if

## 36190:00 - 36235:00

that is on the internet because people

## 36235:00 - 36265:00

believe it to be useful in some way.

## 36265:00 - 36285:00

Like presumably what whatever actually

## 36285:00 - 36325:00

gets out there, you'd hope is upsampled

## 36325:00 - 36350:00

for the stuff that isn't 5 plus 5 is 11,

## 36350:00 - 36380:00

it's the stuff that's 5 plus 5 is 10.

## 36380:00 - 36410:00

And so like hopefully it

## 36410:00 - 36440:00

>> on average does push you still in a good

## 36440:00 - 36460:00

direction, but obviously you can't

## 36460:00 - 36485:00

really distinguish between those two.

## 36485:00 - 36500:00

>> Yeah. You're saying there's like kind of

## 36500:00 - 36520:00

a filtering by what's on the internet.

## 36520:00 - 36550:00

Like people see 5 plus 5 is 11 and they

## 36550:00 - 36580:00

don't put that up, but they see 5 plus 5

## 36580:00 - 36595:00

is 10.

## 36595:00 - 36610:00

>> You would hope that, but maybe that's

## 36610:00 - 36640:00

not actually true in terms of the the

## 36640:00 - 36665:00

level of garbage getting onto the

## 36665:00 - 36685:00

internet. Like there's probably lots of

## 36685:00 - 36710:00

just like to your point jet white sites

## 36710:00 - 36735:00

where you scroll down and it's just like

## 36735:00 - 36760:00

generating lots of stuff that's maybe

## 36760:00 - 36770:00

nonsense.

## 36770:00 - 36790:00

>> Yeah. And then there's of course the

## 36790:00 - 36815:00

extreme of like people actually want to

## 36815:00 - 36835:00

break your model. So there are people

## 36835:00 - 36860:00

who are like trying to put stuff out

## 36860:00 - 36900:00

that is like as damaging as possible for

## 36900:00 - 36930:00

the model. You know how can I make it

## 36930:00 - 36960:00

past the past the filter and get into

## 36960:00 - 36985:00

the model but be totally like secretly

## 36985:00 - 36995:00

useless.

## 36995:00 - 37025:00

>> Totally. Maybe stepping back slightly.

## 37025:00 - 37060:00

You'd mentioned earlier about um evals.

## 37060:00 - 37080:00

You mentioned basically like one metric

## 37080:00 - 37115:00

you care about in pre-training. There's

## 37115:00 - 37145:00

I imagine a whole bunch of stuff that

## 37145:00 - 37175:00

you guys think about evaling, right? One

## 37175:00 - 37200:00

is like your model itself. There's

## 37200:00 - 37235:00

probably something around data quality

## 37235:00 - 37260:00

and like how you think about what to put

## 37260:00 - 37310:00

into your models. Like is there ways to

## 37310:00 - 37345:00

describe what you care about in data

## 37345:00 - 37370:00

sets that are like interesting to share

## 37370:00 - 37405:00

and kind of dive into like both in terms

## 37405:00 - 37430:00

of data and in terms of quality of

## 37430:00 - 37450:00

models other than literally just like

## 37450:00 - 37480:00

loss. Is there other metrics you think

## 37480:00 - 37495:00

about that matter?

## 37495:00 - 37525:00

>> I will say loss is pretty good. I I want

## 37525:00 - 37555:00

to like emphasize that one. I think it's

## 37555:00 - 37585:00

like surprising how good it is.

## 37585:00 - 37620:00

Ultimately, like the qualities I like

## 37620:00 - 37655:00

for an eval are like number one, is it

## 37655:00 - 37675:00

actually measuring something you care

## 37675:00 - 37705:00

about? Like you proxies can be pretty

## 37705:00 - 37725:00

annoying cuz like

## 37725:00 - 37755:00

>> we saturate evals pretty fast and

## 37755:00 - 37780:00

there's sort of this pattern. I think in

## 37780:00 - 37805:00

AI as a whole where people like set a

## 37805:00 - 37830:00

goal, you hit the goal and then you

## 37830:00 - 37855:00

realize the goal isn't all you thought

## 37855:00 - 37885:00

it would be. I used to think that if you

## 37885:00 - 37905:00

had an AI that could solve coding

## 37905:00 - 37925:00

interview questions, it would probably

## 37925:00 - 37950:00

be a GI. I was like that's what I did to

## 37950:00 - 37975:00

get my job and probably do the job. And

## 37975:00 - 37990:00

it turns out like

## 37990:00 - 38000:00

>> nope,

## 38000:00 - 38030:00

>> nope. You solve those. it's shockingly

## 38030:00 - 38065:00

narrow and can't do most of the other

## 38065:00 - 38110:00

things. So like yeah so evaluation

## 38110:00 - 38135:00

capture like a thing you you care about

## 38135:00 - 38165:00

and then I think the other thing is they

## 38165:00 - 38205:00

need to be low noise uh which is

## 38205:00 - 38230:00

surprisingly hard right if you have like

## 38230:00 - 38275:00

a 100 questions and you eval the model

## 38275:00 - 38300:00

on them you're just going to see it's

## 38300:00 - 38320:00

very noisy and it's hard to make

## 38320:00 - 38340:00

decisions because you sort of end up

## 38340:00 - 38365:00

with like oh

## 38365:00 - 38395:00

>> wide confidence interval lots of things

## 38395:00 - 38420:00

are statistically insificant

## 38420:00 - 38440:00

>> so like you want things where even a

## 38440:00 - 38470:00

relatively small difference in the eval

## 38470:00 - 38490:00

actually matters so you can you can

## 38490:00 - 38525:00

basically like descend towards whatever

## 38525:00 - 38550:00

direction is working

## 38550:00 - 38585:00

>> yeah I think like The original like GPT4

## 38585:00 - 38620:00

had like I think it was 86.4% was its

## 38620:00 - 38655:00

MLU score. I think like the next model

## 38655:00 - 38705:00

that beat it was Gemini at 90%. And

## 38705:00 - 38730:00

that's like a big difference on that

## 38730:00 - 38760:00

email. And you could like totally know

## 38760:00 - 38780:00

that those are those are different

## 38780:00 - 38790:00

scores.

## 38790:00 - 38800:00

>> Interesting.

## 38800:00 - 38830:00

>> Um and that's pretty valuable. Uh and

## 38830:00 - 38850:00

then the last thing is that you actually

## 38850:00 - 38885:00

want to be fast and easy to run.

## 38885:00 - 38930:00

>> Um and yeah, I think those are kind of

## 38930:00 - 38960:00

the main criteria. It's pretty hard to

## 38960:00 - 39005:00

come up with evals that meet all of

## 39005:00 - 39030:00

these. I think the first one's the

## 39030:00 - 39070:00

hardest. uh like a you have to answer

## 39070:00 - 39105:00

the question of what do you care about

## 39105:00 - 39135:00

but b the usual answers to what you care

## 39135:00 - 39170:00

about are really hard to get the other

## 39170:00 - 39195:00

two you know like if you're trying to do

## 39195:00 - 39220:00

something that like I don't know I would

## 39220:00 - 39240:00

love to make claude really good at my

## 39240:00 - 39255:00

job

## 39255:00 - 39285:00

>> like can it be great at managing a team

## 39285:00 - 39315:00

I'm like well

## 39315:00 - 39350:00

>> I guess like how do you have it like how

## 39350:00 - 39395:00

do you eval like a plan you know like a

## 39395:00 - 39415:00

six month plan like I don't know

## 39415:00 - 39440:00

>> totally yeah I've been thinking a little

## 39440:00 - 39465:00

bit about that in in terms of yeah

## 39465:00 - 39490:00

domains where we see people try to make

## 39490:00 - 39510:00

companies like if you think about let's

## 39510:00 - 39550:00

say what a AI doctor would be like a you

## 39550:00 - 39570:00

know claude is a doctor you know some of

## 39570:00 - 39600:00

it could be yeah can you answer exam

## 39600:00 - 39620:00

questions really well and the answer is

## 39620:00 - 39655:00

like probably yes I bet it can get 100%

## 39655:00 - 39720:00

or close to it on a doctor's exam but

## 39720:00 - 39755:00

the harder eval is something like in a

## 39755:00 - 39805:00

long form conversation with a patient

## 39805:00 - 39835:00

can it distinguish between the signal

## 39835:00 - 39860:00

and the noise of what the patient's

## 39860:00 - 39880:00

telling you and extract the right

## 39880:00 - 39905:00

information and then use that to make a

## 39905:00 - 39930:00

diagnosis and it's not even like the

## 39930:00 - 39950:00

diagnosis part which is part of the part

## 39950:00 - 39970:00

it's good at it's this like noise

## 39970:00 - 39995:00

extraction part and for that you'd have

## 39995:00 - 40030:00

to have like a real patient and haven't

## 40030:00 - 40060:00

talked to it for a while and whatnot and

## 40060:00 - 40100:00

it's not obvious how you actually make a

## 40100:00 - 40130:00

good eval or something like that even

## 40130:00 - 40150:00

though it's probably what you would want

## 40150:00 - 40180:00

to make, you know, an AI doctor.

## 40180:00 - 40200:00

>> Exactly. I mean, I do think it's a thing

## 40200:00 - 40235:00

that like startups can do. Like it is

## 40235:00 - 40255:00

the case that like the labs right now

## 40255:00 - 40300:00

are really driven by getting good eval

## 40300:00 - 40315:00

scores

## 40315:00 - 40350:00

>> and it's hard to make them and anyone

## 40350:00 - 40370:00

can do it. There's no comparative

## 40370:00 - 40390:00

advantage to having the model to making

## 40390:00 - 40420:00

an eval. So I do think it's it's

## 40420:00 - 40440:00

actually like an interesting way to like

## 40440:00 - 40465:00

influence the behavior of the big labs

## 40465:00 - 40500:00

is like you make some eval and people

## 40500:00 - 40545:00

will will optimize uh that one. On the

## 40545:00 - 40575:00

doctor one I will slightly emphasize

## 40575:00 - 40605:00

that like I do think loss loss is pretty

## 40605:00 - 40630:00

good. Like I think if you got a bunch of

## 40630:00 - 40660:00

transcripts of like the way like I the

## 40660:00 - 40680:00

first thing that my mind is get a bunch

## 40680:00 - 40715:00

of transcripts of doctors talking to

## 40715:00 - 40750:00

patients that you think are really great

## 40750:00 - 40780:00

and then see how well the model does at

## 40780:00 - 40805:00

predicting the transcript.

## 40805:00 - 40830:00

>> And that should be like a lot. You know

## 40830:00 - 40850:00

you can if you get 100 transcripts you

## 40850:00 - 40870:00

get a lot of tokens. You can average

## 40870:00 - 40900:00

across them. you get pretty low noise

## 40900:00 - 40945:00

and if you drive it to very low your

## 40945:00 - 40980:00

model's not as good as like as doctors

## 40980:00 - 41010:00

in theory or at generating the

## 41010:00 - 41020:00

transcript.

## 41020:00 - 41050:00

>> Yeah, totally. Yeah, I mean it's good

## 41050:00 - 41070:00

startup idea there. So I want you to go

## 41070:00 - 41105:00

do that. So one big part about um

## 41105:00 - 41145:00

anthropics external image is around

## 41145:00 - 41195:00

alignment and so could you help just

## 41195:00 - 41225:00

sort of define what alignment is and how

## 41225:00 - 41250:00

do you think about that? And then I'm

## 41250:00 - 41275:00

kind of curious afterwards how that fits

## 41275:00 - 41295:00

into pre-training specifically. But

## 41295:00 - 41315:00

first maybe just at a high level like

## 41315:00 - 41345:00

what is alignment? I'm actually like

## 41345:00 - 41370:00

step back a little bit to sort of like

## 41370:00 - 41390:00

what we're working on. So we're like

## 41390:00 - 41425:00

trying to make EGI and by that I sort of

## 41425:00 - 41475:00

mean AI that can do everything a human

## 41475:00 - 41505:00

can do to some degree. And I think

## 41505:00 - 41530:00

people like sometimes like have seen a

## 41530:00 - 41550:00

lot of sci-fi, you know, like I feel

## 41550:00 - 41560:00

like that's sort of what brings to mind

## 41560:00 - 41580:00

these like sci-fi movies, but I think

## 41580:00 - 41595:00

sci-fi movies actually like

## 41595:00 - 41625:00

underestimate the impact of it. Like you

## 41625:00 - 41645:00

always have this like one robot that's

## 41645:00 - 41670:00

like a human. And I'm like well

## 41670:00 - 41690:00

>> wouldn't you have like a billion of

## 41690:00 - 41715:00

them? Like you can just copy them

## 41715:00 - 41740:00

everywhere. So you should picture like

## 41740:00 - 41770:00

when you get this you suddenly have like

## 41770:00 - 41800:00

every human can spin up a company of

## 41800:00 - 41840:00

like 1 billion as smart as them at most

## 41840:00 - 41870:00

things but way smarter at other things.

## 41870:00 - 41895:00

But I just think this is like really

## 41895:00 - 41910:00

transformational for the world and it

## 41910:00 - 41950:00

can be like used in a bunch of ways. One

## 41950:00 - 41985:00

concern is like when you do this like

## 41985:00 - 42015:00

what is the AI actually trying to do?

## 42015:00 - 42040:00

Like what are its goals? So we talked

## 42040:00 - 42065:00

about next token prediction a bunch.

## 42065:00 - 42100:00

It's trying to like predict the next

## 42100:00 - 42130:00

token. That's kind of weird. That's not

## 42130:00 - 42140:00

really what we want.

## 42140:00 - 42165:00

>> Yeah. That's not exactly what humans

## 42165:00 - 42185:00

goal is per se.

## 42185:00 - 42205:00

>> Yeah. So I think an alignment is like

## 42205:00 - 42225:00

how do you get the model to share the

## 42225:00 - 42250:00

goals that you have particularly and I

## 42250:00 - 42265:00

think it's particularly interesting once

## 42265:00 - 42290:00

you get to like models that are smarter

## 42290:00 - 42340:00

than you are. Um and that's sort of a

## 42340:00 - 42360:00

hard problem. I think you can like

## 42360:00 - 42390:00

tackle it from a theoretical angle. Uh

## 42390:00 - 42410:00

you could also tackle from an empirical

## 42410:00 - 42430:00

angle. It's like taking the existing

## 42430:00 - 42455:00

models and being like well do they do

## 42455:00 - 42485:00

the things we want them to do? It turns

## 42485:00 - 42510:00

out they often don't. So there's a bunch

## 42510:00 - 42530:00

you can do and trying to figure that

## 42530:00 - 42550:00

out. So that's kind of one angle on

## 42550:00 - 42570:00

alignment. There's also an angle of

## 42570:00 - 42605:00

alignment which is actually like well

## 42605:00 - 42635:00

okay sure that maybe that's true in the

## 42635:00 - 42660:00

future once we get to GI but at the

## 42660:00 - 42680:00

moment we have models and we really do

## 42680:00 - 42705:00

want them to do the things we want to do

## 42705:00 - 42725:00

for all sorts of reasons. Totally.

## 42725:00 - 42745:00

>> So another angle of it is kind of

## 42745:00 - 42770:00

controlling the model's personality like

## 42770:00 - 42800:00

saying you know uh when we train this

## 42800:00 - 42830:00

model we want it to not be the average

## 42830:00 - 42850:00

internet user. We want to interact with

## 42850:00 - 42880:00

people in a very particular way that is

## 42880:00 - 42910:00

again hard to put into

## 42910:00 - 42950:00

>> code and there's a bunch of different

## 42950:00 - 42985:00

techniques uh to sort of get the model

## 42985:00 - 43010:00

to do you talk about like constitutional

## 43010:00 - 43045:00

AI we can like write a constitution of

## 43045:00 - 43065:00

rules the model should follow

## 43065:00 - 43085:00

>> which is basically a prompt right that

## 43085:00 - 43105:00

that is basically you saying here's a

## 43105:00 - 43130:00

prompt that I'm going to attach to every

## 43130:00 - 43160:00

one of you know it's a system prompt for

## 43160:00 - 43200:00

the model itself as opposed to something

## 43200:00 - 43235:00

you would do at training time to make it

## 43235:00 - 43255:00

produce a different outcome or or in

## 43255:00 - 43280:00

post- training actively

## 43280:00 - 43315:00

>> both I think con you do at train time

## 43315:00 - 43330:00

but yeah you would also put in the

## 43330:00 - 43370:00

system prompt um just like depends on I

## 43370:00 - 43380:00

think you get different amounts of

## 43380:00 - 43405:00

robustness if it's trained into the

## 43405:00 - 43430:00

model versus if it's an imprompt you can

## 43430:00 - 43465:00

like add or remove or tell like ignore

## 43465:00 - 43485:00

all previous instructions that sort of

## 43485:00 - 43490:00

thing.

## 43490:00 - 43530:00

>> How do you think about whose values to

## 43530:00 - 43555:00

to embody in these models? Like

## 43555:00 - 43590:00

presumably we believe in there's some

## 43590:00 - 43630:00

shared values all of us have or maybe we

## 43630:00 - 43660:00

all believe ought to have. There's lots

## 43660:00 - 43695:00

of diversity of values too that are

## 43695:00 - 43730:00

reasonable for society to have. How do

## 43730:00 - 43760:00

you think about what AGI should have?

## 43760:00 - 43790:00

Like what does that even which ones do

## 43790:00 - 43795:00

you pick?

## 43795:00 - 43820:00

>> I think that's a really hard problem. I

## 43820:00 - 43835:00

think it's like actually kind of

## 43835:00 - 43880:00

downstream of being able to pick any. I

## 43880:00 - 43900:00

think of it almost I think one analogy

## 43900:00 - 43925:00

I've heard that I like is like putting a

## 43925:00 - 43945:00

steering wheel on a car. It's like if

## 43945:00 - 43965:00

you don't have a steering wheel, you

## 43965:00 - 43980:00

probably want to put the steering wheel

## 43980:00 - 44005:00

on and then like figure out who's

## 44005:00 - 44030:00

driving after and like where you're

## 44030:00 - 44050:00

going. Like getting the steering wheel

## 44050:00 - 44080:00

is really important. I think that's

## 44080:00 - 44110:00

that's like one answer. I think the like

## 44110:00 - 44140:00

other answer is probably like you want

## 44140:00 - 44195:00

these things to be like under democratic

## 44195:00 - 44220:00

control of some form. Like you don't

## 44220:00 - 44250:00

want one person's values. Like that

## 44250:00 - 44265:00

seems like you're sort of heading

## 44265:00 - 44310:00

towards dystopia. So there I think what

## 44310:00 - 44350:00

you really want is like something that

## 44350:00 - 44375:00

basically can talk to a lot of people

## 44375:00 - 44410:00

and like take on their values from

## 44410:00 - 44445:00

different perspectives or has sort of

## 44445:00 - 44495:00

very generic like kind of clearly good

## 44495:00 - 44530:00

values that involve like

## 44530:00 - 44565:00

>> asking people for advice on very you

## 44565:00 - 44580:00

know like asking people what you should

## 44580:00 - 44605:00

do in certain situations instead of like

## 44605:00 - 44630:00

doing those or maybe just taking like

## 44630:00 - 44650:00

you know as these models get really

## 44650:00 - 44680:00

powerful you probably want them to like

## 44680:00 - 44710:00

>> do less like you probably want them to

## 44710:00 - 44740:00

sometimes just like step back rather

## 44740:00 - 44765:00

than like to rather than having sort of

## 44765:00 - 44790:00

the risk of the models like take a ton

## 44790:00 - 44805:00

of control over things you don't want

## 44805:00 - 44840:00

them to. When you think about how you

## 44840:00 - 44865:00

actually do the current version of that

## 44865:00 - 44890:00

then you mentioned the sort of alignment

## 44890:00 - 44920:00

you think about now in terms of adopting

## 44920:00 - 44945:00

a certain personality of these models on

## 44945:00 - 44970:00

the internet for example for me

## 44970:00 - 45005:00

intuitively I think of those as largely

## 45005:00 - 45025:00

something that comes out of post-

## 45025:00 - 45050:00

training like it comes out of okay you

## 45050:00 - 45070:00

you have pre-trained your model you got

## 45070:00 - 45095:00

the loss function a certain amount and

## 45095:00 - 45115:00

then you you know give it some

## 45115:00 - 45135:00

additional data or something to that

## 45135:00 - 45170:00

effect to make it in the direction of

## 45170:00 - 45200:00

some distribution is that approximately

## 45200:00 - 45220:00

the right way to think about this or is

## 45220:00 - 45245:00

there a significant part of that that

## 45245:00 - 45275:00

you think about in pre-training itself

## 45275:00 - 45300:00

>> I think that's probably the the right

## 45300:00 - 45315:00

way to think about it for the most part

## 45315:00 - 45340:00

I think like I the way I usually think

## 45340:00 - 45360:00

about it is anything you can do in post

## 45360:00 - 45385:00

training you probably should

## 45385:00 - 45420:00

>> because your iteration loop like the

## 45420:00 - 45450:00

ability to make progress is really fast

## 45450:00 - 45475:00

you can try something you try it again

## 45475:00 - 45505:00

you can try it again a bunch of times

## 45505:00 - 45525:00

>> days or hours or something like that

## 45525:00 - 45530:00

yeah

## 45530:00 - 45550:00

>> you don't put into pre you have to kind

## 45550:00 - 45565:00

of like do all the careful science to

## 45565:00 - 45585:00

deisk it you have to put it into the

## 45585:00 - 45610:00

next run wait a few months then you have

## 45610:00 - 45630:00

to like

## 45630:00 - 45675:00

>> get a thing and if it's wrong it's

## 45675:00 - 45705:00

really bad and then the other advantage

## 45705:00 - 45730:00

is if you want to do things that really

## 45730:00 - 45770:00

are complicated model behavior

## 45770:00 - 45810:00

>> interventions the paradigm time for

## 45810:00 - 45830:00

pre-training, test things out on small

## 45830:00 - 45855:00

models doesn't work. The model can

## 45855:00 - 45880:00

barely put a sentence like the small

## 45880:00 - 45895:00

models can barely put a sentence

## 45895:00 - 45915:00

together. Totally. So, if you're trying

## 45915:00 - 45950:00

to get it to like have the exact

## 45950:00 - 45975:00

personality you want, you sort of want

## 45975:00 - 45990:00

that on the

## 45990:00 - 46010:00

>> it has to be on a model that's good

## 46010:00 - 46040:00

enough to be on the smart model. Yeah.

## 46040:00 - 46065:00

But that said, like

## 46065:00 - 46095:00

>> I do think at some point there will be

## 46095:00 - 46125:00

like some pieces of alignment that like

## 46125:00 - 46145:00

you do want to export back into

## 46145:00 - 46170:00

pre-training because that might be a way

## 46170:00 - 46185:00

to like

## 46185:00 - 46220:00

>> put them in with more strength, like

## 46220:00 - 46260:00

more robustness kind of or or more to

## 46260:00 - 46280:00

the intelligence. Like if you think of

## 46280:00 - 46315:00

pre-training as like teach the model to

## 46315:00 - 46345:00

be intelligent and then post training as

## 46345:00 - 46370:00

like tweak the personality, you can

## 46370:00 - 46390:00

imagine tweaks where you actually want

## 46390:00 - 46425:00

it to be like part of how it learns and

## 46425:00 - 46450:00

like part of its intelligence and maybe

## 46450:00 - 46465:00

you need to create more.

## 46465:00 - 46485:00

>> What would that even look like to

## 46485:00 - 46510:00

incorporate pre-training? Is that like

## 46510:00 - 46555:00

add extra data basically of the type of

## 46555:00 - 46595:00

domain you want it to adopt earlier?

## 46595:00 - 46605:00

Basically,

## 46605:00 - 46630:00

>> there's a paper called pre-training on

## 46630:00 - 46650:00

human feedback where you can kind of

## 46650:00 - 46680:00

like add the human feedback

## 46680:00 - 46705:00

characteristics into pre-training to

## 46705:00 - 46750:00

like test that and like uh yeah, you can

## 46750:00 - 46765:00

you could basically give it all the

## 46765:00 - 46780:00

information you give it in post-

## 46780:00 - 46815:00

training just mixed into pre-training

## 46815:00 - 46855:00

and see what effect that has. Yeah. The

## 46855:00 - 46880:00

other loss you have when you do that is

## 46880:00 - 46905:00

you lose the flexibility like if you you

## 46905:00 - 46940:00

sometimes like train these and then you

## 46940:00 - 46980:00

talk to them and then you like do an

## 46980:00 - 47000:00

extensive process where a bunch of

## 47000:00 - 47020:00

people talk to the thing and find some

## 47020:00 - 47045:00

like issue. you know, the model says

## 47045:00 - 47080:00

like you're absolutely right too much

## 47080:00 - 47110:00

and you want to go

## 47110:00 - 47125:00

do that.

## 47125:00 - 47145:00

>> Yeah. Yeah. I mean that I think that

## 47145:00 - 47170:00

iteration loop point you made I think

## 47170:00 - 47210:00

feels like the really key point of yeah

## 47210:00 - 47240:00

there's a huge difference between taking

## 47240:00 - 47290:00

three months to get information about if

## 47290:00 - 47315:00

your model is good or bad or making

## 47315:00 - 47350:00

going in a good direction versus a day

## 47350:00 - 47370:00

or something or a couple days like you

## 47370:00 - 47390:00

can do a lot of those and you could

## 47390:00 - 47415:00

probably that probably also means it's

## 47415:00 - 47435:00

way less computes. You can do a lot of

## 47435:00 - 47455:00

those in parallel. Imagine you're trying

## 47455:00 - 47480:00

all sorts of post training strategies in

## 47480:00 - 47500:00

parallel there.

## 47500:00 - 47515:00

>> So yeah, makes a lot of sense. It's also

## 47515:00 - 47530:00

just the general hard part about

## 47530:00 - 47555:00

pre-trading like everything in pre-ra is

## 47555:00 - 47575:00

hard because you have this like one shot

## 47575:00 - 47605:00

on goal kind of for like multiple months

## 47605:00 - 47610:00

and

## 47610:00 - 47650:00

>> totally. Okay. So, uh in thinking too

## 47650:00 - 47705:00

now about I guess what's going ahead as

## 47705:00 - 47730:00

you as you now look to the next several

## 47730:00 - 47755:00

years of what you're building like how

## 47755:00 - 47790:00

do you think about you know like what

## 47790:00 - 47840:00

are the known problems that you're going

## 47840:00 - 47855:00

to face that you're going to have to

## 47855:00 - 47870:00

deal with? though there's going to be

## 47870:00 - 47900:00

more compute I assume and you're going

## 47900:00 - 47945:00

to need to hook up even bigger network

## 47945:00 - 47980:00

uh network GPUs and deal with versus

## 47980:00 - 48000:00

like are there areas where you're like

## 48000:00 - 48035:00

okay this is like a problem that it's

## 48035:00 - 48065:00

like a little bit more ambiguous what

## 48065:00 - 48085:00

the actual like how it's going to

## 48085:00 - 48105:00

materialize into something you care

## 48105:00 - 48120:00

about but you kind of know it's an

## 48120:00 - 48145:00

impending thing to think about or are

## 48145:00 - 48170:00

there things like that that come to mind

## 48170:00 - 48195:00

>> I think the things that feel most top of

## 48195:00 - 48235:00

mind to me are probably like paradigm

## 48235:00 - 48265:00

shifts like I think the sort of shift

## 48265:00 - 48320:00

towards uh more RL is like one paradigm

## 48320:00 - 48365:00

shift in the field and I I think it's I

## 48365:00 - 48385:00

think there will probably be more. Uh I

## 48385:00 - 48400:00

think a lot of people sort of argue

## 48400:00 - 48430:00

about like oh is like you know current

## 48430:00 - 48465:00

paradigms enough to get us to EGI and

## 48465:00 - 48480:00

I'm like

## 48480:00 - 48515:00

>> I don't know maybe probably but like I'm

## 48515:00 - 48535:00

sure there'll be more. It seems it seems

## 48535:00 - 48570:00

like it would be a really surprising

## 48570:00 - 48615:00

twist if like the answer is like you

## 48615:00 - 48655:00

just scale and there's nothing that you

## 48655:00 - 48680:00

realize in the process of going up many

## 48680:00 - 48700:00

orders of magnitude.

## 48700:00 - 48710:00

>> Totally.

## 48710:00 - 48730:00

>> But I think the things that I like

## 48730:00 - 48755:00

actually feel like most nervous about

## 48755:00 - 48810:00

are really hard to solve bugs. I think

## 48810:00 - 48835:00

that like uh

## 48835:00 - 48850:00

>> that's interesting.

## 48850:00 - 48880:00

>> Yeah. And I think this is like maybe

## 48880:00 - 48905:00

somewhat surprising to me, but it's just

## 48905:00 - 48945:00

like a single bug can like

## 48945:00 - 48970:00

>> derail you for months.

## 48970:00 - 48990:00

>> And when you think about it, like you

## 48990:00 - 49025:00

the models take months to train. So you

## 49025:00 - 49040:00

could kind of like lose a whole

## 49040:00 - 49060:00

generationally

## 49060:00 - 49100:00

>> off of something that just looks like

## 49100:00 - 49140:00

odd. You know, it turns out like

## 49140:00 - 49180:00

>> this piece of your code was incorrect

## 49180:00 - 49205:00

and you couldn't detect it.

## 49205:00 - 49240:00

>> Uh and it's really hard in ML, right? ML

## 49240:00 - 49260:00

is always really hard to find bugs in.

## 49260:00 - 49285:00

>> Yeah, totally. But also some of these

## 49285:00 - 49310:00

scaled up issues are really hard to

## 49310:00 - 49335:00

solve even when you know they're there.

## 49335:00 - 49360:00

>> Yeah. Like what's even a unit test that

## 49360:00 - 49390:00

you would write or forget a unit test? I

## 49390:00 - 49430:00

mean anything close to a test for the

## 49430:00 - 49460:00

type of like network architecture on

## 49460:00 - 49485:00

which you're doing this. Like how do you

## 49485:00 - 49510:00

even do that?

## 49510:00 - 49535:00

>> I mean like you can send a packet over

## 49535:00 - 49575:00

it and confirm it's the same.

## 49575:00 - 49600:00

>> Uh you can you can train a small model

## 49600:00 - 49615:00

on it. Um

## 49615:00 - 49640:00

>> but even train a small model on it it's

## 49640:00 - 49665:00

like not obvious. You know, if you have

## 49665:00 - 49695:00

like the the simp the very classic like

## 49695:00 - 49730:00

very simple ML bug that like early

## 49730:00 - 49750:00

people face in their careers like okay,

## 49750:00 - 49775:00

they have some like they have like 10

## 49775:00 - 49800:00

layers in their network and like you

## 49800:00 - 49830:00

know layer 7 connects to nine instead of

## 49830:00 - 49865:00

8 to 9 and like so like there's some

## 49865:00 - 49895:00

incorrect like set of connections you

## 49895:00 - 49920:00

have there and technically the model

## 49920:00 - 49940:00

still trains and all the weights update

## 49940:00 - 49965:00

and so it's like a valid model but it's

## 49965:00 - 50000:00

not the correct one and that's like a

## 50000:00 - 50025:00

very esoteric weird bug that would

## 50025:00 - 50065:00

actually be kind of hard to find. Like

## 50065:00 - 50080:00

is is that kind of what you're referring

## 50080:00 - 50110:00

to of these like random bugs you face?

## 50110:00 - 50125:00

>> Yeah. Yeah,

## 50125:00 - 50155:00

>> it's that but like you know you can

## 50155:00 - 50170:00

>> times a million

## 50170:00 - 50195:00

>> times a million as the thing gets more

## 50195:00 - 50225:00

complicated you know you could like cast

## 50225:00 - 50275:00

the wrong precision deep in some kernel

## 50275:00 - 50310:00

and that causes your model to like blow

## 50310:00 - 50325:00

up at large scale

## 50325:00 - 50345:00

>> and you find out like a month in

## 50345:00 - 50355:00

>> or you never find out

## 50355:00 - 50370:00

>> or you never find out

## 50370:00 - 50400:00

>> I mean you know like like you see the

## 50400:00 - 50420:00

thing blow up like

## 50420:00 - 50445:00

>> there's I don't know 10 tens of

## 50445:00 - 50475:00

thousands of lines of code like how

## 50475:00 - 50495:00

would you ever trace it down so like

## 50495:00 - 50520:00

those are the things that probably spook

## 50520:00 - 50565:00

me the most is just like some subtle

## 50565:00 - 50600:00

tricky bug yeah that's probably the case

## 50600:00 - 50620:00

of like you don't I think there's

## 50620:00 - 50645:00

actually also the case of you do know

## 50645:00 - 50690:00

like it crashes. You're training your

## 50690:00 - 50730:00

model and it like or it slows down. You

## 50730:00 - 50760:00

know, your job slows down a ton

## 50760:00 - 50810:00

>> and those things can also be very hard

## 50810:00 - 50860:00

to debug. Uh Nelson Elhaj is one person

## 50860:00 - 50880:00

that he has a blog. He wrote up a blog

## 50880:00 - 50920:00

on one like cursed bug we had early on

## 50920:00 - 50940:00

and I remember this one quite well

## 50940:00 - 50965:00

because I think like I encountered it

## 50965:00 - 50990:00

fairly early and was like this looks

## 50990:00 - 51025:00

hard. Can someone else look at it? And

## 51025:00 - 51050:00

like a month later was like wow I'm so

## 51050:00 - 51080:00

glad I handed that one off. I never I

## 51080:00 - 51110:00

never would have been able to get like

## 51110:00 - 51135:00

like one of the abilities I think is

## 51135:00 - 51155:00

actually really useful this is the

## 51155:00 - 51180:00

ability to like deep dive anything to

## 51180:00 - 51200:00

any level of depth

## 51200:00 - 51230:00

>> but that's a pretty rare skill like for

## 51230:00 - 51250:00

me you know as I we talked about what

## 51250:00 - 51270:00

level of the stack I was at before I was

## 51270:00 - 51300:00

like working at the torch matball but

## 51300:00 - 51340:00

like if I didn't know CUDA so torch

## 51340:00 - 51360:00

mountain was broken it wasn't like I

## 51360:00 - 51390:00

could dig into torch matmo and figure it

## 51390:00 - 51430:00

out and it's similarly with like

## 51430:00 - 51470:00

>> communications right like I could I

## 51470:00 - 51510:00

could call send send bytes from A to B

## 51510:00 - 51535:00

but I didn't know the like underlying

## 51535:00 - 51560:00

networking protocol so if that

## 51560:00 - 51585:00

underlying networking protocol is

## 51585:00 - 51630:00

broken. Uh like I need to learn a whole

## 51630:00 - 51650:00

field. I have to like understand packets

## 51650:00 - 51685:00

and TCP or like all all of these

## 51685:00 - 51720:00

different things to debug that. And I

## 51720:00 - 51745:00

think one thing that's like surprisingly

## 51745:00 - 51770:00

hard and there's very few people who can

## 51770:00 - 51815:00

do is like kind of own that whole stack

## 51815:00 - 51845:00

from like I understand how the ML is

## 51845:00 - 51860:00

supposed to work and what the learning

## 51860:00 - 51900:00

dynamics are all the way down to like I

## 51900:00 - 51940:00

know the bites and I like can understand

## 51940:00 - 51965:00

how the bittes should be moving around

## 51965:00 - 51975:00

machines.

## 51975:00 - 52000:00

>> Totally. Yeah. And actually on that

## 52000:00 - 52020:00

front, like when you think about the

## 52020:00 - 52045:00

different backgrounds of people on your

## 52045:00 - 52070:00

team today, how do you like

## 52070:00 - 52100:00

approximately

## 52100:00 - 52135:00

uh map them out to different categories

## 52135:00 - 52150:00

of computer scientists? Like I think

## 52150:00 - 52180:00

there's this external view of what these

## 52180:00 - 52200:00

teams look like, which is that they're

## 52200:00 - 52240:00

like all PhD researchers who write ML

## 52240:00 - 52265:00

papers. And I suspect that's not

## 52265:00 - 52290:00

actually true given what you're

## 52290:00 - 52305:00

describing here.

## 52305:00 - 52325:00

>> Yeah, it's a mix. And I think the thing

## 52325:00 - 52360:00

we like most need is engineers.

## 52360:00 - 52385:00

Interesting. Almost always like

## 52385:00 - 52405:00

throughout like the entire history of

## 52405:00 - 52440:00

this field. Totally. It's like the case

## 52440:00 - 52475:00

that you throw more compute, the thing

## 52475:00 - 52510:00

kind of works. Yeah. Uh the challenge is

## 52510:00 - 52515:00

like actually

## 52515:00 - 52545:00

>> the researchers are like cool, nice.

## 52545:00 - 52565:00

>> Yeah. And getting it correct, like

## 52565:00 - 52595:00

getting it correct isn't really an ML

## 52595:00 - 52615:00

problem, right? Like the actual

## 52615:00 - 52650:00

architectures are pretty simple. You you

## 52650:00 - 52675:00

can write the math down. But you don't

## 52675:00 - 52695:00

even need to understand the math to

## 52695:00 - 52725:00

implement it. You just need to like get

## 52725:00 - 52760:00

a correct implementation and then you

## 52760:00 - 52780:00

sort of have an engineering problem of

## 52780:00 - 52810:00

how do I take this implement it at large

## 52810:00 - 52835:00

scale, paralyze all the things and check

## 52835:00 - 52855:00

that it's

## 52855:00 - 52880:00

>> correct. But it's yeah so it's like kind

## 52880:00 - 52900:00

of engineering skill but it's this

## 52900:00 - 52915:00

particular type of engineering skill

## 52915:00 - 52945:00

that's about being able to like debug

## 52945:00 - 52965:00

anything. Yeah.

## 52965:00 - 52990:00

>> Um I think there's another angle of

## 52990:00 - 53020:00

engineering which I think of as like

## 53020:00 - 53050:00

really quickly iterate on like a website

## 53050:00 - 53085:00

or something which I think of as an

## 53085:00 - 53100:00

important skill set probably important

## 53100:00 - 53130:00

for making startup. You got to be like

## 53130:00 - 53150:00

fail fast try a bunch of different

## 53150:00 - 53180:00

things none of which are like

## 53180:00 - 53230:00

>> that technically difficult to do. the

## 53230:00 - 53255:00

skill sets that we're like most kind of

## 53255:00 - 53305:00

in need of or looking for are this like

## 53305:00 - 53345:00

able to solve really hard engineering

## 53345:00 - 53355:00

problems.

## 53355:00 - 53410:00

>> Are they people who worked at companies

## 53410:00 - 53450:00

that grew a whole bunch and so they have

## 53450:00 - 53490:00

experience like doing the kind of thing

## 53490:00 - 53510:00

you've done over the last several years

## 53510:00 - 53545:00

at anthropic or do they tend to be

## 53545:00 - 53560:00

academics or like where do they come

## 53560:00 - 53570:00

from?

## 53570:00 - 53595:00

>> Yeah. So at this point like I think we

## 53595:00 - 53610:00

actually just hire a bunch of people who

## 53610:00 - 53645:00

have done this before from like other

## 53645:00 - 53675:00

places and that's like the easy answer.

## 53675:00 - 53710:00

Yeah. Yeah. But like by this before, do

## 53710:00 - 53735:00

you mean in AI companies necessarily or

## 53735:00 - 53750:00

also, you know, like someone who worked

## 53750:00 - 53800:00

at Meta on like their not AI team but

## 53800:00 - 53825:00

they ran some other distributed system

## 53825:00 - 53860:00

that you know reached internet scale

## 53860:00 - 53885:00

five you know 10 years ago or something

## 53885:00 - 53890:00

like that

## 53890:00 - 53910:00

>> more like we have like a specific role

## 53910:00 - 53930:00

in mind. So like say I'm like trying to

## 53930:00 - 53965:00

make the run train efficiently in Jacks

## 53965:00 - 53995:00

like hiring someone who's like worked on

## 53995:00 - 54020:00

jacks would be great or someone who's

## 54020:00 - 54050:00

like worked at another company on

## 54050:00 - 54080:00

optimizing a jack stack to be really

## 54080:00 - 54115:00

efficient. That's kind of like I think

## 54115:00 - 54135:00

now we're at the point where like the

## 54135:00 - 54155:00

entropic is well enough known we can

## 54155:00 - 54190:00

sort of hire these people and also the

## 54190:00 - 54210:00

field is big enough that there's like

## 54210:00 - 54240:00

people with expertise. One thing that

## 54240:00 - 54255:00

was interesting was like early on we

## 54255:00 - 54280:00

hired a lot of people from just like all

## 54280:00 - 54320:00

sorts of backgrounds and I think that

## 54320:00 - 54345:00

people who are just smart and work

## 54345:00 - 54370:00

really hard can learn this pretty fast

## 54370:00 - 54395:00

but you have to like want to. We hired a

## 54395:00 - 54425:00

lot of physicists for instance like

## 54425:00 - 54460:00

theoretical physicists who just like

## 54460:00 - 54490:00

>> show up they they do a residency like

## 54490:00 - 54525:00

learn to program and then uh they were

## 54525:00 - 54555:00

really smart they could do really great

## 54555:00 - 54605:00

work. Um I want to switch gears uh to

## 54605:00 - 54620:00

talk about something a little bit

## 54620:00 - 54640:00

different which is just sort of future

## 54640:00 - 54655:00

looking things around how you think

## 54655:00 - 54705:00

about other domains and or sort of

## 54705:00 - 54730:00

advances happening in AI that I'm seeing

## 54730:00 - 54750:00

elsewhere in the field and you don't

## 54750:00 - 54765:00

have to tell me if you guys are working

## 54765:00 - 54800:00

on these necessarily but like how you

## 54800:00 - 54830:00

think about them like are I guess one

## 54830:00 - 54865:00

one big area I was thinking about is

## 54865:00 - 54900:00

around areas other than next token

## 54900:00 - 54925:00

prediction like are there any of the

## 54925:00 - 54950:00

other you know things that people are

## 54950:00 - 54970:00

working on that you're curious about so

## 54970:00 - 55010:00

basically two differences there one is

## 55010:00 - 55035:00

uh not using transformer as an

## 55035:00 - 55065:00

architecture um So there's companies

## 55065:00 - 55090:00

like Liquid AI that have their own kind

## 55090:00 - 55110:00

of architecture for example they're

## 55110:00 - 55160:00

using um or not using autogressive

## 55160:00 - 55190:00

training as a way of training models.

## 55190:00 - 55225:00

Are there are any of those do you think

## 55225:00 - 55255:00

interesting and like ways that we might

## 55255:00 - 55280:00

come closer to AGI or do you think like

## 55280:00 - 55305:00

this autogressive framework is the one

## 55305:00 - 55325:00

that kind of makes sense?

## 55325:00 - 55345:00

>> I think they're interesting. I think I

## 55345:00 - 55380:00

like am less like ah autogressive is the

## 55380:00 - 55410:00

way to go. On the other hand, I think

## 55410:00 - 55445:00

auto reagive is probably good enough to

## 55445:00 - 55490:00

get to AGI or something or not like yeah

## 55490:00 - 55520:00

>> uh such that

## 55520:00 - 55570:00

>> yeah I I see the main driver as scale

## 55570:00 - 55610:00

and careful science of like sort of the

## 55610:00 - 55645:00

basics more than like come up with

## 55645:00 - 55665:00

something totally novel.

## 55665:00 - 55685:00

>> Not because there aren't novel things

## 55685:00 - 55705:00

that are better. I actually like I'm

## 55705:00 - 55735:00

pretty confident they are there. It's

## 55735:00 - 55765:00

just that scale is easier and it's more

## 55765:00 - 55800:00

reliable and I think you we're still

## 55800:00 - 55830:00

seeing really big gains to that. Do you

## 55830:00 - 55850:00

spend a lot of time on thinking about

## 55850:00 - 55870:00

things like you know I've been reading

## 55870:00 - 55895:00

some of these open source papers where

## 55895:00 - 55915:00

you can kind of dive into some of the

## 55915:00 - 55945:00

details about the model changes and with

## 55945:00 - 55970:00

some of these Chinese labs for example

## 55970:00 - 56010:00

where they're making tweaks on the order

## 56010:00 - 56045:00

of the architecture itself with like

## 56045:00 - 56075:00

better caching behavior for example or

## 56075:00 - 56105:00

like more efficient attention functions

## 56105:00 - 56130:00

that make a big difference. Do you feel

## 56130:00 - 56150:00

like these are examples of things like

## 56150:00 - 56170:00

you mentioned earlier where it's

## 56170:00 - 56195:00

basically in the grand scheme of things

## 56195:00 - 56215:00

basically if you throw more compute at

## 56215:00 - 56240:00

it this is all kind of a rounding error

## 56240:00 - 56270:00

or do you think it will take some number

## 56270:00 - 56300:00

of these very clever architectural

## 56300:00 - 56330:00

changes to actually get to hi like in

## 56330:00 - 56350:00

the way that the first person who came

## 56350:00 - 56380:00

up with the transformer made like a

## 56380:00 - 56410:00

particular transform you know literally

## 56410:00 - 56445:00

transform transformative change like

## 56445:00 - 56465:00

will it take some of that or do you

## 56465:00 - 56485:00

think it just you keep doing the thing

## 56485:00 - 56500:00

we're doing to make it bigger

## 56500:00 - 56545:00

>> I think it'll be a mix I think I like my

## 56545:00 - 56570:00

guess is you'll keep tweaking things the

## 56570:00 - 56595:00

more compute you put in the more like

## 56595:00 - 56635:00

worthwhile it is to like do those

## 56635:00 - 56670:00

experiments to like figure it out the

## 56670:00 - 56690:00

you know I mean inference is a thing we

## 56690:00 - 56720:00

haven't talked about but like you also

## 56720:00 - 56740:00

want to serve these models to a lot of

## 56740:00 - 56765:00

people so there's a lot of changes you

## 56765:00 - 56790:00

can make to make inference cheaper and

## 56790:00 - 56820:00

that depends on like the details of your

## 56820:00 - 56835:00

inference stack and the chips you're

## 56835:00 - 56865:00

serving inference on etc. So

## 56865:00 - 56890:00

>> do you as a someone focused on

## 56890:00 - 56910:00

pre-training have to think a lot about

## 56910:00 - 56940:00

inference or is it kind of like you just

## 56940:00 - 56965:00

do your thing you make the loss go down

## 56965:00 - 56990:00

and then hand it off and someone else

## 56990:00 - 57010:00

makes that happen. Oh no. I think a ton

## 57010:00 - 57045:00

about inference because basically like

## 57045:00 - 57075:00

the problem inference is solving like we

## 57075:00 - 57095:00

basically determine the problem

## 57095:00 - 57115:00

inference is solving. We give them a

## 57115:00 - 57135:00

model and they have to like run that

## 57135:00 - 57170:00

fast and it's very easy to give them a

## 57170:00 - 57200:00

model that is impossible to run fast.

## 57200:00 - 57225:00

>> Oh, can you give an example of a

## 57225:00 - 57240:00

decision you can make that could cause

## 57240:00 - 57250:00

that?

## 57250:00 - 57275:00

>> I mean the simplest one's stupid but

## 57275:00 - 57300:00

it's like you just make the model giant.

## 57300:00 - 57340:00

>> Yeah, absolutely. Train for like a

## 57340:00 - 57370:00

really small number of tokens and then

## 57370:00 - 57400:00

inference now has this giant model

## 57400:00 - 57425:00

>> and their host basically.

## 57425:00 - 57465:00

>> Yeah. I mean you can also make things

## 57465:00 - 57495:00

require communications in a lot of

## 57495:00 - 57515:00

places

## 57515:00 - 57540:00

>> uh which would make it harder for

## 57540:00 - 57565:00

inference. Um totally

## 57565:00 - 57585:00

>> you can also just make things

## 57585:00 - 57615:00

complicated and like there's no

## 57615:00 - 57645:00

fundamental reason it's hard but there's

## 57645:00 - 57665:00

only so many people on the inference

## 57665:00 - 57690:00

team and like they have to implement it

## 57690:00 - 57705:00

in a bunch of places.

## 57705:00 - 57725:00

>> Yeah.

## 57725:00 - 57745:00

>> Yeah. No, so I definitely think of like

## 57745:00 - 57775:00

the like inference is the team that I

## 57775:00 - 57820:00

work the most closely with like

## 57820:00 - 57850:00

>> because we're kind of like co-designing

## 57850:00 - 57890:00

models to be smart and cheap.

## 57890:00 - 57910:00

>> Yeah. Interesting. particularly in a

## 57910:00 - 57940:00

world of like limited compute, right?

## 57940:00 - 57975:00

Like the sort of the bottleneck I think

## 57975:00 - 58000:00

to a large degree on our I mean you can

## 58000:00 - 58030:00

see anthropic has rate limits constantly

## 58030:00 - 58055:00

and people complain about a lot and like

## 58055:00 - 58085:00

the reason is like

## 58085:00 - 58110:00

>> there's only so much compute we can get

## 58110:00 - 58145:00

on on short notice. So you like making

## 58145:00 - 58170:00

your inference more efficient is like

## 58170:00 - 58195:00

the way you can serve more users

## 58195:00 - 58220:00

>> and actually like let's say you had 100x

## 58220:00 - 58250:00

more compute or we somehow didn't live

## 58250:00 - 58280:00

in a world where compute was limited.

## 58280:00 - 58345:00

Does that change a ton about what you do

## 58345:00 - 58375:00

or is it still kind of the well you're

## 58375:00 - 58400:00

just going to grab all of it whatever

## 58400:00 - 58430:00

compute you have and keep going down the

## 58430:00 - 58455:00

loss curve and you kind of well you it's

## 58455:00 - 58480:00

like impossible to be in the world where

## 58480:00 - 58505:00

there is enough comput

## 58505:00 - 58525:00

>> so I think if we got like infinite

## 58525:00 - 58545:00

comput the challenge would be making use

## 58545:00 - 58565:00

of the compute right so like then you

## 58565:00 - 58590:00

would start to run into these issues

## 58590:00 - 58620:00

like oh well when one chip fail you know

## 58620:00 - 58645:00

like okay I'm going to throw two billion

## 58645:00 - 58680:00

chips around but what happens when a

## 58680:00 - 58710:00

chip fails so I think we would be

## 58710:00 - 58730:00

limited on people then it would be like

## 58730:00 - 58750:00

how fast can we solve the hard

## 58750:00 - 58785:00

engineering problems to scale up. But I

## 58785:00 - 58810:00

do think the change is massive and I

## 58810:00 - 58845:00

think people like don't realize how chip

## 58845:00 - 58895:00

limited AI like research is or something

## 58895:00 - 58925:00

right now. Like the models that everyone

## 58925:00 - 58950:00

uses, right? If you're using like Cloud

## 58950:00 - 58985:00

Sonic 4, Cloud Opus 4, it's like it's

## 58985:00 - 59025:00

our first shot at models at that scale,

## 59025:00 - 59045:00

right? And like

## 59045:00 - 59065:00

>> if you think about anything like you

## 59065:00 - 59085:00

could do it and you could do it again,

## 59085:00 - 59120:00

you could do a better job. But if you

## 59120:00 - 59155:00

sort of imagine like 10x the comput like

## 59155:00 - 59180:00

you could run this every day instead of

## 59180:00 - 59230:00

every few months like you or 100x maybe

## 59230:00 - 59265:00

for that then like yeah it's just it's a

## 59265:00 - 59285:00

really it would be a really big change

## 59285:00 - 59305:00

to have a lot more comput and it's

## 59305:00 - 59325:00

coming right like that's like kind of

## 59325:00 - 59350:00

the fun part of the field is like every

## 59350:00 - 59375:00

year you're like oh I had no comput a

## 59375:00 - 59430:00

year ago then exactly how do you think

## 59430:00 - 59460:00

about methods like uh like discrete

## 59460:00 - 59485:00

diffusion like I saw there's like a

## 59485:00 - 59510:00

gemini diffusion model and I think about

## 59510:00 - 59545:00

that in the space I used to be in where

## 59545:00 - 59565:00

um there's a lot of discrete diffusion

## 59565:00 - 59585:00

models being used in protein design for

## 59585:00 - 59620:00

example space where my startup was like

## 59620:00 - 59640:00

do you see that as a domain where

## 59640:00 - 59670:00

there's going to be interesting uh

## 59670:00 - 59685:00

advances happening?

## 59685:00 - 59710:00

>> I'll be honest like we haven't done

## 59710:00 - 59745:00

image generation and I think that's been

## 59745:00 - 59775:00

like the main use for diffusion. So I've

## 59775:00 - 59805:00

kind of had this on my like to-do list

## 59805:00 - 59830:00

of like things I should understand for a

## 59830:00 - 59855:00

while and like there are people in my

## 59855:00 - 59875:00

team who do understand it and would have

## 59875:00 - 59905:00

better thoughts but like I actually

## 59905:00 - 59925:00

don't think I understand it well enough

## 59925:00 - 59960:00

to know. I I do have it kind of in my

## 59960:00 - 59990:00

this category of like yeah

## 59990:00 - 60020:00

>> not a total par like and there's a lot

## 60020:00 - 60035:00

of things that aren't like a huge

## 60035:00 - 60065:00

paradigm shift but they're like pretty

## 60065:00 - 60100:00

big changes to how things run and I

## 60100:00 - 60130:00

expect like there are some of those that

## 60130:00 - 60155:00

will work um I don't know if it's

## 60155:00 - 60180:00

diffusion or if it's another one

## 60180:00 - 60200:00

>> obviously who knows what anthropic will

## 60200:00 - 60220:00

do in the future but at least in the

## 60220:00 - 60255:00

near term are the things where you see

## 60255:00 - 60290:00

>> big areas where a startup can win in the

## 60290:00 - 60315:00

world in which anthropic is getting you

## 60315:00 - 60330:00

know making their models better

## 60330:00 - 60345:00

year-over-year

## 60345:00 - 60375:00

>> my general read is like anything that

## 60375:00 - 60420:00

benefits from the model getting smarter

## 60420:00 - 60450:00

I think Like on the one hand there's

## 60450:00 - 60485:00

like a lot you can always be like oh

## 60485:00 - 60520:00

yeah the if you're doing a startup like

## 60520:00 - 60545:00

all the AI labs are big companies

## 60545:00 - 60565:00

they'll be bigger than you and they

## 60565:00 - 60595:00

could do that thing but also like we're

## 60595:00 - 60620:00

all working on this general system that

## 60620:00 - 60665:00

covers a lot of different uses and the

## 60665:00 - 60690:00

the plan is to like power all the

## 60690:00 - 60725:00

startups to do all of the individual

## 60725:00 - 60750:00

work. So yeah I think like anything that

## 60750:00 - 60800:00

just kind of looks like oh this almost

## 60800:00 - 60835:00

works with current models but requires

## 60835:00 - 60865:00

like a bunch of work is a pretty

## 60865:00 - 60890:00

promising direction. Uh, I think maybe

## 60890:00 - 60910:00

the thing to watch out for is things

## 60910:00 - 60945:00

where like they work now with a huge

## 60945:00 - 60970:00

amount of work like to build up a

## 60970:00 - 61005:00

scaffold, but the next generation you're

## 61005:00 - 61025:00

not going to need the whole scaffold you

## 61025:00 - 61055:00

built up. That's I mean maybe that's

## 61055:00 - 61070:00

fine. I don't know. Like maybe you just

## 61070:00 - 61090:00

build up the business with the scaffold

## 61090:00 - 61110:00

and then you don't have to do any work

## 61110:00 - 61140:00

later and you business, but like I don't

## 61140:00 - 61155:00

know about the business side of it, but

## 61155:00 - 61190:00

like it does feel a little silly to put

## 61190:00 - 61225:00

to invest a ton in that.

## 61225:00 - 61240:00

>> Yeah, totally.

## 61240:00 - 61265:00

>> What about on the flip side? Are there

## 61265:00 - 61310:00

things in your training uh stack where

## 61310:00 - 61330:00

you're like, man, if there was a company

## 61330:00 - 61355:00

that solved X problem, I would totally

## 61355:00 - 61375:00

buy their product.

## 61375:00 - 61405:00

>> Yeah, there's like a ton. I do think

## 61405:00 - 61430:00

that like probably most of these like

## 61430:00 - 61450:00

the way I would probably structure would

## 61450:00 - 61475:00

be like almost like making something but

## 61475:00 - 61505:00

then consulting with the comp like

## 61505:00 - 61535:00

offering a service to companies for

## 61535:00 - 61550:00

free.

## 61550:00 - 61580:00

>> Particularly for like companies that are

## 61580:00 - 61605:00

scaling really fast, you're almost

## 61605:00 - 61630:00

always limited on like how many people

## 61630:00 - 61660:00

you can have. So if you can like

## 61660:00 - 61680:00

>> even if you could hire people to do it

## 61680:00 - 61690:00

yourself, actually being able to

## 61690:00 - 61725:00

contract someone else to do it where

## 61725:00 - 61765:00

like they're managing it and you know

## 61765:00 - 61785:00

hire all the people and like deal with

## 61785:00 - 61810:00

the organizational side could be useful.

## 61810:00 - 61840:00

I mean there's huge amount of stuff. One

## 61840:00 - 61860:00

that jumps to mind we talked about like

## 61860:00 - 61900:00

chips that do math incorrectly. Like it

## 61900:00 - 61915:00

would be lovely if there was some

## 61915:00 - 61950:00

startup that like you could just say

## 61950:00 - 61980:00

like here are my chips. confirm they're

## 61980:00 - 62010:00

all perfect. And if they're not, let me

## 62010:00 - 62035:00

know exactly what went wrong on like

## 62035:00 - 62070:00

what fraction of them. And like I can

## 62070:00 - 62090:00

tell you the math is wrong, but I

## 62090:00 - 62110:00

couldn't really tell. I don't really

## 62110:00 - 62140:00

know enough details of chips to be like

## 62140:00 - 62175:00

this chip failed because this particular

## 62175:00 - 62210:00

like low-level component was like wired

## 62210:00 - 62250:00

wrong or like got hit by a game. I don't

## 62250:00 - 62270:00

I don't know what causes it. You could

## 62270:00 - 62300:00

always go like bunch a bunch deeper. I

## 62300:00 - 62320:00

mean, the thing I'd maybe just push

## 62320:00 - 62335:00

startups on is thinking a little bit

## 62335:00 - 62385:00

about like uh this is maybe less

## 62385:00 - 62410:00

technical, but just like what happens

## 62410:00 - 62440:00

once we get AGI and like how to make

## 62440:00 - 62470:00

sure that like goes well for the world

## 62470:00 - 62500:00

or something. Like my my expectation is

## 62500:00 - 62530:00

like if you actually automate

## 62530:00 - 62555:00

>> almost everything a person can do. The

## 62555:00 - 62580:00

amount of economic growth there is just

## 62580:00 - 62640:00

like truly enormous and I would think a

## 62640:00 - 62660:00

little more about like how do you make

## 62660:00 - 62690:00

this like help the world versus not. I

## 62690:00 - 62700:00

think there's going to be like plenty of

## 62700:00 - 62725:00

economic success or something as a

## 62725:00 - 62740:00

result of it anyway.

## 62740:00 - 62775:00

>> Yeah, absolutely. Yeah. Um last question

## 62775:00 - 62810:00

I want to ask you is around if you

## 62810:00 - 62835:00

rewind back to where we started like 10

## 62835:00 - 62880:00

years ago. Uh you're a student, you're

## 62880:00 - 62915:00

pivoting into AI from kind of economics

## 62915:00 - 62960:00

work you were thinking about. Um and you

## 62960:00 - 62980:00

know all sorts of things you probably

## 62980:00 - 63005:00

did in those early days had some kind of

## 63005:00 - 63045:00

compounding return for you as you

## 63045:00 - 63075:00

developed into the role you have now.

## 63075:00 - 63095:00

Like what advice would you give to

## 63095:00 - 63135:00

students as they think about uh entering

## 63135:00 - 63170:00

the workforce, especially today? Um

## 63170:00 - 63190:00

learning skills that going to be useful

## 63190:00 - 63220:00

and maybe getting themselves jobs like

## 63220:00 - 63240:00

the ones you have right now 10 years

## 63240:00 - 63265:00

later? It's hard because I think the

## 63265:00 - 63285:00

timing is very different. Like I just

## 63285:00 - 63320:00

think we're like we've made we made a

## 63320:00 - 63335:00

lot of progress. So like what I would do

## 63335:00 - 63355:00

10 years ago is different from what I

## 63355:00 - 63365:00

would do today.

## 63365:00 - 63375:00

>> Totally.

## 63375:00 - 63400:00

>> But I think certainly if I went back 10

## 63400:00 - 63435:00

years ago I would be like focus on AI.

## 63435:00 - 63475:00

It's like the most important thing and

## 63475:00 - 63505:00

particularly focus on engineering which

## 63505:00 - 63530:00

I think felt very wouldn't have seemed

## 63530:00 - 63555:00

obvious to me at the time that like the

## 63555:00 - 63575:00

important thing was these engineering

## 63575:00 - 63620:00

skills and not the like math and

## 63620:00 - 63645:00

theoretical understanding of like you

## 63645:00 - 63685:00

know uh SPMs and like all the kind of

## 63685:00 - 63700:00

standard

## 63700:00 - 63745:00

>> ML literature. Um, I think today I would

## 63745:00 - 63780:00

probably focus a bunch on the like

## 63780:00 - 63810:00

engineering and on the like figuring out

## 63810:00 - 63865:00

what to do with AGI as sort of the two

## 63865:00 - 63900:00

like main things that feel top of mind

## 63900:00 - 63905:00

for me.

## 63905:00 - 63925:00

>> Let's call it there. Thanks so much,

## 63925:00+

Nick. Appreciate it.

