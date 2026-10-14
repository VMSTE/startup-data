---
source: https://www.youtube.com/watch?v=8dgyqYHLcCI
title: An inside look at X’s Community Notes | Keith Coleman & Jay Baxter
author: Lenny's Podcast
date: 2025-02-27
views: 9010
description: |-
  Keith Coleman (VP of Product) and Jay Baxter (founding ML engineer), the minds behind Community Notes, reveal how a small, scrappy team inside Twitter/X built the most trusted crowdsourced information system on the internet—one that’s changing the way we understand truth online. What you'll learn:
  1. How Community Notes actually works—a deep dive into the groundbreaking algorithm that rewards “bridging agreement” instead of majority rule
  2. The seemingly crazy yet brilliant way this idea survived multiple CEO changes—from Jack to Parag to Elon
  3. How this project started with a dumpster fire GIF (literally)—the untold backstory of its early launch
  4. The secret to running ultra-fast, high-impact product teams—no OKRs, no Jira; just one Google Doc
  5. What Meta’s adoption of Community Notes means for the future of online (mis)information—why this open source system is becoming the industry standard

  —

  Brought to you by:
  • WorkOS—Modern identity platform for B2B SaaS, free up to 1 million MAUs: https://workos.com/lenny
  • Productboard—Make products that matter: https://www.productboard.com/lenny
  • Wix Studio—The web creation platform built for agencies: https://www.wix.com/studio?utm_source=Lennyspodcast&utm_medium=Podcastad&utm_campaign=SL

  Find the transcript at: https://www.lennysnewsletter.com/p/how-x-built-the-best-fact-checking-system-on-the-internet

  Where to find Keith Coleman:
  • X: https://x.com/kcoleman
  • LinkedIn: https://www.linkedin.com/in/keith-coleman-19b12b46/

  Where to find Jay Baxter:
  • X: https://x.com/_jaybaxter_
  • LinkedIn: https://www.linkedin.com/in/jaybaxter/
  • Website: http://jaybaxter.net/

  Where to find Lenny:
  • Newsletter: https://www.lennysnewsletter.com
  • X: https://twitter.com/lennysan
  • LinkedIn: https://www.linkedin.com/in/lennyrachitsky/

  In this episode, we cover:
  (00:00) Introduction to Community Notes
  (06:56) How the “bridging-based” algorithm works
  (13:33) The impact and scale of Community Notes
  (17:24) Understanding the note publishing threshold 
  (21:32) Challenges and philosophies
  (26:26) The effect of notes on re-sharing content
  (29:41) Origin story
  (35:46) Embracing small teams for big impact
  (40:23) The thermal project approach
  (47:47) Algorithm development and internal competitions
  (50:34) An inside look at how the team operates 
  (58:56) Working with Elon
  (01:05:30) Launching Birdwatch 
  (01:10:48) The core principles behind Community Notes
  (01:26:15) Anonymity and pseudonymity in contributions
  (01:32:17) Sustaining the project through leadership changes
  (01:37:57) Future directions for Community Notes
  (01:42:12) Final thoughts and optimism for the future

  Referenced:
  • Community Notes on X: https://x.com/CommunityNotes
  • Sign up to be a Community Notes contributor: https://communitynotes.x.com/guide/en/contributing/signing-up
  • The Making of Community Notes: https://asteriskmag.com/issues/08/the-making-of-community-notes
  • “Readers added a Community Note to this Tweet”: https://x.com/HelpfulNotes/status/1718103364792205704
  • Note-ranking algorithm: https://communitynotes.x.com/guide/en/under-the-hood/ranking-notes#matrix-factorization
  • Study: Community Notes on X could be key to curbing misinformation: https://giesbusiness.illinois.edu/news/2024/11/18/study--community-notes-on-x-could-be-key-to-curbing-misinformation
  • Study Finds X’s (Formerly Twitter’s) Community Notes Provide Accurate, Credible Answers to Vaccine Misinformation: https://qi.ucsd.edu/study-finds-xs-formerly-twitters-community-notes-provide-accurate-credible-answers-to-vaccine-misinformation/
  • Did the Roll-Out of Community Notes Reduce Engagement with Misinformation on X/Twitter?: https://dl.acm.org/doi/10.1145/3686967
  • Kayvon Beykpour on LinkedIn: https://www.linkedin.com/in/kayvz/
  • Jack Dorsey on X: https://x.com/jack
  • “Birdwatch gives me the creeps” tweet: https://x.com/elonmusk/status/1589454464611540992
  • Blake Scholl on LinkedIn: https://www.linkedin.com/in/blakescholl/
  • Creating Truthtelling Incentives with the Bayesian Truth Serum: https://www.eecs.harvard.edu/cs286r/courses/fall12/papers/DW08.pdf
  • Asana: https://asana.com/
  • Spaces: https://blog.x.com/en_us/topics/product/2021/spaces-is-here
  • Amazon MTurk: https://www.mturk.com/
  • Community notes on GitHub: https://github.com/twitter/communitynotes
  • What do I think about Community Notes?: https://vitalik.eth.limo/general/2023/08/16/communitynotes.html
  • X’s community-led approach: tackling inaccurate and misleading information: https://blog.x.com/en_us/topics/company/2023/xs-community-led-approach-tackling-inaccurate-and-misleading-information
  • Messi-Ronaldo rivalry: https://en.wikipedia.org/wiki/Messi%E2%80%93Ronaldo_rivalry
  • Supernotes paper: https://arxiv.org/pdf/2411.06116v1

  Production and marketing by https://penname.co/. For inquiries about sponsoring the podcast, email podcast@lennyrachitsky.com.

  Lenny may be an investor in the companies discussed.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:47:50.875Z
---

# An inside look at X’s Community Notes | Keith Coleman & Jay Baxter

## 00:00 - 45:00

the work that you guys do has had such a

## 45:00 - 75:00

tremendous impact on the way the world

## 75:00 - 105:00

works I want to start with just giving

## 105:00 - 140:00

people a brief understanding of what is

## 140:00 - 180:00

community notes someone on X can see a

## 180:00 - 210:00

post if they think it's misleading they

## 210:00 - 240:00

can propose a note that they think other

## 240:00 - 265:00

people might find informative other

## 265:00 - 300:00

people can then rate that note we

## 300:00 - 335:00

actually look for agreement from people

## 335:00 - 375:00

who have disagreed in the past and and

## 375:00 - 405:00

what we see is when people actually have

## 405:00 - 440:00

that sort of surprising agreement that's

## 440:00 - 480:00

what makes the notes so neutral and and

## 480:00 - 515:00

accurate and well written really overall

## 515:00 - 535:00

there's many people that are very

## 535:00 - 560:00

polarized how do you deal with people

## 560:00 - 600:00

that are like super antiva super jan6

## 600:00 - 630:00

one philosophical thing that's important

## 630:00 - 680:00

is that we want all of humanity to

## 680:00 - 715:00

participate and sometimes people are

## 715:00 - 735:00

surprised by that we have all of

## 735:00 - 775:00

humanity we then have the data to

## 775:00 - 810:00

understand what notes will be helpful to

## 810:00 - 855:00

actual Humanity every post is eligible

## 855:00 - 900:00

for notes we shouldn't exempt Elon we

## 900:00 - 925:00

shouldn't exempt government figures we

## 925:00 - 955:00

should like everyone even advertisers

## 955:00 - 1000:00

can get notes there have been external

## 1000:00 - 1025:00

studies you know run by people totally

## 1025:00 - 1065:00

independent of us who have found that if

## 1065:00 - 1100:00

you take a post with or without a

## 1100:00 - 1135:00

community note that actually people's

## 1135:00 - 1155:00

agreement with the core claims on the

## 1155:00 - 1195:00

post does change if they see it with the

## 1195:00 - 1225:00

Note versus without is there anything

## 1225:00 - 1255:00

else along the lines of just working for

## 1255:00 - 1290:00

Elon within an oron runs that made

## 1290:00 - 1315:00

surprise people if I were started

## 1315:00 - 1335:00

company in that company it would be even

## 1335:00 - 1375:00

leaner than I would have made it before

## 1375:00 - 1415:00

I've been amazed with just how much the

## 1415:00 - 1465:00

team is able to accomplish with a small

## 1465:00 - 1495:00

group and I think because of a small

## 1495:00 - 1535:00

group

## 1535:00 - 1560:00

[Music]

## 1560:00 - 1590:00

today my guests are Keith Coleman

## 1590:00 - 1630:00

product lead for Community notes and J

## 1630:00 - 1665:00

bter founding ml engineer and researcher

## 1665:00 - 1700:00

for Community notes this conversation

## 1700:00 - 1730:00

may be my newest favorite podcast

## 1730:00 - 1775:00

episode so far Community notes is one of

## 1775:00 - 1825:00

the most impactful and clever and also

## 1825:00 - 1855:00

underappreciated products in the world

## 1855:00 - 1905:00

right now if you ever use x/ Twitter and

## 1905:00 - 1935:00

you see a note underneath a tweet

## 1935:00 - 1960:00

correcting the misinformation in that

## 1960:00 - 2005:00

tweet that is community notes I've never

## 2005:00 - 2035:00

heard a deep dive into the story behind

## 2035:00 - 2065:00

the product and the team that built it

## 2065:00 - 2100:00

and I'm excited to bring you just that

## 2100:00 - 2130:00

we get into the surprising origin story

## 2130:00 - 2160:00

of the product how the algorithm

## 2160:00 - 2200:00

actually works how the algorithm emerged

## 2200:00 - 2230:00

out of an internal contest within

## 2230:00 - 2265:00

Twitter the principles behind Community

## 2265:00 - 2295:00

notes and why staying true to them has

## 2295:00 - 2340:00

been so key to its success also how it

## 2340:00 - 2370:00

survived four different leaders

## 2370:00 - 2410:00

including Elon and Jack and why it's now

## 2410:00 - 2445:00

a big part of the solution to solving

## 2445:00 - 2480:00

misinformation on the internet including

## 2480:00 - 2510:00

recently being adopted by meta as their

## 2510:00 - 2540:00

main factchecking tool this is an

## 2540:00 - 2575:00

incredibly special episode and I'm so

## 2575:00 - 2600:00

excited to bring it to you if you enjoy

## 2600:00 - 2630:00

this podcast don't forget to subscribe

## 2630:00 - 2650:00

and followed in your favorite podcasting

## 2650:00 - 2690:00

app or YouTube also if you become a

## 2690:00 - 2730:00

subscriber of my newsletter you now get

## 2730:00 - 2775:00

a year free of notion and superhuman and

## 2775:00 - 2820:00

granola and linear and perplexity Pro

## 2820:00 - 2860:00

check that out at Lenny newletter tocom

## 2860:00 - 2895:00

with that I bring you Keith Coleman and

## 2895:00 - 2930:00

J

## 2930:00 - 2970:00

bter this episode is brought to you by

## 2970:00 - 3015:00

work OS if if you're building a SAS app

## 3015:00 - 3045:00

at some point your customers will start

## 3045:00 - 3095:00

asking for Enterprise features like saml

## 3095:00 - 3135:00

authentication and skim provisioning

## 3135:00 - 3175:00

that's where work OS comes in making it

## 3175:00 - 3205:00

fast and painless to add Enterprise

## 3205:00 - 3250:00

features to your app their apis are easy

## 3250:00 - 3275:00

to understand so that you can ship

## 3275:00 - 3305:00

quickly and get back to building other

## 3305:00 - 3350:00

features today hundreds of companies are

## 3350:00 - 3390:00

already powered by work OS including

## 3390:00 - 3435:00

ones you probably know like versel

## 3435:00 - 3485:00

webflow and Loom work OS also recently

## 3485:00 - 3525:00

acquired warrant the fine grain

## 3525:00 - 3565:00

authorization service warrant's product

## 3565:00 - 3595:00

is based on a groundbreaking

## 3595:00 - 3645:00

authorization system called zanbar which

## 3645:00 - 3675:00

was originally designed for Google to

## 3675:00 - 3715:00

power Google Docs and YouTube this

## 3715:00 - 3750:00

enables fast authorization checks at

## 3750:00 - 3780:00

enormous scale while maintaining a

## 3780:00 - 3815:00

flexible model that can be adapted to

## 3815:00 - 3850:00

even the most complex use cases if

## 3850:00 - 3875:00

you're currently looking to build

## 3875:00 - 3915:00

role-based access control or other

## 3915:00 - 3955:00

Enterprise features like single sign on

## 3955:00 - 3990:00

skim or user management you should

## 3990:00 - 4030:00

consider consider work OS it's a dropin

## 4030:00 - 4070:00

replacement for azero and supports up to

## 4070:00 - 4125:00

1 million monthly active users for free

## 4125:00 - 4175:00

check it out at work.com to learn more

## 4175:00 - 4210:00

that's

## 4210:00 - 4240:00

[Music]

## 4240:00 - 4280:00

work.com this episode is brought to you

## 4280:00 - 4315:00

by product board the leading product

## 4315:00 - 4350:00

management platform for the Enterprise

## 4350:00 - 4380:00

for over 10 years product board has

## 4380:00 - 4415:00

helped customer Centric organizations

## 4415:00 - 4455:00

like Zoom Salesforce and Autodesk build

## 4455:00 - 4495:00

the right products faster and as an

## 4495:00 - 4520:00

endtoend platform product board

## 4520:00 - 4555:00

seamlessly supports all stages of the

## 4555:00 - 4585:00

product development life cycle from

## 4585:00 - 4615:00

Gathering customer insights to planning

## 4615:00 - 4650:00

a road map to aligning stakeholders to

## 4650:00 - 4685:00

earning customer buying all with a

## 4685:00 - 4730:00

single source of Truth and now product

## 4730:00 - 4760:00

leaders can get even more visibility

## 4760:00 - 4795:00

into customer needs with product board

## 4795:00 - 4840:00

pulse a new voice of customer solution

## 4840:00 - 4870:00

built-in intelligence helps you analyze

## 4870:00 - 4900:00

Trends across all of your feedback and

## 4900:00 - 4935:00

then dive Deeper by asking AI your

## 4935:00 - 4970:00

follow-up questions see how product

## 4970:00 - 5000:00

board can help your team to deliver

## 5000:00 - 5035:00

higher impact products that solve real

## 5035:00 - 5070:00

customer needs and Advance your business

## 5070:00 - 5110:00

goals for a special offer and free

## 5110:00 - 5165:00

15-day trial visit product board.com

## 5165:00 - 5300:00

Lenny that's product board.com

## 5300:00 - 5350:00

lny Keith and J thank you so much for

## 5350:00 - 5385:00

being here welcome to the podcast it's

## 5385:00 - 5420:00

great to be here thanks thanks for

## 5420:00 - 5460:00

having us on it's so my pleasure I'm so

## 5460:00 - 5495:00

thrilled to be having this conversation

## 5495:00 - 5540:00

the work that you guys do has had such a

## 5540:00 - 5575:00

tremendous impact on the way the world

## 5575:00 - 5610:00

works so many product teams are always

## 5610:00 - 5635:00

talking about driving impact I want to

## 5635:00 - 5675:00

drive impact like you guys have actually

## 5675:00 - 5700:00

built things that have changed the world

## 5700:00 - 5730:00

in meaningful ways and continueed to do

## 5730:00 - 5760:00

that and I've never really heard the

## 5760:00 - 5790:00

backstory of how Community us came to be

## 5790:00 - 5830:00

and how it works and all these things so

## 5830:00 - 5845:00

I'm really appreciative of you guys

## 5845:00 - 5895:00

making time to chat yeah first you know

## 5895:00 - 5925:00

thanks for saying that that's that's why

## 5925:00 - 5955:00

we built this thing is to help people

## 5955:00 - 5980:00

and it's great to hear it it's great to

## 5980:00 - 6015:00

see people enjoying it and finding it

## 6015:00 - 6055:00

useful I want to start with just giving

## 6055:00 - 6100:00

people a brief understanding of what is

## 6100:00 - 6140:00

community notes I think a lot of people

## 6140:00 - 6175:00

may have kind of heard about it kind of

## 6175:00 - 6200:00

maybe see it on X as they scroll through

## 6200:00 - 6235:00

they see these notes but they're like I

## 6235:00 - 6265:00

don't actually know what this is so can

## 6265:00 - 6285:00

you just kind of briefly describe what

## 6285:00 - 6325:00

is community notes Community notes is a

## 6325:00 - 6375:00

way for the people like the public to

## 6375:00 - 6415:00

add context to posts that might be

## 6415:00 - 6465:00

misleading the basic way it works is

## 6465:00 - 6515:00

that uh someone on x can see a post if

## 6515:00 - 6540:00

they think it's misleading they can

## 6540:00 - 6565:00

propose a note that they think other

## 6565:00 - 6600:00

people might find informative other

## 6600:00 - 6645:00

people can then rate that note and if

## 6645:00 - 6680:00

the note is found helpful by people who

## 6680:00 - 6710:00

normally disagree with each other

## 6710:00 - 6740:00

indicating that it's probably accurate

## 6740:00 - 6775:00

it's probably really neutrally worded

## 6775:00 - 6810:00

it's probably informative then it will

## 6810:00 - 6845:00

show to everyone on X and the goal is

## 6845:00 - 6875:00

just to get people more information

## 6875:00 - 6900:00

about what they're seeing so they can

## 6900:00 - 6945:00

make better decisions in their lives

## 6945:00 - 6985:00

amazing and I think like hearing this

## 6985:00 - 7005:00

it's like

## 7005:00 - 7045:00

absur that this works I think when

## 7045:00 - 7100:00

people originally heard this idea like

## 7100:00 - 7130:00

no way this is going to work and so just

## 7130:00 - 7185:00

to dive a little bit deeper can you give

## 7185:00 - 7225:00

us a sense a deeper understanding of how

## 7225:00 - 7250:00

it actually works because I think it's

## 7250:00 - 7280:00

the algorithm that you guys designed

## 7280:00 - 7315:00

that is so clever that allowed this to

## 7315:00 - 7350:00

work so talk a little bit about that

## 7350:00 - 7400:00

algorithm yeah so so I think a key

## 7400:00 - 7435:00

misunderstanding a lot of people have if

## 7435:00 - 7465:00

they haven't really dived into details

## 7465:00 - 7495:00

they kind of just think that maybe

## 7495:00 - 7520:00

someone can write a note and it appears

## 7520:00 - 7560:00

immediately or or we're just taking a

## 7560:00 - 7605:00

majority rules vote uh of who thinks the

## 7605:00 - 7630:00

not's good I think both of those

## 7630:00 - 7660:00

approaches would probably lead to biased

## 7660:00 - 7690:00

or inaccurate notes I think the key

## 7690:00 - 7730:00

thing uh really that we do is we

## 7730:00 - 7765:00

actually look for agreement from people

## 7765:00 - 7810:00

who have disagreed in the past uh and

## 7810:00 - 7850:00

and what we see is when people actually

## 7850:00 - 7885:00

have that sort of surprising agreement

## 7885:00 - 7930:00

that's that's what makes the notes uh so

## 7930:00 - 7965:00

neutral and and accurate and well

## 7965:00 - 8005:00

written really overall um is just that

## 8005:00 - 8075:00

people who are very polarized um overall

## 8075:00 - 8105:00

uh often can't find agreement when

## 8105:00 - 8140:00

things aren't accurate right I I I think

## 8140:00 - 8165:00

it also provides some good anti-

## 8165:00 - 8200:00

manipulation properties I think people

## 8200:00 - 8255:00

are often you know if you said I think

## 8255:00 - 8290:00

like back in 2020 before we started

## 8290:00 - 8320:00

building anything here whether this

## 8320:00 - 8355:00

could work at all I think a room of ml

## 8355:00 - 8385:00

Engineers would say oh you have to keep

## 8385:00 - 8415:00

it closed Source you know people are

## 8415:00 - 8440:00

going to be manipulating this all the

## 8440:00 - 8470:00

time you have to use ground truth labels

## 8470:00 - 8515:00

from fact Checkers there's no way that

## 8515:00 - 8545:00

you could like bootstrap the system

## 8545:00 - 8590:00

without external labels uh but it turns

## 8590:00 - 8620:00

out that you can do that um with with

## 8620:00 - 8650:00

this kind of bridging based agreement

## 8650:00 - 8685:00

algorithm is what we call it okay so

## 8685:00 - 8715:00

just to summarize and make it super

## 8715:00 - 8735:00

clear it's basically people someone

## 8735:00 - 8770:00

writes a note this information is f

## 8770:00 - 8790:00

what's like a good example just as we

## 8790:00 - 8825:00

talk about this like a classic example

## 8825:00 - 8865:00

really really classic example is an AI

## 8865:00 - 8910:00

generated image or an out of context

## 8910:00 - 8940:00

image like look what's happening here

## 8940:00 - 8965:00

but it's actually from like five years

## 8965:00 - 8995:00

ago in a different country a different

## 8995:00 - 9020:00

topic oh man I've seen those so many

## 9020:00 - 9045:00

times where like look what's happening

## 9045:00 - 9080:00

in San Francisco like no this is a a

## 9080:00 - 9105:00

whole different city and that's not

## 9105:00 - 9140:00

totally yeah yeah okay okay so someone

## 9140:00 - 9180:00

posts this AI image uh someone writes a

## 9180:00 - 9210:00

note this is actually five years ago in

## 9210:00 - 9260:00

a different city and this algorithm

## 9260:00 - 9295:00

helps understand if this is a real if

## 9295:00 - 9330:00

this is true this note is true and it's

## 9330:00 - 9395:00

just people regular people doing this

## 9395:00 - 9440:00

yep yep regular people uh who have

## 9440:00 - 9460:00

signed up to be Community notes

## 9460:00 - 9495:00

contributors so you know there are a few

## 9495:00 - 9515:00

checks like you do have to have a

## 9515:00 - 9560:00

verified phone number for instance um

## 9560:00 - 9580:00

but yeah at the end of the day these are

## 9580:00 - 9615:00

these are regular people uh not

## 9615:00 - 9645:00

necessarily professional fact trackers

## 9645:00 - 9670:00

or anything like that and you know that

## 9670:00 - 9700:00

was like that was really important to us

## 9700:00 - 9725:00

too like there was a question at the

## 9725:00 - 9760:00

beginning to the point Jay was making of

## 9760:00 - 9790:00

like well did did anyone think this was

## 9790:00 - 9810:00

going to work obviously it was kind of a

## 9810:00 - 9860:00

crazy idea we didn't know if regular

## 9860:00 - 9880:00

people were going to be able to do this

## 9880:00 - 9920:00

task and certainly you know people had

## 9920:00 - 9940:00

concerns about whether they would do it

## 9940:00 - 9980:00

do it effectively initially some people

## 9980:00 - 10010:00

inside company were suggesting like hey

## 10010:00 - 10055:00

why don't you have journalists or you

## 10055:00 - 10090:00

know some some select group be the first

## 10090:00 - 10130:00

participants but very specifically we

## 10130:00 - 10155:00

like no that's like we're trying to move

## 10155:00 - 10210:00

away from the idea of curated editorial

## 10210:00 - 10235:00

