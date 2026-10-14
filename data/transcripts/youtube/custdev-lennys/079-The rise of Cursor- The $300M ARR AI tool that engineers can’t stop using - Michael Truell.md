---
source: https://www.youtube.com/watch?v=En5cSXgGvZM
title: "The rise of Cursor: The $300M ARR AI tool that engineers can’t stop
  using | Michael Truell"
author: Lenny's Podcast
date: 2025-05-01
views: 123657
description: >-
  *Michael Truell* is the co-founder and CEO of Anysphere, the company behind
  Cursor—the fastest-growing AI code editor in the world, reaching $300 million
  in annual recurring revenue just two years after its launch. In this
  conversation, Michael shares his vision for the future, lessons learned, and
  advice for preparing for the fast-approaching AI future.


  *What you’ll learn:*

  1. Cursor's early pivot from automating CAD to automating code

  2. Michael’s vision for “what comes after code” and how programming will
  evolve

  3. Why Cursor built their own custom AI models despite not starting there

  4. Key lessons from Cursor’s rapid growth

  5. Why “taste” and logic design will become more valuable engineering skills
  than technical coding ability

  6. Why the market for AI coding tools is much larger than people realize—and
  why there will likely be one dominant winner

  7. Michael’s advice for engineers and product teams preparing for the AI
  future


  *Transcript:*
  https://www.lennysnewsletter.com/p/the-rise-of-cursor-michael-truell


  *Brought to you by:*

  Eppo—Run reliable, impactful experiments: https://www.geteppo.com/

  Vanta—Automate compliance. Simplify security: https://vanta.com/lenny

  OneSchema—Import CSV data 10x faster: https://oneschema.co/lenny


  *Where to find Michael Truell:*

  • X: https://x.com/mntruell

  • LinkedIn: https://www.linkedin.com/in/michael-t-5b1bbb122/

  • Website: https://mntruell.com/


  *In this episode, we cover:*

  (00:00) Introduction to Michael Truell and Cursor

  (04:20) What comes after code

  (08:32) The importance of taste

  (12:39) Cursor’s origin story

  (18:31) Why they chose to build an IDE

  (22:39) Will everyone become engineering managers?

  (24:31) How they decided it was time to ship

  (26:45) Reflecting on Cursor's success

  (32:03) Counterintuitive lessons on building AI products

  (34:02) Inside Cursor's stack

  (38:42) Defensibility and market dynamics in AI

  (46:13) Tips for using Cursor

  (51:25) Hiring and building a strong team

  (59:10) Staying focused amid rapid AI advancements

  (01:02:31) Final thoughts and advice for aspiring AI innovators


  *Referenced:*

  • Cursor: https://www.cursor.com/

  • Microsoft Copilot: https://copilot.microsoft.com/

  • Scaling laws for neural language models:
  https://openai.com/index/scaling-laws-for-neural-language-models/

  • MIT: https://www.mit.edu/

  • Telegram: https://telegram.org/

  • Signal: https://signal.org/

  • WhatsApp: https://www.whatsapp.com/

  • Devin: https://devin.ai/

  • Visual Studio Code: https://code.visualstudio.com/

  • Chromium: https://chromium.googlesource.com/chromium/src/base/

  • Exploring ChatGPT (GPT) Wrappers—What They Are and How They Work:
  https://learnprompting.org/blog/gpt_wrappers

  • OpenAI’s CPO on how AI changes must-have skills, moats, coding, startup
  playbooks, more | Kevin Weil (CPO at OpenAI, ex-Instagram, Twitter):
  https://www.lennysnewsletter.com/p/kevin-weil-open-ai

  • Behind the founder: Marc Benioff:
  https://www.lennysnewsletter.com/p/behind-the-founder-marc-benioff

  • DALL-E 3: https://openai.com/index/dall-e-3/

  • Stable Diffusion 3: https://stability.ai/news/stable-diffusion-3


  _Production and marketing by https://penname.co/._

  _For inquiries about sponsoring the podcast, email
  podcast@lennyrachitsky.com._


  Lenny may be an investor in the companies discussed.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:46:03.247Z
---

# The rise of Cursor: The $300M ARR AI tool that engineers can’t stop using | Michael Truell

## 00:00 - 50:00

Our goal with cursor is to invent a new

## 50:00 - 70:00

type of programming, a very different

## 70:00 - 100:00

way to build software. So a world kind

## 100:00 - 140:00

of after code. I think that more and

## 140:00 - 170:00

more being an engineer will start to

## 170:00 - 205:00

feel like being a logic designer and

## 205:00 - 230:00

really it will be about specifying your

## 230:00 - 255:00

intent for how exactly you want

## 255:00 - 285:00

everything to work. What is the most

## 285:00 - 310:00

counterintuitive thing you've learned so

## 310:00 - 340:00

far about building cursor? We definitely

## 340:00 - 365:00

didn't expect to be doing any of our own

## 365:00 - 385:00

model development. And at this point,

## 385:00 - 425:00

every magic moment in Kurser involves a

## 425:00 - 450:00

custom model in some way. What's

## 450:00 - 480:00

something that you wish you knew before

## 480:00 - 510:00

you got into this role? Many people you

## 510:00 - 555:00

hear hired too fast. I think we actually

## 555:00 - 595:00

hired too slow to begin with. You guys

## 595:00 - 650:00

went from $0 to 100 million ARR in a

## 650:00 - 675:00

year and a half, which is historic. Was

## 675:00 - 700:00

there an inflection point where things

## 700:00 - 720:00

just started to really take off? The

## 720:00 - 760:00

growth has been fairly just consistent

## 760:00 - 785:00

on an exponential. An exponential to

## 785:00 - 810:00

begin with feels fairly slow and the

## 810:00 - 830:00

numbers are really low and it didn't

## 830:00 - 855:00

really feel off to the races to begin

## 855:00 - 875:00

with. What do you think is the secret to

## 875:00 - 925:00

your success? I think it's been

## 925:00 - 965:00

Today my guest is Michael Tru. Michael

## 965:00 - 1010:00

is co-founder and CEO of Any Sphere, the

## 1010:00 - 1045:00

company behind Cursor. If you've been

## 1045:00 - 1075:00

living under rock and haven't heard of

## 1075:00 - 1115:00

Cursor, it is the leading AI code editor

## 1115:00 - 1145:00

and is at the very forefront of changing

## 1145:00 - 1175:00

how engineers and product teams build

## 1175:00 - 1215:00

software. It's also one of the fastest

## 1215:00 - 1250:00

growing products of all time, hitting

## 1250:00 - 1300:00

100 million ARR just 20 months after

## 1300:00 - 1350:00

launching and then 300 million ARR just

## 1350:00 - 1390:00

2 years since launch. Michael's been

## 1390:00 - 1425:00

working on AI for 10 years. He studied

## 1425:00 - 1465:00

computer science and math at MIT, did AI

## 1465:00 - 1500:00

research at MIT and Google, and is a

## 1500:00 - 1535:00

student of tech and business history. As

## 1535:00 - 1565:00

you'll soon see, Michael thinks deeply

## 1565:00 - 1590:00

about where things are heading, and what

## 1590:00 - 1615:00

the future of building software looks

## 1615:00 - 1650:00

like. We chat about the origin story of

## 1650:00 - 1690:00

Cursor, his prediction of what happens

## 1690:00 - 1730:00

after code, his biggest counterintuitive

## 1730:00 - 1765:00

lessons from building Cursor, where he

## 1765:00 - 1785:00

sees things going for software

## 1785:00 - 1825:00

engineers, and so much more. Michael

## 1825:00 - 1860:00

does not do many podcasts. The only

## 1860:00 - 1890:00

other podcast he's ever done is Lex

## 1890:00 - 1925:00

Freedman. So, it was a true honor to

## 1925:00 - 1950:00

have Michael on. If you enjoy this

## 1950:00 - 1975:00

podcast, don't forget to subscribe and

## 1975:00 - 2000:00

follow it in your favorite podcasting

## 2000:00 - 2030:00

app or YouTube. Also, if you become an

## 2030:00 - 2065:00

annual subscriber of my newsletter, you

## 2065:00 - 2105:00

get a year free of Perplexity, Linear,

## 2105:00 - 2135:00

Superhuman, Notion, and Granola. Check

## 2135:00 - 2165:00

it out at lenny'snewsletter.com and

## 2165:00 - 2210:00

click bundle. With that, I bring you

## 2210:00 - 2255:00

Michael Troll. This episode is brought

## 2255:00 - 2305:00

to you by EPO. EPO is a next generation

## 2305:00 - 2335:00

AB testing and feature management

## 2335:00 - 2375:00

platform built by alums of Airbnb and

## 2375:00 - 2415:00

Snowflake for modern growth teams.

## 2415:00 - 2455:00

Companies like Twitch, Miro, ClickUp,

## 2455:00 - 2490:00

and DraftKings rely on EPO to power

## 2490:00 - 2535:00

their experiments. Experimentation is

## 2535:00 - 2560:00

increasingly essential for driving

## 2560:00 - 2590:00

growth and for understanding the

## 2590:00 - 2625:00

performance of new features. And EPO

## 2625:00 - 2650:00

helps you increase experimentation

## 2650:00 - 2690:00

velocity while unlocking rigorous deep

## 2690:00 - 2715:00

analysis in a way that no other

## 2715:00 - 2745:00

commercial tool does. When I was at

## 2745:00 - 2775:00

Airbnb, one of the things that I loved

## 2775:00 - 2810:00

most was our experimentation platform

## 2810:00 - 2845:00

where I could set up experiments easily,

## 2845:00 - 2875:00

troubleshoot issues, and analyze

## 2875:00 - 2910:00

performance all on my own. EPO does all

## 2910:00 - 2945:00

that and more with advanced statistical

## 2945:00 - 2975:00

methods that can help you shave weeks

## 2975:00 - 3010:00

off experiment time and accessible UI

## 3010:00 - 3045:00

for diving deeper into performance and

## 3045:00 - 3075:00

out- of-the-box reporting that helps you

## 3075:00 - 3110:00

avoid annoying prolonged analytic

## 3110:00 - 3150:00

cycles. EPO also makes it easy for you

## 3150:00 - 3175:00

to share experiment insights with your

## 3175:00 - 3210:00

team, sparking new ideas for the AB

## 3210:00 - 3245:00

testing flywheel. EPO powers

## 3245:00 - 3285:00

experimentation across every use case,

## 3285:00 - 3320:00

including product growth, machine

## 3320:00 - 3350:00

learning, monetization, and email

## 3350:00 - 3405:00

marketing. Check out EPO at

## 3405:00 - 3445:00

geto.com/lenny and 10x your experiment

## 3445:00 - 3515:00

velocity. That's get

## 3515:00 - 3545:00

epo.com/lenny. This episode is brought

## 3545:00 - 3585:00

to you by Vanta. When it comes to

## 3585:00 - 3620:00

ensuring your company has top-notch

## 3620:00 - 3655:00

security practices, things get

## 3655:00 - 3705:00

complicated fast. Now you can assess

## 3705:00 - 3735:00

risk, secure the trust of your

## 3735:00 - 3770:00

customers, and automate compliance for

## 3770:00 - 3805:00

SOCK 2, ISO

## 3805:00 - 3850:00

27,01, HIPPA, and more with a single

## 3850:00 - 3905:00

platform, Vanta. Vanta's market leading

## 3905:00 - 3940:00

trust management platform helps you

## 3940:00 - 3970:00

continuously monitor compliance

## 3970:00 - 4015:00

alongside reporting and tracking risk.

## 4015:00 - 4055:00

Plus, you can save hours by completing

## 4055:00 - 4100:00

security questionnaires with Vanta AI.

## 4100:00 - 4135:00

Join thousands of global companies that

## 4135:00 - 4165:00

use Vanta to automate evidence

## 4165:00 - 4205:00

collection, unify risk management, and

## 4205:00 - 4265:00

streamline security reviews. Get $1,000

## 4265:00 - 4310:00

off Vanta when you go to

## 4310:00 - 4425:00

vanta.com/lenny. That's

## 4425:00 - 4460:00

venta.com/lenny. Michael, thank you so

## 4460:00 - 4490:00

much for being here. Welcome to the

## 4490:00 - 4530:00

podcast. Thank you. Uh it's great to be

## 4530:00 - 4555:00

here. Thank you for having me. When we

## 4555:00 - 4580:00

were chatting earlier, you had this

## 4580:00 - 4605:00

really interesting phrase, this idea of

## 4605:00 - 4630:00

what comes after

## 4630:00 - 4670:00

code. Talk about that just like the

## 4670:00 - 4690:00

vision you have of where you think

## 4690:00 - 4730:00

things are going in terms of moving from

## 4730:00 - 4765:00

code to maybe something else. Our our

## 4765:00 - 4825:00

goal with Kerser is to invent sort of a

## 4825:00 - 4860:00

a new type of programming. um a very

## 4860:00 - 4895:00

different way to build software that's

## 4895:00 - 4935:00

kind of just distilled down into you

## 4935:00 - 4975:00

describing the intent to the computer

## 4975:00 - 5005:00

for what you want in the most concise

## 5005:00 - 5045:00

way possible. Uh and really distilled

## 5045:00 - 5075:00

down to you just defining how you think

## 5075:00 - 5100:00

the software should work and how you

## 5100:00 - 5145:00

think it should look. And yeah, with

## 5145:00 - 5170:00

with you know the technology that we we

## 5170:00 - 5200:00

have today and as it matures it uh we

## 5200:00 - 5225:00

think you can get to a place where you

## 5225:00 - 5250:00

can invent a method of building software

## 5250:00 - 5290:00

that's legions higher level and more

## 5290:00 - 5330:00

productive uh in some cases more more

## 5330:00 - 5405:00

accessible too and um that that process

## 5405:00 - 5450:00

will be will be a gradual moving away

## 5450:00 - 5480:00

from you know what building software

## 5480:00 - 5555:00

looks like today. Um and um I you know I

## 5555:00 - 5590:00

want to contrast it with maybe like the

## 5590:00 - 5620:00

vision of you know what software looks

## 5620:00 - 5660:00

like in the future. Um that you know I

## 5660:00 - 5680:00

think you know a couple visions that are

## 5680:00 - 5705:00

in the popular conscious that we at

## 5705:00 - 5765:00

least um have some disagreement with. Um

## 5765:00 - 5790:00

one is you know there's a group of

## 5790:00 - 5825:00

people who think that um you know

## 5825:00 - 5845:00

software building in the future is going

## 5845:00 - 5870:00

to look very much like it it does today

## 5870:00 - 5900:00

which mostly means text editing formal

## 5900:00 - 5920:00

programming languages like TypeScript

## 5920:00 - 5955:00

and Go and C and Rust. Uh, and then

## 5955:00 - 5975:00

there's another group that kind of

## 5975:00 - 5995:00

thinks like, you know, you're just going

## 5995:00 - 6040:00

to type into a bot and you're going to

## 6040:00 - 6065:00

ask it to build you something and then

## 6065:00 - 6090:00

you're going to ask it to to change

## 6090:00 - 6110:00

something about what you're building.

## 6110:00 - 6125:00

And it's kind of like this, you know,

## 6125:00 - 6150:00

chatbot Slackbot style where you're

## 6150:00 - 6180:00

talking to your engineering department.

## 6180:00 - 6210:00

And we think that there are problems

## 6210:00 - 6240:00

with with both of those

## 6240:00 - 6285:00

visions. I think that on the, you know,

## 6285:00 - 6320:00

on the the chatbot style end of things,

## 6320:00 - 6345:00

um, and we think it's going to look like

## 6345:00 - 6400:00

weirder than both. Um the problem with

## 6400:00 - 6450:00

the the chatbot style end of things is

## 6450:00 - 6490:00

um that lacks a lot of precision. If you

## 6490:00 - 6515:00

want humans to have completely, you

## 6515:00 - 6545:00

know, complete control over what the

## 6545:00 - 6580:00

software looks like and how it works,

## 6580:00 - 6605:00

you need to let them, you know, gesture

## 6605:00 - 6665:00

at what they want to be changed. Um you

## 6665:00 - 6690:00

know, in a form factor that's more

## 6690:00 - 6720:00

precise than just, you know, change this

## 6720:00 - 6745:00

about my app, you know, kind of in a

## 6745:00 - 6775:00

text box removed from the whole thing.

## 6775:00 - 6810:00

And then, um you know, the the version

## 6810:00 - 6830:00

of the world where kind of nothing

## 6830:00 - 6860:00

changes, we think we think is is wrong.

## 6860:00 - 6880:00

So we think that the the technology is

## 6880:00 - 6905:00

going to get much much much better. uh

## 6905:00 - 6945:00

and so a world you know kind of after

## 6945:00 - 6990:00

