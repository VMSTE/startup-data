---
source: https://www.youtube.com/watch?v=5QcCeSsNRks
title: "François Chollet: How We Get To AGI"
author: Y Combinator
date: 2025-07-03
views: 137038
description: >-
  François Chollet on June 16, 2025 at AI Startup School in San Francisco.


  François Chollet is a leading voice in AI. He's the creator of the Keras
  library, author of Deep Learning with Python, and the founder of the ARC
  Prize, a global competition aimed at measuring true general intelligence.


  He's spent years thinking deeply about what intelligence actually is, and why
  scaling up today’s AI models isn’t enough to reach it.


  In this talk, he walks through the limits of pretraining and memorized skills,
  and lays out a path toward true general intelligence— AI that can adapt on the
  fly, reason in new situations, and invent novel solutions. He explains why
  abstraction and compositionality matter, how ARC became the benchmark for
  progress, and what his team at a new research lab called Ndea is building
  next.


  Apply to Y Combinator: https://ycombinator.com/apply

  Work at a startup: https://workatastartup.com


  Chapters:

  00:00 - The Falling Cost of Compute

  00:57 - Deep-Learning’s Scaling Era & Benchmarks

  01:59 - The ARC Benchmark

  03:02 - The 2024 Shift to Test-Time Adaptation

  05:01 - What Is Intelligence?

  07:12 - Why Benchmarks Matter (and Mislead)

  08:57 - ARC 1 Exposes Scaling Limits

  10:58 - ARC 2: Compositional Reasoning Arrives

  12:55 - Humans vs. Models on ARC 2

  14:58 - Previewing ARC 3 & Interactive Agency

  17:00 - Kaleidoscopic Hypothesis and Abstractions

  22:00 - Type 1 vs. Type 2 Abstractions

  26:00 - Discrete Program Search & Inventive AI

  29:00 - Fusing Intuition with Symbolic Reasoning

  32:00 - Building AGI Through Meta-Learning Systems

  33:44 - NDEA: a new AI research lab
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:44:28.668Z
---

# François Chollet: How We Get To AGI

## 00:00 - 60:00

Hi everyone, I'm Francois. I'm super

## 60:00 - 90:00

excited to share with you some of my

## 90:00 - 130:00

ideas about HGI and how we're going to

## 130:00 - 170:00

get there. This chart right there is one

## 170:00 - 200:00

of the most important facts about the

## 200:00 - 240:00

world. The cost of compute has been

## 240:00 - 275:00

consistently falling by two orders of

## 275:00 - 325:00

magnitude every decade since 1940.

## 325:00 - 355:00

There's no sign that is stopping anytime

## 355:00 - 410:00

soon. And in AI, compute and data have

## 410:00 - 445:00

long been the primary bottleneck to what

## 445:00 - 495:00

we could achieve. And in 2010s, as you

## 495:00 - 535:00

all know, with the abundance of GPU

## 535:00 - 580:00

based compute and large data sets, deep

## 580:00 - 615:00

learning really started to work. And all

## 615:00 - 665:00

of a sudden, we are making fast progress

## 665:00 - 695:00

on problems that had long seemed

## 695:00 - 740:00

intractable across computer vision and

## 740:00 - 770:00

natural language processing. And in

## 770:00 - 800:00

particular, self-supervised text

## 800:00 - 840:00

modeling started to work. And the

## 840:00 - 895:00

dominant paradigm of AI became scaling

## 895:00 - 945:00

up LM3 training. And this approach was

## 945:00 - 1000:00

crushing almost all benchmarks and

## 1000:00 - 1035:00

remarkably it was getting predictably

## 1035:00 - 1085:00

better benchmark results as we scaled up

## 1085:00 - 1130:00

model size and train data size with the

## 1130:00 - 1160:00

exact same architecture and the exact

## 1160:00 - 1195:00

same training process. That's the

## 1195:00 - 1245:00

scaling laws that Jared told you about a

## 1245:00 - 1275:00

few minutes ago. So it really seemed

## 1275:00 - 1315:00

like really it all figured out and many

## 1315:00 - 1365:00

people extrapolated that more scale uh

## 1365:00 - 1405:00

was all that was needed to solve

## 1405:00 - 1450:00

everything and get to a GI. Our field

## 1450:00 - 1505:00

became obsessed with the idea that

## 1505:00 - 1535:00

general intelligence would spontaneously

## 1535:00 - 1580:00

emerge by cramming more and more data

## 1580:00 - 1630:00

into bigger and bigger models. But there

## 1630:00 - 1675:00

was one problem. We were confused about

## 1675:00 - 1720:00

what these benchmarks really meant.

## 1720:00 - 1760:00

There's a big difference between

## 1760:00 - 1800:00

memorized skills which are static and

## 1800:00 - 1835:00

task specific and fluid general

## 1835:00 - 1875:00

intelligence the ability to understand

## 1875:00 - 1910:00

something you've never seen before on

## 1910:00 - 1975:00

the fly. And back in 2019 before the

## 1975:00 - 2030:00

rise of LLMs I released an AI benchmark

## 2030:00 - 2075:00

to highlight this difference. Uh it's

## 2075:00 - 2110:00

called the abstraction reasoning corpus

## 2110:00 - 2155:00

or ark1.

## 2155:00 - 2215:00

And from uh at that time back in 2019 to

## 2215:00 - 2285:00

now with a model like GP4.5 for instance

## 2285:00 - 2345:00

there's been a roughly 50,000x scale up

## 2345:00 - 2415:00

of basel and we went from 0% accuracy on

## 2415:00 - 2475:00

that benchmark to roughly 10%. Which is

## 2475:00 - 2510:00

not a lot. It's very close to zero if

## 2510:00 - 2540:00

you take into account the fact that any

## 2540:00 - 2570:00

one of you in this room would score well

## 2570:00 - 2605:00

above 95%.

## 2605:00 - 2655:00

So to crack general fluid intelligence,

## 2655:00 - 2710:00

it turns out we needed new ideas beyond

## 2710:00 - 2745:00

just scaling up pre-training and doing

## 2745:00 - 2795:00

static inference. This benchmark was not

## 2795:00 - 2845:00

about uh regurgitating memorized skills.

## 2845:00 - 2880:00

It was really about making sense of a

## 2880:00 - 2910:00

new problem that you've never seen

## 2910:00 - 2965:00

before on the fly. But then last year in

## 2965:00 - 3010:00

2024, everything changed. the AI

## 3010:00 - 3050:00

research community started pivoting to a

## 3050:00 - 3100:00

new and very different pattern test

## 3100:00 - 3140:00

adaptation creating models that could

## 3140:00 - 3175:00

change their own state at test time to

## 3175:00 - 3215:00

adapt to something new. So this wasn't

## 3215:00 - 3240:00

about quering pre-loaded knowledge

## 3240:00 - 3285:00

anymore. It was really about the ability

## 3285:00 - 3330:00

to learn and adapt at inference time and

## 3330:00 - 3370:00

suddenly we started seeing significant

## 3370:00 - 3415:00

