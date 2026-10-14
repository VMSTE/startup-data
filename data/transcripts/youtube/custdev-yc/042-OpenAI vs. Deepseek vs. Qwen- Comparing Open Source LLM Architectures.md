---
source: https://www.youtube.com/watch?v=raTbhtKZTZA
title: "OpenAI vs. Deepseek vs. Qwen: Comparing Open Source LLM Architectures"
author: Y Combinator
date: 2025-08-29
views: 31407
description: >-
  OpenAI recently released its first open-weights model since GPT-2, entering a
  field led by DeepSeek and Alibaba's Qwen.


  YC's Ankit Gupta breaks down everything you need to know about these top OSS
  models, including what sets them apart under the hood. He’ll compare their
  approaches to mixture-of-experts, long-context training, and post-training
  techniques that shape reasoning and alignment—and explore how different design
  choices lead to surprisingly similar performance.


  Apply to Y Combinator: https://www.ycombinator.com/apply

  Work at a startup: https://www.ycombinator.com/jobs


  00:00 – OpenAI OSS Launch

  01:00 – Comparing Open Source LLM Architectures

  01:46 – GPT OSS Overview

  02:37 – Under The Hood of GPT OSS

  03:25 – Qwen-3 Architecture

  04:17 – Qwen-3 Training

  05:12 – Qwen-3 Post-Training

  06:08 – Qwen-3 Reasoning & RL Innovations

  06:52 – DeepSeek V3 Overview

  07:40 – DeepSeek V3.1 Updates

  08:39 – Attention Mechanism (MLA)

  09:39 – Comparing Model Sizes

  10:35 – Long Context Strategies

  11:25 – Reflections on Methods

  12:00 – Takeaways
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:42:38.382Z
---

# OpenAI vs. Deepseek vs. Qwen: Comparing Open Source LLM Architectures

## 00:00 - 45:00

OpenAI recently dropped GPT OSS, its

## 45:00 - 85:00

first open weights model since GPT2 in

## 85:00 - 120:00

2019. It's one of the highest profile

## 120:00 - 140:00

open source model launches since

## 140:00 - 180:00

DeepSeek R1 made waves back in January.

## 180:00 - 215:00

But how does GPT OSS compared to the

## 215:00 - 240:00

other top open source models out there

## 240:00 - 300:00

architecturally? Let's find out.

## 300:00 - 390:00

[Music]

## 390:00 - 425:00

GPT OSS is one of OpenAI's most

## 425:00 - 460:00

anticipated recent launches. a large

## 460:00 - 490:00

fully open weights model from one of the

## 490:00 - 525:00

leading American AI labs. Let's take a

## 525:00 - 550:00

closer look at the paper to find out how

## 550:00 - 580:00

it was actually engineered and trained.

## 580:00 - 625:00

GPT OSS is a mixture of experts model

## 625:00 - 665:00

available in two sizes, 120 billion

## 665:00 - 700:00

parameters and 20 billion parameters.

## 700:00 - 730:00

Each token activates the top four

## 730:00 - 755:00

experts, meaning only a portion of the

## 755:00 - 785:00

total parameters are used at any given

## 785:00 - 815:00

time. This allows for efficient

## 815:00 - 835:00

inference without sacrificing the

## 835:00 - 875:00

benefits of a larger model. Trained as a

## 875:00 - 915:00

decoder only transformer, GPTOSS

## 915:00 - 935:00

incorporates plenty of features typical

## 935:00 - 975:00

to modern LLMs. This includes grouped

## 975:00 - 1005:00

query attention, a modified attention

## 1005:00 - 1035:00

mechanism that lets multiple query heads

## 1035:00 - 1070:00

share the same key value pairs to reduce

## 1070:00 - 1105:00

memory use and speed up inference. It

## 1105:00 - 1135:00

also includes swiggloo activations in

## 1135:00 - 1165:00

the feed forward network layers which

## 1165:00 - 1190:00

allow for more nuance transformations

