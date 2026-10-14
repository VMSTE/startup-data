---
source: https://www.youtube.com/watch?v=2Yguz5U-Nic
title: "Nobel Laureate John Jumper: AI is Revolutionizing Scientific Discovery"
author: Y Combinator
date: 2025-07-15
views: 41158
description: >-
  John Jumper on June 16, 2025 at AI Startup School in San Francisco.


  John Jumper is a physicist-turned-computational biologist who led DeepMind’s
  AlphaFold team—and earned the 2024 Nobel Prize in Chemistry for solving
  protein folding, a decades-old scientific challenge. 


  In this talk, he shares how a deep learning breakthrough at CASP14 turned into
  AlphaFold 1 and then AlphaFold 2, delivering atomic accuracy predictions and
  revolutionizing biology. He explains the scientific puzzle behind protein
  folding, the key algorithmic breakthroughs, and the impact of making millions
  of protein structures accessible to researchers worldwide.


  Apply to Y Combinator: https://ycombinator.com/apply

  Work at a startup: https://workatastartup.com


  Chapters:

  00:00 - Personal Background

  01:26 - Transition to Computational Biology

  02:01 - Journey into Machine Learning

  02:59 - Joining Google DeepMind

  03:47 - AlphaFold and Its Impact

  04:54 - The Complexity of Cells and Proteins

  07:44 - Challenges in Protein Structure Determination

  10:28 - Building the AlphaFold AI System

  11:29 - The Importance of Research in AI

  13:28 - AlphaFold's Breakthrough and Public Data

  18:09 - Making AlphaFold Accessible

  21:20 - Real-World Applications and Success Stories

  22:33 - Engineering New Proteins with AlphaFold

  25:23 - Future of AI in Structural Biology
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:43:57.808Z
---

# Nobel Laureate John Jumper: AI is Revolutionizing Scientific Discovery

## 00:00 - 35:00

This is something of a nice change. I've

## 35:00 - 70:00

given a lot of scientific talks and no

## 70:00 - 115:00

one claps and cheers when I come on. Not

## 115:00 - 225:00

normally even when I come on.

## 225:00 - 250:00

It's really exciting. It's really

## 250:00 - 295:00

wonderful to be here. I guess I should

## 295:00 - 325:00

start off assuming that not everyone in

## 325:00 - 380:00

this cavernous hall knows who I am. Who

## 380:00 - 425:00

am I? I'm I'm someone who has done some

## 425:00 - 470:00

work in AI for science who really

## 470:00 - 525:00

believes that we can use the AI systems,

## 525:00 - 580:00

these technologies, these ideas to

## 580:00 - 615:00

change the world in a very specific way

## 615:00 - 660:00

to make science go faster to enable new

## 660:00 - 700:00

discoveries. I think it's really really

## 700:00 - 735:00

wonderful. We have the opportunity to

## 735:00 - 790:00

take these tools, these ideas

## 790:00 - 830:00

and aim them toward the question of how

## 830:00 - 875:00

can we build the right AI systems so

## 875:00 - 915:00

that sick people can become healthy and

## 915:00 - 960:00

go home from the hospital. And it's been

## 960:00 - 1000:00

kind of a a really wonderful and winding

## 1000:00 - 1040:00

journey for me to end up here. I was

## 1040:00 - 1075:00

originally trained as a physicist. I

## 1075:00 - 1100:00

thought I was going to be a laws of the

## 1100:00 - 1145:00

universe physicist. If I was very very

## 1145:00 - 1175:00

lucky, I could do something that would

## 1175:00 - 1225:00

end up one sentence in a textbook.

## 1225:00 - 1270:00

And I did physics and I went to actually

## 1270:00 - 1325:00

do a PhD in physics. And then kind of

## 1325:00 - 1370:00

what I was working on didn't really grab

## 1370:00 - 1400:00

me. I just it didn't feel like what I

## 1400:00 - 1440:00

wanted to do. So I dropped out. I didn't

## 1440:00 - 1465:00

start a startup. That would have been

## 1465:00 - 1515:00

very on point for this event, but I uh

## 1515:00 - 1560:00

dropped out and I ended up working at a

## 1560:00 - 1595:00

company that was doing computational

## 1595:00 - 1630:00

biology. How do we get computers to say

## 1630:00 - 1675:00

something smart about biology? And I

## 1675:00 - 1715:00

loved it. I loved it not just because it

## 1715:00 - 1740:00

was fun, but it was something that would

## 1740:00 - 1785:00

let me do what I thought I was good at.

## 1785:00 - 1830:00

Write code, manipulate equations, think

## 1830:00 - 1860:00

hard thoughts about the nature of the

## 1860:00 - 1905:00

world and use it toward this very

## 1905:00 - 1950:00

applied purpose that at the end we want

## 1950:00 - 1985:00

to ena we want to make medicines or we

## 1985:00 - 2025:00

want to enable others to make medicines.

## 2025:00 - 2075:00

Then I really kind of became a biologist

## 2075:00 - 2100:00

and a machine learner. Actually a

## 2100:00 - 2125:00

machine learner because I left that job

## 2125:00 - 2150:00

and I went back to grad school in

## 2150:00 - 2215:00

biohysics and chemistry and uh I no

## 2215:00 - 2245:00

longer had access to this incredible

## 2245:00 - 2290:00

computer hardware that I had when I was

## 2290:00 - 2320:00

working at my previous job and in fact

## 2320:00 - 2365:00

they had custom asics for simulating how

## 2365:00 - 2390:00

proteins this part of your body that

## 2390:00 - 2425:00

I'll talk about move. And since I didn't

## 2425:00 - 2465:00

have that anymore but I still wanted to

## 2465:00 - 2490:00

work on the same problems. Well, I

## 2490:00 - 2510:00

didn't want to just do the same thing

