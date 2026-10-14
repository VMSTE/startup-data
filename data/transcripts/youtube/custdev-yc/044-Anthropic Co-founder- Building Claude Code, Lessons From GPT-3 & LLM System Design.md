---
source: https://www.youtube.com/watch?v=JdT78t1Offo
title: "Anthropic Co-founder: Building Claude Code, Lessons From GPT-3 & LLM
  System Design"
author: Y Combinator
date: 2025-08-19
views: 135042
description: >-
  Tom Brown co-founded Anthropic after helping build GPT-3 at OpenAI. A
  self-taught engineer, he went from getting a B-minus in linear algebra to
  becoming one of the key people behind AI's scaling breakthroughs. And his work
  is paying off. 


  Today, Anthropic's Claude is the go-to choice for developers, and his team is
  overseeing what he calls "humanity's largest infrastructure buildout ever." On
  this episode of The Lightcone, he discusses his unconventional path from YC
  founder to AI researcher, the discovery of scaling laws that changed
  everything, and his advice for young engineers entering AI today.


  Apply to Y Combinator: https://www.ycombinator.com/apply

  Work at a startup: https://www.ycombinator.com/jobs


  Chapters:

  0:00 - From Failure to Success

  2:30 - Early Startup Days at Linked Language

  4:12 - The Grouper Dating Experiment

  6:10 - Making the Leap to OpenAI

  8:42 - First Product Launch Challenges

  10:12 - Self-Teaching AI Research

  12:44 - Building GPT-3 Infrastructure

  15:44 - The Anthropic Spinoff

  18:23 - Early Days of Building Claude

  20:21 - The ChatGPT Wake-Up Call

  22:08 - Claude 3.5 Sonnet Breakthrough

  24:13 - Why Benchmarks Don't Tell the Whole Story

  26:20 - Claude Code's Secret Sauce

  28:51 - Building for the AI Agent

  31:11 - The Largest Infrastructure Buildout Ever

  32:46 - Multi-Chip Strategy

  34:38 - Advice for the Next Generation
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:42:51.239Z
---

# Anthropic Co-founder: Building Claude Code, Lessons From GPT-3 & LLM System Design

## 00:00 - 45:00

When we started out, we didn't seem like

## 45:00 - 110:00

we were going to be successful at all.

## 110:00 - 150:00

OpenAI had a billion dollars and like

## 150:00 - 185:00

all of these all of this star power and

## 185:00 - 230:00

we had seven co-founders in co like

## 230:00 - 255:00

trying to build something and we didn't

## 255:00 - 275:00

know if we were necessarily going to

## 275:00 - 295:00

make a product or what the products

## 295:00 - 320:00

would look like. One thing that's

## 320:00 - 360:00

interesting to look at is just that

## 360:00 - 385:00

humanity is on track for like the

## 385:00 - 415:00

largest infrastructure buildout of all

## 415:00 - 440:00

time. Tell us about the early days of

## 440:00 - 480:00

anthropic. So you had a general idea of

## 480:00 - 510:00

this sort of like long-term mission that

## 510:00 - 545:00

you wanted to do to, you know, not

## 545:00 - 580:00

destroy humanity, but like what did you

## 580:00 - 605:00

actually work on for the first year? How

## 605:00 - 655:00

did that converge on an actual product?

## 655:00 - 765:00

[Music]

## 765:00 - 795:00

Welcome back to another episode of The

## 795:00 - 820:00

Light Cone. Today we've got a real

## 820:00 - 860:00

treat, co-founder of Anthropic, Tom

## 860:00 - 870:00

Brown.

## 870:00 - 910:00

>> Excited to be here. So Tom, one of the

## 910:00 - 940:00

things that a lot of the people watching

## 940:00 - 980:00

uh would love to figure out is you got

## 980:00 - 1040:00

started in tech at the age of 21, fresh

## 1040:00 - 1090:00

from MIT. How does someone go from that

## 1090:00 - 1160:00

in 2009 to literally co-founding

## 1160:00 - 1210:00

something as important as anthropic?

## 1210:00 - 1255:00

>> Summer 2009, linked language. Two of my

## 1255:00 - 1285:00

friends had started that out. I think

## 1285:00 - 1320:00

they had seen one of our other friends,

## 1320:00 - 1355:00

Kyle Vote, kind of do a YC company. And

## 1355:00 - 1380:00

so it was in the water that that's a

## 1380:00 - 1410:00

thing that we could try to do. They

## 1410:00 - 1440:00

started out I was the first employee

## 1440:00 - 1475:00

back then. Yeah. You guys let me join

## 1475:00 - 1505:00

for all the dinners and stuff like that

## 1505:00 - 1530:00

too. I could have instead gone to like a

## 1530:00 - 1555:00

big tech company or something like that.

## 1555:00 - 1605:00

And I think probably just as a software

## 1605:00 - 1630:00

engineer, I might have learned more

## 1630:00 - 1670:00

software engineering skills. But I think

## 1670:00 - 1735:00

by being there with the other

## 1735:00 - 1765:00

co-founders without anyone telling us

## 1765:00 - 1800:00

what to do basically like we had to

## 1800:00 - 1835:00

figure out how to live, how to like the

## 1835:00 - 1870:00

company would die by default. I think in

## 1870:00 - 1890:00

school there was a lot of like a feeling

## 1890:00 - 1915:00

of more of people would give me tasks

## 1915:00 - 1940:00

and I would do the tasks. It's kind of

## 1940:00 - 1975:00

like a dog waiting for like food to be

## 1975:00 - 2000:00

like fed to them in their bowl or

## 2000:00 - 2025:00

something like that. And I think for

## 2025:00 - 2050:00

that company it was more like wolves and

## 2050:00 - 2090:00

we have to like hunt our real like food

## 2090:00 - 2115:00

otherwise like we're our kids are going

## 2115:00 - 2140:00

to starve or something like that. I

## 2140:00 - 2180:00

think that that mindset I think has been

## 2180:00 - 2220:00

like the most valuable mindset that

## 2220:00 - 2255:00

shift that I've had for trying to do

## 2255:00 - 2295:00

like bigger more exciting things.

## 2295:00 - 2340:00

>> Yeah. Big tech just teaches you to work

## 2340:00 - 2385:00

at a big tech company whereas uh it's

## 2385:00 - 2410:00

much more fun to be a wolf.

## 2410:00 - 2445:00

>> Yeah. How did you go from like so

## 2445:00 - 2485:00

working at friend's startup to then you

## 2485:00 - 2535:00

started your own one? So linked was um

## 2535:00 - 2580:00

we ran the company for a bit. I ended up

## 2580:00 - 2620:00

going back to to school afterwards and

## 2620:00 - 2670:00

then when I left school I went to this

## 2670:00 - 2685:00

company Mopub

## 2685:00 - 2715:00

>> the mobile advertising thing right?

## 2715:00 - 2740:00

>> Yeah. Yeah. I was like the first

## 2740:00 - 2775:00

engineer there. I was like okay I want

## 2775:00 - 2805:00

to be a wolf but like I was really bad

## 2805:00 - 2855:00

at programming also. I was like very

## 2855:00 - 2895:00

very struggling as like a a like

## 2895:00 - 2925:00

software engineer. I know I want to do

## 2925:00 - 2945:00

more but I don't know how to do it yet.

## 2945:00 - 2975:00

And so I think that was kind of like a

## 2975:00 - 3000:00

experience getting to scale something.

## 3000:00 - 3040:00

Winter 2012, one of my friends who was

## 3040:00 - 3090:00

my smartest friend from college pitched

## 3090:00 - 3130:00

me on let's go and start a YC company.

## 3130:00 - 3165:00

We did at the time solid stage. This was

## 3165:00 - 3205:00

before Docker existed. And so the idea

## 3205:00 - 3240:00

was try to make it easier to do DevOps,

## 3240:00 - 3270:00

but Docker doesn't exist. So it's going

## 3270:00 - 3310:00

to be a more flexible Heroku, which

## 3310:00 - 3345:00

basically meant a more complicated like

## 3345:00 - 3385:00

Heroku. And so we I remember we like we

## 3385:00 - 3425:00

interviewed with you guys. I think folks

## 3425:00 - 3450:00

didn't really understand what we were

## 3450:00 - 3470:00

trying to build. I think we didn't

## 3470:00 - 3485:00

really understand what we were trying to

## 3485:00 - 3500:00

build that much

## 3500:00 - 3525:00

>> when you're trying to do something new.

## 3525:00 - 3560:00

That's actually sometimes common.

## 3560:00 - 3585:00

>> Yeah. I think we were an outlier there

## 3585:00 - 3605:00

cuz we like did our interviews and then

## 3605:00 - 3635:00

we got called back driving back to San

## 3635:00 - 3675:00

Francisco and TLB had written on the

## 3675:00 - 3725:00

board like an angry frowny face and what

## 3725:00 - 3775:00

are you actually going to build? And so

## 3775:00 - 3820:00

he like wanted us to explain that. I

