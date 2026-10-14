---
source: https://www.youtube.com/watch?v=LznOHjLLBQ8
title: "EM Group Chat #094: Solving The Cold Start Problem With Andrew Chen"
author: Everything Marketplaces
date: 2022-04-15
views: 8837
description: |-
  Recording of the Everything Marketplaces Group Chat #094 (4/5) with Andrew Chen, who's a General Partner at Andreessen Horowitz (a16z). Andrew focuses on marketplace investments at a16z, where they've invested in notable marketplaces like Airbnb, Lyft, Hipcamp, Neighbor, and more. Andrew is a top mind when it comes to marketplaces and is also the author of The Cold Start Problem.

  0:05 Intro
  1:22 Andrew's background
  3:45 Writing The Cold Start Problem
  5:34 Initially solving the cold start problem & atomic networks
  10:42 How to build & measure strong initial atomic networks
  16:05 Thinking through marketplace expansion (categories, new markets, layering on services, etc)
  20:06 Examples of marketplace expansion & playbooks
  24:25 Key learnings from The Cold Start Problem & tips for early stage marketplace founders
  27:30 Group Q&A on timing for marketplace expansion & the pull for launching new categories
  31:36 Group Q&A on how to think about defensibility with marketplaces
  35:34 Group Q&A on how to quantify community & users without monetization
  38:47 Group Q&A on how much to focus on one side of a marketplace early-on
  40:51 Group Q&A on adverse selection with marketplaces

  Follow-up thread for Q&A with Andrew on Twitter: https://twitter.com/Yoroomie/status/1511399144350384128?s=20&t=j2AgkckY7lMZ7i6_4wI83Q

  Andrew's blog: https://www.andrewchen.com
  The Cold Start Problem: https://www.coldstart.com
  a16z: https://www.a16z.com

  Join other marketplace founders & all of our group chats: http://www.everythingmarketplaces.com
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:21:29.937Z
---

# EM Group Chat #094: Solving The Cold Start Problem With Andrew Chen

## 00:00 - 20:00

so welcome back to everything

## 20:00 - 55:00

marketplaces for a talk with founders

## 55:00 - 80:00

and leaders from some of today's top

## 80:00 - 125:00

marketplaces so this is episode 94 which

## 125:00 - 150:00

is a very special group chat that we

## 150:00 - 180:00

just had with the one and only andrew

## 180:00 - 210:00

chen who's a partner at anderson

## 210:00 - 235:00

horowitz and is also the author of the

## 235:00 - 275:00

cold start problem so andrew is one off

## 275:00 - 305:00

if not the top minds when it comes to

## 305:00 - 345:00

both marketplaces and network effects so

## 345:00 - 375:00

this is a really incredible chat that we

## 375:00 - 400:00

just had with andrew where we got to

## 400:00 - 425:00

discuss the cold start problem in more

## 425:00 - 460:00

detail dove into some of the specific

## 460:00 - 500:00

topics that he covered such as atomic

## 500:00 - 530:00

networks and also i had a really great q

## 530:00 - 565:00

a for those on the chat so i really

## 565:00 - 595:00

enjoyed this conversation i felt like it

## 595:00 - 625:00

was almost a master class for you know

## 625:00 - 660:00

both marketplaces and network effects

## 660:00 - 675:00

and so i know you're going to find a

## 675:00 - 800:00

really great watch to the end

## 800:00 - 830:00

so andrew welcome to the group chat and

## 830:00 - 860:00

wow this is a huge treat to have you

## 860:00 - 890:00

join us here today is uh you know you're

## 890:00 - 915:00

definitely one of the most requested

## 915:00 - 945:00

group chat guests in the you know the

## 945:00 - 980:00

cold start problem should be a required

## 980:00 - 1010:00

reading for every uh marketplace founder

## 1010:00 - 1040:00

and leader um you know so i'm really

## 1040:00 - 1080:00

excited to uh you know chat with you uh

## 1080:00 - 1100:00

about the cold start problem a little

## 1100:00 - 1125:00

bit more detail on some of the topics

## 1125:00 - 1160:00

that you covered in the uh in the book

## 1160:00 - 1185:00

and i also have a group q a here with

## 1185:00 - 1220:00

some that are on the chat today um but

## 1220:00 - 1245:00

before we do though i think it might be

## 1245:00 - 1265:00

great if you can start off by showing a

## 1265:00 - 1285:00

little bit more on your background those

## 1285:00 - 1315:00

that uh you know don't know useful and

## 1315:00 - 1350:00

then uh you know what led you to uh to

## 1350:00 - 1375:00

writing the cold start problem yeah

## 1375:00 - 1400:00

definitely well um

## 1400:00 - 1430:00

uh so so i've been at introducing

## 1430:00 - 1460:00

norwoods now for four years and one of

## 1460:00 - 1510:00

my primary investment areas um is is

## 1510:00 - 1545:00

marketplaces and so

## 1545:00 - 1580:00

um we actually just did one uh a month

## 1580:00 - 1620:00

ago actually we just did two uh in in

## 1620:00 - 1655:00

last month which has been great um and

## 1655:00 - 1700:00

then the firm also um with jeff jordan

## 1700:00 - 1735:00

um who was ceo of opentable and before

## 1735:00 - 1775:00

that was at ebay um you know we've done

## 1775:00 - 1810:00

a whole bunch over the years we've we've

## 1810:00 - 1840:00

ended up investing in

## 1840:00 - 1900:00

airbnb and instacart and lyft um and you

## 1900:00 - 1930:00

know many others um and then before

## 1930:00 - 1995:00

before uh my career in investing um i

## 1995:00 - 2025:00

was at uber during the hyper growth

## 2025:00 - 2050:00

years of the company and so i talked

## 2050:00 - 2095:00

about it in the book of course um but

## 2095:00 - 2135:00

this was a period where we were adding

## 2135:00 - 2160:00

um three percent of the world's

## 2160:00 - 2205:00

population onto the platform each year

## 2205:00 - 2250:00

we were spending 300 million dollars um

## 2250:00 - 2290:00

annually on the give get program you

## 2290:00 - 2320:00

know give get give ten dollars get ten

## 2320:00 - 2365:00

dollars and another billion dollars on

## 2365:00 - 2405:00

paid marketing um and then i was part of

## 2405:00 - 2455:00

the executive group um uh that oversaw

## 2455:00 - 2480:00

the us regent and so that was a 30

## 2480:00 - 2535:00

billion dollar p l um and we met weekly

## 2535:00 - 2565:00

it was myself and travis and our head of

## 2565:00 - 2600:00

finance our head of operations you know

## 2600:00 - 2630:00

about a dozen other people

## 2630:00 - 2675:00

um to to to run the company

## 2675:00 - 2700:00

um and then before that i was a founder

## 2700:00 - 2740:00

so um i actually raised money from

## 2740:00 - 2755:00

um

## 2755:00 - 2785:00

marc andreessen and ben horowitz for my

## 2785:00 - 2810:00

seed round and index vendors and

## 2810:00 - 2840:00

ignition partners for my series a and i

## 2840:00 - 2860:00

was working on a bunch of you know

## 2860:00 - 2890:00

facebook apps back when that was a thing

## 2890:00 - 2925:00

um and sold that sold myself from the

## 2925:00 - 2965:00

team to uber um as part of that and so

## 2965:00 - 3000:00

i've kind of you know straddled kind of

## 3000:00 - 3040:00

social um and that's you know one of my

## 3040:00 - 3065:00

investment areas and the marketplaces is

## 3065:00 - 3100:00

kind of being the other which is why the

## 3100:00 - 3125:00

various case studies in the book are

## 3125:00 - 3145:00

kind of about that and then yeah

## 3145:00 - 3180:00

personally i am splitting my time

## 3180:00 - 3220:00

between san francisco and la um and so

## 3220:00 - 3255:00

i've probably been more in la than sf

## 3255:00 - 3290:00

recently i happen to be in sf right now

## 3290:00 - 3330:00

um in lower pack heights next to japan

## 3330:00 - 3375:00

town and uh in fillmore if you guys know

## 3375:00 - 3430:00

sf um and yeah and so and

## 3430:00 - 3470:00

you know the book was released in early

## 3470:00 - 3525:00

december and selling super well and um

## 3525:00 - 3555:00

you can come to the a16z lobby whenever

## 3555:00 - 3590:00

you want and pick up a pic pick up an

## 3590:00 - 3625:00

extra copy um but yeah it's been a

## 3625:00 - 3655:00

really fun uh thing to work on

## 3655:00 - 3680:00

yeah i saw quite the incredible uh

## 3680:00 - 3705:00

background you know thanks for giving us

## 3705:00 - 3740:00

a kind of quick rundown on that and yeah

## 3740:00 - 3770:00

you know as we did mention here uh right

## 3770:00 - 3800:00

before we started recording uh certainly

## 3800:00 - 3825:00

the cold start problem is kind of like

## 3825:00 - 3855:00

the uh you know defective uh kind of

## 3855:00 - 3880:00

go-to handbook for us all in the world

## 3880:00 - 3915:00

of marketplaces you know so what led you

## 3915:00 - 3965:00

to uh to actually you know to write that

## 3965:00 - 4015:00

yeah well i think um uh i've been i've

## 4015:00 - 4065:00

been writing for a long time on my blog

## 4065:00 - 4110:00

um and uh and which is just you know my

## 4110:00 - 4155:00

name andrewchat.com and um you know one

## 4155:00 - 4195:00

of the big things after writing almost a

## 4195:00 - 4225:00

thousand essays was huh i should

## 4225:00 - 4260:00

probably like organize some of it um in

## 4260:00 - 4300:00

a way that made sense for a long time

## 4300:00 - 4340:00

one of the things i would do is take a

## 4340:00 - 4375:00

piece of industry terminology whether

## 4375:00 - 4430:00

that's you know viral loops or you know

## 4430:00 - 4475:00

cost of customer acquisition or

## 4475:00 - 4520:00

um or or you know something like that

## 4520:00 - 4560:00

and try to write the definitive piece

## 4560:00 - 4580:00

about that

## 4580:00 - 4620:00

you know piece of terminology um and so

## 4620:00 - 4650:00

one of the one of the one of the things

## 4650:00 - 4675:00

that comes up a lot in marketplace

## 4675:00 - 4725:00

companies is as many of you know the

## 4725:00 - 4790:00

chicken and egg you know problem the

## 4790:00 - 4810:00

um

## 4810:00 - 4850:00

