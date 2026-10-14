---
source: https://www.youtube.com/watch?v=HIiLt3Kb1kQ
title: How to (logically) test Facebook Ads at an incredible speed
author: Steph France
date: 2025-08-24
views: 2097
description: >-
  D2C brand & consumer app, work with me: https://sfrance.co


  🔗 Get the file from the video:
  https://curiousmarketer.gumroad.com/l/programmatic-creative-testing


  WATCH NEXT 👇

  https://www.youtube.com/watch?v=QDvuD90XV9k


  TOOLS (affiliate links) 👇


  Templated (Static ads image creation at scale):

  https://swiy.co/templated


  Icon (Turn your mini-VSL script into an ad):

  https://swiy.co/icon


  WORK WITH ME 👇

  https://tally.so/r/wM4pRA


  CONNECT WITH ME 👇


  https://twitter.com/meetstef

  https://www.linkedin.com/in/stephane-franceschini


  DESCRIPTION:


  Learn how to run programmatic creative testing for Facebook (Meta) Ads—fast,
  logically, and at scale. This video shows a complete system that turns ad
  creative into variables (USP, marketing angle, messaging framework, level of
  awareness, market sophistication, copy length), feeds them to an LLM, and
  pushes bulk ads into Ads Manager—so you can test more ideas, find winners, and
  iterate with intent.


  What you’ll see:

  • The thinking: segmenting an ad into controllable variables (USP → angles →
  frameworks → awareness/sophistication) so you test messages, not guesses.  

  • The build: a Google Sheets + Make.com backend that composes prompts
  (ChatGPT/Claude), generates hooks, and creates static image ads from templates
  (via an image templating API).  

  • The workflow: generate hooks → human review → render variants → push to
  existing ad sets → let the algorithm allocate spend → mark winners →
  iterate.  

  • Expansion: turn winning hooks into mini VSL/text-based scripts for voiceover
  + B-roll assembly.  

  • Example used: Jones Road Beauty’s “Miracle Balm” to illustrate USP → angle →
  hook → image → ad deployment.


  Why this matters:

  • Systematic creative coverage: test multiple USPs and angles without creative
  chaos.  

  • Voice of customer first: mine reviews, forums, and Reddit for exact phrasing
  to feed the model.  

  • Faster throughput: prioritize static images to validate hooks before
  producing video.  

  • Structured iteration: once a winner emerges, spin variants (new images,
  adjacent angles, new frameworks) instead of starting from scratch.


  Key concepts included:

  • Unique Selling Proposition (USP) vs. marketing angles (angle = one focused
  way to express a USP).  

  • Messaging frameworks (e.g., bold statements, desire/future state) and copy
  length control.  

  • Eugene Schwartz: levels of awareness (unaware → most aware) and market
  sophistication (1–5).  

  • Campaign structure approach: build campaigns/ad sets yourself, push ads via
  API, and give the algorithm wide room to optimize.


  Tools/workflow stack:

  • Research & prompts: Google Sheets (context hub), voice-of-customer “gold
  nuggets” (reviews, forums).  

  • Automation: Make.com for prompt assembly + API calls.  

  • LLMs: ChatGPT / Claude for copy generation.  

  • Creatives: template-based image rendering via API (auto-fit headline
  length).  

  • Ads Manager: bulk ad creation into selected ad sets.  

  • Post-win: script generation for mini VSLs and B-roll mapping in an editor.


  Who this is for:

  • Media buyers, performance marketers, founders, agencies, and teams running
  ecom, SaaS, apps, or services on Meta who want faster, more logical creative
  testing and a repeatable system.


  Search intents this video answers:

  • “How to test Facebook ads fast”  

  • “Facebook ads creative testing framework”  

  • “Programmatic creative testing Meta ads”  

  • “AI for Facebook ads copy + image generation”  

  • “Bulk ad creation Google Sheets + Make.com”


  TIMESTAMPS:


  00:00 - Introduction to programmatic testing

  04:45 - Mental framework overview

  09:31 - Context: brand, product, voice

  14:16 - System setup: sheets, automations

  19:02 - Unique selling propositions and angles

  23:47 - Hooks, frameworks, awareness

  28:33 - From hooks to images and ads

  33:18 - Iteration, scripts, and wrap-up
tags:
  - Facebook Ads
  - Facebook ads testing
  - creative testing framework
  - creative testing facebook ads
  - facebook ads strategy
  - facebook advertising
  - facebook ads creative testing
  - how to test facebook ads
  - facebook ads
  - ecommerce
  - facebook ads testing
  - facebook ads testing strategy
  - facebook ad creative testing
  - facebook ad testing framework
  - meta ads
  - ad creative testing
  - facebook ads creative strategy
  - how to test facebook ad creative
  - facebook ad creative
  - scaling facebook ads
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T11:53:02.149Z
---

# How to (logically) test Facebook Ads at an incredible speed

## 00:00 - 35:00

In this video, I want to show you how to

## 35:00 - 75:00

do programmatic creative testing at

## 75:00 - 130:00

scale. But first, let's figure out what

## 130:00 - 215:00

it is exactly. See, an ad, it's not only

## 215:00 - 275:00

um a piece of written copy or a nice

## 275:00 - 335:00

picture. It's you can segment an ad into

## 335:00 - 390:00

different predefined parameters. You can

## 390:00 - 425:00

have a unique selling proposition you

## 425:00 - 480:00

want this specific ad to push. You can

## 480:00 - 525:00

have the marketing angle related to this

## 525:00 - 565:00

specific unique selling proposition that

## 565:00 - 605:00

you want the ad to push. You can have a

## 605:00 - 645:00

specific messaging framework you want to

## 645:00 - 695:00

use in your ad. You can use the

## 695:00 - 745:00

awareness of your prospect related to

## 745:00 - 790:00

your product or the sophistication of

## 790:00 - 820:00

your market or even the length of the

## 820:00 - 860:00

copy. So, as you can see, there are so

## 860:00 - 925:00

many different variables that we can use

## 925:00 - 985:00

to create an ad. And by an ad, I mean a

## 985:00 - 1045:00

hook or a longer copy that you can use

## 1045:00 - 1110:00

as a mini VSSL or whatever the ad is.

## 1110:00 - 1160:00

You always can segment it into different

## 1160:00 - 1220:00

variables. So now that AI can handle the

## 1220:00 - 1270:00

creative part, if we are able to build a

## 1270:00 - 1360:00

system to feed the right variables to an

## 1360:00 - 1420:00

LLM model, an AI, then the AI can

## 1420:00 - 1470:00

actually output the ads that we want.

## 1470:00 - 1540:00

Exactly. Which allow us to then generate

## 1540:00 - 1600:00

hundreds or thousands of different ads,

## 1600:00 - 1630:00

review them to make sure that they are

## 1630:00 - 1665:00

good. So that's the human touch. and

## 1665:00 - 1705:00

then push them right away into an ad

## 1705:00 - 1765:00

account. So we are able to literally

## 1765:00 - 1830:00

test with a proper structure and test

## 1830:00 - 1875:00

every potential marketing angle and

## 1875:00 - 1925:00

every potential combination that we

## 1925:00 - 1970:00

want. And in this video I'm going to

## 1970:00 - 2020:00