## 3820:00 - 3855:00

guess we explained it enough or he was

## 3855:00 - 3875:00

just like these guys still don't know

## 3875:00 - 3900:00

what they're doing but maybe they'll

## 3900:00 - 3945:00

figure it out. Halfway through I kind of

## 3945:00 - 3975:00

felt I still didn't actually understand

## 3975:00 - 4015:00

what we were going to build and how we

## 4015:00 - 4045:00

would attach a mission to it that like I

## 4045:00 - 4090:00

wanted to to work on for my whole life.

## 4090:00 - 4095:00

>> Yeah.

## 4095:00 - 4145:00

>> Um and so I left PG actually introed me

## 4145:00 - 4185:00

to Michael Waxman who was the grouper

## 4185:00 - 4200:00

founder.

## 4200:00 - 4210:00

>> Yeah. So,

## 4210:00 - 4260:00

>> so Grouper was a dating app only it was

## 4260:00 - 4300:00

novel in that you had what three guys

## 4300:00 - 4325:00

and three girls. Y

## 4325:00 - 4355:00

>> this was before AI in a lot of ways. So

## 4355:00 - 4385:00

there was like a set of a team of people

## 4385:00 - 4425:00

who would manually link people up,

## 4425:00 - 4475:00

right? And they'd meet up at a bar and

## 4475:00 - 4500:00

shenanigans would ensue.

## 4500:00 - 4555:00

>> Yes. Reliably shenanigans. People didn't

## 4555:00 - 4575:00

always have a great time. I think you

## 4575:00 - 4605:00

went you went on a couple group.

## 4605:00 - 4625:00

>> Okay.

## 4625:00 - 4660:00

The pitch for grouper for me for like

## 4660:00 - 4705:00

why I was excited for it was just I was

## 4705:00 - 4765:00

like an incredibly awkward kid. What I

## 4765:00 - 4800:00

wanted to do was to basically have a

## 4800:00 - 4845:00

thing that lets awkward people like me

## 4845:00 - 4895:00

go out and talk to other people for me

## 4895:00 - 4930:00

to talk to girls and feel like I was

## 4930:00 - 4955:00

safe doing it with like my friends

## 4955:00 - 4980:00

around and stuff like that. And so I

## 4980:00 - 5000:00

think who were going to be our employees

## 5000:00 - 5030:00

was important. I did like all of our

## 5030:00 - 5050:00

engineering interviews. who would take

## 5050:00 - 5085:00

someone. The only person who went on

## 5085:00 - 5125:00

more was Greg Brockman.

## 5125:00 - 5155:00

>> I think he had I think he had a he had a

## 5155:00 - 5185:00

phase where like every single week

## 5185:00 - 5240:00

>> he would go and like post on uh Slack or

## 5240:00 - 5260:00

Hip Chat at the time.

## 5260:00 - 5275:00

>> New York and he was hanging out at the

## 5275:00 - 5305:00

Recurse Center during this period. I

## 5305:00 - 5310:00

think

## 5310:00 - 5355:00

>> Oh, I I think he was at Stripe. Maybe

## 5355:00 - 5380:00

maybe for part of it he was at Recurse.

## 5380:00 - 5415:00

Yeah. But he also had uh I think just

## 5415:00 - 5445:00

like a phase where he would just at

## 5445:00 - 5470:00

Stripe he would just like post in their

## 5470:00 - 5490:00

thing every like I'm going on grouper

## 5490:00 - 5530:00

who's going for like a whole year.

## 5530:00 - 5560:00

So I I ended up being close with Greg

## 5560:00 - 5585:00

which which ended up being a connection

## 5585:00 - 5600:00

to the open AAI.

## 5600:00 - 5625:00

>> What was the journey like? Because you

## 5625:00 - 5680:00

started as u you just graduated from MIT

## 5680:00 - 5730:00

CS. You were 21. You became first an

## 5730:00 - 5770:00

early employee for all these YC

## 5770:00 - 5795:00

startups. Then you started your company

## 5795:00 - 5860:00

just a couple years later. And what was

## 5860:00 - 5895:00

the path for you to eventually become

## 5895:00 - 5920:00

the co-founder of Anthropic? It was like

## 5920:00 - 5960:00

a long path but it's pretty impressive.

## 5960:00 - 5985:00

How how did you get there? I mean, it

## 5985:00 - 6020:00

sounds like getting in touch with Greg

## 6020:00 - 6065:00

at that moment moment.

## 6065:00 - 6095:00

>> Uh, and then you were one of the first

## 6095:00 - 6125:00

uh, you know, a couple dozen people to

## 6125:00 - 6165:00

join OpenAI as a result.

## 6165:00 - 6240:00

>> Yeah. So, I left Grouper 2014,

## 6240:00 - 6315:00

June 2014, and I joined OpenAI

## 6315:00 - 6360:00

I think a year later. I tried to like

## 6360:00 - 6390:00

build up courage to make the switch to

## 6390:00 - 6435:00

be a to try to learn AI research. At the

## 6435:00 - 6460:00

time I was like, "Okay, it seems like

## 6460:00 - 6490:00

sometime in our lifetimes we might end

## 6490:00 - 6530:00

up making transformative AI. If we do,

## 6530:00 - 6555:00

that would be the biggest thing. Maybe

## 6555:00 - 6585:00

there's some way that I could help out,

## 6585:00 - 6645:00

but also I got like a B minus in linear

## 6645:00 - 6685:00

algebra in college." And so it seemed

## 6685:00 - 6710:00

like at the time you needed to be just

## 6710:00 - 6740:00

top superstar in order to try to help

## 6740:00 - 6765:00

out with that at all. And so I think I

## 6765:00 - 6790:00

had like a lot of uncertainty about

## 6790:00 - 6830:00

whether I would be able to help. And

## 6830:00 - 6855:00

also I'd had some success with startups.

## 6855:00 - 6885:00

And so a lot of me was just like rather

## 6885:00 - 6915:00

than trying to retool at this like I

## 6915:00 - 6940:00

could try to do another startup or

## 6940:00 - 6970:00

something like that. I feel like in that

## 6970:00 - 7015:00

period um going to work on AI research

## 7015:00 - 7050:00

which is not seen as like a ser like not

## 7050:00 - 7080:00

like a practically serious thing to do

## 7080:00 - 7100:00

and you're in a world where it's like

## 7100:00 - 7120:00

people try and build companies and do

## 7120:00 - 7140:00

these like really practical things like

## 7140:00 - 7165:00

what did your were your friends like oh

## 7165:00 - 7180:00

that's really cool you're going to go

## 7180:00 - 7215:00

work on AI stuff or was it

## 7215:00 - 7235:00

>> not really

## 7235:00 - 7255:00

>> I think my friends were like that sounds

## 7255:00 - 7300:00

that sounds weird and bad kind of like

## 7300:00 - 7325:00

it it doesn't really seem like it

## 7325:00 - 7355:00

doesn't seem like like AI safety is a

## 7355:00 - 7365:00

thing we should be wear like

## 7365:00 - 7395:00

overpopulation on Mars doesn't make any

## 7395:00 - 7425:00

sense and my friends were also just like

## 7425:00 - 7440:00

I don't know if you're going to be good

## 7440:00 - 7485:00

at that tough. I think that for that

## 7485:00 - 7520:00

reason, I think I didn't try very hard

## 7520:00 - 7550:00

for I like kind of flip-flopped on it

## 7550:00 - 7580:00

for like 6 months trying to build up

## 7580:00 - 7600:00

courage to do it.

## 7600:00 - 7625:00

>> And what were you specifically at this

## 7625:00 - 7650:00

point? Like you're reading research

## 7650:00 - 7685:00

papers like what it what does it look

## 7685:00 - 7695:00

like?

## 7695:00 - 7730:00

>> Yeah. So, first I was just kind of

## 7730:00 - 7760:00

hanging out. I built like an art car for

## 7760:00 - 7790:00

Titanic 7 and stuff like that.

## 7790:00 - 7810:00

>> Oh, that was fun. Yeah.

## 7810:00 - 7850:00

>> Yeah. So I I spent like a whole summer

## 7850:00 - 7880:00

like 3 months after Grouper doing that

## 7880:00 - 7900:00

cuz honestly I was I was like kind of

## 7900:00 - 7935:00

burned out for Grouper where I know

## 7935:00 - 7955:00

startups like the highs are high like

## 7955:00 - 7990:00

the lows are low and we weren't working

## 7990:00 - 8015:00

at the end. Our business wasn't

## 8015:00 - 8050:00

succeeding. Our revenue was going down

## 8050:00 - 8080:00

but I my main job still was like

## 8080:00 - 8105:00

recruiting engineers and so I had to

## 8105:00 - 8130:00

like pitch them on this dream that I had

## 8130:00 - 8150:00

had but I like no longer really

## 8150:00 - 8200:00

>> sounds like a death march. And so I was

## 8200:00 - 8220:00

super burnt out and I was like, "Okay,

## 8220:00 - 8250:00

