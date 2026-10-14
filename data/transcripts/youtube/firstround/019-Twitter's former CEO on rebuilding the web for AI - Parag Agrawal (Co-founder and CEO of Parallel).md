---
source: https://www.youtube.com/watch?v=fORbmCMX5GA
title: Twitter's former CEO on rebuilding the web for AI | Parag Agrawal
  (Co-founder and CEO of Parallel)
author: First Round Capital
date: 2025-08-14
views: 68155
description: >-
  Parag Agrawal is the co-founder and CEO of Parallel, a startup building search
  infrastructure for the web’s second user: AIs. Before launching Parallel,
  Parag spent over a decade at Twitter, where he served as CTO and later CEO
  during a period of intense transformation, as well as public scrutiny.


  In this episode, Parag shares what he learned from his time at Twitter, why
  the web must evolve to serve AI at massive scale, how Parallel is tackling
  “deep research” challenges by prioritizing accuracy over speed, and the design
  choices that make their APIs uniquely agent-friendly. 


  We also discuss:

  • Why Parallel designs for AI as the primary customer

  • Lessons from 11 years at Twitter and applying them to a startup

  • Potential business models to keep the web open for AI

  • Hiring philosophy: balancing high potential and experienced talent

  • The evolving role of engineers in an AI-assisted world

  • Why “agents” are finally becoming useful in production

  • And much more…


  References:

  • Clay: https://www.clay.com/

  • Index Ventures: https://www.indexventures.com/

  • Josh Kopelman: https://www.linkedin.com/in/jkopelman/

  • KLA: https://www.kla.com/

  • OpenAI: https://openai.com/

  • Parallel: https://parallel.ai/

  • Patrick Collison: https://www.linkedin.com/in/patrickcollison/

  • Stripe: https://stripe.com/


  Where to find Parag:

  • LinkedIn: https://www.linkedin.com/in/paragagr/

  • X/Twitter: https://x.com/paraga


  Where to find Todd:

  • LinkedIn: https://www.linkedin.com/in/toddj0/

  • X/Twitter: https://x.com/tjack


  Where to find First Round Capital:

  • Website: https://firstround.com/

  • First Round Review: https://review.firstround.com/

  • X/Twitter: https://twitter.com/firstround

  • YouTube: https://www.youtube.com/@FirstRoundCapital

  • This podcast on all platforms: https://review.firstround.com/podcast


  Timestamps:

  (1:26) Founding Parallel with an AI-first mission

  (3:23) From Twitter CTO/CEO to startup founder

  (6:20) What the AI era spells for companies

  (7:58) The CEO to founder pipeline

  (11:18) Reflections on Twitter’s transformation

  (17:48) How Parallel was born

  (22:31) Early use cases for Parallel

  (31:42) How has Parallel’s ICP changed?

  (34:37) AI’s impact on competitor dynamics

  (36:06) When should founders launch?

  (37:43) Parag’s fundraising framework

  (40:14) Building a high-impact engineering team

  (44:49) Counterproductive uses of AI

  (47:35) How will the software engineer role evolve?

  (49:10) How are Parallel’s customers using AI?

  (53:27) Defining agents in 2025

  (55:02) Parallel’s long-term vision

  (1:03:43) Parag’s growth as a founder
tags:
  - startup
  - founder
  - first round
  - first round capital
  - in depth
  - parag agrawal
  - twitter
  - parallel
  - AI
  - product
  - engineering
  - tech
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:24:40.862Z
---

# Twitter's former CEO on rebuilding the web for AI | Parag Agrawal (Co-founder and CEO of Parallel)

## 00:00 - 30:00

I don't tend to enjoy public attention

## 30:00 - 70:00

too much. During the Twitter era, I

## 70:00 - 110:00

couldn't say very much. Now, I want to

## 110:00 - 150:00

harness public attention towards the

## 150:00 - 170:00

future I want to build.

## 170:00 - 205:00

>> Hey everyone, it's Todd Jackson. I'm a

## 205:00 - 230:00

partner at First Round. For today's

## 230:00 - 260:00

episode, I'm excited to sit down with

## 260:00 - 300:00

Parog Agarwal. He's the founder and CEO

## 300:00 - 335:00

of Parallel, an infrastructure startup

## 335:00 - 370:00

building a new web for AI agents.

## 370:00 - 425:00

>> We believe that AI is will use the web a

## 425:00 - 460:00

thousandx, a millionx, more than humans

## 460:00 - 495:00

ever have. I first met Parog when we

## 495:00 - 520:00

worked together back at Twitter, where

## 520:00 - 555:00

he spent over a decade rising from

## 555:00 - 610:00

engineer to CTO to CEO before selling

## 610:00 - 630:00

the company to Elon Musk.

## 630:00 - 660:00

>> I was entertaining some calls about

## 660:00 - 700:00

taking on jobs that might have on paper

## 700:00 - 740:00

felt like big jobs. I just couldn't join

## 740:00 - 750:00

a mission.

## 750:00 - 780:00

>> Now he's a founder building in the post

## 780:00 - 820:00

chat GPT era. In our conversation, we

## 820:00 - 850:00

dig into what he's learned from scaling

## 850:00 - 880:00

Twitter and leading it through its most

## 880:00 - 910:00

dramatic chapter, as well as what he's

## 910:00 - 955:00

had to unlearn as he builds parallel. We

## 955:00 - 990:00

also explore what is and isn't working

## 990:00 - 1030:00

in production, where agents are headed,

## 1030:00 - 1060:00

and why he believes the next generation

## 1060:00 - 1085:00

of the web will look fundamentally

## 1085:00 - 1095:00

different.

## 1095:00 - 1125:00

>> Our customer is an AI. We are going to

## 1125:00 - 1175:00

design an API that is excruciatingly

## 1175:00 - 1185:00

slow.

## 1185:00 - 1230:00

>> Let's dive in.

## 1230:00 - 1280:00

[Music]

## 1280:00 - 1290:00

>> Welcome to the show.

## 1290:00 - 1320:00

>> Thanks for having me. So, we're going to

## 1320:00 - 1345:00

dig into a bunch of different topics

## 1345:00 - 1375:00

today, but just to make sure everyone

## 1375:00 - 1415:00

has kind of the starting context. Could

## 1415:00 - 1445:00

you start by explaining at a high level

## 1445:00 - 1490:00

what your new company Parallel does? At

## 1490:00 - 1525:00

Parallel, we're obsessed with the open

## 1525:00 - 1590:00

web. We believe that AI is will use the

## 1590:00 - 1655:00

web a,000x, a millionx more than humans

## 1655:00 - 1720:00

ever have. And as a result, the web will

## 1720:00 - 1755:00

need to transform. In order to drive

## 1755:00 - 1795:00

that transformation, we've been building

## 1795:00 - 1855:00

the best tools that AIs can use to

## 1855:00 - 1905:00

access content in the web. In fact, like

## 1905:00 - 1960:00

the products we've shipped recently are

## 1960:00 - 2025:00

the only APIs that hit human and even

## 2025:00 - 2075:00

higher than human level performance on a

## 2075:00 - 2125:00

variety of deep research benchmarks.

## 2125:00 - 2155:00

And that's been a key milestones that

## 2155:00 - 2185:00

we've been working towards and we

## 2185:00 - 2220:00

finally hit. you were at Twitter for 11

## 2220:00 - 2270:00

years uh left in late 2022 and there was

## 2270:00 - 2300:00

just a little bit you know publicity

## 2300:00 - 2345:00

around that um starting parallel and

## 2345:00 - 2390:00

raised your seed round in 2024 and so

## 2390:00 - 2425:00

the company's still less than 18 months

## 2425:00 - 2450:00

old and you've been pretty quietly

## 2450:00 - 2480:00

building in stealth up until now is that

## 2480:00 - 2495:00

right

## 2495:00 - 2525:00

>> that's right and you know about our seed

## 2525:00 - 2560:00

round because you were with us through

## 2560:00 - 2610:00

that journey um we've been building away

## 2610:00 - 2670:00

we've had products out with customers

## 2670:00 - 2720:00

and we've been working with some of the

## 2720:00 - 2745:00

forwardlooking

## 2745:00 - 2800:00

customers whether they are private early

## 2800:00 - 2830:00

age companies or slightly more

## 2830:00 - 2865:00

established companies and it's been

## 2865:00 - 2900:00

amazing to work with a bunch of

## 2900:00 - 2935:00

customers who are ahead of the curve as

## 2935:00 - 2965:00

we see them and they've essentially

## 2965:00 - 3040:00

shaped us and our product and that's why

## 3040:00 - 3105:00

we've been quiet but now we think our

## 3105:00 - 3120:00

product is there

## 3120:00 - 3155:00

>> you and I actually met each other 10

## 3155:00 - 3190:00

years ago way back before that in 2014

## 3190:00 - 3235:00

at Twitter and one of the big projects

## 3235:00 - 3265:00

that we took on together was how to

## 3265:00 - 3305:00

introduce ranking into the home timeline

## 3305:00 - 3345:00

at Twitter which which was hard. Um, but

## 3345:00 - 3375:00

I bring that up because I think it's so

## 3375:00 - 3410:00

interesting to compare that to what you

## 3410:00 - 3455:00

are working on now because you spent

## 3455:00 - 3510:00

kind of a decade plus being responsible

## 3510:00 - 3555:00

for all these big atscale technical

## 3555:00 - 3585:00

decisions at Twitter dealing with all

## 3585:00 - 3610:00

the constraints of of 10-year-old

## 3610:00 - 3650:00

infrastructure and then you got this

## 3650:00 - 3700:00

opportunity to start completely fresh in

## 3700:00 - 3735:00

a you know in a post chat GBT world with

## 3735:00 - 3770:00

a clean sheet of paper. What was that

## 3770:00 - 3810:00

transition like for you when you're

## 3810:00 - 3865:00

working with a established product with

## 3865:00 - 3910:00

has product market fit like Twitter

## 3910:00 - 3965:00

versus 0 to1 journey? I think every way

## 3965:00 - 4005:00

of working to me feels different when

## 4005:00 - 4045:00

you're working with a team of 10 versus

## 4045:00 - 4085:00

a team of 8,000. Every practice you have

## 4085:00 - 4120:00

as a leader in my opinion must be

## 4120:00 - 4225:00

different when you're working in 2019

## 4225:00 - 4275:00

at Twitter with legacy infrastructure at

## 4275:00 - 4345:00

scale versus at a startup in 2025 with

## 4345:00 - 4410:00

20 people all in person. Everything you

## 4410:00 - 4460:00

get to do is different. So in some sense

## 4460:00 - 4495:00

this startup is like a journey in

## 4495:00 - 4520:00

unlearning everything I might have

## 4520:00 - 4550:00

learned before. So what are some what

## 4550:00 - 4575:00

are some examples of that? Like if you

## 4575:00 - 4600:00

think of and it could be you know the

## 4600:00 - 4640:00

pre-AII versus the post AI it could be

## 4640:00 - 4675:00

just the size the number of people it

## 4675:00 - 4695:00

could be sort of like incremental

## 4695:00 - 4725:00

changes on an existing thing versus a

## 4725:00 - 4745:00

brand new thing. What are some of the

## 4745:00 - 4785:00

sort of like specific ways? I think all

## 4785:00 - 4835:00

of it right like you think of team

## 4835:00 - 4885:00

Twitter was famously remote friendly

## 4885:00 - 4925:00

parallel we're all in person in one

## 4925:00 - 4980:00

office 5 days a week and I think you get

## 4980:00 - 5015:00

to do that at small scale. I think you

## 5015:00 - 5050:00

must do that at least I must do that for

## 5050:00 - 5105:00

who I am for this moment 0ero to1 if you

## 5105:00 - 5155:00

think of like preai versus post AI I

## 5155:00 - 5190:00

actually think you have to think about

## 5190:00 - 5240:00

product very differently at Twitter if

## 5240:00 - 5270:00

you ask for my framework or how to build

## 5270:00 - 5325:00

product it was like okay what do people

## 5325:00 - 5360:00

need what can be built you find

## 5360:00 - 5380:00

something in the intersection you try to

## 5380:00 - 5415:00

ship that right and you have to track

## 5415:00 - 5450:00

technology change at some rate in order

## 5450:00 - 5505:00

to find that constantly people need

## 5505:00 - 5545:00

everything with AI. So that's almost

## 5545:00 - 5590:00

obvious and now you all you really have

## 5590:00 - 5665:00

to zoom into what works and what can

## 5665:00 - 5725:00

work and where is it going and you have

## 5725:00 - 5770:00

to look sort of a step ahead and build

## 5770:00 - 5800:00

towards that and it's a very different

## 5800:00 - 5845:00

art like everything is now stoastic like

## 5845:00 - 5875:00

you build deterministic systems earlier

## 5875:00 - 5900:00

and now you're really thinking about

## 5900:00 - 5940:00

like building and communicating

## 5940:00 - 5985:00

stoastic systems so it's very very

## 5985:00 - 6010:00