you know after code um I think it looks

## 6990:00 - 7015:00

like a world where you have a

## 7015:00 - 7050:00

representation of the logic of your

## 7050:00 - 7075:00

software that does look more like

## 7075:00 - 7100:00

English right you have kind of written

## 7100:00 - 7130:00

down you can imagine in doctrine form

## 7130:00 - 7150:00

you can imagine in kind of an evolution

## 7150:00 - 7180:00

of programming language towards pseudo

## 7180:00 - 7220:00

code you have written down you know the

## 7220:00 - 7245:00

logic of the software and you can you

## 7245:00 - 7265:00

can edit that at a high level and you

## 7265:00 - 7300:00

can point at that and it won't be kind

## 7300:00 - 7330:00

of the the impenetrable millions of

## 7330:00 - 7360:00

lines of code um it'll instead be

## 7360:00 - 7380:00

something that's like much turser and

## 7380:00 - 7395:00

easier to

## 7395:00 - 7445:00

to navigate. But that world where the

## 7445:00 - 7480:00

kind of crazy hard to

## 7480:00 - 7515:00

understand something that's a little bit

## 7515:00 - 7570:00

more human readable uh human editable uh

## 7570:00 - 7605:00

is one is one that we're working toward.

## 7605:00 - 7635:00

This is a profound point. I think I I

## 7635:00 - 7655:00

want to make sure people don't miss what

## 7655:00 - 7685:00

you're saying here, which is that what

## 7685:00 - 7710:00

you're envisioning in the next year

## 7710:00 - 7740:00

essentially is kind of when things start

## 7740:00 - 7780:00

to shift is uh people move away from

## 7780:00 - 7815:00

even seeing code think having to think

## 7815:00 - 7860:00

in code in like JavaScript and Python

## 7860:00 - 7895:00

and there's this abstraction that will

## 7895:00 - 7930:00

appear uh essentially pseudo code

## 7930:00 - 7955:00

describing what the code should be doing

## 7955:00 - 8000:00

more in English sentences. Yep. We we

## 8000:00 - 8025:00

think it ends up ends up looking like

## 8025:00 - 8065:00

that. Um, and we're very opinionated

## 8065:00 - 8090:00

that that path goes through kind of

## 8090:00 - 8125:00

existing professional engineers and it

## 8125:00 - 8150:00

looks like this this evolution away from

## 8150:00 - 8185:00

code. Uh, and it definitely looks like

## 8185:00 - 8205:00

the human still being in the driver's

## 8205:00 - 8250:00

seat, right? and the human having both a

## 8250:00 - 8285:00

ton of control over all aspects of the

## 8285:00 - 8320:00

software and not giving that up. And

## 8320:00 - 8360:00

then also uh the human having the the

## 8360:00 - 8405:00

ability to um make changes very quickly

## 8405:00 - 8430:00

like having a fast duration loop and not

## 8430:00 - 8480:00

just like you know having something in

## 8480:00 - 8505:00

the background that's that's super slow

## 8505:00 - 8540:00

and takes like weeks uh go do all your

## 8540:00 - 8600:00

work for you. This uh begs the question

## 8600:00 - 8630:00

for people that are getting are

## 8630:00 - 8650:00

currently engineers or thinking about

## 8650:00 - 8695:00

becoming engineers or designers or

## 8695:00 - 8720:00

product managers like what skills do you

## 8720:00 - 8765:00

think will be more more and more

## 8765:00 - 8820:00

valuable in this world of the what comes

## 8820:00 - 8870:00

after code? I think taste will be

## 8870:00 - 8915:00

increasingly more valuable and I think

## 8915:00 - 8945:00

often when people think about taste in

## 8945:00 - 8980:00

the realm of software they think about

## 8980:00 - 9025:00

you know visuals or taste over smooth

## 9025:00 - 9080:00

animations and uh you know coloring

## 9080:00 - 9125:00

things UI UX etc on kind of the visual

## 9125:00 - 9160:00

design of things and I think more and

## 9160:00 - 9185:00

more and you know the visual side of

## 9185:00 - 9225:00

things is an important part of defining

## 9225:00 - 9260:00

you know a piece of software but then as

## 9260:00 - 9285:00

mentioned before I think that the other

## 9285:00 - 9315:00

half of defining a piece of software is

## 9315:00 - 9365:00

is the logic of and how the thing works.

## 9365:00 - 9405:00

And we have amazing tools for specking

## 9405:00 - 9435:00

out the visuals of things. And then when

## 9435:00 - 9470:00

you get into the the logic of how a

## 9470:00 - 9515:00

piece of software works really the best

## 9515:00 - 9540:00

representation we have of that is code

## 9540:00 - 9570:00

right now. You can kind of gesture at it

## 9570:00 - 9590:00

with Figma and you can gesture at it

## 9590:00 - 9625:00

with writing down notes. Um but it's you

## 9625:00 - 9645:00

know when you have an actual working

## 9645:00 - 9685:00

prototype and so I think that more and

## 9685:00 - 9725:00

more being being an engineer will start

## 9725:00 - 9770:00

to feel like being a logic designer. And

## 9770:00 - 9800:00

really it will be about specifying your

## 9800:00 - 9825:00

intent for how exactly you want

## 9825:00 - 9855:00

everything to work. And it will less be

## 9855:00 - 9900:00

about it be more more about the the what

## 9900:00 - 9935:00

and a little bit less about the how um

## 9935:00 - 9955:00

exactly you're going to do things under

## 9955:00 - 9990:00

the hood. Uh and so yeah, I think I

## 9990:00 - 10010:00

think taste will be increasingly

## 10010:00 - 10045:00

important. I think one aspect of

## 10045:00 - 10070:00

software engineering and we're very far

## 10070:00 - 10090:00

from this right now and there are lots

## 10090:00 - 10130:00

of you know uh funny funny memes going

## 10130:00 - 10150:00

around the internet about you know the

## 10150:00 - 10170:00

kind of some of the trials and

## 10170:00 - 10195:00

tribulations people can run into if they

## 10195:00 - 10215:00

trust AI for too many things when it

## 10215:00 - 10265:00

comes to engineering um around you know

## 10265:00 - 10310:00

uh building building apps that uh you

## 10310:00 - 10330:00

know have have glaring glaring

## 10330:00 - 10365:00

deficiencies and and problems and

## 10365:00 - 10405:00

functionality issues but um I think we

## 10405:00 - 10455:00

will get to a place where um you will be

## 10455:00 - 10505:00

able to uh be less careful as a software

## 10505:00 - 10530:00

engineer which right now is an

## 10530:00 - 10565:00

incredibly incredibly important uh

## 10565:00 - 10625:00

skill. Um, and yeah, we'll move a little

## 10625:00 - 10645:00

bit from carefulness and a little bit

## 10645:00 - 10695:00

more towards taste. And this uh makes me

## 10695:00 - 10715:00

think of vibe coding. Is that kind of

## 10715:00 - 10735:00

what you're describing when you talk

## 10735:00 - 10760:00

about not having to think about the

## 10760:00 - 10795:00

details as much and just kind of going

## 10795:00 - 10825:00

with the flow? I think it's I think it's

## 10825:00 - 10865:00

related. I think that v coding right now

## 10865:00 - 10920:00

describes um exactly kind of this this

## 10920:00 - 10980:00

state of creation that uh is pretty

## 10980:00 - 11005:00

controversial where you're generating a

## 11005:00 - 11020:00

lot of code and you aren't really

## 11020:00 - 11060:00

understanding the details. That is that

## 11060:00 - 11100:00

is like a a state of creation that then

## 11100:00 - 11130:00

has has lots of problems like you don't

## 11130:00 - 11170:00

really by by not understanding the

## 11170:00 - 11195:00

details under the hood right now. You

## 11195:00 - 11220:00

then very quickly get to a place where

## 11220:00 - 11245:00

you're kind of limited at a certain

## 11245:00 - 11265:00

point where you create something that's

## 11265:00 - 11290:00

big enough that that you can't change.

## 11290:00 - 11320:00

And so I think some of the some of the

## 11320:00 - 11340:00

you know ideas that we're interested

## 11340:00 - 11385:00

around you know how do you give people

## 11385:00 - 11415:00

uh continued control over all the

## 11415:00 - 11465:00

details um you know when they don't

## 11465:00 - 11490:00

really understand the code like I think

## 11490:00 - 11540:00

that um solutions there um are very

## 11540:00 - 11570:00

relevant to to the people who are buy

## 11570:00 - 11625:00

coding right now I you know I think that

## 11625:00 - 11660:00

uh right now we we kind of we lack the

## 11660:00 - 11695:00

ability to you know let the themakers

## 11695:00 - 11715:00

actually have complete control over the

## 11715:00 - 11765:00

software and so um one of the one of the

## 11765:00 - 11800:00

issues also with you with vibe coding

## 11800:00 - 11830:00

and and letting letting taste really

## 11830:00 - 11865:00

shine through from people is you can

## 11865:00 - 11890:00

create stuff, but a lot of it is the AI

## 11890:00 - 11915:00

making decisions that you are unwieldy

## 11915:00 - 11950:00

and you don't have control over. One

## 11950:00 - 11975:00

more question along these lines. You you

## 11975:00 - 12000:00

throw out this word taste. When you say

## 12000:00 - 12030:00

taste, what are you thinking? I'm

## 12030:00 - 12055:00

thinking having the right idea for for

## 12055:00 - 12090:00

what should be built. And then just it

## 12090:00 - 12120:00

it will become more and more about kind

## 12120:00 - 12150:00

of the effortless translation of here's

## 12150:00 - 12180:00

exactly what you want built. Here's how

## 12180:00 - 12200:00

you want everything to work. Here's how

## 12200:00 - 12225:00

you want it to look. And then you'll be

## 12225:00 - 12265:00

able to make that um on a computer and

## 12265:00 - 12290:00

it will less be about this kind of

## 12290:00 - 12325:00

translation layer of like you and your

## 12325:00 - 12350:00

team have a picture of what you'd want

## 12350:00 - 12395:00

to build and then you have to really

## 12395:00 - 12435:00

painstakingly labor intensive like lay

## 12435:00 - 12475:00

out that into a format that a computer

## 12475:00 - 12515:00

can then execute and interpret. And so

## 12515:00 - 12540:00

yeah, I think you know less is less on

## 12540:00 - 12575:00

the UI side of things. Maybe taste is a

## 12575:00 - 12610:00

little bit of a misnomer uh but just

## 12610:00 - 12635:00

about having the right idea for for what

## 12635:00 - 12675:00

should be built. Awesome. Okay, I'm

## 12675:00 - 12695:00

going to come back to these topics, but

## 12695:00 - 12735:00

I want to actually zoom us back out to

## 12735:00 - 12800:00

the beginnings of cursor. Uh, I've never

## 12800:00 - 12820:00

heard the origin story. I don't think

## 12820:00 - 12850:00

many people know how this whole thing

## 12850:00 - 12880:00

started. Basically, you guys are

## 12880:00 - 12905:00

building one of the fastest growing

## 12905:00 - 12935:00

products in the history of the world.

## 12935:00 - 12960:00

It's changing the way people build

## 12960:00 - 12985:00

products. It's changing careers,

## 12985:00 - 13020:00

professions. It's it's changing so much.

## 13020:00 - 13050:00

How did it all begin? Any memorable

## 13050:00 - 13070:00

moments along the journey of the early

## 13070:00 - 13115:00

days? Carer kind of started as a

## 13115:00 - 13170:00

solution search of a problem. um and uh

## 13170:00 - 13210:00

a little a little bit where it very much

## 13210:00 - 13270:00

came from reflecting on um how AI was

## 13270:00 - 13305:00

going to get better um over the course

## 13305:00 - 13365:00

of the next 10 years. And um there were

## 13365:00 - 13395:00

there were kind of two defining moments.

## 13395:00 - 13445:00

One was uh being really excited by using

## 13445:00 - 13485:00

the the the first beta version of the

## 13485:00 - 13530:00

Git Co-ilot. Actually this was the first

## 13530:00 - 13580:00

time we had used an AI product that was

## 13580:00 - 13630:00

really really really useful and um was

## 13630:00 - 13670:00

you know actually just useful at all uh

## 13670:00 - 13705:00

and wasn't just a vaporware kind of demo

## 13705:00 - 13750:00

thing and in addition to being an you

## 13750:00 - 13775:00

know the first AI product that we used

## 13775:00 - 13820:00

that was useful G copilo was also one of

## 13820:00 - 13855:00

the most useful if not the most useful

## 13855:00 - 13895:00

dev tool we' ever adopted

## 13895:00 - 13940:00

um and that got us really excited you

## 13940:00 - 13970:00

know another moment that got us really

## 13970:00 - 14005:00

excited was the series of scaling on

## 14005:00 - 14030:00

papers coming out of OpenAI and other

## 14030:00 - 14060:00

places that showed that even if we had

## 14060:00 - 14100:00

no new ideas, AI was going to get better

## 14100:00 - 14125:00

and better just by pulling on simple

## 14125:00 - 14155:00

levers like scaling up the models and

## 14155:00 - 14185:00

also scaling up the the data that was

## 14185:00 - 14225:00

going into the models. And so at the end

## 14225:00 - 14260:00

of 2021, beginning of 2022, this got us

## 14260:00 - 14290:00

excited about how you know AI products

## 14290:00 - 14315:00

were now possible. This technology was

## 14315:00 - 14365:00

going to mature uh into the future. And

## 14365:00 - 14400:00

it felt like when we looked around there

## 14400:00 - 14445:00

were lots of people talking about making

## 14445:00 - 14500:00

models and there it felt like people

## 14500:00 - 14530:00

weren't really picking an area of

## 14530:00 - 14555:00

knowledge work and thinking about what

## 14555:00 - 14585:00

it was going to look like as AI got

## 14585:00 - 14630:00

better and better and um you know that

## 14630:00 - 14665:00

set us on the the path to like an you

## 14665:00 - 14685:00

know kind of an idea generation

## 14685:00 - 14720:00

exercise. It was like you know how are

## 14720:00 - 14755:00

each these areas of knowledge work uh

## 14755:00 - 14780:00

going to change in the future as this

## 14780:00 - 14810:00

tech gets more mature. Like what is the

## 14810:00 - 14835:00

you know end state of the work going to

## 14835:00 - 14875:00

look like? Um how are the the tools that

## 14875:00 - 14905:00

we use to do that work going to change?

## 14905:00 - 14935:00

Um how are the models going to get you

## 14935:00 - 14980:00

know need to get better to support uh

## 14980:00 - 15025:00

changes in the work? And you know once

## 15025:00 - 15055:00

scaling and pre-training ran out like

## 15055:00 - 15080:00

how are we going to keep pushing forward

## 15080:00 - 15100:00

technological

## 15100:00 - 15165:00

capabilities and the myth step at at the

## 15165:00 - 15190:00

beginning for sure is we actually worked

## 15190:00 - 15230:00

on you know we sort of did this whole

## 15230:00 - 15275:00

grand exercise uh and we decided to work

## 15275:00 - 15330:00

on you know uh an area uh of knowledge

## 15330:00 - 15350:00

work that we thought would be relatively

## 15350:00 - 15395:00

uncompetitive and sleepy and and boring

## 15395:00 - 15415:00

uh and you know no one no one would be

## 15415:00 - 15435:00

looking at it because you know we

## 15435:00 - 15460:00

thought oh coding's great you know

## 15460:00 - 15480:00

coding is totally interchangeable

## 15480:00 - 15505:00

because AI but you people are already

## 15505:00 - 15550:00

doing that. And uh so there was a period

## 15550:00 - 15590:00

of you know four months to begin with

## 15590:00 - 15615:00

where we were actually working on a very

## 15615:00 - 15660:00

different idea which was helping to

## 15660:00 - 15685:00

automate and augment mechanical

## 15685:00 - 15715:00

engineering uh and building tools for

## 15715:00 - 15745:00

mechanical engineers. You know there

## 15745:00 - 15780:00

were problems from the get-go in that we

## 15780:00 - 15815:00

had uh you know me and my co-founders we

## 15815:00 - 15865:00

we weren't mechanical engineers. Um you

## 15865:00 - 15885:00

know we had friends who were mechanical

## 15885:00 - 15915:00

engineers but uh we were we were very

## 15915:00 - 15940:00

much unfamiliar with the field. So

## 15940:00 - 15965:00

there's a little bit of a blind man in

## 15965:00 - 16005:00

the elephant problem from the get-go. Uh

## 16005:00 - 16035:00

you know there were problems around you

## 16035:00 - 16060:00

know how would you actually take take

## 16060:00 - 16080:00

the models that exist today and make

## 16080:00 - 16105:00

them useful for mechanical engineering.