## 1190:00 - 1230:00

than simpler activations like RLU as

## 1230:00 - 1260:00

well as rotary positional embeddings or

## 1260:00 - 1290:00

rope which encode token position

## 1290:00 - 1320:00

directly into the attention mechanism to

## 1320:00 - 1360:00

support longer contexts. Finally, the

## 1360:00 - 1390:00

model also makes use of RMS norm with

## 1390:00 - 1425:00

pre-normalization, a normalization

## 1425:00 - 1455:00

method that scales inputs by their root

## 1455:00 - 1485:00

mean square for more stable training.

## 1485:00 - 1515:00

One standout capability of the model is

## 1515:00 - 1565:00

its 131,000 token context window, which

## 1565:00 - 1595:00

it achieves by applying yarn scaling

## 1595:00 - 1620:00

during pre-training rather than as an

## 1620:00 - 1650:00

inference time adjustment. We'll touch

## 1650:00 - 1675:00

on what this means a little bit later in

## 1675:00 - 1715:00

the video. For GPTO OSS, OpenAI makes

## 1715:00 - 1760:00

use of their open- source 0200K harmony

## 1760:00 - 1790:00

tokenizer. This bite pair encoding

## 1790:00 - 1835:00

tokenizer has over 200,000 tokens and

## 1835:00 - 1875:00

builds on the O200K tokenizer used in

## 1875:00 - 1915:00

models like GPT40. As for the data set

## 1915:00 - 1955:00

GPT OSS was trained on, OpenAI has only

## 1955:00 - 1985:00

disclosed the broad strokes. The model

## 1985:00 - 2015:00

was trained on a textonly corpus in the

## 2015:00 - 2055:00

trillions of tokens with a focus on stem

## 2055:00 - 2085:00

coding and general knowledge. Harmful

## 2085:00 - 2115:00

content was filtered out for safety, but

## 2115:00 - 2140:00

beyond that, there's little else known

## 2140:00 - 2170:00

publicly. Once training was complete,

## 2170:00 - 2195:00

the model was released in a quantized

## 2195:00 - 2225:00

format by default, making it lightweight

## 2225:00 - 2250:00

enough for deployment on modest

## 2250:00 - 2280:00

hardware. This allows it to be run on

## 2280:00 - 2320:00

consumer grade GPUs, laptops, or other

## 2320:00 - 2350:00

resource limited hardware. However,

## 2350:00 - 2370:00

there's no unquantized version

## 2370:00 - 2415:00

available. GPTOSS also underwent

## 2415:00 - 2440:00

substantial post-training for safety and

## 2440:00 - 2470:00

alignment, shaping its default behavior

## 2470:00 - 2505:00

for more controlled outputs. It's worth

## 2505:00 - 2525:00

noting that some in the open source

## 2525:00 - 2555:00

community are experimenting with

## 2555:00 - 2585:00

reducing or removing these layers in

## 2585:00 - 2610:00

order to explore the raw models

## 2610:00 - 2640:00

capabilities. In the broader landscape

## 2640:00 - 2685:00

of open source AI, GPToss arrives as a

## 2685:00 - 2715:00

fully equipped long context model ready

## 2715:00 - 2750:00

for immediate use. As impressive as it

## 2750:00 - 2785:00

is, however, it's just one of several

## 2785:00 - 2820:00

models in a rapidly expanding field of

## 2820:00 - 2865:00

open source LLMs. Quen 3, the newest

## 2865:00 - 2895:00

family of models developed by Alibaba

## 2895:00 - 2925:00

Cloud, dropped this past April to

## 2925:00 - 2960:00

considerable hype with benchmark scores

## 2960:00 - 2985:00

that rivaled those of leading open

## 2985:00 - 3020:00

source-based models like DeepSeek V3 or

## 3020:00 - 3060:00

Llama 4. The Quen 3 family includes both

## 3060:00 - 3085:00

dense models, which activate all of

## 3085:00 - 3115:00

