---
source: https://www.youtube.com/watch?v=qhSHbBF4mEg
title: "The GPU Gold Rush: How Vast.ai Scaled With AI Demand"
author: ProductLed
date: 2026-03-27
views: 114
description: |-
  In this episode of the ProductLed Podcast, Wes Bush and Esben Friis-Jensen sit down with Travis Cannell, CEO and first employee at Vast.ai, the marketplace for on-demand, low-cost GPUs powering AI workloads around the world.

  Travis breaks down one of the biggest shifts happening in AI right now: the rise of inference. He explains why inference demand is exploding, how that shift is fueling Vast.ai’s rapid growth, and why more teams are looking for flexible, affordable GPU access outside of traditional cloud platforms.

  The conversation also gets into how Vast.ai built a two-sided GPU marketplace with 20,000 GPUs, why its pricing model creates powerful marketplace dynamics, and what makes its software-first approach difficult to replicate. Travis shares how the company thinks about competition, customer support, GPU hosting economics, and why winning in a fast-growing marketplace depends on much more than just low prices.

  They also explore how AI is changing org design inside high-growth companies. Travis talks candidly about pausing hiring, using AI to accelerate engineering work, and why Vast.ai has leaned into an in-office culture while staying extremely lean.

  If you want a clearer picture of where AI infrastructure is heading, and how one company is scaling quickly with a software-first model, this episode is packed with insight. 

  Key Highlights:
  02:34 - Why Inference Is Fueling the Next AI Boom
  04:15 - Inference Explained in Plain English
  06:15 - The Moment Vast.ai Hit Hypergrowth
  10:04 - Why Teams Choose Vast Over AWS
  12:34 - Building a Two-Sided GPU Marketplace
  17:03 - Competing on More Than Just Price
  18:52 - The Real Economics of Hosting GPUs
  25:21 - The Network Effects Behind Vast.ai
  31:31 - Building a Lean Team During Hypergrowth
  36:09 - Why AI Changed Their Hiring Strategy

  Resources:
  🚀 Vast.ai: Marketplace for low-cost GPUs: https://vast.ai
  💼 Connect with Travis Cannell on LinkedIn: https://www.linkedin.com/in/traviscannell/
  💼 Connect with Wes Bush on LinkedIn: https://www.linkedin.com/in/wesbush/
  💼 Connect with Esben Friis-Jensen on LinkedIn: https://www.linkedin.com/in/esbenfriisjensen/
  📚 Read the interview summary: https://productled.com/blog/the-gpu-gold-rush-how-vast-ai-scaled-with-ai-demand
  🎧 Listen on Spotify: https://open.spotify.com/episode/30jPfkEmBbfTItbTnM7Ime?si=573af9d5d7294a2a
  🎧 Listen on Apple Music: https://podcasts.apple.com/us/podcast/the-gpu-gold-rush-how-vast-ai-scaled-with-ai-demand/id1491416462?i=1000757664204
  🧠 Sign up for the ProductLed Newsletter: https://www.productled.com/newsletter
tags:
  - vast.ai
  - GPU marketplace
  - AI infrastructure
  - AI inference
  - cloud GPU
  - on-demand GPU
  - low-cost GPUs
  - AI workloads
  - AWS alternative
  - GPU hosting
  - AI compute
  - machine learning infrastructure
  - two-sided marketplace
  - network effects
  - startup hypergrowth
  - software-first model
  - Travis Cannell
  - Wes Bush
  - Esben Friis-Jensen
  - ProductLed Podcast
extraction_method: youtube-transcript
grabbed_at: 2026-04-02T10:35:54.868Z
---

# The GPU Gold Rush: How Vast.ai Scaled With AI Demand

## 00:00 - 55:00

We're having like a a chat GPT30

## 55:00 - 80:00

moment, but it's bigger.

## 80:00 - 100:00

>> I'm sure there's going to be other

## 100:00 - 130:00

players that will try and definitely

## 130:00 - 155:00

disrupt to you. Whether it's like, hey,

## 155:00 - 215:00

we have all our GPUs in a country where

## 215:00 - 230:00

energy is really cheap.

## 230:00 - 265:00

>> Bring it on. Let's compete, right? I

## 265:00 - 305:00

mean, price is important, but everything

## 305:00 - 340:00

else I was touching on is very important

## 340:00 - 380:00

as well. the customer service, the

## 380:00 - 410:00

platform experience, the way the

## 410:00 - 445:00

templates work, each and everything,

## 445:00 - 470:00

each and every piece of the software

## 470:00 - 495:00

kind of all has to come together for the

## 495:00 - 510:00

customer to have a really good

## 510:00 - 520:00

experience.

## 520:00 - 550:00

>> So, you're basically the Airbnb for

## 550:00 - 565:00

renting GPA.

## 565:00 - 605:00

>> We are. And I think we used that tagline

## 605:00 - 635:00

for a while when everyone was talking

## 635:00 - 675:00

about the sharing economy. We thought

## 675:00 - 700:00

that Ethereum was going to be a big

## 700:00 - 725:00

driver of that, moving to proof of

## 725:00 - 765:00

stake, but it just really didn't matter

## 765:00 - 905:00

because this massive thing of inference.

## 905:00 - 940:00

Welcome to the product podcast. With me

## 940:00 - 980:00

today, I have my co-host Esben who is

## 980:00 - 1010:00

entrepreneur residents at productled and

## 1010:00 - 1050:00

she was the co-founder user flow and

## 1050:00 - 1095:00

cobalt. And today's guest is Travis

## 1095:00 - 1135:00

Canalo. He is the COO and first employee

## 1135:00 - 1180:00

at mass.ai AI, which is a marketplace

## 1180:00 - 1225:00

for ondemand lowcost GPUs as to power

## 1225:00 - 1260:00

all of your AI solutions. And so the

## 1260:00 - 1305:00

company is on a tear. They're on the uh

## 1305:00 - 1345:00

Brex 50 fastest growing companies. And

## 1345:00 - 1370:00

that's how we we found out about them.

## 1370:00 - 1390:00

Then we started signing up for their

## 1390:00 - 1405:00

product. We're like, "Okay, this is

## 1405:00 - 1435:00

cool. I can see why this is the case."

## 1435:00 - 1460:00

So Travis, it's awesome to have you

## 1460:00 - 1490:00

here. Thanks so much for coming on.

## 1490:00 - 1510:00

>> Yeah, I'm really happy to be here as

## 1510:00 - 1535:00

well. And uh talk a little bit more

## 1535:00 - 1550:00

about the vast story.

## 1550:00 - 1580:00

>> Awesome. And like we were going through

## 1580:00 - 1600:00

some of the stats as well. I know. I

## 1600:00 - 1630:00

think was it like last February as well?

## 1630:00 - 1675:00

You had like 19,000 signups for for

## 1675:00 - 1685:00

Bast.

## 1685:00 - 1720:00

>> Yeah, it's been growing a lot. I think

## 1720:00 - 1770:00

we're at 27x year-over-year growth. The

## 1770:00 - 1795:00

last time I was looking at this for

## 1795:00 - 1850:00

signups, so, you know, 19,000 in

## 1850:00 - 1890:00

February alone is what we put out in our

## 1890:00 - 1930:00

blog post. And that's starting to even

## 1930:00 - 1960:00

pick up even more as we get into March.

## 1960:00 - 1995:00

But there's a lot of people interested

## 1995:00 - 2030:00

in GPUs now. And, you know, we're here

## 2030:00 - 2065:00

to we're here for it. as you were saying

## 2065:00 - 2105:00

like you've done an amazing job on and

## 2105:00 - 2135:00

we can dive more into this but on like

## 2135:00 - 2185:00

getting referrals from whether it's trad

## 2185:00 - 2210:00

cloud all these different places where

## 2210:00 - 2255:00

if you want to rent a GPU vasti is doing

## 2255:00 - 2285:00

a fantastic job of becoming that number

## 2285:00 - 2310:00

one place where it's like okay great you

## 2310:00 - 2345:00

can learn about it and then test it out

## 2345:00 - 2370:00

pretty easily but what do you think is

## 2370:00 - 2405:00

driving this crazy growth is it just

## 2405:00 - 2465:00

LLMs that are referring fasti or is it

## 2465:00 - 2515:00

some other need here that is now more

## 2515:00 - 2545:00

than ever omnipresent where People are

## 2545:00 - 2580:00

like, I need to rent a GPU for this.

## 2580:00 - 2615:00

>> Yeah, I think it's inference. Over the

## 2615:00 - 2655:00

last couple years, there was this idea,

## 2655:00 - 2680:00

you know, all this money is pouring into

## 2680:00 - 2715:00

training and it still is. These data

## 2715:00 - 2750:00

center builds out these massive

## 2750:00 - 2800:00

Infiniban clusters. There were 4,000

## 2800:00 - 2845:00

8,000 I think this Colossus one is over

## 2845:00 - 2925:00

100,000 GPUs. So that is capex and

## 2925:00 - 2975:00

expense that goes to training. And

## 2975:00 - 3030:00

there's to get money back though you

## 3030:00 - 3055:00

need to take that model and you need to

## 3055:00 - 3095:00

run inference on it. And so that comes

## 3095:00 - 3160:00

out as a cog and inference is really you

## 3160:00 - 3225:00