Tom, like chill out, do some yoga, like

## 8250:00 - 8280:00

do some CrossFit, like build an art

## 8280:00 - 8290:00

car." And

## 8290:00 - 8315:00

>> what was the hindsight? Like, you know,

## 8315:00 - 8345:00

hindsight's 2020. What's the

## 8345:00 - 8380:00

retrospective on like Grouper obviously

## 8380:00 - 8410:00

attracted all these really, really smart

## 8410:00 - 8445:00

people. The graphs were up and to the

## 8445:00 - 8480:00

right and then it flatlined and maybe

## 8480:00 - 8515:00

started declining. What happened?

## 8515:00 - 8545:00

>> I think that when we started the

## 8545:00 - 8585:00

competition was like, "Okay, Cupid.

## 8585:00 - 8605:00

>> It was all web- based."

## 8605:00 - 8645:00

>> All web- based. The main problem that I

## 8645:00 - 8685:00

think we were solving was the it's hard

## 8685:00 - 8710:00

to like go and put yourself out there

## 8710:00 - 8745:00

and go like talk to someone new and they

## 8745:00 - 8775:00

might just be like I don't want to talk

## 8775:00 - 8805:00

to you. You seem weird. And so we solved

## 8805:00 - 8850:00

that by just blind matching. Tinder came

## 8850:00 - 8890:00

out while we were doing grouper and

## 8890:00 - 8920:00

Tinder solved that same problem with

## 8920:00 - 8955:00

both people have to show interest before

## 8955:00 - 8980:00

you get matched. So there's also no

## 8980:00 - 9005:00

worries about getting rejected. And I

## 9005:00 - 9030:00

think that they just had better that was

## 9030:00 - 9060:00

a better solution to that same problem.

## 9060:00 - 9090:00

So good work Tinder. Good work all the

## 9090:00 - 9120:00

swipers. I think that that that solved

## 9120:00 - 9150:00

the like mission that we were trying to

## 9150:00 - 9180:00

solve better than we solved it.

## 9180:00 - 9200:00

>> And then yeah, like when did you get

## 9200:00 - 9240:00

serious about AI and just how did you

## 9240:00 - 9265:00

approach

## 9265:00 - 9280:00

it?

## 9280:00 - 9305:00

>> Three months of like kind of playing and

## 9305:00 - 9340:00

having fun and then I ran out of money

## 9340:00 - 9385:00

also when I had like my personal runway.

## 9385:00 - 9430:00

I I ran out and so I was like, okay, I

## 9430:00 - 9480:00

think that I'm going to need 6 months of

## 9480:00 - 9515:00

stealth study to have a shot at getting

## 9515:00 - 9560:00

a job. At that point it was Deep Mind or

## 9560:00 - 9590:00

Google Brain were the two places to do

## 9590:00 - 9625:00

work there or MIRI. Merie was the third

## 9625:00 - 9655:00

one that I was like looking at. So I was

## 9655:00 - 9685:00

like if I want to help out with that

## 9685:00 - 9725:00

those are the three places to look at. I

## 9725:00 - 9745:00

don't have any of the skills yet. I need

## 9745:00 - 9785:00

six months of self-study to feel like I

## 9785:00 - 9810:00

would not be a drag on them and like

## 9810:00 - 9830:00

actually be helping instead.

## 9830:00 - 9885:00

>> Can you um maybe explain a bit what was

## 9885:00 - 9905:00

that self study like? Because I'm sure

## 9905:00 - 9930:00

there's a lot of software engineers

## 9930:00 - 9955:00

right now in their 20s are looking to

## 9955:00 - 10005:00

retool to become AI researchers. What

## 10005:00 - 10030:00

was what was that six months like? Even

## 10030:00 - 10070:00

though as you said you had uh gotten a B

## 10070:00 - 10100:00

minus in linear algebra which is like

## 10100:00 - 10105:00

core

## 10105:00 - 10135:00

>> might have been a C++. I'm not I should

## 10135:00 - 10170:00

check.

## 10170:00 - 10180:00

I'm going to keep telling

## 10180:00 - 10200:00

>> that's pretty impressive where where you

## 10200:00 - 10205:00

got to.

## 10205:00 - 10235:00

>> Yeah. Yeah. It turned out okay. First I

## 10235:00 - 10265:00

did a contract actually with Twitch um

## 10265:00 - 10310:00

and like earned like enough to have that

## 10310:00 - 10335:00

six months of runway. So I did like

## 10335:00 - 10355:00

three-month contract with Twitch and

## 10355:00 - 10405:00

then I made a a plan to self-study. I

## 10405:00 - 10430:00

don't think it's the right plan now for

## 10430:00 - 10465:00

people too at least 2015. What did it

## 10465:00 - 10495:00

looked like? It was like take a Corsera

## 10495:00 - 10555:00

course on machine learning, try to solve

## 10555:00 - 10600:00

some Kaggle projects, read linear

## 10600:00 - 10650:00

algebra done right, and uh I had a

## 10650:00 - 10690:00

statistics textbook. I think I had YC

## 10690:00 - 10745:00

alumni credits and so I bought like a

## 10745:00 - 10770:00

GPU

## 10770:00 - 10815:00

and I would like SSH into the GPU to

## 10815:00 - 10845:00

like work through my courses for it.

## 10845:00 - 10875:00

>> And this is right after Yeah, it was

## 10875:00 - 10910:00

already after Alex Knack, right?

## 10910:00 - 10935:00

>> This is after Alex Neck. Yeah. So I was

## 10935:00 - 10970:00

mostly doing image image classification

## 10970:00 - 11000:00

stuff that I was trying to learn was

## 11000:00 - 11025:00

like the thing that all the courses

## 11025:00 - 11040:00

would teach you to do.

## 11040:00 - 11075:00

>> How did you get the open AI job?

## 11075:00 - 11105:00

>> Because you were one of the few

## 11105:00 - 11135:00

engineers. It was mostly researchers and

## 11135:00 - 11160:00

they had pretty stacked team of

## 11160:00 - 11170:00

researchers.

## 11170:00 - 11225:00

>> I messaged Greg um as soon as OpenAI was

## 11225:00 - 11250:00

announced and I was like I'd love to

## 11250:00 - 11290:00

help out in some way. I got a B minus in

## 11290:00 - 11330:00

my linear algebra but I know some

## 11330:00 - 11350:00

engineering. I've done a bit of

## 11350:00 - 11375:00

distributed systems work. if you guys

## 11375:00 - 11405:00

need help, I'm like happy to mop floors

## 11405:00 - 11435:00

if if you guys need I want to help out,

## 11435:00 - 11470:00

however. And I think Greg was like,

## 11470:00 - 11500:00

yeah, I think there's like a posity of

## 11500:00 - 11545:00

people who he said posity, too. I was

## 11545:00 - 11580:00

like, fancy word there. There's a posity

## 11580:00 - 11620:00

of people who know both machine learning

## 11620:00 - 11645:00

and distributed systems. So, like, yes,

## 11645:00 - 11670:00

you should do that. I think he

## 11670:00 - 11705:00

introduced me to Peter Aiel also to help

## 11705:00 - 11735:00

me put together like a little course for

## 11735:00 - 11775:00

myself, too. And then I checked in on

## 11775:00 - 11805:00

with him, I think every month or

## 11805:00 - 11830:00

something. And then after a couple

## 11830:00 - 11860:00

months he was like oh we actually have a

## 11860:00 - 11895:00

project which is uh we need to put

## 11895:00 - 11930:00

together we want to play a game like

## 11930:00 - 11970:00

play games can you help uh make

## 11970:00 - 12015:00

Starcraft environment and so I joined to

## 12015:00 - 12045:00

like help them with the Starcraft uh

## 12045:00 - 12080:00

environment. So that that ended up I

## 12080:00 - 12105:00

think getting my foot in the door. I I

## 12105:00 - 12135:00

didn't do any machine learning work with

## 12135:00 - 12180:00

them for the first nine months that I

## 12180:00 - 12195:00

was there basically.

## 12195:00 - 12230:00

>> And what did OpenAI feel like at this

## 12230:00 - 12260:00

point? Like had it raised much funding?

## 12260:00 - 12280:00

Did it have like an office? which is

## 12280:00 - 12305:00

what will do it. Did it feel like a

## 12305:00 - 12315:00

startup?

## 12315:00 - 12345:00

>> So it was in the chocolate on top of the

## 12345:00 - 12380:00

dandelion chocolate factory. Um

## 12380:00 - 12415:00

>> this is after Greg's apartment. That's

## 12415:00 - 12420:00

the

## 12420:00 - 12440:00

>> after Greg's apartment. Yeah. So like

## 12440:00 - 12460:00

right after Greg's apartment in the

## 12460:00 - 12490:00

chocolate factory when it kicked off,

## 12490:00 - 12515:00

right? It was like a billion dollars of

## 12515:00 - 12550:00

committed funding from Elon. It felt

## 12550:00 - 12575:00

like it was like very solid.

## 12575:00 - 12625:00

