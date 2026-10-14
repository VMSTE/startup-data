---
source: https://www.youtube.com/watch?v=dIPdY541vus
title: "Google DeepMind CTO: Advancing AI Frontier, New Reasoning Methods, Video
  Generation’s Potential"
author: Alex Kantrowitz
date: 2025-05-24
views: 12515
description: >-
  Koray Kavukcuoglu is the Chief Technology Officer of Google DeepMind.
  Kavukcuoglu joins Big Technology to discuss how his team is pushing the
  frontier of AI research inside Google and the path to AGI.


  Tune in to hear Kavukcuoglu break down the value of brute scale versus novel
  techniques and how the new inference-time “DeepThink” mode could supercharge
  reasoning.


  We also cover Veo 3’s sound-synced video generation, the
  open-source-versus-proprietary debate, and what a ten-percent jump in model
  quality might unlock for users everywhere.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:58:23.725Z
---

# Google DeepMind CTO: Advancing AI Frontier, New Reasoning Methods, Video Generation’s Potential

## 00:00 - 25:00

What's going on in the heart of Google's

## 25:00 - 70:00

AI research operation? We'll find out

## 70:00 - 100:00

with Google DeepMind's chief technology

## 100:00 - 150:00

officer right after this. Welcome to Big

## 150:00 - 180:00

Technology Podcast, a show for

## 180:00 - 215:00

coolheaded and nuance conversation of

## 215:00 - 255:00

the tech world and beyond. We have a

## 255:00 - 290:00

great show for you today, a bonus show

## 290:00 - 345:00

just as Google's IO news hits the wire.

## 345:00 - 385:00

We have so much to talk about including

## 385:00 - 415:00

what's going on with the company, what

## 415:00 - 470:00

it's announced today, but also really

## 470:00 - 510:00

what is happening in the research effort

## 510:00 - 545:00

underlying it all. And we have a great

## 545:00 - 595:00

guest for you. Joining us today is Korai

## 595:00 - 635:00

Kavukolu. He is the chief technology

## 635:00 - 660:00

officer of DeepMind. We're going to

## 660:00 - 700:00

speak with Korai today and then tomorrow

## 700:00 - 745:00

you'll hear from DeepMind CEO Demesis

## 745:00 - 765:00

Avis. Korai, great to see you. Welcome

## 765:00 - 805:00

to the show. Thank you very much.

## 805:00 - 840:00

Welcome. Thanks for inviting. All right.

## 840:00 - 870:00

Uh it's great to be here. Folks, by the

## 870:00 - 895:00

way, if you're watching on video, uh

## 895:00 - 920:00

Cory and I are in two separate

## 920:00 - 980:00

conference rooms in uh Google's uh I

## 980:00 - 1000:00

don't know, it's a pretty cool new

## 1000:00 - 1015:00

building that they have. It's called

## 1015:00 - 1060:00

what? Gradient gradient. We call it the

## 1060:00 - 1100:00

gradient canopy. Gradient canopy.

## 1100:00 - 1150:00

Anyway, we're here. Um and Google's uh

## 1150:00 - 1200:00

IO presentation is about to uh go on and

## 1200:00 - 1240:00

that's what's going on. So um anyway,

## 1240:00 - 1275:00

let's talk about what you're working on,

## 1275:00 - 1315:00

Korai. I mean I'm curious like what's

## 1315:00 - 1350:00

happening within Google uh Google deep

## 1350:00 - 1385:00

mind. Um can you tell me a little bit

## 1385:00 - 1425:00

about the biggest problems that your

## 1425:00 - 1460:00

research house is tackling?

## 1460:00 - 1495:00

Yeah thank you very much first of all I

## 1495:00 - 1540:00

mean great to have this conversation.

## 1540:00 - 1600:00

um like when when when you think about

## 1600:00 - 1640:00

the whole of Google deep mind like

## 1640:00 - 1665:00

there's first and foremost there's a

## 1665:00 - 1695:00

single vision right that we want to

## 1695:00 - 1725:00

build AGI that's our

## 1725:00 - 1780:00

goal and um but when we think about

## 1780:00 - 1825:00

building AGI there are two aspects to it

## 1825:00 - 1870:00

one doing all the research that is very

## 1870:00 - 1930:00

targeted on going towards building AGI

## 1930:00 - 1980:00

doing that research but we are also very

## 1980:00 - 2025:00

much ambitious and passionate about

## 2025:00 - 2060:00

doing a lot of research that showcases

## 2060:00 - 2115:00

and explores how AI even in its current

## 2115:00 - 2170:00

form can be used to impact the world. So

## 2170:00 - 2200:00

there are those two categories of

## 2200:00 - 2230:00

things. So like with Gemini models, with

## 2230:00 - 2265:00

VO models, all those kinds of generative

## 2265:00 - 2295:00

AI models and exciting things that is

## 2295:00 - 2335:00

happening there. That's our main line of

## 2335:00 - 2380:00

AGI research that is going on. We also

## 2380:00 - 2435:00

have uh as many people would know things

## 2435:00 - 2470:00

like alpha folds, our work on

## 2470:00 - 2510:00

mathematics, chemistry and all those

## 2510:00 - 2540:00

kinds of things where we are really

## 2540:00 - 2585:00

exploring the boundaries of how AI can

## 2585:00 - 2630:00

be used to do new kinds of science,

## 2630:00 - 2670:00

right? And then we have much more

## 2670:00 - 2700:00

general exploratory computer science

## 2700:00 - 2745:00

related um research that's going on. So,

## 2745:00 - 2785:00

it's a it's a big spectrum and there was

## 2785:00 - 2815:00

a moment a couple years ago where I

## 2815:00 - 2840:00

think those of us outside the company

## 2840:00 - 2885:00

started to notice, wow, Google is really

## 2885:00 - 2930:00

pushing allin on generative AI and I

## 2930:00 - 2955:00

think your career journey was a little

## 2955:00 - 2985:00

bit part of that. You went from

## 2985:00 - 3015:00

overseeing lots of projects to be

## 3015:00 - 3060:00

strictly focused on generative AI which

## 3060:00 - 3095:00

means you have I think one of the best

## 3095:00 - 3155:00

views in the world as to what is helping

## 3155:00 - 3210:00

models uh get better. And I wanted to

