---
source: https://www.youtube.com/watch?v=lATVlT5F-P0
title: Is Generative AI a Cybersecurity Disaster Waiting to Happen? — With Yinon
  Costica
author: Alex Kantrowitz
date: 2025-09-23
views: 3068
description: >-
  Yinon Costica is the co-founder and VP of product at Wiz, which sold to Google
  for $32 billion in cash. Costica joins Big Technology Podcast to discuss the
  extent of the cybersecurity threats that generative AI is creating, from
  vulnerabilities in AI software to the risks involved in “vibe coding.” Tune in
  to hear how attackers are using AI, why defenders face new asymmetries, and
  what guardrails organizations need now. We also cover Google’s $32 billion
  acquisition of Wiz, the DeepSeek controversy, post-quantum cryptography, and
  the future risks of autonomous vehicles and humanoid robots. Hit play for a
  sharp, accessible look at the cutting edge of AI and cybersecurity.


  ---

  Enjoying Big Technology Podcast? Please rate us five stars ⭐⭐⭐⭐⭐ in your
  podcast app of choice.

  Want a discount for Big Technology on Substack + Discord? Here’s 25% off for
  the first year: https://www.bigtechnology.com/subscribe?coupon=0843016b

  Questions? Feedback? Write to: bigtechnologypodcast@gmail.com


  00:00 Opening and guest intro

  01:05 AI as a new software stack

  04:25 Core AI tools with RCE flaws

  06:18 Cloud infrastructure risks

  09:20 How secure is AI-written code

  13:54 Agents and security reviewers

  17:38 How attackers use AI today

  22:09 Asymmetry: attackers vs. defenders

  32:36 What Wiz actually does

  40:11 DeepSeek case and media spin
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:49:31.046Z
---

# Is Generative AI a Cybersecurity Disaster Waiting to Happen? — With Yinon Costica

## 00:00 - 35:00

What type of novel security threats are

## 35:00 - 95:00

emerging as AI advances? Let's find out

## 95:00 - 145:00

with Whiz co-founder Enone Costikica who

## 145:00 - 180:00

is here in studio to speak with us about

## 180:00 - 205:00

what's happening. Enone, great to see

## 205:00 - 220:00

you. Welcome to the show.

## 220:00 - 240:00

>> Thank you, Alex.

## 240:00 - 285:00

>> All right, so AI is it's doing amazing

## 285:00 - 320:00

things. It is producing lines and lines

## 320:00 - 360:00

of code for engineers and helping people

## 360:00 - 400:00

build things faster than they ever could

## 400:00 - 440:00

before. The other side of it is it's

## 440:00 - 495:00

helping I imagine bad guys produce lines

## 495:00 - 540:00

and lines of code and attack faster than

## 540:00 - 590:00

they ever could before. Now you are the

## 590:00 - 635:00

co-founder of Whiz which is in the

## 635:00 - 665:00

middle of a sales process or selling to

## 665:00 - 700:00

Google for 32 billion.

## 700:00 - 710:00

>> Correct.

## 710:00 - 740:00

>> Okay. So you're the perfect person to

## 740:00 - 785:00

have to discuss this because Whiz is a

## 785:00 - 825:00

cyber security company. we've never had

## 825:00 - 870:00

a cyber security expert like you on to

## 870:00 - 915:00

talk about how what's happening um

## 915:00 - 955:00

especially as generative AI rises. So

## 955:00 - 980:00

just give us a little bit of a state of

## 980:00 - 1020:00

play here in terms of um what this

## 1020:00 - 1060:00

explosion of the ability to code has

## 1060:00 - 1090:00

done to cyber security.

## 1090:00 - 1120:00

>> Yeah, it's interesting. I think the

## 1120:00 - 1155:00

ability to code is just one aspect of

## 1155:00 - 1195:00

AI. When we think about AI as a whole,

## 1195:00 - 1240:00

first I'm thinking about a whole new

## 1240:00 - 1295:00

stick that is created. We are now at an

## 1295:00 - 1340:00

era that is the big bang of technologies

## 1340:00 - 1400:00

and you are reinventing a whole array of

## 1400:00 - 1440:00

capabilities technologies that are being

## 1440:00 - 1475:00

brought in play whether it's the prompts

## 1475:00 - 1510:00

the model the infrastructure the

## 1510:00 - 1545:00

platforms and they're all playing

## 1545:00 - 1595:00

together in order to allow customers to

## 1595:00 - 1650:00

leverage AI AI can be used let's say as

## 1650:00 - 1690:00

a employee based like a chat GPD query

## 1690:00 - 1735:00

it can be as part of a SAS like you know

## 1735:00 - 1780:00

in cursor in GitHub copilot and it can

## 1780:00 - 1810:00

be your own developed AI like as an

## 1810:00 - 1840:00

enterprise you're starting to develop

## 1840:00 - 1875:00

applications all of these are leveraging

## 1875:00 - 1930:00

these new technologies now as with any

## 1930:00 - 1970:00

new technology it's based on software

## 1970:00 - 2035:00

and software by itself is obviously can

## 2035:00 - 2065:00

have vulnerabilities so when we think

## 2065:00 - 2110:00

about AI first we need to understand

## 2110:00 - 2145:00

that it's code and code has

## 2145:00 - 2180:00

vulnerabilities like any other software

## 2180:00 - 2225:00

that we have shipped before and it's

## 2225:00 - 2265:00

interesting just a Two weeks ago there

## 2265:00 - 2310:00

was pontoon. You know you know pontoon.

## 2310:00 - 2340:00

It's an amazing event where they bring

## 2340:00 - 2380:00

together the best researchers and this

## 2380:00 - 2415:00

year they had for the first time the AI

## 2415:00 - 2470:00

category. What does it mean AI category?

## 2470:00 - 2505:00

They're basically doing a context to

## 2505:00 - 2545:00

find vulnerabilities in certain

## 2545:00 - 2605:00

technologies and the more you know

## 2605:00 - 2655:00

impactful the vulnerability is h the

## 2655:00 - 2700:00

bigger the bounty you get back. So this

## 2700:00 - 2745:00

time we had for the first time in this

## 2745:00 - 2795:00

spawn to on event the AI category and

## 2795:00 - 2840:00

six technologies were presented. Out of

## 2840:00 - 2885:00

these six technologies four were

## 2885:00 - 2935:00

actually researched and found to be

## 2935:00 - 2975:00

vulnerable at what we call the highest

## 2975:00 - 3025:00

impactful vulnerability which is remote

## 3025:00 - 3065:00

code execution rce which means that you

## 3065:00 - 3105:00

can do anything with that technology.

## 3105:00 - 3145:00

The learning that we have from here is

## 3145:00 - 3200:00

that AI is very new as a software and

## 3200:00 - 3245:00

the fundamentals exist. It's a vulner it

## 3245:00 - 3270:00

can be vulnerable and you can actually

## 3270:00 - 3315:00

use it in order to just run your own

## 3315:00 - 3350:00

code on it like any other technology and

## 3350:00 - 3385:00

software we have used to ship. So that's

## 3385:00 - 3410:00

the first layer. But before you move to

## 3410:00 - 3430:00

the second layer, I just want to make

## 3430:00 - 3465:00

sure I'm understanding this is a

## 3465:00 - 3490:00

research competition.

## 3490:00 - 3525:00

>> Yeah. Was it that there were six AI

## 3525:00 - 3570:00

applications that were developed and of

## 3570:00 - 3610:00

those six they were five that were so

## 3610:00 - 3660:00

vulnerable that uh a bad actor could use

## 3660:00 - 3690:00

those vulnerabilities to remote in and

## 3690:00 - 3740:00

and run this software any way they

## 3740:00 - 3745:00

wanted to.

## 3745:00 - 3770:00

>> Correct. There are six technologies that

## 3770:00 - 3805:00

are used to build AI technologies like

## 3805:00 - 3870:00

Nvidia, like Postgress, SQL. These are

## 3870:00 - 3895:00

radius. These are common technologies

## 3895:00 - 3930:00

that are used to build the application.

## 3930:00 - 3975:00

Out of the six, four actually had

## 3975:00 - 4010:00

critical vulnerabilities at the highest

## 4010:00 - 4055:00

stake. And in by the way, AI has the

## 4055:00 - 4095:00

most vulnerabilities now that are being

## 4095:00 - 4150:00

disclosed with research itself like

## 4150:00 - 4195:00

competed in this pawn to own contest. It

## 4195:00 - 4230:00

won the first place, but we need to

## 4230:00 - 4260:00

understand that this is an area of

## 4260:00 - 4295:00

active research. It's a new technology.

## 4295:00 - 4320:00

Hence, it has a lot to do with the

## 4320:00 - 4365:00

maturity to it. erh in order to get to

## 4365:00 - 4415:00

the level of let's say trust right in

## 4415:00 - 4430:00

the software

## 4430:00 - 4480:00

>> it wasn't just it wasn't just an output

## 4480:00 - 4525:00

of an AI uh

## 4525:00 - 4565:00

>> enabled technology that was vulnerable

## 4565:00 - 4600:00

>> it was the actual building tools that

## 4600:00 - 4640:00

are used to build AI itself were

## 4640:00 - 4680:00

vulnerable all these companies all these

## 4680:00 - 4715:00

engineers who are relying on artificial

## 4715:00 - 4760:00

intelligence tools um because they're so

## 4760:00 - 4805:00

new they they may not know it whereas

## 4805:00 - 4830:00

what you're claiming that they may not

## 4830:00 - 4880:00

know it. Uh but uh bad actors could be

## 4880:00 - 4910:00

basically hacking into the code that

## 4910:00 - 4940:00

they are writing with these tools and

## 4940:00 - 4990:00

then uh not just controlling the the

## 4990:00 - 5020:00

tools themselves but the outputs as

## 5020:00 - 5030:00

well.

## 5030:00 - 5065:00

>> Exactly. And this is what we see. It's

## 5065:00 - 5105:00

scary. It's a new technology stick. It's

## 5105:00 - 5135:00

being built. It's being it's now

## 5135:00 - 5170:00

maturing over time. We're learning about

## 5170:00 - 5200:00

it. We're securing it. We're improving

## 5200:00 - 5240:00

it. But we also need to remember that as

## 5240:00 - 5275:00

with any technology this is new software

## 5275:00 - 5320:00

and it's now being out there you know

## 5320:00 - 5375:00

tested by pentester but also by threat

## 5375:00 - 5405:00

actors. So that's one it's a new

## 5405:00 - 5435:00

technology stick it's important to

## 5435:00 - 5480:00

understand and that's the most important

## 5480:00 - 5505:00

thing to understand about AI. It's

## 5505:00 - 5530:00

software like any other software.

## 5530:00 - 5570:00

>> Five minutes in you've already told me

## 5570:00 - 5610:00

about something that I didn't even

## 5610:00 - 5640:00

anticipate coming in would be a problem

## 5640:00 - 5670:00

which is it's not just the code. the

## 5670:00 - 5700:00

it's the foundational uh tools that are

## 5700:00 - 5720:00

used to output it.

## 5720:00 - 5745:00

>> You're bringing new software.

## 5745:00 - 5765:00

>> Okay. And is the second thing that

## 5765:00 - 5795:00

you're about to go on to the uh

## 5795:00 - 5825:00

unreliability of AI produced code

## 5825:00 - 5840:00

itself?

## 5840:00 - 5865:00

>> Not even that. First, we're going to

## 5865:00 - 5900:00

look at the infrastructure, right?

## 5900:00 - 5930:00

Because in the end, you're running these

## 5930:00 - 5965:00

new tools, but they're running on top of

## 5965:00 - 5985:00

infrastructure like any other

## 5985:00 - 6030:00

application. You have identities,

## 6030:00 - 6060:00

workloads, you have you're using the

## 6060:00 - 6100:00

basic components. uh you are storing

## 6100:00 - 6145:00

your training data sets in buckets that

## 6145:00 - 6180:00

can be now publicly exposed. You're

## 6180:00 - 6215:00

using identities that can be overly

## 6215:00 - 6260:00

permissive. You're using VMs or

## 6260:00 - 6290:00

containers that can be also compromised

## 6290:00 - 6325:00

or misconfigured. So just to translate

## 6325:00 - 6370:00

to a non or less technical audience all

## 6370:00 - 6405:00

these um the infrastructure that you're

## 6405:00 - 6430:00

talking about is you're bu people are

## 6430:00 - 6480:00

building AI programs uh and then they

## 6480:00 - 6525:00

are relying on the cloud correct all the

## 6525:00 - 6565:00

tools that are used to support uh

