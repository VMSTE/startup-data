---
source: https://www.youtube.com/watch?v=iaOhgeCIj0w
title: "Workshop: High Performance Web Sites w/ Steve Souders of Google"
author: First Round Capital
date: 2013-04-08
views: 11167
description: >-
  Performance is critical for successful websites. In the past, the focus was on
  backend performance to make sure sites stayed up. Today the focus is on speed.
  Studies from Google, Yahoo!, Amazon, Microsoft, Netflix, and other leading
  websites show that a faster site results in a better user experience, more
  traffic, increased revenue, and lower operating costs. Steve Souders, Head
  Performance Engineer at Google, describes the best practices for building high
  performance websites. It turns out that 80%+ of the time the user is waiting
  is spent in the frontend, not the backend. These performance best practices
  include reducing the number and size of HTTP requests, loading JavaScript
  asynchronously, and making pages render more quickly. Attendees of this
  workshop will leave with a list of actionable takeaways that have a track
  record of making websites twice as fast. 


  About the speaker:


  Steve is the Head Performance Engineer at Google where he works on web
  performance and open source initiatives. He previously served as Chief
  Performance Yahoo!. Prior to that Steve worked at General Magic, WhoWhere?,
  and Lycos, and co-founded Helix Systems and CoolSync. Steve is the author of
  High Performance Web Sites and Even Faster Web Sites. He is the creator of
  YSlow, one of the top 25 Firefox add-ons. He's created numerous performance
  tools and services including the HTTP Archive, Cuzillion, Jdrop, ControlJS,
  and Browserscope. He serves as co-chair of Velocity, the web performance and
  operations conference from O'Reilly, and is co-founder of the Firebug Working
  Group. He taught CS193H: High Performance Web Sites at Stanford.
tags:
  - web performance
  - High Performance Web Sites
  - Google (Organization)
  - Steve Souders
  - javascript
  - yslow
  - o'reilly
  - first round capital
  - workshop
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T20:57:52.255Z
---

# Workshop: High Performance Web Sites w/ Steve Souders of Google

## 00:00 - 210:00

um so it's great to be here um I'll talk

## 210:00 - 235:00

a little bit about myself and my

## 235:00 - 270:00

background and why Google pays me to

## 270:00 - 300:00

come here and talk to first round

## 300:00 - 335:00

capital and this is being recorded right

## 335:00 - 360:00

yeah okay so maybe we'll turn the camera

## 360:00 - 390:00

off after a while and then I can say

## 390:00 - 410:00

some fun

## 410:00 - 465:00

things um and I read the list I to be

## 465:00 - 510:00

honest I don't know much about first CR

## 510:00 - 565:00

Capital um but I you know like I taught

## 565:00 - 620:00

at Stanford and uh was very excited to

## 620:00 - 675:00

do that I know Don can and he you know

## 675:00 - 735:00

greased the skids to get me in there and

## 735:00 - 760:00

the uh but it was kind of frustrating

## 760:00 - 805:00

because it was about I forget like 300

## 805:00 - 865:00

hours of work and I only had about 45

## 865:00 - 900:00

students in the class and so it was a

## 900:00 - 950:00

lot of time to put in for a small number

## 950:00 - 990:00

of people and most of those people

## 990:00 - 1035:00

didn't not go into building websites um

## 1035:00 - 1065:00

you know like less than half there were

## 1065:00 - 1115:00

uh people from all different departments

## 1115:00 - 1160:00

and disciplines and so then Google

## 1160:00 - 1205:00

Ventures asked me to do a workshop for

## 1205:00 - 1245:00

some of their portfolio companies and

## 1245:00 - 1295:00

was really good because um most of the

## 1295:00 - 1340:00

people most of the engineers knew like a

## 1340:00 - 1375:00

lot about the latest and greatest HTML 5

## 1375:00 - 1420:00

and blah blah blah um but maybe hadn't

## 1420:00 - 1460:00

like really drank the web performance

## 1460:00 - 1490:00

Kool-Aid yet or been exposed to a lot of

## 1490:00 - 1550:00

it and so um I really like this

## 1550:00 - 1595:00

opportunity um to talk to people who are

## 1595:00 - 1630:00

actively building websites and trying to

## 1630:00 - 1665:00

get as many people to consume them and

## 1665:00 - 1720:00

are really concerned about um business

## 1720:00 - 1740:00

Effectiveness we'll talk about that a

## 1740:00 - 1810:00

little bit and uh so I think it's a you

## 1810:00 - 1865:00

know I think the soil is very rich and

## 1865:00 - 1890:00

and so I hope this goes well I hope you

## 1890:00 - 1930:00

guys enjoy it and I was driving up here

## 1930:00 - 1960:00

that I don't know about you guys I live

## 1960:00 - 2000:00

in the South Bay and the last few days

## 2000:00 - 2030:00

been kind of gray and rainy and the sun

## 2030:00 - 2070:00

came out about noon today and so it's a

## 2070:00 - 2090:00

beautiful day out there so I don't want

## 2090:00 - 2120:00

to I was like really we're going to be

## 2120:00 - 2160:00

inside for two hours so we'll try to

## 2160:00 - 2180:00

keep it more an hour and a half and then

## 2180:00 - 2220:00

we can do Q&A for as long as you want

## 2220:00 - 2250:00

and Kevin sent me a list of the

## 2250:00 - 2285:00

companies coming and it was hugely

## 2285:00 - 2330:00

impressive a lot of companies that I use

## 2330:00 - 2365:00

and if it's okay you know maybe we'll

## 2365:00 - 2390:00

just kind of start over here and just

## 2390:00 - 2440:00

someone from each company shout out like

## 2440:00 - 2470:00

what company you're

## 2470:00 - 2865:00

from t

## 2865:00 - 2965:00

what was that last

## 2965:00 - 3010:00

one okay

## 3010:00 - 3025:00

how

## 3025:00 - 3070:00

about oh yeah I looked at your website

## 3070:00 - 3120:00

anyone from Uber oh cool did you say

## 3120:00 - 3200:00

Uber you guys are still stealth mode I

## 3200:00 - 3225:00

understand

## 3225:00 - 3270:00

okay and then I always make you know the

## 3270:00 - 3300:00

sad thing about doing so many of these

## 3300:00 - 3345:00

talks is um I've heard every joke that

## 3345:00 - 3385:00

I've told and so I think they're all

## 3385:00 - 3410:00

pretty lame well let's be honest they

## 3410:00 - 3450:00

are all pretty lame but you know even

## 3450:00 - 3500:00

for a terrible talk by a tech presenter

## 3500:00 - 3535:00

they're especially lame cuz I've heard

## 3535:00 - 3570:00

them all the time so one of the lame

## 3570:00 - 3590:00

things I always say before I start is

## 3590:00 - 3645:00

pay particular attention to the um

## 3645:00 - 3680:00

photos in the background of the slides

## 3680:00 - 3705:00

because that's where I've really put the

## 3705:00 - 3735:00

most time in this

## 3735:00 - 3795:00

talk um so this is the Story of My Life

## 3795:00 - 3875:00

see I take slow things and make them

## 3875:00 - 3910:00

fast we might have to turn the lights

## 3910:00 - 3950:00

out a little bit uh Brian and I were at

## 3950:00 - 3980:00

Yahoo for many years together I was

## 3980:00 - 4015:00

there for eight years I was the chief

## 4015:00 - 4055:00

performance Yahoo um which is the best

## 4055:00 - 4095:00

tile I've ever had um I've been at

## 4095:00 - 4120:00

Google for 5

## 4120:00 - 4190:00

years um most all the work I do is open

## 4190:00 - 4230:00

source um so my the biggest thing I did

## 4230:00 - 4275:00

was why slow that kind of started the

## 4275:00 - 4305:00

web performance you know interest and

## 4305:00 - 4345:00

stuff and I've done kazillion Sprite me

## 4345:00 - 4365:00

well actually look at those two today

## 4365:00 - 4405:00

Hammerhead browser scope was a big one

## 4405:00 - 4440:00

that lindsy Simon now at twist I think

## 4440:00 - 4475:00

right around the corner uh runs that

## 4475:00 - 4505:00

project and it's become

## 4505:00 - 4550:00

you know very very successful J drop is

## 4550:00 - 4585:00

one of the um JD drop and spritey were

## 4585:00 - 4620:00

two of the best things I ever built and

## 4620:00 - 4665:00

they never went anywhere um or they be

## 4665:00 - 4705:00

stayed very small HP archive has gotten

## 4705:00 - 4740:00

huge and we probably won't talk about

## 4740:00 - 4770:00

that too much today but I encourage you

## 4770:00 - 4815:00

to check it out htpr archive.org

## 4815:00 - 4880:00

um and I wrote These two books um that

## 4880:00 - 4930:00

were pretty popular I taught at Stanford

## 4930:00 - 4975:00

and I co-chair the Velocity Conference

## 4975:00 - 5025:00

we just announced New York so we have um

## 5025:00 - 5050:00

Santa Clara in

## 5050:00 - 5105:00

June um New York in October London in

## 5105:00 - 5180:00

November and Beijing in December um and

## 5180:00 - 5235:00

so the cfp has actually closed for June

## 5235:00 - 5255:00

if you think you have a really

## 5255:00 - 5295:00

compelling talk after today email me

## 5295:00 - 5335:00

we're just finishing the review process

## 5335:00 - 5370:00

so there's still some slots open but

## 5370:00 - 5405:00

certainly I'd encourage everyone to

## 5405:00 - 5445:00

attend it's gotten big it started you

## 5445:00 - 5470:00

know this is our fifth or sixth year and

## 5470:00 - 5530:00

it's gone from 500 to 25 200 people um

## 5530:00 - 5570:00

and it's all about operation scalability

## 5570:00 - 5595:00

performance all this stuff we'll talk

## 5595:00 - 5615:00

about

## 5615:00 - 5670:00

today so I think

## 5670:00 - 5715:00

today there are three main parts to what

## 5715:00 - 5755:00

I'm going to talk about so this first

## 5755:00 - 5785:00

part is the Kool-Aid part to just make

## 5785:00 - 5845:00

sure we're all on the bus and it'll be

## 5845:00 - 5895:00

pretty fast and to me it's kind of fun

## 5895:00 - 5935:00

uh I don't know if I get beat up for

## 5935:00 - 5980:00

showing an VC from another firm this is

## 5980:00 - 6015:00

Fred Wilson from Union Square how many

## 6015:00 - 6070:00

people know Fred or read his blog he

## 6070:00 - 6100:00

like blogs twice a day or something like

## 6100:00 - 6140:00

that that's amazing and he's probably

## 6140:00 - 6200:00

the number one VC out of New York

## 6200:00 - 6270:00

City individually maybe not collectively

## 6270:00 - 6320:00

and this is a few years ago um he was at

## 6320:00 - 6360:00

future of web apps and he talked about

## 6360:00 - 6400:00

his 10 golden principles of successful

## 6400:00 - 6435:00

web apps and number one on the list was

## 6435:00 - 6460:00

speed first and foremost we believe that

## 6460:00 - 6490:00

speed is more than a feature speed is

## 6490:00 - 6520:00

the most important feature and he went

## 6520:00 - 6575:00

on to talk about how they have all of

## 6575:00 - 6615:00

their portfolio companies monitored by

## 6615:00 - 6680:00

pingdom and in their empirical data

## 6680:00 - 6720:00

shows that certainly when the website's

## 6720:00 - 6755:00

performance drops off the business's

## 6755:00 - 6785:00

performance drops off and that's why he

## 6785:00 - 6830:00

and his uh partners are so keen on

## 6830:00 - 6900:00

performance um we had Alex Wagner speak

## 6900:00 - 6935:00

at keynote at philosopy last year from

## 6935:00 - 7005:00

Union Square and so this was to me was a

## 7005:00 - 7060:00

crossing point um about I think it was

## 7060:00 - 7110:00

three velocities ago I realized that we

## 7110:00 - 7155:00

were getting really good penetration in

## 7155:00 - 7195:00

the developer space but they were

## 7195:00 - 7260:00

running into roadblocks where a lot of

## 7260:00 - 7300:00

times depending on the company decision-

## 7300:00 - 7335:00

making does not rest in engineering it

## 7335:00 - 7390:00

rests in marketing or product management

## 7390:00 - 7445:00

and um that Engineers might be really

## 7445:00 - 7480:00

keen on performance like they are on

## 7480:00 - 7535:00

unit test or QA which maybe aren't the

## 7535:00 - 7570:00

world's most exciting things to talk

## 7570:00 - 7615:00

about or evangelize to someone in

## 7615:00 - 7665:00

product or sales or marketing and so

## 7665:00 - 7700:00

about three or four years ago I

## 7700:00 - 7735:00

collected a bunch of case studies to

## 7735:00 - 7770:00

come and present a philosophy about the

## 7770:00 - 7800:00

impact of performance on the bottom line

## 7800:00 - 7820:00

and I'm going to run through some of

## 7820:00 - 7860:00

those now and so to me this was a really

## 7860:00 - 7895:00

you know crossing over point where

## 7895:00 - 7965:00

without any effort of my own here's a

## 7965:00 - 8000:00

guy in the business world up and talking

## 8000:00 - 8030:00

about how critically important it is for

## 8030:00 - 8080:00

websites to be fast so that was very

## 8080:00 - 8115:00

cool and then um a bunch of case studies

## 8115:00 - 8155:00

came out that uh I managed on stage to

## 8155:00 - 8190:00

get Bing and Google search to stand up

## 8190:00 - 8225:00

because they had both told me on the

## 8225:00 - 8250:00

side that they had run the same

## 8250:00 - 8285:00

basically the same experiment which was

## 8285:00 - 8320:00

to introduce intentional delays into the

## 8320:00 - 8365:00

search results page and even deeper than

## 8365:00 - 8395:00

that I won't go into it at different

## 8395:00 - 8420:00

points what if it's on the server what

## 8420:00 - 8470:00

if it's after the nav head appears what

## 8470:00 - 8505:00

if it's after the first few results

## 8505:00 - 8555:00

appear you know uh very intricate stuff

## 8555:00 - 8595:00

um B took it up to 2 seconds and saw you

## 8595:00 - 8640:00

know all their goodness metrics drop off

## 8640:00 - 8665:00

perhaps most importantly Revenue per

## 8665:00 - 8725:00

user off 4% um Google uh only took it up

## 8725:00 - 8765:00

to 400 milliseconds and saw you know

## 8765:00 - 8830:00

percentage wise of a smaller change 6%

## 8830:00 - 8860:00

but at Google scale I mean there's a

## 8860:00 - 8905:00

direct correlation between uh searches

## 8905:00 - 8960:00

per user and AD revenue and so a drop

## 8960:00 - 9005:00

off of 6% at Google scale is a lot of

## 9005:00 - 9045:00

money and certainly if they had taken

## 9045:00 - 9100:00

this up higher um it's not a linear uh

## 9100:00 - 9135:00

curve it's uh you know geometric or

## 9135:00 - 9180:00

exponential so um it would have been a

## 9180:00 - 9205:00

lot bigger than that and the scary thing

## 9205:00 - 9270:00

about this was after you know we had

## 9270:00 - 9320:00

these buckets of users and after the

## 9320:00 - 9355:00

delay was removed we kept people

## 9355:00 - 9395:00

segmented in those buckets and the

## 9395:00 - 9435:00

people in this bucket it took them I

## 9435:00 - 9485:00

think it was 6 weeks to get back to the

