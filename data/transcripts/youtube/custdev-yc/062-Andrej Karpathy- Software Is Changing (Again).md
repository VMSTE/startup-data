---
source: https://www.youtube.com/watch?v=LCEmiRjPEtQ
title: "Andrej Karpathy: Software Is Changing (Again)"
author: Y Combinator
date: 2025-06-19
views: 2403668
description: |-
  Andrej Karpathy's keynote on June 17, 2025 at AI Startup School in San Francisco. Slides provided by Andrej: https://drive.google.com/file/d/1a0h1mkwfmV2PlekxDN8isMrDA5evc4wW/view?usp=sharing

  Chapters:
  00:00 - Intro
  01:25 - Software evolution: From 1.0 to 3.0
  04:40 - Programming in English: Rise of Software 3.0
  06:10 - LLMs as utilities, fabs, and operating systems
  11:04 - The new LLM OS and historical computing analogies
  14:39 - Psychology of LLMs: People spirits and cognitive quirks
  18:22 - Designing LLM apps with partial autonomy
  23:40 - The importance of human-AI collaboration loops
  26:00 - Lessons from Tesla Autopilot & autonomy sliders
  27:52 - The Iron Man analogy: Augmentation vs. agents
  29:06 - Vibe Coding: Everyone is now a programmer
  33:39 - Building for agents: Future-ready digital infrastructure
  38:14 - Summary: We’re in the 1960s of LLMs — time to build

  Drawing on his work at Stanford, OpenAI, and Tesla, Andrej sees a shift underway. Software is changing, again. We’ve entered the era of “Software 3.0,” where natural language becomes the new programming interface and models do the rest.

  He explores what this shift means for developers, users, and the design of software itself— that we're not just using new tools, but building a new kind of computer.

  More content from Andrej: https://www.youtube.com/@AndrejKarpathy

  Thoughts (From Andrej Karpathy!)
  0:49 - Imo fair to say that software is changing quite fundamentally again. LLMs are a new kind of computer, and you program them *in English*. Hence I think they are well deserving of a major version upgrade in terms of software.
  6:06 - LLMs have properties of utilities, of fabs, and of operating systems → New LLM OS, fabbed by labs, and distributed like utilities (for now). Many historical analogies apply - imo we are computing circa ~1960s.
  14:39 - LLM psychology: LLMs = "people spirits", stochastic simulations of people, where the simulator is an autoregressive Transformer. Since they are trained on human data, they have a kind of emergent psychology, and are simultaneously superhuman in some ways, but also fallible in many others. Given this, how do we productively work with them hand in hand?
  Switching gears to opportunities...
  18:16 - LLMs are "people spirits" → can build partially autonomous products.
  29:05 - LLMs are programmed in English → make software highly accessible! (yes, vibe coding)
  33:36 - LLMs are new primary consumer/manipulator of digital information (adding to GUIs/humans and APIs/programs) → Build for agents!

  Some of the links:
  - Software 2.0 blog post from 2017 https://karpathy.medium.com/software-2-0-a64152b37c35
  - How LLMs flip the script on technology diffusion https://karpathy.bearblog.dev/power-to-the-people/
  - Vibe coding MenuGen (retrospective) https://karpathy.bearblog.dev/vibe-coding-menugen/

  Apply to Y Combinator: https://ycombinator.com/apply
  Work at a startup: https://workatastartup.com
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:45:04.856Z
---

# Andrej Karpathy: Software Is Changing (Again)

## 00:00 - 65:00

Please welcome former director of AI

## 65:00 - 115:00

Tesla Andre Carpathy.

## 115:00 - 190:00

[Music]

## 190:00 - 245:00

Hello.

## 245:00 - 315:00

[Music]

## 315:00 - 380:00

Wow, a lot of people here. Hello.

## 380:00 - 410:00

Um, okay. Yeah. So I'm excited to be

## 410:00 - 450:00

here today to talk to you about software

## 450:00 - 505:00

in the era of AI. And I'm told that many

## 505:00 - 540:00

of you are students like bachelors,

## 540:00 - 570:00

masters, PhD and so on. And you're about

## 570:00 - 605:00

to enter the industry. And I think it's

## 605:00 - 625:00

actually like an extremely unique and

## 625:00 - 645:00

very interesting time to enter the

## 645:00 - 685:00

industry right now. And I think

## 685:00 - 715:00

fundamentally the reason for that is

## 715:00 - 790:00

that um software is changing uh again.

## 790:00 - 830:00

And I say again because I actually gave

## 830:00 - 875:00

this talk already. Um but the problem is

## 875:00 - 900:00

that software keeps changing. So I

## 900:00 - 915:00

actually have a lot of material to

## 915:00 - 945:00

create new talks and I think it's

## 945:00 - 965:00

changing quite fundamentally. I think

## 965:00 - 1005:00

roughly speaking software has not

## 1005:00 - 1030:00

changed much on such a fundamental level

## 1030:00 - 1075:00

for 70 years. And then it's changed I

## 1075:00 - 1110:00

think about twice quite rapidly in the

## 1110:00 - 1140:00

last few years. And so there's just a

## 1140:00 - 1160:00

huge amount of work to do a huge amount

## 1160:00 - 1205:00

of software to write and rewrite. So

## 1205:00 - 1235:00

let's take a look at maybe the realm of

## 1235:00 - 1265:00

software. So if we kind of think of this

## 1265:00 - 1295:00

as like the map of software this is a

## 1295:00 - 1330:00

really cool tool called map of GitHub.

## 1330:00 - 1365:00

Um this is kind of like all the software

## 1365:00 - 1385:00

that's written. Uh these are

## 1385:00 - 1410:00

instructions to the computer for

## 1410:00 - 1440:00

carrying out tasks in the digital space.

## 1440:00 - 1465:00

So if you zoom in here, these are all

## 1465:00 - 1500:00

different kinds of repositories and this

## 1500:00 - 1525:00

is all the code that has been written.

## 1525:00 - 1560:00

And a few years ago I kind of observed

## 1560:00 - 1595:00

that um software was kind of changing

## 1595:00 - 1625:00

and there was kind of like a new type of

## 1625:00 - 1660:00

software around and I called this

## 1660:00 - 1705:00

software 2.0 at the time and the idea

## 1705:00 - 1740:00

here was that software 1.0 is the code

## 1740:00 - 1775:00

you write for the computer. Software 2.0

## 1775:00 - 1810:00

know are basically neural networks and

## 1810:00 - 1835:00

in particular the weights of a neural

## 1835:00 - 1885:00

network and you're not writing this code

## 1885:00 - 1920:00

directly you are most you are more kind

## 1920:00 - 1945:00

of like tuning the data sets and then

## 1945:00 - 1970:00

you're running an optimizer to create to

## 1970:00 - 2010:00

create the parameters of this neural net

## 2010:00 - 2040:00

and I think like at the time neural nets

## 2040:00 - 2060:00

were kind of seen as like just a

## 2060:00 - 2075:00

different kind of classifier like a

## 2075:00 - 2100:00

decision tree or something like that and

## 2100:00 - 2150:00

so I think it was kind of like um I

## 2150:00 - 2170:00

think this framing was a lot more

## 2170:00 - 2200:00

appropriate and now actually what we

## 2200:00 - 2225:00

have is kind of like an equivalent of

## 2225:00 - 2260:00

GitHub in the realm of software 2.0 And

## 2260:00 - 2300:00

I think the hugging face is basically

## 2300:00 - 2345:00

equivalent of GitHub in software 2.0.

## 2345:00 - 2370:00

And there's also model atlas and you can

## 2370:00 - 2400:00

visualize all the code written there. In

## 2400:00 - 2420:00

case you're curious, by the way, the

## 2420:00 - 2470:00

giant circle, the point in the middle,

## 2470:00 - 2510:00

uh these are the parameters of flux, the

## 2510:00 - 2545:00

image generator. And so anytime someone

## 2545:00 - 2580:00

tunes a on top of a flux model, you

## 2580:00 - 2615:00

basically create a git commit uh in this

## 2615:00 - 2650:00

space and uh you create a different kind

## 2650:00 - 2690:00

of a image generator. So basically what

## 2690:00 - 2725:00

we have is software 1.0 is the computer

## 2725:00 - 2765:00

code that programs a computer. Software

## 2765:00 - 2810:00

2.0 are the weights which program neural

## 2810:00 - 2845:00

networks. Uh and here's an example of

## 2845:00 - 2890:00

Alexet image recognizer neural network.

## 2890:00 - 2915:00

Now so far all of the neural networks

## 2915:00 - 2940:00

that we've been familiar with until

## 2940:00 - 2965:00

recently where kind of like fixed

## 2965:00 - 3025:00

function computers image to categories

## 3025:00 - 3055:00

or something like that. And I think

## 3055:00 - 3085:00

what's changed and I think is a quite

## 3085:00 - 3110:00

fundamental change is that neural

## 3110:00 - 3155:00

networks became programmable with large

## 3155:00 - 3200:00

language models. And so I I see this as

## 3200:00 - 3245:00

quite new, unique. It's a new kind of a

## 3245:00 - 3300:00

computer and uh so in my mind it's uh

## 3300:00 - 3325:00

worth giving it a new designation of

## 3325:00 - 3365:00

software 3.0. And basically your prompts

## 3365:00 - 3425:00

are now programs that program the LLM.

## 3425:00 - 3470:00

And uh remarkably uh these uh prompts

## 3470:00 - 3505:00

are written in English. So it's kind of

## 3505:00 - 3555:00

a very interesting programming language.

## 3555:00 - 3610:00

Um so maybe uh to summarize the

## 3610:00 - 3630:00

