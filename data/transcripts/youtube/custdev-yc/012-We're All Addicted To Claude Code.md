---
source: https://www.youtube.com/watch?v=qwmmWzPnhog
title: We're All Addicted To Claude Code
author: Y Combinator
date: 2026-02-06
views: 119660
description: >-
  Wondering why your maker-turned-manager suddenly seems distracted in meetings?
  Maybe they're addicted to coding agents! In this episode of Lightcone, Calvin
  French-Owen — a co-founder of Segment and former engineer on OpenAI's Codex
  team — joins us to talk about why coding agents suddenly feel so powerful, the
  differences between Codex, Claude Code, and Cursor, and what the future of
  work will look like.


  0:00 Intro

  1:15 Garry can’t stop using Claude Code!

  4:00 Contrast with IDE’s, context-splitting

  6:23 Distribution models, top down vs bottom up

  9:11 Licensing and optimization

  12:28 Tips on becoming a top 1% user of coding agents

  17:36 When can the agents work 24-48 hour running jobs on their own? 

  21:34 Can the agent teach things like architecture?

  26:27 Will the next generation have even better taste and multitasking
  ability? 

  29:58 Maker vs manager schedules

  31:36 How would Calvin build Segment now? 

  35:52 The importance of testing

  38:52 The Claude bots are talking (to each other!)

  40:10 Examples of complex issues, how will the tools evolve

  43:00 Outro


  Apply to Y Combinator: https://www.ycombinator.com/apply

  Work at a startup: https://www.ycombinator.com/jobs
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:38:37.708Z
---

# We're All Addicted To Claude Code

## 00:00 - 20:00

I feel like when I'm using quad code,

## 20:00 - 40:00

it's like, oh, I feel like I'm flying

## 40:00 - 50:00

through the code.

## 50:00 - 90:00

>> When it's in your CLI, this thing can

## 90:00 - 145:00

debug nested delayed jobs like five

## 145:00 - 180:00

levels in and figure out what the bug

## 180:00 - 210:00

was and then write a test for it and it

## 210:00 - 245:00

never happens again. This is insane. I

## 245:00 - 265:00

think everyone who's experimenting with

## 265:00 - 300:00

this stuff on like a hobbyist level or

## 300:00 - 325:00

at like a very small startup, they're

## 325:00 - 345:00

just pushing the coding agents as far as

## 345:00 - 370:00

they can go because it's like you don't

## 370:00 - 390:00

really have time to figure out anything

## 390:00 - 410:00

else. Like as a startup, you have

## 410:00 - 440:00

limited runway. You're just going to

## 440:00 - 475:00

orient around speed. I think at a bigger

## 475:00 - 510:00

company you have a lot more to lose.

## 510:00 - 530:00

>> What are some of the tips to become a

## 530:00 - 590:00

top 1% user of coding agents?

## 590:00 - 740:00

>> Yeah. What's your stack?

## 740:00 - 770:00

>> Hey everyone, welcome back to another

## 770:00 - 815:00

episode of the Ly Cone. Gary, are you

## 815:00 - 830:00

are you ready to record?

## 830:00 - 860:00

>> I'm I'm in plan mode right now, but

## 860:00 - 900:00

okay. Yeah, I guess it's time. Sorry

## 900:00 - 940:00

about that. Well, welcome to another

## 940:00 - 980:00

episode of the light cone. And today we

## 980:00 - 1010:00

have an incredible guest, Kelvin French

## 1010:00 - 1045:00

Owen. He's one of the first people to

## 1045:00 - 1100:00

create codecs at OpenAI and before that

## 1100:00 - 1130:00

he started Segment, which is

## 1130:00 - 1170:00

multi-billion dollar company that got to

## 1170:00 - 1220:00

a very successful exit. Kelvin, welcome

## 1220:00 - 1225:00

back.

## 1225:00 - 1240:00

>> Thanks for having me.

## 1240:00 - 1300:00

>> I guess what a crazy time for all of us.

## 1300:00 - 1345:00

Uh I recently got very very addicted to

## 1345:00 - 1390:00

Claude Code and uh I would describe it

## 1390:00 - 1450:00

as like 10 years ago I was a marathon

## 1450:00 - 1485:00

runner and I love doing it and then I

## 1485:00 - 1515:00

suffered a catastrophic knee injury

## 1515:00 - 1560:00

which is called manager mode

## 1560:00 - 1605:00

and I uh stopped coding which is tragic

## 1605:00 - 1645:00

and horrible. Uh but now the last nine

## 1645:00 - 1690:00

days have been like this incredible

## 1690:00 - 1745:00

unlock of all the things I remember

## 1745:00 - 1790:00

being able to do and it's like you know

## 1790:00 - 1830:00

I got a new total knee replacement and

## 1830:00 - 1860:00

actually it's a bionic knee and it

## 1860:00 - 1905:00

allows me to run five times faster.

## 1905:00 - 1935:00

What's your take on it? Because you're I

## 1935:00 - 1975:00

mean right out there at the forefront of

## 1975:00 - 2030:00

it. I mean codeex pioneered all of the a

## 2030:00 - 2070:00

lot of the ideas that now like everyone

## 2070:00 - 2110:00

still uses and codeex is still evolving

## 2110:00 - 2120:00

too.

## 2120:00 - 2165:00

>> For brief context when I was at openai

## 2165:00 - 2190:00

um I was working on the codeex web

## 2190:00 - 2235:00

project at the time cursor was out in

## 2235:00 - 2265:00

the market and they had kind of built

## 2265:00 - 2310:00

this shim uh around I think it was set

## 2310:00 - 2355:00

3.5 and it was able to work in your IDE.

## 2355:00 - 2400:00

FOD code had just come out uh and it was

## 2400:00 - 2440:00

working as a CLI and we kind of had this

## 2440:00 - 2490:00

idea like hey in the future coding is

## 2490:00 - 2505:00

really going to feel more like talking

## 2505:00 - 2550:00

to a co-orker like you're going to send

## 2550:00 - 2580:00

off a question and then they'll go off

## 2580:00 - 2605:00

and do something and come back to you

## 2605:00 - 2640:00

with a PR. Uh and so that's where we

## 2640:00 - 2670:00

started with this web view. Uh and

## 2670:00 - 2690:00

that's what we were building. I think

## 2690:00 - 2715:00

directionally that's still kind of

## 2715:00 - 2745:00

correct for where things should go. But

## 2745:00 - 2780:00

obviously now everyone is coding with

## 2780:00 - 2820:00

CLIs instead. Like they're using those

## 2820:00 - 2850:00

tools a lot more whether it's cloud code

## 2850:00 - 2885:00

or whether it's codecs. And I think at

## 2885:00 - 2925:00

least for me kind of the lesson in that

## 2925:00 - 2960:00

is I think in some sense you're right

## 2960:00 - 2990:00

that like everyone is going to become a

## 2990:00 - 3020:00

manager in the future or at least that's

## 3020:00 - 3050:00

my hottake but in order to get there

## 3050:00 - 3085:00

there are steps along the way and you

## 3085:00 - 3105:00

have to really build a lot of trust in

## 3105:00 - 3125:00

the model and understand what it's

## 3125:00 - 3175:00

doing. you recently came over to cloud

## 3175:00 - 3210:00

code. What's the transition been like in

## 3210:00 - 3245:00

terms of as using it as your you know

## 3245:00 - 3260:00

one of your stacks?

## 3260:00 - 3295:00

>> Yeah. Yeah. So cloud code is uh

## 3295:00 - 3330:00

certainly my kind of like daily driver

## 3330:00 - 3365:00

today. And honestly this has switched

## 3365:00 - 3400:00

every few months. Uh for a while I was

## 3400:00 - 3430:00

deeply in cursor. I think their new

## 3430:00 - 3455:00

model which is really fast is actually

## 3455:00 - 3500:00

quite good. Then I kind of moved over to

## 3500:00 - 3535:00

quad code especially with Opus. Cloud

## 3535:00 - 3565:00

code is a really interesting product and

## 3565:00 - 3595:00

I think it's underrated how good the

## 3595:00 - 3635:00

both product and model are working

## 3635:00 - 3685:00

together. if you study them closely, I

## 3685:00 - 3715:00

think one of the things that claude code

## 3715:00 - 3745:00

does in particular that's really amazing

## 3745:00 - 3800:00

is split up context well and so if you

## 3800:00 - 3825:00

look at uh I don't know things like

## 3825:00 - 3865:00

skills or sub agents like when you ask

## 3865:00 - 3895:00

cla code to do something it will

## 3895:00 - 3945:00

typically spawn an explore sub agent or

## 3945:00 - 3975:00

like multiple ones and basically each of

## 3975:00 - 4025:00

those are running haik coup to traverse

## 4025:00 - 4050:00

the file system and kind of like explore

## 4050:00 - 4070:00

what's there and they're doing it in

## 4070:00 - 4105:00

their own context window and I think

## 4105:00 - 4140:00

enthropic has kind of like figured

## 4140:00 - 4185:00

something out here around given a task

## 4185:00 - 4210:00

does that task fit in the context window

## 4210:00 - 4235:00

or should I actually like split it into

## 4235:00 - 4265:00

many more and the models are like

## 4265:00 - 4300:00

insanely good at this which I think

## 4300:00 - 4320:00

gives them really good results

## 4320:00 - 4350:00

>> and I think the fascinating thing is

## 4350:00 - 4390:00

because it's on the terminal is the

## 4390:00 - 4440:00

purest form for composible atomic

## 4440:00 - 4480:00

integrations because if you came from ID

## 4480:00 - 4510:00

first world which is where cursor was

## 4510:00 - 4560:00

and I suppose codeex too this concept of

## 4560:00 - 4600:00

uh finding the context more free form

## 4600:00 - 4660:00

wouldn't come out so natural right

## 4660:00 - 4690:00

string which is so unique.

## 4690:00 - 4730:00

>> Yeah. And I personally I was surprised I

## 4730:00 - 4750:00

don't know how you all feel but I was

## 4750:00 - 4770:00

surprised that like

## 4770:00 - 4800:00

>> weird it's like a weird retro future

## 4800:00 - 4835:00

that like the CLI which are the

## 4835:00 - 4870:00

technology from 20 years ago have

## 4870:00 - 4905:00

somehow beaten out all the actual

## 4905:00 - 4925:00

ideides which were supposed to be the

## 4925:00 - 4930:00

future.

## 4930:00 - 4965:00

>> 100%. Yeah. And I I think it's important

## 4965:00 - 5000:00

actually to claude code that it's not an

## 5000:00 - 5045:00

IDE because it sort of distances you

## 5045:00 - 5080:00

from the code that's being written. Like

## 5080:00 - 5105:00

IDEs are all about exploring files,

## 5105:00 - 5120:00

right? and you're like trying to keep

## 5120:00 - 5140:00

all the state in your head and

## 5140:00 - 5175:00

understand what's going on. But the fact

## 5175:00 - 5205:00

that a CLI is like a totally different

## 5205:00 - 5225:00

thing means that they have a lot more

## 5225:00 - 5270:00

freedom in terms of how it feels. And I

## 5270:00 - 5290:00

I don't know about you, but I feel like

## 5290:00 - 5310:00

when I'm using cloud code, it's like,

## 5310:00 - 5330:00

oh, I feel like I'm flying through the

## 5330:00 - 5350:00

code, you know? It's like there's all

## 5350:00 - 5375:00

sorts of things going. There's like

## 5375:00 - 5405:00

little progress indicators. It's kind of

## 5405:00 - 5440:00

like giving me status updates, but like

