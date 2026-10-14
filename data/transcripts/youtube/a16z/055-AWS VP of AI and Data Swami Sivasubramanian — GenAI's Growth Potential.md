---
source: https://www.youtube.com/watch?v=DmUjdOXGw9c
title: AWS VP of AI and Data Swami Sivasubramanian — GenAI's Growth Potential
author: Alex Kantrowitz
date: 2024-05-01
views: 2129
description: Swami Sivasubramanian is the VP of AI and Data at Amazon Web
  Services (AWS). Swami joins me in a Youtube exclusive to discuss the future of
  artificial intelligence and the potential of large language models. Tune in to
  hear Swami's insights on the scalability of AI systems, the impact of compute
  and energy constraints, and the role of architectural innovations in driving
  progress. We also cover topics like multimodal AI, reasoning capabilities,
  on-device vs. cloud inference, and the business applications of language
  models. Hit playfor an in-depth exploration of the state of the art in AI and
  where the field is headed, from one of the leading experts at AWS.
tags:
  - AWS AI
  - Swami Sivasubramanian
  - Amazon Web Services AI
  - Future of AI
  - Large Language Models
  - AI Scalability
  - AI Compute Constraints
  - AI Energy Constraints
  - AI Model Architectures
  - Multimodal AI
  - AI Reasoning Capabilities
  - On-Device AI Inference
  - Cloud AI Inference
  - Business Applications of AI
  - Conversational AI
  - Generative AI
  - AI Innovation
  - AI Trends
  - AI Insights
  - Tech Interviews
  - AI Podcast
  - AWS Executives
  - Foundational Models
  - Open Source AI Models
  - AI Chips
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:34:17.793Z
---

# AWS VP of AI and Data Swami Sivasubramanian — GenAI's Growth Potential

## 00:00 - 15:00

we're going to talk about some of the

## 15:00 - 50:00

big pressing issues in generative AI

## 50:00 - 90:00

including whether generative AI has that

## 90:00 - 115:00

much more room to run given the

## 115:00 - 155:00

constraints on data compute and even

## 155:00 - 190:00

energy we are joined today with by a

## 190:00 - 240:00

very special guest Swami CA subra Manan

## 240:00 - 295:00

is here he's the VP of AI and data at

## 295:00 - 330:00

AWS and we're so lucky to have yet

## 330:00 - 365:00

another executive from Amazon web

## 365:00 - 405:00

services here Swami great to see you

## 405:00 - 455:00

thank you so much for coming on hey uh

## 455:00 - 485:00

thanks for having me really looking

## 485:00 - 520:00

forward to our con

## 520:00 - 570:00

me too and there was a moment in the

## 570:00 - 605:00

podcast that I watched recently and

## 605:00 - 645:00

listened to recently where Mark

## 645:00 - 670:00

Zuckerberg was talking about the

## 670:00 - 720:00

potential constraints on the further

## 720:00 - 780:00

building of generative AI systems and

## 780:00 - 805:00

the training and the inference of them

## 805:00 - 850:00

and he said you got to ask Amazon and

## 850:00 - 885:00

actually here we are we're with Amazon

## 885:00 - 910:00

so let me set it up for you and then I'm

## 910:00 - 955:00

going to ask you the question okay so

## 955:00 - 1015:00

he's on this podcast with dwares fotel

## 1015:00 - 1040:00

and they're talking about whether we're

## 1040:00 - 1080:00

going to hit a wall with llms because if

## 1080:00 - 1115:00

you think about llama 3 which met a just

## 1115:00 - 1155:00

release which we just talked about uh it

## 1155:00 - 1185:00

trained with 10 times more data and a

## 1185:00 - 1215:00

100 times more compute and dwares was

## 1215:00 - 1260:00

trying to get Mark to say well where's

## 1260:00 - 1285:00

the limit here in terms of you're going

## 1285:00 - 1310:00

to you know press you're pressing

## 1310:00 - 1345:00

resources on computer you're pressing

## 1345:00 - 1375:00

resources on data are you going to

## 1375:00 - 1410:00

eventually hit an end and Zuckerberg of

## 1410:00 - 1450:00

course says that energy is the real

## 1450:00 - 1500:00

question right that it's it's a fact

## 1500:00 - 1515:00

that if you're going to train these

## 1515:00 - 1545:00

models and run these models you need

## 1545:00 - 1585:00

very big data centers uh and he talked

## 1585:00 - 1610:00

about the fact that you might even need

## 1610:00 - 1665:00

a gigawatt data center which is

## 1665:00 - 1700:00

effectively as big as a you know a

## 1700:00 - 1745:00

nuclear power plant and dwares and this

## 1745:00 - 1775:00

is the the point here and then we're

## 1775:00 - 1810:00

going to let you talk dwares was like

## 1810:00 - 1845:00

didn't Amazon do this and Mark

## 1845:00 - 1895:00

Zuckerberg says you have to ask them so

## 1895:00 - 1920:00

I'm curious what you think about the

## 1920:00 - 1945:00

constraints of data when it comes to

## 1945:00 - 1990:00

training large language model models and

## 1990:00 - 2015:00

then maybe you can talk about your

## 2015:00 - 2045:00

efforts since uh Mark Zuckerberg

## 2045:00 - 2085:00

suggests that we ask

## 2085:00 - 2160:00

you all right uh first of all uh just to

## 2160:00 - 2200:00

give some context I

## 2200:00 - 2275:00

mean uh I'll just say AI is first uh has

## 2275:00 - 2325:00

the most transformative technology and

## 2325:00 - 2370:00

potential uh for us it is the most

## 2370:00 - 2430:00

transformative technology and uh the

## 2430:00 - 2465:00

reason we are having this moment and all

## 2465:00 - 2515:00

these uh conversation is because uh the

## 2515:00 - 2560:00

Advent of Transformer Technologies which

## 2560:00 - 2620:00

is uh the new neural net architecture

## 2620:00 - 2660:00

which helps us build these large

## 2660:00 - 2720:00

language models that uh can learn from

## 2720:00 - 2785:00

huge amount of data but also be able to

## 2785:00 - 2820:00

uh actually scale it up that means you

## 2820:00 - 2860:00

can throw more computer and more data

## 2860:00 - 2890:00

and then it naturally gets better and

## 2890:00 - 2945:00

better so that is uh the reason why now

## 2945:00 - 3010:00

suddenly AI is having its moment now uh

## 3010:00 - 3040:00

to get to your

## 3040:00 - 3095:00

question where does it stop where is the

## 3095:00 - 3125:00

this is what researchers call it as like

## 3125:00 - 3165:00

scaling loss saying like is it actually

## 3165:00 - 3190:00

constantly are we going to keep throwing

## 3190:00 - 3230:00

more and more compute and more and more

## 3230:00 - 3265:00

data or is there no more compute left or

## 3265:00 - 3315:00

no more data left in the world and uh

## 3315:00 - 3380:00

this is where uh few things uh suspect

## 3380:00 - 3420:00

is going to happen one I don't think we

## 3420:00 - 3485:00

are anywhere uh close to yet uh hitting

## 3485:00 - 3550:00

that wall yet uh so I do think um we are

## 3550:00 - 3590:00

going to actually see lot of net new

## 3590:00 - 3635:00

Innovations uh when it comes to

## 3635:00 - 3675:00

optimizing how to actually train these

## 3675:00 - 3720:00

models in parallel and get better

## 3720:00 - 3765:00

utilization so that we can continue to

## 3765:00 - 3815:00

actually build these models uh really

## 3815:00 - 3875:00

