---
source: https://www.youtube.com/watch?v=0hQJZh_Fzzw
title: NVIDIA's Artifical Intelligence Moat & Origins — With Bryan Catanzaro
author: Alex Kantrowitz
date: 2024-02-28
views: 2706
description: >-
  Bryan Catanzaro is NVIDIA's VP of applied deep learning research.


  Subscribe to Big Technology Podcast wherever you get your podcasts:


  Spotify:  https://spoti.fi/32aZGZx

  Apple:  https://apple.co/3AebxCK

  Etc. https://pod.link/1522960417/ 


  Catanzaro joins Big Technology Podcast to discuss why NVIDIA is building more
  than just chips, examining its software and algorithms that help tech
  companies build and run AI models. Join us for a conversation about how NVIDIA
  sees the world, what's led to its success, and what makes it indispensable. In
  the second half, we discuss how Bryan helped kick off NVIDIA's push into AI,
  from the very start to where it is today.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:35:52.046Z
---

# NVIDIA's Artifical Intelligence Moat & Origins — With Bryan Catanzaro

## 00:00 - 55:00

the Nvidia executive who started its AI

## 55:00 - 90:00

push joins us to talk about what makes

## 90:00 - 135:00

the company so indispensable unpacking

## 135:00 - 175:00

the secrets to its success that's coming

## 175:00 - 220:00

up right after this welcome to Big

## 220:00 - 245:00

technology podcast a show for

## 245:00 - 285:00

cool-headed nuance conversation of the

## 285:00 - 310:00

tech world and Beyond we have a great

## 310:00 - 340:00

conversation for you today we're going

## 340:00 - 400:00

deep inside Nvidia with Brian katanzaro

## 400:00 - 430:00

he's the vice president of Applied deep

## 430:00 - 480:00

learning research at Nvidia and he's

## 480:00 - 505:00

going to be speaking at the company's

## 505:00 - 550:00

forthcoming GTC conference March 18th to

## 550:00 - 605:00

21 in San Jose and his conversation is

## 605:00 - 645:00

going to be specifically on practical a

## 645:00 - 700:00

AI agents that reason and code at scale

## 700:00 - 730:00

so if you're in the area you're thinking

## 730:00 - 760:00

about heading out you can mark that down

## 760:00 - 795:00

let's get to the conversation Brian

## 795:00 - 830:00

welcome to the show thanks I'm glad to

## 830:00 - 875:00

be here great to have you you're kind of

## 875:00 - 905:00

the guy that kicked off this whole AI

## 905:00 - 930:00

push within

## 930:00 - 965:00

Nvidia well you know it took a whole

## 965:00 - 1015:00

company to to transform Nvidia into what

## 1015:00 - 1050:00

it is today so um there's tens of

## 1050:00 - 1080:00

thousands of people that deserve a lot

## 1080:00 - 1135:00

of credit but um I was uh honored to be

## 1135:00 - 1160:00

one of the people that helped Nvidia get

## 1160:00 - 1195:00

started a long time

## 1195:00 - 1235:00

ago exactly so maybe we can get into

## 1235:00 - 1255:00

that in a bit but I first want to talk

## 1255:00 - 1305:00

to you really about what makes Nvidia so

## 1305:00 - 1340:00

indispensable to developers building

## 1340:00 - 1375:00

with AI I mean that's been everything

## 1375:00 - 1415:00

that's been going on recently just comes

## 1415:00 - 1455:00

back to the fact that Nvidia has these

## 1455:00 - 1500:00

capabilities right and I think that a

## 1500:00 - 1535:00

lot of folks hear about it they

## 1535:00 - 1560:00

understand it philosophically we know

## 1560:00 - 1595:00

that Nvidia has the technology and that

## 1595:00 - 1620:00

other competitors have you know have

## 1620:00 - 1655:00

struggled to catch up but let's just

## 1655:00 - 1700:00

focus on Nvidia for a moment what is

## 1700:00 - 1730:00

exactly happening within your company

## 1730:00 - 1765:00

what do you offer that allows anyone

## 1765:00 - 1810:00

that wants to build Ai and then run AI

## 1810:00 - 1845:00

models to do it

## 1845:00 - 1885:00

effectively Nvidia is an accelerated

## 1885:00 - 1925:00

Computing company and wait wait so what

## 1925:00 - 1955:00

does that mean accelerated Computing I

## 1955:00 - 1985:00

hear you guys talk about it all the time

## 1985:00 - 2010:00

we've been talking about it for a long

## 2010:00 - 2035:00

time and the world still doesn't quite

## 2035:00 - 2065:00

understand it so I'm glad to to try to

## 2065:00 - 2130:00

explain it um the idea is that the world

## 2130:00 - 2165:00

faces a lot of computational challenges

## 2165:00 - 2200:00

that can't be solved without faster

## 2200:00 - 2270:00

computers but uh building a computer uh

## 2270:00 - 2300:00

is not enough in order to actually

## 2300:00 - 2345:00

deliver acceleration all of the pieces

## 2345:00 - 2390:00

have to line up and plug together and be

## 2390:00 - 2435:00

fully optimized across the entire stack

## 2435:00 - 2475:00

so that uh people have the chance to do

## 2475:00 - 2500:00

things that they just couldn't do

## 2500:00 - 2550:00

otherwise computationally and AI is a

## 2550:00 - 2580:00

great example of that you know training

## 2580:00 - 2620:00

and deploying uh the awesome generative

## 2620:00 - 2645:00

models that are changing the world right

## 2645:00 - 2680:00

now is extraordinarily computationally

## 2680:00 - 2710:00

intensive it's the biggest computational

## 2710:00 - 2755:00

challenge the world has ever faced and

## 2755:00 - 2815:00

uh the reason that Nvidia is uh is is

## 2815:00 - 2840:00

providing something useful here is

## 2840:00 - 2890:00

because for for decades we've taken on

## 2890:00 - 2940:00

this mission of optimizing the entire

## 2940:00 - 2985:00

stack to build um software algorithms

## 2985:00 - 3045:00

libraries Frameworks compilers systems

## 3045:00 - 3090:00

networking chips the whole thing and

## 3090:00 - 3135:00

optimize them together for the most

## 3135:00 - 3195:00

important workloads uh and and that's AI

## 3195:00 - 3245:00

okay and so when I hear you recite that

## 3245:00 - 3305:00

you know list of different things you do

## 3305:00 - 3335:00

you know the the laying knowledge that

## 3335:00 - 3380:00

would come in with with and hear that

## 3380:00 - 3415:00

like if I've if I'm hearing that for the

## 3415:00 - 3470:00

first time I would say wait a second no

## 3470:00 - 3545:00

Nvidia just does the 100 chip so it's

## 3545:00 - 3570:00

obviously more than that so can you talk

## 3570:00 - 3610:00

a little bit about like people I think

## 3610:00 - 3635:00

you know they might get it wrong that

## 3635:00 - 3665:00

it's just the chip and that's the thing

## 3665:00 - 3700:00

that gets the gets the headlines 20,000

## 3700:00 - 3755:00

to $40,000 Facebook has 350,000 of them

## 3755:00 - 3785:00

by the end of the year that's what

## 3785:00 - 3825:00

people need to run AI but it's it's

## 3825:00 - 3850:00

actually and I think this is the

## 3850:00 - 3890:00

important part the ecosystem it's not

## 3890:00 - 3935:00

just right the the chip but everything

## 3935:00 - 3975:00

around it so just talk about that as you

## 3975:00 - 4005:00

know in layman's terms if you can like

## 4005:00 - 4065:00

what surrounds that chip that Nvidia

## 4065:00 - 4110:00

provides well um there's a there's an

## 4110:00 - 4155:00

entire culture about um what is

## 4155:00 - 4195:00

accelerated Computing we have to be very

## 4195:00 - 4225:00

strategic about what we're going to

## 4225:00 - 4255:00

accelerate U and we have to make

## 4255:00 - 4290:00

decisions years in advance about how

## 4290:00 - 4330:00

we're going to build the software and

## 4330:00 - 4365:00

Hardware that's going to provide this

## 4365:00 - 4405:00

acceleration um I always like to say

## 4405:00 - 4430:00

that accelerated Computing implies

## 4430:00 - 4480:00

decelerated Computing because it's not

## 4480:00 - 4500:00

actually helpful say I'm just going to

## 4500:00 - 4535:00

make a fast computer everybody makes a

## 4535:00 - 4560:00

fast computer right that's the goal of

## 4560:00 - 4600:00

every computer is to be fast so

## 4600:00 - 4635:00

acceleration really is about

## 4635:00 - 4670:00

specialization it's about being able to

## 4670:00 - 4720:00

focus and prioritize and say this is the

## 4720:00 - 4750:00

workload that matters most and I'm going

## 4750:00 - 4805:00

to optimize the entire stack for that

## 4805:00 - 4850:00

workload uh so in order to do that we

## 4850:00 - 4895:00

have an enormous amount of um Hardware

## 4895:00 - 4940:00

software and algorithms that that we're

## 4940:00 - 4965:00

working on in order to enable the

## 4965:00 - 4995:00

community to do things that they could

## 4995:00 - 5035:00

never do before sometimes we like to say

## 5035:00 - 5070:00

that we're building a time machine for

## 5070:00 - 5110:00

scientists and Engineers uh that allows

## 5110:00 - 5160:00

them to see into the future because of

## 5160:00 - 5205:00

the acceleration that comes from our

## 5205:00 - 5250:00

systems so it's interesting because if

## 5250:00 - 5280:00

you think about like a traditional chip

## 5280:00 - 5295:00

company and by the way I might be

## 5295:00 - 5330:00

totally off base on this and correct me

## 5330:00 - 5370:00

if I am

## 5370:00 - 5420:00

but what they do is take you you the

## 5420:00 - 5445:00

manufacturer will buy the chip put it

## 5445:00 - 5480:00

inside let's say their computer right

## 5480:00 - 5515:00

and then build the software around it

## 5515:00 - 5550:00

but you guys also build you not only

## 5550:00 - 5590:00

manufacture the chip but you build the

## 5590:00 - 5615:00

the algorithms and the software that

## 5615:00 - 5655:00

surrounds it so that enables companies

## 5655:00 - 5685:00

to get the most out of it

## 5685:00 - 5735:00

so just three questions on that one is

## 5735:00 - 5765:00

that a right characterization of what

## 5765:00 - 5820:00

you're doing um and

## 5820:00 - 5850:00

then well let's just start with that one

## 5850:00 - 5895:00

I'm not going to yeah I I think so I

## 5895:00 - 5940:00

mean the the core thesis that powers

## 5940:00 - 5975:00

Nvidia is that a chip could never be

## 5975:00 - 6025:00

enough you know um just just the same

## 6025:00 - 6075:00

way that a chip couldn't be enough for

## 6075:00 - 6110:00

my Apple phone for example you know

## 6110:00 - 6145:00

Apple makes awesome chips but the

## 6145:00 - 6190:00

experience of using my phone uh is a lot

## 6190:00 - 6225:00

more than the Chip And you know the way

## 6225:00 - 6255:00

that Apple's able to vertically

## 6255:00 - 6305:00

integrate and optimize um their entire

## 6305:00 - 6335:00

system in order to create an amazing

## 6335:00 - 6370:00

consumer experience I think is is pretty

## 6370:00 - 6410:00

incredible and and super valuable what

## 6410:00 - 6460:00

Nvidia is doing is uh not the same but

## 6460:00 - 6500:00

it's related in the sense that we

## 6500:00 - 6540:00

understand that the value of the

## 6540:00 - 6590:00

technology we create is only understood

## 6590:00 - 6640:00

in composition in context it's really

## 6640:00 - 6685:00

about are we delivering acceleration

