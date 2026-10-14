---
source: https://www.youtube.com/watch?v=a8-QsBHoH94
title: "Chelsea Finn: Building Robots That Can Do Anything"
author: Y Combinator
date: 2025-07-22
views: 92159
description: >-
  Chelsea Finn on June 17th, 2025 at AI Startup School in San Francisco.


  From MIT through her PhD at Berkeley, where she pioneered meta‑learning
  methods, and Google Brain, Chelsea Finn has built her career around teaching
  machines how to learn. Now an Assistant Professor at Stanford and co‑founder
  of Physical Intelligence, she’s using that foundation to bring learning-driven
  robotics into messy, real-world environments rather than confined lab setups.


  In this talk, Chelsea traces the evolution of her team’s work—from early
  experiments on robotic grasping and vision to today’s ambitious efforts at
  folding laundry, tidying kitchens, and generalizing across tasks—all without
  hand-crafted code. Instead, they used scalable foundation models and massive
  datasets, teaching robots physical common sense as they learn by doing. 


  She shares stories of the rocky setbacks, the surprises hidden in data, and
  the moment it all clicked: robots equipped with generalizable physical
  intelligence can indeed adapt and assist in the unpredictable world around us.


  Apply to Y Combinator: https://ycombinator.com/apply

  Work at a startup: https://workatastartup.com


  Chapters:

  00:00 - General Purpose Robots

  00:11 - Challenges in Robotics Applications

  00:57 - Physical Intelligence: A New Approach

  01:47 - Learning from Language Models

  02:08 - Data Sources for Training Robots

  03:32 - Training with Real-World Data

  04:39 - Initial Successes and Challenges

  09:10 - Breakthrough in Robot Training

  11:03 - Improving Performance

  15:43 - Expanding Capabilities

  17:34 - Robots in Unseen Environments

  25:54 - Handling Open-Ended Prompts

  29:36 - Evaluating Robot Performance

  30:03 - Future Directions and Challenges

  31:27 - Audience Q&A
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:43:44.092Z
---

# Chelsea Finn: Building Robots That Can Do Anything

## 00:00 - 35:00

Hi everyone. Um, I'm really excited to

## 35:00 - 65:00

talk about developing general purpose

## 65:00 - 120:00

robots and how we might uh actually like

## 120:00 - 150:00

truly develop and bring intelligence

## 150:00 - 205:00

into the physical world. So, um, to

## 205:00 - 245:00

start off, I'd like to talk about this

## 245:00 - 280:00

problem, which is that if you want to

## 280:00 - 325:00

truly solve a robotics application, you

## 325:00 - 345:00

essentially need to build an entire

## 345:00 - 400:00

company around that application. uh you

## 400:00 - 420:00

need to build a different company for

## 420:00 - 470:00

logistics, for wet lab automation, for

## 470:00 - 515:00

robots and kitchens, for surgical robots

## 515:00 - 565:00

and so on. And this is really really

## 565:00 - 600:00

hard to do because that company needs to

## 600:00 - 630:00

make new hardware, develop custom

## 630:00 - 660:00

software, design unique movement

## 660:00 - 690:00

primitives for that application, handle

## 690:00 - 725:00

edge cases and so on. And you have to do

## 725:00 - 760:00

all of that from scratch uh if you want

## 760:00 - 805:00

to solve a robotics problem. And as a

## 805:00 - 845:00

result, uh, a lot of robotics companies

## 845:00 - 880:00

haven't been very successful in actually

## 880:00 - 915:00

bringing robots into the physical world

## 915:00 - 960:00

successfully, uh, in our daily lives. I

## 960:00 - 985:00

co-founded a company called physical

## 985:00 - 1020:00

intelligence, uh, that's trying to solve

## 1020:00 - 1060:00

this problem. And in particular, we're

## 1060:00 - 1085:00

trying to develop a general purpose

## 1085:00 - 1125:00

model that can enable any robot to do

## 1125:00 - 1190:00

any task in any environment. uh and we

## 1190:00 - 1240:00

think that this sort of generalist model

## 1240:00 - 1290:00

may work better and be easier to use

## 1290:00 - 1320:00

than purpose-built models just like

## 1320:00 - 1365:00

we've seen in the development of found

## 1365:00 - 1400:00

foundation models for language and other

## 1400:00 - 1435:00

applications. Uh for example, if you

## 1435:00 - 1475:00

want to build uh a coding assistant, you

## 1475:00 - 1510:00

don't nowadays develop something

## 1510:00 - 1545:00

specifically for coding, but you develop

## 1545:00 - 1565:00

and you build on models that were

## 1565:00 - 1600:00

trained on large amounts of data, not

## 1600:00 - 1640:00

just on code. And essentially this is

## 1640:00 - 1665:00

the problem of trying to develop these

## 1665:00 - 1685:00

sorts of foundation models and bring

## 1685:00 - 1715:00

this sort of intelligence into the

## 1715:00 - 1750:00

physical world rather than the digital

## 1750:00 - 1805:00

world where they largely are today. So

## 1805:00 - 1845:00

how do we do this? Uh in this talk I'd

## 1845:00 - 1875:00

like to talk about how we go about doing

## 1875:00 - 1940:00

this. And if we were to take a lesson

## 1940:00 - 1960:00

from language models we know that

## 1960:00 - 1980:00

language models have taught us the

## 1980:00 - 2035:00

importance of scale. And so one possible

## 2035:00 - 2075:00

conclusion would be that perhaps scale

## 2075:00 - 2110:00

is the most important ingredient for

## 2110:00 - 2155:00

developing these models. And if you were

## 2155:00 - 2245:00

to say this conclusion is true, then

## 2245:00 - 2280:00

you might look to certain data sources

## 2280:00 - 2320:00

for largecale uh data. So for example,

## 2320:00 - 2355:00

we might look at data from industrial

## 2355:00 - 2390:00

automation and you get tons and tons of

## 2390:00 - 2440:00

data of robots uh doing tasks over and

## 2440:00 - 2470:00

over again like this. But this sort of

## 2470:00 - 2510:00

data isn't going to allow robots to go

## 2510:00 - 2540:00

into disaster zones or to make a

## 2540:00 - 2595:00

sandwich uh or to bag groceries. And so

## 2595:00 - 2635:00

this massive scale doesn't have the

## 2635:00 - 2670:00

diversity of behaviors that we need in

## 2670:00 - 2710:00

order to solve this general problem.

## 2710:00 - 2730:00

Alternatively, maybe we look at data

## 2730:00 - 2770:00

from YouTube which has a also a massive

## 2770:00 - 2800:00

data source and many videos of humans

## 2800:00 - 2830:00

doing tasks uh that could be useful for

## 2830:00 - 2870:00

training robots. uh but at the same time

## 2870:00 - 2895:00

we don't learn how to write by watching

## 2895:00 - 2920:00

other people write and we don't become

## 2920:00 - 2945:00

expert tennis players by watching

## 2945:00 - 2980:00

Wimbledon. Uh and so even though there's

## 2980:00 - 3015:00

a massive scale of data here, it's very

## 3015:00 - 3045:00

challenging to use and there's also a a

## 3045:00 - 3080:00

gap between the embodiment of robots and

## 3080:00 - 3120:00

humans. Um and lastly, we might look at

## 3120:00 - 3150:00

data from simulation and you can also

## 3150:00 - 3190:00

get a massive scale of data here, but uh

## 3190:00 - 3235:00

this data lacks realism and also has a

## 3235:00 - 3270:00

gap from reality. And so I think the

## 3270:00 - 3320:00

lesson here is that scale is necessary

## 3320:00 - 3355:00

for developing these models that can

## 3355:00 - 3395:00

generalize in open world conditions, but

## 3395:00 - 3420:00

they're subordinate to actually solving

## 3420:00 - 3455:00

the problem. So you need scale, but it's

## 3455:00 - 3480:00

not sufficient uh for the entire

## 3480:00 - 3505:00

problem. And so at physical

## 3505:00 - 3540:00

intelligence, we've been um this is an

## 3540:00 - 3580:00

example of a data episode uh that we've

## 3580:00 - 3630:00

collected. Uh this is uh in honor of our

## 3630:00 - 3650:00

first anniversary, which was a few

## 3650:00 - 3700:00

months ago. uh where we um here you can

## 3700:00 - 3735:00

see a teley operator uh in person who's

## 3735:00 - 3775:00

operating um some leader arms to control

## 3775:00 - 3825:00

the robot uh to light a match and light

## 3825:00 - 3865:00

a candle with the match and with this

## 3865:00 - 3905:00

sort of data we can train robots to do a

## 3905:00 - 3950:00

variety of different tasks and so um

## 3950:00 - 3975:00

what I'd like to talk about is some of

## 3975:00 - 4025:00

our recent results at trying to develop

## 4025:00 - 4055:00

sort of physical intelligence with

## 4055:00 - 4090:00

largecale real robot data I should

## 4090:00 - 4125:00

mention this is large scale by today's

## 4125:00 - 4170:00

robot standards and arguably a minuscule

## 4170:00 - 4200:00

amount of data compared to the sorts of

## 4200:00 - 4235:00

robot data that we should have in the

## 4235:00 - 4265:00

years to come. And so in particular,

## 4265:00 - 4300:00

we'll be looking at whether robots can

## 4300:00 - 4325:00

do a variety of dextrous long horizon

## 4325:00 - 4355:00

tasks, whether robots can succeed in

## 4355:00 - 4380:00

places they've never been, whether

## 4380:00 - 4410:00

robots can respond to open-ended prompts

## 4410:00 - 4445:00

and interjections. Uh, and even if

## 4445:00 - 4470:00

you're not excited about robotics, I

## 4470:00 - 4505:00

think that the lessons uh that we've

## 4505:00 - 4530:00

learned from trying to address these

## 4530:00 - 4565:00

problems are applicable outside of the

## 4565:00 - 4600:00

physical world. So um can we develop

## 4600:00 - 4630:00

robots that can have uh complete

## 4630:00 - 4665:00

dextrous long horizon tasks? And in

## 4665:00 - 4695:00

particular uh in this first part I'd

## 4695:00 - 4735:00

like to talk about how we trained uh a

## 4735:00 - 4785:00

pi zero foundation model to do this task

## 4785:00 - 4825:00

which is to unload a dryer and fold

## 4825:00 - 4860:00

laundry. Uh and to date I think this is

## 4860:00 - 4900:00

the most impressive thing that I've seen

## 4900:00 - 4940:00

uh a robot do in the physical world.

## 4940:00 - 4970:00

It's really hard.

## 4970:00 - 5070:00

