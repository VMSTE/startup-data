---
source: https://www.youtube.com/watch?v=DjF-Rvrmbk4
title: ai automation builds 100+ ads in 24hrs - research, creative, and data analytics
author: Cody Schneider
date: 2025-06-10
views: 5623
description: >-
  In this episode, Cody sits down with Jonathan Bach—Twitter’s breakout expert
  on AI-driven marketing automations—to cut through the “vibe marketing” hype
  and show exactly how real workflows get built and scaled. You’ll learn why
  true marketing expertise is the foundation for any automation, plus actionable
  tactics for:


  Automating Audience Research: Scrape and analyze Reddit and Twitter at scale
  to pinpoint customer pain points, trigger events, and exact language for your
  messaging.


  Bulk Creative Production: Use OpenAI’s Image Gen API (and soon video tools) to
  generate hundreds of ad variations, feeding algorithms with endless new
  assets.


  Performance Analysis at Scale: Build n8n flows (with sub-agents) to pull
  Facebook Ads data every few days, extract insights on top-performing
  campaigns, and even auto-draft new ad copy.


  Simplifying UX with Custom Front-Ends: Wrap complex n8n back-ends in
  user-friendly Bolt or Lovable interfaces so non-technical teammates can
  trigger workflows.


  Speeding Up Development with AI: Leverage Claude 4 or Perplexity to generate
  n8n JSON templates in one prompt, cutting hours off your build time.


  Timestamps

  (00:00) Intro & why marketing know-how is critical

  (02:45) Jonathan’s journey from manual ads to n8n automations

  (07:30) Your stack: n8n, Railway.com, Bolt/Lovable front-ends

  (12:15) Jonathan’s top 3 workflows: research, creative, analysis

  (18:00) Reddit scraping → structured marketing insights

  (25:40) Twitter scraping → viral content modeling

  (31:10) OpenAI Image Gen → bulk ad-variation workflows

  (38:20) Building custom UIs around n8n flows

  (44:50) Facebook Ads data → automated performance review & new-ad drafts

  (51:10) Video ads today & tomorrow (e.g. Google Veo3)

  (56:40) Using Claude/Perplexity to auto-generate n8n workflows


  Notable Quotes


  “You have to be an expert at that thing to build these automations. Then you
  can automate 80% of the work.” — Jonathan

  “I tell Claude what I want, and it gives me a 60–80% complete n8n workflow.” —
  Jonathan


  Actionable Takeaways


  Pick a core marketing process you know inside-out before automating.


  Automate audience research to inform your copy and creative.


  Bulk-generate and test creatives with AI-powered image (and soon video) tools.


  Set up recurring performance-analysis flows so you focus on decisions, not
  data collection.


  Build simple front-end UIs so your whole team can trigger automations.


  Use AI (Claude, Perplexity) to draft your workflow JSON and cut development
  time.


  Resources


  Nate Herk’s n8n tutorials: youtube.com/@nateherk


  Mark Kashef’s workflow deep dives: youtube.com/@Mark_Kashef


  AI GPT Workshop: youtube.com/@AI-GPTWorkshop/videos


  RapidAPI (third-party APIs): rapidapi.com


  Apify (web scraping): apify.com


  TwitterAPI.io (Twitter data): twitterapi.io


  Sponsored by TalentFiber: Hire US-trained offshore engineers at half the cost.
  Learn more at talentfiber.com.
tags:
  - cody schneider
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T11:53:08.849Z
---

# ai automation builds 100+ ads in 24hrs - research, creative, and data analytics

## 00:00 - 20:00

Everybody's talking about Vibe

## 20:00 - 45:00

Marketing, but it's basically all

## 45:00 - 70:00

vaporware. It's very rare that you

## 70:00 - 110:00

actually see people that understand what

## 110:00 - 140:00

they're doing. This is another one of

## 140:00 - 165:00

those episodes that's talking to an

## 165:00 - 190:00

individual that's actually building

## 190:00 - 220:00

these out at scale, actually

## 220:00 - 255:00

implementing these within his workflows

## 255:00 - 280:00

and his process, who's an expert in this

## 280:00 - 300:00

thing. I think the biggest thing for

## 300:00 - 330:00

people to understand is that you have to

## 330:00 - 365:00

understand marketing to automate a

## 365:00 - 390:00

process, right? So, you have to be an

## 390:00 - 415:00

expert at that thing to be able to go

## 415:00 - 430:00

and actually build out these

## 430:00 - 460:00

automations. But when you do that, you

## 460:00 - 495:00

can automate 80% of the work that you

## 495:00 - 525:00

previously were doing. Like all the tool

## 525:00 - 550:00

sets are available. And really in the

## 550:00 - 570:00

last three months has this become

## 570:00 - 595:00

possible. Today I'm hosting my friend

## 595:00 - 645:00

Jonathan. He is going insanely viral on

## 645:00 - 670:00

Twitter right now with the marketing

## 670:00 - 700:00

automations that he's building using

## 700:00 - 740:00

NADN and a bunch of piec together APIs.

## 740:00 - 760:00

You're going to learn how to do audience

## 760:00 - 800:00

research at scale to understand how your

## 800:00 - 830:00

customer talks and what pain points they

## 830:00 - 855:00

have. specifically, he's scraping

## 855:00 - 885:00

Reddit, pulling in all of that data, and

## 885:00 - 925:00

then analyzing it for all the insights

## 925:00 - 950:00

related to your audience and the product

## 950:00 - 970:00

that you're trying to promote. He's

## 970:00 - 985:00

going to share with us how to make

## 985:00 - 1010:00

creative at scale. We're going to talk

## 1010:00 - 1035:00

about the principles of why you should

## 1035:00 - 1060:00

be creating a bunch of different

## 1060:00 - 1095:00

variations of creative now that for you

## 1095:00 - 1135:00

page content is kind of ruling the

## 1135:00 - 1180:00

world. Broad targeting and more creative

## 1180:00 - 1205:00

is more effective at creating the

## 1205:00 - 1230:00

outcomes that you're looking for than

## 1230:00 - 1265:00

really defined audiences and less volume

## 1265:00 - 1290:00

of creative. Finally, he's going to

## 1290:00 - 1325:00

share some of the automations that he's

## 1325:00 - 1355:00

starting to experiment with for the

## 1355:00 - 1385:00

actual data analysis of what's working,

## 1385:00 - 1415:00

why it's working, etc. And also share

## 1415:00 - 1435:00

how to get started with this, where do

## 1435:00 - 1465:00

you even begin, how do you learn this,

## 1465:00 - 1500:00

and specifically how to use stuff like

## 1500:00 - 1540:00

perplexity AI with Claude 4 to go and

## 1540:00 - 1585:00

write complex NAND JSON outputs that you

## 1585:00 - 1620:00

can then just copy and paste into an NAN

## 1620:00 - 1645:00

to create the visualization. If you're

## 1645:00 - 1675:00

listening to this on the podcast, I

## 1675:00 - 1705:00

would highly suggest going and watching

## 1705:00 - 1730:00

it on YouTube for the second half of

## 1730:00 - 1765:00

this video. The majority of it is a lot

## 1765:00 - 1785:00

of screen sharing, so you'll want to see

## 1785:00 - 1810:00

that. And then finally, if you're trying

## 1810:00 - 1845:00

to hire engineers for your startup, go

## 1845:00 - 1885:00

to talentfiber.com to hire the best

## 1885:00 - 1920:00

offshore talent. They place 300 plus

## 1920:00 - 1945:00

engineers for startups. You can get

## 1945:00 - 1985:00

engineers with US experience that have

## 1985:00 - 2025:00

worked for the last 7 plus years, have

## 2025:00 - 2060:00

perfect English, work US time zones, and

## 2060:00 - 2090:00

are embedded with your team for half the

## 2090:00 - 2120:00

cost of a US equivalent. We're getting

## 2120:00 - 2160:00

people for 5,500 as an example, or I've

## 2160:00 - 2190:00

seen that. And the best part is they

## 2190:00 - 2230:00

function as a outsourced HR department.

## 2230:00 - 2255:00

So they do all the technical interviews.

## 2255:00 - 2290:00

They actually find you people that know

## 2290:00 - 2315:00

how to do what they say they do. So by

## 2315:00 - 2340:00

the time that you're even talking to

## 2340:00 - 2360:00

candidates, it's really just a vibe

## 2360:00 - 2380:00

check. Do you want to work with them on

## 2380:00 - 2425:00

a daily basis, etc. Go to townfr.com to

## 2425:00 - 2445:00

learn more. And with that said, let's

## 2445:00 - 2500:00

get started with today's show.

## 2500:00 - 2625:00

[Music]

## 2625:00 - 2645:00

Jonathan, what's good, man? How you

## 2645:00 - 2670:00

doing? What's going on? What's going on?

## 2670:00 - 2710:00

We're here. Hell yeah. I've been looking

## 2710:00 - 2740:00

forward to this, man. all weekend. Um I

## 2740:00 - 2760:00

was traveling this weekend. I was just

## 2760:00 - 2805:00

telling you about it. But um I think you

## 2805:00 - 2830:00

know there's a lot of people talking

## 2830:00 - 2870:00

about a you know AI automations or a

## 2870:00 - 2895:00

like vibe marketing, right? I feel like

## 2895:00 - 2930:00

is this like vaporware term that's

## 2930:00 - 2965:00

thrown around right now. Nobody is

## 2965:00 - 2990:00

actually doing this. Like it's very rare

## 2990:00 - 3020:00

that I actually talk to somebody that's

## 3020:00 - 3055:00

building out um you know systems and

## 3055:00 - 3080:00

processes. And really what it comes down

## 3080:00 - 3100:00

to is a lot of people don't know how to

## 3100:00 - 3140:00

market first off. So they can't define a

## 3140:00 - 3165:00

process. And if they can't define a

## 3165:00 - 3185:00

process, how can they go and automate

## 3185:00 - 3205:00

it? Right? Like I see all these

## 3205:00 - 3225:00

engineers a lot of the times trying to

## 3225:00 - 3255:00

build AI agents that do marketing and

## 3255:00 - 3285:00

it's they're not even doing marketing.

## 3285:00 - 3305:00

It's not even doing a marketing

## 3305:00 - 3340:00

activity. So I'm I think to start I'd

## 3340:00 - 3370:00

love to learn like how how did you get

## 3370:00 - 3410:00

into this piece of this like on the AI

## 3410:00 - 3435:00

you know doing the automation stuff for

## 3435:00 - 3460:00

for marketing? I know your your

## 3460:00 - 3495:00

background specifically in um uh paid

## 3495:00 - 3530:00

ads management. Yes. So I'm curious like

## 3530:00 - 3555:00

when you got when you started using

## 3555:00 - 3580:00

these uh automations within your

## 3580:00 - 3605:00

workflows like was it in the last six

## 3605:00 - 3640:00

months? Was it more recently? I feel for

## 3640:00 - 3675:00

us uh we saw in like the last like three

## 3675:00 - 3710:00

months something got better that just

## 3710:00 - 3735:00

got smarter and so it's like way more

## 3735:00 - 3755:00

useful to use it. But I'm curious what

## 3755:00 - 3790:00

you're seeing on your side. Yeah, I

## 3790:00 - 3815:00

definitely I I definitely feel like in

## 3815:00 - 3840:00

the past 3 months for sure I feel like

## 3840:00 - 3865:00

things have really started to go I guess

## 3865:00 - 3910:00

like even more exponential. I say I I've

## 3910:00 - 3940:00

probably been playing around with this

## 3940:00 - 3975:00

since the the start of the year. That's

## 3975:00 - 3995:00

kind of like when I started looking into

## 3995:00 - 4040:00

like workflows and ended specifically. I

## 4040:00 - 4085:00

actually started off by hiring a

## 4085:00 - 4125:00

different um automation team to build

## 4125:00 - 4185:00

out a workflow for me on the paid ads or

## 4185:00 - 4225:00

um yeah creative and advertising side of

## 4225:00 - 4245:00

things where I wanted to kind of like

## 4245:00 - 4265:00

automate a little bit of the reporting

## 4265:00 - 4300:00

and also a little bit of the I guess

## 4300:00 - 4340:00

like daytoday insights that you can pull

## 4340:00 - 4370:00

from like ads manager stuff like that.

## 4370:00 - 4405:00

So I actually ended up hiring them to

## 4405:00 - 4445:00

build out a pretty complex workflow

## 4445:00 - 4510:00

which was very helpful. Um, and that

## 4510:00 - 4560:00

kind of like inspired me to like dive a

## 4560:00 - 4590:00

little deeper and kind of like figure

## 4590:00 - 4620:00

out what options are possible and kind

## 4620:00 - 4645:00

like what we can actually do with these

## 4645:00 - 4685:00

tools because I mean I I just saw like

## 4685:00 - 4710:00

the I can show you later the the flow

## 4710:00 - 4735:00

that they built and like it was just

## 4735:00 - 4765:00

like this huge thing and I was like oh

## 4765:00 - 4810:00

my god this is this is actually insane.

## 4810:00 - 4840:00

Um what's what's actually possible with

## 4840:00 - 4870:00

these tools now? Um cuz like we were

## 4870:00 - 4890:00

pulling creative reports, we were

## 4890:00 - 4915:00

pulling kind of like scaling

## 4915:00 - 4950:00

recommendations, writing new ad copy. it

## 4950:00 - 4990:00

was like this whole giant thing. So

## 4990:00 - 5025:00