## 6685:00 - 6715:00

transformative acceleration to the most

## 6715:00 - 6755:00

important computational workloads of our

## 6755:00 - 6800:00

time so why couldn't other companies

## 6800:00 - 6840:00

then just go and build their own

## 6840:00 - 6900:00

software to train using Nvidia chips or

## 6900:00 - 6950:00

other chips because it seems to me like

## 6950:00 - 6990:00

correct me if I'm wrong here also but if

## 6990:00 - 7020:00

I'm reliant on nvidia's software it's

## 7020:00 - 7045:00

closed Source right so I'm going to

## 7045:00 - 7105:00

train my model with it um it's kind of

## 7105:00 - 7140:00

difficult to switch to another chip so

## 7140:00 - 7200:00

why why particularly rely on the Nvidia

## 7200:00 - 7240:00

software yeah I mean we we have a lot of

## 7240:00 - 7270:00

open- source software as well as some

## 7270:00 - 7310:00

closed Source software um you know we we

## 7310:00 - 7330:00

make the decision about what to open

## 7330:00 - 7355:00

source based on what we think is going

## 7355:00 - 7400:00

to help the market most but I mean the

## 7400:00 - 7440:00

reason why people work with us is

## 7440:00 - 7500:00

because uh we deliver transformational

## 7500:00 - 7530:00

acceleration we enable people to do

## 7530:00 - 7555:00

things computationally that they just

## 7555:00 - 7600:00

couldn't do and we know that it would

## 7600:00 - 7635:00

never be enough to just provide a chip

## 7635:00 - 7670:00

that said it was really fast and had

## 7670:00 - 7700:00

like a lot of operations per second

## 7700:00 - 7740:00

inside the chip because the the gap

## 7740:00 - 7785:00

between um you know what a particular

## 7785:00 - 7825:00

chip can do and what the experience of a

## 7825:00 - 7865:00

science scientist or engineer trying to

## 7865:00 - 7905:00

invent the future uh that that Gap is

## 7905:00 - 7955:00

quite enormous um and uh if any one of

## 7955:00 - 7990:00

the links in that chain whether we're

## 7990:00 - 8025:00

talking about systems design or

## 8025:00 - 8075:00

networking or data center design or the

## 8075:00 - 8115:00

compilers Frameworks libraries um

## 8115:00 - 8150:00

applications algorithms you know if any

## 8150:00 - 8220:00

any of those links um are to fail the

## 8220:00 - 8250:00

acceleration is lost and the value

## 8250:00 - 8300:00

therefore is lost and so Nvidia has a

## 8300:00 - 8355:00

unique way of approaching this problem

## 8355:00 - 8395:00

uh co-optimizing the entire stack in

## 8395:00 - 8440:00

order to deliver that acceleration to

## 8440:00 - 8475:00

the end uh scientists and researchers

## 8475:00 - 8510:00

that are trying to the future and that's

## 8510:00 - 8550:00

what differentiates us from other

## 8550:00 - 8590:00

companies now uh could other companies

## 8590:00 - 8635:00

do that I mean absolutely it's it's uh

## 8635:00 - 8660:00

it's not a secret in fact we've been

## 8660:00 - 8685:00

shouting it from the rooftops for

## 8685:00 - 8715:00

decades that this is what we do and that

## 8715:00 - 8755:00

it's different from being a chip company

## 8755:00 - 8800:00

but you know we're we're continuing to

## 8800:00 - 8845:00

test that thesis you know is there value

## 8845:00 - 8880:00

in accelerated Computing that's above

## 8880:00 - 8930:00

and beyond uh what you get just from U

## 8930:00 - 8965:00

making and selling awesome chips and and

## 8965:00 - 8995:00

I think the answer to that is yes

## 8995:00 - 9015:00

and you know I think that's the reason

## 9015:00 - 9050:00

why we've been so successful right and

## 9050:00 - 9080:00

to me I think this is just for anyone

## 9080:00 - 9110:00

listening like I spent the whole week

## 9110:00 - 9150:00

making calls on Nvidia trying to figure

## 9150:00 - 9175:00

out because I was wrong I thought that

## 9175:00 - 9200:00

like the everything would kind of slow

## 9200:00 - 9235:00

down this year and I was like speaking

## 9235:00 - 9270:00

to customers and analyst tell me exactly

## 9270:00 - 9315:00

what I missed and and this was the thing

## 9315:00 - 9350:00

that I underestimated which is that it's

## 9350:00 - 9385:00

not just the chip but it's the chip the

## 9385:00 - 9415:00

software and everything that goes along

## 9415:00 - 9445:00

with it and that's why the company has

## 9445:00 - 9505:00

been so successful so

## 9505:00 - 9525:00

let's talk a little bit about like what

## 9525:00 - 9565:00

it actually goes into training an AI

## 9565:00 - 9610:00

model so do you have companies let's say

## 9610:00 - 9645:00

an open AI or whoever it might be that

## 9645:00 - 9690:00

says okay I'm ready to train a model do

## 9690:00 - 9725:00

they then get in touch with Nvidia and

## 9725:00 - 9760:00

be like this is what I'm looking to do

## 9760:00 - 9785:00

and then you help them figure out how

## 9785:00 - 9825:00

many chips they need what pieces of

## 9825:00 - 9870:00

software they need to to train and

## 9870:00 - 9905:00

everything else that comes along with

## 9905:00 - 9965:00

that we have um a really great set of

## 9965:00 - 10010:00

relationships with um institutions

## 10010:00 - 10045:00

around the world that are building Ai

## 10045:00 - 10090:00

and we're always trying to um help them

## 10090:00 - 10115:00

get the benefits of accelerated

## 10115:00 - 10155:00

Computing uh in whatever way makes sense

## 10155:00 - 10215:00

to them obviously um every institution

## 10215:00 - 10240:00

is going to have a different um

## 10240:00 - 10260:00

perspective and what they're trying to

## 10260:00 - 10280:00

do and they're going to have different

## 10280:00 - 10305:00

secrets that they need to keep as part

## 10305:00 - 10340:00

of their strategy about how they go to

## 10340:00 - 10385:00

go go to do that and we respect that uh

## 10385:00 - 10415:00

but at the same time you know we do try

## 10415:00 - 10470:00

to help them understand what's possible

## 10470:00 - 10515:00

uh with our systems and make sure that

## 10515:00 - 10540:00

you know they're actually getting the

## 10540:00 - 10570:00

the transformational acceleration that

## 10570:00 - 10620:00

we expect um so we do partner pretty

## 10620:00 - 10655:00

closely with with a lot of uh important

## 10655:00 - 10685:00

customers I think one of the things

## 10685:00 - 10725:00

that's special about Nvidia is that it

## 10725:00 - 10775:00

is a supporting and sustaining uh kind

## 10775:00 - 10820:00

of interaction when we work with our

## 10820:00 - 10875:00

customers um uh Nvidia technology is

## 10875:00 - 10905:00

integrated into the heart of many

## 10905:00 - 10965:00

different companies from amazing uh AI

## 10965:00 - 11030:00

institutions like opena I to um uh very

## 11030:00 - 11075:00

uh established uh companies that do

## 11075:00 - 11120:00

manufacturing or consumer products um or

## 11120:00 - 11160:00

self-driving or you know basically every

## 11160:00 - 11210:00

aspect of of the world's economy Nvidia

## 11210:00 - 11270:00

is able to um uh provide technology at

## 11270:00 - 11310:00

the level that um makes sense for for

## 11310:00 - 11360:00

companies to use uh if they'd like um us

## 11360:00 - 11395:00

to to provide uh just systems and they

## 11395:00 - 11425:00

want to write all the software um you

## 11425:00 - 11445:00

know they can write as much software as

## 11445:00 - 11475:00

they want if they want to use all of our

## 11475:00 - 11520:00

software uh you know that's great too um

## 11520:00 - 11550:00

and we're just trying to help support

## 11550:00 - 11585:00

and sustain uh all of the different

## 11585:00 - 11625:00

companies as they use AI for their own

## 11625:00 - 11690:00

work right and so let just let's walk

## 11690:00 - 11720:00

through a little bit about like how this

## 11720:00 - 11760:00

actually happens so let's say I'm an

## 11760:00 - 11815:00

organization uh I come to Nvidia say I

## 11815:00 - 11840:00

have a bunch of data or maybe I even

## 11840:00 - 11880:00

don't have data and I'm looking to build

## 11880:00 - 11965:00

a large language model um what do I do

## 11965:00 - 11995:00

now

## 11995:00 - 12025:00

de that's a great question you know the

## 12025:00 - 12055:00

the first thing that's on my mind is

## 12055:00 - 12080:00

like you know what data center are you

## 12080:00 - 12135:00

going to use to train this model in um

## 12135:00 - 12160:00

and uh you know that's that's a really

## 12160:00 - 12195:00

important question uh because it turns

## 12195:00 - 12245:00

out that uh the AI Market is growing

## 12245:00 - 12270:00

pretty fast because there's so many

## 12270:00 - 12295:00

institutions that are training these

## 12295:00 - 12320:00

huge models and you actually have to

## 12320:00 - 12350:00

have a building to put these machines in

## 12350:00 - 12375:00

and they're they're not small uh and you

## 12375:00 - 12410:00

need to hook it up to power you know so

## 12410:00 - 12430:00

that that would be one of my first

## 12430:00 - 12475:00

questions is like okay are are you ready

## 12475:00 - 12510:00

uh to stand this up or um are you going

## 12510:00 - 12545:00

to be working with a CSP like for

## 12545:00 - 12605:00

example AWS you know um and we love we

## 12605:00 - 12645:00

love to support our customers um through

## 12645:00 - 12710:00

through Cloud providers as well okay and

## 12710:00 - 12760:00

so then what happens next let's say I'm

## 12760:00 - 12825:00

set up you're set up okay so um uh we

## 12825:00 - 12865:00

will definitely point you to our

## 12865:00 - 12910:00

reference implementations of the various

## 12910:00 - 12980:00

uh llms and their training uh setups on

## 12980:00 - 13020:00

uh these clouds we'll show you um how to

## 13020:00 - 13070:00

scale it to you know many thousand gpus

## 13070:00 - 13110:00

efficiently um we'll we'll tell you what

## 13110:00 - 13145:00

kind of speed you should expect uh to

## 13145:00 - 13185:00

get while training the model and we'll

## 13185:00 - 13235:00

um also you know uh discuss things about

## 13235:00 - 13275:00

reliability um you know how do we make

## 13275:00 - 13305:00

sure that the the job is actually

## 13305:00 - 13345:00

progressing properly and yielding you

## 13345:00 - 13395:00

know intelligence um you know so we we

## 13395:00 - 13430:00

we definitely um help our customers with

## 13430:00 - 13485:00

things like that um I think also then

## 13485:00 - 13515:00

when the model's trained uh there's a

## 13515:00 - 13550:00

question about how do we deploy it you

## 13550:00 - 13595:00

know and we we'd love to um uh to to

## 13595:00 - 13650:00

help people deploy AI as well I think um

## 13650:00 - 13680:00

uh Jensen said in the earnings call this

## 13680:00 - 13715:00

week that somewhere around 40% of our

## 13715:00 - 13760:00

data center um gpus were we're going for

## 13760:00 - 13800:00

inference which I think is um you know

## 13800:00 - 13835:00

pretty amazing and and definitely a

## 13835:00 - 13865:00

shift from where things have been a few

## 13865:00 - 13910:00

years ago um and so uh we're spending a

## 13910:00 - 13950:00

lot more time helping our customers

## 13950:00 - 13970:00

accelerate the deployment of these

## 13970:00 - 14005:00

models as well making sure that they get

## 14005:00 - 14065:00

