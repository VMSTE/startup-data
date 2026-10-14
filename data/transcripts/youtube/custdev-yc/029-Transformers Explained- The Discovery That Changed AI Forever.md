---
source: https://www.youtube.com/watch?v=JZLZQVmfGn8
title: "Transformers Explained: The Discovery That Changed AI Forever"
author: Y Combinator
date: 2025-10-23
views: 91517
description: >-
  Nearly every modern AI model, from ChatGPT and Claude to Gemini and Grok, is
  built on the same foundation: the Transformer.


  In this video, YC's Ankit Gupta traces how AI learned to understand language —
  from early RNNs and LSTMs to attention mechanisms and the breakthrough 2017
  paper Attention Is All You Need — the discovery that unlocked the modern AI
  era.
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:40:48.386Z
---

# Transformers Explained: The Discovery That Changed AI Forever

## 00:00 - 35:00

Nearly every state-of-the-art AI system,

## 35:00 - 70:00

whether it's ChatGPT, Claude, Gemini, or

## 70:00 - 105:00

Grok, is built on the same underlying

## 105:00 - 145:00

model architecture, the Transformer. But

## 145:00 - 165:00

where did the Transformer architecture

## 165:00 - 200:00

come from? And what can its development

## 200:00 - 225:00

teach us about the way breakthroughs in

## 225:00 - 255:00

AI happen? Let's dive in.

## 255:00 - 380:00

[Music]

## 380:00 - 405:00

A Transformer is a neural network that

## 405:00 - 445:00

uses self-attention to take input data,

## 445:00 - 475:00

like text or images, model the

## 475:00 - 510:00

relationships between that data, and

## 510:00 - 535:00

finally generate outputs, like

## 535:00 - 570:00

meaningful text responses, translations,

## 570:00 - 600:00

or classifications. Many people know

## 600:00 - 620:00

that the original Transformer

## 620:00 - 645:00

architecture was introduced in a

## 645:00 - 690:00

now-famous 2017 paper from Google called

## 690:00 - 710:00

"Attention Is All You Need." But what

## 710:00 - 735:00

you might not know about are the

## 735:00 - 760:00

breakthroughs that made this overnight

## 760:00 - 795:00

success possible. There are three key

## 795:00 - 825:00

developments that we'll discuss today:

## 825:00 - 860:00

long short-term memory, seek-to-seek

## 860:00 - 885:00

with attention, and then finally,

## 885:00 - 920:00

Transformers. Let's start with long

## 920:00 - 955:00

short-term memory networks, or LSTMs.

## 955:00 - 985:00

One of the core challenges motivating

## 985:00 - 1020:00

early AI research was to get neural

## 1020:00 - 1055:00

networks to understand sequences.

## 1055:00 - 1075:00

Natural language is inherently

## 1075:00 - 1105:00

sequential. The meaning of a word

## 1105:00 - 1145:00

depends on what comes before it or after

## 1145:00 - 1175:00

it, and understanding an entire sentence

## 1175:00 - 1210:00

requires maintaining context across many

## 1210:00 - 1245:00

words. Early architectures, like

## 1245:00 - 1275:00

feedforward neural networks, process

## 1275:00 - 1305:00

each input in isolation, and so they

## 1305:00 - 1325:00

weren't capable of understanding

## 1325:00 - 1360:00

context, or they required looking at

## 1360:00 - 1390:00

inputs of a fixed length. So,

## 1390:00 - 1415:00

researchers developed recurrent neural

## 1415:00 - 1450:00

networks, or RNNs, as a solution to

## 1450:00 - 1490:00

this. In simple terms, an RNN iterates

## 1490:00 - 1530:00

over the inputs in order, one at a time,

## 1530:00 - 1560:00

and consumes the previous outputs as

## 1560:00 - 1595:00

additional input at each step. So, if an

## 1595:00 - 1630:00

input is of length N, there are N

## 1630:00 - 1670:00