## 16105:00 - 16130:00

The way we net it out is you need to

## 16130:00 - 16150:00

actually develop your own models from

## 16150:00 - 16215:00

the get- go and the way we did that was

## 16215:00 - 16250:00

uh was tricky and you know there's not a

## 16250:00 - 16320:00

lot of uh data on the internet of of um

## 16320:00 - 16360:00

you know 3D models of uh of different

## 16360:00 - 16385:00

tools and parts and the steps that I

## 16385:00 - 16415:00

took to build build up to those 3D

## 16415:00 - 16445:00

models. uh and then getting them from

## 16445:00 - 16475:00

the sources that that have them is like

## 16475:00 - 16515:00

also a tricky process too. But um

## 16515:00 - 16545:00

eventually what happened was you know we

## 16545:00 - 16580:00

we came to our senses we realized we're

## 16580:00 - 16600:00

not super excited about mechanical

## 16600:00 - 16635:00

engineering it's not the thing we want

## 16635:00 - 16665:00

to dedicate our lives to and we looked

## 16665:00 - 16700:00

around and uh in the area of programming

## 16700:00 - 16750:00

it felt like you know despite you know a

## 16750:00 - 16780:00

decent amount of time ensuing uh not

## 16780:00 - 16815:00

much had changed and it felt like the

## 16815:00 - 16845:00

people that were working on the space

## 16845:00 - 16875:00

maybe had a had a disconnect with us and

## 16875:00 - 16895:00

it felt like they weren't being

## 16895:00 - 16935:00

sufficiently ambitious about um where

## 16935:00 - 16955:00

everything was going to go in the future

## 16955:00 - 16985:00

and how kind of all of software creation

## 16985:00 - 17010:00

was going to blow through these models

## 17010:00 - 17035:00

uh and that's what set us off on the the

## 17035:00 - 17080:00

path to to building Kersia. Okay, so

## 17080:00 - 17100:00

interesting. Okay, so first of all, I

## 17100:00 - 17125:00

love that there's this this is advice

## 17125:00 - 17165:00

that you often hear of go after boring

## 17165:00 - 17180:00

industry because no one's going to be

## 17180:00 - 17220:00

there and there's opportunity and you

## 17220:00 - 17250:00

know sometimes it works but I love that

## 17250:00 - 17270:00

this journey it's like no actually go

## 17270:00 - 17320:00

after the hottest most uh popular space

## 17320:00 - 17370:00

AI coding app building and it worked out

## 17370:00 - 17405:00

and the way you phrased it just now is

## 17405:00 - 17430:00

you didn't see enough ambition

## 17430:00 - 17465:00

potentially that you thought there was

## 17465:00 - 17500:00

more to be done so it feels like that's

## 17500:00 - 17525:00

an interesting lesson if even if

## 17525:00 - 17555:00

something looks like okay it's too late

## 17555:00 - 17580:00

there's GitHub copilots out there are

## 17580:00 - 17620:00

some other products if you notice that

## 17620:00 - 17645:00

they're just not as ambitious as they

## 17645:00 - 17700:00

could be or as you are or you see almost

## 17700:00 - 17725:00

a flaw in their approach that there's

## 17725:00 - 17755:00

still a big opportunity. Does that

## 17755:00 - 17790:00

resonate? Uh that totally resonates and

## 17790:00 - 17810:00

I think it's

## 17810:00 - 17860:00

um a part of it is you need there to to

## 17860:00 - 17895:00

be like leaprogs that can happen. And

## 17895:00 - 17915:00

you need there to be things that you can

## 17915:00 - 17965:00

do. And I think the exciting thing about

## 17965:00 - 18000:00

about AI is in a in a bunch of places

## 18000:00 - 18030:00

and I think this is, you know, very much

## 18030:00 - 18065:00

still true of our space and you can talk

## 18065:00 - 18085:00

about how we think about that and how we

## 18085:00 - 18125:00

deal with that. But um, you know, I

## 18125:00 - 18145:00

think that just the ceiling is really

## 18145:00 - 18190:00

high and um, yes, if you if you look

## 18190:00 - 18230:00

around uh, you know, probably even if

## 18230:00 - 18260:00

you you take the best tool in kind of

## 18260:00 - 18295:00

like any of these any of these fields,

## 18295:00 - 18315:00

um, there should be a lot more that

## 18315:00 - 18330:00

needs to be done over the next few

## 18330:00 - 18365:00

years. And so that that space having

## 18365:00 - 18395:00

that space having that you know high

## 18395:00 - 18450:00

ceiling I think is is unique um amongst

## 18450:00 - 18475:00

areas of software at least the degree to

## 18475:00 - 18510:00

which it is it is high with AI. Let's

## 18510:00 - 18540:00

come back to the ID question. So there's

## 18540:00 - 18560:00

kind of a few routes you could have

## 18560:00 - 18580:00

taken and other companies are doing

## 18580:00 - 18610:00

different routes. So there's building an

## 18610:00 - 18640:00

ID for engineers to work within and

## 18640:00 - 18675:00

adding AI magic to it. There's another

## 18675:00 - 18725:00

route of just a full AI agentic devon

## 18725:00 - 18750:00

sort of product and then there's just

## 18750:00 - 18790:00

like a model that is very good at coding

## 18790:00 - 18810:00

and focusing on building the best

## 18810:00 - 18840:00

possible coding model. What made you

## 18840:00 - 18875:00

decide and see that the ID path was the

## 18875:00 - 18935:00

best route? The folks who were from the

## 18935:00 - 19010:00

get-go working on just a uh a model were

## 19010:00 - 19070:00

working on end to end uh automation

## 19070:00 - 19110:00

programming. I think

## 19110:00 - 19145:00

uh they were trying to build something

## 19145:00 - 19175:00

very different from us which is we care

## 19175:00 - 19220:00

about giving humans control over all the

## 19220:00 - 19260:00

decisions um in kind of the end tool

## 19260:00 - 19310:00

that they're building and I think those

## 19310:00 - 19340:00

folks were very much thinking of a of a

## 19340:00 - 19380:00

future where kind of you know end the

## 19380:00 - 19410:00

whole thing is done by AI and maybe like

## 19410:00 - 19445:00

the AI is making all the decisions too

## 19445:00 - 19465:00

and so one there was kind of like a

## 19465:00 - 19495:00

personal interest component two I think

## 19495:00 - 19550:00

that always we try to be intense realist

## 19550:00 - 19580:00

about where the technology is today, you

## 19580:00 - 19615:00

know, very very very excited about how

## 19615:00 - 19645:00

AI is going to mature over the course of

## 19645:00 - 19705:00

many decades. But, uh, you know, I think

## 19705:00 - 19755:00

that sometimes people, you know, there's

## 19755:00 - 19795:00

there's an instinct to to see AI do

## 19795:00 - 19825:00

magical things in one area and then kind

## 19825:00 - 19850:00

of anthropomorphize these models and

## 19850:00 - 19870:00

think, you know, it's better than a

## 19870:00 - 19895:00

smart person here and so must be better

## 19895:00 - 19920:00

than a smart person there. But these

## 19920:00 - 20005:00

things have massive issues. And um we uh

## 20005:00 - 20050:00

from the from the very start our our

## 20050:00 - 20075:00

product development process was really

## 20075:00 - 20110:00

about dog fooding and using the tool

## 20110:00 - 20160:00

intensely every day and we we never

## 20160:00 - 20180:00

wanted to ship anything that wasn't

## 20180:00 - 20220:00

wasn't useful to us. And you know we had

## 20220:00 - 20240:00

the benefit of doing that because we

## 20240:00 - 20285:00

were the end user part of our product.

## 20285:00 - 20315:00

And I think that that instills a realism

## 20315:00 - 20355:00

in you around where the where the tech

## 20355:00 - 20415:00

is right now. And so uh that definitely

## 20415:00 - 20440:00

made us think that we need the humans to

## 20440:00 - 20465:00

be in the driver's seat. The AI cannot

## 20465:00 - 20490:00

do everything. We're also interested in

## 20490:00 - 20525:00

giving humans that control too for for

## 20525:00 - 20560:00

personal reasons. And so that that gets

## 20560:00 - 20580:00

you away from just you're a model

## 20580:00 - 20605:00

company that also gets you away from

## 20605:00 - 20635:00

just kind of this endto-end stuff with

## 20635:00 - 20665:00

without the human having control. And

## 20665:00 - 20695:00

then the way you get through an IDE

## 20695:00 - 20720:00

versus maybe a plugin to an existing

## 20720:00 - 20770:00

coding environment is uh the belief that

## 20770:00 - 20795:00

you know programming is going to flow

## 20795:00 - 20820:00

through these models and the act of

## 20820:00 - 20845:00

programming is going to change a lot

## 20845:00 - 20875:00

over the course of the next few years

## 20875:00 - 20920:00

and that the extensibility that existing

## 20920:00 - 20950:00

coding environments have is so so so

## 20950:00 - 20980:00

limited. So if you think that the UI is

## 20980:00 - 21000:00

going to change a lot, if you think that

## 21000:00 - 21015:00

the form factor of programming is going

## 21015:00 - 21040:00

to change a lot, you necessarily need to

## 21040:00 - 21055:00

have control over the entire

## 21055:00 - 21085:00

application. I know that you guys today

## 21085:00 - 21145:00

have an IDE and uh and that's probably

## 21145:00 - 21175:00

the bias you have of this is maybe where

## 21175:00 - 21190:00

the future is heading, but I'm just

## 21190:00 - 21220:00

curious, do you think a big part of the

## 21220:00 - 21255:00

future is also going to be AI engineers

## 21255:00 - 21280:00

that are just sitting in Slack and just

## 21280:00 - 21305:00

doing things for you? Is that something

## 21305:00 - 21340:00

that fits into Cursor one day? I think

## 21340:00 - 21395:00

you'll want the ability to move between

## 21395:00 - 21435:00

all of these things fairly effortlessly.

## 21435:00 - 21485:00

And sometimes I think you will want to

## 21485:00 - 21515:00

have the thing kind of go spin off on

## 21515:00 - 21540:00

its own for a while and then I think

## 21540:00 - 21585:00

you'll want the ability to pull in the

## 21585:00 - 21615:00

AI's work and then work with it very

## 21615:00 - 21645:00

very very quickly, right? And then maybe

## 21645:00 - 21685:00

have it go spin off again. And so these

## 21685:00 - 21720:00

like kind of background versus

## 21720:00 - 21745:00

foreground form factors, I think you

## 21745:00 - 21790:00

want that all to work well in one place.

## 21790:00 - 21840:00

And uh I think the background stuff

## 21840:00 - 21865:00

there's like a segment of programming

## 21865:00 - 21900:00

that it's especially useful for which is

## 21900:00 - 21930:00

type of programming tasks where it's

## 21930:00 - 21975:00

very easy to specify exactly what you

## 21975:00 - 22030:00

want um with you know without much

## 22030:00 - 22060:00

description and exactly what correctness

## 22060:00 - 22085:00

looks like without much description and

## 22085:00 - 22120:00

often that's the bug fixes are kind of

## 22120:00 - 22160:00

like the are are a great example of that

## 22160:00 - 22180:00

but it's definitely not all of

## 22180:00 - 22220:00

programming. So I think that you know

## 22220:00 - 22260:00

what the IDE is will totally change over

## 22260:00 - 22285:00

time and kind of our approach to you

## 22285:00 - 22320:00

know having our own editor was premised

## 22320:00 - 22345:00

on it's going to have to evolve over

## 22345:00 - 22375:00

time and I think that that will both

## 22375:00 - 22405:00

include you can spin off things from

## 22405:00 - 22430:00

different surface areas like Slack or

## 22430:00 - 22460:00

your issue tracker or whatever it is and

## 22460:00 - 22485:00

I think that will also include like you

## 22485:00 - 22510:00

know the pane of glass that you're

## 22510:00 - 22555:00

staring at is going to change a lot. Um

## 22555:00 - 22590:00

and you know we just mostly think of an

## 22590:00 - 22625:00

ID as the place where you are building

## 22625:00 - 22660:00

software. I think something people don't

## 22660:00 - 22685:00

talk enough about with with talking

## 22685:00 - 22740:00

about agents and all these AI engineers

## 22740:00 - 22755:00

are going to be doing all stuff for you

## 22755:00 - 22780:00

is basically we're all becoming uh

## 22780:00 - 22825:00

engineering managers with a lot of

## 22825:00 - 22865:00

reports that are just like not that not

## 22865:00 - 22900:00

that smart and you have to do a lot of

## 22900:00 - 22935:00

reviewing and approving and specifying.

## 22935:00 - 22965:00

I guess thoughts on that and is there

## 22965:00 - 22980:00

anything you could do to make that

## 22980:00 - 23000:00

easier? Because that sounds really hard.

## 23000:00 - 23030:00

Like anyone that has a large team, has

## 23030:00 - 23055:00

had a large team being like, "Oh my god,

## 23055:00 - 23090:00

all these uh junior people just checking

## 23090:00 - 23105:00

in with me

## 23105:00 - 23145:00

doing not high quality work over and

## 23145:00 - 23170:00

over." It's just like, "What a life.

## 23170:00 - 23195:00

It's going to suck." Yeah. Maybe

## 23195:00 - 23250:00

eventually one-on- ones with uh

## 23250:00 - 23300:00

so many one-on- ones. Um uh yeah. So the

## 23300:00 - 23355:00

the customers we've seen have uh most

## 23355:00 - 23400:00

success with AI, I think are still

## 23400:00 - 23435:00

fairly conservative about some of the

## 23435:00 - 23475:00

ways in which in which they they use

## 23475:00 - 23520:00

this stuff. And so I do think today that

## 23520:00 - 23550:00

the most successful customers really

## 23550:00 - 23600:00

lean on things like um you know our next

## 23600:00 - 23635:00

edit prediction where we you know you're

## 23635:00 - 23665:00

coding as normal and predicting the next

## 23665:00 - 23690:00

actions you're going to do. And then

## 23690:00 - 23715:00

they also really lean on like scoping

## 23715:00 - 23740:00

down the stuff that you're going to hand

## 23740:00 - 23795:00

off uh to the bot. And you know there's

## 23795:00 - 23830:00

for a fixed percent of your time spent

## 23830:00 - 23880:00

reviewing code you could um from from an

## 23880:00 - 23930:00

agent um or from an AI overall you could

## 23930:00 - 23960:00

you know there's kind of two patterns

## 23960:00 - 23990:00

one is you could you know spend a bunch

## 23990:00 - 24025:00

of time specifying things up front the

## 24025:00 - 24065:00

AI goes and works and then you then go

## 24065:00 - 24100:00

and review the AI's work and then you're

## 24100:00 - 24130:00

done that's the whole task or you could

## 24130:00 - 24175:00

really chop things up right so you can

## 24175:00 - 24200:00

you know specify a little bit AI write

## 24200:00 - 24225:00

something review specify a little bit AI

## 24225:00 - 24250:00

write something review and that's kind

## 24250:00 - 24275:00

of you know autocompletes all in the way

## 24275:00 - 24345:00

of that spectrum and um still we see uh

## 24345:00 - 24385:00

often the most successful people um

## 24385:00 - 24420:00

using these tools are are are chopping

## 24420:00 - 24445:00

things up right now and keeping things

## 24445:00 - 24480:00

fairly that sounds less less terrible.

## 24480:00 - 24525:00

I'm I'm glad there's a solution here. I

## 24525:00 - 24555:00

want to go back to you guys building

## 24555:00 - 24595:00

cursor for the first time. What was the

## 24595:00 - 24625:00

point where you realized this is ready?

## 24625:00 - 24650:00

What was kind of a moment of like okay I

## 24650:00 - 24670:00

think this is time to put it out there

## 24670:00 - 24710:00

and see what happens. So when we started

## 24710:00 - 24780:00

building cursor um we were fairly

## 24780:00 - 24810:00

paranoid about spinning for a while

## 24810:00 - 24860:00

without releasing to the world. And so

## 24860:00 - 24905:00

to to begin with too we actually the the

## 24905:00 - 24935:00

first version of kers was was hand

## 24935:00 - 25010:00

rolled. We uh now we we use uh VS code

## 25010:00 - 25040:00

kind of as a base like many browsers use

## 25040:00 - 25080:00

chromium as a base um and had for worked

## 25080:00 - 25110:00

off of that. uh to begin with we we

## 25110:00 - 25150:00

didn't and built a prototype of cursor

## 25150:00 - 25205:00

from scratch and that involved a lot of

## 25205:00 - 25235:00

work. We had to build our own uh you

## 25235:00 - 25250:00

know there were a lot of things that go

## 25250:00 - 25285:00

into you know a modern code editor uh

## 25285:00 - 25340:00

including um you know support for many

