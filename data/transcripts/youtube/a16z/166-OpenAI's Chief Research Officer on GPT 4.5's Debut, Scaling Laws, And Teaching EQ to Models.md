---
source: https://www.youtube.com/watch?v=pdfI9MuxWq8
title: OpenAI's Chief Research Officer on GPT 4.5's Debut, Scaling Laws, And
  Teaching EQ to Models
author: Alex Kantrowitz
date: 2025-02-27
views: 24705
description: Mark Chen is the chief research officer at OpenAI. Chen joins Big
  Technology Podcast to discuss the debut of GPT 4.5, the company's largest
  model, which is going live today. In this bonus episode, Chen speaks about
  what the new model says about the AI scaling wall, how scaling traditional GPT
  models compares to reasoning models like OpenAI's o1, how important EQ is for
  AI models today, whether product matters more than models, and how OpenAI's
  talent bench looks after last year's departures. Tune in for an inside look at
  what it took to build OpenAI's newest and biggest large language model, and
  why OpenAI is committed to pushing the frontier forward.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T21:04:12.133Z
---

# OpenAI's Chief Research Officer on GPT 4.5's Debut, Scaling Laws, And Teaching EQ to Models

## 00:00 - 35:00

open aai Chief research officer Mark

## 35:00 - 75:00

Chen is here to talk about the release

## 75:00 - 125:00

of GPT 4.5 the company's largest and

## 125:00 - 170:00

best model yet which is coming out today

## 170:00 - 210:00

we'll dive in right after this welcome

## 210:00 - 240:00

to Big technology podcast a show for

## 240:00 - 265:00

cool-headed nuance conversation of the

## 265:00 - 310:00

tech world and Beyond we're joined today

## 310:00 - 350:00

by Mark Chen the chief research officer

## 350:00 - 380:00

at open aai who's here to talk about the

## 380:00 - 440:00

company's newest release GPT 4.5 yes

## 440:00 - 480:00

it's finally here and it is debuting

## 480:00 - 510:00

today Mark great to see you welcome to

## 510:00 - 535:00

the show thank you so much for having me

## 535:00 - 585:00

on thanks for being here this is uh in

## 585:00 - 610:00

four and a half years of the show our

## 610:00 - 650:00

first open AI interview so hopefully the

## 650:00 - 685:00

first of many we appreciate you uh

## 685:00 - 720:00

jumping into the water like this and

## 720:00 - 780:00

it's on big news with the release of GPT

## 780:00 - 860:00

4.5 yeah um so gbd 4.5 really it

## 860:00 - 900:00

signifies the latest milestone in our

## 900:00 - 950:00

predictable scaling uh Paradigm so you

## 950:00 - 975:00

know previous models that have fit this

## 975:00 - 1015:00

Paradigm have been gbd3 3

## 1015:00 - 1055:00

3.54 and now this is the latest thing it

## 1055:00 - 1090:00

um signifies an order of magnitude

## 1090:00 - 1125:00

improvement over the last models kind of

## 1125:00 - 1170:00

commure it with the jump from 3.5 to

## 1170:00 - 1205:00

four I think the question that most of

## 1205:00 - 1230:00

our listeners are going to be asking and

## 1230:00 - 1270:00

certainly we asked on our show in the

## 1270:00 - 1315:00

past couple months is why isn't this GPT

## 1315:00 - 1355:00

5 I mean what is it going to take to get

## 1355:00 - 1435:00

to GPT 5 yeah um well I think gp5 uh you

## 1435:00 - 1475:00

know whenever we make these naming

## 1475:00 - 1525:00

decisions right uh we try to keep with

## 1525:00 - 1575:00

uh a sense of what the trends are so uh

## 1575:00 - 1595:00

again when it comes to predictable

## 1595:00 - 1650:00

scaling right um going from three to 3.5

## 1650:00 - 1675:00

you can kind of predict out you know

## 1675:00 - 1710:00

what an order of magnitude of

## 1710:00 - 1750:00

improvements in in you know amount of

## 1750:00 - 1775:00

compute that you train the model with uh

## 1775:00 - 1800:00

in terms of efficiency improvements will

## 1800:00 - 1850:00

buy you and uh we find this model kind

## 1850:00 - 1900:00

of aligns with what 4.5 would be so we

## 1900:00 - 1945:00

want to name it what it is okay but

## 1945:00 - 1980:00

there's been so much talk about um when

## 1980:00 - 2015:00

GPT 5 is going to come correct me if I'm

## 2015:00 - 2035:00

wrong but I think there's been a longer

## 2035:00 - 2110:00

wait between GPT 4 and 4.5 uh than there

## 2110:00 - 2160:00

has been between let's say uh GPT 3.5

## 2160:00 - 2225:00

and four and I don't know is is this uh

## 2225:00 - 2245:00

like because we're seeing a lot of hype

## 2245:00 - 2280:00

from uh opening ey folks on Twitter

## 2280:00 - 2320:00

about what's coming next or uh maybe

## 2320:00 - 2355:00

this is probably it probably is the most

## 2355:00 - 2380:00

impatient industry in the world and the

## 2380:00 - 2430:00

most impatient users in the world but um

## 2430:00 - 2450:00

it seems to me like the expectations for

## 2450:00 - 2525:00

GPT 5 are built up pretty high and so

## 2525:00 - 2555:00

I'm curious from like your perspective

## 2555:00 - 2580:00

um do you think it's going to be hard to

## 2580:00 - 2615:00

meet those expectations whenever that