yeah, I saw that and that kind of like

## 5025:00 - 5050:00

triggered something inside of me that

## 5050:00 - 5085:00

was like, okay, I think this is like

## 5085:00 - 5125:00

really something to look into. So yeah,

## 5125:00 - 5150:00

I used that workflow for a little bit.

## 5150:00 - 5195:00

Um, and then I just decided like, okay,

## 5195:00 - 5225:00

I can either keep hiring someone else to

## 5225:00 - 5250:00

kind of like build out these things for

## 5250:00 - 5285:00

me or I can try to like double down on

## 5285:00 - 5310:00

this myself and really understand

## 5310:00 - 5350:00

because yeah, I feel like that

## 5350:00 - 5380:00

understanding kind of learning what

## 5380:00 - 5410:00

these automations can do for you now

## 5410:00 - 5440:00

makes a lot of sense. So you you're kind

## 5440:00 - 5470:00

of like ahead of the curve and I like

## 5470:00 - 5495:00

always staying up to date on what's new

## 5495:00 - 5520:00

so you don't have to like always pay

## 5520:00 - 5555:00

someone else to do this for you. So

## 5555:00 - 5585:00

yeah, long story short, just started

## 5585:00 - 5635:00

like diving through like classic YouTube

## 5635:00 - 5680:00

tutorials, walkthrough, beginner guides,

## 5680:00 - 5700:00

joined a couple of school communities

## 5700:00 - 5725:00

and that's kind of like how I got

## 5725:00 - 5755:00

started with Yeah. specifically and it

## 5755:00 - 5800:00

ended like workflows uh in particular.

## 5800:00 - 5835:00

Yeah. any any resources on the learning

## 5835:00 - 5860:00

side specifically like school

## 5860:00 - 5890:00

communities or stuff like that or even

## 5890:00 - 5910:00

YouTube channels that you feel like is

## 5910:00 - 5940:00

are making good content like specific

## 5940:00 - 5980:00

ones? 100%. I can uh send some over to

## 5980:00 - 6005:00

you so you can link them later. But for

## 6005:00 - 6055:00

sure yeah Nate Herk is is probably the

## 6055:00 - 6080:00

main one that I've watched a lot. He has

## 6080:00 - 6130:00

a lot of amazing like beginner like full

## 6130:00 - 6165:00

step-by-step walkthroughs or like un

## 6165:00 - 6190:00

like actually from start to finish

## 6190:00 - 6230:00

learning how to not just like build

## 6230:00 - 6260:00

workflows in N&M but actually just like

## 6260:00 - 6275:00

understanding all the different

## 6275:00 - 6300:00

components cuz like there are a lot of

## 6300:00 - 6325:00

moving pieces and things to understand

## 6325:00 - 6365:00

right so you you can't really just like

## 6365:00 - 6400:00

hop in especially for Nadm which is a

## 6400:00 - 6430:00

little bit more complex than like a make

## 6430:00 - 6480:00

or or a gum loop you do kind of like

## 6480:00 - 6510:00

need to understand a little bit of the I

## 6510:00 - 6555:00

guess like technical uh things

## 6555:00 - 6605:00

underneath it. So yeah, he he is uh

## 6605:00 - 6660:00

probably the the YouTube he has a school

## 6660:00 - 6695:00

community as well, which I recommend uh

## 6695:00 - 6735:00

the most, I would say. Awesome. Cool.

## 6735:00 - 6760:00

No, I'll link that for sure. Um I just

## 6760:00 - 6810:00

found his YouTube channel. So um I'd

## 6810:00 - 6835:00

love to hear about your stack kind of

## 6835:00 - 6865:00

like the technical components of this of

## 6865:00 - 6895:00

how how are you deploying this? Um like

## 6895:00 - 6920:00

what we're doing currently is using

## 6920:00 - 6950:00

railway.com and then just running an

## 6950:00 - 6985:00

instance basically um for all the

## 6985:00 - 7015:00

automations that we're building. Um, we

## 7015:00 - 7050:00

found that to be the kind of the easiest

## 7050:00 - 7080:00

way to do it. Basically, log in with

## 7080:00 - 7110:00

GitHub, they give you like $5 of free

## 7110:00 - 7145:00

credits to like get started. Um, you

## 7145:00 - 7180:00

install N8, it's like three clicks

## 7180:00 - 7210:00

basically to have it with workers. Um,

## 7210:00 - 7240:00

but I'm curious what you're using uh

## 7240:00 - 7260:00

kind of at the scale that you're doing.

## 7260:00 - 7280:00

I know you're doing it at like a way

## 7280:00 - 7320:00

larger scale than than the average

## 7320:00 - 7345:00

person. So, yeah. Yeah. I mean, I'm

## 7345:00 - 7375:00

honestly not even that like I guess

## 7375:00 - 7400:00

fancy with it. So, for the most part,

## 7400:00 - 7425:00

I'm just like running them inside of

## 7425:00 - 7465:00

Naden just like trigger like just Yeah.

## 7465:00 - 7500:00

Uh, firing. You're using their paid

## 7500:00 - 7535:00

hosting just like their Yeah, I'm using

## 7535:00 - 7550:00

their paid hosting and then I'm just

## 7550:00 - 7585:00

like firing in everything like within

## 7585:00 - 7625:00

trigger nodes inside of N. I am actually

## 7625:00 - 7655:00

in the process now of kind of like

## 7655:00 - 7705:00

building out custom um UI frontends

## 7705:00 - 7725:00

using like bolt and kind like vibe

## 7725:00 - 7750:00

coding a little bit more just kind like

## 7750:00 - 7790:00

have a cool um interface for the

## 7790:00 - 7810:00

workflows. I think especially like if

## 7810:00 - 7840:00

you're going to start, you know, having

## 7840:00 - 7870:00

other people use these workflows, it

## 7870:00 - 7890:00

makes a lot of sense to kind of like

## 7890:00 - 7930:00

have a a bit of a cleaner front end for

## 7930:00 - 7955:00

them to interact with so they don't have

## 7955:00 - 7990:00

to like go into edit and do that. So

## 7990:00 - 8020:00

yeah, that's something I'm I'm uh

## 8020:00 - 8050:00

working on right now as well. But for

## 8050:00 - 8080:00

the most part or like for the actual uh

## 8080:00 - 8110:00

flows that I use daily, I would say I

## 8110:00 - 8170:00

just use and end for now. Nice. Nice. Um

## 8170:00 - 8215:00

the So just to give people context of

## 8215:00 - 8240:00

like what you can do with this, like

## 8240:00 - 8275:00

what are your top three, you know,

## 8275:00 - 8300:00

workflows that you're using specifically

## 8300:00 - 8345:00

for marketing? Um I I you talked to me

## 8345:00 - 8390:00

previously about uh your like bulk ad

## 8390:00 - 8440:00

generator y uh system. Um, so may maybe

## 8440:00 - 8465:00

uh talk through that and may some of the

## 8465:00 - 8485:00

other ones that you're using most both

## 8485:00 - 8510:00

for yourself and for clients or or what

## 8510:00 - 8535:00

have people also been most interested

## 8535:00 - 8565:00

in? I mean your Twitter is growing like

## 8565:00 - 8595:00

crazy. It's wild. I feel like I every

## 8595:00 - 8620:00

day or every other day that I see you

## 8620:00 - 8650:00

pop up and look at it, it's like another

## 8650:00 - 8685:00

thousand followers that follow you. So I

## 8685:00 - 8710:00

feel like this category people don't

## 8710:00 - 8745:00

understand like how much people want to

## 8745:00 - 8805:00

like to do uh like AI automation for

## 8805:00 - 8855:00

marketing like marketing uh uh tactics.

## 8855:00 - 8885:00

Uh, so anyway, I I I'd love to learn

## 8885:00 - 8905:00

like what you're seeing people be

## 8905:00 - 8930:00

receptive to and also what you're using

## 8930:00 - 8970:00

most. Yep. I guess probably a little bit

## 8970:00 - 9010:00

just due to to my I guess like core

## 9010:00 - 9055:00

audience being like uh advertisers and

## 9055:00 - 9095:00

kind of like Yeah. D brand. So for me,

## 9095:00 - 9140:00

I've seen a lot of traction with either

## 9140:00 - 9175:00

like um creative research and kind of

## 9175:00 - 9205:00

like avatar audience research and kind

## 9205:00 - 9235:00

of like marketing insights. That's uh

## 9235:00 - 9260:00

that's a big one. And the other one is

## 9260:00 - 9285:00

obviously like creative production. So

## 9285:00 - 9345:00

like using uh uh OpenAI's image gen API

## 9345:00 - 9390:00

to create static ads automatically. Um

## 9390:00 - 9420:00

I'm working on like another one right

## 9420:00 - 9445:00

now which is kind of like a video scroll

## 9445:00 - 9475:00

stopper. We discussed that on our last

## 9475:00 - 9495:00

call as well to kind of like create

## 9495:00 - 9545:00

video like hooks for uh video ads. That

## 9545:00 - 9570:00

one is almost finished. But yeah, I

## 9570:00 - 9600:00

would say the the top two or top three

## 9600:00 - 9645:00

are like marketing insights uh

## 9645:00 - 9710:00

generating new copy and new um hooks for

## 9710:00 - 9745:00

ads. And then lastly, like creative

## 9745:00 - 9795:00

production on the uh like image and then

## 9795:00 - 9825:00

soon video side of things as well. Video

## 9825:00 - 9850:00

is obviously a lot harder just due to

## 9850:00 - 9875:00

kind of like the models that are that

## 9875:00 - 9910:00

are out there right now. Images and

## 9910:00 - 9940:00

static ads are a lot easier to kind of

## 9940:00 - 9970:00

just prompt and and and get working

## 9970:00 - 10020:00

right away. But I think soon, very soon

## 10020:00 - 10050:00

videos are going to be like working

## 10050:00 - 10075:00

really well too. And then it's that's

## 10075:00 - 10100:00

going to be like a a total game changer.

## 10100:00 - 10145:00

Obviously like with Google VO3, I mean

## 10145:00 - 10175:00

that's that's insane. So I don't have

## 10175:00 - 10200:00

access yet unfortunately over here in

## 10200:00 - 10230:00

Norway but yeah just from what I've seen

## 10230:00 - 10270:00

it looks it looks insane. So yeah once

## 10270:00 - 10295:00

like you're able to integrate those

## 10295:00 - 10330:00

workflows in like an ended end as well I

## 10330:00 - 10355:00

think it's going to be it's going to be

## 10355:00 - 10385:00

crazy. But yeah I would say yeah um

## 10385:00 - 10440:00

audience research and um creative like

## 10440:00 - 10480:00

production are the top two kind of like

## 10480:00 - 10510:00

segments that I'm uh seeing a lot of

## 10510:00 - 10530:00

people interested in for me at the

## 10530:00 - 10565:00

moment. No, that makes total sense too,

## 10565:00 - 10600:00

right? It's like historically, you know,

## 10600:00 - 10655:00

when I was doing uh paid ads management

## 10655:00 - 10685:00

for for companies at scale, like I mean

## 10685:00 - 10720:00

we try to go and make like a 100 plus

## 10720:00 - 10745:00

variations of create actually, it's

## 10745:00 - 10765:00

funny, I'm doing this right now actually

## 10765:00 - 10800:00

for a mobile application. Um we're just

## 10800:00 - 10835:00

doing like AI avatar variations with

## 10835:00 - 10860:00

like different hook, different painpoint

## 10860:00 - 10900:00

combinations. Um and then using the hey

## 10900:00 - 10935:00

gen API basically to like go bulk and go

## 10935:00 - 10990:00

bulk generate all these videos. Um, but

## 10990:00 - 11045:00

the, you know, anymore these ad channels

## 11045:00 - 11080:00

are so effective at finding the right

## 11080:00 - 11100:00

people if you have like the correct

## 11100:00 - 11125:00

conversion event set up. So like what

## 11125:00 - 11145:00

we're doing is basically having a

## 11145:00 - 11195:00

conversion event on the free trial start

## 11195:00 - 11240:00

uh um uh user action like in the mobile

## 11240:00 - 11275:00

application, sending that event back and

## 11275:00 - 11310:00

then really your job as a a marketer or

## 11310:00 - 11340:00

an advertiser is just like finding the

## 11340:00 - 11370:00

creative that actually gets that event

## 11370:00 - 11405:00

to happen as cheaply as possible, right?

## 11405:00 - 11445:00

So your game turns into like creative

## 11445:00 - 11485:00

development and testing rather than uh

## 11485:00 - 11520:00

you know audience definition or

## 11520:00 - 11565:00

understanding which I think is a for me

## 11565:00 - 11595:00

it's been a mind switch. You know I I

## 11595:00 - 11620:00

I've been doing this 10 years so it's it

## 11620:00 - 11665:00

I'm from the the um you know the vintage

## 11665:00 - 11700:00

of of marketers with Facebook ads where

## 11700:00 - 11735:00

it's like super complex you know

## 11735:00 - 11755:00

targeting that was the only way that you

## 11755:00 - 11800:00

would actually get better. Totally. Um

## 11800:00 - 11830:00

but anyway you you mentioned something

## 11830:00 - 11855:00

uh a minute ago and I just want to come

## 11855:00 - 11885:00

back to it. uh this idea of like

## 11885:00 - 11935:00

connecting frontends to N8 end flows.

## 11935:00 - 11955:00

I've seen people doing this where they

