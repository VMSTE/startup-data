---
source: https://www.youtube.com/watch?v=qvNCVYkHKfg
title: Why Can't AI Make Its Own Discoveries? — With Yann LeCun
author: Alex Kantrowitz
date: 2025-03-19
views: 210930
description: >-
  Yann LeCun is the chief AI scientist at Meta. He joins Big Technology Podcast
  to discuss the strengths and limitations of current AI models, weighing in on
  why they've been unable to invent new things despite possessing almost all the
  world's written knowledge. LeCun digs deep into AI science, explaining why AI
  systems must build an abstract knowledge of the way the world operates to
  truly advance. We also cover whether AI research will hit a wall, whether
  investors in AI will be disappointed, and the value of open source after
  DeepSeek. Tune in for a fascinating conversation with one of the world's
  leading AI pioneers.


  Chapters: 


  00:00 Introduction to Jan LeCun and AI's limitations

  01:12 Why LLMs can't make scientific discoveries

  05:40 Reasoning in AI systems: limitations of chain of thought

  10:13 LLMs approaching diminishing returns and the need for a new paradigm

  16:29 "A PhD next to you" vs. actual intelligent systems

  21:36 Consumer AI adoption vs. enterprise implementation challenges

  25:37 Historical parallels: expert systems and the risk of another AI winter

  29:37 Four critical capabilities AI needs for true understanding

  33:19 Testing AI's physics understanding with the paper test

  37:24 Why video generation systems don't equal real comprehension

  43:33 Self-supervised learning and its limitations for understanding

  51:10 JEPA: Building abstract representations for reasoning and planning

  54:33 Open source vs. proprietary AI development

  58:57 Conclusion
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T21:03:10.176Z
---

# Why Can't AI Make Its Own Discoveries? — With Yann LeCun

## 00:00 - 40:00

why has generative AI ingested all the

## 40:00 - 75:00

world's knowledge but not been able to

## 75:00 - 105:00

come up with scientific discoveries of

## 105:00 - 150:00

its own and has it finally starting to

## 150:00 - 180:00

understand the physical world we'll

## 180:00 - 230:00

discuss it with meta Chief AI scientist

## 230:00 - 280:00

and touring Award winner Yan laon

## 280:00 - 315:00

welcome to Big technology podcast a show

## 315:00 - 350:00

for cool-headed nuance conversation of

## 350:00 - 405:00

the tech world and Beyond I'm Alex cans

## 405:00 - 440:00

and I am thrilled to welcome Yan laon

## 440:00 - 480:00

the chief AI scientist touring Award

## 480:00 - 520:00

winner and a man known as The Godfather

## 520:00 - 565:00

of AI to Big technology podcast Yan

## 565:00 - 590:00

great to see you again welcome to the

## 590:00 - 630:00

show pleasure to be here let's start

## 630:00 - 660:00

with a question about scientific

## 660:00 - 700:00

discovery and why AI has not been able

## 700:00 - 735:00

to come up with it until this point this

## 735:00 - 765:00

is coming from dwares Patel he asked it

## 765:00 - 795:00

a couple months ago why do you make of

## 795:00 - 835:00

the fact that AIS generative AI

## 835:00 - 865:00

basically have the entire Corpus of

## 865:00 - 895:00

human knowledge memorized and they

## 895:00 - 925:00

haven't been able to make a single new

## 925:00 - 960:00

connection that has led to Discovery

## 960:00 - 1000:00

whereas if even a moderately intelligent

## 1000:00 - 1050:00

person had this much stuff memorized uh

## 1050:00 - 1075:00

they would notice oh this thing causes

## 1075:00 - 1110:00

this symptom this other thing causes

## 1110:00 - 1145:00

this symptom there might be a medical

## 1145:00 - 1175:00

cure here so shouldn't we be expecting

## 1175:00 - 1220:00

that type that type of stuff from AI

## 1220:00 - 1290:00

well from AI yes from large NE models no

## 1290:00 - 1330:00

you know there's several types of AI

## 1330:00 - 1375:00

architectures right and and all of a

## 1375:00 - 1415:00

sudden when we talk about AI we imagine

## 1415:00 - 1475:00

chatbots chatbots LMS are trained on an

## 1475:00 - 1505:00

enormous amount of of knowledge which is

## 1505:00 - 1550:00

purely text and they're trained to

## 1550:00 - 1600:00

basically regurgitate to retrieve to uh

## 1600:00 - 1625:00

essentially produce answers that are

## 1625:00 - 1660:00

conform to the statistics of whatever

## 1660:00 - 1700:00

text they've been trained on and it's

## 1700:00 - 1720:00

amazing what you can do with them it's

## 1720:00 - 1755:00

very useful there's no question about it

## 1755:00 - 1780:00

uh we also know that they can

## 1780:00 - 1835:00

hallucinate facts that AR true uh but

## 1835:00 - 1875:00

they really in their purest form they

## 1875:00 - 1920:00

are incapable of inventing new things

## 1920:00 - 1965:00

let me throw out this perspective that

## 1965:00 - 2000:00

uh Tom Wolf from hugging face shared on

## 2000:00 - 2030:00

LinkedIn over the past week I know you

## 2030:00 - 2065:00

were involved in a discussion about it

## 2065:00 - 2090:00

it's very interesting he says to create

## 2090:00 - 2135:00

an Einstein in a data center we don't

## 2135:00 - 2165:00

just need a system that knows all the

## 2165:00 - 2200:00

answers but rather one that can ask

## 2200:00 - 2230:00

questions nobody else has thought or

## 2230:00 - 2275:00

dared to ask one that writes what if

## 2275:00 - 2315:00

everything everyone is wrong about this

## 2315:00 - 2365:00

when all texperts textbooks experts and

## 2365:00 - 2410:00

common knowledge suggest

## 2410:00 - 2465:00

otherwise is it possible to teach llm to

## 2465:00 - 2505:00

do that no

## 2505:00 - 2555:00

no not not in the current form uh I mean

## 2555:00 - 2615:00

and and whatever form of AI would be

## 2615:00 - 2655:00

able to do that will not be llms they

## 2655:00 - 2715:00

might use llm as one component llms are

## 2715:00 - 2735:00

useful to

## 2735:00 - 2815:00

turn uh you know to produce text okay so

## 2815:00 - 2850:00

we might in the future AI systems we

## 2850:00 - 2900:00

might use them to turn abstract thoughts

## 2900:00 - 2930:00

into into

## 2930:00 - 2970:00

language uh in the human brain that's

## 2970:00 - 3000:00

done by a tiny little brain area right

## 3000:00 - 3030:00

here called the BR area it's about this

## 3030:00 - 3095:00

big um that's our LM okay but we don't

## 3095:00 - 3155:00

think in language we think in uh you

## 3155:00 - 3195:00

know mental representations of a

## 3195:00 - 3230:00

situation we have mental models of

## 3230:00 - 3250:00

everything we think about we can think

## 3250:00 - 3295:00

even if we can speak uh and that takes

## 3295:00 - 3330:00

place here that's like you know where

## 3330:00 - 3365:00

real intelligence is and that's the part

## 3365:00 - 3395:00

that we haven't reproduced certainly

## 3395:00 - 3450:00

with with llm so the question is

## 3450:00 - 3505:00

um you know is are we going to have

## 3505:00 - 3570:00

eventually ai architectures ai systems

## 3570:00 - 3630:00

that are capable of U not just answering

## 3630:00 - 3705:00

questions that already there but solving

## 3705:00 - 3765:00

giving new solutions to problems that we

## 3765:00 - 3830:00

specify the answer is yes eventually not

## 3830:00 - 3880:00

with current TMS um and then the next

## 3880:00 - 3910:00

question is are they going to be able to

## 3910:00 - 3940:00

ask their own questions like figure out

## 3940:00 - 3970:00

what are the good questions to answer

## 3970:00 - 4000:00

and the answer is eventually yes but

## 4000:00 - 4030:00

that's going to take a while before we

## 4030:00 - 4060:00

get machines that are capable of this

## 4060:00 - 4090:00

like you know in in humans we we have

## 4090:00 - 4120:00

all the characteristic we have people

## 4120:00 - 4150:00

who are who have extremely good memory

## 4150:00 - 4215:00

they can um you know retrieve a lot of

## 4215:00 - 4245:00

things they have a lot of accumulated

## 4245:00 - 4305:00

knowledge um we have people who are

## 4305:00 - 4330:00

problem solvers right you give them a

## 4330:00 - 4375:00

problem they'll solve it and I think uh

## 4375:00 - 4400:00

Toma was actually talking about this

## 4400:00 - 4415:00

kind of stuff he said like you know if

## 4415:00 - 4445:00

you're good at school you're a good

## 4445:00 - 4470:00

Problem Solver we give you a problem you

## 4470:00 - 4525:00

can solve it um and you score well in

## 4525:00 - 4585:00

math or physics or whatever it is um but

## 4585:00 - 4630:00

then in research the the most difficult

## 4630:00 - 4665:00

thing is to actually ask the right to

## 4665:00 - 4700:00

ask the the the good questions what are

## 4700:00 - 4735:00

the important questions it's not just

## 4735:00 - 4775:00

solving the problem it's also asking the

## 4775:00 - 4830:00

right questions kind of framing uh a

## 4830:00 - 4880:00

problem you know in the right way so so

## 4880:00 - 4940:00

you have kind of uh new insight and and

## 4940:00 - 4990:00

then after that comes okay I need to

## 4990:00 - 5020:00

turn this into equations or into

## 5020:00 - 5080:00

something you know practical a model um

## 5080:00 - 5105:00

and that may be a different scale from

## 5105:00 - 5145:00

the one that as the the the right

## 5145:00 - 5175:00

questions might be a different scale

## 5175:00 - 5230:00

also to um solve equations the people

## 5230:00 - 5245:00

who write the equations are not

## 5245:00 - 5270:00

necessarily the people who write them

## 5270:00 - 5345:00

who who solve them um and other people

## 5345:00 - 5375:00

who remember that there is you know some

## 5375:00 - 5405:00

textbook from 100 years ago where

## 5405:00 - 5435:00

similar equations were solved right

## 5435:00 - 5465:00

those are three different skills so LMS

## 5465:00 - 5515:00

are really good at retrieval not good at

## 5515:00 - 5545:00

solving new problems get you know

## 5545:00 - 5575:00

finding new solutions to new problems

## 5575:00 - 5615:00

they can retrieve existing Solutions and

## 5615:00 - 5650:00

they're certainly not good at all at

## 5650:00 - 5685:00

asking the right questions and for those

## 5685:00 - 5710:00

tuning in and and learning about this

## 5710:00 - 5740:00

for the first time LMS is the technology

## 5740:00 - 5775:00

behind things like the GPT model that's

## 5775:00 - 5825:00

within baked within uh Chad GPT but let

## 5825:00 - 5865:00

let me ask you this Yan so the AI field

## 5865:00 - 5895:00

does seem to have moved from standard

## 5895:00 - 5960:00

llms to LMS that can reason uh and go

## 5960:00 - 6000:00

step by step and I'm curious can can you

## 6000:00 - 6050:00

program this this sort of

## 6050:00 - 6095:00

counterintuitive or uh this heretical

## 6095:00 - 6145:00

thinking by imbuing a reasoning model

## 6145:00 - 6215:00

with an instruction to question its

## 6215:00 - 6260:00

directives well so we have to figure out

## 6260:00 - 6295:00

what reasoning really mean okay and

## 6295:00 - 6330:00

there are um you know obviously everyone

## 6330:00 - 6385:00

is trying to um get

## 6385:00 - 6440:00

llms to reason to some extent to perhaps

## 6440:00 - 6465:00

be able to check whether the answer they

## 6465:00 - 6525:00

