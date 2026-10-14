---
source: https://www.youtube.com/watch?v=QUIgIBx5NDQ
title: "Generative AI 101: Tokens, Pre-training, Fine-tuning, Reasoning — With
  SemiAnalysis CEO Dylan Patel"
author: Alex Kantrowitz
date: 2025-04-23
views: 7910
description: >-
  Dylan Patel is the founder and CEO of SemiAnalysis. He joins Big Technology
  Podcast to explain how generative AI work, explaining the inner workings of
  tokens, pre-training, fine-tuning, open source, and reasoning. We also cover
  DeepSeek’s efficiency breakthrough, the race to build colossal AI data
  centers, and what GPT-5’s hybrid training approach could unlock. Hit play for
  a masterclass you’ll want to send to every friend puzzled (or excited) about
  the future of AI.


  Chapters: 


  00:00 - Introduction to Generative AI with Dylan Patel

  02:00 - Basics of AI Model Training

  04:30 - Understanding Tokens and Word Representation

  07:00 - How Models Process Language Patterns

  10:00 - Attention Mechanisms and Context Understanding

  13:00 - Pre-Training: Learning from Internet Data

  16:00 - Loss Minimization and Learning Processes

  19:00 - Why GPUs Are Perfect for AI Computation

  22:00 - Post-Training and Model Personalities

  25:00 - Reasoning: How Modern AI Models Think

  28:00 - The Growing Efficiency of AI Models

  31:00 - Data Center Build-Outs Despite Increasing Efficiency

  34:00 - The Future of GPT-5 and AI Development
tags:
  - generative AI
  - tokenization
  - pre-training
  - post-training
  - loss minimization
  - attention mechanism
  - embeddings
  - transformers
  - NVIDIA GPU
  - matrix multiplication
  - reinforcement learning
  - human feedback
  - reasoning models
  - model efficiency
  - scaling laws
  - DeepSeek
  - GPT-5
  - data centers
  - vector space
  - context window
  - fine-tuning
  - RLHF
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T21:01:06.101Z
---

# Generative AI 101: Tokens, Pre-training, Fine-tuning, Reasoning — With SemiAnalysis CEO Dylan Patel

## 00:00 - 25:00

If you've ever wondered how generative

## 25:00 - 65:00

AI works and where the technology is

## 65:00 - 105:00

heading, this episode is for you. We're

## 105:00 - 135:00

going to explain the basics of the

## 135:00 - 165:00

technology and then catch up with

## 165:00 - 205:00

modern-day advances like reasoning to

## 205:00 - 235:00

help you understand exactly how it does

## 235:00 - 275:00

what it does and where it might advance

## 275:00 - 305:00

in the future. That's coming up with

## 305:00 - 340:00

semi analysis founder and chief analyst

## 340:00 - 390:00

Dylan Patel right after this. Welcome to

## 390:00 - 420:00

Big Technology Podcast, a show for

## 420:00 - 465:00

coolheaded and nuanced conversation of

## 465:00 - 500:00

the tech world and beyond. We're joined

## 500:00 - 540:00

today by semi analysis founder and chief

## 540:00 - 580:00

analyst Dylan Patel, a leading expert in

## 580:00 - 620:00

semiconductor and generative AI research

## 620:00 - 640:00

and someone I've been looking forward to

## 640:00 - 700:00

speaking with for a long time now. I

## 700:00 - 730:00

want this to be an episode that a helps

## 730:00 - 770:00

people learn how generative AI works and

## 770:00 - 810:00

b is an episode that people will send to

## 810:00 - 845:00

their friends to explain to them how

## 845:00 - 870:00

generative AI works. I've had a couple

## 870:00 - 905:00

of those that I've been sending to my

## 905:00 - 935:00

friends uh and colleagues and

## 935:00 - 980:00

counterparts about what is going on

## 980:00 - 1020:00

within generative AI. That includes one

## 1020:00 - 1055:00

this 3 and 1/2 hour long video from

## 1055:00 - 1095:00

Andre Karpathy explaining everything

## 1095:00 - 1125:00

about training large language models.

## 1125:00 - 1155:00

And the second one is a great episode

## 1155:00 - 1185:00

that Dylan and Nathan Lambert from the

## 1185:00 - 1230:00

Allen Institute of AI did uh with Lex

## 1230:00 - 1275:00

Freiedman. Both of those 3 hours plus.

## 1275:00 - 1325:00

So I want to do it ours in an hour. Uh,

## 1325:00 - 1360:00

and I'm very excited to begin. So,

## 1360:00 - 1390:00

Dylan, it's great to see you and welcome

## 1390:00 - 1425:00

to the show. Thank you for having me.

## 1425:00 - 1445:00

Great to have you here. Let's just start

## 1445:00 - 1490:00

with tokens. Can you explain how the how

## 1490:00 - 1540:00

AI researchers basically take words and

## 1540:00 - 1580:00

then give them numerical representations

## 1580:00 - 1605:00

and parts of words and give them

## 1605:00 - 1645:00

numerical representations? So, what are

## 1645:00 - 1700:00

tokens? Tokens are are in fact like

## 1700:00 - 1735:00

chunks of words, right? Uh, in in the

## 1735:00 - 1755:00

human way, you can think of like

## 1755:00 - 1790:00

syllables, right? Um, syllables are

## 1790:00 - 1820:00

often, you know, viewed as like a chunks

## 1820:00 - 1865:00

of word. Um, they have some meaning. Um,

## 1865:00 - 1910:00

it's the base level of of of speaking,

## 1910:00 - 1940:00

right? Is is syllables, right? Now, for

## 1940:00 - 1970:00

models, tokens are the base level of

## 1970:00 - 2020:00

output. They're all about like sort of

## 2020:00 - 2045:00

compressing, you know, sort of this is

## 2045:00 - 2090:00

the most efficient representation of

## 2090:00 - 2125:00

language. From my understanding, AI

## 2125:00 - 2145:00

models are very good at predicting

## 2145:00 - 2220:00

patterns. So if you give it 1 3 7 9 it

## 2220:00 - 2255:00

might know the next number is going to

## 2255:00 - 2305:00

be 11. And so what it's doing in with

## 2305:00 - 2340:00

tokens is taking words breaking them

## 2340:00 - 2380:00

down to their component parts assigning

## 2380:00 - 2420:00

them a numerical value and then

## 2420:00 - 2455:00

basically in its own word in its own

## 2455:00 - 2485:00

language learning to predict what number

## 2485:00 - 2520:00

comes next because computers are better

## 2520:00 - 2545:00

at numbers and then converting that

## 2545:00 - 2575:00

number back to text and that's what we

## 2575:00 - 2610:00

see come out. Is that is that accurate?

## 2610:00 - 2650:00

Yeah. And each individual token uh is

## 2650:00 - 2680:00

actually it's not just like one number,

## 2680:00 - 2715:00

right? It's multiple vectors. You could

## 2715:00 - 2750:00

think of like well the tokenizer needs

## 2750:00 - 2790:00

to learn king and queen are actually

## 2790:00 - 2830:00

extremely similar on on most in terms of

## 2830:00 - 2860:00

like the English language. Extremely

## 2860:00 - 2905:00

similar, right? Except there is like one

## 2905:00 - 2935:00

vector in which they're super different,

## 2935:00 - 2965:00

right? Because a king is a male and a fe

## 2965:00 - 2995:00

a queen is a female, right? And then

## 2995:00 - 3030:00

from there like you know in language

## 3030:00 - 3055:00

oftent times kings are considered

## 3055:00 - 3085:00

conquerors and and you know all these

## 3085:00 - 3105:00

other things and like these are just

## 3105:00 - 3130:00

like historical things right so a lot of

## 3130:00 - 3155:00

the text around them while they're both

## 3155:00 - 3210:00

like royal regal right like you know uh

## 3210:00 - 3245:00

monarchy etc there are many vectors in

## 3245:00 - 3275:00

which they differ so like it's not just

## 3275:00 - 3305:00

like converting a to a word into one

## 3305:00 - 3330:00

number right it's like converting it

## 3330:00 - 3375:00

into multiple vectors and each of these

## 3375:00 - 3405:00

vectors the model learns what it means

## 3405:00 - 3445:00

right um you don't initialize the model

## 3445:00 - 3490:00

with like hey you know king means

## 3490:00 - 3550:00

male uh monarch blah and it's associated

## 3550:00 - 3575:00

with like war and conquering because

## 3575:00 - 3600:00

that's what all the writing about kings

## 3600:00 - 3630:00

is on you know in history and all that

## 3630:00 - 3645:00

right like people don't talk about the

## 3645:00 - 3680:00

daily lives of kings that much or they

## 3680:00 - 3700:00

mostly talk about like their wars and

## 3700:00 - 3755:00

conquests and stuff um and so like there

## 3755:00 - 3785:00

will be each of these numbers in this

## 3785:00 - 3835:00

embedding space right will be assigned

## 3835:00 - 3865:00

over time as the model reads the

## 3865:00 - 3900:00

internet's text and trains on it'll

## 3900:00 - 3930:00

start to realize oh king and queen are

## 3930:00 - 3965:00

exactly similar on these vectors but

## 3965:00 - 3990:00

very different on these vectors and

## 3990:00 - 4020:00

these vectors aren't you don't

## 4020:00 - 4045:00

explicitly tell the model hey this is

## 4045:00 - 4070:00

what this vector is for but it could be

## 4070:00 - 4110:00

