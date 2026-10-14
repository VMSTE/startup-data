---
source: https://www.youtube.com/watch?v=KU-gdDfQtHc
title: "Building Confluent: From open source side project to public company |
  Jay Kreps (Co-founder and CEO)"
author: First Round Capital
date: 2026-03-26
views: 605
description: >-
  Jay Kreps is the co-founder and CEO of Confluent, the company built around
  Apache Kafka — the open-source data streaming platform he originally built
  while at LinkedIn. In this conversation, Jay shares his full journey: how
  Confluent grew from a scrappy group of engineers with no go-to-market
  experience into a publicly traded enterprise software company. He makes the
  case that the difference between what a company can do, and what it must do,
  is one of the most underrated building levers; illustrated through his years
  spent pushing Confluent towards a cloud product, in the face of widespread
  opposition.


  In this episode, we discuss:

  • Why moving from software engineer to CEO requires almost an entirely new
  skillset

  • The product marketing pyramid Jay built to explain Kafka to the world

  • How Confluent bludgeoned its way to a cloud-first business when the early
  product was “embarrassing”

  • The critical difference between what a company can do and what it must do

  • What keeps scaling companies from becoming "Chipotle”


  References:

  • Amazon Web Services: https://aws.amazon.com/

  • Apache Kafka: https://kafka.apache.org/

  • Benchmark: https://www.benchmark.com/

  • Confluent: https://www.confluent.io/

  • Jun Rao: https://www.linkedin.com/in/junrao

  • LinkedIn: https://www.linkedin.com/

  • McKinsey & Company: https://www.mckinsey.com/

  • MySpace: https://www.myspace.com/

  • Neha Narkhede: https://www.linkedin.com/in/nehanarkhede

  • Oracle: https://www.oracle.com/

  • Red Hat: https://www.redhat.com/

  • Snowflake: https://www.snowflake.com/


  Where to find Jay:

  • LinkedIn: https://www.linkedin.com/in/jaykreps/

  • Twitter/X: https://x.com/jaykreps


  Where to find Brett:

  • LinkedIn: https://www.linkedin.com/in/brett-berson-9986094/

  • Twitter/X: https://twitter.com/brettberson


  Where to find First Round Capital:

  • Website: https://firstround.com/

  • First Round Review: https://review.firstround.com/

  • Twitter/X: https://twitter.com/firstround

  • YouTube: https://www.youtube.com/@FirstRoundCapital

  • This podcast on all platforms: https://review.firstround.com/podcast


  Timestamps:

  01:18 Making the leap from engineer to CEO

  03:33 The 80% rule: what a CEO actually needs to know 

  04:54 Scaling different business disciplines 

  09:31 How Confluent’s story began in LinkedIn

  12:13 The growing need for scalable data tech

  13:37 What the early Kafka product looked like

  16:38 Kafka’s underwhelming open-source launch

  18:38 The blog post that accelerated Kafka’s adoption

  20:16 Why so many marketing messages fail

  28:08 The decision to build Confluent 

  34:24 Planning to fundraise before building the product

  39:19 Confluent’s early years: Tough product decisions

  47:07 The underrated growth lever question for companies

  55:46 Why founder optimism is an overrated trait

  1:00:29 What should founders give up as they scale?

  1:02:47 Why people become trapped in a failure mindset

  1:08:33 The Chipotle problem: Losing excellence at scale
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:20:06.570Z
---

# Building Confluent: From open source side project to public company | Jay Kreps (Co-founder and CEO)

## 00:00 - 30:00

For today's episode, I'm sitting down

## 30:00 - 65:00

with Jay Krops. He's the co-founder and

## 65:00 - 100:00

CEO of Confluent, the data streaming

## 100:00 - 145:00

platform built around Apache Kafka, the

## 145:00 - 175:00

open- source system he and his

## 175:00 - 200:00

co-founders created while they were

## 200:00 - 245:00

working as engineers at LinkedIn. In our

## 245:00 - 280:00

conversation, Jay shares what it takes

## 280:00 - 320:00

to go from software engineer to CEO. I

## 320:00 - 370:00

think the CEO job generally you operate

## 370:00 - 425:00

more in a kind of fog of partial

## 425:00 - 455:00

understanding. Very quickly, as the

## 455:00 - 475:00

organization gets bigger, it's

## 475:00 - 500:00

impossible to know everything about

## 500:00 - 505:00

everything.

## 505:00 - 545:00

>> He traces Confluence Origins as an

## 545:00 - 585:00

open-source project and shares how they

## 585:00 - 615:00

landed their first enterprise customers

## 615:00 - 650:00

when the product was nowhere near done.

## 650:00 - 685:00

The software product that doesn't have

## 685:00 - 715:00

nearly enough features. We've taken that

## 715:00 - 750:00

out to very large enterprises that we

## 750:00 - 785:00

have no business working with for more

## 785:00 - 810:00

money than we feel at all comfortable

## 810:00 - 840:00

with. How a single blog post did more

## 840:00 - 875:00

for Confluence adoption than years of

## 875:00 - 905:00

engineering. If we can't express why

## 905:00 - 935:00

this is exciting, it's probably not

## 935:00 - 965:00

going to be that successful of an open

## 965:00 - 980:00

source project.

## 980:00 - 1020:00

>> And why they bet everything on a cloud

## 1020:00 - 1050:00

product that investors and half the

## 1050:00 - 1080:00

company thought was a terrible idea.

## 1080:00 - 1110:00

>> We just kind of bludgeoned our way

## 1110:00 - 1145:00

through like none of it was pretty. Some

## 1145:00 - 1190:00

of our biggest early customers quit on

## 1190:00 - 1305:00

us. Let's dive in.

## 1305:00 - 1340:00

What's surprised you most? Like you

## 1340:00 - 1385:00

started the company as a software

## 1385:00 - 1410:00

engineer.

## 1410:00 - 1420:00

>> Yeah.

## 1420:00 - 1450:00

>> And now you've had the full

## 1450:00 - 1485:00

>> Yeah. I mean lots of things have been

## 1485:00 - 1525:00

lots of things have been surprising. You

## 1525:00 - 1585:00

know, probably initially

## 1585:00 - 1625:00

the surprising thing was just how much

## 1625:00 - 1675:00

of a jump in the deep end learning curve

## 1675:00 - 1725:00

there is for going from software you

## 1725:00 - 1760:00

know like the I the skill sets are

## 1760:00 - 1785:00

almost exactly opposite even though

## 1785:00 - 1825:00

that's a it's not uncommon you know for

## 1825:00 - 1860:00

this kind of tech company but it's still

## 1860:00 - 1885:00

you know the set of things that you need

## 1885:00 - 1950:00

to be good at are you know communication

## 1950:00 - 1985:00

uh your the decisions you're making are

## 1985:00 - 2025:00

very different you know certainly For

## 2025:00 - 2060:00

engineering decisions,

## 2060:00 - 2085:00

they're mostly knowable and there's

## 2085:00 - 2110:00

mostly kind of right and wrong answers,

## 2110:00 - 2155:00

but usually, especially the early phase

## 2155:00 - 2190:00

of a company, you're making a lot of

## 2190:00 - 2250:00

kind of very big critical decisions

## 2250:00 - 2285:00

with a lot of unknowable aspects, you

## 2285:00 - 2315:00

know, but it'll certainly impact how the

## 2315:00 - 2345:00

company turns out and you know that, but

## 2345:00 - 2375:00

you don't know what the right answer is,

## 2375:00 - 2410:00

and you won't find out until later. So,

## 2410:00 - 2425:00

you know, I think in a lot of those

## 2425:00 - 2465:00

areas, it's it's quite different. And I

## 2465:00 - 2545:00

I think the CEO job generally you're um

## 2545:00 - 2610:00

you operate, you know, much more in a

## 2610:00 - 2660:00

kind of fog of partial understanding.

## 2660:00 - 2680:00

You know, I don't know that everybody

## 2680:00 - 2720:00

understands that that very quickly as

## 2720:00 - 2740:00

the organization gets bigger, it's

## 2740:00 - 2765:00

impossible to know everything about

## 2765:00 - 2820:00

everything. And so you have to kind of

## 2820:00 - 2865:00

be roughly directionally right. And

## 2865:00 - 2900:00

people see this often in executives and

## 2900:00 - 2920:00

it bothers them of like, oh, they don't

## 2920:00 - 2945:00

understand that thing. And it's true,

## 2945:00 - 2970:00

right? You you but in practice, you

## 2970:00 - 2990:00

can't understand everything about

## 2990:00 - 3020:00

everything. You have to understand a lot

## 3020:00 - 3040:00

about the most important things and

## 3040:00 - 3065:00

enough about some of the other things

## 3065:00 - 3105:00

and try and make that judgment. And the

## 3105:00 - 3135:00

feel of doing that and how you do it, I

## 3135:00 - 3165:00

think is, you know, probably also

## 3165:00 - 3210:00

surprising if you come out of a kind of

## 3210:00 - 3240:00

engineering path where you do, you know,

## 3240:00 - 3260:00

you don't do that at all. There's no

## 3260:00 - 3310:00

shooting from hip. In the first bucket,

## 3310:00 - 3340:00

if you think about going from software

## 3340:00 - 3390:00

engineer to founder and then over time

## 3390:00 - 3440:00

founder to CEO, what's your clustering

## 3440:00 - 3475:00

of the things you have to figure out at

## 3475:00 - 3520:00

some point? Well, it's a it's a lot of

## 3520:00 - 3565:00

things. I mean, I think CEOs need to

## 3565:00 - 3650:00

know, you know, about 80% of what their

## 3650:00 - 3680:00

executives know about their function, I

## 3680:00 - 3705:00

think, over time. So, really kind of

## 3705:00 - 3745:00

learn that discipline. Not enough to be

## 3745:00 - 3805:00

good at it, but enough to be to know

## 3805:00 - 3845:00

good what good is and know if it's going

## 3845:00 - 3880:00

well. And so I think there's just a very

## 3880:00 - 3920:00

long there's a large learning curve

## 3920:00 - 3945:00

because you end up having to understand

## 3945:00 - 3975:00

a bunch of these discipline, you know,

## 3975:00 - 4015:00

what what is a head of marketing do and

## 4015:00 - 4045:00

what each of the subgroups of marketing

## 4045:00 - 4070:00

do and how are we doing it and how does

## 4070:00 - 4110:00

that apply in our business and you know

## 4110:00 - 4160:00

what's the finance team for and you know

## 4160:00 - 4195:00

all those kind of things. I I think that

## 4195:00 - 4245:00

what why do you think 80%. Not 90, not

## 4245:00 - 4260:00

50, not 20.

## 4260:00 - 4295:00

>> Yeah. Yeah. I think, you know, it's just

## 4295:00 - 4330:00

Yeah. I mean, ideally it should be 100%.

## 4330:00 - 4365:00

Right. But it's just not practically if

## 4365:00 - 4425:00

somebody's done that job for 10 years

## 4425:00 - 4470:00

and you're kind of a dilotant who steps

## 4470:00 - 4530:00

in every time there's a a role to fill

## 4530:00 - 4565:00

and then maybe manages it indirectly

## 4565:00 - 4600:00

through them. you know, 80% is kind of

## 4600:00 - 4625:00

aspirationally the best you'll be able

## 4625:00 - 4650:00

to do for all of the different

## 4650:00 - 4690:00

disciplines as the business begins to

## 4690:00 - 4745:00

scale. Did you think about what is

## 4745:00 - 4795:00

correct in the context of confluent?

## 4795:00 - 4815:00

Yeah, I think that that's really

## 4815:00 - 4870:00

critical and I think each discipline I I

## 4870:00 - 4905:00

always think of it as having some degree

## 4905:00 - 4970:00

of kind of carryover, you know. So if

## 4970:00 - 5010:00

you think about say a finance team, if

## 5010:00 - 5040:00

you're kind of plugging from one SAS

## 5040:00 - 5075:00

company to another, how much is it

## 5075:00 - 5105:00

basically the same thing right

## 5105:00 - 5140:00

everywhere and how much of it is going

## 5140:00 - 5165:00

to be unique to you? And I would say

## 5165:00 - 5215:00

it's actually pretty high that it's the

## 5215:00 - 5260:00

same across. So it's a very transferable

## 5260:00 - 5300:00

discipline. And then you know I think

## 5300:00 - 5345:00

when you get into uh aspects of software

## 5345:00 - 5365:00

engineering I think it's very

## 5365:00 - 5395:00

transferable like engineering teams are

## 5395:00 - 5430:00

relatively structurally similar. They'll

## 5430:00 - 5455:00

have different concentrations and

## 5455:00 - 5480:00

specialties, but it's not massively

## 5480:00 - 5505:00

different. And then you get into

## 5505:00 - 5540:00

something like product is quite

## 5540:00 - 5555:00

different, right? I mean, there's

## 5555:00 - 5605:00

obviously some transferable practices,

## 5605:00 - 5630:00

but you actually need to make good

## 5630:00 - 5680:00

decisions in that space about that

## 5680:00 - 5705:00

thing. You know, I think each of these

## 5705:00 - 5760:00

organizations has, you know, different

## 5760:00 - 5790:00

uh different genres and so you need to

## 5790:00 - 5845:00

know what what genre of marketing team

## 5845:00 - 5875:00

am I going to have and that requires

## 5875:00 - 5915:00

having some opinion about what the go to

## 5915:00 - 5965:00

market is going to be like and you know

## 5965:00 - 6005:00

I think probably for early companies

## 6005:00 - 6045:00

that go to market construction is is

## 6045:00 - 6065:00

probably one of the areas where this

## 6065:00 - 6100:00

goes the most wrong where you're

## 6100:00 - 6135:00

effectively you're trying you're talking

## 6135:00 - 6155:00

to people and you're trying to cut and

## 6155:00 - 6185:00

paste what they've done into your

## 6185:00 - 6215:00

organization but without really thinking

## 6215:00 - 6265:00

about the problem that you need to solve

## 6265:00 - 6300:00

and I think go to market people are

## 6300:00 - 6345:00

often very executionoriented and so I

## 6345:00 - 6375:00

would say they're often guilty of this

## 6375:00 - 6405:00

where it's like hey this is the playbook

## 6405:00 - 6460:00

I have done I will do this playbook here

## 6460:00 - 6485:00

but ultimately if you think about what

## 6485:00 - 6525:00

is go to market doing you know it's

## 6525:00 - 6585:00

trying to help the customer find you

## 6585:00 - 6630:00

figure out the value you know make use

## 6630:00 - 6700:00

of the product in some A and that like

## 6700:00 - 6740:00

particular journey is actually very

## 6740:00 - 6770:00

unique for each company and so you have

## 6770:00 - 6795:00

to actually think okay what techniques

## 6795:00 - 6830:00

are going to work well for us and which

## 6830:00 - 6880:00

are not going to work well. You you know

## 6880:00 - 6940:00

you see this a lot where aspirationally

## 6940:00 - 6990:00

the founder would love to have kind of a

## 6990:00 - 7030:00

very productled motion but in fact the

## 7030:00 - 7050:00

product does not particularly lend

## 7050:00 - 7095:00

itself to that and you know they're

## 7095:00 - 7120:00

they're will they're trying to will that

## 7120:00 - 7150:00

into existence but it's actually not you

## 7150:00 - 7180:00

know if you think about who's going to

## 7180:00 - 7205:00

make a decision about using this thing

## 7205:00 - 7220:00

and what they're going to go through

## 7220:00 - 7250:00

it's going to be very hard to do it that

## 7250:00 - 7290:00

way and so you know I think that's one

## 7290:00 - 7325:00

that's that's a common example of people

## 7325:00 - 7365:00

trying to pick the mechanic mix

## 7365:00 - 7400:00

independent of the problem that's being

## 7400:00 - 7435:00

solved and I I think that's true to some

## 7435:00 - 7470:00

extent in every discipline but maybe go

## 7470:00 - 7505:00

to market is the most common. So did you

## 7505:00 - 7595:00

find that you need to bring in

## 7595:00 - 7625:00

go to market talent that was very

## 7625:00 - 7675:00

pioneering and sort of curiosity

## 7675:00 - 7720:00

oriented or did it mean that for far

## 7720:00 - 7750:00

longer than you would ever imagine you

## 7750:00 - 7790:00

were intimately involved? Yeah,

## 7790:00 - 7855:00

definitely definitely my you know I was

## 7855:00 - 7880:00

pretty heavily involved in the go to