produced are correct

## 6525:00 - 6555:00

um

## 6555:00 - 6610:00

and the way people are approaching the

## 6610:00 - 6665:00

problem at the moment is that they

## 6665:00 - 6695:00

basically are trying to do this by

## 6695:00 - 6720:00

modifying the current Paradigm without

## 6720:00 - 6780:00

completely changing it okay so can you

## 6780:00 - 6825:00

you know bolt a couple WS on top of llm

## 6825:00 - 6870:00

so that you kind of have some

## 6870:00 - 6910:00

primitive um reasoning function and

## 6910:00 - 6940:00

that's essentially what a lot of

## 6940:00 - 6980:00

reasoning systems are doing you know

## 6980:00 - 7010:00

when way

## 7010:00 - 7065:00

of uh getting itms to kind of appear to

## 7065:00 - 7100:00

reason is Chain of Thought right so you

## 7100:00 - 7145:00

basically tell them to generate more

## 7145:00 - 7180:00

tokens than they really need to in the

## 7180:00 - 7205:00

hope that in the process of generating

## 7205:00 - 7225:00

those tokens they're going to devote

## 7225:00 - 7275:00

more computation to answering a question

## 7275:00 - 7320:00

and uh to some extent that works

## 7320:00 - 7355:00

surprisingly but but it's very limited

## 7355:00 - 7410:00

you don't actually get uh real reasoning

## 7410:00 - 7475:00

um out of this uh reasoning at least in

## 7475:00 - 7530:00

classical AI is in many domain um

## 7530:00 - 7565:00

involves a search through a space of

## 7565:00 - 7605:00

potential Solutions okay so you have a

## 7605:00 - 7630:00

problem to solve you can characterize

## 7630:00 - 7660:00

whether the problem is solved or not so

## 7660:00 - 7680:00

you have some way of telling whether the

## 7680:00 - 7725:00

problem is solved um and then you search

## 7725:00 - 7750:00

through a space of solutions for when

## 7750:00 - 7790:00

that actually satisfies the the

## 7790:00 - 7835:00

constraints or you know is is identified

## 7835:00 - 7875:00

as being a solution

## 7875:00 - 7930:00

um and that you know that's how that's

## 7930:00 - 7955:00

kind of the most general form of of

## 7955:00 - 7995:00

reasoning you can imagine there is no

## 7995:00 - 8055:00

mechanism at all in llms for this search

## 8055:00 - 8095:00

mechanism what you have is you have to

## 8095:00 - 8125:00

kind of Bolt this on top of it right so

## 8125:00 - 8170:00

one way to do this is you get an LM to

## 8170:00 - 8195:00

produce lots and lots and lots of

## 8195:00 - 8230:00

sequences of answers right sequences of

## 8230:00 - 8270:00

tokens which you know represent answers

## 8270:00 - 8305:00

and then you have a separate system that

## 8305:00 - 8340:00

picks which one is good okay this is a

## 8340:00 - 8380:00

bit like writing a program by sort of

## 8380:00 - 8415:00

randomly more or less generating

## 8415:00 - 8470:00

instructions um you know while maybe

## 8470:00 - 8520:00

respecting the grammar of the of the

## 8520:00 - 8555:00

language uh and then checking all of

## 8555:00 - 8585:00

those programs for when that actually

## 8585:00 - 8630:00

works it not a good way not a very

## 8630:00 - 8665:00

efficient way of producing correct

## 8665:00 - 8705:00

pieces of code it's not a good way of

## 8705:00 - 8775:00

reasoning uh either so um a big issue

## 8775:00 - 8820:00

there is is that when when humans or

## 8820:00 - 8885:00

animals reason we don't do it in token

## 8885:00 - 8925:00

space in other words when we reason we

## 8925:00 - 8975:00

don't have to you know generate a text

## 8975:00 - 9020:00

that expresses solution um and then

## 9020:00 - 9045:00

generate another one and then generate

## 9045:00 - 9075:00

another one and then among other ones we

## 9075:00 - 9125:00

we produce pick the one that is good we

## 9125:00 - 9160:00

reason internally right we have a mental

## 9160:00 - 9195:00

model of the situation and we manipulate

## 9195:00 - 9235:00

it in our head and we find kind of a

## 9235:00 - 9265:00

good solution when we plan a sequence of

## 9265:00 - 9310:00

actions to I don't know you know build a

## 9310:00 - 9360:00

table or something um we we plan the

## 9360:00 - 9390:00

sequence of action you know we have a

## 9390:00 - 9430:00

mental model of that in your head if I

## 9430:00 - 9465:00

if I tell you and this has nothing to do

## 9465:00 - 9505:00

with language okay so if I tell you

## 9505:00 - 9540:00

imagine a cube floating in front in

## 9540:00 - 9580:00

front of us right now now rotate that

## 9580:00 - 9635:00

Cube 90° along a vertical axis okay you

## 9635:00 - 9700:00

can imagine this this thing taking place

## 9700:00 - 9735:00

and you can readily observe that it's a

## 9735:00 - 9780:00

cube if I wrot it it 90° it's going to

## 9780:00 - 9820:00

look just like the cube that I started

## 9820:00 - 9870:00

with okay um because you have this metal

## 9870:00 - 9940:00

model of of a cube um and that reasoning

## 9940:00 - 9975:00

is in some abstract continuous space

## 9975:00 - 10010:00

it's not in text it's not related to

## 10010:00 - 10085:00

language or or anything like that um and

## 10085:00 - 10110:00

humans do this all the time animals do

## 10110:00 - 10155:00

this all the time and this is what we

## 10155:00 - 10205:00

yet cannot reproduce uh with with

## 10205:00 - 10240:00

machines yeah it reminds me you're

## 10240:00 - 10265:00

talking through Chain of Thought and how

## 10265:00 - 10310:00

it doesn't produce much novel insights

## 10310:00 - 10340:00

and um when deep SE came out one of the

## 10340:00 - 10375:00

big screenshots that was going around

## 10375:00 - 10420:00

was someone asking deep seek for a novel

## 10420:00 - 10450:00

Insight on The Human Condition and as

## 10450:00 - 10475:00

you read it it's one another one of

## 10475:00 - 10515:00

these very like clever tricks the AI PS

## 10515:00 - 10545:00

because it does seem like it's running

## 10545:00 - 10565:00

through all these different like very

## 10565:00 - 10595:00

interesting observations about humans

## 10595:00 - 10665:00

how we take our uh our our hate like our

## 10665:00 - 10695:00

violent side and we Channel it towards

## 10695:00 - 10720:00

cooperation instead of competition and

## 10720:00 - 10750:00

that helps us build more and then you're

## 10750:00 - 10775:00

like as you read The Chain of Thought

## 10775:00 - 10795:00

you're like this is kind of just like

## 10795:00 - 10825:00

you read sapiens and maybe some other

## 10825:00 - 10860:00

books and that's your Chain of Thought

## 10860:00 - 10905:00

pretty much yeah I mean yeah a lot of it

## 10905:00 - 10980:00

is uh regation I'm now going to move a

## 10980:00 - 11020:00

part the conversation I had later closer

## 11020:00 - 11095:00

up which is the wall uh effectively is

## 11095:00 - 11130:00

training standard large language models

## 11130:00 - 11170:00

coming close to hitting a wall whereas

## 11170:00 - 11210:00

before there was somewhat predictable uh

## 11210:00 - 11235:00

returns if you put a number a certain

## 11235:00 - 11260:00

amount of data and a certain amount of

## 11260:00 - 11295:00

compute towards training these models

## 11295:00 - 11360:00

you can make them predictably better um

## 11360:00 - 11425:00

as we're talking it seems to me like you

## 11425:00 - 11475:00

believe that that is eventually not

## 11475:00 - 11495:00

going to be true

## 11495:00 - 11520:00

well it I don't know if I would call it

## 11520:00 - 11545:00

a wall but it's certainly diminishing

## 11545:00 - 11580:00

return in the sense that you know we've

## 11580:00 - 11630:00

kind of run out of natural Text data to

## 11630:00 - 11660:00

train those those llms where they're

## 11660:00 - 11695:00

already trained with you know on the

## 11695:00 - 11755:00

order of uh you know 10 to the 13 or 10

## 11755:00 - 11810:00

to the 14 tokens that's a lot that's a

## 11810:00 - 11845:00

lot and that's the the whole internet

## 11845:00 - 11870:00

that's all the publicly available

## 11870:00 - 11890:00

internet and then you know some

## 11890:00 - 11940:00

company's license uh uh content that is

## 11940:00 - 11975:00

not publicly available and then there is

## 11975:00 - 12000:00

talks about like you know generating

## 12000:00 - 12040:00

artificial data and then hiring

## 12040:00 - 12080:00

thousands of people to kind of you know

## 12080:00 - 12120:00

generate more data other knowledge phds

## 12120:00 - 12170:00

and professors yeah but in fact it could

## 12170:00 - 12190:00

be even simpler than this because most

## 12190:00 - 12215:00

of the systems actually don't understand

## 12215:00 - 12280:00

basic logic for example right so um so

## 12280:00 - 12300:00

to some extent you know there going to

## 12300:00 - 12320:00

be slow

## 12320:00 - 12370:00

progress uh along those lines with uh

## 12370:00 - 12415:00

synthetic data with you know hiring more

## 12415:00 - 12470:00

people to you know plug the holes in the

## 12470:00 - 12495:00

in the sort of you know knowledge

## 12495:00 - 12545:00

background of uh of uh of of those

## 12545:00 - 12580:00

systems but but it's diminishing return

## 12580:00 - 12630:00

right the the costs are ballooning of uh

## 12630:00 - 12675:00

generating that data and the the returns

## 12675:00 - 12730:00

are are are not not that great so we

## 12730:00 - 12795:00

need a new paradig okay we need um a new

## 12795:00 - 12835:00

kind of architecture of systems that at

## 12835:00 - 12885:00

the you know at the core are capable of

## 12885:00 - 12950:00

those uh search and uh um you know

## 12950:00 - 12975:00

searching for a good solution checking

## 12975:00 - 13015:00

whether that solution is good planning

## 13015:00 - 13040:00

for a sequence of actions to arrive at a

## 13040:00 - 13075:00

particular goal which is what you would

## 13075:00 - 13100:00

need for an agentic system to really

## 13100:00 - 13140:00

work everybody is talking about agentic

## 13140:00 - 13165:00

system nobody has any idea how to build

## 13165:00 - 13210:00

them other than uh basically

## 13210:00 - 13250:00

regurgitating plant that have the system

## 13250:00 - 13285:00

has already been trained on okay so you

## 13285:00 - 13325:00

know it's like it's like everything in

## 13325:00 - 13365:00

computer science you you can you can

## 13365:00 - 13390:00

engineer a

## 13390:00 - 13465:00

solution uh which is limited for for in

## 13465:00 - 13510:00

the context of AI

## 13510:00 - 13535:00

uh you

## 13535:00 - 13580:00

can make a system that is you know based

## 13580:00 - 13620:00

on on learning or retrieval with

## 13620:00 - 13660:00

enormous amounts of data but really the

## 13660:00 - 13700:00

complex things the complex thing is uh

## 13700:00 - 13725:00

how you build a system that can solve

## 13725:00 - 13745:00

new problems without being trained to

## 13745:00 - 13780:00

solve those problems we are capable of

## 13780:00 - 13810:00

doing this animals are capable of doing

## 13810:00 - 13865:00

this facing a new situation we can

## 13865:00 - 13930:00

either uh Solve IT zero shot without

## 13930:00 - 13960:00

without training ourselves to handle

## 13960:00 - 13995:00

that situation just a first time we

## 13995:00 - 14010:00

encounter

## 14010:00 - 14065:00