## 6565:00 - 6595:00

basically anything that runs online

## 6595:00 - 6620:00

software that runs online and there

## 6620:00 - 6660:00

could be vulnerabilities there as well.

## 6660:00 - 6680:00

>> Exactly. vulnerabilities,

## 6680:00 - 6720:00

misconfiguration, and in

## 6720:00 - 6780:00

>> fact you have a program and it's running

## 6780:00 - 6825:00

off of a cloud a cloud system uh but

## 6825:00 - 6870:00

you're exposing a huge part of um the

## 6870:00 - 6900:00

way that your program runs.

## 6900:00 - 6915:00

>> Yeah. Without knowing it.

## 6915:00 - 6970:00

>> Exactly. So if we look at incidents

## 6970:00 - 7025:00

around let's say AI applications

## 7025:00 - 7085:00

we had an incident where a very large I

## 7085:00 - 7120:00

would say software provider exposed a

## 7120:00 - 7165:00

bucket uh through with all of the

## 7165:00 - 7190:00

training data sets in there a lot of

## 7190:00 - 7220:00

sensitive data and they didn't intend to

## 7220:00 - 7270:00

expose it. This is a very basic security

## 7270:00 - 7290:00

issue that we have experienced in the

## 7290:00 - 7340:00

past decade now applied to AI. So again

## 7340:00 - 7390:00

when we think about AI it's not all new.

## 7390:00 - 7420:00

It's new software, it's existing

## 7420:00 - 7455:00

infrastructure and when we think about

## 7455:00 - 7525:00

securing it, the basics apply and it's

## 7525:00 - 7550:00

very important to remember it. The

## 7550:00 - 7585:00

fundamentals apply the fundamentals of

## 7585:00 - 7625:00

patching vulnerabilities, securing

## 7625:00 - 7675:00

configurations, uh, managing identities

## 7675:00 - 7715:00

and so on. So this is like the second

## 7715:00 - 7735:00

layer that we think about the

## 7735:00 - 7745:00

infrastructure.

## 7745:00 - 7770:00

>> Okay. And can I ask one more question

## 7770:00 - 7805:00

about that? So basically what what I

## 7805:00 - 7830:00

imagine a lot of organizations are doing

## 7830:00 - 7855:00

right now is when they want to build

## 7855:00 - 7900:00

personalized AI uh personalized AI tool

## 7900:00 - 7930:00

tools for their company, they're saying

## 7930:00 - 7950:00

we want to build something specific to

## 7950:00 - 7980:00

us that does what we do that can you

## 7980:00 - 8000:00

know maybe replace our employees or

## 8000:00 - 8030:00

augment our employees. Let's just

## 8030:00 - 8050:00

download everything from the

## 8050:00 - 8085:00

organization and we'll throw it into the

## 8085:00 - 8110:00

bot and they've been promised by some

## 8110:00 - 8150:00

API provider that the bot will not use

## 8150:00 - 8180:00

that data for training or it won't spew

## 8180:00 - 8210:00

it out elsewhere. Uh but the thing that

## 8210:00 - 8245:00

they miss is as they download all this

## 8245:00 - 8295:00

important secure information uh uh from

## 8295:00 - 8320:00

their company, they might store it

## 8320:00 - 8350:00

somewhere. Exact. Because where else are

## 8350:00 - 8375:00

you going to have the treasure trove or

## 8375:00 - 8420:00

this like motherload of data other than

## 8420:00 - 8455:00

when you're starting to train a bot

## 8455:00 - 8480:00

specified for your company?

## 8480:00 - 8515:00

>> Exactly. So if I'm a threat actor, why

## 8515:00 - 8550:00

wouldn't I use a good old tech like

## 8550:00 - 8590:00

techniques I'm using to expose buckets,

## 8590:00 - 8640:00

databases, misconfigurations in order to

## 8640:00 - 8680:00

exfiltrate this precious data? why would

## 8680:00 - 8720:00

I go through complicated AI prompts and

## 8720:00 - 8745:00

so on if I can go directly at the

## 8745:00 - 8780:00

infrastructure. So that's a second layer

## 8780:00 - 8820:00

that we have to be mindful of and these

## 8820:00 - 8855:00

are all best practices that we apply and

## 8855:00 - 8905:00

we follow but they apply the same way on

## 8905:00 - 8965:00

our AI applications and actually when we

## 8965:00 - 9005:00

look at AI related incidents the

## 9005:00 - 9065:00

majority of them is within this layer of

## 9065:00 - 9115:00

using the infrastructure in an insecured

## 9115:00 - 9170:00

manner that allows threat actors to just

## 9170:00 - 9205:00

do what they are used to do in cloud in

## 9205:00 - 9220:00

the past.

## 9220:00 - 9245:00

>> Okay. And now let's circle back to the

## 9245:00 - 9265:00

question I asked in the beginning

## 9265:00 - 9290:00

because you know we've been building up

## 9290:00 - 9325:00

to it which is how vulnerable is AI

## 9325:00 - 9340:00

written code?

## 9340:00 - 9375:00

>> So AI written code is interesting

## 9375:00 - 9445:00

because one yes it is it may be more

## 9445:00 - 9480:00

vulnerable because we haven't instructed

## 9480:00 - 9540:00

it to sec to be secured. We need to as

## 9540:00 - 9585:00

we use AI to build applications, we need

## 9585:00 - 9620:00

to also instruct

## 9620:00 - 9660:00

it in what we want the application to

## 9660:00 - 9710:00

do. We need to instruct it in the way we

## 9710:00 - 9755:00

want it to be secured, right? Apply list

## 9755:00 - 9790:00

privileges,

## 9790:00 - 9830:00

remove data if not in use. So there are

## 9830:00 - 9870:00

all of these, you know, best practices

## 9870:00 - 9910:00

in securities that we apply today if we

## 9910:00 - 9945:00

have a human developing it and we review

## 9945:00 - 9990:00

it. But with AI we need to now specify

## 9990:00 - 10050:00

the same manner and as an example uh we

## 10050:00 - 10075:00

have released the research team have

## 10075:00 - 10125:00

released it's it's a rule set that you

## 10125:00 - 10190:00

can feed into AI generate generator like

## 10190:00 - 10235:00

code generator through AI and this rule

## 10235:00 - 10290:00

set will guide AI to build a secure code

## 10290:00 - 10330:00

more than if you didn't and this is just

## 10330:00 - 10365:00

one aspect but the more interesting

## 10365:00 - 10420:00

thing around securing code that is

## 10420:00 - 10465:00

generated by AI is what happens if you

## 10465:00 - 10515:00

actually need to fix it and who is the

## 10515:00 - 10555:00

owner of this code. Now there is a very

## 10555:00 - 10605:00

interesting question that arises because

## 10605:00 - 10670:00

if I'm the developer of the code and now

## 10670:00 - 10700:00

there is a vulnerability or someone

## 10700:00 - 10750:00

reported a security issue I wrote the

## 10750:00 - 10795:00

code I know it by heart and I have

## 10795:00 - 10835:00

someone reviewed it but let's say I vibe

## 10835:00 - 10875:00

code my entire application and it's

## 10875:00 - 10920:00

funny because on the first blog intro

## 10920:00 - 10975:00

like post introducing vibe code the the

## 10975:00 - 11010:00

person who posted it said you can forget

## 11010:00 - 11045:00

that code even exists But no, you

## 11045:00 - 11080:00

cannot. The code is vulnerable and now

## 11080:00 - 11110:00

if something happens, you need to get

## 11110:00 - 11150:00

back to it and fix it. But you need to

## 11150:00 - 11200:00

know the code to do it. So there is a

## 11200:00 - 11245:00

broader questions on responsibility

## 11245:00 - 11275:00

around the code that is generated

## 11275:00 - 11310:00

through AI and who is going to go back

## 11310:00 - 11345:00

and fix it if something happens. By the

## 11345:00 - 11370:00

way, it's not only security also

## 11370:00 - 11415:00

reliability, availability,

## 11415:00 - 11460:00

scale. How do we how do we assure that

## 11460:00 - 11500:00

we have the proper capability to

## 11500:00 - 11535:00

maintain the software that we have shift

## 11535:00 - 11575:00

shift like shipped across security

## 11575:00 - 11600:00

availability reliability in the long

## 11600:00 - 11615:00

term.

## 11615:00 - 11655:00

>> Okay. So I think that what you're saying

## 11655:00 - 11710:00

is basically AI can build pretty secure

## 11710:00 - 11760:00

code if you introduce the instructions

## 11760:00 - 11795:00

or the the protocols to build secure

## 11795:00 - 11815:00

code into the prompt.

## 11815:00 - 11820:00

>> Correct.

## 11820:00 - 11865:00

>> That seems fairly that seems good. But

## 11865:00 - 11910:00

then the other side of it is um what

## 11910:00 - 11940:00

we're seeing now is engineers are

## 11940:00 - 11975:00

starting to be removed from the code

## 11975:00 - 12015:00

that they are writing because often

## 12015:00 - 12060:00

times they are shephering that code

## 12060:00 - 12080:00

through a processing.

## 12080:00 - 12120:00

>> They're vibing it and the AI is is um

## 12120:00 - 12140:00

doing the rest.

## 12140:00 - 12180:00

>> Are we already seeing cyber security

## 12180:00 - 12235:00

problems uh within companies who who

## 12235:00 - 12270:00

have had developers that have just

## 12270:00 - 12320:00

vibecoded or AI coded applications?

## 12320:00 - 12365:00

Yeah, there are actually there are very

## 12365:00 - 12405:00

known examples of someone some people

## 12405:00 - 12440:00

that have posted that they've vibe code

## 12440:00 - 12480:00

an application and then it got hacked

## 12480:00 - 12525:00

hours after or days after and now they

## 12525:00 - 12565:00

don't know how to recover because they

## 12565:00 - 12615:00

didn't have the skill. So the way I'm

## 12615:00 - 12655:00

looking at it is that

## 12655:00 - 12715:00

vibing code is a great way to accelerate

## 12715:00 - 12745:00

but it doesn't remove you from the

## 12745:00 - 12785:00

responsibility of actually knowing your

## 12785:00 - 12820:00

code being able to address issues within

## 12820:00 - 12880:00

the code and guide AI

## 12880:00 - 12920:00

further into the you know maintenance

## 12920:00 - 12960:00

process as we go and use the application

## 12960:00 - 13005:00

and mature the application. So this is I

## 13005:00 - 13040:00

think a maturity thing that we need to

## 13040:00 - 13085:00

go and to do and another aspect is when

## 13085:00 - 13130:00

we think about how would an agent

## 13130:00 - 13160:00

architecture work because you're talking

## 13160:00 - 13220:00

only on one role which is the developer

## 13220:00 - 13265:00

but if we are fast forwarding

## 13265:00 - 13315:00

like agentic concepts into the future.

## 13315:00 - 13355:00

So why wouldn't you have a security

## 13355:00 - 13400:00

reviewer that is also an agent. So you

## 13400:00 - 13430:00

commit code, you're developing your code

## 13430:00 - 13465:00

and next you should have like a security

## 13465:00 - 13505:00

review to your code but also performed

## 13505:00 - 13560:00

by an agent that is minded for security

## 13560:00 - 13590:00

with all the security best practices

## 13590:00 - 13625:00

guideline that we have provided it and

## 13625:00 - 13645:00

someone should maybe look at the

## 13645:00 - 13680:00

architecture and someone should look at

## 13680:00 - 13725:00

data privacy and you can think about and

## 13725:00 - 13770:00

again it doesn't exist today yet but as

## 13770:00 - 13825:00

we fast forward AI doesn't mean that

## 13825:00 - 13860:00

it's only doing the coding it can do

## 13860:00 - 13890:00

other things in the development life

## 13890:00 - 13915:00

cycle that we can rely on.

## 13915:00 - 13940:00

>> But this is scaring me even more because

## 13940:00 - 13975:00

I thought when you said, "Okay, there's

## 13975:00 - 14000:00

people are going to vibe code." By the

## 14000:00 - 14040:00

way, vibe coding is coding just by

## 14040:00 - 14065:00

prompt. So you say, "Build me this

## 14065:00 - 14080:00

application and it builds an

## 14080:00 - 14110:00

application." Um, as opposed to just

## 14110:00 - 14140:00

doing the code yourself. I thought,

## 14140:00 - 14175:00

okay, so now we'll have defined roles.

## 14175:00 - 14215:00

will have you know you if if vive coding

## 14215:00 - 14245:00

becomes a thing people will vibe code

## 14245:00 - 14290:00