well I mean AWS actually for instance uh

## 3875:00 - 3925:00

we have invested in Technologies uh such

## 3925:00 - 3970:00

as uh trinium 2 chips which actually can

## 3970:00 - 4035:00

deliver up to 4X fast training and uh

## 4035:00 - 4075:00

also it is while improving Energy

## 4075:00 - 4125:00

Efficiency up to two times as an example

## 4125:00 - 4165:00

so Innovation and compute Innovation is

## 4165:00 - 4205:00

compute is only one now the second thing

## 4205:00 - 4245:00

is uh right now many of the scaling laws

## 4245:00 - 4285:00

and others are also built upon the

## 4285:00 - 4320:00

Assumption of a certain kind of

## 4320:00 - 4360:00

architectures but if you see already

## 4360:00 - 4390:00

when it comes to how these models are

## 4390:00 - 4440:00

train and if you see there are starting

## 4440:00 - 4490:00

to see new kinds of architectures that

## 4490:00 - 4545:00

are going to change how these models

## 4545:00 - 4600:00

scale in the future and I suspect uh

## 4600:00 - 4660:00

that is going to change uh how these uh

## 4660:00 - 4690:00

scaling losss are going to be reshaped

## 4690:00 - 4740:00

as well when it comes to that that is

## 4740:00 - 4785:00

going to drive net new efficiency gain

## 4785:00 - 4830:00

as well and uh so compute the

## 4830:00 - 4870:00

architecture of the model architecture

## 4870:00 - 4890:00

of the model but you still didn't answer

## 4890:00 - 4940:00

my question about energy and so I want

## 4940:00 - 4970:00

to let me just put a put a fine point on

## 4970:00 - 5020:00

it right yeah have you built what is the

## 5020:00 - 5065:00

biggest data center that you've built to

## 5065:00 - 5100:00

train these models in terms of I don't

## 5100:00 - 5130:00

know me megawatts or

## 5130:00 - 5195:00

gigawatts um and do you think that there

## 5195:00 - 5230:00

comes a point where energy becomes the

## 5230:00 - 5255:00

biggest constraint on these things

## 5255:00 - 5295:00

because that is exactly what Zuckerberg

## 5295:00 - 5350:00

is saying and this is a guy who has in

## 5350:00 - 5430:00

his back pocket 650,000 Nvidia h100 gpus

## 5430:00 - 5465:00

or equivalent so I think he has an idea

## 5465:00 - 5515:00

of you know what the resource constraint

## 5515:00 - 5560:00

might be after you take care of compute

## 5560:00 - 5605:00

yeah think compute and energy are going

## 5605:00 - 5645:00

to be uh along with data are the three

## 5645:00 - 5680:00

dimensions where the stealing

## 5680:00 - 5715:00

constraints are going to be um but focus

## 5715:00 - 5760:00

on the energy stuff yeah the energy

## 5760:00 - 5800:00

stuff is a constraint but U that is why

## 5800:00 - 5840:00

AWS if you see when you offer compute we

## 5840:00 - 5870:00

are not just offering server we are

## 5870:00 - 5915:00

actually offering a cluster that uh

## 5915:00 - 5965:00

comes with all of it and the uh this is

## 5965:00 - 6030:00

an area where uh um we have always been

## 6030:00 - 6075:00

um investing a lot not just to actually

## 6075:00 - 6115:00

procure more energy but also to be more

## 6115:00 - 6180:00

energy efficient as well so I think U

## 6180:00 - 6230:00

there is an inherent actually what is

## 6230:00 - 6265:00

going on with the industry though is

## 6265:00 - 6320:00

especially in the AI space is the rate

## 6320:00 - 6370:00

of scaling and demand is so incredibly

## 6370:00 - 6425:00

high that that's why you starting to see

## 6425:00 - 6475:00

energy uh consumption needs are also

## 6475:00 - 6535:00

increasing in a big way and uh we are

## 6535:00 - 6575:00

actually innovating in big way not just

## 6575:00 - 6625:00

in uh building our data centers and

## 6625:00 - 6680:00

capacity and uh doing more on this front

## 6680:00 - 6710:00

and we have made lots of announcements

## 6710:00 - 6765:00

even uh including uh today on uh some of

## 6765:00 - 6815:00

the new regions we are expanding and so

## 6815:00 - 6855:00

forth uh including in Indiana and

## 6855:00 - 6905:00

whatnot but uh the other aspect that is

## 6905:00 - 6950:00

equally important is also how do you

## 6950:00 - 6995:00

actually make this energy sustainable

## 6995:00 - 7035:00

and that continues to be a big priority

## 7035:00 - 7085:00

for us and right no everybody agrees

## 7085:00 - 7125:00

that making it sustainable is important

## 7125:00 - 7150:00

but I want to get back to this this

## 7150:00 - 7200:00

constraint here is there is there I mean

## 7200:00 - 7230:00

it seems like what you're also pointing

## 7230:00 - 7280:00

at here is there is legitimacy in this

## 7280:00 - 7310:00

idea that the industry is sort of coming

## 7310:00 - 7365:00

up against an En energy

## 7365:00 - 7425:00

constraint uh yeah there is actually uh

## 7425:00 - 7450:00

all this going to be we are going to be

## 7450:00 - 7490:00

compute and energy constraint when it it

## 7490:00 - 7540:00

comes to this uh but this is where I do

## 7540:00 - 7595:00

think uh that constraint also is uh

## 7595:00 - 7645:00

contingent on that um certain things

## 7645:00 - 7685:00

around how these models are architected

## 7685:00 - 7730:00

and so forth that is where I'm saying so

## 7730:00 - 7765:00

it is uh currently all these going to be

## 7765:00 - 7820:00

true and this is where uh cloud is

## 7820:00 - 7850:00

actually making it better that is the

## 7850:00 - 7895:00

Nuance uh I'm actually talking about and

## 7895:00 - 7930:00

then net new architectures are going to

## 7930:00 - 7990:00

be better net new chip uh designs are

## 7990:00 - 8040:00

also going to make it better so

## 8040:00 - 8075:00

I and so we should talk a little bit

## 8075:00 - 8115:00

about the way that llms are going to be

## 8115:00 - 8495:00

rearchitecturing

## 8495:00 - 8525:00

an important issue here but now going

## 8525:00 - 8560:00

back to these two Legacy problems of

## 8560:00 - 8620:00

data and compute uh and and you think

## 8620:00 - 8650:00

about the way that these models have

## 8650:00 - 8705:00

grown you know just the Llama example

## 8705:00 - 8755:00

for instance 10 times more data 100

## 8755:00 - 8785:00

times more compute I mean they had

## 8785:00 - 8810:00

clusters of I think

## 8810:00 - 8865:00

32,000 or 24,000 something some crazy

## 8865:00 - 8910:00

number of Nvidia chips put together so

## 8910:00 - 8935:00

they they you know and that's from some

## 8935:00 - 8985:00

of like the healthiest compute resources

## 8985:00 - 9030:00

in the whole industry the data they also

## 9030:00 - 9065:00

started effectively running out there

## 9065:00 - 9110:00

was a story in the New York Times where

## 9110:00 - 9145:00

um internally at meta they were saying

## 9145:00 - 9165:00

if we don't get more data we're never

## 9165:00 - 9200:00

going to catch up with chat GPT and even

## 9200:00 - 9265:00

started to consider buying uh Simon and

## 9265:00 - 9325:00

Schuster or spending $10 a book to get

## 9325:00 - 9380:00

the data necessary to train um so I