## 3210:00 - 3225:00

ask you a question that we've been

## 3225:00 - 3265:00

asking on the show a lot, which is the

## 3265:00 - 3335:00

scale question. Um, now Google has a

## 3335:00 - 3375:00

tremendous amount of compute at your

## 3375:00 - 3415:00

disposal. Uh, and so you basically have

## 3415:00 - 3455:00

the option. Is it scale that you want to

## 3455:00 - 3485:00

throw at these models or is it new

## 3485:00 - 3520:00

techniques? So let me just ask it to you

## 3520:00 - 3585:00

as plainly as I can. Is scale the star

## 3585:00 - 3625:00

right now or is it a supporting actor in

## 3625:00 - 3655:00

terms of trying to get models to the

## 3655:00 - 3690:00

next step?

## 3690:00 - 3730:00

It's a um it's a good question I think

## 3730:00 - 3800:00

also the way you framed it u because um

## 3800:00 - 3855:00

it is definitely an important definitely

## 3855:00 - 3910:00

an important factor right like because I

## 3910:00 - 3940:00

think like the way I'd like to think

## 3940:00 - 3980:00

about this is it's rare that in any

## 3980:00 - 4010:00

research problem you would have a

## 4010:00 - 4075:00

dimension that like pretty confidently

## 4075:00 - 4105:00

would would give you improvements right

## 4105:00 - 4130:00

like with of course like with maybe

## 4130:00 - 4170:00

diminishing returns but most of the time

## 4170:00 - 4220:00

with research it's always like that. So

## 4220:00 - 4265:00

like when we think about our research

## 4265:00 - 4310:00

right now in the case of generative AI

## 4310:00 - 4360:00

models right scale is definitely one of

## 4360:00 - 4405:00

those but like it's one of those things

## 4405:00 - 4435:00

that are equally important with other

## 4435:00 - 4475:00

things when we are thinking about our

## 4475:00 - 4510:00

architectures like the architectural

## 4510:00 - 4545:00

elements the algorithms that we put in

## 4545:00 - 4590:00

there that com that make up the model

## 4590:00 - 4625:00

right they are as important as the

## 4625:00 - 4655:00

scale. We of course analyze and

## 4655:00 - 4705:00

understand as with scale how do these

## 4705:00 - 4730:00

different architectures different

## 4730:00 - 4765:00

algorithms become more and more

## 4765:00 - 4790:00

effective. That's an important part

## 4790:00 - 4820:00

because you know that you are putting

## 4820:00 - 4855:00

more computational

## 4855:00 - 4895:00

capacity and like you want to make sure

## 4895:00 - 4935:00

that you research the kinds of

## 4935:00 - 4970:00

architectures and algorithms that pay

## 4970:00 - 5025:00

off the best under that kind of scaling

## 5025:00 - 5060:00

property. Right? But as I said that's

## 5060:00 - 5090:00

not the only one. Data is really

## 5090:00 - 5125:00

important. I think it is as critical as

## 5125:00 - 5165:00

any other thing. The algorithms,

## 5165:00 - 5205:00

architectures, modules that we put into

## 5205:00 - 5245:00

the system as important. Understanding

## 5245:00 - 5290:00

their properties with data with more

## 5290:00 - 5335:00

compute that is as important, right? And

## 5335:00 - 5370:00

then of course inference time techniques

## 5370:00 - 5410:00

is as important as well, right? Like

## 5410:00 - 5465:00

because now that you have a particular

## 5465:00 - 5505:00

architecture, a particular model, you

## 5505:00 - 5550:00

can multiply its reasoning

## 5550:00 - 5610:00

capabilities by making sure that you can

## 5610:00 - 5645:00

use that model over and over again

## 5645:00 - 5670:00

through different techniques at

## 5670:00 - 5720:00

inference time. You know, it to me it's

## 5720:00 - 5780:00

both hopeful and puzzling uh to hear

## 5780:00 - 5800:00

about all the different techniques to

## 5800:00 - 5830:00

make these models better. And I'll

## 5830:00 - 5870:00

explain that. Um, it's helpful because

## 5870:00 - 5905:00

it seems like we're definitely going to

## 5905:00 - 5960:00

see a lot of improvement from where the

## 5960:00 - 5990:00

models are today. And the models are

## 5990:00 - 6040:00

already pretty good. Um, the the the

## 6040:00 - 6100:00

thing that's puzzling to me is u the

## 6100:00 - 6130:00

idea with scale was there was

## 6130:00 - 6175:00

effectively limitless potential in

## 6175:00 - 6230:00

making these AI models bigger. And you

## 6230:00 - 6265:00

said the words diminishing returns. Um,

## 6265:00 - 6295:00

and we've heard that from from you and

## 6295:00 - 6320:00

basically everybody working on this

## 6320:00 - 6365:00

problem. And uh and it's no secret,

## 6365:00 - 6400:00

right, that right now we've been waiting

## 6400:00 - 6435:00

forever for uh

## 6435:00 - 6495:00

GPT5. Uh Meta had some problems with

## 6495:00 - 6550:00

Llama. Uh Anthropic has been trying to

## 6550:00 - 6605:00

tell us there's a new uh Claude Opus

## 6605:00 - 6630:00

model coming out forever. We haven't

## 6630:00 - 6660:00

seen it. So clearly a lot of the

## 6660:00 - 6685:00

research houses may maybe with the

## 6685:00 - 6725:00

exception of Google uh are struggling

## 6725:00 - 6760:00

with what you get from when you make the

## 6760:00 - 6800:00

models bigger. And so I just want to ask

## 6800:00 - 6855:00

you about that. I mean, it seems like

## 6855:00 - 6875:00

it's nice that there are all these

## 6875:00 - 6910:00

techniques, but again, thinking about

## 6910:00 - 6940:00

this one technique that was supposed to

## 6940:00 - 6990:00

have limitless potential, is that a

## 6990:00 - 7020:00

disappointment for the generative AI

## 7020:00 - 7045:00

field overall if that's not going to be

## 7045:00 - 7110:00

the case? Yeah. Um I I really I really

## 7110:00 - 7155:00

don't think about it that way because we

## 7155:00 - 7200:00

have been able to um push the

## 7200:00 - 7235:00

capabilities of the models quite

## 7235:00 - 7285:00

