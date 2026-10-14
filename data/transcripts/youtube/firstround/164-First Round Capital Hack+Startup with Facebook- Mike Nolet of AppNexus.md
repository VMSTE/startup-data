---
source: https://www.youtube.com/watch?v=BlWCZFiQ7_U
title: "First Round Capital Hack+Startup with Facebook: Mike Nolet of AppNexus"
author: First Round Capital
date: 2012-12-05
views: 6813
description: >-
  At Hack+Startup Brooklyn Beta Edition, Mike Nolet, Co-Founder and CTO at
  AppNexus talks DevOps and how to overcome difficult processes at scale like
  deployment and infrastructure. 


  Mike Nolet is the CTO of AppNexus, an advertising technology company that
  works with some of the biggest companies in the word-- Microsoft, eBay, and
  Orange to name a few. At its core, AppNexus helps these businesses shift away
  from a traditional hand-sold advertising world where publishers have to deal
  with advertisers to one geared for the 21st century. In the process, AppNexus
  has raised over $65 million in venture capital from firms like Venrock, Khosla
  and First Round Capital (us!) and now have over 400 employees in New York
  City.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T21:02:23.322Z
---

# First Round Capital Hack+Startup with Facebook: Mike Nolet of AppNexus

## 00:00 - 215:00

[Applause]

## 215:00 - 245:00

how many people here know what app Nexus

## 245:00 - 285:00

is just out of curiosity got all right

## 285:00 - 320:00

okay fair number so just real quick I

## 320:00 - 345:00

know we're here for Tech but it's maybe

## 345:00 - 390:00

relevant to understand what we do um we

## 390:00 - 430:00

are an advertising technology company so

## 430:00 - 480:00

we license technology to big companies

## 480:00 - 525:00

uh like Microsoft like eBay um like

## 525:00 - 575:00

orange is a global Telco um and what we

## 575:00 - 615:00

do is help these companies shift from a

## 615:00 - 665:00

traditional negotiated handhold world

## 665:00 - 715:00

where um buyers and sellers of media so

## 715:00 - 735:00

Publishers websites who are trying to

## 735:00 - 760:00

make money and they're talking to

## 760:00 - 790:00

advertisers the traditional way is just

## 790:00 - 830:00

hand negotiated people do big bulk deals

## 830:00 - 855:00

by millions and millions and millions of

## 855:00 - 895:00

ads at flat rates um and doing that in

## 895:00 - 920:00

real time so basically doing it

## 920:00 - 960:00

programmatically um on page load

## 960:00 - 1005:00

actually holding an auction um having a

## 1005:00 - 1030:00

real-time bidding process where people

## 1030:00 - 1060:00

bid on those ad Impressions um and then

## 1060:00 - 1100:00

clearing that actual auction so we

## 1100:00 - 1120:00

license technology that lets people

## 1120:00 - 1160:00

operate ad exchanges trading businesses

## 1160:00 - 1195:00

trade desks um and we work with

## 1195:00 - 1220:00

companies across the entire Spectrum so

## 1220:00 - 1270:00

it's just full technology company um and

## 1270:00 - 1300:00

so what's cool is this actually should

## 1300:00 - 1340:00

be 50 not 500 milliseconds so on page

## 1340:00 - 1360:00

load we actually in 50 milliseconds will

## 1360:00 - 1405:00

do these auctions and you may not know

## 1405:00 - 1425:00

this but there's a lot of ads on the

## 1425:00 - 1460:00

internet these days um so we do this

## 1460:00 - 1500:00

about 800,000 times a second at at Peak

## 1500:00 - 1545:00

time uh so I don't think we're at Peak

## 1545:00 - 1580:00

time now we're kind of Dipping down but

## 1580:00 - 1610:00

this afternoon I could have said hey you

## 1610:00 - 1645:00

know in the last 5 Seconds we saw x

## 1645:00 - 1680:00

million users um and actually saw x

## 1680:00 - 1730:00

million ads um and we've been going

## 1730:00 - 1760:00

through this five-year kind of roller

## 1760:00 - 1810:00

coaster which has been quite a ride we

## 1810:00 - 1845:00

started we thought 10,000 ads the second

## 1845:00 - 1895:00

was a big deal um we hit 100,000 and I

## 1895:00 - 1940:00

think a year later hit 250,000 and um

## 1940:00 - 1965:00

the the Y AIS is actually a little off

## 1965:00 - 2000:00

our metric system tends to average down

## 2000:00 - 2045:00

so the actually the end Peak here is 800

## 2045:00 - 2070:00

and Facebook just got into the realtime

## 2070:00 - 2095:00

advertising launching Facebook ad

## 2095:00 - 2125:00

exchange we license technology helps

## 2125:00 - 2155:00

people buy on Facebook ad exchange it's

## 2155:00 - 2180:00

one of the things we do and you can see

## 2180:00 - 2210:00

a nice little fun Peak when they start

## 2210:00 - 2250:00

doing that um so yeah so we serve lots

## 2250:00 - 2300:00

and lots and lots of ads um and we have

## 2300:00 - 2325:00

really thousands and thousands of

## 2325:00 - 2360:00

servers to actually do this so as you

## 2360:00 - 2390:00

can imagine if you're doing 800,000

## 2390:00 - 2420:00

requests to second that you need a fair

## 2420:00 - 2440:00

amount of Hardware to do that we