you know the bootstrapping problem you

## 4850:00 - 4885:00

know it's known by various names right

## 4885:00 - 4920:00

or you know as i described it the cold

## 4920:00 - 4940:00

start problem

## 4940:00 - 4995:00

um and try to uh and really define that

## 4995:00 - 5050:00

in in the best um way that i can and so

## 5050:00 - 5090:00

i started writing it uh three years ago

## 5090:00 - 5105:00

and

## 5105:00 - 5140:00

ended up interviewing just an amazing

## 5140:00 - 5185:00

set of people everyone from the ceos and

## 5185:00 - 5240:00

founders of zoom and slack and tinder

## 5240:00 - 5275:00

and a lot of early airbnb employees a

## 5275:00 - 5325:00

lot of early lift and uber and sidecar

## 5325:00 - 5350:00

employees

## 5350:00 - 5380:00

you know folks from all over and that

## 5380:00 - 5415:00

was just incredibly fun to to put

## 5415:00 - 5445:00

something together that that sort of you

## 5445:00 - 5470:00

know talks about the entire field

## 5470:00 - 5500:00

yeah certainly i can certainly imagine

## 5500:00 - 5540:00

that a lot lots of uh great stories uh

## 5540:00 - 5575:00

that you included in there um so you

## 5575:00 - 5600:00

know you did a really great job as far

## 5600:00 - 5630:00

as you know kind of laying out well

## 5630:00 - 5655:00

first off kind of like defining the cold

## 5655:00 - 5685:00

start problem and then uh you know

## 5685:00 - 5715:00

laying it out in the various stages um

## 5715:00 - 5750:00

and you know one of the stages that you

## 5750:00 - 5775:00

mentioned and kind of concepts you laid

## 5775:00 - 5820:00

out uh in the book um you know as far as

## 5820:00 - 5855:00

atomic networks um that's something

## 5855:00 - 5880:00

that's come up quite a bit here since

## 5880:00 - 5910:00

most of us are early stage marketplace

## 5910:00 - 5940:00

founders and teams and uh you know i

## 5940:00 - 5965:00

love to dive into that topic a little

## 5965:00 - 5985:00

bit more

## 5985:00 - 6045:00

yeah definitely um well the the main

## 6045:00 - 6105:00

case study that i use um that that is uh

## 6105:00 - 6140:00

that's that's uh in the book is

## 6140:00 - 6180:00

um how tinder got started and off the

## 6180:00 - 6205:00

ground and the amazing thing about

## 6205:00 - 6230:00

tinder is

## 6230:00 - 6275:00

um as a story is that um they actually

## 6275:00 - 6325:00

got the product idea right

## 6325:00 - 6360:00

uh pretty much from the beginning and so

## 6360:00 - 6390:00

when it was just sean rad

## 6390:00 - 6430:00

um and jonathan bedin and ryan ogle and

## 6430:00 - 6455:00

like kind of this crew of about four or

## 6455:00 - 6485:00

five people

## 6485:00 - 6525:00

the original app that came up that they

## 6525:00 - 6565:00

came up with was actually pretty much

## 6565:00 - 6595:00

spot on like they had big photos they

## 6595:00 - 6630:00

had sign in with facebook they had the

## 6630:00 - 6670:00

swiping they had you know they had a lot

## 6670:00 - 6715:00

of the right features pretty much um you

## 6715:00 - 6740:00

know off the bat and this is something i

## 6740:00 - 6770:00

think also for many of us in in the

## 6770:00 - 6815:00

marketplace side of things you know um

## 6815:00 - 6845:00

building like a rideshare app from

## 6845:00 - 6875:00

scratch like okay great that that does

## 6875:00 - 6905:00

have you know you you have to innovate a

## 6905:00 - 6940:00

lot for that but if you look at what

## 6940:00 - 6955:00

like

## 6955:00 - 6985:00

stockx is doing or you look at what

## 6985:00 - 7045:00

cameo is doing or you look at what

## 7045:00 - 7070:00

you know a lot of these modern

## 7070:00 - 7120:00

marketplaces are doing they actually the

## 7120:00 - 7160:00

the primary structure of them is

## 7160:00 - 7195:00

actually not that different than

## 7195:00 - 7230:00

products from 10 years ago you know you

## 7230:00 - 7265:00

need some concept of a listing you need

## 7265:00 - 7290:00

some search capability you need some

## 7290:00 - 7325:00

browse capability

## 7325:00 - 7360:00

and so because of that you can actually

## 7360:00 - 7405:00

nail the product side fairly easily and

## 7405:00 - 7430:00

if you sort of believe in the lean

## 7430:00 - 7455:00

startup side of the world if you just

## 7455:00 - 7480:00

have the right features and you have the

## 7480:00 - 7510:00

killer product you know that should be

## 7510:00 - 7540:00

that should be it right okay well but

## 7540:00 - 7555:00

that's not what the temperature of folks

## 7555:00 - 7590:00

figured out right the what the tigger

## 7590:00 - 7620:00

folks figured out was they basically

## 7620:00 - 7645:00

built this app it was all the right

## 7645:00 - 7665:00

features

## 7665:00 - 7705:00

and then what ended up happening um that

## 7705:00 - 7750:00

that was problematic was they basically

## 7750:00 - 7785:00

spent the first six months just inviting

## 7785:00 - 7810:00

their friends to use the app they just

## 7810:00 - 7845:00

text them and i try to get them to on

## 7845:00 - 7880:00

there and you'd swipe through like five

## 7880:00 - 7925:00

profiles and then you'd immediately uh

## 7925:00 - 7955:00

run out of people and then that was it

## 7955:00 - 7995:00

and so they realized that okay it wasn't

## 7995:00 - 8025:00

enough to just build the right features

## 8025:00 - 8050:00

they needed to get the right network

## 8050:00 - 8085:00

into the app as well and one of the big

## 8085:00 - 8115:00

questions is well how many people do you

## 8115:00 - 8130:00

need

## 8130:00 - 8175:00

in an app like that in order for it for

## 8175:00 - 8205:00

it to work and and this is where kind of

## 8205:00 - 8225:00

a thought experiment would be very

## 8225:00 - 8250:00

valuable which is

## 8250:00 - 8305:00

it's very clear that having 500 people

## 8305:00 - 8345:00

all from the same city with the same

## 8345:00 - 8380:00

context who are all single who are all

## 8380:00 - 8415:00

looking for the same thing that that is

## 8415:00 - 8445:00

much more effective

## 8445:00 - 8495:00

than um if you got one or two people

## 8495:00 - 8510:00

from

## 8510:00 - 8540:00

you know 10 different universities

## 8540:00 - 8590:00

around the world because the the the

## 8590:00 - 8630:00

because then it would be too fragmented

## 8630:00 - 8670:00

and so there's sort of this idea that

## 8670:00 - 8705:00

okay yeah you actually need density you

## 8705:00 - 8730:00

need clustering

## 8730:00 - 8780:00

um of a network in order for it to be

## 8780:00 - 8820:00

valuable and so because of that what

## 8820:00 - 8845:00

what tinder ended up doing was they

## 8845:00 - 8860:00

ended up

## 8860:00 - 8890:00

throwing a birthday party they posted

## 8890:00 - 8935:00

bouncers in front of the um you know in

## 8935:00 - 8970:00

front of the birthday party and as a

## 8970:00 - 9020:00

result they were able to um get 500

## 9020:00 - 9045:00

people at usc

## 9045:00 - 9085:00

um one of the local universities in la

## 9085:00 - 9130:00

to to install um to install the app and

## 9130:00 - 9170:00

then as a result it just took over usc

## 9170:00 - 9195:00

from there and then they basically were

## 9195:00 - 9210:00

able

## 9210:00 - 9250:00

they realized okay great if if they can

## 9250:00 - 9300:00

build a network and that's what happens

## 9300:00 - 9320:00

they should be able to build a second

## 9320:00 - 9350:00

network and a third network and like

## 9350:00 - 9385:00

keep going from there and so i think you

## 9385:00 - 9405:00

know for many of us that are thinking

## 9405:00 - 9440:00

about this from a marketplace context

## 9440:00 - 9480:00

it's the reason why it's so hard when

## 9480:00 - 9505:00

you build a marketplace to launch in

## 9505:00 - 9530:00

five cities at once right at the

## 9530:00 - 9560:00

beginning or to launch in five different

## 9560:00 - 9590:00

product verticals at once at the

## 9590:00 - 9610:00

beginning and why

## 9610:00 - 9645:00

you see so often that marketplace

## 9645:00 - 9675:00

companies you know ebay's case start

## 9675:00 - 9725:00

start out with um you know collectibles

## 9725:00 - 9770:00

and sort of expand from there or

## 9770:00 - 9805:00

why you see you know uber start from

## 9805:00 - 9840:00

kind of limos and black car services

## 9840:00 - 9885:00

before and and and to do it all in san

## 9885:00 - 9915:00

francisco and to show that i can work in

## 9915:00 - 9945:00

san francisco before expanding to other

## 9945:00 - 9980:00

service lines and in other cities and so

## 9980:00 - 10025:00

i think that that sort of nugget of like

## 10025:00 - 10080:00

density as kind of a major advantage um

## 10080:00 - 10115:00

and and sort of you know the idea is if

## 10115:00 - 10140:00

you can build one you can probably build

## 10140:00 - 10180:00

many i think that that's an important um

## 10180:00 - 10210:00

you know point in realization that i

## 10210:00 - 10235:00

think many of us

## 10235:00 - 10265:00

in in the marketplace industry

## 10265:00 - 10305:00

have a better sense of versus

## 10305:00 - 10335:00

interestingly enough if you work at a

## 10335:00 - 10360:00

bigger company if you work at a google

## 10360:00 - 10390:00

or an apple and you work in the digital

## 10390:00 - 10430:00

world you tend to not actually want to

## 10430:00 - 10465:00

launch small and grow from there you

## 10465:00 - 10505:00

tend to want to kind of blast out the

## 10505:00 - 10545:00

whole world and have like a big pr push

## 10545:00 - 10595:00

um and and as a result you know uh of of

## 10595:00 - 10630:00

course you end up with the problem that

## 10630:00 - 10655:00

a lot of those products end up not

## 10655:00 - 10680:00

working because they can't they can't

## 10680:00 - 10715:00

actually sustain their network effects

## 10715:00 - 10745:00

yeah yeah that's a really great example

## 10745:00 - 10775:00

