---
source: https://www.youtube.com/watch?v=LKgAx7FWva4
title: "Windsurf CEO: Betting On AI Agents, Pivoting In 48 Hours, And The Future
  of Coding"
author: Y Combinator
date: 2025-05-02
views: 250518
description: >-
  Varun Mohan didn't set out to build one of the fastest-growing AI developer
  tools. He just knew his company had to change, or die.


  After initially betting on GPU virtualization, he saw the writing on the wall:
  if there was a future for his company, it would be at the AI application
  layer, not infra. Over a single weekend, he and his team pivoted to building
  Windsurf— a tool to help everyone, both technical and non-technical, write
  code faster and smarter.


  In this conversation, Varun shares the inside story of how they pivoted at the
  edge of failure, trained new models from scratch, outpaced giants like GitHub
  Copilot, and what the future of building with AI looks like.


  Apply to Y Combinator: https://ycombinator.com/apply

  Work at a startup: https://workatastartup.com


  Chapters (Powered by https://chapterme.co/) - 

  0:00 Intro

  00:53 Windsurf - how big is it, where did it start? 

  3:00 The big pivot 

  6:20 Irrational optimism + uncompromising realism

  7:52 Earliest versions shipped

  10:26 The first customers

  13:13 The transition from Codeium to Windsurf

  19:45 Going up against Github Copilot

  23:15 All insights depreciate; you need to keep proving yourself

  26:50 Strong evals go a long way

  30:15 Windsurf for hardcore engineering

  31:55 Tips to get more precise changes when vibe coding

  35:15 How will Windsurf evolve

  38:00 Will AI become the infinite workhorse?

  38:48 How does Windsurf interview candidates?

  42:48 What happens if we get “just in time” software? 

  44:46 How many non-developers use Windsurf?

  47:28 Thoughts on the GPT wrapper meme

  49:17 Advice for new AI startups

  51:39 Outro
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:46:14.017Z
---

# Windsurf CEO: Betting On AI Agents, Pivoting In 48 Hours, And The Future of Coding

## 00:00 - 20:00

One of the things that I think is is

## 20:00 - 45:00

true for any startup is you have to keep

## 45:00 - 70:00

proving yourself. Every single insight

## 70:00 - 100:00

that we have is a depreciating insight.

## 100:00 - 125:00

You look at a company like Nvidia. If

## 125:00 - 160:00

Nvidia doesn't innovate in the next two

## 160:00 - 205:00

years, AMD will be on their case. That's

## 205:00 - 230:00

why I'm completely okay with a lot of

## 230:00 - 265:00

our insights being wrong. Um if we don't

## 265:00 - 285:00

continually have insights that we are

## 285:00 - 310:00

executing on, uh we are just slowly

## 310:00 - 345:00

dying. This notion of just a developer

## 345:00 - 370:00

is is probably going to broaden out to

## 370:00 - 410:00

what's called a builder. And uh I think

## 410:00 - 435:00

everyone is going to be a builder. I

## 435:00 - 460:00

think software is going to be this very

## 460:00 - 505:00

very democratized thing.

## 505:00 - 605:00

[Music]

## 605:00 - 645:00

Welcome back to another episode of the

## 645:00 - 680:00

Light Cone. Today we've got a real

## 680:00 - 740:00

treat. We have the co-founder and CEO of

## 740:00 - 770:00

Windsurf, one of the people who

## 770:00 - 815:00

literally brought Vibe Coding into

## 815:00 - 860:00

existence, Verun. Thanks for joining us.

## 860:00 - 885:00

Thanks for having me, guys. Where is

## 885:00 - 915:00

Windinsurf now? Like all of us

## 915:00 - 950:00

intuitively know. I mean, well, we use

## 950:00 - 985:00

it, but you know, how big is it now?

## 985:00 - 1015:00

Where is it? Yeah. So, the the product

## 1015:00 - 1045:00

has had well over a million developers

## 1045:00 - 1095:00

kind of use uh the product um has has

## 1095:00 - 1120:00

hundreds of thousands of daily active

## 1120:00 - 1150:00

users right now. It's being used for all

## 1150:00 - 1175:00

sorts of things from modifying large

## 1175:00 - 1210:00

code bases to building apps extremely

## 1210:00 - 1255:00

quickly, 0ero to one. Um and uh and

## 1255:00 - 1275:00

we're super excited to see where the

## 1275:00 - 1300:00

technology is going. Let's get to the

## 1300:00 - 1340:00

brass tax. How did you get started? The

## 1340:00 - 1380:00

company actually started uh four years

## 1380:00 - 1435:00

ago. uh we didn't start as windsurf uh

## 1435:00 - 1465:00

we actually started as a company called

## 1465:00 - 1505:00

exofunction we were a GPU virtualization

## 1505:00 - 1550:00

company at the time uh previously me and

## 1550:00 - 1590:00

my co-founder had worked on autonomous

## 1590:00 - 1630:00

vehicles and ARVR and we believe deep

## 1630:00 - 1650:00

learning was going to transform many

## 1650:00 - 1680:00

many industries uh from financial

## 1680:00 - 1720:00

services to defense to healthcare uh

## 1720:00 - 1755:00

many industries yeah uh we might have

## 1755:00 - 1780:00

timed it wrong though ultimately we

## 1780:00 - 1810:00

built a system to make it easier to run

## 1810:00 - 1855:00

these deep learning workloads uh and

## 1855:00 - 1885:00

similar to what VMware does for

## 1885:00 - 1915:00

computers and CPUs. We did that for

## 1915:00 - 1960:00

GPUs. Um the middle of 2022 rolled

## 1960:00 - 1995:00

around though and what happened at the

## 1995:00 - 2020:00

time was we were managing upwards of

## 2020:00 - 2060:00

10,000 GPUs for a handful of companies

## 2060:00 - 2080:00

and we had made it to a couple million

## 2080:00 - 2120:00

in revenue but the transformer became

## 2120:00 - 2150:00

very popular with these models like text

## 2150:00 - 2185:00

Da Vinci from OpenAI and we felt that

## 2185:00 - 2220:00

that was going to fundamentally disrupt

## 2220:00 - 2260:00

the business we had or that small small

## 2260:00 - 2285:00

business that we had at the time uh

## 2285:00 - 2310:00

because we felt that everyone was going

## 2310:00 - 2340:00

to run these transformer type models and

## 2340:00 - 2365:00

in a world in which everyone was going

## 2365:00 - 2405:00

to run one type of model architecture

## 2405:00 - 2440:00

transformers we thought if we were a GPU

## 2440:00 - 2465:00

infrastructure provider, we would get

## 2465:00 - 2490:00

commoditized, right? If everyone's going

## 2490:00 - 2520:00

to do the same thing, what is our alpha

## 2520:00 - 2545:00

alpha going to be? So, at the time, we

## 2545:00 - 2570:00

basically said, hey, could we take our

## 2570:00 - 2595:00

technology and wholesale pivot the

## 2595:00 - 2625:00

company to do something else? And that's

## 2625:00 - 2660:00

that's scary. Yeah, that was that was a

## 2660:00 - 2690:00

a bet the company moment. We did it

## 2690:00 - 2730:00

within a weekend. Uh so, you know,

## 2730:00 - 2755:00

weekend me and my co-founder had a

## 2755:00 - 2790:00

conversation along the lines of I don't

## 2790:00 - 2805:00

think this is going to work. We don't

## 2805:00 - 2835:00

think we know how to scale this company.

## 2835:00 - 2865:00

Um and uh at the time, we were early

## 2865:00 - 2895:00

adopters of GitHub copilot. We told the

## 2895:00 - 2925:00

rest of the company on Monday and uh

## 2925:00 - 2955:00

everyone started working on Kodium which

## 2955:00 - 2995:00

is the extension product uh the Monday

## 2995:00 - 3025:00

immediately after. I'm just curious to

## 3025:00 - 3070:00

like dig into this pivot story because

## 3070:00 - 3120:00

it's like pretty rare actually to hear

## 3120:00 - 3160:00

like the details of a pivot especially a

## 3160:00 - 3185:00

late stage pivot like at the time that

## 3185:00 - 3210:00

you guys decided to pivot to codium. How

## 3210:00 - 3240:00

far along was the company? How many how

## 3240:00 - 3265:00

many people One of the things about the

## 3265:00 - 3300:00

company was I guess like we tried to

## 3300:00 - 3335:00

embrace a lot of the YC uh sort of

## 3335:00 - 3365:00

analogies here of you know ramen

## 3365:00 - 3400:00

profitability all these other uh sort of

## 3400:00 - 3425:00

key insights. We were only a team of

## 3425:00 - 3450:00

eight people at the time even though we

## 3450:00 - 3475:00

were making a couple million in revenue.

## 3475:00 - 3500:00

We were kind of like free cash flow

## 3500:00 - 3535:00

positive. It was the peak of zero

## 3535:00 - 3565:00

interest rate uh at that time. So the

## 3565:00 - 3590:00

company was a year and a half old. We

## 3590:00 - 3625:00

had raised somehow magically $28 million

## 3625:00 - 3665:00

of of cash at the time. And uh I think

## 3665:00 - 3705:00

the big point here uh in our in our

## 3705:00 - 3740:00

minds was um it doesn't matter if we're

## 3740:00 - 3765:00

doing kind of well now if we didn't know

## 3765:00 - 3795:00

how to scale it, we kind of need to

## 3795:00 - 3825:00

change things like really fast. I guess

## 3825:00 - 3880:00

the thing that's remarkable is when you

## 3880:00 - 3940:00

started the company, you had this thesis

## 3940:00 - 3975:00

where you were betting that a lot of

## 3975:00 - 4000:00

companies were going to build their own

## 4000:00 - 4040:00

custom deep learning pipelines to train

## 4040:00 - 4065:00

birds, right? That was like the thing

## 4065:00 - 4115:00

that was working. But in 2022, you saw

## 4115:00 - 4160:00

the hockey stick shift that suddenly

## 4160:00 - 4190:00

there would be one model that would rule

## 4190:00 - 4235:00

them all. So you were foreshadowing a

## 4235:00 - 4265:00

lot of the future and there's a lot of

## 4265:00 - 4300:00

it that came from that conviction. So

## 4300:00 - 4325:00

I'm curious what were those signs

## 4325:00 - 4350:00

because you had to be really embedded

## 4350:00 - 4380:00

into it to we're making already seven

## 4380:00 - 4405:00

figures. You could have raised a series

## 4405:00 - 4440:00

A. You're like we're going to throw that

## 4440:00 - 4470:00

all that away and burn it. Yeah. So

## 4470:00 - 4495:00

actually even crazily enough we had

## 4495:00 - 4545:00

raised our series A at that time. So but

## 4545:00 - 4565:00

whether or not we should have been able

## 4565:00 - 4600:00

to is a is a different question. No, I

## 4600:00 - 4625:00

think you're you're totally right. I

## 4625:00 - 4645:00

think one of the things that was

## 4645:00 - 4665:00

happening at the time was we were

## 4665:00 - 4685:00

working with largely speaking these

## 4685:00 - 4710:00

autonomous vehicle companies because

## 4710:00 - 4730:00

they had the largest sort of deep

## 4730:00 - 4765:00

learning workloads at the time and we

## 4765:00 - 4800:00

were sort of seeing hey that workload is

## 4800:00 - 4830:00

growing and it's large but we were

## 4830:00 - 4855:00

betting fundamentally that the other

## 4855:00 - 4890:00

workloads which were these other natural

## 4890:00 - 4920:00

language workloads uh kind of like these

## 4920:00 - 4940:00

workloads in these other industries like

## 4940:00 - 4970:00

financial services healthcare would take

## 4970:00 - 5015:00

off but I think once we saw these these

## 5015:00 - 5050:00

models these generative models handle so

## 5050:00 - 5085:00

many of the use cases right uh maybe an

## 5085:00 - 5115:00

example is in the past you would train a

## 5115:00 - 5145:00

BERT model uh to actually go ahead and

## 5145:00 - 5175:00

do sentiment classification. But very

## 5175:00 - 5215:00

quickly when we tried even a bad version

## 5215:00 - 5260:00

of GPT3 like the very old version, we

## 5260:00 - 5285:00

were like this is going to kill

## 5285:00 - 5310:00

sentiment classification. There's no

## 5310:00 - 5345:00

reason why anyone is going to train a

## 5345:00 - 5380:00

very custom model anymore for this task.

## 5380:00 - 5410:00

I think we saw the writing on the wall

## 5410:00 - 5450:00

that our hypothesis was just wrong,

## 5450:00 - 5475:00

right? And uh and that's like one of

## 5475:00 - 5500:00

those things, right? you go in with some

## 5500:00 - 5540:00

thesis on on uh on where you believe the

## 5540:00 - 5570:00

space is going to go, but if your

## 5570:00 - 5600:00

hypothesis is wrong and and you know

## 5600:00 - 5625:00

information on the ground changes, you

## 5625:00 - 5655:00

have to change really fast. So then what

## 5655:00 - 5690:00

did you decide to do? So it's like you

## 5690:00 - 5725:00

decided, okay, we're going to pivot and

## 5725:00 - 5750:00

when we work with founders, that's kind

## 5750:00 - 5770:00

of stage one. So you're not half foot

## 5770:00 - 5795:00

in, half foot out. So you had that

## 5795:00 - 5820:00

conviction, we need to try something

## 5820:00 - 5845:00

out. How do you figure out what was

## 5845:00 - 5870:00

going to be the next step? I think we

## 5870:00 - 5895:00

needed to pick something that actually

## 5895:00 - 5915:00

everyone at the company was going to be

## 5915:00 - 5940:00

excited about. I think if we had picked

## 5940:00 - 5990:00

something that was was what we thought

## 5990:00 - 6015:00

could be valuable but people were not

## 6015:00 - 6045:00

excited about we would ultimately we

## 6045:00 - 6070:00

would fail we'd fail immediately. We

## 6070:00 - 6100:00

came with an opinionated stance of we

## 6100:00 - 6125:00

were early adopters of a product called

## 6125:00 - 6150:00

GitHub copilot. We thought that that was

## 6150:00 - 6180:00

the tip of the iceberg on where the

## 6180:00 - 6200:00

technology could go. Obviously everyone

## 6200:00 - 6240:00

at the company was a developer. Uh dev

## 6240:00 - 6260:00

tool companies generally speaking

## 6260:00 - 6290:00

usually don't do that well in the in the

## 6290:00 - 6325:00

past. They have not. But hey like when

## 6325:00 - 6345:00

you have no other options it's a very

## 6345:00 - 6370:00

easy decision, right? Like you're going

## 6370:00 - 6410:00

to be a zero with a high probability

## 6410:00 - 6435:00

anyways. uh you might as well pick

## 6435:00 - 6450:00

something that you think could be

## 6450:00 - 6470:00

valuable and everyone's going to be

## 6470:00 - 6495:00

motivated to work on. I everyone's

## 6495:00 - 6525:00

forgot this now it feels like because

## 6525:00 - 6560:00

GitHub copilot's in the background but

## 6560:00 - 6595:00

at that particular moment it felt

## 6595:00 - 6625:00

inevitable that copilot was going to win

## 6625:00 - 6665:00

right like it just had everything like

## 6665:00 - 6705:00

the GitHub connection Microsoft

## 6705:00 - 6760:00

distribution like open AI open AI yeah

## 6760:00 - 6795:00

like it it would it seemed like no one

## 6795:00 - 6820:00

could compete so how did you have like

## 6820:00 - 6855:00

the bravery to be like ah yeah we can

## 6855:00 - 6905:00

totally crush yeah co-pilot yeah so this

## 6905:00 - 6930:00

is where uh there's there's like an

## 6930:00 - 6965:00

irrational optimism piece I've said this

## 6965:00 - 7000:00

before but uh to the company. But I

## 7000:00 - 7030:00

think startups require like two distinct

## 7030:00 - 7070:00

beliefs and they're they actually kind

## 7070:00 - 7110:00

of like run counter uh to to each other.

## 7110:00 - 7135:00

You need this irrational optimism

## 7135:00 - 7160:00

because if you don't have the optimism,

## 7160:00 - 7185:00

you just won't do anything. You're just

## 7185:00 - 7215:00

a pessimist and a skeptic and those

## 7215:00 - 7235:00

people don't really accomplish anything

## 7235:00 - 7285:00

in life. Um and you need uncompromising

## 7285:00 - 7310:00

realism, which is that when the when the

## 7310:00 - 7340:00

facts change, you actually change your

## 7340:00 - 7375:00

mind, right? Uh and that's a very hard

## 7375:00 - 7405:00

thing to do both because the thing that

## 7405:00 - 7430:00

makes you succeed through irrational

## 7430:00 - 7460:00

optimism like you know is exactly

## 7460:00 - 7495:00

opposite to the things that allow you to

## 7495:00 - 7530:00

be a very realistic company. So

## 7530:00 - 7560:00

irrational optimism we basically said

## 7560:00 - 7590:00

hey we know how to run and train models

## 7590:00 - 7615:00

ourselves. We actually trained the first

## 7615:00 - 7650:00

autocomplete models ourselves and ran it

## 7650:00 - 7685:00

on our product gave it out for free. I

## 7685:00 - 7715:00

don't think we had the exact road map on

## 7715:00 - 7745:00

where this was going but we just felt

## 7745:00 - 7785:00

there was a lot more to do here. Um and

## 7785:00 - 7820:00

if the if uh if we couldn't do it then I

## 7820:00 - 7845:00

guess we'd die. uh but we might as well

## 7845:00 - 7880:00

bet that we could do it. Were your early

## 7880:00 - 7910:00

versions better than copilot GitHub

## 7910:00 - 7945:00

copilot at the time? So our earliest

## 7945:00 - 7965:00

version that we shipped out was

## 7965:00 - 8000:00

materially worse than GitHub copilot.

## 8000:00 - 8040:00

The only difference was it was free. Uh

## 8040:00 - 8080:00

we built a VS code extension after pivot

## 8080:00 - 8105:00

within I think 2 months we had shipped

## 8105:00 - 8135:00

the product and given it out to

## 8135:00 - 8165:00

hackernews uh like posted something on

## 8165:00 - 8210:00

hackernews. Um and uh we we built that

## 8210:00 - 8240:00

out. it was missing a lot of key

## 8240:00 - 8260:00

features like the model that we were

## 8260:00 - 8285:00

running was like an open source model

## 8285:00 - 8310:00

that was not nearly good as the model

## 8310:00 - 8345:00

that GitHub copilot was running. Uh very

## 8345:00 - 8375:00

quickly then our training infrastructure

## 8375:00 - 8405:00

got better. So we actually went out and

## 8405:00 - 8440:00

trained our own models uh based on the

## 8440:00 - 8470:00

task and then suddenly it actually got

## 8470:00 - 8495:00

capabilities that even GitHub copilot

## 8495:00 - 8515:00

didn't within 2 months. Basic

## 8515:00 - 8550:00

capabilities. Now we'd find this like

## 8550:00 - 8570:00

hilarious that it was even

## 8570:00 - 8600:00

state-of-the-art but our our model could

## 8600:00 - 8625:00

actually fill in the middle of code. So

## 8625:00 - 8650:00

when you're writing code, you're not

## 8650:00 - 8680:00

only just adding code at the end of your

## 8680:00 - 8705:00

cursor, but you're filling it in between

## 8705:00 - 8750:00

two parts between two parts of a line,

## 8750:00 - 8785:00

right? And that code is very incomplete

## 8785:00 - 8810:00

and looks nothing like the training data

## 8810:00 - 8845:00

of these original models, right? So we

## 8845:00 - 8870:00

trained our models to make it actually

## 8870:00 - 8905:00

very very capable for that use case. And

## 8905:00 - 8930:00

uh that actually allowed us to pull

## 8930:00 - 8975:00

ahead in terms of the quality, latency,

## 8975:00 - 8995:00

um we were able to control a lot of

## 8995:00 - 9020:00

details within a couple months. So the

## 9020:00 - 9040:00

beginning of 2023, I'd say the

## 9040:00 - 9070:00

autocomplete capabilities were much

## 9070:00 - 9100:00

better than what co-pilot had. Was that

## 9100:00 - 9125:00

a totally new capability for you guys?

## 9125:00 - 9150:00

Cuz like you guys have been building GPU

## 9150:00 - 9180:00

infrastructure. It sounds like you

## 9180:00 - 9200:00

basically hacked together the first

## 9200:00 - 9230:00

version by taking an off-the-shelf open

## 9230:00 - 9265:00

source model, sticking it into like a VS

## 9265:00 - 9290:00

Code extension and just kind of like

## 9290:00 - 9310:00

wiring the two to like talk to each

## 9310:00 - 9335:00

other. But then right after that, you

## 9335:00 - 9365:00

had to train your own coding model like

## 9365:00 - 9390:00

from scratch. And you guys have been

## 9390:00 - 9415:00

like following the transformer stuff,

## 9415:00 - 9445:00

but like you hadn't built it. Like in

## 9445:00 - 9465:00

order to do that, I assume you had to

## 9465:00 - 9500:00

like download all of GitHub and like

## 9500:00 - 9530:00

train a whole model from scratch. How

## 9530:00 - 9550:00

did you all figure out how to do that in

## 9550:00 - 9590:00

like only two months? Yeah. Um it's a

## 9590:00 - 9620:00

it's a great question. So first of all,

## 9620:00 - 9645:00

when we ran the model ourselves, the

## 9645:00 - 9665:00

reason why we were able to run it and

## 9665:00 - 9690:00

provide it for free is we actually had

## 9690:00 - 9725:00

our own inference runtime at the time

## 9725:00 - 9750:00

and that that obviously came from the

## 9750:00 - 9775:00

fact that we were originally a GPU

## 9775:00 - 9800:00

virtualization company to start with. So

## 9800:00 - 9825:00

that enabled us to actually ship the

## 9825:00 - 9855:00

vzero with an open source product uh

## 9855:00 - 9880:00

quite quickly. Immediately after that,

## 9880:00 - 9900:00

you're totally right. We had never

## 9900:00 - 9930:00

trained a model like this in the past.

## 9930:00 - 9970:00

Uh but I think we hired people that were

## 9970:00 - 10015:00

smart, capable, and and uh excited to to

## 10015:00 - 10045:00

win. Uh so we needed to figure it out.

## 10045:00 - 10065:00

There is no other option, right?

## 10065:00 - 10100:00

otherwise you die. Um, makes the

## 10100:00 - 10130:00

decision-m really really simple. So,

## 10130:00 - 10160:00

yeah, we had to figure out how how do

## 10160:00 - 10185:00

you get a lot of data? How do you do

## 10185:00 - 10210:00

this at scale? How do you clean this

## 10210:00 - 10240:00

data? How do you make it so that it's

## 10240:00 - 10270:00

actually capable of of uh handling this

## 10270:00 - 10305:00

case where code is very incomplete? And

## 10305:00 - 10340:00

uh we shipped a we shipped a a model

## 10340:00 - 10375:00

like very very quickly after that. Wow.

## 10375:00 - 10395:00

And you did all of that with like

## 10395:00 - 10430:00

eightish people in two months. Yeah,

## 10430:00 - 10470:00

that's right. And then right after that

## 10470:00 - 10525:00

because you were running your own models

## 10525:00 - 10550:00

you started getting interesting

## 10550:00 - 10585:00

customers right? Yeah. So basically what

## 10585:00 - 10610:00

happened the product was free at the

## 10610:00 - 10640:00

time. So we ended up getting a lot of

## 10640:00 - 10665:00

developers using the product across all

## 10665:00 - 10710:00

the ids. So VS code jet brains um

## 10710:00 - 10745:00

Eclipse Vim company started reaching out

## 10745:00 - 10770:00

because they not wanted to not only I

## 10770:00 - 10805:00

guess run the product in a secure way.

## 10805:00 - 10830:00

They also wanted to personalize it to

## 10830:00 - 10850:00

all the private data inside the company.

## 10850:00 - 10880:00

So very quickly afterwards in the next

## 10880:00 - 10920:00

coming months companies like Dell, JP

## 10920:00 - 10950:00

Morgan Chase started to become customers

## 10950:00 - 10985:00

of our of our product. Um now these

## 10985:00 - 11010:00

companies have like tens of thousands of

## 11010:00 - 11035:00

developers on the product internally.

## 11035:00 - 11080:00

But we started actually m making a lot

## 11080:00 - 11105:00

of focus of the company. Making sure

## 11105:00 - 11130:00

that the product works on these very

## 11130:00 - 11155:00

large code bases. Some of these

## 11155:00 - 11175:00

companies have code bases that are well

## 11175:00 - 11215:00

over a 100 million lines of code, right?

## 11215:00 - 11245:00

And making sure that the suggestions are

## 11245:00 - 11275:00

are fast is one thing, but making sure

## 11275:00 - 11305:00

it's actually personalized to the

## 11305:00 - 11325:00

codebase and the environment that they

## 11325:00 - 11350:00

have was almost a requirement at the

## 11350:00 - 11380:00

time. You did that pivot, you built it

## 11380:00 - 11420:00

in two months, then shipped it, and

## 11420:00 - 11450:00

within a couple of months, you got these

## 11450:00 - 11485:00

big logos. Yeah. So, I mean, obviously

## 11485:00 - 11510:00

these companies take some time to time

## 11510:00 - 11550:00

to close, but pilots were starting uh

## 11550:00 - 11585:00

within a within like a couple months or

## 11585:00 - 11620:00

a quarter after that. Uh, you know,

## 11620:00 - 11645:00

obviously we had no sales people at the

## 11645:00 - 11670:00

company, so like the founding team was

## 11670:00 - 11700:00

just trying to run as many pilots as

## 11700:00 - 11725:00

possible. to see what would ultimately

## 11725:00 - 11750:00

work. At what point did you expand

## 11750:00 - 11785:00

beyond just the VS Code extension into

## 11785:00 - 11815:00

supporting all these other IDEs? That

## 11815:00 - 11845:00

was actually very very soon afterwards.

## 11845:00 - 11880:00

Um how did you think about that? Like

## 11880:00 - 11900:00

you know there's like one argument that

## 11900:00 - 11935:00

you could make which is like there's

## 11935:00 - 11975:00

lots of VS Code developers. You had a

## 11975:00 - 12010:00

tiny team. You could have made the

## 12010:00 - 12040:00

argument that I just focus on building a

## 12040:00 - 12070:00

great experience for VS Code. You'd only

## 12070:00 - 12095:00

captured a tiny percentage of the market

## 12095:00 - 12135:00

of all possible VS VS Code developers.

## 12135:00 - 12165:00

And that that's not what you did. you

## 12165:00 - 12200:00

expanded like horizontally very quickly

## 12200:00 - 12235:00

and built extensions for all those IDEs.

## 12235:00 - 12270:00

Why? I think maybe the fundamental

## 12270:00 - 12310:00

reason that that we thought was quite

## 12310:00 - 12330:00

critical is if we were going to work

## 12330:00 - 12355:00

with companies, companies have

## 12355:00 - 12385:00

developers that write in many languages.

## 12385:00 - 12425:00

Uh like for instance uh like you know a

## 12425:00 - 12450:00

company like JP Morgan Chase might have

## 12450:00 - 12475:00

over half of their developers writing in

## 12475:00 - 12505:00

Java and for those developers they are

## 12505:00 - 12540:00

going to use Jetrains and Intelligj.

## 12540:00 - 12585:00

Intelligj is over 70 to 80% of all Java

## 12585:00 - 12615:00

developers in the world currently use uh

## 12615:00 - 12650:00

Intelligj right now. So we would just

## 12650:00 - 12685:00

need to turn away a lot of companies

## 12685:00 - 12705:00

like a lot of companies would not be

## 12705:00 - 12735:00

able to use us as the de facto solution

## 12735:00 - 12760:00

like we'd be one of many solutions

## 12760:00 - 12790:00

inside the company. Um so because of

## 12790:00 - 12820:00

that we made the decision but luckily

## 12820:00 - 12840:00

because we made the decision early

## 12840:00 - 12865:00

enough it changed the architecture of

## 12865:00 - 12890:00

how we built the product out which is to

## 12890:00 - 12930:00

say we are not like building a separate

## 12930:00 - 12950:00

version of the product for every single

## 12950:00 - 12975:00

ID. We have a lot of shared

## 12975:00 - 13005:00

infrastructure that actually lives on a

## 13005:00 - 13040:00

per editor basis. So it's actually a

## 13040:00 - 13070:00

very very small amount of code that

## 13070:00 - 13090:00

actually needs to get written to make

## 13090:00 - 13120:00

sure we can support as many ids as

## 13120:00 - 13140:00

possible. Um, so this is one of those

## 13140:00 - 13165:00

things that an early decision that we

## 13165:00 - 13195:00

made ended up making it much easier to

## 13195:00 - 13220:00

make this transition. How about the

## 13220:00 - 13250:00

transition from Kodium to WinSurf? At

## 13250:00 - 13290:00

the time we, you know, now now we're

## 13290:00 - 13320:00

probably going to middle of 2023. We

## 13320:00 - 13345:00

start working with some very large

## 13345:00 - 13370:00

enterprises. Within the next year, like

## 13370:00 - 13395:00

the business has gotten well over sort

## 13395:00 - 13435:00

of eight figures in in in revenue um

## 13435:00 - 13465:00

just from these enterprises using the

## 13465:00 - 13485:00

product and we have this like free

## 13485:00 - 13515:00

individual product. But I think one of

## 13515:00 - 13550:00

the things about this industry that we

## 13550:00 - 13575:00

all kind of know is the space moves

## 13575:00 - 13625:00

really really fast and uh we basically

## 13625:00 - 13660:00

are always making bets on things that

## 13660:00 - 13690:00

are not working right actually most of

## 13690:00 - 13720:00

the bets we make in the company don't

## 13720:00 - 13760:00

work and I'm excited uh when I'm like

## 13760:00 - 13800:00

happy when we are when we're let's say

## 13800:00 - 13825:00

only 50% of the things we're doing are

## 13825:00 - 13855:00

actually working because I think when if

## 13855:00 - 13890:00

a 100% of the things we're doing uh are

## 13890:00 - 13935:00

working um I think like it's a very bad

## 13935:00 - 13960:00

sign for us because it's probably like

## 13960:00 - 14000:00

one of one of maybe three things. Um the

## 14000:00 - 14030:00

first thing it it it is is like hey

## 14030:00 - 14060:00

we're not trying hard enough. Uh right

## 14060:00 - 14085:00

that's that's probably what it means.

## 14085:00 - 14115:00

The second thing is we somehow have a

## 14115:00 - 14150:00

lot of hubris right and the hubris is

## 14150:00 - 14175:00

like we believe everything we do is

## 14175:00 - 14205:00

right even despite the facts that are

## 14205:00 - 14235:00

that are sort of on the ground. And then

## 14235:00 - 14270:00

um the the sort of third key piece is

## 14270:00 - 14295:00

here is we're not actually testing our

## 14295:00 - 14325:00

hypotheses in a way that like tells us

## 14325:00 - 14355:00

where the future is going. We're not

## 14355:00 - 14380:00

actually at the frontier of what the

## 14380:00 - 14410:00

capabilities and technology um

## 14410:00 - 14450:00

ultimately is. We believed actually in

## 14450:00 - 14475:00

the very beginning of last year that

## 14475:00 - 14505:00

agents were going to be extremely huge

## 14505:00 - 14535:00

and we had prototypes of this in the

## 14535:00 - 14560:00

beginning of last year and and they just

## 14560:00 - 14585:00

didn't work. But there were different

## 14585:00 - 14610:00

pieces we were building that we felt

## 14610:00 - 14630:00

were going to be important to making

## 14630:00 - 14660:00

agents work which is understanding large

## 14660:00 - 14695:00

code bases understanding the intent of

## 14695:00 - 14725:00

developers making edits on the codebase

## 14725:00 - 14750:00

really really quickly and we had all

## 14750:00 - 14775:00

these pieces. The thing we didn't have

## 14775:00 - 14805:00

is a model that was capable of calling

## 14805:00 - 14845:00

these tools efficiently enough. And then

## 14845:00 - 14865:00

obviously in the middle of last year

## 14865:00 - 14895:00

that completely changed with the advent

## 14895:00 - 14955:00

of like set um 35 right and with that we

## 14955:00 - 14995:00

basically said okay we now have these

## 14995:00 - 15030:00

agent capabilities but the ceiling of

## 15030:00 - 15060:00

what is we can show to our developers on

## 15060:00 - 15100:00

VS code was limited. We were not able to

## 15100:00 - 15125:00

provide a good enough experience and we

## 15125:00 - 15145:00

thought what was going to happen is

## 15145:00 - 15185:00

developers would spend way more time not

## 15185:00 - 15210:00

writing software but reviewing software

## 15210:00 - 15240:00

that the AI was going to put out. We are

## 15240:00 - 15270:00

I think a technology company at heart

## 15270:00 - 15300:00

and I you know I I think we are a we are

## 15300:00 - 15330:00

a product company but I think the

## 15330:00 - 15370:00

product serves the technology which is

## 15370:00 - 15410:00

to say we want to make the product as

## 15410:00 - 15435:00

good as possible to make it so that

## 15435:00 - 15465:00

people can experience the technology

## 15465:00 - 15495:00

right and we felt that we were you know

## 15495:00 - 15520:00

with VS code we were not able to do that

## 15520:00 - 15550:00

so the middle of last year we decided

## 15550:00 - 15580:00

hey like we need to actually go out and

## 15580:00 - 15630:00

actually have our own ID out there um so

## 15630:00 - 15650:00

that's what that's what triggered

## 15650:00 - 15680:00

actually creating winerf the way that

## 15680:00 - 15710:00

you did that was you forked VS code for

## 15710:00 - 15740:00

VS code was got a whole new set of

## 15740:00 - 15760:00

capabilities that you guys had to learn

## 15760:00 - 15790:00

like basically how to like develop on

## 15790:00 - 15825:00

this VS codebase that I'm sure is super

## 15825:00 - 15850:00

complicated. Yeah, we needed to figure

## 15850:00 - 15880:00

that out. Uh that was one once again

## 15880:00 - 15910:00

another thing where uh we ended up

## 15910:00 - 15960:00

shipping windsurf out in uh within uh

## 15960:00 - 15980:00

less than 3 months of starting the

## 15980:00 - 16010:00

project. Uh that's when we we shipped it

## 16010:00 - 16035:00

out across all operating systems. Wow.

## 16035:00 - 16070:00

And what what happened like was did it

## 16070:00 - 16105:00

like take off immediately or was it

## 16105:00 - 16140:00

unnoticed for for a long time? It took

## 16140:00 - 16170:00

off pretty quickly I would say. Um I

## 16170:00 - 16190:00

think the speed at which it took off

## 16190:00 - 16225:00

among early adopters was was quite high.

## 16225:00 - 16250:00

There were obviously some very rough

## 16250:00 - 16270:00

edges and this is like one of those

## 16270:00 - 16290:00

things where you know because of the

## 16290:00 - 16315:00

rough edges obviously people started

## 16315:00 - 16350:00

coming and leaving the platform fairly

## 16350:00 - 16380:00

quickly. But what we saw was like as we

## 16380:00 - 16410:00

improved the capabilities of the agent

## 16410:00 - 16430:00

as we improved the capabilities of the

## 16430:00 - 16465:00

passive experience even the passive tab

## 16465:00 - 16515:00

experience has made massive leaps um in

## 16515:00 - 16540:00

the last like couple months. We started

## 16540:00 - 16570:00

realizing that not only were people

## 16570:00 - 16600:00

talking about the product more and more

## 16600:00 - 16620:00

uh people were also staying on the

## 16620:00 - 16645:00

product uh more and more at a higher

## 16645:00 - 16695:00

rate. How many people worked on shipping

## 16695:00 - 16750:00

windsurf? And it was done in a period of

## 16750:00 - 16780:00

one or two months. Uh a couple months.

## 16780:00 - 16810:00

So yeah, like less than three months. Um

## 16810:00 - 16835:00

this was another I wouldn't say it's a

## 16835:00 - 16860:00

bet the company moment because it's not

## 16860:00 - 16885:00

a fundamentally different uh sort of

## 16885:00 - 16910:00

paradigm compared to like moving from a

## 16910:00 - 16960:00

GPU virtualization product to a to an

## 16960:00 - 17005:00

like a an AI code product. But yeah, it

## 17005:00 - 17030:00

was uh anyone that could work on it

## 17030:00 - 17060:00

needed to kind of like drop what they

## 17060:00 - 17085:00

were working on in the past and work on

## 17085:00 - 17115:00

it immediately. And at that time, how

## 17115:00 - 17140:00

how big uh were you guys? The

## 17140:00 - 17185:00

engineering team was probably still less

## 17185:00 - 17235:00

than 25 people. Wow. This is crazy.

## 17235:00 - 17265:00

Interestingly, our company actually from

## 17265:00 - 17305:00

an employee standpoint actually didn't

## 17305:00 - 17345:00

have that few people. We actually had a

## 17345:00 - 17380:00

fairly large go to market team because

## 17380:00 - 17415:00

it's in the AI space. One thing that's

## 17415:00 - 17435:00

like a little bit weird about our

## 17435:00 - 17455:00

company compared to most other companies

## 17455:00 - 17480:00

is we have a fairly large go to market

## 17480:00 - 17510:00

team. Like we were selling our product

## 17510:00 - 17545:00

to the largest Fortune 500 companies.

## 17545:00 - 17575:00

It's very hard to do that purely by

## 17575:00 - 17605:00

letting them swipe a credit card. Uh you

## 17605:00 - 17630:00

need a lot of support. you need to make

## 17630:00 - 17655:00

sure that the that the technology is

## 17655:00 - 17685:00

like getting adopted properly. Um, which

## 17685:00 - 17715:00

is very different than just give the

## 17715:00 - 17745:00

people the product and see it grow um

## 17745:00 - 17770:00

effectively. So from an engineering

## 17770:00 - 17795:00

standpoint, we've always run fairly

## 17795:00 - 17830:00

lean. Uh but because of the market

## 17830:00 - 17850:00

interest, we've always had a lot of

## 17850:00 - 17875:00

people in go to market actually. Who are

## 17875:00 - 17905:00

like sort of the ideal people to go into

## 17905:00 - 17930:00

that function? Is it you know really

## 17930:00 - 17960:00

good engineers who want to be forward

## 17960:00 - 17995:00

deployed? Yeah, we so we have two

## 17995:00 - 18015:00

components of it. We have account

## 18015:00 - 18060:00

executives. These are folks that um in

## 18060:00 - 18090:00

general we we try to find people that

## 18090:00 - 18120:00

are very curious and excited about the

## 18120:00 - 18145:00

capabilities. In fact, people that would

## 18145:00 - 18170:00

use windsurf in their free time because

## 18170:00 - 18190:00

they're they're providing the product to

## 18190:00 - 18225:00

leaders who also love software and

## 18225:00 - 18250:00

technology, right? So, if they're if

## 18250:00 - 18290:00

they're just completely just unaware of

## 18290:00 - 18305:00

the technology, they're not going to be

## 18305:00 - 18325:00

helpful. And then we also have these

## 18325:00 - 18375:00

deployed engineer uh like sort of roles

## 18375:00 - 18405:00

similar to what you said uh that get

## 18405:00 - 18425:00

their hands really dirty with the

## 18425:00 - 18445:00

technology and make sure that our

## 18445:00 - 18470:00

customers get the most value from the

## 18470:00 - 18500:00

from the technology. I mean the wild

## 18500:00 - 18535:00

thing is uh because everyone uses wind

## 18535:00 - 18580:00

surf it sounded like um you're having

## 18580:00 - 18625:00

even these AEES who are non-technical

## 18625:00 - 18675:00

become like just vibe coding champions.

## 18675:00 - 18705:00

Yeah. No, one of our biggest users of

## 18705:00 - 18745:00

Windsurf at the company is a is a

## 18745:00 - 18795:00

nontechnical person who leads u uh like

## 18795:00 - 18830:00

partnerships uh at the company. Uh he

## 18830:00 - 18870:00

has actually replaced buying a bunch of

## 18870:00 - 18910:00

sales tools uh inside the company. uh

## 18910:00 - 18935:00

and uh this is one of those things where

## 18935:00 - 18960:00

I think windsurf is giving power back to

## 18960:00 - 18990:00

the domain experts right in the past

## 18990:00 - 19020:00

what would happen in an organization is

## 19020:00 - 19050:00

he would need to talk to a product

## 19050:00 - 19080:00

manager who would talk to an engineer

## 19080:00 - 19105:00

who and the engineer would have a large

## 19105:00 - 19135:00

backlog because there this clearly

## 19135:00 - 19155:00

doesn't immediately make the product

## 19155:00 - 19185:00

better right so this has to be a lower

## 19185:00 - 19225:00

priority but now he is actually kind of

## 19225:00 - 19255:00

uh empowered to actually go and build

## 19255:00 - 19280:00

these apps does he have any programming

## 19280:00 - 19320:00

background at all interesting cuz that's

## 19320:00 - 19340:00

definitely one of the controversies on

## 19340:00 - 19365:00

Twitter at the moment is just like is

## 19365:00 - 19390:00

vibe can you actually vibe code unless

## 19390:00 - 19425:00

you know some amount of coding already.

## 19425:00 - 19465:00

Yeah. One of the things we do have is if

## 19465:00 - 19490:00

we do need to deploy one of these apps,

## 19490:00 - 19525:00

we have a person that actually focuses

## 19525:00 - 19545:00

on making sure that these apps are

## 19545:00 - 19575:00

secure and deployed. But the amount of

## 19575:00 - 19600:00

leverage that that person has is

## 19600:00 - 19635:00

ridiculous. Instead of him going out and

## 19635:00 - 19670:00

building all of these apps, the Vzero

## 19670:00 - 19705:00

could actually get built by by people

## 19705:00 - 19720:00

that are domain experts but

## 19720:00 - 19745:00

non-technical inside the company. With

## 19745:00 - 19770:00

the Kodium launch, you went head-on

## 19770:00 - 19815:00

against like Microsoft and GitHub and

## 19815:00 - 19840:00

like you know these incumb huge

## 19840:00 - 19880:00

incumbents. with the ID launch, you went

## 19880:00 - 19910:00

sort of head-on against cursor. It's

## 19910:00 - 19950:00

like the hot startup of the moment and

## 19950:00 - 20005:00

like um I know again how was how did you

## 20005:00 - 20035:00

all think about that internally? This

## 20035:00 - 20055:00

might be a weird thing about our

## 20055:00 - 20080:00

company, but our company just doesn't

## 20080:00 - 20120:00

have like like morale is not really

## 20120:00 - 20160:00

affected by what other companies do,

## 20160:00 - 20205:00

right? Uh it's not possible if uh like

## 20205:00 - 20235:00

our company has gone through a lot of

## 20235:00 - 20260:00

basically very turbulent times. the fact

## 20260:00 - 20305:00

that we needed to pivot at 10 uh 10 10

## 20305:00 - 20330:00

employees and just completely kill our

## 20330:00 - 20365:00

idea is like a normal thing for the

## 20365:00 - 20390:00

company and then second of all kind of

## 20390:00 - 20420:00

like the companies that are relevant in

## 20420:00 - 20465:00

our space has always been a fluctuating

## 20465:00 - 20495:00

uh set of companies like you know I I

## 20495:00 - 20520:00

really respect all the companies in our

## 20520:00 - 20555:00

space but yeah co-pilot if you were to

## 20555:00 - 20585:00

go to the beginning of 2023 everyone

## 20585:00 - 20605:00

would have thought GitHub copilot was

## 20605:00 - 20640:00

the was the product that everyone would

## 20640:00 - 20665:00

be would use and there was no point

## 20665:00 - 20695:00

building and in the middle uh kind of

## 20695:00 - 20720:00

Devon came out and like everyone was

## 20720:00 - 20750:00

like hey like Devon is going to solve

## 20750:00 - 20775:00

everything, right? Um, and and I'm sure

## 20775:00 - 20805:00

they're doing good work now. Uh, but and

## 20805:00 - 20835:00

then after that, obviously, Curser is is

## 20835:00 - 20860:00

doing a really great job. So, I think

## 20860:00 - 20895:00

what really matters to us most is are we

## 20895:00 - 20920:00

actually do we have a good long-term

## 20920:00 - 20955:00

strategy and are we executing in a way

## 20955:00 - 20975:00

where we're getting towards that

## 20975:00 - 21000:00

long-term strategy while being flexible

## 21000:00 - 21025:00

with the details, right? And as long as

## 21025:00 - 21055:00

we're doing that, I think we we have a

## 21055:00 - 21075:00

fighter's chance, right? And that's like

## 21075:00 - 21110:00

the way we've always Do you educate

## 21110:00 - 21140:00

yourself at all on the competitor's

## 21140:00 - 21175:00

products, though? Yeah. Yeah. I think we

## 21175:00 - 21200:00

don't want to put our heads in the sand

## 21200:00 - 21225:00

and kind of tell ourselves our product

## 21225:00 - 21270:00

is awesome. um and uh and and just kind

## 21270:00 - 21300:00

of because it's very easy to do that um

## 21300:00 - 21325:00

especially given the fact that before we

## 21325:00 - 21350:00

worked on Windsor the company was also

## 21350:00 - 21385:00

growing very very quickly from like a

## 21385:00 - 21400:00

revenue standpoint. What sort of

## 21400:00 - 21430:00

opinions did you have or what taste or

## 21430:00 - 21475:00

opinions did you have for the full IDE

## 21475:00 - 21520:00

um that was sort of maybe different to

## 21520:00 - 21560:00

cursor? I'm actually asking is curs is a

## 21560:00 - 21600:00

very well-liked product obviously and so

## 21600:00 - 21630:00

at a product level why are you like oh

## 21630:00 - 21650:00

yeah like actually we want to build it

## 21650:00 - 21680:00

this way. Yeah. No, I think it's a great

## 21680:00 - 21725:00

question. Uh so maybe the first point is

## 21725:00 - 21750:00

at the time actually when we started

## 21750:00 - 21775:00

working on windsurf all the products

## 21775:00 - 21800:00

were basically chat and this

## 21800:00 - 21825:00

autocomplete uh capability. I think

## 21825:00 - 21860:00

that's basically what uh GitHub Copel

## 21860:00 - 21890:00

was, what cursor was at the time. I

## 21890:00 - 21910:00

think we took a very opinionated stance

## 21910:00 - 21955:00

that we thought agents were were uh

## 21955:00 - 21975:00

where the technology was actually going.

## 21975:00 - 22010:00

We were the first agentic editor that

## 22010:00 - 22060:00

was out there. Um and uh I think the

## 22060:00 - 22090:00

biggest sort of takeaway was we didn't

## 22090:00 - 22115:00

believe in this kind of paradigm where

## 22115:00 - 22135:00

everyone would be at mentioning

## 22135:00 - 22165:00

everything, right? This almost reminded

## 22165:00 - 22200:00

us of like the anti pattern of what

## 22200:00 - 22230:00

Google and and these search engines were

## 22230:00 - 22255:00

before like Google improved their

## 22255:00 - 22285:00

product a lot which was kind of like

## 22285:00 - 22320:00

these landing pages that had like every

## 22320:00 - 22355:00

distinct kind of like bucket of things

## 22355:00 - 22380:00

you could search for. But Google came

## 22380:00 - 22410:00

out with this very clean search box.

## 22410:00 - 22435:00

Even Google at the time you would need

## 22435:00 - 22455:00

you would get better answers if you

## 22455:00 - 22510:00

wrote and or uh like site link. Um and

## 22510:00 - 22535:00

now it's gotten way better, right? And I

## 22535:00 - 22565:00

guess we had a belief that the the

## 22565:00 - 22600:00

software would get more and more easy to

## 22600:00 - 22630:00

build, right? And we would build from

## 22630:00 - 22660:00

that starting point when we saw all the

## 22660:00 - 22685:00

other players in the space making their

## 22685:00 - 22720:00

product so configurable in a way that we

## 22720:00 - 22750:00

thought was I think good for users now

## 22750:00 - 22775:00

for what the technology was but

## 22775:00 - 22800:00

something that wouldn't be unnecessary

## 22800:00 - 22830:00

down the line. So we invested in

## 22830:00 - 22860:00

capabilities like how do you deeply

## 22860:00 - 22890:00

understand the codebase to understand

## 22890:00 - 22920:00

the intent of the developer? How do you

## 22920:00 - 22955:00

how do you actually go out and uh and

## 22955:00 - 22985:00

and make changes in a way that's like

## 22985:00 - 23020:00

very quick um to the codebase. We took

## 23020:00 - 23040:00

the approach of hey instead of having

## 23040:00 - 23070:00

this readonly system where you tag

## 23070:00 - 23090:00

everything what happens if you could

## 23090:00 - 23120:00

make changes very quickly and that's why

## 23120:00 - 23145:00

like at the time we we were kind of the

## 23145:00 - 23175:00

first to do that now if you were to ask

## 23175:00 - 23210:00

like is that a very obvious decision now

## 23210:00 - 23235:00

I think it's very obvious now it looks

## 23235:00 - 23260:00

very obvious and this is where like one

## 23260:00 - 23280:00

of the things that I think is is true

## 23280:00 - 23305:00

for any startup is you have to keep

## 23305:00 - 23340:00

proving yourself right like every single

## 23340:00 - 23365:00

insight that we have is a depreciating

## 23365:00 - 23405:00

insight it is a very very depreciating

## 23405:00 - 23435:00

insight like technology the reason why

## 23435:00 - 23470:00

companies win um at any given point is

## 23470:00 - 23495:00

not like they had a tech they had a tech

## 23495:00 - 23510:00

insight

## 23510:00 - 23555:00

like one year ago, right? Actually, if a

## 23555:00 - 23585:00

company wins, um other than the fact

## 23585:00 - 23615:00

that they have, you know, a monopoly, uh

## 23615:00 - 23650:00

you know, it's it's a it's actually like

## 23650:00 - 23690:00

a compounding tech advantage that keeps

## 23690:00 - 23720:00

sort of existing over and over again.

## 23720:00 - 23740:00

And I think the example of this that I

## 23740:00 - 23780:00

find most most exciting is you look at a

## 23780:00 - 23810:00

company like Nvidia. If Nvidia doesn't

## 23810:00 - 23850:00

innovate in the next two years, AMD will

## 23850:00 - 23895:00

be on their case, right? And Nvidia will

## 23895:00 - 23940:00

not be able to make 60 70% gross margins

## 23940:00 - 23965:00

at that point, right? um even though

## 23965:00 - 23990:00

it's like one of the largest companies

## 23990:00 - 24035:00

in existence uh right now by basically

## 24035:00 - 24065:00

having good insights to start with

## 24065:00 - 24090:00

you're able to learn from the market and

## 24090:00 - 24115:00

maybe compound that advantage with time

## 24115:00 - 24155:00

and that's the only thing that that is

## 24155:00 - 24180:00

uh that could be persistent. It sounds

## 24180:00 - 24210:00

like a moat is uh you know we think of

## 24210:00 - 24245:00

it as a noun but it's actually a verb.

## 24245:00 - 24270:00

Yeah. Something that could change with

## 24270:00 - 24300:00

time right I also think for us and I

## 24300:00 - 24325:00

tell the company this if we're not

## 24325:00 - 24360:00

continuing to have insights and that's

## 24360:00 - 24385:00

why I'm completely okay with a lot of

## 24385:00 - 24420:00

our insights being wrong. um if we don't

## 24420:00 - 24440:00

continually have insights that we are

## 24440:00 - 24480:00

executing on we are just slowly dying um

## 24480:00 - 24510:00

that's like what's actually happening I

## 24510:00 - 24555:00

think the interesting thing is that is

## 24555:00 - 24585:00

easier now looking back and connecting

## 24585:00 - 24620:00

the dots on your journey how a lot of

## 24620:00 - 24660:00

these technology bets you took actually

## 24660:00 - 24700:00

did end up compounding what windsurf

## 24700:00 - 24730:00

ended up becoming right like it was

## 24730:00 - 24765:00

happen stance that you being really good

## 24765:00 - 24810:00

at GPU deployment VMware optimization

## 24810:00 - 24835:00

ended up being the thing to be really

## 24835:00 - 24865:00

good of you at being blazingly fast

## 24865:00 - 24895:00

autocomplete because it's faster than

## 24895:00 - 24920:00

other products Right. So that kind of

## 24920:00 - 24960:00

compounded there. There's the aspect of

## 24960:00 - 24990:00

you building all these uh plugins for

## 24990:00 - 25040:00

enterprises and being so good at reading

## 25040:00 - 25075:00

large code bases and you did something

## 25075:00 - 25105:00

that was contrarian. There was a lot of

## 25105:00 - 25140:00

products and we work with OC companies.

## 25140:00 - 25210:00

A lot of uh codegen tools use uh vector

## 25210:00 - 25235:00

databases because we work with a lot of

## 25235:00 - 25260:00

companies and that's was the standard

## 25260:00 - 25285:00

approach how a lot of folks were

## 25285:00 - 25310:00

building. But you guys did something

## 25310:00 - 25350:00

very different, right? Yeah. So, one of

## 25350:00 - 25380:00

the things that sort of uh I think got

## 25380:00 - 25420:00

really popular is this term rag got very

## 25420:00 - 25455:00

popular. You weren't anti-rag. Yeah. I

## 25455:00 - 25490:00

don't know if we're anti anti-rag. Rag

## 25490:00 - 25510:00

obviously makes sense. You do want to

## 25510:00 - 25530:00

retrieve some stuff and based on the

## 25530:00 - 25550:00

retrieval you want to generate some

## 25550:00 - 25575:00

stuff. So, I guess the idea is is

## 25575:00 - 25600:00

correct that you know everything is

## 25600:00 - 25630:00

retrieval augmented generation. But I

## 25630:00 - 25665:00

think what people got maybe a little too

## 25665:00 - 25700:00

opinionated about was like the way rag

## 25700:00 - 25725:00

is implemented. It has to be a vector

## 25725:00 - 25750:00

database that you go out and search. I

## 25750:00 - 25780:00

think a vector database is a tool in the

## 25780:00 - 25800:00

toolkit. Right? If you were to think

## 25800:00 - 25830:00

about what users ultimately want, they

## 25830:00 - 25865:00

want great answers and they want uh

## 25865:00 - 25895:00

great agents. That's what they actually

## 25895:00 - 25920:00

want. And how do you end up doing that?

## 25920:00 - 25945:00

You need to make sure that what's in the

## 25945:00 - 25980:00

context is as relevant as possible. So

## 25980:00 - 26005:00

what we ended up doing is having a

## 26005:00 - 26050:00

series of systems that enable us to pack

## 26050:00 - 26075:00

the context with the most relevant

## 26075:00 - 26105:00

snippets of code. And the way we

## 26105:00 - 26125:00

ultimately did that was it was a

## 26125:00 - 26160:00

combination of keyword search, rag,

## 26160:00 - 26195:00

abstract syntax tree parsing and then on

## 26195:00 - 26220:00

top of that using as you mentioned all

## 26220:00 - 26250:00

the GPU infrastructure we have to take

## 26250:00 - 26285:00

large chunks of the codebase and in real

## 26285:00 - 26320:00

time rank it right as the query is

## 26320:00 - 26350:00

coming in right and we found that that

## 26350:00 - 26390:00

is like the best way for us to find the

## 26390:00 - 26430:00

best context for the user. And the kind

## 26430:00 - 26460:00

of the motivation for this is because

## 26460:00 - 26480:00

people have kind of weird questions.

## 26480:00 - 26505:00

They might have a question for a large

## 26505:00 - 26560:00

codebase of upgrade all versions of of

## 26560:00 - 26605:00

uh of this API to this API. And if

## 26605:00 - 26630:00

embedding search only finds five of

## 26630:00 - 26660:00

them, it's not of the 10, it's not a

## 26660:00 - 26700:00

very useful a useful feature at that

## 26700:00 - 26725:00

point. So we needed to make sure the

## 26725:00 - 26750:00

precision recall was as high as

## 26750:00 - 26780:00

possible, which meant that we used a

## 26780:00 - 26800:00

series of technologies to actually get

## 26800:00 - 26830:00

to the get to the the best solution.

## 26830:00 - 26855:00

There's a bit of a thing going on with a

## 26855:00 - 26895:00

lot of AI startups getting built taking

## 26895:00 - 26935:00

too much of a intellectual shortcut with

## 26935:00 - 26975:00

what's what works for the problem domain

## 26975:00 - 27010:00

space but you took it from first

## 27010:00 - 27040:00

principle right so you build like a way

## 27040:00 - 27095:00

more complex system that did a parson

## 27095:00 - 27140:00

sing all this stuff which is like cool

## 27140:00 - 27165:00

yeah I think maybe one of the things

## 27165:00 - 27200:00

that I that is potentially interesting

## 27200:00 - 27245:00

to discuss there is is uh we started off

## 27245:00 - 27260:00

a lot of the companies started off

## 27260:00 - 27290:00

working on autonomous vehicles and the

## 27290:00 - 27310:00

reason why that's kind of important is

## 27310:00 - 27340:00

these are systems where you can't just

## 27340:00 - 27370:00

yolo these systems, which is to say you

## 27370:00 - 27390:00

build the software and then you kind of

## 27390:00 - 27415:00

like let it run. You need really good

## 27415:00 - 27450:00

evaluation. I think at the company we

## 27450:00 - 27475:00

don't strive for complexity. We strive

## 27475:00 - 27505:00

for what works. Uh and then the question

## 27505:00 - 27530:00

then is like why is the system so much

## 27530:00 - 27555:00

more complex now? It was because we

## 27555:00 - 27580:00

built really good evaluation systems.

## 27580:00 - 27610:00

Oh, interesting. How do the evals work?

## 27610:00 - 27635:00

Yeah, so the evals for code are actually

## 27635:00 - 27665:00

really cool. Uh basically the idea is

## 27665:00 - 27690:00

code you can leverage a property of code

## 27690:00 - 27740:00

which it can be run, right? uh and uh we

## 27740:00 - 27780:00

not only have real-time user data, we

## 27780:00 - 27810:00

can put that aside for now, but we can

## 27810:00 - 27850:00

take a lot of open source projects and

## 27850:00 - 27885:00

find I guess commits in these open

## 27885:00 - 27915:00

source projects uh with tests attached

## 27915:00 - 27955:00

to them. So you can imagine a lot of

## 27955:00 - 27980:00

cool things we can do based on that. You

## 27980:00 - 28025:00

can take the intent of a commit, delete

## 28025:00 - 28050:00

all the code that is not the unit test,

## 28050:00 - 28085:00

right? And then you can see, hey, are

## 28085:00 - 28110:00

you able to retrieve the parts where the

## 28110:00 - 28140:00

change needs to get made? Do you have a

## 28140:00 - 28165:00

good highle intent to make those

## 28165:00 - 28190:00

changes? And then after making the

## 28190:00 - 28220:00

changes, does the test pass? you can do

## 28220:00 - 28255:00

that task, you can mask the task. And by

## 28255:00 - 28300:00

masking the task, it's it's more like

## 28300:00 - 28325:00

more like the the Google task. And what

## 28325:00 - 28355:00

I mean by the Google task is it's trying

## 28355:00 - 28385:00

to predict your intent, which is to say,

## 28385:00 - 28410:00

let's say you only put in a third of the

## 28410:00 - 28445:00

change, but you don't get the intent.

## 28445:00 - 28470:00

Can you then fill out the rest to make

## 28470:00 - 28500:00

the test pass? So there's so many ways

## 28500:00 - 28530:00

you can slice this. And each of them,

## 28530:00 - 28550:00

you can break it down into so much

## 28550:00 - 28575:00

granularity. You can be like, what is my

## 28575:00 - 28610:00

retrieval accuracy? What is my intent

## 28610:00 - 28650:00

accuracy? What is my um what is my

## 28650:00 - 28675:00

passing? What is my test passing

## 28675:00 - 28705:00

accuracy? You can do that. And then now

## 28705:00 - 28730:00

you have a hill to climb. And I think

## 28730:00 - 28755:00

that's actually important before you add

## 28755:00 - 28795:00

a lot of complexity for any of these AI

## 28795:00 - 28825:00

apps. I think you need to like make a

## 28825:00 - 28855:00

rigorous hill that you can actually

## 28855:00 - 28880:00

climb, right? Otherwise, you're just

## 28880:00 - 28905:00

shooting in the dark, right? Why would

## 28905:00 - 28940:00

we add the ASG parsing if it's

## 28940:00 - 28965:00

unnecessary? Actually, it's awesome if

## 28965:00 - 28995:00

it was unnecessary. Um, right? I don't

## 28995:00 - 29020:00

want to add a lot of complex stuff to

## 29020:00 - 29045:00

our code. In fact, I want the I want the

## 29045:00 - 29085:00

simplest code that ends up doing the uh

## 29085:00 - 29125:00

having the most impact. So, the eval

## 29125:00 - 29160:00

really really critical for us to make a

## 29160:00 - 29185:00

lot of these investments at the company.

## 29185:00 - 29210:00

How much of the development that you do

## 29210:00 - 29245:00

is like basically driven by improving

## 29245:00 - 29275:00

the scores on the eval versus like

## 29275:00 - 29310:00

basically vibes based like you guys are

## 29310:00 - 29335:00

all using winerve yourself you're

## 29335:00 - 29365:00

getting feedback from users all the time

## 29365:00 - 29385:00

and then you have just like a sense that

## 29385:00 - 29405:00

this thing is going to work better and

## 29405:00 - 29435:00

then the eval are just sort of like a

## 29435:00 - 29460:00

check that you didn't screw up something

## 29460:00 - 29485:00

else it's a little bit of both but

## 29485:00 - 29515:00

obviously for some kinds of systems I

## 29515:00 - 29540:00

think eval are more important than vi

## 29540:00 - 29570:00

but like more easy than vibes uh just

## 29570:00 - 29600:00

because for the system that basically

## 29600:00 - 29625:00

takes a large chunk of the code chunks

## 29625:00 - 29650:00

it up and passes it to hundreds of GPUs

## 29650:00 - 29685:00

in parallel giving you a result in one

## 29685:00 - 29720:00

It's very hard to have an intuition of

## 29720:00 - 29750:00

like is this way better because that's a

## 29750:00 - 29780:00

very complex sort of retrieval question.

## 29780:00 - 29820:00

Um but on the other hand there are much

## 29820:00 - 29840:00

easier things that from a vibe

## 29840:00 - 29865:00

perspective are valuable. What if we

## 29865:00 - 29890:00

looked at the open files in a codebase?

## 29890:00 - 29925:00

This is actually harder thing to eval

## 29925:00 - 29960:00

because when you're evaling you don't

## 29960:00 - 29985:00

know what the user is doing in real

## 29985:00 - 30005:00

time. This is one of those cases where

## 30005:00 - 30045:00

having a product and market helps us a

## 30045:00 - 30075:00

lot right and we're able to take a lot

## 30075:00 - 30105:00

of user data on how people use the

## 30105:00 - 30130:00

product to actually actively make the

## 30130:00 - 30155:00

product much better. So that's maybe

## 30155:00 - 30175:00

starts with vibes and then after that

## 30175:00 - 30220:00

you can build evo right um so it's it's

## 30220:00 - 30250:00

a little bit of both basically I think a

## 30250:00 - 30280:00

lot of uh there's been a lot of chatter

## 30280:00 - 30315:00

on the internet about vibes code is only

## 30315:00 - 30370:00

for toy apps windsurf is actually being

## 30370:00 - 30405:00

used for real production large code

## 30405:00 - 30440:00

bases can you tell us about how the

## 30440:00 - 30480:00

power users use it for like more

## 30480:00 - 30510:00

hardcore engineering so this is an

## 30510:00 - 30530:00

interesting thing where a lot of us at

## 30530:00 - 30560:00

the company I I'm not saying that this

## 30560:00 - 30595:00

is this is common didn't get a

## 30595:00 - 30640:00

tremendous value from chatbt in the way

## 30640:00 - 30675:00

that probably a lot of the rest of the

## 30675:00 - 30695:00

world did. Um, and that's not because

## 30695:00 - 30720:00

Chajbt is not a useful product. I think

## 30720:00 - 30755:00

Chajbt is an incredibly useful product.

## 30755:00 - 30785:00

It's actually because a lot of them had

## 30785:00 - 30820:00

already used things like like Stack

## 30820:00 - 30845:00

Overflow at the time. And Stack Overflow

## 30845:00 - 30880:00

is a worse version than Chad GBT for the

## 30880:00 - 30900:00

kinds of questions you want, but that

## 30900:00 - 30925:00

was just a thing that they already knew

## 30925:00 - 30955:00

how to use, right? Um, and so they were

## 30955:00 - 30985:00

able to get away with not using or

## 30985:00 - 31020:00

relying on chat nearly as much. But

## 31020:00 - 31045:00

basically what happened is very recently

## 31045:00 - 31070:00

with agents, the agent is making larger

## 31070:00 - 31110:00

and larger scale changes with time. And

## 31110:00 - 31135:00

I think what developers now at our

## 31135:00 - 31165:00

company do is they have felt the hills

## 31165:00 - 31195:00

and valleys of this product which is to

## 31195:00 - 31225:00

say if you don't provide enough intent.

## 31225:00 - 31245:00

It actually goes out and changes way

## 31245:00 - 31275:00

more of the code than you actually need.

## 31275:00 - 31300:00

Right? Um and this is like a real

## 31300:00 - 31325:00

problem with with the with the tool

## 31325:00 - 31350:00

right now. But they understand the hills

## 31350:00 - 31380:00

and valleys and now the very first time

## 31380:00 - 31405:00

they have a task. They are putting it

## 31405:00 - 31435:00

into windsurf. They're not their first

## 31435:00 - 31465:00

thing is not to actually go out and type

## 31465:00 - 31490:00

in in the actual editor. It's to

## 31490:00 - 31520:00

actually put the intent and actually uh

## 31520:00 - 31560:00

and actually make those changes. Um and

## 31560:00 - 31575:00

uh they're doing kind of very

## 31575:00 - 31600:00

interesting things now like deploying

## 31600:00 - 31640:00

our our software uh to our servers

## 31640:00 - 31660:00

actually now gets done with the

## 31660:00 - 31695:00

workflows that are entirely built um

## 31695:00 - 31730:00

inside Windsurf. Uh so just a lot of

## 31730:00 - 31755:00

boilerplate and repetitive tasks have

## 31755:00 - 31780:00

been completely uh like sort of

## 31780:00 - 31810:00

eliminated inside our company. But the

## 31810:00 - 31840:00

reason why this is possible is kind of

## 31840:00 - 31865:00

because we're able to operate over a

## 31865:00 - 31885:00

codebase that has many millions of lines

## 31885:00 - 31925:00

of code uh really really effectively. So

## 31925:00 - 31960:00

if you were to give some tips to the

## 31960:00 - 32005:00

audience, how should a user that uses

## 32005:00 - 32055:00

windsurf properly provide this intent so

## 32055:00 - 32080:00

that the changes are more surgical?

## 32080:00 - 32115:00

Because what you're saying with the

## 32115:00 - 32155:00

agents creating all these broad changes,

## 32155:00 - 32185:00

I've seen that happen. But how how do

## 32185:00 - 32230:00

you get those precise changes? What do

## 32230:00 - 32250:00

you do? How do you how do you feed the

## 32250:00 - 32275:00

system? How do you become a shouted it

## 32275:00 - 32330:00

with all caps, right? Yeah. Um, no. So,

## 32330:00 - 32350:00

I I think this is one of those things

## 32350:00 - 32405:00

where uh I think you kind of need to

## 32405:00 - 32430:00

need to have a little bit of faith in

## 32430:00 - 32460:00

the system and let it kind of mess up a

## 32460:00 - 32490:00

little bit. Uh, which is which is kind

## 32490:00 - 32520:00

of scary because I think a lot of people

## 32520:00 - 32545:00

for the most part they will write off

## 32545:00 - 32570:00

these tools really quickly. Obviously,

## 32570:00 - 32595:00

no one at our company would ride off the

## 32595:00 - 32615:00

tool because they're building the tools

## 32615:00 - 32635:00

themselves. I think people's

## 32635:00 - 32665:00

expectations are very high and maybe

## 32665:00 - 32695:00

that's like the the main piece of

## 32695:00 - 32720:00

feedback I'd give which is that you know

## 32720:00 - 32745:00

our product actually for these larger

## 32745:00 - 32780:00

and larger changes it might make 90% of

## 32780:00 - 32810:00

the changes correctly but if 10% is

## 32810:00 - 32840:00

wrong people will just write off the

## 32840:00 - 32880:00

entire tool and I think at that point

## 32880:00 - 32905:00

actually probably the right thing to do

## 32905:00 - 32935:00

is either revert the change we have an

## 32935:00 - 32965:00

ability to actually revert the change or

## 32965:00 - 33000:00

just keep going and see where see where

## 33000:00 - 33035:00

it ultimately can go uh and and maybe

## 33035:00 - 33075:00

the the most important aspect is commit

## 33075:00 - 33100:00

your code like as frequently as possible

## 33100:00 - 33130:00

I think that maybe that's like the big

## 33130:00 - 33165:00

big sort of uh tip there which is that

## 33165:00 - 33190:00

uh you know you don't want to get in a

## 33190:00 - 33215:00

situation where you've made 20 changes

## 33215:00 - 33240:00

and on top of that made some changes

## 33240:00 - 33270:00

yourselves and you can't like revert it

## 33270:00 - 33300:00

and then you get like very frustrated at

## 33300:00 - 33320:00

the end of it and one thing I've

## 33320:00 - 33355:00

wondered like in that vein is whether we

## 33355:00 - 33410:00

need to change the way git works with

## 33410:00 - 33430:00

this AI

## 33430:00 - 33475:00

coding paradigm have you thought at all

## 33475:00 - 33515:00

about whether doing git commit all the

## 33515:00 - 33550:00

time is the right move or whether there

## 33550:00 - 33575:00

needs to be like a deeper infrastructure

## 33575:00 - 33615:00

change yeah I think we have so you One

## 33615:00 - 33645:00

of the things that we always think of is

## 33645:00 - 33670:00

in the future you're going to have many

## 33670:00 - 33700:00

many agents running in parallel on your

## 33700:00 - 33740:00

codebase. That has some some trade-offs,

## 33740:00 - 33760:00

right? If you have two agents that kind

## 33760:00 - 33790:00

of modify the same piece of code at the

## 33790:00 - 33805:00

same time, it's hard to actually know

## 33805:00 - 33825:00

what's going on. That's another thing is

## 33825:00 - 33845:00

that like it's hard to have multiple

## 33845:00 - 33890:00

branches checked out at the same time

## 33890:00 - 33920:00

with different agents working on them

## 33920:00 - 33950:00

independently. All the merge conflicts.

## 33950:00 - 33980:00

Oh god. Yeah, there's a lot of But hey,

## 33980:00 - 34000:00

like you know, that's how that's how

## 34000:00 - 34025:00

real software development works too.

## 34025:00 - 34045:00

When you have a lot of engineers that

## 34045:00 - 34065:00

operate on a codebase, they're all like

## 34065:00 - 34090:00

kind of mcking around with the codebase

## 34090:00 - 34120:00

at the same time. So that's not a very

## 34120:00 - 34145:00

unique thing. I think git is a great

## 34145:00 - 34165:00

tool. I think it's maybe a question of

## 34165:00 - 34210:00

like how how can you skin git to work in

## 34210:00 - 34245:00

a way that is that is uh that works for

## 34245:00 - 34270:00

this for this product surface. An

## 34270:00 - 34290:00

example is git has these things called

## 34290:00 - 34315:00

work trees which is like you can have

## 34315:00 - 34340:00

many work trees and versions of the

## 34340:00 - 34375:00

repository all in your all in the same

## 34375:00 - 34415:00

directory. Um and and you know perhaps

## 34415:00 - 34440:00

you can have many of these agents

## 34440:00 - 34470:00

working on different work trees. Um or

## 34470:00 - 34500:00

instead of exposing the branch concept

## 34500:00 - 34520:00

to you, you actually can maintain a

## 34520:00 - 34555:00

branch yourself that you can apply to

## 34555:00 - 34585:00

the to the main branch of the user. um

## 34585:00 - 34610:00

kind of repeatedly one of the things

## 34610:00 - 34635:00

that we think about at the company in

## 34635:00 - 34660:00

terms of why we think our agent is

## 34660:00 - 34685:00

really good is like we try to have a

## 34685:00 - 34710:00

unified timeline on everything that

## 34710:00 - 34735:00

happened. The unified timeline is not

## 34735:00 - 34770:00

just what the developer did but actually

## 34770:00 - 34790:00

what the developer did in addition to

## 34790:00 - 34820:00

what the agent did. So actually our

## 34820:00 - 34850:00

product if you end up doing things in

## 34850:00 - 34875:00

the editor if you end up doing things in

## 34875:00 - 34905:00

the terminal right all of those things

## 34905:00 - 34940:00

are captured and the intent is is

## 34940:00 - 34970:00

actually kind of tracked in such a way

## 34970:00 - 35005:00

where when you use the AI the AI knows

## 35005:00 - 35040:00

right in that situation. So, in some

## 35040:00 - 35065:00

ways, we'd like this thing where the

## 35065:00 - 35090:00

agent is not operating on a completely

## 35090:00 - 35110:00

different timeline, but it's like

## 35110:00 - 35130:00

something that's kind of getting merged

## 35130:00 - 35160:00

in um you know, at a fairly high

## 35160:00 - 35190:00

cadence. Um so, I think this is like an

## 35190:00 - 35210:00

open problem. I don't I don't think we

## 35210:00 - 35240:00

have like the exact right answer for

## 35240:00 - 35265:00

this. What are other things that you

## 35265:00 - 35295:00

envision changing about Winterf in the

## 35295:00 - 35320:00

future? How how is it going to evolve?

## 35320:00 - 35340:00

There's probably a lot of people that

## 35340:00 - 35365:00

think the vibe coding is kind of a kind

## 35365:00 - 35390:00

of a fad, but I think that's going to

## 35390:00 - 35420:00

get more and more capable with time. I

## 35420:00 - 35445:00

think, you know, whenever I hear someone

## 35445:00 - 35465:00

saying, "Hey, this is not going to work

## 35465:00 - 35495:00

for this complex use case." It's it's

## 35495:00 - 35520:00

like it feels like a lite saying

## 35520:00 - 35540:00

something, right? It's like if you look

## 35540:00 - 35575:00

at the way these these uh these AIs have

## 35575:00 - 35605:00

gotten better sort of year over year.

## 35605:00 - 35640:00

It's it's actually it's astonishing.

## 35640:00 - 35670:00

Like I'll give you an example of of

## 35670:00 - 35695:00

something that I held like kind of near

## 35695:00 - 35720:00

and dear to my heart which is you know

## 35720:00 - 35750:00

there's this math Olympiad called Amy

## 35750:00 - 35785:00

and I used to do that uh do that in in

## 35785:00 - 35825:00

high school. Um and you know I was very

## 35825:00 - 35850:00

excited about about how well I would do.

## 35850:00 - 35885:00

My high score was somewhere close to 14.

## 35885:00 - 35925:00

And uh and uh that's a very high score.

## 35925:00 - 35965:00

Yeah. But but the but the crazy thing is

## 35965:00 - 35985:00

that was one of those things that I

## 35985:00 - 36010:00

thought oh wow like the AI systems

## 36010:00 - 36030:00

they're they're not going to get

## 36030:00 - 36075:00

anywhere near um as good and beginning

## 36075:00 - 36100:00

of the year last year it was probably

## 36100:00 - 36140:00

like well under five maybe um and now

## 36140:00 - 36170:00

they're you know the average that open

## 36170:00 - 36200:00

out is like it's getting 14 and a half

## 36200:00 - 36250:00

to 15 right uh for O4 mini uh so it's

## 36250:00 - 36285:00

almost like you have to keep projecting

## 36285:00 - 36315:00

this out right it's going to get crazy

## 36315:00 - 36345:00

and basically every part of the software

## 36345:00 - 36370:00

development life cycle whether it be

## 36370:00 - 36400:00

writing code reviewing code testing code

## 36400:00 - 36435:00

debugging code designing code AI is

## 36435:00 - 36460:00

going to be adding 10 times the amount

## 36460:00 - 36495:00

of leverage very shortly. It's going to

## 36495:00 - 36525:00

happen like much much more quickly than

## 36525:00 - 36555:00

people imagine. Going back to your

## 36555:00 - 36580:00

current engineering team, I'm curious

## 36580:00 - 36615:00

like if they have all this time freed up

## 36615:00 - 36645:00

from you know not having to deal with

## 36645:00 - 36685:00

like version upgrades and you know

## 36685:00 - 36715:00

boring boiler plate stuff like what do

## 36715:00 - 36745:00

they spend the extra time on? One of the

## 36745:00 - 36765:00

things about our company and probably

## 36765:00 - 36790:00

every startup uh that that is building

## 36790:00 - 36825:00

in the space is the ceiling of where the

## 36825:00 - 36860:00

technology can go is so high. It's so

## 36860:00 - 36890:00

high. So it's it's actually that you

## 36890:00 - 36920:00

know if developers can spend less time

## 36920:00 - 36945:00

doing boiler plate they can spend more

## 36945:00 - 36980:00

time testing hypothesis for things that

## 36980:00 - 37015:00

they're not sure work right in some ways

## 37015:00 - 37045:00

engineering becomes a lot more of like a

## 37045:00 - 37085:00

research kind of uh kind of culture

## 37085:00 - 37110:00

right where you're testing hypothesis

## 37110:00 - 37145:00

really really quickly um and that has

## 37145:00 - 37170:00

some high cycle time attached to it

## 37170:00 - 37190:00

right you need to go out and implement

## 37190:00 - 37210:00

things you need to build the evaluation

## 37210:00 - 37235:00

you need to test it out with our users

## 37235:00 - 37255:00

but that's like the things that actually

## 37255:00 - 37285:00

make the product way better does that

## 37285:00 - 37305:00

mean you're going to hire a different

## 37305:00 - 37335:00

type of engineer going forward like

## 37335:00 - 37355:00

you're looking for different things

## 37355:00 - 37390:00

Yeah, I think for engineers that we

## 37390:00 - 37420:00

hire, we want to look for people with

## 37420:00 - 37450:00

really high agency that are willing to

## 37450:00 - 37490:00

be wrong uh and bold. But, you know,

## 37490:00 - 37515:00

weirdly, I don't know if that's that's

## 37515:00 - 37545:00

changed for a startup, right? Startup

## 37545:00 - 37580:00

should never be hiring people that uh

## 37580:00 - 37605:00

the reason why they're joining a company

## 37605:00 - 37635:00

is to to very quickly write like

## 37635:00 - 37665:00

boilerplate code, right? Because in some

## 37665:00 - 37685:00

sense, and I don't want like, you know,

## 37685:00 - 37710:00

this is not the goal, but a startup can

## 37710:00 - 37745:00

succeed even if they have extremely kind

## 37745:00 - 37785:00

of ugly code, right? That's not usually

## 37785:00 - 37805:00

the reason why a startup fails. Sounds

## 37805:00 - 37840:00

like my startup. Yeah. Yeah. Exactly.

## 37840:00 - 37855:00

That's not usually the reason why

## 37855:00 - 37880:00

startup fails. The reason why a startup

## 37880:00 - 37905:00

fails is they didn't build a product

## 37905:00 - 37935:00

that was differentially good uh for

## 37935:00 - 37970:00

their users. That's why they ultimately

## 37970:00 - 38010:00

failed. This is all true, but also like

## 38010:00 - 38040:00

in reality, you always need some sort of

## 38040:00 - 38075:00

like workh horses to just kind of get

## 38075:00 - 38095:00

certain things done. I feel like in the

## 38095:00 - 38120:00

old days this was like building Android

## 38120:00 - 38165:00

apps. Um it's like you hired someone to

## 38165:00 - 38190:00

do it because there were very few people

## 38190:00 - 38210:00

who would just be willing to do it.

## 38210:00 - 38255:00

Yeah. Like maybe in your vision for

## 38255:00 - 38285:00

engineering like you don't need those

## 38285:00 - 38310:00

like that's not actually a useful skill

## 38310:00 - 38335:00

to have in an organization anymore

## 38335:00 - 38355:00

because the AI is just like your

## 38355:00 - 38390:00

infinite workhorse. Is that fair? Yeah.

## 38390:00 - 38425:00

Maybe the the the sort of aspects of

## 38425:00 - 38455:00

software that are really niche that are

## 38455:00 - 38485:00

undesirable for a lot of people to do

## 38485:00 - 38520:00

except a handful of people. Those things

## 38520:00 - 38545:00

kind of get democratized a lot more

## 38545:00 - 38570:00

unless that has like a lot of depth

## 38570:00 - 38600:00

attached to it, right? At least for the

## 38600:00 - 38625:00

time being. Um, yeah, if something is

## 38625:00 - 38655:00

like, hey, like, you know, we need to

## 38655:00 - 38685:00

change a system to use a new version.

## 38685:00 - 38715:00

Um, and there was someone that deeply

## 38715:00 - 38735:00

always got in the weeds with version

## 38735:00 - 38755:00

changes. I don't think you have people

## 38755:00 - 38785:00

that are just focused on that, right,

## 38785:00 - 38810:00

inside companies. How about how you

## 38810:00 - 38840:00

interview people? Yeah, I think I think

## 38840:00 - 38870:00

we have a fairly rigorous and high

## 38870:00 - 38905:00

technical bar and that has a that's a

## 38905:00 - 38930:00

combination of we give interviews that

## 38930:00 - 38955:00

actually allow people to use the AI to

## 38955:00 - 38980:00

kind of solve a problem because we want

## 38980:00 - 39020:00

to validate if people like kind of hate

## 39020:00 - 39045:00

these tools or not. there are still some

## 39045:00 - 39075:00

developers that do and obviously if you

## 39075:00 - 39100:00

do we're probably the wrong company to

## 39100:00 - 39125:00

kind of work at but also at the same

## 39125:00 - 39165:00

time we do have sort of interviews in

## 39165:00 - 39220:00

person where uh kind of on site where we

## 39220:00 - 39245:00

don't give them the AI and we want to

## 39245:00 - 39270:00

see them think right it would be a bad

## 39270:00 - 39290:00

thing if ultimately when someone needs

## 39290:00 - 39320:00

to write a nested for loop they need to

## 39320:00 - 39365:00

go to chatbt right and and I'm not like

## 39365:00 - 39400:00

that's fundamentally because because uh

## 39400:00 - 39440:00

it just it just feels like that is a

## 39440:00 - 39470:00

good proxy for problem solving skills

## 39470:00 - 39490:00

and I think problem solving skills are

## 39490:00 - 39520:00

just at a high level still should go at

## 39520:00 - 39545:00

a premium that That is the valuable

## 39545:00 - 39570:00

skill that humans have. Yeah. A

## 39570:00 - 39600:00

challenge that a lot of companies we've

## 39600:00 - 39635:00

talked to have had that that we've even

## 39635:00 - 39675:00

had ourselves is that Windsurf has

## 39675:00 - 39710:00

gotten so good that if you give people

## 39710:00 - 39745:00

windsurf it's difficult to even come up

## 39745:00 - 39780:00

with an interview question that Windsurf

## 39780:00 - 39820:00

can't just oneshot where you know anyone

## 39820:00 - 39840:00

can do it because you literally just

## 39840:00 - 39860:00

copy and paste the question into

## 39860:00 - 39900:00

Windsorf and hit enter and so you're not

## 39900:00 - 39915:00

really evaluating anything at that

## 39915:00 - 39945:00

point. So I actually think that's true

## 39945:00 - 39980:00

and it's it's it's you're totally right.

## 39980:00 - 40020:00

There's very few problems now that

## 40020:00 - 40055:00

something like an O4 Mini is not able to

## 40055:00 - 40090:00

solve now. Um, right? I mean, if you

## 40090:00 - 40110:00

look at competitive programming, it's

## 40110:00 - 40140:00

just it's just in a league of its own

## 40140:00 - 40160:00

already at this point. The crazy thing

## 40160:00 - 40195:00

is interviews by nature are going to be

## 40195:00 - 40225:00

kind of isolated problems, right?

## 40225:00 - 40250:00

They're by nature because if the problem

## 40250:00 - 40290:00

actually required so much understanding

## 40290:00 - 40315:00

to do, you wouldn't be able to explain

## 40315:00 - 40340:00

the problem. So, that's like perfect for

## 40340:00 - 40370:00

the LMS where you give them an isolated

## 40370:00 - 40400:00

problem where you can test and run code

## 40400:00 - 40425:00

extremely quickly. So, yeah, you're

## 40425:00 - 40455:00

totally right. Like I think if you tell

## 40455:00 - 40485:00

if you only have algorithmic interviews

## 40485:00 - 40515:00

and you let people use the

## 40515:00 - 40545:00

AI, I don't know, you're not really

## 40545:00 - 40570:00

testing anything at that point. Does

## 40570:00 - 40595:00

that mean that you've gone away from

## 40595:00 - 40630:00

just algorithmic questions and you ask

## 40630:00 - 40655:00

different like much harder questions

## 40655:00 - 40680:00

that are actually well suited to being

## 40680:00 - 40720:00

able being able to use an AI? Yeah, we

## 40720:00 - 40755:00

we have questions obviously where that

## 40755:00 - 40790:00

are that are both system designy plus

## 40790:00 - 40830:00

algorithms algorithms related. But these

## 40830:00 - 40850:00

are questions that are fairly

## 40850:00 - 40885:00

open-ended, right? Uh there may not be a

## 40885:00 - 40910:00

correct answer. there are there are

## 40910:00 - 40935:00

trade-offs that you can ultimately make

## 40935:00 - 40960:00

and I think what we want to do is just

## 40960:00 - 40990:00

see how people think right given

## 40990:00 - 41015:00

different trade-offs and different

## 41015:00 - 41050:00

constraints right uh and and we're

## 41050:00 - 41075:00

trying to validate for like intellectual

## 41075:00 - 41100:00

curiosity right and if someone

## 41100:00 - 41140:00

ultimately says I don't know why why why

## 41140:00 - 41170:00

that's totally fine as long as like

## 41170:00 - 41215:00

they've gone to a depth that we feel um

## 41215:00 - 41250:00

kind of shows you kind of interest um

## 41250:00 - 41275:00

interest and like good problem solving

## 41275:00 - 41300:00

skills if that makes sense like you can

## 41300:00 - 41330:00

tell when someone is curious right and

## 41330:00 - 41355:00

wants to learn things it's like very

## 41355:00 - 41400:00

obvious the next thought after is which

## 41400:00 - 41425:00

might be counterintuitive. You're at the

## 41425:00 - 41455:00

forefront of building all these AI

## 41455:00 - 41505:00

coding tools. It hasn't affected at all

## 41505:00 - 41545:00

your hiring plans. On the contrary, you

## 41545:00 - 41570:00

actually need way more engineers to

## 41570:00 - 41605:00

execute. Tell us more about that. So, I

## 41605:00 - 41640:00

think I think that just boils down to I

## 41640:00 - 41660:00

think the problem has a very high

## 41660:00 - 41690:00

ceiling, right? There's so many more

## 41690:00 - 41715:00

things that we really want to do. The

## 41715:00 - 41735:00

mission of the company is to reduce the

## 41735:00 - 41765:00

time it takes to build technology and

## 41765:00 - 41800:00

apps by 99%. It's going to take a lot of

## 41800:00 - 41840:00

work to go out and do that. Now granted,

## 41840:00 - 41860:00

each person in our company is way more

## 41860:00 - 41895:00

productive than they were a year ago. Uh

## 41895:00 - 41925:00

but I think for us to go out and

## 41925:00 - 41950:00

accomplish that, I think it's, you know,

## 41950:00 - 41990:00

it's a herculan task. We need to start

## 41990:00 - 42025:00

targeting more of the development

## 42025:00 - 42045:00

experience. Right? Right now, we've

## 42045:00 - 42090:00

helped a lot with the code writing

## 42090:00 - 42140:00

process. Um and and maybe the the the

## 42140:00 - 42175:00

navigation of code process, but we have

## 42175:00 - 42210:00

not touched much on the on the design

## 42210:00 - 42245:00

process, on the deploying process, the

## 42245:00 - 42280:00

debugging process is fairly rudimentary

## 42280:00 - 42300:00

right now. There's just so many

## 42300:00 - 42320:00

different pieces. is if I was to look at

## 42320:00 - 42345:00

it like you know if you say you have 100

## 42345:00 - 42380:00

units of time you know we have an axe

## 42380:00 - 42420:00

we've cut off maybe like 40 or 50 in

## 42420:00 - 42445:00

that in that in that time but there's

## 42445:00 - 42475:00

just a lot more snippets that we need to

## 42475:00 - 42500:00

cut out basically at this point it does

## 42500:00 - 42540:00

feel like when I'm using Windsurf like I

## 42540:00 - 42585:00

am often the extremely slow bridge

## 42585:00 - 42610:00

between different pieces of technology

## 42610:00 - 42645:00

copying and pasting data back and forth

## 42645:00 - 42680:00

from my that's probably actually still a

## 42680:00 - 42705:00

large chunk of your time all the pieces

## 42705:00 - 42730:00

have gotten so fast that now it's like

## 42730:00 - 42755:00

the glue between them but like I'm the

## 42755:00 - 42795:00

glue but I'm like much slower

## 42795:00 - 42825:00

can I go off the reservation and ask a

## 42825:00 - 42865:00

weird question. Go for it. Okay. Uh, one

## 42865:00 - 42890:00

of the things that I mean, I think Pete

## 42890:00 - 42925:00

on our team, he just released a great

## 42925:00 - 42960:00

essay about, you know, prompting and you

## 42960:00 - 43000:00

should let users have access to system

## 43000:00 - 43030:00

prompts. The other thing that he came up

## 43030:00 - 43065:00

with that we've been using all at YC

## 43065:00 - 43110:00

internally is a new agent infrastructure

## 43110:00 - 43155:00

that has direct access, read access to

## 43155:00 - 43190:00

our system of record, our Postgress

## 43190:00 - 43235:00

database. And in the process of using

## 43235:00 - 43275:00

this, we're starting to realize like if

## 43275:00 - 43315:00

codegen gets a lot better, which it's,

## 43315:00 - 43350:00

you know, I based on this conversation,

## 43350:00 - 43380:00

I think we can count on that getting

## 43380:00 - 43435:00

like 10x 100x better from here. Uh what

## 43435:00 - 43480:00

if instead of you know building package

## 43480:00 - 43515:00

software, there's like just in time

## 43515:00 - 43550:00

software that the agent basically just

## 43550:00 - 43595:00

builds for you as you need it. Does that

## 43595:00 - 43640:00

change the nature of software and SAS?

## 43640:00 - 43680:00

And you know what happens to all of us

## 43680:00 - 43715:00

in Windsurf? I don't know. I think this

## 43715:00 - 43750:00

notion of just a developer is is

## 43750:00 - 43770:00

probably going to broaden out to what's

## 43770:00 - 43810:00

called a builder and uh I think everyone

## 43810:00 - 43835:00

is going to be a builder and they can

## 43835:00 - 43860:00

decide like you know how deep they want

## 43860:00 - 43895:00

to go and build things. uh maybe maybe

## 43895:00 - 43920:00

our current version of developers can go

## 43920:00 - 43945:00

deep enough that they can build more

## 43945:00 - 43985:00

complex things, right? Um in the in the

## 43985:00 - 44010:00

shorter term, but yeah, I think software

## 44010:00 - 44040:00

is going to be this very very democ

## 44040:00 - 44080:00

democratized thing, right? I I imagine a

## 44080:00 - 44120:00

future in which you know what actually

## 44120:00 - 44160:00

happens when you ask an AI assistant,

## 44160:00 - 44190:00

hey, build me something that like tracks

## 44190:00 - 44225:00

the amount of calories I have. Why would

## 44225:00 - 44265:00

you have a very custom app that goes out

## 44265:00 - 44290:00

and does this? It's probably something

## 44290:00 - 44325:00

that takes like all the inputs from your

## 44325:00 - 44365:00

AR glasses and everything and has a

## 44365:00 - 44385:00

custom piece of software that kind of

## 44385:00 - 44410:00

comes out and like an app that is there

## 44410:00 - 44440:00

and like it has tasks that go and tell

## 44440:00 - 44470:00

you uh you know are you on track with

## 44470:00 - 44500:00

with all the calories you're you're sort

## 44500:00 - 44535:00

of consuming here. Um and I think that's

## 44535:00 - 44565:00

a very very custom piece of software

## 44565:00 - 44590:00

that you have for yourself that you can

## 44590:00 - 44620:00

keep tweaking. I can imagine a future

## 44620:00 - 44645:00

like that where effectively everyone is

## 44645:00 - 44665:00

building but people don't know what

## 44665:00 - 44695:00

they're building as software. They just

## 44695:00 - 44730:00

they're kind of just building uh just

## 44730:00 - 44755:00

capabilities and technology that they

## 44755:00 - 44785:00

have for themselves. Do many people use

## 44785:00 - 44810:00

windsurf who don't know how to write

## 44810:00 - 44840:00

code at all? It's actually a large a

## 44840:00 - 44865:00

large number of our users. Yeah.

## 44865:00 - 44890:00

Interesting. Yeah. How did they end up

## 44890:00 - 44920:00

getting into windsurf? Like did they

## 44920:00 - 44945:00

work at some company where like some

## 44945:00 - 44970:00

programmer showed them how to use it?

## 44970:00 - 45010:00

Like I I I tend to think of windsurf as

## 45010:00 - 45050:00

targeting more like the professional

## 45050:00 - 45085:00

developer market that's like using this

## 45085:00 - 45120:00

as a new superpower versus the like

## 45120:00 - 45150:00

non-technical user market that's doing

## 45150:00 - 45180:00

like what Gary was talking about. We

## 45180:00 - 45205:00

were shocked by this too because we were

## 45205:00 - 45240:00

like, "Hey, our product is an ID, but

## 45240:00 - 45265:00

there's actually a non-trivial chunk of

## 45265:00 - 45290:00

our developers that have never opened

## 45290:00 - 45325:00

the editor up and they just, you know,

## 45325:00 - 45360:00

our agent is called Cascade, right? And

## 45360:00 - 45395:00

uh just live in Cascade. We have browser

## 45395:00 - 45425:00

preview, so they just open up the

## 45425:00 - 45450:00

browser preview. They can click on

## 45450:00 - 45490:00

things and and sort of uh make changes.

## 45490:00 - 45525:00

The benefit is because because we kind

## 45525:00 - 45555:00

of understand the code when they come

## 45555:00 - 45585:00

back to the repository and the code has

## 45585:00 - 45615:00

actually gotten like quite gnarly. we're

## 45615:00 - 45640:00

actually able to pick up from where the

## 45640:00 - 45680:00

developer left off or the the the the

## 45680:00 - 45705:00

kind of builder left off and and keep

## 45705:00 - 45735:00

going from where they were. Um I will

## 45735:00 - 45765:00

say we have not optimized tremendously

## 45765:00 - 45790:00

for that use case. But it's actually

## 45790:00 - 45840:00

kind of crazy how how how much is

## 45840:00 - 45865:00

actually happening there? Do you think

## 45865:00 - 45915:00

in the long term that this ends up being

## 45915:00 - 45960:00

one product that targets like both of

## 45960:00 - 45995:00

these audiences or do you think actually

## 45995:00 - 46055:00

there's like different products for

## 46055:00 - 46080:00

different audiences? There's like a wind

## 46080:00 - 46115:00

surf which is like focused on like

## 46115:00 - 46155:00

serious developers who want to see the

## 46155:00 - 46180:00

code and be in the details and then

## 46180:00 - 46210:00

there's maybe other products for for

## 46210:00 - 46230:00

folks who are totally nontechnical who

## 46230:00 - 46250:00

don't who don't even want to see the

## 46250:00 - 46285:00

code. I don't know what the long term is

## 46285:00 - 46305:00

going to look like. Something tells me

## 46305:00 - 46335:00

it's going to become more unified. But

## 46335:00 - 46355:00

one of the things that I will just say

## 46355:00 - 46385:00

is like as a startup for us even though

## 46385:00 - 46420:00

we do have you know like a a good number

## 46420:00 - 46450:00

of people there's a limit to what we can

## 46450:00 - 46480:00

focus on internally as well. Uh so for

## 46480:00 - 46510:00

us like we're not going to be focused on

## 46510:00 - 46540:00

how do we build the best possible

## 46540:00 - 46575:00

experience for uh the developer as well

## 46575:00 - 46605:00

as build the experience where we have so

## 46605:00 - 46640:00

many things for the the non-developer.

## 46640:00 - 46680:00

But I I have to imagine that this idea

## 46680:00 - 46710:00

of building technology if you as you get

## 46710:00 - 46740:00

better and better at understanding code

## 46740:00 - 46760:00

um you're going to be able to deliver a

## 46760:00 - 46790:00

great experience for non-developers um

## 46790:00 - 46825:00

as well. But I don't know what the path

## 46825:00 - 46850:00

dependence is. I assume like a bunch of

## 46850:00 - 46870:00

companies in the space will go from

## 46870:00 - 46900:00

non-developers to then supporting an

## 46900:00 - 46930:00

ability to edit the code, right? And I

## 46930:00 - 46955:00

think we're starting to see this already

## 46955:00 - 46980:00

where you know the the lines are sort of

## 46980:00 - 47000:00

getting blurred right now. You probably

## 47000:00 - 47035:00

care about it for your evals at least.

## 47035:00 - 47070:00

Yeah. No, you need to you need to care

## 47070:00 - 47090:00

about it for your evals. That maybe

## 47090:00 - 47125:00

that's like the hard part for me that to

## 47125:00 - 47155:00

to imagine for the pure non-developer

## 47155:00 - 47185:00

product. What is the hill you're

## 47185:00 - 47205:00

climbing if you're not like kind of

## 47205:00 - 47225:00

understanding the code? How do you know

## 47225:00 - 47245:00

your product is getting better and

## 47245:00 - 47270:00

better? Um is like an open question. Are

## 47270:00 - 47295:00

you completely relying on the base

## 47295:00 - 47320:00

models getting better, which is fine,

## 47320:00 - 47345:00

but then you should imagine then your

## 47345:00 - 47380:00

product is an extremely light layer on

## 47380:00 - 47410:00

top of the base model, which is a scary

## 47410:00 - 47430:00

place to be, right? That means you're

## 47430:00 - 47455:00

going to get competed across all

## 47455:00 - 47480:00

different axis. How do you think about

## 47480:00 - 47510:00

that in general? I guess like the

## 47510:00 - 47530:00

something we've talked about a lot on

## 47530:00 - 47595:00

this podcast is just the GBT rapper meme

## 47595:00 - 47645:00

um has completely gone away. I feel um

## 47645:00 - 47680:00

though every big release from one of the

## 47680:00 - 47700:00

labs sort of brings it back a little bit

## 47700:00 - 47725:00

and everyone's a little bit scared that

## 47725:00 - 47760:00

like you know open AI is just going to

## 47760:00 - 47795:00

eat everything. Um how do you think

## 47795:00 - 47830:00

about that? I think the way we I I think

## 47830:00 - 47855:00

about this is like yeah the company as I

## 47855:00 - 47885:00

mentioned before it's a moving goalpost

## 47885:00 - 47910:00

which is to say today if we're

## 47910:00 - 47950:00

generating sort of 80 90% of all

## 47950:00 - 47985:00

committed software uh yeah I think I

## 47985:00 - 48015:00

think when the new model comes out uh

## 48015:00 - 48045:00

we're going to need to up our game. We

## 48045:00 - 48075:00

can't just be at the same same stage.

## 48075:00 - 48100:00

maybe we need to be generating 95% of

## 48100:00 - 48130:00

all committed code and I think our

## 48130:00 - 48165:00

opportunity is the gap between where the

## 48165:00 - 48200:00

foundation model is and what the what

## 48200:00 - 48250:00

what 100% is right and as long as we can

## 48250:00 - 48280:00

continue to deliver an experience where

## 48280:00 - 48305:00

there is a gap between the two which I

## 48305:00 - 48330:00

think there is as long as there's any

## 48330:00 - 48365:00

human in the loop at all um in the

## 48365:00 - 48400:00

experience uh there's a gap we'll be

## 48400:00 - 48425:00

able to go out and build things but that

## 48425:00 - 48465:00

is a constantly transforming sort of uh

## 48465:00 - 48495:00

goalpost for us right so you can imagine

## 48495:00 - 48520:00

when a new model comes out maybe the

## 48520:00 - 48550:00

baseline on what the foundation model by

## 48550:00 - 48585:00

itself provides has doubled the alpha we

## 48585:00 - 48610:00

provide on top of what the base model

## 48610:00 - 48640:00

provides needs to double as well. It

## 48640:00 - 48670:00

feels very like for me the reason why

## 48670:00 - 48705:00

this is not the most concerning is let's

## 48705:00 - 48725:00

suppose that you were to take the

## 48725:00 - 48760:00

foundation model and it's providing 90%.

## 48760:00 - 48790:00

It's reducing the time it takes by 90%.

## 48790:00 - 48815:00

That actually means if we can deliver

## 48815:00 - 48850:00

one or two% more percentage points,

## 48850:00 - 48900:00

that's a 20% gain on top of what the new

## 48900:00 - 48935:00

baseline is, right? Like I guess 90 if

## 48935:00 - 48975:00

90 becomes 92 or 93. Um, which which

## 48975:00 - 49010:00

which is still very very valuable,

## 49010:00 - 49030:00

right? At that point because effectively

## 49030:00 - 49065:00

the 90 becomes the new baseline uh for

## 49065:00 - 49100:00

everyone. So I I think basically the way

## 49100:00 - 49125:00

we sort of operate is how can we provide

## 49125:00 - 49155:00

as much additional value as possible and

## 49155:00 - 49180:00

as long as we have our eye on that I

## 49180:00 - 49200:00

think we're going to we're going to do

## 49200:00 - 49230:00

fine. What advice would you have for our

## 49230:00 - 49255:00

startups that are working in the like AI

## 49255:00 - 49285:00

coding space? you have a ton of them.

## 49285:00 - 49315:00

What are what are the opportunities that

## 49315:00 - 49350:00

like you think are going to be open to

## 49350:00 - 49390:00

new startups? I've seen a lot of things

## 49390:00 - 49410:00

that I I think could be like

## 49410:00 - 49435:00

particularly interesting. I I don't

## 49435:00 - 49460:00

think any of these technologies we've

## 49460:00 - 49485:00

really adopted, but there's so many

## 49485:00 - 49520:00

different pieces of how people build

## 49520:00 - 49555:00

software and uh so and I'm not going to

## 49555:00 - 49575:00

say niche, but there are so many

## 49575:00 - 49605:00

different types of workloads out there.

## 49605:00 - 49630:00

I've not really seen a lot of startups

## 49630:00 - 49655:00

in the space that are just like we do

## 49655:00 - 49705:00

this one thing really really well. Um,

## 49705:00 - 49740:00

like I'll give you an example. Like we

## 49740:00 - 49770:00

do these kind of like Java migrations

## 49770:00 - 49805:00

really really well. Crazy enough, if you

## 49805:00 - 49830:00

look at this category, the amount that

## 49830:00 - 49870:00

people spend on this is probably maybe

## 49870:00 - 49895:00

billions if not tens of billions of

## 49895:00 - 49925:00

dollars doing these migrations every

## 49925:00 - 49955:00

year. It's a it's a massive category.

## 49955:00 - 49990:00

Um, that's an example. Migrations from

## 49990:00 - 50025:00

what to what? So example, this is like

## 50025:00 - 50060:00

actually kind of crazy. JVM 7 to eight

## 50060:00 - 50120:00

or something JVM Rails versions even

## 50120:00 - 50140:00

even more than that actually. It's like

## 50140:00 - 50180:00

a lot of a lot of companies write cobalt

## 50180:00 - 50220:00

have cobalt and crazy enough most of the

## 50220:00 - 50250:00

IRS software is written in cobalt.

## 50250:00 - 50280:00

Apparently in the early 2000s they try

## 50280:00 - 50320:00

to migrate from cobalt to Java. I think

## 50320:00 - 50350:00

it was a five plus billion dollar

## 50350:00 - 50375:00

project. Uh surprise surprise it didn't

## 50375:00 - 50400:00

happen. You think they could oneshot it

## 50400:00 - 50425:00

now? I don't I don't know if they can

## 50425:00 - 50465:00

oneshot it but I'm just kidding. But uh

## 50465:00 - 50505:00

but no but it's imagine imagine if you

## 50505:00 - 50540:00

could do those tasks very well. It's

## 50540:00 - 50570:00

such an economically valuable sort of

## 50570:00 - 50595:00

task. I think we obviously don't have

## 50595:00 - 50625:00

the ability to focus on these kinds of

## 50625:00 - 50645:00

things inside the company. That's a very

## 50645:00 - 50680:00

exciting space if you could do a really

## 50680:00 - 50705:00

good job there. The second key piece is

## 50705:00 - 50725:00

there are so many things that developers

## 50725:00 - 50765:00

do that are also not making the product

## 50765:00 - 50805:00

better uh but important like automatic

## 50805:00 - 50835:00

resolution of like you know kind of uh

## 50835:00 - 50885:00

alerts and and and uh and bugs in the in

## 50885:00 - 50925:00

in software. Um that's also a huge huge

## 50925:00 - 50970:00

amount of amount of spend um out there

## 50970:00 - 51000:00

and I'd be curious to see like what a

## 51000:00 - 51030:00

best-in-class product in that category

## 51030:00 - 51055:00

actually looks like. I'm sure someone

## 51055:00 - 51080:00

that if they got truly in the weeds on

## 51080:00 - 51100:00

that, they could build an awesome

## 51100:00 - 51145:00

product. Um, but but I think I I've not

## 51145:00 - 51170:00

heard of one that is like tremendously

## 51170:00 - 51185:00

taken off. I think those are actually

## 51185:00 - 51215:00

both really great insights. And one

## 51215:00 - 51235:00

thing I like about them is that there's

## 51235:00 - 51265:00

like it's not just an opportunity for

## 51265:00 - 51295:00

like two startups. Like each one of

## 51295:00 - 51325:00

those is like a bucket that could have

## 51325:00 - 51370:00

like a hundred large companies in. We

## 51370:00 - 51405:00

actually do have a company from from S21

## 51405:00 - 51435:00

called Bloop that does these Cobalt to

## 51435:00 - 51480:00

Java migrations with with agents. That's

## 51480:00 - 51520:00

awesome. It's a gnarly problem. It's a

## 51520:00 - 51550:00

very gnarly problem, but it's if you

## 51550:00 - 51575:00

were to talk to any company that has

## 51575:00 - 51605:00

existed for over 30 years, this is

## 51605:00 - 51630:00

probably something that is costing them

## 51630:00 - 51655:00

hundreds of millions a year. So,

## 51655:00 - 51690:00

reflecting on this journey, I mean,

## 51690:00 - 51710:00

we're all really thankful for you

## 51710:00 - 51740:00

creating Windsurf. It's uh you

## 51740:00 - 51785:00

supercharging all of society right now.

## 51785:00 - 51825:00

Uh what would you say to the person who

## 51825:00 - 51850:00

you know basically the you from 5 years

## 51850:00 - 51885:00

ago before you started this whole thing?

## 51885:00 - 51910:00

The biggest thing I would say is change

## 51910:00 - 51945:00

your mind much much faster than you

## 51945:00 - 51980:00

believe is reasonable. Right? It's very

## 51980:00 - 52005:00

easy to kind of fall in love with your

## 52005:00 - 52040:00

ideas um over and over again and you do

## 52040:00 - 52065:00

need to otherwise you won't really do

## 52065:00 - 52110:00

anything uh but but pivot as quickly as

## 52110:00 - 52140:00

possible and treat pivots as a badge of

## 52140:00 - 52165:00

honor. Most people don't have the

## 52165:00 - 52190:00

courage to change their mind on things

## 52190:00 - 52230:00

and they would rather kind of fail doing

## 52230:00 - 52250:00

the thing that they told everyone they

## 52250:00 - 52290:00

were doing than uh change their mind uh

## 52290:00 - 52325:00

take a bold step and succeed. Vun, thank

## 52325:00 - 52355:00

you so much for joining us today. We'll

## 52355:00 - 52395:00

catch you guys next time.

## 52395:00+

[Music]