different in my mind in terms of how you

## 6010:00 - 6030:00

think about

## 6030:00 - 6065:00

and systems that are getting better so

## 6065:00 - 6095:00

quickly like the leaps that are being

## 6095:00 - 6140:00

made every 6 months, 12 months is

## 6140:00 - 6180:00

amazing to me. But it's interesting when

## 6180:00 - 6205:00

it comes to the product like how do you

## 6205:00 - 6240:00

design the product in such a way to say

## 6240:00 - 6260:00

okay the models are where they are right

## 6260:00 - 6280:00

now but in 6 months they're going to be

## 6280:00 - 6315:00

much different and better. How does it

## 6315:00 - 6335:00

influence the way you think about like

## 6335:00 - 6370:00

thinking ahead on product? We've made

## 6370:00 - 6405:00

two opinionated stances when it relates

## 6405:00 - 6450:00

to that. One thing we did early on was

## 6450:00 - 6475:00

we took the counter approach of saying

## 6475:00 - 6515:00

our customer is an AI.

## 6515:00 - 6550:00

And one of the things that led us down

## 6550:00 - 6600:00

was we going to design an API that is

## 6600:00 - 6645:00

excruciatingly slow. Humans have no

## 6645:00 - 6670:00

patience on the web, right? Like when we

## 6670:00 - 6695:00

were building Twitter, we thought of

## 6695:00 - 6730:00

like okay, if you don't serve the

## 6730:00 - 6765:00

timeline within a second, you're going

## 6765:00 - 6790:00

to lose people. You can see it in your

## 6790:00 - 6810:00

numbers. You can see it in your metrics.

## 6810:00 - 6845:00

So you got to figure out how to do the

## 6845:00 - 6865:00

best thing possible in a second.

## 6865:00 - 6890:00

>> Performance is incredibly important when

## 6890:00 - 6915:00

the user is waiting. when users were

## 6915:00 - 6935:00

sitting there waiting for the query.

## 6935:00 - 6985:00

>> If it's an agent doing something in the

## 6985:00 - 7040:00

background, which could be running a

## 7040:00 - 7065:00

workflow when there's no human waiting

## 7065:00 - 7110:00

for it, or if it is someone trying to

## 7110:00 - 7145:00

collect a large number of data and fill

## 7145:00 - 7180:00

it into a database and you're doing

## 7180:00 - 7225:00

10,000 operations, a million operations,

## 7225:00 - 7255:00

the latency of each operation doesn't

## 7255:00 - 7305:00

matter. And if you relax that

## 7305:00 - 7350:00

constraint, you get to do more. Now

## 7350:00 - 7375:00

today we all call it deep research

## 7375:00 - 7405:00

because that's better branding than slow

## 7405:00 - 7445:00

in terms of agents are our customers. We

## 7445:00 - 7485:00

want to leap towards automating end to

## 7485:00 - 7530:00

end and so that helped us build

## 7530:00 - 7555:00

differently and we took a leap of faith

## 7555:00 - 7600:00

that it's going to happen even if the

## 7600:00 - 7645:00

models that day weren't good enough we

## 7645:00 - 7680:00

bet on models getting better to support

## 7680:00 - 7690:00

that.

## 7690:00 - 7720:00

>> So on top of all the things you know

## 7720:00 - 7745:00

that were that were happening at Twitter

## 7745:00 - 7775:00

and sort of setting the drama aside you

## 7775:00 - 7805:00

went through some very big what I would

## 7805:00 - 7850:00

call altitude shifts. um you know the

## 7850:00 - 7900:00

transition from CTO to CEO and I'm

## 7900:00 - 7930:00

curious just like what was that like for

## 7930:00 - 7955:00

you and and what did you learn from that

## 7955:00 - 7990:00

experience that that may have equipped

## 7990:00 - 8030:00

you to be a better founder in some ways?

## 8030:00 - 8065:00

One of the things when I was taking on

## 8065:00 - 8150:00

the CEO role was until then I really

## 8150:00 - 8210:00

thought of my job as being versatile to

## 8210:00 - 8270:00

the needs of the company and to shape

## 8270:00 - 8315:00

myself to be most effective which

## 8315:00 - 8340:00

doesn't mean that you don't get to

## 8340:00 - 8370:00

change the company around you but you

## 8370:00 - 8440:00

don't get to shape the company to you.

## 8440:00 - 8480:00

One of the big shifts I went through

## 8480:00 - 8550:00

taking on the CEO was I decided that the

## 8550:00 - 8575:00

most

## 8575:00 - 8610:00

productive way to operate would be to

## 8610:00 - 8660:00

shape the company around me. Take on the

## 8660:00 - 8690:00

founder role for the company because I

## 8690:00 - 8740:00

think there is no other way. If you try

## 8740:00 - 8775:00

to fit yourself to an organization, a

## 8775:00 - 8820:00

company, a plan that exists, I don't

## 8820:00 - 8870:00

think you do justice to the role. So

## 8870:00 - 8895:00

when I stepped in, I was like, I'm going

## 8895:00 - 8935:00

to shape the company to what I believe

## 8935:00 - 8990:00

and who I am. And that was a mindset I

## 8990:00 - 9050:00

took on taking in that role. And really

## 9050:00 - 9100:00

that manifested as me having the

## 9100:00 - 9145:00

conviction in that moment to change the

## 9145:00 - 9175:00

company, to change how Twitter did

## 9175:00 - 9215:00

things. I was there for a while.

## 9215:00 - 9245:00

>> You must have done that as the CTO as

## 9245:00 - 9270:00

well. I'm assuming you had you had so

## 9270:00 - 9290:00

much scope.

## 9290:00 - 9310:00

>> I don't think it's the same. I think

## 9310:00 - 9350:00

it's very very different. Like I think I

## 9350:00 - 9390:00

had a lot of agency and a lot of

## 9390:00 - 9425:00

influence

## 9425:00 - 9480:00

but I never perhaps it was my failing to

## 9480:00 - 9525:00

not embrace it to I can change anything

## 9525:00 - 9580:00

here. I tried and was often frustrated.

## 9580:00 - 9610:00

Right. So one of the things I did as

## 9610:00 - 9635:00

soon as I took the role is I think we

## 9635:00 - 9665:00

changed the structure of the company. We

## 9665:00 - 9685:00

changed the leadership team

## 9685:00 - 9720:00

substantially. Within a month I was

## 9720:00 - 9760:00

about to meaningfully change how many

## 9760:00 - 9790:00

people were at Twitter and what our road

## 9790:00 - 9835:00

map and priorities were. Now, we didn't

## 9835:00 - 9880:00

get a chance to see it all through, but

## 9880:00 - 9920:00

really I think it's really important. It

## 9920:00 - 9985:00

is different to embrace shaping

## 9985:00 - 10035:00

something to you versus shaping yourself

## 10035:00 - 10045:00

to something.

## 10045:00 - 10095:00

>> How did it feel to have so much public

## 10095:00 - 10145:00

attention trained on what was going on

## 10145:00 - 10170:00

inside the company? Like what what was

## 10170:00 - 10210:00

that experience like for you? And is

## 10210:00 - 10225:00

there anything that you kind of took

## 10225:00 - 10270:00

away from it? I don't tend to enjoy

## 10270:00 - 10300:00

public attention too much but I think

## 10300:00 - 10335:00

it's a very valuable thing like as a

## 10335:00 - 10380:00

founder now I actually think to drive

## 10380:00 - 10425:00

the impact I want to drive to shape the

## 10425:00 - 10460:00

world the way I want to shape it you

## 10460:00 - 10530:00

have to use public attention to find the

## 10530:00 - 10560:00

people who want to join you in your

## 10560:00 - 10605:00

mission to find customers and to

## 10605:00 - 10645:00

evangelize the future you want to live

## 10645:00 - 10680:00

in to find partners so in some sense

## 10680:00 - 10700:00

like public attention is really

## 10700:00 - 10725:00

important now what was unfortunate about

## 10725:00 - 10775:00

the public attention I did receive

## 10775:00 - 10830:00

during the the the Twitter era was that

## 10830:00 - 10880:00

in that moment I couldn't say very much

## 10880:00 - 10920:00

and in that moment I was going through

## 10920:00 - 10970:00

what felt like a zero sum game rather

## 10970:00 - 10995:00

than the current moment where it feels

## 10995:00 - 11040:00

like a extreme positive sum game. Now I

## 11040:00 - 11090:00

want to harness public attention towards

## 11090:00 - 11135:00

the future I want to build. But I didn't

## 11135:00 - 11155:00

get to do that then.

## 11155:00 - 11185:00

>> Yeah. I you know cuz I was sort of

## 11185:00 - 11215:00

watching it from the outside at that

## 11215:00 - 11250:00

point and uh just knowing you and

## 11250:00 - 11290:00

working with you. There was there was

## 11290:00 - 11340:00

stuff being said about you but but you

## 11340:00 - 11380:00

had to remain pretty quiet. I mean is

## 11380:00 - 11400:00

there anything that you that you sort of

## 11400:00 - 11445:00

want to say now? lots. But I think this

## 11445:00 - 11480:00

one thing I'll say I think people

## 11480:00 - 11535:00

assumed or might have assumed that as an

## 11535:00 - 11570:00

insider who's been at the company for 10

## 11570:00 - 11635:00

years and takes on the role of a CEO,

## 11635:00 - 11680:00

I was going to continue

## 11680:00 - 11725:00

going in the same direction.

## 11725:00 - 11805:00

The reality is that my goal was to make

## 11805:00 - 11835:00

Twitter what I think it must have been

## 11835:00 - 11880:00

and what could have been and should have

## 11880:00 - 11925:00

been. And that required a massive

## 11925:00 - 11955:00

transformation

## 11955:00 - 12025:00

of the company, the people, the product.

## 12025:00 - 12060:00

And really like all of that was coming

## 12060:00 - 12100:00

together. Like one weird anecdote that's

## 12100:00 - 12140:00

I think out there but not understood is

## 12140:00 - 12220:00

that the 3 days after we signed the deal

## 12220:00 - 12295:00

to sell the company, which was a Monday,

## 12295:00 - 12335:00

Thursday was our earnings score. And

## 12335:00 - 12400:00

there was a whole plan to

## 12400:00 - 12430:00

really

## 12430:00 - 12465:00

like trim the company down by about 20

## 12465:00 - 12495:00

25%

## 12495:00 - 12530:00

going into that earnings call because I

## 12530:00 - 12580:00

think Twitter needed to change and adapt

## 12580:00 - 12645:00

to the current moment and go from

## 12645:00 - 12700:00

being just a great product to being a

## 12700:00 - 12745:00

great product and a great business you

## 12745:00 - 12765:00

know and that was the change I think

## 12765:00 - 12790:00

that was coming which would allow you to

## 12790:00 - 12830:00

innovate on product in a real way.

## 12830:00 - 12880:00

uh I didn't get to see that through and

## 12880:00 - 12905:00

I wish most people got that.

## 12905:00 - 12945:00

>> You didn't get the chance to do that,

## 12945:00 - 12975:00

but now that you've been sort of an

## 12975:00 - 13010:00

observer of of what's happened to

## 13010:00 - 13045:00

Twitter now ex you know over the last

## 13045:00 - 13080:00

couple years what what is your take?

## 13080:00 - 13110:00

>> I think it was I was obsessed with this

## 13110:00 - 13160:00

idea. as obsessed with what we used to

## 13160:00 - 13190:00

call internally project Saturn at the

## 13190:00 - 13215:00

time, which is how do you take this

## 13215:00 - 13300:00

whole problem around content moderation

## 13300:00 - 13340:00

and actually harness the power of

## 13340:00 - 13405:00

Twitter and the community and the users

## 13405:00 - 13450:00

to do it themselves. Now, it's

## 13450:00 - 13490:00

idealistic, but I think that's sort of

## 13490:00 - 13525:00

in the realm of possible. And I think as

## 13525:00 - 13580:00

we've seen the team continue to work on

## 13580:00 - 13610:00

like what we used to call bird watch and

## 13610:00 - 13655:00

now it's called community notes. I think

## 13655:00 - 13695:00

it's great. It's loving up to the top

## 13695:00 - 13755:00

ideals of being transparent, being open

## 13755:00 - 13815:00

and sort of enabling people to to

## 13815:00 - 13850:00

contribute to Twitter in new unique ways

## 13850:00 - 13885:00

to make the entire experience better. So

## 13885:00 - 13915:00

if you have to think of like what

## 13915:00 - 13935:00

happened well like it's something I

## 13935:00 - 13975:00

really believed in I'm so glad continues

## 13975:00 - 14020:00

to be something uh where I think I

## 14020:00 - 14055:00

believe now others are even trying to

## 14055:00 - 14130:00

replicate that uh and that sort of I'm

## 14130:00 - 14165:00

so glad that continues to happen. It's

## 14165:00 - 14205:00

so amazing. What was was there one or

## 14205:00 - 14240:00

two things that you kind of took away

## 14240:00 - 14280:00

