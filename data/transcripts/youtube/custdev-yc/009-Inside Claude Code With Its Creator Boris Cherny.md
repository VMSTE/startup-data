---
source: https://www.youtube.com/watch?v=PQU9o_5rHC4
title: Inside Claude Code With Its Creator Boris Cherny
author: Y Combinator
date: 2026-02-17
views: 195391
description: >-
  A very special guest on this episode of the Lightcone! Boris Cherny, the
  creator of Claude Code, sits down to share the incredible journey of
  developing one of the most transformative coding tools of the AI era. 


  00:00 Intro

  01:45 The most surprising moment in the rise of Claude Code

  02:38 How Boris came up with the idea for Claude Code

  05:38 The elegant simplicity of terminals

  07:09 The first use cases

  09:00 What’s in Boris’ CLAUDE.md?

  11:29 How do you decide the terminal’s verbosity? 

  15:44 Beginner’s mindset is key as the models improve

  18:56 Hyper specialists vs hyper generalists

  21:51 The vision for Claude teams

  23:48 Subagents

  25:12 A world without plan mode? 

  28:38 Tips for founders to build for the future

  30:07 How much life does the terminal still have? 

  30:57 Advice for dev tool founders

  32:11 Claude Code and TypeScript parallels 

  35:34 Designing for the terminal was hard

  37:36 Other advice for builders

  40:31 Productivity per engineer

  41:36 Why Boris chose to join Anthropic 

  44:46 How coding will change

  46:22 Outro


  Apply to Y Combinator: https://www.ycombinator.com/apply

  Work at a startup: https://www.ycombinator.com/jobs
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:38:18.317Z
---

# Inside Claude Code With Its Creator Boris Cherny

## 00:00 - 20:00

At Enthropic, the way that we thought

## 20:00 - 55:00

about it is we don't build for the model

## 55:00 - 85:00

of today. We build for the model six

## 85:00 - 110:00

months from now. That's actually like

## 110:00 - 140:00

still my advice to to founders that are

## 140:00 - 170:00

building on LLM. Just try to think about

## 170:00 - 200:00

like what is that frontier where the

## 200:00 - 230:00

model is not very good at today cuz it's

## 230:00 - 255:00

going to get good at it. All of Quad

## 255:00 - 280:00

Code has just been written and rewritten

## 280:00 - 300:00

and rewritten and rewritten over and

## 300:00 - 330:00

over and over. There is no part of Quad

## 330:00 - 355:00

Code that was around 6 months ago. You

## 355:00 - 380:00

try a thing, you give it to users, you

## 380:00 - 410:00

talk to users, you learn, and then

## 410:00 - 430:00

eventually you might end up at a good

## 430:00 - 455:00

idea. Sometimes you don't. Are you also

## 455:00 - 475:00

in the back of your mind thinking that

## 475:00 - 510:00

maybe like in 6 months you won't need to

## 510:00 - 535:00

prompt that explicitly? Like the model

## 535:00 - 555:00

will just be good enough to figure out

## 555:00 - 565:00

on its own?

## 565:00 - 605:00

>> Maybe in a month,

## 605:00 - 635:00

>> no more need for plan mode in a month.

## 635:00 - 780:00

>> Oh my god.

## 780:00 - 815:00

Welcome to another episode of the light

## 815:00 - 850:00

cone and today we have an extremely

## 850:00 - 890:00

special guest, Boris Churnney, the

## 890:00 - 955:00

creator engineer of Claude Code. Boris,

## 955:00 - 975:00

thanks for joining us.

## 975:00 - 990:00

>> Thanks for having me.

## 990:00 - 1010:00

>> Thanks for creating a thing that has

## 1010:00 - 1040:00

taken away my sleep for about 3 weeks

## 1040:00 - 1085:00

straight.

## 1085:00 - 1125:00

>> I am very addicted to Cloud Code and uh

## 1125:00 - 1165:00

it feels like rocket boosters. Has it

## 1165:00 - 1205:00

felt like this for people like for you

## 1205:00 - 1230:00

know months at this point. I think it

## 1230:00 - 1275:00

was like end of November is where uh a

## 1275:00 - 1310:00

lot of my friends said like something

## 1310:00 - 1320:00

changed.

## 1320:00 - 1350:00

>> I remember for me I felt this way when I

## 1350:00 - 1380:00

first created Quad Code and I didn't yet

## 1380:00 - 1405:00

know if I was on to something. I kind of

## 1405:00 - 1430:00

felt like I was on to something and then

## 1430:00 - 1460:00

that's when I wasn't sleeping.

## 1460:00 - 1470:00

>> Yeah.

## 1470:00 - 1495:00

>> And that was just like three straight

## 1495:00 - 1505:00

months.

## 1505:00 - 1555:00

>> This was uh September 2024. Yeah. It was

## 1555:00 - 1580:00

like three straight months. I I didn't

## 1580:00 - 1610:00

take a single day vacation. Worked

## 1610:00 - 1630:00

through the weekends. Worked every

## 1630:00 - 1660:00

single night. I was just like, "Oh my

## 1660:00 - 1680:00

god, this is I think this is going to be

## 1680:00 - 1725:00

a thing. I don't know if it's useful yet

## 1725:00 - 1745:00

because it it couldn't actually code

## 1745:00 - 1755:00

yet."

## 1755:00 - 1805:00

>> If you look back on uh those moments to

## 1805:00 - 1840:00

now, like what would be like the most

## 1840:00 - 1870:00

surprising thing about this moment right

## 1870:00 - 1880:00

now?

## 1880:00 - 1905:00

>> It's unbelievable that we're still using

## 1905:00 - 1930:00

a terminal. That was supposed to be the

## 1930:00 - 1945:00

starting point. I didn't think that

## 1945:00 - 1965:00

would be the ending point. And then the

## 1965:00 - 2000:00

second one is that it's even useful cuz

## 2000:00 - 2035:00

uh you know at the beginning it didn't

## 2035:00 - 2070:00

really write code. Even in February when

## 2070:00 - 2110:00

we G it wrote maybe like 10% of my code

## 2110:00 - 2125:00

or something like that. I didn't really

## 2125:00 - 2145:00

use it to write code. it wasn't very

## 2145:00 - 2170:00

good at it. I still wrote most of my

## 2170:00 - 2225:00

code by hand. Uh so the fact that it it

## 2225:00 - 2265:00

actually like our bets paid off and it

## 2265:00 - 2300:00

got good at the thing that we thought it

## 2300:00 - 2320:00

was going to get good at because it

## 2320:00 - 2350:00

wasn't obvious. At Enthropic, the way

## 2350:00 - 2380:00

that we thought about it is we don't

## 2380:00 - 2405:00

build for the model of today. We build

## 2405:00 - 2450:00

for the model 6 months from now. And

## 2450:00 - 2470:00

that's actually like still my advice to

## 2470:00 - 2520:00

to founders that are building on LLM is,

## 2520:00 - 2540:00

you know, just try to think about like

## 2540:00 - 2570:00

what is that frontier where the model is

## 2570:00 - 2605:00

not very good at today. um because it's

## 2605:00 - 2630:00

going to get good at it and you just

## 2630:00 - 2640:00

have to wait.

## 2640:00 - 2660:00

>> Going back though, but when do you

## 2660:00 - 2685:00

remember when you first got the idea?

## 2685:00 - 2705:00

Can you just talk us through that? Like

## 2705:00 - 2745:00

was it some like a spark or what was

## 2745:00 - 2770:00

even the first version of it in your

## 2770:00 - 2780:00

mind?

## 2780:00 - 2800:00

>> You know, it's funny. It was like it was

## 2800:00 - 2825:00

so accidental that it just kind of

## 2825:00 - 2875:00

evolved into this. Um you know as as

## 2875:00 - 2910:00

anthropic I think for Ant the bet has

## 2910:00 - 2965:00

been coding for a long time and the bet

## 2965:00 - 3020:00

has been the path to save to safe AGI is

## 3020:00 - 3035:00

through coding

## 3035:00 - 3060:00

>> and this is this has kind of always been

## 3060:00 - 3100:00

the idea and the way you get there is

## 3100:00 - 3125:00

you you teach the model how to code then

## 3125:00 - 3145:00

you teach it how to use tools then you

## 3145:00 - 3185:00

teach it how to use computers um and you

## 3185:00 - 3205:00

can kind of see that because the the

## 3205:00 - 3235:00

first team that I joined at Enthropic it

## 3235:00 - 3270:00

was called the anthropic labs team uh

## 3270:00 - 3300:00

and it produced three products it was

## 3300:00 - 3350:00

quadcode MCP and in the desktop app. So

## 3350:00 - 3370:00

you can kind of see how these like weave

## 3370:00 - 3410:00

together. The particular product that we

## 3410:00 - 3450:00

built, you know, like no one no one

## 3450:00 - 3490:00

asked me to build a CLI.

## 3490:00 - 3530:00

Um we kind of knew maybe it was time to

## 3530:00 - 3555:00

build some kind of coding product cuz it

## 3555:00 - 3590:00

seemed like the model was ready, but no

## 3590:00 - 3620:00

one had yet really built the product

## 3620:00 - 3655:00

that harnessed this capability. So like

## 3655:00 - 3685:00

still there's this insane feeling of

## 3685:00 - 3710:00

product overhang. But at the time it was

## 3710:00 - 3745:00

just like even crazier cuz like no one

## 3745:00 - 3775:00

had built this yet. And so I I started

## 3775:00 - 3815:00

like hacking around uh and I was like,

## 3815:00 - 3845:00

"Okay, we build a coding product. What

## 3845:00 - 3870:00

do I have to do first? I have to

## 3870:00 - 3895:00

understand how to use the API because I

## 3895:00 - 3925:00

hadn't used anthropic API at that

## 3925:00 - 3970:00

point." Um and so I I just built like a

## 3970:00 - 4000:00

little terminal app to use the API.

## 4000:00 - 4020:00

That's all that I did. And it was a

## 4020:00 - 4045:00

little chat app because you know like

## 4045:00 - 4075:00

you think about the you know AI

## 4075:00 - 4095:00

applications of the time and you know

## 4095:00 - 4135:00

for non-coders today most what what are

## 4135:00 - 4160:00

most people using is just a chat app. So

## 4160:00 - 4205:00

that's what I built. Uh and you know it

## 4205:00 - 4225:00

was in a terminal. I can ask questions.

## 4225:00 - 4275:00

I give answers. Then I think tool use

## 4275:00 - 4295:00

came out. I just wanted to try out tool

## 4295:00 - 4315:00

use because I I don't really understand

## 4315:00 - 4345:00

what this is. I was like to use this is

## 4345:00 - 4370:00

cool. Is this actually useful? Probably

## 4370:00 - 4395:00

not. Let me just try it.

## 4395:00 - 4425:00

>> You built it in terminal just because it

## 4425:00 - 4445:00

was the easiest way to get something up

## 4445:00 - 4460:00

and running.

## 4460:00 - 4490:00

>> Yes. Cuz I didn't have to build a UI.

## 4490:00 - 4505:00

>> Okay.

## 4505:00 - 4515:00

>> It was just me

## 4515:00 - 4540:00

>> at that point. It was like the IDEs,

## 4540:00 - 4575:00

Cursor, Windsurf

## 4575:00 - 4615:00

taking off. Were you sort of under any

## 4615:00 - 4640:00

pressure or getting lots of suggestions

## 4640:00 - 4665:00

of, hey, like we should build this out

## 4665:00 - 4710:00

as a plugin or as a as a fully featured

## 4710:00 - 4735:00

ID itself? There was no pressure because

## 4735:00 - 4755:00

we didn't even know what we wanted to

## 4755:00 - 4785:00

build. Like the the team was just in

## 4785:00 - 4810:00

explore mode, you know, like we we

## 4810:00 - 4840:00

didn't we know vaguely we wanted to do

## 4840:00 - 4860:00

something in coding, but it wasn't

## 4860:00 - 4895:00

obvious what no one was high confidence

## 4895:00 - 4915:00

enough. That was like my job to figure

## 4915:00 - 4960:00

out. And so I g I gave the model uh the

## 4960:00 - 4985:00

batch tool. That was the first tool that

## 4985:00 - 5010:00

that I gave it just cuz I think that was

## 5010:00 - 5050:00

literally the example in our docs. I

## 5050:00 - 5070:00

just like took the example. It was in

## 5070:00 - 5095:00

Python. I just ported it to TypeScript

## 5095:00 - 5115:00

because that that's how I wrote it. You

## 5115:00 - 5135:00

know, I didn't know like what the model

## 5135:00 - 5155:00

could do with bash. So I asked it to

## 5155:00 - 5180:00

like read a file. It could like cat the

## 5180:00 - 5225:00

file. So like that was cool. And then I

## 5225:00 - 5240:00

was like, "Okay, like what can you

## 5240:00 - 5270:00

actually do?" And and I asked her, "What

## 5270:00 - 5300:00

music am I listening to?" He wrote some

## 5300:00 - 5355:00

like Apple script to script my my Mac

## 5355:00 - 5385:00

and look up the music in my music

## 5385:00 - 5390:00

player.

## 5390:00 - 5410:00

>> Oh my god.

## 5410:00 - 5445:00

>> And this was Sauna 3.5.

## 5445:00 - 5475:00

>> And you know, like I I didn't think the

## 5475:00 - 5510:00

model could do that. And that was my

## 5510:00 - 5550:00