## 2440:00 - 2470:00

generate 10 to 15 terabytes of data

## 2470:00 - 2510:00

every single day um so just pretty crazy

## 2510:00 - 2550:00

numbers um and today I just want to talk

## 2550:00 - 2615:00

to you about how we manage um what I

## 2615:00 - 2645:00

call devops which I I I've gotten into

## 2645:00 - 2685:00

debates is devops like religion or is it

## 2685:00 - 2730:00

you know team function um I think it's a

## 2730:00 - 2755:00

function not a religion but I think

## 2755:00 - 2790:00

there's religious aspects to us if you

## 2790:00 - 2860:00

want um and so uh talk to you about how

## 2860:00 - 2900:00

we actually manage deployments and how

## 2900:00 - 2935:00

how we manage our infrastructure now

## 2935:00 - 2960:00

some of you might say hey we don't have

## 2960:00 - 3005:00

3,000 servers so that's true but that I

## 3005:00 - 3035:00

think none of that matters the

## 3035:00 - 3070:00

principles here are what's important um

## 3070:00 - 3100:00

the investment and the reward from being

## 3100:00 - 3140:00

able to do what um I will actually show

## 3140:00 - 3185:00

you live which I think is a lot more fun

## 3185:00 - 3240:00

um so uh our devop systems uh we call

## 3240:00 - 3270:00

our main system is called

## 3270:00 - 3385:00

mro and uh Maestro is a uh it's a API

## 3385:00 - 3420:00

driven application so basically U we

## 3420:00 - 3470:00

have a central server that runs um and

## 3470:00 - 3505:00

you it's a standard restful framework

## 3505:00 - 3540:00

where you can actually post different

## 3540:00 - 3580:00

you know tasks to it um and obviously

## 3580:00 - 3605:00

one of the main tasks is to kick off

## 3605:00 - 3645:00

different run books for different jobs

## 3645:00 - 3675:00

um and I'll show the UI in a second but

## 3675:00 - 3700:00

what was cool is first we actually built

## 3700:00 - 3730:00

this UI so we took kind of standard

## 3730:00 - 3770:00

software engineering practices right um

## 3770:00 - 3795:00

most devop starts with just kind of

## 3795:00 - 3835:00

hacking things together um and then you

## 3835:00 - 3875:00

know when we built on the third version

## 3875:00 - 3900:00

of this we decided to treat it like a

## 3900:00 - 3930:00

software application that we could

## 3930:00 - 3960:00

deploy and hand to our customers that

## 3960:00 - 3990:00

was kind of the philosophy and thus we

## 3990:00 - 4010:00

went with that service oriented

## 4010:00 - 4040:00

architecture at API and what's cool is

## 4040:00 - 4065:00

our Engineers very quickly said we don't

## 4065:00 - 4090:00

like uis to do deployments and they

## 4090:00 - 4120:00

wrote their own command line deployment

## 4120:00 - 4150:00

scripts so I'm just going to do a

## 4150:00 - 4200:00

deployment of our um hbi application um

## 4200:00 - 4240:00

it's the front end and all it did was it

## 4240:00 - 4295:00

took uh tag 1.21.20 and said deploy this

## 4295:00 - 4345:00

to prod and here you can now see a

## 4345:00 - 4400:00

status of that actual upgrade um it's

## 4400:00 - 4435:00

silencing nagios because some alerts May

## 4435:00 - 4470:00

Fire when certain upgrades are happening

## 4470:00 - 4500:00

um it's running puppet we do use puppet

## 4500:00 - 4530:00

for our deployments and you can actually

## 4530:00 - 4560:00

go and see all the details of what this

## 4560:00 - 4590:00

is actually doing you can run the see

## 4590:00 - 4625:00

the commands that it's actually running

## 4625:00 - 4650:00

um you can see actually this is the API

## 4650:00 - 4680:00

call that was generated U for the

## 4680:00 - 4725:00

specific instances um and this is how

## 4725:00 - 4755:00

our Engineers do their deployments day

## 4755:00 - 4805:00

in day out um now in this case I only

## 4805:00 - 4830:00

showed you deployment on four actual

## 4830:00 - 4850:00

servers this will take about a minute so

## 4850:00 - 4885:00

we'll just let it run um but you know as

## 4885:00 - 4910:00

you can imagine we also I'm not going to

## 4910:00 - 4940:00

deploy our ad servers right now that's

## 4940:00 - 4965:00

not the ad server team would just kill

## 4965:00 - 5020:00

me some of you may want me to do it but

## 5020:00 - 5055:00

I'll show you some other stuff but uh

## 5055:00 - 5080:00

our you can also we've integrated all of

## 5080:00 - 5105:00

this into our metric so inside of our

## 5105:00 - 5135:00

moner this is an answer released that

## 5135:00 - 5165:00

happened earlier today um it was

## 5165:00 - 5200:00

completed on 91 servers uh for some

## 5200:00 - 5230:00

reason it was aborted so something went

## 5230:00 - 5280:00

wrong with the the release um you can

## 5280:00 - 5315:00

see that the ader team has metrics that

## 5315:00 - 5350:00

they're watching as the release is going

## 5350:00 - 5380:00

and then you can actually see across all

## 5380:00 - 5410:00

of those different servers see what's

## 5410:00 - 5445:00

actually happening follow the releases

## 5445:00 - 5475:00

look at standard out this instance was

