---
source: https://www.youtube.com/watch?v=Ri5lsPb7low
title: How I created my first Agent without code
author: Steph France
date: 2024-12-24
views: 3598
description: >-
  ✅ MUST WATCH 👇

  In this video I break down my most up to date framework that gives founders a
  simple roadmap to create unlimited marketing assets that speak directly to
  their customers' souls.

  https://youtu.be/QDvuD90XV9k


  GET THE BLUEPRINT FROM THE VIDEO 👇

  https://curiousmarketer.gumroad.com/l/simplest-ai-agent


  JOIN THE DISCORD SERVER👇

  https://discord.gg/HRbGnhsgYU



  👋 Who am I?


  Hi, I'm Stéphane, Curious marketer and independent consultant. (French, if you
  haven't noticed)

  During the day, I help D2C business owners to attract, convert and keep
  customers with smart marketing systems & quiz funnels.

  At night, I'm working on this channel trying to give my best to help founders
  to find, validate, launch and scale their business ideas.


  Let's connect:


  🐦  Twitter:  https://twitter.com/meetstef

  👨‍💻  Linkedin: https://www.linkedin.com/in/stephane-franceschini



  Description:


  Discover how to create a basic AI agent using no-code tools like Make.com in
  this detailed walkthrough. This video showcases a step-by-step process for
  building an autonomous synonym generator that iterates through tasks and
  stores results in Google Sheets. Perfect for no-code enthusiasts, marketers,
  and content creators, this guide explores webhooks, OpenAI API, Google Sheets
  integration, and iterative loops, providing practical insights into AI
  automation. Learn how to expand this concept for various applications such as
  customer service, marketing, and task automation. Ideal for anyone curious
  about starting with AI agents without programming.



  🔗Recommendation (contains affiliate links)


  Tools:


  Typeform (Quiz): https://typeform.partnerlinks.io/d8cao7ifvpc9

  Tally (Quiz): https://tally.so/

  Systeme.io (Funnel & Landing page):
  https://systeme.io/?sa=sa0002704595877dbd6bea03d606af6dad30a47d73cd


  Books:


  Cashvertising: https://amzn.to/3PVdkWf

  $100M Offers: https://amzn.to/3PPOU07

  Ask: https://amzn.to/3PPOU07

  Product launch: https://amzn.to/3xu9jBI

  The goal: https://amzn.to/4cOeM6E

  The beginning of Infinity: https://amzn.to/4bGt3RU

  (This last one has nothing to do with starting a business, it's just my best
  book ever 😅)


  Hardware:


  My Webcam (Mx Brio): https://amzn.to/3wMG0KU

  My Microphone (Shure MV7+): https://amzn.to/3V3bnIZ

  The Best Laptop in the World: https://amzn.to/3X453n8

  Portable second screen: https://amzn.to/4c2Xstg

  Gaming chair: https://amzn.to/3V5Iigf

  Stand up desk: https://amzn.to/3KKvmYt


  ⌚️Timestamps:


  00:00 - Introduction

  00:41 - Defining the AI agent concept

  02:08 - Setting up the agent in Make

  04:27 - Adding a looping mechanism

  06:03 - Example walkthrough of the AI agent

  09:03 - Use cases and potential improvements

  11:43 - Theoretical expansion of the system

  14:44 - Advanced features and future thoughts

  15:59 - Closing thoughts and feedback request
tags:
  - AI agent creation
  - make.com
  - AI
  - AI Agents
  - Open AI
  - Tutorial
  - No-code
  - Automations
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T11:53:54.896Z
---

# How I created my first Agent without code

## 00:00 - 60:00

so it's Christmas and I was thinking a

## 60:00 - 135:00

lot about AI agents for some reason um

## 135:00 - 155:00

and

## 155:00 - 195:00

actually specifically about how to

## 195:00 - 260:00

create AI agents the simplest way

## 260:00 - 310:00

possible and using no code because I

## 310:00 - 355:00

just can't code so I have to use no code

## 355:00 - 400:00

and I thought why not just making a

