---
source: https://www.youtube.com/watch?v=nlSK8NA8ClU
title: "AI's Research Frontier: Memory, World Models, & Planning — With Joelle Pineau"
author: Alex Kantrowitz
date: 2026-02-06
views: 22517
description: >-
  Joelle Pineau is the chief AI officer at Cohere. Pineau joins Big Technology
  Podcast to discuss where the cutting edge of AI research is headed — and what
  it will take to move from impressive demos to reliable agents. Tune in to hear
  why memory, world models, and more efficient reasoning are emerging as the
  next big frontiers, plus what current approaches are missing. We also cover
  the “capability overhang” in enterprise AI, why consumer assistants still
  aren’t lighting the world on fire, what AI sovereignty actually means, and
  whether the major labs can ever pull away from each other. Hit play for a
  cool-headed, deeply practical look at what’s next for AI and how it gets
  deployed in the real world.


  Chapters:

  0:00 - Intro: Where AI research is heading

  2:02 - Current cutting edge of AI research

  5:14 - Memory vs. continual learning in AI models

  9:46 - Why memory is so difficult

  14:23 - State of reasoning and hierarchical planning

  17:19 - How LLMs think ahead while generating text

  19:00 - World models and embedded physics understanding

  21:32 - Physical vs. digital world models

  24:13 - Do models need to understand gravity for AGI?

  25:51 - The capability overhang in AI

  28:22 - Why consumer AI assistants aren't taking off

  30:42 - Companies vs. individuals adopting AI

  31:44 - Why AI labs stay neck-and-neck competitively

  33:41 - Commercial applications of AI in enterprise

  38:11 - Impact on entry-level and mid-career employees

  41:12 - AI coding agents and vibe coding

  43:13 - Concentration of AI in big tech companies

  46:23 - Social media entrepreneurs vs. research scientists

  48:09 - Economics of AI advertising

  51:02 - Can the pace of AI adoption keep up?

  ---


  Enjoying Big Technology Podcast? Please rate us five stars ⭐⭐⭐⭐⭐ in your
  podcast app of choice.


  Want a discount for Big Technology on Substack + Discord? Here’s 25% off for
  the first year: https://www.bigtechnology.com/subscribe?coupon=0843016b
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:28:18.688Z
---

# AI's Research Frontier: Memory, World Models, & Planning — With Joelle Pineau

## 00:00 - 30:00

Where is the cutting edge of AI research

## 30:00 - 65:00

leading today and how are some companies

## 65:00 - 100:00

already putting it into action? Let's

## 100:00 - 130:00

talk about it with cohhere chief AI

## 130:00 - 180:00

officer Joel Pino right after this.

## 180:00 - 210:00

Welcome to Big Technology Podcast, a

## 210:00 - 240:00

show for Coolheaded and Nuance

## 240:00 - 275:00

conversation of the tech world and

## 275:00 - 310:00

beyond. Today, we're going to look deep

## 310:00 - 350:00

into the state of AI research, where the

## 350:00 - 385:00

cutting edge is leading, whether there

## 385:00 - 410:00

are limitations with the current

## 410:00 - 450:00

methodologies, and how some companies

## 450:00 - 485:00

are already putting this technology into

## 485:00 - 515:00

action in a practical way. We're joined

## 515:00 - 550:00

by the perfect guest, Joel Pino, is

## 550:00 - 585:00

here. She's the chief AI scientist at

## 585:00 - 620:00

Coher. Joel, welcome to the show.

## 620:00 - 645:00

>> Thank you. Glad to be here.

## 645:00 - 690:00

>> So, for those that don't know Joelle, uh

## 690:00 - 740:00

she is a a you know, a researcher who's

## 740:00 - 780:00

been at this for a long time. You and I

## 780:00 - 830:00

met uh actually maybe a month after Chad

## 830:00 - 865:00

GPT was released and everybody was

## 865:00 - 915:00

asking whether AI was sentient. You at

## 915:00 - 945:00

that time were the head of the

## 945:00 - 985:00

fundamental AI research division at

## 985:00 - 1030:00

Meta. Uh you you're also a professor at

## 1030:00 - 1070:00

McGill and currently you're the chief AI

## 1070:00 - 1100:00

officer at Coher Coher. We've had Aiden

## 1100:00 - 1135:00

Gomez on the show. He founded the

## 1135:00 - 1170:00

company in 2019. He's also one of the

## 1170:00 - 1205:00

authors of the attention is all you need

## 1205:00 - 1240:00

paper which basically kicked off the

## 1240:00 - 1300:00

generative AI moment. Um so coher is uh

## 1300:00 - 1340:00

seven years old at this point six seven

## 1340:00 - 1385:00

years old uh for the kids out there. Uh

## 1385:00 - 1440:00

it's raised 1.6 billion. It's worth 7

## 1440:00 - 1480:00

billion and it sells AI to enterprise.

## 1480:00 - 1510:00

So that sets the stage.

## 1510:00 - 1520:00

>> Yes.

## 1520:00 - 1550:00

>> Let's talk a little bit about AI

## 1550:00 - 1595:00

research. Uh there's so much discussion

## 1595:00 - 1625:00

people have been talking about whether

## 1625:00 - 1670:00

AI research is going to hit a wall and

## 1670:00 - 1715:00

whether you know these new methodologies

## 1715:00 - 1740:00

things like putting reinforcement

## 1740:00 - 1770:00

learning on top of large language models

## 1770:00 - 1825:00

going through reasoning um uh teaching

## 1825:00 - 1870:00

the models to use different tools. Um

## 1870:00 - 1895:00

there's so many different opinions of

## 1895:00 - 1935:00

where to focus right now. So what in

## 1935:00 - 1985:00

your opinion is the cutting edge of AI

## 1985:00 - 2005:00

research and where do you think it's

## 2005:00 - 2065:00

going to lead? M well I'm certainly not

## 2065:00 - 2100:00

worried about research hitting a wall

## 2100:00 - 2130:00

like there's so many questions that we

## 2130:00 - 2165:00

need to work on right now and I'd

## 2165:00 - 2205:00

separate it into two two interesting

## 2205:00 - 2250:00

angles right one is like what are the

## 2250:00 - 2290:00

right problems to be solving right now

## 2290:00 - 2325:00

what are the the things that the models

## 2325:00 - 2355:00

the current generation of models we have

## 2355:00 - 2395:00

can't do and then there's a question of

## 2395:00 - 2430:00

like how do we go about it right like

## 2430:00 - 2465:00

what's the hypothesis

## 2465:00 - 2495:00

that may give us the clue to how to

## 2495:00 - 2530:00

solve some of these problems So in terms

## 2530:00 - 2570:00

of of what problems to solve, I think um

## 2570:00 - 2620:00

an important one is um what do we do

## 2620:00 - 2660:00

about memory? Uh machines have the

## 2660:00 - 2690:00

ability to remember tremendous amounts

## 2690:00 - 2715:00

of information. You're just like

## 2715:00 - 2760:00

stocking it in there. The hard part is

## 2760:00 - 2800:00

knowing like when to pull on what piece

## 2800:00 - 2850:00

of information to make a prediction, to

## 2850:00 - 2900:00

generate information, to reason. And so

## 2900:00 - 2935:00

having this ability to be a lot more

## 2935:00 - 2985:00

selective about the all the information

## 2985:00 - 3020:00

you've seen in context is super

## 3020:00 - 3055:00

important. And already transformers were

## 3055:00 - 3085:00

an important piece of that. You know,

## 3085:00 - 3115:00

attention is all you need. Well, it

## 3115:00 - 3140:00

turns out it's not all you need. You

## 3140:00 - 3155:00

need a little bit more than that. You

## 3155:00 - 3185:00

need the ability to reason about

## 3185:00 - 3225:00

information at different time scales, at

## 3225:00 - 3255:00

different granularity, and so on and so

## 3255:00 - 3285:00

forth. So there's definitely a good

## 3285:00 - 3320:00

piece of work to be done there which

## 3320:00 - 3345:00

really involves and now we talk about

## 3345:00 - 3380:00

the how you know the choice of

## 3380:00 - 3405:00

architecture the choice of learning

## 3405:00 - 3450:00

mechanisms the type of data sets the

## 3450:00 - 3485:00

type of use cases that we need to we

## 3485:00 - 3520:00

need to look into.

## 3520:00 - 3560:00

Another big research theme is on

## 3560:00 - 3595:00

building world models. We hear a lot

## 3595:00 - 3640:00

about world models which are essentially

## 3640:00 - 3670:00

the ability to take in all this

## 3670:00 - 3720:00

information and predict the effect of

## 3720:00 - 3760:00

actions you know. So when we talk about

## 3760:00 - 3805:00

causality, how are actions transforming

## 3805:00 - 3835:00

the world? This is what a world model

## 3835:00 - 3875:00

should be able to do. World models are

## 3875:00 - 3915:00

absolutely essential when you want to

## 3915:00 - 3945:00

build agents because these agents are

## 3945:00 - 3965:00

going to take actions which is going to

## 3965:00 - 3990:00

change the world. You want to be able to

## 3990:00 - 4015:00

predict these effects. So whether you're

## 4015:00 - 4045:00

building robots and then we talk about

## 4045:00 - 4085:00

physical world models but also the

## 4085:00 - 4125:00

agents getting deployed on the web you

## 4125:00 - 4165:00

need to build digital world models so

## 4165:00 - 4190:00

that these agents you know whether

## 4190:00 - 4220:00

they're making financial decisions

## 4220:00 - 4260:00

communicating on your behalf organizing

## 4260:00 - 4290:00

meetings that they have the ability to

## 4290:00 - 4315:00

predict the consequence of their

## 4315:00 - 4355:00

actions. So that's a big theme and

## 4355:00 - 4390:00

there's a lot of different hypotheses

## 4390:00 - 4430:00

about how to go about building these

## 4430:00 - 4470:00

world models. And and the third theme

## 4470:00 - 4515:00

I'm I'll highlight and there's many more

## 4515:00 - 4555:00

but like me at least pick out the top

## 4555:00 - 4625:00

three choice um is about how do we uh

## 4625:00 - 4680:00

build in reasoning efficiently. Um and

## 4680:00 - 4710:00

right now a lot of the reasoning methods

## 4710:00 - 4750:00

are still uh quite thorough based on

## 4750:00 - 4790:00

sort of forward search methods and and

## 4790:00 - 4825:00

learning the right reward function. But

## 4825:00 - 4860:00

I do think there's, you know, like the

## 4860:00 - 4900:00

the transformer moment for for reasoning

## 4900:00 - 4945:00

and choosing action and being able to

## 4945:00 - 4995:00

plan at different levels of granularity.

## 4995:00 - 5030:00

We're still far away from doing that.

## 5030:00 - 5075:00

And so there's all sorts of ways that

## 5075:00 - 5115:00

it's being baked in, you know, LLM as a

## 5115:00 - 5145:00

judge and things like that where AI

## 5145:00 - 5180:00

systems give feedback to AI systems in

## 5180:00 - 5225:00

order to train them is still very early

## 5225:00 - 5240:00

days.

## 5240:00 - 5270:00

>> Okay. I I want to dig into a lot of what

## 5270:00 - 5295:00

you just said. Let's start at the

## 5295:00 - 5335:00

beginning. Let's start with memory. Uh,

## 5335:00 - 5370:00

is memory and continual learning two

## 5370:00 - 5410:00

sides of the same coin? I mean, there's

## 5410:00 - 5465:00

this idea that the models can search the

## 5465:00 - 5490:00

web and they can find something in a

## 5490:00 - 5510:00

session, but as soon as you close that

## 5510:00 - 5560:00

session, they forget it. Um, and I guess

## 5560:00 - 5585:00

the reason why I'm going there is

## 5585:00 - 5620:00

because a way that some people have

## 5620:00 - 5650:00

suggested solving both of these is just

## 5650:00 - 5685:00

