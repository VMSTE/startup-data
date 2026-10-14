---
source: https://www.youtube.com/watch?v=5noIKN8t69U
title: "Alexandr Wang: Building Scale AI, Transforming Work With Agents &
  Competing With China"
author: Y Combinator
date: 2025-06-18
views: 346831
description: >-
  Alexandr Wang started Scale AI to help machine learning teams label data
  faster.


  It started as a simple API for human labor, but behind the scenes, he was
  tackling a much bigger problem: how to turn messy, real-world data into
  something AI could learn from. Today, that early idea powers a
  multi-hundred-million-dollar engine behind America's AI infrastructure—fueling
  everything from Fortune 500 workflows to real-time military planning. 


  Just last week, Meta agreed to invest over $14 billion in Scale, valuing the
  company at $29 billion.


  Alexandr joined us on the Lightcone to share how Scale evolved from a scrappy
  YC startup into the backbone of some of the world's most advanced AI systems,
  how he thinks about competition with Chinese AI labs, and what it takes to
  build infrastructure that shapes the frontier.


  Apply to Y Combinator: https://ycombinator.com/apply

  Work at a startup: https://workatastartup.com


  Chapters (Powered by https://ChapterMe.co):

  00:00 Intro

  01:15 Alexandr’s early days at YC

  07:25 Dialing in on what worked

  10:24 Model improvements, evals

  19:18 The techno optimist view of work

  27:47 The turning points for Scale AI

  37:37 Agentic workflows 

  41:55 “Humanity’s Last Exam”

  47:48 U.S. vs China in AI and hard tech

  56:57 How to be hardcore
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:45:15.464Z
---

# Alexandr Wang: Building Scale AI, Transforming Work With Agents & Competing With China

## 00:00 - 30:00

Since we recorded this Lite Cone episode

## 30:00 - 90:00

with Scale AI CEO Alexander Wang, Meta

## 90:00 - 165:00

has agreed to invest over $14 billion in

## 165:00 - 205:00

scale, valuing the company at $29

## 205:00 - 250:00

billion. Alex has also announced he will

## 250:00 - 290:00

lead Meta's new AI super intelligence

## 290:00 - 330:00

lab. Our conversation you're about to

## 330:00 - 370:00

hear covers the history leading up to

## 370:00 - 410:00

this investment. From scale's early days

## 410:00 - 460:00

at YC to its integral role in the

## 460:00 - 500:00

training of foundational models. Let's

## 500:00 - 545:00

get to it. The AI industry really

## 545:00 - 615:00

continues to suffer from a lack of uh

## 615:00 - 670:00

very hard evals and very hard tests that

## 670:00 - 725:00

show really like the frontier of model

## 725:00 - 780:00

capabilities. The biggest thing is you

## 780:00 - 825:00

just have to really really really care.

## 825:00 - 845:00

When you interview people or when you

## 845:00 - 865:00

interact with people, you can tell

## 865:00 - 895:00

people who are just sort of like phone

## 895:00 - 925:00

it in versus people who sort of like

## 925:00 - 965:00

hang on to their work. It's like the so

## 965:00 - 1010:00

incredibly monumental and forceful and

## 1010:00 - 1045:00

important to them that they they do

## 1045:00 - 1080:00

great work. Very exciting time to to see

## 1080:00 - 1115:00

the how the frontier of human knowledge

## 1115:00 - 1145:00

expands.

## 1145:00 - 1250:00

[Music]

## 1250:00 - 1300:00

Welcome to another episode of the Light

## 1300:00 - 1350:00

Cone. Today we have a real treat. It's

## 1350:00 - 1405:00

Alexander Wang of Scale AI. Jared, you

## 1405:00 - 1450:00

worked with uh Alexander way back in the

## 1450:00 - 1480:00

beginning actually. Uh what was that

## 1480:00 - 1510:00

like? What year was it? Put us in the

## 1510:00 - 1545:00

spot. Yeah, Alex. I mean, most of what

## 1545:00 - 1575:00

we want to talk about today is like what

## 1575:00 - 1610:00

Scale is doing now because like the the

## 1610:00 - 1640:00

current stuff is like so so awesome and

## 1640:00 - 1670:00

so interesting since Scale got started

## 1670:00 - 1705:00

at YC. I thought it just seemed

## 1705:00 - 1725:00

appropriate to start all the way at the

## 1725:00 - 1765:00

start. And um you it's funny uh Diane

## 1765:00 - 1815:00

and I were at MIT last month talking to

## 1815:00 - 1835:00

college students and like of all the

## 1835:00 - 1875:00

founders, the one that they like most

## 1875:00 - 1910:00

look up to and like want to emulate is

## 1910:00 - 1940:00

actually you. Like everybody wants to be

## 1940:00 - 1965:00

the next Alexander Wankers. Everybody

## 1965:00 - 1990:00

knows the story of how you like dropped

## 1990:00 - 2030:00

out of MIT and and ended up starting

## 2030:00 - 2050:00

scale, but they don't know the real

## 2050:00 - 2090:00

story. And so I thought it'd be cool to

## 2090:00 - 2110:00

go back to the beginning and just talk

## 2110:00 - 2130:00

about the real story of how you ended up

## 2130:00 - 2170:00

dropping out of MIT and starting scale.

## 2170:00 - 2210:00

So before I went to MIT, I worked at um

## 2210:00 - 2265:00

Quora for a year. And so this is 2015 to

## 2265:00 - 2315:00

2016 or no sorry 2014 to 2015 was when I

## 2315:00 - 2345:00

worked as a software engineer and this

## 2345:00 - 2365:00

was already at a point in the market

## 2365:00 - 2400:00

where ML engineers as they were called

## 2400:00 - 2435:00

or like machine learning engineers uh

## 2435:00 - 2475:00

made more than software engineers. So

## 2475:00 - 2500:00

that was already like the market state

## 2500:00 - 2530:00

at that point. I went to these summer

## 2530:00 - 2580:00

camps um that were that were organized

## 2580:00 - 2630:00

by um by rationalists the rationality

## 2630:00 - 2665:00

community in San Francisco. So um and

## 2665:00 - 2690:00

they were for precocious teams but they

## 2690:00 - 2760:00

were organized by um uh many people who

## 2760:00 - 2790:00

have become pivotal in the AI industry.

## 2790:00 - 2825:00

So one of the organizers is this guy

## 2825:00 - 2885:00

Paul Cristiano who um used to uh who's

## 2885:00 - 2930:00

the inventor of RHF actually and now he

## 2930:00 - 2960:00

run or he's a research director at the

## 2960:00 - 2980:00

US AI safety institute. He was at

## 2980:00 - 3010:00

opening for a long time. Um Greg

## 3010:00 - 3045:00

Brockman came and gave a speech at one

## 3045:00 - 3075:00

point. Eleazar Yudkowski came and gave a

## 3075:00 - 3100:00

speech at one point and actually I was

## 3100:00 - 3130:00

very like when I was I don't know must

## 3130:00 - 3195:00

have been uh 16 I was exposed to this

## 3195:00 - 3230:00

concept that like potentially the most

## 3230:00 - 3260:00

important thing to work on in my

## 3260:00 - 3305:00

lifetime was AI and AI safety. So

## 3305:00 - 3325:00

something I was exposed to very early

## 3325:00 - 3345:00

very early on. So then when I went to

## 3345:00 - 3405:00

MIT I was started MIT when I was 18. I

## 3405:00 - 3460:00

like studied AI quite deeply. That was

## 3460:00 - 3495:00

most of what I did in the sort of day

## 3495:00 - 3560:00

job. and then um uh kind of got antsy

## 3560:00 - 3600:00

applied to YC and then the idea was kind

## 3600:00 - 3625:00

of like okay how could initially was

## 3625:00 - 3670:00

like okay where can you apply um sort of

## 3670:00 - 3745:00

like AI to things and this was um in the

## 3745:00 - 3785:00

era of chat bots which is like crazy to

## 3785:00 - 3820:00

think about actually um that there was

## 3820:00 - 3865:00

like this like mini chatbot bubble boom

## 3865:00 - 3935:00

yeah yeah yeah 100% in uh in 2016 um

## 3935:00 - 3985:00

which is uh which was I guess spurred by

## 3985:00 - 4025:00

magic right? Or or some of these apps

## 4025:00 - 4060:00

and and uh Facebook had a big vision

## 4060:00 - 4080:00

around chat bots. And anyway, there's

## 4080:00 - 4110:00

this little mini chatbot boom. So, the

## 4110:00 - 4155:00

initial thing that we wanted to work on

## 4155:00 - 4220:00

uh and um was was chat bots for doctors,

## 4220:00 - 4245:00

right?

## 4245:00 - 4285:00

Which is like a funny idea because do

## 4285:00 - 4315:00

you guys know anything about doctors?

## 4315:00 - 4355:00

Yeah. No, not at all. um like basically

## 4355:00 - 4390:00

no I it was just sort of like oh doctors

## 4390:00 - 4440:00

are a thing that sound expensive and so

## 4440:00 - 4465:00

and I think it was like I think it's

## 4465:00 - 4490:00

like indicative of like I mean I don't

## 4490:00 - 4510:00

know you guys see this all the time but

## 4510:00 - 4550:00

I feel like most of the times young

## 4550:00 - 4600:00

founders like first 10 ideas are like

## 4600:00 - 4620:00

always first of all they're very

## 4620:00 - 4640:00

mimemetic so they're probably like

## 4640:00 - 4660:00

there's a lot of like the same ideas

## 4660:00 - 4685:00

over there's like a dating app there's

## 4685:00 - 4725:00

like some something for like you know

## 4725:00 - 4750:00

social life you know there's the same

## 4750:00 - 4805:00

ideas um and then I think that like I

## 4805:00 - 4830:00

think young people have a very poor

## 4830:00 - 4860:00

sense sense of alpha like what are what

## 4860:00 - 4880:00

are the things that they're actually

## 4880:00 - 4910:00

like going to be uniquely positioned to

## 4910:00 - 4945:00

do and I think you know most young

## 4945:00 - 4965:00

people don't have a sense of self so

## 4965:00 - 5000:00

it's you know it's not clear so when we

## 5000:00 - 5045:00

were in YC we were roommates with uh

## 5045:00 - 5125:00

with um with another YC uh company and

## 5125:00 - 5160:00

we were sort of like um we were sort of

## 5160:00 - 5200:00

observing this like this like chatbot

## 5200:00 - 5235:00

boom ahead of you know that was

## 5235:00 - 5265:00

happening at the time um and but it was

## 5265:00 - 5315:00

very clear that like um chat bots if you

## 5315:00 - 5340:00

wanted to build them, and this is funny

## 5340:00 - 5365:00

to say in retrospect, required lots of

## 5365:00 - 5410:00

data um and required lots of like human

## 5410:00 - 5445:00

elbow grease um to be able to get them

## 5445:00 - 5485:00

to work effectively. And so like just

## 5485:00 - 5520:00

like kind of off the cuff at one point

## 5520:00 - 5570:00

was like, oh, like what if you just did

## 5570:00 - 5600:00

that? What if you just did the data and

## 5600:00 - 5635:00

the the like language data and the the

## 5635:00 - 5675:00

human data so to speak for the chatbot

## 5675:00 - 5705:00

companies? We were also very lost, by

## 5705:00 - 5730:00

the way. I think you probably remember

## 5730:00 - 5785:00

we we were we were quite lost mid batch.

## 5785:00 - 5835:00

um uh and like many YC companies I think

## 5835:00 - 5885:00

and so then we um switched to this like

## 5885:00 - 5910:00

concept I think the you know the initial

## 5910:00 - 5950:00

idea was like API for um for human tasks

## 5950:00 - 5985:00

or something along those lines and uh

## 5985:00 - 6030:00

and one night I was just like trolling

## 6030:00 - 6070:00

around for domains scaleappi.com was

## 6070:00 - 6115:00

available and then we just bought it we

## 6115:00 - 6155:00

launched it I think a week later we

## 6155:00 - 6185:00

product hunt yeah I remember the the

## 6185:00 - 6225:00

product hunt page is still live I was

## 6225:00 - 6265:00

reading it last night and I remembered

## 6265:00 - 6295:00

the tagline line. It was an API for

## 6295:00 - 6325:00

human labor. Like that that that that's

## 6325:00 - 6355:00

my recollection of sort of like the like

## 6355:00 - 6380:00

distilled insight that you had was like

## 6380:00 - 6405:00

what if there is an a what if you could

## 6405:00 - 6440:00

call a human with like an API? Yeah. And

## 6440:00 - 6475:00

that was I mean I think it was like 3

## 6475:00 - 6515:00

days for us to put up the landing page.

## 6515:00 - 6545:00

It launched on product hunt. I think

## 6545:00 - 6605:00

this idea captured some amount of

## 6605:00 - 6660:00

imagination of the like of the startup

## 6660:00 - 6685:00

community at the time because it was

## 6685:00 - 6730:00

sort of like this weird form of futurism

## 6730:00 - 6770:00

where you have like humans delegated

## 6770:00 - 6810:00

like APIs delegate to humans in this in

## 6810:00 - 6830:00

this interesting way. It's like an

## 6830:00 - 6870:00

inversion of the Yes. Yeah. Humans doing

## 6870:00 - 6890:00

work for the machines instead of the

## 6890:00 - 6920:00

other way around. Yeah. Yeah. Yeah. It's

## 6920:00 - 6960:00

funny because the the initial phase, you

## 6960:00 - 6990:00

know, we sort of we just worked with all

## 6990:00 - 7020:00

these engineers who reached out to us

## 7020:00 - 7060:00

from um from that product hunt which was

## 7060:00 - 7095:00

a real grab of use cases, but then that

## 7095:00 - 7120:00

was enough for us to raise money at the

## 7120:00 - 7155:00

time and like you know uh and to get

## 7155:00 - 7205:00

going and then a few months after that

## 7205:00 - 7240:00

uh we it became clear that like

## 7240:00 - 7295:00

self-driving cars was actually the first

## 7295:00 - 7320:00

major application that we needed to

## 7320:00 - 7370:00

focus on. And so there were many uh very

## 7370:00 - 7395:00

big decisions I would say in the first

## 7395:00 - 7420:00

like year or so of the company. One

## 7420:00 - 7460:00

thing that was curious is at that point

## 7460:00 - 7490:00

there were other solutions that were

## 7490:00 - 7520:00

already the game in town like mechanical

## 7520:00 - 7545:00

turk from Amazon was sort of the thing

## 7545:00 - 7575:00

that people were using but you ended up

## 7575:00 - 7610:00

capturing this whole other set of people

## 7610:00 - 7635:00

that didn't know about it and you had a

## 7635:00 - 7715:00

way better API and you kind of won.

## 7715:00 - 7735:00

Yeah. It was not clear at that point

## 7735:00 - 7765:00

because you probably were compared a lot

## 7765:00 - 7795:00

with mechanical turd. Yeah. So,

## 7795:00 - 7815:00

Mechanical Turk was definitely the sort

## 7815:00 - 7875:00

of like um the concept in most people's

## 7875:00 - 7905:00

mind at the time. I mean, it was just it

## 7905:00 - 7915:00

was kind of one of these things where I

## 7915:00 - 7930:00

think a lot of people had heard about

## 7930:00 - 7960:00

it, but anyone who had used it knew it

## 7960:00 - 7990:00

was just awful.

## 7990:00 - 8015:00

And so, it's like whenever you're in a

## 8015:00 - 8045:00

space and that's kind of the like that's

## 8045:00 - 8070:00

like the thing. It's like people mention

## 8070:00 - 8100:00

a thing, but it sucks, that's usually

## 8100:00 - 8145:00

like a pretty good sign. Um, and so that

## 8145:00 - 8170:00

was that was enough to give us like

## 8170:00 - 8195:00

early confidence. But then I think the

## 8195:00 - 8245:00

thing that like really I would say the

## 8245:00 - 8290:00

the um the thing that was as actually

## 8290:00 - 8325:00

fundamental to the success of the the

## 8325:00 - 8360:00

company was actually focusing on this

## 8360:00 - 8390:00

like on this like seemingly very narrow

## 8390:00 - 8430:00

problem of of self-driving cars. I think

## 8430:00 - 8485:00

that um you know I remember very early

## 8485:00 - 8520:00

on when it was maybe like six months

## 8520:00 - 8560:00

after we were out of YC basically um

## 8560:00 - 8590:00

there was another YC company Cruz that

## 8590:00 - 8615:00

that had reached out to us on our

## 8615:00 - 8655:00

website and sort of like in the blink of

## 8655:00 - 8685:00

an eye they became our largest customer

## 8685:00 - 8725:00

and they found you just from your launch

## 8725:00 - 8770:00

or yeah just yeah I think maybe even

## 8770:00 - 8790:00

Google like I it's not even totally

## 8790:00 - 8820:00

obvious but just yeah vaguely from our

## 8820:00 - 8845:00

launch and vaguely it was actually an

## 8845:00 - 8880:00

XYC founder that uh was working at

## 8880:00 - 8910:00

Cruise that reached out to us so maybe

## 8910:00 - 8980:00

some YC mumbo jumbo.

## 8980:00 - 9025:00

We're a ketti. Yeah. Uh, who knows? The

## 9025:00 - 9060:00

world works in mysterious ways, but and

## 9060:00 - 9090:00

so they grew very very large. So then

## 9090:00 - 9120:00

early on we made this decision and I

## 9120:00 - 9160:00

remember we we we um went to our lead

## 9160:00 - 9190:00

investor at the time and you know we had

## 9190:00 - 9220:00

this conversation. It's like hey

## 9220:00 - 9240:00

actually we think we should probably

## 9240:00 - 9280:00

just focus on this self-driving thing.

## 9280:00 - 9295:00

You know it was actually a very

## 9295:00 - 9320:00

interesting conversation because the

## 9320:00 - 9350:00

reaction was like oh that's just like

## 9350:00 - 9390:00

obviously way too small a market. um

## 9390:00 - 9415:00

then like you you know you're never

## 9415:00 - 9440:00

going to build like a gigantic business

## 9440:00 - 9495:00

that way. Um and we were like we think

## 9495:00 - 9540:00

it's probably a much bigger market than

## 9540:00 - 9580:00

than you think it is because there's

## 9580:00 - 9610:00

like you know all these self-driving

## 9610:00 - 9630:00

companies are getting crazy amounts of

## 9630:00 - 9665:00

funding and the automotive companies are

## 9665:00 - 9700:00

doing huge programs in self-driving and

## 9700:00 - 9730:00

it clearly is the future. Like it feels

## 9730:00 - 9765:00

like something that that um that should

## 9765:00 - 9795:00

exist and so we're like if we focus on

## 9795:00 - 9820:00

it we think we can build like build the

## 9820:00 - 9845:00

business much more quickly. And it's

## 9845:00 - 9865:00

funny looking back because both things

## 9865:00 - 9905:00

are true. It is both true that it

## 9905:00 - 9925:00

enabled us to build the business to be

## 9925:00 - 9965:00

to get to scale pretty very quickly and

## 9965:00 - 10005:00

it is also true that that was not a big

## 10005:00 - 10045:00

enough market to sustain a gigantic

## 10045:00 - 10080:00

business. The story of scale in many

## 10080:00 - 10115:00

ways is like this progression of like

## 10115:00 - 10150:00

how do you continue you know AI is this

## 10150:00 - 10185:00

incredibly dynamic space. Um, lots of

## 10185:00 - 10220:00

things are constantly changing and um, a

## 10220:00 - 10255:00

lot of I think what um, what we pride

## 10255:00 - 10295:00

ourselves on at the company is how we've

## 10295:00 - 10335:00

been able to um, continue building on

## 10335:00 - 10375:00

and and um, contributing to this very

## 10375:00 - 10415:00

fastmoving industry. When did you uh,

## 10415:00 - 10450:00

become much more aware of the scaling

## 10450:00 - 10500:00

laws because you know uh, one of the

## 10500:00 - 10530:00

interesting facts that sort of emerged

## 10530:00 - 10565:00

is that uh, you're a little bit the

## 10565:00 - 10625:00

Jensen Hang of data. I think that in

## 10625:00 - 10655:00

self-driving

## 10655:00 - 10700:00

um scaling laws were not really a thing.

## 10700:00 - 10735:00

Um because and the fundamental the the

## 10735:00 - 10760:00

biggest reason actually was that like

## 10760:00 - 10775:00

one of the biggest problems in

## 10775:00 - 10800:00

self-driving is that your whole

## 10800:00 - 10835:00

algorithm needs to run on the car and so

## 10835:00 - 10860:00

you're very constrained by the amount of

## 10860:00 - 10905:00

compute you have access to and is

## 10905:00 - 10950:00

available to you. So like a lot of the

## 10950:00 - 10980:00

engineers and a lot of the companies

## 10980:00 - 11000:00

working on self-driving never really

## 11000:00 - 11025:00

thought about scaling laws. They were

## 11025:00 - 11045:00

just all thinking about like, okay, how

## 11045:00 - 11080:00

do you keep grinding these algorithms to

## 11080:00 - 11100:00

be better and better better that are

## 11100:00 - 11135:00

like small enough to fit onto these um

## 11135:00 - 11170:00

onto these cars? But then we started

## 11170:00 - 11220:00

working with OpenAI in 2019. This was

## 11220:00 - 11295:00

like GPD2 era. Um and I would say like

## 11295:00 - 11320:00

GPT1

## 11320:00 - 11380:00

GPT was sort of like this curiosity.

## 11380:00 - 11430:00

GPD2. Um, I remember OpenAI like they

## 11430:00 - 11455:00

would have a booth at these like large

## 11455:00 - 11485:00

AI conferences and they would like, you

## 11485:00 - 11520:00

know, their demo would be to allow

## 11520:00 - 11565:00

researchers to like talk to GPD2 and it

## 11565:00 - 11595:00

was like

## 11595:00 - 11625:00

mildly like it was it wasn't like

## 11625:00 - 11640:00

particularly impressive, but it was like

## 11640:00 - 11670:00

kind of cool. is like kind of this thing

## 11670:00 - 11735:00

and then um I think by GPG3

## 11735:00 - 11770:00

uh it was sort of this like that's when

## 11770:00 - 11820:00

the scaling loss clearly um you know

## 11820:00 - 11865:00

felt very real and that was I mean I

## 11865:00 - 11925:00

think GPD3 was 2020 um so which is

## 11925:00 - 11950:00

actually like long before before the

## 11950:00 - 11990:00

world caught on to what was happening

## 11990:00 - 12030:00

did did you know as early as 2020 did

## 12030:00 - 12060:00

did you have a strong inkling that this

## 12060:00 - 12090:00

was really going to be like the next big

## 12090:00 - 12125:00

chapter of scale or not until chat GPT

## 12125:00 - 12180:00

took off was was 35 or was it four? I

## 12180:00 - 12230:00

think that like um in 2020 I think it

## 12230:00 - 12275:00

was clear that scaling laws were going

## 12275:00 - 12320:00

to be a big thing, but it was still not

## 12320:00 - 12360:00

totally obvious. you I remember this

## 12360:00 - 12400:00

like interaction, you know, I I got

## 12400:00 - 12460:00

early access to GPD3 and then it was

## 12460:00 - 12495:00

like in the playground and then I I was

## 12495:00 - 12515:00

like playing with it with a friend of

## 12515:00 - 12550:00

mine and uh I I told the friend of mine,

## 12550:00 - 12580:00

"Oh, you can like talk to this model."

## 12580:00 - 12650:00

And during the conversation, um uh my

## 12650:00 - 12685:00

friend got like visibly frustrated and

## 12685:00 - 12730:00

angry at the AI, but in a way that

## 12730:00 - 12750:00

wasn't just like, "Oh, this is a dumb

## 12750:00 - 12775:00

like toy." It was like it was in a way

## 12775:00 - 12800:00

that was like somewhat personal. And

## 12800:00 - 12830:00

that's when I was I realized like whoa,

## 12830:00 - 12850:00

this is like somehow qualitatively

## 12850:00 - 12880:00

different from anything that had existed

## 12880:00 - 12910:00

before. I feel like it was passing the

## 12910:00 - 12950:00

touring test at that point. Kind of. It

## 12950:00 - 12980:00

was like semblances. Yeah, semblance. It

## 12980:00 - 13015:00

was like sort of like the the the

## 13015:00 - 13050:00

glimpses of it potentially passing the

## 13050:00 - 13080:00

touring test, right? But I think the

## 13080:00 - 13110:00

thing that really

## 13110:00 - 13165:00

um caused the recognition of I would say

## 13165:00 - 13185:00

generative AI, which is still even the

## 13185:00 - 13225:00

term in some ways, it was really Dolly I

## 13225:00 - 13280:00

think that that um that convinced um

## 13280:00 - 13315:00

that convinced everyone. But I think I

## 13315:00 - 13365:00

think my my personal um journey was like

## 13365:00 - 13400:00

GBD3

## 13400:00 - 13440:00

like was like highly interesting and

## 13440:00 - 13480:00

then and so it was like one of many bets

## 13480:00 - 13550:00

at the company and then in 2022

## 13550:00 - 13600:00

over the course of Dolly and and then um

## 13600:00 - 13645:00

and then later chatbt and you know um

## 13645:00 - 13685:00

GP4 etc. and we worked with open eye on

## 13685:00 - 13705:00

instruct GBT which is kind of the

## 13705:00 - 13735:00

precursor to chat GBT. it became very

## 13735:00 - 13760:00

obvious that that was like the at the

## 13760:00 - 13785:00

farm moment for the for the company and

## 13785:00 - 13810:00

for frankly the world. That's when we

## 13810:00 - 13845:00

saw it as well with the big shift in

## 13845:00 - 13885:00

companies because it was that 3.5 moment

## 13885:00 - 13930:00

release end of uh 2022 and we started

## 13930:00 - 13955:00

seeing a bunch of companies and smart

## 13955:00 - 14000:00

people changing directions and pivoting

## 14000:00 - 14050:00

their companies in 2023 and that was

## 14050:00 - 14085:00

that moment this dynamic that you

## 14085:00 - 14125:00

referenced which is kind of the you know

## 14125:00 - 14150:00

scales the NVIDIA for data kind of

## 14150:00 - 14235:00

thing. Um I think that became quite

## 14235:00 - 14315:00

obvious. Um I would say GPD4 really was

## 14315:00 - 14350:00

the moment where it was like it was like

## 14350:00 - 14395:00

wow this is like like scaling laws are

## 14395:00 - 14425:00

very real. The need for data will

## 14425:00 - 14490:00

basically you know grow to consume you

## 14490:00 - 14535:00

know all available information and and

## 14535:00 - 14575:00

um and knowledge on that humans have.

## 14575:00 - 14615:00

And so um it was like wow this is this

## 14615:00 - 14650:00

is like this like astronomically large

## 14650:00 - 14690:00

opportunity. Yeah for seemed like the

## 14690:00 - 14725:00

first time it was something that you

## 14725:00 - 14755:00

could uh get to not hallucinate

## 14755:00 - 14785:00

basically ever you could actually have a

## 14785:00 - 14840:00

zero uh hallucination experience in

## 14840:00 - 14875:00

limited domains and which is we're still

## 14875:00 - 14910:00

sort of in that regime even at this

## 14910:00 - 14935:00

point. You know, the classic view is

## 14935:00 - 14970:00

that if it's hallucinating, you're not

## 14970:00 - 15005:00

giving it the correct data in the prompt

## 15005:00 - 15060:00

or context or uh you're trying to do too

## 15060:00 - 15095:00

much in one step. Yeah. I mean, I think

## 15095:00 - 15130:00

I think like the reasoning paradigm is

## 15130:00 - 15165:00

is is has a lot of lags and it's

## 15165:00 - 15205:00

actually been interesting this last era

## 15205:00 - 15275:00

of the of model improvement because um

## 15275:00 - 15305:00

uh the gains are not really coming from

## 15305:00 - 15355:00

pre-training um which is so so we're

## 15355:00 - 15390:00

like moving on to a new scaling curve of

## 15390:00 - 15425:00

of reasoning and reinforcement learning

## 15425:00 - 15470:00

but it's it's like shockingly effective

## 15470:00 - 15525:00

um and and I think that you know it's

## 15525:00 - 15570:00

the the analogies between like AI and

## 15570:00 - 15595:00

and Mors law are pretty clear which is

## 15595:00 - 15615:00

like you know you'll get on different

## 15615:00 - 15650:00

like technical curves but like if you

## 15650:00 - 15675:00

zoom way out it'll just be feel like

## 15675:00 - 15705:00

this like smooth improvement of models.

## 15705:00 - 15725:00

One of the things that uh has been

## 15725:00 - 15765:00

popping up with some of the like really

## 15765:00 - 15800:00

big well-known rappers is they're

## 15800:00 - 15835:00

getting access to full parameter

## 15835:00 - 15875:00

finetunes of the base models especially

## 15875:00 - 15920:00

the frontier base closed source models.

## 15920:00 - 15945:00

Is that like a big part of your business

## 15945:00 - 15980:00

or you know something that people are

## 15980:00 - 16010:00

sort of coming to you for just like

## 16010:00 - 16045:00

these verticalized full parameter

## 16045:00 - 16085:00

fine-tuned like data sets? Yeah, I think

## 16085:00 - 16135:00

this is going to be a like blueprint for

## 16135:00 - 16160:00

the future, right? So right now I mean

## 16160:00 - 16210:00

like the total number of large scale

## 16210:00 - 16235:00

parameter fine tuned or reinforcement

## 16235:00 - 16260:00

fine-tuned models is like still pretty

## 16260:00 - 16295:00

small but if you kind of think about it

## 16295:00 - 16360:00

like that like one version of the future

## 16360:00 - 16435:00

is that every firm's core IP is actually

## 16435:00 - 16480:00

their specialized model or their own

## 16480:00 - 16515:00

fine-tuned model and just in the same

## 16515:00 - 16565:00

way that like you know today you would

## 16565:00 - 16600:00

generally think that the co the the uh

## 16600:00 - 16630:00

IP of most tech companies is their

## 16630:00 - 16650:00

codebase

## 16650:00 - 16685:00

um in the future you would generally

## 16685:00 - 16715:00

think that their their their specialized

## 16715:00 - 16755:00

IP might be the model that powers all of

## 16755:00 - 16805:00

their all their internal um workflows.

## 16805:00 - 16830:00

And what are the special things they can

## 16830:00 - 16865:00

add on top? Well, they can add on um

## 16865:00 - 16910:00

data and environments that are somehow

## 16910:00 - 16950:00

specific very very specific to the

## 16950:00 - 16990:00

day-to-day problems or information or

## 16990:00 - 17015:00

challenges or business problems that

## 17015:00 - 17060:00

they see um on a day-to-day level. And

## 17060:00 - 17110:00

that's the kind of like really gritty

## 17110:00 - 17155:00

real world information that you know

## 17155:00 - 17175:00

nobody else will have because nobody

## 17175:00 - 17200:00

else is like doing the same the exact

## 17200:00 - 17230:00

same business motion as them. There's a

## 17230:00 - 17265:00

lot of weird tension in that though. Um

## 17265:00 - 17295:00

I remember uh friends of ours from one

## 17295:00 - 17335:00

of the top model companies came by and

## 17335:00 - 17370:00

they were like hey do you think YC and

## 17370:00 - 17425:00

YC companies would give us their evals

## 17425:00 - 17460:00

so we could train against it? And we

## 17460:00 - 17485:00

were like no dude what are you talking

## 17485:00 - 17515:00

about? Why why would they do that?

## 17515:00 - 17545:00

Because that's like their moat. And then

## 17545:00 - 17575:00

I guess now that based on this

## 17575:00 - 17610:00

conversation, it's actually I mean eval

## 17610:00 - 17640:00

are pretty important as a part of RL

## 17640:00 - 17680:00

cycles. And then even the eval are not

## 17680:00 - 17710:00

really uh the valuable part. The

## 17710:00 - 17740:00

valuable part is actually the like

## 17740:00 - 17770:00

properly fine-tuned model for your data

## 17770:00 - 17805:00

set and your set of you know sort of

## 17805:00 - 17835:00

problems. Yeah, it's like these Lego

## 17835:00 - 17855:00

blocks, right? If you have the data and

## 17855:00 - 17885:00

you have the environments and then you

## 17885:00 - 17925:00

have the you have you know a base model,

## 17925:00 - 17955:00

you like you know can stack those on top

## 17955:00 - 17980:00

of each other get get a fine tuned model

## 17980:00 - 18010:00

and obviously the eval are important.

## 18010:00 - 18040:00

This is some of the tension and this is

## 18040:00 - 18070:00

basically you know in a nutshell the

## 18070:00 - 18125:00

sort of like um does AGI become a Borg

## 18125:00 - 18145:00

that just sort of like swallows the

## 18145:00 - 18175:00

whole economy in like you know has one

## 18175:00 - 18205:00

firm or do you still have a specialized

## 18205:00 - 18245:00

economy? My belief generally speaking is

## 18245:00 - 18290:00

that you you still do have a specialized

## 18290:00 - 18340:00

economy like the like these models are

## 18340:00 - 18390:00

platforms but the like like alpha in the

## 18390:00 - 18440:00

modern world will be determined by you

## 18440:00 - 18480:00

know to what degree you're able to sort

## 18480:00 - 18505:00

of like encapsulate your business

## 18505:00 - 18545:00

problems into data sets or environments

## 18545:00 - 18585:00

that are then conducive towards building

## 18585:00 - 18620:00

like you know differentiated models or

## 18620:00 - 18645:00

differentiated AI capabilities. Yeah,

## 18645:00 - 18675:00

that's why asking for eval was so crazy

## 18675:00 - 18700:00

to me because it's like okay you get the

## 18700:00 - 18750:00

evals the base model is way better and

## 18750:00 - 18775:00

then not you know now all your

## 18775:00 - 18820:00

competitors have exactly uh the same

## 18820:00 - 18855:00

thing that used to be your advantage. I

## 18855:00 - 18905:00

think we will undergo a process in AI

## 18905:00 - 18960:00

where we learn what the bright lines

## 18960:00 - 18990:00

are, right? I mean, I think that like

## 18990:00 - 19035:00

it's like very obvious and intuitive to

## 19035:00 - 19060:00

tech companies that they should not give

## 19060:00 - 19090:00

away their codebase and they should not

## 19090:00 - 19110:00

give away their database. Like they

## 19110:00 - 19125:00

should not give away their data, they

## 19125:00 - 19145:00

should not give away their codebase. The

## 19145:00 - 19190:00

analoges of that in a you know highly AI

## 19190:00 - 19225:00

fueled economy I think will identify

## 19225:00 - 19270:00

over time but are yeah the evals your

## 19270:00 - 19305:00

data your environments etc. I think you

## 19305:00 - 19345:00

have a very uh techno optimistic view of

## 19345:00 - 19400:00

what the future is going to be with how

## 19400:00 - 19430:00

jobs are going to be shaped. Can you

## 19430:00 - 19450:00

talk more about that? Because I think

## 19450:00 - 19485:00

you hinted at it before. It's going to

## 19485:00 - 19515:00

be more specialized. It's not that all

## 19515:00 - 19560:00

these jobs are going to go away, right?

## 19560:00 - 19600:00

First off, it's undeniably true that

## 19600:00 - 19655:00

we're we're uh at the beginning of an

## 19655:00 - 19710:00

era of like a new a new way of working

## 19710:00 - 19735:00

like like you know this there's this

## 19735:00 - 19755:00

term that people have used a long time

## 19755:00 - 19805:00

which is like the future of work. Well

## 19805:00 - 19830:00

uh we are like entering the future of

## 19830:00 - 19865:00

work or the certainly the next era and

## 19865:00 - 19905:00

so work fundamentally will change but I

## 19905:00 - 19970:00

do think um humans own the future and we

## 19970:00 - 20015:00

we are we are like uh we have a lot of

## 20015:00 - 20050:00

agency actually and a lot of a lot of

## 20050:00 - 20085:00

choice in how this sort of like

## 20085:00 - 20125:00

reformatting of of work or how the

## 20125:00 - 20150:00

reformatting of sort of like workflows

## 20150:00 - 20175:00

ends up playing out. You know, I think

## 20175:00 - 20220:00

you kind of see this play out in uh in

## 20220:00 - 20250:00

coding right now. And I think coding in

## 20250:00 - 20305:00

some ways is is really the sort of like

## 20305:00 - 20355:00

um case study for other fields and and

## 20355:00 - 20395:00

other you know other areas of work where

## 20395:00 - 20430:00

sort of the the initial phase is this

## 20430:00 - 20485:00

sort of like assistant style thing where

## 20485:00 - 20520:00

um you know you're kind of doing your

## 20520:00 - 20545:00

work and then the models are kind of

## 20545:00 - 20565:00

like assisting you a little bit here and

## 20565:00 - 20605:00

there and then you go to a you know the

## 20605:00 - 20635:00

sort of like cursor agent mode kind of

## 20635:00 - 20675:00

thing where you're you're like um

## 20675:00 - 20720:00

synchronously asking the the models to

## 20720:00 - 20745:00

like carry out these workflows and

## 20745:00 - 20765:00

you're sort of like you're you're

## 20765:00 - 20800:00

managing like one agent kind of or

## 20800:00 - 20825:00

you're sort of like you're kind of like

## 20825:00 - 20865:00

pair programming with a single agent and

## 20865:00 - 20900:00

then and then now with like codecs or

## 20900:00 - 20925:00

other systems like it's it's very clear

## 20925:00 - 20955:00

the paradigm is like oh you have this

## 20955:00 - 20985:00

like you have this like swarm of agents

## 20985:00 - 21010:00

that you're going to deploy on like all

## 21010:00 - 21030:00

these various tasks and you're just

## 21030:00 - 21070:00

going to like sort of like you know dep

## 21070:00 - 21100:00

like um give all these tasks and you'll

## 21100:00 - 21140:00

have this sort of like um this this

## 21140:00 - 21170:00

cohort of of agents that are sort of

## 21170:00 - 21200:00

like you know doing this work that you

## 21200:00 - 21225:00

you think is appropriate.

## 21225:00 - 21295:00

And that last job um uh has a has a

## 21295:00 - 21320:00

semantic meaning in the in the current

## 21320:00 - 21345:00

workforce. It's a manager. You know,

## 21345:00 - 21375:00

you're basically managing this sort of

## 21375:00 - 21435:00

like this set of agents to do um actual

## 21435:00 - 21470:00

work. And so and and I think that like

## 21470:00 - 21520:00

AGI or you know AGI or doomers or

## 21520:00 - 21550:00

whatnot like they take this view that

## 21550:00 - 21585:00

like oh even this job of like managing

## 21585:00 - 21605:00

the agents will just be done by the

## 21605:00 - 21640:00

agents. So like humans will be taken out

## 21640:00 - 21680:00

of the of the process entirely. But our

## 21680:00 - 21720:00

belief, my personal belief is that you

## 21720:00 - 21780:00

know this is um management is very

## 21780:00 - 21820:00

complicated. Um management is also like

## 21820:00 - 21850:00

more about like what's the vision that

## 21850:00 - 21875:00

you have and what's the sort of like

## 21875:00 - 21910:00

what's the like end result you're aiming

## 21910:00 - 21945:00

towards and those will be fundamentally

## 21945:00 - 21990:00

I think like you know we have a human

## 21990:00 - 22025:00

demand and human desired driven economy.

## 22025:00 - 22060:00

So those will be driven by humans. And

## 22060:00 - 22105:00

so I think the terminal state of the

## 22105:00 - 22150:00

economy is just is largecale humans

## 22150:00 - 22185:00

manage agents in a nutshell. I have a

## 22185:00 - 22225:00

funny story where um founder friend of

## 22225:00 - 22275:00

mine is trying to promote uh one of his

## 22275:00 - 22305:00

you know junior employees but they're

## 22305:00 - 22335:00

really really smart and they're working

## 22335:00 - 22375:00

on the agent infrastructure and then he

## 22375:00 - 22415:00

was like hey do you want to like you

## 22415:00 - 22435:00

know I'm looking for someone who could

## 22435:00 - 22465:00

step into management. You've never

## 22465:00 - 22495:00

managed people before. or do you you

## 22495:00 - 22535:00

know if we hired some people uh under

## 22535:00 - 22575:00

you like how would you feel about that

## 22575:00 - 22625:00

and uh this you know uh mid20some really

## 22625:00 - 22665:00

smart you know sort of do he's just like

## 22665:00 - 22700:00

he's an engineer and he's like why would

## 22700:00 - 22740:00

I do that like just give me like more

## 22740:00 - 22780:00

compute like you know the model like

## 22780:00 - 22805:00

look at what just happened to the model

## 22805:00 - 22845:00

literally like last month and you know I

## 22845:00 - 22865:00

didn't have to do anything it just

## 22865:00 - 22885:00

started doing things that it couldn't do

## 22885:00 - 22920:00

a month ago why would I want to manage

## 22920:00 - 22955:00

people like just give me like I will

## 22955:00 - 22985:00

just manage more agents for and it's

## 22985:00 - 23020:00

fine. Okay. So, what are the unique

## 23020:00 - 23070:00

things that that um that humans will do

## 23070:00 - 23100:00

over time? I mean, I think this like

## 23100:00 - 23140:00

this like element of vision um is very

## 23140:00 - 23175:00

important. This element of like kind of

## 23175:00 - 23230:00

like debugging or sort of like um fixing

## 23230:00 - 23285:00

when things go wrong. Like most of a

## 23285:00 - 23335:00

manager's job, speaking as a manager, is

## 23335:00 - 23365:00

is just like putting out fires, dealing

## 23365:00 - 23395:00

with problems, dealing with like like

## 23395:00 - 23420:00

issues that come up. Like I think

## 23420:00 - 23465:00

intuitively, you know, I the idealistic

## 23465:00 - 23495:00

manager job seems like this very cushy

## 23495:00 - 23520:00

job because you're like, "Oh yeah, all

## 23520:00 - 23545:00

the other people do all the work and I'm

## 23545:00 - 23570:00

just sort of like I just vaguely

## 23570:00 - 23600:00

supervise and then the reality is

## 23600:00 - 23625:00

obviously like highly chaotic." I think

## 23625:00 - 23655:00

people often jump to this like, you

## 23655:00 - 23685:00

know, extreme reality where it's like,

## 23685:00 - 23725:00

oh yeah, these like, you know, you're

## 23725:00 - 23745:00

just going to manage the agents and

## 23745:00 - 23765:00

you're going to sort of like live this

## 23765:00 - 23800:00

like, you know, kind of Victorian life

## 23800:00 - 23825:00

where all your problems are solved. But

## 23825:00 - 23850:00

but no, I think it's still going to be

## 23850:00 - 23870:00

pretty complicated like getting agents

## 23870:00 - 23895:00

to like coordinate well with one another

## 23895:00 - 23930:00

and like coordinating the workflows and

## 23930:00 - 23955:00

and and debugging the issues that come

## 23955:00 - 23975:00

up like these are still complicated

## 23975:00 - 24015:00

issues and you know having seen what

## 24015:00 - 24050:00

happened in self-driving which was more

## 24050:00 - 24080:00

or less that like you know it's easy to

## 24080:00 - 24130:00

get to 90% very very hard to get to 99%

## 24130:00 - 24160:00

I think that like something similar will

## 24160:00 - 24185:00

happen as with large scale agent

## 24185:00 - 24225:00

deployments and that like you know final

## 24225:00 - 24265:00

10% of accuracy will be like you know

## 24265:00 - 24295:00

will require a lot of work. Yeah. Even

## 24295:00 - 24330:00

for uh self-driving cars right now,

## 24330:00 - 24365:00

there's the remote assist for all these

## 24365:00 - 24400:00

super etch case. So there's still a

## 24400:00 - 24430:00

human at the end managing the car. Yeah.

## 24430:00 - 24485:00

And the ratio, by the way, I mean um the

## 24485:00 - 24500:00

companies don't publish them, but I

## 24500:00 - 24540:00

think the ratio is something like five

## 24540:00 - 24600:00

cars to to one teley operator um or or

## 24600:00 - 24630:00

maybe even less than maybe three cars

## 24630:00 - 24685:00

per teley operator. So um the ratio is

## 24685:00 - 24730:00

like you know much lower than people

## 24730:00 - 24765:00

think. I think that like humans are much

## 24765:00 - 24795:00

more involved even in self-driving cars

## 24795:00 - 24830:00

than I think most people appreciate. I

## 24830:00 - 24860:00

mean, which if you put it in that

## 24860:00 - 24885:00

perspective, I think it's still very

## 24885:00 - 24915:00

optimistic. It's just the output of

## 24915:00 - 24945:00

getting rides instead of doing in

## 24945:00 - 24970:00

today's world, if you're a Uber driver,

## 24970:00 - 24995:00

you just do one car. In this world, you

## 24995:00 - 25025:00

can do five cars, right? Well, you have

## 25025:00 - 25055:00

to believe for this like for an

## 25055:00 - 25080:00

optimistic version of the future where,

## 25080:00 - 25110:00

you know, unemployment is still low,

## 25110:00 - 25145:00

etc. You just have to believe that

## 25145:00 - 25180:00

humans are like almost insatiable in

## 25180:00 - 25215:00

their desire and their demand. um and

## 25215:00 - 25260:00

that like you know prices will go down,

## 25260:00 - 25310:00

things will become you know uh the the

## 25310:00 - 25335:00

economy will become more efficient and

## 25335:00 - 25365:00

we'll just like want more. And I think

## 25365:00 - 25400:00

this has been a pretty reliable trend

## 25400:00 - 25435:00

for like the history of humanity is that

## 25435:00 - 25480:00

like you know um we have somewhat

## 25480:00 - 25535:00

insatiable demand. Um, and so I have I

## 25535:00 - 25560:00

have like conviction that like you know

## 25560:00 - 25580:00

the economy can kind of get as efficient

## 25580:00 - 25620:00

as it needs or as it like can get like

## 25620:00 - 25660:00

hyper hyperefficient and then human

## 25660:00 - 25685:00

demand will just like continue to sort

## 25685:00 - 25710:00

of like fill the bucket. Yeah. In the

## 25710:00 - 25755:00

20th century uh you know when you said

## 25755:00 - 25805:00

computer maybe early 20th century people

## 25805:00 - 25845:00

didn't think of like a computer as it is

## 25845:00 - 25885:00

today. They thought of a human being

## 25885:00 - 25915:00

that would sit in front of a punch card

## 25915:00 - 25950:00

tabulator and that was like what a

## 25950:00 - 25985:00

computer was doing. I mean title. It was

## 25985:00 - 26030:00

literally that was a real person's job.

## 26030:00 - 26065:00

And then of course now today it's like

## 26065:00 - 26090:00

where are all the computers? Well,

## 26090:00 - 26120:00

they're actually real computers now. I

## 26120:00 - 26145:00

don't know. It's that was the Apollo

## 26145:00 - 26180:00

mission. It was a bunch of uh people

## 26180:00 - 26200:00

just crunching numbers with the

## 26200:00 - 26240:00

trajectories of uh of the Apollo and

## 26240:00 - 26285:00

that was it because the uh computer that

## 26285:00 - 26325:00

went on the uh rocket is actually was a

## 26325:00 - 26360:00

microcontroller with I think only like

## 26360:00 - 26395:00

single digit hertz. It was like very

## 26395:00 - 26425:00

tiny amount of computations. It was just

## 26425:00 - 26460:00

humans doing it. Totally. and and even

## 26460:00 - 26500:00

this like I mean I think the concept of

## 26500:00 - 26530:00

being a programmer is somewhat is like

## 26530:00 - 26575:00

highly esoteric um in the sense that

## 26575:00 - 26605:00

like oh you're like writing the

## 26605:00 - 26645:00

instructions for these like machines to

## 26645:00 - 26700:00

just like you know just continue do

## 26700:00 - 26725:00

repetitively and in some ways it's like

## 26725:00 - 26770:00

the leverage boost that all humans will

## 26770:00 - 26795:00

get is like similar to the leverage

## 26795:00 - 26820:00

boost that like programmers have had

## 26820:00 - 26855:00

historically for a long time I think a

## 26855:00 - 26880:00

like a lot of people in Silicon Valley

## 26880:00 - 26920:00

say this like the the the closest thing

## 26920:00 - 26975:00

to alchemy in our world preai, let's

## 26975:00 - 27010:00

say, is programming because you sort of

## 27010:00 - 27045:00

like you can do something that uh

## 27045:00 - 27080:00

creates like like an infinite there's

## 27080:00 - 27120:00

these infinite replicas of whatever you

## 27120:00 - 27150:00

build and they can sort of like run an

## 27150:00 - 27205:00

infinite number of times and um and I

## 27205:00 - 27240:00

think the entire human workforce will

## 27240:00 - 27305:00

soon see that kind that large of a

## 27305:00 - 27345:00

leverage boost which is extremely

## 27345:00 - 27365:00

exciting because I think that like

## 27365:00 - 27430:00

programmers are are are um have like

## 27430:00 - 27465:00

benefited Ed over the past few decades

## 27465:00 - 27495:00

from this like unique perch where they

## 27495:00 - 27550:00

they have like you know one 10x or 100x

## 27550:00 - 27590:00

engineer can like can build something

## 27590:00 - 27630:00

like absolutely incredible and like very

## 27630:00 - 27670:00

very valuable and like very um uh

## 27670:00 - 27710:00

shockingly productive and all of a

## 27710:00 - 27750:00

sudden I think like like humans in all

## 27750:00 - 27770:00

trades I think will like gain this like

## 27770:00 - 27805:00

level of leverage. Alex, I'm curious to

## 27805:00 - 27830:00

return to a point that you made earlier

## 27830:00 - 27860:00

about like how scale has kept

## 27860:00 - 27890:00

reinventing itself. If you had to like

## 27890:00 - 27925:00

describe the arc of scale like what's

## 27925:00 - 28000:00

what's what's the story and what were

## 28000:00 - 28025:00

the turning points? Our initial business

## 28025:00 - 28065:00

was all around um you know producing

## 28065:00 - 28110:00

data um you know generating data for

## 28110:00 - 28140:00

various AI applications and primarily

## 28140:00 - 28165:00

self-driving car companies right for for

## 28165:00 - 28185:00

the early years it was really like

## 28185:00 - 28205:00

you're saying you're really focused on

## 28205:00 - 28225:00

on that. Yeah for the first like three

## 28225:00 - 28255:00

years fully focused on that. One of the

## 28255:00 - 28285:00

properties of focusing on that business

## 28285:00 - 28325:00

of building that business is over time

## 28325:00 - 28375:00

you know we had this like obligation to

## 28375:00 - 28420:00

really like get ahead of most of the

## 28420:00 - 28450:00

waves of AI if that makes sense because

## 28450:00 - 28500:00

you know for AI to be successful in any

## 28500:00 - 28555:00

vertical area it needed data and so like

## 28555:00 - 28605:00

our demand for our our products would

## 28605:00 - 28640:00

preede a lot of times the actual sort of

## 28640:00 - 28675:00

like evolution of AI into those

## 28675:00 - 28715:00

industries. So, you know, as an example,

## 28715:00 - 28740:00

we started working with OpenAI on

## 28740:00 - 28785:00

language models in 2019. Um, we started

## 28785:00 - 28830:00

working with the DoD on government AI

## 28830:00 - 28865:00

applications um and defense AI

## 28865:00 - 28905:00

applications in 2020. This is like long

## 28905:00 - 28940:00

before I think the you know recent sort

## 28940:00 - 29015:00

of like dronefueled um you know AI uh AI

## 29015:00 - 29040:00

craze in the in the Department of

## 29040:00 - 29065:00

Defense. we started working with

## 29065:00 - 29105:00

enterprises long before um there was

## 29105:00 - 29135:00

sort of like this uh you know the recent

## 29135:00 - 29165:00

sort of like larger waves around uh

## 29165:00 - 29210:00

enterprise AI implementation. So um

## 29210:00 - 29275:00

almost uh uh sort of systemically or or

## 29275:00 - 29325:00

intrinsically we've had to uh basically

## 29325:00 - 29375:00

build ahead of the waves of AI. I think

## 29375:00 - 29405:00

this actually quite similar to Nvidia.

## 29405:00 - 29430:00

you know, whenever like Jensen gives his

## 29430:00 - 29475:00

annual presentations about, you know,

## 29475:00 - 29505:00

Nvidia and its two trends outlook, like

## 29505:00 - 29550:00

he always is so ahead of the trends. Um,

## 29550:00 - 29580:00

and that's because he has to get there

## 29580:00 - 29605:00

on the trend before the trend can even

## 29605:00 - 29665:00

happen. That's I think been one um one

## 29665:00 - 29690:00

way in which our businesses continue to

## 29690:00 - 29720:00

adapt because AI is like this, you know,

## 29720:00 - 29755:00

it's this this like it's the fastest

## 29755:00 - 29790:00

moving industry I think ever um in the

## 29790:00 - 29820:00

history of the world. And so you know

## 29820:00 - 29875:00

that each each turn um each evolution uh

## 29875:00 - 29910:00

has been has moved incredibly quickly.

## 29910:00 - 29940:00

The other thing that that happened late

## 29940:00 - 30000:00

2021 early 2022 um we started working on

## 30000:00 - 30035:00

um applications and so we started

## 30035:00 - 30085:00

building out uh AI based applications

## 30085:00 - 30135:00

and now u more much more so uh agentic

## 30135:00 - 30170:00

workflows and agentic applications um

## 30170:00 - 30200:00

for enterprises and government

## 30200:00 - 30235:00

customers. And this was an interesting

## 30235:00 - 30260:00

evolution of our business because

## 30260:00 - 30290:00

because historically like our core

## 30290:00 - 30320:00

business is highly operational. You

## 30320:00 - 30350:00

know, we build this like data foundry.

## 30350:00 - 30385:00

We have all these processes to produce

## 30385:00 - 30420:00

data. Um it's a very operational process

## 30420:00 - 30445:00

that involves like lots of humans and

## 30445:00 - 30485:00

human experts to be able to produce data

## 30485:00 - 30515:00

with quality control systems in place.

## 30515:00 - 30570:00

That highly operational business um and

## 30570:00 - 30590:00

the success of that business is what

## 30590:00 - 30635:00

created the momentum for us to you know

## 30635:00 - 30665:00

sort of dream about building an

## 30665:00 - 30700:00

applications business. when we went into

## 30700:00 - 30725:00

it,

## 30725:00 - 30775:00

uh, I had studied other businesses that

## 30775:00 - 30860:00

had basically successfully um, added on

## 30860:00 - 30895:00

very different businesses and what are

## 30895:00 - 30945:00

sort of like the unique traits or or why

## 30945:00 - 30965:00

do some of those work and one of them

## 30965:00 - 31005:00

that is probably the most interesting

## 31005:00 - 31040:00

um, I think is like the most singular in

## 31040:00 - 31100:00

modern uh, modern business history is

## 31100:00 - 31155:00

um, Amazon building AWS. You know, if in

## 31155:00 - 31205:00

2000 you had written a short story that

## 31205:00 - 31240:00

said that like, you know, this large

## 31240:00 - 31275:00

online retailer would build this like

## 31275:00 - 31320:00

largecale cloud computing rent to server

## 31320:00 - 31350:00

business. Like it would seem like

## 31350:00 - 31380:00

nonsensical. I remember when they

## 31380:00 - 31445:00

launched AWS in 2006, Amazon stock went

## 31445:00 - 31480:00

down because all the analysts thought it

## 31480:00 - 31505:00

was such a terrible idea. It never been

## 31505:00 - 31535:00

done before. It just like it doesn't

## 31535:00 - 31560:00

seem related at all to their core

## 31560:00 - 31600:00

business. um it has it's like this like

## 31600:00 - 31635:00

weird thing but the sort of like wisdom

## 31635:00 - 31670:00

of that was I think twofold. I think

## 31670:00 - 31730:00

like first um and uh from talking to

## 31730:00 - 31765:00

people who are like there at the out you

## 31765:00 - 31790:00

know the sort of like the genesis moment

## 31790:00 - 31835:00

of this business like one thing probably

## 31835:00 - 31860:00

the most important thing was that they

## 31860:00 - 31910:00

had conviction that that the the sort of

## 31910:00 - 31935:00

like underlying business model of AWS

## 31935:00 - 31965:00

would basically be this like this like

## 31965:00 - 32000:00

infinitely large and growing market like

## 32000:00 - 32030:00

that market would would literally grow

## 32030:00 - 32065:00

forever. there would be like this like

## 32065:00 - 32090:00

exponential of the amount of compute

## 32090:00 - 32115:00

that needed built up needed to be built

## 32115:00 - 32165:00

up in the world and um if you did that

## 32165:00 - 32190:00

there was like sufficient cost of you

## 32190:00 - 32215:00

know cost advantages from economies of

## 32215:00 - 32250:00

scale I think like startups you know you

## 32250:00 - 32280:00

kind of like

## 32280:00 - 32320:00

um uh you kind of have to like switch

## 32320:00 - 32345:00

modes at a certain point where like

## 32345:00 - 32385:00

early on you're trying to go for very

## 32385:00 - 32410:00

very narrow markets like almost the

## 32410:00 - 32440:00

narrowest markets you can and then

## 32440:00 - 32465:00

you're just trying to like gain momentum

## 32465:00 - 32485:00

and then sort of like slowly grow out

## 32485:00 - 32535:00

from those hyper narrow markets and then

## 32535:00 - 32570:00

um at some point you if you like have

## 32570:00 - 32600:00

ambitions to be a hundred billion dollar

## 32600:00 - 32625:00

company or more then you have to sort of

## 32625:00 - 32660:00

like switch gears and say where are the

## 32660:00 - 32695:00

infinite markets um and how do you build

## 32695:00 - 32740:00

towards those infinite markets and so um

## 32740:00 - 32770:00

this was sort of like uh the moment

## 32770:00 - 32805:00

where we realized that and and the

## 32805:00 - 32835:00

simple realization was that every

## 32835:00 - 32865:00

business and every organization was just

## 32865:00 - 32890:00

going to have to reformat their entire

## 32890:00 - 32950:00

businesses um with AIdriven technology

## 32950:00 - 32990:00

um and now obviously like agent driven

## 32990:00 - 33025:00

technology and that would just be like

## 33025:00 - 33055:00

Over time that would swallow the entire

## 33055:00 - 33095:00

economy and so it was like another one

## 33095:00 - 33120:00

of these like okay that's an infinite

## 33120:00 - 33150:00

business to build out AI applications

## 33150:00 - 33190:00

and AI deployments for large enterprises

## 33190:00 - 33215:00

and governments. I think a lot of people

## 33215:00 - 33240:00

don't realize that you guys are in the

## 33240:00 - 33265:00

middle of this transformation. They

## 33265:00 - 33290:00

still think of scale as the data

## 33290:00 - 33330:00

labeling company but like if you fast

## 33330:00 - 33385:00

forward 10 years do you think most of

## 33385:00 - 33440:00

scale will actually be the agent

## 33440:00 - 33470:00

business? Yeah, it's it's growing much

## 33470:00 - 33500:00

faster at this point. And I think it it

## 33500:00 - 33545:00

it's an infinite market. So the crappy

## 33545:00 - 33565:00

thing about most markets is that they

## 33565:00 - 33605:00

have like a pretty shallow S-curve. Um

## 33605:00 - 33630:00

but then you know you look at

## 33630:00 - 33665:00

hyperscalers or like you know these like

## 33665:00 - 33695:00

mega cap tech companies and they just

## 33695:00 - 33725:00

have like these like ridiculously large

## 33725:00 - 33755:00

markets. So you really want to get into

## 33755:00 - 33785:00

these these these like um infinite

## 33785:00 - 33825:00

markets. So our strategy so far has been

## 33825:00 - 33880:00

to focus on building use cases for you

## 33880:00 - 33905:00

know focus on a small number of

## 33905:00 - 33945:00

customers and um and be quite selective.

## 33945:00 - 33975:00

So we work with you know the number one

## 33975:00 - 33995:00

pharma company in the world the number

## 33995:00 - 34025:00

one telco in the world the number one uh

## 34025:00 - 34060:00

bank the number one um healthcare

## 34060:00 - 34100:00

provider um and we work a lot with the

## 34100:00 - 34125:00

US government you know the department

## 34125:00 - 34150:00

department of defense and and other

## 34150:00 - 34200:00

government agencies and um the whole

## 34200:00 - 34220:00

thing is like how do we take a very

## 34220:00 - 34265:00

focused approach towards building um

## 34265:00 - 34315:00

stuff that resemble you know real

## 34315:00 - 34345:00

differentiated AI capabilities and all

## 34345:00 - 34375:00

this I think sounds somewhat tright but

## 34375:00 - 34440:00

but um we have this multiund million

## 34440:00 - 34460:00

business in building all these

## 34460:00 - 34485:00

applications. By my account, I think

## 34485:00 - 34525:00

it's it's one of the largest AI

## 34525:00 - 34555:00

application businesses um in the

## 34555:00 - 34575:00

industry. Certainly what our investors

## 34575:00 - 34620:00

tell us and it's fueled by our

## 34620:00 - 34645:00

differentiation in the data business

## 34645:00 - 34710:00

because our belief fundamentally is that

## 34710:00 - 34745:00

um kind of what we talked about before

## 34745:00 - 34785:00

the the end state for every enterprise

## 34785:00 - 34850:00

or every organization is um some form of

## 34850:00 - 34900:00

specialization um imbued to them by

## 34900:00 - 34935:00

their own data. Our day jobs

## 34935:00 - 34980:00

historically have been producing highly

## 34980:00 - 35020:00

differentiated data for you know these

## 35020:00 - 35045:00

like largecale model builders in the

## 35045:00 - 35085:00

world and then we can apply that wisdom

## 35085:00 - 35105:00

and that capability and those

## 35105:00 - 35135:00

operational capabilities towards

## 35135:00 - 35160:00

enterprises and their unique problem

## 35160:00 - 35205:00

sets and um and give them specialized

## 35205:00 - 35235:00

applications. Honestly like it kind of

## 35235:00 - 35280:00

sounds like palent here at the like most

## 35280:00 - 35310:00

zoomed out level if you sort of like

## 35310:00 - 35345:00

squint and that you're a technology

## 35345:00 - 35370:00

provider. We're like a technology

## 35370:00 - 35420:00

provider to like the most, you know,

## 35420:00 - 35445:00

some of the largest organizations in the

## 35445:00 - 35485:00

world um with a focus on data. Yeah. Um

## 35485:00 - 35515:00

and I think the key difference is like,

## 35515:00 - 35570:00

you know, Palunteer um has built a real

## 35570:00 - 35620:00

focus around these data ontologies and

## 35620:00 - 35665:00

um and really solving this like messy

## 35665:00 - 35690:00

like data integration problem for

## 35690:00 - 35730:00

enterprises. Um and then our whole

## 35730:00 - 35770:00

viewpoint is like what is the like most

## 35770:00 - 35805:00

strategic data that will enable

## 35805:00 - 35840:00

differentiation for your AI strategy and

## 35840:00 - 35890:00

how do we like generate or harness that

## 35890:00 - 35920:00

data from within your enterprise towards

## 35920:00 - 35955:00

developing that. I guess you will end up

## 35955:00 - 35995:00

being pretty big competitors in another

## 35995:00 - 36030:00

5 10 years but for now like it's

## 36030:00 - 36050:00

basically so green field honestly. I

## 36050:00 - 36075:00

mean I think it's an infinitely large

## 36075:00 - 36100:00

market the other so you might not ever

## 36100:00 - 36130:00

meet actually which is interesting.

## 36130:00 - 36160:00

Yeah. Yeah. I I think in practice now we

## 36160:00 - 36210:00

actually like frankly we work we're more

## 36210:00 - 36240:00

partnered with Palunteer than than

## 36240:00 - 36280:00

competitive with them. Yeah. Um and uh

## 36280:00 - 36300:00

well that's because the problems at

## 36300:00 - 36330:00

these giant organizations are actually

## 36330:00 - 36375:00

so massive and intractable that they'd

## 36375:00 - 36400:00

throw up their hands. It's like they

## 36400:00 - 36430:00

have no shot at ever hiring people who

## 36430:00 - 36470:00

could possibly solve the problem. Uh but

## 36470:00 - 36500:00

a company like Scale or a company like

## 36500:00 - 36545:00

Palunteer can actually hire kind of the

## 36545:00 - 36565:00

same kind of people who would apply to

## 36565:00 - 36605:00

YC actually. It's kind of like there's

## 36605:00 - 36630:00

this Yeah. I don't know the the through

## 36630:00 - 36660:00

line in my head right now is realizing

## 36660:00 - 36705:00

like you know there's plenty of capital

## 36705:00 - 36765:00

and then the limiting agent is actually

## 36765:00 - 36830:00

really great technical smart people who

## 36830:00 - 36880:00

uh are optimistic and actually work

## 36880:00 - 36920:00

really hard. There's like not enough of

## 36920:00 - 36945:00

those people. That's true for the world.

## 36945:00 - 36970:00

And by the way, I think one of the cool

## 36970:00 - 37020:00

things about um agents as we were

## 37020:00 - 37040:00

talking about before is that like all of

## 37040:00 - 37075:00

a sudden those people get near infinite

## 37075:00 - 37120:00

leverage. So, um I think we're going to

## 37120:00 - 37155:00

I think that bottleneck gets exploded

## 37155:00 - 37195:00

now hopefully um due to due to AI.

## 37195:00 - 37235:00

Again, I I think you know just like how

## 37235:00 - 37280:00

in cloud AWS is the largest by far, but

## 37280:00 - 37305:00

there's so many other cloud providers

## 37305:00 - 37345:00

that actually are all at like like it's

## 37345:00 - 37370:00

not a winner take all kind of business

## 37370:00 - 37400:00

per se and it doesn't have to be. Yeah.

## 37400:00 - 37440:00

Exactly. And and and I think that um

## 37440:00 - 37475:00

it's just too big of a market to even be

## 37475:00 - 37500:00

close to winner takes all. like I just

## 37500:00 - 37535:00

there's no single organization that

## 37535:00 - 37575:00

could have the organi um operational

## 37575:00 - 37610:00

breadth to be able to to swallow the

## 37610:00 - 37640:00

whole market. Talking about uh

## 37640:00 - 37680:00

operations, you clearly are living in

## 37680:00 - 37725:00

the future which is super cool. I'm sure

## 37725:00 - 37775:00

you're running scale with all these

## 37775:00 - 37815:00

agents and tools already to make it very

## 37815:00 - 37840:00

efficient. Could you share some of the

## 37840:00 - 37870:00

things that you're doing internally as a

## 37870:00 - 37905:00

company and agents you're adopting so

## 37905:00 - 37935:00

you can do more with less people? You

## 37935:00 - 38000:00

know, we saw this early because uh when

## 38000:00 - 38045:00

when the model developers were starting

## 38045:00 - 38080:00

to develop agents and starting to

## 38080:00 - 38105:00

develop using reinforcement learning

## 38105:00 - 38145:00

like actual you know like reasoning

## 38145:00 - 38175:00

models where the the models could

## 38175:00 - 38215:00

actually like really do end toend

## 38215:00 - 38265:00

workflows. We were uh responsible for

## 38265:00 - 38300:00

producing a lot of the data sets that

## 38300:00 - 38350:00

enabled um the agents to get there and

## 38350:00 - 38390:00

then we saw just like how effective that

## 38390:00 - 38415:00

that training process is. I think that

## 38415:00 - 38445:00

like the efficacy of reinforcement

## 38445:00 - 38500:00

learning for um for agent deployments is

## 38500:00 - 38555:00

like is pretty insane. So then once we

## 38555:00 - 38585:00

realize that we realize like okay if you

## 38585:00 - 38645:00

can actually like you know turn um

## 38645:00 - 38715:00

existing human-driven workflows into

## 38715:00 - 38760:00

environments and and data for

## 38760:00 - 38810:00

reinforcement learning. Um then you have

## 38810:00 - 38855:00

this ability to convert these like human

## 38855:00 - 38895:00

workflows into human workflows um

## 38895:00 - 38915:00

especially ones where you're like okay

## 38915:00 - 38945:00

with some level of fault faultiness and

## 38945:00 - 38975:00

and okay with a certain level of

## 38975:00 - 39015:00

reliability you can convert those into

## 39015:00 - 39045:00

um into agentic workflows. So there's

## 39045:00 - 39095:00

all sorts of like you know agent

## 39095:00 - 39140:00

workflows that that happen in our hiring

## 39140:00 - 39195:00

processes and happen um in our quality

## 39195:00 - 39220:00

control processes and happen to sort of

## 39220:00 - 39255:00

just like automate away certain like

## 39255:00 - 39300:00

data analyses um and data processes as

## 39300:00 - 39325:00

well as like various like sales

## 39325:00 - 39360:00

reporting like it's sort of like

## 39360:00 - 39405:00

embedded at you know every major org of

## 39405:00 - 39430:00

the company. Um and the whole thing is

## 39430:00 - 39475:00

like um it's just like mindset like can

## 39475:00 - 39510:00

you identify these like very repetitive

## 39510:00 - 39540:00

human workflows and basically like

## 39540:00 - 39560:00

undergo this process where you convert

## 39560:00 - 39585:00

that into data sets that enable you to

## 39585:00 - 39620:00

build automation tools. What do these

## 39620:00 - 39655:00

data sets actually look like? I mean for

## 39655:00 - 39695:00

browser use is like is it an environment

## 39695:00 - 39740:00

and then you know here's a video of a

## 39740:00 - 39770:00

human being going through this process

## 39770:00 - 39805:00

of like filling out this form and decide

## 39805:00 - 39855:00

like yes no on this uh drop down or

## 39855:00 - 39875:00

something. I mean you know what's a

## 39875:00 - 39910:00

concrete example just for the audience?

## 39910:00 - 39940:00

One of the processes that we go through

## 39940:00 - 39985:00

is like you know you you um you'll take

## 39985:00 - 40040:00

a sort of like full packet of a from a

## 40040:00 - 40060:00

candidate and you'll like want to

## 40060:00 - 40105:00

distill that into like you know a brief

## 40105:00 - 40145:00

of some sort that sort of like gives all

## 40145:00 - 40170:00

the salient details about that candidate

## 40170:00 - 40200:00

for like decision by a sort of like

## 40200:00 - 40245:00

broader committee. Um and these kinds of

## 40245:00 - 40280:00

cases you know broadly speaking like

## 40280:00 - 40320:00

deep research plus+ kind of things are

## 40320:00 - 40350:00

like the lowest hanging fruit. It's just

## 40350:00 - 40375:00

sort of like can you take these

## 40375:00 - 40405:00

processes that like more or less look

## 40405:00 - 40430:00

like you know you have to like click

## 40430:00 - 40455:00

around a bunch of places and pull a

## 40455:00 - 40475:00

bunch of pieces of information and then

## 40475:00 - 40510:00

blend them together and then p produce

## 40510:00 - 40540:00

some analysis on top of that like that

## 40540:00 - 40565:00

process that fundamental like

## 40565:00 - 40595:00

information driven sort of like analysis

## 40595:00 - 40645:00

process is the easiest thing to to drive

## 40645:00 - 40685:00

via workloads and the kinds of data you

## 40685:00 - 40750:00

need are just like you know um uh you we

## 40750:00 - 40770:00

call them kind of environments but

## 40770:00 - 40800:00

usually it's just like what is the task

## 40800:00 - 40845:00

what is the the full um sort of like

## 40845:00 - 40870:00

data set that's necessary to conduct

## 40870:00 - 40910:00

that task and um what is like the rubric

## 40910:00 - 40935:00

for how how you conduct that

## 40935:00 - 40970:00

effectively. Do you need RL and

## 40970:00 - 41015:00

fine-tuning when like prompt engineering

## 41015:00 - 41055:00

and metaprompting seems so good? I think

## 41055:00 - 41080:00

that yeah I mean I think I think

## 41080:00 - 41105:00

prompting I mean as the malls get better

## 41105:00 - 41130:00

prompting will get better but like

## 41130:00 - 41155:00

prompting gets you to a certain level

## 41155:00 - 41185:00

and then reinforcement learning gets you

## 41185:00 - 41235:00

beyond that level. And um actually this

## 41235:00 - 41255:00

is a good point. I I think that like

## 41255:00 - 41290:00

probably most of the time in our in our

## 41290:00 - 41330:00

business it's mostly prompting that just

## 41330:00 - 41365:00

is like works really well. I mean that's

## 41365:00 - 41390:00

the weird thing is like oh shoot you

## 41390:00 - 41415:00

don't have to crack open the models and

## 41415:00 - 41450:00

then frankly like the next models are

## 41450:00 - 41485:00

going to be so good and then the evals

## 41485:00 - 41510:00

are mainly about picking which model or

## 41510:00 - 41535:00

you know at what point do you switch to

## 41535:00 - 41580:00

the next one. I do think startups need

## 41580:00 - 41625:00

basically like a strategy for how they

## 41625:00 - 41690:00

like will um walk up the complexity

## 41690:00 - 41725:00

curve so to speak. Like you need to like

## 41725:00 - 41750:00

you you know whatever product or

## 41750:00 - 41785:00

business you build like needs to like

## 41785:00 - 41830:00

really um benefit from like the ability

## 41830:00 - 41860:00

to like race up this complexity curve

## 41860:00 - 41890:00

which is the broad broader curve of

## 41890:00 - 41935:00

capability of the models. I mean you you

## 41935:00 - 41970:00

actually created this uh leaderboard

## 41970:00 - 42015:00

that has a lot of these super hard tasks

## 42015:00 - 42040:00

that are trying to go into this next

## 42040:00 - 42070:00

curve of uh reasoning. Can you tell us

## 42070:00 - 42095:00

about it? One of the things that we

## 42095:00 - 42125:00

built um in partnership with the center

## 42125:00 - 42175:00

for safety is humanity's last exam. It

## 42175:00 - 42210:00

was a funny name. I think unfortunately

## 42210:00 - 42240:00

there will be yet another exam beyond

## 42240:00 - 42290:00

it. But you know the idea was how like

## 42290:00 - 42350:00

let's effectively work with you know the

## 42350:00 - 42390:00

the the smartest scientists in the field

## 42390:00 - 42425:00

and you know um you know we worked with

## 42425:00 - 42455:00

many very brilliant professors but also

## 42455:00 - 42490:00

very many like individual researchers

## 42490:00 - 42515:00

who are like quite brilliant um and we

## 42515:00 - 42555:00

just collated and aggregated this data

## 42555:00 - 42585:00

set of what the smartest researchers in

## 42585:00 - 42620:00

the world would say the hardest

## 42620:00 - 42650:00

scientific problems they've worked on

## 42650:00 - 42690:00

recently are. they solved them or they

## 42690:00 - 42705:00

sort of like came to the right, you

## 42705:00 - 42725:00

know, they were able to solve the

## 42725:00 - 42745:00

problems, but they're sort of like the

## 42745:00 - 42770:00

hardest problems that they're aware of

## 42770:00 - 42805:00

and know of. I was curious how you came

## 42805:00 - 42835:00

up with these problems. So, each of the

## 42835:00 - 42875:00

professors contributed new problems. So,

## 42875:00 - 42890:00

these are not these are problems that

## 42890:00 - 42925:00

have never appeared in any textbook or

## 42925:00 - 42955:00

any exam ever. They just like came out

## 42955:00 - 42980:00

of their brains and they like typed up

## 42980:00 - 43010:00

like a new problem like from scratch. Am

## 43010:00 - 43030:00

I understanding this right? Yeah. Yeah.

## 43030:00 - 43060:00

And the the general guidance was like,

## 43060:00 - 43100:00

you know, what has come up recently in

## 43100:00 - 43140:00

your research that you think is like a

## 43140:00 - 43175:00

is a particularly hard problem, right?

## 43175:00 - 43200:00

The problems are stupidly hard

## 43200:00 - 43225:00

incidentally. They're like insane. I

## 43225:00 - 43255:00

don't know if you guys have looked at

## 43255:00 - 43290:00

these problems. They're totally crazy.

## 43290:00 - 43310:00

Yeah. It's totally crazy. And by the

## 43310:00 - 43340:00

way, like they cannot be searched on the

## 43340:00 - 43365:00

internet. It's like you need to have a

## 43365:00 - 43425:00

lot of a lot of expertise and actually

## 43425:00 - 43460:00

think about them. Yeah. For quite long

## 43460:00 - 43485:00

time. Yeah. They require a lot of

## 43485:00 - 43520:00

reason. I'm recently like uh right now

## 43520:00 - 43555:00

so we have a time limit where the models

## 43555:00 - 43590:00

um can only think for I think it's 15

## 43590:00 - 43615:00

minutes or 30 minutes and one of the

## 43615:00 - 43635:00

most recent requests from one of the

## 43635:00 - 43660:00

labs was like can you please increase

## 43660:00 - 43710:00

that time limit to like a day so that

## 43710:00 - 43745:00

the model has like up to a day to think

## 43745:00 - 43775:00

about the um to think about the

## 43775:00 - 43820:00

problems. Um but yeah no they're they're

## 43820:00 - 43855:00

deviously hard problems unless you have

## 43855:00 - 43895:00

expertise in the specific problem you

## 43895:00 - 43920:00

probably don't have a chance of getting

## 43920:00 - 43960:00

it right. Um but even this evaluation

## 43960:00 - 43995:00

like I think when we first launched it

## 43995:00 - 44030:00

um you know and this was just earlier

## 44030:00 - 44070:00

this year uh the the best models were

## 44070:00 - 44120:00

scoring like 7% 8% on it. Now the best

## 44120:00 - 44170:00

models score north of 20%. It's moved

## 44170:00 - 44195:00

really really quickly and I think you

## 44195:00 - 44215:00

know I think uh do you think we're going

## 44215:00 - 44240:00

to get a benchmark saturation for this

## 44240:00 - 44270:00

one as well? I think eventually yeah

## 44270:00 - 44300:00

it'll it'll be saturated and then we

## 44300:00 - 44325:00

have to move on to new evaluations. I

## 44325:00 - 44375:00

mean I think the like uh the the the

## 44375:00 - 44405:00

saving grace for the naming was that it

## 44405:00 - 44450:00

is the last exam. The new eval will be

## 44450:00 - 44480:00

sort of like real world tasks, real

## 44480:00 - 44500:00

world activities which are sort of like

## 44500:00 - 44520:00

fundamentally fuzzier and more

## 44520:00 - 44550:00

complicated. Have you solved any of the

## 44550:00 - 44585:00

problems yourself, Alex? I know I I know

## 44585:00 - 44605:00

you were a competitive math person for a

## 44605:00 - 44640:00

long time. Yeah. Yeah. The I mean the

## 44640:00 - 44675:00

math problems require a lot of they're

## 44675:00 - 44715:00

like very deep in the fields. I think uh

## 44715:00 - 44755:00

I was I managed to get a handful but

## 44755:00 - 44805:00

like most of them are like hopeless. Um

## 44805:00 - 44825:00

yeah, I looked at the ones that the

## 44825:00 - 44870:00

models can solve and so

## 44870:00 - 44895:00

so that was that was one of the evals

## 44895:00 - 44915:00

and we we've produced a number of other

## 44915:00 - 44960:00

evaluations but um but yeah, I think

## 44960:00 - 45005:00

that like the the in the AI industry

## 45005:00 - 45065:00

really I think um continues to suffer

## 45065:00 - 45145:00

from a lack of uh very hard evals and

## 45145:00 - 45200:00

very hard tests that show really like

## 45200:00 - 45245:00

the frontier of of um model

## 45245:00 - 45280:00

capabilities. And these eval when you

## 45280:00 - 45305:00

get when you build an eval that sort of

## 45305:00 - 45345:00

like becomes popular in the industry, it

## 45345:00 - 45370:00

has this like deeper effect which is

## 45370:00 - 45400:00

that that's all of a sudden the like

## 45400:00 - 45435:00

northstar and the yard stick that that

## 45435:00 - 45470:00

researchers are trying to um optimize

## 45470:00 - 45500:00

for. And so it's it's actually this like

## 45500:00 - 45530:00

very gratifying activity. You know we

## 45530:00 - 45580:00

built humanity last exam. Um you know

## 45580:00 - 45620:00

most of the like all the model providers

## 45620:00 - 45645:00

um you know will always report their

## 45645:00 - 45680:00

their their their results. There's like

## 45680:00 - 45710:00

tons of researchers who are really

## 45710:00 - 45750:00

motivated by by doing a good job. I mean

## 45750:00 - 45785:00

it's it's uh and and the models are

## 45785:00 - 45815:00

going to get you know deviously good at

## 45815:00 - 45835:00

like you know frontier research

## 45835:00 - 45865:00

problems. I guess Sam's starting to talk

## 45865:00 - 45895:00

about you know that sort of stage four

## 45895:00 - 45945:00

innovators of AGI is coming and you know

## 45945:00 - 45980:00

that's the prognostication for the next

## 45980:00 - 46005:00

year. Do you think that's you know

## 46005:00 - 46050:00

correct the next 20 12 to 24 months is

## 46050:00 - 46080:00

like really the moment that literally

## 46080:00 - 46125:00

new scientific break breakthrough um is

## 46125:00 - 46160:00

coming from the operation of reasoning

## 46160:00 - 46185:00

and these models. I mean, I think it's

## 46185:00 - 46210:00

super plausible, you know, in fields

## 46210:00 - 46240:00

like biology, and this is probably one

## 46240:00 - 46265:00

of the ones that comes up the most, but

## 46265:00 - 46295:00

there's like there's probably intuitions

## 46295:00 - 46330:00

that the models have about biology that

## 46330:00 - 46375:00

humans don't even have um because it's

## 46375:00 - 46405:00

just, you know, they have this like

## 46405:00 - 46430:00

different form of intelligence, right?

## 46430:00 - 46465:00

And so, you'd expect there to be some

## 46465:00 - 46520:00

areas and some fields where the models

## 46520:00 - 46565:00

um have have some fundamental deep

## 46565:00 - 46600:00

advantage versus humans. And so, I think

## 46600:00 - 46630:00

it's like very realistic to expect in

## 46630:00 - 46655:00

those fields. Biology I think is sort of

## 46655:00 - 46685:00

like the clearest one for me. Kind of

## 46685:00 - 46710:00

already happened for chemistry. Last

## 46710:00 - 46755:00

year the Nobel Prize went to uh the

## 46755:00 - 46805:00

Google team Dez and John Jumper with

## 46805:00 - 46850:00

Alpha Fold. Yeah, exactly. That was like

## 46850:00 - 46880:00

a huge jump. Before that there was like

## 46880:00 - 46925:00

this competition where um they were

## 46925:00 - 46965:00

trying to get more protein fold

## 46965:00 - 46995:00

structures that were going to get solved

## 46995:00 - 47055:00

and it was like abysmal and Alphafall

## 47055:00 - 47105:00

destroyed it. It's a strange time to be

## 47105:00 - 47135:00

a scientist, but an exciting time for

## 47135:00 - 47205:00

science. There's this um uh short story.

## 47205:00 - 47235:00

It talks about this future where like,

## 47235:00 - 47290:00

you know, there's uh effectively AIs

## 47290:00 - 47320:00

that are like that are conducting all

## 47320:00 - 47375:00

the frontier of R&D research and um and

## 47375:00 - 47405:00

scientists, you know, what scientists do

## 47405:00 - 47430:00

is they just sort of like look at the

## 47430:00 - 47460:00

discoveries that the AIs make and sort

## 47460:00 - 47490:00

of like try to understand them. Yeah. I

## 47490:00 - 47515:00

mean I think that like very exciting

## 47515:00 - 47550:00

time to to see the how the frontier of

## 47550:00 - 47585:00

human knowledge expands and then I mean

## 47585:00 - 47610:00

I think that'll be great because in

## 47610:00 - 47665:00

areas like um in biology will fuel

## 47665:00 - 47695:00

breakthroughs in medicine and healthcare

## 47695:00 - 47720:00

and and all these other and all these

## 47720:00 - 47745:00

other things and then the majority of

## 47745:00 - 47775:00

the economy will will chug along you

## 47775:00 - 47805:00

know giving humans what they want. China

## 47805:00 - 47840:00

open sourcing or Deepseek open sourcing

## 47840:00 - 47865:00

their models is like another very

## 47865:00 - 47885:00

interesting question like how does that

## 47885:00 - 47930:00

play out and um and there's this awkward

## 47930:00 - 47955:00

sort of thing that you know the best

## 47955:00 - 47985:00

open source models in the world now come

## 47985:00 - 48010:00

out of China I mean that's sort of this

## 48010:00 - 48050:00

like awkward reality uh to contend with

## 48050:00 - 48085:00

and what do you think we can do to just

## 48085:00 - 48110:00

make sure that it's the American models

## 48110:00 - 48145:00

that are ahead or you know is that

## 48145:00 - 48175:00

written in the stars or you know

## 48175:00 - 48215:00

something tells me that's not the

## 48215:00 - 48245:00

simplest explanation for me about why

## 48245:00 - 48275:00

the Chinese models are so good is is

## 48275:00 - 48320:00

espionage I I think that there's um

## 48320:00 - 48375:00

there's a lot of secrets in how these

## 48375:00 - 48410:00

frontier models are trained. Um and when

## 48410:00 - 48435:00

I say secrets, they you know it sounds

## 48435:00 - 48450:00

more interesting than they are, but

## 48450:00 - 48470:00

there's just a lot of task and

## 48470:00 - 48495:00

knowledge. There's a lot of like you

## 48495:00 - 48550:00

know tricks and small um and intuitions

## 48550:00 - 48575:00

about where to set the hyperparameters

## 48575:00 - 48600:00

and like you know ways to make these

## 48600:00 - 48635:00

models um work and to get the model

## 48635:00 - 48685:00

training to work. the Chinese labs have

## 48685:00 - 48710:00

been have been able to move so quickly

## 48710:00 - 48745:00

and accelerate and make such fast

## 48745:00 - 48790:00

progress. Um whereas some even like very

## 48790:00 - 48825:00

talented US labs like have made progress

## 48825:00 - 48855:00

less quickly. And I just purely think

## 48855:00 - 48890:00

it's because you know a lot of the the

## 48890:00 - 48930:00

secrets about how to train these models

## 48930:00 - 48965:00

um you know those secrets leave the

## 48965:00 - 48990:00

frontier labs and make their way back to

## 48990:00 - 49050:00

these Chinese labs. Um I I think the the

## 49050:00 - 49075:00

only way to model the future is that

## 49075:00 - 49145:00

China has pretty advanced models. Um,

## 49145:00 - 49170:00

you know, the Solace right now is

## 49170:00 - 49205:00

they're not the best models. Um, they're

## 49205:00 - 49240:00

sort of like a half step behind, let's

## 49240:00 - 49285:00

say. Um, but, uh, but it's tough to

## 49285:00 - 49310:00

model what'll happen when it's sort of

## 49310:00 - 49335:00

truly neck and neck. We're very behind

## 49335:00 - 49385:00

on energy production, which is just pure

## 49385:00 - 49415:00

regulation, like that could be fixed in

## 49415:00 - 49445:00

2 seconds, but, you know, hasn't been

## 49445:00 - 49470:00

yet. That's a huge problem. I mean, if

## 49470:00 - 49500:00

you look at, you know, not that the past

## 49500:00 - 49530:00

will be a predictor of the future. If

## 49530:00 - 49570:00

you look at what US total grid

## 49570:00 - 49590:00

production looks like, it's like looks

## 49590:00 - 49635:00

flat as a pig. And if you look at um you

## 49635:00 - 49685:00

know Chinese uh aggregate uh you know

## 49685:00 - 49710:00

grid production it's like you know it's

## 49710:00 - 49740:00

doubled over the past decade. It's just

## 49740:00 - 49770:00

like it's just this like straight up I

## 49770:00 - 49805:00

saw that and it's astonishing. It's I

## 49805:00 - 49845:00

mean that's just a policy failure. China

## 49845:00 - 49875:00

just you know the vast majority of that

## 49875:00 - 49925:00

is coal and coal's growing in China and

## 49925:00 - 49960:00

um in the United States uh actually

## 49960:00 - 49990:00

renewables have grown a lot but

## 49990:00 - 50025:00

renewables trade off against the uh the

## 50025:00 - 50050:00

sort of fossil fuels. So we've sort of

## 50050:00 - 50090:00

like done a done a transition of our of

## 50090:00 - 50155:00

our um energy grid whereas they're just

## 50155:00 - 50190:00

continuing to compound. Let's say we

## 50190:00 - 50220:00

have this issue on power production but

## 50220:00 - 50250:00

we're we're advantage in chips. I think

## 50250:00 - 50280:00

like net net we will come out ahead on

## 50280:00 - 50330:00

compute. Um if you look at data I mean

## 50330:00 - 50355:00

this goes towards a lot of the questions

## 50355:00 - 50380:00

you've been you've been asking about but

## 50380:00 - 50410:00

like I mean I think China is like

## 50410:00 - 50435:00

fundamentally very well positioned on

## 50435:00 - 50465:00

data. Um it's weird to say because

## 50465:00 - 50500:00

obviously like you know we help all the

## 50500:00 - 50530:00

American companies with data in China

## 50530:00 - 50570:00

they can ignore copyright or other

## 50570:00 - 50610:00

privacy rules and and they can sort of

## 50610:00 - 50635:00

um you know build these large models

## 50635:00 - 50665:00

without abandon. And then and then the

## 50665:00 - 50700:00

second issue is that um there's actually

## 50700:00 - 50740:00

large scale government programs in China

## 50740:00 - 50795:00

for data labeling. Um there are uh you

## 50795:00 - 50855:00

know seven data labeling centers um like

## 50855:00 - 50880:00

in various cities that have been started

## 50880:00 - 50920:00

up by the government itself. There's

## 50920:00 - 50970:00

large scale subsidies for um for AI

## 50970:00 - 51000:00

companies to use data labeling a voucher

## 51000:00 - 51025:00

system. In fact, there's like college

## 51025:00 - 51055:00

programs because you know one of the

## 51055:00 - 51080:00

interesting things is in China like

## 51080:00 - 51110:00

employment is such a large national

## 51110:00 - 51145:00

priority that they like you know when

## 51145:00 - 51180:00

they have a strategic area like AI

## 51180:00 - 51205:00

they'll like figure out okay what are

## 51205:00 - 51225:00

all the jobs and they'll like create

## 51225:00 - 51275:00

these like funnels to um to to create

## 51275:00 - 51300:00

those jobs. And then we're seeing this

## 51300:00 - 51335:00

in robotics data too where like there's

## 51335:00 - 51365:00

the already in China there are like

## 51365:00 - 51400:00

large scale factories full of robots

## 51400:00 - 51465:00

that just go and collect data. Um and uh

## 51465:00 - 51510:00

and strangely enough like even a lot of

## 51510:00 - 51555:00

US companies today actually rely on data

## 51555:00 - 51585:00

from China in training these like

## 51585:00 - 51610:00

robotics foundation models. Long story

## 51610:00 - 51640:00

short, I think China likely has a data

## 51640:00 - 51670:00

an advantage on data and then the

## 51670:00 - 51745:00

algorithms um you know the US is is on

## 51745:00 - 51770:00

net much more innovative but if

## 51770:00 - 51800:00

espionage continues to be a reality then

## 51800:00 - 51825:00

like you know you're basically even on

## 51825:00 - 51870:00

algorithms. So, um, so it's hard to

## 51870:00 - 51905:00

model, but I think that probably like,

## 51905:00 - 51960:00

you know, it's like 60 40 7030 that the

## 51960:00 - 51995:00

United States like has like an

## 51995:00 - 52025:00

undeniable continued advantage, but

## 52025:00 - 52060:00

there's like a lot of worlds where China

## 52060:00 - 52100:00

just like catches up or potentially even

## 52100:00 - 52130:00

overtakes. I mean the the scary thing

## 52130:00 - 52170:00

for me is you know watching Optimus or

## 52170:00 - 52205:00

YC has uh some robotics companies like

## 52205:00 - 52245:00

Weave Robotics and you know we look at

## 52245:00 - 52285:00

those things the software can be as good

## 52285:00 - 52310:00

or better than anything coming out of

## 52310:00 - 52340:00

China but when it comes to the hardware

## 52340:00 - 52380:00

it's like bomb cost over here 20,000

## 52380:00 - 52420:00

30,000 bucks like you can't you know we

## 52420:00 - 52440:00

can't even make like high precision

## 52440:00 - 52480:00

screws over here and then over there the

## 52480:00 - 52520:00

same m the same robot the embodied robot

## 52520:00 - 52550:00

could be made for like I don't know 2

## 52550:00 - 52590:00

3,000 $4,000 right it's like you just

## 52590:00 - 52615:00

walk down a street in Shenzen Zen and

## 52615:00 - 52650:00

like they they got it, you know, and so

## 52650:00 - 52675:00

how do you compete against that at sort

## 52675:00 - 52725:00

of that at a state level? The degree to

## 52725:00 - 52785:00

which China is incredible manufacturing,

## 52785:00 - 52810:00

I mean that's a that's a very big

## 52810:00 - 52880:00

problem. Um and it relates to defense

## 52880:00 - 52905:00

and national security. It's a

## 52905:00 - 52950:00

fundamental issue uh because on some

## 52950:00 - 52975:00

level defense and national security will

## 52975:00 - 53025:00

boil down to which countries have more

## 53025:00 - 53060:00

things that like can deter conflict or

## 53060:00 - 53105:00

can can go into a you know can can shoot

## 53105:00 - 53130:00

other things down. Yeah. I don't think

## 53130:00 - 53150:00

it's going to be fighter jets and

## 53150:00 - 53185:00

aircraft carriers anymore. I mean it's

## 53185:00 - 53220:00

probably going to be you know this micro

## 53220:00 - 53265:00

war of it's like hyper micro. It's

## 53265:00 - 53310:00

drones and embodied robots and I mean

## 53310:00 - 53340:00

Yeah. Exactly. Drones embodied robots.

## 53340:00 - 53435:00

Cyber warfare. the um cold war era um uh

## 53435:00 - 53455:00

philosophy of like you know you build

## 53455:00 - 53495:00

like bigger and bigger bombs. Um it's

## 53495:00 - 53520:00

like the exact opposite of that. It's

## 53520:00 - 53535:00

actually like it's like the

## 53535:00 - 53585:00

fragmentation and uh and and move

## 53585:00 - 53615:00

towards sort of like you know smaller

## 53615:00 - 53650:00

more nimble attraable resources. Um is

## 53650:00 - 53700:00

the is the that that's like one of the

## 53700:00 - 53735:00

big picture trends I would say. Um and

## 53735:00 - 53760:00

then the other big picture trend is just

## 53760:00 - 53800:00

what we believe which is uh the move

## 53800:00 - 53860:00

towards uh agentic warfare or agentic

## 53860:00 - 53890:00

defense which is basically you know if

## 53890:00 - 53955:00

you if you actually mapped out the what

## 53955:00 - 53990:00

warfare looks like today or like what

## 53990:00 - 54045:00

like the um you know the actual process

## 54045:00 - 54090:00

of a conflict um you know if you look at

## 54090:00 - 54125:00

Russia Ukraine or other conflict other

## 54125:00 - 54165:00

conflict areas like the decision-making

## 54165:00 - 54215:00

processes are driven are remarkably

## 54215:00 - 54245:00

manual and human driven. And it's just

## 54245:00 - 54270:00

like all these all these like very

## 54270:00 - 54315:00

critical battle time decisions are made

## 54315:00 - 54350:00

like with very limited information

## 54350:00 - 54400:00

unfortunately um uh in these like very

## 54400:00 - 54445:00

manual workflows. And so it's very clear

## 54445:00 - 54490:00

that that um if you used AI agents, you

## 54490:00 - 54520:00

would have perfect information and you

## 54520:00 - 54570:00

would have uh immediate decision-m and

## 54570:00 - 54610:00

so that you know it's we're going to see

## 54610:00 - 54660:00

this like huge shift towards um

## 54660:00 - 54710:00

agentdriven uh warfare and agent-driven

## 54710:00 - 54750:00

um conflict and it has the potential of

## 54750:00 - 54775:00

turning these conflicts into these like

## 54775:00 - 54825:00

almost incomprehensibly fastm moving uh

## 54825:00 - 54865:00

kinds of scenarios. And that's something

## 54865:00 - 54895:00

that you guys are actively working on,

## 54895:00 - 54925:00

right? Can you is there anything that

## 54925:00 - 54955:00

you can talk about? I assume some of it

## 54955:00 - 55005:00

is classified, but yeah. Yeah. So, one

## 55005:00 - 55030:00

of the things we're doing is we we're

## 55030:00 - 55060:00

building this uh this system called

## 55060:00 - 55105:00

Thunder Forge um with uh the Indopacific

## 55105:00 - 55145:00

Command um out in out in Hawaii. It's

## 55145:00 - 55180:00

responsible for the sort of Indopacific

## 55180:00 - 55230:00

region and it is the flagship DoD

## 55230:00 - 55270:00

program for um using AI for military

## 55270:00 - 55305:00

planning and and operations. So, we're

## 55305:00 - 55335:00

basically doing exactly what I said. We

## 55335:00 - 55380:00

are we take the h the existing human

## 55380:00 - 55410:00

workflow the military works in a what's

## 55410:00 - 55445:00

called a doctrinal way or they're sort

## 55445:00 - 55485:00

of like governed by the doctrine of this

## 55485:00 - 55515:00

like you know very established military

## 55515:00 - 55550:00

planning process and you just convert

## 55550:00 - 55600:00

that into you know a series of agents

## 55600:00 - 55640:00

that work together um and and conduct

## 55640:00 - 55660:00

you know the exact same task but it's

## 55660:00 - 55695:00

just like all agent driven and then all

## 55695:00 - 55740:00

of a sudden you you turn these like um

## 55740:00 - 55765:00

very critical decision-making cycles

## 55765:00 - 55830:00

from you know 72 hours to 10 minutes And

## 55830:00 - 55875:00

it kind of like changes it from um you

## 55875:00 - 55910:00

know you know when you play chess if you

## 55910:00 - 55935:00

play chess versus a human they have to

## 55935:00 - 55965:00

spend all this time thinking um you know

## 55965:00 - 55990:00

you you know it's sort of this like slow

## 55990:00 - 56020:00

game and if you play chess against a

## 56020:00 - 56045:00

computer it's just like these immediate

## 56045:00 - 56075:00

moves back and it's like this sort of

## 56075:00 - 56125:00

like unrelenting form of of warfare. I

## 56125:00 - 56150:00

mean some of it is like the being able

## 56150:00 - 56175:00

to see the chain of thought immediately

## 56175:00 - 56225:00

was is the most powerful thing. Yeah.

## 56225:00 - 56250:00

Like cuz is you know I don't want the

## 56250:00 - 56285:00

answer. I want to see how you got there.

## 56285:00 - 56315:00

And then actually seeing the reasoning

## 56315:00 - 56355:00

itself was so powerful. I mean that's

## 56355:00 - 56405:00

actually why the um launch of that first

## 56405:00 - 56435:00

deepseek was way more interesting

## 56435:00 - 56485:00

because uh I think 01 had come out but

## 56485:00 - 56515:00

they hid the uh the reasoning and it's

## 56515:00 - 56550:00

like no the reasoning is actually a

## 56550:00 - 56580:00

really important part of it and the only

## 56580:00 - 56610:00

reason why they hid it was they didn't

## 56610:00 - 56640:00

want other people to steal it which they

## 56640:00 - 56670:00

did anyway. I think that that's that's

## 56670:00 - 56725:00

another like um interesting thing about

## 56725:00 - 56785:00

this space which is that um you know so

## 56785:00 - 56810:00

far you could really model as like

## 56810:00 - 56850:00

there's like advanced capabilities um

## 56850:00 - 56875:00

and you can try to keep those secret and

## 56875:00 - 56900:00

you can try to keep those closed but

## 56900:00 - 56930:00

they open over time kind of no matter

## 56930:00 - 56970:00

what you do. Well, I mean clearly Alex

## 56970:00 - 57025:00

you've done a lot of incredible things

## 57025:00 - 57055:00

and transformed your company multiple

## 57055:00 - 57090:00

times and you have all these deep matter

## 57090:00 - 57130:00

expertise in many areas. you're clearly

## 57130:00 - 57180:00

hardcore. Is there advice for the

## 57180:00 - 57210:00

audience to be more like you? You know,

## 57210:00 - 57250:00

I think that the the the biggest thing

## 57250:00 - 57295:00

is um you just have to really really

## 57295:00 - 57350:00

really care. Um and I think it's like a

## 57350:00 - 57405:00

a folly of youth in some ways that um

## 57405:00 - 57430:00

that when you're young like almost

## 57430:00 - 57465:00

everything feels like, you know, so

## 57465:00 - 57495:00

astronomically important that you just

## 57495:00 - 57530:00

like you try immensely hard and you care

## 57530:00 - 57570:00

about every detail. You know, everything

## 57570:00 - 57605:00

uh matters just way more to you. And I

## 57605:00 - 57655:00

think um and I think that that trait is

## 57655:00 - 57700:00

really really important and um you know

## 57700:00 - 57720:00

it's like just in varying degrees for

## 57720:00 - 57750:00

different people. So I wrote this post

## 57750:00 - 57775:00

many years ago called hire people who

## 57775:00 - 57820:00

give a and it really is pretty

## 57820:00 - 57855:00

simple. You notice I noticed, you know,

## 57855:00 - 57875:00

when you interview people or when you

## 57875:00 - 57890:00

interact with people, you can tell

## 57890:00 - 57925:00

people who are just sort of like phone

## 57925:00 - 57955:00

it in versus people who sort of like

## 57955:00 - 58010:00

they like hang on to their work as like,

## 58010:00 - 58045:00

you know, it's like it's like so

## 58045:00 - 58085:00

incredibly monumental and forceful and

## 58085:00 - 58120:00

important to them that they they do

## 58120:00 - 58150:00

great work and it sort of like eats at

## 58150:00 - 58175:00

them when they don't do great work and

## 58175:00 - 58195:00

when they do great work, they're sort of

## 58195:00 - 58225:00

so satisfied with themselves. And so

## 58225:00 - 58255:00

there's sort of this like um the

## 58255:00 - 58305:00

magnitude of of care. And one of the

## 58305:00 - 58345:00

greatest indicators of like a just like

## 58345:00 - 58365:00

how much I enjoyed working with people

## 58365:00 - 58395:00

or like frankly how successful they were

## 58395:00 - 58435:00

at scale was really just this like what

## 58435:00 - 58480:00

is what you know to what degree of their

## 58480:00 - 58515:00

what degree their soul is invested in

## 58515:00 - 58580:00

into um uh into the work that they do.

## 58580:00 - 58615:00

And so I think that that you know if you

## 58615:00 - 58645:00

were to pick one thing that that

## 58645:00 - 58670:00

probably is the sort of like unifier in

## 58670:00 - 58710:00

some way. It's like, you know, um I care

## 58710:00 - 58750:00

a lot, uh I care a lot about every

## 58750:00 - 58785:00

decision we make at the company. Um you

## 58785:00 - 58820:00

know, I still review every hire at the

## 58820:00 - 58845:00

company. You know, I I we have this

## 58845:00 - 58885:00

process why where I approve or reject

## 58885:00 - 58905:00

literally every single hire at the

## 58905:00 - 58955:00

company. Um uh and and so I care

## 58955:00 - 58990:00

immensely and then this and then like I

## 58990:00 - 59005:00

work with all these people who care

## 59005:00 - 59040:00

immensely and then that enables us to

## 59040:00 - 59100:00

really sort of like we um we feel much

## 59100:00 - 59125:00

more deeply what happens in the business

## 59125:00 - 59170:00

and as a result we sort of like uh you

## 59170:00 - 59190:00

know we'll change course more quickly

## 59190:00 - 59230:00

we'll learn more quickly um we will

## 59230:00 - 59255:00

we'll take our work more seriously we'll

## 59255:00 - 59280:00

adapt more quickly and I think that

## 59280:00 - 59310:00

that's been quite important to the to

## 59310:00 - 59340:00

the success that we've had. Alex, you

## 59340:00 - 59375:00

were telling me a story recently that

## 59375:00 - 59405:00

stuck with me about how like quite

## 59405:00 - 59435:00

recently even even when Scale was a very

## 59435:00 - 59465:00

large company, you were personally hand

## 59465:00 - 59500:00

reviewing all like the data that was

## 59500:00 - 59525:00

being sent to partner companies and

## 59525:00 - 59560:00

being like basically like the final

## 59560:00 - 59590:00

quality control like you know like you

## 59590:00 - 59630:00

know that data point is not good enough.

## 59630:00 - 59665:00

Yeah, exactly. I think a lot of founders

## 59665:00 - 59725:00

would probably um would probably uh you

## 59725:00 - 59765:00

know agree with this but um what your

## 59765:00 - 59800:00

customers feel and when your customers

## 59800:00 - 59835:00

are happy and sad like it really like

## 59835:00 - 59865:00

gets to you and so when you have when

## 59865:00 - 59890:00

you have unhappy customers it's like

## 59890:00 - 59930:00

it's like personally very painful thing

## 59930:00 - 59970:00

broadly speaking you know we have this

## 59970:00 - 60005:00

value at our company um quality is

## 60005:00 - 60055:00

fractal um and and I do believe that

## 60055:00 - 60120:00

like high standards sort of like um they

## 60120:00 - 60165:00

trickle down within an organization and

## 60165:00 - 60210:00

um you know it's very rare that you see

## 60210:00 - 60255:00

an organization where like where like

## 60255:00 - 60310:00

standards um increase as you get lower

## 60310:00 - 60340:00

and lower down in the organization. You

## 60340:00 - 60355:00

know most of the time when people

## 60355:00 - 60380:00

realize their manager or their

## 60380:00 - 60400:00

management manager or their like

## 60400:00 - 60430:00

director or whomever don't really care

## 60430:00 - 60460:00

then they sort of like you know that

## 60460:00 - 60510:00

that removes the sort of like the like

## 60510:00 - 60550:00

deep desire to to need to care. Um, and

## 60550:00 - 60580:00

so it's like incredibly important that

## 60580:00 - 60625:00

that high standards um, and and this

## 60625:00 - 60680:00

sort of like this deep um, uh, sort of

## 60680:00 - 60720:00

care for quality is like this is this

## 60720:00 - 60775:00

like um, deeply embedded sort of um,

## 60775:00 - 60810:00

tenant of the entire organization.

## 60810:00 - 60870:00

Founder mode, man. Founder mode, man. We

## 60870:00 - 60900:00

got to have you back. Thank you so much

## 60900:00 - 60940:00

for spending time with us. With that,

## 60940:00 - 60975:00

sorry we're out of time, but we'll see

## 60975:00 - 61005:00

you next time.

## 61005:00 - 61045:00

[Music]

## 61045:00 - 61120:00

Heat. Hey, heat. Hey, heat.

## 61120:00+

[Music]