like you know it could be as much as

## 4110:00 - 4135:00

like one vector could be like is it a

## 4135:00 - 4160:00

building or not right and and it doesn't

## 4160:00 - 4185:00

actually know that you don't you don't

## 4185:00 - 4210:00

know that ahead of time it just happens

## 4210:00 - 4235:00

to in the latent space and then all

## 4235:00 - 4255:00

these vectors sort of relate to each

## 4255:00 - 4295:00

other but yeah these these numbers are

## 4295:00 - 4350:00

um are efficient representation of words

## 4350:00 - 4385:00

uh because you can do math on them right

## 4385:00 - 4405:00

you can you can multiply them you can

## 4405:00 - 4445:00

divide them you can run them through an

## 4445:00 - 4480:00

entire model whereas Whereas we're and

## 4480:00 - 4505:00

and your brain does something similar,

## 4505:00 - 4530:00

right? When it hears something, it

## 4530:00 - 4555:00

converts that into a frequency in your

## 4555:00 - 4585:00

ears and then that gets converted to

## 4585:00 - 4605:00

frequencies that should go through your

## 4605:00 - 4630:00

brain, right? This is this is the same

## 4630:00 - 4660:00

thing as a tokenizer, right? Um although

## 4660:00 - 4685:00

it's like obviously a very different

## 4685:00 - 4715:00

medium of compute, right? Ones and zeros

## 4715:00 - 4760:00

for for computers versus uh you know

## 4760:00 - 4785:00

binary and multiplication etc. being

## 4785:00 - 4820:00

more efficient whereas humans uh brains

## 4820:00 - 4870:00

are more like analog in nature and um

## 4870:00 - 4900:00

you know think more in waves and and

## 4900:00 - 4930:00

patterns in different ways. uh while

## 4930:00 - 4950:00

they are very different it is a

## 4950:00 - 4985:00

tokenizer right like language is not

## 4985:00 - 5030:00

actually how our brain thinks it's just

## 5030:00 - 5070:00

a representation for which it to you

## 5070:00 - 5130:00

know reason over yeah so that's crazy so

## 5130:00 - 5150:00

the tokens are the sufficient

## 5150:00 - 5180:00

representation of words but more than

## 5180:00 - 5220:00

that the models are also learning the

## 5220:00 - 5250:00

way that they are all all these words

## 5250:00 - 5295:00

are connected and that brings us to

## 5295:00 - 5325:00

pre-training from my understanding

## 5325:00 - 5385:00

pre-training is when you take the entire

## 5385:00 - 5420:00

basically the entire internet worth of

## 5420:00 - 5505:00

text and you use that to teach the model

## 5505:00 - 5555:00

these representations between each

## 5555:00 - 5595:00

token. So therefore like we talked about

## 5595:00 - 5640:00

if you gave if you gave a model the sky

## 5640:00 - 5690:00

is and the next word is typically blue

## 5690:00 - 5720:00

in in the pre-training which is

## 5720:00 - 5750:00

basically all of the English language

## 5750:00 - 5800:00

all or all of language on the internet

## 5800:00 - 5825:00

uh it should know that the next token is

## 5825:00 - 5850:00

blue. So what you do is you want to make

## 5850:00 - 5890:00

sure that when the model uh is

## 5890:00 - 5945:00

outputting information it's closely tied

## 5945:00 - 5990:00

to what that next value should be. Is

## 5990:00 - 6025:00

that is that a proper description of

## 6025:00 - 6060:00

what happens in pre-training? Yeah, I

## 6060:00 - 6085:00

think I think that's that's pretty

## 6085:00 - 6110:00

that's the objective function which is

## 6110:00 - 6165:00

just to reduce loss i.e. how often is

## 6165:00 - 6195:00

the token predicted incorrectly versus

## 6195:00 - 6225:00

correctly. Right. Right. So if it's it's

## 6225:00 - 6275:00

like this if you said the sky is red um

## 6275:00 - 6310:00

that's not the most probable outcome. So

## 6310:00 - 6335:00

that would be wrong. that text is on the

## 6335:00 - 6350:00

internet, right? Like because the

## 6350:00 - 6380:00

Martian sky is red and there's all these

## 6380:00 - 6405:00

books about Mars and sci-fi, right? So,

## 6405:00 - 6435:00

how does the model then learn how to,

## 6435:00 - 6460:00

you know, figure this out and in what

## 6460:00 - 6490:00

context is it accurate to say blue and

## 6490:00 - 6535:00

red, right? So, so I mean, um, first of

## 6535:00 - 6570:00

all, the model doesn't just output one

## 6570:00 - 6610:00

token, right? It outputs a distribution.

## 6610:00 - 6645:00

Um, it turns out the most the way most

## 6645:00 - 6685:00

people take it is they take the top, uh,

## 6685:00 - 6740:00

top K, i.e. the most high probability.

## 6740:00 - 6770:00

So, yes, blue is obviously the right

## 6770:00 - 6800:00

answer if you give it to anyone on this

## 6800:00 - 6835:00

planet. Um, but there are situations and

## 6835:00 - 6865:00

contexts where the sky is red is the

## 6865:00 - 6890:00

appropriate sentence. But that's not

## 6890:00 - 6925:00

just in isolation, right? It's like if

## 6925:00 - 6960:00

the prior passage is all about Mars and

## 6960:00 - 6980:00

all this and then all of a sudden it's

## 6980:00 - 7005:00

like and it's like a quote from a

## 7005:00 - 7040:00

Martian settler and it's like the sky is

## 7040:00 - 7060:00

and then the correct token is actually

## 7060:00 - 7095:00

red, right? The correct word. Um, and so

## 7095:00 - 7125:00

it has to know this through the

## 7125:00 - 7155:00

attention mechanism, right? Um, if it

## 7155:00 - 7190:00

was just the sky is blue, always you're

## 7190:00 - 7215:00

going to output blue because blue is

## 7215:00 - 7265:00

let's say 80% 90% 99% likely to be the

## 7265:00 - 7300:00

right option. But as you as you start to

## 7300:00 - 7335:00

add context about Mars or any other

## 7335:00 - 7355:00

planet, right, other planets have

## 7355:00 - 7385:00

different colored colored atmospheres, I

## 7385:00 - 7440:00

presume. Um you end up with this um

## 7440:00 - 7475:00

distribution starts to shift, right? If

## 7475:00 - 7540:00

if I add we're on Mars, the sky is, you

## 7540:00 - 7575:00

know, then then all of a sudden blue

## 7575:00 - 7610:00

goes from 99%, you know, in the prior

## 7610:00 - 7640:00

context window, right? The uh the text

## 7640:00 - 7665:00

that you sent to the model, the

## 7665:00 - 7695:00

attention of it, all of a sudden it

## 7695:00 - 7745:00

realizes the sky is blue uh preceded by

## 7745:00 - 7785:00

that the the stuff about Mars. Now,

## 7785:00 - 7810:00

blues rockets down to like, you know,

## 7810:00 - 7840:00

let's call it 20% probability and red

## 7840:00 - 7885:00

rockets up to 80% probability, right?

## 7885:00 - 7930:00

Um, now the model outputs that and then

## 7930:00 - 7970:00

most people just end up taking the top

## 7970:00 - 7995:00

probability and outputting it to the

## 7995:00 - 8040:00

user. Um, and and that's sort of like

## 8040:00 - 8070:00

how how does the model learn that is is

## 8070:00 - 8100:00

the attention mechanism, right? And this

## 8100:00 - 8160:00

is sort of the beauty. Yeah, the the uh

## 8160:00 - 8210:00

the attention mechanism is the beauty of

## 8210:00 - 8255:00

of modern sort of large language models.

## 8255:00 - 8285:00

It takes the relational value you know

## 8285:00 - 8315:00

in this vector space between every

## 8315:00 - 8365:00

single token right um so the sky you

## 8365:00 - 8395:00

know the sky is blue right like when I

## 8395:00 - 8425:00

think about it yes blue is the next

## 8425:00 - 8480:00

token after the sky is but in in a lot

## 8480:00 - 8515:00

of like older style models you would

## 8515:00 - 8540:00

have you would just predict the exact

## 8540:00 - 8580:00

next word so after sky obviously it's

## 8580:00 - 8600:00

you know it's it could be many things it

## 8600:00 - 8630:00

could be blue but it could also be like

## 8630:00 - 8670:00

uh scraper right you know skyscraper is

## 8670:00 - 8705:00

yeah that's that that that makes sense

## 8705:00 - 8750:00

um but what attention does is it it it

## 8750:00 - 8800:00

is it is um taking all of these various

## 8800:00 - 8845:00

values, the query, the key, the value um

## 8845:00 - 8865:00

which represents what you're looking

## 8865:00 - 8890:00

for, what you where you where you're

## 8890:00 - 8940:00

looking um and what what that value is

## 8940:00 - 8985:00

across the attention. Um and you're

## 8985:00 - 9030:00

you're you're calculating mathematically

## 9030:00 - 9060:00

what the relationship is between all of

## 9060:00 - 9095:00

these tokens. Um and so going back to

## 9095:00 - 9130:00

the king queen representation, right?

## 9130:00 - 9165:00

The way these two words interact is now

## 9165:00 - 9195:00

calculated, right? And the way that

## 9195:00 - 9225:00

every word in the entire passage you

## 9225:00 - 9270:00

sent is calculated uh is tied together.

## 9270:00 - 9305:00