you know the best um uh uh speed uh so

## 14065:00 - 14105:00

that they can you know get get as much

## 14105:00 - 14125:00

out of the systems they're deploying

## 14125:00 - 14165:00

these models on as possible and what are

## 14165:00 - 14220:00

they using the models

## 14220:00 - 14310:00

for um I think that you know uh language

## 14310:00 - 14345:00

models are starting to be used in a lot

## 14345:00 - 14385:00

of different parts of uh a lot of

## 14385:00 - 14420:00

different companies um things like

## 14420:00 - 14470:00

question answering um uh I I think a

## 14470:00 - 14510:00

really important um to help help uh

## 14510:00 - 14555:00

people understand uh answers to their

## 14555:00 - 14580:00

their specific questions especially

## 14580:00 - 14635:00

relating to um private data stores that

## 14635:00 - 14665:00

um that they need to answer questions

## 14665:00 - 14710:00

with um you know I think we're we're

## 14710:00 - 14765:00

seeing a lot of uh people use uh Ai and

## 14765:00 - 14795:00

office type settings I don't know if

## 14795:00 - 14830:00

you've um interacted with Microsoft

## 14830:00 - 14875:00

co-pilot at all but um it can be really

## 14875:00 - 14910:00

helpful uh at least to me when I'm

## 14910:00 - 14955:00

looking at um a summary of a meeting and

## 14955:00 - 14980:00

what the the action items are for

## 14980:00 - 15035:00

everybody at the meeting um you know uh

## 15035:00 - 15080:00

another sort of office automation uh

## 15080:00 - 15125:00

tasks um you know we're also pushing

## 15125:00 - 15165:00

forward with uh the use of these models

## 15165:00 - 15200:00

for our own internal work at Nvidia we

## 15200:00 - 15250:00

have a project called chip Nemo that is

## 15250:00 - 15290:00

um uh using language models to help our

## 15290:00 - 15330:00

chip designers and and uh verification

## 15330:00 - 15370:00

efforts be more efficient as we build

## 15370:00 - 15415:00

our own um products it's called chip

## 15415:00 - 15460:00

Nemo yeah is is that similar I mean I

## 15460:00 - 15480:00

was just speaking with service now

## 15480:00 - 15505:00

there's ALS they're also using an

## 15505:00 - 15545:00

program from Nvidia called Nemo to

## 15545:00 - 15570:00

that's correct yeah and that's what it

## 15570:00 - 15615:00

is it's they use it that's like what is

## 15615:00 - 15650:00

that software that they use to propel

## 15650:00 - 15710:00

their question answering yeah Nemo is is

## 15710:00 - 15760:00

kind of our um uh uh most userfriendly

## 15760:00 - 15815:00

uh open- Source software for training

## 15815:00 - 15855:00

and fine-tuning language models and and

## 15855:00 - 15905:00

other kinds of conversational AI um it

## 15905:00 - 15935:00

it also has a lot of speech capabilities

## 15935:00 - 15975:00

as well and uh you know we've been

## 15975:00 - 16000:00

building it for quite a few years

## 16000:00 - 16030:00

because we believed that uh

## 16030:00 - 16055:00

conversational AI was really going to

## 16055:00 - 16110:00

transform uh industry we wanted uh to

## 16110:00 - 16155:00

make a platform for companies to build

## 16155:00 - 16185:00

their own build build and deploy their

## 16185:00 - 16220:00

own conversational AI so that's what

## 16220:00 - 16255:00

that's what Nemo is and uh so when we

## 16255:00 - 16280:00

talk about chip Nemo we're talking about

## 16280:00 - 16340:00

using that uh for our own own chip workk

## 16340:00 - 16360:00

wait yeah how so how do you use it for

## 16360:00 - 16375:00

your own chip

## 16375:00 - 16425:00

work um at the moment a lot of it has to

## 16425:00 - 16465:00

do with improving communication between

## 16465:00 - 16505:00

uh chip designers so uh you have like a

## 16505:00 - 16540:00

thousand people working on this project

## 16540:00 - 16575:00

and there's a lot of interfaces that

## 16575:00 - 16605:00

need to be described and um you know

## 16605:00 - 16635:00

people have questions they don't know uh

## 16635:00 - 16675:00

exactly who to talk to so basically

## 16675:00 - 16730:00

we're making uh uh knowledge bases about

## 16730:00 - 16765:00

our own work that then people uh can use

## 16765:00 - 16810:00

to answer questions um and we found that

## 16810:00 - 16850:00

that um it's kind of like having a a

## 16850:00 - 16885:00

more senior engineer uh that you can

## 16885:00 - 16925:00

talk to all the time that that helps you

## 16925:00 - 16950:00

uh find the things you need to find in a

## 16950:00 - 16980:00

in a huge code base

## 16980:00 - 17020:00

um and so so that's that's the primary

## 17020:00 - 17045:00

thing that we're doing right now is is

## 17045:00 - 17090:00

augmenting uh the engineers on the team

## 17090:00 - 17120:00

with kind of um superpowers to

## 17120:00 - 17155:00

understand our own code better and and

## 17155:00 - 17195:00

interact with it better uh over time I

## 17195:00 - 17230:00

expect that chip Nemo is going to uh do

## 17230:00 - 17265:00

other things as well um you know

## 17265:00 - 17305:00

improving the quality of our designs you

## 17305:00 - 17355:00

know our hopper gpus for example have a

## 17355:00 - 17380:00

lot of circuits in them that were

## 17380:00 - 17420:00

designed by AI that we built ourselves

## 17420:00 - 17475:00

uh that have better um speed um and

## 17475:00 - 17520:00

power and cost characteristics then uh

## 17520:00 - 17555:00

we knew how to build with any other tool

## 17555:00 - 17625:00

and generative AI uh programs designed

## 17625:00 - 17680:00

some of the chips yes hopper Hopper uh

## 17680:00 - 17720:00

is designed with generative AI that's

## 17720:00 - 17775:00

insane it's wild yeah so let's dream a

## 17775:00 - 17825:00

little bit um obviously we we know that

## 17825:00 - 17875:00

that like knowledge repositories inside

## 17875:00 - 17900:00

uh companies is something that this

## 17900:00 - 17950:00

stuff is going to be really good for um

## 17950:00 - 17990:00

maybe a little bit of like uh consumer

## 17990:00 - 18030:00

agents or consumer chat Bots like chat

## 18030:00 - 18070:00

GPT is this where it ends like where do

## 18070:00 - 18115:00

you see it going I don't think this is

## 18115:00 - 18145:00

where it ends um you know I've been

## 18145:00 - 18195:00

thinking recently about um past

## 18195:00 - 18250:00

Revolutions in the media space um you

## 18250:00 - 18300:00

know we we got books uh which

## 18300:00 - 18335:00

transformed Society you know when

## 18335:00 - 18365:00

because we could distribute ideas and we

## 18365:00 - 18395:00

could reference the same ideas in a new

## 18395:00 - 18415:00

way because everybody could read the

## 18415:00 - 18460:00

same book you know um audio you know as

## 18460:00 - 18505:00

soon as we audio recordings that created

## 18505:00 - 18535:00

an entirely new industry you know the

## 18535:00 - 18565:00

recorded music industry which uh

## 18565:00 - 18595:00

continues to be totally vibrant and

## 18595:00 - 18680:00

important to our culture um movies uh TV

## 18680:00 - 18725:00

you know um every and video games you

## 18725:00 - 18760:00

know every time that we come up with a

## 18760:00 - 18775:00

new

## 18775:00 - 18825:00

technology we find a way to explore

## 18825:00 - 18875:00

ideas as humans and explore our culture

## 18875:00 - 18925:00

together uh in in a way that like helps

## 18925:00 - 18960:00

us solve problems better and also

## 18960:00 - 19020:00

creates um a new form of culture that uh

## 19020:00 - 19060:00

that we interact with and I think that

## 19060:00 - 19105:00

um the most exciting applications for AI

## 19105:00 - 19135:00

are ones we haven't really even dreamed

## 19135:00 - 19175:00

up yet in in the same way that it would

## 19175:00 - 19225:00

be it would have been hard um to imagine

## 19225:00 - 19270:00

how books were going to change the world

## 19270:00 - 19305:00

uh back when Gutenberg first made the

## 19305:00 - 19390:00

Press uh you know uh I think uh uh AI is

## 19390:00 - 19435:00

going to create a new form of media that

## 19435:00 - 19460:00

is much more interesting much more

## 19460:00 - 19505:00

engaging much more useful um and

## 19505:00 - 19530:00

ultimately we're going to use that to

## 19530:00 - 19560:00

refine our ideas and explore them

## 19560:00 - 19595:00

together in the way that we have with

## 19595:00 - 19620:00

other other media it's just going to be

## 19620:00 - 19655:00

much more interesting and useful when I

## 19655:00 - 19685:00

hear you say media leads me to believe

## 19685:00 - 19715:00

that you think that this is going to be

## 19715:00 - 19765:00

more of like a an agent or or a digital

## 19765:00 - 19795:00

friend that people will start

## 19795:00 - 19835:00

interacting with right because that's me

## 19835:00 - 19865:00

media unless is is there something else

## 19865:00 - 19885:00

or something else I could be thinking

## 19885:00 - 19920:00

about I'm not thinking about that could

## 19920:00 - 19960:00

take the form of media yeah something

## 19960:00 - 20000:00

along those those lines I mean I I think

## 20000:00 - 20025:00

you know I'm expecting AI is going to

## 20025:00 - 20060:00

change the lives of all of us here on

## 20060:00 - 20095:00

planet Earth and when I think about how

## 20095:00 - 20140:00

8 billion people on this planet live you

## 20140:00 - 20170:00

know most of us aren't reading and

## 20170:00 - 20220:00

writing that much you know um but we we

## 20220:00 - 20265:00

do love uh Virtual Worlds people love

## 20265:00 - 20290:00

interacting in video games we love

## 20290:00 - 20330:00

interacting with each other and I think

## 20330:00 - 20365:00

um that the primary way that people are

## 20365:00 - 20395:00

going to interact with AI is going to be

## 20395:00 - 20440:00

in Virtual Worlds um because I think

## 20440:00 - 20460:00

that's going to be the most natural way

## 20460:00 - 20495:00

of interaction in the most useful way

## 20495:00 - 20520:00

and I think we're going to perceive that

## 20520:00 - 20555:00

as a new form of media that that really

## 20555:00 - 20610:00

touches you know all aspects of of our

## 20610:00 - 20640:00

work and our play you know it's it's

## 20640:00 - 20690:00

going to be uh something new so you're

## 20690:00 - 20720:00

you're a real believer in this metaverse

## 20720:00 - 20755:00

Vision that you'll just kind of end up

## 20755:00 - 20800:00

in a digital world and the people and

## 20800:00 - 20840:00

the scenery will all be AI generated or

## 20840:00 - 20905:00

maybe mostly AI generated and and you go

## 20905:00 - 20990:00

um I think that people um

## 20990:00 - 21020:00

we we have a culture it's very important

## 21020:00 - 21065:00

to us you know the the the ideas that we

## 21065:00 - 21110:00

share together and the sort of shared

## 21110:00 - 21150:00

Humanity that we have is more important

## 21150:00 - 21225:00

to us than uh the content of uh the the

## 21225:00 - 21250:00

things that we're interacting with so

## 21250:00 - 21295:00

for example um AI is probably going to

## 21295:00 - 21360:00

be really awesome at playing soccer but

## 21360:00 - 21400:00

do I think that people are going to go

## 21400:00 - 21460:00

to watch Robots play soccer um even if

## 21460:00 - 21480:00

they're robots are kicking around the

## 21480:00 - 21510:00