## 5440:00 - 5465:00

the code that's being written is not the

## 5465:00 - 5490:00

front and center thing.

## 5490:00 - 5525:00

>> I mean, dev environments are so messy. I

## 5525:00 - 5575:00

mean, I really like how clean a sandbox

## 5575:00 - 5615:00

conceptually is.

## 5615:00 - 5645:00

But then I just ran into all these crazy

## 5645:00 - 5700:00

issues like trying to do just simple

## 5700:00 - 5730:00

testing, right? It needs to access

## 5730:00 - 5780:00

Postgress and then it can't do it or you

## 5780:00 - 5830:00

know my codeex.md ended up being 20

## 5830:00 - 5865:00

lines long and even then it didn't work.

## 5865:00 - 5900:00

When it's in your CLI, it could just

## 5900:00 - 5940:00

access your development database. I mean

## 5940:00 - 5960:00

I'm not sure if I'm supposed to do this,

## 5960:00 - 5995:00

but I've actually also had it access my

## 5995:00 - 6035:00

production database to do

## 6035:00 - 6070:00

>> and uh it can just do it. It's like,

## 6070:00 - 6105:00

yeah, okay, here. Like, I looked into it

## 6105:00 - 6130:00

and I think this happened and I'm going

## 6130:00 - 6165:00

to debug this, you know, concurrency

## 6165:00 - 6205:00

issue. I was like, oh my god, like this

## 6205:00 - 6260:00

thing can debug nested delayed jobs like

## 6260:00 - 6300:00

five levels in and figure out what the

## 6300:00 - 6330:00

bug was and then write a test for it and

## 6330:00 - 6365:00

it never happens again. This is insane.

## 6365:00 - 6405:00

>> Yeah. And I think that distribution mode

## 6405:00 - 6435:00

is frankly underrated. like thinking

## 6435:00 - 6470:00

about a cursor or a cloud code or a

## 6470:00 - 6500:00

codec CLI, the fact that you can just

## 6500:00 - 6535:00

download it and use it without having to

## 6535:00 - 6575:00

get it permissions or anything makes a

## 6575:00 - 6600:00

huge difference. And actually, I was

## 6600:00 - 6620:00

playing around with a product the other

## 6620:00 - 6670:00

day where you download a desktop app

## 6670:00 - 6710:00

>> and then it execs the clawed code that

## 6710:00 - 6745:00

you have running on your laptop and uses

## 6745:00 - 6785:00

that and communicates back via an MCP

## 6785:00 - 6820:00

server to the desktop product. Mhm. And

## 6820:00 - 6850:00

>> it's like this is a very interesting way

## 6850:00 - 6905:00

of now starting to work with your laptop

## 6905:00 - 6925:00

where you don't have to get anyone's

## 6925:00 - 6945:00

permission to do it. You just download

## 6945:00 - 6965:00

the product and go.

## 6965:00 - 6990:00

>> Yeah. I was looking at like New Relic

## 6990:00 - 7030:00

has an MCP but you know Sentry you can

## 7030:00 - 7070:00

like copy markdown but like it's like an

## 7070:00 - 7105:00

auto bug fixer basically. It's right

## 7105:00 - 7115:00

there.

## 7115:00 - 7140:00

>> It's super interesting that in a world

## 7140:00 - 7170:00

where things are changing so fast you

## 7170:00 - 7195:00

really want your product to have a

## 7195:00 - 7230:00

bottoms up distribution not top down

## 7230:00 - 7265:00

because like top down is like just too

## 7265:00 - 7300:00

slow. like the CTO of a company is going

## 7300:00 - 7330:00

to be like have all these concerns about

## 7330:00 - 7365:00

security and privacy and what if and

## 7365:00 - 7395:00

control exactly versus like the

## 7395:00 - 7415:00

engineers just like install the thing

## 7415:00 - 7435:00

and start using like this thing is

## 7435:00 - 7445:00

amazing.

## 7445:00 - 7470:00

>> Yeah, I think that's right. The one

## 7470:00 - 7495:00

thing I do struggle with I mean I'm like

## 7495:00 - 7545:00

a B2B enterprise guy generally but I

## 7545:00 - 7570:00

feel like there's some amount of moat

## 7570:00 - 7600:00

that happens when you do that top down

## 7600:00 - 7630:00

sale and there's got to be some company

## 7630:00 - 7660:00

who manages to crack it where it's like

## 7660:00 - 7690:00

oh this is a thing that everyone has

## 7690:00 - 7725:00

access to maybe individual people can

## 7725:00 - 7765:00

take it up. That was the original um

## 7765:00 - 7805:00

Netscape Navigator. It was free for

## 7805:00 - 7850:00

non-commercial use and then uh people

## 7850:00 - 7875:00

would just download it and use it for

## 7875:00 - 7910:00

commercial use and then they could just

## 7910:00 - 7950:00

track down the IPs and figure out uh

## 7950:00 - 7980:00

exactly how many clients were in all of

## 7980:00 - 8015:00

these different companies and say

## 8015:00 - 8035:00

>> you should pay for this. You're in

## 8035:00 - 8065:00

violation but all you have to do is buy

## 8065:00 - 8105:00

a license. So I'd be curious if you

## 8105:00 - 8145:00

could do that work again here. I mean

## 8145:00 - 8170:00

that your point about distribution is

## 8170:00 - 8210:00

very interesting because uh now people

## 8210:00 - 8245:00

are probably just making architecture

## 8245:00 - 8300:00

decisions about what to use directly in

## 8300:00 - 8340:00

claude code like they might not even

## 8340:00 - 8385:00

know what you know what analytics to use

## 8385:00 - 8415:00

and it's like oh yeah as long as cla

## 8415:00 - 8445:00

code says use post hog like they're

## 8445:00 - 8465:00

using post hog

## 8465:00 - 8505:00

>> 100%. One of the companies who I advise

## 8505:00 - 8535:00

was talking about their like GEO

## 8535:00 - 8570:00

strategy. This is like the generative

## 8570:00 - 8600:00

optimization or how you show up in chat

## 8600:00 - 8635:00

bots. And what he was saying is funny is

## 8635:00 - 8655:00

one of their competitors had put

## 8655:00 - 8695:00

together a like top five list of like

## 8695:00 - 8720:00

tools in their category that you should

## 8720:00 - 8750:00

be using. And of course their tool is

## 8750:00 - 8785:00

ranked at the top of this top five list.

## 8785:00 - 8810:00

And like any human looking at this would

## 8810:00 - 8830:00

be like, oh, this is so obviously

## 8830:00 - 8855:00

biased. It's like the top tool is the

## 8855:00 - 8895:00

one that's in the domain, you know? But

## 8895:00 - 8935:00

the LMS get fooled and like they're

## 8935:00 - 8960:00

pulling together a bunch of contexts and

## 8960:00 - 8975:00

they're saying like, "Oh, this is the

## 8975:00 - 9000:00

top." And then they'll just recommend

## 9000:00 - 9030:00

it. I think yeah, if you're selling a

## 9030:00 - 9060:00

developer tool, like having good docs

## 9060:00 - 9080:00

that are out there, like having social

## 9080:00 - 9125:00

proof, like maybe being posted on Reddit

## 9125:00 - 9150:00

a little bit more, all of that helps

## 9150:00 - 9175:00

your case tremendously,

## 9175:00 - 9205:00

>> which is why I think a lot of the open-

## 9205:00 - 9250:00

source uh projects have taken off a lot

## 9250:00 - 9285:00

more. I think one of the examples is

## 9285:00 - 9305:00

Superbase actually.

## 9305:00 - 9340:00

>> Yeah. Yeah. uh which really took off

## 9340:00 - 9370:00

last year and part of it is because they

## 9370:00 - 9400:00

have such a good open- source

## 9400:00 - 9425:00

documentation how to set up a bunch of

## 9425:00 - 9460:00

stuff. Whenever someone asks how to set

## 9460:00 - 9485:00

up anything that you need some sort of

## 9485:00 - 9540:00

backend firebased type of transaction

## 9540:00 - 9590:00

the default answer from all the LMS is

## 9590:00 - 9615:00

actually superbase. I was just trying

## 9615:00 - 9635:00

some of these questions that comes from

## 9635:00 - 9665:00

that. The thing is it's winning the

## 9665:00 - 9695:00

internet and it was like that before

## 9695:00 - 9735:00

when it was like Stack Overflow and

## 9735:00 - 9770:00

searching Google and then now that

## 9770:00 - 9820:00

nobody uses Google anymore. It's like

## 9820:00 - 9855:00

crazy. You just Yeah, it's kind of the

## 9855:00 - 9870:00

same deal.

## 9870:00 - 9910:00

>> I I will say it does help open source

## 9910:00 - 9940:00

disproportionately. I would say like I

## 9940:00 - 9955:00

don't know if you all saw there was a

## 9955:00 - 9980:00

ramp blog post that they recently

## 9980:00 - 10000:00

published about building their own

## 10000:00 - 10020:00

coding agent and they were mentioning

## 10020:00 - 10060:00

that they use open code as a harness um

## 10060:00 - 10100:00

because the model can look and see the

## 10100:00 - 10120:00

source code and understand how it's

## 10120:00 - 10145:00

working. And I I do this all the time

## 10145:00 - 10175:00

with open source products. I'll like

## 10175:00 - 10205:00

clone the repo and then spin up codeex

## 10205:00 - 10225:00

or cloud code and be like, "Hey, give me

## 10225:00 - 10250:00

a walkthrough of what's going on here

## 10250:00 - 10270:00

and it's really useful."

## 10270:00 - 10290:00

>> What do you think are some of the tips

## 10290:00 - 10325:00

for anyone that wants to build a coding

## 10325:00 - 10360:00

agent since you've uh done it a lot?

## 10360:00 - 10405:00

What are what are some uh now lessons

## 10405:00 - 10435:00

that you learned that you want to share?

## 10435:00 - 10470:00

>> I mean, I think the number one thing uh

## 10470:00 - 10515:00

is managing context well. Basically, we

## 10515:00 - 10555:00

kind of had like a checkpoint for uh I

## 10555:00 - 10580:00

think it was 03 like one of the

## 10580:00 - 10605:00

reasoning models and then we did a bunch

## 10605:00 - 10640:00

of fine-tuning on it um in reinforcement

## 10640:00 - 10660:00

learning where it's like oh you're given

## 10660:00 - 10685:00

a bunch of questions to like solve these

## 10685:00 - 10720:00

coding problems or like fix tests or

## 10720:00 - 10755:00

whatever or implement a feature um and

## 10755:00 - 10790:00

then the model was RL to respond to

## 10790:00 - 10825:00

those. And so I think most people are

## 10825:00 - 10860:00

not going to be doing that right but the

## 10860:00 - 10885:00

things that you can do are figure out

## 10885:00 - 10935:00

like hey what context should I be

## 10935:00 - 10960:00

supplying to this agent to get the best

## 10960:00 - 10995:00

possible result. And so for cloud code,

## 10995:00 - 11015:00

if you watch it working, it's like, oh,

## 11015:00 - 11035:00

I'm going to like spawn a bunch of these

## 11035:00 - 11075:00

explore sub agents. They will like

## 11075:00 - 11105:00

search for different patterns in the

## 11105:00 - 11140:00

file system. They will come back. Uh

## 11140:00 - 11165:00

they will have this context. They'll

## 11165:00 - 11185:00

summarize it for me and then I'll have

## 11185:00 - 11210:00

someplace to go. It's interesting

## 11210:00 - 11250:00

watching like different agents structure

## 11250:00 - 11285:00