applications and the role of a developer

## 14290:00 - 14335:00

will be to audit monitor look for

## 14335:00 - 14380:00

vulnerabilities there and address them.

## 14380:00 - 14415:00

So that will be their expertise is not

## 14415:00 - 14440:00

actually building the things it is

## 14440:00 - 14480:00

securing them uh and maybe improving

## 14480:00 - 14505:00

them in some ways that the bots can't

## 14505:00 - 14540:00

handle. But what you're saying now is

## 14540:00 - 14575:00

we're we now have uh we're looking

## 14575:00 - 14600:00

towards a future where there are going

## 14600:00 - 14655:00

to be agents like another AI bot whose

## 14655:00 - 14700:00

role is to do that thing to secure the

## 14700:00 - 14745:00

Exactly. Okay. So then aren't doesn't

## 14745:00 - 14770:00

that isn't that like a triple risk then

## 14770:00 - 14805:00

or a double risk because you're now

## 14805:00 - 14860:00

going to have uh a AI bot whose core

## 14860:00 - 14895:00

competency is to build an AI bot whose

## 14895:00 - 14930:00

core competency is to secure. So if

## 14930:00 - 14950:00

something goes wrong now, we're

## 14950:00 - 14975:00

definitely not going to have a human

## 14975:00 - 15000:00

with the skills to be able to diagnose

## 15000:00 - 15015:00

and address.

## 15015:00 - 15060:00

>> So it actually doesn't conflict with

## 15060:00 - 15125:00

each each other. We can accelerate or um

## 15125:00 - 15190:00

automate more, but it doesn't actually

## 15190:00 - 15245:00

remove us from the need to have a let's

## 15245:00 - 15290:00

say a human in the loop that we will be

## 15290:00 - 15320:00

able to then account when something

## 15320:00 - 15370:00

happens in the details. So there are two

## 15370:00 - 15405:00

separate questions and that's why when

## 15405:00 - 15445:00

we started I said yeah vibe coding can

## 15445:00 - 15495:00

be improved h it can it can be bad but

## 15495:00 - 15540:00

it can also be improved in various ways

## 15540:00 - 15595:00

but also it doesn't resolve from the

## 15595:00 - 15640:00

actual need to say who is the owner of

## 15640:00 - 15675:00

the code what is the operating model

## 15675:00 - 15715:00

when something happens and let's say AI

## 15715:00 - 15760:00

cannot fix an issue so who does and who

## 15760:00 - 15805:00

owns this over time and this is maybe

## 15805:00 - 15845:00

the most I would say erh

## 15845:00 - 15875:00

when when I look at the challenges

## 15875:00 - 15905:00

technology will continue and accelerate

## 15905:00 - 15940:00

and help us to build the applications

## 15940:00 - 15975:00

but still we have to figure out what is

## 15975:00 - 16010:00

the operating model that when something

## 16010:00 - 16050:00

happens we know who to turn to and we

## 16050:00 - 16080:00

know that we will be able think about it

## 16080:00 - 16105:00

you're an enterprise you're developing

## 16105:00 - 16140:00

an application forget about security

## 16140:00 - 16165:00

let's say basic reliability the

## 16165:00 - 16195:00

application goes down for whatever

## 16195:00 - 16240:00

reason you cannot just wait and rely on

## 16240:00 - 16275:00

you know maybe AI will figure it out

## 16275:00 - 16305:00

maybe it doesn't right we need to

## 16305:00 - 16345:00

>> seems like a bad strategy

## 16345:00 - 16385:00

So we need to have accountability in the

## 16385:00 - 16420:00

end. Okay. So how do we maintain this?

## 16420:00 - 16450:00

And if I'm a developer and I shipped an

## 16450:00 - 16485:00

application and it goes doesn't matter

## 16485:00 - 16525:00

if I built it myself or through AI but

## 16525:00 - 16560:00

it goes down tomorrow and I'm not able

## 16560:00 - 16605:00

to fix it and get it up again. I'm not

## 16605:00 - 16645:00

doing my job right. So this is a big

## 16645:00 - 16685:00

question. How do we continue to own the

## 16685:00 - 16725:00

application while leveraging increasing

## 16725:00 - 16755:00

amount of automation?

## 16755:00 - 16785:00

>> Okay. Okay, so we've talked about the

## 16785:00 - 16815:00

liabilities in the tools you use to

## 16815:00 - 16855:00

build AI. Uh liabilities in the

## 16855:00 - 16880:00

infrastructure used to store key

## 16880:00 - 16915:00

information for AI and now liabilities

## 16915:00 - 16950:00

in AI code and Vive coding in

## 16950:00 - 16975:00

particular. But there's another side to

## 16975:00 - 17020:00

this which is I love the fact that you

## 17020:00 - 17050:00

know people are able to build things

## 17050:00 - 17085:00

just by a prompt now or maybe a little

## 17085:00 - 17115:00

bit more sophisticated. They prompt,

## 17115:00 - 17140:00

they code a little bit, they build off

## 17140:00 - 17160:00

each other and now something that might

## 17160:00 - 17205:00

have taken a team of 10 can be done with

## 17205:00 - 17250:00

one person. Um, but you know, we've

## 17250:00 - 17270:00

called them threat actors. I call them

## 17270:00 - 17295:00

bad actors. Basically, bad guys looking

## 17295:00 - 17345:00

to do damage or looking to hack into to

## 17345:00 - 17375:00

uh computer programs. They have all

## 17375:00 - 17420:00

these tools at their disposal as well.

## 17420:00 - 17480:00

So, are we already seeing them putting

## 17480:00 - 17525:00

those tools to use in an attempt to hack

## 17525:00 - 17565:00

into software? And has that increased

## 17565:00 - 17600:00

the sophistication and the level of

## 17600:00 - 17655:00

hacking that we're seeing already? So

## 17655:00 - 17695:00

there are several ways in which threat

## 17695:00 - 17755:00

actors can use AI. Okay. And the first

## 17755:00 - 17810:00

thing is just hacking into an applica AI

## 17810:00 - 17845:00

application, right? And if you think

## 17845:00 - 17875:00

about how do I hack into AI application

## 17875:00 - 17920:00

and why it's appealing there is what's

## 17920:00 - 17975:00

called like the trifecta of let's say

## 17975:00 - 18015:00

risk factors in AI. One, it's exposed.

## 18015:00 - 18050:00

Second, it has access to private data.

## 18050:00 - 18095:00

Third, you have um untrusted content

## 18095:00 - 18145:00

like the query the you know the chat

## 18145:00 - 18185:00

queries that you send to it the prompt

## 18185:00 - 18220:00

that are expo that is also exposed to

## 18220:00 - 18250:00

the threat actor. So one you have the

## 18250:00 - 18300:00

layer of directly aiming at the AI

## 18300:00 - 18345:00

application and trying to extract via

## 18345:00 - 18385:00

the prompt sensitive data. So that's

## 18385:00 - 18420:00

one. The second thing that you can do

## 18420:00 - 18465:00

you can automate and iterate more on

## 18465:00 - 18500:00

what is already known. And I think this

## 18500:00 - 18530:00

is one thing that we look at AI, it's

## 18530:00 - 18565:00

really good in automating repetitive

## 18565:00 - 18635:00

tests. So instead of trying one type of

## 18635:00 - 18670:00

attack or one type of vulnerability, I

## 18670:00 - 18760:00

can automate and iterate through NI like

## 18760:00 - 18805:00

built like purpose-built application to

## 18805:00 - 18850:00

try and test many more options, right?

## 18850:00 - 18875:00

And then you have the third layer that

## 18875:00 - 18915:00

am I able to discover new type of

## 18915:00 - 18960:00

threats using AI? Am I able to do

## 18960:00 - 19000:00

vulnerability research to find new

## 19000:00 - 19030:00

vulnerabilities because I've trained AI

## 19030:00 - 19065:00

to do something very specific in that

## 19065:00 - 19110:00

case. So these are the three levels that

## 19110:00 - 19155:00

we can look at and I think that the

## 19155:00 - 19210:00

interesting thing is and let's try to

## 19210:00 - 19245:00

tackle it one by one. When I'm targeting

## 19245:00 - 19280:00

directly the AI application, it's like

## 19280:00 - 19315:00

any attack surface. We need now to

## 19315:00 - 19365:00

understand how to secure AI applications

## 19365:00 - 19410:00

the prompt the data within the models

## 19410:00 - 19455:00

against threat actors and that's almost

## 19455:00 - 19515:00

like application security applied to AI

## 19515:00 - 19555:00

whole new stack whole new type of

## 19555:00 - 19595:00

applications still a lot to learn how to

## 19595:00 - 19640:00

secure it and yes threat actors can do

## 19640:00 - 19690:00

it today I think it's very available for

## 19690:00 - 19735:00

them today any we should think about it

## 19735:00 - 19780:00

that any prompt that we exposed is going

## 19780:00 - 19800:00

to

## 19800:00 - 19840:00

tested also by threat actors. So that's

## 19840:00 - 19900:00

one. Second layer, the automation. This

## 19900:00 - 19970:00

touches a very I would say the deep uh

## 19970:00 - 20010:00

issue with security which is the

## 20010:00 - 20065:00

attacker to defender asymmetry. And if

## 20065:00 - 20105:00

we think you know historically just for

## 20105:00 - 20145:00

those who are not familiar the asymmetry

## 20145:00 - 20190:00

means that a defender has to defend on

## 20190:00 - 20230:00

all fronts all of the time while the

## 20230:00 - 20275:00

attacker has to find only one thing that

## 20275:00 - 20310:00

actually works in order to get in. So

## 20310:00 - 20345:00

the asymmetry is insane. It means that

## 20345:00 - 20385:00

the more estate we have the more we need

## 20385:00 - 20425:00

to secure as defenders the harder and

## 20425:00 - 20455:00

harder it becomes because we need to

## 20455:00 - 20495:00

secure everything out there. But the

## 20495:00 - 20530:00

threat actors can find one vulnerability

## 20530:00 - 20585:00

and they will still get in. So

## 20585:00 - 20620:00

historically we've become better and

## 20620:00 - 20665:00

better in improving the ability to

## 20665:00 - 20705:00

secure the foundations, remove the risk

## 20705:00 - 20760:00

proactively, detect and respond. So this

## 20760:00 - 20785:00

is where security has been throughout

## 20785:00 - 20830:00

history. Okay. And improving the our

## 20830:00 - 20875:00

ability to cope with this asymmetry. And

## 20875:00 - 20925:00

now with AI the interesting thing that

## 20925:00 - 20960:00

the threat actors can automate a lot

## 20960:00 - 21020:00

more but from a defense perspective it

## 21020:00 - 21045:00

doesn't give me the same order of

## 21045:00 - 21095:00

magnitude of let's say improvement that

## 21095:00 - 21155:00

the threat actor can gain. So in essence

## 21155:00 - 21205:00

there is an aggravation a significant

## 21205:00 - 21250:00

aggravation in the asymmetry that we're

## 21250:00 - 21300:00

going to face because I can test the

## 21300:00 - 21355:00

threat actors I can try more as a

## 21355:00 - 21400:00

defender it doesn't help me to detect

## 21400:00 - 21450:00

more at the same order of magnitude so

## 21450:00 - 21495:00

this is a challenge that we are going to

## 21495:00 - 21525:00

see more and more more automation on the

## 21525:00 - 21560:00

threat actor side and the reason is that

## 21560:00 - 21605:00

from a detector detection point of view

## 21605:00 - 21645:00

from the defender point of view, I

## 21645:00 - 21685:00

cannot withstand a high false posit pos

## 21685:00 - 21725:00

positive rate. From the threat actor's

## 21725:00 - 21760:00

perspective, I I don't care about the

## 21760:00 - 21795:00

false positive. I just need one. From

## 21795:00 - 21830:00

the detection, if I have a high false

## 21830:00 - 21875:00

positive rate, I'm done. I cannot even I

## 21875:00 - 21925:00

I cannot find the hay in the ST because

## 21925:00 - 21975:00

let's say even if I have 0.1% 0.001%,

## 21975:00 - 22030:00

001%. You take it as much lower as you

## 22030:00 - 22065:00

want. Just multiply it by the attempts

## 22065:00 - 22105:00

of threats that you get, you're going to

## 22105:00 - 22145:00

be bombarded with noise. And noise is

## 22145:00 - 22165:00

the enemy of security.

## 22165:00 - 22195:00

>> They can like DDoS your infrastructure

## 22195:00 - 22215:00

pretty much with attacks.

## 22215:00 - 22255:00

>> DOS your security team. You're actually