>> The other interesting milestone for you

## 12625:00 - 12680:00

was when you got to build a lot of the

## 12680:00 - 12735:00

engineering around the training for GBT.

## 12735:00 - 12755:00

Yeah. For GP3

## 12755:00 - 12800:00

>> for and how how what was that? Because

## 12800:00 - 12845:00

you got from GPT2 was in TPUs, right?

## 12845:00 - 12850:00

>> Yep.

## 12850:00 - 12890:00

>> And the big breakthrough in GPT3 was

## 12890:00 - 12930:00

like use more compute and using GPUs.

## 12930:00 - 12965:00

>> Yep. So I ended up working at OpenAI for

## 12965:00 - 13010:00

a year, left, went to Google Brain for a

## 13010:00 - 13070:00

year, came back, and then GPT3 was 2018

## 13070:00 - 13110:00

through 2019 was like building up to

## 13110:00 - 13150:00

GP3, which exactly as you said was like

## 13150:00 - 13175:00

scaling things up. I think that like

## 13175:00 - 13210:00

Daario had seen the big trend of scaling

## 13210:00 - 13245:00

laws basically. You published a paper

## 13245:00 - 13255:00

for that.

## 13255:00 - 13260:00

>> Yeah. Yeah.

## 13260:00 - 13305:00

>> And that's like a pretty important paper

## 13305:00 - 13345:00

that now has withtood the test of time

## 13345:00 - 13385:00

and we're living now the dream of it.

## 13385:00 - 13410:00

Definitely like seeing that line of

## 13410:00 - 13440:00

reliably you get more intelligence if

## 13440:00 - 13465:00

you spend more compute with the right

## 13465:00 - 13495:00

recipe was the main thing that was at

## 13495:00 - 13520:00

least for me was like this is a thing

## 13520:00 - 13555:00

that's like happening happening now cuz

## 13555:00 - 13580:00

you could look even at the time we

## 13580:00 - 13620:00

weren't spending very much money on the

## 13620:00 - 13665:00

on the training jobs at the time and you

## 13665:00 - 13700:00

could see that there was scaling there

## 13700:00 - 13735:00

and then also Danny Hernandez did a

## 13735:00 - 13765:00

paper at the time that showed uh how

## 13765:00 - 13800:00

much cheaper algorithmic efficiency was

## 13800:00 - 13840:00

making stuff over time too and like

## 13840:00 - 13875:00

those two things stack together that was

## 13875:00 - 13895:00

like, oh wow, we're going to get a lot

## 13895:00 - 13935:00

more intelligence over the next few

## 13935:00 - 13945:00

years.

## 13945:00 - 13990:00

>> So, it was noteworthy and surprising

## 13990:00 - 14020:00

when you saw it.

## 14020:00 - 14045:00

>> Yeah. And I I think the thing that

## 14045:00 - 14060:00

seemed the weirdest to me is like I'm

## 14060:00 - 14080:00

not a physicist, but like all these

## 14080:00 - 14110:00

physicists were were doing this stuff.

## 14110:00 - 14140:00

The like original scaling laws paper

## 14140:00 - 14170:00

just the like very straight line over

## 14170:00 - 14210:00

like 12 orders of magnitude. I'm just

## 14210:00 - 14250:00

like 12 orders of magnitude is like just

## 14250:00 - 14285:00

like a stupidly large amount of I've

## 14285:00 - 14310:00

like never seen anything go over 12

## 14310:00 - 14335:00

orders of magnitude. that convinced me

## 14335:00 - 14380:00

to definitely pivot all of my work into

## 14380:00 - 14410:00

scaling which I I hadn't been doing

## 14410:00 - 14420:00

before.

## 14420:00 - 14455:00

>> Can I ask a like kind of lay person

## 14455:00 - 14480:00

question? I mean

## 14480:00 - 14530:00

>> is it fair to say that the scaling law

## 14530:00 - 14555:00

might show up in all of these other

## 14555:00 - 14600:00

domains then they're like are there like

## 14600:00 - 14650:00

two five 100 10,000 domains where the

## 14650:00 - 14680:00

scaling law could hold that we're just

## 14680:00 - 14700:00

not investing into?

## 14700:00 - 14750:00

>> Yeah. So I think in physics scaling laws

## 14750:00 - 14775:00

hold all over the place which I didn't

## 14775:00 - 14815:00

know at the time but um within physics

## 14815:00 - 14840:00

like there's a whole field called

## 14840:00 - 14880:00

phenomenology that basically looks at

## 14880:00 - 14930:00

various aspects of the world and then

## 14930:00 - 14960:00

does those types of fits and they they

## 14960:00 - 14990:00

find these like power law distributions

## 14990:00 - 15030:00

all over the all over the place. This

## 15030:00 - 15070:00

was like I think the first one that I

## 15070:00 - 15115:00

had ever seen in a um like computer

## 15115:00 - 15160:00

science adjacent thing which I I think

## 15160:00 - 15200:00

was like interesting and surprising and

## 15200:00 - 15230:00

>> and at the time it was people were mad

## 15230:00 - 15260:00

about it. They actually were like you're

## 15260:00 - 15300:00

throwing money at GPUs or just like

## 15300:00 - 15330:00

wasting money. This is very wasteful.

## 15330:00 - 15345:00

Yeah. That was sort of

## 15345:00 - 15380:00

>> People are still mad about that.

## 15380:00 - 15420:00

>> Yes. Different people now but still

## 15420:00 - 15435:00

people mad about it.

## 15435:00 - 15455:00

>> Yeah. Yeah. I guess. Yeah. The

## 15455:00 - 15480:00

researchers were mad at that too where

## 15480:00 - 15510:00

it's like it's it's not elegant. you're

## 15510:00 - 15545:00

just like brute forcing it. The like

## 15545:00 - 15595:00

jester cap like stack more layers like

## 15595:00 - 15620:00

which I think I think like anthropics

## 15620:00 - 15650:00

slogan I think is like do the stupid

## 15650:00 - 15675:00

thing that works. That was a thing where

## 15675:00 - 15705:00

like this was very clearly the very

## 15705:00 - 15735:00

stupid thing that that works.

## 15735:00 - 15780:00

>> Can you uh tell us then how you ended up

## 15780:00 - 15815:00

collecting the last infinity stone

## 15815:00 - 15855:00

>> with? Yeah, with Enthropic because

## 15855:00 - 15880:00

there's very few people in the world

## 15880:00 - 15910:00

that have basically worked at OpenAI,

## 15910:00 - 15960:00

deep mind and anthropic and you were

## 15960:00 - 15990:00

part of the team that spun off from

## 15990:00 - 16005:00

GPD3.

## 16005:00 - 16010:00

>> Yeah.

## 16010:00 - 16055:00

>> And then started Anthropic. So how was

## 16055:00 - 16070:00

how was that jump?

## 16070:00 - 16100:00

>> There were two teams there. That was the

## 16100:00 - 16135:00

safety or and the scaling or were the

## 16135:00 - 16190:00

two orgs that reported into Daario and

## 16190:00 - 16245:00

Daniela. I think we had just like worked

## 16245:00 - 16275:00

together extremely well. One thing I

## 16275:00 - 16305:00

think that was great both at OpenAI and

## 16305:00 - 16345:00

and at Anthropic was just like we had a

## 16345:00 - 16380:00

culture where like everything is on

## 16380:00 - 16415:00

Slack 100% of things on Slack. And

## 16415:00 - 16455:00

within that all public channels, great

## 16455:00 - 16490:00

communication. I think that that group

## 16490:00 - 16525:00

also was the group that took the scaling

## 16525:00 - 16565:00

laws the most seriously where it was

## 16565:00 - 16585:00

like okay like this actually is going to

## 16585:00 - 16620:00

be transformative. there's going to be a

## 16620:00 - 16665:00

handoff where like humanity will hand

## 16665:00 - 16715:00

off control to transformative AI AI at

## 16715:00 - 16740:00

some point and hopefully like they'll be

## 16740:00 - 16765:00

aligned with us and like that'll be a

## 16765:00 - 16810:00

good transition that goes well but it

## 16810:00 - 16835:00

might not be the stakes are incredibly

## 16835:00 - 16870:00

high and so I think that group was very

## 16870:00 - 16900:00

focused on like how do we make sure that

## 16900:00 - 16950:00

that's taken seriously enough and that

## 16950:00 - 16975:00

like we've built an institution that can

## 16975:00 - 17010:00

handle the weight of that that ended up

## 17010:00 - 17045:00

being the core group that left to join

## 17045:00 - 17075:00

Anthropic and I think I think it wasn't

## 17075:00 - 17105:00

clear at all to me that like that was

## 17105:00 - 17130:00

the right thing for the world at the

## 17130:00 - 17160:00

time. In hindsight now, it seems like

## 17160:00 - 17190:00

that was a good choice. I think what was

## 17190:00 - 17215:00

kind of cool then too is when we started

## 17215:00 - 17270:00

out, we didn't seem like we were going