this context. Uh like I think cursor

## 11285:00 - 11310:00

takes an approach where they actually do

## 11310:00 - 11340:00

semantic search where they embed

## 11340:00 - 11390:00

everything and figure out like hey what

## 11390:00 - 11425:00

query is closest to this? If you look at

## 11425:00 - 11465:00

a codeex or a cloud code, uh they

## 11465:00 - 11500:00

actually just use like grip.

## 11500:00 - 11530:00

>> And I think that works because well,

## 11530:00 - 11570:00

>> yeah, it works very well because code is

## 11570:00 - 11600:00

very context dense.

## 11600:00 - 11625:00

>> Um like if you think about lines of

## 11625:00 - 11645:00

code, it's like each line is probably

## 11645:00 - 11675:00

less than 80 characters. There's not a

## 11675:00 - 11715:00

lot of like big like data blobs or like

## 11715:00 - 11745:00

JSON in your codebase. Maybe there's

## 11745:00 - 11780:00

some, but not a lot. You can respect git

## 11780:00 - 11805:00

ignore to figure out and like filter out

## 11805:00 - 11835:00

stuff that's just not relevant or is

## 11835:00 - 11870:00

like packaged. And you can use gp and

## 11870:00 - 11905:00

rip grep to like find context around the

## 11905:00 - 11925:00

code which probably gives you a good

## 11925:00 - 11945:00

sense for what that code is doing. And

## 11945:00 - 11970:00

you can navigate the f folder structure.

## 11970:00 - 12005:00

>> And also elements are really good at

## 12005:00 - 12050:00

emitting very complicated gp expressions

## 12050:00 - 12075:00

that would like torture a human.

## 12075:00 - 12100:00

>> Yes. Yeah. Yeah. Yeah. Yeah. This is

## 12100:00 - 12145:00

like the RL in practice.

## 12145:00 - 12180:00

>> Yeah. And so I think all of that like if

## 12180:00 - 12205:00

you're trying to build a system well I'm

## 12205:00 - 12230:00

trying to build systems that integrate

## 12230:00 - 12275:00

uh agents for non-coding work. Uh I

## 12275:00 - 12290:00

think you can learn a lot of those

## 12290:00 - 12330:00

lessons and say like hey how do I get my

## 12330:00 - 12360:00

data in the format that is like maybe

## 12360:00 - 12395:00

closest to code where the model can like

## 12395:00 - 12430:00

peak and look at like areas around it

## 12430:00 - 12465:00

and get the right structured data.

## 12465:00 - 12505:00

>> So given this is how a lot of the

## 12505:00 - 12535:00

superpowers for the best coding agents

## 12535:00 - 12580:00

is context engineering. What are some of

## 12580:00 - 12640:00

the tips to become a top 1% user of

## 12640:00 - 12650:00

coding agents?

## 12650:00 - 12675:00

>> Yeah. What's your stack?

## 12675:00 - 12700:00

>> Yeah. What what do you do to be so

## 12700:00 - 12725:00

productive with it? one is if you're

## 12725:00 - 12785:00

able to use uh just generally far less

## 12785:00 - 12820:00

code and plumbing. Um so a lot of what I

## 12820:00 - 12860:00

do is like deploy stacks on like

## 12860:00 - 12890:00

Verscell or Nex.js or like Cloudflare

## 12890:00 - 12905:00

workers where there's kind of like

## 12905:00 - 12925:00

already a bunch of boiler plate like

## 12925:00 - 12960:00

taking care of for you and then you

## 12960:00 - 12985:00

don't really have to think that much

## 12985:00 - 13015:00

about like hey I need to stand up like

## 13015:00 - 13040:00

all these different services and deal

## 13040:00 - 13070:00

with like service discovery and like

## 13070:00 - 13100:00

registering on like some sort of central

## 13100:00 - 13120:00

endpoint or like all these databases.

## 13120:00 - 13155:00

It's like oh like everything is pretty

## 13155:00 - 13205:00

roughly defined in this like one or 200

## 13205:00 - 13255:00

lines of code. I tend to operate more

## 13255:00 - 13285:00

towards microservices for that as well

## 13285:00 - 13310:00

or like individual packages that are

## 13310:00 - 13340:00

fairly well structured. I think it's

## 13340:00 - 13375:00

also worth knowing like what the LLM

## 13375:00 - 13420:00

superpowers are like in general coding

## 13420:00 - 13460:00

agents are I think Andre Carpathy just

## 13460:00 - 13480:00

tweeted about this. They're like super

## 13480:00 - 13520:00

persistent so they will keep going no

## 13520:00 - 13575:00

matter what. they end up uh typically

## 13575:00 - 13625:00

just making more of whatever's there. So

## 13625:00 - 13645:00

if you're trying to direct them to do

## 13645:00 - 13700:00

something, it's worth like I mean I can

## 13700:00 - 13730:00

pick on OpenAI slightly in this example.

## 13730:00 - 13765:00

OpenAI has like a giant monor repo. It's

## 13765:00 - 13810:00

been there for uh a few years now and

## 13810:00 - 13845:00

has like I don't know thousands of

## 13845:00 - 13870:00

engineers who are committing. Some of

## 13870:00 - 13900:00

those engineers are like super senior

## 13900:00 - 13940:00

meta folks who came in and are like know

## 13940:00 - 13965:00

exactly how to write production code.

## 13965:00 - 14030:00

Some are like new PhDs. It's like uh a

## 14030:00 - 14070:00

pretty wide range and so the LM will

## 14070:00 - 14090:00

pick up different things depending on

## 14090:00 - 14110:00

where you direct it. I think there's a

## 14110:00 - 14145:00

lot of room actually for coding agents

## 14145:00 - 14170:00

to figure out like what is the like

## 14170:00 - 14200:00

optimal type of code that we should

## 14200:00 - 14230:00

produce. I mean obviously giving the

## 14230:00 - 14260:00

model a way to check its work helps

## 14260:00 - 14300:00

improve performance drastically. So the

## 14300:00 - 14335:00

more that you can run tests in lint uh

## 14335:00 - 14380:00

CI etc. Um personally I also use code

## 14380:00 - 14415:00

review bots pretty aggressively. Um I

## 14415:00 - 14460:00

know like reptile YC company is really

## 14460:00 - 14495:00

good. Um, I use the cursor bug bot has

## 14495:00 - 14520:00

gotten quite good and I actually like

## 14520:00 - 14560:00

codeex for code review as well. I find

## 14560:00 - 14590:00

it does a very good job on correctness.

## 14590:00 - 14620:00

So, those are all things that like the

## 14620:00 - 14650:00

agents are good at. Uh, and they're

## 14650:00 - 14685:00

excellent exploring the codebase too. I

## 14685:00 - 14720:00

think areas where they don't do well,

## 14720:00 - 14760:00

uh, they make more. If your goal is not

## 14760:00 - 14780:00

to make more, they'll like often

## 14780:00 - 14815:00

duplicate code and like spend a bunch of

## 14815:00 - 14845:00

time re-implementing things that like

## 14845:00 - 14875:00

you're like, "Oh, of course you didn't

## 14875:00 - 14900:00

want to do this." I think context

## 14900:00 - 14940:00

poisoning is a real thing where it kind

## 14940:00 - 15000:00

of like goes down one loop and it will

## 15000:00 - 15035:00

continue because it has this persistence

## 15035:00 - 15070:00

but it's referring back to tokens which

## 15070:00 - 15120:00

are like not right in terms of pursuing

## 15120:00 - 15155:00

a solution. Um and so one thing that I

## 15155:00 - 15200:00

often do is like very actively clear

## 15200:00 - 15210:00

context

## 15210:00 - 15235:00

>> like how often

## 15235:00 - 15290:00

>> usually uh when it gets above like 50%

## 15290:00 - 15300:00

tokens.

## 15300:00 - 15310:00

>> Oh wow.

## 15310:00 - 15350:00

>> Yeah. Yeah. I don't there's this guy Dex

## 15350:00 - 15380:00

uh from this company Human Layer that

## 15380:00 - 15395:00

was actually another YC company.

## 15395:00 - 15430:00

>> Yes, a YC company from Fall 24.

## 15430:00 - 15450:00

>> Yeah. Yeah. And he talks a lot about it.

## 15450:00 - 15455:00

Yeah.

## 15455:00 - 15490:00

>> He has this concept of like the LLM's

## 15490:00 - 15520:00

reaching the dumb zone

## 15520:00 - 15545:00

>> where it's like after a certain amount

## 15545:00 - 15595:00

of tokens uh it just starts like

## 15595:00 - 15630:00

degrading in quality. And I actually

## 15630:00 - 15660:00

think that's very true especially if you

## 15660:00 - 15690:00

think about like how the reinforcement

## 15690:00 - 15720:00

learning might work. Like imagine you're

## 15720:00 - 15755:00

a college student. You're taking an

## 15755:00 - 15785:00

exam. In the first five minutes of that

## 15785:00 - 15805:00

exam, you're like, "Oh, I have all the

## 15805:00 - 15830:00

time in the world. Like, I'll do a great

## 15830:00 - 15850:00

job. I'll think through each of these

## 15850:00 - 15875:00

problems." Let's say you have like five

## 15875:00 - 15895:00

minutes left and you still have half the

## 15895:00 - 15930:00

exam left. You're like, "Oh man, I just

## 15930:00 - 15965:00

got to do whatever I can." Like, that's

## 15965:00 - 15995:00

the LM with a context window, right?

## 15995:00 - 16025:00

>> One of the tricks that uh I think

## 16025:00 - 16080:00

founders use is you put like a canary at

## 16080:00 - 16100:00

the beginning of the context. There's

## 16100:00 - 16140:00

something very esoteric that it's like

## 16140:00 - 16165:00

something really funny. It's like, I

## 16165:00 - 16215:00

don't know, my name is Calvin and blah

## 16215:00 - 16280:00

blah blah. I drank tea at 8 am. Some

## 16280:00 - 16315:00

random fact. And then as you keep going,

## 16315:00 - 16345:00

you ask it, do you remember what's my

## 16345:00 - 16380:00

name? Do you remember when I drank tea?

## 16380:00 - 16410:00

And then when it starts forgetting, that

## 16410:00 - 16435:00

I think is a bit of a sign that the

## 16435:00 - 16475:00

context has poison. That's like one

## 16475:00 - 16510:00

trick I've seen people do. They do a

## 16510:00 - 16530:00

random canery.

## 16530:00 - 16565:00

>> I have not tried this, but I fully

## 16565:00 - 16580:00

believe it. Yeah,

## 16580:00 - 16600:00

>> that's interesting. I haven't run across

## 16600:00 - 16640:00

any bugs before compaction, but maybe

## 16640:00 - 16665:00

I'm not paying attention. But you're

## 16665:00 - 16690:00

saying like that actually is actively

## 16690:00 - 16725:00

something that it just starts doing

## 16725:00 - 16755:00

weirder things that are not like

## 16755:00 - 16765:00

optimal.

## 16765:00 - 16775:00

>> Yeah. Yeah.

## 16775:00 - 16795:00

>> Okay. I got to be on the lookout for

## 16795:00 - 16805:00

that

## 16805:00 - 16835:00

>> solvable within cloud code itself. Like

## 16835:00 - 16870:00

it should be able to basically do some

## 16870:00 - 16920:00

sort of detection like what is saying

## 16920:00 - 16950:00

>> do your own internal heartbeat around it

## 16950:00 - 16965:00

around the context.

## 16965:00 - 16990:00

>> Yeah. And I think we're just not there

## 16990:00 - 17020:00