their parameters for each query, and

## 3115:00 - 3145:00

mixture of expert models, which only

## 3145:00 - 3165:00

activate a small subset of their

## 3165:00 - 3195:00

parameters for each query. The dense

## 3195:00 - 3220:00

models come in seven different size

## 3220:00 - 3260:00

classes, including a6 billion parameter

## 3260:00 - 3290:00

model, one of the smallest current

## 3290:00 - 3320:00

generation openweight models around,

## 3320:00 - 3350:00

while the models come in two different

## 3350:00 - 3385:00

size classes. Architecturally, Quen 3

## 3385:00 - 3410:00

dense models are very similar to the

## 3410:00 - 3445:00

Quen 2.5 models, Alibaba's previous

## 3445:00 - 3495:00

releases. Like Quen 2.5 and GPOSS, Quen

## 3495:00 - 3525:00

3 incorporates features like group query

## 3525:00 - 3565:00

attention, swiggloo, rope, and RMS norm.

## 3565:00 - 3600:00

Quinn 3's sparse models share the same

## 3600:00 - 3625:00

fundamental architecture as its dense

## 3625:00 - 3655:00

models, but add a mixture of experts

## 3655:00 - 3690:00

layer with 128 total experts of which

## 3690:00 - 3735:00

eight are activated per token. All Quinn

## 3735:00 - 3765:00

3 models also use the same tokenizer

## 3765:00 - 3785:00

used in previous Quen models, which

## 3785:00 - 3820:00

implements bite level bite pair codings

## 3820:00 - 3850:00

that allow it to handle any text or

## 3850:00 - 3875:00

symbol without special pre-processing,

## 3875:00 - 3895:00

unlike word or character-based

## 3895:00 - 3925:00

tokenizers. One of the main things that

## 3925:00 - 3955:00

sets Quen 3 apart from previous Quen

## 3955:00 - 3985:00

models is the way it controls the scale

## 3985:00 - 4020:00

of the key query and value projections

## 4020:00 - 4060:00

to keep attention score stable at scale.

## 4060:00 - 4105:00

It replaces QKV bias, a static offset

## 4105:00 - 4150:00

that shifts KQV projections in previous

## 4150:00 - 4195:00

models with QK norm, a normalization

## 4195:00 - 4230:00

step that dynamically rescales that

## 4230:00 - 4260:00

query and key vectors to maintain

## 4260:00 - 4300:00

constant magnitudes. Data set wise, Quen

## 4300:00 - 4330:00

3 was trained on 36 trillion

## 4330:00 - 4355:00

pre-training tokens, twice as many as

## 4355:00 - 4390:00

the Quen 2.5 models. In addition to

## 4390:00 - 4420:00

pulling data from multilingual texts,

## 4420:00 - 4450:00

STEM and coding sources, and reasoning

## 4450:00 - 4500:00

tasks, Quen 3 also uses Quen 2.5 models

## 4500:00 - 4530:00

to generate trillions of tokens of

## 4530:00 - 4565:00

synthetic data in different formats like

## 4565:00 - 4590:00

textbooks, instructions, and code

## 4590:00 - 4625:00

snippets. Quen 3's pre-training occurred

## 4625:00 - 4655:00

in three stages. In stage one, the

## 4655:00 - 4680:00

general stage, models were trained on

## 4680:00 - 4715:00

over 30 trillion tokens covering 119

## 4715:00 - 4755:00

languages at a sequence length of 4096

## 4755:00 - 4785:00

tokens. In stage two, the reasoning

## 4785:00 - 4810:00

stage, models were trained on an

## 4810:00 - 4840:00

additional 5 trillion higher quality

## 4840:00 - 4875:00

tokens featuring more stem reasoning and

## 4875:00 - 4905:00

coding problems. And in stage three,

## 4905:00 - 4925:00

which the Quen team calls the long

## 4925:00 - 4960:00

context stage, context length was

## 4960:00 - 5000:00

extended to over 32,000 tokens using a