progress on ARC. So finally we had AI

## 3415:00 - 3455:00

that was showing genuine signs of fluid

## 3455:00 - 3485:00

intelligence. So in particular in

## 3485:00 - 3535:00

December last year, OpenAI previewed its

## 3535:00 - 3590:00

uh 03 model and they used a version of

## 3590:00 - 3625:00

it that was uh fine-tuned specifically

## 3625:00 - 3665:00

on ARC and that showed human level

## 3665:00 - 3700:00

performance on that benchmark to the

## 3700:00 - 3755:00

first time and today in 2025 we have

## 3755:00 - 3795:00

suddenly moved on from the pre-training

## 3795:00 - 3830:00

scaling pattern and we're now fully in

## 3830:00 - 3875:00

the era of Tesla adaptation. So Tesla

## 3875:00 - 3920:00

adaptation is all about the ability of a

## 3920:00 - 3960:00

model to modify its own behavior

## 3960:00 - 4000:00

dynamically based on the specific data

## 4000:00 - 4045:00

it encounters during inference. So that

## 4045:00 - 4085:00

covers techniques like test time

## 4085:00 - 4125:00

training, program synthesis, train of

## 4125:00 - 4165:00

thought synthesis where the model tries

## 4165:00 - 4210:00

to reprogram itself uh for the task at

## 4210:00 - 4270:00

hand. And today every single AI approach

## 4270:00 - 4305:00

that performs well on ARC is using one

## 4305:00 - 4350:00

of these techniques. So today I want to

## 4350:00 - 4400:00

answer the following questions. First,

## 4400:00 - 4425:00

why did the pre-training scaling

## 4425:00 - 4485:00

paradigm not get us to a GI? If you look

## 4485:00 - 4530:00

back just two years ago, this was the

## 4530:00 - 4560:00

standard dogma. Everybody was saying

## 4560:00 - 4600:00

this and today almost no one believes

## 4600:00 - 4645:00

this anymore. So what happened? And

## 4645:00 - 4700:00

next, does this adaptation get us to AGI

## 4700:00 - 4740:00

this time? And if that's the case, maybe

## 4740:00 - 4790:00

AGI is already here. Some people believe

## 4790:00 - 4855:00

so. And finally, besides uh the sign

## 4855:00 - 4895:00

adaptation, what else might be next for

## 4895:00 - 4920:00

AI?

## 4920:00 - 4955:00

And to answer these questions, we have

## 4955:00 - 4985:00

to go back to a more fundamental

## 4985:00 - 5045:00

question. What is even intelligence?

## 5045:00 - 5070:00

What what do we mean when we say we're

## 5070:00 - 5125:00

trying to build AGI? If you look back

## 5125:00 - 5160:00

over the past decades, there's been two

## 5160:00 - 5200:00

lines of thoughts to define intelligence

## 5200:00 - 5235:00

and to define the goals of AI. There's

## 5235:00 - 5300:00

the Minsky style view. Uh AI is about

## 5300:00 - 5325:00

making machines that are capable of

## 5325:00 - 5360:00

performing tasks uh that would normally

## 5360:00 - 5400:00

be done by humans. And this echoes very

## 5400:00 - 5440:00

closely uh the current mainstream

## 5440:00 - 5510:00

corporate view that AGI would be uh a

## 5510:00 - 5550:00

model that could perform most

## 5550:00 - 5600:00

economically valuable tasks like 80% is

## 5600:00 - 5650:00

often quoted as as the number. But then

## 5650:00 - 5690:00

there's the mac view that AI is about

## 5690:00 - 5730:00

getting machines to handle problems they

## 5730:00 - 5765:00

have not been prepared for. It's about

## 5765:00 - 5815:00

getting AI to deal with something new.

## 5815:00 - 5865:00

And my view is more like the MATI view.

## 5865:00 - 5920:00

Intelligence is a process and skill is

## 5920:00 - 5965:00

the output of that process. So skill

## 5965:00 - 6005:00

itself is not intelligence and

## 6005:00 - 6045:00

displaying skill at any number of tasks

## 6045:00 - 6085:00

does not show intelligence. This is like

## 6085:00 - 6130:00

the difference between a road network

## 6130:00 - 6170:00

and a road building company. If you have

## 6170:00 - 6205:00

a road network, then you can go from A

## 6205:00 - 6265:00

to B for a specific predefined set of

## 6265:00 - 6295:00

A's and B's. But if you have a road

## 6295:00 - 6325:00

building company, then you can start

## 6325:00 - 6380:00

connecting new A's, new B's on the fly

## 6380:00 - 6430:00

as your needs evolve. So intelligence is

## 6430:00 - 6465:00

the ability to deal with new situations.

## 6465:00 - 6505:00

It's the ability to blaze fresh trails

## 6505:00 - 6545:00

and build new roads. So attributing

## 6545:00 - 6580:00

intelligence towards really a

## 6580:00 - 6630:00

crystallized behavior program, a skill

## 6630:00 - 6670:00

program, that's a category error. You

## 6670:00 - 6710:00

are confusing the process and its

## 6710:00 - 6765:00

output. So don't confuse the road and

## 6765:00 - 6810:00

the process that created the road. So to

## 6810:00 - 6850:00

formalize this a bit, I see intelligence

## 6850:00 - 6890:00

as the conversion ratio between the

## 6890:00 - 6930:00

information you have uh mostly your past

## 6930:00 - 6985:00

experience but also any uh developer

## 6985:00 - 7015:00

imparted prior that the system might

## 7015:00 - 7065:00

have and your operational area over the

## 7065:00 - 7105:00

space of potential future situations

## 7105:00 - 7135:00

that you might encounter and that's

## 7135:00 - 7175:00

going to feature high novelty and

## 7175:00 - 7220:00

uncertainty. So intelligence is the

## 7220:00 - 7270:00

efficiency with which you operationalize

## 7270:00 - 7310:00

past information in order to deal with

## 7310:00 - 7355:00

the future. It's an efficiency ratio and

## 7355:00 - 7405:00

that's the reason why using exam like

## 7405:00 - 7460:00

benchmarks models is a bad idea. They're

## 7460:00 - 7500:00

not going to tell you how close we are

## 7500:00 - 7545:00

to AGI because human exams weren't

## 7545:00 - 7580:00

designed to measure intelligence. They

## 7580:00 - 7610:00

were designed to measure task specific

## 7610:00 - 7655:00

skill and knowledge. They were designed

## 7655:00 - 7700:00

according to assumptions that are

## 7700:00 - 7730:00

sensible for humans but not for

## 7730:00 - 7765:00

machines. Like for instance, most exams

## 7765:00 - 7795:00

assume that you haven't read and

## 7795:00 - 7835:00

memorized all the exam questions and the

## 7835:00 - 7870:00

answers beforehand. So if you want to

## 7870:00 - 7925:00

regly define and measure intelligence,

## 7925:00 - 7965:00

here are some key concepts that you have

## 7965:00 - 8015:00

to take into account. The first is the

## 8015:00 - 8065:00

distinction between static skills and