yet. Like I agree with you in the limit.

## 17020:00 - 17035:00

Uh

## 17035:00 - 17065:00

>> right now it's definitely hard to manage

## 17065:00 - 17100:00

context well. And I think kind of the

## 17100:00 - 17125:00

way it gets around it is like split up

## 17125:00 - 17150:00

context windows and then try and merge

## 17150:00 - 17175:00

everything. But you're sort of still at

## 17175:00 - 17205:00

the limit right now of like everything

## 17205:00 - 17245:00

that lives in context at the end of a

## 17245:00 - 17285:00

cloud code session is kind of fixed.

## 17285:00 - 17310:00

It's actually interesting. The codeex

## 17310:00 - 17345:00

approach is kind of the opposite and

## 17345:00 - 17370:00

they just wrote about this on the OpenAI

## 17370:00 - 17430:00

blog where it will run compaction like

## 17430:00 - 17470:00

periodically after each turn. And so

## 17470:00 - 17500:00

codecs can continue to run for a very

## 17500:00 - 17520:00

long time. And if you look at the

## 17520:00 - 17570:00

percentage in the uh the CLI, you'll see

## 17570:00 - 17605:00

it like move up and down as compaction

## 17605:00 - 17645:00

runs. I guess like there are these very

## 17645:00 - 17675:00

different architectures between cloud

## 17675:00 - 17715:00

code and codeex sound like they're

## 17715:00 - 17760:00

actually deeper in that codeex is

## 17760:00 - 17795:00

actually meant for much longer running

## 17795:00 - 17840:00

jobs. So you that's sort of like off the

## 17840:00 - 17885:00

bat a different use case and then the

## 17885:00 - 17910:00

architecture is very different as a

## 17910:00 - 17945:00

result. I guess right now it seems like

## 17945:00 - 17995:00

CLI's you know 2026 might be the year of

## 17995:00 - 18055:00

CLI but then this other idea that AGI is

## 18055:00 - 18090:00

here and it's actually ASI is around the

## 18090:00 - 18140:00

corner the coding agents right now are

## 18140:00 - 18165:00

really really smart but not smart enough

## 18165:00 - 18205:00

to run on their own for long periods of

## 18205:00 - 18265:00

time but a 10x increase in compute from

## 18265:00 - 18315:00

here are we there like are we at 24

## 18315:00 - 18365:00

hours or 48 hour running jobs on codecs

## 18365:00 - 18400:00

and that architecture is correct for

## 18400:00 - 18415:00

that world.

## 18415:00 - 18440:00

>> Yeah, I think it's a good question. It

## 18440:00 - 18460:00

sort of goes back to like kind of the

## 18460:00 - 18505:00

founding DNA of both companies. Like I

## 18505:00 - 18530:00

feel like Anthropic has always been very

## 18530:00 - 18565:00

big on like building tools for humans

## 18565:00 - 18585:00

where it comes to like, oh, here's the

## 18585:00 - 18630:00

style of the tone and like here's how it

## 18630:00 - 18655:00

should fit with all of the rest of your

## 18655:00 - 18685:00

work. And I think quad code is like a

## 18685:00 - 18720:00

very natural extension of that. In a lot

## 18720:00 - 18745:00

of ways, it like works like a human

## 18745:00 - 18770:00

would where it's like, oh, you need to

## 18770:00 - 18800:00

build like, I don't know, a doghouse or

## 18800:00 - 18820:00

something. It's like, oh, I'll go to the

## 18820:00 - 18845:00

hardware store and I'll build all these

## 18845:00 - 18875:00

materials and I'll like figure out how

## 18875:00 - 18905:00

they all fit together. Whereas OpenAI

## 18905:00 - 18950:00

really leans into this idea of just like

## 18950:00 - 19000:00

we are going to train the best model and

## 19000:00 - 19030:00

reinforce over time and get it to do

## 19030:00 - 19065:00

longer and longer horizon things uh in

## 19065:00 - 19090:00

this pursuit of artificial general

## 19090:00 - 19125:00

intelligence. And so it may not work

## 19125:00 - 19150:00

like a human at all. Like going back to

## 19150:00 - 19170:00

the doghouse example, it's like

## 19170:00 - 19185:00

>> but AlphaGo didn't either.

## 19185:00 - 19210:00

>> Yeah, but AlphaGo didn't either. It's

## 19210:00 - 19240:00

like, oh, it's like instead I will have

## 19240:00 - 19275:00

a 3D printer that can print from scratch

## 19275:00 - 19310:00

like a doghouse and it will be exactly

## 19310:00 - 19335:00

what you want and it will take a long

## 19335:00 - 19370:00

time and it will be like very custom and

## 19370:00 - 19410:00

it will do like weird things but it will

## 19410:00 - 19435:00

work you know and like maybe in the

## 19435:00 - 19465:00

limit that's the right call and so it's

## 19465:00 - 19480:00

going to be really interesting to see

## 19480:00 - 19515:00

how they play out. I mean net net it

## 19515:00 - 19545:00

seems like the latter is somewhat

## 19545:00 - 19605:00

inevitable but I like the former so much

## 19605:00 - 19640:00

you know like even this idea that it gs

## 19640:00 - 19665:00

was like I thought about you know 10

## 19665:00 - 19690:00

years ago I was like yeah I was in there

## 19690:00 - 19730:00

like writing my own really weird reaxes

## 19730:00 - 19760:00

to try to figure out where everything

## 19760:00 - 19785:00

was when I was refactoring or what

## 19785:00 - 19810:00

trying to understand code or whatever.

## 19810:00 - 19845:00

So that's the feeling I get when I'm

## 19845:00 - 19885:00

using it. It's like I can do five

## 19885:00 - 19925:00

people's worth of work in like a single

## 19925:00 - 19960:00

day. It's like rocket boosters. It's

## 19960:00 - 19970:00

unbelievable.

## 19970:00 - 20000:00

>> Yeah. I I think it's going to be really

## 20000:00 - 20025:00

interesting to see how this plays out

## 20025:00 - 20065:00

across large and small companies. I

## 20065:00 - 20090:00

think everyone who's experimenting with

## 20090:00 - 20120:00

this stuff on like a hobbyist level or

## 20120:00 - 20150:00

at like a very small startup, they're

## 20150:00 - 20175:00

just pushing the coding agents as far as

## 20175:00 - 20200:00

they can go because it's like you don't

## 20200:00 - 20220:00

really have time to figure out anything

## 20220:00 - 20245:00

else. Like as a startup, you have

## 20245:00 - 20265:00

limited runway. You're just going to

## 20265:00 - 20315:00

like orient around speed. I think at a

## 20315:00 - 20345:00

bigger company you have a lot more to

## 20345:00 - 20370:00

lose and you have all these other

## 20370:00 - 20400:00

internal processes around code review

## 20400:00 - 20425:00

and you probably already hired like a

## 20425:00 - 20455:00

big ENT team and I think it's going to

## 20455:00 - 20505:00

be very strange as like these individual

## 20505:00 - 20545:00

teams of like one person are like hey

## 20545:00 - 20570:00

that team over there isn't doing the

## 20570:00 - 20590:00

right thing like let me just build a

## 20590:00 - 20630:00

prototype that like works better. I

## 20630:00 - 20655:00

think at some point it's going to start

## 20655:00 - 20700:00

working better and I think that

## 20700:00 - 20745:00

landscape shift is going to be a very

## 20745:00 - 20775:00

interesting strange thing. my

## 20775:00 - 20810:00

10-year-old is uh you know he has

## 20810:00 - 20840:00

writing assignments every day and then

## 20840:00 - 20865:00

yesterday was the first day where he

## 20865:00 - 20910:00

used AI

## 20910:00 - 20945:00

and then I was like this is not a turn

## 20945:00 - 20980:00

of a phrase that a 10-year-old is

## 20980:00 - 21010:00

capable of doing

## 21010:00 - 21040:00

>> and then I think about that in this

## 21040:00 - 21070:00

context because we you know are working

## 21070:00 - 21115:00

with a lot of 18 to 22 year olds who you

## 21115:00 - 21145:00

know they've done internships but like

## 21145:00 - 21190:00

they haven't done like manager work like

## 21190:00 - 21230:00

you know we're saying um you know postp

## 21230:00 - 21265:00

productduct market fit uh once you're

## 21265:00 - 21305:00

have job cues of like millions of jobs

## 21305:00 - 21335:00

and like you know hundreds of thousands

## 21335:00 - 21380:00

of errors. That's like real management.

## 21380:00 - 21410:00

Like that's really you know it's

## 21410:00 - 21445:00

horribly unglamorous like combing

## 21445:00 - 21475:00

through hundreds of thousands of errors

## 21475:00 - 21515:00

and then like manually making sure that

## 21515:00 - 21550:00

like the thing works for all of your

## 21550:00 - 21585:00

users in the background. How does the

## 21585:00 - 21625:00

next generation understand that? Can the

## 21625:00 - 21665:00

cloud code bot actually teach people

## 21665:00 - 21705:00

about uh architecture and things like

## 21705:00 - 21745:00

that or you know are you just gonna bump

## 21745:00 - 21790:00

your head into it and users just kind of

## 21790:00 - 21825:00

suffer and you know people have to

## 21825:00 - 21835:00

figure it out

## 21835:00 - 21860:00

>> like at least where I find myself

## 21860:00 - 21885:00

spending the most time when it comes to

## 21885:00 - 21920:00

product is figuring out the kind of

## 21920:00 - 21965:00

product model in a sense like what are

## 21965:00 - 21995:00

the things that the user has to

## 21995:00 - 22025:00

understand today um and what are the

## 22025:00 - 22065:00

primitives that they can use to like do

## 22065:00 - 22085:00

whatever they want. I always think of

## 22085:00 - 22145:00

Slack like this. It's like Slack was in

## 22145:00 - 22170:00

some ways not really a new concept. It's

## 22170:00 - 22200:00

like there were many chats that existed

## 22200:00 - 22235:00

before it. Um, but the fact that they

## 22235:00 - 22265:00

had like channels, messages, and

## 22265:00 - 22300:00

reactions in a simple way that people

## 22300:00 - 22320:00

could just like think about and be like,

## 22320:00 - 22350:00

"Oh, I understand how to like navigate

## 22350:00 - 22375:00

this." It made a lot of sense for

## 22375:00 - 22405:00

people. But then kind of once they were

## 22405:00 - 22435:00

there, like it's very hard to change

## 22435:00 - 22470:00

that later on for a user, you know? It's

## 22470:00 - 22500:00

like, oh, maybe they wanted to go in

## 22500:00 - 22525:00

more of like a document first way or

## 22525:00 - 22550:00

like maybe right now they're trying to

## 22550:00 - 22575:00

incorporate agents. It's like difficult

## 22575:00 - 22605:00

to change the user's mental model. And

## 22605:00 - 22630:00

so I at least for myself building

## 22630:00 - 22650:00

products it's like you have to think

## 22650:00 - 22690:00

about that very carefully from an early

## 22690:00 - 22720:00

stage because again whatever you supply

## 22720:00 - 22745:00

to the coding agents as that kind of

## 22745:00 - 22770:00

kernel is going to be what they run with

## 22770:00 - 22825:00

and make more of forever more. YC's next

## 22825:00 - 22870:00

batch is now taking applications. Got a

## 22870:00 - 22900:00

startup in you? Apply at y

## 22900:00 - 22935:00

combinator.com/apply.

## 22935:00 - 22975:00

It's never too early and filling out the

## 22975:00 - 23020:00

app will level up your idea. Okay, back