## 2510:00 - 2565:00

with less compute. And so I started to

## 2565:00 - 2590:00

learn and I was getting very interested

## 2590:00 - 2640:00

in statistics, in machine learning. We

## 2640:00 - 2680:00

didn't call it AI back then. In fact, we

## 2680:00 - 2700:00

didn't even call it machine learning.

## 2700:00 - 2725:00

That was a bit disreputable. I said, I'm

## 2725:00 - 2775:00

working in statistical physics. But you

## 2775:00 - 2805:00

know, how are we going to develop

## 2805:00 - 2830:00

algorithms? How are we going to learn

## 2830:00 - 2865:00

from data and do that instead of very

## 2865:00 - 2890:00

large compute? And I guess it turns out

## 2890:00 - 2930:00

in terms of AI in addition to very large

## 2930:00 - 2995:00

compute to answer new problems. And

## 2995:00 - 3055:00

after this I joined uh Google DeepMind

## 3055:00 - 3110:00

and really joining a company that wanted

## 3110:00 - 3150:00

to say how are we going to take these

## 3150:00 - 3190:00

powerful technologies and all kind of

## 3190:00 - 3225:00

these ideas and we they were becoming

## 3225:00 - 3260:00

very very readily apparent how powerful

## 3260:00 - 3285:00

these technologies were with

## 3285:00 - 3315:00

applications

## 3315:00 - 3365:00

uh to especially games but also to

## 3365:00 - 3395:00

things like data centers and others. How

## 3395:00 - 3415:00

are we going to take these technologies

## 3415:00 - 3450:00

and use them to advance science and

## 3450:00 - 3500:00

really push forward scientific frontier?

## 3500:00 - 3535:00

And how can we do this in an industrial

## 3535:00 - 3580:00

setting with an incredibly fast pace

## 3580:00 - 3610:00

working with some really smart people

## 3610:00 - 3640:00

working with great computer resources

## 3640:00 - 3675:00

and with all that you darn well better

## 3675:00 - 3715:00

make some progress and it's been really

## 3715:00 - 3750:00

really fun and the fact that I'm on this

## 3750:00 - 3775:00

stage indicates that we made some

## 3775:00 - 3825:00

progress and I think it really the

## 3825:00 - 3865:00

guiding principle for me has that when

## 3865:00 - 3940:00

we do this work that ultimately we are

## 3940:00 - 3965:00

building tools that will enable

## 3965:00 - 4000:00

scientists to make discoveries.

## 4000:00 - 4040:00

And what I think is really heartening

## 4040:00 - 4065:00

about the work we've done and the part

## 4065:00 - 4120:00

that really I think still just resonates

## 4120:00 - 4165:00

with me at my core is there about I

## 4165:00 - 4220:00

think 35,000 citations of Alphafold. But

## 4220:00 - 4270:00

within that is there are tens of

## 4270:00 - 4310:00

thousands of examples of people using

## 4310:00 - 4355:00

our tools to do science that I couldn't

## 4355:00 - 4405:00

do on my own but are using it to make

## 4405:00 - 4460:00

discoveries. be it vaccines, be it drug

## 4460:00 - 4500:00

development, be it how the body works.

## 4500:00 - 4515:00

And I think that's really really

## 4515:00 - 4560:00

exciting. And the part I want to talk to

## 4560:00 - 4590:00

you about today and the story I want to

## 4590:00 - 4645:00

tell you is a bit about the problem, a

## 4645:00 - 4670:00

bit about how we did it. And I think

## 4670:00 - 4715:00

especially the role of research and

## 4715:00 - 4740:00

machine learning research and the fact

## 4740:00 - 4770:00

that it isn't just off-the-shelf machine

## 4770:00 - 4800:00

learning and then I want to tell you a

## 4800:00 - 4830:00

little bit about what happens when you

## 4830:00 - 4870:00

make something great and how people use

## 4870:00 - 4915:00

it and what it does for the world. So,

## 4915:00 - 4940:00

I'll start with the world's shortest

## 4940:00 - 5010:00

biology lesson. The cell is complex.

## 5010:00 - 5065:00

Um, for people who have only studied

## 5065:00 - 5105:00

biology in high school or in college,

## 5105:00 - 5135:00

you might have this idea that the cell

## 5135:00 - 5170:00

is a couple parts that have labels

## 5170:00 - 5205:00

attached to them. And it's kind of

## 5205:00 - 5230:00

simple, but really it looks much more

## 5230:00 - 5265:00

like what you see on the screen. It's

## 5265:00 - 5315:00

dense. It's complex. Uh, in terms of

## 5315:00 - 5345:00

crowding, it's like the swimming pool on

## 5345:00 - 5405:00

the 4th of July and it's in full of

## 5405:00 - 5455:00

enormous complexity. Humans have about

## 5455:00 - 5500:00

20,000 different types of proteins.

## 5500:00 - 5525:00

Those are some of the blobs you see on

## 5525:00 - 5555:00

the screen. They come together to do

## 5555:00 - 5600:00

practically every function in your cell.

## 5600:00 - 5645:00

You can see that uh kind of green tail

## 5645:00 - 5710:00

is the psyllium of uh an ecoli. That's

## 5710:00 - 5745:00

how it moves around. And you can see in

## 5745:00 - 5775:00

fact how it moves around. And you can

## 5775:00 - 5800:00

see that thing that looks like it turns

## 5800:00 - 5845:00

and in fact it turns and drives this

## 5845:00 - 5875:00

motor. All of this is made of proteins.

## 5875:00 - 5925:00

When people say that DNA is the

## 5925:00 - 5950:00

instruction manual for life, well, this

## 5950:00 - 5995:00

is what it's telling you how to do. It's

## 5995:00 - 6025:00

telling you how to build these tiny

## 6025:00 - 6070:00

machines. And biology has evolved an