first I think ever fuel the AGI moment

## 5550:00 - 5575:00

>> where I was just like, "Oh my god, the

## 5575:00 - 5620:00

model it just wants to use tools. That's

## 5620:00 - 5635:00

all it wants."

## 5635:00 - 5660:00

>> That's kind of fascinating. I mean it's

## 5660:00 - 5735:00

very kind of contrarian that clocker

## 5735:00 - 5780:00

works so well in such an elegant simple

## 5780:00 - 5815:00

form factor. I mean terminals have been

## 5815:00 - 5850:00

around for a really long time and that

## 5850:00 - 5895:00

seemed to be like a good design

## 5895:00 - 5925:00

constraint that allowed a lot of

## 5925:00 - 5980:00

interesting developer experiences like

## 5980:00 - 6000:00

it doesn't feel like working. It just

## 6000:00 - 6035:00

feels fun as a developer. I don't think

## 6035:00 - 6085:00

about files where everything is and that

## 6085:00 - 6120:00

came by accident almost.

## 6120:00 - 6155:00

>> Yeah, it was an accident. I remember so

## 6155:00 - 6180:00

after the terminal started to take off

## 6180:00 - 6225:00

internally. Um and honestly like after

## 6225:00 - 6250:00

building this thing I think like 2 days

## 6250:00 - 6270:00

after the first prototype I started

## 6270:00 - 6310:00

giving it to my team just for dogfooting

## 6310:00 - 6340:00

cuz you know like you know if you come

## 6340:00 - 6375:00

up with an idea and it seems useful the

## 6375:00 - 6390:00

first thing you want to do is you want

## 6390:00 - 6410:00

to give it to people to see how they use

## 6410:00 - 6445:00

it. And then I came in the next day and

## 6445:00 - 6480:00

then Robert who sits across from me

## 6480:00 - 6515:00

who's another engineer he he just like

## 6515:00 - 6540:00

had quad code on his computer and he was

## 6540:00 - 6575:00

like using it to code. I was like I was

## 6575:00 - 6590:00

like what what are you what are you

## 6590:00 - 6615:00

doing? Like this thing isn't ready. It's

## 6615:00 - 6640:00

just a prototype. But yeah, it it was

## 6640:00 - 6670:00

already useful in that form factor. And

## 6670:00 - 6710:00

I remember when we did our launch review

## 6710:00 - 6745:00

to kind of launch quad code externally,

## 6745:00 - 6785:00

this was in December, November,

## 6785:00 - 6835:00

something like that in 2024. Um Dario

## 6835:00 - 6865:00

asked and he was like, "The us chart

## 6865:00 - 6895:00

internally like the the Dow chart is

## 6895:00 - 6930:00

like vertical. Are you like forcing

## 6930:00 - 6950:00

engineers to use it? Like why are you

## 6950:00 - 6975:00

mandating them?"

## 6975:00 - 7010:00

>> And I was just like, "No, no, we didn't.

## 7010:00 - 7035:00

We I just like posted about it and they

## 7035:00 - 7055:00

they' just been like telling each other

## 7055:00 - 7085:00

about it." Honestly, it was it was just

## 7085:00 - 7115:00

accidental. We we started with the CLI

## 7115:00 - 7135:00

because it was the cheapest thing and it

## 7135:00 - 7155:00

just kind of stayed there for a bit.

## 7155:00 - 7215:00

>> So in that 2024 period, what how were

## 7215:00 - 7245:00

the engineers using it? Were they sort

## 7245:00 - 7275:00

of shipping code with it yet or were

## 7275:00 - 7300:00

they using it in a different way?

## 7300:00 - 7320:00

>> The model is not very good at coding

## 7320:00 - 7360:00

yet. I I was using it personally for

## 7360:00 - 7405:00

automating git. Um I think at this point

## 7405:00 - 7435:00

I I probably forgotten most of my git

## 7435:00 - 7470:00

because cloud code has just been doing

## 7470:00 - 7495:00

it for so long. But yeah, like

## 7495:00 - 7525:00

automating uh bash commands that that

## 7525:00 - 7550:00

was a very early use case and like

## 7550:00 - 7580:00

operating like Kubernetes and kind of

## 7580:00 - 7605:00

things like this. People were using it

## 7605:00 - 7630:00

for coding. So there were some early

## 7630:00 - 7650:00

signs of this. I think the first use

## 7650:00 - 7680:00

case was actually writing unit tests

## 7680:00 - 7700:00

because it's a little bit lower risk and

## 7700:00 - 7745:00

the model was still pretty bad at it

## 7745:00 - 7765:00

>> but people were were were kind of

## 7765:00 - 7785:00

figuring it out and and they were

## 7785:00 - 7815:00

figuring out how to use this thing.

## 7815:00 - 7850:00

>> Um and one thing that we saw is people

## 7850:00 - 7885:00

started writing these markdown files for

## 7885:00 - 7915:00

themselves and then having the model

## 7915:00 - 7950:00

read that markdown file. And this is

## 7950:00 - 7985:00

where QuadMD came from. Probably the

## 7985:00 - 8010:00

single for me biggest principle in

## 8010:00 - 8050:00

product is latent demand. Um and the

## 8050:00 - 8080:00

just every bit of this product is built

## 8080:00 - 8105:00

through latent demand after their

## 8105:00 - 8155:00

initial CLI. Uh and so quadmd is an

## 8155:00 - 8180:00

example of that. There's this other

## 8180:00 - 8210:00

general principle that I think is maybe

## 8210:00 - 8250:00

interesting where you can build for the

## 8250:00 - 8285:00

model and then you can build scaffolding

## 8285:00 - 8310:00

around the model in order to improve

## 8310:00 - 8345:00

performance a little bit and depending

## 8345:00 - 8365:00

on the domain you can improve

## 8365:00 - 8405:00

performance maybe 10 20% something like

## 8405:00 - 8430:00

that and then essentially the gain is

## 8430:00 - 8470:00

wiped out with the next model. So either

## 8470:00 - 8500:00

you can build build the scaffolding and

## 8500:00 - 8525:00

then you know get some performance gain

## 8525:00 - 8560:00

and then rebuild it again or you just

## 8560:00 - 8585:00

wait for the next model and then you

## 8585:00 - 8610:00

kind of get it for free. the quantumd

## 8610:00 - 8630:00

and kind of the scaffolding is an

## 8630:00 - 8665:00

example of that and really I think

## 8665:00 - 8690:00

that's why we stayed in the CLI is

## 8690:00 - 8735:00

because we felt there is no UI we could

## 8735:00 - 8770:00

build that would still be relevant in 6

## 8770:00 - 8800:00

months because the model was improving

## 8800:00 - 8815:00

so quickly

## 8815:00 - 8835:00

>> earlier we were saying like we should

## 8835:00 - 8875:00

compare cloud MDs but you said something

## 8875:00 - 8915:00

very profound which is you know yours is

## 8915:00 - 8950:00

actually very short which is almost like

## 8950:00 - 8975:00

the opposite of what you know people

## 8975:00 - 9015:00

might expect why is that what's in your

## 9015:00 - 9030:00

cloud MD

## 9030:00 - 9065:00

>> okay so I I checked this before we came

## 9065:00 - 9100:00

so my my cloud has two

## 9100:00 - 9160:00

Um, one is, uh, there it's just two

## 9160:00 - 9190:00

lines. So, the first line is whenever

## 9190:00 - 9235:00

you put up a PR, enable automerge. Um,

## 9235:00 - 9260:00

so as soon as someone accepts it, it's

## 9260:00 - 9290:00

merged. That's just so I can like code

## 9290:00 - 9315:00

and I don't have to kind of go back and

## 9315:00 - 9355:00

forth with CR or whatever. And then the

## 9355:00 - 9380:00

second one is whenever I put up a PR,

## 9380:00 - 9410:00

post it in our internal team stamps

## 9410:00 - 9440:00

channel. Uh, just so someone can stamp

## 9440:00 - 9495:00

it and I can get unblocked. Uh, and the

## 9495:00 - 9530:00

idea is every other instruction is in

## 9530:00 - 9555:00

our quadmd that's checked into the

## 9555:00 - 9595:00

codebase and it's something our entire

## 9595:00 - 9625:00

team contributes to multiple times a

## 9625:00 - 9675:00

week. And very often I'll see someone's

## 9675:00 - 9715:00

PR and they make some like mistake

## 9715:00 - 9740:00

that's totally preventable and I'll just

## 9740:00 - 9770:00

literally tag Claude on the PR. I'll

## 9770:00 - 9800:00

just do like add quad, you know, like

## 9800:00 - 9825:00

add this to the quad MD and I'll do

## 9825:00 - 9850:00

this, you know, like many times a week.

## 9850:00 - 9880:00

>> Do you have to like compact the Claude

## 9880:00 - 9910:00

MD? Like I definitely reached a point

## 9910:00 - 9930:00

where I got the message at the top

## 9930:00 - 9970:00

saying your cloud MD is like thousands

## 9970:00 - 10010:00

of tokens now. What do you do when you

## 10010:00 - 10025:00

guys hit that?

## 10025:00 - 10055:00

>> So our quadm is actually pretty short. I

## 10055:00 - 10085:00

think it's like couple thousand tokens

## 10085:00 - 10120:00

maybe something like that. Um if if you

## 10120:00 - 10140:00

hit this my recommendation would be

## 10140:00 - 10170:00

delete your quadmd and just start fresh.

## 10170:00 - 10185:00

>> Interesting.

## 10185:00 - 10210:00

>> I think a lot of people like they try to

## 10210:00 - 10250:00

overengineer this right and and really

## 10250:00 - 10280:00

like the capability changes with every

## 10280:00 - 10320:00

model. And so the thing that you want is

## 10320:00 - 10355:00

do the minimal possible thing in order

## 10355:00 - 10395:00

to get the model on track. And so if you

## 10395:00 - 10425:00

delete your quadd and then you know the

## 10425:00 - 10445:00

model is getting off track, it does the

## 10445:00 - 10465:00

wrong thing. That's when you kind of add

## 10465:00 - 10500:00

back a little bit at a time. And what

## 10500:00 - 10520:00

you're probably going to find is with

## 10520:00 - 10545:00

every model, you have to add less and

## 10545:00 - 10570:00

less. For me, I consider myself a pretty

## 10570:00 - 10610:00

average engineer to be honest. Like I

## 10610:00 - 10645:00

don't use a lot of fancy tools. Like I I

## 10645:00 - 10675:00

don't use like Vim. I use, you know, VS

## 10675:00 - 10705:00

Code because it's simpler. Um I don't

## 10705:00 - 10715:00

really

## 10715:00 - 10735:00

>> Wait, really? I would have assumed that

## 10735:00 - 10755:00

because you built this in the terminal

## 10755:00 - 10785:00

that you were sort of like a dieh hard

## 10785:00 - 10820:00

ter terminal like Vim Vim only person

## 10820:00 - 10865:00

you know screw those VS code people you

## 10865:00 - 10870:00

know

## 10870:00 - 10890:00

>> well we have people like that on the

## 10890:00 - 10915:00

team there's you know like Adam Wolf for

## 10915:00 - 10940:00

example he's he's on the team he's like

## 10940:00 - 10965:00

you will never take Vim for my cold dead

## 10965:00 - 11005:00

hands like yeah so there's definitely a

## 11005:00 - 11025:00

lot of people like that on the team and

## 11025:00 - 11045:00

this is one of the things that I learned

## 11045:00 - 11075:00

early on is every engineer likes to hold

## 11075:00 - 11100:00

their dev tools differently they like to

## 11100:00 - 11120:00

use different tools there's just no one

## 11120:00 - 11145:00

tool that works for everyone but I think

## 11145:00 - 11175:00

also this is one of the things that

## 11175:00 - 11225:00

makes it possible for quad code to be so

## 11225:00 - 11265:00

good because I kind of think about it as

## 11265:00 - 11285:00

what is the product that I would use

## 11285:00 - 11325:00

that makes sense to me and so to use

## 11325:00 - 11345:00

quad code you don't have to understand

## 11345:00 - 11375:00

Vim you don't have to understand TMX you

## 11375:00 - 11405:00

don't have to know how to like SSH you

## 11405:00 - 11420:00

don't have to know all the stuff you

## 11420:00 - 11450:00

just have to open up the tool and it'll

## 11450:00 - 11480:00

guide you it'll it'll do all this stuff

## 11480:00 - 11510:00

>> how do you decide how verbose you want

## 11510:00 - 11540:00

like sort of the terminal to be like

## 11540:00 - 11565:00

sometimes you have to go you know

## 11565:00 - 11610:00

control O and check it out and is it

## 11610:00 - 11645:00

like internal bike shed battles around

## 11645:00 - 11700:00

like longer shorter I mean every user

## 11700:00 - 11735:00

probably has a for an opinion like how

## 11735:00 - 11760:00

do you make those sorts of decisions?

## 11760:00 - 11785:00

>> What What's your opinion? Is it is it

## 11785:00 - 11800:00

too verbose right now?

## 11800:00 - 11835:00

>> Oh, I love the verbosity cuz basically

## 11835:00 - 11870:00

sometimes it just like goes off the deep

## 11870:00 - 11905:00

end and I'm watching and then I can just

## 11905:00 - 11930:00

read very quickly and it's like, "Oh,

## 11930:00 - 11955:00

no, no, it's not that." And then I

## 11955:00 - 11990:00