## 11955:00 - 11985:00

like use lovable basically to build like

## 11985:00 - 12040:00

the front end uh kind of application. I

## 12040:00 - 12060:00

don't know what you would call it or UI

## 12060:00 - 12100:00

of the of the flow and then N is

## 12100:00 - 12145:00

basically the the backend uh that's like

## 12145:00 - 12175:00

actually doing the functions. Could you

## 12175:00 - 12200:00

talk about that more and kind of like

## 12200:00 - 12225:00

how you're setting that up, how you're

## 12225:00 - 12260:00

using it? Yeah, for sure. I mean, again,

## 12260:00 - 12290:00

it's not something I've done uh a lot

## 12290:00 - 12335:00

yet, but um what I'm basically doing

## 12335:00 - 12360:00

right now is is pretty much exactly what

## 12360:00 - 12385:00

you said. So, you have a working

## 12385:00 - 12445:00

automation inside of Nen. Um and then

## 12445:00 - 12475:00

instead of like so like yeah, for the

## 12475:00 - 12520:00

most part like I I uh fire all of these

## 12520:00 - 12560:00

flows like on a on a like a form submit.

## 12560:00 - 12600:00

So like for example for the for for

## 12600:00 - 12625:00

Reddit scraper like you add in the

## 12625:00 - 12655:00

keyword that you want to scrape and then

## 12655:00 - 12690:00

you send that over to like Reddit's API

## 12690:00 - 12735:00

scraper tool and then and it uh scrapes

## 12735:00 - 12790:00

entire um yeah post based on based on

## 12790:00 - 12825:00

the keyword but instead of like instead

## 12825:00 - 12870:00

of firing the flow based on a form that

## 12870:00 - 12900:00

you have inside of nen you can kind of

## 12900:00 - 12955:00

like have a uh a UI inside of a lovable

## 12955:00 - 12985:00

or or bolt which I'm using and then kind

## 12985:00 - 13015:00

of like have a custom UI where you have

## 13015:00 - 13040:00

like the form there instead and then you

## 13040:00 - 13090:00

pass the the keyword that you submit

## 13090:00 - 13125:00

through bolt over into n and then that

## 13125:00 - 13160:00

triggers the flow instead. So it's

## 13160:00 - 13185:00

basically just kind of like beautifying

## 13185:00 - 13225:00

the the flow a little bit. But I mean

## 13225:00 - 13270:00

there's tons of there's tons of uh I

## 13270:00 - 13295:00

guess like customizations and ways you

## 13295:00 - 13330:00

can kind of like

## 13330:00 - 13365:00

uh visually present the output as well

## 13365:00 - 13385:00

which I'm also interested in because

## 13385:00 - 13425:00

like there's obviously you're kind of

## 13425:00 - 13450:00

limited inside of edit in and kind of

## 13450:00 - 13500:00

like how you I guess present the the the

## 13500:00 - 13535:00

data or the output that you get. For the

## 13535:00 - 13565:00

most part I'm just like using a Google

## 13565:00 - 13600:00

sheet for kind of like the output in

## 13600:00 - 13640:00

terms of like uh yeah the like copy or

## 13640:00 - 13675:00

marketing insights or whatever. But if

## 13675:00 - 13715:00

you pass that data back to like a Bolt,

## 13715:00 - 13750:00

you can present it a lot, I guess, like

## 13750:00 - 13800:00

cooler, if that makes sense. No, 100%.

## 13800:00 - 13825:00

Yeah, I I I'm just thinking about it is

## 13825:00 - 13850:00

like, you know, if you're doing bulk

## 13850:00 - 13890:00

image generation for uh you know, image

## 13890:00 - 13925:00

ads, pulling that back into a dashboard,

## 13925:00 - 13950:00

you know, maybe there's some type of I

## 13950:00 - 14000:00

am working I am working on that on uh

## 14000:00 - 14035:00

for a video uh flow right now. It's not

## 14035:00 - 14080:00

done yet, but I can see No, I don't have

## 14080:00 - 14110:00

that saved. I can show you the one that

## 14110:00 - 14135:00

I'm building a little bit later if you

## 14135:00 - 14170:00

want for like a Tik Tok marketing

## 14170:00 - 14195:00

insights where you basically just like I

## 14195:00 - 14245:00

said you you submit the um you submit

## 14245:00 - 14280:00

the the keywords uh and the amount of

## 14280:00 - 14305:00

videos that you want to scrape and then

## 14305:00 - 14335:00

you give a product uh description and

## 14335:00 - 14365:00

then it's it scrapes the videos based on

## 14365:00 - 14400:00

that like pulls pain points trigger

## 14400:00 - 14435:00

events and rewrites the script from the

## 14435:00 - 14460:00

scraped videos and then sends everything

## 14460:00 - 14500:00

back. So I can show unreal. Absolutely.

## 14500:00 - 14525:00

Yeah. I think the like second half of

## 14525:00 - 14555:00

this will just go through all the flows

## 14555:00 - 14585:00

that you built because I think for sure

## 14585:00 - 14615:00

for a lot of people it'll kind of give

## 14615:00 - 14655:00

uh you know really a jump point of like

## 14655:00 - 14680:00

what's possible or like what people are

## 14680:00 - 14710:00

thinking about with this and I I think

## 14710:00 - 14740:00

that's the you know the biggest hurdle

## 14740:00 - 14765:00

right now currently for marketers is

## 14765:00 - 14790:00

like they know it exists but they don't

## 14790:00 - 14810:00

really know what are the actual like

## 14810:00 - 14855:00

tactical implementations of this um and

## 14855:00 - 14880:00

so anyway yeah I think second half of

## 14880:00 - 14910:00

this video we'll just have you screen

## 14910:00 - 14930:00

share and talk through kind of some of

## 14930:00 - 14975:00

the automations but sounds good um cool

## 14975:00 - 15035:00

okay so companywise I the talk to me

## 15035:00 - 15060:00

about how you're implementing this

## 15060:00 - 15085:00

within your business. So you do paid ads

## 15085:00 - 15125:00

management for e-commerce brands from my

## 15125:00 - 15160:00

understanding. Um hit you know what were

## 15160:00 - 15190:00

you doing before and then like what has

## 15190:00 - 15230:00

this solved now like why you know why

## 15230:00 - 15255:00

why are why why are we even talking

## 15255:00 - 15290:00

about this today? Yeah you know what's

## 15290:00 - 15315:00

the purpose of the implementation within

## 15315:00 - 15335:00

the business for you know anybody that's

## 15335:00 - 15380:00

listening. So I mean like you said with

## 15380:00 - 15410:00

the with the image gen thing that you're

## 15410:00 - 15430:00

working on like I mean obviously just

## 15430:00 - 15460:00

like volume creative volume right now is

## 15460:00 - 15485:00

huge with advertising in general just

## 15485:00 - 15510:00

like the more you can feed the algo and

## 15510:00 - 15540:00

that's just going to get get bigger or

## 15540:00 - 15570:00

more and more important. So just the

## 15570:00 - 15605:00

more I guess like yeah creative output

## 15605:00 - 15645:00

and variation that you can generate the

## 15645:00 - 15670:00

the more you can just feed that back

## 15670:00 - 15700:00

into Facebook and obviously like you're

## 15700:00 - 15715:00

not going to be able to generate all

## 15715:00 - 15760:00

that manually yourself. So being able to

## 15760:00 - 15790:00

just have these tools that can pretty

## 15790:00 - 15850:00

much just like 10x 100x your own manual

## 15850:00 - 15875:00

output is kind of like how I'm seeing

## 15875:00 - 15910:00

it. So it's it's kind of like just

## 15910:00 - 15955:00

having an extension of yourself and um

## 15955:00 - 15995:00

yeah just maximizing output and also I

## 15995:00 - 16025:00

mean obvious like obviously just saving

## 16025:00 - 16060:00

time, right? And just like having having

## 16060:00 - 16100:00

these workflows run 247 automatically

## 16100:00 - 16125:00

just spit things out inside inside of

## 16125:00 - 16150:00

these work uh inside of these sheets and

## 16150:00 - 16175:00

inside of these databases. So you don't

## 16175:00 - 16210:00

have to do all that manually. you just

## 16210:00 - 16245:00

have a compilation of of sheets and

## 16245:00 - 16270:00

databases and things that that are

## 16270:00 - 16300:00

presented to you on like a daily or

## 16300:00 - 16325:00

weekly basis, whatever, and then you can

## 16325:00 - 16350:00

just kind of like skim through

## 16350:00 - 16370:00

everything, take what you need, and then

## 16370:00 - 16415:00

just run with that. So, yeah, for me it

## 16415:00 - 16435:00

and again, I think we discussed this on

## 16435:00 - 16470:00

our last call, too. I mean, also right

## 16470:00 - 16505:00

now, I'm not even like super super

## 16505:00 - 16550:00

worried about the actual output of these

## 16550:00 - 16595:00

agents in a lot of cases because I mean,

## 16595:00 - 16620:00

sure, they're somewhat limited in terms

## 16620:00 - 16650:00

of like the the tech and the output like

## 16650:00 - 16690:00

obviously in terms of especially like on

## 16690:00 - 16715:00

the video side of thing for creative

## 16715:00 - 16785:00

like it's not amazing yet, but it likely

## 16785:00 - 16820:00

will be and it will likely be pretty

## 16820:00 - 16850:00

soon, right? So I'm also kind of like in

## 16850:00 - 16885:00

the mindset of like getting ahead of the

## 16885:00 - 16915:00

curve right now and understanding the

## 16915:00 - 16945:00

logic and the and the tools and kind of

## 16945:00 - 16980:00

like how to build it these yeah these

## 16980:00 - 17015:00

agents or these workflows. So when the

## 17015:00 - 17040:00

output kind of like goes really

## 17040:00 - 17075:00

exponential then you're already like

## 17075:00 - 17120:00

really good position to kind like really

## 17120:00 - 17165:00

um take advantage of the flows. Totally.

## 17165:00 - 17190:00

Yeah. I think the thing that people get

## 17190:00 - 17225:00

hung up on right now is like maybe it's

## 17225:00 - 17250:00

not perfect, right? But like then your

## 17250:00 - 17285:00

job all it should be is like a curator,

## 17285:00 - 17315:00

right? rather than being the, you know,

## 17315:00 - 17345:00

the grunt labor for the production. I

## 17345:00 - 17365:00

mean, I think about a marketer, right?

## 17365:00 - 17405:00

Like it, and again, everybody has done

## 17405:00 - 17420:00

this where it's like, okay, I want to

## 17420:00 - 17455:00

make 10 variations of ad creative, like

## 17455:00 - 17480:00

that's a slog to go and generate like

## 17480:00 - 17545:00

each of those variations. Um, the the

## 17545:00 - 17570:00

real power of this is like, okay, cool.

## 17570:00 - 17600:00

If I can have every, you know, all the

## 17600:00 - 17640:00

hard labor or the heavy lifting done and

## 17640:00 - 17670:00

then my job is just to come in and like

## 17670:00 - 17725:00

have, I guess, like, you know, taste or

## 17725:00 - 17760:00

preference like that. That is the real

## 17760:00 - 17780:00

opportunity here with all of us.

## 17780:00 - 17825:00

Exactly. Um, and you know, maybe gets it

## 17825:00 - 17850:00

only 80% of the way there and then you

## 17850:00 - 17870:00

have to have a human in the loop to get

## 17870:00 - 17910:00

it the last 20%. But a lot of the times

## 17910:00 - 17935:00

I mean there there's so much time saving

## 17935:00 - 17965:00

with that. I mean for example like we we

## 17965:00 - 18010:00

have agencies uh like one of ours is a a

## 18010:00 - 18055:00

SAS SEO agency right historically if I

## 18055:00 - 18100:00

was doing uh you know any type of SEO

## 18100:00 - 18130:00

services like content writing was the

## 18130:00 - 18165:00

the most time consuming aspect like

## 18165:00 - 18195:00

researching the article and then doing

## 18195:00 - 18215:00

the content writing was the most

## 18215:00 - 18250:00

timeconuming aspects of the whole

## 18250:00 - 18290:00

process. Like now we have an automation

## 18290:00 - 18320:00

that basically, you know, takes the

## 18320:00 - 18350:00

target keyword, scrapes what's currently

## 18350:00 - 18385:00

ranking on page one, and then writes the

## 18385:00 - 18410:00

first draft of the article based on

## 18410:00 - 18450:00

that. I mean, it's 90% of the way there.

## 18450:00 - 18475:00

We have a human coming in over the top

## 18475:00 - 18500:00

of it just to like edit it for dwell

## 18500:00 - 18535:00

time so that it's like basically just

## 18535:00 - 18570:00

more readable from a human standpoint.

## 18570:00 - 18610:00

But that, you know, that process that

## 18610:00 - 18650:00

used to take like a day to write an

## 18650:00 - 18680:00

article, as an example, it now happens

## 18680:00 - 18745:00

in, you know, 30 seconds. And I mean, we

## 18745:00 - 18775:00

can get a hundred of those out the door,

## 18775:00 - 18815:00

right? That in in the time that it used

## 18815:00 - 18860:00

to take to only get maybe 10 of them or

## 18860:00 - 18895:00

even less, maybe five of them. So, I

## 18895:00 - 18915:00

think that's like the mindset to

## 18915:00 - 18945:00

approach the Swiss. And and the other

## 18945:00 - 18985:00

thing to piggyback on that with is we're