show you you can see two screens. Why is

## 2020:00 - 2060:00

because here it's the thinking process

## 2060:00 - 2110:00

behind it. So that's the most important

## 2110:00 - 2145:00

thing in this video is actually to

## 2145:00 - 2195:00

understand like how to think of

## 2195:00 - 2250:00

programmatic creative testing. Uh and at

## 2250:00 - 2280:00

the same time I'm going to show you the

## 2280:00 - 2330:00

system that I used I built for my

## 2330:00 - 2360:00

clients that they are currently using to

## 2360:00 - 2400:00

scale their ad accounts and find winning

## 2400:00 - 2460:00

ads after winning ads. Um and we will go

## 2460:00 - 2520:00

and we will see the different uh pieces

## 2520:00 - 2585:00

of the system one after the other. So

## 2585:00 - 2620:00

you will not only see a spreadsheet but

## 2620:00 - 2685:00

you will see a proper uh mental

## 2685:00 - 2725:00

framework that you can use. So who is it

## 2725:00 - 2760:00

for? Basically every company that is

## 2760:00 - 2800:00

running ads on Facebook can use this

## 2800:00 - 2840:00

system, this approach. If you are a

## 2840:00 - 2880:00

business owner, uh this might completely

## 2880:00 - 2920:00

change the way you think of running your

## 2920:00 - 2970:00

paid acquisition. If you are a marketer,

## 2970:00 - 3020:00

I think you will love it. And if you are

## 3020:00 - 3085:00

not yet at the scale of u scaling ads or

## 3085:00 - 3140:00

even running ads then it is worth keep

## 3140:00 - 3190:00

watching because what you will learn the

## 3190:00 - 3265:00

way to think of ads in a logical and

## 3265:00 - 3325:00

structural way will probably reframe uh

## 3325:00 - 3380:00

your approach uh so you will be a lot

## 3380:00 - 3420:00

better of when you you get into it. So

## 3420:00 - 3445:00

if you're new here my name is Steph

## 3445:00 - 3485:00

France. I'm a marketer and independent

## 3485:00 - 3520:00

consultant and on this channel I help

## 3520:00 - 3560:00

you to generate more revenue by writing

## 3560:00 - 3610:00

marketing copy that resonates with your

## 3610:00 - 3660:00

customer and I do it using AI of course

## 3660:00 - 3710:00

uh market research a lot and system

## 3710:00 - 3750:00

thinking before everything. So let's

## 3750:00 - 3790:00

dive into it. Just for context, the

## 3790:00 - 3815:00

system you're going to see in this video

## 3815:00 - 3860:00

is the exact reproduction of the system

## 3860:00 - 3905:00

I use for my client, but I did it for

## 3905:00 - 3945:00

the brand John Road Beauty, which is a

## 3945:00 - 3995:00

D2C brand that a lot of people know. Uh,

## 3995:00 - 4040:00

and I used this product as an example.

## 4040:00 - 4085:00

So, this way I get to show it to you

## 4085:00 - 4125:00

without having to hide anything. And

## 4125:00 - 4160:00

again this system works for every type

## 4160:00 - 4220:00

of product uh whether it's e-commerce uh

## 4220:00 - 4270:00

consumer app SAS service whatever as

## 4270:00 - 4305:00

long as you can advertise on Facebook

## 4305:00 - 4335:00

but just for the sake of the example

## 4335:00 - 4365:00

remember that everything you will see is

## 4365:00 - 4420:00

for Jones beauty a D2C brand okay so

## 4420:00 - 4460:00

before showing you the actual system I

## 4460:00 - 4505:00

want to show you the mental framework um

## 4505:00 - 4545:00

so you understand how it works before

## 4545:00 - 4585:00

seeing it and I think it's the best way

## 4585:00 - 4620:00

because it's kind of a complex system to

## 4620:00 - 4665:00

to explain and I want it to be as simple

## 4665:00 - 4710:00

as possible so you you grab the main

## 4710:00 - 4750:00

idea not the the nitty-gritty of how it

## 4750:00 - 4820:00

works. So let's move on first to uh this

## 4820:00 - 4855:00

mental framework and then after that I

## 4855:00 - 4890:00

will show you the different pieces but

## 4890:00 - 4920:00

then every time I will show you a piece

## 4920:00 - 4970:00

you will know exactly what it means

## 4970:00 - 5025:00

within this framework. So when we talk

## 5025:00 - 5090:00

about um programmatic creative testing,

## 5090:00 - 5110:00

first of all we need to generate the

## 5110:00 - 5140:00

ads. And to generate the ads, what we

## 5140:00 - 5175:00

need is the full context about the

## 5175:00 - 5215:00

product. And to get the full context, we

## 5215:00 - 5265:00

need to give as much information as

## 5265:00 - 5305:00

possible to the AI we are going to use.

## 5305:00 - 5345:00

And for that we want the AI to

## 5345:00 - 5380:00

understand the brand. So we want a

## 5380:00 - 5415:00

proper brand description. We want the AI

## 5415:00 - 5450:00

to understand the product that we are

## 5450:00 - 5490:00

selling because it's always product by

## 5490:00 - 5530:00

product. Uh because you can't just

## 5530:00 - 5555:00

advertise a brand. You want to advertise

## 5555:00 - 5605:00

a product of course. And then we want to

## 5605:00 - 5660:00

give AI the voice of the customer. And

## 5660:00 - 5715:00

this one is probably the most important

## 5715:00 - 5760:00

because the ads that we are going to

## 5760:00 - 5825:00

create are going to be created with

## 5825:00 - 5875:00

using as much as possible the proper

## 5875:00 - 5925:00

wording that the customers are using

## 5925:00 - 5970:00

whether whether it's uh in the customer

## 5970:00 - 6045:00

reviews or if it's on forums or Reddit

## 6045:00 - 6100:00

uh wherever the customer is talking

## 6100:00 - 6140:00

about their pain we are going to gather

## 6140:00 - 6170:00

all this information and we feed it to

## 6170:00 - 6230:00

AI every time we generate new uh copy.

## 6230:00 - 6270:00

So that gives us the full context about

## 6270:00 - 6345:00

the product then from that we are using

## 6345:00 - 6390:00

AI or not to generate different unique

## 6390:00 - 6425:00

selling proposition. What are selling

## 6425:00 - 6490:00

proposition? Before you ask let's read a

## 6490:00 - 6530:00

short description so we are all aligned.

## 6530:00 - 6585:00

So a unique selling proposition USP is

## 6585:00 - 6625:00

your product's overall unique position

## 6625:00 - 6660:00

in the marketplace. The fundamental

## 6660:00 - 6715:00

promise that differentiates you from all

## 6715:00 - 6765:00

competitors. It's the big picture

## 6765:00 - 6805:00

identity that establishes what makes

## 6805:00 - 6860:00

your product uniquely valuable and why

## 6860:00 - 6905:00

customers should choose you over

## 6905:00 - 6980:00

alternatives. So this is basically you

## 6980:00 - 7000:00

don't have many unique thing

## 7000:00 - 7040:00

proposition. It's like one two three

## 7040:00 - 7085:00

four maximum. It's like the very thing

## 7085:00 - 7130:00

that you you that matter to your

## 7130:00 - 7160:00