making the context window massive and

## 5685:00 - 5710:00

then just becoming efficient in the way

## 5710:00 - 5730:00

that you navigate that.

## 5730:00 - 5740:00

>> Yeah.

## 5740:00 - 5770:00

>> What do you think about that hypothesis?

## 5770:00 - 5810:00

Um the the the two concepts are related,

## 5810:00 - 5850:00

but they're not exactly the same. Um and

## 5850:00 - 5885:00

so memory is is really about how do you

## 5885:00 - 5930:00

address sort of what information to pull

## 5930:00 - 5960:00

in in the context of the task you're

## 5960:00 - 6010:00

trying to solve. Continual learning

## 6010:00 - 6060:00

makes the assumption that the context

## 6060:00 - 6100:00

keep on changing. Therefore, what you've

## 6100:00 - 6140:00

learned keeps on changing. So there's a

## 6140:00 - 6175:00

notion of non-stationerity

## 6175:00 - 6200:00

that is really key to continual

## 6200:00 - 6245:00

learning. I I confess I have a little

## 6245:00 - 6275:00

bit of trouble with continual learning

## 6275:00 - 6310:00

uh as a concept because I feel the

## 6310:00 - 6355:00

community has never been able to nail

## 6355:00 - 6390:00

like how do we articulate the problem in

## 6390:00 - 6430:00

a way that we all agree on it and so

## 6430:00 - 6455:00

everyone who does work on continual

## 6455:00 - 6485:00

learning takes a different flavor of it

## 6485:00 - 6530:00

which makes it at least in my eyes and I

## 6530:00 - 6555:00

haven't worked a lot in this area but

## 6555:00 - 6580:00

makes it a little bit hard to know

## 6580:00 - 6630:00

whether we're making progress or not on

## 6630:00 - 6670:00

on memory it's a little bit more

## 6670:00 - 6720:00

standardized the tension really is about

## 6720:00 - 6750:00

it's a question of efficiency and

## 6750:00 - 6785:00

relevance. So the way to measure whether

## 6785:00 - 6815:00

you're doing that is a little bit better

## 6815:00 - 6845:00

standardized and you don't want to be

## 6845:00 - 6890:00

just sort of remembering everything. Um

## 6890:00 - 6920:00

and so it's a little bit better

## 6920:00 - 6945:00

standardized how we articulate the

## 6945:00 - 6960:00

tasks.

## 6960:00 - 7000:00

>> Okay, let's go. We're going to touch on

## 7000:00 - 7025:00

both of those now and then we'll keep

## 7025:00 - 7065:00

going down the list. Um with continual

## 7065:00 - 7110:00

learning maybe I'm you know so far

## 7110:00 - 7135:00

removed from it I'm not struggling with

## 7135:00 - 7180:00

it. So I'll give you my caveman thought

## 7180:00 - 7210:00

about what this is and you can help us

## 7210:00 - 7240:00

break it down a little bit. I mean the

## 7240:00 - 7280:00

problem has been articulated that the

## 7280:00 - 7325:00

models they are they don't change as

## 7325:00 - 7355:00

they go about all these I mean think

## 7355:00 - 7390:00

about how powerful it would be if let's

## 7390:00 - 7430:00

say the GPT model which is speaking with

## 7430:00 - 7470:00

800 million or maybe more uh by the time

## 7470:00 - 7520:00

this comes out million people a week

## 7520:00 - 7555:00

could I mean might be scary actually but

## 7555:00 - 7585:00

could internalize those conversations

## 7585:00 - 7610:00

and learn from the discussions that it's

## 7610:00 - 7655:00

having um that would almost you know you

## 7655:00 - 7680:00

I I agree with you that the wall we're

## 7680:00 - 7710:00

not at the wall but the question is

## 7710:00 - 7745:00

>> is there going to be enough data to keep

## 7745:00 - 7775:00

making these machines smarter and you

## 7775:00 - 7810:00

know as they have these conversations

## 7810:00 - 7840:00

that opens up that ability to continue

## 7840:00 - 7880:00

to grow and learn but the model stays

## 7880:00 - 7920:00

static despite all the fact all these

## 7920:00 - 7950:00

conversations that it's having with

## 7950:00 - 7970:00

people isn't that the problem

## 7970:00 - 8000:00

>> and I mean don't get me wrong right like

## 8000:00 - 8040:00

I absolutely believe we need to address

## 8040:00 - 8070:00

the fact that these models need to keep

## 8070:00 - 8110:00

on evolving I have no doubt about that I

## 8110:00 - 8140:00

just mean right now the progress in the

## 8140:00 - 8160:00

research community that's working on

## 8160:00 - 8200:00

continual learning isn't necessarily

## 8200:00 - 8225:00

connecting to the work that's going on

## 8225:00 - 8260:00

on scaling now the models that are

## 8260:00 - 8290:00

released right you know they keep on

## 8290:00 - 8315:00

evolving I would say you know the

## 8315:00 - 8350:00

generative models we have today whether

## 8350:00 - 8380:00

it's Chad GPD whether it's Gemini

## 8380:00 - 8405:00

whether it's our the command models that

## 8405:00 - 8440:00

the coher team is building these models

## 8440:00 - 8485:00

keep on improving it's just we don't

## 8485:00 - 8545:00

necessarily let them improve online but

## 8545:00 - 8600:00

we you know we ship at definite times

## 8600:00 - 8630:00

like a release of a model which has a

## 8630:00 - 8665:00

particular characteristic

## 8665:00 - 8695:00

advantage of doing that frankly is you

## 8695:00 - 8730:00

can really test the model before you put

## 8730:00 - 8755:00

it out there. You can put it through its

## 8755:00 - 8785:00

paces in terms of performance, in terms

## 8785:00 - 8835:00

of safety and so on. And I would be a

## 8835:00 - 8860:00

little bit reluctant to just let the

## 8860:00 - 8895:00

model keep running on its own because

## 8895:00 - 8935:00

you know the learning can go very very

## 8935:00 - 8985:00

fast and you can switch out of a mode

## 8985:00 - 9025:00

that seems completely reasonable very

## 9025:00 - 9060:00

quickly which you know we have seen a

## 9060:00 - 9075:00

few times in the past.

## 9075:00 - 9110:00

>> Yeah, I think we might be thinking about

## 9110:00 - 9145:00

one of the same instances when Microsoft

## 9145:00 - 9185:00

had this bot called Tay. Yes. Uh, I'll

## 9185:00 - 9220:00

tell you a story. I actually broke the

## 9220:00 - 9260:00

news of Tay that Microsoft was going had

## 9260:00 - 9290:00

this great bot, spoke with the people,

## 9290:00 - 9315:00

wrote the first story about it when I

## 9315:00 - 9350:00

was at Buzzfeed. I pinned it to my

## 9350:00 - 9385:00

Twitter profile. I went to sleep on the

## 9385:00 - 9415:00

West Coast and I woke up with all these

## 9415:00 - 9450:00

messages being like, "Hey, that chatbot

## 9450:00 - 9475:00

that you wrote about, the fun teen

## 9475:00 - 9510:00

chatbot is actually espousing Nazi

## 9510:00 - 9545:00

ideology. You might want to unpin that

## 9545:00 - 9575:00

tweet." And it was because it kept

## 9575:00 - 9610:00

learning. So okay, maybe continue

## 9610:00 - 9650:00

learning, you know, if it's done cuz it

## 9650:00 - 9690:00

has to also be done with some sort of

## 9690:00 - 9730:00

fine-tuning where you want to make sure

## 9730:00 - 9755:00

that behavior maybe it's preemptive

## 9755:00 - 9770:00

fine-tuning even.

## 9770:00 - 9795:00

>> Well, let's not release continual

## 9795:00 - 9830:00

learning till we've achieved continual

## 9830:00 - 9840:00

testing.

## 9840:00 - 9890:00

>> That sounds like a very reasonable uh

## 9890:00 - 9935:00

plan. All right, memory. Uh what makes

## 9935:00 - 9960:00

it so difficult? I'll tell you one

## 9960:00 - 9995:00

story. uh

## 9995:00 - 10035:00

>> uh my Friday co-host and I uh with the

## 10035:00 - 10090:00

my Friday co-host uh Ranjan Roy and I uh

## 10090:00 - 10155:00

we both went into Gemini on Google and

## 10155:00 - 10205:00

uh on Gmail and we asked can you find my

## 10205:00 - 10250:00

the first email that I ever sent uh with

## 10250:00 - 10260:00

my wife.

## 10260:00 - 10270:00

>> Okay.

## 10270:00 - 10290:00

>> Couldn't do it. Y

## 10290:00 - 10325:00

>> um is that because there's is it just

## 10325:00 - 10370:00

because there's so many emails in there

## 10370:00 - 10435:00

that actually like applying AI to to try

## 10435:00 - 10470:00

to figure out like what conversations

## 10470:00 - 10525:00

have been had is that difficult or is it

## 10525:00 - 10550:00

kind of a product problem from Google

## 10550:00 - 10585:00

like where why is memory so difficult

## 10585:00 - 10620:00

and how how are we going to end up like

## 10620:00 - 10650:00

how is the research community going to

## 10650:00 - 10680:00

tackle this?

## 10680:00 - 10710:00

>> I mean like it's a little bit difficult

## 10710:00 - 10745:00

to diagnose just from your description.

## 10745:00 - 10770:00

I feel like I'm a little bit like, you

## 10770:00 - 10800:00

know, a surgeon who's, you know, on the

## 10800:00 - 10825:00

phone hearing the description of the

## 10825:00 - 10830:00

patient. So,

## 10830:00 - 10880:00

>> have you asked Hat about your symptoms?

## 10880:00 - 10915:00

>> So, I won't necessarily venture, you

## 10915:00 - 10950:00

know, a precise diagnosis for your case.

## 10950:00 - 10985:00

But, but nonetheless, I don't think it's

## 10985:00 - 11020:00

that difficult to to figure out. I mean,

## 11020:00 - 11050:00

I'd have to know what information is is

## 11050:00 - 11080:00

the bot pulling from, right? Like just

## 11080:00 - 11110:00

in terms of like visibility and privacy.

## 11110:00 - 11135:00

Did you give it access to all of the

## 11135:00 - 11175:00

information it needed to answer that?

## 11175:00 - 11220:00

>> Um, and that's the first one. And you

## 11220:00 - 11260:00

know we do a lot you know go back to

## 11260:00 - 11285:00

what we're building at cohhere actually

## 11285:00 - 11330:00

like we do a lot of deployments on site.

## 11330:00 - 11355:00

So sometimes it's just a question like

## 11355:00 - 11380:00

we didn't activate the access to the

## 11380:00 - 11405:00

right information to do it. So you need

## 11405:00 - 11435:00

to figure out whether that access to the

## 11435:00 - 11460:00

right information is there.

## 11460:00 - 11510:00

>> Um and there's all sorts of reason that

## 11510:00 - 11550:00

you may not want to give the bots access

## 11550:00 - 11590:00

to all of your information all the time.

## 11590:00 - 11620:00

So that's one one practical

## 11620:00 - 11665:00

consideration. Um the other one is like

## 11665:00 - 11700:00

retrieving the right information. And

## 11700:00 - 11735:00

so, you know, did the query match how

## 11735:00 - 11775:00

the information was encoded? Because in

## 11775:00 - 11805:00

most of these, you may not want to just

## 11805:00 - 11845:00

leave the information in raw form. It

## 11845:00 - 11880:00

gets very expensive. I mean, you're one

## 11880:00 - 11900:00

person, but at the scale that some of

## 11900:00 - 11930:00

these companies are operating, you have

## 11930:00 - 11960:00

to compress it, which we often call

## 11960:00 - 11980:00

embeddings. So, you create like

## 11980:00 - 12020:00

embeddings of this representation. And

## 12020:00 - 12065:00

so, it may not have embedded the

## 12065:00 - 12100:00

information properly. And then there's