## 8065:00 - 8095:00

fluid intelligence. So between having

## 8095:00 - 8145:00

access to a collection uh of static

## 8145:00 - 8200:00

programs to solve known problems versus

## 8200:00 - 8240:00

being able to synthesize brand new

## 8240:00 - 8290:00

programs on the fly to face a problem

## 8290:00 - 8325:00

you never seen before. And of course

## 8325:00 - 8360:00

it's not a binary. It's not one or the

## 8360:00 - 8390:00

other. There's a spectrum between the

## 8390:00 - 8440:00

two. The second concept is operational

## 8440:00 - 8495:00

area for a given skill. There's a big

## 8495:00 - 8530:00

difference between being skilled only in

## 8530:00 - 8555:00

situations that are very close to what

## 8555:00 - 8600:00

you've seen before and uh being skilled

## 8600:00 - 8630:00

for any situation within a very broad

## 8630:00 - 8680:00

scope. For instance, if you know how to

## 8680:00 - 8715:00

drive, you should be able to drive in

## 8715:00 - 8760:00

any city, not just uh in a specific

## 8760:00 - 8800:00

geopence area. Like you can learn to

## 8800:00 - 8825:00

drive in San Jose and then move to

## 8825:00 - 8860:00

Sacramento and you can still drive,

## 8860:00 - 8905:00

right? Again, so it's there's a spectrum

## 8905:00 - 8940:00

there. It's not it's not binary. And

## 8940:00 - 8970:00

lastly, you should look at uh

## 8970:00 - 9000:00

information efficiency for a given

## 9000:00 - 9035:00

skill. How much information, how much

## 9035:00 - 9080:00

data, how much practice did you need to

## 9080:00 - 9110:00

acquire that skill? And of course,

## 9110:00 - 9140:00

higher information efficiency means

## 9140:00 - 9170:00

higher intelligence. And the reason

## 9170:00 - 9230:00

these definitions matter a lot is that

## 9230:00 - 9280:00

as engineers, we can only build what we

## 9280:00 - 9320:00

measure. So the way we define and

## 9320:00 - 9365:00

measure intelligence is not a technical

## 9365:00 - 9410:00

detail. It really reflects our

## 9410:00 - 9435:00

understanding of the problem of

## 9435:00 - 9475:00

cognition. It scopes out the the

## 9475:00 - 9500:00

questions we're going to be asking and

## 9500:00 - 9535:00

so it determines the answers that we're

## 9535:00 - 9565:00

going to be getting. It's the feedback

## 9565:00 - 9620:00

signal that drives us towards our goals.

## 9620:00 - 9660:00

And a phenomenon you see constantly in

## 9660:00 - 9725:00

engineering is the shortcut rule. So

## 9725:00 - 9760:00

it's it's the fact that when you focus

## 9760:00 - 9800:00

on uh achieving a single measure of

## 9800:00 - 9855:00

success, you may succeed but you will do

## 9855:00 - 9885:00

that at the expense of everything else

## 9885:00 - 9935:00

that was not captured by your measure.

## 9935:00 - 9975:00

So you hit the target but you miss the

## 9975:00 - 10020:00

points and you see this all the time uh

## 10020:00 - 10065:00

on Kaggle for instance. Uh we saw it

## 10065:00 - 10105:00

with the Netflix prize where the winning

## 10105:00 - 10145:00

system was extremely accurate but it was

## 10145:00 - 10175:00

way too complex to ever be used in

## 10175:00 - 10205:00

production. So it ended up never being

## 10205:00 - 10245:00

used. It was effectively pointless. Uh

## 10245:00 - 10300:00

we also saw it in AI uh with chess

## 10300:00 - 10335:00

playing for AI. The reason the AI

## 10335:00 - 10385:00

community set out to create uh programs

## 10385:00 - 10425:00

that could play chess back in the 70s

## 10425:00 - 10465:00

was because uh people expected this

## 10465:00 - 10505:00

would teach us about human intelligence.

## 10505:00 - 10540:00

And then a couple decades later, we

## 10540:00 - 10575:00

achieved a goal when Deep Blue beat

## 10575:00 - 10630:00

Kasparov, the world champion. And in the

## 10630:00 - 10665:00

process we had really learned nothing

## 10665:00 - 10705:00

about intelligence. So you hit the

## 10705:00 - 10755:00

targets but you miss the points. And for

## 10755:00 - 10800:00

decades AI has chased task specific

## 10800:00 - 10835:00

skill because that was our definition of

## 10835:00 - 10870:00

intelligence. But this definition only

## 10870:00 - 10915:00

leads to automation which is exactly the

## 10915:00 - 10950:00

kind of system that we have today. But

## 10950:00 - 10990:00

we actually want AI that's capable of

## 10990:00 - 11030:00

autonomous invention. We don't want to

## 11030:00 - 11075:00

stop at automating known tasks. We want

## 11075:00 - 11115:00

AI that could tackle humanity's most

## 11115:00 - 11150:00

difficult challenges and accelerate

## 11150:00 - 11205:00

scientific progress. That's what AGI is

## 11205:00 - 11240:00

meant to be. And to achieve that, we

## 11240:00 - 11275:00

need a new target. We need to stop

## 11275:00 - 11325:00

targeting fluid intelligence itself, the

## 11325:00 - 11385:00

ability to adapt and invent. So one

## 11385:00 - 11435:00

definition of AGI only enops automation.

## 11435:00 - 11475:00

So it increases economic productivity.

## 11475:00 - 11510:00

Obviously, it's extremely valuable.

## 11510:00 - 11550:00

Maybe it also increases unemployment.

## 11550:00 - 11595:00

But the other definition unlocks

## 11595:00 - 11635:00

invention and the acceleration of the

## 11635:00 - 11670:00

timeline of science. And it's by

## 11670:00 - 11700:00

measuring what you really care about

## 11700:00 - 11735:00

that we'll be able to make progress. So

## 11735:00 - 11760:00

we need a better target. We need a

## 11760:00 - 11800:00

better feedback signal.

## 11800:00 - 11830:00

What does that look like? My first

## 11830:00 - 11880:00

attempt at creating a way to measure

## 11880:00 - 11935:00

intelligence in AI systems was the RKGI

## 11935:00 - 11985:00

benchmark. So I released ARK1 back in uh

## 11985:00 - 12050:00

2019. It's like an IQ test for machines

## 12050:00 - 12110:00

and also humans. So ARK1 contains 1,000

## 12110:00 - 12160:00

tasks like this one here. And each task

## 12160:00 - 12200:00

is unique. So that means that you cannot

## 12200:00 - 12245:00

cram for ARC. You have to figure out

## 12245:00 - 12285:00

each task on the fly by using your

## 12285:00 - 12325:00

general intelligence rather than your

## 12325:00 - 12360:00

memorized knowledge. And of course

## 12360:00 - 12420:00

solving any problem always requires some

## 12420:00 - 12450:00

knowledge. And in the case of most

## 12450:00 - 12490:00

benchmarks, the knowledge prior that you

## 12490:00 - 12550:00

