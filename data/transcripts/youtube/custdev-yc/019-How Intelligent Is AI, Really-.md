---
source: https://www.youtube.com/watch?v=pBlIgs6w7Ss
title: How Intelligent Is AI, Really?
author: Y Combinator
date: 2025-12-17
views: 13336
description: >-
  ARC-AGI is redefining how to measure progress on the path to AGI - focusing on
  reasoning, generalization, and adaptability instead of memorization or scale.
  During this month's NeurIPS 2025 conference, YC's Diana Hu sat down with ARC
  Prize Foundation President Greg Kamradt to find out why most AI benchmarks
  fail, how ARC-AGI reveals the limits of today’s models, and why measuring
  intelligence may be harder than building it.


  Apply to Y Combinator: https://www.ycombinator.com/apply


  Chapters: 

  00:11 — What ARC Prize is and why it exists

  00:38 — François Chollet’s definition of AGI

  01:48 — What ARC-AGI Actually Tests

  02:25 — When LLMs Failed the ARC Benchmark

  02:44 — The Reasoning Breakthrough

  03:38 — ARC-AGI Becomes the Standard

  04:20 — Vanity Metrics

  04:49 — False Positives in AI Progress

  06:06 — The Evolution of ARC-AGI

  07:05 — Inside ARC-AGI v3

  08:55 — Measuring Intelligence beyond just accuracy

  10:25 — What happens if a model solves ARC-AGI?
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:39:27.913Z
---

# How Intelligent Is AI, Really?

## 00:00 - 240:00

I'm excited today to welcome Greg Camrad

## 240:00 - 280:00

who is the president of the Ark Prize.

## 280:00 - 290:00

>> That's right.

## 290:00 - 335:00

>> Thanks for coming here at Europe's 2025

## 335:00 - 355:00

in beautiful San Diego.

## 355:00 - 370:00

>> Thank you, Diana.

## 370:00 - 410:00

>> So, what does the Art Prize Foundation

## 410:00 - 425:00

do?

## 425:00 - 455:00

>> Yes. So the ARP price foundation is a

## 455:00 - 485:00

nonprofit and but it's a little bit of a

## 485:00 - 515:00

different nonprofit because we are very

## 515:00 - 555:00

tech forward and so our mission is to

## 555:00 - 600:00

pull forward open progress towards

## 600:00 - 625:00

systems that can generalize just like

## 625:00 - 635:00

humans.

## 635:00 - 685:00

>> So according to Franachal he defines

## 685:00 - 725:00

intelligence as the ability to learn new

## 725:00 - 770:00

things a lot more efficiently.

## 770:00 - 805:00

What does that mean for founders as they

## 805:00 - 835:00

look at all these benchmarks for all

## 835:00 - 870:00

these model releases that are chasing

## 870:00 - 910:00

MLU bench numbers?

## 910:00 - 935:00

>> Yes, absolutely. Well, so one of the

## 935:00 - 965:00

cool things about ARP prize is we have a

## 965:00 - 1000:00

very opinionated definition of

## 1000:00 - 1020:00

intelligence. And this came from

## 1020:00 - 1070:00

France's paper in 2019 on the measure of

## 1070:00 - 1105:00

intelligence. And in there, you would

## 1105:00 - 1130:00

normally think that intelligence would

## 1130:00 - 1165:00

be how much can you score on the SAT

## 1165:00 - 1210:00

test or how hard of math problems can

## 1210:00 - 1240:00

you do? And he actually proposed an

## 1240:00 - 1265:00

alternative theory, which is the

## 1265:00 - 1295:00

foundation for what Arc Prize does. And

## 1295:00 - 1330:00

he actually defined intelligence as your

## 1330:00 - 1390:00

ability to learn new things. So, we

## 1390:00 - 1415:00

already know that AI is really good at

## 1415:00 - 1445:00

chess. It's superhuman. We know that AI

## 1445:00 - 1465:00

is really good at go. It's super human.

## 1465:00 - 1480:00

We know that it's really good at

## 1480:00 - 1510:00

self-driving. But getting those same

## 1510:00 - 1545:00

systems to learn something else, a

## 1545:00 - 1580:00

different skill, that is actually the

