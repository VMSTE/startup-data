---
source: https://www.youtube.com/watch?v=qbvY0dQgSJ4
title: Al Engineering 101 with Chip Huyen (Nvidia, Stanford, Netflix)
author: Lenny's Podcast
date: 2025-10-23
views: 45568
description: |-
  Chip Huyen is a core developer on Nvidia’s Nemo platform, a former AI researcher at Netflix, and taught machine learning at Stanford. She’s a two-time founder and the author of two widely read books on AI, including AI Engineering, which has been the most-read book on the O’Reilly platform since its launch. Unlike many AI commentators, Chip has built multiple successful AI products and platforms and works directly with enterprises on their AI strategies, giving her unique visibility into what’s actually happening inside companies building AI products.

  *We discuss:*
  1. What people think makes AI apps better vs. what actually makes AI apps better
  2. What pre-training vs. post-training is, and why fine-tuning should be your last resort
  3. How RLHF (reinforcement learning from human feedback) actually works
  4. Why data quality matters more than which vector database you choose
  5. Why high performers are seeing the most gains from AI coding tools
  6. Why most AI problems are actually UX issues

  *Brought to you by:*
  Dscout—The UX platform to capture insights at every stage: from ideation to production: https://www.dscout.com/
  Justworks—The all-in-one HR solution for managing your small business with confidence: https://www.justworks.com
  Persona—A global leader in digital identity verification: https://withpersona.com/lenny

  *Transcript:* https://www.lennysnewsletter.com/p/al-engineering-101-with-chip-huyen

  *My biggest takeaways (for paid newsletter subscribers):* https://www.lennysnewsletter.com/i/176081814/my-biggest-takeaways-from-this-conversation

  *Where to find Chip Huyen:*
  • X: https://x.com/chipro
  • LinkedIn: https://www.linkedin.com/in/chiphuyen/
  • Website: https://huyenchip.com/
  • Substack: https://substack.com/@chiphuyen

  *Where to find Lenny:*
  • Newsletter: https://www.lennysnewsletter.com
  • X: https://twitter.com/lennysan
  • LinkedIn: https://www.linkedin.com/in/lennyrachitsky/

  *In this episode, we cover:*
  (00:00) Introduction to Chip Huyen
  (04:28) Chip’s viral LinkedIn post
  (07:05) Understanding AI training: pre-training vs. post-training
  (08:50) Language modeling explained
  (13:55) The importance of post-training
  (15:20) Reinforcement learning and human feedback
  (22:23) The importance of evals in AI development
  (31:55) Retrieval augmented generation (RAG) explained
  (38:50) Challenges in AI tool adoption
  (43:19) Challenges in measuring productivity
  (45:20) The three-bucket test
  (49:10) The future of engineering roles
  (55:31) ML Engineers vs. AI engineers
  (57:12) Looking forward: the impact of AI
  (01:05:48) Model capabilities vs. perceived performance
  (01:08:23) Lightning round and final thoughts

  *Referenced:*
  • Chip’s LinkedIn post on what actually improves AI apps: https://www.linkedin.com/posts/chiphuyen_aiapplications-aiengineering-activity-7358971409227792384-y0mf/
  • Prediction and Entropy of Printed English: https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf
  • Why experts writing AI evals is creating the fastest-growing companies in history | Brendan Foody (CEO of Mercor): https://www.lennysnewsletter.com/p/experts-writing-ai-evals-brendan-foody
  •Inside the expert network training every frontier AI model | Garrett Lord (Handshake CEO): https://www.lennysnewsletter.com/p/inside-handshake-garrett-lord
  • First interview with Scale AI’s CEO: $14B Meta deal, what’s working in enterprise AI, and what frontier labs are building next | Jason Droege: https://www.lennysnewsletter.com/p/first-interview-with-scale-ais-ceo-jason-droege
  • Anthropic’s CPO on what comes next | Mike Krieger (co-founder of Instagram): https://www.lennysnewsletter.com/p/anthropics-cpo-heres-what-comes-next
  • Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar (creators of the #1 eval course): https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill
  ...References continued at: https://www.lennysnewsletter.com/p/al-engineering-101-with-chip-huyen

  *Recommended books:*
  • The Complete Sherlock Holmes: https://www.amazon.com/Complete-Sherlock-Holmes-Volumes/dp/0553328255
  • AI Engineering: Building Applications with Foundation Models: https://www.amazon.com/AI-Engineering-Building-Applications-Foundation/dp/1098166302
  • The Selfish Gene: https://www.amazon.com/Selfish-Gene-Anniversary-Introduction/dp/0199291152
  • From Third World to First: The Singapore Story: 1965-2000: https://www.amazon.com/Third-World-First-Singapore-1965-2000/dp/0060197765

  _Production and marketing by https://penname.co/._
  _For inquiries about sponsoring the podcast, email podcast@lennyrachitsky.com._

  Lenny may be an investor in the companies discussed.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:41:21.795Z
---

# Al Engineering 101 with Chip Huyen (Nvidia, Stanford, Netflix)

## 00:00 - 35:00

One question that get asked a lot and a

## 35:00 - 60:00

lot is how do we keep up to date with

## 60:00 - 95:00

the latest AI news? Why why do you need

## 95:00 - 125:00

to keep up to date with the latest AI

## 125:00 - 155:00

news? If you talk to the users and

## 155:00 - 180:00

understand what they want, what they

## 180:00 - 205:00

don't want, look into the feedback, then

## 205:00 - 230:00

you can actually improve the application

## 230:00 - 245:00

way way way more.

## 245:00 - 270:00

>> A lot of companies are building AI

## 270:00 - 285:00

products. A lot of companies are not

## 285:00 - 315:00

having a good time building AI products.

## 315:00 - 350:00

>> We are in an ideal crisis now. We have

## 350:00 - 385:00

all this really cool tools. You have do

## 385:00 - 410:00

everything from scratch. It have your

## 410:00 - 440:00

design. It can have your right code. You

## 440:00 - 470:00

have your website. So in theory, we

## 470:00 - 495:00

should see a lot more. But at the same

## 495:00 - 520:00

time, it more or less somehow stuck.

## 520:00 - 550:00

They don't know what to build.

## 550:00 - 580:00

>> All this AI hype, the data is actually

## 580:00 - 600:00

showing most companies try it, doesn't

## 600:00 - 620:00

do a lot, they stop. What do you think

## 620:00 - 635:00

is the gap here?

## 635:00 - 660:00

>> It's really hard to measure

## 660:00 - 705:00

productivity. So I do ask people to ask

## 705:00 - 730:00

their managers, would you rather have

## 730:00 - 770:00

give everyone on the team very expensive

## 770:00 - 820:00

coding agent subscriptions or you get an

## 820:00 - 850:00

extra headcount. Almost everyone

## 850:00 - 885:00

managers would say headcount. But if you

## 885:00 - 925:00

ask VP level or someone who manage a lot

## 925:00 - 970:00

of teams they would say one AI assistant

## 970:00 - 995:00

because as managers you are still

## 995:00 - 1035:00

growing. So for you having one HR head

## 1035:00 - 1070:00

is big whereas for executive maybe you

## 1070:00 - 1095:00

have more business metrics that you you

## 1095:00 - 1125:00

care about. So you actually think about

## 1125:00 - 1165:00

what actually drive productivity metrics

## 1165:00 - 1190:00

for you.

## 1190:00 - 1230:00

>> Today my guest is Chip Hen. Unlike a lot

## 1230:00 - 1260:00

of people who share insights into

## 1260:00 - 1290:00

building great AI products and where

## 1290:00 - 1320:00

things are heading. Chip has built

## 1320:00 - 1355:00

multiple successful AI products,

## 1355:00 - 1395:00

platforms, tools. Chip was a core

## 1395:00 - 1435:00

developer on NVIDIA's Nemo platform, an

## 1435:00 - 1470:00

AI researcher at Netflix. She taught

## 1470:00 - 1505:00

machine learning at Stanford. She's also

## 1505:00 - 1540:00

a two-time founder and the author of two

## 1540:00 - 1565:00

of the most popular books in the world

## 1565:00 - 1600:00

of AI, including her most recent book

## 1600:00 - 1635:00

called AI Engineering, which has been

## 1635:00 - 1665:00

the most read book on the O'Reilly

## 1665:00 - 1700:00

platform since its launch. She's also

## 1700:00 - 1730:00

gotten to work with a lot of enterprises

## 1730:00 - 1765:00

on their AI strategies and so she gets

## 1765:00 - 1795:00

to see what's actually happening on the

## 1795:00 - 1815:00

ground inside a lot of different

## 1815:00 - 1850:00

companies. In our conversation, Chip

## 1850:00 - 1890:00

explains a lot of the basics like what

## 1890:00 - 1920:00

exactly does pre-training and

## 1920:00 - 1955:00

post-training look like? What is RAG?

## 1955:00 - 1980:00

What is reinforcement learning? What is

## 1980:00 - 2020:00

RHF? We also get into everything she's

## 2020:00 - 2050:00

learned about how to build great AI

## 2050:00 - 2080:00

products, including what people think it

## 2080:00 - 2110:00

takes and what it actually takes. We

## 2110:00 - 2135:00

talk about the most common pitfalls that

## 2135:00 - 2165:00

companies run into, where she's seeing

## 2165:00 - 2195:00

the most productivity gains, and so much

## 2195:00 - 2230:00

more. This episode is quite technical,

## 2230:00 - 2255:00

more technical than most conversations

## 2255:00 - 2285:00

I've had, and is meant for anyone

## 2285:00 - 2310:00

looking for a more in-depth conversation

## 2310:00 - 2350:00

about AI. If you enjoy this podcast,

## 2350:00 - 2370:00

don't forget to subscribe and follow it

## 2370:00 - 2400:00

in your favorite podcasting app or

## 2400:00 - 2430:00

YouTube. And if you become an annual

## 2430:00 - 2465:00

subscriber of my newsletter, you get a

## 2465:00 - 2520:00

year free of 16 incredible products,

## 2520:00 - 2550:00

including Devon, Lovable, Replet, Bolt,

## 2550:00 - 2580:00

NAN, Linear, Superhum, Dcript, Whisper

## 2580:00 - 2610:00

Flow, Gamma, Perplexity, Warp, Granola,

## 2610:00 - 2635:00

Magic Patterns, Rickcast, JPRD, and

## 2635:00 - 2680:00

Mobin. Head on over to Lenny's.com and

## 2680:00 - 2720:00

click product pass. With that, I bring

## 2720:00 - 2765:00

you Chip when after a short word from

## 2765:00 - 2805:00

our sponsors. This episode is brought to

## 2805:00 - 2855:00

you by Dcout. Design teams today are

## 2855:00 - 2895:00

expected to move fast, but also to get

## 2895:00 - 2940:00

it right. That's where Dout comes in.

## 2940:00 - 2975:00

Dout is the all-in-one research platform

## 2975:00 - 3005:00

built for modern product and design

## 3005:00 - 3035:00

teams. Whether you're running usability

## 3035:00 - 3070:00

tests, interviews, surveys, or in the

## 3070:00 - 3110:00

wild fieldwork, Dout makes it easy to

## 3110:00 - 3140:00

connect with real users and get real

## 3140:00 - 3180:00

insights fast. You can even test your

## 3180:00 - 3220:00

Figma prototypes directly inside the

## 3220:00 - 3265:00

platform. No juggling tools, no chasing

## 3265:00 - 3300:00

ghost participants. And with the

## 3300:00 - 3345:00

industry's most trusted panel, plus AI

## 3345:00 - 3385:00

powered analysis, your team gets clarity

## 3385:00 - 3420:00

and confidence to build better without

## 3420:00 - 3450:00

slowing down. So if you're ready to

## 3450:00 - 3475:00

streamline your research, speed up

## 3475:00 - 3510:00

decisions, and design with impact. Head

## 3510:00 - 3555:00

to dscout.com to learn more. That's

## 3555:00 - 3600:00

dsc.com.

## 3600:00 - 3625:00

The answers you need to move

## 3625:00 - 3665:00

confidently. Did you know that I have a

## 3665:00 - 3700:00

whole team that helps me with my podcast

## 3700:00 - 3730:00

and with my newsletter? I want everyone

## 3730:00 - 3765:00

on that team to be super happy and

## 3765:00 - 3805:00

thrive in their roles. Just Works knows

## 3805:00 - 3830:00

that your employees are more than just

## 3830:00 - 3865:00

your employees. They're your people. My

## 3865:00 - 3895:00

team is spread out across Colorado,

## 3895:00 - 3940:00

Australia, Nepal, West Africa, and San

## 3940:00 - 3970:00

Francisco. My life would be so

## 3970:00 - 4005:00

incredibly complicated to hire people

## 4005:00 - 4030:00

internationally, to pay people on time

## 4030:00 - 4065:00

and in their local currencies, and to

## 4065:00 - 4110:00

answer their HR questions 24/7. But with

## 4110:00 - 4150:00

Just Works, it's super easy. Whether

## 4150:00 - 4175:00

you're setting up your own automated

## 4175:00 - 4210:00

payroll, offering premium benefits, or

## 4210:00 - 4245:00

hiring internationally, JustWorks offers

## 4245:00 - 4295:00

simple software and 24/7 human support

## 4295:00 - 4325:00

from small business experts for you and

## 4325:00 - 4355:00

your people. They do your human

## 4355:00 - 4390:00

resources right so that you can do right

## 4390:00 - 4435:00

by your people. Just works for your

## 4435:00 - 4510:00

people.

## 4510:00 - 4540:00

>> Chip, thank you so much for being here

## 4540:00 - 4570:00

and welcome to the podcast.

## 4570:00 - 4600:00

>> Hi, Lenny. I've been a big fan of a

## 4600:00 - 4625:00

podcast for a while. So, I'm really

## 4625:00 - 4655:00

excited to be here. Thank you for having

## 4655:00 - 4660:00

me.

## 4660:00 - 4690:00

>> I want to start with this table

## 4690:00 - 4735:00

slashchart that you shared on LinkedIn a

## 4735:00 - 4765:00

while ago that went super viral. And I

## 4765:00 - 4790:00

think it went super viral because it hit

## 4790:00 - 4820:00

a nerve with a lot of people. And let me

## 4820:00 - 4840:00

just read this and we'll show this on

## 4840:00 - 4865:00

YouTube for people that are watching.

## 4865:00 - 4895:00

So, it's this very simple table you

## 4895:00 - 4925:00

shared of what people think will improve

## 4925:00 - 4970:00

AI apps and what actually improves AI

## 4970:00 - 5000:00

apps. what people think will improve AI

## 5000:00 - 5030:00

apps, staying up to date with the latest

## 5030:00 - 5070:00

AI news, adopting the newest agentic

## 5070:00 - 5100:00

framework, agonizing over vector

## 5100:00 - 5140:00

databases to use, constantly evaluating

## 5140:00 - 5180:00

what model is smarter, fine-tuning a

## 5180:00 - 5215:00

model, and then you have what actually

## 5215:00 - 5260:00

improves AI apps, talking to users,

## 5260:00 - 5285:00

building more reliable platforms,

## 5285:00 - 5320:00

preparing better data, optimizing

## 5320:00 - 5350:00

end-to-end workflows, writing better

## 5350:00 - 5390:00

prompts. Why do you think this such a

## 5390:00 - 5415:00

nerve with people? And just what if you

## 5415:00 - 5430:00

had to boil it down, what do you think

## 5430:00 - 5450:00

is what do you think people are missing

## 5450:00 - 5480:00

about building successful AI apps?

## 5480:00 - 5510:00

>> One one question that get asked a lot

## 5510:00 - 5560:00

and a lot is that how do we keep up to

## 5560:00 - 5605:00

date with the latest AI news? And I'm

## 5605:00 - 5640:00

like why why do you need to keep up to

## 5640:00 - 5675:00

date with the latest AI news? I know it

## 5675:00 - 5710:00

sound very counter counter intuitive but

## 5710:00 - 5750:00

there's so much news out there. A lot of

## 5750:00 - 5795:00

people also ask me questions like how do

## 5795:00 - 5815:00

I choose between two different

## 5815:00 - 5845:00

technologies like maybe like recently

## 5845:00 - 5890:00

like MCP versus like Asian Asians,

## 5890:00 - 5915:00

right? like protocol and it was like

## 5915:00 - 5950:00

which one is better or like this or that

## 5950:00 - 5990:00

and a ser question I used to ask them is

## 5990:00 - 6030:00

like first like if how much of the

## 6030:00 - 6075:00

improvements could you get like from

## 6075:00 - 6110:00

like optimal solutions versus nonoptimal

## 6110:00 - 6140:00

solutions right and sometimes they were

## 6140:00 - 6175:00

like actually it's not much right and I

## 6175:00 - 6195:00

was like okay if it's not much

## 6195:00 - 6240:00

improvement why do you want to spend so

## 6240:00 - 6265:00

much time debating something that

## 6265:00 - 6305:00

doesn't uh make that much difference to

## 6305:00 - 6335:00

your performance and another question

## 6335:00 - 6365:00

they asked is like if you adopt a new

## 6365:00 - 6420:00

technology like how hard it would be to

## 6420:00 - 6450:00

switch that out to another. And

## 6450:00 - 6480:00

sometimes it were like, oh, I think it

## 6480:00 - 6520:00

would be like a lot of work switching it

## 6520:00 - 6550:00

out. And I was just like, hm, let's say

## 6550:00 - 6580:00

here's a new technology. It hasn't been

## 6580:00 - 6610:00

tested by a lot of people. And if you

## 6610:00 - 6635:00

adopt it, you would be like stuck with

## 6635:00 - 6665:00

it forever. Like, do you actually want

## 6665:00 - 6690:00

to adopt it, right? And maybe you want

## 6690:00 - 6735:00

to think twice about about like

## 6735:00 - 6785:00

overcommit to like a new technology that

## 6785:00 - 6825:00

hasn't been battle tested. I love your

## 6825:00 - 6865:00

just broader advice is just simple like

## 6865:00 - 6900:00

talk to to build successful apps talk to

## 6900:00 - 6955:00

users build better data uh write better

## 6955:00 - 7005:00

prompts optimize the user experience

## 7005:00 - 7040:00

versus just like what is the latest and

## 7040:00 - 7060:00

greatest what's the best model to use

## 7060:00 - 7100:00

right now what's happening in AI let me

## 7100:00 - 7135:00

follow this thread of this idea of

## 7135:00 - 7180:00

fine-tuning and basically post-training

## 7180:00 - 7205:00

there's all these terms that people hear

## 7205:00 - 7225:00

in AI and I think this is going to be a

## 7225:00 - 7250:00

really good opportunity for people to

## 7250:00 - 7285:00

learn what we're actually talking about

## 7285:00 - 7315:00

since you actually do these things. You

## 7315:00 - 7330:00

build these things. You work with

## 7330:00 - 7350:00

companies doing these things. And um

## 7350:00 - 7370:00

there's a few terms I want to sprinkle

## 7370:00 - 7395:00

in through the conversation, but let's

## 7395:00 - 7420:00

start with this one. What what's the

## 7420:00 - 7450:00

simplest way for someone to understand

## 7450:00 - 7485:00

what is the difference between

## 7485:00 - 7510:00

pre-training and post- training and then

## 7510:00 - 7540:00

just how fine-tuning fits into that?

## 7540:00 - 7575:00

Just what fine-tuning actually is.

## 7575:00 - 7600:00

>> Disclaimer, I don't have like full

## 7600:00 - 7630:00

visibility into like on what like this

## 7630:00 - 7665:00

big secretive like frontier labs are

## 7665:00 - 7700:00

doing. Uh but right from what I heard,

## 7700:00 - 7730:00

right? So, so I think it's like one is

## 7730:00 - 7765:00

um like supervised fetuning when you

## 7765:00 - 7790:00

have demonstration data and you have

## 7790:00 - 7830:00

like a bunch of like um experts like

## 7830:00 - 7870:00

okay here's a prop right and here is

## 7870:00 - 7905:00

what the answer should be like and like

## 7905:00 - 7945:00

you you you just train it like on like

## 7945:00 - 7990:00

to like stim like uh simulate um like

## 7990:00 - 8025:00

emulate what the human expert would be

## 8025:00 - 8055:00

like and that's also like what a lot of

## 8055:00 - 8105:00

people would like um the the open source

## 8105:00 - 8130:00

models are doing they do it by

## 8130:00 - 8160:00

distillation so instead of having human

## 8160:00 - 8195:00

experts should like write really good

## 8195:00 - 8240:00

starting a great answers to like prompts

## 8240:00 - 8290:00

that get like very popular famous good

## 8290:00 - 8325:00

models to like generate a respond to it

## 8325:00 - 8365:00

and like getting this train smaller

## 8365:00 - 8405:00

model to emulate. So, so sometimes you

## 8405:00 - 8435:00

see people just like so that's because

## 8435:00 - 8470:00

like some I I really appreciate open

## 8470:00 - 8500:00

source community by the way but like

## 8500:00 - 8525:00

going from like have been able to train

## 8525:00 - 8575:00

a models that can emulate a existing

## 8575:00 - 8615:00

good model is very different from like

## 8615:00 - 8650:00

being able to train a good models like

## 8650:00 - 8695:00

an outperform existing good model. So

## 8695:00 - 8730:00

it's a big step there. Uh so yeah so

## 8730:00 - 8765:00

like we have supervised fetuning and

## 8765:00 - 8800:00

another things that's like very big uh

## 8800:00 - 8820:00

I'm not sure you have guessed talking

## 8820:00 - 8845:00

about it already but like reinforcement

## 8845:00 - 8875:00

learning is like everywhere. Okay, let's

## 8875:00 - 8895:00

pause on that because I definitely want

## 8895:00 - 8920:00

to spend time on that and that's such a

## 8920:00 - 8950:00

cool topic that I that's emerging more

## 8950:00 - 8975:00

and more in my conversations. But just

## 8975:00 - 9005:00

to even summarize the things you just

## 9005:00 - 9030:00

shared which I think is really really

## 9030:00 - 9070:00

important stuff. So the idea here is a

## 9070:00 - 9095:00

model is essentially this algorithm

## 9095:00 - 9125:00

piece of code that someone writes and

## 9125:00 - 9150:00

say the frontier models are feeding it

## 9150:00 - 9180:00

just like the entire internet of content

## 9180:00 - 9225:00

and basically it's trying to test itself

## 9225:00 - 9265:00

on predicting in all of the in across

## 9265:00 - 9320:00

all that data the next word essentially

## 9320:00 - 9345:00

token is a simpler way isn't the correct

## 9345:00 - 9370:00

way to think about it but a simpler way

## 9370:00 - 9390:00

to think about it is like the next word

## 9390:00 - 9460:00

in a in text and as it gets it wrong it

## 9460:00 - 9495:00

adjusts these things called weights

## 9495:00 - 9530:00

essentially uh just like is that a

## 9530:00 - 9550:00

simple way to think about it even though

## 9550:00 - 9580:00

that's that even that's just like very

## 9580:00 - 9610:00

surface level. So I think of language

## 9610:00 - 9650:00

modeling as a way of encoding

## 9650:00 - 9675:00

statistical information about a

## 9675:00 - 9725:00

language, right? So so let's say that um

## 9725:00 - 9760:00

we we both speak English. So we kind get

## 9760:00 - 9790:00

a sense of like what is more

## 9790:00 - 9835:00

statistically likely like if I say my

## 9835:00 - 9875:00

favorite color is then you would like

## 9875:00 - 9900:00

okay that should be another color like

## 9900:00 - 9925:00

the word blue would be much more likely

## 9925:00 - 9980:00

to appear than the word like uh of table

## 9980:00 - 10020:00

right because statistically blue is more

## 10020:00 - 10055:00

likely to come back to every color is so

## 10055:00 - 10100:00

so it's just like get is um it's is it's

## 10100:00 - 10130:00

a way of encoding statical information

## 10130:00 - 10155:00

so like when language modeling when you

## 10155:00 - 10190:00

train a large amount of data like it you

## 10190:00 - 10225:00

see a lot of languages a lot of domains

## 10225:00 - 10260:00

so it can tell like okay you bas say

## 10260:00 - 10300:00

this standards then if user do the

## 10300:00 - 10325:00

prompt then it would come like with the

## 10325:00 - 10375:00

next uh most likely token uh so by the

## 10375:00 - 10405:00

way it's not a new idea actually every

## 10405:00 - 10435:00

so it's the idea comes very very old

## 10435:00 - 10505:00

like from the 1951 papers um um the like

## 10505:00 - 10535:00

English entropy I think it's like called

## 10535:00 - 10560:00

Shannon it's a great paper and I think

## 10560:00 - 10605:00

every a story I really like um it's from

## 10605:00 - 10645:00

did you read Sherlock Holm by the way

## 10645:00 - 10670:00

>> uh yeah I read a few Sherlock Holmes

## 10670:00 - 10685:00

books yeah

## 10685:00 - 10715:00

>> yeah so so this is story of like when

## 10715:00 - 10745:00

Sherlock Holmes was using this statical

## 10745:00 - 10790:00

information to like have sewn a case. So

## 10790:00 - 10830:00

he was getting um so this in this story

## 10830:00 - 10875:00

uh there is uh somebody left message uh

## 10875:00 - 10910:00

with a lot of like stick figures. So

## 10910:00 - 10950:00

Shhol was like okay he knows that in

## 10950:00 - 11005:00

English the most common letter is E then

## 11005:00 - 11055:00

the most common stick figure must be E

## 11055:00 - 11085:00

right and then he goes he start like

## 11085:00 - 11145:00

that it was just s uh so the uh the code

## 11145:00 - 11180:00

so I think that's language so in a way

## 11180:00 - 11205:00

that's like simple language modeling

## 11205:00 - 11225:00

right but instead of like at a word

## 11225:00 - 11265:00

level he does it at like tok like

## 11265:00 - 11290:00

character level and token is something

## 11290:00 - 11330:00

in between right token is not quite a

## 11330:00 - 11375:00

word uh but it's bigger than a character

## 11375:00 - 11410:00

so let's say uh we we say token because

## 11410:00 - 11460:00

uh it helps us like read what help us

## 11460:00 - 11490:00

reduce vocabulary because with character

## 11490:00 - 11520:00

is like smallest amount of like

## 11520:00 - 11560:00

vocabulary right so the five has like 26

## 11560:00 - 11590:00

character but words can have like

## 11590:00 - 11625:00

millions and millions right uh whereas

## 11625:00 - 11685:00

um um tokens you can like

## 11685:00 - 11715:00

be able to like get like the sweet spot

## 11715:00 - 11745:00

between the two so let's say that we

## 11745:00 - 11805:00

have like uh the new word like uh uh how

## 11805:00 - 11845:00

to say like podcasting right let's say

## 11845:00 - 11880:00

it's a it's a new word but it can divide

## 11880:00 - 11915:00

podcast and ink So people understand

## 11915:00 - 11945:00

okay podcast we know the meaning we know

## 11945:00 - 12005:00

that ink is like uh like a verb like

## 12005:00 - 12040:00

girant whatever it is so we we know the

## 12040:00 - 12065:00

word like podcasting. So that's why the

## 12065:00 - 12115:00

token comes in but yeah uh that's like

## 12115:00 - 12140:00

the pre-tuning is basically like

## 12140:00 - 12185:00

encoding statistical informations of

## 12185:00 - 12215:00

language to have you predict what is

## 12215:00 - 12275:00

most likely um I think like most likely

## 12275:00 - 12310:00

is the most simple way of doing it. uh

## 12310:00 - 12330:00

because it's more like building a

## 12330:00 - 12365:00

distributions of like okay so the next

## 12365:00 - 12400:00

token could be like more like like 90%

## 12400:00 - 12440:00

of the time it could be like a color 90

## 12440:00 - 12460:00

like 10% of the time could be like

## 12460:00 - 12485:00

something else right so based on

## 12485:00 - 12510:00

distributions the language could like

## 12510:00 - 12565:00

pick like depending on your sampling

## 12565:00 - 12595:00

strategy like do you want it to always

## 12595:00 - 12635:00

pick the most likely token or you wanted

## 12635:00 - 12665:00

to pick something more creative you know

## 12665:00 - 12710:00

so so so I think sampling strategy I

## 12710:00 - 12750:00

think is something extremely important

## 12750:00 - 12775:00

can have you boost up performance in a

## 12775:00 - 12825:00

in a huge way and very very underrated.

## 12825:00 - 12880:00

>> Okay, awesome. So essentially uh a model

## 12880:00 - 12935:00

is just code with this whole uh set of

## 12935:00 - 12965:00

weights essentially the statistical

## 12965:00 - 13005:00

model that has learned to predict what

## 13005:00 - 13030:00

comes next after certain words and

## 13030:00 - 13050:00

phrases.

## 13050:00 - 13060:00

>> Yeah.

## 13060:00 - 13105:00

>> And then post-raining and fine-tuning

## 13105:00 - 13135:00

specifically is doing that same thing.

## 13135:00 - 13190:00

So pre-training you get like GPT5

## 13190:00 - 13230:00

fine-tuning is someone taking GPT5 and

## 13230:00 - 13270:00

doing the same sort of thing. uh

## 13270:00 - 13295:00

adjusting these awaits a little bit for

## 13295:00 - 13345:00

specific use cases on data that they uh

## 13345:00 - 13370:00

find is necessary to do their very

## 13370:00 - 13395:00

specific use case. Is that a simple way

## 13395:00 - 13410:00

to think about it?

## 13410:00 - 13450:00

>> Yeah, I think you ws as like functions,

## 13450:00 - 13480:00

right? So let's say just like you you

## 13480:00 - 13520:00

have uh maybe has a functions of like

## 13520:00 - 13585:00

maybe Lenny's height is maybe like 1x

## 13585:00 - 13625:00

like 1x plus something or like 2x like

## 13625:00 - 13665:00

one and plus something is is a waist,

## 13665:00 - 13700:00

right? So you change it until you fit

## 13700:00 - 13750:00

the uh the the correct data which is

## 13750:00 - 13780:00

like my height and your height, right?

## 13780:00 - 13800:00

So so you can think of the weight is

## 13800:00 - 13825:00

just like a way like they function. So

## 13825:00 - 13865:00

so you like chain adjust the weight so

## 13865:00 - 13890:00

they can fit the data which is a

## 13890:00 - 13910:00

training data.

## 13910:00 - 13945:00

>> Awesome. Okay. So so we're talking about

## 13945:00 - 13965:00

pre-training, post- training,

## 13965:00 - 13985:00

finetuning. Is there anything else here

## 13985:00 - 14005:00

that's important to share about just

## 14005:00 - 14045:00

like what this is exactly? What people

## 14045:00 - 14090:00

need to understand about these parts of

## 14090:00 - 14130:00

training? So the vast majority of time

## 14130:00 - 14170:00

we don't touch on like pre-union model

## 14170:00 - 14215:00

like as users we don't use already done

## 14215:00 - 14225:00

for us.

## 14225:00 - 14255:00

>> Yeah. So so I think actually it's bit of

## 14255:00 - 14290:00

fun like uh process like when my friends

## 14290:00 - 14315:00

training models like I try to play with

## 14315:00 - 14335:00

their pre-shing model and they're

## 14335:00 - 14380:00

horrendous. They like saying things like

## 14380:00 - 14415:00

oh my god this is like yeah it's crazy.

## 14415:00 - 14460:00

Um so so it's it's really interesting to

## 14460:00 - 14495:00

look at like how much of like post

## 14495:00 - 14545:00

training can change the motor behavior.

## 14545:00 - 14585:00

Um yeah and I think that's where like a

## 14585:00 - 14615:00

lot of time that a lot of people are

## 14615:00 - 14650:00

spending energy on nowadays in front lab

## 14650:00 - 14690:00

is on like post training because uh

## 14690:00 - 14740:00

pre-training uh I think um so preing

## 14740:00 - 14765:00

have been

## 14765:00 - 14800:00

used to like increase the general c

## 14800:00 - 14835:00

capacity of of of a model capabilities

## 14835:00 - 14880:00

of a model and it depends on a lot of

## 14880:00 - 14930:00

data and like model size to increase um

## 14930:00 - 14965:00

to increase the model capabilities and

## 14965:00 - 14995:00

at some point we are actually like have

## 14995:00 - 15025:00

max out like in data right and then

## 15025:00 - 15050:00

people like texted that pretty much I

## 15050:00 - 15070:00

think a lot of people are doing like

## 15070:00 - 15115:00

with other data like audios and videos

## 15115:00 - 15140:00

and everyone's trying to think of like

## 15140:00 - 15175:00

what is the new source of data but where

## 15175:00 - 15210:00

like post trading but like of course

## 15210:00 - 15240:00

like this more of like everyone can have

## 15240:00 - 15285:00

very similar pre-training data is like

## 15285:00 - 15325:00

post trading is where they make a big

## 15325:00 - 15345:00

difference nowadays

## 15345:00 - 15375:00

>> this is a good segue to you talked about

## 15375:00 - 15400:00

supervised learning versus unsupervised

## 15400:00 - 15420:00

learning I love we're getting into this

## 15420:00 - 15445:00

by the way this is super interesting so

## 15445:00 - 15475:00

you talked about labeled data basically

## 15475:00 - 15515:00

supervised learning is AI learning on

## 15515:00 - 15555:00

data that somebody has already labeled

## 15555:00 - 15580:00

and told it here's correct versus

## 15580:00 - 15615:00

incorrect for example this is spam

## 15615:00 - 15665:00

versus not spam this is uh a good short

## 15665:00 - 15690:00

story this is not a good short story

## 15690:00 - 15725:00

we've had u the cos of a lot of these

## 15725:00 - 15760:00

companies that do this for labs uh

## 15760:00 - 15815:00

mercor and scale handshake uh there's

## 15815:00 - 15870:00

micro uh there's a few others so is is

## 15870:00 - 15895:00

that essentially what these companies

## 15895:00 - 15930:00

are doing for labs giving them labeled

## 15930:00 - 15960:00

data high quality data to train on

## 15960:00 - 16000:00

>> it is in a way but I think it's more

## 16000:00 - 16045:00

like a product of big equations. So

## 16045:00 - 16060:00

there are a lot more different

## 16060:00 - 16090:00

components than that. So that's why I

## 16090:00 - 16110:00

was talking about reinforcement

## 16110:00 - 16145:00

learning. I'm not sure if your CEOs that

## 16145:00 - 16180:00

you interview bring up like that term.

## 16180:00 - 16225:00

Uh so so the idea is that um you want

## 16225:00 - 16265:00

people to like so like let's say you

## 16265:00 - 16300:00

have a model give the model like a prop

## 16300:00 - 16335:00

right and it produce an output right you

## 16335:00 - 16395:00

want to buy like you want to reinforce

## 16395:00 - 16430:00

or encourage the model to produce an

## 16430:00 - 16480:00

output that is better right so so like

## 16480:00 - 16520:00

how like now time to like how do we know

## 16520:00 - 16570:00

that the answer is good or bad right so

## 16570:00 - 16630:00

people realize on like um signals so one

## 16630:00 - 16660:00

way to get like a first one good or bad

## 16660:00 - 16685:00

is like human feedback Right? It happen

## 16685:00 - 16710:00

we have two responses. You can okay this

## 16710:00 - 16750:00

one is better than the other. Um and we

## 16750:00 - 16790:00

do that is because like as humans uh we

## 16790:00 - 16825:00

tend to it's very hard to give like

## 16825:00 - 16860:00

concrete score but it's easier to do

## 16860:00 - 16895:00

comparisons right like if you ask me

## 16895:00 - 16945:00

okay give this song a score. I'm not a

## 16945:00 - 16970:00

musicians like and don't know like how

## 16970:00 - 16990:00

hard it is like it's like yeah I don't

## 16990:00 - 17020:00

know like what like now 10 I go six you

## 17020:00 - 17045:00

know and like if you ask me again a

## 17045:00 - 17070:00

month from now and I completely forgot

## 17070:00 - 17105:00

okay maybe now seven or like four I

## 17105:00 - 17130:00

don't know but they need to ask me okay

## 17130:00 - 17155:00

here are two songs and which one would

## 17155:00 - 17190:00

you prefer to play for the birthday

## 17190:00 - 17230:00

party I was like okay I can prefer this

## 17230:00 - 17275:00

song so like comparison is a lot easier

## 17275:00 - 17320:00

um so say yes so we have a humans um you

## 17320:00 - 17355:00

have human feedback uh and then you use

## 17355:00 - 17380:00

this human feedback to train a reward

## 17380:00 - 17420:00

model so like tell like which like so

## 17420:00 - 17445:00

and then Free root model help you like

## 17445:00 - 17475:00

okay the model now produce this response

## 17475:00 - 17510:00

is robot model can score is this good or

## 17510:00 - 17535:00

bad you charge some bias toward like

## 17535:00 - 17570:00

producing better model the better

## 17570:00 - 17600:00

responses another ways like you can

## 17600:00 - 17625:00

instead of using a humans you can use

## 17625:00 - 17675:00

like AI right like a response say yes or

## 17675:00 - 17710:00

good good or bad right or the thing is

## 17710:00 - 17735:00

that people are very big on nowadays

## 17735:00 - 17770:00

like verifiable rewards which is like

## 17770:00 - 17810:00

natural um so basically they give it a

## 17810:00 - 17855:00

math problems and then math solutions uh

## 17855:00 - 17885:00

like is a model output a solution is you

## 17885:00 - 17920:00

know that okay expected response should

## 17920:00 - 17970:00

in a 42 and it doesn't provide 42 then

## 17970:00 - 18005:00

it's then it's wrong right it's not a

## 18005:00 - 18050:00

good response um so so yes so like uh a

## 18050:00 - 18080:00

lot of time people like using this um

## 18080:00 - 18140:00

human labor like human um human laborers

## 18140:00 - 18180:00

should like produce like m like um how

## 18180:00 - 18220:00

to say expert questions and like the

## 18220:00 - 18260:00

expected answers and in a way that like

## 18260:00 - 18300:00

design a system that like verifiable so

## 18300:00 - 18340:00

that the the models can can be trained

## 18340:00 - 18350:00

on yeah

## 18350:00 - 18370:00

>> okay I'm really glad you went there this

## 18370:00 - 18415:00

is essentially RHF reinforcement

## 18415:00 - 18440:00

learning with human feedback which is

## 18440:00 - 18470:00

exactly what I wanted to also talk about

## 18470:00 - 18485:00

right

## 18485:00 - 18520:00

>> yeah so um I think it's like it's

## 18520:00 - 18545:00

general it's like it's a way of learning

## 18545:00 - 18575:00

it's like training is contextual

## 18575:00 - 18600:00

learning and whether it learned from

## 18600:00 - 18635:00

human feedback or like AI feedback or

## 18635:00 - 18680:00

like verifiable rewards uh I think I say

## 18680:00 - 18720:00

you say just different way of like um

## 18720:00 - 18745:00

collei signals

## 18745:00 - 18780:00

>> awesome yeah that's uh I we had the c of

## 18780:00 - 18805:00

anthropic on the podcast and he talked

## 18805:00 - 18830:00

about their version of RHF which is

## 18830:00 - 18870:00

AIdriven reinforcement learning I love

## 18870:00 - 18885:00

the way you phrased it where you

## 18885:00 - 18930:00

basically you want to help the model.

## 18930:00 - 18960:00

You want to reinforce correct behavior

## 18960:00 - 18990:00

and correct answers and this is the

## 18990:00 - 19025:00

method to do it. Whether it's say an

## 19025:00 - 19065:00

engineer seeing an output from a model

## 19065:00 - 19100:00

being like no here's how I would code it

## 19100:00 - 19140:00

differently and then training and it's

## 19140:00 - 19175:00

training a different model that the

## 19175:00 - 19230:00

original model works with to tell it am

## 19230:00 - 19255:00

I correct or not correct. Is that right?

## 19255:00 - 19265:00

Yeah.

## 19265:00 - 19295:00

>> Yeah. I I think I think that's a way of

## 19295:00 - 19335:00

of looking into it and I think that's a

## 19335:00 - 19375:00

space is so exciting nowadays because

## 19375:00 - 19425:00

there's so many like domain expert task

## 19425:00 - 19460:00

that the model like that model

## 19460:00 - 19495:00

developers want model to do well on

## 19495:00 - 19525:00

right let's say you're like accountant

## 19525:00 - 19545:00

right like maybe you want to use a model

## 19545:00 - 19580:00

to have accounting task so I need a lot

## 19580:00 - 19625:00

of like accounting data like examples

## 19625:00 - 19650:00

from like accountants so you need to

## 19650:00 - 19675:00

hire a lot of them should I do it or if

## 19675:00 - 19705:00

you want to do physics problems or you

## 19705:00 - 19760:00

want to do um I don't know like legal

## 19760:00 - 19790:00

questions and stuff or like engineering

## 19790:00 - 19815:00

questions or like somebody was telling

## 19815:00 - 19855:00

me they want to do like uh using like

## 19855:00 - 19890:00

coding for to solve scientific problems

## 19890:00 - 19910:00

and not just like coding to build

## 19910:00 - 19945:00

product which is another different whole

## 19945:00 - 19975:00

realm of things and I also like using

## 19975:00 - 20020:00

very specific toolings like uh yeah like

## 20020:00 - 20050:00

I'm not sure what apps you use but maybe

## 20050:00 - 20090:00

like um for editing app or like

## 20090:00 - 20130:00

Quickbooks or like Google Excel like

## 20130:00 - 20160:00

they have very specific like tune

## 20160:00 - 20200:00

specific um expert expertise that you

## 20200:00 - 20230:00

want the models to learn. So like they

## 20230:00 - 20275:00

need a lot of like humans expert in this

## 20275:00 - 20325:00

area to like create data to train them.

## 20325:00 - 20355:00

Um and it's a massive things. It's like

## 20355:00 - 20385:00

people because uh everyone wants a lot

## 20385:00 - 20410:00

of data and like want slaps like

## 20410:00 - 20460:00

unlimited budget. Uh but uh whether I

## 20460:00 - 20485:00

think this is also like a little bit of

## 20485:00 - 20525:00

lowkey interesting economics. I'm not

## 20525:00 - 20560:00

sure you talk to to like the guest about

## 20560:00 - 20590:00

I thought it's very interesting to think

## 20590:00 - 20635:00

about because it's very lopsided, right?

## 20635:00 - 20665:00

because like there only like a very

## 20665:00 - 20720:00

small numbers of frontier labs right and

## 20720:00 - 20755:00

they want a lot of data and there's like

## 20755:00 - 20785:00

a massive amount of like startups or

## 20785:00 - 20820:00

companies are providing related data so

## 20820:00 - 20845:00

like you can see this companies like

## 20845:00 - 20880:00

this startup like doing later but they

## 20880:00 - 20920:00

have like maybe have like massive AR but

## 20920:00 - 20950:00

you ask them like okay so how many

## 20950:00 - 20975:00

customers you have and they could be

## 20975:00 - 21015:00

like oh a very small numbers I'm not

## 21015:00 - 21050:00

sure I'm not sure you you I saw you

## 21050:00 - 21060:00

smiling

## 21060:00 - 21095:00

>> yeah we chat we chat about that

## 21095:00 - 21125:00

>> yeah so so I'm like a bit like leave me

## 21125:00 - 21160:00

unease Right? They have like a companies

## 21160:00 - 21195:00

growing like crazy but it's like heavily

## 21195:00 - 21230:00

dependent on like

## 21230:00 - 21270:00

>> two or three companies and at the same

## 21270:00 - 21300:00

time like if I if I was this company

## 21300:00 - 21340:00

Frontier Labs what could be the right

## 21340:00 - 21385:00

economical things for me to do right now

## 21385:00 - 21420:00

I want a lot of startups I want to have

## 21420:00 - 21455:00

a lot of providers so I can pick and

## 21455:00 - 21490:00

choose and then this providers can also

## 21490:00 - 21525:00

like to compete each other to lower the

## 21525:00 - 21550:00

price and it's so dependent on me they

## 21550:00 - 21580:00

will sell to me regardless. So, so I

## 21580:00 - 21615:00

feel like Yeah. So, so this economics,

## 21615:00 - 21655:00

the whole economics is very interesting

## 21655:00 - 21685:00

to me and I'm curious to see how it

## 21685:00 - 21695:00

plays out.

## 21695:00 - 21720:00

>> What I'm hearing is you're uh you're

## 21720:00 - 21750:00

bearish on the future of these data

## 21750:00 - 21795:00

labeling companies because as you said,

## 21795:00 - 21825:00

they don't have a lot of leverage over

## 21825:00 - 21845:00

pricing because they have so few

## 21845:00 - 21875:00

customers and there's so many people

## 21875:00 - 21910:00

getting into the space. So, basically,

## 21910:00 - 21930:00

even though they're some of the fastest

## 21930:00 - 21950:00

growing companies in the world, you're

## 21950:00 - 21985:00

feeling like there's there's a challenge

## 21985:00 - 21995:00

up ahead.

## 21995:00 - 22040:00

>> I'm not sure if I'm bearish on it. Um I

## 22040:00 - 22095:00

think I'm curious because I think things

## 22095:00 - 22150:00

have has a way of work out in ways that

## 22150:00 - 22205:00

I don't expect. So I think that maybe

## 22205:00 - 22235:00

these companies they have a lot of data.

## 22235:00 - 22265:00

Maybe they wouldn't be able to use that

## 22265:00 - 22295:00

to like have some insight that helps

## 22295:00 - 22330:00

them like stay ahead of the curve, you

## 22330:00 - 22370:00

know. So so I don't know. Uh

## 22370:00 - 22410:00

>> a very fair answer. Okay. While we're on

## 22410:00 - 22445:00

this topic, I want to chat about evals,

## 22445:00 - 22475:00

which is a very recurring topic in this

## 22475:00 - 22525:00

podcast. This is the other piece of data

## 22525:00 - 22560:00

content these companies share that AI

## 22560:00 - 22585:00

labs really need. Can you just talk

## 22585:00 - 22625:00

about what an eval is the simplest way

## 22625:00 - 22670:00

to understand it and then how this helps

## 22670:00 - 22695:00

models get smarter.

## 22695:00 - 22730:00

>> So I think if people approach eval I

## 22730:00 - 22765:00

think there like two very different

## 22765:00 - 22825:00

problems. ones is a app builder right

## 22825:00 - 22865:00

like can I say I have an app uh that do

## 22865:00 - 22925:00

like uh maybe a chatbot very simple and

## 22925:00 - 22950:00

I know it's first thing that came to my

## 22950:00 - 22980:00

mind um and I want you to know is

## 22980:00 - 23010:00

chatbot is good or bad right so I need

## 23010:00 - 23040:00

to come up way with like evaluate the

## 23040:00 - 23085:00

chatbot um another thing is uh I think

## 23085:00 - 23140:00

of this as a uh task specific evol

## 23140:00 - 23170:00

design so let's say I'm a model

## 23170:00 - 23220:00

developer and I want to make my model

## 23220:00 - 23255:00

better at curve writing right and I was

## 23255:00 - 23300:00

like okay but how How how do I even

## 23300:00 - 23330:00

measure cerwiting right? So I would need

## 23330:00 - 23370:00

someone to like okay understand cer

## 23370:00 - 23400:00

writing and think about like what makes

## 23400:00 - 23445:00

good story like what makes a story good

## 23445:00 - 23495:00

and then designed the whole data set and

## 23495:00 - 23525:00

then criteria to evaluate creative

## 23525:00 - 23565:00

writing. Um so yeah so so I think

## 23565:00 - 23590:00

there's that I think it's like more like

## 23590:00 - 23645:00

eval design that is very interesting uh

## 23645:00 - 23710:00

come criteria um come guideline how to

## 23710:00 - 23755:00

do it and then also like train people

## 23755:00 - 23805:00

like how to do it effectively um so I

## 23805:00 - 23840:00

guess uh in a course I think Evar is

## 23840:00 - 23890:00

really really fun because it's extremely

## 23890:00 - 23915:00

creative uh I was looking at like

## 23915:00 - 23940:00

different avons people build and was

## 23940:00 - 23990:00

like wow like it's not dry at all this

## 23990:00 - 24020:00

is like super super super fun

## 24020:00 - 24055:00

>> we had a whole podcast any vals with HML

## 24055:00 - 24110:00

Haml and Shrea and uh and that's exactly

## 24110:00 - 24130:00

what they talked about is just it's

## 24130:00 - 24155:00

actually really fun to create evals for

## 24155:00 - 24195:00

for companies especially. So let's still

## 24195:00 - 24220:00

dig into that one a little bit more.

## 24220:00 - 24250:00

There's this kind of debate online that

## 24250:00 - 24275:00

I don't know how big of a deal this

## 24275:00 - 24320:00

debate is, but it feels like people uh

## 24320:00 - 24345:00

spend a lot of time thinking about this

## 24345:00 - 24385:00

this idea of do we need evals for AI

## 24385:00 - 24410:00

products? Some of the best companies say

## 24410:00 - 24440:00

they don't really do evals. They just go

## 24440:00 - 24460:00

on vibes. They're just like is this

## 24460:00 - 24505:00

working well? Can I feel it or not?

## 24505:00 - 24535:00

What's your take on just the importance

## 24535:00 - 24585:00

of building evals and the skill of eval

## 24585:00 - 24645:00

for app AI apps not the model companies?

## 24645:00 - 24685:00

>> You don't have to be like absolutely

## 24685:00 - 24725:00

perfect at things to win. You just need

## 24725:00 - 24755:00

to be like good enough and being

## 24755:00 - 24795:00

consistent about it. Okay, this is not

## 24795:00 - 24835:00

the philosophy I follow but like I have

## 24835:00 - 24865:00

worked with enough companies to see that

## 24865:00 - 24905:00

play out. So when I say like why company

## 24905:00 - 24930:00

don't need evaluate let's say you are

## 24930:00 - 24965:00

like an executive right and you want to

## 24965:00 - 24995:00

have a new use case. So here's a use

## 24995:00 - 25020:00

case you you started out we built and

## 25020:00 - 25040:00

it's like it works well right the

## 25040:00 - 25065:00

customers are somewhat happy don't you

## 25065:00 - 25090:00

don't have the exact metric for it but

## 25090:00 - 25130:00

like the traffic keeps increasing like

## 25130:00 - 25155:00

people seem happy people keep buying

## 25155:00 - 25185:00

stuff right and now here's our engineer

## 25185:00 - 25230:00

coming like okay we need eva for it and

## 25230:00 - 25265:00

so I think it was like okay how much

## 25265:00 - 25295:00

effort do we need to put into eva and

## 25295:00 - 25335:00

they were like okay uh maybe like two

## 25335:00 - 25370:00

engineers as much as much and it could

## 25370:00 - 25400:00

maybe would improve so was like okay so

## 25400:00 - 25430:00

how much expected gain can I get from it

## 25430:00 - 25460:00

and the engineer would be like oh maybe

## 25460:00 - 25515:00

you can improve it from like 80% to like

## 25515:00 - 25570:00

82% 85% right and I was like okay but we

## 25570:00 - 25600:00

take like that two engineers and we

## 25600:00 - 25640:00

launch a new feature then it could give

## 25640:00 - 25675:00

me like so much more like improvement

## 25675:00 - 25705:00

right so so I think it's like one of

## 25705:00 - 25730:00

them is like sometime people think of

## 25730:00 - 25760:00

evol okay this is good enough just don't

## 25760:00 - 25790:00

touch it like if you do spend a lot of

## 25790:00 - 25815:00

energy on eva I would like only

## 25815:00 - 25855:00

incremental improvement where it spends

## 25855:00 - 25895:00

the energy on like another use case and

## 25895:00 - 25930:00

maybe it's good enough that you vive

## 25930:00 - 25970:00

check it right so so I I do think it's

## 25970:00 - 26005:00

like maybe like that's a debate is about

## 26005:00 - 26035:00

um I do think that's like a lot of time

## 26035:00 - 26060:00

people just like get things to the to

## 26060:00 - 26095:00

the place when it's like okay good

## 26095:00 - 26145:00

enough people run but and then but of

## 26145:00 - 26165:00

course it's like there's a lot of risk

## 26165:00 - 26195:00

associated with it because if you don't

## 26195:00 - 26240:00

have a clear metric you uh you have a

## 26240:00 - 26290:00

good visibility to how the application

## 26290:00 - 26320:00

models are performing it might do

## 26320:00 - 26350:00

something very dumb or it can cost you

## 26350:00 - 26390:00

like I know some something like crazy

## 26390:00 - 26450:00

can happen so so yeah so um so so I do

## 26450:00 - 26515:00

think evol is very very important. If

## 26515:00 - 26565:00

you have if you operate at scale and

## 26565:00 - 26615:00

where like failures can have like

## 26615:00 - 26650:00

catastrophic consequences then you do

## 26650:00 - 26685:00

need to be very tyrannical about like

## 26685:00 - 26725:00

what you put in front of the users

## 26725:00 - 26750:00

understand different failure modes like

## 26750:00 - 26785:00

what could go wrong and also maybe in a

## 26785:00 - 26825:00

space that like is is a feature of the

## 26825:00 - 26850:00

product is as a competitive advantage

## 26850:00 - 26875:00

right you want to be the best at it you

## 26875:00 - 26905:00

want to have like a very strong

## 26905:00 - 26940:00

understanding of like where you are and

## 26940:00 - 26970:00

like where you are with the competitors

## 26970:00 - 26990:00

but it's just something that's like more

## 26990:00 - 27015:00

like a low key. Okay, this like

## 27015:00 - 27040:00

something is like okay that's not the

## 27040:00 - 27075:00

core or like it helps with our users

## 27075:00 - 27125:00

then maybe you don't need to be so so

## 27125:00 - 27160:00

obsessed or like tyical about it is okay

## 27160:00 - 27190:00

that's good enough for now and if it

## 27190:00 - 27225:00

fails then it fails like okay I know

## 27225:00 - 27250:00

it's like it's so terrifying but like

## 27250:00 - 27300:00

yeah um yeah I think it's all about like

## 27300:00 - 27330:00

the question of like return investment

## 27330:00 - 27375:00

um I'm a big fan of I love writing Eva

## 27375:00 - 27415:00

say it's like I understand why some

## 27415:00 - 27460:00

people would choose to not focus on Eva

## 27460:00 - 27500:00

right away and choose like bringing on

## 27500:00 - 27530:00

new functionalities instead.

## 27530:00 - 27555:00

>> Awesome. That is a really pragmatic

## 27555:00 - 27595:00

answer. What I'm hearing is eval are

## 27595:00 - 27620:00

great, very important, especially if

## 27620:00 - 27660:00

you're operating at scale, but pick your

## 27660:00 - 27690:00

battles. You don't need to write evals

## 27690:00 - 27720:00

for every little feature. Something that

## 27720:00 - 27760:00

Hamlin Shrea shared is that people need

## 27760:00 - 27780:00

just like I don't know five or seven

## 27780:00 - 27815:00

evals for the most important elements of

## 27815:00 - 27835:00

their product. Is that is that what you

## 27835:00 - 27855:00

see or do you see a lot more in

## 27855:00 - 27885:00

production that people build and need?

## 27885:00 - 27955:00

Um I I don't think of like

## 27955:00 - 27990:00

just a fixed number unlike the evol like

## 27990:00 - 28020:00

what was the goal of evol right the go

## 28020:00 - 28055:00

to evol is to guys of product

## 28055:00 - 28105:00

development um so so like you see evol

## 28105:00 - 28135:00

um because I think I'm a big fan of evol

## 28135:00 - 28170:00

is is that it helps you uncover

## 28170:00 - 28195:00

opportunities where the products are

## 28195:00 - 28225:00

doing well so I sometimes seen it very

## 28225:00 - 28270:00

often okay we look at the AA we realize

## 28270:00 - 28315:00

it's like okay it perform really poorly

## 28315:00 - 28360:00

on this like specific segment of users

## 28360:00 - 28390:00

and then we look into it's like what

## 28390:00 - 28415:00

what what what's what's wrong with it

## 28415:00 - 28450:00

and it turns out it's like we just like

## 28450:00 - 28475:00

don't have a good messaging to it. So

## 28475:00 - 28515:00

like we should like just focus on the

## 28515:00 - 28545:00

things that we doing can improve

## 28545:00 - 28580:00

significantly. Yeah. So I kind of the

## 28580:00 - 28630:00

number of evol is really depends like we

## 28630:00 - 28665:00

have seen product with like hundreds of

## 28665:00 - 28685:00

different metrics right like people like

## 28685:00 - 28730:00

going crazy this is because like product

## 28730:00 - 28755:00

is like general right have different

## 28755:00 - 28780:00

have like one avar for like I don't know

## 28780:00 - 28820:00

like uh verity have like one evolve for

## 28820:00 - 28865:00

like user sensitive data um and like

## 28865:00 - 28910:00

another is like is um for length but

## 28910:00 - 28965:00

like has a number of like um okay let's

## 28965:00 - 29005:00

just example complex simple like div

## 29005:00 - 29035:00

research so so you have the application

## 29035:00 - 29070:00

you have like build a to like do deep

## 29070:00 - 29105:00

research for you, right? like okay like

## 29105:00 - 29145:00

have a prompt like me say okay do me a

## 29145:00 - 29190:00

com comprehensive research on Lenny's

## 29190:00 - 29240:00

podcast and help me like some like uh

## 29240:00 - 29295:00

propose like show me report on what kind

## 29295:00 - 29325:00

of topics he's interested in what kind

## 29325:00 - 29360:00

of videos could get the most views or

## 29360:00 - 29390:00

like what topics that he's missing on

## 29390:00 - 29420:00

that he should be covering right like

## 29420:00 - 29450:00

have that kind of like prompt then how

## 29450:00 - 29505:00

do you evaluate the the result right I

## 29505:00 - 29540:00

don't think this like one like metrics

## 29540:00 - 29570:00

that would help maybe just like maybe

## 29570:00 - 29600:00

you have like a 100 I think somebody has

## 29600:00 - 29625:00

a benchmark and is they get like a 100

## 29625:00 - 29655:00

expert like write a bunch of prompts and

## 29655:00 - 29695:00

they go through like all the all the

## 29695:00 - 29730:00

answers on AI and I do it and it's like

## 29730:00 - 29775:00

it's extremely costly and slow right but

## 29775:00 - 29810:00

if I might have something else for like

## 29810:00 - 29840:00

one way was thinking about it um I was

## 29840:00 - 29875:00

talking to a friend about it and and one

## 29875:00 - 29935:00

way is like how to produce the result of

## 29935:00 - 29970:00

the of the summary right at first you

## 29970:00 - 30015:00

need to do like gather informations and

## 30015:00 - 30075:00

to gather informations you need to do a

## 30075:00 - 30130:00

lot search queries uh you like gathers

## 30130:00 - 30160:00

grab the search results and then from

## 30160:00 - 30200:00

the search results you like uh aggregate

## 30200:00 - 30225:00

and then maybe say okay I'm still

## 30225:00 - 30250:00

missing on this you have to go another

## 30250:00 - 30280:00

route and like another route is another

## 30280:00 - 30320:00

summary so every step of the way you

## 30320:00 - 30350:00

need evaluations right you don't need to

## 30350:00 - 30380:00

end to end so maybe the first search

## 30380:00 - 30410:00

query you might first think about like

## 30410:00 - 30450:00

okay now I write five search queries I

## 30450:00 - 30475:00

might look into like how good are the

## 30475:00 - 30505:00

search queries like do they like are

## 30505:00 - 30525:00

they like similar to each other because

## 30525:00 - 30555:00

you need five such queries that are very

## 30555:00 - 30615:00

similar like Lenny podcast nanny podcast

## 30615:00 - 30655:00

uh last month landed podcast like two

## 30655:00 - 30685:00

months ago right it's not it's not very

## 30685:00 - 30715:00

very exciting but like if the quer is a

## 30715:00 - 30745:00

podcast like the the keywords are like

## 30745:00 - 30805:00

more um more diverse right and then look

## 30805:00 - 30830:00

at the results of the of the search

## 30830:00 - 30855:00

query let's say you enter the search

## 30855:00 - 30905:00

query like Lenny Parscat data label like

## 30905:00 - 30940:00

and then they come up with like 10 pages

## 30940:00 - 30965:00

uh 10 results and then you come up with

## 30965:00 - 31030:00

like oh Lenny podcast on uh I don't know

## 31030:00 - 31070:00

m um I don't know like uh Frontier Labs

## 31070:00 - 31095:00

and have like 10 results. I might look

## 31095:00 - 31125:00

at a different web page like how much of

## 31125:00 - 31160:00

them overlapping like are we are we

## 31160:00 - 31190:00

doing both like the breath like getting

## 31190:00 - 31235:00

a lot of page but also like do we have

## 31235:00 - 31265:00

depth and also like have relevance

## 31265:00 - 31290:00

because we come up with a search queries

## 31290:00 - 31340:00

that completely irrelevant to the to to

## 31340:00 - 31370:00

the original prompt. So I feel like

## 31370:00 - 31400:00

every aspect of it it would need a way

## 31400:00 - 31425:00

of evaluating right so I don't think

## 31425:00 - 31470:00

it's just like how many evolve should I

## 31470:00 - 31535:00

get but like how many evolve should do I

## 31535:00 - 31580:00

need to get a good coverage a high

## 31580:00 - 31615:00

confidence in my application's

## 31615:00 - 31645:00

performance and also to help me

## 31645:00 - 31670:00

understand like where it is not

## 31670:00 - 31715:00

performing well so that I can fix it.

## 31715:00 - 31750:00

>> Awesome. And I'm hearing also just

## 31750:00 - 31800:00

especially for the very core use case

## 31800:00 - 31825:00

like the most common path people take in

## 31825:00 - 31880:00

your product is where you want to focus.

## 31880:00 - 31910:00

>> Yeah. So yeah.

## 31910:00 - 31940:00

>> Okay. Let me there's one more term I

## 31940:00 - 31965:00

want to cover and I want to go in a

## 31965:00 - 32015:00

somewhat different direction. Rag people

## 32015:00 - 32065:00

see this term a lot. RA what does it

## 32065:00 - 32075:00

mean?

## 32075:00 - 32115:00

>> So rag is stand for retrieval augmented

## 32115:00 - 32170:00

generations. It also not specific to JD

## 32170:00 - 32215:00

AI. So um the idea is just like for a

## 32215:00 - 32245:00

lot of questions we need context to

## 32245:00 - 32295:00

answer. So I think it came pretty oh I

## 32295:00 - 32335:00

think it's from the paper 2017.

## 32335:00 - 32375:00

So so someone was like um so they

## 32375:00 - 32405:00

realizes like for a bunch of like

## 32405:00 - 32435:00

benchmark when the question answering

## 32435:00 - 32465:00

benchmarks they realize it's like okay

## 32465:00 - 32520:00

if we give the model informations about

## 32520:00 - 32555:00

the questions then the answer can be

## 32555:00 - 32585:00

much much better. So what they do was

## 32585:00 - 32615:00

they try to retrieve information from

## 32615:00 - 32650:00

Wikipedia. So for for questionable

## 32650:00 - 32675:00

topics just like retrieve that and then

## 32675:00 - 32710:00

put in the context and like answer it

## 32710:00 - 32735:00

does much better. So I feel like it

## 32735:00 - 32755:00

sounds like a no-brainer, right? I mean

## 32755:00 - 32780:00

like obviously. So, so I think that's

## 32780:00 - 32810:00

what racket as a simplest sense is just

## 32810:00 - 32855:00

like providing the model with a relevant

## 32855:00 - 32900:00

context so so that it can answer the

## 32900:00 - 32930:00

questions and and that's where like

## 32930:00 - 32970:00

things get like uh really uh more more

## 32970:00 - 33005:00

interesting because traditionally when

## 33005:00 - 33055:00

it started out rack is mostly like text

## 33055:00 - 33090:00

um so so we we talk about like a lot of

## 33090:00 - 33130:00

way like how to prepare data so that the

## 33130:00 - 33160:00

model can retrieve u effectively let's

## 33160:00 - 33190:00

say there like not everything is a

## 33190:00 - 33230:00

wikipia page right like Wikipedia page

## 33230:00 - 33265:00

is pretty contained and like you know

## 33265:00 - 33295:00

everything about it is about a topic. Uh

## 33295:00 - 33320:00

but a lot of time you have documents

## 33320:00 - 33355:00

extremely long, right? And like they

## 33355:00 - 33380:00

have a weird way of like structures the

## 33380:00 - 33410:00

documents. Let's say that um you have

## 33410:00 - 33450:00

documents about Lenny uh podcast, right?

## 33450:00 - 33480:00

And in the in the future in the

## 33480:00 - 33525:00

beginning documents like from now on

## 33525:00 - 33555:00

podcast wouldn't refer to Lenny's

## 33555:00 - 33590:00

podcast, right? So let's say somebody in

## 33590:00 - 33620:00

the future like tell me about Lenny,

## 33620:00 - 33665:00

right? Lenny's work. And because the

## 33665:00 - 33690:00

rest of the document does not have the

## 33690:00 - 33730:00

term leni you just don't know uh you

## 33730:00 - 33755:00

might not read through it and the

## 33755:00 - 33780:00

document is long enough that it chunk

## 33780:00 - 33805:00

into a different part. So like the

## 33805:00 - 33840:00

second part doesn't have the the word

## 33840:00 - 33875:00

manic so you cannot reach. So I have to

## 33875:00 - 33910:00

find a way to like process data. So that

## 33910:00 - 33955:00

makes sure it's like it can retrieve the

## 33955:00 - 33985:00

information just relevant to the query

## 33985:00 - 34010:00

even though it might not immediately

## 34010:00 - 34050:00

like obvious that is related. So people

## 34050:00 - 34075:00

come up with like only thing I think

## 34075:00 - 34110:00

like contextual visual

## 34110:00 - 34165:00

um like uh giving x chunk of the data uh

## 34165:00 - 34200:00

the relevant like maybe like summary

## 34200:00 - 34245:00

meta data so that it knows um or like

## 34245:00 - 34285:00

some people use like as a hypothetical

## 34285:00 - 34315:00

questions it's very interesting like for

## 34315:00 - 34345:00

even the chunk of like documents I

## 34345:00 - 34385:00

generated a bunch of questions that the

## 34385:00 - 34420:00

chunks can help answer so that when they

## 34420:00 - 34455:00

have a a query it was like okay does it

## 34455:00 - 34485:00

match any of the like hypothetical

## 34485:00 - 34520:00

questions so it can it can fetch it so

## 34520:00 - 34550:00

it's very interesting approach

## 34550:00 - 34580:00

Okay. So maybe before I go to the next

## 34580:00 - 34610:00

thing I just want to say this like data

## 34610:00 - 34640:00

preparations for rack is extremely

## 34640:00 - 34675:00

important and I would say this like in

## 34675:00 - 34710:00

the a lot of the companies that I have

## 34710:00 - 34745:00

seen that's like the biggest performance

## 34745:00 - 34785:00

in their rack solutions coming from like

## 34785:00 - 34835:00

better data preparations not agonizing

## 34835:00 - 34880:00

over like what better databases to use

## 34880:00 - 34910:00

uh because database of course it's very

## 34910:00 - 34930:00

important to care about like things like

## 34930:00 - 34980:00

latency or like if you have like very

## 34980:00 - 35025:00

specific access patterns like read heavy

## 35025:00 - 35050:00

or write heavy Of course it's like it

## 35050:00 - 35090:00

matters but in term of like pure quality

## 35090:00 - 35110:00

answers right I think the data

## 35110:00 - 35140:00

preparation is just like hands out

## 35140:00 - 35165:00

>> when you say data preparation what's an

## 35165:00 - 35200:00

example to make that real and concrete

## 35200:00 - 35220:00

for us to understand

## 35220:00 - 35255:00

>> so so like one way is like uh um

## 35255:00 - 35285:00

mentioned as in like um you have like

## 35285:00 - 35320:00

chunks of data so we think about like

## 35320:00 - 35355:00

how big of each chunk should be right

## 35355:00 - 35400:00

because um if it's like so let's think

## 35400:00 - 35430:00

about like if a context you want to

## 35430:00 - 35465:00

maximize maybe you can it's very simple

## 35465:00 - 35500:00

example right you want to retrieve like

## 35500:00 - 35545:00

a thousand words right so If HM's data

## 35545:00 - 35595:00

is too long um then so if if a data cham

## 35595:00 - 35635:00

is long then it's more likely to contain

## 35635:00 - 35675:00

more relevant metadata so you can

## 35675:00 - 35735:00

retrieve more but if it's too long like

## 35735:00 - 35770:00

then you have a thousand word and so

## 35770:00 - 35795:00

chunk is like a thousand words you can

## 35795:00 - 35825:00

reach one chunk so it's not very useful

## 35825:00 - 35870:00

but it's too short then you can retrieve

## 35870:00 - 35910:00

more relevant information like oh so it

## 35910:00 - 35965:00

can retrieve a wider range of like

## 35965:00 - 35995:00

documents and chunk but at the same time

## 35995:00 - 36030:00

a chunk is too small to contain relevant

## 36030:00 - 36055:00

information. So you have like very nice

## 36055:00 - 36095:00

like chunk design like how big a chunk

## 36095:00 - 36130:00

should be. Uh you add like contextual

## 36130:00 - 36170:00

informations like summary, metadata,

## 36170:00 - 36205:00

hypothetical questions. Uh somebody was

## 36205:00 - 36230:00

telling me like um a very big

## 36230:00 - 36275:00

performance they got is that from um

## 36275:00 - 36305:00

rewriting their data in the question

## 36305:00 - 36340:00

answering format. So like instead of

## 36340:00 - 36365:00

having like so they have a podcast right

## 36365:00 - 36400:00

instead of just chunking the podcast you

## 36400:00 - 36430:00

just like reframe rewrite it into like

## 36430:00 - 36470:00

here's a question here's answers um like

## 36470:00 - 36495:00

and and produce a lot of them. you can

## 36495:00 - 36530:00

use AI for that as well. So that's one

## 36530:00 - 36565:00

example of data processing. A lot of

## 36565:00 - 36605:00

example we I see is like for people

## 36605:00 - 36640:00

helping like using AI to have like

## 36640:00 - 36680:00

specific uh tool use and documentations

## 36680:00 - 36710:00

right and a lot and we write

## 36710:00 - 36755:00

documentation usually a lot of document

## 36755:00 - 36800:00

documentation today is written for human

## 36800:00 - 36830:00

um reading and AI reading is different

## 36830:00 - 36860:00

because it's different because humans we

## 36860:00 - 36890:00

have like common sense and we kind know

## 36890:00 - 36935:00

what it is. Um so so one one things or

## 36935:00 - 36960:00

like uh human for human experts they

## 36960:00 - 36985:00

have the context that AI doesn't quite

## 36985:00 - 37020:00

have. So somebody told me that like

## 37020:00 - 37050:00

what's the big change they have is like

## 37050:00 - 37080:00

let's say that um you have a you have a

## 37080:00 - 37115:00

function a document uh documentation for

## 37115:00 - 37150:00

this maybe this library and this library

## 37150:00 - 37195:00

say okay the output of this one is like

## 37195:00 - 37230:00

maybe talking for like I know some crazy

## 37230:00 - 37285:00

term maybe some uh temperature something

## 37285:00 - 37340:00

under graph should be like one zero or

## 37340:00 - 37375:00

minus one and as a human expert maybe

## 37375:00 - 37400:00

understand the scale like what one in

## 37400:00 - 37425:00

the scale mean but like for AI just

## 37425:00 - 37445:00

really doesn't understand what that

## 37445:00 - 37475:00

means so so actually have like another

## 37475:00 - 37505:00

allot annotation

## 37505:00 - 37540:00

layer for AI it's like okay got

## 37540:00 - 37580:00

temperatures equal one mean like that

## 37580:00 - 37615:00

it's not like it's the abstra it's like

## 37615:00 - 37650:00

associated with the scale over there so

## 37650:00 - 37690:00

just saving all this data processing to

## 37690:00 - 37720:00

make it easier for AI to retrieve the

## 37720:00 - 37745:00

relevant information to answer the

## 37745:00 - 37760:00

questions

## 37760:00 - 37785:00

>> this episode is brought to you by

## 37785:00 - 37825:00

persona the verified identity platform

## 37825:00 - 37865:00

helping organizations onboard users

## 37865:00 - 37910:00

fight fraud and build trust we talk a

## 37910:00 - 37940:00

lot on this podcast about the amazing

## 37940:00 - 37975:00

advances in AI but this can be a

## 37975:00 - 38010:00

double-edged sword report. For every wow

## 38010:00 - 38045:00

moment, there are fraudsters using the

## 38045:00 - 38080:00

same tech to wreak havoc, laundering

## 38080:00 - 38110:00

money, taking over employee identities,

## 38110:00 - 38150:00

and impersonating businesses. Persona

## 38150:00 - 38170:00

helps combat these threats with

## 38170:00 - 38210:00

automated user, business, and employee

## 38210:00 - 38245:00

verification. Whether you're looking to

## 38245:00 - 38280:00

catch candidate fraud, meet age

## 38280:00 - 38310:00

restrictions, or keep your platform

## 38310:00 - 38345:00

safe, Persona helps you verify users in

## 38345:00 - 38375:00

a way that's tailored to your specific

## 38375:00 - 38415:00

needs. Best of all, Persona makes it

## 38415:00 - 38440:00

easy to know who you're dealing with

## 38440:00 - 38475:00

without adding friction for good users.

## 38475:00 - 38515:00

This is why leading platforms like Etsy,

## 38515:00 - 38560:00

LinkedIn, Square, and Lyft trust Persona

## 38560:00 - 38600:00

to secure their platform. Persona is

## 38600:00 - 38640:00

also offering my listeners 500 free

## 38640:00 - 38680:00

services per month for one full year.

## 38680:00 - 38740:00

Just head to withpersona.com/lenny

## 38740:00 - 38765:00

to get started. That's

## 38765:00 - 38800:00

withpersona.com/lenny.

## 38800:00 - 38830:00

Thanks again to Persona for sponsoring

## 38830:00 - 38885:00

this episode. Awesome. Okay. So, you've

## 38885:00 - 38920:00

talked a bit about how you work with

## 38920:00 - 38950:00

companies on these sorts of things, on

## 38950:00 - 38980:00

their AI strategies, on their AI

## 38980:00 - 39015:00

products, how they build, which tools

## 39015:00 - 39045:00

they build, all these things. I want to

## 39045:00 - 39075:00

spend a little time here because a lot

## 39075:00 - 39100:00

of companies are building AI products. A

## 39100:00 - 39120:00

lot of companies are not having a good

## 39120:00 - 39160:00

time building AI products. Let me ask a

## 39160:00 - 39190:00

few questions along these lines of what

## 39190:00 - 39210:00

you've learned working with companies

## 39210:00 - 39255:00

that are doing this. Well, one is just,

## 39255:00 - 39290:00

I guess, in terms of AI tool adoption

## 39290:00 - 39310:00

and adoption in general within

## 39310:00 - 39325:00

companies. There's all this talk

## 39325:00 - 39360:00

recently of just like all this AI hype.

## 39360:00 - 39380:00

The data is actually showing most

## 39380:00 - 39415:00

companies try it doesn't do a lot they

## 39415:00 - 39440:00

stop and so there's all this just like

## 39440:00 - 39475:00

maybe this isn't going anywhere. So in

## 39475:00 - 39505:00

terms of just adoption of tools and AI

## 39505:00 - 39525:00

within companies what are you seeing

## 39525:00 - 39535:00

there

## 39535:00 - 39565:00

>> for gen AI in company I think there are

## 39565:00 - 39620:00

two type of genai toolings that have

## 39620:00 - 39665:00

been uh I have seen like ones is to like

## 39665:00 - 39715:00

um internal productivity right like have

## 39715:00 - 39785:00

coding tool slack chatbot um uh internal

## 39785:00 - 39825:00

knowledge like a lot of big enterprises

## 39825:00 - 39850:00

have some kind like a wrapper around

## 39850:00 - 39900:00

like um model so but like with access

## 39900:00 - 39935:00

like maybe some different kind of racket

## 39935:00 - 39975:00

I think we talk about that Um okay like

## 39975:00 - 40000:00

text based rack I haven't talked about

## 40000:00 - 40030:00

like Asian tech rack or like multim

## 40030:00 - 40065:00

motor rack yet but it's like yes there a

## 40065:00 - 40105:00

whole very exciting area around that um

## 40105:00 - 40120:00

yeah so like b b b b b b b b b b b b b b

## 40120:00 - 40140:00

b b b b b b b b b b b b b b b b b b b b b b b b b basically to allows the

## 40140:00 - 40205:00

employee to like access internal

## 40205:00 - 40235:00

document. Uh somebody somebody asked

## 40235:00 - 40275:00

like okay um I'm I'm having a baby what

## 40275:00 - 40325:00

could be the maternal or paternal policy

## 40325:00 - 40350:00

right or like am I having this

## 40350:00 - 40395:00

operations with the health benefit like

## 40395:00 - 40425:00

cover that or like I want to like

## 40425:00 - 40465:00

interview or I want to like refer my

## 40465:00 - 40490:00

friend what could be the process for

## 40490:00 - 40525:00

that so a lot of this like having

## 40525:00 - 40555:00

chatbot internal chatbot to help with

## 40555:00 - 40615:00

internal operations um and um another

## 40615:00 - 40670:00

things um another category is more like

## 40670:00 - 40720:00

customerf facing um so or like partner

## 40720:00 - 40760:00

facing um so so customer support chatbot

## 40760:00 - 40790:00

is a big one you have a hotel chain you

## 40790:00 - 40815:00

might have like a booking chatbot which

## 40815:00 - 40845:00

is like somehow massive like a lot of

## 40845:00 - 40870:00

booking chatbot because I guess it's

## 40870:00 - 40920:00

it's it's I do have this theory of like

## 40920:00 - 40960:00

a lot of applications uh companies

## 40960:00 - 40995:00

pursue because they can't measure the

## 40995:00 - 41030:00

concrete outcome and I feel like booking

## 41030:00 - 41060:00

or sale chatbot it's very clear right

## 41060:00 - 41085:00

like what's a conversion rate right now

## 41085:00 - 41120:00

with a chatbot with human operators and

## 41120:00 - 41145:00

what could be conversion rate with a

## 41145:00 - 41180:00

chatbot and then some somehow I think

## 41180:00 - 41220:00

it's like very clear outcome comes and

## 41220:00 - 41270:00

companies are easier to buy into this um

## 41270:00 - 41310:00

this solutions. So a lot of companies

## 41310:00 - 41340:00

have that like customer uh facing

## 41340:00 - 41395:00

chatbot. Uh so yeah so so that is um

## 41395:00 - 41445:00

another category of tool um and I think

## 41445:00 - 41500:00

that um I think for customers or

## 41500:00 - 41545:00

external facing tools um because people

## 41545:00 - 41610:00

are driven to um people are driven to

## 41610:00 - 41650:00

choose applications with clear outcomes.

## 41650:00 - 41695:00

So, so the questions of uh adopting them

## 41695:00 - 41730:00

is really based on like whether they see

## 41730:00 - 41765:00

the outcome or not. Of course, it's not

## 41765:00 - 41800:00

perfect because sometimes uh the outcome

## 41800:00 - 41840:00

can be bad not because the idea or like

## 41840:00 - 41880:00

the applications idea itself is bad.

## 41880:00 - 41920:00

It's just because the

## 41920:00 - 41955:00

the I know the the process of building

## 41955:00 - 42000:00

it is like not that great. Um yeah. So,

## 42000:00 - 42035:00

so it's tricky for the internal

## 42035:00 - 42065:00

adoptions of like tooling. So, internal

## 42065:00 - 42090:00

productivity that's where it gets

## 42090:00 - 42115:00

tricky. I would say like a lot of

## 42115:00 - 42150:00

companies uh what they think of as a

## 42150:00 - 42180:00

strategy like I think of as have like

## 42180:00 - 42245:00

usually have very um have like two key

## 42245:00 - 42285:00

aspect right it's like use cases and the

## 42285:00 - 42320:00

second is talent you might have like

## 42320:00 - 42350:00

great data for great use cases but you

## 42350:00 - 42380:00

don't have talents and you cannot do it

## 42380:00 - 42405:00

so a lot of time in the beginning with

## 42405:00 - 42435:00

geni and it's still and sometimes I'm

## 42435:00 - 42455:00

really admire a lot of companies for

## 42455:00 - 42485:00

that it's just like exactly like okay we

## 42485:00 - 42545:00

need our employees to be very geni aware

## 42545:00 - 42585:00

like very AI literate right so what to

## 42585:00 - 42620:00

do is they start like maybe like

## 42620:00 - 42665:00

adopting a bunch of tools for for the

## 42665:00 - 42695:00

team to use. They have a lot of upskill

## 42695:00 - 42730:00

upscaling uh workshops like they

## 42730:00 - 42765:00

encourage learning. I think it's like a

## 42765:00 - 42795:00

really really good thing and it's also

## 42795:00 - 42825:00

like willing to spend a lot of money

## 42825:00 - 42860:00

into like adopting like um giving people

## 42860:00 - 42900:00

like touchd

## 42900:00 - 42935:00

subscriptions uh cloud code

## 42935:00 - 42985:00

subscriptions like to get the employees

## 42985:00 - 43045:00

to like to to be more AI literate. Um

## 43045:00 - 43075:00

and the other thing is like a lot of the

## 43075:00 - 43105:00

secretary come say okay we spend a ton

## 43105:00 - 43150:00

of money as this tool but then we don't

## 43150:00 - 43180:00

see because you can see the usage it's

## 43180:00 - 43220:00

like but people don't seem to use them

## 43220:00 - 43270:00

as much and what is the issue so so yeah

## 43270:00 - 43310:00

so I think is that that is um that is

## 43310:00 - 43335:00

tricky yeah

## 43335:00 - 43365:00

>> what do you think is the issue is it

## 43365:00 - 43405:00

just they're not they're like they don't

## 43405:00 - 43425:00

know how to use them like what do you

## 43425:00 - 43450:00

think is the gap here do you think we'll

## 43450:00 - 43485:00

get to a place of just like wow work is

## 43485:00 - 43520:00

completely different because of AI for a

## 43520:00 - 43535:00

lot of companies

## 43535:00 - 43565:00

The main thing is like it's really hard

## 43565:00 - 43620:00

to measure productivity uh gain. So I

## 43620:00 - 43645:00

talked to a lot of people and they was

## 43645:00 - 43680:00

like first of all on on sample is coding

## 43680:00 - 43705:00

right a lot of companies not using

## 43705:00 - 43765:00

coding agents uh or coding aided coding

## 43765:00 - 43825:00

uh and um I was asking I was like I was

## 43825:00 - 43855:00

like okay do do you think that like it

## 43855:00 - 43895:00

helps with your productivity and a lot

## 43895:00 - 43925:00

of time the question is very handwavy

## 43925:00 - 43970:00

just like okay like okay I feel like

## 43970:00 - 44000:00

it's been better right and okay because

## 44000:00 - 44055:00

we have more PRs uh we see more code and

## 44055:00 - 44085:00

then immediate correct me okay but of

## 44085:00 - 44120:00

course code number of life code is not a

## 44120:00 - 44155:00

good metric for that right so so it's

## 44155:00 - 44190:00

it's really really tricky and it's

## 44190:00 - 44250:00

something funny uh so so so I do ask um

## 44250:00 - 44285:00

people to ask their managers because I

## 44285:00 - 44315:00

work with like usually the VP level so

## 44315:00 - 44350:00

they have like multiple teams under them

## 44350:00 - 44385:00

so I ask them like okay do you ask

## 44385:00 - 44445:00

managers um like okay would you rather

## 44445:00 - 44480:00

have access uh would you rather have

## 44480:00 - 44510:00

give everyone on the team like very

## 44510:00 - 44585:00

expensive coding agent um subscriptions

## 44585:00 - 44610:00

or you get an extra headcount right

## 44610:00 - 44645:00

let's say it's like maybe like um and

## 44645:00 - 44690:00

and almost everyone could say the

## 44690:00 - 44730:00

managers could say headcount but if you

## 44730:00 - 44765:00

ask VP level or like someone who manage

## 44765:00 - 44795:00

a lot of teams they could say just like

## 44795:00 - 44835:00

they would want AI assistant assistance

## 44835:00 - 44865:00

tools and the reason is that people say

## 44865:00 - 44900:00

like okay because as managers right

## 44900:00 - 44930:00

because you are still growing like

## 44930:00 - 44955:00

you're not as a level when you you

## 44955:00 - 44980:00

manage hundreds of thousands of people

## 44980:00 - 45020:00

so for you like having one HR hash count

## 45020:00 - 45065:00

is like is big so you want that not for

## 45065:00 - 45090:00

productivity reasons but because you

## 45090:00 - 45115:00

just want you have more people working

## 45115:00 - 45155:00

for you. Whereas for executive, you care

## 45155:00 - 45205:00

more about like the um the maybe you

## 45205:00 - 45240:00

have more like business metrics that you

## 45240:00 - 45275:00

care about. So so you actually think

## 45275:00 - 45320:00

about like what actually drive drive

## 45320:00 - 45370:00

productivity uh metrics for you. Uh so

## 45370:00 - 45415:00

so yeah, so it's tricky. Um and I think

## 45415:00 - 45435:00

that's like the question of like

## 45435:00 - 45460:00

productivity.

## 45460:00 - 45505:00

um it's not I'm not sure it's like

## 45505:00 - 45540:00

fundamentally is the some people are

## 45540:00 - 45560:00

more productive but it's just like we

## 45560:00 - 45595:00

don't have a good way of measuring

## 45595:00 - 45640:00

productivity improvement. Uh another

## 45640:00 - 45690:00

thing is also varies wily um and I think

## 45690:00 - 45730:00

that people do tell me that they notice

## 45730:00 - 45760:00

different buckets of of employees like

## 45760:00 - 45815:00

different reactions to AI assisted tools

## 45815:00 - 45845:00

like first of all I keep going back to

## 45845:00 - 45885:00

coding because it's big and it's like

## 45885:00 - 45935:00

easier to like reason about um so it

## 45935:00 - 45970:00

says like um I have different reports

## 45970:00 - 46010:00

like one team would tell me that like um

## 46010:00 - 46045:00

one of the people tell me okay amongst

## 46045:00 - 46085:00

all his engineers he think it's like

## 46085:00 - 46115:00

senior engineers would get the most

## 46115:00 - 46145:00

output like would be more productive

## 46145:00 - 46175:00

because it's like okay so that person

## 46175:00 - 46200:00

very interesting so so he actually

## 46200:00 - 46245:00

divided his team to like three bucket

## 46245:00 - 46275:00

but he didn't tell them obviously he was

## 46275:00 - 46310:00

like okay here's more like currently

## 46310:00 - 46350:00

like u best performing average

## 46350:00 - 46385:00

performing and lowest performing and

## 46385:00 - 46415:00

then there's a randomized trial so like

## 46415:00 - 46455:00

they give like half of each of each

## 46455:00 - 46505:00

group like access to like to like cursor

## 46505:00 - 46540:00

and then was noticed like over time was

## 46540:00 - 46575:00

like okay the something funny like the

## 46575:00 - 46605:00

the group that get the biggest

## 46605:00 - 46635:00

performance boost like in his opinion.

## 46635:00 - 46665:00

So it goes very close to his team as the

## 46665:00 - 46685:00

biggest boom Bruce like is the senior

## 46685:00 - 46715:00

engineer the highest performing. So the

## 46715:00 - 46740:00

highest performing engineer get the

## 46740:00 - 46770:00

biggest boost out of it and then the

## 46770:00 - 46825:00

second group is just like the um the

## 46825:00 - 46865:00

average performing. So so he so his

## 46865:00 - 46900:00

opinion is like okay the highest

## 46900:00 - 46930:00

performing engineers they also more

## 46930:00 - 46965:00

proactive they say know how to solve

## 46965:00 - 46990:00

problem. So AI helps them to solve

## 46990:00 - 47020:00

problem better. Whereas the people who

## 47020:00 - 47075:00

are lowest performing they only don't

## 47075:00 - 47110:00

care much about work right? So like it's

## 47110:00 - 47155:00

easier to just like go on autopilot get

## 47155:00 - 47185:00

it to like generate like bad code and

## 47185:00 - 47210:00

just like do it and I just don't know

## 47210:00 - 47250:00

what to do with it. As another company

## 47250:00 - 47285:00

however they told me just like actually

## 47285:00 - 47310:00

senior engineers are the one most

## 47310:00 - 47370:00

resistant to like using AI as tooling

## 47370:00 - 47410:00

because they said it's like okay but AI

## 47410:00 - 47440:00

because they are more opinionated and

## 47440:00 - 47465:00

they have very high standard was like

## 47465:00 - 47515:00

okay but AI code jet code just sucks. So

## 47515:00 - 47545:00

just like very very resistant in using

## 47545:00 - 47585:00

this. So I don't know I I haven't quite

## 47585:00 - 47620:00

be able to reconcile like very different

## 47620:00 - 47650:00

reports on that yet.

## 47650:00 - 47690:00

>> This is so interesting. So just to make

## 47690:00 - 47720:00

sure I'm hearing what you're the story.

## 47720:00 - 47755:00

So there's a company work with that did

## 47755:00 - 47790:00

a three bucket test with their

## 47790:00 - 47830:00

engineering team where they created

## 47830:00 - 47870:00

three sorts of groups. The highest

## 47870:00 - 47900:00

performing engineers, mid-performing

## 47900:00 - 47945:00

engineers, lowest performing engineers

## 47945:00 - 47985:00

uh and gave some of them so they gave

## 47985:00 - 48020:00

some of them access to say cursor. Was

## 48020:00 - 48035:00

it cursor or what did they give them

## 48035:00 - 48050:00

access to? It was cursor.

## 48050:00 - 48075:00

>> I think by then it was cursor.

## 48075:00 - 48095:00

>> Okay, cool. And so

## 48095:00 - 48120:00

>> I didn't work with them. This more like

## 48120:00 - 48135:00

a friend company.

## 48135:00 - 48170:00

>> Okay. It's a friends company. So do they

## 48170:00 - 48200:00

give like half of the higher performing

## 48200:00 - 48230:00

engineers cursor and half not or how did

## 48230:00 - 48245:00

they do the split?

## 48245:00 - 48270:00

>> Yeah. So like they give like half of the

## 48270:00 - 48295:00

entire company but like half for each

## 48295:00 - 48330:00

bucket. Yeah. And then they observe the

## 48330:00 - 48355:00

difference in like productivity.

## 48355:00 - 48370:00

>> I see. Yeah.

## 48370:00 - 48390:00

>> So how do they even do that? They're

## 48390:00 - 48420:00

just like okay you get cursor, you don't

## 48420:00 - 48445:00

get cursors. That how did they do that?

## 48445:00 - 48455:00

That's so interesting.

## 48455:00 - 48475:00

>> Yeah. I I didn't again just the

## 48475:00 - 48510:00

mechanics of it. Uh but but I was like

## 48510:00 - 48545:00

at Raspia for doing a randomized trial.

## 48545:00 - 48570:00

>> That is so cool. Yeah.

## 48570:00 - 48605:00

>> Okay. Wow. How large was this

## 48605:00 - 48625:00

engineering team? Was it like hundreds

## 48625:00 - 48635:00

of people?

## 48635:00 - 48660:00

>> Um it's it's not that large. It's about

## 48660:00 - 48720:00

like maybe um 30 40. Yeah.

## 48720:00 - 48745:00

>> 30 to 40. Okay. Yeah.

## 48745:00 - 48790:00

>> Wow. Okay. So they found that the

## 48790:00 - 48830:00

highest performing engineers had the

## 48830:00 - 48875:00

most benefit from using AI tools and

## 48875:00 - 48910:00

then behind them was the middle tier

## 48910:00 - 48945:00

engineers and the worst performers

## 48945:00 - 48985:00

>> were the lowest performers. Okay.

## 48985:00 - 49025:00

>> But also not the same everywhere. Um

## 49025:00 - 49065:00

like companies Yeah. Yeah. different.

## 49065:00 - 49090:00

>> Right. This other example you shared of

## 49090:00 - 49125:00

just senior engineers in this one

## 49125:00 - 49160:00

example are most resistant to changing

## 49160:00 - 49200:00

the way they work which I get. I I do

## 49200:00 - 49245:00

feel like the most valuable people right

## 49245:00 - 49300:00

now other than ML researchers uh and AI

## 49300:00 - 49335:00

researchers like yourself are senior

## 49335:00 - 49370:00

engineers because it feels like junior

## 49370:00 - 49405:00

engineers are just like so much of this

## 49405:00 - 49445:00

is now done by AI but an engineer that

## 49445:00 - 49460:00

knows what they're doing that

## 49460:00 - 49500:00

understands how things work at a large

## 49500:00 - 49550:00

scale with AI tools just basically like

## 49550:00 - 49580:00

infinite junior engineers doing their

## 49580:00 - 49625:00

bidding feels like an extremely valuable

## 49625:00 - 49650:00

and powerful asset.

## 49650:00 - 49680:00

>> Yeah. Uh I definitely like really

## 49680:00 - 49715:00

appreciate as you see companies like we

## 49715:00 - 49780:00

appreciate engineers who are um have a

## 49780:00 - 49810:00

good understanding of the whole systems

## 49810:00 - 49845:00

and be able to have good problem solving

## 49845:00 - 49880:00

skill like thinking holistically instead

## 49880:00 - 49925:00

of like local uh locally um when our

## 49925:00 - 49950:00

company have seen as the way they work

## 49950:00 - 49975:00

as they told me they work completely

## 49975:00 - 50000:00

different now I like so they actually

## 50000:00 - 50035:00

restructured engineering arc so that

## 50035:00 - 50060:00

like they get more senior engineer

## 50060:00 - 50090:00

should be more in the PR review because

## 50090:00 - 50125:00

they like to get like sort of writing

## 50125:00 - 50145:00

guidelines on like what is a good

## 50145:00 - 50185:00

engineering practices. Um what is a

## 50185:00 - 50210:00

process would be like they be like okay

## 50210:00 - 50235:00

so they write like a lot of like

## 50235:00 - 50290:00

processes uh on how to work well and

## 50290:00 - 50330:00

then they um and then they have more

## 50330:00 - 50370:00

more junior engineers just like produce

## 50370:00 - 50425:00

code and and like submit PR but senior

## 50425:00 - 50460:00

engineer more in the reviewing case. So

## 50460:00 - 50490:00

I think is it might be prepare for the

## 50490:00 - 50515:00

future. So another company actually told

## 50515:00 - 50550:00

me something very similar. So that kind

## 50550:00 - 50580:00

preparing the future when they only need

## 50580:00 - 50610:00

a very small

## 50610:00 - 50655:00

group of like very very strong engineers

## 50655:00 - 50705:00

to like create like processes and like

## 50705:00 - 50745:00

reviewing code to get into production

## 50745:00 - 50785:00

but I get like AI or like junior

## 50785:00 - 50815:00

engineers should like produce code but

## 50815:00 - 50860:00

then the question becomes like how does

## 50860:00 - 50890:00

one become a very strong

## 50890:00 - 50920:00

>> right that's right that's right I feel

## 50920:00 - 50950:00

like

## 50950:00 - 50970:00

>> yeah so so I don't know what's the

## 50970:00 - 51020:00

process was thinking about like yeah um

## 51020:00 - 51050:00

>> no one's thinking It's just it's a

## 51050:00 - 51090:00

problem. We won't have any more in 10 20

## 51090:00 - 51120:00

years. There'll be no more engineers

## 51120:00 - 51140:00

because no one's hiring junior

## 51140:00 - 51165:00

engineers. Although I could make the

## 51165:00 - 51185:00

case junior engineers, people just

## 51185:00 - 51210:00

getting into computer science right now

## 51210:00 - 51260:00

are just native AI native. And in

## 51260:00 - 51305:00

theory, you could argue they will become

## 51305:00 - 51335:00

really good really fast if they're

## 51335:00 - 51380:00

curious, aren't just, you know,

## 51380:00 - 51420:00

delegating learning and thinking to AI,

## 51420:00 - 51450:00

but learning how to actually using it to

## 51450:00 - 51475:00

learn how to code well and architect

## 51475:00 - 51505:00

correctly. like you could argue they

## 51505:00 - 51540:00

will be the most successful engineers in

## 51540:00 - 51555:00

the future.

## 51555:00 - 51585:00

>> I do think that what I mentioned is like

## 51585:00 - 51625:00

loading to architect um I think I I

## 51625:00 - 51660:00

group that in like system thinking I do

## 51660:00 - 51700:00

think it's very important skill because

## 51700:00 - 51740:00

I think AI can help automate a lot of

## 51740:00 - 51800:00

like um destroy the skills but like

## 51800:00 - 51835:00

knowing how to like utilize the skills

## 51835:00 - 51890:00

together to solve a problems is is very

## 51890:00 - 51935:00

uh it's is it's hard. So there's a a

## 51935:00 - 52000:00

webinar between um Mer Sami who was my

## 52000:00 - 52035:00

one of my favorite professors. He was a

## 52035:00 - 52070:00

chair of the curriculum of the CS

## 52070:00 - 52095:00

department at Stford. We spend a lot of

## 52095:00 - 52135:00

time thinking about CIS educations right

## 52135:00 - 52160:00

like what what what should students

## 52160:00 - 52210:00

learn nowaday like AI coding and then

## 52210:00 - 52245:00

the other person is like Andrew which is

## 52245:00 - 52280:00

of course it's like a legend in the AI

## 52280:00 - 52330:00

space and NAMI person like Sami said

## 52330:00 - 52355:00

something very interesting is like he

## 52355:00 - 52380:00

said like a lot of people think that CS

## 52380:00 - 52415:00

is about coding but it's not like coding

## 52415:00 - 52460:00

is just a means to an end like CS is

## 52460:00 - 52500:00

about system thinking like using like

## 52500:00 - 52535:00

coding to solve actual problem and

## 52535:00 - 52585:00

problem solving will never go way

## 52585:00 - 52610:00

because like what like AI can automate

## 52610:00 - 52640:00

more stuff the problem just get bigger

## 52640:00 - 52680:00

but like the process of understanding

## 52680:00 - 52720:00

what cause the issue and like how to

## 52720:00 - 52765:00

like design step-by-step solution to it

## 52765:00 - 52805:00

will always be there um so I think an

## 52805:00 - 52850:00

example of um of like I actually have a

## 52850:00 - 52890:00

lot of issues with like AI for like um

## 52890:00 - 52940:00

in the way of like is debugging so I'm

## 52940:00 - 52960:00

not sure you use a lot of air for coding

## 52960:00 - 53005:00

but like something I've noticed and also

## 53005:00 - 53030:00

seen from my friends it's like it is

## 53030:00 - 53055:00

pretty good when you have very clear

## 53055:00 - 53090:00

welldefy task maybe write do re

## 53090:00 - 53115:00

documentations

## 53115:00 - 53155:00

fixes specific features or like build an

## 53155:00 - 53190:00

app from scratch right like doesn't have

## 53190:00 - 53215:00

to interact with a large existing code

## 53215:00 - 53245:00

base but it added something like a

## 53245:00 - 53280:00

little bit more complicated um maybe

## 53280:00 - 53295:00

require interacting with a lot of

## 53295:00 - 53330:00

components and stuff is usually like not

## 53330:00 - 53375:00

that good um and and for example like I

## 53375:00 - 53420:00

was using AI to like use um to deploy an

## 53420:00 - 53465:00

applications um and I was testing out a

## 53465:00 - 53500:00

new uh hosting service I was not

## 53500:00 - 53530:00

familiar with I was like okay like

## 53530:00 - 53555:00

usually they for me so what they think

## 53555:00 - 53590:00

AI does give me is like confidence to

## 53590:00 - 53620:00

try new tool like before with AI is like

## 53620:00 - 53640:00

trying new tools has a lot of

## 53640:00 - 53670:00

documentations for the beginning but I

## 53670:00 - 53705:00

was like okay just try it out and and

## 53705:00 - 53735:00

learn. So I was testing out this new

## 53735:00 - 53775:00

hosting service and it kept getting a

## 53775:00 - 53810:00

bug. It was like very very annoying and

## 53810:00 - 53850:00

I was like okay I asked uh car codes

## 53850:00 - 53880:00

like fix it and it keep g keeping like

## 53880:00 - 53910:00

it keep changing the way like maybe

## 53910:00 - 53955:00

change environment variable fix the code

## 53955:00 - 53985:00

maybe I change from the function to this

## 53985:00 - 54030:00

function maybe change the language maybe

## 54030:00 - 54065:00

it doesn't process JavaScript well I

## 54065:00 - 54100:00

don't know whatever and it didn't work

## 54100:00 - 54135:00

and I was like okay that's it I'm just

## 54135:00 - 54170:00

going to read the document document uh

## 54170:00 - 54195:00

documentation myself and see what's

## 54195:00 - 54240:00

wrong and it turns out it's like I'm on

## 54240:00 - 54280:00

another tier like the fish I want did

## 54280:00 - 54310:00

not is not available in this tier.

## 54310:00 - 54345:00

Right? So I feel like okay so the issue

## 54345:00 - 54385:00

with clon is trying to focus on fixing

## 54385:00 - 54415:00

things from a very a different component

## 54415:00 - 54440:00

where the issue is from a different

## 54440:00 - 54470:00

component. So I think I think of like

## 54470:00 - 54500:00

okay be understanding like how different

## 54500:00 - 54550:00

components um work together and where

## 54550:00 - 54580:00

the source of issue might come from you

## 54580:00 - 54605:00

need to you need to have a holistic view

## 54605:00 - 54630:00

of it and this made me think is like

## 54630:00 - 54665:00

okay how do we teach AI like system

## 54665:00 - 54690:00

thinking like like that right I think I

## 54690:00 - 54725:00

have all the human experts like having

## 54725:00 - 54780:00

like right like very much built scaffold

## 54780:00 - 54805:00

uh just like okay for this kind of

## 54805:00 - 54835:00

problem look into this look into that

## 54835:00 - 54870:00

look into that and then stuff so so I

## 54870:00 - 54900:00

think is that could be one way but also

## 54900:00 - 54925:00

made me think is like how do we teach

## 54925:00 - 54980:00

humans like system thinking. Um yeah, so

## 54980:00 - 55000:00

so yeah. So I think it's very

## 55000:00 - 55050:00

interesting um skill. I I do think it's

## 55050:00 - 55065:00

very important.

## 55065:00 - 55100:00

>> That's exactly the same insight Brett

## 55100:00 - 55135:00

Taylor shared on the podcast. He's the

## 55135:00 - 55165:00

co-founder of Sierra. He created Google

## 55165:00 - 55205:00

Maps. He was CEO of Salesforce, Quip, a

## 55205:00 - 55225:00

few other things. And I asked him just

## 55225:00 - 55255:00

like should people learn to code? And

## 55255:00 - 55280:00

his point is exactly what you said,

## 55280:00 - 55305:00

which is learning taking computer

## 55305:00 - 55340:00

science classes is not about learning

## 55340:00 - 55385:00

Java and Python. It's learning how

## 55385:00 - 55445:00

systems work and how code operates and

## 55445:00 - 55490:00

how software works broadly, not just

## 55490:00 - 55535:00

here's like a function to do a thing.

## 55535:00 - 55570:00

One thing that I wanted to help people

## 55570:00 - 55595:00

understand, you you wrote this book

## 55595:00 - 55620:00

called AI engineering, which is

## 55620:00 - 55645:00

essentially helping people understand

## 55645:00 - 55695:00

this new genre of engineer. And you have

## 55695:00 - 55720:00

this really simple way of thinking about

## 55720:00 - 55755:00

the difference between an ML engineer

## 55755:00 - 55795:00

and an AI engineer which has a really

## 55795:00 - 55840:00

good correlary to product managers now

## 55840:00 - 55870:00

of just like an AI product manager

## 55870:00 - 55910:00

versus a non-AI product manager. The way

## 55910:00 - 55930:00

you describe it and fill in what I'm

## 55930:00 - 55975:00

missing is just ML engineers built

## 55975:00 - 56025:00

models themselves. AI engineers use

## 56025:00 - 56070:00

existing models to build products.

## 56070:00 - 56095:00

Anything you want to add there? One

## 56095:00 - 56135:00

thing I really dislike about writing

## 56135:00 - 56180:00

books is that you have to defy like this

## 56180:00 - 56210:00

and and I think it's like no definition

## 56210:00 - 56235:00

to be perfect because they always be

## 56235:00 - 56270:00

like edge cases. Um but yeah in general

## 56270:00 - 56315:00

I think it's like just like gen like AI

## 56315:00 - 56350:00

as a service like more as a service like

## 56350:00 - 56375:00

when somebody build the models for you

## 56375:00 - 56420:00

and the base model performance is a

## 56420:00 - 56450:00

pretty shock. So, so it's like it's

## 56450:00 - 56480:00

enable people to just like okay now I

## 56480:00 - 56530:00

want she in integrate AI into my product

## 56530:00 - 56575:00

I don't need to learn what green is even

## 56575:00 - 56605:00

though knowing that could really help uh

## 56605:00 - 56630:00

but but yeah it's like it makes the

## 56630:00 - 56660:00

entry barrier really low for people who

## 56660:00 - 56715:00

want to use AI to build product and at

## 56715:00 - 56760:00

the same time AI capabilities are like

## 56760:00 - 56800:00

so strong like it's also like increase

## 56800:00 - 56835:00

like the possibilities like the type

## 56835:00 - 56870:00

applications that AI can be used for so

## 56870:00 - 56895:00

I think like yeah so like both entry

## 56895:00 - 56925:00

barriers like super low and like the

## 56925:00 - 56955:00

demand And for like a applications like

## 56955:00 - 56990:00

a lot bigger. So it feels very very

## 56990:00 - 57035:00

exciting. It opens up like a whole new

## 57035:00 - 57070:00

world of possibilities.

## 57070:00 - 57095:00

>> Oh yeah. It's like now you don't have to

## 57095:00 - 57120:00

time you don't even have to spend time

## 57120:00 - 57145:00

building this AI brain. Now you can just

## 57145:00 - 57195:00

use it to do stuff. Uh such a such an

## 57195:00 - 57235:00

unlock. Okay. Maybe just a vital

## 57235:00 - 57295:00

question. You get to see a lot of where

## 57295:00 - 57320:00

what's working, what's not working,

## 57320:00 - 57350:00

where things are heading. I'm curious

## 57350:00 - 57385:00

just if you had to think about in the

## 57385:00 - 57405:00

next two or three years just where

## 57405:00 - 57440:00

things are heading. What do you think

## 57440:00 - 57470:00

what do you think how do you think

## 57470:00 - 57515:00

building products will be different? How

## 57515:00 - 57545:00

do you think companies working will be

## 57545:00 - 57575:00

different? If you had to think of maybe

## 57575:00 - 57615:00

the biggest change we expect to see in

## 57615:00 - 57645:00

the next few years in terms of how

## 57645:00 - 57670:00

companies work.

## 57670:00 - 57710:00

>> I think in a lot of organizations they

## 57710:00 - 57765:00

don't move that fast, right? Um but at

## 57765:00 - 57800:00

the same time they also move faster than

## 57800:00 - 57850:00

I expected. uh because again I think

## 57850:00 - 57880:00

it's like biased like and don't work

## 57880:00 - 57915:00

with dinosaur companies don't care like

## 57915:00 - 57950:00

a lot of executive who comes to me are

## 57950:00 - 57990:00

like very forwardlooking so maybe for me

## 57990:00 - 58025:00

I'm very biased uh towards towards like

## 58025:00 - 58085:00

organization just like move fast um so

## 58085:00 - 58140:00

so yeah so I think one big change I see

## 58140:00 - 58185:00

is just like in organizational structure

## 58185:00 - 58215:00

um I think it's like a lot of value

## 58215:00 - 58270:00

place um in like um so before like we

## 58270:00 - 58295:00

have like a lot of disjointed team like

## 58295:00 - 58320:00

we have very clear like engineering ing

## 58320:00 - 58355:00

team, product team. But then there's a

## 58355:00 - 58390:00

question of like who should write Eva,

## 58390:00 - 58420:00

right? Like who should own the matrix?

## 58420:00 - 58470:00

And it turns out it's like Eva is not a

## 58470:00 - 58495:00

um it's not a it's not a separate

## 58495:00 - 58520:00

problem. It's a system problem, right?

## 58520:00 - 58555:00

Because you you you need to look into

## 58555:00 - 58580:00

different components how interest each

## 58580:00 - 58610:00

other. You need user behaviors because

## 58610:00 - 58630:00

you need to know what users care about

## 58630:00 - 58670:00

so that you can so that you can like

## 58670:00 - 58705:00

write write about like reflect what

## 58705:00 - 58740:00

users care about. So, so all of that

## 58740:00 - 58760:00

like you can sort it from like you know

## 58760:00 - 58780:00

look into different component

## 58780:00 - 58830:00

architectures uh place guardrails and

## 58830:00 - 58855:00

stuff. So it's just engineering but

## 58855:00 - 58890:00

understanding users is like what product

## 58890:00 - 58915:00

right so so because of like a lot of

## 58915:00 - 58945:00

things and they are extremely important.

## 58945:00 - 58985:00

So like that guy bring product team and

## 58985:00 - 59010:00

like engineering team even like

## 59010:00 - 59040:00

marketing team like user acquisition

## 59040:00 - 59080:00

like very close to each other so so yeah

## 59080:00 - 59110:00

since in a way people are structuring so

## 59110:00 - 59140:00

that's more communications between like

## 59140:00 - 59185:00

previously very distinct functions.

## 59185:00 - 59240:00

Another thing is I also see as teams um

## 59240:00 - 59280:00

of course like think about like what can

## 59280:00 - 59320:00

be automated in the next few years and

## 59320:00 - 59355:00

what what cannot be automated and I see

## 59355:00 - 59395:00

that people already like shedding like

## 59395:00 - 59435:00

actually is it's a little bit like scary

## 59435:00 - 59465:00

to think about it but I also think it's

## 59465:00 - 59505:00

like the team told me it's like okay

## 59505:00 - 59525:00

this is between you and me but we have

## 59525:00 - 59560:00

we like got rid of these functions right

## 59560:00 - 59585:00

like for a lot of thing like uh

## 59585:00 - 59615:00

previously outsource for example like

## 59615:00 - 59645:00

traditionally is a business outsourcing

## 59645:00 - 59690:00

this core to them and like can done with

## 59690:00 - 59765:00

like not um can be a more um system uh

## 59765:00 - 59815:00

um systematized um so so with that you

## 59815:00 - 59850:00

can actually like use AI like automate a

## 59850:00 - 59880:00

lot of that and also like a separation

## 59880:00 - 59905:00

think more like what is the value of

## 59905:00 - 59935:00

like junior engineers or like senior

## 59935:00 - 59960:00

engineers how you restructure

## 59960:00 - 60010:00

engineering for that um so so yeah so I

## 60010:00 - 60050:00

do definitely think that um is one thing

## 60050:00 - 60075:00

to success organization people are just

## 60075:00 - 60110:00

moving pieces around and like thinking

## 60110:00 - 60155:00

about like use cases um whether you need

## 60155:00 - 60190:00

to like spin out new use cases and who

## 60190:00 - 60250:00

would lead a new effort and like yeah um

## 60250:00 - 60315:00

that is one big uh change. Another

## 60315:00 - 60350:00

things in ter of like AI, I think this

## 60350:00 - 60410:00

is um I'm not sure how true this is. Um

## 60410:00 - 60455:00

I guess I'm I'm also like on the camp of

## 60455:00 - 60515:00

like thinking that is has merit is it's

## 60515:00 - 60570:00

a camp of like okay uh base models we

## 60570:00 - 60610:00

have probably like not quite max out but

## 60610:00 - 60675:00

we want we unlikely to see like really

## 60675:00 - 60730:00

really strong like craziness strong

## 60730:00 - 60750:00

models. So like you remember like when

## 60750:00 - 60790:00

we have like GBT right then GB2 which is

## 60790:00 - 60825:00

a big step up like an order of magnitude

## 60825:00 - 60865:00

like like better than like GBD and then

## 60865:00 - 60910:00

GB3 which like much much bigger GB4 much

## 60910:00 - 60940:00

much bigger and then of course I have

## 60940:00 - 61000:00

GBD 5 but like is GB 5 like that scale

## 61000:00 - 61055:00

of like much bigger like a step jump

## 61055:00 - 61085:00

compared to like the previous I think

## 61085:00 - 61120:00

it's a debatable right so so I think

## 61120:00 - 61140:00

that it's like we had reached a point

## 61140:00 - 61205:00

where like the base model um performance

## 61205:00 - 61240:00

improvement is not going to be like

## 61240:00 - 61285:00

mind-blowing it was in the last three

## 61285:00 - 61325:00

years uh so so I think it's like a lot

## 61325:00 - 61355:00

of like improvements we're going to see

## 61355:00 - 61400:00

in the post training phase in the

## 61400:00 - 61460:00

application building phase um and um and

## 61460:00 - 61490:00

yes also I think that's where I feel I

## 61490:00 - 61545:00

was see a lot of improvement there so

## 61545:00 - 61585:00

very like interesting like multimodality

## 61585:00 - 61635:00

um so we've seen a lot of uh text based

## 61635:00 - 61685:00

uh but I think there a lot of um audio

## 61685:00 - 61735:00

videos use cases uh that is very very

## 61735:00 - 61780:00

exciting and I think audio is not quite

## 61780:00 - 61815:00

as soft as thinking because I do work

## 61815:00 - 61855:00

with like with with like a couple of

## 61855:00 - 61905:00

like voice startups and when I talk to

## 61905:00 - 61940:00

think about voice it's a entirely

## 61940:00 - 61980:00

different beast uh so let's say have

## 61980:00 - 62015:00

chatbot right we go from a text chatbot

## 62015:00 - 62055:00

to voice chatbot it's like the consoles

## 62055:00 - 62080:00

are completely different because now

## 62080:00 - 62105:00

with voice chatbot right we need to

## 62105:00 - 62130:00

think about like latency because like

## 62130:00 - 62170:00

multiple steps uh first like like text

## 62170:00 - 62215:00

like like voice to text text to text and

## 62215:00 - 62245:00

text question into text answer and then

## 62245:00 - 62280:00

like and then text to voice answer right

## 62280:00 - 62315:00

so it's like manable hops and like

## 62315:00 - 62345:00

latency become very important and

## 62345:00 - 62375:00

there's a question like what does make

## 62375:00 - 62415:00

you sound natural so for example like

## 62415:00 - 62470:00

people think like um in in in AI and

## 62470:00 - 62495:00

humans so like when humans talk to each

## 62495:00 - 62550:00

other like if I say if I say you try to

## 62550:00 - 62585:00

interrupt me it's like um chip that

## 62585:00 - 62625:00

right I would like pause and I try to

## 62625:00 - 62665:00

hear you out right but sometime I may

## 62665:00 - 62705:00

just say say some word not like

## 62705:00 - 62750:00

acknowledge when I mhm that I shouldn't

## 62750:00 - 62785:00

stop I just continue so the question of

## 62785:00 - 62815:00

like force interruption like whether

## 62815:00 - 62860:00

it's like I should should I stop or not

## 62860:00 - 62890:00

like it's is a big and like what

## 62890:00 - 62930:00

perceived as like natural conversations

## 62930:00 - 62955:00

and that's also regulations right

## 62955:00 - 62990:00

because like because like a lot of time

## 62990:00 - 63025:00

people want to build AI chatbot voice

## 63025:00 - 63055:00

chat bots that sound like humans try to

## 63055:00 - 63100:00

like trick users into thinking they're

## 63100:00 - 63130:00

talking to humans but also of like maybe

## 63130:00 - 63155:00

potential regulations saying like okay

## 63155:00 - 63205:00

you have to disclose to users when to

## 63205:00 - 63265:00

talk if the if the bot is talking to is

## 63265:00 - 63305:00

human or um or AI. So, so I think just

## 63305:00 - 63345:00

like um there's a whole space I think

## 63345:00 - 63385:00

it's not quite as so as as you think is

## 63385:00 - 63445:00

it but it's al it's not quite like an AI

## 63445:00 - 63475:00

foundation model problem right because

## 63475:00 - 63510:00

like a human interruption detection is

## 63510:00 - 63540:00

actually a classical machineing problem

## 63540:00 - 63575:00

like you you it's is a different uh

## 63575:00 - 63620:00

framing but like you can view classifier

## 63620:00 - 63660:00

for that or or like the question of like

## 63660:00 - 63685:00

let's see actually have a massive

## 63685:00 - 63735:00

engineuric challenge not an AI challenge

## 63735:00 - 63755:00

of course it can be an AI challenge

## 63755:00 - 63780:00

because people are trying to build like

## 63780:00 - 63815:00

voicetovoice model. So instead of having

## 63815:00 - 63855:00

like having to first like transcribe the

## 63855:00 - 63895:00

voice from me into text and then get a

## 63895:00 - 63920:00

model generous text answer and get

## 63920:00 - 63965:00

another model to like turn from text to

## 63965:00 - 63990:00

speech, you just like voice your voice

## 63990:00 - 64020:00

directly. So that is something who are

## 64020:00 - 64065:00

working on but it's like very hard. Um

## 64065:00 - 64100:00

yeah. So so yeah. So like even audio I

## 64100:00 - 64125:00

think of it is like the easier than

## 64125:00 - 64165:00

video right because video have like both

## 64165:00 - 64205:00

image and voice. Uh it's already like

## 64205:00 - 64235:00

pretty hard. So I think it's a lot of

## 64235:00 - 64265:00

challenges in that space.

## 64265:00 - 64300:00

That was an awesome list of things. Let

## 64300:00 - 64330:00

me mirror them back real quick. So what

## 64330:00 - 64350:00

you're predicting in the next few years,

## 64350:00 - 64385:00

things that will change in the way we

## 64385:00 - 64430:00

work and these actually resonate with so

## 64430:00 - 64450:00

many conversations I've had on this

## 64450:00 - 64485:00

podcast. So this is just kind of

## 64485:00 - 64515:00

doubling doubling down on where things

## 64515:00 - 64545:00

are heading. One is the blurring of

## 64545:00 - 64570:00

lines between different functions

## 64570:00 - 64610:00

instead of just like design engineering.

## 64610:00 - 64635:00

Everyone's going to be doing a lot of

## 64635:00 - 64675:00

different things now. Uh, two is just

## 64675:00 - 64710:00

more of work being automated with agents

## 64710:00 - 64755:00

and all these AI tools and just in

## 64755:00 - 64800:00

theory productivity going up. Third is a

## 64800:00 - 64840:00

shifting from pre-training models to

## 64840:00 - 64865:00

post-training fine-tuning and things

## 64865:00 - 64905:00

like that because to your point model

## 64905:00 - 64940:00

models maybe are slowing down and how

## 64940:00 - 64965:00

smart they're getting. Although I'll

## 64965:00 - 64995:00

point folks to the ed chat with the

## 64995:00 - 65015:00

co-founder of Anthropic. He made a

## 65015:00 - 65045:00

really good point here. He's like we're

## 65045:00 - 65070:00

really bad at understanding what

## 65070:00 - 65100:00

exponentials feel like when we're in the

## 65100:00 - 65130:00

middle of that. And also models are

## 65130:00 - 65165:00

being released more often. So the

## 65165:00 - 65190:00

difference between them we may not

## 65190:00 - 65210:00

notice because they're just happening

## 65210:00 - 65245:00

more often versus GPT3 came out like a

## 65245:00 - 65300:00

year I don't know a before after JPT2.

## 65300:00 - 65345:00

So uh maybe true maybe not. And then the

## 65345:00 - 65370:00

fourth point you made is this idea of

## 65370:00 - 65405:00

multimodal investing in multimodal

## 65405:00 - 65445:00

experiences. I cannot wait for JPT voice

## 65445:00 - 65480:00

mode to get better at interruption. Like

## 65480:00 - 65500:00

exactly what you're saying. I'm just

## 65500:00 - 65520:00

like talking to it and then someone

## 65520:00 - 65550:00

makes a little sound. It's like okay and

## 65550:00 - 65575:00

then you have to and then it's like and

## 65575:00 - 65605:00

then it stops talking. It's so annoying.

## 65605:00 - 65650:00

I'm shocked that we don't have better

## 65650:00 - 65685:00

voice assistant at home yet. I think I

## 65685:00 - 65720:00

have been testing out a bunch. Like I

## 65720:00 - 65750:00

keep hoping, oh my god, Zach could be

## 65750:00 - 65780:00

the one and then I know how many of them

## 65780:00 - 65800:00

I just like had to get away because

## 65800:00 - 65815:00

they're not that good.

## 65815:00 - 65840:00

>> I think it's coming. I hear it's coming.

## 65840:00 - 65870:00

Anthropic is working with someone uh

## 65870:00 - 65890:00

that I don't know if it's launched or

## 65890:00 - 65905:00

not yet.

## 65905:00 - 65940:00

>> Yeah, I want to bring back to what you

## 65940:00 - 65975:00

mentioned about like the your guest like

## 65975:00 - 66000:00

from Antropic mentioned about the

## 66000:00 - 66035:00

performance uh improvement. I think

## 66035:00 - 66075:00

there's a big change. Um I think like um

## 66075:00 - 66125:00

this difference between um a model based

## 66125:00 - 66150:00

capability so I'm not talking about like

## 66150:00 - 66190:00

the pre-trained model right versus a

## 66190:00 - 66235:00

perceived performance. So, so let's say

## 66235:00 - 66275:00

just like um a machine thought about

## 66275:00 - 66300:00

like are you familiar with the term test

## 66300:00 - 66330:00

time compute?

## 66330:00 - 66360:00

>> Uh I don't think so.

## 66360:00 - 66390:00

>> Yeah, help us understand. So um so so

## 66390:00 - 66425:00

the idea is like okay like um you have

## 66425:00 - 66455:00

some a fixed amount of compute, right?

## 66455:00 - 66475:00

So you're going to spend a lot of

## 66475:00 - 66510:00

compute on pre-shooting or training the

## 66510:00 - 66550:00

model pre-tuning and then have spend a

## 66550:00 - 66590:00

lot of uh some computing and the ratio

## 66590:00 - 66615:00

like pre-tuning to the post training

## 66615:00 - 66660:00

compute is like crazy varies different

## 66660:00 - 66705:00

between different lab um um and also

## 66705:00 - 66740:00

like since then has to spend comput uh

## 66740:00 - 66780:00

on like Jerry inference when I have a

## 66780:00 - 66820:00

train and 500 model now it want to like

## 66820:00 - 66850:00

serve to users so I might type a

## 66850:00 - 66885:00

questions or prompt and like Jerry like

## 66885:00 - 66920:00

do inference like and that requires a

## 66920:00 - 66945:00

compute and I guess I feel about

## 66945:00 - 66975:00

discussion of like uh should I spend

## 66975:00 - 67015:00

more compute on like pre-tuning or

## 67015:00 - 67055:00

fetuning or inference right because like

## 67055:00 - 67075:00

inference and people found I was just

## 67075:00 - 67115:00

like test time compute so like spending

## 67115:00 - 67150:00

more compute on inference is like call

## 67150:00 - 67190:00

like test time like u compute uh like

## 67190:00 - 67230:00

the strategy of like just allocating

## 67230:00 - 67265:00

more resources compute resource to

## 67265:00 - 67320:00

generate uh inference when I bring

## 67320:00 - 67340:00

better performance and how does that do

## 67340:00 - 67375:00

it like let's say um let's say you have

## 67375:00 - 67410:00

a math questions right and maybe instead

## 67410:00 - 67440:00

of just generic one answer I can gen

## 67440:00 - 67470:00

four different answers and say okay

## 67470:00 - 67520:00

whichever is uh the best according to

## 67520:00 - 67565:00

some standard uh or like okay have four

## 67565:00 - 67595:00

answers and then maybe like three of

## 67595:00 - 67640:00

them say 42 and one of them said like 20

## 67640:00 - 67665:00

okay three of them in the in in

## 67665:00 - 67700:00

agreement so the answer should be 42

## 67700:00 - 67715:00

right so like just people shouldn't

## 67715:00 - 67745:00

generate a bunch of it or another thing

## 67745:00 - 67775:00

is like a lot of time like reasoning uh

## 67775:00 - 67800:00

thinking just like people should like

## 67800:00 - 67835:00

generate more thickening tokens I spend

## 67835:00 - 67865:00

more time thinking before showing the

## 67865:00 - 67900:00

final answers uh it's like require more

## 67900:00 - 67935:00

compute but also like give it more uh

## 67935:00 - 67980:00

more and more more better performance.

## 67980:00 - 68010:00

So so yes. So so so I think it's like

## 68010:00 - 68055:00

from the user perspective right like

## 68055:00 - 68110:00

when the model spend more time exploring

## 68110:00 - 68140:00

different potential answers thinking

## 68140:00 - 68180:00

longer it can give you much better final

## 68180:00 - 68240:00

answers but the base model itself does

## 68240:00 - 68265:00

not change.

## 68265:00 - 68270:00

>> Awesome.

## 68270:00 - 68290:00

>> Does it make sense? Yes.

## 68290:00 - 68330:00

>> Yes. Absolutely. Uh that is a good

## 68330:00 - 68390:00

correlary to uh to Ben man's point.

## 68390:00 - 68425:00

>> Yeah. Chip, we covered a lot of ground.

## 68425:00 - 68450:00

I've gone through everything I was

## 68450:00 - 68485:00

hoping to learn and more. Before we get

## 68485:00 - 68510:00

to our very exciting lightning round, is

## 68510:00 - 68535:00

there anything else that you wanted to

## 68535:00 - 68555:00

share? Anything else you want to leave

## 68555:00 - 68570:00

listeners with?

## 68570:00 - 68600:00

>> So, I do work at a few companies that

## 68600:00 - 68635:00

does this things of like they want

## 68635:00 - 68670:00

employees to like come up with ideas.

## 68670:00 - 68705:00

So, there's a big debate on like what is

## 68705:00 - 68730:00

a better way for a strategy, right?

## 68730:00 - 68770:00

Should it be top down or like bottom up,

## 68770:00 - 68800:00

right? Should like executive come up

## 68800:00 - 68830:00

with like one or two like killer use

## 68830:00 - 68860:00

case and like everyone like allocate

## 68860:00 - 68890:00

resource to that or like should you give

## 68890:00 - 68930:00

engineers and PMs and smart people like

## 68930:00 - 68965:00

come up with ideas and I think it's a

## 68965:00 - 68990:00

mixture of both. So, so some companies

## 68990:00 - 69020:00

it was like okay we hire a bunch of

## 69020:00 - 69055:00

smart people like let's see like what

## 69055:00 - 69085:00

they come up with and they they organize

## 69085:00 - 69125:00

like hackathons or like internal

## 69125:00 - 69160:00

challenge to get people to to build

## 69160:00 - 69215:00

product and one things that um I noticed

## 69215:00 - 69245:00

is like a lot of people just like don't

## 69245:00 - 69290:00

know what to build uh and it shocked me

## 69290:00 - 69320:00

like why I feel like we are in some kind

## 69320:00 - 69355:00

like an idea crisis right now we have

## 69355:00 - 69390:00

all this really cool tools to have you

## 69390:00 - 69415:00

like do everything from scratch I can

## 69415:00 - 69445:00

have you like design it can have you

## 69445:00 - 69470:00

like write code it can have build

## 69470:00 - 69505:00

website. So in theory we should see a

## 69505:00 - 69535:00

lot more but at the same time people are

## 69535:00 - 69575:00

like somehow stuck like they don't know

## 69575:00 - 69615:00

what to build and and I think it's like

## 69615:00 - 69650:00

maybe a lot of had to do with like maybe

## 69650:00 - 69695:00

like um society expectations because

## 69695:00 - 69730:00

like we have gone through uh we have

## 69730:00 - 69755:00

gone into this phase of like

## 69755:00 - 69790:00

specializations like people like uh very

## 69790:00 - 69840:00

highly uh specialized and people are

## 69840:00 - 69870:00

supposed to do like focus on one thing

## 69870:00 - 69890:00

really well instead of like a big

## 69890:00 - 69915:00

picture and we don't have a big picture

## 69915:00 - 69945:00

of you. it's hard to come up with like

## 69945:00 - 69985:00

ideas of what to build. So, so I know

## 69985:00 - 70015:00

what like uh when when I work with this

## 70015:00 - 70040:00

company on this hackathon like we do

## 70040:00 - 70065:00

work out like a how come up with a

## 70065:00 - 70100:00

guideline like how to come up with ideas

## 70100:00 - 70125:00

and usually what we think of is like

## 70125:00 - 70175:00

okay like one tip is like go look from

## 70175:00 - 70215:00

the last week right like for a week just

## 70215:00 - 70240:00

like pay attention to what you do and

## 70240:00 - 70270:00

what frustrate you and when something

## 70270:00 - 70310:00

frustrate you think about like is there

## 70310:00 - 70345:00

anything we can do

## 70345:00 - 70370:00

is there like can you be done a

## 70370:00 - 70400:00

different way so it's not frustrating

## 70400:00 - 70430:00

and you can talk like people can swap

## 70430:00 - 70465:00

accept notebooks or teams and if you see

## 70465:00 - 70500:00

common frustrations maybe just something

## 70500:00 - 70525:00

you can think about like just to build

## 70525:00 - 70550:00

something around that. So yeah so I feel

## 70550:00 - 70585:00

like um just like notice like how we

## 70585:00 - 70615:00

work uh thinking of like ways to like

## 70615:00 - 70650:00

constantly ask questions like how can be

## 70650:00 - 70690:00

better and then I just build something

## 70690:00 - 70725:00

to like address the frustrations. I

## 70725:00 - 70745:00

think it's a good way to just like learn

## 70745:00 - 70770:00

and adopt AI.

## 70770:00 - 70800:00

>> I think people have felt exactly what

## 70800:00 - 70825:00

you're describing every time they open

## 70825:00 - 70850:00

up one of these vibe coding tools where

## 70850:00 - 70875:00

they could just describe anything you

## 70875:00 - 70900:00

want. I'm like I don't know what do I

## 70900:00 - 70940:00

want? And and I love this very tactical

## 70940:00 - 70960:00

piece of advice, just like what

## 70960:00 - 70980:00

frustrates you, just pay attention to

## 70980:00 - 71020:00

where you're frustrated. For example, I

## 71020:00 - 71050:00

just built a very cool little VIP coded

## 71050:00 - 71090:00

app. I was working on a newsletter post

## 71090:00 - 71150:00

inside Google Docs and I I pasted all

## 71150:00 - 71185:00

these images into the Google Doc from

## 71185:00 - 71215:00

screenshots and stuff and and then I

## 71215:00 - 71240:00

forgot, oh yeah, you can't take images

## 71240:00 - 71270:00

out of Google Docs. It's like this Hotel

## 71270:00 - 71290:00

California experience where you can

## 71290:00 - 71320:00

paste stuff into it. Very hard to get

## 71320:00 - 71355:00

images back out. So, I just went to all

## 71355:00 - 71390:00

the VIP coded tools and just build an

## 71390:00 - 71425:00

app that I can give you a Google doc URL

## 71425:00 - 71455:00

and it let me download all the images

## 71455:00 - 71485:00

automatically and it worked amazingly

## 71485:00 - 71510:00

well and it made it really cute and I'll

## 71510:00 - 71540:00

I'll link to it in the show notes.

## 71540:00 - 71565:00

>> Oh, I would love to see that. I do I'm

## 71565:00 - 71590:00

very bullish on like using AI just

## 71590:00 - 71625:00

create like micro tools like just

## 71625:00 - 71660:00

something just like make your life a bit

## 71660:00 - 71670:00

easier

## 71670:00 - 71710:00

>> and 100%. I feel like that's one of the

## 71710:00 - 71730:00

main ways people are using these tools

## 71730:00 - 71770:00

just like a little niche problem they

## 71770:00 - 71810:00

have. With that, Chip, we've reached our

## 71810:00 - 71855:00

very exciting lightning round. I've got

## 71855:00 - 71915:00

five questions for you. Are you ready?

## 71915:00 - 71945:00

>> Yeah. Always. No. No. Uh, depends on how

## 71945:00 - 71970:00

hard the questions are.

## 71970:00 - 72010:00

>> They're very consistent across every

## 72010:00 - 72045:00

guest. So, uh, I imagine you've heard

## 72045:00 - 72075:00

them before. First question, what are

## 72075:00 - 72105:00

two or three books that you find

## 72105:00 - 72150:00

yourself recommending most to other

## 72150:00 - 72205:00

people? O I'm really terrified of like

## 72205:00 - 72240:00

book recommendations because I feel like

## 72240:00 - 72260:00

what books a person should read really

## 72260:00 - 72285:00

depends on what they want and where they

## 72285:00 - 72315:00

in life and where they want to get to.

## 72315:00 - 72345:00

Uh but there's several books that I do

## 72345:00 - 72390:00

think is really change the way I think

## 72390:00 - 72415:00

and see the world. So one thing is a

## 72415:00 - 72455:00

selfish gene that's like understand uh

## 72455:00 - 72495:00

it actually changed uh it actually

## 72495:00 - 72515:00

helped me with the question like whether

## 72515:00 - 72550:00

I want to have kids or not. uh because

## 72550:00 - 72600:00

it's like uh understanding more of like

## 72600:00 - 72655:00

um yeah a lot of our functions of way we

## 72655:00 - 72700:00

operate is the functions of our genes uh

## 72700:00 - 72730:00

and genes want to do one thing was like

## 72730:00 - 72785:00

to procreate uh so so yes in a little

## 72785:00 - 72815:00

way but I like the book also proposed

## 72815:00 - 72850:00

another thing it's like um so everyone

## 72850:00 - 72870:00

wants to live forever right now and

## 72870:00 - 72915:00

maybe it's not like consciously but

## 72915:00 - 72955:00

subconsciously we do we do want that and

## 72955:00 - 72990:00

and I said two ways like one is like by

## 72990:00 - 73025:00

genes like genans wants just like want

## 73025:00 - 73050:00

to continue forever But also there are

## 73050:00 - 73080:00

two ideas. Um I think there's something

## 73080:00 - 73115:00

going meme. Uh it's like being a boy if

## 73115:00 - 73135:00

you have some ideas out there and then

## 73135:00 - 73160:00

it's like last for a long time. That's

## 73160:00 - 73190:00

the one you like live on. I know it's

## 73190:00 - 73240:00

like it's a little bit like um abstract

## 73240:00 - 73270:00

but I thought it's very interesting. The

## 73270:00 - 73300:00

other books I really really like. It's

## 73300:00 - 73340:00

like from like u the book from um

## 73340:00 - 73405:00

Singaporean um previous um I think he's

## 73405:00 - 73430:00

known as the father of Singapore. I know

## 73430:00 - 73465:00

like Limi Guango I'm not so sure what's

## 73465:00 - 73490:00

the title it but like he did so he was

## 73490:00 - 73530:00

the one who led Singapore from uh he

## 73530:00 - 73570:00

changed uh Singapore from a third

## 73570:00 - 73605:00

country to a forceful country within 25

## 73605:00 - 73660:00

years and I have never seen any country

## 73660:00 - 73695:00

leaders spend so much effort into like

## 73695:00 - 73735:00

pushing down his thought on like how to

## 73735:00 - 73785:00

build a country uh like like that um

## 73785:00 - 73815:00

yeah I talk a lot about like public

## 73815:00 - 73855:00

policy like how to like create policies

## 73855:00 - 73900:00

that encourage people to do the right

## 73900:00 - 73925:00

thing that is good for the nation And

## 73925:00 - 73960:00

also talking about like uh foreign

## 73960:00 - 74000:00

affairs, foreign policies like the

## 74000:00 - 74030:00

relation of like the country with other.

## 74030:00 - 74060:00

So it's a really good book to think

## 74060:00 - 74095:00

about. For me it's like system thinking

## 74095:00 - 74120:00

but like it's a different kind system

## 74120:00 - 74145:00

which is country which a lot of us don't

## 74145:00 - 74175:00

get a chance to like ever experiment in

## 74175:00 - 74205:00

our life. So it's good to learn about

## 74205:00 - 74210:00

that.

## 74210:00 - 74240:00

>> What was the name of that second book?

## 74240:00 - 74290:00

>> Uh it's called like from third to first

## 74290:00 - 74310:00

world fashion. I think I have it

## 74310:00 - 74345:00

somewhere here. Yeah,

## 74345:00 - 74385:00

>> there it is. Show and tell. That's

## 74385:00 - 74405:00

that's awesome. I definitely want to

## 74405:00 - 74425:00

read that. That's a really good tip.

## 74425:00 - 74445:00

I've heard a lot about just the impact

## 74445:00 - 74470:00

he's had and I've seen all these videos

## 74470:00 - 74505:00

on Twitter of just his really wise

## 74505:00 - 74540:00

insights into how to build a thriving

## 74540:00 - 74570:00

society and clearly

## 74570:00 - 74600:00

>> believe like how does he have time to

## 74600:00 - 74640:00

write is such a thick book. It's like

## 74640:00 - 74660:00

insane.

## 74660:00 - 74695:00

>> That is Claude. Please summarize. I'm

## 74695:00 - 74735:00

just joking. Uh by the way, selfish. I

## 74735:00 - 74760:00

also absolutely love that book. That is

## 74760:00 - 74780:00

such a good choice. It's such an under

## 74780:00 - 74815:00

the radar kind of book that really

## 74815:00 - 74845:00

changed the way I see the world as well.

## 74845:00 - 74880:00

Uh so really good pick. Okay, next

## 74880:00 - 74905:00

question. Do you have a favorite recent

## 74905:00 - 74935:00

movie or TV show you really enjoyed?

## 74935:00 - 74970:00

>> So I watch a lot of movie and TV shows

## 74970:00 - 75020:00

as a research uh because I I working on

## 75020:00 - 75060:00

my first novel and I recently uh sold

## 75060:00 - 75095:00

it. So I'm interesting like what makes

## 75095:00 - 75120:00

So it's a drama. It's not a science

## 75120:00 - 75170:00

fictions or uh anything that like tech

## 75170:00 - 75210:00

people usually read. So it's it's very

## 75210:00 - 75245:00

like I know it's a very um out of the

## 75245:00 - 75275:00

left field out of left field and like

## 75275:00 - 75330:00

very um so like reading watching TV to

## 75330:00 - 75380:00

see like what kind of stories become

## 75380:00 - 75410:00

popular trying to understand the trope

## 75410:00 - 75440:00

and and stuff like that. So I'm not sure

## 75440:00 - 75470:00

if the audience like

## 75470:00 - 75495:00

>> well what's one what's one that taught

## 75495:00 - 75525:00

you something about writing?

## 75525:00 - 75590:00

>> I think it like uh Yami Palace is a

## 75590:00 - 75620:00

Chinese TV show.

## 75620:00 - 75665:00

>> Cool. Okay. I haven't that one on the

## 75665:00 - 75700:00

podcast before. Okay. Yeah.

## 75700:00 - 75745:00

>> Next question. Do you have a life motto

## 75745:00 - 75790:00

that you often think about come back to

## 75790:00 - 75820:00

when you're dealing with something hard

## 75820:00 - 75855:00

whether it's in work or in life?

## 75855:00 - 75895:00

>> This sounds very nihilist. I think so.

## 75895:00 - 75925:00

Say it's like in the end nothing really

## 75925:00 - 75950:00

matters. Uh usually think of like in the

## 75950:00 - 75975:00

grand scheme of thing like in a billion

## 75975:00 - 76030:00

years nothing will like no one would

## 76030:00 - 76060:00

ever be there. I think okay some people

## 76060:00 - 76085:00

argue with me about that. So I go to

## 76085:00 - 76120:00

like I so my theory is like in a billion

## 76120:00 - 76150:00

years like none of us would ever exist

## 76150:00 - 76195:00

like so like whatever like messy things

## 76195:00 - 76235:00

like crazy things we do or like how bad

## 76235:00 - 76285:00

we do it I mean no one would be remember

## 76285:00 - 76320:00

wouldn't be there to remember it and I

## 76320:00 - 76355:00

think in a way it's like it sounds scary

## 76355:00 - 76390:00

but it's very liberating because it just

## 76390:00 - 76425:00

allows me okay let's just try things out

## 76425:00 - 76460:00

right like why does it matter and there

## 76460:00 - 76500:00

a story of like recently um so we have

## 76500:00 - 76525:00

some family member who passed away

## 76525:00 - 76585:00

recently and I was talking to my that

## 76585:00 - 76610:00

because I couldn't be home for that. I

## 76610:00 - 76630:00

was asking my dad like okay is there

## 76630:00 - 76665:00

anything I can do to make the person

## 76665:00 - 76715:00

like oh something like comfort anything

## 76715:00 - 76755:00

you can get that person and my dad was

## 76755:00 - 76800:00

just like what can he possibly want at

## 76800:00 - 76830:00

this moment like and this made me real

## 76830:00 - 76850:00

like at the end of life like there's

## 76850:00 - 76890:00

nothing that can bring you like like

## 76890:00 - 76920:00

material can bring you joy there's no

## 76920:00 - 76965:00

like money no product nothing and in a

## 76965:00 - 77010:00

way feel like okay what really do I

## 77010:00 - 77045:00

really care about at the end of the day

## 77045:00 - 77075:00

um so I guess it's like I think about it

## 77075:00 - 77105:00

if it's like okay maybe I fail it maybe

## 77105:00 - 77135:00

don't get the contract maybe things like

## 77135:00 - 77160:00

in but in the end at the end of life

## 77160:00 - 77195:00

like I don't think that actually really

## 77195:00 - 77235:00

matters so in a way it's like it's quite

## 77235:00 - 77250:00

liberating

## 77250:00 - 77270:00

>> uh I know you said it might be

## 77270:00 - 77300:00

nihilistic this is what Steve Jobs

## 77300:00 - 77325:00

shared too in one of his most famous

## 77325:00 - 77370:00

speeches just we will all die someday so

## 77370:00 - 77410:00

don't take things so seriously

## 77410:00 - 77445:00

and it is freeing absolutely it just

## 77445:00 - 77470:00

makes you appreciate every moment every

## 77470:00 - 77500:00

day you have just like yeah let's just

## 77500:00 - 77545:00

do something hard and scary okay final

## 77545:00 - 77570:00

question you talked about how you're

## 77570:00 - 77625:00

writing a novel most people in tech uh

## 77625:00 - 77660:00

have never written something creative

## 77660:00 - 77690:00

and fiction. What's just like one thing

## 77690:00 - 77725:00

you learned in the process about how to

## 77725:00 - 77765:00

write better stories, better fiction?

## 77765:00 - 77805:00

>> A lot of time when we read uh we get

## 77805:00 - 77850:00

trip up by some small things. So I think

## 77850:00 - 77885:00

like I I want to do [ __ ] writing because

## 77885:00 - 77915:00

I just want to go a better writer and I

## 77915:00 - 77950:00

thought like maybe try my like a

## 77950:00 - 77985:00

different audience could help me like

## 77985:00 - 78025:00

become better like anticipating what

## 78025:00 - 78050:00

this different type of audience would

## 78050:00 - 78085:00

want to hear and like like what they

## 78085:00 - 78110:00

care about. So this is a way for me to

## 78110:00 - 78145:00

get a so I think about writing or like

## 78145:00 - 78170:00

even like any kind of like content

## 78170:00 - 78220:00

creations is about like predicting the

## 78220:00 - 78265:00

users's reactions right

## 78265:00 - 78285:00

>> just kidding.

## 78285:00 - 78315:00

>> Yeah. So, so like you do a podcast, it's

## 78315:00 - 78350:00

like okay, what kind of things that the

## 78350:00 - 78390:00

users could find engaging, right? And

## 78390:00 - 78415:00

and I find this like a little bit like

## 78415:00 - 78440:00

uh in a lot of companies like you have

## 78440:00 - 78460:00

like launch a product, you have a

## 78460:00 - 78495:00

narrative coming out, okay, what kind do

## 78495:00 - 78535:00

we position this product in a way that

## 78535:00 - 78570:00

like users would want, right? So, I feel

## 78570:00 - 78595:00

like I have done technical writing for a

## 78595:00 - 78645:00

while and I felt like I have had some

## 78645:00 - 78695:00

experience like trying to predict what

## 78695:00 - 78740:00

engineers would want to hear all care

## 78740:00 - 78770:00

about. But then I don't have an

## 78770:00 - 78795:00

experience like this completely

## 78795:00 - 78825:00

different type of audience. So that's

## 78825:00 - 78850:00

what I want you to like career writing

## 78850:00 - 78885:00

creating a story and that's why I was

## 78885:00 - 78910:00

doing a lot of research on like watching

## 78910:00 - 78945:00

I mean going research enjoy a lot like

## 78945:00 - 78970:00

watching a lot of dramas. I just see

## 78970:00 - 79010:00

like what what people like. Um so so one

## 79010:00 - 79035:00

things that I care about is just like I

## 79035:00 - 79055:00

think I learned is like what like

## 79055:00 - 79085:00

emotional journey was from my editor,

## 79085:00 - 79120:00

right? So like when we write something

## 79120:00 - 79155:00

we we care about like how users would

## 79155:00 - 79205:00

feel like across the the story like we

## 79205:00 - 79225:00

want something in the beginning, right?

## 79225:00 - 79265:00

We want something just like we need to

## 79265:00 - 79290:00

have a hook so that people continue

## 79290:00 - 79320:00

reading. But we also don't want too much

## 79320:00 - 79365:00

of like drama because we'll get like too

## 79365:00 - 79400:00

tired, right? like uh because like the

## 79400:00 - 79435:00

emotionally exhausted like because it's

## 79435:00 - 79465:00

like you're being like emotionally

## 79465:00 - 79505:00

manipulated like a lot of time. So it

## 79505:00 - 79540:00

give like emotional emotional journey

## 79540:00 - 79570:00

maybe have like some some climax or like

## 79570:00 - 79600:00

some something more chill or like maybe

## 79600:00 - 79635:00

like I so care about another things I I

## 79635:00 - 79675:00

didn't realize like for me for for

## 79675:00 - 79710:00

technical writing you entirely focus on

## 79710:00 - 79740:00

the content like the argument is very

## 79740:00 - 79775:00

impersonal right like it it like for

## 79775:00 - 79815:00

example like people like ML compilers

## 79815:00 - 79855:00

like doesn't matter if they like the

## 79855:00 - 79890:00

person telling them about compiler or

## 79890:00 - 79910:00

not right because it's just like

## 79910:00 - 79955:00

objective like like but like for for

## 79955:00 - 79980:00

novel people care about like character

## 79980:00 - 80000:00

likability

## 80000:00 - 80030:00

So, so like in in the first version is

## 80030:00 - 80065:00

my story and makes the characters like a

## 80065:00 - 80115:00

little bit more like uh very uh very

## 80115:00 - 80150:00

logical, very rational and just does

## 80150:00 - 80185:00

everything just like very rationally.

## 80185:00 - 80210:00

And then the feedback I got is I have a

## 80210:00 - 80235:00

very good friend read it and he was he's

## 80235:00 - 80270:00

a amazing person. He's a great person

## 80270:00 - 80300:00

and he was like chip I be honest you I

## 80300:00 - 80330:00

hate that person. So it doesn't matter

## 80330:00 - 80360:00

as a story. It's just like the person is

## 80360:00 - 80390:00

so unlikable. So let's say he doesn't

## 80390:00 - 80430:00

find so is a second version and makes a

## 80430:00 - 80465:00

person the character more likable like

## 80465:00 - 80495:00

what how she makes that character more

## 80495:00 - 80515:00

likable is that you put in some

## 80515:00 - 80545:00

vulnerability like sometime that okay

## 80545:00 - 80580:00

maybe a person like has setback because

## 80580:00 - 80610:00

some people can relate to it. See in a

## 80610:00 - 80635:00

lot of ways it's like it's very

## 80635:00 - 80660:00

interesting. It's like a lot of it is

## 80660:00 - 80710:00

like um yeah, a lot of it is it's about

## 80710:00 - 80745:00

like understand the emotional bits uh

## 80745:00 - 80790:00

like how the users feel not just about

## 80790:00 - 80835:00

the story but also about the characters.

## 80835:00 - 80880:00

>> That is so interesting. Wow, I learned a

## 80880:00 - 80905:00

lot more there than I thought. That was

## 80905:00 - 80945:00

awesome. Really good example. Chip, two

## 80945:00 - 80975:00

final questions. Where can folks find

## 80975:00 - 81005:00

you online if they want to reach out and

## 81005:00 - 81040:00

maybe work with you or uh maybe even

## 81040:00 - 81070:00

just share the stuff that you offer if

## 81070:00 - 81105:00

folks want to reach out? And then how

## 81105:00 - 81145:00

can listeners be useful to you? I'm like

## 81145:00 - 81185:00

I'm on social media, LinkedIn, Twitter.

## 81185:00 - 81220:00

I don't post a lot, but I keep telling

## 81220:00 - 81255:00

myself that I should do more because I

## 81255:00 - 81295:00

kind like the conversation with uh with

## 81295:00 - 81330:00

um with with readers. Uh so I'm actually

## 81330:00 - 81400:00

about to start a a SL a subspect. Um so

## 81400:00 - 81435:00

I have like a placeholder for subspect

## 81435:00 - 81455:00

right now and I'm thinking of doing it

## 81455:00 - 81485:00

for more system thinking because I think

## 81485:00 - 81530:00

it's a very interesting skill. Um and so

## 81530:00 - 81555:00

like thinking of doing a YouTube channel

## 81555:00 - 81595:00

on book reviews and basically books that

## 81595:00 - 81635:00

help you think better. So I think it's

## 81635:00 - 81655:00

the first book I'm going to review is

## 81655:00 - 81680:00

probably like this book because it's

## 81680:00 - 81710:00

like my favorite book growing up. Uh and

## 81710:00 - 81745:00

I have been like keep on reading it. Uh

## 81745:00 - 81800:00

so yes. So how can it be helpful like

## 81800:00 - 81845:00

send me books that you like uh books

## 81845:00 - 81905:00

that have you have changed the way you

## 81905:00 - 81960:00

think or change you the way you do

## 81960:00 - 82005:00

anything. So, I would appreciate it.

## 82005:00 - 82030:00

>> Amazing. I'm I'm excited to read that

## 82030:00 - 82050:00

book.

## 82050:00 - 82075:00

>> Uh, Chip, thank you so much for being

## 82075:00 - 82090:00

here.

## 82090:00 - 82125:00

>> Thank you so much, Lenny, for having me.

## 82125:00 - 82185:00

>> Bye, everyone.

## 82185:00 - 82210:00

Thank you so much for listening. If you

## 82210:00 - 82235:00

found this valuable, you can subscribe

## 82235:00 - 82280:00

to the show on Apple Podcasts, Spotify,

## 82280:00 - 82320:00

or your favorite podcast app. Also,

## 82320:00 - 82350:00

please consider giving us a rating or

## 82350:00 - 82385:00

leaving a review as that really helps

## 82385:00 - 82420:00

other listeners find the podcast. You

## 82420:00 - 82460:00

can find all past episodes or learn more

## 82460:00 - 82510:00

about the show at lennispodcast.com.

## 82510:00+

See you in the next episode.