feedforward pass steps. And as a result,

## 1670:00 - 1700:00

during the backwards pass, the gradient

## 1700:00 - 1735:00

with respect to the early inputs is the

## 1735:00 - 1780:00

result of N matrix multiplications.

## 1780:00 - 1805:00

Now, in practice, this meant that we

## 1805:00 - 1835:00

often face a problem called vanishing

## 1835:00 - 1870:00

gradients. The early inputs in a

## 1870:00 - 1910:00

sequence had less and less influence on

## 1910:00 - 1935:00

the network's output as the sequence

## 1935:00 - 1955:00

grew longer, because it went through

## 1955:00 - 1995:00

these multiple matrix multiplications.

## 1995:00 - 2025:00

Gradients, which are the signals used to

## 2025:00 - 2055:00

adjust weights during training, would

## 2055:00 - 2080:00

fade to near zero as they were passed

## 2080:00 - 2115:00

backwards through time.

## 2115:00 - 2155:00

In the 1990s, Hochreiter and Schmidhuber

## 2155:00 - 2180:00

proposed a solution to this. It was

## 2180:00 - 2205:00

called the long short-term memory

## 2205:00 - 2255:00

network, or LSTMs. LSTMs were a type of

## 2255:00 - 2290:00

RNN that attempted to fix the vanishing

## 2290:00 - 2325:00

gradient problem by introducing gates,

## 2325:00 - 2345:00

which could learn what information to

## 2345:00 - 2390:00

keep, update, or forget. This made it

## 2390:00 - 2415:00

possible to learn long-range

## 2415:00 - 2445:00

dependencies, something vanilla RNNs

## 2445:00 - 2480:00

struggled with. But LSTMs were too

## 2480:00 - 2515:00

expensive to train at scale in the '90s,

## 2515:00 - 2545:00

and so progress stalled. Now, you fast

## 2545:00 - 2585:00

forward to the early 2010s, and GPU

## 2585:00 - 2615:00

acceleration, better optimization

## 2615:00 - 2640:00

techniques, and new large-scale data

## 2640:00 - 2675:00

sets brought LSTMs back into the

## 2675:00 - 2710:00

spotlight. Suddenly, this relatively old

## 2710:00 - 2740:00

architecture was viable again, and it

## 2740:00 - 2760:00

began to dominate natural language

## 2760:00 - 2795:00

processing. LSTMs were quickly adopted

## 2795:00 - 2825:00

for everything from speech recognition

## 2825:00 - 2860:00

to language modeling. In these years,

## 2860:00 - 2885:00

NLP and computer vision were actually

## 2885:00 - 2930:00

somewhat separate worlds. RNNs and LSTMs

## 2930:00 - 2950:00

in particular were preeminent in

## 2950:00 - 2980:00

language tasks, while convolutional

## 2980:00 - 3015:00

neural networks, or CNNs, were winning

## 3015:00 - 3045:00

in vision. But the basic question

## 3045:00 - 3085:00

motivating both NLP and computer vision

## 3085:00 - 3110:00

was the same: How do you model

## 3110:00 - 3140:00

sequences? How do you let those models

## 3140:00 - 3175:00

capture structure that spans time or

## 3175:00 - 3220:00

space? LSTMs were a huge step forward,

## 3220:00 - 3250:00

but they still had limitations. The most

## 3250:00 - 3275:00

fundamental was something called the

## 3275:00 - 3310:00

fixed-length bottleneck. Here's how most

## 3310:00 - 3335:00

early LSTM systems worked. For

## 3335:00 - 3360:00

sequence-to-sequence tasks like

## 3360:00 - 3385:00

translation, you would take the input

## 3385:00 - 3430:00

sentence, feed it into an encoder LSTM,

## 3430:00 - 3460:00

and boil the input down to a single

## 3460:00 - 3510:00

fixed-size vector. Then, a decoder LSTM

## 3510:00 - 3540:00

would take that and try to construct the