## 1580:00 - 1635:00

hard part. And so, um, Franis alongside

## 1635:00 - 1670:00

that proposal of his definition of

## 1670:00 - 1700:00

intelligence, he says, well, I don't

## 1700:00 - 1730:00

just have a definition. I also have a

## 1730:00 - 1765:00

benchmark or a test that tests whether

## 1765:00 - 1805:00

or not you can learn new things. because

## 1805:00 - 1825:00

generally people are going to learn new

## 1825:00 - 1850:00

things over a long horizon, couple

## 1850:00 - 1875:00

hours, couple days or maybe over a

## 1875:00 - 1905:00

lifetime. But he proposed a test called

## 1905:00 - 1940:00

the ARC AGI or at the time it was just

## 1940:00 - 1990:00

called the ARC benchmark. And in it, he

## 1990:00 - 2025:00

tests your ability to learn new things.

## 2025:00 - 2065:00

So what's really cool is that not only

## 2065:00 - 2105:00

humans can take this test, but also

## 2105:00 - 2135:00

machines can take this test too. So

## 2135:00 - 2160:00

whereas other benchmarks, they might try

## 2160:00 - 2205:00

to do what I call PhD++ problems harder

## 2205:00 - 2245:00

and harder. So we had MMLU, we had an

## 2245:00 - 2285:00

MMLU plus, and now we have humanities

## 2285:00 - 2310:00

last exam. Those are going super human,

## 2310:00 - 2360:00

right? Arc benchmarks, normal people can

## 2360:00 - 2380:00

do these. And so we actually test all of

## 2380:00 - 2400:00

our benchmarks to make sure that um

## 2400:00 - 2425:00

normal people can do them.

## 2425:00 - 2445:00

>> And just a bit of context for the

## 2445:00 - 2500:00

audience, this particular price was

## 2500:00 - 2565:00

famously one that a lot of uh LLMs with

## 2565:00 - 2630:00

just pre-training before uh ARL came in

## 2630:00 - 2680:00

in the picture before 2024.

## 2680:00 - 2715:00

>> All these large models, language models

## 2715:00 - 2740:00

were doing terribly, right?

## 2740:00 - 2770:00

>> Yes. Absolutely doing terribly. You

## 2770:00 - 2805:00

know, it's kind of weird, but nowadays

## 2805:00 - 2850:00

it's hard to come up with problems to to

## 2850:00 - 2885:00

stump AI. You know, back in 2012 with

## 2885:00 - 2910:00

ImageNet, all all you needed to do was

## 2910:00 - 2950:00

just show people an image of a cat and

## 2950:00 - 2975:00

you could stump the computer. But when

## 2975:00 - 3005:00

France came out with his benchmark in

## 3005:00 - 3090:00

2019, fast forward all the way to 2024,

## 3090:00 - 3125:00

I think at the time it was GPT4, the

## 3125:00 - 3145:00

base model, no reasoning, I think it was

## 3145:00 - 3190:00

getting 4%. Four or 5%. So clearly

## 3190:00 - 3220:00

showed, hey, humans can do this, but

## 3220:00 - 3250:00

base models are not doing anything. And

## 3250:00 - 3280:00

what's really cool actually is right at

## 3280:00 - 3315:00

01 I remember testing 01 and 01 preview

## 3315:00 - 3335:00

right when that first came out I think

## 3335:00 - 3375:00

performance jumped up to 21%. So you

## 3375:00 - 3400:00

look at that and after 5 years those

## 3400:00 - 3435:00

only 4% and then in such a short time it

## 3435:00 - 3470:00

goes to 21. That tells you something

## 3470:00 - 3495:00

really interesting is going on. So

## 3495:00 - 3535:00

actually we used ARC to identify that

## 3535:00 - 3570:00

reasoning paradigm was huge that was

## 3570:00 - 3600:00

actually transformational for for what

## 3600:00 - 3625:00

was contributing towards towards AI at

## 3625:00 - 3670:00

the time. So much so that now all the

## 3670:00 - 3730:00

big labs XAI, OpenAI are actually now

## 3730:00 - 3775:00

using ArcGI as part of their model

## 3775:00 - 3800:00

releases and the numbers that they're