## 17270:00 - 17340:00

to be successful at all. OpenAI had a

## 17340:00 - 17370:00

billion dollars and like all of these

## 17370:00 - 17410:00

all of this star power and we had seven

## 17410:00 - 17450:00

co-founders in COVID like trying to

## 17450:00 - 17470:00

build something and we didn't know if we

## 17470:00 - 17495:00

were necessarily going to make a product

## 17495:00 - 17520:00

or what the products would look like.

## 17520:00 - 17560:00

And so I think that what was interesting

## 17560:00 - 17600:00

from that too is that all of the initial

## 17600:00 - 17630:00

people who joined were there for the

## 17630:00 - 17660:00

mission too. They all could have worked

## 17660:00 - 17710:00

somewhere else for more prestige, more

## 17710:00 - 17735:00

more more money. People would have known

## 17735:00 - 17760:00

what they were doing etc.

## 17760:00 - 17780:00

>> Well stayed at that opening eye

## 17780:00 - 17790:00

basically.

## 17790:00 - 17825:00

>> Exactly. Yeah. That that exactly that's

## 17825:00 - 17850:00

been an interesting thing then that I

## 17850:00 - 17875:00

think has been like the key to like

## 17875:00 - 17910:00

letting our culture or like let our org

## 17910:00 - 17945:00

scale. We're like 2,000 people now but

## 17945:00 - 17970:00

we still have a thing where it doesn't

## 17970:00 - 18000:00

seem like politics have creeped in. And

## 18000:00 - 18025:00

I think a lot of that is like the first

## 18025:00 - 18055:00

hundred people all were just there for

## 18055:00 - 18080:00

the mission. So like if something starts

## 18080:00 - 18100:00

to go wrong, they'll like raise their

## 18100:00 - 18125:00

hand and be like, "It seems like this

## 18125:00 - 18150:00

person might not be acting for the for

## 18150:00 - 18200:00

the mission." YC's next batch is now

## 18200:00 - 18235:00

taking applications. Got a startup in

## 18235:00 - 18290:00

you? Apply at y combinator.com/apply.

## 18290:00 - 18330:00

It's never too early and filling out the

## 18330:00 - 18375:00

app will level up your idea. Okay, back

## 18375:00 - 18390:00

to the video.

## 18390:00 - 18415:00

>> Hey, tell us about the early days of

## 18415:00 - 18450:00

anthropic. So the the seven you broke

## 18450:00 - 18500:00

off from open AI, you had a general idea

## 18500:00 - 18540:00

of the sort of like

## 18540:00 - 18565:00

long-term mission that you wanted to do

## 18565:00 - 18610:00

to you know not destroy humanity but

## 18610:00 - 18655:00

like how did what did you actually work

## 18655:00 - 18680:00

on for the first year? How did that

## 18680:00 - 18730:00

converge on an actual product? So first

## 18730:00 - 18775:00

year the main thing that I tried to do

## 18775:00 - 18790:00

was just build the training

## 18790:00 - 18820:00

infrastructure that we needed to train a

## 18820:00 - 18850:00

model and then get the compute that we

## 18850:00 - 18875:00

needed to train the model. Those were

## 18875:00 - 18910:00

like my two main projects. all the other

## 18910:00 - 18930:00

things that you need to do when you're

## 18930:00 - 18975:00

like starting up a company too. So like

## 18975:00 - 19010:00

set up a Brex account and like I don't

## 19010:00 - 19040:00

know like all all of that all of that

## 19040:00 - 19060:00

stuff. We started out with seven

## 19060:00 - 19110:00

co-founders. Within like a few months I

## 19110:00 - 19170:00

think like 25 folks from OpenAI um

## 19170:00 - 19200:00

overall had joined. So we had like a

## 19200:00 - 19225:00

pretty substantial team that like

## 19225:00 - 19245:00

already knew how to work together too.

## 19245:00 - 19290:00

And so that helped us get up and running

## 19290:00 - 19300:00

faster.

## 19300:00 - 19325:00

>> And at what point did you launch the

## 19325:00 - 19355:00

first product and when did things begin

## 19355:00 - 19390:00

to actually start working? So the first

## 19390:00 - 19420:00

product that we launched was after

## 19420:00 - 19480:00

chatgpt. We had like a maybe nine months

## 19480:00 - 19525:00

before chat gpt. We had a slackbot

## 19525:00 - 19555:00

version of like claude one.

## 19555:00 - 19600:00

>> Oh yeah, we had that in the YC uh slack

## 19600:00 - 19610:00

actually.

## 19610:00 - 19625:00

>> Yeah. Yeah.

## 19625:00 - 19660:00

>> Yeah. I remember like Tom Blfield adding

## 19660:00 - 19700:00

all of you guys to it.

## 19700:00 - 19720:00

>> It was really cool.

## 19720:00 - 19755:00

>> And then I think that at the time though

## 19755:00 - 19780:00

we didn't know whether or not we wanted

## 19780:00 - 19820:00

to launch it as a product. We didn't

## 19820:00 - 19860:00

know if doing so would be good for the

## 19860:00 - 19890:00

world at the time. I think we hadn't

## 19890:00 - 19910:00

really thought through our theory of

## 19910:00 - 19935:00

impact that much for like how we

## 19935:00 - 19965:00

actually will make stuff work well.

## 19965:00 - 19990:00

Plus, I think actually in hindsight like

## 19990:00 - 20020:00

if we had tried to launch it, we like

## 20020:00 - 20045:00

wouldn't have had the serving

## 20045:00 - 20080:00

infrastructure to have done it. And I

## 20080:00 - 20100:00

think because we weren't sure whether or

## 20100:00 - 20130:00

not we wanted to, we like hesitated for

## 20130:00 - 20150:00

too long on building that

## 20150:00 - 20175:00

infrastructure, which I think is

## 20175:00 - 20215:00

learning for for me.

## 20215:00 - 20250:00

>> I mean, at this time, ChatGpt had not

## 20250:00 - 20275:00

launched yet. Chat GPD hadn't launched

## 20275:00 - 20290:00

and so I guess we didn't know that it

## 20290:00 - 20310:00

would be a big deal too.

## 20310:00 - 20360:00

>> This is around the pandemic 2022.

## 20360:00 - 20395:00

>> This is summer 2022. Yep. And then chat

## 20395:00 - 20465:00

GPD launched fall 2022 and then we

## 20465:00 - 20510:00

relaunched our API after that and then

## 20510:00 - 20565:00

claude AI after that also. I think it

## 20565:00 - 20585:00

didn't seem like it was working

## 20585:00 - 20655:00

basically until Claude 35 and coding. I

## 20655:00 - 20675:00

think like really really like through

## 20675:00 - 20725:00

that whole time then until about a year

## 20725:00 - 20770:00

ago it seemed like it wasn't clear that

## 20770:00 - 20795:00

we were going to end up being like a

## 20795:00 - 20815:00

successful company.

## 20815:00 - 20840:00

>> We actually saw that in the startups

## 20840:00 - 20885:00

because we kind of get a bit of a vibe

## 20885:00 - 20910:00

check in terms of what is the preferred

## 20910:00 - 20965:00

model for startups. So all of 2023 open

## 20965:00 - 21000:00

AI was the response. Then things started

## 21000:00 - 21050:00

to turn in 2024

## 21050:00 - 21100:00

is when uh we saw claw 3.5 and

## 21100:00 - 21140:00

especially sonnet was starting to get a

## 21140:00 - 21175:00

market share per se in the YC batches

## 21175:00 - 21205:00

going from single digit to at some point

## 21205:00 - 21260:00

like 20 and to 30% and especially for

## 21260:00 - 21275:00

coding

## 21275:00 - 21285:00

>> y

## 21285:00 - 21340:00

>> became the default choice which was very

## 21340:00 - 21365:00

interesting. Can you tell us about how

## 21365:00 - 21395:00

that emergent behavior and the spikiness

## 21395:00 - 21420:00

on that particular skill

## 21420:00 - 21455:00

>> must be 80% now or 90.

## 21455:00 - 21480:00

>> Yeah. for coding even more especially

## 21480:00 - 21525:00

now clock code. What was that? Was that

## 21525:00 - 21555:00

on purpose or just kind of happened?

## 21555:00 - 21610:00

>> I think that we invested more in trying

## 21610:00 - 21630:00

to make the model really good at code

## 21630:00 - 21660:00

because we wanted the model to be good

## 21660:00 - 21700:00

at code was one thing

## 21700:00 - 21710:00

>> and you did it.

## 21710:00 - 21725:00

>> Yeah.

## 21725:00 - 21760:00

>> And then I think seeing seeing the

## 21760:00 - 21790:00

reaction of everyone to it was like okay

## 21790:00 - 21830:00

yeah like let's go much harder on that

## 21830:00 - 21835:00

also.

## 21835:00 - 21885:00

>> And this is before 3.5 sonnet. you'd

## 21885:00 - 21910:00

already invested enough in coding to

## 21910:00 - 21930:00