## 9485:00 - 9515:00

Lev of search that they were doing

## 9515:00 - 9565:00

before the experiment started and so

## 9565:00 - 9600:00

this reaction of users to your website

## 9600:00 - 9635:00

to how fast or slow it is to what they

## 9635:00 - 9680:00

expect how they expect it to behave is

## 9680:00 - 9725:00

something that gets ingrained kind of

## 9725:00 - 9770:00

subconsciously and uh a important

## 9770:00 - 9795:00

takeaway of that is if you are running

## 9795:00 - 9830:00

any kind of performance experiments you

## 9830:00 - 9870:00

might need to keep in mind that if you

## 9870:00 - 9910:00

roll it out today you're not might not

## 9910:00 - 9935:00

see the impact of that the day after

## 9935:00 - 9965:00

that you might have to let it run for a

## 9965:00 - 10005:00

while similarly if things degrade you

## 10005:00 - 10050:00

might not see a drop off in in business

## 10050:00 - 10085:00

metrics the very next day after the drop

## 10085:00 - 10115:00

off it might take a while before users

## 10115:00 - 10165:00

really get turned off um but that was

## 10165:00 - 10190:00

exciting to see and it was exciting that

## 10190:00 - 10220:00

they all agreed and then Yahoo got into

## 10220:00 - 10280:00

it and um uh had a similar experiment

## 10280:00 - 10320:00

and for them 400 milliseconds resulted

## 10320:00 - 10355:00

in a 5 to 9% drop

## 10355:00 - 10405:00

off um here's a different kind of

## 10405:00 - 10445:00

business metrics Mozilla cares about uh

## 10445:00 - 10480:00

people downloading Firefox right they

## 10480:00 - 10535:00

don't focus on the money so much and so

## 10535:00 - 10585:00

they made their um IE landing page this

## 10585:00 - 10610:00

is if you're in IE and you want to

## 10610:00 - 10655:00

download Firefox you go to you get

## 10655:00 - 10690:00

redirected to the IE landing page they

## 10690:00 - 10735:00

made that page 2.2 seconds faster and

## 10735:00 - 10780:00

saw a 15% lift in

## 10780:00 - 10830:00

conversions yeah this is a more recent

## 10830:00 - 10860:00

one um this guy's going to speak at the

## 10860:00 - 10895:00

next velocity Kyle Rush worked on

## 10895:00 - 10945:00

Obama's uh most recent campaign and made

## 10945:00 - 11005:00

their campaign page uh 60% faster and it

## 11005:00 - 11075:00

had a 14% lift in donation

## 11075:00 - 11120:00

conversions so that's exciting unless

## 11120:00 - 11135:00

you're

## 11135:00 - 11195:00

Republican uh this is a seminal study

## 11195:00 - 11225:00

that was from the velocity three years

## 11225:00 - 11260:00

ago from Shopzilla where they covered so

## 11260:00 - 11300:00

much they made their site about 4

## 11300:00 - 11345:00

seconds F faster from 7 Seconds to 3

## 11345:00 - 11380:00

seconds and they saw a conversion rate

## 11380:00 - 11415:00

go up 7 to 12% they did deployed this

## 11415:00 - 11440:00

across different countries and different

## 11440:00 - 11480:00

types of uh product lines and so you

## 11480:00 - 11520:00

know there was some variation there um

## 11520:00 - 11575:00

this was a very uh exciting one where

## 11575:00 - 11605:00

they saw their um search engine

## 11605:00 - 11640:00

marketing basically

## 11640:00 - 11680:00

AdWords excuse me uh unique user

## 11680:00 - 11730:00

sessions more than double right and this

## 11730:00 - 11765:00

is because about 3 years ago Google

## 11765:00 - 11810:00

announced that um you know when you

## 11810:00 - 11845:00

participate in AdWords you have this

## 11845:00 - 11885:00

quality score and one of the components

## 11885:00 - 11915:00

of your quality score you know is like

## 11915:00 - 11960:00

do you have you know porn or you know

## 11960:00 - 12000:00

security stuff but also Al how fast is

## 12000:00 - 12040:00

your site and we announced this publicly

## 12040:00 - 12080:00

like three years ago and so they made

## 12080:00 - 12115:00

their site a lot faster they didn't do

## 12115:00 - 12145:00

anything else with bidding more money or

## 12145:00 - 12175:00

anything like that and you know if

## 12175:00 - 12215:00

you're you have a low quality score when

## 12215:00 - 12245:00

in the search results page even if you

## 12245:00 - 12280:00

pay the same amount as someone else who

## 12280:00 - 12310:00

you know has a fast site and doesn't

## 12310:00 - 12350:00

have porn and has good security you're

## 12350:00 - 12375:00

going to be demoted because your site is

## 12375:00 - 12415:00

lower and so just by making it from 7

## 12415:00 - 12450:00

Seconds to 3 seconds they moved up the

## 12450:00 - 12490:00

list and doubled their the impact

## 12490:00 - 12550:00

they're getting from their uh uh ad

## 12550:00 - 12585:00

expenses um so that was huge and this

## 12585:00 - 12625:00

was the first study that that touched on

## 12625:00 - 12665:00

this new area about reducing operating

## 12665:00 - 12705:00

costs so all the case studies so far

## 12705:00 - 12735:00

have had these increases in business

## 12735:00 - 12775:00

metrics and here's a decrease in

## 12775:00 - 12810:00

operating costs they could run the site

## 12810:00 - 12835:00

on half as much Hardware as they had

## 12835:00 - 12890:00

needed before and this makes total sense

## 12890:00 - 12915:00

how many people think this makes total

## 12915:00 - 12950:00

sense they improve the site and and they

## 12950:00 - 12985:00

need half as much Hardware because

## 12985:00 - 13040:00

because you add an expires header and

## 13040:00 - 13075:00

now it used to be that every time the

## 13075:00 - 13120:00

user loaded the page they'd at least

## 13120:00 - 13165:00

have to Ping the server and see if that

## 13165:00 - 13200:00

image was expired yet or not even if the

## 13200:00 - 13255:00

server said no 304 not modified you can

## 13255:00 - 13295:00

s you that's still a hit on the server

## 13295:00 - 13355:00

and most Pages have 50 to 100 images on

## 13355:00 - 13400:00

them and so all of a sudden if you add

## 13400:00 - 13440:00

an expires header users don't have to

## 13440:00 - 13465:00

keep pinging your server so you're going

## 13465:00 - 13495:00

to see the load on your server decreased

## 13495:00 - 13540:00

by about 90% right just by adding an

## 13540:00 - 13580:00

expires header and also the bandwidth

## 13580:00 - 13605:00

out is going to drop well we'll see that

## 13605:00 - 13630:00

one next I

## 13630:00 - 13670:00

think yeah so this was Bill Scott from

## 13670:00 - 13705:00

Yahoo do you remember Bill uh worked on

## 13705:00 - 13755:00

yui with Doug crockford on Ajax stuff

## 13755:00 - 13805:00

and then he went to meibo and Netflix

## 13805:00 - 13865:00

twice and now he's at PayPal with Doug

## 13865:00 - 13900:00

but when he was at Netflix they had had

## 13900:00 - 13940:00

one of those experiences like in 1998

## 13940:00 - 13970:00

where they had compressed JavaScript and

## 13970:00 - 13995:00

someone with

## 13995:00 - 14015:00

uh you know

## 14015:00 - 14070:00

Windows 3.1 that hadn't downloaded

## 14070:00 - 14125:00

Service Pack 2 had a bug where if you

## 14125:00 - 14160:00

compressed JavaScript it would you know

## 14160:00 - 14180:00

the page wouldn't load or something like

## 14180:00 - 14210:00

that and they decided never to compress

## 14210:00 - 14260:00

anything ever again and so he turned on

## 14260:00 - 14295:00

compression and the knock called him up

## 14295:00 - 14325:00

and said the sight's down he said why do

## 14325:00 - 14380:00

you think that they said well our uh

## 14380:00 - 14410:00

traffic leaving the data center just

## 14410:00 - 14435:00

dropped in half the only thing we can be

## 14435:00 - 14475:00

serving is the error page he said nope

## 14475:00 - 14510:00

we just turned on compression and

## 14510:00 - 14535:00

dropped outbound traffic from the data

## 14535:00 - 14570:00

center in half how many people here know

## 14570:00 - 14605:00

how much you pay for traffic in your

## 14605:00 - 14620:00

data

## 14620:00 - 14695:00

center anyone so cut in half like at

## 14695:00 - 14740:00

least five if not six figures a month

## 14740:00 - 14790:00

yeah so one simple change turn on

## 14790:00 - 14835:00

compression uh and there's very few

## 14835:00 - 14875:00

people who have ie6 without Service Pack

## 14875:00 - 14940:00

2 so the chances of a bug are very

## 14940:00 - 15000:00

low um here's Ishmael from edmonds.com

## 15000:00 - 15065:00

he took over a new site and wanted to do

## 15065:00 - 15110:00

a small change very quickly to convince

## 15110:00 - 15145:00

his team that performance was critical

## 15145:00 - 15180:00

and the rest of the company and so in

## 15180:00 - 15210:00

two days they added an expires header

## 15210:00 - 15250:00

and removed eags and they were using

## 15250:00 - 15295:00

aamai and their aamai traffic dropped by

## 15295:00 - 15335:00

a third how many people here use

## 15335:00 - 15400:00

aami not that many wow uh so again

## 15400:00 - 15435:00

imagine cutting your bill by a third

## 15435:00 - 15480:00

right it's huge and this is a very uh

## 15480:00 - 15505:00

it's more complex than turn down

## 15505:00 - 15525:00

compression but it's still a fairly

## 15525:00 - 15540:00

simple

## 15540:00 - 15580:00

change um and then Google you know

## 15580:00 - 15630:00

earlier we announced um latency was part

## 15630:00 - 15665:00

of AdWords quality score about two years

## 15665:00 - 15695:00

ago we announced it was part of SEO it

## 15695:00 - 15755:00

was part of page rank um and so and we

## 15755:00 - 15800:00

go on to qualify that it's one of 200

## 15800:00 - 15860:00

signals and etc etc etc so it's not the

## 15860:00 - 15935:00

hugest thing in the world um but uh it

## 15935:00 - 15970:00

it is a factor and certainly people care

## 15970:00 - 16005:00

about SE

## 16005:00 - 16025:00

so

## 16025:00 - 16040:00

[Music]

## 16040:00 - 16090:00

um so you know you want to make your

## 16090:00 - 16125:00

website fast what and so I saw all these

## 16125:00 - 16160:00

things kind of converging about two

## 16160:00 - 16200:00

years ago and I've been kind of tracking

## 16200:00 - 16215:00

these things in the background and

## 16215:00 - 16250:00

waiting for this uh you know

## 16250:00 - 16300:00

serendipitous moment and said okay it's

## 16300:00 - 16325:00

time to announce this new industry so I

## 16325:00 - 16370:00

call it wpo I'm really good at names

## 16370:00 - 16400:00

this is not a very good name but I

## 16400:00 - 16445:00

thought about it over the weekend and

## 16445:00 - 16470:00

it's the best I could come up with that

## 16470:00 - 16500:00

had a website available and stuff like

## 16500:00 - 16530:00

that so it stands for web performance

## 16530:00 - 16555:00

optimization and it's been fairly well

## 16555:00 - 16585:00

adopted there's now about 20 or 30

## 16585:00 - 16615:00

companies in the space and they pretty

## 16615:00 - 16670:00

much label themselves wpo companies or

## 16670:00 - 16715:00

sometimes feo frontend

## 16715:00 - 16760:00

optimization um and the elevator pitch

## 16760:00 - 16805:00

is it drives TR traffic to your site we

## 16805:00 - 16845:00

saw this with it affects page rank it

## 16845:00 - 16905:00

affects uh your AdWords quality score um

## 16905:00 - 16930:00

we all know it improves the user

## 16930:00 - 16960:00

experience but we don't have to take

## 16960:00 - 16995:00

that we don't have to just trust our gut

## 16995:00 - 17030:00

on that there are all these studies from

## 17030:00 - 17070:00

B and Google search that show even

## 17070:00 - 17095:00

though the websites are faster people

## 17095:00 - 17125:00

spend more time on the site they do more

## 17125:00 - 17170:00

page views um per session more sessions

## 17170:00 - 17205:00

per month so they do that because the

## 17205:00 - 17245:00

user experience is better they love it

## 17245:00 - 17280:00

um more and we saw again many studies

## 17280:00 - 17315:00

that talk about increasing revenue and

## 17315:00 - 17345:00

the icing on the cake is it reduces your

## 17345:00 - 17365:00

operating

## 17365:00 - 17415:00

costs how many people want these

## 17415:00 - 17505:00

things okay it's hot is it hot

## 17505:00 - 17540:00

anything we can do that oh I can talk

## 17540:00 - 17605:00

louder yeah um so that's wpo okay so

## 17605:00 - 17640:00

that's that's the first part how do we

## 17640:00 - 17670:00

feel about making websites fast are we

## 17670:00 - 17720:00

all on the bus yeah yeah let me hear you

## 17720:00 - 17795:00

say yeah yeah come on

## 17795:00 - 17865:00

louder okay on three one two three yes

## 17865:00 - 17900:00

okay we want to make websites faster it

## 17900:00 - 17920:00

is so

## 17920:00 - 17960:00

frustrating come

## 17960:00 - 18035:00

on okay okay part two so I've been

## 18035:00 - 18055:00

thrown around this you know web

## 18055:00 - 18095:00

performance optimization kind of Loosey

## 18095:00 - 18140:00

Goosey um let me get a little more

## 18140:00 - 18175:00

precise there so actually most of my

## 18175:00 - 18230:00

career working on the web up until 2002

## 18230:00 - 18310:00

2003 was on the back end um and then uh

## 18310:00 - 18340:00

Ash and Jeff Rolston came and asked me

## 18340:00 - 18380:00

to uh work start this Performance Group

## 18380:00 - 18420:00

at Yahoo and I said oh cool because I

## 18420:00 - 18450:00

know a lot about backend optimization

## 18450:00 - 18490:00

always like optimizing a achy and

## 18490:00 - 18525:00

compilers and stuff like that and Jeff

## 18525:00 - 18565:00

said no no no and it's kind of a funny

## 18565:00 - 18595:00

story but I'm on video but I won't so I

## 18595:00 - 18635:00

won't tell it I'll tell it after um I

## 18635:00 - 18670:00

want you to do it from the end users

## 18670:00 - 18705:00

perspective and I'm embarrassed to admit

## 18705:00 - 18735:00

you know by this time I had run the my

## 18735:00 - 18775:00

Yahoo team for two or three years I had

## 18775:00 - 18810:00

never looked at like how a browser loads

## 18810:00 - 18840:00

a web page like I had always looked at

## 18840:00 - 18875:00

it from apache's perspective and if we

## 18875:00 - 18940:00

could cut apache's time from 200

## 18940:00 - 18980:00

milliseconds to 180 milliseconds on

## 18980:00 - 19015:00

average that was pretty good and it was

## 19015:00 - 19040:00

a it would take months of work to make

## 19040:00 - 19085:00

that happen um so I'm kind of talking

## 19085:00 - 19110:00

about a different kind of performance

## 19110:00 - 19145:00

here and and this is the way I try to

## 19145:00 - 19210:00

break it down is um certainly back in

## 19210:00 - 19260:00

the web 10 days this holds very true

## 19260:00 - 19300:00