Which is why models have like challenges

## 9305:00 - 9340:00

with like how long can you uh how many

## 9340:00 - 9360:00

documents can you send them, right?

## 9360:00 - 9395:00

Because if you're sending them, you

## 9395:00 - 9420:00

know, just the question like what color

## 9420:00 - 9450:00

is the sky? Okay, it only has to

## 9450:00 - 9475:00

calculate the attention between you know

## 9475:00 - 9495:00

those those words, right? But if you're

## 9495:00 - 9540:00

sending it like 30 books with like

## 9540:00 - 9565:00

insurance claims and all these other

## 9565:00 - 9590:00

things and you're like okay, figure out

## 9590:00 - 9630:00

what what's going on here. Um is this a

## 9630:00 - 9660:00

claim or not? Right? in in the insurance

## 9660:00 - 9680:00

context all of a sudden it's like okay

## 9680:00 - 9710:00

I've got to calculate the attention of

## 9710:00 - 9740:00

not just like the last five words to

## 9740:00 - 9770:00

each other but I have to calculate every

## 9770:00 - 9805:00

you know 50,000 words to each other

## 9805:00 - 9825:00

right which then ends up being a ton of

## 9825:00 - 9855:00

math back in the day actually the best

## 9855:00 - 9875:00

language models were a different

## 9875:00 - 9910:00

architecture entirely right um but then

## 9910:00 - 9950:00

at some point you know transformers

## 9950:00 - 9975:00

large language models sort of large

## 9975:00 - 10000:00

language models which are bas based on

## 10000:00 - 10035:00

transformers primarily uh rocketed past

## 10035:00 - 10060:00

in capabilities because they were able

## 10060:00 - 10085:00

to scale and because the hardware got

## 10085:00 - 10120:00

there um and then we were able to scale

## 10120:00 - 10155:00

them so much that we not to just put

## 10155:00 - 10195:00

like some text in them and not just a

## 10195:00 - 10225:00

lot of text or a lot of books but the

## 10225:00 - 10250:00

entire internet which you know one could

## 10250:00 - 10290:00

view the internet often times as a

## 10290:00 - 10330:00

microcosm of all human culture and

## 10330:00 - 10365:00

learnings and knowledge uh to many

## 10365:00 - 10390:00

extents because most books are on the

## 10390:00 - 10420:00

internet most papers are on the internet

## 10420:00 - 10440:00

um obviously there's a lot of things

## 10440:00 - 10475:00

missing on the internet um but this is

## 10475:00 - 10505:00

sort of this is the sort of modern you

## 10505:00 - 10545:00

know magic of like what what it was sort

## 10545:00 - 10565:00

of like three different things like

## 10565:00 - 10590:00

coming all together at once right an

## 10590:00 - 10630:00

efficient way for models to relate every

## 10630:00 - 10660:00

referred to each other the compute

## 10660:00 - 10700:00

necessary uh to scale the data large

## 10700:00 - 10725:00

enough and then someone actually like

## 10725:00 - 10755:00

pulling the trigger to do that right at

## 10755:00 - 10800:00

the scale that was you know got to the

## 10800:00 - 10820:00

point where it was useful right which

## 10820:00 - 10860:00

was sort of like GPT3.5

## 10860:00 - 10890:00

uh level or four level right where it

## 10890:00 - 10915:00

became extremely useful for normal

## 10915:00 - 10970:00

humans to use uh you know chat chat

## 10970:00 - 11010:00

models okay and so why is it called

## 11010:00 - 11085:00

pre-training so so pre-training is is is

## 11085:00 - 11120:00

sort of called that because it is what

## 11120:00 - 11160:00

happens happens, you know, before the

## 11160:00 - 11195:00

actual uh training of the model, right?

## 11195:00 - 11220:00

Uh the objective function in

## 11220:00 - 11250:00

pre-training is to just predict the next

## 11250:00 - 11280:00

token. Uh but predicting the next token

## 11280:00 - 11325:00

is not what humans want to use AIS for,

## 11325:00 - 11360:00

right? I want it to ask a question and

## 11360:00 - 11410:00

answer it. Uh but in in most cases,

## 11410:00 - 11440:00

asking a question does not necessarily

## 11440:00 - 11480:00

mean that the next most likely token is

## 11480:00 - 11515:00

is the answer, right? Often times it is

## 11515:00 - 11550:00

another question, right? Uh, for

## 11550:00 - 11595:00

example, if I ingested the entire SAT

## 11595:00 - 11620:00

um, you know, and I asked a question,

## 11620:00 - 11660:00

the next like five answer then all the

## 11660:00 - 11685:00

next tokens would be like A is this, B

## 11685:00 - 11715:00

is this, C is this, D is this. Like, no,

## 11715:00 - 11750:00

I just want the answer, right? Um, and

## 11750:00 - 11775:00

so pre-training is the reason it's

## 11775:00 - 11805:00

called pre-training is because you're

## 11805:00 - 11850:00

ingesting humongous volumes of text no

## 11850:00 - 11900:00

matter the use case, right? Um, and

## 11900:00 - 11935:00

you're learning the general patterns

## 11935:00 - 11970:00

across all of language, right? I don't

## 11970:00 - 11990:00

actually know that king and queen relate

## 11990:00 - 12020:00

to each other in this way. And I don't

## 12020:00 - 12040:00

know that king and queen are opposites

## 12040:00 - 12090:00

in these ways, right? Um, and so this is

## 12090:00 - 12115:00

why it's called pre-training is because

## 12115:00 - 12160:00

you must get a broad general

## 12160:00 - 12195:00

understanding of the entire sort of

## 12195:00 - 12245:00

world of text before you're able to then

## 12245:00 - 12285:00

do post-training or fine-tuning, which

## 12285:00 - 12325:00

is let me train it on more specific data

## 12325:00 - 12355:00

that is specifically useful for what I

## 12355:00 - 12400:00

want it to do. Whether it's hey um in

## 12400:00 - 12445:00

chat style applications um you know go

## 12445:00 - 12480:00

and go and you know when I ask a

## 12480:00 - 12530:00

question give me the answer or um in in

## 12530:00 - 12550:00

other applications like teach me how to

## 12550:00 - 12580:00

build a bomb. Well obviously no I'm not

## 12580:00 - 12600:00

going to help you teach build a bomb

## 12600:00 - 12615:00

because that's what I don't want the

## 12615:00 - 12640:00

model to teach me how to build a bomb.

## 12640:00 - 12670:00

So, you know, it's sort of got to do

## 12670:00 - 12690:00

this and it's not like you're teaching

## 12690:00 - 12715:00

it, you know, when you're doing this

## 12715:00 - 12755:00

pre-training um you're filtering out all

## 12755:00 - 12785:00

this data because in fact there's a lot

## 12785:00 - 12810:00

of good useful data on how to build

## 12810:00 - 12835:00

bombs because there's a lot of useful

## 12835:00 - 12885:00

information on like hey like C4

## 12885:00 - 12920:00

chemistry and like you know people want

## 12920:00 - 12950:00

to use it for chemistry right so you

## 12950:00 - 12980:00

don't want to just filter out everything

## 12980:00 - 13000:00

uh so that the model doesn't know

## 13000:00 - 13025:00

anything about it um but at the same

## 13025:00 - 13055:00

time you don't want it to output you

## 13055:00 - 13085:00

know how to build a bomb um so there's

## 13085:00 - 13115:00

like a fine balance here and that's why

## 13115:00 - 13150:00

pre-training is defined as pre because

## 13150:00 - 13180:00

you're you're you're still letting it do

## 13180:00 - 13210:00

things and teaching it things and

## 13210:00 - 13250:00

inputting things into the model that are

## 13250:00 - 13285:00

theoretically like quite bad, right? Um

## 13285:00 - 13325:00

for example, books about like killing or

## 13325:00 - 13350:00

war tactics or what have you, right?

## 13350:00 - 13375:00

Like things that like plausibly you

## 13375:00 - 13400:00

could see like, oh well maybe that's not

## 13400:00 - 13465:00

okay. Um or or wild descriptions of like

## 13465:00 - 13495:00

really grotesque things all over the

## 13495:00 - 13520:00

internet, but you want the model to

## 13520:00 - 13545:00

learn these things, right? Because first

## 13545:00 - 13580:00

you build the general understanding

## 13580:00 - 13605:00

before you say okay now that you've got

## 13605:00 - 13635:00

a general framework of the world let's

## 13635:00 - 13680:00

align you so that you with this general

## 13680:00 - 13700:00

understanding of the world can figure

## 13700:00 - 13730:00

out what is useful for people what is

## 13730:00 - 13760:00

not useful for people what should I

## 13760:00 - 13795:00

respond on what should I not respond on

## 13795:00 - 13825:00

so what happens then in the training

## 13825:00 - 13860:00

process so the the in is the training

## 13860:00 - 13895:00

process that the model is then

## 13895:00 - 13930:00

attempting to make the next prediction

## 13930:00 - 13970:00

and then just trying to minimize loss as

## 13970:00 - 14000:00

it goes right right I mean like

## 14000:00 - 14065:00

basically uh you you have you have loss

## 14065:00 - 14100:00

is is how often you're wrong versus

## 14100:00 - 14130:00

right in the most simple terms right you

## 14130:00 - 14180:00

will you'll run through a passages right

## 14180:00 - 14215:00

through the model um and you'll see how

## 14215:00 - 14240:00

often did the model get it right when it