## 2615:00 - 2660:00

GPT 5 model does come out well I don't

## 2660:00 - 2690:00

think so and one of the fundamental

## 2690:00 - 2720:00

reasons is because we now have two

## 2720:00 - 2755:00

different axes on which we can scale

## 2755:00 - 2810:00

right um so GPD 4.5 this is our latest

## 2810:00 - 2850:00

scaling experiment along the axis of

## 2850:00 - 2880:00

unsupervised learning but there's also

## 2880:00 - 2915:00

reasoning um and when you ask about kind

## 2915:00 - 2950:00

of like uh why there seems to be you

## 2950:00 - 2980:00

know a little bit bigger of a gap in

## 2980:00 - 3020:00

release time between 4 and 4.5 we've

## 3020:00 - 3055:00

been really largely focused on

## 3055:00 - 3090:00

developing the the reasoning par

## 3090:00 - 3145:00

Paradigm as well so um I think you know

## 3145:00 - 3185:00

our research program is really an

## 3185:00 - 3215:00

exploratory research program right um

## 3215:00 - 3245:00

we're looking into all avenues of how we

## 3245:00 - 3285:00

can scale our models and over the last

## 3285:00 - 3320:00

you know one and a half two years we've

## 3320:00 - 3355:00

really found a new very exciting

## 3355:00 - 3375:00

Paradigm through reasoning which we're

## 3375:00 - 3430:00

also scaling um and and so I think like

## 3430:00 - 3485:00

uh GPD 5 really could be the culmination

## 3485:00 - 3525:00

of a lot of the things coming together

## 3525:00 - 3565:00

okay so you talk about how there's been

## 3565:00 - 3595:00

a lot of work toward reasoning we of

## 3595:00 - 3620:00

course have seen that with a one there's

## 3620:00 - 3675:00

a lot of uh Buzz about deep seek um and

## 3675:00 - 3705:00

now we're talking about again like one

## 3705:00 - 3745:00

of the more traditional scaled up large

## 3745:00 - 3805:00

language models uh with GPT 4.5 so the

## 3805:00 - 3840:00

big question here I think that was on a

## 3840:00 - 3885:00

lot of people's mind uh when it came to

## 3885:00 - 3910:00

this upcoming release we thought was

## 3910:00 - 3945:00

going to be 4.55 anyway it doesn't

## 3945:00 - 4005:00

matter the big question is can AI models

## 4005:00 - 4030:00

continue to scale when you add more

## 4030:00 - 4080:00

compute more data and more power to them

## 4080:00 - 4125:00

um it seems like you have an answer to

## 4125:00 - 4165:00

this so I'm curious to hear your point

## 4165:00 - 4205:00

of view on whether what you've learned

## 4205:00 - 4255:00

about the scaling wall um given your

## 4255:00 - 4300:00

development of this model and um and

## 4300:00 - 4320:00

whether we're going to hit it whether

## 4320:00 - 4345:00

we're already seeing some diminishing

## 4345:00 - 4410:00

returns from scaling yeah um I really

## 4410:00 - 4440:00

kind of have a different framing around

## 4440:00 - 4460:00

uh scaling so when it comes to

## 4460:00 - 4495:00

unsupervised learning right um You want

## 4495:00 - 4530:00

to put more ingredients like uh compute

## 4530:00 - 4575:00

algorithmic in algorithmic efficiencies

## 4575:00 - 4630:00

and uh more data um and GPT 4.5 really

## 4630:00 - 4660:00

is proof that we can continue the

## 4660:00 - 4705:00

scaling Paradigm and this Paradigm is

## 4705:00 - 4740:00

not the antithesis of reasoning as well

## 4740:00 - 4780:00

right um You need knowledge in order to

## 4780:00 - 4825:00

build reasoning on top of right um a

## 4825:00 - 4865:00

model can't kind of go in blind um and

## 4865:00 - 4905:00

just learn reasoning from scratch so uh

## 4905:00 - 4945:00

we find these two paradigms to be fairly

## 4945:00 - 4975:00

complimentary um and we think you know

## 4975:00 - 5010:00

they have feedback loops on each other

## 5010:00 - 5100:00

so um yeah GPD 4.5 again uh it is smart

## 5100:00 - 5125:00

in different ways from the ways that

## 5125:00 - 5160:00

reasoning models are smart right um when

## 5160:00 - 5200:00

you look at the model today um it has a

## 5200:00 - 5245:00

lot more World Knowledge um when we look

## 5245:00 - 5305:00

at kind of comparisons against 3PD 40 um

## 5305:00 - 5335:00

you see that everyday use cases people

## 5335:00 - 5375:00

prefer it you know by a margin of 60%

## 5375:00 - 5410:00

for actually productivity and knowledge

## 5410:00 - 5445:00

work against gp40 there's almost like a

## 5445:00 - 5495:00

70% preference rate so people are really

## 5495:00 - 5545:00

responding to this model um and it's

## 5545:00 - 5580:00

this knowledge that we can leverage uh

## 5580:00 - 5620:00

for our reasoning models in the future

## 5620:00 - 5650:00

so what are the examples like you talk

## 5650:00 - 5675:00

about everyday knowledge work what are

## 5675:00 - 5695:00

some of the examples that you would use

## 5695:00 - 5760:00

GPT 4.5 for that you would prefer it

## 5760:00 - 5830:00

over a reasoning model yeah um so I I

## 5830:00 - 5860:00

wouldn't say like uh it's a it's a