customer and that differentiate you from

## 7160:00 - 7200:00

your competitors. So once we have all

## 7200:00 - 7275:00

the context uh then we can think of what

## 7275:00 - 7355:00

are our USPS and for each USP you have

## 7355:00 - 7400:00

different ways to talk about it that

## 7400:00 - 7445:00

where that's where we use marketing

## 7445:00 - 7485:00

angles and as you can see marketing

## 7485:00 - 7555:00

angles are related to a specific USB. So

## 7555:00 - 7595:00

the the overall thing is like you have

## 7595:00 - 7665:00

your product which you have different uh

## 7665:00 - 7700:00

unique selling propositions that each

## 7700:00 - 7725:00

have

## 7725:00 - 7780:00

a lot an infinity of marketing angles

## 7780:00 - 7815:00

that we can use to talk about this

## 7815:00 - 7865:00

specific USP. And again quick definition

## 7865:00 - 7905:00

of a marketing angle it's a specific

## 7905:00 - 7960:00

slice or focus of your USP that becomes

## 7960:00 - 8020:00

the hero of one individual ad campaign.

## 8020:00 - 8055:00

While your USP is the strategic

## 8055:00 - 8090:00

foundation that defines your overall

## 8090:00 - 8130:00

unique market position, a marketing

## 8130:00 - 8180:00

angle takes one specific aspect of that

## 8180:00 - 8235:00

USP and makes it the central message for

## 8235:00 - 8275:00

testing purposes. Each angle should be

## 8275:00 - 8320:00

laser focused on a single emotional

## 8320:00 - 8370:00

trigger, customer problem or benefit.

## 8370:00 - 8420:00

Testing one specific way to communicate

## 8420:00 - 8455:00

positioning rather than trying to

## 8455:00 - 8510:00

communicate everything at once.

## 8510:00 - 8545:00

I hope it's clear. Sorry for my reading

## 8545:00 - 8580:00

in English that is not the best but I

## 8580:00 - 8630:00

get I guess you understood. So once we

## 8630:00 - 8680:00

have this uh

## 8680:00 - 8740:00

we need to frame the message that we are

## 8740:00 - 8810:00

going to create and we can use specific

## 8810:00 - 8875:00

framework that we know work. So when we

## 8875:00 - 8915:00

want to push a specific unique selling

## 8915:00 - 8970:00

proposition using a specific angle then

## 8970:00 - 9015:00

now we can use a specific uh messaging

## 9015:00 - 9045:00

framework. I will show that uh a little

## 9045:00 - 9095:00

bit later in the video um and it will

## 9095:00 - 9140:00

become more clear but let's move on.

## 9140:00 - 9190:00

Then we need to define

## 9190:00 - 9245:00

what type of uh where where is the

## 9245:00 - 9280:00

customer at in their journey of becoming

## 9280:00 - 9315:00

a buyer. So this is the level of

## 9315:00 - 9355:00

awareness something that uh was

## 9355:00 - 9400:00

introduced by Eugene Schwartz which is a

## 9400:00 - 9440:00

very well-known copyriter that wrote

## 9440:00 - 9475:00

breakthrough advertising like every

## 9475:00 - 9515:00

copyriter out there know about that uh

## 9515:00 - 9565:00

but to talk about it quickly um you have

## 9565:00 - 9610:00

a market that is potentially buying your

## 9610:00 - 9650:00

product and depending of the product you

## 9650:00 - 9680:00

will have

## 9680:00 - 9715:00

the market will be segmented in

## 9715:00 - 9770:00

different aspect. So for example, if

## 9770:00 - 9830:00

something is uh is pretty niche, then

## 9830:00 - 9885:00

probably the people that are aware of

## 9885:00 - 9930:00

the solutions and aware of the problem

## 9930:00 - 9985:00

are a lot uh less than if we talk for

## 9985:00 - 10045:00

example like John Johns Rob Beauty

## 10045:00 - 10080:00

skincare is very well known. So we have

## 10080:00 - 10120:00

a lot of people that are solution aware

## 10120:00 - 10160:00

problem aware. Um, if you go from the

## 10160:00 - 10205:00

very beginning, unaware means, I don't

## 10205:00 - 10235:00

even know I have the problem. Problem

## 10235:00 - 10265:00

aware, I'm aware I have this problem,

## 10265:00 - 10290:00

but I I don't even know if there are

## 10290:00 - 10335:00

solutions. Solution aware is like, okay,

## 10335:00 - 10370:00

I I've heard about the solutions, didn't

## 10370:00 - 10415:00

really dig into it yet, but I'm I'm kind

## 10415:00 - 10445:00

of aware that I have a problem and

## 10445:00 - 10480:00

solutions exist. Product aware is

## 10480:00 - 10535:00

someone that already has uh dug into the

## 10535:00 - 10565:00

finding solutions and know a little bit

## 10565:00 - 10610:00

of the market. uh and most aware would

## 10610:00 - 10655:00

be the people that are aware about your

## 10655:00 - 10680:00

specific product. So it's always like a

## 10680:00 - 10735:00

very specific uh pieces of the market.

## 10735:00 - 10770:00

But when you create again when I I go

## 10770:00 - 10810:00

back here, we can push a unique selling

## 10810:00 - 10865:00

proposition uh you using a specific

## 10865:00 - 10900:00

marketing angle with whatever messaging

## 10900:00 - 10965:00

framework we want. But we we are not

## 10965:00 - 11020:00

going to talk about it the same way if

## 11020:00 - 11070:00

we talk about uh if we talk to someone

## 11070:00 - 11115:00

that is just aware that they have a

## 11115:00 - 11180:00

problem or if we talk to someone that is

## 11180:00 - 11240:00

already uh very far along very far into

## 11240:00 - 11285:00

the journey of uh finding a solution for

## 11285:00 - 11340:00

this problem. So this is important to

## 11340:00 - 11410:00

give AI the information about who we are

## 11410:00 - 11440:00

talking to.

## 11440:00 - 11500:00

So with that said um we generate our

## 11500:00 - 11525:00

hooks because for the sake of this

## 11525:00 - 11565:00

example we are generating hooks. We

## 11565:00 - 11605:00

generate a bunch of them. We pick the

## 11605:00 - 11660:00

ones we like and then we generate an

## 11660:00 - 11705:00

image because we are the best way to

## 11705:00 - 11755:00

test a lot of ads at scale is to to use

## 11755:00 - 11835:00

static ads. Um video ads uh longer ads

## 11835:00 - 11875:00

are more complicated to produce and

## 11875:00 - 11920:00

static ads work really well. So we use a

## 11920:00 - 11980:00

combination of a hook based uh put on

## 11980:00 - 12025:00

different images uh that we are going to

## 12025:00 - 12065:00

push to the ad account uh and let

## 12065:00 - 12100:00

Facebook do its magic because the way we

## 12100:00 - 12160:00

are going to uh use uh to structure the

## 12160:00 - 12205:00

campaign on Facebook ads is by letting

## 12205:00 - 12270:00

the algorithm uh as much freedom as

## 12270:00 - 12320:00

possible. So Facebook will decide which

## 12320:00 - 12360:00

ads are resonating the most with your

## 12360:00 - 12405:00

customer.

## 12405:00 - 12470:00

