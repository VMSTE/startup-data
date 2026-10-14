---
source: https://www.youtube.com/watch?v=BsWxPI9UM4c
title: Why AI evals are the hottest new skill for product builders | Hamel
  Husain & Shreya Shankar
author: Lenny's Podcast
date: 2025-09-25
views: 103057
description: |-
  Hamel Husain and Shreya Shankar teach the world’s most popular course on AI evals and have trained over 2,000 PMs and engineers (including many teams at OpenAI and Anthropic). In this conversation, they demystify the process of developing effective evals, walk through real examples, and share practical techniques that’ll help you improve your AI product.

  *What you’ll learn:*
  1. WTF evals are
  2. Why they’ve become the most important new skill for AI product builders
  3. A step-by-step walkthrough of how to create an effective eval
  4. A deep dive into error analysis, open coding, and axial coding
  5. Code-based evals vs. LLM-as-judge
  6. The most common pitfalls and how to avoid them
  7. Practical tips for implementing evals with minimal time investment (30 minutes per week after initial setup)
  8. Insight into the debate between “vibes” and systematic evals

  *Brought to you by:*
  Fin—The #1 AI agent for customer service: https://fin.ai/lenny
  Dscout—The UX platform to capture insights at every stage: from ideation to production: https://www.dscout.com/
  Mercury—The art of simplified finances: https://mercury.com/

  *Transcript:* https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill

  *My biggest takeaways (for paid newsletter subscribers):* https://www.lennysnewsletter.com/i/173871171/my-biggest-takeaways-from-this-conversation

  *Where to find Shreya Shankar*
  • X: https://x.com/sh_reya
  • LinkedIn: https://www.linkedin.com/in/shrshnk/
  • Website: https://www.sh-reya.com/
  • Maven course: https://bit.ly/4myp27m

  *Where to find Hamel Husain*
  • X: https://x.com/HamelHusain
  • LinkedIn: https://www.linkedin.com/in/hamelhusain/
  • Website: https://hamel.dev/
  • Maven course: https://bit.ly/4myp27m

  *Where to find Lenny:*
  • Newsletter: https://www.lennysnewsletter.com
  • X: https://twitter.com/lennysan
  • LinkedIn: https://www.linkedin.com/in/lennyrachitsky/

  *In this episode, we cover:*
  (00:00) Introduction to Hamel and Shreya
  (04:57) What are evals?
  (09:56) Demo: Examining real traces from a property management AI assistant
  (16:51) Writing notes on errors
  (23:54) Why LLMs can’t replace humans in the initial error analysis
  (25:16) The concept of a “benevolent dictator” in the eval process
  (28:07) Theoretical saturation: when to stop
  (31:39) Using axial codes to help categorize and synthesize error notes
  (44:39) The results
  (46:06) Building an LLM-as-judge to evaluate specific failure modes
  (48:31) The difference between code-based evals and LLM-as-judge
  (52:10) Example: LLM-as-judge
  (54:45) Testing your LLM judge against human judgment
  (01:00:51) Why evals are the new PRDs for AI products
  (01:05:09) How many evals you actually need
  (01:07:41) What comes after evals
  (01:09:57) The great evals debate
  (1:15:15) Why dogfooding isn’t enough for most AI products
  (01:18:23) OpenAI’s Statsig acquisition
  (1:23:02) The Claude Code controversy and the importance of context
  (01:24:13) Common misconceptions around evals
  (1:22:28) Tips and tricks for implementing evals effectively
  (1:30:37) The time investment
  (1:33:38) Overview of their comprehensive evals course
  (1:37:57) Lightning round and final thoughts

  *LLM Log Open Codes Analysis Prompt:*
  _Please analyze the following CSV file. There is a metadata field which has an nested field called z_note that contains open codes for analysis of LLM logs that we are conducting. Please extract all of the different open codes. From the _note field, propose 5-6 categories that we can create axial codes from._

  *Referenced:*
  • Building eval systems that improve your AI product: https://www.lennysnewsletter.com/p/building-eval-systems-that-improve
  • Mercor: https://mercor.com/
  • Brendan Foody on LinkedIn: https://www.linkedin.com/in/brendan-foody-2995ab10b
  • Nurture Boss: https://nurtureboss.io/
  • Braintrust: https://www.braintrust.dev/
  • Andrew Ng on X: https://x.com/andrewyng
  • Carrying Out Error Analysis: https://www.youtube.com/watch?v=JoAxZsdw_3w
  • Julius AI: https://julius.ai/
  • Brendan Foody on X—“evals are the new PRDs”: https://x.com/BrendanFoody/status/1939764763485171948
  ...References continued at: https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill

  *Recommended books:*
  • Pachinko: https://www.amazon.com/Pachinko-National-Book-Award-Finalist/dp/1455563935
  • Apple in China: The Capture of the World’s Greatest Company: https://www.amazon.com/Apple-China-Capture-Greatest-Company/dp/1668053373/
  • Machine Learning: https://www.amazon.com/Machine-Learning-Tom-M-Mitchell/dp/1259096955
  • Artificial Intelligence: A Modern Approach: https://www.amazon.com/Artificial-Intelligence-Modern-Approach-Global/dp/1292401133/

  _Production and marketing by https://penname.co/._
  _For inquiries about sponsoring the podcast, email podcast@lennyrachitsky.com._

  Lenny may be an investor in the companies discussed.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:42:10.042Z
---

# Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar

## 00:00 - 25:00

To build great AI products, you need to

## 25:00 - 55:00

be really good at building evals. It's

## 55:00 - 85:00

the highest ROI activity you can engage

## 85:00 - 115:00

in. This process is a lot of fun.

## 115:00 - 155:00

Everyone that does this immediately gets

## 155:00 - 185:00

addicted to it when you're building an

## 185:00 - 210:00

AI application. You just learn a lot.

## 210:00 - 230:00

What's cool about this is you don't need

## 230:00 - 260:00

to do this many, many times. For most

## 260:00 - 290:00

products, you do this process once and

## 290:00 - 305:00

then you build on it.

## 305:00 - 345:00

>> The goal is not to do evals perfectly.

## 345:00 - 380:00

It's to actionably improve your product.

## 380:00 - 415:00

>> I did not realize how much controversy

## 415:00 - 445:00

and drama there is around eval. There's

## 445:00 - 460:00

a lot of people with very strong

## 460:00 - 490:00

opinions. People have been burned by

## 490:00 - 515:00

evals in the past. People have done

## 515:00 - 560:00

evals badly, then they didn't trust it

## 560:00 - 580:00

anymore and then they're like, "Oh, I'm

## 580:00 - 600:00

anti- evals."

## 600:00 - 620:00

>> What are a couple of the most common

## 620:00 - 650:00

misconceptions people have with EVEL?

## 650:00 - 695:00

The top one is we live in the age of AI.

## 695:00 - 735:00

Can't the AI just eval it? But it

## 735:00 - 770:00

doesn't work. A term that you used in

## 770:00 - 800:00

your post that I love is this idea of a

## 800:00 - 825:00

benevolent dictator. When you're doing

## 825:00 - 860:00

this open coding, a lot of teams get

## 860:00 - 900:00

bogged down in having a committee do

## 900:00 - 935:00

this. For a lot of situations, that's

## 935:00 - 965:00

wholly unnecessary. You don't want to

## 965:00 - 995:00

make this process so expensive that you

## 995:00 - 1030:00

can't do it. You can appoint one person

## 1030:00 - 1060:00

whose taste that you trust. It should be

## 1060:00 - 1095:00

the person with domain expertise.

## 1095:00 - 1160:00

Oftentimes it is the product manager.

## 1160:00 - 1200:00

Today my guests are Hamill Hussein and

## 1200:00 - 1240:00

Shrea Shankar. One of the most trending

## 1240:00 - 1270:00

topics on this podcast over the past

## 1270:00 - 1315:00

year has been the rise of evals. Both

## 1315:00 - 1355:00

the chief product officers of Anthropic

## 1355:00 - 1400:00

and OpenAI shared that eval are becoming

## 1400:00 - 1435:00

the most important new skill for product

## 1435:00 - 1475:00

builders. And since then, this has been

## 1475:00 - 1510:00

a recurring theme across many of the top

## 1510:00 - 1555:00

AI builders I've had on. 2 years ago, I

## 1555:00 - 1580:00

had never heard the term evals. Now,

## 1580:00 - 1610:00

it's coming up constantly. When was the

## 1610:00 - 1640:00

last time that a new skill emerged that

## 1640:00 - 1670:00

product builders had to get good at to

## 1670:00 - 1710:00

be successful? Hamill and Shrea have

## 1710:00 - 1740:00

played a major role in shifting evals

## 1740:00 - 1775:00

from being an obscure mysterious subject

## 1775:00 - 1815:00

to one of the most necessary skills for

## 1815:00 - 1855:00

AI product builders. They teach the

## 1855:00 - 1895:00

definitive online course on evals, which

## 1895:00 - 1925:00

happens to be the number one course on

## 1925:00 - 1975:00

Maven. They've now taught over 2,000 PMs

## 1975:00 - 2015:00

and engineers across 500 companies,

## 2015:00 - 2065:00

including large swats of the open AI and

## 2065:00 - 2100:00

anthropic teams along with every other

## 2100:00 - 2145:00

major AI lab. In this conversation, we

## 2145:00 - 2190:00

do a lot of show versus tell. We walk

## 2190:00 - 2220:00

through the process of developing an

## 2220:00 - 2255:00

effective eval, explain what the heck

## 2255:00 - 2290:00

evals are and what they look like,

## 2290:00 - 2325:00

address many of the major misconceptions

## 2325:00 - 2355:00

with eval, give you the first few steps

## 2355:00 - 2385:00

you can take to start building evals for

## 2385:00 - 2420:00

your product, and also share just a ton

## 2420:00 - 2445:00

of best practices that Hamill and Trey

## 2445:00 - 2480:00

have developed over the past few years.

## 2480:00 - 2525:00

This episode is the deepest yet most

## 2525:00 - 2560:00

understandable primer you will find on

## 2560:00 - 2600:00

the world of evals and honestly got me

## 2600:00 - 2625:00

excited to write evals. Even though I

## 2625:00 - 2660:00

have nothing to write eels for, I think

## 2660:00 - 2685:00

you'll feel the same way as you watch

## 2685:00 - 2710:00

this. If this conversation gets you

## 2710:00 - 2735:00

excited, definitely check out Hamill and

## 2735:00 - 2765:00

Shreas's course on Maven. We'll link to

## 2765:00 - 2790:00

it in the show notes. If you use the

## 2790:00 - 2825:00

code Lenny's List when you purchase the

## 2825:00 - 2870:00

course, you'll get 35% off the price of

## 2870:00 - 2905:00

the course. With that, I bring you

## 2905:00 - 2970:00

Hamill Hussein and Shrea Shankar. This

## 2970:00 - 3000:00

episode is brought to you by Finn, the

## 3000:00 - 3035:00

number one AI agent for customer

## 3035:00 - 3060:00

service. If your customer support

## 3060:00 - 3090:00

tickets are piling up, then you need

## 3090:00 - 3130:00

Finn. Finn is the highest performing AI

## 3130:00 - 3180:00

agent on the market with a 65% average

## 3180:00 - 3215:00

resolution rate. Finn resolves even the

## 3215:00 - 3255:00

most complex customer queries. No other

## 3255:00 - 3285:00

AI agent performs better. In

## 3285:00 - 3310:00

head-to-head bake offs with competitors,

## 3310:00 - 3365:00

Finn wins every time. Yes, switching to

## 3365:00 - 3400:00

a new tool can be scary, but Finn works

## 3400:00 - 3430:00

on any help desk with no migration

## 3430:00 - 3455:00

needed, which means you don't have to

## 3455:00 - 3485:00

overhaul your current system or deal

## 3485:00 - 3510:00

with delays in service for your

## 3510:00 - 3545:00

customers. And Finn is trusted by over

## 3545:00 - 3585:00

5,000 customer service leaders and top

## 3585:00 - 3615:00

AI companies like Anthropic and

## 3615:00 - 3650:00

Synthesia. And because Finn is powered

## 3650:00 - 3685:00

by the Finn AI engine, which is a

## 3685:00 - 3710:00

continuously improving system that

## 3710:00 - 3740:00

allows you to analyze, train, test, and

## 3740:00 - 3780:00

deploy with ease. Finn can continuously

## 3780:00 - 3810:00

improve your results, too. So, if you're

## 3810:00 - 3840:00

ready to transform your customer service

## 3840:00 - 3875:00

and scale your support, give Finn a try

## 3875:00 - 3920:00

for only 99 cents per resolution. Plus,

## 3920:00 - 3950:00

Finn comes with a 90-day money back

## 3950:00 - 3980:00

guarantee. Find out how Finn can work

## 3980:00 - 4040:00

for your team at f.ai. ai/lenny. That's

## 4040:00 - 4090:00

finn.ai/lenny.

## 4090:00 - 4140:00

This episode is brought to you by Doutt.

## 4140:00 - 4175:00

Design teams today are expected to move

## 4175:00 - 4215:00

fast, but also to get it right. That's

## 4215:00 - 4255:00

where Dout comes in. Dcout is the

## 4255:00 - 4285:00

all-in-one research platform built for

## 4285:00 - 4325:00

modern product and design teams. Whether

## 4325:00 - 4350:00

you're running usability tests,

## 4350:00 - 4380:00

interviews, surveys, or in the wild

## 4380:00 - 4415:00

fieldwork, Dout makes it easy to connect

## 4415:00 - 4455:00

with real users and get real insights

## 4455:00 - 4495:00

fast. You can even test your Figma

## 4495:00 - 4540:00

prototypes directly inside the platform.

## 4540:00 - 4580:00

No juggling tools, no chasing ghost

## 4580:00 - 4610:00

participants. And with the industry's

## 4610:00 - 4655:00

most trusted panel, plus AI powered

## 4655:00 - 4695:00

analysis, your team gets clarity and

## 4695:00 - 4725:00

confidence to build better without

## 4725:00 - 4755:00

slowing down. So if you're ready to

## 4755:00 - 4780:00

streamline your research, speed of

## 4780:00 - 4810:00

decisions, and design with impact, head

## 4810:00 - 4860:00

to dscout.com to learn more. That's

## 4860:00 - 4905:00

dscout.com.

## 4905:00 - 4930:00

The answers you need to move

## 4930:00 - 5010:00

confidently.

## 5010:00 - 5045:00

Hammel and Shrea, thank you so much for

## 5045:00 - 5075:00

being here and welcome to the podcast.

## 5075:00 - 5090:00

Thank you for having us.

## 5090:00 - 5115:00

>> Yeah, super excited.

## 5115:00 - 5165:00

>> I'm even more excited. Okay, so a couple

## 5165:00 - 5205:00

years ago, I had never heard the term

## 5205:00 - 5255:00

evals. Now it's one of the most trending

## 5255:00 - 5300:00

topics on my podcast essentially that to

## 5300:00 - 5325:00

build great AI products, you need to be

## 5325:00 - 5375:00

really good at building evals. Uh, also

## 5375:00 - 5395:00

turns out some of the fastest growing

## 5395:00 - 5430:00

companies in the world are basically

## 5430:00 - 5470:00

building and selling and creating evals

## 5470:00 - 5505:00

for AI labs. I just had the CF Merkore

## 5505:00 - 5535:00

on the podcast. So, there's something

## 5535:00 - 5585:00

really big happening here. Uh, I want to

## 5585:00 - 5610:00

use this conversation to basically help

## 5610:00 - 5665:00

people understand the space deeply. But

## 5665:00 - 5690:00

let's start with the basics. Just what

## 5690:00 - 5720:00

what the heck are EVALs? For folks that

## 5720:00 - 5745:00

have no idea what we're talking about,

## 5745:00 - 5765:00

give us just a quick understanding of

## 5765:00 - 5800:00

what an eval is. And let's start with

## 5800:00 - 5855:00

with Haml. Sure. Evals is a way to

## 5855:00 - 5900:00

systematically measure and improve an AI

## 5900:00 - 5945:00

application. And it really doesn't have

## 5945:00 - 6005:00

to be scary or unapproachable at all. It

## 6005:00 - 6080:00

really is at its core data analytics on

## 6080:00 - 6140:00

your LLM application in a systematic way

## 6140:00 - 6215:00

of looking at that data and where

## 6215:00 - 6260:00

necessary creating metrics around things

## 6260:00 - 6295:00

so you can measure what's happening and

## 6295:00 - 6335:00

then so you can iterate and do

## 6335:00 - 6375:00

experiments and improve. So that's a

## 6375:00 - 6395:00

that's a really good broad way of

## 6395:00 - 6420:00

thinking about it. If you go one level

## 6420:00 - 6445:00

deeper just to give people a very even

## 6445:00 - 6480:00

more concrete way of imagining and

## 6480:00 - 6500:00

visualizing what we're talking about

## 6500:00 - 6525:00

even if you have a example to show it

## 6525:00 - 6570:00

would be even better. What's a what's an

## 6570:00 - 6590:00

even deeper way of understanding what an

## 6590:00 - 6630:00

eval is? Let's say you have a real

## 6630:00 - 6675:00

estate assistant

## 6675:00 - 6735:00

you know application and it's it's not

## 6735:00 - 6750:00

working the way you want. it's not

## 6750:00 - 6785:00

writing emails to customers the way you

## 6785:00 - 6860:00

want or it's not uh you know calling the

## 6860:00 - 6895:00

right tools

## 6895:00 - 6960:00

or any number of errors and

## 6960:00 - 7000:00

before evals you would be left with

## 7000:00 - 7065:00

guessing you would maybe fix a prompt

## 7065:00 - 7095:00

and hope that you're not breaking

## 7095:00 - 7150:00

anything else with that prompt and you

## 7150:00 - 7180:00

might rely on vibe checks which is

## 7180:00 - 7215:00

totally fine and vibe checks are good

## 7215:00 - 7250:00

and you should do vibe checks

## 7250:00 - 7290:00

initially, but it can become very

## 7290:00 - 7350:00

unmanageable very fast because as your

## 7350:00 - 7395:00

application grows, it's really hard to

## 7395:00 - 7440:00

rely on vibe checks. You just feel lost.

## 7440:00 - 7505:00

And so eval help you create

## 7505:00 - 7565:00

metrics that you can use to measure how

## 7565:00 - 7610:00

your application is doing and kind of

## 7610:00 - 7655:00

give you a way to improve your your

## 7655:00 - 7690:00

application with confidence that you

## 7690:00 - 7720:00

have a feedback signal in which to

## 7720:00 - 7770:00

iterate against. So just to make it very

## 7770:00 - 7800:00

real. So imagining this uh real estate

## 7800:00 - 7830:00

agent maybe they're helping you book a

## 7830:00 - 7880:00

listing or go see an open house. The

## 7880:00 - 7900:00

idea here is you have this agent talking

## 7900:00 - 7925:00

to people. It's answering questions,

## 7925:00 - 7960:00

pointing them to things. As a builder of

## 7960:00 - 7985:00

that agent, how do you know if it's

## 7985:00 - 8015:00

giving them good advice, good answers?

## 8015:00 - 8050:00

Is it telling them things that are

## 8050:00 - 8085:00

completely wrong? So, the idea of eval

## 8085:00 - 8115:00

essentially is to build a set of tests

## 8115:00 - 8170:00

that tell you is how often are is this

## 8170:00 - 8195:00

agent doing something wrong that you

## 8195:00 - 8210:00

don't want it to do? And there's a bunch

## 8210:00 - 8240:00

of ways wrong you could define wrong. It

## 8240:00 - 8280:00

could be uh just making up stuff. It

## 8280:00 - 8320:00

could be uh just answering in a really

## 8320:00 - 8360:00

strange way. Uh the way I think about

## 8360:00 - 8390:00

eval and tell me if this is wrong just

## 8390:00 - 8445:00

simply is like unit tests for for code

## 8445:00 - 8480:00

and then you're smiling. You're like no

## 8480:00 - 8495:00

you idiot.

## 8495:00 - 8525:00

>> Oh that's not what I was thinking.

## 8525:00 - 8555:00

>> Okay. Okay. Tell me tell me how does

## 8555:00 - 8585:00

that feel as a metaphor?

## 8585:00 - 8630:00

>> So okay I like what you said first which

## 8630:00 - 8680:00

is we had a very broad definition. Evals

## 8680:00 - 8720:00

is a big spectrum of ways to measure

## 8720:00 - 8760:00

application quality. Now unit tests are

## 8760:00 - 8800:00

one way of doing this. Maybe there are

## 8800:00 - 8840:00

some non-negotiable functionalities that

## 8840:00 - 8890:00

you want your AI assistant to have and

## 8890:00 - 8925:00

unit tests are going to be able to check

## 8925:00 - 8975:00

that. Now maybe you also because these

## 8975:00 - 9020:00

AI assistants are doing such open-ended

## 9020:00 - 9060:00

tasks, you kind of also want to measure

## 9060:00 - 9095:00

how good are they at very vague or

## 9095:00 - 9130:00

ambiguous things like responding to new

## 9130:00 - 9170:00

types of user requests or you know

## 9170:00 - 9190:00

figuring out if there's new

## 9190:00 - 9230:00

distributions of data like new users are

## 9230:00 - 9265:00

coming and using your real estate agent

## 9265:00 - 9305:00

that you didn't even know would use your

## 9305:00 - 9330:00

product and then all of a sudden you

## 9330:00 - 9360:00

think like oh there's a different way

## 9360:00 - 9390:00

you want to kind of accommodate this new

## 9390:00 - 9435:00

group of people. So eval could also be

## 9435:00 - 9475:00

you know a way of looking at your data

## 9475:00 - 9510:00

regularly to find these new cohorts of

## 9510:00 - 9565:00

people. Evals could also be like metrics

## 9565:00 - 9600:00

that you know you just want to track

## 9600:00 - 9655:00

over time like you want to track people

## 9655:00 - 9690:00

saying yes thumbs up I liked your

## 9690:00 - 9735:00

message. Um you want to very very basic

## 9735:00 - 9760:00

things that are not necessarily AI

## 9760:00 - 9795:00

related but can go back into this

## 9795:00 - 9830:00

flywheel of improving your product. So I

## 9830:00 - 9870:00

would say on the end on overall right

## 9870:00 - 9910:00

unit tests are a very small part of that

## 9910:00 - 9940:00

very big puzzle.

## 9940:00 - 9970:00

>> Awesome. You guys actually brought an

## 9970:00 - 10010:00

example of inval just to show us exactly

## 10010:00 - 10030:00

what the hell we're talking about. We're

## 10030:00 - 10060:00

talking in these big ideas. So how about

## 10060:00 - 10090:00

let's pull one up and show people here's

## 10090:00 - 10110:00

here's what an eval is.

## 10110:00 - 10145:00

>> Yeah. Let me just set the stage for it a

## 10145:00 - 10205:00

little bit. So to echo what Shrea said,

## 10205:00 - 10245:00

it's really important that we don't

## 10245:00 - 10295:00

think of evals as just tests. It's a

## 10295:00 - 10320:00

common trap that a lot of people fall

## 10320:00 - 10360:00