and uh you know certainly are relatable

## 10775:00 - 10820:00

to a lot of us here um you know so uh i

## 10820:00 - 10845:00

i did want to go a little bit deeper on

## 10845:00 - 10875:00

that you know so uh for early-stage

## 10875:00 - 10910:00

marketplaces right so like how should we

## 10910:00 - 10950:00

think about what that like initial kind

## 10950:00 - 10995:00

of um you know atomic network looks like

## 10995:00 - 11020:00

and then how will we think about you

## 11020:00 - 11055:00

know measuring like what a strong kind

## 11055:00 - 11090:00

of uh net network looks like or you know

## 11090:00 - 11115:00

kind of like maybe initial product

## 11115:00 - 11140:00

market fit yeah

## 11140:00 - 11195:00

yeah well i think i think uh um

## 11195:00 - 11230:00

i think there's a conceptual thing and

## 11230:00 - 11265:00

then there's an empirical thing um so on

## 11265:00 - 11310:00

the conceptual side i think you can

## 11310:00 - 11330:00

reason

## 11330:00 - 11390:00

uh and just think well you know for a

## 11390:00 - 11420:00

product like zoom

## 11420:00 - 11460:00

um how many people do i need in order to

## 11460:00 - 11500:00

make it useful right and you can kind of

## 11500:00 - 11525:00

view it as like well it's pretty clear

## 11525:00 - 11555:00

that you can have a conversation with

## 11555:00 - 11590:00

just an individual and that should be

## 11590:00 - 11615:00

and that's very useful

## 11615:00 - 11650:00

um and with the marketplace company on

## 11650:00 - 11690:00

the other hand you know if if uh you

## 11690:00 - 11725:00

know something like um uber where the

## 11725:00 - 11760:00

drivers are fungible you know the fact

## 11760:00 - 11815:00

that um you know one uber x driver from

## 11815:00 - 11845:00

20 minutes away versus an uber driver

## 11845:00 - 11870:00

that's that's five minutes away if

## 11870:00 - 11900:00

they're sort of interchangeable that is

## 11900:00 - 11940:00

a very different kind of marketplace

## 11940:00 - 11975:00

than something like airbnb

## 11975:00 - 12010:00

where you might have two different homes

## 12010:00 - 12050:00

and you might not want you might think

## 12050:00 - 12075:00

oh this one has a hot tub and this one

## 12075:00 - 12105:00

doesn't that's maybe what one consumer

## 12105:00 - 12140:00

thinks another consumer might think oh

## 12140:00 - 12160:00

well this one's next to the park because

## 12160:00 - 12200:00

i have a dog i want that versus another

## 12200:00 - 12235:00

so in those cases the locations are

## 12235:00 - 12280:00

non-fungible um and so because of that

## 12280:00 - 12300:00

you may have different things and you

## 12300:00 - 12335:00

have to reason into

## 12335:00 - 12360:00

how to figure it out i think from an

## 12360:00 - 12410:00

empirical standpoint it's much harder

## 12410:00 - 12435:00

kind of like pre-launch

## 12435:00 - 12490:00

to figure out like okay well how many um

## 12490:00 - 12520:00

uh how how much of a network do i need

## 12520:00 - 12545:00

to build but i think there's a very kind

## 12545:00 - 12580:00

of easy rule of thumb which is if you

## 12580:00 - 12610:00

were if you were to go back to the

## 12610:00 - 12660:00

tinder team and you were to say okay

## 12660:00 - 12725:00

we only have like 100 people in this app

## 12725:00 - 12785:00

um and and we have this xyz bounce rate

## 12785:00 - 12830:00

now if we add another 100 people do we

## 12830:00 - 12855:00

see that there's more engagement to be

## 12855:00 - 12875:00

had

## 12875:00 - 12905:00

and i think you very quickly say oh well

## 12905:00 - 12925:00

there is

## 12925:00 - 12960:00

and then and then and then you can say

## 12960:00 - 12985:00

well what happens if you add more and

## 12985:00 - 13010:00

you launch in more cities and then what

## 13010:00 - 13045:00

you find is oh yes there is

## 13045:00 - 13080:00

and eventually you get to a point where

## 13080:00 - 13115:00

it doesn't matter you know if like

## 13115:00 - 13145:00

probably in san francisco i would guess

## 13145:00 - 13180:00

that tinder has something like

## 13180:00 - 13225:00

50 000 profiles like i'm probably never

## 13225:00 - 13255:00

going to swipe 50 000 profiles so as a

## 13255:00 - 13285:00

result the difference between 50 000

## 13285:00 - 13325:00

profiles and 25 000 profiles the

## 13325:00 - 13365:00

retention curve between two cities that

## 13365:00 - 13410:00

kind of have one versus the other

## 13410:00 - 13435:00

stops mattering because you start

## 13435:00 - 13465:00

getting that diminishing return effect

## 13465:00 - 13495:00

which is kind of this s-curve

## 13495:00 - 13520:00

that i mentioned you know in the cold

## 13520:00 - 13545:00

start problem which also exists by the

## 13545:00 - 13585:00

way you know in in uber drivers

## 13585:00 - 13625:00

eventually because eventually you get

## 13625:00 - 13655:00

three minute etas and you're like okay

## 13655:00 - 13695:00

yeah i don't the difference between

## 13695:00 - 13720:00

ten thousand drivers in san francisco

## 13720:00 - 13755:00

versus eleven thousand is very different

## 13755:00 - 13790:00

than you know a thousand drivers 2 000

## 13790:00 - 13815:00

drivers even though the delta is only a

## 13815:00 - 13850:00

thousand drivers in both cases

## 13850:00 - 13875:00

um doubling the number of drivers is

## 13875:00 - 13900:00

just you know provides a much better

## 13900:00 - 13920:00

level of service so i think i think you

## 13920:00 - 13935:00

can do that

## 13935:00 - 13960:00

and then when you're big one day when

## 13960:00 - 14000:00

you're big and you have many many market

## 14000:00 - 14040:00

marketplaces many many different things

## 14040:00 - 14070:00

what you can do is you can you can build

## 14070:00 - 14110:00

a scatter plot ultimately right so

## 14110:00 - 14145:00

ultimately and we were able to do this

## 14145:00 - 14170:00

at uber you can basically build an

## 14170:00 - 14225:00

x-axis which is the size of your network

## 14225:00 - 14250:00

that might be a city that might be a

## 14250:00 - 14280:00

company that might be a team

## 14280:00 - 14305:00

you know what however you define your

## 14305:00 - 14345:00

network and then you define a y-axis

## 14345:00 - 14400:00

which is like your some kind of value uh

## 14400:00 - 14435:00

you know sort of uh metric so that might

## 14435:00 - 14445:00

be

## 14445:00 - 14485:00

um you know sort of how you how you view

## 14485:00 - 14505:00

um

## 14505:00 - 14540:00

uh you know that might be retention rate

## 14540:00 - 14565:00

or conversion rate or something like

## 14565:00 - 14595:00

that and what you'll see is and then

## 14595:00 - 14625:00

every dot that you put on this graph

## 14625:00 - 14650:00

ends up being kind of one of your

## 14650:00 - 14680:00

networks so let's say your b2b company

## 14680:00 - 14705:00

let's say your dropbox or something like

## 14705:00 - 14735:00

that what you might find is you might

## 14735:00 - 14785:00

find that um there's an s-curve because

## 14785:00 - 14825:00

when there's a lot of when there are not

## 14825:00 - 14860:00

that many users in your company that are

## 14860:00 - 14885:00

using actually i'll use slack that might

## 14885:00 - 14905:00

be cleaner so if there's not a lot of

## 14905:00 - 14940:00

people in your company using slack your

## 14940:00 - 14975:00

retention will be good

## 14975:00 - 15015:00

but not like incredible and then at some

## 15015:00 - 15045:00

point it's going to really pick up

## 15045:00 - 15070:00

because it's like oh my god everyone in

## 15070:00 - 15095:00

my company is using slack

## 15095:00 - 15130:00

it's our primary you know sort of

## 15130:00 - 15160:00

communication mechanism but then there's

## 15160:00 - 15195:00

going to be a little bit of an s curve

## 15195:00 - 15215:00

because eventually you'll get to a point

## 15215:00 - 15235:00

where it's like i just have too many

## 15235:00 - 15270:00

notifications i have like too many too

## 15270:00 - 15290:00

many coworkers that are trying to pick

## 15290:00 - 15310:00

me if any of you have worked in the

## 15310:00 - 15330:00

company with

## 15330:00 - 15360:00

hundreds or thousands of people that all

## 15360:00 - 15400:00

you slack you know that that experience

## 15400:00 - 15430:00

would be familiar and you start using

## 15430:00 - 15460:00

slack more as one-to-one messaging or

## 15460:00 - 15500:00

small group messaging and you stop going

## 15500:00 - 15535:00

to all the big you know big channels

## 15535:00 - 15570:00

and so um so that becomes the other way

## 15570:00 - 15615:00

to see it because if you find that you

## 15615:00 - 15650:00

plot all of your your your various

## 15650:00 - 15700:00

networks and you're only staying up

## 15700:00 - 15725:00

up into the right and you're not yet

## 15725:00 - 15765:00

seeing the plateau what that tells you

## 15765:00 - 15795:00

is that most likely

## 15795:00 - 15835:00

um you can keep going you can keep being

## 15835:00 - 15875:00

more dense in your in your networks and

## 15875:00 - 15895:00

and kind of continue from there so

## 15895:00 - 15925:00

anyway that that's that's how i i would

## 15925:00 - 15950:00

comprehensively answer your question

## 15950:00 - 15970:00

yeah i know that's uh that's really a

## 15970:00 - 15990:00

great answer and i know it's going to

## 15990:00 - 16015:00

lead to some questions here when we get

## 16015:00 - 16060:00

to the to the group q a um but you know

## 16060:00 - 16085:00

i wanted to this is a good kind of segue

## 16085:00 - 16115:00

into you know um

## 16115:00 - 16135:00

assuming that you know it's an early

## 16135:00 - 16160:00

stage kind of marketplace that you you

## 16160:00 - 16190:00

know you do uh you know have that like

## 16190:00 - 16225:00

kind of initial atomic network you know

## 16225:00 - 16250:00

one of the next kind of like uh things

## 16250:00 - 16275:00

to think you know that a lot of us here

## 16275:00 - 16310:00

think about is you know as far as

## 16310:00 - 16350:00