## 6070:00 - 6115:00

incredible mechanism to build the

## 6115:00 - 6150:00

machines it needs, literal nano

## 6150:00 - 6190:00

machines, and build them out of atoms.

## 6190:00 - 6220:00

And so your DNA gives you instructions

## 6220:00 - 6265:00

that say build a protein. Now you might

## 6265:00 - 6310:00

say your DNA is a line and so are

## 6310:00 - 6335:00

proteins in a certain sense. It's

## 6335:00 - 6370:00

instructions on how to attach one bead

## 6370:00 - 6410:00

after another where each bead is a

## 6410:00 - 6435:00

specific kind of molecular arrangement

## 6435:00 - 6500:00

of atoms. And you should wonder if I my

## 6500:00 - 6540:00

DNA is aligned and I am very much not

## 6540:00 - 6570:00

one-dimensional,

## 6570:00 - 6595:00

what happens in between? And the answer

## 6595:00 - 6645:00

is after you make this protein and

## 6645:00 - 6690:00

assemble it one piece at a time, it will

## 6690:00 - 6725:00

fold up spontaneously

## 6725:00 - 6770:00

into a shape like you've opened your

## 6770:00 - 6805:00

IKEA bookshelf and instead of having to

## 6805:00 - 6830:00

do the hard work, it simply builds

## 6830:00 - 6875:00

itself and you get this quite complex

## 6875:00 - 6915:00

structure. You can see quite typical

## 6915:00 - 6945:00

protein, a kynise for those of you who

## 6945:00 - 6980:00

are biologists in the audience over

## 6980:00 - 7010:00

there. And you can see this very complex

## 7010:00 - 7045:00

arrangement of atoms and that

## 7045:00 - 7100:00

arrangement is functional and and the

## 7100:00 - 7145:00

majority not everyone of the proteins uh

## 7145:00 - 7185:00

in your body undergo this transformation

## 7185:00 - 7220:00

and that is what functions and that is

## 7220:00 - 7255:00

incredibly small.

## 7255:00 - 7320:00

So light itself is a few hundred

## 7320:00 - 7365:00

nanometers in size and that's a few

## 7365:00 - 7400:00

nanometers in size. So it's smaller than

## 7400:00 - 7445:00

you can see in a microscope. And for a

## 7445:00 - 7475:00

long time scientists have wanted to

## 7475:00 - 7515:00

understand this structure because they

## 7515:00 - 7565:00

use it to predict how changes in that

## 7565:00 - 7620:00

protein might affect disease. How does

## 7620:00 - 7655:00

that work? How does biology work? Often

## 7655:00 - 7680:00

if you make a drug it is to interrupt

## 7680:00 - 7705:00

the function of a certain protein like

## 7705:00 - 7740:00

this one.

## 7740:00 - 7785:00

Now scientists have through an

## 7785:00 - 7825:00

incredible amount of cleverness figured

## 7825:00 - 7865:00

out the structure of lots of proteins

## 7865:00 - 7910:00

and it remains to this day exceptionally

## 7910:00 - 7945:00

difficult. Right? You shouldn't imagine

## 7945:00 - 7995:00

this as I want to determine the

## 7995:00 - 8030:00

structure of a protein. So I shall open

## 8030:00 - 8065:00

the lab protocol for protein structure

## 8065:00 - 8110:00

determination. I shall follow the steps.

## 8110:00 - 8170:00

It consists of cleverness of ideas of

## 8170:00 - 8200:00

finding many ways. In this case, I'm

## 8200:00 - 8235:00

describing one type of protein structure

## 8235:00 - 8270:00

prediction in or protein structure,

## 8270:00 - 8295:00

sorry, determination, experimental

## 8295:00 - 8330:00

measurement, where you convince that big

## 8330:00 - 8370:00

ugly molecule I just showed you to form

## 8370:00 - 8400:00

a regular crystal kind of like table

## 8400:00 - 8445:00

salt. No one has an easy recipe for

## 8445:00 - 8475:00

this. So, they try many things. They

## 8475:00 - 8530:00

have ideas and it's exceptionally

## 8530:00 - 8570:00

difficult and filled with failure like

## 8570:00 - 8610:00

many things in science.

## 8610:00 - 8670:00

And you're really looking at

## 8670:00 - 8700:00

kind of one way to get an idea of how

## 8700:00 - 8730:00

difficult this is. Just one kind of

## 8730:00 - 8760:00

ordinary paper that we were using. I

## 8760:00 - 8800:00

flipped to the back and it said, you

## 8800:00 - 8825:00

know, in their protocol, after more than

## 8825:00 - 8875:00

a year, crystals began to form. Right?

## 8875:00 - 8905:00

So, not only did they do all these hard

## 8905:00 - 8935:00

experiments, but they had to wait about

## 8935:00 - 8965:00

a year to find out if it worked. And

## 8965:00 - 8995:00

probably that year wasn't spent waiting.

## 8995:00 - 9020:00

It was trying a thousand other things

## 9020:00 - 9065:00

that didn't work as well.

## 9065:00 - 9110:00

Once you do that, you can take this to a

## 9110:00 - 9155:00

uh synretron, a modest thing. You can

## 9155:00 - 9190:00

see the cars rigging the outside of this

## 9190:00 - 9220:00

instrument so that you can shine

## 9220:00 - 9265:00

incredibly bright X-rays on it and get

## 9265:00 - 9300:00

what is called a defraction pattern and

## 9300:00 - 9345:00

you can solve that and you can deposit

## 9345:00 - 9380:00

it in what's called the PDB or the

## 9380:00 - 9415:00

protein datab bank. And one of the

## 9415:00 - 9455:00

things that enabled the work we did is

## 9455:00 - 9495:00

that scientists 50 years ago had the

## 9495:00 - 9535:00

foresight to say these are important,