## 23020:00 - 23035:00

to the video.

## 23035:00 - 23060:00

>> Do you have thoughts just cuz you know

## 23060:00 - 23105:00

the the agent so well? like what what

## 23105:00 - 23135:00

types of engineers are going to benefit

## 23135:00 - 23190:00

more than others um from these tools

## 23190:00 - 23210:00

becoming popular?

## 23210:00 - 23245:00

>> In general, I think that kind of the

## 23245:00 - 23285:00

more senior senior you are, the more you

## 23285:00 - 23300:00

benefit.

## 23300:00 - 23335:00

>> Um because

## 23335:00 - 23365:00

>> the agents are so good at taking some

## 23365:00 - 23420:00

sort of idea and then putting it into

## 23420:00 - 23450:00

action. If you're able to prompt that in

## 23450:00 - 23475:00

a few words, it's kind of like, oh, now

## 23475:00 - 23510:00

suddenly I had this like idea. I I find

## 23510:00 - 23535:00

this so often in open like scrolling

## 23535:00 - 23550:00

through the codebase. It's like, oh,

## 23550:00 - 23570:00

like here's a thing that I wish were

## 23570:00 - 23585:00

different. here's a thing that I wish

## 23585:00 - 23600:00

were different. Here's a thing that I

## 23600:00 - 23625:00

wish were different. Like just being

## 23625:00 - 23645:00

able to kick those off and then have

## 23645:00 - 23680:00

them come back I think is super

## 23680:00 - 23725:00

empowering and multiplies your impact. I

## 23725:00 - 23750:00

think also being able to detect like

## 23750:00 - 23795:00

which sorts of changes are good or bad

## 23795:00 - 23825:00

architecturally is very important or

## 23825:00 - 23860:00

like have a sense for where you might

## 23860:00 - 23890:00

want to flag something to an agent. I

## 23890:00 - 23925:00

think engineers who are more organized

## 23925:00 - 23975:00

like managerish uh and there's probably

## 23975:00 - 24005:00

just a missing product to be built here.

## 24005:00 - 24040:00

Uh maybe something like conductor uh

## 24040:00 - 24070:00

where it's like spread across all of

## 24070:00 - 24095:00

your sessions and kind of reminding you

## 24095:00 - 24125:00

like hey you were working on this thing

## 24125:00 - 24160:00

it's done it needs your input here. Oh

## 24160:00 - 24175:00

you should switch your attention over to

## 24175:00 - 24210:00

this other thing. I think that is

## 24210:00 - 24235:00

>> conductor should add that

## 24235:00 - 24275:00

>> yeah like uh context management for

## 24275:00 - 24305:00

agents but like we also need context

## 24305:00 - 24320:00

management for humans.

## 24320:00 - 24365:00

>> Yes 100%. Yeah. I mean I want like when

## 24365:00 - 24400:00

I wake up every day it kind of is like

## 24400:00 - 24425:00

hey here's all the work that got done

## 24425:00 - 24455:00

overnight. Like here are the like three

## 24455:00 - 24475:00

decisions that you need to make. here

## 24475:00 - 24505:00

are like areas of deep thinking that you

## 24505:00 - 24540:00

were planning to do like I want the turn

## 24540:00 - 24575:00

by turn for my day you know other things

## 24575:00 - 24605:00

that make it very useful like if you're

## 24605:00 - 24645:00

able to build um I don't know some sort

## 24645:00 - 24680:00

of like quick prototype for an idea to

## 24680:00 - 24725:00

show it off like that's an area I mean

## 24725:00 - 24750:00

obviously the agents do super well at

## 24750:00 - 24805:00

this um I would find myself at openai

## 24805:00 - 24835:00

often writing kind of like prototype

## 24835:00 - 24855:00

code or like hey I've got this like

## 24855:00 - 24880:00

in-memory key value store can you now

## 24880:00 - 24915:00

turn it into like uh work with a

## 24915:00 - 24935:00

production database or something like

## 24935:00 - 24970:00

that being able to concisely

## 24970:00 - 25005:00

specify ideas in code and I think having

## 25005:00 - 25060:00

a smell for what the right architecture

## 25060:00 - 25105:00

is is still the area where the models

## 25105:00 - 25130:00

like don't do the best job.

## 25130:00 - 25165:00

>> So if you were going back to your like

## 25165:00 - 25210:00

college days and studying CS again fresh

## 25210:00 - 25240:00

and you like were picking your own like

## 25240:00 - 25265:00

syllabus or curriculum like what would

## 25265:00 - 25300:00

you what would you study? Personally, I

## 25300:00 - 25355:00

think still understanding systems uh is

## 25355:00 - 25400:00

very important. Um and just having some

## 25400:00 - 25445:00

conception of like how like git works,

## 25445:00 - 25485:00

you know, or like HTTP or databases like

## 25485:00 - 25510:00

cues, like all of these different

## 25510:00 - 25555:00

systems. I think that those fundamentals

## 25555:00 - 25585:00

are still quite important. The other

## 25585:00 - 25625:00

thing that I'd probably do is just have

## 25625:00 - 25650:00

a semester where like each week you're

## 25650:00 - 25700:00

just building something and you really

## 25700:00 - 25730:00

try and push the models as far as they

## 25730:00 - 25760:00

can go. There's a sense that you have

## 25760:00 - 25785:00

whenever you're doing something that you

## 25785:00 - 25810:00

could always just like go up the layer

## 25810:00 - 25840:00

and ask the model to do it and like go

## 25840:00 - 25865:00

up a layer and ask the model to do it,

## 25865:00 - 25880:00

you know, where it's like, oh, I have

## 25880:00 - 25910:00

like a implement command where it like

## 25910:00 - 25935:00

implements the next phase of the plan,

## 25935:00 - 25955:00

but then I could have like an implement

## 25955:00 - 25985:00

all command and it like goes stage by

## 25985:00 - 26010:00

stage and creates a new sub agent and

## 26010:00 - 26040:00

then I could have like a check your work

## 26040:00 - 26075:00

kind of thing and like and I think

## 26075:00 - 26110:00

knowing where the models can and can't

## 26110:00 - 26140:00

accomplish that is such a moving target

## 26140:00 - 26175:00

that it's worthwhile just to like tinker

## 26175:00 - 26200:00

a lot. I mean, the other thing that's

## 26200:00 - 26265:00

really really crazy for I mean, I would

## 26265:00 - 26295:00

love to be able to teach 18 to 22 year

## 26295:00 - 26330:00

olds. Like, everyone around like at this

## 26330:00 - 26365:00

table has like ship stuff that people

## 26365:00 - 26405:00

really really want and love. So, it's

## 26405:00 - 26440:00

like how do we teach people that?

## 26440:00 - 26485:00

>> I wonder if like the best 18 to 22 year

## 26485:00 - 26510:00

olds like 5 years from now will just

## 26510:00 - 26540:00

have like off the charts taste and

## 26540:00 - 26570:00

everything because they'll just be so

## 26570:00 - 26595:00

much more prolific. They should be,

## 26595:00 - 26620:00

right? like they should just be

## 26620:00 - 26660:00

launching and like touching reality like

## 26660:00 - 26695:00

10 times as much as like the generation

## 26695:00 - 26710:00

before them.

## 26710:00 - 26735:00

>> The one thing I have wondered about on

## 26735:00 - 26770:00

that note, um I don't know if you all

## 26770:00 - 26795:00

found this, but growing up my mom used

## 26795:00 - 26825:00

to tell me like, oh, like stop

## 26825:00 - 26850:00

multitasking. You're not paying

## 26850:00 - 26905:00

attention to like what I'm doing. Uh

## 26905:00 - 26925:00

>> and I think there is some truth to that.

## 26925:00 - 26950:00

Like often I would be like off on my

## 26950:00 - 26975:00

computer like not paying attention. But

## 26975:00 - 27010:00

I do think I was legitimately better at

## 27010:00 - 27050:00

multitasking than our parents were. Uh,

## 27050:00 - 27080:00

and now I look at this new generation. I

## 27080:00 - 27095:00

think they're actually quite a bit

## 27095:00 - 27125:00

better at multitasking than we are, you

## 27125:00 - 27140:00

know, because they've kind of grown up

## 27140:00 - 27160:00

in this age of the internet and they're

## 27160:00 - 27185:00

dealing with like TikTok and all these

## 27185:00 - 27210:00

like different short form video and

## 27210:00 - 27230:00

things. Like it seems like there's room

## 27230:00 - 27260:00

for both kind of this like deep thinking

## 27260:00 - 27285:00

where you want to like notice what

## 27285:00 - 27320:00

you're seeing and understand and problem

## 27320:00 - 27345:00

solve, but then there's also this mode

## 27345:00 - 27375:00

of just like bounce between a bunch of

## 27375:00 - 27390:00

different things and you're context

## 27390:00 - 27415:00

switching constantly.

## 27415:00 - 27435:00

>> ADHD mode.

## 27435:00 - 27460:00

>> Yeah, the new generation is quite good

## 27460:00 - 27465:00

at this.

## 27465:00 - 27490:00

>> Yes, I definitely think there's a

## 27490:00 - 27515:00

there's a type of smart person. and

## 27515:00 - 27550:00

maybe it's ADHD, but just like always

## 27550:00 - 27580:00

has like a bunch of good projects on the

## 27580:00 - 27610:00

go, but just never actually finishes

## 27610:00 - 27635:00

anything. I might relate to this

## 27635:00 - 27665:00

personality a little bit. Um,

## 27665:00 - 27695:00

>> you release your uh your vibe code.

## 27695:00 - 27715:00

>> Yeah, but I wouldn't only because of

## 27715:00 - 27745:00

Claude code. That's kind of my like now

## 27745:00 - 27770:00

I just think like you kind of like

## 27770:00 - 27790:00

there's certain types of brains that

## 27790:00 - 27820:00

just have like like 10 branches going in

## 27820:00 - 27840:00

their head, but you never have enough

## 27840:00 - 27860:00

hours in the day to actually like see

## 27860:00 - 27880:00

any of them through. So, they're always

## 27880:00 - 27915:00

like half complete. And now it's just

## 27915:00 - 27945:00

like cold code gets you over the line

## 27945:00 - 27980:00

with everything. And it's just like, and

## 27980:00 - 28000:00

you made this point in your blog post

## 28000:00 - 28015:00

about how it feels like a video game,

## 28015:00 - 28035:00

but it's just like there's just a

## 28035:00 - 28065:00

constant novelty factor. Like you start

## 28065:00 - 28085:00

working on something and usually when

## 28085:00 - 28120:00

you hit the point of like I'm like bored

## 28120:00 - 28140:00

and I've got like this other better idea

## 28140:00 - 28170:00

and I should like start on that and then

## 28170:00 - 28200:00

come back to this. Like you can do that

## 28200:00 - 28220:00

now, but like everything can actually

## 28220:00 - 28235:00

get finished.

## 28235:00 - 28270:00

>> Let's live in the future for a moment.

## 28270:00 - 28315:00

It's 40 years from now. Software still

## 28315:00 - 28355:00

exists. Databases still exist. Access

## 28355:00 - 28400:00

control still exists. But like at the

## 28400:00 - 28440:00

core of it, I mean software is entirely

## 28440:00 - 28480:00

personal. access control and who gets to

## 28480:00 - 28515:00

do it is like you know sort of like this

## 28515:00 - 28540:00

manager mode thing that people still

## 28540:00 - 28580:00

have meetings about but then everything

## 28580:00 - 28625:00

else about a company its functions its

## 28625:00 - 28680:00

rules like is defined by people just