## 400:00 - 465:00

video where I share the first AI agent I

## 465:00 - 510:00

built which is kind of cool and which is

## 510:00 - 575:00

the very first iteration of what could

## 575:00 - 635:00

be something bigger only using noode

## 635:00 - 680:00

tools and especially make.com so this

## 680:00 - 715:00

video is probably going to be a little

## 715:00 - 750:00

bit more technical than usual and

## 750:00 - 795:00

shorter it's not prepared so I'm just

## 795:00 - 835:00

going to walk you through what I thought

## 835:00 - 895:00

about um this is a very simple make

## 895:00 - 955:00

scenario and my goal is to create um a

## 955:00 - 1015:00

system that I give a task

## 1015:00 - 1065:00

and it will iterate until he's done with

## 1065:00 - 1125:00

the task right and the first thing I

## 1125:00 - 1160:00

thought about um just to make it very

## 1160:00 - 1235:00

easy is um I want an agent to give me

## 1235:00 - 1300:00

the synonym of a word and to keep on

## 1300:00 - 1345:00

going with giving me new synonym I don't

## 1345:00 - 1375:00

know if I pronounce it correctly synonym

## 1375:00 - 1390:00

or

## 1390:00 - 1440:00

synonym pardon my French but I would say

## 1440:00 - 1495:00

synonym which is the word that has the

## 1495:00 - 1555:00

same same meaning as another word so

## 1555:00 - 1605:00

here is the web hook um if you don't

## 1605:00 - 1655:00

know what's a web hook it's a it's some

## 1655:00 - 1725:00

data that is sent through a new and

## 1725:00 - 1780:00

within the web hook I give one

## 1780:00 - 1855:00

world then I connect to the open AI

## 1855:00 - 1920:00

API and I connect specifically to an

## 1920:00 - 1970:00

assistant that I have created again if

## 1970:00 - 2010:00

you don't know what is an assistant

## 2010:00 - 2060:00

um it would require a lot of um

## 2060:00 - 2085:00

explanation but there is a lot of

## 2085:00 - 2135:00

content on YouTube about it so I will go

## 2135:00 - 2165:00

um straight to the point and just talk

## 2165:00 - 2210:00

about uh what it is that I've created So

## 2210:00 - 2250:00

within the open a API you can create an

## 2250:00 - 2300:00

assistant which is kind of a boat a boat

## 2300:00 - 2375:00

within open AI uh to whom you give a

## 2375:00 - 2425:00

task and you give some information and

## 2425:00 - 2475:00

you attribute a model to use um so this

## 2475:00 - 2520:00

is the name of my agent um it's not an

## 2520:00 - 2570:00

agent yet it's just a boat actually but

## 2570:00 - 2625:00

I call it AI agent test and is the

## 2625:00 - 2655:00

instruction is very simple you are a

## 2655:00 - 2685:00

synonym which

## 2685:00 - 2755:00

is which I thought here synonym expert

## 2755:00 - 2785:00

when you receive a word you will answer

## 2785:00 - 2835:00

with a synonym after five repetitions

## 2835:00 - 2875:00

with an S you will answer with the very

## 2875:00 - 2935:00

first word you were provided with okay

## 2935:00 - 2990:00

save so let's put it on the side now and

## 2990:00 - 3040:00

as you can see see here when I in this

## 3040:00 - 3090:00

module I access this agent and in the

## 3090:00 - 3175:00

message I only give the first world that

## 3175:00 - 3225:00

I want all right

## 3225:00 - 3300:00

so from there normally I just I I should

## 3300:00 - 3365:00

have only one word as the output of this

## 3365:00 - 3410:00

one of this module which is a synonym of

## 3410:00 - 3460:00

the the first word I gave it but I also

## 3460:00 - 3550:00

want to know what is happing and

## 3550:00 - 3610:00

here I will remove that for a while and

## 3610:00 - 3665:00

tell you later what it

## 3665:00 - 3725:00

is I have a column called threads which

## 3725:00 - 3790:00

is for the thread ID for to keep track