it or we can learn to solve it extremely

## 14065:00 - 14140:00

quickly so for example um you know we we

## 14140:00 - 14195:00

we can learn to drive in you know couple

## 14195:00 - 14245:00

dozen hours of practice

## 14245:00 - 14320:00

um and to the point that after 20 30

## 14320:00 - 14355:00

hours it becomes kind of a second nature

## 14355:00 - 14385:00

where this become kind of subconscious

## 14385:00 - 14410:00

we don't don't think about it you don't

## 14410:00 - 14430:00

need to think about it you can speaking

## 14430:00 - 14455:00

of system one system two right that's

## 14455:00 - 14505:00

right so you know the we calls the

## 14505:00 - 14550:00

discussion we had with with Denny kenman

## 14550:00 - 14595:00

a few years ago so um you know the the

## 14595:00 - 14630:00

first time you drive your system too is

## 14630:00 - 14670:00

all uh present you have to use it to

## 14670:00 - 14700:00

imagine all kind of catastroph scenarios

## 14700:00 - 14735:00

and stuff like that right your full

## 14735:00 - 14780:00

attention is devoted to to driving but

## 14780:00 - 14820:00

then after a number of hours you know

## 14820:00 - 14845:00

you can talk to someone at the same time

## 14845:00 - 14865:00

like you don't need to think about it

## 14865:00 - 14905:00

it's become sort of subconscious and

## 14905:00 - 14935:00

more or less automatic um it's become

## 14935:00 - 14970:00

system one and pretty much every task

## 14970:00 - 14995:00

that we

## 14995:00 - 15035:00

you know learn that we accomplished the

## 15035:00 - 15065:00

first time we have to use the full power

## 15065:00 - 15105:00

of our of our minds and then eventually

## 15105:00 - 15145:00

if we repeat them uh sufficiently many

## 15145:00 - 15170:00

times they get they get kind of

## 15170:00 - 15225:00

subconscious I have this vivid memory of

## 15225:00 - 15265:00

uh once being in a a workshop where one

## 15265:00 - 15305:00

of the participants was a chess grandmas

## 15305:00 - 15330:00

and he played a simultaneous game

## 15330:00 - 15365:00

against like 50 of us right you know

## 15365:00 - 15410:00

going from from one person to another

## 15410:00 - 15435:00

you know I got wiped out in 10 turns or

## 15435:00 - 15460:00

something I'm terrible the chess right

## 15460:00 - 15500:00

but um so he would come you know come to

## 15500:00 - 15530:00

my my table and you

## 15530:00 - 15575:00

know had time to think about this cuz he

## 15575:00 - 15600:00

you know he was playing the other 50

## 15600:00 - 15640:00

tables or something so I make my move in

## 15640:00 - 15705:00

front of it it goes like what and then

## 15705:00 - 15730:00

immediately plays so I doesn't have to

## 15730:00 - 15785:00

think about it um I was not a a

## 15785:00 - 15820:00

challenging enough opponent that he had

## 15820:00 - 15870:00

to actually call his system two his

## 15870:00 - 15930:00

system one was sufficient to beat me um

## 15930:00 - 15970:00

and uh what that tells you is that when

## 15970:00 - 16000:00

you become familiar with the task and

## 16000:00 - 16030:00

you you train you train yourself you

## 16030:00 - 16065:00

know it it kind of uh become

## 16065:00 - 16115:00

subconscious but the but the essential

## 16115:00 - 16150:00

ability of humans and many animals is

## 16150:00 - 16195:00

that when you face a new situation you

## 16195:00 - 16210:00

you

## 16210:00 - 16270:00

can think about it figure out a sequence

## 16270:00 - 16310:00

of actions a course of action to

## 16310:00 - 16345:00

accomplish a goal um and you don't need

## 16345:00 - 16380:00

to know much about about the situation

## 16380:00 - 16405:00

other than your common knowledge of how

## 16405:00 - 16430:00

the world Works basically that's what

## 16430:00 - 16475:00

we're missing okay with the with the I

## 16475:00 - 16490:00

systems

## 16490:00 - 16520:00

and it's okay now now I really have to

## 16520:00 - 16540:00

blow up the order here because youve

## 16540:00 - 16560:00

said some very interesting things that

## 16560:00 - 16600:00

we have to talk about um you talked

## 16600:00 - 16650:00

about how basically llms have hit the

## 16650:00 - 16675:00

point of diminishing returns large

## 16675:00 - 16690:00

language models the things that have

## 16690:00 - 16720:00

gotten us here and we need a new

## 16720:00 - 16760:00

paradigm but it also seems to me that

## 16760:00 - 16820:00

that new paradigm is isn't here yet and

## 16820:00 - 16845:00

I know you're working on the research

## 16845:00 - 16865:00

for it and we're going to talk about

## 16865:00 - 16910:00

that what the next new paradigm might be

## 16910:00 - 16940:00

but there's a real timeline issue don't

## 16940:00 - 16985:00

you think because I'm just thinking

## 16985:00 - 17010:00

about the money that's been raised and

## 17010:00 - 17060:00

put into this yes last year 6.6 billion

## 17060:00 - 17105:00

to open AI uh last week or a couple

## 17105:00 - 17135:00

weeks ago another three and a half

## 17135:00 - 17180:00

billion to anthropic after they raised 4

## 17180:00 - 17225:00

billion uh last year Elon Musk is

## 17225:00 - 17265:00

putting another you know another small

## 17265:00 - 17315:00

fortune into into building grock these

## 17315:00 - 17365:00

are all llm first companies they're not

## 17365:00 - 17390:00

searching out the ne I mean maybe open

## 17390:00 - 17440:00

AI is but that 6.6 billion that they got

## 17440:00 - 17495:00

was because of chat GPT so

## 17495:00 - 17525:00

where's this field going to go because

## 17525:00 - 17570:00

if that money is being invested into

## 17570:00 - 17610:00

something that is at the point of

## 17610:00 - 17645:00

diminishing returns requiring a new

## 17645:00 - 17680:00

paradigm to progress that sounds like a

## 17680:00 - 17725:00

real problem well um I mean we have some

## 17725:00 - 17775:00

ideas about what this parad uh is the

## 17775:00 - 17810:00

the difficulty that I mean what we're

## 17810:00 - 17855:00

working on is trying to make it work um

## 17855:00 - 17875:00

and it's you know it's not simple that

## 17875:00 - 17905:00

that take that may take uh that may take

## 17905:00 - 17980:00

years and so the question is um is the

## 17980:00 - 18020:00

the all the capabilities we're talking

## 18020:00 - 18045:00

about perhaps through this new paradigm

## 18045:00 - 18065:00

that we're thinking of that we're

## 18065:00 - 18125:00

working on uh is it going to come uh

## 18125:00 - 18175:00

quickly enough to justify all all of

## 18175:00 - 18195:00

this uh

## 18195:00 - 18235:00

investment uh and if it doesn't come

## 18235:00 - 18290:00

quickly enough is the investment still

## 18290:00 - 18320:00

Justified okay so the first thing you

## 18320:00 - 18365:00

can say is we are not going to get to

## 18365:00 - 18415:00

human level AI by just scaning up LMS

## 18415:00 - 18460:00

this is just not going to happen Okay

## 18460:00 - 18505:00

that's your perspective is no way okay

## 18505:00 - 18575:00

absolutely no way um and and whatever

## 18575:00 - 18620:00

you can hear from some of my uh more

## 18620:00 - 18660:00

adventurous colleagues uh it's not going

## 18660:00 - 18695:00

to happen within the next two years

## 18695:00 - 18730:00

there's absolutely no way in hell to you

## 18730:00 - 18790:00

know pardon my French um the you know

## 18790:00 - 18815:00

the idea that we we're going to have you

## 18815:00 - 18835:00

know a country of Genius in the data

## 18835:00 - 18875:00

center that's complete BS right it's

## 18875:00 - 18900:00

absolutely no way what we're going to

## 18900:00 - 18940:00

have maybe is systems that are trained

## 18940:00 - 18975:00

on sufficiently large amounts of data

## 18975:00 - 18985:00

that

## 18985:00 - 19015:00

any question that any reasonable person

## 19015:00 - 19045:00

may ask will will find an answer through

## 19045:00 - 19080:00

those systems and it would feel like you

## 19080:00 - 19115:00

have you know a PhD sitting next to you

## 19115:00 - 19150:00

but it's not a PhD you have next to you

## 19150:00 - 19215:00

it's you know a system with gigantic uh

## 19215:00 - 19265:00

memory and retrieval ability not not a

## 19265:00 - 19310:00

system that can invent solutions to to

## 19310:00 - 19355:00

new problems um which is really what a

## 19355:00 - 19420:00

phg is okay this is actually it's it's

## 19420:00 - 19465:00

you know connected to this post that uh

## 19465:00 - 19490:00

Tom Tom

## 19490:00 - 19590:00

W made that uh um you you you

## 19590:00 - 19635:00

you inventing new things you know

## 19635:00 - 19665:00

requires

## 19665:00 - 19720:00

uh the the type of uh skill and

## 19720:00 - 19755:00

abilities that uh you're not going to

## 19755:00 - 19820:00

get from from from ANS so

## 19820:00 - 19895:00

um so this's big question which is the

## 19895:00 - 19925:00

investment that is being done now is not

## 19925:00 - 19960:00

done for tomorrow it's not it's done for

## 19960:00 - 19990:00

you know the next few years

## 19990:00 - 20030:00

and most of the investment at least for

## 20030:00 - 20075:00

from The Meta side is investment in uh

## 20075:00 - 20120:00

infrastructure for inference okay so

## 20120:00 - 20145:00

let's imagine that by the end of the

## 20145:00 - 20190:00

year which is really the plan at MAA we

## 20190:00 - 20260:00

have 1 billion users of meta AI through

## 20260:00 - 20305:00

smart glasses you know Standalone app

## 20305:00 - 20355:00

and and whatever um you got to serve

## 20355:00 - 20375:00

those people and that's a lot of

## 20375:00 - 20400:00

computation so that's why you need you

## 20400:00 - 20430:00

know a lot of investment in

## 20430:00 - 20460:00

infrastructure to be able to scale this

## 20460:00 - 20500:00

up and you know build it up over months

## 20500:00 - 20540:00

or or years

## 20540:00 - 20570:00

um and so that you know that's where

## 20570:00 - 20630:00

most of the money is going um at least

## 20630:00 - 20665:00

on on you know on the side of companies

## 20665:00 - 20710:00

like like like MAA Microsoft and and and

## 20710:00 - 20740:00

Google and potentially

## 20740:00 - 20765:00

Amazon

## 20765:00 - 20820:00

um then there is so this is just

## 20820:00 - 20890:00

operations essentially now is there

## 20890:00 - 20960:00

going to be the the market for um you

## 20960:00 - 20995:00

know 1 billion people using those things

## 20995:00 - 21030:00

regularly even if there is no change of

## 21030:00 - 21070:00

Paradigm and the answer is probably yes

## 21070:00 - 21115:00

so you know even if the revolution of

## 21115:00 - 21135:00

new paradigm doesn't come you know

## 21135:00 - 21170:00

within three years this infrastructure

## 21170:00 - 21195:00

is going to be used is there's very

## 21195:00 - 21230:00

little question about that okay so it's

## 21230:00 - 21265:00

a good investment and it takes so long

## 21265:00 - 21315:00

to set up you know data centers and all

## 21315:00 - 21340:00

that stuff that you need to to get

## 21340:00 - 21390:00

started now and plan for you know

## 21390:00 - 21440:00

progress to be continuous uh so that uh

## 21440:00 - 21485:00

you know eventually the investment is is

## 21485:00 - 21515:00

Justified but you can't afford not to do

## 21515:00 - 21565:00