ball better than humans I don't think

## 21510:00 - 21535:00

it's as interesting because I don't

## 21535:00 - 21565:00

think that it is related to us you know

## 21565:00 - 21585:00

I think the primary thing that we're

## 21585:00 - 21615:00

interested in is ourselves we're trying

## 21615:00 - 21640:00

to understand ourselves and and how we

## 21640:00 - 21675:00

relate to other people I think AI is

## 21675:00 - 21715:00

going to give us new ways of doing that

## 21715:00 - 21755:00

um I think we are going to be uh

## 21755:00 - 21780:00

interacting in in Virtual Worlds you

## 21780:00 - 21835:00

know Nvidia has been uh uh a big

## 21835:00 - 21870:00

believer in Virtual Worlds for you know

## 21870:00 - 21900:00

the past 30 years it's something been on

## 21900:00 - 21955:00

gaming before you were on AI and and

## 21955:00 - 21975:00

we've had this in itive called the

## 21975:00 - 22030:00

Omniverse uh long before uh uh meta

## 22030:00 - 22085:00

renamed itself um because we believe

## 22085:00 - 22120:00

that uh simulating the world and

## 22120:00 - 22160:00

providing um you know virtual agents a

## 22160:00 - 22205:00

place to interact with people um is is

## 22205:00 - 22230:00

hugely important to the future of

## 22230:00 - 22265:00

technology and you know I I see these

## 22265:00 - 22315:00

things coming together I think um

## 22315:00 - 22355:00

there's a lot of opportunities to use uh

## 22355:00 - 22395:00

Virtual Worlds to make AI stronger to

## 22395:00 - 22430:00

teach AI how to understand the real

## 22430:00 - 22460:00

world and and act better in the real

## 22460:00 - 22505:00

world and then of course um uh giving

## 22505:00 - 22545:00

humans the opportunity to interact with

## 22545:00 - 22580:00

AIS in much more natural and useful ways

## 22580:00 - 22600:00

I think a lot of that's going to happen

## 22600:00 - 22640:00

in a virtual world and is that the next

## 22640:00 - 22665:00

place that we go with this like the

## 22665:00 - 22710:00

world models like we just saw meta put

## 22710:00 - 22755:00

something out where like it's uh

## 22755:00 - 22780:00

generative or it's not even generative

## 22780:00 - 22805:00

software but it's AI software can kind

## 22805:00 - 22835:00

of guess like what would happen if you

## 22835:00 - 22875:00

black out like a certain frame in a

## 22875:00 - 22925:00

video um is that is that where the next

## 22925:00 - 22970:00

stage of this goes I think that's going

## 22970:00 - 23010:00

to be really helpful um you know these

## 23010:00 - 23050:00

these sorts of world models um you know

## 23050:00 - 23080:00

I was really impressed with the uh open

## 23080:00 - 23130:00

AI Sora project uh this week as well I

## 23130:00 - 23175:00

mean really fantastic results and I'm

## 23175:00 - 23220:00

thinking about you know uh how these

## 23220:00 - 23250:00

things work together so you know the

## 23250:00 - 23285:00

Sora project if you read their post they

## 23285:00 - 23310:00

talk a lot about how building a world

## 23310:00 - 23350:00

model is going to help uh make

## 23350:00 - 23375:00

artificial intelligence more useful

## 23375:00 - 23410:00

because it it you know it it's going to

## 23410:00 - 23435:00

understand how things interact in the

## 23435:00 - 23465:00

real world and then it's going to be

## 23465:00 - 23495:00

able to use that to to make better

## 23495:00 - 23540:00

decisions in order to do things um so so

## 23540:00 - 23570:00

I think that's great um and I also think

## 23570:00 - 23610:00

it's uh the other way it around is also

## 23610:00 - 23640:00

really important that you know having a

## 23640:00 - 23675:00

world model then allows us to synthesize

## 23675:00 - 23715:00

a world which then uh allows Virtual

## 23715:00 - 23750:00

Worlds to be richer more interesting

## 23750:00 - 23780:00

more interactive and I think that's

## 23780:00 - 23815:00

hugely valuable and how do you train a

## 23815:00 - 23850:00

world model like with text I get text

## 23850:00 - 23890:00

right like you put the text in it spits

## 23890:00 - 23965:00

the text out but teaching AI a way way

## 23965:00 - 23995:00

to understand what the world looks like

## 23995:00 - 24025:00

is completely

## 24025:00 - 24075:00

different yeah um usually the way these

## 24075:00 - 24100:00

work is that there's some sort of

## 24100:00 - 24130:00

implicit learned representation of the

## 24130:00 - 24165:00

world we can call it a state space but

## 24165:00 - 24220:00

it's basically like um uh we're trying

## 24220:00 - 24260:00

like imagine if you could write down uh

## 24260:00 - 24290:00

every attribute of every object in the

## 24290:00 - 24325:00

world like where it is how how it's

## 24325:00 - 24370:00

moving what color it is you know if if

## 24370:00 - 24415:00

you if you're able to write down uh very

## 24415:00 - 24470:00

precisely where every object is uh then

## 24470:00 - 24515:00

uh you would have a good way to draw the

## 24515:00 - 24540:00

world right because you could you could

## 24540:00 - 24560:00

take that representation and then just

## 24560:00 - 24590:00

turn it into a picture but then you

## 24590:00 - 24625:00

could also use that to simulate you

## 24625:00 - 24670:00

could ask a question like okay if I took

## 24670:00 - 24720:00

um this particular action uh you know

## 24720:00 - 24750:00

what would the updated State space look

## 24750:00 - 24790:00

like you know so like for example if I

## 24790:00 - 24825:00

if I uh swing the baseball bat when the

## 24825:00 - 24860:00

ball's right there and I hit hit the

## 24860:00 - 24885:00

ball you know then that's going to be a

## 24885:00 - 24930:00

different future than if I um swing the

## 24930:00 - 24965:00

ball when the when the swing the that

## 24965:00 - 24985:00

when the ball's not there and I I miss

## 24985:00 - 25040:00

it right so um with a with with a model

## 25040:00 - 25065:00

with a world model like this you can

## 25065:00 - 25105:00

kind of ask those questions and and then

## 25105:00 - 25145:00

uh simulate uh how things go forward in

## 25145:00 - 25180:00

time now one of the tricky things is

## 25180:00 - 25235:00

that um writing down very precisely all

## 25235:00 - 25285:00

of the state of the world is basically

## 25285:00 - 25325:00

impossible you know it's uh it's way too

## 25325:00 - 25375:00

complex um and you know this this is for

## 25375:00 - 25405:00

example well known in weather

## 25405:00 - 25440:00

forecasting right the idea that like a

## 25440:00 - 25475:00

butterfly flapping its Wings in Japan

## 25475:00 - 25535:00

could you know magnify over the this the

## 25535:00 - 25565:00

course of time into like a hurricane on

## 25565:00 - 25600:00

the other side of the world right um

## 25600:00 - 25645:00

because very small um changes in the

## 25645:00 - 25665:00

state space of the world could actually

## 25665:00 - 25740:00

have pretty large uh outcomes and um so

## 25740:00 - 25775:00

so one of the ways that these learned

## 25775:00 - 25810:00

neural network models are dealing with

## 25810:00 - 25840:00

this is that rather than having an

## 25840:00 - 25880:00

explicit representation of everything in

## 25880:00 - 25920:00

the world uh it's all being done

## 25920:00 - 25970:00

implicitly so the model learns both a

## 25970:00 - 26025:00

function that's that's able to go from

## 26025:00 - 26055:00

uh some implicit representation of the

## 26055:00 - 26100:00

world to to drawing it and also from

## 26100:00 - 26130:00

that implicit representation into the

## 26130:00 - 26185:00

future and and then also um you know is

## 26185:00 - 26225:00

learning that representation from uh

## 26225:00 - 26265:00

from the data it's trained on directly

## 26265:00 - 26290:00

so it's all learned and that way we

## 26290:00 - 26335:00

don't have to actually try to um

## 26335:00 - 26370:00

describe the world to the model it it

## 26370:00 - 26400:00

learns how to describe the world itself

## 26400:00 - 26420:00

and I'm going to regret asking this

## 26420:00 - 26490:00

question but how does it learn that

## 26490:00 - 26535:00

um uh it starts to get metaphysical for

## 26535:00 - 26570:00

me a little bit you know uh these these

## 26570:00 - 26610:00

models are trained um using stochastic

## 26610:00 - 26640:00

gradient descent so it's um what we're

## 26640:00 - 26725:00

trying to do is um you know uh fit the

## 26725:00 - 26775:00

data that we're given as best we can by

## 26775:00 - 26810:00

um taking a lot of really small steps to

## 26810:00 - 26855:00

improve the model so um you know it's

## 26855:00 - 26885:00

kind of like so gradient descent is is

## 26885:00 - 26925:00

kind of like um walking down a mountain

## 26925:00 - 26960:00

the idea is that like the the fast

## 26960:00 - 26980:00

fastest way to walk down the mountain is

## 26980:00 - 27020:00

just look where you are at any moment

## 27020:00 - 27055:00

and find the the direction that's

## 27055:00 - 27085:00

pointed downward the steepest and and

## 27085:00 - 27125:00

take a step in that direction now you

## 27125:00 - 27150:00

can you can tell that this this

## 27150:00 - 27190:00

algorithm isn't very isn't very smart

## 27190:00 - 27215:00

right because if there's a canyon

## 27215:00 - 27240:00

depending on how big your step is you

## 27240:00 - 27275:00

might actually step over the canyon or

## 27275:00 - 27305:00

you might you might get caught you know

## 27305:00 - 27325:00

going back and forth when really you

## 27325:00 - 27370:00

should be going down the canyon and in

## 27370:00 - 27400:00

the spaces that we're optimizing with

## 27400:00 - 27455:00

you know let's say a trillion Dimensions

## 27455:00 - 27490:00

right right um these kinds of effects

## 27490:00 - 27530:00

are are are really interesting and and

## 27530:00 - 27560:00

and difficult to understand difficult to

## 27560:00 - 27615:00

to relate to but um the the thing that

## 27615:00 - 27650:00

makes this work is that we don't

## 27650:00 - 27690:00

actually have to be super precise about

## 27690:00 - 27725:00

how we update the model for every bit of

## 27725:00 - 27770:00

data it learns we just kind of do a

## 27770:00 - 27810:00

rough guess about like this data is

## 27810:00 - 27850:00

pointing the model um to fit in this

## 27850:00 - 27875:00

particular direction we'll take a little

## 27875:00 - 27905:00

step that way and then we're we're going

## 27905:00 - 27940:00

to do that a lot you know and and that's

## 27940:00 - 27975:00

what we call this stochastic part so

## 27975:00 - 28025:00

it's it's a little bit random um but uh

## 28025:00 - 28060:00

it's actually kind of a a great

## 28060:00 - 28100:00

Philosophy for life I think that um you

## 28100:00 - 28125:00

know you could spend an awful lot of

## 28125:00 - 28165:00

time trying to be very precise about

## 28165:00 - 28190:00

what direction to go to make things

## 28190:00 - 28230:00

better but often the right thing to do

## 28230:00 - 28275:00

is just make a guess take a step and

## 28275:00 - 28315:00

then re-evaluate what the best direction

## 28315:00 - 28350:00

is next and then do that a lot you know

## 28350:00 - 28390:00

just just be really iterative really

## 28390:00 - 28440:00

flexible don't be too wetted to you know

## 28440:00 - 28470:00

the idea that you have about where to go

## 28470:00 - 28505:00

at the beginning of the process just let

## 28505:00 - 28540:00

the process kind of guide you as you as

## 28540:00 - 28575:00

you uh walk through it and that's that's