## 9535:00 - 9580:00

these are hard. We should collect them

## 9580:00 - 9625:00

all in one place. So there's a data set

## 9625:00 - 9670:00

that represents ex essentially all the

## 9670:00 - 9720:00

academic output of protein structures in

## 9720:00 - 9765:00

the community and available to everyone.

## 9765:00 - 9815:00

So our work was on very public data.

## 9815:00 - 9850:00

About 200,000 protein structures are

## 9850:00 - 9895:00

known. They pretty regularly increase at

## 9895:00 - 9950:00

about 12,000 a year.

## 9950:00 - 9990:00

But this is much much smaller than the

## 9990:00 - 10020:00

need.

## 10020:00 - 10060:00

Getting the kind of input information,

## 10060:00 - 10100:00

the DNA that tells you about a protein

## 10100:00 - 10150:00

is much much much much easier. So

## 10150:00 - 10205:00

billions of protein sequences are being

## 10205:00 - 10245:00

discovered. About 3,000 times faster are

## 10245:00 - 10275:00

we learning about protein sequence than

## 10275:00 - 10310:00

protein structure.

## 10310:00 - 10360:00

Okay, that's all scientific content, but

## 10360:00 - 10405:00

I should talk to you about the little

## 10405:00 - 10435:00

thing we did which has this kind of

## 10435:00 - 10475:00

schematic diagram.

## 10475:00 - 10520:00

We wanted to build an AI system. In

## 10520:00 - 10540:00

fact, we didn't even care if it was an

## 10540:00 - 10585:00

AI system. That's one of the nice things

## 10585:00 - 10630:00

about uh working in AI for science is

## 10630:00 - 10655:00

you don't care how you solve it. If it

## 10655:00 - 10680:00

ended up being a computer program, if it

## 10680:00 - 10715:00

ended up being anything else, we want to

## 10715:00 - 10765:00

find some way to get from the left where

## 10765:00 - 10790:00

each of those letters represents a

## 10790:00 - 10825:00

specific building block of the protein

## 10825:00 - 10860:00

considered an order. We want to put

## 10860:00 - 10895:00

something in the middle in the alpha

## 10895:00 - 10925:00

fold and we want to end up with

## 10925:00 - 10960:00

something on the right. And you'll see

## 10960:00 - 10985:00

uh two structures there if you look

## 10985:00 - 11040:00

closely where the blue is our prediction

## 11040:00 - 11070:00

and the green is the experimental

## 11070:00 - 11100:00

structure that took someone a year or

## 11100:00 - 11130:00

two of effort. If you want to put an

## 11130:00 - 11180:00

economic value on it on the order of

## 11180:00 - 11215:00

$100,000

## 11215:00 - 11270:00

and you can see we were able to do this

## 11270:00 - 11315:00

and I want to tell you how

## 11315:00 - 11360:00

and there were really three components

## 11360:00 - 11390:00

to doing this or to do any machine

## 11390:00 - 11430:00

learning problem and you can say you

## 11430:00 - 11460:00

have data and you have compute and you

## 11460:00 - 11490:00

have research

## 11490:00 - 11545:00

and I feel like we tell too many stories

## 11545:00 - 11575:00

about the first two and not enough about

## 11575:00 - 11630:00

the third. In data, we had 200,000

## 11630:00 - 11665:00

protein structures. Everyone has the

## 11665:00 - 11695:00

same data.

## 11695:00 - 11745:00

In terms of compute, this isn't LLM

## 11745:00 - 11810:00

scale. It's the final model itself was

## 11810:00 - 11865:00

128 TPU v3 cores, roughly equivalent to

## 11865:00 - 11925:00

a GPU per core for two weeks. This is

## 11925:00 - 11975:00

again within the scope of say academic

## 11975:00 - 12025:00

resources but it's worth saying really

## 12025:00 - 12050:00

most of your compute when you think

## 12050:00 - 12075:00

about how much compute you need don't

## 12075:00 - 12100:00

get distracted by the number for the

## 12100:00 - 12145:00

final model the real cost of compute is

## 12145:00 - 12200:00

the cost of ideas that didn't work all

## 12200:00 - 12230:00

the things you had to do to get there

## 12230:00 - 12260:00

and then finally research and I would

## 12260:00 - 12320:00

say this is all but about two people

## 12320:00 - 12350:00

that worked on this it's a small group

## 12350:00 - 12410:00

of people that end up doing this So

## 12410:00 - 12435:00

really when you look at these machine

## 12435:00 - 12470:00

learning breakthroughs they're probably

## 12470:00 - 12520:00

fewer people than you imagine and really

## 12520:00 - 12555:00

this is where our work was

## 12555:00 - 12585:00

differentiated. We came up with a new

## 12585:00 - 12650:00

set of ideas on how do we bring machine

## 12650:00 - 12690:00

learning to this problem and I can say

## 12690:00 - 12735:00

earlier systems largely based on

## 12735:00 - 12775:00

convolutional neural networks did okay.

## 12775:00 - 12810:00

They certainly made progress. If you

## 12810:00 - 12835:00

replace that with a transformer you're

## 12835:00 - 12875:00

honestly about the same. If you take the

## 12875:00 - 12905:00

ideas of a transformer and much

## 12905:00 - 12950:00

experimentation and many more ideas,

## 12950:00 - 12995:00

then that's when you start to get real

## 12995:00 - 13055:00

change. And in almost all the AI systems

## 13055:00 - 13095:00

you can see today, a tremendous amount

## 13095:00 - 13125:00

of research and ideas and what I would

## 13125:00 - 13175:00

call midscale ideas are involved. It

## 13175:00 - 13210:00

isn't just about the headlines where

## 13210:00 - 13260:00

people will say transformers,

## 13260:00 - 13300:00

you know, scaling, test time inference.