need are typically left implicit. In the

## 12550:00 - 12595:00

case of ARC, we made them explicit. So

## 12595:00 - 12640:00

all ARC tasks are built entirely on top

## 12640:00 - 12680:00

of core knowledge prior which are things

## 12680:00 - 12745:00

like objectness, uh elementary physics,

## 12745:00 - 12805:00

um basic geometry, topology, counting.

## 12805:00 - 12850:00

So concepts that any fouryear-old child

## 12850:00 - 12895:00

has already mastered. And solving arc

## 12895:00 - 12935:00

requires very little knowledge and it's

## 12935:00 - 12970:00

knowledge that is very much not

## 12970:00 - 12990:00

specialized. So you don't need to

## 12990:00 - 13030:00

prepare for arc in order to solve it.

## 13030:00 - 13070:00

And what makes arc unique is that you

## 13070:00 - 13105:00

cannot solve it purely by memorizing

## 13105:00 - 13135:00

patterns. It really requires you to

## 13135:00 - 13165:00

demonstrate through the intelligence.

## 13165:00 - 13200:00

And meanwhile pretty pretty much every

## 13200:00 - 13240:00

other benchmark out there is targeting

## 13240:00 - 13280:00

fixed known tasks. So they can't

## 13280:00 - 13305:00

actually be solved or hacked via

## 13305:00 - 13345:00

memorization alone. That's what makes

## 13345:00 - 13385:00

ARC fairly easy for humans but very

## 13385:00 - 13425:00

challenging for AI. And when you see a

## 13425:00 - 13465:00

problem like this where a human child

## 13465:00 - 13505:00

can perform really well but the most

## 13505:00 - 13535:00

advanced the most sophisticated AI

## 13535:00 - 13570:00

models out there struggle that's like a

## 13570:00 - 13610:00

big red flashing light telling you that

## 13610:00 - 13650:00

we're missing something that new ideas

## 13650:00 - 13685:00

are needed. One thing I want you to keep

## 13685:00 - 13735:00

in mind is that ARC is not going to tell

## 13735:00 - 13780:00

you whether a system is already a GR or

## 13780:00 - 13820:00

not. That's not its purpose. Arc is

## 13820:00 - 13860:00

really a tool to direct the attention of

## 13860:00 - 13900:00

the research community towards what we

## 13900:00 - 13945:00

see as the most important unsolved

## 13945:00 - 13990:00

bottlenecks on the way to AGI. So ARC is

## 13990:00 - 14040:00

not the destination and solving ARC is

## 14040:00 - 14070:00

not the goal. Arc is really just an

## 14070:00 - 14110:00

arrow pointing in the right direction

## 14110:00 - 14145:00

and ARC has completely resisted the

## 14145:00 - 14185:00

pre-training scaling paradigm. Even

## 14185:00 - 14235:00

after a 50,000x scale up of pre-trained

## 14235:00 - 14275:00

baselons, their performance on ARC

## 14275:00 - 14315:00

stayed near zero. So we can decisively

## 14315:00 - 14355:00

conclude that fluid intelligence does

## 14355:00 - 14400:00

not emerge from scaling up pre-training.

## 14400:00 - 14450:00

You absolutely need test adaptation in

## 14450:00 - 14480:00

order to demonstrate genuine fluid

## 14480:00 - 14535:00

intelligence. And importantly when the

## 14535:00 - 14585:00

arrival of test adaptation happened last

## 14585:00 - 14625:00

year, ARC was really the only benchmark

## 14625:00 - 14675:00

at the time that provided a clear signal

## 14675:00 - 14705:00

about the profound shift that was

## 14705:00 - 14745:00

happening. other benchmarks were

## 14745:00 - 14785:00

saturated. So they could not distinguish

## 14785:00 - 14830:00

between a true IQ increase and just

## 14830:00 - 14865:00

brute force scaling.

## 14865:00 - 14905:00

So now you you see this graph and you're

## 14905:00 - 14930:00

probably asking well clearly at this

## 14930:00 - 14970:00

point AR1 is also saturating. So does

## 14970:00 - 15010:00

that mean we have human level AI now?

## 15010:00 - 15070:00

Well not yet. What you see on this graph

## 15070:00 - 15140:00

is that ARK1 was a binary test. It was a

## 15140:00 - 15170:00

minimal reproduction of fluid

## 15170:00 - 15200:00

intelligence. So it only really gives

## 15200:00 - 15260:00

you two possible modes. Either you have

## 15260:00 - 15290:00

no fluid intelligence in which case you

## 15290:00 - 15350:00

will score near zero like basel or you

## 15350:00 - 15385:00

have nonzero fluid intelligence in which

## 15385:00 - 15435:00

case you will instantly score very high

## 15435:00 - 15470:00

like the O3 model from open eye for

## 15470:00 - 15510:00

instance. And of course every one of you

## 15510:00 - 15545:00

in this room would score within noise

## 15545:00 - 15630:00

distance of 100%. So ARC saturates ARK

## 15630:00 - 15685:00

one saturates way below human level

## 15685:00 - 15740:00

fluid intelligence. And so now we are in

## 15740:00 - 15790:00

need of a better tool, a more sensitive

## 15790:00 - 15825:00

tool that would provide more useful

## 15825:00 - 15870:00

bandwidths and better comparison with

## 15870:00 - 15905:00

human intelligence

## 15905:00 - 15960:00

and that tool is ARGI 2 which released

## 15960:00 - 16020:00

in March this year. So back in 2019,

## 16020:00 - 16060:00

ARK1 was meant to challenge the deep

## 16060:00 - 16095:00

learning pattern where models are big

## 16095:00 - 16135:00

parametric curves uh used for static

## 16135:00 - 16175:00

inference and today ARK 2 challenges

## 16175:00 - 16215:00

reasoning systems. It changes the test

## 16215:00 - 16265:00

adaptation pattern. The benchmark format

## 16265:00 - 16300:00

is still the same. There's a much

## 16300:00 - 16345:00

greater focus on probing compositional

## 16345:00 - 16390:00

jarization. So the tasks are still very

## 16390:00 - 16420:00

feasible for humans, but they're much

## 16420:00 - 16465:00

more sophisticated. And as a result, ARK

## 16465:00 - 16515:00

2 is not easily brute forceable. In

## 16515:00 - 16555:00

practice, what this means is that in ARK

## 16555:00 - 16590:00

one, for many tasks, you could just look

## 16590:00 - 16630:00

at it and instantly see the solution

## 16630:00 - 16665:00

without having to think too much about

## 16665:00 - 16735:00

it. With ARK 2, all tasks require some

## 16735:00 - 16780:00

level of deliberate thinking, but they

## 16780:00 - 16820:00

still remain very feasible for humans.

## 16820:00 - 16865:00

And we know this because we tested 400

## 16865:00 - 16915:00

people firsthand in person in San Diego

## 16915:00 - 16960:00

over several days. And we are not

## 16960:00 - 16990:00

talking about people who have physics

## 16990:00 - 17050:00

PhDs here. We recruited uh random folks