## 5860:00 - 5890:00

different profile from from a reasoning

## 5890:00 - 5950:00

model right um so with a larger model um

## 5950:00 - 5995:00

what you're doing is it it takes more

## 5995:00 - 6015:00

time to kind of process and think

## 6015:00 - 6045:00

through the query but it's also giving

## 6045:00 - 6080:00

you an immediate response back so this

## 6080:00 - 6125:00

is very similar to what a gp4 would have

## 6125:00 - 6165:00

would have done for you right um whereas

## 6165:00 - 6215:00

I think um with something like 01 you

## 6215:00 - 6245:00

get a model where you give a query and

## 6245:00 - 6320:00

it can think for several minutes um and

## 6320:00 - 6345:00

and I think these are fundamentally kind

## 6345:00 - 6375:00

of different trade-offs right uh you

## 6375:00 - 6405:00

have a model that immediately comes back

## 6405:00 - 6460:00

to you doesn't do much thinking um uh

## 6460:00 - 6485:00

but comes up with a better answer versus

## 6485:00 - 6520:00

a model that you know uh thinks for a

## 6520:00 - 6570:00

while um and then comes comes up with

## 6570:00 - 6605:00

the with an answer and you know we find

## 6605:00 - 6635:00

that in a lot of areas like creative

## 6635:00 - 6685:00

writing for instance um uh again this is

## 6685:00 - 6715:00

stuff that we want to test over the next

## 6715:00 - 6765:00

one or two months um but uh we find that

## 6765:00 - 6790:00

there there are areas like creative

## 6790:00 - 6815:00

writing where this model outshines

## 6815:00 - 6860:00

reasoning models okay so writing any

## 6860:00 - 6910:00

other use cases yeah so there's there's

## 6910:00 - 6950:00

writing um I think some coding use cases

## 6950:00 - 7015:00

as well um we also find that um kind of

## 7015:00 - 7060:00

like uh you know there there are some

## 7060:00 - 7090:00

particular kind of scientific domains

## 7090:00 - 7120:00

where this outshines in terms of the

## 7120:00 - 7160:00

amount of knowledge that it can display

## 7160:00 - 7185:00

okay and I'm going to come back to

## 7185:00 - 7225:00

benchmarks uh in a moment but I want to

## 7225:00 - 7265:00

keep on this scaling question because I

## 7265:00 - 7295:00

think there's been a lot of conversation

## 7295:00 - 7335:00

about it in public and it's great to uh

## 7335:00 - 7360:00

be speaking with you from open AI to

## 7360:00 - 7395:00

sort of get to the bottom of of what's

## 7395:00 - 7425:00

happening so the first is um the

## 7425:00 - 7465:00

question that folks have is do you end

## 7465:00 - 7505:00

up at this size and you don't talk about

## 7505:00 - 7540:00

the size of the models which is you know

## 7540:00 - 7580:00

which is fair U but they're big right

## 7580:00 - 7610:00

this is the largest model uh that openi

## 7610:00 - 7660:00

has ever released GPT 4.5 so I'm

## 7660:00 - 7695:00

actually curious to hear at this size uh

## 7695:00 - 7735:00

does adding you know similar amounts of

## 7735:00 - 7785:00

compute similar amounts of data get you

## 7785:00 - 7830:00

the same returns uh that you did or are

## 7830:00 - 7855:00

are we already starting to see the

## 7855:00 - 7895:00

returns of adding these resources tail

## 7895:00 - 7940:00

off no no we are seeing the same returns

## 7940:00 - 7995:00

and I I do want to stress that JD 4.5 is

## 7995:00 - 8030:00

next point on this unsupervised learning

## 8030:00 - 8060:00

Paradigm and you know we're very

## 8060:00 - 8090:00

rigorous about how we do this we make

## 8090:00 - 8115:00

projections based on all the models

## 8115:00 - 8150:00

we've trained before on what performance

## 8150:00 - 8195:00

to expect um and in this case um you

## 8195:00 - 8230:00

know we put together the scaling

## 8230:00 - 8265:00

machinery and this is the point that

## 8265:00 - 8315:00

lies at that next order of magnitude so

## 8315:00 - 8345:00

what's it been like getting here I mean

## 8345:00 - 8380:00

again we talked okay so there was there

## 8380:00 - 8425:00

was a period of time that was longer

## 8425:00 - 8460:00

than the last interval and part of that

## 8460:00 - 8480:00

was focused on reasoning but there's

## 8480:00 - 8520:00

also been some reports that open eyes

## 8520:00 - 8550:00

had to start and stop a couple times to

## 8550:00 - 8590:00

get this to work um and really had to

## 8590:00 - 8625:00

fight through some thorny issues to get

## 8625:00 - 8675:00

it to be this step change as you're

## 8675:00 - 8710:00

saying so talk a little bit about the

## 8710:00 - 8755:00

process and um maybe you can confirm or

## 8755:00 - 8780:00

deny some of the things that we've heard

## 8780:00 - 8820:00

about having to start and stop again and

## 8820:00 - 8880:00

uh retrain to get here um actually so I

## 8880:00 - 8910:00

I think it's it's interesting that this

## 8910:00 - 8945:00

gets uh is a point that's attributed to

## 8945:00 - 8975:00

this model because um actually in in in

## 8975:00 - 9005:00

developing all of our foundation models

## 9005:00 - 9050:00

right um they are all experiments right

## 9050:00 - 9095:00

I I think um you know running all the

## 9095:00 - 9125:00

foundation models often times does

