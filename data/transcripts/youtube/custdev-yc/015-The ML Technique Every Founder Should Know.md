---
source: https://www.youtube.com/watch?v=dC_3ys349bU
title: The ML Technique Every Founder Should Know
author: Y Combinator
date: 2026-01-22
views: 36841
description: >-
  Diffusion is the foundational machine learning framework behind
  state-of-the-art AI image and video generation, including Sora, Midjourney and
  Google Veo. In this episode of Decoded, YC General Partner Ankit Gupta sits
  down with YC Visiting Partner Francois Chaubard to discuss how diffusion
  works, walk through a code sample, and explain why everyone training models
  should understand it.


  Apply to Y Combinator: https://www.ycombinator.com/apply

  Work at a startup: https://www.ycombinator.com/jobs


  Chapters:


  00:00 Intro

  00:33 What is diffusion?

  02:50 What are applications of diffusion today?

  04:06 Key innovations

  07:01 Code examples

  19:25 The "squint test"

  22:27 Other areas diffusion is widely accessible 

  24:49 Outro
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:39:02.691Z
---

# The ML Technique Every Founder Should Know

## 00:00 - 20:00

Welcome back to another episode of

## 20:00 - 60:00

Decoded. Today I'm sitting down with YC

## 60:00 - 95:00

visiting partner Francois Shaard to talk

## 95:00 - 120:00

about one of the most important topics

## 120:00 - 155:00

in AI today, diffusion. Francois has

## 155:00 - 185:00

been doing computer vision since 2012

## 185:00 - 220:00

when he started in Fee Le's lab. And

## 220:00 - 250:00

after a decade running focal systems,

## 250:00 - 275:00

he's currently back at Stanford

## 275:00 - 300:00

finishing his PhD working on

## 300:00 - 330:00

diffusion-based world models for AGI.

## 330:00 - 350:00

We're going to break down what diffusion

## 350:00 - 375:00

is, how it's evolved over the past

## 375:00 - 490:00

decade, and how it's used today.

## 490:00 - 520:00

>> [music]

## 520:00 - 545:00

>> Francois, thanks for being here.

## 545:00 - 560:00

>> Thank you for having me.

## 560:00 - 590:00

>> Well, we just got back from Nurups. We

## 590:00 - 610:00

just spent a lot of time talking to

## 610:00 - 640:00

researchers and thinking about all the

## 640:00 - 680:00

newest models out there. Um, I think we

## 680:00 - 720:00

saw diffusion pop up over and over and

## 720:00 - 750:00

newer versions of these type of uh

## 750:00 - 775:00

approaches that are not auto reggressive

## 775:00 - 805:00

LLM. And so I wanted to talk to you

## 805:00 - 830:00

about those today. So first, why don't

## 830:00 - 870:00

we start by defining um what is

## 870:00 - 910:00

diffusion? The fusion is a very

## 910:00 - 945:00

fundamental machine learning framework

## 945:00 - 1000:00

that allows you to learn any p data any

## 1000:00 - 1040:00

probability of data for any domain as

## 1040:00 - 1055:00

long as you have the data.

## 1055:00 - 1075:00

>> So you're trying to learn some data

## 1075:00 - 1090:00

distribution.

## 1090:00 - 1095:00

>> That's right.

## 1095:00 - 1135:00

>> Now in a sense all LLMs or all machine

## 1135:00 - 1170:00

learning models are about learning data

## 1170:00 - 1185:00

distributions.

## 1185:00 - 1220:00

>> How does diffusion in particular what

## 1220:00 - 1245:00

what stance does it take or what

## 1245:00 - 1270:00

approach does it take to being able to

## 1270:00 - 1280:00

learn distribution?

## 1280:00 - 1295:00

>> Yeah, I mean I think you can use

## 1295:00 - 1335:00

diffusion to to always do that. The

## 1335:00 - 1360:00

thing where it stands out in particular

## 1360:00 - 1395:00

is mapping from high dimensions to high

## 1395:00 - 1445:00

dimensions, especially in low data uh

## 1445:00 - 1480:00

regimes. So, say I only have 30 images

## 1480:00 - 1505:00

of Gary, which I actually have some code

## 1505:00 - 1540:00

that we're going to walk through. Um, I

## 1540:00 - 1565:00

only have 30 images of Gary and again,

## 1565:00 - 1640:00

we're in this thousand by 10,000 by3 uh

## 1640:00 - 1680:00

uh dimensional space and I want to map

## 1680:00 - 1720:00

to another three 3 million dimensional

## 1720:00 - 1765:00

space with only 30 training samples and

## 1765:00 - 1795:00

I can still do it and it's pretty pretty

## 1795:00 - 1810:00

powerful in that way.

## 1810:00 - 1835:00

>> Okay, cool. So, so you have this ability

## 1835:00 - 1865:00

to use relatively small amounts of data

## 1865:00 - 1900:00

compared to the dimensionality to learn

## 1900:00 - 1920:00

a P data. That's right.

## 1920:00 - 1960:00

>> Um, what's the what's the basic process

## 1960:00 - 1990:00

by which diffusion works? Like just walk

## 1990:00 - 2020:00

through like at a very high level and

## 2020:00 - 2035:00

we'll walk through the math a little bit

## 2035:00 - 2065:00

later, but a very high level, how does

## 2065:00 - 2085:00

this process actually work?

## 2085:00 - 2130:00

>> We take some sample of the data, an

## 2130:00 - 2180:00

image of Anka, an image of Gary, and we

## 2180:00 - 2205:00

just hit it with noise. And then we just

## 2205:00 - 2230:00

keep hitting it with noise and we create

## 2230:00 - 2285:00

this train of of noised up images. It's

## 2285:00 - 2315:00

very easy to create noisy images, right?

## 2315:00 - 2360:00

It's hard to create get walk backwards

## 2360:00 - 2415:00

and create from noise images of you or

## 2415:00 - 2460:00

Gary. And so then we flip it and then we

## 2460:00 - 2505:00

try to have teach the model to reverse

## 2505:00 - 2540:00

that process. And that's basically it.

## 2540:00 - 2585:00

>> Okay, cool. So it's basically a a noiser

## 2585:00 - 2610:00

and a dinoiser and the dinoiser is the

## 2610:00 - 2635:00

model that you end up training.

## 2635:00 - 2665:00

>> Exactly. Yeah. You will uh you will

## 2665:00 - 2695:00

basically teach your force and and give

## 2695:00 - 2745:00

it uh noised up images and then have it

## 2745:00 - 2775:00

learn intermediate representations to

## 2775:00 - 2800:00

get to back to P data.

## 2800:00 - 2835:00

>> Cool. Nice. And what kinds of stuff is

## 2835:00 - 2860:00