## 25340:00 - 25375:00

different languages and um navigation

## 25375:00 - 25400:00

support for moving amongst the language

## 25400:00 - 25420:00

you know error tracking support for

## 25420:00 - 25460:00

things. there's, you know, things like,

## 25460:00 - 25485:00

you know, an integrated command line,

## 25485:00 - 25510:00

you know, the ability to use like remote

## 25510:00 - 25560:00

servers to uh to, you know, to the

## 25560:00 - 25585:00

ability to connect to remote servers to

## 25585:00 - 25620:00

to view and and run code. And so we kind

## 25620:00 - 25645:00

of just like went on this blitz of

## 25645:00 - 25675:00

building things incredibly quickly,

## 25675:00 - 25705:00

building kind of our own uh editor from

## 25705:00 - 25740:00

scratch and then also the AI components.

## 25740:00 - 25780:00

And um it was after like a couple of

## 25780:00 - 25830:00

months that we just you know uh it was

## 25830:00 - 25870:00

after maybe five weeks that we were

## 25870:00 - 25915:00

living on the editor full-time and you

## 25915:00 - 25945:00

know had thrown away our previous editor

## 25945:00 - 25980:00

uh and we're we're using new one and

## 25980:00 - 26005:00

then once it got to a point where we

## 26005:00 - 26050:00

found it a bit useful then we put it in

## 26050:00 - 26070:00

other people's hands and had this like

## 26070:00 - 26095:00

very short beta period and then we

## 26095:00 - 26130:00

launched out to the world within uh a

## 26130:00 - 26155:00

couple of months from the first line of

## 26155:00 - 26190:00

code. I I think it was probably probably

## 26190:00 - 26220:00

three months and it was definitely a

## 26220:00 - 26260:00

like you know let's let's just get this

## 26260:00 - 26285:00

out to people and build in public

## 26285:00 - 26310:00

quickly. The thing that took us by

## 26310:00 - 26330:00

surprise is we thought we would be

## 26330:00 - 26360:00

building for a couple hundred people for

## 26360:00 - 26400:00

a long time and you know from the get-

## 26400:00 - 26430:00

go there there was kind of an immediate

## 26430:00 - 26465:00

crush of interest and a lot of feedback

## 26465:00 - 26495:00

too. Uh and you know that was super

## 26495:00 - 26515:00

helpful. We learned from that and that's

## 26515:00 - 26540:00

actually you know why we switched to

## 26540:00 - 26580:00

being based off of VS Code instead of

## 26580:00 - 26615:00

just you know this headold thing. Uh a

## 26615:00 - 26640:00

lot of that was motivated by kind of the

## 26640:00 - 26685:00

initial user feedback and uh you know

## 26685:00 - 26710:00

and then have been iterating in in

## 26710:00 - 26755:00

public uh from there. I like how you

## 26755:00 - 26805:00

understated uh the the traction that you

## 26805:00 - 26855:00

got. Uh I think you guys went from zero

## 26855:00 - 26890:00

dollars to 100 million ARR in like a

## 26890:00 - 26920:00

year and a half or something like that

## 26920:00 - 26975:00

which is uh historic. What do you think

## 26975:00 - 27015:00

was the key to this to success of

## 27015:00 - 27040:00

something like this? He's talking about

## 27040:00 - 27065:00

docuing being a big part of it. Like you

## 27065:00 - 27115:00

build it in three months that's insane.

## 27115:00 - 27145:00

Uh what do you think was is the secret

## 27145:00 - 27185:00

to your success? The first version was

## 27185:00 - 27225:00

was not you know the three-month version

## 27225:00 - 27270:00

wasn't very good and so I think it's

## 27270:00 - 27325:00

been you know a sustained paranoia about

## 27325:00 - 27350:00

you know there are all of these ways in

## 27350:00 - 27375:00

which this this thing could get better.

## 27375:00 - 27420:00

You know the end goal is really to uh

## 27420:00 - 27450:00

invent a very new form of programming

## 27450:00 - 27475:00

that involves automating a lot of coding

## 27475:00 - 27540:00

as we know today. And um no matter you

## 27540:00 - 27565:00

know where we are with cursor it feels

## 27565:00 - 27590:00

like we're very very far away from that

## 27590:00 - 27610:00

end goal. And so there's u there's

## 27610:00 - 27645:00

always a lot to do but I think it's been

## 27645:00 - 27685:00

kind of uh a lot of it hasn't been over

## 27685:00 - 27720:00

rotated on kind of that initial push but

## 27720:00 - 27745:00

instead is like the continued evolution

## 27745:00 - 27765:00

of the tool and just making the tool

## 27765:00 - 27795:00

consistently better. Was there an

## 27795:00 - 27820:00

inflection point after those three

## 27820:00 - 27835:00

months where things just started to

## 27835:00 - 27870:00

really take off? To be honest it felt

## 27870:00 - 27930:00

fairly slow to begin with. Um and you

## 27930:00 - 27960:00

know maybe maybe comes from some

## 27960:00 - 28025:00

impatience on our part. Um but uh one

## 28025:00 - 28060:00

what I think you know there's the the

## 28060:00 - 28110:00

overall speed of the growth which is um

## 28110:00 - 28135:00

uh you know continues to take us by

## 28135:00 - 28170:00

surprise. I think one of the things that

## 28170:00 - 28200:00

uh has been most surprising too is that

## 28200:00 - 28235:00

the growth has been fairly just

## 28235:00 - 28280:00

consistent on an exponential of just

## 28280:00 - 28310:00

consistent month- over-month growth

## 28310:00 - 28360:00

accelerated at times by um launches on

## 28360:00 - 28405:00

our part and other things. But uh you

## 28405:00 - 28435:00

know but an exponential to begin with

## 28435:00 - 28465:00

feels feels fairly slow when the the

## 28465:00 - 28500:00

numbers are really low and uh so it

## 28500:00 - 28520:00

didn't it didn't really feel off to the

## 28520:00 - 28550:00

races to begin with. To me this sounds

## 28550:00 - 28570:00

like build it and they will come

## 28570:00 - 28595:00

actually working. You guys just built an

## 28595:00 - 28620:00

awesome product that you loved

## 28620:00 - 28660:00

yourselves as engineers. You put it out.

## 28660:00 - 28700:00

People just loved it, told everyone

## 28700:00 - 28745:00

about it. it it being essentially all

## 28745:00 - 28800:00

just us you know the the team working on

## 28800:00 - 28825:00

the product and making the product good

## 28825:00 - 28860:00

in lie of you know other things one

## 28860:00 - 28895:00

could spend one's time on you know we we

## 28895:00 - 28925:00

definitely spent time on tons of other

## 28925:00 - 28945:00

things for instance building the team

## 28945:00 - 29010:00

was incredibly important and you know

## 29010:00 - 29045:00

uh doing things like uh you know support

## 29045:00 - 29090:00

rotations very important but some of the

## 29090:00 - 29125:00

normal things that people maybe reach

## 29125:00 - 29165:00

for uh and in building the company early

## 29165:00 - 29205:00

on um we really let those fires ear for

## 29205:00 - 29225:00

a long time especially when it came to

## 29225:00 - 29260:00

things like like sales and marketing and

## 29260:00 - 29290:00

so just working on the product and

## 29290:00 - 29325:00

building a product that you like your

## 29325:00 - 29350:00

team likes and then you know also then

## 29350:00 - 29380:00

adjusting it for some set of users that

## 29380:00 - 29420:00

can kind of sound simple but then you

## 29420:00 - 29465:00

know it's hard to do that well and uh

## 29465:00 - 29475:00

there are a bunch of different

## 29475:00 - 29500:00

directions one could have run in a bunch

## 29500:00 - 29540:00

of different product directions and I

## 29540:00 - 29565:00

think that um you know one of the

## 29565:00 - 29620:00

difficult things you know I think focus

## 29620:00 - 29645:00

and kind of strategically picking the

## 29645:00 - 29680:00

right things to build and prioritizing

## 29680:00 - 29710:00

effectively is tricky I think another

## 29710:00 - 29750:00

thing that's tricky about this um this

## 29750:00 - 29800:00

domain is it's kind of a new form of

## 29800:00 - 29850:00

product building where um it's very

## 29850:00 - 29890:00

intipary in that we are something in

## 29890:00 - 29935:00

between a normal software company uh and

## 29935:00 - 29965:00

then in between a normal software

## 29965:00 - 29990:00

company and then a foundation model

## 29990:00 - 30050:00

company in that um you know uh we want

## 30050:00 - 30080:00

to develop a you know we're developing a

## 30080:00 - 30120:00

product for millions of people and that

## 30120:00 - 30140:00

you know that side of things has to be

## 30140:00 - 30170:00

excellent. But then also one important

## 30170:00 - 30205:00

dimension of product quality is doing

## 30205:00 - 30230:00

more and more on the science and doing

## 30230:00 - 30250:00

more and more on the model side of

## 30250:00 - 30275:00

things uh in places where it makes

## 30275:00 - 30320:00

sense. And so that element of things

## 30320:00 - 30365:00

doing that well too has been tricky but

## 30365:00 - 30385:00

yeah you know the overall thing would

## 30385:00 - 30420:00

note is you know uh maybe you know some

## 30420:00 - 30450:00

of these things sound simple to specify

## 30450:00 - 30475:00

but then like doing them well is is hard

## 30475:00 - 30510:00

and there are rough ways you can run.

## 30510:00 - 30540:00

I'm excited to have Andrew Luo joining

## 30540:00 - 30590:00

us today. Andrew is CEO of OneKema, one

## 30590:00 - 30625:00

of our longtime podcast sponsors.

## 30625:00 - 30650:00

Welcome Andrew. Thanks for having me,

## 30650:00 - 30685:00

Lenny. Great to be here. So, what is new

## 30685:00 - 30715:00

with One Schema? I know that you work

## 30715:00 - 30745:00

with some of my favorite companies like

## 30745:00 - 30780:00

RAMP and Vanza and Watershed. I heard

## 30780:00 - 30810:00

you guys launched a new data intake

## 30810:00 - 30845:00

product that automates the hours of

## 30845:00 - 30875:00

manual work that teams spend importing

## 30875:00 - 30910:00

and mapping and integrating CSV and

## 30910:00 - 30950:00

Excel files. Yes. So, we just launched

## 30950:00 - 31000:00

the 2.0 of one schema file feeds. We've

## 31000:00 - 31040:00

rebuilt it from the ground up with AI.

## 31040:00 - 31075:00

We saw so many customers coming to us

## 31075:00 - 31105:00

with teams of data engineers that

## 31105:00 - 31135:00

struggled with the manual work required

## 31135:00 - 31175:00

to clean messy spreadsheets. File feeds

## 31175:00 - 31210:00

2.0 allows nontechnical teams to

## 31210:00 - 31250:00

automate the process of transforming CSV

## 31250:00 - 31280:00

and Excel files with just a simple

## 31280:00 - 31315:00

prompt. We support all of the trickiest

## 31315:00 - 31360:00

file integrations, SFTP, S3, and even

## 31360:00 - 31395:00

email. I can tell you that if my team

## 31395:00 - 31430:00

had to build integrations like this, how

## 31430:00 - 31460:00

nice would it be to take this off our

## 31460:00 - 31485:00

road map and instead use something like

## 31485:00 - 31525:00

one schema? Absolutely, Lenny. We've

## 31525:00 - 31560:00

heard so many horror stories of outages

## 31560:00 - 31595:00

from even just a single bad record in

## 31595:00 - 31630:00

transactions, employee files, purchase

## 31630:00 - 31665:00

orders, you name it. Debugging these

## 31665:00 - 31695:00

issues is often like finding a needle in

## 31695:00 - 31730:00

a haststack. One schema stops any bad

## 31730:00 - 31760:00

data from entering your system and

## 31760:00 - 31790:00

automatically validates your files,

## 31790:00 - 31820:00

generating error reports with the exact

## 31820:00 - 31855:00

issues in all bad files. I know that

## 31855:00 - 31885:00

importing incorrect data can cause all

## 31885:00 - 31910:00

kinds of pain for your customers and

## 31910:00 - 31945:00

quickly lose their trust. Andrew, thank

## 31945:00 - 31970:00

you so much for joining me. If you want

## 31970:00 - 31990:00

to learn more, head on over to

## 31990:00 - 32065:00

onskeema.co. co that's

## 32065:00 - 32105:00

oneskeema.co. What is the most

## 32105:00 - 32130:00

counterintuitive thing you've learned so

## 32130:00 - 32165:00

far about building cursor building AI

## 32165:00 - 32200:00

products? I I think one thing that's

## 32200:00 - 32230:00

been counterintuitive for us uh hinted

## 32230:00 - 32260:00

at at it a little bit

## 32260:00 - 32305:00

before, but is we we definitely didn't

## 32305:00 - 32330:00

expect to be doing any of our own model

## 32330:00 - 32365:00

development when we started. As

## 32365:00 - 32385:00

mentioned, you know, when we when we got

## 32385:00 - 32405:00

into this, there were companies that

## 32405:00 - 32435:00

were immediately from the get- go going

## 32435:00 - 32470:00

and just focusing on kind of training

## 32470:00 - 32530:00

model from scratch. And we had done the

## 32530:00 - 32565:00

calculation for what it took to to train

## 32565:00 - 32600:00

GP4 and just knew that that was not

## 32600:00 - 32610:00

going to be something we were going to

## 32610:00 - 32650:00

be able to do. And it also felt a little

## 32650:00 - 32690:00

bit like uh focusing one's attention in

## 32690:00 - 32735:00

the wrong area because there are lots of

## 32735:00 - 32760:00

amazing models out there. and why I do

## 32760:00 - 32790:00

all this work to replicate kind of what

## 32790:00 - 32820:00

other players had done especially on the

## 32820:00 - 32845:00

pre-training side of things you know

## 32845:00 - 32885:00

taking a a neural network that knows

## 32885:00 - 32915:00

nothing and then teaching it the whole

## 32915:00 - 32960:00

internet and uh so we thought we were we

## 32960:00 - 32990:00

weren't going to be doing that at all

## 32990:00 - 33030:00

and it seemed clear to us from the start

## 33030:00 - 33055:00

that the the existing models there were

## 33055:00 - 33080:00

lots of things that they could be doing

## 33080:00 - 33110:00

for us that um they weren't doing

## 33110:00 - 33130:00

because you know there wasn't the right

## 33130:00 - 33170:00

tool built for them in fact though we do

## 33170:00 - 33195:00

a ton of model development and

## 33195:00 - 33235:00

internally it's a it's a big um focus

## 33235:00 - 33275:00

for us in the hiring front uh and have

## 33275:00 - 33315:00

assembled a fantastic team there and

## 33315:00 - 33345:00

it's also been a big win on the the

## 33345:00 - 33370:00

product quality side of things for us.

## 33370:00 - 33410:00

Uh and at this point every magic moment

## 33410:00 - 33445:00

in Kerserv involves a custom model in

## 33445:00 - 33500:00

some way and uh so that that was

## 33500:00 - 33520:00

definitely counterintuitive and and

## 33520:00 - 33570:00

surprising and uh it's it's been a

## 33570:00 - 33595:00

gradual thing where you know there was

## 33595:00 - 33625:00

an initial use case for for training our

## 33625:00 - 33645:00

own model where it really didn't make

## 33645:00 - 33660:00

sense to use any of the biggest

## 33660:00 - 33685:00

foundation models that was incredibly

## 33685:00 - 33710:00

successful kind of moved to another use

## 33710:00 - 33760:00

case that worked really well. uh and has

## 33760:00 - 33800:00

have been going from there. And one of

## 33800:00 - 33840:00

the you know that the helpful things in

## 33840:00 - 33870:00

in doing this sort of model development

## 33870:00 - 33915:00

is is picking your your spots carefully,

## 33915:00 - 33935:00

not trying to reinvent the wheel, not

## 33935:00 - 33970:00

trying to focus on places maybe where

## 33970:00 - 34020:00

the the the best foundation models are

## 34020:00 - 34045:00

are excellent, but instead kind of

## 34045:00 - 34070:00

focusing on their weaknesses and how you

## 34070:00 - 34100:00

can complement them. I think this is

## 34100:00 - 34115:00

going to be surprising to a lot of

## 34115:00 - 34135:00

people hearing that you have your own

## 34135:00 - 34170:00

models. when I you know when people talk

## 34170:00 - 34195:00

about cursor and all the folks in the

## 34195:00 - 34230:00

space they would kind of call them GPT

## 34230:00 - 34255:00

rappers they're just sitting on top of

## 34255:00 - 34295:00

Jad JPT or sonnet and what you're saying

## 34295:00 - 34320:00

is that you have your own models talk

## 34320:00 - 34345:00