## 7880:00 - 7920:00

market for was that counterintuitive to

## 7920:00 - 7965:00

start the way Confluent came about there

## 7965:00 - 8005:00

was a open- source project that was out

## 8005:00 - 8030:00

there and had some traction before the

## 8030:00 - 8065:00

company came around

## 8065:00 - 8110:00

>> and since I was the CEO as we were

## 8110:00 - 8130:00

starting the company it was a group of

## 8130:00 - 8155:00

technical people it was like okay we got

## 8155:00 - 8175:00

to go figure out how to get customers

## 8175:00 - 8205:00

and sell this thing and that was kind of

## 8205:00 - 8245:00

on day one an important problem to go

## 8245:00 - 8280:00

solve and so it was kind of natural that

## 8280:00 - 8330:00

would be the case and the the common you

## 8330:00 - 8360:00

know the common wisdom in this area I

## 8360:00 - 8395:00

think is exactly right which is like you

## 8395:00 - 8415:00

know the founders have to figure out how

## 8415:00 - 8465:00

to sell the thing maybe poorly you know

## 8465:00 - 8520:00

but just kind of stumble through it and

## 8520:00 - 8575:00

in many ways that early experience of

## 8575:00 - 8605:00

you know selling our product was I I

## 8605:00 - 8645:00

think very valuable through the whole

## 8645:00 - 8690:00

life cycle of the company because later

## 8690:00 - 8740:00

on much of what will happen in that

## 8740:00 - 8790:00

journey has whole teams that do little

## 8790:00 - 8820:00

subp parts of it. But it's very hard for

## 8820:00 - 8845:00

those teams to kind of think about that

## 8845:00 - 8870:00

bigger picture. But just having gone

## 8870:00 - 8895:00

through that process of like, hey, this

## 8895:00 - 8930:00

is how people find out about us. This is

## 8930:00 - 8975:00

why they decide to use us. This is what

## 8975:00 - 9000:00

has to happen before they've got the

## 9000:00 - 9030:00

value out of it. Then you can kind of

## 9030:00 - 9075:00

start to construct an organization that,

## 9075:00 - 9130:00

you know, makes that go faster than that

## 9130:00 - 9175:00

does it at scale. And so yeah, you know,

## 9175:00 - 9220:00

in a sense, I thought it was natural,

## 9220:00 - 9245:00

you know, that that's always an area

## 9245:00 - 9275:00

you're gonna and and companies, you

## 9275:00 - 9315:00

know, grow, you always want more growth.

## 9315:00 - 9340:00

You always, you know, you always want to

## 9340:00 - 9365:00

move faster on that. So, it's natural

## 9365:00 - 9395:00

that that's an area you're going to put

## 9395:00 - 9435:00

time into. Maybe just so we have a

## 9435:00 - 9460:00

little bit more scaffolding, you can

## 9460:00 - 9490:00

give us the trailer version of the

## 9490:00 - 9520:00

Confluence story going all the way back

## 9520:00 - 9540:00

to when you were at LinkedIn and then

## 9540:00 - 9570:00

we'll use that as sort of a jumping off

## 9570:00 - 9575:00

point.

## 9575:00 - 9620:00

>> Yeah, sure. So um you know I joined

## 9620:00 - 9680:00

LinkedIn in 2007 and I think it was a

## 9680:00 - 9700:00

pretty small company at that time. It

## 9700:00 - 9715:00

was probably probably less than 100

## 9715:00 - 9745:00

people but had been around for you know

## 9745:00 - 9795:00

a few years and you know it was an

## 9795:00 - 9850:00

interesting time for software. I joined

## 9850:00 - 9900:00

you know the area I had studied when I

## 9900:00 - 9920:00

was in school and I was deeply

## 9920:00 - 9945:00

interested in was machine learning but

## 9945:00 - 9970:00

it was kind of early in the use of

## 9970:00 - 10015:00

machine learning in software companies

## 10015:00 - 10055:00

and I I came so I was looking for a role

## 10055:00 - 10095:00

which would kind of apply this where I

## 10095:00 - 10120:00

could kind of use these skills and I

## 10120:00 - 10140:00

thought LinkedIn would be a good place

## 10140:00 - 10185:00

for it because there's very interesting

## 10185:00 - 10220:00

data in these social networks about the

## 10220:00 - 10250:00

world and it just seemed like there'd be

## 10250:00 - 10290:00

a lot of applications so you know so

## 10290:00 - 10330:00

that was kind of what got me excited

## 10330:00 - 10370:00

excited and made me want to go there. It

## 10370:00 - 10415:00

turned out in practice it was pretty

## 10415:00 - 10460:00

tricky to pull off that kind of machine

## 10460:00 - 10505:00

learning oriented product. I I you know

## 10505:00 - 10550:00

I worked on some of the data driven

## 10550:00 - 10590:00

functionality they had there around you

## 10590:00 - 10620:00

know recommending people you would know

## 10620:00 - 10640:00

or

## 10640:00 - 10670:00

>> um coming up with the similar profiles

## 10670:00 - 10715:00

but end to end as an individual engineer

## 10715:00 - 10745:00

it was kind of hard to take something

## 10745:00 - 10785:00

you knew and get the right products

## 10785:00 - 10815:00

specified. you know, ultimately was a

## 10815:00 - 10850:00

relatively productdriven thing and so

## 10850:00 - 10885:00

kind of a something something happened

## 10885:00 - 10930:00

and then a specification came out and

## 10930:00 - 10950:00

then that was the thing the engineering

## 10950:00 - 10980:00

team built. And so it was hard to kind

## 10980:00 - 11010:00

of say, hey, you know, for these kind of

## 11010:00 - 11045:00

relevanceoriented techniques, this is

## 11045:00 - 11085:00

where the opportunity lies, at least for

## 11085:00 - 11120:00

me as a software engineer early on. And

## 11120:00 - 11160:00

so, yeah, I was I was kind of frustrated

## 11160:00 - 11205:00

by that. And then as a result, you know,

## 11205:00 - 11240:00

I kind of realized like, hey, half the

## 11240:00 - 11275:00

problem in any of these products is

## 11275:00 - 11315:00

actually not the machine learning stuff.

## 11315:00 - 11365:00

It's actually just the data like getting

## 11365:00 - 11395:00

getting it being able to work with it at

## 11395:00 - 11425:00

scale, being able to apply it, being

## 11425:00 - 11465:00

able to do that in the context of like a

## 11465:00 - 11530:00

real running production system. And so I

## 11530:00 - 11575:00

ended up spending most of my time on,

## 11575:00 - 11615:00

you know, kind of data infrastructure.

## 11615:00 - 11650:00

And that was early. You know, there

## 11650:00 - 11700:00

there's been a whole rise of cloud

## 11700:00 - 11745:00

computing and open source and, you know,

## 11745:00 - 11785:00

whole waves of data systems that are

## 11785:00 - 11815:00

oriented at making this stuff easy, but

## 11815:00 - 11850:00

this was kind of right at the very

## 11850:00 - 11865:00

beginning of that. So, you just didn't

## 11865:00 - 11905:00

have most of it. You know, there was

## 11905:00 - 11935:00

couple of open source databases, but

## 11935:00 - 11965:00

nothing really built to operate at

## 11965:00 - 12005:00

scale. And there was there was a whole

## 12005:00 - 12050:00

revolution happening around distributed

## 12050:00 - 12090:00

systems and and distributed computing

## 12090:00 - 12115:00

that kind of Google was pioneering but

## 12115:00 - 12155:00

it was all locked up inside Google. You

## 12155:00 - 12185:00

know there was a period of time where

## 12185:00 - 12225:00

there was a really significant need for

## 12225:00 - 12295:00

scalable data technologies. There was no

## 12295:00 - 12335:00

commercial offerings whatsoever that

## 12335:00 - 12390:00

addressed that. And um there was a rise

## 12390:00 - 12425:00

of open source technology but none of it

## 12425:00 - 12460:00

addressed that either. So there was just

## 12460:00 - 12515:00

nothing but everybody needed it. And you

## 12515:00 - 12550:00

know that kind of made it a really key

## 12550:00 - 12570:00

problem for any of the technology

## 12570:00 - 12630:00

companies of the day. And you know um I

## 12630:00 - 12670:00

felt that that was true for you know all

## 12670:00 - 12700:00

the data technology that was out there

## 12700:00 - 12750:00

that there was an opportunity for any of

## 12750:00 - 12780:00

the classical databases to have a kind

## 12780:00 - 12825:00

of scalable version of it that would be

## 12825:00 - 12875:00

you know important. And so um I worked

## 12875:00 - 12905:00

on that database for a while but in the

## 12905:00 - 12940:00

end it was um you know it became not

## 12940:00 - 12985:00

that unique. there was, you know, 20

## 12985:00 - 13015:00

other systems that were doing it and

## 13015:00 - 13050:00

they all had different uh aspects of

## 13050:00 - 13105:00

popularity and um you know so and then

## 13105:00 - 13135:00

my scope inside of LinkedIn had grown

## 13135:00 - 13160:00

and I there was a couple different teams

## 13160:00 - 13190:00

that I owned including some of the

## 13190:00 - 13235:00

analytics areas and uh some of the

## 13235:00 - 13265:00

product areas

## 13265:00 - 13310:00

and so I was looking for well what you

## 13310:00 - 13330:00

know what what are the other problems

## 13330:00 - 13365:00

that aren't solved you know if there's a

## 13365:00 - 13400:00

hundred of these key value stores what

## 13400:00 - 13430:00

you know what's unique that nobody else

## 13430:00 - 13480:00

is thinking about and I felt like hey

## 13480:00 - 13525:00

you know it really is about the the flow

## 13525:00 - 13560:00

of data and so when you went and built

## 13560:00 - 13595:00

the first version of the product it was

## 13595:00 - 13635:00

the customer was just LinkedIn

## 13635:00 - 13665:00

and like what was the first version of

## 13665:00 - 13695:00

the product yeah it was I it was just a

## 13695:00 - 13730:00

very early it was not radically

## 13730:00 - 13765:00

different you know in terms of what it

## 13765:00 - 13800:00

did from what the technology is now it

## 13800:00 - 13835:00

was not nearly as scalable or mature

## 13835:00 - 13875:00

didn't have all the features but um yeah

## 13875:00 - 13900:00

it was it was kind of an early sketch of

## 13900:00 - 13940:00

that you know that was built in part as

## 13940:00 - 14000:00

kind of a side project. And then you

## 14000:00 - 14050:00

know the goal for this was to replace a

## 14050:00 - 14105:00

lot of these ad hoc pipelines that had

## 14105:00 - 14145:00

been built up internally which turned

## 14145:00 - 14215:00

out to be extremely uh controversial

## 14215:00 - 14245:00

and political project internally.

## 14245:00 - 14260:00

>> Why?

## 14260:00 - 14285:00

>> Well, you know, uh it's a funny thing

## 14285:00 - 14305:00

about how these engineering

## 14305:00 - 14345:00

organizations work. There's somebody who

## 14345:00 - 14375:00

owns each of these things and their

## 14375:00 - 14405:00

team's job is that thing, right? And so

## 14405:00 - 14425:00

if you come in with something that's

## 14425:00 - 14445:00

going to replace a bunch of those,

## 14445:00 - 14465:00

they're like, "Oh, no, we don't want

## 14465:00 - 14515:00

it." And you know, so some of the use

## 14515:00 - 14545:00

cases I own, so we just rolled it out

## 14545:00 - 14590:00

for that. Some of the use cases other

## 14590:00 - 14635:00

people in the organization owned and we

## 14635:00 - 14660:00

spent nine months talking about it.

## 14660:00 - 14680:00

>> And when you rolled it out for the stuff

## 14680:00 - 14705:00

that you kind of could just rip and

## 14705:00 - 14745:00

replace, was it in did it click for you?

## 14745:00 - 14790:00

This is hugely powerful. You know, is uh

## 14790:00 - 14815:00

you know, it was originally just me who

## 14815:00 - 14845:00

worked on this and then we added pretty

## 14845:00 - 14885:00

quickly some other really strong

## 14885:00 - 14920:00

engineers, two two of whom uh became my

## 14920:00 - 14965:00

co-founders at Confluent, June and and

## 14965:00 - 15005:00

Nha. And yeah, you know, I think we got

## 15005:00 - 15060:00

increasingly excited about it. Um, in

## 15060:00 - 15095:00

the, you know, you can kind of, you

## 15095:00 - 15135:00

know, you're on to a big problem when

## 15135:00 - 15205:00

the number of use cases just keeps get,

## 15205:00 - 15230:00

you know, going up by like an order of

## 15230:00 - 15265:00

magnitude that kind of pop out and where

## 15265:00 - 15295:00

the problem you're solving seems really

## 15295:00 - 15335:00

fundamental. And so, you know, kind of

## 15335:00 - 15380:00

seeing that internally, we felt like it

## 15380:00 - 15410:00

was a really big thing. You know, the

## 15410:00 - 15440:00

goal was to really unlock a lot of the

## 15440:00 - 15480:00

use of data. I think it definitely did

## 15480:00 - 15535:00

that internally. And so and you know

## 15535:00 - 15580:00

that kind of led up to the open- source

## 15580:00 - 15610:00

release and and trying to take it out to

## 15610:00 - 15655:00

other companies as well. And so what was

## 15655:00 - 15700:00

the it was a very small group of

## 15700:00 - 15725:00

software engineers working on this early

## 15725:00 - 15795:00

version? What did it feel like?

## 15795:00 - 15825:00

Was it like just you know you were

## 15825:00 - 15850:00

earlier in your career working on cool

## 15850:00 - 15885:00

technology? This is interest like what

## 15885:00 - 15910:00

was like the energy of the team? I I

## 15910:00 - 15945:00

think it was a um yeah it was a high

## 15945:00 - 15990:00

energy group. It was very small. Um I

## 15990:00 - 16010:00

think for most of the time we probably

## 16010:00 - 16045:00

had three to five people. It was not

## 16045:00 - 16090:00

some massive team. You know I think you

## 16090:00 - 16115:00

know we were very passionate about the

## 16115:00 - 16150:00

thing we were doing. Um you know I think

## 16150:00 - 16190:00

the open source part helped that once it

## 16190:00 - 16215:00

well you know once it's a thing then you

## 16215:00 - 16240:00

maybe the team believes in it more than

## 16240:00 - 16285:00

they would just some internal technology

## 16285:00 - 16325:00

layer. And you know I think it ramped up

## 16325:00 - 16365:00

as you know the the story of open

## 16365:00 - 16400:00

sourcing it was interesting. So we we

## 16400:00 - 16425:00

were very excited about this cuz we're

## 16425:00 - 16450:00

already using it internally. We released

## 16450:00 - 16505:00

>> and it was not just your team's uh use

## 16505:00 - 16535:00

cases. It now started to spread.

## 16535:00 - 16550:00

>> That's right. That's right. So it was

## 16550:00 - 16620:00

broadly used um internally and so we we

## 16620:00 - 16645:00

released it as open source. We assumed

## 16645:00 - 16675:00

it would be you know immediately very

## 16675:00 - 16710:00

popular. And but how did you decide that

## 16710:00 - 16725:00

was the right time?

## 16725:00 - 16750:00

>> Just it was it was far enough along.

## 16750:00 - 16780:00

Yeah. It worked. We you know we were

## 16780:00 - 16830:00

using it in production. Um

## 16830:00 - 16855:00

>> and you know interestingly it was kind

## 16855:00 - 16885:00

of the opposite. So we we'd had success

## 16885:00 - 16910:00

with some of these other open source

## 16910:00 - 16950:00

projects. You know, we we released this

## 16950:00 - 16990:00

thinking it was really the best thing

## 16990:00 - 17035:00

that we' done and uh you know, just

## 17035:00 - 17070:00

nobody had any idea what it was.

## 17070:00 - 17080:00

>> Really?

## 17080:00 - 17120:00

>> Yeah. Yeah. Yeah. Well, you know, it was

## 17120:00 - 17140:00

um and it was very different than the

## 17140:00 - 17165:00

first big open source release.

## 17165:00 - 17200:00

>> Yeah. Yeah. So, so when we done the

## 17200:00 - 17220:00

database before, it was very easy to

## 17220:00 - 17245:00

explain what it was. It was a database.

## 17245:00 - 17270:00

People knew about databases. So, this

## 17270:00 - 17300:00

was like, hey, it's a database. It has