realize that that was really promising

## 21930:00 - 21960:00

and you decided to double down.

## 21960:00 - 21985:00

>> I think this really was like individuals

## 21985:00 - 22020:00

within the org being like we want to do

## 22020:00 - 22060:00

coding uh before 35 sonnet and then when

## 22060:00 - 22090:00

we saw 35 sonnet's really good product

## 22090:00 - 22125:00

market fit that was good signal to like

## 22125:00 - 22140:00

go go for that

## 22140:00 - 22170:00

>> and do you guys know like the day that

## 22170:00 - 22205:00

you guys launched 3.5 sonnet did you

## 22205:00 - 22230:00

know that you had something really

## 22230:00 - 22255:00

special and this was going to be the

## 22255:00 - 22285:00

turning point for the company or were

## 22285:00 - 22310:00

you as surprised as openi when they

## 22310:00 - 22335:00

launched chat GBT and it just like

## 22335:00 - 22365:00

unexpectedly took off? Yeah, I I wish

## 22365:00 - 22405:00

that I wish that we had like more

## 22405:00 - 22430:00

foresight on that, but no, I think I

## 22430:00 - 22455:00

think it was surprising for us too like

## 22455:00 - 22485:00

how how big of a deal it was. And then I

## 22485:00 - 22520:00

think 37 sonnet also like surprised us

## 22520:00 - 22560:00

by how much it unlocked like agentic

## 22560:00 - 22590:00

coding. I think for for each of these

## 22590:00 - 22625:00

things, yeah, we move quite fast in

## 22625:00 - 22660:00

rolling them out and so we really um

## 22660:00 - 22700:00

often don't know what the results are

## 22700:00 - 22715:00

going to be there.

## 22715:00 - 22750:00

>> I think it's what made a lot of these

## 22750:00 - 22785:00

coding agent startups work. I mean

## 22785:00 - 22830:00

there's a crazy story of Replet winning

## 22830:00 - 22875:00

going to 100 million in uh just 10

## 22875:00 - 22925:00

months right there's cursor of course a

## 22925:00 - 22975:00

story and all built on all these with

## 22975:00 - 22990:00

with sonnet

## 22990:00 - 23010:00

>> I think that all all of those things

## 23010:00 - 23045:00

have been surprising to me and then also

## 23045:00 - 23080:00

just like in my working with claude too

## 23080:00 - 23110:00

like I think I continue to be surprised

## 23110:00 - 23140:00

by like the type of stuff that it can do

## 23140:00 - 23165:00

and I I do think with each one there's

## 23165:00 - 23195:00

like more stuff that kind of unlocks but

## 23195:00 - 23210:00

one of my friends was telling me that

## 23210:00 - 23260:00

she had some code that she uh some code

## 23260:00 - 23285:00

source tool that she wanted to modify,

## 23285:00 - 23310:00

but she didn't have the source code for

## 23310:00 - 23340:00

it. She had the compiled binary, and

## 23340:00 - 23360:00

she's like, "Claude, can you can you

## 23360:00 - 23400:00

decompile this?" Like, "Yeah, can can

## 23400:00 - 23425:00

you disassemble the assembly?" And

## 23425:00 - 23460:00

Claude Claude chewed on it for 10

## 23460:00 - 23495:00

minutes and like made a C version of it.

## 23495:00 - 23535:00

And so then she had the thing to which

## 23535:00 - 23555:00

is insane. And she's like, "Yeah, like

## 23555:00 - 23585:00

if I spent 3 days on it, I probably

## 23585:00 - 23615:00

could have gotten the hex tables and

## 23615:00 - 23650:00

like wrote a little code to do, but like

## 23650:00 - 23680:00

it did the whole thing, made up variable

## 23680:00 - 23710:00

names for them, etc." So I do think that

## 23710:00 - 23740:00

like we keep getting surprised by stuff

## 23740:00 - 23765:00

that model has memorized all the hex

## 23765:00 - 23795:00

tables it can think through try to work

## 23795:00 - 23815:00

through it. I think we're going to

## 23815:00 - 23840:00

continue to be surprised by that sort of

## 23840:00 - 23850:00

stuff too.

## 23850:00 - 23890:00

>> If you pull like the YC founders they

## 23890:00 - 23925:00

prefer using anthropic models for coding

## 23925:00 - 23970:00

by like a huge margin that's much larger

## 23970:00 - 24000:00

than what you would predict if you just

## 24000:00 - 24030:00

looked at the benchmark results.

## 24030:00 - 24035:00

>> Yeah.

## 24035:00 - 24085:00

>> So there there seems to be some X factor

## 24085:00 - 24115:00

that makes people really like these

## 24115:00 - 24150:00

models for coding. Do you know what it

## 24150:00 - 24190:00

is and is it intentional in some way or

## 24190:00 - 24220:00

it just came out of the black box

## 24220:00 - 24230:00

somehow?

## 24230:00 - 24265:00

>> I think that the benchmarks benchmarks

## 24265:00 - 24310:00

are like easy to game where I think that

## 24310:00 - 24335:00

all the other big labs I think have

## 24335:00 - 24365:00

teams where they like their whole job

## 24365:00 - 24380:00

with the team is to like make the

## 24380:00 - 24425:00

benchmarks scores good and we don't have

## 24425:00 - 24455:00

such a team. And so I think that I think

## 24455:00 - 24490:00

that that is probably the biggest

## 24490:00 - 24495:00

factor.

## 24495:00 - 24520:00

>> You don't teach to the test.

## 24520:00 - 24555:00

>> We don't teach to the test cuz I I do

## 24555:00 - 24575:00

feel like if you start doing that then

## 24575:00 - 24610:00

like it has weird bad incentives. Maybe

## 24610:00 - 24630:00

we could like put that team under

## 24630:00 - 24650:00

marketing or something like that and

## 24650:00 - 24680:00

then ignore all the benchmarks. But I

## 24680:00 - 24700:00

think that that's one reasons why

## 24700:00 - 24755:00

there's some train test mismatch there.

## 24755:00 - 24790:00

>> So the evaluations are more qualitative

## 24790:00 - 24825:00

but internally or you have your internal

## 24825:00 - 24850:00

>> We have internal benchmarks. Yeah. But

## 24850:00 - 24870:00

we don't we don't publish them.

## 24870:00 - 24895:00

>> And is it the internal benchmarks that

## 24895:00 - 24920:00

the teams are really focused on

## 24920:00 - 24935:00

improving?

## 24935:00 - 24955:00

>> That's right. Yeah. So we have internal

## 24955:00 - 24980:00

benchmarks that the team focuses on and

## 24980:00 - 25010:00

improving and then we also have a bunch

## 25010:00 - 25060:00

of tasks like I think that accelerating

## 25060:00 - 25105:00

our own engineers is like a top top

## 25105:00 - 25140:00

priority for us too and so we we do a

## 25140:00 - 25165:00

ton of like dog fooding there to make

## 25165:00 - 25195:00

sure that it's helping with our folks

## 25195:00 - 25225:00

too. Going back to go Golden Golden Gate

## 25225:00 - 25260:00

Claude, there's a lot of sort of inter

## 25260:00 - 25290:00

the interpretability seems like it's a

## 25290:00 - 25325:00

big part of it. And then most people

## 25325:00 - 25355:00

would say that, you know, Claude's

## 25355:00 - 25405:00

personality just feels better. And then

## 25405:00 - 25435:00

how do you sort of at once be very

## 25435:00 - 25470:00

quantitative, but then also, you know,

## 25470:00 - 25505:00

build evals around personality.

## 25505:00 - 25555:00

>> The evals for personality are kind of

## 25555:00 - 25580:00

complicated, too, for like how do you

## 25580:00 - 25605:00

tell if like Claude has like a good

## 25605:00 - 25635:00

heart or something like that? It's like

## 25635:00 - 25670:00

hard to hard to know. Um, but I do think

## 25670:00 - 25705:00

that that's like Amanda Ascll's team's

## 25705:00 - 25730:00

mandate is I think she describes it as

## 25730:00 - 25775:00

like being like a a good world traveler

## 25775:00 - 25800:00

where like it can like Claude goes and

## 25800:00 - 25820:00

talks with all sorts of people from

## 25820:00 - 25845:00

different backgrounds and like each of

## 25845:00 - 25875:00

the people should come from come to that

## 25875:00 - 25910:00

being like I I like feel good about like

## 25910:00 - 25940:00

this conversation that I've had interp

## 25940:00 - 25965:00

really I think is like a long-term bet

## 25965:00 - 25990:00

right where it's like right now the

## 25990:00 - 26015:00

models aren't that scary but at some

## 26015:00 - 26045:00

point they're going to be more scary and

## 26045:00 - 26075:00

so I think the hope there is to have

## 26075:00 - 26110:00

some ability to know what's actually

## 26110:00 - 26140:00

going on under the hood when it becomes

## 26140:00 - 26180:00

more intense. Then more recently, Claude

## 26180:00 - 26215:00

Code's been a real success. Can you talk

