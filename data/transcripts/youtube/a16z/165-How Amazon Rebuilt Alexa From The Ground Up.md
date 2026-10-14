---
source: https://www.youtube.com/watch?v=Jq-JmvFUXCM
title: How Amazon Rebuilt Alexa From The Ground Up
author: Alex Kantrowitz
date: 2025-03-05
views: 4446
description: >-
  Panos Panay is the senior vice president of Devices & Services at Amazon.
  Daniel Rausch is the Vice President of Alexa at Amazon. The two join Big
  Technology Podcast to discuss how the company rearchitected Alexa, blending a
  deterministic system with the latest generative AI technology to create
  something that can both turn your lights off and speak with you about
  philosophy. We also discuss how all big tech companies seem to be converging
  on the same contextually aware, general AI assistant, and why Amazon believes
  Alexa has a chance to win. Tune in for a front row perspective on one of the
  tech industry's biggest AI projects.


  Chapters:


  0:00 - Introduction to Amazon's revamped Alexa

  2:09 - The challenge of keeping existing users while rebuilding Alexa

  4:56 - Technical architecture: Re-engineering Alexa from the ground up

  8:39 - How Alexa handles deterministic vs. non-deterministic commands

  13:27 - The speed/latency challenge with natural language AI

  16:20 - Real-world examples: "Don't play music in the baby's room"

  19:34 - Technical challenges of the live demo

  24:43 - The vision and competitive landscape for voice assistants

  27:56 - Amazon's advantages in the home environment

  30:41 - Family calendars and multi-user functionality

  32:52 - Mobile strategy and cross-device continuity

  35:15 - Agentic AI capabilities in the new Alexa

  40:53 - Proactive vs. reactive assistant features

  44:30 - Trust, privacy, and data management

  47:34 - The importance of screens for Alexa devices

  51:39 - Voice AI as the future of artificial intelligence
tags:
  - Alexa Plus
  - Amazon AI
  - Voice Assistant
  - Panos Panay
  - Daniel Rauch
  - Alex Kantrowitz
  - Big Technology Podcast
  - LLMs
  - Conversational AI
  - Smart Home
  - Natural Language Processing
  - Amazon Echo
  - Future of AI
  - Voice AI
  - Agentic AI
  - Smart Assistant
  - Tech Interview
  - Amazon
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T21:03:57.050Z
---

# How Amazon Rebuilt Alexa From The Ground Up

## 00:00 - 35:00

the Amazon leaders who spearheaded the

## 35:00 - 85:00

new Alexa are here in studio to talk

## 85:00 - 125:00

about what it took to rebuild the

## 125:00 - 170:00

pioneering Ai and where voice AI is

## 170:00 - 200:00

heading in the age of large language

## 200:00 - 260:00

models we're joined today by Panos panai

## 260:00 - 310:00

Amazon senior vice president of devices

## 310:00 - 360:00

and services and Daniel Roush the VP of

## 360:00 - 410:00

Alexa and Fire TV gentlemen great to see

## 410:00 - 455:00

you welcome to the show thanks man so

## 455:00 - 490:00

great to be here sounded kind of fun so

## 490:00 - 525:00

you you both sounded kind of fun yeah

## 525:00 - 565:00

you both must be relieved to have this

## 565:00 - 655:00

out uh yeah I mean excited relieved is a

## 655:00 - 690:00

tricky word on this one you know we're

## 690:00 - 725:00

we're finishing the product now it's

## 725:00 - 765:00

coming out next month so we're pumped

## 765:00 - 800:00

that we're through the event and yeah

## 800:00 - 820:00

there's some relief I would say would

## 820:00 - 840:00

you agree you feel a little bit of

## 840:00 - 865:00

relief but the truth is like it's all

## 865:00 - 890:00

about getting it into a customer's hands

## 890:00 - 930:00

as fast as possible so you still the

## 930:00 - 965:00

team's feeling that urgency right now

## 965:00 - 990:00

yeah that's the big moment for the team

## 990:00 - 1010:00

right you get that first customer

## 1010:00 - 1040:00

response so we're we still feel like

## 1040:00 - 1070:00

we're building towards it but yesterday

## 1070:00 - 1105:00

was great okay so I have uh three Echo

## 1105:00 - 1145:00

devices in my house we have three rooms

## 1145:00 - 1175:00

yeah what are they house is generous uh

## 1175:00 - 1210:00

but in my apartment there's one in the

## 1210:00 - 1245:00

bedroom there's one in the kitchen

## 1245:00 - 1260:00

dining room and there's one in the

## 1260:00 - 1305:00

office yeah so they are first generation

## 1305:00 - 1330:00

I'm really looking forward to getting

## 1330:00 - 1375:00

these updates working hopefully within

## 1375:00 - 1420:00

these devices and uh and getting a

## 1420:00 - 1445:00

chance to use a new and improved Alexa

## 1445:00 - 1475:00

I've been hanging on to the echos for a

## 1475:00 - 1510:00

long time in the hope that something

## 1510:00 - 1550:00

like this would happen so we're here and

## 1550:00 - 1575:00

I I'm just I was at your your event

## 1575:00 - 1600:00

where you were announcing it I'll give

## 1600:00 - 1625:00

listeners a little bit understanding of

## 1625:00 - 1655:00

what I saw and then we're going to go

## 1655:00 - 1675:00

into some questions about what it was

## 1675:00 - 1710:00

like to build this so this new Alexa

## 1710:00 - 1745:00

it's called Alexa plus it is

## 1745:00 - 1780:00

conversational so it understands natural

## 1780:00 - 1825:00

language it understands your context and

## 1825:00 - 1855:00

you don't have to say Alexa every time

## 1855:00 - 1885:00

it we'll sort of have it back and forth

## 1885:00 - 1925:00

with you it is I think you could call it

## 1925:00 - 1955:00

a gentic it allows you to take action

## 1955:00 - 1990:00

like book a table call an Uber it will

## 1990:00 - 2015:00

go out on the world and help monitor

## 2015:00 - 2050:00

ticket prices for you for instance and

## 2050:00 - 2095:00

it's also deeply integrated into Amazon

## 2095:00 - 2120:00

services and namely Prime it's going to

## 2120:00 - 2155:00

be free for Prime members $1 19999 a

## 2155:00 - 2200:00

month if you're not a Prime members not

## 2200:00 - 2240:00

not a Prime member and the coolest thing

## 2240:00 - 2280:00

I saw in the demo was that uh you you I

## 2280:00 - 2340:00

think one of you asked for a uh the song

## 2340:00 - 2380:00

with what was it Bradley Cooper and Lady

## 2380:00 - 2415:00

Gaga and didn't say lady Goa I just said

## 2415:00 - 2460:00

Bradley Cooper Bradley Cooper uh in in

## 2460:00 - 2505:00

that what was the movie called uh stars

## 2505:00 - 2555:00

born stars born great great movie and

## 2555:00 - 2585:00

then it it called up P pull the play the

## 2585:00 - 2635:00

song and then you said now let me see it

## 2635:00 - 2655:00

the in the movie and it connects to

## 2655:00 - 2670:00

Prime video and you could see in the

## 2670:00 - 2740:00

movie so very cool product uh definitely

## 2740:00 - 2765:00

I think what a lot of us have been

## 2765:00 - 2805:00

hoping to see from the Alexa team and

## 2805:00 - 2855:00

from Amazon on Alexa um we're going to

## 2855:00 - 2875:00

talk a little bit about what it took to

## 2875:00 - 2915:00

build it and then the strategy here so I

## 2915:00 - 2935:00

think the first question I need to ask

## 2935:00 - 2975:00

you both is uh what what did take so

## 2975:00 - 3010:00

long because I think that like for all

## 3010:00 - 3040:00

of us whove you know I think there's 500

## 3040:00 - 3085:00

or 600 million uh Alexa enabled devices

## 3085:00 - 3140:00

out there we've been wondering as open

## 3140:00 - 3175:00

AI of the world and other companies have

## 3175:00 - 3225:00

made these big advances on voice AI when

## 3225:00 - 3255:00

Amazon was going to make its move and

## 3255:00 - 3290:00

and you have made the move um but what

## 3290:00 - 3335:00

what was the uh process that made it

## 3335:00 - 3375:00

take as long as it has ponos I think the

## 3375:00 - 3420:00

easiest way to say it is uh you've

## 3420:00 - 3445:00

started the summary when you have

## 3445:00 - 3465:00

hundreds of millions of customers that

## 3465:00 - 3515:00

are active right now you I mean this is

## 3515:00 - 3535:00

we talked a little bit about it

## 3535:00 - 3580:00

yesterday but every one of them matter

## 3580:00 - 3610:00

how do we make sure they all get the

## 3610:00 - 3655:00

great experience they need um meaning

## 3655:00 - 3690:00

you can't start from

## 3690:00 - 3745:00

zero and ignore it and if you could it

## 3745:00 - 3785:00

could be much faster although it's not

## 3785:00 - 3805:00

that easy to hook up the thousands of

## 3805:00 - 3835:00

apis and all the partners that we're

## 3835:00 - 3865:00

bringing together and all the experts

## 3865:00 - 3905:00

it's not it takes time but the first

## 3905:00 - 3940:00

thing is and there's two parts to it but

## 3940:00 - 3960:00

the first thing is you got hundreds of

## 3960:00 - 3990:00

millions of customers they love certain

## 3990:00 - 4020:00

things that they do on Alexa today they

## 4020:00 - 4045:00

might not love everything but they love

## 4045:00 - 4100:00

certain things for sure you can't you

## 4100:00 - 4130:00

can't leave that behind can't wake up

## 4130:00 - 4180:00

one day and whatever you use Alexa for

## 4180:00 - 4225:00

whether it's timers or music you can't

## 4225:00 - 4265:00

not make it better and great and so you

## 4265:00 - 4300:00

don't feel like something was taken away

## 4300:00 - 4325:00

from you when you when you take

## 4325:00 - 4375:00

something away from a customer um you've

## 4375:00 - 4410:00

just missed you've missed and so that's

## 4410:00 - 4450:00

one it takes time to make sure you can

## 4450:00 - 4490:00

get it all done so everything on what

## 4490:00 - 4525:00

you would call Alexa not Alexa plus

## 4525:00 - 4580:00

works on Alexa plus but better and that

## 4580:00 - 4610:00

was just the first point part of the

## 4610:00 - 4645:00

vision can't leave anyone behind which

## 4645:00 - 4675:00

was important we can talk about devices

## 4675:00 - 4700:00

and so forth but customers who love

## 4700:00 - 4755:00

their products um that are in and they

## 4755:00 - 4780:00

need them we can't take that away that

## 4780:00 - 4830:00

was one second piece is you're rearching

## 4830:00 - 4880:00

from the ground up so you've got first

## 4880:00 - 4905:00

the weight of keeping hundreds of

## 4905:00 - 4930:00

millions of customers and then you're

## 4930:00 - 4970:00

rearching from the ground up if we

## 4970:00 - 5000:00

started from zero customers I think this

## 5000:00 - 5035:00

is a different story you can move a lot

## 5035:00 - 5065:00

faster we can solve problems and then

## 5065:00 - 5100:00

just add features as we go if that makes

## 5100:00 - 5135:00

sense so maybe we just had a

## 5135:00 - 5165:00

conversationalist a pretty cool one then

## 5165:00 - 5195:00

we can add personalization then we can

## 5195:00 - 5245:00

add memory then we can add the experts

## 5245:00 - 5275:00

and people would just get updates along

## 5275:00 - 5305:00

the way and maybe learn and be great

## 5305:00 - 5340:00

however on day one we need to support

## 5340:00 - 5365:00

everything people love and know about

## 5365:00 - 5410:00

Alexa day one and so a little bit of

## 5410:00 - 5450:00

patience there um it takes a little bit

## 5450:00 - 5495:00

longer and the vision was it the vision

## 5495:00 - 5530:00

Vision was clear like we're going to go

## 5530:00 - 5575:00

bring a conversational agent forward an

