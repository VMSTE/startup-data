---
source: https://www.youtube.com/watch?v=BJjsfNO5JTo
title: How To Get The Most Out Of Vibe Coding | Startup School
author: Y Combinator
date: 2025-04-25
views: 343322
description: >-
  AI can't yet one-shot an entire product—but with the rise of vibe coding, it's
  getting close.  


  YC's Tom Blomfield has spent the last month building side projects with tools
  like Claude Code, Windsurf, and Aqua, seeing just how far you can push modern
  LLMs. From writing full-stack apps to debugging with a single paste of an
  error message, AI is becoming a legit collaborator in the dev process. This
  video is a playbook for anyone who wants to get the most out of vibe coding
  and build faster.


  Apply to Y Combinator: https://ycombinator.com/apply

  Work at a startup: https://workatastartup.com


  Chapters (Powered by https://chapterme.co/) - 

  0:00 Intro

  0:54 Some vibe coding tips from YC X25 founders

  4:12 First, pick your tools and make a plan 

  6:27 Use version control 

  7:23 Write tests 

  8:14 Remember, LLM's aren't just for coding

  8:57 Bug fixes

  11:10 Documentation

  12:03 Functionality 

  13:20 Choose the correct stack

  15:08 Refactor frequently

  15:40 Keep experimenting!

  16:21 Outro
tags:
  - YC
  - Y Combinator
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:46:24.920Z
---

# How To Get The Most Out Of Vibe Coding | Startup School

## 00:00 - 150:00

[Music]

## 150:00 - 195:00

Hi, I'm Tom and I'm a partner here at

## 195:00 - 230:00

YC. For the last month, I've been

## 230:00 - 270:00

experimenting vibe coding, a couple of

## 270:00 - 325:00

side projects and I found not only is it

## 325:00 - 355:00

remarkably good, but it's also a

## 355:00 - 385:00

practice you can get measurably better

## 385:00 - 420:00

at if you're open to tinkering and

## 420:00 - 450:00

picking up best practices. In this

## 450:00 - 485:00

video, I want to share some ways you can

## 485:00 - 530:00

get great results when vibe coding. It's

## 530:00 - 565:00

kind of like uh prompt engineering from

## 565:00 - 590:00

a year or two ago. People were

## 590:00 - 630:00

discovering new stuff every week and

## 630:00 - 665:00

posting about it on social media. The

## 665:00 - 705:00

best techniques are the same techniques

## 705:00 - 745:00

that a professional software engineer

## 745:00 - 780:00

might use. And some people like, well,

## 780:00 - 800:00

that's not vibe coding, is it? You're

## 800:00 - 835:00

now just software engineering. I I I

## 835:00 - 865:00

kind of think that's beside the point.

## 865:00 - 890:00

We're trying to use these tools to get

## 890:00 - 925:00

the best results. And the YC Spring

## 925:00 - 950:00

Batch just kicked off a couple of weeks

## 950:00 - 985:00

ago. And before I give you my advice for

## 985:00 - 1015:00

Vibe Coding, let's hear from the

## 1015:00 - 1050:00

founders on the tips they're using to

## 1050:00 - 1085:00

get the best out of the AI tools today.

## 1085:00 - 1110:00

If you get stuck in a place where the AI

## 1110:00 - 1145:00

ID can't implement or can't debug

## 1145:00 - 1170:00

something and it's just stuck in a loop,

## 1170:00 - 1215:00

sometimes going to the LLM's website,

## 1215:00 - 1235:00

like literally to the UI and just

## 1235:00 - 1265:00

pasting in your code and asking the same

## 1265:00 - 1300:00

question can get you a result that for

## 1300:00 - 1330:00

whatever reason the ID like couldn't get

## 1330:00 - 1355:00

to and you can solve your problem that

## 1355:00 - 1390:00

way. So I'd say like just load up both

## 1390:00 - 1430:00

cursor and windsurf on the same project.

## 1430:00 - 1470:00

Um cursor it's a bit faster so you can

## 1470:00 - 1500:00

do a lot of like the front end like a

## 1500:00 - 1520:00

little more like full stacky like link

## 1520:00 - 1555:00

the front end to the back end. Windsurf

## 1555:00 - 1585:00

thinks for a bit longer. I used to just

## 1585:00 - 1605:00

be like scrolling on my phone while I

## 1605:00 - 1635:00

type build this agent or like you know

## 1635:00 - 1670:00

like like modify this prompt and I'll

## 1670:00 - 1710:00

just like scroll fix scroll or like you

## 1710:00 - 1740:00

know paste an error. Now while I'm

## 1740:00 - 1770:00

waiting for uh winds surf to think I can

## 1770:00 - 1800:00

go on cursor and like you know start

## 1800:00 - 1825:00

updating the front end. Uh, sometimes

## 1825:00 - 1860:00

I'll load up both at the same time and

## 1860:00 - 1890:00

like have like the same context. Maybe

## 1890:00 - 1915:00

if I'm trying to update the front end,

## 1915:00 - 1940:00

I'll give it like style it in like the

## 1940:00 - 1975:00

style of that file and then I'll just

## 1975:00 - 2005:00

press enter for both and then they'll

## 2005:00 - 2040:00

both basically give me like slightly

## 2040:00 - 2065:00

different iterations of the same front

## 2065:00 - 2085:00

end and I'll just pick which one I like

## 2085:00 - 2125:00

better. My advice would be to uh think

## 2125:00 - 2150:00

of the AI as a different kind of

## 2150:00 - 2185:00

programming language and vibe coding as

## 2185:00 - 2215:00

being a different um a new type of

## 2215:00 - 2250:00

programming language. And so instead of

## 2250:00 - 2275:00

programming with code, you're

## 2275:00 - 2325:00

programming with language. And uh

## 2325:00 - 2350:00

because of that you kind of have to

## 2350:00 - 2395:00

provide a lot of the necessary context

## 2395:00 - 2430:00

and uh information in a very detailed

## 2430:00 - 2465:00

way if you want to get good results. I

## 2465:00 - 2500:00

usually start wipe coding in the reverse

## 2500:00 - 2530:00

direction that is first starting from

## 2530:00 - 2570:00

the test cases. I handcraft my test

## 2570:00 - 2600:00

cases. I don't use any LLMs to write my

## 2600:00 - 2655:00

test cases and once it is done I have

## 2655:00 - 2700:00

strong guard rules that my LLMs can uh

## 2700:00 - 2730:00

can follow for generating the code.

## 2730:00 - 2755:00

Right? and then they can freely generate

## 2755:00 - 2785:00

the code that they want to generate. And

## 2785:00 - 2825:00

once I see those green flags on my test

## 2825:00 - 2850:00

cases, the job is done. I don't need to

## 2850:00 - 2895:00

micromanage my code bases. I just I just

## 2895:00 - 2930:00

uh take overview about the modularity of

## 2930:00 - 2960:00

the code. Other than that, it's fine.

## 2960:00 - 2985:00

Yeah, I think it's very important to

## 2985:00 - 3020:00

first spend like unreasonable amount of

## 3020:00 - 3080:00

time uh in like a pure LLM to build out

## 3080:00 - 3105:00

like the scope and the actual

## 3105:00 - 3135:00

architecture of what you're trying to

## 3135:00 - 3175:00

build before offloading that to cursor

## 3175:00 - 3210:00

or any other kind of coding tool uh and

## 3210:00 - 3240:00

let it just like free run in the

## 3240:00 - 3270:00

codebase just random making up stuff

## 3270:00 - 3305:00

that doesn't really work. Um so make

## 3305:00 - 3325:00

sure you understand what the actual goal

## 3325:00 - 3360:00

of what you're building is. My advice

## 3360:00 - 3405:00

would be to really monitor whether the

## 3405:00 - 3435:00

LLM is falling into a rabbit hole when

## 3435:00 - 3470:00

it's answering your question. And if you

## 3470:00 - 3510:00

notice that it just keeps regenerating

## 3510:00 - 3550:00

code and it looks kind of funky. It's

## 3550:00 - 3570:00

not really able to figure it out. If

## 3570:00 - 3600:00

you're having to find yourself copy and

## 3600:00 - 3640:00

pasting error messages all the time, it

## 3640:00 - 3685:00

probably means something's gone uh ary

## 3685:00 - 3715:00

and you should take a step back, even

## 3715:00 - 3750:00

prompt the LLM and say, "Hey, you know,

## 3750:00 - 3775:00

let's take a step back and try to

## 3775:00 - 3825:00

examine basically why it's failing. Is

## 3825:00 - 3855:00

it a, you know, is it because you

## 3855:00 - 3890:00

haven't provided enough context for the

## 3890:00 - 3925:00

LM to be able to figure it out or have

## 3925:00 - 3960:00

you just gotten unlucky and it's unable

## 3960:00 - 4000:00

to do your request? The overarching

## 4000:00 - 4050:00

theme here is to make the LLM follow the

## 4050:00 - 4090:00

processes that a good professional

## 4090:00 - 4125:00

software developer would use. So, let's

## 4125:00 - 4160:00

dive in and explore some of the best

## 4160:00 - 4205:00

vibe coding advice I've seen. First,

## 4205:00 - 4245:00

where to start. If you've never written

## 4245:00 - 4285:00

any code before, I would probably go for

## 4285:00 - 4330:00

a tool like Replet or Lovable. They give

## 4330:00 - 4375:00

you an easy to use visual interface and

## 4375:00 - 4425:00

it's a great way to try out new UIs

## 4425:00 - 4465:00

directly in code. Many product managers

## 4465:00 - 4490:00

and designers are actually going

## 4490:00 - 4530:00

straight to implementation of a new idea

## 4530:00 - 4570:00

in code rather than designing mock-ups

## 4570:00 - 4595:00

in something like Figma just because

## 4595:00 - 4645:00

it's so quick. But when I tried this, I

## 4645:00 - 4680:00

was impressed with the UIs. But tools

## 4680:00 - 4720:00

like Lovable started to struggle when I

## 4720:00 - 4765:00

wanted to more precisely modify backend

## 4765:00 - 4810:00

logic rather than just pure UI changes.

## 4810:00 - 4845:00

I'd change a button over here and the

## 4845:00 - 4895:00

backend logic would bizarrely change. So

## 4895:00 - 4925:00

if you've written code before, even if

## 4925:00 - 4955:00

you're a little bit rusty like me, you

## 4955:00 - 4995:00

can probably leap straight to tools like

## 4995:00 - 5040:00

Windsurf Cursor or Claude Code. Once

## 5040:00 - 5080:00

you've picked the tool you want to use,

## 5080:00 - 5105:00

the first step is not to dive in and

## 5105:00 - 5140:00

write code. Instead, I would work with

## 5140:00 - 5205:00

the LLM to write a comprehensive plan.

## 5205:00 - 5245:00

Put that in a markdown file inside your

## 5245:00 - 5280:00

project folder and keep referring back

## 5280:00 - 5310:00

to it. This is a plan that you develop

## 5310:00 - 5345:00

with the AI and you sort of step through

## 5345:00 - 5365:00

while you're implementing the project

## 5365:00 - 5390:00

rather than trying to oneshot the whole

## 5390:00 - 5435:00

thing. And so what I'd do after you've

## 5435:00 - 5465:00

created the first draft of this plan, go

## 5465:00 - 5510:00

through it, delete or remove things that

## 5510:00 - 5545:00

you don't like. You might mark certain

## 5545:00 - 5580:00

features explicitly as won't do too

## 5580:00 - 5615:00

complicated. And you might also like to

## 5615:00 - 5655:00

keep a section of ideas for later. You

## 5655:00 - 5690:00

know, to tell the LLM, look, I consider

## 5690:00 - 5720:00

this, but it's out of scope for now.

## 5720:00 - 5760:00

Once you've got that plan, work with the

## 5760:00 - 5800:00

LLM to implement it section by section

## 5800:00 - 5835:00

and explicitly say, let's just do

## 5835:00 - 5870:00

section two right now. Then you check

## 5870:00 - 5905:00

that it works. You run your tests and

## 5905:00 - 5940:00

you get commit. Then have the AI go back

## 5940:00 - 5970:00

to your plan and mark section two as

## 5970:00 - 6010:00

complete. I probably wouldn't expect the

## 6010:00 - 6065:00

models to oneshot entire products yet,

## 6065:00 - 6100:00

especially if they're complicated. I

## 6100:00 - 6130:00

prefer to do this piece by piece and

## 6130:00 - 6150:00

make sure I have a working

## 6150:00 - 6175:00

implementation of each step and

## 6175:00 - 6210:00

crucially commit it to Git so that you

## 6210:00 - 6245:00

can revert if if things go wrong on the

## 6245:00 - 6290:00

the next step. But honestly, this advice

## 6290:00 - 6330:00

might change in the next 2 or 3 months.

## 6330:00 - 6365:00

The models are getting better so quickly

## 6365:00 - 6390:00

that it's hard to say where we're going

## 6390:00 - 6430:00

to be in the near future. My next tip is

## 6430:00 - 6475:00

to use version control. Version control

## 6475:00 - 6535:00

is your friend. Use Git religiously. I

## 6535:00 - 6570:00

know the tools have these kind of revert

## 6570:00 - 6605:00

sort of functionality. I don't trust

## 6605:00 - 6635:00

them yet. So, I always make sure I'm

## 6635:00 - 6665:00

starting with a kind of a clean git

## 6665:00 - 6695:00

slate before I start a new feature so

## 6695:00 - 6730:00

that I can revert to a known working

## 6730:00 - 6770:00

version if the AI goes off on a vision

## 6770:00 - 6815:00

quest. So, don't be afraid to get reset

## 6815:00 - 6855:00

head hard if it's not working and just

## 6855:00 - 6900:00

roll the dice again. I found I had bad

## 6900:00 - 6950:00

results if I'm like prompting the AI

## 6950:00 - 6980:00

multiple times to try to get something

## 6980:00 - 7020:00

working. It tends to accumulate layers

## 7020:00 - 7070:00

and layers and layers of bad code rather

## 7070:00 - 7105:00

than like really understanding the root

## 7105:00 - 7150:00

cause. You might go and and try four,

## 7150:00 - 7180:00

five, six different prompts and you

## 7180:00 - 7205:00

finally get the solution. I'd actually

## 7205:00 - 7255:00

just take that solution, get reset, and

## 7255:00 - 7295:00

then feed that solution into the AI on a

## 7295:00 - 7330:00

clean codebase so you can implement that

## 7330:00 - 7360:00

clean solution without layers and layers

## 7360:00 - 7395:00

of of craft. The next thing you should

## 7395:00 - 7440:00

do is write tests or get your LLM to

## 7440:00 - 7470:00

write tests for you. They're pretty good

## 7470:00 - 7510:00

at this. Although they often default to

## 7510:00 - 7555:00

writing very low-level like unit tests,

## 7555:00 - 7590:00

I prefer to keep these tests super high

## 7590:00 - 7635:00

level. uh basically you want to simulate

## 7635:00 - 7670:00

someone clicking through the the site or

## 7670:00 - 7715:00

the app and ensure that the features are

## 7715:00 - 7760:00

working end to end rather than testing

## 7760:00 - 7810:00

uh functions on a kind of unit basis and

## 7810:00 - 7845:00

so make sure you write highlevel

## 7845:00 - 7875:00

integration tests before you move on to

## 7875:00 - 7925:00

the next feature. LLMs have a bad habit

## 7925:00 - 7960:00

of making unnecessary changes to

## 7960:00 - 7990:00

unrelated logic. So you tell it to fix

## 7990:00 - 8015:00

this thing over there and it just

## 8015:00 - 8040:00

changes some logic over here for really

## 8040:00 - 8075:00

no reason at all. And so having these

## 8075:00 - 8110:00

test suites in place catch these

## 8110:00 - 8150:00

regressions early will identify when the

## 8150:00 - 8180:00

LLM has has gone off and made

## 8180:00 - 8215:00

unnecessary changes so that you can get

## 8215:00 - 8265:00

reset and start again. Keep in mind LLMs

## 8265:00 - 8305:00

aren't just for coding. I use them for a

## 8305:00 - 8335:00

lot of non-coding work when I'm building

## 8335:00 - 8360:00

these kind of side projects. For

## 8360:00 - 8420:00

example, I had uh Claude Sonet 3.7

## 8420:00 - 8455:00

configure my DNS servers which is always

## 8455:00 - 8500:00

a task I hated and set up Heroku hosting

## 8500:00 - 8545:00

via a command line tool. It was a DevOps

## 8545:00 - 8575:00

engineer for me and accelerated my

## 8575:00 - 8620:00

progress like 10x. I also used chat GPT

## 8620:00 - 8665:00

to create a um an image for my site's

## 8665:00 - 8695:00

favicon, that little icon that appears

## 8695:00 - 8730:00

at the top of the the browser window.

## 8730:00 - 8770:00

And then Claude took that image and

## 8770:00 - 8810:00

wrote a quick throwaway script to resize

## 8810:00 - 8845:00

it into the six different sizes and

## 8845:00 - 8890:00

formats I needed for favicons across all

## 8890:00 - 8925:00

different platforms. So the AI is now my

## 8925:00 - 8960:00

designer as well. Okay, so now let's

## 8960:00 - 9010:00

look at bug fixes. The first thing I do

## 9010:00 - 9060:00

when I encounter any bug is just copy

## 9060:00 - 9095:00

paste the error message straight back

## 9095:00 - 9125:00

into the LLM. It might be from your

## 9125:00 - 9170:00

server log files or the JavaScript

## 9170:00 - 9220:00

console in the browser. Often this error

## 9220:00 - 9260:00

message is enough for the AI to identify

## 9260:00 - 9290:00

and fix a problem. You don't even need

## 9290:00 - 9310:00

to explain what's going wrong or what

## 9310:00 - 9345:00

you think's going wrong. Simply the

## 9345:00 - 9380:00

error message is enough. It's so

## 9380:00 - 9410:00

powerful that pretty soon I actually

## 9410:00 - 9445:00

expect all the major coding tools to be

## 9445:00 - 9485:00

able to ingest these errors without

## 9485:00 - 9510:00

humans having to copy paste. If you

## 9510:00 - 9540:00

think about it, our value being the

## 9540:00 - 9585:00

copypaste machine is is uh kind of

## 9585:00 - 9605:00

weird, right? We're like we're we're

## 9605:00 - 9635:00

leaving the thinking to LLM. But I think

## 9635:00 - 9660:00

that copyping is going to go out the

## 9660:00 - 9690:00

window and these LLM tools are going to

## 9690:00 - 9735:00

be able to tail logs or you know um spin

## 9735:00 - 9770:00

up a headless browser and inspect the

## 9770:00 - 9810:00

the kind of JavaScript errors. With more

## 9810:00 - 9850:00

complex bugs, you can ask the LLM to

## 9850:00 - 9880:00

think through three or four possible

## 9880:00 - 9930:00

causes before writing any code. After

## 9930:00 - 9970:00

each failed attempt at fixing the bug, I

## 9970:00 - 10000:00

would get reset and start again again so

## 10000:00 - 10025:00

you're not accumulating layers and

## 10025:00 - 10060:00

layers of crust. Don't make multiple

## 10060:00 - 10105:00

attempts at bug fixes without resetting

## 10105:00 - 10135:00

because the LLM just adds more layers of

## 10135:00 - 10180:00

crap. Get reset, start again, and add

## 10180:00 - 10220:00

logging. Logging is your friend. If in

## 10220:00 - 10250:00

doubt, if it's not working, switch

## 10250:00 - 10310:00

models. Maybe it's Claude um Sonic 3.7,

## 10310:00 - 10335:00

maybe it's one of the OpenAI models,

## 10335:00 - 10385:00

maybe it's Gemini. I often find that um

## 10385:00 - 10420:00

different models succeed where the

## 10420:00 - 10450:00

others fail. And if you do eventually

## 10450:00 - 10485:00

find the source of a gnarly bug, I would

## 10485:00 - 10535:00

just reset all of the changes and then

## 10535:00 - 10565:00

um give the LLM very specific

## 10565:00 - 10605:00

instructions on how to fix that precise

## 10605:00 - 10660:00

bug on a clean code base to avoid this

## 10660:00 - 10695:00

like layers and layers of of junk code

## 10695:00 - 10735:00

accumulating. Next tip is to write

## 10735:00 - 10770:00

instructions for the LLM. Put these

## 10770:00 - 10800:00

instructions in whether it's cursor

## 10800:00 - 10850:00

rules, windsurf rules, claw markdown

## 10850:00 - 10890:00

file. Each tool has a slightly different

## 10890:00 - 10925:00

naming convention. But I know founders

## 10925:00 - 10960:00

who've written hundreds of lines of

## 10960:00 - 11005:00

instructions for uh their AI coding

## 11005:00 - 11040:00

agent and it makes them way way way more

## 11040:00 - 11075:00

effective. There's tons of advice online

## 11075:00 - 11100:00

about what to put in these instruction

## 11100:00 - 11125:00

files. I'll let you go and find that on

## 11125:00 - 11155:00

your own. Okay, let's talk about

## 11155:00 - 11200:00

documentation. I still find that

## 11200:00 - 11245:00

pointing these agents at online web

## 11245:00 - 11280:00

documentation is a little bit patchy

## 11280:00 - 11305:00

still. I mean, some people are

## 11305:00 - 11350:00

suggesting uh using an MCP server to

## 11350:00 - 11365:00

access this

## 11365:00 - 11400:00

documentation, which works for some

## 11400:00 - 11430:00

people. Uh seems like overkill to me.

## 11430:00 - 11480:00

So, I'll often just download all of the

## 11480:00 - 11515:00

documentation for a given set of APIs

## 11515:00 - 11555:00

and put them in a subdirectory of my

## 11555:00 - 11595:00

working folder so the LLM can access

## 11595:00 - 11620:00

them locally. And then in my

## 11620:00 - 11645:00

instructions, I'll say go and read the

## 11645:00 - 11675:00

docs before you implement this thing.

## 11675:00 - 11705:00

And it's often much more accurate. A

## 11705:00 - 11740:00

side note to remember, you can use the

## 11740:00 - 11780:00

LLM as a teacher, especially for people

## 11780:00 - 11805:00

who are less familiar with the coding

## 11805:00 - 11835:00

language. You might implement something

## 11835:00 - 11870:00

and then get the AI to walk through that

## 11870:00 - 11910:00

implementation line by line and explain

## 11910:00 - 11960:00

it to you. It's a great way to learn new

## 11960:00 - 11995:00

technologies. It's much better than

## 11995:00 - 12030:00

scrolling Stack Overflow like uh we all

## 12030:00 - 12065:00

used to do. Now, let's look at more

## 12065:00 - 12100:00

complex functionality. If you're working

## 12100:00 - 12145:00

on a a new piece of functionality, a new

## 12145:00 - 12180:00

feature that's more complex than you'd

## 12180:00 - 12220:00

normally trust the AI to implement, I

## 12220:00 - 12265:00

would do it as a standalone project in a

## 12265:00 - 12315:00

totally clean codebase. Get a small

## 12315:00 - 12350:00

reference implementation working without

## 12350:00 - 12375:00

the the complication of your existing

## 12375:00 - 12420:00

project or even download a reference

## 12420:00 - 12445:00

implementation if someone's written one

## 12445:00 - 12495:00

and posted on GitHub. Then you point to

## 12495:00 - 12545:00

your LLM at the implementation and tell

## 12545:00 - 12575:00

it to follow that while reimplementing

## 12575:00 - 12620:00

it inside your larger codebase. It

## 12620:00 - 12650:00

actually works surprisingly well.

## 12650:00 - 12700:00

Remember, small files and modularity are

## 12700:00 - 12735:00

your friend. This is true for human

## 12735:00 - 12780:00

coders as well. I think we might see a

## 12780:00 - 12810:00

shift towards more modular or

## 12810:00 - 12855:00

service-based architecture where the LLM

## 12855:00 - 12895:00

has clear API boundaries that it can

## 12895:00 - 12930:00

work within while maintaining a

## 12930:00 - 12965:00

consistent external interface rather

## 12965:00 - 13010:00

than these huge uh monor repos with

## 13010:00 - 13045:00

massive interdependencies. These are

## 13045:00 - 13085:00

hard for both humans and LLMs. It's just

## 13085:00 - 13120:00

not clear if a change in one place is

## 13120:00 - 13150:00

going to impact another part part of the

## 13150:00 - 13195:00

codebase. And so having this this modern

## 13195:00 - 13230:00

architecture with a consistent external

## 13230:00 - 13270:00

API means you can change the internals

## 13270:00 - 13300:00

as long as the external interface in the

## 13300:00 - 13330:00

test still pass you're probably good.

## 13330:00 - 13365:00

Now a note on choosing the right text

## 13365:00 - 13410:00

stack. I chose to build my project

## 13410:00 - 13445:00

partially in Ruby on Rails mostly

## 13445:00 - 13470:00

because I was familiar with it from when

## 13470:00 - 13500:00

I used to um be a professional

## 13500:00 - 13545:00

developer. But I was blown away by the

## 13545:00 - 13580:00

AI's performance especially when it was

## 13580:00 - 13630:00

writing uh Rubon Rails code. And I think

## 13630:00 - 13670:00

this is because Rails is a 20-year-old

## 13670:00 - 13710:00

framework with a ton of wellestablished

## 13710:00 - 13760:00

conventions. A lot of Rails code bases

## 13760:00 - 13790:00

look very, very similar and it's obvious

## 13790:00 - 13815:00

to an experienced Ruby on Rails

## 13815:00 - 13845:00

developer where a specific piece of

## 13845:00 - 13890:00

functionality should live or the right

## 13890:00 - 13915:00

Rails way of achieving a certain

## 13915:00 - 13960:00

outcome. That means there's a ton of

## 13960:00 - 14005:00

pretty consistent highquality training

## 14005:00 - 14050:00

data for Rails code bases online. I've

## 14050:00 - 14085:00

had other friends have less success with

## 14085:00 - 14120:00

languages like Rust or Elixir where

## 14120:00 - 14150:00

there's just not as much training data

## 14150:00 - 14190:00

online, but who knows that might change

## 14190:00 - 14260:00

very soon. Okay, next bit of advice, use

## 14260:00 - 14300:00

screenshots. You can copy and paste

## 14300:00 - 14330:00

screenshots into most coding agents

## 14330:00 - 14370:00

these days and it's very useful either

## 14370:00 - 14400:00

to demonstrate a bug in the UI

## 14400:00 - 14445:00

implementation that you can see or to

## 14445:00 - 14500:00

pull in design uh inspiration from

## 14500:00 - 14530:00

another site that you might want to use

## 14530:00 - 14585:00

in your project. Voice is another really

## 14585:00 - 14625:00

cool way to interact with these tools. I

## 14625:00 - 14670:00

use Aqua, a YC company, and basically I

## 14670:00 - 14720:00

can just talk at my computer and Aqua

## 14720:00 - 14765:00

transcribes whatever I'm saying into the

## 14765:00 - 14800:00

tool I'm using. I'm switching a lot

## 14800:00 - 14825:00

between Windinsurf and Clawude Code at

## 14825:00 - 14865:00

the moment, but with Aqua, I can

## 14865:00 - 14910:00

effectively input instructions at 140

## 14910:00 - 14945:00

words per minute, which is about double

## 14945:00 - 14975:00

what I can type. And the AI is so

## 14975:00 - 15005:00

tolerant of minor grammar and

## 15005:00 - 15035:00

punctuation mistakes that it honestly

## 15035:00 - 15070:00

doesn't matter if the transcription's

## 15070:00 - 15100:00

not perfect. I actually wrote this

## 15100:00 - 15150:00

entire talk with Aqua. Next, make sure

## 15150:00 - 15190:00

to refactor frequently. When you've got

## 15190:00 - 15230:00

the code working and crucially the tests

## 15230:00 - 15270:00

implemented, you can refactor at will,

## 15270:00 - 15290:00

knowing that your tests are going to

## 15290:00 - 15325:00

catch any regressions. You can even ask

## 15325:00 - 15360:00

the LLM to identify parts of your

## 15360:00 - 15390:00

codebase that seem repetitive or might

## 15390:00 - 15425:00

be good candidates for refactoring. And

## 15425:00 - 15460:00

again, this is just a tip that any

## 15460:00 - 15490:00

professional software developer would

## 15490:00 - 15540:00

follow. You don't have um files that are

## 15540:00 - 15565:00

thousands of lines long. You keep them

## 15565:00 - 15590:00

small and modular. It makes it much

## 15590:00 - 15630:00

easier for both humans and LLMs to

## 15630:00 - 15660:00

understand what's going on. Finally,

## 15660:00 - 15700:00

keep experimenting. It seems like the

## 15700:00 - 15735:00

state-of-the-art of this stuff changes

## 15735:00 - 15780:00

week by week. I try every new model

## 15780:00 - 15810:00

release to see which performs better in

## 15810:00 - 15840:00

each different scenario. Some are better

## 15840:00 - 15880:00

at debugging or long-term planning or

## 15880:00 - 15915:00

implementing features or refactoring.

## 15915:00 - 15950:00

For example, at the moment, Gemini seems

## 15950:00 - 15985:00

best for whole codebase indexing and

## 15985:00 - 16015:00

coming up with implementation plans,

## 16015:00 - 16065:00

while Sonet 3.7, to me at least, seems

## 16065:00 - 16090:00

like the leading contender to actually

## 16090:00 - 16130:00

implement the code changes. I tried GPT

## 16130:00 - 16165:00

4.1 just a couple of days ago, and

## 16165:00 - 16195:00

honestly, I I wasn't yet as impressed.

## 16195:00 - 16225:00

It just came back with me with too many

## 16225:00 - 16255:00

questions and actually got the

## 16255:00 - 16290:00

implementation wrong too many times. But

## 16290:00 - 16330:00

I'll try it again next week and I'm sure

## 16330:00 - 16365:00

things will have changed again. Thanks

## 16365:00 - 16405:00

for watching and I'd love it if you have

## 16405:00 - 16430:00

tips or tricks for getting the most out

## 16430:00 - 16460:00

of these models. Please share them in

## 16460:00 - 16515:00

the comments below.

## 16515:00+

[Music]