about just like the stack behind the

## 34345:00 - 34385:00

scenes yeah of course um so we

## 34385:00 - 34420:00

definitely use uh the biggest genation

## 34420:00 - 34450:00

models you know a bunch of different

## 34450:00 - 34475:00

ways um they're really important

## 34475:00 - 34500:00

components of of bringing the cursor

## 34500:00 - 34530:00

experience to people the the places

## 34530:00 - 34585:00

where we use our own models so sometimes

## 34585:00 - 34630:00

it's to serve a use case that a

## 34630:00 - 34650:00

foundation model wouldn't be able to

## 34650:00 - 34705:00

serve at all for cost or speed reasons.

## 34705:00 - 34750:00

And so one example of that is um uh the

## 34750:00 - 34785:00

autocomplete side of things. And so this

## 34785:00 - 34835:00

can be a little bit tricky for uh people

## 34835:00 - 34870:00

who don't code to understand. But code

## 34870:00 - 34925:00

is this weird form of work where

## 34925:00 - 34975:00

sometimes really the next 5 10 20 30

## 34975:00 - 35015:00

minutes of your work is entirely

## 35015:00 - 35030:00

predictable from looking over your

## 35030:00 - 35065:00

shoulder. And I would contrast this with

## 35065:00 - 35115:00

writing. So writing, you know, everyone

## 35115:00 - 35155:00

or lots of people are familiar with, you

## 35155:00 - 35185:00

know, Gmail's autocomplete and kind of

## 35185:00 - 35210:00

the different forms of autocomplete that

## 35210:00 - 35235:00

show up when you're trying to get those

## 35235:00 - 35255:00

text messages or emails or things like

## 35255:00 - 35290:00

that. They can only be so helpful

## 35290:00 - 35315:00

because often it's just really not clear

## 35315:00 - 35340:00

what you're going to be writing just by

## 35340:00 - 35365:00

looking at what you've written before.

## 35365:00 - 35390:00

But in code, sometimes when you edit a

## 35390:00 - 35425:00

part of a codebase, it just you're going

## 35425:00 - 35450:00

to need to change things and in other

## 35450:00 - 35470:00

other parts of a codebase and it's it's

## 35470:00 - 35490:00

entirely clear how you're going to need

## 35490:00 - 35545:00

to change things. And uh so one core

## 35545:00 - 35570:00

part of cursor is this really souped-up

## 35570:00 - 35595:00

autocomplete experience where you

## 35595:00 - 35615:00

predict like the next set of things

## 35615:00 - 35640:00

you're going to be doing across multiple

## 35640:00 - 35675:00

files across multiple places within a

## 35675:00 - 35730:00

file. And you know making models good at

## 35730:00 - 35760:00

that use case. One there's this speed

## 35760:00 - 35790:00

component of those models need to be

## 35790:00 - 35810:00

really fast. They need to give you a

## 35810:00 - 35845:00

completion within 300 milliseconds.

## 35845:00 - 35870:00

There's also this cost component of

## 35870:00 - 35910:00

we're running tons and tons and tons of

## 35910:00 - 35935:00

molecules. You know every keystroke we

## 35935:00 - 35955:00

need to be you know changing our

## 35955:00 - 35975:00

prediction for what you're going to do

## 35975:00 - 36005:00

next. And then it's also this really

## 36005:00 - 36045:00

specialty use case of you need models

## 36045:00 - 36070:00

that are really good not at completing

## 36070:00 - 36105:00

the next token of just like a generic

## 36105:00 - 36135:00

text sequence but are really good at

## 36135:00 - 36175:00

autocompleting a series of diffs um you

## 36175:00 - 36200:00

know looking at what's changed within a

## 36200:00 - 36220:00

codebase and then predicting the next

## 36220:00 - 36245:00

sort of things that are going to change

## 36245:00 - 36270:00

you know both deleted and added and all

## 36270:00 - 36335:00

of that and we we found a ton of success

## 36335:00 - 36370:00

in training models specifically for that

## 36370:00 - 36400:00

task. So that's a place where you know

## 36400:00 - 36430:00

no foundation models are involved. It's

## 36430:00 - 36455:00

kind of our own thing. We don't have a

## 36455:00 - 36485:00

lot of labeling or branding about this

## 36485:00 - 36520:00

in the app but that you know cores of uh

## 36520:00 - 36545:00

you know powers a very core part of

## 36545:00 - 36595:00

cursor and then uh you know another set

## 36595:00 - 36630:00

of places where user models are to to

## 36630:00 - 36685:00

help things like sonnet or gemini or gbt

## 36685:00 - 36730:00

and those sit both on the input of those

## 36730:00 - 36765:00

big models and on the output on the

## 36765:00 - 36790:00

input side of things. Those models are

## 36790:00 - 36820:00

searching throughout a codebase trying

## 36820:00 - 36855:00

to figure out the parts of a codebase to

## 36855:00 - 36900:00

show to one of these big models. Um, you

## 36900:00 - 36920:00

can kind of think about this as like a

## 36920:00 - 36950:00

mini Google search that's specifically

## 36950:00 - 36985:00

built for finding the, you know,

## 36985:00 - 37010:00

relevant parts of a codebase to show one

## 37010:00 - 37050:00

of these big models. And then on the

## 37050:00 - 37085:00

output side of things, you know, we take

## 37085:00 - 37125:00

the sketches of the changes that these

## 37125:00 - 37145:00

models are suggesting you make with that

## 37145:00 - 37190:00

codebase. And then, you know, we have

## 37190:00 - 37210:00

models that then kind of fill in the

## 37210:00 - 37235:00

details of like, you know, the high

## 37235:00 - 37255:00

level thinking is done by these smartest

## 37255:00 - 37290:00

models. They spend a few tokens on doing

## 37290:00 - 37320:00

that. And then these smaller specialty

## 37320:00 - 37350:00

incredibly fast models coupled with some

## 37350:00 - 37400:00

inference tracks then take those highle

## 37400:00 - 37430:00

uh changes and turn them actually into

## 37430:00 - 37465:00

full code discs. And so it's been super

## 37465:00 - 37510:00

helpful for um pushing on on quality in

## 37510:00 - 37545:00

places where you need a specialty task.

## 37545:00 - 37575:00

And it's been super helpful for pushing

## 37575:00 - 37605:00

on speed, which is such an important

## 37605:00 - 37640:00

dimension of product quality for us uh

## 37640:00 - 37685:00

too. This is so interesting. I just had

## 37685:00 - 37720:00

Kevin Wheel on the podcast, CPO of

## 37720:00 - 37755:00

OpenAI, and he calls this the ensemble

## 37755:00 - 37780:00

of models. That's the same way they

## 37780:00 - 37810:00

work. to use the best feature of each

## 37810:00 - 37840:00

one and to your point the cost

## 37840:00 - 37885:00

advantages of using cheaper models. Uh

## 37885:00 - 37920:00

these open these other models are they

## 37920:00 - 37945:00

based on like llama and things like that

## 37945:00 - 37970:00

just open source models that you guys

## 37970:00 - 38020:00

plug into and build on? Yeah. So uh

## 38020:00 - 38070:00

again we try try to be very pragmatic

## 38070:00 - 38085:00

about the places that we're going to do

## 38085:00 - 38105:00

this work and we don't want to reinvent

## 38105:00 - 38140:00

the wheel and so um starting from the

## 38140:00 - 38185:00

the very best um you know uh pre-trained

## 38185:00 - 38235:00

models that exist out there often open

## 38235:00 - 38275:00

source ones you know sometimes in

## 38275:00 - 38305:00

collaboration with these big model

## 38305:00 - 38330:00

providers that that don't share their

## 38330:00 - 38355:00

weights out into the world. Um because

## 38355:00 - 38380:00

the thing we care about less is you know

## 38380:00 - 38430:00

the ability to read read line by line

## 38430:00 - 38465:00

you know the you know the the matrix of

## 38465:00 - 38500:00

weights that then you know go to give

## 38500:00 - 38525:00

you give you a certain output and it's

## 38525:00 - 38545:00

you know we just care about the ability

## 38545:00 - 38580:00

to kind of to to train these things to

## 38580:00 - 38620:00

post train them and so uh by and large

## 38620:00 - 38650:00

by and large yes open source models you

## 38650:00 - 38685:00

know sometimes working with the closed

## 38685:00 - 38710:00

source providers too to tune things.

## 38710:00 - 38740:00

This leads to a a discussion that a lot

## 38740:00 - 38765:00

of AI founders always think about and

## 38765:00 - 38805:00

investors which is moes and

## 38805:00 - 38860:00

defensibility in AI. Uh so it feels like

## 38860:00 - 38910:00

one is custom models is is a moat in the

## 38910:00 - 38945:00

space. How do you just think about

## 38945:00 - 38975:00

long-term defensibility in the space

## 38975:00 - 39000:00

knowing there's other folks as you said

## 39000:00 - 39030:00

launching constantly trying to take your

## 39030:00 - 39070:00

trying to eat your lunch? I think that

## 39070:00 - 39125:00

you know there are ways to to build in

## 39125:00 - 39200:00

inertia and u you know tra traditional

## 39200:00 - 39240:00

modes but uh I you know I think by and

## 39240:00 - 39275:00

large we're in a space where you know it

## 39275:00 - 39325:00

is incumbent on us uh to continue to try

## 39325:00 - 39375:00

to build the best thing and and and

## 39375:00 - 39420:00

everyone in this industry and I you know

## 39420:00 - 39445:00

I truly just think that the ceiling is

## 39445:00 - 39490:00

so high that kind of no matter what you

## 39490:00 - 39545:00

know entrenchment you build um you be

## 39545:00 - 39605:00

leaprog and I think that this uh

## 39605:00 - 39635:00

resembles markets that are maybe a

## 39635:00 - 39670:00

little bit different from normal

## 39670:00 - 39705:00

software markets, normal enterprise uh

## 39705:00 - 39735:00

markets of the past. You know, I think

## 39735:00 - 39770:00

one that comes to mind is is the market

## 39770:00 - 39810:00

for search engines at the end of 1999

## 39810:00 - 39835:00

or, you know, at the end of the the '90s

## 39835:00 - 39865:00

and beginning of the 2000s. I think

## 39865:00 - 39900:00

another market that comes to mind that

## 39900:00 - 39940:00

resembles this market in many ways, it's

## 39940:00 - 39980:00

actually just like the development of um

## 39980:00 - 40005:00

the personal computer and mini

## 40005:00 - 40040:00

computers, you know, in the 70s, '8s,

## 40040:00 - 40090:00

90s. And um I think that yes, you know,

## 40090:00 - 40120:00

in each of those markets, the ceiling

## 40120:00 - 40150:00

was incredibly high. You know, it was

## 40150:00 - 40185:00

possible to switch. You could keep

## 40185:00 - 40220:00

getting value for like the incremental

## 40220:00 - 40245:00

hour of a smart person's time, the

## 40245:00 - 40275:00

incremental R&D dollar for a really long

## 40275:00 - 40295:00

time. You wouldn't run out of useful

## 40295:00 - 40350:00

things to build. And then you know in in

## 40350:00 - 40380:00

in search in particular not in the

## 40380:00 - 40420:00

computer case having distribution was

## 40420:00 - 40450:00

was helpful for making the product

## 40450:00 - 40485:00

better too in that you could tune the

## 40485:00 - 40520:00

algorithms you could tune the learning

## 40520:00 - 40550:00

based off of the the data and the

## 40550:00 - 40585:00

feedback you're getting from users and I

## 40585:00 - 40600:00

think that you know all of those

## 40600:00 - 40635:00

dynamics exist exist in our market too

## 40635:00 - 40680:00

and so I think that you know maybe the

## 40680:00 - 40710:00

sad sad truth for people like us but

## 40710:00 - 40735:00

then like the amazing truth for the

## 40735:00 - 40760:00

world is I think that there are many

## 40760:00 - 40795:00

leaf frogs that exist uh there's many

## 40795:00 - 40825:00

you know more useful things to We're a

## 40825:00 - 40850:00

long way away from where we can be in,

## 40850:00 - 40880:00

you know, 5 10 years and it's kind of

## 40880:00 - 40900:00

incumbent on us state to keep that

## 40900:00 - 40930:00

engine going. So what I'm hearing is

## 40930:00 - 40970:00

sounds like a lot more like a consumer

## 40970:00 - 41000:00

sort of mode where it's just be the best

## 41000:00 - 41030:00

thing consistently so that people stick

## 41030:00 - 41075:00

with you versus creating lock in and

## 41075:00 - 41095:00

things like that where they're just for

## 41095:00 - 41120:00

like Salesforce where it's just

## 41120:00 - 41140:00

contracts with the entire company and

## 41140:00 - 41170:00

you have to use this product. Yeah. And

## 41170:00 - 41200:00

I think the the important thing to note

## 41200:00 - 41245:00

is, you know, if you're in a a space

## 41245:00 - 41275:00

where like you kind of run out of useful

## 41275:00 - 41305:00

things to do very quickly, then that's

## 41305:00 - 41325:00

you know, that's not a great situation

## 41325:00 - 41355:00

to be in. But if you're in a place

## 41355:00 - 41420:00

where, you know, big investments and um

## 41420:00 - 41450:00

you know, ha having more and more great

## 41450:00 - 41480:00

people working on the right path can

## 41480:00 - 41515:00

keep giving you value, then you can get

## 41515:00 - 41545:00

kind of these economies of scale of R&D

## 41545:00 - 41585:00

and you can kind of have you know, you

## 41585:00 - 41615:00

know, deeply work on the technology in

## 41615:00 - 41635:00

the right direction and and get to a

## 41635:00 - 41670:00

place where that is defensible. Uh but

## 41670:00 - 41710:00

yes it is it is you know I think there's

## 41710:00 - 41735:00

there's a consumer-like tenency to it

## 41735:00 - 41765:00

and I really think it's just a you know

## 41765:00 - 41800:00

about building the best thing possible.

## 41800:00 - 41820:00

Do you think in the future there's one

## 41820:00 - 41840:00

winner in this space or do you think

## 41840:00 - 41870:00

it's going to be a world of a number of

## 41870:00 - 41905:00

products like this? I think the market

## 41905:00 - 41935:00

is just so very big. And this is also

## 41935:00 - 41975:00

one thing that um you know, you asked

## 41975:00 - 42015:00

about the IDE thing early on

## 42015:00 - 42065:00

and one thing that I think tripped up

## 42065:00 - 42080:00

some people that were thinking about the

## 42080:00 - 42135:00

space is like they looked at the IDE

## 42135:00 - 42180:00

market of the past 10 years and they

## 42180:00 - 42220:00

said, you know, who's making money off

## 42220:00 - 42250:00

of the editors? Like, you know, there's

## 42250:00 - 42295:00

all these it's this super fragmented

## 42295:00 - 42315:00

space where everyone kind of has their

## 42315:00 - 42350:00

own thing with their own configuration.

## 42350:00 - 42385:00

And you know there's one company that

## 42385:00 - 42420:00

commercially like you know actually

## 42420:00 - 42450:00

makes money off of of making great great

## 42450:00 - 42485:00

editors but like that company is only so

## 42485:00 - 42550:00

big and uh you know then like the

## 42550:00 - 42570:00

conclusion was it was going to look like

## 42570:00 - 42600:00

that in the future. And I think that the

## 42600:00 - 42630:00

thing that people missed was that you

## 42630:00 - 42685:00

know there was only so much you could do

## 42685:00 - 42715:00

building an editor in the 2010s for

## 42715:00 - 42755:00

coders. And you know the the company

## 42755:00 - 42785:00

that made money off of editors was doing

## 42785:00 - 42810:00

things like making it easy to navigate

## 42810:00 - 42850:00

around a codebase and you know doing

## 42850:00 - 42875:00

some some error checking and type

## 42875:00 - 42920:00

checking for things and you know having

## 42920:00 - 42955:00

good debugging tools but like which were

## 42955:00 - 43000:00

all very useful but I think that the the

## 43000:00 - 43030:00

set of things you can build for

## 43030:00 - 43050:00

programmers. I think the set of things

## 43050:00 - 43070:00

you can build for knowledge workers in

## 43070:00 - 43110:00

many different areas just goes very far

## 43110:00 - 43135:00

and very deep. And I think that really

## 43135:00 - 43170:00

kind of like the the problem in front of

## 43170:00 - 43205:00

all of us is is like the automation of a

## 43205:00 - 43230:00

lot of busy work and knowledge work and

## 43230:00 - 43260:00

really changing all the areas of

## 43260:00 - 43285:00

knowledge work in front of us to be u

## 43285:00 - 43330:00

much highable and more productive. So uh

## 43330:00 - 43355:00

that that was all you know a long-winded

## 43355:00 - 43385:00