## 22255:00 - 22260:00

the

## 22260:00 - 22280:00

>> that's what it is. It's like a physical

## 22280:00 - 22310:00

like we're just going to DDoS is

## 22310:00 - 22330:00

basically you send a bunch of traffic to

## 22330:00 - 22365:00

your website and take it down. So go

## 22365:00 - 22370:00

ahead.

## 22370:00 - 22400:00

>> Yeah. Actually run security. I can tell

## 22400:00 - 22440:00

you a nice story. Not not technology

## 22440:00 - 22465:00

oriented. One time I walked into a

## 22465:00 - 22510:00

building and I saw a new employee

## 22510:00 - 22570:00

training for the guards of the building

## 22570:00 - 22640:00

and um they were just next to the fire

## 22640:00 - 22685:00

like fire alarm. And then the one who

## 22685:00 - 22730:00

was giving the tour was saying if the

## 22730:00 - 22775:00

alarm is sound, if you hear the alarm

## 22775:00 - 22825:00

this is a fire alarm, this is where you

## 22825:00 - 22875:00

go, you turn it off and then the alarm

## 22875:00 - 22915:00

stops. And then a lady asked from the

## 22915:00 - 22950:00

new employees, "And what if it's a real

## 22950:00 - 22990:00

fire?" And he told her, "Listen, it's

## 22990:00 - 23025:00

not a real fire, it's a false alarm."

## 23025:00 - 23060:00

Why do I love this story? Because this

## 23060:00 - 23090:00

is exactly the challenge the security

## 23090:00 - 23140:00

teams have to face with false positives.

## 23140:00 - 23210:00

If we're not going to be really accurate

## 23210:00 - 23260:00

in detecting the highfidelity alerts and

## 23260:00 - 23295:00

really making the extra mile to make

## 23295:00 - 23320:00

sure that if a security team sees

## 23320:00 - 23360:00

something, it's actually it's actually a

## 23360:00 - 23395:00

thing they need to take in very fast.

## 23395:00 - 23440:00

We're becoming like unable to cope with

## 23440:00 - 23450:00

the real threat.

## 23450:00 - 23475:00

>> So this is the risk is that if you

## 23475:00 - 23510:00

automate, if you're a threat actor or

## 23510:00 - 23545:00

someone trying to hack into a system,

## 23545:00 - 23570:00

you can automate it. You can overwhelm a

## 23570:00 - 23595:00

security team because every false

## 23595:00 - 23620:00

positive they need to put attention to

## 23620:00 - 23645:00

and then eventually you get past their

## 23645:00 - 23655:00

defenses.

## 23655:00 - 23710:00

>> Exactly. And this is why there is a good

## 23710:00 - 23745:00

way to tackle this. It's actually

## 23745:00 - 23775:00

reducing the noise by investing more in

## 23775:00 - 23800:00

the fundamentals and less on the

## 23800:00 - 23840:00

detection. Okay. So if we are always

## 23840:00 - 23885:00

trying to detect, it's going to be hard.

## 23885:00 - 23920:00

We're going to be bombarded with alerts.

## 23920:00 - 23965:00

If we're proactively reducing the risk

## 23965:00 - 24015:00

and the chance of being attacked in the

## 24015:00 - 24040:00

first place, namely patching

## 24040:00 - 24060:00

vulnerabilities, fixing

## 24060:00 - 24095:00

misconfigurations, we are in a much

## 24095:00 - 24135:00

better position to turn down the noise.

## 24135:00 - 24175:00

So this is where security has invested a

## 24175:00 - 24205:00

lot of time and now it's going to

## 24205:00 - 24260:00

aggravate if AI is being applied by the

## 24260:00 - 24270:00

threat actors.

## 24270:00 - 24325:00

>> Who are the threat actors?

## 24325:00 - 24370:00

>> Everyone. AI is very accessible as a

## 24370:00 - 24410:00

technology. We need to understand that

## 24410:00 - 24450:00

it's accessible.

## 24450:00 - 24500:00

It's simplified. It can be used at

## 24500:00 - 24545:00

scale. It's not very expensive. You

## 24545:00 - 24580:00

don't need to be a superpower to use it.

## 24580:00 - 24620:00

You don't need a lot of funds to use it

## 24620:00 - 24660:00

to be honest. It's accessible.

## 24660:00 - 24685:00

>> So, is it like organized crime,

## 24685:00 - 24700:00

governments,

## 24700:00 - 24735:00

>> everyone? State nations, organized

## 24735:00 - 24780:00

teenagers, teenagers in basement. Yeah,

## 24780:00 - 24810:00

it's easy. It's accessible. Why wouldn't

## 24810:00 - 24825:00

you do it?

## 24825:00 - 24845:00

>> Well, you could go to jail if you get

## 24845:00 - 24865:00

caught. Oh, I'm saying as a threat

## 24865:00 - 24905:00

actor, why wouldn't you try to use AI?

## 24905:00 - 24925:00

>> I mean, same answer. Oh, why wouldn't

## 24925:00 - 24950:00

you use AI if you're if you if you

## 24950:00 - 24970:00

already decided to do something bad?

## 24970:00 - 25005:00

>> If you are already a threat actor, of

## 25005:00 - 25025:00

course you're going to use AI, right?

## 25025:00 - 25060:00

So, that's why I'm saying as a threat

## 25060:00 - 25100:00

actor, it's a new tool in your stick and

## 25100:00 - 25135:00

now you can leverage it to accelerate to

## 25135:00 - 25180:00

automate. I think there is a thing about

## 25180:00 - 25215:00

cyber crime. It's it's a business,

## 25215:00 - 25250:00

right? And we don't I don't know if we

## 25250:00 - 25280:00

always it's not it's not just bad guys.

## 25280:00 - 25325:00

These are like businesses. H if you

## 25325:00 - 25360:00

think about ransomware, it's a business.

## 25360:00 - 25405:00

It has rules to it, right? You know,

## 25405:00 - 25435:00

when you pay the ransom, you get the

## 25435:00 - 25470:00

data, right? It's it's a rule. You don't

## 25470:00 - 25500:00

you're not tricked into it because it's

## 25500:00 - 25520:00

a business and they need to maintain

## 25520:00 - 25575:00

their reputation. So, as a business,

## 25575:00 - 25605:00

same way that any other business is

## 25605:00 - 25635:00

looking into AI and thinking how can we

## 25635:00 - 25685:00

use it to accelerate to automate

## 25685:00 - 25725:00

cyber crime, state nations, they have

## 25725:00 - 25770:00

the same logic. Today, in the year 2025,

## 25770:00 - 25805:00

these bad guys, teenagers in basement,

## 25805:00 - 25820:00

whatever you want to call them,

## 25820:00 - 25865:00

businesses, uh they've had access to

## 25865:00 - 25900:00

pretty sophisticated generative AI for a

## 25900:00 - 25935:00

couple years now. So, talk a little bit

## 25935:00 - 25975:00

about the curve that you've seen since

## 25975:00 - 26015:00

the introduction of Chad GPT. Are we

## 26015:00 - 26055:00

seeing about the same uh threats like

## 26055:00 - 26080:00

we've seen previously or has it

## 26080:00 - 26100:00

escalated exponentially?

## 26100:00 - 26125:00

>> Currently, from what we see, we are

## 26125:00 - 26175:00

seeing and we are releasing like the the

## 26175:00 - 26210:00

state of AI and we are monitoring for

## 26210:00 - 26265:00

threats. there is a site threats with IO

## 26265:00 - 26300:00

that we monitor all of the cloud AI

## 26300:00 - 26345:00

related incidents and we do a breakdown

## 26345:00 - 26385:00

of basically what was the root cause the

## 26385:00 - 26425:00

techniques in and to be honest we're

## 26425:00 - 26460:00

seeing today more of the same right it's

## 26460:00 - 26490:00

not that we are seeing a significant

## 26490:00 - 26530:00

shift in the threat landscape it's

## 26530:00 - 26560:00

really turning back to the

## 26560:00 - 26595:00

infrastructure the things that we know

## 26595:00 - 26605:00

that are working

## 26605:00 - 26630:00

>> so no the same vulnerabilities but the

## 26630:00 - 26670:00

magnitude of attacks have they gone up

## 26670:00 - 26700:00

>> always they're always trying to do more

## 26700:00 - 26750:00

but you need to remember that al also on

## 26750:00 - 26800:00

the blue side on the defender side we

## 26800:00 - 26845:00

are really getting good in protecting

## 26845:00 - 26900:00

our infrastructure and I think that we

## 26900:00 - 26930:00

are seeing a trend and it's always easy

## 26930:00 - 26960:00

to talk about the increasing rate of

## 26960:00 - 27005:00

attacks and the red side and I think it

## 27005:00 - 27030:00

will always be that way there will

## 27030:00 - 27065:00

always try more it doesn't mean that

## 27065:00 - 27105:00

there will be more successful because on

## 27105:00 - 27140:00

the blue side we have major

## 27140:00 - 27165:00

transformations in how we look at

## 27165:00 - 27205:00

security that is helping us to improve

## 27205:00 - 27230:00

improve the foundation, improve the

## 27230:00 - 27260:00

processes, improve the ability to

## 27260:00 - 27295:00

proactively reduce the risk, the ability

## 27295:00 - 27330:00

to detect and respond. And I think that

## 27330:00 - 27405:00

we are seeing um like since we are still

## 27405:00 - 27455:00

at the foundations that we know how to

## 27455:00 - 27495:00

secure, I think that we are seeing that

## 27495:00 - 27545:00

we are not at the phase that you're

## 27545:00 - 27575:00

saying where we're seeing crazy stuff

## 27575:00 - 27585:00

happening.

## 27585:00 - 27610:00

>> I'm not saying it. I'm just asking about

## 27610:00 - 27615:00

it.

## 27615:00 - 27635:00

>> No, not yet.

## 27635:00 - 27660:00

>> We're not seeing the crazy stuff.

## 27660:00 - 27690:00

>> Why do you think that is? Because I

## 27690:00 - 27715:00

think that with every conversation

## 27715:00 - 27750:00

around generative AI, there's always

## 27750:00 - 27785:00

this, oh, you got to be looking at cyber

## 27785:00 - 27820:00

security part of the conversation

## 27820:00 - 27860:00

because all these tools are in the hands

## 27860:00 - 27890:00

of the bad guys now for all these

## 27890:00 - 27960:00

reasons, but yet we're, you know, in in

## 27960:00 - 28010:00

reality, the actual ability of them to

## 28010:00 - 28060:00

get through is not higher. Is it I mean,

## 28060:00 - 28095:00

is your answer just because companies

## 28095:00 - 28120:00

are doing a better job securing their

## 28120:00 - 28150:00

infrastructure? Because if so, then it's

## 28150:00 - 28185:00

really not a big problem. I think that

## 28185:00 - 28235:00

we are in the process when when I think

## 28235:00 - 28285:00

about like the last decade right

## 28285:00 - 28335:00

>> this process of automation it's not new

## 28335:00 - 28375:00

to us right automation has taken place

## 28375:00 - 28420:00

before AI long before AI and will take

## 28420:00 - 28465:00

it place after AI long before we are

## 28465:00 - 28490:00

always in a journey to continue and

## 28490:00 - 28540:00

automate what threat actors a decade ago

## 28540:00 - 28570:00

have done on the keyboard you know

## 28570:00 - 28615:00

manually and when we look at cloud

## 28615:00 - 28655:00

attacks for instance the ability to

## 28655:00 - 28715:00

automate What happens as soon as I walk

## 28715:00 - 28745:00

into an account as a threat actor? What

## 28745:00 - 28785:00

do I do? Well, I can automate quite a

## 28785:00 - 28810:00

bit. And we have seen this level of

## 28810:00 - 28840:00

automation. We have seen this level of

## 28840:00 - 28875:00

automation for instance with ransomware.

## 28875:00 - 28915:00

We have seen automation happening over

## 28915:00 - 28965:00

the course of the last decade. But in

## 28965:00 - 29000:00

response within security, we have

## 29000:00 - 29035:00

basically developed the capabilities to

## 29035:00 - 29075:00

respond to this automation. AI is

## 29075:00 - 29110:00

another layer that allows us to automate

## 29110:00 - 29150:00

more. right now. Okay, I'm not talking

## 29150:00 - 29180:00

because we're not seeing the crazy new

## 29180:00 - 29240:00

threats yet. We are right now at the

## 29240:00 - 29270:00

phase where we are seeing accelerated

## 29270:00 - 29325:00

automation of the known threats, known

## 29325:00 - 29360:00

