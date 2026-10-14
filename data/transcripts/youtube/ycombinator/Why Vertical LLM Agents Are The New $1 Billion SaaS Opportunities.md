---
source: https://www.youtube.com/watch?v=eBVi_sLaYsc
title: Why Vertical LLM Agents Are The New $1 Billion SaaS Opportunities
author: Y Combinator
date: 2024-10-04
views: 440978
description: >-
  As LLM’s become exponentially better it is clear that vertical AI agents are
  key to the next generation of billion dollar SaaS companies. In this episode
  of the Lightcone, the hosts sit down with YC alum Jake Heller, the co-founder
  and CEO of Casetext (which sold to Thomson Reuters for $650 million in cash in
  2023) to discuss what it takes to build a successful vertical AI company and
  overcome resistance from industry veterans and skeptics.  


  Chapters (Powered by https://bit.ly/chapterme-yc) -

  00:00 Coming Up

  01:40 Building a successful vertical AI company

  06:05 The unique challenges of law and AI

  09:24 The turning point for lawyers with ChatGPT

  11:25 Finding product market fit in legal

  15:04 Entering deep founder mode

  20:40 Approaching prompt engineering step by step

  25:05 Going beyond GPT wrappers

  28:10 Aiming for 100% accuracy

  30:48 Thoughts on o1’s capabilities

  36:42 Outro
tags:
  - YC
  - Y Combinator
  - SaaS
  - Vertical AI
  - Open AI
  - o1
  - ChatGPT
  - Jake Heller
  - Garry Tan
  - Diana Hu
  - Jared Friedman
  - Casetext
  - Thomson Reuters
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T11:52:40.008Z
---

# Why Vertical LLM Agents Are The New $1 Billion SaaS Opportunities

## 00:00 - 35:00

this is their first ever experience

## 35:00 - 70:00

talking to this Godlike feeling you know

## 70:00 - 100:00

AI that was all of a sudden doing these

## 100:00 - 150:00

tasks that would take me when I practice

## 150:00 - 175:00

like a whole day and it's being done in

## 175:00 - 200:00

a minute and a half the whole company

## 200:00 - 230:00

all 120 of us did not sleep for those

## 230:00 - 260:00

you know months before gbd4 we felt like

## 260:00 - 300:00

we had this amazing opportunity to run

## 300:00 - 325:00

far ahead of the market that's why

## 325:00 - 355:00

you're the first man on the moon

## 355:00 - 465:00

[Music]

## 465:00 - 510:00

yeah welcome back to another episode of

## 510:00 - 555:00

the light cone I'm Gary this is Jared

## 555:00 - 595:00

and Diana Harge is out but he'll be back

## 595:00 - 655:00

on the next one and today we have a very

## 655:00 - 710:00

special guest Jake heler of case text I

## 710:00 - 755:00

think of Jake is a little bit like one

## 755:00 - 795:00

of the first people on the surface of

## 795:00 - 845:00

the Moon he created uh case tax more

## 845:00 - 915:00

than I think 11 12 years ago actually

## 915:00 - 970:00

and in the first 10 years you went from0

## 970:00 - 1030:00

to $100 million valuation and then in a

## 1030:00 - 1075:00

matter of 2 months after the release of

## 1075:00 - 1140:00

GPT 4 that valuation went to a liquid

## 1140:00 - 1215:00

exit to Thompson Reuters for $650

## 1215:00 - 1270:00

million so you have a lot of lessons

## 1270:00 - 1330:00

about how to create real value from

## 1330:00 - 1360:00

really like large language models I

## 1360:00 - 1385:00

think you were of um you know our

## 1385:00 - 1435:00

friends in YC one of the first people to

## 1435:00 - 1485:00

actually realize this is a sea change

## 1485:00 - 1530:00

and revolution and not only that we're

## 1530:00 - 1560:00

going to bet the company on it and you

## 1560:00 - 1610:00

were super right so welcome Jake happy

## 1610:00 - 1635:00

to be here one of the cool things I

## 1635:00 - 1670:00

think about Jake story and reason why we

## 1670:00 - 1705:00

wanted to bring him on today is that if

## 1705:00 - 1735:00

you just look at the companies that good

## 1735:00 - 1775:00

Founders are starting now it's a lot of

## 1775:00 - 1810:00

vertical AI agents I mean I was trying

## 1810:00 - 1865:00

to count the ones in s24 we have

## 1865:00 - 1905:00

literally dozens of the YC companies in

## 1905:00 - 1925:00

the last batch for building vertical

## 1925:00 - 1970:00

specific AI agents and I think Jake is

## 1970:00 - 2010:00

the founder who is currently running the

## 2010:00 - 2050:00

most successful vertical AI agent it's

## 2050:00 - 2075:00

by far the largest acquisition and it's

## 2075:00 - 2115:00

actually deployed at scale in a lot of

## 2115:00 - 2160:00

mission critical situations and the

## 2160:00 - 2200:00

inspiration for this was uh we hosted

## 2200:00 - 2235:00

this Retreat a few months ago and Jake

## 2235:00 - 2280:00

gave an incredible talk about how he

## 2280:00 - 2320:00

built it and we thought that it'd be

## 2320:00 - 2350:00

super useful for people who watch the

## 2350:00 - 2375:00

light cone who are interested in this

## 2375:00 - 2415:00

area to hear directly from one of the

## 2415:00 - 2445:00

most successful builders in this area

## 2445:00 - 2505:00

how he did it so how did you do it

## 2505:00 - 2540:00

well first of all like like a lot of

## 2540:00 - 2570:00

these things um there's a certain amount

## 2570:00 - 2600:00

of luck over the course of our decade

## 2600:00 - 2645:00

long uh Journey we started investing

## 2645:00 - 2685:00

very deeply in AI uh and natural

## 2685:00 - 2730:00

language processing and we we became

## 2730:00 - 2755:00

close with a number of different

## 2755:00 - 2785:00

research Labs including some of the

## 2785:00 - 2840:00

folks at open Ai and when it came time

## 2840:00 - 2880:00

for them to start testing early versions

## 2880:00 - 2905:00

uh we didn't realize it was gbd4 at the

## 2905:00 - 2940:00

time but what was what was

## 2940:00 - 2985:00

gbd4 we got a very early kind of like

## 2985:00 - 3010:00

view of it

## 3010:00 - 3055:00

and so you know months before the public

## 3055:00 - 3110:00

release of gbd4 you know we as a company

## 3110:00 - 3150:00

were all under NDA all working on this

## 3150:00 - 3190:00

thing and I I'll never forget the first

## 3190:00 - 3240:00

time I saw it it took maybe 48 hours for

## 3240:00 - 3270:00

us to decide to take every single person

## 3270:00 - 3300:00

of the company and shift what they were

## 3300:00 - 3340:00

working on from what the projects we

## 3340:00 - 3380:00

were then working on at the time to 100%

## 3380:00 - 3410:00

of the company all working on building

## 3410:00 - 3440:00

this new product we call co-counsel

## 3440:00 - 3470:00

based on the Jeep D4 technology how many

## 3470:00 - 3500:00

people was that we're about 20 people at

## 3500:00 - 3540:00

the time so you took like 120 people and

## 3540:00 - 3560:00

completely changed what they were all

## 3560:00 - 3605:00

working on yes yes yes in 48 hours yes

## 3605:00 - 3645:00

and for the people watching uh casex

## 3645:00 - 3685:00

originally I mean had always been in the

## 3685:00 - 3720:00

legal space you're a lawyer and you

## 3720:00 - 3750:00

built something for yourself and you

## 3750:00 - 3785:00

know sort of the first versions of it

## 3785:00 - 3825:00

were actually sort of uh annotated

## 3825:00 - 3865:00

versions of case law actually yeah

## 3865:00 - 3890:00

that's exactly right so in the very

## 3890:00 - 3940:00

early Origins the company the mission of

## 3940:00 - 3975:00

the company what we're always focused on

## 3975:00 - 4015:00

is how can we build something that

## 4015:00 - 4040:00

brings the best of technology to the

## 4040:00 - 4085:00

legal space um I as a lawyer I actually

## 4085:00 - 4125:00

like the job a lot the parts of my job

## 4125:00 - 4160:00

that I hated the most was when I had to

## 4160:00 - 4180:00

interact with the technology that

## 4180:00 - 4220:00

lawyers have to use um regularly to get

## 4220:00 - 4255:00

the job done I remember thinking and

## 4255:00 - 4305:00

this is like 2012 when I was at a law

## 4305:00 - 4335:00

firm if I want want to do something

## 4335:00 - 4370:00

really trivial I had like a new iPhone

## 4370:00 - 4410:00

at the time I can go on Google and find

## 4410:00 - 4460:00

like movie times or where's the closest

## 4460:00 - 4480:00

open Thai restaurant with vegetarian

## 4480:00 - 4515:00

options that was super easy but if I

## 4515:00 - 4535:00

wanted to find the piece of evidence

## 4535:00 - 4565:00

that was going to exonerate my client

## 4565:00 - 4580:00

and and make it so he doesn't have to go

## 4580:00 - 4620:00

to jail for the rest of his life or the

## 4620:00 - 4650:00

um key legal case that will help me win

## 4650:00 - 4680:00

a billion dollar lawsuit well that's

## 4680:00 - 4705:00

going to be like 5 days in a row till

## 4705:00 - 4730:00

5:00 a.m. every day it's like there's

## 4730:00 - 4750:00

got to be a better way what is the

## 4750:00 - 4775:00

process as a lawyer you would have to

## 4775:00 - 4815:00

read the Stacks and stacks of documents

## 4815:00 - 4855:00

pretty much yeah um right before I

## 4855:00 - 4880:00

started practicing before everything

## 4880:00 - 4915:00

went virtual or like

## 4915:00 - 4960:00

online uh you would literally be in a

## 4960:00 - 5000:00

basement with Bankers box is full of

## 5000:00 - 5045:00

documents reading them one by one by one

## 5045:00 - 5080:00

to try to find you know all the emails

## 5080:00 - 5115:00

in a company like fiser or Google to see

## 5115:00 - 5155:00

if there is potential fraud or um and

## 5155:00 - 5190:00

then if you wanted to find case law

## 5190:00 - 5215:00

slightly before my time you'd literally

## 5215:00 - 5240:00

go to the library and open up books and

## 5240:00 - 5275:00

just start reading and you know new

## 5275:00 - 5310:00

products were coming out that were some

## 5310:00 - 5345:00

of the first web-based research tools

## 5345:00 - 5370:00

but they were pretty clunky it was just

## 5370:00 - 5400:00

hard to find the relevant information

## 5400:00 - 5435:00

you couldn't do contrl F or any of this

## 5435:00 - 5470:00

stuff basically basally not yeah and

## 5470:00 - 5505:00

what was interesting about your is you

## 5505:00 - 5545:00

also happened to be the rare breed of

## 5545:00 - 5580:00

having also computer science training so

## 5580:00 - 5620:00

this must have driven you nuts yeah

## 5620:00 - 5665:00

exactly I mean in the law firm I'll

## 5665:00 - 5715:00

never forget I was building like browser

## 5715:00 - 5765:00

plugins to go on top of the the tools I

## 5765:00 - 5800:00

was using just to make my like life more

## 5800:00 - 5830:00

efficient and effective and actually one

## 5830:00 - 5845:00

of the reasons I left the law firm to

## 5845:00 - 5885:00

start a company and apply to YC was I

## 5885:00 - 5910:00

got in trouble with the general counsel

## 5910:00 - 5930:00

who thought like hey why are you

## 5930:00 - 5950:00

spending all your time you know doing

## 5950:00 - 5985:00

this Tech stuff and also made at the

## 5985:00 - 6015:00

time very clear that that my Law Firm

## 6015:00 - 6040:00

owns all that

## 6040:00 - 6075:00

technology so I decided to do something

## 6075:00 - 6105:00

different so do you want to tell us a

## 6105:00 - 6130:00

little bit about the first 10 years of

## 6130:00 - 6170:00

case text the sort of like long slog in

## 6170:00 - 6220:00

the pre llm era one of the lessons here

## 6220:00 - 6255:00

I think that I took away from that time

## 6255:00 - 6305:00

period is that uh when you start a

## 6305:00 - 6345:00

company you may not get the exact right

## 6345:00 - 6360:00

you may have like the right kind of

## 6360:00 - 6385:00

general direction you know there's a

## 6385:00 - 6415:00

problem you're trying to solve it but it

## 6415:00 - 6435:00

could take a very long time to figure

## 6435:00 - 6465:00

out what the solution is for us for

## 6465:00 - 6500:00

example you know we saw that there was

## 6500:00 - 6535:00

this kind of combined issue of like bad

## 6535:00 - 6575:00

technology in the legal sphere but also

## 6575:00 - 6605:00

like this very like a lot of lawyers use

## 6605:00 - 6650:00

content to do things like research and

## 6650:00 - 6690:00

understand like what the law is and so

## 6690:00 - 6720:00

we thought okay well we can do the

## 6720:00 - 6745:00

technology better but how are we going

## 6745:00 - 6770:00

get this content and we spent like a

## 6770:00 - 6800:00

couple of years trying to get as Gary

## 6800:00 - 6845:00

said lawyers to annotate case law and to

## 6845:00 - 6880:00

provide information so it's like a ugc

## 6880:00 - 6915:00

site like user generated that was a big

## 6915:00 - 6940:00

focus of ours like the kind of onew

## 6940:00 - 6975:00

punch of better technology but also

## 6975:00 - 7010:00

better content um we you know at the

## 7010:00 - 7035:00

time our heroes were like stock overflow

## 7035:00 - 7065:00

and Wikipedia and GitHub and other kind

## 7065:00 - 7115:00

of Open Source or ugc kind of websites

## 7115:00 - 7150:00

and it was a total failure like we could

## 7150:00 - 7175:00

not get lawyers to contribute their time

## 7175:00 - 7210:00

and information and and I think these

## 7210:00 - 7230:00

are just different populations the

## 7230:00 - 7265:00

typical Wikipedia editor has more time

## 7265:00 - 7290:00

on their hands than they know what to do

## 7290:00 - 7320:00

with and so they're adding not all but

## 7320:00 - 7350:00

but many do and they're adding content

## 7350:00 - 7400:00

for free um and and altruistically

## 7400:00 - 7440:00

lawyers bill by the hour their time is

## 7440:00 - 7460:00

incredibly valuable they're always

## 7460:00 - 7495:00

running out of time they had no time to

## 7495:00 - 7530:00

kind of contribute to some ugc site so

## 7530:00 - 7585:00

we had to Pivot and we started investing

## 7585:00 - 7615:00

investing very deeply at the time it was

## 7615:00 - 7640:00

not called AI it's just like natural

## 7640:00 - 7675:00

language processing and machine learning

## 7675:00 - 7715:00

and saw that first of all we didn't need

## 7715:00 - 7750:00

to create all this ugc like to to

## 7750:00 - 7800:00

replicate some of the best benefits of

## 7800:00 - 7820:00

what our competitors had in these big

## 7820:00 - 7860:00

content databases some of it you can

## 7860:00 - 7900:00

basically do even then kind of automated

## 7900:00 - 7950:00

basis and then also uh we were starting

## 7950:00 - 7985:00

to create these user experiences that

## 7985:00 - 7995:00

were

## 7995:00 - 8015:00

you know a lot better than what our

## 8015:00 - 8070:00

competitors could offer based on then at

## 8070:00 - 8105:00

the time what seems kind of quaint like

## 8105:00 - 8145:00

AI stuff like you know the same

## 8145:00 - 8185:00

recommendation algorithm that powers

## 8185:00 - 8215:00

Pandora and spotify's like recommended

## 8215:00 - 8265:00

music you can use they look at basically

## 8265:00 - 8295:00

is how this song relates to that song

## 8295:00 - 8315:00

people listen to this also list to this

## 8315:00 - 8345:00

and this and this right similarly we

## 8345:00 - 8380:00

looked at okay cases that site to you

## 8380:00 - 8400:00

know other cases they all reference

## 8400:00 - 8440:00

earlier opinions you know they they kind

## 8440:00 - 8485:00

of build out this network of citations

## 8485:00 - 8515:00

and we found ways that we can check a

## 8515:00 - 8540:00

lawyer work they'd upload their work so

## 8540:00 - 8575:00

far and be like well everybody who talks

## 8575:00 - 8595:00

about this case talks about this case

## 8595:00 - 8640:00

too and you missed that um so cool

## 8640:00 - 8695:00

experiences like that but the truth is

## 8695:00 - 8740:00

until the very end until co-counsel a

## 8740:00 - 8775:00

lot of what we did were relatively

## 8775:00 - 8795:00

speaking kind of incremental

## 8795:00 - 8825:00

improvements on the legal

## 8825:00 - 8870:00

workflow and one of the things that's

## 8870:00 - 8915:00

kind of weird about this is um when

## 8915:00 - 8940:00

there's just an incremental Improvement

## 8940:00 - 8975:00

it's actually pretty easy to ignore a

## 8975:00 - 9000:00

lot of our clients

## 9000:00 - 9025:00

they never say this literally but you

## 9025:00 - 9045:00

kind this impression you walk into the

## 9045:00 - 9090:00

room their office and you try to pitch

## 9090:00 - 9110:00

them a product and you say this is going

## 9110:00 - 9130:00

to change everything about the way you

## 9130:00 - 9170:00

practice and they go well I make $5

## 9170:00 - 9210:00

million a year I don't want nothing to

## 9210:00 - 9260:00

change this technology PL it's not I do

## 9260:00 - 9285:00

not want to introduce anything that has

## 9285:00 - 9315:00

the opportunity to make my life at all

## 9315:00 - 9355:00

worse um or potentially worse or

## 9355:00 - 9375:00

potentially more efficient because they

## 9375:00 - 9420:00

build by the hour it was really only

## 9420:00 - 9470:00

after like much later when chat GPD came

## 9470:00 - 9500:00

out you know the time we were privately

## 9500:00 - 9545:00

and secretly working on gp4 chat GPT

## 9545:00 - 9585:00

came out and all of a sudden every

## 9585:00 - 9640:00

lawyer in America probably in the world

## 9640:00 - 9695:00

saw oh my God I don't know exactly how

## 9695:00 - 9730:00

this going to change my work but it's

## 9730:00 - 9760:00

going to change it very substantially

## 9760:00 - 9805:00

like they could feel it and the same you

## 9805:00 - 9825:00

know guys and gals were telling us I

## 9825:00 - 9845:00

make $5 million a year why would it

## 9845:00 - 9875:00

change anything about my life we like I

## 9875:00 - 9895:00

make $5 million a year this is going to

## 9895:00 - 9920:00

change something I need to be ahead of

## 9920:00 - 9950:00

this the technology itself and we'll get

## 9950:00 - 9980:00

into a second really changed what we can

## 9980:00 - 10020:00

build for life employers but also the

## 10020:00 - 10075:00

market perceptions of what was like what

## 10075:00 - 10120:00

was necessary really Chang as well and

## 10120:00 - 10160:00

for the first time in our 10 years you

## 10160:00 - 10190:00

know even before we launched Co counil

## 10190:00 - 10230:00

publicly based on GPT 4 they were

## 10230:00 - 10250:00

calling us like you know we know you

## 10250:00 - 10290:00

work on AI we need to get on top of this

## 10290:00 - 10310:00

what can you know what can you show us

## 10310:00 - 10335:00

what can we what can we work on and I

## 10335:00 - 10355:00

think it's because the change was not

## 10355:00 - 10380:00

incremental anymore it was like

## 10380:00 - 10410:00

fundamental and all of a sudden they had

## 10410:00 - 10430:00

to pay attention they could not ignore

## 10430:00 - 10465:00

it I guess uh the mental model I have

## 10465:00 - 10505:00

for you is there's this concept of the

## 10505:00 - 10540:00

idea maze you know the founder goes in

## 10540:00 - 10575:00

the beginning of the Maze and they're

## 10575:00 - 10615:00

just like feeling around like actually

## 10615:00 - 10660:00

uh in the arena talking to you know

## 10660:00 - 10695:00

customers learning like where are the

## 10695:00 - 10735:00

walls which which path to go should I go

## 10735:00 - 10785:00

left or right like and then um as is

## 10785:00 - 10830:00

actually common for startup Founders in

## 10830:00 - 10865:00

the idea maze you will actually reach a

## 10865:00 - 10900:00

dead end and then usually you have to

## 10900:00 - 10940:00

Pivot yeah and then I think you have a

## 10940:00 - 10965:00

very interesting story because you were

## 10965:00 - 11020:00

sort of towards the end of maybe like

## 11020:00 - 11050:00

one of the uh you know parts that

## 11050:00 - 11070:00

weren't going to get you all the way to

## 11070:00 - 11125:00

product Market fit but then lm's Dro and

## 11125:00 - 11155:00

then it's like the maze got shaken up

## 11155:00 - 11185:00

yeah and then you are actually much

## 11185:00 - 11235:00

closer to product Market fit than

## 11235:00 - 11270:00

absolutely anyone else

## 11270:00 - 11310:00

that's yeah I it's exactly right that's

## 11310:00 - 11335:00

why you're the first man on the moon

## 11335:00 - 11365:00

yeah yeah I think I think there's

## 11365:00 - 11395:00

there's cly something to that and the

## 11395:00 - 11445:00

thing is you know each time we got

## 11445:00 - 11480:00

progressed through that maze it felt

## 11480:00 - 11505:00

like maybe now we're at product Market

## 11505:00 - 11535:00

fit you know we were making real Revenue

## 11535:00 - 11575:00

before we um launched co- counil and we

## 11575:00 - 11595:00

had real customers and they said really

## 11595:00 - 11630:00

great things about us I keep on thinking

## 11630:00 - 11650:00

about this article written by Mark

## 11650:00 - 11690:00

andreon in like the early 2000s uh I

## 11690:00 - 11710:00

think it's called the only thing that

## 11710:00 - 11755:00

matters and in it he describes the what

## 11755:00 - 11780:00

it feels like to have product Market fit

## 11780:00 - 11810:00

he lists things like your servers will

## 11810:00 - 11845:00

go down you can't hire support people

## 11845:00 - 11875:00

and sales people fast enough you're

## 11875:00 - 11905:00

going to eat for a yearfree at bucks the

## 11905:00 - 11950:00

the kind of famous Woodside you know uh

## 11950:00 - 11980:00

Diner where where a lot of VCS will take

## 11980:00 - 11995:00

you

## 11995:00 - 12040:00

the press and I read that early on in my

## 12040:00 - 12085:00

like like you know career and I was like

## 12085:00 - 12110:00

okay well that's like

## 12110:00 - 12140:00

hyperbolic but when we launched Co

## 12140:00 - 12185:00

counil it was literally exactly that our

## 12185:00 - 12205:00

servers were going down we could not

## 12205:00 - 12225:00

hire support people fast enough we

## 12225:00 - 12255:00

couldn't hire sales people fast enough I

## 12255:00 - 12320:00

ate a lot of bucks you know um before we

## 12320:00 - 12345:00

was a really big day if we in the ABA

## 12345:00 - 12380:00

journal or some other you know legal

## 12380:00 - 12420:00

specific uh publication we were on CNN

## 12420:00 - 12465:00

and MSNBC and like you know all of a

## 12465:00 - 12485:00

sudden everything changed and that's

## 12485:00 - 12505:00

real product Market fit looks like I

## 12505:00 - 12545:00

think Mark Mark was even in like 2005

## 12545:00 - 12585:00

whenever the article came out exactly

## 12585:00 - 12610:00

right about it looked like in 2023 can

## 12610:00 - 12635:00

you talk about that crazy time because

## 12635:00 - 12655:00

it was only two months from when you

## 12655:00 - 12685:00

launched co- counil to getting bought

## 12685:00 - 12725:00

for $650 million so like what happened

## 12725:00 - 12755:00

in those two months well to to be clear

## 12755:00 - 12780:00

the transaction only closed six months

## 12780:00 - 12805:00

after we launched but it was two months

## 12805:00 - 12860:00

the conversation started and so uh so we

## 12860:00 - 12905:00

started building CO counil and and for

## 12905:00 - 12935:00

just just to uh to kind of background

## 12935:00 - 12970:00

purposes the idea we came up with again

## 12970:00 - 13000:00

like 48 hours like a weekend after

## 13000:00 - 13045:00

seeing gp4 was um and it's something

## 13045:00 - 13075:00

that not but kind of still sound crazy

## 13075:00 - 13105:00

today but it's feel felt crazy at the

## 13105:00 - 13165:00

time which is this AI Legal Assistant by

## 13165:00 - 13190:00

which we mean it's like almost like a

## 13190:00 - 13215:00

new member of the firm you can just talk

## 13215:00 - 13255:00

to it um not unlike how you might talk

## 13255:00 - 13290:00

to something like chat GPT today uh and

## 13290:00 - 13340:00

give it tasks like I need you to read

## 13340:00 - 13365:00

these a million documents for me and

## 13365:00 - 13395:00

tell me if there's any evidence of fraud

## 13395:00 - 13420:00

happening in this company and then

## 13420:00 - 13445:00

within a couple of hours it's like I've

## 13445:00 - 13480:00

read all the documents here's what the

## 13480:00 - 13515:00

summary is or summarize documents or do

## 13515:00 - 13545:00

legal research and put together a whole

## 13545:00 - 13575:00

memo after researching you know hundreds

## 13575:00 - 13610:00

or thousands of cases answering the

## 13610:00 - 13650:00

lawyer's initial research question and

## 13650:00 - 13675:00

and so in that sense it was this like

## 13675:00 - 13710:00

really powerful extension of the

## 13710:00 - 13730:00

workforce of these law firms that was

## 13730:00 - 13775:00

the concept from the beginning and we

## 13775:00 - 13815:00

made an very early initial version of it

## 13815:00 - 13845:00

and we started because we couldn't you

## 13845:00 - 13870:00

know under our agreement with open AI we

## 13870:00 - 13890:00

could not be public about this product

## 13890:00 - 13925:00

but they did let us extend the NDA to a

## 13925:00 - 13955:00

handful of our customers and so we

## 13955:00 - 13990:00

started having our customers use it

## 13990:00 - 14045:00

and so you know for months before gb4

## 14045:00 - 14085:00

was launched publicly we had a number of

## 14085:00 - 14120:00

law firms un like they had no idea

## 14120:00 - 14140:00

they're using GPT for but they were like

## 14140:00 - 14170:00

seeing something really special right

## 14170:00 - 14205:00

this is actually even before chat GPT so

## 14205:00 - 14245:00

they this is their first ever experience

## 14245:00 - 14280:00

talking to this Godlike feeling you know

## 14280:00 - 14310:00

AI that was all of a sudden doing these

## 14310:00 - 14355:00

tasks that would take me when I

## 14355:00 - 14380:00

practiced like a whole day and it's

## 14380:00 - 14420:00

being done in a minute and a half right

## 14420:00 - 14465:00

and and so as you might imagine like it

## 14465:00 - 14500:00

was it was nuts I mean first of all the

## 14500:00 - 14525:00

whole company all 120 of us did not

## 14525:00 - 14550:00

sleep for those you know months before

## 14550:00 - 14580:00

gbd4 was like publicly launch therefore

## 14580:00 - 14610:00

could publicly launch the product we

## 14610:00 - 14640:00

felt like we had this amazing

## 14640:00 - 14665:00

opportunity to run far ahead of the

## 14665:00 - 14685:00

market something really beautiful

## 14685:00 - 14710:00

happens when everybody's working super

## 14710:00 - 14745:00

super hard which is you iterate so

## 14745:00 - 14785:00

quickly past and actually I I still see

## 14785:00 - 14810:00

some companies out there they're stuck

## 14810:00 - 14845:00

where we were in the first month of

## 14845:00 - 14895:00

seeing gbd4 right um and I think it's

## 14895:00 - 14915:00

because they're just not like as

## 14915:00 - 14965:00

intensely focused and engaged as as we

## 14965:00 - 15010:00

were were able to be during those like

## 15010:00 - 15040:00

couple like about 6 months or so before

## 15040:00 - 15080:00

the public launch of gbd4 you kind of uh

## 15080:00 - 15110:00

to do this transition you had to shake

## 15110:00 - 15135:00

the company you kind of went into deep

## 15135:00 - 15170:00

founder mode because there was a lot of

## 15170:00 - 15205:00

uh push back from employees I like oh

## 15205:00 - 15245:00

this thing was working why should we go

## 15245:00 - 15275:00

into throw ourselves into the deep end

## 15275:00 - 15325:00

of AI and tell us about that founder

## 15325:00 - 15360:00

mode moment for you and so first of all

## 15360:00 - 15390:00

like this is especially true you running

## 15390:00 - 15420:00

a business for 10 years because they've

## 15420:00 - 15455:00

seen you wander through that Maze and

## 15455:00 - 15490:00

and bump it to dead ends and a lot of

## 15490:00 - 15530:00

those folks have been there for uh most

## 15530:00 - 15575:00

or all that time watching you know me as

## 15575:00 - 15595:00

the founder saying we're definitely

## 15595:00 - 15610:00

going this direction it's definitely

## 15610:00 - 15665:00

going to work and sometimes it doesn't

## 15665:00 - 15685:00

and you only get so many of those with

## 15685:00 - 15730:00

employees right so this was maybe my

## 15730:00 - 15760:00

last one that I had with some of these

## 15760:00 - 15790:00

folks and they're like here Jake goes

## 15790:00 - 15815:00

again with this crazy new technology and

## 15815:00 - 15850:00

some idea we're gonna invest deeply in

## 15850:00 - 15890:00

and and yeah it took some some a job to

## 15890:00 - 15925:00

convince people and if you imagine like

## 15925:00 - 15950:00

what some of the different roles are if

## 15950:00 - 15975:00

you're in the go to market role if

## 15975:00 - 16010:00

you're if you're selling or marketing a

## 16010:00 - 16050:00

product and we're making you know we're

## 16050:00 - 16090:00

growing 70 80% year-over-year we're

## 16090:00 - 16120:00

between $15 and $20 million in ARR

## 16120:00 - 16155:00

things weren't like terrible right um

## 16155:00 - 16185:00

that's great yeah we're great yeah we

## 16185:00 - 16220:00

but like so they were like what why are

## 16220:00 - 16255:00

we even the board you know some of the

## 16255:00 - 16280:00

members like I get this immediately some

## 16280:00 - 16335:00

of them had to be persuaded right um and

## 16335:00 - 16360:00

about the founder mode moment like one

## 16360:00 - 16405:00

thing that really worked for me is uh I

## 16405:00 - 16435:00

led the way through example I built the

## 16435:00 - 16475:00

first version of it myself um wow even

## 16475:00 - 16505:00

with 120 person company with like a

## 16505:00 - 16540:00

whole bunch of Engineers and lawyers and

## 16540:00 - 16585:00

stuff like mhm before that you like

## 16585:00 - 16615:00

opened up your like IDE and actually

## 16615:00 - 16640:00

built the thing yourself oh yeah and

## 16640:00 - 16695:00

part of it was uh the NDA only extended

## 16695:00 - 16720:00

at first to me and my co-founder that

## 16720:00 - 16755:00

was it that was a blessing though it it

## 16755:00 - 16795:00

turned out to be like perfect and even

## 16795:00 - 16830:00

after the NDA got extended a little bit

## 16830:00 - 16855:00

we kept it pretty small at first for the

## 16855:00 - 16900:00

first like you know little bit of time I

## 16900:00 - 16930:00

made my mind within 48 Hours whole is

## 16930:00 - 16950:00

going to do this but we actually only

## 16950:00 - 16970:00

told the company I think a week and a

## 16970:00 - 16995:00

half afterward first got access during

## 16995:00 - 17020:00

that week and a half like we built the

## 17020:00 - 17045:00

very first version like prototype

## 17045:00 - 17085:00

version of this and and again I I won't

## 17085:00 - 17105:00

I'll never forget this the timing is

## 17105:00 - 17135:00

just so funny like we saw it on like a

## 17135:00 - 17165:00

Friday we had it all weekend long we're

## 17165:00 - 17205:00

working with it and then Monday was an

## 17205:00 - 17235:00

executive offsite where everybody came

## 17235:00 - 17265:00

all my Executives came and they expected

## 17265:00 - 17285:00

we're we're going to be talking about

## 17285:00 - 17300:00

how we're going to hit our sales Target

## 17300:00 - 17335:00

for the next quarter how and it's like

## 17335:00 - 17365:00

guys we're talking about none of that

## 17365:00 - 17390:00

you know we are talking about something

## 17390:00 - 17410:00

totally different right now let me show

## 17410:00 - 17450:00

you something on my laptop you know uh

## 17450:00 - 17475:00

so yeah I I built the first version

## 17475:00 - 17505:00

myself but going through that process me

## 17505:00 - 17525:00

and and and then a handful of other

## 17525:00 - 17580:00

people I think was really helpful and we

## 17580:00 - 17605:00

also brought in customers early and that

## 17605:00 - 17630:00

helped convince a lot of people as soon

## 17630:00 - 17665:00

as like a skeptical sales or marketing

## 17665:00 - 17695:00

or whatever person or even an engineer

## 17695:00 - 17740:00

was on the other line end of a zoom

## 17740:00 - 17815:00

call uh where um a customer was was

## 17815:00 - 17840:00

reacting to the product in real time and

## 17840:00 - 17865:00

giving us their honest reactions and

## 17865:00 - 17905:00

like seeing the look on their face again

## 17905:00 - 17925:00

you have to imagine it's almost hard to

## 17925:00 - 17945:00

imagine that the world was like pre-

## 17945:00 - 17975:00

chat GPT but then there some of these

## 17975:00 - 18000:00

people were seeing that that exact idea

## 18000:00 - 18050:00

for the first time and they were they

## 18050:00 - 18080:00

were just blown away and that really

## 18080:00 - 18110:00

changed Minds quickly I mean we saw

## 18110:00 - 18125:00

people go through like existential

## 18125:00 - 18155:00

crisises live you know on Zoom calls

## 18155:00 - 18180:00

like oh my God you see their expression

## 18180:00 - 18225:00

change exactly in all kinds of ways it's

## 18225:00 - 18260:00

like what am I going to do lot the very

## 18260:00 - 18280:00

common reaction amongst the senior

## 18280:00 - 18300:00

attorneys we showed it to was like well

## 18300:00 - 18335:00

that got up retir soon like you know i'

## 18335:00 - 18365:00

have to deal with

## 18365:00 - 18415:00

this and some of this was um really

## 18415:00 - 18485:00

driven by GPD 4 coming out like you had

## 18485:00 - 18520:00

access to three you had access even to

## 18520:00 - 18550:00

two I think we had access we were we

## 18550:00 - 18590:00

were in a close relationship again with

## 18590:00 - 18615:00

a lot of the labs but including open ey

## 18615:00 - 18660:00

and they kept on showing us stuff kind

## 18660:00 - 18705:00

of early on in its development and

## 18705:00 - 18720:00

they're like well can you build

## 18720:00 - 18750:00

something with this for legal and every

## 18750:00 - 18800:00

time we're like no this sucks like you

## 18800:00 - 18835:00

know by by time we got to three and 3.5

## 18835:00 - 18865:00

it was like okay well this is plausible

## 18865:00 - 18905:00

sounding English and sounds kind of like

## 18905:00 - 18940:00

a lawyer so kudos for that but it is

## 18940:00 - 18975:00

just making stuff up wildly like we just

## 18975:00 - 19005:00

didn't it's very hard to connect it to a

## 19005:00 - 19045:00

real use case especially in legal where

## 19045:00 - 19065:00

it's so important that you actually get

## 19065:00 - 19095:00

the facts right the you can't

## 19095:00 - 19145:00

hallucinate um you can't even you know

## 19145:00 - 19190:00

make the wrong kinds of assumptions and

## 19190:00 - 19230:00

we had to do a lot of work with those

## 19230:00 - 19255:00

earlier models to even get them close to

## 19255:00 - 19280:00

usable and they just weren weren't

## 19280:00 - 19315:00

really I mean like one one like totem or

## 19315:00 - 19355:00

like one example along the way is when

## 19355:00 - 19415:00

gbd 3.5 came out the study was run um

## 19415:00 - 19470:00

and it showed that gbd 3.5 got a 10 10th

## 19470:00 - 19500:00

percentile on the bar passage right so

## 19500:00 - 19525:00

like it did better than some people

## 19525:00 - 19555:00

actually but the 10% of them yeah

## 19555:00 - 19570:00

probably the ones who just filling out

## 19570:00 - 19620:00

randomly basically um when we got early

## 19620:00 - 19645:00

X gd4 we're like let's run the study

## 19645:00 - 19675:00

again too and we work with open AI we're

## 19675:00 - 19705:00

like we going to confirm this this test

## 19705:00 - 19730:00

is not in the training set and it wasn't

## 19730:00 - 19765:00

totally new test to it and the test we

## 19765:00 - 19805:00

ran it did better than 90% of the test

## 19805:00 - 19830:00

takers right so it's like a big

## 19830:00 - 19870:00

difference and and also we started

## 19870:00 - 19900:00

runting some tests like okay here's like

## 19900:00 - 19925:00

four or five cases to

## 19925:00 - 19975:00

read um using those cases write a memo

## 19975:00 - 20010:00

responding to this question and we we

## 20010:00 - 20055:00

did a lot of prompt work to get it to

## 20055:00 - 20085:00

essentially just do it accurately to

## 20085:00 - 20140:00

cite the actual things in the in context

## 20140:00 - 20175:00

uh that we gave it and not make things

## 20175:00 - 20210:00

up and we're like okay well this is very

## 20210:00 - 20245:00

different than we saw before so is is a

## 20245:00 - 20270:00

big moment for us and and honestly I'm

## 20270:00 - 20305:00

not sure what the mindset was of the the

## 20305:00 - 20335:00

researchers we were working with but it

## 20335:00 - 20365:00

almost felt like by the time we were

## 20365:00 - 20395:00

having that meeting it felt like one of

## 20395:00 - 20430:00

those other meetings we' had in the past

## 20430:00 - 20450:00

where we were getting ready to say like

## 20450:00 - 20485:00

this this is not going to work for legal

## 20485:00 - 20525:00

keep on trying and I think they saw us

## 20525:00 - 20550:00

go through maybe some form of the

## 20550:00 - 20580:00

existential crisis on that call that our

## 20580:00 - 20615:00

customers did we were like oh wait this

## 20615:00 - 20665:00

is super super super different I guess

## 20665:00 - 20710:00

you know today we have 01 we have you

## 20710:00 - 20760:00

know chain of thoughts reasoning um I

## 20760:00 - 20795:00

think a lot of people look at it as it's

## 20795:00 - 20840:00

not merely the text itself but also the

## 20840:00 - 20875:00

instructions that lead up to you know

## 20875:00 - 20920:00

the workflow but you know way at the

## 20920:00 - 20960:00

beginning nobody knew any of this stuff

## 20960:00 - 20995:00

how did you start you had your sort of

## 20995:00 - 21030:00

tests that you had written for previous

## 21030:00 - 21070:00

versions of the model they outperformed

## 21070:00 - 21095:00

but then there's this moment where you

## 21095:00 - 21130:00

say okay well now it's something but

## 21130:00 - 21175:00

what do we do next and how do we do it

## 21175:00 - 21205:00

so the process that we started with then

## 21205:00 - 21230:00

it's actually not too dissimilar to what

## 21230:00 - 21265:00

we're doing today it started with a

## 21265:00 - 21285:00

question of like okay well what problem

## 21285:00 - 21315:00

are we trying to solve for the user

## 21315:00 - 21365:00

right the user wants to do research uh

## 21365:00 - 21400:00

legal research um so and they want like

## 21400:00 - 21425:00

a memo answering their question with

## 21425:00 - 21450:00

citations to the original source so like

## 21450:00 - 21470:00

that's the end result and then we're

## 21470:00 - 21510:00

like well how do we go from that end

## 21510:00 - 21545:00

result like working backwards almost

## 21545:00 - 21595:00

what would it take to get there and what

## 21595:00 - 21645:00

ends up happening a lot uh with the

## 21645:00 - 21665:00

things that we built for coals we call

## 21665:00 - 21710:00

them skills which felt very unique in at

## 21710:00 - 21730:00

the time I think a lot of companies Now

## 21730:00 - 21775:00

call their AI capability skills so when

## 21775:00 - 21815:00

you're building these skills um it turns

## 21815:00 - 21860:00

out it usually takes a lot of work to go

## 21860:00 - 21890:00

from like say the customer inputs

## 21890:00 - 21920:00

something say like a set of documents or

## 21920:00 - 21950:00

a question or what have you to the end

## 21950:00 - 21985:00

result that they're looking for

## 21985:00 - 22020:00

and the way that we thought about it was

## 22020:00 - 22050:00

how would the best attorney in the world

## 22050:00 - 22100:00

approach this problem and so in the case

## 22100:00 - 22140:00

of research for example the best

## 22140:00 - 22175:00

attorney would you know get the request

## 22175:00 - 22230:00

save from a partner and then break that

## 22230:00 - 22255:00

request down into like actual search

## 22255:00 - 22285:00

queries that run against these these

## 22285:00 - 22330:00

platforms and sometimes they use special

## 22330:00 - 22360:00

search syntax it looks actually proba

## 22360:00 - 22395:00

like SQL almost right so like from the

## 22395:00 - 22415:00

English language query you have to break

## 22415:00 - 22435:00

it down to these different kind of

## 22435:00 - 22455:00

search queries maybe a dozen different

## 22455:00 - 22505:00

search queries you being really diligent

## 22505:00 - 22530:00

and then um they'd execute the search

## 22530:00 - 22580:00

queries against these databases of law

## 22580:00 - 22610:00

they come back with say like 100 results

## 22610:00 - 22645:00

each and then they you know the most

## 22645:00 - 22675:00

diligent best attorney would sit down

## 22675:00 - 22710:00

and just read every single one of these

## 22710:00 - 22735:00

results that come back all the the case

## 22735:00 - 22770:00

law statutes regulations and you start

## 22770:00 - 22820:00

to do things like make notes and uh

## 22820:00 - 22855:00

summarize and kind of compile like an

## 22855:00 - 22885:00

outline of what your response might be

## 22885:00 - 22915:00

like line by line or paragraph by

## 22915:00 - 22960:00

paragraph actually yeah 100% And you

## 22960:00 - 22990:00

start like just taking out those like

## 22990:00 - 23005:00

insights you're getting from what you're

## 23005:00 - 23040:00

reading and then finally based on all

## 23040:00 - 23070:00

that work and all the citations you've

## 23070:00 - 23105:00

gathered Etc then finally you put

## 23105:00 - 23140:00

together your your you know research

## 23140:00 - 23175:00

memo and so we're like okay well each

## 23175:00 - 23200:00

one of those steps along the way for the

## 23200:00 - 23230:00

vast majority of them those were

## 23230:00 - 23255:00

impossible to accomplish with previous

## 23255:00 - 23280:00

technology but now they're they're

## 23280:00 - 23320:00

prompts think step by step yeah think

## 23320:00 - 23345:00

step by step yeah exactly but we

## 23345:00 - 23370:00

actually broke it down each each you

## 23370:00 - 23405:00

know so getting to the final result may

## 23405:00 - 23435:00

be a dozen or two dozen different

## 23435:00 - 23470:00

individual prompts Each of which might

## 23470:00 - 23505:00

by the way be thinking step by step them

## 23505:00 - 23550:00

themselves but um and for the for each

## 23550:00 - 23585:00

of those prompts you know as part of

## 23585:00 - 23615:00

this like chain of of actions you take

## 23615:00 - 23655:00

to get to the final result we had a very

## 23655:00 - 23700:00

clear sense of what good looks like and

## 23700:00 - 23725:00

we were able you know we had a Ser

## 23725:00 - 23755:00

series like a battery of tests before

## 23755:00 - 23790:00

but this got way more intense where we'

## 23790:00 - 23830:00

write at first maybe a few dozen tests

## 23830:00 - 23850:00

and then a few hundred and a few

## 23850:00 - 23870:00

thousand for every single one of those

## 23870:00 - 23935:00

PRS so you know if if the the the job to

## 23935:00 - 23960:00

be done in the very beginning of this

## 23960:00 - 24005:00

research process for example is taking

## 24005:00 - 24025:00

the English language query and breaking

## 24025:00 - 24065:00

it down into search queries we had a a

## 24065:00 - 24085:00

very clear sense of what good search

## 24085:00 - 24105:00

queries look like and wrote like a gold

## 24105:00 - 24140:00

standard answers for giving this input

## 24140:00 - 24165:00

this is what the outpa looks like right

## 24165:00 - 24210:00

and so our prompt Engineers um and I was

## 24210:00 - 24230:00

one of them at the very beginning we all

## 24230:00 - 24255:00

just kind of in it together we're

## 24255:00 - 24280:00

writing these English language prompts

## 24280:00 - 24310:00

to try to you know write the test first

## 24310:00 - 24335:00

basically and wrote These English

## 24335:00 - 24375:00

language prompts to try to get it so of

## 24375:00 - 24420:00

1,200 times they got the right answer 1,

## 24420:00 - 24460:00

1,199 times or what have you so sort of

## 24460:00 - 24495:00

like um test driven development oh yeah

## 24495:00 - 24530:00

really approach from doing software

## 24530:00 - 24555:00

engineering to to to prompt that's

## 24555:00 - 24585:00

exactly right and and the funny thing is

## 24585:00 - 24600:00

I never really believed in test driven

## 24600:00 - 24630:00

development before prompting like I was

## 24630:00 - 24660:00

like the code works it doesn't it's fine

## 24660:00 - 24675:00

like you'll see it when you but like

## 24675:00 - 24700:00

with prompting actually think becomes

## 24700:00 - 24745:00

even more important because of the kind

## 24745:00 - 24790:00

of like nature of these llms they might

## 24790:00 - 24835:00

go in Crazy directions unexpectedly and

## 24835:00 - 24880:00

so you know you might very easily add in

## 24880:00 - 24900:00

a set of instructions to solve one

## 24900:00 - 24920:00

problem you're seeing with these sets of

## 24920:00 - 24945:00

tests and then to break something with

## 24945:00 - 24985:00

these sets of tests so so that that

## 24985:00 - 25020:00

exact kind of theory of test development

## 25020:00 - 25060:00

applies you know 10x more I'd say in the

## 25060:00 - 25095:00

world of prompting there's a lot of uh

## 25095:00 - 25130:00

sort of the naysay are saying that a lot

## 25130:00 - 25160:00

of companies are just building GP

## 25160:00 - 25205:00

rappers and there's not a lot of Ip

## 25205:00 - 25240:00

getting built but it's actually there's

## 25240:00 - 25275:00

a lot of finesse to how you explain all

## 25275:00 - 25310:00

of this like can you tell us about all

## 25310:00 - 25345:00

of that and how much more there's to be

## 25345:00 - 25380:00

built oh yeah I I mean I think the thing

## 25380:00 - 25405:00

is when you're actually trying to solve

## 25405:00 - 25430:00

a problem for a customer and actually

## 25430:00 - 25460:00

doing the job in our case of like what a

## 25460:00 - 25485:00

young associate it might do and do it

## 25485:00 - 25520:00

really well there are many layers of

## 25520:00 - 25550:00

things you have to add in to actually

## 25550:00 - 25585:00

get the job done and by the time you

## 25585:00 - 25625:00

like add that all up you're not like a

## 25625:00 - 25675:00

GPT rapper you're a full application

## 25675:00 - 25705:00

that may include in our case proprietary

## 25705:00 - 25740:00

data sets like the law itself and our

## 25740:00 - 25760:00

annotations to the law that we added

## 25760:00 - 25805:00

automatically it may include um

## 25805:00 - 25835:00

connections into customer databases in

## 25835:00 - 25870:00

our case in legal they have these very

## 25870:00 - 25900:00

specific legal specific document

## 25900:00 - 25945:00

Management Systems um you know so

## 25945:00 - 25970:00

connecting into those is like very

## 25970:00 - 26020:00

important um it may include uh something

## 26020:00 - 26050:00

as subtle as like how well you OCR and

## 26050:00 - 26070:00

like what OCR programs you use and how

## 26070:00 - 26105:00

you set those up when you're doing that

## 26105:00 - 26125:00

task of you know one of the tasks that

## 26125:00 - 26160:00

the co counsil does for example is

## 26160:00 - 26210:00

reviewing large sets of documents once

## 26210:00 - 26230:00

you start working a lot of documents you

## 26230:00 - 26255:00

see like stuff there handw ring all over

## 26255:00 - 26300:00

it and they're like tilted in the scan

## 26300:00 - 26330:00

and there's this crazy thing that they

## 26330:00 - 26355:00

do in law where they print four pages on

## 26355:00 - 26395:00

one page to save like room and LR is

## 26395:00 - 26420:00

going to read it directly across but

## 26420:00 - 26455:00

actually goes you know 1 two 3 four so

## 26455:00 - 26480:00

by the time you've dealt with like all

## 26480:00 - 26520:00

the edge cases frankly uh not even

## 26520:00 - 26540:00

before you hit the the large language

## 26540:00 - 26565:00

model like everything else up to the

## 26565:00 - 26605:00

large language model um there might be

## 26605:00 - 26625:00

dozens of things you buil into your

## 26625:00 - 26650:00

application to actually make it work and

## 26650:00 - 26685:00

work well and then you get to the

## 26685:00 - 26715:00

prompting piece and writing out tests

## 26715:00 - 26745:00

and very specific prompts and and the

## 26745:00 - 26795:00

strategy for how you break down you know

## 26795:00 - 26845:00

uh a big problem into step by step by

## 26845:00 - 26905:00

step kind of thinking um and and how you

## 26905:00 - 26925:00

feed in the information how you format

## 26925:00 - 26965:00

that information the right way um all of

## 26965:00 - 27025:00

that also becomes like you know your IP

## 27025:00 - 27055:00

and it's very hard to replicate very

## 27055:00 - 27075:00

hard to build and therefore very hard to

## 27075:00 - 27100:00

replicate which is all the business

## 27100:00 - 27135:00

logic which is all even all the very

## 27135:00 - 27175:00

successful SAS companies with very

## 27175:00 - 27205:00

specific domain you need very very

## 27205:00 - 27260:00

custom esoteric Niche Integrations like

## 27260:00 - 27320:00

plug into this esoteric law database

## 27320:00 - 27345:00

yeah absolutely two things I think about

## 27345:00 - 27370:00

it all the time it's like basically all

## 27370:00 - 27405:00

SAS for a while was just like a SQL

## 27405:00 - 27440:00

rapper right like if you think about

## 27440:00 - 27470:00

like very successful companies like

## 27470:00 - 27500:00

Salesforce they built that business

## 27500:00 - 27540:00

logic around basically just databases

## 27540:00 - 27565:00

and connections between like tables and

## 27565:00 - 27605:00

a database and sometimes bridging that

## 27605:00 - 27650:00

gap between um something that like

## 27650:00 - 27675:00

either a very technical person can do

## 27675:00 - 27700:00

but most people can't and making

## 27700:00 - 27745:00

accessible or um bridging that gap

## 27745:00 - 27775:00

between that almost works like you can

## 27775:00 - 27810:00

do a lot of cool Demos in chat GPT

## 27810:00 - 27850:00

without building a line of code but that

## 27850:00 - 27890:00

almost works and works you know 70% of

## 27890:00 - 27915:00

the time but going to 100% of the time

## 27915:00 - 27950:00

is a very different kind of task and

## 27950:00 - 28005:00

people will pay $20 a month for the 70%

## 28005:00 - 28045:00

and maybe $500 or $1,000 a month for

## 28045:00 - 28060:00

something that actually works depending

## 28060:00 - 28090:00

on the use case right so there's a lot

## 28090:00 - 28145:00

of value gained going that last mile or

## 28145:00 - 28175:00

100 miles whatever it is yeah can you

## 28175:00 - 28220:00

talk about how you went from 70% to 100%

## 28220:00 - 28240:00

because I think the other knock on this

## 28240:00 - 28275:00

technology that we hear a lot is like oh

## 28275:00 - 28310:00

these LMS hallucinate too much they're

## 28310:00 - 28350:00

not accurate enough for real world use

## 28350:00 - 28390:00

but as you said earlier like the use

## 28390:00 - 28420:00

case that you're working on is a mission

## 28420:00 - 28460:00

critical use case there's like a lot at

## 28460:00 - 28505:00

stake if the agent gives bad information

## 28505:00 - 28535:00

to lawyers who are working on important

## 28535:00 - 28575:00

court cases how did you make it accurate

## 28575:00 - 28610:00

enough for lawyers who are conservative

## 28610:00 - 28650:00

by nature to trusted this test driven

## 28650:00 - 28665:00

development framework first of all goes

## 28665:00 - 28710:00

a long way because you can start seeing

## 28710:00 - 28740:00

you know patterns and why it's making a

## 28740:00 - 28775:00

mistake and then you add instructions

## 28775:00 - 28800:00

against that pattern and then sometimes

## 28800:00 - 28840:00

it still doesn't you know do the right

## 28840:00 - 28870:00

thing and then you kind of really ask

## 28870:00 - 28900:00

yourself okay well was I being super

## 28900:00 - 28940:00

clear in my instructions uh you know am

## 28940:00 - 28980:00

I including information doesn't you know

## 28980:00 - 29005:00

it doesn't it shouldn't see or too much

## 29005:00 - 29030:00

or too little information for it to

## 29030:00 - 29065:00

really get the full context and usually

## 29065:00 - 29100:00

like these things are pretty intelligent

## 29100:00 - 29155:00

and so usually you can kind of root

## 29155:00 - 29195:00

cause why you're failing certain tests

## 29195:00 - 29220:00

and then build to a place where you're

## 29220:00 - 29245:00

actually passing those tests and just

## 29245:00 - 29285:00

getting it right you know and and one of

## 29285:00 - 29310:00

the things we learned is if it after

## 29310:00 - 29345:00

passes frankly even like 100 tests the

## 29345:00 - 29375:00

odd that it will do on any random

## 29375:00 - 29415:00

distribution of like user inputs the

## 29415:00 - 29450:00

next 100,000 100% accurately is like

## 29450:00 - 29480:00

very high one of the things that strikes

## 29480:00 - 29525:00

me that is tricky like many Founders we

## 29525:00 - 29555:00

work with are very tempted to just raw

## 29555:00 - 29610:00

dog it yeah there's like no evales no

## 29610:00 - 29650:00

test driven we're just like Vibes only

## 29650:00 - 29695:00

prompt engineering and maybe I mean you

## 29695:00 - 29735:00

switched over to this uh very quickly

## 29735:00 - 29775:00

then like was it just obvious from the

## 29775:00 - 29800:00

beginning you're like we just can't do

## 29800:00 - 29830:00

it that other way we should not raw dog

## 29830:00 - 29860:00

any of these prompts yeah I think I

## 29860:00 - 29890:00

think the the biggest thing first of all

## 29890:00 - 29920:00

depends on the use case for a lot of

## 29920:00 - 29940:00

things that we were working on For

## 29940:00 - 29970:00

Better or For Worse there was was a

## 29970:00 - 29995:00

right answer and if you get the wrong

## 29995:00 - 30030:00

answer lawyers are not going to be happy

## 30030:00 - 30055:00

about it you know I had been a lawyer

## 30055:00 - 30080:00

myself but also been s lawyers for a

## 30080:00 - 30110:00

decade and every time we made the

## 30110:00 - 30140:00

smallest mistake in anything that we did

## 30140:00 - 30180:00

we heard about it immediately right and

## 30180:00 - 30220:00

so I had that voice in my head maybe as

## 30220:00 - 30265:00

I was going through this process um and

## 30265:00 - 30285:00

that that how was the learning from the

## 30285:00 - 30320:00

10 years of slogging through pre- LMS

## 30320:00 - 30360:00

you're like no it has to be 100% oh yeah

## 30360:00 - 30385:00

oh yeah that's probably true of way more

## 30385:00 - 30420:00

domains than we realize actually it

## 30420:00 - 30450:00

could be um because and the other thing

## 30450:00 - 30475:00

that we we're thinking about a lot is

## 30475:00 - 30495:00

you can lose faith in these things

## 30495:00 - 30530:00

really quickly right you have one bad

## 30530:00 - 30555:00

experience especially if it's your first

## 30555:00 - 30585:00

bad your first experience is bad and

## 30585:00 - 30620:00

you're like you know maybe I'll check on

## 30620:00 - 30645:00

this AI stuff a year from now especially

## 30645:00 - 30665:00

if you're like a busy lawyer not a

## 30665:00 - 30695:00

technologist so we we knew you had to

## 30695:00 - 30745:00

make that first encounter the first week

## 30745:00 - 30775:00

really really work for the lawyer or

## 30775:00 - 30790:00

else they're not going to invest in it

## 30790:00 - 30850:00

deeply so let's talk a bit about open AI

## 30850:00 - 30915:00

01 because it is very different model I

## 30915:00 - 30965:00

mean up to this point with gbd4 and all

## 30965:00 - 31015:00

that previous generation the analogy in

## 31015:00 - 31060:00

terms of the intelligence is sort of the

## 31060:00 - 31085:00

kind of system one thinking and the

## 31085:00 - 31150:00

Daniel canaman type of uh intelligence

## 31150:00 - 31175:00

right he has this whole economic theory

## 31175:00 - 31205:00

want the Nobel priz around it system one

## 31205:00 - 31250:00

thinking is just very fast is kind of

## 31250:00 - 31280:00

these decisions that humans make very

## 31280:00 - 31320:00

intuitively and based on patterns and LM

## 31320:00 - 31355:00

are fantastic at that but they're

## 31355:00 - 31400:00

terrible at the executive function

## 31400:00 - 31415:00

because what I'm hearing with all the

## 31415:00 - 31445:00

stuff that you're describing is kind of

## 31445:00 - 31485:00

you're just giving the the llm like

## 31485:00 - 31520:00

executive function is like how do you

## 31520:00 - 31545:00

think right how do I manage you it's

## 31545:00 - 31575:00

really that slower

## 31575:00 - 31620:00

thinking and I think aan is exciting we

## 31620:00 - 31645:00

haven't seen things built yet because it

## 31645:00 - 31705:00

just got announced few days ago right I

## 31705:00 - 31740:00

think it's getting to that system to

## 31740:00 - 31770:00

thinking and I think this is has been a

## 31770:00 - 31805:00

big area of research which I saw a lot

## 31805:00 - 31845:00

in uh news a year ago where a lot of the

## 31845:00 - 31885:00

researchers were excited to unlock this

## 31885:00 - 31920:00

because this is the missing piece to our

## 31920:00 - 31950:00

AGI let's talk about what are your

## 31950:00 - 31990:00

thoughts on one and how this changes so

## 31990:00 - 32025:00

so first of all I think 's a very

## 32025:00 - 32070:00

impressive model um like with other

## 32070:00 - 32100:00

things we gave it the kinds of tests

## 32100:00 - 32145:00

that we knew were failing and the degree

## 32145:00 - 32170:00

of it's not just math degree of

## 32170:00 - 32205:00

thoroughness precision intelligence

## 32205:00 - 32235:00

applied to some of these questions and

## 32235:00 - 32255:00

sometimes it's the stuff that you

## 32255:00 - 32280:00

wouldn't wouldn't expect you need a

## 32280:00 - 32310:00

super smart model to do like in one of

## 32310:00 - 32350:00

the tests that we run we give it uh

## 32350:00 - 32400:00

lawyers real legal brief but we edited

## 32400:00 - 32440:00

very slightly some of uh that lawyer's

## 32440:00 - 32480:00

quotations to the case to make it a

## 32480:00 - 32505:00

wrong quotation or wrong kind of

## 32505:00 - 32530:00

summarization of his case so he this

## 32530:00 - 32565:00

like 40 page legal brief you alter

## 32565:00 - 32590:00

things with just adding the word like

## 32590:00 - 32615:00

not can change the meaning of something

## 32615:00 - 32655:00

entirely right and then we give the full

## 32655:00 - 32700:00

text of the case as well to the AI and

## 32700:00 - 32735:00

we say well what did you know what did

## 32735:00 - 32750:00

the

## 32750:00 - 32785:00

lawyer uh get wrong about this case of

## 32785:00 - 32830:00

anything and literally every llm before

## 32830:00 - 32845:00

that would be like nothing it's

## 32845:00 - 32875:00

perfectly right and it's just not a

## 32875:00 - 32935:00

precise thinker about some of the the

## 32935:00 - 32965:00

very nuanced things that we altered

## 32965:00 - 32985:00

about the brief to make it slightly

## 32985:00 - 33015:00

wrong and then one got gets it like

## 33015:00 - 33045:00

immediately like you said like it thinks

## 33045:00 - 33065:00

actually for a while like it sits there

## 33065:00 - 33080:00

for a minute you're like is this

## 33080:00 - 33115:00

anything thing on you know like but then

## 33115:00 - 33155:00

then it starts answering and it's like

## 33155:00 - 33185:00

oh well you know changed an and to a

## 33185:00 - 33225:00

neither nor so those are the kinds of

## 33225:00 - 33250:00

tests that you kind of expect even

## 33250:00 - 33290:00

frankly earlier AI like LMS to be able

## 33290:00 - 33345:00

to pass but just could not and all of a

## 33345:00 - 33370:00

sudden o1 is even doing these things

## 33370:00 - 33415:00

that take like like precise detail

## 33415:00 - 33445:00

thinking obviously we don't have the

## 33445:00 - 33490:00

internals on o how o1 really works we

## 33490:00 - 33525:00

have you know this broad idea of chain

## 33525:00 - 33590:00

of thoughts seemingly we know that if

## 33590:00 - 33650:00

open AI had a giant Corpus of internal

## 33650:00 - 33690:00

monologue of people thinking through

## 33690:00 - 33735:00

doing things step by step 01 would be

## 33735:00 - 33780:00

even a lot better it sort of rhymes with

## 33780:00 - 33815:00

uh the thing you did to you know put

## 33815:00 - 33855:00

your first uh step on the moon right

## 33855:00 - 33895:00

like you it rhymes with break it down

## 33895:00 - 33940:00

into you know uh chunks where you can

## 33940:00 - 33990:00

get to 100% accuracy instead of just

## 33990:00 - 34020:00

throw it all in the context window and

## 34020:00 - 34055:00

you know maybe magically it will work

## 34055:00 - 34085:00

yeah do you think that that's what's

## 34085:00 - 34110:00

happening then I think there's a good

## 34110:00 - 34145:00

shot that that they've had you know

## 34145:00 - 34170:00

maybe change what their contractors are

## 34170:00 - 34215:00

doing instead of just doing you know

## 34215:00 - 34260:00

input in answer out they were doing

## 34260:00 - 34290:00

input in how would I think about solving

## 34290:00 - 34325:00

this problem and then answer out but

## 34325:00 - 34345:00

then it you know the interesting thing

## 34345:00 - 34385:00

is then it's kind of limited by the

## 34385:00 - 34405:00

intelligence of the people writing those

## 34405:00 - 34425:00

instructions and one of the things that

## 34425:00 - 34450:00

we're investigating for what it's worth

## 34450:00 - 34495:00

with o1 is can we prompt it to tell it

## 34495:00 - 34520:00

what to think about during its thinking

## 34520:00 - 34570:00

process and inject like again like we've

## 34570:00 - 34585:00

hired some of the best lawyers in the

## 34585:00 - 34620:00

country how would the some of the best

## 34620:00 - 34635:00

lawyers in the country think about

## 34635:00 - 34670:00

solving this problem and maybe you know

## 34670:00 - 34695:00

we have no conclusive evidence one way

## 34695:00 - 34725:00

or the other yet that this dramatically

## 34725:00 - 34760:00

improves things is so early uh and just

## 34760:00 - 34790:00

just not enough time yet has passed

## 34790:00 - 34810:00

there's a chance that that one of the

## 34810:00 - 34835:00

new prompting techniques with L1 is

## 34835:00 - 34860:00

teaching it not just like how to answer

## 34860:00 - 34880:00

the question what examples of good

## 34880:00 - 34915:00

answers look like but how to think and I

## 34915:00 - 34940:00

think that that's another like really

## 34940:00 - 34985:00

interesting opportunity here is is um

## 34985:00 - 35035:00

injecting domain expertise or um just

## 35035:00 - 35070:00

your own intelligence I'm just so

## 35070:00 - 35130:00

thankful because I think you're sort of

## 35130:00 - 35170:00

sharing the breadcrumbs and you know

## 35170:00 - 35225:00

where there a great many other spaces

## 35225:00 - 35260:00

where this technology is just beginning

## 35260:00 - 35300:00

I mean you go to pretty much any company

## 35300:00 - 35335:00

people have no concept of what's just

## 35335:00 - 35370:00

happened yeah like they actually

## 35370:00 - 35405:00

literally still repeat all of those sort

## 35405:00 - 35445:00

of tired tropes of oh you better be

## 35445:00 - 35475:00

fine-tuning or all the I mean these

## 35475:00 - 35515:00

things are just not connected to like

## 35515:00 - 35545:00

what we're seeing day-to-day with

## 35545:00 - 35585:00

startups and Founders trying to create

## 35585:00 - 35620:00

things for users what I'm kind of glad

## 35620:00 - 35660:00

for is that we get to actually share

## 35660:00 - 35700:00

this news like this knowledge cuz like

## 35700:00 - 35725:00

even the things we talked about you know

## 35725:00 - 35770:00

hey you should probably do evals like

## 35770:00 - 35805:00

there's a lot of alpha in getting to

## 35805:00 - 35850:00

100% not just 70% these are sort of the

## 35850:00 - 35880:00

breadcrumbs that will actually go on to

## 35880:00 - 35920:00

create uh all of the billion dooll

## 35920:00 - 35955:00

companies maybe thousands of them

## 35955:00 - 35985:00

actually we hope so I mean I think that

## 35985:00 - 36005:00

you're about start to see a lot of other

## 36005:00 - 36045:00

fields like law really level up when you

## 36045:00 - 36080:00

don't have to spend you know millions of

## 36080:00 - 36110:00

dollars in six months literally in a

## 36110:00 - 36135:00

basement reading document by document by

## 36135:00 - 36170:00

document right when you when you

## 36170:00 - 36190:00

actually can just get past that and get

## 36190:00 - 36220:00

just the results and now you're thinking

## 36220:00 - 36275:00

strategically and intelligently and the

## 36275:00 - 36305:00

unlock for these companies I mean they

## 36305:00 - 36340:00

currently pay again millions of dollars

## 36340:00 - 36375:00

in salaries for these jobs to be done

## 36375:00 - 36420:00

each of them right so for any company to

## 36420:00 - 36465:00

come out with a AI that can do even % of

## 36465:00 - 36515:00

that the value is like really there and

## 36515:00 - 36540:00

I just want to encourage people to not

## 36540:00 - 36565:00

kind of give up based on those tropes

## 36565:00 - 36585:00

right like oh it hallucinates too much

## 36585:00 - 36620:00

it's too an accurate it's do whatever

## 36620:00 - 36655:00

there's for an example of anything it's

## 36655:00 - 36690:00

like there's a path and you can do it

## 36690:00 - 36720:00

and there's some good news in that uh

## 36720:00 - 36740:00

you know what the jobs aren't going to

## 36740:00 - 36765:00

go away they'll just be more interesting

## 36765:00 - 36800:00

that's what I think yeah well with that

## 36800:00 - 36835:00

we're out of time but Jake thank you so

## 36835:00 - 36855:00

much for being with us thanks for having

## 36855:00 - 36900:00

me see you guys next time

## 36900:00 - 36960:00

[Music]

## 36960:00 - 36990:00

now

## 36990:00+

[Music]

