---
source: https://www.youtube.com/watch?v=p8Jx4qvDoSo
title: Scaling and the Road to Human-Level AI | Anthropic Co-founder Jared Kaplan
author: Y Combinator
date: 2025-07-29
views: 57817
description: >-
  Jared Kaplan on June 16th, 2025 at AI Startup School in San Francisco.


  Jared Kaplan started out as a theoretical physicist chasing questions about
  the universe. Then he helped uncover one of AI’s most surprising truths: that
  intelligence scales in a predictable, almost physical way.


  That insight became foundational to the modern era of large language
  models—and led him to co-found Anthropic.


  In this talk, he walks through how that discovery reshaped the path to
  human-level AI, what it means for future models like Claude, and why even the
  dumbest questions can lead to the biggest breakthroughs. He reflects on
  memory, oversight, and what’s left to solve as models grow smarter—and
  longer-horizon tasks come within reach.


  Apply to Y Combinator: https://ycombinator.com/apply


  Chapters:

  00:17 - From Physics to AI

  01:41 - Initial Skepticism and Shift to AI

  02:12 - AI Training Phases

  02:32 - Pre-Training

  03:16 - Reinforcement Learning

  04:19 - Scaling Laws in Training

  08:19 - Unlocking AI Capabilities

  11:27 - Organizational Knowledge and Memory

  12:19 - Oversight and Nuanced Tasks

  13:38 - Preparing for the Future

  15:48 - Claude 4 and Beyond

  21:18 - Human-AI Collaboration

  29:50 - Scaling Laws and Compute Efficiency

  35:26 - Audience Q&A
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:43:30.585Z
---

# Scaling and the Road to Human-Level AI | Anthropic Co-founder Jared Kaplan

## 00:00 - 50:00

Hey everyone. Um, I'm Jared Kaplan. I'm

## 50:00 - 105:00

going to talk briefly about scaling and

## 105:00 - 140:00

the road to human level AI, but my guess

## 140:00 - 170:00

is for this audience, a lot of these

## 170:00 - 200:00

ideas are pretty familiar, so I'll keep

## 200:00 - 235:00

it short and then we're going to do a

## 235:00 - 275:00

sort of fireside chat Q&A with uh with

## 275:00 - 330:00

Diana. I actually have only been working

## 330:00 - 400:00

on AI for about six years. I uh before

## 400:00 - 430:00

that had a long career, the vast

## 430:00 - 470:00

majority of my career as a theoretical

## 470:00 - 525:00

physicist. um working in academia. And

## 525:00 - 580:00

so uh how did I get to AI? Well, I I I

## 580:00 - 610:00

want to be brief. Why did I start in

## 610:00 - 645:00

physics? It was basically because my mom

## 645:00 - 690:00

was a science fiction writer and I

## 690:00 - 730:00

wanted to figure out if we could build a

## 730:00 - 775:00

faster than light drive and physics was

## 775:00 - 825:00

the way to do that. Um I also was very

## 825:00 - 865:00

excited about just understanding the

## 865:00 - 905:00

universe. How do things work? How do the

## 905:00 - 965:00

biggest trends that underly sort of

## 965:00 - 1000:00

everything that we see around us, where

## 1000:00 - 1045:00

does that all come from? For example, is

## 1045:00 - 1070:00

the universe deterministic? Do we have

## 1070:00 - 1095:00

free will? I was very, very interested

## 1095:00 - 1125:00

in all of those questions. But

## 1125:00 - 1175:00

fortunately, along the way, uh during my

## 1175:00 - 1215:00

career as a physicist, I met a lot of

## 1215:00 - 1250:00

very, very interesting, very deep

## 1250:00 - 1295:00

people, including many of the uh

## 1295:00 - 1340:00

founders of Anthropic that I now work

## 1340:00 - 1390:00

with all of the time. And uh I was

## 1390:00 - 1410:00

really interested in what they were

## 1410:00 - 1460:00

doing and I kept track of it. And as I

## 1460:00 - 1510:00

moved from different uh among different

## 1510:00 - 1550:00

subject areas in physics from large

## 1550:00 - 1580:00

hadron collider physics, particle

## 1580:00 - 1635:00

physics, cosmology, string theory, um

## 1635:00 - 1685:00

and on I got a little bit frustrated, a

## 1685:00 - 1705:00

little bit bored. I didn't feel like we

## 1705:00 - 1745:00

were making progress quickly enough. And

## 1745:00 - 1770:00

a lot of my friends were telling me that

## 1770:00 - 1820:00

AI was becoming a really big deal. Um

## 1820:00 - 1850:00

and I didn't believe them. I was really

## 1850:00 - 1890:00

skeptical. I thought, well, AI, people

## 1890:00 - 1920:00

have been working on it for 50 years.

## 1920:00 - 1970:00

SVMs aren't that exciting. Um, that was

## 1970:00 - 2025:00

all we knew about back in 2005, 2009

## 2025:00 - 2050:00

when I was in school. But I got

## 2050:00 - 2090:00

convinced that that maybe AI would be an

## 2090:00 - 2145:00

exciting field to work on. Um, and I I

## 2145:00 - 2180:00

got very lucky to know the right people

## 2180:00 - 2225:00

and the rest is history. So uh I'm going

## 2225:00 - 2265:00

to talk a little bit about how our

## 2265:00 - 2310:00

contemporary AI models work and how

## 2310:00 - 2350:00

scaling is leading them to get better

## 2350:00 - 2405:00

and better. So there are really two

## 2405:00 - 2460:00

fundamental phases to the training of

## 2460:00 - 2500:00

contemporary AI models like claude

## 2500:00 - 2530:00

chatgpt

## 2530:00 - 2615:00

etc. The first phase is pre-training and

## 2615:00 - 2665:00

that's where we train AI models to

## 2665:00 - 2710:00

imitate human written data, human

## 2710:00 - 2750:00

written text and understand the

## 2750:00 - 2795:00

correlations underlying that data. And

## 2795:00 - 2845:00

these these figures are very very retro.

## 2845:00 - 2880:00

This is actually from the playground of

## 2880:00 - 2930:00

the original GPD3 model. And you can see

## 2930:00 - 2970:00

that as a speaker at a journal club,

## 2970:00 - 3000:00

you're probably elephant me to say

## 3000:00 - 3025:00

certain things. is the word elephant in

## 3025:00 - 3085:00

that sentence is really really unlikely.

## 3085:00 - 3135:00

What pre-training does is teach models

## 3135:00 - 3175:00

what words are likely to follow other

## 3175:00 - 3230:00

words in large corporate of text and now

## 3230:00 - 3265:00

with contemporary models multimodal

## 3265:00 - 3320:00

data. The second phase of training for

## 3320:00 - 3365:00

contemporary AI models is reinforcement

## 3365:00 - 3405:00

learning. This is another very retro

## 3405:00 - 3450:00

slide. Um it shows the original

## 3450:00 - 3495:00

interface we used for sort of claude

## 3495:00 - 3545:00

zero or claude negative one uh back in

## 3545:00 - 3590:00

the ancient days of 2022

## 3590:00 - 3655:00

when we were collecting feedback data.

## 3655:00 - 3685:00

And what you see here is basically the

## 3685:00 - 3740:00

interface for having a conversation with

## 3740:00 - 3785:00

very very early versions of Claude and

## 3785:00 - 3865:00

picking which response from Claude was

## 3865:00 - 3900:00

better according to you, according to

## 3900:00 - 3955:00

crowdworkers, etc. And using that

## 3955:00 - 4010:00

signal, we optimize, we reinforce the

## 4010:00 - 4070:00

behaviors that are chosen to be good,

## 4070:00 - 4095:00

that are chosen to be helpful, honest,

## 4095:00 - 4125:00

and harmless. And we discourage the

## 4125:00 - 4165:00

behaviors that are bad. So really all

## 4165:00 - 4210:00

there is to training these models is

## 4210:00 - 4250:00

learning to predict the next word and

## 4250:00 - 4285:00

then doing reinforcement learning to

## 4285:00 - 4330:00

learn to do useful tasks. And it turns

## 4330:00 - 4380:00

out that there are scaling laws for both

## 4380:00 - 4445:00

of these phases of training. So this is

## 4445:00 - 4485:00

a a figure that that we made five or six