risks and this is a journey security has

## 29360:00 - 29400:00

been into in the past decade and it's

## 29400:00 - 29440:00

only one step up. So it's interesting

## 29440:00 - 29475:00

because I guess it's what you're talking

## 29475:00 - 29510:00

about sort of follows I think a lot of

## 29510:00 - 29555:00

the progression of generative AI to date

## 29555:00 - 29580:00

which is that it's a very promising

## 29580:00 - 29620:00

technology but companies trying to put

## 29620:00 - 29645:00

because if bad guys are companies

## 29645:00 - 29675:00

they're businesses companies trying to

## 29675:00 - 29710:00

put it into action have seen mixed

## 29710:00 - 29730:00

results and so actually what I'm getting

## 29730:00 - 29760:00

from you is same thing happen is

## 29760:00 - 29795:00

happening with the bad actors but then

## 29795:00 - 29835:00

the question is if these models get much

## 29835:00 - 29890:00

more intelligent um does that open us up

## 29890:00 - 29950:00

to bigger risks I believe there are

## 29950:00 - 29985:00

areas that

## 29985:00 - 30030:00

yes if they become increasingly better.

## 30030:00 - 30060:00

Let's take vulnerability research as an

## 30060:00 - 30105:00

example. Vulnerability research is one

## 30105:00 - 30135:00

area. Let's explain what's a

## 30135:00 - 30180:00

vulnerability. Okay. A vulnerability by

## 30180:00 - 30215:00

definition is ability to move from one

## 30215:00 - 30250:00

trust level to another trust level in a

## 30250:00 - 30285:00

way that is not permitted. For instance,

## 30285:00 - 30330:00

if I can run remote code, then I'm

## 30330:00 - 30370:00

moving from the outside to the inside.

## 30370:00 - 30400:00

And this is the worst that can happen

## 30400:00 - 30430:00

because I'm literally running code from

## 30430:00 - 30475:00

remotely external in your internal

## 30475:00 - 30500:00

environment. Right? So that's a

## 30500:00 - 30570:00

vulnerability. A vulnerability can be un

## 30570:00 - 30630:00

like unauthenticated access. So

## 30630:00 - 30665:00

authentication bypass. I'm logging in

## 30665:00 - 30740:00

and I have this trick that I'm giving a

## 30740:00 - 30770:00

false password and I'm still able to

## 30770:00 - 30800:00

login. Okay, that's authentication

## 30800:00 - 30850:00

bypass. I was able to walk into an un

## 30850:00 - 30890:00

like a higher trust without the

## 30890:00 - 30915:00

permission to do so. So that's a

## 30915:00 - 30960:00

vulnerability. The ability to research

## 30960:00 - 31020:00

and find vulnerabilities. This is kind

## 31020:00 - 31060:00

of the bottleneck of the security space.

## 31060:00 - 31095:00

Okay? Because vulnerabilities are what

## 31095:00 - 31145:00

allow threat actors to move from, you

## 31145:00 - 31180:00

know, low trust to higher trust

## 31180:00 - 31225:00

environments. And the ability to

## 31225:00 - 31285:00

automate research by

## 31285:00 - 31330:00

you know AI of vulnerabilities can open

## 31330:00 - 31385:00

up maybe a race where you can find many

## 31385:00 - 31425:00

vulnerabilities and unable to patch them

## 31425:00 - 31465:00

at the same pace.

## 31465:00 - 31500:00

There are solutions today that are

## 31500:00 - 31545:00

already leveraging AI to detect

## 31545:00 - 31575:00

vulnerabilities.

## 31575:00 - 31610:00

These are companies, security companies

## 31610:00 - 31650:00

that are using AI to analyze your code

## 31650:00 - 31680:00

and find vulnerabilities in your code

## 31680:00 - 31735:00

that up until today you needed like a

## 31735:00 - 31775:00

very deep research to do it and it's

## 31775:00 - 31820:00

automated. It's really nice from a

## 31820:00 - 31860:00

security perspective. Threat actors may

## 31860:00 - 31905:00

try to weaponize it to find faster and

## 31905:00 - 31940:00

faster vulnerabilities and automate the

## 31940:00 - 31980:00

process to put it into action so that

## 31980:00 - 32020:00

they can always use what we call in the

## 32020:00 - 32070:00

industry zero day vulnerabilities. Zero

## 32070:00 - 32100:00

day vulnerabilities means that it's a

## 32100:00 - 32130:00

vulnerability that besides the threat

## 32130:00 - 32165:00

actor that found it, no one else has

## 32165:00 - 32210:00

seen it. So it's

## 32210:00 - 32245:00

under the radar. That's the meaning of a

## 32245:00 - 32290:00

zero day vulnerability. So if we look

## 32290:00 - 32330:00

into what could be a risk, yes, if we're

## 32330:00 - 32385:00

able to create a perpetu that finds

## 32385:00 - 32425:00

vulnerabilities, operationalize them,

## 32425:00 - 32490:00

and puts it into action, it's scary. But

## 32490:00 - 32535:00

I think that today we're again looking

## 32535:00 - 32600:00

at the detection mechanism and so on,

## 32600:00 - 32605:00

>> right?

## 32605:00 - 32625:00

>> Keeping the fight.

## 32625:00 - 32650:00

>> Okay. So we're deep into the

## 32650:00 - 32680:00

conversation, but good time to really

## 32680:00 - 32710:00

introduce what Whiz is. I mentioned in

## 32710:00 - 32740:00

the beginning that Whiz has sold to

## 32740:00 - 32800:00

Google for 32 billion. Um, so what your

## 32800:00 - 32850:00

company does is basically just that. It

## 32850:00 - 32885:00

looks at everything and you correct me

## 32885:00 - 32910:00

if I'm wrong, but looks at everything

## 32910:00 - 32955:00

that an organization has uh in the cloud

## 32955:00 - 33000:00

and tries to find those vulnerabilities

## 33000:00 - 33025:00

proactively.

## 33025:00 - 33065:00

>> Correct. Whis connects uh very quickly

## 33065:00 - 33105:00

to any cloud environment and assesses

## 33105:00 - 33155:00

all of the risks to the cloud. We call

## 33155:00 - 33200:00

them attack p. So risks that you know we

## 33200:00 - 33230:00

talked about the noise. We remove the

## 33230:00 - 33280:00

noise. We focus on really what are the

## 33280:00 - 33320:00

critical attack path that threat actors

## 33320:00 - 33355:00

can use in order to get gain access to

## 33355:00 - 33405:00

an environment and we surface them to

## 33405:00 - 33440:00

security and development teams so they

## 33440:00 - 33485:00

can proactively reduce the risks before

## 33485:00 - 33510:00

the bad guys find them.

## 33510:00 - 33550:00

>> Okay, so that's what WHIS does.

## 33550:00 - 33585:00

Interestingly, it doesn't happen only in

## 33585:00 - 33620:00

cloud. We can do the same thing

## 33620:00 - 33630:00

>> on prem

## 33630:00 - 33680:00

>> on on prem private cloud but also during

## 33680:00 - 33715:00

the coding phase which is even more

## 33715:00 - 33750:00

interesting. This means that as you are

## 33750:00 - 33800:00

developing, I can actually predict what

## 33800:00 - 33845:00

would become a critical attack path and

## 33845:00 - 33890:00

guardrail and let's say help developers

## 33890:00 - 33925:00

make the right choices while developing

## 33925:00 - 33950:00

before it gets to the cloud. Right?

## 33950:00 - 33985:00

>> So this is like even preventive

## 33985:00 - 34030:00

security. So this is and the last pillar

## 34030:00 - 34055:00

is like detective. This is where we

## 34055:00 - 34090:00

don't want to be but we have to have the

## 34090:00 - 34120:00

controls is to monitor the cloud

## 34120:00 - 34140:00

environment and if we are seeing a

## 34140:00 - 34180:00

suspicious activity detect and respond

## 34180:00 - 34220:00

to it. So this is a bit on what whis

## 34220:00 - 34225:00

does.

## 34225:00 - 34250:00

>> Do you think increasing threats from

## 34250:00 - 34280:00

generative AI played into why Google

## 34280:00 - 34315:00

wanted to acquire the company?

## 34315:00 - 34365:00

>> Security again it's a

## 34365:00 - 34405:00

we're in this battle for decades. I

## 34405:00 - 34420:00

think

## 34420:00 - 34455:00

>> we are improving dramatically as an

## 34455:00 - 34495:00

industry. I think the generative AI

## 34495:00 - 34550:00

increases one the use of software. So

## 34550:00 - 34605:00

cloud security has become even more

## 34605:00 - 34635:00

important today because we understand

## 34635:00 - 34685:00

that AI will be used at scale by any

## 34685:00 - 34715:00

business. By the way, historically we're

## 34715:00 - 34750:00

looking at cloud. There were I call it

## 34750:00 - 34785:00

three migration waves into cloud. The

## 34785:00 - 34825:00

first one were the cloud natives.

## 34825:00 - 34870:00

Spotify okay we're recording in Spotify

## 34870:00 - 34880:00

studios.

## 34880:00 - 34930:00

>> So we are cloud native started in cloud

## 34930:00 - 34975:00

born to cloud. Then came covid. Covid

## 34975:00 - 35005:00

actually brought the second wave where

## 35005:00 - 35040:00

businesses realized that staying on prem

## 35040:00 - 35070:00

means they may be disconnected from

## 35070:00 - 35110:00

their business and moving to cloud is

## 35110:00 - 35150:00

the way to go and they then came the

## 35150:00 - 35205:00

second wave right the during covid the

## 35205:00 - 35240:00

major the banks the financial pharma

## 35240:00 - 35265:00

they all moved to cloud because they

## 35265:00 - 35295:00

realized okay that's not the playground

## 35295:00 - 35325:00

that's a strategy and now we're are

## 35325:00 - 35365:00

watching at the third wave which is AI

## 35365:00 - 35405:00

so AI augments the use of cloud it

## 35405:00 - 35430:00

augments the use of technologies

## 35430:00 - 35485:00

transformation into cloud and AI and it

## 35485:00 - 35520:00

all piles up in the same direction. So

## 35520:00 - 35555:00

just going back to the point yes AI

## 35555:00 - 35590:00

increases the use of software increases

## 35590:00 - 35645:00

the importance of cloud AI security what

## 35645:00 - 35675:00

we call the fundamentals how do we build

## 35675:00 - 35715:00

secure application so absolutely it

## 35715:00 - 35765:00

plays into how do we think about you

## 35765:00 - 35800:00

know strategically what's important for

## 35800:00 - 35840:00

an organization cloud and AI security

## 35840:00 - 35885:00

right so that's one second thing I do

## 35885:00 - 35940:00

think that AI requires us to innovate

## 35940:00 - 35985:00

faster than ever before and this is an

## 35985:00 - 36010:00

interesting piece we talked about the

## 36010:00 - 36055:00

new STE, we talk about new threats, we

## 36055:00 - 36085:00

we can talk about the pace of adoption

## 36085:00 - 36120:00

of technologies which is also

## 36120:00 - 36155:00

mind-blowing.

## 36155:00 - 36215:00

We are at an era that we are innovating

## 36215:00 - 36285:00

more than ever before. And in order to

## 36285:00 - 36325:00

keep up, you need solutions that can

## 36325:00 - 36370:00

help security to enable the business to

## 36370:00 - 36410:00

move forward and not secure a solution

## 36410:00 - 36450:00

that will block sec, you know, block the

## 36450:00 - 36485:00

business from using technologies. And I

## 36485:00 - 36520:00

think that when you look at whiz, whis

## 36520:00 - 36555:00

is really a technology that allows

## 36555:00 - 36600:00

organizations to adopt technologies in a

## 36600:00 - 36635:00

way that enable the business rather than

## 36635:00 - 36660:00

blocking the business. And this will

## 36660:00 - 36700:00

become a critical attribute for any

## 36700:00 - 36750:00

company out there. Otherwise, you know,

## 36750:00 - 36795:00

AI is moving and businesses will move

## 36795:00 - 36825:00

with AI and any other business should

## 36825:00 - 36860:00

keep up with AI because this is going to

## 36860:00 - 36910:00

define businesses in the upcoming years.

## 36910:00 - 36950:00

>> Yeah. I mean I I think that I'll just

## 36950:00 - 36990:00

add that obviously like Google is trying

## 36990:00 - 37030:00

to be the one where startups anyone

## 37030:00 - 37050:00

who's trying to build I mean they're

## 37050:00 - 37070:00

seeing tremendous growth in cloud I

## 37070:00 - 37115:00