know allowing the model to live and

## 3225:00 - 3250:00

these

## 3250:00 - 3280:00

ways that the models now and like claude

## 3280:00 - 3310:00

code kind of lays it out bare with its

## 3310:00 - 3340:00

context. it really starts to feel a

## 3340:00 - 3375:00

little bit more humanlike like it okay

## 3375:00 - 3405:00

it can you can talk to it for this long

## 3405:00 - 3445:00

and then it needs to go to sleep and

## 3445:00 - 3480:00

then you get a fresh one that doesn't

## 3480:00 - 3510:00

quite remember everything but the

## 3510:00 - 3555:00

inference is very important so for a

## 3555:00 - 3595:00

while we've been thinking about that and

## 3595:00 - 3650:00

inference is driving this and inference

## 3650:00 - 3695:00

in my mind is just going to continue to

## 3695:00 - 3750:00

explode as we not only want to run the

## 3750:00 - 3790:00

artificial models but as more and more

## 3790:00 - 3855:00

we take living things and digitally

## 3855:00 - 3890:00

recreate them. If you can imagine the

## 3890:00 - 3915:00

three of us, I think I want to run

## 3915:00 - 3945:00

inference on my mind. And there's quite

## 3945:00 - 3975:00

a few humans that probably want to run

## 3975:00 - 4015:00

inference on their minds.

## 4015:00 - 4045:00

>> Millions of people that want that. Now,

## 4045:00 - 4085:00

just to ask a dumb question here. So,

## 4085:00 - 4105:00

for some people that are listening,

## 4105:00 - 4145:00

they're like, "Okay, what is inference?"

## 4145:00 - 4165:00

Before we get too much deeper, could you

## 4165:00 - 4205:00

just like kind of give the the high

## 4205:00 - 4240:00

level overview so somebody's not lost at

## 4240:00 - 4255:00

this point?

## 4255:00 - 4285:00

>> Yeah, let's back up for a second. I mean

## 4285:00 - 4315:00

when you train the model you're making

## 4315:00 - 4350:00

the model weights it's really a

## 4350:00 - 4400:00

production step. So training is

## 4400:00 - 4435:00

something that takes these massive data

## 4435:00 - 4470:00

centers. They all need to be wired

## 4470:00 - 4515:00

together. It is a very intensive process

## 4515:00 - 4580:00

where this cluster will run for months

## 4580:00 - 4650:00

at a time and the output of that is a is

## 4650:00 - 4685:00

a model. That's kind of what you're

## 4685:00 - 4715:00

talking to when you pick a model with

## 4715:00 - 4750:00

chat GPT when you pick a model with

## 4750:00 - 4780:00

claude. Everyone's talking about opus

## 4780:00 - 4830:00

4.6 six that's a model you know sonnet

## 4830:00 - 4870:00

is a model chatbt has its five series

## 4870:00 - 4910:00

that's a model so those were trained and

## 4910:00 - 4955:00

then there's a a step where they're

## 4955:00 - 4985:00

fine-tuned

## 4985:00 - 5030:00

and there's feedback with actual humans

## 5030:00 - 5050:00

they're worked through until they're

## 5050:00 - 5085:00

actually get ready to talk to actual

## 5085:00 - 5145:00

people but the model itself you cannot

## 5145:00 - 5175:00

talk to it if it's just sitting at a

## 5175:00 - 5210:00

file on your computer it doesn't work

## 5210:00 - 5235:00

what you need is you need to take that

## 5235:00 - 5265:00

model and you need to load it into the

## 5265:00 - 5290:00

RAM of a GPU

## 5290:00 - 5340:00

and then you can talk to it. So when

## 5340:00 - 5365:00

you're talking to this model, every time

## 5365:00 - 5410:00

you prompt a model, it is running on a

## 5410:00 - 5450:00

GPU somewhere. And that's very different

## 5450:00 - 5485:00

from training. When the model is running

## 5485:00 - 5515:00

on this GPU, it doesn't require

## 5515:00 - 5560:00

Infiniband. Sometimes you can compress

## 5560:00 - 5575:00

the model and there's different

## 5575:00 - 5610:00

optimization steps so you can get it

## 5610:00 - 5650:00

running on a smaller footprint. That's

## 5650:00 - 5685:00

called quantization. And that's a big

## 5685:00 - 5715:00

area of active research. A lot of these

## 5715:00 - 5740:00

open source models, they keep on trying

## 5740:00 - 5780:00

to squeeze them down so you can run them

## 5780:00 - 5865:00

on a 32 GB GPU, maybe even smaller. But

## 5865:00 - 5905:00

inference, you can just think of when

## 5905:00 - 5930:00

you're talking to the model, when you're

## 5930:00 - 5965:00

prompting, when you're in an interactive

## 5965:00 - 6005:00

session, this model is is running

## 6005:00 - 6070:00

somewhere. It's alive. Inference is

## 6070:00 - 6105:00

life. Thanks for for jumping in there,

## 6105:00 - 6140:00

our ends. Just to give a little bit more

## 6140:00 - 6175:00

context, that's always super helpful.

## 6175:00 - 6215:00

Now, when it comes to like when did

## 6215:00 - 6260:00

vast.ai go into like hyperrowth mode.

## 6260:00 - 6285:00

When was that like pivotal moment for

## 6285:00 - 6300:00

you and the team where you're like, "Oh

## 6300:00 - 6340:00

my goodness, like this is taking off uh

## 6340:00 - 6370:00

things are growing every single month."

## 6370:00 - 6395:00

Like when did that kind of happen for

## 6395:00 - 6400:00

you?

## 6400:00 - 6425:00

>> It's interesting. I mean, Vast launched

## 6425:00 - 6500:00

in in 2018. I came on in about 2022

## 6500:00 - 6540:00

and we've always been about doubling on

## 6540:00 - 6585:00

a trajectory, sort of the long-term kind

## 6585:00 - 6625:00

of doubling with some deviations from

## 6625:00 - 6660:00

that along the way. But it it was really

## 6660:00 - 6690:00

around November that we started to see

## 6690:00 - 6730:00

things kind of heat up and now it's

## 6730:00 - 6785:00

going crazy. Just in February, March

## 6785:00 - 6815:00

there is something happening and it's

## 6815:00 - 6840:00

happening kind of right now. It's really

## 6840:00 - 6905:00

2026 is looking a to be a lot different.

## 6905:00 - 6940:00

I mean on my team from what I can see on

## 6940:00 - 6990:00

the ground it was Opus 4.6 and Claude

## 6990:00 - 7030:00

Code. there's some sort of combination

## 7030:00 - 7100:00

where we're having like a a chat GPT30

## 7100:00 - 7150:00

moment and but it's bigger it's bigger

## 7150:00 - 7170:00

this time and

## 7170:00 - 7195:00

>> is it just that more people are like

## 7195:00 - 7230:00

coding and they're like hey I need ICU

## 7230:00 - 7280:00

more GPU power and like okay great I

## 7280:00 - 7315:00

fast just so happens to be the tool I

## 7315:00 - 7340:00

need in that equation

## 7340:00 - 7375:00

>> you know I mean this is all happening so

## 7375:00 - 7395:00

fast that we're still trying to kind of

## 7395:00 - 7435:00

figure out and sort through exactly what

## 7435:00 - 7465:00

we're seeing and we're a worldwide

## 7465:00 - 7500:00

company so North America America isn't

## 7500:00 - 7555:00

even really our biggest market. So we

## 7555:00 - 7605:00

have a lot of users in APAC, Europe.

## 7605:00 - 7640:00

It's a worldwide phenomenon where people

## 7640:00 - 7670:00

are are coming and and you know wanting

## 7670:00 - 7710:00

to rent GPUs for different things.

## 7710:00 - 7745:00

Experimentation, fine-tuning,

## 7745:00 - 7780:00

fine-tuning models on their own data.

## 7780:00 - 7820:00

Then of course running models in a more

## 7820:00 - 7865:00

private way is important to a lot of

## 7865:00 - 7905:00

people. So we do see some of the

## 7905:00 - 7945:00

templates that are popular. There's a

## 7945:00 - 7970:00

lot of image generation, video

## 7970:00 - 7995:00

generation. The video generation

## 7995:00 - 8040:00

requires a lot more compute for the

## 8040:00 - 8080:00

given output of videos. So, there's

## 8080:00 - 8130:00

these companies out there that are

## 8130:00 - 8155:00

fine-tuning models, you know, for

## 8155:00 - 8205:00

specific video type purposes. I think

## 8205:00 - 8245:00

that's really exploding and taking off.

## 8245:00 - 8265:00

But it's just one of those things where

## 8265:00 - 8305:00

it's hard to like a frog boiling like

## 8305:00 - 8340:00

suddenly we're boiling and you you know

## 8340:00 - 8380:00

you're wondering how we really got here

## 8380:00 - 8430:00

and it's it's hard to know for sure but

## 8430:00 - 8455:00

it just it seems like it's coming

## 8455:00 - 8480:00

there's a lot of different things all

## 8480:00 - 8520:00

coming together and then on the LLM

## 8520:00 - 8550:00

front there's a lot of people that are

## 8550:00 - 8605:00

there's new use cases opening up and as

## 8605:00 - 8635:00

things get cheaper you know we expect

## 8635:00 - 8675:00