## 17050:00 - 17095:00

uh Uber drivers, UCDS students, uh

## 17095:00 - 17120:00

people who are unemployed. So basically

## 17120:00 - 17150:00

anyone trying to make some money on the

## 17150:00 - 17215:00

side and all tasks in AR 2 were sold by

## 17215:00 - 17250:00

at least two of the people that saw it.

## 17250:00 - 17295:00

And each task was seen on average by

## 17295:00 - 17325:00

about seven people. And so what that

## 17325:00 - 17370:00

tells you is that a group of 10 random

## 17370:00 - 17420:00

people with majority voting would score

## 17420:00 - 17480:00

100% on ARK 2. So we know these tasks

## 17480:00 - 17525:00

are completely doable by regular folks

## 17525:00 - 17575:00

with no prior training. So how well do

## 17575:00 - 17630:00

AI models do? Well, if you take basel

## 17630:00 - 17675:00

models like GPT4.5,

## 17675:00 - 17730:00

Lama 4, it's simple. They get 0%. There

## 17730:00 - 17770:00

is simply no way to do these tasks

## 17770:00 - 17815:00

simply via memorization. Next, if you

## 17815:00 - 17855:00

look at static reasoning systems, so

## 17855:00 - 17900:00

systems that use a single chin of

## 17900:00 - 17925:00

thoughts that they generate for the

## 17925:00 - 17960:00

task, they don't do much better. They do

## 17960:00 - 18005:00

on the order of one to 2%. So very much

## 18005:00 - 18045:00

within noise distance of zero. So what

## 18045:00 - 18085:00

that tells you is that to solve AR 2,

## 18085:00 - 18140:00

you really need test adaptation. All

## 18140:00 - 18175:00

systems that do meaningfully above zero

## 18175:00 - 18220:00

are using TTL, but even then they're

## 18220:00 - 18260:00

still far below human level. So compared

## 18260:00 - 18305:00

to ARK1, AR2 enables much more granular

## 18305:00 - 18350:00

evaluation of DTS systems. Systems like

## 18350:00 - 18390:00

03 for instance. And that's where you

## 18390:00 - 18440:00

see that 03 and other systems like it

## 18440:00 - 18490:00

are still not yet quite human level. And

## 18490:00 - 18535:00

in my view, as long as it's easy to come

## 18535:00 - 18575:00

up with tasks that any one of you can do

## 18575:00 - 18620:00

that are easy for humans, but that AI

## 18620:00 - 18655:00

cannot figure out no matter how much

## 18655:00 - 18695:00

computers are it, we don't have a GI

## 18695:00 - 18730:00

yet. and you will know that we are close

## 18730:00 - 18765:00

to having AGI when it becomes

## 18765:00 - 18800:00

increasingly difficult to come up with

## 18800:00 - 18835:00

such tasks. We're clearly not there yet.

## 18835:00 - 18890:00

And to be clear, I don't think ARK 2 is

## 18890:00 - 18930:00

the final test. We're not going to stop

## 18930:00 - 18970:00

at ARC 2. We've started development on

## 18970:00 - 19030:00

RKGI 3 and AR 3 is a significant

## 19030:00 - 19075:00

departure from the input output pair

## 19075:00 - 19130:00

formats of ARC one and two. We're

## 19130:00 - 19180:00

assessing agency, the ability to

## 19180:00 - 19220:00

explore, uh, to learn interactively, to

## 19220:00 - 19260:00

set goals, uh, achieve goals

## 19260:00 - 19305:00

autonomously. So, your AI is dropped

## 19305:00 - 19355:00

into a brand new environment where it

## 19355:00 - 19395:00

doesn't know what the controls do. It

## 19395:00 - 19415:00

doesn't know what the goal is. It

## 19415:00 - 19445:00

doesn't know where the the gameplay

## 19445:00 - 19480:00

mechanics are, just to figure out

## 19480:00 - 19525:00

everything on the fly, starting with

## 19525:00 - 19565:00

what is it even supposed to do uh, uh,

## 19565:00 - 19600:00

in the game. And every single game is

## 19600:00 - 19645:00

entirely unique. They're all built on

## 19645:00 - 19685:00

top of core knowledge prior only, just

## 19685:00 - 19740:00

like in AR one and two. So we'll have

## 19740:00 - 19785:00

hundreds of interactive reasoning tasks

## 19785:00 - 19840:00

like this one. And efficiency is central

## 19840:00 - 19885:00

to the design of AR 3. So models won't

## 19885:00 - 19920:00

just be graded on whether they can solve

## 19920:00 - 19965:00

a task, but on how efficiently they

## 19965:00 - 20000:00

solve it. And we are establishing a

## 20000:00 - 20040:00

strict limit of the number of actions

## 20040:00 - 20075:00

that a model can take. And we are

## 20075:00 - 20110:00

targeting the same level of action

## 20110:00 - 20140:00

efficiency as we observe in human. So

## 20140:00 - 20205:00

we're going to launch this in early 2026

## 20205:00 - 20240:00

and next month in July we're going to

## 20240:00 - 20270:00

release a developer preview so you can

## 20270:00 - 20300:00

start playing with it. What's it going

## 20300:00 - 20345:00

to take to solve AR 2 and we're still

## 20345:00 - 20390:00

very far from it today. Uh then solve AR

## 20390:00 - 20445:00

3 and we're even further away from that.

## 20445:00 - 20485:00

Maybe in the future solve AR 4

## 20485:00 - 20525:00

eventually get to AGI. What are we still

## 20525:00 - 20575:00

missing? So I've said that intelligence

## 20575:00 - 20610:00

is the efficiency with which you

## 20610:00 - 20665:00

operationalize the past to face a

## 20665:00 - 20700:00

constantly changing future. But of

## 20700:00 - 20745:00

course if the future you face had really

## 20745:00 - 20780:00

nothing in common with the past, no

## 20780:00 - 20805:00

common ground with anything you've seen

## 20805:00 - 20840:00

before, you could not make sense of it

## 20840:00 - 20880:00

no matter how intelligent you were. But

## 20880:00 - 20925:00

here's the thing. Nothing is ever truly

## 20925:00 - 20960:00

novel. The universe around you is made

## 20960:00 - 21000:00

of many different things that are all

## 21000:00 - 21035:00

similar to each other. Like one tree is

## 21035:00 - 21060:00

similar to another tree is also similar

## 21060:00 - 21130:00

to your neuron or electromagnetism

## 21130:00 - 21170:00

is similar to hydrodnamics is also

## 21170:00 - 21215:00

similar to gravity. So we are surrounded

## 21215:00 - 21250:00

by isomorphisms.

## 21250:00 - 21295:00

I call this the kaleidoscope hypothesis.

## 21295:00 - 21325:00

Our experience of the world seems to

## 21325:00 - 21365:00

feature a neverending novelty and

## 21365:00 - 21410:00

complexity. But the number of unique

## 21410:00 - 21440:00

atoms of meaning that you need to

## 21440:00 - 21480:00

describe it is actually very small. And

## 21480:00 - 21535:00