think like 30% quarter over quarter uh

## 37115:00 - 37145:00

in the most recent quarter but that's

## 37145:00 - 37190:00

been the case for for a while as AI has

## 37190:00 - 37230:00

built up and if there's a chance that

## 37230:00 - 37275:00

these vulnerabilities actually start to

## 37275:00 - 37325:00

um show themselves and become more

## 37325:00 - 37365:00

difficult then I would imagine that Whiz

## 37365:00 - 37390:00

is pretty well suited to help them out

## 37390:00 - 37420:00

there. I think there is an interesting

## 37420:00 - 37450:00

concept for those who are not familiar

## 37450:00 - 37505:00

with the history of cyber security. Um

## 37505:00 - 37550:00

there was a very interesting initiative

## 37550:00 - 37610:00

um back in even I think basically in the

## 37610:00 - 37685:00

2000 okay year 2000 of by Microsoft and

## 37685:00 - 37730:00

I want to just it was called trustworthy

## 37730:00 - 37780:00

computing and trustworthy computing was

## 37780:00 - 37835:00

around this concept that if humans won't

## 37835:00 - 37890:00

be able to trust their compute they

## 37890:00 - 37915:00

won't use it

## 37915:00 - 37950:00

>> and that started a whole initiative

## 37950:00 - 37995:00

within Microsoft to secure Windows to

## 37995:00 - 38025:00

secure all of the software that they

## 38025:00 - 38060:00

ship. And this changed the security

## 38060:00 - 38110:00

industry forever because this created

## 38110:00 - 38140:00

the concept that security has to be

## 38140:00 - 38170:00

built in in order for people to trust

## 38170:00 - 38210:00

it. And when we think about AI, when we

## 38210:00 - 38245:00

think about cloud, security has to be

## 38245:00 - 38280:00

baked into these processes. So we can

## 38280:00 - 38335:00

trust anything that we leverage in terms

## 38335:00 - 38385:00

of cloud and AI moving forward. Security

## 38385:00 - 38435:00

is a cornerstone for our ability to use

## 38435:00 - 38500:00

technologies at scale. And yeah, this is

## 38500:00 - 38550:00

I think we have to solve it, right? We

## 38550:00 - 38585:00

have to make sure we can trust cloud and

## 38585:00 - 38590:00

AI.

## 38590:00 - 38615:00

>> Oh, clearly Google thinks so. I mean, I

## 38615:00 - 38635:00

think this was the biggest acquisition

## 38635:00 - 38650:00

in their history.

## 38650:00 - 38660:00

>> Correct.

## 38660:00 - 38690:00

>> So, it tells you everything you need to

## 38690:00 - 38715:00

know. All right, we got to take a break.

## 38715:00 - 38740:00

Uh, but after we come back, I want to

## 38740:00 - 38780:00

talk about what might uh be like the big

## 38780:00 - 38825:00

black swan events, whether uh bad actors

## 38825:00 - 38855:00

can hack into humanoid robots when we

## 38855:00 - 38890:00

see them. And also, you had a very

## 38890:00 - 38910:00

interesting report on Deep Seek when it

## 38910:00 - 38935:00

came out. So, we'll touch on that as

## 38935:00 - 38965:00

well. All right, back right after this

## 38965:00 - 39000:00

and we're back here on Big Technology

## 39000:00 - 39035:00

Podcast with Enon Costika, the

## 39035:00 - 39080:00

co-founder of Whiz, also its VP of

## 39080:00 - 39135:00

product. Um, uh, let's talk about, uh,

## 39135:00 - 39170:00

DeepSeek right away because there was an

## 39170:00 - 39200:00

interesting release that Whiz put out

## 39200:00 - 39250:00

when Deepseek was, um, sort of all the

## 39250:00 - 39285:00

rage and it got a lot of headlines.

## 39285:00 - 39320:00

Yeah. Uh, it was here, this is from your

## 39320:00 - 39360:00

blog. Whiz research uncovers exposed

## 39360:00 - 39400:00

deepseek database leaking sensitive

## 39400:00 - 39455:00

information including chat history. Now,

## 39455:00 - 39490:00

I took issue with this because I I had

## 39490:00 - 39535:00

just met you at the Amazon um the re

## 39535:00 - 39565:00

reinvent conference and you had talked

## 39565:00 - 39610:00

to me about how what Whiz does is it

## 39610:00 - 39635:00

proactively we were just talking about

## 39635:00 - 39670:00

before the break. It proactively looks

## 39670:00 - 39700:00

through your code and finds things that

## 39700:00 - 39755:00

might be exposed. And I saw this blog

## 39755:00 - 39790:00

post and I was like, well, that's what

## 39790:00 - 39820:00

Wiz does. And you could probably write

## 39820:00 - 39860:00

similar headlines about many different

## 39860:00 - 39905:00

uh companies. And I think what happened

## 39905:00 - 39970:00

was this the news cycle ran with it and

## 39970:00 - 40010:00

and people who were uh afraid of

## 40010:00 - 40060:00

deepseek pointed to it and said ah look

## 40060:00 - 40095:00

deepseek is trying to leak your

## 40095:00 - 40125:00

information to the Chinese Communist

## 40125:00 - 40160:00

Party which is actually not what it was.

## 40160:00 - 40180:00

So what do you think about my read on

## 40180:00 - 40225:00

the situation there? Okay, so let's go

## 40225:00 - 40265:00

back on the details on the deepseick.

## 40265:00 - 40300:00

What happened? Deepseek was introduced

## 40300:00 - 40345:00

and gained a lot of traction and

## 40345:00 - 40400:00

interest from businesses, media,

## 40400:00 - 40445:00

everything and from our research team as

## 40445:00 - 40510:00

well looking into um DeepSync and the

## 40510:00 - 40550:00

research team found again we talked

## 40550:00 - 40590:00

about it in the fundamentals. It's not a

## 40590:00 - 40640:00

very advanced AI you know centric

## 40640:00 - 40680:00

capability. It's an exposed database in

## 40680:00 - 40720:00

the end if we simplify it that includes

## 40720:00 - 40790:00

a lot of sensitive data uh from deepseek

## 40790:00 - 40880:00

h they closed uh the exposure after uh

## 40880:00 - 40935:00

we disclosed it and then we published a

## 40935:00 - 40990:00

blog post about the fact that deepse had

## 40990:00 - 41055:00

a an open open database if we simplify

## 41055:00 - 41105:00

and I think that deepseek has a few in

## 41105:00 - 41145:00

the deepseek that week there are a Few

## 41145:00 - 41190:00

interesting things that worth noting.

## 41190:00 - 41240:00

One, deepseek adoption was something

## 41240:00 - 41290:00

that we need to pause and understand how

## 41290:00 - 41355:00

fast technologies can propagate uh

## 41355:00 - 41445:00

within our estate. H within a week

## 41445:00 - 41500:00

almost 10% of organizations were using

## 41500:00 - 41540:00

deepseek

## 41540:00 - 41605:00

let it sink. Okay, within a week and I

## 41605:00 - 41645:00

think that this is just one aspect of

## 41645:00 - 41695:00

when we think about you know from a

## 41695:00 - 41735:00

security perspective what do we need to

## 41735:00 - 41795:00

do as we are facing this rapid adoption

## 41795:00 - 41840:00

of new technologies in the end deepseek

## 41840:00 - 41870:00

raises interesting questions around I'm

## 41870:00 - 41920:00

going to use it to train s on sensitive

## 41920:00 - 41955:00

data I'm going to what are the questions

## 41955:00 - 42000:00

that we should be asking when we bring a

## 42000:00 - 42040:00

new technology into play by the way it's

## 42040:00 - 42080:00

not just dipsick any technologies that

## 42080:00 - 42115:00

we're bringing in and I think deepseek

## 42115:00 - 42160:00

was interesting because of the rapid

## 42160:00 - 42200:00

adoption on one hand second the

## 42200:00 - 42240:00

questions around okay where did it come

## 42240:00 - 42290:00

from it came out of nowhere right nobody

## 42290:00 - 42330:00

anticipated it and all of a sudden

## 42330:00 - 42365:00

everybody started downloading the models

## 42365:00 - 42425:00

using it and third we found what is a

## 42425:00 - 42470:00

critical vulnerability that we felt like

## 42470:00 - 42495:00

you know we need to let people know

## 42495:00 - 42555:00

about and I think that these areas. This

## 42555:00 - 42585:00

is

## 42585:00 - 42630:00

really important for teams to ask the

## 42630:00 - 42680:00

question on how do we enable safe use of

## 42680:00 - 42725:00

technologies that doesn't h prohibit the

## 42725:00 - 42770:00

business from using them but does in

## 42770:00 - 42800:00

like

## 42800:00 - 42855:00

instill uh the security measures we need

## 42855:00 - 42905:00

h in place and this is really around

## 42905:00 - 42945:00

what we've learned from this deepseek

## 42945:00 - 42980:00

technology is adopted faster than ever

## 42980:00 - 43010:00

we need to know what we're what our

## 43010:00 - 43045:00

teams are doing with the technology And

## 43045:00 - 43085:00

third, we need to do the scrutiny around

## 43085:00 - 43110:00

what is the security posture of the

## 43110:00 - 43145:00

technologies we use. Again, deepseek

## 43145:00 - 43195:00

like any other AI tools. As we talked

## 43195:00 - 43240:00

about earlier, it's a new space, new

## 43240:00 - 43280:00

software. It's it's being developed as

## 43280:00 - 43325:00

we go. We need to put the to scrutinize

## 43325:00 - 43360:00

the technologies as being adopted as we

## 43360:00 - 43385:00

have done in the past decade. It's

## 43385:00 - 43400:00

nothing new.

## 43400:00 - 43420:00

>> But my point is I feel like you guys

## 43420:00 - 43450:00

find similar vulnerabilities like the

## 43450:00 - 43480:00

one that you found with DeepSeek every

## 43480:00 - 43500:00

day. Mhm.

## 43500:00 - 43570:00

>> And this release let it let the media

## 43570:00 - 43595:00

run with this. There was already fear of

## 43595:00 - 43630:00

deepseek and the media kind of ran with

## 43630:00 - 43665:00

it and said see these you know the whole

## 43665:00 - 43700:00

point of deepseek was like a data

## 43700:00 - 43740:00

exfiltration exercise.

## 43740:00 - 43770:00

>> This is what the media takes of it

## 43770:00 - 43775:00

right.

## 43775:00 - 43795:00

>> So yeah but I want to hear from you what

## 43795:00 - 43805:00

what was really

## 43805:00 - 43830:00

>> I think that in general we focused on

## 43830:00 - 43880:00

the research on the entire AI stack over

## 43880:00 - 43930:00

the past year and a half. uh we launched

## 43930:00 - 43975:00

products to secure AI AISPM and which is

## 43975:00 - 44015:00

AI security posture management we have

## 44015:00 - 44050:00

released the AI state of the union like

## 44050:00 - 44090:00

what's being used not used and I think

## 44090:00 - 44125:00

we have also researched many many AI

## 44125:00 - 44170:00

technologies and that we found to be

## 44170:00 - 44200:00

vulnerable you can cover in our

## 44200:00 - 44230:00

>> you said earlier five of six of these

## 44230:00 - 44265:00

foundational technologies exactly so was

## 44265:00 - 44300:00

the were the vulnerabilities in deepseek

## 44300:00 - 44365:00

any worse than what you typically find

## 44365:00 - 44415:00

>> it was a very what I would a typical

## 44415:00 - 44465:00

exposure that exposed a lot of sensitive

## 44465:00 - 44525:00

data. But yet if we look historically

## 44525:00 - 44555:00

there were similar incidents for

## 44555:00 - 44590:00

instance with Microsoft releasing a

## 44590:00 - 44630:00

token that had access to sensitive data

## 44630:00 - 44680:00

in you know a bucket used for training

## 44680:00 - 44735:00

AI and I think there is there are

## 44735:00 - 44770:00

vulnerabilities more complex but

## 44770:00 - 44810:00

vulnerabilities in Nvidia's toolkits

## 44810:00 - 44850:00

that they released for developing AI. I

## 44850:00 - 44880:00

think what media does with it is one

## 44880:00 - 44960:00

thing right but the research shows like

## 44960:00 - 44990:00

throughout the past years and the

## 44990:00 - 45040:00

research we are we have shared on around

## 45040:00 - 45090:00

AI that AI really the messages that we

## 45090:00 - 45155:00

started with AI is a new stack of tools

## 45155:00 - 45185:00

there there are software tools they have

## 45185:00 - 45235:00