difference if you're doing sentiment

## 3630:00 - 3655:00

classification for example you can

## 3655:00 - 3705:00

imagine writing some uh amount of Python

## 3705:00 - 3735:00

to to basically do sentiment

## 3735:00 - 3765:00

classification or you can train a neural

## 3765:00 - 3795:00

net or you can prompt a large language

## 3795:00 - 3830:00

model. Uh so here this is a few short

## 3830:00 - 3850:00

prompt and you can imagine changing it

## 3850:00 - 3875:00

and programming the computer in a

## 3875:00 - 3910:00

slightly different way. So basically we

## 3910:00 - 3955:00

have software 1.0 software 2.0 and I

## 3955:00 - 3990:00

think we're seeing maybe you've seen a

## 3990:00 - 4030:00

lot of GitHub code is not just like code

## 4030:00 - 4055:00

anymore. there's a bunch of like English

## 4055:00 - 4090:00

interspersed with code and so I think

## 4090:00 - 4120:00

kind of there's a growing category of

## 4120:00 - 4150:00

new kind of code. So not only is it a

## 4150:00 - 4180:00

new programming paradigm, it's also

## 4180:00 - 4210:00

remarkable to me that it's in our native

## 4210:00 - 4245:00

language of English. And so when this

## 4245:00 - 4295:00

blew my mind a few uh I guess years ago

## 4295:00 - 4345:00

now I tweeted this and um I think it

## 4345:00 - 4365:00

captured the attention of a lot of

## 4365:00 - 4385:00

people and this is my currently pinned

## 4385:00 - 4420:00

tweet uh is that remarkably we're now

## 4420:00 - 4465:00

programming computers in English. Now,

## 4465:00 - 4525:00

when I was at uh Tesla, um we were

## 4525:00 - 4580:00

working on the uh autopilot and uh we

## 4580:00 - 4620:00

were trying to get the car to drive and

## 4620:00 - 4665:00

I sort of showed this slide at the time

## 4665:00 - 4690:00

where you can imagine that the inputs to

## 4690:00 - 4715:00

the car are on the bottom and they're

## 4715:00 - 4740:00

going through a software stack to

## 4740:00 - 4780:00

produce the steering and acceleration

## 4780:00 - 4805:00

and I made the observation at the time

## 4805:00 - 4850:00

that there was a ton of C++ code around

## 4850:00 - 4875:00

in the autopilot which was the software

## 4875:00 - 4905:00

1.0 code and then there was some neural

## 4905:00 - 4945:00

nets in there doing image recognition

## 4945:00 - 4980:00

and uh I kind of observed that over time

## 4980:00 - 5010:00

as we made the autopilot better

## 5010:00 - 5045:00

basically the neural network grew in

## 5045:00 - 5095:00

capability and size and in addition to

## 5095:00 - 5140:00

that all the C++ code was being deleted

## 5140:00 - 5200:00

and kind of like was um and a lot of the

## 5200:00 - 5240:00

kind of capabilities and functionality

## 5240:00 - 5270:00

that was originally written in 1.0 was

## 5270:00 - 5315:00

migrated to 2.0. So as an example, a lot

## 5315:00 - 5345:00

of the stitching up of information

## 5345:00 - 5375:00

across images from the different cameras

## 5375:00 - 5415:00

and across time was done by a neural

## 5415:00 - 5440:00

network and we were able to delete a lot

## 5440:00 - 5495:00

of code and so the software 2.0 stack

## 5495:00 - 5540:00

quite literally ate through the software

## 5540:00 - 5565:00

stack of the autopilot. So I thought

## 5565:00 - 5590:00

this was really remarkable at the time

## 5590:00 - 5615:00

and I think we're seeing the same thing

## 5615:00 - 5655:00

again where uh basically we have a new

## 5655:00 - 5680:00

kind of software and it's eating through

## 5680:00 - 5705:00

the stack. We have three completely

## 5705:00 - 5740:00

different programming paradigms and I

## 5740:00 - 5760:00

think if you're entering the industry

## 5760:00 - 5785:00

it's a very good idea to be fluent in

## 5785:00 - 5820:00

all of them because they all have slight

## 5820:00 - 5845:00

pros and cons and you may want to

## 5845:00 - 5885:00

program some functionality in 1.0 or 2.0

## 5885:00 - 5905:00

or 3.0. Are you going to train

## 5905:00 - 5925:00

neurallet? Are you going to just prompt

## 5925:00 - 5955:00

an LLM? Should this be a piece of code

## 5955:00 - 5985:00

that's explicit etc. So we all have to

## 5985:00 - 6005:00

make these decisions and actually

## 6005:00 - 6055:00

potentially uh fluidly trans transition

## 6055:00 - 6110:00

between these paradigms. So what I

## 6110:00 - 6160:00

wanted to get into now is first I want

## 6160:00 - 6195:00

to in the first part talk about LLMs and

## 6195:00 - 6225:00

how to kind of like think of this new

## 6225:00 - 6250:00

paradigm and the ecosystem and what that

## 6250:00 - 6290:00

looks like. Uh like what are what is

## 6290:00 - 6310:00

this new computer? What does it look

## 6310:00 - 6335:00

like and what does the ecosystem look

## 6335:00 - 6395:00

like? Um I was struck by this quote from

## 6395:00 - 6425:00

Anduring actually uh many years ago now

## 6425:00 - 6455:00

I think and I think Andrew is going to

## 6455:00 - 6490:00

be speaking right after me. Uh but he

## 6490:00 - 6510:00

said at the time AI is the new

## 6510:00 - 6555:00

electricity and I do think that it um

## 6555:00 - 6575:00

kind of captures something very

## 6575:00 - 6610:00

interesting in that LLMs certainly feel

## 6610:00 - 6645:00

like they have properties of utilities

## 6645:00 - 6690:00

right now. So

## 6690:00 - 6735:00

um LLM labs like OpenAI, Gemini,

## 6735:00 - 6785:00

Enthropic etc. They spend capex to train

## 6785:00 - 6810:00

the LLMs and this is kind of equivalent

## 6810:00 - 6850:00

to building out a grid and then there's

## 6850:00 - 6880:00

opex to serve that intelligence over

## 6880:00 - 6940:00

APIs to all of us and this is done

## 6940:00 - 6975:00

through metered access where we pay per

## 6975:00 - 7005:00

million tokens or something like that

## 7005:00 - 7030:00

and we have a lot of demands that are

## 7030:00 - 7065:00

very utility- like demands out of this

## 7065:00 - 7100:00

API we demand low latency high uptime

## 7100:00 - 7145:00

consistent quality etc. In electricity,

## 7145:00 - 7180:00

you would have a transfer switch. So you

## 7180:00 - 7205:00

can transfer your electricity source

## 7205:00 - 7240:00

from like grid and solar or battery or

## 7240:00 - 7280:00

generator. In LLM, we have maybe open

## 7280:00 - 7305:00

router and easily switch between the

## 7305:00 - 7340:00

different types of LLMs that exist.

## 7340:00 - 7380:00

Because the LLM are software, they don't

## 7380:00 - 7415:00

compete for physical space. So it's okay

## 7415:00 - 7445:00

to have basically like six electricity

## 7445:00 - 7465:00

providers and you can switch between

## 7465:00 - 7495:00

them, right? Because they don't compete

## 7495:00 - 7530:00

in such a direct way. And I think what's

## 7530:00 - 7560:00

also a little fascinating and we saw

## 7560:00 - 7605:00

this in the last few days actually a lot

## 7605:00 - 7645:00

of the LLMs went down and people were

## 7645:00 - 7685:00

kind of like stuck and unable to work.

## 7685:00 - 7705:00

And uh I think it's kind of fascinating

## 7705:00 - 7725:00

to me that when the state-of-the-art

## 7725:00 - 7760:00

LLMs go down, it's actually kind of like

## 7760:00 - 7795:00

an intelligence brownout in the world.

## 7795:00 - 7820:00

It's kind of like when the voltage is

## 7820:00 - 7865:00

unreliable in the grid and uh the planet

## 7865:00 - 7915:00

just gets dumber the more reliance we

## 7915:00 - 7945:00

have on these models, which already is

## 7945:00 - 7970:00

like really dramatic and I think will

## 7970:00 - 8010:00

continue to grow. But LLM's don't only

## 8010:00 - 8035:00

have properties of utilities. I think

## 8035:00 - 8055:00

it's also fair to say that they have

## 8055:00 - 8105:00

some properties of fabs. And the reason

## 8105:00 - 8155:00

for this is that the capex required for

## 8155:00 - 8200:00

building LLM is actually quite large. Uh

## 8200:00 - 8235:00

it's not just like building some uh

## 8235:00 - 8265:00

power station or something like that,

## 8265:00 - 8290:00

right? You're investing a huge amount of

## 8290:00 - 8330:00

money and I think the tech tree and uh

## 8330:00 - 8370:00

for the technology is growing quite

## 8370:00 - 8405:00

rapidly. So we're in a world where we

## 8405:00 - 8445:00

have sort of deep tech trees, research

## 8445:00 - 8480:00

and development secrets that are

## 8480:00 - 8535:00

centralizing inside the LLM labs. Um and

## 8535:00 - 8570:00

but I think the analogy muddies a little

## 8570:00 - 8600:00

bit also because as I mentioned this is

## 8600:00 - 8635:00

software and software is a bit less

## 8635:00 - 8680:00

defensible because it is so malleable.

## 8680:00 - 8715:00

And so um I think it's just an

## 8715:00 - 8735:00

interesting kind of thing to think about

## 8735:00 - 8775:00

potentially. There's many analogy

## 8775:00 - 8800:00