into because they jump straight to the

## 10360:00 - 10400:00

test like let me write some tests and

## 10400:00 - 10430:00

usually that's not what you want to do.

## 10430:00 - 10460:00

You should start with some kind of data

## 10460:00 - 10515:00

analysis to ground what you should even

## 10515:00 - 10545:00

test. And that's a little bit different

## 10545:00 - 10590:00

than software engineering where you have

## 10590:00 - 10625:00

a lot more

## 10625:00 - 10670:00

expectations of how the system is going

## 10670:00 - 10710:00

to work. With LLMs, it's a lot more

## 10710:00 - 10755:00

surface area. It's very stochastic. So,

## 10755:00 - 10790:00

we kind of have a different flavor here.

## 10790:00 - 10820:00

And so, the example I'm going to show

## 10820:00 - 10870:00

you today, it's actually a real estate

## 10870:00 - 10895:00

example. It's a different kind of real

## 10895:00 - 10925:00

estate example. It's uh from a company

## 10925:00 - 10965:00

called Nurture Boss. I can share my

## 10965:00 - 11015:00

screen to show you their website just to

## 11015:00 - 11060:00

help you understand this uh use case a

## 11060:00 - 11095:00

little bit. So, let me share my screen.

## 11095:00 - 11120:00

So, this is a company that I worked

## 11120:00 - 11160:00

with. It's called Nurture Boss and it is

## 11160:00 - 11210:00

a AI assistant for property managers who

## 11210:00 - 11250:00

are managing apartments. And it helps

## 11250:00 - 11300:00

with various tasks such as inbound

## 11300:00 - 11350:00

leads, customer service, booking

## 11350:00 - 11395:00

appointments, so on and so forth, like

## 11395:00 - 11430:00

all the different sort of operations you

## 11430:00 - 11480:00

might be doing as a property manager. It

## 11480:00 - 11525:00

helps you with that. And so, you know,

## 11525:00 - 11570:00

you can see kind of what they do. It's a

## 11570:00 - 11615:00

very good example because it has a lot

## 11615:00 - 11655:00

of the complexities of a modern AI

## 11655:00 - 11705:00

application. So there's lots of

## 11705:00 - 11740:00

different channels that you can interact

## 11740:00 - 11790:00

through the AI with like chat,

## 11790:00 - 11835:00

text, voice, but also there's tool

## 11835:00 - 11880:00

calls, lots of tool calls for like

## 11880:00 - 11925:00

booking appointments, getting uh

## 11925:00 - 11955:00

information about availability, so on

## 11955:00 - 11995:00

and so forth. There's also rag

## 11995:00 - 12020:00

retrieval,

## 12020:00 - 12055:00

getting information about customers and

## 12055:00 - 12100:00

properties and things like that. So it's

## 12100:00 - 12155:00

pretty fullyfledged in terms of an AI

## 12155:00 - 12180:00

application

## 12180:00 - 12210:00

and so

## 12210:00 - 12245:00

they have been really generous with me

## 12245:00 - 12300:00

and uh allowing me to use their data as

## 12300:00 - 12345:00

a teaching example and so we have

## 12345:00 - 12400:00

anonymized it but what I'm going to walk

## 12400:00 - 12460:00

through today is okay let's create let's

## 12460:00 - 12525:00

do the first part of how we would start

## 12525:00 - 12575:00

to build evals for nurture boss like why

## 12575:00 - 12615:00

Would we even want to do that? So let's

## 12615:00 - 12660:00

go through the very beginning stage what

## 12660:00 - 12700:00

we call error analysis

## 12700:00 - 12755:00

which is let's look at the data of their

## 12755:00 - 12785:00

application

## 12785:00 - 12850:00

and first start with what's going wrong.

## 12850:00 - 12895:00

So I'm going to jump to that next and

## 12895:00 - 12960:00

I'm going to open an observability tool

## 12960:00 - 13000:00

and you can use whatever you want here.

## 13000:00 - 13045:00

I just happen to have this data loaded

## 13045:00 - 13120:00

in a tool called brain trust but you can

## 13120:00 - 13165:00

load it in anything you know it's not we

## 13165:00 - 13195:00

don't have a favorite tool or anything

## 13195:00 - 13235:00

in the blog post that we wrote with you

## 13235:00 - 13265:00

uh we

## 13265:00 - 13310:00

had the same example but in Phoenix

## 13310:00 - 13355:00

Arise um and I think Aman on your blog

## 13355:00 - 13395:00

post use Phoenix Arise as well and

## 13395:00 - 13435:00

there's also Langmith so these are kind

## 13435:00 - 13480:00

of like different tools that you can use

## 13480:00 - 13545:00

so what you see here on the screen. This

## 13545:00 - 13635:00

is logs from the application

## 13635:00 - 13665:00

and

## 13665:00 - 13705:00

let me just show you how it looks. So

## 13705:00 - 13750:00

what you see here is and let me make it

## 13750:00 - 13795:00

full screen. So this is one particular

## 13795:00 - 13835:00

interaction that a customer had with the

## 13835:00 - 13890:00

nurture boss application.

## 13890:00 - 13940:00

And what it is, it's a detailed log of

## 13940:00 - 13970:00

everything that happened. So it's it's a

## 13970:00 - 14015:00

it's called a trace and it's just an

## 14015:00 - 14060:00

engineering term for logs of a sequence

## 14060:00 - 14100:00

of events. It's been a the concept of a

## 14100:00 - 14125:00

trace has been around for a really long

## 14125:00 - 14155:00

time but it's especially really

## 14155:00 - 14175:00

important when it comes to AI

## 14175:00 - 14210:00

applications. So we have all the

## 14210:00 - 14245:00

different components and pieces and

## 14245:00 - 14295:00

information that the AI needs to do its

## 14295:00 - 14340:00

job and we are logged all of it and

## 14340:00 - 14385:00

we're looking at a view of that and so

## 14385:00 - 14430:00

you see here a system prompt. The

## 14430:00 - 14460:00

assistant prompt says you are an AI

## 14460:00 - 14490:00

assistant working as a leasing team

## 14490:00 - 14560:00

member at retreat at Acme Apartments.

## 14560:00 - 14595:00

Remember I said this is anonymized. So

## 14595:00 - 14640:00

that's why the name is Acme Apartments.

## 14640:00 - 14670:00

Your primary role is to respond to text

## 14670:00 - 14700:00

messages from both residents and

## 14700:00 - 14740:00

perspective uh both current residents

## 14740:00 - 14770:00

and prospective residents. Your goal is

## 14770:00 - 14800:00

to provide accurate helpful information

## 14800:00 - 14850:00

yada yada yada. And then there's a lot

## 14850:00 - 14900:00

of detail around guidelines of how we

## 14900:00 - 14940:00

want this thing to behave.

## 14940:00 - 14965:00

>> Is this their actual system prompt by

## 14965:00 - 14975:00

the way for this company?

## 14975:00 - 15015:00

>> It is. Yes. It's a real system prompt.

## 15015:00 - 15035:00

>> That's amazing because that's really

## 15035:00 - 15060:00

it's rare you see actual company

## 15060:00 - 15080:00

products system prompt. That's like

## 15080:00 - 15105:00

their crown jewels a lot of times. So

## 15105:00 - 15135:00

this is actually very cool on its own.

## 15135:00 - 15185:00

>> Yeah. Yeah. It's really cool. And you

## 15185:00 - 15225:00

know you see all these different sort of

## 15225:00 - 15270:00

features that they want to

## 15270:00 - 15310:00

or different use cases. So things about

## 15310:00 - 15365:00

tour scheduling, handling applications,

## 15365:00 - 15410:00

guidance on how to talk to different

## 15410:00 - 15455:00

personas, so on and so forth. And you

## 15455:00 - 15495:00

can see the user just kind of jumps in

## 15495:00 - 15550:00

here. It says asks, okay, do you have a

## 15550:00 - 15580:00

one-bedroom with study available? I saw

## 15580:00 - 15625:00

it on virtual tours. And then you can

## 15625:00 - 15680:00

see that the LM

## 15680:00 - 15725:00

calls some tools. It calls this get

## 15725:00 - 15780:00

individual's information tool and it

## 15780:00 - 15845:00

pulls back that person's information and

## 15845:00 - 15880:00

then it gets the community's

## 15880:00 - 15905:00

availability.

## 15905:00 - 15955:00

So it's, you know, it's querying a

## 15955:00 - 15995:00

database with the availability for that

## 15995:00 - 16050:00

apartment complex. And then finally, the

## 16050:00 - 16090:00

AI responds, hey, we we have several

## 16090:00 - 16125:00

one-bedroom apartments available, but

## 16125:00 - 16160:00

none specifically listed with a study.

## 16160:00 - 16200:00

Here are a few options.

## 16200:00 - 16220:00

Uh, and then it says, "Can you let me

## 16220:00 - 16250:00

know when one with a study is

## 16250:00 - 16275:00

available?"

## 16275:00 - 16300:00

And then it says, "I currently don't

## 16300:00 - 16335:00

have specific information on the

## 16335:00 - 16360:00

availability of a one-bedroom

## 16360:00 - 16390:00

apartment."

## 16390:00 - 16435:00

User says, "Thank you." And the AI says,

## 16435:00 - 16465:00

"You're welcome. If you have any more

## 16465:00 - 16530:00

questions, feel free to reach out." Now,

## 16530:00 - 16560:00

this is

## 16560:00 - 16625:00

an example of a trace, and this is we're

## 16625:00 - 16700:00

looking at one specific data point.

## 16700:00 - 16725:00

And so one thing that's really important

## 16725:00 - 16800:00

to do when you're doing data analysis of

## 16800:00 - 16855:00

your LLM application is to look at data.

## 16855:00 - 16895:00

Now you might wonder there's a lot of

## 16895:00 - 16930:00

these logs.

## 16930:00 - 16965:00

It's kind of messy. There's a lot of

## 16965:00 - 17000:00

things going on here. How in the hell

## 17000:00 - 17045:00

are you supposed to look at this data?

## 17045:00 - 17085:00

Do you want to just drown in this data?

## 17085:00 - 17130:00

How do you even analyze this data? So it

## 17130:00 - 17165:00

turns out there is a way to do it that

## 17165:00 - 17205:00

is completely manageable

## 17205:00 - 17245:00

and it's not something that we invented.

## 17245:00 - 17280:00

It's been around in machine learning and

## 17280:00 - 17315:00

data science for a really long time and

## 17315:00 - 17355:00

it's called error analysis. And what you

## 17355:00 - 17430:00

do is the first step in conquering data

## 17430:00 - 17490:00

like this is just to write notes. Okay?

## 17490:00 - 17540:00

So, you got to put your product hat on,

## 17540:00 - 17560:00

which is why we're talking to you

## 17560:00 - 17615:00

because product people have to be in the

## 17615:00 - 17655:00

room. Um, and they have to be involved

## 17655:00 - 17705:00

in sort of doing this. You know, usually

## 17705:00 - 17750:00

a developer is not suited to do this,

## 17750:00 - 17765:00

especially if it's not a coding

## 17765:00 - 17775:00

application.

## 17775:00 - 17810:00

>> And I'm just to mirror back why I think

## 17810:00 - 17835:00

you're saying that is because this is

## 17835:00 - 17865:00

the user experience of your product.

## 17865:00 - 17890:00

People talking to this agent is the

## 17890:00 - 17925:00

entire product essentially. And so it

## 17925:00 - 17955:00

makes sense for the product person to be

## 17955:00 - 17995:00

involved, super involved in this. Yeah.

## 17995:00 - 18025:00

So let's let's reflect on this

## 18025:00 - 18060:00

conversation.

## 18060:00 - 18140:00

Okay. A user asked about availability.

## 18140:00 - 18185:00

The AI said, "Oh, we don't really have

## 18185:00 - 18240:00

that. Have a nice day."

## 18240:00 - 18280:00

Now, for a product that is helping you

## 18280:00 - 18310:00

with

## 18310:00 - 18390:00

lead management,

## 18390:00 - 18440:00

is that good? Like, do you feel

## 18440:00 - 18500:00

like this is the way we want it to to

## 18500:00 - 18505:00

go?

## 18505:00 - 18535:00

>> Not ideal.

## 18535:00 - 18565:00

Yes. Not ideal. And I'm glad you said

## 18565:00 - 18605:00

that. A lot of people would say, "Oh,

## 18605:00 - 18640:00

it's great. Like the AI did the right

## 18640:00 - 18675:00

thing. It said we don't it looked it

## 18675:00 - 18700:00

said we didn't have available and it's

## 18700:00 - 18725:00

not available." But with your product

## 18725:00 - 18770:00

hat on, you know, that's not correct.

## 18770:00 - 18810:00

And so what you would do is you would

## 18810:00 - 18840:00

just write a quick note here. You would

## 18840:00 - 18905:00

say okay um you know you might pop in

## 18905:00 - 18950:00

here let me just and you can write a

## 18950:00 - 18995:00

note so every observability application

## 18995:00 - 19040:00

has ability to write notes and you

## 19040:00 - 19075:00

wouldn't try to figure out if something

## 19075:00 - 19105:00

is wrong in this applica you know in

## 19105:00 - 19140:00

this case it's kind of not doing the

## 19140:00 - 19180:00

right thing. Um but you just write a

## 19180:00 - 19225:00

quick note um should you know should

## 19225:00 - 19315:00

have handed off to a human

## 19315:00 - 19350:00

>> and as we watch this happening it's like

## 19350:00 - 19370:00

you mentioned this and you'll explain

## 19370:00 - 19400:00

more you're doing this this feels very

## 19400:00 - 19445:00

ma manual and unscalable but uh as you

## 19445:00 - 19470:00

said this is just one step of the

## 19470:00 - 19500:00

process and there's a system to this and

## 19500:00 - 19520:00

it's just the first part

## 19520:00 - 19545:00

>> and you don't have to do it for all of

## 19545:00 - 19595:00

your data you can you sample your data

## 19595:00 - 19650:00

and just take a look and it's surprising

## 19650:00 - 19690:00

amazing how much you learn when you do

## 19690:00 - 19725:00

this. Everyone that does this

## 19725:00 - 19765:00

immediately gets addicted to it and they

## 19765:00 - 19800:00

say, "This is the greatest thing that

## 19800:00 - 19840:00

you can do when you're building an AI

## 19840:00 - 19860:00

application." You just learn a lot.

## 19860:00 - 19895:00

You're like, "Hm, this is not how I want

## 19895:00 - 19955:00

it to to work." Okay. And so, um, that's

## 19955:00 - 20005:00

just an example. So, you write this note

## 20005:00 - 20040:00

and then we can go on to the next trace.

## 20040:00 - 20065:00

So, this is the next trace. I just

## 20065:00 - 20105:00

pushed a hot key on my keyboard. Let me

## 20105:00 - 20155:00

go back to uh looking at it.

## 20155:00 - 20175:00

>> And these tools make it easy to go

## 20175:00 - 20200:00

through a bunch and add these notes

## 20200:00 - 20220:00

quickly.

## 20220:00 - 20280:00

>> Yes. And so this is another one. Similar

## 20280:00 - 20305:00

system prompt. We don't need to go

## 20305:00 - 20330:00

through all of it. Again, we'll just

## 20330:00 - 20370:00

jump right into the user question. Okay.

## 20370:00 - 20410:00

I've been texting you all day. Maybe

## 20410:00 - 20475:00

it's is funny. Um

## 20475:00 - 20520:00

um

## 20520:00 - 20545:00

and

## 20545:00 - 20610:00

uh the user says please okay yeah this

## 20610:00 - 20660:00

one is you this one is just like an

## 20660:00 - 20720:00

error in the application where you know

## 20720:00 - 20775:00

um this is a text message application

## 20775:00 - 20805:00

and so

## 20805:00 - 20840:00

you know it's a tech the sorry the

## 20840:00 - 20870:00

channel through which the customer is

## 20870:00 - 20895:00

communicating is through text message

## 20895:00 - 20915:00

and it's just getting like really

## 20915:00 - 20960:00

garbled And you can see here that it

## 20960:00 - 21000:00

kind of doesn't make sense,

## 21000:00 - 21025:00

you know, like the words are being cut

## 21025:00 - 21065:00

off like in the meantime

## 21065:00 - 21100:00

and then the system doesn't know how to

## 21100:00 - 21125:00

respond because you know how people text

## 21125:00 - 21160:00

message, they like write short phrases,

## 21160:00 - 21200:00

they you know split split their sentence

## 21200:00 - 21245:00

across four or five different turns. So

## 21245:00 - 21255:00

in this case

## 21255:00 - 21275:00

>> you do with something like that.

## 21275:00 - 21310:00

>> Yeah. So this is a this is a different

## 21310:00 - 21330:00

kind of error.

## 21330:00 - 21370:00

>> This is more of hey we're not handling

## 21370:00 - 21400:00

this interaction correctly. This is more

## 21400:00 - 21435:00

of a technical problem.

## 21435:00 - 21475:00

um rather than hey the AI is not doing

## 21475:00 - 21510:00

exactly what we want. So we would write

## 21510:00 - 21530:00

down too like it's amazing you're

## 21530:00 - 21555:00

catching that too here otherwise you'd

## 21555:00 - 21585:00

have no idea this was happening.

## 21585:00 - 21605:00

>> Yeah you might not know this is

## 21605:00 - 21645:00

happening right and so you would just

## 21645:00 - 21695:00

say okay um you would write a note like

## 21695:00 - 21725:00

oh

## 21725:00 - 21785:00

conversation flow

## 21785:00 - 21825:00

is janky

## 21825:00 - 21860:00

because of text message and I like yeah

## 21860:00 - 21885:00

I like that I like that you're using the

## 21885:00 - 21910:00

word janky. shows you just how informal

## 21910:00 - 21945:00

this can be at this stage. Yeah, it's

## 21945:00 - 21975:00

supposed to be chill like just don't

## 21975:00 - 22025:00

overthink it. And there's some there's a

## 22025:00 - 22070:00

way to do this. So

## 22070:00 - 22115:00

the question always comes up, how do you

## 22115:00 - 22145:00

do this? Do you look at do you try to

## 22145:00 - 22175:00

find all the different problems in this

## 22175:00 - 22215:00

trace? What what do you write a note

## 22215:00 - 22290:00

about? And the answer is just write down

## 22290:00 - 22310:00

the first thing that you see that's

## 22310:00 - 22345:00

wrong, the most upstream error. Don't

## 22345:00 - 22390:00

worry about all the errors. just capture

## 22390:00 - 22415:00

the most the first thing that you see

## 22415:00 - 22465:00

that's wrong and stop and move on.

## 22465:00 - 22505:00

And you can get really good at this. The

## 22505:00 - 22545:00

first two or three can be very painful,

## 22545:00 - 22600:00

but you know, it doesn't we can, you

## 22600:00 - 22640:00

know, do a bunch of them really fast.

## 22640:00 - 22700:00

So, here's another one. And um let's

## 22700:00 - 22740:00

skip the system prompt again. And the

## 22740:00 - 22775:00

user asks, "Hey, I'm looking for a two

## 22775:00 - 22810:00

to threebedroom with either one or two

## 22810:00 - 22865:00

bats. Do you provide virtual tours?

## 22865:00 - 22930:00

and a bunch of tools are called

## 22930:00 - 22965:00

and it says, "Hi Sarah, currently we

## 22965:00 - 22990:00

have three bedroomedroom, two and a half

## 22990:00 - 23065:00

bathroom apartment available for $2,175.

## 23065:00 - 23085:00

Um, unfortunately we don't have any

## 23085:00 - 23115:00

two-bedroom options at the moment. We do

## 23115:00 - 23145:00

offer virtual tool tours. You can

## 23145:00 - 23185:00

schedule a tour blah blah blah. It just

## 23185:00 - 23220:00

so happens that there is no virtual

## 23220:00 - 23265:00

tour,

## 23265:00 - 23310:00

>> right? So um you know it is

## 23310:00 - 23345:00

hallucinating something that doesn't

## 23345:00 - 23375:00

exist and you would you kind of have to

## 23375:00 - 23415:00

bring your context as an engineer or

## 23415:00 - 23445:00

even your product content and say hey

## 23445:00 - 23485:00

this is kind of weird like you know we

## 23485:00 - 23520:00

shouldn't be telling person about

## 23520:00 - 23545:00

virtual tour when it's not offered. So

## 23545:00 - 23600:00

you would say okay uh you know offered

## 23600:00 - 23655:00

virtual tour

## 23655:00 - 23700:00

and you just you know you just write the

## 23700:00 - 23725:00

note.

## 23725:00 - 23750:00

So you can see there's a diversity of

## 23750:00 - 23775:00

different kinds of errors that we're

## 23775:00 - 23830:00

seeing and we're actually learning a lot

## 23830:00 - 23870:00

about your application

## 23870:00 - 23915:00

um in a very short amount of time.

## 23915:00 - 23945:00

>> One common question that we get from

## 23945:00 - 23980:00

people at this stage is okay I

## 23980:00 - 24020:00

understand what's going on. Can I ask an

## 24020:00 - 24065:00

LLM to do this process for me?

## 24065:00 - 24105:00

>> Great question. And I loved Hammel's

## 24105:00 - 24160:00

most recent example because what we

## 24160:00 - 24190:00

usually find when we try to ask an LLM

## 24190:00 - 24225:00

to do this error analysis is it just

## 24225:00 - 24260:00

says the trace looks good because it

## 24260:00 - 24295:00

doesn't have the context needed to

## 24295:00 - 24330:00

understand whether something might be

## 24330:00 - 24385:00

you know bad product smell or you know

## 24385:00 - 24430:00

not for example the hallucination about

## 24430:00 - 24465:00

scheduling the tour right I can

## 24465:00 - 24495:00

guarantee you I would bet money on this

## 24495:00 - 24535:00

if I put that into chat GBT and asked is

## 24535:00 - 24565:00

there an error it would say no did a

## 24565:00 - 24575:00

great

## 24575:00 - 24615:00

But Hamill had the context of knowing,

## 24615:00 - 24645:00

oh, we don't actually have this virtual

## 24645:00 - 24680:00

tour functionality, right? So, I think

## 24680:00 - 24710:00

in these cases, it's so important to

## 24710:00 - 24740:00

make sure you are manually doing this

## 24740:00 - 24775:00

yourself. Um, and we'll talk a we can

## 24775:00 - 24800:00

talk a little bit more about when to use

## 24800:00 - 24845:00

LLMs in the process later, but like

## 24845:00 - 24875:00

number one pitfall right here is people

## 24875:00 - 24900:00

are like, let me automate this with an

## 24900:00 - 24920:00

LLM.

## 24920:00 - 24940:00

>> Do you think they'll we'll get to a

## 24940:00 - 24975:00

place where where an agent can do this?

## 24975:00 - 25005:00

>> Oh, no, no, no. Sorry. There are parts

## 25005:00 - 25050:00

of error analysis that an LLM is suited

## 25050:00 - 25085:00

for which we can talk about later in

## 25085:00 - 25100:00

this podcast

## 25100:00 - 25140:00

>> but right now in this stage of free form

## 25140:00 - 25180:00

note takingaking is not the

## 25180:00 - 25200:00