## 3790:00 - 3845:00

of the conversation input

## 3845:00 - 3920:00

output and here this is this module I

## 3920:00 - 3985:00

add a row to uh my Google sheet that I

## 3985:00 - 4030:00

just showed you and I put the thread ID

## 4030:00 - 4080:00

which is which comes from this module

## 4080:00 - 4130:00

the synonym which comes from this web

## 4130:00 - 4190:00

Hook and the result which comes from

## 4190:00 - 4240:00

this module it's just to keep track of

## 4240:00 - 4305:00

it but wait an agent is supposed to have

## 4305:00 - 4350:00

a loop it's supposed to iterate on what

## 4350:00 - 4390:00

it is

## 4390:00 - 4440:00

um it's supposed to be autonomous right

## 4440:00 - 4495:00

so normally I should have a a way for

## 4495:00 - 4545:00

the agents to understand what was the

## 4545:00 - 4575:00

last word and then go back to the

## 4575:00 - 4630:00

beginning and iterate based on the last

## 4630:00 - 4695:00

World U so that's why here I have a HTTP

## 4695:00 - 4765:00

request which basically take the the web

## 4765:00 - 4795:00

hook

## 4795:00 - 4860:00

and post it again so I basically post

## 4860:00 - 4920:00

the entry at the end of my scenario I

## 4920:00 - 4975:00

post the same web hook at uh as the as I

## 4975:00 - 5025:00

posted at the beginning and I also give

## 5025:00 - 5080:00

as the synonym the result the result the

## 5080:00 - 5105:00

output of this

## 5105:00 - 5195:00

one and I also give the thread ID so

## 5195:00 - 5245:00

this way I keep track of the

## 5245:00 - 5290:00

conversation because that's the

## 5290:00 - 5365:00

specificity of an AI uh assistant within

## 5365:00 - 5410:00

open AI is that you you get to talk in

## 5410:00 - 5440:00

the same conversation as long as you

## 5440:00 - 5505:00

keep the same thread ID all right

## 5505:00 - 5555:00

so now when I finish a scenario then it

## 5555:00 - 5615:00

goes back and starts a new scenario but

## 5615:00 - 5650:00

instead of having the word I gave it at

## 5650:00 - 5700:00

the beginning it has the word which was

## 5700:00 - 5775:00

the output of the previous run and

## 5775:00 - 5790:00

that's why

## 5790:00 - 5825:00

here I

## 5825:00 - 5925:00

got this um data that's my first try as

## 5925:00 - 5985:00

you can see that was a try just one solo

## 5985:00 - 6005:00

try

## 6005:00 - 6055:00

and here I gave the word Smuggler it

## 6055:00 - 6085:00

says trafficker it started again with

## 6085:00 - 6140:00

trafficker and it says dealer and then

## 6140:00 - 6205:00

here and VOR and VOR Amic and then it

## 6205:00 - 6255:00

was five times so now he says

## 6255:00 - 6305:00

smug and then it started again and it it

## 6305:00 - 6375:00

was running until I um decided to stop

## 6375:00 - 6440:00

it it could have run for basically let

## 6440:00 - 6515:00

me show you in action uh how it works

## 6515:00 - 6580:00

all right so I just grab the um address

## 6580:00 - 6625:00

of my web hook and I have it here

## 6625:00 - 6660:00

already so I I have the the address of

## 6660:00 - 6705:00

the web hook and then I go question mark

## 6705:00 - 6740:00

and then I was just doing it before but

## 6740:00 - 6780:00

I messed up with my recording so I'm

## 6780:00 - 6800:00

doing it again that's why I have the

## 6800:00 - 6850:00

word I wanted to show you so I just put

## 6850:00 - 6920:00

the first synonym as bottle and now

## 6920:00 - 6980:00

before I proceed I just turn on my

## 6980:00 - 7005:00

scenario

## 7005:00 - 7055:00

and now be prepared to have your mind

## 7055:00 - 7095:00

completely blown away because it is so

## 7095:00 - 7145:00