## 5575:00 - 5645:00

assistant for everyone that is smart has

## 5645:00 - 5690:00

memory can personalize to you and then

## 5690:00 - 5735:00

ultimately be incredibly useful and so

## 5735:00 - 5780:00

we when we had that laid out we're okay

## 5780:00 - 5815:00

great but we can't leave any customers

## 5815:00 - 5855:00

behind and right at that point you kind

## 5855:00 - 5895:00

of step back once you put the vision

## 5895:00 - 5920:00

together you realize you need a full re

## 5920:00 - 5940:00

architecture but you're not going to

## 5940:00 - 5970:00

leave your customers out so you're re

## 5970:00 - 6005:00

architecting pretty much two stacks at

## 6005:00 - 6040:00

that point one what is classically known

## 6040:00 - 6090:00

as Alexa to be awesome and come into

## 6090:00 - 6125:00

this conversational world and the other

## 6125:00 - 6155:00

is everything new that it has to do yeah

## 6155:00 - 6175:00

and I want to go a level deeper with

## 6175:00 - 6220:00

Daniel on this one because P what you're

## 6220:00 - 6255:00

talking about a re architecture is sort

## 6255:00 - 6290:00

of what I've heard has been the holdup

## 6290:00 - 6315:00

here with Alexa for all these years

## 6315:00 - 6345:00

which is that and Daniel tell me if I'm

## 6345:00 - 6395:00

wrong but basically what folks have told

## 6395:00 - 6435:00

me is that the old version or the

## 6435:00 - 6480:00

original version of Alexa was built with

## 6480:00 - 6530:00

a lot of like then commands right so you

## 6530:00 - 6570:00

know it will understand some structured

## 6570:00 - 6600:00

commands turn on the lights okay then it

## 6600:00 - 6630:00

will take that and almost like

## 6630:00 - 6665:00

deterministically say okay I understand

## 6665:00 - 6690:00

this command this is what I'm going to

## 6690:00 - 6720:00

do turn the switch with large language

## 6720:00 - 6760:00

models it's a completely different ball

## 6760:00 - 6805:00

game because you have to make room for

## 6805:00 - 6840:00

uncertainty so actually the fact that

## 6840:00 - 6880:00

you've been able to introduce an Alexa

## 6880:00 - 6905:00

with large language models which I think

## 6905:00 - 6935:00

will have will be able to keep that

## 6935:00 - 6985:00

functionality is an engineering feat um

## 6985:00 - 7010:00

that's my perspective from the outside

## 7010:00 - 7030:00

what what is it actually like on the

## 7030:00 - 7065:00

inside and how close is that assessment

## 7065:00 - 7090:00

to the challenge well the team will love

## 7090:00 - 7130:00

to hear you say engineering feat uh cuz

## 7130:00 - 7160:00

I do think that I think there no lack of

## 7160:00 - 7205:00

feet it is it is real that is the size

## 7205:00 - 7245:00

of the task for sure I think um I think

## 7245:00 - 7275:00

you're you're on to it for sure uh you

## 7275:00 - 7315:00

know large language models the one thing

## 7315:00 - 7335:00

I'd add just in terms of thinking

## 7335:00 - 7360:00

through the technical architecture to

## 7360:00 - 7410:00

what Pano said is that it's really just

## 7410:00 - 7445:00

the the latest generations of large

## 7445:00 - 7490:00

language models that can even do the

## 7490:00 - 7530:00

things that Alexa needs to be able to do

## 7530:00 - 7555:00

uh so you're talking about our Nova

## 7555:00 - 7590:00

models right which we uh announced

## 7590:00 - 7620:00

within the last few months and starting

## 7620:00 - 7650:00

to get into customers hands that's super

## 7650:00 - 7685:00

exciting uh you know partnership that we

## 7685:00 - 7710:00

have with anthropy like you you really

## 7710:00 - 7755:00

need very state-of-the-art technology at

## 7755:00 - 7780:00

the base of the architecture and those

## 7780:00 - 7835:00

large language models and in large part

## 7835:00 - 7865:00

because of what you said we need them to

## 7865:00 - 7905:00

behave in ways that we can predict and

## 7905:00 - 7975:00

are certain someone says lock my door or

## 7975:00 - 8020:00

you know play that song you want it to

## 8020:00 - 8045:00

happen right some are higher consequence

## 8045:00 - 8065:00

than others and you really need to get

## 8065:00 - 8095:00

it right but you also want all the

## 8095:00 - 8130:00

elegance and nuance and understanding

## 8130:00 - 8180:00

and non-deterministic behaviors of large

## 8180:00 - 8210:00

language models themselves right so we

## 8210:00 - 8245:00

would call that a stochastic system that

## 8245:00 - 8280:00

you know it's literally at runtime that

## 8280:00 - 8310:00

you're making those determinations so if

## 8310:00 - 8340:00

you want to integrate tens of thousands

## 8340:00 - 8395:00

of services on day one day one out of

## 8395:00 - 8435:00

the box take advantage of everything

## 8435:00 - 8460:00

that Alexa has always been able to do as

## 8460:00 - 8505:00

Panos was saying and introduce all of

## 8505:00 - 8545:00

this new unbelievable behavior that you

## 8545:00 - 8575:00

can get out of large language models

## 8575:00 - 8610:00

that is a big engineering feat so how

## 8610:00 - 8650:00

does it know when the user is saying

## 8650:00 - 8690:00

Turn The Lights On versus like something

## 8690:00 - 8730:00

more esoteric like is there something

## 8730:00 - 8760:00

built within the technology that's kind

## 8760:00 - 8795:00

of like a switcher that determines first

## 8795:00 - 8840:00

your intent and then decides which part

## 8840:00 - 8875:00

of the model to send it out to the way

## 8875:00 - 8905:00

to think about it is you know at at the

## 8905:00 - 8930:00

base level you have large language

## 8930:00 - 8960:00

models and you have this model agnostic

## 8960:00 - 8995:00

system that's even itself going to

## 8995:00 - 9030:00

choose the right model for the job and

## 9030:00 - 9065:00

the models play different roles in there

## 9065:00 - 9110:00

what what's already happened is um even

## 9110:00 - 9135:00

even honestly sort of in the way you

## 9135:00 - 9165:00

asked a few of the questions is that

## 9165:00 - 9195:00

people assume the large language model

## 9195:00 - 9260:00

is the product a product like Alexa is

## 9260:00 - 9310:00

so much more than quote unquote just a

## 9310:00 - 9350:00

large language model so you have models

## 9350:00 - 9380:00

playing many different roles in the in

## 9380:00 - 9430:00

the system overall even models helping

## 9430:00 - 9460:00

us decide which model and models

## 9460:00 - 9495:00

themselves deciding if they're the best

## 9495:00 - 9530:00

you know tool for the job so to speak so

## 9530:00 - 9560:00

then you have a system that

## 9560:00 - 9585:00

progressively decides how to get

## 9585:00 - 9610:00

something done I wouldn't think about it

## 9610:00 - 9655:00

like a switch or something in classic

## 9655:00 - 9690:00

computer science that is a you know it's

## 9690:00 - 9720:00

a gate that's not that's not how the

## 9720:00 - 9765:00

system works it's it's a collection of

## 9765:00 - 9810:00

model behaviors and systems Downstream

## 9810:00 - 9840:00

of that that complete specific tasks and

## 9840:00 - 9860:00

that and that's where we introduce this

## 9860:00 - 9915:00

term expert to try to help coales around

## 9915:00 - 9940:00

the system behavior and explain it

## 9940:00 - 9970:00

better the large language models are

## 9970:00 - 10005:00

interacting with these experts that do

## 10005:00 - 10045:00

things like get you the sports score

## 10045:00 - 10095:00

play a song play a video know where you

## 10095:00 - 10120:00

are in the song so that you can go to

## 10120:00 - 10145:00

the video like all the things that you

## 10145:00 - 10185:00

saw yesterday at the event and so Panos

## 10185:00 - 10225:00

this is a mixture of experts model it is

## 10225:00 - 10265:00

you think about it and a mixture of

## 10265:00 - 10295:00

experts model but each expert

## 10295:00 - 10325:00

theoretically has its own model as well

## 10325:00 - 10370:00

so you're building on top of it each

## 10370:00 - 10415:00

expert is smarter when you think experts

## 10415:00 - 10440:00

it's like it's a weird term yeah but

## 10440:00 - 10490:00

there's think photos Smart Home

## 10490:00 - 10525:00

entertainment whether that's music or

## 10525:00 - 10570:00

video local info info all the partners

## 10570:00 - 10590:00

that connect you have communication

## 10590:00 - 10620:00

expert you have an artifact expert you

## 10620:00 - 10640:00

have a memory expert you have a

## 10640:00 - 10680:00

personalization expert each of them play

## 10680:00 - 10715:00

a role and they kind of arbitrate with

## 10715:00 - 10750:00

each other at all times so like the

## 10750:00 - 10770:00

model is just lighting up when it

## 10770:00 - 10795:00

determines that that's what you want to

## 10795:00 - 10845:00

do that's right uh just Daniel kind of

## 10845:00 - 10870:00

said it well like because the llm at the

## 10870:00 - 10915:00

bottom of that stack is it's deter it's

## 10915:00 - 10945:00

deterministic it's choosing which model

## 10945:00 - 10975:00

to use then the experts come into play

## 10975:00 - 11015:00

on top of it it's pretty it's a pretty

## 11015:00 - 11050:00

phenomenal way to you know it's a pretty

## 11050:00 - 11075:00

interesting way to think about it this

## 11075:00 - 11110:00

is a mixture of experts model for those

## 11110:00 - 11140:00

at home it's been part of what deep seek

## 11140:00 - 11190:00

has used to become much more efficient

## 11190:00 - 11230:00

uh in its in its reasoning for instance

## 11230:00 - 11255:00

because instead of lighting up the

## 11255:00 - 11290:00

entire large language model is deciding

## 11290:00 - 11335:00

to light up certain areas that might be

## 11335:00 - 11370:00

I it's not a deep seek Innovation but

## 11370:00 - 11390:00

they've just kind of used it to an

## 11390:00 - 11440:00

extreme extent um has that has using

## 11440:00 - 11475:00

that architecture helped you build this

## 11475:00 - 11510:00

in a way that for instance like reducing

## 11510:00 - 11550:00

latency or sort of lightening the

## 11550:00 - 11575:00

compute burden that you otherwise might

## 11575:00 - 11610:00

have had if you want something

## 11610:00 - 11675:00

incredibly fast stable even secure like

## 11675:00 - 11720:00

the paths on data right that where

## 11720:00 - 11760:00

you're really taking care of customers

## 11760:00 - 11790:00

um this is this is the fundamental

## 11790:00 - 11815:00

approach I think that that is

## 11815:00 - 11850:00

state-of-the-art and accurate and for

## 11850:00 - 11880:00

sure accurate don't forget accurate so

## 11880:00 - 11915:00

important yeah but on on that note I

## 11915:00 - 11980:00

mean are the is the new Alexa is there

## 11980:00 - 12015:00

going to be some sacrifice to having

## 12015:00 - 12055:00

those Alexa commands those standard turn

## 12055:00 - 12105:00

the lights on set the alarm um to in

## 12105:00 - 12140:00

order to enable all the llms to work the

## 12140:00 - 12165:00

way that they they're going to I think

## 12165:00 - 12200:00

you just called out the sacrifice and

## 12200:00 - 12255:00

it's time okay how long it's taken us to

## 12255:00 - 12280:00

get to where we are it's why it's my

## 12280:00 - 12300:00

favorite question like why is it taking

## 12300:00 - 12345:00

you so long like if I told you where we

## 12345:00 - 12400:00

were four months ago on somebody said

## 12400:00 - 12445:00

lock that door and then we had to

## 12445:00 - 12490:00

determine what that meant

## 12490:00 - 12545:00

versus in the past lock my front door

## 12545:00 - 12565:00

and you had to know it was the front

## 12565:00 - 12640:00