[Applause]

## 5070:00 - 5095:00

This is an incredibly difficult problem.

## 5095:00 - 5120:00

You can see that it's not perfect. Uh

## 5120:00 - 5150:00

here is making some miscrops, making

## 5150:00 - 5175:00

some mistakes, but it's really really

## 5175:00 - 5200:00

hard because you have to deal with the

## 5200:00 - 5245:00

variability in the clothes and the way

## 5245:00 - 5285:00

in which they might be positioned and

## 5285:00 - 5325:00

crumpled uh and be able to handle all

## 5325:00 - 5350:00

those sorts of things. And as you're

## 5350:00 - 5375:00

doing this task, which takes about 10

## 5375:00 - 5400:00

minutes for the robot, there's many

## 5400:00 - 5440:00

opportunities to fail uh to fail

## 5440:00 - 5470:00

catastrophically. For example, dropping

## 5470:00 - 5495:00

um things on the ground, which is hard

## 5495:00 - 5535:00

to recover from. uh and you have to be

## 5535:00 - 5570:00

able to recover from even small

## 5570:00 - 5600:00

mistakes. I was personally actually

## 5600:00 - 5630:00

working quite a bit um on this laundry

## 5630:00 - 5660:00

folding robot along with Michael and

## 5660:00 - 5705:00

Siraj uh and of course supported uh and

## 5705:00 - 5735:00

with contributions from the whole

## 5735:00 - 5775:00

physical intelligence team. Uh so how do

## 5775:00 - 5815:00

you even approach this sort of problem?

## 5815:00 - 5840:00

It's this is a really really hard thing

## 5840:00 - 5885:00

for a robot to do and what we did is we

## 5885:00 - 5935:00

started simple. Uh we started with can a

## 5935:00 - 5975:00

robot fold a single size single brand

## 5975:00 - 6025:00

shirt uh and can a robot dynamically

## 6025:00 - 6065:00

flatten one shirt again single brand

## 6065:00 - 6095:00

single sized and if you start simple

## 6095:00 - 6115:00

this makes the problem quite a bit

## 6115:00 - 6150:00

easier uh we collected some data with

## 6150:00 - 6180:00

teley operation and trained a policy

## 6180:00 - 6210:00

with imitation learning and our model

## 6210:00 - 6240:00

had around 100 million parameters

## 6240:00 - 6275:00

mapping from images from the robot's

## 6275:00 - 6325:00

cameras to joint target joint positions

## 6325:00 - 6360:00

on the robot arms and we do this source

## 6360:00 - 6405:00

of control at 50 hertz on the robot

## 6405:00 - 6445:00

Uh, and uh, we founded the company in

## 6445:00 - 6500:00

kind of mid-March of of 2024. Uh, and a

## 6500:00 - 6525:00

couple months later after we had set

## 6525:00 - 6555:00

everything up, we were able to get a

## 6555:00 - 6600:00

policy that could fairly reliably fold a

## 6600:00 - 6630:00

single size single brand shirt. Uh, you

## 6630:00 - 6655:00

can see that I'm testing the policy

## 6655:00 - 6705:00

right here. Uh, and we also wanted to

## 6705:00 - 6735:00

test some dynamic motions because you

## 6735:00 - 6750:00

need to be able to match the control

## 6750:00 - 6780:00

frequency accurately in order to do

## 6780:00 - 6810:00

these sorts of dynamic motions. Um and

## 6810:00 - 6835:00

so these were some of our very initial

## 6835:00 - 6875:00

tests at uh addressing this sort of

## 6875:00 - 6910:00

laundry folding problem. Then from there

## 6910:00 - 6925:00

we wanted to make the problem

## 6925:00 - 6970:00

incrementally harder. Uh and so we

## 6970:00 - 7000:00

instead of starting from the shirt flat

## 7000:00 - 7050:00

on the table, we started in a crumpled

## 7050:00 - 7100:00

position like these. And it turns out

## 7100:00 - 7130:00

that this actually makes it a lot

## 7130:00 - 7170:00

harder. Uh and so here are some videos

## 7170:00 - 7205:00

of some of our initial attempts at

## 7205:00 - 7250:00

trying to train the robot to fold these

## 7250:00 - 7305:00

shirts. And the robot struggles. uh the

## 7305:00 - 7330:00

the robot does some things that kind of

## 7330:00 - 7360:00

look somewhat sensible but generally

## 7360:00 - 7410:00

isn't able to make progress on the task.

## 7410:00 - 7445:00

Uh with many tests we frequently were

## 7445:00 - 7480:00

getting 0% success rate in our tests of

## 7480:00 - 7515:00

this uh system and really struggling to

## 7515:00 - 7560:00

make progress. So really here is the it

## 7560:00 - 7580:00

introduces this challenge of handling

## 7580:00 - 7610:00

the sorts of variability in the ways in

## 7610:00 - 7640:00

which shirts might be crumpled on the

## 7640:00 - 7675:00

table. We had some initial signs of life

## 7675:00 - 7725:00

in late June uh of of last year. Uh and

## 7725:00 - 7765:00

so in this case, the robot was able to

## 7765:00 - 7790:00

kind of make progress on flattening the

## 7790:00 - 7825:00

shirt. Uh it's also then able to fold

## 7825:00 - 7895:00

the shirt uh decently well uh from that

## 7895:00 - 7940:00

initial state. Still not perfect. Uh and

## 7940:00 - 7965:00

as you can see, it takes quite a while

## 7965:00 - 7990:00

to do this. So this is a video that was

## 7990:00 - 8025:00

sped up AEX. Uh so not something that

## 8025:00 - 8065:00

you might have the patience uh for a

## 8065:00 - 8095:00

robot to do.

## 8095:00 - 8135:00

Um, so with some initial signs of life,

## 8135:00 - 8165:00

the also very low success rate, we

## 8165:00 - 8190:00

started to transition to a slightly

## 8190:00 - 8210:00

harder version of the task where the

## 8210:00 - 8245:00

laundry starts in a laundry basket. We

## 8245:00 - 8280:00

also introduced variable size shirts and

## 8280:00 - 8355:00

shorts into the mix. Uh, and again, the

## 8355:00 - 8395:00

robot really struggled. So in many of

## 8395:00 - 8430:00

our tests, we were getting 0% success

## 8430:00 - 8460:00

rate across the board, and we're really

## 8460:00 - 8490:00

struggling to actually get the robots to

## 8490:00 - 8515:00

learn how to do these tasks. At this

## 8515:00 - 8540:00

point, we were trying to consider a lot

## 8540:00 - 8575:00

of different things. uh we thought that

## 8575:00 - 8605:00

maybe the robot needs memory, needs

## 8605:00 - 8640:00

history in some way. Uh maybe we need to

## 8640:00 - 8680:00

just train our models for longer. Maybe

## 8680:00 - 8710:00

we should be doing control and endeector

## 8710:00 - 8735:00

space rather than in joint space of the

## 8735:00 - 8775:00

robot. Uh maybe our encoders, we knew

## 8775:00 - 8795:00

that there were calibration issues and

## 8795:00 - 8820:00

maybe we need that calibration to be

## 8820:00 - 8845:00

more consistent. Uh maybe we need to

## 8845:00 - 8870:00

condition the model on more information

## 8870:00 - 8900:00

about the data. Uh maybe we need

## 8900:00 - 8925:00

hierarchy because this is a pretty long

## 8925:00 - 8950:00

horizon task and it needs to break it

## 8950:00 - 8985:00

down into different subtasks. Maybe we

## 8985:00 - 9020:00

need higher resolution images. uh maybe

## 9020:00 - 9035:00

we need to introduce kind of

## 9035:00 - 9070:00

interventions in data collection. A lot

## 9070:00 - 9095:00

of these things we also tried. We had

## 9095:00 - 9120:00

around two to three months of failure

## 9120:00 - 9150:00

where nothing was really working at

## 9150:00 - 9190:00

addressing this task. But then at some

## 9190:00 - 9220:00

point we actually had a bit of a

## 9220:00 - 9255:00

breakthrough uh which was that um we

## 9255:00 - 9290:00

found one thing that really seemed to

## 9290:00 - 9330:00

make a difference in the robot's ability

## 9330:00 - 9365:00

to do the task. And this was actually to

## 9365:00 - 9400:00

take some inspiration from the world of

## 9400:00 - 9430:00

language modeling to actually instead of

## 9430:00 - 9460:00

just training a policy on all of our

## 9460:00 - 9500:00

data, we pre-train on all the data and

## 9500:00 - 9550:00

then fine-tune on a highly on a curated

## 9550:00 - 9580:00

consistent highquality set of

## 9580:00 - 9625:00

demonstration data. When we did this,

## 9625:00 - 9650:00

uh, we found that the robot was actually

## 9650:00 - 9690:00

able to make progress and a lot more

## 9690:00 - 9730:00

reliably fold articles of clothing. Uh,

## 9730:00 - 9760:00

and so I think that this video was the

## 9760:00 - 9805:00

first video where the robot was able to

## 9805:00 - 9860:00

fold five items in a row and stack them.

## 9860:00 - 9890:00

Uh, I went home very excited this day.

## 9890:00 - 9930:00

Uh, this was in September of 2024, so

## 9930:00 - 9985:00

multiple months after our initial tests.

## 9985:00 - 10035:00

Uh, now this is far from perfect. Uh, it

## 10035:00 - 10070:00

takes 20 minutes to fold five items of

## 10070:00 - 10130:00

clothes. Uh and um at the same time

## 10130:00 - 10155:00

though it kind of suggested that this

## 10155:00 - 10205:00

sort of recipe was able to unlock uh the

## 10205:00 - 10235:00

capability in the robot to actually fold

## 10235:00 - 10275:00

these articles of clothing. So you can

## 10275:00 - 10300:00

see these sorts of failures here. In

## 10300:00 - 10330:00

this case, it attempted to fold the the

## 10330:00 - 10365:00

blue shirt around seven times uh before

## 10365:00 - 10395:00

eventually actually figuring out how to

## 10395:00 - 10420:00

do that. Um there's also other failure

## 10420:00 - 10450:00

modes as well. So, here's an example

## 10450:00 - 10485:00

where the robot pushes the stack to the

## 10485:00 - 10520:00

corner of the table uh and decides to

## 10520:00 - 10550:00

kind of fiddle with it a bit uh and then

## 10550:00 - 10595:00

eventually uh slides it off the table

## 10595:00 - 10620:00

and then it proceeds as if nothing had

## 10620:00 - 10640:00

happened and it's going to continue to

## 10640:00 - 10675:00