## 12100:00 - 12145:00

like retrieving that information. and

## 12145:00 - 12180:00

maybe it retrieved like 10,000 different

## 12180:00 - 12210:00

items and didn't didn't rank this one

## 12210:00 - 12235:00

close to the top and so it didn't

## 12235:00 - 12260:00

generate the right response. But it

## 12260:00 - 12290:00

could be that it knows of it. It just

## 12290:00 - 12320:00

didn't show up at the top.

## 12320:00 - 12355:00

>> Um so there's like a few different

## 12355:00 - 12390:00

reasons which makes it hard. One of them

## 12390:00 - 12420:00

is like the access to the information

## 12420:00 - 12440:00

when it's encoding that information.

## 12440:00 - 12465:00

Then it's like retrieve the information

## 12465:00 - 12490:00

at the right moment.

## 12490:00 - 12520:00

>> But when when this stuff works, it's

## 12520:00 - 12565:00

pretty magical. I was just in uh Claude

## 12565:00 - 12610:00

actually and I noticed that Claude's uh

## 12610:00 - 12645:00

memory capabilities have really

## 12645:00 - 12680:00

improved. I was speaking so I love to

## 12680:00 - 12705:00

upload the transcripts of my interviews

## 12705:00 - 12735:00

and like just you know get get a a

## 12735:00 - 12780:00

grading out like uh give me a rating on

## 12780:00 - 12820:00

a variety of metrics. You decide to tell

## 12820:00 - 12835:00

the bot you decide.

## 12835:00 - 12880:00

>> Do you agree with the ratings that the

## 12880:00 - 12895:00

body is giving you?

## 12895:00 - 12900:00

>> Definitely.

## 12900:00 - 12910:00

>> Okay.

## 12910:00 - 12935:00

>> Usually well you've trained it well.

## 12935:00 - 12965:00

>> I did. So some are good, some are bad.

## 12965:00 - 13000:00

Um I I actually had Gemini do a bunch of

## 13000:00 - 13025:00

ratings and it was like five of five on

## 13025:00 - 13065:00

all categories and I was like

## 13065:00 - 13095:00

>> that is wrong. Uh and then I went to

## 13095:00 - 13120:00

ChachiPT and Claude and they were

## 13120:00 - 13150:00

actually much more reasonable about it.

## 13150:00 - 13175:00

But one of the interesting things that

## 13175:00 - 13225:00

Claude did uh when I asked it this week,

## 13225:00 - 13280:00

it started comparing it uh to the other

## 13280:00 - 13300:00

interviews I had done. Okay.

## 13300:00 - 13330:00

>> And it said, you know, you actually hit

## 13330:00 - 13380:00

better points on this one and this is

## 13380:00 - 13425:00

why this one didn't resonate in my

## 13425:00 - 13465:00

opinion. Did you benchmark it with a

## 13465:00 - 13495:00

sample of your audience?

## 13495:00 - 13525:00

>> That that that's probably the next and

## 13525:00 - 13570:00

it'll probably when when it when I

## 13570:00 - 13605:00

because I'll take um data out of the

## 13605:00 - 13640:00

podcast analytics and drop it in these

## 13640:00 - 13665:00

bots. It's going to be able to cross

## 13665:00 - 13685:00

reference. So when it works, it's

## 13685:00 - 13730:00

magical. And you know, you've identified

## 13730:00 - 13780:00

this as one of the areas where AI

## 13780:00 - 13810:00

research really needs to, you know,

## 13810:00 - 13830:00

concentrate and this is the cutting

## 13830:00 - 13845:00

edge.

## 13845:00 - 13900:00

>> Um how good can this get and what do you

## 13900:00 - 13925:00

think? Do you think that it's at a

## 13925:00 - 13960:00

moment of real progress or is it sort of

## 13960:00 - 13990:00

party tricks to be able to get Claude to

## 13990:00 - 14020:00

be able to do the things that I talked

## 14020:00 - 14035:00

about?

## 14035:00 - 14075:00

>> Um the question on rating specifically

## 14075:00 - 14105:00

like analyzing the information and sort

## 14105:00 - 14130:00

of distilling some feedback

## 14130:00 - 14160:00

>> more more about the memory the fact that

## 14160:00 - 14205:00

it can call back memory in particular.

## 14205:00 - 14250:00

>> Um no I mean we're making good progress

## 14250:00 - 14280:00

on that. You know extending the context

## 14280:00 - 14315:00

length is kind of the easiest way to go

## 14315:00 - 14345:00

about it but there's quite a bit of

## 14345:00 - 14375:00

progress that is that is being made on

## 14375:00 - 14410:00

this. Okay, let's talk about reasoning.

## 14410:00 - 14440:00

You mentioned reasoning as a as a

## 14440:00 - 14465:00

cutting edge

## 14465:00 - 14510:00

>> uh moment. The problem is efficiency. Is

## 14510:00 - 14545:00

that is that really the issue here? I

## 14545:00 - 14575:00

mean, so so reasoning is the model

## 14575:00 - 14625:00

basically goes step by step. It it tries

## 14625:00 - 14670:00

to answer, checks the answer,

## 14670:00 - 14690:00

>> tries a different answer, then

## 14690:00 - 14725:00

eventually decides, okay, this is

## 14725:00 - 14750:00

probably what they want, and then it

## 14750:00 - 14810:00

spits something out.

## 14810:00 - 14855:00

>> Yes. I mean, that roughly happens this

## 14855:00 - 14905:00

way. I think the the challenge is really

## 14905:00 - 14945:00

being able to

## 14945:00 - 14985:00

plan at different levels of sort of

## 14985:00 - 15020:00

temporal granularity, right? So, in

## 15020:00 - 15055:00

terms of how you execute actions, let's

## 15055:00 - 15085:00

say, you know, you're you're planning a

## 15085:00 - 15125:00

trip, right? You're not going to start

## 15125:00 - 15165:00

by thinking of like what are the shoes

## 15165:00 - 15200:00

that I put on to go on my trip, right?

## 15200:00 - 15220:00

You're going to start by talking

## 15220:00 - 15255:00

thinking like roughly what season,

## 15255:00 - 15285:00

roughly what, you know, part of the

## 15285:00 - 15315:00

world do I want to go visit? You start

## 15315:00 - 15355:00

from the top level and then you take it

## 15355:00 - 15395:00

down a notch which is like okay you've

## 15395:00 - 15430:00

identified like a rough time a rough

## 15430:00 - 15470:00

place like let's get more precise on the

## 15470:00 - 15500:00

time and the place and maybe the

## 15500:00 - 15525:00

activity and like maybe who you want to

## 15525:00 - 15555:00

go with and then you take it down

## 15555:00 - 15580:00

another notch right and that's when you

## 15580:00 - 15600:00

start booking your reservations and so

## 15600:00 - 15635:00

on. But sometimes you know you'll hit a

## 15635:00 - 15675:00

blocker on the reservation and you can't

## 15675:00 - 15695:00

get the flights or the hotel you want

## 15695:00 - 15725:00

and then you'll pop back up and say like

## 15725:00 - 15750:00

do I change my dates? Do I change my

## 15750:00 - 15780:00

place? Do I change who I go with? I'm

## 15780:00 - 15800:00

not going to bring the kids because then

## 15800:00 - 15845:00

we can, you know, have more options. So,

## 15845:00 - 15900:00

we can pop back up in terms of level of

## 15900:00 - 15940:00

resolution. That's the part that the

## 15940:00 - 15970:00

reasoning models don't do. They do

## 15970:00 - 15995:00

really well at like one level of

## 15995:00 - 16035:00

granularity. So, you've got a robot, you

## 16035:00 - 16090:00

give it all these like motions for the

## 16090:00 - 16130:00

for the hands, what the body motions, it

## 16130:00 - 16170:00

can plan essentially to control the

## 16170:00 - 16210:00

motors at that level of granularity. But

## 16210:00 - 16240:00

the going back and forth between

## 16240:00 - 16300:00

different levels of sort of resolution

## 16300:00 - 16350:00

of action, it's really hard. So on the

## 16350:00 - 16390:00

technical terms, we call it hierarchical

## 16390:00 - 16435:00

planning. That's really hard to do that

## 16435:00 - 16480:00

decomposition and keeping the

## 16480:00 - 16515:00

information relevant as you go back and

## 16515:00 - 16525:00

forth.

## 16525:00 - 16555:00

>> Is that just a limitation of the large

## 16555:00 - 16580:00

language model? Because the fact that an

## 16580:00 - 16635:00

LLM can even do this in the first place

## 16635:00 - 16660:00

uh like again like it started with

## 16660:00 - 16675:00

predict the next

## 16675:00 - 16705:00

>> do it at the word level. Right. Right.

## 16705:00 - 16755:00

>> And out of the word level, you do get

## 16755:00 - 16790:00

the higher the higher level. It is

## 16790:00 - 16820:00

really impressive. I think that's the

## 16820:00 - 16845:00

part that probably shocked a lot of

## 16845:00 - 16885:00

people. They expected at, you know, back

## 16885:00 - 16930:00

in 2023 or so, they expected that as

## 16930:00 - 16970:00

you're generating tokens, you're not

## 16970:00 - 17015:00

going to be able to generate sort of big

## 17015:00 - 17055:00

ideas or or bigger plan. And yet, it's

## 17055:00 - 17085:00

pretty remarkable that it does it. Which

## 17085:00 - 17110:00

is why you get sort of you know

## 17110:00 - 17145:00

different opinions in terms of some

## 17145:00 - 17180:00

people's thinking like hey like it's

## 17180:00 - 17210:00

already impressive like like let's just

## 17210:00 - 17240:00

keep on pushing that way of doing things

## 17240:00 - 17270:00

and we will unblock this and other

## 17270:00 - 17310:00

people being a lot more skeptical that

## 17310:00 - 17325:00

you'll achieve it.

## 17325:00 - 17355:00

>> Explain that a little more. So as it's

## 17355:00 - 17395:00

typing as it's I mean I think Andre

## 17395:00 - 17420:00

Karpathy basically explained that the

## 17420:00 - 17455:00

transformer is a computer and every time

## 17455:00 - 17470:00

you

## 17470:00 - 17495:00

>> generate a new token you're going

## 17495:00 - 17520:00

through a piece of computing. So the

## 17520:00 - 17560:00

more you type, the bigger the computer

## 17560:00 - 17575:00

is that you use.

## 17575:00 - 17600:00

>> Yes. The more I mean the more

## 17600:00 - 17625:00

information goes in and the bigger your

## 17625:00 - 17645:00

representation is.

## 17645:00 - 17650:00

>> Yeah.

## 17650:00 - 17695:00

>> Okay. And so but are you saying that as

## 17695:00 - 17755:00

this happens the computer is effectively

## 17755:00 - 17785:00

already thinking ahead? I I'll give one

## 17785:00 - 17830:00

example. Claude uh just to go back to

## 17830:00 - 17875:00

some anthropic research, they published

## 17875:00 - 17900:00

uh this amazing research where they

## 17900:00 - 17930:00

asked Claude to write a poem. Yeah.

## 17930:00 - 17975:00

>> And as it's writing the first line, it's

## 17975:00 - 18010:00

already activating features in the model

## 18010:00 - 18040:00

that's thinking what rhymes with that.

## 18040:00 - 18050:00

>> Yeah.

## 18050:00 - 18075:00

>> Which is amazing because again, it's

## 18075:00 - 18115:00

technology that predicts the next word.

## 18115:00 - 18140:00

But as it's predicting the next token,

## 18140:00 - 18185:00

it's already thinking the next sentence,

## 18185:00 - 18210:00

which to me is just

## 18210:00 - 18220:00

>> mindboggling.

## 18220:00 - 18285:00

>> Yeah. And so I mean this is why to some

## 18285:00 - 18350:00

degree the emphasis on code and the

## 18350:00 - 18400:00

ability to build representations of code