## 9125:00 - 9150:00

involve stopping at certain Pro just

## 9150:00 - 9180:00

kind of analyzing what's going on and

## 9180:00 - 9220:00

then restarting the runs and uh I don't

## 9220:00 - 9240:00

think that this is a characteristic of

## 9240:00 - 9285:00

dpd 4.5 I'm it's something that we've

## 9285:00 - 9330:00

done with you gbd4 with O Series models

## 9330:00 - 9365:00

um and you know they are largely

## 9365:00 - 9410:00

experiments right we we want to go in um

## 9410:00 - 9435:00

diagnose them in the middle and if we

## 9435:00 - 9465:00

want to make some interventions we we

## 9465:00 - 9500:00

should make interventions but

## 9500:00 - 9530:00

um I wouldn't characterize this as kind

## 9530:00 - 9580:00

of uh something that we do for GPD 4.5

## 9580:00 - 9610:00

that we don't do for other models we've

## 9610:00 - 9630:00

already talked a little bit about

## 9630:00 - 9670:00

reasoning versus these traditional GPT

## 9670:00 - 9725:00

models uh but it makes me think of deep

## 9725:00 - 9775:00

seek and um I think you already gave a

## 9775:00 - 9800:00

pretty compelling answer as to like what

## 9800:00 - 9825:00

you would use one of these models for

## 9825:00 - 9860:00

versus a reasoning model uh but there's

## 9860:00 - 9905:00

another thing that deeps did that um is

## 9905:00 - 9930:00

worth discussing which is that they made

## 9930:00 - 9965:00

their models much more efficient and

## 9965:00 - 9985:00

it's kind of interesting like when I

## 9985:00 - 10010:00

told to you about like all right so you

## 10010:00 - 10035:00

need data you need compute you need

## 10035:00 - 10065:00

power you're like yeah and you need

## 10065:00 - 10105:00

model optimizations which is something

## 10105:00 - 10150:00

that people often Overlook and just

## 10150:00 - 10185:00

going back to deep seek for a moment the

## 10185:00 - 10215:00

model optimization the fact that they

## 10215:00 - 10245:00

went from basically queering the entire

## 10245:00 - 10275:00

knowledge base to mixture of experts

## 10275:00 - 10310:00

where they're able to sort of Route the

## 10310:00 - 10335:00

queries to certain parts of the model

## 10335:00 - 10365:00

instead of lighting it all up is

## 10365:00 - 10400:00

credited with help them helping them get

## 10400:00 - 10435:00

more efficient so I just want to turn it

## 10435:00 - 10470:00

over to you um without commenting on

## 10470:00 - 10495:00

what they did or if you can if you want

## 10495:00 - 10525:00

but I'm actually more curious what open

## 10525:00 - 10570:00

AI is doing on that front and what sort

## 10570:00 - 10610:00

of whether you did similar optimizations

## 10610:00 - 10630:00

with GPT

## 10630:00 - 10680:00

4.5 and are you able to run these large

## 10680:00 - 10725:00

models more efficiently and if so how

## 10725:00 - 10765:00

yeah so I would say um kind of the

## 10765:00 - 10805:00

process of making a model efficient to

## 10805:00 - 10845:00

serve I often see as fairly decoupled

## 10845:00 - 10885:00

from developing the core capability of

## 10885:00 - 10935:00

the model right um and we see a lot of

## 10935:00 - 10965:00

work being done on the inference stack

## 10965:00 - 10985:00

right I think that's something that uh

## 10985:00 - 11020:00

deep seek did very well um and it's also

## 11020:00 - 11050:00

something that we push on a lot right um

## 11050:00 - 11085:00

we care about serving these models at

## 11085:00 - 11135:00

cheap cost to all users um and we push

## 11135:00 - 11185:00

on that quite a bit um so I think this

## 11185:00 - 11220:00

is irrespective of you know gbd4

## 11220:00 - 11255:00

reasoning models we're always applying

## 11255:00 - 11290:00

that pressure to be able to influence

## 11290:00 - 11330:00

more cheaply and and I think we've done

## 11330:00 - 11355:00

a good job of that over time right like

## 11355:00 - 11380:00

uh the cost have Dro you know many

## 11380:00 - 11405:00

orders of magnitude since we first

## 11405:00 - 11450:00

launched your bd4 and so are there like

## 11450:00 - 11495:00

are I mean maybe tell me if this is to

## 11495:00 - 11535:00

but um the move towards for instance

## 11535:00 - 11580:00

mixture of experts um is that more of a

## 11580:00 - 11615:00

reasoning thing or can you apply that in

## 11615:00 - 11675:00

GPT yeah so um that is an architectural

## 11675:00 - 11725:00

um element of language models I think

## 11725:00 - 11750:00

pretty much all large language models

## 11750:00 - 11800:00

today use utilize mixture of experts um

## 11800:00 - 11835:00

and it's something that applies equally

## 11835:00 - 11885:00

to efficiency wins in uh Foundation

## 11885:00 - 11945:00

models like GPT 4 4.5 as it does to

## 11945:00 - 11985:00

reasoning models so you were able to use

## 11985:00 - 12030:00

that here as well basically um no we've

## 12030:00 - 12070:00

definitely explored mixture of experts

## 12070:00 - 12085:00

as well as a number of other

## 12085:00 - 12130:00

architectural improvements

## 12130:00 - 12195:00

in okay great um so we we have a Discord

## 12195:00 - 12215:00

uh with some members of the big