## 17300:00 - 17330:00

less features than your other databases,

## 17330:00 - 17360:00

but it's more scalable. So it was just

## 17360:00 - 17400:00

very easy to explain what is it where

## 17400:00 - 17445:00

does it fit what do you use it for and

## 17445:00 - 17495:00

then Kafka this open source project um

## 17495:00 - 17525:00

was very difficult to explain you know

## 17525:00 - 17555:00

it was like well long explanation it's

## 17555:00 - 17605:00

about real-time data it's for this and

## 17605:00 - 17645:00

um you know it actually took a while you

## 17645:00 - 17680:00

know probably the first

## 17680:00 - 17735:00

year it mostly sat on the shelf as a

## 17735:00 - 17770:00

open source project which we were quite

## 17770:00 - 17800:00

uh disappointed about then

## 17800:00 - 17825:00

>> we really were you aggressively working

## 17825:00 - 17855:00

on it internally Yeah. Yeah. Yeah. Yeah.

## 17855:00 - 17905:00

So, internally heavily used, externally

## 17905:00 - 17980:00

by no means particularly popular. And

## 17980:00 - 18020:00

And did you feel

## 18020:00 - 18045:00

Well, you said you felt surprised, but

## 18045:00 - 18085:00

do you did you feel like demotivated or

## 18085:00 - 18105:00

did you feel like I don't know why it's

## 18105:00 - 18115:00

not catching?

## 18115:00 - 18145:00

>> Yeah, somewhat somewhat. you know, I

## 18145:00 - 18180:00

think we were um you know, we had the

## 18180:00 - 18210:00

courage of our convictions because I

## 18210:00 - 18250:00

think we were using this internally and

## 18250:00 - 18300:00

so we'd kind of seen it work and so we

## 18300:00 - 18345:00

put more energy into kind of getting it

## 18345:00 - 18415:00

adopted and um you know eventually

## 18415:00 - 18450:00

started to think about okay how you know

## 18450:00 - 18475:00

how could you get people very excited

## 18475:00 - 18535:00

about this area and um and so I I ended

## 18535:00 - 18570:00

up writing a very long blog post about

## 18570:00 - 18630:00

it that really kind of caught on and I

## 18630:00 - 18645:00

Why?

## 18645:00 - 18690:00

>> Um we I I think I put a lot of energy

## 18690:00 - 18710:00

into it cuz I was like, "Hey, you know,

## 18710:00 - 18765:00

if we you know, if you ultimately if if

## 18765:00 - 18810:00

we can't express why this is exciting,

## 18810:00 - 18870:00

then you know, I think it's probably not

## 18870:00 - 18905:00

going to be that successful of an open

## 18905:00 - 18950:00

source project." And um I think the blog

## 18950:00 - 19000:00

post was kind of unusual in its form. It

## 19000:00 - 19045:00

was like probably I think it was like 25

## 19045:00 - 19110:00

pages long or something and had

## 19110:00 - 19145:00

weird pictures and you know it was just

## 19145:00 - 19175:00

it was kind of entertaining but also

## 19175:00 - 19210:00

computer sciency and then also talked

## 19210:00 - 19245:00

about some of the applications of this

## 19245:00 - 19270:00

kind of more real-time way of thinking

## 19270:00 - 19310:00

about data and so I think it was enough

## 19310:00 - 19340:00

of a new way of thinking that people

## 19340:00 - 19395:00

were um you know were intrigued and I

## 19395:00 - 19420:00

think that really helped the technology

## 19420:00 - 19450:00

kind of catch on in Silicon Valley and

## 19450:00 - 19505:00

eventually beyond. But so before you put

## 19505:00 - 19540:00

that out and after you put it out and it

## 19540:00 - 19580:00

started to gain momentum, the product

## 19580:00 - 19620:00

did not change. So it it was really your

## 19620:00 - 19645:00

theory was it's a positioning and

## 19645:00 - 19685:00

basically market of course continued to

## 19685:00 - 19700:00

evolve better and better.

## 19700:00 - 19725:00

>> You know, it continued to evolve, but it

## 19725:00 - 19765:00

was effectively the same idea. So yeah,

## 19765:00 - 19800:00

it was you know what was it that it took

## 19800:00 - 19845:00

us probably several years to discover

## 19845:00 - 19910:00

was basically product marketing

## 19910:00 - 19945:00

you know in an open source context was

## 19945:00 - 19985:00

yeah you got to tell people why it's

## 19985:00 - 20025:00

interesting. So maybe building on this

## 20025:00 - 20055:00

just a little bit, if you had another

## 20055:00 - 20085:00

software engineer who built a really

## 20085:00 - 20130:00

interesting product and is trying to

## 20130:00 - 20185:00

figure out how to do product marketing

## 20185:00 - 20235:00

or explain it to a more technical

## 20235:00 - 20275:00

audience like what would you teach them

## 20275:00 - 20310:00

or explain to them they should try to

## 20310:00 - 20365:00

do? It's interesting in this area that

## 20365:00 - 20395:00

Confluent operates in, which is, you

## 20395:00 - 20435:00

know, this kind of very technical

## 20435:00 - 20490:00

uh software products. You know, it is

## 20490:00 - 20530:00

often the case that when you see early

## 20530:00 - 20590:00

companies that have quick success, I

## 20590:00 - 20625:00

would say one of the defining things is

## 20625:00 - 20655:00

often that the founders are very good at

## 20655:00 - 20680:00

that kind of communication, you know, to

## 20680:00 - 20725:00

a surprising degree. And so, yeah, what

## 20725:00 - 20750:00

what did I learn about doing that over

## 20750:00 - 20790:00

the years? um you know first of all just

## 20790:00 - 20840:00

that it matters a lot and is hard right

## 20840:00 - 20870:00

so like you you know we would think

## 20870:00 - 20915:00

about uh you know solving some computer

## 20915:00 - 20960:00

science problem as being very hard you

## 20960:00 - 20980:00

know if you're have a software

## 20980:00 - 21005:00

engineering background you don't think

## 21005:00 - 21045:00

of product marketing as being hard or

## 21045:00 - 21080:00

maybe you think it's hard but you don't

## 21080:00 - 21110:00

um know how to engage in a hard thing

## 21110:00 - 21150:00

like that you think okay maybe you know

## 21150:00 - 21170:00

some people are good at that some people

## 21170:00 - 21205:00

are not good at that but in fact I feel

## 21205:00 - 21245:00

like a lot of marketing it just takes a

## 21245:00 - 21265:00

lot of thinking

## 21265:00 - 21295:00

So like the amount of time you're going

## 21295:00 - 21345:00

to think about how to convey the thing

## 21345:00 - 21395:00

is just much higher, you know, than you

## 21395:00 - 21440:00

would expect. And you know, the level of

## 21440:00 - 21465:00

detail you're going to put into how you

## 21465:00 - 21500:00

do that is just much higher than you

## 21500:00 - 21535:00

would expect. And so, you know, that

## 21535:00 - 21570:00

that was one of the first takeaways. You

## 21570:00 - 21610:00

know, the second takeaway,

## 21610:00 - 21630:00

uh, you know, this is all kind of like

## 21630:00 - 21670:00

marketing 101, but it's true is, you

## 21670:00 - 21710:00

know, marketing messages are ultimately

## 21710:00 - 21755:00

kind of a, you know, they're kind of a

## 21755:00 - 21800:00

pyramid, I think, where, you know, at

## 21800:00 - 21850:00

the top of the pyramid there's some, you

## 21850:00 - 21880:00

know, gestalt message. It's like, what's

## 21880:00 - 21915:00

the title? What's the slogan of the blog

## 21915:00 - 21955:00

post, you know, but it's not enough to

## 21955:00 - 21990:00

just have that. And people often think

## 21990:00 - 22015:00

of marketing as just being that. It's

## 22015:00 - 22040:00

oh, it's some slogan that we slap on it

## 22040:00 - 22085:00

or it's some whatever, you know, which

## 22085:00 - 22115:00

which is actually totally wrong. You

## 22115:00 - 22150:00

need the rest of the pyramid. So what

## 22150:00 - 22190:00

supports it is all the evidence, right?

## 22190:00 - 22230:00

It has to be the the people using it who

## 22230:00 - 22260:00

are doing that thing, the truth of the

## 22260:00 - 22300:00

the long form argument for what you're

## 22300:00 - 22335:00

saying. You know, the slogan kind of

## 22335:00 - 22370:00

sits on top of that. And when you see

## 22370:00 - 22405:00

things that don't work, it's usually

## 22405:00 - 22430:00

because they're either missing the top

## 22430:00 - 22465:00

of the pyramid. like there's lots of

## 22465:00 - 22490:00

examples but they can't boil down to

## 22490:00 - 22540:00

what it is or it's the opposite like

## 22540:00 - 22570:00

they have some slogan but it is not

## 22570:00 - 22620:00

supported in the broad set of facts that

## 22620:00 - 22655:00

would be the rest of the pyramid and so

## 22655:00 - 22680:00

I I always think about these things as

## 22680:00 - 22725:00

just kind of construct that full pyramid

## 22725:00 - 22755:00

the top or the bottom first

## 22755:00 - 22805:00

>> bottom I think the top has to come later

## 22805:00 - 22845:00

because um well not I don't know about

## 22845:00 - 22875:00

later but you know it's a distilled

## 22875:00 - 22920:00

version of what you think so your first

## 22920:00 - 22965:00

version of this will not be the piffy

## 22965:00 - 23000:00

oneline statement, right? It takes a

## 23000:00 - 23060:00

while to get to really understand how to

## 23060:00 - 23105:00

boil it down in a way that actually, you

## 23105:00 - 23150:00

know, you you're never in a short

## 23150:00 - 23205:00

statement going to convey, you know, a

## 23205:00 - 23260:00

very deep truth except by reference to a

## 23260:00 - 23285:00

larger set of things, right? So, you

## 23285:00 - 23310:00

have to kind of almost build the body of

## 23310:00 - 23350:00

work before you can boil it down. But,

## 23350:00 - 23385:00

but you kind of do both together, I

## 23385:00 - 23455:00

guess. What's the best example of this

## 23455:00 - 23490:00

from all the years building Confluent?

## 23490:00 - 23535:00

One example for us was, you know, as we

## 23535:00 - 23575:00

were preparing to go public, one thing

## 23575:00 - 23605:00

you have to do is explain your company

## 23605:00 - 23655:00

to investors. In a different class of

## 23655:00 - 23680:00

investors than venture capitalists.

## 23680:00 - 23705:00

Venture capitalists usually are a little

## 23705:00 - 23730:00

more specialized in tech, will do a

## 23730:00 - 23770:00

little bit more research. Um, you know,

## 23770:00 - 23820:00

so kind of public market investors just

## 23820:00 - 23860:00

by nature they there's fewer public

## 23860:00 - 23895:00

companies, right? And so they have to

## 23895:00 - 23925:00

generally make their money across a

## 23925:00 - 23955:00

broader set of things. And so they're

## 23955:00 - 23980:00

going to be less specialized in your

## 23980:00 - 24035:00

area. And especially as you're, you

## 24035:00 - 24060:00

know, new and coming out, you got to

## 24060:00 - 24090:00

really kind of boil it down. And so I I

## 24090:00 - 24120:00

do I thought that was a good exercise

## 24120:00 - 24160:00

for us, you know, h how did that

## 24160:00 - 24190:00

exercise go? It was like, well, what

## 24190:00 - 24230:00

what do these people understand today?

## 24230:00 - 24255:00

You know, what is the frame of reference

## 24255:00 - 24320:00

that they have? How can we uh connect

## 24320:00 - 24390:00

ourselves to that um in a way that uh

## 24390:00 - 24420:00

helps them understand the opportunity

## 24420:00 - 24450:00

for the company, why it's a big deal,

## 24450:00 - 24470:00

you know, why it's a strategic

## 24470:00 - 24515:00

technology. And so we put a lot of

## 24515:00 - 24555:00

effort into that. You know, what we came

## 24555:00 - 24595:00

away with is like, okay, these people

## 24595:00 - 24630:00

understand databases because there's

## 24630:00 - 24660:00

been a lot of successful database

## 24660:00 - 24690:00

companies. So if you want to explain

## 24690:00 - 24730:00

what you do, don't do it from first

## 24730:00 - 24760:00

principles. just say how are you

## 24760:00 - 24790:00

different from a database

## 24790:00 - 24805:00

>> and similar I guess.

## 24805:00 - 24840:00

>> Yeah. Yeah. And so our approach to that

## 24840:00 - 24880:00

was uh for the IPO was very much like

## 24880:00 - 24945:00

okay databases data at rest but now all

## 24945:00 - 24970:00

the parts of the company are connected

## 24970:00 - 24995:00

there's going to be an equally important

## 24995:00 - 25040:00

problem of data in motion right and so

## 25040:00 - 25070:00

you know the goal was to convey hey

## 25070:00 - 25115:00

these two things are related everything

## 25115:00 - 25160:00

that's at rest has to also be in motion

## 25160:00 - 25200:00

so the opportunity could be equally big

## 25200:00 - 25240:00

you know it's caused by the parts of the

## 25240:00 - 25265:00

company all having to talk to each other

## 25265:00 - 25290:00

in software which probably wasn't the

## 25290:00 - 25350:00

case you originally and you know that

## 25350:00 - 25410:00

kind of implies a large TAM you know not

## 25410:00 - 25440:00

in terms of detailed analysis but just

## 25440:00 - 25470:00

in terms of you know you're comparing to

## 25470:00 - 25520:00

something big and it gives an anchor for

## 25520:00 - 25550:00

what the technology is and where the

## 25550:00 - 25605:00

company sits. we're not a operational

## 25605:00 - 25635:00

tool or something like that, you know,

## 25635:00 - 25675:00

and a a remarkable amount of thought

## 25675:00 - 25720:00

went into something that is kind of

## 25720:00 - 25750:00

small, but it's actually very important

## 25750:00 - 25770:00

if you're going to kind of come out to a

## 25770:00 - 25800:00

new audience. And so, I think audience

## 25800:00 - 25840:00

by audience, you have to almost work

## 25840:00 - 25865:00

through that. You know, the companies

## 25865:00 - 25915:00

that are often the punchiest and best

## 25915:00 - 25940:00

are very early companies where there's

## 25940:00 - 25965:00

typically just one audience, which is

## 25965:00 - 26025:00

like the user. Um and then over time you

## 26025:00 - 26060:00

may have a whole set of you know if

## 26060:00 - 26080:00

you're selling for more money you'll

## 26080:00 - 26115:00

have a whole constituency

## 26115:00 - 26135:00

buyer

## 26135:00 - 26175:00

>> you know the you'll have your internal

## 26175:00 - 26200:00

employees which are now a large enough

## 26200:00 - 26220:00

group that you need to think about you

## 26220:00 - 26255:00

have investors you and usually as

## 26255:00 - 26300:00

companies as time goes by as a result of

## 26300:00 - 26330:00

that many things become more watered

## 26330:00 - 26345:00

down because you're trying to say

## 26345:00 - 26380:00

something to a bunch of people who have

## 26380:00 - 26405:00

very different context and you notice

## 26405:00 - 26435:00

this that companies kind of lose the

## 26435:00 - 26465:00

edge in communication as they get bigger

## 26465:00 - 26490:00

and it's it's almost inherent because

## 26490:00 - 26530:00

you just have to talk to more people.

## 26530:00 - 26570:00

>> Winding the clock back, you have this

## 26570:00 - 26600:00

magnumopus blog post.

## 26600:00 - 26610:00

>> Yeah.

## 26610:00 - 26635:00

>> And so then what happens after the next

## 26635:00 - 26670:00

few months? Did it like instantly click

## 26670:00 - 26710:00

hacker news kind of?

## 26710:00 - 26745:00

>> People were very excited about the blog

## 26745:00 - 26780:00

post that definitely helped the kind of

## 26780:00 - 26815:00

spread of the technology. I you know I

## 26815:00 - 26855:00

we went and did talks as well in some of

## 26855:00 - 26910:00

the tech companies and you know it

## 26910:00 - 26960:00

really did start to catch on. you know,

## 26960:00 - 26985:00

people were, I would say, passionately

## 26985:00 - 27045:00

excited about the idea. It um matched

## 27045:00 - 27075:00

problems that they had that were top of-

## 27075:00 - 27125:00

mind and, you know, that that was kind

## 27125:00 - 27165:00

of what led to, you know, starting to