today you know some of these other

## 19300:00 - 19350:00

requests can be dynamic but certainly in

## 19350:00 - 19390:00

the web 10 days okay so so first of all

## 19390:00 - 19415:00

this is a waterfall chart how many

## 19415:00 - 19440:00

people have looked at a waterfall chart

## 19440:00 - 19485:00

in the last week

## 19485:00 - 19520:00

okay so it's good you're here um the

## 19520:00 - 19550:00

other people uh well it's good the

## 19550:00 - 19565:00

people who raised your hand I'm glad

## 19565:00 - 19610:00

you're here too okay so the other people

## 19610:00 - 19645:00

I'm really glad you're here okay so this

## 19645:00 - 19690:00

is a waterfall chart each horizontal bar

## 19690:00 - 19740:00

is an HTTP request it's a resource right

## 19740:00 - 19780:00

and um I forget where I got this I think

## 19780:00 - 19820:00

I got from webpagetest.org we'll look at

## 19820:00 - 19850:00

that later and you can see the time that

## 19850:00 - 19875:00

it takes and the different colors or

## 19875:00 - 19930:00

different things like DNS look up uh TC

## 19930:00 - 19970:00

uh I forget what that is TCP connection

## 19970:00 - 20040:00

and and uh data download and certainly

## 20040:00 - 20080:00

in the web1 world all of these things

## 20080:00 - 20120:00

were static stuff mostly images you know

## 20120:00 - 20180:00

we started adding CSS and JavaScript um

## 20180:00 - 20225:00

but all of the backend computation time

## 20225:00 - 20265:00

where you're optimizing databases and

## 20265:00 - 20305:00

optimizing rpcs and trying to make you

## 20305:00 - 20380:00

know rpcs asynchronous and um you know

## 20380:00 - 20420:00

optimizing the compiler and doing you

## 20420:00 - 20470:00

know uh dlls and things like that all of

## 20470:00 - 20540:00

that was in this part the backend part

## 20540:00 - 20595:00

right and all this part I call front end

## 20595:00 - 20635:00

part now a lot of people like to break

## 20635:00 - 20690:00

it into three categories backend Network

## 20690:00 - 20720:00

and front end and by front end certainly

## 20720:00 - 20755:00

we think of things like parsing

## 20755:00 - 20795:00

executing JavaScript applying Styles

## 20795:00 - 20835:00

parsing the HTML and laying out the Dom

## 20835:00 - 20865:00

all that stuff is expensive but there's

## 20865:00 - 20905:00

also a lot of network time going in here

## 20905:00 - 20945:00

but the reason I just I I just lump

## 20945:00 - 20990:00

Network in the front end is the browser

## 20990:00 - 21020:00

is going to do pretty much what you tell

## 21020:00 - 21055:00

it to do and it turns out that there are

## 21055:00 - 21115:00

a ton of ways that you can tell the

## 21115:00 - 21145:00

browser to manage the network more

## 21145:00 - 21185:00

efficiently without changing the network

## 21185:00 - 21215:00

conditions at all and this was true for

## 21215:00 - 21250:00

the very first engagement I did back in

## 21250:00 - 21310:00

2004 the team said uh well what do you

## 21310:00 - 21335:00

want to we back then we had this deal

## 21335:00 - 21365:00

with SBC and people were still using a

## 21365:00 - 21395:00

lot of dial UPS well what do you want us

## 21395:00 - 21430:00

to do give everyone a free DSL account

## 21430:00 - 21460:00

we can't do that they're they have slow

## 21460:00 - 21480:00

network connections there's nothing we

## 21480:00 - 21510:00

can do and within a month we had made

## 21510:00 - 21560:00

the page twice as fast right and the

## 21560:00 - 21590:00

network conditions hadn't changed just

## 21590:00 - 21625:00

the way that we told the browser how to

## 21625:00 - 21660:00

use the network had changed and by doing

## 21660:00 - 21685:00

that we could make things much more

## 21685:00 - 21725:00

efficient so netk there are some things

## 21725:00 - 21760:00

you can't do about Network there's some

## 21760:00 - 21815:00

you know it definitely is a factor but I

## 21815:00 - 21845:00

lump it into this front-end part because

## 21845:00 - 21890:00

the people creating the page and and

## 21890:00 - 21950:00

that um set of commands the HTML that's

## 21950:00 - 21990:00

commanding the browser what do those

## 21990:00 - 22030:00

people can cause that Network to be very

## 22030:00 - 22065:00

inefficient used very inefficiently or

## 22065:00 - 22100:00

very efficiently and so I want these

## 22100:00 - 22150:00

people to feel some uh responsibility

## 22150:00 - 22190:00

for that and and you know take that into

## 22190:00 - 22215:00

consideration when they're building and

## 22215:00 - 22265:00

deploying their pages and so you know I

## 22265:00 - 22295:00

looked at this and I forget what this is

## 22295:00 - 22325:00

it might be Google Search now but you

## 22325:00 - 22380:00

know eight years ago it was my Yahoo and

## 22380:00 - 22445:00

I was like wow all the time that you

## 22445:00 - 22475:00

know it's like that story about the

## 22475:00 - 22500:00

drunk looking for his keys under the

## 22500:00 - 22525:00

street light but really lost them

## 22525:00 - 22565:00

somewhere else but the street light like

## 22565:00 - 22595:00

all that time i' had been trying to make

## 22595:00 - 22625:00

my Yahoo faster I'd been looking at

## 22625:00 - 22670:00

Apache because that's what I knew and

## 22670:00 - 22700:00

that's how the web grew these you know

## 22700:00 - 22730:00

it grew from people who knew servers and

## 22730:00 - 22765:00

backends and not so much of this stuff

## 22765:00 - 22805:00

we added this stuff you know dhtml and

## 22805:00 - 22820:00

stuff

## 22820:00 - 22875:00

later so this is where we focused and

## 22875:00 - 22910:00

still where most companies Focus their

## 22910:00 - 22955:00

performance efforts is on this backend

## 22955:00 - 22990:00

part and I'm not saying you shouldn't do

## 22990:00 - 23050:00

that half a velocity is on this part

## 23050:00 - 23095:00

but you should focus on this part if

## 23095:00 - 23135:00

you're worried about availability and

## 23135:00 - 23190:00

failover and downtime right if what you

## 23190:00 - 23225:00

want to do is make the user experience

## 23225:00 - 23260:00

faster create a faster experience for

## 23260:00 - 23300:00

the users you got to focus on this part

## 23300:00 - 23340:00

the front end part so when I saw this I

## 23340:00 - 23365:00

was like

## 23365:00 - 23415:00

Wow uh I've been looking at the for

## 23415:00 - 23440:00

years I've been looking at the wrong

## 23440:00 - 23480:00

part I've been optimizing the small poll

## 23480:00 - 23520:00

in the tent the short pole in the tent

## 23520:00 - 23545:00

well maybe it's an anomaly so I started

## 23545:00 - 23575:00

looking at other Yahoo sites they all

## 23575:00 - 23610:00

had the same profile I looked at the

## 23610:00 - 23655:00

Alexa top 10 the Alexa top 100 every

## 23655:00 - 23680:00

site that I've looked at for the last

## 23680:00 - 23720:00

eight years pretty much holds true for

## 23720:00 - 23755:00

this there are some exceptions but by

## 23755:00 - 23785:00

and large this is true this is what

## 23785:00 - 23850:00

you'll see for uh almost all Sites so uh

## 23850:00 - 23920:00

just recently I went back I think these

## 23920:00 - 23965:00

are uh I forget how long ago it was

## 23965:00 - 24005:00

about 6 months months ago um but I bet I

## 24005:00 - 24030:00

could go and look again and they'd be

## 24030:00 - 24100:00

the same so um if we look at the Alexa

## 24100:00 - 24155:00

top 10 uh they have about 27% of the

## 24155:00 - 24180:00

time that the user is waiting for the

## 24180:00 - 24220:00

page to load is on the back end but

## 24220:00 - 24265:00

these sites are highly highly optimized

## 24265:00 - 24300:00

they have very few requests and so the

## 24300:00 - 24345:00

pi is very small and the HTML document

## 24345:00 - 24380:00

this is basically how much is the HML

## 24380:00 - 24415:00

document of the page load time out of

## 24415:00 - 24460:00

the whole page load time and uh for them

## 24460:00 - 24510:00

27 % on average is the HTML document

## 24510:00 - 24530:00

they typically this is like the Google

## 24530:00 - 24575:00

front page the Yahoo uh search front

## 24575:00 - 24620:00

page um very few request the pi is very

## 24620:00 - 24650:00

small so the HTML document is a bigger

## 24650:00 - 24725:00

slice of the P if we step up to

## 24725:00 - 24795:00

the Alexa top 1000 177% is spent on the

## 24795:00 - 24870:00

back end and the top 100,000 16% and so

## 24870:00 - 24910:00

this was the really the first kind of

## 24910:00 - 24965:00

performance work Discovery thing that I

## 24965:00 - 25010:00

published is the performance Golden Rule

## 25010:00 - 25055:00

where from looking at all these sites I

## 25055:00 - 25130:00

say 80 to 9 80 to 90% of the time that

## 25130:00 - 25165:00

the user is waiting for the page to load

## 25165:00 - 25200:00

is on this front end part front end and

## 25200:00 - 25250:00

networking part so if you want to make

## 25250:00 - 25295:00

the site faster that's where you got to

## 25295:00 - 25330:00

focus and and to drive it home I tell

## 25330:00 - 25355:00

most people you know I might look at

## 25355:00 - 25375:00

their site just to make sure they know

## 25375:00 - 25400:00

that like they're not running on

## 25400:00 - 25430:00

WordPress and my sql's really slow or

## 25430:00 - 25470:00

something like that but almost always

## 25470:00 - 25525:00

always I see this profile this 8020 Rule

## 25525:00 - 25565:00

and I say you know you could and they

## 25565:00 - 25600:00

keep wanting to go back to optimize the

## 25600:00 - 25635:00

back in well maybe you know if we run on

## 25635:00 - 25690:00

AWS or Rackspace instead of a or we buy

## 25690:00 - 25725:00

our own servers or we I'm like you know

## 25725:00 - 25750:00

what I'm just telling you like you could

## 25750:00 - 25800:00

reduce the backend time to zero and most

## 25800:00 - 25845:00

people wouldn't notice right because

## 25845:00 - 25880:00

you're going from the average site loads

## 25880:00 - 25935:00

in about 8 seconds so if you could cut

## 25935:00 - 26000:00

uh 10% of that it would be 7 .2 seconds

## 26000:00 - 26025:00

people aren't going to care but if you

## 26025:00 - 26080:00

can cut the front end time in half which

## 26080:00 - 26120:00

we've done successfully over and over

## 26120:00 - 26160:00

and over again you can make a 8sec site

## 26160:00 - 26215:00

4 seconds right so this is where you

## 26215:00 - 26235:00

really need to focus if you want to make

## 26235:00 - 26280:00

the website fast there's just if you

## 26280:00 - 26315:00

look there's a a priori greater

## 26315:00 - 26340:00

probability that you're going to have an

## 26340:00 - 26390:00

impact if you work on this long pole

## 26390:00 - 26435:00

than on this short Pole right the

## 26435:00 - 26470:00

changes are simpler we're not re

## 26470:00 - 26505:00

architecting we're not sharding across

## 26505:00 - 26550:00

multiple data centers we're adding an

## 26550:00 - 26595:00

expires header we're turning on gzip

## 26595:00 - 26630:00

right most of the changes are far

## 26630:00 - 26660:00

simpler than a backend

## 26660:00 - 26695:00

optimization and they've been proven to

## 26695:00 - 26725:00

work over the last eight years I've

## 26725:00 - 26750:00

worked with a ton of sites there's all

## 26750:00 - 26785:00

these other companies and by deploying

## 26785:00 - 26840:00

these best practices um we can make site

## 26840:00 - 26885:00

it's pretty easy to make sites twice as

## 26885:00 - 26930:00

fast so I want to talk a little bit

## 26930:00 - 26960:00

about so I Define kind of when I throw

## 26960:00 - 26990:00

the word performance around really what

## 26990:00 - 27020:00

I mean is front-end performance not

## 27020:00 - 27065:00

scalability I really mean how fast it is

## 27065:00 - 27085:00

from the user's

## 27085:00 - 27135:00

perspective um then I want to talk about

## 27135:00 - 27170:00

fast like I say how fast it is what do

## 27170:00 - 27210:00

you mean fast okay so let's talk a

## 27210:00 - 27240:00

little bit about metrics so suppose I do

## 27240:00 - 27295:00

a search for Steve saouter and uh I get

## 27295:00 - 27335:00

back search results and I click on the

## 27335:00 - 27390:00

one for my website right so this is the

## 27390:00 - 27420:00

first I'm going to highlight here four

## 27420:00 - 27465:00

or five time measurements that we should

## 27465:00 - 27510:00

all be familiar with and probably we

## 27510:00 - 27535:00

should be tracking oh and I didn't

## 27535:00 - 27580:00

mention that before so I think just like

## 27580:00 - 27640:00

Union Square if uh first round Capital

## 27640:00 - 27685:00

doesn't have it already I think what

## 27685:00 - 27715:00

Fred is doing there with having a

## 27715:00 - 27745:00

dashboard for all the portfolio

## 27745:00 - 27790:00

companies that is using standard metrics

## 27790:00 - 27840:00

I encourage every VC to do that I think

## 27840:00 - 27865:00

that's really really valuable and I

## 27865:00 - 27900:00

noticed a lot of the companies here or

## 27900:00 - 27930:00

the ones who get submitted URLs are

## 27930:00 - 27970:00

doing that with New Relic or some other

## 27970:00 - 28000:00

uh metrics and we'll give some examples

## 28000:00 - 28065:00

in just a few slides so these are all uh

## 28065:00 - 28125:00

uh con conceptual names of of timing

## 28125:00 - 28165:00

metrics fast metrics that would be good

## 28165:00 - 28205:00

to be aware of so there's time to First

## 28205:00 - 28230:00

Bite so I've clicked on the search

## 28230:00 - 28300:00

result and it's gone to steve.com that

## 28300:00 - 28330:00

and that's the back end has stitched

## 28330:00 - 28375:00

together an HTML document and the first

## 28375:00 - 28435:00

packet of that HTML document is back and

## 28435:00 - 28485:00

it's not until that first packet comes

## 28485:00 - 28540:00

back that the browser clears the screen

## 28540:00 - 28585:00

right so if the user clicks on a search

## 28585:00 - 28625:00

result and your page is your backend is

## 28625:00 - 28655:00

really really slow they're going to be

## 28655:00 - 28680:00

staring at Google search and they're

## 28680:00 - 28710:00

going to be like well how come what's

## 28710:00 - 28740:00

going on and they'll click on it again

## 28740:00 - 28775:00

which will just reset that timer and

## 28775:00 - 28795:00

click on and finally they'll click on

## 28795:00 - 28850:00

the next result so time to first bite it

## 28850:00 - 28890:00

it's important to keep that pretty short

## 28890:00 - 28935:00

right and that will clear the browser

## 28935:00 - 28985:00

right but until it gets enough to parse

## 28985:00 - 29015:00

it's not going to display anything and

## 29015:00 - 29040:00

if there's anything blocking we'll talk

## 29040:00 - 29060:00

about that anything that's blocking

## 29060:00 - 29090:00

parsing this is what the user is going

## 29090:00 - 29125:00