## 13300:00 - 13330:00

These are all important but they're one

## 13330:00 - 13380:00

of many ingredients in a really powerful

## 13380:00 - 13430:00

system and in fact we can measure how

## 13430:00 - 13485:00

much our research was worth. So someone

## 13485:00 - 13520:00

Alphafold 2 is the system that is quite

## 13520:00 - 13560:00

famous the one that uh was quite a large

## 13560:00 - 13585:00

improvement. Alpha fold one was the best

## 13585:00 - 13625:00

in the world but someone did uh the

## 13625:00 - 13665:00

Alcesi lab did a very uh careful

## 13665:00 - 13720:00

experiment where they took Alphold 2 the

## 13720:00 - 13770:00

architecture and they trained it on 1%

## 13770:00 - 13810:00

of the available data and they could

## 13810:00 - 13855:00

show that alpha fold 2 trained on 1% of

## 13855:00 - 13900:00

the data was as accurate or more

## 13900:00 - 13935:00

accurate as alphafold one which was the

## 13935:00 - 13975:00

state-of-the-art system previously. So

## 13975:00 - 14005:00

there's a very clean thing that says

## 14005:00 - 14060:00

that the third uh the third of these

## 14060:00 - 14100:00

ingredients research was worth a

## 14100:00 - 14130:00

hundfold of the first of these

## 14130:00 - 14175:00

ingredients data. And I think this is

## 14175:00 - 14225:00

generally really really important that

## 14225:00 - 14265:00

one of the big as you're all thinking as

## 14265:00 - 14300:00

you're all in startups or thinking about

## 14300:00 - 14360:00

startups think about the amount to which

## 14360:00 - 14440:00

ideas research discoveries amplify data

## 14440:00 - 14475:00

amplify compute they work together with

## 14475:00 - 14505:00

it we wouldn't want to use less data

## 14505:00 - 14530:00

than we have we wouldn't want to use

## 14530:00 - 14585:00

less compute than we have available but

## 14585:00 - 14625:00

ideas are a core component when you're

## 14625:00 - 14650:00

doing machine learning research and they

## 14650:00 - 14695:00

really helped to transform the world.

## 14695:00 - 14730:00

>> YC's Next Batch is now taking

## 14730:00 - 14770:00

applications. Got a startup in you?

## 14770:00 - 14820:00

Apply at y combinator.com/apply.

## 14820:00 - 14855:00

It's never too early. And filling out

## 14855:00 - 14905:00

the app will level up your idea. Okay,

## 14905:00 - 14940:00

back to the video. We can even go back

## 14940:00 - 14970:00

and we can do ablations and we can say

## 14970:00 - 15000:00

what parts matter. And don't focus too

## 15000:00 - 15030:00

much on the details. We pulled this from

## 15030:00 - 15075:00

our paper. You can see here this is the

## 15075:00 - 15105:00

difference compared to the baseline. And

## 15105:00 - 15145:00

you take either of those and you can see

## 15145:00 - 15175:00

that each of the ideas that you might

## 15175:00 - 15205:00

remove from our final system kind of

## 15205:00 - 15250:00

discreet identifiable ideas some of

## 15250:00 - 15305:00

which were incredibly popular research

## 15305:00 - 15345:00

areas within the field like this work

## 15345:00 - 15370:00

came out and a part of it was

## 15370:00 - 15425:00

equivariant and people said equivariance

## 15425:00 - 15455:00

that is the answer alphafold is an

## 15455:00 - 15490:00

equivariant system and it's great we

## 15490:00 - 15525:00

must do more research on equivarians to

## 15525:00 - 15570:00

get even more great systems well I was

## 15570:00 - 15630:00

very confused by this because the sixth

## 15630:00 - 15680:00

uh row there no IPA invariant point

## 15680:00 - 15705:00

attention that removes all the

## 15705:00 - 15760:00

equavariance in alpha fold and it hurts

## 15760:00 - 15810:00

a bit but only a bit. Alpha fold itself

## 15810:00 - 15850:00

on this GDT scale that you can see on

## 15850:00 - 15900:00

the left graph. Alphafold 2 was about 30

## 15900:00 - 15955:00

GDT better than alphafold one and

## 15955:00 - 15990:00

equivariance explains two or three of

## 15990:00 - 16040:00

this. It isn't about one idea. It's

## 16040:00 - 16080:00

about many midscale ideas that add up to

## 16080:00 - 16125:00

a transformative system. And it's very

## 16125:00 - 16145:00

very important when you're building

## 16145:00 - 16185:00

these systems to think about what we

## 16185:00 - 16215:00

would call in this context biological

## 16215:00 - 16250:00

relevance. We would have ideas that were

## 16250:00 - 16300:00

better. We kind of got our system

## 16300:00 - 16360:00

grinding 1% at a time. But what really

## 16360:00 - 16390:00

mattered was when we crossed the

## 16390:00 - 16425:00

accuracy that it mattered to an

## 16425:00 - 16455:00

experimental biologist who didn't care

## 16455:00 - 16495:00

about machine learning. And you have to

## 16495:00 - 16525:00

get there through a lot of work and a

## 16525:00 - 16560:00

lot of effort. And when you do, it is

## 16560:00 - 16605:00

incredibly transformative. And we can

## 16605:00 - 16645:00

measure against uh this axis where the

## 16645:00 - 16680:00

dark blue axis the other systems

## 16680:00 - 16705:00

available at the time. And this was

## 16705:00 - 16750:00

assessed. Protein structure prediction

## 16750:00 - 16815:00

is in some ways far ahead of uh LLMs or

## 16815:00 - 16845:00

the general machine learning space and

## 16845:00 - 16895:00

having blind assessment. Since 1994,

## 16895:00 - 16920:00

every two years, everyone interested in

## 16920:00 - 16955:00

predicting the structure of proteins