## 5475:00 - 5500:00

upgraded successfully

## 5500:00 - 5520:00

um pretty much everything you need to

## 5520:00 - 5590:00

manage servers in bulk um but it's also

## 5590:00 - 5620:00

not just releases that we do on here uh

## 5620:00 - 5680:00

we also have um for example uh our SATs

## 5680:00 - 5740:00

dashboard so for uh doing managing kind

## 5740:00 - 5760:00

of our production infrastructure we

## 5760:00 - 5810:00

obviously we're a 247 business 365 um

## 5810:00 - 5850:00

this is a real-time snapshot of um

## 5850:00 - 5890:00

basically our four core real-time

## 5890:00 - 5915:00

applications so this is the apps that

## 5915:00 - 5955:00

have to deal with this 800,000 QPS and

## 5955:00 - 5995:00

this is pulled it's a 10-second delay um

## 5995:00 - 6025:00

it's a back end that sits and runs and

## 6025:00 - 6050:00

actually does Real Time updates so when

## 6050:00 - 6070:00

we're firefighting you can actually go

## 6070:00 - 6110:00

see what's going on in nym1 there's a

## 6110:00 - 6145:00

couple boxes down I don't know why

## 6145:00 - 6185:00

there's no necessar for us a couple

## 6185:00 - 6215:00

boxes down isn't a big deal but then of

## 6215:00 - 6235:00

course what's really cool is that you

## 6235:00 - 6260:00

can then actually go do things with

## 6260:00 - 6295:00

these servers so I can go filter and

## 6295:00 - 6325:00

take all my nym boxes and then apply a

## 6325:00 - 6360:00

runbook to them which can be restart the

## 6360:00 - 6395:00

servers it can be upgrade it can be run

## 6395:00 - 6420:00

a TCB dump it can be any of these kind

## 6420:00 - 6460:00

of things um and all of this is a

## 6460:00 - 6495:00

completely scriptable framework so

## 6495:00 - 6525:00

what's cool is that all of our Engineers

## 6525:00 - 6545:00

start and actually write their own

## 6545:00 - 6600:00

scripts do things um and I'll show you

## 6600:00 - 6630:00

real quick how that actually works so

## 6630:00 - 6655:00

all of these scripts are are scripts

## 6655:00 - 6685:00

that are actual individual engineering

## 6685:00 - 6725:00

teams can deploy the production so

## 6725:00 - 6775:00

basically uh our devops or our Ops team

## 6775:00 - 6805:00

is being removed from critical path for

## 6805:00 - 6830:00

being able to manage production and the

## 6830:00 - 6865:00

way we treat it all of our Engineers own

## 6865:00 - 6890:00

their own code in production that's our

## 6890:00 - 6920:00

kind of Golden Rule and the reason why

## 6920:00 - 6955:00

is you know when Ops person gets paid

## 6955:00 - 6980:00

for someone else's shitty code the

## 6980:00 - 7015:00

shitty code doesn't get fixed when the

## 7015:00 - 7040:00

engineer gets paid for his own shitty

## 7040:00 - 7075:00

code it turns out he fixes his shitty

## 7075:00 - 7120:00

code um which is why we actually do this

## 7120:00 - 7150:00

um but what's cool is you know these

## 7150:00 - 7175:00

These are scripts you can actually go

## 7175:00 - 7205:00

and look at the source here's a sample

## 7205:00 - 7245:00

script that we're not going to run

## 7245:00 - 7270:00

through all of this but you can just go

## 7270:00 - 7300:00

and edit these scripts and build scripts

## 7300:00 - 7325:00

to basically manage production which you

## 7325:00 - 7360:00

can then of course share with others and

## 7360:00 - 7385:00

they can take Dynamic input and we can

## 7385:00 - 7430:00

do all sorts of fun stuff and then I'll

## 7430:00 - 7450:00

show you one more thing before we talk

## 7450:00 - 7485:00

about how we got here which is you know

## 7485:00 - 7535:00

the team team also went off and said um

## 7535:00 - 7570:00

hey let's actually go build some command

## 7570:00 - 7590:00

line tools that help us manage

## 7590:00 - 7630:00

production so someone wrote a tool God

## 7630:00 - 7665:00

called M find and he said hey I want a

## 7665:00 - 7700:00

tool to find production impression bus

## 7700:00 - 7730:00

boxes so this is an API called to

## 7730:00 - 7755:00

Maestro and says hey give me all boxes

## 7755:00 - 7780:00

that are impression buses it's our front

## 7780:00 - 7825:00

end application um and then he said well

## 7825:00 - 7855:00

hey you know um let me add some more

## 7855:00 - 7890:00

filters to this so I want to be able to

## 7890:00 - 7910:00

pull things that are only serving ads

## 7910:00 - 7945:00

for a Google ad exchange we split out

## 7945:00 - 7980:00

these boxes for some technical reasons

## 7980:00 - 8020:00

in terms of how they manage DNS details

## 8020:00 - 8040:00

don't really matter and then someone's

## 8040:00 - 8065:00

like well hey what if we actually let

## 8065:00 - 8100:00

you actually do commands on those boxes

## 8100:00 - 8130:00

so I can actually go and do an mxc which

## 8130:00 - 8165:00

means I'm going to you know take these

## 8165:00 - 8200:00

uh boxes serving adct traffic and I can

## 8200:00 - 8250:00