effectively, right? I think in a way um

## 7285:00 - 7325:00

the whole scale discussion starts from

## 7325:00 - 7365:00

the scaling laws right like scaling laws

## 7365:00 - 7410:00

uh explain the performance of the models

## 7410:00 - 7450:00

under both data and compute and number

## 7450:00 - 7505:00

of parameters right and like researching

## 7505:00 - 7540:00

all three in combination is the

## 7540:00 - 7590:00

important thing and when when I look at

## 7590:00 - 7645:00

the kind of um progress that we are

## 7645:00 - 7705:00

getting from that general technology I

## 7705:00 - 7755:00

think it is it is still improving Um

## 7755:00 - 7825:00

what I what I think is important is to

## 7825:00 - 7865:00

make sure that there's a broad spectrum

## 7865:00 - 7910:00

of research that is going on across the

## 7910:00 - 7945:00

board and like rather than thinking

## 7945:00 - 7985:00

about scaling only in one dimension

## 7985:00 - 8025:00

there's actually many different ways to

## 8025:00 - 8090:00

think about it and investing in those

## 8090:00 - 8135:00

and we can see the returns that I think

## 8135:00 - 8185:00

across the field really not just um not

## 8185:00 - 8225:00

just here at Google but across the field

## 8225:00 - 8290:00

many different models are improving with

## 8290:00 - 8365:00

quite significant steps right um so I

## 8365:00 - 8415:00

think as a field the progress has been

## 8415:00 - 8460:00

quite stellar I think it's very exciting

## 8460:00 - 8510:00

and in Google we are very excited about

## 8510:00 - 8540:00

the progress that we have been having

## 8540:00 - 8590:00

with Gemini models like going from 1.5

## 8590:00 - 8635:00

to two to 2.5 I think we had a very

## 8635:00 - 8670:00

steady progress very steady improvement

## 8670:00 - 8710:00

in the capabilities of models both in

## 8710:00 - 8730:00

the spectrum of the capability ities

## 8730:00 - 8775:00

that we have but also at the quality

## 8775:00 - 8820:00

level for each capability as well.

## 8820:00 - 8875:00

Right? So I think what I'm what I'm

## 8875:00 - 8915:00

excited about is we are pushing the

## 8915:00 - 8960:00

frontier all the time and we see returns

## 8960:00 - 9005:00

in many re research directions and many

## 9005:00 - 9040:00

different dimensions of um research

## 9040:00 - 9090:00

directions and um I'm excited that

## 9090:00 - 9125:00

there's actually I think there is um

## 9125:00 - 9150:00

there's a lot more progress to do and

## 9150:00 - 9175:00

there's a lot more progress that needs

## 9175:00 - 9225:00

to happen for reaching AGI as well. You

## 9225:00 - 9260:00

started your remarks today saying that

## 9260:00 - 9295:00

the goal is AGI and there's progress

## 9295:00 - 9325:00

that needs to happen before AGI. You

## 9325:00 - 9375:00

just said we had Yan Lakun on the show a

## 9375:00 - 9405:00

couple of weeks ago. You worked in Jan's

## 9405:00 - 9465:00

lab. Jan emphatically stated there is no

## 9465:00 - 9510:00

way the AI industry is going to reach

## 9510:00 - 9535:00

human level intelligence, which is his

## 9535:00 - 9605:00

term for AGI, just by scaling up LLMs.

## 9605:00 - 9670:00

Do you agree? Well, I mean, I think um

## 9670:00 - 9715:00

that's a hypothesis, right? that might

## 9715:00 - 9760:00

turn out to be true or not but also I

## 9760:00 - 9805:00

don't think that there is any research

## 9805:00 - 9860:00

lab that is trying to only do scaling of

## 9860:00 - 9900:00

the LMS so like I don't know if anyone

## 9900:00 - 9925:00

is actually trying to negate that

## 9925:00 - 9970:00

hypothesis or not I mean we are not from

## 9970:00 - 10005:00

from my point of view we are investing

## 10005:00 - 10045:00

in such a broad spectrum of research

## 10045:00 - 10085:00

that I think that is what is necessary

## 10085:00 - 10130:00

and clearly I think like many of the

## 10130:00 - 10165:00

researchers that I talked to and me

## 10165:00 - 10230:00

myself I think that um there is a lot

## 10230:00 - 10280:00

more um critical elements that needs to

## 10280:00 - 10320:00

be invented right so there is critical

## 10320:00 - 10360:00

innovations on our path to AGI that we

## 10360:00 - 10410:00

need to uh we need to get through that's

## 10410:00 - 10450:00

why we are still looking at this as a

## 10450:00 - 10495:00

very ambitious research problem and I

## 10495:00 - 10530:00

think it is important to keep that kind

## 10530:00 - 10595:00

of critical thinking in mind with any

## 10595:00 - 10635:00

research problem you always try to look

## 10635:00 - 10670:00

at multiple different hypotheses try to

## 10670:00 - 10710:00

look at many different solutions. A

## 10710:00 - 10740:00

research problem this ambitious like

## 10740:00 - 10775:00

probably the most important problem that

## 10775:00 - 10820:00

we are working in our lifetimes, right?

## 10820:00 - 10865:00

It is the hardest problem maybe we are

## 10865:00 - 10950:00

working as um as a problem as a research

## 10950:00 - 11020:00

um problem in our in our um in our work.

## 11020:00 - 11085:00

I think like um like having that really

## 11085:00 - 11140:00

ambitious research agenda and portfolio

## 11140:00 - 11180:00

and uh making investments in many

## 11180:00 - 11215:00

different directions is the important

## 11215:00 - 11250:00

thing from my point of view. What is

## 11250:00 - 11300:00

important is defining where the goal is

## 11300:00 - 11345:00

that our goal is AGI. Our goal is not to

## 11345:00 - 11395:00

build AGI in a particular way. What's

## 11395:00 - 11430:00

important is build the AGI in the right

## 11430:00 - 11485:00

way that is positively impactful. that

## 11485:00 - 11535:00

is building uh building on it that we

## 11535:00 - 11570:00

can bring a huge amount of benefits to

## 11570:00 - 11600:00

the world that's why we are trying to

## 11600:00 - 11625:00

research AGI that's why we are trying to

## 11625:00 - 11675:00

build AGI right like AGI in itself