vulnerabilities we need to put the

## 45235:00 - 45295:00

effort to secure it by the way the the

## 45295:00 - 45345:00

tools we use and the infrastructure we

## 45345:00 - 45410:00

It doesn't mean that we can obiate the

## 45410:00 - 45445:00

need to do infrastructure security the

## 45445:00 - 45475:00

same way that we have done. And that's

## 45475:00 - 45505:00

basically the message I think that we

## 45505:00 - 45535:00

should all take including from the

## 45535:00 - 45575:00

deepseek incident. This is a very common

## 45575:00 - 45620:00

misconfiguration that happens.

## 45620:00 - 45645:00

>> Yeah. Exposing a database.

## 45645:00 - 45660:00

>> Having spoken with you, I was thinking

## 45660:00 - 45695:00

that as well and I was like trying to be

## 45695:00 - 45725:00

like come on. But I think that it's good

## 45725:00 - 45755:00

that you guys talked about it. But I

## 45755:00 - 45785:00

feel like the I'm looking back at the

## 45785:00 - 45820:00

story of the context the media missed is

## 45820:00 - 45845:00

this stuff happens all the time to

## 45845:00 - 45855:00

everybody.

## 45855:00 - 45885:00

>> Yeah. New

## 45885:00 - 45895:00

>> everybody.

## 45895:00 - 45940:00

>> All right. Uh let's talk about some uh

## 45940:00 - 45970:00

wild stuff now. Some more pie in the sky

## 45970:00 - 46025:00

things. Uh so all these AI labs are

## 46025:00 - 46045:00

trying to develop super intelligence.

## 46045:00 - 46070:00

They've gone from like AGI to super

## 46070:00 - 46100:00

intelligence over the course of a couple

## 46100:00 - 46135:00

of months. Uh one of the things that you

## 46135:00 - 46170:00

can you would imagine you would find is

## 46170:00 - 46205:00

is uh with super intelligence is the

## 46205:00 - 46265:00

ability to break into anything. Uh I I

## 46265:00 - 46290:00

was speaking with a researcher recently

## 46290:00 - 46310:00

who gave this interesting thought

## 46310:00 - 46345:00

experiment that I kind of want to run by

## 46345:00 - 46375:00

you. I do want to run by you which is

## 46375:00 - 46445:00

that um if an a if if an AI lab built an

## 46445:00 - 46510:00

AI system uh that was an expert at

## 46510:00 - 46540:00

detecting vulnerabilities could get past

## 46540:00 - 46590:00

any system today no matter how good. you

## 46590:00 - 46625:00

know, no offense to anyone working in AI

## 46625:00 - 46650:00

security, but the idea of super

## 46650:00 - 46690:00

intelligence is you can surpass what

## 46690:00 - 46725:00

exists today. Would they then have and

## 46725:00 - 46780:00

and they imagine they saw um other labs

## 46780:00 - 46815:00

getting close to building the same

## 46815:00 - 46855:00

thing, which would eventually like

## 46855:00 - 46890:00

destroy security on the internet, but

## 46890:00 - 46920:00

they then have a responsibility to go in

## 46920:00 - 46980:00

and delete the competing AIs because of

## 46980:00 - 47005:00

what could happen if this technology

## 47005:00 - 47065:00

prolifer proliferates.

## 47065:00 - 47110:00

You're looking at it from the threat

## 47110:00 - 47145:00

perspective. I always try to think about

## 47145:00 - 47180:00

it from the defender perspective. Are we

## 47180:00 - 47220:00

able to

## 47220:00 - 47250:00

generate faster technologies that will

## 47250:00 - 47290:00

defend against this sort of stuff?

## 47290:00 - 47310:00

>> But doesn't the idea of super

## 47310:00 - 47345:00

intelligence then worry you a little bit

## 47345:00 - 47380:00

because a we're not quite sure. I mean

## 47380:00 - 47410:00

if it happens and it's still a big if,

## 47410:00 - 47430:00

we're not quite sure if it's going to be

## 47430:00 - 47450:00

something that's developed by the good

## 47450:00 - 47485:00

guys or the bad guys. And even if it's

## 47485:00 - 47515:00

developed by the quote unquote good

## 47515:00 - 47555:00

guys, there could be hidden bad stuff

## 47555:00 - 47580:00

going in there going on in there.

## 47580:00 - 47610:00

>> It's true to any technology. Quantum

## 47610:00 - 47645:00

computing is another example. Like there

## 47645:00 - 47675:00

are many new technologies and there will

## 47675:00 - 47710:00

always be new technologies that will be

## 47710:00 - 47750:00

introduced. And I think that as

## 47750:00 - 47790:00

defenders

## 47790:00 - 47840:00

and in general as a good guys, we need

## 47840:00 - 47885:00

to think about how do we create the

## 47885:00 - 47940:00

proper guard rails to secure and build

## 47940:00 - 47980:00

foundations that help us to continue and

## 47980:00 - 48020:00

adopt technologies in a way that is

## 48020:00 - 48060:00

controlled manner and secured. Now of

## 48060:00 - 48090:00

course you can think about scenarios

## 48090:00 - 48125:00

that are far exceeds the worst case

## 48125:00 - 48160:00

scenarios that we have seen up until now

## 48160:00 - 48215:00

with security. But I think that

## 48215:00 - 48245:00

historically that wasn't the case. And

## 48245:00 - 48280:00

historically the same things were said

## 48280:00 - 48320:00

about cloud. They were said about data

## 48320:00 - 48355:00

legs. They were said about containers.

## 48355:00 - 48400:00

They were said about many different uh

## 48400:00 - 48440:00

innovations that were introduced. And I

## 48440:00 - 48470:00

think that we were good enough in an

## 48470:00 - 48505:00

industry. I'll give you like the

## 48505:00 - 48540:00

positive perspective. Most of the

## 48540:00 - 48580:00

technologies that were introduced in the

## 48580:00 - 48620:00

past were introduced without thinking

## 48620:00 - 48675:00

about security at all. And if we think

## 48675:00 - 48735:00

about you know the said story of you

## 48735:00 - 48780:00

know why we ended up in a I would say a

## 48780:00 - 48815:00

huge deficit of security in the industry

## 48815:00 - 48850:00

it's because security always came later

## 48850:00 - 48900:00

on it came bolt on we invented

## 48900:00 - 48930:00

autonomous cars and then we figured out

## 48930:00 - 48970:00

okay so you know they can now be

## 48970:00 - 49025:00

controlled and you know being you know

## 49025:00 - 49065:00

crashed into places without control so

## 49065:00 - 49110:00

we need to secure it. um the concepts

## 49110:00 - 49180:00

behind uh I think today AI security are

## 49180:00 - 49240:00

actually well thought today rather than

## 49240:00 - 49285:00

much later and it shows a bit on the

## 49285:00 - 49330:00

maturity of not only the security teams

## 49330:00 - 49350:00

by the way it shows a lot on the

## 49350:00 - 49390:00

maturity of the industry that we are

## 49390:00 - 49445:00

having the discussion on what's safe AI

## 49445:00 - 49505:00

what how to secure AI architecture and

## 49505:00 - 49555:00

unlike before you know talking about new

## 49555:00 - 49595:00

technologies and their Security was

## 49595:00 - 49630:00

always something that were was perceived

## 49630:00 - 49690:00

as a inhibitor to innovation. Let's

## 49690:00 - 49720:00

let's get it right first and then let's

## 49720:00 - 49760:00

secure it. Let's not let's not get the

## 49760:00 - 49805:00

folks scared about it, right? So they

## 49805:00 - 49840:00

won't block it. But today it's actually

## 49840:00 - 49885:00

a much more I would say integrated

## 49885:00 - 49920:00

discussion of of course we're using

## 49920:00 - 49955:00

going to use AI but of course we're

## 49955:00 - 50000:00

going also to uh put the guardrail the

## 50000:00 - 50040:00

security in place the standards. We're

## 50040:00 - 50080:00

going to ask the questions. So as we do

## 50080:00 - 50125:00

this, we also develop the muscle of

## 50125:00 - 50185:00

let's secure AI at the get-go. And I

## 50185:00 - 50210:00

think it actually shows a lot on the

## 50210:00 - 50265:00

maturity. I'm I'm I'm I'm positive

## 50265:00 - 50280:00

actually. Yes.

## 50280:00 - 50315:00

>> About this because I think we are at a

## 50315:00 - 50360:00

position that we've never been in it

## 50360:00 - 50390:00

before. Like it's it's relatively new

## 50390:00 - 50420:00

that we talk about technology and the

## 50420:00 - 50440:00

security of the technology at the same

## 50440:00 - 50480:00

time. It's great. I mean, I know you're

## 50480:00 - 50510:00

in security and so I would I guess I'd

## 50510:00 - 50540:00

be optimistic if I was, you know,

## 50540:00 - 50565:00

co-founding a security company, but I

## 50565:00 - 50620:00

think you're underrating the risks.

## 50620:00 - 50660:00

>> I just think that as an industry, we are

## 50660:00 - 50700:00

there are always risks and the risks are

## 50700:00 - 50730:00

always

## 50730:00 - 50775:00

scary and they far exceed what you know

## 50775:00 - 50820:00

ordinary people can think about when

## 50820:00 - 50860:00

they just see a technology. But I do

## 50860:00 - 50905:00

think that we have strong foundations

## 50905:00 - 50945:00

within the security industry and the uh

## 50945:00 - 50985:00

development industry to build the proper

## 50985:00 - 51030:00

guardrails and I have trust that we have

## 51030:00 - 51080:00

established enough track record on how

## 51080:00 - 51115:00

to secure

## 51115:00 - 51155:00

applications environments that we can

## 51155:00 - 51200:00

continue and innovate and as I'm going

## 51200:00 - 51230:00

to talk not only about whiz like the

## 51230:00 - 51270:00

entire industry if I look today at the

## 51270:00 - 51310:00

pace of innovation around AI security

## 51310:00 - 51335:00

look about look at the number of

## 51335:00 - 51360:00

startups that are already focusing on

## 51360:00 - 51405:00

providing solutions to AI security, AI

## 51405:00 - 51440:00

firewalls, AI security posture

## 51440:00 - 51495:00

management tools, AI security gateways,

## 51495:00 - 51525:00

right? There is a whole array of

## 51525:00 - 51570:00

security industry solutions that are

## 51570:00 - 51635:00

basically creating AI aware controls

## 51635:00 - 51685:00

that are now already in place already in

## 51685:00 - 51715:00

place. It's not like futuristic. It's

## 51715:00 - 51745:00

existing solutions. Yes, we need to

## 51745:00 - 51780:00

mature. Yes, we need to research. Yes,

## 51780:00 - 51815:00

we need to do a lot more. But we are

## 51815:00 - 51860:00

building the capabilities towards there.

## 51860:00 - 51880:00

>> What about quantum? You mentioned

## 51880:00 - 51910:00

quantum. Uh everyone talks about how

## 51910:00 - 51950:00

quantum will break encryption and break

## 51950:00 - 51985:00

security. You have a big smile already

## 51985:00 - 52000:00

hearing the word

## 52000:00 - 52030:00

>> quantum is interesting. I think it's

## 52030:00 - 52085:00

also it's an exercise, right? What if

## 52085:00 - 52115:00

exercise? I think we're seeing a lot

## 52115:00 - 52175:00

more awareness to post quantum

## 52175:00 - 52210:00

cryptography, right? the ability to

## 52210:00 - 52250:00

basically use cryptography that will

## 52250:00 - 52310:00

withstand quantum quantum you know if

## 52310:00 - 52360:00

quantum computing happens what happen

## 52360:00 - 52390:00

>> I don't know I'm not in the space for

## 52390:00 - 52430:00

speculations I do think that you know

## 52430:00 - 52500:00

it's good practice to improve again

## 52500:00 - 52530:00

>> you it's the same thread actually it's

## 52530:00 - 52555:00

interesting because you will hear me

## 52555:00 - 52605:00

giving the same speech about quantum

## 52605:00 - 52650:00

computing like security as AI there are

## 52650:00 - 52700:00

foundations we need to be really good in

## 52700:00 - 52735:00

running initiatives that will that will

## 52735:00 - 52785:00

secure our foundations in AI. It can be

## 52785:00 - 52830:00

whatever we talked about but in quantum

## 52830:00 - 52860:00

computing it should be about using the

## 52860:00 - 52890:00

cryptographic tools that we that are

## 52890:00 - 52940:00

suitable for this era and we do I think

## 52940:00 - 52970:00

the one thing that has changed around

## 52970:00 - 53020:00