way to say I think the market's really

## 43385:00 - 43410:00

really big that we're in. uh I think

## 43410:00 - 43430:00

it's much bigger than people have

## 43430:00 - 43480:00

realized uh than you know the other uh

## 43480:00 - 43505:00

you know building tools for developers

## 43505:00 - 43535:00

in the past and I think that there will

## 43535:00 - 43565:00

be a bunch of different solutions. I

## 43565:00 - 43595:00

think that there will be one company and

## 43595:00 - 43625:00

to be determined if it's going to be us,

## 43625:00 - 43645:00

but I do think that there will be one

## 43645:00 - 43705:00

company that builds the the general tool

## 43705:00 - 43730:00

that builds almost all the world

## 43730:00 - 43765:00

software and that will be a very very

## 43765:00 - 43805:00

generationally big business. But I think

## 43805:00 - 43825:00

that there will be kind of niches you

## 43825:00 - 43865:00

can occupy and doing something for a

## 43865:00 - 43890:00

particular segment of the market or for

## 43890:00 - 43910:00

a very particular part of the software

## 43910:00 - 43940:00

development life cycle. But the general

## 43940:00 - 43975:00

like programming shifts from just

## 43975:00 - 44000:00

writing formal programming languages to

## 44000:00 - 44040:00

something way higher level. this is the

## 44040:00 - 44075:00

application you you purchase and use to

## 44075:00 - 44110:00

do that. Uh I think that there will be

## 44110:00 - 44150:00

generally one winner there and and it

## 44150:00 - 44205:00

will be a very big business. juicy. Uh

## 44205:00 - 44240:00

along those lines, it's interesting that

## 44240:00 - 44270:00

Microsoft was actually like right at

## 44270:00 - 44320:00

this like at the center of this first

## 44320:00 - 44360:00

with an amazing product. Amazing

## 44360:00 - 44395:00

distribution co-pilot you said was like

## 44395:00 - 44430:00

the thing that got you over the hump of

## 44430:00 - 44445:00

like, wow, there could be something

## 44445:00 - 44480:00

really big here and it doesn't feel like

## 44480:00 - 44500:00

they're winning. Feels like they're

## 44500:00 - 44545:00

falling behind. What do you think? What

## 44545:00 - 44570:00

What do you think happened there? I

## 44570:00 - 44600:00

think that there are like specific

## 44600:00 - 44655:00

historical reasons why co-pilot might

## 44655:00 - 44705:00

not have lived up or so far have have

## 44705:00 - 44735:00

kind of uh lived up to the expectations

## 44735:00 - 44760:00

that some people had for it. And then I

## 44760:00 - 44790:00

think that there are structural reasons.

## 44790:00 - 44840:00

I think the structural reason is and to

## 44840:00 - 44875:00

be clear you know Microsoft you know in

## 44875:00 - 44920:00

the co-pilot case obviously a big

## 44920:00 - 44955:00

inspiration for our work. Um and in

## 44955:00 - 44985:00

general I you know think they do lots of

## 44985:00 - 45020:00

awesome things and we're users of many

## 45020:00 - 45050:00

Microsoft products.

## 45050:00 - 45105:00

Um but I think that this is a market

## 45105:00 - 45150:00

that's not super friendly to incumbents

## 45150:00 - 45195:00

in that um you know a market that's

## 45195:00 - 45220:00

friendly to incumbents might be one

## 45220:00 - 45250:00

where there's only so much to do it kind

## 45250:00 - 45280:00

of gets commoditized fairly quickly and

## 45280:00 - 45300:00

you can bundle that in with other

## 45300:00 - 45345:00

products and where the ROI between you

## 45345:00 - 45370:00

know different products is you know

## 45370:00 - 45390:00

quite quite

## 45390:00 - 45440:00

small and you know in that case perhaps

## 45440:00 - 45460:00

it doesn't make sense to buy the

## 45460:00 - 45480:00

innovative solution it makes sense to

## 45480:00 - 45510:00

just kind of buy that thing bundled in

## 45510:00 - 45540:00

with other stuff another market that

## 45540:00 - 45570:00

might be, you know, particularly helpful

## 45570:00 - 45615:00

for incumbents. It is one where there's,

## 45615:00 - 45645:00

you know, from from the get- go, it's

## 45645:00 - 45670:00

just like you have your stuff in one

## 45670:00 - 45695:00

place and it's like really really

## 45695:00 - 45735:00

excruciatingly hard to switch. And, you

## 45735:00 - 45755:00

know, for better, for worse, I think in

## 45755:00 - 45785:00

in our case, you can try out different

## 45785:00 - 45810:00

tools. You can decide which product you

## 45810:00 - 45840:00

think is better. And so, that's not

## 45840:00 - 45885:00

super friendly uh to to in comments and

## 45885:00 - 45910:00

that's more friendly to whoever you

## 45910:00 - 45925:00

think is going to have the most

## 45925:00 - 45960:00

innovative product. And then the

## 45960:00 - 45990:00

specific historical reasons like as I

## 45990:00 - 46025:00

understand them are the group of people

## 46025:00 - 46050:00

that worked on the first version of

## 46050:00 - 46100:00

copilot have by and large gone on to do

## 46100:00 - 46140:00

other things at other places. I think

## 46140:00 - 46155:00

it's been a little hard to kind of

## 46155:00 - 46175:00

coordinate among all the different

## 46175:00 - 46195:00

departments and parties that might be

## 46195:00 - 46235:00

involved in in making something uh like

## 46235:00 - 46270:00

this. I want to come back to cursor. A

## 46270:00 - 46290:00

question I like to ask everyone that's

## 46290:00 - 46350:00

building a tool like this. If you could

## 46350:00 - 46385:00

sit next to every new user that uses

## 46385:00 - 46405:00

cursor for the first time and just

## 46405:00 - 46450:00

whisper a couple tips in their ear to be

## 46450:00 - 46480:00

more successful, most successful with

## 46480:00 - 46520:00

cursor, what would be like one or two

## 46520:00 - 46565:00

tips? I think right now and we'd want to

## 46565:00 - 46605:00

fix this at a product level. A lot of

## 46605:00 - 46650:00

being successful with Kerser is kind of

## 46650:00 - 46690:00

having a taste for like what the models

## 46690:00 - 46730:00

can do, both what complexity of a task

## 46730:00 - 46760:00

they can handle and like kind of how

## 46760:00 - 46790:00

much you need to

## 46790:00 - 46830:00

specify, you know, things things to that

## 46830:00 - 46860:00

that model, but like having a a taste

## 46860:00 - 46885:00

for the quality of the model and where

## 46885:00 - 46905:00

its gaps exist and what it can do and

## 46905:00 - 46960:00

what it can't. And um right now we don't

## 46960:00 - 46995:00

do a good job in the product of like you

## 46995:00 - 47045:00

know educating people around that um and

## 47045:00 - 47075:00

maybe giving people some swim lanes

## 47075:00 - 47110:00

giving people some guidelines but so um

## 47110:00 - 47155:00

to develop that taste um would give kind

## 47155:00 - 47210:00

of two two tips. So one is as mentioned

## 47210:00 - 47270:00

before uh I would bias less toward like

## 47270:00 - 47305:00

hey trying to have the model like you

## 47305:00 - 47365:00

know trying in one go to tell the model

## 47365:00 - 47390:00

hey here's exactly what I want you to do

## 47390:00 - 47415:00

then seeing the output and then either

## 47415:00 - 47440:00

being disappointed or accepting the

## 47440:00 - 47470:00

entire thing for an entire big task.

## 47470:00 - 47500:00

Instead what I would do is I would chop

## 47500:00 - 47530:00

things up into bits and you can spend

## 47530:00 - 47550:00

basically you know the same amount of

## 47550:00 - 47595:00

time specifying things overall but

## 47595:00 - 47620:00

chopped up more. So you're specifying a

## 47620:00 - 47635:00

little bit, you're getting a little bit

## 47635:00 - 47650:00

of work, you're specifying a little bit,

## 47650:00 - 47670:00

getting a little bit of work, and you

## 47670:00 - 47700:00

know, not doing as much the like let's

## 47700:00 - 47740:00

write a giant thing telling all exactly

## 47740:00 - 47765:00

what to do. I think that will be a

## 47765:00 - 47790:00

little bit of a recipe for disaster

## 47790:00 - 47830:00

right now. Uh and so biasing toward

## 47830:00 - 47865:00

chopping things up at the at the same

## 47865:00 - 47895:00

time and it might make sense to do this

## 47895:00 - 47920:00

on a side project and not on your

## 47920:00 - 47950:00

professional work. You know, I would

## 47950:00 - 47990:00

encourage people to especially, you

## 47990:00 - 48045:00

know, developers who are kind of used to

## 48045:00 - 48070:00

existing workflows for building

## 48070:00 - 48095:00

software. You know, I would encourage

## 48095:00 - 48130:00

people to explicitly try to fall on

## 48130:00 - 48165:00

their face and try to discover the

## 48165:00 - 48210:00

limits of uh what these models can do

## 48210:00 - 48245:00

by, you know, being ambitious in like

## 48245:00 - 48290:00

kind of a a safe environment, uh like

## 48290:00 - 48325:00

perhaps a side project and and trying to

## 48325:00 - 48355:00

kind of go hand to use AI to the fullest

## 48355:00 - 48385:00

because, you know, sometimes we do run

## 48385:00 - 48425:00

or a lot of the time we run into people

## 48425:00 - 48465:00

um who haven't given the AI yet a fair

## 48465:00 - 48505:00

shake and are kind of underestimating

## 48505:00 - 48540:00

its abilities. So generally biasing

## 48540:00 - 48565:00

towards chopping things up and making

## 48565:00 - 48590:00

things smaller but like to discover the

## 48590:00 - 48620:00

limits of what you can do there like

## 48620:00 - 48645:00

explicitly just kind of try to go for

## 48645:00 - 48680:00

broke in a safe environment and you know

## 48680:00 - 48710:00

get get a taste for it. You might be

## 48710:00 - 48730:00

surprised in some of the places where

## 48730:00 - 48760:00

the model doesn't break. What I'm

## 48760:00 - 48800:00

essentially hearing is kind of build a

## 48800:00 - 48840:00

gut feeling of what the model can do and

## 48840:00 - 48885:00

how far it can take an idea versus just

## 48885:00 - 48935:00

kind of guiding it along. And I bet that

## 48935:00 - 48965:00

you need to rebuild this gut every time

## 48965:00 - 48985:00

there's a new model launch like when

## 48985:00 - 49015:00

it's on it I don't know 4.0. I know

## 49015:00 - 49035:00

comes out you have to kind of do this

## 49035:00 - 49085:00

again. Is that generally right? Yes. Uh

## 49085:00 - 49130:00

it's not you know for the past few years

## 49130:00 - 49170:00

it hasn't been as big as like I think

## 49170:00 - 49215:00

the the first kind of experience people

## 49215:00 - 49240:00

have had with some of these big models

## 49240:00 - 49285:00

but um yeah you know it this is also a

## 49285:00 - 49310:00

problem we would hope to solve much

## 49310:00 - 49345:00

better just for users and take the burn

## 49345:00 - 49375:00

off of them. But yeah each of these

## 49375:00 - 49400:00

things have slightly different quirks

## 49400:00 - 49435:00

and different personalities. kind of

## 49435:00 - 49460:00

along these lines, something that people

## 49460:00 - 49500:00

are always debating, tools like cursor,

## 49500:00 - 49530:00

are they more helpful to junior

## 49530:00 - 49570:00

engineers or are they more helpful to

## 49570:00 - 49590:00

senior engineers? Do they make senior

## 49590:00 - 49610:00

engineers 10x better? Do they make

## 49610:00 - 49635:00

junior engineers more like senior

## 49635:00 - 49670:00

engineers? Where do you think most of

## 49670:00 - 49700:00

who do you think it benefits most today

## 49700:00 - 49760:00

from cursor? I think across the board u

## 49760:00 - 49790:00

both of these cohorts benefit in big

## 49790:00 - 49840:00

ways. It's a little hard to say on the

## 49840:00 - 49880:00

relative ranking. I will say they fall

## 49880:00 - 49925:00

into different anti patterns. So I would

## 49925:00 - 49975:00

the junior engineers we see going a

## 49975:00 - 50025:00

little too wholesale relying on AI for

## 50025:00 - 50085:00

everything and we're not yet in a place

## 50085:00 - 50115:00

where you can kind of do that end to end

## 50115:00 - 50140:00

on a professional tool you know working

## 50140:00 - 50165:00

with tens hundreds of other people

## 50165:00 - 50195:00

within a long

## 50195:00 - 50240:00

codebase and then the senior engineers

## 50240:00 - 50265:00

for many folks is not true for all and

## 50265:00 - 50340:00

we actually uh uh often you know one of

## 50340:00 - 50365:00

the ways these tools are adopted is

## 50365:00 - 50385:00

there's developer experience teams

## 50385:00 - 50420:00

within companies often there staffed by

## 50420:00 - 50450:00

incredibly senior, you know, senior

## 50450:00 - 50485:00

people because often those are people

## 50485:00 - 50515:00

who, you know, are building tools to

## 50515:00 - 50540:00

make the rest of the engineers within an

## 50540:00 - 50560:00

organization more productive. And we've

## 50560:00 - 50595:00

seen some very very um, you know,

## 50595:00 - 50660:00

boundary pushing kind of uh uh yeah,

## 50660:00 - 50685:00

like we've seen people who are, you

## 50685:00 - 50715:00

know, on on the the front lines of like

## 50715:00 - 50745:00

really trying to adopt the technology as

## 50745:00 - 50770:00

much as possible there. But by and large

## 50770:00 - 50815:00

I would say on average as a group the

## 50815:00 - 50865:00

senior engineers underrate what AI can

## 50865:00 - 50900:00

do for them and stick to their existing

## 50900:00 - 50930:00

workflows. And so the relative ranking

## 50930:00 - 50955:00

is a little hard. I think they both have

## 50955:00 - 50985:00

they they fall into to different

## 50985:00 - 51020:00

different antiatterns. Uh but they both

## 51020:00 - 51055:00

by and large get get big benefits these

## 51055:00 - 51105:00

tools. That makes absolute sense. Uh I

## 51105:00 - 51125:00

love that it's like two ends of the

## 51125:00 - 51150:00

spectrum like expect too much don't

## 51150:00 - 51215:00

expect enough. And it's like the uh the

## 51215:00 - 51270:00

three bears. Is that the allegory? Yeah.

## 51270:00 - 51320:00

Yeah. Okay. The uh Yeah. Maybe the sort

## 51320:00 - 51360:00

of senior but not staff, you know, right

## 51360:00 - 51405:00

right in the middle.

## 51405:00 - 51435:00

Interesting. Okay. Just a couple more

## 51435:00 - 51475:00

questions. Um what's something that you

## 51475:00 - 51510:00

wish you knew before you got into this

## 51510:00 - 51545:00

role? If you could go back to Michael at

## 51545:00 - 51570:00

the beginning of Cursor, which was not

## 51570:00 - 51600:00

that long ago, and you could give him

## 51600:00 - 51620:00

some advice, what's something that you

## 51620:00 - 51650:00

would tell him? The tough thing with

## 51650:00 - 51720:00

this is feels like so much of the uh the

## 51720:00 - 51775:00

hard one knowledge is tacit and a bit

## 51775:00 - 51825:00

hard to communicate verbally and

## 51825:00 - 51880:00

uh the sad fact of life feels like for

## 51880:00 - 51910:00

you know for some areas of human

## 51910:00 - 51940:00

endeavor like you kind of do need to

## 51940:00 - 51990:00

fall on your face to uh either either

## 51990:00 - 52015:00

need to fall on your face to to learn

## 52015:00 - 52035:00

the correct thing or you need to be kind

## 52035:00 - 52060:00

of around someone which is a great

## 52060:00 - 52085:00

example of kind of excellence in the

## 52085:00 - 52140:00

thing and one area where we have felt

## 52140:00 - 52220:00

this is is is hiring. Um I think that uh

## 52220:00 - 52280:00

we actually were so we we tried to be

## 52280:00 - 52325:00

incredibly patient on the hiring front.

## 52325:00 - 52385:00

Um it was really important to us that

## 52385:00 - 52420:00

you know both for personal reasons and

## 52420:00 - 52445:00

also for I think actually for the

## 52445:00 - 52495:00

company strategy having a world-class

## 52495:00 - 52540:00

group of engineers and researchers to

## 52540:00 - 52575:00

work on on cursor with us was going to

## 52575:00 - 52605:00

be incredibly important. Also getting

## 52605:00 - 52650:00

people who fit, you know, a sort of mix

## 52650:00 - 52705:00

of, you know, intellectual curiosity and