## 4485:00 - 4535:00

years ago now and it shows how as you

## 4535:00 - 4590:00

scale up the pre-training phase of AI,

## 4590:00 - 4640:00

you predictably get better and better

## 4640:00 - 4690:00

performance for our models. And this was

## 4690:00 - 4715:00

something that came about because I was

## 4715:00 - 4750:00

just sort of asking the dumbest possible

## 4750:00 - 4785:00

question. As a physicist, that's what

## 4785:00 - 4805:00

you're trained to do. You sort of look

## 4805:00 - 4840:00

at the big picture and you ask really

## 4840:00 - 4885:00

dumb things. I'd heard it was very

## 4885:00 - 4925:00

popular in the 2010s to say that big

## 4925:00 - 4970:00

data was important and so I just wanted

## 4970:00 - 5030:00

to know how big should the data be? How

## 5030:00 - 5070:00

important is it? How much does it help?

## 5070:00 - 5105:00

Similarly, a lot of people were noticing

## 5105:00 - 5160:00

that larger AI models performed better.

## 5160:00 - 5190:00

And so we just asked the question, how

## 5190:00 - 5235:00

much better do these models perform? And

## 5235:00 - 5275:00

we got really lucky. We found that

## 5275:00 - 5305:00

there's actually something very very

## 5305:00 - 5355:00

very precise and surprising underlying

## 5355:00 - 5395:00

AI training. This really blew us away

## 5395:00 - 5420:00

that there are these nice trends that

## 5420:00 - 5455:00

are as precise as anything that you see

## 5455:00 - 5505:00

in physics or or astronomy. And these

## 5505:00 - 5565:00

gave us a lot of conviction to believe

## 5565:00 - 5610:00

that AI was just going to keep getting

## 5610:00 - 5640:00

smarter and smarter in a very

## 5640:00 - 5680:00

predictable way. Because as you can see

## 5680:00 - 5745:00

in these figures already back in 2019,

## 5745:00 - 5790:00

we were looking across many many many

## 5790:00 - 5840:00

orders of magnitude in compute, in data

## 5840:00 - 5905:00

set size, in neural network size. And so

## 5905:00 - 5945:00

we expected once you see something is

## 5945:00 - 5975:00

true over many many many orders of

## 5975:00 - 6000:00

magnitude you expect it's probably going

## 6000:00 - 6030:00

to continue to be true for a long time

## 6030:00 - 6065:00

further. So this has sort of been one of

## 6065:00 - 6095:00

the fundamental things that I think

## 6095:00 - 6160:00

underlies uh uh improvements in in AI.

## 6160:00 - 6190:00

The other is actually also something

## 6190:00 - 6220:00

that started to appear quite a long time

## 6220:00 - 6260:00

ago although it's become really really

## 6260:00 - 6305:00

impactful uh in the last couple of years

## 6305:00 - 6345:00

is that you can see scaling laws in the

## 6345:00 - 6395:00

reinforcement learning phase of AI

## 6395:00 - 6455:00

training. So uh a researcher about four

## 6455:00 - 6515:00

years ago decided to study scaling laws

## 6515:00 - 6560:00

for Alph Go. Basically putting together

## 6560:00 - 6615:00

two very very high-profile AI successes,

## 6615:00 - 6655:00

GPD3 and scaling for pre-training and

## 6655:00 - 6710:00

AlphaGo. This was just a researcher uh

## 6710:00 - 6755:00

Andy Jones working on his own uh with

## 6755:00 - 6805:00

like his own I think maybe single GPU

## 6805:00 - 6840:00

back in these sort of ancient days. And

## 6840:00 - 6870:00

so he couldn't study AlphaGo, that was

## 6870:00 - 6895:00

expensive, but he could study a simpler

## 6895:00 - 6940:00

game called Hex. So he made this plot

## 6940:00 - 7000:00

that you see here. Now, ELO scores, I

## 7000:00 - 7045:00

think, weren't as as as well known um

## 7045:00 - 7095:00

back then, but all EOS ELO scores are,

## 7095:00 - 7130:00

of course, is chess ratings. They

## 7130:00 - 7180:00

basically describe how likely it is for

## 7180:00 - 7215:00

one player to beat another in a game of

## 7215:00 - 7265:00

chess. They're used now to benchmark AI

## 7265:00 - 7310:00

models to see sort of how often does a

## 7310:00 - 7340:00

human prefer one AI model to another.

## 7340:00 - 7365:00

But but back then this is just sort of

## 7365:00 - 7410:00

the classic application of ELO scores as

## 7410:00 - 7450:00

as chess ratings. And he looked at as

## 7450:00 - 7505:00

you train different models to play this

## 7505:00 - 7555:00

game of hex, which is a very simple

## 7555:00 - 7600:00

board game, a bit simpler than than Go,

## 7600:00 - 7630:00

how do they do? And he saw these

## 7630:00 - 7670:00

remarkable straight lines. So it's sort

## 7670:00 - 7720:00

of a skill in science to notice very

## 7720:00 - 7760:00

very simple trends and and this was one

## 7760:00 - 7800:00

I think it went unnoticed. I think

## 7800:00 - 7830:00

people didn't focus on this this sort of

## 7830:00 - 7865:00

kind of scaling behavior in RL soon

## 7865:00 - 7890:00

enough but but eventually it came to

## 7890:00 - 7940:00

pass. So we see that basically you can

## 7940:00 - 7960:00

scale up the compute in both

## 7960:00 - 8000:00

pre-training and RL and get better and

## 8000:00 - 8030:00

better performance. And I think that's

## 8030:00 - 8065:00

sort of the fundamental thing that is

## 8065:00 - 8115:00

driving AI progress. It's not that AI

## 8115:00 - 8145:00

researchers are really smart or they

## 8145:00 - 8210:00

suddenly got smart. It's that we found a

## 8210:00 - 8265:00

very very simple way of making AI better

## 8265:00 - 8300:00

systematically and and we're we're

## 8300:00 - 8345:00

turning that crank. So what kinds of

## 8345:00 - 8375:00

capabilities is this unlocking? I tend

## 8375:00 - 8420:00

to think of AI capabilities on two axes.

## 8420:00 - 8455:00

I think the less interesting axis, but

## 8455:00 - 8510:00

it's still very important is basically

## 8510:00 - 8580:00

the the flexibility of AI, the ability

## 8580:00 - 8635:00

of AI to meet us where we are. So if you

## 8635:00 - 8700:00

put say Alph Go on this figure, it would

## 8700:00 - 8740:00

be very very far below the X-axis

## 8740:00 - 8775:00

because although Alph Go was super

## 8775:00 - 8825:00

intelligent, it was better than any Go

## 8825:00 - 8890:00

player at playing Go, it was uh only

## 8890:00 - 8930:00

able to operate in the universe of a Go

## 8930:00 - 8975:00

board. But we've made steady progress

## 8975:00 - 9010:00

since the advent of large language

## 9010:00 - 9085:00

models making uh AI that can deal with

## 9085:00 - 9130:00

many many many all of the modalities

## 9130:00 - 9160:00

that that people can deal with. We don't

## 9160:00 - 9195:00

have AI models I think that uh that have

## 9195:00 - 9230:00

a sense of smell. Um but that's that's

## 9230:00 - 9270:00

probably coming. And so as you go up the

## 9270:00 - 9320:00

y- axis here you get to AI systems that

## 9320:00 - 9365:00

can do more and more relevant things in

## 9365:00 - 9390:00

in the world. I think the more

## 9390:00 - 9420:00

interesting axis though is sort of the

## 9420:00 - 9470:00

the x-axis here which is how long it

## 9470:00 - 9505:00

would take a person to do to do the

## 9505:00 - 9550:00

kinds of tasks that AI models can do and

## 9550:00 - 9580:00

that's something that has been

## 9580:00 - 9620:00

increasing steadily as we increase the

## 9620:00 - 9645:00

capability of AI. This is sort of the

## 9645:00 - 9705:00

time horizon for for tasks and um an

## 9705:00 - 9740:00

organization meter studied this very

## 9740:00 - 9780:00

systematically and found yet another

## 9780:00 - 9815:00

scaling trend. They found that if you

## 9815:00 - 9865:00

look at uh the length of tasks that AI

## 9865:00 - 9915:00