it right because um because there would

## 21565:00 - 21595:00

be too much of a of a risk to take if

## 21595:00 - 21625:00

you have the cash but let's go back to

## 21625:00 - 21655:00

what you said the stuff today is still

## 21655:00 - 21685:00

deeply flawed and there have been

## 21685:00 - 21720:00

questions about whether it's going to be

## 21720:00 - 21755:00

used now meta is making this consumer

## 21755:00 - 21785:00

BET right the consumers want to use the

## 21785:00 - 21835:00

AI that makes sense open AI has 400

## 21835:00 - 21865:00

million users of chat

## 21865:00 - 21915:00

GPT meta has three four billion I mean

## 21915:00 - 21965:00

basically if you have a phone three 3

## 21965:00 - 21985:00

something billion

## 21985:00 - 22050:00

users uh 600 million users of

## 22050:00 - 22110:00

M right okay so more than chat jpt yeah

## 22110:00 - 22155:00

but but it's not used as much as so the

## 22155:00 - 22205:00

users are not as intense but basically

## 22205:00 - 22230:00

the idea that that meta can get to a

## 22230:00 - 22265:00

billion consumer users yeah that seems

## 22265:00 - 22305:00

reasonable but the thing is a lot of

## 22305:00 - 22350:00

this investment has been made with the

## 22350:00 - 22380:00

idea that this will be useful to

## 22380:00 - 22430:00

Enterprises uh not just a consumer app

## 22430:00 - 22465:00

and there's a problem because like we've

## 22465:00 - 22480:00

been talking about but it's not good

## 22480:00 - 22525:00

enough yet uh you look at Deep research

## 22525:00 - 22545:00

this is something Benedict devans has

## 22545:00 - 22600:00

brought up deep research is pretty good

## 22600:00 - 22645:00

but it might only get you 95% of the way

## 22645:00 - 22695:00

there and maybe 5% of it hallucinates so

## 22695:00 - 22730:00

if you have a 100 page research report

## 22730:00 - 22760:00

and 5% of it is wrong and you don't know

## 22760:00 - 22810:00

what 5% that's that's a problem and

## 22810:00 - 22860:00

similarly in in Enterprises

## 22860:00 - 22895:00

today all every Enterprise is trying to

## 22895:00 - 22935:00

figure out how to make uh AI useful to

## 22935:00 - 22975:00

them uh generative AI useful to them and

## 22975:00 - 23050:00

other types of AI uh but only 10% or 20%

## 23050:00 - 23080:00

maybe of proof of Concepts make it out

## 23080:00 - 23115:00

the door into production because there

## 23115:00 - 23140:00

it's either too expensive or it's

## 23140:00 - 23195:00

fallible so if this is if we are getting

## 23195:00 - 23250:00

to the top here uh what do you

## 23250:00 - 23290:00

anticipate is going to happen with with

## 23290:00 - 23330:00

everything that's that that has been

## 23330:00 - 23370:00

pushed in the anticipation that it is

## 23370:00 - 23440:00

going to get even better from

## 23440:00 - 23475:00

here well so again it's a question

## 23475:00 - 23505:00

timeline right when when are those

## 23505:00 - 23550:00

systems going to become sufficiently

## 23550:00 - 23595:00

reliable and intelligent so that the

## 23595:00 - 23650:00

deployment is made easier um but but you

## 23650:00 - 23685:00

know I mean this this situation you're

## 23685:00 - 23720:00

describing

## 23720:00 - 23760:00

that you know beyond the impressive

## 23760:00 - 23795:00

demos actually deploying systems that

## 23795:00 - 23855:00

are reliable is where things tend to

## 23855:00 - 23920:00

falter in in the use of computers and

## 23920:00 - 23955:00

Technologies and particularly AI this is

## 23955:00 - 24000:00

not new um it's it's

## 24000:00 - 24070:00

basically um you know why we we had

## 24070:00 - 24080:00

super

## 24080:00 - 24135:00

impressive you know autonomous driving

## 24135:00 - 24205:00

demos 10 years ago um but we still don't

## 24205:00 - 24265:00

have level five s driving cars right um

## 24265:00 - 24315:00

it's the last mile that's really

## 24315:00 - 24370:00

difficult uh so to speak for cars you

## 24370:00 - 24410:00

know it's you know the last the last

## 24410:00 - 24470:00

few that was not deliberate the you know

## 24470:00 - 24515:00

last few few percent of reliability

## 24515:00 - 24580:00

which makes a system uh practical um and

## 24580:00 - 24605:00

how you integrate it with sort of

## 24605:00 - 24650:00

existing systems and and and blah blah

## 24650:00 - 24700:00

blah and you know how it makes uh users

## 24700:00 - 24745:00

of it more efficient if you want or more

## 24745:00 - 24820:00

reliable or or whatever um that's where

## 24820:00 - 24840:00

that's where it's that's where it's

## 24840:00 - 24900:00

difficult um and you know this is why if

## 24900:00 - 24930:00

we take if we go back several several

## 24930:00 - 24970:00

years and we look what happened with IDM

## 24970:00 - 25020:00

wetson okay so wetson was going to be

## 25020:00 - 25070:00

the thing that you know IBM was was

## 25070:00 - 25100:00

going to push and generate tons of

## 25100:00 - 25155:00

Revenue by by having wson uh you know

## 25155:00 - 25180:00

learn about medicine and then be

## 25180:00 - 25240:00

deployed in every um every

## 25240:00 - 25285:00

hospital and it was basically a complete

## 25285:00 - 25340:00

failure and was sold for parts right um

## 25340:00 - 25380:00

and cost a lot of money to to IBM

## 25380:00 - 25445:00

including the CEO and the what happens

## 25445:00 - 25480:00

is that actually deploying those system

## 25480:00 - 25515:00

in in situations where they are reliable

## 25515:00 - 25570:00

and and actually help people and don't

## 25570:00 - 25610:00

like hurt the natural conservativism of

## 25610:00 - 25665:00

the of the labor force um this is where

## 25665:00 - 25695:00

things become complicated we're seeing

## 25695:00 - 25720:00

the same you know the process we're

## 25720:00 - 25745:00

seeing now with the difficulty of

## 25745:00 - 25785:00

deploying a system is not new it's it's

## 25785:00 - 25835:00

it's happened absolutely at at all times

## 25835:00 - 25890:00

this is also why you know some some of

## 25890:00 - 25915:00

your listeners perhaps are too young to

## 25915:00 - 25940:00

remember this but there was a big wave

## 25940:00 - 26010:00

of interest in AI in 1980s early 1980s

## 26010:00 - 26070:00

um around expert systems um and you know

## 26070:00 - 26110:00

the the hottest job in the 1980s was

## 26110:00 - 26150:00

going was going to be knowledge engineer

## 26150:00 - 26175:00

and your job was going to be to sit next

## 26175:00 - 26225:00

to an expert and then you know turn the

## 26225:00 - 26260:00

knowledge of the expert into rules and

## 26260:00 - 26325:00

facts that would then be fed to a um

## 26325:00 - 26355:00

inference engine that would be able to

## 26355:00 - 26385:00

kind of derive new facts and and answer

## 26385:00 - 26440:00

questions and blah blah blah um big wave

## 26440:00 - 26485:00

of interest uh the ja government started

## 26485:00 - 26510:00

a big program called fifth generation

## 26510:00 - 26545:00

computer the hardware was going to be

## 26545:00 - 26570:00

designed to actually take care of that

## 26570:00 - 26605:00

and blah blah blah you know mostly

## 26605:00 - 26665:00

mostly a failure there was kind of

## 26665:00 - 26710:00

a you know the wave of Interest kind of

## 26710:00 - 26765:00

died in the the mid90s about this and

## 26765:00 - 26800:00

and you know a few companies were

## 26800:00 - 26850:00

successful but basically for a narrow

## 26850:00 - 26890:00

set of applications for which you could

## 26890:00 - 26920:00

actually reduce human knowledge to a

## 26920:00 - 26980:00

bunch of rules and for which um it was

## 26980:00 - 27040:00

econom economically feasible to do so um

## 27040:00 - 27080:00

but the the the wide ranging impact on

## 27080:00 - 27125:00

all of society and industry was just not

## 27125:00 - 27195:00

there and so that's a denture of uh of

## 27195:00 - 27230:00

AI all the time um I mean the the

## 27230:00 - 27290:00

signals are clear that you know still um

## 27290:00 - 27340:00

llms with all the Bears and whistles

## 27340:00 - 27370:00

actually play an important role if

## 27370:00 - 27415:00

nothing else for information retrieval

## 27415:00 - 27455:00

uh you know most companies want to have

## 27455:00 - 27500:00

some sort of internal experts that know

## 27500:00 - 27530:00

all the internal documents so that any

## 27530:00 - 27570:00

employee can ask any question we have

## 27570:00 - 27600:00

one at MAA it's called Metate it's

## 27600:00 - 27635:00

really cool it's very useful yeah and

## 27635:00 - 27680:00

I'm I'm not suggesting that AI is gonna

## 27680:00 - 27715:00

that modern AI is not or modern general

## 27715:00 - 27790:00

of AI is not useful or U I'm I'm asking

## 27790:00 - 27840:00

purely that there's been a lot of money

## 27840:00 - 27880:00

that's been invested into expecting this

## 27880:00 - 27915:00

stuff to effectively achieve God level

## 27915:00 - 27965:00

capabilities and we both are talking

## 27965:00 - 27985:00

about how like there's you know

## 27985:00 - 28025:00

potentially diminishing returns here and

## 28025:00 - 28055:00

then what happens if there's that

## 28055:00 - 28095:00

timeline mismatch like you mentioned and

## 28095:00 - 28125:00

um this is the last question I'll ask

## 28125:00 - 28145:00

about it because I feel like we have so

## 28145:00 - 28190:00

much else to cover but I feel like

## 28190:00 - 28230:00

timeline mismatches uh that might be

## 28230:00 - 28270:00

personal to you you and I first spoke

## 28270:00 - 28315:00

nine years ago which is crazy now nine

## 28315:00 - 28395:00

years ago uh and you know about how in

## 28395:00 - 28435:00

the early days you had an idea for how

## 28435:00 - 28470:00

AI should be structured and you couldn't

## 28470:00 - 28515:00

even get a seat at the conferences um

## 28515:00 - 28540:00

and then eventually with the right

## 28540:00 - 28570:00

amount of when when the right amount of

## 28570:00 - 28595:00

compute came around those ideas started

## 28595:00 - 28645:00

working and then the entire AI field

## 28645:00 - 28685:00

took off based off of your idea that you

## 28685:00 - 28745:00

you worked on with Benjo and Hinton um

## 28745:00 - 28775:00

but and a bunch of others and many

## 28775:00 - 28825:00

others uh and but for the sake of

## 28825:00 - 28870:00

efficiency we'll say go look it up um

## 28870:00 - 28905:00

but just talking about those mismatch

## 28905:00 - 28945:00

timelines when there have been overhyped

## 28945:00 - 28985:00

moments uh the AI field maybe with the

## 28985:00 - 29005:00

expert systems that you were just

## 29005:00 - 29030:00

talking about and they don't pan out the

## 29030:00 - 29075:00

way that people expect the AI field goes

## 29075:00 - 29100:00

into what's called AI winter well

## 29100:00 - 29140:00

there's a backlash yeah correct and so

## 29140:00 - 29175:00

if we're going to if we are potentially

## 29175:00 - 29205:00

approaching this moment of mismatch

## 29205:00 - 29245:00

timelines do you fear that there could

## 29245:00 - 29280:00

be another winter now given the amount

## 29280:00 - 29315:00

of investment uh given the fact that

## 29315:00 - 29330:00

there's going to be potentially

## 29330:00 - 29370:00