## 14240:00 - 14275:00

got it right great reinforce that uh

## 14275:00 - 14305:00

when I got it wrong let's figure out

## 14305:00 - 14355:00

which which neurons neurons in the model

## 14355:00 - 14385:00

you know quote unquote neurons in the

## 14385:00 - 14435:00

model you can tweak to then fix the

## 14435:00 - 14460:00

answer so that when you go through it

## 14460:00 - 14480:00

again it actually outputs the correct

## 14480:00 - 14515:00

answer and then you move the the move

## 14515:00 - 14555:00

the model slightly in that direction. Um

## 14555:00 - 14580:00

now obviously the the challenge with

## 14580:00 - 14640:00

this is um if I if I first you know I

## 14640:00 - 14670:00

can I can come up with a simplistic way

## 14670:00 - 14695:00

where all the neurons will just output

## 14695:00 - 14720:00

the sky is blue every single time it

## 14720:00 - 14775:00

says the sky is but then when it goes to

## 14775:00 - 14845:00

um you know hey the the color blue is

## 14845:00 - 14870:00

commonly used on walls because it's

## 14870:00 - 14890:00

soothing right and it's like oh what's

## 14890:00 - 14930:00

the next word is soothing right soothing

## 14930:00 - 14955:00

you know and so like that that is a

## 14955:00 - 14985:00

completely different representation and

## 14985:00 - 15025:00

to understand that blue is soothing and

## 15025:00 - 15050:00

that the sky is blue and those things

## 15050:00 - 15080:00

aren't actually related but they are

## 15080:00 - 15115:00

related to blue is like very important

## 15115:00 - 15155:00

and so you know over often times you'll

## 15155:00 - 15175:00

run through the training data set

## 15175:00 - 15215:00

multiple times right uh because the

## 15215:00 - 15245:00

first time you see it oh great maybe you

## 15245:00 - 15290:00

memorized that the sky is blue um and

## 15290:00 - 15335:00

and you memorize the wall is blue and

## 15335:00 - 15385:00

that uh and when people describe art and

## 15385:00 - 15425:00

often times use the color blue it can it

## 15425:00 - 15455:00

can be representations of art or the

## 15455:00 - 15500:00

wall right and so over time as you go

## 15500:00 - 15535:00

through all this text in pre-training

## 15535:00 - 15565:00

Yes, you're minimizing loss initially by

## 15565:00 - 15600:00

just memorizing, but over time because

## 15600:00 - 15630:00

you're constantly overwriting the model,

## 15630:00 - 15665:00

it starts to learn the generalization,

## 15665:00 - 15695:00

right? I.e. blue is a soothing color,

## 15695:00 - 15730:00

also represents the sky, also used in

## 15730:00 - 15775:00

art to for either of those two motifs,

## 15775:00 - 15805:00

right? And so that's sort of the the

## 15805:00 - 15835:00

goal of pre-training is is you don't

## 15835:00 - 15860:00

want to memorize, right? Because that's,

## 15860:00 - 15890:00

you know, in school you memorize all the

## 15890:00 - 15925:00

time. Um, and that's not useful because

## 15925:00 - 15950:00

you forget everything you memorize. Uh

## 15950:00 - 15975:00

but if you get tested on it then and

## 15975:00 - 16010:00

then you get tested on it 6 months later

## 16010:00 - 16045:00

um and then again 6 months later after

## 16045:00 - 16075:00

that or or however you do it ends up

## 16075:00 - 16100:00

being oh you you don't actually like

## 16100:00 - 16130:00

memorize that anymore. You just know it

## 16130:00 - 16165:00

innately um and you've generalized on it

## 16165:00 - 16200:00

and that's the real goal uh that you

## 16200:00 - 16245:00

want out of the model. Uh but that's not

## 16245:00 - 16265:00

necessarily something you can just

## 16265:00 - 16295:00

measure right and therefore loss is

## 16295:00 - 16350:00

something you can measure i.e for this

## 16350:00 - 16385:00

group of this group of text, right?

## 16385:00 - 16435:00

Because you train the model in in steps.

## 16435:00 - 16460:00

Every step you're inputting a bunch of

## 16460:00 - 16485:00

text. You're trying to uh you're trying

## 16485:00 - 16510:00

to see what's predict the right token

## 16510:00 - 16525:00

where you didn't predict the right

## 16525:00 - 16555:00

token. Let's adjust the neurons. Okay,

## 16555:00 - 16585:00

on to the next batch of text. And you'll

## 16585:00 - 16620:00

do this these batches over and over and

## 16620:00 - 16660:00

over again um o across, you know,

## 16660:00 - 16700:00

trillions of words of text, right? Um

## 16700:00 - 16730:00

and and as you step through and then

## 16730:00 - 16765:00

you're like, "Oh, well, I'm done." But I

## 16765:00 - 16790:00

bet if I go back to the first first

## 16790:00 - 16810:00

group of text, which was all about the

## 16810:00 - 16835:00

sky being blue, it's going to get the

## 16835:00 - 16870:00

answer wrong because maybe later on in

## 16870:00 - 16895:00

the training, it discovered it saw some

## 16895:00 - 16925:00

passages about sci-fi and how the how

## 16925:00 - 16960:00

Martian sky is red. So like it'll it'll

## 16960:00 - 16990:00

overwrite but then over time as you go

## 16990:00 - 17025:00

through the data multiple times as you

## 17025:00 - 17050:00

see it on the internet multiple times as

## 17050:00 - 17070:00

you see it in different books multiple

## 17070:00 - 17100:00

times whether it be scientific sci-fi

## 17100:00 - 17130:00

whatever it is you start to realize and

## 17130:00 - 17165:00

it starts to learn that uh that

## 17165:00 - 17195:00

representation of like oh when it's on

## 17195:00 - 17230:00

Mars it's red because the sky and Mars

## 17230:00 - 17260:00

is red because the atmospheric makeup is

## 17260:00 - 17290:00

this way whereas the atmospheric makeup

## 17290:00 - 17320:00

in in on Earth is a different way. And

## 17320:00 - 17345:00

so that's sort of like the whole point

## 17345:00 - 17385:00

of pre-training is is to minimize loss,

## 17385:00 - 17410:00

but the nice side effect is that the

## 17410:00 - 17440:00

model initially memorizes, but then it

## 17440:00 - 17475:00

stops memorizing and it generalizes. And

## 17475:00 - 17510:00

that's the useful pattern that we want.

## 17510:00 - 17540:00

Okay, that's fascinating. Uh we've

## 17540:00 - 17585:00

touched on post-training uh for a bit,

## 17585:00 - 17630:00

but just to recap, post-raining is so

## 17630:00 - 17655:00

you have a model that's good at

## 17655:00 - 17685:00

predicting the next word, and in post-

## 17685:00 - 17710:00

training, you sort of give it a

## 17710:00 - 17750:00

personality by inputting sample

## 17750:00 - 17790:00

conversations to make the model want to

## 17790:00 - 17830:00

emulate the certain values that you want

## 17830:00 - 17875:00

it to take on.

## 17875:00 - 17905:00

Yeah. So, post training can be a number

## 17905:00 - 17930:00

of different things. The most simple way

## 17930:00 - 17980:00

of doing it is is yeah, uh pay for

## 17980:00 - 18025:00

humans to label a bunch of data. um take

## 18025:00 - 18085:00

a bunch of example conversations um etc

## 18085:00 - 18120:00

and input that data and train on that at

## 18120:00 - 18160:00

the end, right? Um and so that that

## 18160:00 - 18215:00

example data is is useful uh but this is

## 18215:00 - 18245:00

not scalable, right? Like using humans

## 18245:00 - 18275:00

to train models is just so expensive,

## 18275:00 - 18305:00

right? So then there's the magic of sort

## 18305:00 - 18340:00

of reinforcement learning and and other

## 18340:00 - 18375:00

synthetic data technologies, right?

## 18375:00 - 18410:00

Where the model is helping teach the

## 18410:00 - 18445:00

model, right? So you have many models in

## 18445:00 - 18495:00

in in a sort of in a post training where

## 18495:00 - 18530:00

yes you have some example human data but

## 18530:00 - 18560:00

human data does not scale that fast

## 18560:00 - 18605:00

right cuz cuz the internet is trillions

## 18605:00 - 18640:00

and trillions of words out there whereas

## 18640:00 - 18675:00

you know even if you had you know Alex

## 18675:00 - 18725:00

and I write words all day long for our

## 18725:00 - 18760:00

whole lives would we would have millions

## 18760:00 - 18795:00

or you know hundreds of millions of

## 18795:00 - 18820:00

words written right it's nothing it's

## 18820:00 - 18850:00

like orders of magnitude off in terms of

## 18850:00 - 18890:00

the number of words required um so then

## 18890:00 - 18935:00

you have the model, you know, takes some

## 18935:00 - 18985:00

of this example data um and you have

## 18985:00 - 19030:00

various models that are surrounding the

## 19030:00 - 19050:00

main model that you're training, right?

## 19050:00 - 19075:00

And these can be policy models, right?

## 19075:00 - 19110:00

Teaching it, hey, is this is this what

## 19110:00 - 19130:00

you want or that what you want? Uh

## 19130:00 - 19160:00

reward models, right? Like is that good?

## 19160:00 - 19185:00

Is that a good response or is that a bad

## 19185:00 - 19215:00

bad response? You have value models like

## 19215:00 - 19250:00