## 3540:00 - 3575:00

target sentence word by word. This

## 3575:00 - 3600:00

yielded impressive results on the

## 3600:00 - 3635:00

benchmarks of that era. But in practice,

## 3635:00 - 3665:00

that single vector was still unable to

## 3665:00 - 3695:00

accurately capture the meaning of long

## 3695:00 - 3725:00

or complex sentences.

## 3725:00 - 3755:00

Also, there wasn't a great way to encode

## 3755:00 - 3790:00

the concept of order into a fixed-size

## 3790:00 - 3820:00

vector. This was very important in

## 3820:00 - 3845:00

translation tasks. For example, in

## 3845:00 - 3880:00

English, we put adjectives before nouns,

## 3880:00 - 3900:00

and in Spanish, we often place

## 3900:00 - 3935:00

adjectives after nouns. You'd see this

## 3935:00 - 3975:00

in performance. These models worked okay

## 3975:00 - 4000:00

on short inputs, but they quickly fell

## 4000:00 - 4030:00

apart as sequences got longer. And

## 4030:00 - 4055:00

truthfully, this was more than a

## 4055:00 - 4080:00

performance issue. It pointed to a

## 4080:00 - 4120:00

deeper architectural problem. Allowing

## 4120:00 - 4150:00

the decoder to only see one static

## 4150:00 - 4185:00

summary of the input was a fundamental

## 4185:00 - 4220:00

limitation. Why not give it access to

## 4220:00 - 4245:00

all the intermediate information that

## 4245:00 - 4280:00

the encoder saw? This sort of insight is

## 4280:00 - 4315:00

what gave rise to the next big leap. In

## 4315:00 - 4350:00

2014, a paper introduced what would

## 4350:00 - 4375:00

become the new standard for sequence

## 4375:00 - 4410:00

translation: sequence-to-sequence, or

## 4410:00 - 4455:00

seq2seq, models with attention. Like

## 4455:00 - 4490:00

before, the core idea was to train two

## 4490:00 - 4520:00

neural networks jointly: an encoder,

## 4520:00 - 4545:00

which reads the input sequence and

## 4545:00 - 4575:00

builds a representation of it, and a

## 4575:00 - 4600:00

decoder, which generates the output

## 4600:00 - 4635:00

sequence one step at a time.

## 4635:00 - 4670:00

Both models were LSTMs, and crucially,

## 4670:00 - 4700:00

they were trained together end to end.

## 4700:00 - 4725:00

But there was a key insight that enabled

## 4725:00 - 4770:00

this performance jump: attention.

## 4770:00 - 4805:00

Even though seq2seq used a fixed-length

## 4805:00 - 4835:00

vector, researchers realized that if you

## 4835:00 - 4870:00

could let the decoder look back, or

## 4870:00 - 4920:00

attend to, the encoder's hidden states,

## 4920:00 - 4940:00

you could let the model learn how to

## 4940:00 - 4975:00

align parts of the input to parts of the

## 4975:00 - 5025:00

output. Bahdanau, Cho, and Bengio showed

## 5025:00 - 5050:00

that these models could significantly

## 5050:00 - 5080:00

outperform traditional rule-based

## 5080:00 - 5115:00

systems and the existing seq2seq models

## 5115:00 - 5145:00

on tasks like machine translation. That

## 5145:00 - 5175:00

was a big deal. These models were

## 5175:00 - 5205:00

evaluated on translation benchmarks and

## 5205:00 - 5220:00

showed near state-of-the-art

## 5220:00 - 5250:00

performance, beating even the best

## 5250:00 - 5280:00

statistical systems at the time. It was

## 5280:00 - 5310:00

a sign that neural models could compete

## 5310:00 - 5335:00

head-to-head with the mature

## 5335:00 - 5370:00

production-grade systems of old. And for

## 5370:00 - 5395:00

many people, this was the first moment

## 5395:00 - 5410:00

they began to see these models in