diminishing returns with the main way of

## 29370:00 - 29410:00

training these things and maybe we'll

## 29410:00 - 29455:00

add in the fact that the market is is

## 29455:00 - 29480:00

the stock market looks like it's going

## 29480:00 - 29515:00

through a bit of a downturn right now

## 29515:00 - 29550:00

now that's a variable uh probably the

## 29550:00 - 29575:00

third most important variable of what

## 29575:00 - 29620:00

we're talking about but it has to factor

## 29620:00 - 29675:00

so I yeah I I think um I mean there's

## 29675:00 - 29715:00

certainly a question of timing there but

## 29715:00 - 29760:00

I think uh if we try to dig a little bit

## 29760:00 - 29810:00

deeper um as I said before if you think

## 29810:00 - 29830:00

that we're going to get to human level

## 29830:00 - 29855:00

AI by just training on more data and

## 29855:00 - 29890:00

scanning up LMS you're making a mistake

## 29890:00 - 29930:00

so if you're if you're an investor and

## 29930:00 - 29960:00

you invested in a company that told you

## 29960:00 - 29985:00

we're going to get to human level Ai and

## 29985:00 - 30025:00

PhD level by just you know training on

## 30025:00 - 30085:00

more data and with a few tricks um I

## 30085:00 - 30100:00

don't know if you're going to use your

## 30100:00 - 30130:00

shirt but that was probably not a good

## 30130:00 - 30200:00

idea um however there are ideas about

## 30200:00 - 30250:00

how to uh go forward and have systems

## 30250:00 - 30305:00

that are capable of doing what what

## 30305:00 - 30350:00

every intelligent animal and and human

## 30350:00 - 30390:00

are capable of doing and that current a

## 30390:00 - 30425:00

systems are not capable of doing and I'm

## 30425:00 - 30450:00

I'm talking about understanding the

## 30450:00 - 30475:00

physical world

## 30475:00 - 30510:00

um having persistent memory and being

## 30510:00 - 30540:00

able to reason and plan those are the

## 30540:00 - 30580:00

four characteristics that that you know

## 30580:00 - 30625:00

need to be there um and that require

## 30625:00 - 30650:00

systems that you know can acquire common

## 30650:00 - 30700:00

sense that can learn from uh natural

## 30700:00 - 30735:00

sensors like video as opposed to just

## 30735:00 - 30800:00

text just human produced uh data um and

## 30800:00 - 30820:00

that's a big challenge I mean I've been

## 30820:00 - 30855:00

talking about this for many years now

## 30855:00 - 30895:00

and uh and saying this is this is where

## 30895:00 - 30935:00

the challenge is this is what we have to

## 30935:00 - 30975:00

uh to figure out and and

## 30975:00 - 31005:00

my group and I have or people working

## 31005:00 - 31040:00

with me and others who have listened to

## 31040:00 - 31090:00

me are making progress along along this

## 31090:00 - 31140:00

line uh of uh system that can be trained

## 31140:00 - 31165:00

to understand how the world works on

## 31165:00 - 31210:00

video for example systems that can use

## 31210:00 - 31245:00

Mental models of how the world the

## 31245:00 - 31275:00

physical world Works to plan sequences

## 31275:00 - 31305:00

of actions to arrive at a particular

## 31305:00 - 31355:00

goal so we we have kind of early results

## 31355:00 - 31385:00

of this kind of systems U and there are

## 31385:00 - 31410:00

people at Deep mind working on similar

## 31410:00 - 31430:00

things and there you know people in

## 31430:00 - 31475:00

various universities working on this uh

## 31475:00 - 31525:00

so um the question is you know when is

## 31525:00 - 31570:00

this going to go from uh interesting

## 31570:00 - 31625:00

research papers uh demonstrating a new

## 31625:00 - 31670:00

capability with a new architecture to

## 31670:00 - 31715:00

you know architectures at scale that you

## 31715:00 - 31735:00

know are practical for a lot of

## 31735:00 - 31780:00

applications and can find solutions to

## 31780:00 - 31805:00

new problems without being trained to do

## 31805:00 - 31860:00

it um Etc

## 31860:00 - 31910:00

and you know it it's not going to happen

## 31910:00 - 31935:00

within the next three years but it may

## 31935:00 - 31975:00

happen with you know between 3 to 5

## 31975:00 - 32000:00

years something like that and that's

## 32000:00 - 32040:00

kind of corresponds to you know the sort

## 32040:00 - 32110:00

of ramp up that we see in uh uh in in

## 32110:00 - 32150:00

investment now whether

## 32150:00 - 32190:00

other so so that that's the first thing

## 32190:00 - 32210:00

now the the second thing that's

## 32210:00 - 32235:00

important is that there's not going to

## 32235:00 - 32300:00

be one secret Magic Bullet that one

## 32300:00 - 32335:00

company or one group of people is going

## 32335:00 - 32375:00

to invent that is going to just solve

## 32375:00 - 32440:00

the problem um it's going to be a lot of

## 32440:00 - 32475:00

different ideas a lot of effort some

## 32475:00 - 32515:00

principles around which to base this

## 32515:00 - 32550:00

that that some people may may not

## 32550:00 - 32600:00

subscribe to and will will go um in a

## 32600:00 - 32625:00

direction that is you know well turn out

## 32625:00 - 32685:00

to be a dead end uh so there's not going

## 32685:00 - 32725:00

to be like a

## 32725:00 - 32765:00

day before which there is no AGI and

## 32765:00 - 32800:00

after which we have AGI this is not

## 32800:00 - 32855:00

going to be an event um it's going to be

## 32855:00 - 32925:00

continuous conceptual ideas that as time

## 32925:00 - 32970:00

goes by are going to be made bigger and

## 32970:00 - 33005:00

to scale and going to work better and

## 33005:00 - 33030:00

it's not going to come from a single

## 33030:00 - 33050:00

entity it's going to come from the

## 33050:00 - 33075:00

entire research Community across the

## 33075:00 - 33110:00

world and the people who share their

## 33110:00 - 33135:00

research are going to move faster than

## 33135:00 - 33180:00

the ones that don't and so if you think

## 33180:00 - 33215:00

that there is some startup somewhere

## 33215:00 - 33250:00

with five people who has discovered the

## 33250:00 - 33290:00

secret of a GI and you should invest

## 33290:00 - 33325:00

five billion in them you're making a

## 33325:00 - 33370:00

huge mistake you know Yan first of all I

## 33370:00 - 33400:00

always enjoy our conversations because

## 33400:00 - 33425:00

we start to get some real answers and I

## 33425:00 - 33455:00

remember even from our last conversation

## 33455:00 - 33470:00

I was just

## 33470:00 - 33490:00

and always looking back to that

## 33490:00 - 33520:00

conversation saying okay this is what

## 33520:00 - 33550:00

Yan says this is what everybody else is

## 33550:00 - 33580:00

saying I'm pretty sure that this is the

## 33580:00 - 33605:00

grounding point and that's been

## 33605:00 - 33630:00

corrected I know we're going to do that

## 33630:00 - 33665:00

with this one as well and now you've set

## 33665:00 - 33715:00

me up for two uh interesting threads

## 33715:00 - 33745:00

that we're going to pull out um as we go

## 33745:00 - 33785:00

on with our conversation first is the

## 33785:00 - 33810:00

understanding of physics and the real

## 33810:00 - 33845:00

world and the second is open source so

## 33845:00 - 33865:00

we'll do that when we come back right

## 33865:00 - 33905:00

after this and we're back here with Yan

## 33905:00 - 33955:00

laon he is the chief AI scientist at

## 33955:00 - 33990:00

meta the touring Award winner that we're

## 33990:00 - 34020:00

thrilled to have on our show luckily for

## 34020:00 - 34055:00

the third time um I want to talk to you

## 34055:00 - 34095:00

about physics Yan because there's sort

## 34095:00 - 34130:00

of this famous moment in big technology

## 34130:00 - 34155:00

podcast history and I say famous with

## 34155:00 - 34185:00

our listeners I don't know if it really

## 34185:00 - 34220:00

extended Beyond but you had

## 34220:00 - 34280:00

me uh uh write to chat GPT if I hold a

## 34280:00 - 34310:00

paper horizontally with both hands and

## 34310:00 - 34340:00

let it let the go let go of the paper

## 34340:00 - 34390:00

with my left hand uh what will happen

## 34390:00 - 34420:00

and uh I write it and it convincingly

## 34420:00 - 34450:00

says like it writes though the physics

## 34450:00 - 34480:00

will will happen and the paper will

## 34480:00 - 34520:00

float towards your left hand and I read

## 34520:00 - 34545:00

it out loud convinced and you're like

## 34545:00 - 34570:00

that thing just hallucinated and you

## 34570:00 - 34615:00

believed it that is what happened so

## 34615:00 - 34645:00

listen it's been two years I put the

## 34645:00 - 34720:00

test to chat PT today uh it says um when

## 34720:00 - 34745:00

you let go of the paper with your left

## 34745:00 - 34780:00

hand grav gravity will cause the left

## 34780:00 - 34810:00

side of the paper to drop while the

## 34810:00 - 34835:00

right side still held up by your right

## 34835:00 - 34865:00

hand remains in place this creates a

## 34865:00 - 34905:00

pivot effect where the paper rotates

## 34905:00 - 34940:00

around the point where your right hand

## 34940:00 - 34965:00

is hting it

## 34965:00 - 35000:00

so now it gets it right it learned the

## 35000:00 - 35040:00

lesson you know it's quite possible that

## 35040:00 - 35125:00

this uh um you know some someone hired

## 35125:00 - 35170:00

by open AI to solve the problem was fed

## 35170:00 - 35205:00

that question and sort of fed the answer

## 35205:00 - 35230:00

and the system was fine tune with the

## 35230:00 - 35265:00

answer I mean you know obviously you can

## 35265:00 - 35300:00

imagine an infinite number of such

## 35300:00 - 35355:00

questions and and this is where you know

## 35355:00 - 35395:00

uh the the the So-Cal post training of

## 35395:00 - 35450:00

LM becomes expensive um which is that

## 35450:00 - 35480:00

you know how much coverage of all those

## 35480:00 - 35515:00

style of questions do you have to do for

## 35515:00 - 35565:00

the system to basically cover 90% of or

## 35565:00 - 35605:00

95% or whatever percentage of all the

## 35605:00 - 35650:00

questions that people may ask it um but

## 35650:00 - 35690:00

there you know it's there's a long tale

## 35690:00 - 35730:00

and there's no way you can train the

## 35730:00 - 35760:00

system to answer all possible questions

## 35760:00 - 35785:00

because there is an essentially infinite

## 35785:00 - 35825:00

number of them and and there is way more

## 35825:00 - 35875:00

question the system cannot answer that

## 35875:00 - 35910:00

um then questions he can it can answer

## 35910:00 - 35940:00

you cannot cover the set of all possible

## 35940:00 - 35985:00

training uh you know questions in the

## 35985:00 - 36025:00

training the training set right so

## 36025:00 - 36055:00

because I think our conversation last

## 36055:00 - 36095:00

time was saying you you said that

## 36095:00 - 36130:00

because these actions of like what's

## 36130:00 - 36150:00

happening with the paper if you let go

## 36150:00 - 36180:00

of it with your hand has not been

## 36180:00 - 36215:00

covered widely in text the model won't

## 36215:00 - 36240:00

really know how to handle it because

## 36240:00 - 36270:00

unless it's been covered in text the

## 36270:00 - 36290:00

model won't have that understanding

## 36290:00 - 36320:00

won't have that inherent understanding

## 36320:00 - 36350:00

right of the real world and I've kind of

## 36350:00 - 36405:00

gone with that for a while uh then I

## 36405:00 - 36435:00