## 11675:00 - 11720:00

sometimes like u it it might come across

## 11720:00 - 11755:00

as it's a goal in itself the goal in

## 11755:00 - 11810:00

itself is the fact that if we do that

## 11810:00 - 11850:00

then we can hugely benefit all of

## 11850:00 - 11890:00

society all of the world right that's

## 11890:00 - 11920:00

the goal so like with that

## 11920:00 - 11965:00

responsibility of course like you put in

## 11965:00 - 11995:00

not just partic particular it's not very

## 11995:00 - 12025:00

important to me if that particular

## 12025:00 - 12060:00

hypothesis is important or not. What is

## 12060:00 - 12100:00

important is we reach that with doing a

## 12100:00 - 12140:00

very ambitious research by pursuing a

## 12140:00 - 12185:00

very ambitious research agenda and

## 12185:00 - 12255:00

building a very strong um understanding

## 12255:00 - 12305:00

of the field of intelligence. Okay. So

## 12305:00 - 12325:00

let's get to a little bit of that

## 12325:00 - 12355:00

research agenda. One of the

## 12355:00 - 12395:00

announcements that you're making at uh

## 12395:00 - 12435:00

IO which is this week which just uh by

## 12435:00 - 12465:00

when this airs it will just have been

## 12465:00 - 12500:00

made is that you're there's a new

## 12500:00 - 12540:00

product called deepthink that you're

## 12540:00 - 12585:00

releasing which is uh relying on

## 12585:00 - 12620:00

reasoning or as you put it uh test time

## 12620:00 - 12655:00

compute I think I have that right in

## 12655:00 - 12680:00

terms of what the product's going to

## 12680:00 - 12730:00

look like. How effective has uh

## 12730:00 - 12770:00

including reasoning in these models been

## 12770:00 - 12815:00

in advancing them? I mean would you say

## 12815:00 - 12840:00

when you think about all the different

## 12840:00 - 12880:00

tech techniques that you've discussed so

## 12880:00 - 12955:00

far today uh scaling included how how uh

## 12955:00 - 12990:00

what sort of a magnitude improvement are

## 12990:00 - 13035:00

you seeing by uh using reasoning and

## 13035:00 - 13085:00

talk a little bit about deep think

## 13085:00 - 13130:00

okay I mean first of all deep think like

## 13130:00 - 13165:00

it's not necessarily it's not a like a

## 13165:00 - 13230:00

separate product it is a mode that we

## 13230:00 - 13290:00

are enabling our 2.5 pro model so that

## 13290:00 - 13330:00

like it can spend a lot more time during

## 13330:00 - 13375:00

inference time to think to build

## 13375:00 - 13410:00

hypothesis and the important thing is to

## 13410:00 - 13455:00

build parallel hypothesis rather than a

## 13455:00 - 13500:00

single chain of it can build parallel

## 13500:00 - 13550:00

ones and then re can reason over

## 13550:00 - 13595:00

multiple of those build a hypothesis

## 13595:00 - 13620:00

build an understanding over those and

## 13620:00 - 13650:00

then continue building those parallel

## 13650:00 - 13685:00

chains of thoughts but this one thinks a

## 13685:00 - 13715:00

little bit longer than your traditional

## 13715:00 - 13770:00

reasoning model it will I mean in the

## 13770:00 - 13815:00

current setup Yes, it takes longer and

## 13815:00 - 13875:00

it takes um because like understanding

## 13875:00 - 13910:00

those parallel to building those

## 13910:00 - 13965:00

parallel to thoughts it's all um it's

## 13965:00 - 14010:00

it's it's it's all a much more um longer

## 14010:00 - 14060:00

process but like one thing that we are

## 14060:00 - 14115:00

also um that we are

## 14115:00 - 14165:00

also positioning it as is right now it's

## 14165:00 - 14200:00

research right like we are sharing some

## 14200:00 - 14235:00

initial research results we are excited

## 14235:00 - 14265:00

about it we are excited about the

## 14265:00 - 14315:00

technique that what it enables

## 14315:00 - 14370:00

uh what it can actually uh what it can

## 14370:00 - 14400:00

actually enable in terms of new

## 14400:00 - 14450:00

capabilities and new new new performance

## 14450:00 - 14490:00

levels. But it's early days and that's

## 14490:00 - 14530:00

why uh we are only sharing it right now.

## 14530:00 - 14565:00

We're going to start sharing with safety

## 14565:00 - 14595:00

researchers and some trusted testers

## 14595:00 - 14630:00

because we want to also understand the

## 14630:00 - 14660:00

kinds of problems that people want to

## 14660:00 - 14685:00

solve with it and the kinds of new

## 14685:00 - 14725:00

capabilities it brings and how we should

## 14725:00 - 14770:00

train it the way that that we want to

## 14770:00 - 14805:00

train. Right. So it is it is early days

## 14805:00 - 14850:00

on that but it is like what what I think

## 14850:00 - 14890:00

is an exciting research direction that

## 14890:00 - 14935:00

we found in the inference time thinking

## 14935:00 - 14965:00

model space. Yeah. Can so can you talk

## 14965:00 - 14995:00

about what precisely it does different

## 14995:00 - 15045:00

than traditional reasoning models? Like

## 15045:00 - 15100:00

the current um reasoning thinking models

## 15100:00 - 15125:00

most of the time at least I can talk

## 15125:00 - 15160:00

from from our research point of view

## 15160:00 - 15215:00

builds a single chain of thought right

## 15215:00 - 15255:00

and then as you build a single chain of

## 15255:00 - 15285:00

thought and as the model continues to

## 15285:00 - 15335:00

attend to its chain of thought it builds

## 15335:00 - 15370:00

a better understanding of what response

## 15370:00 - 15410:00

it wants to give you. it can alternate

## 15410:00 - 15440:00

between different hypothesis reflect on

## 15440:00 - 15480:00

what it has done before. Now of course

## 15480:00 - 15515:00

like one if you think about it just also

## 15515:00 - 15550:00

in a visual kind of space. One kind of

## 15550:00 - 15585:00

scalability that you can bring onto the

## 15585:00 - 15625:00

table is can you have multiple parallel

## 15625:00 - 15670:00

chains of thoughts so that you can you

## 15670:00 - 15725:00

can actually um analyze different