analogies you can make like a 4

## 8800:00 - 8825:00

nanometer process node maybe is

## 8825:00 - 8850:00

something like a cluster with certain

## 8850:00 - 8880:00

max flops. You can think about when

## 8880:00 - 8910:00

you're use when you're using Nvidia GPUs

## 8910:00 - 8930:00

and you're only doing the software and

## 8930:00 - 8950:00

you're not doing the hardware. That's

## 8950:00 - 8985:00

kind of like the fabless model. But if

## 8985:00 - 9005:00

you're actually also building your own

## 9005:00 - 9030:00

hardware and you're training on TPUs if

## 9030:00 - 9050:00

you're Google, that's kind of like the

## 9050:00 - 9085:00

Intel model where you own your fab. So I

## 9085:00 - 9105:00

think there's some analogies here that

## 9105:00 - 9135:00

make sense. But actually I think the

## 9135:00 - 9160:00

analogy that makes the most sense

## 9160:00 - 9205:00

perhaps is that in my mind LLM have very

## 9205:00 - 9250:00

strong kind of analogies to operating

## 9250:00 - 9295:00

systems. Uh in that this is not just

## 9295:00 - 9325:00

electricity or water. It's not something

## 9325:00 - 9345:00

that comes out of the tap as a

## 9345:00 - 9380:00

commodity. uh this is these are now

## 9380:00 - 9430:00

increasingly complex software ecosystems

## 9430:00 - 9475:00

right so uh they're not just like simple

## 9475:00 - 9510:00

commodities like electricity and it's

## 9510:00 - 9530:00

kind of interesting to me that the

## 9530:00 - 9565:00

ecosystem is shaping in a very similar

## 9565:00 - 9600:00

kind of way where you have a few closed

## 9600:00 - 9640:00

source providers like Windows or Mac OS

## 9640:00 - 9660:00

and then you have an open source

## 9660:00 - 9710:00

alternative like Linux and I think for u

## 9710:00 - 9755:00

neural for LLMs as well we have a kind

## 9755:00 - 9790:00

of a few competing closed source

## 9790:00 - 9820:00

providers and then maybe the llama

## 9820:00 - 9855:00

ecosystem is currently like maybe a

## 9855:00 - 9885:00

close approximation to something that

## 9885:00 - 9915:00

may grow into something like Linux.

## 9915:00 - 9940:00

Again, I think it's still very early

## 9940:00 - 9965:00

because these are just simple LLMs, but

## 9965:00 - 9990:00

we're starting to see that these are

## 9990:00 - 10015:00

going to get a lot more complicated.

## 10015:00 - 10045:00

It's not just about the LLM itself. It's

## 10045:00 - 10065:00

about all the tool use and the

## 10065:00 - 10090:00

multiodalities and how all of that

## 10090:00 - 10120:00

works. And so when I sort of had this

## 10120:00 - 10155:00

realization a while back, I tried to

## 10155:00 - 10185:00

sketch it out and it kind of seemed to

## 10185:00 - 10210:00

me like LLMs are kind of like a new

## 10210:00 - 10260:00

operating system, right? So the LLM is a

## 10260:00 - 10290:00

new kind of a computer. It's sitting

## 10290:00 - 10325:00

it's kind of like the CPU equivalent. uh

## 10325:00 - 10355:00

the context windows are kind of like the

## 10355:00 - 10405:00

memory and then the LLM is orchestrating

## 10405:00 - 10440:00

memory and compute uh for problem

## 10440:00 - 10495:00

solving um using all of these uh

## 10495:00 - 10540:00

capabilities here and so definitely if

## 10540:00 - 10570:00

you look at it looks very much like

## 10570:00 - 10605:00

operating system from that perspective.

## 10605:00 - 10645:00

Um, a few more analogies. For example,

## 10645:00 - 10685:00

if you want to download an app, say I go

## 10685:00 - 10725:00

to VS Code and I go to download, you can

## 10725:00 - 10770:00

download VS Code and you can run it on

## 10770:00 - 10835:00

Windows, Linux or or Mac in the same way

## 10835:00 - 10885:00

as you can take an LLM app like cursor

## 10885:00 - 10925:00

and you can run it on GPT or cloud or

## 10925:00 - 10955:00

Gemini series, right? It's just a drop

## 10955:00 - 10980:00

down. So, it's kind of like similar in

## 10980:00 - 11010:00

that way as well.

## 11010:00 - 11035:00

uh more analogies that I think strike me

## 11035:00 - 11070:00

is that we're kind of like in this

## 11070:00 - 11095:00

1960sish

## 11095:00 - 11150:00

era where LLM compute is still very

## 11150:00 - 11175:00

expensive for this new kind of a

## 11175:00 - 11220:00

computer and that forces the LLMs to be

## 11220:00 - 11260:00

centralized in the cloud and we're all

## 11260:00 - 11305:00

just uh sort of thing clients that

## 11305:00 - 11335:00

interact with it over the network and

## 11335:00 - 11365:00

none of us have full utilization of

## 11365:00 - 11400:00

these computers and therefore it makes

## 11400:00 - 11435:00

sense to use time sharing where we're

## 11435:00 - 11470:00

all just you know a dimension of the

## 11470:00 - 11500:00

batch when they're running the computer

## 11500:00 - 11530:00

in the cloud. And this is very much what

## 11530:00 - 11555:00

computers used to look like at during

## 11555:00 - 11580:00

this time. The operating systems were in

## 11580:00 - 11600:00

the cloud. Everything was streamed

## 11600:00 - 11660:00

around and there was batching. And so

## 11660:00 - 11690:00

the p the personal computing revolution

## 11690:00 - 11715:00

hasn't happened yet because it's just

## 11715:00 - 11740:00

not economical. It doesn't make sense.

## 11740:00 - 11775:00

But I think some people are trying. And

## 11775:00 - 11805:00

it turns out that Mac minis, for

## 11805:00 - 11835:00

example, are a very good fit for some of

## 11835:00 - 11870:00

the LLMs because it's all if you're

## 11870:00 - 11895:00

doing batch one inference, this is all

## 11895:00 - 11920:00

super memory bound. So this actually

## 11920:00 - 11945:00

works.

## 11945:00 - 11975:00

And uh I think these are some early

## 11975:00 - 12005:00

indications maybe of personal computing.

## 12005:00 - 12030:00

Uh but this hasn't really happened yet.

## 12030:00 - 12055:00

It's not clear what this looks like.

## 12055:00 - 12085:00

Maybe some of you get to invent what

## 12085:00 - 12130:00

what this is or how it works or uh what

## 12130:00 - 12170:00

this should what this should be. Maybe

## 12170:00 - 12200:00

one more analogy that I'll mention is

## 12200:00 - 12240:00

whenever I talk to Chach or some LLM

## 12240:00 - 12270:00

directly in text, I feel like I'm

## 12270:00 - 12305:00

talking to an operating system through

## 12305:00 - 12350:00

the terminal. Like it's just it's it's

## 12350:00 - 12375:00

text. It's direct access to the

## 12375:00 - 12410:00

operating system. And I think a guey

## 12410:00 - 12445:00

hasn't yet really been invented in like

## 12445:00 - 12490:00

a general way like should chatt have a

## 12490:00 - 12520:00

guey like different than just a tech

## 12520:00 - 12555:00

bubbles. Uh certainly some of the apps

## 12555:00 - 12585:00

that we're going to go into in a bit

## 12585:00 - 12640:00

have guey but there's no like guey

## 12640:00 - 12670:00

across all the tasks if that makes

## 12670:00 - 12720:00

sense. Um there are some ways in which

## 12720:00 - 12755:00

LLMs are different from kind of

## 12755:00 - 12790:00

operating systems in some fairly unique

## 12790:00 - 12830:00

way and from early computing. And I

## 12830:00 - 12880:00

wrote about uh this one particular

## 12880:00 - 12900:00

property that strikes me as very

## 12900:00 - 12950:00

different uh this time around. It's that

## 12950:00 - 12995:00

LLMs like flip they flip the direction

## 12995:00 - 13030:00

of technology diffusion uh that is

## 13030:00 - 13085:00

usually uh present in technology. So for

## 13085:00 - 13115:00

example with electricity, cryptography,

## 13115:00 - 13150:00

computing, flight, internet, GPS, lots

## 13150:00 - 13175:00

of new transformative technologies that

## 13175:00 - 13205:00

have not been around. Typically it is

## 13205:00 - 13235:00

the government and corporations that are

## 13235:00 - 13275:00

the first users because it's new and

## 13275:00 - 13310:00

expensive etc. and it only later

## 13310:00 - 13345:00

diffuses to consumer. Uh, but I feel

## 13345:00 - 13365:00

like LLMs are kind of like flipped

## 13365:00 - 13400:00

around. So maybe with early computers,

## 13400:00 - 13430:00

it was all about ballistics and military

## 13430:00 - 13480:00

use, but with LLMs, it's all about how

## 13480:00 - 13505:00

do you boil an egg or something like

## 13505:00 - 13530:00

that. This is certainly like a lot of my

## 13530:00 - 13560:00

use. And so it's really fascinating to

## 13560:00 - 13590:00

me that we have a new magical computer

## 13590:00 - 13620:00

and it's like helping me boil an egg.

## 13620:00 - 13645:00

It's not helping the government do

## 13645:00 - 13675:00

something really crazy like some

## 13675:00 - 13700:00

military ballistics or some special

## 13700:00 - 13730:00

technology. Indeed, corporations are

## 13730:00 - 13750:00

governments are lagging behind the

## 13750:00 - 13785:00

adoption of all of us, of all of these

## 13785:00 - 13815:00