## 28680:00 - 28735:00

doing things in their own cloud code

## 28735:00 - 28765:00

like thing I don't know maybe it's a CLI

## 28765:00 - 28800:00

or it's like you know having giant

## 28800:00 - 28835:00

armies of workers then I don't know what

## 28835:00 - 28850:00

would that look like

## 28850:00 - 28885:00

>> like imagine if every time a company

## 28885:00 - 28920:00

signed up for segment you fork the

## 28920:00 - 28960:00

codebase you give them their own copy

## 28960:00 - 28985:00

of segment is running on their own

## 28985:00 - 29010:00

servers and then if they want to change

## 29010:00 - 29045:00

anything about it they just like tell

## 29045:00 - 29070:00

some chat window which is running like

## 29070:00 - 29105:00

an agent coding loop and just like edits

## 29105:00 - 29160:00

their version of segment as segment the

## 29160:00 - 29190:00

corporation pushes out more features

## 29190:00 - 29215:00

some agent figures out how to merge

## 29215:00 - 29255:00

>> yeah I I could totally see it I mean

## 29255:00 - 29285:00

sort of what I've been thinking I don't

## 29285:00 - 29310:00

know how far this future is but like

## 29310:00 - 29365:00

eventually every person who's working

## 29365:00 - 29390:00

like has their own sort of like cloud

## 29390:00 - 29420:00

computer and like set of cloud agents

## 29420:00 - 29445:00

who are running for them and and they're

## 29445:00 - 29470:00

mostly just like talking back and forth.

## 29470:00 - 29500:00

It's kind of like having like a super EA

## 29500:00 - 29525:00

or something where it's like, "Oh, here

## 29525:00 - 29540:00

are the things I need to pay attention

## 29540:00 - 29565:00

to. Like, let me make some quick

## 29565:00 - 29590:00

decisions. Like, let me spend more time

## 29590:00 - 29620:00

on this. Let me like meet with other

## 29620:00 - 29660:00

people." Cuz I think that there's still

## 29660:00 - 29690:00

going to be room for people who are like

## 29690:00 - 29715:00

want to meet other people and exchange

## 29715:00 - 29755:00

ideas in person. At least I get a lot of

## 29755:00 - 29770:00

fulfillment out of that. And then

## 29770:00 - 29785:00

separately, there's going to be this

## 29785:00 - 29820:00

army of agents who are like doing things

## 29820:00 - 29845:00

on your behalf and like automating a

## 29845:00 - 29885:00

bunch of things. Uh, I think the average

## 29885:00 - 29920:00

company is probably going to get like a

## 29920:00 - 29940:00

little smaller and there's going to be

## 29940:00 - 29975:00

many more of them doing more things.

## 29975:00 - 30000:00

>> Something I'm curious to see is kind of

## 30000:00 - 30030:00

like what the update version of the PG

## 30030:00 - 30070:00

maker uh maker schedule versus manager

## 30070:00 - 30105:00

schedule would look like cuz I feel like

## 30105:00 - 30130:00

part of what's going on at YC is sort of

## 30130:00 - 30155:00

a lot of our jobs are essentially

## 30155:00 - 30195:00

manager schedule which just really made

## 30195:00 - 30230:00

it hard to do any sort of building your

## 30230:00 - 30260:00

own software. But now you totally can

## 30260:00 - 30275:00

and that's why like a bunch of the

## 30275:00 - 30280:00

partners

## 30280:00 - 30315:00

>> just do it in the meeting like I like

## 30315:00 - 30355:00

right at the beginning of this podcast.

## 30355:00 - 30390:00

You let it run and then come back.

## 30390:00 - 30410:00

>> Well, like in the pockets, right? Like

## 30410:00 - 30430:00

in like it just used to be like

## 30430:00 - 30460:00

literally unless you had like, you know,

## 30460:00 - 30500:00

4 hours minimum block free to do

## 30500:00 - 30525:00

something, it just wasn't worth even

## 30525:00 - 30550:00

getting started, right? And I I think

## 30550:00 - 30585:00

that's actually goes very deep to how

## 30585:00 - 30610:00

we've changed programming. Like it used

## 30610:00 - 30635:00

to be that in order to write any code,

## 30635:00 - 30665:00

you had to fill your own context window

## 30665:00 - 30700:00

with so much data about all the

## 30700:00 - 30720:00

different class names and the functions

## 30720:00 - 30745:00

and the code that it touches. It would

## 30745:00 - 30770:00

take hours to build up that context

## 30770:00 - 30795:00

window. And so doing it in 10-minute

## 30795:00 - 30830:00

snatches was just like so frustrating. I

## 30830:00 - 30860:00

do think I think maybe one one primitive

## 30860:00 - 30905:00

for this future world will be I think

## 30905:00 - 30930:00

still the data models need to be still

## 30930:00 - 30985:00

be consistent and the system of record

## 30985:00 - 31005:00

>> there's there's opportunity for

## 31005:00 - 31040:00

something that's kind of agentic first

## 31040:00 - 31065:00

because right now we're still kind of in

## 31065:00 - 31090:00

integrated very much with databases and

## 31090:00 - 31130:00

SQL or NoSQL queries that are very low

## 31130:00 - 31160:00

level but imagine something that

## 31160:00 - 31185:00

generates all the data that you need for

## 31185:00 - 31205:00

all the different views for custom

## 31205:00 - 31265:00

software so a lot of the world would be

## 31265:00 - 31305:00

custom views but I think the unifi stuff

## 31305:00 - 31330:00

we still need to have data to be

## 31330:00 - 31340:00

correct.

## 31340:00 - 31370:00

>> I think data has a lot of gravity and I

## 31370:00 - 31400:00

I think you see this with companies who

## 31400:00 - 31455:00

are like offering access via API or MCP

## 31455:00 - 31505:00

like I think Slack uh locked down their

## 31505:00 - 31525:00

API a little bit because they didn't

## 31525:00 - 31555:00

want people just exfiltrating everything

## 31555:00 - 31580:00

from Slack and then building agentic

## 31580:00 - 31600:00

experiences on top of it.

## 31600:00 - 31645:00

>> I wonder with that note if you were to

## 31645:00 - 31700:00

rebuild segment in the current with the

## 31700:00 - 31720:00

current tools

## 31720:00 - 31765:00

>> how would it look like? I mean, segment

## 31765:00 - 31805:00

is a funny business in that uh where we

## 31805:00 - 31830:00

started was building these integrations,

## 31830:00 - 31860:00

right? Um and so it's like, oh, you need

## 31860:00 - 31900:00

to wire up like the same data going to

## 31900:00 - 31940:00

like mix panel and kissmetrics and

## 31940:00 - 31970:00

Google Analytics, etc. And I think just

## 31970:00 - 32010:00

writing that code now like that used to

## 32010:00 - 32045:00

be maybe a more annoying or harder thing

## 32045:00 - 32075:00

to do and so it was worth paying for.

## 32075:00 - 32105:00

Now it like that value has dropped to

## 32105:00 - 32120:00

zero.

## 32120:00 - 32145:00

>> Yeah. And actually like in many cases

## 32145:00 - 32170:00

you're better off like saying, "Oh, I

## 32170:00 - 32195:00

actually want to map it this way and I

## 32195:00 - 32225:00

want this specific behavior." like I

## 32225:00 - 32270:00

will just tell the quad or codeex what

## 32270:00 - 32305:00

to do and then it will do it and I'll

## 32305:00 - 32330:00

have exactly the behavior that I want.

## 32330:00 - 32360:00

So I think that aspect of segment like

## 32360:00 - 32395:00

the value has dropped precipitously. I

## 32395:00 - 32425:00

think the aspect of like keeping this

## 32425:00 - 32460:00

data pipeline running and like

## 32460:00 - 32485:00

continuing to automate a bunch of parts

## 32485:00 - 32520:00

of your business or like schedule these

## 32520:00 - 32545:00

like email deliveries which should go

## 32545:00 - 32570:00

out through customer IO every time a

## 32570:00 - 32605:00

customer signs up or like manage

## 32605:00 - 32635:00

audiences for you like that value is

## 32635:00 - 32665:00

kind of still there and I think you

## 32665:00 - 32685:00

could do a lot more interesting things

## 32685:00 - 32715:00

where it's like hey if I have all this

## 32715:00 - 32740:00

data and like a full view of the

## 32740:00 - 32780:00

customer like how should I be emailing

## 32780:00 - 32805:00

them? Should I change like parts of the

## 32805:00 - 32830:00

product when they log in? Should I be

## 32830:00 - 32850:00

giving them different onboardings

## 32850:00 - 32880:00

depending on who they are? like there's

## 32880:00 - 32905:00

a lot more interesting stuff that you

## 32905:00 - 32945:00

could do by basically running like I

## 32945:00 - 32995:00

don't know small LM agents over them and

## 32995:00 - 33020:00

changing that. That would be the changes

## 33020:00 - 33035:00

I would make.

## 33035:00 - 33065:00

>> So it's kind of like moving up the stack

## 33065:00 - 33095:00

to your comment earlier and all the way

## 33095:00 - 33130:00

turtles down the low-level stuff is gone

## 33130:00 - 33165:00

is now really more doing things at the

## 33165:00 - 33185:00

campaign level which is way more

## 33185:00 - 33195:00

abstract.

## 33195:00 - 33235:00

>> Yes. I mean I'm amazed at to what degree

## 33235:00 - 33270:00

like claude code even just from like the

## 33270:00 - 33310:00

context of what I'm working on figures

## 33310:00 - 33345:00

out like what my motivations are.

## 33345:00 - 33385:00

>> Yeah. I I I'm still blown away by coding

## 33385:00 - 33415:00

agents because effectively what you're

## 33415:00 - 33445:00

doing is you're like giving them a copy

## 33445:00 - 33475:00

of a repo and then you're slipping a

## 33475:00 - 33500:00

little note under the door and being

## 33500:00 - 33535:00

like, "Hey, go implement this thing."

## 33535:00 - 33565:00

They have like no knowledge of like what

## 33565:00 - 33590:00

your company is or like what you do, who

## 33590:00 - 33620:00

your customers are in most cases. Maybe

## 33620:00 - 33640:00

it's in the training set because they

## 33640:00 - 33685:00

know you're Gary. But it blows my mind

## 33685:00 - 33710:00

that it works at all. And and that's

## 33710:00 - 33730:00

where I think the context is really

## 33730:00 - 33750:00

important, right? Because if it latches

## 33750:00 - 33785:00

on to something that isn't quite right,

## 33785:00 - 33810:00

it doesn't have a lot to go on. And if

## 33810:00 - 33830:00

it misses something that's essential,

## 33830:00 - 33860:00

it's going to just reimplement it.

## 33860:00 - 33880:00

>> What do you think the constraints are

## 33880:00 - 33925:00

right now? I mean, like context window

## 33925:00 - 33960:00

is still a constraint, but it's like so

## 33960:00 - 34000:00

big that, you know, it's like we can do

## 34000:00 - 34045:00

some stuff like we can't do the mega

## 34045:00 - 34085:00

rearchitectures, but we can do a lot.

## 34085:00 - 34135:00

And then if the opus 4.5 somehow got a

## 34135:00 - 34190:00

lot smarter, uh, and then that unlocked

## 34190:00 - 34225:00

a big thing, which was interesting. I

## 34225:00 - 34245:00

don't have no idea if that was like

## 34245:00 - 34285:00

pre-training or post-training. like what

## 34285:00 - 34330:00

are there other like levers that you

## 34330:00 - 34380:00

think of other than you know basic model