fold. We continue to iterate on this

## 10675:00 - 10725:00

recipe. We uh selected and worked on our

## 10725:00 - 10750:00

curation strategy for curating a higher

## 10750:00 - 10785:00

quality set of demonstration data. Uh we

## 10785:00 - 10815:00

got it from 20 minutes down to 12

## 10815:00 - 10845:00

minutes uh for these five items. This is

## 10845:00 - 10880:00

kind of how we were evaluating uh how

## 10880:00 - 10930:00

good our robot system was. uh it still

## 10930:00 - 10960:00

makes mistakes. It's still the full

## 10960:00 - 10995:00

quality still varies, but um it's still

## 10995:00 - 11030:00

significantly better than our previous

## 11030:00 - 11060:00

curation recipe. Now, at this point, we

## 11060:00 - 11100:00

were still training models largely um

## 11100:00 - 11125:00

kind of we were pre-training uh and

## 11125:00 - 11160:00

fine-tuning only on laundry data, and we

## 11160:00 - 11185:00

weren't leveraging uh kind of

## 11185:00 - 11220:00

pre-trained models in the community. And

## 11220:00 - 11245:00

there were some folks working at

## 11245:00 - 11265:00

physical intelligence that were working

## 11265:00 - 11290:00

on developing a pre-trained model

## 11290:00 - 11340:00

trained on all of the robot data. And um

## 11340:00 - 11370:00

we then started to try to introduce

## 11370:00 - 11430:00

these models into our um into our

## 11430:00 - 11470:00

recipe. And so we took an open- source

## 11470:00 - 11490:00

vision language model, a three billion

## 11490:00 - 11525:00

parameter model uh called Polygeemma.

## 11525:00 - 11550:00

Previously we're using the previous

## 11550:00 - 11575:00

videos were all with like a 100 to 300

## 11575:00 - 11600:00

million parameters that we're iterating

## 11600:00 - 11650:00

on. Um this model takes as input images

## 11650:00 - 11695:00

from the robot also a language command

## 11695:00 - 11755:00

uh and then has a head a diffusion head

## 11755:00 - 11775:00

that's going to attend to all the

## 11775:00 - 11800:00

internal values of the vision language

## 11800:00 - 11850:00

model. and uh with the joint angles uh

## 11850:00 - 11885:00

predict a chunk of 50 actions into the

## 11885:00 - 11930:00

future. So about 1 second uh of of

## 11930:00 - 11975:00

action steps and we're using a flow

## 11975:00 - 12015:00

matching a variant of diffusion uh to

## 12015:00 - 12050:00

actually output these actions and output

## 12050:00 - 12080:00

continuous actions. Um so we took this

## 12080:00 - 12125:00

pre-trained uh this model and instead of

## 12125:00 - 12155:00

pre-training only on laundry, we

## 12155:00 - 12180:00

pre-trained on all of the robot data

## 12180:00 - 12220:00

that we had collected. Uh and then we

## 12220:00 - 12245:00

just fine-tuned it with the same exact

## 12245:00 - 12275:00

post- training recipe that we had

## 12275:00 - 12310:00

developed uh without using the vision

## 12310:00 - 12335:00

language models. Uh and when we did

## 12335:00 - 12370:00

this, we actually saw the robot uh

## 12370:00 - 12400:00

continue to actually get better when we

## 12400:00 - 12430:00

just plugged in that new pre-trained

## 12430:00 - 12475:00

model. Uh and so in the left video, it's

## 12475:00 - 12505:00

able to do five items in 9 minutes,

## 12505:00 - 12535:00

which was faster than the 12 minutes we

## 12535:00 - 12560:00

had before. In the right videos, we were

## 12560:00 - 12590:00

testing with um some novel clothing

## 12590:00 - 12625:00

items and found that it was also quite

## 12625:00 - 12665:00

efficient at folding multiple items in a

## 12665:00 - 12700:00

row. Uh, and we also saw as a result

## 12700:00 - 12730:00

there was also more consistent bold

## 12730:00 - 12765:00

quality by using this model that was

## 12765:00 - 12810:00

about 10 times larger um, and had seen

## 12810:00 - 12855:00

more robot data as input. To look at a

## 12855:00 - 12890:00

few highlights of this, here's a pair of

## 12890:00 - 12915:00

shorts that the robot hasn't seen

## 12915:00 - 12950:00

before. And this is kind of a tricky

## 12950:00 - 12970:00

scenario where to flatten it, it

## 12970:00 - 13000:00

actually kind of needs to reach under

## 13000:00 - 13030:00

the kind of the bottom of the shorts.

## 13030:00 - 13055:00

And it's able to do that. is able to

## 13055:00 - 13085:00

kind of figure out that it should reach

## 13085:00 - 13125:00

under um the the left part of the shorts

## 13125:00 - 13190:00

in order to uh eventually flatten it. Uh

## 13190:00 - 13225:00

and then um once it actually

## 13225:00 - 13255:00

successfully flattens it, uh it's able

## 13255:00 - 13295:00

to fold it successfully. It also has to

## 13295:00 - 13330:00

do something similar at times to fold

## 13330:00 - 13350:00

shirts. So in this case, it needs to

## 13350:00 - 13380:00

actually kind of fold the shirt over on

## 13380:00 - 13405:00

itself with actually puts it in a more

## 13405:00 - 13435:00

crumpled state arguably, but allows it

## 13435:00 - 13465:00

to find the corners of the shirt and

## 13465:00 - 13515:00

then uh go ahead and fold it.

## 13515:00 - 13540:00

Uh, and then like I mentioned, it also

## 13540:00 - 13575:00

is able to handle unseen clothing items.

## 13575:00 - 13620:00

So, uh, here's an example of a shirt

## 13620:00 - 13665:00

with a V-neck, uh, that is able to fold

## 13665:00 - 13700:00

even though, um, like the the post

## 13700:00 - 13725:00

training data set didn't have, well,

## 13725:00 - 13750:00

didn't this shirt was completely held

## 13750:00 - 13770:00

out and the post training data set

## 13770:00 - 13805:00

didn't have any V-necks uh, as input in

## 13805:00 - 13830:00

the data set, it's also able to fold

## 13830:00 - 13860:00

shirts with buttons. So, it has some

## 13860:00 - 13885:00

degree of generalization to different

## 13885:00 - 13930:00

clothing items.

## 13930:00 - 13970:00

Um, and then lastly, because this policy

## 13970:00 - 14005:00

is a neural network and it's kind of uh

## 14005:00 - 14030:00

taking his input, the current image,

## 14030:00 - 14075:00

it's able to handle interruptions. So

## 14075:00 - 14110:00

here, Michael is uh continuing to mess

## 14110:00 - 14150:00

with the robot and the robot uh figures

## 14150:00 - 14175:00

out that it should put the the shirt

## 14175:00 - 14205:00

away uh while it's trying to fold the

## 14205:00 - 14235:00

other shirt. In this case, Michael's

## 14235:00 - 14255:00

going to continue messing with the

## 14255:00 - 14325:00

robot. So, Michael unfolds one side

## 14325:00 - 14380:00

and the robot reacts.

## 14380:00 - 14450:00

Michael goes in again

## 14450:00 - 14490:00

and the robot makes some mistakes here

## 14490:00 - 14535:00

but able to recover. Michael messes it

## 14535:00 - 14575:00

up again. So those are some results of

## 14575:00 - 14615:00

of what the robot's able to do. Now I

## 14615:00 - 14635:00

talked about this pre-training and

## 14635:00 - 14660:00

post-training recipe being really

## 14660:00 - 14680:00

important. We can actually

## 14680:00 - 14725:00

quantitatively measure that and actually

## 14725:00 - 14750:00

make sure that this is actually what's

## 14750:00 - 14775:00

leading to improvement. So, we compared

## 14775:00 - 14800:00

this pre-training and post-training

## 14800:00 - 14840:00

recipe to not using any pre-training and

## 14840:00 - 14875:00

only training on the curated data set

## 14875:00 - 14915:00

versus no post-training where you're

## 14915:00 - 14945:00

training on all of the data rather than

## 14945:00 - 14990:00

fine-tuning on the curated data set. Uh,

## 14990:00 - 15015:00

and we evaluated these models in terms

## 15015:00 - 15050:00

of their progress on the task where you

## 15050:00 - 15075:00

u make partial progress for getting it

## 15075:00 - 15095:00

out of the bin, which is the easiest

## 15095:00 - 15125:00

part, and then further progress for

## 15125:00 - 15150:00

flattening, folding, and stacking the

## 15150:00 - 15190:00

items. And we see that the pre-training

## 15190:00 - 15225:00

and post-training recipe is able to get

## 15225:00 - 15275:00

far higher performance than omitting

## 15275:00 - 15305:00

pre-training and omitting post-training.

## 15305:00 - 15340:00

Uh and notably omitting pre-training and

## 15340:00 - 15370:00

post- training is basically able to get

## 15370:00 - 15400:00

it out of the bin and make very little

## 15400:00 - 15430:00

progress after that. Whereas when we

## 15430:00 - 15460:00

combine pre-training and curated

## 15460:00 - 15485:00

post-raining, we get far higher

## 15485:00 - 15525:00

performance whereas able to reliably uh

## 15525:00 - 15565:00

flatten and fold objects. Um and then

## 15565:00 - 15590:00

the last thing that I'll mention on this

## 15590:00 - 15625:00

note is that uh nothing in this recipe

## 15625:00 - 15660:00

is specific to laundry. And so we took

## 15660:00 - 15710:00

the same recipe um and fine-tuned on

## 15710:00 - 15760:00

other tasks. So here uh the task is to

## 15760:00 - 15800:00

um kind of clean up a table. And the

## 15800:00 - 15845:00

robot's also able to successfully uh do

## 15845:00 - 15880:00

this task uh despite the fact that we

## 15880:00 - 15905:00

primarily were iterating a lot on

## 15905:00 - 15935:00

laundry, but it's able to also apply

## 15935:00 - 15975:00

this recipe to this task. It also um is

## 15975:00 - 16020:00

able to scoop uh coffee beans into a

## 16020:00 - 16065:00

coffee grinder. Uh this task is pretty

## 16065:00 - 16100:00

hard. it has to construct the bottom

## 16100:00 - 16135:00

part of a cardboard box uh which

## 16135:00 - 16200:00

requires uh quite a bit of dexterity and

## 16200:00 - 16250:00

then um lastly autonomously lighting a

## 16250:00 - 16290:00

candle with a match again with this kind

## 16290:00 - 16330:00

of same pre-training and post-training