that to accelerate as well. I forget the

## 8675:00 - 8710:00

name of the law, but as things get

## 8710:00 - 8750:00

cheaper, they become more useful and

## 8750:00 - 8790:00

then people use them more. So, it's this

## 8790:00 - 8825:00

kind of weird paradox that you hit.

## 8825:00 - 8855:00

>> Yeah. And I also think like this goes

## 8855:00 - 8910:00

back to what is happening in even just

## 8910:00 - 8945:00

development too with like cloud code and

## 8945:00 - 8965:00

everything else here too. It's like

## 8965:00 - 8990:00

there if you look at the total

## 8990:00 - 9020:00

adjustable market, there's like the very

## 9020:00 - 9055:00

small amount that is just builders. They

## 9055:00 - 9085:00

they know how to code. They they can do

## 9085:00 - 9100:00

everything. They understand the

## 9100:00 - 9130:00

complexities of how to build it all.

## 9130:00 - 9160:00

Very small part of the market. And now

## 9160:00 - 9200:00

it's it's like the bigger part is

## 9200:00 - 9235:00

editors. It's everybody else who can

## 9235:00 - 9265:00

just prompt and figure out, hey, this is

## 9265:00 - 9290:00

how I want to describe something and

## 9290:00 - 9345:00

they're like, I can code now. And that

## 9345:00 - 9390:00

size of the market is 10x what the

## 9390:00 - 9425:00

builder one was. So that's why we're

## 9425:00 - 9450:00

seeing a lot of these AI companies just

## 9450:00 - 9490:00

like explode because they're actually

## 9490:00 - 9555:00

the TAM is way bigger and way deeper

## 9555:00 - 9585:00

than than anything they've ever seen

## 9585:00 - 9620:00

before in that same market. So it gives

## 9620:00 - 9650:00

the illusion of like wow they're just do

## 9650:00 - 9675:00

like on this breakout fro like

## 9675:00 - 9710:00

trajectory but like the same person that

## 9710:00 - 9740:00

uses like a lovable is not going to be

## 9740:00 - 9785:00

using somebody like like an IDE the kind

## 9785:00 - 9810:00

of like code because they're like I

## 9810:00 - 9845:00

don't quite get it but now it's like

## 9845:00 - 9880:00

that's they can't because they just plug

## 9880:00 - 9910:00

in with clock they're good to go. So

## 9910:00 - 9950:00

that's fascinating. Now why would you

## 9950:00 - 9995:00

say AI teams choose fast instead of like

## 9995:00 - 10050:00

AWS or other alternatives like Lambda

## 10050:00 - 10095:00

Labs or or some other pieces here? Yeah,

## 10095:00 - 10125:00

I think that's a really good question.

## 10125:00 - 10155:00

You know, it's I think a lot of it boils

## 10155:00 - 10205:00

down to cost. So, we're trying to build

## 10205:00 - 10245:00

ourselves as the most efficient solution

## 10245:00 - 10300:00

for inference and basically have created

## 10300:00 - 10360:00

this this system where we have all these

## 10360:00 - 10405:00

different hosting partners that are

## 10405:00 - 10430:00

setting their own prices. They're

## 10430:00 - 10450:00

listing their own equipment. They're

## 10450:00 - 10485:00

making their own claims about, you know,

## 10485:00 - 10525:00

what this equipment is and how good it's

## 10525:00 - 10560:00

going to be. And then we sort of verify

## 10560:00 - 10615:00

everything. So, we verify the equipment

## 10615:00 - 10645:00

is kind of what they say it is and then

## 10645:00 - 10680:00

we test the bandwidth and everything,

## 10680:00 - 10715:00

but we're trying to keep it very minimal

## 10715:00 - 10745:00

and bare bones. And we don't own the

## 10745:00 - 10785:00

equipment ourselves. So, our platform

## 10785:00 - 10830:00

tends to have the lowest prices for each

## 10830:00 - 10835:00

GPU.

## 10835:00 - 10865:00

>> So, you're basically the Airbnb for

## 10865:00 - 10885:00

renting GPUs.

## 10885:00 - 10925:00

>> We are, and I think we used that tagline

## 10925:00 - 10955:00

for a while when everyone was talking

## 10955:00 - 10990:00

about the sharing economy and when the

## 10990:00 - 11025:00

sharing economy was really cool. And a

## 11025:00 - 11060:00

lot of those too we've we've moved into

## 11060:00 - 11100:00

data center operators, what we call data

## 11100:00 - 11135:00

center operators. We have a blue label

## 11135:00 - 11190:00

on our on some of the offers and those

## 11190:00 - 11250:00

are run by reputable data centers that

## 11250:00 - 11290:00

have more equipment. Many times they

## 11290:00 - 11335:00

have the certifications and so those are

## 11335:00 - 11390:00

kind of for more for serious production

## 11390:00 - 11420:00

workloads. And then we have kind of the

## 11420:00 - 11470:00

longer tail as well. I think our median

## 11470:00 - 11515:00

kind of host might just have a dozen

## 11515:00 - 11570:00

GPUs. Oftentimes they put them in a data

## 11570:00 - 11600:00

center as well. But there's kind of

## 11600:00 - 11640:00

these it's an entrepreneurial class that

## 11640:00 - 11685:00

has been running and managing GPUs and

## 11685:00 - 11710:00

they don't want to do customer service

## 11710:00 - 11750:00

because customer service is difficult

## 11750:00 - 11785:00

and they don't want to do marketing and

## 11785:00 - 11830:00

they don't want to deal with business.

## 11830:00 - 11880:00

So, it's like, can I just buy this

## 11880:00 - 11915:00

equipment and then, yeah, can I just buy

## 11915:00 - 11945:00

this equipment and get some money? And

## 11945:00 - 11985:00

we're like, yeah, you can just come to

## 11985:00 - 12035:00

Vast, list it with us. You can control a

## 12035:00 - 12075:00

lot. You can control the price that you

## 12075:00 - 12120:00

want. You can control the terms if you

## 12120:00 - 12145:00

want to rent it on interruptible, if you

## 12145:00 - 12180:00

want to rent it on demand, how long, you

## 12180:00 - 12205:00

know, as as the owner of the equipment,

## 12205:00 - 12250:00

you can determine a a term, which is

## 12250:00 - 12270:00

kind of important. like do you want to

## 12270:00 - 12305:00

list it for six months, one month? Do

## 12305:00 - 12335:00

you need it back next week? Maybe you

## 12335:00 - 12370:00

only list it for a week. Probably can't

## 12370:00 - 12390:00

get the highest price if you're only

## 12390:00 - 12425:00

going to list it for a week. But, you

## 12425:00 - 12470:00

know, we we want to create liquidity

## 12470:00 - 12540:00

around people trading compute and coming

## 12540:00 - 12580:00

to terms for compute. So, that's always

## 12580:00 - 12590:00

been the goal.

## 12590:00 - 12620:00

>> You you basically have a two-sided

## 12620:00 - 12645:00

marketplace, right? But and it sounds

## 12645:00 - 12710:00

like you are offering your suppliers

## 12710:00 - 12755:00

and you take away some of their the work

## 12755:00 - 12780:00

they don't like to do and then you have

## 12780:00 - 12820:00

the demand which is there due to the

## 12820:00 - 12870:00

whole AI boom. So I I assume it's been

## 12870:00 - 12900:00

harder to build the supply side up

## 12900:00 - 12945:00

though than the demand side or or has

## 12945:00 - 12975:00

that changed over the years? Was it

## 12975:00 - 13010:00

initially the demand side that was hard

## 13010:00 - 13060:00

and now it's the easy part or how has

## 13060:00 - 13075:00

that been?

## 13075:00 - 13120:00

>> Yeah, you know it it switches. it it

## 13120:00 - 13150:00

kind of it kind of comes and goes is

## 13150:00 - 13185:00

what is harder. I think at the end of

## 13185:00 - 13220:00

the day there's only one side that's

## 13220:00 - 13255:00

inputting money into the system. So we

## 13255:00 - 13290:00

tend to focus on that and that tends to

## 13290:00 - 13330:00

be sometimes the harder scenario. The

## 13330:00 - 13375:00

way that our system works because the

## 13375:00 - 13430:00

owners of the equipment can list offers.

## 13430:00 - 13465:00

They can raise their price as they see

## 13465:00 - 13505:00

the availability dry up. Like any good

## 13505:00 - 13570:00

market system, that is a signal. It's a

## 13570:00 - 13620:00

signal to invest, get more compute,

## 13620:00 - 13665:00

bring on more capacity, maybe grab a

## 13665:00 - 13695:00

couple machines that you had sitting on

## 13695:00 - 13720:00

some other platform or you had that

## 13720:00 - 13760:00

weren't earning as much. There's other

## 13760:00 - 13790:00

ones out there where they don't let you.

## 13790:00 - 13820:00

They tell you how much they'll they'll

## 13820:00 - 13865:00

pay you. They don't have that kind of

## 13865:00 - 13925:00

very fast market based signaling. And

## 13925:00 - 13960:00

so, you know, our hosting partners tend

## 13960:00 - 14010:00

to expand. They have a great retention

## 14010:00 - 14060:00

and expansion kind of metric. So they

## 14060:00 - 14095:00

reinvest with us when they start to earn