## 15725:00 - 15770:00

hypotheses in parallel and then you will

## 15770:00 - 15805:00

have more capacity exploring different

## 15805:00 - 15845:00

kinds of hypothesis and then you can

## 15845:00 - 15885:00

look at you can compare those and then

## 15885:00 - 15920:00

you can eliminate the ones or you can

## 15920:00 - 15960:00

you can you can continue pursuing and

## 15960:00 - 15995:00

you can sort of expand on particular

## 15995:00 - 16045:00

ones. It's a very intuitive process in a

## 16045:00 - 16090:00

way but of course it is more involved. I

## 16090:00 - 16125:00

just want to cap this segment by asking

## 16125:00 - 16160:00

you um in terms of the pace of

## 16160:00 - 16190:00

improvement of models like I'm just

## 16190:00 - 16225:00

going to use the open AI uh schema just

## 16225:00 - 16280:00

to give an example. Um the progress this

## 16280:00 - 16310:00

is something that everybody who uh that

## 16310:00 - 16340:00

comes on the show says the progress of

## 16340:00 - 16410:00

going from like GPT3 to GPT4 was

## 16410:00 - 16480:00

undeniable. Um GPT4 to 4.5 less of a

## 16480:00 - 16515:00

leap. So I want to ask you just in terms

## 16515:00 - 16550:00

of the velocity of improvement if that's

## 16550:00 - 16580:00

the right way to put it. Are we coming

## 16580:00 - 16605:00

back down to earth a little bit right

## 16605:00 - 16650:00

now?

## 16650:00 - 16715:00

Um again when I look at our model family

## 16715:00 - 16785:00

right going from Gemini 1 to 1.5 to two

## 16785:00 - 16835:00

to now to 2.5 I'm very excited about the

## 16835:00 - 16875:00

pace that we have when I look at the

## 16875:00 - 16915:00

capabilities that we keep adding right

## 16915:00 - 16960:00

like uh we have always designed Gemini

## 16960:00 - 17000:00

models to be multimodel from the

## 17000:00 - 17020:00

beginning right like that was our

## 17020:00 - 17060:00

ambition because we want to build AGI we

## 17060:00 - 17110:00

want to make sure that uh we have models

## 17110:00 - 17140:00

that can fulfill the capabilities that

## 17140:00 - 17180:00

we expect from from from a general

## 17180:00 - 17225:00

intelligence. So multimodality was key

## 17225:00 - 17265:00

from the beginning and we have been as

## 17265:00 - 17310:00

the uh versions have been progressing we

## 17310:00 - 17335:00

have been adding that natural

## 17335:00 - 17370:00

multimodality more and more and more and

## 17370:00 - 17395:00

when when I look at the pace of

## 17395:00 - 17420:00

improvement in our reasoning

## 17420:00 - 17460:00

capabilities like lately we have added

## 17460:00 - 17500:00

the thinking capabilities and I think

## 17500:00 - 17555:00

with 2.5 pro um we wanted to make a big

## 17555:00 - 17605:00

leap in our reasoning capabilities our

## 17605:00 - 17645:00

coding capabilities and I think one of

## 17645:00 - 17670:00

the critical things is we are bringing

## 17670:00 - 17700:00

all these together in one single model

## 17700:00 - 17730:00

family and that is actually one of the

## 17730:00 - 17785:00

catalyzers of of of improvement and

## 17785:00 - 17830:00

improvement at pace as well. is harder,

## 17830:00 - 17850:00

but we find

## 17850:00 - 17895:00

that creating a single model that can

## 17895:00 - 17920:00

understand the world and then you can

## 17920:00 - 17970:00

ask questions about, oh, can you code me

## 17970:00 - 18010:00

um this this this sort of like a

## 18010:00 - 18055:00

simulation of a tree growing and then it

## 18055:00 - 18095:00

can do it right? that requires

## 18095:00 - 18125:00

understanding of a lot of the things not

## 18125:00 - 18170:00

just how to code because like again we

## 18170:00 - 18200:00

are trying to bring these models to be

## 18200:00 - 18270:00

useful to be usable by a very broad uh

## 18270:00 - 18330:00

audience and um I think our pace has

## 18330:00 - 18375:00

been really reflective of the research

## 18375:00 - 18405:00

investments that we have been doing

## 18405:00 - 18435:00

across the board. So no velocity

## 18435:00 - 18465:00

slowdown is what I'm hearing from you

## 18465:00 - 18540:00

which is good. Um look I think like let

## 18540:00 - 18575:00

me just put it in the way that I'm very

## 18575:00 - 18605:00

excited about everything that we have

## 18605:00 - 18645:00

been doing as Gemini progresses and

## 18645:00 - 18670:00

research is getting more and more

## 18670:00 - 18700:00

exciting. Of course like for us folks

## 18700:00 - 18735:00

who are doing research it is it's really

## 18735:00 - 18770:00

good. Okay. So I want to ask you you

## 18770:00 - 18800:00

know you're on the model side. I want to

## 18800:00 - 18850:00

ask you basically sometimes we debate on

## 18850:00 - 18880:00

the show what the value is of improving

## 18880:00 - 18915:00

models. So let me just like put a

## 18915:00 - 18950:00

thought experiment to you. Uh what do

## 18950:00 - 18990:00

you think the value of improving these

## 18990:00 - 19090:00

models by 10% would get us?

## 19090:00 - 19125:00

You froze for a second. So maybe if you

## 19125:00 - 19155:00

build up to the question maybe I missed

## 19155:00 - 19190:00

but I I got the latest part. Yeah. So

## 19190:00 - 19225:00

what do you think improving these models

## 19225:00 - 19270:00

by 10% would get us?

## 19270:00 - 19325:00

I think like um the question there is

## 19325:00 - 19375:00

like how do we define 10%.

## 19375:00 - 19435:00

Right. like uh that is where the um that

## 19435:00 - 19490:00

is where the value is defined already.

## 19490:00 - 19535:00

Right? One of the important things about

## 19535:00 - 19575:00

doing research and improving the models

## 19575:00 - 19625:00

is quantifying progress. Right? We use

## 19625:00 - 19670:00

many different ways to quantify progress

## 19670:00 - 19710:00

and not every one of them is linear and

## 19710:00 - 19750:00

not every one of them is linear with the