decisions being made around this this is

## 10235:00 - 10265:00

supposed to be open to everyone so there

## 10265:00 - 10310:00

very we very intentionally try to allow

## 10310:00 - 10355:00

all humans in there people are randomly

## 10355:00 - 10395:00

selected um and that's important to it

## 10395:00 - 10425:00

you know feeling fair feeling open

## 10425:00 - 10475:00

feeling trustable yeah and again it's

## 10475:00 - 10500:00

just like the sound sounds like the Holy

## 10500:00 - 10540:00

Grail of understanding what is true and

## 10540:00 - 10595:00

it actually works and works so well at

## 10595:00 - 10645:00

meta recently as you all know uh decided

## 10645:00 - 10705:00

to uh adopt this exact system for them

## 10705:00 - 10740:00

and instead of having tens of thousands

## 10740:00 - 10780:00

of fact Checkers reviewing things one

## 10780:00 - 10805:00

distinction that I would make which may

## 10805:00 - 10835:00

maybe can come off as nitpicky but I

## 10835:00 - 10880:00

think is important is uh Community notes

## 10880:00 - 10915:00

adds additional context it's not

## 10915:00 - 10955:00

factchecking necessarily right so so

## 10955:00 - 10990:00

there are cases where the post could

## 10990:00 - 11025:00

true but maybe just misleading because

## 11025:00 - 11060:00

there's there's no context or there

## 11060:00 - 11100:00

missing context uh and you know we cover

## 11100:00 - 11165:00

those cases and I think that's that's

## 11165:00 - 11185:00

kind of an important distinction we also

## 11185:00 - 11205:00

we just have the philosophy that users

## 11205:00 - 11220:00

should be able to make up their own

## 11220:00 - 11260:00

minds right like here here's the here's

## 11260:00 - 11300:00

extra context take it or leave it right

## 11300:00 - 11325:00

yeah what I think about you shared this

## 11325:00 - 11365:00

with me this example of a a picture with

## 11365:00 - 11420:00

a with a with a cat and somebody's

## 11420:00 - 11465:00

community net was just that's a dog or

## 11465:00 - 11490:00

is it the other way around or that's a

## 11490:00 - 11550:00

yeah yeah it Palestinian boy shares his

## 11550:00 - 11585:00

bread with a dog was the post and it's a

## 11585:00 - 11635:00

picture of this cat

## 11635:00 - 11675:00

right so like obviously this particular

## 11675:00 - 11705:00

note is not super necessary because it

## 11705:00 - 11730:00

just says that's a cat and links to

## 11730:00 - 11780:00

Wikipedia for cat uh it's kind of a good

## 11780:00 - 11845:00

example that uh that like the system is

## 11845:00 - 11870:00

this is not something a professional

## 11870:00 - 11895:00

fact check or whatever right or think

## 11895:00 - 11935:00

would need factchecking but it it's

## 11935:00 - 11965:00

proof that the system is really run by

## 11965:00 - 12005:00

the users at the end of the day uh and

## 12005:00 - 12055:00

and add some com if I guess uh and you

## 12055:00 - 12110:00

know that's the note is correct and I

## 12110:00 - 12160:00

can you know it's important when does a

## 12160:00 - 12205:00

post get triggered to even be considered

## 12205:00 - 12230:00

for Community note is there like a

## 12230:00 - 12250:00

threshold or is it just you can write a

## 12250:00 - 12280:00

commun on anything and people decide

## 12280:00 - 12310:00

what they want vote on how's that work

## 12310:00 - 12365:00

so every post is eligible for notes um

## 12365:00 - 12395:00

it's and that was again another really

## 12395:00 - 12440:00

important principle it's like it we

## 12440:00 - 12490:00

shouldn't exempt uh Elon shouldn't

## 12490:00 - 12520:00

exempt government figures we should like

## 12520:00 - 12550:00

everyone even advertisers can get notes

## 12550:00 - 12585:00

so any posts on the platform can get a

## 12585:00 - 12620:00

note and if you look in practice um

## 12620:00 - 12650:00

you'll see notes appearing on world

## 12650:00 - 12715:00

leaders on Elon on ads on media

## 12715:00 - 12750:00

organizations and on obviously like just

## 12750:00 - 12795:00

regular people using social media but

## 12795:00 - 12820:00

yeah the idea is really that it's an

## 12820:00 - 12865:00

even playing field for a note to be

## 12865:00 - 12895:00

proposed the person proposing has to

## 12895:00 - 12940:00

have earned the ability to write notes

## 12940:00 - 12995:00

so there is there is that aspect where

## 12995:00 - 13025:00

you have to like earn in to be able to

## 13025:00 - 13050:00

do this and the way you earn that

## 13050:00 - 13105:00

ability is is through your ratings by

## 13105:00 - 13130:00

demonstrating the ability to help

## 13130:00 - 13160:00

identify notes that are found helpful to

## 13160:00 - 13190:00

a broad range of people so basically

## 13190:00 - 13235:00

like if you have an ability to to sort

## 13235:00 - 13270:00

of see and know recognize what's helpful

## 13270:00 - 13300:00

to a lot of people then you have the

## 13300:00 - 13335:00

ability to start proposing notes I

## 13335:00 - 13375:00

actually signed up to be an a what do

## 13375:00 - 13400:00

you what do you call these people no no

## 13400:00 - 13440:00

no Tak contributors no okay contributors

## 13440:00 - 13480:00

yes I've been rating I haven't achieved

## 13480:00 - 13520:00

hi can write notes yet yeah it's not

## 13520:00 - 13560:00

super easy it takes it takes an effort

## 13560:00 - 13580:00

are there stats you can share about the

## 13580:00 - 13605:00

scale of community notes at this point

## 13605:00 - 13630:00

especially things that might surprise

## 13630:00 - 13680:00

people yeah um I mean the service is

## 13680:00 - 13720:00

growing rapidly so there are hundreds of

## 13720:00 - 13755:00

notes per day and to put that into

## 13755:00 - 13795:00

context I saw some stats recently from

## 13795:00 - 13820:00

someone at UC Berkeley saying there

## 13820:00 - 13855:00

there were something like 10 fact checks

## 13855:00 - 13890:00

traditional fact checks a day so in

## 13890:00 - 13925:00

contrast there's hundreds of notes a day

## 13925:00 - 13970:00

um that are getting shown they span a

## 13970:00 - 14005:00

huge range of topics from obviously

## 14005:00 - 14060:00

politics news um out to Entertainment

## 14060:00 - 14100:00

Sports gaming just whatever's going on

## 14100:00 - 14140:00

that day in addition to there being

## 14140:00 - 14165:00

hundred of the hundreds of these

## 14165:00 - 14200:00

individual notes they can also be

## 14200:00 - 14245:00

matched to multiple posts so if someone

## 14245:00 - 14280:00

writes a note on an image or a video

## 14280:00 - 14315:00

like let's say it's AI generated or

## 14315:00 - 14355:00

something like that that note will

## 14355:00 - 14385:00

automatically be matched to all posts

## 14385:00 - 14420:00

that contain the same image so you can

## 14420:00 - 14445:00

have a single note matching to thousands

## 14445:00 - 14515:00

of posts and over uh let's say the last

## 14515:00 - 14565:00

the last year 2024 we had something like

## 14565:00 - 14610:00

95,000 notes that were seeing about 30

## 14610:00 - 14655:00

billion times that's more than double

## 14655:00 - 14685:00

the prior year prior year was something

## 14685:00 - 14755:00

like 37k notes seen 14 billion times so

## 14755:00 - 14800:00

that rate is increasing dramatically you

## 14800:00 - 14845:00

think about like 30 billion views that's

## 14845:00 - 14885:00

a lot of information that is getting out

## 14885:00 - 14915:00

there that might not have been out there

## 14915:00 - 14970:00

otherwise which is pretty cool and the

## 14970:00 - 14990:00

part of the reason reason it is

## 14990:00 - 15025:00

expanding like that is the contributor

## 15025:00 - 15060:00

base is expanding um there's something

## 15060:00 - 15115:00

like 950,000 contributors around the

## 15115:00 - 15160:00

world that's you know nearing a million

## 15160:00 - 15215:00

people making this happen um which is

## 15215:00 - 15240:00

amazing and I'm one of those right like

## 15240:00 - 15280:00

I count as a contributor yeah you signed

## 15280:00 - 15315:00

up as a contributor UK okay then there's

## 15315:00 - 15350:00

more people on the weight list too uh so

## 15350:00 - 15370:00

there there's plenty of head room for

## 15370:00 - 15415:00

more growth regarding the the like the

## 15415:00 - 15485:00

matching uh the on on VD media and urls

## 15485:00 - 15520:00

um I think that's a huge way to get

## 15520:00 - 15570:00

extra coverage also I I do think uh

## 15570:00 - 15600:00

we've been very careful to make sure

## 15600:00 - 15650:00

that those matches are uh precise

## 15650:00 - 15670:00

because I think one thing that people

## 15670:00 - 15710:00

love about Community notes compared to

## 15710:00 - 15745:00

other types of factchecking is that

## 15745:00 - 15770:00

actually the notes are custom written

## 15770:00 - 15795:00

for the particular claim you're seeing

## 15795:00 - 15845:00

right so so often a fact check warning

## 15845:00 - 15880:00

would just say something like you know

## 15880:00 - 15905:00

get the facts here and then there's a

## 15905:00 - 15955:00

link to some generic page about voting

## 15955:00 - 16005:00

uh like information uh which is you know

## 16005:00 - 16030:00

so so not helpful to have the the

## 16030:00 - 16075:00

information behind a click so so pulling

## 16075:00 - 16115:00

the context up you know so that you zero

## 16115:00 - 16145:00

clicks that you need to make and and

## 16145:00 - 16185:00

keeping it specific is so important I uh

## 16185:00 - 16210:00

one feature I love that I imagine you

## 16210:00 - 16240:00

guys thought deeply about is if I like

## 16240:00 - 16270:00

the post in the past I get notified

## 16270:00 - 16300:00

later if a community note shows up so

## 16300:00 - 16345:00

that I'm not like remembering this false

## 16345:00 - 16385:00

information yeah I mean we we try to

## 16385:00 - 16430:00

make notes as fast as they as we can so

## 16430:00 - 16460:00

we want them to appear instantly if

## 16460:00 - 16495:00

possible but in inevitably there's going

## 16495:00 - 16530:00

to be a time gap between when a post

## 16530:00 - 16555:00

goes live and when people figure out

## 16555:00 - 16570:00

what's going on and when they get the

## 16570:00 - 16595:00

note out there and so we send those

## 16595:00 - 16640:00

notifications to try to close that Gap

## 16640:00 - 16680:00

um and yeah we get we we get a lot of

## 16680:00 - 16715:00

love for that we see people take

## 16715:00 - 16735:00

screenshots and share them they're

## 16735:00 - 16785:00

excited about it um and it's also a

## 16785:00 - 16810:00

pretty cool example of something you can

## 16810:00 - 16850:00

do on the internet in the social media

## 16850:00 - 16875:00

world that was difficult in kind of like

## 16875:00 - 16915:00

a print or standard news World um where

## 16915:00 - 16945:00

you would see maybe a correction like

## 16945:00 - 16995:00

the next day in a corner of a paper but

## 16995:00 - 17020:00

it was hard to read here you're getting

## 17020:00 - 17050:00

a ping about it if you've if you've

## 17050:00 - 17090:00

engaged with the post and not show up

## 17090:00 - 17140:00

one user feedback uh point is I'd love

## 17140:00 - 17170:00

the push to just tell me here's what you

## 17170:00 - 17200:00

got wrong because I I find that I

## 17200:00 - 17220:00

actually have to go into it and like

## 17220:00 - 17255:00

read it and I feel like the push could

## 17255:00 - 17295:00

just be like here's information here's

## 17295:00 - 17325:00

more context to this thing you

## 17325:00 - 17375:00

like we'll go take a look at that go

## 17375:00 - 17420:00

live Easier feedback nice okay I want to

## 17420:00 - 17445:00

get into the origin story this whole

## 17445:00 - 17460:00

thing but two more questions because

## 17460:00 - 17500:00

we're on this thread one is what what's

## 17500:00 - 17525:00

the kind of the threshold for a note to

## 17525:00 - 17555:00

show up on a note is that information

## 17555:00 - 17600:00

you can share just how does that work so

## 17600:00 - 17625:00

just because of the details of the way

## 17625:00 - 17660:00

the algorithm works it uses this machine

## 17660:00 - 17690:00

learning algorithm you know called

## 17690:00 - 17720:00

Matrix factorization where you know we

## 17720:00 - 17750:00

fit it with gradient descend and whatnot

## 17750:00 - 17810:00

the threshold is you know it's it's

## 17810:00 - 17865:00

0.4 uh on this you know madeup scale 0.4

## 17865:00 - 17915:00

great there we go I mean in practice

## 17915:00 - 17970:00

what it means is you know basically a a

## 17970:00 - 18005:00

a majority of people if there is a

## 18005:00 - 18035:00

polarized divide relevant to the note

## 18035:00 - 18060:00

you know obviously some notes are not

## 18060:00 - 18090:00

about politics or something polarizing

## 18090:00 - 18140:00

but if there is then a majority a

## 18140:00 - 18170:00

sizable majority of people on both sides

## 18170:00 - 18195:00

would would generally need to find the

## 18195:00 - 18250:00

note helpful uh and then there are these

## 18250:00 - 18285:00

there are other rules that come into

## 18285:00 - 18320:00

play beyond that main one so you know

## 18320:00 - 18365:00

even if it's above that threshold um it

## 18365:00 - 18400:00

might get filtered out if um there

## 18400:00 - 18425:00

there's a separate algorithm that's

## 18425:00 - 18465:00

looking at agreement between people's

## 18465:00 - 18485:00

incorrect t

## 18485:00 - 18515:00

so like maybe maybe people found the

## 18515:00 - 18555:00

note helpful but incorrect right like it

## 18555:00 - 18590:00

happens uh and in those cases it doesn't

## 18590:00 - 18610:00

matter if it's above the helpfulness

## 18610:00 - 18655:00

threshold so is this point4 is uh that's

## 18655:00 - 18680:00

probably the wrong way to think about it

## 18680:00 - 18725:00

but is it 40% of people that normally

## 18725:00 - 18755:00

disagree agree okay means nothing like

## 18755:00 - 18775:00

that it's it's just like on some

## 18775:00 - 18835:00

arbitrary scale yeah yeah if we changed

## 18835:00 - 18860:00

random other things about the algorithm

## 18860:00 - 18885:00

that number would also have to change to

## 18885:00 - 18925:00

an equally seemingly arbitrary number

## 18925:00 - 18980:00

yeah that we we arrived at at some like

## 18980:00 - 19020:00

some numbers like that by gauging user

## 19020:00 - 19050:00

feedback so we we could share a lot of

## 19050:00 - 19075:00

notes with people get feedback on which

## 19075:00 - 19105:00

ones are helpful and there sort of just

## 19105:00 - 19160:00

align emerged about indicating where you

## 19160:00 - 19190:00

know where the where things go from like

## 19190:00 - 19220:00

questionable to pretty clearly helpful

## 19220:00 - 19255:00

yeah and and it is set right now by the

## 19255:00 - 19305:00

way to be really conservative I think uh

## 19305:00 - 19360:00

we we just are pretty particular about

## 19360:00 - 19395:00

quality and we really want no quality to

## 19395:00 - 19460:00

be really high I think uh I think Keith

## 19460:00 - 19495:00

and I both believe that we deler die

## 19495:00 - 19545:00

based on the quality uh of the notes at

## 19545:00 - 19585:00

the end of the day so so we'd rather not

## 19585:00 - 19630:00

show a note that may be good but we

## 19630:00 - 19665:00

don't have enough signal on um then the

## 19665:00 - 19690:00

other way around that makes so much

## 19690:00 - 19725:00

sense like I've never seen a community

## 19725:00 - 19785:00

note that is wrong and breaking that

## 19785:00 - 19820:00

promise is a big deal so I completely

## 19820:00 - 19845:00

get why you guys are super conservative

## 19845:00 - 19880:00

there uh okay two more questions along

## 19880:00 - 19905:00

the because I'm just curious these

## 19905:00 - 19930:00

weren't on my list of questions asked

## 19930:00 - 19960:00

but I feel like people wonder this how

## 19960:00 - 19985:00

many notes are

## 19985:00 - 20020:00

versus end up showing up and triggering

## 20020:00 - 20100:00

on it we probably show about 8% of notes

## 20100:00 - 20155:00

that get proposed um I think that's it's

## 20155:00 - 20205:00

been between it's say 7% and 10% or 11%

## 20205:00 - 20230:00

something like that over time the number

## 20230:00 - 20275:00

can vary a little bit um and as Jay said

## 20275:00 - 20320:00

there are un undoubtedly and you can see

## 20320:00 - 20350:00

there's there's clearly more good notes

## 20350:00 - 20405:00

than we show but the goal is to hold a

## 20405:00 - 20435:00

really high bar like we want to show a

## 20435:00 - 20480:00

note when it's going to be helpful when

## 20480:00 - 20525:00

it's not going to appear you know bias

## 20525:00 - 20550:00

and undermine trust in the system like

## 20550:00 - 20580:00

we want these to be neutral informative

## 20580:00 - 20615:00

helpful and um you know as Jay was

## 20615:00 - 20655:00

saying like we view the worst possible

## 20655:00 - 20695:00

mistake as showing a bad note because

## 20695:00 - 20720:00

that's going to undermine trust and the

## 20720:00 - 20760:00

trust is is is why people like the

## 20760:00 - 20815:00

product so so yeah we the bar is there

## 20815:00 - 20835:00

and you know like I said there's there's

## 20835:00 - 20875:00

clearly some um some in that remaining

## 20875:00 - 20915:00

let's call it 90% that are good and then

## 20915:00 - 20940:00

there's a lot that are just like not

## 20940:00 - 20970:00

that great and there's some that are bad

## 20970:00 - 21025:00

and if you write one of these ones that

## 21025:00 - 21060:00

are bad which bad being defined as

## 21060:00 - 21105:00

people who normally disagree find the

## 21105:00 - 21130:00

note not helpful so it's like the

## 21130:00 - 21170:00

inverse of the ones we show if you write

## 21170:00 - 21200:00

one that people you know people normally

## 21200:00 - 21225:00

disagree find not helpful you actually

## 21225:00 - 21250:00

will ultimately lose your ability to

## 21250:00 - 21290:00

write and have to earn it back so that

## 21290:00 - 21330:00

that range that ear 90% is a mix

## 21330:00 - 21350:00

sometimes people look at the number

## 21350:00 - 21375:00

they're like oh why don't you show more

## 21375:00 - 21395:00

it's like well you probably actually

## 21395:00 - 21420:00

don't really want us showing most of

## 21420:00 - 21475:00

those it's the the the gold here is that

## 21475:00 - 21495:00

the system is able to filter out the

## 21495:00 - 21545:00

good ones that makes sense okay one

## 21545:00 - 21575:00

other question is there's many people

## 21575:00 - 21615:00

that are very polarized like very

## 21615:00 - 21660:00

disagreeable with a lot of things how do

## 21660:00 - 21690:00

they filter into this algorithm how do

## 21690:00 - 21715:00

you deal with people that are like super

## 21715:00 - 21760:00

antiva super janix like all these very

## 21760:00 - 21805:00

extreme potential views If people really

## 21805:00 - 21850:00

are so polarized uh that there there

## 21850:00 - 21890:00

isn't agreement uh among people who

## 21890:00 - 21920:00

typically disagree you know it's

## 21920:00 - 21945:00

possible that this is one of those notes

## 21945:00 - 21980:00

that might be correct but

## 21980:00 - 22025:00

but just wouldn't be useful cont it

## 22025:00 - 22075:00

wouldn't be you know helpful to show uh

## 22075:00 - 22115:00

as as context maybe maybe it's about a

## 22115:00 - 22170:00

claim that people have you know really

## 22170:00 - 22195:00

entrenched opinions about and they've

## 22195:00 - 22235:00

read hundreds of things about it already

## 22235:00 - 22270:00

uh right like probably probably this is

## 22270:00 - 22320:00

just uh not going to improve people's

## 22320:00 - 22340:00

understanding it's just not going to be

## 22340:00 - 22375:00

a helpful user experience so it might

## 22375:00 - 22410:00

not be the worst thing uh in those cases

## 22410:00 - 22450:00

to not show the note people a few years

## 22450:00 - 22480:00

ago were pretty pessimistic that maybe

## 22480:00 - 22535:00

fact checking never changes people's uh

## 22535:00 - 22565:00

you know understandings about what's

## 22565:00 - 22610:00

true actually there have been external

## 22610:00 - 22645:00

um studies you know run by people

## 22645:00 - 22680:00

totally independent of us uh who have

## 22680:00 - 22735:00

found that if you take a community note

## 22735:00 - 22775:00

uh or a post with or without a community

## 22775:00 - 22815:00

note that actually people's agreement

## 22815:00 - 22845:00

with the core claims in the post does

## 22845:00 - 22875:00

change if they see it with the Note

## 22875:00 - 22900:00

versus without so we are having an

## 22900:00 - 22925:00

impact uh on this thing that people

## 22925:00 - 22965:00

previously thought was maybe not so easy

## 22965:00 - 22985:00

to deal

## 22985:00 - 23035:00

um and um so it's nice to focus on the

## 23035:00 - 23050:00

cases where there is the bridging

## 23050:00 - 23100:00

agreement I would also say there is this

## 23100:00 - 23130:00

reputation component to the algorithm as

## 23130:00 - 23180:00

well so if you consistently rate notes

## 23180:00 - 23240:00

in a way that is counter to the the

## 23240:00 - 23275:00

bridging based consensus then we'll stop

## 23275:00 - 23330:00

counting your ratings right so uh you

## 23330:00 - 23355:00

know if if you're the kind of person who

## 23355:00 - 23410:00

constantly rates bad notes as helpful uh

## 23410:00 - 23445:00

we we do filter you out so so there's a

## 23445:00 - 23465:00

difference between those types of people

## 23465:00 - 23495:00

versus just the the good but polarized

## 23495:00 - 23545:00

ones yeah I think you one philosophical

## 23545:00 - 23600:00

thing that's important is that we want

## 23600:00 - 23645:00

all of humanity to participate and

## 23645:00 - 23665:00

sometimes people are surprised by that

## 23665:00 - 23685:00

they'll be like oh aren't there people

## 23685:00 - 23720:00

who are like you know shouldn't be doing

## 23720:00 - 23750:00

this or like there's so you know I don't

## 23750:00 - 23775:00

their their thinking is so extreme or

## 23775:00 - 23790:00

something maybe they shouldn't

## 23790:00 - 23825:00

participate but our view is it's

## 23825:00 - 23860:00

actually we want to have all of humanity

## 23860:00 - 23890:00

here because if we have all of humanity

## 23890:00 - 23930:00

we can we then have the data to

## 23930:00 - 23965:00

understand what notes will be helpful to

## 23965:00 - 24005:00

actual Humanity you know we can we can

## 24005:00 - 24035:00