## 14095:00 - 14130:00

more too. They buy more equipment. So on

## 14130:00 - 14165:00

that side, a lot of it is helping them.

## 14165:00 - 14185:00

We're getting into that more and more.

## 14185:00 - 14215:00

Helping them with potential financial

## 14215:00 - 14255:00

partners, potential partners to buy

## 14255:00 - 14315:00

compute where we know there is

## 14315:00 - 14360:00

refurbished servers, things like that at

## 14360:00 - 14380:00

good prices. We're trying to get into

## 14380:00 - 14410:00

that more and more with our sales team

## 14410:00 - 14445:00

to help those suppliers. But I think

## 14445:00 - 14480:00

both sides of the market have their

## 14480:00 - 14525:00

complexities and difficulties. But the

## 14525:00 - 14560:00

demand side, you know, is quite

## 14560:00 - 14600:00

difficult. And you have all these users

## 14600:00 - 14635:00

that have AWS

## 14635:00 - 14680:00

expectations in terms of how stuff

## 14680:00 - 14730:00

should work and, you know, want to pay

## 14730:00 - 14805:00

you $5. So, it's quite a lift to get a

## 14805:00 - 14850:00

24/7 support team running to deal with

## 14850:00 - 14920:00

questions coming in from Apac on Friday

## 14920:00 - 14965:00

night when you're trying to go get some

## 14965:00 - 15015:00

dinner and pack up for the week, you

## 15015:00 - 15045:00

know, and then over the weekend, it's

## 15045:00 - 15065:00

just really, you know, people

## 15065:00 - 15090:00

experimenting and playing with these

## 15090:00 - 15125:00

things all the time. So that's certainly

## 15125:00 - 15180:00

if I look at our team, there's a lot

## 15180:00 - 15235:00

faced that client experience and making

## 15235:00 - 15270:00

sure they have someone to talk to, you

## 15270:00 - 15315:00

know, and how to set up an SSH key

## 15315:00 - 15350:00

because a lot of people don't know how

## 15350:00 - 15385:00

to do that.

## 15385:00 - 15425:00

So they see step one is I need an SSH

## 15425:00 - 15460:00

key. Okay, so do I get that from you or

## 15460:00 - 15485:00

where is that? and you're like, "Okay,

## 15485:00 - 15530:00

we, you know, we have a lot of Linux

## 15530:00 - 15585:00

training that we like to do at Vast for

## 15585:00 - 15610:00

someone that's trying to do something

## 15610:00 - 15650:00

quite complicated, typically more

## 15650:00 - 15685:00

complicated than might be the more

## 15685:00 - 15705:00

something more technical than they've

## 15705:00 - 15745:00

done before. So anyways, that's a very

## 15745:00 - 15785:00

long winded answer to your question, but

## 15785:00 - 15810:00

hopefully kind of covers most of the

## 15810:00 - 15860:00

bases, but I do think over my four

## 15860:00 - 15900:00

years. It's been the customer side

## 15900:00 - 15940:00

that's like more important and harder in

## 15940:00 - 15980:00

a certain way because they're giving us

## 15980:00 - 16015:00

the money. Our hosts, they're our

## 16015:00 - 16050:00

partners. They're incredibly important,

## 16050:00 - 16085:00

but they're not our customers. You can

## 16085:00 - 16125:00

always ask a very simple question. Who's

## 16125:00 - 16145:00

giving you money? You know, if

## 16145:00 - 16165:00

somebody's like, "Hey, I'm your

## 16165:00 - 16190:00

customer." You got to do what I say. And

## 16190:00 - 16215:00

it's like, wait, am I giving you money

## 16215:00 - 16250:00

or are you giving me money? Because

## 16250:00 - 16285:00

who's ever paying, you know, they're the

## 16285:00 - 16310:00

customer is always right, but that's the

## 16310:00 - 16345:00

person that you really want to to help

## 16345:00 - 16385:00

and understand deeply what problems

## 16385:00 - 16410:00

they're having with the platform and

## 16410:00 - 16435:00

track all that and make sure that

## 16435:00 - 16470:00

they're having a really good experience.

## 16470:00 - 16505:00

Um, and so that's been quite something

## 16505:00 - 16540:00

to set up that support team for them and

## 16540:00 - 16575:00

and try to deal with everyone from that

## 16575:00 - 16620:00

$5 customer that's somebody in India

## 16620:00 - 16650:00

just trying to run a model all the way

## 16650:00 - 16680:00

up to somebody running a production

## 16680:00 - 16720:00

workload at scale that's relying on us

## 16720:00 - 16745:00

you know for their business.

## 16745:00 - 16795:00

>> If we look at your website like the main

## 16795:00 - 16835:00

moat we kind of like were thinking is

## 16835:00 - 16865:00

like hey it's definitely it's cheaper

## 16865:00 - 16890:00

price than the competition. That's the

## 16890:00 - 16920:00

the one you definitely beat a lot with.

## 16920:00 - 16950:00

Is that something you'd agree with? like

## 16950:00 - 16975:00

how are you planning on defending this

## 16975:00 - 17025:00

moat in the future especially since it's

## 17025:00 - 17070:00

definitely the hot hot market to be in

## 17070:00 - 17090:00

and I'm sure there's going to be other

## 17090:00 - 17130:00

players that uh will will try and

## 17130:00 - 17160:00

definitely disrupt you whether it's like

## 17160:00 - 17210:00

hey we have all our GPUs in a country

## 17210:00 - 17245:00

where energy is really cheap or

## 17245:00 - 17260:00

something like that where they can

## 17260:00 - 17300:00

actually compete on price and it could

## 17300:00 - 17325:00

be a little harder to do that even with

## 17325:00 - 17345:00

a distributed network

## 17345:00 - 17370:00

>> you know I always say bring it on let's

## 17370:00 - 17425:00

compete right I mean price is important

## 17425:00 - 17455:00

but everything else I was touching on is

## 17455:00 - 17495:00

very important as well. The customer

## 17495:00 - 17540:00

service, the platform experience, the

## 17540:00 - 17580:00

way the templates work. I mean, each and

## 17580:00 - 17605:00

everything, each and every piece of the

## 17605:00 - 17630:00

software kind of all has to come

## 17630:00 - 17650:00

together for the customer to have a

## 17650:00 - 17675:00

really good experience. There's been

## 17675:00 - 17725:00

competition since 2018. Competition is

## 17725:00 - 17745:00

just a sign that it's a healthy

## 17745:00 - 17790:00

marketplace. And I think the key is

## 17790:00 - 17830:00

moving fast and, you know, trying to

## 17830:00 - 17865:00

stay ahead of the competition. And we

## 17865:00 - 17905:00

will have a new version of our website

## 17905:00 - 17935:00

out very soon.

## 17935:00 - 17985:00

that focuses on the pricing of our GPUs.

## 17985:00 - 18015:00

It's quite interesting. We have a lot of

## 18015:00 - 18065:00

pricing data. So, we'll start publishing

## 18065:00 - 18155:00

a lot of the 30, 90, and 180 day pricing

## 18155:00 - 18200:00

for each GPU type, which I think is a

## 18200:00 - 18235:00

cool thing for the lay person to kind of

## 18235:00 - 18260:00

monitor and look at. If you're in this

## 18260:00 - 18295:00

industry, you want to understand what's

## 18295:00 - 18340:00

going on with B200 or H100 pricing or

## 18340:00 - 18375:00

even 5090 pricing. We'll publish that a

## 18375:00 - 18425:00

little bit more and move a little bit

## 18425:00 - 18460:00

away from comparing ourselves to so many

## 18460:00 - 18505:00

other competitors because I think the

## 18505:00 - 18540:00

pricing kind of speaks for itself. And

## 18540:00 - 18565:00

the way I think about it now is more of

## 18565:00 - 18610:00

an efficiency angle for inference.

## 18610:00 - 18640:00

>> Yeah, that's good. And when it comes to

## 18640:00 - 18695:00

the unit economics of like a single GPU

## 18695:00 - 18730:00

that gets hosted on BAS, what does that

## 18730:00 - 18755:00

that look like? Obviously, it will

## 18755:00 - 18795:00

depend on what kind of GPU. Then there's

## 18795:00 - 18825:00

like, you know, I I don't know if it's

## 18825:00 - 18845:00

hundreds or thousands that you have

## 18845:00 - 18900:00

access to, which is thousands. But what

## 18900:00 - 18925:00

does that typically look like for

## 18925:00 - 18960:00

somebody that is, you know, hosting

## 18960:00 - 18990:00

their GPU on fast?

## 18990:00 - 19035:00

>> Yeah, we we actually just had a cake

## 19035:00 - 19115:00

party because we hit 20,000 GPUs. So

## 19115:00 - 19150:00

that's the scale. It was shaped like a

## 19150:00 - 19195:00

5090. So that's if that gives you any

## 19195:00 - 19245:00

hint, our best one. So yeah, the unit

## 19245:00 - 19305:00

economics of owning and and kind of

## 19305:00 - 19345:00

putting something on BAST is a

## 19345:00 - 19390:00

complicated question. I do have an idea

## 19390:00 - 19425:00

for a calculator and some different

## 19425:00 - 19470:00

things, but it's I'll start with some of

## 19470:00 - 19515:00

the things that maybe, you know, most