## 16330:00 - 16370:00

recipe.

## 16370:00 - 16415:00

And so this is pointing at this kind of

## 16415:00 - 16445:00

the benefit of foundation models that I

## 16445:00 - 16475:00

alluded to before which is that to do

## 16475:00 - 16500:00

these different tasks you don't have to

## 16500:00 - 16530:00

start completely from scratch. you can

## 16530:00 - 16565:00

actually leverage pre-training across

## 16565:00 - 16595:00

multiple robots and across multiple

## 16595:00 - 16650:00

tasks. And then we're also able to apply

## 16650:00 - 16690:00

that same recipe to robots at other

## 16690:00 - 16715:00

companies. Uh this is a robot that I've

## 16715:00 - 16750:00

actually never seen in person before. Uh

## 16750:00 - 16785:00

they collected data. They sent the data

## 16785:00 - 16825:00

to us. We fine-tuned our model on their

## 16825:00 - 16855:00

data. We actually didn't even know

## 16855:00 - 16885:00

exactly how the model is being

## 16885:00 - 16910:00

controlled. Uh exactly the

## 16910:00 - 16955:00

representation of their actions. uh but

## 16955:00 - 16990:00

by fine-tuning the model on this new

## 16990:00 - 17030:00

robot, the model is able to control the

## 17030:00 - 17070:00

robot in order to uh make a cup of

## 17070:00 - 17120:00

coffee in this case. So um some

## 17120:00 - 17150:00

takeaways for this part uh we were able

## 17150:00 - 17175:00

to independently develop post- training

## 17175:00 - 17195:00

and pre-training and decouple the

## 17195:00 - 17230:00

problem um and then eventually get the

## 17230:00 - 17260:00

best of both. Uh we found that training

## 17260:00 - 17300:00

on all the data doesn't work for complex

## 17300:00 - 17330:00

tasks and this sort of pre post post

## 17330:00 - 17355:00

pre-training and post-training on

## 17355:00 - 17385:00

curated data leads to far better

## 17385:00 - 17425:00

performance. And then we broke up this

## 17425:00 - 17455:00

really hard problem of folding laundry

## 17455:00 - 17485:00

by gradually starting with folding

## 17485:00 - 17525:00

single shirts and going to more and more

## 17525:00 - 17570:00

complex versions of the task. Now

## 17570:00 - 17595:00

there's a number of limitations here and

## 17595:00 - 17620:00

one limitation I'd like to point out is

## 17620:00 - 17665:00

that these robots inevitably um in this

## 17665:00 - 17705:00

case were trained in the environments

## 17705:00 - 17740:00

that they were tested. Uh and so this

## 17740:00 - 17770:00

means that in principle you could use

## 17770:00 - 17790:00

these methods to collect a lot of data

## 17790:00 - 17820:00

in one environment and then deploy them

## 17820:00 - 17850:00

in one environment. But ultimately,

## 17850:00 - 17870:00

there's going to be things that change

## 17870:00 - 17910:00

about an environment and scenarios where

## 17910:00 - 17935:00

we would want to actually apply these

## 17935:00 - 17960:00

robots to environments that they've

## 17960:00 - 18000:00

never seen in before. And so, how can

## 18000:00 - 18025:00

robots actually succeed in places that

## 18025:00 - 18050:00

they've never been? The lesson we've

## 18050:00 - 18090:00

learned from machine learning in other

## 18090:00 - 18120:00

places is that we should collect diverse

## 18120:00 - 18160:00

data. Uh, and so we started by

## 18160:00 - 18195:00

collecting data of tidying bedrooms and

## 18195:00 - 18245:00

kitchens in many different environments.

## 18245:00 - 18275:00

Uh, and here's an example, kind of a

## 18275:00 - 18335:00

sample of that data. uh and we collected

## 18335:00 - 18370:00

robot data in homes across San Francisco

## 18370:00 - 18425:00

here uh and also collected data in

## 18425:00 - 18465:00

diverse mock kitchens and mock bedrooms

## 18465:00 - 18500:00

and in total we had more than 100 unique

## 18500:00 - 18535:00

rooms represented in the data set that

## 18535:00 - 18570:00

ended up being uh a part of a bigger

## 18570:00 - 18605:00

pre-training mixture. So we trained on

## 18605:00 - 18640:00

this diverse mobile manipulation data uh

## 18640:00 - 18660:00

including the low-level action

## 18660:00 - 18695:00

prediction as well as predicting highle

## 18695:00 - 18730:00

subtask commands for how to complete the

## 18730:00 - 18770:00

task. But we also trained on previously

## 18770:00 - 18800:00

collected static manipulation data that

## 18800:00 - 18840:00

was also fairly diverse. Um static

## 18840:00 - 18865:00

manipulation data that we had collected

## 18865:00 - 18910:00

in our office and in labs as well as web

## 18910:00 - 18960:00

data um and highle instructional data.

## 18960:00 - 18990:00

And I should point out here that the

## 18990:00 - 19025:00

mobile manipulation data of tidying

## 19025:00 - 19060:00

bedrooms and kitchens only accounted for

## 19060:00 - 19115:00

2.4% of the overall pre-training mix.

## 19115:00 - 19150:00

And so the lesson here is that you were

## 19150:00 - 19185:00

basically able to spin up a new task and

## 19185:00 - 19210:00

actually an entirely new robot. the rest

## 19210:00 - 19230:00

of the mixture didn't have any mobile

## 19230:00 - 19265:00

manipulation data with this particular

## 19265:00 - 19305:00

mobile manipulator in it um without

## 19305:00 - 19335:00

redoing all of the data collection.

## 19335:00 - 19365:00

We're able to build upon everything that

## 19365:00 - 19390:00

had been done before. And it's kind of

## 19390:00 - 19435:00

this kind of same story of foundation

## 19435:00 - 19470:00

models being able to make it easier to

## 19470:00 - 19510:00

spin up um a new problem, a new

## 19510:00 - 19540:00

application without starting from

## 19540:00 - 19585:00

scratch. Um now this wasn't completely

## 19585:00 - 19625:00

easy. Um we had a couple challenges. One

## 19625:00 - 19650:00

of the challenges that we ran into is

## 19650:00 - 19700:00

that naively uh this model can ignore

## 19700:00 - 19740:00

language instructions. So we had

## 19740:00 - 19760:00

actually in this case asked it to pick

## 19760:00 - 19785:00

up the cutting board and it chose to

## 19785:00 - 19815:00

pick up the plate instead. Now we're

## 19815:00 - 19845:00

again asking it to pick up the cutting

## 19845:00 - 19890:00

board. Uh and instead the robot had a

## 19890:00 - 19915:00

mind of its own decided to pick up the

## 19915:00 - 19945:00

plate. Uh and then we tell it to put the

## 19945:00 - 19975:00

plate in the sink. And eventually it

## 19975:00 - 20010:00

decides that well after kind of moving

## 20010:00 - 20030:00

away from the cutting board it

## 20030:00 - 20050:00

eventually decided that it would

## 20050:00 - 20085:00

actually pick up the cutting board. And

## 20085:00 - 20105:00

so in the early development of our

## 20105:00 - 20140:00

model, we found that it often ignored

## 20140:00 - 20180:00

language.

## 20180:00 - 20220:00

And to solve this, we thought about how

## 20220:00 - 20245:00

vision language models actually follow

## 20245:00 - 20265:00

language well. And so maybe there's a

## 20265:00 - 20305:00

way to preserve the inherent abilities

## 20305:00 - 20330:00

of the pre-trained models when

## 20330:00 - 20385:00

addressing this task. Uh and so what we

## 20385:00 - 20425:00

did is with this PI zero architecture,

## 20425:00 - 20465:00

this action head that's using diffusion

## 20465:00 - 20515:00

is randomly initialized. And this ends

## 20515:00 - 20550:00

up actually deteriorating the

## 20550:00 - 20585:00

pre-trained knowledge that's present in

## 20585:00 - 20620:00

the vision language model. Uh and we

## 20620:00 - 20665:00

found that if we can prevent this

## 20665:00 - 20690:00

deterioration, we might be able to get

## 20690:00 - 20735:00

better language following. Uh and so the

## 20735:00 - 20770:00

recipe that we came up with was actually

## 20770:00 - 20810:00

in some ways fairly similar, but instead

## 20810:00 - 20835:00

we're going to be predicting tokenized

## 20835:00 - 20865:00

actions. And then when we have the

## 20865:00 - 20885:00

diffusion head, we'll be stopping the

## 20885:00 - 20910:00

gradient from the randomly initialized

## 20910:00 - 20940:00

diffusion head to prevent it from

## 20940:00 - 20975:00

deteriorating the language following

## 20975:00 - 21025:00

abilities of the VLM backbone. Uh and we

## 21025:00 - 21055:00

found that this first led to faster

## 21055:00 - 21080:00

training because the tokenized actions

## 21080:00 - 21125:00

are a more direct supervision signal.

## 21125:00 - 21160:00

And second, it also followed language

## 21160:00 - 21205:00

far better. Uh an 80% follow rate rather

## 21205:00 - 21240:00

than a 20% follower rate. Uh which

## 21240:00 - 21270:00

suggests that we're able to preserve the

## 21270:00 - 21305:00

the kind of pre-training in the vision

## 21305:00 - 21335:00

language model backbone. So, we put

## 21335:00 - 21360:00

those pieces together. We took that

## 21360:00 - 21390:00

recipe and trained it um pre-trained it

## 21390:00 - 21410:00

on all of our data, including the mobile

## 21410:00 - 21450:00

manipulation data. We fine-tuned it on

## 21450:00 - 21480:00

mobile manipulation data in a variety of

## 21480:00 - 21510:00

environments. And then we tested the

## 21510:00 - 21550:00

model in places it's never been in

## 21550:00 - 21590:00

before. So, we rented uh three Airbnbs

## 21590:00 - 21635:00

that uh we had never been to before. Uh

## 21635:00 - 21685:00

we put the robot in those homes, in this

## 21685:00 - 21725:00

case, in the kitchen, and I asked it to

## 21725:00 - 21755:00

close the cabinet. I asked it to put

## 21755:00 - 21775:00

away the dishes. has also never seen

## 21775:00 - 21815:00

these dishes um or the these forks,

## 21815:00 - 21860:00

these objects. And the robot's able to

## 21860:00 - 21890:00

succeed even though it's never been the

## 21890:00 - 21915:00

here before. There's different uh

## 21915:00 - 21945:00

countertops, different furniture,

## 21945:00 - 21975:00

different objects, and so forth. Uh

