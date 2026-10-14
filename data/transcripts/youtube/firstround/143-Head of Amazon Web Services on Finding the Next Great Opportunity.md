---
source: https://www.youtube.com/watch?v=6zqyOoIYso4
title: Head of Amazon Web Services on Finding the Next Great Opportunity
author: First Round Capital
date: 2013-04-15
views: 3180
description: ""
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:57:07.724Z
---

# Head of Amazon Web Services on Finding the Next Great Opportunity

## 00:00 - 125:00

I get to talk to you a little bit about

## 125:00 - 160:00

today about well I thought of a few

## 160:00 - 190:00

things it's a relatively short talk and

## 190:00 - 220:00

so what I thought I would do is I'd

## 220:00 - 250:00

start off by talking a little bit about

## 250:00 - 280:00

how I work because not everyone's going

## 280:00 - 315:00

to be INF interested in infrastructure

## 315:00 - 330:00

although I'm going to try to make it

## 330:00 - 350:00

interesting so I'm going to talk a

## 350:00 - 375:00

little bit about first about here's how

## 375:00 - 405:00

I figure out what I'm going to work on

## 405:00 - 430:00

because I think some of these some of

## 430:00 - 460:00

these techniques are good techniques to

## 460:00 - 490:00

to figure out what to work on and and

## 490:00 - 520:00

how to be working on things that are

## 520:00 - 550:00

that are relevant then I want to talk

## 550:00 - 585:00

about three things that happen to be hot

## 585:00 - 625:00

in my world right now that I think are

## 625:00 - 645:00

big changes and whenever you see big

## 645:00 - 670:00

changes what that means is Big

## 670:00 - 715:00

opportunity so I'm going to talk quickly

## 715:00 - 760:00

about networking storage and overall

## 760:00 - 800:00

cloud computing some of why cloud

## 800:00 - 830:00

computing is not just a fat it's

## 830:00 - 850:00

actually something pretty relevant

## 850:00 - 890:00

pretty big it's going to stay big and

## 890:00 - 915:00

what that might mean for you so that's

## 915:00 - 950:00

the game plan um we'll hopefully have a

## 950:00 - 970:00

little bit of time for questions at the

## 970:00 - 1025:00

end see how things go

## 1025:00 - 1035:00

all

## 1035:00 - 1075:00

right how we think about problems or at

## 1075:00 - 1115:00

least how I think about problems I love

## 1115:00 - 1155:00

cost models it's kind of weird that it's

## 1155:00 - 1195:00

supposedly a technical guy would love

## 1195:00 - 1230:00

basically spreadsheet models driving my

## 1230:00 - 1275:00

work and it's I would never started that

## 1275:00 - 1310:00

way what's happened over the years is

## 1310:00 - 1380:00

I've learned it's super easy to do great

## 1380:00 - 1425:00

work on a problem that's just not that

## 1425:00 - 1460:00

relevant you got to work on the problems

## 1460:00 - 1505:00

that are the most important and that's

## 1505:00 - 1535:00

one thing the second thing that models

## 1535:00 - 1565:00

teach us is and I'll show I'll give you

## 1565:00 - 1585:00

examples with this one because it's kind

## 1585:00 - 1630:00

of fun um models teach us that people

## 1630:00 - 1670:00

don't look hard enough at things what

## 1670:00 - 1710:00

happens is people start to say something

## 1710:00 - 1735:00

and then you say something and then

## 1735:00 - 1760:00

three of us say something and after a

## 1760:00 - 1825:00

while it becomes true it's not true it's

## 1825:00 - 1875:00

phenomenal how many things I've managed

## 1875:00 - 1930:00

to supposedly innovate by just not

## 1930:00 - 1965:00

believing things just simply not

## 1965:00 - 1990:00

believing things checking to see if it

## 1990:00 - 2035:00

really is true and it's not it's really

## 2035:00 - 2075:00

it's it's it's kind of it's almost

## 2075:00 - 2110:00

criminal so listen this is about Big

## 2110:00 - 2160:00

Data Centers so think think order 50,000

## 2160:00 - 2200:00

servers in a single building this is the

## 2200:00 - 2245:00

cost model for building everything from

## 2245:00 - 2285:00

the operating system on

## 2285:00 - 2320:00

down you can make a lot of mistakes

## 2320:00 - 2350:00

building these models the first one you

## 2350:00 - 2395:00

can make is power you buy every month it

## 2395:00 - 2435:00

doesn't have any lasting value data

## 2435:00 - 2470:00

centers last for 10 plus years

## 2470:00 - 2500:00

networking gear usually goes four to

## 2500:00 - 2545:00

five servers go three you need some way

## 2545:00 - 2575:00

to get that data together if you do not

## 2575:00 - 2615:00

normalize you'll get confused and think

## 2615:00 - 2650:00

the data center is by far the most

## 2650:00 - 2680:00

expensive component in the whole system

## 2680:00 - 2730:00

and it's not and so you got to normalize

## 2730:00 - 2785:00

the way I normalize boring um take the

## 2785:00 - 2825:00

amortization period of the equipment

## 2825:00 - 2860:00

assume a zero residual value which is

## 2860:00 - 2885:00

pretty close to the fact in our world

## 2885:00 - 2940:00

today and 5% cost of money and what do I

## 2940:00 - 2970:00

pay every month once I know what I pay

## 2970:00 - 3000:00

every month I can compare it to power

## 3000:00 - 3020:00

and I can compare it to everything else

## 3020:00 - 3060:00

I'm paying every month so you're done at

## 3060:00 - 3090:00

that point a whole bunch of things

## 3090:00 - 3120:00

interesting pop from this but let's

## 3120:00 - 3160:00

start with let's start with how come

## 3160:00 - 3200:00

people costs aren't there all the

## 3200:00 - 3240:00

Enterprise customers I talk to say the

## 3240:00 - 3285:00

people costs dominate their business

## 3285:00 - 3320:00

that's the most expensive cost they have

## 3320:00 - 3345:00

Administration is the most expensive

## 3345:00 - 3375:00

cost they've got it's not even here and

## 3375:00 - 3410:00

the reason it's not even here is because

## 3410:00 - 3460:00

it's not even here it's not relevant in

## 3460:00 - 3485:00

the cloud and the reason it's not

## 3485:00 - 3520:00

relevant the cloud is if you're managing

## 3520:00 - 3565:00

133 SharePoint three exchange servers

## 3565:00 - 3605:00

two Oracle servers and a SQL Server you

## 3605:00 - 3640:00

do it all by by hand you have no choice

## 3640:00 - 3680:00

you can't you can't hire six people and

## 3680:00 - 3700:00

and automate each one of those

## 3700:00 - 3720:00

operations it's not going to happen it's

## 3720:00 - 3740:00

just not going to

## 3740:00 - 3810:00

happen if you're managing 10,000 MySQL

## 3810:00 - 3870:00

servers or considerably more hundreds of

## 3870:00 - 3910:00

thousands of ec2 servers well first of

## 3910:00 - 3945:00