## 18400:00 - 18435:00

and generate code is so interesting

## 18435:00 - 18485:00

because when you look at code and you

## 18485:00 - 18510:00

know for for people who've programmed

## 18510:00 - 18550:00

before the code has that structure that

## 18550:00 - 18595:00

hierarchical structure it's encoded in

## 18595:00 - 18630:00

anyone who looks at a bunch of code even

## 18630:00 - 18660:00

if it's not necessarily a language you

## 18660:00 - 18685:00

understand you understand the notion of

## 18685:00 - 18720:00

functions and variables and libraries

## 18720:00 - 18755:00

and so on. And so those different levels

## 18755:00 - 18790:00

of granularity of the project, it's

## 18790:00 - 18850:00

encoded in there. Um, and so there, you

## 18850:00 - 18880:00

know, there's there's some hope that by

## 18880:00 - 18915:00

training enough on code, the machine

## 18915:00 - 18955:00

essentially like infers these kinds of

## 18955:00 - 18995:00

structural cues.

## 18995:00 - 19040:00

>> Fascinating. So that that I mean like

## 19040:00 - 19070:00

you talked about the the the fact that

## 19070:00 - 19095:00

this technology and this is sort of the

## 19095:00 - 19145:00

thing that that sort of went makes my

## 19145:00 - 19175:00

head explode a little bit. the fact that

## 19175:00 - 19205:00

this technology is able to do these

## 19205:00 - 19240:00

things that you wouldn't think given the

## 19240:00 - 19285:00

architecture it is supposed to do. Um

## 19285:00 - 19310:00

same with if you think about video

## 19310:00 - 19350:00

models and image models and by the way

## 19350:00 - 19375:00

one of your former colleagues Yan Lakun

## 19375:00 - 19400:00

would always talk about how

## 19400:00 - 19430:00

>> to gener and I know he has some

## 19430:00 - 19460:00

criticisms of video models but to be

## 19460:00 - 19490:00

able to generate AI video you really

## 19490:00 - 19515:00

have to be able to predict and plan

## 19515:00 - 19535:00

what's going to happen in the physical

## 19535:00 - 19555:00

world. Absolutely.

## 19555:00 - 19570:00

>> And

## 19570:00 - 19605:00

>> there's some embedded intelligence that

## 19605:00 - 19635:00

even leading researchers I don't think

## 19635:00 - 19690:00

fully get. um that when you for instance

## 19690:00 - 19740:00

ask a model just to use Yan's favorite

## 19740:00 - 19790:00

example to drop a pencil there's so many

## 19790:00 - 19820:00

permutations of where that can go and

## 19820:00 - 19865:00

now the models without like I mean

## 19865:00 - 19895:00

without having lessons of physics

## 19895:00 - 19920:00

understand that it drops and maybe hits

## 19920:00 - 19950:00

the table and might bounce but bounce up

## 19950:00 - 20005:00

>> yep because it's seen enough data from

## 20005:00 - 20040:00

objects that are dropped that have these

## 20040:00 - 20065:00

kinds of behavior

## 20065:00 - 20090:00

>> but tried to predict what's the behavior

## 20090:00 - 20130:00

of a similar object dropped on you know

## 20130:00 - 20160:00

on a different planet it and probably

## 20160:00 - 20185:00

the prediction is wrong because all of

## 20185:00 - 20220:00

the data was taken with our gravity

## 20220:00 - 20240:00

constant.

## 20240:00 - 20265:00

>> Yes. I mean, I will say as I'm talking

## 20265:00 - 20290:00

about this, I did just see a video

## 20290:00 - 20345:00

generated where uh a man's fingers came

## 20345:00 - 20390:00

out of a styrofoam cup as he was holding

## 20390:00 - 20430:00

it. So, there's there's room to

## 20430:00 - 20455:00

>> a lot of room for improvement.

## 20455:00 - 20495:00

>> Now, there is some talk Deis Abvis was

## 20495:00 - 20530:00

on recently talking about how Google's

## 20530:00 - 20580:00

video models in some way have capab like

## 20580:00 - 20615:00

these world model capabilities. they do

## 20615:00 - 20645:00

understand the physics and you brought

## 20645:00 - 20685:00

up world models as another area where

## 20685:00 - 20725:00

this technology really has the potential

## 20725:00 - 20755:00

to grow. It's the cutting edge

## 20755:00 - 20775:00

>> still kind of undefined.

## 20775:00 - 20830:00

>> Yeah. I I will say and and you know

## 20830:00 - 20855:00

going back to the caveman here, I'm a

## 20855:00 - 20890:00

little bit confused about why for

## 20890:00 - 20910:00

instance like one of the examples that

## 20910:00 - 20970:00

you brought up earlier was that if you

## 20970:00 - 21000:00

want a model to be able to like go out

## 21000:00 - 21035:00

and like complete financial transactions

## 21035:00 - 21070:00

and understand the implications of

## 21070:00 - 21100:00

financial transactions, it has to know

## 21100:00 - 21120:00

how the world works.

## 21120:00 - 21125:00

>> Yeah.

## 21125:00 - 21160:00

>> Um but can't you just teach that in

## 21160:00 - 21195:00

text? Can't you teach it like if you use

## 21195:00 - 21240:00

my credit card and you know buy anything

## 21240:00 - 21280:00

online I will go bankrupt like in in

## 21280:00 - 21310:00

text or even number logic and therefore

## 21310:00 - 21340:00

don't do it like why does and and I

## 21340:00 - 21375:00

think world models is like you these

## 21375:00 - 21410:00

models need to understand gravity why

## 21410:00 - 21435:00

does a model need to understand gravity

## 21435:00 - 21495:00

to learn these basic um rules of sort of

## 21495:00 - 21530:00

the way that the world works

## 21530:00 - 21565:00

>> well and and and this is why earlier I

## 21565:00 - 21585:00

sort of distinguish between like

## 21585:00 - 21615:00

physical world models and digital world

## 21615:00 - 21650:00

models right it's it's possible that you

## 21650:00 - 21670:00

can actually build really effective

## 21670:00 - 21715:00

agents, web- based agents that don't

## 21715:00 - 21760:00

understand the concept of gravity. And

## 21760:00 - 21785:00

it's possible you can build physical

## 21785:00 - 21810:00

world models for robots that don't need

## 21810:00 - 21845:00

to understand, you know, the functioning

## 21845:00 - 21885:00

banking system. And so you can define

## 21885:00 - 21950:00

the word world as being like a contained

## 21950:00 - 22020:00

environment. Um, and so but but if you

## 22020:00 - 22050:00

want to deploy the agent on that

## 22050:00 - 22085:00

environment, then it does need to

## 22085:00 - 22125:00

understand the the rules of that that

## 22125:00 - 22160:00

environment quite well.

## 22160:00 - 22205:00

The challenge is getting enough coverage

## 22205:00 - 22255:00

of data for all the possible futures,

## 22255:00 - 22285:00

right? And all the different ways that

## 22285:00 - 22330:00

the world could could evolve subject to

## 22330:00 - 22360:00

various events, various events

## 22360:00 - 22420:00

happening. So, a lot of the cases today

## 22420:00 - 22470:00

where it's actually most beneficial is

## 22470:00 - 22500:00

is where there's like a place for the

## 22500:00 - 22530:00

human on the table. And I I'll give you

## 22530:00 - 22565:00

an example, right? People talk a lot

## 22565:00 - 22595:00

about using chatbots for customer

## 22595:00 - 22620:00

service, right? Like chatbots should be

## 22620:00 - 22645:00

you should just like plug them in. and

## 22645:00 - 22675:00

they will answer all your questions. Um

## 22675:00 - 22720:00

they'll be available 24/7

## 22720:00 - 22760:00

and so on. In reality and and there will

## 22760:00 - 22795:00

be of course many chat bots deployed for

## 22795:00 - 22830:00

these kinds of cases. But you know like

## 22830:00 - 22860:00

one of the use cases we've seen that

## 22860:00 - 22905:00

works really well is actually to have

## 22905:00 - 22945:00

the bot like pull together all the

## 22945:00 - 22980:00

relevant information. You do customer

## 22980:00 - 23010:00

service, you pull together all the

## 23010:00 - 23035:00

relevant information from many different

## 23035:00 - 23065:00

sources as opposed to like following a

## 23065:00 - 23115:00

script being just chatbot. pull together

## 23115:00 - 23140:00

all that information about you know the

## 23140:00 - 23175:00

the the documents the documentation that

## 23175:00 - 23210:00

accompanies the system the case on the

## 23210:00 - 23245:00

client the different problem that

## 23245:00 - 23270:00

description that you have. You pull all

## 23270:00 - 23300:00

together that and then you pose a

## 23300:00 - 23335:00

diagnostic and then you pose a few

## 23335:00 - 23365:00

suggested actions and then you keep a

## 23365:00 - 23400:00

human in the loop to validate the plan

## 23400:00 - 23435:00

and to carry out the action. And so that

## 23435:00 - 23480:00

means that the human you know can and

## 23480:00 - 23510:00

these are more complicated cases than

## 23510:00 - 23535:00

just like your cell phone plan or

## 23535:00 - 23580:00

something like that. Um but nonetheless

## 23580:00 - 23620:00

in those cases like what would have

## 23620:00 - 23665:00

taken a long time you know maybe you

## 23665:00 - 23690:00

know half an hour to pull together all

## 23690:00 - 23725:00

that information distill it for a human

## 23725:00 - 23760:00

now you can reduce that down to like a

## 23760:00 - 23810:00

20 second you know analyze verify and

## 23810:00 - 23850:00

carry out the action. So if you have

## 23850:00 - 23890:00

that ability to combine the human and

## 23890:00 - 23930:00

the AI agent, actually you get often

## 23930:00 - 23985:00

some much more powerful results and it

## 23985:00 - 24005:00

means if your world model isn't

## 24005:00 - 24045:00

complete, humans in the loop, they

## 24045:00 - 24070:00

figure out the pieces that's missing.

## 24070:00 - 24095:00

They give that extra information and

## 24095:00 - 24125:00

then you bring that information back to

## 24125:00 - 24155:00

train your agent. Then you get continual

## 24155:00 - 24170:00

learning.

## 24170:00 - 24190:00

>> There you go.

## 24190:00 - 24205:00

>> We're getting there. We're getting

## 24205:00 - 24220:00

there.

## 24220:00 - 24255:00

>> Do you buy that the models need to

## 24255:00 - 24295:00

understand gravity for AGI to be

## 24295:00 - 24320:00

reached? I mean there are basically like

## 24320:00 - 24350:00

a couple schools of thought that you

## 24350:00 - 24390:00

could you could basically train AGI on

## 24390:00 - 24435:00

on bits and you know letters and stuff

## 24435:00 - 24450:00

like that.

## 24450:00 - 24480:00

>> Um images or and then there are others

## 24480:00 - 24525:00

that believe you know you really need uh

## 24525:00 - 24565:00

you really need the these models to

## 24565:00 - 24615:00

understand like um you know not just the

## 24615:00 - 24640:00

rules of poker but like what happens

## 24640:00 - 24670:00

when a person puts their hand on a poker

## 24670:00 - 24735:00

table. What do you think? Yeah. I mean,

## 24735:00 - 24840:00

I I tend to actually place my bet not on

## 24840:00 - 24870:00

the fact that we're going to reach like

## 24870:00 - 24940:00

a single super intelligent agent, but on

## 24940:00 - 24980:00

the fact that we are much more likely to

## 24980:00 - 25010:00

live in a future where there's going to

## 25010:00 - 25050:00

be many agents for many things. And so,

## 25050:00 - 25080:00

some agents will absolutely need to

## 25080:00 - 25115:00

understand gravity. You know, if we're

## 25115:00 - 25150:00

going to have physical robots that are

## 25150:00 - 25170:00

moving around in the world that are

## 25170:00 - 25190:00

going to be hitting objects, that are