## 27165:00 - 27195:00

think about, you know, turning it into a

## 27195:00 - 27250:00

company. Was the was the usage of the

## 27250:00 - 27275:00

open source product did it look like an

## 27275:00 - 27300:00

exponential after that

## 27300:00 - 27325:00

>> or was kind of like

## 27325:00 - 27360:00

>> yeah we had no real measurement you know

## 27360:00 - 27400:00

there um you know we did we didn't have

## 27400:00 - 27420:00

any kind of detailed tracking or

## 27420:00 - 27450:00

anything like that but certainly just in

## 27450:00 - 27485:00

who we would hear from and the types of

## 27485:00 - 27515:00

companies that were adopting it. You

## 27515:00 - 27570:00

know that that looked like a pretty nice

## 27570:00 - 27625:00

growth curve. It was never um you know

## 27625:00 - 27660:00

this type of technology is some work to

## 27660:00 - 27695:00

adopt. So it was never just kind of

## 27695:00 - 27730:00

rocket to the moon. And that's been true

## 27730:00 - 27765:00

through the whole um life of the

## 27765:00 - 27805:00

company. It's been the open source has

## 27805:00 - 27855:00

kind of grown steadily, you know, kind

## 27855:00 - 27900:00

of a line going up for that whole time

## 27900:00 - 27930:00

period, but but it wasn't like, you

## 27930:00 - 27970:00

know, went from zero to infinity

## 27970:00 - 27990:00

overnight.

## 27990:00 - 28020:00

>> What did it feel like as you were

## 28020:00 - 28035:00

thinking about do we want to start a

## 28035:00 - 28070:00

company around this? You know, I think

## 28070:00 - 28120:00

actually my co-founder brought it up,

## 28120:00 - 28165:00

but I'd had kind of a very similar idea.

## 28165:00 - 28195:00

And so I think to some extent we were

## 28195:00 - 28235:00

kind of thinking in that way and I think

## 28235:00 - 28295:00

it came about sort of naturally in that,

## 28295:00 - 28325:00

you know, we were hearing from companies

## 28325:00 - 28360:00

that were well outside of tech all of a

## 28360:00 - 28410:00

sudden. So you know, media companies and

## 28410:00 - 28460:00

banks and uh you know, that that kind of

## 28460:00 - 28495:00

helped us understand, okay, what do they

## 28495:00 - 28520:00

have the same problem? And it turned out

## 28520:00 - 28560:00

yeah they have the same problem but you

## 28560:00 - 28610:00

know maybe bigger in some ways. And so

## 28610:00 - 28650:00

we felt like okay this could be very

## 28650:00 - 28680:00

applic you know this could be applicable

## 28680:00 - 28725:00

broadly and you know then it was just

## 28725:00 - 28770:00

hey is there a form of company that

## 28770:00 - 28800:00

would fit this you know effectively what

## 28800:00 - 28860:00

we had was an open source project. Now,

## 28860:00 - 28880:00

you know, there's more of a pattern for

## 28880:00 - 28905:00

how this works. But at that time, I

## 28905:00 - 28940:00

think companies around open source were

## 28940:00 - 28980:00

seen as kind of not very successful.

## 28980:00 - 29005:00

There had been and a lot of people had

## 29005:00 - 29020:00

tried it at that point.

## 29020:00 - 29045:00

>> Yeah. There had been Red Hat and that

## 29045:00 - 29090:00

worked and there um you know there had

## 29090:00 - 29140:00

been some companies around Hadoop that

## 29140:00 - 29170:00

kind of struggled. You know, it just was

## 29170:00 - 29230:00

not seen as like a great uh paradigm.

## 29230:00 - 29275:00

Even in the early 2010s, developer tools

## 29275:00 - 29305:00

in general, I think, were a much more

## 29305:00 - 29355:00

skeptical category. just broadly. Yeah.

## 29355:00 - 29410:00

So people were yeah not that excited

## 29410:00 - 29465:00

about the whole space and that obviously

## 29465:00 - 29490:00

made it more challenging for us coming

## 29490:00 - 29520:00

in we kind of understood okay this is

## 29520:00 - 29580:00

not not exactly a hot area you know and

## 29580:00 - 29625:00

I would say even in the crowd we were in

## 29625:00 - 29685:00

probably enterprise generally was not

## 29685:00 - 29720:00

necessarily the thing you know we had we

## 29720:00 - 29740:00

kind of come out of a social network and

## 29740:00 - 29770:00

that had been the you know the big

## 29770:00 - 29790:00

marquee companies of the day were

## 29790:00 - 29820:00

definitely those you know it was Google

## 29820:00 - 29875:00

and Facebook and so on wasn't uh you

## 29875:00 - 29910:00

know wasn't whatever the equivalent

## 29910:00 - 29960:00

enterprise thing was and this is 2014 so

## 29960:00 - 29985:00

it was you know kind of right at the

## 29985:00 - 30020:00

rise of a lot of the SAS stuff but that

## 30020:00 - 30050:00

was that had not kind of broken through

## 30050:00 - 30095:00

at that point and so so yeah we were

## 30095:00 - 30125:00

like well you know this is a really good

## 30125:00 - 30160:00

idea this is a really good technological

## 30160:00 - 30230:00

idea that doesn't have a really easy

## 30230:00 - 30260:00

company form and is hard

## 30260:00 - 30290:00

>> but you thought a lot about that

## 30290:00 - 30310:00

>> we thought a lot about it so we were

## 30310:00 - 30330:00

like well what are we going to do maybe

## 30330:00 - 30370:00

we package this up into some kind of

## 30370:00 - 30410:00

vertical solution or something, but that

## 30410:00 - 30450:00

didn't really make any sense. And then,

## 30450:00 - 30470:00

you know, eventually we were like, look,

## 30470:00 - 30500:00

we should just, you know, just take a

## 30500:00 - 30525:00

product to market around this. Just do

## 30525:00 - 30545:00

the obvious thing, like build this into

## 30545:00 - 30580:00

a product and take it out to people. In

## 30580:00 - 30625:00

2014, that was just where it started to

## 30625:00 - 30680:00

be clear that the, you know, the cloud

## 30680:00 - 30725:00

was going to be a big thing, right? But

## 30725:00 - 30780:00

at that point everybody believed it was

## 30780:00 - 30825:00

just really AWS like there was not going

## 30825:00 - 30855:00

to be any other companies. So it was,

## 30855:00 - 30880:00

you know, it was a really interesting

## 30880:00 - 30900:00

dilemma of how you would try and

## 30900:00 - 30920:00

construct a company because you have

## 30920:00 - 30955:00

this cloud thing that's happening that's

## 30955:00 - 31010:00

maybe I don't know what five seven% of

## 31010:00 - 31035:00

IT spend or something some small

## 31035:00 - 31085:00

percentage it's really just Amazon you

## 31085:00 - 31110:00

know it's unclear that anybody can live

## 31110:00 - 31160:00

in that ecosystem around it the kind of

## 31160:00 - 31200:00

open- source on premise companies have

## 31200:00 - 31230:00

not done that well so that was the

## 31230:00 - 31275:00

dilemma coming into it was like okay can

## 31275:00 - 31320:00

you you know and we're a category that

## 31320:00 - 31375:00

doesn't exist and nobody has heard

## 31375:00 - 31425:00

So can you get something going in that

## 31425:00 - 31485:00

dynamic? Uh and if so, how? You know, I

## 31485:00 - 31510:00

think um that that was kind of the

## 31510:00 - 31545:00

challenge. Now being software engineers,

## 31545:00 - 31565:00

I think we dramatically overthought

## 31565:00 - 31585:00

this. Yeah, we spent probably nine

## 31585:00 - 31615:00

months thinking about how to do it. Was

## 31615:00 - 31670:00

it mainly inside with you all talking

## 31670:00 - 31715:00

amongst yourself or were you getting out

## 31715:00 - 31740:00

and understanding customers and

## 31740:00 - 31775:00

understanding like what was the mix of

## 31775:00 - 31785:00

the nine months?

## 31785:00 - 31820:00

>> Meet Yeah, we did go meet. Most of it

## 31820:00 - 31850:00

was us theorizing which was probably not

## 31850:00 - 31890:00

that useful. Um since in the end we just

## 31890:00 - 31920:00

did the obvious thing. We did go meet

## 31920:00 - 31945:00

with a bunch of the users of the

## 31945:00 - 31985:00

technology and just be like hey you know

## 31985:00 - 32015:00

is this important to you? Would you you

## 32015:00 - 32050:00

know what would a product product more

## 32050:00 - 32075:00

of a productized version of it look

## 32075:00 - 32120:00

like? Would you pay for that? And that

## 32120:00 - 32155:00

you know that was pretty enthusiastic.

## 32155:00 - 32180:00

The you know people were passionate

## 32180:00 - 32205:00

about the technology. So of course they

## 32205:00 - 32240:00

all tell you yes even though maybe they

## 32240:00 - 32270:00

will or won't be customers later on. You

## 32270:00 - 32315:00

know, I think that combined with the

## 32315:00 - 32345:00

impact internally at LinkedIn kind of

## 32345:00 - 32365:00

carried us through. So even though it

## 32365:00 - 32390:00

was like, okay, not the most appealing

## 32390:00 - 32465:00

area, not a really clear product path,

## 32465:00 - 32490:00

we felt like, look, there's like

## 32490:00 - 32510:00

fundamentally there's something very

## 32510:00 - 32560:00

valuable here. We should just do it. And

## 32560:00 - 32585:00

you know, I actually think there's

## 32585:00 - 32645:00

something to that. You know, I I when

## 32645:00 - 32690:00

I've seen people who create companies in

## 32690:00 - 32730:00

kind of a very top- down McKenzie way of

## 32730:00 - 32790:00

thinking of like, okay, market analysis,

## 32790:00 - 32830:00

uh, like in some sense it actually works

## 32830:00 - 32870:00

less well than just like marinating in

## 32870:00 - 32905:00

some problem where you're convinced that

## 32905:00 - 32935:00

there's like a really meaty chunk of

## 32935:00 - 32960:00

value and then even if you don't have

## 32960:00 - 32990:00

the rest of it figured out, like you're

## 32990:00 - 33040:00

kind of in the right spot. And, you

## 33040:00 - 33065:00

know, I think to some extent, you know,

## 33065:00 - 33095:00

I think we we understood that part of

## 33095:00 - 33125:00

it. We were like look this data

## 33125:00 - 33145:00

infrastructure even though it's very

## 33145:00 - 33190:00

uncool is actually really valuable to

## 33190:00 - 33230:00

the you know to companies now and

## 33230:00 - 33250:00

they're going to want this and this

## 33250:00 - 33275:00

problem that we're solving is a really

## 33275:00 - 33315:00

valuable problem. So somehow we will be

## 33315:00 - 33350:00

able to get some of that value even

## 33350:00 - 33395:00

though the M even though prior examples

## 33395:00 - 33445:00

didn't go that well. What was the first

## 33445:00 - 33470:00

version of the product? How did you

## 33470:00 - 33500:00

conceive of it and it happened after you

## 33500:00 - 33525:00

raised capital or before?

## 33525:00 - 33565:00

>> You know it was a it was an interesting

## 33565:00 - 33585:00

kind of occurrence. So the yeah the idea

## 33585:00 - 33610:00

was okay we're going to leave LinkedIn

## 33610:00 - 33655:00

and go figure out the details and put

## 33655:00 - 33680:00

together a company and probably

## 33680:00 - 33725:00

eventually go raise money. When we went

## 33725:00 - 33760:00

to quit LinkedIn was like oh okay well

## 33760:00 - 33795:00

this is you know first of all we don't

## 33795:00 - 33815:00

really want you to leave but if you're

## 33815:00 - 33845:00

going to leave we do think this is

## 33845:00 - 33875:00

really valuable we would be interested

## 33875:00 - 33905:00

in investing and we were like

## 33905:00 - 33925:00

>> off the balance sheet.

## 33925:00 - 33955:00

>> Yeah. Yeah. Which they had not done in

## 33955:00 - 34000:00

the past. So you know we were very

## 34000:00 - 34035:00

unconfident in our ability to raise

## 34035:00 - 34060:00

money. So, we were like, "Okay, this

## 34060:00 - 34090:00

sounds great. We should totally do

## 34090:00 - 34130:00

that." And but they were like, "Well,

## 34130:00 - 34185:00

because we don't do any investing, we

## 34185:00 - 34215:00

kind of need it to be a priced round

## 34215:00 - 34250:00

where somebody else is helping set the

## 34250:00 - 34310:00

price is not just us assessing our own

## 34310:00 - 34335:00

thing."

## 34335:00 - 34385:00

And so, so you should go try and find

## 34385:00 - 34425:00

some VC who will participate as well,

## 34425:00 - 34455:00

right? you know, so we were like, "Okay,

## 34455:00 - 34480:00

we should do this and we should do it

## 34480:00 - 34535:00

before they change their mind because

## 34535:00 - 34565:00

maybe they, you know, maybe this goes

## 34565:00 - 34610:00

away if we let it sit too long." And so,

## 34610:00 - 34640:00

you know, we went from kind of thinking

## 34640:00 - 34675:00

of like, okay, we're going to quit our

## 34675:00 - 34715:00

jobs and we're going to cultivate, you

## 34715:00 - 34740:00

know, figure out our product and build

## 34740:00 - 34775:00

some early version and get some first

## 34775:00 - 34800:00

customers to like, okay, now we're going

## 34800:00 - 34850:00

to go fundra for a company that is not

## 34850:00 - 34885:00

incorporated and doesn't have a name.

## 34885:00 - 34920:00

that actually was probably the right

## 34920:00 - 34970:00

thing to do. Um, and so, you know, that

## 34970:00 - 34990:00

initial fund raise,

## 34990:00 - 35015:00

>> why was it the right thing to do?

## 35015:00 - 35040:00

>> You know, I first of all, I think it

## 35040:00 - 35095:00

helps if there's interest. And for us, I

## 35095:00 - 35140:00

think it helped that the company we were

## 35140:00 - 35180:00

at was interested. I do think with a

## 35180:00 - 35200:00

little bit of homework we would have

## 35200:00 - 35220:00

done a much you know we would have done

## 35220:00 - 35275:00

a better job of you know putting that

## 35275:00 - 35325:00

fund raise together but in practice I

## 35325:00 - 35360:00

think a lot of VCs are used to some of

## 35360:00 - 35390:00

the rough edges and can kind of see they

## 35390:00 - 35415:00

can kind of get past that if there's

## 35415:00 - 35445:00

some traction and something happening in

## 35445:00 - 35480:00

the world and you know if there's

## 35480:00 - 35505:00

interest that always helps.

## 35505:00 - 35540:00

>> Uh so so I think I think it was probably

## 35540:00 - 35555:00

the right thing.

## 35555:00 - 35575:00

>> So then you raised the money with no

## 35575:00 - 35615:00

product no nothing other than the

## 35615:00 - 35630:00

promise of what you were going to do.

## 35630:00 - 35665:00

>> That's right. Yeah. Basically, we had a

## 35665:00 - 35710:00

popular open source thing and some

## 35710:00 - 35745:00

slides of what we would do. And so,

## 35745:00 - 35765:00

yeah, and it went from something where

## 35765:00 - 35785:00

LinkedIn was going to be the kind of

## 35785:00 - 35825:00

major investor to being, you know, a

## 35825:00 - 35850:00

smaller part of the round. And it went

## 35850:00 - 35885:00

from kind of a seed investment to a

## 35885:00 - 35910:00

series A through the course of that

## 35910:00 - 35955:00

fundraising process. But, um, but yeah,

## 35955:00 - 35985:00

was, you know, was ultimately

## 35985:00 - 36010:00

successful. We, you know, benchmark

## 36010:00 - 36030:00

invested. We were really happy to have

## 36030:00 - 36075:00

him. Um, you know, that was, uh, Eric

## 36075:00 - 36110:00

Fisher, who is awesome part of the

## 36110:00 - 36165:00

company from early on. How close was the

## 36165:00 - 36220:00

V1 of the product to kind of what you

## 36220:00 - 36245:00

hashed out on the slides?

## 36245:00 - 36295:00

>> Yeah, it depends on what you call V1.

## 36295:00 - 36355:00

Um, you know, what we had pitched was

## 36355:00 - 36400:00

actually very close to what we built.

## 36400:00 - 36430:00

It's just I said we were going to do it

## 36430:00 - 36475:00