## 18985:00 - 19015:00

not doing anything different, right?

## 19015:00 - 19045:00

Like you're not changing how you're

## 19045:00 - 19070:00

running your ads accounts or like how

## 19070:00 - 19100:00

you're doing your your your creative

## 19100:00 - 19135:00

development in any way. The only thing

## 19135:00 - 19170:00

that's changing is the automation of

## 19170:00 - 19200:00

those processes that already exist,

## 19200:00 - 19230:00

right? So, it's like not a reinvent.

## 19230:00 - 19260:00

We're not reinventing the wheel or any

## 19260:00 - 19315:00

any uh big uh I don't know. It's not

## 19315:00 - 19350:00

like this. How I think about it is we're

## 19350:00 - 19375:00

not replacing anything that we were

## 19375:00 - 19405:00

doing previously. Um we're just like

## 19405:00 - 19445:00

augmenting it, right? And so anyways, I

## 19445:00 - 19470:00

I think that's things that like people

## 19470:00 - 19490:00

get hung up on where they're trying to

## 19490:00 - 19525:00

like find these like new creative ways

## 19525:00 - 19560:00

to like use this like because and that

## 19560:00 - 19590:00

frontier is totally there. like there

## 19590:00 - 19615:00

are people that are probably going to

## 19615:00 - 19665:00

invent uh these new use cases but for

## 19665:00 - 19690:00

the majority of companies it's just like

## 19690:00 - 19730:00

what are you doing currently what can

## 19730:00 - 19760:00

you automate of that and for a lot of

## 19760:00 - 19790:00

companies that's like 80% of their human

## 19790:00 - 19810:00

labor they can go and automate with

## 19810:00 - 19840:00

these tools especially on the marketing

## 19840:00 - 19870:00

side and I mean that's immediate cost

## 19870:00 - 19910:00

savings right like we can I've seen I' I

## 19910:00 - 19945:00

I have friends that run agencies that

## 19945:00 - 19985:00

their their margin was like 30% and

## 19985:00 - 20005:00

started implementing these AI

## 20005:00 - 20040:00

automations and tools etc and I mean

## 20040:00 - 20070:00

they took their margins to like 70%

## 20070:00 - 20090:00

overnight just because they like

## 20090:00 - 20120:00

automated that human labor. So I think

## 20120:00 - 20145:00

again just that's the way to think about

## 20145:00 - 20195:00

this if you're you know a founder

## 20195:00 - 20215:00

listening to this ahead of growth

## 20215:00 - 20265:00

listening to this etc. So um with that

## 20265:00 - 20295:00

said man I let's just jump into it. I'd

## 20295:00 - 20325:00

love to see some of the workflows some

## 20325:00 - 20345:00

of the ways that you're you're

## 20345:00 - 20385:00

implementing this. Um okay and uh yeah

## 20385:00 - 20405:00

I'll just have you screen share and

## 20405:00 - 20425:00

maybe we just like talk through the

## 20425:00 - 20470:00

automations and and uh uh uh show have

## 20470:00 - 20525:00

you show uh the audience. Let's do it.

## 20525:00 - 20555:00

I'll pull up a couple of flows here and

## 20555:00 - 20590:00

then we can get started. Let's

## 20590:00 - 20645:00

see. Um, let's do let's start with the

## 20645:00 - 20670:00

Reddit one because we already discussed

## 20670:00 - 20695:00

that a little bit. Let me just pull that

## 20695:00 - 20730:00

up right here. I'll see if I can find

## 20730:00 - 20770:00

that. Yeah, here we

## 20770:00 - 20820:00

go. I think we should be good now. Yep,

## 20820:00 - 20860:00

I can see that. It's perfect. Cool.

## 20860:00 - 20905:00

Yeah. So, this is a Reddit marketing

## 20905:00 - 20955:00

insights um flow that I built inside of

## 20955:00 - 20990:00

Nen. So yeah, basically I can just

## 20990:00 - 21020:00

quickly go through the flow high level

## 21020:00 - 21045:00

and I can just kind of like show you the

## 21045:00 - 21070:00

output here as well later. I'll just

## 21070:00 - 21100:00

pull this up first. So I just have it

## 21100:00 - 21135:00

ready,

## 21135:00 - 21190:00

but we basically again so we start with

## 21190:00 - 21240:00

a with a trigger to kind of like fire

## 21240:00 - 21275:00

the entire workflow. So in this case I I

## 21275:00 - 21310:00

do it manually inside of Naden as I do

## 21310:00 - 21335:00

with most of these flows that I

## 21335:00 - 21370:00

mentioned. So this one is fired based on

## 21370:00 - 21405:00

a form submission. So here I basically

## 21405:00 - 21460:00

just enter the brand name. I entered the

## 21460:00 - 21505:00

website and a product

## 21505:00 - 21560:00

explanation and then where is

## 21560:00 - 21600:00

the where's the

## 21600:00 - 21645:00

keyword? Let's

## 21645:00 - 21695:00

see.

## 21695:00 - 21740:00

Oh, that's cuz I have a pin data here.

## 21740:00 - 21760:00

Let me just unpin this and I'll show

## 21760:00 - 21790:00

you. Oh, sorry. This is based on the

## 21790:00 - 21815:00

product explanation. Sorry. So if I just

## 21815:00 - 21870:00

do let's just do

## 21870:00 - 21920:00

try

## 21920:00 - 21975:00

drink.com and then

## 21975:00 - 22000:00

alcohol

## 22000:00 - 22025:00

alternate

## 22025:00 - 22075:00

alternative

## 22075:00 - 22115:00

beverage. Sorry I have so many flows. I

## 22115:00 - 22140:00

think this one basically descripes

## 22140:00 - 22180:00

Reddit for pain points based on that

## 22180:00 - 22220:00

like on a on a product description or on

## 22220:00 - 22260:00

a yeah like an uh like for a certain

## 22260:00 - 22310:00

niche if that makes sense. Totally. Yes.

## 22310:00 - 22330:00

So, it's running in the background.

## 22330:00 - 22355:00

Basically, it went to Reddit. It

## 22355:00 - 22390:00

identified, you know, all of the Reddit

## 22390:00 - 22425:00

conversations that happened around Yeah.

## 22425:00 - 22455:00

probably alcohol alternative. I imagine

## 22455:00 - 22475:00

that's probably like the main keyword

## 22475:00 - 22520:00

that it ends up pulling. Correct. Um,

## 22520:00 - 22560:00

pulls that context back into the context

## 22560:00 - 22600:00

window of the AI and then at that point

## 22600:00 - 22620:00

then, you know, the writing process

## 22620:00 - 22645:00

basically starts occurring. You're just

## 22645:00 - 22675:00

hitting a chat GPT endpoint to actually

## 22675:00 - 22705:00

do that writing. Um, just again,

## 22705:00 - 22735:00

narrating's for the the audience that's

## 22735:00 - 22765:00

only listening.

## 22765:00 - 22800:00

But the uh also if you're listening only

## 22800:00 - 22830:00

to this, go to YouTube. It'll probably

## 22830:00 - 22880:00

be more impactful for you. So then after

## 22880:00 - 22905:00

it completes that writing, what are

## 22905:00 - 22930:00

those following steps that are occurring

## 22930:00 - 22975:00

after that? So yeah, I can I can just

## 22975:00 - 22995:00

walk through everything. So basically

## 22995:00 - 23025:00

yeah what we said here is that we we

## 23025:00 - 23070:00

send everything off to a uh open AI node

## 23070:00 - 23105:00

first uh which is basically like a chat

## 23105:00 - 23140:00

GPT node and we tell it that it is a

## 23140:00 - 23160:00

marketing strategist and Reddit

## 23160:00 - 23210:00

researcher and based uh on the product

## 23210:00 - 23245:00

description that we pass through the

## 23245:00 - 23265:00

form right here. You can see that this

## 23265:00 - 23295:00

is kind of like a dynamic keyword. So

## 23295:00 - 23330:00

yeah whatever we add in the in the form

## 23330:00 - 23370:00

is kind of like what we um research

## 23370:00 - 23410:00

right here. So we basically yeah now I

## 23410:00 - 23435:00

remember the entire flow. So we

## 23435:00 - 23485:00

basically explain our product

## 23485:00 - 23530:00

uh description and then based on that we

## 23530:00 - 23580:00

have um the actual AI spit out the

## 23580:00 - 23615:00

optimal keyword to scrape rider that's

## 23615:00 - 23665:00

how I built this for I remember now so

## 23665:00 - 23705:00

basically this one so I should have

## 23705:00 - 23745:00

basically explained uh this a little bit

## 23745:00 - 23785:00

different in the in the form but in this

## 23785:00 - 23830:00

case uh the AI meant that we should

## 23830:00 - 23865:00

scrape ready for quit drinking that's

## 23865:00 - 23895:00

the keyword that we wanted to scrape so

## 23895:00 - 23945:00

you basically just send uh the keyword

## 23945:00 - 24000:00

quit drinking to the Reddit node and

## 24000:00 - 24030:00

we're then we're scraping Reddit for

## 24030:00 - 24070:00

that specific keyword and then topics

## 24070:00 - 24105:00

and posts around that. Then what what I

## 24105:00 - 24140:00

want there's a specific Reddit node on

## 24140:00 - 24175:00

NAN. Sorry, I haven't seen this before.

## 24175:00 - 24215:00

There is Yeah, there is. It's amazing,

## 24215:00 - 24240:00

man. Yeah, it's crazy. So, you can do

## 24240:00 - 24265:00

this or you can kind like do it through

## 24265:00 - 24295:00

like HTTP request nodes as well

## 24295:00 - 24320:00

obviously, but yeah, I just like

## 24320:00 - 24345:00

perplexity or whatever. That's what I've

## 24345:00 - 24375:00

done previously is like basically a

## 24375:00 - 24425:00

perplexity call to their API to pull

## 24425:00 - 24450:00

back the you know relevant Reddit

## 24450:00 - 24485:00

threads and then we put that whatever's

## 24485:00 - 24515:00

on there like into the context window.

## 24515:00 - 24545:00

So yeah. Yeah, for sure. But yeah, they

## 24545:00 - 24570:00

haven't they have native ones as well.

## 24570:00 - 24610:00

So this one works just fine. So yeah, I

## 24610:00 - 24630:00

basically just wanted to scrape 10

## 24630:00 - 24690:00

posts. We then filter those posts by uh

## 24690:00 - 24730:00

I guess like by virality or popularity.

## 24730:00 - 24765:00

So I basically just filter by if the

## 24765:00 - 24830:00

post uh has two up votes or more and the

## 24830:00 - 24865:00

the basically if the post has a text. So

## 24865:00 - 24895:00

it's just not like a like a empty

## 24895:00 - 24945:00

headline post or whatever, right? So

## 24945:00 - 24980:00

yeah, you can basically just filter. So

## 24980:00 - 25015:00

I I pulled just 10 posts right here, but

## 25015:00 - 25050:00

you could pull like 100 a thousand and

## 25050:00 - 25075:00

then you can filter based on like

## 25075:00 - 25100:00

certain amount of uploads or certain

## 25100:00 - 25120:00

amount of comments just so you know

## 25120:00 - 25160:00

you're getting like super hot post or

## 25160:00 - 25205:00

super like viral post. Um, but yeah, you

## 25205:00 - 25240:00

can customize this however you want. We

## 25240:00 - 25290:00

then send this over into a different AI

## 25290:00 - 25350:00

node which basically just like um ranks

## 25350:00 - 25395:00

if the all of the posts that we scraped

## 25395:00 - 25450:00

are relevant for our keyword or product.

## 25450:00 - 25510:00

So we basically stack ranks the uh the

## 25510:00 - 25550:00

posts or sorry stacks ranks the

## 25550:00 - 25585:00

information that it scraped against each

## 25585:00 - 25620:00

other like the ideas basically against

## 25620:00 - 25650:00

each other of which one's the best based

## 25650:00 - 25685:00

on our product description. So like for

## 25685:00 - 25720:00

for an alcohol alternative, it it kind

## 25720:00 - 25765:00

of like it it analyzes if these posts

## 25765:00 - 25790:00

are actually like relevant to that

## 25790:00 - 25855:00

pretty much. Interesting. Okay. So it

## 25855:00 - 25880:00

does that and then what happens next

## 25880:00 - 25915:00

after that? Then we pass everything

## 25915:00 - 25975:00

through to the um the main AI agent

## 25975:00 - 26020:00

which turns these scrape posts into

## 26020:00 - 26060:00

market insights. So here we have a

## 26060:00 - 26110:00

prompt that um tells the agent that it

## 26110:00 - 26145:00

is a senior marketing strategist helping

## 26145:00 - 26175:00

DDC brands extract powerful messaging

## 26175:00 - 26225:00

insights from patch of Reddit post. Then

## 26225:00 - 26255:00

we basically just send over all the

## 26255:00 - 26290:00

posts and then we give it the the

## 26290:00 - 26330:00

product uh description right here and

## 26330:00 - 26375:00

then we basically have it uh analyze the

## 26375:00 - 26400:00

overall conversation and return the

## 26400:00 - 26440:00

following structured insights. Top three

## 26440:00 - 26485:00

pain points, trigger events, um desired

## 26485:00 - 26520:00

outcomes, interesting quotes or phrases.

## 26520:00 - 26545:00

So, like if there are any like really

## 26545:00 - 26575:00

cool phrases inside of the post that we

## 26575:00 - 26620:00