go call them and see how they're doing

## 8250:00 - 8325:00

uh I think I need a-s here um and this

## 8325:00 - 8365:00

will actually go off and calls Maestro

## 8365:00 - 8400:00

does a job and says oh here's the status

## 8400:00 - 8425:00

from these boxes and then another

## 8425:00 - 8455:00

engineer got bored and said well that's

## 8455:00 - 8480:00

not very pretty so let's add a pretty

## 8480:00 - 8520:00

call to our command line and now you can

## 8520:00 - 8560:00

get the status of all these boxes pretty

## 8560:00 - 8600:00

five um so it's really fun what

## 8600:00 - 8630:00

Engineers start doing once you give them

## 8630:00 - 8670:00

these apis right so taking that API

## 8670:00 - 8695:00

driven approach that you might take to

## 8695:00 - 8720:00

your standard web application taking

## 8720:00 - 8755:00

them to your production systems suddenly

## 8755:00 - 8780:00

opens up actually a whole world of

## 8780:00 - 8805:00

innovation and what's awesome is our

## 8805:00 - 8850:00

devops guys can actually really focus on

## 8850:00 - 8905:00

writing better um devop systems not on

## 8905:00 - 8930:00

just writing yet another script or yet

## 8930:00 - 8965:00

another tool to actually do this let's

## 8965:00 - 9000:00

go back to a little bit of slideware um

## 9000:00 - 9045:00

so how did we actually get here right so

## 9045:00 - 9085:00

um I looked up on Wikipedia before this

## 9085:00 - 9125:00

um and this is what Wikipedia defines as

## 9125:00 - 9165:00

devops it's software engineering mixed

## 9165:00 - 9200:00

with quality assurance and Technical

## 9200:00 - 9245:00

operations um I didn't think this was a

## 9245:00 - 9270:00

very good definition so I went on Google

## 9270:00 - 9310:00

and devops Borat is actually much better

## 9310:00 - 9345:00

at defining devops which is that to make

## 9345:00 - 9375:00

error is human to propagate error to all

## 9375:00 - 9440:00

servers in automatic way is devops um

## 9440:00 - 9460:00

and anyone who's managed production

## 9460:00 - 9500:00

application knows that it's true um and

## 9500:00 - 9540:00

so one really important thing for me is

## 9540:00 - 9595:00

that devops is not just a new name for

## 9595:00 - 9635:00

your CIS admin team um there are

## 9635:00 - 9660:00

certainly companies out here that have

## 9660:00 - 9700:00

just renamed CIS admins to devops um if

## 9700:00 - 9730:00

you would like to sex up your CIS admin

## 9730:00 - 9765:00

team you can call them site reliability

## 9765:00 - 9800:00

Engineers um that's a nice sexy name I

## 9800:00 - 9825:00

think Google uses that for their sis

## 9825:00 - 9880:00

admin team um but no devops really is in

## 9880:00 - 9905:00

my mind a function right there is

## 9905:00 - 9925:00

certainly a certain religion we'll talk

## 9925:00 - 9950:00

about that in a little bit but you

## 9950:00 - 9995:00

really if you want internal tools that

## 9995:00 - 10020:00

really help you manage production you

## 10020:00 - 10075:00

need to staff people against that right

## 10075:00 - 10120:00

so the hardest part we found towards

## 10120:00 - 10145:00

this is actually finding the right

## 10145:00 - 10195:00

people um so when we first started uh we

## 10195:00 - 10230:00

had our CIS admin team um and we told

## 10230:00 - 10260:00

our CIS admin team hey build tools to

## 10260:00 - 10295:00

automate your job right um and they went

## 10295:00 - 10315:00

out and they used kind of a couple

## 10315:00 - 10345:00

offthe shelf tools like puppet and

## 10345:00 - 10370:00

things like that and then they wrote

## 10370:00 - 10415:00

some code now the only problem is that

## 10415:00 - 10455:00

and are there s admins in the

## 10455:00 - 10510:00

room one one I'm sorry for what I'm

## 10510:00 - 10565:00

about to say um so the problem with CIS

## 10565:00 - 10610:00

admins is they're really good at you

## 10610:00 - 10640:00

know getting something from State a to

## 10640:00 - 10695:00

State B you know once right fantastic

## 10695:00 - 10730:00

you need that done and you know often

## 10730:00 - 10760:00

they can write a script to do that and

## 10760:00 - 10785:00

and they can do that and that script

## 10785:00 - 10830:00

will work 90% of the time right because

## 10830:00 - 10860:00

generally that script's written off and

## 10860:00 - 10895:00

hair on fire and it's busy and oh my God

## 10895:00 - 10915:00

we need that release tomorrow no one

## 10915:00 - 10950:00

thought about looping in the Ops guy and

## 10950:00 - 10975:00

so what your Ops team is generally good

## 10975:00 - 11015:00

at is getting stuff done very quickly

## 11015:00 - 11050:00

right but the accuracy of what they do

## 11050:00 - 11080:00

tends to be a little bit lower it's not

## 11080:00 - 11105:00

that they're not good Engineers it's

## 11105:00 - 11130:00

just their skill set is optimized

## 11130:00 - 11180:00

towards now fast ASAP please and what

## 11180:00 - 11205:00

that means is that most code you're

## 11205:00 - 11235:00

going to get out of your Ops Team Works