## 21975:00 - 22000:00

lastly, I asked it to clean up the

## 22000:00 - 22065:00

spill, and the robot is able to oblige

## 22065:00 - 22095:00

and wipe down the spill and eventually

## 22095:00 - 22270:00

put the sponge into the sink.

## 22270:00 - 22295:00

Uh it's also able to do this for

## 22295:00 - 22325:00

bedrooms. So Laura asked it in this case

## 22325:00 - 22370:00

just clean the bedroom and it puts uh

## 22370:00 - 22410:00

articles of clothing in. Uh it throws

## 22410:00 - 22465:00

away the trash and uh then is able to

## 22465:00 - 22510:00

tidy the bed by putting the uh putting

## 22510:00 - 22565:00

the pillow at the top of the bed and uh

## 22565:00 - 22595:00

tidying the the blanket or the comforter

## 22595:00 - 22685:00

of the bed.

## 22685:00 - 22720:00

YC's next batch is now taking

## 22720:00 - 22760:00

applications. Got a startup in you?

## 22760:00 - 22810:00

Apply at y combinator.com/apply.

## 22810:00 - 22850:00

It's never too early and filling out the

## 22850:00 - 22895:00

app will level up your idea. Okay, back

## 22895:00 - 22940:00

to the video. So, quantitatively, I

## 22940:00 - 22960:00

talked about how the kind of there's

## 22960:00 - 23000:00

only 2.7% or something of the the

## 23000:00 - 23030:00

mixture and so how much does that other

## 23030:00 - 23060:00

data actually help? Uh could we actually

## 23060:00 - 23105:00

just train on that kind of 2.7%.

## 23105:00 - 23140:00

And we find that these kind of bars on

## 23140:00 - 23170:00

the right which are excluding data from

## 23170:00 - 23205:00

static robots in labs and environments

## 23205:00 - 23245:00

and so forth um reduces performance

## 23245:00 - 23265:00

significantly. So the performance goes

## 23265:00 - 23305:00

down to less than 60% when you exclude

## 23305:00 - 23345:00

that data when evaluated in novel homes

## 23345:00 - 23375:00

compared to if you use the full

## 23375:00 - 23420:00

pre-training mixture it has uh more than

## 23420:00 - 23465:00

20% higher performance. Lastly we also

## 23465:00 - 23495:00

looked at is the diversity of data

## 23495:00 - 23525:00

helpful? Is it important? And so we

## 23525:00 - 23565:00

increase the amount of data from these

## 23565:00 - 23600:00

environments to test this. It's always

## 23600:00 - 23635:00

good to like you can kind of do vibe

## 23635:00 - 23670:00

eval but it's really helpful to actually

## 23670:00 - 23710:00

measure how well uh these things work

## 23710:00 - 23745:00

and so this is what this is measuring

## 23745:00 - 23775:00

and we find that if we actually increase

## 23775:00 - 23820:00

the amount of homes the amount of uh

## 23820:00 - 23845:00

locations that are represented in the

## 23845:00 - 23875:00

data the performance increases which is

## 23875:00 - 23910:00

great uh and it actually gets to the

## 23910:00 - 23960:00

same level of performance as if we train

## 23960:00 - 24015:00

on data from that target environment and

## 24015:00 - 24045:00

so it means we're actually mostly

## 24045:00 - 24090:00

closing the generalization gap and

## 24090:00 - 24115:00

suggest that the bottlenecks at this

## 24115:00 - 24155:00

point for this sort of task lie not in

## 24155:00 - 24185:00

collecting more diverse data but in

## 24185:00 - 24215:00

actually getting higher reliability and

## 24215:00 - 24250:00

higher performance. Um now I should also

## 24250:00 - 24275:00

mention that there's failure modes like

## 24275:00 - 24310:00

this the success rate was around 80%.

## 24310:00 - 24340:00

There's lots of room for improvement. Uh

## 24340:00 - 24360:00

here are a couple examples of those

## 24360:00 - 24395:00

failure modes. So um here it's told to

## 24395:00 - 24430:00

put the items in the drawer. Uh it is

## 24430:00 - 24460:00

able to put it in the drawer but the

## 24460:00 - 24490:00

item isn't fully in the drawer at the

## 24490:00 - 24510:00

end and it decides that it's done and

## 24510:00 - 24550:00

kind of moves on to the next thing. Uh

## 24550:00 - 24575:00

here the robot uh needs to put the

## 24575:00 - 24605:00

clothes in the laundry basket. It drives

## 24605:00 - 24645:00

over the shirt um and then it gets stuck

## 24645:00 - 24695:00

and it's not able to lift it up. Uh here

## 24695:00 - 24720:00

we asked it to put the dishes in the

## 24720:00 - 24780:00

sink and it successfully is able to put

## 24780:00 - 24805:00

a number of the dishes in the sink but

## 24805:00 - 24825:00

it struggles to pick up the cutting

## 24825:00 - 24855:00

board uh in this particular case because

## 24855:00 - 24890:00

it's a very thin and it's flush against

## 24890:00 - 24950:00

the surface of uh the countertop. Uh and

## 24950:00 - 24975:00

in the last case, my probably my

## 24975:00 - 25000:00

favorite case, um it's told to put the

## 25000:00 - 25045:00

spatula into a drawer and it decides

## 25045:00 - 25085:00

that the oven looks a lot like a drawer

## 25085:00 - 25140:00

and so it opens the oven um and uh yeah,

## 25140:00 - 25185:00

tries to to put it in there. Um and

## 25185:00 - 25205:00

beyond this, there's also challenges

## 25205:00 - 25220:00

with regard to speed, partial

## 25220:00 - 25265:00

observability, uh long-term planning um

## 25265:00 - 25305:00

and so uh yeah, lots of work to do

## 25305:00 - 25350:00

still. So the takeaway here is that with

## 25350:00 - 25385:00

diverse data, uh, robots can follow a

## 25385:00 - 25415:00

variety of instructions in environments

## 25415:00 - 25450:00

that the robot has never been in before.

## 25450:00 - 25485:00

Uh, which is a big step up from a lot of

## 25485:00 - 25520:00

robotic scenarios where they're trained

## 25520:00 - 25550:00

in the scenarios that they are being

## 25550:00 - 25600:00

tested. Now the last kind of bit I'd

## 25600:00 - 25660:00

like to talk about is this model has a

## 25660:00 - 25695:00

fairly limited instruction set. It can

## 25695:00 - 25720:00

only follow kind of a certain set of

## 25720:00 - 25765:00

commands. And if we think about how

## 25765:00 - 25800:00

other forms of AI technology have been

## 25800:00 - 25830:00

deployed, people really like to

## 25830:00 - 25855:00

customize and actually tell the robot

## 25855:00 - 25875:00

what they want or tell the system what

## 25875:00 - 25920:00

they want from these kinds of models.

## 25920:00 - 25945:00

And so just like we prompt language

## 25945:00 - 25980:00

models, can we allow robots to respond

## 25980:00 - 26010:00

to open-ended prompts and open-ended

## 26010:00 - 26045:00

interjections?

## 26045:00 - 26080:00

Uh so to do this and actually to do the

## 26080:00 - 26110:00

past work, we're actually leveraging

## 26110:00 - 26145:00

hierarchical uh vision language action

## 26145:00 - 26165:00

models. So we're going to have a high

## 26165:00 - 26225:00

level policy break down uh the prompt

## 26225:00 - 26285:00

into uh intermediate uh verbal responses

## 26285:00 - 26320:00

and intermediate atomic language

## 26320:00 - 26370:00

commands. So the highle prompt might be

## 26370:00 - 26400:00

kind of can you make me a sandwich uh

## 26400:00 - 26440:00

and this highle policy will break it

## 26440:00 - 26490:00

down into the subtask of pick up one

## 26490:00 - 26525:00

slice of bread. This will be passed to a

## 26525:00 - 26555:00

low-level model that actually executes

## 26555:00 - 26610:00

and predicts target joint angles um to

## 26610:00 - 26640:00

fulfill the low-level command of picking

## 26640:00 - 26675:00

up one slice of bread. Now, on its own,

## 26675:00 - 26700:00

this isn't going to be able to follow

## 26700:00 - 26760:00

all sorts of prompts, and it's actually

## 26760:00 - 26785:00

fairly tricky to handle open-ended

## 26785:00 - 26825:00

language because it's going to be

## 26825:00 - 26855:00

challenging to collect a large number of

## 26855:00 - 26895:00

human robot interactions with the real

## 26895:00 - 26935:00

robot in the loop. And this is also

## 26935:00 - 26975:00

going to be fairly hard to scale. Uh and

## 26975:00 - 27005:00

so what we did is we kind of took all of

## 27005:00 - 27050:00

our existing robot data and we can

## 27050:00 - 27085:00

actually generate synthetic data for the

## 27085:00 - 27120:00

existing robot data. In particular, we

## 27120:00 - 27160:00

can use language models to reabel and

## 27160:00 - 27205:00

generate hypothetical human prompts for

## 27205:00 - 27240:00

the scenarios that the robots are in.

## 27240:00 - 27260:00

And so what this looks like is we'll

## 27260:00 - 27305:00

take data that says um here's a kind of

## 27305:00 - 27330:00

a video and then the next skill is to

## 27330:00 - 27350:00

pick up a Kit Kat because that's what

## 27350:00 - 27375:00

the robot does next in terms of just

## 27375:00 - 27420:00

like basic low-level annotation. And

## 27420:00 - 27445:00

then for this scenario where the robot

## 27445:00 - 27475:00

is about to pick up the KitKat, we can

## 27475:00 - 27510:00

ask a vision language model, what is a

## 27510:00 - 27545:00

hypothetical prompt that a human might

## 27545:00 - 27590:00

have asked that led to this um this

## 27590:00 - 27620:00

particular scenario and the robot to

## 27620:00 - 27655:00

actually choose to pick up a Kit Kat.

## 27655:00 - 27675:00

And then we can train our high level

## 27675:00 - 27710:00

policy on these synthetic prompts to

## 27710:00 - 27745:00

basically augment the robot data with

## 27745:00 - 27775:00

various human interactions that might

## 27775:00 - 27810:00

have led to those different situations.

## 27810:00 - 27840:00

And as a result of this, we're able to

## 27840:00 - 27870:00

actually allow robots to follow a

## 27870:00 - 27895:00

variety of different prompts. So on the

## 27895:00 - 27925:00

left, we ask, "Hi, robot. Can you make

## 27925:00 - 27965:00

me a ham and cheese sandwich?"

## 27965:00 - 27995:00

The robot says, "Sure, I'll start with