## 52705:00 - 52725:00

experimentation because there's gonna be

## 52725:00 - 52765:00

so many new things we need to build and

## 52765:00 - 52790:00

then also kind of an intellectual

## 52790:00 - 52830:00

honesty and maybe micro pessimism,

## 52830:00 - 52855:00

bluntness because, you know, with all

## 52855:00 - 52885:00

the noise and, you know, especially as

## 52885:00 - 52920:00

the company's grown and the business has

## 52920:00 - 52950:00

grown, you know, keeping a level head, I

## 52950:00 - 52985:00

think, is incredibly important, too. Um

## 52985:00 - 53005:00

but getting the right group of people

## 53005:00 - 53055:00

into the company you know was you know

## 53055:00 - 53085:00

the the thing that maybe more than

## 53085:00 - 53125:00

anything else apart from apart from

## 53125:00 - 53180:00

building the product we really really um

## 53180:00 - 53240:00

uh you know fussed over and uh you know

## 53240:00 - 53270:00

I we actually waited a long time to grow

## 53270:00 - 53305:00

the team because of that and I think

## 53305:00 - 53345:00

that most you know many people you hear

## 53345:00 - 53380:00

hired too fast. I think we actually

## 53380:00 - 53425:00

hired too slow to begin with. I think it

## 53425:00 - 53440:00

could have been remedied. I think we

## 53440:00 - 53495:00

could have been better at it. And um you

## 53495:00 - 53555:00

know the the method of uh uh of

## 53555:00 - 53580:00

recruiting that we ended up uh

## 53580:00 - 53605:00

eventually falling into working really

## 53605:00 - 53635:00

well for us which which isn't that novel

## 53635:00 - 53665:00

of like going after people that we think

## 53665:00 - 53690:00

are really world class and like

## 53690:00 - 53720:00

recruiting them over the course of in

## 53720:00 - 53770:00

some cases many years. Uh ended up

## 53770:00 - 53790:00

working for us in the end but I I don't

## 53790:00 - 53810:00

think we were very good at it to begin

## 53810:00 - 53830:00

with. And so I think that there were

## 53830:00 - 53880:00

hard one lessons around both who was the

## 53880:00 - 53910:00

right profile like who actually meets

## 53910:00 - 53940:00

sense on the team like what did what did

## 53940:00 - 53970:00

greatness look like um and then how to

## 53970:00 - 54020:00

you know um talk with someone um about

## 54020:00 - 54050:00

about the opportunity and you know get

## 54050:00 - 54080:00

them excited if they really weren't

## 54080:00 - 54115:00

looking for anything. Um there there

## 54115:00 - 54145:00

were lots of kind of learnings there

## 54145:00 - 54180:00

about how to do that well um and that

## 54180:00 - 54210:00

took us a bit of time. What are some of

## 54210:00 - 54235:00

those learnings for folks that are you

## 54235:00 - 54265:00

know hiring right now? What's something

## 54265:00 - 54305:00

you missed or or learned? I think you

## 54305:00 - 54350:00

know to start with uh we maybe we

## 54350:00 - 54380:00

actually biased a little bit too much

## 54380:00 - 54415:00

towards

## 54415:00 - 54450:00

um looking for people who fit the

## 54450:00 - 54505:00

archetype of well-known school very

## 54505:00 - 54540:00

young had done the things that were like

## 54540:00 - 54590:00

you know high credential um in those

## 54590:00 - 54660:00

well-known school environments and um

## 54660:00 - 54710:00

and actually like you know I think found

## 54710:00 - 54745:00

were lucky early on to find a lot of you

## 54745:00 - 54790:00

know u to find uh fantastic people who

## 54790:00 - 54825:00

were willing to, you know, to do this

## 54825:00 - 54855:00

with us, uh, who were who were later

## 54855:00 - 54895:00

careered. And so, yeah, I think we kind

## 54895:00 - 54920:00

of spent a bunch of time on maybe a

## 54920:00 - 54945:00

little bit of the wrong profile to begin

## 54945:00 - 54975:00

with. And part of that was a seniority

## 54975:00 - 54995:00

thing. Part of that was like, you know,

## 54995:00 - 55020:00

kind of an interest and experience

## 55020:00 - 55060:00

thing, too. We have hired people who are

## 55060:00 - 55080:00

excellent, excellent, excellent, and

## 55080:00 - 55125:00

very young, but they maybe look uh, in

## 55125:00 - 55155:00

some cases slightly different from, you

## 55155:00 - 55180:00

know, being straight out of central

## 55180:00 - 55215:00

casting. You know, another lesson is

## 55215:00 - 55260:00

just like we very much evolved our

## 55260:00 - 55325:00

interview loop. And so now we uh you

## 55325:00 - 55370:00

know we have like a handrolled set of

## 55370:00 - 55405:00

interview questions and then you know

## 55405:00 - 55460:00

kind of core to our um core to how we

## 55460:00 - 55485:00

interview too is is actually we have

## 55485:00 - 55520:00

people on site for two days and do do a

## 55520:00 - 55575:00

project with us a work test project and

## 55575:00 - 55600:00

um that has worked really well but

## 55600:00 - 55640:00

increasingly refining that and then yeah

## 55640:00 - 55680:00

I think how to to learn about what

## 55680:00 - 55715:00

people are interested in and you know

## 55715:00 - 55740:00

put our best foot forward and and

## 55740:00 - 55765:00

letting them know about the opportunity

## 55765:00 - 55785:00

when they're really not looking for

## 55785:00 - 55820:00

anything and have those conversations.

## 55820:00 - 55850:00

Uh there's definitely been, you know,

## 55850:00 - 55890:00

gotten gotten better at that over time.

## 55890:00 - 55910:00

Do you have a favorite interview

## 55910:00 - 55940:00

question they like to ask? I think this

## 55940:00 - 55980:00

two-day work test, which we thought

## 55980:00 - 56010:00

would not scale past a few people, has

## 56010:00 - 56055:00

been has had surprising staying power.

## 56055:00 - 56100:00

And the great thing about it is it lets

## 56100:00 - 56140:00

someone go end to end on like a real

## 56140:00 - 56165:00

project. It's it's not, you know, work

## 56165:00 - 56200:00

that we use. It's kind of a canal list

## 56200:00 - 56230:00

of projects. Um, but it gives you two

## 56230:00 - 56265:00

days of seeing like a real work

## 56265:00 - 56330:00

product. And um, it doesn't have to be

## 56330:00 - 56355:00

incredibly time intensive on the team's

## 56355:00 - 56385:00

front uh, time. You know, you can take

## 56385:00 - 56410:00

the time you would spend in like a half

## 56410:00 - 56440:00

day or one day onsite and you kind of

## 56440:00 - 56465:00

spread it out over those two days and

## 56465:00 - 56500:00

give someone a lot of time to do to do

## 56500:00 - 56545:00

work on their project. And so that can

## 56545:00 - 56590:00

actually help it help it scale. Uh and

## 56590:00 - 56620:00

then it really helps

## 56620:00 - 56680:00

you it helps to enforce you know do you

## 56680:00 - 56720:00

want to be around this person type test

## 56720:00 - 56765:00

um because you are around this person uh

## 56765:00 - 56800:00

you know for two days and so you know

## 56800:00 - 56845:00

bunch of meals with them and uh so that

## 56845:00 - 56870:00

one we didn't expect that one to stick

## 56870:00 - 56895:00

around but that has been really really

## 56895:00 - 56925:00

important to our value process and then

## 56925:00 - 56960:00

also important to getting people excited

## 56960:00 - 56990:00

at the especially the very early stages

## 56990:00 - 57025:00

of the company because before people are

## 57025:00 - 57060:00

using the product and know about it and

## 57060:00 - 57080:00

you know when the the product is

## 57080:00 - 57115:00

comparatively like not very good. Really

## 57115:00 - 57150:00

the only thing you have going for you is

## 57150:00 - 57175:00

you know a team of people that you know

## 57175:00 - 57205:00

some some people find special and want

## 57205:00 - 57240:00

to be around and you know the two days

## 57240:00 - 57270:00

it would would give us a chance to just

## 57270:00 - 57310:00

like you know have this person uh meet

## 57310:00 - 57350:00

us and uh in some cases hopefully get

## 57350:00 - 57370:00

get convinced that they they want to

## 57370:00 - 57405:00

throw in with us. And so yeah that one

## 57405:00 - 57435:00

that one was unexpected not exactly an

## 57435:00 - 57460:00

interview question but kind of like a

## 57460:00 - 57495:00

you know a formative interview. The

## 57495:00 - 57530:00

ultimate interview question. So just to

## 57530:00 - 57545:00

be very clear about what you're

## 57545:00 - 57565:00

describing, it's a you give them an

## 57565:00 - 57595:00

assignment like build this feature in

## 57595:00 - 57620:00

our actual codebase, work with the team

## 57620:00 - 57665:00

to uh code it and ship it. Is that

## 57665:00 - 57700:00

roughly right? Uh yes. Not not like so

## 57700:00 - 57730:00

we don't use the IP not shipped end to

## 57730:00 - 57780:00

end but yeah it's like a mock like very

## 57780:00 - 57820:00

often in our codebase here's a real mini

## 57820:00 - 57855:00

two-day project you're going to do it

## 57855:00 - 57890:00

end to end largely being left alone. You

## 57890:00 - 57925:00

know there's there's collaboration too.

## 57925:00 - 57950:00

Uh and then you know we're we're a

## 57950:00 - 57990:00

pretty inerson company so in almost all

## 57990:00 - 58020:00

cases yeah it's actually just sitting in

## 58020:00 - 58050:00

office with us too and you've been

## 58050:00 - 58080:00

saying that this has scaled to even

## 58080:00 - 58110:00

today's how how big are you guys at this

## 58110:00 - 58175:00

point? Uh so we are going on 60 people

## 58175:00 - 58220:00

so small for the scale and impact that I

## 58220:00 - 58245:00

was I was thinking it'd be a lot larger

## 58245:00 - 58285:00

than that. Yeah. And I imagine the

## 58285:00 - 58325:00

largest percentage is engineers. Yeah.

## 58325:00 - 58380:00

The thing that's more than anything and

## 58380:00 - 58420:00

to be clear, you know, a big part of the

## 58420:00 - 58460:00

the work ahead of us is is is building a

## 58460:00 - 58495:00

group of people that is is bigger and

## 58495:00 - 58530:00

awesome and can continue to make the the

## 58530:00 - 58550:00

product better and the service we give

## 58550:00 - 58575:00

to customers better. And so you don't

## 58575:00 - 58610:00

plan to stay that small uh for longer.

## 58610:00 - 58645:00

We wouldn't wouldn't hope so. But uh

## 58645:00 - 58680:00

yeah, part part of the reason that um

## 58680:00 - 58720:00

that number is is small is uh the

## 58720:00 - 58755:00

percentage of of engineering and and

## 58755:00 - 58780:00

research and design is very high within

## 58780:00 - 58820:00

the company. And so uh many software

## 58820:00 - 58840:00

companies when they have you know

## 58840:00 - 58885:00

roughly 40 engineers would be over 100

## 58885:00 - 58915:00

people because there's lots of

## 58915:00 - 58940:00

operational work and often they're very

## 58940:00 - 58975:00

very salesled from the get- go uh and

## 58975:00 - 59010:00

that's just quite labor intensive and

## 59010:00 - 59030:00

you know we started from a place of

## 59030:00 - 59060:00

being like incredibly lean and

## 59060:00 - 59100:00

productled and like you know we now

## 59100:00 - 59125:00

serve lots of market customers and had

## 59125:00 - 59155:00

built out but you know there's much more

## 59155:00 - 59200:00

to do there. a question I wanted to ask

## 59200:00 - 59240:00

you. There's so much happening in AI.

## 59240:00 - 59265:00

There's things launching every there's

## 59265:00 - 59300:00

like newsletters like many newsletters

## 59300:00 - 59325:00

whose entire function is to tell you

## 59325:00 - 59365:00

what is happening in AI every single

## 59365:00 - 59400:00

day. Running a company that's at the

## 59400:00 - 59425:00

center kind of the white hot center of

## 59425:00 - 59475:00

the space. How do you stay focused and

## 59475:00 - 59510:00

how do you help your team stay focused

## 59510:00 - 59535:00

and heads down and just build and not

## 59535:00 - 59555:00

get distracted by all these shiny

## 59555:00 - 59600:00

things? you know, I think hiring is a

## 59600:00 - 59625:00

big part of it and if you get people

## 59625:00 - 59665:00

with the the right attitude,

## 59665:00 - 59705:00

um, and you know, all of this should be

## 59705:00 - 59750:00

asked and like, you know, I think we're

## 59750:00 - 59785:00

doing well there. I think that like, you

## 59785:00 - 59810:00

know, we'd probably be doing better

## 59810:00 - 59855:00

there, too. And, um, you know, it's

## 59855:00 - 59870:00

something that we should probably talk

## 59870:00 - 59900:00

even more about as a company. But I

## 59900:00 - 59920:00

think that you know hiring people with

## 59920:00 - 59945:00

the right disposition, you know, people

## 59945:00 - 60000:00

who are less focused on external

## 60000:00 - 60025:00

validation, more focused on building

## 60025:00 - 60045:00

something really great, more focused on

## 60045:00 - 60080:00

doing really high quality work and

## 60080:00 - 60115:00

people who are just generally kind of uh

## 60115:00 - 60160:00

level levelheaded and uh maybe like the

## 60160:00 - 60175:00

highs aren't very high and the lows

## 60175:00 - 60220:00

aren't very low. I think hiring can can

## 60220:00 - 60240:00

get you through a lot here. I think

## 60240:00 - 60265:00

that's that's actually like you know a

## 60265:00 - 60305:00

learning throughout the company is that

## 60305:00 - 60345:00

you know for any you you need process

## 60345:00 - 60365:00

you need hierarchy you need lots of

## 60365:00 - 60400:00

things but for for any kind of

## 60400:00 - 60425:00

organizational tool that you're intro in

## 60425:00 - 60485:00

introducing into a company you know the

## 60485:00 - 60510:00

the result you're looking to get from

## 60510:00 - 60550:00

that tool also you know you can go

## 60550:00 - 60590:00

pretty far on like hiring people with

## 60590:00 - 60620:00

the right behaviors that you want like

## 60620:00 - 60640:00

you know to result from that

## 60640:00 - 60670:00

organizational thing and you know the

## 60670:00 - 60705:00

specific example that comes to mind is

## 60705:00 - 60735:00

we've been able to get away with not

## 60735:00 - 60770:00

ton of process yet on the engineering

## 60770:00 - 60805:00

front and I think we need a little bit

## 60805:00 - 60835:00

more process but for our size not a ton

## 60835:00 - 60870:00

of process by hiring people who I think

## 60870:00 - 60910:00

are really excellent you know one is you

## 60910:00 - 60935:00

know hiring people who are level-headed

## 60935:00 - 60965:00

I think two is just talking about it a

## 60965:00 - 60995:00

lot I think three is hopefully leading

## 60995:00 - 61045:00

by example uh and yeah for us personally

## 61045:00 - 61110:00

you know we've you know since 2021 2022

## 61110:00 - 61145:00

been professionally working on on this

## 61145:00 - 61175:00

and been working on AI and we've just

## 61175:00 - 61215:00

seen a sea change of the comingings and

## 61215:00 - 61255:00

goings of um various technologies and

## 61255:00 - 61285:00

ideas of you know if you're to transport

## 61285:00 - 61315:00

yourself back to end of 2021 beginning

## 61315:00 - 61365:00

of 2022 this is GFD3 you know instruct

## 61365:00 - 61390:00

doesn't exist there's no doll there's no

## 61390:00 - 61440:00

stable diffusion and then you know we've

## 61440:00 - 61475:00

gone through all of those image

## 61475:00 - 61520:00

technologies existing trackt and that

## 61520:00 - 61585:00

rise and you know G4 all of these new

## 61585:00 - 61610:00

models all these different modalities

## 61610:00 - 61675:00

all the video stuff and only you know a

## 61675:00 - 61710:00

very small number of these things really

## 61710:00 - 61755:00

kind of affect affect the business. So I

## 61755:00 - 61790:00

think we've kind of just built up a

## 61790:00 - 61820:00

little bit of an immune system and kind

## 61820:00 - 61855:00

of know know when when an event comes

## 61855:00 - 61880:00

around that actually is really going to

## 61880:00 - 61905:00

matter for us. And this is, you know,

## 61905:00 - 61940:00

this dynamic too of there being lots and

## 61940:00 - 62010:00

lots and lots of chatter but then maybe

## 62010:00 - 62055:00

only a few things that really matter I

## 62055:00 - 62075:00

think has been mirrored in AI over the