better model that better better

## 24035:00 - 24055:00

understand and better show those notes

## 24055:00 - 24110:00

so it's advantageous to have people who

## 24110:00 - 24175:00

have all sorts of points of views and uh

## 24175:00 - 24210:00

we don't expect that every note will be

## 24210:00 - 24260:00

loved by every single person um you know

## 24260:00 - 24310:00

that's kind of an impossible bar but we

## 24310:00 - 24345:00

do intend to show the notes that like

## 24345:00 - 24380:00

80% of people are going to you know read

## 24380:00 - 24420:00

and say wow I'm God I knew that and so

## 24420:00 - 24450:00

you know in that sense it doesn't matter

## 24450:00 - 24510:00

how you know maybe extreme someone views

## 24510:00 - 24535:00

person's views as it's still great to

## 24535:00 - 24570:00

have them in the program um so you know

## 24570:00 - 24595:00

no matter what your views are please

## 24595:00 - 24625:00

sign up and participate it it helps

## 24625:00 - 24660:00

identify what's really helpful cool and

## 24660:00 - 24675:00

we'll link to people if they want to

## 24675:00 - 24705:00

actually sign up uh so they know how to

## 24705:00 - 24745:00

do this something we didn't actually T

## 24745:00 - 24770:00

specified these are all volunteers no

## 24770:00 - 24795:00

one's getting paid to be doing these

## 24795:00 - 24840:00

notes and voting right yeah it's totally

## 24840:00 - 24880:00

based on intrinsic motivation and and we

## 24880:00 - 24910:00

think that's a great reason to be doing

## 24910:00 - 24945:00

it um when you talk to the most active

## 24945:00 - 24980:00

contributors a lot of them they just

## 24980:00 - 25005:00

they want to have better information out

## 25005:00 - 25025:00

in the world and that's a great

## 25025:00 - 25075:00

motivation so yeah that's why they and

## 25075:00 - 25105:00

you know if you if you think about like

## 25105:00 - 25130:00

for these people the impact they can

## 25130:00 - 25195:00

have it's kind of nuts so uh when we

## 25195:00 - 25260:00

first launched us-wide this was like in

## 25260:00 - 25305:00

2022 a note appeared on a White House

## 25305:00 - 25350:00

tweet and the White House deleted the

## 25350:00 - 25395:00

tweet and reissued an updated statement

## 25395:00 - 25435:00

and like like imagine being the person

## 25435:00 - 25470:00

who wrote that you probably have like 12

## 25470:00 - 25520:00

followers your your posts probably get

## 25520:00 - 25570:00

you know a couple likes and here you

## 25570:00 - 25610:00

just put a put a note on the White House

## 25610:00 - 25645:00

and they changed their public talking

## 25645:00 - 25690:00

points based on what you did like that

## 25690:00 - 25750:00

is an incredible amount of impact so you

## 25750:00 - 25780:00

know it you can see why people are

## 25780:00 - 25810:00

motivated to do it when they care about

## 25810:00 - 25840:00

what's going on in the world it um you

## 25840:00 - 25870:00

know you don't have to be a big

## 25870:00 - 25930:00

well-known person to shape the discourse

## 25930:00 - 25975:00

and information flow in a in a way it's

## 25975:00 - 26025:00

helpful it's insane like there's so much

## 26025:00 - 26050:00

to love about this one is just the

## 26050:00 - 26085:00

meritocracy of this whole operation of

## 26085:00 - 26125:00

just anybody can that is true and

## 26125:00 - 26175:00

correct can participate and have impact

## 26175:00 - 26205:00

also just shows you how much information

## 26205:00 - 26240:00

we get that is just wrong like we had no

## 26240:00 - 26270:00

idea how often we see things that are

## 26270:00 - 26310:00

wrong and now we do working on this

## 26310:00 - 26335:00

product has made me realize just how

## 26335:00 - 26365:00

many things I used to trust kind of by

## 26365:00 - 26425:00

default that now I look at more skeptic

## 26425:00 - 26480:00

skeptically definitely mean these days

## 26480:00 - 26510:00

okay uh before we get to the origin

## 26510:00 - 26530:00

story is there anything else along these

## 26530:00 - 26545:00

lines you guys think might be really

## 26545:00 - 26580:00

important to share really really

## 26580:00 - 26630:00

interesting sure I guess one other thing

## 26630:00 - 26685:00

just um is is that although we don't

## 26685:00 - 26725:00

actually use the fact that a post was

## 26725:00 - 26780:00

noted uh in the core ranking algorithm

## 26780:00 - 26830:00

um which you know we we think is a nice

## 26830:00 - 26885:00

property uh there is a really big impact

## 26885:00 - 26915:00

just organically meaning not from the

## 26915:00 - 26945:00

algorithm but just from user Behavior

## 26945:00 - 26995:00

where people will like and reshare or

## 26995:00 - 27060:00

you know quote uh posts way less uh when

## 27060:00 - 27100:00

when notes are applied so just I don't

## 27100:00 - 27125:00

know for for people out there who

## 27125:00 - 27180:00

typically run AB tests on big uh you

## 27180:00 - 27205:00

know platforms you may already be

## 27205:00 - 27240:00

familiar with this but like 1% is

## 27240:00 - 27285:00

typically an awesome effect size for any

## 27285:00 - 27320:00

sort of algorithm change we saw more

## 27320:00 - 27385:00

like 30 to 40% engagement rate drops uh

## 27385:00 - 27420:00

for likes and reposts and an AB test we

## 27420:00 - 27490:00

ran uh when comparing uh showing a post

## 27490:00 - 27515:00

with or without a note which is just

## 27515:00 - 27560:00

crazy big um and then and then if you

## 27560:00 - 27595:00

actually look that's that's just an AB

## 27595:00 - 27620:00

test on the engagement rate so that's

## 27620:00 - 27645:00

not the network effect if you capture

## 27645:00 - 27700:00

the the overall Network effect of how a

## 27700:00 - 27755:00

post uh you know is spread less by that

## 27755:00 - 27790:00

person's repost uh this could feel like

## 27790:00 - 27810:00

Top Line with a difference and

## 27810:00 - 27850:00

differences approach different multiple

## 27850:00 - 27875:00

different external research groups have

## 27875:00 - 27910:00

both found consistently that there's

## 27910:00 - 27970:00

like a 50 or 60% drop in total repost

## 27970:00 - 28015:00

which is just nuts um after not is

## 28015:00 - 28055:00

applied so it's having a really big

## 28055:00 - 28115:00

impact on spread actually too that's so

## 28115:00 - 28145:00

like that's so great to hear it's what I

## 28145:00 - 28180:00

would want to see and it's incredible

## 28180:00 - 28220:00

impact basically like a AI image of

## 28220:00 - 28255:00

something false would just go crazy on

## 28255:00 - 28285:00

Twitter and did before Community notes

## 28285:00 - 28310:00

came out and now what you're saying is

## 28310:00 - 28345:00

just adding that context not actually

## 28345:00 - 28370:00

like you're saying the algorithm doesn't

## 28370:00 - 28410:00

demote it if there's something incorrect

## 28410:00 - 28440:00

it's just people are like okay this is

## 28440:00 - 28460:00

false why would I want to retweet this

## 28460:00 - 28510:00

that Mak correct yeah the the notes just

## 28510:00 - 28540:00

totally take the wind out of these

## 28540:00 - 28570:00

stories so like the thing will be going

## 28570:00 - 28625:00

viral note appears res sharing drops 50

## 28625:00 - 28670:00

to 60% and like that's it like it just

## 28670:00 - 28720:00

you can at 50 to 60% per generation this

## 28720:00 - 28755:00

the virality quickly goes to zero and

## 28755:00 - 28795:00

and by the way there's uh I I have very

## 28795:00 - 28830:00

mixed feelings about this next one uh

## 28830:00 - 28870:00

but authors become 80% more likely to

## 28870:00 - 28905:00

decrease or sorry to delete their post

## 28905:00 - 28945:00

after they get noted which okay that's

## 28945:00 - 28985:00

great because like less less misinfo out

## 28985:00 - 29035:00

there but I'm pained about because those

## 29035:00 - 29075:00

are usually the best notes like if if

## 29075:00 - 29115:00

the note was so just good that you had

## 29115:00 - 29140:00

nothing you had no other option but to

## 29140:00 - 29180:00

delete your post those notes don't get

## 29180:00 - 29225:00

seen by other people right because

## 29225:00 - 29260:00

there's there's an argument by the way

## 29260:00 - 29305:00

that like seeing that just because you

## 29305:00 - 29330:00

might see the same misleading claim

## 29330:00 - 29375:00

elsewhere off X or somewhere else on X

## 29375:00 - 29405:00

uh you know it might be good to actually

## 29405:00 - 29445:00

show better to have seen the post with

## 29445:00 - 29495:00

the note than not see it at all yeah

## 29495:00 - 29525:00

unsure about that Co that is so

## 29525:00 - 29575:00

interesting yeah uh yeah I could I'd be

## 29575:00 - 29605:00

so sad if I was that Community not

## 29605:00 - 29650:00

writer and just oh man it's so good they

## 29650:00 - 29720:00

just can't even keep the post up okay so

## 29720:00 - 29755:00

coming back from today's world where

## 29755:00 - 29820:00

you're this like small amount of code is

## 29820:00 - 29855:00

changing the way people understand the

## 29855:00 - 29890:00

world and what they believe and making

## 29890:00 - 29915:00

the White House resin their

## 29915:00 - 29945:00

announcements zooming back to the

## 29945:00 - 29975:00

beginning of how this whole project

## 29975:00 - 30035:00

started uh what I heard just briefly is

## 30035:00 - 30070:00

uh Keith you were just kind of tired of

## 30070:00 - 30100:00

managing PMS you wanted to just work on

## 30100:00 - 30125:00

something yourself you wanted to work on

## 30125:00 - 30165:00

something impactful away from corporate

## 30165:00 - 30200:00

BS and you basically just started

## 30200:00 - 30240:00

looking for something that was impactful

## 30240:00 - 30265:00

important and you found this talk about

## 30265:00 - 30295:00

just how it all came to be at beginnings

## 30295:00 - 30340:00

of the story yeah so I mean for me the

## 30340:00 - 30375:00

beginnings actually go back to why I

## 30375:00 - 30440:00

joined you was then Twitter um in 2016 I

## 30440:00 - 30480:00

was uh I had a start out

## 30480:00 - 30525:00

and we were we' had some acquisition

## 30525:00 - 30580:00

offers and one of them was from company

## 30580:00 - 30630:00

Twitter and uh it was 2016 it was the

## 30630:00 - 30670:00

middle of the election between Donald

## 30670:00 - 30720:00

Trump and Hillary Clinton and there were

## 30720:00 - 30745:00

like something like three televised

## 30745:00 - 30805:00

debates but every day there was a debate

## 30805:00 - 30825:00

happening on Twitter and it was very

## 30825:00 - 30875:00

clear like this is where people are

## 30875:00 - 30900:00

talking about these things that matter

## 30900:00 - 30950:00

where where you know information is

## 30950:00 - 30980:00

being shared where where ideas are being

## 30980:00 - 31045:00

formed and as a user it was obvious that

## 31045:00 - 31085:00

I could get good information there but

## 31085:00 - 31125:00

uh it was also obvious that there was

## 31125:00 - 31145:00

kind of questionable information

## 31145:00 - 31175:00

floating around and I remember just

## 31175:00 - 31210:00

looking as an outsider thinking like wow

## 31210:00 - 31240:00

like this is a really hard problem that

## 31240:00 - 31275:00

it also seems really important so we

## 31275:00 - 31315:00

ended up going to Twitter and and the

## 31315:00 - 31335:00

company was in a turnaround at that

## 31335:00 - 31365:00

point so like my first three years was

## 31365:00 - 31400:00

just helping to get the company growing

## 31400:00 - 31445:00

again um you know working on on

## 31445:00 - 31490:00

everything that was the consumer product

## 31490:00 - 31525:00

um you know getting user growth going

## 31525:00 - 31550:00

back getting people wanting to work

## 31550:00 - 31605:00

there again Etc um but a few years in I

## 31605:00 - 31665:00

was reflecting on what we had done um

## 31665:00 - 31690:00

you know I think we had done a lot of

## 31690:00 - 31710:00

good work getting

## 31710:00 - 31780:00

momentum going but it and people in the

## 31780:00 - 31820:00

US and in the industry had tried things

## 31820:00 - 31850:00

to kind of deal with with misleading

## 31850:00 - 31880:00

information but nothing was really

## 31880:00 - 31900:00

working like it was obvious nothing was

## 31900:00 - 31945:00

working um nothing could handle the

## 31945:00 - 31975:00

scale of the problem nothing could

## 31975:00 - 32010:00

handle the speed and a lot of people

## 32010:00 - 32045:00

just didn't trust the existing

## 32045:00 - 32065:00

approaches like this the existing

## 32065:00 - 32120:00

approaches were either fact Checkers or

## 32120:00 - 32145:00

internal trust and safety teams making

## 32145:00 - 32180:00

decisions about what was or was not

## 32180:00 - 32220:00

misleading and like a lot of people just

## 32220:00 - 32265:00

didn't want or trust that to be the way

## 32265:00 - 32285:00

this was decided which is very

## 32285:00 - 32330:00

reasonable and so you know I'm looking

## 32330:00 - 32370:00

at that I was I was still managing a

## 32370:00 - 32415:00

large PM team

## 32415:00 - 32455:00

uh you know that's a whole story in

## 32455:00 - 32470:00

itself

## 32470:00 - 32535:00

I um I felt like I would that job

## 32535:00 - 32580:00

required a lot of energy in and I and I

## 32580:00 - 32610:00

didn't feel like I always saw the output

## 32610:00 - 32645:00

that I wanted to see from it like I

## 32645:00 - 32670:00

didn't see the change in the product I

## 32670:00 - 32705:00

wanted to see and you know I was

## 32705:00 - 32730:00

contemplating should I go start a

## 32730:00 - 32780:00

company uh should I do something else

## 32780:00 - 32810:00

and I kept coming back to this problem

## 32810:00 - 32855:00

I'm like man like the how is the world

## 32855:00 - 32885:00

going to deal with the with this

## 32885:00 - 32915:00

information quality issue of like what

## 32915:00 - 32950:00

we get on social media wherever we get

## 32950:00 - 32995:00

it and I'm like you know I'm at I'm at

## 32995:00 - 33020:00

this company where you can make a

## 33020:00 - 33060:00

difference on this problem like why not

## 33060:00 - 33110:00

go and try some crazy ideas and see if

## 33110:00 - 33155:00

like one of them might work and so I

## 33155:00 - 33180:00

came back I had I had a kid I came back

## 33180:00 - 33225:00

from paternity leave I went to my boss

## 33225:00 - 33260:00

Kavon I was like Hey Kayon how about I

## 33260:00 - 33305:00

just stop doing my job and I go work on

## 33305:00 - 33335:00

this instead you know this being try

## 33335:00 - 33365:00

some crazy ideas to see if we can deal

## 33365:00 - 33425:00

with with misleading info he was stoked

## 33425:00 - 33455:00

uh and so I went off and started working

## 33455:00 - 33525:00

on that um you know it started with just

## 33525:00 - 33570:00

reading any research I could on the the

## 33570:00 - 33600:00

problem and existing Solutions what was

## 33600:00 - 33625:00

or was not working or what were the

## 33625:00 - 33665:00

issues um and then into prototyping and

## 33665:00 - 33715:00

then you know It ultimately led to us

## 33715:00 - 33745:00

building and piloting this idea that

## 33745:00 - 33790:00

became Community notes amazing okay I

## 33790:00 - 33810:00

have so many questions and we're GNA

## 33810:00 - 33845:00

keep going through the story but uh when

## 33845:00 - 33875:00

you joined Twitter what was kind of the

## 33875:00 - 33895:00

it was called Twitter at this point I'm

## 33895:00 - 33920:00

going to try to call call it X now which

## 33920:00 - 33970:00

I know is important to your boss what uh

## 33970:00 - 34010:00

era of Twitter was it at that point like

## 34010:00 - 34060:00

it was Kon run uh joined or and who was

## 34060:00 - 34090:00

the CE because there's been many so okay

## 34090:00 - 34140:00

yeah I started I I came in December 2016

## 34140:00 - 34180:00

so Jack had re relatively recently come

## 34180:00 - 34215:00

back as CEO to turn the company around

## 34215:00 - 34235:00

and just to give you a sense of like the

## 34235:00 - 34270:00

state of the company um something like a

## 34270:00 - 34300:00

third of employees were leaving every

## 34300:00 - 34330:00

year so just imagine like a a third of

## 34330:00 - 34370:00

your team gone every year um you know

## 34370:00 - 34415:00

the stock was in the toilet um the

## 34415:00 - 34485:00

product was not really growing um and so

## 34485:00 - 34530:00

uh Jack was working on a turnaround um

## 34530:00 - 34565:00

and Kon was there already Kon was

## 34565:00 - 34595:00

running Periscope with a bunch of video

## 34595:00 - 34665:00

stuff and you know that that group

## 34665:00 - 34700:00

continued to You Know Jack Jack was

## 34700:00 - 34760:00

there up through the start of the the

## 34760:00 - 34800:00

community not then Bird Watch Project

## 34800:00 - 34850:00

and yeah okay and it was called Bird

## 34850:00 - 34870:00

Watch I I don't think we've used that

## 34870:00 - 34890:00

term yet but that's an important point

## 34890:00 - 34925:00

it was called Bird Watch initially yeah

## 34925:00 - 34960:00

so it was originally called bird watch

## 34960:00 - 35015:00

when um uh when we started the project

## 35015:00 - 35050:00

but obviously somewhat famously the name

## 35050:00 - 35090:00

changed along the way yeah maybe it was

## 35090:00 - 35110:00

just tell that story real quick and I

## 35110:00 - 35145:00

know we're zooming in forward but just I

## 35145:00 - 35180:00

have this Twitter thread that I saw with

## 35180:00 - 35220:00

between Jack and Elon when they're

## 35220:00 - 35255:00

debating what to call it in elon's like

## 35255:00 - 35285:00

bird watch sounds creepy I want to

## 35285:00 - 35315:00

change it uh is there anything there you

## 35315:00 - 35350:00

can share yeah the story there the story

## 35350:00 - 35405:00

there is kind of funny um Elon Elon came

## 35405:00 - 35445:00

in acquired the company and you know we

## 35445:00 - 35480:00

had just launched the product relatively

## 35480:00 - 35505:00

recently us it had been in Pilot for a

## 35505:00 - 35550:00

year but we had just made it available

## 35550:00 - 35595:00

us-wide and he I guess he'd been seeing

## 35595:00 - 35670:00

the notes and um he is soon after soon

## 35670:00 - 35705:00

after the exhibition he dm' me and he

## 35705:00 - 35745:00

was like Hey this community notes thing

## 35745:00 - 35780:00

is awesome and I was like oh I'm glad

## 35780:00 - 35805:00

you like it like let's you know talk and

## 35805:00 - 35840:00

so we talked the next day and he kept

## 35840:00 - 35865:00

referring to it as this community notes

## 35865:00 - 35905:00

thing and I was like you know it's

## 35905:00 - 35945:00

interesting that you keep calling that

## 35945:00 - 35965:00

calling it that because because that's

## 35965:00 - 35995:00

actually the very first thing that I

## 35995:00 - 36045:00

called it like the very first figma

## 36045:00 - 36090:00

mockup I made depicting this thing was

## 36090:00 - 36125:00

called Community notes it just I don't

## 36125:00 - 36175:00

know why it just felt really natural and

## 36175:00 - 36200:00

so that's what we had that's the first

## 36200:00 - 36240:00

prototype we had tested uh you know

## 36240:00 - 36275:00

later the project changed it changed its

## 36275:00 - 36310:00

name to bird watch but you know Elon was

## 36310:00 - 36360:00

like hey let's just call it that and so

## 36360:00 - 36415:00

the next day we just changed the name

## 36415:00 - 36465:00

and uh you know it's it was a it's

## 36465:00 - 36505:00

always uh you're notable for the team

## 36505:00 - 36525:00

when you change your name but really the

## 36525:00 - 36560:00

the team was excited about it I think it

## 36560:00 - 36610:00

is a much more understandable name Jack

## 36610:00 - 36645:00

has made fun of it calling it uh like

## 36645:00 - 36675:00

the ultimate Facebook name or something

## 36675:00 - 36705:00

like that but the most boring Facebook

## 36705:00 - 36755:00

name Bor which is funny because they're

## 36755:00 - 36785:00

now you know launching Community notes

## 36785:00 - 36845:00

um but uh but I think it is a very

## 36845:00 - 36875:00

understandable intuative name and I

## 36875:00 - 36900:00

think it has served the product really

## 36900:00 - 36925:00

well there's there's a reason it was the

## 36925:00 - 36965:00

name in the very first markup I think

## 36965:00 - 37010:00

descriptive names just make sense uh

## 37010:00 - 37050:00

this uh connection with Elon and I want

## 37050:00 - 37070:00

to talk later about just how you've

## 37070:00 - 37095:00

dealt with so many strong personalities

## 37095:00 - 37125:00

over and kept this alive throughout so

## 37125:00 - 37170:00

many changes but before we get to that

## 37170:00 - 37205:00

um you you did something that I think a

## 37205:00 - 37245:00

lot of product leaders Eng leaders just

## 37245:00 - 37300:00

people that have managed people dream of

## 37300:00 - 37355:00

give up all this power in air quotes and

## 37355:00 - 37410:00

career trajectory and influence and just

## 37410:00 - 37435:00

like forget all that I'm going to go

## 37435:00 - 37455:00

back to just building something off

## 37455:00 - 37515:00

awesome small team is there any advice

## 37515:00 - 37545:00

there you could share from that

## 37545:00 - 37565:00

experience that you think might be

## 37565:00 - 37605:00

helpful for other leaders to share or to

## 37605:00 - 37650:00

hear to help them maybe do that same

## 37650:00 - 37675:00

jump because that's really difficult in

## 37675:00 - 37710:00

practice easy to talk about hard to do

## 37710:00 - 37755:00

yeah I think it is a difficult jump um

## 37755:00 - 37790:00

I've I've done it a bunch of times in my

## 37790:00 - 37820:00

career and I've always been very happy

## 37820:00 - 37850:00

with it where I started with a small

## 37850:00 - 37880:00

team that it kind of grew into something

## 37880:00 - 37930:00

bigger and then I was like you know this

## 37930:00 - 37950:00

is like we're kind of dealing with a lot

## 37950:00 - 37980:00

of B production stuff teams really big I

## 37980:00 - 38000:00

want to go back to do something like

## 38000:00 - 38030:00

crazy and new with a small team again

## 38030:00 - 38060:00

and so I've kind of done that like saw

## 38060:00 - 38105:00

teeth leap um a bunch of times but it

## 38105:00 - 38135:00

can be hard because certainly the

## 38135:00 - 38200:00

natural like the classic career path is

## 38200:00 - 38260:00

sort of I don't know Rewards or uh you

## 38260:00 - 38305:00