door and you had to say front door um

## 12640:00 - 12680:00

it's pretty phenomenal but you know 6

## 12680:00 - 12725:00

months ago it took longer than anyone

## 12725:00 - 12770:00

would wait to lock a door and you know

## 12770:00 - 12800:00

our customers need immediate response

## 12800:00 - 12835:00

and we won't make that trade-off so to

## 12835:00 - 12865:00

be that accurate with the latency that's

## 12865:00 - 12900:00

needed with the speed sub two seconds at

## 12900:00 - 12960:00

the end of the day um you end up you end

## 12960:00 - 12985:00

up needing a little bit more time ref

## 12985:00 - 13015:00

the expert so the expert can be quicker

## 13015:00 - 13040:00

and the model can pick the right model

## 13040:00 - 13075:00

quicker and the smaller model can be

## 13075:00 - 13100:00

trained to make sure it knows where the

## 13100:00 - 13145:00

door is he gave an example earlier which

## 13145:00 - 13175:00

I thought it's a Nuance but let me just

## 13175:00 - 13195:00

share it with

## 13195:00 - 13255:00

you previously in Alexa you couldn't say

## 13255:00 - 13280:00

play that

## 13280:00 - 13320:00

song it would look for a song called

## 13320:00 - 13370:00

that right it was that

## 13370:00 - 13410:00

simple now the model has to reason and

## 13410:00 - 13465:00

say that song I wonder what he's asking

## 13465:00 - 13490:00

I wonder what she's asking I wonder what

## 13490:00 - 13520:00

the person's asking that's what's

## 13520:00 - 13555:00

happening in the system then the expert

## 13555:00 - 13600:00

shows up looks at the history the

## 13600:00 - 13630:00

personalization what conversation were

## 13630:00 - 13680:00

we having play that song oh he's talking

## 13680:00 - 13700:00

about the conversation we just had about

## 13700:00 - 13750:00

Bradley Cooper and Lady Gaga shallow

## 13750:00 - 13800:00

shallow play that all happens in you

## 13800:00 - 13845:00

know Sub 2000 you know how how many

## 13845:00 - 13885:00

milliseconds are we talking we count in

## 13885:00 - 13920:00

single milliseconds now in component so

## 13920:00 - 13955:00

now you're all that is going on and the

## 13955:00 - 13985:00

Stack's working through it versus today

## 13985:00 - 14025:00

which is play shallow and that's the

## 14025:00 - 14050:00

only way you're going to play shallow

## 14050:00 - 14105:00

yep that's it and so I think it's just

## 14105:00 - 14120:00

understanding that

## 14120:00 - 14165:00

Nuance um in where natural language

## 14165:00 - 14200:00

comes in where you can talk to the you

## 14200:00 - 14260:00

can talk to Alexa without being precise

## 14260:00 - 14285:00

just like you can talk to me and I'll

## 14285:00 - 14335:00

use some microtels to get you know are

## 14335:00 - 14375:00

you asking me a rude question a great

## 14375:00 - 14405:00

question a nice question are you leading

## 14405:00 - 14445:00

me um and then from those microtels I

## 14445:00 - 14475:00

can then move to the words and then

## 14475:00 - 14510:00

determine where you're taking me and you

## 14510:00 - 14530:00

don't have to write it down type it and

## 14530:00 - 14570:00

read it exactly all that is happening

## 14570:00 - 14595:00

now in the machine which is pretty

## 14595:00 - 14630:00

powerful there was a cool scene in your

## 14630:00 - 14675:00

demo uh at the event at the launch event

## 14675:00 - 14710:00

where I think Panos it was you where you

## 14710:00 - 14740:00

said don't play the music in the baby's

## 14740:00 - 14785:00

room yeah so and it's really I didn't

## 14785:00 - 14815:00

say that so that's very explicit too

## 14815:00 - 14845:00

like don't play the music in the baby's

## 14845:00 - 14890:00

room it will the model will come up the

## 14890:00 - 14915:00

expert will show up the music expert

## 14915:00 - 14945:00

this is where it's super powerful and go

## 14945:00 - 14990:00

got it play it everywhere else or you

## 14990:00 - 15025:00

can just say don't wake the baby play

## 15025:00 - 15065:00

the music everywhere then the model will

## 15065:00 - 15115:00

go don't play it in the baby's room I

## 15115:00 - 15150:00

know I know what they're asking so this

## 15150:00 - 15185:00

is where that just that small model in

## 15185:00 - 15235:00

the expert does its job um and the fact

## 15235:00 - 15255:00

that you can just naturally move it

## 15255:00 - 15280:00

around in that demo I don't know if you

## 15280:00 - 15305:00

noticed by the way

## 15305:00 - 15335:00

nerve-wracking yeah so for listeners

## 15335:00 - 15380:00

Panos did this entire demo live I mean

## 15380:00 - 15395:00

we're going to talk about Apple

## 15395:00 - 15425:00

intelligence in a second but Apple

## 15425:00 - 15465:00

intelligence I was at the wwc launch

## 15465:00 - 15520:00

event and uh it was all a vision and

## 15520:00 - 15550:00

what we saw at this Alexa launch event

## 15550:00 - 15600:00

was a working demo now look I I mean we

## 15600:00 - 15635:00

know to reserve us commentators know to

## 15635:00 - 15665:00

reserve complete judgment until it's in

## 15665:00 - 15705:00

our hands yeah you have to for sure but

## 15705:00 - 15730:00

it was real it was all real real and

## 15730:00 - 15765:00

working yeah but what makes you nervous

## 15765:00 - 15790:00

in an event like that you're not worried

## 15790:00 - 15830:00

about the product working I mean six

## 15830:00 - 15855:00

months ago I would have worried about

## 15855:00 - 15880:00

the product working and I would have

## 15880:00 - 15905:00

shown you more Vision

## 15905:00 - 15975:00

demos like videos but the product's

## 15975:00 - 16000:00

working

## 16000:00 - 16035:00

the challenge is the

## 16035:00 - 16075:00

infrastructure the thousands of Wi-Fi

## 16075:00 - 16095:00

signals that are pinging around that

## 16095:00 - 16135:00

room like it's just an unusual these

## 16135:00 - 16180:00

live environments are very unusual turns

## 16180:00 - 16215:00

out Tech reporters like Tech and they're

## 16215:00 - 16265:00

using a lot of it we all on the Wi-Fi

## 16265:00 - 16295:00

well more more I mean the signals that

## 16295:00 - 16330:00

are being pulled from Bluetooth to Wi-Fi

## 16330:00 - 16380:00

to I mean who knows what's in pockets

## 16380:00 - 16410:00

and one of my favorite tech demo moments

## 16410:00 - 16450:00

is Steve Jobs just losing his on

## 16450:00 - 16500:00

stage cuz all the report are connected

## 16500:00 - 16520:00

to Wi-Fi and he's like you could either

## 16520:00 - 16555:00

be connected to Wi-Fi or you can have a

## 16555:00 - 16605:00

demo you pick totally yes that's but we

## 16605:00 - 16630:00

didn't have to have that situation so

## 16630:00 - 16650:00

but then and then you got you know the

## 16650:00 - 16675:00

servers have to be lit up and you you

## 16675:00 - 16695:00

know you're worried about latency and

## 16695:00 - 16725:00

what's happening in the room so you got

## 16725:00 - 16745:00

all that going on and now you're going

## 16745:00 - 16780:00

to do live and this is your baby right I

## 16780:00 - 16810:00

mean you love what you're about to show

## 16810:00 - 16860:00

you love it and if it doesn't go off

## 16860:00 - 16890:00

like I don't want to tell you what the

## 16890:00 - 16940:00

backup plan was you know what was backup

## 16940:00 - 16960:00

we're not going to talk about it for

## 16960:00 - 17005:00

real let's not talk about the backup

## 17005:00 - 17040:00

plan let me just say I can't tease the

## 17040:00 - 17070:00

backup plan and then not share the

## 17070:00 - 17090:00

backup plan they were really good they

## 17090:00 - 17120:00

were really good not a great it was not

## 17120:00 - 17155:00

a great backup just say no it was they

## 17155:00 - 17195:00

were great they were great they weren't

## 17195:00 - 17230:00

going to work but they were great plants

## 17230:00 - 17260:00

I would say I'm looking over here at

## 17260:00 - 17280:00

some of the team that was helping

## 17280:00 - 17350:00

yesterday I I uh but during that moment

## 17350:00 - 17415:00

um you you may have you may have heard

## 17415:00 - 17455:00

it's it was very nuanced at one point I

## 17455:00 - 17505:00

said move the musicak bring the music

## 17505:00 - 17560:00

here I want to hear the music over there

## 17560:00 - 17600:00

and the reason I use different

## 17600:00 - 17630:00

sentences I know what the model's going

## 17630:00 - 17665:00

to reason over and do but I wanted to

## 17665:00 - 17700:00

make it clear like you don't have to

## 17700:00 - 17730:00

think about what you want to happen you

## 17730:00 - 17780:00

just have to talk I want the music over

## 17780:00 - 17830:00

there okay and if and if the model

## 17830:00 - 17860:00

doesn't know or if the if Alexa doesn't

## 17860:00 - 17895:00

know she'll ask

## 17895:00 - 17950:00

you do you mean in the living room yeah

## 17950:00 - 17980:00

so so are we going to have a spe

## 17980:00 - 18005:00

trade-off here from the traditional

## 18005:00 - 18040:00

Alexa tasks just quickly Daniel I'm

## 18040:00 - 18070:00

curious like is it is the stuff I was

## 18070:00 - 18105:00

doing beforehand like or doing I'm doing

## 18105:00 - 18140:00

now um set an alarm is it going to take

## 18140:00 - 18165:00

a little longer because of this process

## 18165:00 - 18195:00

or it'll be the same amount of time no

## 18195:00 - 18225:00

be I mean this is where we have such a

## 18225:00 - 18265:00

high bar before we're willing to put it

## 18265:00 - 18310:00

out because and and deterministic

## 18310:00 - 18375:00

systems are incredibly fast right it is

## 18375:00 - 18410:00

it is straightforward computer science

## 18410:00 - 18455:00

in this day and age with an AWS cloud

## 18455:00 - 18490:00

and the great connect ity that everyone

## 18490:00 - 18510:00

has in their homes to make a

## 18510:00 - 18535:00

deterministic system fast on something

## 18535:00 - 18570:00

exactly like you said making a

## 18570:00 - 18600:00

non-deterministic system fast that can

## 18600:00 - 18625:00

respond in any way gathers all the

## 18625:00 - 18680:00

context figures out Legions of different

## 18680:00 - 18710:00

things which experts to invoke making

## 18710:00 - 18745:00

that system fast on something as simple

## 18745:00 - 18800:00

as a instruction or you know is is hard

## 18800:00 - 18835:00

that quite hard What technological

## 18835:00 - 18865:00

breakthroughs or Innovations did you

## 18865:00 - 18910:00

rely on to get it from a place where you

## 18910:00 - 18955:00

were dissatisfied with the latency to a

## 18955:00 - 18990:00

point now or you're happy well I think

## 18990:00 - 19020:00

it's it's another version of using the

## 19020:00 - 19050:00

right tool for the job and building

## 19050:00 - 19095:00

building a system of that's frankly just

## 19095:00 - 19145:00

more complex overall to get the simple

## 19145:00 - 19175:00

things done so it's a bit you know

## 19175:00 - 19200:00

there's like an irony in that but you

## 19200:00 - 19225:00

need a system

## 19225:00 - 19275:00

that creates very fast paths for simple

## 19275:00 - 19300:00

things even though you started with an

## 19300:00 - 19335:00

incredibly complex system already you're

## 19335:00 - 19370:00

adding these kinds of complexity to get

## 19370:00 - 19405:00

simple things done so that I mean I

## 19405:00 - 19430:00

won't go into the specific technical

## 19430:00 - 19470:00

details here but that is that's the

## 19470:00 - 19495:00

upshot you need to be able to figure out

## 19495:00 - 19520:00