## 25190:00 - 25215:00

going to be picking up objects and so

## 25215:00 - 25255:00

on, they will need to understand that

## 25255:00 - 25280:00

other agents that are dealing, for

## 25280:00 - 25310:00

example, with our digital life may not

## 25310:00 - 25360:00

need to understand that. And we also

## 25360:00 - 25390:00

need to have a protocol for these agents

## 25390:00 - 25425:00

to interact with each other and to talk

## 25425:00 - 25455:00

to each other. So, I actually think

## 25455:00 - 25505:00

that's a much more likely scenario. um

## 25505:00 - 25540:00

rather than have like the Uber agent

## 25540:00 - 25570:00

that needs to understand everything and

## 25570:00 - 25630:00

have an fully encapsulated world model.

## 25630:00 - 25660:00

>> There's a popular thing that AI lab

## 25660:00 - 25690:00

leaders have been saying recently.

## 25690:00 - 25710:00

They've been talking about how there's a

## 25710:00 - 25765:00

capability overhang. How the AI

## 25765:00 - 25800:00

technology can do a lot more than it's

## 25800:00 - 25825:00

being used for.

## 25825:00 - 25845:00

>> Do you believe that?

## 25845:00 - 25890:00

>> Um absolutely. Yeah.

## 25890:00 - 25920:00

>> Say say more about it. Talk about what

## 25920:00 - 25945:00

do you think is not being done that

## 25945:00 - 26000:00

could be done? I see it every day. Uh I

## 26000:00 - 26035:00

mean

## 26035:00 - 26065:00

and I'll I'll I'll open up a little

## 26065:00 - 26090:00

window like one of the reasons I was

## 26090:00 - 26135:00

super excited about joining go here is

## 26135:00 - 26170:00

because it's one of the few places that

## 26170:00 - 26190:00

you know that we have a team that does

## 26190:00 - 26235:00

research. So I get to see you know

## 26235:00 - 26260:00

day-to-day what's happening in research.

## 26260:00 - 26290:00

We have a team that does modeling. So I

## 26290:00 - 26315:00

get to see the models that we're

## 26315:00 - 26345:00

building look at the evaluations the

## 26345:00 - 26385:00

full spread of evaluations and we have a

## 26385:00 - 26425:00

product that's product is an agentic

## 26425:00 - 26450:00

platform that is going to real clients.

## 26450:00 - 26485:00

So you get to see the whole thing and I

## 26485:00 - 26525:00

see something that our models can do and

## 26525:00 - 26550:00

I see some things that we've built into

## 26550:00 - 26585:00

the products and then we go and there's

## 26585:00 - 26610:00

a lot of customers that are not using

## 26610:00 - 26640:00

the full functionality for all sorts of

## 26640:00 - 26690:00

reasons. Um so I think like that that

## 26690:00 - 26720:00

between like what we have in terms of

## 26720:00 - 26750:00

capacity versus what's being deployed

## 26750:00 - 26795:00

right now there's a big gap between

## 26795:00 - 26870:00

that. Sometimes the reasons are um are

## 26870:00 - 26910:00

uh capacity questions like a lot of

## 26910:00 - 26940:00

actual we talk a lot about super

## 26940:00 - 26985:00

intelligence big models. In reality

## 26985:00 - 27010:00

paying customers want like a good

## 27010:00 - 27040:00

trade-off in terms of performance for

## 27040:00 - 27070:00

efficiency. So you know we'll train

## 27070:00 - 27100:00

bigger models but we'll deploy smaller

## 27100:00 - 27130:00

models because it gives us that

## 27130:00 - 27155:00

tradeoff. It's like good enough

## 27155:00 - 27185:00

intelligence to get the job done. And

## 27185:00 - 27210:00

I'm like well we could give you so much

## 27210:00 - 27250:00

more. They're like no it's good enough.

## 27250:00 - 27285:00

So, and it's a perfectly, you know,

## 27285:00 - 27315:00

rational position for them to be taking.

## 27315:00 - 27340:00

So, some of that is for efficiency

## 27340:00 - 27420:00

reasons. Um, some of that gap is also

## 27420:00 - 27465:00

because you're going into

## 27465:00 - 27510:00

organizations which have systems and

## 27510:00 - 27540:00

processes in place. And sometimes

## 27540:00 - 27595:00

there's like a a mismatch between what

## 27595:00 - 27645:00

those processes are set up to do today

## 27645:00 - 27695:00

>> versus what would be a I think, you

## 27695:00 - 27725:00

know, a more welcoming environment for

## 27725:00 - 27760:00

an AI agent. So there's these kinds of

## 27760:00 - 27790:00

things and then the the other one is

## 27790:00 - 27820:00

often I think there's a lot of

## 27820:00 - 27855:00

intelligence that is not encoded. So the

## 27855:00 - 27890:00

agents go they plug into a bunch of

## 27890:00 - 27920:00

internal system they leverage all the

## 27920:00 - 27955:00

business intelligence with privacy

## 27955:00 - 27985:00

security consideration. They leverage

## 27985:00 - 28020:00

all that information

## 28020:00 - 28050:00

but sometimes there's big pockets of

## 28050:00 - 28075:00

information that we're not leveraging

## 28075:00 - 28105:00

right now. And if we did if we connected

## 28105:00 - 28140:00

into that then we would be able to do a

## 28140:00 - 28180:00

lot more. So that that like impedance

## 28180:00 - 28210:00

mismatch in terms of the information

## 28210:00 - 28250:00

sharing from the organization or from

## 28250:00 - 28295:00

the individual to the AI is another case

## 28295:00 - 28360:00

where leaves a lot of you know lot of

## 28360:00 - 28385:00

machine intelligence on the table.

## 28385:00 - 28405:00

>> So we're going to talk about enterprise

## 28405:00 - 28430:00

in a moment but let me ask you one

## 28430:00 - 28455:00

question about how this applies to

## 28455:00 - 28500:00

consumers. Um obviously we talked about

## 28500:00 - 28545:00

a lot of technology and uh the vision is

## 28545:00 - 28585:00

there within the big tech companies to

## 28585:00 - 28635:00

have a like a universal assistant uh

## 28635:00 - 28660:00

something like an Apple intelligence or

## 28660:00 - 28705:00

an Alexa plus uh you know both of them

## 28705:00 - 28740:00

have rolled out in their own way uh but

## 28740:00 - 28765:00

both both of them and I guess you know

## 28765:00 - 28805:00

meta has their own product Google has

## 28805:00 - 28825:00

their own product none of these are

## 28825:00 - 28855:00

lighting the world on fire is do you

## 28855:00 - 28885:00

think that is is this another example of

## 28885:00 - 28920:00

a capability overhanging or is it that

## 28920:00 - 28970:00

the technology is just not there Yet

## 28970:00 - 29010:00

>> uh I think both are true.

## 29010:00 - 29065:00

>> I think you know people

## 29065:00 - 29110:00

are expecting you know basically been

## 29110:00 - 29135:00

promised super intelligence. So you know

## 29135:00 - 29165:00

they are expecting magic out of these

## 29165:00 - 29220:00

these AI systems. It is not magic. Um

## 29220:00 - 29250:00

and so I would say like there's a big

## 29250:00 - 29285:00

gap between expectation what they can do

## 29285:00 - 29325:00

today. And then there's also a mismatch

## 29325:00 - 29360:00

between you know what people try to do

## 29360:00 - 29400:00

versus what might be the strength of of

## 29400:00 - 29445:00

these agents. I I compared a little bit.

## 29445:00 - 29465:00

You know, you're working in a team, you

## 29465:00 - 29515:00

get a new teammate in like day one. You

## 29515:00 - 29545:00

may not know exactly what this person is

## 29545:00 - 29580:00

capable of, not capable of, and it takes

## 29580:00 - 29610:00

some time working together, and and

## 29610:00 - 29635:00

sometimes that person gets a lot better

## 29635:00 - 29655:00

when you give them a lot more

## 29655:00 - 29680:00

information, and sometimes you discover

## 29680:00 - 29705:00

they have a new skill that they didn't

## 29705:00 - 29735:00

have, but at the end of the day, you

## 29735:00 - 29780:00

know, often that person isn't

## 29780:00 - 29815:00

able to do everything everywhere all at

## 29815:00 - 29830:00

once.

## 29830:00 - 29860:00

>> And so, I think there's there's both

## 29860:00 - 29885:00

both these things are true at the same

## 29885:00 - 29895:00

time.

## 29895:00 - 29920:00

>> Yeah. There's also I mean a lot of

## 29920:00 - 29950:00

corporate politics. I just wrote this

## 29950:00 - 29960:00

>> of course

## 29960:00 - 29990:00

>> I wrote this uh story recently in big

## 29990:00 - 30020:00

technology talking about how there's

## 30020:00 - 30050:00

like these two basic and actually you're

## 30050:00 - 30075:00

in a great position to talk about this

## 30075:00 - 30110:00

or or give us the real story here. From

## 30110:00 - 30140:00

my vantage point there's basically two

## 30140:00 - 30175:00

trajectories that a lot of companies are

## 30175:00 - 30240:00

on. The companies themselves have uh I'm

## 30240:00 - 30285:00

not talking about your customers but um

## 30285:00 - 30315:00

if you think about like companies

## 30315:00 - 30360:00

overall um many of them have struggled

## 30360:00 - 30395:00

to put this technology into place. But

## 30395:00 - 30425:00

individuals are starting to see the

## 30425:00 - 30460:00

benefit. So you actually have like these

## 30460:00 - 30490:00

companies with these pilots that are not

## 30490:00 - 30520:00

getting into production but then you

## 30520:00 - 30560:00

might have somebody you know lower down

## 30560:00 - 30595:00

using clawed code who's like actually

## 30595:00 - 30620:00

getting done.

## 30620:00 - 30640:00

>> Um so what do you what do you think

## 30640:00 - 30660:00

about that and what do you think it

## 30660:00 - 30685:00

means if we end up seeing that

## 30685:00 - 30710:00

divergence continue?

## 30710:00 - 30750:00

>> I think that is absolutely true. We see

## 30750:00 - 30775:00

this all the time even within our own

## 30775:00 - 30840:00

companies. Uh yes uh people's ability to

## 30840:00 - 30905:00

leverage the technology varies a lot. I

## 30905:00 - 30930:00

mean the reality is we are moving

## 30930:00 - 30950:00

towards a world where there's going to

## 30950:00 - 30975:00

be more and more of that technology and

## 30975:00 - 31000:00

so the people who have the ability to

## 31000:00 - 31025:00

understand and leverage the technology

## 31025:00 - 31060:00

are going to have an edge.

## 31060:00 - 31110:00

>> Okay, I agree.

## 31110:00 - 31140:00

Uh all right, last question before we

## 31140:00 - 31165:00

take a break and go on to some more of

## 31165:00 - 31200:00

like the practical applications, some of

## 31200:00 - 31245:00

the more coherent stuff. I I still can't

## 31245:00 - 31280:00

wrap my head around the fact that

## 31280:00 - 31335:00

>> the AI labs are so close together in

## 31335:00 - 31370:00

terms of the technology they produce.

## 31370:00 - 31400:00

One builds some innovation, the next has

## 31400:00 - 31440:00

the innovation. Um, one seems like it

## 31440:00 - 31475:00

leaps ahead, the next seems like it

## 31475:00 - 31500:00

leaps ahead.

## 31500:00 - 31555:00

>> Can you envision a scenario where one of

## 31555:00 - 31590:00

the labs just like kind of hits on

## 31590:00 - 31655:00

something and and can actually open up a

## 31655:00 - 31685:00

lead against the others or is it just

## 31685:00 - 31745:00

going to be neck andneck forever?

## 31745:00 - 31810:00

I think it's really hard to keep ideas

## 31810:00 - 31845:00

in a box

## 31845:00 - 31875:00

>> especially because in many ways these

## 31875:00 - 31925:00