diffusion used for today? What are some

## 2860:00 - 2885:00

applications that it's widely deployed

## 2885:00 - 2895:00

in?

## 2895:00 - 2945:00

>> It's honestly surprising how uh uh

## 2945:00 - 2990:00

applicable this process is. I think the

## 2990:00 - 3050:00

the original 2015 Joshua Sixine paper

## 3050:00 - 3105:00

was on CIPR10 which is just images. Um,

## 3105:00 - 3145:00

and I think it's got it has its roots in

## 3145:00 - 3200:00

images, but it is far uh uh more

## 3200:00 - 3230:00

sprawling than just images. As you've

## 3230:00 - 3260:00

seen, we you know, uh uh Deep Mind just

## 3260:00 - 3300:00

won the Nobel Prize for doing this exact

## 3300:00 - 3350:00

procedure on protein folding. Uh you can

## 3350:00 - 3380:00

drive cars with this with the diffusion

## 3380:00 - 3415:00

policy paper, which is like an insane

## 3415:00 - 3475:00

result. Um you can um uh predict the

## 3475:00 - 3520:00

weather. Um there's really no limit to

## 3520:00 - 3535:00

the things that this can do.

## 3535:00 - 3555:00

>> Yeah, it's pretty incredible to see. I

## 3555:00 - 3585:00

mean we have these image and video

## 3585:00 - 3615:00

generation models that seem to be really

## 3615:00 - 3640:00

advancing over the last few years.

## 3640:00 - 3660:00

Stable diffusion is the one that I think

## 3660:00 - 3690:00

many people have heard of and then newer

## 3690:00 - 3715:00

versions of it seem to be using this as

## 3715:00 - 3740:00

well. And then yeah in the world of life

## 3740:00 - 3775:00

sciences that my company was in too. I

## 3775:00 - 3805:00

think we see this newest generation of

## 3805:00 - 3845:00

life sciences AI companies are heavily

## 3845:00 - 3870:00

investing in this set of technologies.

## 3870:00 - 3895:00

There's a model called diff do that

## 3895:00 - 3925:00

works really well for predicting uh

## 3925:00 - 3955:00

small molecule binding to proteins and

## 3955:00 - 3980:00

then yeah alpha fold especially the

## 3980:00 - 4010:00

newest alpha fold versions use diffusion

## 4010:00 - 4040:00

pretty heavily. It's really cool to see

## 4040:00 - 4070:00

the same core piece of technology apply

## 4070:00 - 4090:00

to so many different domains.

## 4090:00 - 4105:00

>> Yeah. Yeah.

## 4105:00 - 4130:00

>> This class of models has evolved over

## 4130:00 - 4165:00

the years and you know there's a whole

## 4165:00 - 4185:00

slew of papers someone could read. So

## 4185:00 - 4205:00

you should probably go read the papers

## 4205:00 - 4230:00

to learn all the details. But maybe at a

## 4230:00 - 4270:00

high level we can try to trace out a few

## 4270:00 - 4300:00

of the key

## 4300:00 - 4325:00

>> innovations that happened starting with

## 4325:00 - 4360:00

the paper you already mentioned that now

## 4360:00 - 4385:00

led to the newest versions of these

## 4385:00 - 4410:00

models. So how would you map those out?

## 4410:00 - 4440:00

Like what was the the first kind of turn

## 4440:00 - 4475:00

of the crank from this very high level

## 4475:00 - 4530:00

diffusion process you uh outlined? What

## 4530:00 - 4545:00

was the first version of that that

## 4545:00 - 4560:00

started to work?

## 4560:00 - 4595:00

>> Yeah. So I think that the 2015 original

## 4595:00 - 4665:00

Josha paper um is it put up all the key

## 4665:00 - 4705:00

pieces all the key components of modern

## 4705:00 - 4730:00

diffusion and so like now we're just

## 4730:00 - 4750:00

playing with different things. So

## 4750:00 - 4790:00

theuler how do we add noise at what

## 4790:00 - 4830:00

weight like that's a whole part that we

## 4830:00 - 4855:00

can discuss. What's the loss function?

## 4855:00 - 4885:00

Should I predict should the the deep

## 4885:00 - 4925:00

learning model condition upon x of t

## 4925:00 - 4970:00

predict uh the actual data x of t minus

## 4970:00 - 5010:00

one or should it pred predict the error

## 5010:00 - 5045:00

that was just added to it or should it

## 5045:00 - 5070:00

predict the velocity which is the error

## 5070:00 - 5125:00

divided by the time uh should it predict

## 5125:00 - 5165:00

the velocity of the the start and the

## 5165:00 - 5195:00

end that's called flow matching there's

## 5195:00 - 5220:00

so there's all these different plays on

## 5220:00 - 5240:00

what the loss function is

## 5240:00 - 5270:00

>> so in all of those the idea is still to

## 5270:00 - 5290:00

do dnoising

## 5290:00 - 5300:00

>> yes

## 5300:00 - 5360:00

>> uh but the objective for each of them is

## 5360:00 - 5380:00

somewhat different from each other. I

## 5380:00 - 5400:00

mean they're all pretty closely related

## 5400:00 - 5425:00

whether it's basically a delta between

## 5425:00 - 5455:00

two things or the previous step or the

## 5455:00 - 5475:00

first step. How do these all actually

## 5475:00 - 5500:00

come together? Were these are series of

## 5500:00 - 5540:00

papers that happened one after another?

## 5540:00 - 5565:00

>> Yeah, I think we just kind of hill

## 5565:00 - 5615:00

climbed on this uh ferroche inception

## 5615:00 - 5645:00

distance metric that's kind of a kooky

## 5645:00 - 5695:00

weird uh um measure to see how good an

## 5695:00 - 5725:00

image is. Um but we just kept getting

## 5725:00 - 5750:00

better and better and better on it by

## 5750:00 - 5775:00

like doing these little tricks. And so

## 5775:00 - 5810:00

like it turns out that predicting the

## 5810:00 - 5835:00

actual data itself is actually quite

## 5835:00 - 5860:00

hard. And like maybe predicting the

## 5860:00 - 5885:00

error is actually easier. And then

## 5885:00 - 5915:00

predicting the velocity was even easier

## 5915:00 - 5970:00

than that. And then predicting the uh

## 5970:00 - 6010:00

global error across the entire diffusion

## 6010:00 - 6040:00

schedule is even easier than that. And

## 6040:00 - 6070:00

like just kept finding easier and easier

## 6070:00 - 6130:00

ways um to to basically uh sample from

## 6130:00 - 6165:00

noise to data. And here when you say

## 6165:00 - 6225:00

easier were was the ease largely driven

## 6225:00 - 6270:00

by it was mathematically simpler or it

## 6270:00 - 6320:00