potentially uh layering on new use cases

## 16350:00 - 16395:00

um services or expanding um you know

## 16395:00 - 16435:00

locations right as far as geographies so

## 16435:00 - 16465:00

how do you kind of uh you know when

## 16465:00 - 16485:00

you're chatting with like early stage

## 16485:00 - 16525:00

marketplaces how do you uh kind of you

## 16525:00 - 16555:00

know help them think through this

## 16555:00 - 16585:00

yeah i think i think it depends on what

## 16585:00 - 16610:00

you're trying to do right i think that

## 16610:00 - 16645:00

there is a world where

## 16645:00 - 16700:00

um you have decided that uh your core

## 16700:00 - 16725:00

thing is working

## 16725:00 - 16760:00

um and if your core if your core

## 16760:00 - 16785:00

business is working and you've been able

## 16785:00 - 16820:00

to build an atomic network then the

## 16820:00 - 16865:00

question is okay well how well can you

## 16865:00 - 16905:00

build a second one or a third one or a

## 16905:00 - 16925:00

fourth one

## 16925:00 - 16980:00

and um and and what's certainly easier

## 16980:00 - 17025:00

um is to take the atomic network that

## 17025:00 - 17055:00

you've built in one place whether that's

## 17055:00 - 17090:00

again that's a camp one campus or one

## 17090:00 - 17130:00

city or one team and to just build a

## 17130:00 - 17165:00

second copy of it and you're really just

## 17165:00 - 17205:00

copying and pasting right i think that

## 17205:00 - 17265:00

is itself hard enough but that is

## 17265:00 - 17290:00

relatively easy

## 17290:00 - 17315:00

compared to

## 17315:00 - 17345:00

layering on an additional service or

## 17345:00 - 17380:00

product like that tends to be you're

## 17380:00 - 17415:00

taking on real um you know sort of

## 17415:00 - 17440:00

market risk by doing that because you

## 17440:00 - 17465:00

just don't know if that's going to be

## 17465:00 - 17525:00

possible or not um and so i think you

## 17525:00 - 17570:00

know the the usually kind of from a

## 17570:00 - 17610:00

staging standpoint what i would say is

## 17610:00 - 17660:00

the seed round is really for um getting

## 17660:00 - 17690:00

your initial product to market

## 17690:00 - 17720:00

your series a

## 17720:00 - 17750:00

where usually what we are finding is

## 17750:00 - 17775:00

we're usually doing them between three

## 17775:00 - 17825:00

to five million in gross revenue

## 17825:00 - 17855:00

um in in gmb

## 17855:00 - 17905:00

and when we do the series a around that

## 17905:00 - 17935:00

typically there may be only in one

## 17935:00 - 17965:00

market they might be in the market and a

## 17965:00 - 18000:00

half or something like that but we don't

## 18000:00 - 18030:00

expect them to be in three markets or

## 18030:00 - 18055:00

five markets or ten markets or whatever

## 18055:00 - 18075:00

and they're raising

## 18075:00 - 18100:00

something in the realm of kind of like

## 18100:00 - 18135:00

10 million bucks plus or minus

## 18135:00 - 18170:00

um what we find in the series b though

## 18170:00 - 18200:00

once we get into like kind of a growth

## 18200:00 - 18255:00

stage if it's you know if it becomes

## 18255:00 - 18280:00

kind of more of a stretch it becomes

## 18280:00 - 18310:00

like a 20 million dollar raise 25

## 18310:00 - 18345:00

million dollar raise then you're really

## 18345:00 - 18390:00

expecting okay the like the the copy and

## 18390:00 - 18425:00

paste machine is really working

## 18425:00 - 18470:00

right and not only do we see this

## 18470:00 - 18505:00

company in multiple cities or multiple

## 18505:00 - 18535:00

teams or multiple campuses or you know

## 18535:00 - 18565:00

however way you want to cut it

## 18565:00 - 18595:00

but also

## 18595:00 - 18625:00

um they're able to to

## 18625:00 - 18675:00

to replicate this very consistently and

## 18675:00 - 18720:00

so one of the things i often ask for is

## 18720:00 - 18765:00

um some kind of a you know like gmb on

## 18765:00 - 18790:00

the y-axis

## 18790:00 - 18840:00

and then the x-axis is time

## 18840:00 - 18865:00

and then every and then have you have

## 18865:00 - 18895:00

multiple lines each one is its own city

## 18895:00 - 18920:00

or each one is its own team and what you

## 18920:00 - 18940:00

want to see is that

## 18940:00 - 18970:00

every single one of these new networks

## 18970:00 - 19000:00

that's being up and running is working

## 19000:00 - 19045:00

better and better than before um is one

## 19045:00 - 19070:00

of the things you start looking for and

## 19070:00 - 19125:00

then um and and and so um you know

## 19125:00 - 19170:00

oftentimes uh you know to to finish up

## 19170:00 - 19210:00

your question um it really just depends

## 19210:00 - 19250:00

on the on the on the timing of all these

## 19250:00 - 19265:00

things

## 19265:00 - 19300:00

um and i think i tend to be very

## 19300:00 - 19330:00

realistic about what you

## 19330:00 - 19365:00

can accomplish early

## 19365:00 - 19415:00

and so early on i tend to not push for

## 19415:00 - 19450:00

too many new

## 19450:00 - 19500:00

products or too many new geographies

## 19500:00 - 19540:00

because as long as you if if the market

## 19540:00 - 19580:00

is big enough you should be able to take

## 19580:00 - 19625:00

um an individual vertical whether that's

## 19625:00 - 19665:00

again a city or campus or whatever and

## 19665:00 - 19690:00

you should be able to show that that

## 19690:00 - 19730:00

individual atomic network is worth

## 19730:00 - 19750:00

hopefully

## 19750:00 - 19805:00

tens of millions of um of dollars

## 19805:00 - 19830:00

because if you're copying and pasting a

## 19830:00 - 19850:00

bunch of those you're going to

## 19850:00 - 19885:00

eventually run out and you want to make

## 19885:00 - 19910:00

sure that each atomic network is

## 19910:00 - 19940:00

valuable enough on its own so that when

## 19940:00 - 19965:00

you replicate it

## 19965:00 - 19990:00

300 times

## 19990:00 - 20020:00

um you know you're able to get something

## 20020:00 - 20060:00

where the where the gmb is in the

## 20060:00 - 20100:00

billions or tens of billions yeah that's

## 20100:00 - 20130:00

uh that's that's really helpful um so

## 20130:00 - 20155:00

you know what as far as on the on the

## 20155:00 - 20190:00

note is you know copy pasting and you

## 20190:00 - 20220:00

know kind of uh you know the playbook

## 20220:00 - 20250:00

and scaling in new markets um are there

## 20250:00 - 20285:00

any recent examples of you know maybe

## 20285:00 - 20315:00

earlier stage marketplaces you've seen

## 20315:00 - 20340:00

or you know worked with or maybe you

## 20340:00 - 20370:00

know advise um that have done this

## 20370:00 - 20405:00

really well um and maybe sharing a

## 20405:00 - 20425:00

little bit about you know what that

## 20425:00 - 20465:00

playbook is like that they've used

## 20465:00 - 20505:00

yeah definitely um well there's a couple

## 20505:00 - 20540:00

companies that um that we've invested in

## 20540:00 - 20575:00

recently uh that

## 20575:00 - 20610:00

that i can talk about um

## 20610:00 - 20660:00

so uh one one that i love and it might

## 20660:00 - 20685:00

you know and actually many of you guys

## 20685:00 - 20710:00

may some of you guys may even be

## 20710:00 - 20750:00

customers is a company called nash

## 20750:00 - 20790:00

and what it is is it's uh let me just uh

## 20790:00 - 20810:00

actually

## 20810:00 - 20855:00

pick it's like basic it's usenash.com so

## 20855:00 - 20885:00

i'll just i can now put it in the chat

## 20885:00 - 20915:00

right here okay yeah oh there it goes

## 20915:00 - 20955:00

okay i found it i found it right yeah

## 20955:00 - 20975:00

exactly it's this one

## 20975:00 - 21010:00

um yeah and so what they do is they

## 21010:00 - 21040:00

basically are

## 21040:00 - 21090:00

they've created a set of apis and apps

## 21090:00 - 21135:00

so that on one side of the network

## 21135:00 - 21190:00

um it is uh couriers and like fleets so

## 21190:00 - 21220:00

these are kind of like delivery you know

## 21220:00 - 21260:00

folks and like think of this as kind of

## 21260:00 - 21315:00

the long tail of uh delivery providers

## 21315:00 - 21345:00

that exist in every city and so this is

## 21345:00 - 21390:00

like bike messengers this is you know um

## 21390:00 - 21425:00

trucks with refrigeration in them this

## 21425:00 - 21460:00

is you know all sorts of people and then

## 21460:00 - 21500:00

on the flip side on the other side is

## 21500:00 - 21545:00

basically every everybody from um you

## 21545:00 - 21585:00

know florists and kind of you know small

## 21585:00 - 21645:00

businesses um and also apps right so

## 21645:00 - 21680:00

basically if you wanted to add delivery

## 21680:00 - 21735:00

to your app you could implement them um

## 21735:00 - 21785:00

in an api and and uh and integrate it

## 21785:00 - 21805:00

into your app and then that way you

## 21805:00 - 21825:00

wouldn't have to recruit drivers

## 21825:00 - 21845:00

yourself

## 21845:00 - 21870:00

um so that that's another you know

## 21870:00 - 21915:00

really really good one um and so and so

## 21915:00 - 21950:00

for this uh what i really enjoyed about

## 21950:00 - 21990:00

it um you know um

## 21990:00 - 22010:00

you know the way that the founders talk

## 22010:00 - 22040:00

about their business is

## 22040:00 - 22090:00

it's both geographical and digital

## 22090:00 - 22125:00

um in its own way because if you think

## 22125:00 - 22140:00

about it

## 22140:00 - 22185:00

the networks on the on the supply side

## 22185:00 - 22225:00

on the labor side which is the delivery

## 22225:00 - 22270:00

ultimately you actually have to go city

## 22270:00 - 22310:00

within a city and just call down and

## 22310:00 - 22345:00

basically just use sales right i think

## 22345:00 - 22380:00

one of the things that you find about

## 22380:00 - 22405:00

working with the hard side of the market

## 22405:00 - 22440:00

is you often end up being ends up being

## 22440:00 - 22465:00

very sales driven