## 16955:00 - 16980:00

gets together and predicts the structure

## 16980:00 - 17010:00

of a hundred proteins whose answer isn't

## 17010:00 - 17035:00

known to anyone except the research

## 17035:00 - 17070:00

group that just solved it, right?

## 17070:00 - 17100:00

Unpublished. And so, you really do know

## 17100:00 - 17140:00

what works. And we had about a third of

## 17140:00 - 17180:00

the error of any other group on this

## 17180:00 - 17225:00

assessment. But it matters because once

## 17225:00 - 17250:00

you are working on problems in which you

## 17250:00 - 17275:00

don't know the answer, you get to really

## 17275:00 - 17320:00

measure how good things are. And you can

## 17320:00 - 17360:00

really find that a lot of systems don't

## 17360:00 - 17405:00

live up to what people believe over the

## 17405:00 - 17435:00

course of their research. And because

## 17435:00 - 17470:00

even if you have a benchmark, we all

## 17470:00 - 17520:00

overfit to our ideas to the benchmark,

## 17520:00 - 17560:00

right? Unless you have held out. And in

## 17560:00 - 17605:00

fact, the problems you have in the real

## 17605:00 - 17635:00

world are almost always harder than the

## 17635:00 - 17665:00

problems you train on, right? Because

## 17665:00 - 17695:00

you have to learn from much data and you

## 17695:00 - 17735:00

apply it to very important singular

## 17735:00 - 17770:00

problems. So it is very very important

## 17770:00 - 17805:00

that you measure well both as you're

## 17805:00 - 17840:00

developing and when people are trying to

## 17840:00 - 17870:00

decide whether they should use your

## 17870:00 - 17910:00

system. External benchmarks are

## 17910:00 - 17960:00

absolutely critical to figuring out what

## 17960:00 - 18000:00

works and that's what really helps drive

## 18000:00 - 18035:00

the world forward. So just some

## 18035:00 - 18065:00

wonderful examples of this is typical

## 18065:00 - 18095:00

performance for us. These are blind

## 18095:00 - 18130:00

predictions. You can see they're pretty

## 18130:00 - 18170:00

darn good. also important we made it

## 18170:00 - 18200:00

available and we thought it was and we

## 18200:00 - 18225:00

did a lot of assessment but we decided

## 18225:00 - 18255:00

that it was very important to make it

## 18255:00 - 18285:00

available in two ways. One is that we

## 18285:00 - 18305:00

open source the code and we actually

## 18305:00 - 18330:00

open sourced the code about a week

## 18330:00 - 18375:00

before we released a database of

## 18375:00 - 18405:00

predictions starting originally at

## 18405:00 - 18440:00

300,000 predictions and later going to

## 18440:00 - 18495:00

200 million essentially every protein um

## 18495:00 - 18525:00

from an organism whose genome has been

## 18525:00 - 18565:00

sequenced. And this made an enormous

## 18565:00 - 18580:00

difference. And one of the most

## 18580:00 - 18610:00

interesting kind of sociological things

## 18610:00 - 18650:00

is this huge difference between when we

## 18650:00 - 18670:00

released a piece of code that

## 18670:00 - 18720:00

specialists could use and we got some

## 18720:00 - 18745:00

information and then when we made it

## 18745:00 - 18810:00

available to the world in this database

## 18810:00 - 18855:00

form. It was really interesting kind of

## 18855:00 - 18875:00

you know you release something and every

## 18875:00 - 18910:00

day you check Twitter to find out or

## 18910:00 - 18965:00

check X to find out what's going on. And

## 18965:00 - 19020:00

what we would really see is even after

## 19020:00 - 19065:00

that CASP assessment, I would say that

## 19065:00 - 19095:00

the structure predictors were convinced

## 19095:00 - 19145:00

this obviously was this enormous advance

## 19145:00 - 19180:00

solved the problem. But general

## 19180:00 - 19205:00

biologists, the people we wanted to use,

## 19205:00 - 19220:00

the people who didn't care about

## 19220:00 - 19240:00

structure prediction, they cared about

## 19240:00 - 19280:00

proteins to do their experiments, they

## 19280:00 - 19305:00

weren't as sure. They said, "Well, maybe

## 19305:00 - 19350:00

CASP was easy. I don't know." And then

## 19350:00 - 19385:00

this database came out and people got

## 19385:00 - 19440:00

curious and they clicked in and the

## 19440:00 - 19475:00

amount to which the proof was social was

## 19475:00 - 19525:00

extraordinary that people would look and

## 19525:00 - 19565:00

say how did deep mind get access to my

## 19565:00 - 19610:00

unpublished structure. you know, this

## 19610:00 - 19635:00

moment at which they really believed it

## 19635:00 - 19690:00

that everyone had a a protein either had

## 19690:00 - 19720:00

a protein that they hadn't solved or had

## 19720:00 - 19750:00

a friend who had a protein that was

## 19750:00 - 19785:00

unpublished and they could compare and

## 19785:00 - 19815:00

that's what really made the difference.

## 19815:00 - 19840:00

And having this database, this

## 19840:00 - 19895:00

accessibility, this ease led everyone to

## 19895:00 - 19940:00

try it and figure out how it worked.

## 19940:00 - 19985:00

Word of mouth is really how this trust

## 19985:00 - 20010:00

is built. And you can kind of see some

## 20010:00 - 20055:00

of these testimonials, right? I wrestled

## 20055:00 - 20100:00

for three to four months trying to do

## 20100:00 - 20155:00

this uh scientific task. You know, this

## 20155:00 - 20190:00

morning I got an alpha fold prediction

## 20190:00 - 20245:00

and now it's much better. I want my time

## 20245:00 - 20295:00

back, right? You know, you really

## 20295:00 - 20325:00

appreciate alphafold when you run it on