know running a large organization or

## 38305:00 - 38350:00

being a manager or things like that but

## 38350:00 - 38380:00

I think at the end of the day you got to

## 38380:00 - 38420:00

work on stuff you love you got to be

## 38420:00 - 38455:00

having fun and you I think people want

## 38455:00 - 38510:00

be having impact and I think there's one

## 38510:00 - 38545:00

myth that that can get in people's way

## 38545:00 - 38580:00

is the idea that the the more people you

## 38580:00 - 38605:00

manage or something or the larger your

## 38605:00 - 38635:00

scope is the more impact you have I

## 38635:00 - 38685:00

definitely do not think that is true um

## 38685:00 - 38730:00

if you just look at I mean look at

## 38730:00 - 38760:00

Community notes for example if I had

## 38760:00 - 38825:00

stayed running a large consumer PM team

## 38825:00 - 38860:00

like what would I have produced like 16

## 38860:00 - 38895:00

more pages of okrs like I don't know you

## 38895:00 - 38935:00

know a bunch of documents and I think

## 38935:00 - 38965:00

building Community notes has had had way

## 38965:00 - 39010:00

bigger impact on the world it's become

## 39010:00 - 39040:00

the industry standard for how to deal

## 39040:00 - 39075:00

with this now which is super cool people

## 39075:00 - 39095:00

love it it's the first thing that is

## 39095:00 - 39140:00

plausibly dealing with the internet

## 39140:00 - 39170:00

scale you know issue of information

## 39170:00 - 39220:00

quality um you know I I think it's

## 39220:00 - 39245:00

unquestionably a bigger impact than I

## 39245:00 - 39270:00

would have had if I were just do

## 39270:00 - 39300:00

whatever doing some standard management

## 39300:00 - 39350:00

track thing like I was doing before and

## 39350:00 - 39390:00

I think that's true of so many other uh

## 39390:00 - 39415:00

you know small companies and and

## 39415:00 - 39460:00

startups I I was just reading

## 39460:00 - 39495:00

screenshot it I think it's Blake scholes

## 39495:00 - 39525:00

uh LinkedIn the other day who went from

## 39525:00 - 39575:00

like director of coupons or something to

## 39575:00 - 39630:00

building the first uh supersonic from

## 39630:00 - 39685:00

group on yeah yeah yeah and I you know

## 39685:00 - 39725:00

those stories are everywhere when you

## 39725:00 - 39760:00

look and so I definitely have found that

## 39760:00 - 39795:00

you know for me I love building Hands-On

## 39795:00 - 39840:00

I love trying crazy new ideas I I love

## 39840:00 - 39870:00

the zero to one experience it's fun to

## 39870:00 - 39890:00

scale things up to and it can be fun to

## 39890:00 - 39950:00

operate it you know it's scale but um

## 39950:00 - 39995:00

doesn't you you know this team is a good

## 39995:00 - 40015:00

example of one that operates at a very

## 40015:00 - 40055:00

large scale but that is still very small

## 40055:00 - 40095:00

yeah I think the way you guys operate is

## 40095:00 - 40125:00

what more and more companies are trying

## 40125:00 - 40185:00

to do uh remove middle management layers

## 40185:00 - 40215:00

create small teams that just execute and

## 40215:00 - 40265:00

build impact and just like ic's uh

## 40265:00 - 40290:00

whenever I say IC I have a comment on

## 40290:00 - 40320:00

YouTube like what is IC so I'm just

## 40320:00 - 40345:00

gonna explain individual contributor

## 40345:00 - 40380:00

non- manager is when I say the word I

## 40380:00 - 40430:00

see so let me follow this thread and

## 40430:00 - 40460:00

when I asked people about how you you

## 40460:00 - 40505:00

set up the team to operate effectively

## 40505:00 - 40550:00

and and protect it initially there's

## 40550:00 - 40585:00

this term thermal that came up a lot

## 40585:00 - 40610:00

they was like a thermal team if that's

## 40610:00 - 40655:00

how you describe it yeah what is thermal

## 40655:00 - 40700:00

yeah so um anyone who's worked in a

## 40700:00 - 40720:00

larger company probably knows that

## 40720:00 - 40745:00

things can get kind of bureaucratic or

## 40745:00 - 40790:00

bogged down decision- making can be slow

## 40790:00 - 40820:00

like there's these large planning Cycles

## 40820:00 - 40850:00

people can like try to like take someone

## 40850:00 - 40880:00

from one team move to another like at

## 40880:00 - 40905:00

random arbitrary times that can disrupt

## 40905:00 - 40935:00

a project like all sorts of things like

## 40935:00 - 40965:00

that um

## 40965:00 - 41000:00

uh you know our company this is you

## 41000:00 - 41020:00

number of years ago when we started this

## 41020:00 - 41055:00

project um we had a lot of Founders in

## 41055:00 - 41080:00

the company like Kavon is an example

## 41080:00 - 41105:00

founder who was helping to run the

## 41105:00 - 41160:00

company and he had this idea like hey

## 41160:00 - 41200:00

why don't we create this program called

## 41200:00 - 41240:00

it thermal where we could have teams

## 41240:00 - 41275:00

that were somewhat isolated from that

## 41275:00 - 41310:00

they could run on through their own

## 41310:00 - 41340:00

process they would have like one clear

## 41340:00 - 41380:00

owner the team would be entirely

## 41380:00 - 41440:00

dedicated to that project and uh we

## 41440:00 - 41465:00

would just sort of repeatedly make

## 41465:00 - 41495:00

funding decisions as to whether to

## 41495:00 - 41525:00

continue the effort and so why was it

## 41525:00 - 41545:00

called thermal by the way what was the

## 41545:00 - 41575:00

idea there I think the I think it was

## 41575:00 - 41625:00

like an an old bird analogy of like

## 41625:00 - 41660:00

thermals lifting you know the the birds

## 41660:00 - 41700:00

on their wings Twitter obvious s 1.0

## 41700:00 - 41735:00

obviously had a lot of bird analogies

## 41735:00 - 41780:00

blessed heart uh and so you know that

## 41780:00 - 41825:00

was one of them um but the you know the

## 41825:00 - 41895:00

idea uh I loved the idea as someone who

## 41895:00 - 41935:00

you know liked the startup environment

## 41935:00 - 41965:00

and so when we were starting this

## 41965:00 - 42000:00

project I was like Hey Kayon like why

## 42000:00 - 42025:00

don't we make this the first thermal

## 42025:00 - 42060:00

project and he was like yeah let's do it

## 42060:00 - 42100:00

and so so we started with that way of

## 42100:00 - 42140:00

operating and it gave us you know from

## 42140:00 - 42150:00

day

## 42150:00 - 42205:00

one a lot of freedom and autonomy that I

## 42205:00 - 42235:00

think was really important to make the

## 42235:00 - 42270:00

product work so just be very specific

## 42270:00 - 42300:00

about what what make it a what makes it

## 42300:00 - 42335:00

a thermal project how do you set that up

## 42335:00 - 42365:00

and this is asking from a perspective if

## 42365:00 - 42390:00

a company wants to build their own

## 42390:00 - 42405:00

something like this what does that look

## 42405:00 - 42435:00

like yeah I think there's a bunch of key

## 42435:00 - 42475:00

attributes so keep one one key attribute

## 42475:00 - 42520:00

is um there's one clear driver of the

## 42520:00 - 42565:00

project who's effectively like founder

## 42565:00 - 42585:00

um I guess I mean maybe you get have two

## 42585:00 - 42605:00

or something but like it's like really

## 42605:00 - 42650:00

clear there's like driver of the project

## 42650:00 - 42680:00

and also there's one clear decision

## 42680:00 - 42730:00

maker that they go to oh outside of the

## 42730:00 - 42760:00

team outside of the team and that was

## 42760:00 - 42805:00

true back when we started and it is true

## 42805:00 - 42825:00

now like if

## 42825:00 - 42870:00

we need need something or have a

## 42870:00 - 42900:00

question about something I talked to

## 42900:00 - 42940:00

Elon and it you know it was like that

## 42940:00 - 42965:00

from the beginning like that now I think

## 42965:00 - 42985:00

that's a big reason we're able to make

## 42985:00 - 43030:00

decisions effectively quickly um in a

## 43030:00 - 43055:00

simple way and it probably has to be

## 43055:00 - 43095:00

someone very senior not yes it needs to

## 43095:00 - 43125:00

be some someone senior who can make the

## 43125:00 - 43160:00

decisions you need made whatever they

## 43160:00 - 43195:00

are so I think that's really important

## 43195:00 - 43230:00

that clear decision-making structure

## 43230:00 - 43290:00

another was 100% Focus so everyone on

## 43290:00 - 43325:00

the project is expected to be totally

## 43325:00 - 43400:00

focused on it um that at a lot of

## 43400:00 - 43430:00

companies it can be easy to have

## 43430:00 - 43465:00

people's attention sort of spread across

## 43465:00 - 43510:00

a bunch of things and it makes it hard

## 43510:00 - 43570:00

to get stuff done like you'll go to like

## 43570:00 - 43590:00

you'll try talk to who you know whoever

## 43590:00 - 43615:00

that person is you'll ask them for help

## 43615:00 - 43640:00

on something and they'll be like yeah

## 43640:00 - 43675:00

I'll help you I got to finish this thing

## 43675:00 - 43695:00

you know and it'll take me like a week

## 43695:00 - 43720:00

or two and then I'll get to it and like

## 43720:00 - 43765:00

a week or two delay totally changes the

## 43765:00 - 43790:00

momentum of a project when you know we

## 43790:00 - 43845:00

were 100% focused you we talk we talk in

## 43845:00 - 43870:00

the morning it's like hey Jay why don't

## 43870:00 - 43890:00

we like try this thing on the algorith

## 43890:00 - 43920:00

he's like yeah then like then you know

## 43920:00 - 43950:00

that afternoon or the next day we're

## 43950:00 - 43990:00

looking at results and so because of

## 43990:00 - 44035:00

that total focus the rate of iteration

## 44035:00 - 44085:00

goes way up and then you know beyond

## 44085:00 - 44130:00

that there was uh also just the ability

## 44130:00 - 44175:00

to use whatever our own sort of like

## 44175:00 - 44215:00

decision-making process was we didn't

## 44215:00 - 44245:00

need to write

## 44245:00 - 44285:00

okrs or you know follow others like

## 44285:00 - 44320:00

standard practices obviously like we had

## 44320:00 - 44350:00

to make sure we were respons responsibly

## 44350:00 - 44380:00

building the product and everything but

## 44380:00 - 44415:00

you we didn't use need to use standard

## 44415:00 - 44440:00

um the standard practices and I think

## 44440:00 - 44475:00

that's a another great example like okrs

## 44475:00 - 44525:00

I understand why they can be helpful um

## 44525:00 - 44575:00

but they can also be um you know not

## 44575:00 - 44600:00

necessarily the right Cadence at which

## 44600:00 - 44630:00

to set goals like I don't I think it's

## 44630:00 - 44660:00

really unclear that quarterly or annual

## 44660:00 - 44705:00

goals are actually like the right pace

## 44705:00 - 44765:00

like we would set our goals for what

## 44765:00 - 44790:00

like we would set the goal for the next

## 44790:00 - 44820:00

Milestone that mattered and we would

## 44820:00 - 44840:00

work on that and when we reach that

## 44840:00 - 44870:00

Milestone we would have an idea of what

## 44870:00 - 44895:00

was coming after and then we when we hit

## 44895:00 - 44925:00

that we'd set the next Milestone whether

## 44925:00 - 44970:00

that was two weeks a month month three

## 44970:00 - 45000:00

months like what whatever it was like we

## 45000:00 - 45035:00

set our own pace and and goals at that

## 45035:00 - 45065:00

pace and that just I think is a lot more

## 45065:00 - 45100:00

natural for the development of something

## 45100:00 - 45135:00

the the whole okr determination and

## 45135:00 - 45175:00

planning process took longer than it

## 45175:00 - 45205:00

would take us to pick a goal and then

## 45205:00 - 45230:00

execute it on it and finish

## 45230:00 - 45280:00

it how big was the team early on uh that

## 45280:00 - 45330:00

you set up how many Engineers it started

## 45330:00 - 45385:00

with just me and then we when we decided

## 45385:00 - 45430:00

to build the thing it we we figured we

## 45430:00 - 45470:00

needed about five um we wanted to be as

## 45470:00 - 45495:00

small as we possibly could it was clear

## 45495:00 - 45555:00

we needed someone on ML doing scoring it

## 45555:00 - 45590:00

was clear we needed someone to do some

## 45590:00 - 45615:00

client engineering work someone to do

## 45615:00 - 45670:00

backend engineering work um there may

## 45670:00 - 45690:00

have been like you know one or two other

## 45690:00 - 45735:00

oh we needed a designer and um a

## 45735:00 - 45785:00

researcher to help us understand the

## 45785:00 - 45830:00

customer base and make sure we were we

## 45830:00 - 45855:00

were building the thing in a way that

## 45855:00 - 45880:00

was actually going to to resonate with

## 45880:00 - 45905:00

people and so I think that was I think

## 45905:00 - 45965:00

it was like back end front end uh ml

## 45965:00 - 45990:00

design research that was that was the

## 45990:00 - 46020:00

original team from what I remember

## 46020:00 - 46050:00

amazing so one basically one of each

## 46050:00 - 46080:00

function a question I have for Jay

## 46080:00 - 46110:00

actually is there's all this talk of

## 46110:00 - 46165:00

small teams and uh moving fast but you

## 46165:00 - 46185:00

know sometimes you just need more

## 46185:00 - 46220:00

Engineers to build a thing is there

## 46220:00 - 46240:00

anything you've learned about just how

## 46240:00 - 46280:00

to keep a team small while moving as

## 46280:00 - 46335:00

fast as you are and not need we need to

## 46335:00 - 46360:00

hire more engineers and need to more

## 46360:00 - 46390:00

Engineers I think in the in the

## 46390:00 - 46420:00

beginning when we were iterating uh you

## 46420:00 - 46445:00

know what what should even the require

## 46445:00 - 46495:00

requirements be um it was it was

## 46495:00 - 46530:00

definitely good to just have it you know

## 46530:00 - 46570:00

like one ml engineer but I think at some

## 46570:00 - 46620:00

point we got clear on what the goals of

## 46620:00 - 46645:00

the the algorithm should really be and

## 46645:00 - 46675:00

we try you know we were really I think

## 46675:00 - 46700:00

at the very beginning it wasn't clear

## 46700:00 - 46745:00

that we needed to build this bridging

## 46745:00 - 46790:00

based uh algorithm right the actual

## 46790:00 - 46830:00

first algorithm that I put into

## 46830:00 - 46850:00

production was very focused on

## 46850:00 - 46880:00

anti-manipulation it was this kind of

## 46880:00 - 46930:00

page rank variant uh but it didn't solve

## 46930:00 - 46980:00

the problem of you know bias basically

## 46980:00 - 47010:00

so if if there's some if there are more

## 47010:00 - 47055:00

users on one side the a pag rank type

## 47055:00 - 47080:00

graph algorithm can actually amplify

## 47080:00 - 47120:00

those biases so I think you know after

## 47120:00 - 47150:00

building that prototype and and getting

## 47150:00 - 47205:00

data from that it was clear that you

## 47205:00 - 47250:00

know uh the the bridging based algorithm

## 47250:00 - 47280:00

was going to be the way that we needed

## 47280:00 - 47330:00

to solve it and at that point basically

## 47330:00 - 47380:00

uh I set up a a Bake Off basically made

## 47380:00 - 47425:00

you know this this kind of like the you

## 47425:00 - 47465:00

know Kangle competition or something so

## 47465:00 - 47510:00

that was like the key time uh where it

## 47510:00 - 47550:00

was really important to pull in other

## 47550:00 - 47605:00

Engineers that is such a cool story uh I

## 47605:00 - 47630:00

want to follow that thread before we do

## 47630:00 - 47680:00

that you mention you guys yell thermal

## 47680:00 - 47705:00

what does that mean is that like YOLO

## 47705:00 - 47735:00

like a version of just okay we're just

## 47735:00 - 47770:00

gonna ship because we're thermal project

## 47770:00 - 47825:00

ship it

## 47825:00 - 47875:00

okay marketers I know that you love TS

## 47875:00 - 47910:00

so let me get right to the point Wick

## 47910:00 - 47940:00

Studio gives you everything you need to

## 47940:00 - 47985:00

cater to any client at any scale all in

## 47985:00 - 48015:00

one place here's how your workflow could

## 48015:00 - 48050:00

look scale content with Dynamic pages

## 48050:00 - 48090:00

and reusable assets effortlessly

## 48090:00 - 48110:00

FastTrack projects with built-in

## 48110:00 - 48150:00

marketing Integrations like meta Capi

## 48150:00 - 48190:00

zapier Google ads and more AB test

## 48190:00 - 48225:00

landing pages in days not weeks with

## 48225:00 - 48260:00

intuitive design tools connected

## 48260:00 - 48295:00

tracking and analytics tools like Google

## 48295:00 - 48340:00

analytics and semrush and capture key

## 48340:00 - 48370:00

business events without the hassle of

## 48370:00 - 48405:00

manual setup manage all your client

## 48405:00 - 48430:00

social media and Communications from a

## 48430:00 - 48470:00

unified dashboard then create schedule

## 48470:00 - 48500:00

and post content across all their

## 48500:00 - 48530:00

channels if you're working on content

## 48530:00 - 48570:00

Rich sites Wick Studio no code CMS lets

## 48570:00 - 48590:00

you build and manage without touching

## 48590:00 - 48620:00

the design and when you're ready for

## 48620:00 - 48655:00

more Wix Studio grows with you add your

## 48655:00 - 48690:00

own code create custom Integrations with

## 48690:00 - 48735:00

Wix made apis or leverage robust native

## 48735:00 - 48770:00

Business Solutions drive real client

## 48770:00 - 48805:00

growth with Wix Studio go to Wix

## 48805:00 - 48855:00

studio.com

## 48855:00 - 48890:00

okay so coming back to this algorithm

## 48890:00 - 48905:00

this is actually really interesting

## 48905:00 - 48935:00

because I I've never heard any of this I

## 48935:00 - 48975:00

was going to ask just what inspired this

## 48975:00 - 49015:00

actual algorithm and you basically did

## 49015:00 - 49045:00

an internal competition amongst ml

## 49045:00 - 49075:00

Engineers to see you had the most

## 49075:00 - 49100:00

successful algorithm

## 49100:00 - 49160:00

Netflix contest style cackle style yeah

## 49160:00 - 49195:00

yeah I I think so I mean this particular

## 49195:00 - 49250:00

idea of of finding you know content that

## 49250:00 - 49295:00

is liked by people on opposite sides of

## 49295:00 - 49325:00

of a polarized divider who who typically

## 49325:00 - 49370:00

disagree know this was not an an idea

## 49370:00 - 49420:00

out of thin air right like I think Keith

## 49420:00 - 49450:00

had found some of Chris Bills work he

## 49450:00 - 49485:00

had done he had you know made this list

## 49485:00 - 49515:00

of accounts that were often liked by

## 49515:00 - 49560:00

people who uh you know were on both

## 49560:00 - 49615:00

sides politically um there is um you

## 49615:00 - 49660:00

know other other projects like uh polus

## 49660:00 - 49695:00

out there that that look for agreement

## 49695:00 - 49740:00

among uh you know people who typically

## 49740:00 - 49805:00

disagree but I think the yeah it wasn't

## 49805:00 - 49850:00

obvious that our project definitely

## 49850:00 - 49870:00

needed to use that from the very

## 49870:00 - 49905:00

beginning but then you know when you

## 49905:00 - 49925:00

when you implement it and compare it

## 49925:00 - 49955:00

against these other type like page rank

## 49955:00 - 49995:00

seems obviously you know it's designed

## 49995:00 - 50015:00

to be kind of manipulation resistant

## 50015:00 - 50055:00

it's naturally naturally like if you

## 50055:00 - 50090:00

just have a voting ring of people who

## 50090:00 - 50130:00

all vote them themselves up then page

## 50130:00 - 50175:00

rank can filter that out very well but

## 50175:00 - 50220:00

like that just wasn't the main attack

## 50220:00 - 50260:00

Vector I guess so we got we had to get

## 50260:00 - 50290:00

some real data from the pilot to realize

## 50290:00 - 50325:00

that okay the real thing going on here

## 50325:00 - 50380:00

is people are polarized and uh and and

## 50380:00 - 50425:00

so it was only once we got that uh the

## 50425:00 - 50460:00

the real data from the pilot that I

## 50460:00 - 50500:00

think it was it was clear that the the

## 50500:00 - 50540:00

brid based algorithm was was was um the

## 50540:00 - 50575:00

direction we really needs to go I want

## 50575:00 - 50615:00

to come back to the way you operate the

## 50615:00 - 50645:00

team I hear that you run the whole team

## 50645:00 - 50685:00

off a single Google doc that's like a

## 50685:00 - 50710:00

four-year-old doc that you just keep

## 50710:00 - 50760:00

adding uh goals to bullet points is that

## 50760:00 - 50810:00

true there there is a very long running

## 50810:00 - 50865:00

dock um that has had to be uh chopped

## 50865:00 - 50890:00

and purged because it was breaking

## 50890:00 - 50920:00

Google Docs and chrome at various points

## 50920:00 - 50960:00

in time it sort of of like a note taking

## 50960:00 - 51015:00

dock um it's really where we coordinate

## 51015:00 - 51045:00

what we're doing um the team meets on a

## 51045:00 - 51090:00

daily basis um we spend whatever amount

## 51090:00 - 51125:00

of time we need to get on the same page

## 51125:00 - 51160:00

about what we're building it can be you

## 51160:00 - 51195:00

we might talk about anything from you

## 51195:00 - 51245:00

know what's most important right now to

## 51245:00 - 51290:00

what are what should we work on next to

## 51290:00 - 51320:00

what are we trying to launch right now

## 51320:00 - 51355:00

and why is it not launch like what's in

## 51355:00 - 51385:00

the way of launching it and we might

## 51385:00 - 51430:00

review uh new modeling or scoring

## 51430:00 - 51465:00

algorithm up and you know try to

## 51465:00 - 51490:00

understand what's working in it what's

## 51490:00 - 51525:00

not um so we'll just cover whatever we

## 51525:00 - 51570:00

want and um or whatever feels most

## 51570:00 - 51615:00

important and we like you know as you

## 51615:00 - 51660:00

said we set our goals very dynamically

## 51660:00 - 51695:00

um so it's whatever seems like the most

## 51695:00 - 51730:00

important thing for us to work on now

## 51730:00 - 51775:00

and next is what we spend our time on I

## 51775:00 - 51800:00

think that served the project really

## 51800:00 - 51850:00

well um versus how feeling attached to

## 51850:00 - 51885:00

like some kind of quarterly goals or

## 51885:00 - 51920:00

something like well look at like what is

## 51920:00 - 51945:00

going to help people the most or like

## 51945:00 - 51970:00

what's the biggest problem right now

## 51970:00 - 52000:00