## 22465:00 - 22495:00

um and so you're just calling calling

## 22495:00 - 22525:00

down calling down all these all these

## 22525:00 - 22545:00

providers which is which is what the

## 22545:00 - 22590:00

team's done on the flip side what you

## 22590:00 - 22635:00

end up doing on the demand side is

## 22635:00 - 22670:00

a lot of these are small businesses a

## 22670:00 - 22700:00

lot of these are apps

## 22700:00 - 22730:00

a lot of these are startups and they

## 22730:00 - 22770:00

exist not necessarily in the geography

## 22770:00 - 22795:00

part of what they want to do is they

## 22795:00 - 22830:00

want to build a new app

## 22830:00 - 22865:00

that basically can deliver anywhere and

## 22865:00 - 22910:00

so in that case um you know that you

## 22910:00 - 22970:00

know those networks are built um on a on

## 22970:00 - 23015:00

a sort of category by category basis um

## 23015:00 - 23045:00

whether that's like healthcare and

## 23045:00 - 23085:00

you're delivering coded tests or whether

## 23085:00 - 23120:00

that's food and you're you know working

## 23120:00 - 23150:00

with food food delivery providers

## 23150:00 - 23170:00

there's kind of lots of different ways

## 23170:00 - 23220:00

but that's an example of a recent um you

## 23220:00 - 23250:00

know investment of ours that

## 23250:00 - 23290:00

has approached it very interestingly

## 23290:00 - 23310:00

yeah that's a that's a great example

## 23310:00 - 23340:00

when you uh when you mention uh you know

## 23340:00 - 23370:00

being a sales letter sales driven you

## 23370:00 - 23400:00

got got a quite a few nods here in the

## 23400:00 - 23445:00

uh group chat so i think yes yeah can

## 23445:00 - 23475:00

relate to that well it's funny i mean i

## 23475:00 - 23505:00

think we ended up talking about that in

## 23505:00 - 23550:00

uber all the time where um we

## 23550:00 - 23580:00

the the operating team that would

## 23580:00 - 23625:00

basically run a city was kind of uh was

## 23625:00 - 23655:00

kind of a trio of people it was the

## 23655:00 - 23690:00

general manager who oversaw the entire

## 23690:00 - 23710:00

region

## 23710:00 - 23745:00

then there was a driver operations which

## 23745:00 - 23785:00

was basically a very sales driven very

## 23785:00 - 23810:00

hands-on

## 23810:00 - 23850:00

um you know very quantitative

## 23850:00 - 23885:00

and then there was a marketing manager

## 23885:00 - 23930:00

who tended to be more on the demand side

## 23930:00 - 23960:00

and that person tended to be

## 23960:00 - 24000:00

much more broadcast and demand in social

## 24000:00 - 24050:00

media performance marketing and so i

## 24050:00 - 24070:00

think that's one of the hardest things

## 24070:00 - 24095:00

about marketplace companies is you

## 24095:00 - 24130:00

ultimately have to master

## 24130:00 - 24170:00

all the skills needed to be a successful

## 24170:00 - 24195:00

consumer business and all the skills

## 24195:00 - 24240:00

needed to be a successful b2b company

## 24240:00 - 24275:00

and then you overlay you know fintech

## 24275:00 - 24315:00

and you also overlay uh international

## 24315:00 - 24340:00

you overlay all the other things it's

## 24340:00 - 24360:00

one of the most

## 24360:00 - 24400:00

complex business models um you know out

## 24400:00 - 24430:00

there which is which is uh you know part

## 24430:00 - 24445:00

of the fun

## 24445:00 - 24470:00

certainly so

## 24470:00 - 24495:00

um so we're gonna get in a group

## 24495:00 - 24515:00

questions here a little bit because

## 24515:00 - 24530:00

otherwise i feel like you and i could

## 24530:00 - 24560:00

just go on chatting for quite a bit um

## 24560:00 - 24600:00

but like right before we do though um so

## 24600:00 - 24630:00

i would love to learn you know what are

## 24630:00 - 24660:00

maybe like uh you know one to three kind

## 24660:00 - 24700:00

of like key takeaways or tips um you

## 24700:00 - 24730:00

know from from the cold start problem uh

## 24730:00 - 24760:00

that you like to share with us as early

## 24760:00 - 24805:00

as earlier probably marketplace founders

## 24805:00 - 24835:00

yeah i think i think the first thing is

## 24835:00 - 24865:00

just like know where you are

## 24865:00 - 24915:00

in in from a stage standpoint

## 24915:00 - 24955:00

um and and don't and don't fool yourself

## 24955:00 - 24995:00

there you know i think a lot of folks um

## 24995:00 - 25025:00

who don't have product market you know

## 25025:00 - 25060:00

fit basically think okay yeah i just

## 25060:00 - 25095:00

need to raise and burn a lot of money

## 25095:00 - 25130:00

and that's the right way to do it when

## 25130:00 - 25160:00

in fact uber

## 25160:00 - 25200:00

started out very very early on extremely

## 25200:00 - 25215:00

lean

## 25215:00 - 25260:00

and only start to spend enormous amounts

## 25260:00 - 25295:00

of money um once they were kind of

## 25295:00 - 25335:00

accelerating and going from there so i

## 25335:00 - 25375:00

think understanding where you are is is

## 25375:00 - 25400:00

important are you are you at the cold

## 25400:00 - 25425:00

start problem or are you at the tipping

## 25425:00 - 25455:00

point stage or are you working on

## 25455:00 - 25490:00

saturation like what are you working on

## 25490:00 - 25515:00

um and that you have different

## 25515:00 - 25545:00

strategies for different phases i think

## 25545:00 - 25570:00

that i think that's you know one of the

## 25570:00 - 25600:00

most important points that i make

## 25600:00 - 25650:00

um the second thing i would say is uh

## 25650:00 - 25700:00

there there is a long playbook of

## 25700:00 - 25730:00

different things that you can do um and

## 25730:00 - 25765:00

so some people they should build you

## 25765:00 - 25790:00

know they should do a come for the tools

## 25790:00 - 25835:00

stay for the network um uh you know kind

## 25835:00 - 25875:00

of strategy as coined by my my colleague

## 25875:00 - 25920:00

chris dixon or others maybe should be

## 25920:00 - 25945:00

subsidizing

## 25945:00 - 25970:00

all that growth

## 25970:00 - 26000:00

and i think the only way to figure out

## 26000:00 - 26055:00

ultimately is you can't remove the art

## 26055:00 - 26100:00

from all this like there's just a long

## 26100:00 - 26130:00

phase of experimentation

## 26130:00 - 26170:00

um that you end up going through and and

## 26170:00 - 26220:00

that's just that's just part and key to

## 26220:00 - 26255:00

um you know the whole thing um so so i

## 26255:00 - 26285:00

think i think that that's important and

## 26285:00 - 26345:00

then the final thing i'll mention is um

## 26345:00 - 26365:00

is that uh

## 26365:00 - 26405:00

um you know i think i think a lot of

## 26405:00 - 26450:00

times um you know what we're seeing

## 26450:00 - 26490:00

um in in the market is

## 26490:00 - 26530:00

um is that there's a there's a lack of

## 26530:00 - 26575:00

understanding around kind of the metrics

## 26575:00 - 26605:00

guidelines and targets that you need to

## 26605:00 - 26640:00

hit in order to show that you're

## 26640:00 - 26675:00

an interesting company and so for us

## 26675:00 - 26700:00

that's why we're always thinking about

## 26700:00 - 26730:00

and looking at

## 26730:00 - 26765:00

i reference this in kind of the the i

## 26765:00 - 26785:00

think it's like three quarters of the

## 26785:00 - 26815:00

way through the book kind of the triple

## 26815:00 - 26845:00

triple double double double framework

## 26845:00 - 26860:00

because

## 26860:00 - 26895:00

ultimately there is a minimum growth

## 26895:00 - 26920:00

rate that we need to see

## 26920:00 - 26955:00

and then similarly we want to see

## 26955:00 - 26985:00

retention rates at least on one side of

## 26985:00 - 27030:00

the network of you know over 50 annually

## 27030:00 - 27065:00

and there's a good reason for that also

## 27065:00 - 27090:00

based on benchmarks that we see it so i

## 27090:00 - 27125:00

know as a as a early

## 27125:00 - 27155:00

um as an as a you know when you're

## 27155:00 - 27180:00

building something really early it's

## 27180:00 - 27220:00

hard to assess like how good is my

## 27220:00 - 27250:00

product market fit and so i think

## 27250:00 - 27270:00

looking at some of those metrics and

## 27270:00 - 27305:00

comparing are are some of the you know

## 27305:00 - 27350:00

key ways to do it awesome that's uh

## 27350:00 - 27375:00

that's really helpful

## 27375:00 - 27415:00

um cool we're gonna jump right into some

## 27415:00 - 27455:00

of the uh questions um see quite a few

## 27455:00 - 27485:00

hands right but uh hey john uh do you

## 27485:00 - 27505:00

wanna jump on

## 27505:00 - 27520:00

cool

## 27520:00 - 27565:00

uh andrew thanks for being here um my

## 27565:00 - 27610:00

background is a pm at uber linkedin and

## 27610:00 - 27645:00

then a startup called curated so been

## 27645:00 - 27680:00

working in marketplaces for a while

## 27680:00 - 27695:00

i'm now

## 27695:00 - 27715:00

founder of a marketplace in the

## 27715:00 - 27760:00

expertise economy space

## 27760:00 - 27795:00

so i wanted to double click a little bit

## 27795:00 - 27830:00

more on timing for expansion and then

## 27830:00 - 27845:00

also

## 27845:00 - 27890:00

uh kind of what you see go wrong in

## 27890:00 - 27925:00

expansion um i think it's easy to start

## 27925:00 - 27955:00

to feel the pull from customers or

## 27955:00 - 27990:00

supply side and start to think you know

## 27990:00 - 28015:00

this is this is exactly the time we need

## 28015:00 - 28050:00

to go but then kind of underestimate the

## 28050:00 - 28090:00

team and the resources so um just

## 28090:00 - 28130:00

curious if you could speak more to

## 28130:00 - 28165:00

uh when you know it's absolutely time to

## 28165:00 - 28210:00

start going and expand that that network

## 28210:00 - 28245:00

or launch new categories and and kind of

## 28245:00 - 28285:00

what teams can do to prepare

## 28285:00 - 28350:00

uh to to actually expand successfully