was easier to implement an engineer or

## 6320:00 - 6365:00

simpler to reason about or what what got

## 6365:00 - 6375:00

easier really.

## 6375:00 - 6405:00

>> It actually is that too but I didn't

## 6405:00 - 6430:00

mean it that way. What I actually meant

## 6430:00 - 6465:00

was it's easier for the model to learn.

## 6465:00 - 6500:00

>> Um but it is also and we'll go through

## 6500:00 - 6540:00

some coding examples. The math actually

## 6540:00 - 6575:00

got easier. Yeah. and like the the the

## 6575:00 - 6615:00

code got smaller which is actually

## 6615:00 - 6670:00

opposite oppositely true in uh most of

## 6670:00 - 6695:00

uh the case of most machine learning

## 6695:00 - 6725:00

actually things get more complicated. I

## 6725:00 - 6750:00

think we started with units and that was

## 6750:00 - 6785:00

like the predominant architecture we

## 6785:00 - 6800:00

didn't really talk about architectures

## 6800:00 - 6835:00

that much but then we got into these uh

## 6835:00 - 6865:00

diffusion transformers and like this

## 6865:00 - 6890:00

cross attention mechanism and things

## 6890:00 - 6930:00

like that and so um yeah we just kept

## 6930:00 - 6985:00

getting better and better at reducing uh

## 6985:00 - 7005:00

FID.

## 7005:00 - 7030:00

>> Interesting. Should we dive into some

## 7030:00 - 7050:00

code examples? Let's do it.

## 7050:00 - 7060:00

>> Let's do it.

## 7060:00 - 7100:00

>> I'll walk you through. I made about uh

## 7100:00 - 7145:00

one, two, three, four, five, six, seven

## 7145:00 - 7185:00

of these that I implemented um with

## 7185:00 - 7225:00

varying levels of success, but uh the

## 7225:00 - 7255:00

the all the structures are going to be

## 7255:00 - 7290:00

the same. So the the Josha paper, the

## 7290:00 - 7335:00

non-equilibrium thermodynamics paper, uh

## 7335:00 - 7365:00

you can see here here are some nice

## 7365:00 - 7405:00

images of Gary. You can see here very

## 7405:00 - 7430:00

nice. This is the what I could find

## 7430:00 - 7440:00

online.

## 7440:00 - 7465:00

>> Nice. Um, and then

## 7465:00 - 7495:00

>> so those are images of Gary that you've

## 7495:00 - 7525:00

downsampled so that they're a thousand

## 7525:00 - 7555:00

by thousand or they're they're smaller.

## 7555:00 - 7560:00

These are

## 7560:00 - 7575:00

>> 64 by 64.

## 7575:00 - 7590:00

>> 64 by 64.

## 7590:00 - 7605:00

>> Yeah, they're really small. This is just

## 7605:00 - 7640:00

a very small example. 64 and then I

## 7640:00 - 7680:00

randomly augment it to create more data.

## 7680:00 - 7710:00

Great. >> Um, because I was I was lazy and that

## 7710:00 - 7740:00

was easier than uh downloading more

## 7740:00 - 7780:00

images and [laughter] cool.

## 7780:00 - 7810:00

>> Didn't want to get security on you.

## 7810:00 - 7850:00

>> Exactly. So and then wait I implemented

## 7850:00 - 7875:00

this diffusion schedule and this is

## 7875:00 - 7910:00

probably one of the most important like

## 7910:00 - 7940:00

of all the parts of diffusion that's

## 7940:00 - 7970:00

difficult to comprehend I would say that

## 7970:00 - 8005:00

the noise schedule is actually the

## 8005:00 - 8030:00

hardest part to understand and that I

## 8030:00 - 8070:00

really like I struggled with myself and

## 8070:00 - 8115:00

so if you can see here the noise that's

## 8115:00 - 8165:00

added from time step uh zero to t to 10

## 8165:00 - 8230:00

to 25 all the way to 100 uh is clearly

## 8230:00 - 8255:00

destroying the structure.

## 8255:00 - 8265:00

>> Yes.

## 8265:00 - 8295:00

>> And then we want to end is basically

## 8295:00 - 8330:00

random static. Exactly. And we want to

## 8330:00 - 8365:00

basically reverse this and from here get

## 8365:00 - 8400:00

to here and have the model get to that

## 8400:00 - 8420:00

point, get to this point, get the point,

## 8420:00 - 8485:00

etc., etc. And so, uh, the interesting

## 8485:00 - 8525:00

part, and this is Joshua really, you

## 8525:00 - 8560:00

know, uh, implemented almost everything

## 8560:00 - 8600:00

that we needed for diffusion. Um, and

## 8600:00 - 8620:00

there was just a few little tweaks that

## 8620:00 - 8650:00

were missing, and he didn't he didn't

## 8650:00 - 8685:00

scale it up. That's to me the the parts

## 8685:00 - 8750:00

that, um, uh, were were missing. And if

## 8750:00 - 8790:00

you see here the, um, the noise

## 8790:00 - 8845:00

schedule. So it would make sense to me

## 8845:00 - 8910:00

that I would have linear interpolation

## 8910:00 - 8955:00

between uh the image and the noise. And

## 8955:00 - 9005:00

I would start with like one and zero,

## 9005:00 - 9045:00

one being the image and zero being the

## 9045:00 - 9070:00

noise. You gradually add it and I gra

## 9070:00 - 9105:00

and I linearly add it. But if you do

## 9105:00 - 9150:00

that, it actually is massively unstable

## 9150:00 - 9180:00

because the instantaneous amount of

## 9180:00 - 9225:00

error that you're adding is very small

## 9225:00 - 9245:00

in the beginning. If you think about

## 9245:00 - 9260:00

like an image

## 9260:00 - 9275:00

>> on a relative basis

## 9275:00 - 9305:00

>> on a relative basis and then at the end

## 9305:00 - 9345:00

you have to to destroy all the to get to

## 9345:00 - 9385:00

complete noise you need to add a lot of

## 9385:00 - 9395:00

error

## 9395:00 - 9425:00

>> and so like if you're a model and you're

## 9425:00 - 9455:00

just looking at this little chunk of the

## 9455:00 - 9495:00

noise schedule then you have to handle a

## 9495:00 - 9535:00

lot of error in one step and on this

## 9535:00 - 9565:00

side of the the schedule you need to

## 9565:00 - 9600:00

handle such small amounts of error and

## 9600:00 - 9645:00

what you actually want is constant rel

## 9645:00 - 9680:00

like like relatively constant amount of

## 9680:00 - 9710:00

error being introduced every single time

## 9710:00 - 9760:00

step right and that the the cumulative

## 9760:00 - 9790:00

sum of all that error actually ends up