all if you were to try to do it using

## 3945:00 - 3985:00

standard Administration ratios first of

## 3985:00 - 4010:00

all

## 4010:00 - 4030:00

you would never be able to hire that

## 4030:00 - 4060:00

many people it's just you can't do it

## 4060:00 - 4105:00

and second of all people make mistakes

## 4105:00 - 4145:00

and in very large numbers rough numbers

## 4145:00 - 4185:00

I use is people make mistakes about 20%

## 4185:00 - 4240:00

of the time it's not quite true it's

## 4240:00 - 4285:00

about one chance in five one opportunity

## 4285:00 - 4325:00

in five an unintended consequence

## 4325:00 - 4360:00

happens sometimes it's a

## 4360:00 - 4400:00

nit sometimes the entire data center

## 4400:00 - 4440:00

gets disconnected it's bigger than a n

## 4440:00 - 4475:00

people make mistakes just a fact and the

## 4475:00 - 4505:00

more boring the work the the more the

## 4505:00 - 4530:00

mistakes that they make and so

## 4530:00 - 4560:00

automation is a real helpful thing

## 4560:00 - 4595:00

because it it improves the overall

## 4595:00 - 4630:00

reliability and the second thing is it

## 4630:00 - 4680:00

drives down the cost because of that at

## 4680:00 - 4720:00

a very highs scale service 3%

## 4720:00 - 4755:00

Administration is is a pretty typical

## 4755:00 - 4795:00

number i' you it's it's easy to hit that

## 4795:00 - 4835:00

one and what that means

## 4835:00 - 4890:00

is it's just not that important so the

## 4890:00 - 4915:00

first interesting thing that pops from

## 4915:00 - 4955:00

this is I'm not even bothering to keep

## 4955:00 - 4985:00

track of something that the Enterprise

## 4985:00 - 5015:00

says is is the most important thing and

## 5015:00 - 5050:00

that's one way that cloud computing is

## 5050:00 - 5075:00

wildly different from Enterprise

## 5075:00 - 5115:00

Computing second one the industry says

## 5115:00 - 5155:00

listen the the biggest non-p people cost

## 5155:00 - 5190:00

today everyone's talking about power

## 5190:00 - 5230:00

power is the hot issue New York Times

## 5230:00 - 5280:00

just did a couple day a couple um Daye

## 5280:00 - 5335:00

coverage on on Power number one cost on

## 5335:00 - 5365:00

the data center everyone's talking about

## 5365:00 - 5395:00

how they can optimize power we look at

## 5395:00 - 5425:00

the spreadsheet and says well it's not

## 5425:00 - 5450:00

number one that's a disappointment

## 5450:00 - 5475:00

everyone everyone said it's number one

## 5475:00 - 5500:00

not one not one

## 5500:00 - 5535:00

not two it's not even two that's totally

## 5535:00 - 5565:00

disappointing it's number three and it's

## 5565:00 - 5595:00

not even a big three so the first thing

## 5595:00 - 5630:00

you get out of this is there's a case

## 5630:00 - 5665:00

where it's not quite true and say well

## 5665:00 - 5690:00

maybe it doesn't matter is it worth

## 5690:00 - 5725:00

optimizing for power it totally is and

## 5725:00 - 5745:00

so maybe it doesn't matter that you're

## 5745:00 - 5765:00

getting it wrong and you think it's the

## 5765:00 - 5790:00

most important second actually the

## 5790:00 - 5840:00

second most important well here's an

## 5840:00 - 5875:00

example why it's not okay it's another I

## 5875:00 - 5895:00

think this is a cool thing so it's worth

## 5895:00 - 5915:00

sharing with

## 5915:00 - 5955:00

you the industry today thinks the way

## 5955:00 - 5980:00

you deal with that because power is

## 5980:00 - 6000:00

number one cost

## 6000:00 - 6045:00

and workloads you buy enough hardware

## 6045:00 - 6095:00

for the peak but often times there's

## 6095:00 - 6135:00

troughs and so you buy for Peak you

## 6135:00 - 6180:00

monetize it at wherever the workload is

## 6180:00 - 6220:00

right now and one way to figure out the

## 6220:00 - 6260:00

expense of of supporting a workload is

## 6260:00 - 6305:00

the ratio between Peak and and and

## 6305:00 - 6335:00

average actually tells you how efficient

## 6335:00 - 6365:00

that workload is is to

## 6365:00 - 6425:00

host so we'll come back to that one so

## 6425:00 - 6470:00

if you're looking if you're looking at

## 6470:00 - 6510:00

at that particular you know that's a

## 6510:00 - 6545:00

fact then the way you handle the troughs

## 6545:00 - 6585:00

is you virtualize the servers pack them

## 6585:00 - 6625:00

on the small workloads pack them on the

## 6625:00 - 6650:00

smallest number of servers you can and

## 6650:00 - 6680:00

shut off all the remaining servers you

## 6680:00 - 6705:00

save all the power that's the number one

## 6705:00 - 6735:00

cost it's a big win well what you get

## 6735:00 - 6780:00

from this is it's a 133% win now you

## 6780:00 - 6805:00

know I've been knowing to do crazy

## 6805:00 - 6840:00

things for 133% so it's not

## 6840:00 - 6880:00

disappointing but it's only

## 6880:00 - 6940:00

133% another way to look at it though

## 6940:00 - 6965:00

way a way that's productive here to look

## 6965:00 - 7020:00

at it is you're wasting 87% because you

## 7020:00 - 7040:00

still bought the server you still bought

## 7040:00 - 7060:00

the network you still bought the power

## 7060:00 - 7090:00

distribution gear you didn't use it you

## 7090:00 - 7115:00

still bought the mechanical gear but

## 7115:00 - 7145:00

you're not using it and you still bought

## 7145:00 - 7185:00

the shell that it all exists in and so

## 7185:00 - 7215:00

what this tells you is wait a sec wait a

## 7215:00 - 7250:00

sec this is interesting if I could run a

## 7250:00 - 7290:00

workload any workload that was worth

## 7290:00 - 7345:00

more than the than the marginal cost of

## 7345:00 - 7390:00

power it would be a win I said I

## 7390:00 - 7410:00

shouldn't be shutting these servers off

## 7410:00 - 7440:00

I should be turning them all on if any

## 7440:00 - 7470:00

workload in your company is worth more

## 7470:00 - 7510:00

than than 13% can't turn it on that's

## 7510:00 - 7540:00

super interesting hard to do though say

## 7540:00 - 7570:00

you're in tax preparation software you

## 7570:00 - 7615:00

got a really busy time of year and then

## 7615:00 - 7640:00

the rest of the years this not so busy

## 7640:00 - 7680:00

not much you can do about that but in

## 7680:00 - 7710:00

the cloud environment we're bringing

## 7710:00 - 7740:00

together a large number of

## 7740:00 - 7785:00

non-correlated workloads two things

## 7785:00 - 7815:00

happen that are cool the first thing

## 7815:00 - 7855:00

that happens is a whole bunch of

## 7855:00 - 7890:00