So with that approach already uh you can

## 12470:00 - 12495:00

take it away. I'm not saying you should

## 12495:00 - 12540:00

stop the video, right? But just just

## 12540:00 - 12595:00

starting thinking about uh creating ads

## 12595:00 - 12640:00

in that way

## 12640:00 - 12680:00

is is already helpful because the the

## 12680:00 - 12720:00

one of the biggest problem of uh and

## 12720:00 - 12755:00

actually a lot of

## 12755:00 - 12810:00

marketing agencies uh don't have like a

## 12810:00 - 12850:00

structured way to to think of ads. So,

## 12850:00 - 12900:00

it's more creative. But again, um I'm

## 12900:00 - 12940:00

not I'm not a creative person. Uh I like

## 12940:00 - 12975:00

systems and I like to understand what

## 12975:00 - 13015:00

I'm doing. And if you start thinking of

## 13015:00 - 13080:00

ads into in something that is not chaos,

## 13080:00 - 13125:00

it's it's logical. It's like when you

## 13125:00 - 13190:00

find uh everything that you see um in

## 13190:00 - 13235:00

pink right here, it's like after you've

## 13235:00 - 13280:00

tested so many of them, you know, after

## 13280:00 - 13310:00

you have

## 13310:00 - 13380:00

this, then you find the ones that are

## 13380:00 - 13435:00

actually uh resonating with your

## 13435:00 - 13470:00

customers and and they already exist.

## 13470:00 - 13495:00

You just have to find them. You just

## 13495:00 - 13525:00

have to find the right message, the the

## 13525:00 - 13560:00

right framework to speak to your

## 13560:00 - 13590:00

customer. And then once you have them

## 13590:00 - 13650:00

then you can one uh scale them as much

## 13650:00 - 13690:00

as you can and two you can iterate from

## 13690:00 - 13735:00

it to create better ads.

## 13735:00 - 13775:00

But now let's go back into the system.

## 13775:00 - 13810:00

So it will be a little bit more uh

## 13810:00 - 13860:00

technical. But uh now I want to show you

## 13860:00 - 13910:00

how you can actually uh automate all of

## 13910:00 - 13955:00

that. If you are an established business

## 13955:00 - 13990:00

and you would like to uh install this

## 13990:00 - 14035:00

system uh then I will put a link in the

## 14035:00 - 14065:00

description probably a quick form that

## 14065:00 - 14115:00

you can just uh fill out and so I will

## 14115:00 - 14160:00

be notified and I will get back to you

## 14160:00 - 14205:00

as soon as possible. So first of all uh

## 14205:00 - 14240:00

brand description that's the we are

## 14240:00 - 14280:00

talking about the context. Now here is a

## 14280:00 - 14325:00

spreadsheet as you recognized it's u

## 14325:00 - 14375:00

it's in it's built within Google sheets

## 14375:00 - 14420:00

and one spreadsheet can be used for um

## 14420:00 - 14470:00

one product basically and every of these

## 14470:00 - 14510:00

spreadsheets will be connected to a back

## 14510:00 - 14565:00

end which is built uh within make.com

## 14565:00 - 14630:00

and it contains few uh automations

## 14630:00 - 14670:00

that are not that complicated uh but

## 14670:00 - 14730:00

just to show you and this is not a video

## 14730:00 - 14760:00

about making automations

## 14760:00 - 14815:00

But those automations are gathering all

## 14815:00 - 14850:00

the data that we put within the

## 14850:00 - 14870:00

spreadsheet. So you can see brand

## 14870:00 - 14900:00

description, product description. It

## 14900:00 - 14955:00

gathers everything together and and in

## 14955:00 - 15020:00

the end it creates those huge prompts

## 15020:00 - 15065:00

that we are going to use either with

## 15065:00 - 15125:00

cloud or with uh chat GPT and put back

## 15125:00 - 15170:00

into the spreadsheet. So again the point

## 15170:00 - 15215:00

here is not to show you automations is

## 15215:00 - 15265:00

that you understand that this framework

## 15265:00 - 15325:00

this system uh is built into a

## 15325:00 - 15365:00

spreadsheet which is extremely simple

## 15365:00 - 15415:00

but every action that we do is run on

## 15415:00 - 15450:00

the back end uh through make.com

## 15450:00 - 15500:00

connected to the different APIs AIS that

## 15500:00 - 15555:00

we need to make it run. So let's go back

## 15555:00 - 15600:00

to the brand description here. we need

## 15600:00 - 15655:00

to input the the information that the

## 15655:00 - 15705:00

brand uh that we have about the brand.

## 15705:00 - 15740:00

So if you don't know anything about the

## 15740:00 - 15775:00

brand for example if it's not yours but

## 15775:00 - 15820:00

a client's brand then you can use uh

## 15820:00 - 15875:00

prompt. So we use predefined prompt uh

## 15875:00 - 15935:00

to have AI dig into the brand and uh

## 15935:00 - 15980:00

understand all the specificity of the

## 15980:00 - 16030:00

branding. Then you copy it and past it

## 16030:00 - 16090:00

into the right section. So the system

## 16090:00 - 16135:00

will take all that information and bring

## 16135:00 - 16210:00

it to the uh um the AI on the back end.

## 16210:00 - 16250:00

And I actually think that I showed you a

## 16250:00 - 16290:00

wrong one because that was the product

## 16290:00 - 16320:00

but it doesn't matter because this is

## 16320:00 - 16360:00

the exact same approach. Then you take

## 16360:00 - 16415:00

the product page and you feed AI with it

## 16415:00 - 16455:00

which uh will give you all the

## 16455:00 - 16490:00

information about specific product. So

## 16490:00 - 16550:00

the II know what exactly uh is the

## 16550:00 - 16585:00

product that it's advertising and then

## 16585:00 - 16625:00

now we have the gold nuggets and that is

## 16625:00 - 16660:00

the most uh interesting and important

## 16660:00 - 16710:00

thing. So either the the brand the

## 16710:00 - 16765:00

product already has customer reviews

## 16765:00 - 16815:00

then we would gather everything like um

## 16815:00 - 16860:00

take a huge piece of copy and pasted

## 16860:00 - 16930:00

text of the reviews give it to AI with

## 16930:00 - 16985:00

predefined prompt that will only keep

## 16985:00 - 17025:00

the the important quotes and then we

## 17025:00 - 17055:00

just copy them here the same way we have

## 17055:00 - 17090:00

done for brand and product description

## 17090:00 - 17130:00

but we also want to understand what

## 17130:00 - 17170:00

people are talking about on the internet

## 17170:00 - 17210:00

and for that I'm going to link in the

## 17210:00 - 17260:00

the description a video that is all

## 17260:00 - 17320:00

about the voice mining framework. So how

## 17320:00 - 17395:00

to to use all the available AI agents to

## 17395:00 - 17445:00

gather every sources on the internet and

## 17445:00 - 17500:00

create this kind of gold nuggets that

## 17500:00 - 17550:00

are basically uh here you have the

## 17550:00 - 17595:00

context about a specific painoint and

## 17595:00 - 17640:00

then you have all the different quotes

## 17640:00 - 17705:00

that people um have said things that

## 17705:00 - 17740:00

people have said on the internet about

## 17740:00 - 17770:00