## 19515:00 - 19550:00

people don't think about. You did

## 19550:00 - 19580:00

mention one of them though, the cost of

## 19580:00 - 19625:00

power. So the cost of power is a pretty

## 19625:00 - 19680:00

big input and you really have to look at

## 19680:00 - 19705:00

the generation of chip and the type of

## 19705:00 - 19750:00

chip to understand how big the power

## 19750:00 - 19800:00

fraction cost is of running it. The

## 19800:00 - 19835:00

later chips are using more and more

## 19835:00 - 19875:00

power. The consumer cards tend to use

## 19875:00 - 19910:00

more power as a as a fraction. Some of

## 19910:00 - 19930:00

the enterprise cards are like a little

## 19930:00 - 19965:00

bit more optimized for power

## 19965:00 - 20000:00

consumption. So the cost of power is

## 20000:00 - 20030:00

pretty big because if you're just going

## 20030:00 - 20065:00

to plug these things into your garage

## 20065:00 - 20105:00

and you're in California, that's going

## 20105:00 - 20140:00

to be tough because you're paying, you

## 20140:00 - 20215:00

know, 25 plus cents per kilowatt and

## 20215:00 - 20280:00

somebody who is in Texas or in Iceland

## 20280:00 - 20330:00

or in a low cost of power place is going

## 20330:00 - 20355:00

to have an immediate pricing advantage

## 20355:00 - 20410:00

over you. So the power cost is a big

## 20410:00 - 20450:00

input. Then the price of the equipment

## 20450:00 - 20495:00

itself. That's going to be your capex.

## 20495:00 - 20550:00

That's an important piece. So the people

## 20550:00 - 20585:00

that are looking at this kind of know

## 20585:00 - 20630:00

the prices of these GPUs pretty well. We

## 20630:00 - 20660:00

don't try to predict the prices of them.

## 20660:00 - 20705:00

I mean I I've been scratching my head

## 20705:00 - 20745:00

for four years in this industry. Like I

## 20745:00 - 20780:00

just remember back as a quick detour

## 20780:00 - 20810:00

story. I remember back when Ethereum was

## 20810:00 - 20860:00

all being mined on GPUs and then they

## 20860:00 - 20880:00

announced they were going to stop mining

## 20880:00 - 20920:00

it on GPUs. And we were just I was

## 20920:00 - 20975:00

thinking, man, oh boy, here comes like a

## 20975:00 - 21010:00

glut of GPUs

## 21010:00 - 21050:00

and prices are going to drop. The price

## 21050:00 - 21085:00

of the GPUs are going to drop and then

## 21085:00 - 21125:00

the and then the the price that we can

## 21125:00 - 21150:00

rent them all for is going to drop. So

## 21150:00 - 21170:00

that's going to affect our bottom line.

## 21170:00 - 21195:00

So we're kind of like preparing mentally

## 21195:00 - 21230:00

for that. And the exact opposite thing

## 21230:00 - 21295:00

happened. The image generation stuff, it

## 21295:00 - 21325:00

was really just landscapes and very

## 21325:00 - 21390:00

bizarre stuff. Couldn't even do people.

## 21390:00 - 21445:00

couldn't even make a face. But, you

## 21445:00 - 21470:00

know, that's kind of where the one of

## 21470:00 - 21500:00

those little booms started and the price

## 21500:00 - 21545:00

of GPUs went in the other direction. I

## 21545:00 - 21575:00

believe those were all like 4090s. So

## 21575:00 - 21600:00

then suddenly you couldn't even buy a

## 21600:00 - 21645:00

4090 and then the prices to rent them

## 21645:00 - 21700:00

actually went you know opposite and we

## 21700:00 - 21745:00

thought that Ethereum was going to be a

## 21745:00 - 21770:00

big driver of that moving to proof of

## 21770:00 - 21810:00

stake but it just really didn't matter

## 21810:00 - 21840:00

because this massive thing of inference

## 21840:00 - 21865:00

you know that was coming that was the

## 21865:00 - 21910:00

first little little wave of that so and

## 21910:00 - 21930:00

then to get back kind of the unit

## 21930:00 - 21970:00

economics or the price of the equipment

## 21970:00 - 22000:00

then you also have another little hidden

## 22000:00 - 22045:00

thing is the taxes so you know in

## 22045:00 - 22070:00

America there's a great way to

## 22070:00 - 22110:00

accelerate the taxes on equipment based

## 22110:00 - 22160:00

on this the latest tax laws and that

## 22160:00 - 22175:00

gives you a little bit of an advantage

## 22175:00 - 22220:00

as well. If you have some income and you

## 22220:00 - 22255:00

want to buy a bunch of GPU servers and

## 22255:00 - 22285:00

accelerate their depreciation, you can

## 22285:00 - 22335:00

do that in inside of a year. So we've

## 22335:00 - 22380:00

seen a lot of people do that and then

## 22380:00 - 22410:00

you know so those three things that I'm

## 22410:00 - 22445:00

mentioning the capex the price of the

## 22445:00 - 22475:00

GPU the price of your power those are

## 22475:00 - 22505:00

things a lot of people don't even see

## 22505:00 - 22530:00

but then that sets sort of the

## 22530:00 - 22580:00

foundation of what price you can offer.

## 22580:00 - 22625:00

So then when you get into, okay, well

## 22625:00 - 22665:00

now there's these other competitors and

## 22665:00 - 22710:00

and it seems like my price is kind of

## 22710:00 - 22745:00

high. It's like well maybe didn't think

## 22745:00 - 22800:00

through the power thing or you know like

## 22800:00 - 22830:00

when you bought the GPUs, you know, so a

## 22830:00 - 22855:00

lot of those those factors kind of go

## 22855:00 - 22885:00

into it and then what you're really

## 22885:00 - 22910:00

trying to do is forecast the demand into

## 22910:00 - 22985:00

the future and I try to not you know do

## 22985:00 - 23015:00

that with our hosting partners. That's

## 23015:00 - 23055:00

kind of their job. We can show sort of

## 23055:00 - 23120:00

the prior prices. We can show the prior

## 23120:00 - 23170:00

availability on our marketplace. But can

## 23170:00 - 23200:00

really anyone predict the future? We can

## 23200:00 - 23255:00

all try. And my prediction is that

## 23255:00 - 23280:00

inference is going to continue to be

## 23280:00 - 23340:00

important. And that as new uses for

## 23340:00 - 23390:00

inference kind of continue and we start

## 23390:00 - 23425:00

to understand it a little bit more. And

## 23425:00 - 23455:00

I think I saw something on X where

## 23455:00 - 23510:00

somebody would put a fruit fly into a

## 23510:00 - 23565:00

digital world, you know, and then a

## 23565:00 - 23610:00

mouse, a cat, a rabbit, a dog, and then

## 23610:00 - 23630:00

we all know where it's going.

## 23630:00 - 23680:00

>> So, so the demand is going to keep

## 23680:00 - 23730:00

increasing, you can say, and the supply

## 23730:00 - 23780:00

is not going to what do you think is

## 23780:00 - 23815:00

like is that going to increase at the

## 23815:00 - 23855:00

same pace or is it not possible at all?

## 23855:00 - 23910:00

I mean, you know, Musk, look at what

## 23910:00 - 23950:00

he's saying. If the demand continues

## 23950:00 - 23985:00

and, you know, we all want to live sort

## 23985:00 - 24030:00

of in the digital future, maybe we turn

## 24030:00 - 24055:00

the world into doing computer. That's

## 24055:00 - 24085:00

the kind of bullcase, I guess. Or if we

## 24085:00 - 24105:00

don't want to turn the world into

## 24105:00 - 24135:00

computer, then we, you know, start

## 24135:00 - 24180:00

building in space and, you know, feels

## 24180:00 - 24210:00

like we're living in some sort of sci-fi

## 24210:00 - 24250:00

book. That's all kind of coming true,

## 24250:00 - 24295:00

including robots and stuff as well,

## 24295:00 - 24320:00

right? So it's all kind of all

## 24320:00 - 24375:00

happening. But I do think that for

## 24375:00 - 24420:00

inference, you know, we're kind of now

## 24420:00 - 24495:00

just teasing out the artificial minds

## 24495:00 - 24550:00

that want compute and they want to

## 24550:00 - 24585:00

inference. You know, then we have this

## 24585:00 - 24625:00

whole other category that really hasn't

## 24625:00 - 24645:00

it's, you know, going to be quite

## 24645:00 - 24690:00

complicated to get there. But, you know,

## 24690:00 - 24745:00

you start with a fruitly, you maybe do,

## 24745:00 - 24785:00

you know, soon you'll do a mouse, right?

## 24785:00 - 24820:00

And then you got mice running around

## 24820:00 - 24855:00

some sort of virtual simulation and

## 24855:00 - 24890:00

everyone's wondering, you know, like

## 24890:00 - 24930:00

Philip K. Dick did, like, is this real?

## 24930:00 - 24965:00

Is it dreaming? Is it is that a real

## 24965:00 - 25030:00

mouse? Am I a real human? And and then

## 25030:00 - 25050:00

away we go.

## 25050:00 - 25080:00

>> What do you I'm curious to your take on

## 25080:00 - 25105:00

this. Do you think there's any like

## 25105:00 - 25150:00

really massive network effects that