sinusoidal waves brought together

## 7890:00 - 7930:00

flatten out the aggregate wave is just

## 7930:00 - 7965:00

flatter it averages and so the first

## 7965:00 - 8000:00

thing is the cost of supporting the

## 8000:00 - 8030:00

aggregate workload remember we talked

## 8030:00 - 8065:00

Peak average the cost of supporting the

## 8065:00 - 8105:00

efficiency of the aggregate workload is

## 8105:00 - 8140:00

wildly better than any individual

## 8140:00 - 8175:00

workload super cool that means that as a

## 8175:00 - 8220:00

cloud provider I win before I even start

## 8220:00 - 8270:00

thinking it's already way better and

## 8270:00 - 8300:00

when you're talking when you're talking

## 8300:00 - 8335:00

utilization it's the biggest win there

## 8335:00 - 8365:00

is because that's everything's being

## 8365:00 - 8420:00

saved if you know if if if if a a

## 8420:00 - 8445:00

standard Enterprise customer could

## 8445:00 - 8490:00

easily be in 10 to 20% utilization which

## 8490:00 - 8555:00

is to say everything's wasted 80 or 90%

## 8555:00 - 8595:00

of the time if you can bring that number

## 8595:00 - 8625:00

up it's it's no higher lever there is

## 8625:00 - 8660:00

it's the most powerful lever there is

## 8660:00 - 8690:00

and so without even thinking we've

## 8690:00 - 8715:00

already got a more efficient aggregate

## 8715:00 - 8745:00

workload the second thing and this is

## 8745:00 - 8770:00

the thing the fun thing that I wanted to

## 8770:00 - 8805:00

tell you about is what do you do with

## 8805:00 - 8850:00

the trough that's remaining the little

## 8850:00 - 8875:00

the distance between the trough and Peak

## 8875:00 - 8900:00

you're still some work there's still

## 8900:00 - 8935:00

some capability to run workload there

## 8935:00 - 8975:00

what do you do with that well you make a

## 8975:00 - 9025:00

market you steal idea from every other

## 9025:00 - 9060:00

very any every other business that runs

## 9060:00 - 9110:00

very expensive assets you you you you

## 9110:00 - 9140:00

create a spot market and say what would

## 9140:00 - 9190:00

you pay me today to run workload for

## 9190:00 - 9240:00

this hour that's not very busy and it's

## 9240:00 - 9265:00

it's a super it's a one of these

## 9265:00 - 9310:00

wonderful win-win-win things it's

## 9310:00 - 9340:00

customers say well I I'll only pay you

## 9340:00 - 9380:00

half of what you normally charge me and

## 9380:00 - 9425:00

here's a cool thing customer is paying

## 9425:00 - 9455:00

less than the cost of of what they're

## 9455:00 - 9500:00

running it's less than cost and so

## 9500:00 - 9530:00

wonderful Big Win huge win for a

## 9530:00 - 9570:00

customer they're happier and heck whenn

## 9570:00 - 9610:00

for us it's way more than the marginal

## 9610:00 - 9650:00

cost of power it's actually a win for us

## 9650:00 - 9680:00

so we're winning and the second and the

## 9680:00 - 9725:00

final thing is all of the assets that

## 9725:00 - 9755:00

are in play best thing you can do for

## 9755:00 - 9800:00

the environment is is is utilize all the

## 9800:00 - 9830:00

Assets in play and there's not just not

## 9830:00 - 9855:00

using them is the worst thing you can do

## 9855:00 - 9890:00

so that's the second thing that that

## 9890:00 - 9940:00

that that kind of pops out from this

## 9940:00 - 9965:00

couple more observations just from the

## 9965:00 - 10010:00

model just just to kind of show you that

## 10010:00 - 10035:00

the model is relevant and and it's a

## 10035:00 - 10085:00

it's a cool way to go after things IBM

## 10085:00 - 10125:00

and HP love to sell blade servers

## 10125:00 - 10160:00

they're a little bit more expensive but

## 10160:00 - 10180:00

you make it up in total cost of

## 10180:00 - 10220:00

ownership you say okay cool that's great

## 10220:00 - 10265:00

what so we turn blades we turn servers

## 10265:00 - 10305:00

over 90° apparently that gets better

## 10305:00 - 10340:00

right up front then you pack them in

## 10340:00 - 10380:00

really tight so it costs a little bit

## 10380:00 - 10430:00

more to cool them because it's a 25 Kow

## 10430:00 - 10455:00

rack so you're paying a little bit more

## 10455:00 - 10485:00

to cool them you're paying a little bit

## 10485:00 - 10515:00

more to buy them but you're going to

## 10515:00 - 10540:00

make it up over time you say well let's

## 10540:00 - 10570:00

just check the math I'm going to pay

## 10570:00 - 10585:00

more on

## 10585:00 - 10625:00

57% and I'm going to send a spend a

## 10625:00 - 10665:00

little bit more on the 18% and I'm going

## 10665:00 - 10695:00

to save on the 4% because I'm going to

## 10695:00 - 10715:00

use less four

## 10715:00 - 10765:00

space uh-uh not going to happen and

## 10765:00 - 10790:00

that's why of the big players like

## 10790:00 - 10835:00

Google Microsoft Amazon you see Zero

## 10835:00 - 10870:00

blade servers sold but the industry

## 10870:00 - 10905:00

doesn't know that because for for what

## 10905:00 - 10930:00

because they just don't carefully

## 10930:00 - 10960:00

inventory the cost and so they're buying

## 10960:00 - 11015:00

them so last one last one I wanted to

## 11015:00 - 11070:00

pop from this one is I love looking at

## 11070:00 - 11100:00

Trends anytime you're working any

## 11100:00 - 11130:00

anything you're working on when you see

## 11130:00 - 11165:00

two things that relate to each other and

## 11165:00 - 11205:00

they're moving apart or two things that

## 11205:00 - 11230:00

relate to each other and they're moving

## 11230:00 - 11265:00

together jump on it it's an opportunity

## 11265:00 - 11295:00

it's cool opportunity here's one that's

## 11295:00 - 11325:00

moving apart that's a problem if you

## 11325:00 - 11385:00

look at the aggregate it workload it it

## 11385:00 - 11425:00

cost all the servers storage and

## 11425:00 - 11455:00

networking the percentage that's

## 11455:00 - 11510:00

networking is going up over time so that

## 11510:00 - 11535:00

says networking is a huge problem is

## 11535:00 - 11555:00

something's broken there and so you have

## 11555:00 - 11590:00

to dig deeper there and so let's start

## 11590:00 - 11610:00

with digging deeper in there that was an

## 11610:00 - 11640:00

example so let's let's let's dig deeper

## 11640:00 - 11660:00

in

## 11660:00 - 11695:00

networking in the networking world I'm

## 11695:00 - 11725:00

comparing the ecosystem because I'm

## 11725:00 - 11760:00

claiming the ecosystem is broken and and

## 11760:00 - 11785:00

we'll talk about how it's being fixed