this specific paint and it's not

## 17770:00 - 17820:00

obviously related to your product, but

## 17820:00 - 17855:00

this is related to your pain point. So

## 17855:00 - 17885:00

again, link in the description, there is

## 17885:00 - 17925:00

a full video about it and it teaches it

## 17925:00 - 17965:00

shows you how to really go from you have

## 17965:00 - 18050:00

no idea about what to um about marketing

## 18050:00 - 18100:00

at all to doing all the research prompt

## 18100:00 - 18140:00

after prompt after prompt using all the

## 18140:00 - 18195:00

AI agents and end up with a master

## 18195:00 - 18220:00

prompt that you can use for your

## 18220:00 - 18250:00

marketing. market research is only a

## 18250:00 - 18285:00

part of it that you can you can use it

## 18285:00 - 18330:00

for this specific purpose but otherwise

## 18330:00 - 18370:00

the the video will also show you how to

## 18370:00 - 18395:00

just generate marketing without even

## 18395:00 - 18425:00

using this system. So really encourage

## 18425:00 - 18470:00

you to to watch it. Anyway that was

## 18470:00 - 18550:00

apparent uh so now we have here we have

## 18550:00 - 18580:00

the run description product description

## 18580:00 - 18620:00

voice banning so we have all the context

## 18620:00 - 18650:00

and now we have we want to have the

## 18650:00 - 18695:00

unique selling proposition. So here are

## 18695:00 - 18725:00

the unique selling proposition which

## 18725:00 - 18775:00

have been uh if you ask uh a brand like

## 18775:00 - 18815:00

John Road beauty they obviously know

## 18815:00 - 18840:00

their unique selling proposition. You

## 18840:00 - 18885:00

don't need AI to actually generate it

## 18885:00 - 18925:00

for you. But in case you need it then

## 18925:00 - 18975:00

you still can ask AI saying hey this is

## 18975:00 - 19005:00

my uh brand description product

## 19005:00 - 19055:00

description uh this is what people say

## 19055:00 - 19105:00

about our products about their programs.

## 19105:00 - 19160:00

please generate uh

## 19160:00 - 19215:00

one, two, three, five USBs for this

## 19215:00 - 19250:00

specific product for me and then you

## 19250:00 - 19305:00

input them in the system. Then here is

## 19305:00 - 19375:00

the first um aspect of the system is

## 19375:00 - 19425:00

that we can generate different marketing

## 19425:00 - 19490:00

angles for a specific USB which means

## 19490:00 - 19540:00

this is where the creativity comes up.

## 19540:00 - 19605:00

At this point you have for example we

## 19605:00 - 19645:00

are talking about this product right

## 19645:00 - 19675:00

miracle bomb. I realized afterward I

## 19675:00 - 19710:00

shouldn't have taken a skincare product

## 19710:00 - 19745:00

because I'm absolutely not an expert in

## 19745:00 - 19795:00

there in that but it doesn't matter.

## 19795:00 - 19855:00

This product miracle bomb the one USB

## 19855:00 - 19885:00

could be the only makeup that's

## 19885:00 - 19930:00

literally impossible to overdo and it

## 19930:00 - 19985:00

describes this specific USB. And now

## 19985:00 - 20040:00

when I generate uh marketing angles

## 20040:00 - 20090:00

here. So I will show you just for the

## 20090:00 - 20120:00

sake of showing you. I'm just clicking

## 20120:00 - 20160:00

here. When I click here, it triggers a

## 20160:00 - 20195:00

web hook. Technical thing. You don't

## 20195:00 - 20225:00

have to know that. But basically it

## 20225:00 - 20270:00

triggers one of the uh the automations

## 20270:00 - 20300:00

that I showed you on the back end that

## 20300:00 - 20405:00

is now uh generating the uh new

## 20405:00 - 20470:00

marketing angles for this specific USB.

## 20470:00 - 20520:00

So there we have them, all the marketing

## 20520:00 - 20545:00

angles that I've generated so far. And

## 20545:00 - 20570:00

as you can see, they're all related to

## 20570:00 - 20625:00

one specific USB. So for the USB we were

## 20625:00 - 20660:00

talking about, the only makeup that's

## 20660:00 - 20695:00

literally impossible to overdo, you can

## 20695:00 - 20760:00

say you can keep applying and it never

## 20760:00 - 20805:00

looks overdone. or if you go too strong

## 20805:00 - 20850:00

with other makeups, it soften back

## 20850:00 - 20895:00

softens it back to natural

## 20895:00 - 20960:00

or uh even in bad lighting or with shaky

## 20960:00 - 21005:00

hands, you still can't mess it up. And

## 21005:00 - 21055:00

then it also explains like this specific

## 21055:00 - 21090:00

marketing angle that is specifically

## 21090:00 - 21115:00

talking about this unique selling

## 21115:00 - 21145:00

proposition. I hope I'm not losing you

## 21145:00 - 21180:00

here. Um but it's very important

## 21180:00 - 21225:00

concept. It's what I was showing here on

## 21225:00 - 21265:00

the side. uh unique selling proposition

## 21265:00 - 21315:00

different marketing angles. So now that

## 21315:00 - 21350:00

we have them, let's see if we have

## 21350:00 - 21395:00

generated them. Not yet already, but it

## 21395:00 - 21435:00

doesn't matter. We don't need them. Uh

## 21435:00 - 21500:00

we arrive at the most important piece of

## 21500:00 - 21530:00

the system is where we are generating

## 21530:00 - 21595:00

the hooks. And as you can see here on

## 21595:00 - 21650:00

the left, I can pick the unique selling

## 21650:00 - 21690:00

proposition I want. And then I can pick

## 21690:00 - 21725:00

the marketing. So let's say this one

## 21725:00 - 21760:00

even in bad lighting or with shaky hands

## 21760:00 - 21800:00

you still can't mess it up and then I

## 21800:00 - 21840:00

have all the messaging frameworks that I

## 21840:00 - 21875:00

was talking about those messaging

## 21875:00 - 21925:00

framework they are

## 21925:00 - 21950:00

on the back end I'm not showing it to

## 21950:00 - 21995:00

you but there there are like specific

## 21995:00 - 22050:00

spreadsheet that uh has hundreds of

## 22050:00 - 22105:00

hooks performing hooks uh that are going

## 22105:00 - 22165:00

to be given to the AI at the moment of

## 22165:00 - 22220:00

generating the hooks uh as examples of

## 22220:00 - 22270:00

what is working in advertising basically

## 22270:00 - 22305:00

and for each of them we have examples uh

## 22305:00 - 22360:00

so you basically say okay I want um for

## 22360:00 - 22395:00

this one I want I don't know desire

## 22395:00 - 22430:00

future states

## 22430:00 - 22470:00

and I want to talk about just program

## 22470:00 - 22520:00

aware people uh the sophistication of

## 22520:00 - 22580:00

the market I am okay let me quickly talk

## 22580:00 - 22610:00

about the sophistication of the market

## 22610:00 - 22645:00

it's another concept that comes from

## 22645:00 - 22675:00

Eugene Schwarz uh in the book

## 22675:00 - 22700:00

Breakthrough Advertising

## 22700:00 - 22760:00

But I think one of the cool thing I know

## 22760:00 - 22790:00