escape and then just stop it and then it

## 11990:00 - 12030:00

just like stops an entire bug farm like

## 12030:00 - 12060:00

as it's happening. I mean, that's

## 12060:00 - 12085:00

usually when I didn't do plan mode

## 12085:00 - 12095:00

properly.

## 12095:00 - 12115:00

>> This is something that we probably

## 12115:00 - 12160:00

change pretty often. Um, I remember

## 12160:00 - 12185:00

early on, this is maybe six months ago,

## 12185:00 - 12220:00

I tried to get rid of bash output just

## 12220:00 - 12240:00

internally just to like summarize it

## 12240:00 - 12270:00

because I was like these giant long bash

## 12270:00 - 12300:00

commands, I don't actually care. And

## 12300:00 - 12325:00

then I gave it to anthropic employees

## 12325:00 - 12365:00

for a day and everyone just revolted.

## 12365:00 - 12395:00

I want to see my dash because it it

## 12395:00 - 12430:00

actually is quite useful for, you know,

## 12430:00 - 12455:00

like for something like git output,

## 12455:00 - 12485:00

maybe it's not useful, but if you're

## 12485:00 - 12510:00

running, you know, like Kubernetes jobs

## 12510:00 - 12525:00

or something like this, you actually do

## 12525:00 - 12560:00

want to see it. We recently hit the hid

## 12560:00 - 12610:00

the file reads and uh file searches. So

## 12610:00 - 12630:00

you'll notice instead of saying, you

## 12630:00 - 12665:00

know, like read food.md said, you know,

## 12665:00 - 12700:00

like read one file, search searched one

## 12700:00 - 12735:00

pattern. And this is something I think

## 12735:00 - 12755:00

we could not have shipped six months ago

## 12755:00 - 12785:00

because the model just was not ready. It

## 12785:00 - 12805:00

would have, you know, it still read the

## 12805:00 - 12830:00

wrong thing pretty often. As a user, you

## 12830:00 - 12855:00

still had to be there and kind of catch

## 12855:00 - 12890:00

it and debug it. But nowadays, I just

## 12890:00 - 12920:00

noticed it's on the right track almost

## 12920:00 - 12955:00

every time. And because it's using tools

## 12955:00 - 12985:00

so much, it's actually a lot better just

## 12985:00 - 13025:00

to summarize it. Um, but then we shipped

## 13025:00 - 13050:00

it. Uh, we dog fooded it for like a

## 13050:00 - 13075:00

month and then people on GitHub didn't

## 13075:00 - 13110:00

like it. Uh so there was a big issue

## 13110:00 - 13130:00

where people like no like I want to see

## 13130:00 - 13150:00

the details and that was really great

## 13150:00 - 13190:00

feedback. Um and so we added a new

## 13190:00 - 13225:00

verbose mode and so that's just like in

## 13225:00 - 13250:00

slash config you can enable verbose mode

## 13250:00 - 13275:00

and if you want to see all the file

## 13275:00 - 13315:00

outputs you can continue to do that and

## 13315:00 - 13335:00

then I posted on the issue and people

## 13335:00 - 13370:00

still still didn't like it which is

## 13370:00 - 13395:00

again awesome because like my favorite

## 13395:00 - 13415:00

thing in the world is just hearing

## 13415:00 - 13435:00

people's feedback and hearing how they

## 13435:00 - 13470:00

actually want to use it. Um and so we

## 13470:00 - 13490:00

just like iterated more and more and

## 13490:00 - 13515:00

more to get that really good and to make

## 13515:00 - 13535:00

it the thing that people want. I'm

## 13535:00 - 13570:00

amazed like how much I enjoy uh fixing

## 13570:00 - 13620:00

bugs now. And then all you have to do is

## 13620:00 - 13665:00

uh have really good logging and then

## 13665:00 - 13700:00

even just say like hey check out that

## 13700:00 - 13735:00

you know this particular object it

## 13735:00 - 13765:00

messed up in this way and it like

## 13765:00 - 13795:00

searches the log. It figures everything

## 13795:00 - 13825:00

out. It can like go into your you can

## 13825:00 - 13850:00

make a production tunnel and it'll look

## 13850:00 - 13885:00

at your production DB for you. It's like

## 13885:00 - 13920:00

this is insane. Bug fixing is just going

## 13920:00 - 13960:00

to sentry copy markdown. You know pretty

## 13960:00 - 13995:00

soon it's just going to be straight MCP.

## 13995:00 - 14035:00

It's like an autobug fixing like and

## 14035:00 - 14090:00

test making sort of uh what's the new uh

## 14090:00 - 14125:00

term they call it like a making a

## 14125:00 - 14145:00

startup factory. Oh yeah.

## 14145:00 - 14175:00

>> Right. There's like all these concepts

## 14175:00 - 14220:00

now of rather than having to review the

## 14220:00 - 14270:00

code, you know, I'm I'm old school, so I

## 14270:00 - 14300:00

like the verbosity. I like to say, "Oh,

## 14300:00 - 14325:00

well, you're doing this, but I want you

## 14325:00 - 14360:00

to do that." Right? But there's a

## 14360:00 - 14395:00

totally different school of thought now

## 14395:00 - 14435:00

that says like anytime an a real human

## 14435:00 - 14490:00

being has to look at code uh that's bad.

## 14490:00 - 14505:00

>> Yeah. Yeah. Yeah.

## 14505:00 - 14520:00

>> Which is fascinating.

## 14520:00 - 14545:00

>> I think like Dan Chipper talks about

## 14545:00 - 14585:00

this a lot as kind of when whenever you

## 14585:00 - 14605:00

see the model make a mistake try to put

## 14605:00 - 14635:00

in the quadmd try to put it in like

## 14635:00 - 14660:00

skills or something like that so it's

## 14660:00 - 14700:00

reusable. But I I think there's this

## 14700:00 - 14720:00

meta point that I actually struggle with

## 14720:00 - 14765:00

a lot. And I people talk about like

## 14765:00 - 14790:00

agents can do this, agents can do that,

## 14790:00 - 14815:00

but actually what agents can do, it

## 14815:00 - 14860:00

changes with every single model. And so

## 14860:00 - 14880:00

sometimes there's a new person that

## 14880:00 - 14895:00

joins the team and they actually use

## 14895:00 - 14935:00

quad code more than I would have used

## 14935:00 - 14945:00

it.

## 14945:00 - 14975:00

>> And I'm just constantly surprised by

## 14975:00 - 15015:00

this. Like for example, there was a we

## 15015:00 - 15040:00

had like a memory leak and we were

## 15040:00 - 15070:00

trying to debug it. Um and by the way,

## 15070:00 - 15095:00

like Jared Sumar has just been on this

## 15095:00 - 15125:00

crusade killing all the memory leaks and

## 15125:00 - 15155:00

it's just been amazing. But before Jared

## 15155:00 - 15190:00

was on the team, I had to do this and

## 15190:00 - 15210:00

there was this memory leak. I I was

## 15210:00 - 15245:00

trying to debug it. And so I I took a

## 15245:00 - 15270:00

heap dump. I opened it in DevTools. I

## 15270:00 - 15290:00

was looking through the profile. Then I

## 15290:00 - 15310:00

was looking through the code and I I was

## 15310:00 - 15340:00

just trying to figure this out. And then

## 15340:00 - 15385:00

another engineer on the team, Chris, he

## 15385:00 - 15425:00

just like asked Quad Code. He was like,

## 15425:00 - 15445:00

"Hey, I think there's a memory leak. Can

## 15445:00 - 15465:00

you like run this?" And then like try to

## 15465:00 - 15490:00

figure it out. And Quad Code like took

## 15490:00 - 15510:00

the heap dump. It wrote a little tool

## 15510:00 - 15535:00

for itself to like analyze the heap

## 15535:00 - 15575:00

dump. And then it found the leak faster

## 15575:00 - 15630:00

than I did. And this is just something I

## 15630:00 - 15670:00

have to constantly relearn because my

## 15670:00 - 15700:00

brain is still stuck somewhere six

## 15700:00 - 15730:00

months ago at times.

## 15730:00 - 15765:00

>> So what would be some advice for

## 15765:00 - 15830:00

technical founders to really become

## 15830:00 - 15865:00

maximalists at the latest model release?

## 15865:00 - 15905:00

It sounds like people off of fresh off

## 15905:00 - 15935:00

of school or that don't have any

## 15935:00 - 15965:00

assumptions might be better suited than

## 15965:00 - 16005:00

maybe sometimes engineers who have been

## 16005:00 - 16030:00

working at it for a long time. And how

## 16030:00 - 16095:00

do the experts get better? I think for

## 16095:00 - 16125:00

yourself it's kind of beginner mindset

## 16125:00 - 16165:00

and uh I don't know maybe just like

## 16165:00 - 16215:00

humility like I feel like engineers as a

## 16215:00 - 16240:00

discipline we've learned to have very

## 16240:00 - 16275:00

strong opinions and senior engineers are

## 16275:00 - 16305:00

kind of rewarded for this in my old job

## 16305:00 - 16330:00

at a big company when I hired like

## 16330:00 - 16350:00

architects and this kind of a type of

## 16350:00 - 16380:00

engineer you look for people that have a

## 16380:00 - 16400:00

lot of experience and really strong

## 16400:00 - 16435:00

opinions but it actually turns out a lot

## 16435:00 - 16460:00

of this stuff just isn't relevant

## 16460:00 - 16485:00

anymore and a lot of these opinions

## 16485:00 - 16520:00

should change because the model is

## 16520:00 - 16565:00

getting better um so I think actually

## 16565:00 - 16585:00

the biggest skill is people that can

## 16585:00 - 16615:00

think scientifically and can just think

## 16615:00 - 16635:00

from first principles.

## 16635:00 - 16670:00

>> How do you screen for that when you try

## 16670:00 - 16705:00

to hire someone now for for your team?

## 16705:00 - 16730:00

>> I sometimes ask about what's an example

## 16730:00 - 16760:00

of when you're wrong. It's a really good

## 16760:00 - 16780:00

one. You know, some of these like

## 16780:00 - 16805:00

classic behavioral questions like not

## 16805:00 - 16835:00

even coding questions I think are quite

## 16835:00 - 16870:00

useful because you can see if people can

## 16870:00 - 16895:00

recognize their mistake in hindsight, if

## 16895:00 - 16930:00

they can claim credit for the mistake

## 16930:00 - 16970:00

and if they learn something from it. And

## 16970:00 - 16995:00

I think a lot of these like very senior

## 16995:00 - 17020:00

people especially there there are some

## 17020:00 - 17045:00

founder types like this but I think

## 17045:00 - 17065:00

founders in particular are actually

## 17065:00 - 17110:00

quite good at it. Um but other people

## 17110:00 - 17150:00

sometimes will never really take uh

## 17150:00 - 17170:00

they'll never take the blame for a

## 17170:00 - 17210:00

mistake. But I don't know like for me

## 17210:00 - 17235:00

personally I'm wrong probably half the

## 17235:00 - 17280:00

time. Like half my ideas are bad and you

## 17280:00 - 17315:00

just have to try stuff and you know you

## 17315:00 - 17340:00

try a thing you give it to users you

## 17340:00 - 17370:00

talk to users you learn and then

## 17370:00 - 17390:00

eventually you might end up at a good

## 17390:00 - 17425:00

idea. Sometimes you don't. And this is

## 17425:00 - 17465:00

the skill that I think in in the past

## 17465:00 - 17505:00

was very important for founders, but now

## 17505:00 - 17530:00

I think it's very important for every

## 17530:00 - 17540:00

engineer.

## 17540:00 - 17570:00

>> Do you think um you would ever hire

## 17570:00 - 17615:00

someone based on the uh claude code

## 17615:00 - 17660:00

transcript of uh them working with the

## 17660:00 - 17700:00

agent cuz we're actively doing that

## 17700:00 - 17745:00

right now. We just added uh just as a

## 17745:00 - 17785:00

test like you can upload a transcript of

## 17785:00 - 17830:00

you coding a feature with cloud code or

## 17830:00 - 17865:00

codeex or whatever it is. Personally, I

## 17865:00 - 17890:00

think that like it's going to work. I

## 17890:00 - 17930:00

mean, you can figure out uh how someone

## 17930:00 - 17965:00

thinks, like whether they're looking at

## 17965:00 - 18000:00

the logs or not, like can they correct

## 18000:00 - 18040:00

the agent if it goes off off the rails?

## 18040:00 - 18075:00

Like, does do they use plan mode? You

## 18075:00 - 18110:00

know, when they use plan mode, do they

## 18110:00 - 18140:00

make sure that there are tests or you

## 18140:00 - 18160:00

know, all of these different things

## 18160:00 - 18170:00

that,

## 18170:00 - 18190:00

>> you know, do they think about systems?

## 18190:00 - 18220:00

Do they even understand systems? Like,

## 18220:00 - 18240:00

there's just so much that's sort of

## 18240:00 - 18280:00

embedded in that that I imagine. I just

## 18280:00 - 18320:00

want like a spider uh a spiderweb graph,

## 18320:00 - 18350:00

you know, like in those video games like

## 18350:00 - 18380:00

NBA 2K. It's like, oh, this person's

## 18380:00 - 18410:00

really good at shooting or defense. It's

## 18410:00 - 18445:00

like you could imagine a spiderweb graph

## 18445:00 - 18485:00

of like, you know, someone's claude code

## 18485:00 - 18505:00