## 11785:00 - 11810:00

right now the ecosystem in the

## 11810:00 - 11875:00

networking world is 1985 IBM these are

## 11875:00 - 11910:00

Mainframe systems it's exactly the same

## 11910:00 - 11960:00

you can compare them exactly um layer by

## 11960:00 - 12000:00

layer the the core of networking

## 12000:00 - 12025:00

equipment the CPU is called an

## 12025:00 - 12055:00

application specific integrated circuits

## 12055:00 - 12110:00

in Asic the Asic is produced by a single

## 12110:00 - 12150:00

vendor the bent metal this the the

## 12150:00 - 12180:00

rudder itself is produced by a single

## 12180:00 - 12225:00

vendor same one that the Asic the

## 12225:00 - 12260:00

protocol stack that runs on top of it

## 12260:00 - 12290:00

same vendor it's all vertically

## 12290:00 - 12330:00

integrated just like an IBM Mainframe

## 12330:00 - 12355:00

and what we need to have happen is what

## 12355:00 - 12385:00

happened in the server world is when we

## 12385:00 - 12420:00

had competition at the CPU level and you

## 12420:00 - 12450:00

can we don't have enough but there's a

## 12450:00 - 12475:00

little bit of competition at the CPU

## 12475:00 - 12515:00

level that's a good thing and when

## 12515:00 - 12545:00

you've got competition at the bent metal

## 12545:00 - 12575:00

level at the server level and you can

## 12575:00 - 12610:00

buy for a given CPU you can buy it from

## 12610:00 - 12660:00

HP from IBM from Dell dot dot dot dot

## 12660:00 - 12690:00

dot that's a good thing and when there's

## 12690:00 - 12730:00

operating system choice you can run BSD

## 12730:00 - 12750:00

you can run a Millions different

## 12750:00 - 12780:00

versions of Linux you can run Windows

## 12780:00 - 12800:00

that's a good thing and we know what

## 12800:00 - 12860:00

happened to the server World cost

## 12860:00 - 12920:00

plunged the rate of innovation

## 12920:00 - 12955:00

skyrocketed it's a good thing same thing

## 12955:00 - 12980:00

needs to happen in the in the network

## 12980:00 - 13005:00

World well the the right equipment is

## 13005:00 - 13030:00

there to actually make it happen today

## 13030:00 - 13050:00

and there's a ton of startup

## 13050:00 - 13080:00

opportunities that are circling around

## 13080:00 - 13105:00

networking right now because these

## 13105:00 - 13140:00

opportunities are there but the big

## 13140:00 - 13170:00

players like Cisco and Juniper it's hard

## 13170:00 - 13210:00

to for them to fundamentally change the

## 13210:00 - 13240:00

way they do the way they conduct their

## 13240:00 - 13290:00

business and 80% margins are hard to do

## 13290:00 - 13335:00

in a commodity world and so it may not

## 13335:00 - 13365:00

be attractive for them to go after this

## 13365:00 - 13400:00

and so what happens is now you can buy

## 13400:00 - 13455:00

as6 from a wide variety of competitors

## 13455:00 - 13500:00

fulcom Broad

## 13500:00 - 13555:00

uh marll several others you can buy take

## 13555:00 - 13585:00

broadcom as an example you can buy a

## 13585:00 - 13655:00

broadcom reference platform router from

## 13655:00 - 13740:00

Quant celestica Dell NEC dni and a whole

## 13740:00 - 13765:00

bunch of others that I won't be thinking

## 13765:00 - 13795:00

about right now lots and lots and lots

## 13795:00 - 13840:00

of competition use there's open source

## 13840:00 - 13890:00

routing Stacks like quag and there's

## 13890:00 - 13920:00

four fee routing Stacks available from

## 13920:00 - 13960:00

many players available as well and so

## 13960:00 - 13985:00

the right equipment is there to

## 13985:00 - 14030:00

fundamentally change the world and

## 14030:00 - 14070:00

there's a need to change it I told you

## 14070:00 - 14100:00

one need the costs are going up over

## 14100:00 - 14130:00

time so it's a problem anytime you see

## 14130:00 - 14165:00

someone with with Mammoth margins that

## 14165:00 - 14215:00

says something needs to change um second

## 14215:00 - 14270:00

thing is because networking gear is so

## 14270:00 - 14305:00

expensive we do another one of those

## 14305:00 - 14350:00

dumb things we turn to our model we know

## 14350:00 - 14385:00

from the model that networking although

## 14385:00 - 14450:00

Believe It or Not 128 Port 128 Port

## 14450:00 - 14510:00

router at 60% % Mark uh 60% markdown

## 14510:00 - 14535:00

because we're big customers so they give

## 14535:00 - 14635:00

us a great deal 60% markdown it's still

## 14635:00 - 14680:00

$350,000 for 128

## 14680:00 - 14725:00

ports that's a big number and by the way

## 14725:00 - 14780:00

for power it takes 20 kilowatt to give

## 14780:00 - 14835:00

you a data point a kilowatt a kilowatt

## 14835:00 - 14880:00

um is if you look at it a rack of of

## 14880:00 - 14915:00

servers rough numbers about 10 kilowatts

## 14915:00 - 14965:00

and so 20 kilowatts is a lot for 128

## 14965:00 - 14995:00

ports

## 14995:00 - 15050:00

okay so big opportunity going on in

## 15050:00 - 15105:00

networking right now um many layers of

## 15105:00 - 15155:00

it one many drivers of it I talked about

## 15155:00 - 15195:00

one was cost the second driver of it is

## 15195:00 - 15230:00

the one that I I just about got to but

## 15230:00 - 15285:00

but failed is um people make a mistakes

## 15285:00 - 15315:00

the networking cost from the previous Mo

## 15315:00 - 15350:00

from the previous model was about 8% of

## 15350:00 - 15380:00

the overall cost in the whole in the

## 15380:00 - 15400:00

whole system but the equipment is

## 15400:00 - 15425:00

ridiculously expensive I told you it was

## 15425:00 - 15465:00

$300,000 piece of equipment so because

## 15465:00 - 15495:00

it's so expensive you want to get really

## 15495:00 - 15530:00

good value from it so you over subscribe

## 15530:00 - 15550:00

it and you do everything you can to

## 15550:00 - 15580:00

optimize it but it's crazy because it

## 15580:00 - 15630:00

turns out the servers are 55% and if you

## 15630:00 - 15670:00

lower your your server utilization by

## 15670:00 - 15700:00

under supplying the network you're

## 15700:00 - 15735:00

making a terrible mistake and so as much

## 15735:00 - 15765:00

as I hate paying $350,000 per piece of

## 15765:00 - 15800:00

networking gear you almost have to if

## 15800:00 - 15825:00

you're smart because you really got to

## 15825:00 - 15845:00

get everything you can for the most

## 15845:00 - 15890:00

expensive asset there now it turns out

## 15890:00 - 15925:00

you can do both um the world's changing

## 15925:00 - 15965:00

in network so you can afford a lot more

## 15965:00 - 15985:00