## 9790:00 - 9830:00

looking like this uh like this curve

## 9830:00 - 9840:00

here.

## 9840:00 - 9875:00

>> That's the uh the pink curve.

## 9875:00 - 9880:00

>> Yeah.

## 9880:00 - 9920:00

>> And so they call this a beta schedule.

## 9920:00 - 9970:00

Beta is the diffusion rate, the rate of

## 9970:00 - 10000:00

diffusion that I'm I'm doing while I'm

## 10000:00 - 10025:00

rolling this thing out from time zero to

## 10025:00 - 10080:00

time uh t capital t. And uh and so you

## 10080:00 - 10125:00

can see here the the beta schedule. So

## 10125:00 - 10165:00

we we have usually have some beta min to

## 10165:00 - 10230:00

beta max and then we one minus that is

## 10230:00 - 10260:00

the alpha and you can think about the

## 10260:00 - 10290:00

beta as like how much noise I'm adding

## 10290:00 - 10310:00

at every time step. Yep.

## 10310:00 - 10335:00

>> And you think about the alpha as how

## 10335:00 - 10370:00

much

## 10370:00 - 10405:00

yeah being retained and then the term

## 10405:00 - 10445:00

that really matters is the alpha bar and

## 10445:00 - 10470:00

these are the weight weights that are

## 10470:00 - 10520:00

used and it has this kind of like one

## 10520:00 - 10570:00

minus sigmoid looking thing. Um but

## 10570:00 - 10615:00

that's basically the the noise schedule

## 10615:00 - 10655:00

and once you get that right really this

## 10655:00 - 10695:00

this this part here then everything kind

## 10695:00 - 10735:00

of else just works and then I train some

## 10735:00 - 10760:00

model and then we can actually

## 10760:00 - 10790:00

>> so there what was the training objective

## 10790:00 - 10810:00

again? So you were adding this noise and

## 10810:00 - 10840:00

the training objective was to do what

## 10840:00 - 10845:00

exactly

## 10845:00 - 10880:00

>> the train in this case it's to minimize

## 10880:00 - 10915:00

the kale divergence between the

## 10915:00 - 10945:00

distribution uh the real distribution

## 10945:00 - 10980:00

and the distribution that I'm learning.

## 10980:00 - 11025:00

And so um I I won't go through the code

## 11025:00 - 11045:00

for this one because it's a little bit

## 11045:00 - 11080:00

hairier, but you can kind of see the

## 11080:00 - 11125:00

result on these generated images um

## 11125:00 - 11165:00

after 100 diffusion steps at inference

## 11165:00 - 11200:00

time. And you can see that the ferroche

## 11200:00 - 11235:00

inception distance is 222

## 11235:00 - 11285:00

>> which is like extremely high today like

## 11285:00 - 11310:00

modern day would be like maybe like

## 11310:00 - 11335:00

eight or 10 or something. And what's

## 11335:00 - 11355:00

interesting here, I mean, you kind of

## 11355:00 - 11380:00

scroll through it there, but it's, and

## 11380:00 - 11410:00

you mentioned it, there's quite a lot of

## 11410:00 - 11435:00

code that it actually takes to do that

## 11435:00 - 11485:00

kale divergence base loss. I suspect

## 11485:00 - 11510:00

that in these later models you're going

## 11510:00 - 11540:00

to show, it gets significantly simpler.

## 11540:00 - 11570:00

So, I'm I'm just mentally noting that

## 11570:00 - 11585:00

because I suspect there's going to be

## 11585:00 - 11620:00

interesting contrast to draw uh between

## 11620:00 - 11630:00

these two.

## 11630:00 - 11655:00

>> Yeah. So, the next one I would like to

## 11655:00 - 11685:00

show is flow matching, which is it's

## 11685:00 - 11725:00

just so beautiful and simple. Uh and

## 11725:00 - 11805:00

this was out of um meta uh yearn litman

## 11805:00 - 11850:00

uh where he basically said we don't need

## 11850:00 - 11880:00

a lot of this stuff. What we need to do

## 11880:00 - 11920:00

forget the if you think about the

## 11920:00 - 11990:00

noising process as being this like um I

## 11990:00 - 12030:00

start from data I randomly sample a

## 12030:00 - 12045:00

vector

## 12045:00 - 12080:00

>> of noise and I just go in this direction

## 12080:00 - 12105:00

and then I do it again. I go in this

## 12105:00 - 12125:00

direction and I do it again. I go in

## 12125:00 - 12145:00

that direction. I go in this direction

## 12145:00 - 12165:00

that direction and then I'm here at

## 12165:00 - 12195:00

noise and then you have to teach the

## 12195:00 - 12245:00

thing to go in the exact opposite path

## 12245:00 - 12270:00

and you have to do this very securest

## 12270:00 - 12300:00

path and so at test time it's actually

## 12300:00 - 12330:00

quite expensive you have to do we've all

## 12330:00 - 12380:00

waited for you know uh chatgbt or or to

## 12380:00 - 12410:00

to or midjourney to like make an image

## 12410:00 - 12445:00

and it takes a while it's doing like a

## 12445:00 - 12475:00

thousand calls to the model again and

## 12475:00 - 12505:00

again iterating through to get to that

## 12505:00 - 12530:00

point of p data right

## 12530:00 - 12565:00

>> instead and like intuitively it's like

## 12565:00 - 12605:00

okay we're doing the ciruitous path but

## 12605:00 - 12630:00

surely there's a shorter path between

## 12630:00 - 12640:00

those two.

## 12640:00 - 12665:00

>> And so that's what makes flow matching

## 12665:00 - 12705:00

so cool to me at least is that they said

## 12705:00 - 12755:00

forget all of that intermediary results.

## 12755:00 - 12820:00

There is a a velocity a global velocity

## 12820:00 - 12885:00

between the noise and the data and it's

## 12885:00 - 12915:00

just this direction. It's just this

## 12915:00 - 12945:00

straight line. And I don't care where

## 12945:00 - 12980:00

you are go in that line. Wherever you

## 12980:00 - 13000:00

are, you're over here. Go in that line

## 13000:00 - 13030:00

and teach it to go in that line. And

## 13030:00 - 13050:00

that's what flow matching does. And so

## 13050:00 - 13080:00

I'll show that in the code. I bet it's

## 13080:00 - 13110:00

like five lines of code. It really is

## 13110:00 - 13145:00

quite simple. And so this pretty cool.

## 13145:00 - 13165:00

So

## 13165:00 - 13210:00

>> here you go. The

## 13210:00 - 13250:00

>> you basically have like 10 15 lines of

## 13250:00 - 13295:00

code that is the most powerful machine

## 13295:00 - 13330:00

learning procedure uh ever.

## 13330:00 - 13380:00