## 28350:00 - 28380:00

yeah i mean it's funny enough i would

## 28380:00 - 28435:00

say that the the most common reason why

## 28435:00 - 28465:00

we end up um

## 28465:00 - 28510:00

uh seeing teams expand is

## 28510:00 - 28560:00

is is as a proof point to investors

## 28560:00 - 28595:00

um you know for better or worse right

## 28595:00 - 28640:00

and um and i'll give the counterpoint to

## 28640:00 - 28685:00

myself at the end of this but um but but

## 28685:00 - 28705:00

i think what investors need to be able

## 28705:00 - 28750:00

to see when they are valuing a company

## 28750:00 - 28785:00

at several hundred million in valuation

## 28785:00 - 28805:00

you know so if you look at from the

## 28805:00 - 28845:00

investor lens whatever

## 28845:00 - 28875:00

price that they come in at they

## 28875:00 - 28910:00

basically are underwriting that they

## 28910:00 - 28955:00

that easily there should be a three two

## 28955:00 - 28995:00

to three x step up and valuation in the

## 28995:00 - 29035:00

next round so if they're coming in at

## 29035:00 - 29080:00

200 or 300 million in valuation you're

## 29080:00 - 29100:00

saying that potentially they're going to

## 29100:00 - 29155:00

be a 600 to 900 million valuation

## 29155:00 - 29180:00

company in

## 29180:00 - 29210:00

you know 18 to 24 months

## 29210:00 - 29235:00

and you're kind of like well how do you

## 29235:00 - 29275:00

do that right like so typically you're

## 29275:00 - 29305:00

not going to do that purely by taking

## 29305:00 - 29335:00

your core market and just growing it a

## 29335:00 - 29350:00

bunch

## 29350:00 - 29375:00

because um one of the things that you

## 29375:00 - 29410:00

have a lot more control of is you

## 29410:00 - 29435:00

actually have a lot more control of

## 29435:00 - 29470:00

opening in more markets

## 29470:00 - 29505:00

as compared to growing an individual

## 29505:00 - 29555:00

market 3x it's usually easier just to

## 29555:00 - 29590:00

open more market markets and so as a

## 29590:00 - 29630:00

result of that

## 29630:00 - 29670:00

investors really want to see it and so

## 29670:00 - 29705:00

one of the first conversations that i

## 29705:00 - 29735:00

have with the startup as soon as we've

## 29735:00 - 29760:00

done our investment literally the first

## 29760:00 - 29785:00

board meeting is

## 29785:00 - 29825:00

asking them do you feel like you have a

## 29825:00 - 29845:00

good sense for what you need to

## 29845:00 - 29880:00

accomplish in the next 18 months to

## 29880:00 - 29905:00

raise your next round

## 29905:00 - 29945:00

and hopefully the answer is yes

## 29945:00 - 29970:00

hopefully hopefully others have been

## 29970:00 - 29995:00

having that conversation with them along

## 29995:00 - 30010:00

the way

## 30010:00 - 30040:00

um and one of the first things that

## 30040:00 - 30070:00

often ends up happening especially once

## 30070:00 - 30115:00

you are in the kind of 100 million plus

## 30115:00 - 30165:00

type valuation range is to show

## 30165:00 - 30205:00

repeatability to show that

## 30205:00 - 30250:00

um you know one flavor is is you know i

## 30250:00 - 30270:00

think lowest hanging fruit is just

## 30270:00 - 30295:00

opening more markets so that's more

## 30295:00 - 30330:00

cities more colleges more teams more et

## 30330:00 - 30345:00

cetera

## 30345:00 - 30390:00

or and then the second is once you've

## 30390:00 - 30420:00

kind of mined that

## 30420:00 - 30450:00

is are there more services that you can

## 30450:00 - 30465:00

offer

## 30465:00 - 30500:00

um and showing showing a growth path

## 30500:00 - 30515:00

there too

## 30515:00 - 30555:00

um and so so i i i think you know you

## 30555:00 - 30585:00

ultimately need to be able to show both

## 30585:00 - 30630:00

um but i think right around kind of the

## 30630:00 - 30655:00

series b

## 30655:00 - 30690:00

um kind of the end of the series a is

## 30690:00 - 30720:00

kind of when you should be thinking

## 30720:00 - 30755:00

about um adding adding a lot more

## 30755:00 - 30785:00

regions and so what that means is that's

## 30785:00 - 30820:00

typically kind of think of that as you

## 30820:00 - 30855:00

know you're kind of in the 5 to 10

## 30855:00 - 30910:00

million gmb kind of range is when you

## 30910:00 - 30940:00

should start thinking about it um you

## 30940:00 - 30970:00

should be thinking about it when um

## 30970:00 - 30990:00

[Music]

## 30990:00 - 31030:00

you are uh you've shown that you can

## 31030:00 - 31070:00

uh you know i think uh

## 31070:00 - 31110:00

almost always if you're successful in

## 31110:00 - 31145:00

one home market

## 31145:00 - 31175:00

investors will kind of view it as like

## 31175:00 - 31195:00

you kind of get that for free because

## 31195:00 - 31230:00

you understand your market so well

## 31230:00 - 31245:00

um

## 31245:00 - 31275:00

a second market is often good but you

## 31275:00 - 31300:00

often pick a second market that's also

## 31300:00 - 31330:00

easy i think three is kind of the magic

## 31330:00 - 31355:00

number where you can start to argue that

## 31355:00 - 31390:00

it's repeatable and so any three and

## 31390:00 - 31425:00

above are kind of like you know three

## 31425:00 - 31450:00

three three or three plus markets is

## 31450:00 - 31475:00

kind of when i start to think okay yeah

## 31475:00 - 31510:00

we can we can start to connect the dots

## 31510:00 - 31550:00

and underwrite this to five markets or

## 31550:00 - 31600:00

ten markets great question thank you

## 31600:00 - 31640:00

hey rich do you want to jump on

## 31640:00 - 31675:00

yeah hey andrew how you doing a former

## 31675:00 - 31705:00

marketplace founder and now a fintech

## 31705:00 - 31730:00

founder based upon my learnings on the

## 31730:00 - 31755:00

supply side

## 31755:00 - 31775:00

i'm curious to know your thoughts around

## 31775:00 - 31820:00

defensibility on marketplaces

## 31820:00 - 31845:00

you mentioned nash which is a delivery

## 31845:00 - 31895:00

api webflow no code banking as a service

## 31895:00 - 31935:00

solutions when you're kind of evaluating

## 31935:00 - 31965:00

a company to invest in how do you think

## 31965:00 - 31990:00

about defensibility using those types of

## 31990:00 - 32020:00

tools

## 32020:00 - 32065:00

yeah i think ultimately um from a

## 32065:00 - 32100:00

defensibility sample and i think you you

## 32100:00 - 32135:00

ultimately have to ask the question

## 32135:00 - 32185:00

um do you think that it's going to

## 32185:00 - 32230:00

is the market going to be a um you know

## 32230:00 - 32265:00

winner winner take most

## 32265:00 - 32295:00

um you know type of market it's it's

## 32295:00 - 32330:00

rare by the way that you have truly a

## 32330:00 - 32355:00

winner take all because even in the in

## 32355:00 - 32380:00

the cases where people talk about winner

## 32380:00 - 32415:00

take all um as i address in the book

## 32415:00 - 32455:00

oftentimes you find these niches

## 32455:00 - 32495:00

where um you know where people pop up

## 32495:00 - 32525:00

and then it's hard to stamp out these

## 32525:00 - 32550:00

niches

## 32550:00 - 32580:00

and so almost every marketplace has kind

## 32580:00 - 32610:00

of niche competitors that emerge over

## 32610:00 - 32645:00

time and so i just think about it as

## 32645:00 - 32675:00

winner take most and so i think the

## 32675:00 - 32710:00

question comes down to

## 32710:00 - 32765:00

um thinking about uh

## 32765:00 - 32800:00

the thought experiment of

## 32800:00 - 32825:00

each side of the market so typically

## 32825:00 - 32870:00

when i analyze a marketplace company for

## 32870:00 - 32895:00

investment i usually think about the

## 32895:00 - 32935:00

demand side first then the supply side i

## 32935:00 - 32975:00

think about in each case acquisition

## 32975:00 - 33020:00

versus retention and i think about

## 33020:00 - 33055:00

imagining a small version of the network

## 33055:00 - 33080:00

in a big version of the network and how

## 33080:00 - 33110:00

you might choose differently depending

## 33110:00 - 33135:00

on the thing so in the nash case part of

## 33135:00 - 33175:00

the reason why i got excited about it is

## 33175:00 - 33265:00

um if you are a um if you are a uh uh

## 33265:00 - 33330:00

you know um a company that is delivers

## 33330:00 - 33365:00

cakes you know like super fancy cakes

## 33365:00 - 33420:00

anywhere in the us and you basically

## 33420:00 - 33460:00

want to mail them to like a hub and then

## 33460:00 - 33480:00

you want you want to overnight them to a

## 33480:00 - 33520:00

hub and then you want to deliver it um

## 33520:00 - 33560:00

you know to to uh to somebody kind of

## 33560:00 - 33580:00

last mile

## 33580:00 - 33605:00

and you

## 33605:00 - 33650:00

would you rather work with a large

## 33650:00 - 33695:00

network or a small network right and i

## 33695:00 - 33715:00

think the first thing you would say is

## 33715:00 - 33745:00

like yeah you probably work with a large

## 33745:00 - 33780:00

network because if you work with a small

## 33780:00 - 33805:00

network the problem becomes there's a

## 33805:00 - 33830:00

lot of different areas that you may not

## 33830:00 - 33860:00

be able to deliver to

## 33860:00 - 33890:00

and then on the flip side

## 33890:00 - 33925:00

um if you are a courier

## 33925:00 - 33955:00

you know individual courier you might

## 33955:00 - 33985:00

think okay do i want to work with a

## 33985:00 - 34010:00

company that gives me a lot of business

## 34010:00 - 34030:00

or do you want to give me do i want to

## 34030:00 - 34050:00

work with a company that gives me a

## 34050:00 - 34075:00

little bit of business and in that case

## 34075:00 - 34100:00

you might say well maybe you should just

## 34100:00 - 34135:00

do both right and in that case you can

## 34135:00 - 34175:00

sort of dual app and do that and so that

## 34175:00 - 34210:00

might indicate that for example the

## 34210:00 - 34250:00

demand side of the of the business the