said you know what let's let's try to

## 36435:00 - 36465:00

generate some AI videos

## 36465:00 - 36490:00

and one of the interesting things that

## 36490:00 - 36525:00

I've seen with the AI videos is there is

## 36525:00 - 36560:00

some understanding of how the physical

## 36560:00 - 36620:00

world works there um in a way that in

## 36620:00 - 36645:00

our first meeting nine years ago you

## 36645:00 - 36680:00

said um one of the hardest things to do

## 36680:00 - 36715:00

is you ask an AI what happens if you

## 36715:00 - 36755:00

hold a pen vertically on a table and let

## 36755:00 - 36800:00

go uh will it fall and there's like an

## 36800:00 - 36835:00

unbelievable amount of permutations uh

## 36835:00 - 36865:00

that can occur and it's very very

## 36865:00 - 36900:00

difficult for the AI to figure that out

## 36900:00 - 36940:00

because it just doesn't inherently

## 36940:00 - 36970:00

understand physics but now you go to

## 36970:00 - 37025:00

something like Sora uh and you say um

## 37025:00 - 37075:00

show me a a video of a man sitting on a

## 37075:00 - 37135:00

chair kicking his legs and you can get

## 37135:00 - 37175:00

that video and the person sits on the

## 37175:00 - 37215:00

chair and they kick their legs and the

## 37215:00 - 37250:00

legs you know don't fall out of their

## 37250:00 - 37290:00

sockets or stuff they Bend at the joints

## 37290:00 - 37315:00

and they don't have three legs and they

## 37315:00 - 37345:00

don't have three legs so wouldn't that

## 37345:00 - 37365:00

suggest an improvement of the

## 37365:00 - 37400:00

capabilities here with these large large

## 37400:00 - 37470:00

models no why because you still have

## 37470:00 - 37520:00

those videos produced by those uh video

## 37520:00 - 37555:00

generation system where you know you

## 37555:00 - 37600:00

spill a glass of wine and and the wine

## 37600:00 - 37640:00

like floats in the air or like flies off

## 37640:00 - 37720:00

or disappears or whatever and um so you

## 37720:00 - 37755:00

know of course for every specific

## 37755:00 - 37795:00

situation you can always collect more

## 37795:00 - 37820:00

data for that situation and then train

## 37820:00 - 37870:00

your model to handle it but that's not

## 37870:00 - 37900:00

really understanding the underlying

## 37900:00 - 37940:00

reality this is just you know

## 37940:00 - 37970:00

compensating

## 37970:00 - 38030:00

uh the the lack of understanding by uh

## 38030:00 - 38075:00

increasingly large amounts of data um

## 38075:00 - 38090:00

you know

## 38090:00 - 38120:00

children

## 38120:00 - 38180:00

understand uh you know simple Concepts

## 38180:00 - 38195:00

like like

## 38195:00 - 38250:00

gravity um with a surprisingly small

## 38250:00 - 38265:00

amount of

## 38265:00 - 38305:00

data um so in fact there is an

## 38305:00 - 38350:00

interesting calculation you you can do

## 38350:00 - 38385:00

which I've talked about publicly before

## 38385:00 - 38460:00

but um if you take llm typical LM train

## 38460:00 - 38490:00

on 30 trillion tokens something like

## 38490:00 - 38540:00

that right 310 to the 13 tokens a token

## 38540:00 - 38595:00

is about three bytes so that's .9 10 to

## 38595:00 - 38630:00

the 14 tokens let's say 10 to the 14

## 38630:00 - 38700:00

tokens to to round this up

## 38700:00 - 38775:00

um that text would take any of us

## 38775:00 - 38805:00

probably some on the order of 400,000

## 38805:00 - 38840:00

years to read right no

## 38840:00 - 38920:00

problem at 12 hours a day okay um

## 38920:00 - 38985:00

now um if for old has been awake a total

## 38985:00 - 39005:00

of 16,000

## 39005:00 - 39065:00

hours uh you can multiply by 3600 to

## 39065:00 - 39090:00

give number of seconds and then you can

## 39090:00 - 39120:00

put a number on how like how much data

## 39120:00 - 39155:00

has got into your visual cortex through

## 39155:00 - 39195:00

the optic nerve optic nerve each optic

## 39195:00 - 39220:00

nerve we have two of them carries about

## 39220:00 - 39270:00

one meab per second roughly right so

## 39270:00 - 39325:00

it's 2 megabytes per second uh time 3600

## 39325:00 - 39345:00

time

## 39345:00 - 39380:00

16,000 and that's just about 10 to the

## 39380:00 - 39440:00

14 bytes okay so in four years a child

## 39440:00 - 39470:00

has seen through vision or touch for

## 39470:00 - 39530:00

that matter as much data as the biggest

## 39530:00 - 39585:00

LMS and and it tells you clearly that

## 39585:00 - 39610:00

we're not going to get to human level by

## 39610:00 - 39650:00

just training on text it's just not a

## 39650:00 - 39695:00

rich enough source of information um and

## 39695:00 - 39735:00

by the way 16,000 hours is not that much

## 39735:00 - 39790:00

video it's 30 minutes of YouTube uploads

## 39790:00 - 39825:00

okay uh we can get that pretty easily

## 39825:00 - 39885:00

now in N months uh baby has

## 39885:00 - 39945:00

seen you know um let's say 10 to the 13

## 39945:00 - 40005:00

bytes something which is not not much

## 40005:00 - 40095:00

again um and in that in that time baby

## 40095:00 - 40125:00

has learned basically all of intuitive

## 40125:00 - 40175:00

physics that that uh that that that we

## 40175:00 - 40230:00

know about um you know conservation

## 40230:00 - 40255:00

momentum gravity conservation of

## 40255:00 - 40285:00

momentum the fact that object don't

## 40285:00 - 40315:00

spontaneously disappear the fact that

## 40315:00 - 40345:00

they still exist even if you hide them I

## 40345:00 - 40370:00

mean there's all kinds of stuff you know

## 40370:00 - 40395:00

very basic stuff that we learn about the

## 40395:00 - 40445:00

world in the first few months of life um

## 40445:00 - 40465:00

and this is what we need to reproduce

## 40465:00 - 40490:00

with machine this type of learning of

## 40490:00 - 40540:00

you know figuring out uh what is

## 40540:00 - 40570:00

possible and impossible in the world

## 40570:00 - 40615:00

what will result from an action you take

## 40615:00 - 40650:00

um so that you can plan a sequence of

## 40650:00 - 40680:00

actions to arrive at a particular goal

## 40680:00 - 40730:00

that's the idea of world model and now

## 40730:00 - 40765:00

connected with the question about uh

## 40765:00 - 40810:00

video generation systems is the right

## 40810:00 - 40845:00

way to approach this problem to train

## 40845:00 - 40870:00

better and better video generation

## 40870:00 - 40905:00

systems and my answer to this is

## 40905:00 - 40975:00

absolutely no um

## 40975:00 - 41020:00

the the problem of understanding the

## 41020:00 - 41055:00

world does not go

## 41055:00 - 41120:00

through the solution to the to to

## 41120:00 - 41175:00

generating video at the pixel level okay

## 41175:00 - 41230:00

I don't need to know um if I if I take

## 41230:00 - 41305:00

this uh this glass of uh of this cup of

## 41305:00 - 41345:00

of water and I spill it I cannot

## 41345:00 - 41395:00

entirely predict you know the exact path

## 41395:00 - 41450:00

of that the water will will uh follow on

## 41450:00 - 41475:00

the table and what shape it's going to

## 41475:00 - 41500:00

take and all that stuff what noise it's

## 41500:00 - 41555:00

going to make um but at a certain level

## 41555:00 - 41590:00

of obstruction I can make a prediction

## 41590:00 - 41610:00

that the water will

## 41610:00 - 41655:00

spill okay and it it you know probably

## 41655:00 - 41725:00

make my phone wet and everything so um

## 41725:00 - 41780:00

so at a I can't predict all the details

## 41780:00 - 41805:00

but I can predict at some level of

## 41805:00 - 41855:00

abstraction and I think that's really a

## 41855:00 - 41890:00

critical concept the fact that if you

## 41890:00 - 41940:00

want a system to be able to learn to

## 41940:00 - 41965:00

comprehend

## 41965:00 - 41995:00

the the world and understand how the

## 41995:00 - 42050:00

world works it needs to be able to learn

## 42050:00 - 42070:00

an abstract

## 42070:00 - 42105:00

representation of the world that allows

## 42105:00 - 42180:00

you to make those prediction and um what

## 42180:00 - 42205:00

that means is that those architectures

## 42205:00 - 42220:00

will not be

## 42220:00 - 42275:00

generative right and uh I want to get to

## 42275:00 - 42300:00

your solution here in a moment but I

## 42300:00 - 42330:00

just wanted to also like what would a

## 42330:00 - 42355:00

conversation between us be without a

## 42355:00 - 42390:00

demo so I want to just show you I'm

## 42390:00 - 42415:00

going to put this on the screen when we

## 42415:00 - 42450:00

do the video but there's this is a video

## 42450:00 - 42490:00

pretty proud of I got this guy sitting

## 42490:00 - 42535:00

on a chair kicking his legs out and the

## 42535:00 - 42570:00

legs stay attached to his body and I was

## 42570:00 - 42595:00

like all right this stuff is making real

## 42595:00 - 42630:00

progress and then I said can I get a car

## 42630:00 - 42670:00

going into a Hy stack and so it's two

## 42670:00 - 42720:00

bales of hay stacks and then a Hy stack

## 42720:00 - 42770:00

magically emerges from the hood of a car

## 42770:00 - 42810:00

that's stationary and I just said to

## 42810:00 - 42865:00

myself okay yan yan wins again it's it's

## 42865:00 - 42910:00

nice car though yeah I mean the thing is

## 42910:00 - 42955:00

those systems have been fine tun with a

## 42955:00 - 42985:00

huge amount of data for humans because

## 42985:00 - 43020:00

you know that's that's what people are

## 43020:00 - 43080:00

asking most videos they ask to so so

## 43080:00 - 43115:00

there is a lot of data of humans doing

## 43115:00 - 43145:00

various things to to train those th

## 43145:00 - 43185:00

those uh those systems so that's why it

## 43185:00 - 43220:00

works for humans but not for a situation

## 43220:00 - 43265:00

that the the people training that system

## 43265:00 - 43305:00

had not anticipated so you said that the

## 43305:00 - 43345:00

model can't be generative to be able to

## 43345:00 - 43385:00

understand the real world uh you are

## 43385:00 - 43445:00

working on something called V jeppa JEA

## 43445:00 - 43485:00

JEA right V is the video you also have I

## 43485:00 - 43530:00

JEA for images right that is we have

## 43530:00 - 43570:00

jads for all kinds of stuff text also

## 43570:00 - 43615:00

and text so explain how that will solve

## 43615:00 - 43650:00

the problem of being able to allow a

## 43650:00 - 43695:00

machine to abstractly represent what is

## 43695:00 - 43730:00

going on in the real world okay so what

## 43730:00 - 43770:00

has made the success of

## 43770:00 - 43845:00

uh Ai and particularly um natural

## 43845:00 - 43880:00

language understanding in chatbot in the

## 43880:00 - 43925:00

last few years but also to some extent

## 43925:00 - 43965:00

computer vision is self-supervised

## 43965:00 - 44000:00

learning so what is self-supervised

## 44000:00 - 44055:00

learning it's um take an input be it an

## 44055:00 - 44100:00

image a video a piece of text

## 44100:00 - 44170:00

whatever uh corrupt it in some way and

## 44170:00 - 44230:00

train a big neural net to reconstruct it

## 44230:00 - 44265:00

basically recover the uncorrupted