impressive are you ready

## 7145:00 - 7230:00

go all right and now we wait a little

## 7230:00 - 7280:00

bit and we will see it happen maybe we

## 7280:00 - 7320:00

can try to see it right away yeah as you

## 7320:00 - 7360:00

can see it's working right

## 7360:00 - 7420:00

now we cannot really see it

## 7420:00 - 7465:00

though we

## 7465:00 - 7515:00

should now we don't see it but here here

## 7515:00 - 7570:00

it's working yeah I know it's impressive

## 7570:00 - 7605:00

so I give it bottle and gave me flask

## 7605:00 - 7655:00

and then flask then it's vessel then

## 7655:00 - 7710:00

from thisel it goes back again then it's

## 7710:00 - 7790:00

container and okay now receptacle don't

## 7790:00 - 7815:00

know if you pronounce it this

## 7815:00 - 7895:00

way and then how many do I have butter

## 7895:00 - 7940:00

because I asked him I asked it every

## 7940:00 - 7975:00

five iteration go back to the first

## 7975:00 - 8000:00

world I gave you

## 8000:00 - 8040:00

all right so it works and now it goes

## 8040:00 - 8090:00

back again and basically as long as I'm

## 8090:00 - 8160:00

not stopping it it is continuing to run

## 8160:00 - 8200:00

forever and that is kind of a problem

## 8200:00 - 8215:00

for

## 8215:00 - 8280:00

me um so I'm stopping it right now it

## 8280:00 - 8325:00

has a bit of pain to stop because their

## 8325:00 - 8370:00

API is still running but that's not the

## 8370:00 - 8425:00

point what I wanted to show you here is

## 8425:00 - 8515:00

that as useless as uh this AI agent is

## 8515:00 - 8575:00

it is still it still has like 80% of

## 8575:00 - 8635:00

what you would want from an A agent um

## 8635:00 - 8680:00

and we could call it we could give it a

## 8680:00 - 8750:00

name you know like the Sino

## 8750:00 - 8815:00

name no I think it's a yeah synonym guy

## 8815:00 - 8845:00

so this is the guy that's when you want

## 8845:00 - 8900:00

a synonym then you send a webbook with

## 8900:00 - 8945:00

the One World and then it will iterate

## 8945:00 - 8995:00

and give you synonym forever uh but you

## 8995:00 - 9015:00

can have depending on what you are

## 9015:00 - 9045:00

working on if you working on content

## 9045:00 - 9090:00

creation or gross marketing or customer

## 9090:00 - 9140:00

service you can imagine tasks uh

## 9140:00 - 9185:00

specific and create those agent within

## 9185:00 - 9230:00

make in my opinion I mean probably

## 9230:00 - 9260:00

developers are going to get crazy here

## 9260:00 - 9295:00

because I'm just I just can't code so

## 9295:00 - 9335:00

this is my only way to think of how can

## 9335:00 - 9385:00

I create an agent right but I think this

## 9385:00 - 9420:00

is possible from this basis to create

## 9420:00 - 9465:00

different agents and I want to show you

## 9465:00 - 9510:00

how it could look like uh if you go a

## 9510:00 - 9545:00

little bit further but just

## 9545:00 - 9595:00

before I want to show you something else

## 9595:00 - 9660:00

which is let me bring it

## 9660:00 - 9735:00

here I just asked chat GPT what are the

## 9735:00 - 9795:00

requirement for a system using AI to be

## 9795:00 - 9860:00

called agentic or an AI

## 9860:00 - 9915:00

agent that's why I said 80% of the

## 9915:00 - 9955:00

qualities um because those are the

## 9955:00 - 10000:00

things that say that the Define what's

## 10000:00 - 10065:00

an agent basically so

## 10065:00 - 10105:00

autonomy not really at this point

## 10105:00 - 10145:00

because it needs to be uh started and

## 10145:00 - 10215:00

stopped right goal oriented yes I this

## 10215:00 - 10255:00

um somehow useless agent is goal

## 10255:00 - 10300:00