networking gear which is what we're

## 15985:00 - 16030:00

doing and the world's changing in

## 16030:00 - 16070:00

networking and so you can use commodity

## 16070:00 - 16100:00

components now and have competition in

## 16100:00 - 16135:00

the hey healthy ecosystem so that's

## 16135:00 - 16170:00

actually going on another thing

## 16170:00 - 16190:00

happening in the networking world the

## 16190:00 - 16235:00

software defined networking um I

## 16235:00 - 16260:00

discover discovered software defined

## 16260:00 - 16295:00

networking kind of by by backing into it

## 16295:00 - 16325:00

it's an idea originally from Nick McKuen

## 16325:00 - 16360:00

from Stanford University I sort of

## 16360:00 - 16385:00

backed into it and I was working on a

## 16385:00 - 16430:00

networking project with with um with

## 16430:00 - 16475:00

Albert Greenberg and we were looking at

## 16475:00 - 16515:00

at the rate of the rate of change inside

## 16515:00 - 16560:00

a 50,000 server Data Center and I'm I've

## 16560:00 - 16590:00

got a database background and the rate

## 16590:00 - 16635:00

of change is ridiculously slow like

## 16635:00 - 16650:00

instead of having this really

## 16650:00 - 16690:00

complicated distributed system where

## 16690:00 - 16720:00

every router is negotiating with every

## 16720:00 - 16755:00

other router trying to form their

## 16755:00 - 16780:00

Collective opinion of what the

## 16780:00 - 16820:00

connectivity graph is you can just

## 16820:00 - 16850:00

control it centrally a single Central

## 16850:00 - 16875:00

database can do everything if the

## 16875:00 - 16920:00

transaction ratees ridiculously low now

## 16920:00 - 16940:00

it's not reliable enough to have a

## 16940:00 - 16965:00

single database so you have multiple of

## 16965:00 - 17010:00

them but it's not a hard problem and the

## 17010:00 - 17060:00

cool thing is you can do great work with

## 17060:00 - 17110:00

very fast recovery time um guaranteed

## 17110:00 - 17145:00

quality of service segregating out

## 17145:00 - 17190:00

different workloads sorting sorting

## 17190:00 - 17235:00

workloads so that low priority um

## 17235:00 - 17260:00

updates that need to flow through the

## 17260:00 - 17300:00

network anytime in the next hour don't

## 17300:00 - 17320:00

get in the way of high priority

## 17320:00 - 17350:00

workloads you can do lots to drive

## 17350:00 - 17375:00

utilization up and do a better job of

## 17375:00 - 17410:00

network of network optimization if you

## 17410:00 - 17450:00

essentially control so software defined

## 17450:00 - 17475:00

networking really is a simple thing is

## 17475:00 - 17505:00

central control of all the routing

## 17505:00 - 17535:00

decisions is another thing that is

## 17535:00 - 17570:00

becoming possible now another big

## 17570:00 - 17600:00

startup opportunity there's a whole

## 17600:00 - 17625:00

bunch of companies that are working in

## 17625:00 - 17660:00

this space right now uh Nera recently

## 17660:00 - 17695:00

had a very large exit that that was for

## 17695:00 - 17720:00

relatively no one but there's a bunch

## 17720:00 - 17740:00

working

## 17740:00 - 17790:00

there okay here's another one let's jump

## 17790:00 - 17850:00

to storage quickly on the storage side

## 17850:00 - 17895:00

um we've been with disc for a long long

## 17895:00 - 17945:00

time I love to normalize data so you can

## 17945:00 - 17975:00

compare two different so you can can

## 17975:00 - 18010:00

compare unlike things you saw that in my

## 18010:00 - 18055:00

original model on this one normally when

## 18055:00 - 18090:00

you look at discs a commodity disc does

## 18090:00 - 18150:00

around 80 to 100 iOS per second and it

## 18150:00 - 18205:00

does order order 100 megabytes per

## 18205:00 - 18245:00

second and so they're not a comparable

## 18245:00 - 18285:00

numbers so you really can't you know you

## 18285:00 - 18310:00

can't really figure out which is which

## 18310:00 - 18335:00

the cool thing is what I've done is i'

## 18335:00 - 18375:00

to show what's going on I've normalized

## 18375:00 - 18440:00

iOS per second to um using 8K iOS I've

## 18440:00 - 18470:00

normalized them to megabytes per second

## 18470:00 - 18495:00

so they're both in megabytes per second

## 18495:00 - 18525:00

and what it really what this drives home

## 18525:00 - 18570:00

is you'll see the rate that sequential

## 18570:00 - 18610:00

IO is improving on this and then you see

## 18610:00 - 18645:00

the rate that that random iio is

## 18645:00 - 18675:00

improving on this and the answer is it's

## 18675:00 - 18725:00

not it's just flat not so huge problem

## 18725:00 - 18765:00

we know what going on um here's a way to

## 18765:00 - 18825:00

drive that problem home um what this is

## 18825:00 - 18850:00

this kind of an interesting observation

## 18850:00 - 18905:00

if you look at a at a four at a 4 tbyte

## 18905:00 - 18935:00

disc which is this year is going to be

## 18935:00 - 18970:00

this that will be The Sweet Spot a four

## 18970:00 - 19020:00

terab disc if you sequentially read read

## 19020:00 - 19065:00

it it will take 11 hours that's a

## 19065:00 - 19115:00

phenomenally long time it's it's the

## 19115:00 - 19150:00

closest thing there there is to tape and

## 19150:00 - 19185:00

it's kind of funny because Jim Gray said

## 19185:00 - 19240:00

in in 2006 disc is tape it's true it

## 19240:00 - 19270:00

takes 11 hours to read every piece of

## 19270:00 - 19320:00

every bite once the wild thing is if you

## 19320:00 - 19370:00

randomly read it it takes 41 days you

## 19370:00 - 19405:00

better have more than a month just to

## 19405:00 - 19455:00

read everything a single time so clearly

## 19455:00 - 19490:00

it's not going to work um so first

## 19490:00 - 19550:00

observation is dis is still big it's

## 19550:00 - 19580:00

going to be tape it is where we'll back

## 19580:00 - 19615:00

up to we'll archive to it's a huge

## 19615:00 - 19655:00

important business but we will do zero

## 19655:00 - 19690:00

random ios's to it because it makes no

## 19690:00 - 19740:00

sense it's just not the future so first

## 19740:00 - 19800:00

one is disc becomes tape second one

## 19800:00 - 19870:00

is Flash becomes dis semiconductor

## 19870:00 - 19910:00

storage is a capable of of very large

## 19910:00 - 19950:00

numbers of iOS the problem is it's order

## 19950:00 - 19985:00

four to six

## 19985:00 - 20020:00

more expensive than than disc at a

## 20020:00 - 20060:00

capacity basis but it's much cheaper for

## 20060:00 - 20095:00

iops so if you have an iops bound

## 20095:00 - 20135:00

workload which from the previous chart

## 20135:00 - 20160:00

you know almost any random workload is