## 20325:00 - 20370:00

a protein that for a year refused to get

## 20370:00 - 20400:00

expressed and purified. Meaning they for

## 20400:00 - 20420:00

a year they couldn't even get the

## 20420:00 - 20460:00

material to start experiments. These are

## 20460:00 - 20485:00

really important. When you build the

## 20485:00 - 20515:00

right tool, when you solve the right

## 20515:00 - 20570:00

problem, it matters and it changes the

## 20570:00 - 20620:00

lives of people who are doing things not

## 20620:00 - 20660:00

that you would do but building on top of

## 20660:00 - 20690:00

your work. And I think it's just

## 20690:00 - 20725:00

extraordinary to see these and the

## 20725:00 - 20765:00

number of people I talked to. The time

## 20765:00 - 20795:00

that I really knew this tool mattered.

## 20795:00 - 20820:00

In fact, there was a special issue of

## 20820:00 - 20855:00

science on the nuclear pore complex a

## 20855:00 - 20915:00

few months after the tool came out. And

## 20915:00 - 20945:00

the special issue was all about this

## 20945:00 - 20985:00

particular very large kind of several

## 20985:00 - 21040:00

hundred protein system. And three out of

## 21040:00 - 21095:00

the four uh papers in science about this

## 21095:00 - 21120:00

made extensive use of alpha fold. I

## 21120:00 - 21145:00

think I counted over a hundred mentions

## 21145:00 - 21185:00

of the word alphafold in science and we

## 21185:00 - 21210:00

had nothing to do with it. We didn't

## 21210:00 - 21235:00

know it was happening. We weren't

## 21235:00 - 21275:00

collaborating. It was just people doing

## 21275:00 - 21305:00

new science on top of the tools we had

## 21305:00 - 21330:00

built and that is the greatest feeling

## 21330:00 - 21370:00

in the world. And in fact, users do the

## 21370:00 - 21415:00

darnest things. They will use tools in

## 21415:00 - 21475:00

ways you didn't know were possible. The

## 21475:00 - 21525:00

tweet on the left from Yoshaka Morowaki

## 21525:00 - 21560:00

came out two days after our code was

## 21560:00 - 21595:00

available. We had predicted the

## 21595:00 - 21625:00

structure of individual proteins, but we

## 21625:00 - 21655:00

consider we were working on building a

## 21655:00 - 21680:00

system that would predict how proteins

## 21680:00 - 21725:00

came together. But uh this researcher

## 21725:00 - 21755:00

said, "Well, I have alphapold. Why don't

## 21755:00 - 21785:00

I just put two proteins together and

## 21785:00 - 21815:00

I'll put something in between?" You

## 21815:00 - 21835:00

could think of this as prompt

## 21835:00 - 21875:00

engineering but for proteins. And

## 21875:00 - 21900:00

suddenly they find out this is the best

## 21900:00 - 21930:00

protein interaction prediction in the

## 21930:00 - 21970:00

world, right? That when you train on

## 21970:00 - 22010:00

these a really really powerful system,

## 22010:00 - 22050:00

it will have additional in some sense

## 22050:00 - 22085:00

emergent skills as long as they're

## 22085:00 - 22120:00

aligned. People started to find all

## 22120:00 - 22185:00

sorts of problems that Alphafold would

## 22185:00 - 22225:00

work on that we hadn't anticipated. It

## 22225:00 - 22275:00

was so interesting to see the field of

## 22275:00 - 22315:00

science in real time reacting to the

## 22315:00 - 22345:00

existence of these tools, finding their

## 22345:00 - 22400:00

limitations, finding their possibilities

## 22400:00 - 22445:00

and this continues and people do all

## 22445:00 - 22480:00

sorts of exciting work be it in protein

## 22480:00 - 22530:00

design be it in others on top of either

## 22530:00 - 22565:00

the ideas and often the systems we have

## 22565:00 - 22650:00

built. One application that really uh I

## 22650:00 - 22685:00

thought was really important is that

## 22685:00 - 22715:00

people have started to learn how to use

## 22715:00 - 22770:00

it to engineer big proteins or to use it

## 22770:00 - 22805:00

in part of and I want to tell this story

## 22805:00 - 22830:00

for two reasons. One is I think it's a

## 22830:00 - 22865:00

really cool application but the second

## 22865:00 - 22900:00

is how it really changes the work of

## 22900:00 - 22950:00

science and often people will say

## 22950:00 - 22985:00

science is all about experiments and

## 22985:00 - 23025:00

validation. So it's great that you have

## 23025:00 - 23060:00

all these alpha fold predictions. Now

## 23060:00 - 23090:00

all we have to do is solve all the

## 23090:00 - 23145:00

proteins the classic way so that we can

## 23145:00 - 23175:00

tell whether your predictions are right

## 23175:00 - 23225:00

or wrong. And they're right about one

## 23225:00 - 23260:00

thing. Science is about experiments.

## 23260:00 - 23285:00

Science is about doing these

## 23285:00 - 23315:00

experiments.

## 23315:00 - 23360:00

But they're wrong about another thing.

## 23360:00 - 23405:00

Um science is about making hypotheses

## 23405:00 - 23460:00

and testing them not about the structure

## 23460:00 - 23485:00

of a particular protein. In this case,

## 23485:00 - 23535:00

the question was they took this protein

## 23535:00 - 23575:00

on the left called the contractile

## 23575:00 - 23605:00

inject injection system, but that's a

## 23605:00 - 23630:00

mouthful. They like to call it the

## 23630:00 - 23670:00

molecular syringe. And what it does is

## 23670:00 - 23725:00

it attaches to a cell and injects a

## 23725:00 - 23760:00

protein into it. And the scientists at

## 23760:00 - 23825:00

the Jang Lab at uh MIT were saying,

## 23825:00 - 23885:00

well, can we use this protein