oriented it has only one goal perception

## 10300:00 - 10340:00

it doesn't really have a perception

## 10340:00 - 10380:00

although yes because it receives an

## 10380:00 - 10395:00

information he understands the

## 10395:00 - 10425:00

information and starts even though it's

## 10425:00 - 10485:00

very simple reasoning or decision making

## 10485:00 - 10530:00

and uh I would say yes since we are

## 10530:00 - 10565:00

iterating on the same conversation and

## 10565:00 - 10595:00

it keeps track of it and the fact that I

## 10595:00 - 10630:00

say every five iteration you go back to

## 10630:00 - 10675:00

the very first one then prove that there

## 10675:00 - 10725:00

is in this system as simple as this

## 10725:00 - 10775:00

there is some reasoning action yes it

## 10775:00 - 10835:00

takes action it actually um go ahead and

## 10835:00 - 10880:00

uh goes ahead and and create new roles

## 10880:00 - 10930:00

in the Google sheet U

## 10930:00 - 11000:00

adaptivity um no clearly not

## 11000:00 - 11065:00

I it could if I would then read the

## 11065:00 - 11110:00

previous entries of the Google Sheets

## 11110:00 - 11170:00

and and reiterate on it on on it so then

## 11170:00 - 11225:00

it will have adaptivity interactive

## 11225:00 - 11275:00

capabilities no but that is the next

## 11275:00 - 11310:00

step of the video uh that's what I'm

## 11310:00 - 11350:00

going to show you now persistence well

## 11350:00 - 11380:00

it never stops so I guess it's quite

## 11380:00 - 11420:00

persistent and boundaries of decision

## 11420:00 - 11455:00

making doesn't have it because if I

## 11455:00 - 11490:00

don't stop it it never stops so that is

## 11490:00 - 11530:00

something uh you need to consider before

## 11530:00 - 11595:00

starting such a system right but okay

## 11595:00 - 11650:00

now what if we think a little bit

## 11650:00 - 11710:00

further so as you can see here I take my

## 11710:00 - 11735:00

Demi

## 11735:00 - 11825:00

agents then I just add one more step

## 11825:00 - 11880:00

here so basically imagine if we have the

## 11880:00 - 11945:00

same thing so we have a a web hook and

## 11945:00 - 11985:00

with some information it then we have a

## 11985:00 - 12055:00

an assistant that has a certain role and

## 12055:00 - 12080:00

keep track of the

## 12080:00 - 12160:00

conversation then this assistant is Task

## 12160:00 - 12210:00

tasked to do two

## 12210:00 - 12265:00

things or several things one thing is

## 12265:00 - 12300:00

obviously to understand what he's doing

## 12300:00 - 12355:00

U then he goes ahead and he

## 12355:00 - 12430:00

decides which API it should call to

## 12430:00 - 12510:00

accomplish his task and here you can

## 12510:00 - 12580:00

have several apis in line or however you

## 12580:00 - 12620:00

want to position it then it goes I don't

## 12620:00 - 12655:00

want to say to explain how you would

## 12655:00 - 12695:00

position them uh within the me scenario

## 12695:00 - 12725:00

because that's not just the point of

## 12725:00 - 12755:00

this video the point is just the theory

## 12755:00 - 12810:00

of if you have your assistant that

## 12810:00 - 12850:00

decides and that's that's the very

## 12850:00 - 12910:00

important point the assistant decides

## 12910:00 - 12965:00

which API it needs to call and but he

## 12965:00 - 13005:00

has access only to the apis that you

## 13005:00 - 13045:00

gave it access to so for example here's

## 13045:00 - 13095:00

the API of Facebook ads so for example

## 13095:00 - 13140:00

you could go ahead and retrive Facebook

## 13140:00 - 13175:00

the insight about the the current

## 13175:00 - 13230:00

running campaign or a certain access to

## 13230:00 - 13290:00

Shopify or a certain access to pickup or

## 13290:00 - 13350:00

notion or here is a HTTP request because

## 13350:00 - 13395:00