## 3800:00 - 3835:00

hitting. So it's become the standard

## 3835:00 - 3850:00

now.

## 3850:00 - 3885:00

>> Yeah. Well, I I tell you what um we're

## 3885:00 - 3915:00

excited that the community is

## 3915:00 - 3945:00

recognizing that ArcJI can tell you

## 3945:00 - 3960:00

something. That's that's what we're

## 3960:00 - 3990:00

excited about. And when public labs or

## 3990:00 - 4020:00

Frontier Labs like to use us in terms of

## 4020:00 - 4050:00

reporting their performance, it's really

## 4050:00 - 4085:00

awesome that they too say, "Yes, we just

## 4085:00 - 4105:00

came out with this Frontier model. This

## 4105:00 - 4125:00

is how we choose to measure our

## 4125:00 - 4145:00

performance." And so in the past 12

## 4145:00 - 4170:00

months, you're right, we've had OpenAI,

## 4170:00 - 4200:00

we've had XAI with Gro 4, we've had

## 4200:00 - 4240:00

Gemini with Gemini 3 Pro and Deepthink,

## 4240:00 - 4270:00

and then just recently Anthropic with um

## 4270:00 - 4295:00

Opus 45.

## 4295:00 - 4320:00

>> That's cool. So what's going well with

## 4320:00 - 4335:00

all these releases?

## 4335:00 - 4360:00

>> So it's it's going really well that

## 4360:00 - 4405:00

they're adopting it. Um, however, we're

## 4405:00 - 4430:00

mindful of vanity metrics that come from

## 4430:00 - 4465:00

there, too. So just because they use us

## 4465:00 - 4505:00

doesn't necessarily um mean that our

## 4505:00 - 4535:00

mission is done or our job is done or

## 4535:00 - 4555:00

what we're trying to do here. Because

## 4555:00 - 4575:00

again if we go back to the mission of

## 4575:00 - 4620:00

ARP prize is to pull forward open AGI

## 4620:00 - 4645:00

progress. So we want to inspire

## 4645:00 - 4670:00

researchers, small teams, individual

## 4670:00 - 4730:00

researchers and having big labs um give

## 4730:00 - 4770:00

an endorsement more or less is really

## 4770:00 - 4795:00

good for that mission but it's it's also

## 4795:00 - 4830:00

secondary to the overall mission. So now

## 4830:00 - 4860:00

that you've seen also lots of teams

## 4860:00 - 4940:00

trying to ship AI products, what are

## 4940:00 - 4980:00

most common false positives that you

## 4980:00 - 5020:00

observe? Things that feel like progress

## 5020:00 - 5045:00

but aren't quite progress because it's

## 5045:00 - 5085:00

easy to perhaps just hit a benchmark

## 5085:00 - 5110:00

somewhere and call it done.

## 5110:00 - 5115:00

>> Sure.

## 5115:00 - 5140:00

>> But it doesn't quite work.

## 5140:00 - 5175:00

>> Yeah. So when I answer that question, I

## 5175:00 - 5220:00

put on my almost researcher hat because

## 5220:00 - 5245:00

there's two hats that are very prominent

## 5245:00 - 5265:00

within AI right now. There's

## 5265:00 - 5290:00

economically valuable like you know

## 5290:00 - 5315:00

we're going to go monetize this product

## 5315:00 - 5365:00

hat and then there's going to be the um

## 5365:00 - 5400:00

call it romantic pursuit of general

## 5400:00 - 5425:00

intelligence hat and I I'm wearing the

## 5425:00 - 5450:00

latter hat. So one thing that stands out

## 5450:00 - 5480:00

to me is of course is everybody talks

## 5480:00 - 5510:00

about it but all all the RL environments

## 5510:00 - 5540:00

and there's been famous AI researchers

## 5540:00 - 5565:00

that have said hey as long as we can

## 5565:00 - 5610:00

make an RL environment we can score well

## 5610:00 - 5630:00

on this benchmark or this domain or

## 5630:00 - 5670:00

whatever it may be. Um to me that's kind

## 5670:00 - 5690:00

of like whack-a-ole. You know you're not

## 5690:00 - 5710:00

going to be able to make RL environments

