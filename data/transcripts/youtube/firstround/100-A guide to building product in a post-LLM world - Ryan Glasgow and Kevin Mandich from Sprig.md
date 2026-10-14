---
source: https://www.youtube.com/watch?v=KOzU-PvRjOg
title: A guide to building product in a post-LLM world | Ryan Glasgow and Kevin
  Mandich from Sprig
author: First Round Capital
date: 2023-09-07
views: 733
description: >-
  Sprig is an AI-powered user insights platform that has raised over $88m.
  Today’s discussion features two key individuals in Sprig’s journey so far:
  Ryan Glasgow, Sprig’s CEO and founder; and Kevin Mandich, Sprig’s Head of
  Machine Learning. Before Sprig, Ryan was an early PM at GraphScience, Vurb,
  and Weeby (all of which were acquired), and Kevin was an ML Engineer at
  Incubit, and a Post-Doctoral Researcher at UC San Diego. 


  In today’s episode, we discuss:

  • Key lessons from the Sprig founding story

  • Product development in the pre vs. post-LLM world

  • How to overcome AI skepticism

  • How to evaluate new models and how to know when to switch

  • Why you need an ML engineer

  • Sprig’s “AI Squad” team structure

  • How Sprig upskills all team members on AI


  Referenced:

  • Auto-GPT: https://github.com/Significant-Gravitas/Auto-GPT

  • Chat GPT: [https://chat.openai.com](https://chat.openai.com/auth/login)

  • Google’s BERT model: https://en.wikipedia.org/wiki/BERT_(language_model)

  • Jira: https://www.atlassian.com/software/jira

  • Jobs to Be Done Framework:
  https://hbr.org/2016/09/know-your-customers-jobs-to-be-done 

  • Langchain: https://www.langchain.com/ 

  • Sprig: https://sprig.com/


  Where to find Ryan Glasgow:

  • Twitter: https://twitter.com/ryanglasgow

  • LinkedIn: https://www.linkedin.com/in/ryanglasgow/


  Where to find Kevin Mandich:

  • Twitter: https://twitter.com/kevinmandich 

  • LinkedIn: https://www.linkedin.com/in/kevinmandich/ 


  Where to find Brett Berson:

  • Twitter: https://twitter.com/brettberson

  • LinkedIn: https://www.linkedin.com/in/brett-berson-9986094/


  Where to find First Round Capital: 

  • Website: https://firstround.com/ 

  • First Round Review: https://review.firstround.com/ 

  • Twitter: https://twitter.com/firstround

  • Youtube: https://www.youtube.com/@FirstRoundCapital 

  • This podcast on all platforms: https://review.firstround.com/podcast 


  Timestamps:

  [00:02:50] Intro

  [00:04:57] What attracted Kevin to Sprig

  [00:05:53] Kevin's background before Sprig

  [00:07:56] How Ryan gained conviction about Kevin

  [00:09:55] Key technical challenges and how they solved them

  [00:18:46] How to overcome AI skepticism

  [00:21:47] The early difficulties of building an ML-enabled product

  [00:25:06] Evaluating new models and knowing when to switch

  [00:35:09] Using Chat GPT

  [00:37:23] Product development in the pre vs. post-LLM world

  [00:39:53] The impact of AI hype on Sprig's product development

  [00:45:36] Balancing AI automation with user-psychology

  [00:48:47] Do recent LLMs reduce Sprig's competitive advantage?

  [00:51:00] The importance of "selling the vision" to customers

  [00:54:40] How Sprig structures teams

  [00:57:25] How Sprig upskills all team members on AI

  [01:00:25] 3 key tips for companies trying to navigate AI

  [01:06:05] Major limitations with LLMs right now

  [01:10:27] The future of AI and the future of Sprig
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:44:47.727Z
---

# A guide to building product in a post-LLM world | Ryan Glasgow and Kevin Mandich from Sprig

## 00:00 - 35:00

but what if you could actually apply the

## 35:00 - 80:00

concepts of Auto GPT and say write a

## 80:00 - 125:00

product spec about how to improve the

## 125:00 - 165:00

onboarding flow and the AI could then

## 165:00 - 220:00

run the sprig study you know for you

## 220:00 - 275:00

design the questions launch it optimize

## 275:00 - 300:00

the studies as getting just the

## 300:00 - 330:00

responses that you need when the results

## 330:00 - 365:00

are done analyze all the results for you

## 365:00 - 395:00

and actually write the products back

## 395:00 - 430:00

based on the results that I found and

## 430:00 - 470:00

then you have a product spec that is

## 470:00 - 505:00

typically considered multiple jobs to be

## 505:00 - 535:00

done but you're actually delivering a

## 535:00 - 560:00

very complex task the air is able to

## 560:00 - 605:00

break down into smaller subtasks and

## 605:00 - 635:00

then complete and you actually get this

## 635:00 - 670:00

kind of end result

## 670:00 - 700:00

thank you

## 700:00 - 760:00

welcome to in-depth a show that surfaces

## 760:00 - 805:00

tactical advice Founders and startup

## 805:00 - 835:00

leaders need to grow their teams

## 835:00 - 875:00

companies and themselves I'm Brett

## 875:00 - 915:00

Burson a partner at first round and

## 915:00 - 940:00

we're a venture capital firm that helps

## 940:00 - 980:00

startups like notion Roblox Uber and

## 980:00 - 1035:00

square tackle company building firsts on

## 1035:00 - 1075:00

the in-depth podcast we share weekly

## 1075:00 - 1110:00

conversations with startup leaders that

## 1110:00 - 1150:00

skip the talking points and go deeper

## 1150:00 - 1210:00

into not just what to do but how to do

## 1210:00 - 1260:00

it learn more And subscribe today at

## 1260:00 - 1295:00

firstbrand.com for today's episode of

## 1295:00 - 1325:00

in-depth I'm thrilled to be joined by

## 1325:00 - 1380:00

Ryan Glasgow and Kevin mandish Brian is

## 1380:00 - 1415:00

the founder and CEO of sprig user

## 1415:00 - 1455:00

insights platform help product teams

## 1455:00 - 1490:00

build phenomenal products Kevin is

## 1490:00 - 1520:00

Spriggs head of machine learning and was

## 1520:00 - 1550:00

actually the company's first hire back

## 1550:00 - 1600:00

in 2019. plenty of startups are now in

## 1600:00 - 1635:00

the throes of trying to integrate AI

## 1635:00 - 1665:00

into their products but for sprig

## 1665:00 - 1705:00

applied ml has been recorded product

## 1705:00 - 1745:00

idea since the very beginning which is

## 1745:00 - 1780:00

why the founding team brought Kevin in

## 1780:00 - 1815:00

on the ground floor we start today by

## 1815:00 - 1845:00

talking about how Ryan gained conviction

## 1845:00 - 1890:00

on hiring Kevin in such a pivotal role

## 1890:00 - 1925:00

despite not being an expert in the space

## 1925:00 - 1960:00

next we discuss how the startup

## 1960:00 - 1995:00

approached some of its earliest ml

## 1995:00 - 2035:00

projects which was the ability to take a

## 2035:00 - 2070:00

bunch of survey responses and pieces of

## 2070:00 - 2105:00

customer feedback and distill them down

## 2105:00 - 2140:00

into actionable takeaways and insights

## 2140:00 - 2185:00

Ryan talks about his own learnings as a

## 2185:00 - 2215:00

founder and how in many ways working

## 2215:00 - 2250:00

with AI the right way is a bit like

## 2250:00 - 2285:00

being an experienced manager versus a

## 2285:00 - 2320:00

first-time manager first-time managers

## 2320:00 - 2350:00

often get frustrated when a direct

## 2350:00 - 2385:00

report goes about the task in a way

## 2385:00 - 2410:00

that's different than how the manager

## 2410:00 - 2435:00

would approach it but experienced

## 2435:00 - 2465:00

managers understand that multiple

## 2465:00 - 2500:00

approaches can be correct we then

## 2500:00 - 2535:00

discuss all of the different Ai and ml

## 2535:00 - 2570:00

Technologies available to builders today

## 2570:00 - 2595:00

and housebrigg is approaching the

## 2595:00 - 2630:00

decision of what to prioritize and

## 2630:00 - 2665:00

integrate into their own product roadmap

## 2665:00 - 2705:00

this conversation with Ryan and Kevin is

## 2705:00 - 2730:00

something I think a lot of folks will

## 2730:00 - 2765:00

find relevant to some of the decisions

## 2765:00 - 2800:00

they're facing at their own companies

## 2800:00 - 2830:00

today I hope you enjoy the conversation

## 2830:00 - 2880:00

I thought maybe kind of a place to

## 2880:00 - 2920:00

Anchor the conversation is how you

## 2920:00 - 2975:00

thought about applied ml in the context

## 2975:00 - 3015:00

of of founding sprig about five years

## 3015:00 - 3045:00

ago maybe Ryan you could talk a little

## 3045:00 - 3080:00

bit about the role it played in the very

## 3080:00 - 3120:00

very early version of the product and

## 3120:00 - 3145:00

ultimately how it's sort of overlaid

## 3145:00 - 3180:00

with bringing Kevin in to lead the

## 3180:00 - 3210:00

function kind of at the the ground floor

## 3210:00 - 3235:00

this is very much building on the

## 3235:00 - 3250:00

previous

## 3250:00 - 3305:00

in-depth uh review Brad that we recorded

## 3305:00 - 3350:00

uh perhaps two years ago about the early

## 3350:00 - 3385:00

days of sprig and really the unmet need

## 3385:00 - 3425:00

what we're looking to solve for in the

## 3425:00 - 3460:00

market and how that really and Matt need

## 3460:00 - 3490:00

came about I think it's exciting now and

## 3490:00 - 3530:00

very relevant to talk about AI work that

## 3530:00 - 3570:00

was happening in parallel to really you

## 3570:00 - 3595:00

know discovering that unmet need and

## 3595:00 - 3625:00

thinking about building something that

## 3625:00 - 3670:00

didn't exist in the market up until then

## 3670:00 - 3725:00

and in the X explorations of that unmet

## 3725:00 - 3755:00

need and what the customers were looking

## 3755:00 - 3800:00

for they were looking for a a way to

## 3800:00 - 3850:00

collect qualitative product experience

## 3850:00 - 3915:00

data from their users at scale and only

## 3915:00 - 3945:00

half of the job to be done was

## 3945:00 - 3975:00

collecting that data the other half was

## 3975:00 - 4005:00

understanding that data and in that

## 4005:00 - 4055:00

process of manually building out reports

## 4055:00 - 4100:00

or the early spring customers and

## 4100:00 - 4165:00

sending over a deck of analysis found

## 4165:00 - 4215:00

out that the collection of the data was

## 4215:00 - 4255:00

really interesting and insightful but it

## 4255:00 - 4300:00

was actually the ability to quantify the

## 4300:00 - 4340:00

survey data and the qualitative data at

## 4340:00 - 4380:00

the time was actually what made the data

## 4380:00 - 4435:00

so revolutionary for the customers that

## 4435:00 - 4475:00

we're working with and realizing that it

## 4475:00 - 4510:00

was something that had not been done in

## 4510:00 - 4565:00

the time around open text analysis of

## 4565:00 - 4610:00

data and realizing that needed to really

## 4610:00 - 4645:00

think about this with a new approach you

## 4645:00 - 4680:00

know started to work with Kevin on a

## 4680:00 - 4720:00

prototype and build lot of prototype and

## 4720:00 - 4750:00

so we realized that there's there's

## 4750:00 - 4790:00

actually enough progress here to see

## 4790:00 - 4810:00

that this is actually something that

## 4810:00 - 4855:00

might be possible to build and that's

## 4855:00 - 4890:00

when Kevin you know joined Sprague full

## 4890:00 - 4920:00

time and and really joined in Spring's

## 4920:00 - 4950:00

earliest days as a founding team member

## 4950:00 - 4990:00

I can add to that also

## 4990:00 - 5010:00

um one of the things that really

## 5010:00 - 5045:00

attracted me in addition to you know the

## 5045:00 - 5070:00

problem space which I had experienced

## 5070:00 - 5095:00

even as an engineer

## 5095:00 - 5135:00

um you know Ryan's having lived this

## 5135:00 - 5170:00

before and his ability to you know

## 5170:00 - 5205:00

articulate the problem and his idea to

## 5205:00 - 5240:00

solve it one thing that really spoke to

## 5240:00 - 5280:00

me was the analysis of for example

## 5280:00 - 5315:00

opentec survey responses or just open

## 5315:00 - 5355:00

text feedback in general you know that

## 5355:00 - 5390:00

is probably the most data Rich feedback

## 5390:00 - 5415:00

Source there is

## 5415:00 - 5440:00

um and historically it's really hard to

## 5440:00 - 5470:00

been hard to analyze that you know

## 5470:00 - 5505:00

people have done word clouds word counts

## 5505:00 - 5550:00

topic modeling but you know none of

## 5550:00 - 5585:00

those really capture the Nuance of of

## 5585:00 - 5635:00

what people are saying and uh you know

## 5635:00 - 5655:00

it doesn't account for the fact that

## 5655:00 - 5675:00

people could be saying multiple things

## 5675:00 - 5705:00

per response you you know natural

## 5705:00 - 5755:00

language is very messy and I saw all

## 5755:00 - 5790:00

these as sort of like a signal that

## 5790:00 - 5820:00

there's really something special that we

## 5820:00 - 5850:00

could build here um and there's a really

## 5850:00 - 5885:00

lots of untapped data that's out there

## 5885:00 - 5925:00

before you join Kevin maybe you could

## 5925:00 - 5950:00

talk a little bit about some of the

## 5950:00 - 5990:00

things that you had done that

## 5990:00 - 6045:00

transferred well into the role at sprig

## 6045:00 - 6070:00

yeah definitely you know as a quick

## 6070:00 - 6105:00

background I worked as a machine

## 6105:00 - 6130:00

learning engineer for pretty much all my

## 6130:00 - 6175:00

career it's close to 10 years now prior

## 6175:00 - 6195:00

to this it worked at a variety of

## 6195:00 - 6235:00

different companies in the tech space uh

## 6235:00 - 6285:00

legal Tech I worked at a email security

## 6285:00 - 6310:00

company trying to solve the spearfishing

## 6310:00 - 6350:00

problem worked at a computer vision

## 6350:00 - 6390:00

startup for a little while

## 6390:00 - 6415:00

um and prior to sprig actually didn't

## 6415:00 - 6440:00

have any experience in the NLP space

## 6440:00 - 6480:00

that was sort of brand new to be but you

## 6480:00 - 6505:00

know one of the things about machine

## 6505:00 - 6545:00

learning and AI in this industry is that

## 6545:00 - 6575:00

there's a lot of crossover between these

## 6575:00 - 6605:00

different data domains you know if

## 6605:00 - 6630:00

you're able to solve a computer vision

## 6630:00 - 6660:00

problem pretty well a lot of those

## 6660:00 - 6685:00

skills are transferable to natural

## 6685:00 - 6730:00

language or to time series processing or

## 6730:00 - 6760:00

audio processing and so you know I think

## 6760:00 - 6790:00

Ryan realized that and saw that as well

## 6790:00 - 6830:00

when we started looking at this data I'm

## 6830:00 - 6860:00

doing a kind of a quick POC on the

## 6860:00 - 6890:00

analysis I was able to show pretty

## 6890:00 - 6920:00

quickly I think that uh there was

## 6920:00 - 6950:00

something there and that we could

## 6950:00 - 6970:00

potentially build out something like

## 6970:00 - 7005:00

this so you know in that sense I think

## 7005:00 - 7040:00

yeah like like I said the the skills

## 7040:00 - 7075:00

were transferable and we're able to use

## 7075:00 - 7100:00

them to to come up with something

## 7100:00 - 7135:00

relatively quickly I'll just say one

## 7135:00 - 7155:00

thing that I think was interesting is

## 7155:00 - 7195:00

that the work that Kevin and you know

## 7195:00 - 7225:00

had built here at Sprigg had never been

## 7225:00 - 7250:00

done before you know in the broader

## 7250:00 - 7290:00

category there was no prior concept of

## 7290:00 - 7325:00

the Senate have you made ever built in a

## 7325:00 - 7350:00

production system and so I think for

## 7350:00 - 7380:00

anyone who's looking at

## 7380:00 - 7415:00

you know the field of AI a lot of the

## 7415:00 - 7460:00

work uh maybe now has been done but at

## 7460:00 - 7500:00

the time it was all Greenfield work and

## 7500:00 - 7530:00

so it was less about finding someone who

## 7530:00 - 7555:00

had actually done what we were looking

## 7555:00 - 7580:00

to do because it hadn't been done before

## 7580:00 - 7600:00

it was actually about finding someone

## 7600:00 - 7645:00

who can solve very difficult problems

## 7645:00 - 7680:00

and so Kevin was very much someone who

## 7680:00 - 7705:00

was looking to solve something that we

## 7705:00 - 7730:00

hadn't solved at Sprague we hadn't seen

## 7730:00 - 7755:00

anyone else solve and that's really I

## 7755:00 - 7790:00

think what you know attracted him to the

## 7790:00 - 7810:00

problem but also something that I think

## 7810:00 - 7840:00

was important bringing someone in as

## 7840:00 - 7860:00

someone who was really excited about

## 7860:00 - 7880:00

solving something that hadn't been done

## 7880:00 - 7910:00

and felt very comfortable and confident

## 7910:00 - 7945:00

in tackling that type of problem Ryan

## 7945:00 - 7990:00

how did you get to conviction on Kevin

## 7990:00 - 8035:00

specifically given how important a role

## 8035:00 - 8070:00

was at that point in the company's life

## 8070:00 - 8100:00

it was also an area that you weren't

## 8100:00 - 8135:00

sort of a domain expert in and it was

## 8135:00 - 8170:00

also an area that I think historically

## 8170:00 - 8220:00

attracted very research oriented versus

## 8220:00 - 8255:00

production oriented people which I think

## 8255:00 - 8275:00

has its own set of challenges when

## 8275:00 - 8300:00

you're a few people kind of getting a

## 8300:00 - 8325:00

product off the ground not kind of an at

## 8325:00 - 8355:00

scale business with a research function

## 8355:00 - 8390:00

so I'd be curious like what was the the

## 8390:00 - 8425:00

what was the mutual courting process and

## 8425:00 - 8460:00

evaluation process that ultimately got

## 8460:00 - 8490:00

got you to conviction that Kevin was the

## 8490:00 - 8520:00

right fit for the role so with Kevin it

## 8520:00 - 8545:00

was really digging into the AI work that

## 8545:00 - 8580:00

he had done and really understanding the

## 8580:00 - 8605:00

type of work that he had done that

## 8605:00 - 8640:00

hadn't been done before in the field of

## 8640:00 - 8675:00

AI I think email fishing was one that he

## 8675:00 - 8700:00

mentioned very large scale email

## 8700:00 - 8740:00

phishing and something that was very new

## 8740:00 - 8785:00

and really digging into with his in the

## 8785:00 - 8815:00

reference checks and in the interviews

## 8815:00 - 8875:00

deeply understanding how you know he was

## 8875:00 - 8910:00

involved in bringing something new to

## 8910:00 - 8945:00

the company that he was at and talked to

## 8945:00 - 8985:00

other ml injuries as well as references

## 8985:00 - 9030:00

and talk to Kevin's own references and

## 9030:00 - 9060:00

the one theme that we've seen with

## 9060:00 - 9110:00

world-class ml Engineers is they are

## 9110:00 - 9130:00

often some of the smartest people that

## 9130:00 - 9155:00

you'll know and in Kevin's references

## 9155:00 - 9195:00

that was very clear multiple people and

## 9195:00 - 9215:00

I've never had some references before

## 9215:00 - 9245:00

multiple people told me this is you know

## 9245:00 - 9280:00

unequivocally the smartest person they

## 9280:00 - 9305:00

know and usually there's really really

## 9305:00 - 9335:00

smart people are attracted to these

## 9335:00 - 9375:00

really really hard problems and with ML

## 9375:00 - 9425:00

and data science it is in my opinion in

## 9425:00 - 9460:00

engineering some of the more difficult

## 9460:00 - 9500:00

Cutting Edge Frontier problems that are

## 9500:00 - 9520:00

being solved you know in the technology

## 9520:00 - 9555:00

landscape and so making sure that the

## 9555:00 - 9590:00

slope is there is really critical as

## 9590:00 - 9620:00

someone who's really smart just because

## 9620:00 - 9655:00

the AI field is changing and

## 9655:00 - 9695:00

particularly this year every week it's

## 9695:00 - 9725:00

rapidly changing and so you're going to

## 9725:00 - 9760:00

need someone who you can't rely on their

## 9760:00 - 9810:00

prior experience you have to be able to

## 9810:00 - 9840:00

look at what you think they can do in

## 9840:00 - 9875:00

the future and that's ultimately what's

## 9875:00 - 9895:00

going to determine whether they're

## 9895:00 - 9935:00

successful in that new role or not so

## 9935:00 - 9960:00

that's some good context setting so

## 9960:00 - 9985:00

before we spend a lot of the time

## 9985:00 - 10010:00

talking about how you've approached

## 10010:00 - 10035:00

implementing a bunch of the new stuff

## 10035:00 - 10080:00

happening in llms maybe Kevin you could

## 10080:00 - 10115:00

share a little bit about when you joined

## 10115:00 - 10180:00

explain how you approached applied ml in

## 10180:00 - 10200:00

the context of sprig in the product

## 10200:00 - 10235:00

experience in the early days and maybe

## 10235:00 - 10265:00

it you know obviously not too much in

## 10265:00 - 10290:00

the weeds from a technical depth

## 10290:00 - 10315:00

perspective but maybe talk about kind of

## 10315:00 - 10345:00

the product surface area and what you're

## 10345:00 - 10370:00

what you're doing maybe at a little

## 10370:00 - 10400:00

higher level on the the product sorry on

## 10400:00 - 10440:00

the engineering side to to sort of build

## 10440:00 - 10470:00

those features call it three or four

## 10470:00 - 10505:00

years ago you know maybe I can focus on

## 10505:00 - 10550:00

kind of our first major application of

## 10550:00 - 10580:00

ml at sprig you know this is at a high

## 10580:00 - 10610:00

level the ability to take a bunch of

## 10610:00 - 10645:00

responses feedback survey responses

## 10645:00 - 10670:00

whatever it is and uh you know

## 10670:00 - 10705:00

categorize them or distill them down

## 10705:00 - 10740:00

into actionable takeaways that's

## 10740:00 - 10780:00

essentially what researchers do and so a

## 10780:00 - 10810:00

lot a lot of interesting facets to that

## 10810:00 - 10845:00

problem one of which is it's a very

## 10845:00 - 10880:00

subjective problem you can take two

## 10880:00 - 10915:00

expert user researchers give them the

## 10915:00 - 10950:00

same list of you know 500 responses tell

## 10950:00 - 10975:00

them to distill them down into 10

## 10975:00 - 11005:00

actionable takeaways and those 10 will

## 11005:00 - 11040:00

be completely different or even if they

## 11040:00 - 11095:00

are the same 10 takeaways the responses

## 11095:00 - 11115:00

that would go into each of those buckets

## 11115:00 - 11145:00

could be completely different it's just

## 11145:00 - 11175:00

you know based on the person's their

## 11175:00 - 11210:00

history their education and what they're

## 11210:00 - 11245:00

really trying to get out of research

## 11245:00 - 11265:00

um you know that that changes from

## 11265:00 - 11290:00

person to person so that's that's number

## 11290:00 - 11330:00

one um and maybe a better assisting way

## 11330:00 - 11360:00

of saying that is that there's really no

## 11360:00 - 11385:00

Universal source of Truth for an

## 11385:00 - 11415:00

analysis like that so that makes it kind

## 11415:00 - 11460:00

of difficult in classic ml you want an

## 11460:00 - 11485:00

input and an output that's very cut and

## 11485:00 - 11515:00

dry and you want to be able to say with

## 11515:00 - 11545:00

certainty this output is correct or it's

## 11545:00 - 11575:00

not but with this application that was

## 11575:00 - 11605:00

very difficult to do so that I think

## 11605:00 - 11640:00

made a few things necessary on the

## 11640:00 - 11670:00

product and the engineering side one of

## 11670:00 - 11710:00

which was having you know a human in the

## 11710:00 - 11750:00

loop approach to make sure that even if

## 11750:00 - 11780:00

we didn't get the answers that our

## 11780:00 - 11810:00

customers expected or wanted or didn't

## 11810:00 - 11855:00

align with their analysis we'd be able

## 11855:00 - 11885:00

to to modify it and that also included

## 11885:00 - 11920:00

making this system as flexible as

## 11920:00 - 11970:00

possible so an example would be at one

## 11970:00 - 12015:00

point we implemented per customer models

## 12015:00 - 12045:00

so we would take you know our base model

## 12045:00 - 12090:00

fine tune it on the data from a single

## 12090:00 - 12120:00

customer and make that their base model

## 12120:00 - 12160:00

and then from there depending on how you

## 12160:00 - 12195:00

know different we needed to to make the

## 12195:00 - 12240:00

results we could also do like per survey

## 12240:00 - 12275:00

models so you know take they basically

## 12275:00 - 12320:00

different have have different levels of

## 12320:00 - 12350:00

trained models for these different use

## 12350:00 - 12385:00

cases and that helped to get us a long

## 12385:00 - 12435:00

way towards per customer per user

## 12435:00 - 12460:00

customization so those are some of the

## 12460:00 - 12495:00

main challenges other ones include the

## 12495:00 - 12550:00

fact that if you're running a survey you

## 12550:00 - 12580:00

are continuously Gathering data in real

## 12580:00 - 12615:00

time and our customers expect to see

## 12615:00 - 12665:00

these results analyzed in real time so

## 12665:00 - 12685:00

that makes kind of an interesting

## 12685:00 - 12705:00

situation where you know you're getting

## 12705:00 - 12745:00

a constant trickle of responses from an

## 12745:00 - 12760:00

ml point of view I think it's

## 12760:00 - 12805:00

advantageous to analyze as much data in

## 12805:00 - 12840:00

batch as possible you tend to get more

## 12840:00 - 12860:00

information to work with so you have

## 12860:00 - 12905:00

these two conflicting sort of ideas and

## 12905:00 - 12935:00

so we had to come up with a system that

## 12935:00 - 12985:00

allowed us to take advantage of us all

## 12985:00 - 13010:00

the information we had at any one point

## 13010:00 - 13045:00

in time to be able to continuously

## 13045:00 - 13095:00

deliver results to our customers and and

## 13095:00 - 13115:00

I do want to take into that first point

## 13115:00 - 13130:00

because that was something that's been

## 13130:00 - 13160:00

really interesting and unique about Ai

## 13160:00 - 13195:00

and applications of AI is it reminds me

## 13195:00 - 13220:00

almost as a first-time manager because a

## 13220:00 - 13250:00

first-time manager you delegate a task

## 13250:00 - 13275:00

to someone and they do it differently

## 13275:00 - 13315:00

and you know there's a very wide set of

## 13315:00 - 13350:00

permutations for a task and then that

## 13350:00 - 13385:00

first-time manager might say this ask is

## 13385:00 - 13400:00

done incorrectly because it's different

## 13400:00 - 13430:00

than how I would do it but an experience

## 13430:00 - 13470:00

manager might say that you are doing

## 13470:00 - 13495:00

this task in a different way than I

## 13495:00 - 13525:00

would do it and it is still considered

## 13525:00 - 13555:00

correct and so with our own set of

## 13555:00 - 13595:00

customers they often would say you know

## 13595:00 - 13645:00

this is wrong but it was actually the AI

## 13645:00 - 13690:00

had a different way of coming out with

## 13690:00 - 13725:00

the conclusion or the answer and so when

## 13725:00 - 13760:00

you get into as we I think Trend towards

## 13760:00 - 13800:00

artificial general intelligence the

## 13800:00 - 13835:00

definition of correct or the definition

## 13835:00 - 13875:00

of whether something is you know valid

## 13875:00 - 13905:00

or not is becoming increasingly

## 13905:00 - 13935:00

subjective and so when you're Building

## 13935:00 - 13990:00

Technology that could have a wide range

## 13990:00 - 14035:00

of permutations how do you actually work

## 14035:00 - 14075:00

with your customers on what the correct

## 14075:00 - 14110:00

the definition of correct is I think

## 14110:00 - 14125:00

that's something that we've kind of gone

## 14125:00 - 14160:00

back and forth of of really kind of

## 14160:00 - 14195:00

working through and it's certainly not

## 14195:00 - 14215:00

solved and I think it's going to take us

## 14215:00 - 14255:00

a while for as an industry but it's

## 14255:00 - 14275:00

something that you know kid was touching

## 14275:00 - 14295:00

on is how do you kind of incorporate

## 14295:00 - 14345:00

customer subjectivity into building AI

## 14345:00 - 14365:00

which is something that's really new for

## 14365:00 - 14390:00

the people building their products but

## 14390:00 - 14410:00

also the people using products as well

## 14410:00 - 14455:00

it's a really interesting way to frame

## 14455:00 - 14490:00

it so to pull on that a little bit how

## 14490:00 - 14515:00

did you answer that or sort of figure

## 14515:00 - 14550:00

that out in the first few years of sprig

## 14550:00 - 14580:00

let's see well maybe you could back up a

## 14580:00 - 14595:00

little bit

## 14595:00 - 14635:00

um and say that's actually not where we

## 14635:00 - 14665:00

landed to begin with

## 14665:00 - 14685:00

um you know I think at the very

## 14685:00 - 14715:00

beginning we tried to follow the Mantra

## 14715:00 - 14750:00

of you know keep it simple try the

## 14750:00 - 14780:00

simple thing first if that doesn't work

## 14780:00 - 14815:00

then you increase in complexity you know

## 14815:00 - 14840:00

I think the very first attempt we made

## 14840:00 - 14880:00

at this uh which we thought could work

## 14880:00 - 14910:00

because at the time we had a relatively

## 14910:00 - 14945:00

narrow customer base and a narrow data

## 14945:00 - 14985:00

set a narrow data domain and that was

## 14985:00 - 15030:00

basically like a a categorization sort

## 15030:00 - 15060:00

of approach so you know of all the

## 15060:00 - 15080:00

things you could ask somebody about

## 15080:00 - 15115:00

their use in a product maybe there are

## 15115:00 - 15150:00

10 big primary themes you could talk

## 15150:00 - 15185:00

about you know ease of use user

## 15185:00 - 15230:00

interface pricing support whatever and

## 15230:00 - 15255:00

maybe within each of those you have some

## 15255:00 - 15285:00

subcategories so kind of a hierarchical

## 15285:00 - 15320:00

categorization and we found pretty

## 15320:00 - 15360:00

quickly even for our narrow subset of

## 15360:00 - 15400:00

initial customers that this just didn't

## 15400:00 - 15430:00

capture everything like I mentioned

## 15430:00 - 15455:00

language is very nuanced but also

## 15455:00 - 15490:00

people's needs and thoughts about how

## 15490:00 - 15520:00

they're using a product are very nuanced

## 15520:00 - 15550:00

you know somebody could be talking about

## 15550:00 - 15595:00

the you know maybe they want cheaper

## 15595:00 - 15615:00

pricing for the product and somebody

## 15615:00 - 15645:00

else could be saying you know they want

## 15645:00 - 15675:00

team pricing instead of individual

## 15675:00 - 15705:00

pricing a really basic analysis would

## 15705:00 - 15740:00

put those two together but they're

## 15740:00 - 15760:00

really talking about different things

## 15760:00 - 15790:00

and so that's an example of why we

## 15790:00 - 15815:00

decided to go with something a little

## 15815:00 - 15855:00

more you know complex and nuanced how

## 15855:00 - 15885:00

did you think about solving and maybe

## 15885:00 - 15925:00

Ryan you want to take this that issue of

## 15925:00 - 15960:00

the difference between kind of this is

## 15960:00 - 15990:00

what I was expecting versus this is

## 15990:00 - 16025:00

correct and the fact that maybe at a lot

## 16025:00 - 16060:00

of companies those two things were

## 16060:00 - 16100:00

distinct or was that more like a 301

## 16100:00 - 16125:00

problem that you were working on not

## 16125:00 - 16155:00

kind of a 101 problem yeah it was

## 16155:00 - 16225:00

definitely a 101 or v.1.0 was a human

## 16225:00 - 16260:00

Loop solution and so we built open

## 16260:00 - 16295:00

source models it would take a first pass

## 16295:00 - 16340:00

it would be you know generally correct

## 16340:00 - 16370:00

we would have people with internal

## 16370:00 - 16415:00

tooling review all the output

## 16415:00 - 16455:00

before we shipped it to our customers to

## 16455:00 - 16485:00

view in the interface and we originally

## 16485:00 - 16525:00

hired Amazon Mechanical Turks and we

## 16525:00 - 16545:00

said hey we'll save money we'll have

## 16545:00 - 16580:00

three of them review every response but

## 16580:00 - 16630:00

we'd often see that even if all three of

## 16630:00 - 16670:00

them gave the same output we would go to

## 16670:00 - 16705:00

an expert researcher or a customer or

## 16705:00 - 16735:00

look at the data ourselves and often

## 16735:00 - 16775:00

disagree and then so the AI might come

## 16775:00 - 16805:00

up with one thing our human the loot

## 16805:00 - 16825:00

process might have another and our

## 16825:00 - 16840:00

customer might have it so it's actually

## 16840:00 - 16885:00

three different inputs and getting all

## 16885:00 - 16925:00

three to degree degrees was you know

## 16925:00 - 16965:00

very challenging and so we brought on a

## 16965:00 - 16995:00

world-class researcher who was actually

## 16995:00 - 17045:00

on a faculty at Yale as one of our other

## 17045:00 - 17100:00

you know very early team members she was

## 17100:00 - 17135:00

actually the fourth person to joined

## 17135:00 - 17185:00

Sprague and her first role was reviewing

## 17185:00 - 17225:00

this is a very experienced you know

## 17225:00 - 17275:00

world-class researcher you know who is

## 17275:00 - 17325:00

studying quantitative research at Yale

## 17325:00 - 17380:00

come on and actually be that individual

## 17380:00 - 17430:00

who is stamping and approving and tuning

## 17430:00 - 17475:00

the AI and so we at least knew that we

## 17475:00 - 17510:00

have someone with some level of

## 17510:00 - 17550:00

expertise and even though it's one

## 17550:00 - 17575:00

person it's not three mechanical Turks

## 17575:00 - 17595:00

per response it's one person per

## 17595:00 - 17635:00

response saying that we believe

## 17635:00 - 17675:00

definitively based on what we know this

## 17675:00 - 17710:00

is the proper way that the AI should

## 17710:00 - 17750:00

categorize this data and so she really

## 17750:00 - 17775:00

worked with Kevin very closely in the

## 17775:00 - 17820:00

early days to build and fine-tune what

## 17820:00 - 17860:00

correct was and with customers though

## 17860:00 - 17895:00

that was the piece that they will always

## 17895:00 - 17935:00

have their own preferences and nuances

## 17935:00 - 17975:00

and they'll always be some level of Gap

## 17975:00 - 18015:00

and so what we've done in our how we

## 18015:00 - 18055:00

display the data to our customers is

## 18055:00 - 18100:00

make it clear to them and give them the

## 18100:00 - 18150:00

ability to then modify and correct to

## 18150:00 - 18180:00

the hundred percent their own definition

## 18180:00 - 18225:00

their 100 definition of correct because

## 18225:00 - 18255:00

we will never it's very likely to ever

## 18255:00 - 18295:00

get to 100 and so we'll get you know 90

## 18295:00 - 18335:00

95.99 and but we'll always make sure

## 18335:00 - 18365:00

that they have the ability to then do

## 18365:00 - 18400:00

that last mile of analysis on their own

## 18400:00 - 18425:00

and so that's something that we have

## 18425:00 - 18460:00

delegated and put that responsibility on

## 18460:00 - 18480:00

our customers instead of taking on

## 18480:00 - 18515:00

ourselves in those early days did you

## 18515:00 - 18570:00

find that there was specific Nuance in

## 18570:00 - 18625:00

building these ml enabled features that

## 18625:00 - 18650:00

from either a product development

## 18650:00 - 18675:00

process or the way that you interface

## 18675:00 - 18710:00

with customers that felt different than

## 18710:00 - 18750:00

building let's say traditional features

## 18750:00 - 18790:00

and functionality and software yeah one

## 18790:00 - 18815:00

thing that really stood out was the

## 18815:00 - 18855:00

skepticism particularly this was 2019

## 18855:00 - 18885:00

when we started selling this the

## 18885:00 - 18925:00

skepticism around the AI you know that

## 18925:00 - 18955:00

we had built and skepticism around that

## 18955:00 - 19000:00

entire AI you know what was possible

## 19000:00 - 19025:00

they are because we meet with so many

## 19025:00 - 19060:00

teams you know even some of the our

## 19060:00 - 19100:00

largest customers today they had tried

## 19100:00 - 19130:00

all the AI Solutions around text

## 19130:00 - 19170:00

analysis and NLP I said we've tried them

## 19170:00 - 19200:00

you know they don't meet our needs or

## 19200:00 - 19230:00

they say they work great but we've tried

## 19230:00 - 19260:00

them and they don't work well and I

## 19260:00 - 19280:00

think they're still seeing a lot of this

## 19280:00 - 19330:00

today there's some very Buzzy hot gen ad

## 19330:00 - 19365:00

companies you look at the home page but

## 19365:00 - 19405:00

we're very excited you hear about the

## 19405:00 - 19435:00

user feedback on Twitter and it's not

## 19435:00 - 19460:00

delivering on the promise that's

## 19460:00 - 19480:00

something that we had been dealing in

## 19480:00 - 19505:00

you know Kevin and dealing with from day

## 19505:00 - 19560:00

one and so how we solved that was a we

## 19560:00 - 19585:00

said with this human Loop process with

## 19585:00 - 19610:00

an expert user researcher who is

## 19610:00 - 19635:00

reviewing all the data before is

## 19635:00 - 19670:00

delivered to customers but then B we

## 19670:00 - 19705:00

actually in the early days generally

## 19705:00 - 19755:00

encouraged every customer to Pilot spray

## 19755:00 - 19800:00

because it was never about listening to

## 19800:00 - 19840:00

us and taking our word it was always

## 19840:00 - 19870:00

about how can we actually get sprig into

## 19870:00 - 19930:00

your hands with your data and let us

## 19930:00 - 19980:00

actually show you how well this AI works

## 19980:00 - 20015:00

because we're not gonna you know sell

## 20015:00 - 20055:00

you and debate and tell you how well it

## 20055:00 - 20075:00

works that's never going to be good

## 20075:00 - 20100:00

enough for you the only way for you to

## 20100:00 - 20145:00

be fully confident and Trust what we

## 20145:00 - 20175:00

built will actually work for you in a

## 20175:00 - 20200:00

production capability just for you to

## 20200:00 - 20225:00

try it with your own data set with your

## 20225:00 - 20250:00

own users and so that's something in the

## 20250:00 - 20290:00

early days we always almost required I

## 20290:00 - 20310:00

can't think of a customer that didn't

## 20310:00 - 20345:00

run a pilot with sprig uh because it was

## 20345:00 - 20370:00

always something where they wanted to

## 20370:00 - 20415:00

see to believe and they'd install spray

## 20415:00 - 20445:00

in their product they would get that

## 20445:00 - 20490:00

data they would start to see the quality

## 20490:00 - 20525:00

of the text analysis that was coming out

## 20525:00 - 20555:00

of the models that we developed with the

## 20555:00 - 20600:00

human Loop process as our commitment

## 20600:00 - 20635:00

uh to them that this is something that

## 20635:00 - 20665:00

they can trust and feel that they can

## 20665:00 - 20690:00

make decisions about and that's how we

## 20690:00 - 20720:00

overcame the hurdle we had 100

## 20720:00 - 20760:00

conversion rate from a pilot to a pain

## 20760:00 - 20790:00

customer and so we felt really good

## 20790:00 - 20820:00

about that promise and taking on that

## 20820:00 - 20860:00

responsibility ourselves and so I think

## 20860:00 - 20880:00

for anyone building with AI right now is

## 20880:00 - 20925:00

how can you overcome the skepticism that

## 20925:00 - 20950:00

you're naturally going to get even today

## 20950:00 - 20990:00

with where models are at and you have to

## 20990:00 - 21015:00

make sure that you're building that into

## 21015:00 - 21050:00

your product promise whether it's on

## 21050:00 - 21075:00

your marketing website or on your sales

## 21075:00 - 21120:00

process that there continues to be a lot

## 21120:00 - 21160:00

of skepticism increasingly in skepticism

## 21160:00 - 21220:00

as more complex tasks are taken on and

## 21220:00 - 21250:00

you have to think about how to overcome

## 21250:00 - 21290:00

that and ultimately letting users try it

## 21290:00 - 21330:00

for themselves uh is the easiest way to

## 21330:00 - 21355:00

overcome that I think what we're going

## 21355:00 - 21385:00

through now is we're probably close to

## 21385:00 - 21425:00

the peak of the current hype cycle that

## 21425:00 - 21450:00

was introduced earlier this year with

## 21450:00 - 21485:00

you know chat gbt and everything right

## 21485:00 - 21515:00

now we're seeing things with seeing

## 21515:00 - 21550:00

issues with uh you know hallucinations

## 21550:00 - 21585:00

with llms other interesting failure

## 21585:00 - 21625:00

modes that are kind of harder to catch

## 21625:00 - 21645:00

them before so it's going to make it

## 21645:00 - 21675:00

even more challenging and potentially

## 21675:00 - 21720:00

make people even more skeptical so it's

## 21720:00 - 21740:00

it's definitely something you have to

## 21740:00 - 21765:00

have top of Mind as you're building out

## 21765:00 - 21820:00

a product like this what did you find as

## 21820:00 - 21845:00

you were building kind of the first

## 21845:00 - 21885:00

version of this sort of ml enabled

## 21885:00 - 21905:00

product what did you find was

## 21905:00 - 21940:00

surprisingly difficult the first one

## 21940:00 - 21980:00

which is probably you know more relevant

## 21980:00 - 22000:00

for folks that are still hosting their

## 22000:00 - 22045:00

own models is that you know we had to

## 22045:00 - 22075:00

figure out how to basically we basically

## 22075:00 - 22110:00

had to build out a large amount of

## 22110:00 - 22150:00

continuous training infrastructure I

## 22150:00 - 22170:00

think I mentioned before that we had

## 22170:00 - 22190:00

models for different customers different

## 22190:00 - 22225:00

surveys Etc that came with a pretty

## 22225:00 - 22260:00

heavy pretty steep learning curve so

## 22260:00 - 22290:00

trying to figure out figure that part

## 22290:00 - 22330:00

out was was pretty challenging and we we

## 22330:00 - 22355:00

were scaling at the point you know in

## 22355:00 - 22390:00

2020 we were scaling to the point we're

## 22390:00 - 22425:00

getting so much uh survey responses

## 22425:00 - 22460:00

increasingly per month and you know we

## 22460:00 - 22490:00

were continuously chipping away in this

## 22490:00 - 22535:00

long tail of model tuning but it was a

## 22535:00 - 22575:00

little bit I think scary just to see

## 22575:00 - 22625:00

that we weren't quite scaling I think

## 22625:00 - 22670:00

quite as fast as we wanted to on the

## 22670:00 - 22700:00

efficacy of the model and how much was

## 22700:00 - 22740:00

able to take on and in 2020 I think you

## 22740:00 - 22770:00

know Kevin hint to this is this trough

## 22770:00 - 22815:00

of Sorrow around ml will it ever get

## 22815:00 - 22845:00

there will it ever deliver on that

## 22845:00 - 22860:00

promise

## 22860:00 - 22885:00

um and there is some skepticism you know

## 22885:00 - 22905:00

in the industry whether it would get

## 22905:00 - 22940:00

there and we did start to you know

## 22940:00 - 22965:00

credit to Kevin continue to chip away

## 22965:00 - 23000:00

every month the model got more and more

## 23000:00 - 23025:00

you know efficient and effective of

## 23025:00 - 23080:00

taking on the analysis from the internal

## 23080:00 - 23115:00

research team and then over the past

## 23115:00 - 23145:00

nine months 12 months now we're at the

## 23145:00 - 23170:00

period where it's actually all real time

## 23170:00 - 23215:00

and so there was that period of are we

## 23215:00 - 23245:00

going to get to where we want to go can

## 23245:00 - 23275:00

the scale it's a level that we need to

## 23275:00 - 23305:00

but we did get there which was

## 23305:00 - 23335:00

definitely something that uh

## 23335:00 - 23395:00

in hindsight you know a risk but

## 23395:00 - 23420:00

something that was not clear at the time

## 23420:00 - 23450:00

and a lot of people were giving up on ML

## 23450:00 - 23495:00

and AI knowing that they're relying too

## 23495:00 - 23535:00

much on that human Loop process and law

## 23535:00 - 23565:00

serves actually went under uh in 2018

## 23565:00 - 23600:00

2020 just realized that they were not

## 23600:00 - 23635:00

going to get there how it is

## 23635:00 - 23700:00

gbt3 and then Chachi BT and this new

## 23700:00 - 23740:00

wave of large language models sort of

## 23740:00 - 23785:00

fit into the Journey of

## 23785:00 - 23835:00

uh sprig thus far I'll start just by

## 23835:00 - 23865:00

giving the context for I think why

## 23865:00 - 23900:00

having an ml engineer is really critical

## 23900:00 - 23925:00

because I think right now there's kind

## 23925:00 - 23940:00

of this

## 23940:00 - 23970:00

thinking is that you know any engineer

## 23970:00 - 24015:00

can be an ml engineer you just use you

## 24015:00 - 24065:00

know chat gbt apis but when we started

## 24065:00 - 24110:00

to think about shifting from Google's

## 24110:00 - 24150:00

open source models to using something

## 24150:00 - 24210:00

from openai I do think it's critical to

## 24210:00 - 24260:00

have at least one you know ml data

## 24260:00 - 24310:00

scientist who is evaluating all the

## 24310:00 - 24330:00

different models out there and really

## 24330:00 - 24360:00

knowing what the local maximum looks

## 24360:00 - 24400:00

like because I would often ask Kevin are

## 24400:00 - 24440:00

we ready to switch to you know open AIS

## 24440:00 - 24475:00

GPT models for the past three years I've

## 24475:00 - 24500:00

been asking that question and you know

## 24500:00 - 24540:00

he was constantly testing and evaluating

## 24540:00 - 24570:00

when it made sense for us to switch over

## 24570:00 - 24610:00

but you don't really know what the

## 24610:00 - 24645:00

absolute Maxim looks like if you're not

## 24645:00 - 24675:00

able to Leverage The Open Source models

## 24675:00 - 24695:00

that are available and that's not

## 24695:00 - 24740:00

something that a typical full stack

## 24740:00 - 24770:00

software engineer is able to fully

## 24770:00 - 24795:00

evaluate because it's not where the

## 24795:00 - 24830:00

model starts it's where the model can

## 24830:00 - 24860:00

get to and that's that unknown piece

## 24860:00 - 24895:00

that's really critical of how far can

## 24895:00 - 24930:00

this model take us and what will the

## 24930:00 - 24960:00

result look like after significant

## 24960:00 - 24995:00

investment and so Kevin was able to kind

## 24995:00 - 25035:00

of test and evaluate when it made sense

## 25035:00 - 25080:00

to reach a new absolute maximum with the

## 25080:00 - 25105:00

efficacy of our models and switch over

## 25105:00 - 25145:00

yeah and Kevin to build on on Ryan's

## 25145:00 - 25175:00

point I would love to hear what your own

## 25175:00 - 25220:00

process was to figure out if this new

## 25220:00 - 25255:00

set of enabling Technologies were right

## 25255:00 - 25300:00

for sprig and at what point in the early

## 25300:00 - 25350:00

days of open ai's models or or others

## 25350:00 - 25385:00

when we were trying to figure out how to

## 25385:00 - 25425:00

use it we basically did the same thing

## 25425:00 - 25450:00

we were doing before when evaluating

## 25450:00 - 25485:00

other open source models you know how to

## 25485:00 - 25545:00

a set of what we call source of Truth

## 25545:00 - 25585:00

data you know surveys from customers

## 25585:00 - 25620:00

customer feedback that we'd have to feed

## 25620:00 - 25660:00

through it and evaluate and see you know

## 25660:00 - 25700:00

how good the model was at performing

## 25700:00 - 25740:00

it's it's uh its function there

## 25740:00 - 25790:00

um what really kicked off our decision

## 25790:00 - 25830:00

to uh to promote this model and to use

## 25830:00 - 25855:00

it in production was you know a

## 25855:00 - 25885:00

discontinuous jump in efficacy that we

## 25885:00 - 25925:00

saw so it was significantly better than

## 25925:00 - 25955:00

what we were using before 4 and we

## 25955:00 - 25985:00

determined that we'd be able to use it

## 25985:00 - 26020:00

at that high level of efficacy ongoing

## 26020:00 - 26050:00

in the future you know assuming we had

## 26050:00 - 26085:00

some ways of being able to continuously

## 26085:00 - 26115:00

test it and make sure it was still able

## 26115:00 - 26145:00

to deliver over time we rolled that out

## 26145:00 - 26170:00

and announced it in May

## 26170:00 - 26215:00

of switching from the previous

## 26215:00 - 26255:00

generation of Google's open source

## 26255:00 - 26310:00

models to you know open areas gpt4 and

## 26310:00 - 26330:00

now we're at this process of now

## 26330:00 - 26370:00

evaluating other models against open

## 26370:00 - 26420:00

aisgpt4 and primarily open source models

## 26420:00 - 26450:00

like law might have C is there any

## 26450:00 - 26490:00

opportunity to augment with other models

## 26490:00 - 26525:00

or perhaps does it make sense to

## 26525:00 - 26560:00

consider other models entirely as a

## 26560:00 - 26585:00

replacement and so I think for any

## 26585:00 - 26635:00

startup given the advancements in the LM

## 26635:00 - 26665:00

field the current model you're using

## 26665:00 - 26700:00

might be the right model today but three

## 26700:00 - 26730:00

months from now 12 months from now

## 26730:00 - 26765:00

there's a good chance that another model

## 26765:00 - 26800:00

might actually surpass the current model

## 26800:00 - 26830:00

that you're using for the specific use

## 26830:00 - 26865:00

case that you have given how fast the

## 26865:00 - 26900:00

landscape is evolving I think that's the

## 26900:00 - 26950:00

key question and becoming you know a not

## 26950:00 - 26975:00

competitive Advantage but you know for

## 26975:00 - 27015:00

teams internally to knowing what model

## 27015:00 - 27050:00

to use and window switch over and will

## 27050:00 - 27095:00

be something I think will be a yeah a

## 27095:00 - 27115:00

key question for a lot of different

## 27115:00 - 27160:00

companies developing with AI how do you

## 27160:00 - 27190:00

think about about building

## 27190:00 - 27235:00

infrastructure around these product

## 27235:00 - 27275:00

features that gives you maximum

## 27275:00 - 27315:00

flexibility in terms of incorporating

## 27315:00 - 27350:00

new models in the future given I assume

## 27350:00 - 27375:00

kind of your Take On The World Is

## 27375:00 - 27400:00

there's going to be all sorts of new

## 27400:00 - 27435:00

interesting technology coming out and

## 27435:00 - 27470:00

you don't want to have dependency risk

## 27470:00 - 27525:00

on a specific llm for example and does

## 27525:00 - 27550:00

it mean that you're approaching Building

## 27550:00 - 27590:00

Products differently today than maybe

## 27590:00 - 27625:00

previously because there's this desire

## 27625:00 - 27670:00

to be able to use whatever the best is

## 27670:00 - 27705:00

at that given point in time one of the

## 27705:00 - 27735:00

key inputs that you know I've been

## 27735:00 - 27785:00

partying with Kevin on and is really

## 27785:00 - 27815:00

understanding the bounds of each model

## 27815:00 - 27850:00

at any given time you know we often

## 27850:00 - 27880:00

think around the jobs to be done that we

## 27880:00 - 27910:00

want to solve for customers we have to

## 27910:00 - 27930:00

look at the different models that are

## 27930:00 - 27960:00

available and see what can this model do

## 27960:00 - 28005:00

for us today and can we test the various

## 28005:00 - 28040:00

use cases and applications for what we

## 28040:00 - 28070:00

want to do with these various models

## 28070:00 - 28120:00

that we've got and it's very much like a

## 28120:00 - 28145:00

you know I'm a one-year-old and I'm not

## 28145:00 - 28175:00

going to ask her to write a bike today

## 28175:00 - 28215:00

it's not a task that she would succeed

## 28215:00 - 28250:00

at you know but I can't ask her to open

## 28250:00 - 28275:00

and close her hand and she's very

## 28275:00 - 28300:00

successful at that and I remember in the

## 28300:00 - 28325:00

early days a lot of people actually

## 28325:00 - 28375:00

asked us to also ingest support tickets

## 28375:00 - 28415:00

and other type of unstructured data into

## 28415:00 - 28460:00

Sprague and we knew the bounds of the

## 28460:00 - 28495:00

model at the time were not successful

## 28495:00 - 28540:00

with unstructured customer support

## 28540:00 - 28590:00

tickets and so what we did was we relied

## 28590:00 - 28635:00

on encourage customers to ask with a

## 28635:00 - 28680:00

template Gallery very specific survey

## 28680:00 - 28725:00

questions about specific moments in time

## 28725:00 - 28765:00

and ask for example how is your

## 28765:00 - 28800:00

experience using this feature for the

## 28800:00 - 28840:00

first time and you get somewhat like a

## 28840:00 - 28885:00

narrow set of data back and the model at

## 28885:00 - 28925:00

the time 2020 2018 it was very

## 28925:00 - 28950:00

successful with a narrow set of

## 28950:00 - 28975:00

structured data and so I think that's an

## 28975:00 - 29010:00

application you know a kind of example

## 29010:00 - 29035:00

today that's still very relevant is you

## 29035:00 - 29065:00

have to kind of understand the bounds of

## 29065:00 - 29095:00

what the model can do is it a

## 29095:00 - 29125:00

one-year-old is it a 10 year old with

## 29125:00 - 29155:00

that specific task that you want it to

## 29155:00 - 29180:00

do and so that's where I think the

## 29180:00 - 29205:00

various models they do have all their

## 29205:00 - 29235:00

strengths and weaknesses it's not

## 29235:00 - 29285:00

something that you can tell any startup

## 29285:00 - 29315:00

or any team this model is right for you

## 29315:00 - 29335:00

you really have to look at those

## 29335:00 - 29375:00

specific examples test it but understand

## 29375:00 - 29430:00

with your data type or your specific use

## 29430:00 - 29460:00

cases that you have in mind what are the

## 29460:00 - 29500:00

bounds of that model and how advanced is

## 29500:00 - 29530:00

it with what you're looking to do and so

## 29530:00 - 29555:00

that's where Kevin is often evaluating

## 29555:00 - 29600:00

the different models you know for us and

## 29600:00 - 29640:00

Reporting back here are the bounds for

## 29640:00 - 29665:00

these different models available today

## 29665:00 - 29700:00

the you know four to five popular models

## 29700:00 - 29725:00

that people are using and here's how

## 29725:00 - 29760:00

well they perform at the various tasks

## 29760:00 - 29790:00

that we have in mind that we would like

## 29790:00 - 29840:00

to roll out and deliver as jobs to be

## 29840:00 - 29880:00

done and use cases for our customers so

## 29880:00 - 29925:00

it's a lot of back and forth with less

## 29925:00 - 29970:00

so on the customer but I think more so

## 29970:00 - 30000:00

internally of thinking about where we

## 30000:00 - 30025:00

want to take the product I understand

## 30025:00 - 30060:00

the limitations the various models and

## 30060:00 - 30100:00

then starting to really dig in and

## 30100:00 - 30145:00

invest more and more internally when we

## 30145:00 - 30190:00

start to see that ask you know opening

## 30190:00 - 30220:00

and closing of a hand or maybe at some

## 30220:00 - 30245:00

point riding a bike we start to see

## 30245:00 - 30275:00

early success where we think hey maybe

## 30275:00 - 30300:00

this is something that's feasible that

## 30300:00 - 30335:00

we should explore further yeah and on

## 30335:00 - 30375:00

that note I think one of the interesting

## 30375:00 - 30410:00

points about that the limitations that

## 30410:00 - 30450:00

we noticed early on is that the

## 30450:00 - 30495:00

trajectory of ml at that point was you

## 30495:00 - 30530:00

know going up into the right at an

## 30530:00 - 30560:00

accelerating Pace I think Ryan mentioned

## 30560:00 - 30600:00

we made a pretty early bets that this

## 30600:00 - 30625:00

would be able to do what we wanted it to

## 30625:00 - 30650:00

do at scale and with minimal human

## 30650:00 - 30685:00

intervention and so you know part of us

## 30685:00 - 30725:00

part of it was relying on or kind of

## 30725:00 - 30750:00

following that Trend and seeing that the

## 30750:00 - 30785:00

trajectory of what is possible with

## 30785:00 - 30825:00

these models could get us there in the

## 30825:00 - 30855:00

future and so you know we really set it

## 30855:00 - 30885:00

up in such a way that we'd be able to

## 30885:00 - 30915:00

take advantage of that I mean we relied

## 30915:00 - 30940:00

on a lot of human intervention in the

## 30940:00 - 30975:00

meantime until we were able to get there

## 30975:00 - 31020:00

but you know we are at the point now

## 31020:00 - 31065:00

where it can do what we wanted to do how

## 31065:00 - 31110:00

did you or how do you set up this sort

## 31110:00 - 31155:00

of testing environment or approach where

## 31155:00 - 31185:00

you can look at a different model and

## 31185:00 - 31220:00

decide if it could be useful for sprig

## 31220:00 - 31285:00

or not yeah now it's a bit different you

## 31285:00 - 31335:00

know I think prior to large llms

## 31335:00 - 31365:00

becoming available you know our testing

## 31365:00 - 31410:00

framework was asking a model maybe a

## 31410:00 - 31440:00

series of specific questions like hey

## 31440:00 - 31475:00

does this response represent somebody

## 31475:00 - 31510:00

talking about pricing yes or no is this

## 31510:00 - 31550:00

person happy or sad things like that you

## 31550:00 - 31590:00

know with the advents of chat

## 31590:00 - 31625:00

completions and how you know even

## 31625:00 - 31655:00

classification tasks are going through

## 31655:00 - 31690:00

chat completions now we've had to sort

## 31690:00 - 31735:00

of shift that to giving an input into an

## 31735:00 - 31785:00

llm Gathering the outputs and then

## 31785:00 - 31825:00

either semi-automatically or manually

## 31825:00 - 31860:00

determining if the output is what we're

## 31860:00 - 31905:00

looking for or not one example of you

## 31905:00 - 31925:00

know something we've been doing is

## 31925:00 - 31965:00

feeding in data from different types of

## 31965:00 - 31990:00

questions being asked you know maybe

## 31990:00 - 32020:00

question one is how is your experience

## 32020:00 - 32055:00

one to five question two is OpenText

## 32055:00 - 32075:00

what else can we do to improve your

## 32075:00 - 32110:00

experience and we've been experimenting

## 32110:00 - 32145:00

with feeding well have been successful

## 32145:00 - 32175:00

with feeding results from both those

## 32175:00 - 32210:00

questions into a model and then asking

## 32210:00 - 32245:00

it to for example create correlations

## 32245:00 - 32280:00

between those questions for example of

## 32280:00 - 32310:00

the people that gave it a four or five

## 32310:00 - 32340:00

star what are some of the interesting

## 32340:00 - 32365:00

themes that we see in their open text

## 32365:00 - 32400:00

response and that's just that's

## 32400:00 - 32435:00

something that's really hard to evaluate

## 32435:00 - 32460:00

in an automated manner at least right

## 32460:00 - 32500:00

now because it's a more complex task

## 32500:00 - 32530:00

because the output is you know

## 32530:00 - 32570:00

non-deterministic and free form if for

## 32570:00 - 32595:00

now it really just does require some

## 32595:00 - 32640:00

manual value evaluation I think that's a

## 32640:00 - 32670:00

perfect example of what I was referring

## 32670:00 - 32720:00

to is that 2019 we wanted to feed an

## 32720:00 - 32760:00

entire survey results in the entire

## 32760:00 - 32795:00

survey into the models that we had at

## 32795:00 - 32820:00

the time and they're not able to come

## 32820:00 - 32845:00

back with those correlations between

## 32845:00 - 32880:00

question one and question two and come

## 32880:00 - 32920:00

back with much more deeper insights

## 32920:00 - 32975:00

across the entire set of survey data and

## 32975:00 - 33015:00

then we started actually continue you

## 33015:00 - 33100:00

know 2019 now 2020 no 2021 no 2022 okay

## 33100:00 - 33155:00

we're now seeing some progress here and

## 33155:00 - 33180:00

so something that we're going to be

## 33180:00 - 33215:00

formally announcing by the end of this

## 33215:00 - 33270:00

month in August is what we call a study

## 33270:00 - 33315:00

level AI where it's actually the llm is

## 33315:00 - 33350:00

able to understand the entire study and

## 33350:00 - 33395:00

draw insights and summarization you can

## 33395:00 - 33445:00

ask questions about the entire studies

## 33445:00 - 33490:00

results and so we're going from which

## 33490:00 - 33520:00

we're still going to have today you know

## 33520:00 - 33555:00

open text analysis on the question level

## 33555:00 - 33615:00

to now moving to the entire survey or

## 33615:00 - 33655:00

what we call a study level and the llm

## 33655:00 - 33695:00

is now making sense of the entire study

## 33695:00 - 33735:00

and then now we're also in the process

## 33735:00 - 33760:00

of evaluating different models for what

## 33760:00 - 33795:00

we call product level Ai and insights

## 33795:00 - 33835:00

and actually the llm is understanding

## 33835:00 - 33855:00

all the surveys they're collecting and

## 33855:00 - 33875:00

all the different correlations and

## 33875:00 - 33920:00

meaning between all those studies and so

## 33920:00 - 33960:00

it's been exciting to kind of ride the

## 33960:00 - 34010:00

advancements as we go while also testing

## 34010:00 - 34040:00

and evaluating where those boundaries

## 34040:00 - 34070:00

are and when we can actually move

## 34070:00 - 34095:00

forward with the value that we're

## 34095:00 - 34125:00

delivering to customers with AI in the

## 34125:00 - 34180:00

case of a a study level analysis or

## 34180:00 - 34215:00

summary what was that process like

## 34215:00 - 34280:00

iterating to figure out if basically the

## 34280:00 - 34325:00

the infrastructure was good enough to

## 34325:00 - 34350:00

provide the type of product experience

## 34350:00 - 34385:00

that you want particularly because I

## 34385:00 - 34405:00

think you have this issue that we talked

## 34405:00 - 34425:00

about all the way at the beginning of

## 34425:00 - 34460:00

the conversation which is there's a lot

## 34460:00 - 34515:00

of subjective Dynamics to things like

## 34515:00 - 34565:00

summaries or insights or those types of

## 34565:00 - 34605:00

things to a large extent we we stick

## 34605:00 - 34630:00

with the fundamentals when it comes to

## 34630:00 - 34655:00

you know any sort of product or feature

## 34655:00 - 34690:00

developments in this case and in

## 34690:00 - 34725:00

actually a lot of the cases now we are

## 34725:00 - 34760:00

doing a couple different things uh the

## 34760:00 - 34785:00

first is you know a really basic data

## 34785:00 - 34835:00

proof of Concepts internally uh where we

## 34835:00 - 34870:00

you know take our inputs run it through

## 34870:00 - 34910:00

the llm get our outputs kind of review

## 34910:00 - 34940:00

it as a team and give our sort of best

## 34940:00 - 34980:00

estimate as to how useful it is how

## 34980:00 - 35015:00

accurate it is and how impactful it is

## 35015:00 - 35035:00

to our end users

## 35035:00 - 35055:00

um and then you know we follow that up

## 35055:00 - 35105:00

with uh very early sort of testing with

## 35105:00 - 35150:00

users our own user research you know

## 35150:00 - 35170:00

either we show it to somebody in a

## 35170:00 - 35205:00

product through an early beta or you

## 35205:00 - 35235:00

know just interview somebody and kind of

## 35235:00 - 35275:00

get their opinion directly it's just uh

## 35275:00 - 35320:00

as much iteration and evaluation as

## 35320:00 - 35365:00

possible and I remember later last year

## 35365:00 - 35390:00

you know about to answer a question we

## 35390:00 - 35410:00

didn't have the infrastructure developed

## 35410:00 - 35435:00

for testing and actually earlier this

## 35435:00 - 35470:00

year I should say uh we didn't have that

## 35470:00 - 35495:00

introduction available we're using chat

## 35495:00 - 35530:00

CPT where you would just take take a

## 35530:00 - 35560:00

piece of data or a data asset and drop

## 35560:00 - 35590:00

it in and see what it could do exactly

## 35590:00 - 35615:00

because it's and you get the plus

## 35615:00 - 35655:00

version so everyone involved had the

## 35655:00 - 35675:00

plus we got everyone the Plus Account

## 35675:00 - 35715:00

the upgraded version to access the gpt4

## 35715:00 - 35765:00

models and we had a specific example

## 35765:00 - 35805:00

that we are running different prompts on

## 35805:00 - 35845:00

to see can it actually do that cross

## 35845:00 - 35880:00

question analysis and had some

## 35880:00 - 35910:00

breakthroughs you know those late nights

## 35910:00 - 35935:00

those weekend breakthroughs when you

## 35935:00 - 35960:00

know you're away from everyone and

## 35960:00 - 35985:00

really kind of hammering on the keyboard

## 35985:00 - 36020:00

and finding out how to get it to do that

## 36020:00 - 36060:00

cross question analysis and most of that

## 36060:00 - 36095:00

work was was oriented around prompt

## 36095:00 - 36115:00

engineering a lot of us prompt

## 36115:00 - 36140:00

engineering yeah can you actually get

## 36140:00 - 36170:00

the model to look at both of the

## 36170:00 - 36215:00

questions at once a lot of the the early

## 36215:00 - 36255:00

testing it was only focused on analysis

## 36255:00 - 36285:00

around here are takeaways and each

## 36285:00 - 36340:00

takeaway was only looking at a specific

## 36340:00 - 36365:00

question at a time it's the first

## 36365:00 - 36385:00

takeaway might be around question three

## 36385:00 - 36415:00

the second ticker might be question two

## 36415:00 - 36445:00

so how can you get the model to actually

## 36445:00 - 36500:00

look at correlations or analysis between

## 36500:00 - 36540:00

you know a specific user who responded

## 36540:00 - 36580:00

to all the questions and actually find

## 36580:00 - 36620:00

correlations between you know their

## 36620:00 - 36655:00

responses and that's really where we had

## 36655:00 - 36680:00

to do the prompt engineering and I think

## 36680:00 - 36710:00

a lot of the value for AI companies now

## 36710:00 - 36740:00

you know is in profit engineering I

## 36740:00 - 36765:00

think the early days was actually just

## 36765:00 - 36790:00

can you build a model can you get the

## 36790:00 - 36810:00

model running can you get the model

## 36810:00 - 36850:00

working in production where I think a

## 36850:00 - 36880:00

lot of it is can you actually work with

## 36880:00 - 36925:00

these models where you don't quite know

## 36925:00 - 36955:00

how they work even people building them

## 36955:00 - 36975:00

you know Google's admitted they don't

## 36975:00 - 37015:00

know how their model actually works but

## 37015:00 - 37040:00

actually to get the output that you're

## 37040:00 - 37070:00

looking for and then the second test is

## 37070:00 - 37095:00

can you get it the output you're looking

## 37095:00 - 37140:00

for in a highly reproducible way or

## 37140:00 - 37180:00

every time you run that Pro prompt

## 37180:00 - 37220:00

you're getting a result that that

## 37220:00 - 37245:00

customer is looking for and the format

## 37245:00 - 37285:00

looking for but also the accuracy you

## 37285:00 - 37305:00

know and so you know not having

## 37305:00 - 37330:00

hallucinations is probably considered

## 37330:00 - 37370:00

accurate right now in the uh the ml

## 37370:00 - 37425:00

field can you talk more Ryan about what

## 37425:00 - 37450:00

your end-to-end product development

## 37450:00 - 37490:00

process looks like now and maybe in what

## 37490:00 - 37515:00

ways would you say would you say it's

## 37515:00 - 37565:00

similar to the pre-llm world and in what

## 37565:00 - 37585:00

ways would you say when you're building

## 37585:00 - 37630:00

a feature today it might look different

## 37630:00 - 37660:00

in some way the uniqueness that we found

## 37660:00 - 37705:00

for product development specific with AI

## 37705:00 - 37755:00

is that you know we Define product Best

## 37755:00 - 37785:00

in Class product development as a

## 37785:00 - 37835:00

product manager and a minimum designer

## 37835:00 - 37875:00

starting from the very beginning of

## 37875:00 - 37940:00

ideation and building a product spec and

## 37940:00 - 37980:00

a design prototype together we'd love to

## 37980:00 - 38025:00

have Engineers involved sometimes due to

## 38025:00 - 38055:00

you know time constraints and other

## 38055:00 - 38090:00

goals I'm not always able to join I

## 38090:00 - 38125:00

think the unique part with AI is that

## 38125:00 - 38200:00

you have to have an AI engineer involved

## 38200:00 - 38235:00

from day one because there's a question

## 38235:00 - 38260:00

of the feasibility of what you're

## 38260:00 - 38285:00

looking to build and I think that's the

## 38285:00 - 38320:00

big difference is that a best-in-class

## 38320:00 - 38350:00

product development process has an

## 38350:00 - 38385:00

engineer involved from day one but with

## 38385:00 - 38410:00

AI it's actually going to be a

## 38410:00 - 38440:00

requirement because there's been a lot

## 38440:00 - 38475:00

of times where maybe our product

## 38475:00 - 38490:00

management you know someone on our

## 38490:00 - 38525:00

product management team and design team

## 38525:00 - 38545:00

come up with something that I want to do

## 38545:00 - 38570:00

with AI and then they go to Kevin and

## 38570:00 - 38600:00

they might spend you know a month

## 38600:00 - 38635:00

working on something and we quickly find

## 38635:00 - 38670:00

out it's not something that is feasible

## 38670:00 - 38730:00

and so we see more of a you know

## 38730:00 - 38795:00

iterative process of testing and with

## 38795:00 - 38830:00

here's an idea that we want to try is

## 38830:00 - 38875:00

this something that is possible with the

## 38875:00 - 38900:00

current model that working with or maybe

## 38900:00 - 38930:00

a different model and then once we start

## 38930:00 - 38960:00

to get the green light that hey there is

## 38960:00 - 38990:00

some you know there's something here we

## 38990:00 - 39010:00

think we might be able to make this work

## 39010:00 - 39050:00

that's where the you know product

## 39050:00 - 39095:00

manager designer Kevin along with

## 39095:00 - 39135:00

typically another engineer will then

## 39135:00 - 39185:00

start to in lockstep build out that

## 39185:00 - 39225:00

entire feature together and so that's

## 39225:00 - 39245:00

the example that we're referring to

## 39245:00 - 39280:00

earlier around the study level insights

## 39280:00 - 39305:00

is that there was a lot of that early

## 39305:00 - 39350:00

exploration you know chat GPT some

## 39350:00 - 39390:00

internal open AI model infrastructure

## 39390:00 - 39430:00

that we developed with retool where we

## 39430:00 - 39460:00

can enter in our own commands and a

## 39460:00 - 39495:00

retool and get back output you know from

## 39495:00 - 39535:00

open AI that's that's how we do a lot of

## 39535:00 - 39575:00

the testing today but it does require

## 39575:00 - 39615:00

everyone to be involved in that testing

## 39615:00 - 39650:00

process to see you know and a lot of

## 39650:00 - 39700:00

times the AI has actually taken us in

## 39700:00 - 39745:00

different uh directions maybe it's

## 39745:00 - 39770:00

working better than we expected on

## 39770:00 - 39795:00

something in other cases it's working

## 39795:00 - 39845:00

lesser than we had hoped and so we might

## 39845:00 - 39880:00

actually simplify or work within the

## 39880:00 - 39905:00

constraints that we're given kind of

## 39905:00 - 39930:00

maybe continuing to go down a little bit

## 39930:00 - 39975:00

of this path of product development and

## 39975:00 - 40010:00

prioritization kind of in this world of

## 40010:00 - 40070:00

large language models how has the hype

## 40070:00 - 40125:00

and Euphoria in the market change the

## 40125:00 - 40150:00

way that you think about any of these

## 40150:00 - 40180:00

prioritization decisions yeah I think

## 40180:00 - 40215:00

we've noticed a couple things

## 40215:00 - 40250:00

um like you mentioned there's the

## 40250:00 - 40295:00

obvious uh sort of external pressure I

## 40295:00 - 40325:00

think with the Advent of some of these

## 40325:00 - 40355:00

models being released the bar has been

## 40355:00 - 40385:00

lowered quite a bit although some of

## 40385:00 - 40405:00

these analyzes are things you want to do

## 40405:00 - 40450:00

are you know more achievable and so at

## 40450:00 - 40475:00

least I think from our point of view

## 40475:00 - 40520:00

that's kind of prompted us to honestly

## 40520:00 - 40560:00

to work faster and to build build better

## 40560:00 - 40600:00

and faster on the flip side I think it's

## 40600:00 - 40655:00

allowed us to build more than before

## 40655:00 - 40690:00

um you know as one quick example I spent

## 40690:00 - 40725:00

you know several years tuning that that

## 40725:00 - 40760:00

very first sort of feature we built a

## 40760:00 - 40790:00

lot of effort spent on that not much

## 40790:00 - 40825:00

effort spent elsewhere because we really

## 40825:00 - 40850:00

wanted to focus and make sure that was

## 40850:00 - 40875:00

you know where we were spending our

## 40875:00 - 40905:00

effort but now that the floodgates are

## 40905:00 - 40930:00

open we can work on a lot more stuff

## 40930:00 - 40975:00

that expands our ability to to produce

## 40975:00 - 41010:00

I'll say yeah we've we've had so many

## 41010:00 - 41055:00

you know all of that testing and hitting

## 41055:00 - 41090:00

the walls of what's possible you know in

## 41090:00 - 41120:00

the early years we now have the ability

## 41120:00 - 41155:00

to actually the models are now mature

## 41155:00 - 41180:00

enough to actually deliver on a lot of

## 41180:00 - 41210:00

those ideas I think that's been it's

## 41210:00 - 41245:00

been really exciting for us is less on

## 41245:00 - 41280:00

the competitive set and now that they're

## 41280:00 - 41320:00

now incorporating AI I think it's more

## 41320:00 - 41380:00

so that the things like study level AI

## 41380:00 - 41430:00

or product level AI have now been

## 41430:00 - 41470:00

unlocked where before they were not

## 41470:00 - 41515:00

possible and at sprig we see our value

## 41515:00 - 41555:00

for customers as delivering specific

## 41555:00 - 41585:00

recommendations to improve their product

## 41585:00 - 41615:00

experiences and so so much of the early

## 41615:00 - 41645:00

years the r d went into the collection

## 41645:00 - 41675:00

of the data at Large Scale you know

## 41675:00 - 41705:00

we've had kept the AI efforts quite lean

## 41705:00 - 41745:00

just because of the possibilities where

## 41745:00 - 41780:00

you know candidly quite limited and

## 41780:00 - 41815:00

bounded by a single use case of text

## 41815:00 - 41855:00

analysis on a question level but our

## 41855:00 - 41895:00

customers ultimately want us to tell

## 41895:00 - 41935:00

them how to improve their product

## 41935:00 - 41975:00

experience and ultimately can we

## 41975:00 - 42010:00

actually push their product experience

## 42010:00 - 42045:00

forward with them and so I think that's

## 42045:00 - 42085:00

exciting part with AI and where we see

## 42085:00 - 42120:00

it going here at sprig is that we can

## 42120:00 - 42160:00

move Beyond helping them you know

## 42160:00 - 42205:00

summarize question level analysis to now

## 42205:00 - 42240:00

saying here's our actually all the

## 42240:00 - 42265:00

challenges and customer issues we found

## 42265:00 - 42305:00

across the entire survey to now saying

## 42305:00 - 42330:00

here are all the issues with your

## 42330:00 - 42365:00

product experience across your entire

## 42365:00 - 42405:00

product to now saying can we actually

## 42405:00 - 42450:00

tell our customers here's the issue but

## 42450:00 - 42480:00

here's actually the recommendation to

## 42480:00 - 42515:00

fix the issue and can we actually part

## 42515:00 - 42555:00

with other vendors in the space to say

## 42555:00 - 42600:00

we're actually going to implement that

## 42600:00 - 42645:00

fix for you with your permission and so

## 42645:00 - 42690:00

I think the level of what's possible has

## 42690:00 - 42750:00

significantly increased and evolved over

## 42750:00 - 42780:00

the past nine months our customers

## 42780:00 - 42815:00

expect significantly more value

## 42815:00 - 42855:00

delivered with all the recent

## 42855:00 - 42890:00

advancements in Ai and so I think for us

## 42890:00 - 42940:00

it's just unlocking is huge uh level of

## 42940:00 - 42975:00

advancements that we're now quickly

## 42975:00 - 43040:00

shipping this year by far more AI

## 43040:00 - 43080:00

announcements and AI features and AI you

## 43080:00 - 43125:00

know advancements then the company in

## 43125:00 - 43150:00

all the previous years combined and so I

## 43150:00 - 43170:00

think it's just more of that external

## 43170:00 - 43210:00

exam external energy shifting to an AI

## 43210:00 - 43255:00

first company where everyone at sprig

## 43255:00 - 43285:00

every engineer knows how to incorporate

## 43285:00 - 43315:00

AI into their products product managers

## 43315:00 - 43345:00

know how to use and build with AI

## 43345:00 - 43375:00

designers know how to build and design

## 43375:00 - 43405:00

with AI and shifting to an AI first

## 43405:00 - 43450:00

company is really the main unlock for us

## 43450:00 - 43490:00

as an organization is shifting from a

## 43490:00 - 43525:00

company that has an extremely powerful

## 43525:00 - 43570:00

AI feature to be in a company that has

## 43570:00 - 43605:00

AI incorporated into everything that it

## 43605:00 - 43625:00

does and how it delivers value to

## 43625:00 - 43655:00

customers I think that's a good way of

## 43655:00 - 43690:00

putting it you know not only has it

## 43690:00 - 43720:00

accelerated our way towards our

## 43720:00 - 43750:00

long-term Vision but it's increased the

## 43750:00 - 43780:00

scope of that long-term Vision pretty

## 43780:00 - 43810:00

significantly what else can you share

## 43810:00 - 43850:00

about what you're hearing from customers

## 43850:00 - 43905:00

as this kind of tidal wave has sort of

## 43905:00 - 43950:00

been built up do you see sort of a level

## 43950:00 - 43995:00

of enthusiasm and excitement in the

## 43995:00 - 44035:00

abstract that just feels very different

## 44035:00 - 44070:00

than conversations you are having call

## 44070:00 - 44125:00

it 12 months ago and are there sort of

## 44125:00 - 44165:00

strategy Implement implications of that

## 44165:00 - 44210:00

in any way I think we're seeing a level

## 44210:00 - 44270:00

of excitement from customers but also

## 44270:00 - 44330:00

they have to be okay delegating some of

## 44330:00 - 44365:00

the control they previously had it's

## 44365:00 - 44395:00

that balance between man

## 44395:00 - 44430:00

or woman and machine

## 44430:00 - 44500:00

and human in machine and with the new

## 44500:00 - 44535:00

study level AI that we're shipping right

## 44535:00 - 44600:00

now it summarizes the entire study you

## 44600:00 - 44630:00

know with a summarized output and you

## 44630:00 - 44660:00

can ask it questions how should I

## 44660:00 - 44690:00

improve my product experience and I

## 44690:00 - 44720:00

think a lot of people are starting to

## 44720:00 - 44745:00

realize that they need to be comfortable

## 44745:00 - 44790:00

actually delegating something that they

## 44790:00 - 44825:00

previously felt like was a decision that

## 44825:00 - 44865:00

they had to make and be comfortable with

## 44865:00 - 44900:00

moving higher up in the order of

## 44900:00 - 44955:00

decision making and see AI as a true

## 44955:00 - 44980:00

co-pilot where I think a lot of people

## 44980:00 - 45020:00

still are trying to retain that control

## 45020:00 - 45055:00

of all the decisions or do all the

## 45055:00 - 45085:00

analysis or we may make their own

## 45085:00 - 45105:00

decisions around what they want to do

## 45105:00 - 45135:00

you know with this data and how can we

## 45135:00 - 45180:00

actually move you know our the users

## 45180:00 - 45215:00

using sprig and I think the broader

## 45215:00 - 45280:00

individual working with AI to focus on

## 45280:00 - 45320:00

higher level orders of work and I think

## 45320:00 - 45360:00

ultimately is like a species you know

## 45360:00 - 45390:00

we're now so much further along if we

## 45390:00 - 45430:00

can trust and actually find ways to work

## 45430:00 - 45470:00

with AI that allow us to leverage our

## 45470:00 - 45490:00

time more effectively and so I think

## 45490:00 - 45515:00

that balance we're seeing a lot of

## 45515:00 - 45545:00

people kind of uncomfortable with that

## 45545:00 - 45580:00

balance and seeing about how they fit in

## 45580:00 - 45620:00

and work with you know AI together kind

## 45620:00 - 45640:00

of one of the things that just came to

## 45640:00 - 45675:00

mind there is that there's this sort of

## 45675:00 - 45720:00

famous Betty Crocker story where the

## 45720:00 - 45755:00

original Betty Crocker product had the

## 45755:00 - 45795:00

eggs mixed in eggs and milk or whatever

## 45795:00 - 45830:00

it is and it didn't sell very well but

## 45830:00 - 45870:00

when they just sold the mix without it

## 45870:00 - 45895:00

and required a little bit of effort and

## 45895:00 - 45935:00

mixing it sort of took off does that

## 45935:00 - 45965:00

apply to any ways that you're thinking

## 45965:00 - 46010:00

about these AI enabled features where

## 46010:00 - 46040:00

you you kind of need the End customer to

## 46040:00 - 46060:00

feel like they're at least doing a

## 46060:00 - 46085:00

little bit of you know dropping the eggs

## 46085:00 - 46130:00

in and mixing it up so they've done some

## 46130:00 - 46160:00

level of work where they feel like

## 46160:00 - 46205:00

there's some um amount of ownership when

## 46205:00 - 46245:00

they're delivering it or or sort of some

## 46245:00 - 46275:00

amount of involvement versus just spit

## 46275:00 - 46310:00

the thing out and and job is done do you

## 46310:00 - 46345:00

think about building these products in

## 46345:00 - 46375:00

that way I will say that it's something

## 46375:00 - 46410:00

that we don't intentionally do but I

## 46410:00 - 46435:00

think based on the customer feedback and

## 46435:00 - 46460:00

working with customers to develop these

## 46460:00 - 46500:00

features that's how we have landed and a

## 46500:00 - 46530:00

lot of them you know I think a recent

## 46530:00 - 46580:00

example for study level AI we recommend

## 46580:00 - 46615:00

which questions to ask and they click a

## 46615:00 - 46650:00

button on the question that they want to

## 46650:00 - 46695:00

ask and so giving them I won't say the

## 46695:00 - 46730:00

perception but they still have that

## 46730:00 - 46780:00

involvement they're still in the cockpit

## 46780:00 - 46845:00

of you know their own work is critical

## 46845:00 - 46890:00

and it's not something that they feel

## 46890:00 - 46935:00

like any parts of their work is being

## 46935:00 - 46980:00

replaced by Ai and I think that's where

## 46980:00 - 47020:00

you have to find the right balance into

## 47020:00 - 47065:00

your example you know in your own

## 47065:00 - 47110:00

product and working with AI what is the

## 47110:00 - 47155:00

eggs what's the piece that the user is

## 47155:00 - 47175:00

going to bring to the table where they

## 47175:00 - 47220:00

still have that sense of control and

## 47220:00 - 47275:00

authority and purpose and being but the

## 47275:00 - 47315:00

AI is helping them succeed so much more

## 47315:00 - 47355:00

on their role we certainly see as well I

## 47355:00 - 47400:00

think our position is involved about how

## 47400:00 - 47450:00

we let we talk about the OpenText AI I

## 47450:00 - 47485:00

remember at first the very early days of

## 47485:00 - 47505:00

spring there was some wording around

## 47505:00 - 47555:00

your automated user researcher you know

## 47555:00 - 47600:00

or it does all the text analysis for you

## 47600:00 - 47625:00

and that was actually very off-putting

## 47625:00 - 47650:00

for both user researchers and product

## 47650:00 - 47690:00

teams and so today a lot of the wording

## 47690:00 - 47740:00

around OpenText AI specifically around

## 47740:00 - 47790:00

the question level was that the AI will

## 47790:00 - 47835:00

do the heavy lifting for you and let you

## 47835:00 - 47880:00

review the results and then you can

## 47880:00 - 47915:00

deliver and so we've noticed in the

## 47915:00 - 47940:00

sales calls as well people actually feel

## 47940:00 - 47975:00

better if we tell them that it's not

## 47975:00 - 48015:00

meant to do the entire work it's not

## 48015:00 - 48045:00

supposed to give you the answer it's

## 48045:00 - 48070:00

actually supposed to give you everything

## 48070:00 - 48120:00

until right before the answer and when

## 48120:00 - 48150:00

you look at chat CPT I think partly why

## 48150:00 - 48195:00

it's been successful is that it's such a

## 48195:00 - 48230:00

standalone product that's not integrated

## 48230:00 - 48265:00

into anything else and I think if it

## 48265:00 - 48300:00

actually was integrated into your slack

## 48300:00 - 48360:00

or into your email or into your work I

## 48360:00 - 48380:00

think people might feel like they're

## 48380:00 - 48415:00

losing control because all of a sudden

## 48415:00 - 48450:00

it's in that application with them if

## 48450:00 - 48475:00

you have this kind of dark you know

## 48475:00 - 48505:00

corner of the web to go to that gives

## 48505:00 - 48535:00

you a result that you tweak and modify

## 48535:00 - 48570:00

and then you put forward as if it's your

## 48570:00 - 48595:00

own you actually feel really good about

## 48595:00 - 48630:00

that because you got that done you know

## 48630:00 - 48665:00

faster and also potentially higher

## 48665:00 - 48700:00

quality work and so I think for the AI

## 48700:00 - 48725:00

work that we've been developing it's

## 48725:00 - 48750:00

helping customers get to where they want

## 48750:00 - 48785:00

to go but maybe not getting all the way

## 48785:00 - 48825:00

there when you started to see some of

## 48825:00 - 48850:00

the early breakthroughs in large

## 48850:00 - 48890:00

language models was there a period of

## 48890:00 - 48915:00

time that you were worried that it could

## 48915:00 - 48945:00

be a disruptive innovation for the

## 48945:00 - 48985:00

company that in some ways the core of

## 48985:00 - 49025:00

what made the company special was this

## 49025:00 - 49080:00

really hard work that you did in these

## 49080:00 - 49115:00

ml features and now it made it much

## 49115:00 - 49140:00

easier for anybody else to do these

## 49140:00 - 49175:00

types of things and did that inform your

## 49175:00 - 49205:00

strategy in any way it was certainly

## 49205:00 - 49240:00

certainly expected it was a matter of

## 49240:00 - 49290:00

when and not if knowing that AI at some

## 49290:00 - 49335:00

point would allow the barrier to build

## 49335:00 - 49365:00

the technology to be lower and lower

## 49365:00 - 49395:00

over time I think the key question that

## 49395:00 - 49430:00

we just want to make sure we focus on is

## 49430:00 - 49480:00

we're always ahead of the competition in

## 49480:00 - 49520:00

the field of AI and I think that's the

## 49520:00 - 49555:00

dimension that we take a hard look at

## 49555:00 - 49590:00

and you know we are seeing other company

## 49590:00 - 49640:00

knees in our space add for example a

## 49640:00 - 49690:00

survey or study level summarization but

## 49690:00 - 49730:00

while they're launching summarization of

## 49730:00 - 49760:00

an entire survey we're adding the

## 49760:00 - 49805:00

ability to ask custom questions you know

## 49805:00 - 49835:00

summarization and ask custom questions

## 49835:00 - 49870:00

and as they're starting to think about

## 49870:00 - 49905:00

you know maybe whatever is next for them

## 49905:00 - 49930:00

we're moving on to you know product

## 49930:00 - 49965:00

level insights and something that some

## 49965:00 - 49990:00

investors pushed back on in the early

## 49990:00 - 50025:00

days so at some point this will not be a

## 50025:00 - 50060:00

competitive image for you but for us we

## 50060:00 - 50095:00

will always make sure that we are the

## 50095:00 - 50140:00

most Innovative company in the space and

## 50140:00 - 50170:00

we just lined at a really large contract

## 50170:00 - 50220:00

with a very high profile company that

## 50220:00 - 50240:00

you know everyone listening this podcast

## 50240:00 - 50295:00

has used at some point and they purchase

## 50295:00 - 50330:00

sprig because of the AI Vision they saw

## 50330:00 - 50360:00

for what we're going to be working on

## 50360:00 - 50395:00

and so we just announced our vision as

## 50395:00 - 50430:00

well last month and what we want to do

## 50430:00 - 50470:00

with AI and so as long as we continue to

## 50470:00 - 50500:00

push the boundaries and that's why I

## 50500:00 - 50535:00

talked about slope in having someone on

## 50535:00 - 50585:00

your team who is thinking about Ai and

## 50585:00 - 50630:00

ml is that you know for whatever we

## 50630:00 - 50675:00

tackle next I know that Kevin will help

## 50675:00 - 50715:00

us figure out whatever that is and I

## 50715:00 - 50735:00

also know that it's something that we've

## 50735:00 - 50770:00

never done before at sprig and it's

## 50770:00 - 50815:00

never been done before potentially in

## 50815:00 - 50860:00

the broader field of technology and so

## 50860:00 - 50895:00

as long as we can solve those Green

## 50895:00 - 50930:00

Field problems you know with AI continue

## 50930:00 - 50960:00

to deliver customer value that's

## 50960:00 - 50995:00

ultimately the the race that we're

## 50995:00 - 51035:00

focused on in winning maybe Ryan on that

## 51035:00 - 51065:00

point it's an interesting chance to talk

## 51065:00 - 51095:00

a little bit about what sales

## 51095:00 - 51140:00

conversations looked like today do you

## 51140:00 - 51180:00

spend more time trying to explain to

## 51180:00 - 51220:00

customers what your world view is and

## 51220:00 - 51250:00

where we are and where we're going in AI

## 51250:00 - 51280:00

or does it tend to be much more

## 51280:00 - 51325:00

problem-centric and solution-centric it

## 51325:00 - 51360:00

is absolutely far more Vision selling

## 51360:00 - 51390:00

than I would have expected and a lot of

## 51390:00 - 51425:00

times we talk to customers they ask we

## 51425:00 - 51455:00

ask them what do you want us to build Ai

## 51455:00 - 51500:00

and I it's you know very common faster

## 51500:00 - 51540:00

horse you know type of response or it's

## 51540:00 - 51570:00

I don't know what I want because I don't

## 51570:00 - 51585:00

know what's possible and I don't even

## 51585:00 - 51615:00

know know what you could do with these

## 51615:00 - 51655:00

models and so going back to the product

## 51655:00 - 51685:00

development process where you have to

## 51685:00 - 51715:00

really rely on what many would believe

## 51715:00 - 51745:00

is a best-in-class product development

## 51745:00 - 51780:00

process with an AI engineer a product

## 51780:00 - 51815:00

designer product manager all working in

## 51815:00 - 51840:00

lockstep from day one you know I think

## 51840:00 - 51885:00

with working with customers with AI you

## 51885:00 - 51910:00

also have to develop world-class

## 51910:00 - 51950:00

techniques of not asking a customer what

## 51950:00 - 51985:00

to build but instead giving them a set

## 51985:00 - 52025:00

of options to provide feedback on and so

## 52025:00 - 52050:00

a lot of the work that we do with AI is

## 52050:00 - 52090:00

we have five different features that we

## 52090:00 - 52145:00

could build with AI you know ABCDE gave

## 52145:00 - 52175:00

us your feedback and responses to each

## 52175:00 - 52220:00

one sometimes we'll ask what he wants to

## 52220:00 - 52260:00

build and you know they'll say uh you

## 52260:00 - 52285:00

know again we don't know we'll show them

## 52285:00 - 52320:00

what's possible they'll give us that

## 52320:00 - 52375:00

feedback but we always hear if it works

## 52375:00 - 52410:00

or if it works as you say so there's

## 52410:00 - 52445:00

always that caveat and that skepticism

## 52445:00 - 52490:00

that we hear around what we can do and

## 52490:00 - 52530:00

but on the sales front it's absolutely

## 52530:00 - 52585:00

around the taking what we hear is

## 52585:00 - 52615:00

presenting those options those five

## 52615:00 - 52655:00

options or ten options hearing which

## 52655:00 - 52680:00

ones are really resonating with

## 52680:00 - 52705:00

customers and then going on the sales

## 52705:00 - 52755:00

side and saying this is our AI vision

## 52755:00 - 52790:00

for what we want to do with AI and that

## 52790:00 - 52815:00

we've already validated that by

## 52815:00 - 52835:00

presenting those options and getting

## 52835:00 - 52860:00

that feedback and seeing what resonates

## 52860:00 - 52890:00

and then projecting that for the sales

## 52890:00 - 52925:00

side getting those customers to buying

## 52925:00 - 52955:00

it this is what I should be looking for

## 52955:00 - 53005:00

in a solution with AI when you're

## 53005:00 - 53030:00

getting that customer feedback and

## 53030:00 - 53060:00

you're kind of teeing up five to ten

## 53060:00 - 53115:00

specific product ideas or or potential

## 53115:00 - 53155:00

AI features are you giving them points

## 53155:00 - 53190:00

to like assign importance is it

## 53190:00 - 53225:00

qualitative is it quantitative how are

## 53225:00 - 53250:00

you getting them to rank those

## 53250:00 - 53290:00

combination of both I think

## 53290:00 - 53310:00

um yeah we have a couple different

## 53310:00 - 53340:00

feedback mechanisms like I mentioned

## 53340:00 - 53380:00

in-person interviewing you know getting

## 53380:00 - 53425:00

async information we use our own product

## 53425:00 - 53465:00

to get async feedback you know we ask

## 53465:00 - 53490:00

people one to five how useful was this

## 53490:00 - 53530:00

you know open text what can we do to

## 53530:00 - 53555:00

improve this pretty much anything we can

## 53555:00 - 53590:00

get our hands on and Ryan on the on the

## 53590:00 - 53620:00

sales side how does that kind of vision

## 53620:00 - 53675:00

setting fit into your sales process we

## 53675:00 - 53720:00

have a specific you know AI Vision deck

## 53720:00 - 53765:00

and then if you go to sprig.com AI you

## 53765:00 - 53790:00

know we've publicly shared our vision

## 53790:00 - 53830:00

for AI and so I think it's just going

## 53830:00 - 53850:00

back to validating that with the current

## 53850:00 - 53890:00

customers and then in the sales side

## 53890:00 - 53925:00

really seeing you know what is standing

## 53925:00 - 53960:00

out and asking you know what parts of

## 53960:00 - 53990:00

this are most interesting and applicable

## 53990:00 - 54020:00

to the company that you know you're at

## 54020:00 - 54070:00

and and hearing that feedback but we're

## 54070:00 - 54095:00

seeing a lot of companies very similar

## 54095:00 - 54130:00

to digital transformation there's an AI

## 54130:00 - 54165:00

transformation that's happening a lot of

## 54165:00 - 54205:00

them are saying we have been tasked with

## 54205:00 - 54245:00

finding and applying AI to the work that

## 54245:00 - 54280:00

we do this is an okr this is a company

## 54280:00 - 54340:00

mandate you know from the CEO and taking

## 54340:00 - 54380:00

what we're saying to them and pitching

## 54380:00 - 54420:00

internally and saying this is how we

## 54420:00 - 54480:00

want to apply AI for our role for how we

## 54480:00 - 54520:00

develop products here at our company and

## 54520:00 - 54535:00

so that's why there's a lot of sales

## 54535:00 - 54565:00

enablement of telling them this is how

## 54565:00 - 54600:00

AI should be transforming how you

## 54600:00 - 54630:00

develop products and really setting that

## 54630:00 - 54675:00

narrative for them to take with them

## 54675:00 - 54710:00

Switching gears slightly you both

## 54710:00 - 54740:00

mention this a little bit but can you

## 54740:00 - 54795:00

share more about the org structure has

## 54795:00 - 54825:00

changed and maybe product teams have

## 54825:00 - 54865:00

changed if it's been significant over

## 54865:00 - 54890:00

the past year

## 54890:00 - 54950:00

um I could start with uh specifically Ai

## 54950:00 - 54975:00

and how we've how we developed it at the

## 54975:00 - 55010:00

company I think recently the past six

## 55010:00 - 55060:00

months we've modeled our what we call

## 55060:00 - 55105:00

our AI Squad based on some successful

## 55105:00 - 55135:00

examples we've seen in Industry kind of

## 55135:00 - 55165:00

like the vertically integrated approach

## 55165:00 - 55195:00

I think where I mentioned this but a

## 55195:00 - 55220:00

dedicated designer dedicated product

## 55220:00 - 55260:00

manager dedicated Engineers that are

## 55260:00 - 55295:00

responsible for full end-to-end delivery

## 55295:00 - 55340:00

of you know AI related features I think

## 55340:00 - 55370:00

this is in contrast to some other

## 55370:00 - 55400:00

examples and I think something we've

## 55400:00 - 55430:00

tried before where you know maybe you

## 55430:00 - 55485:00

have a dedicated ml team or AI team ml

## 55485:00 - 55515:00

scientists ml Engineers research

## 55515:00 - 55555:00

Engineers who will you know sort of

## 55555:00 - 55605:00

receive tasks and return the results you

## 55605:00 - 55625:00

know maybe have a separate product team

## 55625:00 - 55685:00

that needs AI some some AI feature in

## 55685:00 - 55710:00

what they're building they'll kind of

## 55710:00 - 55735:00

contract it out in a sense to this

## 55735:00 - 55775:00

separate team you know I've read a lot

## 55775:00 - 55810:00

about companies that have kind of taken

## 55810:00 - 55850:00

that approach and from the times we've

## 55850:00 - 55895:00

tried it not as much success uh I think

## 55895:00 - 55915:00

mostly because there's an alignment

## 55915:00 - 55945:00

issue sometimes

## 55945:00 - 55965:00

um it's just kind of harder to get that

## 55965:00 - 56005:00

end-to-end release of a quality feature

## 56005:00 - 56030:00

and so like I mentioned yeah we've had a

## 56030:00 - 56055:00

lot of success with this fully

## 56055:00 - 56090:00

vertically integrated approach and we've

## 56090:00 - 56115:00

certainly seen those challenges as well

## 56115:00 - 56155:00

where a lot of the models today require

## 56155:00 - 56195:00

they have engineering challenges as well

## 56195:00 - 56230:00

as data science challenges and so having

## 56230:00 - 56275:00

AI Engineers embedded with traditional

## 56275:00 - 56305:00

Engineers has been the big breakthrough

## 56305:00 - 56345:00

for us and working together to develop

## 56345:00 - 56375:00

and build these features and not seeing

## 56375:00 - 56420:00

AI as like Kevin said an input output

## 56420:00 - 56455:00

you know the model spits out a response

## 56455:00 - 56490:00

that the engineer then integrates we're

## 56490:00 - 56530:00

seeing it truly does need to be the AI

## 56530:00 - 56580:00

data scientists embedded into a broader

## 56580:00 - 56605:00

Squad and a part of that Squad

## 56605:00 - 56640:00

delivering on and building a feature

## 56640:00 - 56670:00

together and in the case of AI engine

## 56670:00 - 56705:00

engineers in the context of your company

## 56705:00 - 56755:00

is the profile and background relatively

## 56755:00 - 56805:00

same similar excuse me to the same type

## 56805:00 - 56840:00

of AI or ml engineer you would have

## 56840:00 - 56885:00

hired in 2020 or is the spec change for

## 56885:00 - 56930:00

the person a lot of similarities to who

## 56930:00 - 56980:00

I would have hired in 2020 like I

## 56980:00 - 57000:00

mentioned before a lot of the

## 57000:00 - 57035:00

fundamentals remain the same we need a

## 57035:00 - 57075:00

lot of the same skill sets I think given

## 57075:00 - 57130:00

our current switch to hosted llms and

## 57130:00 - 57175:00

away from you know taking Google's birds

## 57175:00 - 57205:00

and fine-tuning it ourselves more

## 57205:00 - 57240:00

towards I guess we call like a full

## 57240:00 - 57280:00

stack ml engineer somebody who's able to

## 57280:00 - 57320:00

you know help integrate this and

## 57320:00 - 57345:00

actually Implement parts of this and in

## 57345:00 - 57375:00

your back end I think we would switch

## 57375:00 - 57415:00

more towards towards that yeah so more

## 57415:00 - 57470:00

of that hybrid how about how you share

## 57470:00 - 57535:00

knowledge and sort of upskill existing

## 57535:00 - 57575:00

product and Engineering folks in your

## 57575:00 - 57605:00

org do you have rituals or things that

## 57605:00 - 57635:00

you found to be impactful other than

## 57635:00 - 57665:00

this important idea of these kind of

## 57665:00 - 57700:00

cross functional pods where you have

## 57700:00 - 57750:00

Specialists on the team well I know one

## 57750:00 - 57790:00

change that Ryan Mastermind did pretty

## 57790:00 - 57815:00

recently actually not recently a few

## 57815:00 - 57850:00

months ago several months ago was giving

## 57850:00 - 57875:00

everybody at the company who wanted it

## 57875:00 - 57920:00

access to you know chat GPT especially

## 57920:00 - 57950:00

people on the AI Squad other Engineers

## 57950:00 - 58005:00

uh with the sort of overall directive to

## 58005:00 - 58045:00

you know try this out uh see how you can

## 58045:00 - 58085:00

use it in your everyday job and as

## 58085:00 - 58120:00

people used it and have been using it I

## 58120:00 - 58140:00

think everyone's sort of getting ideas

## 58140:00 - 58175:00

of how you know we can use it in our own

## 58175:00 - 58220:00

products and with some of our features

## 58220:00 - 58260:00

and you know I've gotten prompt

## 58260:00 - 58295:00

engineering ideas from folks around the

## 58295:00 - 58330:00

company uh from every pretty much every

## 58330:00 - 58355:00

single Department things I wouldn't have

## 58355:00 - 58380:00

thought of before because you know

## 58380:00 - 58405:00

people have different points of view and

## 58405:00 - 58440:00

that's actually been immensely helpful

## 58440:00 - 58485:00

so yeah that's one great example of uh I

## 58485:00 - 58515:00

guess that that proliferation of this

## 58515:00 - 58545:00

this tooling and that requirement yeah

## 58545:00 - 58590:00

we did a at our All Hands Kevin actually

## 58590:00 - 58625:00

led a training on how to use chat CPT

## 58625:00 - 58645:00

and you'd be surprised a lot of people

## 58645:00 - 58670:00

actually have not used it yet and so I

## 58670:00 - 58700:00

think think you know a lot of us if

## 58700:00 - 58725:00

you're on Twitter you're getting the

## 58725:00 - 58760:00

weekly updates on what's Happening AI

## 58760:00 - 58800:00

you've used you know chat GPT you've

## 58800:00 - 58825:00

tried Bard you've tried all the models

## 58825:00 - 58865:00

but I think for a lot of individuals

## 58865:00 - 58910:00

they're still learning how to use these

## 58910:00 - 58945:00

models they are so open-ended today and

## 58945:00 - 58980:00

so Kevin ran through various examples

## 58980:00 - 59020:00

you know interview questions to ask in

## 59020:00 - 59050:00

an interview for someone that you're

## 59050:00 - 59090:00

interviewing uh for a sales team

## 59090:00 - 59125:00

understanding sales contracts and I

## 59125:00 - 59160:00

think the more pervasive AI becomes

## 59160:00 - 59190:00

within a company the more that people

## 59190:00 - 59225:00

realize Kevin's Point how it could be

## 59225:00 - 59270:00

utilized you know in the development of

## 59270:00 - 59305:00

a company's own product another one has

## 59305:00 - 59355:00

been GitHub co-pilot is that we pretty

## 59355:00 - 59380:00

much required all the engineers to use

## 59380:00 - 59410:00

GitHub copilot and so we're constantly

## 59410:00 - 59440:00

thinking about what are all the ways all

## 59440:00 - 59470:00

where all the vendors that we can

## 59470:00 - 59520:00

utilize intercom with Finn you've been

## 59520:00 - 59550:00

trying out fin with our own customers

## 59550:00 - 59575:00

for our customers answering customer

## 59575:00 - 59610:00

support tickets and all of a sudden I

## 59610:00 - 59635:00

guess everyone that AI hat they can put

## 59635:00 - 59680:00

on and think about internally Kevin also

## 59680:00 - 59725:00

ran a brown bag for our engineering team

## 59725:00 - 59755:00

for one hour and really got everyone up

## 59755:00 - 59835:00

to speed on how to use the open Ai apis

## 59835:00 - 59875:00

and how to integrate AI into the

## 59875:00 - 59900:00

features of the developing because we

## 59900:00 - 59935:00

have an AI Squad now but the next step

## 59935:00 - 59985:00

for us is actually having every engineer

## 59985:00 - 60030:00

know how to incorporate Ai and every

## 60030:00 - 60060:00

product manager and every you know

## 60060:00 - 60100:00

everyone on pde should know and have

## 60100:00 - 60140:00

built AI into one of their features by

## 60140:00 - 60175:00

the end of the year and so to get there

## 60175:00 - 60205:00

getting people comfortable and

## 60205:00 - 60235:00

understanding you know AI may be in

## 60235:00 - 60260:00

existing vendors today then

## 60260:00 - 60295:00

understanding how to use it in their own

## 60295:00 - 60320:00

and build with it in their own products

## 60320:00 - 60365:00

and then ultimately incorporating AI

## 60365:00 - 60395:00

into a feature that someone has built

## 60395:00 - 60440:00

here at Sprague Ryan I'd be curious to

## 60440:00 - 60505:00

get your perspective on how you think

## 60505:00 - 60575:00

other CEOs similar to you might think

## 60575:00 - 60625:00

about building products in this new

## 60625:00 - 60655:00

world I think there's some Nuance

## 60655:00 - 60705:00

because of obviously the founding of

## 60705:00 - 60750:00

sprig was oriented around Ai and the

## 60750:00 - 60775:00

ability to sort of synthesize

## 60775:00 - 60815:00

information but I'm curious I'm sure you

## 60815:00 - 60840:00

spent a bunch of time with other CEOs

## 60840:00 - 60875:00

that have you know a product in Market

## 60875:00 - 60915:00

with early traction are doing well so in

## 60915:00 - 60940:00

some ways they're incumbent but they're

## 60940:00 - 60980:00

not you know Salesforce or AWS or

## 60980:00 - 61000:00

something like that so they're a scaling

## 61000:00 - 61055:00

startup and we have this new wave of

## 61055:00 - 61105:00

pools basically at their disposal do you

## 61105:00 - 61130:00

have any thoughts on sort of advice or

## 61130:00 - 61170:00

perspectives you'd give to other similar

## 61170:00 - 61225:00

types of of CEOs and Founders to try to

## 61225:00 - 61255:00

help them kind of navigate this and also

## 61255:00 - 61310:00

maybe reduce the chance that they just

## 61310:00 - 61350:00

Chase shiny objects all the time which I

## 61350:00 - 61370:00

think is probably one of the number one

## 61370:00 - 61395:00

critiques of what's happening right now

## 61395:00 - 61425:00

to give you know recommendations and

## 61425:00 - 61470:00

advice for others I think a lot of CEOs

## 61470:00 - 61490:00

right now are thinking about what is

## 61490:00 - 61535:00

their AI roadmap and there's probably

## 61535:00 - 61565:00

expected to have something if it's

## 61565:00 - 61580:00

something that you're really serious

## 61580:00 - 61620:00

about I do think it's critical to bring

## 61620:00 - 61665:00

in an experienced data scientist with an

## 61665:00 - 61705:00

AI AI backgrounds into the company you

## 61705:00 - 61735:00

know very similar to for all the reasons

## 61735:00 - 61760:00

that you know Kevin has been sharing it

## 61760:00 - 61780:00

I've been sharing about you know why

## 61780:00 - 61815:00

Kevin's been so integral to Our Success

## 61815:00 - 61875:00

is that you do need an a architect and

## 61875:00 - 61905:00

historically companies have had a CTO

## 61905:00 - 61950:00

for the technology and thinking about

## 61950:00 - 61990:00

the architecture of the technology and

## 61990:00 - 62025:00

the stack and how they're going to build

## 62025:00 - 62060:00

their architecture and I think going

## 62060:00 - 62095:00

forward many companies will bring on AI

## 62095:00 - 62130:00

Architects that might even be at the

## 62130:00 - 62175:00

same level or report directly to a CTO

## 62175:00 - 62200:00

to think about what are the models that

## 62200:00 - 62225:00

we're going to use and what are the

## 62225:00 - 62250:00

boundaries of AI and how can we build

## 62250:00 - 62300:00

reproducible Ai and think about this in

## 62300:00 - 62335:00

a systematic way to build a foundation

## 62335:00 - 62400:00

for a company to be AI first and so for

## 62400:00 - 62430:00

here at sprig as we shift to being an AI

## 62430:00 - 62470:00

first company you know Kevin is tasked

## 62470:00 - 62505:00

with setting our AI vision from a

## 62505:00 - 62540:00

technology perspective but also ensuring

## 62540:00 - 62605:00

that our entire pde team knows how to

## 62605:00 - 62650:00

build AI features and functionality and

## 62650:00 - 62705:00

so it's you know very large challenge of

## 62705:00 - 62715:00

thinking about all these different

## 62715:00 - 62750:00

dimensions but also helping guide and

## 62750:00 - 62785:00

steer our roadmap and so if you're

## 62785:00 - 62810:00

really serious about AI which I imagine

## 62810:00 - 62860:00

most companies are having that AI

## 62860:00 - 62900:00

architect to lead the way is going to be

## 62900:00 - 62925:00

really the I think the start the first

## 62925:00 - 62955:00

step I think the second thing is

## 62955:00 - 62985:00

continue to stay focused on the customer

## 62985:00 - 63015:00

value that your customers are looking

## 63015:00 - 63050:00

for and so a lot of companies right now

## 63050:00 - 63085:00

I'm seeing are you know coming up with

## 63085:00 - 63130:00

Solutions with AI instead of actually

## 63130:00 - 63175:00

thinking about what is an existing

## 63175:00 - 63220:00

problem that exists today that AI can

## 63220:00 - 63250:00

actually solve now that maybe didn't

## 63250:00 - 63290:00

exist in the world previously and scene

## 63290:00 - 63325:00

AI is really just a means to delivering

## 63325:00 - 63350:00

customer value and not something that

## 63350:00 - 63395:00

you want to rely on to create a new

## 63395:00 - 63420:00

solution that doesn't maybe solve

## 63420:00 - 63445:00

something that a customer is looking to

## 63445:00 - 63490:00

do and so a lot of you know AI launches

## 63490:00 - 63515:00

and features that were seen announced

## 63515:00 - 63550:00

that are interesting technological

## 63550:00 - 63575:00

breakthroughs or maybe new ways to apply

## 63575:00 - 63610:00

AI but it's not always clear what

## 63610:00 - 63630:00

exactly the problems that they're

## 63630:00 - 63650:00

solving so the end of the day the

## 63650:00 - 63670:00

customer is still looking to grow from

## 63670:00 - 63705:00

point A to point B and just like other

## 63705:00 - 63750:00

Technologies AI is a way to get them

## 63750:00 - 63790:00

from point A to point B the third thing

## 63790:00 - 63850:00

is we are seeing the incumbents uh

## 63850:00 - 63880:00

Microsoft you know being one great

## 63880:00 - 63920:00

example as actually the leaders in the

## 63920:00 - 63950:00

field of AI and so we're seeing a lot of

## 63950:00 - 63975:00

you know from my perspective a lot of

## 63975:00 - 64010:00

startups are having trouble breaking

## 64010:00 - 64045:00

into Industries because they don't own

## 64045:00 - 64080:00

the core workflow or they don't have the

## 64080:00 - 64140:00

proprietary data to provide the AI model

## 64140:00 - 64175:00

and so yeah you mentioned if other

## 64175:00 - 64220:00

customers launched text analysis as a

## 64220:00 - 64250:00

competitive threat to us we own the

## 64250:00 - 64295:00

proprietary data that we collect with

## 64295:00 - 64355:00

sprig's own sdks and directly from our

## 64355:00 - 64405:00

customers customers and so we know that

## 64405:00 - 64460:00

by owning and continuing to collect that

## 64460:00 - 64500:00

proprietary data ourselves it sets us up

## 64500:00 - 64525:00

to be a vertically integrated solution

## 64525:00 - 64565:00

to end that own that workflow from end

## 64565:00 - 64595:00

to end and so we're seeing startups

## 64595:00 - 64640:00

emerge that might own just the analysis

## 64640:00 - 64675:00

but the companies that are actually are

## 64675:00 - 64715:00

owning that data themselves could easily

## 64715:00 - 64765:00

build in that analysis and so new very

## 64765:00 - 64785:00

early on that we wanted to focus on

## 64785:00 - 64820:00

collecting our own data and then

## 64820:00 - 64855:00

following the breakthroughs of AI to

## 64855:00 - 64895:00

then start to incorporate AI to analyze

## 64895:00 - 64930:00

that data at large scale and together

## 64930:00 - 64965:00

the collection analysis is ultimately

## 64965:00 - 64985:00

that value that we're delivering our

## 64985:00 - 65020:00

customers of helping them understand

## 65020:00 - 65055:00

deeply how to improve their user

## 65055:00 - 65095:00

experience and so if you are you know a

## 65095:00 - 65120:00

founder or someone working on AI you

## 65120:00 - 65150:00

really need to think about if you're not

## 65150:00 - 65175:00

owning that core workflow or if you're

## 65175:00 - 65210:00

not owning the data yourself then it's

## 65210:00 - 65240:00

very easy to be disrupted and someone

## 65240:00 - 65270:00

else could easily you know and most

## 65270:00 - 65305:00

likely will build what you're delivering

## 65305:00 - 65340:00

your customers maybe this would be a

## 65340:00 - 65380:00

good place to sort of wrap up and on a

## 65380:00 - 65410:00

similar theme have you share a little

## 65410:00 - 65445:00

bit more about how each of you think

## 65445:00 - 65495:00

about maybe the next 6 12 18 24 months

## 65495:00 - 65540:00

in this wave of llms and maybe what are

## 65540:00 - 65560:00

some of the things that you think are

## 65560:00 - 65595:00

over hyped and some of the things that

## 65595:00 - 65625:00

you think are under hyped not even in

## 65625:00 - 65650:00

like the 10-year vision of what's

## 65650:00 - 65690:00

happening in AI but maybe the sort of

## 65690:00 - 65730:00

near-term future in the sense of where

## 65730:00 - 65750:00

you think there's a lot of really

## 65750:00 - 65775:00

exciting opportunity where you think

## 65775:00 - 65795:00

we're going to see some really big

## 65795:00 - 65835:00

breakthroughs and a ton of End customer

## 65835:00 - 65875:00

value delivered versus what are the

## 65875:00 - 65900:00

things that maybe are a little bit more

## 65900:00 - 65930:00

Mirage like that everybody feels like is

## 65930:00 - 65965:00

going to happen in the next 12 or 24

## 65965:00 - 66000:00

months but given your understanding of

## 66000:00 - 66020:00

the Contours of the problem it's

## 66020:00 - 66045:00

actually probably going to take three

## 66045:00 - 66080:00

five or ten years to sort of see that

## 66080:00 - 66105:00

thing exist in the world a couple

## 66105:00 - 66145:00

immediate ones that come to mind include

## 66145:00 - 66170:00

uh this is something that we've been

## 66170:00 - 66220:00

dealing with at sprig is the ability of

## 66220:00 - 66270:00

a model such as an llm to successfully

## 66270:00 - 66310:00

answer a quantitative question or do

## 66310:00 - 66355:00

math or even count to ten successfully

## 66355:00 - 66385:00

you know right now a lot of these models

## 66385:00 - 66430:00

fall flat and for an application like

## 66430:00 - 66460:00

ours and for a lot of applications out

## 66460:00 - 66490:00

there that's kind of a pretty glaring

## 66490:00 - 66525:00

Omission you know these models are

## 66525:00 - 66550:00

fantastic at summarization they're

## 66550:00 - 66575:00

really good at generating text based on

## 66575:00 - 66620:00

other texts but uh they're not they're

## 66620:00 - 66655:00

not quite good at you know basic math

## 66655:00 - 66685:00

and thing things of that nature so if

## 66685:00 - 66705:00

you're trying to do any sort of analysis

## 66705:00 - 66750:00

it's it really is kind of a big Omission

## 66750:00 - 66780:00

right now and I'll just jump in there

## 66780:00 - 66800:00

because that's a big topic we didn't

## 66800:00 - 66835:00

cover that's been a huge challenge for

## 66835:00 - 66890:00

us is simple comparison of integers that

## 66890:00 - 66915:00

you would expect to be second grade

## 66915:00 - 66970:00

third grade math is shockingly incorrect

## 66970:00 - 67020:00

on the results uh so I won't go into

## 67020:00 - 67050:00

that any further but I think just want

## 67050:00 - 67090:00

to emphasize what Kevin was calling out

## 67090:00 - 67135:00

there is that it's been a a major

## 67135:00 - 67170:00

challenge for us to work around and

## 67170:00 - 67210:00

talking about the bounds of AI That's

## 67210:00 - 67245:00

sort of something that right now it is a

## 67245:00 - 67280:00

wall that that we are hitting here at

## 67280:00 - 67310:00

Sprague yeah and you know it's something

## 67310:00 - 67355:00

that's not entirely unexpected it's just

## 67355:00 - 67395:00

not what llms were created for they were

## 67395:00 - 67430:00

created to go from input to Output with

## 67430:00 - 67470:00

text numbers can be text but it's it's

## 67470:00 - 67495:00

kind of a different domain but yeah

## 67495:00 - 67520:00

that's one thing are there certain

## 67520:00 - 67570:00

implications of that or or does it

## 67570:00 - 67610:00

highlight maybe a misunderstanding is

## 67610:00 - 67645:00

people might have today as it relates to

## 67645:00 - 67675:00

the technology and think it's both yeah

## 67675:00 - 67710:00

it's definitely a misunderstanding I

## 67710:00 - 67760:00

think people will see have seen chat gbt

## 67760:00 - 67795:00

do amazing things they'll ask it to

## 67795:00 - 67840:00

write a recipe to summarize an email to

## 67840:00 - 67880:00

write like a pirate whatever and it just

## 67880:00 - 67905:00

knocks those out of the park and then

## 67905:00 - 67945:00

somebody asks it to do their taxes or

## 67945:00 - 68010:00

you know like uh add 12 plus 18 and it

## 68010:00 - 68040:00

returns four or something right and

## 68040:00 - 68070:00

people kind of say whoa what's going on

## 68070:00 - 68100:00

like this thing is incredibly

## 68100:00 - 68130:00

intelligent in some cases superhumanly

## 68130:00 - 68160:00

intelligence but it can't do second

## 68160:00 - 68190:00

grade math like what's going on so that

## 68190:00 - 68220:00

you know I think that is really just a

## 68220:00 - 68250:00

fundamental misunderstanding probably

## 68250:00 - 68265:00

something that could have been

## 68265:00 - 68295:00

publicized better when these things came

## 68295:00 - 68325:00

out but anyways that's kind of where we

## 68325:00 - 68370:00

are do you think it it means that these

## 68370:00 - 68400:00

large language models are quote less

## 68400:00 - 68440:00

intelligent than a lot of people think I

## 68440:00 - 68465:00

think they're less capable maybe it's a

## 68465:00 - 68510:00

better word yeah it's just uh they're

## 68510:00 - 68555:00

built the way their trained supports a

## 68555:00 - 68590:00

handful of really important use cases

## 68590:00 - 68620:00

but just not everything out there people

## 68620:00 - 68660:00

have found ways of getting around this

## 68660:00 - 68700:00

problem using llms like for example

## 68700:00 - 68740:00

asking your llm to write python code

## 68740:00 - 68800:00

that will add to 16 plus 32 and in that

## 68800:00 - 68835:00

case it's really good at it but you know

## 68835:00 - 68850:00

you don't necessarily want to have to go

## 68850:00 - 68875:00

through that circuitous route to get

## 68875:00 - 68915:00

your answer aside from that's you know I

## 68915:00 - 68955:00

think we're you know related to that

## 68955:00 - 68990:00

we're starting to see the down part of

## 68990:00 - 69015:00

the hype cycle with this uh just the

## 69015:00 - 69050:00

limitations that become became pretty

## 69050:00 - 69085:00

obvious maybe that that quantitative

## 69085:00 - 69120:00

sort of failure falls under a broader

## 69120:00 - 69175:00

category of failures that these llms

## 69175:00 - 69225:00

will experience but you know despite not

## 69225:00 - 69255:00

knowing the answer we'll give an answer

## 69255:00 - 69290:00

very confidently right I think that's

## 69290:00 - 69320:00

going to be a major thing to over a

## 69320:00 - 69355:00

major challenge to overcome because you

## 69355:00 - 69380:00

know right now there's really not a good

## 69380:00 - 69430:00

way to evaluate these at scale or in an

## 69430:00 - 69460:00

automated way you can't necessarily read

## 69460:00 - 69500:00

through every single sentence a llm

## 69500:00 - 69530:00

generates when it's summarizing text for

## 69530:00 - 69560:00

you and I think that's going to hurt

## 69560:00 - 69610:00

trust in a lot of these and maybe kind

## 69610:00 - 69640:00

of slow down adoption because if you're

## 69640:00 - 69675:00

really counting on these these models to

## 69675:00 - 69705:00

you know sort of replace low level

## 69705:00 - 69740:00

intelligence as it were if you can't

## 69740:00 - 69775:00

trust it to do some basic stuff or to

## 69775:00 - 69800:00

always give you the right answer then

## 69800:00 - 69835:00

you know why would you use it right

## 69835:00 - 69870:00

especially for very for applications

## 69870:00 - 69920:00

where accuracy is very very critical so

## 69920:00 - 69960:00

yeah to your original question I think

## 69960:00 - 70000:00

issues like those hallucinations lack of

## 70000:00 - 70030:00

Quant answering those are probably going

## 70030:00 - 70050:00

to be the major things that get released

## 70050:00 - 70085:00

over the next couple years uh I don't

## 70085:00 - 70105:00

know what that looks like you know it

## 70105:00 - 70150:00

might be an llm that's part of a broader

## 70150:00 - 70190:00

sort of array of models that attack a

## 70190:00 - 70235:00

single inputs but since those are the

## 70235:00 - 70275:00

biggest you know most glaring failures

## 70275:00 - 70300:00

of these I think that's what we're going

## 70300:00 - 70335:00

to see the next 12 to 18 months I'll say

## 70335:00 - 70355:00

right now it's a little bit of like a

## 70355:00 - 70385:00

teenager phase there's a lot of maturity

## 70385:00 - 70425:00

that needs to happen or we can just put

## 70425:00 - 70475:00

all this behind us I think that exciting

## 70475:00 - 70515:00

step function that gave us a little bit

## 70515:00 - 70545:00

of glimpse of the future is auto GPT

## 70545:00 - 70580:00

where it can you can give it a very

## 70580:00 - 70625:00

complex task you can say plan a birthday

## 70625:00 - 70660:00

party in Napa for 20 people

## 70660:00 - 70705:00

with a budget of x amount of dollars and

## 70705:00 - 70745:00

it'll take that broad complex task and

## 70745:00 - 70775:00

break it up into subtasks and actually

## 70775:00 - 70815:00

run those subtasks to one model or

## 70815:00 - 70845:00

different models and actually make sure

## 70845:00 - 70890:00

and verify that each of those subtasks

## 70890:00 - 70930:00

is being done correctly and I think that

## 70930:00 - 71000:00

concept is where the next wave and I

## 71000:00 - 71020:00

think we'll see that kind of absolute

## 71020:00 - 71075:00

maximum of AI breakthroughs is that you

## 71075:00 - 71115:00

know even here at sprig we are using AI

## 71115:00 - 71160:00

to solve very specific jobs to be done

## 71160:00 - 71215:00

you know such as you run a study you

## 71215:00 - 71245:00

want to understand the study results you

## 71245:00 - 71280:00

look at the open text analysis for a

## 71280:00 - 71315:00

specific question we also are playing AI

## 71315:00 - 71355:00

to help you summarize all the open text

## 71355:00 - 71390:00

responses for a specific question but

## 71390:00 - 71420:00

what if you could actually apply the

## 71420:00 - 71465:00

concepts of Auto GPT and say write a

## 71465:00 - 71510:00

product spec about how to improve the

## 71510:00 - 71550:00

onboarding flow and the AI could then

## 71550:00 - 71605:00

run the sprig study you know for you

## 71605:00 - 71660:00

design the questions launch it optimize

## 71660:00 - 71685:00

the study so it's getting just the

## 71685:00 - 71715:00

responses that you need when the results

## 71715:00 - 71755:00

are done analyze all the results for you

## 71755:00 - 71780:00

and actually write the products back

## 71780:00 - 71815:00

based on the results that I found and

## 71815:00 - 71855:00

then you have a product spec that is

## 71855:00 - 71890:00

typically considered multiple jobs to be

## 71890:00 - 71920:00

done but you're actually delivering a

## 71920:00 - 71950:00

very complex task the AI is able to

## 71950:00 - 71990:00

break down into smaller subtasks and

## 71990:00 - 72025:00

then complete and you actually get this

## 72025:00 - 72055:00

kind of end result you could even have a

## 72055:00 - 72085:00

model then break it up into jira tickets

## 72085:00 - 72130:00

and so on and so forth exactly exactly

## 72130:00 - 72165:00

yeah it could be implement this product

## 72165:00 - 72190:00

spec it could run it by your team it

## 72190:00 - 72225:00

could break it into jira tasks it could

## 72225:00 - 72250:00

your engineers are working on it

## 72250:00 - 72290:00

Engineers are using copilot to write it

## 72290:00 - 72335:00

and so right now we're playing AI to

## 72335:00 - 72370:00

very specific steps along these broader

## 72370:00 - 72410:00

larger more complex tasks but I think

## 72410:00 - 72445:00

having AI couple those tasks together

## 72445:00 - 72475:00

into complete workflows and one thing

## 72475:00 - 72500:00

we've started to work on is actually our

## 72500:00 - 72530:00

AI Partnerships so there's a lot of

## 72530:00 - 72560:00

companies right now that are working on

## 72560:00 - 72610:00

prompts to build design

## 72610:00 - 72675:00

or Pro you know llms to ship code and

## 72675:00 - 72715:00

changes the code can we actually partner

## 72715:00 - 72755:00

with companies in the Gen design space

## 72755:00 - 72795:00

or gen development space whereas frig is

## 72795:00 - 72845:00

the input into an llm that's creating a

## 72845:00 - 72885:00

mock-up or writing code and actually

## 72885:00 - 72915:00

complete end-to-end very complex

## 72915:00 - 72960:00

workflows of several jobs to be done and

## 72960:00 - 72990:00

actually have these handoffs between

## 72990:00 - 73025:00

different agents and sprig maybe being

## 73025:00 - 73065:00

one more complex agent and so I think

## 73065:00 - 73100:00

the the eggs though is the open question

## 73100:00 - 73130:00

what is the piece that the user brings

## 73130:00 - 73190:00

to to the table to make that final cake

## 73190:00 - 73220:00

but Kevin I'm curious your thoughts on

## 73220:00 - 73260:00

that yeah um I mean what you mentioned

## 73260:00 - 73305:00

with auto GPT and what it's able to do

## 73305:00 - 73350:00

now is a great sort of window into

## 73350:00 - 73375:00

what's coming in probably the near

## 73375:00 - 73395:00

future

## 73395:00 - 73420:00

um I mean that's essentially using Auto

## 73420:00 - 73460:00

gbt or something like link chain is like

## 73460:00 - 73490:00

taking a bunch of really powerful you

## 73490:00 - 73515:00

know car parts and sort of mashing them

## 73515:00 - 73550:00

together to create you know a really

## 73550:00 - 73585:00

janky car that has a very powerful

## 73585:00 - 73610:00

engine that's the first step the neck

## 73610:00 - 73650:00

next thing that comes is sort of more

## 73650:00 - 73685:00

cohesive model that comes out of the

## 73685:00 - 73720:00

factory is able to you know do all of

## 73720:00 - 73750:00

the things you wanted it to do when you

## 73750:00 - 73770:00

were sort of gluing these pieces

## 73770:00 - 73800:00

together and once you have that I mean

## 73800:00 - 73825:00

it's just continuing this March down

## 73825:00 - 73855:00

this March towards full automation

## 73855:00 - 73910:00

across a bunch of different domains for

## 73910:00 - 73960:00

us like you said Ryan maybe that means

## 73960:00 - 73985:00

um you know determining how to build a

## 73985:00 - 74020:00

product spec for a user researcher maybe

## 74020:00 - 74050:00

it's guiding them throughout the

## 74050:00 - 74080:00

research cycle saying like hey this is

## 74080:00 - 74115:00

what your users think this is what you

## 74115:00 - 74140:00

should ask them next and depending on

## 74140:00 - 74160:00

the answer this is what you should ask

## 74160:00 - 74185:00

them after that I think it's just going

## 74185:00 - 74215:00

to guide us down or bring us down a road

## 74215:00 - 74260:00

of yeah helping at different points of

## 74260:00 - 74300:00

of uh you know somebody's somebody's

## 74300:00 - 74335:00

workday I guess just to kind of bring

## 74335:00 - 74370:00

that to life a little bit more Ryan and

## 74370:00 - 74410:00

sort of that medium-term vision of kind

## 74410:00 - 74455:00

of the auto gbt inspired ability to

## 74455:00 - 74510:00

break up tasks have them done have them

## 74510:00 - 74540:00

brought back and then have that sort of

## 74540:00 - 74570:00

loop be closed and a whole nother set of

## 74570:00 - 74600:00

tasks be kicked off and in the context

## 74600:00 - 74630:00

of the spring product do you think

## 74630:00 - 74680:00

that's if you had to guess is 6 to 12

## 74680:00 - 74715:00

months two years three years five years

## 74715:00 - 74750:00

like when you actually look at the

## 74750:00 - 74795:00

technology when you look at where all

## 74795:00 - 74835:00

this enabling technology is what's your

## 74835:00 - 74865:00

best guess in terms of that what it's

## 74865:00 - 74890:00

going to take in terms of time Horizon

## 74890:00 - 74920:00

for that Vision to come to life and the

## 74920:00 - 74950:00

exciting thing for us you know you

## 74950:00 - 74975:00

mentioned about others being able to

## 74975:00 - 75015:00

build a text analysis is that based on

## 75015:00 - 75040:00

what we've seen today in the boundaries

## 75040:00 - 75085:00

of the llms today is that we could based

## 75085:00 - 75125:00

on what we have tested but the models

## 75125:00 - 75160:00

actually build that now and we are

## 75160:00 - 75185:00

seeing the sophistication the capability

## 75185:00 - 75215:00

of the models to build that now I think

## 75215:00 - 75245:00

the roadblocks we've seen is more around

## 75245:00 - 75285:00

the reproducibility the reliability you

## 75285:00 - 75315:00

know some of the other edge cases like

## 75315:00 - 75345:00

the quantitative analysis and I think

## 75345:00 - 75380:00

the other piece is really the comfort of

## 75380:00 - 75410:00

the user and the comfort of the customer

## 75410:00 - 75465:00

with those more complex tasks and giving

## 75465:00 - 75505:00

them that control and I was actually on

## 75505:00 - 75540:00

a speaking on a webinar and I talked

## 75540:00 - 75575:00

about this co-pilot and someone chimed

## 75575:00 - 75620:00

in with a comment said copy soon to be

## 75620:00 - 75650:00

pilot you know a little bit of a dark

## 75650:00 - 75685:00

you know comment for people you know in

## 75685:00 - 75720:00

that webinar uh because I think it is

## 75720:00 - 75755:00

how do we make sure that you know there

## 75755:00 - 75780:00

is that sense of control and that we're

## 75780:00 - 75815:00

all involved and we're co-creating with

## 75815:00 - 75865:00

AI and AI is not creating for us and so

## 75865:00 - 75895:00

I think the waves that we're really

## 75895:00 - 75915:00

riding right now is really the

## 75915:00 - 75945:00

reproducibility and the

## 75945:00 - 75980:00

comprehensiveness of the models which I

## 75980:00 - 76005:00

think for Kevin and the team it's more

## 76005:00 - 76055:00

of a kind of a tactical roadblock I'll

## 76055:00 - 76080:00

save speed bump it's not really a

## 76080:00 - 76110:00

roadblock it's more of a speed bump uh

## 76110:00 - 76145:00

and then the speed bump of getting the

## 76145:00 - 76185:00

user comfortable with how far we can

## 76185:00 - 76215:00

take what's possible but we're

## 76215:00 - 76250:00

absolutely seeing really just a function

## 76250:00 - 76270:00

of time of being able to deliver on that

## 76270:00 - 76305:00

Vision which to me is so exciting about

## 76305:00 - 76340:00

starting with just text analysis and now

## 76340:00 - 76385:00

delivering on very complex workflows

## 76385:00 - 76425:00

that we've always wanted to do but

## 76425:00 - 76475:00

haven't had the llms to deliver on these

## 76475:00 - 76515:00

until now good place to end thank you to

## 76515:00 - 76545:00

so much for coming on and talking about

## 76545:00 - 76585:00

all the stuff you've been uh you've been

## 76585:00 - 76610:00

building it's frig thank you Brett

## 76610:00 - 76655:00

awesome thanks for having us

## 76655:00+

[Music]