in a year and I think in practice

## 36475:00 - 36505:00

the first thing we launched was much

## 36505:00 - 36540:00

less than that. And to do everything on

## 36540:00 - 36595:00

the slide took like five years. So, and

## 36595:00 - 36630:00

so what was the very first thing you put

## 36630:00 - 36670:00

the kind of founding dilemma for us was

## 36670:00 - 36710:00

you know we had at LinkedIn we had

## 36710:00 - 36750:00

really run this software internally as

## 36750:00 - 36790:00

kind of a service

## 36790:00 - 36825:00

and so the the early dilemma was like

## 36825:00 - 36845:00

hey are we going to release a software

## 36845:00 - 36895:00

product you know that's more applicable

## 36895:00 - 36915:00

people can use it in the cloud they can

## 36915:00 - 36950:00

use it in their data centers cloud is

## 36950:00 - 37005:00

still a small fraction and unproven as a

## 37005:00 - 37040:00

you know business model or are we going

## 37040:00 - 37065:00

to do a cloud product where we feel like

## 37065:00 - 37110:00

hey there's more value we can deliver,

## 37110:00 - 37150:00

you know, and of course anybody you talk

## 37150:00 - 37200:00

to is like in a small early company, do

## 37200:00 - 37235:00

not the the right answer is not both is

## 37235:00 - 37265:00

just pick something. But that was

## 37265:00 - 37290:00

actually not clear at all either, right?

## 37290:00 - 37320:00

Because you know, it's okay, we're this

## 37320:00 - 37380:00

0 billion data streaming market,

## 37380:00 - 37400:00

>> you know, are you really going to slice

## 37400:00 - 37435:00

it in half and be like, oh, we're data

## 37435:00 - 37460:00

streaming for the people who want it in

## 37460:00 - 37500:00

this flavor? Uh, that didn't sound right

## 37500:00 - 37550:00

either. So, you know, pretty early on we

## 37550:00 - 37595:00

were convinced we had to do both. Again,

## 37595:00 - 37620:00

the starting with software was actually

## 37620:00 - 37650:00

just pure expediency. It's easier to get

## 37650:00 - 37680:00

a first version out and that would

## 37680:00 - 37725:00

satisfy more of the market. And so, we

## 37725:00 - 37765:00

started with that, you know, and then I

## 37765:00 - 37830:00

felt a lot of angst about the the cloud

## 37830:00 - 37880:00

offering. And you know at that time at

## 37880:00 - 37920:00

you know as we launched Amazon had a a

## 37920:00 - 37965:00

system that was actually built in I I

## 37965:00 - 38010:00

believe imitation of Kafka called

## 38010:00 - 38045:00

Kinesis. So it was incompatible but kind

## 38045:00 - 38095:00

of looked roughly like it and that was

## 38095:00 - 38125:00

popular and we were like oh man that's

## 38125:00 - 38150:00

going to take the opportunity and if it

## 38150:00 - 38190:00

doesn't they'll build something around

## 38190:00 - 38240:00

the open source which they did. So you

## 38240:00 - 38275:00

know so we felt a lot of angst of okay

## 38275:00 - 38300:00

we've got to get this managed service

## 38300:00 - 38330:00

done but it's very hard because we're

## 38330:00 - 38360:00

you know where this very small

## 38360:00 - 38400:00

engineering team we've just built this

## 38400:00 - 38425:00

software product that doesn't have

## 38425:00 - 38460:00

nearly enough features. We've taken that

## 38460:00 - 38500:00

out to, you know, very large enterprises

## 38500:00 - 38540:00

that we have no business working with

## 38540:00 - 38580:00

successfully for more money than we feel

## 38580:00 - 38610:00

at all comfortable with. And then we're

## 38610:00 - 38645:00

like gonna somehow pull resources away

## 38645:00 - 38685:00

from that, build this managed service,

## 38685:00 - 38720:00

which is a very big undertaking, and try

## 38720:00 - 38770:00

and get that working. And you know, we

## 38770:00 - 38805:00

did start that pretty early in the life

## 38805:00 - 38850:00

of the company. Um, you know, I think I

## 38850:00 - 38870:00

don't know when we started working out,

## 38870:00 - 38915:00

maybe we were a year and a half in

## 38915:00 - 38945:00

something like that. Um, and then it

## 38945:00 - 38995:00

took, you know, over a year, I think, to

## 38995:00 - 39020:00

really get a first version of the cloud

## 39020:00 - 39060:00

offering out there. But when you built

## 39060:00 - 39115:00

and shipped the software and you started

## 39115:00 - 39170:00

selling it, did it feel like

## 39170:00 - 39210:00

there's a there there we have real pull.

## 39210:00 - 39240:00

People wanted it, people wanted to pay

## 39240:00 - 39270:00

for it. Like what what what was the

## 39270:00 - 39305:00

feeling inside of the company?

## 39305:00 - 39345:00

>> So, it was it was good. I actually

## 39345:00 - 39390:00

didn't know enough, you know, nothing.

## 39390:00 - 39420:00

it to me I always felt like it didn't

## 39420:00 - 39445:00

seem big enough like we didn't have

## 39445:00 - 39475:00

enough customers

## 39475:00 - 39510:00

um you know the dollar amounts didn't

## 39510:00 - 39530:00

seem big enough but they were actually

## 39530:00 - 39555:00

very good for an early enterprise

## 39555:00 - 39600:00

company I just had no reference to what

## 39600:00 - 39655:00

it ought to look like um and so yeah

## 39655:00 - 39700:00

very quickly we were getting lots of

## 39700:00 - 39750:00

100k plus deals you know coming in but

## 39750:00 - 39785:00

to me it didn't feel like a lot it would

## 39785:00 - 39835:00

be like oh we got four deals this

## 39835:00 - 39850:00

quarter but it was still it was pretty

## 39850:00 - 39880:00

good for like a company that was a few

## 39880:00 - 39925:00

quarters selling. So, so it it moved

## 39925:00 - 39965:00

pretty quickly. The angst was like, hey,

## 39965:00 - 39995:00

we, you know, we have this popular open

## 39995:00 - 40010:00

source with a little bit of

## 40010:00 - 40045:00

functionality around it. We have which

## 40045:00 - 40085:00

we haven't filled out and so we don't,

## 40085:00 - 40130:00

you know, are we justifying the value

## 40130:00 - 40175:00

that we're charging or does the bottom

## 40175:00 - 40205:00

fall out because we just don't have

## 40205:00 - 40265:00

enough kind of meat in the the sandwich,

## 40265:00 - 40325:00

right? And um so that was very much the

## 40325:00 - 40355:00

competing tension on the product side

## 40355:00 - 40395:00

was okay we have this one product which

## 40395:00 - 40455:00

has traction. People want it. We're

## 40455:00 - 40495:00

landing big customers but there's not

## 40495:00 - 40525:00

you know it's 10% of what it ought to

## 40525:00 - 40585:00

be. And then uh and in terms of the role

## 40585:00 - 40615:00

we wanted we wanted to increase that

## 40615:00 - 40640:00

scope. And so we were kind of building

## 40640:00 - 40675:00

things to do that. And then there's this

## 40675:00 - 40710:00

whole other delivery mechanism which is

## 40710:00 - 40755:00

kind of a top tobottom rewrite which

## 40755:00 - 40785:00

really serves a different set of

## 40785:00 - 40810:00

customers and people who are more cloud

## 40810:00 - 40850:00

native etc which we also have to

## 40850:00 - 40875:00

>> and the people that started paying 100

## 40875:00 - 40925:00

or 200 or 300k they could care less

## 40925:00 - 40965:00

about the cloud offering. So they were

## 40965:00 - 40990:00

pulling a different set of features.

## 40990:00 - 41025:00

>> The early customers, you know, again, we

## 41025:00 - 41060:00

were very market driven. So, you know,

## 41060:00 - 41090:00

we knew that like, okay, the kind of

## 41090:00 - 41125:00

tech company that we'd come out of

## 41125:00 - 41170:00

mostly they would not buy a licensed

## 41170:00 - 41200:00

software product. They would just use

## 41200:00 - 41245:00

the open source, right? Um, or they

## 41245:00 - 41285:00

might use a cloud service. You know,

## 41285:00 - 41310:00

they would they would use cloud services

## 41310:00 - 41330:00

from Amazon. Would they use a cloud

## 41330:00 - 41350:00

service from Confluent? We didn't know,

## 41350:00 - 41380:00

but we thought that was the hope there.

## 41380:00 - 41425:00

But where the early customers were was

## 41425:00 - 41475:00

you know effectively large enterprises

## 41475:00 - 41530:00

and um you know that comes with its own

## 41530:00 - 41570:00

difficulties right you definitely need

## 41570:00 - 41625:00

real kind of field team the contractual

## 41625:00 - 41655:00

stuff it's a huge

## 41655:00 - 41685:00

>> list of items you have to do so there

## 41685:00 - 41720:00

was a big kind of you know overhead of

## 41720:00 - 41750:00

that but it was it was working right we

## 41750:00 - 41790:00

we basically had kind of large marquee

## 41790:00 - 41825:00

enterprises big banks insurance

## 41825:00 - 41855:00

companies retailers who were in the

## 41855:00 - 41890:00

first 12 to 24 months

## 41890:00 - 41940:00

>> and did you start to bring in

## 41940:00 - 41970:00

some traditional sales talent at that

## 41970:00 - 41995:00

point or you did it all yourselves?

## 41995:00 - 42030:00

>> No. So, um you know I did the first set

## 42030:00 - 42100:00

of early deals and then uh hired I

## 42100:00 - 42155:00

started to hire uh individual uh reps

## 42155:00 - 42200:00

and we got that would do end to end

## 42200:00 - 42225:00

sales or that would kind of begin a

## 42225:00 - 42250:00

process and bring you in.

## 42250:00 - 42275:00

>> Yeah. Yeah. Yeah. Basically the latter,

## 42275:00 - 42310:00

you know. So I was still involved in

## 42310:00 - 42350:00

meeting all the customers or or one of

## 42350:00 - 42380:00

my co-founders would be but they were

## 42380:00 - 42410:00

and did they come out of the domain?

## 42410:00 - 42450:00

>> Yeah. So I think we um you know the

## 42450:00 - 42510:00

early sales reps were experienced in the

## 42510:00 - 42545:00

area we were in. I mean not our little

## 42545:00 - 42585:00

niche and you know the closest thing we

## 42585:00 - 42635:00

could find and they uh had worked in

## 42635:00 - 42690:00

very early companies and uh we gave them

## 42690:00 - 42720:00

a lot of equity and they were IC

## 42720:00 - 42730:00

sellers.

## 42730:00 - 42780:00

>> Yes. 100%. um or who had you know IC's

## 42780:00 - 42815:00

who had also managed maybe small teams

## 42815:00 - 42835:00

but not kind of

## 42835:00 - 42875:00

>> not VP sales whatever CRO whatever yeah

## 42875:00 - 42920:00

>> and I I think that's really a worthwhile

## 42920:00 - 42955:00

investment of you know I think you can

## 42955:00 - 43015:00

kind of amplify the founder

## 43015:00 - 43045:00

sales thing quite significantly with

## 43045:00 - 43085:00

just a few people um but you need people

## 43085:00 - 43125:00

who have been successful in early

## 43125:00 - 43165:00

companies where they just or whatever

## 43165:00 - 43220:00

>> yeah yeah you know it's like you know

## 43220:00 - 43240:00

there's no product marketing there's you

## 43240:00 - 43265:00

know, there's all these other things you

## 43265:00 - 43290:00

just don't have for them. But, I mean,

## 43290:00 - 43310:00

you have something, you have a deck that

## 43310:00 - 43340:00

you've kind of scrapped together, but

## 43340:00 - 43365:00

they they just have to be okay with

## 43365:00 - 43395:00

that, uh, and be able to fill in the

## 43395:00 - 43425:00

blanks where there isn't, you know,

## 43425:00 - 43455:00

scaffolding for them. And I think people

## 43455:00 - 43480:00

who have been in early companies can do

## 43480:00 - 43510:00

that, but the, you know, the average

## 43510:00 - 43540:00

sales rep coming out of a large company

## 43540:00 - 43605:00

is going to be kind of like WTF, like

## 43605:00 - 43645:00

this doesn't seem right. There's

## 43645:00 - 43670:00

actually a lot of lock in with these

## 43670:00 - 43705:00

products. I think it, you know, I think

## 43705:00 - 43740:00

you could think of it as almost game

## 43740:00 - 43785:00

theory, right? Like the um, you know,

## 43785:00 - 43830:00

selfishly for a provider, you would want

## 43830:00 - 43855:00

as much control and leverage as poss.

## 43855:00 - 43875:00

You would want, you know, as much

## 43875:00 - 43915:00

differentiation as leverage as possible.

## 43915:00 - 43960:00

You know, selfishly as you know, if if

## 43960:00 - 43990:00

you're the software provider, right? If

## 43990:00 - 44020:00

you're the buyer of the software, you

## 44020:00 - 44055:00

want a complete commodity, right?

## 44055:00 - 44090:00

Neither party is going to accept that.

## 44090:00 - 44115:00

and you're kind of trying to find

## 44115:00 - 44140:00

something that's the

## 44140:00 - 44165:00

>> and you want as much differentiation as

## 44165:00 - 44210:00

possible because that's that's how you

## 44210:00 - 44255:00

generate pricing power and market share.

## 44255:00 - 44290:00

You know fundamentally what if you think

## 44290:00 - 44330:00

of what is you know open source is maybe

## 44330:00 - 44385:00

the purest commodity right and so you

## 44385:00 - 44410:00

know if you're trying to sell a product

## 44410:00 - 44465:00

which is purely open source you know

## 44465:00 - 44505:00

effectively the price of that product

## 44505:00 - 44545:00

should collapse to the cost of providing

## 44545:00 - 44580:00

it which is bas kind of at scale of zero

## 44580:00 - 44620:00

right so so there's no business in

## 44620:00 - 44660:00

selling a you know pure open- source

## 44660:00 - 44695:00

software you know the business is going

## 44695:00 - 44730:00

to come out of selling something which

## 44730:00 - 44755:00

has some amount of differentiation and

## 44755:00 - 44790:00

the more differentiation then the more

## 44790:00 - 44820:00

you know you could charge but the

## 44820:00 - 44845:00

customer has to you know accept that and

## 44845:00 - 44880:00

want it and so there you know and

## 44880:00 - 44910:00

they're going to weigh those factors and

## 44910:00 - 44940:00

so if you look at how these businesses

## 44940:00 - 44970:00

have evolved yeah they you know they

## 44970:00 - 45000:00

have to really prove themselves and

## 45000:00 - 45035:00

provide that value to customers and

## 45035:00 - 45080:00

customers have to feel okay and indeed

## 45080:00 - 45120:00

customers can move off of the you know

## 45120:00 - 45150:00

any of these more open systems more

## 45150:00 - 45180:00

easily than they could something purely

## 45180:00 - 45220:00

proprietary but it's not the case that

## 45220:00 - 45265:00

the companies have no stickiness either.

## 45265:00 - 45290:00

In fact, you know, if you just look at

## 45290:00 - 45320:00

kind of revenue retention statistics, it

## 45320:00 - 45335:00

was actually quite good,

## 45335:00 - 45375:00

>> right? And so, you know, so, so if you

## 45375:00 - 45400:00

think about it, the industry has kind of

## 45400:00 - 45445:00

found a balance where you can build a

## 45445:00 - 45490:00

successful company that captures some

## 45490:00 - 45550:00

amount of value. It's not as complete

## 45550:00 - 45590:00

capture as if you had full leverage, but

## 45590:00 - 45610:00

it's also a better deal for the

## 45610:00 - 45655:00

customers. I think it is the case that

## 45655:00 - 45700:00

some of these early uh infrastructure

## 45700:00 - 45740:00

offerings you know that it goes too far

## 45740:00 - 45770:00

where the lock in is so tight that the

## 45770:00 - 45820:00

vendor can actually you know extract in

## 45820:00 - 45845:00

some sense more than the value they

## 45845:00 - 45875:00

create because moving off of it is such

## 45875:00 - 45910:00

a nightmare at that point you know which

## 45910:00 - 45935:00

becomes a very negative thing for the

## 45935:00 - 45985:00

customer right and so so yeah I I think

## 45985:00 - 46025:00

it actually works out relatively well

## 46025:00 - 46055:00