## 9380:00 - 9400:00

guess this is the question for you

## 9400:00 - 9420:00

because you're in this position here

## 9420:00 - 9450:00

right again like it's so cool to speak

## 9450:00 - 9480:00

with someone at AWS because you have all

## 9480:00 - 9505:00

these resources and you know how the

## 9505:00 - 9540:00

data center works this is your your

## 9540:00 - 9585:00

bread and butter so before we get into

## 9585:00 - 9635:00

the new architecture just quickly yeah

## 9635:00 - 9685:00

is the traditional way of training these

## 9685:00 - 9750:00

llms is that going to hit a wall because

## 9750:00 - 9780:00

you know it seems like there's fairly

## 9780:00 - 9815:00

little data left to use and the compute

## 9815:00 - 9845:00

might be kind of running out also so is

## 9845:00 - 9880:00

it sort of like not a nice to have but a

## 9880:00 - 9925:00

must have that new architectures are

## 9925:00 - 9995:00

necessary um I I uh I actually think uh

## 9995:00 - 10030:00

new architectures are absolutely

## 10030:00 - 10080:00

necessary in the future uh and uh there

## 10080:00 - 10110:00

are already hybrid architectures

## 10110:00 - 10175:00

evolving I mean uh I mean um in terms of

## 10175:00 - 10205:00

State space models to actually

## 10205:00 - 10245:00

connectors Hybrid models between State

## 10245:00 - 10325:00

space to uh Transformers and so forth uh

## 10325:00 - 10370:00

but also actually how we are training

## 10370:00 - 10405:00

some of these large language models with

## 10405:00 - 10445:00

even the current data how do they get

## 10445:00 - 10485:00

reinforced and all all those things

## 10485:00 - 10535:00

there is still lot of room uh left in

## 10535:00 - 10575:00

comes to how these models are getting

## 10575:00 - 10645:00

trained uh and uh you already are seeing

## 10645:00 - 10700:00

actually even uh meta for instance uh

## 10700:00 - 10730:00

published a book it is all about

## 10730:00 - 10780:00

actually high quality data than uh lots

## 10780:00 - 10830:00

of data uh and then being able to Cherry

## 10830:00 - 10870:00

bake and do the right cleansing and so

## 10870:00 - 10900:00

forth is number one and then the second

## 10900:00 - 10940:00

thing is also it is not about bigger and

## 10940:00 - 10970:00

bigger model when you look at actually

## 10970:00 - 11015:00

what Enterprise as one because your view

## 11015:00 - 11055:00

is purely on just model providers who

## 11055:00 - 11095:00

are trying to build model but take an

## 11095:00 - 11130:00

Enterprise uh who wants to use these

## 11130:00 - 11180:00

models to actually build an chatboard

## 11180:00 - 11230:00

agent or being able to morgage provider

## 11230:00 - 11275:00

like rocket mortgage uh and so forth

## 11275:00 - 11310:00

that they want to actually test it in

## 11310:00 - 11335:00

production it's not about actually

## 11335:00 - 11380:00

picking the most capable model but it uh

## 11380:00 - 11420:00

in terms of model size or so forth but

## 11420:00 - 11460:00

they want to be able to take a model and

## 11460:00 - 11495:00

customize it with their data using

## 11495:00 - 11535:00

different techniques uh and then being

## 11535:00 - 11585:00

able to get business outcome so for them

## 11585:00 - 11620:00

it is not about the most capable model

## 11620:00 - 11660:00

but it is the most flexible model that

## 11660:00 - 11720:00

actually achieves the tradeoff between

## 11720:00 - 11780:00

their cost accuracy and latency needs

## 11780:00 - 11830:00

and then uh picking that so right this

## 11830:00 - 11890:00

is where I do think um our service like

## 11890:00 - 11945:00

Amazon Bedrock which actually helps with

## 11945:00 - 11980:00

uh not just actually always saying the

## 11980:00 - 12020:00

answer is always the biggest model but

## 12020:00 - 12080:00

instead uh making it super easy to pick

## 12080:00 - 12110:00

from an variety of state-of-the-art

## 12110:00 - 12170:00

models it can be like anthropic or uh

## 12170:00 - 12235:00

Amazon or AI 21 coh here meta mesal or

## 12235:00 - 12275:00

any of them but then making it super

## 12275:00 - 12310:00

easy to evaluate for their use case and

## 12310:00 - 12350:00

then build actually an retrieval

## 12350:00 - 12380:00

augmented generation with the right set

## 12380:00 - 12415:00

of guardrails is going to be big deal

## 12415:00 - 12450:00

and that's why we are already seeing

## 12450:00 - 12495:00

like tens of thousands of customers

## 12495:00 - 12555:00

actually um leveraging rock and the key

## 12555:00 - 12595:00

thing and this is where it's super easy

## 12595:00 - 12640:00

for us to get all this inamed about what

## 12640:00 - 12685:00

is the most uh capable model but to put

## 12685:00 - 12730:00

these llms to work to solve real world

## 12730:00 - 12775:00

problems you got to actually take some

## 12775:00 - 12825:00

of these models and then customize it

## 12825:00 - 12855:00

and the end result is not the biggest

## 12855:00 - 12890:00

model it is actually a much more

## 12890:00 - 12935:00

customized smaller model or a distal

## 12935:00 - 12965:00

model to solve specific business

## 12965:00 - 13015:00

problems and that's why is important

## 13015:00 - 13055:00

well I sort of disagree with you on that

## 13055:00 - 13080:00

I I mean I agree with you that the

## 13080:00 - 13115:00

application is important but the thing

## 13115:00 - 13145:00

that's most important of course is how

## 13145:00 - 13185:00

this stuff continues

## 13185:00 - 13245:00

to uh evolve and get better

## 13245:00 - 13290:00

right uh you wouldn't be satisfied just

## 13290:00 - 13335:00

saying let's stop with what we have now

## 13335:00 - 13370:00

no actually that is not what I'm uh

## 13370:00 - 13425:00

saying uh I'm actually saying uh that

## 13425:00 - 13465:00

you're not hitting a wall from an uh

## 13465:00 - 13500:00

customer perspective who are actually

## 13500:00 - 13535:00

building or innovating with llns because

## 13535:00 - 13575:00

there is not enough data I'm pointing

## 13575:00 - 13620:00

out that even with these llns if I'm

## 13620:00 - 13660:00

actually uh millions of developers who

## 13660:00 - 13700:00

are trying to build amazing applications

## 13700:00 - 13740:00

what is important is taking these llms

## 13740:00 - 13805:00

and being able to customize it and uh uh

## 13805:00 - 13840:00

that is the point uh and still there is

## 13840:00 - 13880:00

so much Innovation and value left to be

## 13880:00 - 13930:00

done there so that is the uh point I'm

## 13930:00 - 13975:00

making and because those set of data is

## 13975:00 - 14030:00

not accessible to any of the model

## 14030:00 - 14065:00

providers and so forth and there is

## 14065:00 - 14125:00

still lot of actually Innovation that is

## 14125:00 - 14175:00

net new possible because uh those are

## 14175:00 - 14210:00

actually insecure environments that are

## 14210:00 - 14240:00

not accessible because most of these

## 14240:00 - 14280:00

models are trained on public data are

## 14280:00 - 14315:00

publicly available or that can be

## 14315:00 - 14335:00

procured but you're not going to you're

## 14335:00 - 14360:00

not going to get like a step change if

## 14360:00 - 14395:00

you start changing with trading with

## 14395:00 - 14420:00

rocket mortgage data you might just get