## 20160:00 - 20195:00

going to be iops found everything's on

## 20195:00 - 20225:00

flash 100% everything everything

## 20225:00 - 20275:00

everything everything is on flash and if

## 20275:00 - 20320:00

you play some cool tricks you might be

## 20320:00 - 20370:00

able to get more workloads on flash than

## 20370:00 - 20395:00

would happen just naturally without

## 20395:00 - 20435:00

change and that's by observing flash has

## 20435:00 - 20490:00

almost has a huge number of iOS it has a

## 20490:00 - 20525:00

number of iOS per gig that's that is so

## 20525:00 - 20565:00

high that few workloads actually need

## 20565:00 - 20610:00

them so if you can play games to trade

## 20610:00 - 20670:00

off iOS to in other words trade some iOS

## 20670:00 - 20710:00

to gain capacity and D duplication is

## 20710:00 - 20755:00

one way of trading iOS to get capacity

## 20755:00 - 20800:00

another one is compression and and

## 20800:00 - 20835:00

running a log structured Block store

## 20835:00 - 20875:00

another one is sparse provisioning if

## 20875:00 - 20905:00

you play some of those tricks you can

## 20905:00 - 20945:00

get it you can get the the the

## 20945:00 - 20990:00

semiconductor storage approaching that

## 20990:00 - 21020:00

of the cost of disc and every time you

## 21020:00 - 21060:00

get it closer more workload goes that

## 21060:00 - 21095:00

way and so this is another one where I

## 21095:00 - 21120:00

think there there are a bunch of

## 21120:00 - 21145:00

startups that that have been wildly

## 21145:00 - 21165:00

successful and there's going to be a

## 21165:00 - 21215:00

bunch more um places where the where the

## 21215:00 - 21250:00

biggest opportunities are right now are

## 21250:00 - 21300:00

finding ways to get the cost per per

## 21300:00 - 21350:00

gigabyte down is is is one way the

## 21350:00 - 21395:00

second way is the reliability of flash

## 21395:00 - 21435:00

is plunging quickly as we drive the cost

## 21435:00 - 21470:00

out the number of iOS that they can

## 21470:00 - 21510:00

sustain before wearing out is going down

## 21510:00 - 21550:00

rapidly and the error rate is going down

## 21550:00 - 21580:00

rapidly and that's a great thing because

## 21580:00 - 21620:00

it's amable to software it's it's you

## 21620:00 - 21650:00

know we can we can do things in software

## 21650:00 - 21685:00

to hide all of those flaws and if

## 21685:00 - 21725:00

there's a hard problem and there's some

## 21725:00 - 21805:00

payback then it's worth it's worth

## 21805:00 - 21845:00

solving client storage everyone knows

## 21845:00 - 21885:00

this is migrating 100% to semiconductor

## 21885:00 - 21910:00

storage as well even though a lot of the

## 21910:00 - 21950:00

workload is not random it's all going

## 21950:00 - 21985:00

semiconductor because there a all the

## 21985:00 - 22015:00

advantages I've written here of on

## 22015:00 - 22050:00

running in semiconductor however every

## 22050:00 - 22090:00

client device is connected to the cloud

## 22090:00 - 22135:00

and every client device is only a cash

## 22135:00 - 22175:00

for for for for the for everything that

## 22175:00 - 22205:00

they're storing which will be in the

## 22205:00 - 22260:00

cloud because of that it it says a huge

## 22260:00 - 22285:00

amount of the of the client device

## 22285:00 - 22320:00

storage probably still will be dis it'll

## 22320:00 - 22370:00

just be dis somewhere

## 22370:00 - 22420:00

else the cloud changes

## 22420:00 - 22480:00

everything this one is

## 22480:00 - 22495:00

probably the mo probably the most

## 22495:00 - 22545:00

important one for me is that the cloud

## 22545:00 - 22590:00

makes it possible to do startups without

## 22590:00 - 22640:00

investing in infrastructure huge deal

## 22640:00 - 22675:00

but more than that you know all the

## 22675:00 - 22700:00

advantages that I've been talking about

## 22700:00 - 22735:00

up till now all those optimization

## 22735:00 - 22765:00

opportunities all those tricks that we

## 22765:00 - 22800:00

can play are possible here so I'm going

## 22800:00 - 22840:00

to cover quickly some of those and then

## 22840:00 - 22865:00

talk about some of the opportunities

## 22865:00 - 22895:00

that follow from

## 22895:00 - 22945:00

it first one let me convince you on

## 22945:00 - 22980:00

scale the cloud is different on scale

## 22980:00 - 23005:00

I've talked about scale all my life

## 23005:00 - 23030:00

every time I talk about scale I'm always

## 23030:00 - 23060:00

doing something bigger than last time

## 23060:00 - 23090:00

and so I think well that's that's high

## 23090:00 - 23140:00

scale this one feels pretty high scale

## 23140:00 - 23175:00

this one feels like we really are high

## 23175:00 - 23220:00

scale this time is we're growing I I put

## 23220:00 - 23245:00

this data together because I wanted to I

## 23245:00 - 23280:00

figured I figured we would be growing at

## 23280:00 - 23335:00

about an amazon.com in the year 2000

## 23335:00 - 23370:00

every month and if that was true be I

## 23370:00 - 23385:00

think it'd be an impressive number I

## 23385:00 - 23405:00

think it'd be a big number we're doing

## 23405:00 - 23445:00

that every day that means today we roll

## 23445:00 - 23480:00

enough gear into Data centers to support

## 23480:00 - 23520:00

amazon.com in the year 2000 that's a

## 23520:00 - 23560:00

$2.7 billion company not that small and

## 23560:00 - 23590:00

we'll do it again tomorrow and then

## 23590:00 - 23620:00

we'll do it the next day and we do it on

## 23620:00 - 23640:00

the

## 23640:00 - 23685:00

weekends I don't know how they do that

## 23685:00 - 23725:00

it's a big deal here's another scrap of

## 23725:00 - 23755:00

data we don't release enough we don't

## 23755:00 - 23775:00

release enough data but here's another

## 23775:00 - 23810:00

interesting scrap look at those object

## 23810:00 - 23860:00

counts a trillion what the heck is that

## 23860:00 - 23895:00

think about this think about how many

## 23895:00 - 23935:00

thousand servers in Cross how many data

## 23935:00 - 23965:00

centers it takes to store that many many

## 23965:00 - 24005:00

objects it's a pretty phenomenal number

## 24005:00 - 24030:00

every time I look at this I kind of go

## 24030:00 - 24070:00

really how about that how about data

## 24070:00 - 24125:00

centers here's the way Amazon works is

## 24125:00 - 24155:00

we have those little boxes those those

## 24155:00 - 24205:00

little boxes are are regions and each

## 24205:00 - 24235:00

one of those and each one of those

## 24235:00 - 24275:00

regions has multiple Data Centers inside

## 24275:00 - 24315:00

a region um we have what's called

## 24315:00 - 24350:00

availability zones each availability

## 24350:00 - 24385:00