## 27995:00 - 28025:00

the bread and add ham and cheese next."

## 28025:00 - 28050:00

And it's able to break down this task

## 28050:00 - 28090:00

into the various subtasks of picking up

## 28090:00 - 28120:00

a slice of bread, putting on the cutting

## 28120:00 - 28145:00

board, picking up a slice of cheese,

## 28145:00 - 28185:00

putting it on the bread, um picking up

## 28185:00 - 28245:00

some ham, um and so on and so forth. I

## 28245:00 - 28270:00

can also follow more complicated prompts

## 28270:00 - 28295:00

like, "Hi robot, can you make me a vegan

## 28295:00 - 28330:00

sandwich? I don't like pickles, though."

## 28330:00 - 28365:00

uh and in this case is able to break it

## 28365:00 - 28395:00

down and decide that it's going to add

## 28395:00 - 28435:00

lettuce and tomatoes to the sandwich uh

## 28435:00 - 28470:00

and not add pickles, not add cheese, not

## 28470:00 - 28525:00

add um meat as well.

## 28525:00 - 28555:00

In addition to prompts, we're also able

## 28555:00 - 28590:00

to train the robot to handle different

## 28590:00 - 28635:00

interjections. Um actually here's an a

## 28635:00 - 28650:00

case where of a different kind of

## 28650:00 - 28680:00

prompt. So on the left we train the

## 28680:00 - 28720:00

robot to clean tables. So put trash away

## 28720:00 - 28755:00

and put dishes into the bin. And on the

## 28755:00 - 28790:00

right we ask the robot clean up only the

## 28790:00 - 28820:00

trash but not the dishes. And the

## 28820:00 - 28840:00

robot's able to understand what that

## 28840:00 - 28885:00

means and connect that to its low-level

## 28885:00 - 28925:00

actions and only put away the trash and

## 28925:00 - 28965:00

complete when it um when the trash is

## 28965:00 - 28990:00

all put away. And then lastly, it's able

## 28990:00 - 29020:00

to handle interjections and situated

## 29020:00 - 29065:00

corrections. So in this case, um the

## 29065:00 - 29105:00

robot is uh kind of getting items for a

## 29105:00 - 29135:00

user. The user interjects and said, "Get

## 29135:00 - 29155:00

me something sweet that's not in the

## 29155:00 - 29185:00

basket." Right after it had put a Kit

## 29185:00 - 29230:00

Kat into the basket and the robot um

## 29230:00 - 29260:00

says, "Uh, sure. Let me get you some

## 29260:00 - 29295:00

Skittles." uh and reasons through kind

## 29295:00 - 29335:00

of basic reasoning of how to uh what how

## 29335:00 - 29365:00

to fulfill the user's request and is

## 29365:00 - 29400:00

able to um respond to those kinds of

## 29400:00 - 29450:00

corrections situated in the world that

## 29450:00 - 29480:00

the robot is in. Now you might also

## 29480:00 - 29505:00

wonder like maybe some existing

## 29505:00 - 29530:00

foundation models could serve as a

## 29530:00 - 29560:00

highle planner for robots and do this

## 29560:00 - 29590:00

sort of high level reasoning without

## 29590:00 - 29615:00

actually training a separate model. And

## 29615:00 - 29655:00

so we also evaluated that um and we

## 29655:00 - 29690:00

found that in blue the performance at

## 29690:00 - 29715:00

following instructions and making

## 29715:00 - 29760:00

progress on the task was substantially

## 29760:00 - 29790:00

lower than the performance of our system

## 29790:00 - 29825:00

which is shown in green. Uh and in

## 29825:00 - 29850:00

general we found that these frontier

## 29850:00 - 29885:00

models generally struggle with visual

## 29885:00 - 29925:00

understanding as it pertains to robotics

## 29925:00 - 29950:00

which makes sense because in general

## 29950:00 - 29980:00

these models aren't kind of really

## 29980:00 - 30015:00

targeting uh many physical applications

## 30015:00 - 30040:00

and have very little data in the

## 30040:00 - 30090:00

physical world. Okay. Um, so to start to

## 30090:00 - 30115:00

wrap up, um, and then we'll all have

## 30115:00 - 30150:00

some time for questions. Uh, I talked a

## 30150:00 - 30180:00

bit about how robots can do a variety of

## 30180:00 - 30210:00

dextrous long horizon tasks with

## 30210:00 - 30235:00

pre-training and post- training. How

## 30235:00 - 30260:00

robots can succeed in places that

## 30260:00 - 30290:00

they've never been, and how they can

## 30290:00 - 30330:00

respond to open-ended prompts and

## 30330:00 - 30360:00

interjections by leveraging synthetic

## 30360:00 - 30405:00

data from language models on top of the

## 30405:00 - 30440:00

robot data that we had collected. Um now

## 30440:00 - 30475:00

with some closing notes the we've seen a

## 30475:00 - 30500:00

few different scenarios in this talk

## 30500:00 - 30550:00

where general purpose robots might be

## 30550:00 - 30595:00

more successful than specialist robots

## 30595:00 - 30630:00

but because we can essentially rather

## 30630:00 - 30655:00

than start from scratch for every single

## 30655:00 - 30695:00

application actually build upon a much

## 30695:00 - 30735:00

broader foundation for physical

## 30735:00 - 30780:00

intelligence in the real world. Um we

## 30780:00 - 30815:00

also saw that like large scale data in

## 30815:00 - 30845:00

the real world is really helpful for

## 30845:00 - 30870:00

developing these things and we found

## 30870:00 - 30905:00

that uh and I think that it's necessary

## 30905:00 - 30925:00

but not sufficient for physical

## 30925:00 - 30960:00

intelligence and there's a lot of uh

## 30960:00 - 30995:00

challenges and we need more research uh

## 30995:00 - 31045:00

to be done uh ourselves and through open

## 31045:00 - 31075:00

source contributions before robots I

## 31075:00 - 31115:00

think will be truly ready to tackle the

## 31115:00 - 31140:00

open world. I'd also like to mention

## 31140:00 - 31160:00

that at physical intelligence we're

## 31160:00 - 31195:00

hiring a number of roles. Uh if you're

## 31195:00 - 31215:00

excited about some of the things that we

## 31215:00 - 31235:00

talked about, you can see a list of the

## 31235:00 - 31295:00

open roles on the pi pi. As well,

## 31295:00 - 31455:00

awesome.

## 31455:00 - 31480:00

Happy to take some questions. Let's

## 31480:00 - 31495:00

start on the left.

## 31495:00 - 31535:00

>> Uh hi Chelsea. So, uh first I want to

## 31535:00 - 31565:00

say thank you for all your work on robot

## 31565:00 - 31600:00

learning. They're all really impressive.

## 31600:00 - 31640:00

Yeah. And uh so mainly I have two

## 31640:00 - 31690:00

questions on uh especially uh regarding

## 31690:00 - 31725:00

the post- training part you mentioned.

## 31725:00 - 31765:00

So um the first thing is uh you

## 31765:00 - 31805:00

mentioned that the in post training the

## 31805:00 - 31835:00

most important part is to have high

## 31835:00 - 31870:00

quality action data. So I'm wondering

## 31870:00 - 31910:00

what the components of that would be and

## 31910:00 - 31950:00

then the second question is what do you

## 31950:00 - 31985:00

think uh RL will play into the part of

## 31985:00 - 32005:00

post training?

## 32005:00 - 32065:00

>> Yeah absolutely. So I think that the the

## 32065:00 - 32090:00

different components of it a lot of it

## 32090:00 - 32115:00

comes down to consistency of the data

## 32115:00 - 32160:00

and the strategy being followed uh and

## 32160:00 - 32200:00

whether the robots whether the um the

## 32200:00 - 32240:00

data completes the task efficiently and

## 32240:00 - 32275:00

with a reliable strategy. Uh and then on

## 32275:00 - 32295:00

the second question I think that

## 32295:00 - 32330:00

reinforcement learning can play a very

## 32330:00 - 32385:00

large role in um it actually in post

## 32385:00 - 32415:00

training. I think that online data from

## 32415:00 - 32445:00

the robots uh which reinforcement

## 32445:00 - 32475:00

learning allows you to use can allow

## 32475:00 - 32510:00

robots to have a much higher success

## 32510:00 - 32555:00

rate and also uh be faster than if

## 32555:00 - 32575:00

they're just trained with imitation

## 32575:00 - 32580:00

learning.

## 32580:00 - 32620:00

>> Yeah, thank you.

## 32620:00 - 32665:00

>> Hi, thank you so much for your talk. Uh

## 32665:00 - 32710:00

so your work is really fascinating and

## 32710:00 - 32745:00

there is no doubt that it will have a

## 32745:00 - 32795:00

lot of impact in the future. But um can

## 32795:00 - 32845:00

I ask you at this stage uh how can you

## 32845:00 - 32890:00

find the fundings because honestly I

## 32890:00 - 32935:00

can't imagine how hard it can be to

## 32935:00 - 32970:00

convince people to invest in a robot

## 32970:00 - 32995:00

that folds close and deal with the

## 32995:00 - 33055:00

dishes. Yeah. So um it's a good

## 33055:00 - 33100:00

question. I think that well I guess

## 33100:00 - 33125:00

first I'll mention that we aren't just

## 33125:00 - 33165:00

focused on applications in the home. uh

## 33165:00 - 33190:00

we really want to solve this broader

## 33190:00 - 33225:00

problem of physical intelligence and

## 33225:00 - 33245:00

we've been starting with those

## 33245:00 - 33290:00

applications because they're ones that

## 33290:00 - 33320:00

are kind of easy to make progress on. Um

## 33320:00 - 33340:00

but we've also been doing tasks like

## 33340:00 - 33370:00

inserting an Ethernet cable which I put

## 33370:00 - 33400:00

put in the talk as well as constructing

## 33400:00 - 33445:00

a cardboard box. Uh and generally I

## 33445:00 - 33465:00

think that this sort of problem has a

## 33465:00 - 33500:00

ton of potential for for like making

## 33500:00 - 33540:00

impact in all sorts of realms not just

## 33540:00 - 33570:00

in domestic tasks but all sorts of

## 33570:00 - 33595:00

realms as well. And even in domestic

## 33595:00 - 33635:00

task, I think there's a huge market for

## 33635:00 - 33680:00

um for this kind of technology. Uh we

## 33680:00 - 33725:00

ourselves haven't had um a lot of

## 33725:00 - 33745:00

challenge with fundraising and I think

## 33745:00 - 33770:00

that a lot of robotics companies