## 12215:00 - 12255:00

technology listeners and reader group

## 12255:00 - 12285:00

and you know a theme that's come up

## 12285:00 - 12310:00

recently it's kind of interesting to be

## 12310:00 - 12335:00

talking with you right now about an

## 12335:00 - 12370:00

extremely large model because a theme

## 12370:00 - 12395:00

that they can't stop talking about the

## 12395:00 - 12430:00

people in the Discord is just that how

## 12430:00 - 12470:00

small and Niche models uh to them are

## 12470:00 - 12500:00

going to you know potenti be the future

## 12500:00 - 12520:00

I'll just read you one comment that we

## 12520:00 - 12560:00

had over the past few days for me the

## 12560:00 - 12580:00

future is very much aligned with Niche

## 12580:00 - 12620:00

models existing in workflows and less so

## 12620:00 - 12670:00

of these general purpose God models um

## 12670:00 - 12700:00

so clearly open AI is a different thesis

## 12700:00 - 12730:00

here and I am curious to hear your

## 12730:00 - 12765:00

perspective on what we get with the big

## 12765:00 - 12800:00

models versus the niche models and do

## 12800:00 - 12825:00

you see them in competition or as

## 12825:00 - 12860:00

compliments help us think about think

## 12860:00 - 12890:00

through that yeah yeah so I think one

## 12890:00 - 12935:00

important thing is we also serve models

## 12935:00 - 12960:00

that are smaller right like we serve our

## 12960:00 - 12985:00

Flagship Frontier models but we Also

## 12985:00 - 13010:00

Serve mini models right which are

## 13010:00 - 13045:00

cost-efficient ways that you can access

## 13045:00 - 13085:00

the capabilities or fairly close to

## 13085:00 - 13115:00

Frontier capabilities for much lower

## 13115:00 - 13140:00

cost right and we think that's an

## 13140:00 - 13165:00

important part of this comprehensive

## 13165:00 - 13215:00

portfolio here um fundamentally at

## 13215:00 - 13245:00

opening eye though uh we're in the

## 13245:00 - 13280:00

business of advancing the frontier of

## 13280:00 - 13320:00

intelligence and that involves

## 13320:00 - 13370:00

developing the best models that we can

## 13370:00 - 13410:00

um and I I think really kind of what

## 13410:00 - 13440:00

we're motivated by is really pushing

## 13440:00 - 13485:00

that out as much as possible um we think

## 13485:00 - 13510:00

there's always going to be use cases at

## 13510:00 - 13555:00

the frontiers of intelligence um you

## 13555:00 - 13580:00

know we we think that you know going

## 13580:00 - 13635:00

from 99.9 percentile in in mathematics

## 13635:00 - 13670:00

to the best in the world in mathematics

## 13670:00 - 13695:00

right like that difference means

## 13695:00 - 13735:00

something to us like I think uh what you

## 13735:00 - 13765:00

know the best human scientists can

## 13765:00 - 13795:00

discover is tangibly different right

## 13795:00 - 13845:00

from what you or I can can discover so

## 13845:00 - 13875:00

um we're we're motivated by pushing the

## 13875:00 - 13910:00

intelligence Frontier as far as possible

## 13910:00 - 13950:00

and at the same time uh we want to make

## 13950:00 - 13995:00

these capabilities cheaper and more cost

## 13995:00 - 14025:00

effective reserve for everyone so we

## 14025:00 - 14045:00

don't think the niche models will go

## 14045:00 - 14075:00

away we want to build these Foundation

## 14075:00 - 14100:00

models and also figure out how to

## 14100:00 - 14135:00

deliver these capabilities at cost over

## 14135:00 - 14175:00

time so um that's always been our

## 14175:00 - 14200:00

philosophy there's always going to be

## 14200:00 - 14240:00

some juice there in in those last bits

## 14240:00 - 14275:00

of intelligence yeah so let's talk about

## 14275:00 - 14300:00

that because we have a debate on the

## 14300:00 - 14335:00

show often what matters more the

## 14335:00 - 14390:00

products or the model right um I'm on

## 14390:00 - 14425:00

team model we have uh Ronan Roy who

## 14425:00 - 14475:00

comes on on Fridays he's team uh product

## 14475:00 - 14495:00

he's basically like just take what you

## 14495:00 - 14520:00

have now and prioritize it and I say

## 14520:00 - 14550:00

well you could probably do more with a

## 14550:00 - 14580:00

better model but I have to be honest I'm

## 14580:00 - 14610:00

kind of at a loss for word sometimes

## 14610:00 - 14650:00

about what that getting from that 99th

## 14650:00 - 14685:00

percentile in math to the best in World

## 14685:00 - 14725:00

a math will do so actually am curious to

## 14725:00 - 14770:00

hear your answer on this one what does

## 14770:00 - 14795:00

what does building the best model in the

## 14795:00 - 14835:00

world do that yeah could do otherwise

## 14835:00 - 14900:00

100% And I think really um it signals a

## 14900:00 - 14930:00

shift right like I I think if you just

## 14930:00 - 14955:00

think about hey you take the current

## 14955:00 - 14985:00

models and you build the best surface

## 14985:00 - 15010:00

for them that's certainly something you

## 15010:00 - 15035:00

should always be doing and exploring

## 15035:00 - 15070:00

that exercise I think 3 years ago that

## 15070:00 - 15100:00

looked like chat right we we launched

## 15100:00 - 15140:00

chat gbt um and today when it look when

## 15140:00 - 15165:00