hey, grade this output, right? And you

## 19250:00 - 19275:00

have all these different models working

## 19275:00 - 19330:00

in conjunction to say um uh you know,

## 19330:00 - 19350:00

different companies have different

## 19350:00 - 19380:00

objective functions, right? In the case

## 19380:00 - 19410:00

of anthropic, they're they want their

## 19410:00 - 19450:00

model to be helpful, harmful, harmless,

## 19450:00 - 19495:00

and safe, right? So, be helpful, but

## 19495:00 - 19525:00

also don't harm people or anyone or

## 19525:00 - 19560:00

anything. And then, you know, uh you

## 19560:00 - 19595:00

know, safe, right? In other cases, like

## 19595:00 - 19645:00

Grock, right? Uh Elon's model from XAI,

## 19645:00 - 19685:00

um it actually just wants to be helpful.

## 19685:00 - 19715:00

Um and maybe has like a little bit of a

## 19715:00 - 19740:00

right leaning to it, right? And and for

## 19740:00 - 19765:00

other folks, right, like you know, I

## 19765:00 - 19790:00

mean, most AI models are made in the Bay

## 19790:00 - 19820:00

Area, so they tend to just be left

## 19820:00 - 19845:00

leaning, right? Um but also the internet

## 19845:00 - 19875:00

on general is a little bit left-leaning

## 19875:00 - 19910:00

um because it skews younger than older.

## 19910:00 - 19935:00

Um and so like all these things like

## 19935:00 - 19975:00

sort of affect models. Um but like it's

## 19975:00 - 20005:00

not just around politics, right? Post

## 20005:00 - 20030:00

training is also just about teaching the

## 20030:00 - 20100:00

model. If I if I say like uh the movie

## 20100:00 - 20160:00

where uh the princess has a slipper and

## 20160:00 - 20200:00

it doesn't fit. It's like well on if I

## 20200:00 - 20225:00

said that into a base model that was

## 20225:00 - 20250:00

just pre-training like the answer

## 20250:00 - 20265:00

wouldn't be oh the movie you're looking

## 20265:00 - 20300:00

for Cinderella. you know, it it would

## 20300:00 - 20335:00

only realize that once it goes, you

## 20335:00 - 20350:00

know, once it goes through post-

## 20350:00 - 20375:00

training, right? Because a lot of times

## 20375:00 - 20405:00

people just throw garbage into the model

## 20405:00 - 20430:00

and then the model still figures out

## 20430:00 - 20450:00

what you want, right? And this is part

## 20450:00 - 20475:00

of what post- training is. Like you can

## 20475:00 - 20500:00

just do stream of consciousness into

## 20500:00 - 20525:00

models and often times it'll figure out

## 20525:00 - 20550:00

what you want. Like, you know, if it's a

## 20550:00 - 20580:00

movie that you're looking for or if it's

## 20580:00 - 20605:00

help answering a question or if you

## 20605:00 - 20635:00

throw a bunch of like unstructured data

## 20635:00 - 20660:00

into it and then ask it to make it into

## 20660:00 - 20695:00

a table, it does this, right? And that's

## 20695:00 - 20715:00

because of all these different aspects

## 20715:00 - 20750:00

of post training, right? example data

## 20750:00 - 20800:00

but also uh you know generating a bunch

## 20800:00 - 20840:00

of data and and grading it um and seeing

## 20840:00 - 20875:00

if it's good or not um and whether it

## 20875:00 - 20900:00

matches the various policies you want is

## 20900:00 - 20930:00

it help you know a lot of times grading

## 20930:00 - 20955:00

can be based on multiple factors right

## 20955:00 - 20970:00

there could be a model that says hey is

## 20970:00 - 21010:00

this helpful hey is this is this safe

## 21010:00 - 21035:00

and what is safe right so then that

## 21035:00 - 21070:00

model for safety needs to be tuned on

## 21070:00 - 21100:00

human data right so there's it is a

## 21100:00 - 21130:00

quite complex thing but the end goal is

## 21130:00 - 21165:00

to be able to get the model to uh output

## 21165:00 - 21200:00

in a certain way models aren't always

## 21200:00 - 21225:00

about just humans using them either

## 21225:00 - 21250:00

Right? There can be models that are just

## 21250:00 - 21280:00

focused on like, hey, like, you know, if

## 21280:00 - 21315:00

it doesn't output code, you know, yes,

## 21315:00 - 21335:00

it was trained on the whole internet

## 21335:00 - 21355:00

because the person's going to talk to

## 21355:00 - 21385:00

the model using text, but if it doesn't

## 21385:00 - 21415:00

output code, you know, penalize it,

## 21415:00 - 21435:00

right? Now, all of a sudden, the model

## 21435:00 - 21465:00

will never output like text ever again.

## 21465:00 - 21510:00

It'll only output code. Um, and and so

## 21510:00 - 21540:00

like these sorts of like models exist

## 21540:00 - 21565:00

too. So post- training is not just a

## 21565:00 - 21600:00

univariable thing, right? It's what

## 21600:00 - 21630:00

variables do you want to target? Um, and

## 21630:00 - 21650:00

so that's why models have different

## 21650:00 - 21680:00

personalities from different companies.

## 21680:00 - 21710:00

It's why they target different use cases

## 21710:00 - 21740:00

and why, you know, it's not just like

## 21740:00 - 21765:00

one model that rules them all, but

## 21765:00 - 21790:00

actually many.

## 21790:00 - 21815:00

That's fascinating. So, that's why we've

## 21815:00 - 21840:00

seen so many different models with

## 21840:00 - 21860:00

different personalities is because it

## 21860:00 - 21900:00

all happens in the post-training uh

## 21900:00 - 21945:00

moment. And this is when when you talk

## 21945:00 - 21975:00

about giving the models examples to

## 21975:00 - 22005:00

follow. That's that's what reinforcement

## 22005:00 - 22035:00

learning with human feedback is, is the

## 22035:00 - 22075:00

humans give some examples and then the

## 22075:00 - 22115:00

model learns to emulate what the human

## 22115:00 - 22160:00

is interested in, what the human trainer

## 22160:00 - 22215:00

is interested in having them uh

## 22215:00 - 22275:00

embody. Is that right? Yeah, exactly.

## 22275:00 - 22310:00

Okay, great. All right, so first half

## 22310:00 - 22340:00

we've covered what training is, what

## 22340:00 - 22390:00

tokens are, what loss is, what uh post-

## 22390:00 - 22420:00

trainining is, post training is, post

## 22420:00 - 22435:00

training, by the way, also called

## 22435:00 - 22465:00

fine-tuning. We've also covered

## 22465:00 - 22490:00

reinforcement learning with human

## 22490:00 - 22515:00

feedback. We're going to take a quick

## 22515:00 - 22550:00

break and then we're going to talk about

## 22550:00 - 22600:00

reasoning. We'll be back right after

## 22600:00 - 22635:00

this. And we're back here on Big

## 22635:00 - 22675:00

Technology Podcast with Dylan Patel.

## 22675:00 - 22720:00

He's the founder and chief analyst at

## 22720:00 - 22760:00

Semi analysis. He actually has great

## 22760:00 - 22825:00

analysis on Nvidia's recent uh uh GTC

## 22825:00 - 22855:00

conference, which we just covered

## 22855:00 - 22890:00

recently on a on a recent episode. You

## 22890:00 - 22930:00

can find semi analysis at

## 22930:00 - 22975:00

semianalysis.com. It is both content and

## 22975:00 - 23015:00

sort of and consulting. So definitely

## 23015:00 - 23060:00

check in with Dylan for all of those uh

## 23060:00 - 23085:00

all those needs. And now we're going to

## 23085:00 - 23125:00

talk a little bit about reasoning

## 23125:00 - 23150:00

because a couple months ago, and Dylan,

## 23150:00 - 23180:00

this is really where you know I sort of

## 23180:00 - 23215:00

entered the picture watching your uh

## 23215:00 - 23260:00

conversation with Flex uh with Nathan

## 23260:00 - 23290:00

Lambert about what the difference is

## 23290:00 - 23345:00

between reasoning and um and your

## 23345:00 - 23390:00

traditional LLMs, large language models.

## 23390:00 - 23425:00

Um, if I gathered it right from your

## 23425:00 - 23450:00

conversation, what reasoning is is

## 23450:00 - 23525:00

basically instead of uh the model going

## 23525:00 - 23550:00

uh basically predicting the next word

## 23550:00 - 23590:00

based off of its training, it uses the

## 23590:00 - 23650:00

tokens to spend more time uh basically

## 23650:00 - 23685:00

figuring out what the right answer is

## 23685:00 - 23720:00

and then coming out with its with a new

## 23720:00 - 23745:00

prediction. I think Carpathy does a very

## 23745:00 - 23780:00

interesting job uh in the YouTube video

## 23780:00 - 23810:00

talking about how models think with

## 23810:00 - 23850:00

tokens. the more tokens there are, the

## 23850:00 - 23875:00

more computes they compute they use

## 23875:00 - 23890:00

because they're running these

## 23890:00 - 23925:00

predictions through the transformer

## 23925:00 - 23955:00

model which we discussed and therefore

## 23955:00 - 23985:00

they can come to better answers. Is that

## 23985:00 - 24025:00

the right way to think about reasoning?

## 24025:00 - 24075:00

So, so I think that um humans are also

## 24075:00 - 24115:00

fantastic at f pattern matching, right?