what are either one of those and we will

## 52000:00 - 52040:00

go tackle it and we can we might change

## 52040:00 - 52085:00

our road map you know multiple times in

## 52085:00 - 52135:00

two weeks based on what we see so I'm

## 52135:00 - 52190:00

hearing no jira no sauna no monday.com

## 52190:00 - 52235:00

no okay yeah I mean we we have to use

## 52235:00 - 52260:00

jira to like coordinate with some other

## 52260:00 - 52290:00

teams like sometimes when we file a

## 52290:00 - 52320:00

request we have to make a jira ticket

## 52320:00 - 52375:00

but no I I am not a fan of heavyweight

## 52375:00 - 52420:00

task management I love like being on the

## 52420:00 - 52450:00

same page being able to keep most things

## 52450:00 - 52485:00

in my head and having a really light way

## 52485:00 - 52520:00

to write down the things that you know I

## 52520:00 - 52555:00

can't or the team can't keep in its head

## 52555:00 - 52620:00

we we did use a SAA briefly um but my

## 52620:00 - 52660:00

memory of it is that it spent you you

## 52660:00 - 52690:00

spent more time in the meeting grooming

## 52690:00 - 52740:00

a backlog of irrelevant stuff than

## 52740:00 - 52785:00

actually you know talking about the the

## 52785:00 - 52830:00

proper priorities um so I think it's

## 52830:00 - 52855:00

nice in the Google Doc that if something

## 52855:00 - 52900:00

becomes relevant it can kind of just

## 52900:00 - 52940:00

fall off without needing explicit

## 52940:00 - 52980:00

backlog grooming so just to maybe

## 52980:00 - 53015:00

summarize a little bit of how you guys

## 53015:00 - 53040:00

operate that might Inspire other

## 53040:00 - 53085:00

companies to set teams up like this uh

## 53085:00 - 53105:00

so I'm going to go through a few things

## 53105:00 - 53150:00

that you shared one is one person in

## 53150:00 - 53180:00

charge of the team like the founder

## 53180:00 - 53205:00

almost they're like basically the

## 53205:00 - 53250:00

founder of the team they have one very

## 53250:00 - 53295:00

senior essentially sponsor decision

## 53295:00 - 53325:00

maker that they interface with in your

## 53325:00 - 53360:00

case Elon no big deal in other cases it

## 53360:00 - 53420:00

could be the CTO CPO someone like that

## 53420:00 - 53455:00

uh the team is focused 100% on this

## 53455:00 - 53515:00

product and and and goal you uh keep the

## 53515:00 - 53555:00

team very small so you start with one

## 53555:00 - 53580:00

person of each function one front

## 53580:00 - 53615:00

engineer back in ml person designer

## 53615:00 - 53635:00

researcher

## 53635:00 - 53710:00

yeah and then uh Google Docs almost

## 53710:00 - 53755:00

basically for your project management is

## 53755:00 - 53780:00

that roughly like yeah it's basically

## 53780:00 - 53810:00

running with Google Docs stop don't use

## 53810:00 - 53845:00

big complicated products I think that's

## 53845:00 - 53870:00

a pretty good recipe on the Google Docs

## 53870:00 - 53895:00

you know take it people can do what they

## 53895:00 - 53925:00

want if they want something else go for

## 53925:00 - 53955:00

it I think those those first ingredients

## 53955:00 - 54005:00

are really are are key structurally and

## 54005:00 - 54035:00

then you know beyond that it's a matter

## 54035:00 - 54060:00

of having an ambitious goal that gets

## 54060:00 - 54125:00

people fired up to go do great work yeah

## 54125:00 - 54150:00

uh awesome I think there's a lot there

## 54150:00 - 54175:00

that a lot of people kind of like think

## 54175:00 - 54200:00

they should do and they set these teams

## 54200:00 - 54220:00

up but they don't actually do and it

## 54220:00 - 54250:00

feels like each of these is just a

## 54250:00 - 54275:00

really key ingredient to actually

## 54275:00 - 54315:00

succeeding it definitely really helped

## 54315:00 - 54350:00

us succeed I don't know that the project

## 54350:00 - 54375:00

would be here if it was not for some of

## 54375:00 - 54420:00

those elements that's that's a powerful

## 54420:00 - 54450:00

statement like this thing that has

## 54450:00 - 54480:00

changed the way the world understands

## 54480:00 - 54505:00

what is true would not have existed if

## 54505:00 - 54550:00

you didn't set it up in this specific

## 54550:00 - 54600:00

way yeah I think uh you know I I don't

## 54600:00 - 54630:00

know if I would have start would have

## 54630:00 - 54675:00

begun the project had I not known we had

## 54675:00 - 54710:00

sort of that structure that ability to

## 54710:00 - 54745:00

make decisions the autonomy the the

## 54745:00 - 54810:00

speed the ability to go fast and you

## 54810:00 - 54855:00

know working we we started with that in

## 54855:00 - 54915:00

1.0 and and it's been continued and if

## 54915:00 - 54955:00

anything furthered in and X I mean X as

## 54955:00 - 54985:00

a whole company operates with a lot of

## 54985:00 - 55055:00

those attributes and um I think it's

## 55055:00 - 55080:00

it's one of the reasons the product is

## 55080:00 - 55110:00

successful I think it's a big those are

## 55110:00 - 55145:00

big reasons why at least I Jaye can

## 55145:00 - 55180:00

speak for himself I have so much fun

## 55180:00 - 55240:00

working on this like I I I love working

## 55240:00 - 55270:00

on it you know it's great to wake up

## 55270:00 - 55310:00

every day and solve these problems we

## 55310:00 - 55330:00

get to you know we get to do them

## 55330:00 - 55370:00

efficiently make decisions quickly build

## 55370:00 - 55395:00

stuff that helps a lot of people it's

## 55395:00 - 55440:00

it's awesome yeah this this like uh

## 55440:00 - 55480:00

whether thermal or Eon way of operating

## 55480:00 - 55520:00

is definitely more fun and and the fact

## 55520:00 - 55565:00

that like that combined with the the

## 55565:00 - 55600:00

awesome mission is super important for

## 55600:00 - 55650:00

internal recruiting like I remember uh

## 55650:00 - 55680:00

like when I was first chatting to Keith

## 55680:00 - 55730:00

about this back in early 2020 you know I

## 55730:00 - 55770:00

had another project I was you know it

## 55770:00 - 55815:00

work on a few but one one was like

## 55815:00 - 55835:00

personalizing the number of push

## 55835:00 - 55875:00

notifications that we send uh and it was

## 55875:00 - 55920:00

it drove a lot of diu um without like

## 55920:00 - 55945:00

losing opt outs

## 55945:00 - 56000:00

uh uh significantly uh so you know that

## 56000:00 - 56045:00

that was like setting me on track uh or

## 56045:00 - 56070:00

you know if IID kept working on that I

## 56070:00 - 56100:00

could have probably gotten a promotion

## 56100:00 - 56140:00

from that with low risk or I could take

## 56140:00 - 56180:00

this huge career I mean it's not as big

## 56180:00 - 56215:00

at a career risk as like joining or

## 56215:00 - 56255:00

founding an actual external startup but

## 56255:00 - 56290:00

there is still career risk I guess and

## 56290:00 - 56330:00

joining a team like this so so just I

## 56330:00 - 56365:00

think all the same aspects of recruiting

## 56365:00 - 56395:00

that apply to external startups apply

## 56395:00 - 56425:00

internally and and you know if you can

## 56425:00 - 56445:00

have

## 56445:00 - 56500:00

an exciting Vision that uh is key

## 56500:00 - 56545:00

related to that and your list Lenny one

## 56545:00 - 56595:00

thing we missed that's super important

## 56595:00 - 56645:00

is that on this project and I think of

## 56645:00 - 56680:00

successful projects like in startups is

## 56680:00 - 56735:00

that people are self- selecting to join

## 56735:00 - 56795:00

we did not assign anyone to this project

## 56795:00 - 56840:00

like people reached out to join or they

## 56840:00 - 56890:00

applied to join the job you know I and

## 56890:00 - 56925:00

the team interviewed every single person

## 56925:00 - 56955:00

that joined the team and we're like we

## 56955:00 - 56980:00

want that person on the team they want

## 56980:00 - 57035:00

to be on the team and so people are

## 57035:00 - 57090:00

totally bought in to the goal Mission

## 57090:00 - 57120:00

the way the team works the other people

## 57120:00 - 57135:00

they're going to be working with and

## 57135:00 - 57190:00

that makes a huge difference so OB like

## 57190:00 - 57220:00

a great time to do that is at the start

## 57220:00 - 57245:00

of one of these things like don't if

## 57245:00 - 57270:00

you're going to try something crazy like

## 57270:00 - 57295:00

I would it's GNA be tough if you're just

## 57295:00 - 57320:00

assigning random people to it but if you

## 57320:00 - 57360:00

let people opt in and self- select

## 57360:00 - 57395:00

you're much more likely to be successful

## 57395:00 - 57450:00

and one thing that I have observed at X

## 57450:00 - 57485:00

which really surprised me was that this

## 57485:00 - 57540:00

is also possible at a large scale you

## 57540:00 - 57570:00

know one of the things Elon did when he

## 57570:00 - 57600:00

bought the company was he basically

## 57600:00 - 57630:00

asked people to self- select to stay

## 57630:00 - 57665:00

like you had you had to click the button

## 57665:00 - 57700:00

and you he sent an email out that was

## 57700:00 - 57745:00

like Hey Twitter 2.0 like Fork fork in

## 57745:00 - 57780:00

the road right fork in the road fork in

## 57780:00 - 57835:00

the road exactly he like Twitter 2.0 you

## 57835:00 - 57865:00

know now X it's going to be hardcore

## 57865:00 - 57890:00

we're going to do ambitious things

## 57890:00 - 57915:00

you're going to work your butt off you

## 57915:00 - 57955:00

know what and you had to click on the

## 57955:00 - 58020:00

form and say Yes I want to join and I

## 58020:00 - 58060:00

think that was really important for the

## 58060:00 - 58110:00

company because you want people to opt

## 58110:00 - 58135:00

into that you want that people to be

## 58135:00 - 58155:00

saying like yeah that's what I want to

## 58155:00 - 58180:00

do and the company's going to be a lot

## 58180:00 - 58210:00

more successful if people aren't sure

## 58210:00 - 58240:00

it's like better for them probably to go

## 58240:00 - 58270:00

do something else and where they're

## 58270:00 - 58310:00

naturally more aligned and happier

## 58310:00 - 58355:00

and I thought that was a great approach

## 58355:00 - 58395:00

to taking a large company and getting it

## 58395:00 - 58420:00

down to people who are really excited

## 58420:00 - 58450:00

about you know working together on a on

## 58450:00 - 58480:00

a mission so you know for us we did it

## 58480:00 - 58510:00

from day one which I think is an easy

## 58510:00 - 58530:00

way to do it but it's possible to do it

## 58530:00 - 58570:00

later as well I love that you described

## 58570:00 - 58615:00

it as fun and I think a lot of people

## 58615:00 - 58655:00

when they see Elon laying off a bunch of

## 58655:00 - 58705:00

people being like very hardcore himself

## 58705:00 - 58740:00

it's people don't imagine it as a fun

## 58740:00 - 58775:00

place to work and it's clear how much

## 58775:00 - 58805:00

you guys love working on this like how

## 58805:00 - 58855:00

fun it is and how interesting it is and

## 58855:00 - 58875:00

it's interesting to hear that because I

## 58875:00 - 58905:00

think a lot of people don't feel that

## 58905:00 - 58935:00

externally is there anything else along

## 58935:00 - 58965:00

the lines of just working for Elon

## 58965:00 - 59000:00

within an org Elon runs that may

## 59000:00 - 59025:00

surprise people about just the way of

## 59025:00 - 59055:00

working that's interesting or surprising

## 59055:00 - 59090:00

or where you think other companies might

## 59090:00 - 59110:00

want to think about

## 59110:00 - 59160:00

adopting I've always liked lean teams

## 59160:00 - 59225:00

but this has made me my my experience at

## 59225:00 - 59275:00

X has made me change the way I would I

## 59275:00 - 59300:00

would think about running a future or

## 59300:00 - 59320:00

you know if I were start a company and

## 59320:00 - 59340:00

change the way I think about starting

## 59340:00 - 59365:00

that company it would be even leaner

## 59365:00 - 59400:00

than I would have made it before I've

## 59400:00 - 59445:00

been amazed with just how much the team

## 59445:00 - 59495:00

is able to accomplish um with a small

## 59495:00 - 59525:00

group and I think because of a small

## 59525:00 - 59575:00

group like when shortly after the

## 59575:00 - 59610:00

acquisition um we had this product

## 59610:00 - 59660:00

called spaces um it was it had been in

## 59660:00 - 59685:00

the product before but it was it was

## 59685:00 - 59755:00

pretty small scale and Elon wanted to

## 59755:00 - 59790:00

run these large spaces I forget who the

## 59790:00 - 59815:00

first people he was going to bring on

## 59815:00 - 59840:00

were but he was going to be there you

## 59840:00 - 59860:00

know ultimately these things have gone

## 59860:00 - 59895:00

on to host politicians and things like

## 59895:00 - 59930:00

that and he's like guys we got to scale

## 59930:00 - 59970:00

this up I forget the number he like I we

## 59970:00 - 59990:00

need to be able to scale like a million

## 59990:00 - 60005:00

people or something like that I'm

## 60005:00 - 60030:00

getting the numbers wrong you be able to

## 60030:00 - 60075:00

scale way up this is the kind of thing

## 60075:00 - 60120:00

at 1.0 that would have taken a year if

## 60120:00 - 60160:00

it had ever happened and the team did it

## 60160:00 - 60230:00

in like two or three weeks and uh it was

## 60230:00 - 60265:00

really exciting and inspiring to see

## 60265:00 - 60290:00

like we I didn't work on that but I

## 60290:00 - 60325:00

watched it from the outside I'm like wow

## 60325:00 - 60375:00

with this tiny team motivated behind a

## 60375:00 - 60405:00

big goal that was like hey guys it's not

## 60405:00 - 60435:00

like are we going to do this it's we are

## 60435:00 - 60460:00

going to do this they got it done in two

## 60460:00 - 60490:00

or three weeks that must have felt

## 60490:00 - 60515:00

amazing for them it was certainly

## 60515:00 - 60565:00

exciting to see um but it's I I

## 60565:00 - 60610:00

definitely come to appreciate just how

## 60610:00 - 60650:00

um lean something can be and and not

## 60650:00 - 60680:00

just get by but actually Thrive because

## 60680:00 - 60720:00

it's that lean I think the point you

## 60720:00 - 60750:00

made about people opting into that is

## 60750:00 - 60765:00

important because I think a lot of

## 60765:00 - 60790:00

people hearing that be like I would

## 60790:00 - 60835:00

never want to be asked to build

## 60835:00 - 60870:00

something like that in two weeks and I

## 60870:00 - 60915:00

think a lot of people do and love that

## 60915:00 - 60940:00

kind of experience as especially working

## 60940:00 - 60965:00

with Elon especially shipping something

## 60965:00 - 60990:00

at that scale but I think there's an

## 60990:00 - 61015:00

important element they're just like okay

## 61015:00 - 61040:00

I I don't want to do that I have other

## 61040:00 - 61070:00

things to do in my life other than ship

## 61070:00 - 61100:00

spaces so I think that's a I think

## 61100:00 - 61135:00

that's a key Point youve raised of just

## 61135:00 - 61175:00

there's an opt-in step totally I think

## 61175:00 - 61200:00

the opt-in is important and it may even

## 61200:00 - 61225:00

be that you want to opt in one part you

## 61225:00 - 61245:00

know at one point in your life and maybe

## 61245:00 - 61270:00

at another point in your life something

## 61270:00 - 61315:00

else is better I think you know whatever

## 61315:00 - 61360:00

it is you're choosing to do it's nice to

## 61360:00 - 61385:00

to be opted in to feel like it's aligned

## 61385:00 - 61420:00

with how you want to spend your time

## 61420:00 - 61445:00

something on my mind and I don't know if

## 61445:00 - 61470:00

you guys want to go here but it's

## 61470:00 - 61490:00

something I think a lot of people think

## 61490:00 - 61530:00

about is when Elon came in he let go of

## 61530:00 - 61560:00

80% of folks and everyone's just like

## 61560:00 - 61605:00

Twitter is dead it's all gonna fall

## 61605:00 - 61635:00

apart there's no way they can run this

## 61635:00 - 61675:00

thing with that small of a staff and

## 61675:00 - 61710:00

clearly it they were wrong clearly it's

## 61710:00 - 61765:00

working great it's like becoming a like

## 61765:00 - 61790:00

a massive deal in the world and

## 61790:00 - 61820:00

continues to grow is there anything

## 61820:00 - 61865:00

about that that you were surprised by or

## 61865:00 - 61895:00

anything about just like how it it

## 61895:00 - 61920:00

continues to operate so well in spite of

## 61920:00 - 61935:00

that big

## 61935:00 - 62015:00

shift I think the the the leaner team

## 62015:00 - 62065:00

the the reduced kind of like process and

## 62065:00 - 62100:00

bureaucracy is the big reason it does

## 62100:00 - 62165:00

move as fast as it does um it's easier

## 62165:00 - 62215:00

to get stuff done faster here

## 62215:00 - 62245:00

and

## 62245:00 - 62295:00

uh yeah I mean I think that's uh I think

## 62295:00 - 62335:00

I think it's that that shrink shrinking

## 62335:00 - 62385:00

is actually a big reason for the

## 62385:00 - 62425:00

increased pace of launches the increase

## 62425:00 - 62470:00

pace of experimentation one thing that I

## 62470:00 - 62505:00

noticed that as a result of that is the

## 62505:00 - 62545:00

people who are here they seem to all

## 62545:00 - 62575:00

really feel like owners like they take

## 62575:00 - 62610:00

like they take the sense of

## 62610:00 - 62640:00

responsibility that an owner takes in

## 62640:00 - 62680:00

the product um they'll try to track down

## 62680:00 - 62740:00

what's wrong fix whatever is needed um

## 62740:00 - 62795:00

jump into any to to help build or fix

## 62795:00 - 62825:00

improve any system that needs help even

## 62825:00 - 62855:00

if it's outside of their space and

## 62855:00 - 62880:00

there's the flip side of that too for

## 62880:00 - 62905:00

people who've worked at big companies

## 62905:00 - 62925:00

they may have experienced this thing

## 62925:00 - 62955:00

where where there's like you want to

## 62955:00 - 62990:00

change some something in some other

## 62990:00 - 63035:00

system or product and so you reach out

## 63035:00 - 63060:00

to that team and like maybe they're a

## 63060:00 - 63090:00

little resistant they maybe be like oh

## 63090:00 - 63120:00

we'll get to that next quarter they have

## 63120:00 - 63150:00

their own goals to hit yeah they yeah

## 63150:00 - 63170:00

exactly like they don't really

## 63170:00 - 63190:00

necessarily want to help you they're

## 63190:00 - 63235:00

busy here you're like hey guys we need

## 63235:00 - 63265:00

to do this thing with that other system

## 63265:00 - 63300:00

you work on and they're like great

## 63300:00 - 63345:00

here's the code here are the docs you

## 63345:00 - 63375:00

know send us the Fab if you have any

## 63375:00 - 63405:00

questions and we'll get it in and it's

## 63405:00 - 63450:00

just the thing you can jump in and and

## 63450:00 - 63490:00

get it done and that kind of

## 63490:00 - 63525:00

collaborative effort like the sense of

## 63525:00 - 63560:00

like shared ownership I

## 63560:00 - 63625:00

think from my experience came from a

## 63625:00 - 63655:00

result was a result of the shrinking of

## 63655:00 - 63695:00

the team down to people who you know

## 63695:00 - 63720:00

want to be there and work together to

## 63720:00 - 63755:00

build this thing so I think that's been

## 63755:00 - 63785:00

a really positive impact it's not always

## 63785:00 - 63810:00

easy certainly like a lot of people have

## 63810:00 - 63845:00

a lot of responsibilities but you know

## 63845:00 - 63890:00

they're here because they're up for it

## 63890:00 - 63925:00

yeah I think one other thing that's key

## 63925:00 - 63975:00

uh is uh when you are forced to have

## 63975:00 - 64020:00

such a small team you know deleting well

## 64020:00 - 64050:00

this is important anyways but deleting

## 64050:00 - 64075:00

code is more important than writing it a

## 64075:00 - 64140:00

lot of the time uh so I I think so often

## 64140:00 - 64165:00

maybe due to promotion incentives or

## 64165:00 - 64225:00

just regular human tency you uh you know

## 64225:00 - 64265:00

Engineers have a a tendency to add these

## 64265:00 - 64310:00

little incremental wins that actually H

## 64310:00 - 64345:00

add you know more of a long-term

## 64345:00 - 64375:00

maintenance cost than is clear because

## 64375:00 - 64405:00

you just run a little one month AB test

## 64405:00 - 64435:00

you see this you know know significant

## 64435:00 - 64460:00

win and you don't realize the

## 64460:00 - 64515:00

maintenance burden you just added uh to

## 64515:00 - 64555:00

your team for the rest of Eternity until

## 64555:00 - 64585:00

you turn the thing off so I think

## 64585:00 - 64620:00

there's a lot to be gained and you get

## 64620:00 - 64670:00

forced to do this um uh By the way when

## 64670:00 - 64695:00

you have such a small team is just

## 64695:00 - 64730:00

deleting you know auditing auditing

## 64730:00 - 64760:00

parts of your system and deleting the

## 64760:00 - 64795:00

things where the maintenance cost is

## 64795:00 - 64865:00

worse than one than the gains so I think

## 64865:00 - 64895:00

we did have to do this across the

## 64895:00 - 64955:00

company um after the the big layoffs and

## 64955:00 - 64995:00

um you know systems are leaner now and

## 64995:00 - 65025:00

and they can be worked on by fewer

## 65025:00 - 65055:00

numbers of people that's an amazing

## 65055:00 - 65080:00

point I remember elon's being like here

## 65080:00 - 65100:00

we have to throw away the whole thing we

## 65100:00 - 65120:00

have to re architect everything it's

## 65120:00 - 65150:00

stupid the way it's built and sounds

## 65150:00 - 65175:00

like that actually worked yeah you don't

## 65175:00 - 65200:00

have well we didn't you don't have to

## 65200:00 - 65225:00

rewrite everything from scratch I mean

## 65225:00 - 65270:00

some things we did I guess rewrite but

## 65270:00 - 65295:00

uh I I mean just even deleting the

## 65295:00 - 65335:00

unnecessary CR and keeping the rest of

## 65335:00 - 65390:00

the core system um that's awesome I love

## 65390:00 - 65410:00

that we're creating kind of a formula to

## 65410:00 - 65450:00

run these sorts of companies and teams

## 65450:00 - 65480:00

there's so much here I want to go back

## 65480:00 - 65515:00

to the the building of the original

## 65515:00 - 65545:00

product we it kind of took us on a long

## 65545:00 - 65600:00