## 14420:00 - 14465:00

a better application for Rocket morgage

## 14465:00 - 14490:00

you're not going to advance the field of

## 14490:00 - 14555:00

AI by getting mortgage data in there I

## 14555:00 - 14575:00

uh I AG I'm not saying it's not

## 14575:00 - 14635:00

important yeah you go ahead yeah but

## 14635:00 - 14675:00

each of these Enterprises each of these

## 14675:00 - 14710:00

startups are actually start uh going to

## 14710:00 - 14750:00

see a step change for their application

## 14750:00 - 14795:00

that I agree with yes so that is the and

## 14795:00 - 14825:00

all I'm pointing out is that is going to

## 14825:00 - 14870:00

be an equally important element that

## 14870:00 - 14905:00

should not be overlooked if you imagine

## 14905:00 - 14960:00

every Enterprise suddenly got uh 10x

## 14960:00 - 14985:00

better when it comes to handling L

## 14985:00 - 15020:00

customer claims are actually our

## 15020:00 - 15065:00

developer is 5X more productive or so

## 15065:00 - 15120:00

forth that is equally important and uh I

## 15120:00 - 15160:00

also think as uh AI field actually

## 15160:00 - 15195:00

continues to get more and more better

## 15195:00 - 15235:00

and better when it comes to actually

## 15235:00 - 15280:00

training these models or even changing

## 15280:00 - 15330:00

the architectures to actually be more

## 15330:00 - 15375:00

efficient uh in terms of how they are

## 15375:00 - 15420:00

actually learning from these data and so

## 15420:00 - 15465:00

forth how we are reinforcing you're also

## 15465:00 - 15500:00

constantly going to re ourselves so just

## 15500:00 - 15555:00

look back six years ago uh even before

## 15555:00 - 15585:00

Transformers came about we thought

## 15585:00 - 15645:00

actually deing uh was actually order of

## 15645:00 - 15705:00

magnitude better than uh uh how uh

## 15705:00 - 15740:00

traditionally machine learning was done

## 15740:00 - 15775:00

and then we found a new kind of scaling

## 15775:00 - 15830:00

architecture with uh Transformers uh and

## 15830:00 - 15865:00

I have no doubt that uh we are going to

## 15865:00 - 15900:00

actually start seeing some such things

## 15900:00 - 15955:00

soon as well now going back to the way

## 15955:00 - 15980:00

that these models evolve can you talk a

## 15980:00 - 16050:00

little bit about how we have actual like

## 16050:00 - 16110:00

the smaller models perform better than

## 16110:00 - 16145:00

the last generation of bigger models is

## 16145:00 - 16180:00

it does is it just like the training is

## 16180:00 - 16210:00

different you talked a little bit about

## 16210:00 - 16255:00

cleaning the data that goes in there um

## 16255:00 - 16280:00

I'm curious what would be involved in

## 16280:00 - 16300:00

that but how are these smaller models

## 16300:00 - 16340:00

performing better than the bigger

## 16340:00 - 16390:00

models um there are a few I mean that

## 16390:00 - 16430:00

notion of what is small and uh what is

## 16430:00 - 16515:00

large uh we always tend to uh I mean

## 16515:00 - 16555:00

because it's relative because our

## 16555:00 - 16585:00

definition of small and large keeps

## 16585:00 - 16615:00

changing but equally important is there

## 16615:00 - 16660:00

are multiple ingredients on what makes a

## 16660:00 - 16710:00

great model one is actually around uh

## 16710:00 - 16760:00

how much compute uh it is uh we have

## 16760:00 - 16805:00

thrown but also how much data that we

## 16805:00 - 16845:00

have uh actually used to train these

## 16845:00 - 16895:00

models and how do they get reinforced uh

## 16895:00 - 16930:00

so that the model knows actually it is

## 16930:00 - 16985:00

to delivering the right uh actually

## 16985:00 - 17020:00

responses to certain questions or so

## 17020:00 - 17075:00

forth uh all these ingredients right and

## 17075:00 - 17110:00

then how do you iterate based on some of

## 17110:00 - 17160:00

these feedback uh uh as well these are

## 17160:00 - 17205:00

some of the ingredients that make into

## 17205:00 - 17250:00

uh how a model provider trains uh these

## 17250:00 - 17310:00

models and uh if you see even if uh

## 17310:00 - 17365:00

someone is actually training an uh much

## 17365:00 - 17395:00

uh smaller model when it comes to

## 17395:00 - 17425:00

parameters but instead they actually

## 17425:00 - 17465:00

have trained on huge number of tokens or

## 17465:00 - 17505:00

so forth with better recipes on

## 17505:00 - 17550:00

reinforcing there is a case to be made

## 17550:00 - 17590:00

uh that uh they are able to actually get

## 17590:00 - 17645:00

higher quality results uh the second

## 17645:00 - 17680:00

when if you see interesting research

## 17680:00 - 17735:00

coming out of Stanford or others is also

## 17735:00 - 17775:00

when it comes to novel architectures uh

## 17775:00 - 17820:00

that they are talking about uh that they

## 17820:00 - 17885:00

expect to see also equally compelling

## 17885:00 - 17935:00

um models uh that are actually going to

## 17935:00 - 17995:00

lean uh learn faster while actually with

## 17995:00 - 18035:00

the same amount of data as well with

## 18035:00 - 18090:00

potentially even 10x cheaper inference

## 18090:00 - 18155:00

time and uh so uh that's why I'm

## 18155:00 - 18180:00

actually very optimistic about the

## 18180:00 - 18230:00

future when it comes to novel model

## 18230:00 - 18270:00

architectures which uh has the potential

## 18270:00 - 18315:00

to disrupt the space in a bay and that's

## 18315:00 - 18360:00

why I keep saying no one model in will

## 18360:00 - 18400:00

rule the world in the future let's talk

## 18400:00 - 18450:00

a little bit about your decisions about

## 18450:00 - 18505:00

partnering versus building in house

## 18505:00 - 18565:00

versus throwing other models out there

## 18565:00 - 18625:00

um do you I mean do you you have a large

## 18625:00 - 18655:00

team building your own large language

## 18655:00 - 18705:00

models in House at AWS and you also have

## 18705:00 - 18745:00

a very big investment in anthropic can

## 18745:00 - 18780:00

you talk through a little bit about what

## 18780:00 - 18815:00

the logic is between kind of going at it

## 18815:00 - 18905:00

in both ways yeah I mean uh so uh if you

## 18905:00 - 18965:00

see um the history of AWS we always

## 18965:00 - 19020:00

believed uh in customer Choice uh even

## 19020:00 - 19060:00

when we actually started with uh and

## 19060:00 - 19095:00

when I started the database team at that

## 19095:00 - 19120:00

time at that time the world used to

## 19120:00 - 19165:00

think databases actually like uh it has

## 19165:00 - 19210:00

to speak SQL and we kind of pioneered

## 19210:00 - 19260:00

the art of uh hey actually customers in

## 19260:00 - 19290:00

fact want different models I mean

## 19290:00 - 19320:00

different databases for different use

## 19320:00 - 19380:00

cases and uh we ended up actually uh

## 19380:00 - 19440:00

ping it and the rest of the industry um

## 19440:00 - 19475:00

and AWS now has the diverse set of

## 19475:00 - 19510:00

portfolio on the database front and rest

## 19510:00 - 19565:00

of uh industry completely pivoted that

## 19565:00 - 19620:00

way and when internally now going to the

## 19620:00 - 19680:00

Gen world and uh so forth internally as