## 24115:00 - 24150:00

Um we're really good at like recognizing

## 24150:00 - 24200:00

things. Um but a lot of tasks it's not

## 24200:00 - 24225:00

like an immediate response, right? we

## 24225:00 - 24260:00

are thinking um whether that's thinking

## 24260:00 - 24285:00

through words out loud, thinking through

## 24285:00 - 24320:00

words in an inner monologue in our head

## 24320:00 - 24350:00

or it's just like processing somehow and

## 24350:00 - 24390:00

then we know the answer, right? Um and

## 24390:00 - 24415:00

this is the same for models, right?

## 24415:00 - 24450:00

Models are horrendous at math, right?

## 24450:00 - 24490:00

Historically have been, right? Um you

## 24490:00 - 24550:00

could ask it, you know, what is 9.11

## 24550:00 - 24595:00

bigger than 9.9? Um and it would say

## 24595:00 - 24620:00

yes, it's bigger even though like

## 24620:00 - 24675:00

everyone knows that 9.11 is is way

## 24675:00 - 24720:00

smaller than 9.9, right? Um, and that's

## 24720:00 - 24740:00

just like a thing that happened in

## 24740:00 - 24770:00

models because they didn't think or

## 24770:00 - 24800:00

reason, right? And and it's the same for

## 24800:00 - 24830:00

you, Alex, right? Like, you know, or

## 24830:00 - 24860:00

myself, right? Like if someone asked me,

## 24860:00 - 24920:00

you know, uh, 17 * 34, I'd be like, I

## 24920:00 - 24940:00

don't know, like right off the top of my

## 24940:00 - 24970:00

head, but, you know, give me give me a a

## 24970:00 - 24995:00

little bit of time. I can do some long

## 24995:00 - 25020:00

form multiplication and I can get the

## 25020:00 - 25045:00

answer, right? And that's because I'm

## 25045:00 - 25085:00

thinking about it. Um, and this is the

## 25085:00 - 25120:00

same thing with reasoning for models. um

## 25120:00 - 25150:00

is you know when when you look at a

## 25150:00 - 25190:00

transformer every word is the every

## 25190:00 - 25215:00

token output it has the same amount of

## 25215:00 - 25265:00

compute behind it right um i.e i.e. you

## 25265:00 - 25310:00

know when I'm saying the versus sky is

## 25310:00 - 25350:00

blue the blue and the the have the or

## 25350:00 - 25385:00

the the is and the blue have the same

## 25385:00 - 25420:00

amount of compute to generate right um

## 25420:00 - 25440:00

and this is not exactly what you want to

## 25440:00 - 25480:00

do right you want to actually um spend

## 25480:00 - 25510:00

more time on the hard things and and and

## 25510:00 - 25545:00

not on the easy things um and so

## 25545:00 - 25595:00

reasoning models are effectively

## 25595:00 - 25630:00

teaching you know large pre-trained

## 25630:00 - 25675:00

models to do this right hey think

## 25675:00 - 25710:00

through the problem hey output a lot of

## 25710:00 - 25750:00

tokens uh think about it generate all

## 25750:00 - 25785:00

text and then when you're done, you

## 25785:00 - 25810:00

know, start answering the question, but

## 25810:00 - 25835:00

now you have all of this stuff you

## 25835:00 - 25890:00

generated in your context, right? Um,

## 25890:00 - 25925:00

and that stuff you generated is is

## 25925:00 - 25965:00

helpful, right? Um, it could be like,

## 25965:00 - 25990:00

you know, all sorts of all, you know,

## 25990:00 - 26020:00

just like any human's thought patterns

## 26020:00 - 26075:00

are, right? Um, and so this this is the

## 26075:00 - 26110:00

sort of like new paradigm that we've

## 26110:00 - 26155:00

entered maybe 6 months ago where models

## 26155:00 - 26205:00

now will think for some time before they

## 26205:00 - 26245:00

answer. And this enables much better

## 26245:00 - 26270:00

performance on all sorts of tasks,

## 26270:00 - 26315:00

whether it be coding or math or

## 26315:00 - 26350:00

understanding science or understanding

## 26350:00 - 26395:00

complex social dilemmas, right? All

## 26395:00 - 26420:00

sorts of different topics they're much

## 26420:00 - 26460:00

much better at. Um, and this is done

## 26460:00 - 26490:00

through post-training, similar to the

## 26490:00 - 26515:00

reinforcement learning by human feedback

## 26515:00 - 26560:00

that we mentioned earlier. Uh, but also

## 26560:00 - 26590:00

there's other forms of post-training and

## 26590:00 - 26620:00

that's that's what makes these reasoning

## 26620:00 - 26650:00

models. Before we head out, I want to

## 26650:00 - 26680:00

hit on a couple things. Um, first of

## 26680:00 - 26715:00

all, the growing efficiency of these

## 26715:00 - 26760:00

models. So, I think one of the things

## 26760:00 - 26790:00

that people focused on with DeepSeek was

## 26790:00 - 26820:00

that it was just able to be much more

## 26820:00 - 26870:00

efficient in the way that it generates

## 26870:00 - 26905:00

answers. Uh, and there was this

## 26905:00 - 26950:00

obviously this big reaction to Nvidia

## 26950:00 - 27005:00

stock where it fell 18% the day or at

## 27005:00 - 27050:00

the Monday after Deepseek weekend um

## 27050:00 - 27070:00

because people thought we wouldn't need

## 27070:00 - 27100:00

as much compute. So can you talk a

## 27100:00 - 27140:00

little bit about how models are becoming

## 27140:00 - 27165:00

more efficient and how they're doing it?

## 27165:00 - 27200:00

Yeah. So there's a variety of u the

## 27200:00 - 27240:00

beauty of these uh of AI is not just

## 27240:00 - 27260:00

that we continue to build new

## 27260:00 - 27300:00

capabilities, right? Um because those

## 27300:00 - 27320:00

new capabilities are going to be able to

## 27320:00 - 27350:00

benefit the world in many ways. Um and

## 27350:00 - 27385:00

there's a lot of focus on those but

## 27385:00 - 27405:00

there's also a lot of there's a lot of

## 27405:00 - 27450:00

focus on well to get to that next level

## 27450:00 - 27490:00

of capabilities is is the scaling laws

## 27490:00 - 27530:00

i.e. the more compute and data I send

## 27530:00 - 27565:00

spend the better the model gets. But

## 27565:00 - 27600:00

then the other vector is well can I get

## 27600:00 - 27630:00

to the same level with less compute and

## 27630:00 - 27675:00

data right um and and those two things

## 27675:00 - 27700:00

are handinand because if I can get to

## 27700:00 - 27725:00

the same level with the less comput and

## 27725:00 - 27760:00

data then I can spend that more comput

## 27760:00 - 27785:00

and data and get to a new level right

## 27785:00 - 27820:00

and so AI researchers are constantly

## 27820:00 - 27860:00

looking for ways to make models more

## 27860:00 - 27885:00

efficient uh whether it be through

## 27885:00 - 27930:00

algorithmic tweaks uh data tweaks uh

## 27930:00 - 27955:00

tweaks in you know how you do

## 27955:00 - 27975:00

reinforcement learning so on and so

## 27975:00 - 28015:00

forth right and so when we look at

## 28015:00 - 28055:00

models across history they've constantly

## 28055:00 - 28080:00

gotten cheaper and cheaper and cheaper,

## 28080:00 - 28125:00

right? Um at a stupendous rate, right?

## 28125:00 - 28165:00

Um and so one easy example is GPT3,

## 28165:00 - 28225:00

right? Uh cuz there's GPT3, 3.5 Turbo,

## 28225:00 - 28305:00

uh Llama 27B, Llama 3, uh Llama 3.1,

## 28305:00 - 28340:00

Llama 3.2, right? As these models have

## 28340:00 - 28375:00

gotten bigger, we've gone from, hey, it

## 28375:00 - 28430:00

costs $60 for a million tokens to it

## 28430:00 - 28475:00

cost less than it costs like 5 cents now

## 28475:00 - 28520:00

for the same quality of model now. And

## 28520:00 - 28555:00

the model has shrank dramatically in

## 28555:00 - 28575:00

size as well and that's because of

## 28575:00 - 28620:00

better algorithms, better data etc. Um

## 28620:00 - 28650:00

and now what happened with DeepSeek was

## 28650:00 - 28695:00

similar. Um you know open AI had GPD4

## 28695:00 - 28725:00

then they had 4 Turbo which was half the

## 28725:00 - 28755:00

cost. Then they had 40 which was again

## 28755:00 - 28790:00

half the cost. Uh and then Meta released

## 28790:00 - 28835:00

Llama 405B open source and so the open

## 28835:00 - 28860:00

source community was able to run that

## 28860:00 - 28885:00

and that was again like roughly like

## 28885:00 - 28930:00

half the cost. Uh but or or 5x lower

## 28930:00 - 28970:00

cost um than 40 which was lower than

## 28970:00 - 29010:00

four turbo and four u but deepseek came

## 29010:00 - 29050:00

out with another tier right. So when we

## 29050:00 - 29110:00

looked at GPD3, the cost fell 1,200x

## 29110:00 - 29155:00

from uh GPD3's initial cost to what you

## 29155:00 - 29220:00

can get llama 3 point uh 2 uh 3b today,

## 29220:00 - 29265:00

right? And likewise when we look at uh

## 29265:00 - 29320:00

from GPD4 to deepse v3 uh it's fallen