>> place for an LLM.

## 25200:00 - 25225:00

>> And this is something you call open

## 25225:00 - 25240:00

coding this.

## 25240:00 - 25265:00

>> Yes, absolutely.

## 25265:00 - 25310:00

>> Uh another uh term that you used in your

## 25310:00 - 25345:00

post that I love and that's fits into

## 25345:00 - 25380:00

this step is this idea of a benevolent

## 25380:00 - 25420:00

dictator. Maybe just talk about what

## 25420:00 - 25450:00

that is and maybe Sha cover that.

## 25450:00 - 25485:00

>> Yeah. So Hamill actually came up with

## 25485:00 - 25495:00

this term.

## 25495:00 - 25550:00

>> Okay, maybe Ham will cover the answer.

## 25550:00 - 25590:00

>> No problem. And we'll actually show the

## 25590:00 - 25635:00

LM automation in this example because

## 25635:00 - 25660:00

we're going to take this example. We're

## 25660:00 - 25675:00

going to go all the way through.

## 25675:00 - 25680:00

>> Amazing.

## 25680:00 - 25745:00

>> And so and so um benevolent dictator is

## 25745:00 - 25820:00

just a catchy term for the fact that

## 25820:00 - 25850:00

when you're doing this open coding, a

## 25850:00 - 25905:00

lot of teams get bogged down in having a

## 25905:00 - 25950:00

committee do this. And for a lot of

## 25950:00 - 26000:00

situations that's wholly unnecessary

## 26000:00 - 26030:00

like

## 26030:00 - 26060:00

you know people get really uncomfortable

## 26060:00 - 26125:00

with okay you know we want everybody on

## 26125:00 - 26155:00

board we want everybody involved so on

## 26155:00 - 26190:00

and so forth. You need to cut through

## 26190:00 - 26250:00

the noise. Um in a lot of organizations

## 26250:00 - 26285:00

if you look really deeply especially

## 26285:00 - 26330:00

small mediumsiz companies there's really

## 26330:00 - 26365:00

like you can appoint one person whose

## 26365:00 - 26420:00

taste that you trust. Um, and you can

## 26420:00 - 26445:00

you can do this with a small number of

## 26445:00 - 26490:00

people and often one person. And that's

## 26490:00 - 26525:00

it's really important to make this

## 26525:00 - 26555:00

tractable. You don't want to make this

## 26555:00 - 26585:00

process so expensive that you can't do

## 26585:00 - 26620:00

it. You're going to lose out. So that's

## 26620:00 - 26660:00

the idea behind benevolent dictator is,

## 26660:00 - 26710:00

hey, you need to simplify this

## 26710:00 - 26750:00

across as many dimensions as you can.

## 26750:00 - 26770:00

Another thing that we'll talk about

## 26770:00 - 26825:00

later is when you goes to building an

## 26825:00 - 26865:00

LLM as a judge, you need a binary score.

## 26865:00 - 26890:00

You don't want to think about is this

## 26890:00 - 26935:00

like a one, two, three, four, five, like

## 26935:00 - 26970:00

assign a score to it. You can't. That's

## 26970:00 - 27000:00

going to slow it down. Just to make sure

## 27000:00 - 27030:00

this benevolent dictator point is is

## 27030:00 - 27055:00

really clear. Basically, this is the

## 27055:00 - 27095:00

person that does this note-taking and

## 27095:00 - 27125:00

ideally they're the expert on the stuff.

## 27125:00 - 27165:00

So, if it's law stuff, maybe there's

## 27165:00 - 27195:00

like a legal person that owns this. It

## 27195:00 - 27230:00

could be a product manager. Give us

## 27230:00 - 27265:00

advice on who this person should be.

## 27265:00 - 27290:00

>> Yeah, it should be the person with

## 27290:00 - 27345:00

domain expertise. So in this case you

## 27345:00 - 27390:00

know it would be the person who

## 27390:00 - 27445:00

understands the business of leasing

## 27445:00 - 27475:00

apartment leasing and has context to

## 27475:00 - 27515:00

understand if this makes sense. It's

## 27515:00 - 27540:00

it's always the domain expert like you

## 27540:00 - 27570:00

said okay for legal it would be a law

## 27570:00 - 27605:00

person for mental health it would be the

## 27605:00 - 27635:00

mental health expert whether that's like

## 27635:00 - 27685:00

a psychiatrist or you know someone else.

## 27685:00 - 27690:00

>> Cool.

## 27690:00 - 27735:00

>> Um oftentimes it is the product manager.

## 27735:00 - 27760:00

>> Cool. So the advice here, pick that

## 27760:00 - 27795:00

person. May not feel so super fair that

## 27795:00 - 27810:00

they're the one in charge and they're

## 27810:00 - 27850:00

the dictator, but they're benevolent.

## 27850:00 - 27875:00

It's going to go be okay.

## 27875:00 - 27905:00

>> Yeah, it's going to be okay. You're just

## 27905:00 - 27935:00

trying to It's not perfection. You're

## 27935:00 - 27995:00

just trying to make progress and

## 27995:00 - 28035:00

in get signal quickly so you have an

## 28035:00 - 28075:00

idea of what to work on because it can

## 28075:00 - 28105:00

become infinitely expensive if you're

## 28105:00 - 28115:00

not careful.

## 28115:00 - 28140:00

>> Yeah. Okay, cool. Let's go back to your

## 28140:00 - 28190:00

examples. Yeah, no problem. So this is

## 28190:00 - 28265:00

another example where we have

## 28265:00 - 28305:00

someone saying, "Okay, do you have any

## 28305:00 - 28350:00

specials?"

## 28350:00 - 28415:00

And the assistant or the AI responds,

## 28415:00 - 28465:00

"Hey, we have a 5% military discount."

## 28465:00 - 28500:00

User responds, "Can you," and it

## 28500:00 - 28525:00

switches a subject, can you tell me how

## 28525:00 - 28570:00

many floors there are? Do you have any

## 28570:00 - 28605:00

onebedrooms available or one bedrooms on

## 28605:00 - 28670:00

the first floor? And the AI responds,

## 28670:00 - 28695:00

"Yeah, okay. We have several one-bedroom

## 28695:00 - 28735:00

apartments available." And then the user

## 28735:00 - 28760:00

wants to confirm any of those on the

## 28760:00 - 28795:00

first floor. And how much are the

## 28795:00 - 28850:00

onebedrooms? And then also is is a

## 28850:00 - 28875:00

current resident. So it's they're also

## 28875:00 - 28905:00

asking, I need a maintenance request.

## 28905:00 - 28935:00

This is actually pretty like you could

## 28935:00 - 28975:00

see the messiness of the real world in

## 28975:00 - 29020:00

here. And the assistant just calls a

## 29020:00 - 29055:00

tool that says transfer call,

## 29055:00 - 29105:00

>> but it doesn't say anything. It just

## 29105:00 - 29150:00

abruptly does transfer call.

## 29150:00 - 29190:00

>> So it's pretty jank I would say like

## 29190:00 - 29240:00

it's just not you know another jank

## 29240:00 - 29265:00

>> another kind of jank a different kind of

## 29265:00 - 29280:00

jank. So you don't want to when you

## 29280:00 - 29300:00

write the open note you don't want to

## 29300:00 - 29325:00

say jank because what we want to do is

## 29325:00 - 29365:00

we want to understand what and when we

## 29365:00 - 29385:00

look at the notes later on we want to

## 29385:00 - 29410:00

understand like what happened. So you

## 29410:00 - 29455:00

just want to say um you know did not

## 29455:00 - 29485:00

confirm

## 29485:00 - 29540:00

call transfer

## 29540:00 - 29595:00

with uh with user.

## 29595:00 - 29620:00

It doesn't have to be perfect. You just

## 29620:00 - 29640:00

have to have a general idea of what's

## 29640:00 - 29650:00

going on.

## 29650:00 - 29660:00

>> Cool.

## 29660:00 - 29715:00

>> So okay. So let's say we do and we Treya

## 29715:00 - 29760:00

and I we recommend doing at least a

## 29760:00 - 29790:00

hundred of these. The question is always

## 29790:00 - 29840:00

like how many of this do you do? And so

## 29840:00 - 29900:00

there's not a magic number. we say 100

## 29900:00 - 29945:00

is because we know that as soon as you

## 29945:00 - 30020:00

start doing this once you do 20 of these

## 30020:00 - 30075:00

you will automatically find it so useful

## 30075:00 - 30130:00

that you will continue doing it. So we

## 30130:00 - 30180:00

just say 100 to mentally unblock you so

## 30180:00 - 30240:00

it's not intimidating like don't worry

## 30240:00 - 30280:00

you're only going to do 100

## 30280:00 - 30340:00

and there is a a term for that of so so

## 30340:00 - 30395:00

the right answer is keep looking at

## 30395:00 - 30440:00

traces until you feel like you're not

## 30440:00 - 30485:00

learning anything new

## 30485:00 - 30500:00

should talk about

## 30500:00 - 30540:00

>> yeah so there's actually a term in data

## 30540:00 - 30585:00

analysis and quant qualitative analysis

## 30585:00 - 30625:00

called theoretical saturation

## 30625:00 - 30660:00

So what this means is when you do all of

## 30660:00 - 30710:00

these processes of looking at your data

## 30710:00 - 30770:00

when do you stop? It's when you are

## 30770:00 - 30820:00

saturating or you're not uncovering any

## 30820:00 - 30860:00

new types of notes, new types of

## 30860:00 - 30905:00

concepts or nothing that will like

## 30905:00 - 30940:00

materially change the next part of your

## 30940:00 - 30985:00

process. Um, and this kind of takes a

## 30985:00 - 31025:00

little bit of intuition to develop. So

## 31025:00 - 31050:00

typically people don't really know when

## 31050:00 - 31080:00

they've reached theoretical saturation

## 31080:00 - 31125:00

yet. That's totally fine. When you do

## 31125:00 - 31165:00

two or three examples or rounds of this,

## 31165:00 - 31205:00

like you will develop the intuition. A

## 31205:00 - 31230:00

lot of people realize like, oh, okay,

## 31230:00 - 31265:00

like I only need to do 40. I only need

## 31265:00 - 31305:00

to do 60. Actually, I only need to do

## 31305:00 - 31335:00

like 15. I don't know. Like depends on

## 31335:00 - 31365:00

the application and develops like how

## 31365:00 - 31400:00

depends on how savvy you are with error

## 31400:00 - 31425:00

analysis. For sure.

## 31425:00 - 31450:00

>> And your point about you probably want

## 31450:00 - 31485:00

to you're going to want to do a bunch. I

## 31485:00 - 31505:00

imagine it's because you're just like,

## 31505:00 - 31525:00

oh, I'm discovering all these problems.

## 31525:00 - 31560:00

I got to see what else is going on here.

## 31560:00 - 31605:00

>> Exactly. And I promise at some point

## 31605:00 - 31630:00

you're like not going to discover new

## 31630:00 - 31650:00

types of problems.

## 31650:00 - 31680:00

>> Yeah. Awesome. So let's say you did a

## 31680:00 - 31710:00

100 of these. What's the next step?

## 31710:00 - 31735:00

>> Yeah. Okay. So you did 100 of these. Now

## 31735:00 - 31790:00

you have all these notes. So this is

## 31790:00 - 31835:00

where you can start using AI to help

## 31835:00 - 31885:00

you. Um you So the part where you looked

## 31885:00 - 31935:00

at this data is important. Like we

## 31935:00 - 31960:00

discussed, you don't want to automate

## 31960:00 - 32000:00

this part too much. Humans will still

## 32000:00 - 32025:00

have jobs. This is a takeaway here.

## 32025:00 - 32035:00

That's great.

## 32035:00 - 32070:00

>> Yes. Just reviewing traces. At least

## 32070:00 - 32090:00

there's one job left for now.

## 32090:00 - 32170:00

>> Yeah. So, yeah, exactly. Um, and so,

## 32170:00 - 32210:00

okay, you have all these notes.

## 32210:00 - 32290:00

Now, to turn this into something useful,

## 32290:00 - 32330:00

you can do basic counting. So, basic

## 32330:00 - 32375:00

counting is the most powerful analytical

## 32375:00 - 32415:00

technique in data science uh because

## 32415:00 - 32460:00

it's so simple and it's kind of

## 32460:00 - 32485:00

undervalued

## 32485:00 - 32525:00

um in many cases. And so, it's very

## 32525:00 - 32555:00

approachable for people. And so the

## 32555:00 - 32575:00

first thing you want you want to do is

## 32575:00 - 32630:00

take these notes and you can categorize

## 32630:00 - 32660:00

them with an LLM. And so there's a lot

## 32660:00 - 32690:00

of different ways to do that. Right

## 32690:00 - 32745:00

before this podcast, I took three

## 32745:00 - 32775:00

different

## 32775:00 - 32855:00

uh coding agents or you know uh AI tools

## 32855:00 - 32910:00

and had it categorize these notes. So

## 32910:00 - 32950:00

one is okay, I uploaded into a cloud

## 32950:00 - 33005:00

project. I uploaded a CSV of these notes

## 33005:00 - 33050:00

and I just exported them directly from

## 33050:00 - 33085:00

this interface. Um, there's a lot of

## 33085:00 - 33110:00

different ways to do this, but I'm I'm

## 33110:00 - 33170:00

showing you the simple stupid way, the

## 33170:00 - 33225:00

most basic way of doing things.

## 33225:00 - 33275:00

And so I dumped the CSV in here and I

## 33275:00 - 33315:00

said, "Please analyze the following CSV

## 33315:00 - 33350:00

file. There's and I told it there's a

## 33350:00 - 33405:00

metadata field that has a note in it."

## 33405:00 - 33440:00

But what I said is I used the word open

## 33440:00 - 33480:00

codes. I said, "Hey, I have different

## 33480:00 - 33520:00

open codes

## 33520:00 - 33570:00

and that's a term of art. That's um LMS

## 33570:00 - 33600:00

know what open codes are and they know

## 33600:00 - 33665:00

what axial codes are because it is a it

## 33665:00 - 33690:00

is a concept that's been around for a

## 33690:00 - 33735:00

really long time. So those words help me

## 33735:00 - 33770:00

shortcut like what I'm trying to do."

## 33770:00 - 33790:00

>> That's awesome. And the end of the end

## 33790:00 - 33820:00

of the prompt is telling it to create

## 33820:00 - 33845:00

axial codes.

## 33845:00 - 33895:00

>> Yes, creating a codes. So what it does

## 33895:00 - 33905:00

is

## 33905:00 - 33930:00

>> so maybe it's worth talking about what

## 33930:00 - 33965:00

are axial codes or like what's the point

## 33965:00 - 34010:00

here right you have a mess of open codes

## 34010:00 - 34060:00

right and you don't have 100 distinct

## 34060:00 - 34095:00

problems actually mo many of them are

## 34095:00 - 34130:00

repeats but because you phrased them

## 34130:00 - 34165:00

differently right and in that you

## 34165:00 - 34190:00

shouldn't have tried to create your

## 34190:00 - 34220:00

taxonomy of failures as you're open

## 34220:00 - 34255:00

coding you just want to get down what's

## 34255:00 - 34290:00

wrong and then organize okay what's the

## 34290:00 - 34345:00

most common failure mode so the purpose

## 34345:00 - 34385:00

axial code basically is just a failure

## 34385:00 - 34425:00

mode. It's like the label or category.

## 34425:00 - 34470:00

And what our goal is is to get to this

## 34470:00 - 34505:00

clusters of failure modes and figure out

## 34505:00 - 34540:00

what is the most prevalent. So then you

## 34540:00 - 34600:00

can go and run and attack that problem.

## 34600:00 - 34615:00

>> That is really helpful. Basically,

## 34615:00 - 34640:00

you're just synthesizing all these

## 34640:00 - 34665:00

categories

## 34665:00 - 34680:00

and themes.

## 34680:00 - 34720:00

>> Super cool. And we'll uh include this

## 34720:00 - 34745:00

prompt in our show notes for folks so

## 34745:00 - 34765:00

they don't have to like sit there and

## 34765:00 - 34800:00

screenshot it and try to type it out

## 34800:00 - 34815:00

themselves.

## 34815:00 - 34850:00

>> Yeah, great idea.

## 34850:00 - 34900:00

Um, and so Claude, you know, went ahead

## 34900:00 - 34945:00

and analyzed the CSV file, decided how

## 34945:00 - 34970:00

to parse it, blah, blah, blah. We don't

## 34970:00 - 35000:00

need to worry about all that stuff. But

## 35000:00 - 35035:00

it came up with a bunch of axial codes.

## 35035:00 - 35070:00

Basically, axial codes are categories

## 35070:00 - 35125:00

like Shrea said. So one is okay

## 35125:00 - 35145:00

capability limitations,

## 35145:00 - 35175:00

misrepresentation,

## 35175:00 - 35205:00

pro processing, protocol violations,

## 35205:00 - 35240:00

human handoff issues, communication

## 35240:00 - 35270:00

quality.

## 35270:00 - 35320:00

It created these categories. Now, do I

## 35320:00 - 35370:00

like all the categories? Not really. I

## 35370:00 - 35400:00

like some of them. It's a good first

## 35400:00 - 35450:00

like stab at it. I would probably rename

## 35450:00 - 35475:00

it a little bit because some of them are

## 35475:00 - 35510:00

a bit too generic. Like what is

## 35510:00 - 35540:00

capability limitations? That's a little

## 35540:00 - 35570:00

bit too broad. That's not actionable. I

## 35570:00 - 35595:00

want to get like a little bit more

## 35595:00 - 35630:00

actionable with it so that if I do

## 35630:00 - 35655:00

decide it's a problem, I know what to do

## 35655:00 - 35685:00

with it. But we'll discuss that in a

## 35685:00 - 35725:00

little bit. Um, so you can do this like

## 35725:00 - 35755:00

with anything. And this is the dumbest

## 35755:00 - 35805:00

way to do it, but dumb sometimes is a

## 35805:00 - 35825:00

good way to get started. So,

## 35825:00 - 35845:00

>> and and this is what LM are really good

## 35845:00 - 35870:00

at, taking a bunch of information and

## 35870:00 - 35885:00

synthesizing.

## 35885:00 - 35910:00

>> Absolutely. Synthesizing for us to make

## 35910:00 - 35940:00

sense of, right? Note that, you know,

## 35940:00 - 35960:00

it's not telling us, it's not

## 35960:00 - 35990:00

automatically proposing fixes or

## 35990:00 - 36020:00

anything. That's our job.

## 36020:00 - 36045:00

>> But, you know, now we can wade through

## 36045:00 - 36080:00

this mess of open codes a lot easier.

## 36080:00 - 36110:00

Another thing that's interesting here in

## 36110:00 - 36150:00

this prompt to generate the axial codes

## 36150:00 - 36195:00

is you can be very detailed if you want,

## 36195:00 - 36240:00

right? You can say I want each axial

## 36240:00 - 36290:00

code to actually be you know some

## 36290:00 - 36335:00

actionable failure mode and maybe the

## 36335:00 - 36375:00

LLM will understand that and propose it

## 36375:00 - 36420:00

or I want you to group these open codes

## 36420:00 - 36485:00

by you know what stage of the user story

## 36485:00 - 36520:00

that it's in. So this is where you can

## 36520:00 - 36565:00

you know be creative or do what's best

## 36565:00 - 36610:00

for you as a product manager or engineer

## 36610:00 - 36635:00

working on this and that will help you

## 36635:00 - 36660:00

do the improvement later.

## 36660:00 - 36695:00

>> Okay. So there's no definitive prompt of

## 36695:00 - 36720:00

here's the one way to do it. You're

## 36720:00 - 36755:00

saying there's you can iterate, see what

## 36755:00 - 36765:00

works for you.

## 36765:00 - 36775:00

>> Absolutely.

## 36775:00 - 36795:00

>> It's interesting the tools don't want to

## 36795:00 - 36820:00

do this or or do they try and they just

## 36820:00 - 36835:00

don't do a great job?

## 36835:00 - 36870:00

>> No, I don't think they do it. We've been

## 36870:00 - 36895:00

screaming from the rooftops, please,

## 36895:00 - 36930:00

please do this. I do think it's a little

## 36930:00 - 36970:00

bit hard, right? Like part of this whole

## 36970:00 - 37000:00

um experience with the EVOS course

## 37000:00 - 37030:00

Hamill and I are teaching are like a lot

## 37030:00 - 37060:00

of people don't actually know this.

## 37060:00 - 37085:00

>> So maybe it's that people don't know

## 37085:00 - 37105:00

this and they don't know how to build

## 37105:00 - 37165:00

tools for it. Um, and hopefully we can

## 37165:00 - 37215:00

demystify some of this magic.

## 37215:00 - 37250:00

>> And just to double click on this point,

## 37250:00 - 37285:00

like this is not a thing everyone does

## 37285:00 - 37310:00

or knows. This is something you two

## 37310:00 - 37345:00

developed based on your experience doing

## 37345:00 - 37380:00

data analysis and data science at at

## 37380:00 - 37390:00

other companies.

## 37390:00 - 37430:00

>> Well, I want to caveat. We didn't invent

## 37430:00 - 37460:00

error analysis. We don't actually want

## 37460:00 - 37500:00

to invent things. That's a bad that's

## 37500:00 - 37530:00

bad signal. If somebody is coming to you

## 37530:00 - 37555:00

with a way to do something that's like

## 37555:00 - 37585:00

entirely new and not grounded in

## 37585:00 - 37615:00

hundreds of years of theory and

## 37615:00 - 37680:00

literature then you should I don't know

## 37680:00 - 37710:00

be a little bit wary of that. But what

## 37710:00 - 37745:00

we tried to do was distill okay what are

## 37745:00 - 37775:00

the new tools and techniques that you

## 37775:00 - 37835:00

need to know make sense of the LLM error

## 37835:00 - 37870:00

analysis and then we created a

## 37870:00 - 37905:00

curriculum or structured way of doing

## 37905:00 - 37940:00

this. So this is all very tailored to

## 37940:00 - 37975:00

LLMs, but you know the terms open

## 37975:00 - 38045:00

coding, axial coding are grounded in um

## 38045:00 - 38070:00

social science.

## 38070:00 - 38105:00

>> Amazing. Okay. Like what's funny about

## 38105:00 - 38130:00

you guys doing this is I just want to go

## 38130:00 - 38155:00

do this somewhere. I don't have I don't

## 38155:00 - 38185:00

have an AI product to do this on, but

## 38185:00 - 38210:00

it's just like oh this would be so fun.

## 38210:00 - 38235:00

Just sit there and find all the problems

## 38235:00 - 38270:00

I'm running into and categorize them and

## 38270:00 - 38300:00

then try to fix them. Delightful.

## 38300:00 - 38325:00

>> I love that.

## 38325:00 - 38350:00

>> Haml pulled up a video. What do you got

## 38350:00 - 38360:00

going on here?

## 38360:00 - 38390:00

>> Yeah. So I pulled up a video just to

## 38390:00 - 38435:00

drive home Shrea's point like we are not

## 38435:00 - 38460:00

inventing anything. So what you see on

## 38460:00 - 38510:00