to be staring at and there's people in

## 29125:00 - 29170:00

here at least for the test I ran where

## 29170:00 - 29195:00

people are staring at this for more than

## 29195:00 - 29220:00

10

## 29220:00 - 29255:00

seconds and I'll point out those

## 29255:00 - 29285:00

companies toward the

## 29285:00 - 29335:00

end and there's no did you lock the door

## 29335:00 - 29375:00

no leaving early no leaving early okay

## 29375:00 - 29420:00

then there's the start render Point okay

## 29420:00 - 29460:00

there's nothing blocking the page or at

## 29460:00 - 29490:00

least we got it out of the way and I got

## 29490:00 - 29530:00

enough of the HTML document parsed that

## 29530:00 - 29560:00

I can start drawing something and this

## 29560:00 - 29580:00

is really important this is what Jacob

## 29580:00 - 29610:00

neelon would talk about get about giving

## 29610:00 - 29650:00

the user feedback progress bar and stuff

## 29650:00 - 29685:00

like that well the page itself is a

## 29685:00 - 29725:00

progress bar right if it stays blank the

## 29725:00 - 29760:00

user is not getting any update so this

## 29760:00 - 29790:00

is giving the user update so it's really

## 29790:00 - 29830:00

important to know when did it go blank

## 29830:00 - 29865:00

and when did I start showing the user

## 29865:00 - 29900:00

that the server is actually not an idiot

## 29900:00 - 29920:00

that it's doing something and it's

## 29920:00 - 29950:00

working and eventually I'll get the page

## 29950:00 - 29985:00

to you okay

## 29985:00 - 30020:00

then we have above the fold so this is

## 30020:00 - 30060:00

where basically almost all the content

## 30060:00 - 30090:00

that the user is expecting or cares

## 30090:00 - 30140:00

about or once is going to appear and the

## 30140:00 - 30180:00

definition of fold depends we can come

## 30180:00 - 30205:00

up with kind of an industry standard but

## 30205:00 - 30240:00

you get the idea of what I mean is most

## 30240:00 - 30290:00

of the stuff up here is showing and then

## 30290:00 - 30325:00

there's finally what we probably are all

## 30325:00 - 30355:00

actually measuring this is the thing

## 30355:00 - 30395:00

that is kind of the de facto performance

## 30395:00 - 30430:00

how fast is it thing to measure is the

## 30430:00 - 30470:00

window.onload time the page load time

## 30470:00 - 30500:00

and that's going to include everything

## 30500:00 - 30550:00

including stuff below the fold right all

## 30550:00 - 30585:00

the stuff that you load all the images

## 30585:00 - 30620:00

the window.onload is not going to fire

## 30620:00 - 30655:00

which means the logo is going to

## 30655:00 - 30680:00

continue to spin the status bar is going

## 30680:00 - 30720:00

to continue to flash until all of the

## 30720:00 - 30740:00

images all the scripts all the

## 30740:00 - 30775:00

stylesheets in the page have been

## 30775:00 - 30810:00

downloaded and parsed by the

## 30810:00 - 30875:00

browser so those are four metrics that

## 30875:00 - 30905:00

would be really good to keep in mind and

## 30905:00 - 30935:00

we'll talk about those some more as we

## 30935:00 - 31030:00

go on and then this is kind of fun so um

## 31030:00 - 31070:00

it used to be three or four years ago

## 31070:00 - 31115:00

that window.onload was all people cared

## 31115:00 - 31170:00

about and not just me but one drum I've

## 31170:00 - 31205:00

been beating for the last three or four

## 31205:00 - 31235:00

years is Progressive rendering

## 31235:00 - 31285:00

Progressive enhancement so it is

## 31285:00 - 31330:00

important to reduce your window.on load

## 31330:00 - 31390:00

but really we as an industry has adopted

## 31390:00 - 31420:00

window.onload because it's the best

## 31420:00 - 31470:00

proxy what we really want to optimize is

## 31470:00 - 31510:00

the user's perception but there's no

## 31510:00 - 31535:00

JavaScript event for the user's

## 31535:00 - 31580:00

perception so window.onload in the web

## 31580:00 - 31660:00

10 world was the best proxy we had for

## 31660:00 - 31710:00

the user's perception but with web 2o

## 31710:00 - 31750:00

it's not right because we can have stuff

## 31750:00 - 31775:00

below the fold that takes a really long

## 31775:00 - 31820:00

time to load uh we are sending beacons

## 31820:00 - 31860:00

and stuff like that um that don't really

## 31860:00 - 31900:00

affect the user experience and the page

## 31900:00 - 31935:00

is actually rendered above the fold and

## 31935:00 - 31965:00

so really what we want to do is f Fus

## 31965:00 - 31995:00

more on rendering the problem is it's

## 31995:00 - 32040:00

really hard to measure that um but we

## 32040:00 - 32095:00

can just as humans we can you know parse

## 32095:00 - 32130:00

that pretty easily so for example

## 32130:00 - 32160:00

suppose you know these are both my

## 32160:00 - 32185:00

website you guys recognize it because

## 32185:00 - 32255:00

you go there every day and um just if

## 32255:00 - 32300:00

you had to boote vote A or B you know it

## 32300:00 - 32340:00

starts off it's blank finally we get

## 32340:00 - 32385:00

something to render this one it renders

## 32385:00 - 32420:00

about halfway at six seconds and then at

## 32420:00 - 32450:00

eight seconds it's fully rendered above

## 32450:00 - 32510:00

the fold this one it it has the same

## 32510:00 - 32550:00

amount of progressive rendering and then

## 32550:00 - 32590:00

at 6 seconds it's done which do you

## 32590:00 - 32635:00

think is better a or b um what do you

## 32635:00 - 32685:00

think A or

## 32685:00 - 32755:00

B yeah you don't want to answer oh you

## 32755:00 - 32810:00

okay yeah you can answer B it's pretty

## 32810:00 - 32850:00

obvious right these two are the same and

## 32850:00 - 32890:00

this is better than that so B is B is

## 32890:00 - 32940:00

better if I could have my website do one

## 32940:00 - 32965:00

or the other which would I pick i' pick

## 32965:00 - 32995:00

B

## 32995:00 - 33055:00

okay how about this one blank a little

## 33055:00 - 33100:00

bit of rendering fully rendered blank

## 33100:00 - 33145:00

blank fully rendered which would be

## 33145:00 - 33170:00

better what do you

## 33170:00 - 33200:00

think yeah because you're giving the

## 33200:00 - 33255:00

user some feedback this user after three

## 33255:00 - 33290:00

or 4 seconds is going to say let me go

## 33290:00 - 33315:00

back to search results and see what the

## 33315:00 - 33350:00

next one is

## 33350:00 - 33385:00

right okay so that was pretty easy they

## 33385:00 - 33440:00

get a little harder blank

## 33440:00 - 33495:00

blank uh

## 33495:00 - 33590:00

blank Progressive Progressive done

## 33590:00 - 33670:00

done this one's a little harder what a

## 33670:00 - 33710:00

because you gave the user feedback

## 33710:00 - 33780:00

sooner I would actually take B here but

## 33780:00 - 33830:00

it's close but

## 33830:00 - 33900:00

now yeah now here is the hardest one and

## 33900:00 - 33935:00

the last

## 33935:00 - 33985:00

one this one's fully rendered at

## 33985:00 - 34035:00

six but it didn't have much

## 34035:00 - 34085:00

feedback this one had more feedback and

## 34085:00 - 34130:00

is fully rendered at

## 34130:00 - 34190:00

6.2 which of those is

## 34190:00 - 34240:00

better I would take a and this is what I

## 34240:00 - 34280:00

mean by tail wagging the dog is

## 34280:00 - 34330:00

sometimes we get focused on the numbers

## 34330:00 - 34370:00

especially as engineers and so like

## 34370:00 - 34390:00

we're going to look at this chart of

## 34390:00 - 34440:00

window.onload and we're mostly looking

## 34440:00 - 34465:00

at that because there's nothing built in

## 34465:00 - 34495:00

the browser right now that gives us

## 34495:00 - 34515:00

feedback about

## 34515:00 - 34575:00

rendering and I've seen this many times

## 34575:00 - 34590:00

where we

## 34590:00 - 34640:00

deploy um performance optimization best

## 34640:00 - 34680:00

practices and it makes the onload time

## 34680:00 - 34730:00

slower but it makes the user experience

## 34730:00 - 34780:00

better and so people are like yeah but

## 34780:00 - 34830:00

you know we're tracking window.onload a

## 34830:00 - 34880:00

lot of it people maybe more on the East

## 34880:00 - 34920:00

Coast actually get their bonuses set by

## 34920:00 - 34960:00

the window.onload calculated by Keynote

## 34960:00 - 35015:00

or Gomez and so like if you're going to

## 35015:00 - 35065:00

make the unload slower there's a lot of

## 35065:00 - 35115:00

resistance to that and here I I'll say

## 35115:00 - 35145:00

we didn't make the user experience that

## 35145:00 - 35175:00

much better but a lot of times you can

## 35175:00 - 35215:00

make it significantly better um like

## 35215:00 - 35260:00

lazy loading images right let's make

## 35260:00 - 35305:00

sure everything above the fold renders

## 35305:00 - 35335:00

first and then we'll start downloading

## 35335:00 - 35365:00

all the other stuff below the fold and

## 35365:00 - 35410:00

by inserting that delay you might

## 35410:00 - 35440:00

actually kick off those below the- fold

## 35440:00 - 35475:00

images later than you would of otherwise

## 35475:00 - 35505:00

which will make the onload fire later

## 35505:00 - 35535:00

but you've guaranteed the stuff the user

## 35535:00 - 35575:00

can see is going to appear sooner and

## 35575:00 - 35600:00

that's a better user experience so you

## 35600:00 - 35630:00

got to be a little careful about what

## 35630:00 - 35700:00

you're focusing on um it's a little

## 35700:00 - 35735:00

tricky

## 35735:00 - 35780:00

so uh this kind of ties into that how

## 35780:00 - 35845:00

many people know about rum data a few

## 35845:00 - 35925:00

people so um how can you gather this dat

## 35925:00 - 35950:00

this timing data well you can do it

## 35950:00 - 35975:00

synthetically

## 35975:00 - 36005:00

um this is where you know we basically

## 36005:00 - 36050:00

mean we're not using real users like

## 36050:00 - 36080:00

we're asking QA people to do it with a

## 36080:00 - 36110:00

stopwatch or a wristwatch we're running

## 36110:00 - 36165:00

in a lab we're using uh you know some

## 36165:00 - 36230:00

automated service um keynote a web page

## 36230:00 - 36270:00

test which I'll show in a minute uh you

## 36270:00 - 36300:00

know water selenium we're building

## 36300:00 - 36340:00

scripts in a lab um but it's not real

## 36340:00 - 36385:00

users we've got a can list of URLs that

## 36385:00 - 36420:00

we're running through now one of the

## 36420:00 - 36465:00

benefits of this is because it's running

## 36465:00 - 36500:00

in this synthetic environment that we

## 36500:00 - 36555:00

control the variables are very well

## 36555:00 - 36605:00

understood I'll give a great example is

## 36605:00 - 36635:00

well here let me talk about so there's

## 36635:00 - 36675:00

fewer variables so because there's fewer

## 36675:00 - 36730:00

variables if you see a regression you

## 36730:00 - 36780:00

can diagnose the cause of that much more

## 36780:00 - 36825:00

quickly it's easier to isolate causes um

## 36825:00 - 36855:00

and you can also gather more metrics

## 36855:00 - 36910:00

like um there's nothing available in

## 36910:00 - 36940:00

JavaScript that tells you the browser

## 36940:00 - 36975:00

the machine CPU but if you're doing this

## 36975:00 - 37015:00

in the lab you can have gather CPU stats

## 37015:00 - 37045:00

pretty easily and that's something that

## 37045:00 - 37090:00

we care about so and memory and when did

## 37090:00 - 37120:00

things render there's no way to do

## 37120:00 - 37175:00

render capturing uh out in the real

## 37175:00 - 37195:00

world but you can do it if you're

## 37195:00 - 37250:00

running in a lab whereas uh ROM real

## 37250:00 - 37300:00

user monitoring is with real users and

## 37300:00 - 37325:00

typically we do this with JavaScript in

## 37325:00 - 37355:00

the page and we look at these events

## 37355:00 - 37415:00

like um window.onload uh we can put a

## 37415:00 - 37455:00

script tag at the very top inside the

## 37455:00 - 37490:00

head tag and that will basically tell us

## 37490:00 - 37570:00

the time to first bite um uh so uh

## 37570:00 - 37590:00

that's what it's done real user you

## 37590:00 - 37620:00

deploy it on your live website running

## 37620:00 - 37650:00

out in the world again I mentioned I saw

## 37650:00 - 37675:00

a lot of people doing that with New

## 37675:00 - 37695:00

Relic you can do it with Google

## 37695:00 - 37745:00

analytics I should add New Relic here um

## 37745:00 - 37800:00

Boomerang is from Yahoo uh torbit is a

## 37800:00 - 37855:00

new company that offers rum uh service

## 37855:00 - 37905:00

and the pro about this is um here I had

## 37905:00 - 37960:00

to come up with a list of URLs to back

## 37960:00 - 37990:00

and I always go back I know Brian from

## 37990:00 - 38020:00

Yahoo sports I always have this Sports

## 38020:00 - 38060:00

analogy where uh the tour to France is

## 38060:00 - 38095:00

going on but you know when you set up

## 38095:00 - 38155:00

your lab you picked you know SL you know

## 38155:00 - 38225:00

sports.com NFL MLB NBA those are the

## 38225:00 - 38260:00

most popular Pages well right now this

## 38260:00 - 38300:00

week when the Tour of France is going on

## 38300:00 - 38350:00

Psy SL cycling is the most popular page

## 38350:00 - 38375:00

and you don't have any monitoring on

## 38375:00 - 38395:00

that right because you didn't change

## 38395:00 - 38430:00

your you don't change your lab setup

## 38430:00 - 38475:00

depending on what time of year it is is

## 38475:00 - 38535:00

um and so this reflects what users are

## 38535:00 - 38585:00

really doing it reflects um what browser

## 38585:00 - 38630:00

they have what their Hardware is like is

## 38630:00 - 38655:00

it slow is it fast are they upgrade

## 38655:00 - 38680:00

Hardware I don't know but if I measure

## 38680:00 - 38725:00

it on real users it's my real users so

## 38725:00 - 38775:00

it's the hardware my users actually use

## 38775:00 - 38815:00

um what's their Network conditions

## 38815:00 - 38840:00

what's their page flow are they going to

## 38840:00 - 38875:00

cycling or MLB where are they

## 38875:00 - 38930:00

geographically located uh uh Etc I'll

## 38930:00 - 39000:00

give a great example of this is um

## 39000:00 - 39055:00

uh uh there's a very popular website

## 39055:00 - 39140:00

that had a regression in their um uh rum

## 39140:00 - 39210:00

data but it was not reflected here right

## 39210:00 - 39260:00

and it turned out they had run an ad

## 39260:00 - 39320:00

campaign in a European country that had

## 39320:00 - 39365:00

like gone up 10x in the number of people

## 39365:00 - 39400:00

using that website and there was no data

## 39400:00 - 39455:00

center near there so all of those 10x

## 39455:00 - 39490:00

amount of people were contributing

## 39490:00 - 39535:00

really slow rum times and so that was a

## 39535:00 - 39580:00