uh

## 22790:00 - 22830:00

I realized about explaining that concept

## 22830:00 - 22875:00

is while I was watching a series um

## 22875:00 - 22940:00

quite recently I think it's 1923

## 22940:00 - 23040:00

uh and so in the in the US um few like

## 23040:00 - 23075:00

100 years ago and you see the first

## 23075:00 - 23120:00

people uh coming into the different

## 23120:00 - 23175:00

cities and selling washing machines,

## 23175:00 - 23195:00

laundry machines

## 23195:00 - 23245:00

And it struck me because they are just

## 23245:00 - 23285:00

showing like hey this washes your

## 23285:00 - 23340:00

clothes and everybody is is amazed by

## 23340:00 - 23360:00

that. It's like what what do you mean

## 23360:00 - 23400:00

it's washing my closes?

## 23400:00 - 23430:00

It doesn't need me to do anything. No no

## 23430:00 - 23465:00

it's just washing washing your closes.

## 23465:00 - 23520:00

And at this point the market was at the

## 23520:00 - 23570:00

first level. it. You didn't need to say,

## 23570:00 - 23620:00

"Hey, uh, this has like the it takes

## 23620:00 - 23665:00

your clothes and it dedicate closes and

## 23665:00 - 23705:00

it has all those super programs and it

## 23705:00 - 23750:00

doesn't, uh, use too much water and not

## 23750:00 - 23790:00

use too much energy and no, it was just

## 23790:00 - 23835:00

like, hey, it just washes your clothes.

## 23835:00 - 23880:00

First level of sophistication. Today for

## 23880:00 - 23915:00

washing machines, we are at the fifth

## 23915:00 - 23955:00

level, which everybody knows about

## 23955:00 - 24000:00

washing machines. So the only way to

## 24000:00 - 24050:00

actually uh

## 24050:00 - 24095:00

be seen by a customer is by providing

## 24095:00 - 24135:00

something that is different that is

## 24135:00 - 24170:00

different from all the other competitors

## 24170:00 - 24215:00

that this specific customer want. It

## 24215:00 - 24250:00

kind of slightly differentiate the way

## 24250:00 - 24295:00

we talk. So for example here uh it's

## 24295:00 - 24340:00

skincare uh it's fourth level, fifth

## 24340:00 - 24390:00

level. Maybe if the product would be

## 24390:00 - 24435:00

like very innovative then we could say

## 24435:00 - 24465:00

okay that's third level. So, I don't

## 24465:00 - 24500:00

know. I I can't come up with creative

## 24500:00 - 24535:00

stuff, but I think you you know what I

## 24535:00 - 24565:00

mean.

## 24565:00 - 24600:00

You you don't have to use it, but it's

## 24600:00 - 24640:00

also a way to kind of uh changes

## 24640:00 - 24665:00

slightly the the message that you are

## 24665:00 - 24700:00

using. So, let's say third level or

## 24700:00 - 24780:00

fourth level and we are going to use um

## 24780:00 - 24865:00

punchy and we want u ch5

## 24865:00 - 24925:00

to use it. And then to create it what we

## 24925:00 - 24975:00

do is basically

## 24975:00 - 25040:00

we are going to drag that down

## 25040:00 - 25090:00

and change one variable if we want. We

## 25090:00 - 25125:00

can also just trying to try to create

## 25125:00 - 25185:00

that. But we can also say okay uh now I

## 25185:00 - 25220:00

don't want uh only this specific

## 25220:00 - 25260:00

messaging framework but I want to

## 25260:00 - 25285:00

generate

## 25285:00 - 25330:00

uh bold statements

## 25330:00 - 25360:00

here

## 25360:00 - 25400:00

and I want it I want the bold statements

## 25400:00 - 25450:00

to be actually standard. So this at this

## 25450:00 - 25495:00

point is for you or your team to think

## 25495:00 - 25540:00

of okay what are we testing in which

## 25540:00 - 25610:00

order and to generate uh one after the

## 25610:00 - 25645:00

other basically

## 25645:00 - 25700:00

and then let's uh put generate click

## 25700:00 - 25735:00

here which will trigger the web hook on

## 25735:00 - 25775:00

the back end which will uh actually

## 25775:00 - 25810:00

generate the different hooks and now you

## 25810:00 - 25860:00

can see it's generating so we can go

## 25860:00 - 25895:00

back uh in a few minutes and we will

## 25895:00 - 25945:00

have the hooks here. Okay, so there we

## 25945:00 - 25995:00

have it. Um, it has it it took like one

## 25995:00 - 26035:00

minute and uh at the same time I was

## 26035:00 - 26070:00

just looking into the other hooks and

## 26070:00 - 26100:00

try to find some interesting just to

## 26100:00 - 26135:00

show you. But those are the ones that

## 26135:00 - 26185:00

have been generated just now. Uh there

## 26185:00 - 26225:00

are some interesting uh beautiful even

## 26225:00 - 26265:00

when applied blind. Shaky hands steady

## 26265:00 - 26315:00

glows. Steady glow. So those are punchy.

## 26315:00 - 26355:00

Uh standard no mirror no problem.

## 26355:00 - 26390:00

Miracle bombs makes mistake impossible

## 26390:00 - 26440:00

and glow inevitable. So that might not

## 26440:00 - 26505:00

be the the best ever hooks, the ever

## 26505:00 - 26550:00

written hooks, but they are pretty good.

## 26550:00 - 26585:00

And when you start having a long list

## 26585:00 - 26615:00

because believe me, you can have you can

## 26615:00 - 26645:00

generate a bunch of them and you go

## 26645:00 - 26685:00

through them. Now that's the moment

## 26685:00 - 26725:00

where you need someone that is that

## 26725:00 - 26765:00

knows the product human being that is

## 26765:00 - 26805:00

good at understanding how the the

## 26805:00 - 26840:00

customer and that says okay this

## 26840:00 - 26870:00

resonates this not this resonate this

## 26870:00 - 26905:00

not and then you select it's not AI

## 26905:00 - 26945:00

testing thousands and thousands of ads

## 26945:00 - 26985:00

without control it's like it generates

## 26985:00 - 27015:00

something and then you can select you

## 27015:00 - 27070:00

can even uh change it if you want but

## 27070:00 - 27125:00

then before generating the ads you are

## 27125:00 - 27165:00

going to have a human looking into

## 27165:00 - 27215:00

But okay uh let's say now we want to

## 27215:00 - 27265:00

create those ones. uh so I am just

## 27265:00 - 27340:00

creating generate and here I am going to

## 27340:00 - 27380:00

check the templates that I've created

## 27380:00 - 27420:00

and those templates I have created them

## 27420:00 - 27480:00

within this tool uh templated which

## 27480:00 - 27515:00

basically is a tool that you can access

## 27515:00 - 27550:00

through an API a little bit complicated

## 27550:00 - 27605:00

but you probably know what it is um that

## 27605:00 - 27685:00

allows to take an image and to generate

## 27685:00 - 27730:00

let me show you so I took a picture from

## 27730:00 - 27785:00

transport beauty. Here I hide the the

## 27785:00 - 27845:00

existing hook and here instead I put a

## 27845:00 - 27925:00

text and this text is just a sample here

## 27925:00 - 27990:00