## 62075:00 - 62140:00

last decade where um there have been so

## 62140:00 - 62185:00

many papers on deep learning in

## 62185:00 - 62220:00

academia. So many papers on AI in

## 62220:00 - 62260:00

academia. Then the amazing thing is

## 62260:00 - 62315:00

there are really a lot of I mean a lot

## 62315:00 - 62340:00

of the progress of AI can be attributed

## 62340:00 - 62380:00

to some very simple elegant ideas that

## 62380:00 - 62410:00

have stayed around and the vast majority

## 62410:00 - 62440:00

of of ideas that have been put out there

## 62440:00 - 62470:00

haven't had staying power and haven't

## 62470:00 - 62505:00

mattered a ton and so the diversity is a

## 62505:00 - 62520:00

little bit mirrored in kind of the

## 62520:00 - 62535:00

evolution of deep learning as a field

## 62535:00 - 62575:00

overall. Last question. What do you

## 62575:00 - 62630:00

think people still most misunderstand or

## 62630:00 - 62665:00

maybe don't fully grasp where about

## 62665:00 - 62720:00

where things are heading with AI in

## 62720:00 - 62745:00

building and the way the world will

## 62745:00 - 62815:00

change? people are still a little bit,

## 62815:00 - 62860:00

you know, occupied too much either end

## 62860:00 - 62880:00

of a spectrum

## 62880:00 - 62915:00

of uh, you know, it's all going to

## 62915:00 - 62960:00

happen very fast and, you know, this is

## 62960:00 - 63010:00

all, you know, bluster and hype and

## 63010:00 - 63050:00

super snake well. And, you know, I think

## 63050:00 - 63100:00

we're in the middle of a technology

## 63100:00 - 63120:00

shift that's going to be incredibly

## 63120:00 - 63145:00

consequential. I think it's going to be

## 63145:00 - 63165:00

more consequential than the internet. I

## 63165:00 - 63175:00

think it's going to be more

## 63175:00 - 63205:00

consequential than, you know, any shift

## 63205:00 - 63245:00

in tech that we've seen since since the

## 63245:00 - 63285:00

advent of computers and I think it's

## 63285:00 - 63305:00

going to take a while and I think it's

## 63305:00 - 63345:00

going to be a multi-deade thing and I

## 63345:00 - 63365:00

think many different groups will be

## 63365:00 - 63410:00

consequential in pushing it forward and

## 63410:00 - 63450:00

um you know to get to a world where

## 63450:00 - 63475:00

computers can increasingly do more and

## 63475:00 - 63505:00

more and more for us. There's all of

## 63505:00 - 63550:00

these independent problems that need to

## 63550:00 - 63570:00

be knocked down and progress needs to be

## 63570:00 - 63600:00

made on them. And some of those are on

## 63600:00 - 63620:00

the the science side of things of

## 63620:00 - 63650:00

getting these models to understand

## 63650:00 - 63685:00

different types of data, be faster,

## 63685:00 - 63715:00

cheaper, smarter, you know, conform to

## 63715:00 - 63760:00

the yeah, the the modalities that we

## 63760:00 - 63780:00

care about, you know, take actions in

## 63780:00 - 63820:00

the real world. And then some of it's on

## 63820:00 - 63845:00

like how we're going to work with that

## 63845:00 - 63870:00

and, you know, what's the, you know,

## 63870:00 - 63895:00

what's the experience that human should

## 63895:00 - 63925:00

actually be seeing and and controlling

## 63925:00 - 63955:00

on a computer and working with these

## 63955:00 - 63980:00

things. But I think it's going to, you

## 63980:00 - 64015:00

know, it's going to take decades. I

## 64015:00 - 64035:00

think that there's going to be lots of

## 64035:00 - 64075:00

amazing work to do. I think that also,

## 64075:00 - 64135:00

you know, one of the most like a pattern

## 64135:00 - 64155:00

of a group that I think will be

## 64155:00 - 64190:00

especially important here, you know, not

## 64190:00 - 64220:00

not to talk our own book, but I think is

## 64220:00 - 64250:00

like, you know, the company that works

## 64250:00 - 64290:00

on um automating and augmenting a

## 64290:00 - 64310:00

particular particular area of knowledge

## 64310:00 - 64360:00

work builds the both the technology

## 64360:00 - 64390:00

under you know under the surface for

## 64390:00 - 64425:00

that um integrating the best parts from

## 64425:00 - 64450:00

providers sometimes doing it in house

## 64450:00 - 64475:00

and then also builds the you know the

## 64475:00 - 64515:00

product experience for that. I think

## 64515:00 - 64545:00

people who do that and you know we're

## 64545:00 - 64570:00

doing it in trying to do it in software

## 64570:00 - 64595:00

people do that in other areas I think

## 64595:00 - 64620:00

those folks will be really really really

## 64620:00 - 64655:00

consequential not just for like you know

## 64655:00 - 64690:00

the end value that users see but then I

## 64690:00 - 64720:00

think as they get to scale they'll be

## 64720:00 - 64755:00

really important for pushing forward uh

## 64755:00 - 64785:00

the you know the technology because I

## 64785:00 - 64805:00

think they'll be able to build you know

## 64805:00 - 64830:00

the most successful of them will be able

## 64830:00 - 64900:00

to build very very big businesses um and

## 64900:00 - 64945:00

um yeah so excited to see the rise of

## 64945:00 - 64975:00

you know other companies like that in

## 64975:00 - 64990:00

other areas

## 64990:00 - 65035:00

I know you guys are hiring uh for folks

## 65035:00 - 65065:00

that are interested in hey I want to go

## 65065:00 - 65085:00

work here and build this sort of stuff.

## 65085:00 - 65100:00

What kind of roles are you looking for

## 65100:00 - 65130:00

right now? Anyone specifically you're

## 65130:00 - 65155:00

trying to any roles you're most excited

## 65155:00 - 65185:00

about filling ASAP? What should people

## 65185:00 - 65215:00

know if they're curious? there are so

## 65215:00 - 65235:00

many things that this group of people

## 65235:00 - 65265:00

need to do that like we are not yet

## 65265:00 - 65330:00

equipped to do and so uh you know kind

## 65330:00 - 65365:00

of generic across the board first of all

## 65365:00 - 65420:00

and so if you uh don't think we have a

## 65420:00 - 65450:00

role for something maybe if you reach

## 65450:00 - 65485:00

out that that won't actually be the case

## 65485:00 - 65505:00

um and maybe we can actually learn from

## 65505:00 - 65540:00

you and kind of decide that we we need

## 65540:00 - 65570:00

something that we weren't yet aware of

## 65570:00 - 65600:00

but um you know by and large I think

## 65600:00 - 65640:00

that you know two two of the most

## 65640:00 - 65665:00

important things for us to do this year

## 65665:00 - 65705:00

are have the best product in the case

## 65705:00 - 65740:00

and then grow it. And we're kind of in

## 65740:00 - 65780:00

this land grab mode where almost

## 65780:00 - 65835:00

everyone in the world is either using no

## 65835:00 - 65875:00

tool like ours or they're using one

## 65875:00 - 65930:00

that's maybe developing less quickly.

## 65930:00 - 65980:00

And uh so so growing growing um cursio

## 65980:00 - 66035:00

is is is a big goal and um uh I would

## 66035:00 - 66080:00

say yeah especially always on the hunt

## 66080:00 - 66120:00

for for folks uh who excellent

## 66120:00 - 66170:00

engineers, designers, researchers um but

## 66170:00 - 66205:00

then folks in uh all across the business

## 66205:00 - 66240:00

side too. I can't help but ask this

## 66240:00 - 66255:00

question now that you talk about

## 66255:00 - 66275:00

engineers. There's kind of this question

## 66275:00 - 66300:00

of just like you know code's going to

## 66300:00 - 66325:00

write up all all our code, AI is going

## 66325:00 - 66350:00

to write all our code, but everyone's

## 66350:00 - 66375:00

still hiring engineers like crazy. all

## 66375:00 - 66405:00

the foundational models, so many we're

## 66405:00 - 66425:00

not out there cheating the, you know,

## 66425:00 - 66480:00

the horn of uh people looking good. So,

## 66480:00 - 66495:00

yeah. Do you think there's going to be

## 66495:00 - 66520:00

an inflection point of like engineering

## 66520:00 - 66560:00

roles start to kind of slow down? Uh I

## 66560:00 - 66585:00

know this is like a big question, but

## 66585:00 - 66625:00

just it's do you see engineers being

## 66625:00 - 66660:00

more and more needed across all these

## 66660:00 - 66695:00

companies or do you think at some point

## 66695:00 - 66740:00

there's all these cursor agents running

## 66740:00 - 66780:00

building for us? Again, we we kind of

## 66780:00 - 66825:00

have the view that like there's this,

## 66825:00 - 66900:00

you know, both long messy middle of uh

## 66900:00 - 66935:00

you know, it it not jumping to a just

## 66935:00 - 66960:00

like you step back and you ask for all

## 66960:00 - 66980:00

your stuff to be done and you have your

## 66980:00 - 67015:00

engineering department and you know very

## 67015:00 - 67055:00

much like you want to evolve from

## 67055:00 - 67100:00

programming as it exists today. We want

## 67100:00 - 67140:00

humans to be in the driver's seat and

## 67140:00 - 67165:00

you know we think even in the end state

## 67165:00 - 67200:00

like that's you know giving folks

## 67200:00 - 67225:00

control over everything is is really

## 67225:00 - 67250:00

important. um and you will need

## 67250:00 - 67270:00

professionals to do that and kind of

## 67270:00 - 67305:00

decide what the the software looks like.

## 67305:00 - 67335:00

So both both I think that yes like you

## 67335:00 - 67375:00

know uh like you know engineers uh are

## 67375:00 - 67410:00

are definitely needed. Uh I think that

## 67410:00 - 67435:00

engineers will be able to do much more.

## 67435:00 - 67460:00

I think the demand for software is very

## 67460:00 - 67490:00

lasting which is you know not the most

## 67490:00 - 67540:00

novel thing but I think it's it's kind

## 67540:00 - 67590:00

of crazy to think about how expensive

## 67590:00 - 67645:00

and labor intensive it is to build

## 67645:00 - 67695:00

things that are pretty simple and easy

## 67695:00 - 67730:00

to specify or it would look like it to

## 67730:00 - 67770:00

the outside observer and you know just

## 67770:00 - 67790:00

how hard those things are to do right

## 67790:00 - 67820:00

now and so if you can you know all of

## 67820:00 - 67845:00

the stuff that exists right now that's

## 67845:00 - 67885:00

you know justified by the cost and

## 67885:00 - 67905:00

demand that we have now if you could

## 67905:00 - 67935:00

bring that down by orders of magnitude I

## 67935:00 - 67970:00

we'd have tons and tons and tons of more

## 67970:00 - 67985:00

stuff that we could do our computers,

## 67985:00 - 68035:00

tons more tools. And you know, I've I've

## 68035:00 - 68055:00

felt this where, you know, one of my

## 68055:00 - 68090:00

early jobs actually was working for a

## 68090:00 - 68135:00

biotechnology company and it was

## 68135:00 - 68165:00

building internal tools for them. And

## 68165:00 - 68195:00

the off-the-shelf tools that existed

## 68195:00 - 68240:00

were horrible and did not fit their use

## 68240:00 - 68270:00

case at all. And then the internal tools

## 68270:00 - 68305:00

I was building, there was definitely a

## 68305:00 - 68335:00

ton of demand there uh for things that

## 68335:00 - 68370:00

could be built. And you know, that far

## 68370:00 - 68390:00

outstripped just the things that I could

## 68390:00 - 68410:00

I could build in the time that I was

## 68410:00 - 68460:00

with them. But yes, I think that uh it's

## 68460:00 - 68510:00

still so, you know, the physics of

## 68510:00 - 68540:00

working on computers are so great. It

## 68540:00 - 68565:00

should be able to you should be able to

## 68565:00 - 68590:00

kind of basically just move everything

## 68590:00 - 68615:00

around, do everything that you want to

## 68615:00 - 68645:00

do. There's still so much friction. I

## 68645:00 - 68665:00

think that there's much more demand for

## 68665:00 - 68700:00

the software than uh for software than

## 68700:00 - 68740:00

what we can build today with, you know,

## 68740:00 - 68765:00

things costing like a blockbuster movie

## 68765:00 - 68790:00

to make kind of simple productivity

## 68790:00 - 68815:00

software. And so I think long into the

## 68815:00 - 68835:00

future, yes, there will actually be more

## 68835:00 - 68865:00

demand for engineers. Is there anything

## 68865:00 - 68900:00

that we didn't cover that you wanted to

## 68900:00 - 68925:00

mention? any last nugget of wisdom you

## 68925:00 - 68955:00

wanted to leave listeners with. You

## 68955:00 - 68985:00

could also say no because we've done a

## 68985:00 - 69050:00

lot. We think a lot about uh

## 69050:00 - 69125:00

how how you set up a a team to be able

## 69125:00 - 69175:00

to make new stuff in addition to like

## 69175:00 - 69205:00

continuing to improve the stuff that you

## 69205:00 - 69235:00

have right now. And I think if we're to

## 69235:00 - 69270:00

be successful like the ID is going to

## 69270:00 - 69300:00

have to change a ton. What for like

## 69300:00 - 69315:00

looks like it's going to have to change

## 69315:00 - 69370:00

a ton going into the future. And um you

## 69370:00 - 69420:00

know if you look around uh the the

## 69420:00 - 69445:00

companies we respect there are

## 69445:00 - 69475:00

definitely examples of companies that

## 69475:00 - 69515:00

have continued to really w like you know

## 69515:00 - 69550:00

ride the wave of many leap frogs and

## 69550:00 - 69570:00

continue to kind of actually push the

## 69570:00 - 69645:00

frontier but you know uh they're they're

## 69645:00 - 69675:00

kind of rare too. uh like it's a hard

## 69675:00 - 69730:00

thing to do and um so you know part of

## 69730:00 - 69765:00

that is is just kind of thinking about

## 69765:00 - 69790:00

the thing and trying to reflect on it

## 69790:00 - 69830:00

you know in our day and you know the

## 69830:00 - 69850:00

first principal side of things part of

## 69850:00 - 69875:00

it is also you know trying to get in and

## 69875:00 - 69915:00

and study past examples of of greatness

## 69915:00 - 69980:00

here and um you know that that's that's

## 69980:00 - 70000:00

something that we think about a lot too.

## 70000:00 - 70040:00

Yeah. Yeah. The what you just told is we

## 70040:00 - 70060:00

were before we started recording you had

## 70060:00 - 70080:00

all these books behind you and I was

## 70080:00 - 70105:00

like what's that over there? It's like

## 70105:00 - 70145:00

the history of some old computer company

## 70145:00 - 70165:00

that was influential in a lot of ways

## 70165:00 - 70205:00

that I've never heard of. Uh and I think

## 70205:00 - 70230:00

that says a lot about you of where a lot

## 70230:00 - 70255:00

of this innovation comes from is

## 70255:00 - 70275:00

studying the past and studying history

## 70275:00 - 70325:00

and what's worked and what hasn't. Okay.

## 70325:00 - 70345:00

Uh where can folks find online if they

## 70345:00 - 70365:00

want to reach out and maybe apply? You

## 70365:00 - 70390:00

said that there may be roles you they

## 70390:00 - 70425:00

may not even be aware of. Where do they

## 70425:00 - 70450:00

go find that? And then how can listeners

## 70450:00 - 70500:00

be useful to you? Yeah. I you know if if

## 70500:00 - 70540:00

folks are um you know interested in

## 70540:00 - 70560:00

working on this stuff would would love

## 70560:00 - 70615:00

to speak and uh they can find uh if they

## 70615:00 - 70640:00

go to kers.com they can kind of both

## 70640:00 - 70665:00

find the product and find out how to

## 70665:00 - 70725:00

reach us. So easy Michael thank you so

## 70725:00 - 70735:00

much for being here. This was

## 70735:00 - 70800:00

incredible. Wonderful. Thank you. Bye

## 70800:00 - 70830:00

everyone. Thank you so much for

## 70830:00 - 70860:00

listening. If you found this valuable

## 70860:00 - 70890:00

you can subscribe to the show on Apple

## 70890:00 - 70925:00

Podcasts, Spotify or your favorite

## 70925:00 - 70965:00

podcast app. Also, please consider

## 70965:00 - 71000:00

giving us a rating or leaving a review

## 71000:00 - 71030:00

as that really helps other listeners

## 71030:00 - 71070:00

find the podcast. You can find all past

## 71070:00 - 71125:00

episodes or learn more about the show at

## 71125:00 - 71155:00

lennispodcast.com. See you in the next

## 71155:00+

episode.