time that we really cared about having

## 39580:00 - 39615:00

both of these in place we could go here

## 39615:00 - 39635:00

and we could go well we don't think it's

## 39635:00 - 39665:00

a regression with the code because when

## 39665:00 - 39695:00

we control the variables so what's going

## 39695:00 - 39730:00

on outside of the variables and that was

## 39730:00 - 39765:00

that way we were able to uh lead us to

## 39765:00 - 39785:00

things that said well let's break it

## 39785:00 - 39840:00

down by country wow in this country uh

## 39840:00 - 39870:00

we've got a 10x increase what happened

## 39870:00 - 39905:00

and then one of the engineers connected

## 39905:00 - 39935:00

with someone in marketing who said oh

## 39935:00 - 39970:00

yeah we just did that you know marketing

## 39970:00 - 40020:00

campaign there um vice versa is like the

## 40020:00 - 40065:00

cycling example or which browser are you

## 40065:00 - 40090:00

running on you're probably not going to

## 40090:00 - 40140:00

run on you know three or certainly five

## 40140:00 - 40185:00

or 10 browsers in the lab but your users

## 40185:00 - 40230:00

might be swinging from IE to Chrome or

## 40230:00 - 40265:00

something like that and so you want to

## 40265:00 - 40315:00

make sure to capture that so both are

## 40315:00 - 40355:00

important I think this one is a little

## 40355:00 - 40405:00

easier and lower cost um I always like

## 40405:00 - 40445:00

to start looking at this data and then

## 40445:00 - 40495:00

only fall back to this data if I can't

## 40495:00 - 40525:00

figure out what's going on here or I see

## 40525:00 - 40560:00

like unexplained regressions when I see

## 40560:00 - 40610:00

a regression that happens when I see rum

## 40610:00 - 40655:00

data get slow on the day we do a push I

## 40655:00 - 40700:00

know it's the push

## 40700:00 - 40755:00

right okay oh and here's just some

## 40755:00 - 40785:00

screenshots how many people here use

## 40785:00 - 40820:00

Google

## 40820:00 - 40865:00

analytics so how many people here know

## 40865:00 - 40900:00

Google analytics is recording how fast

## 40900:00 - 40955:00

your website is oh that's very cool yeah

## 40955:00 - 41000:00

so we added that um by default about a

## 41000:00 - 41065:00

year ago um and we told you know we told

## 41065:00 - 41090:00

people and it's available inside I think

## 41090:00 - 41135:00

this is the old UI actually but uh you

## 41135:00 - 41175:00

can go into Google analytics now even if

## 41175:00 - 41200:00

you've never set it up we're Gathering

## 41200:00 - 41240:00

rum data as part of Google analytics

## 41240:00 - 41285:00

running in your website we do a very

## 41285:00 - 41315:00

small sample size but you can do some

## 41315:00 - 41365:00

JavaScript and increase the sample size

## 41365:00 - 41385:00

um so even if you haven't been doing

## 41385:00 - 41410:00

anything there's probably a Year's worth

## 41410:00 - 41460:00

of rum data for you and here

## 41460:00 - 41520:00

um Philip Tellis from Yahoo started this

## 41520:00 - 41550:00

company called log normal that just got

## 41550:00 - 41605:00

acquired by sosta a load they a load uh

## 41605:00 - 41650:00

testing company and they offer rum data

## 41650:00 - 41680:00

and some nice plots and torbit is this

## 41680:00 - 41750:00

other startup down um in Sano or

## 41750:00 - 41800:00

something like that okay so that's what

## 41800:00 - 41860:00

I mean by performance and how to measure

## 41860:00 - 41915:00

speed so this is the last part some of

## 41915:00 - 41945:00

the best practices so I'm just going to

## 41945:00 - 41995:00

really really quick and I I forgot to

## 41995:00 - 42025:00

tell people to stop and ask questions

## 42025:00 - 42090:00

stop me and ask questions cuz so I don't

## 42090:00 - 42110:00

know about you so far I'd probably be

## 42110:00 - 42140:00

really bored there's just this one guy

## 42140:00 - 42180:00

talking on and on and on yeah have you

## 42180:00 - 42200:00

told any

## 42200:00 - 42240:00

[Laughter]

## 42240:00 - 42295:00

jokes

## 42295:00 - 42335:00

uh well there was the one about slow

## 42335:00 - 42385:00

things fast and focus on the background

## 42385:00 - 42465:00

uh things yeah that's yeah um but from

## 42465:00 - 42500:00

this point forward when I do them I'll

## 42500:00 - 42520:00

highlight them

## 42520:00 - 42575:00

afterward so we can track those

## 42575:00 - 42625:00

better any other

## 42625:00 - 42690:00

questions okay so about 20 minutes okay

## 42690:00 - 42730:00

we're going to Rifle through these so it

## 42730:00 - 42770:00

turned out uh both books had a very

## 42770:00 - 42805:00

simple thing how many people remember

## 42805:00 - 42840:00

Scott Meyer's effective

## 42840:00 - 42905:00

C++ yeah I love that book and so I kind

## 42905:00 - 42945:00

of modeled my book after that I wanted a

## 42945:00 - 42980:00

book where you could read one chapter by

## 42980:00 - 43020:00

itself and it really didn't depend on

## 43020:00 - 43045:00

anything you know you could read it if

## 43045:00 - 43080:00

you had and the book is small so you

## 43080:00 - 43105:00

could read it like if you're on the bus

## 43105:00 - 43170:00

for 15 or 20 minutes so just 14

## 43170:00 - 43215:00

Standalone best practices and it's much

## 43215:00 - 43290:00

more web 10 sort of stuff gzip and

## 43290:00 - 43350:00

um uh you know expires header HTTP stuff

## 43350:00 - 43385:00

avoiding redirects and it turned out the

## 43385:00 - 43455:00

second book had 14 rules too um but a

## 43455:00 - 43525:00

lot of what I focused

## 43525:00 - 43575:00

on were these weird

## 43575:00 - 43620:00

idiosyncrasies about how browsers work

## 43620:00 - 43650:00

and it was really fun because I would

## 43650:00 - 43665:00

like

## 43665:00 - 43715:00

blackbox play with a browser and go wow

## 43715:00 - 43740:00

I wonder why it does I would just notice

## 43740:00 - 43770:00

things as I'm you know using websites

## 43770:00 - 43795:00

wow why did that take so long and I'd

## 43795:00 - 43830:00

open up a packet sniffer huh I wonder

## 43830:00 - 43850:00

why those scripts are all downloading

## 43850:00 - 43890:00

sequentially oh wow look at that that's

## 43890:00 - 43915:00

the way all browsers download scripts

## 43915:00 - 43945:00

they download them sequentially at least

## 43945:00 - 43975:00

in how about the other browsers yep

## 43975:00 - 44010:00

Firefox yep Opera yep back then Chrome

## 44010:00 - 44075:00

wasn't around and um one of the ways I

## 44075:00 - 44100:00

did that was with this tool kazillion

## 44100:00 - 44140:00

how many people here have played with

## 44140:00 - 44185:00

kazillion okay so I'm going to try to do

## 44185:00 - 44220:00

this and I think it will work first I'm

## 44220:00 - 44250:00

going to escape out

## 44250:00 - 44305:00

of PowerPoint and then I'm going to go

## 44305:00 - 44350:00

to

## 44350:00 - 44430:00

Chrome and we going to go to kazillion

## 44430:00 - 44500:00

docomo and and so I built this because I

## 44500:00 - 44525:00

actually built this for the second book

## 44525:00 - 44560:00

because there were so many weird

## 44560:00 - 44590:00

scenarios I wanted to test and I was

## 44590:00 - 44620:00

building like a custom test page for

## 44620:00 - 44660:00

each scenario and I started writing the

## 44660:00 - 44695:00

second book and I realized I had like

## 44695:00 - 44740:00

390 test scenarios and I like didn't

## 44740:00 - 44775:00

want to build that many pages so I just

## 44775:00 - 44820:00

created this so like one that's really

## 44820:00 - 44890:00

interesting is um let's add an external

## 44890:00 - 44940:00

stylesheet let's make it take 5 Seconds

## 44940:00 - 44985:00

to download

## 44985:00 - 45055:00

load and then let's add an image and by

## 45055:00 - 45080:00

default everything takes 2 seconds to

## 45080:00 - 45125:00

download let's just say there's no delay

## 45125:00 - 45185:00

this is a delay on the server and so now

## 45185:00 - 45215:00

I can actually request this

## 45215:00 - 45280:00

page so let's count the image is going

## 45280:00 - 45305:00

to show up at the top it'll be like a

## 45305:00 - 45340:00

little turtle or crab or something like

## 45340:00 - 45370:00

that let's see how long it takes for

## 45370:00 - 45455:00

that to show up 1 1,00 2 1,00 3 1,00 4

## 45455:00 - 45480:00

1,00 5

## 45480:00 - 45550:00

1,000 so if the crab doesn't take any

## 45550:00 - 45570:00

time to

## 45570:00 - 45630:00

download how come it took 5 Seconds well

## 45630:00 - 45655:00

guess what if we change the stylesheet

## 45655:00 - 45685:00

to take 7even seconds it's going to take

## 45685:00 - 45715:00

7 seconds if we change the sty sheet to

## 45715:00 - 45740:00

take 3 seconds it's going to take 3

## 45740:00 - 45775:00

seconds and that's because stylesheets

## 45775:00 - 45850:00

block all rendering in the page right um

## 45850:00 - 45880:00

let's see what are some other well I

## 45880:00 - 45925:00

don't have I IE here but you know so we

## 45925:00 - 45995:00

can do this we can um

## 45995:00 - 46050:00

uh by creating these examples really

## 46050:00 - 46085:00

quickly and easily we can kind of look

## 46085:00 - 46140:00

at the nuances of how browsers work and

## 46140:00 - 46170:00

the other thing that's really cool is

## 46170:00 - 46210:00

you can just these uh you know you can

## 46210:00 - 46265:00

copy and paste these URLs in any browser

## 46265:00 - 46305:00

or send them to you know submit them in

## 46305:00 - 46385:00

bugs to um browser developers and people

## 46385:00 - 46430:00

can recreate the test page over and over

## 46430:00 - 46470:00

and over again cons consistently um so

## 46470:00 - 46490:00

this is a really fun thing if you're

## 46490:00 - 46515:00

ever wondering like what's the

## 46515:00 - 46545:00

interaction like oh so here's another

## 46545:00 - 46595:00

good one um okay uh let's

## 46595:00 - 46770:00

clear and let's add one 2 3 4 five six

## 46770:00 - 46820:00

7 seven images that each take two

## 46820:00 - 46855:00

seconds to

## 46855:00 - 46880:00

download what do you think the

## 46880:00 - 46915:00

window.onload time for this page is

## 46915:00 - 46970:00

going to be

## 46970:00 - 47025:00

yeah four seconds

## 47025:00 - 47070:00

why download six things at

## 47070:00 - 47125:00

once so here let's create the

## 47125:00 - 47180:00

page and we see six show up and then the

## 47180:00 - 47210:00

seventh one and if we look down here I

## 47210:00 - 47260:00

show the onload time is 4 seconds now if

## 47260:00 - 47290:00

we delete one of

## 47290:00 - 47355:00

those and create that

## 47355:00 - 47410:00

page it's 2 seconds so that's how it's

## 47410:00 - 47445:00

really easy to see and it turns out most

## 47445:00 - 47480:00

most major browsers do six connections

## 47480:00 - 47505:00

per host name but there are some out

## 47505:00 - 47525:00

there that do eight and some that do

## 47525:00 - 47570:00

four and with this you can really easily

## 47570:00 - 47620:00

create a test case to see how browsers

## 47620:00 - 47670:00

work so kazillion kind of fun uh that

## 47670:00 - 47695:00

you know so I think I'm pretty good at

## 47695:00 - 47725:00

names because there are zillion pages to

## 47725:00 - 47745:00

check

## 47745:00 - 47800:00

gazillion yeah okay so here's the first

## 47800:00 - 47820:00

rule from the book so I'm just going to

## 47820:00 - 47845:00

touch on a couple of these things make

## 47845:00 - 47875:00

fewer HP requests it turns out it's

## 47875:00 - 47915:00

still the number one rule in the second

## 47915:00 - 47955:00

book and for anything that you do

## 47955:00 - 48005:00

um this is an actual chart of the uh

## 48005:00 - 48055:00

size of pages over the last two years

## 48055:00 - 48120:00

from the HTTP archive um so things are

## 48120:00 - 48140:00

just getting bigger and bigger the

## 48140:00 - 48195:00

average website in November was 87 HTP

## 48195:00 - 48265:00

requests 1.3 Meg um each HTP request has

## 48265:00 - 48295:00

overhead even if you're reusing

## 48295:00 - 48335:00

connections uh cookies have to be sent

## 48335:00 - 48395:00

every time um uh you know if you're

## 48395:00 - 48430:00

starting new connections then you might

## 48430:00 - 48480:00

have uh slow start

## 48480:00 - 48550:00

um uh and so you know one way to make

## 48550:00 - 48575:00

sites faster is just to tell the

## 48575:00 - 48610:00

designers to take stuff off the page and

## 48610:00 - 48650:00

that never goes over really well so the

## 48650:00 - 48690:00

challenge I set for myself was eight

## 48690:00 - 48725:00

years ago was can we make it faster with

## 48725:00 - 48750:00

the stuff that's already on the page and

## 48750:00 - 48785:00

it turns out you can you can do things

## 48785:00 - 48870:00

like um okay so anyone know what this

## 48870:00 - 48925:00

is whoa I spent a lot of time in

## 48925:00 - 48955:00

Nebraska growing up so

## 48955:00 - 48975:00

I didn't think other people would get

## 48975:00 - 49040:00

that okay so that was a joke end end

## 49040:00 - 49080:00

Nebraska

## 49080:00 - 49125:00

yeah

## 49125:00 - 49170:00

okay so I don't mean combine scripts

## 49170:00 - 49200:00

with stylesheets everyone probably knows

## 49200:00 - 49225:00

this now I just mean concatenate your

## 49225:00 - 49255:00

script you know

## 49255:00 - 49310:00

typically you know we used to have 10 to

## 49310:00 - 49365:00

20 to 30 scripts on a page and it's just

## 49365:00 - 49390:00

put those scripts together because

## 49390:00 - 49445:00

scripts block things in the page and if

## 49445:00 - 49465:00

you put them together they're going to

## 49465:00 - 49495:00

get done faster scripts are the most

## 49495:00 - 49535:00

painful when it comes to Performance

## 49535:00 - 49560:00

thing to download bite forbite than

## 49560:00 - 49595:00

anything else on the page so you want to

## 49595:00 - 49625:00

get those out of the way if you have

## 49625:00 - 49655:00

multiple stylesheets stylesheets are the

## 49655:00 - 49680:00

next most painful bite forbite thing to

## 49680:00 - 49720:00

download concatenate those into one to

## 49720:00 - 49750:00

get them downloaded more and you can

## 49750:00 - 49795:00

take these to extremes like if you if

## 49795:00 - 49830:00

you have you know

## 49830:00 - 49880:00

600k of CSS well you might want to break

## 49880:00 - 49905:00

it into two that can download in

## 49905:00 - 49960:00

parallel but for most people um it's

## 49960:00 - 49995:00

good to just put it into one and you can

## 49995:00 - 50040:00

do that there's uh modules to do that

## 50040:00 - 50085:00