the screen here is Andrew Ang one of the

## 38510:00 - 38580:00

famous machine learning uh researchers

## 38580:00 - 38610:00

in the world who have taught a lot of

## 38610:00 - 38660:00

people frankly machine learning and um

## 38660:00 - 38705:00

you can see this is a 8-year-old video.

## 38705:00 - 38755:00

So and he's talking about error analysis

## 38755:00 - 38785:00

and so this is a technique that's been

## 38785:00 - 38840:00

used to analyze stochastic systems for

## 38840:00 - 38885:00

ages. Um, and it's some it's something

## 38885:00 - 38920:00

that you're just using the same machine

## 38920:00 - 38950:00

learning ideas and principles is

## 38950:00 - 38975:00

bringing them in into here because

## 38975:00 - 39010:00

again, these are stochcastic systems.

## 39010:00 - 39045:00

>> Awesome. Well, one thing we're working

## 39045:00 - 39070:00

on getting Andrew in the podcast. We're

## 39070:00 - 39100:00

chatting. So, that'll be really fun. Uh,

## 39100:00 - 39130:00

two, I love that my other my podcast

## 39130:00 - 39150:00

episode just came out today is in your

## 39150:00 - 39175:00

feed there, and it's standing out really

## 39175:00 - 39205:00

well in that feed. So, I'm really happy

## 39205:00 - 39220:00

about that thumbnail.

## 39220:00 - 39240:00

>> Very nice. Yeah, the recommendation

## 39240:00 - 39255:00

algorithm is

## 39255:00 - 39285:00

>> Yes. Here we go. I hope you click on

## 39285:00 - 39355:00

that. Don't don't screw my algorithm.

## 39355:00 - 39380:00

Okay, cool. So, we've done some

## 39380:00 - 39400:00

synthesis. What's I know we're not going

## 39400:00 - 39425:00

to go through the entire step. This is

## 39425:00 - 39450:00

like you have a whole course that takes

## 39450:00 - 39485:00

many days to learn this whole process.

## 39485:00 - 39505:00

What else do you want to share about how

## 39505:00 - 39520:00

to go about this process?

## 39520:00 - 39540:00

>> Okay, so you can you can do this through

## 39540:00 - 39575:00

anything and you know I've used the same

## 39575:00 - 39615:00

thing works just fine in chat GPT. The

## 39615:00 - 39650:00

same exact prompt. You can see it it

## 39650:00 - 39690:00

made axial codes. I really like using

## 39690:00 - 39730:00

Julius AI. Um it's one of my favorite

## 39730:00 - 39790:00

tools. Julius is a is a kind of his

## 39790:00 - 39820:00

third party tool but uses notebooks. I

## 39820:00 - 39860:00

personally like Jupyter notebooks a lot

## 39860:00 - 39905:00

and so it's more of a data science thing

## 39905:00 - 39945:00

but a lot of product managers are kind

## 39945:00 - 39995:00

of learning notebooks nowadays and it's

## 39995:00 - 40020:00

kind of cool it's like a fun playground

## 40020:00 - 40045:00

where you can like write code and look

## 40045:00 - 40080:00

at data but we don't have to go deeply

## 40080:00 - 40105:00

into that just wanted to mention you can

## 40105:00 - 40145:00

use a lot you know AI is really good at

## 40145:00 - 40210:00

this so let's go to the fun part here we

## 40210:00 - 40270:00

go so now we have all the a we have

## 40270:00 - 40300:00

these axial codes so the first thing I

## 40300:00 - 40385:00

like to do I have these open codes right

## 40385:00 - 40440:00

and I have the axial codes that let's

## 40440:00 - 40465:00

say

## 40465:00 - 40510:00

you know the like that we assigned from

## 40510:00 - 40555:00

the cloud project or the chat GPT and so

## 40555:00 - 40620:00

what I do is I collect them first and I

## 40620:00 - 40645:00

take a look like does these axial codes

## 40645:00 - 40685:00

make sense and I look at the

## 40685:00 - 40710:00

correspondence between the different

## 40710:00 - 40760:00

axial codes and the open codes and I and

## 40760:00 - 40795:00

I go through an exercise and I say hm do

## 40795:00 - 40840:00

I like these these codes like can I make

## 40840:00 - 40870:00

them better? Can I refine them? Can I

## 40870:00 - 40920:00

make them more specific? Um you know

## 40920:00 - 40950:00

instead of like being generic I make

## 40950:00 - 40990:00

them very specific in actionable. So you

## 40990:00 - 41025:00

see the ones that I came up with here

## 41025:00 - 41075:00

are tour scheduling rescheduling issues

## 41075:00 - 41120:00

human handoff or transfer issue

## 41120:00 - 41150:00

formatting error with an output

## 41150:00 - 41180:00

conversational flow. We saw the

## 41180:00 - 41210:00

conversational flow issue with the text

## 41210:00 - 41235:00

messages.

## 41235:00 - 41290:00

uh making follow-up promises not kept

## 41290:00 - 41330:00

and and so basically what I can do what

## 41330:00 - 41400:00

you can do now is like you have these

## 41400:00 - 41435:00

axial codes

## 41435:00 - 41480:00

and um so I just collect them into a

## 41480:00 - 41515:00

list. So this is an Excel formula just

## 41515:00 - 41550:00

collect these codes into a list. So now

## 41550:00 - 41585:00

we have a commaepparated list of these

## 41585:00 - 41620:00

codes. And then what you can simply do

## 41620:00 - 41655:00

is you could take your notes that you

## 41655:00 - 41695:00

have those open codes and you can tell

## 41695:00 - 41755:00

an AI and this is using Gemini and AI

## 41755:00 - 41800:00

just for simplicity. This is like the

## 41800:00 - 41825:00

you know again we're trying to keep it

## 41825:00 - 41870:00

simple categorize

## 41870:00 - 41910:00

uh the following note into one of the

## 41910:00 - 41945:00

following categories. That's way this

## 41945:00 - 41975:00

for folks watching there's like I like

## 41975:00 - 42000:00

all these different prompts and formulas

## 42000:00 - 42030:00

you're showing. This is like the Google

## 42030:00 - 42085:00

Sheets AI AI prompt.

## 42085:00 - 42120:00

>> Yeah.

## 42120:00 - 42155:00

>> And so basically what you can do is you

## 42155:00 - 42200:00

can then have you can categorize your

## 42200:00 - 42260:00

faces into one of the buckets

## 42260:00 - 42290:00

and that's what we have here. We have

## 42290:00 - 42335:00

categorized all those problems that we

## 42335:00 - 42365:00

encountered into one of these things.

## 42365:00 - 42395:00

>> And this is automatic which is very

## 42395:00 - 42440:00

exciting. I mean the AI is doing it. So

## 42440:00 - 42480:00

this also drives home the point that

## 42480:00 - 42505:00

your open codes have to be detailed,

## 42505:00 - 42545:00

right? You can't just say janky because

## 42545:00 - 42585:00

if the AI is reading janky, it's not

## 42585:00 - 42615:00

going to be able to categorize it. Even

## 42615:00 - 42640:00

a human wouldn't, right? It would have

## 42640:00 - 42690:00

to go and remember why you said janky.

## 42690:00 - 42715:00

>> So it's important to be, you know,

## 42715:00 - 42755:00

somewhat detailed in your open code.

## 42755:00 - 42785:00

>> Okay. So avoid the word janky is a good

## 42785:00 - 42800:00

rule of thumb

## 42800:00 - 42840:00

>> or other words.

## 42840:00 - 42850:00

>> Okay.

## 42850:00 - 42870:00

>> I was being funny.

## 42870:00 - 42895:00

>> Yeah. Okay. What are some of those other

## 42895:00 - 42920:00

words just to that come that people

## 42920:00 - 42950:00

often use that you think are not good?

## 42950:00 - 42980:00

>> I don't think it's specific words. I

## 42980:00 - 43010:00

think it's just people are not detailed

## 43010:00 - 43045:00

enough in the open code. So it's hard to

## 43045:00 - 43070:00

do the categorization.

## 43070:00 - 43095:00

>> Great. And by the way, the reason you

## 43095:00 - 43130:00

have to map them back is because say

## 43130:00 - 43175:00

clott JPT gave you suggestions and you

## 43175:00 - 43210:00

changed them and iterated on them. So it

## 43210:00 - 43240:00

doesn't you can't just go back and say

## 43240:00 - 43265:00

cool what are in each bucket.

## 43265:00 - 43285:00

>> Yeah. Yeah.

## 43285:00 - 43315:00

>> Great. That's a really good question

## 43315:00 - 43350:00

actually. It's good to iterate and think

## 43350:00 - 43385:00

on about it a little bit like do I like

## 43385:00 - 43420:00

these open codes? Do these actually make

## 43420:00 - 43460:00

sense to me? Just like anything that AI

## 43460:00 - 43500:00

does, it's really good to kind of put

## 43500:00 - 43525:00

yourself in the middle

## 43525:00 - 43555:00

>> just in the loop. Still space.

## 43555:00 - 43565:00

>> Yes. Great.

## 43565:00 - 43570:00

>> Yeah.

## 43570:00 - 43595:00

>> One of the things that I like to do in

## 43595:00 - 43635:00

this step if I'm trying to use AI to do

## 43635:00 - 43675:00

this labeling is also have a new

## 43675:00 - 43735:00

category called none of the above. So an

## 43735:00 - 43775:00

AI can actually say none of the above in

## 43775:00 - 43825:00

the axial code and that informs me,

## 43825:00 - 43870:00

okay, my axial codes are not complete.

## 43870:00 - 43910:00

Like let's go look at those open codes.

## 43910:00 - 43935:00

Let's figure out what some new

## 43935:00 - 43965:00

categories are or figure out how to

## 43965:00 - 44000:00

reword my other axial codes.

## 44000:00 - 44025:00

>> Awesome. And what's cool about this is

## 44025:00 - 44050:00

you don't need to do this many many

## 44050:00 - 44065:00

times. Like no,

## 44065:00 - 44095:00

>> for most products, you do this process

## 44095:00 - 44120:00

once and then you build on it, I

## 44120:00 - 44145:00

imagine, and you just tweak it over

## 44145:00 - 44150:00

time.

## 44150:00 - 44185:00

>> Absolutely. And it gets so fast. Like

## 44185:00 - 44220:00

people people do this like once a week

## 44220:00 - 44250:00

and you can do all of this in like 30

## 44250:00 - 44295:00

minutes and like suddenly your product

## 44295:00 - 44325:00

is like so much better than if you were

## 44325:00 - 44380:00

never aware of any of these problems.

## 44380:00 - 44415:00

>> Yeah. It's absurd to feel like you don't

## 44415:00 - 44440:00

you wouldn't know this is happening like

## 44440:00 - 44460:00

watching this happening. I'm like how

## 44460:00 - 44490:00

could you not do this to your product?

## 44490:00 - 44530:00

>> A lot of people have no idea.

## 44530:00 - 44545:00

>> Most people Yeah.

## 44545:00 - 44575:00

>> Yeah. We we'll talk about that. There's

## 44575:00 - 44595:00

a whole debate around this stuff that we

## 44595:00 - 44635:00

want to talk about. Uh okay cool. So you

## 44635:00 - 44665:00

have this you have the sheet. What comes

## 44665:00 - 44670:00

next?

## 44670:00 - 44705:00

>> Okay. So here's the big unveil.

## 44705:00 - 44750:00

>> This is the magic moment right now.

## 44750:00 - 44810:00

>> So we have all these codes we that you

## 44810:00 - 44855:00

know we applied the ones that we like on

## 44855:00 - 44920:00

our traces. Now you can do the tada. You

## 44920:00 - 44990:00

can count them. So here's a pivot table

## 44990:00 - 45020:00

and we just can do pivot table on those

## 45020:00 - 45050:00

and we can count how many times those

## 45050:00 - 45085:00

different things occurred. So what do we

## 45085:00 - 45140:00

find? found on this on these like traces

## 45140:00 - 45195:00

that we categorized, we found 17

## 45195:00 - 45235:00

conversational flow issues. And I really

## 45235:00 - 45260:00

like pivot tables because you can do

## 45260:00 - 45280:00

cool things. You can like double click

## 45280:00 - 45310:00

on these. You can say, "Oh, okay. Let me

## 45310:00 - 45350:00

let me take a look at those." But that's

## 45350:00 - 45400:00

going into an aside about pivot tables,

## 45400:00 - 45485:00

how cool they are. But um um you know

## 45485:00 - 45560:00

now we have just a nice rough cut of

## 45560:00 - 45605:00

what are our problems and now we have

## 45605:00 - 45670:00

gone from chaos to some kind of thinking

## 45670:00 - 45710:00

around oh you know what these are my

## 45710:00 - 45750:00

biggest problems I need to fix

## 45750:00 - 45790:00

conversational issues you know maybe

## 45790:00 - 45825:00

these human handoff issues it's not

## 45825:00 - 45860:00

necessarily the count is the most

## 45860:00 - 45890:00

important thing you know that might be

## 45890:00 - 45920:00

something that's just really bad and you

## 45920:00 - 45970:00

want to fix that. But okay, now you have

## 45970:00 - 46025:00

some way of looking at your problem and

## 46025:00 - 46050:00

now you can think about whether you need

## 46050:00 - 46075:00

evals

## 46075:00 - 46145:00

uh for for some of these. So you know

## 46145:00 - 46175:00

with the

## 46175:00 - 46200:00

you know there might be some of these

## 46200:00 - 46230:00

things that

## 46230:00 - 46290:00

might be just dumb engineering errors

## 46290:00 - 46320:00

that you don't need to write an eval for

## 46320:00 - 46355:00

because it's very obvious on how to fix

## 46355:00 - 46385:00

them.

## 46385:00 - 46410:00

um maybe the formatting error with

## 46410:00 - 46445:00

output. Maybe you just forgot to tell

## 46445:00 - 46500:00

the LLM how you want it to be formatted

## 46500:00 - 46530:00

and like you didn't even say that in the

## 46530:00 - 46550:00

prompt. So like just go ahead and fix

## 46550:00 - 46610:00

the prompt maybe, you know, and we can

## 46610:00 - 46650:00

decide like okay, do you want an uh do

## 46650:00 - 46685:00

you want to write an email for that? You

## 46685:00 - 46705:00

might be you might still want to write

## 46705:00 - 46735:00

an email for that because you might be

## 46735:00 - 46780:00

able to test that with just code. You

## 46780:00 - 46810:00

could just test the string. Does it have

## 46810:00 - 46855:00

the right formatting potentially without

## 46855:00 - 46900:00

running an LLM? So, there's a

## 46900:00 - 46940:00

costbenefit trade-off to eval. You don't

## 46940:00 - 47000:00

want to get carried away with it. Um,

## 47000:00 - 47030:00

but you want to start, you want to

## 47030:00 - 47070:00

usually ground yourself in your actual

## 47070:00 - 47105:00

errors. You don't want to skip this

## 47105:00 - 47140:00

step.

## 47140:00 - 47170:00

And so, the reason I'm kind of spending

## 47170:00 - 47210:00

so much time on this is like this is

## 47210:00 - 47235:00

where people get lost. they go straight

## 47235:00 - 47275:00

into eval like let me let me just write

## 47275:00 - 47330:00

some tests and that is where things go

## 47330:00 - 47405:00

off the rails. Um so let's let's okay so

## 47405:00 - 47435:00

let's say we want to tackle one of these

## 47435:00 - 47465:00

things.

## 47465:00 - 47500:00

So for example

## 47500:00 - 47545:00

uh let's say we want to

## 47545:00 - 47585:00

tackle this human handoff issue and

## 47585:00 - 47630:00

we're like hm I'm not really sure how to

## 47630:00 - 47660:00

fix this. like that's a kind of

## 47660:00 - 47735:00

subjective sort of judgment call on, you

## 47735:00 - 47765:00

know, should we be handing off to a

## 47765:00 - 47815:00

human and I don't know immediately how

## 47815:00 - 47860:00

to fix it. It's not super obvious, per

## 47860:00 - 47885:00

se. Yeah, I can like change my prompt,

## 47885:00 - 47925:00

but I'm not like sure. I'm not 100%

## 47925:00 - 47985:00

sure. Well, that might be sort of an

## 47985:00 - 48050:00

interesting um thing for an LLM as a

## 48050:00 - 48080:00

judge, for example. So, there's

## 48080:00 - 48110:00

different kinds of evals. One is

## 48110:00 - 48135:00

codebased

## 48135:00 - 48190:00

which you should try to do if you can

## 48190:00 - 48225:00

because they're cheaper. You don't have

## 48225:00 - 48270:00

to, you know, LM as a judge is something

## 48270:00 - 48305:00

it's like a meta eval. You have to eval

## 48305:00 - 48345:00

that eval to make sure the LM that's

## 48345:00 - 48380:00

judging is doing the right thing, which

## 48380:00 - 48425:00

we'll talk about in a second.

## 48425:00 - 48485:00

So, okay, LM as a judge, that's one

## 48485:00 - 48510:00

thing. Okay, how do you build an LM as a

## 48510:00 - 48540:00

judge? Before we get into that actually

## 48540:00 - 48565:00

just to make sure people know exactly

## 48565:00 - 48600:00

what you're describing there these two

## 48600:00 - 48630:00

types of evals. One is you said it's

## 48630:00 - 48675:00

code based one is LLM as judge. Maybe

## 48675:00 - 48700:00

Shrea just help us understand what that

## 48700:00 - 48730:00

what a codebased eval even is. It's just

## 48730:00 - 48755:00

like it's like essentially a unit test.

## 48755:00 - 48780:00

Is that a simple way to think about it?

## 48780:00 - 48805:00

>> Maybe eval is not the right term here

## 48805:00 - 48850:00

but think like automated evaluator. So

## 48850:00 - 48880:00

when we find these failure modes, one of

## 48880:00 - 48910:00

the things we want is like, okay, can we

## 48910:00 - 48940:00

now like go check the prevalence of that

## 48940:00 - 48975:00

failure mode in an automated way without

## 48975:00 - 49025:00

me manually labeling and doing all the

## 49025:00 - 49055:00

coding and the grouping and I want to

## 49055:00 - 49080:00

run it on thousands and thousands of

## 49080:00 - 49115:00

traces. I want to run it every week.

## 49115:00 - 49145:00

That is okay. You should probably build

## 49145:00 - 49185:00

an an automated evaluator to check for

## 49185:00 - 49220:00

that failure mode. Now when we're saying

## 49220:00 - 49270:00

codebased versus llm based, we're saying

## 49270:00 - 49305:00

okay so maybe I could write like a

## 49305:00 - 49340:00

python function or a piece of code to

## 49340:00 - 49365:00

check whether that failure mode is

## 49365:00 - 49400:00

present in a trace or not. And that's

## 49400:00 - 49440:00

possible to do for certain things like

## 49440:00 - 49500:00

you know checking the output is JSON um

## 49500:00 - 49530:00

or you know checking that it's markdown

## 49530:00 - 49560:00

or checking that it's short like these

## 49560:00 - 49585:00

are all things you can capture in code

## 49585:00 - 49620:00

or you can approximately capture in

## 49620:00 - 49655:00

code. uh when we're talking about LLM

## 49655:00 - 49690:00

judge here, we're saying that this is a

## 49690:00 - 49725:00

complex failure mode and we don't know

## 49725:00 - 49770:00

how to evaluate in an automated way. So

## 49770:00 - 49820:00

maybe we will try to use an LLM to

## 49820:00 - 49880:00

evaluate this very very narrow specific

## 49880:00 - 49930:00

failure mode of handoffs.

## 49930:00 - 49975:00

>> So just to try to mirror back how you're

## 49975:00 - 50005:00

describing, you want to test what your

## 50005:00 - 50045:00

say agent or AI product is doing. You

## 50045:00 - 50075:00

ask it a question, it gets back with

## 50075:00 - 50115:00

something. One way to test if it's

## 50115:00 - 50150:00

giving you the right answer is if it's

## 50150:00 - 50175:00

consistently doing the same thing that

## 50175:00 - 50215:00

you could write a code to te to tell you

## 50215:00 - 50250:00

this is true or false. For example, will

## 50250:00 - 50285:00

it ever say there's a virtual tour? So

## 50285:00 - 50305:00

you could ask it

## 50305:00 - 50340:00

>> is do you provide virtual tours?

## 50340:00 - 50365:00

>> It says yes or no and then you could

## 50365:00 - 50415:00

write code to tell you if it's correct

## 50415:00 - 50460:00

based on that specific answer. But if

## 50460:00 - 50480:00

you're asking about something more

## 50480:00 - 50510:00

complicated and it's not binary, you

## 50510:00 - 50555:00

almost need like in a in a one world you

## 50555:00 - 50580:00

need a human to tell you this is

## 50580:00 - 50620:00

correct. The solution to avoid humans

## 50620:00 - 50650:00

having to review all this every time

## 50650:00 - 50700:00

automatically is LLM's replacing human

## 50700:00 - 50740:00

judgment and you call it LLM as judge.

## 50740:00 - 50770:00

The LM is being the judge if this is

## 50770:00 - 50785:00

correct or not.

## 50785:00 - 50835:00

>> Absolutely. You nailed it. Um, so people

## 50835:00 - 50875:00

always think like, oh, like this is at

## 50875:00 - 50915:00

least as hard as my problem of creating

## 50915:00 - 50945:00

the original agent

## 50945:00 - 50985:00

>> and it's not because you're asking the

## 50985:00 - 51030:00

judge to do one thing, evaluate one

## 51030:00 - 51065:00

failure mode. So the scope of the

## 51065:00 - 51135:00

problem is very small and the output of

## 51135:00 - 51190:00

this LLM judge is like pass or fail. So

## 51190:00 - 51230:00

it is a very very tightly scoped thing

## 51230:00 - 51270:00

that LLM judges are very capable of

## 51270:00 - 51305:00

doing very reliably

## 51305:00 - 51325:00

>> and the goal here is just to have a

## 51325:00 - 51360:00

suite of tests that run before you ship

## 51360:00 - 51410:00

to production that tell you things are

## 51410:00 - 51440:00

going the way you want them to the way

## 51440:00 - 51470:00

your agent is interacting. Beautiful

## 51470:00 - 51500:00

thing about LLM judge is you can use

## 51500:00 - 51550:00

them in unit test or CI sure but you

## 51550:00 - 51605:00

could also use it online for monitoring

## 51605:00 - 51655:00

right like I can sample like thousand

## 51655:00 - 51700:00

traces every day run my LLM judge real

## 51700:00 - 51735:00

production traces and see what the

## 51735:00 - 51785:00

failure rate is there this is not a unit

## 51785:00 - 51820:00

test right but still now we get like an

## 51820:00 - 51855:00

extremely specific measure of

## 51855:00 - 51885:00

application quality

## 51885:00 - 51905:00

>> cool that's a really great point because

## 51905:00 - 51935:00

a lot of people disse for being this

## 51935:00 - 51970:00

like not real life thing. It's a thing

## 51970:00 - 51995:00

that you test before it's actually in

## 51995:00 - 52010:00

the real world and

## 52010:00 - 52025:00

>> what's actually happening in the real

## 52025:00 - 52045:00