technologies. So, it's just backwards

## 13815:00 - 13840:00

and I think it informs maybe some of the

## 13840:00 - 13870:00

uses of how we want to use this

## 13870:00 - 13890:00

technology or like where are some of the

## 13890:00 - 13930:00

first apps and so on.

## 13930:00 - 14015:00

So, in summary so far, LLM labs LLMs. I

## 14015:00 - 14060:00

think it's accurate language to use, but

## 14060:00 - 14105:00

LLMs are complicated operating systems.

## 14105:00 - 14140:00

They're circa 1960s in computing and

## 14140:00 - 14170:00

we're redoing computing all over again.

## 14170:00 - 14195:00

and they're currently available via time

## 14195:00 - 14230:00

sharing and distributed like a utility.

## 14230:00 - 14265:00

What is new and unprecedented is that

## 14265:00 - 14285:00

they're not in the hands of a few

## 14285:00 - 14310:00

governments and corporations. They're in

## 14310:00 - 14335:00

the hands of all of us because we all

## 14335:00 - 14360:00

have a computer and it's all just

## 14360:00 - 14405:00

software and Chaship was beamed down to

## 14405:00 - 14440:00

our computers like billions of people

## 14440:00 - 14470:00

like instantly and overnight and this is

## 14470:00 - 14510:00

insane. Uh and it's kind of insane to me

## 14510:00 - 14550:00

that this is the case and now it is our

## 14550:00 - 14580:00

time to enter the industry and program

## 14580:00 - 14620:00

these computers. This is crazy. So I

## 14620:00 - 14660:00

think this is quite remarkable. Before

## 14660:00 - 14700:00

we program LLMs, we have to kind of like

## 14700:00 - 14725:00

spend some time to think about what

## 14725:00 - 14760:00

these things are. And I especially like

## 14760:00 - 14805:00

to kind of talk about their psychology.

## 14805:00 - 14840:00

So the way I like to think about LLMs is

## 14840:00 - 14855:00

that they're kind of like people

## 14855:00 - 14900:00

spirits. Um they are stoastic

## 14900:00 - 14935:00

simulations of people. Um and the

## 14935:00 - 14965:00

simulator in this case happens to be an

## 14965:00 - 14995:00

auto reggressive transformer. So

## 14995:00 - 15045:00

transformer is a neural net. Uh it's and

## 15045:00 - 15080:00

it just kind of like is goes on the

## 15080:00 - 15105:00

level of tokens. It goes chunk chunk

## 15105:00 - 15135:00

chunk chunk chunk. And there's an almost

## 15135:00 - 15165:00

equal amount of compute for every single

## 15165:00 - 15245:00

chunk. Um and um this simulator of

## 15245:00 - 15280:00

course is is just is basically there's

## 15280:00 - 15315:00

some weights involved and we fit it to

## 15315:00 - 15340:00

all of text that we have on the internet

## 15340:00 - 15365:00

and so on. And you end up with this kind

## 15365:00 - 15400:00

of a simulator and because it is trained

## 15400:00 - 15435:00

on humans, it's got this emergent

## 15435:00 - 15470:00

psychology that is humanlike. So the

## 15470:00 - 15510:00

first thing you'll notice is of course

## 15510:00 - 15540:00

uh LLM have encyclopedic knowledge and

## 15540:00 - 15575:00

memory. uh and they can remember lots of

## 15575:00 - 15600:00

things, a lot more than any single

## 15600:00 - 15625:00

individual human can because they read

## 15625:00 - 15660:00

so many things. It's it actually kind of

## 15660:00 - 15690:00

reminds me of this movie Rainman, which

## 15690:00 - 15715:00

I actually really recommend people

## 15715:00 - 15740:00

watch. It's an amazing movie. I love

## 15740:00 - 15775:00

this movie. Um and Dustin Hoffman here

## 15775:00 - 15815:00

is an autistic savant who has almost

## 15815:00 - 15860:00

perfect memory. So, he can read a he can

## 15860:00 - 15885:00

read like a phone book and remember all

## 15885:00 - 15920:00

of the names and phone numbers. And I

## 15920:00 - 15950:00

kind of feel like LM are kind of like

## 15950:00 - 15980:00

very similar. They can remember Shaw

## 15980:00 - 16005:00

hashes and lots of different kinds of

## 16005:00 - 16040:00

things very very easily. So they

## 16040:00 - 16070:00

certainly have superpowers in some set

## 16070:00 - 16100:00

in some respects. But they also have a

## 16100:00 - 16145:00

bunch of I would say cognitive deficits.

## 16145:00 - 16195:00

So they hallucinate quite a bit. Um and

## 16195:00 - 16215:00

they kind of make up stuff and don't

## 16215:00 - 16250:00

have a very good uh sort of internal

## 16250:00 - 16290:00

model of self-nowledge, not sufficient

## 16290:00 - 16320:00

at least. And this has gotten better but

## 16320:00 - 16360:00

not perfect. They display jagged

## 16360:00 - 16380:00

intelligence. So they're going to be

## 16380:00 - 16405:00

superhuman in some problems solving

## 16405:00 - 16430:00

domains. And then they're going to make

## 16430:00 - 16460:00

mistakes that basically no human will

## 16460:00 - 16495:00

make. like you know they will insist

## 16495:00 - 16540:00

that 9.11 is greater than 9.9 or that

## 16540:00 - 16570:00

there are two Rs in strawberry these are

## 16570:00 - 16600:00

some famous examples but basically there

## 16600:00 - 16645:00

are rough edges that you can trip on so

## 16645:00 - 16670:00

that's kind of I think also kind of

## 16670:00 - 16720:00

unique um they also kind of suffer from

## 16720:00 - 16780:00

entrograde amnesia um so uh and I think

## 16780:00 - 16800:00

I'm alluding to the fact that if you

## 16800:00 - 16820:00

have a co-orker who joins your

## 16820:00 - 16855:00

organization this co-orker will over

## 16855:00 - 16900:00

time learn your organization and uh they

## 16900:00 - 16930:00

will understand and gain like a huge

## 16930:00 - 16960:00

amount of context on the organization

## 16960:00 - 16990:00

and they go home and they sleep and they

## 16990:00 - 17015:00

consolidate knowledge and they develop

## 17015:00 - 17055:00

expertise over time. LLMs don't natively

## 17055:00 - 17075:00

do this and this is not something that

## 17075:00 - 17105:00

has really been solved in the R&D of

## 17105:00 - 17150:00

LLM. I think um and so context windows

## 17150:00 - 17175:00

are really kind of like working memory

## 17175:00 - 17200:00

and you have to sort of program the

## 17200:00 - 17225:00

working memory quite directly because

## 17225:00 - 17250:00

they don't just kind of like get smarter

## 17250:00 - 17280:00

by uh by default and I think a lot of

## 17280:00 - 17315:00

people get tripped up by the analogies

## 17315:00 - 17370:00

uh in this way. Uh in popular culture I

## 17370:00 - 17395:00

recommend people watch these two movies

## 17395:00 - 17430:00

uh Momento and 51st dates. In both of

## 17430:00 - 17460:00

these movies, the protagonists, their

## 17460:00 - 17495:00

weights are fixed and their context

## 17495:00 - 17535:00

windows gets wiped every single morning

## 17535:00 - 17570:00

and it's really problematic to go to

## 17570:00 - 17595:00

work or have relationships when this

## 17595:00 - 17625:00

happens and this happens to all the

## 17625:00 - 17660:00

time. I guess one more thing I would

## 17660:00 - 17705:00

point to is security kind of related

## 17705:00 - 17735:00

limitations of the use of LLM. So for

## 17735:00 - 17770:00

example, LLMs are quite gullible. Uh

## 17770:00 - 17800:00

they are susceptible to prompt injection

## 17800:00 - 17845:00

risks. They might leak your data etc.

## 17845:00 - 17875:00

And so um and there's many other

## 17875:00 - 17920:00

considerations uh security related. So,

## 17920:00 - 17955:00

so basically long story short, you have

## 17955:00 - 18000:00

to load your you have to load your you

## 18000:00 - 18020:00

have to simultaneously think through

## 18020:00 - 18050:00

this superhuman thing that has a bunch

## 18050:00 - 18090:00

of cognitive deficits and issues. How do

## 18090:00 - 18125:00

we and yet they are extremely like

## 18125:00 - 18175:00

useful and so how do we program them and

## 18175:00 - 18205:00

how do we work around their deficits and

## 18205:00 - 18260:00

enjoy their superhuman powers.

## 18260:00 - 18290:00

So what I want to switch to now is talk

## 18290:00 - 18315:00

about the opportunities of how do we use

## 18315:00 - 18345:00

these models and what are some of the

## 18345:00 - 18370:00

biggest opportunities. This is not a

## 18370:00 - 18390:00

comprehensive list just some of the

## 18390:00 - 18410:00

things that I thought were interesting

## 18410:00 - 18445:00

for this talk. The first thing I'm kind

## 18445:00 - 18485:00

of excited about is what I would call

## 18485:00 - 18535:00

partial autonomy apps. So for example,

## 18535:00 - 18570:00

let's work with the example of coding.

## 18570:00 - 18605:00

You can certainly go to chacht directly

## 18605:00 - 18630:00

and you can start copy pasting code

## 18630:00 - 18680:00

around and copyping bug reports and

## 18680:00 - 18705:00

stuff around and getting code and copy

## 18705:00 - 18735:00

pasting everything around. Why would you

## 18735:00 - 18755:00

why would you do that? Why would you go

## 18755:00 - 18785:00

directly to the operating system? It

## 18785:00 - 18805:00