you take the best models and the best

## 15165:00 - 15195:00

capabilities I think it looks a little

## 15195:00 - 15230:00

bit more like agents right um and I

## 15230:00 - 15260:00

think reasoning and agents they're

## 15260:00 - 15300:00

they're very very much coupled right um

## 15300:00 - 15330:00

when you think about what makes a good

## 15330:00 - 15355:00

Agent it's something that you can kind

## 15355:00 - 15400:00

of sit back let it do its own thing and

## 15400:00 - 15430:00

you're fairly confident it'll come back

## 15430:00 - 15465:00

with something that you want right and I

## 15465:00 - 15490:00

think reasoning is the engine that

## 15490:00 - 15530:00

powers that right like uh you uh have

## 15530:00 - 15570:00

the model go and try something out and

## 15570:00 - 15610:00

if it um if it can't succeed on the

## 15610:00 - 15635:00

first try it should be able to be like

## 15635:00 - 15655:00

oh well why didn't I succeed and what's

## 15655:00 - 15710:00

a better approach for me to do so um you

## 15710:00 - 15735:00

know I I I think very much kind of like

## 15735:00 - 15765:00

uh the capabilities are always changing

## 15765:00 - 15795:00

and the surface is always changing as a

## 15795:00 - 15825:00

as a response and we're always exploring

## 15825:00 - 15855:00

what the best surface for the current

## 15855:00 - 15890:00

capabilities looks like but just to H

## 15890:00 - 15915:00

I'm on your team here yeah but but again

## 15915:00 - 15935:00

just to hammer home on this like what

## 15935:00 - 15975:00

does that Improvement in model get you

## 15975:00 - 16015:00

like what you think that it will enable

## 16015:00 - 16055:00

yeah yeah so I mean I think uh I mean

## 16055:00 - 16080:00

agents of all forms right when you look

## 16080:00 - 16110:00

at stuff like deep research for instance

## 16110:00 - 16160:00

right um it gives you the ability to

## 16160:00 - 16205:00

essentially kind of get a fully formed

## 16205:00 - 16235:00

report on any single topic that you

## 16235:00 - 16265:00

might be interested in right um I've

## 16265:00 - 16305:00

used it to even put together like

## 16305:00 - 16355:00

hourlong talks um and it goes and really

## 16355:00 - 16370:00

kind of like synthesizes all the

## 16370:00 - 16400:00

information out there and and really

## 16400:00 - 16440:00

organizes it comes up with lessons um

## 16440:00 - 16485:00

allows you to do deep Discovery um it

## 16485:00 - 16550:00

allows you to uh you know like dig into

## 16550:00 - 16570:00

almost any topic that that you're

## 16570:00 - 16625:00

interested in so I feel like um just the

## 16625:00 - 16660:00

amount of information and synthesis

## 16660:00 - 16705:00

that's that's available to you now is is

## 16705:00 - 16745:00

just really rapidly evolving so

## 16745:00 - 16775:00

basically it's not as simple as like

## 16775:00 - 16805:00

just go make deep research better with

## 16805:00 - 16835:00

the product uh with the model you have

## 16835:00 - 16865:00

now am I reading between the lines the

## 16865:00 - 16905:00

right way saying that what you're you're

## 16905:00 - 16940:00

uh expressing here is that if you make

## 16940:00 - 16980:00

the model better then the product is to

## 16980:00 - 17010:00

get better inherently take deep research

## 17010:00 - 17060:00

for instance 100% 100% yeah and that's

## 17060:00 - 17090:00

something that is not enabled unless you

## 17090:00 - 17115:00

have models of a certain level of

## 17115:00 - 17155:00

capability both in reasoning and in the

## 17155:00 - 17200:00

foundational unsupervised learning sense

## 17200:00 - 17225:00

okay you know it's interesting I guess

## 17225:00 - 17245:00

like this one question I've had in the

## 17245:00 - 17275:00

back of my mind is uh and I'm just going

## 17275:00 - 17305:00

to ask it to you again just so I'm sure

## 17305:00 - 17370:00

I'm clear on it is um my view maybe

## 17370:00 - 17395:00

erroneously was that we were just going

## 17395:00 - 17425:00

to or your industry was just going to

## 17425:00 - 17480:00

move from um these massive models to the

## 17480:00 - 17510:00

massive models with reasoning but you're

## 17510:00 - 17540:00

actually saying that there's a dual

## 17540:00 - 17585:00

track here yeah yeah so I think we're

## 17585:00 - 17625:00

always pushing the frontier right and we

## 17625:00 - 17660:00

I think even since you know five six

## 17660:00 - 17695:00

years ago the prevailing way to do that

## 17695:00 - 17735:00

was to up up the scale right and so

## 17735:00 - 17755:00

we've been upping the scale in

## 17755:00 - 17780:00

unsupervised learning we've been upping

## 17780:00 - 17815:00

the scale in reasoning but at the same

## 17815:00 - 17845:00

time right you care about serving mini

## 17845:00 - 17875:00

models you care about serving models

## 17875:00 - 17910:00

that are cost effective that can deliver

## 17910:00 - 17970:00

capabilities at at a cheaper cost um and

## 17970:00 - 17995:00

that will often be sufficient for a lot

## 17995:00 - 18050:00

of use cases right and uh the mission

## 18050:00 - 18080:00

isn't just about pushing the biggest

## 18080:00 - 18120:00

most costly models it's about having

## 18120:00 - 18150:00

that and also a portfolio of models that