everything around you is a recombination

## 21535:00 - 21585:00

of these atoms. And intelligence is the

## 21585:00 - 21635:00

ability to mine your experience to

## 21635:00 - 21675:00

identify these atoms of meaning that can

## 21675:00 - 21705:00

be reused across many different

## 21705:00 - 21740:00

situations, across many different tasks.

## 21740:00 - 21785:00

And this involves identifying um

## 21785:00 - 21845:00

invariance uh structure uh things that

## 21845:00 - 21885:00

seem to be repeated principles.

## 21885:00 - 21925:00

And these building blocks, these atoms

## 21925:00 - 21975:00

are called abstractions. And whenever

## 21975:00 - 22010:00

you encounter a new situation, you're

## 22010:00 - 22050:00

going to make sense of it by recombining

## 22050:00 - 22090:00

on the fly abstractions from your

## 22090:00 - 22135:00

collection to create a brand new model

## 22135:00 - 22185:00

that's adapted to the situation. So

## 22185:00 - 22210:00

implementing intelligence is going to

## 22210:00 - 22265:00

have two key parts. First, there's

## 22265:00 - 22305:00

abstraction acquisition. You want to be

## 22305:00 - 22355:00

able to efficiently extract reusable

## 22355:00 - 22385:00

abstractions from your past experience,

## 22385:00 - 22430:00

from a feed of data, for instance. And

## 22430:00 - 22475:00

then there's on the-fly recombination.

## 22475:00 - 22525:00

You want to be able to efficiently uh

## 22525:00 - 22560:00

select and recombine these building

## 22560:00 - 22615:00

blocks uh into models that are fit for

## 22615:00 - 22660:00

the current situation. And the emphasis

## 22660:00 - 22720:00

on efficiency here is crucial. How

## 22720:00 - 22765:00

intelligent you are is not just

## 22765:00 - 22785:00

determined by whether you can do

## 22785:00 - 22810:00

something. It's determined by how

## 22810:00 - 22845:00

efficiently you can acquire good

## 22845:00 - 22880:00

abstractions from ret experience. how

## 22880:00 - 22915:00

efficiently you can recombine them to

## 22915:00 - 22955:00

navigate novelty. So if you need

## 22955:00 - 22990:00

hundreds of thousands of hours to

## 22990:00 - 23035:00

acquire a simple skill, uh you're not

## 23035:00 - 23065:00

very intelligent. Or if you need to

## 23065:00 - 23105:00

enumerate every single move on the

## 23105:00 - 23145:00

chessboard to find the best move, you're

## 23145:00 - 23175:00

not very intelligent. So intelligence is

## 23175:00 - 23220:00

not just demonstrating high skill. It's

## 23220:00 - 23250:00

really the efficiency with which you

## 23250:00 - 23300:00

acquire and deploy these skills. It's

## 23300:00 - 23330:00

both data efficiency and compute

## 23330:00 - 23385:00

efficiency. And at this point, you start

## 23385:00 - 23425:00

to see why simply making our AI models

## 23425:00 - 23460:00

bigger and training them on more data

## 23460:00 - 23510:00

didn't automatically lead to a GI. We

## 23510:00 - 23545:00

were missing a couple of things. First,

## 23545:00 - 23585:00

these models lacked the ability to do on

## 23585:00 - 23625:00

the-fly recombination. So at training

## 23625:00 - 23655:00

time, they were learning a lot. They

## 23655:00 - 23695:00

were acquiring many useful abstractions,

## 23695:00 - 23720:00

but then at test time, they were

## 23720:00 - 23755:00

completely static. You could only use

## 23755:00 - 23805:00

them to fetch and apply a pre-recorded

## 23805:00 - 23860:00

template. And that is a critical problem

## 23860:00 - 23910:00

that test adaptation is addressing. TTA

## 23910:00 - 23960:00

adds on the re combination capabilities

## 23960:00 - 24005:00

to our AI. And that's actually that's a

## 24005:00 - 24045:00

huge step forward that gets us much much

## 24045:00 - 24095:00

closer to a GI. That's not the only

## 24095:00 - 24125:00

problem. Recombination is not the only

## 24125:00 - 24165:00

thing missing. The other problem is that

## 24165:00 - 24195:00

these models are still incredibly

## 24195:00 - 24240:00

inefficient. If you take gradient

## 24240:00 - 24275:00

descent for instance, gradient descent

## 24275:00 - 24330:00

uh requires vast amounts of data to

## 24330:00 - 24375:00

distill simple abstractions many orders

## 24375:00 - 24420:00

of magnitude more data than what humans

## 24420:00 - 24450:00

need roughly three to four orders of

## 24450:00 - 24515:00

magnitude more. And if you look at uh uh

## 24515:00 - 24550:00

re combination efficiency, even the

## 24550:00 - 24600:00

latest state-of-the-art CTA techniques,

## 24600:00 - 24640:00

they still need thousands of dollars of

## 24640:00 - 24710:00

compute uh to solve ARK1 at human level.

## 24710:00 - 24755:00

And that doesn't even scale to AR 2. And

## 24755:00 - 24790:00

the fundamental issue here is that deep

## 24790:00 - 24825:00

learning models are missing

## 24825:00 - 24860:00

compositional generalization. And that's

## 24860:00 - 24895:00

the thing that ARK 2 is trying to

## 24895:00 - 24945:00

measure. And the reason why is that

## 24945:00 - 24970:00

there's more than one kind of

## 24970:00 - 25005:00

abstraction. And this is really

## 25005:00 - 25040:00

important. I said that intelligence is

## 25040:00 - 25080:00

about mining abstractions from data and

## 25080:00 - 25110:00

then re combining them. There's really

## 25110:00 - 25145:00

two kinds of abstraction. There's type

## 25145:00 - 25190:00

one and type two. They're pretty similar

## 25190:00 - 25225:00

to each other. They mirror each other.

## 25225:00 - 25270:00

So both are about comparing things,

## 25270:00 - 25305:00

comparing instances and merging

## 25305:00 - 25345:00

individual instances into common

## 25345:00 - 25405:00

templates by eliminating certain details

## 25405:00 - 25430:00

about the instances. So basically you

## 25430:00 - 25465:00

take a bunch of things, you compare

## 25465:00 - 25505:00

them, you drop the details that don't

## 25505:00 - 25545:00

matter and what you're left with is an

## 25545:00 - 25575:00

abstraction and the key difference

## 25575:00 - 25620:00

between the two is that one operates

## 25620:00 - 25660:00

over a continuous domain and the other

## 25660:00 - 25695:00

operates over a discrete domain. So type

## 25695:00 - 25745:00

one or value centric abstraction is

## 25745:00 - 25790:00

about comparing things via a continuous

## 25790:00 - 25830:00

distance function and that's the kind of

## 25830:00 - 25875:00

abstraction that's behind uh perception

## 25875:00 - 25915:00

pattern cognition intuition and also of

## 25915:00 - 25950:00

course modern machine learning and type

## 25950:00 - 25990:00

two or programcentric abstraction is

## 25990:00 - 26030:00