world. You're saying you could actually

## 52045:00 - 52075:00

you should actually do exactly that.

## 52075:00 - 52095:00

Test your real thing running in

## 52095:00 - 52130:00

production and it's like a daily hourly

## 52130:00 - 52150:00

sort of thing you could be running.

## 52150:00 - 52170:00

>> Totally.

## 52170:00 - 52205:00

>> Awesome. Okay. Uh Hamill's got a a

## 52205:00 - 52240:00

example of an actual LM is Judge Eval

## 52240:00 - 52270:00

here. So let's take a look.

## 52270:00 - 52330:00

>> I love how Shrea really teed it up um

## 52330:00 - 52380:00

for me. So thank you so much. So what we

## 52380:00 - 52425:00

have is a LM as a judge prompt for this

## 52425:00 - 52465:00

one specific failure. Like Shrea said,

## 52465:00 - 52495:00

you would want to do one specific

## 52495:00 - 52565:00

failure and you want to make it binary

## 52565:00 - 52595:00

because we want to simplify things. We

## 52595:00 - 52625:00

don't want hey like score this on a

## 52625:00 - 52660:00

rating of one to five like how good is

## 52660:00 - 52710:00

it? That's just mostly in most cases

## 52710:00 - 52745:00

that's a weasel way of like not making a

## 52745:00 - 52785:00

decision. Like no, you need to make a

## 52785:00 - 52815:00

decision. Is this good enough or not?

## 52815:00 - 52865:00

Yes or no? can be painful to think about

## 52865:00 - 52905:00

what that is, but you should absolutely

## 52905:00 - 52930:00

do it. Otherwise, this thing becomes

## 52930:00 - 52955:00

very untractable. And then when you

## 52955:00 - 52985:00

report these metrics, no one knows what

## 52985:00 - 53040:00

3.2 versus 3.7 means.

## 53040:00 - 53075:00

>> This is Yeah, we see this all the time

## 53075:00 - 53110:00

also. And even with like expert curated

## 53110:00 - 53150:00

content on the internet where it's like,

## 53150:00 - 53190:00

oh, here's your LLM judge evaluator

## 53190:00 - 53250:00

prompt. Here's a one to seven scale. And

## 53250:00 - 53290:00

I always think I always text Hamill

## 53290:00 - 53320:00

like, "Oh no, like now we have to fight

## 53320:00 - 53365:00

the misinformation again because we know

## 53365:00 - 53390:00

somebody's going to try it out and then

## 53390:00 - 53435:00

come back to us and say, oh, I have 4.2

## 53435:00 - 53470:00

average." And we're going to be like,

## 53470:00 - 53515:00

"Okay,

## 53515:00 - 53540:00

it's wild how much drama there is in

## 53540:00 - 53580:00

Eval's space. We're going to get to

## 53580:00 - 53640:00

that." Oh man. This episode is brought

## 53640:00 - 53670:00

to you by Mercury. I've been banking

## 53670:00 - 53710:00

with Mercury for years and honestly I

## 53710:00 - 53745:00

can't imagine banking any other way at

## 53745:00 - 53780:00

this point. I switched from Chase and

## 53780:00 - 53820:00

holy moly what a difference. Sending

## 53820:00 - 53860:00

wires, tracking spend, giving people on

## 53860:00 - 53900:00

my team access to move money around so

## 53900:00 - 53940:00

freaking easy. Where most traditional

## 53940:00 - 53970:00

banking websites and apps are clunky and

## 53970:00 - 54015:00

hard to use, Mercury is meticulously

## 54015:00 - 54050:00

designed to be an intuitive and simple

## 54050:00 - 54085:00

experience. And Mercury brings all the

## 54085:00 - 54115:00

ways that you use money into a single

## 54115:00 - 54145:00

product, including credit cards,

## 54145:00 - 54185:00

invoicing, bill pay, reimbursements for

## 54185:00 - 54220:00

your teammates, and capital. Whether

## 54220:00 - 54250:00

you're a funded tech startup looking for

## 54250:00 - 54285:00

ways to pay contractors and earn yield

## 54285:00 - 54325:00

on your idle cash, or an agency that

## 54325:00 - 54355:00

needs to invoice customers and keep them

## 54355:00 - 54385:00

current, or an e-commerce brand that

## 54385:00 - 54415:00

needs to stay on top of cash flow and

## 54415:00 - 54450:00

excess capital, Mercury can be tailored

## 54450:00 - 54480:00

to help your business perform at its

## 54480:00 - 54525:00

highest level. See what over 200,000

## 54525:00 - 54565:00

entrepreneurs love about Mercury. Visit

## 54565:00 - 54610:00

mercury.com to apply online in 10

## 54610:00 - 54650:00

minutes. Mercury is a fintech, not a

## 54650:00 - 54675:00

bank. Banking services provided through

## 54675:00 - 54715:00

Mercury's FDIC insured partner banks.

## 54715:00 - 54740:00

For more details, check out the show

## 54740:00 - 54795:00

notes. Okay, so this is your judge

## 54795:00 - 54830:00

prompt. There's no one way to do it.

## 54830:00 - 54870:00

It's okay to use an LLM to help you

## 54870:00 - 54900:00

create it, but again, put yourself in

## 54900:00 - 54930:00

the loop. Don't just blindly accept what

## 54930:00 - 54970:00

the LLM does. And in all of these cases,

## 54970:00 - 54995:00

that's what we did. Like with the axial

## 54995:00 - 55035:00

codes, we kind of iterated on this. You

## 55035:00 - 55070:00

can use an LLM to like help you create

## 55070:00 - 55105:00

this prompt, but make sure you read it.

## 55105:00 - 55165:00

Make sure you edit it, whatever. This is

## 55165:00 - 55195:00

not necessarily the perfect prompt. This

## 55195:00 - 55240:00

is just the stupid like very keeping it

## 55240:00 - 55280:00

very simple just to show you the idea is

## 55280:00 - 55325:00

like, okay, for this handoff failure,

## 55325:00 - 55360:00

um, you know, I said, okay, I want you

## 55360:00 - 55400:00

to output true or false is binary. It's

## 55400:00 - 55425:00

a binary judge. That's what we

## 55425:00 - 55460:00

recommend. And then we then I just go

## 55460:00 - 55490:00

through and say, okay, like when should

## 55490:00 - 55535:00

you be doing a handoff? And I just list

## 55535:00 - 55570:00

them out like, okay, explicit human

## 55570:00 - 55610:00

request ignored or looped.

## 55610:00 - 55660:00

>> Uh some policy mandated transfer,

## 55660:00 - 55705:00

sensitive resident issues, tool data

## 55705:00 - 55740:00

unavailability,

## 55740:00 - 55785:00

same day walk-in or tour requests, you

## 55785:00 - 55810:00

know, you need to talk to a human for

## 55810:00 - 55855:00

that. So on and so forth, right? And so

## 55855:00 - 55885:00

the idea is like now that I know that

## 55885:00 - 55920:00

this is a failure

## 55920:00 - 55950:00

from my data, I'm interested in

## 55950:00 - 55980:00

iterating on it because I know this is

## 55980:00 - 56025:00

actually happening all the time. And

## 56025:00 - 56055:00

like Sha said, like it would be nice to

## 56055:00 - 56140:00

have a way not only to evaluate this on

## 56140:00 - 56165:00

like the data I have, but also on

## 56165:00 - 56190:00

production data just to get a sense of

## 56190:00 - 56220:00

like well what scale is this happening?

## 56220:00 - 56250:00

Let me find more traces. Let me have a

## 56250:00 - 56285:00

you know a way to iterate on this. And

## 56285:00 - 56320:00

so we can take this prompt and I'm going

## 56320:00 - 56365:00

to use a spreadsheet again.

## 56365:00 - 56390:00

So

## 56390:00 - 56450:00

the first step is okay when I'm doing

## 56450:00 - 56480:00

this judge I wrote the prompt. Now a lot

## 56480:00 - 56505:00

of people stop there and they say okay I

## 56505:00 - 56545:00

have my judge prompt we're done good

## 56545:00 - 56575:00

like let's just let's just ship it and

## 56575:00 - 56615:00

let's uh the prompt says if the judge

## 56615:00 - 56640:00

says it's wrong it's wrong. They just

## 56640:00 - 56675:00

like accept it as the gospel be like

## 56675:00 - 56720:00

okay the LM says it's wrong it's it must

## 56720:00 - 56760:00

be wrong. Don't do that because that's

## 56760:00 - 56810:00

the fastest way that you can have evals

## 56810:00 - 56865:00

that don't match what's going on. And

## 56865:00 - 56895:00

when people lose trust in your evals,

## 56895:00 - 56945:00

they'll lose trust in you. So, it's

## 56945:00 - 56970:00

really important that you don't do that.

## 56970:00 - 57010:00

And so, one before you release your LM

## 57010:00 - 57030:00

as a judge, you want to make sure it's

## 57030:00 - 57065:00

aligned to the human. So how do you do

## 57065:00 - 57115:00

that is you actually you have those

## 57115:00 - 57165:00

axial codes and you want to like measure

## 57165:00 - 57205:00

your judge against the axial code and

## 57205:00 - 57240:00

say like hey did does it agree with me?

## 57240:00 - 57270:00

Does my own judge does it agree with me?

## 57270:00 - 57305:00

Just measure it. And so what we have

## 57305:00 - 57350:00

here is okay I say assess this LLM

## 57350:00 - 57400:00

trace. Again I'm using just spreadsheets

## 57400:00 - 57450:00

here. Assess this LLM trace according to

## 57450:00 - 57500:00

these rules. And and the rules are just

## 57500:00 - 57550:00

the prompt that I just showed you.

## 57550:00 - 57625:00

and I ask it okay is there a handoff

## 57625:00 - 57670:00

error true or false.

## 57670:00 - 57715:00

So then this column

## 57715:00 - 57770:00

let me just zoom in a bit. Column H I

## 57770:00 - 57845:00

have okay did this error occur in column

## 57845:00 - 57875:00

G is whether I thought the error

## 57875:00 - 57895:00

occurred or not. You can see

## 57895:00 - 57915:00

>> you're going through it manually. You do

## 57915:00 - 57920:00

that.

## 57920:00 - 57945:00

>> Yeah. Yeah. And which we already did. We

## 57945:00 - 57965:00

we already went through it manually. So

## 57965:00 - 57980:00

we don't it's not like we have to do it

## 57980:00 - 58025:00

again because we kind of have that cheat

## 58025:00 - 58055:00

code from the axial coding. We already

## 58055:00 - 58070:00

did it.

## 58070:00 - 58095:00

>> Um you might have to go through it again

## 58095:00 - 58140:00

if you need more data and there's a lot

## 58140:00 - 58170:00

of details to this on like how to do

## 58170:00 - 58210:00

this correctly. Um you want to split

## 58210:00 - 58245:00

your data and do all these things so

## 58245:00 - 58280:00

that you're not cheating but I just want

## 58280:00 - 58325:00

to show you the concept

## 58325:00 - 58365:00

and basically um what you can do is

## 58365:00 - 58415:00

measure the agreement. Now,

## 58415:00 - 58445:00

>> one thing you should know as a product

## 58445:00 - 58510:00

manager is a lot of people go straight

## 58510:00 - 58550:00

to this like agreement. They say, "Okay,

## 58550:00 - 58630:00

my judge agrees with the human

## 58630:00 - 58680:00

at some percentage of the time."

## 58680:00 - 58740:00

Now, that sounds appealing, but it's a

## 58740:00 - 58805:00

very dangerous metric to use because a

## 58805:00 - 58865:00

lot of times errors have um you know,

## 58865:00 - 58905:00

they only happen on the on the long tail

## 58905:00 - 58940:00

and they don't happen as frequently. So,

## 58940:00 - 58985:00

like if you only have the error 10% of

## 58985:00 - 59010:00

the time,

## 59010:00 - 59055:00

then you can easily have 90% agreement

## 59055:00 - 59140:00

by just having a judge say,

## 59140:00 - 59175:00

uh, it passes all the time. Does that

## 59175:00 - 59210:00

make sense? So like 90% agreement might

## 59210:00 - 59230:00

look good on paper but it might be

## 59230:00 - 59245:00

misleading

## 59245:00 - 59270:00

>> and that's rare. It's a rare.

## 59270:00 - 59285:00

>> Yeah.

## 59285:00 - 59330:00

>> So you know as a product manager or

## 59330:00 - 59360:00

someone even if you're not doing this

## 59360:00 - 59400:00

calculation yourself if someone ever

## 59400:00 - 59455:00

reports to you agreement you should

## 59455:00 - 59490:00

immediately ask okay tell me more like

## 59490:00 - 59510:00

you need you know you know need to look

## 59510:00 - 59560:00

into it to give you more intuition. Here

## 59560:00 - 59625:00

is like a matrix okay of this specific

## 59625:00 - 59665:00

judge in the Google sheet. And this is

## 59665:00 - 59705:00

again a pivot table just keeping it dumb

## 59705:00 - 59770:00

and simple is okay on on the uh rows I

## 59770:00 - 59815:00

have what did the human think what did I

## 59815:00 - 59880:00

think did it have an error true or false

## 59880:00 - 59920:00

and then did my judge have an error true

## 59920:00 - 59935:00

or false

## 59935:00 - 59965:00

>> the intuition here is exactly what

## 59965:00 - 60000:00

Hamill said right you need to look at

## 60000:00 - 60060:00

each type of error so when the human

## 60060:00 - 60105:00

said false but the judge said true or

## 60105:00 - 60155:00

vice versa so those non-green diagonal

## 60155:00 - 60210:00

here and if they're too large then go

## 60210:00 - 60245:00

iterate on your prompt make it more

## 60245:00 - 60285:00

clear to the LLM judge so that you can

## 60285:00 - 60325:00

reduce that misalignment you want to get

## 60325:00 - 60355:00

to a point where most you're going to

## 60355:00 - 60400:00

have some misalignment that's okay we

## 60400:00 - 60435:00

talk about in our course also how to

## 60435:00 - 60475:00

code correct that misalignment but in

## 60475:00 - 60520:00

this stage if you're a product manager

## 60520:00 - 60555:00

and the person who's building the LLM

## 60555:00 - 60625:00

judge eval has not done this they're

## 60625:00 - 60665:00

saying like oh it agrees these 75% of

## 60665:00 - 60700:00

the time we're good. They don't like

## 60700:00 - 60725:00

have this matrix and they haven't

## 60725:00 - 60765:00

iterated to make sure that these two

## 60765:00 - 60805:00

types of errors have gone down to zero,

## 60805:00 - 60840:00

then it's a bad smell. Go and ask them

## 60840:00 - 60865:00

to go fix that.

## 60865:00 - 60905:00

>> Awesome. That's a really good tip is is

## 60905:00 - 60925:00

what to look for when someone's doing

## 60925:00 - 60935:00

this wrong.

## 60935:00 - 60945:00

>> Yeah.

## 60945:00 - 60970:00

>> Actually, could you take us back to the

## 60970:00 - 61025:00

LLM as judge prompt? I just want to

## 61025:00 - 61050:00

highlight something really interesting

## 61050:00 - 61080:00

here. I've had some guests on the

## 61080:00 - 61110:00

podcast recently who've been saying eval

## 61110:00 - 61145:00

are the new PRDS. And if you look at

## 61145:00 - 61205:00

this, this is exactly what this is. Like

## 61205:00 - 61230:00

product managers, product teams, right?

## 61230:00 - 61250:00

Here's what the product should be.

## 61250:00 - 61275:00

Here's all the requirements. Here's like

## 61275:00 - 61300:00

the how it should work. They built the

## 61300:00 - 61330:00

thing. And then they test it manually

## 61330:00 - 61365:00

often. What's cool about this is this is

## 61365:00 - 61400:00

exactly that same thing. And it's

## 61400:00 - 61425:00

running constantly. It's telling you

## 61425:00 - 61460:00

here's how this agent should respond in

## 61460:00 - 61490:00

very specific ways. If it's this, this,

## 61490:00 - 61510:00

this is, do that. If it's this, this is

## 61510:00 - 61545:00

that, do that. And so it's exactly what

## 61545:00 - 61575:00

I've been hearing again and again. You

## 61575:00 - 61620:00

could see right here. This is like the

## 61620:00 - 61645:00

purest sense of what a product

## 61645:00 - 61685:00

requirements document should be is this

## 61685:00 - 61720:00

eval judge that's telling you exactly

## 61720:00 - 61745:00

what it should be and it's automatic and

## 61745:00 - 61760:00

running constantly.

## 61760:00 - 61795:00

>> Yeah, absolutely. And it's kind of

## 61795:00 - 61825:00

derived from our own data. So of course

## 61825:00 - 61855:00

it's a product manager's expectations.

## 61855:00 - 61895:00

What I find a lot of people miss is they

## 61895:00 - 61930:00

just put in what their expectations are

## 61930:00 - 61970:00

before looking at their data. But as we

## 61970:00 - 62000:00

look at our data, we uncover more

## 62000:00 - 62030:00

expectations that we couldn't have

## 62030:00 - 62055:00

dreamed up in the first place. And that

## 62055:00 - 62095:00

ends up going into this prompt. So that

## 62095:00 - 62125:00

is interesting. So it's not so your

## 62125:00 - 62185:00

advice is not skip straight to evals and

## 62185:00 - 62220:00

LLM as judge prompts before you build

## 62220:00 - 62275:00

the product. Still write traditional one

## 62275:00 - 62305:00

pagers P prds to tell your team what

## 62305:00 - 62325:00

we're doing, why we're doing it, what

## 62325:00 - 62365:00

success looks like, but then at the end

## 62365:00 - 62395:00

you could probably pull from that and

## 62395:00 - 62420:00

even improve that original PRD if you're

## 62420:00 - 62455:00

evolving the product uh using this

## 62455:00 - 62460:00

process.

## 62460:00 - 62490:00

>> I would go even further to say you're

## 62490:00 - 62530:00

going to improve. It's going to change.

## 62530:00 - 62565:00

You're never going to know what the

## 62565:00 - 62600:00

failure modes are going to be upfront

## 62600:00 - 62655:00

and you're always going to uncover new,

## 62655:00 - 62710:00

you know, vibes that you think that your

## 62710:00 - 62730:00

product should have, right? You don't

## 62730:00 - 62755:00

really know what you want until you see

## 62755:00 - 62805:00

it with these LLMs. So, you've got, you

## 62805:00 - 62835:00

got to be kind of flexible, have to look

## 62835:00 - 62880:00

at your data, have to PRDs are a great

## 62880:00 - 62920:00

abstraction for thinking about this, but

## 62920:00 - 62950:00

it's not the end all be all. It's going

## 62950:00 - 62975:00

to change.

## 62975:00 - 63010:00

>> I love that. And Haml's pulling up some

## 63010:00 - 63055:00

cool research report. What's this about?

## 63055:00 - 63085:00

>> Oh, this is one of the coolest research

## 63085:00 - 63130:00

reports you can possibly read if you

## 63130:00 - 63175:00

want to know about evals. So, it was

## 63175:00 - 63215:00

authored by someone named Shrea Shankar.

## 63215:00 - 63255:00

>> Oh my god.

## 63255:00 - 63305:00

>> And her collaborators and so it's called

## 63305:00 - 63330:00

who validates the validator.

## 63330:00 - 63360:00

>> That is the best name for a research

## 63360:00 - 63380:00

I've ever heard. That's so good.

## 63380:00 - 63395:00

>> Thank you.

## 63395:00 - 63435:00

>> So I I should let Treya talk about this.

## 63435:00 - 63480:00

I think the one of the most important

## 63480:00 - 63505:00

things to pay attention in this paper

## 63505:00 - 63545:00

are the criteria drift.

## 63545:00 - 63550:00

>> Yeah.

## 63550:00 - 63580:00

>> And what she found.

## 63580:00 - 63625:00

>> So we did this super fun study when we

## 63625:00 - 63680:00

were kind of doing user studies with

## 63680:00 - 63725:00

people who were trying to write LLM

## 63725:00 - 63790:00

judges or just validate their own LLM

## 63790:00 - 63840:00

outputs. And we were this was I think

## 63840:00 - 63885:00

this was before evals was like extremely

## 63885:00 - 63920:00

popular I feel like on the internet.

## 63920:00 - 63950:00

This was we did this project like late

## 63950:00 - 64000:00

2023 was when we started it. But then

## 64000:00 - 64030:00

the thing that really was burning in my

## 64030:00 - 64055:00

mind as a researcher is like why is this

## 64055:00 - 64085:00

problem so hard? We've been having

## 64085:00 - 64135:00

machine learning and AI for so long.

## 64135:00 - 64175:00

It's not new. But suddenly this time

## 64175:00 - 64215:00

around everything is really difficult.

## 64215:00 - 64250:00

So we just did this user study with a

## 64250:00 - 64305:00

bunch of developers and we realized okay

## 64305:00 - 64355:00

what's new here is that you can't figure

## 64355:00 - 64405:00

out your rubrics up front. People's

## 64405:00 - 64450:00

opinions of good and bad change as they

## 64450:00 - 64485:00

review more outputs. They think of

## 64485:00 - 64520:00

failure modes only after seeing 10

## 64520:00 - 64555:00

outputs they would never have dreamed of

## 64555:00 - 64575:00

in the first place. And these are

## 64575:00 - 64605:00

experts, right? These are people who

## 64605:00 - 64640:00

have built many LLM pipelines and now

## 64640:00 - 64700:00

agents before and just you can't ever

## 64700:00 - 64735:00

dream up everything in the first place.

## 64735:00 - 64790:00

Um, and I think that's so key in today's

## 64790:00 - 64835:00

world of AI development.

## 64835:00 - 64860:00

>> Okay, that is a really good point. It's

## 64860:00 - 64890:00

very much reinforcing what we were just

## 64890:00 - 64910:00

talking about and that's why H will pull

## 64910:00 - 64945:00

this up is just okay

## 64945:00 - 64970:00

>> behind it.

## 64970:00 - 64995:00

>> Yeah. Okay, great. You still got to do

## 64995:00 - 65020:00

product the same way, but now you have

## 65020:00 - 65050:00

this really powerful tool that make

## 65050:00 - 65085:00

helps you make sure what you've built is

## 65085:00 - 65115:00

correct. Uh it's not going to replace

## 65115:00 - 65140:00

the PR process.

## 65140:00 - 65150:00

>> Cool.

## 65150:00 - 65185:00

>> How many evals of these? How many say I

## 65185:00 - 65215:00

don't know Lanas judge prompts do you

## 65215:00 - 65240:00

end up with usually say I don't know

## 65240:00 - 65265:00

like I know obviously depends complexity

## 65265:00 - 65290:00

of the product but what's like a number

## 65290:00 - 65320:00

in your experience

## 65320:00 - 65375:00

>> for me like between four and seven

## 65375:00 - 65385:00

>> oh that's it

## 65385:00 - 65415:00

>> it's not that many because a lot of the

## 65415:00 - 65445:00

failure modes as Haml said earlier can

## 65445:00 - 65495:00

be fixed by just fixing your prompt you

## 65495:00 - 65520:00

just didn't think to put it in your