from from the 11 years spent at Twitter

## 14280:00 - 14305:00

either as a leader or or just in terms

## 14305:00 - 14350:00

of the ethos of the company and of the

## 14350:00 - 14380:00

user base that you that you brought to

## 14380:00 - 14410:00

parallel that came with you?

## 14410:00 - 14465:00

>> I think the core ethos pet Twitter like

## 14465:00 - 14545:00

the the why like for me was what the

## 14545:00 - 14570:00

words we used to use was public

## 14570:00 - 14610:00

conversation. But really what it was to

## 14610:00 - 14640:00

me was

## 14640:00 - 14690:00

everyone can in a permissionless way get

## 14690:00 - 14745:00

access to

## 14745:00 - 14775:00

everyone else and their thoughts and

## 14775:00 - 14815:00

their ideas including

## 14815:00 - 14880:00

the best people who are changing the

## 14880:00 - 14905:00

world who you want to connect with

## 14905:00 - 14945:00

directly and to get to them unfiltered

## 14945:00 - 14990:00

and to build upon them unfiltered.

## 14990:00 - 15040:00

So instead of being in

## 15040:00 - 15090:00

clothed, permissioned, invite only,

## 15090:00 - 15130:00

limited access environments,

## 15130:00 - 15165:00

there's this massive democratization of

## 15165:00 - 15190:00

access to people. Like you could

## 15190:00 - 15225:00

literally DM anyone. It's still amazing.

## 15225:00 - 15295:00

And I think that creates magic when it

## 15295:00 - 15345:00

works and it causes all kinds of

## 15345:00 - 15385:00

problems that need solving around like

## 15385:00 - 15420:00

people misbehaving. But I think it's

## 15420:00 - 15450:00

worth solving those problems because of

## 15450:00 - 15495:00

all the positive it creates. Right? And

## 15495:00 - 15515:00

I think that's the same ethos we're

## 15515:00 - 15550:00

taking at parallel which is like I think

## 15550:00 - 15610:00

we want the web to be open and we want

## 15610:00 - 15640:00

it to be permissionless and we want it

## 15640:00 - 15685:00

to be a free market and we want everyone

## 15685:00 - 15710:00

to have access to everything including

## 15710:00 - 15750:00

AIS. We want AIs to have access to the

## 15750:00 - 15805:00

entire web and that's the common thread

## 15805:00 - 15850:00

that sort of motivates parallel which

## 15850:00 - 15890:00

pulls from Twitter. I'm curious this,

## 15890:00 - 15925:00

you know, this decision to do this. So,

## 15925:00 - 15970:00

you were leading a 7,000 person public

## 15970:00 - 16015:00

company and you decided there's a

## 16015:00 - 16035:00

million things you could have done after

## 16035:00 - 16075:00

that and you decided I want to start at

## 16075:00 - 16105:00

the very beginning from zero as a

## 16105:00 - 16135:00

founder of a brand new thing. Like, how

## 16135:00 - 16165:00

did you decide that that was the thing

## 16165:00 - 16205:00

you wanted to do? I was open-minded in

## 16205:00 - 16240:00

the beginning, but I think I was like

## 16240:00 - 16270:00

just sitting there writing a bunch of

## 16270:00 - 16300:00

code,

## 16300:00 - 16345:00

having the time of my life, curious

## 16345:00 - 16400:00

about the world. It was so green field.

## 16400:00 - 16435:00

I was entertaining some calls about

## 16435:00 - 16480:00

taking on jobs that might have on paper

## 16480:00 - 16525:00

felt like big jobs.

## 16525:00 - 16550:00

But like I think like I I was at Twitter

## 16550:00 - 16590:00

long enough to have drunk the Kool-Aid

## 16590:00 - 16635:00

that I was serving to believe in this

## 16635:00 - 16685:00

notion of like openness and direct

## 16685:00 - 16720:00

connection and public information and

## 16720:00 - 16750:00

public data

## 16750:00 - 16790:00

and to join a mission like I just

## 16790:00 - 16815:00

couldn't

## 16815:00 - 16875:00

join a mission and so I think a couple

## 16875:00 - 16905:00

months in I knew that I would start

## 16905:00 - 16930:00

something. I don't think you even know

## 16930:00 - 16965:00

the story but like I ran into Josh

## 16965:00 - 17000:00

somewhere around that time. By then I

## 17000:00 - 17030:00

was set on starting a company. I had no

## 17030:00 - 17095:00

idea when and how to go about doing it.

## 17095:00 - 17125:00

And Josh gave me this piece of advice

## 17125:00 - 17160:00

that stuck with me. It's like just don't

## 17160:00 - 17200:00

be in a rush. This is going to be 10

## 17200:00 - 17265:00

plus years of your life and just don't

## 17265:00 - 17290:00

be in a rush. Don't jump on the first

## 17290:00 - 17295:00

thing.

## 17295:00 - 17330:00

>> As an engineer, as a founder, you you

## 17330:00 - 17370:00

you've developed these muscles on how to

## 17370:00 - 17425:00

build and you are very good at building.

## 17425:00 - 17470:00

But what you only do once or twice is

## 17470:00 - 17520:00

pick is pick the thing to work on. And

## 17520:00 - 17540:00

VCs one, you know, one of the I think

## 17540:00 - 17565:00

the luxuries that we have as VC is we

## 17565:00 - 17585:00

get to we get to look at a lot of things

## 17585:00 - 17615:00

and we get to pick many things and the

## 17615:00 - 17665:00

the picking muscle gets developed. And

## 17665:00 - 17695:00

when as a founder you choose the thing

## 17695:00 - 17725:00

that you're going to work on that that

## 17725:00 - 17750:00

kind of sets the boundaries and

## 17750:00 - 17775:00

constraints for you know if the company

## 17775:00 - 17805:00

is doing well in the next 10 years of

## 17805:00 - 17845:00

your life. And so it's critical. So

## 17845:00 - 17885:00

let's talk about that. How did you this

## 17885:00 - 17930:00

this idea that you picked I think is a

## 17930:00 - 17980:00

phenomenally interesting expansive idea.

## 17980:00 - 18005:00

How did this idea come to you?

## 18005:00 - 18025:00

>> I was actually looking to do something

## 18025:00 - 18085:00

in healthcare. I was hacking away agents

## 18085:00 - 18135:00

for myself to research healthcare.

## 18135:00 - 18240:00

I found myself over time spend more time

## 18240:00 - 18275:00

on the future of the web and just

## 18275:00 - 18300:00

obsessing about this idea in some

## 18300:00 - 18340:00

abstract form like almost living in this

## 18340:00 - 18385:00

science fiction of

## 18385:00 - 18420:00

oh every decision we made at Twitter

## 18420:00 - 18450:00

like we used to think about this service

## 18450:00 - 18495:00

having a 100 millcond SLA because we

## 18495:00 - 18525:00

thinking about an end customer on a

## 18525:00 - 18555:00

mobile device that had about a second

## 18555:00 - 18595:00

and this was in the stack and I started

## 18595:00 - 18630:00

really living in this notion of like All

## 18630:00 - 18675:00

of that's going to change completely.

## 18675:00 - 18705:00

All of the infrastructure that we built,

## 18705:00 - 18740:00

thought about, it's going to look

## 18740:00 - 18780:00

completely different. Every business

## 18780:00 - 18805:00

model we thought about is look going to

## 18805:00 - 18825:00

look completely different. So, it really

## 18825:00 - 18865:00

started as this science fiction of like

## 18865:00 - 18895:00

the primary consumer on the web is now

## 18895:00 - 18925:00

going to be an agent. If you change that

## 18925:00 - 18955:00

one assumption,

## 18955:00 - 18980:00

green field, what does this world look

## 18980:00 - 19010:00

like? I would just obsessively think

## 19010:00 - 19040:00

about this and I didn't actually think I

## 19040:00 - 19060:00

would start something in this space

## 19060:00 - 19075:00

because it's just like science fiction.

## 19075:00 - 19120:00

And I would just talk to people about it

## 19120:00 - 19165:00

and at some point it started becoming

## 19165:00 - 19210:00

like okay so if this could happen

## 19210:00 - 19240:00

there's a good and a bad way it could

## 19240:00 - 19275:00

happen I want the good way I have some

## 19275:00 - 19330:00

views what can I do and it took me

## 19330:00 - 19390:00

months of research understanding talking

## 19390:00 - 19450:00

to people exploring paths around this

## 19450:00 - 19480:00

idea

## 19480:00 - 19525:00

to gain conviction to one day be like

## 19525:00 - 19545:00

I'm going to do this

## 19545:00 - 19580:00

>> so what help us just sort understand

## 19580:00 - 19610:00

that a little bit better. the the idea

## 19610:00 - 19650:00

is is very interesting that the the web

## 19650:00 - 19690:00

as we know it was designed for human

## 19690:00 - 19745:00

users uh with links and navigation and

## 19745:00 - 19770:00

pages and page loads and all of that

## 19770:00 - 19805:00

stuff and if you're an AI a lot of that

## 19805:00 - 19845:00

stuff is is you know it's not designed

## 19845:00 - 19880:00

for you basically can consume data a lot

## 19880:00 - 19900:00

faster you don't need to see one page at

## 19900:00 - 19935:00

a time things like that how did you sort

## 19935:00 - 19975:00

of give us a little bit more of that

## 19975:00 - 20005:00

like what are the different assumptions

## 20005:00 - 20055:00

that you make or patterns that you build

## 20055:00 - 20090:00

for when you were building for an AI as

## 20090:00 - 20120:00

the user instead of a human as the user.

## 20120:00 - 20160:00

>> Humans, as I frame it, operate in a very

## 20160:00 - 20190:00

narrow band.

## 20190:00 - 20220:00

We

## 20220:00 - 20275:00

have a second or two of patience. We

## 20275:00 - 20315:00

under specify what we're looking for. We

## 20315:00 - 20340:00

will either implicitly just click on an

## 20340:00 - 20360:00

app and expect the app to figure out

## 20360:00 - 20400:00

what we want and show it to us like

## 20400:00 - 20455:00

Twitter or we will type an incomplete

## 20455:00 - 20490:00

set of keywords or we click on a link to

## 20490:00 - 20530:00

navigate our way to somewhere. And we

## 20530:00 - 20550:00

hope for the best and we go on this

## 20550:00 - 20595:00

random box to get stuff done. We're also

## 20595:00 - 20635:00

able to consume a few decisions like 10

## 20635:00 - 20665:00

click targets, two to three pages of

## 20665:00 - 20720:00

content at a time and most of the

## 20720:00 - 20745:00

infrastructure on the web is just trying

## 20745:00 - 20785:00

to figure out what we might be trying to

## 20785:00 - 20830:00

do and guess and point us in the right

## 20830:00 - 20855:00

direction.

## 20855:00 - 20905:00

With AI, I think we get to invert a lot

## 20905:00 - 20930:00

of this and actually that inversion is

## 20930:00 - 20970:00

something we're starting to see.

## 20970:00 - 21015:00

AIS can specify what they're trying to

## 21015:00 - 21090:00

solve. In fact, like to to do eval

## 21090:00 - 21130:00

goal is to be able to evalate. To train

## 21130:00 - 21160:00

an RL system, you need to know what the

## 21160:00 - 21195:00

end goal is and what the reward is. And

## 21195:00 - 21215:00

so when you start doing that, you can

## 21215:00 - 21255:00

start communicating that down.

## 21255:00 - 21285:00

And that's a completely different

## 21285:00 - 21310:00

interface for the underlying

## 21310:00 - 21360:00

infrastructure, right? Concretely, that

## 21360:00 - 21405:00

you no longer have to guess what might

## 21405:00 - 21440:00

this user be trying to do. You're no

## 21440:00 - 21500:00

longer stuck with producing a consistent

## 21500:00 - 21550:00

format in your answer or a said quantity

## 21550:00 - 21605:00

in your answer or

## 21605:00 - 21655:00

a 1second latency essay on your answer

## 21655:00 - 21690:00

and sometimes you'll want things in 10

## 21690:00 - 21740:00

minutes and sometimes you'll want 100

## 21740:00 - 21770:00

documents and sometimes you'll want like

## 21770:00 - 21820:00

a one word answer as an AI making a call

## 21820:00 - 21870:00

to you, right? And so the problem space

## 21870:00 - 21925:00

really expands. Now we within this

## 21925:00 - 21970:00

expanded problem set made after a bunch

## 21970:00 - 22000:00

of time with potential customers an

## 22000:00 - 22030:00

opinionated set of narrow decisions

## 22030:00 - 22075:00

around which small slice of this would

## 22075:00 - 22130:00

matter first right and that's sort of

## 22130:00 - 22190:00

where we took this humans are different

## 22190:00 - 22215:00

from AIs they are different in all of

## 22215:00 - 22240:00

these ways the query language will

## 22240:00 - 22275:00

expand but now what's the most

## 22275:00 - 22300:00

interesting slice of this that we should

## 22300:00 - 22355:00

go attack and we went after the slow end