## 19680:00 - 19715:00

we were building bunch of these gen

## 19715:00 - 19760:00

applications and we saw what it takes to

## 19760:00 - 19810:00

put together actually a model uh I mean

## 19810:00 - 19860:00

an N Eng application well there is a

## 19860:00 - 19900:00

notion of one powerful model that you

## 19900:00 - 19950:00

need at hard of doing some of the things

## 19950:00 - 19980:00

there are a bunch of different machine

## 19980:00 - 20025:00

learning models uh that you need uh such

## 20025:00 - 20070:00

as um you need a model to ingest your

## 20070:00 - 20110:00

data to do like vectorize your data and

## 20110:00 - 20140:00

do retrieval augmented generation you

## 20140:00 - 20200:00

need a separate ranker model you need

## 20200:00 - 20230:00

actually a separate model for guardrails

## 20230:00 - 20285:00

you need an uh API orchestration to do

## 20285:00 - 20320:00

software agent and Automation and so

## 20320:00 - 20370:00

forth and each of these models vary

## 20370:00 - 20410:00

across capabilities price and

## 20410:00 - 20460:00

performance and uh what we actually

## 20460:00 - 20525:00

wanted was uh um this letter believ that

## 20525:00 - 20565:00

no single model will be ideal for every

## 20565:00 - 20615:00

use case uh in a way and especially

## 20615:00 - 20650:00

because in this space we are super early

## 20650:00 - 20680:00

customers are still learning and

## 20680:00 - 20725:00

experimenting with different models uh

## 20725:00 - 20790:00

and that's why at Bedrock uh we actually

## 20790:00 - 20825:00

started the premise that uh we are going

## 20825:00 - 20865:00

to actually offer not just our first

## 20865:00 - 20895:00

party but also third party large

## 20895:00 - 20940:00

language models and other foundational

## 20940:00 - 20985:00

models as well like anthropic and uh

## 20985:00 - 21045:00

meta mestral coher and stability and 21

## 21045:00 - 21115:00

and others and if you see uh we uh 3

## 21115:00 - 21190:00

months um after G when uh after we

## 21190:00 - 21220:00

launched bedrock and made it generally

## 21220:00 - 21270:00

available we saw many of our customers

## 21270:00 - 21335:00

um actually using more than one model um

## 21335:00 - 21390:00

because they were still learning and uh

## 21390:00 - 21420:00

I'll just give an example of Thompson

## 21420:00 - 21475:00

Reuters uh Labs recently said that

## 21475:00 - 21520:00

having the ability to use diverse range

## 21520:00 - 21565:00

of model was like a key driver for them

## 21565:00 - 21615:00

to innovate quickly because the space is

## 21615:00 - 21675:00

evolving so much and uh as well that's

## 21675:00 - 21730:00

why I actually think uh this is uh what

## 21730:00 - 21765:00

is important is not just the individual

## 21765:00 - 21820:00

model but also the ability to customize

## 21820:00 - 21870:00

for various use cases and that's where

## 21870:00 - 21900:00

we are starting to see these patterns

## 21900:00 - 21950:00

emerging strongly as well you happy with

## 21950:00 - 22000:00

the anthropic partnership

## 22000:00 - 22045:00

uh anthropic has been a great Partners

## 22045:00 - 22125:00

uh with us and uh they are uh um the

## 22125:00 - 22160:00

producers of one of the most popular

## 22160:00 - 22225:00

models in uh right now and uh especially

## 22225:00 - 22275:00

if you see anthropic uh what they have

## 22275:00 - 22325:00

done with Cloud 3 I mean they are

## 22325:00 - 22390:00

amazing Innovation when it to uh um I

## 22390:00 - 22440:00

mean uh their reasoning capability and

## 22440:00 - 22465:00

they have really been a thought leader

## 22465:00 - 22520:00

and also Innovation and uh responsible

## 22520:00 - 22575:00

Ai and um so we are very excited about

## 22575:00 - 22620:00

their uh partnership and uh some of

## 22620:00 - 22675:00

models on Bedrock has been incredibly

## 22675:00 - 22715:00

powerful and uh popular with our

## 22715:00 - 22765:00

customers as well and on the the end

## 22765:00 - 22825:00

anthropic will also use AWS trinium uh

## 22825:00 - 22875:00

and inferentia chips to build train and

## 22875:00 - 22935:00

deploy their future models and uh as

## 22935:00 - 22980:00

well and um we have been super excited

## 22980:00 - 23050:00

to see also uh where uh in terms of the

## 23050:00 - 23085:00

art of possible and we are already

## 23085:00 - 23155:00

starting to see huge uh adoption and uh

## 23155:00 - 23220:00

customers um as well through our joint

## 23220:00 - 23280:00

Innovation fascinating um I have a

## 23280:00 - 23300:00

couple questions for you based off what

## 23300:00 - 23320:00

you just said first of all you talk

## 23320:00 - 23350:00

about trinium chips but you said can

## 23350:00 - 23395:00

train a model four times faster than the

## 23395:00 - 23465:00

industry standard yeah so have you heard

## 23465:00 - 23495:00

of curious to hear your perspective on

## 23495:00 - 23520:00

how things are going there I mean

## 23520:00 - 23540:00

obviously like the reason why people

## 23540:00 - 23585:00

like to go with Nvidia is because the

## 23585:00 - 23620:00

software is something that they like to

## 23620:00 - 23655:00

use so I'm curious to hear your

## 23655:00 - 23685:00

perspective on how tranium techs up

## 23685:00 - 23710:00

there and then there's also this other

## 23710:00 - 23730:00

new chip that's called I think it's

## 23730:00 - 23770:00

called Gro not like the Elon Musk Rock

## 23770:00 - 23795:00

but

## 23795:00 - 23835:00

grq that apparently is training these

## 23835:00 - 23890:00

models like unbelievably fast so would

## 23890:00 - 23915:00

be eager to hear your perspective on the

## 23915:00 - 23930:00

grock as

## 23930:00 - 23985:00

well um first on

## 23985:00 - 24060:00

uh uh trainum uh trainum two chips uh

## 24060:00 - 24095:00

are are designed with the sole purpose

## 24095:00 - 24130:00

of being able to train these large

## 24130:00 - 24175:00

language models and highly optimized uh

## 24175:00 - 24245:00

for training use case and uh and I

## 24245:00 - 24285:00

mentioned trainum 2 chips they are

## 24285:00 - 24320:00

actually can deliver up to 4X faster

## 24320:00 - 24350:00

training than the first generation

## 24350:00 - 24410:00

trainum chips uh while improving Energy

## 24410:00 - 24465:00

Efficiency as well and uh we also have

## 24465:00 - 24480:00

an

## 24480:00 - 24530:00

separate instance family optimized for

## 24530:00 - 24580:00

running these models inference as well

## 24580:00 - 24630:00

called inferentia so the ec2 instances

## 24630:00 - 24670:00

that are powered by our

## 24670:00 - 24720:00

inferentia um chips that deliver up to

## 24720:00 - 24780:00

50% better price performance uh per watt

## 24780:00 - 24825:00

over comparable ec2 as well and can

## 24825:00 - 24900:00

reduce cost by up to 40% as well so and

## 24900:00 - 24950:00

um interally I mean when we are uh

## 24950:00 - 25005:00

training these uh models we seeing great

## 25005:00 - 25090:00

uh actually um performance and um well

## 25090:00 - 25125:00

we also I mean while I can share some of

## 25125:00 - 25170:00

our early customer feedback on some of

## 25170:00 - 25215:00