## 5710:00 - 5725:00

for every single thing you're going to

## 5725:00 - 5780:00

end up wanting to do. And core to RGI is

## 5780:00 - 5805:00

novelty and novel problems that end up

## 5805:00 - 5830:00

coming in the future, which is one of

## 5830:00 - 5850:00

the reasons why we have a hidden test

## 5850:00 - 5895:00

set by the way. So I think while that's

## 5895:00 - 5915:00

cool and while you're going to get

## 5915:00 - 5940:00

short-term gains from it, I would rather

## 5940:00 - 5965:00

see investment into systems that are

## 5965:00 - 5990:00

actually generalizing and you don't need

## 5990:00 - 6020:00

the environment for it because if you

## 6020:00 - 6055:00

see or if you um compare it to humans,

## 6055:00 - 6080:00

humans don't need the environment to go

## 6080:00 - 6100:00

and train on that.

## 6100:00 - 6125:00

>> Perhaps walk us through a bit of the

## 6125:00 - 6165:00

history of uh ArcGI version. So it was

## 6165:00 - 6215:00

Argia 1, two, and three is coming up

## 6215:00 - 6225:00

soon.

## 6225:00 - 6270:00

>> Yes. which is a whole new thing with

## 6270:00 - 6305:00

gamelike environments and interactive.

## 6305:00 - 6325:00

So walk us through the history and then

## 6325:00 - 6345:00

tell us what

## 6345:00 - 6365:00

>> three is all about.

## 6365:00 - 6400:00

>> Yes, absolutely. So RKGI1 came out in

## 6400:00 - 6450:00

2019. That was France proposed it. I

## 6450:00 - 6485:00

think he made all 800 tasks himself

## 6485:00 - 6525:00

within it which is a huge feat in in and

## 6525:00 - 6550:00

of itself. Um and that came with this

## 6550:00 - 6575:00

paper on the measure of intelligence.

## 6575:00 - 6610:00

Now in 2025

## 6610:00 - 6635:00

just this year earlier in March of this

## 6635:00 - 6675:00

year we came with ARC AGI 2. And so

## 6675:00 - 6705:00

think of that as a deeper version or an

## 6705:00 - 6750:00

upgraded version of RKGI1. Now what's

## 6750:00 - 6780:00

interesting is those two are both static

## 6780:00 - 6805:00

benchmarks or you know call it

## 6805:00 - 6845:00

metastatic benchmarks. We're coming out

## 6845:00 - 6890:00

with RGI 3 next year. And the big

## 6890:00 - 6925:00

difference with RKGI3 is it's going to

## 6925:00 - 6960:00

be interactive. So if you think about

## 6960:00 - 6985:00

reality and the in the world that we all

## 6985:00 - 7015:00

live in, we are constantly making an

## 7015:00 - 7055:00

action, getting feedback and kind of um

## 7055:00 - 7070:00

going back and forth with our

## 7070:00 - 7110:00

environment. And it is in my belief that

## 7110:00 - 7145:00

future AGI will be declared with an

## 7145:00 - 7170:00

interactive benchmark because that is

## 7170:00 - 7225:00

really what reality is. And so um V3 is

## 7225:00 - 7280:00

going to be about 150 video game

## 7280:00 - 7315:00

environments. Now we say video game

## 7315:00 - 7330:00

because that's an easy way to

## 7330:00 - 7345:00

communicate it, but really it's an

## 7345:00 - 7390:00

environment where you give an action and

## 7390:00 - 7430:00

then you get some response. Now, the

## 7430:00 - 7445:00

really cool part and one of the thing

## 7445:00 - 7485:00

that jazzes me up about V3 the most is

## 7485:00 - 7525:00

we're not going to give any instructions

## 7525:00 - 7570:00

to the test taker on how to complete the

## 7570:00 - 7600:00

environment. So, there's no English,

## 7600:00 - 7625:00

there's no words, there's no symbols or

## 7625:00 - 7650:00

anything like that. And in order to beat

## 7650:00 - 7690:00

the benchmark, you need to go in, you

## 7690:00 - 7720:00

need to take a few actions and see how

## 7720:00 - 7745:00

your environment responds and try to

## 7745:00 - 7765:00