## 22355:00 - 22405:00

to end human automation measurable able

## 22405:00 - 22450:00

repetitive eval friendly work.

## 22450:00 - 22485:00

>> So let's talk about a little of that.

## 22485:00 - 22520:00

What are some of the initial kind of use

## 22520:00 - 22565:00

cases, customers, scenarios where you

## 22565:00 - 22590:00

felt like this this kind of architecture

## 22590:00 - 22620:00

could be really powerful?

## 22620:00 - 22650:00

>> So the first few use cases we went after

## 22650:00 - 22710:00

were this notion of repetitive

## 22710:00 - 22795:00

work. you might outsource to a BPO or

## 22795:00 - 22845:00

KPO out there and that was an accidental

## 22845:00 - 22875:00

discovery in some sense talking to some

## 22875:00 - 22895:00

customers who were doing this and

## 22895:00 - 22915:00

they're like oh if your system can

## 22915:00 - 22955:00

outperform this that would be cool like

## 22955:00 - 22990:00

actually we might be able to let's try

## 22990:00 - 23035:00

and so and then we realized that AI

## 23035:00 - 23070:00

performance when you have repetitive

## 23070:00 - 23140:00

wellsp specified work improves

## 23140:00 - 23170:00

human performance when you have to train

## 23170:00 - 23215:00

50 people to do repetitive work

## 23215:00 - 23225:00

declines.

## 23225:00 - 23275:00

>> These are people doing desk research or

## 23275:00 - 23325:00

>> yeah desk research or some workflow on

## 23325:00 - 23380:00

the public web on insurance claims

## 23380:00 - 23435:00

processing or underwriting or figuring

## 23435:00 - 23465:00

out some data set based on something

## 23465:00 - 23505:00

governments published on how much to tax

## 23505:00 - 23540:00

what entity how to be compliant with

## 23540:00 - 23585:00

what on pulling financial data out of

## 23585:00 - 23625:00

the web to create pure data sets. All

## 23625:00 - 23670:00

kinds of this work happens. We're

## 23670:00 - 23705:00

obsessed with the web, but we wanted to

## 23705:00 - 23780:00

add value and we picked this as our

## 23780:00 - 23810:00

things that we would start working on

## 23810:00 - 23845:00

and really pushing the limits of what's

## 23845:00 - 23875:00

possible in a system on delivering

## 23875:00 - 23920:00

quality. So, we decided we would care

## 23920:00 - 23950:00

only about accuracy and quality in our

## 23950:00 - 24005:00

system. We would not care about latency.

## 24005:00 - 24045:00

That decision because this is the set we

## 24045:00 - 24075:00

wanted to go play on first.

## 24075:00 - 24105:00

>> I think it's really exciting if I have

## 24105:00 - 24130:00

the numbers correct. We now have more

## 24130:00 - 24185:00

than 100 paying customers at Parallel.

## 24185:00 - 24225:00

Tell us about some of the use cases.

## 24225:00 - 24265:00

What are they using the APIs for? No,

## 24265:00 - 24315:00

it's been really exciting to work with

## 24315:00 - 24340:00

more and more customers and we've really

## 24340:00 - 24370:00

scaled the number of customers we've

## 24370:00 - 24395:00

been sort of working with both in terms

## 24395:00 - 24440:00

of numbers but also in terms of the

## 24440:00 - 24480:00

breadth of use cases that we now serve.

## 24480:00 - 24545:00

So on the one end we serve these

## 24545:00 - 24580:00

extremely

## 24580:00 - 24625:00

longunning deep research use cases which

## 24625:00 - 24660:00

would otherwise be done by a human and

## 24660:00 - 24715:00

on the other extreme we might serve as a

## 24715:00 - 24760:00

search tool that a coding agent might

## 24760:00 - 24795:00

use and call it and get an answer within

## 24795:00 - 24845:00

3 seconds to look up documentation to

## 24845:00 - 24885:00

figure out how to course correct when it

## 24885:00 - 24930:00

might need the live web. So we have a

## 24930:00 - 24990:00

breadth of usage. The other amazing

## 24990:00 - 25030:00

thing to see as we've been building this

## 25030:00 - 25065:00

is

## 25065:00 - 25120:00

how it's been scaling. We now serve like

## 25120:00 - 25170:00

millions and millions of requests a day

## 25170:00 - 25235:00

and it's our cheapest requests on our

## 25235:00 - 25305:00

system cost under half a cent and the

## 25305:00 - 25340:00

most expensive requests to our system

## 25340:00 - 25400:00

today can cost

## 25400:00 - 25470:00

$10. And it's amazing to see like this

## 25470:00 - 25505:00

is not something I could have imagined

## 25505:00 - 25550:00

the breadth of customers, the scale of

## 25550:00 - 25600:00

use going into this year. And it's been

## 25600:00 - 25640:00

sort of amazing to have all of that come

## 25640:00 - 25665:00

together in this moment.

## 25665:00 - 25695:00

>> It's interesting you named a bunch of

## 25695:00 - 25725:00

different use cases across all of your

## 25725:00 - 25760:00

customers. Is there a, you know, an

## 25760:00 - 25790:00

example or an anecdote that sticks out

## 25790:00 - 25815:00

in your head about a customer that you

## 25815:00 - 25845:00

worked with early on where where they

## 25845:00 - 25880:00

really kind of pushed you and helped

## 25880:00 - 25920:00

shape what parallel would be? Yeah, I

## 25920:00 - 25945:00

think in the early days when we were

## 25945:00 - 25985:00

working on one of these insurance use

## 25985:00 - 26060:00

cases really the bar was we had a data

## 26060:00 - 26110:00

set which was being generated as a

## 26110:00 - 26170:00

result of human operations and we got

## 26170:00 - 26210:00

that data set it was like ground truth

## 26210:00 - 26280:00

and the question was could an AI system

## 26280:00 - 26330:00

this last year compete or drive

## 26330:00 - 26380:00

productivity or entirely replace it as

## 26380:00 - 26430:00

we work through it like we scoring low

## 26430:00 - 26470:00

and then we had to go dig into the data

## 26470:00 - 26495:00

set. Turns out ground truth is never

## 26495:00 - 26530:00

ground truth. Right? So one of the

## 26530:00 - 26580:00

things we we sort of totally changed in

## 26580:00 - 26615:00

our worldview was ground truth is never

## 26615:00 - 26650:00

ground truth and that we actually have

## 26650:00 - 26695:00

to do comparative

## 26695:00 - 26760:00

analysis of quality and really reframe

## 26760:00 - 26800:00

every customer conversation we have

## 26800:00 - 26860:00

around let's compare two alternatives.

## 26860:00 - 26895:00

And we found creative ways of doing it.

## 26895:00 - 26935:00

It's not complicated, right? Two ways of

## 26935:00 - 26970:00

solving a problem will agree in some

## 26970:00 - 26985:00

cases and you don't need to look at

## 26985:00 - 27025:00

them. Where they disagree, you take a

## 27025:00 - 27065:00

small sample and you grade which one you

## 27065:00 - 27110:00

prefer on that sample of five or 10 and

## 27110:00 - 27135:00

then you know which way is better

## 27135:00 - 27200:00

roughly. And so we started from that one

## 27200:00 - 27225:00

customer journey. We went through this

## 27225:00 - 27255:00

bespoke process in the design

## 27255:00 - 27295:00

partnership. But then we learned this

## 27295:00 - 27345:00

very simple pattern that has really been

## 27345:00 - 27370:00

something that has worked with like the

## 27370:00 - 27405:00

customers who are most most most

## 27405:00 - 27450:00

selective on quality bar and are working

## 27450:00 - 27490:00

on like these human operations and

## 27490:00 - 27515:00

scaled human operations when they want

## 27515:00 - 27535:00

to automate them.

## 27535:00 - 27570:00

>> I'd love to hear maybe about some of

## 27570:00 - 27595:00

these examples. One one of the customers

## 27595:00 - 27615:00

that I know of because they're also a

## 27615:00 - 27670:00

first round company is Clay. Um and we

## 27670:00 - 27705:00

we love it obviously when when companies

## 27705:00 - 27740:00

are become customers of each other. Tell

## 27740:00 - 27770:00

tell me about you know sort of their use

## 27770:00 - 27805:00

case for parallel and and what they were

## 27805:00 - 27825:00

trying to do and what maybe there some

## 27825:00 - 27860:00

of their alternatives would have been

## 27860:00 - 27905:00

>> you make it seem like a coincidence like

## 27905:00 - 27945:00

you all connected us with clay that's

## 27945:00 - 28025:00

one of the hugely valuable to discover

## 28025:00 - 28055:00

people who are forward-looking people

## 28055:00 - 28115:00

who are truly innovating like they were

## 28115:00 - 28140:00

one of the early people who worked on

## 28140:00 - 28175:00

building benchmarks with us they were

## 28175:00 - 28260:00

ahead of the curve in bringing AI to a

## 28260:00 - 28305:00

lot of people making it an amazing

## 28305:00 - 28350:00

experience, a really powerful experience

## 28350:00 - 28400:00

and they took a bet on working with us

## 28400:00 - 28440:00

very early on and they built benchmarks

## 28440:00 - 28465:00

with us, collaborated with us, pushed

## 28465:00 - 28505:00

our technology and hopefully got some

## 28505:00 - 28525:00

benefit in pushing their product

## 28525:00 - 28590:00

forward. Now, as early partnerships are,

## 28590:00 - 28625:00

I think it was really co-creation, I

## 28625:00 - 28680:00

would say. But if you think about

## 28680:00 - 28725:00

repetitive web research give people

## 28725:00 - 28785:00

extreme leverage in understanding every

## 28785:00 - 28825:00

prospective customer or current customer

## 28825:00 - 28870:00

everything about them prioritizing

## 28870:00 - 28905:00

across them and all kinds of things that

## 28905:00 - 28950:00

people want to do at scale. We were able

## 28950:00 - 28985:00

to partner with them try to push the

## 28985:00 - 29020:00

limits of

## 29020:00 - 29045:00

accuracy that you can achieve in doing

## 29045:00 - 29075:00

this work because it matters for their

## 29075:00 - 29125:00

use cases. And in that sense that was a

## 29125:00 - 29165:00

really you know great relationship

## 29165:00 - 29190:00

partnership because they've really

## 29190:00 - 29230:00

pushed us being a demanding

## 29230:00 - 29255:00

sophisticated

## 29255:00 - 29265:00

customer.

## 29265:00 - 29300:00

>> So what what are the APIs that parallel

## 29300:00 - 29325:00

provides to them that they're that

## 29325:00 - 29345:00

they're leveraging?

## 29345:00 - 29425:00

>> Parallel are task API which is just our

## 29425:00 - 29465:00

API which allows you to get structured

## 29465:00 - 29515:00

enrichments back.

## 29515:00 - 29545:00

It allows you to specify a compute

## 29545:00 - 29600:00

budget effectively. Um, and we just

## 29600:00 - 29690:00

produce answers. Now, they make a really

## 29690:00 - 29740:00

AI friendly API accessible to end

## 29740:00 - 29775:00

customers. They have a system on top

## 29775:00 - 29830:00

which orchestrates on top of our API in

## 29830:00 - 29875:00

order for people to type small

## 29875:00 - 29910:00

underspecified prompts but they have

## 29910:00 - 29940:00

pattern matched across their customer

## 29940:00 - 30010:00

base and they know what it means in

## 30010:00 - 30035:00

terms of the output someone might want

## 30035:00 - 30070:00

and they specify those queries down to

## 30070:00 - 30085:00

our system.

## 30085:00 - 30110:00

>> Their end users are basically writing

## 30110:00 - 30150:00

stuff in in nil language. Clay has like

## 30150:00 - 30180:00

an AI orchestrator kind of routing

## 30180:00 - 30190:00

system

## 30190:00 - 30205:00

>> and an AI

## 30205:00 - 30230:00

>> so the AI is what's querying

## 30230:00 - 30255:00

>> AI is quering us. Yeah,

## 30255:00 - 30295:00

>> that's what I mean by customers. Like we

## 30295:00 - 30355:00

wanted our customers to be an AI

## 30355:00 - 30390:00

writing queries.

## 30390:00 - 30435:00

Our system is built for natural language

## 30435:00 - 30485:00

but humans as I said earlier

## 30485:00 - 30530:00

underspecify things. You can use AIS to

## 30530:00 - 30590:00

help humans not underspecify things and

## 30590:00 - 30620:00

write query like so we don't

## 30620:00 - 30660:00

particularly optimize our APIs to be

## 30660:00 - 30695:00

human friendly because we expect our

## 30695:00 - 30730:00

customers to be able to do that. So they

## 30730:00 - 30750:00

were basically saying these are the

## 30750:00 - 30775:00

benchmarks we need you to hit or how how

## 30775:00 - 30790:00

did how did that work?

## 30790:00 - 30845:00

>> No, they were they had built

## 30845:00 - 30905:00

real benchmark on the products they

## 30905:00 - 30945:00