there's a a combo Handler blog post you

## 50085:00 - 50135:00

can read and recreate that yourself um

## 50135:00 - 50180:00

you can use data URLs I saw several

## 50180:00 - 50210:00

websites doing that in the list that I

## 50210:00 - 50270:00

got um that just means that anything

## 50270:00 - 50320:00

that actually could generate an HTTP

## 50320:00 - 50350:00

request you can

## 50350:00 - 50410:00

actually excuse me just embed that HTTP

## 50410:00 - 50460:00

response in the page itself you do that

## 50460:00 - 50525:00

by um encoding it as base 64 and so you

## 50525:00 - 50570:00

know anywhere where you can put a URL

## 50570:00 - 50625:00

you can put a data colon um response

## 50625:00 - 50685:00

body and you say what it is and Bas 64

## 50685:00 - 50740:00

and mostly this is good for small things

## 50740:00 - 50770:00

um not just images but also scripts and

## 50770:00 - 50820:00

stylesheets um why small because Bas 64

## 50820:00 - 50850:00

encoding in actually makes it bigger and

## 50850:00 - 50875:00

it's also kind of a pain in the neck to

## 50875:00 - 50925:00

deal with also it's in the page itself

## 50925:00 - 50990:00

so very rarely do we say cach my HTML

## 50990:00 - 51045:00

response um but if it's like 100k of

## 51045:00 - 51070:00

JavaScript you put that in a separate

## 51070:00 - 51105:00

script and you say cach the script by

## 51105:00 - 51140:00

itself but for small things it's

## 51140:00 - 51175:00

probably better to put it in the page

## 51175:00 - 51230:00

than generate a new HTTP request um oh

## 51230:00 - 51255:00

there is a little bit of a workaround

## 51255:00 - 51295:00

like if it's background images rather

## 51295:00 - 51330:00

than embeded in the page you could embed

## 51330:00 - 51355:00

it in the style sheet and keep that

## 51355:00 - 51390:00

cached forever so that would be a way to

## 51390:00 - 51440:00

reduce images images are about 60% of

## 51440:00 - 51485:00

all the byes downloaded uh on pages

## 51485:00 - 51530:00

these days yeah for small images is that

## 51530:00 - 51560:00

preferred over spring a bunch of them

## 51560:00 - 51595:00

together well I think that's kind of a

## 51595:00 - 51620:00

personal preference thing I'll talk

## 51620:00 - 51670:00

about spriting next um to me spriting is

## 51670:00 - 51710:00

kind of a even bigger pain in the neck

## 51710:00 - 51735:00

like you could automate something like

## 51735:00 - 51775:00

this in your build process or in your

## 51775:00 - 51830:00

server um it's really I've met very few

## 51830:00 - 51855:00

people who automate the creation of

## 51855:00 - 51895:00

Sprites and the CSS the connection

## 51895:00 - 51940:00

between the CN CSS and Sprites is is

## 51940:00 - 51980:00

really complicated so I would prefer

## 51980:00 - 52015:00

this technique if there were things that

## 52015:00 - 52050:00

I could Sprite that I used like for a

## 52050:00 - 52105:00

long period of time uh I would do that

## 52105:00 - 52135:00

but I I wouldn't want to do anything as

## 52135:00 - 52165:00

a Sprite that I have to change like on a

## 52165:00 - 52240:00

monthly or weekly

## 52240:00 - 52310:00

basis speaking of

## 52310:00 - 52350:00

Sprites

## 52350:00 - 52405:00

um yeah

## 52405:00 - 52445:00

so now I broke something before but I'm

## 52445:00 - 52485:00

going to go for it

## 52485:00 - 52525:00

again um here's where we're going look

## 52525:00 - 52585:00

at mod cloth where was mod

## 52585:00 - 52625:00

cloth okay

## 52625:00 - 52685:00

so uh I looked at some of the

## 52685:00 - 52720:00

[Music]

## 52720:00 - 52765:00

um websites out there and some people

## 52765:00 - 52810:00

are already using Sprites um this was

## 52810:00 - 52855:00

one that you know isn't super compelling

## 52855:00 - 52895:00

but I think there's a good compelling

## 52895:00 - 52950:00

reason to use Sprites on the site so I

## 52950:00 - 52990:00

wrote this um bookmarklet called Sprite

## 52990:00 - 53020:00

me you can go to Sprite me.org and get

## 53020:00 - 53045:00

it and so it's a bookmarklet I just

## 53045:00 - 53110:00

click on it and it loads every image

## 53110:00 - 53160:00

every CSS background image in the page

## 53160:00 - 53190:00

and you can just go over these and hover

## 53190:00 - 53225:00

over them and see you know all the

## 53225:00 - 53270:00

background images in the page and oh so

## 53270:00 - 53335:00

look you guys are using Sprites cool

## 53335:00 - 53405:00

right um and it turns out it's really

## 53405:00 - 53430:00

complicated there's a lot of Arcane

## 53430:00 - 53470:00

knowledge in what images you can combine

## 53470:00 - 53520:00

together like are they repeat X repeat y

## 53520:00 - 53605:00

both um are they uh in an element that's

## 53605:00 - 53640:00

much bigger than the Sprite uh in which

## 53640:00 - 53665:00

case you have to put a lot of padding

## 53665:00 - 53695:00

around it if you want to Sprite it and

## 53695:00 - 53740:00

so this basically Sprite meat just looks

## 53740:00 - 53770:00

at all the images and applies that

## 53770:00 - 53805:00

Arcane knowledge and suggests what you

## 53805:00 - 53840:00

should Sprite so it's said well I think

## 53840:00 - 53870:00

you could Sprite all of these together

## 53870:00 - 53905:00

and you just click on make Sprite and it

## 53905:00 - 53940:00

actually goes off to this guy Jared her

## 53940:00 - 53975:00

his website I teamed up with him and it

## 53975:00 - 54005:00

takes all those images and combines them

## 54005:00 - 54045:00

all and Returns the Sprite image to me

## 54045:00 - 54090:00

and then I actually changed all the CSS

## 54090:00 - 54110:00

in the page that you're looking at right

## 54110:00 - 54165:00

now to use this Sprite image so here's

## 54165:00 - 54190:00

the Sprite you could actually download

## 54190:00 - 54245:00

and save it and you can say export CSS

## 54245:00 - 54290:00

and it doesn't like generate your new

## 54290:00 - 54325:00

stylesheets but it says well you'll have

## 54325:00 - 54365:00

to change this rule to say background

## 54365:00 - 54405:00

blah blah blah blah blah um so it gives

## 54405:00 - 54440:00

you some tips now in this case we redu

## 54440:00 - 54495:00

seven requests but we increased by 21k

## 54495:00 - 54545:00

so typically that's probably actually a

## 54545:00 - 54600:00

good tradeoff um but I you know it might

## 54600:00 - 54630:00

be more than I would want to do and

## 54630:00 - 54685:00

usually there's like one image that is

## 54685:00 - 54740:00

kind of uh increasing the you know uh

## 54740:00 - 54770:00

color map or something like that and I

## 54770:00 - 54805:00

think I looked at this and concluded it

## 54805:00 - 54865:00

was probably this one

## 54865:00 - 54900:00

so oh

## 54900:00 - 54985:00

yeah he does performance and drag and

## 54985:00 - 55045:00

drop and I think I wrote that myself too

## 55045:00 - 55090:00

um so now we can try this

## 55090:00 - 55145:00

one and I think we'll get so instead of

## 55145:00 - 55185:00

saving seven requests we'll save six but

## 55185:00 - 55225:00

I think we get a smaller increase did I

## 55225:00 - 55285:00

click on it

## 55285:00 - 55340:00

f well it's the image Generation stuff

## 55340:00 - 55385:00

that's

## 55385:00 - 55455:00

Jared that was a joke right so yeah so

## 55455:00 - 55495:00

it's only 13k more for and save six

## 55495:00 - 55525:00

requests so that's pretty good so you

## 55525:00 - 55545:00

know I don't know if it actually makes

## 55545:00 - 55585:00

sense for you to do that but anyway it's

## 55585:00 - 55645:00

a nice tool to play with um and actually

## 55645:00 - 55670:00

people it's all open source so people

## 55670:00 - 55690:00

have taken this and they have actually

## 55690:00 - 55740:00

used the code and the logic to put into

## 55740:00 - 55770:00

automatic Sprite

## 55770:00 - 55835:00

generators

## 55835:00 - 55910:00

um so that's another way that you can uh

## 55910:00 - 55950:00

reduce the

## 55950:00 - 55995:00

uh improve performance without reducing

## 55995:00 - 56035:00

the actual content on the page yeah so

## 56035:00 - 56055:00

there's the

## 56055:00 - 56100:00

example so I'm not going to talk about

## 56100:00 - 56130:00

any of others of these unless there's

## 56130:00 - 56190:00

questions about

## 56190:00 - 56255:00

them number seven avoid CSS

## 56255:00 - 56290:00

Expressions well this so I wrote this

## 56290:00 - 56330:00

book in 2007 when IE was still pretty

## 56330:00 - 56370:00

big and ie supported something called

## 56370:00 - 56405:00

CSS Expressions where you could actually

## 56405:00 - 56455:00

embed JavaScript code in inside of a CSS

## 56455:00 - 56540:00

rule well it turned out that um uh like

## 56540:00 - 56585:00

you could put something you could have

## 56585:00 - 56630:00

like uh uh something that would

## 56630:00 - 56710:00

do um something to a style on a hover

## 56710:00 - 56740:00

and then when you move the mouse over

## 56740:00 - 56790:00

the page that JavaScript would execute

## 56790:00 - 56870:00

about 50,000 times oh right and so

## 56870:00 - 56890:00

people would see this where they were

## 56890:00 - 56945:00

using CSS expressions and other browsers

## 56945:00 - 56975:00

just ignore it but in IE their Pages

## 56975:00 - 57025:00

would just freeze and so you know it's

## 57025:00 - 57055:00

don't use them or if you have to use

## 57055:00 - 57080:00

them there are ways that you can

## 57080:00 - 57140:00

actually um add them but then have them

## 57140:00 - 57205:00

be uh you know uh reflexive and and

## 57205:00 - 57235:00

remove themselves if when they're not

## 57235:00 - 57360:00

needed and make themselves faster

## 57360:00 - 57400:00

yeah no there's not really any secrets

## 57400:00 - 57450:00

the main one is if you look at your site

## 57450:00 - 57505:00

um I think web page tests will tell you

## 57505:00 - 57565:00

like people sometimes create gratuitous

## 57565:00 - 57580:00

uh

## 57580:00 - 57620:00

subdomains and you know if you look at

## 57620:00 - 57640:00

your page and you have like two

## 57640:00 - 57670:00

subdomains that only have one request

## 57670:00 - 57705:00

each like could you maybe move those

## 57705:00 - 57735:00

over to a domain that you're already

## 57735:00 - 57765:00

using we actually do that a lot at

## 57765:00 - 57810:00

Google um I would find cases where we

## 57810:00 - 57830:00

had something on something else it's

## 57830:00 - 57875:00

like yeah you know can you just maybe

## 57875:00 - 57900:00

server from this other one well we want

## 57900:00 - 57925:00

to keep that separate and track the LW

## 57925:00 - 57975:00

like go a new DNS lookup really do we

## 57975:00 - 58040:00

need that um

## 58040:00 - 58080:00

so uh I can't I don't think there are

## 58080:00 - 58120:00

any other like Silver Bullet Secrets

## 58120:00 - 58240:00

there yeah

## 58240:00 - 58305:00

the yeah so that's a good segue

## 58305:00 - 58365:00

because

## 58365:00 - 58430:00

uh yeah um to the second book and on

## 58430:00 - 58470:00

this this one I had a lot of great

## 58470:00 - 58525:00

contributors but one of the ones I wrote

## 58525:00 - 58575:00

was um domain

## 58575:00 - 58600:00

Shing

## 58600:00 - 58690:00

uh Shing dominant domains so um yeah

## 58690:00 - 58735:00

exactly what you were saying is and and

## 58735:00 - 58760:00

we'll have some examples of this from

## 58760:00 - 58810:00

the URLs that were submitted if you know

## 58810:00 - 58865:00

so that you know as we discovered before

## 58865:00 - 58925:00

a browser will only download six

## 58925:00 - 58970:00

requests in parallel for a given host

## 58970:00 - 59020:00

name it's not IP address it's host name

## 59020:00 - 59075:00

based so you can create you know four C

## 59075:00 - 59140:00

names to the same web server uh WW1 dot

## 59140:00 - 59245:00

W2 W3 W4 Dot and if you have um 24

## 59245:00 - 59300:00

images put the first six on domain one 2

## 59300:00 - 59345:00

six third six and all 24 will download

## 59345:00 - 59395:00

in parallel right now maybe that's a

## 59395:00 - 59440:00

good thing maybe that's a bad thing

## 59440:00 - 59475:00

um and it turns out most studies you

## 59475:00 - 59510:00

know um that I did and that other people

## 59510:00 - 59550:00

have done say it's best not to Shard

## 59550:00 - 59585:00

across more than two domains but it

## 59585:00 - 59650:00

depends on how many resources you have

## 59650:00 - 59670:00

um

## 59670:00 - 59715:00

certainly I think it if you have more

## 59715:00 - 59765:00

than 20 resources on one domain and you

## 59765:00 - 59800:00

have a typical page with 50 to 100

## 59800:00 - 59835:00

resources it's probably a good idea to

## 59835:00 - 59875:00

Shard those across two

## 59875:00 - 59920:00

domains so in that case you now the

## 59920:00 - 59965:00

downside of doing that is um there's two

## 59965:00 - 59995:00

main downsides you have an extra DNS

## 59995:00 - 60025:00

look up and then you're using more

## 60025:00 - 60060:00

connection and you know if we know about

## 60060:00 - 60105:00

the congestion window it gradually gets

## 60105:00 - 60135:00

bigger as the browser has more

## 60135:00 - 60170:00

experience with this connection it will

## 60170:00 - 60215:00

allow data uh larger amounts of data to

## 60215:00 - 60290:00

come down and so um if if you keep

## 60290:00 - 60320:00

reusing the same connection it gets

## 60320:00 - 60345:00

smarter and smarter and smarter and more

## 60345:00 - 60365:00

more efficient assuming you don't have a

## 60365:00 - 60455:00

lot of uh packet loss um but if you use

## 60455:00 - 60495:00

more connections that learning curve has

## 60495:00 - 60530:00

to be endured by every connection it's

## 60530:00 - 60570:00

not like this connection to dubdub du.

## 60570:00 - 60625:00

fubar.com has a huge congestion window

## 60625:00 - 60650:00

that it learned so let's give that

## 60650:00 - 60670:00

congestion window to all the other

## 60670:00 - 60710:00

connections TCP doesn't work that way so

## 60710:00 - 60760:00

those are the two main

## 60760:00 - 60815:00

downsides okay so this book was much

## 60815:00 - 60920:00

more targeted at web 20 stuff and um so

## 60920:00 - 60940:00

when I'm out of

## 60940:00 - 61000:00

bowling parties and stuff like that um

## 61000:00 - 61040:00

typically people I I actually don't have

## 61040:00 - 61075:00

any social life all I do is talk about

## 61075:00 - 61120:00

performance all the time and so I stand

## 61120:00 - 61145:00

around and people eventually come up and

## 61145:00 - 61175:00

ask me something about performance like

## 61175:00 - 61215:00

you know what's the main thing I can do