## 65520:00 - 65545:00

prompts and now you put it in your you

## 65545:00 - 65570:00

shouldn't do an eval like this for

## 65570:00 - 65620:00

everything just the the pesky ones that

## 65620:00 - 65665:00

um you've described your ideal behavior

## 65665:00 - 65695:00

in your agent prompt, but it's still

## 65695:00 - 65715:00

failing.

## 65715:00 - 65745:00

>> Got it. So, say you found a problem, you

## 65745:00 - 65780:00

fixed it. In traditional software

## 65780:00 - 65805:00

development, you'd write a unit test to

## 65805:00 - 65830:00

make sure it doesn't happen again. Is

## 65830:00 - 65865:00

your insight here is don't even bother

## 65865:00 - 65895:00

writing an eval around that if it's just

## 65895:00 - 65905:00

gone.

## 65905:00 - 65950:00

>> I think you can if you want to, but the

## 65950:00 - 65985:00

whole game here is about prioritizing.

## 65985:00 - 66020:00

You have finite resources and finite

## 66020:00 - 66050:00

time. You can't write an eval for

## 66050:00 - 66080:00

everything. So prioritize the ones that

## 66080:00 - 66120:00

are the more pesky areas

## 66120:00 - 66135:00

>> and probably the ones that are most

## 66135:00 - 66155:00

risky to your business if they say

## 66155:00 - 66235:00

something like Mecca Hitler Grock and

## 66235:00 - 66270:00

>> cool okay so that's that's very uh

## 66270:00 - 66305:00

relieving that this because this is this

## 66305:00 - 66330:00

prompt is like a lot of work to really

## 66330:00 - 66350:00

think through all these details

## 66350:00 - 66390:00

>> but it's a lot of one-time cost right

## 66390:00 - 66430:00

now forever you can run this on your

## 66430:00 - 66455:00

application

## 66455:00 - 66480:00

>> right

## 66480:00 - 66545:00

and I want to say okay data analysis is

## 66545:00 - 66595:00

super powerful is going to drive lots of

## 66595:00 - 66620:00

improvements very quickly to your

## 66620:00 - 66645:00

application. We showed the most basic

## 66645:00 - 66685:00

kind of data analysis which is counting

## 66685:00 - 66720:00

which is accessible to everyone. You can

## 66720:00 - 66775:00

get you know more

## 66775:00 - 66805:00

sophisticated with the data analysis.

## 66805:00 - 66840:00

There's lots of different ways to sample

## 66840:00 - 66875:00

look at data.

## 66875:00 - 66925:00

We kind of made it look easy in a sense,

## 66925:00 - 66975:00

but there's a lot of skills here to do

## 66975:00 - 67035:00

to it well. Um, you know, building an

## 67035:00 - 67075:00

intuition and a nose for how to sort

## 67075:00 - 67115:00

through this data. For example, let's

## 67115:00 - 67155:00

say I find conversational issues, this

## 67155:00 - 67205:00

like conversational flow issues.

## 67205:00 - 67265:00

Maybe if I was trying to chase down this

## 67265:00 - 67320:00

problem further, I would think about

## 67320:00 - 67355:00

ways to find other conversational flows

## 67355:00 - 67400:00

flow issues that I didn't code. You

## 67400:00 - 67430:00

know, I would maybe dig through the data

## 67430:00 - 67485:00

in several ways. Um, and there's, you

## 67485:00 - 67525:00

know, different ways to go about this.

## 67525:00 - 67590:00

It kind of it's very similar, if not

## 67590:00 - 67625:00

almost exactly similar as kind of

## 67625:00 - 67660:00

traditional analytics techniques that

## 67660:00 - 67695:00

you would do on any product. give us

## 67695:00 - 67740:00

just a quick sense of what comes next

## 67740:00 - 67765:00

and then let's talk about the debate

## 67765:00 - 67795:00

around eval.

## 67795:00 - 67830:00

>> So what comes next after you've built

## 67830:00 - 67870:00

your LLM judge? Well, we find that

## 67870:00 - 67905:00

people just try to use that everywhere

## 67905:00 - 67940:00

they can. So they will put the LLM judge

## 67940:00 - 67985:00

in unit tests as you and they will know

## 67985:00 - 68015:00

like oh here are some example traces

## 68015:00 - 68040:00

where we saw that failure because we

## 68040:00 - 68060:00

labeled it. Now we're going to make

## 68060:00 - 68090:00

those part of unit tests and make sure

## 68090:00 - 68125:00

that every time we push a change to our

## 68125:00 - 68170:00

code these tests are going to pass. They

## 68170:00 - 68205:00

also use it for online monitoring.

## 68205:00 - 68245:00

People are making dashboards on this and

## 68245:00 - 68275:00

I think that's incredible. I think like

## 68275:00 - 68305:00

the products that are doing this, right,

## 68305:00 - 68345:00

they have a very sharp sense of how well

## 68345:00 - 68395:00

their application is performing. Um, and

## 68395:00 - 68425:00

people don't talk about it because this

## 68425:00 - 68460:00

is their moat, right? So people are not

## 68460:00 - 68485:00

going to go and share all of these

## 68485:00 - 68515:00

things because makes sense, right? If

## 68515:00 - 68545:00

you are an email writing assistant and

## 68545:00 - 68570:00

you're doing this and you're doing it

## 68570:00 - 68605:00

well, you don't want somebody else to go

## 68605:00 - 68640:00

and build an email writing assistant and

## 68640:00 - 68680:00

then kind of get you out of business.

## 68680:00 - 68705:00

So, I really want to stress the point

## 68705:00 - 68735:00

that it's like try to use these

## 68735:00 - 68770:00

artifacts that you're building wherever

## 68770:00 - 68830:00

possible online repeatedly. Um, use them

## 68830:00 - 68865:00

to drive improvements to your product.

## 68865:00 - 68915:00

Often times Haml and I will kind of will

## 68915:00 - 68950:00

tell people how to do this up to this

## 68950:00 - 68990:00

very point and it clicks for people and

## 68990:00 - 69030:00

then they like never come back again. So

## 69030:00 - 69070:00

either they have I don't know quit their

## 69070:00 - 69095:00

jobs, they're not doing AI development

## 69095:00 - 69150:00

anymore or they know what to do from

## 69150:00 - 69215:00

here on out. Um I think it's the latter

## 69215:00 - 69260:00

but um I think it's very powerful. Like

## 69260:00 - 69300:00

just watching you do this really opened

## 69300:00 - 69330:00

my eyes to what this is and how

## 69330:00 - 69365:00

systematic the process is. I always

## 69365:00 - 69390:00

imagine you just sit on a computer,

## 69390:00 - 69415:00

okay, what are the things I need to make

## 69415:00 - 69455:00

sure work correctly. And what you're

## 69455:00 - 69490:00

showing us here is here's it's a very

## 69490:00 - 69520:00

simple step by step

## 69520:00 - 69540:00

>> based on real things that are happening

## 69540:00 - 69570:00

in your product. How to catch them,

## 69570:00 - 69605:00

identify them, prioritize them, and then

## 69605:00 - 69610:00

>> absolutely

## 69610:00 - 69635:00

>> catch them if they happen again and fix

## 69635:00 - 69645:00

them.

## 69645:00 - 69680:00

>> Yeah, it's it's not magic. Like anyone

## 69680:00 - 69700:00

can do this. you're going to have to

## 69700:00 - 69745:00

practice the skill like any new skill

## 69745:00 - 69790:00

you have to practice but you can do it.

## 69790:00 - 69825:00

Um and I think what's very empowering

## 69825:00 - 69860:00

now is that product managers are doing

## 69860:00 - 69890:00

this and can do this and can really

## 69890:00 - 69940:00

build very very profitable products with

## 69940:00 - 69960:00

this skill set.

## 69960:00 - 70005:00

>> Okay, great segue to a debate that we

## 70005:00 - 70025:00

kind of got pulled into that was

## 70025:00 - 70070:00

happening on on X the other day. Uh I

## 70070:00 - 70115:00

did not realize how much controversy and

## 70115:00 - 70140:00

drama there is around eval. There's a

## 70140:00 - 70175:00

lot of people with very strong opinions.

## 70175:00 - 70225:00

uh Sabat Shrea give us just a sense of

## 70225:00 - 70270:00

the two sides of the debate around the

## 70270:00 - 70305:00

importance and value of Ebells and then

## 70305:00 - 70330:00

give us your perspective.

## 70330:00 - 70385:00

>> Yeah. So all right I'll be a little bit

## 70385:00 - 70415:00

placating and I say I think everyone is

## 70415:00 - 70450:00

on the same side. I think the

## 70450:00 - 70490:00

misconception is that people have very

## 70490:00 - 70545:00

rigid definitions of what eval is. For

## 70545:00 - 70575:00

example, they might think that eval is

## 70575:00 - 70625:00

just unit tests or they might think that

## 70625:00 - 70685:00

eval is just the data analysis part and

## 70685:00 - 70725:00

no online monitoring or any no

## 70725:00 - 70765:00

monitoring of product specific metrics

## 70765:00 - 70815:00

like actually number of chats engaged in

## 70815:00 - 70855:00

or whatnot. Um so I think everyone has a

## 70855:00 - 70895:00

different mindset of evals going in. And

## 70895:00 - 70920:00

the other thing I will say is that

## 70920:00 - 70955:00

people have been burned by evals in the

## 70955:00 - 70995:00

past. So I think people have done evals

## 70995:00 - 71045:00

badly. One concrete example of this is

## 71045:00 - 71080:00

they've tried to do an LLM judge, but it

## 71080:00 - 71125:00

has not aligned with their expectations.

## 71125:00 - 71160:00

They only uncovered this later on and

## 71160:00 - 71195:00

then they didn't trust it anymore. And

## 71195:00 - 71235:00

then they're like, "Oh, I'm anti-EVOS."

## 71235:00 - 71280:00

And I 100% empathize with that because,

## 71280:00 - 71325:00

you know, you should be anti- liker

## 71325:00 - 71370:00

scale LLM judge. I absolutely agree with

## 71370:00 - 71405:00

you. We are anti- that as well. So, a

## 71405:00 - 71440:00

lot of the misconception stems from two

## 71440:00 - 71470:00

things, right? like people having a

## 71470:00 - 71495:00

narrow definition of evals and then

## 71495:00 - 71525:00

people not doing it well and then

## 71525:00 - 71575:00

getting burned and then wanting to avoid

## 71575:00 - 71610:00

other people making that mistake and

## 71610:00 - 71660:00

then unfortunately X or Twitter is like

## 71660:00 - 71700:00

a medium where you know people are

## 71700:00 - 71730:00

misinterpreting what everybody is saying

## 71730:00 - 71775:00

all the time and you just get all these

## 71775:00 - 71810:00

strong opinions of like don't do eval

## 71810:00 - 71860:00

it's bad we tried it it doesn't work

## 71860:00 - 71910:00

we're clawed code or you know whatever

## 71910:00 - 71960:00

other famous product and we don't do

## 71960:00 - 72005:00

evals and there's just so much nuance

## 72005:00 - 72040:00

behind all of it because because a lot

## 72040:00 - 72065:00

of these applications are standing on

## 72065:00 - 72100:00

the shoulders of evals coding agents is

## 72100:00 - 72145:00

a great example of that claude code

## 72145:00 - 72170:00

right they are standing on the shoulders

## 72170:00 - 72205:00

of claude

## 72205:00 - 72240:00

base model not base but the the

## 72240:00 - 72280:00

fine-tuned claude models have been

## 72280:00 - 72340:00

evaluated on many coding benchmarks

## 72340:00 - 72380:00

can't can't argue against that

## 72380:00 - 72410:00

>> and just to double just to make clear

## 72410:00 - 72435:00

exactly what you're talking about where

## 72435:00 - 72460:00

one of the heads I think maybe the head

## 72460:00 - 72490:00

engineer of cloud code went on a podcast

## 72490:00 - 72525:00

and he's like oh we don't do evals we

## 72525:00 - 72555:00

just vibe we just look at vibes and

## 72555:00 - 72590:00

vibes meaning they just use it and feel

## 72590:00 - 72610:00

if it's right or wrong

## 72610:00 - 72655:00

>> and I think that kind of works so

## 72655:00 - 72690:00

there's two things to that right one is

## 72690:00 - 72710:00

they're standing on the shoulders of the

## 72710:00 - 72745:00

evals that their colleagues are doing

## 72745:00 - 72755:00

for coding

## 72755:00 - 72785:00

>> of the cloud foundational model

## 72785:00 - 72810:00

>> absolutely right we know that they

## 72810:00 - 72840:00

report those numbers because we see the

## 72840:00 - 72875:00

benchmarks we know who's doing well on

## 72875:00 - 72915:00

those other thing is they are actually

## 72915:00 - 72955:00

probably very systematic about the error

## 72955:00 - 73010:00

analysis to some extent. I bet you that

## 73010:00 - 73060:00

they are monitoring who is using Claude,

## 73060:00 - 73090:00

how many people are using Claude, how

## 73090:00 - 73125:00

many chats are being created, how long

## 73125:00 - 73160:00

these chats are. They're also probably

## 73160:00 - 73195:00

monitoring in their internal team.

## 73195:00 - 73230:00

They're dog fooding. Anytime something

## 73230:00 - 73270:00

is off, they maybe have a queue or they

## 73270:00 - 73300:00

send it to the person developing claude

## 73300:00 - 73340:00

code and this person is implicitly doing

## 73340:00 - 73370:00

some form of hair error analysis that

## 73370:00 - 73435:00

Hamill talked about. All of this is eval

## 73435:00 - 73465:00

right there's no world in which they are

## 73465:00 - 73500:00

just being like I made cloud code I'm

## 73500:00 - 73540:00

never looking at anything um and

## 73540:00 - 73585:00

unfortunately right when you don't think

## 73585:00 - 73620:00

about that or talk about that I think

## 73620:00 - 73665:00

that the community most of the community

## 73665:00 - 73695:00

is beginners right or people who don't

## 73695:00 - 73725:00

know about evals and want to learn about

## 73725:00 - 73755:00

it um and it sends the wrong message

## 73755:00 - 73780:00

there now I don't know what cloud code

## 73780:00 - 73825:00

is doing obviously um but I would be

## 73825:00 - 73850:00

willing to bet money that they're doing

## 73850:00 - 73885:00

something in the form of evals

## 73885:00 - 73930:00

>> we'll also say that coding agents are

## 73930:00 - 73980:00

fundamentally very different than other

## 73980:00 - 74050:00

AI products because the developer is the

## 74050:00 - 74095:00

domain expert. So you can short circuit

## 74095:00 - 74150:00

a lot of things and also the developer

## 74150:00 - 74190:00

is using it all day long. So there's a

## 74190:00 - 74220:00

type of dog fooding and type of do

## 74220:00 - 74270:00

domain expertise that is you know you

## 74270:00 - 74315:00

can collapse the activities.

## 74315:00 - 74365:00

You don't need as much data. you don't

## 74365:00 - 74400:00

need as much feedback or exploration

## 74400:00 - 74485:00

because you know so your eval process

## 74485:00 - 74525:00

you know should look different

## 74525:00 - 74550:00

>> because you're seeing the code like you

## 74550:00 - 74570:00

see the code it's generating you can

## 74570:00 - 74595:00

tell this is great this is terrible

## 74595:00 - 74630:00

>> yeah yeah and so and so I think a lot of

## 74630:00 - 74665:00

people had generalized coding agents

## 74665:00 - 74705:00

because coding agents are the first AI

## 74705:00 - 74780:00

product released into the wild and I

## 74780:00 - 74805:00

think it's a mistake to try to

## 74805:00 - 74860:00

generalize that at charge.

## 74860:00 - 74905:00

>> The other thing is yeah, engineers have

## 74905:00 - 74950:00

a dog fooding personality. There are

## 74950:00 - 74980:00

plenty of applications where people are

## 74980:00 - 75025:00

trying to build AI in certain domains

## 75025:00 - 75060:00

and and they don't have a dog fooding

## 75060:00 - 75095:00

for like doctors for example are not out

## 75095:00 - 75115:00

there trying to get all the most

## 75115:00 - 75160:00

incorrect advice from AI

## 75160:00 - 75200:00

and be tolerant and receptive to that.

## 75200:00 - 75230:00

So it's very important to keep I think

## 75230:00 - 75270:00

these nuance things in mind. So what I'm

## 75270:00 - 75290:00

hearing from you Shre is interestingly

## 75290:00 - 75365:00

is that if you if humans on the team are

## 75365:00 - 75420:00

doing very close uh data analysis, error

## 75420:00 - 75465:00

analysis, dog fooding you like crazy and

## 75465:00 - 75515:00

essentially they are the human evals and

## 75515:00 - 75545:00

you're describing that as that's within

## 75545:00 - 75575:00

the umbrella of eval. So you could do it

## 75575:00 - 75615:00

that way if you're very if you have time

## 75615:00 - 75645:00

and motivation to do that or you could

## 75645:00 - 75680:00

set these things up to be automatic.

## 75680:00 - 75715:00

>> Absolutely. And it's also about the

## 75715:00 - 75745:00

skills, right? people who work at

## 75745:00 - 75810:00

Anthropic are very very highly skilled.

## 75810:00 - 75860:00

Um they've been trained in data analysis

## 75860:00 - 75895:00

or software engineering or AI and

## 75895:00 - 75915:00

whatnot, right?

## 75915:00 - 75950:00

>> And you know, you can get there. Anyone

## 75950:00 - 75985:00

can get there of course by like learning

## 75985:00 - 76010:00

the concepts, but

## 76010:00 - 76035:00

>> most people don't have that skill right

## 76035:00 - 76050:00

now.

## 76050:00 - 76100:00

>> Do fooding is is a dangerous one only

## 76100:00 - 76145:00

because a lot of people will say they're

## 76145:00 - 76165:00

dog fooding. They're like, "Yeah, we dog

## 76165:00 - 76245:00

fooded." But are they really? And a lot

## 76245:00 - 76280:00

of people aren't really dog fooding it

## 76280:00 - 76330:00

at that visceral level that you would

## 76330:00 - 76365:00

need to to have to close that feedback

## 76365:00 - 76400:00

loop. So that's the only caveat I would

## 76400:00 - 76435:00

add. There's also this kind of feels

## 76435:00 - 76460:00

like straw man argument of eval versus

## 76460:00 - 76485:00

AB tests.

## 76485:00 - 76515:00

>> Talk about your thoughts there because

## 76515:00 - 76540:00

that feels like a big part of this

## 76540:00 - 76560:00

debate people are having like do you

## 76560:00 - 76585:00

need eval if you have AB tests that are

## 76585:00 - 76635:00

testing production level metrics. So AB

## 76635:00 - 76685:00

tests are again another form of eval I

## 76685:00 - 76715:00

imagine right like when you're doing an

## 76715:00 - 76740:00

AB test right you have two different

## 76740:00 - 76770:00

experimental conditions and then you

## 76770:00 - 76800:00

have a metric that quantifies the

## 76800:00 - 76830:00

success of something and you're

## 76830:00 - 76875:00

comparing the metric and again right an

## 76875:00 - 76915:00

eval in our mind is systematic

## 76915:00 - 76970:00

measurement of quality some metric um

## 76970:00 - 77000:00

you can't really do an AV test without

## 77000:00 - 77050:00

the eval to compare um

## 77050:00 - 77085:00

>> so maybe maybe we just have a different

## 77085:00 - 77125:00

weird take on it Yeah. Okay. So, what

## 77125:00 - 77155:00

I'm hearing is like you consider AB test

## 77155:00 - 77180:00

as part of the suite of evals that you

## 77180:00 - 77215:00

do. I think when people think AB test,

## 77215:00 - 77245:00

it's like we're changing something in

## 77245:00 - 77275:00

the product. We're going to see if this

## 77275:00 - 77320:00

improves some metric we care about. Is

## 77320:00 - 77355:00

that is that enough? Why do we need to

## 77355:00 - 77385:00

test every little feature? Like if it's

## 77385:00 - 77410:00

impacting a metric we care about as a

## 77410:00 - 77430:00

business, we have a bunch of AB tests

## 77430:00 - 77460:00

that are just constantly running.

## 77460:00 - 77510:00

>> This is now a great point. Um, so I

## 77510:00 - 77550:00

think a lot of people prematurely do AB

## 77550:00 - 77590:00

tests because you know they've never

## 77590:00 - 77625:00

done any error analysis in the first

## 77625:00 - 77660:00

place. They just have hypothetically

## 77660:00 - 77695:00

come up with their product requirements

## 77695:00 - 77735:00

and they like believe that you know we

## 77735:00 - 77770:00

should test these things. Um, but it

## 77770:00 - 77790:00

turns out right when you get into the

## 77790:00 - 77825:00

data as Haml showed that like the errors

## 77825:00 - 77865:00

that you're seeing are like not what you

## 77865:00 - 77890:00

thought the errors might be. They were

## 77890:00 - 77930:00

these like weird handoff issues or like

## 77930:00 - 77960:00

I don't know like the text message thing

## 77960:00 - 78005:00

was strange. Um, so I would say that

## 78005:00 - 78030:00

like if you're going to do AB tests and

## 78030:00 - 78060:00

they are powered by actual error

## 78060:00 - 78105:00

analysis as we've shown today, then

## 78105:00 - 78155:00

that's great. Go do it. Um, but if

## 78155:00 - 78190:00

you're just going to do them, which we

## 78190:00 - 78225:00

find that people try to do, just want to

## 78225:00 - 78245:00

do them based on like what you

## 78245:00 - 78285:00

hypothetically think is

## 78285:00 - 78330:00

why is important, then I would encourage

## 78330:00 - 78355:00

people to go and like rethink that and

## 78355:00 - 78385:00

kind of ground your hypothesis.

## 78385:00 - 78420:00

>> Do you have thoughts on what stats sig

## 78420:00 - 78445:00

going to do at OpenAI? Is there anything

## 78445:00 - 78465:00

there that's interesting? I'm just like

## 78465:00 - 78490:00

that was a big deal a huge acquisition

## 78490:00 - 78530:00

AB test company people are like oh AB

## 78530:00 - 78575:00

test the future uh thoughts you know

## 78575:00 - 78625:00

just to add to the previous question a

## 78625:00 - 78675:00

little bit is why is there this debate

## 78675:00 - 78725:00

AB testing versus evals I think

## 78725:00 - 78770:00

fundamentally

## 78770:00 - 78795:00

eval

## 78795:00 - 78825:00

is people are trying to wrap their head

## 78825:00 - 78850:00

around

## 78850:00 - 78895:00

what how to improve their applications

## 78895:00 - 78955:00

and fundamentally um you need to do data

## 78955:00 - 78995:00

science you data science is useful in

## 78995:00 - 79035:00

products like looking at data doing data

## 79035:00 - 79070:00

analytics there's many different suite

## 79070:00 - 79110:00

of tools and um you don't need to invent

## 79110:00 - 79145:00

anything new sure you don't need like

## 79145:00 - 79170:00

necessarily the whole breath of data

## 79170:00 - 79205:00

science and it looks slightly different

## 79205:00 - 79250:00

just slightly with LLMs

## 79250:00 - 79280:00