wanted their customers to have and

## 30945:00 - 30985:00

accuracy they wanted to have. They've

## 30985:00 - 31030:00

also built a lot of AI technologies that

## 31030:00 - 31080:00

can actually solve for those benchmarks.

## 31080:00 - 31100:00

But they were open-minded to working

## 31100:00 - 31145:00

with us if by working together we could

## 31145:00 - 31200:00

do better or we could provide options to

## 31200:00 - 31235:00

their customers. Clay is all about

## 31235:00 - 31265:00

providing many many different ways for

## 31265:00 - 31330:00

people to do things. Um and we ended up

## 31330:00 - 31360:00

being one of the options they're able to

## 31360:00 - 31385:00

provide to their customers and customers

## 31385:00 - 31415:00

use in very creative ways.

## 31415:00 - 31455:00

>> So I mean Clay sounds kind of like one

## 31455:00 - 31485:00

of the perfect initial customers in

## 31485:00 - 31510:00

terms of how forward thinking they are.

## 31510:00 - 31550:00

the amount of volume that they have like

## 31550:00 - 31590:00

really having you know high demands on

## 31590:00 - 31620:00

your system which always I think is a

## 31620:00 - 31640:00

great design partner to work with like

## 31640:00 - 31665:00

are they the ideal customer or who who

## 31665:00 - 31700:00

is the ideal customer now that you're

## 31700:00 - 31725:00

sort of going you know while you're

## 31725:00 - 31750:00

looking to expand

## 31750:00 - 31820:00

>> I think now we have a very broad set of

## 31820:00 - 31890:00

customers we serve um clay is one of the

## 31890:00 - 31925:00

ideal patterns

## 31925:00 - 32005:00

in that scaled repetitive

## 32005:00 - 32050:00

web data is really critical and accuracy

## 32050:00 - 32095:00

matters but on the other extreme we have

## 32095:00 - 32125:00

some coding agents using some of our

## 32125:00 - 32185:00

APIs right so but there we show up maybe

## 32185:00 - 32240:00

in 5% of prompts right so when you need

## 32240:00 - 32275:00

to look up some recent documentation so

## 32275:00 - 32320:00

it's an agent really calling a tool

## 32320:00 - 32360:00

right instead of using our end toend

## 32360:00 - 32410:00

task API you'd use a search API as a

## 32410:00 - 32465:00

tool we have customers doing claims

## 32465:00 - 32510:00

processing and insurance and running a

## 32510:00 - 32545:00

workflow where there are still humans

## 32545:00 - 32600:00

doing some QA on top. Some of the BPOS

## 32600:00 - 32625:00

and KPOS we mentioned earlier, some of

## 32625:00 - 32675:00

them are now our customers too. And so

## 32675:00 - 32705:00

we've sort of we're building a very

## 32705:00 - 32755:00

horizontal product and we have now a

## 32755:00 - 32820:00

variety of different customers

## 32820:00 - 32875:00

where the needs really converge

## 32875:00 - 32910:00

to and the API that we're trying to

## 32910:00 - 32950:00

design we wanted to be able to serve

## 32950:00 - 32995:00

this very diverse set of customers that

## 32995:00 - 33030:00

otherwise wouldn't fit a single ICP

## 33030:00 - 33065:00

>> for those customers for the data that

## 33065:00 - 33090:00

they're trying to gather and make

## 33090:00 - 33120:00

available to their AIS like what are the

## 33120:00 - 33135:00

alternatives

## 33135:00 - 33170:00

>> BPOS right like let's get humans to

## 33170:00 - 33225:00

create extremely highquality data sets

## 33225:00 - 33265:00

and we have a different we have a value

## 33265:00 - 33305:00

prop on that in that like we actually

## 33305:00 - 33350:00

compete really on quality with them. In

## 33350:00 - 33380:00

the other case, the alternative that we

## 33380:00 - 33430:00

often encounter is

## 33430:00 - 33530:00

some sort of build your own or use just

## 33530:00 - 33570:00

plain openi. They just recently shipped

## 33570:00 - 33610:00

a search. In both cases, our primary

## 33610:00 - 33675:00

value prop is quality, quality, quality.

## 33675:00 - 33735:00

And the secondary value prop is price

## 33735:00 - 33775:00

performance. I think for us, the reason

## 33775:00 - 33800:00

we care so much about price performance

## 33800:00 - 33835:00

is this. going back to the vision of

## 33835:00 - 33890:00

like AIS should use the web a lot and

## 33890:00 - 33925:00

create a lot of value. I think the only

## 33925:00 - 33975:00

way you unlock new and new use cases is

## 33975:00 - 34020:00

taking something that can be done and

## 34020:00 - 34050:00

incentivizing people to do it at 100x

## 34050:00 - 34060:00

the scale

## 34060:00 - 34085:00

>> and removing the friction around that

## 34085:00 - 34110:00

basically by having extreme performance

## 34110:00 - 34145:00

for low cost. That makes sense. So this

## 34145:00 - 34170:00

gets into a question actually that you

## 34170:00 - 34195:00

know I'm sure you thought of this as you

## 34195:00 - 34220:00

were sort of like thinking about this

## 34220:00 - 34280:00

idea is is just potential competition

## 34280:00 - 34315:00

and how this market shapes up like one

## 34315:00 - 34350:00

way of of thinking about this is like

## 34350:00 - 34400:00

what do you think is the territory of

## 34400:00 - 34460:00

the hyperscalers or the major labs

## 34460:00 - 34490:00

versus what what is the opportunity

## 34490:00 - 34520:00

that's available to a new startup when

## 34520:00 - 34550:00

it comes to you know this kind of next

## 34550:00 - 34585:00

generation of AI infra

## 34585:00 - 34605:00

>> I don't think too much about the

## 34605:00 - 34650:00

competitive dynamics two reasons

## 34650:00 - 34680:00

one I think we're going to live in the

## 34680:00 - 34740:00

most positive some future over the next

## 34740:00 - 34800:00

several years and so there's just like

## 34800:00 - 34830:00

if even if you can't fully articulate

## 34830:00 - 34870:00

what it is the opportunity set for

## 34870:00 - 34925:00

people to mobilize and make an impact is

## 34925:00 - 35005:00

extremely high I think like hyperscalers

## 35005:00 - 35040:00

can't move fast enough to capture the

## 35040:00 - 35085:00

opportunity can't build fast enough

## 35085:00 - 35130:00

right the labs are amazing they move

## 35130:00 - 35200:00

really really fast but they're also slow

## 35200:00 - 35245:00

relative to how fast we can move right

## 35245:00 - 35300:00

and there are so many places to innovate

## 35300:00 - 35345:00

we see that from our customers every day

## 35345:00 - 35395:00

I of don't think that is something to

## 35395:00 - 35440:00

think about you of course have to on a

## 35440:00 - 35465:00

daily basis think about in the context

## 35465:00 - 35515:00

of what choices your customers have and

## 35515:00 - 35550:00

why they must

## 35550:00 - 35590:00

partner with you collaborate with you

## 35590:00 - 35625:00

buy from you and in that sense we really

## 35625:00 - 35655:00

think about it, but then that's a really

## 35655:00 - 35690:00

product decision on like how do you

## 35690:00 - 35715:00

differentiate your product and stay

## 35715:00 - 35745:00

ahead of the curve and we think about

## 35745:00 - 35765:00

that obsessively.

## 35765:00 - 35790:00

>> So I know that you've been you know we

## 35790:00 - 35805:00

said this before that you had kind of

## 35805:00 - 35825:00

been in stealth for a while. You've been

## 35825:00 - 35870:00

mostly heads down building selling

## 35870:00 - 35910:00

building selling but now you know you're

## 35910:00 - 35930:00

starting to make a little bit more noise

## 35930:00 - 35980:00

with this launch. Um I believe you

## 35980:00 - 36005:00

recently launched some self-s serve

## 36005:00 - 36025:00

options so that people could just come

## 36025:00 - 36060:00

to parallel and find you know the things

## 36060:00 - 36090:00

they want. What what advice would you

## 36090:00 - 36125:00

have for other AI founders who are

## 36125:00 - 36170:00

figuring out you s when do I launch when

## 36170:00 - 36205:00

do I open up the product more? How did

## 36205:00 - 36230:00

you think about that?

## 36230:00 - 36265:00

>> One of the piece of advice I got of

## 36265:00 - 36285:00

starting this company I spoke with

## 36285:00 - 36320:00

Patrick Collison at Stripe on building

## 36320:00 - 36350:00

an API business he said like your first

## 36350:00 - 36395:00

API design will be wrong. just know that

## 36395:00 - 36420:00

I don't know if this is this was

## 36420:00 - 36450:00

intended but I took that really to mean

## 36450:00 - 36510:00

that like keeping the customer set small

## 36510:00 - 36555:00

and intimate so that when we find it's

## 36555:00 - 36595:00

wrong and it's limiting what we would

## 36595:00 - 36635:00

build you want to be able to migrate to

## 36635:00 - 36660:00

a next version of the API even if it's

## 36660:00 - 36715:00

backward incompatible right so we really

## 36715:00 - 36755:00

wanted to maintain that flexibility so

## 36755:00 - 36805:00

we made a very intentional decision to

## 36805:00 - 36850:00

limit the number of customers who would

## 36850:00 - 36875:00

have an API

## 36875:00 - 36925:00

while we didn't feel that we had thought

## 36925:00 - 36955:00

through we didn't want to like design

## 36955:00 - 36995:00

the API in a lab but we also didn't want

## 36995:00 - 37035:00

to have an API that we were stuck

## 37035:00 - 37070:00

supporting forever so we made that

## 37070:00 - 37095:00

intentional choice the other thing we

## 37095:00 - 37145:00

did was we put a lot of almost like we

## 37145:00 - 37185:00

were very selective in the customers

## 37185:00 - 37235:00

like we wanted to work with customers

## 37235:00 - 37270:00

that we love working with and that loved

## 37270:00 - 37310:00

working with us right because like

## 37310:00 - 37355:00

that's what drives you in terms of

## 37355:00 - 37375:00

energy

## 37375:00 - 37390:00

Right.

## 37390:00 - 37415:00

>> Another thing I wanted to ask you about

## 37415:00 - 37455:00

briefly is fundraising. You know, we're

## 37455:00 - 37480:00

seeing founders raise these really big

## 37480:00 - 37515:00

rounds, but also building smaller teams,

## 37515:00 - 37545:00

you know, than than years past. What

## 37545:00 - 37570:00

advice maybe would you share with the

## 37570:00 - 37620:00

founder of an AI company, particularly,

## 37620:00 - 37640:00

you know, every everything's moving so

## 37640:00 - 37670:00

fast these days. There's so so much

## 37670:00 - 37700:00

flashiness. How did you think about

## 37700:00 - 37730:00

fundraising? And what's the maybe advice

## 37730:00 - 37745:00

you give?

## 37745:00 - 37785:00

>> Maybe two different dimensions. One, who

## 37785:00 - 37850:00

to work with? And I had one very simple

## 37850:00 - 37900:00

rubric. People,

## 37900:00 - 37940:00

it's for me just the people I would

## 37940:00 - 38000:00

spend time with. And if they said

## 38000:00 - 38055:00

something to me and I dramatically

## 38055:00 - 38105:00

disagreed with them,

## 38105:00 - 38160:00

will I feel sleepless that night to try

## 38160:00 - 38215:00

to reconcile why? And people who I feel

## 38215:00 - 38255:00

that way with,

## 38255:00 - 38310:00

I want them around me. And I want the

## 38310:00 - 38370:00

coalition we have with we know that

## 38370:00 - 38410:00

Kosla Ventures with Shardlet Index with

## 38410:00 - 38435:00

you and Josh working with us from First

## 38435:00 - 38470:00

Round Capital is it's kind of

## 38470:00 - 38525:00

interesting you all come at

## 38525:00 - 38570:00

our company and our vision with slightly

## 38570:00 - 38615:00

different lenses and the advice I get

## 38615:00 - 38655:00

from all of you is slightly different. I

## 38655:00 - 38680:00

have

## 38680:00 - 38720:00

respect for all of these people. I

## 38720:00 - 38775:00

expect to build it myself and ignore

## 38775:00 - 38825:00

advice a lot of the times because it's

## 38825:00 - 38890:00

not right for me in that moment but I

## 38890:00 - 38925:00

think it's very material sometimes when

## 38925:00 - 38965:00

you get a piece of advice and it changes

## 38965:00 - 39000:00

how you think about something where you

## 39000:00 - 39025:00

go

## 39025:00 - 39080:00

and I think that's the real value I see

## 39080:00 - 39140:00

in choice of investor to me building the

## 39140:00 - 39165:00

company is binary either we are

## 39165:00 - 39200:00

successful or we're not there's just

## 39200:00 - 39235:00

like nothing in the middle right. So I

## 39235:00 - 39280:00

asked myself the question I should raise

## 39280:00 - 39340:00

the amount where I can argue up till

## 39340:00 - 39385:00