tangent and an amazing tangent but uh I

## 65600:00 - 65635:00

heard a story of when you launched bird

## 65635:00 - 65680:00

watch at that point you specifically

## 65680:00 - 65715:00

wanted to keep expectations very low and

## 65715:00 - 65740:00

there was like a gif in the thing and it

## 65740:00 - 65775:00

just looked like clearly this is not um

## 65775:00 - 65810:00

ready for prime time talk about just how

## 65810:00 - 65830:00

you did that how you launched it in a

## 65830:00 - 65865:00

way where people weren't like uh it's

## 65865:00 - 65915:00

never going to work we were very

## 65915:00 - 65940:00

disciplined I guess guest you could say

## 65940:00 - 65985:00

about having the product prove itself at

## 65985:00 - 66040:00

at every given point um you know when

## 66040:00 - 66075:00

when we built the first mockups we had

## 66075:00 - 66125:00

just these were just like pictures of

## 66125:00 - 66150:00

you depicting what community notes might

## 66150:00 - 66170:00

look like we showed those to people

## 66170:00 - 66205:00

across the political Spectrum we saw

## 66205:00 - 66235:00

like hey people really like these

## 66235:00 - 66260:00

whether they're on the right or left

## 66260:00 - 66295:00

like they seem very open to reading

## 66295:00 - 66325:00

these Community notes even when they're

## 66325:00 - 66355:00

critical to people of their own side so

## 66355:00 - 66375:00

we're like all right that gives us

## 66375:00 - 66405:00

confidence that if we can build this

## 66405:00 - 66425:00

like if we can actually make this

## 66425:00 - 66460:00

reality it's going to work then there's

## 66460:00 - 66480:00

a question of like can we make it a

## 66480:00 - 66520:00

reality like are will people in the real

## 66520:00 - 66575:00

world be able to write notes that are of

## 66575:00 - 66625:00

this quality and so um you we built we

## 66625:00 - 66670:00

had an internal pilot test version of

## 66670:00 - 66700:00

this where you could like write notes

## 66700:00 - 66745:00

and we first basically ran this through

## 66745:00 - 66795:00

like an Amazon M Turk type of uh

## 66795:00 - 66830:00

participant test just to see like if you

## 66830:00 - 66860:00

just like put some normal people in

## 66860:00 - 66905:00

there like will they be able to write

## 66905:00 - 66945:00

these notes and not they weren't all all

## 66945:00 - 66975:00

those notes weren't good but like it was

## 66975:00 - 67000:00

clear that there were people out there

## 67000:00 - 67030:00

who could write good notes so I'm like

## 67030:00 - 67075:00

okay this is possible like what will

## 67075:00 - 67105:00

happen if we actually do this out in the

## 67105:00 - 67140:00

real world and like let's run let's run

## 67140:00 - 67190:00

a pilot and find out and so we took that

## 67190:00 - 67230:00

pilot the you we'd run the M kind of

## 67230:00 - 67290:00

test on and we were released it to at

## 67290:00 - 67330:00

first a thousand people to you know

## 67330:00 - 67375:00

totally out in public and we didn't know

## 67375:00 - 67405:00

what was going to show up like you could

## 67405:00 - 67455:00

imagine the not could have been terrible

## 67455:00 - 67490:00

and uh and so we were talking like well

## 67490:00 - 67510:00

what do we do like we're going to put

## 67510:00 - 67535:00

this out there everyone's going to have

## 67535:00 - 67555:00

all these questions they're probably

## 67555:00 - 67600:00

going to be really skeptical like and we

## 67600:00 - 67640:00

know it might be a total dumpster fire

## 67640:00 - 67670:00

and so like what do we do to like set

## 67670:00 - 67695:00

expectations appropriate like we felt

## 67695:00 - 67715:00

like we could probably get there in the

## 67715:00 - 67730:00

end but we just didn't know it was going

## 67730:00 - 67750:00

to happen at first we wanted to set

## 67750:00 - 67790:00

expectations and so we're like well why

## 67790:00 - 67815:00

don't we just stick there's like the

## 67815:00 - 67845:00

page where you see a post in the notes

## 67845:00 - 67870:00

flow like why don't we just stick a

## 67870:00 - 67925:00

dumpster fire gift like on that page and

## 67925:00 - 67975:00

and uh you know you go there you're like

## 67975:00 - 68015:00

hey you know anything you see below here

## 68015:00 - 68050:00

might just be a total dumpster fire um

## 68050:00 - 68085:00

at least it would show we we were aware

## 68085:00 - 68140:00

of that as a possible risk um we in the

## 68140:00 - 68185:00

end we did not do that it cracked me up

## 68185:00 - 68215:00

um but we thought it was kind of like oh

## 68215:00 - 68260:00

you didn't actually launch okay that we

## 68260:00 - 68305:00

had we had mockups of it and every time

## 68305:00 - 68365:00

I looked at the mockup I laughed but uh

## 68365:00 - 68395:00

ultim we had so much to explain on that

## 68395:00 - 68425:00

page like what is this thing and how at

## 68425:00 - 68455:00

work ultim like okay this is probably

## 68455:00 - 68495:00

going to like distract from the point um

## 68495:00 - 68530:00

so we pulled it I somewhat I kind of

## 68530:00 - 68560:00

wish maybe it had seen the light of day

## 68560:00 - 68590:00

at one point but yeah ultimately we kept

## 68590:00 - 68615:00

it simple we focused that page on

## 68615:00 - 68650:00

explaining what was going on here but

## 68650:00 - 68690:00

again you know we um as has happened

## 68690:00 - 68735:00

many time with times with the project um

## 68735:00 - 68770:00

you know we put the pilot out there and

## 68770:00 - 68805:00

the notes were good like they weren't

## 68805:00 - 68825:00

all good there was it was a mixed bag

## 68825:00 - 68860:00

but like there was gold in there and

## 68860:00 - 68895:00

from the very early days with just a

## 68895:00 - 68935:00

thousand contributors it was obvious

## 68935:00 - 68980:00

that that people could write notes that

## 68980:00 - 69015:00

were informative that were neutral that

## 69015:00 - 69050:00

spoke to controversial challenging

## 69050:00 - 69100:00

topics and that if we could just

## 69100:00 - 69145:00

identify those from the rest this was

## 69145:00 - 69165:00

going to work like it was going to work

## 69165:00 - 69200:00

as well as the very first mockups we had

## 69200:00 - 69250:00

made so that became the the the focus

## 69250:00 - 69280:00

then is how do we sift out the gold from

## 69280:00 - 69325:00

the rest I remember uh there's a I think

## 69325:00 - 69350:00

you may have shared with this with me

## 69350:00 - 69375:00

when someone noticed you guys were

## 69375:00 - 69405:00

testing this and they took screenshots

## 69405:00 - 69435:00

and tweeted it and they Elana replied

## 69435:00 - 69485:00

like this is cool yeah yeah so in the in

## 69485:00 - 69510:00

the very in the very early days when it

## 69510:00 - 69550:00

was just a figma prototype we were

## 69550:00 - 69580:00

running these like user testing.com

## 69580:00 - 69615:00

unmoderated studies I guess one of the

## 69615:00 - 69660:00

participants sent one to an NBC reporter

## 69660:00 - 69695:00

who like wrote a bunch of Stories on it

## 69695:00 - 69725:00

anyway like that day there's a lot of

## 69725:00 - 69800:00

chatter about it on on the service and

## 69800:00 - 69835:00

Elon this is like this is put this back

## 69835:00 - 69870:00

in you know time perspective this is I

## 69870:00 - 69940:00

think 2020 so two years before any

## 69940:00 - 69980:00

acquisition stuff happened Elon is just

## 69980:00 - 70025:00

a Twitter user building rockets and

## 70025:00 - 70070:00

electric cars and other cool stuff and

## 70070:00 - 70110:00

stumbles on this thing that depicts the

## 70110:00 - 70140:00

Prototype that we've been testing and he

## 70140:00 - 70195:00

writes back yeah definitely worth trying

## 70195:00 - 70235:00

IMO and I remember thinking that was

## 70235:00 - 70275:00

cool back then and it's interesting to

## 70275:00 - 70325:00

see like he's obviously had a very

## 70325:00 - 70360:00

consistent point on it I think you know

## 70360:00 - 70390:00

the idea was appealing and he you know

## 70390:00 - 70425:00

has obviously been a big fan of it um um

## 70425:00 - 70455:00

in the product and been a big supporter

## 70455:00 - 70495:00

proponent so uh yeah it was kind of it's

## 70495:00 - 70535:00

kind of cool that it came from that

## 70535:00 - 70565:00

support has been from the very early

## 70565:00 - 70595:00

days before he was ever involved in the

## 70595:00 - 70630:00

company I love that moment I must have

## 70630:00 - 70665:00

felt really wild for Elon to be

## 70665:00 - 70695:00

commenting on this figma prototype

## 70695:00 - 70765:00

retesting it was cool it was cool oh man

## 70765:00 - 70800:00

so when we were preparing for this

## 70800:00 - 70845:00

interview I asked uh you guys what's

## 70845:00 - 70870:00

what's the main thing you want to make

## 70870:00 - 70910:00

sure people get and understand about why

## 70910:00 - 70955:00

community has been so effective and

## 70955:00 - 70990:00

Keith you specifically said that it was

## 70990:00 - 71040:00

the principles behind how you wanted to

## 71040:00 - 71065:00

approach this and how you continue to

## 71065:00 - 71110:00

stick to this throughout and we'll talk

## 71110:00 - 71130:00

about how you kept it alive throughout

## 71130:00 - 71150:00

all these different Co changes of

## 71150:00 - 71190:00

leaders but just talk about these

## 71190:00 - 71215:00

principles like what the actual

## 71215:00 - 71245:00

principles are and why that was so key

## 71245:00 - 71295:00

to it working out there are a number of

## 71295:00 - 71330:00

principles that I think when we first

## 71330:00 - 71375:00

shared them with people at the company

## 71375:00 - 71415:00

seemed maybe a little bit crazy um but I

## 71415:00 - 71445:00

think they are they are the reason the

## 71445:00 - 71490:00

product works and I think they've been

## 71490:00 - 71525:00

very important and we do we come back to

## 71525:00 - 71580:00

them regularly today all the time

## 71580:00 - 71630:00

probably the craziest one is just that

## 71630:00 - 71675:00

this thing is going to be the voice of

## 71675:00 - 71700:00

the people it's going to represent the

## 71700:00 - 71725:00

voice of people it's not going to

## 71725:00 - 71770:00

represent the company's voice so it is

## 71770:00 - 71805:00

not a tech company deciding what shows

## 71805:00 - 71855:00

it is the people deciding what shows and

## 71855:00 - 71885:00

that had a lot of implications on the

## 71885:00 - 71940:00

design like first of all there is no we

## 71940:00 - 71980:00

don't have a button that will change the

## 71980:00 - 72025:00

status of the note of a note so if a

## 72025:00 - 72060:00

note is showing because the people have

## 72060:00 - 72100:00

rated it and found it helpful it is

## 72100:00 - 72140:00

going to show like we can't change that

## 72140:00 - 72165:00

and that is the kind of thing that like

## 72165:00 - 72195:00

at when we first proposed this that's

## 72195:00 - 72220:00

unsettling to people they're like wait

## 72220:00 - 72260:00

so like something can go up and and like

## 72260:00 - 72295:00

we you know the company can't take it

## 72295:00 - 72325:00

down or you know what can't change it

## 72325:00 - 72360:00

status get it to stop showing and we're

## 72360:00 - 72400:00

like yeah and like it has to work that

## 72400:00 - 72430:00

well if it doesn't work well enough to

## 72430:00 - 72455:00

do that then it doesn't work if there's

## 72455:00 - 72475:00

a problem with the note this is like one

## 72475:00 - 72505:00

of our one of our key principles was if

## 72505:00 - 72530:00

there's a problem with a note that's so

## 72530:00 - 72555:00

bad you want to do something about it

## 72555:00 - 72585:00

it's a problem with the system like we

## 72585:00 - 72635:00

need to redesign the system to to be

## 72635:00 - 72690:00

showing good notes and so so yeah we had

## 72690:00 - 72720:00

to you know get everyone comfortable

## 72720:00 - 72740:00

with the idea that there was no button

## 72740:00 - 72790:00

to to change the status of a note you

## 72790:00 - 72835:00

similarly we as we talked about earlier

## 72835:00 - 72870:00

we wanted this to represent all of

## 72870:00 - 72895:00

humanity and so we didn't want to be

## 72895:00 - 72935:00

Arbiters of who

## 72935:00 - 72970:00

can come in and be a contributor and who

## 72970:00 - 73005:00

can't like so we we we open it to

## 73005:00 - 73030:00

everyone you just have to make really

## 73030:00 - 73055:00

basic objective criteria like you have

## 73055:00 - 73080:00

to have a verified phone to help reduce

## 73080:00 - 73120:00

the likelihood of having like Bots or

## 73120:00 - 73150:00

things like that participating but

## 73150:00 - 73200:00

beyond that it's random selection and it

## 73200:00 - 73250:00

still is that way today and you know

## 73250:00 - 73280:00

again that people took some time to get

## 73280:00 - 73305:00

people comfortable with it but I think

## 73305:00 - 73370:00

the the the fact that this is the voice

## 73370:00 - 73425:00

of the people and reflects their out

## 73425:00 - 73455:00

through an open and transparent process

## 73455:00 - 73510:00

is so key to both why it is good like

## 73510:00 - 73545:00

why it works but also why it's

## 73545:00 - 73590:00

trusted so I mean that's number one and

## 73590:00 - 73620:00

and you it's you know I think will

## 73620:00 - 73685:00

forever be the heart of the product um

## 73685:00 - 73740:00

another one um that people thought was

## 73740:00 - 73785:00

kind of crazy was transparency you we're

## 73785:00 - 73830:00

like we're this we we the previous

## 73830:00 - 73860:00

approaches to dealing with misleading

## 73860:00 - 73910:00

info they it felt to a lot of people

## 73910:00 - 73940:00

like sort of

## 73940:00 - 73980:00

blackbox tech companies or media

## 73980:00 - 74005:00

companies or leites or whatever making

## 74005:00 - 74045:00

decisions like they people people need

## 74045:00 - 74065:00

to get comfortable with this they need

## 74065:00 - 74095:00

to trust this so the whole thing has to

## 74095:00 - 74140:00

be out in the open like the code that

## 74140:00 - 74175:00

decides what note show has to be out in

## 74175:00 - 74215:00

the open all the data and ratings that

## 74215:00 - 74245:00

that make it happen have to be out in

## 74245:00 - 74280:00

the open people should be able to take

## 74280:00 - 74310:00

the code and data and replicate the

## 74310:00 - 74355:00

whole service and that that we have done

## 74355:00 - 74390:00

exactly what we've said we've done and

## 74390:00 - 74410:00

they should be able to audit it they

## 74410:00 - 74435:00

should be able to go and look and say

## 74435:00 - 74465:00

like hey I think this part could be

## 74465:00 - 74490:00

better or like if they think we're

## 74490:00 - 74515:00

biased they should be able to work you

## 74515:00 - 74545:00

know work with the data and point it out

## 74545:00 - 74570:00

and if they if people have good

## 74570:00 - 74600:00

observations that should Factor back

## 74600:00 - 74640:00

into the code um and this is again

## 74640:00 - 74665:00

something that's kind of difficult to

## 74665:00 - 74700:00

get people comfortable with um that

## 74700:00 - 74730:00

everything is out there you can't cover

## 74730:00 - 74750:00

anything up but I think that's so

## 74750:00 - 74820:00

essential to people trusting it so um

## 74820:00 - 74870:00

yeah I mean we we we set these out on

## 74870:00 - 74905:00

day one we go back to them constantly

## 74905:00 - 74940:00

because we're we're we're always

## 74940:00 - 74975:00

evolving the the product and we always

## 74975:00 - 75005:00

like got to make sure every new Change

## 75005:00 - 75030:00

is open like whenever we update the code

## 75030:00 - 75055:00

there's or update the scoring system

## 75055:00 - 75080:00

there's an update in GitHub when the

## 75080:00 - 75105:00

data is published daily so you can

## 75105:00 - 75145:00

download it and so um yeah I think those

## 75145:00 - 75165:00

have been those have been really

## 75165:00 - 75205:00

essential to the thing working yeah and

## 75205:00 - 75235:00

and by the way these these do not come

## 75235:00 - 75285:00

without a cost right like the the it's

## 75285:00 - 75315:00

actually really hard from an Eng

## 75315:00 - 75360:00

perspective to actually open source the

## 75360:00 - 75380:00

actual algorithm that's running on the

## 75380:00 - 75435:00

actual data uh you because the the way

## 75435:00 - 75460:00

large scale services like this are

## 75460:00 - 75495:00

usually architected does not you know

## 75495:00 - 75550:00

naturally lend itself to like being run

## 75550:00 - 75580:00

uh like as a script by someone who's

## 75580:00 - 75620:00

downloaded a tsv so I actually have to

## 75620:00 - 75670:00

take weird architectural decisions uh to

## 75670:00 - 75700:00

make this possible in a way that

## 75700:00 - 75720:00

probably wouldn't have been if we didn't

## 75720:00 - 75750:00

start with this assumption from scratch

## 75750:00 - 75775:00

we would have had to maybe rewrite the

## 75775:00 - 75815:00

system to make to to make it like this

## 75815:00 - 75845:00

what's an example of that for instance

## 75845:00 - 75875:00

there's a matrix factorization that we

## 75875:00 - 75940:00

that we train right usually you um train

## 75940:00 - 75980:00

a matrix Factor you train your ml model

## 75980:00 - 76055:00

once and then um serve it uh uh uh I

## 76055:00 - 76100:00

guess with a separate Service uh but you

## 76100:00 - 76120:00

know we didn't want to have people

## 76120:00 - 76175:00

externally spinning up services uh you

## 76175:00 - 76210:00

know to to be able to repli replicate

## 76210:00 - 76265:00

the um you know system that we had so I

## 76265:00 - 76290:00

I mean basically I don't think it would

## 76290:00 - 76345:00

have been actually very cool if we had

## 76345:00 - 76380:00

uh open source the code in a way that

## 76380:00 - 76425:00

wasn't actually runable I guess

## 76425:00 - 76495:00

um you know by someone just you at this

## 76495:00 - 76520:00

point you can download python code and

## 76520:00 - 76550:00

and run a script you do need a lot of

## 76550:00 - 76595:00

ram right now but do it on one machine

## 76595:00 - 76625:00

okay okay how much RAM we talking about

## 76625:00 - 76680:00

oh like 500 gigs it it'll take like a

## 76680:00 - 76715:00

day if you don't uh do anything special

## 76715:00 - 76740:00

to speed it

## 76740:00 - 76785:00

up cool possible is the key thing and

## 76785:00 - 76825:00

people have done it um like uh vitalic

## 76825:00 - 76860:00

peteran had a blog post where he you

## 76860:00 - 76915:00

know talks about uh his explorations you

## 76915:00 - 76945:00

know making sure the algorithm really

## 76945:00 - 76985:00

does what it says it does and I think

## 76985:00 - 77020:00

just the fact that a handful of people

## 77020:00 - 77075:00

have done this uh you know there's

## 77075:00 - 77105:00

there's enough people who have done it

## 77105:00 - 77150:00

that there's someone you probably trust

## 77150:00 - 77190:00

who's who's verified yeah yeah and now

## 77190:00 - 77240:00

it's rolling out to meta no big deal uh

## 77240:00 - 77265:00

I love just like as you describe these

## 77265:00 - 77300:00

principles just I could imagine a PM at

## 77300:00 - 77330:00

a company being like okay guys here I

## 77330:00 - 77365:00

want to do this project it's going to be

## 77365:00 - 77400:00

completely like there's so much idealism

## 77400:00 - 77440:00

to it that Works in real life going to

## 77440:00 - 77465:00

be open source we going to give it to

## 77465:00 - 77490:00

everyone we don't have actual control

## 77490:00 - 77515:00

over what it's going to do don't worry

## 77515:00 - 77545:00

about it it's going to just change the

## 77545:00 - 77575:00

way people see this thing that we've

## 77575:00 - 77620:00

been very careful about uh and then it

## 77620:00 - 77665:00

works and I think that's very rare and

## 77665:00 - 77700:00

it's really impressive and what I'm

## 77700:00 - 77725:00

hearing partly is the sticking to those

## 77725:00 - 77760:00

principles was actually really

## 77760:00 - 77800:00

fundamental to it working and not kind

## 77800:00 - 77835:00

of bending over backward bending over

## 77835:00 - 77860:00

when someone's like no no no we can't do

## 77860:00 - 77900:00

this what if we change this part I think

## 77900:00 - 77935:00

if we had if we had broken with any of

## 77935:00 - 77960:00

those principles like if there was

## 77960:00 - 77995:00

anything black box if there was you know

## 77995:00 - 78035:00

what whatever I the product would be a

## 78035:00 - 78075:00

lot harder to trust and so I think it's

## 78075:00 - 78105:00

because we've just stuck to them so

## 78105:00 - 78145:00

cleanly simply that you know people

## 78145:00 - 78185:00

people can't trust it you've talked

## 78185:00 - 78225:00

about a few moments when it was like wow

## 78225:00 - 78255:00

the White House changed their

## 78255:00 - 78285:00

announcement because of a community note

## 78285:00 - 78325:00

we talked about the dog as a cat is are

## 78325:00 - 78360:00

there any other moments that after you

## 78360:00 - 78395:00

launched of like holy this is

## 78395:00 - 78435:00

working this is kind of actually work

## 78435:00 - 78470:00

all along you know we saw it we saw it

## 78470:00 - 78515:00

working like we were pretty we we wanted

## 78515:00 - 78560:00

to be confident whenever we expanded it

## 78560:00 - 78595:00

to New you know audiences or new

## 78595:00 - 78620:00

countries or whatever like we want to be

## 78620:00 - 78660:00

confident was going to work so you know

## 78660:00 - 78705:00

maybe you hold our breath a little bit

## 78705:00 - 78730:00

just to to see that it would do what we

## 78730:00 - 78770:00

expected but we always expected that but

## 78770:00 - 78820:00

that said there were definitely stress

## 78820:00 - 78855:00

stress cases I mean the one that comes

## 78855:00 - 78905:00

to mind is the start of the Israel Hamas

## 78905:00 - 78925:00

conflict

## 78925:00 - 78990:00

uh in 2023 in October um that was

## 78990:00 - 79045:00

probably the largest Deluge of

## 79045:00 - 79080:00

misleading information I've ever seen

## 79080:00 - 79110:00

shared on the internet at one time it

## 79110:00 - 79160:00

was like overwhelming that just the

## 79160:00 - 79205:00

number of photos and videos and whatever

## 79205:00 - 79255:00

coming out related to that was it was

## 79255:00 - 79305:00

insane and um just to you know to give

## 79305:00 - 79330:00

you an example in the first I think it

## 79330:00 - 79370:00

was like first three days or something

## 79370:00 - 79420:00

of that conflict we had 500

## 79420:00 - 79495:00