but it will be replaced by every hook

## 27990:00 - 28045:00

that I'm using here. So we will have the

## 28045:00 - 28070:00

same picture but then it will be

## 28070:00 - 28130:00

replaced by that. So if I look at here,

## 28130:00 - 28190:00

uh it also handle the size of the the

## 28190:00 - 28250:00

font depending on the size of the uh the

## 28250:00 - 28310:00

actual hook. It's auto fit here and it

## 28310:00 - 28380:00

will fill the hat uh which will be uh

## 28380:00 - 28405:00

important for us because this one for

## 28405:00 - 28445:00

example is long but we are going to have

## 28445:00 - 28510:00

like shorter hooks and this is what

## 28510:00 - 28560:00

works in the back end that we can get.

## 28560:00 - 28610:00

Uh here we create the templates and we

## 28610:00 - 28660:00

decide to use um one or other another

## 28660:00 - 28700:00

template. But basically you have you can

## 28700:00 - 28735:00

have a creative team or you can go ahead

## 28735:00 - 28760:00

and create a bunch of different

## 28760:00 - 28810:00

templates of ads that you know will work

## 28810:00 - 28865:00

and apply the hooks that you generate on

## 28865:00 - 28895:00

those templates. So now let's just

## 28895:00 - 28935:00

create them. So we have a long one and

## 28935:00 - 28995:00

two short ones. Let's go

## 28995:00 - 29065:00

and we move on to add creation. Here

## 29065:00 - 29140:00

they are.

## 29140:00 - 29190:00

And as you can see here,

## 29190:00 - 29225:00

shaking hand. And it looks fresh, not

## 29225:00 - 29260:00

fake.

## 29260:00 - 29320:00

And it creates. So why it creates two

## 29320:00 - 29365:00

six while I had three hooks I wanted to

## 29365:00 - 29405:00

create simply because I activated two

## 29405:00 - 29440:00

templates. So for each hook, it will

## 29440:00 - 29490:00

create two variations.

## 29490:00 - 29535:00

Uh let me show you a longer one here.

## 29535:00 - 29570:00

For example,

## 29570:00 - 29610:00

no mirror, no problem. Miracle bombs

## 29610:00 - 29640:00

makes mistake impossible and glow

## 29640:00 - 29685:00

inevitable. Awesome. That's exactly what

## 29685:00 - 29720:00

we want.

## 29720:00 - 29760:00

All right. And now we are we are in this

## 29760:00 - 29805:00

ad creation part of the system and we

## 29805:00 - 29840:00

can simply move on and create the ads.

## 29840:00 - 29880:00

So let's say I want to create first of

## 29880:00 - 29935:00

all I need to select the different the

## 29935:00 - 29995:00

adset I want to put those ads in. So I

## 29995:00 - 30030:00

need to first create the campaign and

## 30030:00 - 30080:00

then create the different adsets. It's

## 30080:00 - 30105:00

it's possible to create the adsets

## 30105:00 - 30150:00

automatically but we ended up realizing

## 30150:00 - 30190:00

that it was a lot better to give the

## 30190:00 - 30225:00

freedom to create the structure of the

## 30225:00 - 30270:00

campaign and only push the ads within

## 30270:00 - 30310:00

the adset that have been created

## 30310:00 - 30350:00

already. So for the sake of this example

## 30350:00 - 30410:00

I create adset one. So again there is an

## 30410:00 - 30450:00

automation that basically retrive the

## 30450:00 - 30485:00

adset that are existing in a specific

## 30485:00 - 30545:00

campaign and then I'm creating the ads.

## 30545:00 - 30595:00

So same thing

## 30595:00 - 30645:00

to create I click here triggers a web

## 30645:00 - 30700:00

hook and it starts creating the ads on

## 30700:00 - 30750:00

the back end.

## 30750:00 - 30800:00

So we can see so there are a lot of uh

## 30800:00 - 30830:00

waiting time here. So I'm going to pause

## 30830:00 - 30880:00

but because the if you create too many

## 30880:00 - 30920:00

ads at the same time then Facebook at

## 30920:00 - 30965:00

some point says it's enough. So as you

## 30965:00 - 31010:00

can see it works slowly but you can just

## 31010:00 - 31060:00

uh put 100 ads and then it will create

## 31060:00 - 31090:00

them one by one and then you can go

## 31090:00 - 31135:00

ahead later and check them out. So if I

## 31135:00 - 31200:00

go here so this is a old um

## 31200:00 - 31255:00

ad uh account that I was using. Let me

## 31255:00 - 31325:00

just find them. Programmative testing

## 31325:00 - 31395:00

ads set one. And here we have our ads.

## 31395:00 - 31440:00

Shaky hand steady glow is the picture we

## 31440:00 - 31485:00

wanted. And you can obviously use the

## 31485:00 - 31520:00

format that you want and so on and so

## 31520:00 - 31550:00

forth. So it's for you to decide which

## 31550:00 - 31585:00

campaign you use, what are the

## 31585:00 - 31630:00

structures of your adset and what ad you

## 31630:00 - 31665:00

want to push in each adset. Okay. So

## 31665:00 - 31705:00

there we go. We have ads running at this

## 31705:00 - 31790:00

point. So imagine you have 100 ads. Um,

## 31790:00 - 31830:00

Facebook decides which ones are the good

## 31830:00 - 31860:00

ones, the ones that resonate with the

## 31860:00 - 31900:00

customer. You find one or two winners

## 31900:00 - 31930:00

and then you come back here and you say,

## 31930:00 - 31975:00

"Okay, those ones are my winners." So,

## 31975:00 - 32015:00

what's the next step? Again, u I

## 32015:00 - 32040:00

mentioned it earlier, but you can

## 32040:00 - 32095:00

iterate. So, if you know that uh this ad

## 32095:00 - 32130:00

was a winner, then you know that this

## 32130:00 - 32185:00

angle pushing this USB, it works. So why

## 32185:00 - 32240:00

don't you just uh create new um

## 32240:00 - 32300:00

iteration of this? You can use new uh

## 32300:00 - 32350:00

imaging images uh with the same hooks.

## 32350:00 - 32400:00

You can use different ways to talk about

## 32400:00 - 32435:00

this specific marketing angle. But you

## 32435:00 - 32475:00

can basically iterate again and again to

## 32475:00 - 32515:00

push the same thing. That is only if you

## 32515:00 - 32565:00

use static ads. But what if you want to

## 32565:00 - 32595:00

do more about that? Then this is the

## 32595:00 - 32650:00

next step. This is a system that is

## 32650:00 - 32690:00

going to create a mini VSSL or a

## 32690:00 - 32745:00

textbased uh ad like something longer

## 32745:00 - 32790:00

that is written specifically based on

## 32790:00 - 32830:00

the hook that was performing. So, but

## 32830:00 - 32855:00

basically

## 32855:00 - 32920:00

we are using u different parameters from

## 32920:00 - 32965:00

the ones that we have used for the hooks

## 32965:00 - 33000:00

but some are the same. You still have

## 33000:00 - 33040:00

the USB that you want to use. You still

## 33040:00 - 33075:00

have the marketing angle. it was this

## 33075:00 - 33140:00

one the original hook. So let's say that

## 33140:00 - 33190:00