you're trying to do something simple so

## 19520:00 - 19560:00

that you can do it fast very comp and it

## 19560:00 - 19615:00

gets tricky you know people understand

## 19615:00 - 19665:00

how to speak to Alexa today I think our

## 19665:00 - 19695:00

new customers we want to you know and

## 19695:00 - 19715:00

current customers we want to open their

## 19715:00 - 19755:00

minds on what they can ask for and how

## 19755:00 - 19805:00

to how to get something done um take the

## 19805:00 - 19870:00

simple tasks that we have timers alarms

## 19870:00 - 19895:00

there's a different way to think about

## 19895:00 - 19935:00

them and then in the non-deterministic

## 19935:00 - 19970:00

world how to translate what's being said

## 19970:00 - 20005:00

into what's being asked for which is

## 20005:00 - 20060:00

different um an example you said how

## 20060:00 - 20080:00

quick will be setting an alarm it'll be

## 20080:00 - 20125:00

lightning fast and you'll likely set it

## 20125:00 - 20170:00

the way you always have I need an alarm

## 20170:00 - 20200:00

set an alarm for 8: a.m. I think that's

## 20200:00 - 20245:00

the classic way to set an alarm or you

## 20245:00 - 20280:00

can say Alexa I need to I need to wake

## 20280:00 - 20310:00

up tomorrow at

## 20310:00 - 20360:00

8 okay and now that's non- determinist

## 20360:00 - 20385:00

and now it's going I think you need an

## 20385:00 - 20420:00

alarm and then it'll offer you an alarm

## 20420:00 - 20480:00

or just set it same with the timer set

## 20480:00 - 20495:00

me a

## 20495:00 - 20540:00

timer um by the way how long do you want

## 20540:00 - 20580:00

the timer for you say the time you can

## 20580:00 - 20630:00

move that to uh set me a timer to I'm

## 20630:00 - 20665:00

cooking my steak medium rare and then

## 20665:00 - 20690:00

she'll say I'm setting you a timer for

## 20690:00 - 20735:00

six minutes okay and so you understand

## 20735:00 - 20760:00

like when you get into that natural

## 20760:00 - 20780:00

language non- deterministic what's

## 20780:00 - 20810:00

happening what are you asking for you're

## 20810:00 - 20835:00

cooking your steak okay I'll get you six

## 20835:00 - 20885:00

minutes on each side or tell me how

## 20885:00 - 20925:00

thick it is and then the answer is you

## 20925:00 - 20970:00

know 2 in thick whatever or I want a

## 20970:00 - 21015:00

Ramen egg that's 8 minutes I got you

## 21015:00 - 21060:00

tell me when you start I'm starting 8

## 21060:00 - 21095:00

Minute Timer started for you and so the

## 21095:00 - 21130:00

world just change from even these most

## 21130:00 - 21160:00

simple

## 21160:00 - 21215:00

tasks it it just changes in the spirit

## 21215:00 - 21255:00

of by the way I never knew how long it

## 21255:00 - 21280:00

took to cook a Ramen egg so I'd always

## 21280:00 - 21315:00

have to go to Tik Tok open it spend 20

## 21315:00 - 21345:00

seconds watching somebody make ramen

## 21345:00 - 21380:00

eggs and then eventually it says put it

## 21380:00 - 21405:00

in the water for eight minutes like

## 21405:00 - 21430:00

that's all you see on TI to for the next

## 21430:00 - 21470:00

week and then I would say yeah that's

## 21470:00 - 21495:00

very True by you by the way don't search

## 21495:00 - 21525:00

Ramen eggs it'll you get hammered with

## 21525:00 - 21565:00

Ramen eggs but I I think uh and then all

## 21565:00 - 21585:00

of a sudden you're like got it 8 minutes

## 21585:00 - 21615:00

set a timer for 8 minutes now just

## 21615:00 - 21650:00

change it just ask for ramen egg and

## 21650:00 - 21675:00

Alexa will just determine what you're

## 21675:00 - 21695:00

looking for and give you an8 Minute

## 21695:00 - 21730:00

Timer okay so just to wrap this section

## 21730:00 - 21775:00

on the technical side my note that I

## 21775:00 - 21805:00

wrote to myself that said they spent too

## 21805:00 - 21845:00

much time building the Alexa microwave

## 21845:00 - 21880:00

and the Alexa alarm clock and not

## 21880:00 - 21925:00

focusing on the technology maybe uh I

## 21925:00 - 21955:00

underestimated the technological lift

## 21955:00 - 21995:00

here a little bit

## 21995:00 - 22020:00

I don't know we can't determine what you

## 22020:00 - 22055:00

were thinking for sure but I think

## 22055:00 - 22080:00

there's a lift here you said it's a feat

## 22080:00 - 22115:00

of engineering that's where you started

## 22115:00 - 22140:00

we have one of the best teams on the

## 22140:00 - 22180:00

planet working on this uh a lot of it

## 22180:00 - 22210:00

has 10 years of history in it you know

## 22210:00 - 22255:00

there's so many um people that work on

## 22255:00 - 22280:00

Alexa today that have been there since

## 22280:00 - 22310:00

its Inception you've got a lot of

## 22310:00 - 22335:00

passion around that in the engineering

## 22335:00 - 22365:00

team and the product you know just the

## 22365:00 - 22395:00

product Team all up we call product

## 22395:00 - 22420:00

makers when you put them all in a

## 22420:00 - 22475:00

collection um and yeah it's a feat it's

## 22475:00 - 22500:00

it it it's okay though we don't it

## 22500:00 - 22520:00

doesn't matter if somebody thinks it

## 22520:00 - 22545:00

should be easy or it's not easy or

## 22545:00 - 22575:00

whatever it doesn't matter actually if

## 22575:00 - 22600:00

it feels like it's easy that sounds

## 22600:00 - 22630:00

pretty good to me right I mean I don't

## 22630:00 - 22680:00

mind it means the customer is happy like

## 22680:00 - 22725:00

this must have been easy like yeah okay

## 22725:00 - 22760:00

I don't care do you like it like do you

## 22760:00 - 22790:00

love it great and that's I think that's

## 22790:00 - 22820:00

where we go so I want to talk about the

## 22820:00 - 22855:00

vision of this product because and the

## 22855:00 - 22900:00

strategy that you're going to put into

## 22900:00 - 22930:00

play here because again I was sitting in

## 22930:00 - 22950:00

the audience and I talked about Apple

## 22950:00 - 22990:00

intelligence before I guess the SE the

## 22990:00 - 23040:00

seg this segment of our conversation is

## 23040:00 - 23070:00

I I've headlined it's Apple intelligence

## 23070:00 - 23125:00

but it works um and you know it's a

## 23125:00 - 23150:00

little factious but I tried not to read

## 23150:00 - 23175:00

anything you posted coming in today

## 23175:00 - 23200:00

because I was like oh no I don't want to

## 23200:00 - 23245:00

defend or have a preconceived notion so

## 23245:00 - 23275:00

that's interesting to keep sharing we've

## 23275:00 - 23310:00

been talking on the show a lot about how

## 23310:00 - 23355:00

you know and yeah just we talked a lot

## 23355:00 - 23420:00

about the buildup to wwc the reveal and

## 23420:00 - 23465:00

it was a a it seems like every Big tech

## 23465:00 - 23500:00

company has almost the same vision and

## 23500:00 - 23535:00

tell me if I'm wrong here but like apple

## 23535:00 - 23565:00

was like the Apple intelligence demo was

## 23565:00 - 23615:00

like um you talk to Siri and ask when

## 23615:00 - 23650:00

your flight is and you're switching

## 23650:00 - 23690:00

flights and it's helping you pick your

## 23690:00 - 23740:00

kids up and um that demo looked a lot

## 23740:00 - 23775:00

like the Google Assistant demo that I've

## 23775:00 - 23825:00

seen like almost every year at Google IO

## 23825:00 - 23890:00

and uh and then I saw your demo and I

## 23890:00 - 23940:00

was also just like this is a similar

## 23940:00 - 23990:00

idea which is that it's a a contextually

## 23990:00 - 24015:00

it's a contextually

## 24015:00 - 24085:00

aware smart AI assistant that helps you

## 24085:00 - 24120:00

get things done and makes your life

## 24120:00 - 24180:00

easier so I'm curious if if you both see

## 24180:00 - 24210:00

the competitive landscape in the same

## 24210:00 - 24255:00

way I do if there's something different

## 24255:00 - 24305:00

about Alexa than the others and how you

## 24305:00 - 24365:00

plan to win uh given the the landscape

## 24365:00 - 24410:00

is developing the way it is you want to

## 24410:00 - 24445:00

jump in so I got a long one here so why

## 24445:00 - 24475:00

don't you just know you start and then

## 24475:00 - 24500:00

I'll

## 24500:00 - 24555:00

go I mean here look the vision for Alexa

## 24555:00 - 24605:00

has been super consistent actually uh

## 24605:00 - 24640:00

for 10 years I think Panos this was it

## 24640:00 - 24670:00

made it into your final deck I believe

## 24670:00 - 24710:00

yesterday you know we we have always

## 24710:00 - 24770:00

wanted to just make lives easier better

## 24770:00 - 24815:00

simpler uh and be the world's best

## 24815:00 - 24840:00

personal assistant that's been the

## 24840:00 - 24885:00

vision for Alexa from the beginning um

## 24885:00 - 24920:00

and so now we just have a technical leap

## 24920:00 - 24960:00

that lets us get closer to that Vision

## 24960:00 - 24980:00

but nothing

## 24980:00 - 25020:00

you know that's been the vision since uh

## 25020:00 - 25050:00

for for all 10 years that Alexa has been

## 25050:00 - 25115:00

out there we have a much more capable AI

## 25115:00 - 25135:00

assistant that's

## 25135:00 - 25170:00

conversational that is personal and

## 25170:00 - 25205:00

personalized now that can get an

## 25205:00 - 25245:00

incredible amount of things done for you

## 25245:00 - 25270:00

uh but the vision is consistent okay I

## 25270:00 - 25295:00

want to go to ponos in a second but I I

## 25295:00 - 25325:00

need to follow up on that because you

## 25325:00 - 25375:00

know the the reaction to this reveal has

## 25375:00 - 25415:00

been this is great it's personalized it

## 25415:00 - 25435:00

has your data to help you figure things

## 25435:00 - 25465:00

out but then you look at a company like

## 25465:00 - 25510:00

Apple which has so much personal data

## 25510:00 - 25535:00

for that people have trusted apple with

## 25535:00 - 25565:00

because it's all it has this security

## 25565:00 - 25610:00

messaging or Google which you know has

## 25610:00 - 25635:00

your you know maybe your Gmail your

## 25635:00 - 25690:00

Google calendar Google Maps uh this is

## 25690:00 - 25715:00

these are the services that you use to

## 25715:00 - 25750:00

get around the world and interact with

## 25750:00 - 25820:00

people um so if you're going to be this

## 25820:00 - 25850:00

personalized assistant like you are

## 25850:00 - 25890:00

coming up against these companies that

## 25890:00 - 25925:00

basically have already been deeply

## 25925:00 - 25955:00

integrated into people's daily daily

## 25955:00 - 26000:00

routines so what is the play there I

## 26000:00 - 26065:00

mean it the the phone you're basically

## 26065:00 - 26110:00

asking about the role of the phone uh in

## 26110:00 - 26135:00

not just the phone because Google has

## 26135:00 - 26170:00

I'm I'm plenty of services on the

## 26170:00 - 26220:00

desktop I mean I'm on an Apple machine I

## 26220:00 - 26260:00

got Gmail open maps to figure out how to

## 26260:00 - 26310:00

get here calendar and so it's it's the

## 26310:00 - 26345:00

op almost the operating system for your

## 26345:00 - 26380:00

your life I mean look you you you told

## 26380:00 - 26410:00

us you have echo in every room in your

## 26410:00 - 26440:00

home and that's great that's also true

## 26440:00 - 26475:00