## 26215:00 - 26245:00

us through like how did that project get

## 26245:00 - 26275:00

started internally? And again, was it

## 26275:00 - 26315:00

like a uh did you like know this time it

## 26315:00 - 26345:00

was going to work or was it a surprise?

## 26345:00 - 26385:00

>> Claude Code was um an internal tool

## 26385:00 - 26415:00

also. So like try to help out our our

## 26415:00 - 26465:00

engineers within Anthropic that uh yeah,

## 26465:00 - 26520:00

Boris um had like hacked together.

## 26520:00 - 26545:00

>> There's an internal anthropic engineer

## 26545:00 - 26560:00

wanting to build it for themselves

## 26560:00 - 26585:00

>> for internal for other internal

## 26585:00 - 26605:00

engineers. Yeah. For him and other

## 26605:00 - 26640:00

internal engineers. And then um I think

## 26640:00 - 26665:00

yeah I think we definitely didn't know

## 26665:00 - 26700:00

that it would be successful out there.

## 26700:00 - 26725:00

And I I think I think to to some degree

## 26725:00 - 26775:00

like we really had fully just bet on the

## 26775:00 - 26830:00

API before that with the intention being

## 26830:00 - 26875:00

like there's like so many so many

## 26875:00 - 26910:00

startups out there with so many good

## 26910:00 - 26945:00

ideas. Who are we to like figure out

## 26945:00 - 26970:00

what the right product is to build on

## 26970:00 - 27000:00

top of this stuff? Everyone out there is

## 27000:00 - 27025:00

going to build better stuff than us. And

## 27025:00 - 27050:00

so put all of our effort into just

## 27050:00 - 27085:00

making the best possible API. And I

## 27085:00 - 27115:00

think that this surprised me as like

## 27115:00 - 27145:00

okay like we actually were able to make

## 27145:00 - 27180:00

something that like as a product was

## 27180:00 - 27215:00

like better than the other products out

## 27215:00 - 27250:00

on the market for this agentic use. I

## 27250:00 - 27290:00

have like some theory that like part of

## 27290:00 - 27315:00

that came from like a mind shift of

## 27315:00 - 27360:00

seeing Claude as like the user uh for

## 27360:00 - 27390:00

this thing too. For like link that we

## 27390:00 - 27420:00

were like trying to build things for

## 27420:00 - 27455:00

teachers were like our users for for

## 27455:00 - 27490:00

grouper it was like single people in New

## 27490:00 - 27530:00

York mostly I guess. Um, for this I

## 27530:00 - 27570:00

think really the the like users are the

## 27570:00 - 27605:00

developers but also I think the users is

## 27605:00 - 27640:00

Claude. It's like give Claude the right

## 27640:00 - 27680:00

tools that Claude can actually do that

## 27680:00 - 27705:00

effectively help Claude get the right

## 27705:00 - 27760:00

context to work effectively. This team

## 27760:00 - 27800:00

was like the most focused on Claude as

## 27800:00 - 27830:00

like a user which I think makes sense

## 27830:00 - 27860:00

that you guys would understand Claude

## 27860:00 - 27900:00

the best. Yeah, I I do think that that's

## 27900:00 - 27930:00

a place where like startup founders

## 27930:00 - 27965:00

though like can can do that too. And I

## 27965:00 - 27985:00

think that that's that's probably a rich

## 27985:00 - 28025:00

vein for people to like make tools that

## 28025:00 - 28075:00

are better for models as users.

## 28075:00 - 28110:00

>> That's the perfect anthropomorphization

## 28110:00 - 28150:00

of like the LLM itself. Like the agent

## 28150:00 - 28175:00

is one of the stakeholders is one of the

## 28175:00 - 28210:00

users that you would go after and try to

## 28210:00 - 28225:00

like empower.

## 28225:00 - 28255:00

>> Yeah. Yeah. Totally. which actually

## 28255:00 - 28295:00

makes a lot of sense why you guys

## 28295:00 - 28350:00

actually got MCP to work to do tool

## 28350:00 - 28385:00

calling because a bunch of other labs

## 28385:00 - 28425:00

had tried to do something and the

## 28425:00 - 28470:00

standard that stuck that really took off

## 28470:00 - 28485:00

was yours.

## 28485:00 - 28510:00

>> Yeah, I think that that seems like a

## 28510:00 - 28540:00

similar one too where it's like

## 28540:00 - 28560:00

>> model model focused

## 28560:00 - 28590:00

>> going back to claw code. So like success

## 28590:00 - 28630:00

is really exciting. It's also scary for

## 28630:00 - 28660:00

like cursor and other companies that

## 28660:00 - 28705:00

have built on top of the API like what's

## 28705:00 - 28730:00

your advice to founders building

## 28730:00 - 28750:00

products like how should they think

## 28750:00 - 28785:00

about building on the API but also

## 28785:00 - 28815:00

worrying about like anthropic or one of

## 28815:00 - 28840:00

the labs building something better than

## 28840:00 - 28850:00

they can build.

## 28850:00 - 28880:00

>> I think I was kind of surprised that

## 28880:00 - 28920:00

claude code like we we did build a thing

## 28920:00 - 28950:00

that was like uh like the best in the

## 28950:00 - 28985:00

market there too. It's not super clear

## 28985:00 - 29025:00

to me what the big advantage was for us

## 29025:00 - 29065:00

for Claude code besides more empathy for

## 29065:00 - 29085:00

Claude or something. That's actually I

## 29085:00 - 29105:00

think that's actually really interesting

## 29105:00 - 29130:00

insight. Like it seems like the thing

## 29130:00 - 29155:00

that Yeah. you were building for a

## 29155:00 - 29185:00

specific user that you knew really well

## 29185:00 - 29205:00

that other people wouldn't have thought

## 29205:00 - 29245:00

to build for versus like you had some

## 29245:00 - 29285:00

like intrinsic technology advantage.

## 29285:00 - 29310:00

>> Yeah. Like I think a startup could could

## 29310:00 - 29330:00

have done that same thing too, right?

## 29330:00 - 29335:00

>> Yeah.

## 29335:00 - 29375:00

>> I think we're the most like developer

## 29375:00 - 29405:00

focused lab. I think we're the most like

## 29405:00 - 29445:00

API focused lab too. So I think we want

## 29445:00 - 29470:00

to make sure that we have the best

## 29470:00 - 29500:00

platform for people to build stuff on

## 29500:00 - 29545:00

cuz this thing is growing so incredibly

## 29545:00 - 29575:00

quickly. like we're not going to be the

## 29575:00 - 29615:00

fastest at figuring out all the ways

## 29615:00 - 29655:00

that we need to empower Claude to do the

## 29655:00 - 29695:00

work that connects Claude to the entire

## 29695:00 - 29730:00

human business that's like human human

## 29730:00 - 29760:00

world is all designed for humans but

## 29760:00 - 29780:00

like we need to get the models to be

## 29780:00 - 29820:00

able to be productive members of uh the

## 29820:00 - 29830:00

economy.

## 29830:00 - 29870:00

>> Are there like ideas or areas you would

## 29870:00 - 29915:00

love to see developers building in or

## 29915:00 - 29945:00

like areas you don't you you think are

## 29945:00 - 29990:00

like underappreciated right now? Yeah,

## 29990:00 - 30020:00

Claude code is like how do you get

## 30020:00 - 30075:00

Claude to be a useful pair programmer

## 30075:00 - 30110:00

kind of um or like junior engineer.

## 30110:00 - 30165:00

You've got like a level

## 30165:00 - 30190:00

two or three or something like that that

## 30190:00 - 30215:00

you can work with or like very spiky

## 30215:00 - 30235:00

because also it can do the like weird

## 30235:00 - 30270:00

disassembly stuff that like a super high

## 30270:00 - 30300:00

level suite would struggle with. Less

## 30300:00 - 30350:00

good at knowing what type of work to do.

## 30350:00 - 30375:00

Needs kind of a lot of handholding.

## 30375:00 - 30405:00

Needs a lot of context from it. That's

## 30405:00 - 30455:00

like one very particular subset of work

## 30455:00 - 30495:00

that can be done. Uh if you look at like

## 30495:00 - 30575:00

all the stuff that happens in businesses

## 30575:00 - 30610:00

besides that, it's like a very tiny

## 30610:00 - 30635:00

fraction of like all the work that's

## 30635:00 - 30675:00

done in businesses that like a smart

## 30675:00 - 30725:00

person who knows how to code and like

## 30725:00 - 30760:00

use lots of tools but doesn't have that

## 30760:00 - 30805:00

much context yet uh would want to do. So

## 30805:00 - 30855:00

I think I think finding ways to coach

## 30855:00 - 30910:00

Claude or uh co coach whatever model to

## 30910:00 - 30965:00

like do useful tasks for businesses

## 30965:00 - 31000:00

seems like there's just like a huge huge

## 31000:00 - 31015:00

space there.

## 31015:00 - 31065:00

>> So Tom, a big part of your job is like