## 18150:00 - 18185:00

people can use cheaply for their use

## 18185:00 - 18225:00

cases okay so let's quickly talk before

## 18225:00 - 18260:00

we leave about the upgrades uh that

## 18260:00 - 18320:00

you're seeing in 4.5 compared to four so

## 18320:00 - 18350:00

I'm curious like if you can just run us

## 18350:00 - 18375:00

through a very high level the benchmarks

## 18375:00 - 18420:00

that hits versus the benchmarks of the

## 18420:00 - 18450:00

previous models and then I'll just throw

## 18450:00 - 18495:00

a double question in here yeah MH um

## 18495:00 - 18525:00

I've already read your blog post and so

## 18525:00 - 18560:00

I have an idea of what's coming um by

## 18560:00 - 18580:00

the way we're going to release this just

## 18580:00 - 18640:00

as the news is released uh so um it

## 18640:00 - 18680:00

seems like you're also saying making a

## 18680:00 - 18705:00

statement in some ways saying like yes

## 18705:00 - 18740:00

we have the traditional benchmarks but

## 18740:00 - 18765:00

we also need to measure how this model

## 18765:00 - 18810:00

Works in with EQ as opposed to just you

## 18810:00 - 18840:00

know pure intelligence so yeah just hit

## 18840:00 - 18870:00

us with the Benchmark improvements and

## 18870:00 - 18900:00

then why you think that it's important

## 18900:00 - 18935:00

for us to look at both of these in

## 18935:00 - 18970:00

conjunction yeah so I mean along all

## 18970:00 - 19000:00

tradition metrics like things like you

## 19000:00 - 19035:00

know GP QA Amy you know the the

## 19035:00 - 19060:00

traditional kind of benchmarks that we

## 19060:00 - 19090:00

track this does signify you know an

## 19090:00 - 19125:00

order of magnitude about at the same

## 19125:00 - 19175:00

level of jump from 3.5 to four um there

## 19175:00 - 19205:00

isn't there's a kind of interesting

## 19205:00 - 19240:00

Focus here also on um I would say more

## 19240:00 - 19280:00

Vib space Ben benchmarks right and I

## 19280:00 - 19300:00

think that's actually important to

## 19300:00 - 19320:00

highlight because every single time

## 19320:00 - 19350:00

we've launched a model there is a

## 19350:00 - 19385:00

discovery process of what the kind of

## 19385:00 - 19405:00

interesting use cases out there are

## 19405:00 - 19450:00

going to be U we notice here you know um

## 19450:00 - 19490:00

it's actually a much more emotionally

## 19490:00 - 19530:00

intelligent model um you know you can

## 19530:00 - 19560:00

kind of uh see examples in the blog post

## 19560:00 - 19595:00

later today but like how it responds to

## 19595:00 - 19630:00

you know queries about uh you know a

## 19630:00 - 19680:00

hard situation or you know um uh advice

## 19680:00 - 19740:00

in in um a particular difficult

## 19740:00 - 19765:00

situation that it responds more

## 19765:00 - 19805:00

emotionally intelligent um I think

## 19805:00 - 19845:00

there's also just kind of like uh you

## 19845:00 - 19875:00

can kind of see like yeah uh this may be

## 19875:00 - 19905:00

a kind of silly example right but um if

## 19905:00 - 19945:00

you ask any of the previous models to

## 19945:00 - 19975:00

create aski art for you right um

## 19975:00 - 20005:00

actually they mostly just fall down this

## 20005:00 - 20055:00

one can do it almost Flawless pretty

## 20055:00 - 20095:00

well um and and so there's just so many

## 20095:00 - 20130:00

kind of like uh Footprints of improved

## 20130:00 - 20190:00

capabilities and um and I think things

## 20190:00 - 20225:00

like creative writing will showcase this

## 20225:00 - 20250:00

one of the things that I I think I

## 20250:00 - 20275:00

picked up uh in the examples that you've

## 20275:00 - 20315:00

given so far is that it doesn't seem

## 20315:00 - 20355:00

like it feels the need to write uh a you

## 20355:00 - 20405:00

know a thesis for every response like

## 20405:00 - 20440:00

one uh user was like I'm having a hard

## 20440:00 - 20480:00

time and it actually succinctly wrote as

## 20480:00 - 20505:00

if a human would as opposed to like

## 20505:00 - 20540:00

maybe the traditional you know here's

## 20540:00 - 20570:00

three paragraphs of self-care routine

## 20570:00 - 20600:00

you can doly yeah yeah yeah and that

## 20600:00 - 20625:00

speaks to the emotional intelligence

## 20625:00 - 20665:00

right it's not like oh uh I see that

## 20665:00 - 20695:00

you're feeling bad here are like five

## 20695:00 - 20720:00

ways you could feel better right it just

## 20720:00 - 20750:00

doesn't feel like a grounded kind of a

## 20750:00 - 20775:00

compassionate response and here you just

## 20775:00 - 20795:00

get something that's you know direct to

## 20795:00 - 20820:00

the point and really invites the user to

## 20820:00 - 20860:00

say more so I think there's going to be

## 20860:00 - 20895:00

a criticism I can I'm anticipating it

## 20895:00 - 20930:00

and let's let's talk about it right now

## 20930:00 - 20965:00

that people will say okay open AI was

## 20965:00 - 20990:00

talking about these traditional

## 20990:00 - 21020:00

benchmarks now it's talking about

## 21020:00 - 21050:00

emotional intelligence it's Shifting the