>> So I I have some data I an image of

## 13380:00 - 13390:00

Gary.

## 13390:00 - 13395:00

>> Yep.

## 13395:00 - 13430:00

>> I have some noise that I I I some

## 13430:00 - 13460:00

isotropic Gaussian noise that I sample

## 13460:00 - 13465:00

from.

## 13465:00 - 13520:00

>> Yep. there's some time that I'm I'm

## 13520:00 - 13545:00

trying to index into in the diffusion

## 13545:00 - 13600:00

schedule and I'm and I create XT, which

## 13600:00 - 13635:00

is the image at the noised up image

## 13635:00 - 13675:00

that's somewhere between extremely noisy

## 13675:00 - 13695:00

and not noisy at all.

## 13695:00 - 13715:00

>> And and that's basically just the

## 13715:00 - 13745:00

sampling procedure. It's T* data.

## 13745:00 - 13755:00

>> Yep.

## 13755:00 - 13790:00

>> Plus one minus that times noise. Yeah,

## 13790:00 - 13820:00

>> that's right. And then I compute the

## 13820:00 - 13865:00

velocity which is independent of the

## 13865:00 - 13890:00

time. I don't care where you are. It's

## 13890:00 - 13920:00

just the global velocity which is just

## 13920:00 - 13970:00

the noise minus the data. And then it I

## 13970:00 - 14020:00

return that back to my uh training loop

## 14020:00 - 14055:00

which is the the shortest amount of code

## 14055:00 - 14070:00

training [laughter] loop I've ever

## 14070:00 - 14125:00

written which is five lines of code. Um

## 14125:00 - 14180:00

I have my batch I have some time. I

## 14180:00 - 14220:00

sample from that function I just uh

## 14220:00 - 14275:00

explained before and then I have my

## 14275:00 - 14310:00

prediction from the model. I feed it in

## 14310:00 - 14380:00

this some element uh some some uh noise

## 14380:00 - 14410:00

up image somewhere between lots of noise

## 14410:00 - 14435:00

and little noise x of t let's call it

## 14435:00 - 14460:00

and I just want it to predict the

## 14460:00 - 14495:00

velocity that I want to go

## 14495:00 - 14515:00

>> and this is also really powerful because

## 14515:00 - 14545:00

here you know you have model abstractor

## 14545:00 - 14585:00

but that model can be any model right so

## 14585:00 - 14625:00

you can put in whatever the relevant

## 14625:00 - 14650:00

model is for your distribution whether

## 14650:00 - 14685:00

that's a protein model for proteins or

## 14685:00 - 14730:00

if it's an LLM for text or an image

## 14730:00 - 14755:00

based model for images

## 14755:00 - 14800:00

>> that is a very clean abst raction as

## 14800:00 - 14820:00

long as you can then predict this

## 14820:00 - 14840:00

velocity and then move in that

## 14840:00 - 14850:00

direction.

## 14850:00 - 14890:00

>> That's right. This code here has nothing

## 14890:00 - 14930:00

to do with images. It could be weather

## 14930:00 - 14970:00

data. It could be, you know, uh uh stock

## 14970:00 - 15015:00

market data. It could be um trajectories

## 15015:00 - 15070:00

from a robotics in a teaops setup. Um it

## 15070:00 - 15105:00

could be proteins. It could be DNA. It

## 15105:00 - 15130:00

doesn't really matter. It's all the

## 15130:00 - 15170:00

exact same code. Um and so and then also

## 15170:00 - 15185:00

we haven't talked about the

## 15185:00 - 15225:00

architecture. So like this model here

## 15225:00 - 15255:00

could be anything you want it to be.

## 15255:00 - 15315:00

like it could be a RNN, it could be a uh

## 15315:00 - 15350:00

UNET which is typically you know

## 15350:00 - 15390:00

traditionally is and and modernly they

## 15390:00 - 15425:00

use these diffusion uh transformers

## 15425:00 - 15460:00

doing this cross attention mechanism and

## 15460:00 - 15510:00

so it can be whatever you want. Um but

## 15510:00 - 15535:00

this all that is independent from

## 15535:00 - 15555:00

whether or not you're doing flow

## 15555:00 - 15595:00

matching or not. I think this is like a

## 15595:00 - 15630:00

really profoundly

## 15630:00 - 15665:00

interesting result in that especially

## 15665:00 - 15705:00

this um I think we often assume as

## 15705:00 - 15730:00

models have gotten more sophisticated

## 15730:00 - 15755:00

that they become less accessible for

## 15755:00 - 15785:00

people to understand but this is

## 15785:00 - 15815:00

>> quite literally 10 lines of code right

## 15815:00 - 15820:00

[laughter]

## 15820:00 - 15845:00

>> that explains

## 15845:00 - 15875:00

>> essentially all of the most important

## 15875:00 - 15910:00

kind of mathematical and fundamental

## 15910:00 - 15950:00

foundations of the models that we all

## 15950:00 - 15985:00

see as generating basically like magical

## 15985:00 - 16010:00

AI results on our phones. Of course,

## 16010:00 - 16025:00

there's lots of engineering how you

## 16025:00 - 16055:00

scale them up. you know that that model

## 16055:00 - 16100:00

could be a 100 billion parameter

## 16100:00 - 16150:00

transformer data centers you know GPUs

## 16150:00 - 16180:00

yeah 100% so it's the engineering that's

## 16180:00 - 16205:00

the really hard part there but a lot of

## 16205:00 - 16230:00

the basic machine learning math is

## 16230:00 - 16250:00

actually quite straightforward

## 16250:00 - 16310:00

>> that's right um yeah and so uh there's a

## 16310:00 - 16345:00

bunch of these like tangent fields to

## 16345:00 - 16390:00

diffusion that all have some different

## 16390:00 - 16415:00

interpretation on what's actually

## 16415:00 - 16435:00

happening but it's all the same exact

## 16435:00 - 16470:00

math and most people learning diffusion

## 16470:00 - 16500:00

actually get quite confused because if

## 16500:00 - 16560:00

you talk to um some uh uh you know

## 16560:00 - 16590:00

probabistic graphical model people they

## 16590:00 - 16615:00

were saying oh this is a proistic

## 16615:00 - 16645:00

graphical model and what's actually this

## 16645:00 - 16670:00

is a hidden markoff model and what we're

## 16670:00 - 16690:00

doing is we're learning this like

## 16690:00 - 16725:00

marovian thing or whatever it's like

## 16725:00 - 16785:00

okay fine but like it's just

## 16785:00 - 16810:00

>> noise [laughter]

## 16810:00 - 16840:00

>> and like you should just show that first

## 16840:00 - 16865:00

and then like if you think about it from

## 16865:00 - 16910:00