makes a lot more sense to have an app

## 18805:00 - 18845:00

dedicated for this. And so I think many

## 18845:00 - 18895:00

of you uh use uh cursor. I do as well.

## 18895:00 - 18935:00

And uh cursor is kind of like the thing

## 18935:00 - 18960:00

you want instead. You don't want to just

## 18960:00 - 18995:00

directly go to the chash apt. And I

## 18995:00 - 19020:00

think cursor is a very good example of

## 19020:00 - 19060:00

an early LLM app that has a bunch of

## 19060:00 - 19100:00

properties that I think are um useful

## 19100:00 - 19130:00

across all the LLM apps. So in

## 19130:00 - 19160:00

particular, you will notice that we have

## 19160:00 - 19200:00

a traditional interface that allows a

## 19200:00 - 19230:00

human to go in and do all the work

## 19230:00 - 19270:00

manually just as before. But in addition

## 19270:00 - 19295:00

to that, we now have this LLM

## 19295:00 - 19320:00

integration that allows us to go in

## 19320:00 - 19365:00

bigger chunks. And so some of the

## 19365:00 - 19390:00

properties of LLM apps that I think are

## 19390:00 - 19430:00

shared and useful to point out. Number

## 19430:00 - 19465:00

one, the LLMs basically do a ton of the

## 19465:00 - 19520:00

context management. Um, number two, they

## 19520:00 - 19550:00

orchestrate multiple calls to LLMs,

## 19550:00 - 19580:00

right? So in the case of cursor, there's

## 19580:00 - 19615:00

under the hood embedding models for all

## 19615:00 - 19650:00

your files, the actual chat models,

## 19650:00 - 19695:00

models that apply diffs to the code, and

## 19695:00 - 19730:00

this is all orchestrated for you. A

## 19730:00 - 19765:00

really big one that uh I think also

## 19765:00 - 19805:00

maybe not fully appreciated always is

## 19805:00 - 19840:00

application specific uh GUI and the

## 19840:00 - 19885:00

importance of it. Um because you don't

## 19885:00 - 19905:00

just want to talk to the operating

## 19905:00 - 19940:00

system directly in text. Text is very

## 19940:00 - 19980:00

hard to read, interpret, understand and

## 19980:00 - 20005:00

also like you don't want to take some of

## 20005:00 - 20050:00

these actions natively in text. So it's

## 20050:00 - 20080:00

much better to just see a diff as like

## 20080:00 - 20110:00

red and green change and you can see

## 20110:00 - 20140:00

what's being added is subtracted. It's

## 20140:00 - 20170:00

much easier to just do command Y to

## 20170:00 - 20195:00

accept or command N to reject. I

## 20195:00 - 20215:00

shouldn't have to type it in text,

## 20215:00 - 20255:00

right? So, a guey allows a human to

## 20255:00 - 20295:00

audit the work of these fallible systems

## 20295:00 - 20330:00

and to go faster. I'm going to come back

## 20330:00 - 20360:00

to this point a little bit uh later as

## 20360:00 - 20395:00

well. And the last kind of feature I

## 20395:00 - 20420:00

want to point out is that there's what I

## 20420:00 - 20460:00

call the autonomy slider. So, for

## 20460:00 - 20490:00

example, in cursor, you can just do tap

## 20490:00 - 20525:00

completion. You're mostly in charge. You

## 20525:00 - 20560:00

can select a chunk of code and command K

## 20560:00 - 20600:00

to change just that chunk of code. You

## 20600:00 - 20630:00

can do command L to change the entire

## 20630:00 - 20670:00

file. Or you can do command I which just

## 20670:00 - 20700:00

you know let it rip do whatever you want

## 20700:00 - 20730:00

in the entire repo and that's the sort

## 20730:00 - 20770:00

of full autonomy agent agentic version

## 20770:00 - 20805:00

and so you are in charge of the autonomy

## 20805:00 - 20835:00

slider and depending on the complexity

## 20835:00 - 20880:00

of the task at hand you can uh tune the

## 20880:00 - 20905:00

amount of autonomy that you're willing

## 20905:00 - 20950:00

to give up uh for that task maybe to

## 20950:00 - 20975:00

show one more example of a fairly

## 20975:00 - 21050:00

successful LLM app uh perplexity um it

## 21050:00 - 21075:00

also has very similar features to what

## 21075:00 - 21120:00

I've just pointed out to in cursor uh it

## 21120:00 - 21145:00

packages up a lot of the information. It

## 21145:00 - 21180:00

orchestrates multiple LLMs. It's got a

## 21180:00 - 21220:00

GUI that allows you to audit some of its

## 21220:00 - 21260:00

work. So, for example, it will site

## 21260:00 - 21285:00

sources and you can imagine inspecting

## 21285:00 - 21315:00

them. And it's got an autonomy slider.

## 21315:00 - 21340:00

You can either just do a quick search or

## 21340:00 - 21370:00

you can do research or you can do deep

## 21370:00 - 21405:00

research and come back 10 minutes later.

## 21405:00 - 21425:00

So, this is all just varying levels of

## 21425:00 - 21460:00

autonomy that you give up to the tool.

## 21460:00 - 21500:00

So, I guess my question is I feel like a

## 21500:00 - 21530:00

lot of software will become partially

## 21530:00 - 21555:00

autonomous. I'm trying to think through

## 21555:00 - 21585:00

like what does that look like? And for

## 21585:00 - 21615:00

many of you who maintain products and

## 21615:00 - 21645:00

services, how are you going to make your

## 21645:00 - 21670:00

products and services partially

## 21670:00 - 21710:00

autonomous? Can an LLM see everything

## 21710:00 - 21750:00

that a human can see? Can an LLM act in

## 21750:00 - 21780:00

all the ways that a human could act? And

## 21780:00 - 21820:00

can humans supervise and stay in the

## 21820:00 - 21845:00

loop of this activity? Because again,

## 21845:00 - 21870:00

these are fallible systems that aren't

## 21870:00 - 21910:00

yet perfect. And what does a diff look

## 21910:00 - 21940:00

like in Photoshop or something like

## 21940:00 - 21975:00

that? You know, and also a lot of the

## 21975:00 - 22000:00

traditional software right now, it has

## 22000:00 - 22030:00

all these switches and all this kind of

## 22030:00 - 22055:00

stuff that's all designed for human. All

## 22055:00 - 22075:00

of this has to change and become

## 22075:00 - 22125:00

accessible to LLMs.

## 22125:00 - 22155:00

So, one thing I want to stress with a

## 22155:00 - 22185:00

lot of these LLM apps that I'm not sure

## 22185:00 - 22235:00

gets as much attention as it should is

## 22235:00 - 22275:00

um we we're now kind of like cooperating

## 22275:00 - 22310:00

with AIS and usually they are doing the

## 22310:00 - 22335:00

generation and we as humans are doing

## 22335:00 - 22375:00

the verification. It is in our interest

## 22375:00 - 22405:00

to make this loop go as fast as

## 22405:00 - 22425:00

possible. So, we're getting a lot of

## 22425:00 - 22465:00

work done. There are two major ways that

## 22465:00 - 22505:00

I think uh this can be done. Number one,

## 22505:00 - 22545:00

you can speed up verification a lot. Um,

## 22545:00 - 22570:00

and I think guies, for example, are

## 22570:00 - 22600:00

extremely important to this because a

## 22600:00 - 22650:00

guey utilizes your computer vision GPU

## 22650:00 - 22685:00

in all of our head. Reading text is

## 22685:00 - 22720:00

effortful and it's not fun, but looking

## 22720:00 - 22760:00

at stuff is fun and it's it's just a

## 22760:00 - 22790:00

kind of like a highway to your brain.

## 22790:00 - 22825:00

So, I think guies are very useful for

## 22825:00 - 22860:00

auditing systems and visual

## 22860:00 - 22890:00

representations in general. And number

## 22890:00 - 22930:00

two, I would say is we have to keep the

## 22930:00 - 22980:00

AI on the leash. We I think a lot of

## 22980:00 - 23010:00

people are getting way over excited with

## 23010:00 - 23060:00

AI agents and uh it's not useful to me

## 23060:00 - 23095:00

to get a diff of 10,000 lines of code to

## 23095:00 - 23130:00

my repo. Like I have to I'm still the

## 23130:00 - 23150:00

bottleneck, right? Even though that

## 23150:00 - 23185:00

10,00 lines come out instantly, I have

## 23185:00 - 23200:00

to make sure that this thing is not

## 23200:00 - 23255:00

introducing bugs. It's just like and

## 23255:00 - 23275:00

that it's doing the correct thing,

## 23275:00 - 23295:00

right? And that there's no security

## 23295:00 - 23380:00

issues and so on. So um I think that um

## 23380:00 - 23420:00

yeah basically you we have to sort of

## 23420:00 - 23470:00

like it's in our interest to make the

## 23470:00 - 23505:00

the flow of these two go very very fast

## 23505:00 - 23535:00

and we have to somehow keep the AI on

## 23535:00 - 23550:00

the leash because it gets way too

## 23550:00 - 23585:00

overreactive. It's uh it's kind of like

## 23585:00 - 23620:00

this. This is how I feel when I do AI

## 23620:00 - 23650:00

assisted coding. If I'm just bite coding

## 23650:00 - 23680:00

everything is nice and great but if I'm

## 23680:00 - 23705:00

actually trying to get work done it's

## 23705:00 - 23745:00

not so great to have an overreactive uh

## 23745:00 - 23785:00

agent doing all this kind of stuff. So

## 23785:00 - 23810:00

this slide is not very good. I'm sorry,

## 23810:00 - 23850:00

but I guess I'm trying to develop like