## 61215:00 - 61260:00

to make my website slower um like I

## 61260:00 - 61285:00

would love to or actually it goes more

## 61285:00 - 61330:00

like this I would love it if I could get

## 61330:00 - 61375:00

some of your time to look at our website

## 61375:00 - 61395:00

and tell us what we can do to make it

## 61395:00 - 61425:00

faster and I always say the same thing

## 61425:00 - 61455:00

oh oh I don't have to look at your

## 61455:00 - 61490:00

website I can tell you right now the

## 61490:00 - 61555:00

thing that's making your website slow is

## 61555:00 - 61595:00

Javascript and they go how do you know

## 61595:00 - 61620:00

that I go do you use JavaScript on your

## 61620:00 - 61665:00

website yes that's how I

## 61665:00 - 61705:00

know right

## 61705:00 - 61750:00

and um so this is what I alluded to

## 61750:00 - 61785:00

before is Javascript bite forbite is the

## 61785:00 - 61840:00

most painful thing to download so this

## 61840:00 - 61890:00

is how uh so why is that it's because

## 61890:00 - 61925:00

scripts block so this is the old world

## 61925:00 - 61970:00

right this is the old world it turned

## 61970:00 - 62015:00

out and with kazillion I was able to

## 62015:00 - 62065:00

figure this out that uh so here's an

## 62065:00 - 62125:00

HTML document script script uh image

## 62125:00 - 62155:00

stylesheet

## 62155:00 - 62215:00

iframe it turns out in the old

## 62215:00 - 62280:00

days uh when the browser hit a script

## 62280:00 - 62330:00

tag for an external script it would stop

## 62330:00 - 62370:00

doing everything else it would stop

## 62370:00 - 62410:00

parsing the HML document it would stop

## 62410:00 - 62440:00

all other downloads

## 62440:00 - 62485:00

until it had downloaded this script and

## 62485:00 - 62520:00

parsed and executed it I didn't show you

## 62520:00 - 62550:00

in kazillion but you for scripts you can

## 62550:00 - 62595:00

say how long should I take the download

## 62595:00 - 62635:00

and how long should I take to uh for the

## 62635:00 - 62675:00

script to have execution time I just go

## 62675:00 - 62740:00

into a a while loop um and so here for

## 62740:00 - 62770:00

each of these scripts I said two seconds

## 62770:00 - 62810:00

to download two seconds to execute and

## 62810:00 - 62845:00

then these Styles sheet image and iframe

## 62845:00 - 62880:00

were each one second and so in these

## 62880:00 - 62910:00

browsers this is what the waterfall

## 62910:00 - 62940:00

chart looks like

## 62940:00 - 62975:00

document the first script stop

## 62975:00 - 62990:00

everything

## 62990:00 - 63035:00

else par download pars and execute

## 63035:00 - 63070:00

second script stop everything else

## 63070:00 - 63110:00

download Parson execute um and then

## 63110:00 - 63140:00

download these other things and guess

## 63140:00 - 63170:00

what it's not just that it blocks other

## 63170:00 - 63200:00

downloads it block downloads it blocks

## 63200:00 - 63235:00

rendering and this is still something

## 63235:00 - 63285:00

that's true today the browser will not

## 63285:00 - 63345:00

render any Dom element that's below a

## 63345:00 - 63390:00

script tag until that script tag whether

## 63390:00 - 63430:00

it's inline or external has been

## 63430:00 - 63460:00

downloaded in the case of external and

## 63460:00 - 63500:00

pared and executed well guess what most

## 63500:00 - 63545:00

people put their script tags in the head

## 63545:00 - 63580:00

which means everything in the Dom

## 63580:00 - 63635:00

element below that like the body will be

## 63635:00 - 63670:00

blocked from rendering so your entire

## 63670:00 - 63710:00

page is blocked from rendering until

## 63710:00 - 63760:00

this has happened right that's why it's

## 63760:00 - 63810:00

so painful and this really doesn't make

## 63810:00 - 63860:00

sense right be so why did browser

## 63860:00 - 63925:00

browsers do this it's because browsers

## 63925:00 - 63990:00

are built by humans that have lives

## 63990:00 - 64045:00

outside of work wives and kids and

## 64045:00 - 64095:00

social bowling

## 64095:00 - 64150:00

events oh that was

## 64150:00 - 64235:00

yeah um and so they said well you know

## 64235:00 - 64270:00

if we just download and execute

## 64270:00 - 64295:00

JavaScript willy-nilly we're going to

## 64295:00 - 64320:00

get these race conditions we're going to

## 64320:00 - 64365:00

get undefined symbol errors if this

## 64365:00 - 64415:00

script depends on this script but it

## 64415:00 - 64490:00

gets part first so we want to very very

## 64490:00 - 64515:00

rigidly

## 64515:00 - 64560:00

enforce JavaScript will be executed in

## 64560:00 - 64595:00

the order that it's declared in the page

## 64595:00 - 64650:00

okay I totally get that but why don't

## 64650:00 - 64675:00

you download them both in parallel I

## 64675:00 - 64705:00

mean while this guy was taking two

## 64705:00 - 64725:00

seconds to download you could have

## 64725:00 - 64760:00

downloaded this one and maybe this one

## 64760:00 - 64785:00

only took 100 milliseconds well just

## 64785:00 - 64825:00

don't parse and execute it right just

## 64825:00 - 64860:00

take the btes and save them and then

## 64860:00 - 64890:00

when this one is finally done pars and

## 64890:00 - 64935:00

execute this one and so like

## 64935:00 - 64955:00

I actually told the browsers that and

## 64955:00 - 65015:00

they did it I think it's the most

## 65015:00 - 65075:00

important performance change all the V8

## 65075:00 - 65115:00

and you know jvm stuff I think this the

## 65115:00 - 65155:00

most important change that browsers have

## 65155:00 - 65205:00

made in the last five years so now on

## 65205:00 - 65235:00

all the new

## 65235:00 - 65285:00

browsers they will download scripts in

## 65285:00 - 65315:00

parallel with each other and with other

## 65315:00 - 65395:00

stuff IE 89 this was 6 to7

## 65395:00 - 65435:00

i89 um

## 65435:00 - 65460:00

actually will download scripts in

## 65460:00 - 65485:00

parallel with each other but we'll still

## 65485:00 - 65525:00

block everything else IE10 finally fixed

## 65525:00 - 65590:00

that and so and they take care of the

## 65590:00 - 65635:00

issue of ensuring that even though these

## 65635:00 - 65665:00

two got done at the same time even if

## 65665:00 - 65700:00

this one got done a little earlier it's

## 65700:00 - 65725:00

not going to parse and executed until

## 65725:00 - 65750:00

this one is done so what we see here is

## 65750:00 - 65795:00

we see two seconds to download and uh to

## 65795:00 - 65825:00

download this one only took a second

## 65825:00 - 65860:00

it's the stylesheet 2 seconds to

## 65860:00 - 65905:00

download 2 seconds to parse and execute

## 65905:00 - 65935:00

the first one 2 seconds to parse execute

## 65935:00 - 65980:00

the second one and then we download the

## 65980:00 - 66035:00

rest and it's not until this point right

## 66035:00 - 66075:00

here um that we can do rendering so

## 66075:00 - 66110:00

rendering is still blocked but we're

## 66110:00 - 66145:00

going to get to that point these aren't

## 66145:00 - 66175:00

at the same scale or actually maybe they

## 66175:00 - 66230:00

are so we actually start rendering at uh

## 66230:00 - 66290:00

6 seconds instead of 8 seconds right so

## 66290:00 - 66335:00

and the total download time is 7 seconds

## 66335:00 - 66380:00

but we can see this still isn't

## 66380:00 - 66420:00

perfect why didn't these get downloaded

## 66420:00 - 66475:00

in parallel as well and again this is

## 66475:00 - 66500:00

actually kind of I should look and

## 66500:00 - 66545:00

update this chart um it's just built by

## 66545:00 - 66575:00

humans right and so like one of the

## 66575:00 - 66610:00

browsers you know they so what they do

## 66610:00 - 66645:00

is they all added this thing called uh

## 66645:00 - 66685:00

look ahead parsing speculative parsing

## 66685:00 - 66720:00

where they stop

## 66720:00 - 66760:00

parsing um and rendering dime elements

## 66760:00 - 66790:00

once they hit this script tag but

## 66790:00 - 66820:00

they'll do look ahead parsing where they

## 66820:00 - 66855:00

just look a little bit ahead and they

## 66855:00 - 66885:00

see if there's any other things like the

## 66885:00 - 66925:00

script IMG

## 66925:00 - 66985:00

um link tag and if so it will say oh

## 66985:00 - 67005:00

well let's download these things in

## 67005:00 - 67030:00

parallel and we have to deal with them

## 67030:00 - 67065:00

maybe a little carefully until this one

## 67065:00 - 67105:00

is done but let's get the Download Pain

## 67105:00 - 67140:00

out of the way and they forgot to add

## 67140:00 - 67175:00

iframe and so you know I submitted a bug

## 67175:00 - 67200:00

and they're like oh yeah we forgot to

## 67200:00 - 67225:00

add iframe to that list of tags to look

## 67225:00 - 67275:00

for or they only look ahead a certain

## 67275:00 - 67320:00

number of bytes um or maybe it's your

## 67320:00 - 67360:00

fault maybe it took a long time in the

## 67360:00 - 67405:00

HTML document you got these bites down

## 67405:00 - 67430:00

pretty fast and these took took a long

## 67430:00 - 67460:00

time and before these bites came down in

## 67460:00 - 67510:00

the HTML document it had already started

## 67510:00 - 67535:00

and it wasn't going to kick off any new

## 67535:00 - 67575:00

downloads at that point but anyway we're

## 67575:00 - 67615:00

a lot better off than we were before but

## 67615:00 - 67645:00

it's still not as optimal as we would

## 67645:00 - 67690:00

like especially IE8 and9 not downloading

## 67690:00 - 67725:00

images in parallel with scripts is seems

## 67725:00 - 67780:00

like a huge Miss um but JavaScript is

## 67780:00 - 67805:00

still a big pain if we look at the Alexa

## 67805:00 - 67850:00

toop 100 I did this little study um

## 67850:00 - 67895:00

where I disabled JavaScript and if I

## 67895:00 - 67950:00

disable JavaScript it cuts 31% off the

## 67950:00 - 67985:00

window.onload time and it's hard to

## 67985:00 - 68005:00

think of something that would be a

## 68005:00 - 68055:00

bigger Factor than that um so JavaScript

## 68055:00 - 68105:00

is still bite forbite the biggest pain

## 68105:00 - 68165:00

and it's growing growing growing right

## 68165:00 - 68225:00

over time so we got to figure out a way

## 68225:00 - 68275:00

to uh get our arms around this

## 68275:00 - 68315:00

problem uh one of the rules in the

## 68315:00 - 68350:00

second book was um to split the initial

## 68350:00 - 68395:00

payload so here we look at some top

## 68395:00 - 68445:00

sites how much JavaScript they have um

## 68445:00 - 68475:00

and what percentage of the functions in

## 68475:00 - 68515:00

this JavaScript are actually executed

## 68515:00 - 68550:00

before the onload event and it turns out

## 68550:00 - 68575:00

on average it's less than

## 68575:00 - 68625:00

30% so why are they downloading

## 68625:00 - 68660:00

JavaScript that's not executed well it

## 68660:00 - 68695:00

could be like error handling and we just

## 68695:00 - 68735:00

didn't trip on the error um but it's

## 68735:00 - 68775:00

probably mostly dhtml things like if you

## 68775:00 - 68810:00

click on the compose button or address

## 68810:00 - 68845:00

book it's going to pop up a div and let

## 68845:00 - 68875:00

you type stuff or show you a list of

## 68875:00 - 68905:00

things or stuff like that you know I

## 68905:00 - 68955:00

love dhtml but if it's if really it's

## 68955:00 - 68995:00

not part of rendering the initial page

## 68995:00 - 69050:00

separate that code out and lazy load it

## 69050:00 - 69085:00

like after the initial page is rendered

## 69085:00 - 69115:00

maybe in the window onload event

## 69115:00 - 69150:00

download the rest of that JavaScript and

## 69150:00 - 69165:00

you're going to have to be a little

## 69165:00 - 69200:00

careful like you wouldn't attach the

## 69200:00 - 69250:00

onload Handler to a compose button until

## 69250:00 - 69290:00

that ja lazy loaded JavaScript was done

## 69290:00 - 69315:00

the lazy loaded JavaScript would do it

## 69315:00 - 69355:00

itself so split the initial payload

## 69355:00 - 69385:00

between what's needed to render the page

## 69385:00 - 69425:00

and everything else defer everything

## 69425:00 - 69480:00

else um page speed um that's actually

## 69480:00 - 69525:00

one word now got to update my slide

## 69525:00 - 69565:00

major branding change it's going to make

## 69565:00 - 69585:00

a big

## 69585:00 - 69650:00

difference yeah um my my slides will be

## 69650:00 - 69695:00

so much faster uh and there's a tool

## 69695:00 - 69720:00

from dilato that will do it

## 69720:00 - 69750:00

automatically for you

## 69750:00 - 69815:00

but it's not perfect um but you're still

## 69815:00 - 69835:00

going to have scripts that you're going

## 69835:00 - 69870:00

to load as part of the page and so you

## 69870:00 - 69900:00

want to do that without blocking the

## 69900:00 - 69955:00

page so back in 1995 we typically put

## 69955:00 - 69995:00

our scripts at the top browser blocked

## 69995:00 - 70045:00

this would block everything in the body

## 70045:00 - 70095:00

um they were downloaded sequentially it

## 70095:00 - 70105:00

blocks

## 70105:00 - 70165:00

rendering um in 2007 in my book first

## 70165:00 - 70200:00

book I said uh move scripts to the

## 70200:00 - 70235:00

bottom right and this is pretty good

## 70235:00 - 70270:00

advice because it means it's not

## 70270:00 - 70305:00

blocking right if this takes a long time

## 70305:00 - 70330:00

there's no Dom elements that are blocked

## 70330:00 - 70380:00

from rendering um so it doesn't and it

## 70380:00 - 70410:00

doesn't block other downloads in the old

## 70410:00 - 70450:00

browsers there's nothing below this so

## 70450:00 - 70480:00

it can't block other images and scripts

## 70480:00 - 70520:00

from downloading um but they still

## 70520:00 - 70570:00

downloaded sequentially in I6 and 7 uh

## 70570:00 - 70600:00

and even today that would happen in

## 70600:00 - 70665:00

those older browsers and um once this

## 70665:00 - 70710:00

JavaScript arrives suppose it's 300K of

## 70710:00 - 70750:00

JavaScript um is going to block the UI

## 70750:00 - 70795:00

thread right and so if the UI thread was

## 70795:00 - 70830:00

still rendering the page rendering could

## 70830:00 - 70870:00

potentially be blocked so we can

## 70870:00 - 70895:00

actually do better than that so the

## 70895:00 - 70940:00

second book talked about loading scripts

## 70940:00 - 70980:00

asynchronously um and this is a pattern

## 70980:00 - 71015:00

from my book that now has been

## 71015:00 - 71060:00

popularized greatly by Google analytics

## 71060:00 - 71100:00

where you create a script element uh you

## 71100:00 - 71135:00

set it source and then you add it to the

## 71135:00 - 71175:00

head a pench child or in do insert

## 71175:00 - 71230:00

before um and this won't block any other