models can do, it's doubling roughly

## 9915:00 - 9970:00

every 7 months. And so what this means

## 9970:00 - 10035:00

is that the increasing intelligence that

## 10035:00 - 10075:00

is being baked into AI by scaling

## 10075:00 - 10115:00

compute for pre-training and RL is

## 10115:00 - 10175:00

leading to predictable useful

## 10175:00 - 10235:00

tasks that the AI models uh can can do,

## 10235:00 - 10260:00

including longer and longer horizon

## 10260:00 - 10295:00

tasks. And so you can sort of speculate

## 10295:00 - 10335:00

about where this is heading. And in AI

## 10335:00 - 10405:00

2027 folks did. And this kind of picture

## 10405:00 - 10455:00

suggests that over the next few years we

## 10455:00 - 10500:00

may reach a point where AI models um can

## 10500:00 - 10535:00

do tasks that don't just take us minutes

## 10535:00 - 10600:00

or hours but days, weeks, months, years

## 10600:00 - 10660:00

etc. Eventually, we imagine AI models or

## 10660:00 - 10700:00

or millions of AI models perhaps working

## 10700:00 - 10735:00

together will be able to do the work

## 10735:00 - 10780:00

that whole human organizations can do.

## 10780:00 - 10800:00

They'll be able to do the kind of work

## 10800:00 - 10835:00

that the entire scientific community

## 10835:00 - 10870:00

currently does. Um, one of the nice

## 10870:00 - 10905:00

things about math or theoretical physics

## 10905:00 - 10955:00

is that you can make progress just by by

## 10955:00 - 11005:00

thinking. Um and so you can imagine AI

## 11005:00 - 11035:00

systems working together to make the

## 11035:00 - 11075:00

kind of progress that the theoretical

## 11075:00 - 11105:00

physics community makes in in say 50

## 11105:00 - 11185:00

years in a matter of days, weeks etc. So

## 11185:00 - 11225:00

what is left if if this sort of picture

## 11225:00 - 11260:00

of scaling can take us very far? What is

## 11260:00 - 11310:00

left? I think that what may be left in

## 11310:00 - 11350:00

order to unlock um kind of human level

## 11350:00 - 11400:00

AI broadly construed is relatively

## 11400:00 - 11425:00

simple. One of the most important

## 11425:00 - 11475:00

ingredients I think is relevant

## 11475:00 - 11505:00

organizational knowledge. So we need to

## 11505:00 - 11565:00

train AI models that don't just greet

## 11565:00 - 11620:00

you with a blank slate but can learn to

## 11620:00 - 11660:00

work within companies, organizations,

## 11660:00 - 11700:00

governments as though they have the kind

## 11700:00 - 11745:00

of context that someone who's been

## 11745:00 - 11780:00

working there for years has. So I think

## 11780:00 - 11815:00

AI models need to be able to work with

## 11815:00 - 11865:00

knowledge. They also need memory. What

## 11865:00 - 11895:00

is memory if not knowledge? I

## 11895:00 - 11945:00

distinguish it in the sense that as you

## 11945:00 - 11985:00

do a task that takes you a very very

## 11985:00 - 12020:00

long time, you need to keep track of

## 12020:00 - 12060:00

your progress on that specific task, you

## 12060:00 - 12090:00

need to build relevant memories and you

## 12090:00 - 12110:00

you need to be able to use them. And

## 12110:00 - 12140:00

that's something that we've uh we've

## 12140:00 - 12190:00

begun to build into into Claude 4 and I

## 12190:00 - 12210:00

think will become increasingly

## 12210:00 - 12245:00

important. A third ingredient that I

## 12245:00 - 12270:00

think that we need to get better at and

## 12270:00 - 12320:00

and we're making progress on is

## 12320:00 - 12400:00

oversight. the ability of AI models to

## 12400:00 - 12445:00

understand sort of fine grained nuances

## 12445:00 - 12510:00

to solve hard fuzzy tasks. So it's easy

## 12510:00 - 12540:00

right now and you see an explosion of

## 12540:00 - 12580:00

progress for us to train AI models that

## 12580:00 - 12625:00

can say write code that passes tests or

## 12625:00 - 12660:00

that answer math questions correctly

## 12660:00 - 12710:00

because it's very crisp what's correct

## 12710:00 - 12740:00

and what's incorrect. So it's very easy

## 12740:00 - 12785:00

to apply reinforcement learning to make

## 12785:00 - 12825:00

AI models uh do better and better at

## 12825:00 - 12865:00

those kinds of tasks. But what we need

## 12865:00 - 12910:00

and are developing are AI models that

## 12910:00 - 12955:00

help us to generate much more nuanced

## 12955:00 - 13020:00

reward signals so that we can leverage

## 13020:00 - 13070:00

reinforcement learning to do to do

## 13070:00 - 13115:00

things like tell good jokes, write good

## 13115:00 - 13190:00

poems, um and have good taste in in

## 13190:00 - 13220:00

research. The other ingredients that we

## 13220:00 - 13255:00

need, I think, are are are simpler. We

## 13255:00 - 13280:00

obviously need to be able to train AI

## 13280:00 - 13310:00

models to do more and more complex

## 13310:00 - 13365:00

tasks. We need to work our way up the

## 13365:00 - 13410:00

y-axis from text models to multimodal

## 13410:00 - 13460:00

models to robotics. Um, and I expect

## 13460:00 - 13495:00

that over the next few years, we'll see

## 13495:00 - 13560:00

increasing uh continued gains from scale

## 13560:00 - 13605:00

when applied applied to these these

## 13605:00 - 13635:00

different domains.

## 13635:00 - 13695:00

And so how should we sort of prepare for

## 13695:00 - 13740:00

this this future these possibilities? I

## 13740:00 - 13775:00

think there are a few a few things that

## 13775:00 - 13830:00

I always recommend. One is I think it's

## 13830:00 - 13890:00

really a good idea to build things that

## 13890:00 - 13925:00

don't quite work yet. This is probably

## 13925:00 - 13945:00

always a good idea. We always want to

## 13945:00 - 13985:00

have ambition, but I think specifically

## 13985:00 - 14020:00

AI models right now are getting better

## 14020:00 - 14050:00

very very quickly. And I think that's

## 14050:00 - 14080:00

going to continue. That means that if

## 14080:00 - 14115:00

you build uh a product that doesn't

## 14115:00 - 14160:00

quite work because Claude 4 is still a

## 14160:00 - 14195:00

little bit too dumb, um you could expect

## 14195:00 - 14235:00

that there'll be a Claude 5 coming that

## 14235:00 - 14280:00

will make that make that product work

## 14280:00 - 14310:00

and deliver a lot of value. So I think

## 14310:00 - 14330:00

that's that's something that I always

## 14330:00 - 14360:00

recommend is sort of experiment on the

## 14360:00 - 14390:00

boundaries of what AI can do because

## 14390:00 - 14425:00

those boundaries are moving rapidly. The

## 14425:00 - 14470:00

next point I think is that AI is going

## 14470:00 - 14515:00

to be helpful for integrating AI. I

## 14515:00 - 14565:00

think that one of the main bottlenecks

## 14565:00 - 14600:00

for AI is really just that it's

## 14600:00 - 14630:00

developing so quickly that we haven't

## 14630:00 - 14695:00

had time to integrate it into

## 14695:00 - 14735:00

products, companies, other thing

## 14735:00 - 14765:00

everything else that we we we do into

## 14765:00 - 14825:00

into science. Um, and so I think that in

## 14825:00 - 14850:00

order to sort of speed that process up,

## 14850:00 - 14890:00

I think leveraging AI for AI integration

## 14890:00 - 14915:00

is going to be is going to be very

## 14915:00 - 14945:00

valuable. And then finally, I mean, I

## 14945:00 - 14965:00

think this is sort of obvious for for

## 14965:00 - 14990:00

this crowd, but I think figuring out

## 14990:00 - 15045:00

where adoption of AI could happen very

## 15045:00 - 15125:00

very quickly is is key. Um, we're seeing

## 15125:00 - 15170:00

uh an explosion of AI integration for

## 15170:00 - 15210:00

coding. And there are a lot of reasons

## 15210:00 - 15240:00

why software engineering is a great

## 15240:00 - 15270:00

place for AI, but I think the big