## 5000:00 - 5015:00

bunch of clever algorithmic

## 5015:00 - 5055:00

optimizations, including ABF, a

## 5055:00 - 5085:00

technique to adjust rope so positional

## 5085:00 - 5110:00

signals remain accurate over much longer

## 5110:00 - 5150:00

sequences, yarn to further scale for

## 5150:00 - 5185:00

longer inputs, and dual chunk attention

## 5185:00 - 5210:00

to process sequences efficiently.

## 5210:00 - 5235:00

Together, all of these optimizations

## 5235:00 - 5260:00

allow the model to reason over much

## 5260:00 - 5305:00

longer inputs at inference. Finally,

## 5305:00 - 5340:00

Quen uses a four-step post-training

## 5340:00 - 5370:00

pipeline with two goals. Giving users

## 5370:00 - 5400:00

more control over how much reasoning to

## 5400:00 - 5430:00

use for a given query and letting them

## 5430:00 - 5465:00

efficiently distill larger model

## 5465:00 - 5500:00

capabilities into smaller models. The

## 5500:00 - 5520:00

first step in the post- training

## 5520:00 - 5550:00

pipeline is a long chain of thought cold

## 5550:00 - 5580:00

start stage which involves feeding a

## 5580:00 - 5610:00

model a curated data set of challenging

## 5610:00 - 5645:00

reasoning problems from math logic and

## 5645:00 - 5680:00

STEM with verifiable reference answers

## 5680:00 - 5705:00

and then filtering outputs to ensure

## 5705:00 - 5735:00

quality. This is followed by a reasoning

## 5735:00 - 5785:00

RL stage using GRPO an RL algorithm

## 5785:00 - 5805:00

originally developed by Deepseek

## 5805:00 - 5845:00

researchers on roughly 4,000 query

## 5845:00 - 5885:00

verifier pairs to strengthen complex

## 5885:00 - 5915:00

problem solving. Personally, I think

## 5915:00 - 5940:00

it's fascinating that it only takes

## 5940:00 - 5980:00

4,000 pairs to get great results. The

## 5980:00 - 5995:00

third step in the post-training

## 5995:00 - 6035:00

pipeline, thinking mode fusion, is a key

## 6035:00 - 6060:00

Quen 3 innovation that integrates

## 6060:00 - 6085:00

reasoning and non-reasoning into a

## 6085:00 - 6115:00

single model, letting users switch modes

## 6115:00 - 6150:00

without changing models. Essentially,

## 6150:00 - 6175:00

what developers did in this step was

## 6175:00 - 6205:00

fine-tune the model on a mix of thinking

## 6205:00 - 6230:00

data, which includes intermediate

## 6230:00 - 6260:00

reasoning steps, and non-thinking data,

## 6260:00 - 6290:00

which omits them, and then build a chat

## 6290:00 - 6325:00

interface to let users toggle modes.

## 6325:00 - 6350:00

Though this was unique to Quinn when the

## 6350:00 - 6385:00

model first launched, GPT5 now features

## 6385:00 - 6410:00

a similar toggle. The final step,

## 6410:00 - 6450:00

general RL, broadens capabilities in

## 6450:00 - 6475:00

instruction following, formatting,

## 6475:00 - 6505:00

preference alignment, tool use, and

## 6505:00 - 6540:00

specialized scenarios. Quinn's

## 6540:00 - 6570:00

developers then use strong to weak

## 6570:00 - 6600:00

distillation, which allows for the

## 6600:00 - 6630:00

training of smaller models from larger

## 6630:00 - 6665:00

ones. All in all, Quen 3's performance

## 6665:00 - 6690:00

is very impressive, especially given its

## 6690:00 - 6725:00

relatively small size. But just months

## 6725:00 - 6750:00

earlier, a different model had already

## 6750:00 - 6780:00

raised the stakes in open source.

## 6780:00 - 6805:00

Released in December of last year,

## 6805:00 - 6840:00