## 11235:00 - 11285:00

90% of the time and you've all seen this

## 11285:00 - 11305:00

right you want to do a release you tell

## 11305:00 - 11325:00

your Ops guy you're trying to do a

## 11325:00 - 11350:00

release maybe you have a script to do it

## 11350:00 - 11385:00

and well one out of 10 times it fails

## 11385:00 - 11415:00

and you you you kind of ping him on IM

## 11415:00 - 11445:00

or you text him and he's like oh gold on

## 11445:00 - 11475:00

give me a minute and I got we type some

## 11475:00 - 11500:00

magic commands and then suddenly the

## 11500:00 - 11520:00

release goes through he's like ah I

## 11520:00 - 11555:00

fixed it and it's good you know and and

## 11555:00 - 11610:00

well anyone have that experience here no

## 11610:00 - 11630:00

you didn't you didn't have it all right

## 11630:00 - 11670:00

good you're good to but but seriously

## 11670:00 - 11705:00

this happens all the time and the

## 11705:00 - 11730:00

problem is when you start dealing with

## 11730:00 - 11760:00

lots and lots of applications or lots

## 11760:00 - 11790:00

and lots of deployments right so

## 11790:00 - 11830:00

deploying small changes frequently is

## 11830:00 - 11860:00

much better than bundling them all

## 11860:00 - 11880:00

together you want to release as little

## 11880:00 - 11920:00

as possible as often as possible because

## 11920:00 - 11950:00

you'll break as little as possible when

## 11950:00 - 11980:00

you if when inevitably you push that bad

## 11980:00 - 12010:00

code and you'll know immediately what

## 12010:00 - 12035:00

the bad code was if you've got 100

## 12035:00 - 12060:00

features you push them together you'll

## 12060:00 - 12100:00

never know kind of what broke what right

## 12100:00 - 12125:00

but to do that you need to release all

## 12125:00 - 12150:00

the time and if it's only going to work

## 12150:00 - 12190:00

90% of the time well you're in trouble

## 12190:00 - 12205:00

because you're going to be constantly

## 12205:00 - 12265:00

pinging your Ops guy um and so Ops guy

## 12265:00 - 12295:00

not the right guy to write your devop

## 12295:00 - 12330:00

system because he doesn't have quite the

## 12330:00 - 12390:00

experience um so on the flip side when

## 12390:00 - 12420:00

we asked Engineers to do it Engineers

## 12420:00 - 12450:00

had no clue how to manage production

## 12450:00 - 12475:00

right Engineers kind of live in these

## 12475:00 - 12510:00

lofty dreams we all do this I'm like

## 12510:00 - 12540:00

half Ops half engineer I'm bad engineer

## 12540:00 - 12570:00

and bad Ops and somehow in the middle it

## 12570:00 - 12610:00

works a little bit um but the the

## 12610:00 - 12635:00

engineers tend to kind of want to write

## 12635:00 - 12665:00

perfect systems and and they don't think

## 12665:00 - 12690:00

about kind of all the things that the

## 12690:00 - 12725:00

offs people think about about the the OS

## 12725:00 - 12750:00

and the hardware and the network and the

## 12750:00 - 12775:00

switches and kind of all the things you

## 12775:00 - 12810:00

need to be able to be a good caman so

## 12810:00 - 12860:00

finding that right uh devops guy I think

## 12860:00 - 12890:00

he looks like this and I think that's a

## 12890:00 - 12925:00

bazooka I'm not sure this is the

## 12925:00 - 12950:00

automator from the Mac I don't if you

## 12950:00 - 12980:00

guys know but um so finding it is

## 12980:00 - 13025:00

actually really hard um and so what we

## 13025:00 - 13075:00

found is that what we had to do is

## 13075:00 - 13100:00

actually do rotational programs so we

## 13100:00 - 13140:00

took Engineers we had them do some Ops

## 13140:00 - 13175:00

all right and we took some Ops people

## 13175:00 - 13200:00

and they did a few rotations in

## 13200:00 - 13230:00

engineering and once you start have done

## 13230:00 - 13265:00

both jobs you end up in a situation

## 13265:00 - 13305:00

where you can actually write good

## 13305:00 - 13340:00

repeatable code that has you know unit

## 13340:00 - 13370:00

test it's crazy idea you know tested

## 13370:00 - 13430:00

code documented um in SVN crazy idea

## 13430:00 - 13460:00

also a good idea um and then on the

## 13460:00 - 13485:00

other side you can also have people have

## 13485:00 - 13515:00

that that firefighting experience so

## 13515:00 - 13545:00

having people do kind of ride alongs

## 13545:00 - 13565:00

we'll have Engineers do ride alongs with

## 13565:00 - 13600:00

the Ops Team and take pages and see how

## 13600:00 - 13630:00

people do that firefighting basically

## 13630:00 - 13650:00

turning the engineer almost into a

## 13650:00 - 13685:00

product manager right for what the Ops

## 13685:00 - 13735:00

guy is doing helped get that knowledge

## 13735:00 - 13785:00

but just getting the right people uh was

## 13785:00 - 13840:00

actually not enough um we had to do two

## 13840:00 - 13870:00

other things uh which were actually

## 13870:00 - 13920:00

really critical the first was you cannot

## 13920:00 - 13980:00

have your devops guys sit on pager right

## 13980:00 - 14005:00

they cannot be in line of fire they