## 31065:00 - 31090:00

owning all the compute infrastructure

## 31090:00 - 31120:00

that makes anthropic work. Can you talk

## 31120:00 - 31150:00

about like what what is the compute

## 31150:00 - 31175:00

infrastructure behind this giant thing?

## 31175:00 - 31210:00

Now, one thing that's interesting to

## 31210:00 - 31250:00

look at is just that humanity is on

## 31250:00 - 31265:00

track for like the largest

## 31265:00 - 31300:00

infrastructure buildout of all time.

## 31300:00 - 31305:00

Now,

## 31305:00 - 31325:00

>> this is going to be larger than the

## 31325:00 - 31350:00

Apollo project, larger than the

## 31350:00 - 31365:00

Manhattan project.

## 31365:00 - 31395:00

>> It'll be bigger than both of them next

## 31395:00 - 31425:00

year if it keeps on the current

## 31425:00 - 31475:00

trajectory, which is like roughly 3x per

## 31475:00 - 31530:00

year increase in spending on AGI

## 31530:00 - 31570:00

compute, which is just bonkers. Yeah.

## 31570:00 - 31610:00

Like 3x per year is wild. I think it's

## 31610:00 - 31640:00

going to keep up on the 3x per year

## 31640:00 - 31675:00

trajectory. It's already locked in for

## 31675:00 - 31740:00

that for for next year and then it's a

## 31740:00 - 31775:00

little bit open for for 2027.

## 31775:00 - 31830:00

>> I mean anecdotally internal to YC uh we

## 31830:00 - 31870:00

can't get enough you know credits across

## 31870:00 - 31905:00

all of the top frontier models including

## 31905:00 - 31930:00

Claude. So you got to help us out a

## 31930:00 - 31960:00

little bit.

## 31960:00 - 31970:00

>> Yeah.

## 31970:00 - 31990:00

>> We're just I mean everyone's

## 31990:00 - 32015:00

bottlenecked literally every you know

## 32015:00 - 32045:00

it's like give me more intelligence. I

## 32045:00 - 32055:00

can't have enough.

## 32055:00 - 32075:00

>> Yeah. And I know you guys have been

## 32075:00 - 32105:00

looking at more hardware startups also

## 32105:00 - 32135:00

for like more accelerators. I think that

## 32135:00 - 32165:00

we will see more accelerators coming

## 32165:00 - 32205:00

online to 2027. That's a good a good

## 32205:00 - 32240:00

space. Also like data center tech I

## 32240:00 - 32255:00

think is a big one.

## 32255:00 - 32280:00

>> Where are the bottlenecks for you guys

## 32280:00 - 32320:00

now? Is it like getting enough

## 32320:00 - 32355:00

electricity, getting enough GPUs,

## 32355:00 - 32395:00

getting construction permits,

## 32395:00 - 32430:00

>> power, people are using jet engines to

## 32430:00 - 32455:00

get power. That's nuts.

## 32455:00 - 32500:00

>> Overall for the buildout, I think power

## 32500:00 - 32535:00

is going to be the biggest bottleneck,

## 32535:00 - 32560:00

especially power in the US. Like we want

## 32560:00 - 32595:00

to build in the US. That's one of our

## 32595:00 - 32630:00

biggest policy goals is to like get the

## 32630:00 - 32675:00

US to like build more data centers,

## 32675:00 - 32705:00

permit more data centers, make it easier

## 32705:00 - 32710:00

to build.

## 32710:00 - 32750:00

>> Is the answer renewables or is it uh

## 32750:00 - 32765:00

nuclear?

## 32765:00 - 32805:00

>> I I definitely I feel like yes, yes, all

## 32805:00 - 32825:00

all of those things. I wish I wish that

## 32825:00 - 32870:00

nuclear was easier to build.

## 32870:00 - 32905:00

>> Anthropic is the only major lab that

## 32905:00 - 32950:00

uses not just one kind of GPU, but the

## 32950:00 - 33000:00

GPUs from three different manufacturers.

## 33000:00 - 33030:00

Can you talk about that and how how how

## 33030:00 - 33050:00

that strategy has played out?

## 33050:00 - 33100:00

>> Yeah. Yeah. So we use um GPUs, TPUs and

## 33100:00 - 33135:00

tranium. Downside of doing that is that

## 33135:00 - 33165:00

we split our performance engineering

## 33165:00 - 33200:00

teams across all of those platforms

## 33200:00 - 33230:00

which is a ton of extra work. The

## 33230:00 - 33255:00

positive thing is it gives us the

## 33255:00 - 33300:00

flexibility to both one like soak up

## 33300:00 - 33335:00

that extra capacity because there there

## 33335:00 - 33375:00

just is more of those altogether than

## 33375:00 - 33410:00

just one and then two is we can use the

## 33410:00 - 33435:00

like right chips for the right jobs

## 33435:00 - 33465:00

where some chips will be better for

## 33465:00 - 33500:00

inference, some chips will be better for

## 33500:00 - 33545:00

training and we can match the the right

## 33545:00 - 33570:00

chips to the right jobs. So yeah, I

## 33570:00 - 33600:00

think that that's kind of the the

## 33600:00 - 33625:00

trade-off there. I guess one cool thing

## 33625:00 - 33660:00

is just connecting the dots through your

## 33660:00 - 33705:00

career and how all of this compounded

## 33705:00 - 33750:00

because you you were the one engineer

## 33750:00 - 33780:00

building that change of the architecture

## 33780:00 - 33830:00

from TPUs to GPUs back at OpenAI that

## 33830:00 - 33870:00

got GPD3 to actually scale and now

## 33870:00 - 33905:00

you're in charge of that at a much much

## 33905:00 - 33955:00

bigger scale year years later. I don't

## 33955:00 - 33985:00

know if that kind of connected dots for

## 33985:00 - 34040:00

you. The big move from TPUs to GPUs at

## 34040:00 - 34070:00

OpenAI I think was partly driven just

## 34070:00 - 34105:00

that PyTorch was a better software stack

## 34105:00 - 34160:00

on top of them than TensorFlow on top of

## 34160:00 - 34190:00

TPUs. And I think that that then

## 34190:00 - 34240:00

unlocked fast iteration where like if

## 34240:00 - 34270:00

you have like a good reliable software

## 34270:00 - 34305:00

stack then you can experiment quickly

## 34305:00 - 34335:00

just like build a whole system that

## 34335:00 - 34355:00

works. I think that that's the thing

## 34355:00 - 34395:00

that we really strive for now at

## 34395:00 - 34430:00

Anthropic too is a challenge of having

## 34430:00 - 34465:00

many more platforms is that it's harder

## 34465:00 - 34490:00

to write all the good software. I think

## 34490:00 - 34525:00

building the muscle of knowing how to

## 34525:00 - 34560:00

build that software well so that all of

## 34560:00 - 34595:00

the people who build on top of that low

## 34595:00 - 34625:00

level can have a great experience with

## 34625:00 - 34645:00

it is the most important thing there.

## 34645:00 - 34680:00

>> Do you have advice for um kind of like a

## 34680:00 - 34730:00

younger Tom version of yourself who now

## 34730:00 - 34765:00

you've seen and went through this crazy

## 34765:00 - 34805:00

journey? If someone was you back in the

## 34805:00 - 34860:00

20s living today and they wanted to ride

## 34860:00 - 34895:00

and join the AI revolution, what would

## 34895:00 - 34910:00

you say to them?

## 34910:00 - 34930:00

>> And very specifically something we see

## 34930:00 - 34960:00

from a lot of hear from a lot of college

## 34960:00 - 34995:00

students at the moment is they uh they

## 34995:00 - 35020:00

don't know what like if they should stay

## 35020:00 - 35045:00

in college like are there going to be

## 35045:00 - 35095:00

jobs for them what like how is the world

## 35095:00 - 35125:00

going to change and what should they do?

## 35125:00 - 35170:00

taking more risks I think is is wise and

## 35170:00 - 35230:00

then also trying to work on stuff where

## 35230:00 - 35270:00

your friends would be really excited and

## 35270:00 - 35305:00

impressed if you did it or a more

## 35305:00 - 35330:00

idealized version of yourself would be

## 35330:00 - 35365:00

really like proud of yourself if you

## 35365:00 - 35390:00

succeeded at it I think is like probably

## 35390:00 - 35420:00

the thing that I would I would try to

## 35420:00 - 35450:00

tell a younger version of myself

## 35450:00 - 35490:00

>> more intrinsic less exttrinsic like

## 35490:00 - 35530:00

don't chase these other credentials and

## 35530:00 - 35555:00

getting the degree or whatever you know

## 35555:00 - 35590:00

working at Fang like those are just

## 35590:00 - 35605:00

irrelevant

## 35605:00 - 35625:00

>> as of today.

## 35625:00 - 35645:00

>> Yeah, exactly.

## 35645:00 - 35700:00

>> That's all we have time for today. We'll

## 35700:00 - 35750:00

see you guys next time.

## 35750:00+

[Music]