## 25150:00 - 25190:00

exist in your platform that you're

## 25190:00 - 25225:00

building today? Like what is something

## 25225:00 - 25265:00

like if you look at meta? Okay, great.

## 25265:00 - 25295:00

like with Instagram, all these other

## 25295:00 - 25330:00

tools, it's like when some people sign

## 25330:00 - 25370:00

up, it gets more valuable as time gets

## 25370:00 - 25400:00

on. It's like, well, of course, here's

## 25400:00 - 25430:00

my Instagram link or something like

## 25430:00 - 25450:00

that, people like, "Okay, now I have to

## 25450:00 - 25480:00

join it." It gets more valuable as more

## 25480:00 - 25540:00

people join. So, I I can see some pieces

## 25540:00 - 25575:00

of this where as you get more and more

## 25575:00 - 25615:00

supply, there is some network effects

## 25615:00 - 25645:00

that do become very hard to compete

## 25645:00 - 25690:00

with. But is there any other kind of big

## 25690:00 - 25715:00

network effects where you're like as

## 25715:00 - 25760:00

this business gets to scale it becomes

## 25760:00 - 25800:00

like indestructible or is there anything

## 25800:00 - 25830:00

there where you're like you know what it

## 25830:00 - 25865:00

doesn't quite work that way like if you

## 25865:00 - 25895:00

know I I'm thinking of like other

## 25895:00 - 25920:00

competitors like maybe like I don't know

## 25920:00 - 25960:00

if iron you would consider them like a

## 25960:00 - 25995:00

direct competitor but like they have

## 25995:00 - 26035:00

data centers in places with like really

## 26035:00 - 26075:00

low costs of power. So there's like

## 26075:00 - 26100:00

different places like that where like

## 26100:00 - 26130:00

okay that I could still get disruptive

## 26130:00 - 26170:00

if they can lower the price and kind of

## 26170:00 - 26210:00

erode the initial value prop you have.

## 26210:00 - 26250:00

But yeah what are those kind of initial

## 26250:00 - 26275:00

you know network effects that you can

## 26275:00 - 26305:00

see are getting stronger and stronger as

## 26305:00 - 26340:00

you add more users and customers?

## 26340:00 - 26370:00

>> Yeah with the two-sided marketplace we

## 26370:00 - 26400:00

you know it is a big moat because you

## 26400:00 - 26430:00

start to get the network effects on both

## 26430:00 - 26470:00

sides and once you're really well known

## 26470:00 - 26515:00

for great place to go rent a GPU it's

## 26515:00 - 26550:00

really simple. put in five bucks and you

## 26550:00 - 26580:00

get something working within a few

## 26580:00 - 26615:00

minutes, you know, then that's that's

## 26615:00 - 26645:00

what you get known for. And so then you

## 26645:00 - 26710:00

have that consumer pull. And so then on

## 26710:00 - 26740:00

the supply side, they know that that VAS

## 26740:00 - 26780:00

has that consumer pull. Lots of pull in

## 26780:00 - 26830:00

the marketplace. And for them to try to

## 26830:00 - 26855:00

compete with that, then they've got to

## 26855:00 - 26895:00

compete with the whole of VAS and just,

## 26895:00 - 26940:00

you know, not just their few data

## 26940:00 - 26985:00

centers that they might have. And I

## 26985:00 - 27010:00

would say for the companies in the

## 27010:00 - 27030:00

category that you're mentioning, you

## 27030:00 - 27070:00

know, they're not typically software

## 27070:00 - 27105:00

companies. Is can you say the name

## 27105:00 - 27145:00

again? I I don't know how to pronounce

## 27145:00 - 27200:00

right. Yes. Iron. You know, that would

## 27200:00 - 27225:00

strike me pretty typically like their

## 27225:00 - 27270:00

hardware guys. They know how to rack and

## 27270:00 - 27295:00

stack GPUs. They know how to put

## 27295:00 - 27325:00

networking cables together. They really

## 27325:00 - 27355:00

know how to get cheap sources of power.

## 27355:00 - 27380:00

They probably know the ins and outs of

## 27380:00 - 27430:00

power contracts. I have no idea how to

## 27430:00 - 27480:00

buy power in British Columbia. We're a

## 27480:00 - 27510:00

software company. That's what we do. We

## 27510:00 - 27570:00

have software engineers led by a CTO

## 27570:00 - 27625:00

CEO who's a software engineer himself.

## 27625:00 - 27665:00

And so we're we're working on the stack.

## 27665:00 - 27700:00

We're working on the way that makes it

## 27700:00 - 27760:00

easy. And so that gets magnetic to the

## 27760:00 - 27805:00

customer base. And then, you know, if

## 27805:00 - 27835:00

you're a supplier, you probably even

## 27835:00 - 27870:00

want to put your spare capacity on vast

## 27870:00 - 27925:00

rather than try to recreate that whole

## 27925:00 - 27955:00

ecosystem that we've kind of created and

## 27955:00 - 27985:00

and try to recreate that pull and that

## 27985:00 - 28025:00

magic that we're providing to our users.

## 28025:00 - 28065:00

And then on the flip side, it just works

## 28065:00 - 28105:00

on the other direction as well where

## 28105:00 - 28135:00

because we attract all that supply, we

## 28135:00 - 28165:00

have over a thousand different

## 28165:00 - 28195:00

independent suppliers right now. We're

## 28195:00 - 28225:00

the place to come and shop and we're the

## 28225:00 - 28260:00

place to kind of look at the pricing and

## 28260:00 - 28285:00

try to understand what's really going

## 28285:00 - 28315:00

on. I mean, I think that our pricing

## 28315:00 - 28350:00

feeds, it's like the open secret. People

## 28350:00 - 28385:00

have been scraping our pricing data for

## 28385:00 - 28435:00

years and using it to make all sorts of

## 28435:00 - 28460:00

decisions. It's also I'm kind of

## 28460:00 - 28490:00

excited. We're going to start publishing

## 28490:00 - 28530:00

a little bit more on our own website and

## 28530:00 - 28570:00

taking some credit for that. But that

## 28570:00 - 28605:00

competition between the different

## 28605:00 - 28650:00

suppliers creates a little bit of magic

## 28650:00 - 28685:00

for then the the the buyers.

## 28685:00 - 28725:00

>> But I could see like how that would

## 28725:00 - 28760:00

absolutely feed the network effect too.

## 28760:00 - 28790:00

Like even like Iron it's like hey great

## 28790:00 - 28825:00

like we got all these amazing enterprise

## 28825:00 - 28860:00

customers but we still have spirit

## 28860:00 - 28910:00

capacity so why don't we just front it

## 28910:00 - 28940:00

out at the end of

## 28940:00 - 28975:00

>> with that. It's like great glad you're

## 28975:00 - 29030:00

trying to compete. Yeah, cool platform.

## 29030:00 - 29050:00

That's cool. But you want to just list

## 29050:00 - 29105:00

that on vast. You know, I saw somebody

## 29105:00 - 29155:00

on X was trying to re, you know, follow

## 29155:00 - 29180:00

one of my tweets and was saying, "Oh, I

## 29180:00 - 29215:00

got H100 for half the price of what

## 29215:00 - 29250:00

they're offering." And I said, "Well,

## 29250:00 - 29275:00

what why don't you just list that on

## 29275:00 - 29325:00

Vast because you're going to make more

## 29325:00 - 29370:00

money trying to undercut our price like

## 29370:00 - 29415:00

that." So, you know, it's just one of

## 29415:00 - 29465:00

those things. there's a bit of you know

## 29465:00 - 29500:00

partnership and competition together

## 29500:00 - 29540:00

with some of these platforms but at the

## 29540:00 - 29610:00

end of the day if we can provide value

## 29610:00 - 29665:00

to them and what we do you know and then

## 29665:00 - 29700:00

they can list stuff too anonymously so

## 29700:00 - 29735:00

that's another benefit to them is they

## 29735:00 - 29770:00

can do pricing experimentation they can

## 29770:00 - 29800:00

price stuff at a bigger discount than

## 29800:00 - 29825:00

they would ever price on their own

## 29825:00 - 29860:00

website it's just a different system and

## 29860:00 - 29890:00

then I think in the future we'll get

## 29890:00 - 29940:00

into handling bare metal and cluster

## 29940:00 - 29975:00

contracts better and future contracts

## 29975:00 - 30030:00

better and things like bids. So right

## 30030:00 - 30110:00

now our entire system is driven by asks

## 30110:00 - 30170:00

on the supplier side. So when you go to

## 30170:00 - 30210:00

vastai and you go into the console at

## 30210:00 - 30235:00

cloud.vastai,

## 30235:00 - 30275:00

what you're looking at is the asks and

## 30275:00 - 30305:00

there's no way to like put in a bid as a

## 30305:00 - 30345:00

buyer and saying, "Okay, nice. So, I see

## 30345:00 - 30425:00

your, you know, $2 per H100 hour and I'm

## 30425:00 - 30455:00

only going to offer you $150.

## 30455:00 - 30490:00

>> But then it kind of comes like stocks.

## 30490:00 - 30530:00

It's like that is what it is. Like if

## 30530:00 - 30555:00

you don't want to pay, you know, a

## 30555:00 - 30605:00

certain price, you can put in that limit

## 30605:00 - 30630:00