## 15270:00 - 15315:00

question is sort of what's next? Um,

## 15315:00 - 15350:00

what beyond software engineering can

## 15350:00 - 15390:00

grow that that quickly? I don't know the

## 15390:00 - 15435:00

answer, of course. Um, but hopefully you

## 15435:00 - 15475:00

guys will figure it out. So that's it

## 15475:00 - 15515:00

for for for the talk. Um, I want to

## 15515:00 - 15565:00

invite Diana on stage for uh for a chat.

## 15565:00 - 15605:00

>> YC's next batch is now taking

## 15605:00 - 15640:00

applications. Got a startup in you?

## 15640:00 - 15690:00

Apply at y combinator.com/apply.

## 15690:00 - 15730:00

It's never too early and filling out the

## 15730:00 - 15780:00

app will level up your idea. Okay, back

## 15780:00 - 15830:00

to the video. That was a awesome talk

## 15830:00 - 15890:00

about all the scaling laws and recently

## 15890:00 - 15950:00

Anthropic just launched clot 4 which is

## 15950:00 - 16015:00

just available. Curious uh how does it

## 16015:00 - 16065:00

change what is possible as all these

## 16065:00 - 16115:00

model releases keep compounding for the

## 16115:00 - 16150:00

next 12 months?

## 16150:00 - 16190:00

>> I think that uh we'll be in trouble if

## 16190:00 - 16230:00

it's 12 months before before an even

## 16230:00 - 16285:00

better model comes out. But uh I guess

## 16285:00 - 16315:00

uh a few things with with Cloud 4. I

## 16315:00 - 16380:00

think that with Cloud 3.7 Sonnet

## 16380:00 - 16430:00

uh it was already really exciting to use

## 16430:00 - 16475:00

3.7 for coding. But I think something

## 16475:00 - 16530:00

that everyone noticed was that 3.7 was a

## 16530:00 - 16590:00

little bit too eager. Um sometimes it

## 16590:00 - 16625:00

just really wanted to make your tests

## 16625:00 - 16660:00

pass. Um and it would do things that

## 16660:00 - 16695:00

that you you don't really want. Uh there

## 16695:00 - 16720:00

are a lot of like try excepts things

## 16720:00 - 16780:00

like that. Um, so with Cloud 4, I think

## 16780:00 - 16830:00

that we've been able to improve the

## 16830:00 - 16870:00

model's ability to act as an agent

## 16870:00 - 16895:00

specifically for coding, but but in a

## 16895:00 - 16925:00

lot of other ways for search, for all

## 16925:00 - 16965:00

kinds of other applications. Um, but

## 16965:00 - 17025:00

also improve its supervision, the sort

## 17025:00 - 17055:00

of oversight that I I I mentioned in my

## 17055:00 - 17105:00

talk, so that it uh it follows your

## 17105:00 - 17150:00

directions and hopefully improves in in

## 17150:00 - 17180:00

code quality. I think the other thing

## 17180:00 - 17210:00

that we've worked on is improving its

## 17210:00 - 17260:00

ability to uh save and store memories

## 17260:00 - 17285:00

and we hope to see people leveraging

## 17285:00 - 17330:00

that because Claude 4 can blow through

## 17330:00 - 17360:00

its context window with a very complex

## 17360:00 - 17415:00

task but can also uh store memories as

## 17415:00 - 17460:00

files or records, retrieve them in order

## 17460:00 - 17490:00

to sort of keep doing work across many

## 17490:00 - 17520:00

many many context windows. But I guess

## 17520:00 - 17550:00

finally I think the picture that scaling

## 17550:00 - 17585:00

laws paint is one of incremental

## 17585:00 - 17630:00

progress. And so I think that what

## 17630:00 - 17680:00

you'll see with Claude is that steadily

## 17680:00 - 17720:00

it gets better in lots of different ways

## 17720:00 - 17760:00

with each release. Um but I think that

## 17760:00 - 17815:00

scaling really suggests a kind of smooth

## 17815:00 - 17870:00

curve towards what I expect is kind of

## 17870:00 - 17910:00

human level AI or AGI.

## 17910:00 - 17950:00

>> Is there some special feature that a lot

## 17950:00 - 17985:00

of the audience here are going to get

## 17985:00 - 18045:00

excited? some some beta that you can

## 18045:00 - 18095:00

some alpha leak you can give everyone on

## 18095:00 - 18115:00

what you think people are going to fall

## 18115:00 - 18160:00

in love with the new APIs.

## 18160:00 - 18185:00

>> I think the thing that I I'm most

## 18185:00 - 18240:00

excited about is sort of uh memory

## 18240:00 - 18275:00

unlocking longer and longer horizon

## 18275:00 - 18325:00

tasks. I think that like as as time goes

## 18325:00 - 18365:00

on we're going to see Claude as a

## 18365:00 - 18390:00

collaborator that can sort of take on

## 18390:00 - 18425:00

larger and larger chunks of work. This

## 18425:00 - 18460:00

is to your point of all these future

## 18460:00 - 18490:00

models being able to take bigger and

## 18490:00 - 18530:00

bigger tasks right now. At this point,

## 18530:00 - 18595:00

they're able to do tasks in the hours.

## 18595:00 - 18630:00

>> Yeah, I think so. I think it's a very

## 18630:00 - 18665:00

imprecise measure, but I think that

## 18665:00 - 18700:00

right now if you look at sort of

## 18700:00 - 18720:00

software engineering tasks, I think

## 18720:00 - 18765:00

meter literally benchmarked how long it

## 18765:00 - 18795:00

would take people to do various tasks

## 18795:00 - 18830:00

and uh and yeah, I think it's a time

## 18830:00 - 18870:00

scale of of hours. I think just gen like

## 18870:00 - 18920:00

broadly as people work with AI,

## 18920:00 - 18950:00

I think that the people who are skeptics

## 18950:00 - 19005:00

of AI will say correctly that AI makes

## 19005:00 - 19055:00

lots of stupid mistakes. Um, it can do

## 19055:00 - 19085:00

things that are absolutely brilliant and

## 19085:00 - 19120:00

and surprise you, but it can also make

## 19120:00 - 19155:00

uh make basic errors. I think one of the

## 19155:00 - 19210:00

sort of basic features of of AI that's

## 19210:00 - 19240:00

different about the shape of AI

## 19240:00 - 19260:00

intelligence compared to human

## 19260:00 - 19290:00

intelligence is that there are a lot of

## 19290:00 - 19320:00

things that I can't do but I can at

## 19320:00 - 19350:00

least judge whether they were done

## 19350:00 - 19405:00

correctly. I think for AI the judgment

## 19405:00 - 19450:00

versus the generative capability is much

## 19450:00 - 19495:00

closer which means that I think that uh

## 19495:00 - 19530:00

a major role people can play in

## 19530:00 - 19560:00

interacting with AI is kind of as

## 19560:00 - 19605:00

managers to sort of sanity check uh

## 19605:00 - 19625:00

sanity check the the work

## 19625:00 - 19650:00

>> which is fascinating because one of the

## 19650:00 - 19690:00

things we observe through the batches in

## 19690:00 - 19750:00

YC last year a lot of companies when

## 19750:00 - 19790:00

they were out and selling products they

## 19790:00 - 19845:00

were selling it more still as a co-pilot

## 19845:00 - 19870:00

where you would have a co-pilot let's

## 19870:00 - 19905:00

say for customer support where you still

## 19905:00 - 19945:00

need the last human approval before they

## 19945:00 - 19990:00

would send the reply for a customer but

## 19990:00 - 20025:00

one thing that has changed just in the

## 20025:00 - 20075:00

spring batch I think a lot of the AI

## 20075:00 - 20120:00

models are very capable to do task end

## 20120:00 - 20160:00

to end to your point that which is uh

## 20160:00 - 20215:00

remarkable founders are selling now

## 20215:00 - 20290:00

directly replacements of full workflows

## 20290:00 - 20325:00

how have you seen this translate to what

## 20325:00 - 20370:00

you hope the audience will build.

## 20370:00 - 20390:00

>> I think there are a lot of

## 20390:00 - 20430:00

possibilities. Basically, it's a

## 20430:00 - 20460:00

question of

## 20460:00 - 20515:00

what level of success or performance is

## 20515:00 - 20555:00