that amount that I have a reason for

## 39385:00 - 39420:00

believing that my binary odds increase

## 39420:00 - 39460:00

for some reason and once I can't make

## 39460:00 - 39485:00

that case I shouldn't raise more than

## 39485:00 - 39530:00

that if you can raise an infinite amount

## 39530:00 - 39605:00

and we were fortunate in that like I got

## 39605:00 - 39635:00

to raise

## 39635:00 - 39685:00

what I thought was the point of based on

## 39685:00 - 39725:00

my plans for the next few

## 39725:00 - 39750:00

the point of diminishing returns on

## 39750:00 - 39790:00

binary success and in fact like I don't

## 39790:00 - 39810:00

even think it's diminishing at some

## 39810:00 - 39845:00

point there negative returns that's the

## 39845:00 - 39885:00

decision-m framework we used like not

## 39885:00 - 39910:00

there's no science it's all intuition

## 39910:00 - 39950:00

it's like okay if we raved x million

## 39950:00 - 40000:00

versus y million

## 40000:00 - 40040:00

do I think there are scenarios I can

## 40040:00 - 40080:00

imagine where we're way more likely to

## 40080:00 - 40120:00

be successful I can let's raise y

## 40120:00 - 40165:00

million what if it is z million I

## 40165:00 - 40195:00

imagine that not really let's just raise

## 40195:00 - 40240:00

y and What about when it comes to team

## 40240:00 - 40285:00

building and I remember you know when

## 40285:00 - 40310:00

the seed round happened I think you

## 40310:00 - 40345:00

already had five or six engineer really

## 40345:00 - 40385:00

really good engineers kind of lined up

## 40385:00 - 40430:00

you know ready ready to go when you were

## 40430:00 - 40485:00

hiring engineers at parallel now just

## 40485:00 - 40535:00

given how productive engineers can be in

## 40535:00 - 40590:00

2025 what do you look for that's maybe

## 40590:00 - 40610:00

different than what you would have

## 40610:00 - 40635:00

looked for you know five or six years

## 40635:00 - 40655:00

ago

## 40655:00 - 40685:00

>> of course at Twitter I got to know and

## 40685:00 - 40735:00

work with some amazing engineers at the

## 40735:00 - 40780:00

same time. There's like a bunch of

## 40780:00 - 40820:00

extremely high potential

## 40820:00 - 40890:00

amazing young engineers around and I

## 40890:00 - 40940:00

really wanted this company to

## 40940:00 - 40980:00

bring in the best of both together. One

## 40980:00 - 41015:00

of my hiring philosophies at parallel

## 41015:00 - 41070:00

really is that you want to maximize how

## 41070:00 - 41130:00

much through hiring you can get alpha.

## 41130:00 - 41160:00

What's the upside? So you got to bet on

## 41160:00 - 41205:00

potential. Not been there, done that.

## 41205:00 - 41240:00

Now, you can't put an entire team of 20

## 41240:00 - 41260:00

people just betting on potential

## 41260:00 - 41340:00

together and get rid of that. So, I hire

## 41340:00 - 41380:00

a team. So it's not an individual choice

## 41380:00 - 41415:00

but everyone on the team is either there

## 41415:00 - 41440:00

where we're taking risk betting on

## 41440:00 - 41500:00

potential or we're hiring someone

## 41500:00 - 41550:00

because they are particularly good at

## 41550:00 - 41595:00

taking these extremely high potential

## 41595:00 - 41640:00

people and channeling them towards a

## 41640:00 - 41670:00

mission giving them room to be creative

## 41670:00 - 41725:00

and bring alpha while aligning them

## 41725:00 - 41765:00

towards a singular outcome for your

## 41765:00 - 41790:00

customers. The second thing that's

## 41790:00 - 41815:00

really important if you embrace this

## 41815:00 - 41865:00

sort of bet take risk on hiring is you

## 41865:00 - 41890:00

have to be somewhat like the system only

## 41890:00 - 41920:00

works if you also embrace being decent

## 41920:00 - 41970:00

at firing. I don't know how to be good

## 41970:00 - 42015:00

at hiring where you don't make mistakes

## 42015:00 - 42045:00

especially when you're trying to bet on

## 42045:00 - 42090:00

upside. And so you have to learn and set

## 42090:00 - 42125:00

the expectations and work in a world

## 42125:00 - 42165:00

where you're good at firing. And I think

## 42165:00 - 42205:00

if you put these together, you get to

## 42205:00 - 42270:00

have a amazing high performant

## 42270:00 - 42355:00

team which can build fast and build for

## 42355:00 - 42390:00

this current moment. And that's sort of

## 42390:00 - 42430:00

the philosophy we've really embraced. It

## 42430:00 - 42460:00

sounds like to me like you've got, you

## 42460:00 - 42480:00

know, I don't know if it's half the

## 42480:00 - 42525:00

folks who are very high potential, maybe

## 42525:00 - 42550:00

earlier career, maybe a little more

## 42550:00 - 42590:00

chaotic. You've got some very senior

## 42590:00 - 42615:00

folks who are kind of like the steady

## 42615:00 - 42645:00

hands who have seen a lot in in the

## 42645:00 - 42655:00

field.

## 42655:00 - 42680:00

>> But I think it's there that's more more

## 42680:00 - 42730:00

to it. It's not just about seniority. I

## 42730:00 - 42815:00

think it's about people who are good at

## 42815:00 - 42875:00

working with bringing the best out of

## 42875:00 - 42910:00

high alpha people and have a track

## 42910:00 - 42955:00

record of having right and those tend to

## 42955:00 - 42995:00

be people I've seen do that well. like

## 42995:00 - 43025:00

more broadly, how do you see this kind

## 43025:00 - 43070:00

of changing when it when it comes to org

## 43070:00 - 43105:00

design, when it comes to the number of

## 43105:00 - 43135:00

engineers you need to to build an

## 43135:00 - 43170:00

incredible product? Where do you think

## 43170:00 - 43200:00

we're going with all of this? There are

## 43200:00 - 43240:00

two forces that pull in you in different

## 43240:00 - 43280:00

directions. Number one, you can deaf

## 43280:00 - 43330:00

one, you don't need a lot of like we

## 43330:00 - 43365:00

don't have any hierarchy right now. We

## 43365:00 - 43405:00

also don't have too many, we don't talk

## 43405:00 - 43445:00

about roles, we don't have teams, we

## 43445:00 - 43480:00

don't have hierarchy. We're very

## 43480:00 - 43495:00

chaotic.

## 43495:00 - 43525:00

>> There's no sub teams within the 22

## 43525:00 - 43530:00

people.

## 43530:00 - 43555:00

>> There are no formal sub teams. People

## 43555:00 - 43610:00

work in small project groups, but those

## 43610:00 - 43640:00

rotate. Now, of course, people take

## 43640:00 - 43690:00

ownership of systems they've built, but

## 43690:00 - 43725:00

there is a lot of fluidity. There's no

## 43725:00 - 43765:00

formal team structures or managers or

## 43765:00 - 43820:00

any such thing so far. So that I think

## 43820:00 - 43850:00

you get to do at this scale. I don't

## 43850:00 - 43885:00

think it scales to double this size, but

## 43885:00 - 43925:00

we get to do this for now. But actually

## 43925:00 - 43960:00

the the force that pulls you towards

## 43960:00 - 44010:00

sort of hiring more people is the

## 44010:00 - 44055:00

possibilities are endless. The customer

## 44055:00 - 44115:00

needs and the products you could build

## 44115:00 - 44150:00

where there is demand for once you are

## 44150:00 - 44175:00

working with some customers and some

## 44175:00 - 44225:00

problem spaces. you see opportunity

## 44225:00 - 44260:00

everywhere. Everything feels within

## 44260:00 - 44300:00

reach and so that pulls you in the

## 44300:00 - 44330:00

direction

## 44330:00 - 44400:00

of having more people, right? So that's

## 44400:00 - 44455:00

why I don't know which way it will

## 44455:00 - 44485:00

converge over time because but I do

## 44485:00 - 44530:00

think that definitely you should expect

## 44530:00 - 44600:00

more to be done by fewer people even if

## 44600:00 - 44630:00

it's like there are obviously ways to

## 44630:00 - 44645:00

work with AIS which are

## 44645:00 - 44675:00

counterproductive and I've done this

## 44675:00 - 44700:00

personally a lot right but

## 44700:00 - 44725:00

systematically if you hire the right

## 44725:00 - 44765:00

people and they have good judgment we'll

## 44765:00 - 44780:00

get the good out of AI

## 44780:00 - 44805:00

>> what's a counterproductive way of

## 44805:00 - 44830:00

working with AI that you've seen

## 44830:00 - 44865:00

>> oh I personally

## 44865:00 - 44895:00

Like I will sometimes there are some

## 44895:00 - 44945:00

things which I could personally engineer

## 44945:00 - 44990:00

and I would do better but if I truly

## 44990:00 - 45030:00

embrace and start enjoying why coding in

## 45030:00 - 45060:00

our code bases

## 45060:00 - 45100:00

I might personally take longer and it's

## 45100:00 - 45125:00

poor and you have to it's like a learned

## 45125:00 - 45165:00

skill in my opinion like you can really

## 45165:00 - 45210:00

in aggregate waste time productivity

## 45210:00 - 45240:00

distract others with like crazy code

## 45240:00 - 45290:00

reviews or bugs that you're fixing

## 45290:00 - 45310:00

downstream because you don't understand

## 45310:00 - 45350:00

what you're doing. There are bad ways of

## 45350:00 - 45385:00

working with AI.

## 45385:00 - 45425:00

I think it's a learned skill to be

## 45425:00 - 45480:00

productive with AI in a real production

## 45480:00 - 45520:00

system. And I've personally I know my

## 45520:00 - 45580:00

team sees this like wcoded stuff without

## 45580:00 - 45610:00

deep full understanding of what I was

## 45610:00 - 45650:00

doing and my team has had to clean up be

## 45650:00 - 45685:00

behind me. So there are bad ways of

## 45685:00 - 45725:00

working with it. But I do think by and

## 45725:00 - 45755:00

large

## 45755:00 - 45790:00

people figure out what are good ways

## 45790:00 - 45825:00

especially in teams.

## 45825:00 - 45890:00

uh there's a lot of code review learning

## 45890:00 - 45940:00

or experiential learning and sharing

## 45940:00 - 45970:00

that happens and setting up the codebase

## 45970:00 - 45995:00

to be more productive for AIS and

## 45995:00 - 46020:00

understanding what works and what

## 46020:00 - 46050:00

doesn't work from your experience and

## 46050:00 - 46095:00

others experiences that really gets you

## 46095:00 - 46125:00

dialed into the right pattern. So you do

## 46125:00 - 46160:00

expect more productivity and I think

## 46160:00 - 46195:00

it'll only increase from there. Is there

## 46195:00 - 46225:00

anything intentional that you guys had

## 46225:00 - 46265:00

to do to enable the codebase to be

## 46265:00 - 46290:00

maximally productive with the with the

## 46290:00 - 46315:00

size of team and the amount of AI

## 46315:00 - 46345:00

codegen that you're using?

## 46345:00 - 46405:00

>> Very tactical things. Um I would say we

## 46405:00 - 46460:00

have this massive crawler and index

## 46460:00 - 46495:00

infrastructure which is like a not like

## 46495:00 - 46565:00

a standard small front-end code base or

## 46565:00 - 46595:00

Python scripts but this like large

## 46595:00 - 46650:00

infrastructure project right

## 46650:00 - 46685:00

even like running tests on it takes a

## 46685:00 - 46720:00

while and so we had to really hook up

## 46720:00 - 46775:00

and give AI access to our CI to be able

## 46775:00 - 46805:00

to trigger things like and do small

## 46805:00 - 46865:00

things of that kind to make the code is

## 46865:00 - 46950:00

friendlier for agents to use. Um I think

## 46950:00 - 47020:00

we use it a lot for code review and

## 47020:00 - 47065:00

we've given extreme experimentation

## 47065:00 - 47095:00

license to every engineer. We don't

## 47095:00 - 47135:00

standardize how people do things like

## 47135:00 - 47165:00

everyone gets to do their own and runs

## 47165:00 - 47190:00

some people are more experimental than

## 47190:00 - 47235:00

others and they experiment with

## 47235:00 - 47275:00

different ways of doing things. So

## 47275:00 - 47300:00

that's the approach we've taken like

## 47300:00 - 47320:00

everything's going to change all the

## 47320:00 - 47370:00

time. We want to be in explore exploit

## 47370:00 - 47415:00

mode constantly rather than like pick

## 47415:00 - 47440:00

our lane and stick to it.

## 47440:00 - 47475:00

>> Where where do you sort of net out in

## 47475:00 - 47515:00

this debate around codegen? I think it's

## 47515:00 - 47530:00

something that people have very

## 47530:00 - 47565:00

different opinions on in terms of what

## 47565:00 - 47600:00

is the role of the software engineer you

## 47600:00 - 47630:00