zone is in fact a Data Center and the

## 24385:00 - 24415:00

way we get redundancy and reliability

## 24415:00 - 24435:00

and the way we encourage you to get

## 24435:00 - 24465:00

redundancy and reliability is run your

## 24465:00 - 24495:00

workload in multiple data centers in the

## 24495:00 - 24530:00

same region so you choose a region to

## 24530:00 - 24570:00

get close to your customers and once you

## 24570:00 - 24600:00

get once you choose a region then within

## 24600:00 - 24630:00

a region you replicate within the region

## 24630:00 - 24660:00

this is a totally different way than the

## 24660:00 - 24685:00

way the rest of the world does

## 24685:00 - 24725:00

redundancy most of the finance Community

## 24725:00 - 24745:00

does redundancy by having one data

## 24745:00 - 24770:00

center in Phoenix and one Data Center in

## 24770:00 - 24815:00

New York and if there's a failure then

## 24815:00 - 24840:00

all the smart people get together and

## 24840:00 - 24870:00

Phoenix is down should be fail over to

## 24870:00 - 24890:00

New York well if we fail over to New

## 24890:00 - 24940:00

York we lose data that's tough but if we

## 24940:00 - 24975:00

don't fail over to New York we lose we

## 24975:00 - 25020:00

lose availability so all the smartest

## 25020:00 - 25050:00

guys think hard and says is it going to

## 25050:00 - 25080:00

be down for an hour or a week and we

## 25080:00 - 25125:00

guess and we guess wrong every time and

## 25125:00 - 25155:00

it's always going to be up in an hour it

## 25155:00 - 25185:00

never is and so we lose availability

## 25185:00 - 25225:00

that's just what always happens so it

## 25225:00 - 25255:00

really is it really is because it it

## 25255:00 - 25285:00

always feels close how could it possibly

## 25285:00 - 25305:00

be down for more than an hour it's

## 25305:00 - 25335:00

impossible it's been years it's never

## 25335:00 - 25385:00

had a problem always a bad day so what

## 25385:00 - 25420:00

happens what happens in in the in the

## 25420:00 - 25450:00

availability zone model is you're doing

## 25450:00 - 25470:00

synchronous rep

## 25470:00 - 25495:00

between data centers that are only a few

## 25495:00 - 25540:00

milliseconds apart and it's synchronous

## 25540:00 - 25580:00

and so if if data center B is having

## 25580:00 - 25620:00

troubles maybe maybe it's not we just

## 25620:00 - 25670:00

think it is kill it costs nothing just

## 25670:00 - 25705:00

kill it kill the entire data center shut

## 25705:00 - 25735:00

down your whole capacity fail over to

## 25735:00 - 25765:00

another one things go on because we

## 25765:00 - 25795:00

can't predict we don't know the

## 25795:00 - 25820:00

difference between good and bad there's

## 25820:00 - 25855:00

always gray failures good and bad's

## 25855:00 - 25895:00

wonderful gray is terrible gray is

## 25895:00 - 25930:00

terrible and so you have to be wrong

## 25930:00 - 25960:00

sometimes this allows you to be wrong

## 25960:00 - 25985:00

you can say okay I think it's I think

## 25985:00 - 26025:00

it's probably broken so shoot it it's a

## 26025:00 - 26060:00

great way to work so believe it or not

## 26060:00 - 26100:00

it really is don't do it your employees

## 26100:00 - 26145:00

it's bad bad it's not General some of

## 26145:00 - 26185:00

these ideas don't generalize

## 26185:00 - 26235:00

okay scale again we one of our

## 26235:00 - 26265:00

postmortem I think we got frustrated

## 26265:00 - 26300:00

that somebody was talking about Amazon's

## 26300:00 - 26330:00

Virginia data center was

## 26330:00 - 26375:00

down and so we I think we wrote up there

## 26375:00 - 26405:00

was actually more than 10 we didn't say

## 26405:00 - 26430:00

how many but there was more than 10 data

## 26430:00 - 26475:00

centers in Virginia so one part of one/

## 26475:00 - 26515:00

tenth of our capacity was down was I

## 26515:00 - 26565:00

think the point we're driving home okay

## 26565:00 - 26595:00

what else can I tell you we're tight on

## 26595:00 - 26620:00

time because I'm having too much fun up

## 26620:00 - 26665:00

here let me say let me go quick then

## 26665:00 - 26710:00

first biggest gain the most powerful

## 26710:00 - 26745:00

lever we already we already covered this

## 26745:00 - 26785:00

is utilization I already told you the

## 26785:00 - 26815:00

tricks we can play in the cloud to drive

## 26815:00 - 26870:00

utilization trick one aggregating

## 26870:00 - 26915:00

non-correlated workloads it's Nob

## 26915:00 - 26945:00

brainer it just does the right thing for

## 26945:00 - 27000:00

you just magically second thing is

## 27000:00 - 27030:00

create a spot Market to fill the trough

## 27030:00 - 27090:00

we do that with with ec2 so utilization

## 27090:00 - 27120:00

is the most powerful lever and we can do

## 27120:00 - 27160:00

cool things with it what else can we

## 27160:00 - 27200:00

talk about data center efficiency

## 27200:00 - 27235:00

industry average data center efficiency

## 27235:00 - 27280:00

is rough numbers every time a watt's

## 27280:00 - 27325:00

delivered to a server roughly one watt

## 27325:00 - 27375:00

is wasted that's rough efficiency it's

## 27375:00 - 27415:00

not a great number it's it's not a great

## 27415:00 - 27460:00

place to be but for companies like us

## 27460:00 - 27495:00

that do nothing except study this

## 27495:00 - 27535:00

problem and hire people to go after this

## 27535:00 - 27575:00

problem it's a better number and so when

## 27575:00 - 27605:00

we deliver a watt we waste

## 27605:00 - 27650:00

about2 Watts it's a big it's a different

## 27650:00 - 27680:00

place to be and it makes total sense if

## 27680:00 - 27720:00

you only do one thing and you all you

## 27720:00 - 27755:00

hire for is people that know how to do

## 27755:00 - 27795:00

those things and all you try to drive

## 27795:00 - 27850:00

Innovation on is innovation in that

## 27850:00 - 27900:00

area it works and so this is the second

## 27900:00 - 27935:00

Advantage it's data centers are heck of

## 27935:00 - 27965:00

a lot better we're building

## 27965:00 - 27995:00

most companies build two data centers in

## 27995:00 - 28055:00

their entire careers we we'll we'll do

## 28055:00 - 28095:00

more than two in the next few months I

## 28095:00 - 28120:00

mean it's just it's it's a because

## 28120:00 - 28150:00

things are happening at a greater rate

## 28150:00 - 28195:00

it means the cycle time between idea and

## 28195:00 - 28225:00

trying it and saying not quite right and

## 28225:00 - 28250:00

changing it and and building the next

## 28250:00 - 28290:00

one is so fast it drives Innovation and

## 28290:00 - 28320:00

that's why things are changing faster

## 28320:00 - 28340:00