is acceptable. There are some tasks

## 20555:00 - 20600:00

where getting it sort of 70% right is is

## 20600:00 - 20625:00

good enough and others where you need

## 20625:00 - 20695:00

99.9% to to deploy. I think that

## 20695:00 - 20720:00

honestly I think it's probably a lot

## 20720:00 - 20780:00

more fun to build for use cases where uh

## 20780:00 - 20830:00

70 80% is good enough because then you

## 20830:00 - 20865:00

can really get to the frontier of what

## 20865:00 - 20900:00

AI is capable of. But I think that we're

## 20900:00 - 20985:00

sort of pushing up the the reliability

## 20985:00 - 21025:00

as well. So I think that uh we will see

## 21025:00 - 21050:00

more and more of these tasks. I think

## 21050:00 - 21110:00

that uh right now human AI collaboration

## 21110:00 - 21160:00

is is going to be the sort of most

## 21160:00 - 21190:00

interesting place because I think that

## 21190:00 - 21215:00

for the most advanced tasks you're

## 21215:00 - 21245:00

really going to need humans in the loop.

## 21245:00 - 21270:00

But I do think in the longer term there

## 21270:00 - 21295:00

will be more and more tasks that can be

## 21295:00 - 21310:00

fully automated.

## 21310:00 - 21355:00

>> Can you say more about what you think

## 21355:00 - 21375:00

the world is going to look like with

## 21375:00 - 21430:00

this human to AI loop collaboration?

## 21430:00 - 21465:00

because there's the essay from Dario

## 21465:00 - 21520:00

with machines of love and grace that he

## 21520:00 - 21550:00

paints this picture that's very

## 21550:00 - 21595:00

optimistic and what are the details of

## 21595:00 - 21645:00

how we get there with with this book?

## 21645:00 - 21690:00

>> I think that we already see some of some

## 21690:00 - 21725:00

of that happening. So at least when I

## 21725:00 - 21770:00

talk to folks who work in say biomedical

## 21770:00 - 21825:00

research um with the right sort of

## 21825:00 - 21860:00

orchestration I think it's possible to

## 21860:00 - 21950:00

take frontier AI models now and produce

## 21950:00 - 22005:00

interesting valuable insights for say

## 22005:00 - 22045:00

drug discovery. Um so I think that's

## 22045:00 - 22085:00

already starting to happen. I guess an

## 22085:00 - 22120:00

aspect of it that that I think about is

## 22120:00 - 22170:00

that like there there's sort of

## 22170:00 - 22195:00

intelligence that requires a lot of

## 22195:00 - 22250:00

depth um and and intelligence that

## 22250:00 - 22270:00

requires a lot of breadth. So for

## 22270:00 - 22325:00

example in math you can sort of work on

## 22325:00 - 22365:00

trying to prove one theorem for a decade

## 22365:00 - 22400:00

like the threemon hypothesis or firmat's

## 22400:00 - 22440:00

last theorem. Um I think that's that's

## 22440:00 - 22470:00

sort of solving one very specific very

## 22470:00 - 22515:00

hard problem. I think there's a lot of

## 22515:00 - 22555:00

areas of science, probably more so in

## 22555:00 - 22595:00

biology, maybe interestingly in

## 22595:00 - 22650:00

psychology or or history, where putting

## 22650:00 - 22715:00

together a very very large number of

## 22715:00 - 22765:00

pieces of information um across many

## 22765:00 - 22800:00

many different areas is kind of where

## 22800:00 - 22850:00

it's at. And I think that AI models

## 22850:00 - 22885:00

during the pre-training phase kind of

## 22885:00 - 22945:00

embibe all of human civilization's

## 22945:00 - 22980:00

knowledge. And so I suspect that there's

## 22980:00 - 23050:00

a lot of uh fruit to be picked in using

## 23050:00 - 23095:00

that sort of feature of AI that it knows

## 23095:00 - 23140:00

much much more than any one human expert

## 23140:00 - 23200:00

and therefore you can kind of elicit um

## 23200:00 - 23240:00

insights putting together many different

## 23240:00 - 23285:00

uh many different areas of expertise say

## 23285:00 - 23325:00

across biology for for for research. So

## 23325:00 - 23370:00

I think that um we're making a lot of

## 23370:00 - 23420:00

progress on making AI better at deeper

## 23420:00 - 23450:00

tasks like hard coding problems, hard

## 23450:00 - 23480:00

math problems, but I suspect that

## 23480:00 - 23520:00

there's a particular overhang in areas

## 23520:00 - 23565:00

where putting together knowledge that

## 23565:00 - 23610:00

maybe no one human expert would have

## 23610:00 - 23655:00

where that kind of intelligence is is is

## 23655:00 - 23685:00

very useful. So I think that's something

## 23685:00 - 23740:00

that I' I'd expect to see more of. Um is

## 23740:00 - 23775:00

sort of leveraging AI's sort of breadth

## 23775:00 - 23825:00

of knowledge. In terms of how exactly it

## 23825:00 - 23860:00

will roll out, I really don't know. It's

## 23860:00 - 23880:00

really really hard to predict the

## 23880:00 - 23940:00

future. Scaling laws give you one way of

## 23940:00 - 23965:00

predicting the future which says this

## 23965:00 - 24000:00

trend is going to continue. I think a

## 24000:00 - 24055:00

lot of trends that we see

## 24055:00 - 24095:00

over the long haul I expect will

## 24095:00 - 24150:00

continue. I mean the economy, the GDP,

## 24150:00 - 24190:00

uh the these kinds of trends are really

## 24190:00 - 24220:00

reliable indicators of the future. But I

## 24220:00 - 24250:00

think in terms of in detail how will

## 24250:00 - 24270:00

things be implemented, I think it's

## 24270:00 - 24290:00

really really hard to say.

## 24290:00 - 24345:00

>> Are there specific areas that you think

## 24345:00 - 24395:00

a lot more builders could go into and

## 24395:00 - 24425:00

build with these new models? I mean

## 24425:00 - 24450:00

there's a lot that has been done let's

## 24450:00 - 24500:00

say for coding tasks but what are some

## 24500:00 - 24535:00

tasks that have a lot more green field

## 24535:00 - 24575:00

that are just getting unlocked right now

## 24575:00 - 24610:00

with the current models

## 24610:00 - 24640:00

>> I come from a research background rather

## 24640:00 - 24685:00

than uh rather than business so I don't

## 24685:00 - 24720:00

I don't know that I have anything very

## 24720:00 - 24745:00

uh very deep to say but I think that

## 24745:00 - 24825:00

like in general any place where um it

## 24825:00 - 24875:00

requires a lot of skill um and it's a

## 24875:00 - 24915:00

task that mostly involves sort

## 24915:00 - 24935:00

sitting in front of a computer

## 24935:00 - 24995:00

interacting with data. I think finance

## 24995:00 - 25025:00

uh people who use Excel spreadsheets a

## 25025:00 - 25100:00

lot. Um I think I I expect law although

## 25100:00 - 25160:00

maybe maybe maybe law uh is is is more

## 25160:00 - 25200:00

regulated requires more uh more more

## 25200:00 - 25240:00

expertise um as a stamp of approval. But

## 25240:00 - 25275:00

I think all of these areas are probably

## 25275:00 - 25325:00

green field. I think another that that I

## 25325:00 - 25385:00

sort of mentioned is how do we integrate

## 25385:00 - 25435:00

AI into existing businesses? I think

## 25435:00 - 25475:00

that like when electricity came along,

## 25475:00 - 25515:00

there was some long adoption cycle and

## 25515:00 - 25555:00

the very first simplest ways of say

## 25555:00 - 25600:00

using electricity weren't necessarily uh

## 25600:00 - 25645:00

the best. You wanted to not just replace

## 25645:00 - 25685:00

a steam engine with an electric motor.

## 25685:00 - 25715:00

You wanted to sort of remake the way

## 25715:00 - 25745:00

that factories work. And I think that

## 25745:00 - 25805:00

probably leveraging AI to integrate AI

## 25805:00 - 25850:00

into parts of the economy um as quickly

## 25850:00 - 25885:00

as possible. I expect there's just a lot

## 25885:00 - 25910:00

of a lot of leverage there.

## 25910:00 - 25940:00

>> Now other question is you have a