I'm starting to think may I too much

## 26475:00 - 26510:00

and well you might look at your job I

## 26510:00 - 26525:00

mean come

## 26525:00 - 26570:00

on you didn't this would be a problem

## 26570:00 - 26600:00

saying customers you know we do so much

## 26600:00 - 26635:00

for customers in the home today and of

## 26635:00 - 26670:00

course we're Amazon so that's not just

## 26670:00 - 26690:00

thank you by the way for having echo in

## 26690:00 - 26725:00

every room in your home that's awesome

## 26725:00 - 26760:00

uh but also we probably put some

## 26760:00 - 26795:00

packages on your doorstep and probably

## 26795:00 - 26830:00

stream you some content and we've got

## 26830:00 - 26855:00

great deep relationships with our

## 26855:00 - 26905:00

customers Prime is an incredibly

## 26905:00 - 26950:00

valuable program for example and you

## 26950:00 - 26970:00

know hundreds of millions of customer

## 26970:00 - 27005:00

customers literally take value uh in

## 27005:00 - 27045:00

that and love it and use it all the time

## 27045:00 - 27090:00

so we we love our relationship with our

## 27090:00 - 27130:00

customers too and think that we can

## 27130:00 - 27160:00

deeply integrate any Services customers

## 27160:00 - 27200:00

want as well we work with Gmail we have

## 27200:00 - 27240:00

the Outlook calendar we integrate Apple

## 27240:00 - 27265:00

calendar I think it's a very powerful

## 27265:00 - 27310:00

Point like you have to take that and and

## 27310:00 - 27335:00

understand like we're both kind of a we

## 27335:00 - 27385:00

have this if you will you have music

## 27385:00 - 27440:00

shopping movies this is real things that

## 27440:00 - 27475:00

people love doing in the home I mean

## 27475:00 - 27515:00

this these are personal at every level

## 27515:00 - 27570:00

um photos but also but we're such an

## 27570:00 - 27630:00

open platform with thousands of Partners

## 27630:00 - 27665:00

um it's hard to say it's a platform so

## 27665:00 - 27695:00

I'd be careful with the word but at the

## 27695:00 - 27735:00

end of the day every single integration

## 27735:00 - 27815:00

Point um across Alexa gives us so many

## 27815:00 - 27850:00

of those insights as well but the key

## 27850:00 - 27890:00

and Daniel hit it he when he asked you a

## 27890:00 - 27920:00

question it might have been rhetorical

## 27920:00 - 27975:00

at some level um

## 27975:00 - 28010:00

I don't I don't think there's anyone

## 28010:00 - 28055:00

close um to being able to understand

## 28055:00 - 28070:00

your

## 28070:00 - 28160:00

home as as Amazon as Alexa it's very

## 28160:00 - 28195:00

it's it's it's a super important element

## 28195:00 - 28250:00

for us Alex like the idea that smart

## 28250:00 - 28275:00

home is connected to your music to your

## 28275:00 - 28315:00

entertainment to your life the fact that

## 28315:00 - 28345:00

we're now bringing in memory to Alexa

## 28345:00 - 28365:00

and you can have that conversation it'll

## 28365:00 - 28425:00

hold the context for you I I think I

## 28425:00 - 28445:00

don't think there's anything else like

## 28445:00 - 28470:00

it because then it's connected to to all

## 28470:00 - 28515:00

your services in a natural way too I

## 28515:00 - 28540:00

don't think it replaces the centerpiece

## 28540:00 - 28575:00

of the phone I think it just adds value

## 28575:00 - 28620:00

to your life in a very different way and

## 28620:00 - 28655:00

I think there might be a little bit of

## 28655:00 - 28680:00

opportunity and this is me understating

## 28680:00 - 28730:00

it but the ambient devices in your house

## 28730:00 - 28760:00

right now and the ones that you can buy

## 28760:00 - 28775:00

from us and some of the beautiful

## 28775:00 - 28800:00

products that we're both making now and

## 28800:00 - 28845:00

have released recently they're in your

## 28845:00 - 28895:00

home and you don't have to think you

## 28895:00 - 28925:00

don't have to open anything you don't

## 28925:00 - 28970:00

have to log into anything you just have

## 28970:00 - 29025:00

to be there and speak and it's a it's a

## 29025:00 - 29055:00

powerful concept when it when natural

## 29055:00 - 29080:00

language shows

## 29080:00 - 29125:00

up yeah I was with uh speaking with Jal

## 29125:00 - 29160:00

gani the head of prime at your event

## 29160:00 - 29195:00

yesterday and he was talking about how

## 29195:00 - 29250:00

the the family calendar is on his Alexa

## 29250:00 - 29300:00

device and it is a Google Calendar so

## 29300:00 - 29325:00

there the fact that there is that

## 29325:00 - 29360:00

interoperability I think where yeah you

## 29360:00 - 29400:00

don't have a phone uh that actually

## 29400:00 - 29425:00

might maybe that's an advantage I'm just

## 29425:00 - 29450:00

trying to it is an advantage just think

## 29450:00 - 29475:00

of it this way like we're not asking you

## 29475:00 - 29520:00

to start something that you knew that

## 29520:00 - 29580:00

you don't already do right we we just

## 29580:00 - 29620:00

want to make it simpler for you so

## 29620:00 - 29670:00

Google Calendar is a great example okay

## 29670:00 - 29700:00

just attach all four of your family's

## 29700:00 - 29720:00

calendar we'll make it a family calendar

## 29720:00 - 29750:00

and put it front in Center for you and

## 29750:00 - 29770:00

then when you decide if you're going to

## 29770:00 - 29810:00

dinner on Friday night we'll rationalize

## 29810:00 - 29860:00

it and you know that concept that

## 29860:00 - 29900:00

there's a communal device in your house

## 29900:00 - 29945:00

that everyone can see you know it's

## 29945:00 - 29960:00

something that people have been asking

## 29960:00 - 29995:00

for for a long time but now that you

## 29995:00 - 30035:00

have so much intelligence in the product

## 30035:00 - 30065:00

and it can do the rationalization for

## 30065:00 - 30120:00

you you I feel like we stand alone there

## 30120:00 - 30155:00

I do think I would I think this calendar

## 30155:00 - 30185:00

example is one that helps flip the

## 30185:00 - 30215:00

question a little bit in my mind

## 30215:00 - 30275:00

because it really is like how often do

## 30275:00 - 30325:00

you say well it was just on my

## 30325:00 - 30365:00

calendar I didn't know to meet you there

## 30365:00 - 30400:00

why I was on my work

## 30400:00 - 30440:00

calendar I say that to my wife tally you

## 30440:00 - 30495:00

know all the time she's like we we we

## 30495:00 - 30520:00

missed the restaurant we missed the

## 30520:00 - 30570:00

reservation so anyway having one spot

## 30570:00 - 30610:00

that is can be communal and personal

## 30610:00 - 30635:00

it's pretty powerful I want to press a

## 30635:00 - 30680:00

little bit on this because the phone

## 30680:00 - 30735:00

seems to be the place where people like

## 30735:00 - 30760:00

it's it's all about like where do people

## 30760:00 - 30795:00

interact with these assistants yep the

## 30795:00 - 30815:00

phone seems like it's going to be a

## 30815:00 - 30860:00

pretty important place it will be so if

## 30860:00 - 30885:00

you don't have a phone I mean again

## 30885:00 - 30905:00

there's some advantage in that like you

## 30905:00 - 30935:00

can bring any service in but like if

## 30935:00 - 30985:00

people are like on uh an Android and

## 30985:00 - 31025:00

they're summoning a Google Assistant uh

## 31025:00 - 31055:00

whatever the name is that week or

## 31055:00 - 31090:00

they're on uh an iPhone and they're

## 31090:00 - 31170:00

summoning Apple intelligence or Siri um

## 31170:00 - 31215:00

where does Alexa fit in on that like is

## 31215:00 - 31230:00

are you going to have to look at deeper

## 31230:00 - 31255:00

Integrations with these phone makers

## 31255:00 - 31280:00

will they even allow you to do that I

## 31280:00 - 31295:00

think people will use different

## 31295:00 - 31315:00

assistants I don't think there's any

## 31315:00 - 31340:00

question about it I don't think there's

## 31340:00 - 31390:00

one although if you lean into Alexa we

## 31390:00 - 31430:00

have the Alexa app on the phone and with

## 31430:00 - 31460:00

one touch of the button on your iPhone

## 31460:00 - 31480:00

you're having the same conversation

## 31480:00 - 31495:00

you're actually carrying the

## 31495:00 - 31515:00

conversation from your home to your

## 31515:00 - 31560:00

phone to your car to your PC with

## 31560:00 - 31590:00

alexa.com we thought that through

## 31590:00 - 31620:00

because we needed that thread for sure

## 31620:00 - 31670:00

so you know as she becomes more personal

## 31670:00 - 31720:00

to you and then you know more needed you

## 31720:00 - 31755:00

want to have her with you everywhere

## 31755:00 - 31795:00

that that app is doing a crazy cool job

## 31795:00 - 31815:00

right now and we haven't released the

## 31815:00 - 31850:00

new Alexa app yet it's coming with if

## 31850:00 - 31880:00

you get Alexa plus you get the Alexa app

## 31880:00 - 31920:00

the Alexa Plus app as well as alexa.com

## 31920:00 - 31945:00

ala.com right there's going to be a web

## 31945:00 - 31985:00

version of this there is um and you just

## 31985:00 - 32010:00

see the more traditional long form work

## 32010:00 - 32035:00

that you do with any AI browser at this

## 32035:00 - 32065:00

point it's the easiest way to say it but

## 32065:00 - 32100:00

you also get all the personalization you

## 32100:00 - 32125:00

also get the context of carryover if you

## 32125:00 - 32150:00

had a conversation in your kitchen it'll

## 32150:00 - 32170:00

just remind you what conversations

## 32170:00 - 32195:00

you've had lately if you've booked a

## 32195:00 - 32225:00

reservation whatever you've done it'll

## 32225:00 - 32250:00

collect it there it so it'll be on your

## 32250:00 - 32285:00

PC and your phone as well so I think we

## 32285:00 - 32315:00

just want to provide that for our

## 32315:00 - 32340:00

customer so they have the opportunity to

## 32340:00 - 32365:00

say I want my assistant my single

## 32365:00 - 32395:00

assistant with me everywhere you might

## 32395:00 - 32415:00

use your phone for different things you

## 32415:00 - 32435:00

might use a different AI assistant on

## 32435:00 - 32470:00

your phone I think that's a fair you

## 32470:00 - 32505:00

know Fair proxy I I don't I wouldn't

## 32505:00 - 32525:00

disagree it just depends on what's the

## 32525:00 - 32550:00

best path to get something done I think

## 32550:00 - 32600:00

Alexa will provide a lot of that best

## 32600:00 - 32650:00

path okay I want to take a quick break

## 32650:00 - 32680:00

and then talk a little bit about the

## 32680:00 - 32740:00

agentic elements in your uh new Alexa

## 32740:00 - 32795:00

release where agents uh might be going

## 32795:00 - 32825:00

and then maybe we dream a little bit

## 32825:00 - 32850:00

about where this technology is going to

## 32850:00 - 32890:00

lead we'll be back right after this and

## 32890:00 - 32915:00

we're back here on big technology

## 32915:00 - 32950:00

podcast with two Amazon Executives

## 32950:00 - 32970:00

responsible

## 32970:00 - 33000:00

for the new Alexa we have Panos panai

## 33000:00 - 33035:00

here is Amazon's senior vice president

## 33035:00 - 33070:00

of devices and service and Daniel Rous

## 33070:00 - 33125:00

is Amazon's vice president of Alexa and

## 33125:00 - 33205:00

Fire TV uh so it's interesting that Alex

## 33205:00 - 33260:00

that that um this a gentic buzzword is

## 33260:00 - 33310:00

now starting to be translated into

## 33310:00 - 33340:00

things that we're things that we're

## 33340:00 - 33365:00

seeing in product and it's kind of