## 14005:00 - 14030:00

cannot take Ops tickets because the

## 14030:00 - 14055:00

problem was their mandate was to build

## 14055:00 - 14100:00

the best internal tools possible but

## 14100:00 - 14125:00

hold on oh crap we all know the rule of

## 14125:00 - 14145:00

Ops right there's always a queue and

## 14145:00 - 14165:00

always has more tickets than you want in

## 14165:00 - 14190:00

it so there's always work you're not

## 14190:00 - 14225:00

doing and that guilt factor and then

## 14225:00 - 14250:00

there's the people pinging you on IM and

## 14250:00 - 14270:00

there there's a person whose release

## 14270:00 - 14305:00

broke you end up never finding those

## 14305:00 - 14335:00

unentered blocks of time that you need

## 14335:00 - 14375:00

to write great code um so actually

## 14375:00 - 14410:00

splitting off a couple people and having

## 14410:00 - 14435:00

them be dedicated to this having them be

## 14435:00 - 14470:00

out of line of fire was critical we did

## 14470:00 - 14500:00

not start making serious progress until

## 14500:00 - 14550:00

we did that um and the second part goes

## 14550:00 - 14585:00

back to the kind of devops as a religion

## 14585:00 - 14630:00

the getting the now we're you know we're

## 14630:00 - 14660:00

right now a 350 person company Tech team

## 14660:00 - 14710:00

is about 150 something um so we might

## 14710:00 - 14730:00

have different problems than you know

## 14730:00 - 14765:00

four guys in a room but for us and we

## 14765:00 - 14790:00

started doing this when we were probably

## 14790:00 - 14830:00

a 60 person Tech Team and even at that

## 14830:00 - 14865:00

size it was hard to get people to

## 14865:00 - 14900:00

collaborate because you know everyone's

## 14900:00 - 14920:00

got their own hat on everyone's got

## 14920:00 - 14945:00

their problems everyone's got kind of

## 14945:00 - 14985:00

what they're focused on but getting um

## 14985:00 - 15015:00

we assumed that if we built it then

## 15015:00 - 15040:00

people would use it we built this

## 15040:00 - 15065:00

fantastic API driven framework and had

## 15065:00 - 15095:00

scripting languages and all of this and

## 15095:00 - 15120:00

no engineering team was using it they

## 15120:00 - 15155:00

wrote their own scripts um and so

## 15155:00 - 15195:00

actually the internal advocacy and then

## 15195:00 - 15235:00

having our devops guys do right alongs

## 15235:00 - 15255:00

with individual engineering teams and

## 15255:00 - 15280:00

showing them how the tools would help

## 15280:00 - 15310:00

them turn out to be actually really

## 15310:00 - 15350:00

critical as well um so don't

## 15350:00 - 15380:00

underestimate I mean number one thing I

## 15380:00 - 15415:00

can say just from CTO to you is like if

## 15415:00 - 15440:00

you want to accomplish this people is

## 15440:00 - 15460:00

the first thing that matters and getting

## 15460:00 - 15490:00

the right people getting them aligned

## 15490:00 - 15525:00

properly right and then having them

## 15525:00 - 15545:00

communicate and Advocate what they're

## 15545:00 - 15585:00

doing um that's you know at a very high

## 15585:00 - 15610:00

level critical to actually getting this

## 15610:00 - 15660:00

to be successful so let's dive in kind

## 15660:00 - 15700:00

of a little bit more technically perhaps

## 15700:00 - 15725:00

so we got the people in the right room

## 15725:00 - 15745:00

we got them focused on the right problem

## 15745:00 - 15770:00

we got them talking to the right people

## 15770:00 - 15795:00

um and it was critical to treat this

## 15795:00 - 15820:00

like engineering I talked a little bit

## 15820:00 - 15860:00

about 10% failure rates we had to treat

## 15860:00 - 15900:00

this like an engineering team

## 15900:00 - 15925:00

technically for cultural and

## 15925:00 - 15950:00

collaboration reasons they actually live

## 15950:00 - 15975:00

inside of our kind of infrastructure

## 15975:00 - 16010:00

oper ations organization but they're

## 16010:00 - 16035:00

treated to engineering they have a DOT

## 16035:00 - 16070:00

Aline into engineering they're expected

## 16070:00 - 16095:00

to have the same level of quality the

## 16095:00 - 16130:00

same level of bug control uh that our

## 16130:00 - 16165:00

engineering teams do um so that we have

## 16165:00 - 16185:00

a system that can actually work across

## 16185:00 - 16225:00

3,000 servers because imagine even if I

## 16225:00 - 16265:00

get my accuracy from 90% to

## 16265:00 - 16300:00

99.9% if I'm deploying on a thousand

## 16300:00 - 16325:00

servers means every deploy something

## 16325:00 - 16360:00

goes wrong right we really need real

## 16360:00 - 16405:00

Testo code that actually works um or as

## 16405:00 - 16450:00

devops Borat would tell us bad code is

## 16450:00 - 16475:00

liability and six points and good code

## 16475:00 - 16525:00

is only a liability after 36 months um

## 16525:00 - 16550:00

and I by the way does anyone agree with

## 16550:00 - 16600:00

this yeah nobody really you think your

## 16600:00 - 16630:00

code is good for for more than 36 months

## 16630:00 - 16660:00

I totally

## 16660:00 - 16705:00