ideas they reside in in people's heads

## 31925:00 - 31960:00

and I mean you've seen as much as me the

## 31960:00 - 31985:00

movement of people between these

## 31985:00 - 32015:00

companies like they're always you know

## 32015:00 - 32050:00

pingponging back and forth they carry

## 32050:00 - 32100:00

the ideas with them you know even if the

## 32100:00 - 32135:00

code stays on on one side like once

## 32135:00 - 32175:00

you've seen some insight you can't unsee

## 32175:00 - 32185:00

it

## 32185:00 - 32190:00

>> right

## 32190:00 - 32230:00

>> and so you They may need to reimplement.

## 32230:00 - 32260:00

They may need to articulate it in

## 32260:00 - 32290:00

different ways. They may give it a

## 32290:00 - 32325:00

different name. But ideas just

## 32325:00 - 32360:00

circulate. You can't keep ideas in a

## 32360:00 - 32390:00

box. And that's why honestly for many

## 32390:00 - 32440:00

years I've been so much an advocate for

## 32440:00 - 32470:00

open science. I just don't believe that

## 32470:00 - 32510:00

you can keep these ideas boxed in unless

## 32510:00 - 32540:00

you're willing to keep people boxed in,

## 32540:00 - 32580:00

which we are not willing to do. Um, and

## 32580:00 - 32635:00

so I don't I don't f I don't think we

## 32635:00 - 32670:00

have a way to close the ideas. We should

## 32670:00 - 32710:00

embrace the fact that when you let the

## 32710:00 - 32745:00

ideas circulate all of us progress

## 32745:00 - 32770:00

faster

## 32770:00 - 32810:00

>> and then the question is let's say all

## 32810:00 - 32850:00

these labs do reach super intelligence

## 32850:00 - 32885:00

you know it's been asked well you can't

## 32885:00 - 32935:00

hoard it so where's the economic value

## 32935:00 - 33000:00

in developing it? Yeah, we're still very

## 33000:00 - 33030:00

very early days in the technology and

## 33030:00 - 33070:00

we're even earlier days in terms of like

## 33070:00 - 33100:00

what are going to be the dominant

## 33100:00 - 33140:00

economic models, what is going to be the

## 33140:00 - 33165:00

right business strategy in the age of

## 33165:00 - 33220:00

AI. Um I think we need to give ourselves

## 33220:00 - 33250:00

the time to experiment. You know, now we

## 33250:00 - 33290:00

have 30 years or so perspective on the

## 33290:00 - 33340:00

internet and the economic impact of that

## 33340:00 - 33365:00

and it's going to take a number of years

## 33365:00 - 33410:00

before we we figure that out. But often,

## 33410:00 - 33435:00

you know, those who develop the

## 33435:00 - 33475:00

technology are not necessarily the same

## 33475:00 - 33520:00

as those who scale the technology versus

## 33520:00 - 33555:00

those who actually commercialize it

## 33555:00 - 33585:00

versus those who actually control it and

## 33585:00 - 33630:00

regulate it. So, there's a there's a

## 33630:00 - 33665:00

pretty complex ecosystem that is all

## 33665:00 - 33695:00

going to arise out of that.

## 33695:00 - 33735:00

>> Okay. Well, at at the at the other side

## 33735:00 - 33755:00

of this break, we're going to talk about

## 33755:00 - 33785:00

some real economic impact of this

## 33785:00 - 33820:00

technology already. Talk a little bit

## 33820:00 - 33855:00

about what Coher is up to.

## 33855:00 - 33890:00

>> Um, and then we'll cover a lot more.

## 33890:00 - 33930:00

episode. We'll be back right after this.

## 33930:00 - 33965:00

And we're back here on Big Technology

## 33965:00 - 34015:00

Podcast with Joel Pino, the chief AI

## 34015:00 - 34065:00

officer at Coher. And of course, this is

## 34065:00 - 34095:00

part of our Davos series that we're

## 34095:00 - 34135:00

hosting at the Qualcomm House uh here in

## 34135:00 - 34175:00

Davos and running over the weeks

## 34175:00 - 34200:00

following. So Joel, it's great to have

## 34200:00 - 34250:00

you. Uh let me give you what I've

## 34250:00 - 34310:00

gathered as the use cases in business um

## 34310:00 - 34350:00

for AI and you tell me if I'm missing

## 34350:00 - 34380:00

any and then maybe what you think is the

## 34380:00 - 34410:00

most valuable. All right, I wrote four

## 34410:00 - 34460:00

down. Uh one is external chat bots, the

## 34460:00 - 34490:00

customer engagement type of chat bots,

## 34490:00 - 34525:00

the type like Brett Taylor talked about

## 34525:00 - 34560:00

at Sierra. Uh the other is internal

## 34560:00 - 34615:00

knowledge. So let's say a company has

## 34615:00 - 34645:00

knowledge within the company and it's

## 34645:00 - 34685:00

all fragmented and maybe there's a bot

## 34685:00 - 34720:00

that you can start to query internal

## 34720:00 - 34735:00

knowledge.

## 34735:00 - 34770:00

>> Third is papering over systems that

## 34770:00 - 34790:00

don't work. I don't think that needs

## 34790:00 - 34825:00

much more explanation. It's like the

## 34825:00 - 34835:00

story of

## 34835:00 - 34865:00

>> skeptical about that but still

## 34865:00 - 34900:00

>> and then the fourth is automation.

## 34900:00 - 34920:00

>> Yeah.

## 34920:00 - 34955:00

>> Am I missing any big categories in as

## 34955:00 - 34985:00

far as AI in business and where do you

## 34985:00 - 35020:00

think the the real value or the biggest

## 35020:00 - 35045:00

category is right now? I think there's

## 35045:00 - 35075:00

like different ways to slice it. I think

## 35075:00 - 35100:00

that's a perfectly reasonable way to

## 35100:00 - 35130:00

slice it. I think another way that I've

## 35130:00 - 35155:00

seen it sliced is between like

## 35155:00 - 35200:00

predictive AI, generative AI versus

## 35200:00 - 35270:00

agentic AI, which is like a whole other

## 35270:00 - 35310:00

level of opportunity. Um, and then the

## 35310:00 - 35350:00

other way I've seen it sliced is is more

## 35350:00 - 35395:00

by application domains, right? like you

## 35395:00 - 35425:00

know whether it's what AI is going to do

## 35425:00 - 35450:00

in healthcare, what AI is going to do

## 35450:00 - 35480:00

for scientific discovery, what it's

## 35480:00 - 35515:00

going to do in banking, what it's you

## 35515:00 - 35555:00

know doing for example um public sector

## 35555:00 - 35590:00

and so on. So that's the other way that

## 35590:00 - 35625:00

people have have looked at the different

## 35625:00 - 35670:00

uh the different

## 35670:00 - 35705:00

case classes of opportunity.

## 35705:00 - 35755:00

>> And so what do you think the biggest is?

## 35755:00 - 35805:00

>> Um the

## 35805:00 - 35860:00

there is so much potential. I I hesitate

## 35860:00 - 35920:00

to pick one. Um I I will say you know

## 35920:00 - 35965:00

quite frankly where Coher has placed its

## 35965:00 - 36015:00

chips and and and the core hypothesis is

## 36015:00 - 36060:00

on um the case of enterprise AI that

## 36060:00 - 36095:00

needs really high privacy and security

## 36095:00 - 36110:00

guarantees. Okay.

## 36110:00 - 36150:00

>> I think there's a big cluster of

## 36150:00 - 36180:00

applications which falls a little bit in

## 36180:00 - 36210:00

the in the second category that you

## 36210:00 - 36240:00

outlined where you know you have a lot

## 36240:00 - 36275:00

of internal business intelligence

## 36275:00 - 36310:00

information perhaps fragmented. you want

## 36310:00 - 36330:00

to be able to leverage all that

## 36330:00 - 36390:00

information to uh to empower your

## 36390:00 - 36430:00

employees. And so in that case,

## 36430:00 - 36455:00

especially when that information is

## 36455:00 - 36480:00

something that you don't want to pop up

## 36480:00 - 36525:00

on the web through an API, um there's an

## 36525:00 - 36565:00

opportunity to build aic systems that

## 36565:00 - 36615:00

work inhouse with the local data that

## 36615:00 - 36650:00

inform the employees and are essentially

## 36650:00 - 36685:00

like close partners to the employees.

## 36685:00 - 36730:00

>> Can you give me like a use case or a a

## 36730:00 - 36765:00

case study? Yeah, I mean we do a lot of

## 36765:00 - 36795:00

work for example in financial services

## 36795:00 - 36830:00

uh because as you can imagine I a lot of

## 36830:00 - 36865:00

that data is quite sensitive in terms of

## 36865:00 - 36915:00

information uh very concrete use cases

## 36915:00 - 36955:00

we're seeing is uh for um financial

## 36955:00 - 36985:00

analysis. So you know we have people

## 36985:00 - 37020:00

whose job it is to advise various

## 37020:00 - 37065:00

clients um and they need to pull on

## 37065:00 - 37105:00

diverse set of data like what's the you

## 37105:00 - 37130:00

know what's the information that's

## 37130:00 - 37155:00

relevant to this particular customer

## 37155:00 - 37185:00

what's the information that's relevant

## 37185:00 - 37220:00

in terms of like the current landscape

## 37220:00 - 37255:00

the possibilities and so on and kind of

## 37255:00 - 37285:00

pull all of that information to make up

## 37285:00 - 37330:00

like a personal plan a financial plan

## 37330:00 - 37365:00

for a client um is the kind of

## 37365:00 - 37410:00

application that this technology can

## 37410:00 - 37440:00

make much easier and you can essentially

## 37440:00 - 37465:00

then query your plan decide Do I have

## 37465:00 - 37490:00

enough information? Do I need to gather

## 37490:00 - 37525:00

more sources of information? And you can

## 37525:00 - 37560:00

combine the internal with the external

## 37560:00 - 37600:00

information, but the output of that

## 37600:00 - 37640:00

stays private. It stays secure. It stays

## 37640:00 - 37665:00

in the hands of just the people who need

## 37665:00 - 37690:00

to see that information.

## 37690:00 - 37710:00

>> You know, I'm glad you brought that up

## 37710:00 - 37755:00

because I was asked recently by someone

## 37755:00 - 37785:00

in the financial service industry, uh,

## 37785:00 - 37810:00

what's going to happen to entry- level

## 37810:00 - 37850:00

employees who were doing a lot of that,

## 37850:00 - 37885:00

you know, collating and pulling in the

## 37885:00 - 37910:00

external information.

## 37910:00 - 37955:00

>> And I didn't have a great answer. I I

## 37955:00 - 37975:00

you know because

## 37975:00 - 38005:00

>> you know you pay you pay entry- level

## 38005:00 - 38035:00

employees less than your standard

## 38035:00 - 38065:00

employees and you you anticipate there's

## 38065:00 - 38095:00

going to be some learning on the job and

## 38095:00 - 38120:00

some productive

## 38120:00 - 38160:00

>> things and now question is what are

## 38160:00 - 38185:00

these people going to do

## 38185:00 - 38210:00

>> if I can do it for them

## 38210:00 - 38250:00

>> if these entry- level employees are able

## 38250:00 - 38285:00

to use AI properly they're skipping

## 38285:00 - 38320:00

ahead to the level where they can

## 38320:00 - 38355:00

actually be fully functioning analysts

## 38355:00 - 38395:00

and they can essentially do 10x the job

## 38395:00 - 38440:00

with the tools and so their growth both

## 38440:00 - 38465:00

in terms of their ability to deliver

## 38465:00 - 38495:00

value to the employer has just been

## 38495:00 - 38540:00

magnified by giving them the AI tools.

## 38540:00 - 38565:00

>> So is then the threat really to the

## 38565:00 - 38615:00

middle the people who are mid-career who

## 38615:00 - 38650:00