## 25940:00 - 25995:00

extensive training as a physicist and

## 25995:00 - 26020:00

you were one of the first to really

## 26020:00 - 26070:00

observe this trend with scaling laws and

## 26070:00 - 26105:00

it probably comes from being a physicist

## 26105:00 - 26160:00

and seeing all these exponentials that

## 26160:00 - 26240:00

happen naturally in nature. How has that

## 26240:00 - 26290:00

training come about with uh being able

## 26290:00 - 26330:00

to perform like the best research in the

## 26330:00 - 26370:00

world with with with with AI?

## 26370:00 - 26410:00

>> I think the thing that was useful from a

## 26410:00 - 26470:00

physics point of view is looking for the

## 26470:00 - 26520:00

biggest picture, most macro trends and

## 26520:00 - 26560:00

then trying to make them as precise as

## 26560:00 - 26605:00

possible. So I remember meeting like

## 26605:00 - 26640:00

kind of brilliant AI researchers who

## 26640:00 - 26685:00

would say things like learning is

## 26685:00 - 26720:00

converging exponentially

## 26720:00 - 26765:00

and I would just ask really dumb

## 26765:00 - 26785:00

questions like are you sure it's an

## 26785:00 - 26820:00

exponential? Could it just be a power

## 26820:00 - 26875:00

law? Is it quadratic? Like like exactly

## 26875:00 - 26930:00

how is this thing converging? And it's a

## 26930:00 - 26960:00

really dumb kind of simple question to

## 26960:00 - 26995:00

ask, but basically I think there was a

## 26995:00 - 27025:00

lot of fruit to be picked and and

## 27025:00 - 27075:00

probably still is in trying to make the

## 27075:00 - 27105:00

big trends that you see as precise as

## 27105:00 - 27140:00

possible because that I don't know it

## 27140:00 - 27160:00

gives you a lot of tools. It allows you

## 27160:00 - 27195:00

to ask like what does it really mean to

## 27195:00 - 27225:00

move the needle? I think with scaling

## 27225:00 - 27295:00

laws, the the holy grail is finding a

## 27295:00 - 27325:00

better slope to the scaling law because

## 27325:00 - 27360:00

that means that as you put in more

## 27360:00 - 27400:00

compute, you're going to get a bigger

## 27400:00 - 27450:00

and bigger advantage over other AI

## 27450:00 - 27500:00

developers. Um, but until you've sort of

## 27500:00 - 27545:00

made precise what the trend is that you

## 27545:00 - 27585:00

see, you sort of don't know exactly what

## 27585:00 - 27620:00

it means to beat it and and how much you

## 27620:00 - 27660:00

can beat it by and how to know

## 27660:00 - 27690:00

systematically whether you're you're

## 27690:00 - 27715:00

you're achieving that end. So, I think

## 27715:00 - 27755:00

those were kind of the tools that that I

## 27755:00 - 27795:00

think I used. It wasn't necessarily like

## 27795:00 - 27830:00

literally applying say quantum field

## 27830:00 - 27880:00

theory to AI. I think that's uh that's a

## 27880:00 - 27910:00

little bit too specific. Well, are there

## 27910:00 - 27950:00

specific uh physics heruristics like

## 27950:00 - 27990:00

reormalization, symmetry that came in

## 27990:00 - 28050:00

very handy to really keep observing this

## 28050:00 - 28085:00

trend or or measuring it?

## 28085:00 - 28110:00

>> Something that you'll observe if you

## 28110:00 - 28150:00

look at AI models is that they're big.

## 28150:00 - 28170:00

Neural networks are big. They have

## 28170:00 - 28210:00

billions now trillions of parameters.

## 28210:00 - 28255:00

That means that they're made out of big

## 28255:00 - 28325:00

matrices. and basically studying uh

## 28325:00 - 28355:00

approximations

## 28355:00 - 28390:00

where you

## 28390:00 - 28420:00

take the limit that neural networks are

## 28420:00 - 28465:00

very big and specifically that the uh

## 28465:00 - 28495:00

matrices that compose neural networks

## 28495:00 - 28515:00

are big. That's actually been kind of

## 28515:00 - 28535:00

useful and that's something that

## 28535:00 - 28575:00

actually was a well-known approximation

## 28575:00 - 28630:00

in in physics um and and in math. Um

## 28630:00 - 28650:00

that's something that's been applied.

## 28650:00 - 28685:00

But I think generally it's really asking

## 28685:00 - 28720:00

very naive dumb questions that gets you

## 28720:00 - 28760:00

very far. I think AI is really in a

## 28760:00 - 28805:00

certain sense only like maybe 101 15

## 28805:00 - 28830:00

years old in terms of the current

## 28830:00 - 28870:00

incarnation of how we're training AI

## 28870:00 - 28895:00

models. That means that it's an

## 28895:00 - 28945:00

incredibly new field. A lot of the most

## 28945:00 - 28975:00

basic questions haven't been answered

## 28975:00 - 29020:00

like questions of interpretability, how

## 29020:00 - 29055:00

AI models really work. And so I think

## 29055:00 - 29105:00

there's there's really a lot to uh to

## 29105:00 - 29150:00

learn at that level rather than applying

## 29150:00 - 29195:00

very very fancy techniques. Are there

## 29195:00 - 29235:00

specific tools in physics that you apply

## 29235:00 - 29265:00

for interpretability?

## 29265:00 - 29290:00

>> I would say that interpretability is a

## 29290:00 - 29320:00

lot more like biology. It's a lot more

## 29320:00 - 29355:00

like neuroscience. So I think those are

## 29355:00 - 29395:00

kind of the tools. Um there there is

## 29395:00 - 29435:00

there is some more more more mathematics

## 29435:00 - 29465:00

there. But I I think it's more like

## 29465:00 - 29505:00

trying to understand the features of the

## 29505:00 - 29555:00

brain. Um the benefit that you get with

## 29555:00 - 29610:00

AI over neuroscience is that um you can

## 29610:00 - 29645:00

really measure everything in AI. You

## 29645:00 - 29685:00

can't measure the the activity of every

## 29685:00 - 29725:00

neuron, every syninnapse in a brain, but

## 29725:00 - 29755:00

you can do that in AI. So there's much

## 29755:00 - 29805:00

much much more data for reverse

## 29805:00 - 29835:00

engineering how AI models work.

## 29835:00 - 29870:00

>> Now when aspect about scaling laws,

## 29870:00 - 29930:00

they've held for over five orders of

## 29930:00 - 29980:00

magnitude, which is wild. This is a bit

## 29980:00 - 30020:00

of a contrarian question, but what

## 30020:00 - 30085:00

empirical sign would convince you that

## 30085:00 - 30125:00

the curve are changing that maybe we're

## 30125:00 - 30150:00

getting off the curve?

## 30150:00 - 30175:00

>> I think it's a really I think it's a

## 30175:00 - 30205:00

really hard question, right? Because I

## 30205:00 - 30235:00

mostly use scaling laws to diagnose

## 30235:00 - 30275:00

whether AI training is broken or not.

## 30275:00 - 30280:00

Mh.

## 30280:00 - 30330:00

>> So I think that uh once you see

## 30330:00 - 30365:00

something and you find it very it's a

## 30365:00 - 30405:00

very compelling trend, it becomes very

## 30405:00 - 30450:00

very interesting to examine

## 30450:00 - 30490:00

where it's failing. But I think that my

## 30490:00 - 30535:00

first inclination is to think if scaling

## 30535:00 - 30575:00

laws are failing, it's because we've

## 30575:00 - 30610:00

screwed up AI training in some way.

## 30610:00 - 30660:00

Maybe we got uh we got the architecture

## 30660:00 - 30700:00

of the neural network wrong or there's

## 30700:00 - 30725:00

some bottleneck in training that we

## 30725:00 - 30760:00

don't see or there's some problem with

## 30760:00 - 30795:00

precision in the algorithms that we're

## 30795:00 - 30850:00

using. So I think it would take a lot to

## 30850:00 - 30900:00

convince me at least that scaling was

## 30900:00 - 30925:00

really no longer working at the level of

## 30925:00 - 30960:00

the sort of these empirical laws because

## 30960:00 - 31000:00

so many times in my experience over the

## 31000:00 - 31030:00

last 5 years when it seemed like scaling