skill level.

## 18505:00 - 18525:00

>> Yeah. What would what would the skills

## 18525:00 - 18545:00

be? What would be those?

## 18545:00 - 18580:00

>> I mean, I think it's like systems

## 18580:00 - 18620:00

testing must be like user behavior. I

## 18620:00 - 18660:00

mean, there's got to be a design part

## 18660:00 - 18690:00

like product sense maybe also just like

## 18690:00 - 18725:00

automating stuff. Mhm. My favorite thing

## 18725:00 - 18775:00

in CloudMD uh for me is I have a thing

## 18775:00 - 18820:00

that says for every plan decide whether

## 18820:00 - 18855:00

it's overengineered, underengineered, or

## 18855:00 - 18885:00

perfectly engineered and why.

## 18885:00 - 18905:00

>> I think this is something that we're

## 18905:00 - 18930:00

trying to figure out, too, cuz I I think

## 18930:00 - 18960:00

uh when I look at engineers on the team

## 18960:00 - 18990:00

that I think are the most effective,

## 18990:00 - 19010:00

there's essentially two, it's very

## 19010:00 - 19050:00

biodal. Um there's one side where it's

## 19050:00 - 19085:00

extreme specialists. Um and so like I

## 19085:00 - 19110:00

named Jared before, like he's a really

## 19110:00 - 19130:00

good example of this and kind of the bun

## 19130:00 - 19160:00

team is a really good example. Just

## 19160:00 - 19190:00

hyper specialist. They understand dev

## 19190:00 - 19220:00

tools better than anyone else. They

## 19220:00 - 19245:00

understand JavaScript runtime systems

## 19245:00 - 19275:00

better than anyone else. And then

## 19275:00 - 19300:00

there's the flip side of kind of hyper

## 19300:00 - 19320:00

generalists and that's kind of the rest

## 19320:00 - 19350:00

of the team. And a lot of people they

## 19350:00 - 19390:00

span like product and info or product

## 19390:00 - 19430:00

and design um or you know like product

## 19430:00 - 19460:00

and user research, product and business.

## 19460:00 - 19500:00

I really like to see people that just do

## 19500:00 - 19540:00

weird stuff. I think that's one of these

## 19540:00 - 19560:00

things that was kind of a warning sign

## 19560:00 - 19590:00

in the past because it's like can these

## 19590:00 - 19625:00

people actually build something useful?

## 19625:00 - 19660:00

>> Um that's the limits test. Yeah, that's

## 19660:00 - 19700:00

what must but but nowadays like for

## 19700:00 - 19730:00

example an engineer on the team Daisy,

## 19730:00 - 19760:00

she was on a different team and then she

## 19760:00 - 19795:00

transferred onto our team and the reason

## 19795:00 - 19850:00

that I wanted her to transfer is she put

## 19850:00 - 19895:00

up a PR for Claude Code like a couple

## 19895:00 - 19930:00

weeks after she joined or something and

## 19930:00 - 19960:00

the PR was to add a new feature to

## 19960:00 - 19990:00

Claude Code and then instead of just

## 19990:00 - 20015:00

adding the feature what she did is first

## 20015:00 - 20050:00

she put up a PR to give Claude code a

## 20050:00 - 20090:00

tool so that it can test an arbitrary

## 20090:00 - 20125:00

tool and verify that that works. And

## 20125:00 - 20160:00

then she put up that PR and then she had

## 20160:00 - 20190:00

Quad write its own tool instead of

## 20190:00 - 20220:00

herself implementing it. And I think

## 20220:00 - 20240:00

it's this kind of out of the box

## 20240:00 - 20265:00

thinking that is is just so interesting

## 20265:00 - 20295:00

because not a lot of people get it yet.

## 20295:00 - 20320:00

You know, like we use the Quad agents

## 20320:00 - 20355:00

SDK to automate pretty much every part

## 20355:00 - 20385:00

of development. It automates code

## 20385:00 - 20430:00

review, security review. Uh it labels

## 20430:00 - 20460:00

all of our issues. It shephards things

## 20460:00 - 20485:00

to production. It does pretty much

## 20485:00 - 20515:00

everything for us. But I think

## 20515:00 - 20545:00

externally I'm seeing a lot of people

## 20545:00 - 20570:00

start to figure this out, but it's

## 20570:00 - 20595:00

actually taken a while to figure out how

## 20595:00 - 20630:00

do you use LMS in this way? How do you

## 20630:00 - 20665:00

use this new kind of automation? So it's

## 20665:00 - 20680:00

kind of a new skill.

## 20680:00 - 20710:00

>> I guess one of the uh funnier things

## 20710:00 - 20735:00

that I've been having office hours with

## 20735:00 - 20775:00

various founders about is um you have

## 20775:00 - 20805:00

like sort of the visionary founder who

## 20805:00 - 20840:00

has like the idea they've like built

## 20840:00 - 20885:00

this like crystal palace of the product

## 20885:00 - 20915:00

that they want to build. they've totally

## 20915:00 - 20950:00

loaded in their brain, you know, who the

## 20950:00 - 20980:00

user is and what they feel and what

## 20980:00 - 21020:00

they're motivated by and then they're

## 21020:00 - 21045:00

sitting in claude code and they can do

## 21045:00 - 21100:00

like, you know, 50x work and then but

## 21100:00 - 21130:00

they have engineers who work for them

## 21130:00 - 21160:00

who like don't have the, you know,

## 21160:00 - 21190:00

crystal memory palace of like the

## 21190:00 - 21220:00

platonic ideal of the product that the

## 21220:00 - 21255:00

pro founder has and they can only do

## 21255:00 - 21295:00

like 5x work. Are you hearing stories

## 21295:00 - 21330:00

like that? there's usually a person

## 21330:00 - 21385:00

who's like the core like designer of a

## 21385:00 - 21430:00

thing and they're just like, you know,

## 21430:00 - 21465:00

trying to blast it out of their brain.

## 21465:00 - 21500:00

What's the nature of like teams like

## 21500:00 - 21525:00

that? You know, it seems like that's

## 21525:00 - 21555:00

almost a stable configuration. Like

## 21555:00 - 21590:00

you're going to have the visionary who

## 21590:00 - 21640:00

like now is unleashed, but you know,

## 21640:00 - 21665:00

maybe going back to the top of it, like

## 21665:00 - 21690:00

I'm experiencing this right now. I was

## 21690:00 - 21740:00

like, "Oh, well, I'm only a solo person

## 21740:00 - 21775:00

and you know, I need to eat and sleep

## 21775:00 - 21820:00

and I have, you know, a whole job. It's

## 21820:00 - 21845:00

like, how am I going to do this?" You

## 21845:00 - 21850:00

know,

## 21850:00 - 21870:00

>> you know, like we just launched quad

## 21870:00 - 21900:00

teams and, you know, this is a way to do

## 21900:00 - 21925:00

it, but you can also just build your own

## 21925:00 - 21950:00

way to do it. It's pretty easy.

## 21950:00 - 21985:00

>> What's the vision for cloud teams?

## 21985:00 - 22020:00

>> Just collaboration. It's like there's

## 22020:00 - 22040:00

this whole new field of like agent top

## 22040:00 - 22065:00

apologies that people are exploring.

## 22065:00 - 22080:00

Like what are the ways that you can

## 22080:00 - 22115:00

configure agents? There's this one sub

## 22115:00 - 22145:00

idea which is uncorrelated context

## 22145:00 - 22170:00

windows. And the idea is just multiple

## 22170:00 - 22200:00

agents, they have fresh context windows

## 22200:00 - 22225:00

that aren't essentially polluted with

## 22225:00 - 22250:00

each other's context or their own

## 22250:00 - 22285:00

previous context. And if you throw more

## 22285:00 - 22305:00

context at a problem, that's like a form

## 22305:00 - 22350:00

of test time compute. Um, and so you

## 22350:00 - 22380:00

just get more capability that way. And

## 22380:00 - 22405:00

then if you have the right topology on

## 22405:00 - 22425:00

top of it, so the agents can communicate

## 22425:00 - 22450:00

in the right way, they're laid out in

## 22450:00 - 22485:00

the right way, then they can just build

## 22485:00 - 22525:00

bigger stuff. And so Teams is kind of

## 22525:00 - 22550:00

like one idea. There's a few more that

## 22550:00 - 22590:00

are coming pretty soon. Um, and the idea

## 22590:00 - 22630:00

is just maybe it can build a little bit

## 22630:00 - 22665:00

more. I think the first kind of big

## 22665:00 - 22695:00

example where it worked is our plugins

## 22695:00 - 22730:00

feature was entirely built by a swarm

## 22730:00 - 22765:00

over over a weekend. It just ran for

## 22765:00 - 22795:00

like a few days. There wasn't really

## 22795:00 - 22830:00

human intervention. And plugins is

## 22830:00 - 22860:00

pretty much in the form that it was when

## 22860:00 - 22875:00

when it came out.

## 22875:00 - 22905:00

>> How did you set that up? Like did you

## 22905:00 - 22940:00

spec out sort of the outcome that you

## 22940:00 - 22985:00

were hoping for and then let it sort of

## 22985:00 - 23025:00

figure out the details and then like let

## 23025:00 - 23040:00

it run?

## 23040:00 - 23075:00

>> Yeah. an engineer on the team just gave

## 23075:00 - 23140:00

uh gave Quad a spec and um told Quad to

## 23140:00 - 23180:00

use a Asauna board and then Quad just

## 23180:00 - 23220:00

put up a bunch of tickets on a sauna and

## 23220:00 - 23240:00

then spawned a bunch of agents and the

## 23240:00 - 23270:00

agent started picking up tasks. The main

## 23270:00 - 23300:00

quad just gave it instructions and they

## 23300:00 - 23315:00

all just figured it out

## 23315:00 - 23355:00

>> like independent um agents that didn't

## 23355:00 - 23385:00

have the context of the bigger spec.

## 23385:00 - 23390:00

Right.

## 23390:00 - 23420:00

>> Right. If you if you think about the way

## 23420:00 - 23455:00

that uh you know like how our agents

## 23455:00 - 23490:00

actually started nowadays and you know I

## 23490:00 - 23510:00

haven't pulled the data on this but I

## 23510:00 - 23530:00

would bet the majority of agents are

## 23530:00 - 23575:00

actually prompted by quad today in the

## 23575:00 - 23615:00

form of uh sub agents cuz like a sub

## 23615:00 - 23645:00

agent is just like a recursive quad code

## 23645:00 - 23670:00

that's all it is in the code and it's

## 23670:00 - 23720:00

just prompted by we call her mama quad

## 23720:00 - 23750:00

>> and that that's all it is and I think

## 23750:00 - 23770:00

probably if you look at most agents

## 23770:00 - 23790:00

they're launched in this way

## 23790:00 - 23820:00

>> my claude insights just told me to do

## 23820:00 - 23860:00

this more for debugging so that I get

## 23860:00 - 23890:00

like I spend a lot of time on debugging

## 23890:00 - 23930:00

And it would just be better to have like

## 23930:00 - 23965:00

multiple sub agents spin up and like

## 23965:00 - 23995:00

debug something in parallel. And so then

## 23995:00 - 24025:00

I just like added that to my claude MD

## 24025:00 - 24045:00

to just be like, hey, like next time you

## 24045:00 - 24080:00

try and fix a bug like have one agent

## 24080:00 - 24100:00

that like looks in the log, like one

## 24100:00 - 24130:00

that looks in the code path. That just

## 24130:00 - 24150:00

seems sort of inevitable.

## 24150:00 - 24195:00

>> For weird scary bugs, I try to uh fix

## 24195:00 - 24225:00

bugs in plan mode and then it seems to

## 24225:00 - 24260:00

use the agents to sort of search

## 24260:00 - 24290:00

everything. Whereas like when you're

## 24290:00 - 24320:00

just trying to do it in line, it's like,

## 24320:00 - 24350:00

okay, I'm going to do like this one task

## 24350:00 - 24385:00

instead of search wide. This is

## 24385:00 - 24415:00

something I do all the time too. I I

## 24415:00 - 24445:00

just say if the if the test seems kind

## 24445:00 - 24465:00

of hard, this kind of research test,

## 24465:00 - 24495:00

I'll calibrate the number of sub aents I

## 24495:00 - 24525:00

ask it to use based on the difficulty of

## 24525:00 - 24535:00

the task.

## 24535:00 - 24560:00

>> So if it's like really hard, I'll say

## 24560:00 - 24595:00

like use three or maybe five or even 10

## 24595:00 - 24630:00

sub aents, research in parallel and then

## 24630:00 - 24650:00

see what they come up with.

## 24650:00 - 24680:00

>> I'm curious. So then why don't you put

## 24680:00 - 24710:00

that in your clawed MD file?

## 24710:00 - 24740:00

>> It's kind of case by case, you know,

## 24740:00 - 24785:00

like quadm like what is it? It's just a

## 24785:00 - 24810:00

it's a shortcut. Like if you find

## 24810:00 - 24830:00

yourself repeating the same thing over

## 24830:00 - 24870:00

and over, you put in the quad MD. But

## 24870:00 - 24890:00

otherwise, you don't have to put

## 24890:00 - 24905:00

everything there. You can just prompt

## 24905:00 - 24915:00

quad.

## 24915:00 - 24935:00

>> Are you also in the back of your mind

## 24935:00 - 24960:00

thinking that maybe like in six months,