## 5410:00 - 5455:00

practice. This was real, usable NLP. For

## 5455:00 - 5485:00

example, Google Translate adopted a

## 5485:00 - 5515:00

neural seq2seq architecture around this

## 5515:00 - 5545:00

time, and you may remember this as the

## 5545:00 - 5570:00

era in which Google Translate started to

## 5570:00 - 5600:00

finally work well.

## 5600:00 - 5630:00

This insight, learning to align and

## 5630:00 - 5650:00

translate at the same time, was

## 5650:00 - 5680:00

transformative, and it wouldn't just

## 5680:00 - 5720:00

stay in NLP. One of the original seq2seq

## 5720:00 - 5755:00

authors, Yoshua Bengio, soon applied

## 5755:00 - 5785:00

similar alignment-based architectures to

## 5785:00 - 5820:00

computer vision. This was the first sign

## 5820:00 - 5840:00

that these sequence models might be

## 5840:00 - 5875:00

useful beyond language. But even when

## 5875:00 - 5905:00

augmented with attention, RNNs were

## 5905:00 - 5930:00

still constrained by their sequential

## 5930:00 - 5965:00

architecture. Processing tokens one at a

## 5965:00 - 5990:00

time made it challenging to run

## 5990:00 - 6020:00

computations in parallel across time

## 6020:00 - 6060:00

steps, so runtimes scaled linearly with

## 6060:00 - 6095:00

sequence length. This made training

## 6095:00 - 6125:00

models on large data sets, the kinds we

## 6125:00 - 6150:00

knew would be necessary to achieve

## 6150:00 - 6200:00

broadly useful AI, intractably slow. In

## 6200:00 - 6230:00

an attempt to speed up RNNs, researchers

## 6230:00 - 6255:00

developed techniques like factorizing

## 6255:00 - 6290:00

LSTM matrices into smaller matrix

## 6290:00 - 6315:00

products, or conditionally activating

## 6315:00 - 6335:00

only parts of a network that were

## 6335:00 - 6375:00

relevant to a query. But the fundamental

## 6375:00 - 6410:00

linear runtime constraint remained. Then

## 6410:00 - 6445:00

came the big breakthrough in 2017, when

## 6445:00 - 6465:00

a team of researchers at Google

## 6465:00 - 6490:00

published a paper called "Attention Is

## 6490:00 - 6520:00

All You Need," which proposed a new

## 6520:00 - 6545:00

machine translation architecture that

## 6545:00 - 6580:00

they called a Transformer. Transformers

## 6580:00 - 6615:00

scrapped recurrence entirely, instead

## 6615:00 - 6655:00

relying solely on an attention mechanism

## 6655:00 - 6695:00

to generate outputs. We won't get fully

## 6695:00 - 6720:00

into the technical weeds of Transformers

## 6720:00 - 6750:00

here. For that, check out Andrej

## 6750:00 - 6785:00

Karpathy's fantastic explainer. But at a

## 6785:00 - 6820:00

high level, Transformers use a modified

## 6820:00 - 6840:00

version of the encoder-decoder

## 6840:00 - 6870:00

architecture originally proposed in

## 6870:00 - 6910:00

seq2seq. Instead of compressing inputs

## 6910:00 - 6940:00

into a single vector embedding,

## 6940:00 - 6965:00

Transformers kept separate embeddings

## 6965:00 - 7000:00

for each input token and updated these

## 7000:00 - 7035:00

through self-attention, a mechanism that

## 7035:00 - 7065:00

updated token representations based on a

## 7065:00 - 7100:00

learned weighted dot product over the

## 7100:00 - 7130:00

embeddings of all other tokens in the

## 7130:00 - 7160:00

sequence. Because each token in this

## 7160:00 - 7190:00

architecture could attend to all others

## 7190:00 - 7220:00

simultaneously, Transformers could

## 7220:00 - 7260:00

process an entire sequence in parallel,

## 7260:00 - 7285:00