if you're familiar with API with an HTTP

## 13395:00 - 13450:00

request you can access every single tool

## 13450:00 - 13495:00

that has an access basically

## 13495:00 - 13545:00

so now you get an information and you

## 13545:00 - 13585:00

have your assistant and you say okay

## 13585:00 - 13620:00

this is your task this is the access

## 13620:00 - 13660:00

that you have which one do you want to

## 13660:00 - 13690:00

call to get the information that you

## 13690:00 - 13750:00

need and then it will decide then you

## 13750:00 - 13795:00

call the API then you record everything

## 13795:00 - 13850:00

that is just for you to track right and

## 13850:00 - 13910:00

the second thing which uh happens in

## 13910:00 - 13970:00

parallel here is like not only you it

## 13970:00 - 14025:00

tells you what's the API it needs to

## 14025:00 - 14085:00

call but it also can tell you what's the

## 14085:00 - 14145:00

next step what's the step afterward

## 14145:00 - 14215:00

right and you can have it uh um at the

## 14215:00 - 14280:00

same time so you say which API do you

## 14280:00 - 14315:00

want to call and what's your next step

## 14315:00 - 14345:00

after that and then it gives you the two

## 14345:00 - 14395:00

answers and here you send it back or you

## 14395:00 - 14460:00

can also call it here and say cool here

## 14460:00 - 14520:00

are the results um from your API code

## 14520:00 - 14560:00

and then you send everything

## 14560:00 - 14655:00

back to the beginning with the reasoning

## 14655:00 - 14730:00

of I wanted to do that I call this API I

## 14730:00 - 14785:00

analyze this API that's my next move and

## 14785:00 - 14855:00

goes back now okay that's your mission

## 14855:00 - 14885:00

now that's your current information in

## 14885:00 - 14920:00

this conversation what else do you want

## 14920:00 - 14960:00

to do what API do you need to call and

## 14960:00 - 15005:00

then again and it goes back and at some

## 15005:00 - 15045:00

point you can imagine that there is a

## 15045:00 - 15095:00

condition for it to stop I don't know

## 15095:00 - 15155:00

how it's just me passing time and just

## 15155:00 - 15200:00

putting out the stuff that is in my mind

## 15200:00 - 15230:00

um yeah so I don't know if it makes

## 15230:00 - 15265:00

sense I honestly don't know I I'm I

## 15265:00 - 15295:00

would be surprised that there are many

## 15295:00 - 15350:00

people watching until uh this point but

## 15350:00 - 15415:00

if you do uh if you are um a

## 15415:00 - 15455:00

developer I would be really interested

## 15455:00 - 15495:00

in in knowing what you think about this

## 15495:00 - 15545:00

system in the comments if it makes sense

## 15545:00 - 15575:00

uh and if you are not a Dev and you're

## 15575:00 - 15630:00

like me uh you can just do no code stuff

## 15630:00 - 15665:00

um does that make sense and what kind of

## 15665:00 - 15740:00

use cases uh you can imagine going for

## 15740:00 - 15765:00

this is obviously just the very very

## 15765:00 - 15810:00

beginning but I think it's just a mental

## 15810:00 - 15850:00

framework of like when you start having

## 15850:00 - 15885:00

that in mind then you when you come

## 15885:00 - 15945:00

across something um then you can say oh

## 15945:00 - 15985:00

hey well maybe I can do a small agent

## 15985:00 - 16025:00

with that without using the fancy tools

## 16025:00 - 16065:00

that are I mean every tool now is in a

## 16065:00 - 16130:00

agent and um since weeks now I'm trying

## 16130:00 - 16185:00

to understand what is actually an agent

## 16185:00 - 16225:00

what does it do so yeah um let me know

## 16225:00 - 16255:00

in the comment if you find it useful

## 16255:00 - 16290:00

found it useful and if you have any idea

## 16290:00 - 16345:00

of other use cases and if it makes sense

## 16345:00 - 16385:00

whatever have a nice day Merry Christmas

## 16385:00+

and I see you in the next video bye