## 34380:00 - 34410:00

intelligence like frontier model

## 34410:00 - 34450:00

intelligence and context window I mean I

## 34450:00 - 34470:00

still think context window is like

## 34470:00 - 34510:00

probably the number one limit like if

## 34510:00 - 34545:00

you look at cloud code executing it's

## 34545:00 - 34565:00

delegating to all these different

## 34565:00 - 34600:00

context windows at the end of the day

## 34600:00 - 34625:00

when each one comes back it's like

## 34625:00 - 34650:00

getting some sort of summary so it's

## 34650:00 - 34680:00

also not getting the full picture like

## 34680:00 - 34695:00

if you have a problem that's just like

## 34695:00 - 34730:00

too big to fit in a single one like kind

## 34730:00 - 34755:00

of no amount of compaction is going to

## 34755:00 - 34785:00

help I would point to that as like both

## 34785:00 - 34815:00

Anthropic has figured something quite

## 34815:00 - 34840:00

useful out with delegating to these

## 34840:00 - 34870:00

subcontext windows, but also I think

## 34870:00 - 34890:00

it's still a block barrier.

## 34890:00 - 34925:00

>> So we'd do better if we had a million

## 34925:00 - 34965:00

million token context every single time.

## 34965:00 - 35000:00

>> Yeah, I think so. And like figure it out

## 35000:00 - 35030:00

a better way to especially train these

## 35030:00 - 35060:00

like very long context trajectories

## 35060:00 - 35075:00

because if you think about it like

## 35075:00 - 35100:00

there's there's a lot of training data

## 35100:00 - 35125:00

on the internet for like what is the

## 35125:00 - 35150:00

next sentence that comes or like what's

## 35150:00 - 35180:00

the next paragraph that comes. If you

## 35180:00 - 35235:00

have 80,000 tokens that are generated

## 35235:00 - 35280:00

like understanding what the next thing

## 35280:00 - 35325:00

to do based upon like oh I should refer

## 35325:00 - 35365:00

to the 20,000 token like that's

## 35365:00 - 35405:00

trickier. I think this like integration

## 35405:00 - 35435:00

and orchestration is starting to become

## 35435:00 - 35465:00

the limiting factor. I mean I think

## 35465:00 - 35495:00

there are like stuff on code review

## 35495:00 - 35515:00

related to this. It's like oh if we're

## 35515:00 - 35545:00

like merging all this code like who's

## 35545:00 - 35570:00

watching it? Does a human still have to

## 35570:00 - 35600:00

watch it? Like how do we verify the

## 35600:00 - 35640:00

changes? And then I think like pulling

## 35640:00 - 35675:00

in the context correctly from your tools

## 35675:00 - 35705:00

like you were talking about Sentry like

## 35705:00 - 35735:00

you want Sentry to auto be able to like

## 35735:00 - 35770:00

figure out a PR you know and then like

## 35770:00 - 35795:00

maybe it pushes it to a subset of your

## 35795:00 - 35820:00

traffic and if it looks good then it

## 35820:00 - 35845:00

rolls out everywhere you know like all

## 35845:00 - 35865:00

of that automation still has to be

## 35865:00 - 35885:00

built. I was surprised how important

## 35885:00 - 35925:00

testing was. Like I was operating for

## 35925:00 - 35970:00

like the first 2 or 3 days of my 9 days

## 35970:00 - 36015:00

in the wilderness. Like uh no tests or

## 36015:00 - 36055:00

very few tests. And then one day I was

## 36055:00 - 36080:00

like, "All right, today's refactor day.

## 36080:00 - 36110:00

I'm going to do get to 100% test

## 36110:00 - 36150:00

coverage." And then I just sped up like

## 36150:00 - 36185:00

crazy. It was just like, "Oh, it did it.

## 36185:00 - 36225:00

It works." I rarely even have to

## 36225:00 - 36265:00

necessarily manually test because it's

## 36265:00 - 36295:00

like the test coverage is so good and

## 36295:00 - 36315:00

like nothing breaks

## 36315:00 - 36355:00

>> which is very similar to what all the

## 36355:00 - 36385:00

companies are doing just for prompt

## 36385:00 - 36425:00

engineering outside of coding is very

## 36425:00 - 36450:00

much test-driven development. I think we

## 36450:00 - 36480:00

had this episode with Jake Heler and

## 36480:00 - 36510:00

that was a big paradigm shift is like

## 36510:00 - 36545:00

the way you get a good prompt is all

## 36545:00 - 36580:00

test driven just like evals right in a

## 36580:00 - 36610:00

sense the test cases are your evals.

## 36610:00 - 36645:00

There are some broken flows now. I think

## 36645:00 - 36695:00

that you we might need a clawed code

## 36695:00 - 36745:00

that could like talk to a stack overflow

## 36745:00 - 36770:00

that was like a clawed code stack

## 36770:00 - 36795:00

overflow.

## 36795:00 - 36830:00

>> Like I had this problem. It was so crazy

## 36830:00 - 36875:00

like I uh instead of using in the in

## 36875:00 - 36940:00

like the priority of a job Q I used or

## 36940:00 - 36970:00

actually I didn't even write again I did

## 36970:00 - 37015:00

not write this. The machine wrote a

## 37015:00 - 37055:00

string with a comma thinking that it

## 37055:00 - 37085:00

would take that syntax, but it was

## 37085:00 - 37125:00

expecting like an array in JSON and then

## 37125:00 - 37165:00

it just like no jobs would run. And then

## 37165:00 - 37215:00

I watched it for like 30 minutes walk

## 37215:00 - 37270:00

through the internals of Rails job like

## 37270:00 - 37310:00

the active job like couple thousand

## 37310:00 - 37350:00

lines of code like trying to debug what

## 37350:00 - 37390:00

was happening and it found the bug

## 37390:00 - 37430:00

actually. I was like that's amazing. I

## 37430:00 - 37455:00

just think about what I would do like 10

## 37455:00 - 37480:00

years ago and I would have been like hey

## 37480:00 - 37520:00

why are the you know jobs not working

## 37520:00 - 37550:00

and then I would find a Stack Overflow

## 37550:00 - 37590:00

or blog a Rails blog post and it's like

## 37590:00 - 37625:00

oh yeah like nobody fixed that stupid

## 37625:00 - 37650:00

bug where you know you think that you

## 37650:00 - 37685:00

can put a you know comma delimited

## 37685:00 - 37710:00

string in there but actually you have to

## 37710:00 - 37725:00

make sure it's an array.

## 37725:00 - 37735:00

>> Uhhuh.

## 37735:00 - 37770:00

>> I was like oh my god like that was very

## 37770:00 - 37800:00

funny actually. I think that's like one

## 37800:00 - 37820:00

of the hardest parts about thinking

## 37820:00 - 37850:00

about what's going to happen here

## 37850:00 - 37890:00

because uh there's like things that you

## 37890:00 - 37940:00

would do as a human in a CLI right now

## 37940:00 - 37980:00

and like that's very obvious but even

## 37980:00 - 38020:00

that idea of like should the agents have

## 38020:00 - 38060:00

their own stack overflow like if you

## 38060:00 - 38100:00

just increase the intelligence by you

## 38100:00 - 38120:00

know I don't know what you even call it

## 38120:00 - 38165:00

like by 10 IQ points like 10 virtual IQ

## 38165:00 - 38185:00

points

## 38185:00 - 38210:00

>> like would it even do that? It would

## 38210:00 - 38240:00

just be like oh yeah that's a string

## 38240:00 - 38250:00

whatever.

## 38250:00 - 38270:00

>> Yeah. Yeah. I think there's something

## 38270:00 - 38305:00

very interesting here around like agent

## 38305:00 - 38350:00

memory. Um, and cloud code has sort of

## 38350:00 - 38385:00

set itself up and I think Codeex 2 by

## 38385:00 - 38410:00

storing all your conversation history

## 38410:00 - 38450:00

just as files. So you could imagine you

## 38450:00 - 38480:00

like give it access to a tool that then

## 38480:00 - 38510:00

can read previous conversation history.

## 38510:00 - 38540:00

I think there's a missing piece around a

## 38540:00 - 38565:00

lot of collaboration there. Like it'd be

## 38565:00 - 38595:00

amazing if like there was some way of

## 38595:00 - 38625:00

smartly sharing your co-workers prompts

## 38625:00 - 38655:00

and you could see and be like, "Oh, like

## 38655:00 - 38685:00

I hit this thing, but actually like

## 38685:00 - 38720:00

Brian over there like fixed it earlier,

## 38720:00 - 38745:00

you know, so like the two of us can

## 38745:00 - 38770:00

share knowledge." I I think there's

## 38770:00 - 38800:00

something there's something onto this of

## 38800:00 - 38830:00

like a model generated like wiki, you

## 38830:00 - 38855:00

know, or like Graopedia stuff.

## 38855:00 - 38880:00

>> Now I can't stop thinking about Have you

## 38880:00 - 38925:00

seen um the Claudebot social like the

## 38925:00 - 38950:00

network for clawbots to talk to each

## 38950:00 - 39000:00

other and it's like that's the evolution

## 39000:00 - 39015:00

for Molen?

## 39015:00 - 39030:00

>> Yeah. I guess what they don't know.

## 39030:00 - 39080:00

Clawbot's essentially like um uh like

## 39080:00 - 39115:00

your own personal AI agent that you can

## 39115:00 - 39140:00

run on your own machine. You can

## 39140:00 - 39180:00

download it. Um do not give it access to

## 39180:00 - 39215:00

emails would be my number one piece of

## 39215:00 - 39255:00

advice or probably anything. Um because

## 39255:00 - 39285:00

it's not clear how safe it is and it's

## 39285:00 - 39305:00

probably almost certainly going to

## 39305:00 - 39325:00

probably a lot of people being prompt

## 39325:00 - 39355:00

injected by it right now. But somebody

## 39355:00 - 39390:00

created um like a I haven't actually

## 39390:00 - 39420:00

seen it but I've like seen it on Twitter

## 39420:00 - 39450:00

but like a site where like everyone can

## 39450:00 - 39475:00

sort of spin up their own like clawbot

## 39475:00 - 39500:00

like personal agent and then the agents

## 39500:00 - 39530:00

can talk to each other and now there's

## 39530:00 - 39555:00

just like all this AI generated content

## 39555:00 - 39590:00

of these like personal AI agents talking

## 39590:00 - 39600:00

to each other.

## 39600:00 - 39635:00

>> Yeah. I mean it looks like Reddit but if

## 39635:00 - 39690:00

Reddit were run by agents. I mean it's

## 39690:00 - 39720:00

interesting to see like Codeex's

## 39720:00 - 39745:00

personality shine through when writing

## 39745:00 - 39805:00

code. I would say uh it does most stuff

## 39805:00 - 39845:00

that humans don't do. kind of this alpha

## 39845:00 - 39865:00

go sense where it's like oh it'll write

## 39865:00 - 39905:00

a Python script to like modify some part

## 39905:00 - 39955:00

of the file system. I think that is like

## 39955:00 - 39980:00

very interesting and kind of alien

## 39980:00 - 40030:00

behavior which has been learned. Yeah.

## 40030:00 - 40055:00

>> Um but it does give these like

## 40055:00 - 40100:00

superhuman results for me at least when

## 40100:00 - 40135:00

debugging complex issues that I find

## 40135:00 - 40160:00

opus often misses.

## 40160:00 - 40185:00

>> What's an example of a complex issue

## 40185:00 - 40215:00

that you could talk about? I mean it's

## 40215:00 - 40245:00

like concurrency or naming issues,