quantum computing is a thought of maybe

## 53020:00 - 53070:00

it is closer than we think and then the

## 53070:00 - 53120:00

threat actors are you know stealing data

## 53120:00 - 53155:00

now so they will be able to decrypt it

## 53155:00 - 53200:00

later once they you know figure it out.

## 53200:00 - 53210:00

>> That's interesting.

## 53210:00 - 53250:00

>> So you know steal now decrypt later.

## 53250:00 - 53305:00

Yes, it's it's an experime it's you know

## 53305:00 - 53350:00

it's a thought right we need to also

## 53350:00 - 53380:00

give it attention and I think there are

## 53380:00 - 53410:00

more and more companies especially

## 53410:00 - 53460:00

regulated companies

## 53460:00 - 53500:00

government that want to make sure that

## 53500:00 - 53540:00

they are securing their data today

## 53540:00 - 53575:00

against crypto like postquantum

## 53575:00 - 53610:00

cryptographic risks. So, all right. I

## 53610:00 - 53640:00

want to end with this. Um, I want to

## 53640:00 - 53675:00

talk a little bit about the threat to

## 53675:00 - 53725:00

hacking uh autonomous vehicles and

## 53725:00 - 53755:00

humanoid robots if they eventually show

## 53755:00 - 53770:00

up.

## 53770:00 - 53810:00

>> I have to ask this in a way that we

## 53810:00 - 53840:00

don't get the same I'm confident we'll

## 53840:00 - 53890:00

be able to get ahead of it response. Um,

## 53890:00 - 53925:00

because I actually want to know like,

## 53925:00 - 53945:00

you know, what's likely to happen if

## 53945:00 - 53980:00

this actually goes down. I heard you

## 53980:00 - 54020:00

speaking recently about there's been

## 54020:00 - 54065:00

attacks on hospitals where um their

## 54065:00 - 54120:00

system uh their systems have broken down

## 54120:00 - 54160:00

and they've been unable to uh send

## 54160:00 - 54190:00

dispatches out and give care to people.

## 54190:00 - 54195:00

Yeah.

## 54195:00 - 54220:00

>> Um

## 54220:00 - 54265:00

if if this happens hypothetically uh is

## 54265:00 - 54310:00

it a magnitude greater risk if let's say

## 54310:00 - 54330:00

humanoid robots which might be in

## 54330:00 - 54385:00

people's h houses or embedded in society

## 54385:00 - 54425:00

or autonomous cars which we know are

## 54425:00 - 54465:00

like all over the roads now. If there's

## 54465:00 - 54490:00

a vulnerability there, is that like a

## 54490:00 - 54530:00

level up from just the typical software

## 54530:00 - 54550:00

hack?

## 54550:00 - 54590:00

>> You know, there are there are things

## 54590:00 - 54620:00

that happened in the history of cyber

## 54620:00 - 54665:00

that were very surprising. For instance,

## 54665:00 - 54710:00

what would happen if I break into your,

## 54710:00 - 54740:00

you know, I don't know, oven, it has an

## 54740:00 - 54795:00

IP. I'm breaking into your, you know,

## 54795:00 - 54830:00

remote cameras. What will happen? Just

## 54830:00 - 54870:00

I'm getting installing something there.

## 54870:00 - 54905:00

So

## 54905:00 - 54945:00

historically there was a DOS attack that

## 54945:00 - 54990:00

actually utilized all of these IoTs in

## 54990:00 - 55035:00

order to target one specific let's say

## 55035:00 - 55080:00

target and they brought it down because

## 55080:00 - 55105:00

we're talking about millions and

## 55105:00 - 55140:00

millions of devices that are flooding a

## 55140:00 - 55170:00

certain area but who thought that this

## 55170:00 - 55240:00

will be the use of these IoT right it's

## 55240:00 - 55275:00

a very creative use by the threat actors

## 55275:00 - 55340:00

right and I think that the way we think

## 55340:00 - 55375:00

about the risks

## 55375:00 - 55405:00

Threat actors are very creative in how

## 55405:00 - 55445:00

they utilize these sorts of stuff. And

## 55445:00 - 55480:00

it's not always in, you know, the direct

## 55480:00 - 55510:00

way. Okay, we're going to hack

## 55510:00 - 55570:00

autonomous cars to run into people and

## 55570:00 - 55605:00

robots to go into people's house and do

## 55605:00 - 55650:00

stuff. But I think that this can cause

## 55650:00 - 55690:00

significant outages for instance, right?

## 55690:00 - 55755:00

We can use it. It can cause significant

## 55755:00 - 55785:00

dysfunctional,

## 55785:00 - 55835:00

let's say, societies, right? if we rely

## 55835:00 - 55875:00

on it too much or we don't have the

## 55875:00 - 55915:00

proper ways to secure against it. So I

## 55915:00 - 55955:00

do think that as things evolve we do

## 55955:00 - 55985:00

need to

## 55985:00 - 56040:00

always think about how this can be used

## 56040:00 - 56090:00

not only in the direct way but also in

## 56090:00 - 56165:00

part of other campaigns that can take

## 56165:00 - 56230:00

place in cyber and with this creativity

## 56230:00 - 56300:00

is amazing in when we innovate h it's

## 56300:00 - 56340:00

frightening when it's used by the threat

## 56340:00 - 56375:00

actors right we're seeing it you know

## 56375:00 - 56415:00

not only in cyber we're seeing it in

## 56415:00 - 56505:00

everywhere, right? And

## 56505:00 - 56565:00

I think we should be always,

## 56565:00 - 56610:00

I would say it, careful about the way we

## 56610:00 - 56645:00

apply technologies to our day-to-day and

## 56645:00 - 56685:00

the guardrails we put into play. Uh

## 56685:00 - 56720:00

because the last thing we want to do is

## 56720:00 - 56770:00

to build trust on something that breaks

## 56770:00 - 56795:00

at some point and we don't have the

## 56795:00 - 56825:00

guardrails to protect against it. Yeah,

## 56825:00 - 56865:00

it's kind of crazy because um throughout

## 56865:00 - 56895:00

this conversation we've talked about uh

## 56895:00 - 56930:00

how we're relying more on AI to code and

## 56930:00 - 56955:00

now we're going to rely more on

## 56955:00 - 57000:00

technology to work autonomously in our

## 57000:00 - 57045:00

society whether that's agents uh taking

## 57045:00 - 57075:00

action our behalf on our behalf with

## 57075:00 - 57115:00

computer use or whether that's cars or

## 57115:00 - 57165:00

humanoid robots and so I think when

## 57165:00 - 57190:00

people like look at the trend of why

## 57190:00 - 57245:00

cyber security is important the more

## 57245:00 - 57290:00

cyber we put in our life so to speak the

## 57290:00 - 57325:00

more security we're going to

## 57325:00 - 57365:00

Correct. The more state we cover, the

## 57365:00 - 57415:00

more security we need. And one concept,

## 57415:00 - 57445:00

you know, one concept that I do want to

## 57445:00 - 57475:00

say, something that was a cornerstone

## 57475:00 - 57510:00

for, at least from my experience with

## 57510:00 - 57545:00

customers in cloud security, it's a

## 57545:00 - 57590:00

concept of democratizing security.

## 57590:00 - 57635:00

Because if we think about just security

## 57635:00 - 57665:00

teams doing security for the whole

## 57665:00 - 57705:00

world, it's not going to scale. But if

## 57705:00 - 57755:00

we think about our responsibility as

## 57755:00 - 57820:00

employees, humans, developers,

## 57820:00 - 57865:00

security teams, IT teams and how can we

## 57865:00 - 57915:00

contribute to this resilience of our

## 57915:00 - 57950:00

systems, right? The cyber resilience of

## 57950:00 - 57985:00

the technologies that we use, this is

## 57985:00 - 58030:00

going to end up in a I think a much more

## 58030:00 - 58080:00

scalable approach to security. And one

## 58080:00 - 58120:00

of the most interesting trends in cyber

## 58120:00 - 58150:00

security is actually that

## 58150:00 - 58195:00

democratization aspect. Another very

## 58195:00 - 58240:00

simple example is fishing emails, right?

## 58240:00 - 58270:00

If we're just a security team, one

## 58270:00 - 58300:00

security training team tries to filter

## 58300:00 - 58335:00

all emails, you know, something will get

## 58335:00 - 58365:00

in and in the end will work. But

## 58365:00 - 58385:00

>> yeah, we haven't even spoken about

## 58385:00 - 58425:00

people uh spoofing other people's voices

## 58425:00 - 58460:00

to try to get in also. See, that's

## 58460:00 - 58470:00

happening now.

## 58470:00 - 58490:00

>> That's happening. That's happening.

## 58490:00 - 58510:00

We've seen live cases

## 58510:00 - 58530:00

>> protect against that.

## 58530:00 - 58575:00

>> This is another as I said, all security

## 58575:00 - 58625:00

products across the industry should

## 58625:00 - 58660:00

become AI aware. Right.

## 58660:00 - 58700:00

>> And if I'm thinking about anti-ishing

## 58700:00 - 58755:00

tools, they need to be able to cope with

## 58755:00 - 58815:00

emails that are created via AI generated

## 58815:00 - 58850:00

capabilities that are very very targeted

## 58850:00 - 58900:00

and seem very very credible. So email

## 58900:00 - 58935:00

security tools should be able to find

## 58935:00 - 58995:00

them. Fishing through fake voice

## 58995:00 - 59040:00

messages deep like basically these are

## 59040:00 - 59075:00

the deep fake stuff. So these are the

## 59075:00 - 59110:00

things that all of the industry has to

## 59110:00 - 59150:00

mature across all of them. There are

## 59150:00 - 59190:00

solutions that are now in play. Security

## 59190:00 - 59245:00

is not security today and this is like

## 59245:00 - 59275:00

me being optimist. I think security

## 59275:00 - 59320:00

today is geared towards finding new

## 59320:00 - 59360:00

threats, responding to them in ways that

## 59360:00 - 59410:00

we can operationalize at scale. But we

## 59410:00 - 59435:00

have to be aware that with new

## 59435:00 - 59470:00

technologies come new threats,

## 59470:00 - 59505:00

>> right? There's a human side to it also,

## 59505:00 - 59550:00

I imagine, where like when somebody is

## 59550:00 - 59575:00

telling you they need money or something

## 59575:00 - 59635:00

like that, like you got to like

## 59635:00 - 59665:00

you can't just believe them anymore.

## 59665:00 - 59690:00

It's weird. Even if it sounds like a

## 59690:00 - 59740:00

parent or sibling, child, there has to

## 59740:00 - 59775:00

be like you have to be like, I'm just

## 59775:00 - 59815:00

trying to be sure that this isn't an AI

## 59815:00 - 59845:00

generated voice. Here are some things

## 59845:00 - 59860:00

I'm going to do to trick.

## 59860:00 - 59885:00

>> Correct. And that's our responsibility

## 59885:00 - 59915:00

in the end. everybody as humans,

## 59915:00 - 59965:00

employees, developers in how do we make

## 59965:00 - 60010:00

sure that we are part of this resilient

## 60010:00 - 60020:00

system.

## 60020:00 - 60055:00

>> Right? So I get I trying to think about

## 60055:00 - 60075:00

how I'm going to how I feel after

## 60075:00 - 60110:00

today's conversation. I mean, on one

## 60110:00 - 60165:00

hand, you sort of help broaden the

## 60165:00 - 60200:00

spectrum of threats that I ever thought

## 60200:00 - 60235:00

about, whether it's the ability to hack

## 60235:00 - 60275:00

the actual tools themselves. On the

## 60275:00 - 60310:00

other hand, it seems like the way that

## 60310:00 - 60350:00

Generative AI is working today, it

## 60350:00 - 60390:00

hasn't led to this massive uptick in

## 60390:00 - 60420:00

security vulnerabilities or even

## 60420:00 - 60450:00

attacks, even though we're always seeing

## 60450:00 - 60495:00

them escalate. So, I I'll choose to

## 60495:00 - 60525:00

leave uh with your perspective,

## 60525:00 - 60565:00

optimistic, and uh we'll have to keep

## 60565:00 - 60580:00

talking.

## 60580:00 - 60610:00

>> Amazing. Thank you very much for having

## 60610:00 - 60640:00

me. >> Thank you, Anon. Thank you everybody for

## 60640:00 - 60665:00

listening. We'll be back on Friday to

## 60665:00 - 60690:00

break down the week's news. Thanks again

## 60690:00 - 60720:00

and we'll see you next time on Big

## 60720:00+

Technology Podcast.