are going to get I mean it's like it's

## 38650:00 - 38685:00

the old story of the social media intern

## 38685:00 - 38715:00

who comes in and all of a sudden is

## 38715:00 - 38750:00

managing like PR or marketing for a

## 38750:00 - 38810:00

company. Is it the Gen Z kid who like

## 38810:00 - 38850:00

uses who who knows who knows how to

## 38850:00 - 38890:00

prompt and can use cohhere and all of a

## 38890:00 - 38910:00

sudden the person who's been doing

## 38910:00 - 38955:00

things for 15 years in a certain way has

## 38955:00 - 38990:00

to look over their shoulder.

## 38990:00 - 39040:00

>> I do think that whenever you introduce a

## 39040:00 - 39085:00

completely disruptive technology,

## 39085:00 - 39110:00

that is a lot of what you see. You see

## 39110:00 - 39145:00

the younger generation for whom that

## 39145:00 - 39185:00

technology is native and is very

## 39185:00 - 39235:00

intuitive and they really you know learn

## 39235:00 - 39280:00

how to use it very quickly and that just

## 39280:00 - 39310:00

makes them so much more effective and

## 39310:00 - 39380:00

productive and folks who are not able to

## 39380:00 - 39420:00

engage with a technology as quickly are

## 39420:00 - 39465:00

finding themselves as a disadvantage. I

## 39465:00 - 39505:00

just remember um being early in my

## 39505:00 - 39530:00

career and maybe this is why I didn't

## 39530:00 - 39565:00

last very long in a company and had to

## 39565:00 - 39600:00

go start my own but you know wanting

## 39600:00 - 39630:00

want having the energy and wanting to do

## 39630:00 - 39655:00

things and you know

## 39655:00 - 39690:00

>> if I would have had something that could

## 39690:00 - 39725:00

like build a prototype and I could bring

## 39725:00 - 39750:00

that to the meeting and show it as

## 39750:00 - 39790:00

opposed to like can I have like a couple

## 39790:00 - 39825:00

hours of the developers time to work on

## 39825:00 - 39845:00

this side project

## 39845:00 - 39870:00

>> that would change things.

## 39870:00 - 39910:00

>> Absolutely. And and and to be honest,

## 39910:00 - 39950:00

right, like that capability is afforded

## 39950:00 - 39975:00

to anyone in the company, right? It's

## 39975:00 - 40010:00

not just the the the more junior

## 40010:00 - 40040:00

staffers that have access to it. It's

## 40040:00 - 40065:00

also the people who are in leadership

## 40065:00 - 40100:00

position which instead of like writing

## 40100:00 - 40135:00

out a memo suddenly can go out and like

## 40135:00 - 40165:00

produce a full-fledged prototype. They

## 40165:00 - 40200:00

don't need, you know, 10 people, 10

## 40200:00 - 40225:00

staffers to help them produce their

## 40225:00 - 40250:00

prototype. They have an idea, they can

## 40250:00 - 40280:00

quickly prototype it and they send that

## 40280:00 - 40325:00

to the team to get uh to get moving with

## 40325:00 - 40365:00

a project. So I think that kind of

## 40365:00 - 40425:00

capability is is is going to open up new

## 40425:00 - 40475:00

new ways to new ways to to set up

## 40475:00 - 40515:00

projects across the organization.

## 40515:00 - 40545:00

>> Um this cloud code thing has been

## 40545:00 - 40560:00

interesting to watch.

## 40560:00 - 40570:00

>> Yeah.

## 40570:00 - 40615:00

>> Uh it went like overnight from something

## 40615:00 - 40655:00

that will like autocomplete developers

## 40655:00 - 40700:00

code to like will go out on the internet

## 40700:00 - 40730:00

and do things and build things to

## 40730:00 - 40745:00

accomplish

## 40745:00 - 40805:00

>> specific tasks. So, is this idea of AI

## 40805:00 - 40845:00

systems going out and doing things like

## 40845:00 - 40885:00

on one hand, you know, I hear I see the

## 40885:00 - 40910:00

story of like and I've said this on the

## 40910:00 - 40935:00

show a couple times, but like you know,

## 40935:00 - 40970:00

the former Amazon CEO of Worldwide

## 40970:00 - 41015:00

Consumers uh going out and vibe coding a

## 41015:00 - 41045:00

CRM over the weekend.

## 41045:00 - 41080:00

>> Um, you know, that's that's cool, but

## 41080:00 - 41105:00

I'm also just like,

## 41105:00 - 41145:00

>> you know, re how real is that? So, I'm

## 41145:00 - 41175:00

curious. Oh, okay. You're giving me a

## 41175:00 - 41200:00

look like, yes, it is real.

## 41200:00 - 41230:00

>> Well, I think that goes back to my idea,

## 41230:00 - 41270:00

right? like those who are able to

## 41270:00 - 41300:00

prototype in this way. It doesn't mean

## 41300:00 - 41330:00

that whatever you've vibe coded into a

## 41330:00 - 41370:00

weekend suddenly turns into $100 million

## 41370:00 - 41410:00

business, right? But it's a way to

## 41410:00 - 41440:00

communicate with your teams

## 41440:00 - 41460:00

>> your intention. So, as long as you have

## 41460:00 - 41500:00

good ideas, you're able to share these

## 41500:00 - 41550:00

ideas in a way that's much more real and

## 41550:00 - 41590:00

to start prototyping much faster.

## 41590:00 - 41615:00

>> Now, there's other ways to communicate

## 41615:00 - 41640:00

your ideas. There's other ways to direct

## 41640:00 - 41680:00

your teams, but that suddenly opens up

## 41680:00 - 41720:00

so much more. It is interesting how AI

## 41720:00 - 41760:00

is and AI is many things but it's a

## 41760:00 - 41795:00

communication technology. it it's

## 41795:00 - 41830:00

becoming that right and this is the kind

## 41830:00 - 41865:00

of thing that that the new the new

## 41865:00 - 41910:00

coding agents are opening up

## 41910:00 - 41945:00

>> is cohhere does cohhere have like a

## 41945:00 - 41985:00

version of this that it's working on

## 41985:00 - 42040:00

>> um I would say like yes we're working on

## 42040:00 - 42065:00

the same kind of capabilities we're

## 42065:00 - 42100:00

building core generic models I would say

## 42100:00 - 42125:00

that's uh it's a bit of a different

## 42125:00 - 42165:00

experience right now uh that we're

## 42165:00 - 42190:00

offering in terms of the north platform

## 42190:00 - 42220:00

but there is a lot of that sort of

## 42220:00 - 42250:00

collaborative work there's a lot of this

## 42250:00 - 42285:00

like you know going out and essentially

## 42285:00 - 42320:00

deploying agents, leveraging external

## 42320:00 - 42355:00

external information. So there's some

## 42355:00 - 42385:00

there's some uh elements that are

## 42385:00 - 42440:00

similar uh but we're less focused

## 42440:00 - 42470:00

specifically on on coding use cases

## 42470:00 - 42500:00

right now.

## 42500:00 - 42530:00

>> U coher obviously has raised a lot of

## 42530:00 - 42585:00

money, more than a billion dollars. Um

## 42585:00 - 42610:00

but

## 42610:00 - 42675:00

I I'm this is not I'll just like draw it

## 42675:00 - 42715:00

out. OpenAI sneezes that over a weekend.

## 42715:00 - 42765:00

Um you have a world now where AI is

## 42765:00 - 42815:00

being developed by a handful of very big

## 42815:00 - 42830:00

companies.

## 42830:00 - 42860:00

>> Uh your former employer Meta is a big

## 42860:00 - 42930:00

player, Amazon, um Google of course,

## 42930:00 - 42975:00

Microsoft and then you know OpenAI and

## 42975:00 - 43020:00

Anthropic with these they raise the

## 43020:00 - 43075:00

entire like uh years worth of VC money

## 43075:00 - 43125:00

uh in a round now. Um what do you think

## 43125:00 - 43155:00

about the risk of the fact that so much

## 43155:00 - 43200:00

of this is being concentrated in so few

## 43200:00 - 43220:00

hands?

## 43220:00 - 43275:00

>> Um honestly I do think it's beneficial

## 43275:00 - 43350:00

to to the ecosystem to have multiple

## 43350:00 - 43395:00

groups who are able to to develop models

## 43395:00 - 43430:00

and to deploy them. I think you know

## 43430:00 - 43455:00

just to give you a concrete example

## 43455:00 - 43500:00

right coher was very early on working on

## 43500:00 - 43545:00

multilingual models. So the ability to

## 43545:00 - 43580:00

understand information, digest

## 43580:00 - 43610:00

information across multiple languages,

## 43610:00 - 43655:00

20 30 and so on languages. We had a line

## 43655:00 - 43705:00

of models that is really well respected,

## 43705:00 - 43765:00

open sourced and so on. Um it's just not

## 43765:00 - 43795:00

on the radar of of some of these

## 43795:00 - 43835:00

companies that are very focused on you

## 43835:00 - 43885:00

know on English ccentric information.

## 43885:00 - 43925:00

Completely fine you know different space

## 43925:00 - 43950:00

for different companies. when we get

## 43950:00 - 43980:00

into markets in Asia, when we get into

## 43980:00 - 44035:00

markets in Europe, suddenly it matters

## 44035:00 - 44070:00

to have a model that is actually

## 44070:00 - 44105:00

state-of-the-art across languages or

## 44105:00 - 44135:00

across the the local language. And so

## 44135:00 - 44170:00

that opens up completely new market.

## 44170:00 - 44240:00

Right now the the the opportunities are

## 44240:00 - 44310:00

so broad that actually there's space for

## 44310:00 - 44355:00

you know upand cominging players to to

## 44355:00 - 44400:00

really keep on growing to have a very

## 44400:00 - 44450:00

healthy uh revenue to bring in talent to

## 44450:00 - 44475:00

actually build new things that are

## 44475:00 - 44500:00

different from some of these other

## 44500:00 - 44535:00

companies are building. So I tend to

## 44535:00 - 44575:00

think it's super healthy to have more

## 44575:00 - 44615:00

rather than fewer companies that are

## 44615:00 - 44655:00

building AI. And I think we're seeing

## 44655:00 - 44680:00

the fact that you know going back to my

## 44680:00 - 44710:00

idea of you know many different AIs who

## 44710:00 - 44740:00

do many different things even at the

## 44740:00 - 44765:00

company level this is what's happening

## 44765:00 - 44785:00

there's a number of players who are

## 44785:00 - 44810:00

building different things and and

## 44810:00 - 44825:00

learning from each other

## 44825:00 - 44850:00

>> but the fact that big tech has so much

## 44850:00 - 44870:00

of it

## 44870:00 - 44895:00

>> not a worry

## 44895:00 - 44915:00

>> it doesn't worry me

## 44915:00 - 44925:00

>> okay

## 44925:00 - 44960:00

>> and I mean you know we could have a a

## 44960:00 - 44995:00

much longer discussion about it

## 44995:00 - 45045:00

>> but it doesn't and it doesn't cause me

## 45045:00 - 45080:00

to lose any sleep over the fact that

## 45080:00 - 45105:00

like what we're building at cohhere has

## 45105:00 - 45150:00

like an amazing amazing paths to to be

## 45150:00 - 45160:00

successful.

## 45160:00 - 45190:00

>> Okay. By the way, I mentioned Anthropic

## 45190:00 - 45230:00

and OpenAI which have Microsoft and

## 45230:00 - 45260:00

Amazon and Google have massive stakes

## 45260:00 - 45280:00

>> and there are many more.

## 45280:00 - 45335:00

>> Yes. Um somebody who does Wario, Dario

## 45335:00 - 45375:00

Amod from Anthropic, well maybe not the

## 45375:00 - 45410:00

fact that he got all that all those

## 45410:00 - 45445:00

billions from Google and Amazon. Um but

## 45445:00 - 45470:00

he does have some things to say about