## 71230:00 - 71260:00

downloads even if you put it in the top

## 71260:00 - 71280:00

of the page it won't block any other

## 71280:00 - 71335:00

downloads across all browsers um it will

## 71335:00 - 71360:00

download in parallel with everything

## 71360:00 - 71395:00

else even in IE it will download in

## 71395:00 - 71450:00

parallel with images um but when the

## 71450:00 - 71500:00

payload arrives if it's 300K it is going

## 71500:00 - 71530:00

to block the UI thread right because

## 71530:00 - 71565:00

there's only one thread that the browser

## 71565:00 - 71630:00

can use um so we can even get around

## 71630:00 - 71660:00

that how can we possibly get around that

## 71660:00 - 71695:00

last red one this is a hack from a

## 71695:00 - 71745:00

couple years ago uh that Gmail mobile

## 71745:00 - 71785:00

talked about so they had this challenge

## 71785:00 - 71810:00

where

## 71810:00 - 71860:00

um uh you're running Gmail on here and

## 71860:00 - 71910:00

let's say there's you know 120k for the

## 71910:00 - 71950:00

JavaScript for the compos div that pops

## 71950:00 - 71980:00

up and you don't need that to render the

## 71980:00 - 72005:00

page so we're going to Lazy load it

## 72005:00 - 72035:00

right well one thing you could do is you

## 72035:00 - 72060:00

could wait till the user clicks on the

## 72060:00 - 72105:00

compose button and then download 120k

## 72105:00 - 72145:00

Over the mobile network that's not a

## 72145:00 - 72170:00

great idea right the user clicked on

## 72170:00 - 72190:00

compose and they're waiting waiting

## 72190:00 - 72215:00

waiting okay well let's do it in the

## 72215:00 - 72245:00

background how do we do that okay in the

## 72245:00 - 72290:00

window onload event we'll download 120k

## 72290:00 - 72325:00

of JavaScript so the user hasn't clicked

## 72325:00 - 72380:00

on compose and they're trying to

## 72380:00 - 72420:00

interact with the page and they're it

## 72420:00 - 72475:00

doesn't hear their click because it's

## 72475:00 - 72520:00

parsing 120k of JavaScript which might

## 72520:00 - 72560:00

not be a lot on the desktop on a small

## 72560:00 - 72585:00

device it can be it can take a fair

## 72585:00 - 72620:00

amount of time so we're blocking the UI

## 72620:00 - 72655:00

thread for this JavaScript that's being

## 72655:00 - 72680:00

parti and executed that the user may

## 72680:00 - 72735:00

never want so instead what they do is

## 72735:00 - 72770:00

they download the JavaScript and comment

## 72770:00 - 72820:00

out the code so it's not par and

## 72820:00 - 72885:00

executed but the bytes are on the device

## 72885:00 - 72910:00

right the bytes have been downloaded in

## 72910:00 - 72945:00

the back ground but I have not blocked

## 72945:00 - 72995:00

the UI thread to Parson execute and so

## 72995:00 - 73025:00

when the user clicks on the compose

## 73025:00 - 73085:00

button you get this scripto element get

## 73085:00 - 73125:00

the doc text property remove to comments

## 73125:00 - 73140:00

and

## 73140:00 - 73205:00

eval oh my God right so eval is just as

## 73205:00 - 73250:00

fast as if you had a normal script block

## 73250:00 - 73310:00

right and eval is bad for security if

## 73310:00 - 73335:00

it's JavaScript that you don't know

## 73335:00 - 73370:00

what's in it but you do this for your

## 73370:00 - 73405:00

code not for an advertiser's code you do

## 73405:00 - 73445:00

this for your code code and um it's

## 73445:00 - 73465:00

perfectly fine so it's good for

## 73465:00 - 73510:00

performance it's safe for security and

## 73510:00 - 73540:00

it's a better user experience when I

## 73540:00 - 73575:00

click on compose and there's a little

## 73575:00 - 73630:00

bit of a delay I'm not that surprised

## 73630:00 - 73675:00

because I asked for something and the

## 73675:00 - 73695:00

delay is not that long because I'm not

## 73695:00 - 73715:00

waiting for the download I'm just

## 73715:00 - 73745:00

waiting for the Parson

## 73745:00 - 73780:00

execute so that's I think a really

## 73780:00 - 73815:00

really great uh

## 73815:00 - 73875:00

hack um that's quite

## 73875:00 - 73925:00

yeah uh but it's kind of hard to so I

## 73925:00 - 73970:00

wrote this uh JavaScript library called

## 73970:00 - 74010:00

control JS there are a lot of script

## 74010:00 - 74045:00

loaders and I just thought none of them

## 74045:00 - 74075:00

were doing as good of a job as they

## 74075:00 - 74105:00

could so I actually wrote this as a

## 74105:00 - 74130:00

proof of concept but it turns out it's

## 74130:00 - 74180:00

been like Washington Post is using it uh

## 74180:00 - 74210:00

I'm pretty sure New Relic and a couple

## 74210:00 - 74250:00

other of these web accelerator companies

## 74250:00 - 74290:00

use it um and I took a different

## 74290:00 - 74330:00

approach as I said let's do it in markup

## 74330:00 - 74375:00

so you know if you change the type um

## 74375:00 - 74405:00

then the browser won't try to parse and

## 74405:00 - 74425:00

execute it

## 74425:00 - 74480:00

and uh so you can um do this you can

## 74480:00 - 74525:00

change your markup to say stuff like

## 74525:00 - 74570:00

that and it works for external scripts

## 74570:00 - 74605:00

and inline scripts no other loader that

## 74605:00 - 74645:00

I know of does that and so it makes sure

## 74645:00 - 74670:00

and and yet this is a very typical

## 74670:00 - 74695:00

pattern we going to download some

## 74695:00 - 74730:00

JavaScript in a library and then we're

## 74730:00 - 74750:00

going to have some inline code that

## 74750:00 - 74785:00

calls it and no other asynchronous

## 74785:00 - 74810:00

script loader supports that as far as I

## 74810:00 - 74835:00

know last time I

## 74835:00 - 74865:00

checked the other thing that's really

## 74865:00 - 74915:00

cool about control JS is you can

## 74915:00 - 74955:00

download you can load itself the control

## 74955:00 - 75000:00

JS Library asynchronously so the whole

## 75000:00 - 75035:00

thing will work asynchronously and not

## 75035:00 - 75080:00

block the page and then um if you want

## 75080:00 - 75140:00

to do that Gmail hack you just say um

## 75140:00 - 75180:00

execute false and it will download it

## 75180:00 - 75220:00

and not execute it and then later you

## 75220:00 - 75280:00

can just um get hold of that uh uh

## 75280:00 - 75325:00

element or no you just have the URL and

## 75325:00 - 75355:00

say execute script and it will find this

## 75355:00 - 75385:00

Dom element and it doesn't do quite the

## 75385:00 - 75425:00

hack that um they did but it's something

## 75425:00 - 75460:00

similar um so this is a nice little

## 75460:00 - 75505:00

Library more to look at as an example um

## 75505:00 - 75535:00

but really to push the envelope and now

## 75535:00 - 75575:00

other people have started doing this um

## 75575:00 - 75600:00

especially the people that have adopted

## 75600:00 - 75640:00

the library and then let's talk about

## 75640:00 - 75710:00

mobile really quick and running out time

## 75710:00 - 75755:00

what time is it oh wow I'm way past okay

## 75755:00 - 75800:00

uh you can do Sprites data URLs but also

## 75800:00 - 75825:00

mobile browsers are more up to date so

## 75825:00 - 75885:00

you can use CSS stuff canvas SVG um you

## 75885:00 - 75935:00

want to images take 60 % of the btes on

## 75935:00 - 75985:00

web pages and you don't want to download

## 75985:00 - 76020:00

your desktop images to a browser so what

## 76020:00 - 76060:00

do you do create multiple sizes of your

## 76060:00 - 76090:00

images that's a huge pain in the neck so

## 76090:00 - 76120:00

there's this whole responsive images

## 76120:00 - 76160:00

problem that the picture and Source set

## 76160:00 - 76195:00

proposals are trying to solve um but

## 76195:00 - 76220:00

there are some other Solutions out there

## 76220:00 - 76255:00

I really like ca iio Source you just

## 76255:00 - 76295:00

take your image and prefix it with this

## 76295:00 - 76325:00

and they will do user agent sniffing and

## 76325:00 - 76370:00

resize the image for you

## 76370:00 - 76405:00

automatically and you can buy it from

## 76405:00 - 76430:00

them if you want want or you could build

## 76430:00 - 76465:00

something very similar um or you could

## 76465:00 - 76495:00

look at a client side solution I don't

## 76495:00 - 76530:00

like these as

## 76530:00 - 76610:00

much here it is um because images are

## 76610:00 - 76645:00

really the most important thing to

## 76645:00 - 76690:00

download because they're visual CSS and

## 76690:00 - 76730:00

JavaScript aren't visual in and of

## 76730:00 - 76770:00

themselves but the images are and

## 76770:00 - 76795:00

they're usually one of the primary

## 76795:00 - 76825:00

visual elements on the page and so we

## 76825:00 - 76860:00

really want to get images in front of

## 76860:00 - 76895:00

the page as quickly as possible but I

## 76895:00 - 76920:00

say that there are less important bite

## 76920:00 - 76955:00

forbite than JavaScript and stylesheets

## 76955:00 - 76990:00

just because JavaScript and stylesheets

## 76990:00 - 77040:00

block images so if we can get images

## 77040:00 - 77085:00

down faster that's really important uh

## 77085:00 - 77130:00

these client side techniques actually

## 77130:00 - 77170:00

delay how early you can get the images

## 77170:00 - 77190:00

to

## 77190:00 - 77235:00

download so I don't like them very much

## 77235:00 - 77265:00

but I do like the background photo like

## 77265:00 - 77300:00

images different sizes just like Russian

## 77300:00 - 77360:00

dolls or if we talk about offline app

## 77360:00 - 77390:00

cache why are we in a desert because

## 77390:00 - 77420:00

often the reception in the middle of a

## 77420:00 - 77515:00

desert is poor you might need to work

## 77515:00 - 77565:00

offline I've got a much better jokes

## 77565:00 - 77600:00

toward the

## 77600:00 - 77670:00

end keep waiting uh how many people use

## 77670:00 - 77705:00

appach yeah it's kind of hard to work

## 77705:00 - 77745:00

with um you specify the Manifest

## 77745:00 - 77795:00

attribute specify your appcache file it

## 77795:00 - 77840:00

has to be formatted like this cash means

## 77840:00 - 77870:00

you can save this in the cash Network

## 77870:00 - 77905:00

means never Sav in the cash fallback

## 77905:00 - 77930:00

means if the the users online use this

## 77930:00 - 77960:00

one if they're offline use this one like

## 77960:00 - 77990:00

you wouldn't show want to show them an a

## 77990:00 - 78065:00

login form if they're offline um and it

## 78065:00 - 78115:00

has to have a special excuse me content

## 78115:00 - 78170:00

type um but it's really hard to work

## 78170:00 - 78220:00

with uh if you specify the Manifest

## 78220:00 - 78255:00

attribute the HTML document is also

## 78255:00 - 78290:00

saved into the app cache so it won't get

## 78290:00 - 78330:00

updated every time um if anything in

## 78330:00 - 78375:00

that manifest file 404s then nothing is

## 78375:00 - 78420:00

saved to appcache you're limited to uh

## 78420:00 - 78495:00

about five Meg um if you change a script

## 78495:00 - 78560:00

or image you have to also uh modify not

## 78560:00 - 78620:00

just touch but modify the uh manifest

## 78620:00 - 78670:00

file um and if you change if you do both

## 78670:00 - 78710:00

of those modify an image and a manifest

## 78710:00 - 78750:00

file um the user still won't see that

## 78750:00 - 78775:00

update until the second time they load

## 78775:00 - 78805:00

the app and I don't have time to go into

## 78805:00 - 78860:00

that but that threw me off for a day on

## 78860:00 - 78920:00

my first appcash app um an alternative

## 78920:00 - 78950:00

that's much simpler as local storage get

## 78950:00 - 78995:00

item set item and um this was really

## 78995:00 - 79040:00

meant as maybe uh alternative for local

## 79040:00 - 79105:00

storage over cookies but um it still

## 79105:00 - 79145:00

supports fmeg and people are using it as

## 79145:00 - 79195:00

a cache this was a study I did uh where

## 79195:00 - 79220:00

both Google search and Bing were doing

## 79220:00 - 79285:00

the same thing rather than put their for

## 79285:00 - 79325:00

mobile rather than put um scripts and

## 79325:00 - 79370:00

stylesheets in their pages in the first

## 79370:00 - 79420:00

time you did a search they would embed

## 79420:00 - 79455:00

um all of these script and and style

## 79455:00 - 79490:00

blocks but then at the end they would

## 79490:00 - 79515:00

have JavaScript that would save those

## 79515:00 - 79545:00

blocks to local storage so this is

## 79545:00 - 79580:00

actually a key in local storage I think

## 79580:00 - 79620:00

this is Google's implementation and they

## 79620:00 - 79680:00

would also set a key a cookie that would

## 79680:00 - 79715:00

list all the modules that had been saved

## 79715:00 - 79750:00

to local storage so now you do another

## 79750:00 - 79810:00

search and the server says oh well um

## 79810:00 - 79835:00

here's the search results I need to give

## 79835:00 - 79870:00

you this module of JavaScript but first

## 79870:00 - 79890:00

let me look at your cookie oh you

## 79890:00 - 79915:00

already have that one then I don't need

## 79915:00 - 79940:00

to give it to you and you need this

## 79940:00 - 79975:00

module of CSS oh it's already in your

## 79975:00 - 80005:00

cookie I don't need to give it to you

## 80005:00 - 80055:00

and this changes the size of the Google

## 80055:00 - 80115:00

or B search results by about 90% goes

## 80115:00 - 80160:00

from about 100K to 10K because it can

## 80160:00 - 80200:00

just read these out of local storage

## 80200:00 - 80285:00

rather than um uh downloading them and

## 80285:00 - 80315:00

uh they do this on mobile because mobile

## 80315:00 - 80350:00

cache sizes are so

## 80350:00 - 80400:00

small okay uh so that took longer than I

## 80400:00 - 80455:00

expected um so what are the takeaways

## 80455:00 - 80500:00

speed matters we're all on that bus

## 80500:00 - 80520:00

right we don't want to do that yes thing

## 80520:00 - 80550:00

again

## 80550:00 - 80595:00

um make sure to track metrics and I gave

## 80595:00 - 80625:00

you some ideas of the metrics to track

## 80625:00 - 80660:00

and it's pretty easy to do rum if you're

## 80660:00 - 80695:00

using Google analytics if you want to

## 80695:00 - 80725:00

make the user experience faster you got

## 80725:00 - 80775:00

to focus on this front-end stuff um

## 80775:00 - 80805:00

there's lots of best practices out there

## 80805:00 - 80835:00

I've got a lot but other people are

## 80835:00 - 80870:00

doing similar things um and there are a

## 80870:00 - 80900:00

lot of tools I didn't go into the tools

## 80900:00 - 80950:00

here but if you download the deck

## 80950:00 - 81015:00

um uh there's about 20 slides of tools

## 81015:00 - 81045:00

that you can look at and there's you can

## 81045:00 - 81090:00

find the deck on my website um right

## 81090:00+

there okay thank you very much thank you