but there you know on the product side

## 46055:00 - 46090:00

there's you know finding a balance of

## 46090:00 - 46140:00

enough value and differential iation um

## 46140:00 - 46170:00

and enough openness. That's kind of the

## 46170:00 - 46185:00

tricky bit.

## 46185:00 - 46210:00

>> You had the software product that was

## 46210:00 - 46260:00

selling well and meeting the the demands

## 46260:00 - 46305:00

of and a number of enterprise customers

## 46305:00 - 46350:00

in the first 12 to 24 months and then

## 46350:00 - 46380:00

you decided to build the managed service

## 46380:00 - 46395:00

alongside it.

## 46395:00 - 46400:00

>> Yeah.

## 46400:00 - 46435:00

>> Even though it felt

## 46435:00 - 46460:00

>> tricky because you had a small team

## 46460:00 - 46475:00

being spread.

## 46475:00 - 46505:00

>> Totally. Yeah. Totally. Totally. So that

## 46505:00 - 46565:00

that that was um probably one of the

## 46565:00 - 46610:00

more difficult things that we had to do

## 46610:00 - 46655:00

early on. How did you have the

## 46655:00 - 46690:00

confidence to do that particularly

## 46690:00 - 46710:00

because you had never done any of this

## 46710:00 - 46720:00

before?

## 46720:00 - 46765:00

>> You know there's always two lenses in a

## 46765:00 - 46820:00

company. One is what can we do? And then

## 46820:00 - 46870:00

the other is what do we have to do? And

## 46870:00 - 46905:00

so what can we do? That's like an

## 46905:00 - 46940:00

opinion from the team. What do we have

## 46940:00 - 46970:00

to do is kind of imposed by the world.

## 46970:00 - 46990:00

And so you kind of look at these things

## 46990:00 - 47035:00

and you're like, okay, can we do two

## 47035:00 - 47055:00

products at the same time? And it's

## 47055:00 - 47105:00

like, well, I don't know. Like maybe,

## 47105:00 - 47125:00

maybe we can. It's going to be very

## 47125:00 - 47150:00

hard. Most people would say, don't do

## 47150:00 - 47190:00

that. That's a bad idea. All else being

## 47190:00 - 47230:00

equal. Um, but if you look at, well, you

## 47230:00 - 47270:00

know, what do we have to do? We

## 47270:00 - 47300:00

absolutely have to do this, right? Like

## 47300:00 - 47345:00

there's no question that a huge portion

## 47345:00 - 47380:00

of the market is going to be in the

## 47380:00 - 47420:00

public cloud. And nobody in the public

## 47420:00 - 47445:00

cloud is going to want to consume a

## 47445:00 - 47485:00

licensed software power. So we like we

## 47485:00 - 47510:00

have to have that part of the market.

## 47510:00 - 47555:00

For me at least I felt okay it's very

## 47555:00 - 47610:00

clear that that's like a existential

## 47610:00 - 47670:00

thing. So we just have to do it you know

## 47670:00 - 47720:00

and then um we have to find a way that

## 47720:00 - 47760:00

it can be done. Uh and I I think that's

## 47760:00 - 47795:00

actually a very

## 47795:00 - 47825:00

important takeaway. I found that that's

## 47825:00 - 47870:00

often true that you know teams because

## 47870:00 - 47910:00

they spend all their time thinking about

## 47910:00 - 47945:00

how to do something they become very

## 47945:00 - 47990:00

fixated on what can be done. Um and it's

## 47990:00 - 48010:00

actually very important to step back and

## 48010:00 - 48035:00

be like hey to be successful in this

## 48035:00 - 48070:00

product area what do we have to do and

## 48070:00 - 48110:00

then you know it's weird once you know

## 48110:00 - 48155:00

you have to do it then you find a way to

## 48155:00 - 48195:00

do it and you know this this phenomenon

## 48195:00 - 48240:00

is seen elsewhere like the um you know I

## 48240:00 - 48275:00

think the famous you know whatever

## 48275:00 - 48325:00

business book example is like the

## 48325:00 - 48380:00

4-minute mile or some marathon time or

## 48380:00 - 48420:00

any of these sports things which once

## 48420:00 - 48445:00

you know for a long time it's seen as

## 48445:00 - 48470:00

unachievable and then as soon as

## 48470:00 - 48490:00

somebody does it and you know you have

## 48490:00 - 48515:00

to do that to compete then everybody

## 48515:00 - 48580:00

does it and um so in other words the it

## 48580:00 - 48610:00

becomes possible once people know they

## 48610:00 - 48650:00

have to do it uh and so I think that's I

## 48650:00 - 48675:00

think that's an important view but it

## 48675:00 - 48720:00

was just very clear we have to do this

## 48720:00 - 48750:00

um it was just very difficult like we

## 48750:00 - 48805:00

understood on the engineering side okay

## 48805:00 - 48825:00

that's a very different delivery

## 48825:00 - 48865:00

mechanism you know it'll be a lot of

## 48865:00 - 48905:00

work to build uh and we'd prepared for

## 48905:00 - 48950:00

that from early in the company so we

## 48950:00 - 48985:00

were kind of we thought set up to do it.

## 48985:00 - 49010:00

It was in fact much harder than we

## 49010:00 - 49030:00

thought. There's definitely a

## 49030:00 - 49065:00

methodology for that for any company

## 49065:00 - 49105:00

that goes multi-roduct.

## 49105:00 - 49140:00

We didn't know the methodology. So I

## 49140:00 - 49190:00

think it was just blunt force was you

## 49190:00 - 49235:00

know um just continuing to focus on it

## 49235:00 - 49265:00

until we did it. It was controversial

## 49265:00 - 49295:00

internally. Probably half the company

## 49295:00 - 49330:00

thought this was like the dumbest thing

## 49330:00 - 49375:00

ever. You know it was still not the case

## 49375:00 - 49425:00

that most of the market was in the

## 49425:00 - 49450:00

public cloud.

## 49450:00 - 49500:00

it was the product wasn't really

## 49500:00 - 49535:00

selling. You know, it was basically

## 49535:00 - 49575:00

harder to sell and we made less money

## 49575:00 - 49625:00

and the economics were worse. So, you

## 49625:00 - 49655:00

know, some of, you know, I I think even

## 49655:00 - 49680:00

some of the investors were kind of like,

## 49680:00 - 49720:00

what do you guys have like the on paper

## 49720:00 - 49765:00

like the best enterprise business ever

## 49765:00 - 49795:00

and you're putting all your energy on

## 49795:00 - 49825:00

this other thing that kind of sucks?

## 49825:00 - 49855:00

Like, if there was two standalone

## 49855:00 - 49885:00

companies, we would definitely invest in

## 49885:00 - 49905:00

this one and we would definitely not

## 49905:00 - 49940:00

invest in that one. you know, we just

## 49940:00 - 49980:00

kind of bludgeoned our way through like

## 49980:00 - 50015:00

none of it was pretty. You know, some of

## 50015:00 - 50080:00

our biggest early customers quit on us

## 50080:00 - 50105:00

>> because the product did not meet their

## 50105:00 - 50115:00

needs

## 50115:00 - 50145:00

>> in various ways, right? They either

## 50145:00 - 50205:00

outscaled us, the limitations were too

## 50205:00 - 50240:00

embarrassing. Yeah, the challenge for

## 50240:00 - 50295:00

this kind of infrastructure is um you

## 50295:00 - 50320:00

know customers often kind of start small

## 50320:00 - 50350:00

and then kind of you just have to do

## 50350:00 - 50385:00

whatever they need to do in their so

## 50385:00 - 50420:00

everything they could flexibly do in

## 50420:00 - 50455:00

their environment you have to have that

## 50455:00 - 50490:00

capability but kind of fully automated

## 50490:00 - 50525:00

and you have to be excellent at kind of

## 50525:00 - 50570:00

at scale operations and yeah the the

## 50570:00 - 50625:00

promise of these kind of fully managed

## 50625:00 - 50655:00

cloud infrastructure offerings you know

## 50655:00 - 50685:00

that that's kind of an easy thing to do

## 50685:00 - 50715:00

for like application layer software but

## 50715:00 - 50745:00

hard for these big distributed data

## 50745:00 - 50780:00

systems, but you the promise is, hey,

## 50780:00 - 50800:00

it's just going to kind of run itself,

## 50800:00 - 50845:00

right? So, it's like a self-driving car,

## 50845:00 - 50905:00

right? And, you know, but the the

## 50905:00 - 50940:00

feeling if you're in a self-driving car

## 50940:00 - 50990:00

that crashes is not so good. You're

## 50990:00 - 51020:00

like, yeah, you know, if I'm holding the

## 51020:00 - 51050:00

wheel, sure, maybe I get into a fender

## 51050:00 - 51070:00

bender once in a while, but at least I

## 51070:00 - 51115:00

know what's going on. And so yeah that

## 51115:00 - 51160:00

early cloud product was very challenging

## 51160:00 - 51200:00

but to to build on the metaphor it did

## 51200:00 - 51240:00

feel like when you were working on it

## 51240:00 - 51280:00

>> and you were making the promise Allah

## 51280:00 - 51335:00

self-driving that everybody continued to

## 51335:00 - 51370:00

be excited about the promise

## 51370:00 - 51425:00

>> it was that when they used the product

## 51425:00 - 51455:00

it was not delivering on the promise and

## 51455:00 - 51495:00

so you knew that the you knew that if

## 51495:00 - 51535:00

the promise was delivered on there was a

## 51535:00 - 51545:00

there there.

## 51545:00 - 51580:00

>> Yeah. I think in many of these areas

## 51580:00 - 51605:00

that we've pushed through something

## 51605:00 - 51630:00

hard, you know, I do think it starts

## 51630:00 - 51680:00

with conviction of like, okay, this has

## 51680:00 - 51740:00

to work, you know, therefore we have to

## 51740:00 - 51765:00

make it work. Like the fact that it's

## 51765:00 - 51825:00

not working now doesn't is not relevant

## 51825:00 - 51880:00

to what has to happen, right? And so,

## 51880:00 - 51910:00

yeah. Yeah. So, but but nonetheless, it

## 51910:00 - 51945:00

was a big struggle. I think inherently

## 51945:00 - 52010:00

that a second product is always

## 52010:00 - 52045:00

kind of irrelevant to people's main

## 52045:00 - 52095:00

goals, you know, and the all the

## 52095:00 - 52140:00

pressure of a business is to satisfy the

## 52140:00 - 52165:00

customers that you have the big

## 52165:00 - 52200:00

prospects coming in the door that that

## 52200:00 - 52230:00

kind of main flow of business becomes

## 52230:00 - 52285:00

this like magnetic force and so yeah we

## 52285:00 - 52320:00

you know we really just had to force

## 52320:00 - 52350:00

feed it in each area. So I think for the

## 52350:00 - 52405:00

engineering team we just we you know

## 52405:00 - 52425:00

originally it was like a small group

## 52425:00 - 52450:00

that was working on the cloud offering

## 52450:00 - 52485:00

and then we were like no okay everybody

## 52485:00 - 52520:00

only does the cloud thing and we will

## 52520:00 - 52550:00

work on the software product in our

## 52550:00 - 52590:00

spare time team by team which is

## 52590:00 - 52610:00

>> a very dangerous thing to do because

## 52610:00 - 52640:00

that was where all the money was. It

## 52640:00 - 52665:00

didn't work to say we're basically just

## 52665:00 - 52700:00

going to split the company and have two

## 52700:00 - 52725:00

companies two go to markets two

## 52725:00 - 52735:00

engineering teams.

## 52735:00 - 52770:00

>> Yeah because um you know many of the

## 52770:00 - 52810:00

fundamental components were shared. So

## 52810:00 - 52835:00

what would happen is like okay the cloud

## 52835:00 - 52860:00

teams try to build this fully managed

## 52860:00 - 52910:00

thing. They need the Kafka part to work

## 52910:00 - 52930:00

for what they're doing. They go to the

## 52930:00 - 52955:00

Kafka team. Kafka team's like look at

## 52955:00 - 52980:00

all these you know this customer needs

## 52980:00 - 53010:00

this and this and you know what do you

## 53010:00 - 53040:00

want this for this science project.

## 53040:00 - 53075:00

>> Yeah totally totally or a small amount

## 53075:00 - 53100:00

of money. It was just, you know, where

## 53100:00 - 53130:00

is the pressure? And then the same on

## 53130:00 - 53170:00

the, you know, the same on the sales and

## 53170:00 - 53200:00

go to market side was just really

## 53200:00 - 53260:00

breaking out every single goal for cloud

## 53260:00 - 53290:00

and treating those numbers like there

## 53290:00 - 53325:00

was just an extra zero or two at the

## 53325:00 - 53360:00

end, you know, like that. That was the

## 53360:00 - 53425:00

thing. Um, until it worked. And um, and

## 53425:00 - 53460:00

it did, you know, we eventually ground,

## 53460:00 - 53485:00

you know, through that kind of painful

## 53485:00 - 53520:00

part, you know, interesting. I mean, the

## 53520:00 - 53550:00

the product was growing quickly early

## 53550:00 - 53590:00

on. It was just very lumpy and

## 53590:00 - 53620:00

uncomfortable and off such a small

## 53620:00 - 53640:00

number relative to the rest of the

## 53640:00 - 53675:00

business that it just looked like zero.

## 53675:00 - 53700:00

>> Was the rest of the business in the tens

## 53700:00 - 53730:00

of mill like what was the scale of it?

## 53730:00 - 53780:00

>> Yeah, you know, it was over time. So, um

## 53780:00 - 53810:00

yeah, we were probably in the tens, you

## 53810:00 - 53845:00

know, the the early early confluent grew

## 53845:00 - 53900:00

very fast off the software product and

## 53900:00 - 53945:00

so you know, I think we got to 100

## 53945:00 - 53970:00

million in revenue just very quickly

## 53970:00 - 54000:00

after and so the software product is

## 54000:00 - 54040:00

like at 100 million and this is like

## 54040:00 - 54060:00

>> Yeah. Well, it was it was different

## 54060:00 - 54090:00

points along the way, but yeah, we we

## 54090:00 - 54120:00

started it in, you know, we started

## 54120:00 - 54140:00

working on it probably in our second

## 54140:00 - 54190:00

year of selling in, you know, probably

## 54190:00 - 54245:00

by our third year of selling. It was on

## 54245:00 - 54310:00

the scoreboard, but just looked like a

## 54310:00 - 54370:00

embarrassing failure. And then um but

## 54370:00 - 54395:00

nonetheless, it was going up. It was

## 54395:00 - 54440:00

just so it just didn't look like it was

## 54440:00 - 54465:00

catching up. And then you know as we

## 54465:00 - 54500:00

kind of rounded the corner on some of

## 54500:00 - 54525:00

the product functionality indeed you did

## 54525:00 - 54575:00

start for you did it feel

## 54575:00 - 54630:00

on the on the managed service that there

## 54630:00 - 54675:00

was a crossing the chasm moment line in

## 54675:00 - 54710:00

the sand or was it just a little bit

## 54710:00 - 54745:00

less shitty every single day forever

## 54745:00 - 54770:00

basically. Yeah, it was it was mostly

## 54770:00 - 54800:00

the latter. You know, I I always feel

## 54800:00 - 54840:00

like the crossing the chasm thing is the

## 54840:00 - 54870:00

promise, you know, can you make this

## 54870:00 - 54915:00

promise and then the the hundred things

## 54915:00 - 54960:00

required to deliver the promise. That's

## 54960:00 - 55005:00

the thing we were chipping away at, but

## 55005:00 - 55055:00

it never felt like on the on the on the

## 55055:00 - 55085:00

act 2 product that there was this

## 55085:00 - 55120:00

massive phase shift and we got to the

## 55120:00 - 55155:00

last brick slid in.

## 55155:00 - 55185:00

>> Absolutely. So, yeah, it definitely

## 55185:00 - 55230:00

wasn't one feature that we did. When you

## 55230:00 - 55265:00

reflect on

## 55265:00 - 55315:00

what about yourself

## 55315:00 - 55365:00

has allowed you to be successful as a

## 55365:00 - 55420:00

founder and CEO specifically at also the

## 55420:00 - 55460:00

first time you've done this. What about

## 55460:00 - 55490:00

you as a human do you think were the

## 55490:00 - 55525:00

input drivers to it or like what's your

## 55525:00 - 55550:00

working theory of it? I think there's

## 55550:00 - 55600:00