## 45470:00 - 45505:00

the big tech companies. Here's a thing

## 45505:00 - 45545:00

that he said recently. Uh some of these

## 45545:00 - 45570:00

companies are essentially led by people

## 45570:00 - 45600:00

who have a scientific background. That's

## 45600:00 - 45635:00

my background. It's steab's background

## 45635:00 - 45655:00

for Google DeepMind.

## 45655:00 - 45680:00

>> Uh some of them are led by the

## 45680:00 - 45710:00

generation of entrepreneurs that did

## 45710:00 - 45745:00

social media. There's a long tradition

## 45745:00 - 45785:00

of scientists thinking about the effects

## 45785:00 - 45820:00

of the technology they built

## 45820:00 - 45885:00

>> um and uh not ducking responsibility. I

## 45885:00 - 45915:00

think the motivation of entrepreneurs

## 45915:00 - 45940:00

particularly the generation of the

## 45940:00 - 45985:00

social media entrepreneurs are very

## 45985:00 - 46015:00

different. Uh they the way they

## 46015:00 - 46050:00

interacted you could say manipulated

## 46050:00 - 46085:00

consumers is very different. So

## 46085:00 - 46120:00

basically I don't think he wants them

## 46120:00 - 46125:00

running

## 46125:00 - 46170:00

>> strong opinions from DI which is I guess

## 46170:00 - 46210:00

not not not something um out of

## 46210:00 - 46245:00

character for Dario Holiday.

## 46245:00 - 46270:00

>> Uh do you think that's a legitimate

## 46270:00 - 46300:00

concern?

## 46300:00 - 46320:00

>> Because it's so interesting you're a

## 46320:00 - 46340:00

research scientist

## 46340:00 - 46365:00

>> who also worked at a social media

## 46365:00 - 46385:00

company. So if anyone knows the answer

## 46385:00 - 46410:00

to this it will be you.

## 46410:00 - 46445:00

>> I mean I think what what's really

## 46445:00 - 46485:00

important like no one is going to be

## 46485:00 - 46510:00

good at everything

## 46510:00 - 46560:00

>> right? The question is like how do you

## 46560:00 - 46630:00

get others in the room to advise you on

## 46630:00 - 46665:00

how to build something great? And you

## 46665:00 - 46700:00

know I spent some time at Meta. I would

## 46700:00 - 46740:00

say there was a there was a very strong

## 46740:00 - 46795:00

channel from researchers to to the

## 46795:00 - 46835:00

leadership team and and the opinions

## 46835:00 - 46865:00

were brought into the room. I think you

## 46865:00 - 46900:00

know I've seen that certainly at cohhere

## 46900:00 - 46925:00

where you know the the research team the

## 46925:00 - 46955:00

modeling team the product team like

## 46955:00 - 46990:00

there's a room where all these points of

## 46990:00 - 47030:00

views can come together. I go back to

## 47030:00 - 47070:00

this thought like I can't expect one

## 47070:00 - 47100:00

person to all have all that that

## 47100:00 - 47140:00

information and as long as they're

## 47140:00 - 47180:00

building up the teams that are diverse

## 47180:00 - 47210:00

>> that are listening to these diverse

## 47210:00 - 47240:00

voices like they will build better

## 47240:00 - 47295:00

products at the end of the day. M okay

## 47295:00 - 47350:00

on that note uh as ads have started to

## 47350:00 - 47375:00

enter the picture

## 47375:00 - 47430:00

>> for generative AI um there's a wonder

## 47430:00 - 47465:00

among outsiders like me about whether

## 47465:00 - 47515:00

these companies will uh do things like

## 47515:00 - 47555:00

engagement max and try to optimize for

## 47555:00 - 47590:00

time spent so they can you know get

## 47590:00 - 47645:00

those numbers up. Um, I don't want to

## 47645:00 - 47670:00

ask you whether you think that's going

## 47670:00 - 47690:00

to happen or not, but I want to ask you

## 47690:00 - 47745:00

as a researcher, whether that's even

## 47745:00 - 47780:00

economically feasible. Are the models

## 47780:00 - 47835:00

now efficient enough where like a vis,

## 47835:00 - 47885:00

let's say you were to show an ad, a

## 47885:00 - 47930:00

visit to to like to serve that visit

## 47930:00 - 47975:00

with an LLM, uh, could be a profitable

## 47975:00 - 48010:00

thing. or is it still so expensive to

## 48010:00 - 48060:00

serve these use cases that this even

## 48060:00 - 48095:00

notion of engagement maxing doesn't make

## 48095:00 - 48130:00

sense because economically it's not

## 48130:00 - 48160:00

valid.

## 48160:00 - 48190:00

>> I mean in general right like through

## 48190:00 - 48225:00

trial and error we we find economic

## 48225:00 - 48255:00

models that are viable right like that's

## 48255:00 - 48280:00

still how it is. So it depends a lot on

## 48280:00 - 48310:00

the pricing model and so on and so forth

## 48310:00 - 48325:00

and so

## 48325:00 - 48355:00

>> expensive ads to buy

## 48355:00 - 48400:00

>> but you know it depends you know yeah it

## 48400:00 - 48440:00

depends on how the model is set up. I I

## 48440:00 - 48455:00

don't know that this is the way that

## 48455:00 - 48485:00

that gets rolled out initially. We'll

## 48485:00 - 48515:00

have to see what what's the progression

## 48515:00 - 48555:00

of that. I I do think, you know, we have

## 48555:00 - 48595:00

the ability to tailor content based on

## 48595:00 - 48630:00

the information we have that is there.

## 48630:00 - 48655:00

That is a lever that's going to continue

## 48655:00 - 48680:00

to be used from an economic point of

## 48680:00 - 48695:00

view.

## 48695:00 - 48740:00

>> AI sovereignity. uh before we go

## 48740:00 - 48770:00

>> uh countries are start and and

## 48770:00 - 48810:00

institutions like banks

## 48810:00 - 48855:00

>> uh are starting to build their own their

## 48855:00 - 48910:00

own models or uh they're not relying on

## 48910:00 - 48940:00

off-the-shelf stuff. So talk talk a

## 48940:00 - 48955:00

little bit because this is something

## 48955:00 - 48990:00

Coher is working on. It's something I

## 48990:00 - 49010:00

don't know a lot about the fact that

## 49010:00 - 49045:00

there is this push or at least it's

## 49045:00 - 49075:00

something that is being discussed. So

## 49075:00 - 49105:00

what is AI sovereignty and how is it

## 49105:00 - 49120:00

playing out?

## 49120:00 - 49160:00

>> Yeah, sovereignty has been used in a few

## 49160:00 - 49220:00

different ways. um in some cases it

## 49220:00 - 49245:00

means the ability to have your own

## 49245:00 - 49275:00

model. So in the case of of financial

## 49275:00 - 49330:00

services and banks that is definitely uh

## 49330:00 - 49375:00

something that they spend a lot of time

## 49375:00 - 49405:00

investing in thinking about looking for

## 49405:00 - 49465:00

solutions. They see the opportunity they

## 49465:00 - 49500:00

were I think early adopters even of you

## 49500:00 - 49530:00

know previous generation AI technologies

## 49530:00 - 49555:00

predictive models for example

## 49555:00 - 49600:00

statistical models and so on and so they

## 49600:00 - 49645:00

see this as as the natural evolution. So

## 49645:00 - 49690:00

they're pretty advanced in terms of uh

## 49690:00 - 49720:00

their sophistication and their readiness

## 49720:00 - 49775:00

for AI. Um and often they have the means

## 49775:00 - 49825:00

to to to invest in it. Um and so we're

## 49825:00 - 49855:00

definitely seeing a lot of interest

## 49855:00 - 49890:00

there. Often though, you know, I think

## 49890:00 - 49930:00

the the talent gap makes it a little bit

## 49930:00 - 49955:00

harder for them. So sometimes they've

## 49955:00 - 49975:00

tried to build their own models and so

## 49975:00 - 50005:00

on. Then they come to us and and they're

## 50005:00 - 50030:00

looking for solutions that are a little

## 50030:00 - 50060:00

bit uh more mature out of the box and so

## 50060:00 - 50090:00

on. And so we have really solid

## 50090:00 - 50165:00

partnerships uh going on there. Um it

## 50165:00 - 50190:00

the the other way to think about

## 50190:00 - 50225:00

sovereignty that we're hearing a lot is

## 50225:00 - 50265:00

that companies want a robust plan for

## 50265:00 - 50315:00

AI. And so you know they want options

## 50315:00 - 50355:00

they they they may be using one model

## 50355:00 - 50390:00

but they actually want to have another

## 50390:00 - 50430:00

model uh to be able to to compare to

## 50430:00 - 50480:00

benchmark. If one model access gets cut

## 50480:00 - 50510:00

off or too expensive they have another

## 50510:00 - 50545:00

one. And so there's an aspect of

## 50545:00 - 50570:00

sovereignty that's really about building

## 50570:00 - 50610:00

a robust strategy. It's not about just

## 50610:00 - 50640:00

using your own or using one thing, but

## 50640:00 - 50675:00

it's about having control over the

## 50675:00 - 50705:00

access to the technology.

## 50705:00 - 50730:00

>> Yeah. It's just as you speak about it,

## 50730:00 - 50760:00

to me, it's just amazing how fast this

## 50760:00 - 50800:00

has moved. And going back to our first

## 50800:00 - 50850:00

meeting in 2022, uh the fact that we're

## 50850:00 - 50890:00

it's 2026, so it's been three years and

## 50890:00 - 50900:00

change.

## 50900:00 - 50930:00

>> Uh but it's it's just a world of a

## 50930:00 - 50955:00

difference year to year to year.

## 50955:00 - 50960:00

>> Yeah.

## 50960:00 - 50985:00

>> So, last question to you. Can the pace

## 50985:00 - 51030:00

keep up?

## 51030:00 - 51080:00

it is still moving very fast on so many

## 51080:00 - 51140:00

fronts you know just the the size of uh

## 51140:00 - 51170:00

the investments

## 51170:00 - 51220:00

um I think on adoption we are so early

## 51220:00 - 51265:00

in the curve and so that's that's going

## 51265:00 - 51295:00

to be the next challenge to see how do

## 51295:00 - 51335:00

we how do we enable this technology to

## 51335:00 - 51380:00

sort of disperse through through society

## 51380:00 - 51440:00

through the through the business world

## 51440:00 - 51465:00

um in people's lives and how do we do

## 51465:00 - 51500:00

that successfully but yeah I think the

## 51500:00 - 51535:00

pace especially when it comes to

## 51535:00 - 51585:00

commercialization and adoption is really

## 51585:00 - 51625:00

very very early days. So got a long way

## 51625:00 - 51640:00

to go.

## 51640:00 - 51670:00

>> Seriously. Well Joel, we've spoken a

## 51670:00 - 51700:00

handful of times. I always appreciate

## 51700:00 - 51720:00

how you're able to take these big things

## 51720:00 - 51755:00

that a lot of us are wondering about and

## 51755:00 - 51780:00

grounded in the research and the

## 51780:00 - 51810:00

practical side of things. So you're

## 51810:00 - 51835:00

always welcome on the show and thank you

## 51835:00 - 51845:00

for coming on.

## 51845:00 - 51875:00

>> Thank you. Always a pleasure.

## 51875:00 - 51905:00

>> All right, everybody. Thank you so much

## 51905:00 - 51930:00

for watching and listening and thank you

## 51930:00 - 51965:00

to Qualcomm for having us here at the

## 51965:00 - 51995:00

space at Davos and we'll see you next

## 51995:00 - 52055:00

time on Big Technology Podcast.

## 52055:00 - 52065:00

>> All right,

## 52065:00 - 52070:00

>> thank you.

## 52070:00 - 52105:00

>> That was great. Thank you so much. Thank

## 52105:00 - 52135:00

you.

## 52135:00+

>> Thanks everyone.