## 31030:00 - 31060:00

was broken it was because we were doing

## 31060:00 - 31070:00

it wrong.

## 31070:00 - 31105:00

>> Interesting. So I guess going into

## 31105:00 - 31135:00

something very specific that goes hand

## 31135:00 - 31175:00

in hand is a lot of the compute power

## 31175:00 - 31230:00

required to go keep going on this curve.

## 31230:00 - 31290:00

What happens uh as compute becomes more

## 31290:00 - 31350:00

more scarce how far down do you go into

## 31350:00 - 31395:00

the precision ladder like do you explore

## 31395:00 - 31440:00

things like FP4 do you explore things

## 31440:00 - 31480:00

like turnary representations what what

## 31480:00 - 31510:00

are your thoughts around that? Yeah, I

## 31510:00 - 31575:00

mean I think that um right now AI is

## 31575:00 - 31615:00

really inefficient because there's a lot

## 31615:00 - 31660:00

of value in AI. So um there's a lot of

## 31660:00 - 31730:00

value in unlocking the most capable

## 31730:00 - 31790:00

frontier model. Um and so companies like

## 31790:00 - 31825:00

Anthropic and others are moving as

## 31825:00 - 31875:00

quickly as we can to both make AI

## 31875:00 - 31910:00

training more efficient and AI inference

## 31910:00 - 31940:00

more efficient as well as unlocking

## 31940:00 - 31970:00

frontier capabilities. But a lot of the

## 31970:00 - 32010:00

focus really is on uh unlocking the

## 32010:00 - 32090:00

frontier. I think that over time as AI

## 32090:00 - 32135:00

becomes more and more widespread, I

## 32135:00 - 32180:00

think that we're going to really drive

## 32180:00 - 32230:00

down the cost of inference and training

## 32230:00 - 32255:00

dramatically from where we are right

## 32255:00 - 32295:00

now. I mean right now we're seeing sort

## 32295:00 - 32365:00

of 3x to 10x gains algorithmically and

## 32365:00 - 32425:00

in sort of scaling up compute um and in

## 32425:00 - 32490:00

uh inference efficiency per year. I

## 32490:00 - 32520:00

guess like the joke is that we're going

## 32520:00 - 32560:00

to get computers back into binary. So I

## 32560:00 - 32600:00

think that we will see much much lower

## 32600:00 - 32635:00

precision as one of the many avenues to

## 32635:00 - 32685:00

make inference more efficient over time.

## 32685:00 - 32725:00

But sort of we h we're very very very

## 32725:00 - 32760:00

out of equilibrium with AI development

## 32760:00 - 32795:00

right now. AI is improving very rapidly.

## 32795:00 - 32825:00

Things are changing very rapidly. We

## 32825:00 - 32865:00

haven't fully realized the potential of

## 32865:00 - 32900:00

current models, but we're unlocking more

## 32900:00 - 32930:00

and more capabilities. So I think that

## 32930:00 - 32970:00

what the equilibrium situation looks

## 32970:00 - 33020:00

like where AI isn't changing that

## 33020:00 - 33055:00

quickly, I think is one where AI is

## 33055:00 - 33095:00

extremely inexpensive, but it's sort of

## 33095:00 - 33115:00

hard to know if we're even going to get

## 33115:00 - 33150:00

there. like AI may just keep getting

## 33150:00 - 33195:00

better so quickly that uh sort of

## 33195:00 - 33230:00

improvements in int intelligence unlock

## 33230:00 - 33260:00

so much more and so we may continue to

## 33260:00 - 33305:00

focus on that rather than say getting

## 33305:00 - 33365:00

precision down to FP2

## 33365:00 - 33410:00

>> which is very much uh the Jebans paradox

## 33410:00 - 33445:00

as intelligence becomes better and

## 33445:00 - 33485:00

better people are going to want it more

## 33485:00 - 33520:00

not that is driving the cost down which

## 33520:00 - 33555:00

is this irony right

## 33555:00 - 33595:00

>> yeah absolutely I mean I think that uh

## 33595:00 - 33615:00

yeah that's that's certainly certainly

## 33615:00 - 33635:00

something that we've seen that there are

## 33635:00 - 33685:00

certain uh certain points where AI

## 33685:00 - 33750:00

becomes accessible enough. That said, um

## 33750:00 - 33800:00

I think as AI systems become more and

## 33800:00 - 33850:00

more capable um and can do more and more

## 33850:00 - 33885:00

of the work that that we do, it's going

## 33885:00 - 33925:00

to be worth it to pay for uh frontier

## 33925:00 - 33965:00

capabilities. I think it's a question

## 33965:00 - 34005:00

that I've always had and can have is

## 34005:00 - 34040:00

kind of like is all of the value at the

## 34040:00 - 34085:00

frontier or is there a lot of value with

## 34085:00 - 34120:00

kind of cheaper systems that aren't

## 34120:00 - 34155:00

quite as capable? And I think the sort

## 34155:00 - 34190:00

of time horizon picture is maybe one way

## 34190:00 - 34230:00

of thinking about this. I think that you

## 34230:00 - 34265:00

can do a lot of very simple bite-sized

## 34265:00 - 34300:00

tasks, but I think it's just much more

## 34300:00 - 34350:00

convenient to be able to use an AI model

## 34350:00 - 34390:00

that can do a very complex task end to

## 34390:00 - 34435:00

end rather than requiring us as humans

## 34435:00 - 34470:00

to sort of orchestrate a much dumber

## 34470:00 - 34500:00

model to break the task down into very

## 34500:00 - 34535:00

very small slices and put them together.

## 34535:00 - 34560:00

So, I do kind of expect that a lot of

## 34560:00 - 34595:00

the value is going to come from the most

## 34595:00 - 34645:00

capable models, but I might be wrong. It

## 34645:00 - 34670:00

it might depend and it might really

## 34670:00 - 34715:00

depend on the capabilities of AI

## 34715:00 - 34745:00

integrators to sort of leverage AI

## 34745:00 - 34765:00

really efficiently.

## 34765:00 - 34805:00

>> What advice would you give this audience

## 34805:00 - 34840:00

which there everyone is early in the

## 34840:00 - 34875:00

career with lots of potential in terms

## 34875:00 - 34920:00

of how do you stay relevant in the

## 34920:00 - 34955:00

future where all these models are going

## 34955:00 - 34995:00

to become so awesome. What should

## 34995:00 - 35055:00

everyone be really good at and study and

## 35055:00 - 35105:00

to still do really good work? I think as

## 35105:00 - 35160:00

I mentioned there's a lot of value in

## 35160:00 - 35200:00

understanding how these models work and

## 35200:00 - 35225:00

being able to really efficiently

## 35225:00 - 35265:00

leverage them and and integrate them and

## 35265:00 - 35290:00

I think there's a lot of value in kind

## 35290:00 - 35325:00

of like building building at the

## 35325:00 - 35355:00

frontier. Um I don't know we could turn

## 35355:00 - 35385:00

it over to the audience for for

## 35385:00 - 35390:00

questions.

## 35390:00 - 35410:00

>> Let's turn it out to the audience for

## 35410:00 - 35440:00

some questions.

## 35440:00 - 35460:00

>> I had a quick question on the scaling

## 35460:00 - 35500:00

loss. You show that a lot of the scaling

## 35500:00 - 35540:00

laws are like linear that like the more

## 35540:00 - 35565:00

we have exponential compute going up but

## 35565:00 - 35605:00

then like we have linear progress in uh

## 35605:00 - 35635:00

in the scaling loss but then on your

## 35635:00 - 35675:00

last slide you show that you expect then

## 35675:00 - 35705:00

suddenly like an exponential growth in

## 35705:00 - 35750:00

like how much time we save. I want to

## 35750:00 - 35780:00

ask you like why do you think that

## 35780:00 - 35810:00

suddenly on this chart we're exponential

## 35810:00 - 35845:00

and not linear anymore?

## 35845:00 - 35865:00

Thank you.

## 35865:00 - 35890:00

>> Yeah, this is a really good question and

## 35890:00 - 35940:00

I don't know. Um I mean the meter

## 35940:00 - 35970:00

finding was kind of an empirical

## 35970:00 - 36020:00

finding. Um the way that I tend to think

## 36020:00 - 36070:00

about this is that um in order to do