probably two things that were helpful

## 55600:00 - 55630:00

for me. You know there's there's

## 55630:00 - 55680:00

probably 15 things 15 ways in which I'm

## 55680:00 - 55730:00

unsuited to the job. But the the two

## 55730:00 - 55765:00

things I think were helpful was you know

## 55765:00 - 55810:00

the first just being um you know curious

## 55810:00 - 55850:00

and wanting to learn about all the parts

## 55850:00 - 55885:00

of the business and how it worked our

## 55885:00 - 55940:00

customers how they work. I do think that

## 55940:00 - 55980:00

um you know even people who come into a

## 55980:00 - 56025:00

CEO job in an atscale company coming out

## 56025:00 - 56065:00

of a different discipline I do think the

## 56065:00 - 56110:00

CEO role is probably more multi-

## 56110:00 - 56150:00

disciplinary you know so so you

## 56150:00 - 56185:00

ultimately have to be very interested in

## 56185:00 - 56205:00

learning about the market learning about

## 56205:00 - 56225:00

the customers learning about the

## 56225:00 - 56260:00

competitors learning about each function

## 56260:00 - 56295:00

you know in a way that's probably

## 56295:00 - 56340:00

broader than many of the other executive

## 56340:00 - 56375:00

roles and you know even as a software

## 56375:00 - 56425:00

engineer I'd always just and curious

## 56425:00 - 56465:00

about stuff and software engineers

## 56465:00 - 56510:00

probably generally are in learning mode

## 56510:00 - 56550:00

more than many professions even if it's

## 56550:00 - 56605:00

not in that broad way. Uh and so I I

## 56605:00 - 56650:00

think that was probably a good asset.

## 56650:00 - 56715:00

And then um I'm also just tenacious.

## 56715:00 - 56750:00

I'm not necessarily an optimist. Like I

## 56750:00 - 56785:00

think it helps if you're an optimist.

## 56785:00 - 56810:00

You know, I think like as you were

## 56810:00 - 56825:00

saying probably some of the best

## 56825:00 - 56850:00

founders are just these inherently

## 56850:00 - 56890:00

optimistic people. But, you know, if you

## 56890:00 - 56920:00

don't have that, then I think it gets

## 56920:00 - 56945:00

you there if you're just determined

## 56945:00 - 56980:00

where you're like, "Well, okay, then the

## 56980:00 - 57015:00

probability is only 20%, but we're not

## 57015:00 - 57050:00

going to give up until we've, you know,

## 57050:00 - 57090:00

lost all hope, right?" And, you know,

## 57090:00 - 57115:00

that that turns out not to be as

## 57115:00 - 57140:00

inspiring a message, so you might want

## 57140:00 - 57165:00

to dress it up a bit. But, you know, I

## 57165:00 - 57215:00

think just willingness to kind of keep

## 57215:00 - 57265:00

working on things um, you know, well

## 57265:00 - 57320:00

past the point where it's a bit painful,

## 57320:00 - 57350:00

you know, I I I think is important. And

## 57350:00 - 57390:00

I, you know, I think that kind of um

## 57390:00 - 57435:00

whatever tenaciousness, pain tolerance,

## 57435:00 - 57465:00

you know, I think that couples, I think

## 57465:00 - 57480:00

that's actually probably the most

## 57480:00 - 57510:00

important ingredient for the willingness

## 57510:00 - 57540:00

to kind of go after the things that you

## 57540:00 - 57585:00

have to do. So I I do think especially

## 57585:00 - 57620:00

in early companies, but probably in all

## 57620:00 - 57650:00

companies, you know, there's these kind

## 57650:00 - 57710:00

of big threats or bad news things or

## 57710:00 - 57740:00

things that will kill the company, and

## 57740:00 - 57765:00

the tendency is nobody wants to talk

## 57765:00 - 57805:00

about that stuff, right? But I do think

## 57805:00 - 57835:00

you have to just kind of lean into those

## 57835:00 - 57880:00

things and get them figured out, right?

## 57880:00 - 57915:00

Get them addressed, whatever it is. And

## 57915:00 - 57950:00

I I do think that's again kind of back

## 57950:00 - 58025:00

to the just tenacious part of it. And I,

## 58025:00 - 58050:00

you know, I have come to believe that

## 58050:00 - 58095:00

that it's not enough on its own, but

## 58095:00 - 58140:00

just not giving up on something, uh, you

## 58140:00 - 58175:00

know, for an extended period of time, it

## 58175:00 - 58220:00

actually gets you pretty far, you know,

## 58220:00 - 58250:00

and I found that in, you know,

## 58250:00 - 58280:00

competitive situations, in other

## 58280:00 - 58310:00

situations, and if you just keep working

## 58310:00 - 58350:00

on it, like you'll keep improving and

## 58350:00 - 58390:00

other people will kind of tap out at

## 58390:00 - 58420:00

some point. And, you know, if you don't,

## 58420:00 - 58450:00

then, you know, eventually you will kind

## 58450:00 - 58470:00

of get there. And maybe it didn't look

## 58470:00 - 58500:00

pretty at first, but it'll look pretty

## 58500:00 - 58540:00

if it eventually works. And you know, I

## 58540:00 - 58560:00

think that that thinking goes a long

## 58560:00 - 58600:00

way. I don't know that it's a blanket

## 58600:00 - 58625:00

rule because of course there is, you

## 58625:00 - 58650:00

know, some point in time,

## 58650:00 - 58675:00

>> right? Are there are there things that

## 58675:00 - 58710:00

you were doggedly pursuing in the

## 58710:00 - 58745:00

context of confluent and then you

## 58745:00 - 58780:00

eventually did wave the white flag or

## 58780:00 - 58825:00

whatever the expression? We mostly um we

## 58825:00 - 58865:00

mostly carried through on things you

## 58865:00 - 58880:00

know that I

## 58880:00 - 58915:00

>> is it because you were would you say if

## 58915:00 - 58940:00

that's the case is it because you were

## 58940:00 - 58950:00

correct

## 58950:00 - 58985:00

>> or that in the process of grinding

## 58985:00 - 59010:00

through

## 59010:00 - 59035:00

>> it kind of got you to

## 59035:00 - 59060:00

>> Yeah, it's probably both. I mean I I

## 59060:00 - 59085:00

guess I would caveat this. So obviously

## 59085:00 - 59110:00

you want to be very flexible about some

## 59110:00 - 59155:00

of the details of how you do something,

## 59155:00 - 59190:00

right? That's the whole point is to

## 59190:00 - 59225:00

change your mind on that. And then I

## 59225:00 - 59255:00

think on the big things you know do we

## 59255:00 - 59300:00

need a cloud service for us you know we

## 59300:00 - 59330:00

also we've wanted you know one of the

## 59330:00 - 59365:00

more recent versions of this was we felt

## 59365:00 - 59400:00

is very important for the company to do

## 59400:00 - 59450:00

the processing of data not just the flow

## 59450:00 - 59485:00

and we worked on this largely

## 59485:00 - 59520:00

unsuccessfully for a number of years

## 59520:00 - 59560:00

right and so it was just kind of

## 59560:00 - 59595:00

products it didn't take off in the last

## 59595:00 - 59635:00

few years that's really started to take

## 59635:00 - 59670:00

off for us as part of the business but

## 59670:00 - 59700:00

to get there we we actually did give up

## 59700:00 - 59730:00

on early versions of the product we had

## 59730:00 - 59775:00

done in that space. And so I guess, you

## 59775:00 - 59790:00

know, I guess you'd have to be

## 59790:00 - 59810:00

thoughtful about what was giving up

## 59810:00 - 59845:00

versus not giving up. You know, I I

## 59845:00 - 59875:00

think it was logically true that we had

## 59875:00 - 59900:00

to have a product. I think it's

## 59900:00 - 59930:00

logically true that Confluent has to do

## 59930:00 - 59965:00

the processing of data to like have

## 59965:00 - 60000:00

strategic importance. So you kind of

## 60000:00 - 60035:00

can't give up on that just because you

## 60035:00 - 60075:00

haven't succeeded yet. Like you has to

## 60075:00 - 60125:00

work. And then the how you get there,

## 60125:00 - 60160:00

you know, you're just gonna keep trying

## 60160:00 - 60220:00

like strategy, people, whatever has to

## 60220:00 - 60240:00

change. You're going to just keep trying

## 60240:00 - 60290:00

until you can kind of make it move. And

## 60290:00 - 60335:00

um you know, I I I think once you know

## 60335:00 - 60365:00

in a very early company, you may not

## 60365:00 - 60410:00

have that much runway to do that. But

## 60410:00 - 60435:00

once you have at least something in the

## 60435:00 - 60455:00

business working, then you usually

## 60455:00 - 60485:00

usually you have enough time to kind of

## 60485:00 - 60510:00

keep working at the things that have to

## 60510:00 - 60545:00

work. So I think just being very clear

## 60545:00 - 60590:00

of like hey what what is it that must be

## 60590:00 - 60650:00

true for this thing to succeed or be at

## 60650:00 - 60695:00

the next level and then am I really

## 60695:00 - 60740:00

confident that we're on that trajectory

## 60740:00 - 60775:00

and I feel like those two things often

## 60775:00 - 60805:00

are missed right people are not clear on

## 60805:00 - 60845:00

what really must be true or they tell

## 60845:00 - 60875:00

themselves kind of a happy story that

## 60875:00 - 60900:00

the things that are already working are

## 60900:00 - 60935:00

really the only thing that's that matter

## 60935:00 - 60970:00

and then you know are we really on that

## 60970:00 - 61000:00

trajectory I think that's another one

## 61000:00 - 61040:00

where people often if if you don't know

## 61040:00 - 61080:00

how to fix something then you often tell

## 61080:00 - 61110:00

yourself well it's good enough right but

## 61110:00 - 61140:00

but in fact you know it's not you know

## 61140:00 - 61165:00

and that that may be about the people

## 61165:00 - 61200:00

doing it may be about the product

## 61200:00 - 61225:00

approach you've taken it may be about

## 61225:00 - 61255:00

something else but you kind of know like

## 61255:00 - 61290:00

okay this is not working the way it

## 61290:00 - 61325:00

should and I think when you don't know

## 61325:00 - 61360:00

the answer of how what how it should be

## 61360:00 - 61390:00

or how to fix it I think it's very

## 61390:00 - 61435:00

uncomfortable to say like okay like this

## 61435:00 - 61485:00

is not this is not this is not happening

## 61485:00 - 61510:00

you know and then But until you say

## 61510:00 - 61540:00

that, you can't really figure out what

## 61540:00 - 61580:00

to do about it. When you're off on

## 61580:00 - 61615:00

trajectory

## 61615:00 - 61650:00

and you look at the root causes across

## 61650:00 - 61695:00

the sort of different trajectories of

## 61695:00 - 61750:00

the business, is it more often X or Y or

## 61750:00 - 61795:00

it's evenly distributed? Meaning 80% of

## 61795:00 - 61820:00

the time when you're off trajectory,

## 61820:00 - 61850:00

it's the wrong person is in the seat.

## 61850:00 - 61880:00

You fix the person, you know, or is it

## 61880:00 - 61920:00

just it's 20% that, it's 20% the product

## 61920:00 - 61965:00

philosophy is wrong. maybe 20% it was

## 61965:00 - 61985:00

just a year too early and the market

## 61985:00 - 62010:00

wasn't there for it. You know

## 62010:00 - 62055:00

>> I I think it's actually all of those

## 62055:00 - 62125:00

things. Um you know a disproportionate

## 62125:00 - 62175:00

percentage is people but I do think also

## 62175:00 - 62210:00

sometimes in organizations people

## 62210:00 - 62255:00

somehow become trapped in basically a

## 62255:00 - 62305:00

failing mindset and methodology. And so

## 62305:00 - 62330:00

like part of the people change is

## 62330:00 - 62365:00

actually changing is opening the

## 62365:00 - 62390:00

aperture on what that part of the org is

## 62390:00 - 62425:00

willing to try. And so yeah, I I think

## 62425:00 - 62480:00

that debugging process is one of the

## 62480:00 - 62535:00

hardest things I think in any company.

## 62535:00 - 62555:00

You know, you kind of have some top

## 62555:00 - 62585:00

level result and you're like, well, this

## 62585:00 - 62655:00

is not what we want, right? And then

## 62655:00 - 62695:00

ascribing the cause of what's not

## 62695:00 - 62755:00

working well is actually shockingly

## 62755:00 - 62780:00

difficult. You see, I mean, you see it

## 62780:00 - 62805:00

all the time. You know, typically it

## 62805:00 - 62835:00

always comes back from sales, right?

## 62835:00 - 62855:00

People are like, well, it's not, you

## 62855:00 - 62890:00

know, sales are not good, so what's the

## 62890:00 - 62915:00

problem? And it's like, okay, that sales

## 62915:00 - 62935:00

leader is bad, right? And it's like,

## 62935:00 - 62975:00

well, it could be

## 62975:00 - 63025:00

but the and you know that that certainly

## 63025:00 - 63055:00

could be and commonly is, but but it

## 63055:00 - 63100:00

could be every other thing in the chain

## 63100:00 - 63145:00

of value leading up to that. You know, I

## 63145:00 - 63165:00

think that's often one of the most

## 63165:00 - 63190:00

maddening parts of these things

## 63190:00 - 63240:00

>> or across the years of the business, do

## 63240:00 - 63290:00

you personally spend a lot of time on

## 63290:00 - 63315:00

this diagnostic work?

## 63315:00 - 63350:00

>> Yeah. Yeah. Yourself?

## 63350:00 - 63385:00

>> Yeah, absolutely. So um you know

## 63385:00 - 63435:00

anything that's not working at a high

## 63435:00 - 63500:00

level is inherently crossunctional

## 63500:00 - 63540:00

and um you know you'll see a weird

## 63540:00 - 63595:00

phenomenon where people in each function

## 63595:00 - 63640:00

are often don't have enough global

## 63640:00 - 63695:00

context to totally diagnose it. They may

## 63695:00 - 63730:00

but but it's often depending on their

## 63730:00 - 63780:00

personality. Some people think mostly

## 63780:00 - 63810:00

about their function. So like you you

## 63810:00 - 63835:00

know you'll see some people where if

## 63835:00 - 63880:00

they're something is not working and

## 63880:00 - 63905:00

they're on the product team they

## 63905:00 - 63940:00

inherently think it's we don't have

## 63940:00 - 63975:00

enough product features right and it's

## 63975:00 - 64000:00

like well it could be right but it could

## 64000:00 - 64025:00

also just be we have no idea how to sell

## 64025:00 - 64050:00

the thing but you are not thinking about

## 64050:00 - 64065:00

that you're thinking about the product

## 64065:00 - 64105:00

functionality right you see other people

## 64105:00 - 64145:00

who are the opposite where they tend to

## 64145:00 - 64170:00

just kind of blame some other part of

## 64170:00 - 64205:00

the organization out of defensiveness

## 64205:00 - 64245:00

but sales blames product as like a

## 64245:00 - 64260:00

configuration

## 64260:00 - 64305:00

>> somehow I do think the CEO is in a good

## 64305:00 - 64330:00

position. You know, if it's important

## 64330:00 - 64355:00

and it's crossunctional, I do think

## 64355:00 - 64385:00

you're in a good position to kind of put

## 64385:00 - 64420:00

the puzzle pieces together. It doesn't

## 64420:00 - 64455:00

mean you're doing that in isolation. You

## 64455:00 - 64485:00

know, like the way the CEO does things

## 64485:00 - 64515:00

is just go ask everybody like, "Hey, why

## 64515:00 - 64550:00

does this work?" And then take all the

## 64550:00 - 64590:00

answers and be like, "Okay, try and

## 64590:00 - 64610:00

figure out which of these makes the most

## 64610:00 - 64640:00

sense and what do we if that was the

## 64640:00 - 64685:00

case, what would we do?" Um, but I I do

## 64685:00 - 64710:00

think often the CEO is in a good

## 64710:00 - 64770:00

position to do that because it you you

## 64770:00 - 64830:00

have to think very flexibly aces across

## 64830:00 - 64865:00

different parts of the or one of the

## 64865:00 - 64890:00

things I wanted to go back to as we kind

## 64890:00 - 64945:00

of start to wrap up, you shared this

## 64945:00 - 64995:00

idea of spending a lot of time figuring

## 64995:00 - 65040:00

out what you must do, not what you can