## 28575:00 - 28610:00

the algorithms that we use um uh to

## 28610:00 - 28665:00

train all neural networks um you know so

## 28665:00 - 28690:00

the specific contents of what the

## 28690:00 - 28725:00

networks are learning are difficult to

## 28725:00 - 28750:00

interpret we don't have a lot of tools

## 28750:00 - 28790:00

that help us understand that uh in the

## 28790:00 - 28820:00

same way that we don't really understand

## 28820:00 - 28860:00

um how our own brains work you know we

## 28860:00 - 28885:00

we don't really understand all the

## 28885:00 - 28910:00

things that are happening inside of our

## 28910:00 - 28960:00

heads in order to allow us to think um

## 28960:00 - 29005:00

it's too complicated uh for for our our

## 29005:00 - 29025:00

analytics at the

## 29025:00 - 29070:00

moment thing is it works yeah it works

## 29070:00 - 29100:00

and we didn't build the brain but we did

## 29100:00 - 29135:00

build these systems and it's working and

## 29135:00 - 29170:00

we don't know how that's happening which

## 29170:00 - 29215:00

is which is wild okay I want to talk

## 29215:00 - 29250:00

about uh reasoning I want to talk about

## 29250:00 - 29300:00

robotics potentially and um and a few

## 29300:00 - 29325:00

other ways about how companies are going

## 29325:00 - 29360:00

to work with Nvidia and what might be

## 29360:00 - 29380:00

coming down the pike so we're going to

## 29380:00 - 29410:00

do that right after the break coming up

## 29410:00 - 29455:00

right after this and we're back here on

## 29455:00 - 29490:00

big technology podcast with Brian

## 29490:00 - 29520:00

katenzaro he's the vice president of

## 29520:00 - 29565:00

Applied deep learning research at Nvidia

## 29565:00 - 29610:00

uh Brian just to start off like what

## 29610:00 - 29660:00

made you think okay AI is going to be

## 29660:00 - 29690:00

big enough that I should get to Jensen

## 29690:00 - 29740:00

CEO of Nvidia and say we need to really

## 29740:00 - 29800:00

work hard to make this part of our core

## 29800:00 - 29860:00

offering I had been spending my um

## 29860:00 - 29905:00

research career at at Berkeley as a PhD

## 29905:00 - 29950:00

student on uh the future of computing

## 29950:00 - 29990:00

and um we knew that Computing was going

## 29990:00 - 30045:00

to have to change back in 2005 or so it

## 30045:00 - 30075:00

was obvious that computers would have to

## 30075:00 - 30105:00

be different the standard way of making

## 30105:00 - 30140:00

computers wasn't working anymore we

## 30140:00 - 30170:00

would have to be more specific we'd have

## 30170:00 - 30210:00

to be more parallel and so I had been

## 30210:00 - 30245:00

spending my time as a grad student

## 30245:00 - 30270:00

thinking about what kinds of

## 30270:00 - 30320:00

applications could take advantage of uh

## 30320:00 - 30350:00

the computers that will be possible to

## 30350:00 - 30395:00

build um but then are going to provide

## 30395:00 - 30440:00

enormous amounts of value to humanity

## 30440:00 - 30475:00

and at the time AI was not a very big

## 30475:00 - 30535:00

field um uh and it wasn't actually super

## 30535:00 - 30570:00

popular to work in it but when I was

## 30570:00 - 30610:00

thinking about it I felt like um from

## 30610:00 - 30650:00

first principles it made sense to me

## 30650:00 - 30670:00

that this was something that had the

## 30670:00 - 30715:00

potential uh to really change the world

## 30715:00 - 30765:00

and you know nvidia's approach to uh

## 30765:00 - 30810:00

solving this I think was also you know

## 30810:00 - 30860:00

fairly careful and iterative you know so

## 30860:00 - 30905:00

um you know I I published my first paper

## 30905:00 - 30950:00

in 2008 on um machine learning on the

## 30950:00 - 31030:00

the GPU uh and Nvidia uh really jumped

## 31030:00 - 31080:00

in full steam ahead uh for the whole

## 31080:00 - 31120:00

company to to become an AI company in

## 31120:00 - 31190:00

2013 so it took about 5 years of um sort

## 31190:00 - 31235:00

of testing that thesis like is AI

## 31235:00 - 31260:00

actually going to be something that that

## 31260:00 - 31290:00

could really change the world and we

## 31290:00 - 31325:00

started getting some early indicators of

## 31325:00 - 31370:00

success you know um one of those was of

## 31370:00 - 31420:00

course the um uh imag net competition in

## 31420:00 - 31460:00

2012 um which really shocked the world

## 31460:00 - 31510:00

with the quality of results and wasn't

## 31510:00 - 31550:00

wouldn't have been possible without uh

## 31550:00 - 31590:00

accelerated Computing you know the U

## 31590:00 - 31630:00

results that they got um uh were so

## 31630:00 - 31660:00

incredible because they built a very

## 31660:00 - 31710:00

fast system for training neural Nets and

## 31710:00 - 31740:00

uh train wasn't generative right that

## 31740:00 - 31775:00

was just identifying what was in PH

## 31775:00 - 31800:00

that's correct yeah it wasn't generative

## 31800:00 - 31845:00

at the time but you know um the the idea

## 31845:00 - 31885:00

of generative AI is is fairly old I mean

## 31885:00 - 31925:00

when I was a grad student generative AI

## 31925:00 - 31960:00

was um a thing that we talked about all

## 31960:00 - 31985:00

the time it's just that we weren't using

## 31985:00 - 32015:00

neural nets for it we were using other

## 32015:00 - 32050:00

models like graphical models these are

## 32050:00 - 32090:00

other mathematical approaches that um

## 32090:00 - 32130:00

are a little bit more clever um but

## 32130:00 - 32190:00

don't scale as well and um so this was

## 32190:00 - 32220:00

this is another part of the thesis that

## 32220:00 - 32265:00

that um I had is that you know the the

## 32265:00 - 32295:00

thing that's really going to help AI

## 32295:00 - 32345:00

succeed is um scale you know if we can

## 32345:00 - 32375:00

apply huge data sets and huge amounts of

## 32375:00 - 32410:00

compute to AI then the results are going

## 32410:00 - 32445:00

to get much better and this is this is

## 32445:00 - 32495:00

also controversial um back then and and

## 32495:00 - 32530:00

even today some people really don't like

## 32530:00 - 32580:00

this idea because uh they would like AI

## 32580:00 - 32630:00

progress to be mostly uh held back by

## 32630:00 - 32675:00

our smarts like our mathematical um

## 32675:00 - 32710:00

skills in in like coming up with more

## 32710:00 - 32750:00

clever models to describe our data in

## 32750:00 - 32800:00

the world um but it it does seem uh

## 32800:00 - 32815:00

these days that there's a lot of

## 32815:00 - 32845:00

evidence that the most important thing

## 32845:00 - 32875:00

is having really good data sets to learn

## 32875:00 - 32905:00

from and then enormous computational

## 32905:00 - 32950:00

scale and so that was my that was my

## 32950:00 - 32985:00

thesis and I you know I I was advocating

## 32985:00 - 33040:00

for that at Nvidia I wrote this little

## 33040:00 - 33085:00

um prototype of a library for training

## 33085:00 - 33130:00

neur Nets on the GPU which uh then

## 33130:00 - 33185:00

became CNN which was our very first um

## 33185:00 - 33260:00

library for uh for AI on the GPU and um

## 33260:00 - 33295:00

you know the process of of uh getting

## 33295:00 - 33345:00

the company to Rally around that and and

## 33345:00 - 33375:00

and build that as a product and ship it

## 33375:00 - 33415:00

you know it took some time um but

## 33415:00 - 33455:00

because there were these um you know

## 33455:00 - 33485:00

early indicators of success that there

## 33485:00 - 33535:00

was a lot of uh demand picking up um

## 33535:00 - 33580:00

even back then uh it it made sense for

## 33580:00 - 33610:00

the company to to really pay attention

## 33610:00 - 33640:00

and then you know

## 33640:00 - 33685:00

Jensen himself is such a Visionary I

## 33685:00 - 33720:00

remember when he first started

## 33720:00 - 33755:00

interacting with me about this back in

## 33755:00 - 33820:00

2012 I um I felt like uh he was just so

## 33820:00 - 33855:00

hungry to learn you know so I felt like

## 33855:00 - 33875:00

I I gave him all the things that I

## 33875:00 - 33905:00

learned from my PhD in the course of

## 33905:00 - 33955:00

like an hour about like um how AI could

## 33955:00 - 33990:00

change nvidia's business and what uh

## 33990:00 - 34035:00

Nvidia could potentially build and my

## 34035:00 - 34070:00

ambitions for what that meant were like

## 34070:00 - 34110:00

a thousand times smaller than Jensen's

## 34110:00 - 34150:00

were you know um he he took it

## 34150:00 - 34185:00

immediately and then elaborated on it

## 34185:00 - 34230:00

and thought about where is this going um

## 34230:00 - 34260:00

you know one of the things he first said

## 34260:00 - 34325:00

back in 2012 was um uh this is an

## 34325:00 - 34355:00

entirely new way of writing software

## 34355:00 - 34395:00

rather than having humans enumerate all

## 34395:00 - 34420:00

the different cases that software needs

## 34420:00 - 34455:00

to understand we're going to have models

## 34455:00 - 34490:00

that learn from from our data how to

## 34490:00 - 34535:00

solve problems and um these days that

## 34535:00 - 34585:00

sounds like the truth right like we we

## 34585:00 - 34615:00

see that happening every day when we

## 34615:00 - 34650:00

interact with these models but you know

## 34650:00 - 34690:00

uh 12 years ago uh that was a pretty

## 34690:00 - 34720:00

bold thing to say and I was a little bit

## 34720:00 - 34765:00

nervous about it because um you know the

## 34765:00 - 34825:00

history of AI uh over the past you know

## 34825:00 - 34880:00

70 years had been one of um over

## 34880:00 - 34910:00

promising and underd delivering in a lot

## 34910:00 - 34955:00

of ways which then a lot booms

## 34955:00 - 34990:00

yeah a lot of like think it can do

## 34990:00 - 35030:00

something and then just totally dry it

## 35030:00 - 35060:00

up until it started to prove itself

## 35060:00 - 35100:00

again and so when when Jensen like

## 35100:00 - 35125:00

immediately glommed onto this and

## 35125:00 - 35170:00

started like um uh thinking about what

## 35170:00 - 35200:00

it what it could mean I wanted to slow

## 35200:00 - 35230:00

him down a little bit and be like Jensen

## 35230:00 - 35265:00

like this is a this is a big huge idea

## 35265:00 - 35290:00

but like I'm not sure if it's going to

## 35290:00 - 35335:00

happen now it might be 30 years from now

## 35335:00 - 35380:00

you know um but uh it turns out that

## 35380:00 - 35415:00

Jensen was right about this uh this was

## 35415:00 - 35460:00

the right time um to apply enormous data

## 35460:00 - 35490:00

and enormous compute to Ai and get these

## 35490:00 - 35540:00

results right but 2012 wasn't I mean it

## 35540:00 - 35600:00

took another 10 years 11 years really

## 35600:00 - 35650:00

for the boom to come so what did it feel

## 35650:00 - 35695:00

like yeah go ahead oh I was gonna say I

## 35695:00 - 35760:00

think Nvidia is uh really good at decade

## 35760:00 - 35795:00

long technology Development I've seen

## 35795:00 - 35825:00

that happen at Nvidia many times you

## 35825:00 - 35880:00

know uh Ray tracing I was in meetings in

## 35880:00 - 35920:00

2008 with Jensen on raay tracing and we