## 23850:00 - 23895:00

many of you some ways of utilizing these

## 23895:00 - 23925:00

agents in my coding workflow and to do

## 23925:00 - 23965:00

AI assisted coding. And in my own work,

## 23965:00 - 23995:00

I'm always scared to get way too big

## 23995:00 - 24035:00

diffs. I always go in small incremental

## 24035:00 - 24065:00

chunks. I want to make sure that

## 24065:00 - 24100:00

everything is good. I want to spin this

## 24100:00 - 24150:00

loop very very fast and um I sort of

## 24150:00 - 24175:00

work on small chunks of single concrete

## 24175:00 - 24220:00

thing. Uh and so I think many of you

## 24220:00 - 24240:00

probably are developing similar ways of

## 24240:00 - 24290:00

working with the with LLMs.

## 24290:00 - 24325:00

Um, I also saw a number of blog posts

## 24325:00 - 24370:00

that try to develop these best practices

## 24370:00 - 24400:00

for working with LLMs. And here's one

## 24400:00 - 24420:00

that I read recently and I thought was

## 24420:00 - 24445:00

quite good. And it kind of discussed

## 24445:00 - 24470:00

some techniques and some of them have to

## 24470:00 - 24495:00

do with how you keep the AI on the

## 24495:00 - 24530:00

leash. And so, as an example, if you are

## 24530:00 - 24580:00

prompting, if your prompt is vague, then

## 24580:00 - 24615:00

uh the AI might not do exactly what you

## 24615:00 - 24645:00

wanted and in that case, verification

## 24645:00 - 24670:00

will fail. You're going to ask for

## 24670:00 - 24700:00

something else. If a verification fails,

## 24700:00 - 24725:00

then you're going to start spinning. So

## 24725:00 - 24750:00

it makes a lot more sense to spend a bit

## 24750:00 - 24775:00

more time to be more concrete in your

## 24775:00 - 24805:00

prompts which increases the probability

## 24805:00 - 24835:00

of successful verification and you can

## 24835:00 - 24865:00

move forward. And so I think a lot of us

## 24865:00 - 24900:00

are going to end up finding um kind of

## 24900:00 - 24935:00

techniques like this. I think in my own

## 24935:00 - 24960:00

work as well I'm currently interested in

## 24960:00 - 25000:00

uh what education looks like in um

## 25000:00 - 25030:00

together with kind of like now that we

## 25030:00 - 25070:00

have AI uh and LLMs what does education

## 25070:00 - 25115:00

look like? And I think a a large amount

## 25115:00 - 25160:00

of thought for me goes into how we keep

## 25160:00 - 25190:00

AI on the leash. I don't think it just

## 25190:00 - 25220:00

works to go to chat and be like, "Hey,

## 25220:00 - 25245:00

teach me physics." I don't think this

## 25245:00 - 25280:00

works because the AI is like gets lost

## 25280:00 - 25310:00

in the woods. And so for me, this is

## 25310:00 - 25345:00

actually two separate apps. For example,

## 25345:00 - 25375:00

there's an app for a teacher that

## 25375:00 - 25410:00

creates courses and then there's an app

## 25410:00 - 25440:00

that takes courses and serves them to

## 25440:00 - 25485:00

students. And in both cases, we now have

## 25485:00 - 25520:00

this intermediate artifact of a course

## 25520:00 - 25545:00

that is auditable and we can make sure

## 25545:00 - 25560:00

it's good. We can make sure it's

## 25560:00 - 25595:00

consistent. and the AI is kept on the

## 25595:00 - 25615:00

leash with respect to a certain

## 25615:00 - 25670:00

syllabus, a certain like um progression

## 25670:00 - 25710:00

of projects and so on. And so this is

## 25710:00 - 25735:00

one way of keeping the AI on leash and I

## 25735:00 - 25760:00

think has a much higher likelihood of

## 25760:00 - 25795:00

working and the AI is not getting lost

## 25795:00 - 25830:00

in the woods.

## 25830:00 - 25865:00

One more kind of analogy I wanted to

## 25865:00 - 25905:00

sort of allude to is I'm not I'm no

## 25905:00 - 25935:00

stranger to partial autonomy and I kind

## 25935:00 - 25960:00

of worked on this I think for five years

## 25960:00 - 26000:00

at Tesla and this is also a partial

## 26000:00 - 26030:00

autonomy product and shares a lot of the

## 26030:00 - 26055:00

features like for example right there in

## 26055:00 - 26090:00

the instrument panel is the GUI of the

## 26090:00 - 26125:00

autopilot so it's showing me what the

## 26125:00 - 26150:00

what the neural network sees and so on

## 26150:00 - 26175:00

and we have the autonomy slider where

## 26175:00 - 26220:00

over the course of my tenure there we

## 26220:00 - 26260:00

did more and more autonomous tasks for

## 26260:00 - 26305:00

the user and maybe the story that I

## 26305:00 - 26350:00

wanted to tell very briefly is uh

## 26350:00 - 26375:00

actually the first time I drove a

## 26375:00 - 26420:00

self-driving vehicle was in 2013 and I

## 26420:00 - 26450:00

had a friend who worked at Whimo and uh

## 26450:00 - 26485:00

he offered to give me a drive around

## 26485:00 - 26525:00

Palo Alto. I took this picture using

## 26525:00 - 26565:00

Google Glass at the time and many of you

## 26565:00 - 26585:00

are so young that you might not even

## 26585:00 - 26620:00

know what that is. Uh but uh yeah, this

## 26620:00 - 26655:00

was like all the rage at the time. And

## 26655:00 - 26680:00

we got into this car and we went for

## 26680:00 - 26715:00

about a 30-minute drive around Palo Alto

## 26715:00 - 26750:00

highways uh streets and so on. And this

## 26750:00 - 26780:00

drive was perfect. There was zero

## 26780:00 - 26830:00

interventions and this was 2013 which is

## 26830:00 - 26870:00

now 12 years ago. And it kind of struck

## 26870:00 - 26900:00

me because at the time when I had this

## 26900:00 - 26935:00

perfect drive, this perfect demo, I felt

## 26935:00 - 26990:00

like, wow, self-driving is imminent

## 26990:00 - 27010:00

because this just worked. This is

## 27010:00 - 27055:00

incredible. Um, but here we are 12 years

## 27055:00 - 27080:00

later and we are still working on

## 27080:00 - 27115:00

autonomy. Um, we are still working on

## 27115:00 - 27150:00

driving agents and even now we haven't

## 27150:00 - 27175:00

actually like really solved the problem.

## 27175:00 - 27210:00

like you may see Whimos going around and

## 27210:00 - 27245:00

they look driverless but you know

## 27245:00 - 27275:00

there's still a lot of teleoperation and

## 27275:00 - 27310:00

a lot of human in the loop of a lot of

## 27310:00 - 27345:00

this driving so we still haven't even

## 27345:00 - 27375:00

like declared success but I think it's

## 27375:00 - 27405:00

definitely like going to succeed at this

## 27405:00 - 27440:00

point but it just took a long time and

## 27440:00 - 27485:00

so I think like like this is software is

## 27485:00 - 27525:00

really tricky I think in the same way

## 27525:00 - 27575:00

that driving is tricky and so when I see

## 27575:00 - 27605:00

things like oh 2025 is the year of

## 27605:00 - 27645:00

agents I get very concerned and I kind

## 27645:00 - 27680:00

of feel like you know this is the decade

## 27680:00 - 27730:00

of agents and this is going to be quite

## 27730:00 - 27760:00

some time. We need humans in the loop.

## 27760:00 - 27785:00

We need to do this carefully. This is

## 27785:00 - 27850:00

software. Let's be serious here. One

## 27850:00 - 27880:00

more kind of analogy that I always think

## 27880:00 - 27930:00

through is the Iron Man suit. Uh I think

## 27930:00 - 27965:00

this is I always love Iron Man. I think

## 27965:00 - 28020:00

it's like so um correct in a bunch of

## 28020:00 - 28045:00

ways with respect to technology and how

## 28045:00 - 28070:00

it will play out. And what I love about

## 28070:00 - 28095:00

the Iron Man suit is that it's both an

## 28095:00 - 28145:00

augmentation and Tony Stark can drive it

## 28145:00 - 28170:00

and it's also an agent. And in some of

## 28170:00 - 28195:00

the movies, the Iron Man suit is quite

## 28195:00 - 28225:00

autonomous and can fly around and find

## 28225:00 - 28250:00

Tony and all this kind of stuff. And so

## 28250:00 - 28285:00

this is the autonomy slider is we can be

## 28285:00 - 28315:00

we can build augmentations or we can

## 28315:00 - 28350:00

build agents and we kind of want to do a

## 28350:00 - 28390:00

bit of both. But at this stage I would

## 28390:00 - 28430:00

say working with fallible LLMs and so

## 28430:00 - 28485:00

on. I would say you know it's less Iron

## 28485:00 - 28525:00

Man robots and more Iron Man suits that

## 28525:00 - 28560:00

you want to build. It's less like

## 28560:00 - 28585:00

building flashy demos of autonomous

## 28585:00 - 28610:00

agents and more building partial

## 28610:00 - 28660:00

autonomy products. And these products

## 28660:00 - 28695:00

have custom gueies and UIUX. And we're

## 28695:00 - 28730:00

trying to um and this is done so that

## 28730:00 - 28755:00

the generation verification loop of the

## 28755:00 - 28800:00

human is very very fast. But we are not

## 28800:00 - 28825:00

losing the sight of the fact that it is

## 28825:00 - 28850:00

in principle possible to automate this

## 28850:00 - 28880:00