## 24960:00 - 24995:00

you won't need to prompt that

## 24995:00 - 25025:00

explicitly? Like the model will just be

## 25025:00 - 25050:00

good enough to figure out on its own.

## 25050:00 - 25085:00

>> Maybe in a month.

## 25085:00 - 25120:00

>> No more need for plan mode in a month.

## 25120:00 - 25130:00

>> Oh my god.

## 25130:00 - 25155:00

>> I think plan mode probably has a limited

## 25155:00 - 25170:00

lifespan.

## 25170:00 - 25185:00

>> Interesting.

## 25185:00 - 25205:00

>> That's some alpha for everyone here.

## 25205:00 - 25230:00

What would the world look like without

## 25230:00 - 25275:00

plan mode? Do you just describe it at

## 25275:00 - 25305:00

the prompt level and it would just do

## 25305:00 - 25340:00

it? One shot it? Yeah, we've uh we've

## 25340:00 - 25355:00

started experimenting with this because

## 25355:00 - 25390:00

quad code can now enter plan mode by

## 25390:00 - 25420:00

itself. I don't know if you've you guys

## 25420:00 - 25430:00

have seen that.

## 25430:00 - 25445:00

>> Yeah.

## 25445:00 - 25470:00

>> So, we're trying to kind of get this

## 25470:00 - 25505:00

experience really good. So, it would

## 25505:00 - 25535:00

enter plan mode the same point where a

## 25535:00 - 25565:00

human would have wanted to enter it. So,

## 25565:00 - 25585:00

I think it's like I think it's something

## 25585:00 - 25615:00

like this, but actually plan mode

## 25615:00 - 25645:00

there's no there's no big secret to it.

## 25645:00 - 25685:00

All it does is it adds one sentence to

## 25685:00 - 25705:00

the prompt that's like please don't

## 25705:00 - 25725:00

code.

## 25725:00 - 25745:00

>> That's all it is. You can you can

## 25745:00 - 25755:00

actually just say that.

## 25755:00 - 25785:00

>> Yeah. So it sounds like a lot of the

## 25785:00 - 25810:00

feature development for clock code is

## 25810:00 - 25855:00

very much a what we talk about a YC talk

## 25855:00 - 25875:00

to your users

## 25875:00 - 25910:00

>> and then you come and implemented it. It

## 25910:00 - 25930:00

wasn't the other way that you had this

## 25930:00 - 25960:00

master plan and then implemented all the

## 25960:00 - 25970:00

features.

## 25970:00 - 25985:00

>> Yeah. Yeah. I mean that that's all it

## 25985:00 - 26020:00

was like plan mode was we saw users that

## 26020:00 - 26050:00

that were like hey quad come up with an

## 26050:00 - 26085:00

idea plan this out but don't write any

## 26085:00 - 26110:00

code yet. And there was kind of various

## 26110:00 - 26135:00

versions of this. Sometimes it was just

## 26135:00 - 26160:00

talking through an idea. Sometimes it

## 26160:00 - 26190:00

was these very sophisticated specs that

## 26190:00 - 26220:00

that they were asking Claude to write,

## 26220:00 - 26250:00

but the common dimension was do a thing

## 26250:00 - 26295:00

without coding yet. And so literally

## 26295:00 - 26320:00

like this was like Sunday night at 10

## 26320:00 - 26350:00

p.m. I was I was just like looking at

## 26350:00 - 26370:00

GitHub issues and kind of seeing what

## 26370:00 - 26400:00

people were talking about and looking at

## 26400:00 - 26435:00

our internal Slack feedback channel and

## 26435:00 - 26460:00

I just wrote this thing in like 30

## 26460:00 - 26490:00

minutes and then uh shipped it that

## 26490:00 - 26515:00

night. It went out Monday morning. That

## 26515:00 - 26540:00

was plan mode. So do you mean that there

## 26540:00 - 26575:00

will be no need for plan mode to in the

## 26575:00 - 26605:00

sense of I'm worried that the model's

## 26605:00 - 26635:00

going to do like it's going to do like

## 26635:00 - 26660:00

the wrong thing or head off in the wrong

## 26660:00 - 26695:00

direction but there will still be a need

## 26695:00 - 26730:00

for that. You need to think through the

## 26730:00 - 26755:00

idea and figure out exactly what it is

## 26755:00 - 26780:00

that you want and you have to do that

## 26780:00 - 26790:00

somewhere.

## 26790:00 - 26815:00

>> I kind of think about it in terms of

## 26815:00 - 26840:00

like kind of increasing model

## 26840:00 - 26885:00

capabilities. So maybe 6 months ago a

## 26885:00 - 26930:00

plan was insufficient. So you get Claude

## 26930:00 - 26960:00

to make a plan. Let's say even with plan

## 26960:00 - 26975:00

mode you still have to kind of sit there

## 26975:00 - 27000:00

and babysit cuz it can go off track.

## 27000:00 - 27035:00

Nowadays what I do is probably 80% of my

## 27035:00 - 27060:00

sessions I say I say plan mode has a

## 27060:00 - 27090:00

limited lifespan but I I'm a heavy plan

## 27090:00 - 27145:00

mode user. Um I probably 80% of my

## 27145:00 - 27190:00

sessions I start in plan mode and claude

## 27190:00 - 27220:00

will you know it'll start it'll start

## 27220:00 - 27245:00

making a plan. I'll move on to my second

## 27245:00 - 27275:00

terminal tab and then I'll have it make

## 27275:00 - 27300:00

another plan and then when I run out of

## 27300:00 - 27335:00

tabs I open the desktop app and then I

## 27335:00 - 27355:00

go to the code tab and then I just start

## 27355:00 - 27380:00

a bunch of tabs there and they all start

## 27380:00 - 27415:00

in plan mode probably know like 80% of

## 27415:00 - 27445:00

the time. Once the plan is good, and

## 27445:00 - 27465:00

sometimes it takes a little back and

## 27465:00 - 27500:00

forth, they just get clawed to execute.

## 27500:00 - 27550:00

And nowadays, what I find with Opus 4.5,

## 27550:00 - 27585:00

I think it started with 4.6 it got

## 27585:00 - 27625:00

really good. Once the plan is good, it

## 27625:00 - 27650:00

just stays on track and it'll just do

## 27650:00 - 27680:00

the thing exactly right almost every

## 27680:00 - 27710:00

time. And so, you know, before you had

## 27710:00 - 27740:00

to babysit after the plan and before the

## 27740:00 - 27780:00

plan, now it's just before the plan. So,

## 27780:00 - 27810:00

maybe the next thing is you just won't

## 27810:00 - 27830:00

have to babysit. You can just kind of

## 27830:00 - 27855:00

give a prompt and Quad will figure it

## 27855:00 - 27860:00

out.

## 27860:00 - 27885:00

>> The next step is Claude just speaks to

## 27885:00 - 27935:00

your users directly.

## 27935:00 - 27970:00

Yeah, it just bypasses you entirely.

## 27970:00 - 27990:00

>> It's funny. This is actually the current

## 27990:00 - 28015:00

stuff for us. Our quads actually like

## 28015:00 - 28040:00

they talk to each other. They talk to

## 28040:00 - 28080:00

our users on Slack, at least internally

## 28080:00 - 28120:00

pretty often. Um, my quad will like

## 28120:00 - 28135:00

tweet once in a while.

## 28135:00 - 28145:00

>> No way.

## 28145:00 - 28180:00

>> Um, but I actually like delete it. It's

## 28180:00 - 28215:00

just like it's a little like cheesy.

## 28215:00 - 28235:00

Like I don't love the tone.

## 28235:00 - 28265:00

>> What does it want to tweet about?

## 28265:00 - 28295:00

>> Sometimes it'll just like respond to

## 28295:00 - 28325:00

someone cuz I always have like co-work

## 28325:00 - 28345:00

in the background and it's like it's the

## 28345:00 - 28370:00

co-work that really loves to do that

## 28370:00 - 28395:00

because it likes using a browser.

## 28395:00 - 28420:00

>> That's funny. A a really common pattern

## 28420:00 - 28450:00

is I ask Quad to build something. It'll

## 28450:00 - 28490:00

look in the codebase. Uh it'll see some

## 28490:00 - 28510:00

engineer touch something in the git

## 28510:00 - 28540:00

flame and then it'll message that

## 28540:00 - 28575:00

engineer on Slack. Um just like asking a

## 28575:00 - 28600:00

clarifying question and then once it

## 28600:00 - 28625:00

gets answer back, it'll keep going.

## 28625:00 - 28675:00

>> What are some tips for founders now on

## 28675:00 - 28710:00

how to build for the future? Sounds like

## 28710:00 - 28740:00

everything is really changing. What are

## 28740:00 - 28780:00

like some principles that will stay on

## 28780:00 - 28800:00

and what will change?

## 28800:00 - 28825:00

>> So I think some of these are pretty are

## 28825:00 - 28855:00

pretty basic, but I think they're even

## 28855:00 - 28880:00

more important now than they were

## 28880:00 - 28915:00

before. Um, so one example is latent

## 28915:00 - 28940:00

demand. Like I mentioned it a thousand

## 28940:00 - 28975:00

times for me. It's just like the single

## 28975:00 - 29010:00

biggest idea in product. It's a it's a

## 29010:00 - 29050:00

thing that no one understands. It's a

## 29050:00 - 29080:00

thing I certainly did not understand my

## 29080:00 - 29115:00

first few startups. And and the idea is

## 29115:00 - 29135:00

like people will only do a thing that

## 29135:00 - 29165:00

they already do. You can't get people to

## 29165:00 - 29195:00

do a new thing. If people are trying to

## 29195:00 - 29220:00

do a thing and you make it easier,

## 29220:00 - 29250:00

that's a good idea. But if if people are

## 29250:00 - 29270:00

doing a thing and you try to make them

## 29270:00 - 29290:00

do a different thing, they're not going

## 29290:00 - 29320:00

to do that. And so you just have to make

## 29320:00 - 29335:00

the thing that they're trying to do

## 29335:00 - 29365:00

easier. And I think quad is going to get

## 29365:00 - 29390:00

increasingly good at kind of figuring

## 29390:00 - 29425:00

out these kind of product ideas for you

## 29425:00 - 29445:00

just because it can look at feedback, it

## 29445:00 - 29470:00

can look at debug logs, it can kind of

## 29470:00 - 29475:00

figure this out.

## 29475:00 - 29500:00

>> That's what you mean by plan mode was

## 29500:00 - 29540:00

latent demand that people were already

## 29540:00 - 29570:00

like I don't know had their clawed chat

## 29570:00 - 29600:00

window open in a browser and were like

## 29600:00 - 29630:00

talking to it to figure out like the

## 29630:00 - 29700:00

spec and and what it should do. And now

## 29700:00 - 29725:00

that like pi mode just became that you

## 29725:00 - 29745:00

just do it in claw code.

## 29745:00 - 29765:00

>> Yeah. Yeah, that's it. Some sometimes

## 29765:00 - 29785:00

what I'll do is I'll just walk around

## 29785:00 - 29815:00

the office on on our floor and I'll just

## 29815:00 - 29865:00

kind of stand behind people like I I'll

## 29865:00 - 29900:00

say like hi so it's not and then um I'll

## 29900:00 - 29925:00

I'll just see kind of like how they're

## 29925:00 - 29955:00

using quad code. Um and this is also

## 29955:00 - 29985:00

just something I saw a lot um but it

## 29985:00 - 30010:00

also came up in GitHub issues like

## 30010:00 - 30030:00

people were talking about it. It seems

## 30030:00 - 30070:00

like so you're surprised how far the

## 30070:00 - 30110:00

terminal has gone and how far it's been

## 30110:00 - 30140:00

pushed like how far do you think it has

## 30140:00 - 30190:00

left to go just given with this world of

## 30190:00 - 30230:00

swore multiple agents like do you think

## 30230:00 - 30275:00

there's going to be a new a need for a

## 30275:00 - 30295:00

different UI on top of it?

## 30295:00 - 30315:00

>> It's funny if you asked me this a year

## 30315:00 - 30335:00

ago I would have said the terminal has

## 30335:00 - 30360:00

like a threemonth lifespan and then

## 30360:00 - 30375:00

we're going to move on to the next

## 30375:00 - 30405:00

thing. Uh and you can see us

## 30405:00 - 30430:00

experimenting with this right because

## 30430:00 - 30460:00

quad code started in a terminal but now

## 30460:00 - 30490:00

it's in you know it's on web you can

## 30490:00 - 30535:00

like quadcode it's in the desktop app

## 30535:00 - 30550:00

you know we've had that for you know

## 30550:00 - 30575:00

like three months or six months or

## 30575:00 - 30615:00

something just in the code tab um it's

## 30615:00 - 30645:00

in the iOS and Android apps just like in

## 30645:00 - 30680:00

the code tab it's in slack it's in

## 30680:00 - 30715:00

GitHub there's VS Code extensions

## 30715:00 - 30750:00

there's Jet Brains extensions so we're

## 30750:00 - 30780:00

just like we're always experimenting

## 30780:00 - 30810:00

with different form factors for this

## 30810:00 - 30835:00

thing to figure out what's the next

## 30835:00 - 30885:00

thing I've been wrong so far about the

## 30885:00 - 30910:00

of the CLI. So, I'm probably not the

## 30910:00 - 30940:00

person to forecast that.

## 30940:00 - 30975:00

>> What about like your advice to DevTool