could potentially use. Um, ad copy

## 26620:00 - 26655:00

hooks, marketing insights, and any

## 26655:00 - 26695:00

trends or opportunities. And then you

## 26695:00 - 26720:00

can see right here, it pulled everything

## 26720:00 - 26760:00

out on the on the right right here. So,

## 26760:00 - 26790:00

top three pain points, realizing alcohol

## 26790:00 - 26825:00

was limiting their potential as success,

## 26825:00 - 26850:00

struggling with social situations

## 26850:00 - 26885:00

without alcohol, um, experiencing

## 26885:00 - 26915:00

negative physical and mental health

## 26915:00 - 26960:00

benefits. Um, interesting quotes. I

## 26960:00 - 26985:00

thought I was high functioning, then I

## 26985:00 - 27015:00

quit drinking. life can be so much

## 27015:00 - 27040:00

better than you even imagine. I only

## 27040:00 - 27080:00

thought that I was high

## 27080:00 - 27135:00

function. Yeah. Yeah. It's super cool.

## 27135:00 - 27175:00

And then pretty much I just um yeah, I

## 27175:00 - 27225:00

send everything out to a Google Sheets

## 27225:00 - 27265:00

that has everything right here. So yeah,

## 27265:00 - 27290:00

you have the the pain points, the

## 27290:00 - 27320:00

trigger events,

## 27320:00 - 27390:00

outcomes, quotes, content ideas, ad copy

## 27390:00 - 27415:00

hooks, and then marketing insights, and

## 27415:00 - 27445:00

then trends. Then you can just literally

## 27445:00 - 27490:00

run this like on a weekly basis, every

## 27490:00 - 27525:00

single day if you want based on multiple

## 27525:00 - 27560:00

keywords. Then you can just come in here

## 27560:00 - 27600:00

and just see like okay like are there

## 27600:00 - 27630:00

any like maybe trigger events that we

## 27630:00 - 27665:00

haven't considered for like our audience

## 27665:00 - 27705:00

that we could discuss or are there any

## 27705:00 - 27745:00

like cool outcomes here that that might

## 27745:00 - 27770:00

be that we could position our product

## 27770:00 - 27800:00

towards that we haven't already. So, I

## 27800:00 - 27845:00

see this flow as kind of like a way to

## 27845:00 - 27880:00

maybe like open up your TAM or kind of

## 27880:00 - 27930:00

like tap into new or different audiences

## 27930:00 - 27965:00

that you haven't maybe considered based

## 27965:00 - 28010:00

on like actual data and post that people

## 28010:00 - 28045:00

are talking about. Same like with quotes

## 28045:00 - 28080:00

as well, right? I mean, like obviously

## 28080:00 - 28110:00

like your customers are your best

## 28110:00 - 28150:00

advertisers. So, like taking their exact

## 28150:00 - 28195:00

wording and phrases is is is for sure

## 28195:00 - 28215:00

going to be an effective marketing

## 28215:00 - 28255:00

strategy a lot of the time. So, 100%.

## 28255:00 - 28275:00

Yeah. I mean, you're mirroring the

## 28275:00 - 28295:00

language that they're using and

## 28295:00 - 28325:00

describing the pain point that you're

## 28325:00 - 28360:00

solving, right? And I I I mean, that's

## 28360:00 - 28410:00

one of the most powerful and the also

## 28410:00 - 28435:00

the hardest things to do like

## 28435:00 - 28460:00

historically is like how do I identify

## 28460:00 - 28485:00

the language that my target customer

## 28485:00 - 28520:00

uses to describe the thing that, you

## 28520:00 - 28555:00

know, my product actually does. I see

## 28555:00 - 28580:00

this with startup startups all the time

## 28580:00 - 28610:00

where they like they call it something

## 28610:00 - 28625:00

different than who they're actually

## 28625:00 - 28655:00

selling it to, right? You know, when

## 28655:00 - 28685:00

they're still trying to figure out kind

## 28685:00 - 28720:00

of their their go to market motion. So,

## 28720:00 - 28750:00

I feel like this is just like a it's

## 28750:00 - 28790:00

basically a cheat code to to get to to

## 28790:00 - 28820:00

get to that messaging faster on how do

## 28820:00 - 28845:00

we even describe the product? How does

## 28845:00 - 28875:00

it fit into the market? Um, based off

## 28875:00 - 28895:00

of, you know, the conversations that are

## 28895:00 - 28920:00

happening. Are you just using Reddit for

## 28920:00 - 28945:00

this or are you using any other sources?

## 28945:00 - 28975:00

I know some pe I saw people using Kora

## 28975:00 - 29010:00

in the past. I saw people trying to do

## 29010:00 - 29040:00

this with Twitter as well, like d you

## 29040:00 - 29065:00

know, the conversations or dialogue that

## 29065:00 - 29090:00

are happening around the platform. I

## 29090:00 - 29130:00

actually do I do have one for both

## 29130:00 - 29170:00

Twitter and for I actually just finished

## 29170:00 - 29210:00

a a Twitter one this morning actually.

## 29210:00 - 29265:00

So this one is a little bit more basic.

## 29265:00 - 29305:00

This one is just pulling

## 29305:00 - 29350:00

um like just top tweets or viral tweets

## 29350:00 - 29380:00

and kind of like the the stats like how

## 29380:00 - 29425:00

many likes and how many how many um yeah

## 29425:00 - 29445:00

retweets and comments and stuff like

## 29445:00 - 29480:00

that. But you could easily add in

## 29480:00 - 29505:00

another step here to kind of like

## 29505:00 - 29545:00

analyze the the scrape data as well and

## 29545:00 - 29565:00

then kind like have the output the same

## 29565:00 - 29605:00

way. But for this for this specific

## 29605:00 - 29645:00

flow, I'm basically just scraping X

## 29645:00 - 29675:00

based on a keyword that I set. And then

## 29675:00 - 29710:00

I just choose if we want to scrape top

## 29710:00 - 29755:00

or latest post. It scrapes. Uh are you

## 29755:00 - 29800:00

doing this for your own uh content uh

## 29800:00 - 29840:00

creation? Yeah. So top automation tweets

## 29840:00 - 29870:00

from the last week. Uh this influences

## 29870:00 - 29905:00

the ones that I go and create. Yeah. If

## 29905:00 - 29935:00

you just if you literally just take a

## 29935:00 - 29995:00

look here, I I've been using this um

## 29995:00 - 30050:00

this sheet right here for both not only

## 30050:00 - 30105:00

just like um ideas or topic ideas to

## 30105:00 - 30125:00

kind of like create content around, but

## 30125:00 - 30170:00

also just like how to structure the

## 30170:00 - 30200:00

post, right? Because like how you

## 30200:00 - 30225:00

obviously like how you write the post

## 30225:00 - 30275:00

itself has plays a huge part in in like

## 30275:00 - 30315:00

the reach and virality. So yeah, I

## 30315:00 - 30345:00

basically just come in here. I see like,

## 30345:00 - 30390:00

okay, this post's got 152,000 views and

## 30390:00 - 30470:00

like 2300 likes. This one got 22,000

## 30470:00 - 30525:00

likes um and so on. And then I structure

## 30525:00 - 30550:00

Yeah. Again, kind of like how they write

## 30550:00 - 30580:00

it. So, yeah, this has definitely been a

## 30580:00 - 30640:00

huge part of um uh yeah, me growing on

## 30640:00 - 30665:00

Twitter as well. Just like literally

## 30665:00 - 30690:00

modeling what I see other people working

## 30690:00 - 30730:00

here. Totally. So this is my strategy

## 30730:00 - 30760:00

for Twitter growth like that I've used

## 30760:00 - 30785:00

over the last two years is just

## 30785:00 - 30815:00

basically like write a bunch of content

## 30815:00 - 30845:00

look at what's working go and write more

## 30845:00 - 30880:00

like the best performing you know all

## 30880:00 - 30905:00

social media is just that right it's

## 30905:00 - 30930:00

like figuring out what resonates with

## 30930:00 - 30975:00

your audience etc. Um, what's

## 30975:00 - 31000:00

interesting though is like you're do you

## 31000:00 - 31025:00

could do this both for what's already

## 31025:00 - 31065:00

gone viral on the platform, your your

## 31065:00 - 31100:00

internal I mean what it will probably

## 31100:00 - 31130:00

turn into as well is like you'll start

## 31130:00 - 31170:00

to see like week overw week trends with

## 31170:00 - 31210:00

like what is like the idea of that

## 31210:00 - 31240:00

moment like the zeitgeist of that moment

## 31240:00 - 31265:00

and you could be basically be like okay

## 31265:00 - 31310:00

cool like um this you know last week

## 31310:00 - 31340:00

this idea or you know what are the top

## 31340:00 - 31365:00

three ideas or what are the common three

## 31365:00 - 31395:00

ideas from all of this source material

## 31395:00 - 31415:00

you could basically take all of these

## 31415:00 - 31455:00

tweets put that into claude and tell it,

## 31455:00 - 31480:00

you know, ask it to give you the

## 31480:00 - 31520:00

insights of like the common uh concepts,

## 31520:00 - 31545:00

right, or formats that are working. And

## 31545:00 - 31575:00

then based off of that, uh, you know,

## 31575:00 - 31605:00

that can influence, okay, we're going to

## 31605:00 - 31640:00

only focus on the ones that are the, you

## 31640:00 - 31665:00

know, that that are have the most

## 31665:00 - 31690:00

virality based off of the source data

## 31690:00 - 31730:00

that we provide. So, right, dude, I I

## 31730:00 - 31755:00

love this man. Okay, so how are you

## 31755:00 - 31770:00

pulling from Twitter? Is it just

## 31770:00 - 31805:00

directly from the API for this data or

## 31805:00 - 31855:00

are you doing Okay, I'm using a uh tool

## 31855:00 - 31905:00

called Twitter API.io. So, it's they

## 31905:00 - 31925:00

have a free account, so I think you can

## 31925:00 - 31950:00

scrape like a thousand tweets or

## 31950:00 - 31990:00

something like that. Um, yep. So, you

## 31990:00 - 32015:00

just literally just sign up, grab their

## 32015:00 - 32080:00

API key, hook it up to um Yeah. Uh, any,

## 32080:00 - 32100:00

and then you just run through the entire

## 32100:00 - 32135:00

flow right here. Totally. Oh, man. It's

## 32135:00 - 32175:00

so cheap. It's like 15 cents per

## 32175:00 - 32195:00

thousand tweets is what I'm saying.

## 32195:00 - 32225:00

Yeah. It's crazy. It's crazy cheap. So,

## 32225:00 - 32260:00

insane. And you can get a lot of data

## 32260:00 - 32290:00

for like I mean, literally next to

## 32290:00 - 32330:00

nothing with a lot of these tools. So it

## 32330:00 - 32350:00

doesn't even have to be like super

## 32350:00 - 32375:00

expensive to to run these flows, which

## 32375:00 - 32415:00

is which is awesome. Totally. We use

## 32415:00 - 32460:00

Rapid API and Apify a lot for all of our

## 32460:00 - 32495:00

like kind of third party API scraping.

## 32495:00 - 32525:00

Um it's crazy what you can scrape with

## 32525:00 - 32565:00

Ampify, man. I My brother's looking for

## 32565:00 - 32590:00

a house right now. And so he's just like

## 32590:00 - 32640:00

using uh like a Zillow scraper API

## 32640:00 - 32685:00

basically from Appify to go and pull all

## 32685:00 - 32730:00

the home data for him. And then that's

## 32730:00 - 32775:00

awesome. Pretty wild. Um uh but anyway,

## 32775:00 - 32810:00

so okay, so this one amazing. I feel

## 32810:00 - 32835:00

like the research component makes total

## 32835:00 - 32870:00

sense like where like how do I aggregate

## 32870:00 - 32920:00

data, organize it, um understand what's

## 32920:00 - 32955:00

working based off of uh the impression

## 32955:00 - 32990:00

data, the engagement data, etc. Okay.

## 32990:00 - 33015:00

So, once you've gotten that insight,

## 33015:00 - 33035:00

what what what do you do from there?

## 33035:00 - 33060:00

Kind of what's your what are some of the

## 33060:00 - 33085:00

flows that you use to actually create

## 33085:00 - 33130:00

the the content or the output? So, I

## 33130:00 - 33165:00

don't really have a full end to-end

## 33165:00 - 33190:00

workflow that kind of like combines

## 33190:00 - 33240:00

everything yet because yeah, I think it

## 33240:00 - 33275:00

I think at least for right now, it

## 33275:00 - 33320:00

probably makes sense to keep uh the the

## 33320:00 - 33360:00

flow separate. Yeah, siloed off and then

## 33360:00 - 33395:00

you can kind of just combine the data. I

## 33395:00 - 33425:00

did actually create this one float that

## 33425:00 - 33465:00

was based off of your tweet actually.

## 33465:00 - 33500:00

Um, let me see if I can find that. Which

## 33500:00 - 33545:00

is the uh, yeah, the Reddit social

## 33545:00 - 33585:00

listener to Let me see if I can find the

## 33585:00 - 33655:00

actual Is it Let me see. Was it the uh,

## 33655:00 - 33690:00

uh, to create basically like a Yeah, the

## 33690:00 - 33725:00

comic book style. Yeah, totally.

## 33725:00 - 33770:00

Exactly. Yeah. So, yeah. So, because I

## 33770:00 - 33800:00

at that point I I was already using the