## 34250:00 - 34285:00

the companies that integrate into nash

## 34285:00 - 34330:00

are probably stickier than the than the

## 34330:00 - 34365:00

delivery side of the network and so that

## 34365:00 - 34395:00

sort of implies that okay but one of the

## 34395:00 - 34415:00

big most important things for the

## 34415:00 - 34450:00

company is probably to figure out

## 34450:00 - 34480:00

on the on the demand on the on the labor

## 34480:00 - 34510:00

side how to make that as sticky as

## 34510:00 - 34535:00

possible how do you do that maybe you

## 34535:00 - 34570:00

build tooling maybe you have loyalty

## 34570:00 - 34595:00

programs maybe you

## 34595:00 - 34655:00

um you know pre-buy a lot of the the

## 34655:00 - 34685:00

time the hours from people ahead of time

## 34685:00 - 34715:00

you sign them into exclusive contracts

## 34715:00 - 34735:00

what do you do so i think you didn't

## 34735:00 - 34760:00

answer there

## 34760:00 - 34785:00

but i think generally you know the

## 34785:00 - 34810:00

reason why network effects end up being

## 34810:00 - 34875:00

so uh powerful and defensible is that

## 34875:00 - 34920:00

building these networks ends up becoming

## 34920:00 - 34950:00

um you know from scratch like people

## 34950:00 - 34980:00

argue like well uber's network effect is

## 34980:00 - 35010:00

not that not that strong you're like

## 35010:00 - 35040:00

okay cool try to build a rideshare

## 35040:00 - 35070:00

company these days right from scratch

## 35070:00 - 35095:00

like it's not going to happen like it

## 35095:00 - 35125:00

would literally cost like you know tens

## 35125:00 - 35155:00

of billions of dollars and so i think

## 35155:00 - 35185:00

the reality is that once you get one of

## 35185:00 - 35210:00

these up and running

## 35210:00 - 35250:00

um it cuts off the number of new

## 35250:00 - 35280:00

entrants and then the only people you're

## 35280:00 - 35305:00

competing with are the people that you

## 35305:00 - 35340:00

kind of started around the same time as

## 35340:00 - 35385:00

you plus or minus kind of three years um

## 35385:00 - 35420:00

so that's that's generally how i've been

## 35420:00 - 35455:00

thinking about it thank you i feel like

## 35455:00 - 35485:00

we're uh we're getting like a master

## 35485:00 - 35535:00

class right now so i love you

## 35535:00 - 35580:00

awesome hey um uh laura did you want to

## 35580:00 - 35595:00

jump on

## 35595:00 - 35625:00

hey andrew how are you doing

## 35625:00 - 35640:00

good

## 35640:00 - 35680:00

awesome so um i'm in the space where

## 35680:00 - 35720:00

assassinated labor marketplace and my

## 35720:00 - 35750:00

question to you is

## 35750:00 - 35790:00

as we go into our next round and think

## 35790:00 - 35825:00

about our next valuation

## 35825:00 - 35870:00

how do you think about

## 35870:00 - 35910:00

i guess quantifying and qualifying an

## 35910:00 - 35940:00

engaged community that you're not

## 35940:00 - 35980:00

necessarily monetizing from so we've got

## 35980:00 - 36025:00

um like a multiple on sas and gmv but

## 36025:00 - 36060:00

any thoughts in terms of

## 36060:00 - 36090:00

the supply side of the community and how

## 36090:00 - 36110:00

you

## 36110:00 - 36145:00

kind of talk to that

## 36145:00 - 36190:00

yeah well i think the the good news is

## 36190:00 - 36250:00

that um uh there has been a

## 36250:00 - 36290:00

long history of companies

## 36290:00 - 36335:00

where um settlement so there's kind of

## 36335:00 - 36380:00

two two flavors of this right so one is

## 36380:00 - 36420:00

um where you where the settlement of the

## 36420:00 - 36460:00

actual transactions does not happen

## 36460:00 - 36500:00

inside the marketplace but you can kind

## 36500:00 - 36530:00

of like estimate it so like a good

## 36530:00 - 36555:00

example in new york

## 36555:00 - 36590:00

is a company called good dog which is

## 36590:00 - 36615:00

all about pet adoption

## 36615:00 - 36650:00

and it's basically like a lead gen

## 36650:00 - 36695:00

business ultimately um because it's a

## 36695:00 - 36730:00

multi-thousand dollar purchase and it's

## 36730:00 - 36755:00

sort of a long sales cycle and so the

## 36755:00 - 36795:00

reality is you maybe don't you know

## 36795:00 - 36830:00

settle um on there but they've they've

## 36830:00 - 36870:00

attracted a tremendous amount of

## 36870:00 - 36915:00

um of investment because one of the

## 36915:00 - 36950:00

things they can point to is they're able

## 36950:00 - 37000:00

to point to the idea that uh the leads

## 37000:00 - 37030:00

that they're sending are worth a certain

## 37030:00 - 37050:00

amount

## 37050:00 - 37100:00

um and it's sort of like one step before

## 37100:00 - 37115:00

gmb

## 37115:00 - 37150:00

um is sort of like sort of you know like

## 37150:00 - 37185:00

a like a qualified interest like dollars

## 37185:00 - 37220:00

amount i have i have a company that we

## 37220:00 - 37235:00

recently

## 37235:00 - 37280:00

invested in that's called stunx

## 37280:00 - 37305:00

that does the same thing it's basically

## 37305:00 - 37340:00

like a demo day

## 37340:00 - 37365:00

product you can basically run demo days

## 37365:00 - 37390:00

on it but you can't settle on the

## 37390:00 - 37420:00

platform right now you can't invest

## 37420:00 - 37445:00

in the company on the platform but what

## 37445:00 - 37465:00

it does is you can say well i want to

## 37465:00 - 37490:00

invest 100k

## 37490:00 - 37535:00

and then it'll connect you off platform

## 37535:00 - 37560:00

and then they can count that you know so

## 37560:00 - 37585:00

that's one flavor of kind of like off

## 37585:00 - 37615:00

platform transactions the other version

## 37615:00 - 37655:00

as well is um you know i think one one

## 37655:00 - 37690:00

of the one of the pieces of good news is

## 37690:00 - 37725:00

that when you look at a product like

## 37725:00 - 37760:00

pinterest for example um that's a

## 37760:00 - 37795:00

product that has a lot of fundamental

## 37795:00 - 37830:00

user engagement they look and feel like

## 37830:00 - 37860:00

a social network it's sort of a monthly

## 37860:00 - 37880:00

actives

## 37880:00 - 37925:00

you know kind of based uh you know uh

## 37925:00 - 37955:00

product but at the same time you know

## 37955:00 - 38005:00

that it's at least mid-funnel in the

## 38005:00 - 38055:00

purchase cycle and so you can also just

## 38055:00 - 38085:00

look at and talk about your product as

## 38085:00 - 38120:00

if it's a social network with the idea

## 38120:00 - 38150:00

that if there's some embedded amount of

## 38150:00 - 38190:00

commercial intent then the monetization

## 38190:00 - 38235:00

story ought to be easier um as as a

## 38235:00 - 38275:00

result um and so and then frankly you

## 38275:00 - 38305:00

know laura look basically the the

## 38305:00 - 38345:00

earlier the businesses the less you're

## 38345:00 - 38365:00

focused on

## 38365:00 - 38405:00

you know the the revenue piece of it and

## 38405:00 - 38430:00

so because we often see

## 38430:00 - 38460:00

you know legion numbers we often see

## 38460:00 - 38490:00

take rates that are like way out of

## 38490:00 - 38515:00

bounds of what's what it's going to end

## 38515:00 - 38550:00

up and so as an investor you kind of

## 38550:00 - 38590:00

have to close your eyes and imagine you

## 38590:00 - 38610:00

know where it's going to go over the

## 38610:00 - 38645:00

next couple years awesome thank you

## 38645:00 - 38670:00

awesome thanks we're going to try to

## 38670:00 - 38705:00

squeeze in uh two two quick questions if

## 38705:00 - 38745:00

you can uh okay cool i'll do i'll do a

## 38745:00 - 38770:00

lightning round version awesome hey uh

## 38770:00 - 38815:00

jennifer do you want to come on

## 38815:00 - 38850:00

thanks so much um thanks for this andrew

## 38850:00 - 38880:00

it's been really good

## 38880:00 - 38915:00

so since reading co-star problem i've

## 38915:00 - 38950:00

been obviously building more and

## 38950:00 - 38980:00

thinking more in terms of atomic

## 38980:00 - 39020:00

networks and the hard side and what i

## 39020:00 - 39055:00

found i have a of a mental health and

## 39055:00 - 39105:00

wellness marketplace is that the

## 39105:00 - 39145:00

creators and the providers sort of ended

## 39145:00 - 39180:00

up um buying from each other and they

## 39180:00 - 39195:00

were becoming like their own little

## 39195:00 - 39245:00

ecosystem my question is how much uh

## 39245:00 - 39280:00

would you suggest continuing to focus on

## 39280:00 - 39315:00

the creators and the providers

## 39315:00 - 39345:00

considering they are buying each other

## 39345:00 - 39380:00

services compared to

## 39380:00 - 39405:00

starting to focus on the demand side of

## 39405:00 - 39450:00

things um and you know our marketing and

## 39450:00 - 39490:00

so on right well i think what's

## 39490:00 - 39560:00

definitely um honestly easiest is if you

## 39560:00 - 39580:00

can build

## 39580:00 - 39610:00

one side of a network

## 39610:00 - 39650:00

and then it just works on its own and so

## 39650:00 - 39680:00

in paypal's case right like that was

## 39680:00 - 39705:00

always sort of the quintessential kind

## 39705:00 - 39740:00

of one-sided network is

## 39740:00 - 39765:00

um you know you just peer appear the

## 39765:00 - 39805:00

buyers were the sellers and so i think

## 39805:00 - 39855:00

it it might be very attractive to go

## 39855:00 - 39910:00

through that and um it might be very uh

## 39910:00 - 39940:00

you know it might be that that market

## 39940:00 - 39960:00

ends up being larger than you think it

## 39960:00 - 39970:00

is

## 39970:00 - 40010:00

um or it ends up at least being a really

## 40010:00 - 40055:00

good initial market so i'm not against

## 40055:00 - 40095:00

um you know exploring that more deeply

## 40095:00 - 40125:00

and seeing if you can add to the network

## 40125:00 - 40145:00

over time