about comparing discrete programs which

## 26030:00 - 26075:00

is to say graphs and instead of trying

## 26075:00 - 26120:00

to compute distances between them you're

## 26120:00 - 26165:00

going to be looking for uh exact

## 26165:00 - 26190:00

structure matching You're going to be

## 26190:00 - 26245:00

looking for exact isomorphisms, subgraph

## 26245:00 - 26280:00

isomeorphisms. And this is what

## 26280:00 - 26325:00

underlying much of human reasoning. It's

## 26325:00 - 26360:00

also what software engineers do when

## 26360:00 - 26390:00

they're refactoring some code. So if you

## 26390:00 - 26420:00

hear a software engineer talk about

## 26420:00 - 26445:00

abstraction, they mean this kind of

## 26445:00 - 26490:00

abstraction. So two kinds of abstraction

## 26490:00 - 26530:00

both driven by analogy making either

## 26530:00 - 26580:00

value analogy or program analogy. And

## 26580:00 - 26630:00

all cognition arises from a combination

## 26630:00 - 26670:00

of these two forms of abstraction. You

## 26670:00 - 26700:00

can remember them. They had left brain

## 26700:00 - 26755:00

versus right brain metaphor. One half

## 26755:00 - 26800:00

for perception, intuition, and the other

## 26800:00 - 26865:00

half for reasoning, planning, uh rigor.

## 26865:00 - 26900:00

And transformers are greats at type one

## 26900:00 - 26935:00

abstraction. They can do everything that

## 26935:00 - 26970:00

type one is effective for perception,

## 26970:00 - 27005:00

intuition, pattern cognition, they all

## 27005:00 - 27035:00

work well. So in that sense,

## 27035:00 - 27070:00

transformers are major breakthrough in

## 27070:00 - 27120:00

AI, but they're still not a good fit for

## 27120:00 - 27160:00

type two. And this is why you will

## 27160:00 - 27190:00

struggle to train one of these models to

## 27190:00 - 27235:00

do very simple type two things like

## 27235:00 - 27280:00

sorting a list or adding digits provided

## 27280:00 - 27330:00

as a sequence of tokens. So how are we

## 27330:00 - 27365:00

going to get to type two? You have to

## 27365:00 - 27405:00

leverage discrete program search as

## 27405:00 - 27445:00

opposed to purely manipulating

## 27445:00 - 27500:00

continuous interpolated spaces learn

## 27500:00 - 27555:00

with descent. Search is what unlocks

## 27555:00 - 27610:00

invention beyond just automation. All

## 27610:00 - 27650:00

known AI systems today that are capable

## 27650:00 - 27695:00

of some kind of uh uh invention, some

## 27695:00 - 27730:00

kind of creativity, they rely on

## 27730:00 - 27770:00

discrete search. Uh even back in the

## 27770:00 - 27805:00

90s, we were already using gigantic

## 27805:00 - 27835:00

search to come up with new antenna

## 27835:00 - 27900:00

designs. Or you can take uh Alph Go with

## 27900:00 - 27945:00

move 37 that was discrete search or more

## 27945:00 - 27990:00

recently the alpha evol system from deep

## 27990:00 - 28030:00

mind all discrete search systems. So

## 28030:00 - 28075:00

deep learning doesn't invent but search

## 28075:00 - 28125:00

does. So what's discrete program search?

## 28125:00 - 28180:00

It's basically combinatoral search over

## 28180:00 - 28230:00

graphs of operators taken from some

## 28230:00 - 28280:00

language, some DSL. And to better

## 28280:00 - 28325:00

understand it, you can try to draw an

## 28325:00 - 28375:00

analogy between program synthesis and

## 28375:00 - 28405:00

the machine learning techniques you

## 28405:00 - 28435:00

already know about. In machine learning,

## 28435:00 - 28480:00

your model is a differentiable

## 28480:00 - 28515:00

parametric function. So it's a curve. In

## 28515:00 - 28550:00

program synthesis, it's going to be a

## 28550:00 - 28595:00

discrete graph, a graph of ops, symbolic

## 28595:00 - 28645:00

ops from some language. In ML, your

## 28645:00 - 28675:00

learning engine, the way you create

## 28675:00 - 28725:00

models is gradient descent, which is

## 28725:00 - 28760:00

very comput efficient. By the way,

## 28760:00 - 28790:00

gradient descent will let you find a

## 28790:00 - 28820:00

model that fits the data very quickly,

## 28820:00 - 28850:00

very efficiently. In program synthesis,

## 28850:00 - 28905:00

the learning engine is searchal search,

## 28905:00 - 28935:00

which is extremely compute efficient.

## 28935:00 - 28970:00

Obviously in machine learning the key

## 28970:00 - 29015:00

obstacle that you run into is data

## 29015:00 - 29060:00

density. In order to fit a model you

## 29060:00 - 29090:00

need a dense sampling of the data

## 29090:00 - 29155:00

manifold. You need a lot of data and

## 29155:00 - 29190:00

program synthesis is the exact reverse.

## 29190:00 - 29220:00

Program synthes is extremely data

## 29220:00 - 29260:00

efficient. You can fit a program using

## 29260:00 - 29300:00

only two or three examples. But in order

## 29300:00 - 29340:00

to find that program you have to sift

## 29340:00 - 29390:00

through a vast space of potential

## 29390:00 - 29435:00

programs. And the size of that space

## 29435:00 - 29480:00

grows cuminally with problem complexity.

## 29480:00 - 29515:00

So you run into this communatoral

## 29515:00 - 29555:00

explosion wall. I said earlier that

## 29555:00 - 29600:00

intelligence is a combination of two

## 29600:00 - 29635:00

forms abstraction. Type one and type

## 29635:00 - 29670:00

two. And I really don't think that

## 29670:00 - 29705:00

you're going to go very far if you go

## 29705:00 - 29745:00

all in on just one of them. Like all in

## 29745:00 - 29785:00

on type one or all in on type two. I

## 29785:00 - 29810:00

think that if you want to really unlock

## 29810:00 - 29840:00

their potential, you have to combine

## 29840:00 - 29885:00

them together. And that's what human

## 29885:00 - 29915:00

intelligence is really good at. That's

## 29915:00 - 29965:00

really what makes us special. We combine

## 29965:00 - 30000:00

perception and intuition together with

## 30000:00 - 30030:00

explicit step-by-step reasoning. We

## 30030:00 - 30075:00

combine both forms of abstraction in all

## 30075:00 - 30100:00

our thoughts, all our actions

## 30100:00 - 30125:00

everywhere. For instance, when you're

## 30125:00 - 30170:00

playing chess, you're using type two.

## 30170:00 - 30215:00

when you calculate when you unfold some

## 30215:00 - 30260:00

potential moves step by step in your

## 30260:00 - 30285:00

mind. But you're not going to do this

## 30285:00 - 30320:00

for every possible move, of course,

## 30320:00 - 30350:00

because there are too many of them,

## 30350:00 - 30375:00

right? You're only going to be doing it

## 30375:00 - 30410:00