these because tranium 2 is not generally

## 25215:00 - 25260:00

available yet uh but it has been super

## 25260:00 - 25300:00

compelling and super promising uh as

## 25300:00 - 25355:00

well because uh the scale at which uh it

## 25355:00 - 25410:00

can train us been uh very very

## 25410:00 - 25475:00

fascinating um as well

## 25475:00 - 25530:00

thoughts on grock or you can't com gr uh

## 25530:00 - 25570:00

I have not actually looked at it deeper

## 25570:00 - 25650:00

for me to offer much uh on it uh as well

## 25650:00 - 25675:00

you talked a little bit about reasoning

## 25675:00 - 25720:00

through our conversation and you know

## 25720:00 - 25750:00

there was this whole Kur fuffle around

## 25750:00 - 25785:00

open AI where they developed this qstar

## 25785:00 - 25820:00

model that apparently had reasoning in

## 25820:00 - 25855:00

it and we still never got the full story

## 25855:00 - 25910:00

there um so what what is going on

## 25910:00 - 25975:00

because from my understanding with

## 25975:00 - 26020:00

reasoning uh it's a different skill

## 26020:00 - 26055:00

different type of teaching than just

## 26055:00 - 26085:00

spitting back information now because it

## 26085:00 - 26135:00

goes through the steps that it has to

## 26135:00 - 26165:00

you know take in order to come back to

## 26165:00 - 26200:00

you with an answer so I'd love to hear

## 26200:00 - 26225:00

your perspective on what The Cutting

## 26225:00 - 26260:00

Edge of reasoning looks like and it

## 26260:00 - 26290:00

seems like it's already in production in

## 26290:00 - 26330:00

some of the models that we're talking

## 26330:00 - 26395:00

about yeah yeah I mean uh take uh when

## 26395:00 - 26440:00

it comes to reasoning um let's talk

## 26440:00 - 26480:00

about where the state of the art with

## 26480:00 - 26515:00

respect to reasoning because reasoning

## 26515:00 - 26540:00

means different things to different

## 26540:00 - 26585:00

people so the ability to actually take

## 26585:00 - 26645:00

an problem which has logical steps uh

## 26645:00 - 26685:00

and then break it down into a sequence

## 26685:00 - 26735:00

of uh actions which is what these models

## 26735:00 - 26775:00

do as like here is the plan I propose

## 26775:00 - 26815:00

and then being able to break down into

## 26815:00 - 26855:00

let's say five or 10 steps and then get

## 26855:00 - 26890:00

feedback and quickly iterate and then

## 26890:00 - 26960:00

produce and work out but uh in a domain

## 26960:00 - 27000:00

like software development these models

## 27000:00 - 27060:00

are starting to get U pretty good uh i'

## 27060:00 - 27095:00

say there are benchmarks like in the

## 27095:00 - 27130:00

soft domain something called the swe

## 27130:00 - 27165:00

bench and you can already start to see

## 27165:00 - 27210:00

some of these models are uh getting

## 27210:00 - 27255:00

pretty good score when it comes to being

## 27255:00 - 27305:00

able to given software development tasks

## 27305:00 - 27340:00

like uh for instance today if you take

## 27340:00 - 27375:00

our J assistant

## 27375:00 - 27435:00

Q it can actually take an uh a task

## 27435:00 - 27470:00

which a developer will say hey I have to

## 27470:00 - 27510:00

work on it today or the next couple of

## 27510:00 - 27550:00

days and like okayy change this error

## 27550:00 - 27605:00

condition uh for this use case to with

## 27605:00 - 27650:00

this error condition and uh and that is

## 27650:00 - 27700:00

the description they put in their uh get

## 27700:00 - 27740:00

repository and then uh give it to Q

## 27740:00 - 27770:00

it'll actually consume it and then

## 27770:00 - 27800:00

generate a plan and then get feedback

## 27800:00 - 27850:00

from the developer and uh uh say the

## 27850:00 - 27900:00

developer is your condition which their

## 27900:00 - 27935:00

code needs to change is not right can

## 27935:00 - 27970:00

you actually do it this way and then it

## 27970:00 - 28030:00

will update the plan and actually submit

## 28030:00 - 28060:00

uh generate the difference in code

## 28060:00 - 28090:00

saying like here are the changes I'm

## 28090:00 - 28125:00

planning to make does it sound okay and

## 28125:00 - 28185:00

then it can actually get back uh and um

## 28185:00 - 28255:00

all these are possible today and uh so

## 28255:00 - 28295:00

uh I actually think uh this reasoning

## 28295:00 - 28340:00

capability is going to actually get uh

## 28340:00 - 28375:00

better and better being able to generate

## 28375:00 - 28415:00

a plan and then being able to

## 28415:00 - 28490:00

iterate with um and uh um uh fellow

## 28490:00 - 28545:00

expert a human and help them assist to

## 28545:00 - 28580:00

get input on the plan and being able to

## 28580:00 - 28625:00

do and uh I think it is a compelling

## 28625:00 - 28685:00

capability if you look at it uh I talked

## 28685:00 - 28740:00

about software upgrades being uh with uh

## 28740:00 - 28795:00

done by Q the reason that is possible is

## 28795:00 - 28850:00

again it's uh not just reasoning uh

## 28850:00 - 28910:00

capability of uh these llms it is also

## 28910:00 - 28980:00

now we can couple reasoning capability

## 28980:00 - 29020:00

with actually compilers and actually

## 29020:00 - 29070:00

reinforce each other so when we actually

## 29070:00 - 29130:00

ask uh so we don't just ask 11 say here

## 29130:00 - 29180:00

is uh jdk 8 and convert to

## 29180:00 - 29235:00

jdk7 instead actually say here is the

## 29235:00 - 29265:00

thing I'm trying to accomplish and then

## 29265:00 - 29325:00

we actually also leverage compilers and

## 29325:00 - 29370:00

other Technologies to actually play off

## 29370:00 - 29415:00

of each other and iterate back and forth

## 29415:00 - 29480:00

and that is why this uh Q capab to do

## 29480:00 - 29505:00

things like code transformation is

## 29505:00 - 29525:00

extremely

## 29525:00 - 29570:00

remarkable uh in a way that it helps

## 29570:00 - 29635:00

Amazon in a big way so that's why the uh

## 29635:00 - 29685:00

uh reasoning capability is not if we

## 29685:00 - 29715:00

view it as purely like everything is

## 29715:00 - 29760:00

going to be llm driven vs industry are

## 29760:00 - 29825:00

going to be very very um not satisfied

## 29825:00 - 29860:00

that's why it has to be actually more R

## 29860:00 - 29905:00

trative and where we work with lln as

## 29905:00 - 29940:00

one of the ingredient it is not the

## 29940:00 - 30020:00

answer for everything thing right okay

## 30020:00 - 30050:00

in terms of where this Computing is

## 30050:00 - 30075:00

happening so obviously a lot of is

## 30075:00 - 30115:00

happening in the cloud right now but

## 30115:00 - 30155:00

Apple has WWDC coming up in just a few

## 30155:00 - 30180:00

weeks and I bet they're going to make

## 30180:00 - 30230:00

this big play of doing uh building LMS

## 30230:00 - 30290:00

and running LMS on device uh there was a

## 30290:00 - 30325:00

story in Mac rumors today it said uh

## 30325:00 - 30360:00

Apple releases open source AI models

## 30360:00 - 30405:00

that run on device I think they released

## 30405:00 - 30450:00

eight of them that run this is what Mac

## 30450:00 - 30485:00