disagree we find like weird stuff like

## 16705:00 - 16765:00

oh I coded that three years ago um so

## 16765:00 - 16815:00

testable rep repeatable code um uh same

## 16815:00 - 16840:00

riger of engineering tools we talked

## 16840:00 - 16885:00

about this um and you know the goal of

## 16885:00 - 16940:00

the assis admin is really to replace uh

## 16940:00 - 16965:00

itself with a small shell script right

## 16965:00 - 17005:00

that script that works % of the time and

## 17005:00 - 17040:00

devops is that restful API and that's

## 17040:00 - 17065:00

kind of a lot of what we did in uh on

## 17065:00 - 17140:00

our side here um so one thing that's the

## 17140:00 - 17165:00

last thing I think that was critical to

## 17165:00 - 17195:00

us being successful was actually using

## 17195:00 - 17230:00

open source effectively um if you want

## 17230:00 - 17265:00

to build everything from scratch uh

## 17265:00 - 17295:00

you're there's just too much right you

## 17295:00 - 17320:00

need monitoring you need metrics you

## 17320:00 - 17345:00

need production management the reason we

## 17345:00 - 17370:00

built Maestro was because we found that

## 17370:00 - 17390:00

in terms of production management

## 17390:00 - 17420:00

actually kind of pushing and all of

## 17420:00 - 17450:00

these that's where there was not much we

## 17450:00 - 17485:00

started this before Chef even existed Ed

## 17485:00 - 17515:00

so there's better tools out there that

## 17515:00 - 17540:00

you could use that might be good enough

## 17540:00 - 17585:00

in terms of Chef and knife um but so

## 17585:00 - 17635:00

definitely use open source tools um you

## 17635:00 - 17670:00

know naos I hate it to death it's one of

## 17670:00 - 17705:00

the worst monitoring Tools in existence

## 17705:00 - 17740:00

but it's the only one and you know it

## 17740:00 - 17770:00

seems to be better in building your own

## 17770:00 - 17815:00

so use it right um gangula is pretty

## 17815:00 - 17850:00

good for metrics uh we love graphite but

## 17850:00 - 17870:00

they have no logo so it's kind of hard

## 17870:00 - 17920:00

to throw them up here uh they really go

## 17920:00 - 17950:00

to graphite website there's actually

## 17950:00 - 17990:00

just kind of plain text but fantastic

## 17990:00 - 18035:00

tool um and then we also have puppet is

## 18035:00 - 18070:00

a really really great tool especially

## 18070:00 - 18100:00

for managing configurations and

## 18100:00 - 18150:00

operating system level stuff um and so

## 18150:00 - 18175:00

using these tools definitely definitely

## 18175:00 - 18205:00

use them don't reinvent every single

## 18205:00 - 18255:00

wheel but if you do use them don't just

## 18255:00 - 18285:00

treat it as software you know don't

## 18285:00 - 18325:00

treat it like the opsy might by default

## 18325:00 - 18360:00

which is install the software type up

## 18360:00 - 18405:00

your puppet config kind of and and go

## 18405:00 - 18430:00

right um and I don't know how many

## 18430:00 - 18455:00

people here use puppet how how many

## 18455:00 - 18470:00

people here use puppet let just do a

## 18470:00 - 18490:00

quick Sur

## 18490:00 - 18515:00

actually Fair how many people have you

## 18515:00 - 18550:00

versioned your puppet

## 18550:00 - 18595:00

configurations about half right this is

## 18595:00 - 18635:00

critical you have to treat puppet like

## 18635:00 - 18665:00

you would a software release you're

## 18665:00 - 18690:00

deploying a script that's going to

## 18690:00 - 18705:00

change your entire production

## 18705:00 - 18730:00

environment it's funny when we first

## 18730:00 - 18760:00

started using puppet and I don't I still

## 18760:00 - 18795:00

think they haven't quite uh uh fixed

## 18795:00 - 18830:00

this just yet we actually have different

## 18830:00 - 18865:00

puppet interations and different puppet

## 18865:00 - 18905:00

code sources inside of our Maestro tool

## 18905:00 - 18930:00

so that you can actually upgrade from

## 18930:00 - 18965:00

one puppet recipe to the next so you

## 18965:00 - 19000:00

have to treat puppet like an automated

## 19000:00 - 19035:00

piece of tool where you tag release and

## 19035:00 - 19075:00

you deploy it right um and you can

## 19075:00 - 19105:00

actually use automation to do that right

## 19105:00 - 19145:00

you can't has can't be a manual SCP a

## 19145:00 - 19180:00

new file over here right so use these

## 19180:00 - 19210:00

tools this way as well your monitoring

## 19210:00 - 19240:00

system it should be automatic if you sp

## 19240:00 - 19275:00

up a new server this shouldn't be hey I

## 19275:00 - 19305:00

have to configure a monitoring to work

## 19305:00 - 19325:00

because if you do it if you require

## 19325:00 - 19360:00

people to do things they will fail

## 19360:00 - 19395:00

naturally maybe 10% of the time during

## 19395:00 - 19435:00

the day and 30% of the time at night

## 19435:00 - 19460:00

right so if there's that pager at night

## 19460:00 - 19485:00

you know they will make mistakes so

## 19485:00 - 19505:00

automate the monitoring automate the

## 19505:00 - 19545:00

metrics and on our side any server we

## 19545:00 - 19580:00