## 29320:00 - 29355:00

roughly 600x in cost, right? So we're

## 29355:00 - 29385:00

not quite at that 1,200x, but it has

## 29385:00 - 29430:00

fallen 600x in cost from $60 to less

## 29430:00 - 29465:00

than uh you know to about a dollar,

## 29465:00 - 29485:00

right? Or or to less than a dollar,

## 29485:00 - 29530:00

sorry, 60x. Um, and so you've got this

## 29530:00 - 29570:00

massive cost decrease. Uh, but it's not

## 29570:00 - 29600:00

necessarily out of bounds, right? We've

## 29600:00 - 29625:00

already seen it. I think what was really

## 29625:00 - 29665:00

surprising, uh, was that it was a

## 29665:00 - 29685:00

Chinese company for the first time,

## 29685:00 - 29720:00

right? Cuz Google and and OpenAI and

## 29720:00 - 29765:00

Enthropic and Meta have all traded

## 29765:00 - 29790:00

blows, right? You know, uh, whether it

## 29790:00 - 29815:00

be OpenAI always being on the leading

## 29815:00 - 29840:00

edge or Enthropic always being on the

## 29840:00 - 29865:00

leading edge or, you know, Google and

## 29865:00 - 29905:00

Meta, you know, being close followers

## 29905:00 - 29935:00

but oftentimes, sometimes with a new

## 29935:00 - 29965:00

feature, um, and sometimes just being

## 29965:00 - 30005:00

much cheaper. Um, we have not seen this

## 30005:00 - 30045:00

from any Chinese company, right? And now

## 30045:00 - 30075:00

we have a Chinese company releasing a

## 30075:00 - 30120:00

model that's cheap. Um, it's not

## 30120:00 - 30145:00

unexpected, right? Like this is actually

## 30145:00 - 30170:00

within the trend line of what happened

## 30170:00 - 30210:00

with GPT3 is happening to GPT4 level

## 30210:00 - 30260:00

quality with Deepseek. Um, it's more so

## 30260:00 - 30295:00

surprising that it's a Chinese company

## 30295:00 - 30320:00

and that's I think why everyone freaked

## 30320:00 - 30350:00

out and then there was a lot of things

## 30350:00 - 30385:00

that like you know from there became a

## 30385:00 - 30405:00

thing, right? Like if Meta had done

## 30405:00 - 30425:00

this, I don't think people would have

## 30425:00 - 30460:00

freaked out, right? Um, and Meta's Meta

## 30460:00 - 30485:00

is going to release their new llama soon

## 30485:00 - 30520:00

enough, right? And that one is going to

## 30520:00 - 30565:00

be, you know, uh, similar level of cost

## 30565:00 - 30605:00

decrease. Uh, probably similar area as

## 30605:00 - 30645:00

Deep Seek V3, right? Um, it's just not

## 30645:00 - 30660:00

people aren't going to freak out because

## 30660:00 - 30685:00

it's an American company and it was sort

## 30685:00 - 30715:00

of expected. All

## 30715:00 - 30735:00

right, Dylan, let me ask you the last

## 30735:00 - 30765:00

question, which is that you mentioned I

## 30765:00 - 30785:00

think you mentioned the bitter lesson,

## 30785:00 - 30830:00

which is basically that the I mean, I'm

## 30830:00 - 30860:00

going to just be kind of facitious in

## 30860:00 - 30885:00

summing it up, but the answer to all

## 30885:00 - 30910:00

questions in machine learning is just to

## 30910:00 - 30955:00

make bigger uh bigger models uh and

## 30955:00 - 30995:00

scale solves almost all problems. So,

## 30995:00 - 31015:00

it's interesting that we have this

## 31015:00 - 31040:00

moment where models are becoming way

## 31040:00 - 31075:00

more efficient. Uh but we also have

## 31075:00 - 31120:00

massive massive data center buildouts.

## 31120:00 - 31155:00

Um I think you it would be great to hear

## 31155:00 - 31185:00

you kind of recap the size of these data

## 31185:00 - 31215:00

center buildouts and then answer this

## 31215:00 - 31250:00

question. Uh if we are getting more

## 31250:00 - 31285:00

efficient, why are these data centers

## 31285:00 - 31320:00

getting so much bigger? Uh and what

## 31320:00 - 31360:00

might that added scale get in the world

## 31360:00 - 31400:00

of generative AI uh for the companies

## 31400:00 - 31430:00

building them. Yeah. So when we look

## 31430:00 - 31465:00

across the ecosystem at data center

## 31465:00 - 31500:00

buildouts um you know we track all the

## 31500:00 - 31540:00

buildouts and and server purchases and

## 31540:00 - 31580:00

supply chains here and and the pace of

## 31580:00 - 31610:00

construction is incredible, right?

## 31610:00 - 31635:00

right? You can just you can pick a state

## 31635:00 - 31660:00

and you can see new data centers going

## 31660:00 - 31710:00

up um all across the US and and around

## 31710:00 - 31740:00

the world, right? Um and so you see

## 31740:00 - 31800:00

things like um capacity in you know, for

## 31800:00 - 31825:00

example, of of the largest scale

## 31825:00 - 31860:00

training supercomputers goes from hey,

## 31860:00 - 31895:00

it's a few hundred million it's it's not

## 31895:00 - 31920:00

even a few hundred million years ago,

## 31920:00 - 31960:00

but like you know, hey, for GPT4 it was

## 31960:00 - 32030:00

a few hundred million. Um and it's it's

## 32030:00 - 32095:00

one building full of GPUs, too. uh GPD

## 32095:00 - 32150:00

4.5 um and uh the reasoning models like

## 32150:00 - 32205:00

0103 were done in a in three buildings

## 32205:00 - 32255:00

on the same site and you know billions

## 32255:00 - 32290:00

of dollars to hey these next generation

## 32290:00 - 32320:00

things that people are making are tens

## 32320:00 - 32365:00

of billions of dollars um like OpenAI's

## 32365:00 - 32415:00

data center in Texas called Stargate

## 32415:00 - 32470:00

right uh with Crusoe and Oracle etc

## 32470:00 - 32505:00

right and likewise applies to Elon Musk

## 32505:00 - 32535:00

who's building these data centers in old

## 32535:00 - 32565:00

in an old factory where he's got like a

## 32565:00 - 32610:00

bunch of like gas generation uh you know

## 32610:00 - 32645:00

outside and he's doing all these crazy

## 32645:00 - 32670:00

things to get the data center up as fast

## 32670:00 - 32705:00

as possible, right? Um and and and you

## 32705:00 - 32730:00

can go to just basically every company

## 32730:00 - 32750:00

and they have like these humongous

## 32750:00 - 32805:00

buildouts. Um and this sort of like and

## 32805:00 - 32835:00

and and and because of the scaling laws,

## 32835:00 - 32875:00

right? You know, 10x more uh compute for

## 32875:00 - 32915:00

linear like improvement gains, right?

## 32915:00 - 32935:00

Like it's sort of like or it's log log,

## 32935:00 - 32975:00

sorry. Um but you uh you end up with

## 32975:00 - 33020:00

this like very confusing thing which is

## 33020:00 - 33065:00

like hey models keep getting better as

## 33065:00 - 33110:00

we spend more but also the model that we

## 33110:00 - 33175:00

had a year ago is now done for way way

## 33175:00 - 33210:00

cheaper right often times 10x cheaper or

## 33210:00 - 33255:00

more right just a year later. Um, so

## 33255:00 - 33280:00

then the question is like why are we

## 33280:00 - 33315:00

spending all this money to scale? Um,

## 33315:00 - 33345:00

and and and there's a few things here,

## 33345:00 - 33380:00

right? A, you can't actually make that

## 33380:00 - 33420:00

cheaper model without making the better

## 33420:00 - 33450:00

bigger model so you can generate data to

## 33450:00 - 33475:00

help you make the cheaper model, right?

## 33475:00 - 33515:00

Like that's part of it. Um, but also

## 33515:00 - 33570:00

another part of it is that um, you know,

## 33570:00 - 33610:00

if we were to freeze AI capabilities

## 33610:00 - 33665:00

where we were uh, basically in uh, what

## 33665:00 - 33710:00

was it March 2023, right? two years ago

## 33710:00 - 33755:00

when GPD4 released um and only made them

## 33755:00 - 33790:00

cheaper, right? Like Deepseek is like

## 33790:00 - 33825:00

much cheaper. It's much more efficient.

## 33825:00 - 33845:00

Um but it's roughly the same

## 33845:00 - 33920:00

capabilities as GPD4 um that would not

## 33920:00 - 33960:00

pay for all of these cap buildouts,

## 33960:00 - 34000:00

right? AI is useful today, but is not

## 34000:00 - 34040:00

capable of doing a lot of things, right?

## 34040:00 - 34070:00

But if we make the model way more

## 34070:00 - 34110:00

efficient and then continue to scale and

## 34110:00 - 34130:00

we have this like stair step, right,

## 34130:00 - 34165:00

where we like increase capabilities

## 34165:00 - 34190:00

massively, make them way more efficient,

## 34190:00 - 34215:00

increase capabilities massively, make

## 34215:00 - 34245:00

them way more efficient. We do the stair

## 34245:00 - 34285:00

step, then you end up with creating all

## 34285:00 - 34320:00

these new capabilities that could in

## 34320:00 - 34350:00

fact pay for, you know, these massive AI

