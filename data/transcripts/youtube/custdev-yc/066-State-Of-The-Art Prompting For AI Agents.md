---
source: https://www.youtube.com/watch?v=DL82mGde6wo
title: State-Of-The-Art Prompting For AI Agents
author: Y Combinator
date: 2025-05-30
views: 329953
description: >-
  At first, prompting seemed to be a temporary workaround for getting the most
  out of large language models. But over time, it's become critical to the way
  we interact with AI.


  On the Lightcone, Garry, Harj, Diana, and Jared break down what they've
  learned from working with hundreds of founders building with LLMs: why
  prompting still matters, where it breaks down, and how teams are making it
  more reliable in production.


  They share real examples of prompts that failed, how companies are testing for
  quality, and what the best teams are doing to make LLM outputs useful and
  predictable.


  The prompt from Parahelp (S24) discussed in the episode:
  https://parahelp.com/blog/prompt-design


  Apply to Y Combinator: https://ycombinator.com/apply

  Work at a startup: https://workatastartup.com


  Chapters (Powered by https://chapterme.co/) -

  0:00 Intro

  0:58 Parahelp’s prompt example

  4:59 Different types of prompts

  6:51 Metaprompting 

  7:58 Using examples

  12:10 Some tricks for longer prompts

  14:18 Findings on evals

  17:25 Every founder has become a forward deployed engineer (FDE)

  23:18 Vertical AI agents are closing big deals with the FDE model 

  26:13 The personalities of the different LLMs

  27:26 Lessons from rubrics

  29:47 Kaizen and the art of communication

  31:00 Outro
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:45:34.406Z
---

# State-Of-The-Art Prompting For AI Agents

## 00:00 - 30:00

Metarprompting is turning out to be a

## 30:00 - 60:00

very very powerful tool that everyone's

## 60:00 - 90:00

using now. It kind of actually feels

## 90:00 - 150:00

like coding in you know 1995 like the

## 150:00 - 185:00

tools are not all the way there. We're

## 185:00 - 220:00

you know in this new frontier. But

## 220:00 - 255:00

personally it also kind of feels like

## 255:00 - 290:00

learning how to manage a person where

## 290:00 - 335:00

it's like how do I actually communicate

## 335:00 - 365:00

uh you know the things that they need to

## 365:00 - 435:00

know in order to make a good decision.

## 435:00 - 540:00

[Music]

## 540:00 - 570:00

Welcome back to another episode of the

## 570:00 - 610:00

light cone. Today we're pulling back the

## 610:00 - 655:00

curtain on what is actually happening

## 655:00 - 705:00

inside the best AI startups when it

## 705:00 - 745:00

comes to prompt engineering. We surveyed

## 745:00 - 795:00

more than a dozen companies and got

## 795:00 - 845:00

their take right from the frontier of

## 845:00 - 890:00

building this stuff, the practical tips.

## 890:00 - 915:00

Jared, why don't we start with an

## 915:00 - 950:00

example from one of your best AI

## 950:00 - 995:00

startups? I managed to get an example

## 995:00 - 1035:00

from a company called Parahelp. Parahelp

## 1035:00 - 1075:00

does AI customer support. There are a

## 1075:00 - 1090:00

bunch of companies who who are doing

## 1090:00 - 1110:00

this, but Parhel is doing it really

## 1110:00 - 1140:00

really well. They're actually powering

## 1140:00 - 1180:00

the customer support for Perplexity and

## 1180:00 - 1215:00

Replet and Bolt and a bunch of other

## 1215:00 - 1250:00

like top AI companies now. So, if you if

## 1250:00 - 1275:00

you go and you like email a customer

## 1275:00 - 1305:00

support ticket into Perplexity, what's

## 1305:00 - 1330:00

actually responding is like their AI

## 1330:00 - 1360:00

agent. The cool thing is that the

## 1360:00 - 1390:00

Powerhel guys very graciously agreed to

## 1390:00 - 1435:00

show us the actual prompt that is

## 1435:00 - 1470:00

powering this agent um and to put it on

## 1470:00 - 1495:00

screen on YouTube for the entire world

## 1495:00 - 1530:00

to see. Um it's like relatively hard to

## 1530:00 - 1560:00

get these prompts for vertical AI agents

## 1560:00 - 1580:00

because they're kind of like the crown

## 1580:00 - 1615:00

jewels of the IP of these companies and

## 1615:00 - 1645:00

so very grateful to the Powerhel guys

## 1645:00 - 1665:00

for agreeing to basically like open

## 1665:00 - 1705:00

source this prompt. Diana, can you walk

## 1705:00 - 1745:00

us through this very detailed prompt?

## 1745:00 - 1770:00

It's super interesting and it's very

## 1770:00 - 1800:00

rare to get a chance to see this in

## 1800:00 - 1825:00

action. So the interesting thing about

## 1825:00 - 1850:00

this prompt is actually first it's

## 1850:00 - 1885:00

really long. It's very detailed in this

## 1885:00 - 1925:00

document you can see is like six pages

## 1925:00 - 1960:00

long just scrolling through it. The big

## 1960:00 - 1990:00

thing that a lot of the best prompts

## 1990:00 - 2035:00

start with is this concept of uh setting

## 2035:00 - 2080:00

up the role of the LLM. You're a manager

## 2080:00 - 2120:00

of a customer service agent and it

## 2120:00 - 2155:00

breaks down into bullet points what it

## 2155:00 - 2190:00

needs to do. Then the big thing is

## 2190:00 - 2235:00

telling the the task which is to approve

## 2235:00 - 2270:00

or reject a tool call because it's

## 2270:00 - 2300:00

orchestrating agent calls from all these

## 2300:00 - 2355:00

other ones. And then it gives it a bit

## 2355:00 - 2395:00

of the highle plan. It breaks it down

## 2395:00 - 2430:00

step by step. You see steps one, two,

## 2430:00 - 2470:00

three, four, five. And then it gives

## 2470:00 - 2500:00

some of the important things to keep in

## 2500:00 - 2575:00

mind that it should not kind of go weird

## 2575:00 - 2610:00

into calling different kinds of tools.

## 2610:00 - 2635:00

It tells them how to structure the

## 2635:00 - 2670:00

output because a lot of things with

## 2670:00 - 2710:00

agents is you need them to integrate

## 2710:00 - 2745:00

with other agents. So almost like gluing

## 2745:00 - 2790:00

the API call. So the is important to

## 2790:00 - 2830:00

specify that it's going to give certain

## 2830:00 - 2870:00

uh output of accepting or rejecting and

## 2870:00 - 2895:00

in this format. Then this is sort of the

## 2895:00 - 2945:00

highle section and one thing that the

## 2945:00 - 2980:00

best prompts do they break it down sort

## 2980:00 - 3020:00

of in this markdown type of style uh

## 3020:00 - 3045:00

formatting. So you have sort of the

## 3045:00 - 3090:00

heading here and then later on it goes

## 3090:00 - 3125:00

into more details on how to do the

## 3125:00 - 3155:00

planning and you see this is like a sub

## 3155:00 - 3195:00

bullet part of it and as part of the

## 3195:00 - 3230:00

plan there's actually three big sections

## 3230:00 - 3275:00

is how to plan and then how to create

## 3275:00 - 3315:00

each of the steps in the plan and then

## 3315:00 - 3360:00

the highle example of the plan. One big

## 3360:00 - 3400:00

thing about the best prompts is they

## 3400:00 - 3455:00

outline how to reason about the task and

## 3455:00 - 3490:00

then a big thing is giving it giving it

## 3490:00 - 3530:00

an example and this is what it does. And

## 3530:00 - 3565:00

one thing that's interesting about this

## 3565:00 - 3600:00

it it looks more like programming than

## 3600:00 - 3645:00

writing English because it has this uh

## 3645:00 - 3705:00

XML tag kind of format to specify sort

## 3705:00 - 3745:00

of the plan. We found that it makes it a

## 3745:00 - 3785:00

lot easier for LMS to follow because a

## 3785:00 - 3845:00

lot of LMS were post-trained in LHF with

## 3845:00 - 3890:00

kind of XML type of input and it turns

## 3890:00 - 3930:00

out to produce better results. Yeah. One

## 3930:00 - 3960:00

thing I'm surprised that isn't in here

## 3960:00 - 3985:00

or maybe this is just the version that

## 3985:00 - 4020:00

they released. What I almost expect is

## 4020:00 - 4070:00

there to be a section where it describes

## 4070:00 - 4125:00

a particular scenario and uh actually

## 4125:00 - 4175:00

gives example output for that scenario.

## 4175:00 - 4215:00

That's in like the next stage of the

## 4215:00 - 4260:00

pipeline. Yeah. Oh, really? Okay. Yeah.

## 4260:00 - 4290:00

Because it's customer specific, right?

## 4290:00 - 4310:00

Because like every customer has their

## 4310:00 - 4345:00

own like flavor of how to respond to

## 4345:00 - 4375:00

these support tickets. And so their

## 4375:00 - 4395:00

challenge like a lot of these agent

## 4395:00 - 4425:00

companies is like how do you build a

## 4425:00 - 4470:00

general purpose product when every

## 4470:00 - 4510:00

customer like wants you know has like

## 4510:00 - 4540:00

slightly different workflows and like

## 4540:00 - 4570:00

preferences. has a really interesting

## 4570:00 - 4605:00

thing that I see the vertical AI agent

## 4605:00 - 4630:00

companies talking about a lot which is

## 4630:00 - 4655:00

like how do you have enough flexibility

## 4655:00 - 4690:00

to make special purpose logic without

## 4690:00 - 4715:00

turning into a consulting company where

## 4715:00 - 4745:00

you're building like a new prompt for

## 4745:00 - 4780:00

for for every customer. I actually think

## 4780:00 - 4810:00

this like concept of like forking and

## 4810:00 - 4850:00

merging prompts across customers and

## 4850:00 - 4875:00

which part of the prompt is customer

## 4875:00 - 4910:00

specific versus like companywide is like

## 4910:00 - 4950:00

a like a really interesting thing that

## 4950:00 - 4970:00

the world is only just beginning to

## 4970:00 - 4995:00

explore. Yeah, that's a very good point

## 4995:00 - 5045:00

Jared. So this is concept of uh defining

## 5045:00 - 5085:00

the prompt in the system prompt. Then

## 5085:00 - 5120:00

there's a de developer prompt and then

## 5120:00 - 5165:00

there's a user prompt. So what this mean

## 5165:00 - 5205:00

is uh the system prompt is basically

## 5205:00 - 5250:00

almost like defining uh sort of the

## 5250:00 - 5290:00

highle API of how your company operates.

## 5290:00 - 5320:00

In this case the example of parhel is

## 5320:00 - 5345:00

very much a system prompt. There's

## 5345:00 - 5375:00

nothing specific about the customer. And

## 5375:00 - 5405:00

then as they add specific instances of

## 5405:00 - 5445:00

that API and calling it then they stuff

## 5445:00 - 5485:00

all that in into more the developer

## 5485:00 - 5515:00

prompt which is not shown here and

## 5515:00 - 5550:00

that's adds all the context of let's say

## 5550:00 - 5580:00

working with perplexity there's certain

## 5580:00 - 5620:00

ways of how you handle rack questions as

## 5620:00 - 5665:00

opposed to working with bold is very

## 5665:00 - 5695:00

different right and then I don't think

## 5695:00 - 5735:00

parhelp has a user prompt because their

## 5735:00 - 5765:00

product is not consumed directly by an

## 5765:00 - 5805:00

end user but a end user prompt could be

## 5805:00 - 5875:00

more like replet or a zero right where

## 5875:00 - 5910:00

users need to type is like generate me a

## 5910:00 - 5945:00

site that that has these buttons this

## 5945:00 - 5970:00

and that that goes all in the user

## 5970:00 - 6005:00

prompt. So that's sort of the

## 6005:00 - 6030:00

architecture that's sort of emerging.

## 6030:00 - 6055:00

And to your point about avoiding

## 6055:00 - 6100:00

becoming a consulting company, I think

## 6100:00 - 6145:00

um there's so many startup opportunities

## 6145:00 - 6185:00

and building the tooling around all of

## 6185:00 - 6225:00

this stuff like for example like um

## 6225:00 - 6245:00

anyone who's done prompt engineering

## 6245:00 - 6285:00

knows that the examples and worked

## 6285:00 - 6310:00

examples are really important to

## 6310:00 - 6340:00

improving the quality of the output. And

## 6340:00 - 6370:00

so then if you take like power as an

## 6370:00 - 6420:00

example, they really want good worked

## 6420:00 - 6450:00

examples that are specific to each

## 6450:00 - 6500:00

company. And so you can imagine that as

## 6500:00 - 6535:00

they scale, you almost want that done

## 6535:00 - 6560:00

automatically. Like in your dream world,

## 6560:00 - 6590:00

what you want is just like a an agent

## 6590:00 - 6615:00

itself that can pluck out the best

## 6615:00 - 6660:00

examples from like the customer data set

## 6660:00 - 6695:00

and then software that just like ingests

## 6695:00 - 6730:00

that straight into like wherever it

## 6730:00 - 6760:00

should belong in the pipeline without

## 6760:00 - 6795:00

you having to manually go out and plug

## 6795:00 - 6815:00

that all and ingest it in all of

## 6815:00 - 6845:00

yourself. That's probably a great segue

## 6845:00 - 6880:00

into metaparrompting which is one of the

## 6880:00 - 6895:00

things we want to talk about because

## 6895:00 - 6930:00

that's that's a consistent theme that

## 6930:00 - 6960:00

keeps coming up when we talk to our AI

## 6960:00 - 6995:00

startups. Yeah, Tropier is uh one of the

## 6995:00 - 7020:00

startups I'm working with in the current

## 7020:00 - 7055:00

YC batch and they've really helped

## 7055:00 - 7115:00

people like YC company Ducky do really

## 7115:00 - 7160:00

in-depth understanding and debugging of

## 7160:00 - 7215:00

the prompts and the return values from a

## 7215:00 - 7250:00

multi-stage workflow. And one of the

## 7250:00 - 7270:00

things they figured out is prompt

## 7270:00 - 7305:00

folding. So you know basically one

## 7305:00 - 7355:00

prompt can dynamically generate better

## 7355:00 - 7385:00

versions of itself. So a good example of

## 7385:00 - 7410:00

that is a classifier prompt that

## 7410:00 - 7455:00

generates a specialized prompt based on

## 7455:00 - 7480:00

the previous query. And so you can

## 7480:00 - 7530:00

actually go in take uh the existing

## 7530:00 - 7565:00

prompt that you have and actually feed

## 7565:00 - 7615:00

it more examples where maybe the prompt

## 7615:00 - 7640:00

failed or didn't quite do what you

## 7640:00 - 7680:00

wanted and you can actually instead of

## 7680:00 - 7715:00

you having to go and rewrite the prompt,

## 7715:00 - 7765:00

you just put it into um you know the raw

## 7765:00 - 7815:00

LLM and say help me make this prompt

## 7815:00 - 7860:00

better. And because it knows itself so

## 7860:00 - 7905:00

well, strangely um metaprompting is

## 7905:00 - 7935:00

turning out to be a very very powerful

## 7935:00 - 7970:00

tool that everyone's using now. And the

## 7970:00 - 8010:00

next step after uh you do sort of prompt

## 8010:00 - 8060:00

folding if the task is very complex

## 8060:00 - 8095:00

there's this concept of uh using

## 8095:00 - 8140:00

examples and this is what Jasberry does

## 8140:00 - 8175:00

is one of the companies I'm working with

## 8175:00 - 8205:00

this batch they basically build

## 8205:00 - 8245:00

automatic bug finding in code which is a

## 8245:00 - 8290:00

lot harder and the way they do it is

## 8290:00 - 8320:00

they feed a bunch of really hard

## 8320:00 - 8355:00

examples that only expert programmers

## 8355:00 - 8380:00

could do let's say if you want to find

## 8380:00 - 8415:00

an N plus1 query it's actually hard for

## 8415:00 - 8455:00

today for even like the best LMS to find

## 8455:00 - 8485:00

those and the way to do those is they

## 8485:00 - 8535:00

find parts of the code then they add

## 8535:00 - 8570:00

those into the prompt a meta prompt

## 8570:00 - 8605:00

that's like hey this is an example of n

## 8605:00 - 8655:00

plus1 type of error and then that works

## 8655:00 - 8680:00

it out and I think this pattern of

## 8680:00 - 8730:00

sometimes when it's too hard to even

## 8730:00 - 8765:00

kind of write a pros around it let's

## 8765:00 - 8795:00

just give you an example that turns out

## 8795:00 - 8835:00

to work really well because it helps LM

## 8835:00 - 8895:00

to reason around complicated tasks and

## 8895:00 - 8925:00

steer it better because you can't quite

## 8925:00 - 8960:00

kind of put exact act parameters and

## 8960:00 - 9000:00

it's almost like um unit testing

## 9000:00 - 9025:00

programming in a sense like test-driven

## 9025:00 - 9075:00

development is sort of the LLM v version

## 9075:00 - 9110:00

of that. Yeah. Another thing that trope

## 9110:00 - 9145:00

uh sort of talks about is you know the

## 9145:00 - 9180:00

the model really wants to actually help

## 9180:00 - 9220:00

you so much that if you just tell it

## 9220:00 - 9255:00

give me back output in this particular

## 9255:00 - 9305:00

format even if it doesn't quite have the

## 9305:00 - 9355:00

information it needs it'll actually just

## 9355:00 - 9385:00

tell you what it thinks you want to hear

## 9385:00 - 9430:00

and it's literally a hallucination. So,

## 9430:00 - 9455:00

one thing they discovered is that you

## 9455:00 - 9490:00

actually have to give the LLM's a real

## 9490:00 - 9525:00

escape hatch. You need to tell it if you

## 9525:00 - 9580:00

do not have enough information to say

## 9580:00 - 9630:00

yes or no or make a determination, don't

## 9630:00 - 9685:00

just make it up. Stop and ask me. And

## 9685:00 - 9715:00

that's a very different way to think

## 9715:00 - 9740:00

about it. That's actually something we

## 9740:00 - 9765:00

learned at some of the internal work

## 9765:00 - 9810:00

that we've done with agents at YC where

## 9810:00 - 9860:00

Jared came up with a really inventive

## 9860:00 - 9910:00

way to give the LLM escape patch. Did

## 9910:00 - 9940:00

you want to talk about that? Yeah. So

## 9940:00 - 9975:00

the trope approach is one way to give

## 9975:00 - 10005:00

the LM an escape patch. We came up with

## 10005:00 - 10040:00

a different way which is in the response

## 10040:00 - 10080:00

format to give it the ability to have

## 10080:00 - 10120:00

part of the response be essentially a

## 10120:00 - 10180:00

complaint to you the developer that like

## 10180:00 - 10205:00

you have given it confusing or

## 10205:00 - 10230:00

underspecified information and it

## 10230:00 - 10270:00

doesn't know what to do. And then the

## 10270:00 - 10305:00

nice thing about that is that we just

## 10305:00 - 10345:00

run your LLM like in production with

## 10345:00 - 10380:00

real hoser data and then you can go back

## 10380:00 - 10415:00

and you can look at the outputs that it

## 10415:00 - 10440:00

has given you in that like output

## 10440:00 - 10485:00

parameter. Um we we call it debug info

## 10485:00 - 10520:00

internally. So like we have this like

## 10520:00 - 10545:00

debug info parameter where it's

## 10545:00 - 10585:00

basically reporting to us things that we

## 10585:00 - 10625:00

need to fix about it and it literally

## 10625:00 - 10660:00

ends up being like a to-do list that you

## 10660:00 - 10690:00

the agent developer has to do. It's like

## 10690:00 - 10720:00

really kind of mind-blowing stuff. Yeah.

## 10720:00 - 10745:00

Yeah, I mean just even for hobbyists or

## 10745:00 - 10765:00

people who are interested in playing

## 10765:00 - 10795:00

around for this for personal projects.

## 10795:00 - 10820:00

Like a very simple way to get started

## 10820:00 - 10850:00

with meta prompting is to follow the

## 10850:00 - 10870:00

same structure of the prompt is give it

## 10870:00 - 10905:00

a role and make the role be like you

## 10905:00 - 10935:00

know you're a expert prompt engineer who

## 10935:00 - 10980:00

gives really like detailed um great

## 10980:00 - 11010:00

critiques and advice on how to um

## 11010:00 - 11050:00

improve prompts and give it the prompt

## 11050:00 - 11090:00

that you had in mind and it will spit

## 11090:00 - 11135:00

you back a much a more expanded better

## 11135:00 - 11160:00

prompt and so you can just keep running

## 11160:00 - 11185:00

that loop for a while. Works

## 11185:00 - 11215:00

surprisingly well. I think it's a common

## 11215:00 - 11250:00

pattern sometimes for companies when

## 11250:00 - 11290:00

they need to get um responses from

## 11290:00 - 11315:00

element elements in their product a lot

## 11315:00 - 11355:00

quicker. They do the meta prompting with

## 11355:00 - 11400:00

a bigger beefier model any of the I

## 11400:00 - 11415:00

don't know hundreds of billions of

## 11415:00 - 11465:00

parameter plus models like uh I guess

## 11465:00 - 11575:00

cloud 4 3.7 or your uh GPD 03 and they

## 11575:00 - 11605:00

do this meta prompting and then they

## 11605:00 - 11645:00

have a very good working one that then

## 11645:00 - 11680:00

they use into the distilled model. So

## 11680:00 - 11720:00

they use it on uh for example an FRO and

## 11720:00 - 11765:00

it ends up working pretty well

## 11765:00 - 11805:00

specifically sometimes for uh voice AI

## 11805:00 - 11855:00

agents companies because uh latency is

## 11855:00 - 11915:00

very important to uh get this whole

## 11915:00 - 11950:00

touring test to pass because if you have

## 11950:00 - 11985:00

too much pause be before the agent

## 11985:00 - 12015:00

responds I think humans can detect

## 12015:00 - 12055:00

something is off. So they use a faster

## 12055:00 - 12095:00

model but with a bigger better prompt

## 12095:00 - 12135:00

that was refined from the bigger models.

## 12135:00 - 12160:00

So that's like a common pattern as well.

## 12160:00 - 12200:00

Another again less sophisticated maybe

## 12200:00 - 12250:00

but um like as the prompt gets longer

## 12250:00 - 12285:00

and longer like it becomes a a large

## 12285:00 - 12325:00

working doc um one thing I found useful

## 12325:00 - 12360:00

is as you're using it if you just note

## 12360:00 - 12410:00

down in a Google doc things that you're

## 12410:00 - 12465:00

seeing just um the outputs not being how

## 12465:00 - 12500:00

you want or not ways that you can think

## 12500:00 - 12525:00

of to improve it. you can just write

## 12525:00 - 12590:00

those in note form and then give Gemini

## 12590:00 - 12625:00

Pro like your notes plus the original

## 12625:00 - 12655:00

prompt and ask it to suggest a bunch of

## 12655:00 - 12700:00

edits to the prompt um to incorporate

## 12700:00 - 12725:00

these in well and it does that quite

## 12725:00 - 12775:00

well. The other trick is uh in uh Gemini

## 12775:00 - 12820:00

2.5 Pro if you look at the thinking

## 12820:00 - 12885:00

traces as is uh parsing through uh

## 12885:00 - 12920:00

evaluation you could actually learn a

## 12920:00 - 12960:00

lot about all those misses as well.

## 12960:00 - 12985:00

We've done that internal as well, right?

## 12985:00 - 13010:00

As this is critical because if you're

## 13010:00 - 13050:00

just using Gemini via the API until

## 13050:00 - 13075:00

recently, you did not get the thinking

## 13075:00 - 13110:00

traces and like the thinking traces are

## 13110:00 - 13145:00

like the critical debug information to

## 13145:00 - 13180:00

like understand like what's wrong with

## 13180:00 - 13210:00

your prompt. They just added it to the

## 13210:00 - 13250:00

API. So you can now actually like pipe

## 13250:00 - 13290:00

that back into your developer tools and

## 13290:00 - 13315:00

workflows. Yeah, I think it's an

## 13315:00 - 13370:00

underrated um consequence of Gemini Pro

## 13370:00 - 13405:00

having such long context windows is you

## 13405:00 - 13450:00

can effectively use it like a a ripple.

## 13450:00 - 13475:00

Go sort of like one by one like put your

## 13475:00 - 13500:00

prompt on like one example then

## 13500:00 - 13540:00

literally watch the reasoning trace in

## 13540:00 - 13585:00

real time to figure out like how you can

## 13585:00 - 13610:00

steer it in the direction you want.

## 13610:00 - 13640:00

Jared and the software team at YC has

## 13640:00 - 13690:00

actually built this um you know various

## 13690:00 - 13725:00

forms of workbenches that allow us to

## 13725:00 - 13760:00

like do debug and things like that. But

## 13760:00 - 13805:00

to your point like sometimes it's better

## 13805:00 - 13830:00

just to use

## 13830:00 - 13875:00

gemini.google.com directly and then drag

## 13875:00 - 13925:00

and drop you know literally JSON files

## 13925:00 - 13960:00

and uh you know you don't have to do it

## 13960:00 - 14000:00

in some sort of special container like

## 14000:00 - 14040:00

it you know seems to be totally

## 14040:00 - 14085:00

something that works even directly in

## 14085:00 - 14125:00

you know chat GPT itself. Yeah, this is

## 14125:00 - 14160:00

all stuff. Um, I would give a shout out

## 14160:00 - 14210:00

to YC's head of data, Eric Bacon, who's

## 14210:00 - 14240:00

um, helped us all a lot a lot of this

## 14240:00 - 14280:00

metaparrotting and using Gemini Pro 2.5

## 14280:00 - 14315:00

as a effectively a ripple. What about

## 14315:00 - 14350:00

evals? I mean, we've uh, talked about

## 14350:00 - 14405:00

evals for going on a year now. Um, what

## 14405:00 - 14430:00

are some of the things that founders are

## 14430:00 - 14465:00

discovering? Even though we've been

## 14465:00 - 14490:00

saying this for a year or more now,

## 14490:00 - 14525:00

Gary, I think it's still the case that

## 14525:00 - 14585:00

like evals are the true crown jewel like

## 14585:00 - 14620:00

data asset for all of these companies.

## 14620:00 - 14655:00

Like one one reason that Powerhel was

## 14655:00 - 14690:00

willing to open source the prompt is

## 14690:00 - 14720:00

they told me that they actually don't

## 14720:00 - 14750:00

consider the prompts to be the crown

## 14750:00 - 14785:00

jewels like the evals are the crown

## 14785:00 - 14815:00

jewels because without the evals you

## 14815:00 - 14855:00

don't know why the prompt was written

## 14855:00 - 14900:00

the way that it was. Um and it's very

## 14900:00 - 14935:00

hard to improve it. Yeah. And I I think

## 14935:00 - 14970:00

in abstraction you can think about you

## 14970:00 - 15000:00

know YC funds a lot of companies

## 15000:00 - 15045:00

especially in vertical AI and SAS and

## 15045:00 - 15085:00

then you can't get the eval unless you

## 15085:00 - 15130:00

sitting literally side by side with

## 15130:00 - 15175:00

people who are doing X Y or Z knowledge

## 15175:00 - 15205:00

work. you know, you need to sit next to

## 15205:00 - 15265:00

the tractor sales regional manager and

## 15265:00 - 15295:00

understand, well, you know, this person

## 15295:00 - 15320:00

cares, you know, this is how they get

## 15320:00 - 15350:00

promoted. This is what they care about.

## 15350:00 - 15390:00

This is that person's reward function.

## 15390:00 - 15420:00

And then you know what you're doing is

## 15420:00 - 15455:00

taking these in-person interactions

## 15455:00 - 15495:00

sitting next to someone in Nebraska and

## 15495:00 - 15535:00

then going back to your computer and

## 15535:00 - 15590:00

codifying it into uh very specific evals

## 15590:00 - 15640:00

like this particular user wants this

## 15640:00 - 15675:00

outcome after they you know after this

## 15675:00 - 15710:00

invoice comes in we have to decide

## 15710:00 - 15740:00

whether we're going to honor the you the

## 15740:00 - 15775:00

warranty on this tractor. Like just to

## 15775:00 - 15820:00

take one of one example that's the true

## 15820:00 - 15855:00

value right like you everyone's really

## 15855:00 - 15930:00

worried about um are we just rappers and

## 15930:00 - 15960:00

you know what is going to happen to

## 15960:00 - 15990:00

startups and I think this is literally

## 15990:00 - 16045:00

where the rubber meets the road where um

## 16045:00 - 16080:00

if you you know if you are out there in

## 16080:00 - 16120:00

particular places understanding that

## 16120:00 - 16160:00

user better than anyone else and having

## 16160:00 - 16200:00

the software actually work for those

## 16200:00 - 16240:00

people that's the moat is that is like

## 16240:00 - 16275:00

such a perfect depiction of like what is

## 16275:00 - 16315:00

the core competency required of founders

## 16315:00 - 16345:00

today? Like literally like the thing

## 16345:00 - 16380:00

that you just said like that's your job

## 16380:00 - 16410:00

as a founder of a company like this is

## 16410:00 - 16450:00

to be really good at that thing and like

## 16450:00 - 16480:00

maniacally obsessed with like the

## 16480:00 - 16510:00

details of the regional tractor sales

## 16510:00 - 16540:00

manager workflow. Yeah. And then the

## 16540:00 - 16580:00

wild thing is it's very hard to do like

## 16580:00 - 16610:00

you know how you have you even been to

## 16610:00 - 16650:00

Nebraska you know the classic view is

## 16650:00 - 16680:00

that uh the best founders in the world

## 16680:00 - 16715:00

they're you know sort of really great

## 16715:00 - 16765:00

cracked engineers and technologists and

## 16765:00 - 16805:00

uh just really brilliant and then at the

## 16805:00 - 16845:00

same time they have to understand some

## 16845:00 - 16875:00

part of the world that very few people

## 16875:00 - 16910:00

understand and then there's this little

## 16910:00 - 16960:00

sliver that is you know uh the founder

## 16960:00 - 17005:00

of a multi-billion dollar startup you

## 17005:00 - 17030:00

know I think of Ryan Peterson from

## 17030:00 - 17075:00

Flexport, you know, really really great

## 17075:00 - 17105:00

person who understands how software is

## 17105:00 - 17145:00

built, but then also I think he was the

## 17145:00 - 17200:00

third biggest uh importer of medical hot

## 17200:00 - 17245:00

tubs for an entire year like you know a

## 17245:00 - 17290:00

decade ago. So you know the weirder that

## 17290:00 - 17320:00

is the more of the world that you've

## 17320:00 - 17345:00

seen that nobody else who's a

## 17345:00 - 17390:00

technologist has seen uh the greater the

## 17390:00 - 17430:00

opportunity actually. I think you've put

## 17430:00 - 17450:00

this in a really interesting way before

## 17450:00 - 17465:00

Gary where you're sort of saying that

## 17465:00 - 17495:00

every founder's become a forward

## 17495:00 - 17525:00

deployed engineer. That's like a term

## 17525:00 - 17555:00

that traces back to Palunteer and since

## 17555:00 - 17590:00

you were early at Palanteer maybe tell

## 17590:00 - 17615:00

us a little bit about how did forward

## 17615:00 - 17645:00

deployed engineer become a thing at

## 17645:00 - 17670:00

Palunteer and and what can founders

## 17670:00 - 17695:00

learn from it now? I mean I think the

## 17695:00 - 17725:00

whole thesis of Palunteer at some level

## 17725:00 - 17775:00

was that um if you look at Meta back

## 17775:00 - 17825:00

then it was called Facebook or Google or

## 17825:00 - 17875:00

any of the top software startups that

## 17875:00 - 17910:00

everyone sort of knew back then. One of

## 17910:00 - 17960:00

the key recognitions that Peter Teal and

## 17960:00 - 18000:00

Alex Karp and Stefan Cohen and Joe

## 18000:00 - 18025:00

Lansdale, Nathan Gettings, like the

## 18025:00 - 18065:00

original founders of Palunteer had was

## 18065:00 - 18120:00

that uh go into anywhere in the Fortune

## 18120:00 - 18180:00

500, go into any government agency in

## 18180:00 - 18225:00

the world, including the United States,

## 18225:00 - 18275:00

and nobody who understands computer

## 18275:00 - 18320:00

science and technology at the level that

## 18320:00 - 18355:00

you at the highest possible level would

## 18355:00 - 18390:00

ever even be in that room. And so

## 18390:00 - 18430:00

Palenteer's sort of really really big

## 18430:00 - 18470:00

idea that they discovered very early was

## 18470:00 - 18510:00

that uh the problems that those places

## 18510:00 - 18555:00

face they're actually multi-billion

## 18555:00 - 18585:00

dollar sometimes trillion dollar

## 18585:00 - 18630:00

problems and yet uh this was well before

## 18630:00 - 18670:00

AI became a thing you know I mean people

## 18670:00 - 18690:00

were sort of talking about machine

## 18690:00 - 18725:00

learning but you know back then they

## 18725:00 - 18750:00

called it data mining you know the world

## 18750:00 - 18790:00

is a wash in data these you know giant

## 18790:00 - 18825:00

databases of people and things and

## 18825:00 - 18875:00

transactions and we have no idea what to

## 18875:00 - 18910:00

do with it. That's what Palanteer was,

## 18910:00 - 18965:00

is and still is. That um you can go and

## 18965:00 - 19005:00

find the world's best technologists who

## 19005:00 - 19055:00

know how to write software to actually

## 19055:00 - 19080:00

make sense of the world. You know, you

## 19080:00 - 19125:00

have these pabytes of data and you don't

## 19125:00 - 19150:00

know how do you find the needle in the

## 19150:00 - 19185:00

haststack. Um and you know the wild

## 19185:00 - 19240:00

thing is going on uh something like 20

## 19240:00 - 19290:00

22 years later it's only become more

## 19290:00 - 19335:00

true that we have more and more data and

## 19335:00 - 19360:00

we have less and less of an

## 19360:00 - 19400:00

understanding of what's going on and uh

## 19400:00 - 19445:00

it's no mistake that actually now that

## 19445:00 - 19485:00

we have LLMs like we actually it is

## 19485:00 - 19520:00

becoming much more tractable and then

## 19520:00 - 19560:00

the forward deployed engineer title was

## 19560:00 - 19595:00

specifically how do you sit next to

## 19595:00 - 19660:00

literally the FBI agent who's um

## 19660:00 - 19690:00

investigating domestic terrorism. How do

## 19690:00 - 19725:00

you sit right next to them in their

## 19725:00 - 19760:00

actual office and see what does the case

## 19760:00 - 19790:00

coming in look like? What are all the

## 19790:00 - 19835:00

steps? Uh when you actually need to go

## 19835:00 - 19870:00

to the federal prosecutor, what are the

## 19870:00 - 19905:00

things that they're sending? Is it I

## 19905:00 - 19935:00

mean what's funny is like literally it's

## 19935:00 - 19965:00

like word documents and Excel

## 19965:00 - 20005:00

spreadsheets, right? And um what you do

## 20005:00 - 20045:00

as a forward deployed engineer is take

## 20045:00 - 20090:00

these sort of you know file cabinet and

## 20090:00 - 20125:00

fax machine things that people have to

## 20125:00 - 20175:00

do and then convert it into really clean

## 20175:00 - 20215:00

software. So you know the classic view

## 20215:00 - 20250:00

is that it should be as easy to actually

## 20250:00 - 20300:00

do uh an investigation at a threeletter

## 20300:00 - 20335:00

agency as going and taking a photo of

## 20335:00 - 20365:00

your lunch on Instagram and posting it

## 20365:00 - 20395:00

to all your friends. Like that's you

## 20395:00 - 20420:00

know kind of the funniest part of it.

## 20420:00 - 20460:00

And so you I think it's no mistake today

## 20460:00 - 20505:00

that four deployed engineers who came up

## 20505:00 - 20530:00

through that system at Palanteer now

## 20530:00 - 20550:00

they're turning out to be some of the

## 20550:00 - 20580:00

best founders at YC actually. Yeah. I

## 20580:00 - 20620:00

mean produced this incredible an

## 20620:00 - 20645:00

incredible number of startup founders

## 20645:00 - 20675:00

cuz yeah like the training to be a fore

## 20675:00 - 20700:00

deployed engineer that's exactly the

## 20700:00 - 20720:00

right training to be a founder of these

## 20720:00 - 20750:00

companies. Now the the other interesting

## 20750:00 - 20775:00

thing about Palunteer is like other

## 20775:00 - 20810:00

companies would send like a salesperson

## 20810:00 - 20845:00

to go and sit with the FBI agent and

## 20845:00 - 20880:00

like Palunteer sent engineers to go and

## 20880:00 - 20905:00

do that. I think Palenter was probably

## 20905:00 - 20935:00

the first company to really like

## 20935:00 - 20965:00

institutionalize that and scale that as

## 20965:00 - 21005:00

a process, right? Yeah. I mean, I think

## 21005:00 - 21035:00

what happened there, the reason why they

## 21035:00 - 21060:00

were able to get these sort of seven and

## 21060:00 - 21095:00

eight and now nine figure contracts very

## 21095:00 - 21135:00

consistently is that uh instead of

## 21135:00 - 21160:00

sending someone who's like hair and

## 21160:00 - 21190:00

teeth and they're in there and you know,

## 21190:00 - 21220:00

let's go to the let's go to the uh

## 21220:00 - 21250:00

steakhouse. You know, it's all like

## 21250:00 - 21290:00

relationship. and you'd have one meeting

## 21290:00 - 21315:00

uh they would really like the

## 21315:00 - 21355:00

salesperson and then through sheer force

## 21355:00 - 21395:00

of personality you'd try to get them to

## 21395:00 - 21425:00

give you a seven-figure contract and

## 21425:00 - 21455:00

like the time scales on this would be

## 21455:00 - 21500:00

you know 6 weeks 10 weeks 12 weeks like

## 21500:00 - 21535:00

5 years I don't know it's like and the

## 21535:00 - 21570:00

software would never work uh whereas if

## 21570:00 - 21610:00

you put an engineer in there and you

## 21610:00 - 21655:00

give them uh you know Palunteer Foundry

## 21655:00 - 21680:00

which is what they now call sort of

## 21680:00 - 21730:00

their core uh data viz and data mining

## 21730:00 - 21780:00

suites instead of the next meeting being

## 21780:00 - 21830:00

reviewing 50 pages of you know sort of

## 21830:00 - 21865:00

sales documentation or a contract or a

## 21865:00 - 21895:00

spec or anything like that. It's

## 21895:00 - 21940:00

literally like, "Okay, we built it." And

## 21940:00 - 21975:00

then you're getting like real live

## 21975:00 - 22020:00

feedback within days. And I mean, that's

## 22020:00 - 22055:00

honestly the biggest opportunity for

## 22055:00 - 22085:00

startup founders. If startup founders

## 22085:00 - 22130:00

can do that and uh that's what forward

## 22130:00 - 22155:00

deployed engineers are sort of used to

## 22155:00 - 22185:00

doing that's how you could beat a

## 22185:00 - 22235:00

Salesforce or an Oracle or you know a

## 22235:00 - 22280:00

Booze Allen or literally any company out

## 22280:00 - 22320:00

there that has a big office and a big

## 22320:00 - 22350:00

fancy you know you have big fancy

## 22350:00 - 22390:00

salespeople with big strong handshakes

## 22390:00 - 22420:00

and it's like how does a really good

## 22420:00 - 22450:00

engineer with a weak handshake go in

## 22450:00 - 22480:00

there and beat them? It's actually you

## 22480:00 - 22505:00

show them something that they've never

## 22505:00 - 22555:00

seen before and like make them feel

## 22555:00 - 22585:00

super heard. You have to be super

## 22585:00 - 22610:00

empathetic about it. Like you actually

## 22610:00 - 22645:00

have to be a great designer and product

## 22645:00 - 22695:00

person and then you know come back and

## 22695:00 - 22725:00

you can just blow them away. Like the

## 22725:00 - 22765:00

software is so powerful that you know

## 22765:00 - 22795:00

the second you see something that you

## 22795:00 - 22830:00

know makes you feel seen you want to buy

## 22830:00 - 22855:00

it on the spot. Is a good way of

## 22855:00 - 22875:00

thinking about it that founders should

## 22875:00 - 22915:00

think about themselves as being the four

## 22915:00 - 22945:00

deployed engineers of their own company.

## 22945:00 - 22965:00

Absolutely. Yeah. Like you definitely

## 22965:00 - 23010:00

can't farm this out. Like literally the

## 23010:00 - 23045:00

founders themselves, they're technical.

## 23045:00 - 23065:00

They have to be the great product

## 23065:00 - 23090:00

people. They have to be the

## 23090:00 - 23120:00

ethnographer. They have to be the

## 23120:00 - 23165:00

designer. You want the person on the

## 23165:00 - 23195:00

second meeting to see the demo you put

## 23195:00 - 23225:00

together based on the stuff you heard.

## 23225:00 - 23260:00

And you want them to say, "Wow, I've

## 23260:00 - 23295:00

never seen anything like that." And take

## 23295:00 - 23325:00

my money. I think the incredible thing

## 23325:00 - 23355:00

about this model is this is why we're

## 23355:00 - 23395:00

seeing a lot of the vertical AI agents

## 23395:00 - 23450:00

take off is precisely this because they

## 23450:00 - 23500:00

can have these meetings with the end

## 23500:00 - 23540:00

buyer and champion at these big

## 23540:00 - 23580:00

enterprises. They take that context and

## 23580:00 - 23615:00

then they stuff it basically in the

## 23615:00 - 23655:00

prompt and then they can quickly come

## 23655:00 - 23690:00

back in a meeting like just the next day

## 23690:00 - 23710:00

maybe with Palunteer would have taken a

## 23710:00 - 23745:00

bit longer and a team of engineers here.

## 23745:00 - 23785:00

It could be just the two founders go in

## 23785:00 - 23815:00

and then they would close this six,

## 23815:00 - 23850:00

seven figure deals which we've seen and

## 23850:00 - 23910:00

with large enterprises which has never

## 23910:00 - 23945:00

been done before and it's just possible

## 23945:00 - 23985:00

with this new model of forward deploy

## 23985:00 - 24045:00

engineer plus AI is just on

## 24045:00 - 24075:00

accelerating. It just reminds me of a

## 24075:00 - 24095:00

company I mentioned before on the

## 24095:00 - 24125:00

podcast like Giger ML who do customer

## 24125:00 - 24165:00

another customer support and especially

## 24165:00 - 24200:00

a lot of voice support and it's just

## 24200:00 - 24250:00

classic case of two extremely um

## 24250:00 - 24290:00

talented software engineers not natural

## 24290:00 - 24320:00

sales people but they force themselves

## 24320:00 - 24355:00

to be essentially forward deployed

## 24355:00 - 24395:00

engineers and they closed a huge deal

## 24395:00 - 24420:00

with Zeppto and then a couple of other

## 24420:00 - 24455:00

companies they can't announce yet but do

## 24455:00 - 24480:00

they physically go on site like the

## 24480:00 - 24510:00

palentier model? Yes. So they did so

## 24510:00 - 24540:00

they they did all of that where once

## 24540:00 - 24565:00

they close the deal they go on site and

## 24565:00 - 24585:00

they sit there with all the customer

## 24585:00 - 24620:00

support people and figuring out how to

## 24620:00 - 24655:00

keep tuning and getting the software or

## 24655:00 - 24690:00

the LM to work even better. But before

## 24690:00 - 24730:00

that even to win the deal what they

## 24730:00 - 24770:00

found is that they can they can win by

## 24770:00 - 24795:00

just having the most impressive demo.

## 24795:00 - 24840:00

And in their case they've um innovated a

## 24840:00 - 24885:00

bit on the rag pipeline so that they can

## 24885:00 - 24925:00

um have their voice responses be both

## 24925:00 - 24955:00

accurate and very low latency. sort of

## 24955:00 - 24985:00

like a technically challenging thing to

## 24985:00 - 25030:00

do, but I just feel like in the like pre

## 25030:00 - 25065:00

sort of the current LLM rise, you

## 25065:00 - 25085:00

couldn't necessarily differentiate

## 25085:00 - 25125:00

enough in the demo phase of sales to

## 25125:00 - 25160:00

beat out incumbent. So, you can really

## 25160:00 - 25185:00

beat Salesforce by having a slightly

## 25185:00 - 25230:00

better CRM with a better UI. But now

## 25230:00 - 25260:00

because the technology evolves so fast

## 25260:00 - 25290:00

and it's so hard to get this like last

## 25290:00 - 25340:00

five 10 five to 10% correct, you can

## 25340:00 - 25365:00

actually if you're a forward deployed

## 25365:00 - 25410:00

engineer go in do the first meeting

## 25410:00 - 25435:00

tweak it so that it works really well

## 25435:00 - 25465:00

for that customer. Go back with the demo

## 25465:00 - 25500:00

and just get that oh wow like we've not

## 25500:00 - 25530:00

seen anyone else pull this off before

## 25530:00 - 25565:00

experience and close huge deals. And

## 25565:00 - 25600:00

that was the exact same case with Happy

## 25600:00 - 25660:00

Robot who has sold seven figure

## 25660:00 - 25705:00

contracts to the top three largest

## 25705:00 - 25745:00

logistic brokers in the world. They

## 25745:00 - 25785:00

build AI voice agents for that. They are

## 25785:00 - 25810:00

the ones doing the forward deploy

## 25810:00 - 25840:00

engineer model and talking to like the

## 25840:00 - 25885:00

CIOS of these companies and quickly

## 25885:00 - 25930:00

shipping a lot of product like very very

## 25930:00 - 25950:00

quick turnaround. And it's been

## 25950:00 - 25980:00

incredible to see that take off right

## 25980:00 - 26015:00

now. And it started from six figure

## 26015:00 - 26050:00

deals now doing closing and seven figure

## 26050:00 - 26085:00

deals which is crazy. This is just a

## 26085:00 - 26110:00

couple months after. So that's the kind

## 26110:00 - 26155:00

of stuff that you can do with uh I mean

## 26155:00 - 26190:00

unbelievably very very smart prompt

## 26190:00 - 26225:00

engineering actually. Well, one of the

## 26225:00 - 26265:00

things that's kind of interesting about

## 26265:00 - 26310:00

uh each model is that they each seem to

## 26310:00 - 26360:00

have their own personality. And one of

## 26360:00 - 26385:00

the things the founders are really

## 26385:00 - 26425:00

realizing is that you're going to go to

## 26425:00 - 26445:00

different people for different things.

## 26445:00 - 26485:00

Actually, one of the things that's known

## 26485:00 - 26520:00

a lot is Claude is sort of the more

## 26520:00 - 26590:00

happy and more human steerable model.

## 26590:00 - 26670:00

And the uh other one is Lama 4 is one

## 26670:00 - 26700:00

that needs a lot more steering. It's

## 26700:00 - 26730:00

almost like talking to a developer and

## 26730:00 - 26760:00

part of it could be an artifact of not

## 26760:00 - 26815:00

having done as much RL RHF on top of it.

## 26815:00 - 26860:00

So is a bit more rough to work with, but

## 26860:00 - 26905:00

you could actually steer it very well if

## 26905:00 - 26920:00

you

## 26920:00 - 26975:00

actually are good at actually doing a

## 26975:00 - 27000:00

lot of prompting and almost doing a bit

## 27000:00 - 27030:00

more RLHF, but it's a bit harder to work

## 27030:00 - 27055:00

with actually. Well, one of the things

## 27055:00 - 27100:00

we've been using uh LLMs for internally

## 27100:00 - 27145:00

is actually helping founders figure out

## 27145:00 - 27185:00

who they should take money from. And so

## 27185:00 - 27225:00

in that case, sometimes you need a very

## 27225:00 - 27275:00

straightforward rubric, a zero to 100.

## 27275:00 - 27315:00

zero being never ever take their money

## 27315:00 - 27350:00

and 100 being take their money right

## 27350:00 - 27380:00

away. Like they actually help you so

## 27380:00 - 27410:00

much that you'd be crazy not to take

## 27410:00 - 27450:00

their money. Harj, we've been working on

## 27450:00 - 27485:00

uh some scoring rubrics around that

## 27485:00 - 27515:00

using prompts. What What are some of the

## 27515:00 - 27545:00

things we've learned? So, it's certainly

## 27545:00 - 27610:00

best practice to give um LLM's rubrics,

## 27610:00 - 27625:00

especially if you want to get a

## 27625:00 - 27650:00

numerical score as the output. You want

## 27650:00 - 27675:00

to give it a rubric to help it

## 27675:00 - 27695:00

understand like how should I think

## 27695:00 - 27730:00

through and what's like a 80 versus a

## 27730:00 - 27765:00

90. But these rubrics are never perfect.

## 27765:00 - 27795:00

there's often always exceptions and you

## 27795:00 - 27855:00

tried it with uh 03 versus Gemini 2.5

## 27855:00 - 27885:00

and you found this this is what we found

## 27885:00 - 27910:00

really interesting is that um you can

## 27910:00 - 27940:00

give the same rubric to two different

## 27940:00 - 27970:00

models and in our in our specific case

## 27970:00 - 28020:00

what we found is that um 03 was very

## 28020:00 - 28055:00

rigid actually like it really sticks to

## 28055:00 - 28100:00

the rubric it's heavily penalizes for

## 28100:00 - 28115:00

anything that doesn't fit like the

## 28115:00 - 28145:00

rubric that you've given it whereas

## 28145:00 - 28195:00

Gemini 2.5 Pro was actually quite good

## 28195:00 - 28235:00

at being flexible in that it would apply

## 28235:00 - 28265:00

the rubric but it could also sort of

## 28265:00 - 28305:00

almost reason through why someone might

## 28305:00 - 28345:00

be like an exception or why you might

## 28345:00 - 28380:00

want to um push something up more

## 28380:00 - 28410:00

positively or negatively than the rubric

## 28410:00 - 28445:00

might suggest, which I just thought was

## 28445:00 - 28480:00

really interesting cuz that it's just

## 28480:00 - 28505:00

like when you're training a person,

## 28505:00 - 28535:00

you're trying to you give them a rubric

## 28535:00 - 28565:00

like you want them to use a rubric as a

## 28565:00 - 28590:00

guide, but there are always these sort

## 28590:00 - 28615:00

of edge cases where you need to sort of

## 28615:00 - 28650:00

think a little bit more deeply. Um, and

## 28650:00 - 28680:00

I just thought it was interesting that

## 28680:00 - 28720:00

the models themselves will handle that

## 28720:00 - 28735:00

differently, which means they sort of

## 28735:00 - 28760:00

have different personalities, right?

## 28760:00 - 28800:00

Like 03 felt a little bit more like the

## 28800:00 - 28820:00

soldier sort of like, okay, I'm

## 28820:00 - 28835:00

definitely like check, check, check,

## 28835:00 - 28885:00

check, check. Um, and Gemini Pro 2.5

## 28885:00 - 28910:00

felt a little bit more like a a high

## 28910:00 - 28935:00

agency sort of employee was like, "Oh,

## 28935:00 - 28960:00

okay. I think this makes sense, but this

## 28960:00 - 28985:00

might be an exception in this case,"

## 28985:00 - 29020:00

which was um just really interesting to

## 29020:00 - 29045:00

see. Yeah, it's funny to see that for

## 29045:00 - 29065:00

investors. You know, sometimes you have

## 29065:00 - 29100:00

investors like a Benchmark or a Thrive,

## 29100:00 - 29125:00

it's like, "Yeah, take their money right

## 29125:00 - 29165:00

away. Their process is immaculate. They

## 29165:00 - 29200:00

never ghost anyone. They answer their

## 29200:00 - 29240:00

emails faster than most founders. It's,

## 29240:00 - 29275:00

you know, very impressive. And then, uh,

## 29275:00 - 29305:00

one example here might be, you know,

## 29305:00 - 29330:00

there are plenty of investors who are

## 29330:00 - 29355:00

just overwhelmed and maybe they're just

## 29355:00 - 29400:00

not that good at managing their time.

## 29400:00 - 29425:00

And so, they might be really great

## 29425:00 - 29450:00

investors and their track record bears

## 29450:00 - 29490:00

that out, but they're sort of slow to

## 29490:00 - 29520:00

get back. They seem overwhelmed all the

## 29520:00 - 29555:00

time. They accidentally, probably not

## 29555:00 - 29600:00

intentionally ghost people. And so this

## 29600:00 - 29645:00

is legitimately exactly what an LLM is

## 29645:00 - 29685:00

for. Like the debug info on some of

## 29685:00 - 29720:00

these are very interesting to see like

## 29720:00 - 29765:00

you know maybe it's a 91 instead of like

## 29765:00 - 29805:00

an 89. We'll see. I guess one of the

## 29805:00 - 29830:00

things that's been really surprising to

## 29830:00 - 29865:00

me as you know we ourselves are playing

## 29865:00 - 29895:00

with it and we spend you know maybe 80

## 29895:00 - 29935:00

to 90% of our time with founders who are

## 29935:00 - 29975:00

all the way out on the edge is uh you

## 29975:00 - 30005:00

know on the one hand the analogies I

## 30005:00 - 30050:00

think even we use to discuss this is uh

## 30050:00 - 30075:00

it's kind of like coding. It kind of

## 30075:00 - 30125:00

actually feels like coding in, you know,

## 30125:00 - 30170:00

1995. Like the tools are not all the way

## 30170:00 - 30195:00

there. There's a lot of stuff that's

## 30195:00 - 30230:00

unspecified. We're, you know, in this

## 30230:00 - 30275:00

new frontier. But personally, it also

## 30275:00 - 30300:00

kind of feels like learning how to

## 30300:00 - 30350:00

manage a person where it's like, how do

## 30350:00 - 30390:00

I actually communicate uh, you know, the

## 30390:00 - 30430:00

things that they need to know in order

## 30430:00 - 30470:00

to make a good decision? And how do I

## 30470:00 - 30510:00

make sure that they know um, you know,

## 30510:00 - 30540:00

how I'm going to evaluate and score

## 30540:00 - 30590:00

them? And uh not only that, like there's

## 30590:00 - 30635:00

this aspect of Kaizen, you know, this um

## 30635:00 - 30665:00

this manufacturing technique that

## 30665:00 - 30695:00

created really really good cars for

## 30695:00 - 30745:00

Japan in the '90s. Uh and that principle

## 30745:00 - 30785:00

actually says that the people who are

## 30785:00 - 30815:00

the absolute best at improving the

## 30815:00 - 30840:00

process are the people actually doing

## 30840:00 - 30885:00

it. That's literally why uh Japanese

## 30885:00 - 30920:00

cars got so good in the '90s. And that's

## 30920:00 - 30960:00

metaprompting to me. So, I don't know.

## 30960:00 - 30990:00

It's a brave new world. We're sort of in

## 30990:00 - 31035:00

this new moment. So, with that, we're

## 31035:00 - 31075:00

out of time. But can't wait to see what

## 31075:00 - 31100:00

kind of prompts you guys come up with.

## 31100:00 - 31140:00

And we'll see you next time.

## 31140:00+

[Music]