spool up it's a pointed click to to

## 19580:00 - 19605:00

spool up a server I highly recommend you

## 19605:00 - 19625:00

build that especially if you're going to

## 19625:00 - 19655:00

have any kind of scale and then when

## 19655:00 - 19670:00

that server is pulled up it

## 19670:00 - 19705:00

automatically has the application it's

## 19705:00 - 19750:00

monitored and we got metrics um really

## 19750:00 - 19800:00

really critical so and we even have

## 19800:00 - 19825:00

staging we have a staging environment

## 19825:00 - 19850:00

for our puppet we have a total Dev

## 19850:00 - 19875:00

environment for our puppet where op team

## 19875:00 - 19905:00

can go play with new tools and new

## 19905:00 - 19950:00

recipes uh we roll those releases uh

## 19950:00 - 19995:00

very very helpful so last thing and

## 19995:00 - 20015:00

let's see if the internet works actually

## 20015:00 - 20030:00

do this so I can show you guys the

## 20030:00 - 20100:00

little live demo um uh one thing I find

## 20100:00 - 20140:00

consistently that almost every company

## 20140:00 - 20200:00

underinvested is metrics um so we use

## 20200:00 - 20230:00

graphite for all of our metrics it's a

## 20230:00 - 20255:00

fantastic tool we sponsored a lot of

## 20255:00 - 20280:00

development under if use the

## 20280:00 - 20310:00

dashboarding UI that came from the fact

## 20310:00 - 20325:00

that we had so many metrics that

## 20325:00 - 20360:00

graphite wasn't working for us um so we

## 20360:00 - 20390:00

worked closely with Chris to get them to

## 20390:00 - 20420:00

build this um we had actually built our

## 20420:00 - 20450:00

own kind of shitty PHP version didn't

## 20450:00 - 20480:00

quite work we wanted to get integrated

## 20480:00 - 20505:00

all the aggregations and cluster stuff

## 20505:00 - 20545:00

we also work closely with chrisson um

## 20545:00 - 20580:00

and you know our team this is we still

## 20580:00 - 20615:00

need to improve this but we now have you

## 20615:00 - 20650:00

know dashboards that show real

## 20650:00 - 20680:00

production status for pretty much

## 20680:00 - 20720:00

anything we have in production um at any

## 20720:00 - 20765:00

point in time um and everyone in the

## 20765:00 - 20795:00

company is religious about this from our

## 20795:00 - 20845:00

CEO down to every single engineer every

## 20845:00 - 20865:00

engineering team has a dashboard

## 20865:00 - 20900:00

application our services teams now have

## 20900:00 - 20930:00

applic have dashboards for their

## 20930:00 - 20960:00

individual clients so we're a B2B

## 20960:00 - 20995:00

company so since we our clients's name

## 20995:00 - 21020:00

in the hundreds we actually track in

## 21020:00 - 21045:00

real time how many Impressions our

## 21045:00 - 21075:00

clients are sending us how much money

## 21075:00 - 21110:00

they're spending and our actual Services

## 21110:00 - 21145:00

people because we've automated pagers

## 21145:00 - 21175:00

integrated to with metrics we didn't

## 21175:00 - 21205:00

intend this to happen but they then

## 21205:00 - 21240:00

started putting themselves on pager for

## 21240:00 - 21275:00

their own accounts so now our monitoring

## 21275:00 - 21310:00

system sends pages to our services

## 21310:00 - 21350:00

engineers and and our implementation

## 21350:00 - 21375:00

Consultants when their accounts do

## 21375:00 - 21410:00

unexpected behavior when volume drops

## 21410:00 - 21440:00

things like that which lets our services

## 21440:00 - 21470:00

team now deliver a fantastic service

## 21470:00 - 21480:00

that

## 21480:00 - 21510:00

they call our clients and sometimes they

## 21510:00 - 21545:00

tell them their site sites are down

## 21545:00 - 21590:00

right before our clients sometimes know

## 21590:00 - 21625:00

um which is pretty crazy right so you

## 21625:00 - 21645:00

imagine you call you're like hey you

## 21645:00 - 21670:00

know we stopped seeing traffic from your

## 21670:00 - 21695:00

account like what's going on it's like

## 21695:00 - 21745:00

really oh our sight's down um it's

## 21745:00 - 21770:00

kind of feels good to be able to do that

## 21770:00 - 21795:00

those kind of phone calls so I really

## 21795:00 - 21825:00

really highly recommend um getting a

## 21825:00 - 21865:00

really solid metric system and

## 21865:00 - 21890:00

integrating that closely with your

## 21890:00 - 21925:00

monitoring so that you can just have all

## 21925:00 - 21945:00

of this be seamless so you have

## 21945:00 - 21980:00

visibility to what happens which matters

## 21980:00 - 22015:00

more and more especially as you get big

## 22015:00 - 22035:00

you know when you have five servers you

## 22035:00 - 22055:00

can log into five servers see what's

## 22055:00 - 22085:00

going on when you have three and a half

## 22085:00 - 22110:00

thousand servers there's no way and when

## 22110:00 - 22130:00

you're Facebook and you have I don't

## 22130:00 - 22160:00

know how many um 100 thousand servers

## 22160:00 - 22195:00

I'm sure you know you have to have some

## 22195:00 - 22225:00

kind of way to look at these metrics uh

## 22225:00+

programmatically