## 19750:00 - 19800:00

same slope. Right? So when we say by

## 19800:00 - 19865:00

improving 10% if we can improve 10% by

## 19865:00 - 19905:00

its understanding in math right

## 19905:00 - 19950:00

understanding of really highly complex

## 19950:00 - 20010:00

reasoning problems I think that is that

## 20010:00 - 20050:00

is a huge improvement because then that

## 20050:00 - 20090:00

actually expands the general knowledge

## 20090:00 - 20120:00

that that would indicate that the

## 20120:00 - 20145:00

general knowledge and the capabilities

## 20145:00 - 20205:00

of the models have expanded a lot right

## 20205:00 - 20240:00

and you would expect that that would

## 20240:00 - 20275:00

make the model a lot more applicable

## 20275:00 - 20335:00

able to a broader range of problems.

## 20335:00 - 20380:00

And what about if you uh improved the

## 20380:00 - 20425:00

model by like 50%. What would that get

## 20425:00 - 20460:00

you? Would the is your product team like

## 20460:00 - 20490:00

saying there are things that we can

## 20490:00 - 20535:00

build if this model was just like 50%

## 20535:00 - 20565:00

better?

## 20565:00 - 20605:00

Again, I think like we work with product

## 20605:00 - 20630:00

teams a lot, right? Like that's actually

## 20630:00 - 20665:00

a taking a step back. That's a that's a

## 20665:00 - 20705:00

quite important thing for me. um

## 20705:00 - 20755:00

thinking about AGI as a goal I think

## 20755:00 - 20785:00

that also goes through working with the

## 20785:00 - 20800:00

product

## 20800:00 - 20850:00

teams because it is important that when

## 20850:00 - 20885:00

we are building AGI it's a research

## 20885:00 - 20940:00

problem. Mhm. We are doing research but

## 20940:00 - 20975:00

the most critical thing is we we

## 20975:00 - 21005:00

actually understand what kind of

## 21005:00 - 21035:00

problems to solve what kind of domains

## 21035:00 - 21085:00

to evoke these models from the users. So

## 21085:00 - 21135:00

that user feedback and that knowledge

## 21135:00 - 21180:00

from the interaction with the users is

## 21180:00 - 21215:00

actually quite critical. So when our

## 21215:00 - 21250:00

products tell us about okay here is an

## 21250:00 - 21295:00

area that we want to improve on then

## 21295:00 - 21320:00

that is actually quite important

## 21320:00 - 21365:00

feedback for us that we can then turn

## 21365:00 - 21425:00

into metrics and and and and pursue

## 21425:00 - 21480:00

those like as you ask like I mean if as

## 21480:00 - 21515:00

we increase the capabilities of the

## 21515:00 - 21545:00

model across I think what is important

## 21545:00 - 21590:00

is across a broad range of metrics which

## 21590:00 - 21635:00

I think we have been seeing in Gemini as

## 21635:00 - 21705:00

I said from like 1.5 to 2.5 right You

## 21705:00 - 21750:00

can see the capability increases across

## 21750:00 - 21795:00

the model. A lot more people can

## 21795:00 - 21835:00

actually use the models in their daily

## 21835:00 - 21890:00

life to help them to to either learn

## 21890:00 - 21950:00

something new or to help them solve a an

## 21950:00 - 21985:00

issue that they see. But that's the

## 21985:00 - 22020:00

goal, right? Like at the end of the day

## 22020:00 - 22065:00

again like the like the reason we build

## 22065:00 - 22100:00

this technology is to build something

## 22100:00 - 22150:00

that is helpful and the products are a

## 22150:00 - 22185:00

critical aspect of how we measure and

## 22185:00 - 22220:00

how we understand what is helpful and

## 22220:00 - 22255:00

what is not and as we increase more in

## 22255:00 - 22290:00

that I think that's that's our main

## 22290:00 - 22325:00

ambition that's great let's take a

## 22325:00 - 22370:00

concrete example that again the company

## 22370:00 - 22405:00

Google is releasing today talking about

## 22405:00 - 22460:00

today which is uh V3 so this is your

## 22460:00 - 22495:00

video generation model and I I think

## 22495:00 - 22540:00

we've really seen an unbelievable uh

## 22540:00 - 22570:00

acceleration in terms of what these

## 22570:00 - 22605:00

models can do from the first generation

## 22605:00 - 22640:00

to second generation to the third. And

## 22640:00 - 22665:00

for listeners and viewers, what's hap

## 22665:00 - 22705:00

what Google is doing now is not only are

## 22705:00 - 22745:00

you able to generate scenes. Uh you're

## 22745:00 - 22805:00

able to generate them with sound. And

## 22805:00 - 22835:00

having watched one of these videos or a

## 22835:00 - 22860:00

couple of them, I can tell you the sound

## 22860:00 - 22905:00

matches. Um and then there's this other

## 22905:00 - 22940:00

crazy product that Google's putting out.

## 22940:00 - 22970:00

I think it's called flow where you could

## 22970:00 - 23010:00

just extend the scene that you've

## 23010:00 - 23060:00

generated and storyboard out like your

## 23060:00 - 23110:00

own ba basically short film. Yeah. So I

## 23110:00 - 23145:00

I'd love to hear your perspective on how

## 23145:00 - 23200:00

this happened and is this like you know

## 23200:00 - 23220:00

I kind of asked you what do we get at

## 23220:00 - 23270:00

10% 50% but is this kind of that perfect

## 23270:00 - 23320:00

example of um the model getting better

## 23320:00 - 23355:00

producing something that goes from you

## 23355:00 - 23385:00

know that's a fun little video to like

## 23385:00 - 23445:00

oh I can really use this now. Yes.

## 23445:00 - 23525:00

Um I think the main difference the main

## 23525:00 - 23600:00

um the main progress going from V2 to V3

## 23600:00 - 23650:00

from V1 to V2 it was a lot more about

## 23650:00 - 23685:00

understanding the physics and the

## 23685:00 - 23740:00

dynamics of the world with V2 I think

## 23740:00 - 23770:00

for the first time we could comfortably

## 23770:00 - 23835:00

say that for many many cases right the

## 23835:00 - 23870:00

model has understood the dynamics of the

## 23870:00 - 23905:00

world well that's very important right

## 23905:00 - 23975:00