## 33365:00 - 33390:00

interesting because Alexa's had skills

## 33390:00 - 33430:00

for a while like call me in Uber and now

## 33430:00 - 33470:00

you can use Alexa to call you maneuver

## 33470:00 - 33510:00

so um is this actually like a really a

## 33510:00 - 33555:00

new moment for a gentic AI or is this a

## 33555:00 - 33580:00

rebranding of some stuff that works a

## 33580:00 - 33625:00

little better than it has Panos what do

## 33625:00 - 33645:00

you

## 33645:00 - 33685:00

think I I can't get it to work anywhere

## 33685:00 - 33750:00

else I mean I think this is a at the end

## 33750:00 - 33785:00

of the day it's it's incredibly new but

## 33785:00 - 33815:00

it's also solving so many different

## 33815:00 - 33865:00

things at the same time first

## 33865:00 - 33920:00

um you have to always go back to how

## 33920:00 - 33960:00

much understanding is is in an utterance

## 33960:00 - 33995:00

just in natural language being able to

## 33995:00 - 34020:00

translate it and we've talked about this

## 34020:00 - 34055:00

already getting down to calling a

## 34055:00 - 34080:00

service calling the right API part

## 34080:00 - 34110:00

making the right partnership so that API

## 34110:00 - 34145:00

is called to make it as simple as

## 34145:00 - 34200:00

possible um it it it's uh I don't think

## 34200:00 - 34220:00

it's been accomplished I don't think

## 34220:00 - 34250:00

you're seeing it out there anywhere

## 34250:00 - 34285:00

connected to an assistant right now I

## 34285:00 - 34320:00

think there's a lot

## 34320:00 - 34355:00

of maybe I maybe you've seen it you got

## 34355:00 - 34395:00

to share with me where it is but uh I

## 34395:00 - 34420:00

don't think you have I don't I have not

## 34420:00 - 34465:00

and so what agents fundamentally like

## 34465:00 - 34505:00

using you know a core llm with an agent

## 34505:00 - 34540:00

non- deterministic calling the right API

## 34540:00 - 34565:00

calling that service booking that

## 34565:00 - 34595:00

service bringing it back and tying it

## 34595:00 - 34625:00

back into all your other services it's a

## 34625:00 - 34655:00

demo we've we've all seen a thousand

## 34655:00 - 34680:00

times but haven't been able to use I

## 34680:00 - 34735:00

think as consumers yeah

## 34735:00 - 34795:00

um okay I I think yeah maybe maybe

## 34795:00 - 34820:00

that's the case I haven't seen those

## 34820:00 - 34850:00

demos myself but I do I believe it I

## 34850:00 - 34880:00

believe it I maybe just need to watch

## 34880:00 - 34920:00

closer uh but I do think it's new I

## 34920:00 - 34965:00

think it's new um what we've cre in what

## 34965:00 - 34985:00

we're doing and building it up I think

## 34985:00 - 35035:00

it is I also think we mean we might mean

## 35035:00 - 35075:00

different things by agent and so I'm

## 35075:00 - 35110:00

just curious Alex what do you what yeah

## 35110:00 - 35135:00

make sure we're grounded in your

## 35135:00 - 35175:00

definition sure there's a ground just in

## 35175:00 - 35205:00

passing I mentioned yesterday in my own

## 35205:00 - 35240:00

part of uh part of our event you know

## 35240:00 - 35270:00

that boy everyone just uses this term

## 35270:00 - 35295:00

agent and I do think people use it in

## 35295:00 - 35330:00

different ways what does it mean to you

## 35330:00 - 35350:00

yeah it's such a great question because

## 35350:00 - 35380:00

I do think that in some ways that agent

## 35380:00 - 35425:00

has been used to Rebrand

## 35425:00 - 35475:00

automation um we've seeing automation

## 35475:00 - 35520:00

demos forever I mean even so just to

## 35520:00 - 35540:00

give you one example upon I wasn't

## 35540:00 - 35575:00

trying to shade the Amazon uh demo I was

## 35575:00 - 35600:00

just to give you one example yeah we

## 35600:00 - 35635:00

were all I mean we a lot of folks

## 35635:00 - 35655:00

watching the tech world were at

## 35655:00 - 35710:00

google.io when they demoed a voice

## 35710:00 - 35740:00

assistant that will go they will call a

## 35740:00 - 35775:00

restaurant for you and book you a table

## 35775:00 - 35800:00

and like they did the actual

## 35800:00 - 35840:00

conversation and the the assistant has

## 35840:00 - 35875:00

like human utterance goes um well maybe

## 35875:00 - 35910:00

we could have a table for it's like and

## 35910:00 - 35950:00

then it would go and book you book you

## 35950:00 - 35975:00

the restaurant I don't I I just don't

## 35975:00 - 36005:00

remember using it but correct so again

## 36005:00 - 36030:00

there's the demo there's the demo and

## 36030:00 - 36050:00

then there's real life and but I think

## 36050:00 - 36080:00

it was also just like you gave a tech

## 36080:00 - 36110:00

command and it would go out and do that

## 36110:00 - 36160:00

for you um but I a lot of this stuff

## 36160:00 - 36190:00

like I said we we've seen demos we

## 36190:00 - 36220:00

haven't seen it uh actually work my

## 36220:00 - 36260:00

definition for agent uh is something

## 36260:00 - 36295:00

that can go out and and accomplish for

## 36295:00 - 36365:00

you uh so um you know you you had a a

## 36365:00 - 36415:00

good demo that I enjoyed watching about

## 36415:00 - 36470:00

um trying to go see a uh Red Sox Yankee

## 36470:00 - 36510:00

game uh by the way for folks listening

## 36510:00 - 36555:00

we the the reveal event was in New York

## 36555:00 - 36585:00

Daniel's apparently a Red Sox fan he

## 36585:00 - 36610:00

trolled the entire audience including

## 36610:00 - 36650:00

the guy sitting directly guy wearing a a

## 36650:00 - 36695:00

Yankee it was almost like he planned it

## 36695:00 - 36725:00

we I kept saying I'm are you sure you

## 36725:00 - 36760:00

want to do this Red Sox bit he's like

## 36760:00 - 36795:00

sure goes through the entire offseason

## 36795:00 - 36835:00

acquisitions which I like I mean as a

## 36835:00 - 36875:00

Mets fan I I will say fine you were fine

## 36875:00 - 36900:00

by the way you saw that that you saw the

## 36900:00 - 36930:00

info expert in action right there that's

## 36930:00 - 36970:00

what it was yeah because your and it was

## 36970:00 - 37000:00

it was not deterministic and then of

## 37000:00 - 37030:00

course it's a different answer every

## 37030:00 - 37080:00

time Alec um every time um Daniel did

## 37080:00 - 37125:00

the demo at the end of the day I mean it

## 37125:00 - 37155:00

was Alexa's decision to talk about Alex

## 37155:00 - 37185:00

bregman it wasn't Daniel's like you

## 37185:00 - 37220:00

couldn't lead that you can't you can't

## 37220:00 - 37265:00

plan that and so a bit of a risky demo

## 37265:00 - 37290:00

because if Alexa decided not to talk

## 37290:00 - 37315:00

about bregman I don't know where you

## 37315:00 - 37345:00

would have taken them I do know a lot

## 37345:00 - 37380:00

about the Red Sox so I figured you know

## 37380:00 - 37400:00

maybe eventually we get to buy some

## 37400:00 - 37435:00

tickets as what was I was thinking but

## 37435:00 - 37470:00

it it wasn't it was to set an example of

## 37470:00 - 37505:00

that kind of agentic capability of set

## 37505:00 - 37545:00

the Baseline of what we mean which is

## 37545:00 - 37575:00

hey I just I actually was just having a

## 37575:00 - 37620:00

a chat about the Red Sox could I get

## 37620:00 - 37645:00

some tickets actually that's a tough

## 37645:00 - 37680:00

game to get oh they're expensive can you

## 37680:00 - 37710:00

watch for tickets for me I mean that

## 37710:00 - 37740:00

that was where we ended up with the demo

## 37740:00 - 37760:00

could have ended up in a lot of

## 37760:00 - 37790:00

different places but being able to set

## 37790:00 - 37835:00

an agent off if you want to call it an

## 37835:00 - 37865:00

agent in that case we think about it a

## 37865:00 - 37900:00

little bit differently but in that case

## 37900:00 - 37940:00

that agentic capability to say first of

## 37940:00 - 37965:00

all I could buy you these tickets right

## 37965:00 - 38005:00

now second of all you don't like the

## 38005:00 - 38065:00

price I'll watch for you infinite

## 38065:00 - 38120:00

patience never runs out of gas if those

## 38120:00 - 38150:00

tickets do drop below a certain price

## 38150:00 - 38185:00

I'm notified and can buy them that's a

## 38185:00 - 38230:00

hugely useful thing for a customer yeah

## 38230:00 - 38260:00

and you could buy it with a command yeah

## 38260:00 - 38280:00

because you're integrated with Ticket

## 38280:00 - 38350:00

Master exactly yep so we so yeah to me I

## 38350:00 - 38400:00

would say that's a gentic behavior great

## 38400:00 - 38445:00

I would say it qualifies um we we had

## 38445:00 - 38480:00

some questions in in a we have a big

## 38480:00 - 38505:00

technology Discord I was like sharing

## 38505:00 - 38540:00

notes with the with the crew as the

## 38540:00 - 38575:00

event was going on and we had some um

## 38575:00 - 38615:00

notes from people about what they they

## 38615:00 - 38665:00

want uh sort of Beyond those simple use

## 38665:00 - 38705:00

cases cool what is I call it simple but

## 38705:00 - 38740:00

you know obviously there's a tech

## 38740:00 - 38775:00

there's a there's a tech lift to get it

## 38775:00 - 38850:00

done so um one one of our listeners said

## 38850:00 - 38875:00

is it going is Alexa still going to be

## 38875:00 - 38915:00

reactive to requests or can it be

## 38915:00 - 38950:00

proactive and suggest at the start of

## 38950:00 - 38965:00

the day

## 38965:00 - 39000:00

uh some smart ideas based on the context

## 39000:00 - 39050:00

that Amazon has for instance um I would

## 39050:00 - 39085:00

say you know do I need to order any

## 39085:00 - 39135:00

birthday gifts and it would then go out

## 39135:00 - 39160:00

go out and say well look on your

## 39160:00 - 39185:00

calendar there are you know five

## 39185:00 - 39220:00

birthdays coming up these are the dates

## 39220:00 - 39260:00

and these are our suggestions so is it

## 39260:00 - 39285:00

going to get is it because that's I

## 39285:00 - 39305:00

think a step further I think you're

## 39305:00 - 39330:00

stepping in you're stepping you said you

## 39330:00 - 39345:00

want to talk a little bit about the

## 39345:00 - 39390:00

future and how proactive Alexa can be

## 39390:00 - 39415:00

like there's a balance one we think

## 39415:00 - 39450:00

Alexa can be incredibly proactive like

## 39450:00 - 39470:00

to the point of when you wake up in the

## 39470:00 - 39495:00

morning you walk into the kitchen it's

## 39495:00 - 39570:00

like Alex you didn't sleep well you know

## 39570:00 - 39595:00

then you can imagine integration with

## 39595:00 - 39630:00

some partners that he like okay let's

## 39630:00 - 39685:00

have the conversation um also say hey

## 39685:00 - 39710:00

your day looks pretty packed today you

## 39710:00 - 39740:00

should probably find some time that

## 39740:00 - 39780:00

proactivity is there it's in the system

## 39780:00 - 39805:00

we're using it in a very different way

## 39805:00 - 39830:00

we don't want to be intrusive with it we

## 39830:00 - 39850:00

got to learn from our customers first

## 39850:00 - 39890:00

like how much proactivity do you want I

## 39890:00 - 39930:00

think it's very very important to you

## 39930:00 - 39945:00

know you don't want to jump to that

## 39945:00 - 39985:00

future you you got to be right so yeah