notes covering all sorts of different uh

## 79495:00 - 79535:00

you know like out of context imagery

## 79535:00 - 79560:00

like people someone say like hey this is

## 79560:00 - 79600:00

happening here um it's actually from

## 79600:00 - 79655:00

like 2013 in Syria there were people

## 79655:00 - 79695:00

making fake like battle footage in the

## 79695:00 - 79735:00

video game simulator Arma 3 so there

## 79735:00 - 79760:00

like notes explaining the stuff looked

## 79760:00 - 79805:00

really looked realistic and you unless

## 79805:00 - 79825:00

you saw they know you like wouldn't

## 79825:00 - 79855:00

really know um there are all sorts of

## 79855:00 - 79880:00

claims about what was going on in the

## 79880:00 - 79945:00

ground and you know that was definitely

## 79945:00 - 79970:00

the product was still pretty new at that

## 79970:00 - 79995:00

point we had only we had expanded in the

## 79995:00 - 80040:00

US um less than a year before that we

## 80040:00 - 80080:00

had been rolling out throughout the

## 80080:00 - 80110:00

world that year and then this large

## 80110:00 - 80160:00

event happened and um you know I felt

## 80160:00 - 80205:00

like we were we were just enough

## 80205:00 - 80240:00

prepared at the right time for the

## 80240:00 - 80270:00

system to be able to handle that like

## 80270:00 - 80300:00

probably one of the most important

## 80300:00 - 80325:00

things we did right before that was

## 80325:00 - 80350:00

launched the ability to write notes on

## 80350:00 - 80380:00

images and media and have images and

## 80380:00 - 80425:00

videos and have those matched to other

## 80425:00 - 80475:00

like I remember at that time thinking

## 80475:00 - 80520:00

like wow I'm glad we launched that

## 80520:00 - 80565:00

feature a few months ago versus still

## 80565:00 - 80605:00

had it on the Shelf um because it was

## 80605:00 - 80645:00

really important in that conflict and I

## 80645:00 - 80690:00

think even it was like just a few weeks

## 80690:00 - 80720:00

before we had launched a major speed up

## 80720:00 - 80760:00

in Notes too I like when we when we

## 80760:00 - 80790:00

first built the product the number one

## 80790:00 - 80840:00

Focus was always quality like we knew we

## 80840:00 - 80875:00

knew that notes the product would live

## 80875:00 - 80900:00

and die by the quality of the notes and

## 80900:00 - 80920:00

like that was the thing we could never

## 80920:00 - 80945:00

give up on we also knew it needed to

## 80945:00 - 80975:00

deliver speed and scale but we're like

## 80975:00 - 81025:00

we will we get the quality in the right

## 81025:00 - 81055:00

place and we can speed we can speed it

## 81055:00 - 81090:00

up and scale it out over time and we had

## 81090:00 - 81110:00

actually just launched a speed up that

## 81110:00 - 81165:00

took like three hours off the time it um

## 81165:00 - 81210:00

time of note needed to go live and I was

## 81210:00 - 81230:00

you know I think a matter of weeks

## 81230:00 - 81260:00

before that conflict happened so again

## 81260:00 - 81310:00

like super glad that was out there the

## 81310:00 - 81330:00

in the first few days of the conflict

## 81330:00 - 81355:00

the median time from a post going live

## 81355:00 - 81380:00

to a note showing up was five hours

## 81380:00 - 81425:00

which is like crazy fast

## 81425:00 - 81455:00

typical factchecking is like two to four

## 81455:00 - 81480:00

it's relased it's really common to see

## 81480:00 - 81515:00

it take two to four days these NES were

## 81515:00 - 81560:00

showing up in five hours we're like we

## 81560:00 - 81600:00

are so glad we got those things out

## 81600:00 - 81640:00

before this happened um it made the

## 81640:00 - 81675:00

service a lot more helpful one other

## 81675:00 - 81750:00

thing that was um I I think nice to you

## 81750:00 - 81805:00

know see see working then was I think

## 81805:00 - 81830:00

one criticism of community not some

## 81830:00 - 81870:00

people bring up is well if you always

## 81870:00 - 81900:00

need agreement from people who typically

## 81900:00 - 81935:00

disagree then in these super polarized

## 81935:00 - 81980:00

settings like that conflict being like

## 81980:00 - 82025:00

probably number one uh then then you

## 82025:00 - 82065:00

know uh you wouldn't see any notes but

## 82065:00 - 82090:00

actually the reality was there were the

## 82090:00 - 82120:00

you know tons of notes about that

## 82120:00 - 82155:00

conflict um so I think there is this

## 82155:00 - 82225:00

kind of um you know nice uh nice

## 82225:00 - 82260:00

property where actually and maybe this

## 82260:00 - 82290:00

is a surprising fact that there's more

## 82290:00 - 82315:00

agreement out there across polarized

## 82315:00 - 82350:00

divides than maybe conventional wisdom

## 82350:00 - 82390:00

says right and PE and the places where

## 82390:00 - 82415:00

people agreed were

## 82415:00 - 82450:00

really objectively true and verifiable

## 82450:00 - 82490:00

like uh I guess maybe this is more true

## 82490:00 - 82540:00

the more polarized the setting is but uh

## 82540:00 - 82590:00

where the the agreement actually uh

## 82590:00 - 82635:00

lands you in uh basically notes that are

## 82635:00 - 82675:00

very neutrally written very focused on

## 82675:00 - 82730:00

the facts and and easy to verify um

## 82730:00 - 82765:00

information I love just like there's

## 82765:00 - 82800:00

this this talk for a while of just like

## 82800:00 - 82830:00

no more there's no more facts like

## 82830:00 - 82875:00

nobody believes there is a single true

## 82875:00 - 82920:00

fact anymore like every is subjective

## 82920:00 - 82950:00

and I think Community notes is the exact

## 82950:00 - 82990:00

proves the opposite yeah facts matter

## 82990:00 - 83015:00

there are facts we can all agree with

## 83015:00 - 83065:00

even the most controversial topics yeah

## 83065:00 - 83110:00

yeah we we saw this really from day one

## 83110:00 - 83160:00

it's you we when we would show those

## 83160:00 - 83195:00

prototypes to people just depicting the

## 83195:00 - 83240:00

idea it was really obvious that people

## 83240:00 - 83280:00

cared more about or they cared a lot

## 83280:00 - 83310:00

about getting understanding reality and

## 83310:00 - 83335:00

what was going on and they were willing

## 83335:00 - 83375:00

to disagree with like their side so to

## 83375:00 - 83435:00

speak to recognize that um and I think

## 83435:00 - 83470:00

that's not always that obvious to people

## 83470:00 - 83510:00

the world does feel really polarized but

## 83510:00 - 83530:00

um people definitely are willing to

## 83530:00 - 83580:00

cross partis and boundaries to to get to

## 83580:00 - 83615:00

you know accurate information and that's

## 83615:00 - 83665:00

why the product works it feels like as

## 83665:00 - 83705:00

we rely more and more on what we know

## 83705:00 - 83735:00

and and understand about the world is

## 83735:00 - 83785:00

becoming social media online and moving

## 83785:00 - 83815:00

this quickly it feels like it's like

## 83815:00 - 83860:00

we're I'm so thankful this exists

## 83860:00 - 83910:00

because otherwise it just be what do we

## 83910:00 - 83960:00

trust anymore like this is like it like

## 83960:00 - 83990:00

this being out aligns with we need this

## 83990:00 - 84055:00

thing to exist at the same time and it

## 84055:00 - 84090:00

feels like at the same time there's also

## 84090:00 - 84140:00

this people just like I just don't trust

## 84140:00 - 84170:00

I I think people have shifted from I

## 84170:00 - 84200:00

trust what I read to okay I shouldn't

## 84200:00 - 84240:00

just believe everything I'm reading uh

## 84240:00 - 84260:00

is there anything there you're noticing

## 84260:00 - 84280:00

about just how

## 84280:00 - 84335:00

people uh think about news they see and

## 84335:00 - 84365:00

their shift of just like I'm not going

## 84365:00 - 84400:00

to believe everything is there anything

## 84400:00 - 84425:00

there noticing but just like human

## 84425:00 - 84465:00

behavior just the way we've shifted

## 84465:00 - 84510:00

understanding what is true we haven't

## 84510:00 - 84550:00

done any research you know to look

## 84550:00 - 84585:00

broadly at at how people's perceptions

## 84585:00 - 84625:00

are are changing there but I certainly

## 84625:00 - 84670:00

have found you know myself that

## 84670:00 - 84730:00

particularly seeing notes um I am more

## 84730:00 - 84760:00

skeptical about what I read at first and

## 84760:00 - 84795:00

I I think that's been helpful and we

## 84795:00 - 84835:00

hear that from people that they think

## 84835:00 - 84870:00

about things a bit more and um you know

## 84870:00 - 84925:00

I think that's a good secondary effect

## 84925:00 - 84975:00

and benefit of of something like this

## 84975:00 - 85010:00

which is the more you see the patterns

## 85010:00 - 85060:00

of how what you're reading can be wrong

## 85060:00 - 85095:00

the more you can thoughtfully question

## 85095:00 - 85150:00

it and try to get a better understanding

## 85150:00 - 85175:00

what's really going on so it's like you

## 85175:00 - 85190:00

know historically I think this was

## 85190:00 - 85230:00

called like media literacy but basic

## 85230:00 - 85270:00

idea of like can you understand the ways

## 85270:00 - 85320:00

in which things can go wrong and try to

## 85320:00 - 85370:00

T them yourself and another aspect I

## 85370:00 - 85405:00

think we help with that is discovery of

## 85405:00 - 85455:00

the community notes uh I think often you

## 85455:00 - 85485:00

know if before Community notes you could

## 85485:00 - 85515:00

have just been living in a little news

## 85515:00 - 85550:00

filter bubble or maybe there were fact

## 85550:00 - 85580:00

checks out there that you should have

## 85580:00 - 85610:00

been reading but you weren't discovering

## 85610:00 - 85650:00

them uh right so so the the fact that

## 85650:00 - 85695:00

the note applies it's directly attached

## 85695:00 - 85735:00

to the post um and visible by anyone who

## 85735:00 - 85790:00

sees the post helps you know cross those

## 85790:00 - 85835:00

those filter Bubbles and and can kind of

## 85835:00 - 85860:00

I think for some people it's the first

## 85860:00 - 85885:00

time they've they've actually seen

## 85885:00 - 85940:00

counterarguments to you know uh to to

## 85940:00 - 85985:00

claims made uh in their own little Echo

## 85985:00 - 86020:00

chamber that's incredible yeah I love

## 86020:00 - 86040:00

the point you're making about how it

## 86040:00 - 86070:00

actually teaches people to be a little

## 86070:00 - 86100:00

more skeptical of the things they read

## 86100:00 - 86145:00

like it's an education uh system more

## 86145:00 - 86175:00

than more than just here's the one thing

## 86175:00 - 86185:00

is

## 86185:00 - 86235:00

wrong I love that okay just a few more

## 86235:00 - 86270:00

questions uh there was an audience

## 86270:00 - 86300:00

question asked on Twitter we all asked

## 86300:00 - 86315:00

on Twitter what do people want to know

## 86315:00 - 86350:00

back ining the notes one was actually

## 86350:00 - 86380:00

why you guys switched to Anonymous

## 86380:00 - 86410:00

contributors what was the dis ision

## 86410:00 - 86455:00

between behind that yeah that was you

## 86455:00 - 86495:00

know we we had this pilot um where we

## 86495:00 - 86535:00

were testing the with a small number of

## 86535:00 - 86555:00

contributors like th few thousand

## 86555:00 - 86580:00

contributors and we learned a lot

## 86580:00 - 86605:00

through that pilot probably the biggest

## 86605:00 - 86645:00

thing we learned was related to

## 86645:00 - 86695:00

anonymity or pseudonymity of

## 86695:00 - 86735:00

contributors we had originally assumed

## 86735:00 - 86760:00

that it was important that people

## 86760:00 - 86800:00

contribute under their like real handle

## 86800:00 - 86825:00

or their real name or whatever it was we

## 86825:00 - 86850:00

actually like the first prototypes

## 86850:00 - 86880:00

depicted that we kind of thought that

## 86880:00 - 86905:00

would be important for like people

## 86905:00 - 86940:00

trusting the note and actually it was

## 86940:00 - 86975:00

totally wrong we were like it was the

## 86975:00 - 87005:00

the the best option was actually the

## 87005:00 - 87040:00

opposite of what we first tried um we

## 87040:00 - 87095:00

found a few things one people were

## 87095:00 - 87130:00

hesitant to write a note on a

## 87130:00 - 87170:00

controversial topic because they didn't

## 87170:00 - 87200:00

want to get like attacked or harassed

## 87200:00 - 87240:00

online and so some people were

## 87240:00 - 87265:00

comfortable doing it doing this but

## 87265:00 - 87290:00

others were not and so it meant there

## 87290:00 - 87320:00

was more potential good notes to be

## 87320:00 - 87370:00

written um than were getting written and

## 87370:00 - 87390:00

this is very clear feedback from the

## 87390:00 - 87455:00

pilot two and this is super interesting

## 87455:00 - 87490:00

people are actually more willing to

## 87490:00 - 87535:00

cross partisan boundaries when they are

## 87535:00 - 87585:00

Anonymous or pseudonymous than when they

## 87585:00 - 87610:00

are under their real name and it

## 87610:00 - 87645:00

intuitively makes a lot of sense like if

## 87645:00 - 87690:00

you publicly are using your name you are

## 87690:00 - 87725:00

you you feel are affiliated with one

## 87725:00 - 87765:00

side versus the other you might hesitate

## 87765:00 - 87805:00

to kind of like be perceived as breaking

## 87805:00 - 87865:00

with that side but you may actually you

## 87865:00 - 87895:00

know for example find a note helpful

## 87895:00 - 87935:00

that's critical of that side and um

## 87935:00 - 87960:00

there's a bunch of studies that show

## 87960:00 - 87980:00

when people are Anonymous they're much

## 87980:00 - 88000:00

more willing to cross bound partisan

## 88000:00 - 88020:00

boundaries and work with the other side

## 88020:00 - 88050:00

agree with the other side and and we saw

## 88050:00 - 88085:00

that too and so by allowing people to

## 88085:00 - 88110:00

just to be student Anonymous you

## 88110:00 - 88140:00

actually get more honest answers about

## 88140:00 - 88160:00

what they really think and it helps find

## 88160:00 - 88190:00

disagreement that really so

## 88190:00 - 88215:00

counterintuitive you know you never hear

## 88215:00 - 88240:00

the opposite always and it's so

## 88240:00 - 88285:00

interesting that's the opposite yeah I

## 88285:00 - 88320:00

think this uh the the same principle

## 88320:00 - 88355:00

applies to making the likes private I

## 88355:00 - 88390:00

was just thinking that yeah yeah I like

## 88390:00 - 88440:00

a lot more stuff that's a little stuff I

## 88440:00 - 88470:00

wouldn't have liked yeah it allows it

## 88470:00 - 88495:00

allows freedom for honesty which is

## 88495:00 - 88555:00

pretty great um and you and we one of

## 88555:00 - 88585:00

the criticisms of pseudonymity is like

## 88585:00 - 88615:00

you know it can generate maybe like

## 88615:00 - 88645:00

people ruce their their quality the

## 88645:00 - 88665:00

quality threshold that they put out

## 88665:00 - 88685:00

there but we have so many quality

## 88685:00 - 88705:00

mechanisms in the system that that

## 88705:00 - 88750:00

wasn't an issue so um we could keep

## 88750:00 - 88780:00

quality High while while opening up for

## 88780:00 - 88825:00

that Honesty another question you

## 88825:00 - 88860:00

touched on this a little bit which is

## 88860:00 - 88905:00

around navigating the existing trust and

## 88905:00 - 88965:00

safety apparatus of Twitter which to as

## 88965:00 - 88990:00

you described basically previously was

## 88990:00 - 89040:00

like we make decisions on what is true

## 89040:00 - 89090:00

and not and there's every company works

## 89090:00 - 89135:00

this way you guys basically upended that

## 89135:00 - 89155:00

like here's a completely different way

## 89155:00 - 89195:00

you have no control over what is what we

## 89195:00 - 89230:00

say is true or not talk about just that

## 89230:00 - 89260:00

experience of kind of overcoming that I

## 89260:00 - 89295:00

imagine very difficult hurdle of like

## 89295:00 - 89320:00

okay forget all that we're going to do

## 89320:00 - 89350:00

it totally different yeah it was

## 89350:00 - 89380:00

definitely what we were proposing was

## 89380:00 - 89410:00

very different I will said I think

## 89410:00 - 89440:00

people were sort of open-minded to it

## 89440:00 - 89500:00

generally speaking um and I think

## 89500:00 - 89535:00

everyone had a sense that what was being

## 89535:00 - 89575:00

done at the time wasn't really working

## 89575:00 - 89605:00

that well or solving the problem and you

## 89605:00 - 89625:00

know people were open to ideas so that

## 89625:00 - 89660:00

was that's like a good foundation but I

## 89660:00 - 89710:00

think one thing we did that was probably

## 89710:00 - 89760:00

very helpful in that is we wanted the

## 89760:00 - 89790:00

product to prove itself at any point

## 89790:00 - 89825:00

like first it had to prove that people

## 89825:00 - 89855:00

could possibly you know find notes

## 89855:00 - 89875:00

helpful then it had to prove that people

## 89875:00 - 89900:00

could possibly like write these not

## 89900:00 - 89940:00

notes that would be good quality and so

## 89940:00 - 89995:00

anytime that we were proposing doing

## 89995:00 - 90040:00

something with the product like running

## 90040:00 - 90085:00

some research test or running the pilot

## 90085:00 - 90150:00

or expanding the pilot we always had the

## 90150:00 - 90185:00

data that had convinced us that that was

## 90185:00 - 90250:00

a good decision like we we were stepping

## 90250:00 - 90285:00

into the next phase of expansion that

## 90285:00 - 90350:00

made sense and so I think we probably

## 90350:00 - 90420:00

rarely proposed anything that the unwise

## 90420:00 - 90445:00

um like because we were holding such a

## 90445:00 - 90490:00

high bar for Quality ourselves um I

## 90490:00 - 90520:00

think you know I I suspect that went a

## 90520:00 - 90565:00

long way so it's partly what I'm hearing

## 90565:00 - 90610:00

is like uh take it step by step to prove

## 90610:00 - 90665:00

this is actually working and partly be

## 90665:00 - 90705:00

confident it is working your to yourself

## 90705:00 - 90740:00

before you try to convince say the trust

## 90740:00 - 90795:00

and safety team this is the way to go

## 90795:00 - 90830:00

exactly uh is there any was there like a

## 90830:00 - 90860:00

moment along that journey of just like

## 90860:00 - 90895:00

okay here this like it shifted from no

## 90895:00 - 90930:00

way this is a thing to okay Wow Let's

## 90930:00 - 90960:00

actually consider this or is it this

## 90960:00 - 91000:00

very gradual process whether other

## 91000:00 - 91050:00

people were saying no way to VI yeah

## 91050:00 - 91070:00

just internally of just like okay we're

## 91070:00 - 91110:00

gonna actually stop this trust and

## 91110:00 - 91160:00

safety uh way of operating and instead

## 91160:00 - 91180:00

verely on community know so is there

## 91180:00 - 91200:00

like a moment of like okay let's

## 91200:00 - 91220:00

actually make that switch or is that

## 91220:00 - 91260:00

Elon actually is that the big switch the

## 91260:00 - 91330:00

biggest change there happened in X um

## 91330:00 - 91355:00

the biggest changes prior to that were

## 91355:00 - 91390:00

just the decision to put this out there

## 91390:00 - 91455:00

and uh you know and have it be operating

## 91455:00 - 91510:00

at you know in public at first us-wide

## 91510:00 - 91545:00

scale um but yeah then the big the

## 91545:00 - 91600:00

bigger switches came in the X period I

## 91600:00 - 91630:00

think even even though there was you

## 91630:00 - 91675:00

know original research uh you know

## 91675:00 - 91700:00

before before Bird Watch had even

## 91700:00 - 91730:00

started uh or Community notes even

## 91730:00 - 91760:00

started from external researchers

## 91760:00 - 91805:00

showing that you know crowdsource fact

## 91805:00 - 91850:00

Checkers uh can do you know lay people

## 91850:00 - 91885:00

can do about as well as fact Checkers

## 91885:00 - 91910:00

and actually agreement rates were kind

## 91910:00 - 91940:00

of similar between the groups like I

## 91940:00 - 91965:00

think even though that research was out

## 91965:00 - 91995:00

there I think there were definitely a

## 91995:00 - 92020:00

lot of people who didn't really believe

## 92020:00 - 92055:00

it could work until it already

## 92055:00 - 92095:00

worked basically prove it prove that it

## 92095:00 - 92130:00

works and yeah that makes sense versus

## 92130:00 - 92170:00

just a bunch of docks and strategy and

## 92170:00 - 92195:00

thinking it's just like look it's

## 92195:00 - 92215:00

actually working you can see for

## 92215:00 - 92265:00

yourself yeah makes sense okay possibly

## 92265:00 - 92310:00

last question uh we'll see what fractals

## 92310:00 - 92350:00

of questions you guys bring up here uh I

## 92350:00 - 92400:00

referenced this a couple times this uh

## 92400:00 - 92430:00

incredible achievement of keeping a

## 92430:00 - 92505:00

project alive through Jack and then I

## 92505:00 - 92535:00

have this note and and Kavon running the

## 92535:00 - 92575:00

show then and then parag running Twitter

## 92575:00 - 92625:00

and then Elon and then Linda taking over

## 92625:00 - 92675:00

a co uh quite rare especially something

## 92675:00 - 92710:00

this visible this impactful to

## 92710:00 - 92785:00

everything that X is any lessons or keys

## 92785:00 - 92825:00

to that actually working of this project

## 92825:00 - 92870:00

surviving throughout so many or changes

## 92870:00 - 92900:00

and leaders

## 92900:00 - 92935:00

it definitely has been a crazy time to

## 92935:00 - 92980:00

be building something uh it's been fun

## 92980:00 - 93040:00

uh the craziness has been entertaining

## 93040:00 - 93105:00

um I think you know one one reason the

## 93105:00 - 93140:00

perhaps the product has has done so well

## 93140:00 - 93175:00

and survived is the product itself the

## 93175:00 - 93210:00

nature of the product itself it is

## 93210:00 - 93260:00

designed to produce information that is

## 93260:00 - 93295:00

found helpful by people who normally

## 93295:00 - 93350:00

disagree and so even if you have CEOs or

## 93350:00 - 93375:00

leaders who might disagree like there's

## 93375:00 - 93400:00

a good chance actually they'll find Al

## 93400:00 - 93420:00

they like wow this thing does produce

## 93420:00 - 93445:00

pretty you know useful output so I think

## 93445:00 - 93470:00

there's something in the nature of the

## 93470:00 - 93500:00

product itself that you know when people

## 93500:00 - 93530:00

see it whatever side they're on you know