like a physics perspective and and

## 16910:00 - 16940:00

there's all this statmech people that

## 16940:00 - 16980:00

have that interpretation um there's a

## 16980:00 - 16995:00

whole bunch of the different

## 16995:00 - 17025:00

interpretations I think it's it gets a

## 17025:00 - 17065:00

little bit uh confusing. Um and the the

## 17065:00 - 17090:00

whole stocastic differential equation

## 17090:00 - 17120:00

people like thinking about that this is

## 17120:00 - 17165:00

a an SDE and I think that's all fine and

## 17165:00 - 17190:00

it probably is helpful to think about

## 17190:00 - 17215:00

but in terms of teaching it it's

## 17215:00 - 17245:00

actually quite quite simple which is

## 17245:00 - 17255:00

powerful.

## 17255:00 - 17260:00

>> Cool.

## 17260:00 - 17300:00

>> So if we go back to here you can see

## 17300:00 - 17335:00

that it's just literally predicting the

## 17335:00 - 17365:00

velocity. Your goal is to have the model

## 17365:00 - 17370:00

predict

## 17370:00 - 17390:00

>> you're minimizing the loss between

## 17390:00 - 17410:00

predictive velocity and velocity

## 17410:00 - 17440:00

>> and the actual velocity. That's it. And

## 17440:00 - 17485:00

that's super stable. Uh and it's it's

## 17485:00 - 17540:00

really clean. And then at test time for

## 17540:00 - 17590:00

the uh physics people this is like a

## 17590:00 - 17620:00

oiler step kind of thing that you're

## 17620:00 - 17650:00

doing where you call the model a bunch

## 17650:00 - 17710:00

of times um and you iteratively refine.

## 17710:00 - 17730:00

So back to the hill climbing that we

## 17730:00 - 17760:00

were talking about. I'll grab some

## 17760:00 - 17855:00

random uh uh noise here x and I just do

## 17855:00 - 17900:00

and I call basically reverse that that

## 17900:00 - 17955:00

um uh uh noising process to d noiseise d

## 17955:00 - 17980:00

noiseise d noiseise and

## 17980:00 - 18000:00

>> it's literally Oiler's method like

## 18000:00 - 18025:00

you're you're using the velocity to

## 18025:00 - 18040:00

point in the direction you want

## 18040:00 - 18055:00

>> point in the direction and just keep

## 18055:00 - 18090:00

going keep going keep going until you've

## 18090:00 - 18125:00

done the number of steps. The one thing

## 18125:00 - 18160:00

that I really don't like about diffusion

## 18160:00 - 18215:00

as it's done today is that I can't keep

## 18215:00 - 18265:00

calling it um beyond if I only trained

## 18265:00 - 18310:00

on 100 uh diffusion steps in my

## 18310:00 - 18340:00

diffusion schedule. If I change that at

## 18340:00 - 18375:00

test time, it doesn't work. And so you

## 18375:00 - 18400:00

can't like, oh, I want it even better,

## 18400:00 - 18430:00

so I'll call it even more. That doesn't

## 18430:00 - 18455:00

you can't I've tried it. It doesn't

## 18455:00 - 18460:00

work.

## 18460:00 - 18480:00

>> Yeah. There's various tricks people try

## 18480:00 - 18490:00

there, but Yeah.

## 18490:00 - 18530:00

>> Yeah. And so like the there's games

## 18530:00 - 18570:00

played that is actually quite exciting.

## 18570:00 - 18590:00

all the expense.

## 18590:00 - 18605:00

>> But wait, sorry, should be clear here.

## 18605:00 - 18630:00

Here you're saying that's not relevant,

## 18630:00 - 18660:00

right? Because these in this type of

## 18660:00 - 18675:00

model, you don't have this time

## 18675:00 - 18690:00

dependency.

## 18690:00 - 18735:00

>> Well, so you do. So at this time, if you

## 18735:00 - 18765:00

change, for example, the number of

## 18765:00 - 18795:00

steps, if you double it, let's say that,

## 18795:00 - 18820:00

and you expect to get even higher

## 18820:00 - 18850:00

resolution images, it actually will just

## 18850:00 - 18880:00

turn into like white. Like it actually

## 18880:00 - 18910:00

just like doesn't work at all. Um, so

## 18910:00 - 18945:00

you can't step beyond number of steps

## 18945:00 - 18965:00

that was trained.

## 18965:00 - 18995:00

>> That's an important detail. Um, there

## 18995:00 - 19025:00

are tricks that people are doing to try

## 19025:00 - 19085:00

to compress that. uh representation. So

## 19085:00 - 19130:00

like if at train time I train for a 100

## 19130:00 - 19160:00

steps and at test time I want to do 10

## 19160:00 - 19195:00

steps then what you can do is you can do

## 19195:00 - 19230:00

distillation into the model to try to

## 19230:00 - 19260:00

have the 10-step model learn the 100

## 19260:00 - 19295:00

step models thing but then you still got

## 19295:00 - 19320:00

to train with 10 steps and so like if

## 19320:00 - 19360:00

you're training with with X steps you

## 19360:00 - 19395:00

have to be using X steps at test time.

## 19395:00 - 19430:00

>> I see interesting. You've talked about

## 19430:00 - 19465:00

this concept of a squint test. Why don't

## 19465:00 - 19490:00

you define the squint test for a second?

## 19490:00 - 19515:00

Tell me a little about where this comes

## 19515:00 - 19550:00

from and then I'd be curious to hear how

## 19550:00 - 19575:00

you think about diffusion models in the

## 19575:00 - 19600:00

context of general intelligence broadly.

## 19600:00 - 19645:00

>> Yan Lakun has this like interesting uh

## 19645:00 - 19680:00

lecture where he talks about um our

## 19680:00 - 19710:00

discovery of flight and that we didn't

## 19710:00 - 19750:00

need uh flapping wings. We kept trying

## 19750:00 - 19795:00

to mimic a bat um and how that was a

## 19795:00 - 19840:00

waste of time. And uh to that I say

## 19840:00 - 19875:00

you're 100% right. However, we did need

## 19875:00 - 19900:00

two wings. you look at the Wright

## 19900:00 - 19935:00

brother's original plane and you squint

## 19935:00 - 19960:00

and you look at a bird, you're just

## 19960:00 - 20005:00

like, hm, while we have helicopters and

## 20005:00 - 20040:00

we have jets and things like that, uh,

## 20040:00 - 20070:00

and rockets, like we we got there

## 20070:00 - 20100:00

eventually. Um, and so there's many

## 20100:00 - 20140:00

elements in the set of things that can

## 20140:00 - 20160:00

achieve flight and they have different

## 20160:00 - 20210:00

pros and cons. Um, and there are many

## 20210:00 - 20235:00