## 40145:00 - 40190:00

um before you then add add the demand

## 40190:00 - 40240:00

side in into the equation so

## 40240:00 - 40275:00

um i i think it sounds intriguing and i

## 40275:00 - 40310:00

think probably one of the things that

## 40310:00 - 40355:00

you're you're questioning is just is it

## 40355:00 - 40385:00

is it too small of a market to just

## 40385:00 - 40425:00

focus on you know creators and you know

## 40425:00 - 40450:00

vendors kind of interacting with each

## 40450:00 - 40465:00

other

## 40465:00 - 40505:00

and i would say um you know if if

## 40505:00 - 40540:00

they're retaining extremely well and

## 40540:00 - 40580:00

they're selling high value services that

## 40580:00 - 40610:00

might be a great place to start and then

## 40610:00 - 40650:00

you can always um you know expand from

## 40650:00 - 40675:00

there that's one of the the beauties of

## 40675:00 - 40715:00

the marketplace model is that it lends

## 40715:00 - 40755:00

itself towards um expanding in terms of

## 40755:00 - 40790:00

services well thanks so much i'm gonna

## 40790:00 - 40820:00

come see you speak at startup grind next

## 40820:00 - 40835:00

week

## 40835:00 - 40850:00

great

## 40850:00 - 40890:00

awesome samuel jump on really quick yeah

## 40890:00 - 40935:00

yeah super short question um marketplace

## 40935:00 - 40970:00

for offline media so kind of the airbnb

## 40970:00 - 41005:00

problem we've got billboards we've got

## 41005:00 - 41035:00

mass transit you can wrap an ice cream

## 41035:00 - 41070:00

truck sponsor pizza boxes

## 41070:00 - 41125:00

um the challenge is like the perception

## 41125:00 - 41170:00

of adverse selection everybody wants to

## 41170:00 - 41200:00

be in times square

## 41200:00 - 41225:00

that's generally

## 41225:00 - 41270:00

one not where they need to be and two

## 41270:00 - 41305:00

uh that's usually sold out so there's

## 41305:00 - 41335:00

not a lot of value for them being in our

## 41335:00 - 41365:00

marketplace but if you want to reach

## 41365:00 - 41390:00

like elon musk there's a billboard we

## 41390:00 - 41415:00

know who drives past every month kind of

## 41415:00 - 41425:00

thing

## 41425:00 - 41450:00

um so

## 41450:00 - 41490:00

the solving for the perception of

## 41490:00 - 41530:00

adverse selection when the real value is

## 41530:00 - 41560:00

in the long tail again like airbnb

## 41560:00 - 41585:00

everybody has a different definition of

## 41585:00 - 41615:00

value but imagine you had to rent like

## 41615:00 - 41655:00

40 airbnbs from 20 different companies

## 41655:00 - 41675:00

um

## 41675:00 - 41720:00

that's uh yeah the would love to hear

## 41720:00 - 41740:00

your thoughts on that

## 41740:00 - 41780:00

yeah yeah i think uh i think average

## 41780:00 - 41820:00

selection is definitely one of the most

## 41820:00 - 41850:00

um you know interesting you know

## 41850:00 - 41885:00

problems that that marketplace companies

## 41885:00 - 41920:00

can potentially solve right i mean i

## 41920:00 - 41965:00

think in many ways you would say um well

## 41965:00 - 42005:00

aren't aren't airbnbs adversely selected

## 42005:00 - 42065:00

compared to hotels um you know or or or

## 42065:00 - 42095:00

and the answer is they could be

## 42095:00 - 42135:00

except that airbnb also added photos and

## 42135:00 - 42170:00

they added reviews and they added enough

## 42170:00 - 42195:00

functionality such that you would

## 42195:00 - 42210:00

actually

## 42210:00 - 42240:00

feel like you had a really really great

## 42240:00 - 42285:00

experience um you know and in a similar

## 42285:00 - 42325:00

way um i think i think uh you know one

## 42325:00 - 42350:00

of the other marketplace companies i've

## 42350:00 - 42385:00

invested in many years ago is angelus

## 42385:00 - 42415:00

and one of the issues with angellist was

## 42415:00 - 42455:00

that um it was also adversely selected

## 42455:00 - 42480:00

because many of the companies that were

## 42480:00 - 42515:00

being brought onto the platform that one

## 42515:00 - 42540:00

in funding were the ones that were

## 42540:00 - 42570:00

having trouble raising funding and as a

## 42570:00 - 42600:00

result were adversely selected compared

## 42600:00 - 42630:00

to the ones who didn't use angel so how

## 42630:00 - 42660:00

do you solve that well angel has ended

## 42660:00 - 42690:00

up solving that by using by creating

## 42690:00 - 42730:00

syndicates private syndicates by using

## 42730:00 - 42780:00

by creating you know um uh private

## 42780:00 - 42830:00

platforms for for funds to use and so as

## 42830:00 - 42875:00

a result um because of that privacy

## 42875:00 - 42910:00

element now people now companies sign up

## 42910:00 - 42960:00

for angellist um even without the intent

## 42960:00 - 42995:00

of having a public fundraising kind of

## 42995:00 - 43035:00

you know flow um which helps a lot so i

## 43035:00 - 43070:00

i think i think the question for you um

## 43070:00 - 43130:00

would be in in in doing that can you add

## 43130:00 - 43155:00

are there things that you can do to add

## 43155:00 - 43205:00

a layer of functionality or value that

## 43205:00 - 43255:00

maybe for a different buyer

## 43255:00 - 43285:00

who doesn't want to be in times square

## 43285:00 - 43310:00

right maybe they're looking for maybe

## 43310:00 - 43335:00

they're more of a performance marketer

## 43335:00 - 43360:00

maybe they're more of a

## 43360:00 - 43410:00

um you know uh somebody that is hyper

## 43410:00 - 43450:00

focused on certain regions um that

## 43450:00 - 43490:00

you're able to provide a way that you

## 43490:00 - 43525:00

can establish liquidity there i think

## 43525:00 - 43555:00

that would be one one question that i

## 43555:00 - 43580:00

would have and then and then the second

## 43580:00 - 43610:00

question i would have is obviously the

## 43610:00 - 43650:00

more that you can

## 43650:00 - 43700:00

um you know create us a a you know

## 43700:00 - 43730:00

define what performance means in a new

## 43730:00 - 43750:00

way

## 43750:00 - 43780:00

um uh and

## 43780:00 - 43805:00

and uh you know whether whether that

## 43805:00 - 43840:00

means it's a star rating system but even

## 43840:00 - 43865:00

better would be if there were a way that

## 43865:00 - 43910:00

you could add you know if you added a

## 43910:00 - 43950:00

layer to manage all the 1 800 numbers

## 43950:00 - 43980:00

that calls that were coming you know

## 43980:00 - 44010:00

from the thing and in order to track

## 44010:00 - 44040:00

that and so then you could then give

## 44040:00 - 44080:00

like an roi a better roi metric for some

## 44080:00 - 44090:00

of the

## 44090:00 - 44125:00

um you know further flung you know

## 44125:00 - 44160:00

billboards um you know maybe that

## 44160:00 - 44190:00

becomes interesting but i think you have

## 44190:00 - 44230:00

to do something to establish a different

## 44230:00 - 44275:00

set of buyers and sellers in order to

## 44275:00 - 44305:00

um build something separately otherwise

## 44305:00 - 44335:00

you're going to end up in a world where

## 44335:00 - 44365:00

it's like you're trying to sell airbnb

## 44365:00 - 44410:00

inventory to hotel shoppers

## 44410:00 - 44440:00

right and if that's not what they're

## 44440:00 - 44460:00

looking for they're not going to want

## 44460:00 - 44485:00

that you're going to want people that

## 44485:00 - 44505:00

are looking for a neighborhood

## 44505:00 - 44530:00

experience or they're looking for a more

## 44530:00 - 44570:00

homey experience for a longer stay and

## 44570:00 - 44600:00

if you can segment out that market then

## 44600:00 - 44640:00

you're you're better off and so um in in

## 44640:00 - 44660:00

the book i have a section about cherry

## 44660:00 - 44690:00

picking which is exactly about this

## 44690:00 - 44710:00

which is you need to

## 44710:00 - 44740:00

cherry pick a niche that's probably

## 44740:00 - 44765:00

already working

## 44765:00 - 44795:00

as opposed to thinking about it like

## 44795:00 - 44825:00

you're trying to just disrupt the whole

## 44825:00 - 44870:00

thing you know starting at once awesome

## 44870:00 - 44900:00

yeah thanks for taking the time to uh

## 44900:00 - 44925:00

you know to get to that last question

## 44925:00 - 44950:00

and i know we're we're actually over

## 44950:00 - 44990:00

right now so okay i appreciate it well

## 44990:00 - 45010:00

this is a really incredible chat so i

## 45010:00 - 45035:00

know we were all you know looking

## 45035:00 - 45065:00

forward to it uh here as you know

## 45065:00 - 45100:00

marketplace founders and leaders and um

## 45100:00 - 45150:00

you know huge fans of you know you and

## 45150:00 - 45190:00

the cold star problem and uh you know uh

## 45190:00 - 45220:00

last but not least so time for kind of a

## 45220:00 - 45240:00

quick plug where should we uh keep up

## 45240:00 - 45260:00

with you

## 45260:00 - 45300:00

yeah so i just uh so so the the big

## 45300:00 - 45340:00

thing that i use um for my big pieces is

## 45340:00 - 45370:00

andrewchen.com so you can sign up to the

## 45370:00 - 45395:00

newsletter there

## 45395:00 - 45425:00

um if if there are questions that i

## 45425:00 - 45455:00

didn't get to if you want to hit me on

## 45455:00 - 45525:00

on twitter um happy to uh uh i'm back to

## 45525:00 - 45555:00

back today but i i'll try and get to

## 45555:00 - 45590:00

everyone's questions if you want to um

## 45590:00 - 45620:00

just just uh you know ask me a question

## 45620:00 - 45645:00

on there i can i can type type in a

## 45645:00 - 45680:00

tweet thread so amazing amazing we

## 45680:00 - 45695:00

really appreciate it maybe i'll start

## 45695:00 - 45720:00

like a thread on there where we all just

## 45720:00 - 45755:00

share our nice questions there so nice

## 45755:00 - 45800:00

stuff all right thanks again so thanks

## 45800:00 - 45830:00

everyone for joining today yup thank you

## 45830:00+

guys see you later