know sort of in 2025. What does it look

## 47630:00 - 47680:00

like in a couple years? I think a few

## 47680:00 - 47720:00

things will continue to matter right

## 47720:00 - 47760:00

what to build not necessarily how to

## 47760:00 - 47825:00

build it and taste those things I think

## 47825:00 - 47850:00

remain the role I think good software

## 47850:00 - 47900:00

engineers have always had that and I

## 47900:00 - 47930:00

think that will remain the most

## 47930:00 - 47960:00

opinionated stance on this topic that I

## 47960:00 - 47995:00

have is actually that there is a like I

## 47995:00 - 48050:00

our APIs are designed to be declarative

## 48050:00 - 48100:00

what I mean by declarative is talk about

## 48100:00 - 48140:00

what you want the output to be but don't

## 48140:00 - 48175:00

tell me how

## 48175:00 - 48205:00

and I think increasingly that's the

## 48205:00 - 48230:00

direction we will end up in. There will

## 48230:00 - 48295:00

be a I think code we write today is the

## 48295:00 - 48330:00

how

## 48330:00 - 48400:00

the conversations that we have with our

## 48400:00 - 48450:00

AI agents and code agents

## 48450:00 - 48500:00

are essentially trying to communicate

## 48500:00 - 48540:00

through both a combination

## 48540:00 - 48605:00

of feedback and don't do this and how

## 48605:00 - 48635:00

actually agreeing on the what we're

## 48635:00 - 48685:00

trying to do but we're not yet agreeing

## 48685:00 - 48715:00

on it or articulating it or storing it

## 48715:00 - 48735:00

in repo.

## 48735:00 - 48760:00

>> Okay. So, I mean, one of the things that

## 48760:00 - 48785:00

we we really like to think about and

## 48785:00 - 48825:00

talk about is companies that are putting

## 48825:00 - 48880:00

AI into production today in in truly

## 48880:00 - 48905:00

valuable ways because people, I think,

## 48905:00 - 48960:00

make all kinds of predictions. Um, and

## 48960:00 - 49000:00

your customers, I think, by definition,

## 49000:00 - 49030:00

are trying to push the limits of

## 49030:00 - 49055:00

technology. So, you have this unique

## 49055:00 - 49095:00

window into what these elite teams are

## 49095:00 - 49150:00

are actually doing today in 2025. How

## 49150:00 - 49205:00

are your customers using AI in ways that

## 49205:00 - 49230:00

are working or doing something that's

## 49230:00 - 49250:00

just really interesting that you think

## 49250:00 - 49275:00

others could learn from?

## 49275:00 - 49320:00

>> I think one of the very hard problems

## 49320:00 - 49380:00

that we don't focus on but our customers

## 49380:00 - 49445:00

are exceptional at is

## 49445:00 - 49490:00

communicating to

## 49490:00 - 49545:00

end humans how to collaborate and

## 49545:00 - 49575:00

partner with the eyes. expectation

## 49575:00 - 49610:00

setting, creating an iteration

## 49610:00 - 49655:00

playground for people to iterate with

## 49655:00 - 49720:00

them, to communicate that the answers

## 49720:00 - 49785:00

aren't always right and do so in a way

## 49785:00 - 49820:00

that makes sense to the customer to

## 49820:00 - 49845:00

communicate what's happening under the

## 49845:00 - 49885:00

hoods as this agent is going out and

## 49885:00 - 49945:00

doing work. Right? I think some of the

## 49945:00 - 50025:00

elite AI teams are really good at having

## 50025:00 - 50055:00

opinionated ways of doing that in

## 50055:00 - 50100:00

different modalities for different

## 50100:00 - 50125:00

customers. That's a common thread we

## 50125:00 - 50165:00

see. I think the other common thread we

## 50165:00 - 50210:00

see with our customers which is probably

## 50210:00 - 50225:00

slightly different from the question

## 50225:00 - 50270:00

you're asking is they're operating in

## 50270:00 - 50320:00

this extreme founder mode. What I mean

## 50320:00 - 50350:00

by that is some of our customers are

## 50350:00 - 50400:00

established companies, you know, BPO.

## 50400:00 - 50425:00

The common thread across all of them

## 50425:00 - 50470:00

that I can pin down is they're super

## 50470:00 - 50500:00

forward-looking, taking risk on their

## 50500:00 - 50530:00

own business,

## 50530:00 - 50565:00

innovating and operating in founder

## 50565:00 - 50610:00

mode. And it's kind of interesting to

## 50610:00 - 50675:00

see. But I do think that is the to me

## 50675:00 - 50745:00

that's sort of how I look at where we

## 50745:00 - 50795:00

will truly co-inovate together

## 50795:00 - 50825:00

is that

## 50825:00 - 50875:00

>> on the flip side, what what mistakes do

## 50875:00 - 50920:00

you see companies making when they try

## 50920:00 - 50945:00

to put AI into production or what is

## 50945:00 - 50990:00

failing? What is not working? I think we

## 50990:00 - 51030:00

at parallel

## 51030:00 - 51110:00

fail to be great at helping everyone

## 51110:00 - 51155:00

measure quality. I think eval are just

## 51155:00 - 51180:00

like a famously hard problem and you can

## 51180:00 - 51210:00

build all kinds of general purpose evals

## 51210:00 - 51265:00

or eval

## 51265:00 - 51310:00

cases but each customer scenario is

## 51310:00 - 51340:00

different

## 51340:00 - 51370:00

and the eval is actually constantly

## 51370:00 - 51395:00

changing

## 51395:00 - 51490:00

and I think we haven't yet dialed in how

## 51490:00 - 51550:00

we can help people understand quality

## 51550:00 - 51590:00

communicate it from us to our customers

## 51590:00 - 51625:00

and from them to their customers when

## 51625:00 - 51660:00

that is the case and I think that is

## 51660:00 - 51720:00

still a thing that there is a lot to

## 51720:00 - 51795:00

innovate on in order to understand when

## 51795:00 - 51840:00

AI works and when it doesn't work and

## 51840:00 - 51880:00

when to use it when not to use it and I

## 51880:00 - 51930:00

think that's partly our burden to solve

## 51930:00 - 51970:00

and I don't think we have nailed that

## 51970:00 - 51980:00

yet.

## 51980:00 - 52015:00

>> Do you have ideas on on what that might

## 52015:00 - 52065:00

look like? We want to automate in some

## 52065:00 - 52120:00

sense and estimate outputs of eval like

## 52120:00 - 52165:00

I think the estimation problem is easier

## 52165:00 - 52250:00

than the the actual evaluating problem.

## 52250:00 - 52290:00

And so I think we do do that some of

## 52290:00 - 52325:00

that internally to identify cases where

## 52325:00 - 52355:00

we didn't do a good job. We build

## 52355:00 - 52395:00

regression tests internally. None of

## 52395:00 - 52440:00

those things yet for us are working well

## 52440:00 - 52480:00

enough that we can establish a customer

## 52480:00 - 52505:00

contract around that. But we'd like to,

## 52505:00 - 52550:00

right? You want to be able to establish

## 52550:00 - 52590:00

a customer contract around your quality

## 52590:00 - 52625:00

which is relevant to them and material

## 52625:00 - 52635:00

for them.

## 52635:00 - 52660:00

>> Yeah, it's true. It's not something that

## 52660:00 - 52695:00

really there's a standard way of

## 52695:00 - 52735:00

measuring. if you are a customer and

## 52735:00 - 52765:00

you're you're you know expecting some

## 52765:00 - 52790:00

level of quality out of the AI that

## 52790:00 - 52805:00

you're using

## 52805:00 - 52835:00

>> and I think if we unlock that right like

## 52835:00 - 52930:00

then you will actually access a large

## 52930:00 - 52970:00

large amount of use cases and actual

## 52970:00 - 53020:00

customers who might today be slightly

## 53020:00 - 53080:00

skeptical who might have been burnt by

## 53080:00 - 53135:00

trying things that didn't work who might

## 53135:00 - 53210:00

want a higher quality SLA but don't even

## 53210:00 - 53265:00

know how to measure it or ask for it or

## 53265:00 - 53300:00

know when it's there or not there.

## 53300:00 - 53355:00

>> So the word agent I think is one of the

## 53355:00 - 53400:00

most overused words that I hear at

## 53400:00 - 53460:00

least. What are agents actually doing

## 53460:00 - 53500:00

that is truly useful that that you see

## 53500:00 - 53530:00

kind of dayto-day and and maybe what do

## 53530:00 - 53555:00

you think that looks like 2 years from

## 53555:00 - 53625:00

now? I used to joke that agents is code

## 53625:00 - 53665:00

for something that is slow, but really I

## 53665:00 - 53700:00

think that there's now a much more clear

## 53700:00 - 53740:00

definition of agents. So I I'm actually

## 53740:00 - 53775:00

starting to embrace the term. I think

## 53775:00 - 53825:00

it's when you allow the AI to have

## 53825:00 - 53850:00

agency

## 53850:00 - 53885:00

to

## 53885:00 - 53940:00

make decisions around

## 53940:00 - 53985:00

how it wants to solve a problem and have

## 53985:00 - 54040:00

access to a collection of tools in order

## 54040:00 - 54090:00

to that. and don't constrain it too much

## 54090:00 - 54140:00

and allow for many different paths to

## 54140:00 - 54190:00

occur in order to achieve an end state.

## 54190:00 - 54220:00

I think that's a reasonable definition

## 54220:00 - 54260:00

of agent. I think the obvious thing is

## 54260:00 - 54295:00

agent doing small contained coding

## 54295:00 - 54370:00

projects work and they don't always work

## 54370:00 - 54420:00

but they work a lot more than I thought

## 54420:00 - 54495:00

they would two years ago. Um and so I

## 54495:00 - 54540:00

think that is the case that it works. I

## 54540:00 - 54605:00

think agents like our agents if I may I

## 54605:00 - 54645:00

think they work surprisingly well in

## 54645:00 - 54685:00

many many use cases and they're not too

## 54685:00 - 54735:00

different in terms of sort of the

## 54735:00 - 54765:00

reliability as you might expect relative

## 54765:00 - 54790:00

to the coding agent. So I think that

## 54790:00 - 54850:00

sort of deep web research doing work

## 54850:00 - 54890:00

over the open web kind of use cases I

## 54890:00 - 54915:00

think they're working.

## 54915:00 - 54965:00

>> What do you think the parallel APIs do

## 54965:00 - 55010:00

exceptionally well today? And then what

## 55010:00 - 55030:00

are the things that you're thinking

## 55030:00 - 55070:00

about that you that where you want to

## 55070:00 - 55105:00

invest in and improve and you know the

## 55105:00 - 55140:00

parallel of 2026 2027

## 55140:00 - 55175:00

>> parallel APIs are really good at the

## 55175:00 - 55240:00

highest quality web research. The second

## 55240:00 - 55300:00

thing we do really well is really good

## 55300:00 - 55370:00

attribution down to specific sources

## 55370:00 - 55405:00

from which web research was done in a

## 55405:00 - 55455:00

very fine grained granular way and that

## 55455:00 - 55500:00

allows us to build a differentiator

## 55500:00 - 55555:00

which is confidence scoring for all of

## 55555:00 - 55620:00

our output elements. So our system is

## 55620:00 - 55670:00

calibrated to know when we might have

## 55670:00 - 55720:00

gotten some answers wrong.

## 55720:00 - 55755:00

And I think that's been like a core

## 55755:00 - 55805:00

thing for us and it's a core need for a

## 55805:00 - 55850:00

lot of our customers because they want

## 55850:00 - 55925:00

to trust the AI and we want to measure

## 55925:00 - 55950:00

the performance of our AI. We want to

## 55950:00 - 55970:00

figure out where to allocate more

## 55970:00 - 56020:00

compute and retrieval money as we're

## 56020:00 - 56060:00

doing research. And for all of these

## 56060:00 - 56100:00

things, knowing when you're more likely

## 56100:00 - 56150:00

to be wrong is really important. And

## 56150:00 - 56185:00

we've spent a lot of time doing that.

## 56185:00 - 56230:00

And but that also shows up as something

## 56230:00 - 56265:00

that is a value prop for customers.

## 56265:00 - 56310:00

>> So continuing on the the agent threat,

## 56310:00 - 56330:00

what what do you think kind of the

## 56330:00 - 56375:00

modern agentic stack looks like and and

## 56375:00 - 56425:00

why are web tools such an essential part

## 56425:00 - 56440:00

of that?

## 56440:00 - 56470:00

>> If you think about I think knowledge

## 56470:00 - 56500:00

work is overused but it's useful to

## 56500:00 - 56525:00

think about like I think if you think

## 56525:00 - 56575:00

about work and an agent either doing it

## 56575:00 - 56605:00

for you or helping you be more

## 56605:00 - 56645:00

productive, right?

## 56645:00 - 56705:00

There is a expectation in the I believe

## 56705:00 - 56740:00

every piece of software we use whether

## 56740:00 - 56800:00