the reason why you're hearing so much

## 28340:00 - 28380:00

about data center um designs right now

## 28380:00 - 28415:00

is the pace of innovation is wildly

## 28415:00 - 28440:00

faster than it ever been

## 28440:00 - 28470:00

before

## 28470:00 - 28505:00

all right Hardware scale

## 28505:00 - 28545:00

effects Hardware companies buy from

## 28545:00 - 28585:00

original design manufacturers they they

## 28585:00 - 28615:00

take the gear they ship it over they

## 28615:00 - 28645:00

they ship it into the channel the

## 28645:00 - 28690:00

channel takes 30% eventually it works

## 28690:00 - 28715:00

its way through the channel and a

## 28715:00 - 28745:00

customer gets it the

## 28745:00 - 28795:00

customers have paid for the for the for

## 28795:00 - 28820:00

the fact that there's thousands and

## 28820:00 - 28845:00

thousands of customers and so there's a

## 28845:00 - 28875:00

complicated distribution Channel when

## 28875:00 - 28905:00

there's 10 Cloud providers they buy

## 28905:00 - 28930:00

directly from the original design

## 28930:00 - 28970:00

manufacturer we design design servers

## 28970:00 - 29000:00

for if we're going to run tens of

## 29000:00 - 29025:00

thousands or hundreds of thousands of a

## 29025:00 - 29055:00

workload the server is designed to

## 29055:00 - 29085:00

support that workload I don't care if it

## 29085:00 - 29135:00

can run nothing else is it's just that

## 29135:00 - 29160:00

workload is what it's going to run it's

## 29160:00 - 29190:00

going to run super well we're going to

## 29190:00 - 29215:00

optimize for that workload and we're

## 29215:00 - 29235:00

going to buy directly from the

## 29235:00 - 29260:00

manufacturer that builds that system

## 29260:00 - 29290:00

it's more efficient just be crazy to

## 29290:00 - 29325:00

think otherwise and people say well I

## 29325:00 - 29385:00

think actually I think actually my my

## 29385:00 - 29430:00

inefficient data center that I built in

## 29430:00 - 29465:00

in 1989

## 29465:00 - 29505:00

buying servers from IBM with this

## 29505:00 - 29535:00

complicated distribution channel is

## 29535:00 - 29560:00

probably I think it's more efficient

## 29560:00 - 29585:00

than than cloud computing I'm pretty

## 29585:00 - 29615:00

sure I've done the I built the model

## 29615:00 - 29660:00

it's like really I mean honest and oh

## 29660:00 - 29700:00

and all their suppliers are making 80%

## 29700:00 - 29735:00

margins you look up you look up e you

## 29735:00 - 29765:00

look up Amazon's margins they're single

## 29765:00 - 29800:00

digit and you look up

## 29800:00 - 29835:00

enterprise software companies and

## 29835:00 - 29875:00

they're 80% it means just really it's

## 29875:00 - 29930:00

cheaper doing that it's it be surprising

## 29930:00 - 29950:00

you know what's cool here's a cool one

## 29950:00 - 29995:00

here's here's a cool one last one we've

## 29995:00 - 30045:00

had 19 price reductions so far it's I

## 30045:00 - 30070:00

worked I've worked in Enterprise

## 30070:00 - 30095:00

software companies for my entire career

## 30095:00 - 30135:00

20-some years I have never had a price

## 30135:00 - 30190:00

reduction this is bizarre who's whatever

## 30190:00 - 30220:00

we have we have price reductions we have

## 30220:00 - 30240:00

price reductions where we have no

## 30240:00 - 30295:00

competitors think about that

## 30295:00 - 30345:00

there it's it's it's spooky and we and

## 30345:00 - 30380:00

it's normal what we do is we work like

## 30380:00 - 30420:00

heck to drive the to drive the cost down

## 30420:00 - 30445:00

every time we drive the cost down we

## 30445:00 - 30475:00

pass up of it on to customers we think

## 30475:00 - 30500:00

it's the right thing to do for customers

## 30500:00 - 30540:00

but it is at least for me it's spooky to

## 30540:00 - 30575:00

be reducing prices in some areas where

## 30575:00 - 30615:00

we don't even have competition and so um

## 30615:00 - 30640:00

it's kind of a good thing I'm pretty

## 30640:00 - 30670:00

sure it's a lot more efficient it makes

## 30670:00 - 30700:00

it a lot of fun for someone like me to

## 30700:00 - 30730:00

work in a place like that because the

## 30730:00 - 30770:00

rate of change is so great and it means

## 30770:00 - 30795:00

that we're constantly you know

## 30795:00 - 30835:00

delivering more value to customers which

## 30835:00 - 30885:00

kind of fun all

## 30885:00 - 30945:00

right let's see if we can last slide I

## 30945:00 - 30990:00

think it's important I'm but it goes

## 30990:00 - 31030:00

like this one of the concerns with AWS

## 31030:00 - 31045:00

if you're working in the startup

## 31045:00 - 31080:00

Community is wow gez AWS they do

## 31080:00 - 31120:00

everything by by hand they do how could

## 31120:00 - 31150:00

I ever sell anything to them and it's

## 31150:00 - 31205:00

true we we don't buy a ton of companies

## 31205:00 - 31230:00

but there's an interesting Factor going

## 31230:00 - 31265:00

on because cloud computing is as big as

## 31265:00 - 31295:00

I told you and it really is that big

## 31295:00 - 31315:00

there's going to be a huge number of

## 31315:00 - 31355:00

providers every Colo provider has to be

## 31355:00 - 31405:00

in cloud computing every Telco provider

## 31405:00 - 31430:00

has to be in cloud computing there's

## 31430:00 - 31475:00

going to be hundreds of TH or thousands

## 31475:00 - 31515:00

of providers of cloud computing if we do

## 31515:00 - 31565:00

something ourselves and don't buy it

## 31565:00 - 31590:00

sometimes you will but if we don't buy

## 31590:00 - 31630:00

if we do it ourselves what that means is

## 31630:00 - 31665:00

every other provider has to respond and

## 31665:00 - 31700:00

do something this is actually that's

## 31700:00 - 31725:00

what I'm calling the second tier effect

## 31725:00 - 31770:00

it drives a lot of opportunity if we do

## 31770:00 - 31800:00

a cool storage device like I described

## 31800:00 - 31850:00

to you earlier for flash storage then

## 31850:00 - 31890:00

great build that idea there's a whole

## 31890:00 - 31910:00

bunch of companies that just suddenly

## 31910:00 - 31945:00

developed a very big need to get that

## 31945:00 - 31970:00

and so there actually is quite a bit of

## 31970:00 - 32000:00

opportunity here so that's what I wanted

## 32000:00 - 32035:00

to cover with you thanks very much I

## 32035:00 - 32075:00

I've appreciated all of your time and uh

## 32075:00 - 32110:00

have enjoyed chatting with

## 32110:00 - 32175:00

you I'm guilty okay thank you so much

## 32175:00 - 32255:00

that was that was

## 32255:00+

great