Deepseek's V3 model was one of the most

## 6840:00 - 6865:00

ambitious open source LLMs to come out

## 6865:00 - 6890:00

of a major lab in recent years.

## 6890:00 - 6935:00

>> The chatbot developed in China called

## 6935:00 - 6950:00

Deep Seek.

## 6950:00 - 6980:00

>> Deepseek is such a fundamental change to

## 6980:00 - 7010:00

the economics of what's going on.

## 7010:00 - 7055:00

>> The most downloaded free app in the US.

## 7055:00 - 7090:00

This is an update in what people think

## 7090:00 - 7140:00

is possible. At 671 billion parameters

## 7140:00 - 7175:00

is a massive generalpurposebased model

## 7175:00 - 7200:00

designed for efficiency as much as

## 7200:00 - 7235:00

capability laying the groundwork for the

## 7235:00 - 7265:00

reasoning focused R1 model that would

## 7265:00 - 7290:00

follow. We're not going to get into a

## 7290:00 - 7325:00

ton of detail about V3's architecture or

## 7325:00 - 7350:00

training pipeline here because we put

## 7350:00 - 7380:00

out a comprehensive deep dive into it

## 7380:00 - 7415:00

back in February. But high level the

## 7415:00 - 7440:00

thing to know about V3 is that it's a

## 7440:00 - 7470:00

mixture of experts model with several

## 7470:00 - 7505:00

hardware and algorithmic optimizations

## 7505:00 - 7540:00

including training V3 natively in 8bit

## 7540:00 - 7580:00

rather than 16 or 32-bit. a huge unlock

## 7580:00 - 7610:00

for cutting training costs. And just

## 7610:00 - 7645:00

recently, DeepSeek pushed V3 even

## 7645:00 - 7680:00

further with an updated version. The

## 7680:00 - 7720:00

newly releasleased V3.1 builds directly

## 7720:00 - 7755:00

on the original V3based checkpoint,

## 7755:00 - 7785:00

extending it with a two-phase long

## 7785:00 - 7815:00

context training approach and adding a

## 7815:00 - 7840:00

hybrid thinking mode that lets the same

## 7840:00 - 7870:00

model switch between reasoning heavy and

## 7870:00 - 7910:00

lightweight inference. It also improves

## 7910:00 - 7940:00

tool use and agent performance thanks to

## 7940:00 - 7975:00

a more advanced post- training. In

## 7975:00 - 8020:00

practice, this means V3.1 keeps the same

## 8020:00 - 8060:00

core architecture as V3, but delivers

## 8060:00 - 8090:00

stronger reasoning, smarter tool use,

## 8090:00 - 8125:00

and greater performance. One thing that

## 8125:00 - 8155:00

sets V3 apart is that it uses a

## 8155:00 - 8190:00

different attention mechanism than GPOSS

## 8190:00 - 8235:00

and Quen 3. In modern LLMs, a lot of the

## 8235:00 - 8270:00

compute and memory is tied up in the KV

## 8270:00 - 8315:00

cache, and so V3 makes use of MLA, which

## 8315:00 - 8350:00

compresses keys and values into a

## 8350:00 - 8375:00

smaller latent space before caching

## 8375:00 - 8405:00

them, then decompresses them during

## 8405:00 - 8440:00

inference. Although MLA is a bit more

## 8440:00 - 8465:00

complex to implement, the previous

## 8465:00 - 8495:00

Deepseek V2 paper found it delivers

## 8495:00 - 8520:00

greater memory savings and better

## 8520:00 - 8550:00

modeling performance than GQA,

## 8550:00 - 8580:00

especially in huge long context models

## 8580:00 - 8610:00

like this one. And that's just one of

## 8610:00 - 8640:00

several areas where Deepseek V3 takes a

## 8640:00 - 8670:00

different path. With all that in mind,

## 8670:00 - 8710:00

let's take a step back from V3 to Quen

## 8710:00 - 8750:00

to GPDoss. How should we think about at