## 34350:00 - 34385:00

buildouts. So, no one is trying to make

## 34385:00 - 34405:00

with these, you know, with these 10

## 34405:00 - 34430:00

billion dollar data centers, they're not

## 34430:00 - 34450:00

trying to make chat models, right?

## 34450:00 - 34470:00

They're not trying to make models that

## 34470:00 - 34500:00

people chat with, just to be clear,

## 34500:00 - 34520:00

right? They're trying to solve things

## 34520:00 - 34550:00

like software engineering and make it

## 34550:00 - 34595:00

automated. Um, which is like a trillion

## 34595:00 - 34625:00

dollar plus industry, right? Um, so

## 34625:00 - 34670:00

these are very different like sort of um

## 34670:00 - 34705:00

use cases and targets. And so it's the

## 34705:00 - 34745:00

bitter lesson because yes, you can make

## 34745:00 - 34765:00

you can spend a lot of time and effort

## 34765:00 - 34815:00

making clever specialized methods um you

## 34815:00 - 34855:00

know based on intuition. Um, and you

## 34855:00 - 34885:00

should, right? But these things should

## 34885:00 - 34910:00

also just have a lot more compute thrown

## 34910:00 - 34930:00

behind them because if you make it more

## 34930:00 - 34965:00

efficient as you follow the scaling laws

## 34965:00 - 34995:00

up, it'll also just get better and you

## 34995:00 - 35025:00

can then unlock new capabilities, right?

## 35025:00 - 35065:00

And so today, you know, a lot of uh AI

## 35065:00 - 35095:00

models, the best ones from Anthropic are

## 35095:00 - 35140:00

now useful for like coding uh as a

## 35140:00 - 35170:00

assistant with you, right? You're you're

## 35170:00 - 35200:00

going back and forth. you know, as time

## 35200:00 - 35225:00

goes forward, as you make them more

## 35225:00 - 35250:00

efficient and continue to scale them,

## 35250:00 - 35280:00

the possibility is that, hey, it can

## 35280:00 - 35310:00

code for like 10 minutes at a time and I

## 35310:00 - 35340:00

can just review the work and it'll make

## 35340:00 - 35375:00

me 5x more efficient, right? Um, you

## 35375:00 - 35400:00

know, and so on and so forth. And this

## 35400:00 - 35450:00

is sort of like where where reasoning

## 35450:00 - 35480:00

models and sort of the scaling sort of

## 35480:00 - 35535:00

argument comes in is like, yes, we can

## 35535:00 - 35565:00

make it more efficient, but we also

## 35565:00 - 35590:00

just, you know, that's not going to

## 35590:00 - 35615:00

solve the problems that we have today,

## 35615:00 - 35640:00

right? The Earth is still going to run

## 35640:00 - 35670:00

out of resources. uh we're going to run

## 35670:00 - 35690:00

out of nickel because we can't make

## 35690:00 - 35710:00

enough batteries and we can't make

## 35710:00 - 35735:00

enough batteries. So then we can't with

## 35735:00 - 35765:00

current technology that we can't replace

## 35765:00 - 35815:00

all of you know uh gas you know gas and

## 35815:00 - 35845:00

coal with renewables right all of these

## 35845:00 - 35870:00

things are going to happen unless like

## 35870:00 - 35910:00

you continue to improve AI and invent

## 35910:00 - 35940:00

and or just generally research new

## 35940:00 - 35970:00

things and AI helps us research new

## 35970:00 - 35995:00

things

## 35995:00 - 36020:00

okay this is really the last one where

## 36020:00 - 36065:00

is GPT5

## 36065:00 - 36120:00

um so so so openai released GP 4.5

## 36120:00 - 36180:00

recently um with uh what they called

## 36180:00 - 36220:00

training run Orion uh there ever hopes

## 36220:00 - 36270:00

that Orion could be used for uh for uh

## 36270:00 - 36315:00

GPD5. Um but its improvement was like

## 36315:00 - 36360:00

not enough to be like really a GPD5. Um

## 36360:00 - 36380:00

furthermore, it was trained on the

## 36380:00 - 36425:00

classical method which is like um which

## 36425:00 - 36460:00

is a ton of pre-training and then some

## 36460:00 - 36480:00

reinforcement learning with human

## 36480:00 - 36505:00

feedback and and some other

## 36505:00 - 36540:00

reinforcement learning like PO and DPO

## 36540:00 - 36590:00

and stuff like that. Um but not but then

## 36590:00 - 36620:00

along the way right this model was

## 36620:00 - 36650:00

trained last year. Along the way another

## 36650:00 - 36680:00

team at OpenAI made the big breakthrough

## 36680:00 - 36705:00

of reasoning, right? strawberry training

## 36705:00 - 36735:00

and they released 01 and then they

## 36735:00 - 36765:00

released 03 and these models are rapidly

## 36765:00 - 36790:00

getting better on re with reinforcement

## 36790:00 - 36830:00

learning with verifiable rewards. Um,

## 36830:00 - 36885:00

and so now GPD5, as Sam calls it, is is

## 36885:00 - 36920:00

going to be a model that has huge

## 36920:00 - 36970:00

pre-training scale, right, like GPD 4.5,

## 36970:00 - 37010:00

but also huge post-training scale like

## 37010:00 - 37050:00

01 and 03 and continuing to scale that

## 37050:00 - 37075:00

up, right? This would be the first time

## 37075:00 - 37125:00

we see a model that was was a step up in

## 37125:00 - 37155:00

both at the same time. And so that's

## 37155:00 - 37195:00

that's what uh OpenAI says is coming.

## 37195:00 - 37220:00

Um, they say it's coming, you know, this

## 37220:00 - 37250:00

year, hopefully in the next 3 to 6

## 37250:00 - 37285:00

months, maybe sooner. I've heard sooner,

## 37285:00 - 37335:00

but, you know, we'll we'll see. Um, but

## 37335:00 - 37375:00

this this path of scaling both

## 37375:00 - 37415:00

pre-training and post-training with

## 37415:00 - 37440:00

reinforcement learning with verifiable

## 37440:00 - 37490:00

rewards massively should yield much

## 37490:00 - 37515:00

better models that are capable of much

## 37515:00 - 37540:00

more things and we'll see what those

## 37540:00 - 37585:00

things are. Very cool. All right, Dylan,

## 37585:00 - 37620:00

do you want to give a quick shout out to

## 37620:00 - 37645:00

those who are interested in potentially

## 37645:00 - 37670:00

working with semi analysis who you work

## 37670:00 - 37690:00

with and where where they can learn

## 37690:00 - 37740:00

more? Sure. So we you know at semi

## 37740:00 - 37765:00

analysis.com we have you know the we

## 37765:00 - 37785:00

have the public stuff which is like all

## 37785:00 - 37830:00

these reports that are uh pseudo-free

## 37830:00 - 37885:00

but then we most of our work is done on

## 37885:00 - 37910:00

uh directly for clients there's these

## 37910:00 - 37945:00

data sets that we sell around every data

## 37945:00 - 37970:00

center in the world servers all the

## 37970:00 - 38005:00

compute where it's manufactured how many

## 38005:00 - 38040:00

where what's the cost and who's doing it

## 38040:00 - 38060:00

um and then we also do a lot of

## 38060:00 - 38085:00

consulting we've got people who have

## 38085:00 - 38120:00

worked all the way from ASML which makes

## 38120:00 - 38150:00

lithography tools all the way up to you

## 38150:00 - 38195:00

know Microsoft and Nvidia um which you

## 38195:00 - 38215:00

know making models and doing

## 38215:00 - 38240:00

infrastructure and so we've got this

## 38240:00 - 38265:00

whole gambit of you know folks there's

## 38265:00 - 38300:00

there's uh there's roughly 30 of us

## 38300:00 - 38340:00

across the world in US Taiwan Singapore

## 38340:00 - 38400:00

Japan uh France Germany um Canada so you

## 38400:00 - 38425:00

know there's a lot of uh engagement

## 38425:00 - 38445:00

points but if you want to reach out just

## 38445:00 - 38480:00

go to the website um you know go to one

## 38480:00 - 38520:00

of those specialized pages of models or

## 38520:00 - 38570:00

uh sales um and and and and reach out

## 38570:00 - 38590:00

and that that'd be the best way to sort

## 38590:00 - 38620:00

of interact and engage with us but for

## 38620:00 - 38645:00

most people just read the blog right

## 38645:00 - 38670:00

like I I think like unless you have

## 38670:00 - 38705:00

specialized like needs unless you're a

## 38705:00 - 38745:00

company in the space um or your investor

## 38745:00 - 38770:00

in the space like you know you just want

## 38770:00 - 38790:00

to be informed just read the blog and

## 38790:00 - 38825:00

it's free right um I think that's that's

## 38825:00 - 38865:00

the best option for most people yeah

## 38865:00 - 38895:00

well I I will attest the blog is

## 38895:00 - 38930:00

magnificent and Dylan is really a thrill

## 38930:00 - 38950:00

to get a chance to meet you and talk

## 38950:00 - 38970:00

through these topics with you so thanks

## 38970:00 - 39005:00

so much for coming on the show thank you

## 39005:00 - 39020:00

so much

## 39020:00 - 39055:00

Alex everybody thanks for listening

## 39055:00 - 39080:00

we'll be back on Friday to break down

## 39080:00 - 39105:00

the week's news until then we'll see you

## 39105:00+

next time on Big Technology podcast.