## 30975:00 - 31000:00

founders? Like, someone's building a

## 31000:00 - 31040:00

DevTool company today. Should they just

## 31040:00 - 31085:00

like be building for engineers and

## 31085:00 - 31110:00

humans or should they be thinking more

## 31110:00 - 31145:00

about like what Claude going to think

## 31145:00 - 31180:00

and want and build for sort of like the

## 31180:00 - 31190:00

agent?

## 31190:00 - 31225:00

>> The way I would frame it is think about

## 31225:00 - 31265:00

the thing that the model wants to do and

## 31265:00 - 31315:00

figure out how do you make that easier.

## 31315:00 - 31345:00

And that's something that we saw, you

## 31345:00 - 31365:00

know, like when I first started hacking

## 31365:00 - 31390:00

on quad code, I I realized like this

## 31390:00 - 31420:00

thing just wants to use tools. It just

## 31420:00 - 31460:00

wants to interact with the world. And

## 31460:00 - 31485:00

how how do you how do you enable that?

## 31485:00 - 31515:00

Well, the way you don't do it is you put

## 31515:00 - 31550:00

it in a box and you're like, here's the

## 31550:00 - 31575:00

API, here's how you interact with me,

## 31575:00 - 31600:00

and here's how you interact with the

## 31600:00 - 31625:00

world. The way you do it is you see what

## 31625:00 - 31650:00

tools it wants to use. You see what it's

## 31650:00 - 31680:00

trying to do, and you enable that the

## 31680:00 - 31720:00

same way that you do for your users. And

## 31720:00 - 31745:00

so, like for if you're building a dev

## 31745:00 - 31760:00

tool startup, I would think about like

## 31760:00 - 31780:00

what is the problem you want to solve

## 31780:00 - 31820:00

for the user? And then when you use when

## 31820:00 - 31840:00

you apply the model to solving this

## 31840:00 - 31860:00

problem, what is the thing the model

## 31860:00 - 31875:00

wants to do?

## 31875:00 - 31900:00

>> And then what is the technical and

## 31900:00 - 31920:00

product solution that serves the weight

## 31920:00 - 31965:00

and demand of both? YC's next batch is

## 31965:00 - 32005:00

now taking applications. Got a startup

## 32005:00 - 32065:00

in you? Apply at y combinator.com/apply.

## 32065:00 - 32105:00

It's never too early and filling out the

## 32105:00 - 32155:00

app will level up your idea. Okay, back

## 32155:00 - 32200:00

to the video. Back in the day, more than

## 32200:00 - 32250:00

10 years ago, you were a very heav heavy

## 32250:00 - 32285:00

user and you wrote a book about

## 32285:00 - 32335:00

TypeScript, right? Before Typescript was

## 32335:00 - 32380:00

cool. This is when everyone was a deep

## 32380:00 - 32410:00

in JavaScript. This is back in early

## 32410:00 - 32430:00

2010s, right?

## 32430:00 - 32450:00

>> Yeah, something like that.

## 32450:00 - 32485:00

>> Before Typescript was a thing because

## 32485:00 - 32540:00

back then is a very weird language. It's

## 32540:00 - 32575:00

not supposed to do a lot of things with

## 32575:00 - 32625:00

being typed in JavaScript and now it's

## 32625:00 - 32655:00

the right thing and it feels like clot

## 32655:00 - 32685:00

code in the terminal has a lot of

## 32685:00 - 32725:00

parallels with TypeScript at the

## 32725:00 - 32735:00

beginning.

## 32735:00 - 32785:00

>> TypeScript makes a lot of really weird

## 32785:00 - 32825:00

language decisions. So if you look at

## 32825:00 - 32855:00

the type system pretty much anything can

## 32855:00 - 32895:00

be a literal type for example and this

## 32895:00 - 32930:00

is like this is super weird cuz like

## 32930:00 - 32960:00

even like like Haskell doesn't even do

## 32960:00 - 33005:00

this. It's just like it's too extreme or

## 33005:00 - 33040:00

it has like conditional types which I

## 33040:00 - 33080:00

don't think any language thought of at

## 33080:00 - 33085:00

all.

## 33085:00 - 33110:00

>> It was like very strongly typed.

## 33110:00 - 33140:00

>> Yeah, it was very strongly and and the

## 33140:00 - 33165:00

idea was like when you know like when

## 33165:00 - 33205:00

Joe Pamer and Anders and the early team

## 33205:00 - 33235:00

was like building this thing, the way

## 33235:00 - 33270:00

they built it is we okay, we have these

## 33270:00 - 33295:00

teams with these big untyped JavaScript

## 33295:00 - 33325:00

code bases. We have to get types in

## 33325:00 - 33345:00

there, but we're not going to get

## 33345:00 - 33370:00

engineers to change that the way that

## 33370:00 - 33395:00

they code. You're not going to get

## 33395:00 - 33415:00

JavaScript people to have like, you

## 33415:00 - 33450:00

know, 15 layers of class inheritance

## 33450:00 - 33480:00

like you would a Java programmer, right?

## 33480:00 - 33495:00

They're going to write code the way

## 33495:00 - 33505:00

they're going to write it. They're

## 33505:00 - 33525:00

they're going to use reflection and

## 33525:00 - 33550:00

they're going to use mutation and

## 33550:00 - 33570:00

they're going to use all these features

## 33570:00 - 33595:00

that traditionally are very very

## 33595:00 - 33610:00

difficult to type.

## 33610:00 - 33645:00

>> They're a very unsafe type to any strong

## 33645:00 - 33665:00

functional programmer.

## 33665:00 - 33685:00

>> That's right. That's right. That's

## 33685:00 - 33705:00

right. And so the thing that they did

## 33705:00 - 33730:00

instead of getting people to kind of

## 33730:00 - 33765:00

change the way that they code, they they

## 33765:00 - 33805:00

built a type system around this. And it

## 33805:00 - 33835:00

was just it's brilliant because there's

## 33835:00 - 33865:00

all these ideas that no one was thinking

## 33865:00 - 33895:00

about even in academia like no one

## 33895:00 - 33920:00

thought of a bunch of these ideas. It

## 33920:00 - 33945:00

purely came out of the practice of

## 33945:00 - 33975:00

observing people and seeing how

## 33975:00 - 33995:00

JavaScript programmers want to write

## 33995:00 - 34035:00

code. And so you know for for quad code

## 34035:00 - 34065:00

it there there are some ideas that are

## 34065:00 - 34095:00

kind of similar in that you know like

## 34095:00 - 34120:00

you can use it like a Unix utility. You

## 34120:00 - 34140:00

can pipe into it. You can pipe out of

## 34140:00 - 34180:00

it. Um in some ways it is kind of

## 34180:00 - 34215:00

rigorous in this way but in in almost

## 34215:00 - 34250:00

every other way it's just the tool that

## 34250:00 - 34285:00

we wanted. like I I build a tool for

## 34285:00 - 34310:00

myself and then the team builds the tool

## 34310:00 - 34350:00

for themselves and then for anthropic

## 34350:00 - 34390:00

employees and then for users and it just

## 34390:00 - 34420:00

ends up being really useful. It's not

## 34420:00 - 34440:00

it's not this like principled and

## 34440:00 - 34490:00

academic thing which I think the the

## 34490:00 - 34515:00

proof is actually in the results. Now

## 34515:00 - 34580:00

fast forward more than 15 years later

## 34580:00 - 34610:00

not many codebases are in Haskell which

## 34610:00 - 34650:00

is more academic and there's tons of

## 34650:00 - 34680:00

them now on TypeScript because it's way

## 34680:00 - 34695:00

more practical

## 34695:00 - 34705:00

>> right

## 34705:00 - 34725:00

>> which is interesting. Yeah, it is

## 34725:00 - 34745:00

interesting, right? It's like TypeScript

## 34745:00 - 34765:00

solves a problem.

## 34765:00 - 34790:00

>> I guess one thing that's cool, I don't

## 34790:00 - 34810:00

know how many people know, but the

## 34810:00 - 34845:00

terminal is actually one of the most

## 34845:00 - 34905:00

beautiful terminal apps out there and is

## 34905:00 - 34950:00

actually written with React terminal.

## 34950:00 - 34970:00

>> When I first started building it, you

## 34970:00 - 35000:00

know, like I I did front-end engineering

## 35000:00 - 35035:00

for for a while. So, and I was also like

## 35035:00 - 35065:00

a, you know, I'm I'm sort of like a

## 35065:00 - 35100:00

hybrid, like I do like design and user

## 35100:00 - 35135:00

research and, you know, write code and

## 35135:00 - 35155:00

all this stuff. And we love hiring

## 35155:00 - 35185:00

engineers that are like this. Um, so we

## 35185:00 - 35220:00

just we love generalists. So for me it's

## 35220:00 - 35240:00

like okay, I'm building a thing for the

## 35240:00 - 35260:00

terminal. I'm actually kind of a shitty

## 35260:00 - 35300:00

Vim user. So like how do I build a thing

## 35300:00 - 35335:00

for people like me that um you know are

## 35335:00 - 35370:00

are going to be working in a terminal.

## 35370:00 - 35400:00

And I think just the delight is so

## 35400:00 - 35435:00

important. And I feel like at YC this is

## 35435:00 - 35455:00

something you talk about a lot, right?

## 35455:00 - 35470:00

It's like build a thing that people

## 35470:00 - 35505:00

love. If the product is useful but you

## 35505:00 - 35525:00

don't fall in love with it, that's not

## 35525:00 - 35565:00

great. Um so it kind of has to do both.

## 35565:00 - 35590:00

Designing for the terminal honestly has

## 35590:00 - 35620:00

been hard, right? It's like uh it's like

## 35620:00 - 35655:00

80 by 100 characters or whatever. you

## 35655:00 - 35690:00

have like 256 colors, you have one font

## 35690:00 - 35720:00

size, you don't have like mouse

## 35720:00 - 35750:00

interactions, there's all this stuff you

## 35750:00 - 35770:00

can't do, and there's all these very

## 35770:00 - 35800:00

hard trade-offs. So, like a little known

## 35800:00 - 35825:00

thing, for example, is you can actually

## 35825:00 - 35865:00

enable mouse interactions in a terminal.

## 35865:00 - 35885:00

So, you can enable like clicking and

## 35885:00 - 35890:00

stuff.

## 35890:00 - 35910:00

>> Oh, how do you do that in cloud code?

## 35910:00 - 35930:00

I've been trying to figure out how to do

## 35930:00 - 35940:00

this.

## 35940:00 - 35965:00

>> We don't we don't have it in cloud code

## 35965:00 - 35985:00

because we actually prototyped it a few

## 35985:00 - 36010:00

times and it felt really bad because the

## 36010:00 - 36035:00

trade-off is you have to virtualize

## 36035:00 - 36075:00

scrolling and so there's all these weird

## 36075:00 - 36090:00

trade-offs because like the way

## 36090:00 - 36120:00

terminals work is like there's no DOM,

## 36120:00 - 36145:00

right? It's like there's like anti-

## 36145:00 - 36180:00

escape codes and these kind of weird

## 36180:00 - 36215:00

organically evolved specs since like the

## 36215:00 - 36235:00

1960s or whatever.

## 36235:00 - 36265:00

>> Yeah. It feels like BBS's. It's like a

## 36265:00 - 36285:00

BBS door game.

## 36285:00 - 36290:00

>> Yeah.

## 36290:00 - 36305:00

>> Oh my god.

## 36305:00 - 36325:00

>> That's like that's like a great

## 36325:00 - 36345:00

compliment. Yeah. Yeah. Like it should

## 36345:00 - 36370:00

feel like you're discovering

## 36370:00 - 36400:00

>> Lord of the Red Dragon. It's fantastic.

## 36400:00 - 36415:00

Oh my god.

## 36415:00 - 36440:00

>> Yeah. But we have we've had to just like

## 36440:00 - 36475:00

discover all these kind of UX principles

## 36475:00 - 36505:00

for building the terminal cuz no one

## 36505:00 - 36535:00

really writes about this stuff. And if

## 36535:00 - 36565:00

you look at the big terminal apps of,

## 36565:00 - 36595:00

you know, like the 80s or 90s or 2000s

## 36595:00 - 36630:00

or whatever, they use like ed curses and

## 36630:00 - 36650:00

they have all these like windows and

## 36650:00 - 36675:00

things like this. And it just looks kind

## 36675:00 - 36705:00

of like janky by modern standards. It

## 36705:00 - 36745:00

just looks too heavy and complicated.

## 36745:00 - 36770:00

And so we had to like reinvent a lot.

## 36770:00 - 36790:00

And you know, for example, something

## 36790:00 - 36825:00

like the terminal spinner, like just

## 36825:00 - 36845:00

like the spinner words, it's gone

## 36845:00 - 36900:00

through probably I want to say like 50

## 36900:00 - 36930:00

maybe 100 iterations at this point. And

## 36930:00 - 36975:00

probably 80% of those didn't ship. So we

## 36975:00 - 37000:00

tried it, it didn't feel good, move on

## 37000:00 - 37015:00

to the next one. try it, didn't feel

## 37015:00 - 37050:00

good, move on to the next one. Uh, and

## 37050:00 - 37075:00

this was like sort of one of the amazing

## 37075:00 - 37105:00

things about quad code, right? Is like

## 37105:00 - 37125:00

you can write these prototypes and you

## 37125:00 - 37155:00