like to be able to have a model that can

## 23975:00 - 24040:00

generate scenes and and and complex

## 24040:00 - 24090:00

scenes where there's dynamic environment

## 24090:00 - 24125:00

happening and also there's interactions

## 24125:00 - 24170:00

of objects happening. I remember one of

## 24170:00 - 24225:00

the things that was quite viral was like

## 24225:00 - 24255:00

cutting the tomato where it was so

## 24255:00 - 24310:00

precise the video generated by V2 that

## 24310:00 - 24355:00

um it looks so realistic that one like

## 24355:00 - 24395:00

like a person was slicing tomatoes and

## 24395:00 - 24445:00

the dynamics there and the and and how

## 24445:00 - 24495:00

both the like not just any single object

## 24495:00 - 24540:00

like how the hand moves but also the

## 24540:00 - 24575:00

interaction between the between

## 24575:00 - 24605:00

different objects the blade the tomato

## 24605:00 - 24645:00

how the slice falls down and everything.

## 24645:00 - 24675:00

It was very precise. Right? So that

## 24675:00 - 24705:00

interactive element was important.

## 24705:00 - 24745:00

Understanding the dynamics is about not

## 24745:00 - 24775:00

just understanding the dynamics of a

## 24775:00 - 24825:00

particular single object but it's also

## 24825:00 - 24855:00

multiple objects interacting with each

## 24855:00 - 24895:00

other which is much much more

## 24895:00 - 24935:00

complex. So I think there we had a big

## 24935:00 - 24975:00

jump with V3. I think we are doing

## 24975:00 - 25025:00

another jump in that aspect. But I see

## 25025:00 - 25075:00

the sound as an orthogonal a new

## 25075:00 - 25105:00

capability that is coming in. Of course,

## 25105:00 - 25140:00

our real world we have multiple senses

## 25140:00 - 25180:00

and vision and sound go hand in hand,

## 25180:00 - 25205:00

right? Like they are perfectly

## 25205:00 - 25245:00

correlated. We perceive them all the all

## 25245:00 - 25280:00

at the same time and they complement

## 25280:00 - 25320:00

each other. So to be able to have a

## 25320:00 - 25345:00

model that understands that

## 25345:00 - 25390:00

interactivity, that complimentarity and

## 25390:00 - 25450:00

being able to generate scenes and videos

## 25450:00 - 25500:00

that can generate both at the same time.

## 25500:00 - 25535:00

I think that speaks to the new like the

## 25535:00 - 25580:00

capability level of the model and like

## 25580:00 - 25625:00

the quality. I think like this is the

## 25625:00 - 25660:00

first step like there are very

## 25660:00 - 25695:00

impressive examples. there are examples

## 25695:00 - 25725:00

that are like um a little bit more

## 25725:00 - 25760:00

falling short of what you would say okay

## 25760:00 - 25800:00

this is really natural but like I think

## 25800:00 - 25835:00

this is an exciting step in terms of

## 25835:00 - 25870:00

expanding that capability and as you

## 25870:00 - 25915:00

said I think I'm excited to see how like

## 25915:00 - 25950:00

this kind of technology can be useful

## 25950:00 - 25990:00

right like you just said that oh it is

## 25990:00 - 26020:00

becoming useful I think that is great to

## 26020:00 - 26060:00

hear right like that like now this is a

## 26060:00 - 26090:00

technology that can be built and I think

## 26090:00 - 26125:00

flow is an experiment in that direction

## 26125:00 - 26180:00

to give it to the uh to give it to users

## 26180:00 - 26230:00

So that like for for for people to

## 26230:00 - 26265:00

experiment and build something with it.

## 26265:00 - 26290:00

Yeah. You like prompt a scene and then

## 26290:00 - 26310:00

they create that creates a scene then

## 26310:00 - 26340:00

you prompt the next scene and you can

## 26340:00 - 26380:00

continue to have a flow a story flow

## 26380:00 - 26410:00

which is a good good name for it. All

## 26410:00 - 26445:00

right. This next question comes to me

## 26445:00 - 26525:00

from a pretty smart uh AI researcher. um

## 26525:00 - 26565:00

they basically talked about how there's

## 26565:00 - 26615:00

this basic uh there's a tension between

## 26615:00 - 26665:00

open- source and proprietary and of

## 26665:00 - 26690:00

course we have companies like Google

## 26690:00 - 26735:00

that's building um you know obviously

## 26735:00 - 26750:00

attention is all you need the

## 26750:00 - 26780:00

transformer came from Google now

## 26780:00 - 26810:00

Google's building proprietary models we

## 26810:00 - 26865:00

saw deepseeek uh push the the um

## 26865:00 - 26905:00

state-of-the-art forward you could argue

## 26905:00 - 26945:00

u so this this person wanted to know and

## 26945:00 - 26985:00

I think it's a really good question um

## 26985:00 - 27060:00

is there a coordin ation or um or or

## 27060:00 - 27105:00

possible between open source and

## 27105:00 - 27140:00

proprietary. I mean we see open AAI

## 27140:00 - 27175:00

doing the you know their new open source

## 27175:00 - 27230:00

model or teasing it or should each uh

## 27230:00 - 27275:00

sort of side try to get its own part of

## 27275:00 - 27315:00

the market. What do you think?

## 27315:00 - 27350:00

Um I think like I want to say a couple

## 27350:00 - 27380:00

of things right like

## 27380:00 - 27440:00

um first and foremost again like take a

## 27440:00 - 27480:00

step back like there's a lot of research

## 27480:00 - 27515:00

that went into building this technology

## 27515:00 - 27550:00

right like of of course like in the last

## 27550:00 - 27610:00

like um two three years I think it

## 27610:00 - 27650:00

became so accessible and so general that

## 27650:00 - 27685:00

people are using in their daily lives

## 27685:00 - 27710:00

but there's a long history of research

## 27710:00 - 27765:00

that built up to this point right so

## 27765:00 - 27815:00

like as a research lab Google and like

## 27815:00 - 27840:00

before of course like there's deep mind

## 27840:00 - 27880:00

and Google brain two separate labs that

## 27880:00 - 27925:00

are working in tandem um in different

## 27925:00 - 27965:00

aspects and many of the technologies

## 27965:00 - 28010:00

that we see today has been built as