making them dramatically faster than

## 7285:00 - 7320:00

RNNs. Remarkably, they were also much

## 7320:00 - 7350:00

more accurate on machine translation

## 7350:00 - 7385:00

benchmarks. Over the next few years,

## 7385:00 - 7415:00

researchers started to experiment with

## 7415:00 - 7440:00

different variations of the Transformer

## 7440:00 - 7475:00

architecture. The architecture described

## 7475:00 - 7510:00

in the original Google paper featured an

## 7510:00 - 7535:00

encoder and decoder that each had

## 7535:00 - 7565:00

self-attention and cross-attention

## 7565:00 - 7590:00

between the two. This resembled the

## 7590:00 - 7620:00

original seq2seq architectures, but

## 7620:00 - 7655:00

without the recurrence. The next several

## 7655:00 - 7685:00

years saw a lot of innovation in the

## 7685:00 - 7720:00

Transformer architecture itself. For

## 7720:00 - 7750:00

example, a series of models called BERT

## 7750:00 - 7785:00

focused on using only the encoder to do

## 7785:00 - 7825:00

masked language modeling. In parallel,

## 7825:00 - 7860:00

efforts to use only the decoder for

## 7860:00 - 7890:00

autoregressive modeling gave rise to

## 7890:00 - 7935:00

OpenAI's GPT series of models. At a high

## 7935:00 - 7960:00

level, we can describe both of these

## 7960:00 - 8000:00

model series as subsets of the original

## 8000:00 - 8015:00

Attention Is All You Can Need

## 8015:00 - 8045:00

Transformer model. It quickly became

## 8045:00 - 8075:00

clear that these models could scale to

## 8075:00 - 8115:00

large numbers of parameters. Ultimately,

## 8115:00 - 8145:00

one model type, the generative

## 8145:00 - 8180:00

pre-trained Transformer model, or GPT,

## 8180:00 - 8210:00

would be scaled up to create the LLMs

## 8210:00 - 8235:00

that we regularly use today in products

## 8235:00 - 8275:00

like ChatGPT or Claude. But not that

## 8275:00 - 8300:00

long ago, it wasn't obvious that there

## 8300:00 - 8345:00

might be one model to rule them all. In

## 8345:00 - 8370:00

fact, people were training variants of

## 8370:00 - 8410:00

model architectures for every task: one

## 8410:00 - 8435:00

for machine translation, another for

## 8435:00 - 8475:00

named entity recognition, and so on.

## 8475:00 - 8505:00

Each with a shared backbone, but slight

## 8505:00 - 8540:00

differences in the final model layers.

## 8540:00 - 8570:00

These models were intelligent in that

## 8570:00 - 8600:00

their accuracy was high, but they were

## 8600:00 - 8640:00

largely single-task models. Also, at

## 8640:00 - 8655:00

this point, there wasn't really a

## 8655:00 - 8690:00

concept of prompting the models, because

## 8690:00 - 8720:00

there was no chat interface. Instead,

## 8720:00 - 8740:00

people interacted with the models

## 8740:00 - 8780:00

through domain-specific inputs. It was

## 8780:00 - 8810:00

only as the labs started to experiment

## 8810:00 - 8840:00

with training autoregressive models on

## 8840:00 - 8875:00

much larger data sets that they began to

## 8875:00 - 8900:00

look and feel more like generally

## 8900:00 - 8940:00

intelligent systems. Hopefully, this

## 8940:00 - 8960:00

history helped contextualize some of

## 8960:00 - 8980:00

what it took to get these models to a

## 8980:00 - 9020:00

place of being able to scale them. In

## 9020:00 - 9045:00

the next video, we'll talk about some of

## 9045:00 - 9070:00

the architectural and engineering

## 9070:00 - 9100:00

innovations it took to actually get them

## 9100:00 - 9130:00

to their current performance levels.

## 9130:00 - 9145:00

Thanks for watching.

## 9145:00+

[Music]