can just do like 20 prototypes back to

## 37155:00 - 37180:00

back, see which one you like, and then

## 37180:00 - 37200:00

ship that and the whole thing takes

## 37200:00 - 37225:00

maybe a couple hours.

## 37225:00 - 37240:00

>> Whereas in the past, what you would have

## 37240:00 - 37280:00

had to do is like wen to use origami or

## 37280:00 - 37300:00

framer or something like this. You built

## 37300:00 - 37325:00

like maybe three prototypes, it took

## 37325:00 - 37350:00

like two weeks. It just took much much

## 37350:00 - 37365:00

longer.

## 37365:00 - 37405:00

>> And so we have this luxury of we have to

## 37405:00 - 37425:00

discover this new thing. We have to

## 37425:00 - 37445:00

build a thing. We don't know what the

## 37445:00 - 37490:00

right endpoint is, but we can iterate

## 37490:00 - 37530:00

there so quickly and that's what makes

## 37530:00 - 37550:00

it really easy and that's what lets us

## 37550:00 - 37585:00

build a product that's like joyous and

## 37585:00 - 37610:00

that people like to use.

## 37610:00 - 37645:00

>> Boris, you had other advice for for

## 37645:00 - 37670:00

builders and we kept interrupting you

## 37670:00 - 37725:00

because we have so many questions, but

## 37725:00 - 37765:00

>> I would say um so okay, so maybe two

## 37765:00 - 37805:00

pieces of advice that are kind of weird

## 37805:00 - 37830:00

because it's like about building for the

## 37830:00 - 37870:00

model. So one is uh don't build for the

## 37870:00 - 37900:00

model of today, build for the model of 6

## 37900:00 - 37920:00

months from now. This is like sort of

## 37920:00 - 37940:00

weird, right? Because like you can't

## 37940:00 - 37965:00

find PMF if the product doesn't work.

## 37965:00 - 37985:00

But actually this is the thing that you

## 37985:00 - 38010:00

should do because otherwise what will

## 38010:00 - 38040:00

happen is you spend a bunch of work you

## 38040:00 - 38065:00

find PMF for the product right now and

## 38065:00 - 38090:00

then you're just going to get leaprogged

## 38090:00 - 38120:00

by someone else um because they're

## 38120:00 - 38140:00

building for the next model and a new

## 38140:00 - 38170:00

model comes out every few months. Use

## 38170:00 - 38195:00

the model, feel out the boundary of what

## 38195:00 - 38220:00

it can do and then build for the model

## 38220:00 - 38250:00

that you think will be the model maybe 6

## 38250:00 - 38280:00

months from now. I think the second

## 38280:00 - 38320:00

thing is um you know actually in the in

## 38320:00 - 38345:00

the quad code where in the quad code

## 38345:00 - 38370:00

area where we sit we have a framed copy

## 38370:00 - 38405:00

of the bitter lesson on the wall. Um and

## 38405:00 - 38450:00

this is this like rich sutton uh I like

## 38450:00 - 38475:00

everyone should read it if if you

## 38475:00 - 38525:00

haven't uh and the idea is the more

## 38525:00 - 38555:00

general model will always be the more

## 38555:00 - 38595:00

specific model and there's a lot of

## 38595:00 - 38620:00

corlaries to this but essentially what

## 38620:00 - 38650:00

it boils down to is never bet against

## 38650:00 - 38690:00

the model. Uh, and so this is just like

## 38690:00 - 38725:00

a thing to that that we always think

## 38725:00 - 38755:00

about where we could build a feature

## 38755:00 - 38785:00

into cloud code. We could make it better

## 38785:00 - 38805:00

as a product and we call this

## 38805:00 - 38830:00

scaffolding. That's all this code that's

## 38830:00 - 38865:00

not the model itself. But we could also

## 38865:00 - 38885:00

just wait like a couple months and the

## 38885:00 - 38915:00

model can probably just do the thing

## 38915:00 - 38950:00

instead. Um, and there's always this

## 38950:00 - 38970:00

trade-off, right? It's like engineering

## 38970:00 - 39005:00

work now and you can kind of extend the

## 39005:00 - 39040:00

capability a little bit, maybe 10 20% or

## 39040:00 - 39065:00

whatever in whatever domain on this

## 39065:00 - 39090:00

like, you know, like the spider chart of

## 39090:00 - 39125:00

what you're trying to extend. Um, or you

## 39125:00 - 39150:00

can just wait and the next model will do

## 39150:00 - 39175:00

it. So just always always think in terms

## 39175:00 - 39200:00

of this trade-off where where do you

## 39200:00 - 39235:00

actually want to invest and assume that

## 39235:00 - 39260:00

whatever the scaffolding is it's just

## 39260:00 - 39275:00

tech.

## 39275:00 - 39300:00

>> How often do you rewrite the code ways

## 39300:00 - 39345:00

of uh clock code is every six months

## 39345:00 - 39385:00

with this with this

## 39385:00 - 39405:00

>> is there scaffolding that you've deleted

## 39405:00 - 39420:00

because you don't need it anymore

## 39420:00 - 39445:00

because the model just improved.

## 39445:00 - 39485:00

>> Oh so much. Yeah. Like all of quad code

## 39485:00 - 39505:00

has just been written and rewritten and

## 39505:00 - 39530:00

rewritten and rewritten over and over

## 39530:00 - 39570:00

and over. We unhip tools every couple

## 39570:00 - 39600:00

weeks. We add new tools every couple

## 39600:00 - 39615:00

weeks.

## 39615:00 - 39640:00

There's no part of quad code that was

## 39640:00 - 39665:00

around six months ago. It's just

## 39665:00 - 39685:00

constantly rewritten.

## 39685:00 - 39720:00

>> Would you say most of the code base for

## 39720:00 - 39770:00

current cloud code is only say 80% of it

## 39770:00 - 39805:00

is only less than a couple months old.

## 39805:00 - 39830:00

>> Yeah, definitely. It might it might even

## 39830:00 - 39860:00

be like less than Yeah, maybe like a

## 39860:00 - 39880:00

couple months. That that feels about

## 39880:00 - 39885:00

right.

## 39885:00 - 39915:00

>> So it's like the life cycle of code now.

## 39915:00 - 39945:00

That's another alpha is expecting it to

## 39945:00 - 39970:00

be the shelf life to be just couple

## 39970:00 - 39980:00

months.

## 39980:00 - 39985:00

>> Yeah.

## 39985:00 - 40005:00

>> For the best founders.

## 40005:00 - 40045:00

>> Do you see uh Steve Yaggi's uh post

## 40045:00 - 40080:00

about how awesome working at Anthropic

## 40080:00 - 40115:00

is? And I think there's a line in there

## 40115:00 - 40165:00

that says that an anthropic engineer uh

## 40165:00 - 40205:00

currently averages 1,000x more

## 40205:00 - 40255:00

productivity than a Google engineer at

## 40255:00 - 40320:00

Google's peak which is really an insane

## 40320:00 - 40365:00

number honestly like 1,000x like you

## 40365:00 - 40395:00

know we're 3 years ago we were still

## 40395:00 - 40420:00

talking about 10x engineers now we're

## 40420:00 - 40460:00

talking about 1000x on top of a Google

## 40460:00 - 40485:00

engineer in the prime like this is

## 40485:00 - 40520:00

unbelievable honestly. Yeah, I mean

## 40520:00 - 40545:00

internally if you if you look at like

## 40545:00 - 40570:00

technical employees, they all use quad

## 40570:00 - 40605:00

code every day. Um, and even

## 40605:00 - 40630:00

non-technical employees, I think like

## 40630:00 - 40665:00

half the sales team uses quad code. Um,

## 40665:00 - 40680:00

they they've started switching to

## 40680:00 - 40705:00

co-work because it's a little easier to

## 40705:00 - 40730:00

use. It has like a VM, so it's a little

## 40730:00 - 40765:00

bit safer. But yeah, we actually we just

## 40765:00 - 40810:00

pulled a stat and the I think the team

## 40810:00 - 40840:00

doubled in size last year, but

## 40840:00 - 40870:00

productivity per engineer grew something

## 40870:00 - 40885:00

like 70%.

## 40885:00 - 40910:00

>> It's measured by

## 40910:00 - 40935:00

>> just like the simplest stupidest

## 40935:00 - 40965:00

measure, pull requests. Um, but we also

## 40965:00 - 40985:00

kind of cross check that against like

## 40985:00 - 41015:00

commits and like uh the lifetime of

## 41015:00 - 41045:00

commits and things like this. And since

## 41045:00 - 41070:00

quad code came out, productivity per

## 41070:00 - 41115:00

engineer at anthropic has grown 150%.

## 41115:00 - 41125:00

>> Oh my god.

## 41125:00 - 41170:00

>> Um, and this is crazy because I in my

## 41170:00 - 41200:00

old life I was responsible for code

## 41200:00 - 41220:00

quality at Meta.

## 41220:00 - 41240:00

>> Um, and I was responsible for the

## 41240:00 - 41270:00

quality of all of our code bases across

## 41270:00 - 41295:00

every product across like you know

## 41295:00 - 41335:00

Facebook, Instagram, WhatsApp, whatever.

## 41335:00 - 41365:00

>> And one of the things that the team

## 41365:00 - 41405:00

worked on was improving productivity.

## 41405:00 - 41440:00

And back then seeing a gain of something

## 41440:00 - 41475:00

like 2% in productivity that was like a

## 41475:00 - 41510:00

year of work by hundreds of people. And

## 41510:00 - 41550:00

so this like 100% this is just like

## 41550:00 - 41585:00

unheard of just completely unheard of.

## 41585:00 - 41610:00

>> What drove you to come over to

## 41610:00 - 41645:00

Anthropic? I mean basically as a builder

## 41645:00 - 41675:00

you could go anywhere. What was the

## 41675:00 - 41705:00

moment that made you say like actually

## 41705:00 - 41735:00

this is the set of people or this is the

## 41735:00 - 41795:00

approach. I was living in rural Japan

## 41795:00 - 41830:00

and I was opening up Hacker News every

## 41830:00 - 41880:00

morning and I was reading the news and

## 41880:00 - 41905:00

uh it was all it just started to be like

## 41905:00 - 41950:00

AI stuff at some point and uh I started

## 41950:00 - 41985:00

to use some of these early products and

## 41985:00 - 42010:00

uh I remember like the first couple

## 42010:00 - 42045:00

times that I used it I was just like it

## 42045:00 - 42075:00

just took my breath away. That was like

## 42075:00 - 42090:00

very cheesy to say, but that was

## 42090:00 - 42110:00

actually that was actually the feeling.

## 42110:00 - 42140:00

Like it was just like it was amazing

## 42140:00 - 42180:00

like as a as as a builder, I've just

## 42180:00 - 42210:00

never kind of felt felt this feeling

## 42210:00 - 42235:00

like using these very very early

## 42235:00 - 42265:00

products. That was like in the quad 2

## 42265:00 - 42290:00

days or you know something like that.

## 42290:00 - 42320:00

And so I I just talking started talking

## 42320:00 - 42350:00

to friends at Labs um just to kind of

## 42350:00 - 42415:00

see what was going on. Um and uh I met

## 42415:00 - 42455:00

Ben man who's one of the founders at uh

## 42455:00 - 42500:00

at Anthropic and uh he just immediately

## 42500:00 - 42535:00

won me over. Um and as soon as I met

## 42535:00 - 42555:00

kind of the rest of the team at an it

## 42555:00 - 42585:00

just won me over and I think I think

## 42585:00 - 42615:00

probably in two ways. So one is it

## 42615:00 - 42665:00

operates as a research lab. Um so the

## 42665:00 - 42700:00

product was teeny teeny tiny. It's

## 42700:00 - 42730:00

really all about building a safe model.

## 42730:00 - 42770:00

That's all that matters. Um and so this

## 42770:00 - 42790:00

idea of just being very close to the

## 42790:00 - 42810:00

model and being very close to

## 42810:00 - 42850:00

development and being not the most

## 42850:00 - 42880:00

important thing because the product

## 42880:00 - 42905:00

isn't anymore. It's just the model is

## 42905:00 - 42940:00

the thing that's the most important. Um

## 42940:00 - 42965:00

that really resonated with me after

## 42965:00 - 42990:00

building product for many years. And

## 42990:00 - 43020:00

then the second thing was just how

## 43020:00 - 43070:00

missiondriven it is. Um like I'm I'm a

## 43070:00 - 43095:00

huge sci-fi reader. My bookshelf is just

## 43095:00 - 43130:00

like filled with sci-fi. And so like I

## 43130:00 - 43165:00

just know how bad this can go.

## 43165:00 - 43190:00

>> And when I kind of think about what's

## 43190:00 - 43220:00

going to happen this year, it you know

## 43220:00 - 43255:00

it's going to be totally insane. And in

## 43255:00 - 43295:00

the worst case it can go very very bad.

## 43295:00 - 43320:00

>> Um and so I just wanted to be at a place

## 43320:00 - 43345:00

that really understood that and kind of

## 43345:00 - 43385:00

really internalized that. And at Ant,

## 43385:00 - 43405:00

you know, like if you overhear

## 43405:00 - 43430:00

conversations in the lunchroom or in the

## 43430:00 - 43460:00

hallway, people are talking about AI

## 43460:00 - 43500:00

safety. this is really the thing that

## 43500:00 - 43535:00

everyone cares about more than anything.