## 44265:00 - 44300:00

version of it or the undistorted version

## 44300:00 - 44335:00

of it or a transformed version of it

## 44335:00 - 44380:00

that would result from taking an action

## 44380:00 - 44405:00

okay

## 44405:00 - 44485:00

um and you know that that would mean um

## 44485:00 - 44515:00

for example in the context of text take

## 44515:00 - 44545:00

a piece of text remove some of the words

## 44545:00 - 44565:00

and then train some big neural net to

## 44565:00 - 44600:00

prct the words that are missing take an

## 44600:00 - 44630:00

image remove some pieces of it and then

## 44630:00 - 44660:00

train bigal net to recover the full

## 44660:00 - 44710:00

image take a video remove a piece of it

## 44710:00 - 44740:00

train that to predict what's missing

## 44740:00 - 44805:00

okay so llms are a special case of this

## 44805:00 - 44890:00

where um you you you take a a text and

## 44890:00 - 44915:00

you train the system to just reproduce

## 44915:00 - 44945:00

the text and you don't need to corrupt

## 44945:00 - 44980:00

the text text because the system is

## 44980:00 - 45005:00

designed in such a way that to predict

## 45005:00 - 45040:00

one particular word or token in the text

## 45040:00 - 45075:00

it can only look at the tokens that are

## 45075:00 - 45140:00

to the left of it okay so so in effect

## 45140:00 - 45170:00

the system has hardwired into its

## 45170:00 - 45200:00

architecture the fact that it cannot

## 45200:00 - 45240:00

look at the present in the future U to

## 45240:00 - 45265:00

predict the present it can only look at

## 45265:00 - 45325:00

the past okay so but basically you train

## 45325:00 - 45350:00

that system to just reproduce its input

## 45350:00 - 45400:00

on its output okay um so this kind of

## 45400:00 - 45420:00

Architecture is called a causal

## 45420:00 - 45470:00

architecture and this is what an llm is

## 45470:00 - 45500:00

a large language model that's what you

## 45500:00 - 45530:00

know all the chatbots in the world are

## 45530:00 - 45570:00

are based on um take a piece of text to

## 45570:00 - 45595:00

and train the system to just reproduce a

## 45595:00 - 45635:00

piece of text on its output um and to

## 45635:00 - 45660:00

predict a particular word it can only

## 45660:00 - 45700:00

look at the word to the to the left of

## 45700:00 - 45745:00

it and so now what you have is a system

## 45745:00 - 45770:00

that given a piece of text can predict

## 45770:00 - 45840:00

the word that that follows um that text

## 45840:00 - 45865:00

and you can take

## 45865:00 - 45920:00

that uh that word that is predicted uh

## 45920:00 - 45955:00

shift it into the input and then predict

## 45955:00 - 45990:00

the second word shift that into the

## 45990:00 - 46010:00

input predict the third word that's

## 46010:00 - 46040:00

called Auto reive prediction it's not a

## 46040:00 - 46110:00

New Concept very old um so you know self

## 46110:00 - 46150:00

supervisor learning does not train to do

## 46150:00 - 46195:00

a particular does not uh train a system

## 46195:00 - 46225:00

to accomplish a particular task other

## 46225:00 - 46275:00

than capture the internal structure of

## 46275:00 - 46305:00

the of the data it doesn't require any

## 46305:00 - 46360:00

labeling by by human Okay so apply these

## 46360:00 - 46425:00

to images um take an image mask a chunk

## 46425:00 - 46475:00

of it like a bunch of

## 46475:00 - 46500:00

Patches from it if you want and then

## 46500:00 - 46525:00

train a begin on that

## 46525:00 - 46595:00

to reconstruct that that what is

## 46595:00 - 46630:00

missing and now use the internal

## 46630:00 - 46660:00

representation of the image learned by

## 46660:00 - 46720:00

the system um as input to a subsequent

## 46720:00 - 46750:00

Downstream task for I don't know image

## 46750:00 - 46790:00

recognition segmentation whatever it is

## 46790:00 - 46810:00

it works to some

## 46810:00 - 46870:00

extent but not great um so there was a

## 46870:00 - 46905:00

big project like this uh to do this at

## 46905:00 - 46945:00

Fair it's called ma Max Auto encoder

## 46945:00 - 46985:00

it's a special case of doing Auto which

## 46985:00 - 47020:00

itself is you know the sort of General

## 47020:00 - 47075:00

framework from which I um I derive this

## 47075:00 - 47140:00

this idea self supervis running so um it

## 47140:00 - 47160:00

doesn't work so

## 47160:00 - 47210:00

well um and there's various ways to you

## 47210:00 - 47235:00

know if you apply this to video also

## 47235:00 - 47270:00

I've been working on this for almost 20

## 47270:00 - 47330:00

years now take a video show just the a

## 47330:00 - 47350:00

piece of the video and then train the

## 47350:00 - 47370:00

system to predict what's going to happen

## 47370:00 - 47405:00

next in the video so same idea as for

## 47405:00 - 47470:00

text but just for for video

## 47470:00 - 47505:00

and that doesn't work very well either

## 47505:00 - 47545:00

um and the reason it doesn't work why

## 47545:00 - 47575:00

does it work for text and not for video

## 47575:00 - 47590:00

for

## 47590:00 - 47635:00

example um and the answer

## 47635:00 - 47715:00

is it's easy to predict a word that

## 47715:00 - 47755:00

comes after a text you cannot exactly

## 47755:00 - 47790:00

predict which word follows a particular

## 47790:00 - 47840:00

text but you can produce something like

## 47840:00 - 47870:00

a probability distribution over all the

## 47870:00 - 47895:00

possible words in your dictionary all

## 47895:00 - 47930:00

the possible tokens is only about you

## 47930:00 - 47975:00

know 100 thousand possible tokens so you

## 47975:00 - 48020:00

you just produce a big Vector with you

## 48020:00 - 48055:00

know 100 thousand different numbers that

## 48055:00 - 48130:00

are positive and some to one okay um now

## 48130:00 - 48150:00

what are you going to

## 48150:00 - 48205:00

do to represent a probability

## 48205:00 - 48240:00

distribution of all possible frames in a

## 48240:00 - 48290:00

video or all possible missing parts of

## 48290:00 - 48330:00

an image we don't know how to do this

## 48330:00 - 48370:00

properly in fact it's mathematically

## 48370:00 - 48405:00

intractable to represent distributions

## 48405:00 - 48440:00

in high dimensional continuous spaces

## 48440:00 - 48485:00

okay we don't know how to do this in a

## 48485:00 - 48560:00

kind of useful way if you want um and so

## 48560:00 - 48590:00

and I've tried to you know do this for

## 48590:00 - 48630:00

video for a long time

## 48630:00 - 48700:00

um and so that is the reason why those

## 48700:00 - 48735:00

idea of s supervis learning using

## 48735:00 - 48785:00

generative models have failed so far and

## 48785:00 - 48820:00

this is why you know using uh you know

## 48820:00 - 48855:00

trying to train a video generation

## 48855:00 - 48895:00

system as a way to understand to get a

## 48895:00 - 48915:00

system to understand how the world works

## 48915:00 - 48950:00

that's why it's it can't

## 48950:00 - 49005:00

Ed um so what's the alternative the

## 49005:00 - 49055:00

alternative is something that is not a

## 49055:00 - 49095:00

gener generative architecture uh which

## 49095:00 - 49120:00

we call jepa so that means joint

## 49120:00 - 49160:00

embedding predictive architecture and we

## 49160:00 - 49195:00

know this works much better than

## 49195:00 - 49240:00

attempting to reconstruct so we we've

## 49240:00 - 49310:00

had uh experimental uh results on

## 49310:00 - 49355:00

learning good representations of of

## 49355:00 - 49390:00

images going back many

## 49390:00 - 49450:00

years where instead of taking an image

## 49450:00 - 49470:00

corrupting it and attempting to

## 49470:00 - 49530:00

reconstruct this image we take the

## 49530:00 - 49570:00

original full image and the corrupted

## 49570:00 - 49615:00

version we run them both through neural

## 49615:00 - 49645:00

Nets those neural Nets produce

## 49645:00 - 49690:00

representations of those of those two

## 49690:00 - 49750:00

images the initial one and the corrupted

## 49750:00 - 49800:00

one and we train another neur a

## 49800:00 - 49830:00

predictor to predict the representation

## 49830:00 - 49850:00

of the full image from the

## 49850:00 - 49950:00

representation of the corrupted one okay

## 49950:00 - 49980:00

and if you train a system if you

## 49980:00 - 50010:00

successfully train a system of this type

## 50010:00 - 50040:00

this this is not trained to reconstruct

## 50040:00 - 50075:00

anything it's just trained to learn a

## 50075:00 - 50105:00

representation so that you can make

## 50105:00 - 50125:00

prediction within the representation

## 50125:00 - 50160:00

layer and you have to make sure that the

## 50160:00 - 50185:00

representation contains as much

## 50185:00 - 50210:00

information as possible about the input

## 50210:00 - 50235:00

which is where it's difficult actually

## 50235:00 - 50255:00

that's the difficult part of training

## 50255:00 - 50290:00

those systems so that's called a jepa

## 50290:00 - 50320:00

joint embedding predictive

## 50320:00 - 50400:00

architecture um and to to train a system

## 50400:00 - 50435:00

to learn good representations of images

## 50435:00 - 50450:00

those

## 50450:00 - 50490:00

joint embedding architectures work much

## 50490:00 - 50520:00

better than the ones that are generative

## 50520:00 - 50545:00

that are trained by

## 50545:00 - 50580:00

reconstruction um and now we have a

## 50580:00 - 50610:00

version that works for video too so we

## 50610:00 - 50675:00

take a video we corrupt it by masking a

## 50675:00 - 50715:00

big chunk of it we run the full video

## 50715:00 - 50755:00

and the corrupted one through encoders

## 50755:00 - 50785:00

that are identical and then and

## 50785:00 - 50815:00

simultaneously we train a predictor to

## 50815:00 - 50850:00

predict the representation of the full

## 50850:00 - 50895:00

video from the partial one

## 50895:00 - 50935:00

and the representation that the system

## 50935:00 - 50985:00

learns of videos when you feed it to a

## 50985:00 - 51040:00

system that you try to tell you for

## 51040:00 - 51060:00

example what action is taking place in

## 51060:00 - 51105:00

the video or whether the video is

## 51105:00 - 51145:00

possible or impossible or things like

## 51145:00 - 51190:00

that it actually works quite well um

## 51190:00 - 51215:00

that's cool so it gives that abstract

## 51215:00 - 51255:00

thinking yeah in a way right and and we

## 51255:00 - 51285:00

have experimental result that shows that

## 51285:00 - 51320:00

this joint embedding training we have

## 51320:00 - 51360:00

several methods for doing this uh there

## 51360:00 - 51380:00

one that's called Dino another one

## 51380:00 - 51420:00

that's called VC rag another one that's

## 51420:00 - 51450:00

Vic another one that's called

## 51450:00 - 51495:00

IA but which is sort of distillation

## 51495:00 - 51545:00

method um and so we you know several

## 51545:00 - 51585:00

different ways to to approach this but

## 51585:00 - 51635:00

one of those is going to lead to a

## 51635:00 - 51670:00

recipe that basically gives us a general

## 51670:00 - 51710:00

way of training those jaer architectures

## 51710:00 - 51730:00

okay so it's not generative because the

## 51730:00 - 51765:00

system is not trying to regenerate the

## 51765:00 - 51805:00

part of the input it's trying to

## 51805:00 - 51845:00

generate a representation an abstract

## 51845:00 - 51875:00

representation of the input and what

## 51875:00 - 51920:00

that allows it to do is to ignore all

## 51920:00 - 51960:00