## 39985:00 - 40005:00

it's a good example wake up in the

## 40005:00 - 40035:00

morning and if I need to buy a birthday

## 40035:00 - 40065:00

gift can you just remind me we can

## 40065:00 - 40085:00

create reminders we can create a

## 40085:00 - 40115:00

conversational piece but I don't think a

## 40115:00 - 40140:00

lot of people want Alexa just to wake up

## 40140:00 - 40175:00

and start talking to you no I do think

## 40175:00 - 40210:00

that yeah don't want to be intrusive you

## 40210:00 - 40245:00

got to be really careful it's we got to

## 40245:00 - 40280:00

be so smart about you know we have 10

## 40280:00 - 40320:00

years of lessons this is what's so

## 40320:00 - 40370:00

awesome about it and you know how much

## 40370:00 - 40425:00

privacy matters and and when you want to

## 40425:00 - 40445:00

invoke Alexa to be part of the

## 40445:00 - 40460:00

conversation

## 40460:00 - 40505:00

versus um when you how proactive you

## 40505:00 - 40545:00

want you want it to be and you know we

## 40545:00 - 40570:00

have a balance on it but I think it's a

## 40570:00 - 40615:00

good push she's already proactive in the

## 40615:00 - 40630:00

spirit

## 40630:00 - 40685:00

of um she has a way to if if I if I went

## 40685:00 - 40715:00

out there and said hey I've been looking

## 40715:00 - 40745:00

for this I watched this movie last week

## 40745:00 - 40770:00

what was that song that was playing in

## 40770:00 - 40795:00

that movie okay give it that little

## 40795:00 - 40825:00

information check Prime video what was

## 40825:00 - 40850:00

he watching okay I got it I think you're

## 40850:00 - 40875:00

watching this movie it was this

## 40875:00 - 40915:00

song proactivity also includes do you

## 40915:00 - 40935:00

want me to play that song or you just

## 40935:00 - 40960:00

want the name of it and a lot of times

## 40960:00 - 40980:00

Alexa will say do you want me to play it

## 40980:00 - 41020:00

for you that's a subtle proactive it's

## 41020:00 - 41065:00

not intrusive it's using context you

## 41065:00 - 41090:00

know contextual information some memory

## 41090:00 - 41120:00

some of your history and in the past

## 41120:00 - 41145:00

you've asked me to play it every time so

## 41145:00 - 41180:00

I'm not don't I just ask you to play it

## 41180:00 - 41205:00

I think those are different forms of

## 41205:00 - 41245:00

productivity but our vision includes

## 41245:00 - 41300:00

Alexa being proactive it has to be that

## 41300:00 - 41330:00

we believe the next step customers will

## 41330:00 - 41400:00

ask for is I I want her more not less

## 41400:00 - 41440:00

right and so instead of me thinking oh I

## 41440:00 - 41470:00

should ask a

## 41470:00 - 41490:00

is there a point where Alexa will know

## 41490:00 - 41535:00

to ask me I think that's a real question

## 41535:00 - 41575:00

I don't think that's today I think that

## 41575:00 - 41615:00

is the future um and I think you know

## 41615:00 - 41655:00

back to where you know we're pretty well

## 41655:00 - 41670:00

positioned for that if that's what

## 41670:00 - 41700:00

customers want I think we can do it for

## 41700:00 - 41725:00

them but the I think what this listener

## 41725:00 - 41750:00

was asking is can I just like with

## 41750:00 - 41810:00

natural language say um can't you know

## 41810:00 - 41840:00

take a look at my calendar and oh yeah

## 41840:00 - 41855:00

tell me something okay so that's

## 41855:00 - 41880:00

different that's different sorry I went

## 41880:00 - 41915:00

all the way to my vision but but here's

## 41915:00 - 41940:00

what I'll P pitch back that already

## 41940:00 - 41970:00

happens okay so when you wake up in the

## 41970:00 - 41995:00

morning whoever that listener is here's

## 41995:00 - 42030:00

the answer yes with Alexa Plus or with

## 42030:00 - 42070:00

curent okay sorry not with Alexa right

## 42070:00 - 42090:00

so this there's no there's no way it's

## 42090:00 - 42130:00

going to happen with Alexa okay it's not

## 42130:00 - 42175:00

but with Alexa plus 100% wake up in the

## 42175:00 - 42195:00

morning get your daily brief tell me

## 42195:00 - 42245:00

what's going on and I you know Alexa

## 42245:00 - 42270:00

knows what time you start work will warn

## 42270:00 - 42295:00

you of the traffic you should probably

## 42295:00 - 42320:00

leave by 8:20 if you got to be there by

## 42320:00 - 42365:00

9: today like that level of proactivity

## 42365:00 - 42390:00

that's in the system but you have to

## 42390:00 - 42460:00

engage first okay uh this this idea of

## 42460:00 - 42510:00

of Alexa uh being proactive like it is

## 42510:00 - 42540:00

it's definitely I I see where your

## 42540:00 - 42575:00

caution is coming from because there are

## 42575:00 - 42600:00

these proactive notifications that you

## 42600:00 - 42635:00

get with Alexa I've had to turn them off

## 42635:00 - 42680:00

yeah um yeah we learned from that yeah

## 42680:00 - 42715:00

so okay that's that's good that um

## 42715:00 - 42735:00

there's learning

## 42735:00 - 42780:00

there I I could go with some other Alexa

## 42780:00 - 42800:00

product feedback but I feel let's let's

## 42800:00 - 42835:00

use our time let's stick with Alexa Plus

## 42835:00 - 42855:00

for a minute but if you want to talk

## 42855:00 - 42880:00

about Alexa and we can tell you if Alexa

## 42880:00 - 42920:00

plus has fixed your frustration we too

## 42920:00 - 42940:00

well the one thing I'll say is I've had

## 42940:00 - 42970:00

uh I use it to play alarms and there

## 42970:00 - 42995:00

have been moments where it will play the

## 42995:00 - 43055:00

ad before it will play the song in the

## 43055:00 - 43100:00

morning so um but but that kind of goes

## 43100:00 - 43140:00

to a question that we did also get in

## 43140:00 - 43200:00

the Discord where people talked about um

## 43200:00 - 43250:00

they talked about who whose assistant do

## 43250:00 - 43265:00

you

## 43265:00 - 43315:00

trust and in the back of some people's

## 43315:00 - 43385:00

head there will be this perspective um

## 43385:00 - 43420:00

Amazon is just going to try to sell me

## 43420:00 - 43455:00

something like for instance that example

## 43455:00 - 43485:00

of you didn't sleep very well like all

## 43485:00 - 43515:00

right or it's like a suggestion for

## 43515:00 - 43540:00

sleeping pills coming up I don't know

## 43540:00 - 43565:00

exactly what it is but like how do you

## 43565:00 - 43595:00

get past this perception of like I'm

## 43595:00 - 43620:00

going to get because you do with an

## 43620:00 - 43655:00

assistant you trust it with a lot of

## 43655:00 - 43680:00

data so how do you get to the point

## 43680:00 - 43700:00

where where people are comfortable

## 43700:00 - 43750:00

sharing this data and feeling good about

## 43750:00 - 43780:00

the fact that it won't be used to lead

## 43780:00 - 43800:00

to

## 43800:00 - 43845:00

purchases well I mean first I think even

## 43845:00 - 43865:00

before you get to that part of the

## 43865:00 - 43905:00

question it's just how do you manage a

## 43905:00 - 43935:00

customer's data how do they see

## 43935:00 - 43970:00

transparently what you're doing what

## 43970:00 - 44015:00

they've told the system how do they have

## 44015:00 - 44060:00

control over their data so all of That's

## 44060:00 - 44095:00

So Paramount uh that you have to start

## 44095:00 - 44130:00

there actually it's like one question

## 44130:00 - 44185:00

earlier than that which is do you trust

## 44185:00 - 44210:00

Alexa and the answer has to be yes so

## 44210:00 - 44245:00

we've been building on a foundation of

## 44245:00 - 44275:00

transparency and control there's the

## 44275:00 - 44315:00

Alexa privacy dashboard which one great

## 44315:00 - 44350:00

place to see everything in terms of

## 44350:00 - 44400:00

system settings and your data Etc I just

## 44400:00 - 44430:00

want to make clear all of that carries

## 44430:00 - 44465:00

forward to Alexa plus I think that's

## 44465:00 - 44505:00

sort of the the important point to make

## 44505:00 - 44550:00

at the top um and then if the question

## 44550:00 - 44570:00

is you

## 44570:00 - 44640:00

know is the question boy should I be you

## 44640:00 - 44675:00

know should I be offered a product in a

## 44675:00 - 44710:00

given case where a system thinks I need

## 44710:00 - 44770:00

it um I find that great when it's great

## 44770:00 - 44805:00

it is great when it's great like I found

## 44805:00 - 44835:00

a pair of shoes I I don't even think it

## 44835:00 - 44890:00

was on Amazon uh recently through uh

## 44890:00 - 44920:00

something I was reading online and I've

## 44920:00 - 44975:00

been I've got a orthotic and you know

## 44975:00 - 45010:00

it's great when it's great basically I

## 45010:00 - 45040:00

was referred something they're awesome

## 45040:00 - 45065:00

alas they have a wide toe box I'm not

## 45065:00 - 45090:00

going to sell alas on your show I'm just

## 45090:00 - 45125:00

telling you that I found them because if

## 45125:00 - 45175:00

you're listening we need sponsors it's

## 45175:00 - 45220:00

an arcade is this the camera which camer

## 45220:00 - 45250:00

that's the ultra sponsor yeah P give

## 45250:00 - 45270:00

them a

## 45270:00 - 45300:00

head

## 45300:00 - 45340:00

sponsors Alex needs sponsors it's an

## 45340:00 - 45375:00

Arcane example but the bottom line is

## 45375:00 - 45405:00

like it's great when it's great and why

## 45405:00 - 45435:00

is it great it's contextual it's

## 45435:00 - 45470:00

relevant it's offering me something that

## 45470:00 - 45520:00

I actually need and so Building Systems

## 45520:00 - 45560:00

where you can do that elegantly like

## 45560:00 - 45585:00

customers actually love that we get

## 45585:00 - 45620:00

feedback that that's great it's not what

## 45620:00 - 45655:00

what's terrible is when you get you know

## 45655:00 - 45680:00

inundated with things that are

## 45680:00 - 45720:00

irrelevant to you and so we're building

## 45720:00 - 45760:00

a system that doesn't do that does Alexa

## 45760:00 - 45795:00

need to have a screen I mean p put this

## 45795:00 - 45815:00

to you you're the head of devices at

## 45815:00 - 45855:00

Amazon a lot of the the demos uh that

## 45855:00 - 45880:00

you did at your launch event were with

## 45880:00 - 45915:00

Alexa with the screen again I have like

## 45915:00 - 45955:00

first or second generation echoes in my

## 45955:00 - 45985:00

house might be time to upgrade but you

## 45985:00 - 46010:00

should upgrade like there's a couple of

## 46010:00 - 46045:00

things you're missing one you're missing

## 46045:00 - 46075:00

speed that you could have that you don't

## 46075:00 - 46125:00

have and I think we speed is time for me

## 46125:00 - 46165:00

okay um it's comfort you know it's

## 46165:00 - 46185:00

confidence like there's so much like

## 46185:00 - 46235:00

first yeah I I would always

## 46235:00 - 46265:00

encourage not not just because I want to

## 46265:00 - 46295:00

sell the next device that's not why I

## 46295:00 - 46320:00

just having something modern if your

## 46320:00 - 46350:00

device is N9 years old you you you're

## 46350:00 - 46400:00

missing eight years of tech okay so I'm

## 46400:00 - 46450:00

judging you giving what you do you know

## 46450:00 - 46480:00

and so your feedback is like half her at

## 46480:00 - 46515:00

this point but I would say okay I say

## 46515:00 - 46560:00

that you know jokingly but I go look um

## 46560:00 - 46595:00

you need more you it's better the