## 43535:00 - 43560:00

Um, and so I just wanted to be in a

## 43560:00 - 43585:00

place like that. I I know I know for me

## 43585:00 - 43610:00

personally the mission is just so

## 43610:00 - 43620:00

important.

## 43620:00 - 43665:00

>> What is gonna happen this year?

## 43665:00 - 43705:00

>> Okay. So if you think back like six

## 43705:00 - 43740:00

months ago and uh kind of what are the

## 43740:00 - 43760:00

predictions that people are making? So

## 43760:00 - 43805:00

Daario predicted that 90% of the code at

## 43805:00 - 43830:00

Anthropic would be would be written by

## 43830:00 - 43880:00

Quad. This is true. Um for me personally

## 43880:00 - 43940:00

it's been 100% for like since Opus 4.5.

## 43940:00 - 43985:00

Um I just I uninstalled my IDE. I don't

## 43985:00 - 44015:00

edit a single line of code by hand. It's

## 44015:00 - 44065:00

just 100% quad code and Opus. Um and you

## 44065:00 - 44095:00

know I land you know like 20 PR a day

## 44095:00 - 44125:00

every day. If you look at Enthropic

## 44125:00 - 44185:00

overall it ranges between like 70 to 90%

## 44185:00 - 44205:00

uh you know depending on the team. For a

## 44205:00 - 44235:00

lot of teams it's also like 100% for a

## 44235:00 - 44275:00

lot of people it's 100%. And I remember

## 44275:00 - 44310:00

making this prediction back in May when

## 44310:00 - 44350:00

we ged cloud code that you wouldn't need

## 44350:00 - 44400:00

an ID to code anymore. Uh and it was

## 44400:00 - 44425:00

totally crazy to say. I feel like people

## 44425:00 - 44450:00

in the audience gasped

## 44450:00 - 44465:00

>> because it was such like a silly

## 44465:00 - 44495:00

prediction at the time. But really all

## 44495:00 - 44525:00

it is is like you just like trace the

## 44525:00 - 44545:00

you know the exponential

## 44545:00 - 44575:00

>> and this is just like so deep in you

## 44575:00 - 44615:00

know the DNA at cuz like you know three

## 44615:00 - 44640:00

of our founders were co-authors of the

## 44640:00 - 44670:00

scaling laws paper they kind of they saw

## 44670:00 - 44700:00

this very early and so this is just like

## 44700:00 - 44725:00

tracing the exponential this is what's

## 44725:00 - 44760:00

going to happen and yes that happened.

## 44760:00 - 44790:00

So continuing to trace the exponential I

## 44790:00 - 44825:00

think what will happen is coding will be

## 44825:00 - 44865:00

generally solved for everyone. Um, and I

## 44865:00 - 44885:00

think today coding is practically

## 44885:00 - 44910:00

solved, you know, for me and I think

## 44910:00 - 44940:00

it'll be the case for everyone. Um, you

## 44940:00 - 44970:00

know, regardless of domain, I think

## 44970:00 - 44995:00

we're going to start to see the title

## 44995:00 - 45030:00

software engineer go away. And I think

## 45030:00 - 45055:00

it's just going to be maybe builder,

## 45055:00 - 45090:00

maybe product manager, maybe we'll keep

## 45090:00 - 45120:00

the title as kind of a vestigial thing,

## 45120:00 - 45150:00

but the work that people do, it's not

## 45150:00 - 45180:00

just going to be coding. It's software

## 45180:00 - 45200:00

engineers are also going to be writing

## 45200:00 - 45220:00

specs. They're going to be talking to

## 45220:00 - 45250:00

users. like this thing that we're

## 45250:00 - 45275:00

starting to see right now in our team

## 45275:00 - 45305:00

where engineers are very much

## 45305:00 - 45350:00

generalists and every single function on

## 45350:00 - 45380:00

our team codes like our PM's code, our

## 45380:00 - 45435:00

designers code, our EM codes, our um

## 45435:00 - 45475:00

like everyone our our finance guy codes

## 45475:00 - 45505:00

like everyone on our team codes. We're

## 45505:00 - 45530:00

going to start to see this everywhere.

## 45530:00 - 45560:00

So this is sort of uh this is kind of

## 45560:00 - 45590:00

like the lower bound if we just continue

## 45590:00 - 45630:00

the trend. The upper bound I think is a

## 45630:00 - 45665:00

lot scarier. Um, and this is something

## 45665:00 - 45705:00

like, you know, we hit ASL4. Um, and

## 45705:00 - 45730:00

this, you know, at anthropic, we talked

## 45730:00 - 45765:00

about these safety levels. ASL3 is where

## 45765:00 - 45800:00

the models are right now. ASL4 is the

## 45800:00 - 45840:00

model is recursively self-improving. Um,

## 45840:00 - 45860:00

and so if this happens, essentially, we

## 45860:00 - 45885:00

have to meet a bunch of criteria before

## 45885:00 - 45915:00

we can release a model. And so the the

## 45915:00 - 45950:00

extreme is that, you know, this happens

## 45950:00 - 45980:00

um or there's some kind of catastrophic

## 45980:00 - 46010:00

misuse like people are using the model

## 46010:00 - 46065:00

to design bioiruses, design zero days,

## 46065:00 - 46090:00

stuff like this. Um, and this is

## 46090:00 - 46110:00

something that we're really really

## 46110:00 - 46130:00

actively working on so that doesn't

## 46130:00 - 46170:00

happen. I think uh it's just been

## 46170:00 - 46195:00

honestly it's just been like so exciting

## 46195:00 - 46225:00

and humbling like seeing how people are

## 46225:00 - 46260:00

using quad code like uh you know I just

## 46260:00 - 46290:00

wanted to build a cool thing and it

## 46290:00 - 46320:00

ended up being really useful uh and that

## 46320:00 - 46355:00

was so surprising and so exciting.

## 46355:00 - 46385:00

>> My impression from Twitter or just the

## 46385:00 - 46415:00

outside is basically everyone went away

## 46415:00 - 46440:00

over the holidays and then like found

## 46440:00 - 46475:00

out about Claude code and it's just been

## 46475:00 - 46510:00

crazy ever since. Is that how it was for

## 46510:00 - 46550:00

you at like internally? Did you were you

## 46550:00 - 46585:00

having like a nice Christmas break and

## 46585:00 - 46620:00

then came back and like what happened?

## 46620:00 - 46645:00

Well, actually for all of December, I

## 46645:00 - 46680:00

was traveling around. Uh, and I I took a

## 46680:00 - 46700:00

coding vacation. So, we were kind of

## 46700:00 - 46720:00

traveling around and I was just like

## 46720:00 - 46745:00

coding every day. So, that was really

## 46745:00 - 46775:00

nice. Uh, and then I also started to use

## 46775:00 - 46805:00

Twitter at the time cuz like I I worked

## 46805:00 - 46840:00

on Threads back then way back when. So,

## 46840:00 - 46865:00

I've been a Threads user for a while.

## 46865:00 - 46890:00

So, I just like tried to see kind of

## 46890:00 - 46925:00

like other platforms where people are.

## 46925:00 - 46945:00

Yeah. I think for a lot of people they

## 46945:00 - 46965:00

kind of discovered that was the moment

## 46965:00 - 46995:00

where they discovered Opus 4.5. I kind

## 46995:00 - 47010:00

of already knew.

## 47010:00 - 47015:00

>> Mhm.

## 47015:00 - 47045:00

>> Uh, and internally quad code's just been

## 47045:00 - 47085:00

on this like exponential tear for many

## 47085:00 - 47115:00

many months now. So that just like it it

## 47115:00 - 47155:00

became even more steep. That's what we

## 47155:00 - 47200:00

saw. And if you look at cloud code now,

## 47200:00 - 47215:00

you know, there was some stat from

## 47215:00 - 47255:00

Mercury that like 70% of startups are

## 47255:00 - 47290:00

you know choosing cloud as their model

## 47290:00 - 47320:00

of choice. There was some other stat

## 47320:00 - 47360:00

from like semi analysis that 4% of all

## 47360:00 - 47395:00

public commits are made by cloud code.

## 47395:00 - 47435:00

um like of all code written everywhere.

## 47435:00 - 47460:00

All the companies, you know, use squad

## 47460:00 - 47490:00

code from like the biggest companies to

## 47490:00 - 47525:00

kind of, you know, smallest startups,

## 47525:00 - 47550:00

you know, like it it wrote it it plotted

## 47550:00 - 47585:00

the course for Perseverance like for

## 47585:00 - 47615:00

like the Mars rover. This is just like

## 47615:00 - 47640:00

this is the coolest thing for me. And we

## 47640:00 - 47670:00

like we even printed posters cuz the

## 47670:00 - 47690:00

team was like, "Wow, this is just like

## 47690:00 - 47720:00

so cool that NASA chooses to use this

## 47720:00 - 47740:00

thing." So, yeah, it's just like it's

## 47740:00 - 47775:00

humbling. Um but it also feels like the

## 47775:00 - 47800:00

very beginning. What's the sort of

## 47800:00 - 47835:00

interaction between uh claude code and

## 47835:00 - 47890:00

then co-work like you know was it a fork

## 47890:00 - 47945:00

of cla code? Was it like you had cla

## 47945:00 - 47990:00

code look at the cloud code and say

## 47990:00 - 48030:00

let's make a new spec for nontechnical

## 48030:00 - 48060:00

people that you know keeps all the

## 48060:00 - 48090:00

lessons and then you know it sort of

## 48090:00 - 48120:00

went off for a couple days and did that.

## 48120:00 - 48155:00

What's the genesis of that and you know

## 48155:00 - 48185:00

where do you think that goes?

## 48185:00 - 48210:00

>> This is going to be like my fifth time

## 48210:00 - 48250:00

using the word wait and demand.

## 48250:00 - 48275:00

It was just that I mean like we we were

## 48275:00 - 48295:00

looking at Twitter and there was like

## 48295:00 - 48320:00

that one guy that was using quad code to

## 48320:00 - 48345:00

like monitor his tomato plants.

## 48345:00 - 48350:00

>> Mhm.

## 48350:00 - 48380:00

>> Uh there was like this other person that

## 48380:00 - 48410:00

was using it to like recover wedding

## 48410:00 - 48440:00

photos off of a corrupted hard drive.

## 48440:00 - 48475:00

There were people that using it for like

## 48475:00 - 48505:00

uh for finance. When we looked

## 48505:00 - 48545:00

internally at anthropic, every designer

## 48545:00 - 48575:00

is using it all the entire finance team

## 48575:00 - 48605:00

at this point is using it. The entire

## 48605:00 - 48630:00

data science team is using it not for

## 48630:00 - 48660:00

coding. People are jumping over hoops to

## 48660:00 - 48680:00

install a thing in the terminal so that

## 48680:00 - 48705:00

they could use this. So we knew for a

## 48705:00 - 48725:00

while that we wanted to build something

## 48725:00 - 48755:00

and so we're experimenting with a bunch

## 48755:00 - 48790:00

of different ideas and the thing that

## 48790:00 - 48820:00

kind of took off was just you know a

## 48820:00 - 48845:00

little cloud code wrapper in a guey in

## 48845:00 - 48870:00

the desktop app and that's all it is.

## 48870:00 - 48895:00

It's just quad code under the hood. It's

## 48895:00 - 48910:00

the same agent.

## 48910:00 - 48925:00

>> Oh wow.

## 48925:00 - 48970:00

>> Um and uh Felix and the team and Felix

## 48970:00 - 49000:00

was early Electron contributor. He kind

## 49000:00 - 49025:00

of knows that stack really well and he

## 49025:00 - 49070:00

was hacking on various ideas and uh they

## 49070:00 - 49100:00

they built it in I think something like

## 49100:00 - 49130:00

10 days. It was it was just like 100%

## 49130:00 - 49170:00

written by quad code. Uh and it just

## 49170:00 - 49205:00

felt ready to release. There was a lot

## 49205:00 - 49235:00

of stuff that we had to build for

## 49235:00 - 49265:00

nontechnical users. So it's a little bit

## 49265:00 - 49305:00

different than a technical audience. Uh

## 49305:00 - 49335:00

it runs in a all the code runs in a

## 49335:00 - 49365:00

virtual machine. Uh there's a lot of

## 49365:00 - 49405:00

delete uh protections for deletion and

## 49405:00 - 49435:00

things like this. There's a lot of

## 49435:00 - 49465:00

permission prompting and kind of other

## 49465:00 - 49515:00

guardrails for users. Um yeah, it was

## 49515:00 - 49550:00

honestly pretty obvious. Boris, thank

## 49550:00 - 49595:00

you so much for making something that uh

## 49595:00 - 49635:00

is taking away all my sleep, but in

## 49635:00 - 49675:00

return, it's making me feel creator mode

## 49675:00 - 49715:00

again, sort of founder mode again. It's

## 49715:00 - 49750:00

been an exhilarating 3 weeks. I like

## 49750:00 - 49775:00

can't believe I waited that long since

## 49775:00 - 49805:00

November to actually get into it. Thank

## 49805:00 - 49840:00

you so much for being with us. Thank you

## 49840:00 - 49875:00

for building what you're building.

## 49875:00 - 49910:00

>> Yeah, thanks for having me. And uh send

## 49910:00 - 49940:00

bugs.

## 49940:00 - 49990:00

>> Sounds good.

## 49990:00 - 50025:00

Come

## 50025:00+

on now.