the details about the that are really

## 51960:00 - 52005:00

not predictable like you know the the

## 52005:00 - 52045:00

pen that you put on the table vertically

## 52045:00 - 52065:00

and when you let it go you cannot

## 52065:00 - 52085:00

predict in which direction is going to

## 52085:00 - 52120:00

fall but at some abstract level you can

## 52120:00 - 52145:00

say that the pen is going to fall

## 52145:00 - 52180:00

falling right without representing the

## 52180:00 - 52225:00

direction um so so that's the that's the

## 52225:00 - 52270:00

idea of jepa and and we're starting to

## 52270:00 - 52350:00

have you know good results on sort of um

## 52350:00 - 52385:00

having systems so VJ system for example

## 52385:00 - 52410:00

is train on natural lots of natural

## 52410:00 - 52455:00

videos and then you can show it a video

## 52455:00 - 52500:00

that's impossible like a video where for

## 52500:00 - 52540:00

example an object disappears or changes

## 52540:00 - 52580:00

shape okay you can generate this with a

## 52580:00 - 52630:00

game engine or something or a situation

## 52630:00 - 52660:00

where you have a ball rolling and it

## 52660:00 - 52720:00

rolls and it starts behind a screen and

## 52720:00 - 52745:00

then the screen comes down and the bll

## 52745:00 - 52790:00

is not there anymore right okay um so

## 52790:00 - 52845:00

things like this and you measure the

## 52845:00 - 52870:00

prediction error of the system so the

## 52870:00 - 52910:00

system is training to predict right and

## 52910:00 - 52945:00

not necessarily in time but but like

## 52945:00 - 52990:00

basically to predict you know the the

## 52990:00 - 53025:00

the sort of coherence of the video and

## 53025:00 - 53070:00

so you you measure the prediction error

## 53070:00 - 53110:00

as you show the the video to the system

## 53110:00 - 53140:00

and when something impossible occurs the

## 53140:00 - 53165:00

prediction error goes goes through the

## 53165:00 - 53215:00

roof and so you can detect if the system

## 53215:00 - 53265:00

has integrated some idea of what you

## 53265:00 - 53300:00

know is possible physically or what's

## 53300:00 - 53345:00

not possible but just being trained with

## 53345:00 - 53395:00

physically possible natural videos um so

## 53395:00 - 53420:00

that that's really interesting that's s

## 53420:00 - 53450:00

of the first hint

## 53450:00 - 53475:00

that a system is a quite suable common

## 53475:00 - 53520:00

sense and yes um we have versions of

## 53520:00 - 53550:00

those system also that are soal action

## 53550:00 - 53585:00

conditions so basically we have things

## 53585:00 - 53640:00

where we have a chunk of video or an

## 53640:00 - 53680:00

image of you know the state of the world

## 53680:00 - 53710:00

at time T and then an action is being

## 53710:00 - 53755:00

taken like you know a robot arm is being

## 53755:00 - 53800:00

moved or whatever and then of course we

## 53800:00 - 53860:00

can observe the the result um resulting

## 53860:00 - 53895:00

from this action so now what we have

## 53895:00 - 53955:00

when when we train a jeta with this um

## 53955:00 - 53985:00

the the model basically can say here is

## 53985:00 - 54010:00

the state of the world at time T here is

## 54010:00 - 54040:00

an action you might take I can predict

## 54040:00 - 54060:00

the state of the world at time t plus

## 54060:00 - 54095:00

one in this abstract representation

## 54095:00 - 54120:00

space there's this learning of of how

## 54120:00 - 54145:00

the world works of how the world works

## 54145:00 - 54170:00

and and the cool thing about this is

## 54170:00 - 54220:00

that now you can imagine you can have

## 54220:00 - 54250:00

the system imagine what would be the

## 54250:00 - 54285:00

outcome of a sequence of actions and if

## 54285:00 - 54315:00

you give it a goal saying like I want

## 54315:00 - 54350:00

the world to look like this at the end

## 54350:00 - 54375:00

can you figure out a sequence of actions

## 54375:00 - 54410:00

to get me to that point it can actually

## 54410:00 - 54445:00

figure out by search

## 54445:00 - 54485:00

for a sequence of actions that will

## 54485:00 - 54510:00

actually produce that result that's

## 54510:00 - 54540:00

planning that's reasoning that's actual

## 54540:00 - 54575:00

reasoning and actual planning okay I

## 54575:00 - 54600:00

have to get you out here where we are

## 54600:00 - 54635:00

over time but can you give me like 60

## 54635:00 - 54680:00

seconds your reaction uh to deep seek

## 54680:00 - 54730:00

and sort of has open source overtaken

## 54730:00 - 54775:00

the propriety proprietary models at this

## 54775:00 - 54810:00

point and we got a limit to 60 seconds

## 54810:00 - 54840:00

otherwise I'm going to get uh killed by

## 54840:00 - 54890:00

your team here so overtaken is a is a

## 54890:00 - 54930:00

strong word I think uh progress is

## 54930:00 - 54955:00

faster in the open source world that's

## 54955:00 - 54990:00

for sure but of course you know uh the

## 54990:00 - 55035:00

pro proprietary shops are profiting from

## 55035:00 - 55075:00

the progress of the open source world

## 55075:00 - 55100:00

right they get access to that

## 55100:00 - 55165:00

information like everybody else um so

## 55165:00 - 55195:00

what what's clear is that there is many

## 55195:00 - 55225:00

more interesting ideas coming out of the

## 55225:00 - 55275:00

open source world that any single shop

## 55275:00 - 55330:00

as big as it can be cannot come up with

## 55330:00 - 55360:00

you know nobody has a monopoly and good

## 55360:00 - 55420:00

ideas and so the magic efficiency of the

## 55420:00 - 55460:00

open source world is is that uh it

## 55460:00 - 55500:00

recruits talents from all over the world

## 55500:00 - 55525:00

and so what we've seen with deeps is

## 55525:00 - 55570:00

that if you set up a small team with a

## 55570:00 - 55615:00

relatively Long Leash and few

## 55615:00 - 55645:00

constraints on coming up with just the

## 55645:00 - 55705:00

next generation of of of llms they can

## 55705:00 - 55725:00

actually come up with new ideas that

## 55725:00 - 55750:00

nobody else had come up with right they

## 55750:00 - 55790:00

can so reinvent a little bit what what

## 55790:00 - 55825:00

uh you know how you do things and then

## 55825:00 - 55855:00

if they share that with the rest of the

## 55855:00 - 55895:00

world then the entire world progresses

## 55895:00 - 55945:00

okay and so um

## 55945:00 - 56010:00

uh the the it's it it clearly shows that

## 56010:00 - 56060:00

um you know open source progresses

## 56060:00 - 56130:00

faster um and um you know a lot more

## 56130:00 - 56160:00

Innovation can can take place in the

## 56160:00 - 56190:00

open source World which the provider

## 56190:00 - 56215:00

world may have hard time catching up

## 56215:00 - 56280:00

with uh is cheaper to run what we see is

## 56280:00 - 56320:00

uh for you know Partners who we we talk

## 56320:00 - 56360:00

to um they say well our clients when

## 56360:00 - 56385:00

they prototype something they may use a

## 56385:00 - 56415:00

proprietary API but when it comes time

## 56415:00 - 56445:00

to actually deploy the product they

## 56445:00 - 56485:00

actually use Llama Or open or other open

## 56485:00 - 56520:00

source engines because it's cheaper and

## 56520:00 - 56575:00

it's more uh secure you know it's more

## 56575:00 - 56605:00

controllable you can run it on premise

## 56605:00 - 56650:00

you know there's all kinds of advantages

## 56650:00 - 56730:00

so um we've seen also a big evolution in

## 56730:00 - 56765:00

the the thinking of some people who are

## 56765:00 - 56850:00

initially worried that U open source

## 56850:00 - 56905:00

efforts uh we're going to I don't know

## 56905:00 - 56930:00

for example you know help the Chinese or

## 56930:00 - 56950:00

something something if you have like

## 56950:00 - 56990:00

some geopolitical reason to think it's a

## 56990:00 - 57050:00

bad idea um but what deeps has shown is

## 57050:00 - 57075:00

that the Chinese don't need us I mean

## 57075:00 - 57105:00

they can come up with really good ideas

## 57105:00 - 57130:00

right I mean we all know that there are

## 57130:00 - 57155:00

really really good scientists in in

## 57155:00 - 57210:00

China and uh one thing that is not Wily

## 57210:00 - 57265:00

known is that the single most cited

## 57265:00 - 57305:00

paper in all of science is a paper on

## 57305:00 - 57340:00

deep learning from 10 years ago from

## 57340:00 - 57410:00

2015 and he came out of Beijing oh okay

## 57410:00 - 57450:00

it's uh the paper is called uh res net

## 57450:00 - 57470:00

so it's a particular type of

## 57470:00 - 57505:00

architecture of neural net where

## 57505:00 - 57535:00

basically by default every stage in a

## 57535:00 - 57575:00

deeping system confuses the identity

## 57575:00 - 57605:00

function it just copies its input on its

## 57605:00 - 57630:00

output and what the neural net does is

## 57630:00 - 57680:00

compute the deviation from this identity

## 57680:00 - 57730:00

okay so that allows to train extremely

## 57730:00 - 57785:00

deep neural net with you know dozens of

## 57785:00 - 57870:00

layers perhaps 100 layers and it was uh

## 57870:00 - 57890:00

the first author of that paper is

## 57890:00 - 57920:00

gentleman called scaming called cing her

## 57920:00 - 57955:00

at the time he was working at Microsoft

## 57955:00 - 58025:00

research Beijing MH um soon thereafter

## 58025:00 - 58055:00

the publication of that paper he joined

## 58055:00 - 58140:00

fair in California so I hired him um

## 58140:00 - 58180:00

and worked at Fair

## 58180:00 - 58255:00

for8 years or so and recently left and

## 58255:00 - 58325:00

is now a professor at MIT okay so uh

## 58325:00 - 58365:00

there are really really good scientists

## 58365:00 - 58395:00

everywhere around the world nobody has a

## 58395:00 - 58440:00

monopoly on good ideas certainly silicon

## 58440:00 - 58470:00

valy does not have a monopoly and good

## 58470:00 - 58520:00

ideas um or another example of that is

## 58520:00 - 58540:00

actually the first Lama came out of

## 58540:00 - 58585:00

Paris it came out of the fair lives in

## 58585:00 - 58650:00

Paris a small team of 12 people um

## 58650:00 - 58735:00

so um you have to take advantage of the

## 58735:00 - 58790:00

diversity of ideas

## 58790:00 - 58835:00

backgrounds uh creative juices of the

## 58835:00 - 58885:00

entire world if you want uh Science and

## 58885:00 - 58920:00

Technology to progress fast and that's

## 58920:00 - 58970:00

enabled by by open source Yan it is

## 58970:00 - 59000:00

always great to speak with you uh

## 59000:00 - 59030:00

appreciate this is our I think fourth or

## 59030:00 - 59070:00

fifth time speaking again Going Back 9

## 59070:00 - 59095:00

years ago you always helped me see

## 59095:00 - 59135:00

through all the hype and the buzz and

## 59135:00 - 59155:00

actually figure out what's happening and

## 59155:00 - 59180:00

I'm sure that's going to be the case for

## 59180:00 - 59215:00

our listeners and viewers as well so y

## 59215:00 - 59235:00

thank you so much for coming on hope we

## 59235:00 - 59270:00

do it again soon thank you all right

## 59270:00 - 59290:00

everybody thank you for watching we'll

## 59290:00 - 59315:00

be back on Friday to break down the

## 59315:00 - 59345:00

week's news until then we'll see you

## 59345:00+

next time on big technology podcast