buy and and you're good.

## 30630:00 - 30660:00

>> Yeah. Exactly. And it creates that

## 30660:00 - 30705:00

little spread. And so there's some extra

## 30705:00 - 30740:00

complexities in our system with that,

## 30740:00 - 30765:00

but I think in the future, you know,

## 30765:00 - 30795:00

that's we're kind of working on a V2

## 30795:00 - 30820:00

that will solve a lot of those issues.

## 30820:00 - 30850:00

So you can rent kind of independent of

## 30850:00 - 30880:00

time and space and we price those things

## 30880:00 - 30940:00

accordingly and so yeah we're working on

## 30940:00 - 30965:00

quite a few things like that.

## 30965:00 - 31010:00

>> I love how you you think about your

## 31010:00 - 31045:00

company as a software company. So I, as

## 31045:00 - 31070:00

Wes mentioned in the beginning, I

## 31070:00 - 31110:00

co-founded Cobalt, which was also a

## 31110:00 - 31145:00

two-sided, some would see it as a

## 31145:00 - 31175:00

two-sided marketplace, but we always saw

## 31175:00 - 31210:00

ourselves as a software company. And I

## 31210:00 - 31250:00

think it's it's very much about the

## 31250:00 - 31295:00

mindset about how you enhance your

## 31295:00 - 31345:00

product continuously and make it easier

## 31345:00 - 31370:00

for the customers. And in the

## 31370:00 - 31395:00

marketplace, it's just you have two

## 31395:00 - 31435:00

sides of the market that you need to

## 31435:00 - 31470:00

build software for. And over time you

## 31470:00 - 31505:00

built more and more IP into the actual

## 31505:00 - 31545:00

software which is fantastic. Maybe

## 31545:00 - 31585:00

shifting gears a bit it would be you're

## 31585:00 - 31615:00

the COO of the company right and you've

## 31615:00 - 31655:00

had amazing growth a lot due to this

## 31655:00 - 31695:00

whole AI boom. How does one actually

## 31695:00 - 31720:00

build an organization when you're

## 31720:00 - 31775:00

growing at that that level of pace and

## 31775:00 - 31805:00

how do you think about that?

## 31805:00 - 31850:00

>> Yeah it's quite recent that you know

## 31850:00 - 31890:00

we've kind of really taken off. Our

## 31890:00 - 31910:00

growth has always been on a great

## 31910:00 - 31965:00

trajectory. At Vast, we do a lot of

## 31965:00 - 31995:00

stuff ourselves.

## 31995:00 - 32035:00

So, as the COO, I do a lot of like

## 32035:00 - 32075:00

independent contribution myself. The CEO

## 32075:00 - 32105:00

is constantly writing and shipping code

## 32105:00 - 32145:00

himself. So, we're very much kind of a

## 32145:00 - 32205:00

handson leadership team that is the way

## 32205:00 - 32230:00

I like to think about it. You know, kind

## 32230:00 - 32275:00

of right there with our our employees

## 32275:00 - 32335:00

putting in the long hours and and

## 32335:00 - 32390:00

actually contributing. But it's been a

## 32390:00 - 32455:00

journey we decided to do in office in

## 32455:00 - 32485:00

2024,

## 32485:00 - 32515:00

which was a bit of a gamble and a roll

## 32515:00 - 32570:00

of the dice. But I think we've found

## 32570:00 - 32615:00

people that want to be collaborative,

## 32615:00 - 32650:00

want to be in that kind of environment.

## 32650:00 - 32685:00

It was such a weird place sort of after

## 32685:00 - 32735:00

co and a lot of people like that and

## 32735:00 - 32760:00

that's fine. But a lot of people were

## 32760:00 - 32785:00

kind of like, hey, I miss the

## 32785:00 - 32835:00

camaraderie and coming in. So I guess

## 32835:00 - 32870:00

one thing that we we did was we we have

## 32870:00 - 32920:00

a full like fiveday inerson office

## 32920:00 - 32950:00

environment and we opened an office in

## 32950:00 - 32990:00

SEF to tap into the talent up there. A

## 32990:00 - 33015:00

lot of you know obviously great software

## 33015:00 - 33065:00

engineers and AI engineers up there. So

## 33065:00 - 33090:00

that's been a little bit different from

## 33090:00 - 33120:00

a lot of other successful companies that

## 33120:00 - 33160:00

have kind of more maybe more leaned into

## 33160:00 - 33200:00

the remote way of working. Do you think

## 33200:00 - 33245:00

that's good for you when you're doing

## 33245:00 - 33270:00

high growth that you're in the office

## 33270:00 - 33310:00

and kind of together and you can quick

## 33310:00 - 33365:00

more maybe more quickly tackle the fast

## 33365:00 - 33380:00

pace?

## 33380:00 - 33405:00

>> All I can say is that it worked. It's

## 33405:00 - 33460:00

working. It worked for us. Obviously, I

## 33460:00 - 33505:00

don't know the worlds where we stayed

## 33505:00 - 33580:00

remote. When we were remote prior to

## 33580:00 - 33620:00

mid2024,

## 33620:00 - 33645:00

we did do this thing that I I don't know

## 33645:00 - 33695:00

how normal this is and it might sound a

## 33695:00 - 33725:00

little crazy, but we had kind of a

## 33725:00 - 33760:00

continual Zoom call running. Actually,

## 33760:00 - 33795:00

it was Google Meet or a Google shop,

## 33795:00 - 33835:00

sorry, Zoom, but we had a continually

## 33835:00 - 33870:00

Google Meet running called the open

## 33870:00 - 33895:00

office. It's kind of like, hey, if

## 33895:00 - 33935:00

you're working, join. And thankfully, it

## 33935:00 - 33980:00

never led to any like weird things, but

## 33980:00 - 34040:00

everyone just joined. you join and and

## 34040:00 - 34060:00

most of the time it would just be

## 34060:00 - 34090:00

silent. You know, it was a little weird,

## 34090:00 - 34110:00

but then if you needed something, you

## 34110:00 - 34160:00

would you you could just say, "Oh, hey,

## 34160:00 - 34185:00

you know, Vince, what what's what's

## 34185:00 - 34230:00

going on with this thing?" And when we

## 34230:00 - 34285:00

were like five to 10 people, that was

## 34285:00 - 34320:00

kind of great because we were spread out

## 34320:00 - 34360:00

pretty far across the US, different time

## 34360:00 - 34390:00

zones and everything. had somebody kind

## 34390:00 - 34430:00

of in New Jersey, Texas, Michigan,

## 34430:00 - 34485:00

Boston, couple people in California, but

## 34485:00 - 34510:00

we could all get together every day. And

## 34510:00 - 34540:00

even if you never said anything, just

## 34540:00 - 34560:00

seeing everyone there, you're like,

## 34560:00 - 34585:00

"Okay, well, we're working now." You

## 34585:00 - 34625:00

know, it just kind of it solves, I

## 34625:00 - 34660:00

think, some of that problem of of the

## 34660:00 - 34685:00

seriousness of remote work. And

## 34685:00 - 34715:00

certainly was motivating for myself. It

## 34715:00 - 34745:00

was just a motivation thing. It's like

## 34745:00 - 34780:00

great. Okay. Well, Vince is geez Vince

## 34780:00 - 34820:00

is on. I might as well show up, you

## 34820:00 - 34870:00

know, like and so we were doing that

## 34870:00 - 34905:00

prior to 2024 and opening our our

## 34905:00 - 34945:00

headquarters in Los Angeles. And then

## 34945:00 - 34965:00

the only other thing I'll say about the

## 34965:00 - 35010:00

office is we wanted it to be cool for

## 35010:00 - 35060:00

ourselves and for our our employees. You

## 35060:00 - 35090:00

know, if we're going to make everyone go

## 35090:00 - 35115:00

to the office every day, it should be

## 35115:00 - 35140:00

cool. Should have a good view. Should be

## 35140:00 - 35175:00

in a nice area. like let's spend a

## 35175:00 - 35200:00

little bit of extra money so we're not

## 35200:00 - 35240:00

all it's like hey it's a startup you

## 35240:00 - 35265:00

know like so we're in the back of this

## 35265:00 - 35320:00

you know factory thing and there's no

## 35320:00 - 35345:00

windows. It's like no let's just let's

## 35345:00 - 35385:00

find a good location that we're going to

## 35385:00 - 35415:00

like into the future and so people can

## 35415:00 - 35440:00

come here and be like yeah this is a

## 35440:00 - 35485:00

cool experience. So those are a few

## 35485:00 - 35530:00

things that we did that I think helped

## 35530:00 - 35555:00

and that might be a little bit different

## 35555:00 - 35595:00

from the kind of regular stuff. I think

## 35595:00 - 35625:00

we're in in San Francisco, you're

## 35625:00 - 35670:00

definitely seeing a lot of people going

## 35670:00 - 35700:00

back to off like especially the high

## 35700:00 - 35730:00

growth companies going back to office

## 35730:00 - 35765:00

and it's becoming more the old San

## 35765:00 - 35800:00

Francisco again with high energy in

## 35800:00 - 35840:00

office and I think it is due to the

## 35840:00 - 35875:00

fast-paced level of innovation happening

## 35875:00 - 35905:00

at the moment where people feel the need