was my hook that was performing then I

## 33190:00 - 33260:00

will create I will take an an ad as an

## 33260:00 - 33295:00

inspiration. So here's a bunch of ads

## 33295:00 - 33340:00

that are known for performing. So let's

## 33340:00 - 33390:00

say I take this one and I want to select

## 33390:00 - 33440:00

a psychological trigger. Uh let's say

## 33440:00 - 33495:00

challenge the beliefs and I want to

## 33495:00 - 33565:00

create a specific emotion into my ads.

## 33565:00 - 33600:00

Uh, I want to use um design and

## 33600:00 - 33655:00

inspiration and I want a a bronze spoke

## 33655:00 - 33705:00

person that is the narrator. I want an

## 33705:00 - 33765:00

ad that is like 4 minute long and I want

## 33765:00 - 33825:00

the copyriter David David Ojv to write

## 33825:00 - 33890:00

it. Obviously, it's just uh to give some

## 33890:00 - 33965:00

uh clue to the AI and I want to talk to

## 33965:00 - 34005:00

people that are programmer aware on a

## 34005:00 - 34050:00

fourth level sophistication market and I

## 34050:00 - 34105:00

want chat GPT5 to create it. So, I'm

## 34105:00 - 34130:00

generating it and you will see the

## 34130:00 - 34220:00

result right away up. It's generating

## 34220:00 - 34255:00

done. It took only a few seconds. So,

## 34255:00 - 34290:00

you have the hook, the the lid, the

## 34290:00 - 34345:00

body, and the CTA. But to visualize it a

## 34345:00 - 34380:00

little bit better and to modify, then

## 34380:00 - 34435:00

you can u use that. It's a Google doc.

## 34435:00 - 34470:00

And this is basically your hook. It

## 34470:00 - 34500:00

always makes it in a way that's possible

## 34500:00 - 34535:00

to to speak it. So basically, you can

## 34535:00 - 34585:00

use this script to create a voice over

## 34585:00 - 34630:00

with B-roll ad. So no mirror, no

## 34630:00 - 34655:00

problem. Miracle bomb makes mistake

## 34655:00 - 34695:00

impossible and glow inevitable. Imagine

## 34695:00 - 34740:00

never again worrying for your blush when

## 34740:00 - 34765:00

went on too strong. never panicking

## 34765:00 - 34820:00

under the harsh office light that you

## 34820:00 - 34860:00

you can read it yourself. It's an ad

## 34860:00 - 34925:00

that is um again it can be modified but

## 34925:00 - 34975:00

this is a very good start that uses all

## 34975:00 - 35010:00

the parameters that you want and you

## 35010:00 - 35055:00

have a script you can um you can run

## 35055:00 - 35100:00

with. What do you do with this script?

## 35100:00 - 35125:00

That's a good question and as I said

## 35125:00 - 35160:00

it's still in the building. Uh I'm still

## 35160:00 - 35200:00

thinking of how we can automatically

## 35200:00 - 35260:00

create uh the ad with the B- rolls that

## 35260:00 - 35305:00

are available uh all the videos that the

## 35305:00 - 35365:00

brand have. Uh not there yet. So far the

## 35365:00 - 35440:00

only um the best way I found is to use

## 35440:00 - 35495:00

icon this specific product within icon.

## 35495:00 - 35530:00

I'll put the link in the description. Uh

## 35530:00 - 35590:00

but basically it's it allows to import

## 35590:00 - 35650:00

all your bureaus and just start with a

## 35650:00 - 35690:00

script. So you just take your script

## 35690:00 - 35725:00

that was written for you, put it into

## 35725:00 - 35770:00

this tool and then it will segment it in

## 35770:00 - 35810:00

different pieces, different sentences

## 35810:00 - 35855:00

and for each of them it will offer it

## 35855:00 - 35895:00

will find the the B-roll that you

## 35895:00 - 35940:00

already have that fits the best to the

## 35940:00 - 35975:00

specific piece of the script. So you can

## 35975:00 - 36005:00

have a very fast process. It's not

## 36005:00 - 36045:00

completely automated yet, but you can

## 36045:00 - 36120:00

generate uh scripts at scale scale quote

## 36120:00 - 36160:00

unquote based on specific parameters you

## 36160:00 - 36205:00

want to test. Take those scripts, put

## 36205:00 - 36270:00

them into icon and have someone that is

## 36270:00 - 36305:00

just attributing the right bureau,

## 36305:00 - 36355:00

creating a voice over with AI and then

## 36355:00 - 36400:00

write into the the ad account and test.

## 36400:00 - 36445:00

You can generate like 20 good ads per

## 36445:00 - 36505:00

day u minimum with a small team using

## 36505:00 - 36535:00

this method. So that's it for this

## 36535:00 - 36575:00

video. I hope you found it useful. I

## 36575:00 - 36610:00

hope it kind of reframed the way you

## 36610:00 - 36650:00

think of ads and now you don't see that

## 36650:00 - 36705:00

as a a creative guesswork that is

## 36705:00 - 36735:00

completely chaotic but instead you see

## 36735:00 - 36780:00

it as okay we actually can make a system

## 36780:00 - 36815:00

out of it. We actually can use different

## 36815:00 - 36850:00

parameters that we can test in a

## 36850:00 - 36915:00

structured way. So we will we will

## 36915:00 - 36965:00

logically find the right combination

## 36965:00 - 37005:00

that works with our customers because

## 37005:00 - 37040:00

that's is the message I really wanted

## 37040:00 - 37090:00

you to uh to get in this video. Uh

## 37090:00 - 37135:00

that's being said that being said uh I

## 37135:00 - 37170:00

will put in the description. So first of

## 37170:00 - 37230:00

all uh I talked briefly about how to go

## 37230:00 - 37255:00

with the gold nuggets and and if this

## 37255:00 - 37295:00

video that you just watched uh kind of

## 37295:00 - 37330:00

feel overwhelming you you would like to

## 37330:00 - 37380:00

create that but not at this level then I

## 37380:00 - 37415:00

will put in the description a video that

## 37415:00 - 37455:00

as I said will walk you through a

## 37455:00 - 37510:00

similar system but if you start from

## 37510:00 - 37555:00

scratch like if you don't have any uh

## 37555:00 - 37595:00

real knowledge in marketing then it will

## 37595:00 - 37650:00

just help you to go from like nothing to

## 37650:00 - 37700:00

very good copywriting and marketing uh

## 37700:00 - 37755:00

all at once only using simple LLM no

## 37755:00 - 37815:00

automation no Google spreadsheet just

## 37815:00 - 37850:00

simple prompts simple framework that you

## 37850:00 - 37885:00

follow and for it works for every type

## 37885:00 - 37920:00

of product business uh even service

## 37920:00 - 37955:00

business so the link in the description

## 37955:00 - 38005:00

I will also put the link of templated

## 38005:00 - 38055:00

and um icon in the descriptions in the

## 38055:00 - 38085:00

description those are affiliate link so

## 38085:00 - 38120:00

if you decide to use them it would be

## 38120:00 - 38150:00

really nice if you could use my

## 38150:00 - 38185:00

affiliate link. That's all for this

## 38185:00 - 38225:00

video. I see you in the next one.

## 38225:00+

Bye-bye.