figure out what the ultimate goal is in

## 7765:00 - 7780:00

the first place.

## 7780:00 - 7805:00

>> I tried a bunch of those uh games. They

## 7805:00 - 7815:00

were actually fun.

## 7815:00 - 7850:00

>> Yeah, they're cool. And much like Ark 1

## 7850:00 - 7880:00

and Ark 2, we're testing humans on every

## 7880:00 - 7945:00

single V3 game. So, we will recruit

## 7945:00 - 7970:00

members of the general public, so

## 7970:00 - 8000:00

accountants, Uber drivers, you know,

## 8000:00 - 8025:00

that type of thing. We'll put 10 people

## 8025:00 - 8060:00

in front of each game, and if each game

## 8060:00 - 8095:00

does not pass a minimum solvability

## 8095:00 - 8135:00

threshold by regular humans, then we're

## 8135:00 - 8165:00

going to exclude it. Now, again, I just

## 8165:00 - 8185:00

have to emphasize, but that's in

## 8185:00 - 8215:00

contrast to other benchmarks where you

## 8215:00 - 8245:00

try to go harder and harder and harder

## 8245:00 - 8290:00

questions. But the fact that ARK 3 will

## 8290:00 - 8330:00

be out there and regular people can do

## 8330:00 - 8385:00

it but AI cannot do it tells you well

## 8385:00 - 8410:00

there's something missing still. There's

## 8410:00 - 8430:00

something clearly missing that we need

## 8430:00 - 8470:00

to um need new ideas for research on.

## 8470:00 - 8505:00

>> So there's this big theme in terms of

## 8505:00 - 8540:00

measuring intelligence with human

## 8540:00 - 8555:00

capabilities.

## 8555:00 - 8565:00

>> Yes.

## 8565:00 - 8615:00

>> So there's this growing idea that

## 8615:00 - 8650:00

accuracy is not the only metric that

## 8650:00 - 8675:00

matters to models.

## 8675:00 - 8725:00

>> Yes. but also the time and amount of

## 8725:00 - 8760:00

data that it takes to acquire new skills

## 8760:00 - 8800:00

which is what this whole spirit of our

## 8800:00 - 8815:00

AGI is.

## 8815:00 - 8825:00

>> Yes.

## 8825:00 - 8865:00

>> So I guess the question is how close are

## 8865:00 - 8925:00

we to evaluating models in human time?

## 8925:00 - 8975:00

>> Yes. So with regards to human time, we

## 8975:00 - 9000:00

actually see time as a little bit

## 9000:00 - 9020:00

arbitrary because if you throw more

## 9020:00 - 9035:00

compute at something, you're going to

## 9035:00 - 9070:00

reduce the time no matter what. So it

## 9070:00 - 9095:00

it's it's almost just a decision on how

## 9095:00 - 9110:00

much compute do you want, which is how

## 9110:00 - 9130:00

much time it's going to take, which

## 9130:00 - 9170:00

tells you that wall clock may not be the

## 9170:00 - 9185:00

important part for what we have

## 9185:00 - 9225:00

intelligence here. But there's two other

## 9225:00 - 9255:00

factors that go into the equation of

## 9255:00 - 9280:00

intelligence. Number one is going to be

## 9280:00 - 9305:00

the amount of training data that you

## 9305:00 - 9330:00

need, which is exactly what you said.

## 9330:00 - 9355:00

And then number two is actually the

## 9355:00 - 9395:00

amount of energy that you need in order

## 9395:00 - 9425:00

to execute upon that intelligence. And

## 9425:00 - 9450:00

the reason why those are so fascinating

## 9450:00 - 9485:00

is because we have benchmarks for humans

## 9485:00 - 9515:00

on both of those. So we know how many

## 9515:00 - 9545:00

data points a human needs in order to

## 9545:00 - 9590:00

execute a task and we know how much

## 9590:00 - 9630:00

energy the human brain consumes to

## 9630:00 - 9670:00

execute a task. So with RKGI3, the way

## 9670:00 - 9685:00

that we're actually going to be

## 9685:00 - 9720:00

measuring efficiency, not just by

## 9720:00 - 9745:00

accuracy,

## 9745:00 - 9770:00