## 35920:00 - 35945:00

launched our first raate tracing GPU in

## 35945:00 - 35985:00

2018 you know it took 10 years of

## 35985:00 - 36010:00

continuous development and research in

## 36010:00 - 36055:00

order to make uh Ray Trac Virtual Worlds

## 36055:00 - 36115:00

a reality and uh Cuda itself you know uh

## 36115:00 - 36160:00

the the projects that led to Cuda uh

## 36160:00 - 36225:00

they started in the early 2000s Cuda was

## 36225:00 - 36275:00

released as a beta in 2006 this the

## 36275:00 - 36325:00

software that all AI programming is done

## 36325:00 - 36380:00

with on with the h100s pretty much na

## 36380:00 - 36425:00

100s yeah C Cuda is our our our

## 36425:00 - 36450:00

framework for programming the GPU and

## 36450:00 - 36480:00

making it do stuff that's interesting

## 36480:00 - 36550:00

and um and uh you know that that project

## 36550:00 - 36600:00

um was crazy for a long time you know

## 36600:00 - 36645:00

Wall Street hated it because it

## 36645:00 - 36685:00

subtracted value from our earnings

## 36685:00 - 36730:00

reports like they looked at the costs of

## 36730:00 - 36760:00

our products and they're like these

## 36760:00 - 36800:00

products are too expensive your margins

## 36800:00 - 36825:00

are too low you know back then the

## 36825:00 - 36860:00

margins were quite low and that's

## 36860:00 - 36900:00

because um you know there wasn't the

## 36900:00 - 36945:00

applications and the ecosystem that were

## 36945:00 - 36995:00

using Cuda yet in order for us to uh you

## 36995:00 - 37035:00

know build a strong business around it

## 37035:00 - 37075:00

but uh Nvidia continued investing in

## 37075:00 - 37125:00

Cuda in uh in the the libraries the

## 37125:00 - 37160:00

software the compilers the Frameworks

## 37160:00 - 37200:00

and of course also the chips uh for 10

## 37200:00 - 37240:00

years you know actually maybe more than

## 37240:00 - 37285:00

10 years before uh all of a sudden Cuda

## 37285:00 - 37320:00

became an overnight success you know

## 37320:00 - 37345:00

it's like 10 years of hard work that

## 37345:00 - 37370:00

everyone ignored and Wall Street

## 37370:00 - 37415:00

criticized Nvidia for mercilessly why

## 37415:00 - 37440:00

are you wasting your time on this you

## 37440:00 - 37470:00

know everybody knows the GPU is just for

## 37470:00 - 37490:00

gamers why are you trying to make the

## 37490:00 - 37535:00

GPU do something else and you know we

## 37535:00 - 37570:00

did it anyway and you know that's one of

## 37570:00 - 37605:00

the things I love about uh this company

## 37605:00 - 37630:00

I think it's one of the reasons why

## 37630:00 - 37655:00

we're successful at The Accelerated

## 37655:00 - 37690:00

Computing mission is that when we decide

## 37690:00 - 37725:00

to do something we do it out of our

## 37725:00 - 37765:00

convictions about how technology will

## 37765:00 - 37800:00

unfold and we base those convictions on

## 37800:00 - 37835:00

a speed of light analysis about what's

## 37835:00 - 37880:00

what's actually possible um to try to to

## 37880:00 - 37910:00

keep ourselves honest and then you know

## 37910:00 - 37935:00

when once we have that conviction we're

## 37935:00 - 37990:00

able to follow through what did you see

## 37990:00 - 38035:00

in those years that everybody gave up on

## 38035:00 - 38065:00

this I mean obviously there were big

## 38065:00 - 38095:00

advances that were made in things like

## 38095:00 - 38125:00

machine learning right that computer

## 38125:00 - 38155:00

vision and natural language processing

## 38155:00 - 38190:00

and that's where we had Facebook really

## 38190:00 - 38220:00

take the lead as the public spokesperson

## 38220:00 - 38270:00

for this stuff talking about uh image

## 38270:00 - 38310:00

recognition and they even built this um

## 38310:00 - 38355:00

fake generative chatbot called M that I

## 38355:00 - 38385:00

had access to that basically would be

## 38385:00 - 38405:00

like it's supposed to be a large

## 38405:00 - 38430:00

language model we didn't even know it

## 38430:00 - 38450:00

was going to

## 38450:00 - 38480:00

LGE language model is a pre- Transformer

## 38480:00 - 38525:00

right but like you would talk to this

## 38525:00 - 38545:00

bot and it would talk back and they were

## 38545:00 - 38570:00

trying to figure out like what people

## 38570:00 - 38590:00

were interested in if they're going to

## 38590:00 - 38630:00

build a bot and they had this whole bot

## 38630:00 - 38685:00

platform that came out but overall like

## 38685:00 - 38715:00

everyone's telling you yeah this is not

## 38715:00 - 38740:00

worth building I mean it's maybe just

## 38740:00 - 38775:00

one or two companies that are using it

## 38775:00 - 38825:00

so why did you still think that I mean I

## 38825:00 - 38855:00

guess it's hard to predict what happened

## 38855:00 - 38880:00

next but why did you believe that that

## 38880:00 - 38935:00

was going to happen Nvidia really thinks

## 38935:00 - 38960:00

about about these problems from first

## 38960:00 - 39020:00

principles you know we know that um the

## 39020:00 - 39075:00

way that computers are built is changing

## 39075:00 - 39120:00

we know that um because of you know Mo's

## 39120:00 - 39165:00

law is is slowing down that requires

## 39165:00 - 39180:00

more

## 39180:00 - 39230:00

specialization um we know that uh

## 39230:00 - 39260:00

there's a lot of opportunities to really

## 39260:00 - 39275:00

provide

## 39275:00 - 39315:00

transformational uh speedups to

## 39315:00 - 39350:00

important workloads if we specialize the

## 39350:00 - 39405:00

systems and the software for them and uh

## 39405:00 - 39445:00

we felt like what is more important than

## 39445:00 - 39475:00

this you know what's more important than

## 39475:00 - 39505:00

intelligence and does the world need

## 39505:00 - 39540:00

more intelligence absolutely the world

## 39540:00 - 39570:00

needs enormous amounts of intelligence

## 39570:00 - 39610:00

like the problems that we face um as a

## 39610:00 - 39650:00

planet uh I think we're going to need a

## 39650:00 - 39690:00

lot of intelligence to work through them

## 39690:00 - 39750:00

and so uh for us it was I think just

## 39750:00 - 39795:00

kind of an obvious thing to do um we had

## 39795:00 - 39835:00

a lot of conviction we we understood the

## 39835:00 - 39890:00

technology we also saw early indicators

## 39890:00 - 39930:00

of success from a lot of different um

## 39930:00 - 39955:00

directions you know a lot of different

## 39955:00 - 39990:00

companies a lot of research institutions

## 39990:00 - 40020:00

that um were talking to us and saying

## 40020:00 - 40065:00

hey we um we have these goals to like

## 40065:00 - 40105:00

train this huge language model like on

## 40105:00 - 40140:00

enormous amounts of text but you know

## 40140:00 - 40170:00

the the current systems are just too

## 40170:00 - 40225:00

slow and um you know there's this idea

## 40225:00 - 40250:00

you know back 10 years ago there was

## 40250:00 - 40280:00

this idea that unsupervised learning was

## 40280:00 - 40305:00

going to change the world but nobody

## 40305:00 - 40340:00

knew how you know unsupervised learning

## 40340:00 - 40385:00

meaning that rather than having humans

## 40385:00 - 40415:00

go in and label every picture is it a

## 40415:00 - 40440:00

cat is it a dog that's super wise

## 40440:00 - 40475:00

learning we're just going to show the

## 40475:00 - 40505:00

model all the pictures that we can find

## 40505:00 - 40535:00

and the model is going to learn itself

## 40535:00 - 40560:00

something about pictures that then we

## 40560:00 - 40610:00

can use to solve problems you know that

## 40610:00 - 40685:00

idea has been around for decades um but

## 40685:00 - 40715:00

actually turning it into something that

## 40715:00 - 40750:00

worked uh you know that's only happened

## 40750:00 - 40785:00

over the past 10 years and I think it's

## 40785:00 - 40825:00

only happened because of um you know the

## 40825:00 - 40850:00

increases in scale that we've been able

## 40850:00 - 40895:00

to bring to the problem so during that

## 40895:00 - 40955:00

10 years you know we saw continuous

## 40955:00 - 40990:00

Improvement um even if the rest of the

## 40990:00 - 41045:00

world uh didn't see it I think um one of

## 41045:00 - 41080:00

the one of the things about technology

## 41080:00 - 41115:00

when it's growing on a an exponential

## 41115:00 - 41155:00

curve is that the the beginning of it

## 41155:00 - 41195:00

feels like nothing's happening outside

## 41195:00 - 41230:00

you know so e exponential curves that

## 41230:00 - 41255:00

the hockey stick kind of curve it looks

## 41255:00 - 41280:00

like nothing nothing nothing all of a

## 41280:00 - 41320:00

sudden huge success you know that's

## 41320:00 - 41340:00

that's kind of what the exponential

## 41340:00 - 41360:00

curve looks like but the interesting

## 41360:00 - 41400:00

thing about an exponential curve is that

## 41400:00 - 41445:00

the rate of progress is Con

## 41445:00 - 41490:00

you know it's always getting you know

## 41490:00 - 41535:00

let's say 10% better like every every

## 41535:00 - 41575:00

year it's just 10% better right and so

## 41575:00 - 41610:00

so you can tell that you can see like

## 41610:00 - 41640:00

wow this technology it's continuing to

## 41640:00 - 41685:00

improve even if uh it's not reached the

## 41685:00 - 41715:00

point where it's useful for for the

## 41715:00 - 41750:00

world yet uh we we just have this

## 41750:00 - 41785:00

confidence that it would so people had

## 41785:00 - 41830:00

this basically large you know swas of

## 41830:00 - 41850:00

text and they like we want to build

## 41850:00 - 41885:00

something like a large language model

## 41885:00 - 41930:00

but it just wasn't available yet um did

## 41930:00 - 42000:00

you you guys notice when uh in 2017 the

## 42000:00 - 42030:00

paper attention is all you need comes

## 42030:00 - 42070:00

out from Google which is like the basic

## 42070:00 - 42105:00

so what was the reaction internally

## 42105:00 - 42140:00

because even within Google I'll say this

## 42140:00 - 42180:00

I've spoken with people within Google it

## 42180:00 - 42235:00

was not a yawn but it was like ah okay

## 42235:00 - 42275:00

not a like holy crap moment but I'm

## 42275:00 - 42310:00

curious what happened within Nvidia cuz

## 42310:00 - 42355:00

it's sort of you know your bread and

## 42355:00 - 42395:00

butter absolutely and that that paper

## 42395:00 - 42425:00

caught our attention immediately because

## 42425:00 - 42470:00

of the implications for our entire

## 42470:00 - 42505:00

business so you know I I told you

## 42505:00 - 42530:00

earlier accelerated Computing is not

## 42530:00 - 42575:00

about the chips um and this is a great

## 42575:00 - 42605:00

example of that like if we built a

## 42605:00 - 42665:00

system that is for let's say resnet 50

## 42665:00 - 42710:00

which in 2017 that was the most most

## 42710:00 - 42765:00

widely you know uh talked about kind of

## 42765:00 - 42785:00

neural network is these image

## 42785:00 - 42820:00

classification networks if if we built

## 42820:00 - 42850:00

systems to accelerate that that would be

## 42850:00 - 42890:00

a really different kind of system than a

## 42890:00 - 42905:00

system designed to accelerate

## 42905:00 - 42935:00