## 33800:00 - 33835:00

the Reddit flow that I had built, right?

## 33835:00 - 33880:00

So, I basically just tagged on the the

## 33880:00 - 33930:00

image gen part and then I created the

## 33930:00 - 33985:00

entire flow. So again, this one we we

## 33985:00 - 34045:00

scrape Reddit uh based on based on a

## 34045:00 - 34080:00

keyword that we give it. We again we we

## 34080:00 - 34120:00

rank if the the post is relevant for our

## 34120:00 - 34160:00

product description. We then turn those

## 34160:00 - 34200:00

pain points into messages. We rank the

## 34200:00 - 34235:00

top 10 messages and then we use those

## 34235:00 - 34275:00

top 10 messages to create like actual

## 34275:00 - 34330:00

image prompts that we send to ChatBT's

## 34330:00 - 34365:00

um OpenAI image den and then we create

## 34365:00 - 34405:00

those comic book ads. So, if I pull up

## 34405:00 - 34455:00

my folder right here, I hope I still

## 34455:00 - 34525:00

have a bunch of them in.

## 34525:00 - 34580:00

Uh, no, I think I deleted them. But

## 34580:00 - 34610:00

basically, you can create those comic

## 34610:00 - 34650:00

book style ads that um totally that you

## 34650:00 - 34680:00

were talking about. So, this is probably

## 34680:00 - 34700:00

the closest that I've come to kind of

## 34700:00 - 34730:00

like combining Yeah. an end to end

## 34730:00 - 34770:00

solution. Yeah, exactly. Exactly. But

## 34770:00 - 34800:00

other than that, like, yeah, I'm keeping

## 34800:00 - 34830:00

things a little bit more siloed for now,

## 34830:00 - 34865:00

just for simplicity's sake, to be

## 34865:00 - 34900:00

honest. Totally. No, that makes sense.

## 34900:00 - 34930:00

So, so you've done this research, you

## 34930:00 - 34970:00

found your insights. Um, at that point,

## 34970:00 - 35000:00

um, like where where are you going? Uh,

## 35000:00 - 35030:00

do you go and, you know, bulk generate

## 35030:00 - 35080:00

with the Open AI, uh, API image calls?

## 35080:00 - 35105:00

Like what flows are you using? And could

## 35105:00 - 35130:00

you talk through some of those, um, that

## 35130:00 - 35160:00

you're seeing be effective right now?

## 35160:00 - 35205:00

Yeah, let me pull up an image gen one.

## 35205:00 - 35230:00

Let's see.

## 35230:00 - 35255:00

So, I imagine when you're breaking this

## 35255:00 - 35290:00

down, it's like research, the actual

## 35290:00 - 35330:00

like creative creation.

## 35330:00 - 35385:00

Um, and then maybe like the

## 35385:00 - 35425:00

the really it's probably like the data

## 35425:00 - 35455:00

analysis of what's actually working. I

## 35455:00 - 35475:00

know you talked about or the

## 35475:00 - 35510:00

conversation we had previously is like

## 35510:00 - 35545:00

you were pulling all that data in from

## 35545:00 - 35580:00

the Facebook ads API and then basically

## 35580:00 - 35600:00

being like, okay, you know, the ones

## 35600:00 - 35615:00

that are winning, what do they have in

## 35615:00 - 35640:00

common? That type of thing.

## 35640:00 - 35675:00

I'm thinking just kind of next or next

## 35675:00 - 35710:00

flows I'd love to see is the actual, you

## 35710:00 - 35735:00

know, the creation of the content and

## 35735:00 - 35765:00

then if there's any of that analysis

## 35765:00 - 35805:00

part as well. Yeah, let me pull up that

## 35805:00 - 35845:00

the the the main one right here. Let's

## 35845:00 - 35890:00

see where is where is that

## 35890:00 - 35945:00

one. So, no, that's not that one. Let's

## 35945:00 - 35985:00

see. I have so many flows in here right

## 35985:00 - 36015:00

now. I need to organize things. No,

## 36015:00 - 36045:00

you're all good, man. You're all good.

## 36045:00 - 36075:00

This is how you know you're like a real

## 36075:00 - 36100:00

practitioner. It's cuz you have a

## 36100:00 - 36130:00

thousand of these that are just like

## 36130:00 - 36175:00

either half baked or or fully done that

## 36175:00 - 36210:00

you just like we're just we're just

## 36210:00 - 36245:00

cooking in a lab at this point. So I

## 36245:00 - 36275:00

love it, man. This one is pretty cool.

## 36275:00 - 36320:00

So, so yeah, I mean, well, first of all,

## 36320:00 - 36350:00

just to be like completely transparent,

## 36350:00 - 36390:00

like I would say tools like triple whale

## 36390:00 - 36435:00

do this a lot better than what what you

## 36435:00 - 36470:00

can do inside of edit end because just

## 36470:00 - 36500:00

to be completely frank like working with

## 36500:00 - 36525:00

and I mean we discussed this on our last

## 36525:00 - 36555:00

call like working with Facebook uh

## 36555:00 - 36600:00

Facebook's API right now is a headache

## 36600:00 - 36640:00

to be honest. So literally just p just

## 36640:00 - 36670:00

pulling data from ads manager and kind

## 36670:00 - 36715:00

like performance is is pretty difficult.

## 36715:00 - 36750:00

I had to actually bring in a like an

## 36750:00 - 36775:00

actual expert to help me complete this

## 36775:00 - 36805:00

flow because I couldn't figure it out.

## 36805:00 - 36830:00

Yeah, you just have to dig through like

## 36830:00 - 36860:00

so much documentation and kind of like

## 36860:00 - 36920:00

just really dig through things. So, um

## 36920:00 - 36975:00

for for for paid ads uh analysis

## 36975:00 - 37015:00

specifically, I would say that that's

## 37015:00 - 37045:00

probably the the the last thing I'm

## 37045:00 - 37090:00

using Nate for right now. But I can work

## 37090:00 - 37110:00

you walk you through this one which

## 37110:00 - 37140:00

basically just shows that it is actually

## 37140:00 - 37170:00

possible uh inside I think that'd be

## 37170:00 - 37200:00

super interesting just to kind of like

## 37200:00 - 37220:00

you know plant the seed of what what

## 37220:00 - 37265:00

this is capable of. Um are you using is

## 37265:00 - 37300:00

it a pre-built node that's in it in to

## 37300:00 - 37335:00

pull the Facebook ads uh data or you

## 37335:00 - 37385:00

doing an HTTP like a a call. It's a it's

## 37385:00 - 37420:00

a mix of both. It's a mix of both. Yeah.

## 37420:00 - 37465:00

Okay. Cool. So, so basically this flow

## 37465:00 - 37515:00

in a in a high level we we pull

## 37515:00 - 37565:00

performance data from ads manager on a

## 37565:00 - 37610:00

3-day basis. So every 3 days we pull the

## 37610:00 - 37660:00

data. So for this for yeah for for

## 37660:00 - 37685:00

example for an ecom brand like we're

## 37685:00 - 37760:00

pulling spend purchases um yeah CPA rows

## 37760:00 - 37795:00

all all the main numbers that we're that

## 37795:00 - 37835:00

we that we're uh optimizing and

## 37835:00 - 37890:00

analyzing. Uh we basically just all of

## 37890:00 - 37920:00

these steps are for like pulling out the

## 37920:00 - 37975:00

individual kind of like metrics and also

## 37975:00 - 38000:00

combining them with the with the

## 38000:00 - 38030:00

creative ID. So like the actual

## 38030:00 - 38060:00

creatives that are generating those

## 38060:00 - 38105:00

results. We pull all of this together.

## 38105:00 - 38155:00

Um and then we basically send this over

## 38155:00 - 38200:00

into we have four different agents here.

## 38200:00 - 38225:00

We kind of like have the the leader

## 38225:00 - 38245:00

agent which is kind of like the

## 38245:00 - 38290:00

orchestra and then we have three sub

## 38290:00 - 38325:00

agents that kind of like report to the

## 38325:00 - 38370:00

main one. We have a performance analyzer

## 38370:00 - 38410:00

agent. We have a deep research agent.

## 38410:00 - 38450:00

And then we have a new ad creation

## 38450:00 - 38495:00

agent. So in a nutshell, what this agent

## 38495:00 - 38545:00

does is that it again it scans um ads

## 38545:00 - 38590:00

manager performance on a 3-day basis. So

## 38590:00 - 38645:00

every 3 days you you this flow runs uh

## 38645:00 - 38700:00

it scans uh campaign adset and ad

## 38700:00 - 38750:00

performance. It pulls all of the running

## 38750:00 - 38810:00

ads. it and then it sends all of that

## 38810:00 - 38840:00

all of that data over to the performance

## 38840:00 - 38890:00

analyzer agent. Uh once that's done, we

## 38890:00 - 38940:00

pass it over to the deep research agent

## 38940:00 - 39000:00

which basically analyzes the content of

## 39000:00 - 39050:00

the winning ad. So like the ad copy um

## 39050:00 - 39095:00

the headlines like the the if it's an

## 39095:00 - 39140:00

image or if it's a video and uses uh

## 39140:00 - 39165:00

perplexities deep research to kind of

## 39165:00 - 39215:00

like analyze why those specific ads are

## 39215:00 - 39255:00

working or not. So kind of like yeah

## 39255:00 - 39305:00

desires uh trigger events pain points

## 39305:00 - 39325:00

etc in the copy and kind of like

## 39325:00 - 39365:00

analyzes why it's working. It then sends

## 39365:00 - 39430:00

all of that over to the third uh sub

## 39430:00 - 39480:00

agent which writes new ad variations

## 39480:00 - 39540:00

based on all the data and then we spit

## 39540:00 - 39585:00

the final output to a slack message. So

## 39585:00 - 39635:00

I can share with you what that looks

## 39635:00 - 39705:00

like as well here. So, if I just see,

## 39705:00 - 39755:00

are you able to see my Slack now or no?

## 39755:00 - 39780:00

Uh, no. I can't. You might need to

## 39780:00 - 39830:00

reshare. Yeah. Yeah. Yeah. Let's see.

## 39830:00 - 39900:00

Let's do screen. Let me just do Yeah.

## 39900:00 - 39925:00

So, this is kind of like how we we did

## 39925:00 - 39950:00

the output. So, we have

## 39950:00 - 40005:00

like creative insights drop April 16.

## 40005:00 - 40040:00

Um, we have the top performing ads, we

## 40040:00 - 40075:00

have the ad ID sent, we have the format,

## 40075:00 - 40115:00

we have the headline, the body copy, and

## 40115:00 - 40145:00

then we have like the the main kind of

## 40145:00 - 40170:00

like KPI. So like we have spend,

## 40170:00 - 40220:00

purchase, CPA, CTR, and then rorowaz for

## 40220:00 - 40265:00

the top three ads. And then we analyze

## 40265:00 - 40295:00

what's working across these ads. So like

## 40295:00 - 40340:00

the the messaging, the voice, the social

## 40340:00 - 40380:00

proof hooks. uh we analyze kind of like

## 40380:00 - 40415:00

trigger events and behavioral insights

## 40415:00 - 40445:00

with uh again yeah as I mentioned

## 40445:00 - 40505:00

perplexity uh the core desires uh

## 40505:00 - 40540:00

psychological framing of like why these

## 40540:00 - 40585:00

ads convert and then the agent also

## 40585:00 - 40630:00

spits out three new variations to test

## 40630:00 - 40680:00

and then call it kind of like a like a

## 40680:00 - 40720:00

yeah task mockup of like what you should

## 40720:00 - 40755:00

consider doing based on all the data

## 40755:00 - 40805:00

right here. That's amazing man. Yeah.

## 40805:00 - 40820:00

Yeah.

## 40820:00 - 40865:00

Yeah. So you can go like I mean you can

## 40865:00 - 40885:00

go super deep with this if you want.

## 40885:00 - 40915:00

Yeah. Totally. Totally. Totally. I feel

## 40915:00 - 40940:00

like the data analysis part is the

## 40940:00 - 40990:00

hardest part of this. Yeah. Yeah. It's

## 40990:00 - 41030:00

that that's still the human. Totally.

## 41030:00 - 41065:00

Yeah. Um and even like using tools like

## 41065:00 - 41095:00

like triple whale now as well like even

## 41095:00 - 41115:00

they are kind like struggling a little

## 41115:00 - 41150:00

bit because like it's it's tough to kind

## 41150:00 - 41185:00

like especially for like for an ads

## 41185:00 - 41220:00

manager like understanding the nuance

## 41220:00 - 41255:00

between like what a top performing ad

## 41255:00 - 41285:00

looks like. So, for example, like let's

## 41285:00 - 41325:00

say we have a top performing campaign

## 41325:00 - 41355:00

that's scaling up, but the CPA is a

## 41355:00 - 41380:00

little bit higher than on like a

## 41380:00 - 41415:00

retargeting campaign, right? The the LMM

## 41415:00 - 41450:00

might rank the retargeting campaign as

## 41450:00 - 41475:00

better performing because it has lower

## 41475:00 - 41510:00

CPA, but it doesn't really understand

## 41510:00 - 41550:00

that it's a retargeting campaign and you

## 41550:00 - 41580:00

can't really scale it up, right? So,

## 41580:00 - 41610:00

it's really tough to kind of like insert

## 41610:00 - 41660:00

those small nuances into into yeah,

## 41660:00 - 41700:00

these workflows. So yeah, I think I mean