## 33770:00 - 33805:00

recently have also done a great job um

## 33805:00 - 33830:00

and found that there's actually a lot of

## 33830:00 - 33850:00

excitement around this sort of

## 33850:00 - 33885:00

technology because I think things are

## 33885:00 - 33915:00

actually starting to work. Uh I started

## 33915:00 - 33945:00

working on this technology uh more than

## 33945:00 - 33975:00

10 years ago at this point and things

## 33975:00 - 34010:00

really weren't working then and so uh

## 34010:00 - 34030:00

yeah I think that there's a lot of

## 34030:00 - 34055:00

excitement that is starting to mature

## 34055:00 - 34100:00

and and um like actually be ready for

## 34100:00 - 34125:00

the real world. I think that there's a

## 34125:00 - 34170:00

lot more work to do uh but generally it

## 34170:00 - 34190:00

seems like there's a lot of people

## 34190:00 - 34220:00

excited about this technology and and

## 34220:00 - 34245:00

eager to actually put funds behind it.

## 34245:00 - 34275:00

>> Okay, thank you so much.

## 34275:00 - 34285:00

>> Yeah.

## 34285:00 - 34335:00

>> Hi. Uh thank you so much. Um I have two

## 34335:00 - 34385:00

questions like one uh uh more broad and

## 34385:00 - 34420:00

one more technical. So the technical one

## 34420:00 - 34480:00

like is uh VAS uh in my opinion like at

## 34480:00 - 34525:00

least to my understanding are a

## 34525:00 - 34560:00

framework that a bit that is a bit

## 34560:00 - 34600:00

separate like from world modeling and I

## 34600:00 - 34625:00

wonder like how the two of them like

## 34625:00 - 34675:00

will interplay among each other and

## 34675:00 - 34700:00

whether like you have actually planned

## 34700:00 - 34755:00

like to somehow like use them together.

## 34755:00 - 34795:00

uh as I see right now like VAS as more

## 34795:00 - 34835:00

of a policies uh that could actually

## 34835:00 - 34880:00

benefit a lot from world modeling and uh

## 34880:00 - 34930:00

from a B perspective I wonder like which

## 34930:00 - 34985:00

kind of infrastructure layers could be

## 34985:00 - 35035:00

the most useful uh to work on such as

## 35035:00 - 35095:00

like explanability, traceability or uh

## 35095:00 - 35145:00

uh safety in general to deploy such

## 35145:00 - 35185:00

models like in the real world.

## 35185:00 - 35230:00

>> Yeah, great question. So um on the first

## 35230:00 - 35270:00

point we there's actually fairly natural

## 35270:00 - 35290:00

ways to incorporate world model

## 35290:00 - 35320:00

objectives into vision language action

## 35320:00 - 35370:00

models and um we've done some work where

## 35370:00 - 35395:00

um instead of only predicting the next

## 35395:00 - 35425:00

action you predict some intermediate

## 35425:00 - 35465:00

subgoal image uh like what should happen

## 35465:00 - 35500:00

in the future in order to accomplish the

## 35500:00 - 35535:00

task uh and then predict an action from

## 35535:00 - 35565:00

there uh and we've seen some kind of

## 35565:00 - 35585:00

signs of life that that seems to be

## 35585:00 - 35610:00

quite promising. So I think there's ways

## 35610:00 - 35655:00

to merge the merge the two paradigms. Uh

## 35655:00 - 35680:00

at the same time I think there's a lot

## 35680:00 - 35700:00

of challenges that come up with world

## 35700:00 - 35745:00

modeling with regard to the ways in

## 35745:00 - 35775:00

which basically the data that you put

## 35775:00 - 35810:00

into it not necessarily being kind of

## 35810:00 - 35830:00

reflective of the ways in which you're

## 35830:00 - 35855:00

going to use it. You might train it on

## 35855:00 - 35885:00

demonstration data of successful data of

## 35885:00 - 35925:00

completing the task and then evaluate it

## 35925:00 - 35965:00

on to try to actually use it to evaluate

## 35965:00 - 35990:00

actions that are not optimally

## 35990:00 - 36020:00

completing the task. And then the world

## 36020:00 - 36065:00

model will hallucinate um a video of

## 36065:00 - 36095:00

completing the task successfully even if

## 36095:00 - 36130:00

the actions that you provide as input

## 36130:00 - 36150:00

didn't uh weren't actually going to

## 36150:00 - 36200:00

successfully lead to a good outcome. Um

## 36200:00 - 36225:00

so there's challenges there to overcome

## 36225:00 - 36265:00

and and so it's not like uh yeah there's

## 36265:00 - 36290:00

various challenges uh but there's also

## 36290:00 - 36325:00

ways to integrate it into the VA uh

## 36325:00 - 36355:00

paradigm and then could you remind me

## 36355:00 - 36380:00

your second question?

## 36380:00 - 36415:00

>> Um what are like the infrastructure

## 36415:00 - 36455:00

layers like you want the chess to work

## 36455:00 - 36510:00

on uh in the shortest term to bring like

## 36510:00 - 36535:00

the most

## 36535:00 - 36560:00

>> um

## 36560:00 - 36580:00

improvements let's say

## 36580:00 - 36615:00

>> to actually run these models on robots.

## 36615:00 - 36640:00

you need uh we have like a real-time

## 36640:00 - 36670:00

system um that needs to actually be

## 36670:00 - 36705:00

hitting a certain frequency to actually

## 36705:00 - 36740:00

like execute actions successfully. Uh

## 36740:00 - 36770:00

and if you have lag in that system and

## 36770:00 - 36800:00

so forth, it introduces all sorts of

## 36800:00 - 36825:00

challenges. And so thinking about fast

## 36825:00 - 36865:00

inference um and infrastructure for like

## 36865:00 - 36885:00

that's actually going to be on the robot

## 36885:00 - 36915:00

is a big part of uh what our software

## 36915:00 - 36950:00

team does. And then also thinking about

## 36950:00 - 36970:00

like large scale machine learning

## 36970:00 - 37000:00

infrastructure, training large models,

## 37000:00 - 37030:00

ingesting large amounts of data. Um the

## 37030:00 - 37065:00

data that we have is different from a

## 37065:00 - 37090:00

lot of kind of typical data sets because

## 37090:00 - 37130:00

it's very multimodal in nature. Um it's

## 37130:00 - 37175:00

kind of videos, actions, language

## 37175:00 - 37235:00

segments um and and various other uh

## 37235:00 - 37280:00

components as well. So um yeah, some

## 37280:00 - 37300:00

interesting infrastructure problems I

## 37300:00 - 37350:00

think both on the robot side uh and on

## 37350:00 - 37385:00

the kind of model training side.

## 37385:00 - 37410:00

>> Thank you so much.

## 37410:00 - 37425:00

>> Yep.

## 37425:00 - 37450:00

>> Hi, I'm Frederick and I have got a

## 37450:00 - 37490:00

question about model sizes in general.

## 37490:00 - 37520:00

So I think what we're seeing right now

## 37520:00 - 37565:00

is that in general larger model sizes

## 37565:00 - 37605:00

lead to better accuracy. For example,

## 37605:00 - 37645:00

also in your experiments or um it's also

## 37645:00 - 37675:00

what OpenAI and Enthropic and others are

## 37675:00 - 37700:00

doing right now with their LLMs.

## 37700:00 - 37730:00

However, there's also the approach of

## 37730:00 - 37775:00

using a quite small model and then

## 37775:00 - 37810:00

outsourcing the world knowledge into a

## 37810:00 - 37840:00

database of some sort with which the

## 37840:00 - 37890:00

model can interact. Um what is your take

## 37890:00 - 37910:00

on that? Do you think that's like a

## 37910:00 - 37940:00

valid approach or do you think

## 37940:00 - 37970:00

encapsulating all the world knowledge

## 37970:00 - 38015:00

inside of the model is better or works

## 38015:00 - 38025:00

better?

## 38025:00 - 38055:00

>> Yeah, it's an interesting question. So

## 38055:00 - 38090:00

in my experience working on like

## 38090:00 - 38145:00

retrievalbased systems um is that it

## 38145:00 - 38170:00

actually is a little bit tricky to well

## 38170:00 - 38190:00

first figure out what should be

## 38190:00 - 38220:00

offloaded versus actually done by the

## 38220:00 - 38260:00

model and second uh sometimes the model

## 38260:00 - 38295:00

will ignore the retrieved content and

## 38295:00 - 38335:00

try to generate something itself and it

## 38335:00 - 38365:00

it actually seems to be very quite

## 38365:00 - 38410:00

tricky to get that technically to work

## 38410:00 - 38445:00

uh exactly the way you want it. Um, I

## 38445:00 - 38465:00

think it's probably going to depend on

## 38465:00 - 38495:00

the application and the use case, uh, in

## 38495:00 - 38540:00

terms of how best to like like whether

## 38540:00 - 38570:00

that might make sense, but in my

## 38570:00 - 38585:00

experience, it ends up being quite

## 38585:00 - 38605:00

tricky to figure out what the division

## 38605:00 - 38655:00

of labor is. And even the like the model

## 38655:00 - 38685:00

part of it will need to have some degree

## 38685:00 - 38730:00

of intelligence in order to um like

## 38730:00 - 38760:00

actually make use of the retrieved

## 38760:00 - 38810:00

information and so forth. Uh, so I think

## 38810:00 - 38840:00

it's an really fascinating research

## 38840:00 - 38870:00

problem. Uh, but it also needs like a

## 38870:00 - 38905:00

lot of research to make that uh to that

## 38905:00 - 38935:00

make that work successfully.

## 38935:00 - 38955:00

Thank you.

## 38955:00 - 38965:00

>> Yeah.

## 38965:00 - 39005:00

>> Hi, Chelsea. My name is Charu Thomas.

## 39005:00 - 39045:00

Um, first off, really appreciate the

## 39045:00 - 39075:00

talk. It was really fascinating and have

## 39075:00 - 39100:00

been a big fan of your work since

## 39100:00 - 39145:00

metalarning. Um, when you think about

## 39145:00 - 39195:00

how software and hardware have are going

## 39195:00 - 39225:00

to continue to evolve, what are the

## 39225:00 - 39280:00

biggest opportunities for builders today

## 39280:00 - 39305:00

for your vision of physical

## 39305:00 - 39340:00

intelligence? I mean, I think that yeah,

## 39340:00 - 39370:00

there's lots of different like

## 39370:00 - 39420:00

opportunities to make things work a lot

## 39420:00 - 39450:00

better and a lot of like open questions.

## 39450:00 - 39470:00