elements in the set of things that can

## 20235:00 - 20265:00

achieve intelligence. We are the only

## 20265:00 - 20320:00

existence proof of it at all. And like

## 20320:00 - 20350:00

I'm sure there will be more elements in

## 20350:00 - 20400:00

the set and maybe LLM's um broadly

## 20400:00 - 20440:00

speaking can get there. But if I squint

## 20440:00 - 20485:00

and I look at LM setup which I I I see

## 20485:00 - 20520:00

this you know monolithic stack

## 20520:00 - 20555:00

transformers the same thing stack stack

## 20555:00 - 20580:00

stacked and there's three stages of

## 20580:00 - 20620:00

training. We do this pre-train uh you

## 20620:00 - 20665:00

know SFT you know post- train and then

## 20665:00 - 20710:00

no learning at at all beyond that. Um

## 20710:00 - 20760:00

and it produces exactly one token at a

## 20760:00 - 20785:00

time, >> right? So iterative token

## 20785:00 - 20805:00

>> iterative token at a time and it never

## 20805:00 - 20845:00

goes backwards. Um and then you look at

## 20845:00 - 20885:00

a brain massively massive amounts of

## 20885:00 - 20910:00

recursion. You have one learning

## 20910:00 - 20935:00

procedure the whole time. You have these

## 20935:00 - 20970:00

two loes that with a corpus colosum

## 20970:00 - 20990:00

between them that's kind of going back

## 20990:00 - 21020:00

and forth like this and we think and

## 21020:00 - 21050:00

then I definitely don't think in one

## 21050:00 - 21075:00

token at a time. When I write code I

## 21075:00 - 21095:00

don't write one little character at a

## 21095:00 - 21125:00

time. I never go backwards and I kind of

## 21125:00 - 21165:00

like am going backwards. I'm recursively

## 21165:00 - 21195:00

uh improving. I'm going backwards again

## 21195:00 - 21225:00

and again. I'm thinking in concepts.

## 21225:00 - 21250:00

>> There's this like dynamic process that's

## 21250:00 - 21285:00

emitting concepts and then higher level

## 21285:00 - 21310:00

higher level concepts and then lower

## 21310:00 - 21330:00

level manifestations of them.

## 21330:00 - 21350:00

>> And I'm sure that may be happening

## 21350:00 - 21380:00

inside the LLM, but it's like it's

## 21380:00 - 21425:00

almost like uh stuck. It can't do more

## 21425:00 - 21455:00

than in one step even though it might

## 21455:00 - 21495:00

want to uh because it has to is the way

## 21495:00 - 21510:00

that we we we trained it,

## 21510:00 - 21530:00

>> right? Like it might have all that in

## 21530:00 - 21565:00

the LLM, but then it's it's sort of

## 21565:00 - 21600:00

bottlenecked ultimately by only its

## 21600:00 - 21620:00

action space is one

## 21620:00 - 21655:00

>> one token at a time. And so I think that

## 21655:00 - 21680:00

that's where I think about diffusion.

## 21680:00 - 21705:00

There's like two main things that

## 21705:00 - 21725:00

diffusion gives me. It doesn't get me

## 21725:00 - 21755:00

all the way to pass my squint test, but

## 21755:00 - 21790:00

it gives me two things that I for sure

## 21790:00 - 21825:00

the brain is doing. Number one, the

## 21825:00 - 21870:00

entire all of biology and nature

## 21870:00 - 21900:00

leverages randomness. Randomness is

## 21900:00 - 21940:00

good. And what is diffusion doing is

## 21940:00 - 21970:00

leveraging randomness. If you give me

## 21970:00 - 22015:00

data and I noise it up and from that I

## 22015:00 - 22050:00

can learn about the data and like is the

## 22050:00 - 22105:00

can the brain add noise to input data?

## 22105:00 - 22145:00

Absolutely. like absolutely like neurons

## 22145:00 - 22175:00

are massively random. Uh this log normal

## 22175:00 - 22205:00

distributions, spike patterns and things

## 22205:00 - 22250:00

like that. Um and the other one is this

## 22250:00 - 22280:00

emission of one thing at a time versus

## 22280:00 - 22315:00

thinking in concepts and then decoding

## 22315:00 - 22365:00

into a big chunk of text and thought and

## 22365:00 - 22395:00

revisioning of the previous thoughts and

## 22395:00 - 22420:00

things like that. And so I think

## 22420:00 - 22445:00

diffusion gives me both of those things

## 22445:00 - 22450:00

for sure.

## 22450:00 - 22480:00

>> People have probably heard of stable

## 22480:00 - 22515:00

diffusion as a very common application

## 22515:00 - 22540:00

of this. people. It's an image

## 22540:00 - 22580:00

generation model that was pretty widely

## 22580:00 - 22625:00

available for the last few years. What

## 22625:00 - 22655:00

people may not be so aware of is all the

## 22655:00 - 22680:00

other ways that diffusion is used in the

## 22680:00 - 22710:00

last few years in products that people

## 22710:00 - 22740:00

are widely using. So what are some of

## 22740:00 - 22770:00

the areas in which diffusion is most

## 22770:00 - 22800:00

widely uh accessible?

## 22800:00 - 22830:00

>> Yeah, it's really any mapping from very

## 22830:00 - 22865:00

highdimensional P data to very

## 22865:00 - 22905:00

highdimensional action spaces or P data

## 22905:00 - 22940:00

uh that you may want to map to. And so I

## 22940:00 - 22970:00

mean yeah of course everyone knows uh

## 22970:00 - 22990:00

generating images because we've done

## 22990:00 - 23030:00

midjourney and things like that uh uh

## 23030:00 - 23060:00

and even more modern versions of that

## 23060:00 - 23120:00

with Sora and VO and Flux and SD3 now

## 23120:00 - 23160:00

and things like that. Um and we've

## 23160:00 - 23195:00

generating videos which is just images

## 23195:00 - 23240:00

stable together um and and videogen and

## 23240:00 - 23265:00

image genen and things like that.

## 23265:00 - 23295:00

However, there's so many more

## 23295:00 - 23315:00

applications that now we're seeing.

## 23315:00 - 23350:00

That's the most exciting part in my my

## 23350:00 - 23380:00

view of all the new applications. And so

## 23380:00 - 23425:00

whether or not you're um now creating

## 23425:00 - 23460:00

sentences, I mean diffusion LLMs was one

## 23460:00 - 23485:00

of the biggest topics that we saw in

## 23485:00 - 23520:00

Europe. Um whether it's continuous uh

## 23520:00 - 23555:00

diffusion LMS or discrete diffusion

## 23555:00 - 23565:00

LLMs.

## 23565:00 - 23625:00

>> Um that's it's writing code now. Um it's