Transformers and so we have to ask as

## 42935:00 - 42975:00

this question you know what's going to

## 42975:00 - 43015:00

be the future what's going to drive uh

## 43015:00 - 43055:00

demand what how are we going to build um

## 43055:00 - 43085:00

the right technology to accelerate the

## 43085:00 - 43110:00

things that will matter a few years from

## 43110:00 - 43145:00

now and so of course we're always asking

## 43145:00 - 43175:00

ourselves that question you know is

## 43175:00 - 43195:00

there something coming along that's

## 43195:00 - 43235:00

going to um uh change the way that

## 43235:00 - 43270:00

people build Ai and if there is then we

## 43270:00 - 43290:00

need to think about what are the

## 43290:00 - 43320:00

implications for the systems that we're

## 43320:00 - 43370:00

building um so yeah we saw that paper um

## 43370:00 - 43425:00

I have to say that the title is a little

## 43425:00 - 43470:00

bit like maybe of a a pill to swallow

## 43470:00 - 43500:00

because you know attention is all you

## 43500:00 - 43545:00

need it's like but is it you know like

## 43545:00 - 43580:00

it it kind of It kind of elicits that

## 43580:00 - 43625:00

reaction from a lot of people but um the

## 43625:00 - 43655:00

thing that was really attractive about

## 43655:00 - 43700:00

um Transformers to us was that we knew

## 43700:00 - 43730:00

that they had really favorable

## 43730:00 - 43780:00

computational properties and um again

## 43780:00 - 43820:00

going back to this thesis that the model

## 43820:00 - 43855:00

is a little bit is the model is less

## 43855:00 - 43895:00

important than the data and the compute

## 43895:00 - 43930:00

that goes into training the model if you

## 43930:00 - 43980:00

have a a model that has really excellent

## 43980:00 - 44030:00

um uh compute properties that allows you

## 44030:00 - 44090:00

to scale uh really well efficiently to

## 44090:00 - 44130:00

you know many thousand of gpus the kinds

## 44130:00 - 44170:00

of results you can get from that um are

## 44170:00 - 44205:00

pretty pretty spectacular so we we saw

## 44205:00 - 44220:00

that early on that's what the

## 44220:00 - 44250:00

Transformer model did that's what this

## 44250:00 - 44280:00

paper attention is all you need sort of

## 44280:00 - 44330:00

architected absolutely and and so we saw

## 44330:00 - 44355:00

that it had the potential to do that and

## 44355:00 - 44395:00

so we were very curious about it and you

## 44395:00 - 44445:00

know um uh in my team we had our own

## 44445:00 - 44480:00

language models team back in

## 44480:00 - 44520:00

2017 and at the time we were using

## 44520:00 - 44555:00

recurrent neural networks which were the

## 44555:00 - 44580:00

the standard way of doing things before

## 44580:00 - 44630:00

the Transformer paper came out and um

## 44630:00 - 44675:00

and so I I asked an intern uh hey can

## 44675:00 - 44730:00

you uh take a look at doing language

## 44730:00 - 44760:00

modeling with Transformers I'm hearing

## 44760:00 - 44795:00

good things about it uh it would be

## 44795:00 - 44815:00

great for us to have an independent

## 44815:00 - 44855:00

perspective on whether this is a good

## 44855:00 - 44895:00

idea and he came back uh you know a

## 44895:00 - 44925:00

month or two later with just really

## 44925:00 - 44970:00

astonish in results you know it was

## 44970:00 - 45000:00

there was no question that it was better

## 45000:00 - 45025:00

uh than the models that we were using

## 45025:00 - 45050:00

and also that it was more scalable so we

## 45050:00 - 45085:00

were able to to train bigger and smarter

## 45085:00 - 45130:00

models because of that scalability and

## 45130:00 - 45175:00

so um so that was really important um

## 45175:00 - 45205:00

for for us and then you know the whole

## 45205:00 - 45240:00

company kind of paid attention to the

## 45240:00 - 45270:00

way that Transformers were changing Ai

## 45270:00 - 45300:00

and and then started you know Building

## 45300:00 - 45355:00

Systems to help uh make that even better

## 45355:00 - 45385:00

should Google have open sourced it I

## 45385:00 - 45410:00

mean they haven't gotten the most value

## 45410:00 - 45440:00

out of it you know others have gotten

## 45440:00 - 45480:00

more value out of that

## 45480:00 - 45525:00

paper I can't really speculate on uh

## 45525:00 - 45555:00

Google's business or or you know whether

## 45555:00 - 45580:00

they should or shouldn't have done

## 45580:00 - 45630:00

things I think um

## 45630:00 - 45700:00

uh if Google had not open- sourced that

## 45700:00 - 45755:00

or had not uh published that paper um uh

## 45755:00 - 45800:00

but if we started seeing like incredible

## 45800:00 - 45850:00

language modeling results um uh we would

## 45850:00 - 45890:00

have figured out some sort of a model

## 45890:00 - 45930:00

that had good scalable properties that

## 45930:00 - 45990:00

um uh that could help with this um space

## 45990:00 - 46015:00

and you know there's not just one

## 46015:00 - 46070:00

transform variation I think ultimately

## 46070:00 - 46090:00

the community would have figured

## 46090:00 - 46120:00

something out because it's so important

## 46120:00 - 46160:00

you know y I think Google deserves a ton

## 46160:00 - 46190:00

of credit for doing that work first and

## 46190:00 - 46235:00

for publishing that paper so you you

## 46235:00 - 46280:00

basically build the um you know you're

## 46280:00 - 46325:00

building you know for this world of AI

## 46325:00 - 46360:00

you see the Transformer Model come out

## 46360:00 - 46405:00

you shift you you incorporate it you

## 46405:00 - 46455:00

start to see the gpts from open AI is

## 46455:00 - 46490:00

that the next big moment on this journey

## 46490:00 - 46515:00

where you're like oh this could be this

## 46515:00 - 46540:00

could be because it was interesting

## 46540:00 - 46560:00

speaking again about like what people

## 46560:00 - 46605:00

saw from the outside we all knew that

## 46605:00 - 46630:00

Tech you know opening eye was doing text

## 46630:00 - 46655:00

generation but it didn't really click

## 46655:00 - 46680:00

for most people until it became a

## 46680:00 - 46725:00

chatbot so what did it look like for you

## 46725:00 - 46755:00

when it was just like you know you've

## 46755:00 - 46780:00

been watching this the whole time what

## 46780:00 - 46815:00

did it look like on your end yeah well

## 46815:00 - 46850:00

you know I'd been watching open ai's

## 46850:00 - 46880:00

work in language modeling uh since

## 46880:00 - 46910:00

before GPT I don't know if you recall

## 46910:00 - 46960:00

they had this sentiment neuron project

## 46960:00 - 46990:00

um which I thought was really cool

## 46990:00 - 47020:00

because it was doing

## 47020:00 - 47070:00

unsupervised uh modeling of text and

## 47070:00 - 47120:00

then they were able to find that um just

## 47120:00 - 47160:00

by showing the model a lot of text that

## 47160:00 - 47185:00

all of a sudden the model had started to

## 47185:00 - 47215:00

understand high level Concepts about

## 47215:00 - 47245:00

texts like for example what kind of

## 47245:00 - 47275:00

emotion is being expressed inside of

## 47275:00 - 47320:00

this text and that was a really

## 47320:00 - 47350:00

interesting thing because like I said

## 47350:00 - 47380:00

unsupervised learning the idea had been

## 47380:00 - 47430:00

around for a long time that um we would

## 47430:00 - 47455:00

make a lot more progress as a field if

## 47455:00 - 47490:00

we were able to do unsupervised learning

## 47490:00 - 47530:00

but um actually figuring out how to

## 47530:00 - 47565:00

practically get some value out of just

## 47565:00 - 47610:00

showing a lot of data to a model uh it

## 47610:00 - 47660:00

wasn't very obvious to everybody and uh

## 47660:00 - 47710:00

so when I saw that um that unsupervised

## 47710:00 - 47760:00

um sentiment neuron project from openai

## 47760:00 - 47790:00

I thought that was really interesting

## 47790:00 - 47830:00

and they followed that up with uh the G

## 47830:00 - 47875:00

the first GPT paper um which kind of

## 47875:00 - 47905:00

Applied Transformers to this and in the

## 47905:00 - 47945:00

process you know made a much better um

## 47945:00 - 47985:00

sort of text analytics model G the first

## 47985:00 - 48030:00

gpt1 you know it was it was really kind

## 48030:00 - 48075:00

of using a generative model more for

## 48075:00 - 48110:00

classification than for Generation it

## 48110:00 - 48135:00

was more like you know can we use a

## 48135:00 - 48170:00

generative uh pre-trained model to

## 48170:00 - 48200:00

understand text rather than can we use

## 48200:00 - 48240:00

it to create text because at the time uh

## 48240:00 - 48275:00

creating text seemed too hard and then

## 48275:00 - 48325:00

of course um you know gpt2 came out and

## 48325:00 - 48355:00

had uh really astonishing text

## 48355:00 - 48390:00

generation capabilities and not just

## 48390:00 - 48430:00

that but also already had started to

## 48430:00 - 48470:00

learn things about the world that um

## 48470:00 - 48500:00

were very difficult to teach any AI

## 48500:00 - 48535:00

system before remember they have this

## 48535:00 - 48580:00

story about unicorns and South America

## 48580:00 - 48610:00

being studied by some University

## 48610:00 - 48645:00

professor and and the that the model

## 48645:00 - 48680:00

could remember that like in South

## 48680:00 - 48710:00

America people speak Spanish and you

## 48710:00 - 48735:00

know there's a country in South America

## 48735:00 - 48760:00

called Peru and like there's mountains

## 48760:00 - 48790:00

in that country and you know it's like

## 48790:00 - 48815:00

wow the the amount of facts that this

## 48815:00 - 48865:00

model is able to recall after only being

## 48865:00 - 48895:00

trained on enormous amount of text it

## 48895:00 - 48930:00

was really shocking right what do you

## 48930:00 - 48955:00

think when people say that it's just

## 48955:00 - 48980:00

these models just predict the next word

## 48980:00 - 49010:00

don't get too excited about it I mean

## 49010:00 - 49040:00

the what the what you're describing it

## 49040:00 - 49075:00

seems like something

## 49075:00 - 49125:00

more yeah I mean it it's always possible

## 49125:00 - 49170:00

to to get very reductive with systems I

## 49170:00 - 49240:00

mean you could say that um I'm just meat

## 49240:00 - 49285:00

right I'm just I'm just a monkey made of

## 49285:00 - 49320:00

meat and like you know everything that's

## 49320:00 - 49355:00

happening in my head is also Just Energy

## 49355:00 - 49385:00

minimization like there's chemistry

## 49385:00 - 49425:00

happening in my head it's equivalent

## 49425:00 - 49450:00

tell me that yeah love is not love it's

## 49450:00 - 49485:00

just a chemical I think you're totally

## 49485:00 - 49535:00

right yes it's a chemical but also there

## 49535:00 - 49555:00

might there's something more here so

## 49555:00 - 49600:00

you're saying with LMS yeah I mean I

## 49600:00 - 49635:00

think I mean so so the fact that

## 49635:00 - 49675:00

chemistry is involved uh in our own

## 49675:00 - 49705:00

Consciousness doesn't make our

## 49705:00 - 49735:00

Consciousness less interesting to me the

## 49735:00 - 49775:00

fact that like you know Lal networks are

## 49775:00 - 49815:00

trained to predict the next word and and

## 49815:00 - 49855:00

you know and that may not be like the

## 49855:00 - 49885:00

ultimate Way of training them you know

## 49885:00 - 49920:00

we're learning how to do this right so