work. And there should be an autonomy

## 28880:00 - 28905:00

slider in your product. And you should

## 28905:00 - 28930:00

be thinking about how you can slide that

## 28930:00 - 28975:00

autonomy slider and make your product uh

## 28975:00 - 29020:00

sort of um more autonomous over time.

## 29020:00 - 29045:00

But this is kind of how I think there's

## 29045:00 - 29070:00

lots of opportunities in these kinds of

## 29070:00 - 29105:00

products. I want to now switch gears a

## 29105:00 - 29135:00

little bit and talk about one other

## 29135:00 - 29160:00

dimension that I think is very unique.

## 29160:00 - 29190:00

Not only is there a new type of

## 29190:00 - 29215:00

programming language that allows for

## 29215:00 - 29250:00

autonomy in software but also as I

## 29250:00 - 29275:00

mentioned it's programmed in English

## 29275:00 - 29315:00

which is this natural interface and

## 29315:00 - 29340:00

suddenly everyone is a programmer

## 29340:00 - 29370:00

because everyone speaks natural language

## 29370:00 - 29410:00

like English. So this is extremely

## 29410:00 - 29435:00

bullish and very interesting to me and

## 29435:00 - 29465:00

also completely unprecedented. I would

## 29465:00 - 29490:00

say it it used to be the case that you

## 29490:00 - 29520:00

need to spend five to 10 years studying

## 29520:00 - 29545:00

something to be able to do something in

## 29545:00 - 29585:00

software. this is not the case anymore.

## 29585:00 - 29615:00

So, I don't know if by any chance anyone

## 29615:00 - 29675:00

has heard of vibe coding.

## 29675:00 - 29705:00

Uh, this this is the tweet that kind of

## 29705:00 - 29735:00

like introduced this, but I'm told that

## 29735:00 - 29775:00

this is now like a major meme. Um, fun

## 29775:00 - 29825:00

story about this is that I've been on

## 29825:00 - 29850:00

Twitter for like 15 years or something

## 29850:00 - 29890:00

like that at this point and I still have

## 29890:00 - 29935:00

no clue which tweet will become viral

## 29935:00 - 29965:00

and which tweet like fizzles and no one

## 29965:00 - 30010:00

cares. And I thought that this tweet was

## 30010:00 - 30030:00

going to be the latter. I don't know. It

## 30030:00 - 30055:00

was just like a shower of thoughts. But

## 30055:00 - 30085:00

this became like a total meme and I

## 30085:00 - 30110:00

really just can't tell. But I guess like

## 30110:00 - 30140:00

it struck a chord and it gave a name to

## 30140:00 - 30175:00

something that everyone was feeling but

## 30175:00 - 30220:00

couldn't quite say in words. So now

## 30220:00 - 30285:00

there's a Wikipedia page and everything.

## 30285:00 - 30310:00

This is like

## 30310:00 - 30430:00

[Applause]

## 30430:00 - 30460:00

yeah this is like a major contribution

## 30460:00 - 30510:00

now or something like that. So,

## 30510:00 - 30545:00

um, so Tom Wolf from HuggingFace shared

## 30545:00 - 30580:00

this beautiful video that I really love.

## 30580:00 - 30625:00

Um,

## 30625:00 - 30710:00

these are kids vibe coding.

## 30710:00 - 30735:00

And I find that this is such a wholesome

## 30735:00 - 30775:00

video. Like, I love this video. Like,

## 30775:00 - 30800:00

how can you look at this video and feel

## 30800:00 - 30830:00

bad about the future? The future is

## 30830:00 - 30875:00

great.

## 30875:00 - 30895:00

I think this will end up being like a

## 30895:00 - 30940:00

gateway drug to software development.

## 30940:00 - 30985:00

Um, I'm not a doomer about the future of

## 30985:00 - 31035:00

the generation and I think yeah, I love

## 31035:00 - 31075:00

this video. So, I tried by coding a

## 31075:00 - 31115:00

little bit uh as well because it's so

## 31115:00 - 31155:00

fun. Uh, so bike coding is so great when

## 31155:00 - 31175:00

you want to build something super duper

## 31175:00 - 31205:00

custom that doesn't appear to exist and

## 31205:00 - 31225:00

you just want to wing it because it's a

## 31225:00 - 31255:00

Saturday or something like that. So, I

## 31255:00 - 31310:00

built this uh iOS app and I don't I

## 31310:00 - 31340:00

can't actually program in Swift, but I

## 31340:00 - 31360:00

was really shocked that I was able to

## 31360:00 - 31385:00

build like a super basic app and I'm not

## 31385:00 - 31410:00

going to explain it. It's really uh

## 31410:00 - 31455:00

dumb, but uh I kind of like this was

## 31455:00 - 31475:00

just like a day of work and this was

## 31475:00 - 31505:00

running on my phone like later that day

## 31505:00 - 31535:00

and I was like, "Wow, this is amazing."

## 31535:00 - 31565:00

I didn't have to like read through Swift

## 31565:00 - 31595:00

for like five days or something like

## 31595:00 - 31635:00

that to like get started. I also

## 31635:00 - 31670:00

vipcoded this app called Menu Genen. And

## 31670:00 - 31695:00

this is live. You can try it in

## 31695:00 - 31730:00

menu.app. And I basically had this

## 31730:00 - 31755:00

problem where I show up at a restaurant,

## 31755:00 - 31775:00

I read through the menu, and I have no

## 31775:00 - 31805:00

idea what any of the things are. And I

## 31805:00 - 31860:00

need pictures. So this doesn't exist. So

## 31860:00 - 31880:00

I was like, "Hey, I'm going to bite code

## 31880:00 - 31930:00

it." So, um, this is what it looks like.

## 31930:00 - 31970:00

You go to menu.app,

## 31970:00 - 32020:00

um, and, uh, you take a picture of a of

## 32020:00 - 32050:00

a menu and then menu generates the

## 32050:00 - 32100:00

images and everyone gets $5 in credits

## 32100:00 - 32130:00

for free when you sign up. And

## 32130:00 - 32170:00

therefore, this is a major cost center

## 32170:00 - 32225:00

in my life. So, this is a negative

## 32225:00 - 32270:00

negative uh, revenue app for me right

## 32270:00 - 32295:00

now.

## 32295:00 - 32320:00

I've lost a huge amount of money on

## 32320:00 - 32350:00

menu.

## 32350:00 - 32385:00

Okay. But the fascinating thing about

## 32385:00 - 32465:00

menu genen for me is that the code of

## 32465:00 - 32500:00

the v the vite coding part the code was

## 32500:00 - 32545:00

actually the easy part of v of v coding

## 32545:00 - 32585:00

menu and most of it actually was when I

## 32585:00 - 32605:00

tried to make it real so that you can

## 32605:00 - 32625:00

actually have authentication and

## 32625:00 - 32660:00

payments and the domain name and averal

## 32660:00 - 32695:00

deployment. This was really hard and all

## 32695:00 - 32735:00

of this was not code. All of this devops

## 32735:00 - 32785:00

stuff was in me in the browser clicking

## 32785:00 - 32830:00

stuff and this was extreme slo and took

## 32830:00 - 32855:00

another week. So it was really

## 32855:00 - 32910:00

fascinating that I had the menu genen um

## 32910:00 - 32950:00

basically demo working on my laptop in a

## 32950:00 - 32985:00

few hours and then it took me a week

## 32985:00 - 33020:00

because I was trying to make it real and

## 33020:00 - 33045:00

the reason for this is this was just

## 33045:00 - 33090:00

really annoying. Um, so for example, if

## 33090:00 - 33120:00

you try to add Google login to your web

## 33120:00 - 33150:00

page, I know this is very small, but

## 33150:00 - 33190:00

just a huge amount of instructions of

## 33190:00 - 33225:00

this clerk library telling me how to

## 33225:00 - 33250:00

integrate this. And this is crazy. Like

## 33250:00 - 33290:00

it's telling me go to this URL, click on

## 33290:00 - 33325:00

this dropdown, choose this, go to this,

## 33325:00 - 33350:00

and click on that. And it's like telling

## 33350:00 - 33375:00

me what to do. Like a computer is

## 33375:00 - 33410:00

telling me the actions I should be

## 33410:00 - 33440:00

taking. Like you do it. Why am I doing

## 33440:00 - 33475:00

this?

## 33475:00 - 33525:00

What the hell?

## 33525:00 - 33560:00

I had to follow all these instructions.

## 33560:00 - 33600:00

This was crazy. So I think the last part

## 33600:00 - 33655:00

of my talk therefore focuses on can we

## 33655:00 - 33690:00

just build for agents? I don't want to

## 33690:00 - 33735:00

do this work. Can agents do this? Thank

## 33735:00 - 33770:00

you.

## 33770:00 - 33810:00

Okay. So roughly speaking, I think

## 33810:00 - 33845:00

there's a new category of consumer and

## 33845:00 - 33885:00

manipulator of digital information. It

## 33885:00 - 33920:00

used to be just humans through GUIs or

## 33920:00 - 33955:00

computers through APIs. And now we have

## 33955:00 - 34000:00

a completely new thing and agents are

## 34000:00 - 34045:00

they're computers but they are humanlike

## 34045:00 - 34070:00

kind of right they're people spirits

## 34070:00 - 34090:00

there's people spirits on the internet

## 34090:00 - 34110:00

and they need to interact with our

## 34110:00 - 34135:00

software infrastructure like can we

## 34135:00 - 34175:00

build for them it's a new thing so as an

## 34175:00 - 34215:00

example you can have robots.txt on your

## 34215:00 - 34250:00

domain and you can instruct uh or like

## 34250:00 - 34305:00