## 23625:00 - 23670:00

creating uh proteins. I mean deep minus

## 23670:00 - 23705:00

won the Nobel Prize for that. There is

## 23705:00 - 23735:00

uh robotic policies this diffusion

## 23735:00 - 23765:00

policy uh uh thing which I think might

## 23765:00 - 23805:00

actually be one of the biggest uh uh uh

## 23805:00 - 23845:00

uses of it and will result in like

## 23845:00 - 23870:00

robotics actually working and rose the

## 23870:00 - 23910:00

robot actually uh working. Um there's

## 23910:00 - 23950:00

weather forecasting for the gencast uh

## 23950:00 - 23985:00

is the most accurate weather forecasting

## 23985:00 - 24015:00

system in the world. Um it's really

## 24015:00 - 24050:00

anything even even like I I I mentioned

## 24050:00 - 24095:00

uh Harrison working on the the diffs

## 24095:00 - 24130:00

diffusion uh for failure sampling just

## 24130:00 - 24165:00

like sampling from for failures and like

## 24165:00 - 24185:00

bad things that could happen. we can do

## 24185:00 - 24200:00

that as well.

## 24200:00 - 24225:00

>> So a lot of the the products where we

## 24225:00 - 24250:00

see people actually using AI especially

## 24250:00 - 24285:00

for things other than just textbased

## 24285:00 - 24315:00

chat a lot of them are using diffusion

## 24315:00 - 24345:00

especially on images, videos

## 24345:00 - 24375:00

increasingly now things like code in the

## 24375:00 - 24405:00

life sciences. So yeah pretty pretty

## 24405:00 - 24435:00

wide birth of things. Yeah, in fact, I

## 24435:00 - 24465:00

would say the only two holdouts right

## 24465:00 - 24495:00

now where state-of-the-art is not

## 24495:00 - 24535:00

diffusion uh diffusion has eaten all of

## 24535:00 - 24580:00

AI except two AR LLMs still are

## 24580:00 - 24635:00

outperforming uh and uh gameplay and

## 24635:00 - 24680:00

things like Alph Go. And so MCTS is

## 24680:00 - 24705:00

still state-of-the-art for those types

## 24705:00 - 24725:00

of things. And so we haven't seen

## 24725:00 - 24750:00

diffusion really take a step in those

## 24750:00 - 24795:00

two fold uh those two areas, but more

## 24795:00 - 24820:00

research is needed. So to bring the

## 24820:00 - 24855:00

conversation to a head now, how should

## 24855:00 - 24895:00

people think about this research area

## 24895:00 - 24925:00

either as researchers contributing to

## 24925:00 - 24955:00

the field or as founders looking to

## 24955:00 - 24980:00

build a new product?

## 24980:00 - 25010:00

>> Yeah, I mean I would think about maybe

## 25010:00 - 25040:00

there's falls in two camps. If you're

## 25040:00 - 25085:00

training models yourself um or if you're

## 25085:00 - 25140:00

using models and and you know not in the

## 25140:00 - 25165:00

business of training models, if you're

## 25165:00 - 25185:00

in the business of training models, I

## 25185:00 - 25210:00

would seriously look at diffusion. I

## 25210:00 - 25235:00

don't care what your application is. You

## 25235:00 - 25265:00

should be looking at this procedure. uh

## 25265:00 - 25320:00

even if it's just to get a latent space

## 25320:00 - 25365:00

that you can then train off of. And so

## 25365:00 - 25400:00

there's no application in machine

## 25400:00 - 25420:00

learning that I I don't think you should

## 25420:00 - 25445:00

be heavily looking at diffusion

## 25445:00 - 25495:00

procedures um as a fundamental piece of

## 25495:00 - 25540:00

of your training loop. Um in the in the

## 25540:00 - 25570:00

case of people who are are not training

## 25570:00 - 25625:00

models, I would just like update your

## 25625:00 - 25655:00

prior on how good these things are

## 25655:00 - 25690:00

getting. And if you just look at in the

## 25690:00 - 25725:00

last 5 years on how good image

## 25725:00 - 25770:00

generation got from midjourney when we

## 25770:00 - 25820:00

first came out to VO and Sora and Flux

## 25820:00 - 25875:00

and SD3 now it's like it's like thousand

## 25875:00 - 25900:00

times better right the answer was just

## 25900:00 - 25930:00

scale it up and that takes time and that

## 25930:00 - 25955:00

takes money and all those things and

## 25955:00 - 26005:00

data and now you apply that to proteins

## 26005:00 - 26045:00

you apply that to DNA you apply that to

## 26045:00 - 26090:00

robotics policies a self-driving car I

## 26090:00 - 26125:00

mean it is um skate to where the puck's

## 26125:00 - 26145:00

going to go all these things are going

## 26145:00 - 26175:00

to work and we're we're watching it

## 26175:00 - 26220:00

happen. It may cost money and time and

## 26220:00 - 26250:00

you know those kinds of things but those

## 26250:00 - 26275:00

are those are solvable things. Those are

## 26275:00 - 26310:00

tractable problems that we can go solve.

## 26310:00 - 26345:00

Um and also the the core procedure of

## 26345:00 - 26365:00

diffusion is getting better. That's

## 26365:00 - 26410:00

another major simpler a lot simpler and

## 26410:00 - 26435:00

it's getting like it's just working

## 26435:00 - 26465:00

better and so skates where the puck's

## 26465:00 - 26505:00

going to go. Bet that rose to the robot

## 26505:00 - 26545:00

will work in people's homes. bet that

## 26545:00 - 26580:00

the the protein folding is only going to

## 26580:00 - 26600:00

get better and now we're going to apply

## 26600:00 - 26630:00

that to DNA and all these other uh

## 26630:00 - 26650:00

metabolomics and things like that.

## 26650:00 - 26680:00

>> We we see founders develop new models

## 26680:00 - 26730:00

for robotics or for text generation or

## 26730:00 - 26775:00

for video using diffusion. Um and we see

## 26775:00 - 26805:00

founders who are using all these methods

## 26805:00 - 26825:00

coming from other places build companies

## 26825:00 - 26850:00

on top of them and it seems like there's

## 26850:00 - 26875:00

this whole new wave of companies that

## 26875:00 - 26900:00

can be built on either end of this now

## 26900:00 - 26920:00

>> right I think it's going to redefine the

## 26920:00 - 26930:00

entire economy.

## 26930:00 - 26955:00

>> Thanks so much for joining us. We're

## 26955:00 - 26980:00

going to keep digging in on topics

## 26980:00 - 27005:00

related to machine learning research

## 27005:00 - 27030:00

like diffusion. Can't wait to see you at

## 27030:00 - 27060:00

the next one.

## 27060:00+

[music]