or not it's an agent must use some form

## 56800:00 - 56840:00

of an advanced AI like an LLM or some

## 56840:00 - 56890:00

multimodal version of it and I think if

## 56890:00 - 56945:00

you're doing that it's almost silly to

## 56945:00 - 56990:00

not have access to the web and so the

## 56990:00 - 57030:00

expectation very soon for every piece of

## 57030:00 - 57075:00

software we interact with is going to be

## 57075:00 - 57110:00

that it has access to an LM it has

## 57110:00 - 57140:00

access to the

## 57140:00 - 57175:00

If you now think about building and

## 57175:00 - 57205:00

that's why we want to be the web tool

## 57205:00 - 57245:00

but now if you zoom into the agents

## 57245:00 - 57310:00

right you think of any agent inside a

## 57310:00 - 57335:00

work environment let's say forgetting

## 57335:00 - 57385:00

personal agents for a moment it must

## 57385:00 - 57450:00

have access to all kinds of internal

## 57450:00 - 57505:00

tools and data in that enterprise

## 57505:00 - 57565:00

it must have access to the web

## 57565:00 - 57600:00

perhaps must have access to because

## 57600:00 - 57625:00

they're so good at coding

## 57625:00 - 57670:00

to a sandbox where it can write and run

## 57670:00 - 57715:00

code, right? And you can come up with a

## 57715:00 - 57745:00

few other tools it needs, but I think

## 57745:00 - 57790:00

that's like those are the top three,

## 57790:00 - 57820:00

right? Access to the web, access to

## 57820:00 - 57865:00

internal data, access to code sandbox,

## 57865:00 - 57880:00

and then you can have a tool number

## 57880:00 - 57905:00

four, you can have a tool number five,

## 57905:00 - 57960:00

but and we're building the web too. And

## 57960:00 - 57990:00

when you think about agents interacting

## 57990:00 - 58040:00

with the web at scale, what are some of

## 58040:00 - 58065:00

the hard problems that most people

## 58065:00 - 58110:00

haven't even realized yet? So many hard

## 58110:00 - 58175:00

problems up and down the stack. So one

## 58175:00 - 58240:00

there is a hard problem

## 58240:00 - 58310:00

on data access. How do we incentive

## 58310:00 - 58355:00

align the business model and the

## 58355:00 - 58400:00

economics of this future web where

## 58400:00 - 58440:00

there's agents, right? We only deal with

## 58440:00 - 58485:00

open data. uh and I think there is a

## 58485:00 - 58530:00

existential risk on the web that the web

## 58530:00 - 58575:00

might close up more and more unless we

## 58575:00 - 58630:00

figure out and solve problems in a way

## 58630:00 - 58665:00

that incentivizes

## 58665:00 - 58725:00

this data to remain open and it must be

## 58725:00 - 58760:00

optimal for most people for putting

## 58760:00 - 58795:00

their content, their ideas, their

## 58795:00 - 58820:00

products or whatever it is they publish

## 58820:00 - 58865:00

on the web out there that they should be

## 58865:00 - 58930:00

able to add maximal value and actually

## 58930:00 - 58965:00

sustain their businesses. goals,

## 58965:00 - 59005:00

whatever they might be, economics, and

## 59005:00 - 59060:00

it must be better for their goals to be

## 59060:00 - 59120:00

open rather than pay wall or closed.

## 59120:00 - 59185:00

And that it's not obvious that that will

## 59185:00 - 59215:00

happen. And that's why we want to show

## 59215:00 - 59250:00

up and we want to pave the path for that

## 59250:00 - 59305:00

being the way the web ends up, which is

## 59305:00 - 59345:00

incentive to remain open through open

## 59345:00 - 59405:00

markets rather than incentives to close

## 59405:00 - 59440:00

up shop. you have all of this very

## 59440:00 - 59490:00

valuable proprietary data that that

## 59490:00 - 59520:00

understandably the producers of that

## 59520:00 - 59575:00

data want to monetize in some way. Do

## 59575:00 - 59605:00

you have an idea for sort of how this

## 59605:00 - 59640:00

all gets sorted out in the coming years?

## 59640:00 - 59675:00

I can talk about a few properties and

## 59675:00 - 59720:00

reasons for believing.

## 59720:00 - 59780:00

One property is I believe we will add so

## 59780:00 - 59825:00

much value through OIS. Going back to

## 59825:00 - 59855:00

the theme of positive sum that there's

## 59855:00 - 59895:00

going to be so much surplus that we have

## 59895:00 - 59920:00

to embrace the world where we are able

## 59920:00 - 59985:00

to share and drive collaboration instead

## 59985:00 - 60045:00

of creating gates. So when you have the

## 60045:00 - 60080:00

pie getting larger, you can actually

## 60080:00 - 60105:00

figure out ways of getting people to

## 60105:00 - 60140:00

collaborate. So we have that moment

## 60140:00 - 60175:00

today where to everyone it is obvious

## 60175:00 - 60225:00

that the pi can get larger and we need

## 60225:00 - 60265:00

to take that mindset. That's one reason

## 60265:00 - 60310:00

for believing. Um another property

## 60310:00 - 60345:00

that's interesting is when you think

## 60345:00 - 60390:00

about information

## 60390:00 - 60440:00

what ads did really well right was

## 60440:00 - 60475:00

differential pricing at scale and

## 60475:00 - 60515:00

efficiency. What does that mean? It

## 60515:00 - 60575:00

means that most ad supported businesses

## 60575:00 - 60620:00

no matter how you look at it queries

## 60620:00 - 60675:00

users are widely accessible to everyone

## 60675:00 - 60745:00

extremely subsidized and free like but

## 60745:00 - 60790:00

they make money from a small fraction of

## 60790:00 - 60845:00

users which allows them to be accessible

## 60845:00 - 60905:00

to a wide wide wide swath of users right

## 60905:00 - 60935:00

and they lose money on a large number of

## 60935:00 - 60970:00

users but that's how the business works

## 60970:00 - 61005:00

is differential pricing end of the

## 61005:00 - 61030:00

And I think we need to bring in that

## 61030:00 - 61055:00

property

## 61055:00 - 61105:00

into getting people publishing on the

## 61105:00 - 61170:00

web. Very simple example, if you consume

## 61170:00 - 61205:00

someone's content

## 61205:00 - 61235:00

through some really expensive model and

## 61235:00 - 61305:00

spend like $4 in GPU to get to some work

## 61305:00 - 61360:00

done at first round versus my retired

## 61360:00 - 61390:00

dad

## 61390:00 - 61445:00

just reading the news through that. I'd

## 61445:00 - 61500:00

like for you to subsidize

## 61500:00 - 61530:00

that so you shouldn't have to pay the

## 61530:00 - 61555:00

exact same for the same content and if

## 61555:00 - 61585:00

we built market mechanics which were

## 61585:00 - 61640:00

open and allowed us to have the context.

## 61640:00 - 61680:00

>> So the same content being used by

## 61680:00 - 61710:00

different people who have different sort

## 61710:00 - 61740:00

of thresholds of of valuing that

## 61740:00 - 61765:00

content. Yeah, we need differential

## 61765:00 - 61800:00

pricing and we need scalable market

## 61800:00 - 61865:00

mechanics to figure this out and we've

## 61865:00 - 61900:00

done some part of the reason we do so

## 61900:00 - 61930:00

much attribution down to sources is to

## 61930:00 - 61965:00

be able to do that math to be able to

## 61965:00 - 62005:00

understand feasibility. We really want

## 62005:00 - 62065:00

to create open solutions where everyone

## 62065:00 - 62120:00

has incentive to remain open and we'll

## 62120:00 - 62155:00

all be beneficiaries of a web that is

## 62155:00 - 62185:00

open for AIS to use it.

## 62185:00 - 62210:00

>> Incredibly interesting idea. How do you

## 62210:00 - 62235:00

how do you get started on something like

## 62235:00 - 62265:00

this? Like is this something where where

## 62265:00 - 62315:00

Parallel would go and find certain uh

## 62315:00 - 62340:00

corpuses of data that you thought were

## 62340:00 - 62365:00

super interesting and but that were that

## 62365:00 - 62400:00

you'd have to pay for as a way of

## 62400:00 - 62420:00

starting to figure this out?

## 62420:00 - 62455:00

>> Yes. But also like even when we didn't

## 62455:00 - 62485:00

have to pay for it, we would like to

## 62485:00 - 62525:00

incentivize people proactively sharing

## 62525:00 - 62565:00

it with us and to recognize their

## 62565:00 - 62605:00

contribution and pay for it. So we want

## 62605:00 - 62655:00

to truly go build this open marketplace

## 62655:00 - 62715:00

and it'll require us to find partners

## 62715:00 - 62750:00

and find innovators, find people who

## 62750:00 - 62810:00

will take some risk as we learn the math

## 62810:00 - 62870:00

together uh and share in a vision of a

## 62870:00 - 62930:00

future open web and are able to see it

## 62930:00 - 62960:00

that way. And I think if we pull the

## 62960:00 - 63010:00

right partners from the AI world and the

## 63010:00 - 63065:00

web publishing side, I think it's

## 63065:00 - 63110:00

possible. So, Prague, let's uh maybe

## 63110:00 - 63150:00

wrap up on a couple personal questions.

## 63150:00 - 63185:00

What are some of the topics that you're

## 63185:00 - 63230:00

going really deep on now personally and

## 63230:00 - 63265:00

kind of geeking out on? I'm just geeking

## 63265:00 - 63315:00

out on the web just all the time. U but

## 63315:00 - 63350:00

outside of this like I think I'm I think

## 63350:00 - 63385:00

the future

## 63385:00 - 63420:00

web index

## 63420:00 - 63475:00

and how it will get built. So, I read a

## 63475:00 - 63510:00

lot of research papers, talked to a lot

## 63510:00 - 63540:00

of AI researchers.

## 63540:00 - 63570:00

We'll build a research team and I think

## 63570:00 - 63605:00

there is a very interesting set of

## 63605:00 - 63650:00

things to be done there. So that's the

## 63650:00 - 63675:00

current geek out obsession. It's

## 63675:00 - 63690:00

material to my company.

## 63690:00 - 63715:00

>> What are are there interesting papers

## 63715:00 - 63750:00

that you've read or like interesting

## 63750:00 - 63780:00

kind of new thoughts that you've had?

## 63780:00 - 63820:00

>> My worldview is currently shaped shaping

## 63820:00 - 63860:00

into a convergence between

## 63860:00 - 63895:00

recommendation systems and search

## 63895:00 - 63940:00

systems and database systems. I think

## 63940:00 - 63975:00

they're all going to start looking like

## 63975:00 - 64015:00

the same thing. And what are the things

## 64015:00 - 64045:00

that you're thinking about again

## 64045:00 - 64100:00

personally in terms of leveling up as an

## 64100:00 - 64140:00

incredible founder, CEO?

## 64140:00 - 64160:00

>> I used to say this thing at Twitter. I

## 64160:00 - 64190:00

don't know if you ever heard it that

## 64190:00 - 64230:00

like I only want to do jobs that I

## 64230:00 - 64280:00

wouldn't hire myself for. And I think

## 64280:00 - 64330:00

it's like I do best when I'm slightly

## 64330:00 - 64375:00

uncomfortable, insecure, don't feel up

## 64375:00 - 64440:00

to it. And that's part of why I wanted

## 64440:00 - 64485:00

to be a founder because I it's it's it's

## 64485:00 - 64505:00

the kind of job that makes you feel that

## 64505:00 - 64540:00

way. Great thing is it like makes you

## 64540:00 - 64605:00

feel that way no matter where you are in

## 64605:00 - 64625:00

the founding journey. Like you're

## 64625:00 - 64660:00

constantly

## 64660:00 - 64695:00

underqualified

## 64695:00 - 64755:00

to be what your aspiration, ambition,

## 64755:00 - 64805:00

and company needs from you. Right? So

## 64805:00 - 64830:00

today, if I have to think about like

## 64830:00 - 64900:00

where I need to really level up, it's in

## 64900:00 - 64945:00

simplifying what we're doing. It's in

## 64945:00 - 64995:00

communicating what we're doing. It's in

## 64995:00 - 65030:00

expanding

## 65030:00 - 65075:00

the coalition we're building towards the

## 65075:00 - 65140:00

open web towards the set of customers.

## 65140:00 - 65175:00

Like our coalition is our customers. And

## 65175:00 - 65220:00

I think there is just so much to be done

## 65220:00 - 65270:00

in doing that. Every day I feel like I

## 65270:00 - 65315:00

got a third of what I wanted to get done

## 65315:00 - 65345:00

despite like having so many AIs at my

## 65345:00 - 65355:00

disposal.

## 65355:00 - 65380:00

>> Well, Prague, thank you. This has been

## 65380:00 - 65410:00

an incredibly interesting conversation.

## 65410:00 - 65440:00

I enjoyed it immensely. So, thank you

## 65440:00 - 65500:00

for being with us.

## 65500:00+

[Music]