## 23885:00 - 23920:00

to do targeted drug delivery? Can we use

## 23920:00 - 23970:00

it to get gene editors like cast 9 into

## 23970:00 - 24015:00

the cell? They tried over a hundred

## 24015:00 - 24050:00

methods to figure out how to take this

## 24050:00 - 24070:00

protein, which they didn't have a

## 24070:00 - 24095:00

structure of. This is just kind of a

## 24095:00 - 24140:00

rendition after the fact, and say, how

## 24140:00 - 24175:00

can we change what it recognizes? I

## 24175:00 - 24200:00

think it's originally involved in plant

## 24200:00 - 24230:00

defense or something like that, and they

## 24230:00 - 24250:00

didn't know how to do it. And they ran

## 24250:00 - 24280:00

an alpha fold prediction. You can see

## 24280:00 - 24300:00

the one on the left. I wouldn't even say

## 24300:00 - 24335:00

it's a great alpha fold prediction, but

## 24335:00 - 24360:00

almost immediately they looked at that

## 24360:00 - 24395:00

and said, "Wait a minute. those legs at

## 24395:00 - 24430:00

the bottom are how it must recognize and

## 24430:00 - 24475:00

attach to cells. Why don't we just

## 24475:00 - 24520:00

replace those with a designed protein?

## 24520:00 - 24545:00

And so almost immediately as soon as

## 24545:00 - 24570:00

they got the alpha fold prediction, they

## 24570:00 - 24615:00

re-engineered to add this design protein

## 24615:00 - 24680:00

that you see in red uh to target a new

## 24680:00 - 24750:00

type of cell. And they take this system

## 24750:00 - 24790:00

and then they show in fact that they can

## 24790:00 - 24835:00

choose cells within a mouse and they can

## 24835:00 - 24870:00

inject proteins in this case fluorescent

## 24870:00 - 24905:00

proteins. So there you'll see the color

## 24905:00 - 24930:00

and they can target the cells they want

## 24930:00 - 24970:00

within a mouse brain. And so they are

## 24970:00 - 25010:00

using this to develop a new type of

## 25010:00 - 25035:00

system

## 25035:00 - 25085:00

of targeted drug discovery. And we see

## 25085:00 - 25120:00

many more examples. We see some in which

## 25120:00 - 25165:00

scientists are using this tool to try

## 25165:00 - 25195:00

thousands and thousands of interactions

## 25195:00 - 25235:00

to figure out which ones are likely to

## 25235:00 - 25270:00

be the case. In fact, discovered a new

## 25270:00 - 25315:00

component of how eggs and sperm come

## 25315:00 - 25355:00

together in fertilization. Many many of

## 25355:00 - 25385:00

these discoveries that are built on top

## 25385:00 - 25445:00

of this. And I like to think that our

## 25445:00 - 25485:00

work made the whole field of what's

## 25485:00 - 25515:00

called structural biology, biology that

## 25515:00 - 25560:00

deals with structures, you know, five or

## 25560:00 - 25615:00

10% faster. But the amount to which that

## 25615:00 - 25665:00

matters for the world is enormous and we

## 25665:00 - 25720:00

will have more of these discoveries. And

## 25720:00 - 25755:00

I think ultimately structure prediction

## 25755:00 - 25785:00

and larger AI for science should be

## 25785:00 - 25820:00

thought of as an incredible capability

## 25820:00 - 25855:00

to be an amplifier for the work of

## 25855:00 - 25895:00

experimentalists that we start from

## 25895:00 - 25925:00

these scattered observations, these

## 25925:00 - 25970:00

natural data. This is our equivalent of

## 25970:00 - 26005:00

all the words on the internet. And then

## 26005:00 - 26030:00

we train a general model that

## 26030:00 - 26070:00

understands the rules underneath it and

## 26070:00 - 26110:00

can fill in the rest of the picture. And

## 26110:00 - 26140:00

I think that we will continue to see

## 26140:00 - 26170:00

this pattern and it will get more

## 26170:00 - 26195:00

general that we will find the right

## 26195:00 - 26250:00

foundational data sources in order to do

## 26250:00 - 26285:00

this. And I think the other thing that

## 26285:00 - 26345:00

has really been a property is that you

## 26345:00 - 26380:00

start where you have data but then you

## 26380:00 - 26430:00

find what problems it can be applied to.

## 26430:00 - 26475:00

And so we find enormous advance,

## 26475:00 - 26510:00

enormous capability to understand

## 26510:00 - 26550:00

interactions in the cell or others that

## 26550:00 - 26590:00

are downstream of extracting the

## 26590:00 - 26650:00

scientific content of these predictions

## 26650:00 - 26685:00

and then the rules they use can be

## 26685:00 - 26715:00

adapted to new purposes. And I think

## 26715:00 - 26750:00

this is really where we see the

## 26750:00 - 26795:00

foundational model aspect of alpha fold

## 26795:00 - 26830:00

or other narrow systems. And in fact, I

## 26830:00 - 26860:00

think we will start to see this on more

## 26860:00 - 26900:00

general systems, be them LLMs or others,

## 26900:00 - 26925:00

that we will find more and more

## 26925:00 - 26970:00

scientific knowledge within them and

## 26970:00 - 27005:00

we'll use them for important important

## 27005:00 - 27050:00

purposes. And I think this is really

## 27050:00 - 27080:00

where this is going. And I think the

## 27080:00 - 27130:00

most exciting question in AI for science

## 27130:00 - 27175:00

is how general will it be. Will we find

## 27175:00 - 27210:00

a couple of narrow places where we have

## 27210:00 - 27250:00

transformative impact or will we have

## 27250:00 - 27285:00

very very broad systems? And I expect it

## 27285:00 - 27320:00

will ultimately be the latter as we

## 27320:00+

figure it out. Thank you.