## 41700:00 - 41735:00

obviously it's it's coming, but for now

## 41735:00 - 41760:00

it it's probably better to kind of like

## 41760:00 - 41810:00

use it for like an like more analysis

## 41810:00 - 41855:00

and then you like take the analysis and

## 41855:00 - 41885:00

data and execute on that instead of like

## 41885:00 - 41930:00

having the the the agents or the LMS

## 41930:00 - 41965:00

kind of like suggest what execution you

## 41965:00 - 41985:00

should do based on the data if that

## 41985:00 - 42025:00

makes sense. No, totally. Yeah, I I feel

## 42025:00 - 42050:00

like it's that human in the loop

## 42050:00 - 42085:00

component is still like a key aspect of

## 42085:00 - 42170:00

this. 100% 100%. Um okay, cool. uh we

## 42170:00 - 42185:00

have a little bit of time left. So,

## 42185:00 - 42240:00

wanted to uh dive into the actual um uh

## 42240:00 - 42270:00

like media creation uh process or the

## 42270:00 - 42300:00

the flows that you're doing to to to

## 42300:00 - 42330:00

make Facebook ads, you know, make video

## 42330:00 - 42355:00

ads, any of those that you're seeing for

## 42355:00 - 42400:00

sure. Which ones are you using uh like

## 42400:00 - 42420:00

most right now or that you're seeing the

## 42420:00 - 42465:00

most success with currently? So, I mean,

## 42465:00 - 42520:00

I'm using all just um Open AI's image

## 42520:00 - 42580:00

gen at the moment for AI uh production.

## 42580:00 - 42635:00

Uh, in terms of like video, it's still

## 42635:00 - 42665:00

not there yet to be completely honest. I

## 42665:00 - 42705:00

mean, sure, like with VO3, but it's

## 42705:00 - 42735:00

super expensive, but in terms of video,

## 42735:00 - 42760:00

it's it's just not there yet from what

## 42760:00 - 42810:00

I'm seeing. Um, so that's still

## 42810:00 - 42855:00

something that isn't quite there yet.

## 42855:00 - 42900:00

But in terms of uh image production, I

## 42900:00 - 42935:00

do have a flow that I can pull up and

## 42935:00 - 42995:00

show you. Just got to find the right

## 42995:00 - 43045:00

one. Yeah, here we go.

## 43045:00 - 43110:00

So in this flow we

## 43110:00 - 43180:00

basically this is for creating like uh

## 43180:00 - 43225:00

iterations of a winning ad that you

## 43225:00 - 43275:00

have. Right? So again we basically just

## 43275:00 - 43335:00

open up or fire off the the the flow

## 43335:00 - 43380:00

with a form trigger where I add in the

## 43380:00 - 43430:00

the brand name, the brand website and

## 43430:00 - 43465:00

kind of like the the winning ad, right,

## 43465:00 - 43500:00

that we want to create new variations

## 43500:00 - 43555:00

of. we we fire up the flow. The first

## 43555:00 - 43575:00

thing that we do is basically just

## 43575:00 - 43615:00

upload the the the winning ad. That's

## 43615:00 - 43645:00

just so we can easily reference it later

## 43645:00 - 43680:00

in the flow because uh yeah, a little

## 43680:00 - 43715:00

bit technical, but right now open it or

## 43715:00 - 43750:00

sorry, nod isn't great at kind of like

## 43750:00 - 43800:00

pulling images from previous nodes in a

## 43800:00 - 43840:00

later step. So that way we just uploaded

## 43840:00 - 43865:00

it to a Google Drive just so we can

## 43865:00 - 43910:00

always reference the the the winning ad

## 43910:00 - 43940:00

or the the reference image whenever we

## 43940:00 - 43985:00

we need to. So it's like local storage

## 43985:00 - 44025:00

is [ __ ] is what we've seen. So we we've

## 44025:00 - 44085:00

been using a a um a Google uh script

## 44085:00 - 44120:00

function. So basically a Google app

## 44120:00 - 44170:00

script as the way to to um do that that

## 44170:00 - 44200:00

pass. It's it's been it's been effective

## 44200:00 - 44230:00

for us to kind of like bypass the

## 44230:00 - 44270:00

limitations of NAD. So like leaning on

## 44270:00 - 44295:00

Google Cloud basically as a way to do

## 44295:00 - 44320:00

it. So anyway, just a random learning

## 44320:00 - 44345:00

for you. Love it. Yeah, that's great.

## 44345:00 - 44375:00

That's great. I mean yeah that's that's

## 44375:00 - 44420:00

a great workound. So yeah I mean yeah

## 44420:00 - 44450:00

this is like super simple. So you just

## 44450:00 - 44480:00

basically you just upload the image ad

## 44480:00 - 44505:00

and then you just redownload it. So we

## 44505:00 - 44550:00

just have it handy for reference. The

## 44550:00 - 44580:00

the next thing we do is we basically

## 44580:00 - 44625:00

just have a uh open AI node that uh

## 44625:00 - 44680:00

pulls a uh description of the actual ad.

## 44680:00 - 44715:00

So we basically just tell it to describe

## 44715:00 - 44750:00

the visual style, subject matter,

## 44750:00 - 44785:00

composition of this image. Is it a

## 44785:00 - 44810:00

lifestyle image, product shot or a

## 44810:00 - 44840:00

combination? Include lighting style and

## 44840:00 - 44875:00

camera angle if possible. So we

## 44875:00 - 44910:00

basically just pull that through. Next

## 44910:00 - 44955:00

we pull branding data. So we basically

## 44955:00 - 45040:00

just um have the uh the next node uh act

## 45040:00 - 45080:00

as a visual brand strategist and art

## 45080:00 - 45120:00

director uh and that we have it analyze

## 45120:00 - 45150:00

the brand website and focus only on kind

## 45150:00 - 45180:00

of like the brand's visual aesthetics.

## 45180:00 - 45230:00

So like color pletes uh photography

## 45230:00 - 45285:00

style imagery themes mood and so on. And

## 45285:00 - 45305:00

then we just again pass the brand

## 45305:00 - 45335:00

website and the brand name. So the

## 45335:00 - 45390:00

entire flow has that.

## 45390:00 - 45420:00

Then we start sending all of this over

## 45420:00 - 45465:00

to the main agent which will be creating

## 45465:00 - 45510:00

the actual prompts. So here we basically

## 45510:00 - 45530:00

just again we pass through all of the

## 45530:00 - 45570:00

data from the form. So we pass the the

## 45570:00 - 45610:00

brand name, the website, the image

## 45610:00 - 45635:00

description and the visual style

## 45635:00 - 45675:00

overview which we pulled from the two

## 45675:00 - 45720:00

previous notes. So it has all of that.

## 45720:00 - 45755:00

And then in the bottom one, this is

## 45755:00 - 45785:00

basically Sorry, my dog's going crazy

## 45785:00 - 45825:00

here. You're all good, man. We this note

## 45825:00 - 45865:00

we basically have like the the main

## 45865:00 - 45905:00

rules for kind of like the the output

## 45905:00 - 45940:00

that we have the entire flow build,

## 45940:00 - 45975:00

right? So yeah, we basically tell it to

## 45975:00 - 46040:00

generate 10 um uh tightly related visual

## 46040:00 - 46085:00

variations of a reference ad, not new

## 46085:00 - 46125:00

concepts. So yeah, I I won't read

## 46125:00 - 46155:00

through the entire thing, but basically

## 46155:00 - 46180:00

this is kind of like where you can play

## 46180:00 - 46210:00

around with the with the prompts to kind

## 46210:00 - 46240:00

of like get the output that you want.

## 46240:00 - 46260:00

So, let's say that you instead of

## 46260:00 - 46310:00

wanting to create um just uh small

## 46310:00 - 46335:00

variations of an image ad, you want to

## 46335:00 - 46380:00

create kind of like a like a net new ad

## 46380:00 - 46410:00

or kind of like a totally different

## 46410:00 - 46445:00

concept. This is kind like where you

## 46445:00 - 46470:00

want to play around and test like what

## 46470:00 - 46515:00

the prompt engineering if you will to

## 46515:00 - 46550:00

kind of like get the perfect output or

## 46550:00 - 46585:00

the output as close to perfect as as

## 46585:00 - 46630:00

possible for now at least.

## 46630:00 - 46670:00

Interesting. Um so, you're doing

## 46670:00 - 46705:00

variations of the winner rather than

## 46705:00 - 46740:00

like totally new. Yeah. Okay, that makes

## 46740:00 - 46775:00

sense. Yeah, for this one, this flow

## 46775:00 - 46810:00

specifically. Yes. So, then we basically

## 46810:00 - 46870:00

get 10 prompts uh based on the the

## 46870:00 - 46905:00

reference image and the bra uh the

## 46905:00 - 46945:00

branding data and the uh description of

## 46945:00 - 46990:00

the winning ad. We download the first

## 46990:00 - 47030:00

winning ad and then we send all of that

## 47030:00 - 47080:00

over into OpenAI's image genen node

## 47080:00 - 47125:00

which then has the the prompt that we

## 47125:00 - 47175:00

pulled from the the agent right here the

## 47175:00 - 47210:00

branding data the image description and

## 47210:00 - 47255:00

the reference ad which we um downloaded

## 47255:00 - 47285:00

here and then we just run through this

## 47285:00 - 47330:00

entire flow as many times as as you

## 47330:00 - 47360:00

want. So in my case I had it generate 10

## 47360:00 - 47395:00

variations. So then it just runs through

## 47395:00 - 47445:00

the entire flow 10 times. Um, I can open

## 47445:00 - 47480:00

up the fold right here and see if I have

## 47480:00 - 47555:00

anything in.

## 47555:00 - 47600:00

Yeah. Amazing, man. Yeah. So, I'm trying

## 47600:00 - 47660:00

to find just like the the original ad if

## 47660:00 - 47700:00

or the original uploaded image, but I

## 47700:00 - 47725:00

mean, you get the gist of it. So, like

## 47725:00 - 47750:00

this was probably Yeah. one that I

## 47750:00 - 47770:00

uploaded. And then if you just go

## 47770:00 - 47830:00

through, you'll see that

## 47830:00 - 47870:00

you can just play around. Yeah. All

## 47870:00 - 47910:00

different variations possible. So, yeah.

## 47910:00 - 47945:00

here. Here's for like obviously new net

## 47945:00 - 47990:00

new concepts, but it's still the same

## 47990:00 - 48035:00

thing, right? So yeah, just depending on

## 48035:00 - 48080:00

again how you kind of like prompt

## 48080:00 - 48120:00

engineer these agents will depend a lot

## 48120:00 - 48140:00

on kind of like the output that you get.

## 48140:00 - 48170:00

So here you can kind of like see you

## 48170:00 - 48200:00

have a lot more similar variations where

## 48200:00 - 48250:00

it's like it's in the bathroom. Um yeah,

## 48250:00 - 48290:00

before and after style. Uh yeah, kind of

## 48290:00 - 48350:00

like uh yeah, in nature and so on. Yep.

## 48350:00 - 48385:00

So you're basically so just to talk

## 48385:00 - 48415:00

through again this whole process from

## 48415:00 - 48455:00

top to bottom um research on the open

## 48455:00 - 48500:00

web find the concepts that make sense

## 48500:00 - 48545:00

look at the data of like what ad formats

## 48545:00 - 48565:00

are currently working or it's really

## 48565:00 - 48605:00

like ad templates y take those ad

## 48605:00 - 48650:00

templates provide the different concepts

## 48650:00 - 48690:00

bulk generate 10 variations you know for

## 48690:00 - 48720:00

each of the based off of the insights

## 48720:00 - 48755:00

based off of the best performing ads and

## 48755:00 - 48795:00

then look at the you know top performers

## 48795:00 - 48830:00

to understand okay what's working not

## 48830:00 - 48855:00

repeat that cycle over and over again is

## 48855:00 - 48890:00

kind of the whole strategy here. So,

## 48890:00 - 48925:00

yep. 100%. And you could you could

## 48925:00 - 48965:00

easily have those all as like their own

## 48965:00 - 48985:00

individual flows. So, you could have

## 48985:00 - 49015:00

like one like this one would be for

## 49015:00 - 49060:00

creating like like again iterations of a

## 49060:00 - 49100:00

winning ad. Another flow could be like

## 49100:00 - 49125:00

creating net new concepts or just like

## 49125:00 - 49155:00

UGC style ads and so on. And then you

## 49155:00 - 49180:00

just like have a ton of different like

## 49180:00 - 49210:00

siloed up flows that are all kind of

## 49210:00 - 49265:00

like yeah working on separate pieces of

## 49265:00 - 49320:00

the entire creative production.

## 49320:00 - 49350:00

That's so interesting, man. This is

## 49350:00 - 49400:00

crazy. I I feel like we could spend

## 49400:00 - 49420:00

probably the next three hours talking

## 49420:00 - 49455:00

through all these, but I know I know

## 49455:00 - 49480:00

we're coming up to time, so I want to

## 49480:00 - 49520:00

respect uh respect that. But uh man, it

## 49520:00 - 49545:00

was been so good to host you. Where

## 49545:00 - 49565:00

where can people find you if they want

## 49565:00 - 49605:00

to learn more? Please go follow Jonathan

## 49605:00 - 49645:00

on Twitter and on YouTube. I know you're

## 49645:00 - 49665:00

posting there as well. We'll include it

## 49665:00 - 49690:00

