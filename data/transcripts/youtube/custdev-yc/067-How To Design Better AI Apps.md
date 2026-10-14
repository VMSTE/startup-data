---
source: https://www.youtube.com/watch?v=WJoZK9sMwvw
title: How To Design Better AI Apps
author: Y Combinator
date: 2025-05-23
views: 96765
description: >-
  In this episode of The Breakdown, Tom and Dave are joined by fellow YC General
  Partner Pete Koomen to lay out a new vision for how AI should actually work:
  not as a chatbot bolted onto legacy software, but as a customizable tool that
  helps people offload the work they don't want to do. From editable system
  prompts to agents that act more like collaborators, they dig into what it
  means to build AI-native software—and why the future belongs to products that
  let users teach machines how to think.


  Pete's essay, "AI Horseless Carriages":
  https://koomen.dev/essays/horseless-carriages


  Apply to Y Combinator: https://ycombinator.com/apply

  Work at a startup: https://workatastartup.com


  Chapters (Powered by https://chapterme.co/) -

  0:00 – Intro

  0:52 – Why AI apps are broken

  2:39 – The problem with Google's AI App

  4:00 – A better way to build AI apps

  5:27 – The hidden system prompt

  7:57 – What if you could access the system prompt?

  9:40 – The developer-user divide in software

  10:48 – The "horseless carriage" metaphor

  13:35 – Email reading agent demo

  14:34 – Everyone can be a prompt engineer

  16:23 – Why coding agents feel magical

  21:42 – Training AI like a human assistant

  28:45 – The problem with chatbot interfaces

  29:10 – Advice for founders
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:45:41.074Z
---

# How To Design Better AI Apps

## 00:00 - 40:00

We're using old software development

## 40:00 - 80:00

techniques to build these features and

## 80:00 - 105:00

we're not actually taking full advantage

## 105:00 - 150:00

of what AI can do. I think the promise

## 150:00 - 190:00

of AI for many of us is that it allows

## 190:00 - 225:00

us to build software that the user can

## 225:00 - 260:00

program to do whatever they want using

## 260:00 - 300:00

only natural language. Steve Jobs

## 300:00 - 325:00

describes software as a sort of as a

## 325:00 - 365:00

bicycle for the mind. This feels like I

## 365:00 - 385:00

don't know like a rocket ship for the

## 385:00 - 415:00

mind.

## 415:00 - 500:00

[Music]

## 500:00 - 525:00

Welcome to another episode of The

## 525:00 - 555:00

Breakdown. Today we're lucky to have

## 555:00 - 595:00

Pete Kumman, our partner here at YC.

## 595:00 - 625:00

Pete was the founder of Optimizely,

## 625:00 - 660:00

which built software to help companies

## 660:00 - 705:00

AB test. Pete, welcome. Thank you. Happy

## 705:00 - 735:00

to be here. So, Pete, you recently wrote

## 735:00 - 765:00

an essay which caused a bit of a stir

## 765:00 - 790:00

and basically told everyone on the

## 790:00 - 825:00

internet who was building AI agents they

## 825:00 - 860:00

were doing it completely wrong. So, tell

## 860:00 - 905:00

us more about that. Sure. uh when I use

## 905:00 - 945:00

AI in my day-to-day life, I've kind of

## 945:00 - 975:00

had two radically different experiences,

## 975:00 - 1030:00

right? On one hand, when I use tools

## 1030:00 - 1080:00

like cursor and wind surf to build

## 1080:00 - 1135:00

software with AI, it feels like the most

## 1135:00 - 1170:00

powerful tool I've ever used, right?

## 1170:00 - 1205:00

It's this feeling of being able to

## 1205:00 - 1230:00

create anything I want. Anything I can

## 1230:00 - 1275:00

picture in my head, uh you know, will

## 1275:00 - 1300:00

materialize in front of me with these

## 1300:00 - 1330:00

tools. And it makes me so excited about

## 1330:00 - 1385:00

AI. Uh, and then I've had a lot of other

## 1385:00 - 1420:00

experiences a lot of times when I'm

## 1420:00 - 1450:00

using existing apps that I'm used to

## 1450:00 - 1485:00

that have incorporated AI into them

## 1485:00 - 1510:00

where it doesn't feel that way at all.

## 1510:00 - 1545:00

Um, it actually feels like more of a

## 1545:00 - 1585:00

chore, right? Like using the AI actually

## 1585:00 - 1635:00

creates more work for me than uh just

## 1635:00 - 1665:00

doing whatever it was myself. The

## 1665:00 - 1720:00

example that I chose in my essay uh was

## 1720:00 - 1765:00

to pick on the integration that the

## 1765:00 - 1815:00

Gmail team built between their AI model

## 1815:00 - 1885:00

Gemini and Gmail's uh interface that uh

## 1885:00 - 1920:00

this is a little draftw writing agent

## 1920:00 - 1965:00

that can create email drafts for me

## 1965:00 - 1990:00

given some instructions. Yeah. And the

## 1990:00 - 2015:00

underlying Gemini model is pretty

## 2015:00 - 2050:00

phenomenal, right? Gemini is amazing.

## 2050:00 - 2080:00

The model itself is absolutely

## 2080:00 - 2105:00

incredible. We've been using it a lot at

## 2105:00 - 2155:00

YC to automate our own work. I'm so

## 2155:00 - 2190:00

impressed with what they built. Um, but

## 2190:00 - 2230:00

a lot of that power, I think, is hidden

## 2230:00 - 2270:00

behind a UI that makes it really

## 2270:00 - 2300:00

frustrating to use. And that was really

## 2300:00 - 2335:00

the focus of my essay. The feature that

## 2335:00 - 2360:00

I chose as my example was this little

## 2360:00 - 2400:00

draftw writing agent that shows up in

## 2400:00 - 2440:00

the Gmail interface. And uh, what it

## 2440:00 - 2485:00

does is I can put in some instructions.

## 2485:00 - 2530:00

So, in this case, let my boss Gary know

## 2530:00 - 2555:00

that my daughter woke up with the flu

## 2555:00 - 2585:00

this morning and I won't be able to come

## 2585:00 - 2620:00

into the office today. and it will spit

## 2620:00 - 2660:00

out an email draft for me to make your

## 2660:00 - 2690:00

life easier. To make my life easier.

## 2690:00 - 2740:00

Exactly. So, here is the email draft

## 2740:00 - 2790:00

that I got when I put that prompt into

## 2790:00 - 2835:00

the UI. Dear Gary, I'm writing to inform

## 2835:00 - 2860:00

you that my daughter woke up with the

## 2860:00 - 2885:00

flu this morning. As a result, I won't

## 2885:00 - 2920:00

be able to come into the office today.

## 2920:00 - 2950:00

Thank you for understanding. Best

## 2950:00 - 2990:00

regards, Pete. And if I got this, I'd be

## 2990:00 - 3020:00

like, Pete has been has his brain taken

## 3020:00 - 3050:00

over by like or he's been fished and I

## 3050:00 - 3080:00

need to report fishing like something's

## 3080:00 - 3110:00

going horribly wrong. accounts been

## 3110:00 - 3145:00

hacked, right? There's two big problems

## 3145:00 - 3185:00

with this. The first problem is, like

## 3185:00 - 3210:00

you're pointing out, that doesn't sound

## 3210:00 - 3245:00

anything like me, right? If you got this

## 3245:00 - 3280:00

email, you wouldn't you would assume

## 3280:00 - 3310:00

somebody else wrote this. My account got

## 3310:00 - 3340:00

hacked. I got fished. And then the

## 3340:00 - 3400:00

second problem is that the draft or

## 3400:00 - 3465:00

rather the prompt that I used to explain

## 3465:00 - 3505:00

what I wanted in the draft is roughly as

## 3505:00 - 3545:00

long as the draft itself. Yeah, that was

## 3545:00 - 3575:00

my contention here. Right. On one side,

## 3575:00 - 3625:00

you have using AI makes you feel like a

## 3625:00 - 3665:00

superhuman with unlimited powers, and on

## 3665:00 - 3705:00

the other hand, using AI is is

## 3705:00 - 3740:00

frustrating and adds more work. Maybe

## 3740:00 - 3755:00

we're jumping ahead a bit a little bit,

## 3755:00 - 3785:00

but the ideal experience, I think, would

## 3785:00 - 3830:00

be something like telling the AI, hey,

## 3830:00 - 3855:00

my daughter's ill, like figure out my

## 3855:00 - 3880:00

calendar today. And then it go through

## 3880:00 - 3905:00

your actual calendar and then figure out

## 3905:00 - 3930:00

each person and then write the

## 3930:00 - 3950:00

appropriate email in the appropriate

## 3950:00 - 3970:00

tone. Right? That's perhaps we're

## 3970:00 - 4005:00

skipping all the way to the end, but I I

## 4005:00 - 4030:00

think that's exactly right. These AI

## 4030:00 - 4080:00

models are now capable of doing things

## 4080:00 - 4110:00

like that where it's actually

## 4110:00 - 4145:00

anticipating all of the things that will

## 4145:00 - 4170:00

need to happen as a result of my

## 4170:00 - 4205:00

daughter waking up with the flu and

## 4205:00 - 4240:00

helping me do those things. But that's

## 4240:00 - 4270:00

not what we've built, right? That's not

## 4270:00 - 4300:00

what what the team has built. So Pete,

## 4300:00 - 4330:00

like the people who work on Gmail, I I

## 4330:00 - 4360:00

know a lot of them. They're not dunes,

## 4360:00 - 4395:00

right? Not at all. Yeah. They probably

## 4395:00 - 4425:00

don't use the feature themselves is my

## 4425:00 - 4460:00

guess cuz I don't use that feature. So

## 4460:00 - 4485:00

how did we get here? Like how did this

## 4485:00 - 4515:00

happen? I know many people who work for

## 4515:00 - 4555:00

Google. They're incredibly smart. Uh why

## 4555:00 - 4595:00

did they ship a feature that ostensibly

## 4595:00 - 4625:00

nobody, including probably them,

## 4625:00 - 4665:00

actually uses? I don't know. Part of the

## 4665:00 - 4750:00

problem is that we're using old software

## 4750:00 - 4785:00

development mentality, old software

## 4785:00 - 4820:00

development techniques to build these

## 4820:00 - 4850:00

features and we're not actually taking

## 4850:00 - 4895:00

full advantage of what AI can do. And so

## 4895:00 - 4925:00

I'll explain what I mean by that, right?

## 4925:00 - 4950:00

And I'll go back to these two problems.

## 4950:00 - 4975:00

Let's start with the tone problem,

## 4975:00 - 5000:00

right? This doesn't actually sound like

## 5000:00 - 5055:00

me. Why is that? Well, what's actually

## 5055:00 - 5105:00

happening under the hood when I ask this

## 5105:00 - 5160:00

Gmail agent for a draft is that this

## 5160:00 - 5210:00

Gmail agent, this little UI, combines my

## 5210:00 - 5245:00

prompt, which is the one we we just

## 5245:00 - 5285:00

talked about, with what's called a

## 5285:00 - 5340:00

system prompt. And the system prompt is

## 5340:00 - 5390:00

the text that explains to the AI who it

## 5390:00 - 5430:00

is and what its job is. And this gets

## 5430:00 - 5465:00

reused every single time. And in the

## 5465:00 - 5505:00

Gmail case, I don't actually know what

## 5505:00 - 5550:00

that system prompt says. This is it's

## 5550:00 - 5585:00

been hidden from the user. I'm not

## 5585:00 - 5620:00

allowed to see it, let alone edit it

## 5620:00 - 5675:00

myself. But we can kind of guess what it

## 5675:00 - 5705:00

says, right? You know, and I've got a

## 5705:00 - 5740:00

little caricatured version of this in

## 5740:00 - 5790:00

the essay. The system prompt here is

## 5790:00 - 5825:00

something like, "You're a helpful email

## 5825:00 - 5855:00

writing assistant responsible for

## 5855:00 - 5890:00

writing emails on behalf of a Gmail

## 5890:00 - 5930:00

user. follow the user's instructions and

## 5930:00 - 5975:00

use a formal businessy tone and correct

## 5975:00 - 6005:00

punctuation so that it's obvious the

## 6005:00 - 6045:00

user is really smart and serious. I

## 6045:00 - 6075:00

actually built a little demo so that you

## 6075:00 - 6130:00

can see the impact of a system prompt on

## 6130:00 - 6165:00

the email draft, right? And so we

## 6165:00 - 6205:00

combine our sort of supposed Gmail

## 6205:00 - 6265:00

system prompt with my user prompt here

## 6265:00 - 6305:00

asking for the draft and we generate the

## 6305:00 - 6345:00

draft and we get something like this.

## 6345:00 - 6375:00

Right? Again, it's an email that seems

## 6375:00 - 6400:00

perfectly reasonable. It does what I've

## 6400:00 - 6430:00

asked but it doesn't sound like me. So

## 6430:00 - 6470:00

just digging in like we are guessing

## 6470:00 - 6505:00

what the the system prompt might be in

## 6505:00 - 6545:00

this case but it seems we've guessed

## 6545:00 - 6575:00

close because the output is basically

## 6575:00 - 6600:00

what you get when you use Gmail

## 6600:00 - 6625:00

relatively similar. And so like just to

## 6625:00 - 6660:00

point out the the system prompt that we

## 6660:00 - 6690:00

have created here um is one that is

## 6690:00 - 6730:00

generic. It would apply to all users in

## 6730:00 - 6760:00

exactly the same way. It's one that's

## 6760:00 - 6810:00

like safe. Um you've explicitly told it

## 6810:00 - 6855:00

um use a businessy tone, look smart and

## 6855:00 - 6885:00

serious. Don't say anything that might

## 6885:00 - 6920:00

make the parent company of this product

## 6920:00 - 6950:00

look bad. And that's got to be the

## 6950:00 - 6970:00

overriding concern for a lot of these

## 6970:00 - 7005:00

companies, right? We don't want the AI

## 7005:00 - 7020:00

to say anything that's going to

## 7020:00 - 7050:00

embarrass Google. I I remember it was

## 7050:00 - 7085:00

either Google or Facebook released like

## 7085:00 - 7115:00

a scientific model like pretty early on

## 7115:00 - 7140:00

and then very very quickly pulled it

## 7140:00 - 7160:00

back because it was saying some it was

## 7160:00 - 7210:00

hallucinating sometimes. And so I think

## 7210:00 - 7240:00

like Google were really on the cutting

## 7240:00 - 7270:00

edge of this transform technology and

## 7270:00 - 7295:00

were like leap frog by open AI just

## 7295:00 - 7315:00

because they was too cautious to put

## 7315:00 - 7345:00

stuff out there. Yes. Yeah. I think

## 7345:00 - 7365:00

that's probably a big part of this,

## 7365:00 - 7405:00

which is that, you know, my my little

## 7405:00 - 7430:00

supposed version here is probably

## 7430:00 - 7455:00

incomplete. There's probably a whole

## 7455:00 - 7480:00

bunch of additional text in the real

## 7480:00 - 7515:00

system prompt about not embarrassing

## 7515:00 - 7540:00

Google and all of the different things

## 7540:00 - 7555:00

it should avoid doing. If you say

## 7555:00 - 7605:00

anything bad about Sundar, you're fine.

## 7605:00 - 7650:00

And we've seen this recently as uh these

## 7650:00 - 7685:00

system prompts kind of get leaked at

## 7685:00 - 7715:00

times. And it's a big deal because

## 7715:00 - 7750:00

everybody's we see the system prompt now

## 7750:00 - 7785:00

for this AI assistant or this one. And

## 7785:00 - 7805:00

if you read those system prompts, yeah,

## 7805:00 - 7840:00

they're quite elaborate. uh and they

## 7840:00 - 7885:00

have direct instructions to avoid

## 7885:00 - 7925:00

certain problems. You can see the mark

## 7925:00 - 7955:00

of the HR team in that system probably.

## 7955:00 - 7980:00

I think there's a deeper issue here

## 7980:00 - 8020:00

which is that we're designing features

## 8020:00 - 8065:00

like this in a way that looks a lot like

## 8065:00 - 8090:00

software that we've been building for

## 8090:00 - 8125:00

decades, right? And so just to

## 8125:00 - 8150:00

illustrate what's possible, let's

## 8150:00 - 8190:00

imagine that Gmail allowed me to not

## 8190:00 - 8235:00

only see but edit this system prompt for

## 8235:00 - 8280:00

myself. I might write a version that

## 8280:00 - 8310:00

instead of saying you are a generic

## 8310:00 - 8340:00

Gmail writing, you know, email writing

## 8340:00 - 8380:00

agent, my version might just say you're

## 8380:00 - 8410:00

Pete, right? You're a 43-year-old

## 8410:00 - 8440:00

husband, you're a father, you're a YC

## 8440:00 - 8480:00

partner, you're busy, and so is everyone

## 8480:00 - 8510:00

you correspond with, and so you do your

## 8510:00 - 8535:00

best to keep emails as short as

## 8535:00 - 8565:00

possible, right? What I've done here is

## 8565:00 - 8590:00

I just take the little program in my

## 8590:00 - 8635:00

brain that is used for writing emails,

## 8635:00 - 8680:00

and I've done my best to explain to

## 8680:00 - 8725:00

Gemini how I do that. And if you just

## 8725:00 - 8775:00

take that same user prompt asking for a

## 8775:00 - 8820:00

draft of an email explaining that my

## 8820:00 - 8850:00

daughter's sick and you use my system

## 8850:00 - 8885:00

prompt rather than the generic

## 8885:00 - 8925:00

one-sizefits-all Gmail system prompt.

## 8925:00 - 8960:00

The draft we get, "Hi Gary, my

## 8960:00 - 8985:00

daughter's sick with the flu, so I can't

## 8985:00 - 9020:00

come in today. Thanks." That sounds like

## 9020:00 - 9045:00

an email that I would have written.

## 9045:00 - 9085:00

Totally. By editing this system prompt,

## 9085:00 - 9140:00

I'm able to explain to the AI model how

## 9140:00 - 9185:00

I write emails in general so that I

## 9185:00 - 9220:00

don't have to do it every single time.

## 9220:00 - 9260:00

And so going back to your question, why

## 9260:00 - 9305:00

did the Gmail team hide decide to hide

## 9305:00 - 9350:00

this system prompt away? My contention

## 9350:00 - 9415:00

is that a lot of AI app developers,

## 9415:00 - 9450:00

including the Gmail team in this case,

## 9450:00 - 9490:00

are treating the system prompt the same

## 9490:00 - 9535:00

way they've been treating code for

## 9535:00 - 9570:00

decades. For, you know, as long as we've

## 9570:00 - 9595:00

had a software industry, there's been a

## 9595:00 - 9635:00

division of labor between me, the user,

## 9635:00 - 9665:00

and you, the developer. The user does

## 9665:00 - 9695:00

not see the code. User doesn't see the

## 9695:00 - 9730:00

code. The developer is the one who is

## 9730:00 - 9760:00

responsible for building the system,

## 9760:00 - 9790:00

defining the system. It's all hidden

## 9790:00 - 9830:00

away, and it's abstracted behind. an

## 9830:00 - 9855:00

interface that I can point and click

## 9855:00 - 9890:00

around to do something. It's more or

## 9890:00 - 9920:00

less one sizefits-all software. That's

## 9920:00 - 9945:00

the only way we've been able to build

## 9945:00 - 9985:00

software up until now is oneizefits-all,

## 9985:00 - 10030:00

right? If you're building an online bank

## 10030:00 - 10065:00

software or a piece of AB testing

## 10065:00 - 10115:00

software, your job as a developer is to

## 10115:00 - 10155:00

go and talk to hundreds or thousands of

## 10155:00 - 10200:00

users and synthesize all of their needs

## 10200:00 - 10260:00

together into one common set of features

## 10260:00 - 10280:00

that you're going to build in your

## 10280:00 - 10315:00

oneizefits-all piece of software. sort

## 10315:00 - 10340:00

of lowest common denominator software.

## 10340:00 - 10380:00

Exactly. Exactly. And that's I think the

## 10380:00 - 10415:00

Gmail system prompt in this case you can

## 10415:00 - 10435:00

think of as the lowest common

## 10435:00 - 10490:00

denominator email writer. It's the safe

## 10490:00 - 10525:00

anyone could use this thing. But what it

## 10525:00 - 10575:00

results in is emails that no individual

## 10575:00 - 10605:00

would actually write. Yeah. No one's

## 10605:00 - 10625:00

getting fired, but this is not the

## 10625:00 - 10635:00

software that's going to take over the

## 10635:00 - 10670:00

world. That's exactly right. You think

## 10670:00 - 10725:00

that developers today are using AI in

## 10725:00 - 10765:00

the previous generation of software

## 10765:00 - 10800:00

development that they've been used to?

## 10800:00 - 10835:00

Yes. Um, and so you use this phrase, the

## 10835:00 - 10870:00

AI horseless carriage. Maybe tell us

## 10870:00 - 10890:00

what you mean by that. This is a

## 10890:00 - 10945:00

reference to early automobile designs

## 10945:00 - 11015:00

that looked a lot like uh carriages with

## 11015:00 - 11050:00

the horse replaced with an engine,

## 11050:00 - 11080:00

right? And there were all sorts of

## 11080:00 - 11120:00

problems with that design. You know, for

## 11120:00 - 11160:00

example, there's less suspension on

## 11160:00 - 11195:00

carriages, which didn't work at high

## 11195:00 - 11220:00

speeds with a vibrating motor, right?

## 11220:00 - 11250:00

That the center of gravity was higher,

## 11250:00 - 11285:00

which made turns harder at high speeds.

## 11285:00 - 11335:00

Basically uh inventing the motor was

## 11335:00 - 11380:00

only a small part of what was needed to

## 11380:00 - 11415:00

produce a vehicle that could take

## 11415:00 - 11435:00

advantage of the it only became useful

## 11435:00 - 11470:00

once you redesign the entire That's

## 11470:00 - 11495:00

exactly right. Right. Yeah. And this

## 11495:00 - 11530:00

phenomena we we see over and over and

## 11530:00 - 11560:00

over again in technology like some some

## 11560:00 - 11610:00

ones that I have lived through when the

## 11610:00 - 11650:00

internet came about. Um a lot of the

## 11650:00 - 11680:00

first search engines were literally just

## 11680:00 - 11715:00

like digitized yellow pages. It was just

## 11715:00 - 11750:00

a directory of listings. And now of

## 11750:00 - 11780:00

course we think like that's silly kind

## 11780:00 - 11810:00

of like Craigslist right that's what it

## 11810:00 - 11845:00

started with when mobile came out the

## 11845:00 - 11870:00

first mobile apps or a lot of the first

## 11870:00 - 11905:00

mobile apps were basically just websites

## 11905:00 - 11955:00

wrapped in a native app wrapper but they

## 11955:00 - 11985:00

didn't take advantage of any of the new

## 11985:00 - 12010:00

technologies available on the mobile

## 12010:00 - 12060:00

phone like GPS like multi-touch and it

## 12060:00 - 12105:00

takes a few years typically to get to

## 12105:00 - 12145:00

the useful bit of the new technology and

## 12145:00 - 12170:00

I guess what what you're claiming Pete

## 12170:00 - 12210:00

is we are like not there yet. I think

## 12210:00 - 12265:00

the the deepest problem here is that

## 12265:00 - 12300:00

when the when the Gmail team set out to

## 12300:00 - 12335:00

build this, they kind of asked, "How can

## 12335:00 - 12400:00

we slot AI into the Gmail application?

## 12400:00 - 12425:00

How do we replace the horse and put an

## 12425:00 - 12465:00

engine in?" That's exactly right. And

## 12465:00 - 12510:00

the the problem with that is that Gmail

## 12510:00 - 12560:00

is an application designed for humans to

## 12560:00 - 12615:00

do work in. Right. The real promise of

## 12615:00 - 12665:00

AI, I think, for many of us is using AI

## 12665:00 - 12720:00

to automate repetitive busy work, right?

## 12720:00 - 12760:00

And a lot of the time I spend on email

## 12760:00 - 12795:00

is repetitive busy work, right? It's

## 12795:00 - 12830:00

it's work that doesn't really need my

## 12830:00 - 12855:00

full brain power, but because we haven't

## 12855:00 - 12890:00

had the technology requires it, right?

## 12890:00 - 12930:00

And so I give a little example in my

## 12930:00 - 12985:00

essay of just, you know, using these

## 12985:00 - 13020:00

simple techniques, what you could do

## 13020:00 - 13055:00

with an email inbox. And here's that

## 13055:00 - 13110:00

example. So this is an example of an

## 13110:00 - 13140:00

email inbox. It's got a bunch of

## 13140:00 - 13190:00

messages on the right hand side and

## 13190:00 - 13235:00

there's an agent operating in this inbox

## 13235:00 - 13270:00

and it's an instead of an email writing

## 13270:00 - 13310:00

agent, it's an email reading agent. On

## 13310:00 - 13340:00

the the left hand side here, you can see

## 13340:00 - 13370:00

this is a system prompt that I wrote

## 13370:00 - 13415:00

that just tells this agent what to do

## 13415:00 - 13465:00

with each email. And the agent can

## 13465:00 - 13500:00

assign a label to an incoming email. It

## 13500:00 - 13545:00

can archive it. uh it can put a color on

## 13545:00 - 13585:00

that label and it can write a draft.

## 13585:00 - 13615:00

Right? Those are the things this agent

## 13615:00 - 13650:00

can do and my instructions are just what

## 13650:00 - 13690:00

to do for each email. So if the email is

## 13690:00 - 13740:00

from my wife, draft a reply and label it

## 13740:00 - 13780:00

personal. If it's from my boss, draft a

## 13780:00 - 13820:00

reply and make it priority one, right?

## 13820:00 - 13855:00

Which is just one one notch lower than

## 13855:00 - 13900:00

emails from my wife. Uh and for anyone

## 13900:00 - 13950:00

else at YC where I work, a YC label and

## 13950:00 - 13980:00

give it priority two, right? Right? If

## 13980:00 - 14005:00

it's from a founder who needs help, call

## 14005:00 - 14035:00

it, you know, put a founders's label on

## 14035:00 - 14065:00

it. Make a right. This is my sort of

## 14065:00 - 14100:00

internal again mental model for how I

## 14100:00 - 14125:00

organize my email. And I'm just

## 14125:00 - 14170:00

explaining to Gemini how I do this work

## 14170:00 - 14200:00

so that it can do it on my behalf. One

## 14200:00 - 14225:00

thing I find interesting about this is

## 14225:00 - 14260:00

this is really the code. This is the

## 14260:00 - 14285:00

programming you are doing for this

## 14285:00 - 14320:00

agent. But if you read it, it's pretty

## 14320:00 - 14355:00

accessible, right? It says if it's a

## 14355:00 - 14395:00

techreated email, label it tech. If it's

## 14395:00 - 14420:00

somebody trying to sell me something,

## 14420:00 - 14460:00

archive it. And this is like a a great

## 14460:00 - 14490:00

example of how the LLM technology is

## 14490:00 - 14530:00

actually good enough to let

## 14530:00 - 14575:00

non-programmers program these apps. You

## 14575:00 - 14595:00

know, the way that I think of these

## 14595:00 - 14660:00

these these models, a super smart, you

## 14660:00 - 14695:00

know, fresh grad right out of college

## 14695:00 - 14730:00

that can do anything pretty well, but

## 14730:00 - 14765:00

has no idea what to do, you know, and

## 14765:00 - 14800:00

the missing step is giving me the

## 14800:00 - 14835:00

ability to teach it how to do work that

## 14835:00 - 14860:00

I don't want to do, which is what I've

## 14860:00 - 14880:00

done here. And you're right, it's

## 14880:00 - 14915:00

completely accessible. One of the sort

## 14915:00 - 14950:00

of pieces of push back I got when I

## 14950:00 - 14975:00

started talking about letting users just

## 14975:00 - 15000:00

write their own system prompts was like,

## 15000:00 - 15025:00

well, most people aren't technical. They

## 15025:00 - 15055:00

don't know how to do that. Which I think

## 15055:00 - 15085:00

is true. This isn't a skill we're born

## 15085:00 - 15130:00

with. But in doing this myself, I found

## 15130:00 - 15170:00

it really intuitive. It's basically like

## 15170:00 - 15200:00

thinking of the way that I make a

## 15200:00 - 15235:00

decision and then trying to explain to

## 15235:00 - 15275:00

this AI model how to do it. And as long

## 15275:00 - 15315:00

as you can kind of um watch it do the

## 15315:00 - 15360:00

job and and give it feedback by by

## 15360:00 - 15385:00

adjusting this prompt, it's pretty

## 15385:00 - 15415:00

intuitive. And so, for example, here,

## 15415:00 - 15445:00

here's what happens when I apply this

## 15445:00 - 15470:00

little agent to each one of the emails

## 15470:00 - 15520:00

in this inbox.

## 15520:00 - 15575:00

Amazing. I love this. Um, this is a this

## 15575:00 - 15610:00

is an essay. Uh, but it's not static. I

## 15610:00 - 15625:00

love the fact that you've built this

## 15625:00 - 15650:00

little widget so people can actually go

## 15650:00 - 15680:00

in, they can edit the system prompt

## 15680:00 - 15715:00

themselves to kind of reformat it the

## 15715:00 - 15735:00

way they want and rerun it. I think it's

## 15735:00 - 15775:00

such a smart way to to convey this kind

## 15775:00 - 15805:00

of idea. One of my favorite things is

## 15805:00 - 15835:00

building demos. And this felt like an

## 15835:00 - 15860:00

intuitive way to start talking about

## 15860:00 - 15915:00

some of these concepts. And this is just

## 15915:00 - 15965:00

another example of how powerful AI makes

## 15965:00 - 15990:00

you feel when you're building with it.

## 15990:00 - 16010:00

When you're just interacting with these

## 16010:00 - 16030:00

models. How did you build this by the

## 16030:00 - 16065:00

way? I vibe coded the whole thing. So I

## 16065:00 - 16100:00

wrote, you know, this is I mean like

## 16100:00 - 16145:00

ironically enough, these AI models are

## 16145:00 - 16170:00

not actually that useful to help you

## 16170:00 - 16210:00

write things from scratch, right? The

## 16210:00 - 16260:00

part where I used AI was describing a

## 16260:00 - 16290:00

demo that I thought would help

## 16290:00 - 16325:00

communicate the the point I was trying

## 16325:00 - 16355:00

to make and then watching it appear,

## 16355:00 - 16380:00

right? Like it's it's absolutely

## 16380:00 - 16420:00

magical. It's astonishing how good these

## 16420:00 - 16450:00

uh especially the coding agents. I mean,

## 16450:00 - 16500:00

I rebuilt my entire my um I was on

## 16500:00 - 16550:00

Tumblr and I migrated my blog to custom

## 16550:00 - 16580:00

software I wrote in one hour on a train

## 16580:00 - 16610:00

journey. The coding agents especially

## 16610:00 - 16655:00

just seem so far ahead of of all the

## 16655:00 - 16680:00

other general purpose agents right now.

## 16680:00 - 16725:00

Yes. And to me uh like we will have

## 16725:00 - 16780:00

caught up when everybody uh has the same

## 16780:00 - 16810:00

experience that we have when we're using

## 16810:00 - 16845:00

these coding agents in their particular

## 16845:00 - 16870:00

domain. Right? So when accountants can

## 16870:00 - 16915:00

build uh accounting agents that do just

## 16915:00 - 16945:00

all of the repetitive workflows on their

## 16945:00 - 16980:00

behalf, when lawyers can build lawyering

## 16980:00 - 17010:00

agents that do the repetitive workflows

## 17010:00 - 17050:00

on their behalf is basically every

## 17050:00 - 17090:00

profession I think will have its cursor

## 17090:00 - 17125:00

moment or its windsurf moment. Why is

## 17125:00 - 17160:00

cursor windsurf or claude code so far

## 17160:00 - 17205:00

ahead of you know, lawyer agents or

## 17205:00 - 17230:00

accounting agents. I think there's two

## 17230:00 - 17295:00

reasons. Um, the first is that these AI

## 17295:00 - 17350:00

models are incredibly good at processing

## 17350:00 - 17395:00

text, right? So, if I can write a good

## 17395:00 - 17425:00

description of a thing I want, they can

## 17425:00 - 17470:00

process that description, that prompt,

## 17470:00 - 17505:00

and turn it into a bunch of code. Right?

## 17505:00 - 17535:00

This is going back to why it was so

## 17535:00 - 17565:00

annoying to write that original email

## 17565:00 - 17605:00

prompt is like these agents aren't good

## 17605:00 - 17625:00

at writing from scratch. They're good at

## 17625:00 - 17660:00

processing instructions and doing and

## 17660:00 - 17695:00

and turning them into to some text

## 17695:00 - 17735:00

output, right? For code, that's actually

## 17735:00 - 17765:00

really useful, right? If I can describe

## 17765:00 - 17800:00

in English what I'm looking for, an

## 17800:00 - 17835:00

agent can output code that does this and

## 17835:00 - 17875:00

it's remarkably effective. This is just

## 17875:00 - 17915:00

a domain where these agents are are

## 17915:00 - 17945:00

really powerful. I think the other

## 17945:00 - 17990:00

reason though is that developer tools

## 17990:00 - 18040:00

are power tools, right? Developer tools

## 18040:00 - 18090:00

by definition allow you to to get to the

## 18090:00 - 18120:00

bare metal, right? to get under the hood

## 18120:00 - 18140:00

of what whatever it is you're working

## 18140:00 - 18185:00

with. And so the teams that built these

## 18185:00 - 18245:00

these tools allowed me full access to

## 18245:00 - 18275:00

have this agent do whatever I wanted it

## 18275:00 - 18310:00

to do. They didn't spend a lot of time

## 18310:00 - 18330:00

making sure that I didn't do anything

## 18330:00 - 18370:00

that was embarrassing to Windsurf or

## 18370:00 - 18410:00

embarrassing to anyone. I'm allowed to

## 18410:00 - 18430:00

just interact directly with the model

## 18430:00 - 18460:00

and use the full power. Whereas I think

## 18460:00 - 18490:00

a lot of a lot of other domains were

## 18490:00 - 18530:00

still using this sort of like kid glove

## 18530:00 - 18560:00

mentality of like oh don't don't let

## 18560:00 - 18590:00

them use the full power of these models.

## 18590:00 - 18655:00

I hope we're able to move beyond u this

## 18655:00 - 18690:00

this moment in time where there's so

## 18690:00 - 18725:00

much assumed liability on the part of

## 18725:00 - 18755:00

the application developers for what

## 18755:00 - 18785:00

these models do. Well, I think the

## 18785:00 - 18820:00

interesting point is if you do change

## 18820:00 - 18875:00

the model where the user is in charge or

## 18875:00 - 18900:00

at least has access to the system

## 18900:00 - 18955:00

prompt, then the u repercussions of that

## 18955:00 - 18985:00

are on the user and not on the company

## 18985:00 - 19035:00

that built the tool. Yeah. It's like um

## 19035:00 - 19070:00

Google put Gmail out and if you write an

## 19070:00 - 19100:00

email full of profanity that's on you,

## 19100:00 - 19130:00

right? Like exactly the same way like if

## 19130:00 - 19160:00

you change the system prompt to act

## 19160:00 - 19200:00

like, you know, a violent jerk, like

## 19200:00 - 19220:00

that's on you. That's not on Google.

## 19220:00 - 19265:00

Yeah. It's it's a shift in mentality. Uh

## 19265:00 - 19300:00

giving giving AI to the user as a tool

## 19300:00 - 19330:00

and they can use it for whatever their

## 19330:00 - 19375:00

purposes are versus feeling like you as

## 19375:00 - 19415:00

a developer have to be responsible for

## 19415:00 - 19445:00

everything these these models output and

## 19445:00 - 19465:00

therefore you nerf it and it's not

## 19465:00 - 19505:00

useful. So I broadly agree with

## 19505:00 - 19535:00

everything you've said so far but I I

## 19535:00 - 19580:00

had some questions and the first one is

## 19580:00 - 19635:00

do you think u the vast majority of

## 19635:00 - 19660:00

people are able to write these kind of

## 19660:00 - 19705:00

system prompts? I think the answer today

## 19705:00 - 19725:00

is

## 19725:00 - 19765:00

no. But I think the answer to that in

## 19765:00 - 19805:00

the near future will be yes. Why is

## 19805:00 - 19845:00

that? When I was growing up computers

## 19845:00 - 19885:00

were still seen as a power tool that

## 19885:00 - 19920:00

only nerds really knew how to use,

## 19920:00 - 19965:00

right? Um, and today that's just no

## 19965:00 - 19995:00

longer the case. All of us use computers

## 19995:00 - 20025:00

all the time. It's no longer like

## 20025:00 - 20055:00

remarkable or interesting for somebody

## 20055:00 - 20090:00

to use to be able to use a computer,

## 20090:00 - 20120:00

right? And so what happened is we all

## 20120:00 - 20145:00

just sort of figured out how to use

## 20145:00 - 20175:00

these things and the interfaces got

## 20175:00 - 20210:00

better, right? It's it's the tech the

## 20210:00 - 20235:00

tech got better and we learned how to

## 20235:00 - 20265:00

use it in time. And so it is

## 20265:00 - 20295:00

unremarkable, right? And I think the

## 20295:00 - 20315:00

same thing is going to happen with

## 20315:00 - 20350:00

prompting. So I think this is actually

## 20350:00 - 20380:00

going to happen a lot faster with

## 20380:00 - 20420:00

prompting because pro writing a prompt

## 20420:00 - 20470:00

is a lot more accessible than you know

## 20470:00 - 20520:00

operating your file system manager on on

## 20520:00 - 20545:00

your computer. You don't need to

## 20545:00 - 20580:00

understand much except to be able to

## 20580:00 - 20615:00

explain yourself in English or whatever

## 20615:00 - 20655:00

language you speak. Having done this uh

## 20655:00 - 20705:00

several times my myself now it's

## 20705:00 - 20740:00

surprisingly intuitive. Right? Thinking

## 20740:00 - 20770:00

about okay how do I write an email?

## 20770:00 - 20805:00

Right? It's it's a bit of a toy example

## 20805:00 - 20835:00

but it's kind of fun. You can write your

## 20835:00 - 20865:00

little internal algorithm for it and

## 20865:00 - 20895:00

then you can watch and if it gets the

## 20895:00 - 20940:00

tone right, your system prompt is is is

## 20940:00 - 20960:00

right. Yeah. And I agree with you on

## 20960:00 - 20995:00

that. I think basically everyone will be

## 20995:00 - 21035:00

able to do this. I'm not sure everyone

## 21035:00 - 21065:00

will want to or to have the initiative

## 21065:00 - 21095:00

or agent like we're three founders

## 21095:00 - 21125:00

sitting here. We love to tinker with

## 21125:00 - 21150:00

this stuff. Like you're telling me about

## 21150:00 - 21205:00

your mom using uh like my mom uses Gmail

## 21205:00 - 21235:00

every day, but is she going to write a

## 21235:00 - 21265:00

system prompt? Like probably probably

## 21265:00 - 21305:00

not. Yeah, maybe. I So I don't know. I'

## 21305:00 - 21340:00

I've learned not to be pessimistic about

## 21340:00 - 21380:00

what what users can learn. Um, but I

## 21380:00 - 21420:00

agree with with the point, Rich, is that

## 21420:00 - 21450:00

I don't think I'd want to write my own

## 21450:00 - 21475:00

email writing system prompt from

## 21475:00 - 21520:00

scratch. I'd like to have that option,

## 21520:00 - 21555:00

right? But I've been using Gmail for 20

## 21555:00 - 21590:00

years, right? And there are 20 years of

## 21590:00 - 21645:00

my email history that a good product

## 21645:00 - 21685:00

could use to to create a draft prompt

## 21685:00 - 21730:00

for me, right? The idea that, take a

## 21730:00 - 21760:00

human analogy, you hire a new employee,

## 21760:00 - 21780:00

you hire an assistant. The idea that

## 21780:00 - 21815:00

you're going to sit down and write out

## 21815:00 - 21850:00

30 pages of instructions of how you do

## 21850:00 - 21880:00

every single thing in your life is

## 21880:00 - 21910:00

possible, but none of us actually do it.

## 21910:00 - 21935:00

You sort of you give this gradual

## 21935:00 - 21965:00

training and if they were able to go

## 21965:00 - 21980:00

through and read all your previous

## 21980:00 - 22020:00

emails, they kind of learn and then you

## 22020:00 - 22050:00

um you kind of interact with them step

## 22050:00 - 22075:00

by step and they write a few emails and

## 22075:00 - 22090:00

you check the drafts and when you're

## 22090:00 - 22115:00

comfortable, you say, "I didn't want to

## 22115:00 - 22140:00

check the drafts anymore. Send it." And

## 22140:00 - 22160:00

then if you spot something that's not

## 22160:00 - 22195:00

quite right, you say, "Oh, no, no, no. I

## 22195:00 - 22220:00

would have phrased that this way or this

## 22220:00 - 22265:00

other way." and the human would take

## 22265:00 - 22295:00

that feedback and edit their own system

## 22295:00 - 22315:00

prompt. So, so Pete, you've been

## 22315:00 - 22355:00

actually doing this at YC, right? You've

## 22355:00 - 22380:00

built some internal tools that our

## 22380:00 - 22425:00

finance team or our legal team uses. Um,

## 22425:00 - 22450:00

and it's it feels like the interaction

## 22450:00 - 22485:00

has been exactly what Tom just described

## 22485:00 - 22525:00

where you literally go sit next to a

## 22525:00 - 22565:00

finance person and you ask them like,

## 22565:00 - 22605:00

"Hey, tell me how you do this this

## 22605:00 - 22630:00

workflow. Like, show me what you do."

## 22630:00 - 22665:00

And then you write some system prompt

## 22665:00 - 22705:00

for them. They try it. It doesn't do it

## 22705:00 - 22730:00

quite right. they edit the system prompt

## 22730:00 - 22755:00

with you. So, it's kind of this like

## 22755:00 - 22780:00

back and forth iterative model that

## 22780:00 - 22815:00

you're suggesting. Yeah. And I'd go

## 22815:00 - 22835:00

further than that. I think there's like

## 22835:00 - 22870:00

a missing tool in AI app development,

## 22870:00 - 22900:00

which is like not everyone has a pizza

## 22900:00 - 22935:00

next to them, but you could have an AI

## 22935:00 - 22960:00

system prompt writer sitting next to you

## 22960:00 - 23005:00

to take you say, "No, this wasn't right

## 23005:00 - 23030:00

or I would have rewritten it like this."

## 23030:00 - 23060:00

And it will translate that back into a

## 23060:00 - 23095:00

system prompt and kind of self-edit or

## 23095:00 - 23140:00

autoupdate. Absolutely. Right. And and

## 23140:00 - 23200:00

these are great examples of um UI

## 23200:00 - 23240:00

conventions that we just haven't figured

## 23240:00 - 23275:00

out yet, right? And and you can see

## 23275:00 - 23305:00

people are experimenting with different

## 23305:00 - 23335:00

models here. Some of the foundation

## 23335:00 - 23380:00

model labs have started building memory

## 23380:00 - 23410:00

into their into their chat bots, right?

## 23410:00 - 23470:00

Which is that's one um mechanism for

## 23470:00 - 23500:00

taking context that I've shared over

## 23500:00 - 23550:00

time and storing it forever, right? Um,

## 23550:00 - 23575:00

I haven't had great experiences with

## 23575:00 - 23600:00

that because again it's it's sort of

## 23600:00 - 23630:00

it's treated like a black box where I

## 23630:00 - 23655:00

can't actually see what it has

## 23655:00 - 23685:00

internalized and what it's stored. My

## 23685:00 - 23715:00

big contention here is that because this

## 23715:00 - 23745:00

is all just English, we no longer have

## 23745:00 - 23775:00

to treat these things like black boxes.

## 23775:00 - 23805:00

The system prompt is almost like this

## 23805:00 - 23835:00

this document that you don't have to

## 23835:00 - 23865:00

edit if you don't want to. But in the at

## 23865:00 - 23885:00

the limit, if there's something really

## 23885:00 - 23910:00

goes wrong, you can go in and tinker

## 23910:00 - 23945:00

with it if you want. But probably for

## 23945:00 - 23970:00

most people, the AI will autogenerate

## 23970:00 - 24010:00

it. it will um look through your

## 24010:00 - 24050:00

previous work to to customize it to you

## 24050:00 - 24080:00

and take your feedback on ongoing basis

## 24080:00 - 24115:00

to kind of edit this system prompt and

## 24115:00 - 24145:00

you know the kind of break glass case is

## 24145:00 - 24165:00

you go and edit the file and be like no

## 24165:00 - 24190:00

no no I really don't want this to happen

## 24190:00 - 24245:00

but I I'd suggest I think in in 5 years

## 24245:00 - 24275:00

for 99% of people they're not touching

## 24275:00 - 24305:00

the system prompt but the system prompt

## 24305:00 - 24330:00

is custom to them. I think that's

## 24330:00 - 24355:00

possible. It'll be interesting to see

## 24355:00 - 24380:00

how this plays out. Some of the work

## 24380:00 - 24430:00

that we've done at YC, building agents

## 24430:00 - 24470:00

to automate some of the repetitive work

## 24470:00 - 24510:00

that we and our teammates do on a

## 24510:00 - 24550:00

regular basis actually suggests to me

## 24550:00 - 24600:00

that writing prompts is going to be part

## 24600:00 - 24630:00

of the day-to-day flow for a lot of

## 24630:00 - 24675:00

people. I agree in the short term, but I

## 24675:00 - 24725:00

I think my contention is like there's a

## 24725:00 - 24760:00

a higher level of of abstraction on top

## 24760:00 - 24790:00

of system prompt writing that you

## 24790:00 - 24815:00

shouldn't actually have to go and edit

## 24815:00 - 24845:00

the system prompt that you're able to

## 24845:00 - 24890:00

like nudge or like say no no that okay

## 24890:00 - 24915:00

here's a new term sheet that's a new

## 24915:00 - 24935:00

term we've never seen before and here's

## 24935:00 - 24970:00

how I would think about it and the goes

## 24970:00 - 25000:00

thank you very much I will take that

## 25000:00 - 25025:00

distill it down into system prompt and

## 25025:00 - 25060:00

and autoedit system prompt rather than

## 25060:00 - 25090:00

Alex having to look up this like 50page

## 25090:00 - 25115:00

document and go like I'm going to change

## 25115:00 - 25140:00

that specific line you know what I It's

## 25140:00 - 25170:00

like a a level of abstraction on top of

## 25170:00 - 25190:00

raw kind of raw dogging the system

## 25190:00 - 25225:00

prompt. I think we'll probably have

## 25225:00 - 25275:00

tools that make it easier to teach an AI

## 25275:00 - 25315:00

over time rather than going up and and

## 25315:00 - 25350:00

editing in, you know, a 10 or 50page

## 25350:00 - 25380:00

prompt uh every time every single time

## 25380:00 - 25425:00

you want to do this. And I hope that

## 25425:00 - 25460:00

developers stop treating these prompts

## 25460:00 - 25505:00

like black boxes. Being able to look at

## 25505:00 - 25540:00

the ground truth of what this agent is

## 25540:00 - 25585:00

being instructed to do on my behalf is

## 25585:00 - 25620:00

incredibly valuable and it seems to be

## 25620:00 - 25645:00

totally missing from a lot of

## 25645:00 - 25675:00

applications. I 100% agree with that.

## 25675:00 - 25700:00

So, so we've been talking a lot about

## 25700:00 - 25730:00

the prompting, right? And and Tom is

## 25730:00 - 25760:00

kind of saying like there's a going to

## 25760:00 - 25800:00

be a bunch of innovation on how we write

## 25800:00 - 25835:00

system prompts or how we edit them or or

## 25835:00 - 25870:00

iterate on them. In the essay, you also

## 25870:00 - 25905:00

talk about tooling which I think is a

## 25905:00 - 25930:00

really important and interesting topic

## 25930:00 - 25960:00

as well. Talk talk to us about that.

## 25960:00 - 25995:00

Yeah, sure. So, so if developers aren't

## 25995:00 - 26020:00

the ones who have to write all these

## 26020:00 - 26050:00

system prompts from scratch, what are

## 26050:00 - 26085:00

they going to focus on? I think the

## 26085:00 - 26130:00

promise of AI for many of us is that it

## 26130:00 - 26160:00

gives us software or it allows us to

## 26160:00 - 26200:00

build software that the user can program

## 26200:00 - 26235:00

to do whatever they want using only

## 26235:00 - 26270:00

natural language. The thing that these

## 26270:00 - 26305:00

agents need in order to be able to do

## 26305:00 - 26360:00

anything useful, we call tools. If we go

## 26360:00 - 26400:00

back to my little email reading agent

## 26400:00 - 26435:00

here, the tools that this agent has

## 26435:00 - 26470:00

access to are a tool for labeling an

## 26470:00 - 26505:00

email, a tool for archiving an email,

## 26505:00 - 26540:00

and a tool for writing a draft. You

## 26540:00 - 26575:00

could imagine many other tools that

## 26575:00 - 26615:00

would make this agent more powerful and

## 26615:00 - 26645:00

more able to do a lot of the busy work

## 26645:00 - 26670:00

that I have to spend my own time on

## 26670:00 - 26695:00

right now, right? And so, a lot of the

## 26695:00 - 26740:00

emails I get are not emails that take a

## 26740:00 - 26770:00

lot of my brain power to handle, but

## 26770:00 - 26795:00

they just need to get done. Paying

## 26795:00 - 26840:00

bills, right? doing introductions and

## 26840:00 - 26865:00

handoffs, right? The number of times

## 26865:00 - 26890:00

that I've had to create a draft and put

## 26890:00 - 26925:00

this, you know, a certain person in BCC

## 26925:00 - 26970:00

and like um it's maddening to have to do

## 26970:00 - 27005:00

this stuff uh over and over again. The

## 27005:00 - 27050:00

point is is that an email in a lot of

## 27050:00 - 27100:00

ways is like my inbox uh you know it's

## 27100:00 - 27130:00

my to-do list or a whole bunch of chores

## 27130:00 - 27170:00

in life, right? The very few emails that

## 27170:00 - 27210:00

I write are really heartfelt original

## 27210:00 - 27240:00

thinking. A lot of it is sort of

## 27240:00 - 27280:00

transactional, you know, and with tools,

## 27280:00 - 27315:00

this email reading agent could handle a

## 27315:00 - 27345:00

lot of that, especially across things

## 27345:00 - 27405:00

like Slack and your calendar and your

## 27405:00 - 27430:00

notion or your Jira or your linear or

## 27430:00 - 27450:00

whatever. There's a company in the

## 27450:00 - 27480:00

current batch called Den basically

## 27480:00 - 27505:00

building cursor for knowledge work

## 27505:00 - 27535:00

that's trying to chain together all of

## 27535:00 - 27565:00

these different MCP servers, which

## 27565:00 - 27595:00

basically a way to call tools for agents

## 27595:00 - 27630:00

so that if your boss, you know, your

## 27630:00 - 27660:00

bossy sends you a message on Slack and

## 27660:00 - 27695:00

says, "Hey, uh, review these terms and

## 27695:00 - 27725:00

conditions." You pull it from Google

## 27725:00 - 27760:00

Docs, you review it, maybe the AI sends

## 27760:00 - 27785:00

it via email to your legal team, they

## 27785:00 - 27815:00

review it, and then you publish it by

## 27815:00 - 27845:00

GitHub. And all of this is controlled

## 27845:00 - 27880:00

via one place with kind of agents

## 27880:00 - 27900:00

calling these tools from different

## 27900:00 - 27930:00

places. And you just sort of sit sit

## 27930:00 - 27965:00

back. It's like a Steve Jobs described

## 27965:00 - 27995:00

software as a sort of as a bicycle for

## 27995:00 - 28025:00

the mind. This feels like I don't know

## 28025:00 - 28055:00

like a rocket ship for the mind. It's

## 28055:00 - 28085:00

incredibly powerful, right? Right. And

## 28085:00 - 28120:00

we built a we built an early version of

## 28120:00 - 28145:00

this inside of YC and we're already

## 28145:00 - 28195:00

seeing employees of YC automate parts of

## 28195:00 - 28225:00

their job that are easy to automate. And

## 28225:00 - 28250:00

and the difference that these tools

## 28250:00 - 28280:00

provide is it takes an agent which

## 28280:00 - 28310:00

previously could only be basically like

## 28310:00 - 28350:00

a Q&A, right? A question and answer

## 28350:00 - 28395:00

thing into something that can go off and

## 28395:00 - 28425:00

accomplish things in the world on your

## 28425:00 - 28470:00

behalf. Yeah. I I kind of hate the the

## 28470:00 - 28500:00

kind of chatbot paradigm. Like it was

## 28500:00 - 28535:00

the easiest. It was the way to bring the

## 28535:00 - 28565:00

most basic LLM experience to the whole

## 28565:00 - 28610:00

world. You know, we had GPT before chat

## 28610:00 - 28640:00

GPT and chat GPT brought it to the

## 28640:00 - 28675:00

mainstream, but now every product is

## 28675:00 - 28700:00

just embedding this chat agent in it.

## 28700:00 - 28725:00

It's like that's not the way this stuff

## 28725:00 - 28750:00

should be used in almost every case. I

## 28750:00 - 28785:00

totally agree because we started with

## 28785:00 - 28825:00

chat bots, a lot of us developers and

## 28825:00 - 28855:00

users are sort of anchored in this place

## 28855:00 - 28885:00

where the thing that LLMs are great at

## 28885:00 - 28940:00

is producing text. uh where I think what

## 28940:00 - 28980:00

we're what we're trying to argue here is

## 28980:00 - 29030:00

these LLMs are capable of automating

## 29030:00 - 29075:00

work on our behalf, accomplishing things

## 29075:00 - 29105:00

in the world on our behalf so that we

## 29105:00 - 29130:00

don't have to. And that's the promise

## 29130:00 - 29150:00

and I think that's an amazing future. I

## 29150:00 - 29180:00

look forward to it. Me too. This has

## 29180:00 - 29215:00

been so interesting. Pete, how do you

## 29215:00 - 29240:00

think founders should be thinking about

## 29240:00 - 29260:00

this when building their companies?

## 29260:00 - 29290:00

That's a great question. I think this is

## 29290:00 - 29315:00

one of the most exciting time to be a

## 29315:00 - 29375:00

founder because almost every tool that

## 29375:00 - 29415:00

we've been using for decades can be

## 29415:00 - 29455:00

rethought from the ground up with AI and

## 29455:00 - 29500:00

I think the AI native version of a lot

## 29500:00 - 29545:00

of tools will look different from the

## 29545:00 - 29575:00

versions we we're used to using. Right.

## 29575:00 - 29610:00

What I what I showed here looks pretty

## 29610:00 - 29640:00

different from an email client that I've

## 29640:00 - 29675:00

been using for most of my life. Yeah. So

## 29675:00 - 29695:00

they've got to go beyond simply like

## 29695:00 - 29720:00

embedding a chatbot inside their

## 29720:00 - 29755:00

existing product. Yes. Instead of asking

## 29755:00 - 29810:00

how do I insert AI into my tool, it's

## 29810:00 - 29840:00

how would I design this tool from

## 29840:00 - 29885:00

scratch to offload as much repetitive

## 29885:00 - 29915:00

work from the user as possible so they

## 29915:00 - 29940:00

can focus on what's important. All

## 29940:00 - 29960:00

right, Pete, thanks for joining us

## 29960:00 - 29980:00

today. Thank you for having me. See you

## 29980:00 - 30030:00

on the next episode.

## 30030:00+

[Music]