Rumors say they run on device rather

## 30485:00 - 30520:00

than through Cloud servers it's called

## 30520:00 - 30595:00

open Elm efficient language models uh

## 30595:00 - 30630:00

what do you think about this push to run

## 30630:00 - 30665:00

on device and if people do start running

## 30665:00 - 30715:00

them on device does it sort of how does

## 30715:00 - 30750:00

it impact the cloud

## 30750:00 - 30830:00

business uh first of all uh I do expect

## 30830:00 - 30875:00

uh the model inference to be happening

## 30875:00 - 30920:00

on U multiple areas this is no different

## 30920:00 - 30945:00

from what happened in the Deep learning

## 30945:00 - 30975:00

world and let's just

## 30975:00 - 31035:00

look at even uh where Alexa for instance

## 31035:00 - 31080:00

uh it runs in deep learning model on the

## 31080:00 - 31125:00

device uh right and actually it does

## 31125:00 - 31160:00

certain decisions and then it does what

## 31160:00 - 31200:00

is like a hierarchical inference uh

## 31200:00 - 31250:00

where it knows to Route certain queries

## 31250:00 - 31310:00

to the cloud and certain queries can be

## 31310:00 - 31355:00

uh answered locally and in fact Alexa

## 31355:00 - 31405:00

actually is a very P powerful model

## 31405:00 - 31445:00

which is a tiny model for like uh the

## 31445:00 - 31520:00

Alexa Auto uh and so forth so I expect

## 31520:00 - 31560:00

lens to evolve in the same way where

## 31560:00 - 31595:00

there are a lot of uh decisions

## 31595:00 - 31625:00

especially if you have a

## 31625:00 - 31665:00

powerful Computing

## 31665:00 - 31720:00

device um which uh many smartphones and

## 31720:00 - 31775:00

others uh to be having that you can

## 31775:00 - 31845:00

actually run some of those uh simple llm

## 31845:00 - 31880:00

things at the edge and you will St but

## 31880:00 - 31915:00

there is still going to be a huge amount

## 31915:00 - 31970:00

of uh inference where you need more data

## 31970:00 - 32010:00

that is available elsewhere or more

## 32010:00 - 32060:00

capabilities and so forth so I expect

## 32060:00 - 32100:00

this hierarchical capability and

## 32100:00 - 32135:00

hierarchical inference to happen in the

## 32135:00 - 32165:00

same way how it played out in the Deep

## 32165:00 - 32215:00

learning era as well this is uh some of

## 32215:00 - 32260:00

the other reason why actually don't view

## 32260:00 - 32330:00

it as you put a big model behind an API

## 32330:00 - 32375:00

and then uh give data on uh as question

## 32375:00 - 32405:00

in the way these generative a

## 32405:00 - 32440:00

applications are going to be built is

## 32440:00 - 32480:00

actually like series of uh things

## 32480:00 - 32525:00

chained together some of it is uh model

## 32525:00 - 32555:00

inference some of it is actually

## 32555:00 - 32625:00

workflows and uh um and whatnot and

## 32625:00 - 32660:00

that's why that pattern is going to be

## 32660:00 - 32685:00

important and there are going to be

## 32685:00 - 32720:00

different models and different data

## 32720:00 - 32765:00

connectors and they all are going to be

## 32765:00 - 32805:00

working together to produce an very

## 32805:00 - 32845:00

seamless experience from a consumer

## 32845:00 - 32890:00

perspective so if hypothetically a big

## 32890:00 - 32930:00

mobile device manufacturer tells us that

## 32930:00 - 32970:00

on device large language models are the

## 32970:00 - 33020:00

future we should view that with a bit of

## 33020:00 - 33040:00

context is that what you're trying to

## 33040:00 - 33060:00

tell us

## 33060:00 - 33100:00

Swami uh it would be hard for me to

## 33100:00 - 33150:00

comment uh anything uh hypothetical but

## 33150:00 - 33190:00

uh what I can say is there are always

## 33190:00 - 33215:00

going to be actually inferences

## 33215:00 - 33270:00

happening in different uh layers of the

## 33270:00 - 33320:00

stack and it is uh going to happen for

## 33320:00 - 33350:00

different uh but there are going to be

## 33350:00 - 33395:00

use cases that are very very good and

## 33395:00 - 33440:00

just uh happening at the edge uh but

## 33440:00 - 33480:00

there are going to be huge amount of use

## 33480:00 - 33540:00

cases and uh as well uh happening on the

## 33540:00 - 33585:00

cloud uh and those both those use cases

## 33585:00 - 33635:00

are always going to exist okay great I

## 33635:00 - 33675:00

want to end uh with a little discussion

## 33675:00 - 33715:00

about open source llama 3 is running

## 33715:00 - 33785:00

through bedrock I believe or AWS day one

## 33785:00 - 33845:00

um what is uh your view on open source

## 33845:00 - 33880:00

compared to these other close sourced

## 33880:00 - 33935:00

models um dangerous good helpful just

## 33935:00 - 33970:00

one of the you know one of the pack

## 33970:00 - 33995:00

what's your

## 33995:00 - 34030:00

thoughts um so well we are big

## 34030:00 - 34090:00

supporters of uh actually uh enabling uh

## 34090:00 - 34155:00

access to these models and uh um I mean

## 34155:00 - 34210:00

companies like uh meta and U mol have

## 34210:00 - 34265:00

been innovating at an incredible clip in

## 34265:00 - 34300:00

some of these faes and uh with the

## 34300:00 - 34315:00

publicly

## 34315:00 - 34380:00

available uh weights and so forth um uh

## 34380:00 - 34415:00

the key thing and both of them are doing

## 34415:00 - 34455:00

incredibly well is also doing it in an

## 34455:00 - 34505:00

uh thoughtful responsible way to put the

## 34505:00 - 34565:00

appropriate amount of guard roils and um

## 34565:00 - 34635:00

Asal so uh that's why I actually think

## 34635:00 - 34695:00

uh this responsible Innovation uh even

## 34695:00 - 34780:00

in open source is a good Trend and uh um

## 34780:00 - 34830:00

and I expect that to continue especially

## 34830:00 - 34865:00

with uh thoughtful Innovation from some

## 34865:00 - 34895:00

of these providers and those are some of

## 34895:00 - 34935:00

the reasons why we partner with them to

## 34935:00 - 34975:00

even actually make make these models

## 34975:00 - 35030:00

accessible to all developers as well can

## 35030:00 - 35060:00

you actually build the guardrails into

## 35060:00 - 35095:00

the models and can't people override

## 35095:00 - 35150:00

them a little bit once they're

## 35150:00 - 35230:00

open um these uh these models have built

## 35230:00 - 35300:00

in guardrails and uh they also uh and in

## 35300:00 - 35340:00

areas like Bedrock we also layer

## 35340:00 - 35375:00

actually guardrails on top of these

## 35375:00 - 35415:00

models uh as well so that imagine if

## 35415:00 - 35450:00

you're an Enterprise wanting to build an

## 35450:00 - 35505:00

uh customer Service chat B for insurance

## 35505:00 - 35550:00

you want it to be only talking about uh

## 35550:00 - 35605:00

your data and uh specific insurance and

## 35605:00 - 35650:00

not answer questions related to weather

## 35650:00 - 35710:00

or uh something else uh right and uh so

## 35710:00 - 35770:00

you so Gods when we think of God Els uh

## 35770:00 - 35805:00

we always think of the extreme scenarios

## 35805:00 - 35845:00

but for many Enterprises it is about

## 35845:00 - 35885:00