## 36070:00 - 36100:00

more and more complex logger horizon

## 36100:00 - 36150:00

tasks um what you really need is some

## 36150:00 - 36200:00

ability to self-correct. You need to be

## 36200:00 - 36225:00

able to sort of identify that you've

## 36225:00 - 36255:00

you've you make a plan and then you

## 36255:00 - 36280:00

start executing in the plan. But

## 36280:00 - 36310:00

everyone knows that our plans are kind

## 36310:00 - 36365:00

of worthless and uh and we encounter

## 36365:00 - 36410:00

reality. we get things wrong. And so I

## 36410:00 - 36435:00

think that a lot of what determines the

## 36435:00 - 36470:00

horizon length of what models can

## 36470:00 - 36500:00

accomplish is their ability to notice

## 36500:00 - 36535:00

that they're doing something wrong and

## 36535:00 - 36580:00

and correct it. Um, and I think that's

## 36580:00 - 36605:00

not sort of like a lot of bits of

## 36605:00 - 36630:00

information. It doesn't necessarily

## 36630:00 - 36670:00

require a huge change in intelligence to

## 36670:00 - 36710:00

sort of notice one or two more times

## 36710:00 - 36735:00

that you've made a mistake and how to

## 36735:00 - 36770:00

correct that mistake. But if you sort of

## 36770:00 - 36810:00

fix your mistake, maybe you sort of on

## 36810:00 - 36845:00

the order sort of double the horizon

## 36845:00 - 36875:00

length of the task because like instead

## 36875:00 - 36905:00

of getting stuck here, you get stuck

## 36905:00 - 36945:00

twice as far twice as far out. So I

## 36945:00 - 36965:00

think that's sort of the picture that I

## 36965:00 - 36990:00

have that like you can kind of unlock

## 36990:00 - 37025:00

longer and longer horizons with

## 37025:00 - 37070:00

relatively modest improvements in your

## 37070:00 - 37115:00

kind of ability to understand the task

## 37115:00 - 37150:00

and self-correct. But that just kind of

## 37150:00 - 37185:00

like those are just words. I think the

## 37185:00 - 37220:00

empirical trend is maybe the most

## 37220:00 - 37260:00

interesting thing. And uh maybe we can

## 37260:00 - 37300:00

build more detailed models for why that

## 37300:00 - 37330:00

trend is true, but it's sort of your

## 37330:00 - 37365:00

guess is as good as mine.

## 37365:00 - 37400:00

>> Yeah. So I also have a question over

## 37400:00 - 37435:00

here. Um so it's an honor. Um so

## 37435:00 - 37480:00

basically um in terms of um increasing

## 37480:00 - 37520:00

the time horizon, I feel like so my

## 37520:00 - 37545:00

mental model of neuronet networks is

## 37545:00 - 37565:00

very simple. If you want them to do

## 37565:00 - 37615:00

something, you train on such data. Um so

## 37615:00 - 37650:00

if you want them to um if you want to

## 37650:00 - 37685:00

increase the um time horizon you have to

## 37685:00 - 37710:00

slowly get for example verification

## 37710:00 - 37750:00

signals. Now um I think one way to do

## 37750:00 - 37785:00

this is via product. So like for example

## 37785:00 - 37810:00

um cloud agent and then you use the

## 37810:00 - 37840:00

verification signal to incrementally

## 37840:00 - 37875:00

improve the model. Now my question is

## 37875:00 - 37905:00

basically this works really nicely for

## 37905:00 - 37930:00

for example coding where you have a

## 37930:00 - 37955:00

product that is sufficiently good such

## 37955:00 - 37990:00

that you can deploy it and then get the

## 37990:00 - 38020:00

verification signal but what about other

## 38020:00 - 38050:00

domains like in other domains are we

## 38050:00 - 38110:00

just um scaling data labelers to AGI or

## 38110:00 - 38150:00

is there a better approach? Yeah, it's a

## 38150:00 - 38215:00

good question. I mean, um, so when when

## 38215:00 - 38285:00

sort of skeptics ask me sort of why do I

## 38285:00 - 38330:00

think we will be able to sort of scale

## 38330:00 - 38365:00

and get something like broadly human

## 38365:00 - 38410:00

level AI, it's basically because of of

## 38410:00 - 38445:00

what you said. there is some sort of

## 38445:00 - 38490:00

very kind of operationally intensive

## 38490:00 - 38525:00

path where you just sort of build more

## 38525:00 - 38565:00

and more different tasks for AI models

## 38565:00 - 38595:00

to do that are more and more complex,

## 38595:00 - 38635:00

more and more long horizon and you just

## 38635:00 - 38680:00

sort of turn the crank and train with RL

## 38680:00 - 38715:00

on those those more more complicated

## 38715:00 - 38745:00

tasks. So I sort of feel like that's the

## 38745:00 - 38800:00

worst case for AI progress. And I mean

## 38800:00 - 38845:00

given the level of investment in AI and

## 38845:00 - 38875:00

I think the the sort of level of value

## 38875:00 - 38915:00

that I think is being created with AI, I

## 38915:00 - 38955:00

think people will do that if necessary.

## 38955:00 - 38985:00

That said, I think there are a lot of

## 38985:00 - 39030:00

ways of sort of making it simpler. The

## 39030:00 - 39085:00

best is to have an AI model that is

## 39085:00 - 39160:00

trained to oversee and supervise what uh

## 39160:00 - 39190:00

claw like you have claude say which

## 39190:00 - 39220:00

you're training to be clawed when you

## 39220:00 - 39240:00

have another AI model that's sort of

## 39240:00 - 39295:00

providing supervision and is not just

## 39295:00 - 39325:00

saying did you do this incredibly

## 39325:00 - 39385:00

complicated task correctly like did you

## 39385:00 - 39420:00

become a faculty member and get tenure

## 39420:00 - 39450:00

will that take six or seven years is

## 39450:00 - 39475:00

that like an endto-end task where at the

## 39475:00 - 39500:00

end you sort of either get tenure or not

## 39500:00 - 39540:00

over seven that's that's ridiculous.

## 39540:00 - 39570:00

That's very inefficient. But instead can

## 39570:00 - 39610:00

provide more detailed supervision that

## 39610:00 - 39640:00

says you're doing this well, you're

## 39640:00 - 39675:00

doing this poorly. Um I think that sort

## 39675:00 - 39715:00

of as we're able to use AI more and more

## 39715:00 - 39755:00

in that kind of way, we'll probably be

## 39755:00 - 39785:00

able to make training for very long

## 39785:00 - 39815:00

horizon tasks more efficient and I think

## 39815:00 - 39850:00

we're already doing this to some extent.

## 39850:00 - 39885:00

>> We'll do one last question.

## 39885:00 - 39920:00

>> Yeah, I wanted to build on top of that.

## 39920:00 - 39950:00

when you're basically developing like

## 39950:00 - 39990:00

these tasks and then training them with

## 39990:00 - 40040:00

RL, would are you like like would you

## 40040:00 - 40080:00

like try creating these tasks like using

## 40080:00 - 40120:00

large language models like the tasks you

## 40120:00 - 40150:00

use for RL or are you still using

## 40150:00 - 40165:00

humans?

## 40165:00 - 40215:00

>> Great question. So I would say a mix. Um

## 40215:00 - 40240:00

I mean obviously we're building the

## 40240:00 - 40285:00

tasks as much as possible using AI to

## 40285:00 - 40340:00

sort of like say generate tasks with

## 40340:00 - 40415:00

code. we do like also uh ask humans to

## 40415:00 - 40450:00

create tasks. So it's it's basically

## 40450:00 - 40490:00

some mixture of those things. Um I think

## 40490:00 - 40530:00

that as AI gets better and better,

## 40530:00 - 40555:00

hopefully we're able to leverage AI more

## 40555:00 - 40585:00

and more, but of course the frontier of

## 40585:00 - 40615:00

the difficulty of these tasks also

## 40615:00 - 40655:00

increases. So I think humans are are are

## 40655:00 - 40675:00

still going to be involved.

## 40675:00 - 40695:00

>> Okay. Thank you.

## 40695:00 - 40720:00

>> All right. Let's give it a round of

## 40720:00 - 40755:00

applause to Jared.

## 40755:00+

>> Thank you so much. Thanks.