## 8750:00 - 8775:00

a high level the differences between

## 8775:00 - 8810:00

these models? One big difference is

## 8810:00 - 8845:00

size. The Quen 3 model family is the

## 8845:00 - 8870:00

only one of the three to offer both

## 8870:00 - 8900:00

dense and mixture of expert variants.

## 8900:00 - 8940:00

with dense models from 6 billion to 32

## 8940:00 - 8960:00

billion parameters and a mixture of

## 8960:00 - 8990:00

experts lineup that includes a 30

## 8990:00 - 9025:00

billion parameter model and a 235

## 9025:00 - 9060:00

billion parameter model. Notably, Quen's

## 9060:00 - 9090:00

mixture of experts base models matched

## 9090:00 - 9120:00

the dense models performance with only a

## 9120:00 - 9155:00

fifth as many active parameters. On the

## 9155:00 - 9190:00

other hand, Deepseek V3 only comes in a

## 9190:00 - 9230:00

mixture of experts architecture with 671

## 9230:00 - 9265:00

billion parameters of which 37 billion

## 9265:00 - 9290:00

are activated for a given token

## 9290:00 - 9320:00

prediction. So considerably larger than

## 9320:00 - 9365:00

even the biggest Quen 3 model. GPT OSS

## 9365:00 - 9390:00

sits in the middle. It offers twoe

## 9390:00 - 9435:00

models. One with 117 billion parameters

## 9435:00 - 9465:00

of which 5.1 billion are activated for a

## 9465:00 - 9500:00

given token and a smaller one with 21

## 9500:00 - 9535:00

billion parameters of which 3.6 billion

## 9535:00 - 9560:00

are activated for a given token. One of

## 9560:00 - 9575:00

the most interesting technical

## 9575:00 - 9605:00

differences lies in how each model

## 9605:00 - 9640:00

extends its context length. Yarn short

## 9640:00 - 9675:00

for yet another rope extension is a

## 9675:00 - 9695:00

technique for stretching the model's

## 9695:00 - 9730:00

rotary positional embeddings so that it

## 9730:00 - 9755:00

can handle far longer sequences than it

## 9755:00 - 9790:00

was originally trained on. Normally rope

## 9790:00 - 9810:00

starts to break down when you feed it

## 9810:00 - 9840:00

more tokens than its base frequency was

## 9840:00 - 9870:00

set for. But yarn tweaks that frequency.

## 9870:00 - 9905:00

So the same embedding space covers much

## 9905:00 - 9935:00

more ground. What's interesting is how

## 9935:00 - 9955:00

the three models here use it

## 9955:00 - 10000:00

differently. GPTOSS applies yarn right

## 10000:00 - 10030:00

from pre-training. So its weights have

## 10030:00 - 10070:00

learned to work natively with 131,000

## 10070:00 - 10115:00

token contexts. Deepsee takes a staged

## 10115:00 - 10145:00

approach fine-tuning after pre-training

## 10145:00 - 10190:00

to first reach 32,000 tokens, then

## 10190:00 - 10230:00

further training to achieve 128,000.

## 10230:00 - 10280:00

Quen also fine-tunes to 32,000, but

## 10280:00 - 10310:00

skips that additional retraining step.

## 10310:00 - 10345:00

Instead, at inference time, they apply

## 10345:00 - 10375:00

yarn scaling again, increasing the rope

## 10375:00 - 10400:00

base frequency by a factor of four to

## 10400:00 - 10440:00

reach 128,000 tokens without extra

## 10440:00 - 10485:00

retraining. In other words, GPTOSS is

## 10485:00 - 10525:00

born with long context ability. DeepSeek

## 10525:00 - 10555:00

is trained into it step by step, and

## 10555:00 - 10590:00

Quen pushes the limits of what a 32,000

## 10590:00 - 10625:00

train model can do without more long

## 10625:00 - 10655:00

context training. Personally, I think

## 10655:00 - 10675:00

one of the most interesting things about