like hey I am actually trying to keep

## 35885:00 - 35925:00

the topic constraint to this so that I

## 35925:00 - 35980:00

can do certain way and uh so that's uh

## 35980:00 - 36010:00

those and you want it to preserve

## 36010:00 - 36055:00

actually like uh private information or

## 36055:00 - 36085:00

sensitive information and various other

## 36085:00 - 36140:00

things so that's why uh on top of some

## 36140:00 - 36180:00

of the guard rails of the individual FMS

## 36180:00 - 36225:00

Bedrock guard rails also is another

## 36225:00 - 36275:00

layer that helps developers and

## 36275:00 - 36320:00

companies actually build those get those

## 36320:00 - 36360:00

capabilities out of the box as well and

## 36360:00 - 36435:00

uh yeah we see uh up to 40 84 uh%

## 36435:00 - 36465:00

Improvement in

## 36465:00 - 36510:00

uh forther accuracy U because of those

## 36510:00 - 36560:00

capability as well cool all right let's

## 36560:00 - 36605:00

end with some fun ones um are you

## 36605:00 - 36640:00

thinking about building a nuclear power

## 36640:00 - 36695:00

plant to power AI

## 36695:00 - 36755:00

training um uh I am not thinking about

## 36755:00 - 36810:00

it myself but I can't speak to my infra

## 36810:00 - 36890:00

team uh as well do you think $7 trillion

## 36890:00 - 36930:00

is the right amount a little bit more or

## 36930:00 - 36970:00

a little bit less than we might need for

## 36970:00 - 37010:00

chip companies that are focused on

## 37010:00 - 37050:00

building

## 37050:00 - 37075:00

AI

## 37075:00 - 37125:00

um I actually I've never done the math

## 37125:00 - 37210:00

myself to know if this uh uh but um but

## 37210:00 - 37245:00

I would say all depends on what time

## 37245:00 - 37295:00

scale you're talking about uh right

## 37295:00 - 37320:00

inflation these days it could be next

## 37320:00 - 37400:00

year that that's relatively

## 37400:00 - 37505:00

cheap yeah uh AGI before or after after

## 37505:00 - 37610:00

2030 I'd say uh intelligence uh is an uh

## 37610:00 - 37675:00

a never ending Pursuit um I think AGI is

## 37675:00 - 37720:00

a very heavily overloaded term and

## 37720:00 - 37775:00

widely misunderstood so that's why I

## 37775:00 - 37825:00

actually don't use that word uh I think

## 37825:00 - 37850:00

uh intelligence is going to be

## 37850:00 - 37895:00

constantly getting better but it is

## 37895:00 - 37940:00

going to be human assisted uh uh

## 37940:00 - 37975:00

intelligence assisting humans is going

## 37975:00 - 38025:00

to be the future that's my guess yeah

## 38025:00 - 38060:00

and fi finally um I didn't mean to

## 38060:00 - 38105:00

demean rocket mortgage earlier uh just

## 38105:00 - 38135:00

to be clear I think that this stuff is

## 38135:00 - 38160:00

really fascinating when it comes to

## 38160:00 - 38200:00

business and it seems like it'll be hand

## 38200:00 - 38240:00

inand they will provide the capital

## 38240:00 - 38275:00

necessary to advance the St

## 38275:00 - 38295:00

state-ofthe-art and then the state-

## 38295:00 - 38330:00

ofthe art will learn from them as it

## 38330:00 - 38355:00

moves the next models forward does that

## 38355:00 - 38400:00

sound kind of right to you

## 38400:00 - 38460:00

or uh I actually I mean generative AI

## 38460:00 - 38520:00

and it's uh such an infancy space with

## 38520:00 - 38585:00

uh so much uh happening in this uh

## 38585:00 - 38695:00

domain uh and uh there is lot uh of um I

## 38695:00 - 38745:00

mean bright Minds working on this space

## 38745:00 - 38790:00

and uh our goal is to actually enable

## 38790:00 - 38855:00

all the bright Minds uh to be able to

## 38855:00 - 38900:00

First be able to interact with it and

## 38900:00 - 38930:00

actually get the best out of these

## 38930:00 - 38965:00

technology that's why in aw yes we are

## 38965:00 - 38995:00

not just enabling model Builders to

## 38995:00 - 39025:00

build these models that's where we spend

## 39025:00 - 39055:00

a lot of time talking about like how do

## 39055:00 - 39095:00

you actually enable them so that they

## 39095:00 - 39145:00

don't hit a wall and so forth uh but

## 39145:00 - 39180:00

this technology won't reach its

## 39180:00 - 39230:00

potential and you won't have that uh

## 39230:00 - 39270:00

virtuous Loop or feedback cycle unless

## 39270:00 - 39330:00

there are enough people able to consume

## 39330:00 - 39370:00

and build remarkable applications uh

## 39370:00 - 39410:00

using these models uh otherwise we are

## 39410:00 - 39465:00

building it with no means uh to do

## 39465:00 - 39510:00

something useful with it and that is the

## 39510:00 - 39555:00

other Mission we are very excited about

## 39555:00 - 39590:00

and uh those are some of the reasons why

## 39590:00 - 39615:00

we actually have buil things like

## 39615:00 - 39645:00

Bedrock which is used by tens of

## 39645:00 - 39690:00

thousands of uh companies already or

## 39690:00 - 39740:00

with things like Amazon q and so forth

## 39740:00 - 39780:00

this virtuous cycle of actually uh

## 39780:00 - 39840:00

companies and organization uh getting

## 39840:00 - 39885:00

useful value out of it and being able to

## 39885:00 - 39935:00

leverage these models to do amazing

## 39935:00 - 39990:00

things it will sound triple simple as

## 39990:00 - 40040:00

like what rocket marage was uh able to

## 40040:00 - 40085:00

do in terms of automation or what bridge

## 40085:00 - 40135:00

water is able to do or what fiser is

## 40135:00 - 40180:00

doing from like scientific and medical

## 40180:00 - 40215:00

content generation to manufacturing

## 40215:00 - 40255:00

process Improvement to Dana farberg

## 40255:00 - 40315:00

Cancer Institute is uh using Claud on

## 40315:00 - 40345:00

Bedrock to develop a new research

## 40345:00 - 40400:00

solution the potentials are endless and

## 40400:00 - 40445:00

that's what is exciting to me in this

## 40445:00 - 40505:00

space um as well and uh I actually the

## 40505:00 - 40535:00

good news is we still just getting

## 40535:00 - 40610:00

started um and uh it's uh truly day one

## 40610:00 - 40665:00

year spot on I agree and I do think you

## 40665:00 - 40690:00

know as I spoke with Matt Wood about and

## 40690:00 - 40730:00

speaking with you it's just clear that

## 40730:00 - 40790:00

Amazon is just in every layer whether it

## 40790:00 - 40825:00

comes to foundational model running

## 40825:00 - 40870:00

other companies foundational models um

## 40870:00 - 40905:00

helping companies build their own

## 40905:00 - 40935:00

technology and Advance it in their own

## 40935:00 - 40990:00

ways uh smart way to do business thank

## 40990:00 - 41020:00

you for coming on and speaking with me

## 41020:00 - 41065:00

Swami and I hope we can do it again soon

## 41065:00 - 41105:00

really good to get a chance to chat hey

## 41105:00 - 41145:00

me too hey thanks again Alex so thanks

## 41145:00 - 41180:00

for having me you bet thank you

## 41180:00 - 41210:00

everybody for watching and we'll see you

## 41210:00+

next time on big technology