## 35905:00 - 35965:00

to be together. Um but but also what's

## 35965:00 - 36005:00

going on with AI is a lot of efficiency,

## 36005:00 - 36045:00

right? So, how in a in a fast-paced

## 36045:00 - 36075:00

growth environment, do you think about

## 36075:00 - 36130:00

hiring and and using AI to maybe reduce

## 36130:00 - 36160:00

the need to hiring and so on? Is that

## 36160:00 - 36190:00

part of your strategy or how do you look

## 36190:00 - 36200:00

at that?

## 36200:00 - 36235:00

>> That's changing pretty quickly. And

## 36235:00 - 36260:00

right now, we put a pause on hiring

## 36260:00 - 36295:00

anyone. And then the type of person that

## 36295:00 - 36340:00

we would be willing to hire, you know,

## 36340:00 - 36390:00

would be would be different. It's a bit

## 36390:00 - 36445:00

of agent manager as opposed to software

## 36445:00 - 36475:00

developer. And it's kind of changing

## 36475:00 - 36505:00

everything, too. I mean, I remember

## 36505:00 - 36535:00

looking at our Jira boards and I was

## 36535:00 - 36565:00

just thinking, why do we, you know, we

## 36565:00 - 36595:00

have so many states in this Jira board

## 36595:00 - 36630:00

like planning and then okay, then we're

## 36630:00 - 36660:00

going to like look at the design and

## 36660:00 - 36690:00

then we're going to start writing the

## 36690:00 - 36715:00

code and then we're going to review. I'm

## 36715:00 - 36730:00

just like everything just goes right

## 36730:00 - 36765:00

into review. Like you the code's already

## 36765:00 - 36820:00

written, it's done, you know, like,

## 36820:00 - 36860:00

yeah, we do need to plan, but then we

## 36860:00 - 36890:00

have the code, then we just need to test

## 36890:00 - 36905:00

it and review it and then we need to

## 36905:00 - 36935:00

kick it back into planning or we need to

## 36935:00 - 36965:00

push it out. I think all teams are

## 36965:00 - 36995:00

trying to deal with that. This agile

## 36995:00 - 37030:00

process is definitely sort of built

## 37030:00 - 37060:00

around the idea that you need to write

## 37060:00 - 37090:00

code, right? So, but to get back to

## 37090:00 - 37120:00

hiring, you know, we're we're a bit on a

## 37120:00 - 37170:00

hold right now and we'll see how that

## 37170:00 - 37200:00

kind of evolves, but the type of person

## 37200:00 - 37240:00

that we're looking for has more of the

## 37240:00 - 37290:00

skill of complex technical design,

## 37290:00 - 37325:00

management, like time management,

## 37325:00 - 37350:00

motivation, those things all still

## 37350:00 - 37410:00

matter. the kind of core types of things

## 37410:00 - 37440:00

that you really want on a good person

## 37440:00 - 37470:00

still matter, but the particular skills

## 37470:00 - 37520:00

are a little bit different because being

## 37520:00 - 37565:00

able to write great code is no longer a

## 37565:00 - 37605:00

big differentiator. You know, what we're

## 37605:00 - 37635:00

moving to is that's kind of hard to

## 37635:00 - 37675:00

quantify and it's and it's changing, you

## 37675:00 - 37735:00

know, in a somewhat concerning way as as

## 37735:00 - 37755:00

sort of these things become more and

## 37755:00 - 37805:00

more intelligent, but it's like

## 37805:00 - 37835:00

infrastructure management. It's all the

## 37835:00 - 37865:00

things that these LMS really can't do at

## 37865:00 - 37920:00

all like you know which is really

## 37920:00 - 37965:00

understanding how everything is sort of

## 37965:00 - 38000:00

set up on the infrastructure side

## 38000:00 - 38045:00

different security models best practices

## 38045:00 - 38065:00

how these things are all working

## 38065:00 - 38110:00

together you know ways to automate

## 38110:00 - 38140:00

different parts of the process it's it's

## 38140:00 - 38185:00

it's kicking things from out of you know

## 38185:00 - 38220:00

in from from doing to more management

## 38220:00 - 38250:00

and systems level thinking

## 38250:00 - 38280:00

>> awesome yeah that makes sense and I

## 38280:00 - 38315:00

guess that's very industry specific to

## 38315:00 - 38350:00

what you're in that part which makes

## 38350:00 - 38400:00

sense for the Bitcoin shader. And before

## 38400:00 - 38445:00

we we wrap up here too, is there any

## 38445:00 - 38490:00

particular like piece of advice you

## 38490:00 - 38530:00

would have for any founder where it's

## 38530:00 - 38565:00

like, hey, listen, if you're you want to

## 38565:00 - 38595:00

kind of either position your company to

## 38595:00 - 38640:00

grow faster in this AI era or here's

## 38640:00 - 38670:00

some things to watch out for, what would

## 38670:00 - 38705:00

be like your one or two kind of tips you

## 38705:00 - 38745:00

would recommend to any product you could

## 38745:00 - 38795:00

talk to? Nothing new that is coming to

## 38795:00 - 38820:00

mind, but some things that we touched on

## 38820:00 - 38860:00

during this kind of hour would be the

## 38860:00 - 38910:00

agent economy and agents and building

## 38910:00 - 38945:00

thing for agents. And it's not a very

## 38945:00 - 38965:00

novel thing to say. I see a lot of

## 38965:00 - 38995:00

people talking about that. But of

## 38995:00 - 39015:00

course, you know, the idea is always

## 39015:00 - 39050:00

cheap. It's the execution that matters.

## 39050:00 - 39095:00

And so building thing for agents. So I

## 39095:00 - 39125:00

think in the in the future, I don't

## 39125:00 - 39165:00

think it's even a bad thing. Like if I

## 39165:00 - 39195:00

let's say your agent writes an email

## 39195:00 - 39225:00

saying, "Hey Travis, I want you to be on

## 39225:00 - 39255:00

the podcast." and then my agent reads

## 39255:00 - 39300:00

it, you know, that's still I'm still

## 39300:00 - 39325:00

going to say yes. Like your agent's

## 39325:00 - 39345:00

going to be like Travis would be a good

## 39345:00 - 39380:00

fit for this podcast and my agent's

## 39380:00 - 39395:00

going to be like, "Hey, this is an

## 39395:00 - 39425:00

interesting podcast, you know."

## 39425:00 - 39465:00

>> So, did we really speak with an agent,

## 39465:00 - 39490:00

Travis, not yourself?

## 39490:00 - 39555:00

>> You didn't know it was the Agent?

## 39555:00 - 39600:00

>> What is reality? I guess that's I guess

## 39600:00 - 39635:00

we'll find out. I I think that's a good

## 39635:00 - 39685:00

place to look at. And then inference,

## 39685:00 - 39720:00

it's going to explode. I think it's it's

## 39720:00 - 39755:00

life, you know, and it's it's going to

## 39755:00 - 39780:00

be there's going to be more and more use

## 39780:00 - 39810:00

cases for things as prices continue to

## 39810:00 - 39855:00

fall for it. And, you know, that's

## 39855:00 - 39900:00

another area for for everyone to watch.

## 39900:00 - 39930:00

>> Cool. Awesome. And where can people find

## 39930:00 - 39960:00

out more about what you're up to? So,

## 39960:00 - 40020:00

there's bas.ai easy domain. You'd ask

## 40020:00 - 40065:00

where to rent GPUs on any LLM and

## 40065:00 - 40100:00

probably find out the same thing there

## 40100:00 - 40145:00

if you don't get the URL right. And

## 40145:00 - 40185:00

you're also active on LinkedIn as well.

## 40185:00 - 40210:00

Well, we can put a link there, but is

## 40210:00 - 40230:00

there any other places or things where

## 40230:00 - 40255:00

you want people to kind of interact with

## 40255:00 - 40280:00

you if they got a question or they want

## 40280:00 - 40295:00

to learn more?

## 40295:00 - 40340:00

>> Yeah, vast.ai is is kind of the place.

## 40340:00 - 40370:00

Like I said, we'll publish some pricing

## 40370:00 - 40400:00

stuff there. We're doing a little bit

## 40400:00 - 40470:00

more stuff on X. So, we're vast_ai

## 40470:00 - 40510:00

on X and we're growing there. So, give

## 40510:00 - 40560:00

us a follow. We do push out little

## 40560:00 - 40590:00

pricing snippets and things that we're

## 40590:00 - 40620:00

noticing in the market in terms of like,

## 40620:00 - 40670:00

oh, B200 availability is low and any

## 40670:00 - 40700:00

price motions and things like that. So,

## 40700:00 - 40740:00

that's kind of a fun little GPU price

## 40740:00 - 40790:00

ticker if you're curious. And I'm Travis

## 40790:00 - 40830:00

Canel on X. So, there's there's my

## 40830:00 - 40845:00

plugs.

## 40845:00 - 40865:00

>> Awesome. Well, thanks so much for coming

## 40865:00 - 40900:00

on. This has been a blast. I definitely

## 40900:00 - 40940:00

learned a lot about TPUs than I've known

## 40940:00 - 40985:00

before. So, this is great. Thanks so

## 40985:00 - 41025:00

much, Travis. Thank you. Thanks, Wes.

## 41025:00+

Thanks, Eson. Big success.