within the show notes, but do you have a

## 49690:00 - 49705:00

preference if people want to reach out

## 49705:00 - 49725:00

or want to hire you or want to work with

## 49725:00 - 49765:00

you? Yeah, I mean, just hitting me up on

## 49765:00 - 49805:00

um on X is cool. Uh yeah, I think that's

## 49805:00 - 49830:00

probably the best place to to reach me

## 49830:00 - 49875:00

right now. Amazing, man. Amazing. This

## 49875:00 - 49895:00

is so

## 49895:00 - 49930:00

valuable. I there's so much I'm thinking

## 49930:00 - 49950:00

about. I like can't even like put it

## 49950:00 - 49995:00

into words of like what I The last last

## 49995:00 - 50020:00

thing I have a question for you with

## 50020:00 - 50065:00

actually before we jump though is so I

## 50065:00 - 50090:00

mean we're finding this sometimes right

## 50090:00 - 50140:00

now where it's like creating the N8 end

## 50140:00 - 50175:00

flow is like can be a timeconsuming. I

## 50175:00 - 50190:00

mean we're we're speeding this up,

## 50190:00 - 50215:00

right? So what we're doing currently is

## 50215:00 - 50250:00

we go we use perplexity to basically

## 50250:00 - 50305:00

write JSON that we then take um and you

## 50305:00 - 50355:00

know basically paste into N to like

## 50355:00 - 50390:00

speed up that workflow building. But I

## 50390:00 - 50420:00

can show you something for please I

## 50420:00 - 50440:00

would love I would love to see what

## 50440:00 - 50470:00

you're using to build these out quickly

## 50470:00 - 50495:00

because the challenge we're facing is

## 50495:00 - 50530:00

like do we do a workflow or do we just

## 50530:00 - 50555:00

go straight to code with what we're

## 50555:00 - 50590:00

doing right like with our engineers. So

## 50590:00 - 50625:00

I'm curious actually I had that I had

## 50625:00 - 50660:00

that tap pulled up but I forgot. So let

## 50660:00 - 50700:00

me pull that up right here. So I'm using

## 50700:00 - 50730:00

Claude for this a lot and it's working

## 50730:00 - 50760:00

really good actually. So good. Yeah.

## 50760:00 - 50805:00

Yep. Yeah. So inside of Claude, if you

## 50805:00 - 50825:00

have a paid plan now, you can have

## 50825:00 - 50890:00

what's called projects. Um and and um

## 50890:00 - 50930:00

yeah, just just full disclosure, I did

## 50930:00 - 50965:00

not think of this. I pulled this from uh

## 50965:00 - 50990:00

Mark Chef's YouTube channel. I'll I'll

## 50990:00 - 51015:00

send you the link for him as well. He he

## 51015:00 - 51055:00

also shares a ton of amazing flows. But

## 51055:00 - 51105:00

you can basically um up. So what you

## 51105:00 - 51130:00

basically do is inside of cloud

## 51130:00 - 51170:00

projects, you just create a new project.

## 51170:00 - 51230:00

Uh let's just call this N test

## 51230:00 - 51290:00

3. You can add like what's called

## 51290:00 - 51325:00

product knowledge or instructions. So

## 51325:00 - 51350:00

what you do is you and I'll show you the

## 51350:00 - 51370:00

prompts and everything. You basically

## 51370:00 - 51420:00

just upload like best practices of

## 51420:00 - 51465:00

building N templates and like you pull

## 51465:00 - 51500:00

from the actual N documentation of like

## 51500:00 - 51520:00

these are the actual nodes that are

## 51520:00 - 51560:00

possible. This is like the like the tech

## 51560:00 - 51600:00

behind it. You can you upload that you

## 51600:00 - 51640:00

upload a ton of like example workflows

## 51640:00 - 51670:00

like JSON workflows and then you can

## 51670:00 - 51730:00

basically just have Claude spit out like

## 51730:00 - 51780:00

I would say like 70 to 80% completed

## 51780:00 - 51815:00

workflows. So if I just open this up

## 51815:00 - 51845:00

right here, you can see that I have like

## 51845:00 - 51910:00

the JSON uh instructions for like um

## 51910:00 - 51945:00

yeah prompting cloud. So I want you to

## 51945:00 - 51965:00

create fully functional internet

## 51965:00 - 51995:00

workflows. No images or screenshots,

## 51995:00 - 52035:00

only valid JSON follows and instructions

## 52035:00 - 52070:00

precisely. Then you just like have all

## 52070:00 - 52110:00

these rules right here. You upload a ton

## 52110:00 - 52155:00

of like reference JSON builds that might

## 52155:00 - 52205:00

be relevant. And then you also have um

## 52205:00 - 52250:00

this like cheat sheet and tips and

## 52250:00 - 52280:00

tricks that you upload. Then you can

## 52280:00 - 52315:00

literally come in and say

## 52315:00 - 52355:00

like, I want

## 52355:00 - 52385:00

to

## 52385:00 - 52465:00

build a workflow that scrapes Twitter

## 52465:00 - 52540:00

for popular

## 52540:00 - 52635:00

posts and uses that as a database to

## 52635:00 - 52890:00

create new Twitter posts for me.

## 52890:00 - 52925:00

So right now Claude basically is going

## 52925:00 - 52965:00

it's using your uh documentation that

## 52965:00 - 52985:00

you've provided it and it's going to go

## 52985:00 - 53040:00

and write this JSON node. Um yeah and it

## 53040:00 - 53065:00

it's literally writing the code right

## 53065:00 - 53135:00

now. So in a in a second right here um

## 53135:00 - 53170:00

I'll try and copy and paste it and we'll

## 53170:00 - 53200:00

see if it worked. it usually works

## 53200:00 - 53235:00

pretty well. And again, it's it's not

## 53235:00 - 53285:00

it's not 100% there obviously, but like

## 53285:00 - 53320:00

how I see this is that instead of kind

## 53320:00 - 53355:00

of like trying to, you know, like mindm

## 53355:00 - 53385:00

map out these workflows or kind of like

## 53385:00 - 53425:00

just uh map them out on paper or

## 53425:00 - 53465:00

whatever first, I I literally just tell

## 53465:00 - 53495:00

Cloud what I want to build and then it

## 53495:00 - 53525:00

maps it out for me. And then you kind of

## 53525:00 - 53580:00

like have a canvas that is like 60 70

## 53580:00 - 53625:00

80% there. 80% of the way there

## 53625:00 - 53650:00

complexity of the flow and then you can

## 53650:00 - 53690:00

just like run with that instead.

## 53690:00 - 53725:00

Totally. We're doing the same thing but

## 53725:00 - 53755:00

with perplexity because we found it's

## 53755:00 - 53780:00

really good at hitting like API

## 53780:00 - 53810:00

endpoints. So if I'm going to go hit a

## 53810:00 - 53860:00

rapid API endpoint, um I can include

## 53860:00 - 53890:00

that within the steps. So like you know

## 53890:00 - 53925:00

basically it's like write nad JSON for

## 53925:00 - 53965:00

the following you know flow. Yeah. Um,

## 53965:00 - 54000:00

and then list out like what I'm wanting

## 54000:00 - 54035:00

the thing to do, include the API

## 54035:00 - 54065:00

endpoints that I'm wanting to hit. Um,

## 54065:00 - 54090:00

it's going to go and find that

## 54090:00 - 54125:00

documentation. Um, and then what we'll

## 54125:00 - 54160:00

find is that like most of the times, so

## 54160:00 - 54190:00

we're using perplexity plow with claude

## 54190:00 - 54230:00

4 like as the as the model. Most of the

## 54230:00 - 54255:00

times it'll oneshot it. If it doesn't

## 54255:00 - 54285:00

oneshot it, we'll then take that to

## 54285:00 - 54330:00

claude and be like uh you know it

## 54330:00 - 54365:00

basically if it won't import into n

## 54365:00 - 54395:00

correctly, we just take it to right

## 54395:00 - 54455:00

cloud floor to um have it uh uh fix the

## 54455:00 - 54495:00

code if it made mistakes and it will fix

## 54495:00 - 54520:00

the code within like two prompts

## 54520:00 - 54540:00

typically to actually get the output

## 54540:00 - 54570:00

that will go into it. So anyway, it's

## 54570:00 - 54600:00

just random thing we're seeing work. I

## 54600:00 - 54635:00

think you have to to show me that then

## 54635:00 - 54665:00

because I mean that sounds that sounds

## 54665:00 - 54695:00

amazing. Yeah, I need to make a YouTube

## 54695:00 - 54720:00

video about it. basically like showing

## 54720:00 - 54755:00

the process. One that we did was like we

## 54755:00 - 54780:00

were trying to generate a bunch of

## 54780:00 - 54820:00

vector images quickly. So I had it

## 54820:00 - 54860:00

basically like list of keywords from a a

## 54860:00 - 54900:00

Google sheet. Um it goes through that

## 54900:00 - 54940:00

list of keywords. It generates an image

## 54940:00 - 55005:00

with the chat GPT uh open a um uh or the

## 55005:00 - 55045:00

chat GPT image API. Yeah. Pulls takes

## 55045:00 - 55105:00

that image back. It then goes and uses a

## 55105:00 - 55165:00

AI uh uh background remover to remove

## 55165:00 - 55200:00

the background of the image and then

## 55200:00 - 55240:00

takes that um the remove background

## 55240:00 - 55275:00

version and sends it to a vectorzer to

## 55275:00 - 55305:00

then vectorize that image. And so then

## 55305:00 - 55335:00

basically like make the you know the SVG

## 55335:00 - 55380:00

at scale from you know a list of keyword

## 55380:00 - 55415:00

phrases. So um but anyway that that

## 55415:00 - 55445:00

whole that whole flow was like written

## 55445:00 - 55490:00

entirely by

## 55490:00 - 55530:00

um a perplexity

## 55530:00 - 55570:00

you know a couple perplexity queries. So

## 55570:00 - 55595:00

I mean I mean that's what's so cool like

## 55595:00 - 55650:00

you like sure you need to understand

## 55650:00 - 55690:00

like I guess again like the logic behind

## 55690:00 - 55725:00

and kind of like have a sur at least a

## 55725:00 - 55745:00

surface level understanding but you

## 55745:00 - 55780:00

don't even need to go like that deep

## 55780:00 - 55805:00

especially now like with these tools

## 55805:00 - 55855:00

like literally it it it oneshotted this

## 55855:00 - 55895:00

thing pretty good. So like you have it's

## 55895:00 - 55940:00

based based on a chat message. You can

## 55940:00 - 55965:00

see that we have a couple of tools down

## 55965:00 - 55990:00

here and it it like it even gives you

## 55990:00 - 56010:00

like these sticky notes kind of like

## 56010:00 - 56055:00

explain how the like what tools are uh

## 56055:00 - 56090:00

available, how the workflow works and it

## 56090:00 - 56120:00

even like creates these subworkflows

## 56120:00 - 56150:00

that extracts everything. So I mean

## 56150:00 - 56170:00

again like you can see right here like

## 56170:00 - 56200:00

it just created this node and like these

## 56200:00 - 56225:00

down at the bottom here don't really

## 56225:00 - 56265:00

make any sense but you already have like

## 56265:00 - 56310:00

I mean 70 I'd say 60 to 70% of the flow

## 56310:00 - 56335:00

is already done. You just need to like

## 56335:00 - 56390:00

hook in the your APIs. Um yeah, clean up

## 56390:00 - 56410:00

the data, make sure like everything's

## 56410:00 - 56440:00

pulling correctly and I mean you're

## 56440:00 - 56475:00

you're good to go. So yeah, it's totally

## 56475:00 - 56520:00

totally crazy. No, so like as an

## 56520:00 - 56545:00

example, just for the audience, so we

## 56545:00 - 56575:00

talked about that it was a it was like

## 56575:00 - 56615:00

Twitter API.io or something like that.

## 56615:00 - 56650:00

Yeah, you could basically just reference

## 56650:00 - 56685:00

their API like endpoints within that

## 56685:00 - 56720:00

perplexity call and it's going to go and

## 56720:00 - 56780:00

create that um that node within NAN for

## 56780:00 - 56805:00

you automatically. So just so like

## 56805:00 - 56835:00

people understand how it affects crazy.

## 56835:00 - 56850:00

You definitely need to You need to

## 56850:00 - 56870:00

record that video and send that send

## 56870:00 - 56930:00

that to me. Send it over to

## 56930:00 - 56970:00

Awesome, man. Yo, thank you again for

## 56970:00 - 57010:00

coming on. I appreciate it, man. Um I

## 57010:00 - 57045:00

know my audience is going to be uh super

## 57045:00 - 57065:00

stoked to listen to this and actually

## 57065:00 - 57100:00

see the applications that you're doing.

## 57100:00 - 57135:00

Um and again, we'll uh we'll have to

## 57135:00 - 57160:00

have you back in like, you know, six

## 57160:00 - 57195:00

months uh to to tell us kind of the

## 57195:00 - 57220:00

state of the union of what's going on in

## 57220:00 - 57250:00

AI marketing workflows. So for sure,

## 57250:00 - 57275:00

dude. I love it. Yeah, I appreciate you

## 57275:00 - 57305:00

taking the time to to have me on. It was

## 57305:00 - 57340:00

a blast, man. Awesome, man. Awesome.

## 57340:00 - 57355:00

We'll talk to you soon. Thanks, brother.

## 57355:00+

All right, man. Later.