## 21050:00 - 21080:00

goalposts and wants us to pay attention

## 21080:00 - 21110:00

to something else what's your response

## 21110:00 - 21165:00

there well I I really don't think that

## 21165:00 - 21195:00

the accurate characterization is that it

## 21195:00 - 21230:00

doesn't hit the benchmarks that that we

## 21230:00 - 21265:00

expected to so when you look at kind of

## 21265:00 - 21320:00

the development of 3 to 3.5 to 4 to 4.5

## 21320:00 - 21355:00

um this does hit the benchmarks that we

## 21355:00 - 21400:00

expect um and I think the main thing is

## 21400:00 - 21445:00

like uh you know it's all about use case

## 21445:00 - 21465:00

Discovery every time you put a new model

## 21465:00 - 21485:00

out there

## 21485:00 - 21540:00

um and in many senses like gp4 is

## 21540:00 - 21590:00

already very smart right um and and kind

## 21590:00 - 21625:00

of when we were putting that this

## 21625:00 - 21640:00

parallel is kind of like when we were

## 21640:00 - 21670:00

putting gp4 out right it's like we saw

## 21670:00 - 21695:00

it hit all the right benchmarks that we

## 21695:00 - 21725:00

expected to but what are users going to

## 21725:00 - 21765:00

resonate with that was the key question

## 21765:00 - 21780:00

and I think that's the question that

## 21780:00 - 21825:00

we're asking today with GPD 4.5 as well

## 21825:00 - 21855:00

um and we're inviting people to be like

## 21855:00 - 21880:00

hey you know we did some early

## 21880:00 - 21905:00

Explorations we see that it's more

## 21905:00 - 21935:00

emotionally intelligent you know we see

## 21935:00 - 21960:00

that it's a better creative writer but

## 21960:00 - 21990:00

what do you see here

## 21990:00 - 22025:00

yep all right Mark so I've been seeing

## 22025:00 - 22050:00

you in I we mentioned this before we

## 22050:00 - 22065:00

started recording I've been seeing you

## 22065:00 - 22085:00

in all the opening eye videos about

## 22085:00 - 22125:00

every release so first of all great to

## 22125:00 - 22180:00

uh speak to you uh live uh but also over

## 22180:00 - 22210:00

the past year we've seen a lot of Exodus

## 22210:00 - 22230:00

uh out of opening ey maybe the media

## 22230:00 - 22275:00

plays it up too much probably we do um

## 22275:00 - 22300:00

but I am kind of curious what it's like

## 22300:00 - 22335:00

working within open Ai and how you see

## 22335:00 - 22365:00

the talent bench inside the company you

## 22365:00 - 22395:00

recently became Chief research officer

## 22395:00 - 22430:00

just a few months ago um and now look we

## 22430:00 - 22460:00

have a new foundational model so just

## 22460:00 - 22485:00

give us a sense as

## 22485:00 - 22515:00

the talent situation

## 22515:00 - 22570:00

is um it's still I think the most World

## 22570:00 - 22635:00

Class um AI organization um I would say

## 22635:00 - 22660:00

that there's a separation between the

## 22660:00 - 22690:00

talent bar at opening ey and any other

## 22690:00 - 22735:00

firm out there and um when it comes to

## 22735:00 - 22760:00

kind of people leaving you know like the

## 22760:00 - 22805:00

AI landscape it changes a lot um You

## 22805:00 - 22830:00

probably more so than any other field

## 22830:00 - 22855:00

out there right um the field three

## 22855:00 - 22880:00

months ago looks different from the

## 22880:00 - 22910:00

field three months before that and I

## 22910:00 - 22935:00

think it's kind of just natural in the

## 22935:00 - 22975:00

development of AI that some people will

## 22975:00 - 23000:00

have their own thesis about here's the

## 23000:00 - 23045:00

way I I want to develop Ai and go try it

## 23045:00 - 23080:00

their their own way um I think that's

## 23080:00 - 23105:00

healthy and it also gives an opportunity

## 23105:00 - 23150:00

for people internally to shine and um

## 23150:00 - 23180:00

we've never had a shortage of people

## 23180:00 - 23210:00

internally who are willing to step up

## 23210:00 - 23250:00

and we've seen that a lot and I really

## 23250:00 - 23280:00

just love the bench that we have here

## 23280:00 - 23340:00

very cool all right folks GPT 4.5 is out

## 23340:00 - 23385:00

today for open AI Pro users next week

## 23385:00 - 23435:00

it's coming out for plus team Enterprise

## 23435:00 - 23495:00

and edu uh Mark great to see you thank

## 23495:00 - 23520:00

you again for spending time you're about

## 23520:00 - 23550:00

to go and do the live stream so I'm very

## 23550:00 - 23570:00

grateful that you spent the time with me

## 23570:00 - 23605:00

today thank so much I really appreciate

## 23605:00 - 23630:00

your time to you thanks for having me

## 23630:00 - 23670:00

well let's do it again soon and uh folks

## 23670:00 - 23700:00

uh so we shouted out the Ronan and I

## 23700:00 - 23725:00

argument we'll we'll go into that in

## 23725:00 - 23765:00

More Everything uh we can share about

## 23765:00 - 23815:00

GPT 4.5 coming up tomorrow on the Friday

## 23815:00 - 23840:00

show thanks for listening thanks again

## 23840:00 - 23865:00

to Mark and open AI for the for the

## 23865:00 - 23900:00

interview and we'll see you next time on

## 23900:00+

big technology podcast