## 46595:00 - 46630:00

product's just better as it you know

## 46630:00 - 46655:00

generationally generation over

## 46655:00 - 46685:00

generation always got better now does it

## 46685:00 - 46710:00

need a screen inredible yeah it does

## 46710:00 - 46735:00

does okay it doesn't have to have a

## 46735:00 - 46775:00

screen it's a better experience with a

## 46775:00 - 46830:00

screen okay it really is now let me let

## 46830:00 - 46870:00

me qualify it because you have a screen

## 46870:00 - 46915:00

in your pocket that works with

## 46915:00 - 46960:00

Alexa you have a screen on your desktop

## 46960:00 - 46980:00

that works with

## 46980:00 - 47020:00

Alexa the screen in your home you should

## 47020:00 - 47085:00

have one it's very powerful it's nuanced

## 47085:00 - 47125:00

it's not intrusive the new design is

## 47125:00 - 47165:00

elegant it's soft if that makes sense

## 47165:00 - 47195:00

like where it's what you want in the

## 47195:00 - 47240:00

home something softer um you can get the

## 47240:00 - 47270:00

expression from Alexa from that screen

## 47270:00 - 47300:00

and she brings visual Expressions as as

## 47300:00 - 47340:00

much as anything but but here's the

## 47340:00 - 47375:00

trick it will come with you in your

## 47375:00 - 47420:00

earbuds it'll come on your Alexa frames

## 47420:00 - 47455:00

it'll be in your pocket it will be in

## 47455:00 - 47495:00

your car so you don't always need a

## 47495:00 - 47550:00

screen but in your home I mean the the

## 47550:00 - 47585:00

the command and control the information

## 47585:00 - 47640:00

management what you get off of it it is

## 47640:00 - 47685:00

powerful will it work without a screen

## 47685:00 - 47735:00

absolutely absolutely and it'll be great

## 47735:00 - 47770:00

so need is a relative term I want you to

## 47770:00 - 47810:00

have a screen okay because it the

## 47810:00 - 47855:00

experience is that much better and uh

## 47855:00 - 47880:00

there's a Nuance in it like when we when

## 47880:00 - 47905:00

we start rolling out preview the first

## 47905:00 - 47940:00

customers to get preview will be our

## 47940:00 - 47970:00

screen based customers because it's the

## 47970:00 - 48025:00

best experience okay that simple and so

## 48025:00 - 48050:00

you'll be like I want the preview and

## 48050:00 - 48070:00

I'll I'll

## 48070:00 - 48115:00

say you need a screen get a screen all

## 48115:00 - 48140:00

right maybe two and then I'll light

## 48140:00 - 48165:00

we'll light up all your we'll light up

## 48165:00 - 48190:00

all your Echoes but but you need a

## 48190:00 - 48230:00

screen okay maybe one in the kitchen one

## 48230:00 - 48265:00

in the office you only need one yeah

## 48265:00 - 48285:00

well I mean it's up to you keep the

## 48285:00 - 48315:00

screen out the bedroom at least that's

## 48315:00 - 48345:00

that's my perspective totally like you

## 48345:00 - 48365:00

know the only the only screen I allow in

## 48365:00 - 48405:00

the bedroom is the Kindle that's a cool

## 48405:00 - 48435:00

product but I I'm using mine here you

## 48435:00 - 48465:00

know I just listening to you I by the

## 48465:00 - 48490:00

way I got the alarm in the morning note

## 48490:00 - 48530:00

I get that bug filed like I got you but

## 48530:00 - 48550:00

the but

## 48550:00 - 48605:00

the but the idea that different devices

## 48605:00 - 48660:00

work in different places is real right

## 48660:00 - 48685:00

but I think you need a central Hub right

## 48685:00 - 48735:00

now I think Alexa plus is so

## 48735:00 - 48795:00

Dynamic um and the more you can learn to

## 48795:00 - 48835:00

do the screen will teach you like hey

## 48835:00 - 48870:00

get after it y you saw Daniel's

## 48870:00 - 48890:00

Thumbtack demo which is a little bit

## 48890:00 - 48920:00

even is was more agentic than if you

## 48920:00 - 48980:00

will for us then the GrubHub slash did

## 48980:00 - 49010:00

we do GrubHub or open table last night

## 49010:00 - 49055:00

Open Table gu t with Uber right um but

## 49055:00 - 49095:00

the Thumbtack demo was you know

## 49095:00 - 49130:00

conversation let's I need a repair

## 49130:00 - 49165:00

person well that agent goes out and

## 49165:00 - 49200:00

starts booking it for you on the website

## 49200:00 - 49220:00

and then you need the screen to give you

## 49220:00 - 49260:00

a status like working on it back in a

## 49260:00 - 49305:00

bit don't worry about it okay I think

## 49305:00 - 49330:00

that is uh that's what you want that

## 49330:00 - 49365:00

Ambience for in the background so I

## 49365:00 - 49395:00

think the can't be more clear I don't

## 49395:00 - 49425:00

think I think it'd be great okay I'm I'm

## 49425:00 - 49450:00

sold I'm going to get one all right

## 49450:00 - 49475:00

we're running up on time here I want to

## 49475:00 - 49510:00

give you both a minute to answer uh this

## 49510:00 - 49540:00

question and then we'll head out but

## 49540:00 - 49560:00

it's got to be a minute or your team

## 49560:00 - 49620:00

here will have my head um uh we talked

## 49620:00 - 49660:00

about how uh voice AI might be the

## 49660:00 - 49715:00

future of AI or the Catalyst for these

## 49715:00 - 49740:00

large language models on the show a

## 49740:00 - 49785:00

while back open AI for instance debuted

## 49785:00 - 49845:00

or introduced this advanced form of AI

## 49845:00 - 49895:00

uh called uh in with GPT 40 and you can

## 49895:00 - 49925:00

see the inflection point of chat GPT

## 49925:00 - 49950:00

that the second they announced that bam

## 49950:00 - 49975:00

it goes from 100 million to 300 million

## 49975:00 - 50015:00

users um is voice AI the future of

## 50015:00 - 50050:00

artificial intelligence you want to

## 50050:00 - 50070:00

start and I'll close this out I mean

## 50070:00 - 50095:00

we've believe for a long time that voice

## 50095:00 - 50135:00

is the most natural interface uh we're

## 50135:00 - 50160:00

using it right now we're using it with

## 50160:00 - 50185:00

your listeners we're using it with each

## 50185:00 - 50230:00

other um it's incredibly expressive you

## 50230:00 - 50270:00

can load an unbelievable amount of

## 50270:00 - 50300:00

context and Power in it you can be

## 50300:00 - 50340:00

definite you can be vague you can be

## 50340:00 - 50395:00

nuanced so and it's just we're born with

## 50395:00 - 50435:00

the knowledge of how to use it and it's

## 50435:00 - 50490:00

completely intuitive so I think we do

## 50490:00 - 50525:00

strongly believe that it's one of the

## 50525:00 - 50555:00

best ways to get things done it is not

## 50555:00 - 50590:00

the only way to get things done but I do

## 50590:00 - 50615:00

think it's pushing us it's challenging

## 50615:00 - 50655:00

us to get more and more human more

## 50655:00 - 50685:00

natural and that's why it's always been

## 50685:00 - 50715:00

one of the kind of centerpieces of our

## 50715:00 - 50775:00

vision for Alexa so yes my answer is yes

## 50775:00 - 50795:00

and I think it's really pushing the

## 50795:00 - 50830:00

envelope now okay a minute two Panos I

## 50830:00 - 50865:00

think we're at that time we're this is

## 50865:00 - 50900:00

the inflection point and mentioned it

## 50900:00 - 50930:00

yesterday you know the I believe the

## 50930:00 - 50970:00

vision for Alexa is incredibly ambitious

## 50970:00 - 51005:00

it centers around voice for sure I don't

## 51005:00 - 51030:00

think it ends at voice I think the

## 51030:00 - 51065:00

interaction model needs to be the one

## 51065:00 - 51105:00

that's most natural to you no doubt if

## 51105:00 - 51130:00

you need to touch the screen to complete

## 51130:00 - 51150:00

a task if you need to get to your

## 51150:00 - 51190:00

computer and write the long form I think

## 51190:00 - 51220:00

it's a flow and what the thing you don't

## 51220:00 - 51255:00

want to do is you don't want to block

## 51255:00 - 51280:00

the customer from the interaction that

## 51280:00 - 51315:00

they need to go get something done it's

## 51315:00 - 51330:00

why we're on the phone it's why we're on

## 51330:00 - 51375:00

the PC it's why we're in your glasses

## 51375:00 - 51410:00

it's why we're in your ears and

## 51410:00 - 51435:00

ultimately though the anchoring point of

## 51435:00 - 51470:00

all of it is the voice because it is

## 51470:00 - 51510:00

natural it's innate to all of us the

## 51510:00 - 51545:00

trick is getting to natural conversation

## 51545:00 - 51570:00

the trick is trusting that you can just

## 51570:00 - 51615:00

talk and and realize that as we talk to

## 51615:00 - 51660:00

each other it's pretty sure you can talk

## 51660:00 - 51680:00

that way with Alexa and you're going to

## 51680:00 - 51710:00

find that and I think that is the

## 51710:00 - 51760:00

transformation that's coming I think it

## 51760:00 - 51830:00

finishes you know um the next chapter

## 51830:00 - 51855:00

ends the first chapter and starts the

## 51855:00 - 51900:00

next chapter and leads us to getting so

## 51900:00 - 51920:00

finishing is the wrong word there but

## 51920:00 - 51965:00

getting us to that next that next leap

## 51965:00 - 51995:00

over the next 10 years this is that

## 51995:00 - 52020:00

starting point that technology is

## 52020:00 - 52040:00

enabling it right now and that

## 52040:00 - 52095:00

inflection is happening um and it's

## 52095:00 - 52135:00

compelling so it was a longer way to say

## 52135:00 - 52160:00

yeah it starts with voice but I don't

## 52160:00 - 52205:00

think it ends with voice it never will

## 52205:00 - 52270:00

like we it is also a Nate test you

## 52270:00 - 52320:00

always we as as humans were always going

## 52320:00 - 52345:00

to find the

## 52345:00 - 52400:00

best and easiest path to get something

## 52400:00 - 52450:00

done and we think voice will lead to

## 52450:00 - 52490:00

most of that but not all of it like we

## 52490:00 - 52530:00

don't want to overstate it like we will

## 52530:00 - 52560:00

find the best easiest which means

## 52560:00 - 52600:00

basically the fastest path to completion

## 52600:00 - 52625:00

which is why you need to upgrade your

## 52625:00 - 52675:00

devices and get a screen you with me I

## 52675:00 - 52695:00

told you already I'm buying one all

## 52695:00 - 52720:00

right well get on it man we did sell we

## 52720:00 - 52745:00

sold at least one device here in New

## 52745:00 - 52780:00

York good news while we're here our goal

## 52780:00 - 52825:00

this week was not to sell devices but

## 52825:00 - 52870:00

we'll do that soon very efficient and SC

## 52870:00 - 52895:00

we're killing it now we have a new

## 52895:00 - 52945:00

sponsor we uh we sold a device this is

## 52945:00 - 52985:00

we're we're killing it well look Panos

## 52985:00 - 53015:00

and Daniel um I want to just say while

## 53015:00 - 53040:00

we're recording that I don't take it for

## 53040:00 - 53075:00

granted to be speaking uh on record with

## 53075:00 - 53125:00

Amazon um it's always great for me to be

## 53125:00 - 53160:00

able to hear what you're doing and be

## 53160:00 - 53190:00

able to ask these questions and I'm sure

## 53190:00 - 53220:00

for listeners uh it'll be great as well

## 53220:00 - 53240:00

so thank you both for being here and

## 53240:00 - 53265:00

thanks for coming you so much really

## 53265:00 - 53290:00

great awesome well thank you everyone

## 53290:00 - 53310:00

for listening and we'll see you next

## 53310:00+

time on big technology podcast