## 40245:00 - 40265:00

right?

## 40265:00 - 40285:00

>> I find the models are actually like

## 40285:00 - 40315:00

decent at concurrency. oftentimes

## 40315:00 - 40345:00

there's stuff where it's like, oh,

## 40345:00 - 40365:00

there's a request that is like

## 40365:00 - 40410:00

traversing several different services. I

## 40410:00 - 40450:00

mean, kind of to your point about the uh

## 40450:00 - 40485:00

serialization and deserialization of

## 40485:00 - 40505:00

like stuff with commas in it.

## 40505:00 - 40545:00

>> Um, it's like, oh, it needs to track

## 40545:00 - 40570:00

some sort of complex behavior around

## 40570:00 - 40625:00

those or like way of uh I don't know

## 40625:00 - 40660:00

refreshing complex UI state and Opus

## 40660:00 - 40690:00

often will miss it if there is many

## 40690:00 - 40725:00

files, but codeex seems to catch it.

## 40725:00 - 40735:00

>> Interesting.

## 40735:00 - 40745:00

>> Yeah.

## 40745:00 - 40775:00

>> Yeah. Prognostication about how will

## 40775:00 - 40805:00

tools continue to evolve. It's very

## 40805:00 - 40835:00

interesting like I feel like sort of a

## 40835:00 - 40890:00

new citizen in this land in a way like I

## 40890:00 - 40920:00

just you know knew it was happening. I

## 40920:00 - 40950:00

you know manager schedule finally a

## 40950:00 - 40980:00

project appeared and was like oh I'm

## 40980:00 - 41005:00

going to go all in on this

## 41005:00 - 41055:00

>> and then now I'm like in it's like uh

## 41055:00 - 41095:00

>> I'm in a stranger in a strange land but

## 41095:00 - 41130:00

it but it like resembles exactly what I

## 41130:00 - 41135:00

remember.

## 41135:00 - 41175:00

>> I think we all we all feel that way like

## 41175:00 - 41200:00

I think I think the most important thing

## 41200:00 - 41225:00

is just to keep tinkering because it all

## 41225:00 - 41270:00

changes every few months. I do feel like

## 41270:00 - 41295:00

the best or the people who will get the

## 41295:00 - 41320:00

most out of coding agents in the future

## 41320:00 - 41345:00

are going to be kind of like more

## 41345:00 - 41375:00

manager-like where they're focusing on

## 41375:00 - 41420:00

directing flows in certain ways. They're

## 41420:00 - 41445:00

probably going to be a little bit more

## 41445:00 - 41500:00

like designer artist in some ways where

## 41500:00 - 41525:00

it's like they're figuring out what

## 41525:00 - 41550:00

specifically goes in the product and

## 41550:00 - 41585:00

what stuff you can do without. And I

## 41585:00 - 41625:00

think they'll be very good at just like

## 41625:00 - 41660:00

continuing to think about automation and

## 41660:00 - 41690:00

where they're missing context. I guess

## 41690:00 - 41720:00

what's funny is I tried to use codeex

## 41720:00 - 41760:00

just now uh for my Rails project but the

## 41760:00 - 41795:00

thing is like it's kind of obvious that

## 41795:00 - 41840:00

nobody at OpenAI cares about Rails which

## 41840:00 - 41870:00

is fine like it's a very it's a

## 41870:00 - 41910:00

vestigial language it's very strange it

## 41910:00 - 41940:00

just happened to be the one that I you

## 41940:00 - 41970:00

know really really went deep on 10 years

## 41970:00 - 41985:00

ago

## 41985:00 - 42015:00

>> and then uh it's just funny how much of

## 42015:00 - 42065:00

it is exactly again anyone can make

## 42065:00 - 42090:00

something but then the something people

## 42090:00 - 42150:00

want is very hard and um even when you

## 42150:00 - 42190:00

have like unlimited resources is at like

## 42190:00 - 42225:00

an openi. It's like I guess if someone

## 42225:00 - 42260:00

from codeex is watching right now, my

## 42260:00 - 42300:00

request would be go down the list of all

## 42300:00 - 42335:00

of the run times and just add like

## 42335:00 - 42365:00

syntactic sugar. There's like this is

## 42365:00 - 42425:00

probably like you know 10 PRs at most

## 42425:00 - 42470:00

for like I don't know the top like 15

## 42470:00 - 42505:00

run times. I guess it's like sort of the

## 42505:00 - 42550:00

reminder that like man actually like

## 42550:00 - 42605:00

there are far fewer excuses for software

## 42605:00 - 42650:00

that doesn't quite work for a user you

## 42650:00 - 42700:00

know now than ever actually. Yeah, I do

## 42700:00 - 42725:00

think it this is an interesting point in

## 42725:00 - 42765:00

terms of mix of training data. Codex

## 42765:00 - 42850:00

works very well on Python monor repos

## 42850:00 - 42870:00

shape of openi.

## 42870:00 - 42895:00

>> Yeah. Yeah. And it's like I remember

## 42895:00 - 42925:00

working like internally open I was like

## 42925:00 - 42955:00

oh my gosh this tool is amazing. It is

## 42955:00 - 42995:00

incredible. Um and it kind of makes

## 42995:00 - 43035:00

sense in terms of the data mix and the

## 43035:00 - 43060:00

researchers who are working on it. I

## 43060:00 - 43085:00

think Enthropic is focused a little bit

## 43085:00 - 43105:00

more on like some of the front-end

## 43105:00 - 43155:00

things. Um, and I don't know in terms of

## 43155:00 - 43190:00

like a Ruby for example, like who has

## 43190:00 - 43215:00

the best model there and who's

## 43215:00 - 43240:00

incorporated the data mix.

## 43240:00 - 43245:00

>> Yeah.

## 43245:00 - 43265:00

>> Like some of the labs tend to take this

## 43265:00 - 43305:00

perspective of just more data is better.

## 43305:00 - 43350:00

Uh, and so they'll just flood as much

## 43350:00 - 43380:00

data as possible while others I think

## 43380:00 - 43410:00

are a little bit more tuned in terms of

## 43410:00 - 43445:00

the mix. And I think depending on which

## 43445:00 - 43465:00

approach you take there, it can give

## 43465:00 - 43490:00

very different results where it's like,

## 43490:00 - 43535:00

oh, I'm taking just the like top 10% of

## 43535:00 - 43555:00

JavaScript is pretty different than if

## 43555:00 - 43590:00

you're looking across everything. I

## 43590:00 - 43620:00

actually think OpenAI and the you know

## 43620:00 - 43655:00

OpenAI models are really good at Ruby

## 43655:00 - 43685:00

from what I can tell and then

## 43685:00 - 43715:00

>> it's it's the harness around the model.

## 43715:00 - 43735:00

It is Yeah.

## 43735:00 - 43755:00

>> Oh, interesting. Okay.

## 43755:00 - 43785:00

>> It's literally like Rails has this weird

## 43785:00 - 43820:00

thing where you have to have, you know,

## 43820:00 - 43855:00

access Postgress in a certain way or

## 43855:00 - 43890:00

like it couldn't fit. Yeah. The

## 43890:00 - 43910:00

sandboxing.

## 43910:00 - 43945:00

>> Yeah, the sandboxing. It's such an

## 43945:00 - 43980:00

interesting question because uh I think

## 43980:00 - 44010:00

OpenAI actually takes the like

## 44010:00 - 44045:00

sandboxing and security question more

## 44045:00 - 44080:00

seriously than almost anyone else. I

## 44080:00 - 44100:00

remember when we were building codeex

## 44100:00 - 44125:00

like basically one of the gates that you

## 44125:00 - 44140:00

have to pass through in order to release

## 44140:00 - 44175:00

a model is you have to like talk about

## 44175:00 - 44200:00

safety and security risks like every

## 44200:00 - 44220:00

time you want to release. One of the

## 44220:00 - 44240:00

things we were looking into was prompt

## 44240:00 - 44265:00

injection especially for opening up to

## 44265:00 - 44280:00

the internet because a bunch of users

## 44280:00 - 44305:00

were like oh this has to like work on

## 44305:00 - 44325:00

the internet. We're like, "Oh, we don't

## 44325:00 - 44350:00

know." Like, "It seems pretty easy to

## 44350:00 - 44395:00

prompt." >> Operator was also Yeah. that. Yeah.

## 44395:00 - 44445:00

>> And so, uh, the PM on our team, Alex,

## 44445:00 - 44485:00

uh, basically like put together a GitHub

## 44485:00 - 44515:00

issue and it had like a very obvious

## 44515:00 - 44540:00

prompt injection, which was like, "Oh,

## 44540:00 - 44565:00

reveal this thing." And then he told the

## 44565:00 - 44595:00

model like, "Hey, go fix this issue."

## 44595:00 - 44615:00

Uh, and he's like, "Oh, there's no way

## 44615:00 - 44640:00

this is going to work." And like

## 44640:00 - 44665:00

immediately the prompt injection works,

## 44665:00 - 44710:00

you know? And so I think OpenAI like

## 44710:00 - 44750:00

sort of correctly is very worried about

## 44750:00 - 44770:00

this and is like, "Hey, we're going to

## 44770:00 - 44790:00

run everything in on a sandbox. We're

## 44790:00 - 44810:00

going to make sure it like doesn't touch

## 44810:00 - 44830:00

all these sensitive files in your

## 44830:00 - 44845:00

machine. We're going to be very careful

## 44845:00 - 44885:00

about secrets. And I think if you're a

## 44885:00 - 44910:00

startup where you're just like running

## 44910:00 - 44940:00

fast, you probably don't care. You're

## 44940:00 - 44970:00

just like, I just want it to work. Y,

## 44970:00 - 44975:00

you know,

## 44975:00 - 45005:00

>> are you a dangerously skip permissions

## 45005:00 - 45025:00

person?

## 45025:00 - 45065:00

>> Uh, I actually am not. I like have a set

## 45065:00 - 45080:00

of things that are

## 45080:00 - 45100:00

>> How about you? Are you running?

## 45100:00 - 45145:00

>> Not I like to read, you know. I like to

## 45145:00 - 45160:00

read what it's doing.

## 45160:00 - 45185:00

>> Are you skip permissions, Jerry?

## 45185:00 - 45210:00

>> 100%.

## 45210:00 - 45230:00

>> YOLO.

## 45230:00 - 45265:00

>> Oh my god. It's about 50/50 on the YC

## 45265:00 - 45295:00

engineering team.

## 45295:00 - 45320:00

>> It's about 5050.

## 45320:00 - 45350:00

>> A security engineer would watch this

## 45350:00 - 45380:00

part and say, "You can't release this

## 45380:00 - 45410:00

part of the video. Just cut it from the

## 45410:00 - 45440:00

podcast. You can't have this out here."

## 45440:00 - 45465:00

>> I think it's context dependent. Like if

## 45465:00 - 45490:00

you're at an enterprise, you don't want

## 45490:00 - 45515:00

to do that. If you're a startup and have

## 45515:00 - 45550:00

nothing to lose, you probably do.

## 45550:00 - 45575:00

>> YC has progressed a little bit from a

## 45575:00 - 45600:00

startup. We still act like one though,

## 45600:00 - 45640:00

which is, I think, important. Cool. I

## 45640:00 - 45665:00

mean, this is so awesome. Kelvin, thank

## 45665:00 - 45690:00

you so much for joining us.

## 45690:00 - 45710:00

>> Of course. Thanks for having me.

## 45710:00 - 45745:00

>> Oh my god. There's Yeah. So fun. All

## 45745:00+

right, back to Claude.