## 28010:00 - 28050:00

research prototypes right as research

## 28050:00 - 28090:00

ideas and have been published in papers

## 28090:00 - 28115:00

as you said transformers the most

## 28115:00 - 28145:00

critical technology that is underlying

## 28145:00 - 28200:00

things and then uh and then models like

## 28200:00 - 28245:00

Alph Go right alpha fold all of these

## 28245:00 - 28285:00

kinds of things all these research ideas

## 28285:00 - 28325:00

have been evolving into building the

## 28325:00 - 28365:00

knowledge space that we have right now.

## 28365:00 - 28415:00

All that research I think publications

## 28415:00 - 28455:00

and and and and open sourcing all those

## 28455:00 - 28485:00

have been a critical element because we

## 28485:00 - 28530:00

were uh we were we were really in the

## 28530:00 - 28570:00

exploratory space at those times.

## 28570:00 - 28620:00

Nowadays I think like the other thing

## 28620:00 - 28670:00

that we always like need to remember is

## 28670:00 - 28700:00

actually we have at Google we have our

## 28700:00 - 28730:00

GMA models right that that are there

## 28730:00 - 28760:00

that are the open weights models just

## 28760:00 - 28790:00

like llama open weights models we have

## 28790:00 - 28825:00

the gem open weights models the reason

## 28825:00 - 28875:00

to do those for us is also there's a

## 28875:00 - 28925:00

different community of developers and

## 28925:00 - 28965:00

users who want to interact with those

## 28965:00 - 29005:00

models who actually need that kind of

## 29005:00 - 29040:00

being able to download those weights

## 29040:00 - 29065:00

into their own environment enironment

## 29065:00 - 29105:00

and use that and and and build with

## 29105:00 - 29145:00

that. So I feel like it's not an

## 29145:00 - 29185:00

eitheror. I think there are different

## 29185:00 - 29235:00

kinds of use cases and communities that

## 29235:00 - 29270:00

actually benefit from different kinds of

## 29270:00 - 29310:00

models. But what is most important is at

## 29310:00 - 29360:00

the end of the day in the in the path

## 29360:00 - 29415:00

towards AGI of course it's important

## 29415:00 - 29465:00

that we are being conscious about what

## 29465:00 - 29505:00

we enable with the technologies that we

## 29505:00 - 29550:00

develop. So when we develop our frontier

## 29550:00 - 29595:00

technologies, we t we we choose to

## 29595:00 - 29635:00

develop them under the Gemini umbrella

## 29635:00 - 29670:00

which are not open weights models

## 29670:00 - 29720:00

because we want to also make sure that

## 29720:00 - 29750:00

we can be responsible in the way that

## 29750:00 - 29805:00

they are used as well. Right. Right. But

## 29805:00 - 29830:00

at the end of the day, what really

## 29830:00 - 29865:00

matters is the research that goes into

## 29865:00 - 29910:00

building the technology and doing that

## 29910:00 - 29945:00

research and pushing the frontier of the

## 29945:00 - 29970:00

technology and building it the right way

## 29970:00 - 30010:00

with the positive impact. And I think it

## 30010:00 - 30040:00

can happen both in open weights

## 30040:00 - 30090:00

ecosystem or in the closed system. But I

## 30090:00 - 30155:00

think like when I think about all the um

## 30155:00 - 30185:00

sort of the umbrella of things that we

## 30185:00 - 30225:00

are trying to do, we are quite ambitious

## 30225:00 - 30270:00

goals building AGI and doing it the

## 30270:00 - 30300:00

right way with the positive impact.

## 30300:00 - 30340:00

That's how we develop our Gemini models.

## 30340:00 - 30365:00

Okay. I have like 30 seconds left with

## 30365:00 - 30410:00

you. You're chief technology officer. Uh

## 30410:00 - 30465:00

are you a fan of vibe coding?

## 30465:00 - 30515:00

Yes, exactly. I I find it really

## 30515:00 - 30550:00

exciting, right? Like I mean because

## 30550:00 - 30595:00

like what it does is all of a sudden it

## 30595:00 - 30635:00

enables a lot of people who are not

## 30635:00 - 30675:00

necessarily who do not necessarily have

## 30675:00 - 30700:00

that coding background to build

## 30700:00 - 30735:00

applications. It's a whole new world

## 30735:00 - 30780:00

that is opening right like u you can

## 30780:00 - 30805:00

actually say oh I want an application

## 30805:00 - 30855:00

like this and then you you see it you

## 30855:00 - 30885:00

can imagine what kinds of things could

## 30885:00 - 30920:00

be possible in the space of learning

## 30920:00 - 30950:00

right you want to learn about something

## 30950:00 - 30980:00

you can you can have a textual

## 30980:00 - 31015:00

representation but you can ask the model

## 31015:00 - 31050:00

to build you an application that

## 31050:00 - 31085:00

explains you certain concepts and it

## 31085:00 - 31120:00

would do it right and this is the

## 31120:00 - 31145:00

beginning right like some things it does

## 31145:00 - 31175:00

well some things it doesn't well it

## 31175:00 - 31210:00

doesn't do well but I find it really

## 31210:00 - 31235:00

exciting. This is the kinds of things

## 31235:00 - 31265:00

that the technology brings. All of a

## 31265:00 - 31315:00

sudden like the whole space of building

## 31315:00 - 31350:00

applications, the whole space of

## 31350:00 - 31420:00

building um dynamic interactive

## 31420:00 - 31490:00

applications becomes accessible to a

## 31490:00 - 31530:00

large broader community and set of

## 31530:00 - 31570:00

people. All right, great to see you.

## 31570:00 - 31590:00

Thank you so much for coming on the

## 31590:00 - 31625:00

show. Yeah, thank you very much. Thanks

## 31625:00 - 31650:00

for inviting Alex. Definitely. We'll

## 31650:00 - 31680:00

have to do it again in person sometime.

## 31680:00 - 31710:00

All right, everybody. Thank you for

## 31710:00 - 31740:00

listening. We'll have Dennis Asabis on

## 31740:00 - 31795:00

the CEO of Google DeepMind tomorrow and

## 31795:00 - 31830:00

so we invite you to join us then. We'll

## 31830:00 - 31860:00

see you next time on Big Technology

## 31860:00+

Podcast.