advise I suppose um uh web crawlers on

## 34305:00 - 34330:00

how to behave on your website in the

## 34330:00 - 34355:00

same way you can have maybe lm.txt txt

## 34355:00 - 34385:00

file which is just a simple markdown

## 34385:00 - 34425:00

that's telling LLMs what this domain is

## 34425:00 - 34465:00

about and this is very readable to a to

## 34465:00 - 34505:00

an LLM. If it had to instead get the

## 34505:00 - 34540:00

HTML of your web page and try to parse

## 34540:00 - 34560:00

it, this is very errorprone and

## 34560:00 - 34590:00

difficult and will screw it up and it's

## 34590:00 - 34610:00

not going to work. So we can just

## 34610:00 - 34635:00

directly speak to the LLM. It's worth

## 34635:00 - 34685:00

it. Um a huge amount of documentation is

## 34685:00 - 34710:00

currently written for people. So you

## 34710:00 - 34755:00

will see things like lists and bold and

## 34755:00 - 34795:00

pictures and this is not directly

## 34795:00 - 34850:00

accessible by an LLM. So I see some of

## 34850:00 - 34880:00

the services now are transitioning a lot

## 34880:00 - 34910:00

of the their docs to be specifically for

## 34910:00 - 34950:00

LLMs. So Versell and Stripe as an

## 34950:00 - 34990:00

example are early movers here but there

## 34990:00 - 35030:00

are a few more that I've seen already

## 35030:00 - 35065:00

and they offer their documentation in

## 35065:00 - 35110:00

markdown. Markdown is super easy for LMS

## 35110:00 - 35165:00

to understand. This is great. Um maybe

## 35165:00 - 35205:00

one simple example from from uh my

## 35205:00 - 35230:00

experience as well. Maybe some of you

## 35230:00 - 35255:00

know three blue one brown. He makes

## 35255:00 - 35320:00

beautiful animation videos on YouTube.

## 35320:00 - 35385:00

[Applause]

## 35385:00 - 35415:00

Yeah, I love this library. So that he

## 35415:00 - 35455:00

wrote uh Manon and I wanted to make my

## 35455:00 - 35500:00

own and uh there's extensive

## 35500:00 - 35540:00

documentations on how to use manon and

## 35540:00 - 35565:00

so I didn't want to actually read

## 35565:00 - 35585:00

through it. So I copy pasted the whole

## 35585:00 - 35620:00

thing to an LLM and I described what I

## 35620:00 - 35650:00

wanted and it just worked out of the box

## 35650:00 - 35690:00

like LLM just bcoded me an animation

## 35690:00 - 35720:00

exactly what I wanted and I was like wow

## 35720:00 - 35760:00

this is amazing. So if we can make docs

## 35760:00 - 35800:00

legible to LLMs, it's going to unlock a

## 35800:00 - 35850:00

huge amount of um kind of use and um I

## 35850:00 - 35870:00

think this is wonderful and should

## 35870:00 - 35915:00

should happen more. The other thing I

## 35915:00 - 35935:00

wanted to point out is that you do

## 35935:00 - 35960:00

unfortunately have to it's not just

## 35960:00 - 35980:00

about taking your docs and making them

## 35980:00 - 36010:00

appear in markdown. That's the easy

## 36010:00 - 36030:00

part. We actually have to change the

## 36030:00 - 36075:00

docs because anytime your docs say click

## 36075:00 - 36110:00

this is bad. An LLM will not be able to

## 36110:00 - 36165:00

natively take this action right now. So,

## 36165:00 - 36190:00

Verscell, for example, is replacing

## 36190:00 - 36225:00

every occurrence of click with an

## 36225:00 - 36255:00

equivalent curl command that your LM

## 36255:00 - 36300:00

agent could take on your behalf. Um, and

## 36300:00 - 36325:00

so I think this is very interesting. And

## 36325:00 - 36355:00

then, of course, there's a model context

## 36355:00 - 36380:00

protocol from Enthropic. And this is

## 36380:00 - 36410:00

also another way, it's a protocol of

## 36410:00 - 36445:00

speaking directly to agents as this new

## 36445:00 - 36465:00

consumer and manipulator of digital

## 36465:00 - 36490:00

information. So, I'm very bullish on

## 36490:00 - 36525:00

these ideas. The other thing I really

## 36525:00 - 36555:00

like is a number of little tools here

## 36555:00 - 36610:00

and there that are helping ingest data

## 36610:00 - 36645:00

that in like very LLM friendly formats.

## 36645:00 - 36665:00

So for example, when I go to a GitHub

## 36665:00 - 36710:00

repo like my nanoGPT repo, I can't feed

## 36710:00 - 36735:00

this to an LLM and ask questions about

## 36735:00 - 36775:00

it uh because it's you know this is a

## 36775:00 - 36810:00

human interface on GitHub. So when you

## 36810:00 - 36840:00

just change the URL from GitHub to get

## 36840:00 - 36870:00

ingest then uh this will actually

## 36870:00 - 36900:00

concatenate all the files into a single

## 36900:00 - 36930:00

giant text and it will create a

## 36930:00 - 36955:00

directory structure etc. And this is

## 36955:00 - 36980:00

ready to be copy pasted into your

## 36980:00 - 37025:00

favorite LLM and you can do stuff. Maybe

## 37025:00 - 37055:00

even more dramatic example of this is

## 37055:00 - 37090:00

deep wiki where it's not just the raw

## 37090:00 - 37140:00

content of these files. uh this is from

## 37140:00 - 37180:00

Devon but also like they have Devon

## 37180:00 - 37210:00

basically do analysis of the GitHub repo

## 37210:00 - 37240:00

and Devon basically builds up a whole

## 37240:00 - 37300:00

docs uh pages just for your repo and you

## 37300:00 - 37330:00

can imagine that this is even more

## 37330:00 - 37365:00

helpful to copy paste into your LLM. So

## 37365:00 - 37390:00

I love all the little tools that

## 37390:00 - 37415:00

basically where you just change the URL

## 37415:00 - 37440:00

and it makes something accessible to an

## 37440:00 - 37490:00

LLM. So this is all well and great and u

## 37490:00 - 37510:00

I think there should be a lot more of

## 37510:00 - 37545:00

it. One more note I wanted to make is

## 37545:00 - 37585:00

that it is absolutely possible that in

## 37585:00 - 37630:00

the future LLMs will be able to this is

## 37630:00 - 37655:00

not even future this is today they'll be

## 37655:00 - 37680:00

able to go around and they'll be able to

## 37680:00 - 37710:00

click stuff and so on but I still think

## 37710:00 - 37765:00

it's very worth u basically meeting LLM

## 37765:00 - 37805:00

halfway LLM's halfway and making it

## 37805:00 - 37830:00

easier for them to access all this

## 37830:00 - 37860:00

information uh because this is still

## 37860:00 - 37905:00

fairly expensive I would say to use and

## 37905:00 - 37940:00

uh a lot more difficult and so I do

## 37940:00 - 37970:00

think that lots of software there will

## 37970:00 - 38010:00

be a long tail where it won't like adapt

## 38010:00 - 38035:00

apps because these are not like live

## 38035:00 - 38070:00

player sort of repositories or digital

## 38070:00 - 38100:00

infrastructure and we will need these

## 38100:00 - 38140:00

tools. Uh but I think for everyone else

## 38140:00 - 38160:00

I think it's very worth kind of like

## 38160:00 - 38195:00

meeting in some middle point. So I'm

## 38195:00 - 38240:00

bullish on both if that makes sense.

## 38240:00 - 38285:00

So in summary, what an amazing time to

## 38285:00 - 38310:00

get into the industry. We need to

## 38310:00 - 38345:00

rewrite a ton of code. A ton of code

## 38345:00 - 38380:00

will be written by professionals and by

## 38380:00 - 38425:00

coders. These LLMs are kind of like

## 38425:00 - 38455:00

utilities, kind of like fabs, but

## 38455:00 - 38480:00

they're kind of especially like

## 38480:00 - 38515:00

operating systems. But it's so early.

## 38515:00 - 38570:00

It's like 1960s of operating systems and

## 38570:00 - 38600:00

uh and I think a lot of the analogies

## 38600:00 - 38645:00

cross over. Um and these LMS are kind of

## 38645:00 - 38690:00

like these fallible uh you know people

## 38690:00 - 38720:00

spirits that we have to learn to work

## 38720:00 - 38755:00

with. And in order to do that properly,

## 38755:00 - 38790:00

we need to adjust our infrastructure

## 38790:00 - 38815:00

towards it. So when you're building

## 38815:00 - 38840:00

these LLM apps, I describe some of the

## 38840:00 - 38880:00

ways of working effectively with these

## 38880:00 - 38910:00

LLMs and some of the tools that make

## 38910:00 - 38950:00

that uh kind of possible and how you can

## 38950:00 - 38980:00

spin this loop very very quickly and

## 38980:00 - 39010:00

basically create partial tunneling

## 39010:00 - 39055:00

products and then um yeah, a lot of code

## 39055:00 - 39080:00

has to also be written for the agents

## 39080:00 - 39120:00

more directly. But in any case, going

## 39120:00 - 39155:00

back to the Iron Man suit analogy, I

## 39155:00 - 39180:00

think what we'll see over the next

## 39180:00 - 39210:00

decade roughly is we're going to take

## 39210:00 - 39265:00

the slider from left to right. And I'm

## 39265:00 - 39290:00

very interesting. It's going to be very

## 39290:00 - 39320:00

interesting to see what that looks like.

## 39320:00 - 39355:00

And I can't wait to build it with all of

## 39355:00+

you. Thank you.