## 10675:00 - 10700:00

these papers and the state-of-the-art in

## 10700:00 - 10725:00

deep learning more generally is that a

## 10725:00 - 10760:00

lot of these read as empirical findings.

## 10760:00 - 10785:00

Each lab describes the combination of

## 10785:00 - 10810:00

tools that works well for them, but

## 10810:00 - 10845:00

almost no one gives a first principles

## 10845:00 - 10870:00

justification of why one tool is better

## 10870:00 - 10905:00

than the other. For instance, why MLA is

## 10905:00 - 10940:00

better than GQA full stop. This is much

## 10940:00 - 10965:00

different from domains like math or

## 10965:00 - 10995:00

theoretical physics which are all about

## 10995:00 - 11025:00

providing first principles explanations

## 11025:00 - 11065:00

that derive results from axioms or laws.

## 11065:00 - 11090:00

Also, it's interesting that even though

## 11090:00 - 11115:00

most of these models have similar

## 11115:00 - 11145:00

topline benchmark statistics and use

## 11145:00 - 11175:00

broadly the same tools like attention

## 11175:00 - 11200:00

mechanisms, activation functions,

## 11200:00 - 11225:00

positional embeddings, and so on, they

## 11225:00 - 11255:00

achieve these similar results using

## 11255:00 - 11290:00

often very different techniques. This is

## 11290:00 - 11325:00

quite surprising. You'd expect that very

## 11325:00 - 11345:00

different training methods would lead to

## 11345:00 - 11380:00

very different results. Also, all of the

## 11380:00 - 11410:00

major models heavily use reinforcement

## 11410:00 - 11430:00

learning as part of the post-raining and

## 11430:00 - 11455:00

reasoning portions of their model

## 11455:00 - 11480:00

training efforts. And it's fascinating

## 11480:00 - 11505:00

and pretty surprising how some of these

## 11505:00 - 11540:00

RL efforts require very little amounts

## 11540:00 - 11575:00

of data. just 4,000 data pairs in the

## 11575:00 - 11605:00

case of Quinn. Another point here is

## 11605:00 - 11625:00

that it's very opaque what the

## 11625:00 - 11650:00

differences in data sets are between the

## 11650:00 - 11675:00

labs. It's clear from the papers that

## 11675:00 - 11695:00

there's an enormous amount of work

## 11695:00 - 11720:00

happening behind the scenes in data set

## 11720:00 - 11745:00

engineering. This work is probably a

## 11745:00 - 11770:00

significant aspect of the moat that

## 11770:00 - 11790:00

makes these companies comfortable

## 11790:00 - 11820:00

releasing their models. It's very

## 11820:00 - 11835:00

difficult to replicate what they're

## 11835:00 - 11865:00

releasing. So the big takeaway when

## 11865:00 - 11890:00

reading these papers is you shouldn't

## 11890:00 - 11920:00

focus too much on just the benchmark

## 11920:00 - 11950:00

performance or topline stats like

## 11950:00 - 11985:00

context size. Instead, look at the

## 11985:00 - 12015:00

specific methods that these labs are

## 12015:00 - 12050:00

using to achieve those results. There

## 12050:00 - 12080:00

are tons of high performing open source

## 12080:00 - 12100:00

models that we didn't discuss in this

## 12100:00 - 12145:00

video, like Kim K2 or Google Gemma 3.

## 12145:00 - 12165:00

But when you peek under the hood of many

## 12165:00 - 12200:00

of these, you'll find nuance differences

## 12200:00 - 12230:00

that I find really interesting. I hope

## 12230:00 - 12255:00

this gives you a framework for how to

## 12255:00 - 12275:00

understand the latest open source

## 12275:00 - 12305:00

releases and gives you a toolkit to

## 12305:00 - 12335:00

start tinkering with them yourself.

## 12335:00 - 12355:00

Thanks for watching. See you in the next

## 12355:00 - 12390:00

episode.

## 12390:00+

[Music]