I think kind of like what I was

## 39470:00 - 39500:00

mentioning before, uh, thinking about

## 39500:00 - 39545:00

better ways of having infrastructure on

## 39545:00 - 39580:00

like kind of the robot side. I think

## 39580:00 - 39605:00

that there isn't a lot of like there's

## 39605:00 - 39635:00

some open source code for that sort of

## 39635:00 - 39670:00

thing, but there's a lot of um

## 39670:00 - 39700:00

opportunities to make robot

## 39700:00 - 39755:00

infrastructure better. Uh, and not a lot

## 39755:00 - 39780:00

of people I think are are working on

## 39780:00 - 39815:00

that aspect of the problem. also lots of

## 39815:00 - 39840:00

opportunities like I guess one of the

## 39840:00 - 39885:00

things I love about um about AI and

## 39885:00 - 39910:00

computer science as a whole is there's a

## 39910:00 - 39945:00

really big open source community and I

## 39945:00 - 39970:00

think that there's a ton of opportunity

## 39970:00 - 40010:00

to actually like do open source work and

## 40010:00 - 40045:00

contribute to like a broader community

## 40045:00 - 40080:00

that's trying to like collect data open

## 40080:00 - 40120:00

source models fix bugs on those models

## 40120:00 - 40145:00

uh fine-tune those models figure out new

## 40145:00 - 40185:00

recipes for fine-tuning those models um

## 40185:00 - 40210:00

so yeah all sorts of questions also like

## 40210:00 - 40235:00

on the research side especially in the

## 40235:00 - 40255:00

open source realm

## 40255:00 - 40290:00

>> yeah thank you

## 40290:00 - 40330:00

>> hi Hi, Chelsea. Uh, I also, just like

## 40330:00 - 40365:00

everyone else, am a big fan of all your

## 40365:00 - 40390:00

work. So, thank you for putting that all

## 40390:00 - 40430:00

out. Uh, I've been reading through a lot

## 40430:00 - 40455:00

of your group's work recently and

## 40455:00 - 40500:00

particularly enjoyed reading Siraj uh,

## 40500:00 - 40545:00

Siraj's PhD thesis. It taught me a lot

## 40545:00 - 40580:00

about scaling real world robotics with

## 40580:00 - 40635:00

data. And a question I have is how do

## 40635:00 - 40660:00

you think synthetic data will sort of

## 40660:00 - 40695:00

scale for robotics in the future? As

## 40695:00 - 40735:00

we've seen with LMS, we've moved a we've

## 40735:00 - 40785:00

moved away from sort of not moved away

## 40785:00 - 40815:00

from pre-training, but moved away from

## 40815:00 - 40865:00

human collected data into more creating

## 40865:00 - 40890:00

synthetic data and a lot of filtering

## 40890:00 - 40930:00

and a lot of self-grading. So, how do

## 40930:00 - 40970:00

you think using generative synthetic

## 40970:00 - 41005:00

data for creating environments or reward

## 41005:00 - 41045:00

models will impact robotics?

## 41045:00 - 41065:00

>> Yeah, I have many thoughts on this

## 41065:00 - 41105:00

topic. Uh I think that at the end of the

## 41105:00 - 41130:00

day there's going to be no replacement

## 41130:00 - 41165:00

for real data and so we're like large

## 41165:00 - 41190:00

amounts of real robot data is going to

## 41190:00 - 41240:00

be a necessary component of any like

## 41240:00 - 41265:00

system that's going to work in a

## 41265:00 - 41295:00

generalizable way. Uh so we're going to

## 41295:00 - 41325:00

need that. Um, at the same time I do

## 41325:00 - 41345:00

think that there's tools for like

## 41345:00 - 41375:00

simulation and synthetic data especially

## 41375:00 - 41405:00

to potentially play on the evaluation

## 41405:00 - 41430:00

side because it's very tricky to

## 41430:00 - 41455:00

actually as you for example are

## 41455:00 - 41490:00

generalizing too many environments. It's

## 41490:00 - 41520:00

very tricky to actually evaluate how

## 41520:00 - 41550:00

well that model generalizes not just in

## 41550:00 - 41575:00

one new environment but in 10 new

## 41575:00 - 41590:00

environments because then you actually

## 41590:00 - 41625:00

need to bring the robot to those 10

## 41625:00 - 41645:00

environments or construct 10

## 41645:00 - 41680:00

environments. Uh whereas in simulation

## 41680:00 - 41715:00

that gets a lot easier. Uh and so I

## 41715:00 - 41740:00

think I'm really excited about kind of

## 41740:00 - 41765:00

simulation and synthetic data for that

## 41765:00 - 41795:00

use case. I should also mention that I

## 41795:00 - 41825:00

think that the analog of synthetic data

## 41825:00 - 41865:00

in language models is actually not

## 41865:00 - 41915:00

necessarily simulation in robotics but

## 41915:00 - 41940:00

closer to something like reinforcement

## 41940:00 - 41965:00

learning. Uh I think that a lot of

## 41965:00 - 41990:00

synthetic data is generated by the model

## 41990:00 - 42020:00

that's actually trying to do the task

## 42020:00 - 42040:00

and then trying to kind of reason

## 42040:00 - 42060:00

through different ways of doing the

## 42060:00 - 42090:00

task. And I think that the analogy there

## 42090:00 - 42120:00

is a robot that's trying to attempt the

## 42120:00 - 42150:00

task and learn from its own attempts and

## 42150:00 - 42180:00

get better from its own attempts. And

## 42180:00 - 42205:00

that sort of online data from the model

## 42205:00 - 42230:00

I think will also play a really critical

## 42230:00 - 42265:00

role in post training and something that

## 42265:00 - 42295:00

uh we're working on quite a bit. Uh and

## 42295:00 - 42325:00

so yeah that that I think is like really

## 42325:00 - 42350:00

important and really helpful.

## 42350:00 - 42375:00

>> Thank you.

## 42375:00 - 42405:00

>> Cool. I think we have time for one more

## 42405:00 - 42425:00

question. Sorry we won't be able to get

## 42425:00 - 42450:00

to everyone. Yeah.

## 42450:00 - 42490:00

>> Hi. It's super cool to see you as an MIT

## 42490:00 - 42525:00

EES alumni now working in a really cool

## 42525:00 - 42545:00

robotics and talking to us about

## 42545:00 - 42580:00

robotics and entrepreneurship. Um, but

## 42580:00 - 42610:00

I've been wondering how robotics

## 42610:00 - 42640:00

research that involves hardware

## 42640:00 - 42665:00

components plays out differently in

## 42665:00 - 42710:00

academia versus industry and are there

## 42710:00 - 42740:00

typically more resources, fewer

## 42740:00 - 42770:00

constraints or broader applications in

## 42770:00 - 42805:00

one setting over the other? And what

## 42805:00 - 42845:00

kind of people or goals do you think

## 42845:00 - 42885:00

might be better suited for each path?

## 42885:00 - 42910:00

>> Yeah, it's an interesting question. Uh,

## 42910:00 - 42970:00

I still love both kind of startup um and

## 42970:00 - 42995:00

academic environments and industry

## 42995:00 - 43015:00

environments. I think they all have

## 43015:00 - 43055:00

various pros and cons. Uh certainly I

## 43055:00 - 43090:00

think that uh any um I think that

## 43090:00 - 43120:00

generally academic environments aren't

## 43120:00 - 43150:00

quite as well resourced in terms of data

## 43150:00 - 43180:00

collection throughput, eval throughput

## 43180:00 - 43220:00

and compute as um like startups and

## 43220:00 - 43255:00

industry labs. Uh but at the same time I

## 43255:00 - 43290:00

think that there's a lot of uh problems

## 43290:00 - 43325:00

that you can solve without large amounts

## 43325:00 - 43360:00

of resources uh that uh we need to

## 43360:00 - 43390:00

figure out like on the algorithm side.

## 43390:00 - 43410:00

Uh so I think that there's a lot of

## 43410:00 - 43430:00

really interesting work to be done

## 43430:00 - 43470:00

there. Um and then on the like in

## 43470:00 - 43510:00

industry and in startups, I think the um

## 43510:00 - 43535:00

actually like trying to do some of the

## 43535:00 - 43565:00

research on these big models, scaling up

## 43565:00 - 43600:00

data, seeing what hap things happen at

## 43600:00 - 43650:00

large scales um is is really great to do

## 43650:00 - 43675:00

there. Yeah, I think that there's yeah,

## 43675:00 - 43700:00

there's there's a place for both. I also

## 43700:00 - 43740:00

think that the gap isn't as large as

## 43740:00 - 43780:00

often people make it seem. Uh and

## 43780:00 - 43805:00

oftentimes people in industry

## 43805:00 - 43830:00

environments kind of wish they had more

## 43830:00 - 43860:00

compute. Like you kind of always wish

## 43860:00 - 43895:00

that you had more resources. uh and

## 43895:00 - 43920:00

sometimes when you have a lot of

## 43920:00 - 43950:00

resources, you don't actually think as

## 43950:00 - 43985:00

carefully and as critically about what

## 43985:00 - 44005:00

runs you're going to be doing and so

## 44005:00 - 44040:00

forth and you uh end up being sometimes

## 44040:00 - 44080:00

more wasteful of compute uh than if you

## 44080:00 - 44105:00

were kind of more compute constrained.

## 44105:00 - 44130:00

So there's also actually downsides to

## 44130:00 - 44165:00

having more resources in my experience.

## 44165:00 - 44200:00

>> I'm really sorry. Can I just ask a one

## 44200:00 - 44240:00

quick question on architecture? I know

## 44240:00 - 44290:00

that um the scaling laws have worked

## 44290:00 - 44330:00

well for transformer based architectures

## 44330:00 - 44365:00

and I was thinking do you see currently

## 44365:00 - 44435:00

limits um in VLM based architecture

## 44435:00 - 44470:00

which are kind of made for like text

## 44470:00 - 44510:00

tokens because they don't have like

## 44510:00 - 44565:00

modules for physical awareness. Yeah.

## 44565:00 - 44595:00

And how do you deal with that?

## 44595:00 - 44625:00

>> Yeah. So, we we tokenized the actions

## 44625:00 - 44650:00

and so I'd encourage you to take a look

## 44650:00 - 44685:00

at the the fast tokenizer paper that we

## 44685:00 - 44715:00

put out um as as kind of a way to

## 44715:00 - 44745:00

accomplish that. And yeah, we should uh

## 44745:00 - 44785:00

wrap up there. Uh thanks everyone and um

## 44785:00+

yeah, hope you enjoy the event.