for a couple of different options,

## 30410:00 - 30430:00

right? Like here, you're going to look

## 30430:00 - 30475:00

at the knight, the queen. And the way

## 30475:00 - 30515:00

you narrow down these options is via

## 30515:00 - 30550:00

intuition, is via pattern recognition on

## 30550:00 - 30580:00

the board. So, and you build that up

## 30580:00 - 30615:00

very much through experience, right?

## 30615:00 - 30650:00

You've mined your past experience

## 30650:00 - 30680:00

unconsciously to extract these patterns

## 30680:00 - 30715:00

and that's very much type one. So you're

## 30715:00 - 30755:00

using type one intuition to make type

## 30755:00 - 30795:00

two calculation tractable. So how is the

## 30795:00 - 30820:00

merger between type one and type two

## 30820:00 - 30860:00

going to work? Well the key system two

## 30860:00 - 30900:00

technique is discrete search over a

## 30900:00 - 30930:00

space of program one and the blocker

## 30930:00 - 30965:00

that you run into is explosion. And

## 30965:00 - 31000:00

meanwhile the key system one technique

## 31000:00 - 31045:00

is uh curve fitting and interpolation on

## 31045:00 - 31080:00

the curve. So you take a lot of data,

## 31080:00 - 31110:00

you embed it on some kind of

## 31110:00 - 31160:00

interpolating manifold that enables fast

## 31160:00 - 31205:00

but approximate judgment calls about the

## 31205:00 - 31255:00

target space and the big idea is going

## 31255:00 - 31290:00

to be to leverage these fast but

## 31290:00 - 31330:00

approximate judgment calls to fight

## 31330:00 - 31375:00

commit explosion and make program search

## 31375:00 - 31415:00

tractable. A simple analogy to

## 31415:00 - 31450:00

understand this would be drawing a map.

## 31450:00 - 31490:00

So you take a space of discrete objects

## 31490:00 - 31520:00

with discrete relationships that would

## 31520:00 - 31560:00

normally require connectal search like

## 31560:00 - 31590:00

path finding on a subway system for

## 31590:00 - 31635:00

instance and you embed these objects uh

## 31635:00 - 31675:00

into a latent space where you can use a

## 31675:00 - 31720:00

continuous distance function to make

## 31720:00 - 31765:00

fast but approximate guesses about these

## 31765:00 - 31795:00

great relationships

## 31795:00 - 31835:00

and this enables you to keep explosion

## 31835:00 - 31895:00

in check while doing search

## 31895:00 - 31925:00

and this is what the full picture looks

## 31925:00 - 31965:00

like. This is the system that we are

## 31965:00 - 32000:00

currently working on. AI is going to

## 32000:00 - 32040:00

move towards systems that are more like

## 32040:00 - 32090:00

programmers that approach a new task by

## 32090:00 - 32130:00

writing software for it. And when faced

## 32130:00 - 32170:00

with a new task, your programmer like

## 32170:00 - 32220:00

metalarner will synthesize on the fly a

## 32220:00 - 32270:00

program or model that is adapted to the

## 32270:00 - 32315:00

task. And this program will blend uh

## 32315:00 - 32345:00

deep learning subm modules for type one

## 32345:00 - 32380:00

sub problems like perception for

## 32380:00 - 32425:00

instance and algorithmic modules uh for

## 32425:00 - 32475:00

type two sub problems. And these models

## 32475:00 - 32515:00

are going to be assembled by a discrete

## 32515:00 - 32565:00

program search system that is guided by

## 32565:00 - 32605:00

deep learning based intuition about the

## 32605:00 - 32640:00

structure of program space. And this

## 32640:00 - 32685:00

search process isn't done from scratch.

## 32685:00 - 32725:00

is going to leverage a global library of

## 32725:00 - 32755:00

reusable building blocks of

## 32755:00 - 32790:00

abstractions. And that library is

## 32790:00 - 32825:00

constantly evolving as it's learning

## 32825:00 - 32860:00

from incoming tasks. So when a new

## 32860:00 - 32890:00

problem appears, the system is going to

## 32890:00 - 32930:00

search through this library for relevant

## 32930:00 - 32975:00

building blocks. Uh and whenever in the

## 32975:00 - 33005:00

in the course of solving a new problem,

## 33005:00 - 33030:00

you're synthesizing a new building

## 33030:00 - 33050:00

block. You're going to be uploading it

## 33050:00 - 33090:00

back to the library. Much like as a

## 33090:00 - 33130:00

software engineer, if you develop a

## 33130:00 - 33160:00

useful library for your own work, you're

## 33160:00 - 33185:00

going to put it on GitHub. so that other

## 33185:00 - 33225:00

people can reuse it. And the ultimate

## 33225:00 - 33265:00

goal here is to have an AI that can face

## 33265:00 - 33305:00

a completely new situation and it's

## 33305:00 - 33330:00

going to use its rich abstraction

## 33330:00 - 33375:00

library uh to quickly assemble a working

## 33375:00 - 33405:00

model much like a human software

## 33405:00 - 33445:00

engineer can quickly create a piece of

## 33445:00 - 33480:00

software to solve a new problem by

## 33480:00 - 33525:00

leveraging existing tools in libraries.

## 33525:00 - 33560:00

And this AI is going to keep improving

## 33560:00 - 33610:00

itself over time both by expanding its

## 33610:00 - 33650:00

library of abstractions and also by

## 33650:00 - 33690:00

refining its intuition about the

## 33690:00 - 33740:00

structure of program space.

## 33740:00 - 33775:00

This system is what you are building at

## 33775:00 - 33830:00

India our new research lab. We started

## 33830:00 - 33870:00

India because we believe that in order

## 33870:00 - 33900:00

to dramatically accelerate scientific

## 33900:00 - 33945:00

progress we need AI that's capable of

## 33945:00 - 33990:00

independent invention and discovery. We

## 33990:00 - 34030:00

need AI that could expand the frontiers

## 34030:00 - 34085:00

of knowledge, not just uh operate within

## 34085:00 - 34135:00

them. And we really believe that a new

## 34135:00 - 34165:00

form of AI is going to be key to this

## 34165:00 - 34205:00

acceleration. Deep learning is great at

## 34205:00 - 34235:00

automation. It's incredibly powerful for

## 34235:00 - 34275:00

automation, but scientific discovery

## 34275:00 - 34325:00

requires something more. And our

## 34325:00 - 34375:00

approach at Tendia is to leverage a deep

## 34375:00 - 34420:00

learning guided uh program search to

## 34420:00 - 34460:00

build this uh programmer like

## 34460:00 - 34505:00

metalarner. And to test our progress,

## 34505:00 - 34535:00

our first milestone is going to be to

## 34535:00 - 34585:00

solve RKGI using a system that starts at

## 34585:00 - 34635:00

knowing nothing at all about RKGI.

## 34635:00 - 34665:00

And you ultimately want to leverage our

## 34665:00 - 34710:00

system for science to empower human

## 34710:00 - 34750:00

researchers and help accelerate the

## 34750:00+

timeline of science.