## 93530:00 - 93570:00

left right what up down um they're

## 93570:00 - 93605:00

likely to find it pretty helpful um so I

## 93605:00 - 93655:00

do think that helps um uh I also think

## 93655:00 - 93735:00

the team executed really well um we had

## 93735:00 - 93770:00

ambitious goals that were exciting they

## 93770:00 - 93825:00

solved a real problem this is a real

## 93825:00 - 93850:00

problem that matters in the

## 93850:00 - 93900:00

world at at every step

## 93900:00 - 93930:00

you know as as we talked about the

## 93930:00 - 93965:00

product needed to prove itself and you

## 93965:00 - 93995:00

know we would make sure it proved itself

## 93995:00 - 94025:00

and we would bring the results that

## 94025:00 - 94050:00

convinced us and we' share those with

## 94050:00 - 94080:00

people and so they would say oh yeah it

## 94080:00 - 94115:00

I agree it kind of proved itself let's

## 94115:00 - 94160:00

take the next leap and and we've we've

## 94160:00 - 94185:00

done that all along the way and we

## 94185:00 - 94245:00

continue to operate that way and I think

## 94245:00 - 94330:00

like that focus on the outcome and goal

## 94330:00 - 94380:00

that matters and executing against it

## 94380:00 - 94425:00

really helps like the team did not get

## 94425:00 - 94475:00

distracted by much all through the

## 94475:00 - 94500:00

period during which the acquisition

## 94500:00 - 94525:00

happened like there was a lot of

## 94525:00 - 94560:00

opportunity for distraction this team

## 94560:00 - 94595:00

was shipping like every week like we

## 94595:00 - 94635:00

were super focused on the goal like

## 94635:00 - 94690:00

let's make this thing work let's get

## 94690:00 - 94740:00

these notes out there and um you I think

## 94740:00 - 94785:00

people saw that execution and and were

## 94785:00 - 94825:00

excited to support it yeah like it's

## 94825:00 - 94850:00

working why would we must with that and

## 94850:00 - 94880:00

it's important and it keeps us from

## 94880:00 - 94925:00

having to higher ATT of thousands of of

## 94925:00 - 94955:00

people to fact check you know an

## 94955:00 - 94995:00

interesting thing about that is no one

## 94995:00 - 95040:00

ever asked us or brought up or seem to

## 95040:00 - 95080:00

care about anything related to cost

## 95080:00 - 95125:00

savings um in this process and I think

## 95125:00 - 95170:00

that's like a pro like a an assumption

## 95170:00 - 95195:00

people have outside the company that

## 95195:00 - 95220:00

like this must have been a reason there

## 95220:00 - 95250:00

was interest in it but like that was

## 95250:00 - 95285:00

never a goal was NE not at all why the

## 95285:00 - 95310:00

project was starters not why people are

## 95310:00 - 95350:00

excited about the project and I think

## 95350:00 - 95385:00

that's also you know for people outside

## 95385:00 - 95420:00

who you don't see the conversations is

## 95420:00 - 95450:00

like kind of a heartening thing to know

## 95450:00 - 95480:00

is that the focus was always on solving

## 95480:00 - 95525:00

the problem the other approach is even

## 95525:00 - 95580:00

if you had 10,000 people doing it like

## 95580:00 - 95605:00

it the real issue is that they don't

## 95605:00 - 95635:00

work that well because they're not

## 95635:00 - 95655:00

trusted or they don't scale it or

## 95655:00 - 95710:00

they're too slow and so um the goal is

## 95710:00 - 95740:00

really always just let's like help

## 95740:00 - 95780:00

people stay informed at scale you know

## 95780:00 - 95810:00

let's build an internet internet scale

## 95810:00 - 95835:00

solution to an internet scale problem

## 95835:00 - 95875:00

that people like something I heard about

## 95875:00 - 95910:00

you Keith when I was asking people about

## 95910:00 - 95935:00

how this worked and why this worked so

## 95935:00 - 95980:00

well is that they describe you with a

## 95980:00 - 96010:00

having a very low

## 96010:00 - 96060:00

ego and that allowed you to give up this

## 96060:00 - 96095:00

whole team and power influence and just

## 96095:00 - 96120:00

the name forget it whatever you want

## 96120:00 - 96155:00

we'll call it Community notes CR is

## 96155:00 - 96175:00

there anything there you can share of

## 96175:00 - 96215:00

just like how how you think about that

## 96215:00 - 96250:00

and how important that is as a product

## 96250:00 - 96295:00

leader to have a low

## 96295:00 - 96370:00

ego um you know for me this this project

## 96370:00 - 96395:00

I feel like I get to do community

## 96395:00 - 96440:00

service with this project like my I like

## 96440:00 - 96475:00

I see my work is in service of the

## 96475:00 - 96505:00

people and the community and like that's

## 96505:00 - 96555:00

what motivates me the only thing that I

## 96555:00 - 96625:00

care about is delivering the outcome

## 96625:00 - 96675:00

that the world finds helpful and so in

## 96675:00 - 96715:00

some ways the project has has not been

## 96715:00 - 96750:00

about like ego results it's it's like

## 96750:00 - 96785:00

about truth seeking like let's find not

## 96785:00 - 96810:00

truth in the sense of like what

## 96810:00 - 96835:00

information is true but like let's find

## 96835:00 - 96860:00

out what's actually going to make this

## 96860:00 - 96920:00

work um like how does it need to be how

## 96920:00 - 96965:00

does it need to be structured what is it

## 96965:00 - 96990:00

what should it be called like whatever

## 96990:00 - 97015:00

is going to produce the best outcome is

## 97015:00 - 97065:00

what we should do and um so I think you

## 97065:00 - 97105:00

know I feel more attached to the product

## 97105:00 - 97140:00

being helpful than to anything else and

## 97140:00 - 97180:00

so you know to whatever degree might

## 97180:00 - 97205:00

seem like low ego is probably more

## 97205:00 - 97230:00

result of wanting to actually solve the

## 97230:00 - 97265:00

problem and I think I think partly what

## 97265:00 - 97290:00

I'm hearing is just if you win and

## 97290:00 - 97330:00

succeed good things will happen so focus

## 97330:00 - 97360:00

on that certainly satisfying things will

## 97360:00 - 97385:00

happen it's very satisfying to have

## 97385:00 - 97405:00

people people appreciate it it's

## 97405:00 - 97435:00

satisfying that like people on the left

## 97435:00 - 97480:00

and right you know love it it's

## 97480:00 - 97505:00

satisfying that even people who receive

## 97505:00 - 97545:00

notes love notes and screenshot them and

## 97545:00 - 97590:00

post them like that's amazing it feels

## 97590:00 - 97635:00

it feels you know so good to have helped

## 97635:00 - 97685:00

give people that and um and yeah you

## 97685:00 - 97705:00

know it's very motivating it's a great

## 97705:00 - 97740:00

reason to wake up in the morning it's

## 97740:00 - 97770:00

absurd this is work but it's also like

## 97770:00 - 97805:00

of of course this would work of course

## 97805:00 - 97835:00

something like this should work it's

## 97835:00 - 97885:00

like such Internet it's of the internet

## 97885:00 - 97945:00

you you know that's why it works oh man

## 97945:00 - 97970:00

where's Community n going from here what

## 97970:00 - 97990:00

your people look what's happening

## 97990:00 - 98030:00

where's it going what's uh what's the

## 98030:00 - 98085:00

future we're always working on you

## 98085:00 - 98135:00

basically more better notes faster so we

## 98135:00 - 98165:00

want there's clearly opportunity to get

## 98165:00 - 98215:00

more notes out there um we want want

## 98215:00 - 98245:00

them to stay as good or better than they

## 98245:00 - 98280:00

are we want to get them there faster so

## 98280:00 - 98300:00

we're always working on like core

## 98300:00 - 98350:00

product changes um to help deliver that

## 98350:00 - 98405:00

like recently for example we um just

## 98405:00 - 98430:00

released an update to what we call the

## 98430:00 - 98460:00

community notes bat signal or the

## 98460:00 - 98505:00

ability to request a community note so

## 98505:00 - 98555:00

we anyone on X can say hey I think this

## 98555:00 - 98590:00

post needs a community note and now they

## 98590:00 - 98640:00

can even out a source explaining why so

## 98640:00 - 98675:00

that when a prospective writer sees that

## 98675:00 - 98700:00

it's much easier for them to write a

## 98700:00 - 98735:00

note um so we're always working on on

## 98735:00 - 98770:00

core things like that core

## 98770:00 - 98820:00

improvements um I think there are also

## 98820:00 - 98855:00

New Frontiers that show a lot of

## 98855:00 - 98925:00

potential um AI and llms are one it's

## 98925:00 - 98975:00

easy to imagine a lot of ways that um AI

## 98975:00 - 99040:00

could assist the people in this task

## 99040:00 - 99065:00

they're doing of of trying to get

## 99065:00 - 99115:00

information out there quickly um maybe

## 99115:00 - 99140:00

you Jay should talk about the supernotes

## 99140:00 - 99190:00

work that uh we've done with some folks

## 99190:00 - 99210:00

outside the

## 99210:00 - 99255:00

company yeah so I mean one cool thing

## 99255:00 - 99315:00

about having public data en code is that

## 99315:00 - 99350:00

uh external researchers can can

## 99350:00 - 99415:00

collaborate with you uh and and case um

## 99415:00 - 99475:00

the supernotes of this idea that we can

## 99475:00 - 99540:00

uh basically take existing notes input

## 99540:00 - 99580:00

uh existing proposed notes that aren't

## 99580:00 - 99600:00

actually you know maybe they have some

## 99600:00 - 99625:00

problem maybe they have they part of the

## 99625:00 - 99660:00

story maybe they're worded and kind of a

## 99660:00 - 99705:00

biased way basically take all these in

## 99705:00 - 99740:00

have an llm generate a ton of different

## 99740:00 - 99775:00

variants and then basically make the

## 99775:00 - 99845:00

simulated jury uh so to to basically you

## 99845:00 - 99900:00

know get a representative group of

## 99900:00 - 99935:00

contributors of for Community notes who

## 99935:00 - 99955:00

would be rating the note and try to

## 99955:00 - 99985:00

predict based on their past ratings how

## 99985:00 - 100025:00

they would rate these LM generated notes

## 100025:00 - 100080:00

and so this way you can actually um you

## 100080:00 - 100115:00

know rather than just like having an LM

## 100115:00 - 100140:00

write a note from scratch and hoping

## 100140:00 - 100170:00

it's good you can kind of like simulate

## 100170:00 - 100195:00

the entire Community notes rating

## 100195:00 - 100245:00

process uh and and you know explicitly

## 100245:00 - 100275:00

create notes that are likely to be rated

## 100275:00 - 100315:00

helpful by people so I I think ideas

## 100315:00 - 100365:00

like that um are are very promising uh

## 100365:00 - 100395:00

for the future um

## 100395:00 - 100435:00

and it's a nice way that that LS and

## 100435:00 - 100490:00

humans can work together I think like

## 100490:00 - 100530:00

obviously you know agents can can browse

## 100530:00 - 100575:00

the web too and and and that's one way

## 100575:00 - 100620:00

that you know you could imagine agents

## 100620:00 - 100665:00

assisting humans is you know maybe maybe

## 100665:00 - 100700:00

checking whether a source is actually

## 100700:00 - 100740:00

supported by the note um or a note is

## 100740:00 - 100765:00

actually supported by the source

## 100765:00 - 100800:00

although then you get into things like

## 100800:00 - 100850:00

well uh you know are are people going to

## 100850:00 - 100875:00

actually be as diligent you know right

## 100875:00 - 100910:00

now I think are very diligent because

## 100910:00 - 100945:00

they know just some Community

## 100945:00 - 100965:00

contributor wrote this like I better

## 100965:00 - 101005:00

check this before I read read it helpful

## 101005:00 - 101055:00

but you know hopefully people um we can

## 101055:00 - 101090:00

design things in a way such that uh

## 101090:00 - 101135:00

people don't trust uh the output and

## 101135:00 - 101160:00

actually verify themselves before

## 101160:00 - 101195:00

assuring a helpful rating yeah that is

## 101195:00 - 101235:00

such an interesting area to explore

## 101235:00 - 101280:00

where you want to avoid AI hallucinating

## 101280:00 - 101340:00

sloppy slop uh versus make it easier and

## 101340:00 - 101370:00

scale it even further what an

## 101370:00 - 101395:00

interesting challenge

## 101395:00 - 101425:00

what's cool about this project in

## 101425:00 - 101460:00

addition to this the AI element is that

## 101460:00 - 101490:00

it's being done outside the company like

## 101490:00 - 101515:00

we talked earlier about like trans the

## 101515:00 - 101550:00

open source transparency like the key

## 101550:00 - 101580:00

reason we we made this all open source

## 101580:00 - 101610:00

was so people could see how it worked

## 101610:00 - 101650:00

but the dream is actually that it's the

## 101650:00 - 101685:00

it's not just that the contributions to

## 101685:00 - 101705:00

the notes and ratings are from the

## 101705:00 - 101735:00

people but the dream is actually the

## 101735:00 - 101775:00

product is built by the people like what

## 101775:00 - 101800:00

if the scoring algorithm were

## 101800:00 - 101835:00

significantly or entirely written by the

## 101835:00 - 101875:00

public like that would be incredible and

## 101875:00 - 101925:00

supern is probably the first very

## 101925:00 - 101965:00

substantial potential change in like the

## 101965:00 - 102010:00

algorithm of the way it works that was

## 102010:00 - 102040:00

coming kind of coming from the outside

## 102040:00 - 102080:00

and plausibly could be part of the core

## 102080:00 - 102115:00

um so we'd love to see the product go in

## 102115:00 - 102155:00

that direction as well sweet go super

## 102155:00 - 102205:00

notes well guys the work you're doing is

## 102205:00 - 102265:00

tremendous uh I think uh this is every

## 102265:00 - 102290:00

product person's dream I think to work

## 102290:00 - 102340:00

on something like this small team uh

## 102340:00 - 102385:00

lots of support lots of impact like just

## 102385:00 - 102420:00

like innately interesting and so I think

## 102420:00 - 102455:00

this is going to inspire a lot of people

## 102455:00 - 102475:00

uh so let me just ask you is there

## 102475:00 - 102490:00

anything else you wanted to share

## 102490:00 - 102515:00

anything else you think might be helpful

## 102515:00 - 102555:00

folks to leave them with sure I guess

## 102555:00 - 102590:00

one thing that uh just I thought was

## 102590:00 - 102610:00

interesting over the course of working

## 102610:00 - 102650:00

on this product is just there's uh I

## 102650:00 - 102700:00

think in a similar way to how retweets

## 102700:00 - 102730:00

originally were not something like Jack

## 102730:00 - 102755:00

came up with I think user just started

## 102755:00 - 102780:00

doing it and then it became a core part

## 102780:00 - 102815:00

of the product there's a huge way

## 102815:00 - 102855:00

already in which uh there's just a lot

## 102855:00 - 102890:00

of surprising things that people wanted

## 102890:00 - 102920:00

to use communed notes for that I don't

## 102920:00 - 102960:00

think we really expected and it's it's

## 102960:00 - 103025:00

kind of cool to see those uh you know uh

## 103025:00 - 103070:00

user desires uh kind of emerg I think

## 103070:00 - 103115:00

like one example you know I I guess we'

## 103115:00 - 103170:00

have always been imagining um political

## 103170:00 - 103225:00

uh type of misinformation but um for

## 103225:00 - 103270:00

whatever reason there's like um you know

## 103270:00 - 103305:00

a lot of people who love debating me

## 103305:00 - 103350:00

whether Messi or Ronaldo got more goals

## 103350:00 - 103390:00

uh I guess uh it's kind of kind of a

## 103390:00 - 103435:00

funny one uh that there's a community

## 103435:00 - 103465:00

moderation aspect right so like I think

## 103465:00 - 103495:00

we also thought that you know this would

## 103495:00 - 103550:00

be specifically for um adding context to

## 103550:00 - 103585:00

misleading or potentially misleading

## 103585:00 - 103630:00

information but what you can see is that

## 103630:00 - 103680:00

um there are some notes that um go

## 103680:00 - 103750:00

beyond that um towards like calling out

## 103750:00 - 103790:00

um content that they think is Spam or

## 103790:00 - 103840:00

something um so I I think that's that's

## 103840:00 - 103865:00

just I guess another just another

## 103865:00 - 103905:00

dimension in which Community notes is a

## 103905:00 - 103950:00

a product that's like driven by the

## 103950:00 - 103985:00

people itself that's so beautiful it's

## 103985:00 - 104015:00

basically they're trying to keep Twitter

## 104015:00 - 104055:00

SLX uh healthy and they're just like no

## 104055:00 - 104080:00

this should be taken down this tweet of

## 104080:00 - 104130:00

spam yeah I love that uh is there an

## 104130:00 - 104155:00

answer on the Messi versus who was the

## 104155:00 - 104210:00

other soccer Ronaldo Ronaldo okay is

## 104210:00 - 104235:00

there like a definitive fact there or

## 104235:00 - 104290:00

it's is that just unnown unknowable yeah

## 104290:00 - 104315:00

I guess I guess that's an interesting

## 104315:00 - 104360:00

one because it's a it's a case where

## 104360:00 - 104410:00

Raiders are actually very po ized uh I

## 104410:00 - 104435:00

guess it actually kind of fits into the

## 104435:00 - 104465:00

the core algorithm where there's some

## 104465:00 - 104500:00

people are just die hard Messi fans or

## 104500:00 - 104520:00

Ronaldo fans just so like they could be

## 104520:00 - 104580:00

on politics um so actually you know

## 104580:00 - 104620:00

specifically model that topic uh as well

## 104620:00 - 104670:00

as some other topics so we can like

## 104670:00 - 104700:00

estimate people's opinion on on that

## 104700:00 - 104730:00

particular debate it's kind of kind of

## 104730:00 - 104750:00

funny that something like that would

## 104750:00 - 104775:00

emerge but you're saying that's the most

## 104775:00 - 104835:00

controversial topic on X Ronaldo versus

## 104835:00 - 104885:00

Messi it's a controversial one oh wow

## 104885:00 - 104935:00

who knew okay uh Keith is there anything

## 104935:00 - 104980:00

you wanted to add uh yeah you know

## 104980:00 - 105030:00

Community notes is cool itself but I

## 105030:00 - 105070:00

think what it points to about Society is

## 105070:00 - 105120:00

actually even bigger um you Society

## 105120:00 - 105155:00

often feels really polarized you hear

## 105155:00 - 105175:00

people talk about it all the time like

## 105175:00 - 105205:00

no one can ever agree on anything but

## 105205:00 - 105230:00

actually like Community note shows you

## 105230:00 - 105280:00

people really can agree on quite a lot

## 105280:00 - 105315:00

even on super controversial topics

## 105315:00 - 105345:00

related to politics and everything like

## 105345:00 - 105365:00

there's a lot of agreement that's why

## 105365:00 - 105425:00

this work and I think that's a really

## 105425:00 - 105465:00

big reason for optimism about the world

## 105465:00 - 105500:00

is it while it might feel polarized

## 105500:00 - 105540:00

there's probably like an 80% you know

## 105540:00 - 105590:00

set of people that agree on quite a lot

## 105590:00 - 105630:00

of things and imagine if we could use

## 105630:00 - 105665:00

the same kind of approaches we use with

## 105665:00 - 105710:00

notes but to find agreement on

## 105710:00 - 105755:00

legislation or policies or things like

## 105755:00 - 105795:00

that that people want the government of

## 105795:00 - 105835:00

the world to do like possibly we could

## 105835:00 - 105865:00

get a lot more momentum Behind these

## 105865:00 - 105900:00

ideas that the people really want and

## 105900:00 - 105930:00

everyone would be a lot happier like

## 105930:00 - 105955:00

maybe 10% of the people on the edges

## 105955:00 - 105980:00

wouldn't be happy but like I bet there's

## 105980:00 - 106005:00

a lot of agreement that we are not

## 106005:00 - 106055:00

identifying and if we did it we'd all be

## 106055:00 - 106090:00

pretty happy so I don't know I think

## 106090:00 - 106120:00

it's easy for people to feel pessimistic

## 106120:00 - 106150:00

about the world but I think this is uh

## 106150:00 - 106175:00

this product is a good reason to be

## 106175:00 - 106215:00

optimistic about the future what an

## 106215:00 - 106250:00

incredible way to ended uh I can also

## 106250:00 - 106275:00

see Keith white people want to join you

## 106275:00 - 106315:00

and work with you and work on this team

## 106315:00 - 106365:00

appreciate it if you do want to join we

## 106365:00 - 106420:00

are hiring in an ml engineer you get to

## 106420:00 - 106445:00

work on these amazing problems with us

## 106445:00 - 106485:00

and have a lot of fun so we're accepting

## 106485:00 - 106540:00

applications x.com Community notes okay

## 106540:00 - 106565:00

great I'm glad you give the your all oh

## 106565:00 - 106615:00

man you're about to get flooded uh guys

## 106615:00 - 106655:00

thank you so much for doing this um is

## 106655:00 - 106680:00

there anywhere other than that place to

## 106680:00 - 106720:00

go off uh join the team as an ml ml

## 106720:00 - 106740:00

engineer is there any other place you

## 106740:00 - 106760:00

want to point people to either your

## 106760:00 - 106805:00

socials or anything else I'm K Coleman

## 106805:00 - 106875:00

on X um please reach out if you have any

## 106875:00 - 106905:00

feedack back or want to help us out

## 106905:00 - 106930:00

whether you're want to work here or want

## 106930:00 - 106960:00

to do something from the outside would

## 106960:00 - 107035:00

love to talk yeah I'm atore ja y

## 107035:00 - 107085:00

boterore ATX uh yeah I think in

## 107085:00 - 107115:00

particular you know besides just using

## 107115:00 - 107165:00

communter notes um it it would be great

## 107165:00 - 107225:00

to to get more substantial contributions

## 107225:00 - 107260:00

you know like pull requests um

## 107260:00 - 107300:00

collaborate on projects like supernotes

## 107300:00 - 107330:00

um I think that's the most exciting type

## 107330:00 - 107365:00

of stuff um people do want to contribute

## 107365:00 - 107420:00

ship some code guys yeah amazing guys

## 107420:00 - 107455:00

thank you uh so much for doing this

## 107455:00 - 107495:00

thanks for having us thank you so much

## 107495:00 - 107540:00

bye

## 107540:00 - 107580:00

everyone thank you so much for listening

## 107580:00 - 107600:00

if you found this valuable you can

## 107600:00 - 107640:00

subscribe to the show on Apple podcast

## 107640:00 - 107685:00

Spotify or your favorite podcast app

## 107685:00 - 107720:00

also please consider giving us a rating

## 107720:00 - 107755:00

or leaving a review as that really helps

## 107755:00 - 107795:00

other listeners find the podcast you can

## 107795:00 - 107830:00

find all past episodes or learn more

## 107830:00 - 107880:00

about the show at Lenny podcast.com

## 107880:00+

see you in the next episode