um you know you might your tactics might

## 79280:00 - 79340:00

be different and so really what it is is

## 79340:00 - 79415:00

like using analytic tools uh to

## 79415:00 - 79450:00

understand your product Now people say

## 79450:00 - 79480:00

the word eval is trying to kind of like

## 79480:00 - 79530:00

carve out this new thing and saying oh

## 79530:00 - 79580:00

eval and in AB testing but if you zoom

## 79580:00 - 79620:00

out it's it's the same data science as

## 79620:00 - 79645:00

before and I think that's what's causing

## 79645:00 - 79690:00

the confusion is hey we need data

## 79690:00 - 79730:00

science thinking and AI product just you

## 79730:00 - 79755:00

know is helpful to have that thinking in

## 79755:00 - 79800:00

AI products like it is in any product uh

## 79800:00 - 79840:00

is my take on that. So yeah, that's a

## 79840:00 - 79855:00

really good take. Like I think just the

## 79855:00 - 79885:00

word eval triggers people now.

## 79885:00 - 79910:00

>> And if you just call it we're just doing

## 79910:00 - 79940:00

air analysis using doing data science to

## 79940:00 - 79965:00

understand where our problem break our

## 79965:00 - 79990:00

product breaks and just setting up tests

## 79990:00 - 80005:00

to make sure we know

## 80005:00 - 80055:00

>> that's boring. It sounds boring.

## 80055:00 - 80085:00

>> No, no, no. We need a mysterious term

## 80085:00 - 80145:00

like evals to to really get the momentum

## 80145:00 - 80190:00

going. Your question about stats. Um I

## 80190:00 - 80225:00

think it's very exciting to be honest. I

## 80225:00 - 80255:00

don't know much about it because, you

## 80255:00 - 80280:00

know, I just imagine that they're this

## 80280:00 - 80315:00

company that many there's a tool that

## 80315:00 - 80355:00

many people use and maybe it just so

## 80355:00 - 80395:00

happened that OpenAI acquired them. I'm

## 80395:00 - 80415:00

sure they've been using them in the

## 80415:00 - 80470:00

past. Um, I'm sure OpenAI's competitors

## 80470:00 - 80500:00

>> are using Stat Sig as well.

## 80500:00 - 80540:00

>> So maybe there is something strategic in

## 80540:00 - 80570:00

that acquisition. I have no idea. I

## 80570:00 - 80595:00

don't know anything there. But I think

## 80595:00 - 80615:00

those are really the bigger questions

## 80615:00 - 80645:00

for me than you know is this

## 80645:00 - 80685:00

fundamentally changing AV testing or

## 80685:00 - 80730:00

making evals more of a priority. I I

## 80730:00 - 80765:00

think they've always been a priority. I

## 80765:00 - 80790:00

think Open AAI has always been doing

## 80790:00 - 80835:00

some form of them and OpenAI has gone so

## 80835:00 - 80895:00

far like historically speaking as to

## 80895:00 - 80930:00

like go and look at all the Twitter

## 80930:00 - 80970:00

sentiment and try to do some sort of

## 80970:00 - 81015:00

retrospective on that and then tie that

## 81015:00 - 81040:00

back to their products. Like they're

## 81040:00 - 81070:00

certainly they're doing some amount of

## 81070:00 - 81100:00

evals before they ship their new

## 81100:00 - 81125:00

foundation models, but they're going so

## 81125:00 - 81150:00

much beyond and being like, "Okay, let's

## 81150:00 - 81175:00

find all the tweets that are complaining

## 81175:00 - 81195:00

about it, all the Reddit threads that

## 81195:00 - 81225:00

are complaining about it that go try to

## 81225:00 - 81260:00

like figure out what's going on." So, it

## 81260:00 - 81290:00

goes to show that like eval are very,

## 81290:00 - 81325:00

very important. No one has really

## 81325:00 - 81365:00

figured it out yet. People are using all

## 81365:00 - 81405:00

the available sources signal that they

## 81405:00 - 81440:00

can to improve their products. What I

## 81440:00 - 81485:00

will say is I'm really hopeful that it

## 81485:00 - 81550:00

might shift the our creative focus

## 81550:00 - 81605:00

within OpenAI. Hopefully up until now a

## 81605:00 - 81650:00

lot of the big labs understandably

## 81650:00 - 81725:00

focused on general benchmarks like MMLU

## 81725:00 - 81765:00

score, human eval which are very

## 81765:00 - 81815:00

important for foundation models and you

## 81815:00 - 81875:00

know those not very related to product

## 81875:00 - 81900:00

specific evals like the ones we talked

## 81900:00 - 81930:00

about today but like handoff and stuff

## 81930:00 - 81965:00

like that like those you know they tend

## 81965:00 - 82000:00

not to correlate.

## 82000:00 - 82025:00

>> Yeah, they don't correlate with math

## 82025:00 - 82095:00

problem solving. Sorry to say.

## 82095:00 - 82155:00

Exactly. And so um you know if you look

## 82155:00 - 82215:00

at the eval products let's say the ones

## 82215:00 - 82260:00

up until recently that some of the big

## 82260:00 - 82285:00

labs have they don't have error

## 82285:00 - 82325:00

analysis. They have gener a suite of

## 82325:00 - 82375:00

generic tools cosign similarity

## 82375:00 - 82420:00

hallucination score whatever and that

## 82420:00 - 82455:00

doesn't work. It's a good first stab at

## 82455:00 - 82495:00

it. It's okay. you know, at least you're

## 82495:00 - 82515:00

doing something getting people maybe

## 82515:00 - 82530:00

it's like getting people to look at

## 82530:00 - 82600:00

data, but uh eventually what we hope to

## 82600:00 - 82655:00

see is okay some a bit more data science

## 82655:00 - 82715:00

thinking in this like eval process.

## 82715:00 - 82740:00

Hopefully the tools we'll get to

## 82740:00 - 82765:00

>> Haml and I should not be the only two

## 82765:00 - 82790:00

people on the planet that are promoting

## 82790:00 - 82820:00

like a structured way of thinking about

## 82820:00 - 82855:00

application specific evals.

## 82855:00 - 82885:00

>> It's like mindboggling to me. Why are we

## 82885:00 - 82925:00

the only two people doing this? The

## 82925:00 - 82960:00

whole world,

## 82960:00 - 82995:00

what's wrong? Um, so I hope that, you

## 82995:00 - 83025:00

know, we're not the only people and that

## 83025:00 - 83055:00

more people catch on.

## 83055:00 - 83090:00

>> Well, the fact that your course on Maven

## 83090:00 - 83110:00

is the number one highest grossing

## 83110:00 - 83150:00

course on Maven, clearly there's demand

## 83150:00 - 83185:00

and interest and there's more people I

## 83185:00 - 83220:00

think on your side. Interestingly, uh,

## 83220:00 - 83255:00

just an example you've been sharing on

## 83255:00 - 83295:00

Twitter that was I think is informative.

## 83295:00 - 83325:00

Everyone's been saying how Cloud Code

## 83325:00 - 83355:00

doesn't care about eval. They're all

## 83355:00 - 83385:00

about vibes and everyone's like what and

## 83385:00 - 83415:00

they're the best coding agent out there.

## 83415:00 - 83450:00

So clearly this is right. More recently,

## 83450:00 - 83480:00

there's all this talk about codecs, open

## 83480:00 - 83520:00

AI codecs being better and everyone's

## 83520:00 - 83560:00

switching and they're so pro eels.

## 83560:00 - 83570:00

>> I know.

## 83570:00 - 83610:00

>> What? Yeah. So,

## 83610:00 - 83645:00

>> gets me every time. The internet's so

## 83645:00 - 83670:00

inconsistent.

## 83670:00 - 83710:00

My favorite thing was um like yesterday,

## 83710:00 - 83740:00

I believe like a couple of lab mates and

## 83740:00 - 83785:00

I were out getting like dessert or

## 83785:00 - 83830:00

something and somebody said like, "Oh,

## 83830:00 - 83870:00

um do you like Codex or Claude better or

## 83870:00 - 83905:00

whatever?" And the other person said,

## 83905:00 - 83945:00

"Oh, I like Claude." And then someone

## 83945:00 - 83970:00

else said, "But the new version of

## 83970:00 - 84010:00

Codeex is better." And then the first

## 84010:00 - 84040:00

person said, "Oh, but the last I checked

## 84040:00 - 84085:00

was two days ago, so maybe my the

## 84085:00 - 84125:00

thoughts maybe I'm not up to date." And

## 84125:00 - 84150:00

I was like, "Oh my god,

## 84150:00 - 84165:00

>> so true.

## 84165:00 - 84200:00

>> This is the world we live in." Oh my

## 84200:00 - 84215:00

god.

## 84215:00 - 84260:00

>> Okay. So, I want to ask about just top

## 84260:00 - 84290:00

misconceptions people have with Evals

## 84290:00 - 84320:00

and top tips and tricks for being

## 84320:00 - 84360:00

successful. So, maybe just share one or

## 84360:00 - 84390:00

two each of each. So let me just start

## 84390:00 - 84435:00

with misconceptions and maybe I'll go to

## 84435:00 - 84465:00

the Hamill first. Just what are a couple

## 84465:00 - 84490:00

of the most common misconceptions people

## 84490:00 - 84555:00

have with Eval still. The top one is hey

## 84555:00 - 84600:00

I can just buy a tool plug it in and

## 84600:00 - 84645:00

it'll do the eval for you. Why do I have

## 84645:00 - 84690:00

to worry about this? We live in the age

## 84690:00 - 84750:00

of AI. Can't the AI just eval it? That's

## 84750:00 - 84800:00

the most common misconception. And

## 84800:00 - 84835:00

people want that so much that people do

## 84835:00 - 84905:00

sell it, but it doesn't work.

## 84905:00 - 84945:00

So that's the first one. Shoot, we need

## 84945:00 - 84970:00

humans still. Great. I think that's

## 84970:00 - 85000:00

great news.

## 85000:00 - 85060:00

>> The second one that you know I see a lot

## 85060:00 - 85090:00

is

## 85090:00 - 85155:00

hey um just not looking at the data you

## 85155:00 - 85190:00

know. So

## 85190:00 - 85230:00

in my consulting people come to me with

## 85230:00 - 85270:00

problems all the time and the first

## 85270:00 - 85315:00

thing I'll say is let's go look at your

## 85315:00 - 85345:00

traces

## 85345:00 - 85400:00

and you can see the kind of their eyes

## 85400:00 - 85445:00

pop open like what do you mean like yeah

## 85445:00 - 85475:00

let's look at it right now and they're

## 85475:00 - 85520:00

surprised that I am going I'm going to

## 85520:00 - 85575:00

go look at individual traces

## 85575:00 - 85630:00

um and we always it always 100% of the

## 85630:00 - 85680:00

time learn a lot and figure out what the

## 85680:00 - 85735:00

problem is. And so, um, I think people

## 85735:00 - 85765:00

just don't know how powerful looking at

## 85765:00 - 85790:00

the data is like we showed on this

## 85790:00 - 85810:00

podcast.

## 85810:00 - 85840:00

>> I would agree with that.

## 85840:00 - 85865:00

>> Those are the top two. Okay. Is there

## 85865:00 - 85885:00

anything else or those are those are the

## 85885:00 - 85915:00

ones like solve those problems?

## 85915:00 - 85950:00

>> Oh, those are definitely And then I

## 85950:00 - 85995:00

guess the one I would add is there's no

## 85995:00 - 86040:00

one correct way to do evals. There are

## 86040:00 - 86100:00

many incorrect ways of doing evals,

## 86100:00 - 86140:00

but there are also many correct ways of

## 86140:00 - 86175:00

doing it. And you got to think about

## 86175:00 - 86215:00

where you are at with your product, how

## 86215:00 - 86275:00

many how much resources you have, um,

## 86275:00 - 86310:00

and figure out the plan that works best

## 86310:00 - 86340:00

for you. It'll always involve some form

## 86340:00 - 86375:00

of error analysis as we showed today,

## 86375:00 - 86430:00

but how you operationalize those metrics

## 86430:00 - 86455:00

is going to change based on where you're

## 86455:00 - 86470:00

at.

## 86470:00 - 86505:00

>> Amazing. Okay. What are a couple just

## 86505:00 - 86530:00

tips and tricks you want to leave people

## 86530:00 - 86570:00

with as they start on their eval journey

## 86570:00 - 86600:00

or just try to get better at something

## 86600:00 - 86615:00

they're already doing?

## 86615:00 - 86685:00

>> So tip number one is just don't be

## 86685:00 - 86750:00

alarmed or don't you know be scared of

## 86750:00 - 86795:00

looking at your data. The process we try

## 86795:00 - 86830:00

to make it as structured as possible.

## 86830:00 - 86860:00

There are inevitably you know questions

## 86860:00 - 86890:00

that are going to come up. That's

## 86890:00 - 86935:00

totally fine. You might feel like you're

## 86935:00 - 86980:00

not doing it perfectly. That's also

## 86980:00 - 87020:00

fine. The goal is not to do eval

## 87020:00 - 87060:00

perfectly. It's to actionably improve

## 87060:00 - 87090:00

your product. And we guarantee you no

## 87090:00 - 87130:00

matter what you do, you're doing parts

## 87130:00 - 87150:00

of these process. You're going to find

## 87150:00 - 87185:00

ways of actionable improvement. And then

## 87185:00 - 87205:00

you're going to iterate on your own

## 87205:00 - 87245:00

process from there. The other tip that I

## 87245:00 - 87315:00

would say is we're very pro- AI. Use LLM

## 87315:00 - 87360:00

to help you organize any thoughts that

## 87360:00 - 87400:00

you have throughout this entire process.

## 87400:00 - 87435:00

So this could be everything ranging from

## 87435:00 - 87470:00

like initial product requirements,

## 87470:00 - 87520:00

right? Figure out how to organize them

## 87520:00 - 87555:00

uh for yourself, figure out how to

## 87555:00 - 87595:00

improve on that product requirements doc

## 87595:00 - 87625:00

based on the open codes that you've

## 87625:00 - 87660:00

created, right? Like don't be afraid to

## 87660:00 - 87700:00

use AI in ways that you know present

## 87700:00 - 87735:00

information better for you.

## 87735:00 - 87785:00

>> Sweet. So don't be scared. Uh use LMS as

## 87785:00 - 87810:00

much as you can throughout the process,

## 87810:00 - 87850:00

>> but not to replace yourself.

## 87850:00 - 87905:00

>> Right. Okay. Great. Still jobs. Great.

## 87905:00 - 87920:00

Hello.

## 87920:00 - 87950:00

>> Yeah, let me actually share my screen.

## 87950:00 - 87985:00

So, when I show something,

## 87985:00 - 88050:00

>> so to piggyback off what Treya said is

## 88050:00 - 88105:00

if you heard any phrase in this podcast,

## 88105:00 - 88140:00

you've probably heard look at your data

## 88140:00 - 88185:00

more than anything else. And so, it's so

## 88185:00 - 88230:00

important that we teach that you should

## 88230:00 - 88285:00

create your own tools to make it as easy

## 88285:00 - 88315:00

as possible. So, I showed you some tools

## 88315:00 - 88335:00

when we're going through the live

## 88335:00 - 88380:00

example of like how to annotate data.

## 88380:00 - 88440:00

Most of the people I work with, they

## 88440:00 - 88490:00

realize how important this is and they

## 88490:00 - 88540:00

vibe code their own tools or they we

## 88540:00 - 88570:00

shouldn't say vibe code. We they just

## 88570:00 - 88605:00

they make their own tools and it's it's

## 88605:00 - 88650:00

cheaper than ever before because you

## 88650:00 - 88685:00

have AI that can help you and AI is

## 88685:00 - 88715:00

really good at creating simple web

## 88715:00 - 88765:00

applications that can show you data that

## 88765:00 - 88795:00

have, you know, that can write to a

## 88795:00 - 88830:00

database. It's very simple. And so for

## 88830:00 - 88880:00

the nurture boss use case, we wanted to

## 88880:00 - 88940:00

remove all the friction of looking at

## 88940:00 - 88980:00

data. And so what you see here is just

## 88980:00 - 89030:00

some screenshots of

## 89030:00 - 89070:00

uh what the application that they

## 89070:00 - 89110:00

created looks like. It's just okay. They

## 89110:00 - 89135:00

have the different channels, voice,

## 89135:00 - 89180:00

email, text. Um they have the different

## 89180:00 - 89220:00

threads. They hid the system prompt by

## 89220:00 - 89250:00

default. Little quality of life

## 89250:00 - 89290:00

improvements. And then they al actually

## 89290:00 - 89335:00

had this axial coding part here where

## 89335:00 - 89375:00

you can see okay in red the count of

## 89375:00 - 89405:00

different errors. They automated that

## 89405:00 - 89455:00

part in a nice way and they just they

## 89455:00 - 89510:00

created this within a few hours. Um and

## 89510:00 - 89555:00

so it's really hard to have a

## 89555:00 - 89580:00

one-sizefits-all thing for looking at

## 89580:00 - 89620:00

your data. You don't have to go here

## 89620:00 - 89645:00

immediately,

## 89645:00 - 89685:00

but something to think about is make it

## 89685:00 - 89720:00

as easy as possible because again, it's

## 89720:00 - 89775:00

the most powerful activity that you can

## 89775:00 - 89815:00

engage in. It's the highest ROI activity

## 89815:00 - 89870:00

you can engage in. And so, um, you know,

## 89870:00 - 89915:00

with AI, yeah, just remove all the

## 89915:00 - 89955:00

friction. That's amazing. And again, I

## 89955:00 - 89985:00

think the ROI piece is so important. We

## 89985:00 - 90020:00

haven't even touched on this enough. The

## 90020:00 - 90045:00

goal here is to make your product

## 90045:00 - 90085:00

better, which will make your business

## 90085:00 - 90115:00

more successful. Like this isn't just a

## 90115:00 - 90145:00

little exercise to catch bugs and things

## 90145:00 - 90175:00

like that. Like this is the way to make

## 90175:00 - 90205:00

AI products better because the

## 90205:00 - 90245:00

experience is how users interact with

## 90245:00 - 90295:00

your AI. Absolutely. If any, you know,

## 90295:00 - 90320:00

we teach our students, hey, when you're

## 90320:00 - 90350:00

doing these evals, if you see something

## 90350:00 - 90400:00

that's wrong, just go fix it. Like the

## 90400:00 - 90450:00

whole point is not to have eval suite

## 90450:00 - 90490:00

where you can point at edit it and say

## 90490:00 - 90525:00

oh look at my evals no just fix your

## 90525:00 - 90565:00

application make it better do you know

## 90565:00 - 90620:00

if it's obvious do it so totally agree

## 90620:00 - 90660:00

with you amazing how long a question I

## 90660:00 - 90680:00

ask but this is I think something people

## 90680:00 - 90705:00

are thinking about how long do you spend

## 90705:00 - 90730:00

on this like how long does it usually

## 90730:00 - 90755:00

take to do the first time

## 90755:00 - 90790:00

>> I can answer for myself for applications

## 90790:00 - 90820:00

that I work with usually I'll spend

## 90820:00 - 90865:00

three to four days really working with

## 90865:00 - 90890:00

whoever to do initial rounds of error

## 90890:00 - 90935:00

analysis, like a lot of labeling, feel

## 90935:00 - 90965:00

like we're in a good place to create the

## 90965:00 - 90990:00

spreadsheet that Hamill had and

## 90990:00 - 91025:00

everyone's kind of on board and

## 91025:00 - 91065:00

convinced and even like a few LLM judge

## 91065:00 - 91100:00

evaluators. Um, but this is a onetime

## 91100:00 - 91140:00

cost. Once I figured out how to

## 91140:00 - 91175:00

integrate that in unit tests or I have

## 91175:00 - 91205:00

like a script that automatically runs it

## 91205:00 - 91235:00

on samples and I will create a cron job

## 91235:00 - 91270:00

to just do this every week. I would say

## 91270:00 - 91315:00

it's like I don't know I find myself

## 91315:00 - 91350:00

probably spending more time looking at

## 91350:00 - 91375:00

data because I'm just data hungry like

## 91375:00 - 91405:00

that. I'm so curious. I'm like I've

## 91405:00 - 91460:00

gained so much from this process and

## 91460:00 - 91500:00

it's like put me above and beyond in any

## 91500:00 - 91540:00

of my you know collaborations with

## 91540:00 - 91590:00

folks. So, I want to keep doing it, but

## 91590:00 - 91645:00

I don't have to. I would say like maybe

## 91645:00 - 91685:00

30 minutes a week after that.

## 91685:00 - 91725:00

>> So, it's a week essentially, a week

## 91725:00 - 91745:00

essentially up front and then like 30

## 91745:00 - 91775:00

minutes to keep improving and adding to

## 91775:00 - 91785:00

your suite.

## 91785:00 - 91815:00

>> Yeah, it's really not that much time. I

## 91815:00 - 91845:00

think people just get overwhelmed by how

## 91845:00 - 91870:00

much time they spend up front and then

## 91870:00 - 91905:00

thinking that they have to keep doing

## 91905:00 - 91930:00

this all the time.

## 91930:00 - 91985:00

>> Amazing. Is there anything else that you

## 91985:00 - 92015:00

wanted to share or leave listeners with?

## 92015:00 - 92035:00

Anything else you want to kind of double

## 92035:00 - 92070:00

down on as a point before we get to our

## 92070:00 - 92105:00

very exciting lightning round? So I

## 92105:00 - 92160:00

would say this process is a lot of fun

## 92160:00 - 92205:00

actually. So it can it's like okay

## 92205:00 - 92230:00

you're looking at data. Oh it sounds

## 92230:00 - 92275:00

like you're annotating things. Okay

## 92275:00 - 92315:00

actually like so I was just looking at a

## 92315:00 - 92355:00

client's data yesterday. The same exact

## 92355:00 - 92405:00

process. It's a application that sends

## 92405:00 - 92470:00

emails recruiting emails to try to get

## 92470:00 - 92535:00

candidates to apply for a job. and

## 92535:00 - 92565:00

we decided to start looking at traces.

## 92565:00 - 92590:00

Jump right into it. Hey, let's look at

## 92590:00 - 92650:00

your traces. The we looked at a trace.

## 92650:00 - 92690:00

The first thing I saw was

## 92690:00 - 92750:00

this like email that is worded like

## 92750:00 - 92790:00

given your background blah blah blah

## 92790:00 - 92825:00

blah blah. So I asked the person right

## 92825:00 - 92850:00

away and this is where putting your

## 92850:00 - 92900:00

product hat on and just being critical

## 92900:00 - 92925:00

and this is where the fun part is. I

## 92925:00 - 92950:00

said, you know what, I hate this email.

## 92950:00 - 92980:00

like do you like the email given your

## 92980:00 - 93010:00

background when and when when I receive

## 93010:00 - 93050:00

a message given your background I just

## 93050:00 - 93085:00

delete that. So I'm like what is this

## 93085:00 - 93120:00

given your background with machine

## 93120:00 - 93150:00

learning and blah blah I'm like this is

## 93150:00 - 93185:00

a generic thing like so I asked the

