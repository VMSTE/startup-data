---
source: https://www.youtube.com/watch?v=cN0kZnSjfzI
title: I build AI agents for 4 businesses. None of them use teams.
author: Steph France
date: 2026-03-08
views: 2045
description: |-
  Want to learn how to build a general-purpose AI agent for your business? I'm launching Agent Operators — a community where I share the skills, frameworks, and architecture from my real client work. Join the waitlist: https://sfrance.co/community/

  Connect with me:
  https://sfrance.co
  https://twitter.com/meetstef
  https://www.linkedin.com/in/stephane-franceschini

  ---
  Description:

  Why I stopped building multi-agent teams and what I do instead.

  Everyone in the AI agent space is building teams of 50 agents, mission control dashboards, agent swarms. I thought the same thing a year ago and even made a video about it. After building agents full-time for real businesses, I completely changed my mind.

  In this video I break down:
  — Why one general-purpose agent outperforms a team of agents for most businesses
  — The API rate limit problem nobody talks about
  — The coordination nightmare of multi-agent systems
  — My work lane framework for running parallel tasks with a single agent
  — When you actually need multiple agents (with a real example from my client work)
  — What the research says (UBC paper + Microsoft's decision framework)

  My take: don't build 30 agents. Teach one agent 30 skills.

  📄 Research paper (UBC): https://arxiv.org/abs/2601.04748
  arXiv.org
  📄 Microsoft single vs multi-agent framework: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents
  📺 My old video about building agent teams: https://youtu.be/cF20jBzi4sQ
tags:
  - ai agents
  - multi-agent
  - single agent
  - agent swarm
  - team of agents
  - ai agent architecture
  - general purpose agent
  - openclaw
  - work lanes
  - ai productivity
  - ai for business
  - one agent vs many
  - ai agent framework
  - building ai agents
  - ai consulting
  - agent skills
  - context management
  - progressive disclosure
  - api rate limit
  - microsoft ai agents
  - ubc paper agents
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T11:52:21.840Z
---

# I build AI agents for 4 businesses. None of them use teams.

## 00:00 - 40:00

In this video, I'm going to talk about

## 40:00 - 85:00

uh why if you are a founder or even a

## 85:00 - 140:00

soloreneur, you shouldn't uh spend your

## 140:00 - 190:00

time build team of agents, but instead

## 190:00 - 235:00

you should think in terms of general

## 235:00 - 270:00

purpose agent. And I know it's quite a

## 270:00 - 305:00

controversial claim because a lot of

## 305:00 - 355:00

content out there show you how to build

## 355:00 - 410:00

like to to have like 15 agents on your

## 410:00 - 460:00

Mac Mini and it runs your business. I I

## 460:00 - 505:00

I actually made a YouTube video a year

## 505:00 - 560:00

ago, like in January 25, talking about

## 560:00 - 595:00

how to structure a team of agent. And I

## 595:00 - 635:00

think the the the sort of process behind

## 635:00 - 670:00

it is still valid. But it's just that as

## 670:00 - 720:00

of today, um I don't think this is the

## 720:00 - 760:00

best way to use your time because the

## 760:00 - 795:00

results are not there yet. And then

## 795:00 - 825:00

that's what I'm going to talk about in

## 825:00 - 860:00

this video. And most importantly, what

## 860:00 - 925:00

I'm I want to show you is my own

## 925:00 - 970:00

structure. and the the working framework

## 970:00 - 1000:00

for general purpose agent that I'm

## 1000:00 - 1055:00

developing uh which contains work lanes

## 1055:00 - 1100:00

which I'm going to explain later uh and

## 1100:00 - 1145:00

project which are atomic tasks uh and I

## 1145:00 - 1175:00

will also explain that a bit later but

## 1175:00 - 1215:00

I'm going to show you like the

## 1215:00 - 1250:00

I I actually work with different agents

## 1250:00 - 1275:00

but they are all for one specific

## 1275:00 - 1310:00

business each business that I'm working

## 1310:00 - 1345:00

with which is because I'm independent

## 1345:00 - 1380:00

consultant I build a general purpose

## 1380:00 - 1445:00

agent for it and the team is acting with

## 1445:00 - 1485:00

one agent that has a lot of different

## 1485:00 - 1525:00

capabilities and most importantly that

## 1525:00 - 1570:00

is always uh able to retrive the right

## 1570:00 - 1605:00

information at the right time rather

## 1605:00 - 1630:00

than having the huge complexity of

## 1630:00 - 1670:00

having a team of agent. I'm quickly

## 1670:00 - 1710:00

going to show you like um there is also

## 1710:00 - 1760:00

like a team a paper from Microsoft uh

## 1760:00 - 1820:00

about single agent or multiple agent. Um

## 1820:00 - 1860:00

there is also research study that went

## 1860:00 - 1910:00

through this uh problem and uh I

## 1910:00 - 1950:00

actually came up to the same conclusion

## 1950:00 - 1985:00

as this research did before I found it.

## 1985:00 - 2040:00

So I think I'm not going in the right

## 2040:00 - 2090:00

the wrong direction. Um but of course

## 2090:00 - 2135:00

everybody is figuring it out in the

## 2135:00 - 2185:00

agent space. So um take this with a

## 2185:00 - 2210:00

grain of salt. That's my way of

## 2210:00 - 2250:00

approaching it and I think there is a

## 2250:00 - 2305:00

lot of value in terms of uh in thinking

## 2305:00 - 2335:00

of what's possible with agent and

## 2335:00 - 2360:00

building teams and and and we need

## 2360:00 - 2405:00

people that create content about it

## 2405:00 - 2450:00

because it will happen at some point but

## 2450:00 - 2520:00

right now let's uh just build one agent

## 2520:00 - 2575:00

right uh and you will get like such an

## 2575:00 - 2610:00

incredible improvement in terms of

## 2610:00 - 2635:00

productivity and everything you can

## 2635:00 - 2685:00

achieve uh rather than spending time an

## 2685:00 - 2745:00

incredible amount of time uh tweaking

## 2745:00 - 2790:00

and and refining a team of agents that

## 2790:00 - 2825:00

won't even bring you the same um the

## 2825:00 - 2860:00

same improvement. Okay, let's go into

## 2860:00 - 2895:00

it. So,

## 2895:00 - 2960:00

why are team of agents or agents swarm a

## 2960:00 - 3020:00

trap? Um as I said, building one agent

## 3020:00 - 3070:00

is a m massive amount of work. You need

## 3070:00 - 3130:00

to get a lot of things right. And one

## 3130:00 - 3195:00

very important concept is um

## 3195:00 - 3235:00

information architecture and progressive

## 3235:00 - 3280:00

disclosure. And also another one is

## 3280:00 - 3325:00

context management. Um information

## 3325:00 - 3380:00

architecture is how do you design your

## 3380:00 - 3435:00

workspace so that your agent will always

## 3435:00 - 3470:00

find the right information at the same

## 3470:00 - 3550:00

time. And this takes a lot of um input

## 3550:00 - 3580:00

from your side to help the agent

## 3580:00 - 3620:00

organize and to to structure it in a way

## 3620:00 - 3680:00

that it it won't mess up over time, but

## 3680:00 - 3725:00

instead it will uh it will keep it

## 3725:00 - 3810:00

organized and always know when and where

## 3810:00 - 3870:00

to find the right information.

## 3870:00 - 3920:00

I have a full concept um about that

## 3920:00 - 3945:00

which I'm probably going to talk about

## 3945:00 - 3980:00

in a future video, but it's something

## 3980:00 - 4030:00

I'm developing um these days along the

## 4030:00 - 4075:00

way while I'm building. Uh it's it's a

## 4075:00 - 4125:00

structure for agents to always um to

## 4125:00 - 4165:00

have the right architecture and I'm

## 4165:00 - 4195:00

adding different files into my agents

## 4195:00 - 4225:00

like rules.md

## 4225:00 - 4275:00

um workspace.md to teach my agent how is

## 4275:00 - 4325:00

my workspace organized. I I'm really

## 4325:00 - 4385:00

careful about my tools.mmd. So the the I

## 4385:00 - 4425:00

have a file that is loaded every time my

## 4425:00 - 4465:00

agent so I talked about talk to my agent

## 4465:00 - 4520:00

on discord um and my agent reads uh

## 4520:00 - 4575:00

agent.md that tells it to read all these

## 4575:00 - 4630:00

files and all these files are leading to

## 4630:00 - 4685:00

other files that are in the workspace.

## 4685:00 - 4740:00

So it can always like no progressive

## 4740:00 - 4775:00

disclosure is like you show only a

## 4775:00 - 4825:00

little bit of information that explains

## 4825:00 - 4870:00

where is the rest of the information so

## 4870:00 - 4925:00

that if it needs it knows where to go to

## 4925:00 - 4980:00

find it and it's that is progressive

## 4980:00 - 5015:00

disclosure and information architecture

## 5015:00 - 5055:00

is how do you do you make the

## 5055:00 - 5100:00

information flow where do you mention

## 5100:00 - 5160:00

which um which folder to find the

## 5160:00 - 5195:00

information and context Text management

## 5195:00 - 5260:00

is basically um always being aware of

## 5260:00 - 5305:00

the amount of context that you have uh

## 5305:00 - 5340:00

in a session with your agent. And as of

## 5340:00 - 5390:00

today, unfortunately uh we don't have

## 5390:00 - 5450:00

models that provide more than 200,000 uh

## 5450:00 - 5485:00

token in context window, which is not

## 5485:00 - 5530:00

that much in the end. Um a lot of models

## 5530:00 - 5590:00

are promising 1 million uh token context

## 5590:00 - 5630:00

window, but it's not really working in

## 5630:00 - 5690:00

in practice. So

## 5690:00 - 5730:00

that's why am I mentioning that is

## 5730:00 - 5780:00

because all those files so if you are

## 5780:00 - 5830:00

aware about what's tok to tokens are

## 5830:00 - 5855:00

they are the amount of information that

## 5855:00 - 5905:00

you give your agent uh and all those

## 5905:00 - 5955:00

files they contain a lot of information

## 5955:00 - 6020:00

which means you start every conversation

## 6020:00 - 6085:00

with your agent by giving like 30 or

## 6085:00 - 6135:00

50,000 tokens so it knows everything

## 6135:00 - 6160:00

about what you are doing and you know

## 6160:00 - 6220:00

that you only play with the next 100,000

## 6220:00 - 6280:00

tokens or 150 if you want to go a little

## 6280:00 - 6315:00

bit further. Uh and then you need to

## 6315:00 - 6355:00

manage the context to avoid being

## 6355:00 - 6390:00

compacted and lose a bunch of

## 6390:00 - 6415:00

information about what you are talking

## 6415:00 - 6450:00

about. I'm going too far. This is

## 6450:00 - 6485:00

another video about context management.

## 6485:00 - 6540:00

Let's go back into presentation.

## 6540:00 - 6580:00

All right. Now you get the point. One

## 6580:00 - 6645:00

agent is complex um and hard to build,

## 6645:00 - 6700:00

right? So multiply that by 50. It

## 6700:00 - 6720:00

doesn't multiply your output. It

## 6720:00 - 6755:00

actually multiplies your mainten

## 6755:00 - 6790:00

maintenance. Um I really truly believe

## 6790:00 - 6870:00

that uh in business you need 100% 95%

## 6870:00 - 6930:00

certainty. Um a swarm or team of agent

## 6930:00 - 6960:00

will give you like I would say more even

## 6960:00 - 7020:00

like 60 or or 70%. By the way, this is

## 7020:00 - 7055:00

made by notebook LM. I'm testing it out.

## 7055:00 - 7090:00

So sometimes the things that are written

## 7090:00 - 7115:00

are not the things that I'm saying just

## 7115:00 - 7145:00

for you to know.

## 7145:00 - 7185:00

All right, let's talk about API

## 7185:00 - 7225:00

bottleneck. This one is is a good one.

## 7225:00 - 7280:00

It's a good reason uh on its own not to

## 7280:00 - 7320:00

think in terms of teams but rather in

## 7320:00 - 7365:00

terms of general purpose agent. So when

## 7365:00 - 7400:00

you have uh an AI provider, let's say

## 7400:00 - 7430:00

it's anthropic and you are using cloud

## 7430:00 - 7475:00

opus 4.6 six like I'm using or if you're

## 7475:00 - 7520:00

using chat GPT through the API or if

## 7520:00 - 7570:00

you're using another model like Kimmy or

## 7570:00 - 7625:00

or Minimax or whatever the model that

## 7625:00 - 7665:00

you are using you always have an API

## 7665:00 - 7720:00

rate limit for I know my one I think is

## 7720:00 - 7790:00

10,000 tokens per second which means um

## 7790:00 - 7845:00

I can only send this amount of data if I

## 7845:00 - 7890:00

send more then I will start having like

## 7890:00 - 7940:00

times timeouts uh I will start having

## 7940:00 - 8000:00

the the my API calls failing silently.

## 8000:00 - 8030:00

So I won't even know it, but the agent

## 8030:00 - 8085:00

won't get the the proper um feedback

## 8085:00 - 8115:00

from the model

## 8115:00 - 8170:00

um with one agent. So I've heard some

## 8170:00 - 8205:00

people saying like one agent can't do

## 8205:00 - 8235:00

several tasks at the same time. That

## 8235:00 - 8280:00

that's absolutely wrong. Uh you can have

## 8280:00 - 8330:00

as many different stream of conversation

## 8330:00 - 8385:00

as you want with one single agent and

## 8385:00 - 8445:00

that's what I do here. um within my

## 8445:00 - 8505:00

workspace um I'm having I'm constantly

## 8505:00 - 8555:00

working on like three to five uh

## 8555:00 - 8590:00

different stream of work at the same

## 8590:00 - 8655:00

time. So I start with one I I read what

## 8655:00 - 8700:00

it told me just earlier.

## 8700:00 - 8750:00

I use my microphone with whisper flow to

## 8750:00 - 8790:00

say whatever I want it to do later. Then

## 8790:00 - 8830:00

I switch on to the next one and I do the

## 8830:00 - 8855:00

same. Then I switch on to the next one.

## 8855:00 - 8890:00

I do the same. Then I go back go back to

## 8890:00 - 8930:00

the first one. And so I always have like

## 8930:00 - 9000:00

three to four conversations uh like um

## 9000:00 - 9040:00

sessions from my agents that are sending

## 9040:00 - 9100:00

and receiving um information to opuse

## 9100:00 - 9130:00

4.6.

## 9130:00 - 9185:00

But I can't go further than that than

## 9185:00 - 9220:00

four or five because my brain can't

## 9220:00 - 9255:00

process more than that. By the time I I

## 9255:00 - 9305:00

read the the three, four, five, then did

## 9305:00 - 9335:00

the first one was stopped since a while.

## 9335:00 - 9360:00

So it doesn't make any sense to have

## 9360:00 - 9385:00

more than that. Three, four is the right

## 9385:00 - 9420:00

sweet spot unless you are way smarter

## 9420:00 - 9455:00

than me and maybe you can have 10. But

## 9455:00 - 9495:00

also that's another lie is like people

## 9495:00 - 9565:00

showing like they have 50 uh windows at

## 9565:00 - 9615:00

the same time. Maybe I'm I'm super dumb

## 9615:00 - 9655:00

but I just can't don't think that it is

## 9655:00 - 9680:00

possible to have that many conversation

## 9680:00 - 9720:00

with agents at the same time. But

## 9720:00 - 9765:00

anyway, I was talking about uh the API

## 9765:00 - 9810:00

rate limit. So with my agent, I can have

## 9810:00 - 9835:00

several conversations at the time. It's

## 9835:00 - 9865:00

a general purpose agent, but with

## 9865:00 - 9900:00

different sessions that work in parallel

## 9900:00 - 9935:00

and it can also have like spawn sub

## 9935:00 - 9995:00

agents that work in parallel of my own

## 9995:00 - 10040:00

session with my agent, right?

## 10040:00 - 10085:00

But this already has a limit as I said

## 10085:00 - 10130:00

after the what's funny is that the API

## 10130:00 - 10175:00

rate um kind of correlate with my brain

## 10175:00 - 10210:00

limit. It's like four five conversations

## 10210:00 - 10250:00

you start reaching the the API rate

## 10250:00 - 10315:00

limit. But now when I hear that people

## 10315:00 - 10360:00

are using 20 agents at the same time

## 10360:00 - 10400:00

that are working simultaneously

## 10400:00 - 10445:00

but they all have one one API key. So

## 10445:00 - 10485:00

that's a problem because they will reach

## 10485:00 - 10530:00

the API rate limit.

## 10530:00 - 10565:00

So it's possible if you are a big

## 10565:00 - 10605:00

organization of course you have specific

## 10605:00 - 10660:00

contract that you have like a higher API

## 10660:00 - 10725:00

rate limit that I have. Um and and you

## 10725:00 - 10775:00

can also set up different uh contract

## 10775:00 - 10825:00

for each agent which will give them each

## 10825:00 - 10875:00

their API rate limit which is absolutely

## 10875:00 - 10910:00

feasible. But if you are using one

## 10910:00 - 10990:00

single access an API key and OO token

## 10990:00 - 11020:00

then there is no point in having 20

## 11020:00 - 11060:00

agents working at the same time because

## 11060:00 - 11110:00

simply it will reach the API rate limit

## 11110:00 - 11160:00

and it will fade fail silently but the

## 11160:00 - 11205:00

agent will pretend it worked. So it will

## 11205:00 - 11235:00

tell the orchestrator that it worked

## 11235:00 - 11270:00

perfectly. the orchestrator won't know

## 11270:00 - 11305:00

because it won't check and then as a

## 11305:00 - 11365:00

result you have a failed uh output but

## 11365:00 - 11395:00

you don't even know it and that's a

## 11395:00 - 11435:00

really big trap.

## 11435:00 - 11510:00

So the coordination nightmare. Um

## 11510:00 - 11570:00

so when you have one agent, you give it

## 11570:00 - 11660:00

um is role uh you give it tools with

## 11660:00 - 11710:00

credential accesses. Uh you give it

## 11710:00 - 11765:00

information uh within the workspace

## 11765:00 - 11815:00

where to find what. Right? But now

## 11815:00 - 11860:00

imagine you have another agent. The

## 11860:00 - 11900:00

question is why do you build another

## 11900:00 - 11955:00

agent? Is this other agent has access to

## 11955:00 - 11990:00

the same information? In that case, it's

## 11990:00 - 12050:00

not really another agent. Um, does it

## 12050:00 - 12105:00

have its own workspace? Right? Because

## 12105:00 - 12145:00

if you have a developer agent and a

## 12145:00 - 12185:00

content creation agent, then technically

## 12185:00 - 12220:00

they have different things to store. So,

## 12220:00 - 12250:00

are they storing in the same workspace

## 12250:00 - 12285:00

that you need to keep organized and

## 12285:00 - 12325:00

always up to date for each agent or do

## 12325:00 - 12370:00

you have like different workspace? In in

## 12370:00 - 12405:00

that case, how do you make sure that

## 12405:00 - 12440:00

they are having the same up-to-date

## 12440:00 - 12465:00

information?

## 12465:00 - 12510:00

And what about accesses when um you have

## 12510:00 - 12565:00

a new access access to a new tool? Um do

## 12565:00 - 12605:00

you deploy it to only one agent or

## 12605:00 - 12660:00

different agent? So just be before they

## 12660:00 - 12725:00

even start talking together like having

## 12725:00 - 12795:00

it work properly is a real pain. But now

## 12795:00 - 12835:00

when they start working together the

## 12835:00 - 12890:00

problem is what is the information that

## 12890:00 - 12935:00

they are passing each other. And for

## 12935:00 - 12990:00

example when I start one session with my

## 12990:00 - 13030:00

agent. So it will start here. It will

## 13030:00 - 13070:00

read this file that will tell it to read

## 13070:00 - 13115:00

this files and depending on what I asked

## 13115:00 - 13185:00

it will go and look for this specific uh

## 13185:00 - 13240:00

client space that will tell it to look

## 13240:00 - 13270:00

into this project that is currently

## 13270:00 - 13335:00

working that refers to this note that I

## 13335:00 - 13395:00

have taken. Um and maybe in my prompt I

## 13395:00 - 13475:00

also told it to use a certain tool that

## 13475:00 - 13525:00

went and um

## 13525:00 - 13560:00

was using a certain skill that I have

## 13560:00 - 13610:00

built. So all of that is the context of

## 13610:00 - 13680:00

my uh agent right it's a huge stack of

## 13680:00 - 13730:00

context but now imagine if it needs to

## 13730:00 - 13800:00

pass this on to another agent. So what

## 13800:00 - 13850:00

is it passing like just the mission of

## 13850:00 - 13900:00

what it should do but does this agent

## 13900:00 - 13950:00

needs to reread everything or does it

## 13950:00 - 14010:00

only read the mission that it got you

## 14010:00 - 14055:00

know and I don't want to work to go into

## 14055:00 - 14085:00

detail because you know I'm not a team

## 14085:00 - 14130:00

agent expert u I understand the

## 14130:00 - 14160:00

principle but I spend more of the my

## 14160:00 - 14205:00

time working on single purpose agent uh

## 14205:00 - 14240:00

but to me that is a major problem it's

## 14240:00 - 14270:00

like how do you make sure they really

## 14270:00 - 14330:00

have the right context to write on to to

## 14330:00 - 14390:00

work on the task and when they have

## 14390:00 - 14440:00

worked how do you make sure that they

## 14440:00 - 14495:00

send back the right answer

## 14495:00 - 14545:00

okay now let me uh introduce you to the

## 14545:00 - 14590:00

concept of work lane which is something

## 14590:00 - 14640:00

I'm currently developing uh which is

## 14640:00 - 14710:00

basically how how to structure stream of

## 14710:00 - 14765:00

streams of work and let me go back into

## 14765:00 - 14810:00

my own agent. So,

## 14810:00 - 14850:00

what are you looking at here? It's

## 14850:00 - 14915:00

Discord that is connected to my agent

## 14915:00 - 14965:00

which is called John which is my own

## 14965:00 - 14995:00

personal assistant that helps me to to

## 14995:00 - 15060:00

to manage my business uh my consulting

## 15060:00 - 15110:00

business to manage YouTube but also to

## 15110:00 - 15190:00

manage my clients uh businesses and each

## 15190:00 - 15240:00

of my client has its own agent. So we

## 15240:00 - 15285:00

have one here. We have another one here.

## 15285:00 - 15330:00

Another one here. Here that's something

## 15330:00 - 15385:00

else. But basically um

## 15385:00 - 15415:00

I'm going to talk about those uh just in

## 15415:00 - 15485:00

a moment. Um for now it's uh what is the

## 15485:00 - 15510:00

structure. So that's how I communicate

## 15510:00 - 15570:00

with my agent and each of those are

## 15570:00 - 15615:00

discord channels but they start a new

## 15615:00 - 15650:00

session which means every I can have

## 15650:00 - 15690:00

different conversations in parallel uh

## 15690:00 - 15730:00

on different topics.

## 15730:00 - 15770:00

So the way I structure it is I always

## 15770:00 - 15805:00

have my main session which is which I

## 15805:00 - 15860:00

call John which here I just wanted to

## 15860:00 - 15905:00

hide u he just talks about what I'm

## 15905:00 - 15930:00

talking about right now so you didn't

## 15930:00 - 15980:00

see my previous conversation but this is

## 15980:00 - 16025:00

where I would just go and say hey add

## 16025:00 - 16065:00

this tool or can you check that or like

## 16065:00 - 16100:00

very basic stuff it's not a proper

## 16100:00 - 16125:00

structured conversation it's just my

## 16125:00 - 16180:00

access to to my agent without having to

## 16180:00 - 16205:00

sort it up in a proper conversation.

## 16205:00 - 16275:00

Here are my videos brainstormed. So this

## 16275:00 - 16320:00

is uh when I brainstormed this video, I

## 16320:00 - 16350:00

went into this channel and then I say

## 16350:00 - 16385:00

okay take this this information, this

## 16385:00 - 16425:00

information, this information, what can

## 16425:00 - 16470:00

we do? How can we present it and so on.

## 16470:00 - 16525:00

So that's one stream of work. Uh here I

## 16525:00 - 16590:00

have work lanes. So if I go back here,

## 16590:00 - 16655:00

uh work lanes they are they all like the

## 16655:00 - 16700:00

equivalent of spaces for me. It's like

## 16700:00 - 16790:00

they there are uh blocks in your life

## 16790:00 - 16850:00

like my personal life is one block, my

## 16850:00 - 16890:00

business is one block, one client is one

## 16890:00 - 16945:00

block. Um and you can imagine different

## 16945:00 - 16985:00

blocks in your life and they all have a

## 16985:00 - 17045:00

sort of infinite road map in terms of

## 17045:00 - 17100:00

when you you can make a road map of okay

## 17100:00 - 17130:00

what are the things I need to do in the

## 17130:00 - 17165:00

next week in the next month in the next

## 17165:00 - 17205:00

year maybe if you want and then you can

## 17205:00 - 17255:00

work on this one task at the time and

## 17255:00 - 17290:00

update the road map and then maybe

## 17290:00 - 17335:00

brainstorm again and modify the road map

## 17335:00 - 17370:00

but it's always the same thing just

## 17370:00 - 17400:00

something that is moving forward world

## 17400:00 - 17445:00

it's the work lane but then in your work

## 17445:00 - 17470:00

lane

## 17470:00 - 17525:00

the um you have what I call project

## 17525:00 - 17560:00

maybe I will find a better name uh but

## 17560:00 - 17605:00

the agent extract specific tasks execute

## 17605:00 - 17645:00

them in parallel session and merge the

## 17645:00 - 17680:00

result back into the main lane so what

## 17680:00 - 17730:00

that means is when I'm here I'm not

## 17730:00 - 17775:00

opening for for privacy right but this

## 17775:00 - 17820:00

is long conversation I have with my

## 17820:00 - 17860:00

agent talking like brainstorming making

## 17860:00 - 17915:00

it research um brainstorming again

## 17915:00 - 17950:00

asking my agents to ask me questions so

## 17950:00 - 17990:00

I can answer and then we have all the

## 17990:00 - 18015:00

information and I say okay let's create

## 18015:00 - 18060:00

the road map with what we have said and

## 18060:00 - 18105:00

then we say I say sometimes I just work

## 18105:00 - 18130:00

in my lane I say okay what's the next

## 18130:00 - 18170:00

step okay let's do it and so on so forth

## 18170:00 - 18215:00

and sometimes I only work with uh lanes

## 18215:00 - 18250:00

right I'm working on my YouTube lane and

## 18250:00 - 18275:00

I'm working on my client one lane by the

## 18275:00 - 18310:00

way I just for this video I changed the

## 18310:00 - 18365:00

name usually my client's name here um

## 18365:00 - 18425:00

but I I work with only with with lane

## 18425:00 - 18480:00

one step at a time. But sometimes I find

## 18480:00 - 18525:00

okay I'm working mainly on this uh

## 18525:00 - 18595:00

client one and turns out I have a lot of

## 18595:00 - 18630:00

different project that when I look at my

## 18630:00 - 18665:00

road map I'm like okay but all these

## 18665:00 - 18705:00

project are um I can work on them in

## 18705:00 - 18760:00

parallel. So I say okay for for this and

## 18760:00 - 18815:00

this and this tasks uh extract the

## 18815:00 - 18850:00

content and create a project for each of

## 18850:00 - 18885:00

them and then automatically it will

## 18885:00 - 18945:00

create a project in in the workspace a

## 18945:00 - 18985:00

project folder and a discord channel

## 18985:00 - 19020:00

which will uh have all the context for

## 19020:00 - 19065:00

me to work only on this specific task.

## 19065:00 - 19105:00

So instead of going one by one in my

## 19105:00 - 19135:00

lane now I'm having different

## 19135:00 - 19180:00

conversations for each of those. And now

## 19180:00 - 19220:00

when I'm going to work I'm working like

## 19220:00 - 19265:00

I'm having maybe for clients uh for

## 19265:00 - 19295:00

YouTube I'm working on the lane. I don't

## 19295:00 - 19330:00

have specific project but I stop working

## 19330:00 - 19365:00

on client one lane and instead I work on

## 19365:00 - 19395:00

three project at the time for this

## 19395:00 - 19440:00

specific client. But when I'm done I say

## 19440:00 - 19470:00

check the different project they are all

## 19470:00 - 19500:00

done. Please update the road map and

## 19500:00 - 19540:00

let's move let's move on. Then now it it

## 19540:00 - 19585:00

knows exactly where are the project and

## 19585:00 - 19625:00

then we can move on on the general road

## 19625:00 - 19655:00

map. So that's basically the difference

## 19655:00 - 19705:00

between the work lane and the project A

## 19705:00 - 19755:00

project B. What allows me to work like

## 19755:00 - 19805:00

simultaneously on different things. So

## 19805:00 - 19850:00

let's talk about the only time you need

## 19850:00 - 19890:00

multiple agents. I'm saying you need

## 19890:00 - 19915:00

right? You can always have multiple

## 19915:00 - 19965:00

agent but when do you need them? So this

## 19965:00 - 20020:00

is from the paper that I will link uh in

## 20020:00 - 20065:00

the description that you can access um

## 20065:00 - 20115:00

from Microsoft that says go multi- aent

## 20115:00 - 20150:00

only when security and compliance

## 20150:00 - 20190:00

requires strict data isolation. I have

## 20190:00 - 20225:00

one case like that I'm going to show you

## 20225:00 - 20270:00

multiple completely different

## 20270:00 - 20315:00

independent teams on different domains.

## 20315:00 - 20350:00

So that's not about compliance. It's

## 20350:00 - 20390:00

just like really the teams for that work

## 20390:00 - 20415:00

for the same business but they have

## 20415:00 - 20460:00

nothing to do uh with each other. In

## 20460:00 - 20495:00

that case it makes sense to make

## 20495:00 - 20550:00

different agent but that requires you to

## 20550:00 - 20590:00

be like already a big organization. If

## 20590:00 - 20625:00

you are if you are just a small business

## 20625:00 - 20670:00

then you are not doing that like all

## 20670:00 - 20710:00

team can have the context of everything.

## 20710:00 - 20765:00

So here is one. So let me show you the

## 20765:00 - 20830:00

agent I'm working on. So this is a

## 20830:00 - 20885:00

purely general purpose agents um that

## 20885:00 - 20945:00

does that knows everything about one

## 20945:00 - 20980:00

client and different brands within this

## 20980:00 - 21025:00

client and um they have their own

## 21025:00 - 21060:00

different brands and and for each of

## 21060:00 - 21095:00

them I I store the market research. I

## 21095:00 - 21150:00

store like um a lot of skills that they

## 21150:00 - 21200:00

can use, but the team is is uh learning

## 21200:00 - 21250:00

how to use one specific agent that

## 21250:00 - 21285:00

manages the whole business and all the

## 21285:00 - 21320:00

different brands. [snorts]

## 21320:00 - 21360:00

This one uh so let me show you this one.

## 21360:00 - 21390:00

This one is exactly the same thing as

## 21390:00 - 21415:00

this one, but for another client. So,

## 21415:00 - 21450:00

it's a general purpose agent, but this

## 21450:00 - 21485:00

one Lena

## 21485:00 - 21535:00

is a customer service agent. So it works

## 21535:00 - 21585:00

for the same client that this one is

## 21585:00 - 21620:00

working already but they have two agents

## 21620:00 - 21660:00

and the reason is that Lena is a

## 21660:00 - 21695:00

customer service agent. So it works on

## 21695:00 - 21750:00

top of our customer service uh system

## 21750:00 - 21800:00

which is gorgeous and it has access to

## 21800:00 - 21870:00

very specific uh tools that are only

## 21870:00 - 21910:00

required for customer service such as

## 21910:00 - 21970:00

ERP um like certain access in Shopify uh

## 21970:00 - 22020:00

the invoicing tool and all all the stuff

## 22020:00 - 22075:00

that this agent needs

## 22075:00 - 22120:00

and it there is a lot of security

## 22120:00 - 22165:00

involved here because this agent is

## 22165:00 - 22225:00

customerf facing and we also it's also

## 22225:00 - 22270:00

team facing but we don't want to mix all

## 22270:00 - 22305:00

the accesses and to give this agent for

## 22305:00 - 22360:00

example the right to uh create Facebook

## 22360:00 - 22415:00

ads like this one can but we don't want

## 22415:00 - 22445:00

the customer service to be able to to

## 22445:00 - 22485:00

put budget on our on our ads it doesn't

## 22485:00 - 22530:00

make sense so in that case we are here

## 22530:00 - 22585:00

at the uh security and compliance

## 22585:00 - 22665:00

requires strict uh data isolation

## 22665:00 - 22700:00

If you wonder what is this one, it's my

## 22700:00 - 22750:00

wife's agent. My wife is a coach. She is

## 22750:00 - 22785:00

crushing it with her agent. She's just

## 22785:00 - 22810:00

like

## 22810:00 - 22845:00

doing so many things. I'm just managing

## 22845:00 - 22880:00

the agent from the back end. But that's

## 22880:00 - 22915:00

that's a pure general purpose agent that

## 22915:00 - 22960:00

she uses to uh grow her business. She's

## 22960:00 - 23005:00

like creating ress with it. Like she

## 23005:00 - 23040:00

rebuilt a whole website. She managed

## 23040:00 - 23090:00

SEO. she she manages so many things at

## 23090:00 - 23125:00

the same time with one general purpose

## 23125:00 - 23150:00

agent.

## 23150:00 - 23185:00

So that's from the paper I was

## 23185:00 - 23225:00

mentioning earlier which I haven't read

## 23225:00 - 23285:00

entirely but basically to summarize if

## 23285:00 - 23350:00

you compare like a really welldone uh

## 23350:00 - 23385:00

multiple team agent with one single

## 23385:00 - 23425:00

agent in most of the case you get the

## 23425:00 - 23475:00

same thing. The thing is if most of the

## 23475:00 - 23515:00

case if you try to make it then chances

## 23515:00 - 23555:00

are you won't have a really well done

## 23555:00 - 23610:00

multiple agent team working together. So

## 23610:00 - 23640:00

most of the case you will have less

## 23640:00 - 23695:00

result than a single agent.

## 23695:00 - 23745:00

So in the end um don't build 30 agents

## 23745:00 - 23795:00

teach one agent 30 skills. Skills are

## 23795:00 - 23840:00

modular portable and compound over time.

## 23840:00 - 23875:00

There is a whole other video about how

## 23875:00 - 23915:00

to use progressive disclosure in terms

## 23915:00 - 23965:00

of skills. Um

## 23965:00 - 23990:00

so this this is a problem we are

## 23990:00 - 24045:00

currently solving but in general this is

## 24045:00 - 24090:00

uh the framework I wanted to share with

## 24090:00 - 24135:00

you because those are my beliefs at the

## 24135:00 - 24185:00

moment. It might evolve I have no idea.

## 24185:00 - 24220:00

Maybe the models will will evolve or

## 24220:00 - 24250:00

someone will come up with a very good

## 24250:00 - 24305:00

framework that is easy to apply. But as

## 24305:00 - 24350:00

of today uh I am only focusing on

## 24350:00 - 24410:00

general purpose agents and I'm building

## 24410:00 - 24450:00

agents uh separate agents for the same

## 24450:00 - 24495:00

business only if it's really needed. I

## 24495:00 - 24535:00

would love to hear what you think about

## 24535:00 - 24590:00

that and if you have tried uh actual

## 24590:00 - 24635:00

agent team what were the results you got

## 24635:00 - 24670:00

please write it in the comments. I I I

## 24670:00 - 24720:00

can't wait to to hear about that and um

## 24720:00 - 24755:00

I just see you in the next video.

## 24755:00+

Bye-bye.