I I told you they're video games and

## 9770:00 - 9795:00

they're turn-based video games. And so

## 9795:00 - 9820:00

you click, you might click up, left,

## 9820:00 - 9855:00

right, down, or something like that. And

## 9855:00 - 9880:00

we're going to count the number of

## 9880:00 - 9925:00

actions that it takes a human to beat

## 9925:00 - 9950:00

the game. and we're going to compare

## 9950:00 - 9975:00

that to the number of actions that it

## 9975:00 - 10025:00

takes in AI to beat the game. So, back

## 10025:00 - 10075:00

in the old um Atari days in 2016 when

## 10075:00 - 10100:00

they were making a run at video games,

## 10100:00 - 10120:00

then they would use brute force

## 10120:00 - 10150:00

solutions and they would need millions

## 10150:00 - 10180:00

and billions of frames of video game and

## 10180:00 - 10205:00

they would need millions of actions to

## 10205:00 - 10225:00

basically spam and brute force the

## 10225:00 - 10260:00

space. Um, we're not going to let you do

## 10260:00 - 10295:00

that on ARI 3 and so we're basically

## 10295:00 - 10335:00

going to normalize AI performance to the

## 10335:00 - 10375:00

average human performance that we see.

## 10375:00 - 10385:00

>> That's very cool.

## 10385:00 - 10395:00

>> Yes.

## 10395:00 - 10415:00

>> My last question.

## 10415:00 - 10480:00

>> Yes. Let's um wave a magic wand and then

## 10480:00 - 10530:00

there's a super amazing team that

## 10530:00 - 10570:00

suddenly tomorrow res launches a model

## 10570:00 - 10630:00

that scores 100% in the arc AGI

## 10630:00 - 10670:00

>> benchmarks.

## 10670:00 - 10695:00

What should the world update about the

## 10695:00 - 10725:00

priors of what AGI is?

## 10725:00 - 10735:00

>> Yeah,

## 10735:00 - 10760:00

>> how would the world change?

## 10760:00 - 10790:00

>> Well, it's it's funny you ask that. Um

## 10790:00 - 10825:00

the what AGI is question is such a deep

## 10825:00 - 10865:00

topic that we can go much deeper on. So

## 10865:00 - 10890:00

um from the beginning Franuis has always

## 10890:00 - 10935:00

said that the thing that solves arc AGI

## 10935:00 - 10975:00

is necessary for AGI it's not

## 10975:00 - 11025:00

sufficient. So what that means is um it

## 11025:00 - 11070:00

the thing that solves arc AGI 1 and two

## 11070:00 - 11105:00

will not be AGI but will it will be an

## 11105:00 - 11135:00

authoritative source of generalization.

## 11135:00 - 11190:00

Now our claim for V3 is that it no the

## 11190:00 - 11240:00

thing that beats it won't be AGI however

## 11240:00 - 11275:00

it will be the most authoritative

## 11275:00 - 11310:00

evidence that we have to date about a

## 11310:00 - 11345:00

system that can generalize. If a team

## 11345:00 - 11365:00

were to come out and be at it tomorrow,

## 11365:00 - 11390:00

we would of course want to analyze that

## 11390:00 - 11425:00

system, figure out where still are the

## 11425:00 - 11450:00

failure points that come from that. And

## 11450:00 - 11480:00

like any good benchmark creator, we want

## 11480:00 - 11505:00

to continue to guide um the world

## 11505:00 - 11530:00

towards what we believe to be proper

## 11530:00 - 11580:00

AGI. But ultimately um ARP, we want to

## 11580:00 - 11605:00

put ourselves in a position when we can

## 11605:00 - 11635:00

fully understand and be ready to declare

## 11635:00 - 11670:00

when we do actually have AGI. So if that

## 11670:00 - 11695:00

team were to do it tomorrow, we'd want

## 11695:00 - 11720:00

to have a conversation with them. We'll

## 11720:00 - 11735:00

put it that way.

## 11735:00 - 11760:00

>> That's a good way to wrap. Thank you so

## 11760:00 - 11775:00

much for coming and chatting with us,

## 11775:00 - 11780:00

Greg.

## 11780:00+

>> Thank you, Diana.