## 93185:00 - 93230:00

person like hey you know can we do

## 93230:00 - 93255:00

better than this like this is kind of

## 93255:00 - 93310:00

like a this is like a sounds like

## 93310:00 - 93350:00

generic recruiting and they're like oh

## 93350:00 - 93410:00

yeah maybe yeah like it's the AI because

## 93410:00 - 93430:00

they were like they were proud of it

## 93430:00 - 93450:00

like the AI is doing the right thing is

## 93450:00 - 93470:00

sending this email with the right

## 93470:00 - 93500:00

information with the right link with the

## 93500:00 - 93535:00

right name everything and so that's

## 93535:00 - 93570:00

where the fun part is is like put your

## 93570:00 - 93630:00

product hat on and get into like is this

## 93630:00 - 93655:00

really good? Something I want to make

## 93655:00 - 93680:00

sure we cover before we get to a very

## 93680:00 - 93715:00

exciting light round is this is just

## 93715:00 - 93745:00

scratching the surface of all the things

## 93745:00 - 93785:00

you need to know to do this well. Uh I

## 93785:00 - 93825:00

think this is the best primer I've ever

## 93825:00 - 93860:00

seen on how to do this well. Nice.

## 93860:00 - 93910:00

>> But you I think we did it. But you guys

## 93910:00 - 93940:00

teach a course that goes much much

## 93940:00 - 93960:00

deeper for people that really want to

## 93960:00 - 93990:00

get good at this and take this really

## 93990:00 - 94040:00

seriously. share what else you teach in

## 94040:00 - 94060:00

the course that we didn't cover and what

## 94060:00 - 94090:00

else you get as a student being part of

## 94090:00 - 94115:00

the the course you teach at Maven.

## 94115:00 - 94140:00

>> Yeah, I can talk about the syllabus a

## 94140:00 - 94160:00

little bit and then Haml can talk about

## 94160:00 - 94210:00

all the perks. Um, so we go through a

## 94210:00 - 94250:00

life cycle of error analysis, then

## 94250:00 - 94290:00

automated evaluators, then how to

## 94290:00 - 94320:00

improve your application, like how do

## 94320:00 - 94355:00

you create that flywheel for yourself.

## 94355:00 - 94400:00

We also have a few special topics that

## 94400:00 - 94435:00

we find like pretty much no one has ever

## 94435:00 - 94460:00

heard of or taught before, which is

## 94460:00 - 94495:00

exciting. One is how do you build your

## 94495:00 - 94550:00

own interfaces for error analysis. So we

## 94550:00 - 94600:00

kind of go through actual interfaces

## 94600:00 - 94640:00

that we've built and we also live code

## 94640:00 - 94690:00

them on the spot for new data. Um and we

## 94690:00 - 94725:00

show kind of how we use cloud code

## 94725:00 - 94765:00

cursor or whatever we're feeling in the

## 94765:00 - 94795:00

moment that day to build these

## 94795:00 - 94835:00

interfaces. Um and we also talk about

## 94835:00 - 94875:00

kind of broadly cost optimization as

## 94875:00 - 94915:00

well. So, we a couple of people that

## 94915:00 - 94955:00

I've worked with um they got to a point

## 94955:00 - 94980:00

where their evals are very good, their

## 94980:00 - 95015:00

product is very good, but it's all very

## 95015:00 - 95045:00

expensive because they're using like

## 95045:00 - 95085:00

state-of-the-art models. So, how can we

## 95085:00 - 95130:00

kind of replace certain uses of the most

## 95130:00 - 95190:00

expensive GPT5 models with, you know, 5

## 95190:00 - 95250:00

nano, 4 mini, whatnot, and save a lot of

## 95250:00 - 95275:00

money but still maintain the same

## 95275:00 - 95310:00

quality. So, we also give some tips for

## 95310:00 - 95355:00

that. Um, Haml, you want We also have

## 95355:00 - 95385:00

many perks.

## 95385:00 - 95405:00

>> Yeah. Talk about the perks.

## 95405:00 - 95435:00

>> Okay. The perks.

## 95435:00 - 95490:00

>> So, my favorite perk is there's a60page

## 95490:00 - 95530:00

book that's meticulously written that

## 95530:00 - 95570:00

we've created that walks through the

## 95570:00 - 95610:00

entire process in detail of how to do

## 95610:00 - 95655:00

evalu.

## 95655:00 - 95700:00

So, you don't have to sit there and take

## 95700:00 - 95745:00

all these notes. We've done all the hard

## 95745:00 - 95795:00

work for you and we've like documented

## 95795:00 - 95825:00

it in detail.

## 95825:00 - 95885:00

um you know and organize things. So that

## 95885:00 - 95915:00

is really useful. Another really

## 95915:00 - 95950:00

interesting thing and something that I

## 95950:00 - 96015:00

got the idea from you Lenny is okay this

## 96015:00 - 96050:00

is an AI course.

## 96050:00 - 96080:00

Education shouldn't be this thing where

## 96080:00 - 96140:00

you you're only watching lectures and

## 96140:00 - 96180:00

doing homework assignments. So students

## 96180:00 - 96220:00

should have access to an AI that also

## 96220:00 - 96270:00

helps them. So what we've done is we've

## 96270:00 - 96300:00

uh you know just like there's the

## 96300:00 - 96340:00

Lennybot that you have

## 96340:00 - 96370:00

>> yeah lennybot.com

## 96370:00 - 96425:00

uh we have made the same thing with the

## 96425:00 - 96470:00

same software that you're using and we

## 96470:00 - 96495:00

have put everything we've ever said

## 96495:00 - 96530:00

about eval into that. So, every single

## 96530:00 - 96570:00

lesson, every office hours, every

## 96570:00 - 96625:00

Discord chat, any blogs, papers,

## 96625:00 - 96670:00

anything that we've ever said publicly

## 96670:00 - 96710:00

and within our course, we've put it in

## 96710:00 - 96765:00

there and we've tested it with um a

## 96765:00 - 96800:00

bunch of students and they've said it's

## 96800:00 - 96845:00

helpful. Um so, we're giving all

## 96845:00 - 96890:00

students 10 months free unlimited access

## 96890:00 - 96940:00

to that alongside the course.

## 96940:00 - 96980:00

>> Amazing. And then you'll charge for that

## 96980:00 - 97015:00

later down the road is the idea. I just

## 97015:00 - 97040:00

take one month at a time. I don't know

## 97040:00 - 97050:00

what we're doing.

## 97050:00 - 97070:00

>> Eight months and then we'll have to

## 97070:00 - 97100:00

figure it out. I was thinking we should

## 97100:00 - 97120:00

have this whole interview should have

## 97120:00 - 97140:00

just been our bots talking to each

## 97140:00 - 97150:00

other.

## 97150:00 - 97195:00

>> That's amazing. I I would watch that

## 97195:00 - 97225:00

only for like 10 minutes then I don't

## 97225:00 - 97245:00

know what they're talking about.

## 97245:00 - 97275:00

>> Yeah, maybe maybe 30 seconds. Did you

## 97275:00 - 97295:00

guys train it on the voice mode by the

## 97295:00 - 97320:00

way? That's my favorite feature of this

## 97320:00 - 97360:00

of Deli's product. If not, you should do

## 97360:00 - 97370:00

that.

## 97370:00 - 97380:00

>> Oh,

## 97380:00 - 97425:00

>> I think I'm I can't remember. Um I

## 97425:00 - 97450:00

should I should look at it. Definitely

## 97450:00 - 97465:00

sure. Now that we have this podcast

## 97465:00 - 97500:00

episode, you could use this uh content

## 97500:00 - 97530:00

to train it. It's 11 laps powered. It's

## 97530:00 - 97565:00

so good. Uh okay. So that's how do they

## 97565:00 - 97590:00

get to I guess that's okay. They get to

## 97590:00 - 97630:00

that once they become a uh they enter

## 97630:00 - 97645:00

your course. So there's no

## 97645:00 - 97675:00

>> sign up for the course and then you'll

## 97675:00 - 97700:00

get a bunch of emails. Everything will

## 97700:00 - 97725:00

be clear hopefully.

## 97725:00 - 97765:00

>> Amazing. Okay. We also have a discord

## 97765:00 - 97795:00

>> of all the students who have ever taken

## 97795:00 - 97845:00

the class and that discord is so active

## 97845:00 - 97895:00

>> I I can't go on vacation without getting

## 97895:00 - 97925:00

notified on the plane or

## 97925:00 - 97960:00

>> bitter sweet bittersweet. Incredible.

## 97960:00 - 98000:00

Okay. Uh with that we've reached our

## 98000:00 - 98030:00

very exciting lightning round. I've got

## 98030:00 - 98070:00

five questions for you. Are you ready?

## 98070:00 - 98090:00

>> Yes. Let's go.

## 98090:00 - 98110:00

>> Let's do it. Okay. So, I'm going to

## 98110:00 - 98145:00

bounce between you two. Share something

## 98145:00 - 98180:00

if you want. You can pass if you want.

## 98180:00 - 98225:00

First question. Shrea. What are two or

## 98225:00 - 98260:00

three books that you find yourself

## 98260:00 - 98285:00

recommending most to other people?

## 98285:00 - 98315:00

>> So I like to recommend a fiction book

## 98315:00 - 98360:00

because life is about more than eval. So

## 98360:00 - 98395:00

recently I

## 98395:00 - 98475:00

read Pachenko by uh Ninjan Lee uh really

## 98475:00 - 98540:00

great book and then I also am currently

## 98540:00 - 98595:00

reading Apple in China which the name of

## 98595:00 - 98630:00

the author is slipping my mind but this

## 98630:00 - 98660:00

is kind of more of an exposition written

## 98660:00 - 98700:00

by a journalist on how Apple did a lot

## 98700:00 - 98745:00

of manufacturing processes in Asia over

## 98745:00 - 98805:00

the last um couple several decades. Very

## 98805:00 - 98815:00

eye opening.

## 98815:00 - 98860:00

>> Amazing. Haml.

## 98860:00 - 98910:00

>> Yeah, I have them right here. Uh, so the

## 98910:00 - 98955:00

so I'm a nerd. Okay, so I'm not as cool

## 98955:00 - 98990:00

as RA is. So I actually have like

## 98990:00 - 99030:00

textbooks which are like my favorite. So

## 99030:00 - 99080:00

this one is very classic one. Machine

## 99080:00 - 99115:00

learning by Mitchell. Now, it's kind of

## 99115:00 - 99140:00

theoretical, but the thing I like about

## 99140:00 - 99200:00

it is it um really drives home the fact

## 99200:00 - 99285:00

that AAM's razor is prevalent not only

## 99285:00 - 99345:00

in like science but also in machine

## 99345:00 - 99380:00

learning and AI. So, a lot of times the

## 99380:00 - 99415:00

simplest and also engineering. So like a

## 99415:00 - 99450:00

lot of times the simpler approach

## 99450:00 - 99495:00

generalizes better. And so that's the

## 99495:00 - 99525:00

thing I kind of internalized deeply from

## 99525:00 - 99565:00

that book. And um also really like this

## 99565:00 - 99590:00

one. So another textbook. I told you I'm

## 99590:00 - 99625:00

a nerd. This is like also an very old

## 99625:00 - 99645:00

one.

## 99645:00 - 99655:00

>> Wow.

## 99655:00 - 99690:00

>> Um, and this is like, you know, nor

## 99690:00 - 99725:00

algorithms and it's just like I really

## 99725:00 - 99750:00

like it because it's just human

## 99750:00 - 99795:00

ingenuity and it's very like lots of

## 99795:00 - 99815:00

clever useful things.

## 99815:00 - 99830:00

>> They're down the street.

## 99830:00 - 99850:00

>> Computing.

## 99850:00 - 99895:00

>> I'm at Berkeley.

## 99895:00 - 99925:00

>> The people that did that research.

## 99925:00 - 99950:00

>> Yeah.

## 99950:00 - 99970:00

>> Yeah. Textbook authors.

## 99970:00 - 100015:00

>> Super cool. Oh, man. Nerds. I love it.

## 100015:00 - 100050:00

Okay, next question. Favorite recent

## 100050:00 - 100080:00

movie or TV show? I'll jump to Haml

## 100080:00 - 100100:00

first.

## 100100:00 - 100145:00

Okay. So, I'm a dad of two parents. I

## 100145:00 - 100150:00

have two parents.

## 100150:00 - 100205:00

>> I don't get to Oh, sorry. Uh, two kids.

## 100205:00 - 100255:00

So, yeah, I'm a dad of two kids

## 100255:00 - 100310:00

>> and I don't really get the time to watch

## 100310:00 - 100355:00

any TV or movies. So, I watch whatever

## 100355:00 - 100380:00

my kids are watching. So, I've watched

## 100380:00 - 100415:00

Frozen like three times in the last

## 100415:00 - 100420:00

week.

## 100420:00 - 100445:00

>> Only three? Oh, okay. In the last week.

## 100445:00 - 100490:00

Okay. Yeah. So, that's

## 100490:00 - 100525:00

>> great. That's my Frozen. I love it.

## 100525:00 - 100545:00

Okay. Sure. Yeah.

## 100545:00 - 100580:00

>> Yeah. I don't have kids so I can give

## 100580:00 - 100620:00

all these amazing answers actually. So

## 100620:00 - 100645:00

my husband and I have been watching The

## 100645:00 - 100695:00

Wire recently. We never actually saw it

## 100695:00 - 100745:00

growing up. So we started watching it

## 100745:00 - 100765:00

and it's great.

## 100765:00 - 100790:00

>> I feel like everyone goes through that

## 100790:00 - 100815:00

eventually in their life. They decide I

## 100815:00 - 100830:00

will watch The Wire.

## 100830:00 - 100850:00

>> I know. So we are in that

## 100850:00 - 100900:00

>> year of your life. I It's great. I It's

## 100900:00 - 100925:00

such a great show. Oh man. And but it's

## 100925:00 - 100960:00

so many episodes and everyone's an hour

## 100960:00 - 100980:00

long.

## 100980:00 - 101020:00

>> I know. We get through like two or three

## 101020:00 - 101045:00

a week. So,

## 101045:00 - 101060:00

>> so we're very slow.

## 101060:00 - 101100:00

>> Worth it. Okay, next question. Do you

## 101100:00 - 101120:00

have a favorite product you've recently

## 101120:00 - 101150:00

discovered that you really love? And

## 101150:00 - 101170:00

we'll start with Shrea.

## 101170:00 - 101210:00

>> Yeah, I really like using cursor.

## 101210:00 - 101270:00

Honestly, now Cloud Code. Um, I'll I'll

## 101270:00 - 101310:00

say why. So, I think as a I'm a

## 101310:00 - 101355:00

researcher more so than anything else. I

## 101355:00 - 101380:00

write papers, I write code, I build

## 101380:00 - 101420:00

systems, everything. And I I find that

## 101420:00 - 101460:00

like a tool I'm so bullish on AI

## 101460:00 - 101490:00

assisted coding because like I have to

## 101490:00 - 101530:00

wear a lot of hats all the time. Um and

## 101530:00 - 101570:00

now I can be more ambitious with the

## 101570:00 - 101610:00

things that I build um and write papers

## 101610:00 - 101650:00

about. So I'm super excited about those.

## 101650:00 - 101700:00

Cursor was my entry point into this. Uh

## 101700:00 - 101740:00

but I'm starting to find myself trying

## 101740:00 - 101760:00

always trying to keep up with all these

## 101760:00 - 101800:00

AI assisted coding tools.

## 101800:00 - 101850:00

>> Haml. Yeah, I really like cloud code and

## 101850:00 - 101890:00

I like it because I feel like the UX is

## 101890:00 - 101940:00

outstanding. Um, there's a lot of love

## 101940:00 - 101995:00

that went into that. Um, it's just it's

## 101995:00 - 102030:00

just really impressive as a terminal

## 102030:00 - 102080:00

application that is that nice.

## 102080:00 - 102110:00

>> Ironic that you two both love cloud code

## 102110:00 - 102155:00

when it's just built on vibes.

## 102155:00 - 102185:00

>> I think it's false. It's not just built

## 102185:00 - 102210:00

on vibes.

## 102210:00 - 102255:00

>> There we go. Okay, two more questions.

## 102255:00 - 102280:00

Uh Hamill, do you have a favorite life

## 102280:00 - 102320:00

motto that you find yourself using and

## 102320:00 - 102365:00

coming back to in work or in life?

## 102365:00 - 102440:00

>> Keep learning and think like a beginner.

## 102440:00 - 102455:00

>> Beautiful. Shria,

## 102455:00 - 102505:00

>> I like that. Uh for me, it's to always

## 102505:00 - 102545:00

try to think about the other side's

## 102545:00 - 102585:00

argument. I find myself sometimes just

## 102585:00 - 102610:00

encountering arguments on the internet

## 102610:00 - 102665:00

like this recent eval debates and like

## 102665:00 - 102705:00

really think okay put myself in their

## 102705:00 - 102735:00

shoes. There's probably a generous take,

## 102735:00 - 102775:00

generous interpretation, and I think

## 102775:00 - 102825:00

we're all much stronger together than if

## 102825:00 - 102860:00

we start picking fights. My vision for

## 102860:00 - 102895:00

Evals is not that Hamel and I become

## 102895:00 - 102935:00

billionaires. It is that everyone can

## 102935:00 - 102970:00

build AI products and we're all on the

## 102970:00 - 102990:00

same page.

## 102990:00 - 103035:00

>> Slash Everyone becomes billionaires.

## 103035:00 - 103040:00

>> Yes.

## 103040:00 - 103065:00

>> Yes.

## 103065:00 - 103095:00

>> Amazing. Final question. When I have two

## 103095:00 - 103130:00

guests on, I always like to ask this

## 103130:00 - 103165:00

question and I'll start with Hamill.

## 103165:00 - 103200:00

What's something about Shrea that you

## 103200:00 - 103245:00

like most? What do you like most about

## 103245:00 - 103270:00

Shrea? And I'm going to ask her the same

## 103270:00 - 103345:00

question in reverse. Yeah, Shrea is one

## 103345:00 - 103385:00

of the wisest people that I know,

## 103385:00 - 103425:00

>> especially for being so young relative

## 103425:00 - 103460:00

to me. I feel like she's like much wiser

## 103460:00 - 103510:00

than I am, honestly. Seriously. Um,

## 103510:00 - 103570:00

she's very grounded and has like a very

## 103570:00 - 103610:00

even perspective on things.

## 103610:00 - 103650:00

And so I'm just really impressed by that

## 103650:00 - 103700:00

all the time.

## 103700:00 - 103710:00

>> Sure. Yeah.

## 103710:00 - 103750:00

>> Yeah. My favorite thing about Hamill is

## 103750:00 - 103790:00

his energy. I don't know anybody who

## 103790:00 - 103825:00

consistently maintains momentum and

## 103825:00 - 103870:00

energy like Hamill does. Um I often

## 103870:00 - 103930:00

think that like I would start caring

## 103930:00 - 104005:00

much less about Evals if not for Hamill.

## 104005:00 - 104050:00

And uh everyone needs a Haml in their

## 104050:00 - 104115:00

life for sure. M. Oh, well, we all have

## 104115:00 - 104160:00

a Haml in our life now. Uh, this was

## 104160:00 - 104185:00

incredible. This was everything I'd

## 104185:00 - 104215:00

hoped it'd be. I feel like this is the

## 104215:00 - 104260:00

most interesting, in-depth uh,

## 104260:00 - 104310:00

consumable uh, primer on emails that

## 104310:00 - 104330:00

I've ever seen. I'm really thankful

## 104330:00 - 104365:00

YouTube made time for this. Uh, two

## 104365:00 - 104390:00

final questions. Where can folks find

## 104390:00 - 104425:00

you? Where can they find the course? And

## 104425:00 - 104465:00

how can listeners be useful to you? Uh,

## 104465:00 - 104490:00

I'll start with Shrea.

## 104490:00 - 104530:00

>> Yeah. Uh, you can reach me via email.

## 104530:00 - 104560:00

It's on my website. If you Google my

## 104560:00 - 104585:00

name, that is the easiest way to get to

## 104585:00 - 104620:00

my website. You can find the course. If

## 104620:00 - 104680:00

you Google AI evals for engineers and

## 104680:00 - 104710:00

product managers or just AI evals

## 104710:00 - 104750:00

course, you'll find it. Um, we'll send

## 104750:00 - 104785:00

some links hopefully after this so it's

## 104785:00 - 104840:00

easy. And how to be helpful. Two things

## 104840:00 - 104880:00

always for me. One is ask me questions

## 104880:00 - 104910:00

when you have them. I will try to get to

## 104910:00 - 104940:00

them.

## 104940:00 - 104970:00

R respond as soon as I can. The other

## 104970:00 - 105010:00

one is tell us your successes. One of

## 105010:00 - 105050:00

the things that keeps us going is

## 105050:00 - 105085:00

somebody tells us like what they

## 105085:00 - 105130:00

implemented or what they did a real case

## 105130:00 - 105180:00

study and Haml and I get so excited from

## 105180:00 - 105235:00

these um and it really keeps us going.

## 105235:00 - 105270:00

So please share.

## 105270:00 - 105305:00

>> Yeah. Uh it's pretty easy to find me.

## 105305:00 - 105370:00

I'm my website is hamill.dev.

## 105370:00 - 105425:00

I'll give you the the link. Um you can

## 105425:00 - 105470:00

find me on social media, LinkedIn,

## 105470:00 - 105530:00

Twitter. Um thing that's most helpful is

## 105530:00 - 105565:00

to echo what Shrea said, we would be

## 105565:00 - 105605:00

delighted if we're not the only people

## 105605:00 - 105640:00

teaching evals. We would love other

## 105640:00 - 105695:00

people to teach evals. And so any kind

## 105695:00 - 105730:00

of blog posts,

## 105730:00 - 105785:00

writing especially that as you go

## 105785:00 - 105810:00

through this and learn this that you

## 105810:00 - 105860:00

want to share, we would be delighted to

## 105860:00 - 105910:00

help reshare that or amplify that.

## 105910:00 - 105950:00

Amazing. Very generous. Thank you so

## 105950:00 - 105970:00

much for being here. Uh, I really

## 105970:00 - 105990:00

appreciate it and you guys have a lot

## 105990:00 - 106020:00

going on. So, so thank you.

## 106020:00 - 106050:00

>> Thanks Lenny for having us and for all

## 106050:00 - 106080:00

the compliments.

## 106080:00 - 106135:00

>> My pleasure. Bye everyone.

## 106135:00 - 106165:00

>> Thank you so much for listening. If you

## 106165:00 - 106190:00

found this valuable, you can subscribe

## 106190:00 - 106230:00

to the show on Apple Podcasts, Spotify,

## 106230:00 - 106275:00

or your favorite podcast app. Also,

## 106275:00 - 106305:00

please consider giving us a rating or

## 106305:00 - 106335:00

leaving a review as that really helps

## 106335:00 - 106375:00

other listeners find the podcast. You

## 106375:00 - 106410:00

can find all past episodes or learn more

## 106410:00 - 106460:00

about the show at lennispodcast.com.

## 106460:00+

See you in the next episode.