## 65040:00 - 65110:00

do. Is that instantiated across the

## 65110:00 - 65140:00

company, across the whole history of the

## 65140:00 - 65185:00

company in some way or is it just an

## 65185:00 - 65250:00

idea that you hit the drum on and

## 65250:00 - 65295:00

mention all the time and yeah, probably

## 65295:00 - 65330:00

more the latter. we didn't turn it into

## 65330:00 - 65420:00

like a value or you know um you know

## 65420:00 - 65440:00

management principle or something like

## 65440:00 - 65485:00

that but but I um but I do think it's

## 65485:00 - 65545:00

kind of a common refrain of like you

## 65545:00 - 65585:00

know especially as a company gets bigger

## 65585:00 - 65625:00

it's very difficult

## 65625:00 - 65655:00

um you know a natural thing if you're

## 65655:00 - 65680:00

one team that needs to do something that

## 65680:00 - 65710:00

touches five teams is you go to the five

## 65710:00 - 65730:00

teams and you're like hey this is what I

## 65730:00 - 65765:00

need from you and everybody says oh I

## 65765:00 - 65795:00

can do it or I can't do it or if I could

## 65795:00 - 65820:00

do it I could do in 12 months or

## 65820:00 - 65845:00

whatever it is. You put all that

## 65845:00 - 65870:00

together and you're like, "Okay, here's

## 65870:00 - 65895:00

what's doable. We can do this project

## 65895:00 - 65945:00

and it's going to take two years." And

## 65945:00 - 65965:00

that's kind of the best answer that

## 65965:00 - 65985:00

we've gotten out of all these people. So

## 65985:00 - 66025:00

that's what it is, right? And I don't

## 66025:00 - 66090:00

have any magic wand as a person in the

## 66090:00 - 66125:00

company to change that, right? And so

## 66125:00 - 66155:00

the lens that's very important for, you

## 66155:00 - 66175:00

know, really that whole group of

## 66175:00 - 66205:00

constituents is like, okay, how

## 66205:00 - 66225:00

important is that thing and is that good

## 66225:00 - 66265:00

enough? Right? Maybe 2 years is fine. If

## 66265:00 - 66300:00

it's not fine, then the fact that that

## 66300:00 - 66320:00

was the best we could do is not

## 66320:00 - 66350:00

relevant. Like we're you know we're

## 66350:00 - 66380:00

we're going to be unsuccessful if that's

## 66380:00 - 66450:00

what we do. And you know once once

## 66450:00 - 66470:00

you know it's weird how these things

## 66470:00 - 66525:00

work. Everybody who has found this with

## 66525:00 - 66575:00

headcount with budget with timelines you

## 66575:00 - 66600:00

know if you kind of just go back and say

## 66600:00 - 66635:00

well okay you know what would the

## 66635:00 - 66670:00

3-month version of it look like? Maybe

## 66670:00 - 66715:00

that's totally impossible, but a

## 66715:00 - 66735:00

significant portion of the time there is

## 66735:00 - 66750:00

something you could do in three months.

## 66750:00 - 66785:00

And what would that be? Is that a good

## 66785:00 - 66810:00

starting point? What if we change this

## 66810:00 - 66835:00

assumption? You know, it kind of makes

## 66835:00 - 66860:00

people go back to the drawing board and

## 66860:00 - 66900:00

question assumptions, but it doesn't

## 66900:00 - 66945:00

naturally happen in a big organization.

## 66945:00 - 66975:00

So, yeah, I don't know a way of making

## 66975:00 - 67010:00

it happen more organically that I think

## 67010:00 - 67050:00

it's a good practice. To wrap up, when

## 67050:00 - 67095:00

you look at the totality going from

## 67095:00 - 67150:00

open- source project software, managed

## 67150:00 - 67200:00

service at scale, enterprise software

## 67200:00 - 67245:00

company, publicly traded company. What

## 67245:00 - 67280:00

are a few of the things that you figured

## 67280:00 - 67320:00

out that are globally correct for people

## 67320:00 - 67350:00

creating startups that maybe aren't

## 67350:00 - 67400:00

talked about enough? like there are many

## 67400:00 - 67435:00

things you mentioned that are correct in

## 67435:00 - 67465:00

the context of the vessel that is

## 67465:00 - 67500:00

confluent but I'm curious like where do

## 67500:00 - 67570:00

you have conviction that these few ideas

## 67570:00 - 67600:00

are broadly correct and maybe

## 67600:00 - 67640:00

underappreciated or underexplored

## 67640:00 - 67690:00

in company building yeah it's hard to

## 67690:00 - 67740:00

know what's underappreciated because so

## 67740:00 - 67790:00

much you know like even compared to when

## 67790:00 - 67825:00

we were starting 10 years ago there's so

## 67825:00 - 67855:00

much wisdom that's out there that is

## 67855:00 - 67905:00

probably appreciated by somebody. I I

## 67905:00 - 67935:00

think as a company gets bigger, one of

## 67935:00 - 67960:00

the things I've come to believe is

## 67960:00 - 68000:00

really important is having, you know,

## 68000:00 - 68055:00

that, you know, a small company kind of

## 68055:00 - 68095:00

works almost like a,

## 68095:00 - 68120:00

you know, fancy restaurant, like fine

## 68120:00 - 68150:00

dining. Anything can be kind of

## 68150:00 - 68190:00

customized or done right to get the

## 68190:00 - 68220:00

outcome. And it works pretty well, but

## 68220:00 - 68265:00

at small scale, in a big company, I

## 68265:00 - 68290:00

think you become almost like you you

## 68290:00 - 68330:00

naturally become more of a system. And

## 68330:00 - 68355:00

so it's a little bit like Chipotle, like

## 68355:00 - 68395:00

it's not going to be great, but it's not

## 68395:00 - 68425:00

going to be terrible. And that's kind of

## 68425:00 - 68465:00

the natural tendency and it's the most

## 68465:00 - 68505:00

comfortable thing. You know, I do think

## 68505:00 - 68545:00

trying to replicate pockets of

## 68545:00 - 68590:00

excellence even if it is leads to

## 68590:00 - 68615:00

inconsistency.

## 68615:00 - 68655:00

Um I think that's actually, you know,

## 68655:00 - 68705:00

really important. the and to do it, you

## 68705:00 - 68745:00

know, you almost need people to, you

## 68745:00 - 68775:00

know, do things that are kind of outside

## 68775:00 - 68820:00

of the norm of how business operates.

## 68820:00 - 68850:00

So, I found that to be very true in

## 68850:00 - 68905:00

hiring where, you know, people who just,

## 68905:00 - 68935:00

you know, act like they have they, you

## 68935:00 - 68965:00

know, they just have to fight for their

## 68965:00 - 69015:00

life to go hire this team by themselves

## 69015:00 - 69045:00

as if there was no recruiting support

## 69045:00 - 69080:00

and they're just really devoting a ton

## 69080:00 - 69115:00

of energy to it like that, those people

## 69115:00 - 69160:00

are just massively more successful. But

## 69160:00 - 69200:00

if you're in, you know, most of the

## 69200:00 - 69240:00

large tech companies, they actually have

## 69240:00 - 69270:00

kind of some pipeline system that feeds

## 69270:00 - 69300:00

you candidates and the whole system is

## 69300:00 - 69330:00

actually set up to disincentivize that

## 69330:00 - 69345:00

because they don't want to be dependent

## 69345:00 - 69385:00

on people, you know, only having

## 69385:00 - 69415:00

successful managers that they can find

## 69415:00 - 69440:00

their own people. and say, you know, I

## 69440:00 - 69460:00

do think there's many things that are

## 69460:00 - 69500:00

very like that where you have to train

## 69500:00 - 69535:00

the team to kind of go beyond.

## 69535:00 - 69570:00

>> Is that sort of centralization versus

## 69570:00 - 69600:00

decentralization and pushing things to

## 69600:00 - 69635:00

the edges or that's not capturing the

## 69635:00 - 69645:00

idea?

## 69645:00 - 69680:00

>> I think it's decentralization combined

## 69680:00 - 69725:00

with like a sense of accountability. You

## 69725:00 - 69745:00

know, I I think as a company gets

## 69745:00 - 69790:00

bigger, how you can give people some

## 69790:00 - 69840:00

unit that they own and and have them

## 69840:00 - 69875:00

feel like, okay, I have flexibility to

## 69875:00 - 69915:00

go pursue these goals and I have goals.

## 69915:00 - 69940:00

You know, I think that that ends up

## 69940:00 - 69995:00

being um you know, underthought as

## 69995:00 - 70025:00

companies grow, but it's it's really at

## 70025:00 - 70050:00

the right time, right? Like for a

## 70050:00 - 70090:00

company with a 100 people, it's not an

## 70090:00 - 70125:00

issue, right? like the place you need

## 70125:00 - 70160:00

that is man maybe the management team as

## 70160:00 - 70190:00

as a company gets to be

## 70190:00 - 70220:00

>> a few thousand you have to have units

## 70220:00 - 70245:00

that are like that that are kind of

## 70245:00 - 70285:00

working in that way they can kind of

## 70285:00 - 70320:00

move quickly make decisions on their own

## 70320:00 - 70365:00

have a certain amount of autonomy etc.

## 70365:00 - 70405:00

And yet it's very natural to to lose

## 70405:00 - 70445:00

that as a company grows and you're

## 70445:00 - 70490:00

saying that at 100 people

## 70490:00 - 70515:00

unconsciously

## 70515:00 - 70560:00

that's just the way that it works 100%.

## 70560:00 - 70595:00

Yeah. And that as you scale

## 70595:00 - 70610:00

>> Yeah. Yeah. I think

## 70610:00 - 70640:00

>> unconsciously you lead to centralization

## 70640:00 - 70680:00

standal standardization process.

## 70680:00 - 70710:00

>> Yeah. That that's exactly right. Like

## 70710:00 - 70760:00

you know intuitively in a small company

## 70760:00 - 70815:00

the people who have a lot of freedom in

## 70815:00 - 70865:00

decisionm you know are close enough to

## 70865:00 - 70900:00

everything happening that you will just

## 70900:00 - 70945:00

do the thing that makes sense right and

## 70945:00 - 70970:00

you know as a company gets bigger you

## 70970:00 - 71015:00

you often lose that. Um you know so much

## 71015:00 - 71070:00

so that uh you know a common thing I

## 71070:00 - 71120:00

tell people is which sounds ridiculous

## 71120:00 - 71145:00

but it it actually is just very useful

## 71145:00 - 71185:00

is to tell I just tell them you know

## 71185:00 - 71215:00

neither I nor anybody on the management

## 71215:00 - 71265:00

team wants you to do something stupid.

## 71265:00 - 71290:00

So if you think you are doing something

## 71290:00 - 71320:00

that is stupid

## 71320:00 - 71385:00

don't just do it but come talk to us.

## 71385:00 - 71425:00

Uh, and you would think that that's not

## 71425:00 - 71465:00

needed, right? And and yet it often is

## 71465:00 - 71500:00

because people think, "Okay, we're

## 71500:00 - 71545:00

supposed to do this thing, right? And so

## 71545:00 - 71590:00

then they just go do it." And yet they

## 71590:00 - 71630:00

actually know something that means that

## 71630:00 - 71670:00

that's not a good idea. You know, I find

## 71670:00 - 71705:00

every time those things escalate,

## 71705:00 - 71750:00

something good happens. either

## 71750:00 - 71770:00

the management team learned something

## 71770:00 - 71800:00

about the problem they didn't know or

## 71800:00 - 71820:00

the person working on the problem

## 71820:00 - 71845:00

learned something about the global

## 71845:00 - 71875:00

context that they didn't know but would

## 71875:00 - 71910:00

need to know to get the right outcome

## 71910:00 - 71960:00

right and you know in a smaller company

## 71960:00 - 72000:00

I I feel like you have much less of that

## 72000:00 - 72045:00

because the management is so close to

## 72045:00 - 72060:00

what's happening

## 72060:00 - 72080:00

>> and you even as a CEO can hold

## 72080:00 - 72090:00

everything

## 72090:00 - 72115:00

>> in a larger company you have to execute

## 72115:00 - 72140:00

some kind of strategy so you're telling

## 72140:00 - 72180:00

people hey this is what we want without

## 72180:00 - 72210:00

understanding every implication of that

## 72210:00 - 72250:00

so you need um you know you need really

## 72250:00 - 72305:00

the the whole company trying to you know

## 72305:00 - 72345:00

optimize for the end outcome that you

## 72345:00 - 72390:00

actually care about not just do the

## 72390:00 - 72425:00

thing and and I do think that that

## 72425:00 - 72460:00

requires you know kind of creating some

## 72460:00 - 72515:00

units that have that type of thinking

## 72515:00 - 72555:00

and so that that's been you know that's

## 72555:00 - 72600:00

been important for us as the company has

## 72600:00 - 72640:00

grown up just trying to break units of

## 72640:00 - 72670:00

product that carry a revenue target that

## 72670:00 - 72695:00

can think of you know how are we

## 72695:00 - 72725:00

marketing our area, how are we getting

## 72725:00 - 72750:00

customers? They can't do everything

## 72750:00 - 72770:00

because of course they're sitting in a

## 72770:00 - 72805:00

system that handles some of the problems

## 72805:00 - 72840:00

for them, but it gives them, you know, a

## 72840:00 - 72880:00

certain level of accountability. And I

## 72880:00 - 72915:00

think it just really helps them think

## 72915:00 - 72950:00

through, you know, end to end what's

## 72950:00 - 72975:00

working or not working, why are

## 72975:00 - 73010:00

customers using this or not using this,

## 73010:00 - 73055:00

what's holding us back in growth, and

## 73055:00 - 73100:00

then, you know, that that becomes kind

## 73100:00 - 73145:00

of the point that can easily escalate to

## 73145:00 - 73175:00

the larger management team to unblock

## 73175:00 - 73200:00

things in the rest of the system. Do you

## 73200:00 - 73235:00

spend a significant amount of your time

## 73235:00 - 73265:00

working on making this happen in the

## 73265:00 - 73300:00

company or now it just kind of happened?

## 73300:00 - 73335:00

>> Yeah, I think it took us a couple years.

## 73335:00 - 73375:00

You know, inherently as you grow, you're

## 73375:00 - 73390:00

just kind of always in this

## 73390:00 - 73420:00

uncomfortable state where you're set up

## 73420:00 - 73450:00

for something

## 73450:00 - 73490:00

a few years ago and now you're doing

## 73490:00 - 73525:00

something slightly different. So yeah,

## 73525:00 - 73560:00

it was it was it took us a few years to

## 73560:00 - 73605:00

go from, you know, kind of a fully

## 73605:00 - 73640:00

centralized thing to having, you know,

## 73640:00 - 73670:00

effectively little product areas that

## 73670:00 - 73725:00

act like 45% of a company, right? You

## 73725:00 - 73770:00

know, they've got the GNA stuff all done

## 73770:00 - 73795:00

for them, but they have a revenue target

## 73795:00 - 73825:00

and they have some dedicated marketing

## 73825:00 - 73855:00

and they have, you know, a plan of how

## 73855:00 - 73880:00

they're going to be successful and a

## 73880:00 - 73910:00

plan of how they're going to grow and

## 73910:00 - 73955:00

dedicated sales support and so on. And

## 73955:00 - 73985:00

as you start to have more of that, you

## 73985:00 - 74015:00

can, you know, make it more real that

## 74015:00 - 74050:00

like, hey, you guys own this thing,

## 74050:00 - 74090:00

figure it out, you know, don't wait for

## 74090:00 - 74130:00

somebody to come to you with the, you

## 74130:00 - 74155:00

know, don't just assume you're

## 74155:00 - 74185:00

responsible for this narrow part. Like,

## 74185:00 - 74230:00

oh, I've done the product specs and I've

## 74230:00 - 74250:00

done the engineering and so and so's

## 74250:00 - 74275:00

done the design and hopefully it all

## 74275:00 - 74305:00

works. You know, really think through

## 74305:00 - 74330:00

whether it's going to work and solve all

## 74330:00 - 74360:00

the problems across that that are

## 74360:00 - 74375:00

required.

## 74375:00 - 74400:00

>> Good place to end. Thank you for the

## 74400:00 - 74410:00

conversation.

## 74410:00 - 74420:00

>> Yeah, my pleasure.

## 74420:00 - 74455:00

>> That was great. Really interesting.

## 74455:00+

Really enjoyed it.