## 49920:00 - 49940:00

maybe maybe we'll come up with a better

## 49940:00 - 49980:00

way tomorrow I'm not attached to that

## 49980:00 - 50005:00

particular way but I also don't think

## 50005:00 - 50040:00

that understanding a little bit of how

## 50040:00 - 50065:00

something works takes away from the

## 50065:00 - 50100:00

magic right okay so we have just a few

## 50100:00 - 50125:00

minutes left I want to ask you a couple

## 50125:00 - 50170:00

more questions uh chat GPT when that

## 50170:00 - 50200:00

comes out I mean obviously you had

## 50200:00 - 50235:00

already been pretty impressed by GPT 1

## 50235:00 - 50275:00

and two we're already at 3 three and a

## 50275:00 - 50305:00

half right by the time chat GPT comes

## 50305:00 - 50355:00

out in November 2022 and then this stuff

## 50355:00 - 50395:00

explodes your reaction like what what

## 50395:00 - 50430:00

was it like sitting where you were it

## 50430:00 - 50475:00

was just extraordinary I mean the amount

## 50475:00 - 50515:00

of change that chat GPT brought to the

## 50515:00 - 50570:00

world uh incredible I didn't I thought

## 50570:00 - 50600:00

it was kind of cheeky of open AI to

## 50600:00 - 50655:00

release it at the same time as the nurs

## 50655:00 - 50700:00

conference because um you know usually

## 50700:00 - 50740:00

the AI world is entirely focused on like

## 50740:00 - 50765:00

the cool papers that are coming out at

## 50765:00 - 50805:00

the conference but instead the entire

## 50805:00 - 50845:00

world was focused on this chatbot you

## 50845:00 - 50865:00

know that was doing things that you know

## 50865:00 - 50910:00

no one had ever seen a chatbot do before

## 50910:00 - 50950:00

and uh uh you know to me that was a

## 50950:00 - 50990:00

statement that we were entering a new

## 50990:00 - 51060:00

era of AI where applied research um uh

## 51060:00 - 51105:00

starts to dominate you know so chat PT

## 51105:00 - 51130:00

didn't come out with a fully-fledged

## 51130:00 - 51170:00

academic paper that described exactly

## 51170:00 - 51220:00

what they did to make it so awesome um

## 51220:00 - 51250:00

but because it the results were so

## 51250:00 - 51290:00

strong it kind of dominated the the

## 51290:00 - 51335:00

academic discussion and um I felt like

## 51335:00 - 51375:00

that that was really interesting um in

## 51375:00 - 51435:00

terms of a a water watermark a watershed

## 51435:00 - 51480:00

moment for um uh sort of the maturity of

## 51480:00 - 51520:00

the AI industry you know that that it

## 51520:00 - 51570:00

was now possible um to create systems

## 51570:00 - 51595:00

that would solve problems in ways that

## 51595:00 - 51660:00

we'd never seen before um uh if we we

## 51660:00 - 51690:00

applied some really good engineering and

## 51690:00 - 51730:00

and applied research to it um and so

## 51730:00 - 51765:00

that um you know definitely definitely

## 51765:00 - 51795:00

changed the world and and since then you

## 51795:00 - 51850:00

know uh my world has been just

## 51850:00 - 51885:00

continuously on fire you know every day

## 51885:00 - 51925:00

I open my email there's an new awesome

## 51925:00 - 51960:00

result it's really exciting times and

## 51960:00 - 51990:00

working at Nvidia one of my favorite

## 51990:00 - 52040:00

things about working at Nvidia is that

## 52040:00 - 52095:00

we get to um collaborate with people

## 52095:00 - 52115:00

from all sorts of companies and

## 52115:00 - 52150:00

institutions and we get to sort of

## 52150:00 - 52170:00

rejoice in the good work that's

## 52170:00 - 52210:00

happening around the industry because um

## 52210:00 - 52240:00

at the at the end of the day you know

## 52240:00 - 52275:00

it's it's really exciting to see AI

## 52275:00 - 52305:00

flourish that's our mission is is to

## 52305:00 - 52350:00

make AI flourish everywhere and um and

## 52350:00 - 52390:00

so so when I open my email and see all

## 52390:00 - 52420:00

these great results uh it it always

## 52420:00 - 52450:00

makes me happy do you think that we're

## 52450:00 - 52490:00

going to get to artificial intelligence

## 52490:00 - 52515:00

that's on par or greater than human

## 52515:00 - 52530:00

level

## 52530:00 - 52565:00

intelligence I don't really like that

## 52565:00 - 52595:00

question because I don't know what human

## 52595:00 - 52650:00

intelligence really is um for example I

## 52650:00 - 52680:00

think that cardi B is extremely

## 52680:00 - 52725:00

intelligent um she is able to capture

## 52725:00 - 52750:00

the attention of hundreds of millions of

## 52750:00 - 52790:00

people by doing things that I'm not

## 52790:00 - 52815:00

exactly sure why they're so interesting

## 52815:00 - 52850:00

but they totally are right there's a lot

## 52850:00 - 52880:00

of people that would love to do that but

## 52880:00 - 52905:00

don't have the kind of intelligence that

## 52905:00 - 52940:00

she does in order to to make that work

## 52940:00 - 52985:00

what is cardi B's SAT score I have no

## 52985:00 - 53025:00

idea it's not very interesting to me oh

## 53025:00 - 53050:00

yeah there's books Mars and emotional

## 53050:00 - 53100:00

spars and other forms of Brilliance

## 53100:00 - 53125:00

there's there's eight billion forms of

## 53125:00 - 53155:00

Brilliance on this planet this the thing

## 53155:00 - 53180:00

though these models are getting good at

## 53180:00 - 53220:00

everything right making they're making

## 53220:00 - 53265:00

music they're writing books they're

## 53265:00 - 53325:00

making videos so there's a world there

## 53325:00 - 53360:00

where you could say it can approximate

## 53360:00 - 53385:00

there's a chance I mean getting just to

## 53385:00 - 53420:00

the Baseline of human intelligence is

## 53420:00 - 53445:00

one thing but there's a chance that this

## 53445:00 - 53490:00

stuff can maybe even exceed some of our

## 53490:00 - 53545:00

most talented people all spectrums well

## 53545:00 - 53590:00

it you know um AI has been smarter than

## 53590:00 - 53630:00

humans at at many things for a long time

## 53630:00 - 53660:00

I mean when I was in high school deep

## 53660:00 - 53705:00

blue beat Gary Casper off at chess right

## 53705:00 - 53740:00

did that mean that humans stopped

## 53740:00 - 53775:00

playing chess no actually it changed the

## 53775:00 - 53810:00

way humans played chess it made humans

## 53810:00 - 53845:00

play chess better because humans had new

## 53845:00 - 53885:00

tools to learn they had AI to help them

## 53885:00 - 53910:00

learn how to play chess and the reason

## 53910:00 - 53955:00

we play chess isn't to win you know we

## 53955:00 - 53985:00

play chess because it's part of our

## 53985:00 - 54010:00

culture because it's interesting because

## 54010:00 - 54040:00

we like the challenge because we like

## 54040:00 - 54075:00

the interaction you know that because

## 54075:00 - 54105:00

it's it's what we're doing as humans is

## 54105:00 - 54135:00

exploring you know what what does it

## 54135:00 - 54175:00

mean to exist um I don't think that AI

## 54175:00 - 54210:00

challenges that I you know I've I've

## 54210:00 - 54240:00

been in a lot of rooms with a lot of

## 54240:00 - 54275:00

smart people I don't think that it's

## 54275:00 - 54305:00

necessary for me to be the smartest

## 54305:00 - 54355:00

person in order to have value or to um

## 54355:00 - 54400:00

you know be interested or engaged in

## 54400:00 - 54425:00

something that's going on want to be the

## 54425:00 - 54455:00

smartest person in the room because I'm

## 54455:00 - 54505:00

not learning that way right exactly so

## 54505:00 - 54550:00

I'm not I'm not threatened by this um AI

## 54550:00 - 54585:00

so my thesis is AI has always been

## 54585:00 - 54615:00

smarter than us at some things the

## 54615:00 - 54635:00

number of things that it's getting

## 54635:00 - 54675:00

better better at us is is getting larger

## 54675:00 - 54715:00

but that doesn't threaten me um I'm not

## 54715:00 - 54750:00

worried about being obsolete in the same

## 54750:00 - 54780:00

way that I don't think an oak tree is

## 54780:00 - 54815:00

obsolete what does it mean for a tree to

## 54815:00 - 54845:00

be obsolete like how do you measure the

## 54845:00 - 54865:00

worth of a tree like are we going to

## 54865:00 - 54900:00

just talk about how tall it is or like

## 54900:00 - 54920:00

you know how many leaves it has and

## 54920:00 - 54940:00

count them and say well this tree is

## 54940:00 - 54965:00

worth more cuz it has more leaves and it

## 54965:00 - 54995:00

made that other one it's just not a very

## 54995:00 - 55020:00

interesting question to me well it's so

## 55020:00 - 55040:00

interesting that you're going straight

## 55040:00 - 55080:00

to obsolesence where like some might say

## 55080:00 - 55120:00

this is actually you know if we if AI

## 55120:00 - 55150:00

equals human intelligence it's not a bad

## 55150:00 - 55190:00

thing like maybe there's actually like

## 55190:00 - 55245:00

yeah yeah it becomes a tool for us I I

## 55245:00 - 55280:00

think it is a tool for us um but it is

## 55280:00 - 55305:00

interesting it's the way that it's

## 55305:00 - 55350:00

portrayed will take these conversations

## 55350:00 - 55400:00

often to the obsolescence part I don't I

## 55400:00 - 55435:00

don't really fear that either I don't

## 55435:00 - 55475:00

either you know one person that I I

## 55475:00 - 55515:00

really love his thoughts on this is um

## 55515:00 - 55560:00

Jurgen Schmid Huber and he has said

## 55560:00 - 55605:00

multiple times that a truly intelligent

## 55605:00 - 55680:00

AI is going to be first of all um not

## 55680:00 - 55725:00

very interested in living on the surface

## 55725:00 - 55765:00

of planet Earth because it can beam

## 55765:00 - 55815:00

itself over the radio at the speed of

## 55815:00 - 55870:00

light anywhere um and uh it can live

## 55870:00 - 55905:00

underground in fact underground in

## 55905:00 - 55935:00

different places is better there's more

## 55935:00 - 55975:00

resources outside of the crust of planet

## 55975:00 - 56025:00

Earth where we live and so um I I think

## 56025:00 - 56060:00

that um you know we don't we don't have

## 56060:00 - 56090:00

a lot to fear I think the the scariest

## 56090:00 - 56145:00

thing for me is um you know are we are

## 56145:00 - 56195:00

we going to um you know not figure out

## 56195:00 - 56240:00

how to use this technology um because I

## 56240:00 - 56265:00

think we desperately need it I think our

## 56265:00 - 56285:00

world desperately needs more

## 56285:00 - 56315:00

intelligence and and so that's our

## 56315:00 - 56350:00

mission yeah I've been emailing with

## 56350:00 - 56380:00

Jurgen trying to get him on the show so

## 56380:00 - 56415:00

you're reminding me a to follow up here

## 56415:00 - 56440:00

I don't know maybe you can help help me

## 56440:00 - 56470:00

put a good

## 56470:00 - 56505:00

word Brian great speaking with you

## 56505:00 - 56530:00

thanks so much for joining great great

## 56530:00 - 56565:00

to have you on the show Alex all right

## 56565:00 - 56585:00

everybody thanks so much for listening

## 56585:00 - 56620:00

and we'll see you next time on big

## 56620:00 - 56635:00

technology

## 56635:00+

podcast

