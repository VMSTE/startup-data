---
source: https://www.youtube.com/watch?v=dP8NmcEkxJI
title: How to measure and improve developer productivity | Nicole Forsgren
  (Microsoft Research, Github)
author: Lenny's Podcast
date: 2023-07-30
views: 32953
description: |-
  Dr. Nicole Forsgren is a developer productivity and DevOps expert who works with engineering organizations to make work better. Best known as co-author of the Shingo Publication Award-winning book Accelerate and the DevOps Handbook, 2nd edition and author of the State of DevOps Reports, she has helped some of the biggest companies in the world transform their culture, processes, tech, and architecture. Nicole is currently a Partner at Microsoft Research, leading developer productivity research and strategy, and a technical founder/CEO with a successful exit to Google. In a previous life, she was a software engineer, sysadmin, hardware performance engineer, and professor. She has published several peer-reviewed journal papers, has been awarded public and private research grants (funders include NASA and the NSF), and has been featured in the Wall Street Journal, Forbes, Computerworld, and InformationWeek. In today’s podcast, we discuss:
  • Two frameworks for measuring developer productivity: DORA and SPACE
  • Benchmarks for what good and great look like
  • Common mistakes to avoid when measuring developer productivity
  • Resources and tools for improving your metrics
  • Signs your developer experience needs attention
  • How to improve your developer experience
  • Nicole’s Four-Box framework for thinking about data and relationships

  —

  This episode is brought to you by DX—a platform for measuring and improving developer productivity: https://getdx.com/lenny

  Find the full transcript at: https://www.lennysnewsletter.com/p/how-to-measure-and-improve-developer

  Where to find Nicole Forsgren:
  • Twitter: https://twitter.com/nicolefv
  • LinkedIn: https://www.linkedin.com/in/nicolefv/
  • Website: https://nicolefv.com/

  Where to find Lenny:
  • Newsletter: https://www.lennysnewsletter.com
  • Twitter: https://twitter.com/lennysan
  • LinkedIn: https://www.linkedin.com/in/lennyrachitsky/

  In this episode, we cover:
  (00:00) Nicole’s background
  (07:55) Unpacking the terms “developer productivity,” “developer experience,” and “DevOps”
  (10:06) How to move faster and improve practices across the board
  (13:43) The DORA framework
  (18:54) Benchmarks for success
  (22:33) Why company size doesn’t matter 
  (24:54) How to improve DevOps capabilities by working backward
  (29:23) The SPACE framework and choosing metrics
  (32:51) How SPACE and DORA work together
  (35:39) Measuring satisfaction
  (37:52) Resources and tools for optimizing metrics 
  (41:29) Nicole’s current book project
  (45:43) Common pitfalls companies run into when rolling out developer productivity/optimizations
  (47:42) How the DevOps space has progressed
  (50:07) The impact of AI on the developer experience and productivity
  (54:04) First steps to take if you’re trying to improve the developer experience
  (55:15) Why Google is an example of a company implementing DevOps solutions well
  (56:11) The importance of clear communication
  (57:32) Nicole’s Four-Box framework
  (1:05:15) Advice on making decisions 
  (1:08:56) Lightning round

  Referenced:
  • Chef: https://www.chef.io/
  • DORA: https://dora.dev/
  • GitHub: https://github.com/
  • Microsoft Research: https://www.microsoft.com/en-us/research/
  • What is DORA?: https://devops.com/what-is-dora-and-why-you-should-care/
  • Dustin Smith on LinkedIn: https://www.linkedin.com/in/dustin-smith-b0525458/
  • Nathen Harvey on LinkedIn: https://www.linkedin.com/in/nathen/
  • What is CI/CD?: https://about.gitlab.com/topics/ci-cd/
  • Trunk-based development: https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development
  • DORA DevOps Quick Check: https://dora.dev/quickcheck/
  • Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations: https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339
  • The SPACE of Developer Productivity: https://queue.acm.org/detail.cfm?id=3454124
  • DevOps Metrics: Nicole Forsgren and Mik Kersten: https://queue.acm.org/detail.cfm?id=3182626
  • How to Measure Anything: Finding the Value of Intangibles in Business: https://www.amazon.com/How-Measure-Anything-Intangibles-Business/dp/1118539273/
  • GitHub Copilot: https://github.com/features/copilot
  • Tabnine: https://www.tabnine.com/the-leading-ai-assistant-for-software-development
  • Nicole’s Decision-Making Spreadsheet: https://docs.google.com/spreadsheets/d/1wItAODkhZ-zKnnFbyDERCd8Hq2NQ03WPvCfigBQ5vpc/edit?usp=sharing
  • How to do linear regression and correlation analysis: https://www.lennysnewsletter.com/p/linear-regression-and-correlation-analysis

  Find all lightning round references at: https://www.lennyspodcast.com/

  Production and marketing by https://penname.co/. For inquiries about sponsoring the podcast, email podcast@lennyrachitsky.com.

  Lenny may be an investor in the companies discussed.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T12:03:01.513Z
---

# How to measure and improve developer productivity | Nicole Forsgren (Microsoft Research, Github)

## 00:00 - 40:00

starting with what is your problem or

## 40:00 - 75:00

what is your goal I would say this is a

## 75:00 - 105:00

bigger challenge than most people

## 105:00 - 140:00

recognize or realize eighty percent of

## 140:00 - 170:00

the folks that I work with this is their

## 170:00 - 195:00

biggest problem even at like executive

## 195:00 - 225:00

levels teams will have gone off for

## 225:00 - 255:00

several months and they're tackling

## 255:00 - 275:00

something and they'll come back with

## 275:00 - 300:00

uncertainty and they'll say like well

## 300:00 - 330:00

you told me to improve developer

## 330:00 - 355:00

experience I'm like okay what do you

## 355:00 - 390:00

mean by this are you talking about inner

## 390:00 - 410:00

and outer loop are you talking about

## 410:00 - 440:00

friction are you talking about culture

## 440:00 - 470:00

but if you're talking about culture this

## 470:00 - 490:00

is totally different than if you're

## 490:00 - 520:00

talking about friction in tool chains if

## 520:00 - 550:00

you're on different pages you're heading

## 550:00 - 615:00

in completely different directions

## 615:00 - 660:00

welcome to Lenny's podcast where I

## 660:00 - 685:00

interview world-class product leaders

## 685:00 - 710:00

and growth experts to learn from their

## 710:00 - 735:00

hard-winning experiences building and

## 735:00 - 765:00

growing today's most successful products

## 765:00 - 820:00

today my guest is Nicole forsgren this

## 820:00 - 840:00

is actually my first recording back

## 840:00 - 870:00

since going on Batley for the past

## 870:00 - 900:00

couple of months and what an awesome

## 900:00 - 930:00

episode to get back into the swing of

## 930:00 - 975:00

things Nicole is the developer

## 975:00 - 1010:00

productivity expert having written the

## 1010:00 - 1045:00

award-winning book accelerate and she's

## 1045:00 - 1075:00

been the co-author of the state of

## 1075:00 - 1110:00

devops report year after year she's

## 1110:00 - 1135:00

currently a partner at Microsoft

## 1135:00 - 1170:00

research leading developer productivity

## 1170:00 - 1210:00

research and strategy and she's helped

## 1210:00 - 1225:00

some of the biggest companies in the

## 1225:00 - 1260:00

world move faster improve product

## 1260:00 - 1310:00

quality and transform their cultures in

## 1310:00 - 1340:00

our conversation we get into the weeds

## 1340:00 - 1375:00

of how to go about measuring and

## 1375:00 - 1400:00

improving your engineering team's

## 1400:00 - 1435:00

productivity and experience we talk

## 1435:00 - 1465:00

about the Dora framework and the space

## 1465:00 - 1495:00

framework and how to actually Implement

## 1495:00 - 1525:00

them to understand how your engineering

## 1525:00 - 1560:00

team is doing Nicole also shares

## 1560:00 - 1590:00

benchmarks for what Elite companies are

## 1590:00 - 1640:00

at we talk about why moving faster turns

## 1640:00 - 1660:00

out to be one of the best ways to

## 1660:00 - 1700:00

improve quality and stability plus

## 1700:00 - 1735:00

pitfalls you want to avoid and also a

## 1735:00 - 1765:00

preview of a new book that she's working

## 1765:00 - 1805:00

on and so much more enjoy this episode

## 1805:00 - 1850:00

with Nicole forsgrin after a short word

## 1850:00 - 1890:00

from our sponsors

## 1890:00 - 1930:00

today's entire episode is brought to you

## 1930:00 - 1970:00

by DX a platform for measuring and

## 1970:00 - 2015:00

improving developer productivity DX is

## 2015:00 - 2040:00

designed by the researchers behind

## 2040:00 - 2085:00

Frameworks such as Dora space and devex

## 2085:00 - 2125:00

including Nicole forsgren who is my

## 2125:00 - 2160:00

guest for this very episode if you've

## 2160:00 - 2190:00

tried measuring developer productivity

## 2190:00 - 2210:00

you know that there are a lot of basic

## 2210:00 - 2240:00

metrics out there and a lot of ways to

## 2240:00 - 2275:00

do this wrong and getting that full view

## 2275:00 - 2320:00

of productivity is still really hard DX

## 2320:00 - 2345:00

tackles this problem by combining

## 2345:00 - 2380:00

qualitative and quantitative insights

## 2380:00 - 2410:00

based on the very research Nicole and

## 2410:00 - 2435:00

her team have done giving you full

## 2435:00 - 2465:00

clarity into how your developers are

## 2465:00 - 2505:00

doing DX is used by both startups and

## 2505:00 - 2540:00

Fortune 500 companies including

## 2540:00 - 2595:00

companies like twilio amplitude eBay Rex

## 2595:00 - 2650:00

toast Pfizer and Procter Gamble to learn

## 2650:00 - 2680:00

more about DX and get a demo of their

## 2680:00 - 2730:00

product visit their website at getdx.com

## 2730:00 - 2810:00

Lenny that's getdx.com Lenny

## 2810:00 - 2855:00

thank you

## 2855:00 - 2905:00

Nicole Welcome to the podcast

## 2905:00 - 2940:00

thank you so much I'm excited to be here

## 2940:00 - 2980:00

I'm excited to have you here I actually

## 2980:00 - 3010:00

skipped this question usually with

## 3010:00 - 3035:00

guests but I thought it'd be actually

## 3035:00 - 3055:00

really valuable to spend a little time

## 3055:00 - 3085:00

on your background you have such a

## 3085:00 - 3115:00

unique role and unique set of

## 3115:00 - 3155:00

experiences could you just talk briefly

## 3155:00 - 3185:00

about the things you've been up to in

## 3185:00 - 3220:00

your career where you've worked and then

## 3220:00 - 3245:00

what you're up to now and what you focus

## 3245:00 - 3285:00

on these days sure and I appreciate the

## 3285:00 - 3315:00

question because you're right I sort of

## 3315:00 - 3350:00

had this like Choose Your Own Adventure

## 3350:00 - 3385:00

background so I started as a software

## 3385:00 - 3455:00

engineer at IBM I was uh writing

## 3455:00 - 3480:00

software for like large Enterprise

## 3480:00 - 3520:00

systems which meant I ended up running

## 3520:00 - 3560:00

them I was so I was also a sis admin I

## 3560:00 - 3595:00

was wrecking the stacking I was I was

## 3595:00 - 3620:00

running these really really large labs

## 3620:00 - 3675:00

and then I kind of stumbled into this

## 3675:00 - 3705:00

seven day March for several years and I

## 3705:00 - 3740:00

was like there has to be a better way

## 3740:00 - 3765:00

and we're hearing like rumors of it but

## 3765:00 - 3805:00

like management was not buying in and so

## 3805:00 - 3865:00

I decided to win this battle with data

## 3865:00 - 3915:00

and I was like I should go do a PhD me

## 3915:00 - 3960:00

and so ended up kind of taking a slight

## 3960:00 - 4025:00

pivot into uh PhD and management

## 4025:00 - 4065:00

information systems which some people

## 4065:00 - 4085:00

are less familiar with but it's

## 4085:00 - 4125:00

basically a cross between Tech and

## 4125:00 - 4165:00

business and I ended up getting a fairly

## 4165:00 - 4220:00

technical PhD so I went to a school I

## 4220:00 - 4250:00

went to University of Arizona which has

## 4250:00 - 4295:00

a very very technical degree but I liked

## 4295:00 - 4320:00

that it crossed with business because

## 4320:00 - 4365:00

then I had the ability to make these

## 4365:00 - 4400:00

strong business case statements right so

## 4400:00 - 4475:00

it was like how is or is the way that we

## 4475:00 - 4515:00

develop and deliver software tied to

## 4515:00 - 4550:00

outcomes at the individual level right

## 4550:00 - 4605:00

can I be more productive can I have

## 4605:00 - 4640:00

better work-life balance and the team

## 4640:00 - 4670:00

level is the team more productive is the

## 4670:00 - 4700:00

team more efficient and the

## 4700:00 - 4735:00

organizational level right this is what

## 4735:00 - 4765:00

I was really interested in originally do

## 4765:00 - 4800:00

I see better Roi do I see better

## 4800:00 - 4840:00

efficiency because then I could sell it

## 4840:00 - 4880:00

to people right and so that was really

## 4880:00 - 4915:00

kind of what I originally went into and

## 4915:00 - 4945:00

and I was a professor for a handful of

## 4945:00 - 4965:00

years because like if you're doing

## 4965:00 - 5000:00

research like traditionally that's

## 5000:00 - 5030:00

that's the job in Academia I also had a

## 5030:00 - 5060:00

master's in accounting because that

## 5060:00 - 5080:00

really helped me make that kind of like

## 5080:00 - 5105:00

Financial tie and understanding

## 5105:00 - 5145:00

financial statements and then after you

## 5145:00 - 5170:00

know a handful of years kind of walked

## 5170:00 - 5220:00

away from tenure because Academia was

## 5220:00 - 5245:00

not convinced that devops was a thing

## 5245:00 - 5300:00

right the devops wasn't real and stayed

## 5300:00 - 5335:00

a devops report who we you know I was

## 5335:00 - 5365:00

doing with Dora devops research and

## 5365:00 - 5405:00

assessment uh in collaboration with just

## 5405:00 - 5445:00

humble and Gene Kim and we started that

## 5445:00 - 5480:00

work with puppet so shout out to Alana

## 5480:00 - 5510:00

Brown for starting that Nigel Karsten

## 5510:00 - 5555:00

and the the team there uh we kind of

## 5555:00 - 5615:00

pivoted away and you know Chef uh the

## 5615:00 - 5640:00

little configuration management startup

## 5640:00 - 5685:00

at the time uh hired me and they're like

## 5685:00 - 5715:00

we'll give you half time to do research

## 5715:00 - 5735:00

and have time to help our engineering

## 5735:00 - 5785:00

practices improve that's cool yeah I

## 5785:00 - 5810:00

mean they were incredible because like

## 5810:00 - 5835:00

what startup is gonna be like yeah do

## 5835:00 - 5870:00

research so I was there for a year and a

## 5870:00 - 5915:00

half and then left to you know do door

## 5915:00 - 5955:00

full time we had it we actually had a

## 5955:00 - 5990:00

SAS offering so we continued this data

## 5990:00 - 6025:00

devops report just under the Dora banner

## 6025:00 - 6065:00

and we had a SAS offering because so

## 6065:00 - 6100:00

many large companies were like I want my

## 6100:00 - 6125:00

own customized

## 6125:00 - 6190:00

measurement reading and report and then

## 6190:00 - 6220:00

the joke there you know when we met with

## 6220:00 - 6240:00

Gartner they were like you know your

## 6240:00 - 6265:00

superpower here was that you tricked

## 6265:00 - 6300:00

people into strategy which was not only

## 6300:00 - 6335:00

how do I Benchmark that was kind of our

## 6335:00 - 6355:00

top of the funnel because everyone wants

## 6355:00 - 6375:00

to know how they compare

## 6375:00 - 6405:00

but the important thing is what should

## 6405:00 - 6445:00

you do next what's the most important

## 6445:00 - 6485:00

Next Step so it's how do I measure what

## 6485:00 - 6505:00

do I do next

## 6505:00 - 6555:00

and that gave me this incredible view

## 6555:00 - 6585:00

into

## 6585:00 - 6650:00

advising large organizations into this

## 6650:00 - 6685:00

transformation journey and then we built

## 6685:00 - 6705:00

out this amazing partner Network because

## 6705:00 - 6730:00

we weren't actually Consulting we just

## 6730:00 - 6755:00

had this SAS piece but then how do you

## 6755:00 - 6800:00

act on it we were then acquired by

## 6800:00 - 6835:00

Google so I was CEO and co-founder so I

## 6835:00 - 6865:00

kind of LED that that acquisition and

## 6865:00 - 6885:00

then the integration and building out

## 6885:00 - 6920:00

these teams in Google and after that

## 6920:00 - 6975:00

point uh I joined GitHub which is you

## 6975:00 - 7010:00

know this the largest uh developer

## 7010:00 - 7035:00

Network so I had this amazing

## 7035:00 - 7075:00

opportunity to do more grounded and

## 7075:00 - 7105:00

applied research again I was VP research

## 7105:00 - 7160:00

and strategy and uh then I went over to

## 7160:00 - 7195:00

MSR where I kind of wear a couple hats

## 7195:00 - 7245:00

so right now I have a research lab there

## 7245:00 - 7285:00

with an incredible team uh it's the

## 7285:00 - 7315:00

developer experience lab where we do a

## 7315:00 - 7345:00

bunch of work across productivity

## 7345:00 - 7380:00

community and well-being

## 7380:00 - 7435:00

and then I also help with Microsoft's

## 7435:00 - 7475:00

you know kind of cross company effort to

## 7475:00 - 7510:00

improve their developer infrastructure

## 7510:00 - 7545:00

so it's like sort of kind of this this

## 7545:00 - 7605:00

round effort into like how do I really

## 7605:00 - 7670:00

remain engaged in measuring applying

## 7670:00 - 7710:00

thinking about this work both in like

## 7710:00 - 7765:00

very applied concrete pieces and

## 7765:00 - 7810:00

Incredibly forward-looking work with MSR

## 7810:00 - 7855:00

amazing and just to clarify MSR this is

## 7855:00 - 7895:00

at Microsoft yeah thank you yeah MSR is

## 7895:00 - 7940:00

Microsoft research Okay cool so you've

## 7940:00 - 7975:00

shared a couple of these terms devops

## 7975:00 - 8015:00

developer productivity I'm curious what

## 8015:00 - 8060:00

the term you like to use for this area

## 8060:00 - 8100:00

you focus on develop productivity

## 8100:00 - 8130:00

developer experience devops what's kind

## 8130:00 - 8150:00

of the way the best way to think about

## 8150:00 - 8185:00

this I really love that you asked this

## 8185:00 - 8215:00

question because I think they're very

## 8215:00 - 8250:00

related Concepts that people sometimes

## 8250:00 - 8290:00

you know conflate but but I see them as

## 8290:00 - 8325:00

being different so related but different

## 8325:00 - 8365:00

so productivity I think is you know

## 8365:00 - 8400:00

basically how much we can get done and

## 8400:00 - 8430:00

how much we can do over time

## 8430:00 - 8460:00

and I think that's why it's so important

## 8460:00 - 8480:00

to have this holistic measure right

## 8480:00 - 8510:00

because we can't just brute force it

## 8510:00 - 8555:00

right so that's why when my team and I

## 8555:00 - 8595:00

and a bunch of my peers study

## 8595:00 - 8620:00

productivity we include this community

## 8620:00 - 8655:00

effect right because software is a team

## 8655:00 - 8690:00

sport we joke right and also why

## 8690:00 - 8725:00

well-being is so important right because

## 8725:00 - 8760:00

we see that when you do productivity the

## 8760:00 - 8795:00

right way we see sustainability we see

## 8795:00 - 8830:00

well-being we see reductions in Burnout

## 8830:00 - 8895:00

now developer experience is very related

## 8895:00 - 8935:00

and very tied to this and it contributes

## 8935:00 - 8975:00

to productivity but developer

## 8975:00 - 9005:00

experiences like if you think about who

## 9005:00 - 9035:00

your users are right developers really

## 9035:00 - 9090:00

are you are your users in this software

## 9090:00 - 9125:00

engineering in the software development

## 9125:00 - 9170:00

piece and so it's you know developer

## 9170:00 - 9200:00

experience is sort of like what is it

## 9200:00 - 9235:00

like to write software is this a

## 9235:00 - 9260:00

friction free process is this a very

## 9260:00 - 9325:00

predictable and certain experience right

## 9325:00 - 9370:00

can we reduce this uncertainty and

## 9370:00 - 9400:00

increase the predictability here to

## 9400:00 - 9440:00

contribute to productivity

## 9440:00 - 9475:00

and then how does devops fit into that

## 9475:00 - 9495:00

just so that we kind of have the mental

## 9495:00 - 9540:00

model of these terms people have sort of

## 9540:00 - 9560:00

co-opted the terms and some people named

## 9560:00 - 9595:00

their tools devops I'm maybe a little

## 9595:00 - 9650:00

more old school so uh when I was doing a

## 9650:00 - 9685:00

bunch of my devops research it was the

## 9685:00 - 9720:00

capabilities and tools and processes

## 9720:00 - 9765:00

that we can use to improve our software

## 9765:00 - 9805:00

development and delivery end to end so

## 9805:00 - 9835:00

that it's faster and it is more reliable

## 9835:00 - 9885:00

so devops was kind of this technical

## 9885:00 - 9935:00

architectural cultural practices that

## 9935:00 - 9975:00

enable us to do this work better so that

## 9975:00 - 10025:00

it is yes like more productive we have a

## 10025:00 - 10055:00

better developer experience that was

## 10055:00 - 10080:00

kind of this like again this very

## 10080:00 - 10120:00

holistic picture so what I love about

## 10120:00 - 10160:00

this topic is that I've never met a

## 10160:00 - 10215:00

founder or a leader who is not thinking

## 10215:00 - 10250:00

we need to move faster we need our

## 10250:00 - 10285:00

Engineers to be more productive we need

## 10285:00 - 10320:00

to get things out the door quicker we

## 10320:00 - 10360:00

want Engineers to be happier like nobody

## 10360:00 - 10405:00

doesn't want that and so that's why I'm

## 10405:00 - 10425:00

excited to dig into a lot of these

## 10425:00 - 10455:00

things is that roughly what you find as

## 10455:00 - 10485:00

well that nobody's ever like we're good

## 10485:00 - 10510:00

we don't need any of this we don't need

## 10510:00 - 10545:00

to focus on this area you know what I'll

## 10545:00 - 10615:00

say yes and right so

## 10615:00 - 10650:00

and it kind of goes back to like why I

## 10650:00 - 10690:00

got into this because on the one hand

## 10690:00 - 10740:00

you won't say anyone who's saying uh

## 10740:00 - 10770:00

like we're we don't really need to go

## 10770:00 - 10815:00

faster everything's fine but at the same

## 10815:00 - 10875:00

time very often I will come into

## 10875:00 - 10905:00

scenarios or I'll find myself in

## 10905:00 - 10935:00

scenarios where people are like

## 10935:00 - 10965:00

I mean it would be nice if we were going

## 10965:00 - 11015:00

faster but do we really need to show me

## 11015:00 - 11075:00

the business case what's the ROI or if

## 11075:00 - 11120:00

we go too fast we'll have an instability

## 11120:00 - 11170:00

right what are our safety measures are

## 11170:00 - 11210:00

we going to lose reliability what is

## 11210:00 - 11230:00

happening right when I first started

## 11230:00 - 11285:00

like ITIL and itsm right the the old

## 11285:00 - 11305:00

school kind of change management

## 11305:00 - 11330:00

processes

## 11330:00 - 11395:00

the common knowledge was that you had to

## 11395:00 - 11430:00

have at least a two-week

## 11430:00 - 11475:00

wait for change approvals in order to

## 11475:00 - 11510:00

get that stability turns out that's not

## 11510:00 - 11555:00

right right it was just kind of

## 11555:00 - 11600:00

an old wives tale right

## 11600:00 - 11665:00

and so we kind of have this weird

## 11665:00 - 11725:00

balance of I want to move faster but is

## 11725:00 - 11750:00

it worth the investment

## 11750:00 - 11800:00

what am I gonna get for it are you sure

## 11800:00 - 11870:00

this is the priority or I've been in

## 11870:00 - 11910:00

I've been in meetings where it's like oh

## 11910:00 - 11960:00

yes absolutely right like this is this

## 11960:00 - 11990:00

is a priority but it's the lowest

## 11990:00 - 12020:00

priority and I'm like

## 12020:00 - 12075:00

right so so then what we want to do is

## 12075:00 - 12105:00

we want to have these

## 12105:00 - 12155:00

these kind of pointed conversations or

## 12155:00 - 12185:00

these kind of like Socratic type

## 12185:00 - 12210:00

questions and conversations where it's

## 12210:00 - 12260:00

like help me understand more what your

## 12260:00 - 12295:00

concerns are are your concerns around

## 12295:00 - 12335:00

reliability when you move faster we're

## 12335:00 - 12365:00

not just trying to like all the guard

## 12365:00 - 12420:00

rails down and Sprint for no purpose of

## 12420:00 - 12440:00

sprinting and this is where kind of the

## 12440:00 - 12480:00

Dora and devops research program comes

## 12480:00 - 12525:00

into play where it's we don't just want

## 12525:00 - 12555:00

to move fast and take all guard rails

## 12555:00 - 12595:00

down we want to implement good technical

## 12595:00 - 12620:00

practices like

## 12620:00 - 12665:00

automated testing good architectural

## 12665:00 - 12710:00

practices so that when you move fast you

## 12710:00 - 12760:00

are also more stable right we want to be

## 12760:00 - 12785:00

thinking about improving the developer

## 12785:00 - 12820:00

experience so that when we are faster we

## 12820:00 - 12850:00

are also Saving Time right and then we

## 12850:00 - 12875:00

can highlight a handful of Statistics

## 12875:00 - 12925:00

like what is your

## 12925:00 - 12980:00

typical time for feature delivery what

## 12980:00 - 13025:00

is your typical time to First PR what is

## 13025:00 - 13065:00

your typical time to steady state

## 13065:00 - 13095:00

productivity what is your typical time

## 13095:00 - 13170:00

for code review and PR process and if we

## 13170:00 - 13215:00

are to do like back of the napkin math

## 13215:00 - 13275:00

what sorts of time are you spending here

## 13275:00 - 13320:00

and if we do a rough look at industry

## 13320:00 - 13365:00

what are your peers spending here

## 13365:00 - 13425:00

and are we losing time right and if we

## 13425:00 - 13445:00

could turn this into

## 13445:00 - 13495:00

a value calculation

## 13495:00 - 13530:00

what does that look like so that we can

## 13530:00 - 13555:00

think about

## 13555:00 - 13605:00

the priority and the strategy here and

## 13605:00 - 13670:00

and I think that's where it becomes

## 13670:00 - 13725:00

a more focused conversation

## 13725:00 - 13755:00

this is a great segue too something I

## 13755:00 - 13770:00

was going to get to a little bit later

## 13770:00 - 13805:00

but let's just get into it which is the

## 13805:00 - 13845:00

Dora framework and then there's also the

## 13845:00 - 13875:00

space framework can you just talk about

## 13875:00 - 13900:00

what these two are when you use one

## 13900:00 - 13925:00

versus the other and then how that

## 13925:00 - 13960:00

essentially helps you measure and then

## 13960:00 - 13995:00

improve productivity and and uh and

## 13995:00 - 14035:00

developer experience sure sure

## 14035:00 - 14060:00

absolutely and I'm so glad you brought

## 14060:00 - 14115:00

this up so Dora is it's an entire

## 14115:00 - 14145:00

research program now many people when

## 14145:00 - 14185:00

they hear Dora now they think of the

## 14185:00 - 14220:00

Four Keys or the Dora four or the four

## 14220:00 - 14260:00

metrics and I think that's what the

## 14260:00 - 14295:00

research program and and the company

## 14295:00 - 14350:00

ended up becoming most known for and so

## 14350:00 - 14385:00

that was the software delivery

## 14385:00 - 14450:00

performance metrics and those are

## 14450:00 - 14475:00

there's two speed and two stability

## 14475:00 - 14515:00

metrics so the speed metrics are lead

## 14515:00 - 14560:00

time so how long does it take to get

## 14560:00 - 14585:00

from code committed to code running in

## 14585:00 - 14635:00

production deployment frequency how

## 14635:00 - 14670:00

often do you deploy code

## 14670:00 - 14735:00

and then the stability metrics are mttr

## 14735:00 - 14770:00

uh meantime to restore so if something

## 14770:00 - 14800:00

happens how long does it take you to

## 14800:00 - 14855:00

come back and then change fail rate for

## 14855:00 - 14905:00

every change that is pushed you know

## 14905:00 - 14955:00

what's the rough percentage of incidents

## 14955:00 - 14995:00

or like that require human intervention

## 14995:00 - 15030:00

right now the thing that was really

## 15030:00 - 15065:00

interesting is when we started measuring

## 15065:00 - 15135:00

these we found that they move in tandem

## 15135:00 - 15170:00

now like with

## 15170:00 - 15235:00

very strong significance right from a

## 15235:00 - 15265:00

statistical standpoint now what this

## 15265:00 - 15300:00

means is now we say speed and stability

## 15300:00 - 15335:00

move together most people only think

## 15335:00 - 15360:00

about this from the speed standpoint

## 15360:00 - 15385:00

which means when you move faster you are

## 15385:00 - 15405:00

more stable

## 15405:00 - 15430:00

which means you're you're pushing

## 15430:00 - 15460:00

smaller changes more often right so if

## 15460:00 - 15480:00

you're pushing all the time it's going

## 15480:00 - 15500:00

to be very very small changes which

## 15500:00 - 15530:00

means you have a smaller blast radius

## 15530:00 - 15570:00

which means when you push you have an

## 15570:00 - 15600:00

error in production it's going to be

## 15600:00 - 15640:00

easier to debug right uh it's going to

## 15640:00 - 15675:00

be much easier to figure all that out uh

## 15675:00 - 15705:00

your mean time to restore and mitigate

## 15705:00 - 15735:00

it's going to be much faster

## 15735:00 - 15780:00

but that also means is the reverse when

## 15780:00 - 15825:00

you push changes less frequently you

## 15825:00 - 15875:00

will have more unstable systems because

## 15875:00 - 15910:00

when you push less frequency you will

## 15910:00 - 15965:00

have very very large batch changes which

## 15965:00 - 16015:00

means you'll have a very high very large

## 16015:00 - 16050:00

blast radius which means when you do

## 16050:00 - 16090:00

have a resulting

## 16090:00 - 16155:00

bug error you will have to disentangle

## 16155:00 - 16200:00

this big you know

## 16200:00 - 16240:00

ball of mud right and figure out which

## 16240:00 - 16280:00

piece actually caused the error

## 16280:00 - 16330:00

figure all of that out

## 16330:00 - 16380:00

that ended up being a big surprise right

## 16380:00 - 16395:00

because

## 16395:00 - 16430:00

refer to my prior comment about I you

## 16430:00 - 16480:00

know ITIL and itsm if you're forcing a

## 16480:00 - 16510:00

two-week

## 16510:00 - 16565:00

pause for change approvals

## 16565:00 - 16595:00

you're causing this batching up of

## 16595:00 - 16615:00

changes and sometimes people were

## 16615:00 - 16650:00

waiting if two weeks is good a month

## 16650:00 - 16680:00

must be better or three months must be

## 16680:00 - 16715:00

better or six months must be better and

## 16715:00 - 16735:00

I mean just think about the merge

## 16735:00 - 16765:00

conflicts you're causing right you're

## 16765:00 - 16805:00

just causing so many challenges and

## 16805:00 - 16830:00

figuring out how to push this code into

## 16830:00 - 16860:00

production

## 16860:00 - 16890:00

so many people think of those four

## 16890:00 - 16925:00

metrics one because we found that speed

## 16925:00 - 16950:00

and stability moved together and two

## 16950:00 - 16985:00

because we started publishing benchmarks

## 16985:00 - 17045:00

on what this looks like for low medium

## 17045:00 - 17075:00

high and then Elite performers for many

## 17075:00 - 17095:00

times

## 17095:00 - 17140:00

this I believe may have been interesting

## 17140:00 - 17180:00

uh I'm not sure if it was useful or

## 17180:00 - 17210:00

helpful but I think it was interesting

## 17210:00 - 17265:00

because it gave people at least

## 17265:00 - 17300:00

something to shoot for something to aim

## 17300:00 - 17340:00

for I will definitely say what's most

## 17340:00 - 17370:00

important is knowing where you are and

## 17370:00 - 17405:00

the progress that you're making right it

## 17405:00 - 17440:00

doesn't matter if frankly you're a high

## 17440:00 - 17480:00

performer or you're an elite performer

## 17480:00 - 17510:00

it matters that you know where you are

## 17510:00 - 17550:00

and you're making progress right

## 17550:00 - 17590:00

you know can you push daily or on demand

## 17590:00 - 17610:00

or

## 17610:00 - 17655:00

is your only technical capability you

## 17655:00 - 17700:00

can push twice a year right just know

## 17700:00 - 17725:00

where you are and is it a business

## 17725:00 - 17750:00

decision or a technical capability

## 17750:00 - 17780:00

that's basically what it comes down to

## 17780:00 - 17815:00

I'm gonna jump in real quick just to

## 17815:00 - 17845:00

highlight what you're talking what you

## 17845:00 - 17875:00

just said which I think is extremely

## 17875:00 - 17905:00

important and powerful and people might

## 17905:00 - 17960:00

kind of move on too quickly uh I also

## 17960:00 - 17980:00

want to ask you what actual benchmarks

## 17980:00 - 18010:00

are if you can share those whatever you

## 18010:00 - 18025:00

want to share there but before I ask

## 18025:00 - 18055:00

that essentially what you're sharing

## 18055:00 - 18100:00

right now is just I feel like the 64 000

## 18100:00 - 18145:00

question of this episode is just how do

## 18145:00 - 18200:00

I move faster as a team and what I'm

## 18200:00 - 18245:00

hearing is essentially it's ship smaller

## 18245:00 - 18290:00

things is kind of at the core of it and

## 18290:00 - 18345:00

also if we're if quality is low you're

## 18345:00 - 18385:00

also saying the answer is more

## 18385:00 - 18415:00

often ship smaller things is that

## 18415:00 - 18465:00

roughly the message yes absolutely it

## 18465:00 - 18510:00

ends up being much much safer amazing so

## 18510:00 - 18535:00

I think that's an extremely important

## 18535:00 - 18590:00

takeaway uh that I think people would I

## 18590:00 - 18615:00

don't know that's surprising to me to

## 18615:00 - 18655:00

hear that it's uh quality comes from

## 18655:00 - 18700:00

Shipping faster and and also to ship

## 18700:00 - 18725:00

faster and move help your team move

## 18725:00 - 18765:00

faster it's Chip smaller things and and

## 18765:00 - 18810:00

just deploy more often yep amazing okay

## 18810:00 - 18850:00

great I know we'll talk more about this

## 18850:00 - 18875:00

but let me go back to the question I was

## 18875:00 - 18915:00

going to ask because yeah okay are you

## 18915:00 - 18940:00

are there benchmarks you can share just

## 18940:00 - 18965:00

right now that you think would be useful

## 18965:00 - 18980:00

to people and they said it was

## 18980:00 - 19000:00

interesting and maybe not as useful to

## 19000:00 - 19040:00

people as you imagine yeah uh so I will

## 19040:00 - 19110:00

admit I I only have the 2019 benchmarks

## 19110:00 - 19145:00

top of mind the team at Google has

## 19145:00 - 19180:00

continued that work since I left uh it's

## 19180:00 - 19240:00

been led by uh Dr Dustin Smith Nathan

## 19240:00 - 19280:00

Harvey continues the work so huge shout

## 19280:00 - 19310:00

out to that team many others uh

## 19310:00 - 19370:00

participate you can go to dora.dev and

## 19370:00 - 19405:00

find all of the continued reports

## 19405:00 - 19445:00

they've integrated all of this work but

## 19445:00 - 19475:00

I will say they've they've remained

## 19475:00 - 19510:00

fairly consistent so so really quickly

## 19510:00 - 19555:00

I'll share the Elite Performance so

## 19555:00 - 19585:00

deployment frequency you can deploy on

## 19585:00 - 19600:00

demand

## 19600:00 - 19640:00

lead time for changes takes less than a

## 19640:00 - 19685:00

day time to restore is less than an hour

## 19685:00 - 19720:00

and your change fail rate is between

## 19720:00 - 19760:00

zero and fifteen percent amazing okay

## 19760:00 - 19785:00

I'm writing these down these are

## 19785:00 - 19825:00

extremely valuable and I will mention

## 19825:00 - 19850:00

people will say well this is kind of

## 19850:00 - 19865:00

like

## 19865:00 - 19900:00

a chunk of time right it's not super

## 19900:00 - 19930:00

precise

## 19930:00 - 19965:00

Precision isn't really super important

## 19965:00 - 19990:00

here right like I don't it doesn't

## 19990:00 - 20025:00

really matter if you can like if your

## 20025:00 - 20050:00

lead time is

## 20050:00 - 20080:00

if it's less than a day it's less than a

## 20080:00 - 20110:00

day right like that's fine from a

## 20110:00 - 20125:00

business

## 20125:00 - 20160:00

perspective it doesn't matter if it's

## 20160:00 - 20185:00

like

## 20185:00 - 20230:00

four hours or like four hours and two

## 20230:00 - 20280:00

minutes right

## 20280:00 - 20330:00

General categories

## 20330:00 - 20370:00

are fine now I will say like the next

## 20370:00 - 20395:00

category for lead time for changes by

## 20395:00 - 20450:00

the day is if uh lead time is between a

## 20450:00 - 20490:00

day and a week and this is for for good

## 20490:00 - 20525:00

for hot yeah between Elite and high

## 20525:00 - 20555:00

Elite is less than a day and high is

## 20555:00 - 20585:00

between a day and a week

## 20585:00 - 20615:00

and then it goes between a week and a

## 20615:00 - 20650:00

month and between a month and six months

## 20650:00 - 20705:00

right so so you can ask people and they

## 20705:00 - 20725:00

can tell you right they can kind of

## 20725:00 - 20745:00

hunch it

## 20745:00 - 20790:00

and this is from it's a committing code

## 20790:00 - 20830:00

into the repo and going out into

## 20830:00 - 20890:00

production to it to about like ring zero

## 20890:00 - 20930:00

so you don't like don't worry if it's

## 20930:00 - 20960:00

like oh well now we need to think about

## 20960:00 - 20990:00

like the global deploy and like which is

## 20990:00 - 21030:00

the final endpoint it's like how long

## 21030:00 - 21075:00

does it take to get

## 21075:00 - 21150:00

through your deployment pipeline because

## 21150:00 - 21190:00

are you going to be surprised do you

## 21190:00 - 21240:00

have fast feedback loops how does your

## 21240:00 - 21290:00

deployment pipeline work does your

## 21290:00 - 21345:00

deployment pipeline work right

## 21345:00 - 21385:00

or are you going to commit code

## 21385:00 - 21410:00

are you going to wait for that final

## 21410:00 - 21455:00

review for about three months

## 21455:00 - 21485:00

is something going to happen or break

## 21485:00 - 21520:00

and when it comes back to the developer

## 21520:00 - 21540:00

because something happened or broke

## 21540:00 - 21580:00

because that kind of happens right are

## 21580:00 - 21615:00

they going to have to insert themselves

## 21615:00 - 21640:00

back in the code re-review all the

## 21640:00 - 21665:00

things that happened three months ago

## 21665:00 - 21710:00

all so many other things happened

## 21710:00 - 21750:00

that's incredibly difficult which to

## 21750:00 - 21790:00

your prior question this is how it

## 21790:00 - 21830:00

relates to the developer experience if

## 21830:00 - 21880:00

something happened less than a day and

## 21880:00 - 21905:00

like it's a surprise and it's not great

## 21905:00 - 21930:00

but like whatever right something

## 21930:00 - 21975:00

happened Downstream and I gotta fix it

## 21975:00 - 22020:00

I'm still sitting in my code right in my

## 22020:00 - 22050:00

head I've got that mental model I know

## 22050:00 - 22085:00

what happened maybe it's not great but

## 22085:00 - 22100:00

it's fine

## 22100:00 - 22150:00

if it happened three months ago

## 22150:00 - 22190:00

and I get interrupted first of all

## 22190:00 - 22225:00

interruptions like suck that's not fun

## 22225:00 - 22275:00

second of all now I've got a like

## 22275:00 - 22300:00

re-remember

## 22300:00 - 22365:00

re-read all of this code maybe reload an

## 22365:00 - 22400:00

entire new workspace instead of

## 22400:00 - 22425:00

libraries and everything because I

## 22425:00 - 22465:00

maybe it's a whole quarter ago and like

## 22465:00 - 22520:00

we thought we were done

## 22520:00 - 22550:00

and I got to do the whole thing all over

## 22550:00 - 22600:00

if a listener is working at a startup I

## 22600:00 - 22615:00

imagine they're hearing this and they're

## 22615:00 - 22670:00

like takes a data ship that we ship all

## 22670:00 - 22705:00

day a thousand times a day I imagine

## 22705:00 - 22745:00

these benchmarks are more valuable for

## 22745:00 - 22775:00

larger companies is there a kind of

## 22775:00 - 22815:00

buckets you think about for like here's

## 22815:00 - 22850:00

the size of company this is meant for

## 22850:00 - 22875:00

and then do you think about anything

## 22875:00 - 22900:00

differently for a startup say I don't

## 22900:00 - 22945:00

know 10 people if anyone is only

## 22945:00 - 22975:00

listening to this I just got the biggest

## 22975:00 - 23025:00

smile because we saw no statistical

## 23025:00 - 23075:00

significance between small companies and

## 23075:00 - 23105:00

large companies the only statistical

## 23105:00 - 23140:00

significant statistically significant

## 23140:00 - 23170:00

difference was with retail I'll come

## 23170:00 - 23210:00

back to that it's so funny because large

## 23210:00 - 23250:00

companies would say oh but this isn't

## 23250:00 - 23280:00

fair for us we have more complex code

## 23280:00 - 23325:00

bases we have so many things to do small

## 23325:00 - 23350:00

companies just don't have to deal with

## 23350:00 - 23380:00

this small companies would come to me

## 23380:00 - 23405:00

and they would say oh but this isn't

## 23405:00 - 23435:00

fair large companies have so much money

## 23435:00 - 23460:00

they have so many resources they don't

## 23460:00 - 23480:00

have to deal with all the things this

## 23480:00 - 23505:00

doesn't apply to me

## 23505:00 - 23560:00

wow so it's like either way

## 23560:00 - 23580:00

and on days when I was feeling real

## 23580:00 - 23625:00

snarky I'd be like pick your excuse

## 23625:00 - 23700:00

you've got your like drop down now when

## 23700:00 - 23750:00

I say retail was a bit of an outlier

## 23750:00 - 23790:00

they had a statistically significant

## 23790:00 - 23810:00

difference

## 23810:00 - 23835:00

their difference was that they were

## 23835:00 - 23890:00

actually better why now I can't tell you

## 23890:00 - 23930:00

why I can in a research paper we'd have

## 23930:00 - 23955:00

a discussion section and this is where

## 23955:00 - 23985:00

you like get to guess

## 23985:00 - 24010:00

right

## 24010:00 - 24065:00

I would surmise and we do this in the

## 24065:00 - 24115:00

report that it's probably because retail

## 24115:00 - 24160:00

went through the retail apocalypse right

## 24160:00 - 24200:00

if you didn't survive like if you

## 24200:00 - 24225:00

weren't just killing it you did not

## 24225:00 - 24245:00

survive

## 24245:00 - 24310:00

so many retail firms just did not make

## 24310:00 - 24340:00

it through you had to be at the top of

## 24340:00 - 24375:00

your game there was no such that my

## 24375:00 - 24415:00

Black Black Friday there's no such thing

## 24415:00 - 24455:00

as not having systems that are

## 24455:00 - 24490:00

performing incredibly well there's no

## 24490:00 - 24510:00

such thing as not being in the cloud

## 24510:00 - 24540:00

because if you cannot make it through

## 24540:00 - 24570:00

you know

## 24570:00 - 24615:00

bursting on demand

## 24615:00 - 24645:00

bursting like magic sometimes I joke

## 24645:00 - 24685:00

right you're not gonna make it

## 24685:00 - 24760:00

and so I suspect if I were to guess

## 24760:00 - 24795:00

if you're not already a high performer

## 24795:00 - 24850:00

in the retail space

## 24850:00 - 24900:00

natural selection got rid of you that is

## 24900:00 - 24915:00

really interesting that makes a lot of

## 24915:00 - 24930:00

sense

## 24930:00 - 24965:00

so I'm looking at these thresholds again

## 24965:00 - 25005:00

and I'm thinking from the perspective of

## 25005:00 - 25030:00

a Founder who's just like I wish my

## 25030:00 - 25060:00

engineering team moved faster

## 25060:00 - 25100:00

essentially you're saying if deploy

## 25100:00 - 25140:00

times if they deploy more than once a

## 25140:00 - 25170:00

day if their deploy frequency is on

## 25170:00 - 25205:00

demand or I think it was hourly was kind

## 25205:00 - 25230:00

of the other bucket it was that part of

## 25230:00 - 25285:00

it yeah and then their meantime their

## 25285:00 - 25310:00

fail rate is like less than 10 percent

## 25310:00 - 25355:00

and their mean time to recovery is less

## 25355:00 - 25385:00

than an hour basically you're doing

## 25385:00 - 25420:00

great that's kind of the message of this

## 25420:00 - 25465:00

framework at least and if you're not

## 25465:00 - 25495:00

doing it through like brute force and

## 25495:00 - 25550:00

killing yourself now can I can I jump in

## 25550:00 - 25585:00

here because then people are like but

## 25585:00 - 25630:00

how do I do this so let's say that like

## 25630:00 - 25660:00

you're not in that category and you're

## 25660:00 - 25675:00

like

## 25675:00 - 25710:00

because this is the next this is the

## 25710:00 - 25735:00

piece of criticism I'll get about Dora

## 25735:00 - 25780:00

right people are like

## 25780:00 - 25830:00

well all you've done is make me feel bad

## 25830:00 - 25885:00

you gave me these metrics you've judged

## 25885:00 - 25950:00

me now I feel bad and then I'm like

## 25950:00 - 25975:00

so there's Dora there I wrote a book

## 25975:00 - 26010:00

called accelerate right which is like

## 26010:00 - 26050:00

the first four years of the research

## 26050:00 - 26090:00

compiled and put together and expanded

## 26090:00 - 26125:00

in a few things and I'll joke there's a

## 26125:00 - 26165:00

whole rest of the book right

## 26165:00 - 26205:00

Dora is best known for the four metrics

## 26205:00 - 26235:00

but there's an entire research program

## 26235:00 - 26290:00

supporting it so it's not just these

## 26290:00 - 26340:00

four metrics what we find is that if you

## 26340:00 - 26375:00

improve a set of capabilities I loved

## 26375:00 - 26400:00

your question around what is devops

## 26400:00 - 26425:00

devops is not a tool chain you buy

## 26425:00 - 26460:00

marketing teams label tool chains devops

## 26460:00 - 26500:00

because they wanted your money devops is

## 26500:00 - 26535:00

a set of capabilities they're technical

## 26535:00 - 26560:00

capabilities their architectural

## 26560:00 - 26590:00

capabilities their cultural capabilities

## 26590:00 - 26645:00

they are lean management practices

## 26645:00 - 26700:00

that predict

## 26700:00 - 26740:00

speed and stability and then speed

## 26740:00 - 26770:00

instability gives you money

## 26770:00 - 26810:00

right because like it's your ability to

## 26810:00 - 26840:00

create these features that give you

## 26840:00 - 26875:00

money so when you work backwards if you

## 26875:00 - 26900:00

want money like you get the features

## 26900:00 - 26935:00

fast if you want the features fast and

## 26935:00 - 26975:00

stable you do the things and the things

## 26975:00 - 27020:00

are technical capabilities like

## 27020:00 - 27045:00

automated testing

## 27045:00 - 27110:00

cicd and cicd is continuous integration

## 27110:00 - 27175:00

continuous deployment is that right yes

## 27175:00 - 27220:00

um trunk-based development

## 27220:00 - 27265:00

using a Version Control System

## 27265:00 - 27285:00

right

## 27285:00 - 27345:00

so do you have good technical practices

## 27345:00 - 27390:00

do you have good architectural practices

## 27390:00 - 27425:00

like do you have a Loosely coupled

## 27425:00 - 27440:00

system

## 27440:00 - 27485:00

are you using the cloud or like if

## 27485:00 - 27500:00

you're not in the cloud for whatever

## 27500:00 - 27565:00

reason are you using the underlying

## 27565:00 - 27615:00

architectural pieces that enable good

## 27615:00 - 27640:00

cloud

## 27640:00 - 27670:00

to do the cloud right or if you're in

## 27670:00 - 27690:00

the cloud and you're not realizing

## 27690:00 - 27705:00

benefits is it because you're doing

## 27705:00 - 27740:00

Cloud wrong right do you have a good

## 27740:00 - 27795:00

culture

## 27795:00 - 27845:00

so you know you don't you don't just

## 27845:00 - 27875:00

like magically go fast and have

## 27875:00 - 27910:00

stability right so working backwards

## 27910:00 - 27945:00

which pieces are you struggling at now

## 27945:00 - 27995:00

uh you kind of noted down the benchmarks

## 27995:00 - 28045:00

if you go to dora.dev the the team at

## 28045:00 - 28095:00

Google was lovely we uh we worked really

## 28095:00 - 28115:00

closely with the team they're keeping

## 28115:00 - 28150:00

this updated you can take a quick check

## 28150:00 - 28170:00

there's a button there that says quick

## 28170:00 - 28200:00

check you can plug in where you kind of

## 28200:00 - 28235:00

think you are like I said you can hunch

## 28235:00 - 28250:00

it

## 28250:00 - 28275:00

and it'll tell you where you are in the

## 28275:00 - 28300:00

benchmarks today

## 28300:00 - 28340:00

and what industry you're in and then the

## 28340:00 - 28380:00

cool part is it'll say now like you'll

## 28380:00 - 28405:00

want to ask yourself

## 28405:00 - 28445:00

like where am I struggling but it'll say

## 28445:00 - 28510:00

for your performance profile and for the

## 28510:00 - 28540:00

industry that you're in statistically

## 28540:00 - 28580:00

over the last several years these are

## 28580:00 - 28615:00

probably your constraints

## 28615:00 - 28655:00

AKA these are probably the things that

## 28655:00 - 28680:00

you're struggling in right now right

## 28680:00 - 28740:00

like for people in finance who are high

## 28740:00 - 28795:00

performers they tend to struggle with

## 28795:00 - 28830:00

these four things right whether it's

## 28830:00 - 28870:00

like culture or continuous integration

## 28870:00 - 28890:00

or

## 28890:00 - 28925:00

whatever I love that you're getting

## 28925:00 - 28950:00

tactical with how to actually improve

## 28950:00 - 28965:00

these already which is the bread and

## 28965:00 - 29010:00

butter of this podcast and so we'll link

## 29010:00 - 29030:00

to this quick check because there's

## 29030:00 - 29070:00

door.dev Quick Check and by the way they

## 29070:00 - 29090:00

do not collect your name they do not

## 29090:00 - 29135:00

collect your info there is no there's no

## 29135:00 - 29185:00

lead any lead gen anything everything's

## 29185:00 - 29200:00

just there

## 29200:00 - 29230:00

and then there's deep dives into every

## 29230:00 - 29255:00

single one of the capabilities

## 29255:00 - 29290:00

amazing and also your book talks about

## 29290:00 - 29310:00

all these things so people should go

## 29310:00 - 29330:00

check out the book obviously it's on

## 29330:00 - 29365:00

Amazon search accelerate is that right

## 29365:00 - 29410:00

yep okay so we were talking about Dora

## 29410:00 - 29435:00

this may be a good time to talk about

## 29435:00 - 29460:00

space which I think is a different

## 29460:00 - 29505:00

framework you recommend what is that all

## 29505:00 - 29580:00

about okay so space is a way to measure

## 29580:00 - 29610:00

we say productivity developer

## 29610:00 - 29645:00

productivity but it's a little bit more

## 29645:00 - 29685:00

than that space is a good way to measure

## 29685:00 - 29740:00

any type of complex creative work now

## 29740:00 - 29780:00

how do they relate

## 29780:00 - 29840:00

let's say you go through the quick check

## 29840:00 - 29870:00

it points out like four things and you

## 29870:00 - 29895:00

decide you want to improve continuous

## 29895:00 - 29945:00

integration and culture right

## 29945:00 - 29985:00

well now you're like cool but how am I

## 29985:00 - 30020:00

going to actually measure them

## 30020:00 - 30060:00

this is where space comes in because

## 30060:00 - 30110:00

space helps you figure out space gives

## 30110:00 - 30155:00

you a framework to pick the right

## 30155:00 - 30200:00

metrics

## 30200:00 - 30235:00

now some people are like well space you

## 30235:00 - 30260:00

didn't give me the exact metrics people

## 30260:00 - 30285:00

love Dora because it's like here's the

## 30285:00 - 30310:00

exact four you need

## 30310:00 - 30355:00

well space is like when you want to

## 30355:00 - 30390:00

measure something that's complex

## 30390:00 - 30425:00

creative work maybe like developer

## 30425:00 - 30460:00

productivity there's also an example at

## 30460:00 - 30510:00

the bottom for Incident Management

## 30510:00 - 30535:00

when you have something you want to

## 30535:00 - 30575:00

measure it says within your context

## 30575:00 - 30620:00

within the metrics you have available to

## 30620:00 - 30675:00

you here's how to pick

## 30675:00 - 30710:00

that's what space is good for now we

## 30710:00 - 30760:00

called it space because it stands for

## 30760:00 - 30790:00

the five Dimensions that you want to

## 30790:00 - 30850:00

measure so s is satisfaction and

## 30850:00 - 30885:00

well-being

## 30885:00 - 30915:00

so satisfaction well-being is kind of

## 30915:00 - 30950:00

self-explanatory now some people might

## 30950:00 - 30975:00

jump in here and say oh well you're just

## 30975:00 - 31010:00

you know touchy feeling this actually

## 31010:00 - 31035:00

matters because we find that

## 31035:00 - 31060:00

satisfaction well-being ends up being

## 31060:00 - 31105:00

incredibly highly correlated with all of

## 31105:00 - 31145:00

the other dimensions of productivity and

## 31145:00 - 31195:00

doing things well and as soon as

## 31195:00 - 31240:00

satisfaction well-being things like uh

## 31240:00 - 31275:00

sustainability if you're satisfied as

## 31275:00 - 31300:00

soon as that starts falling off other

## 31300:00 - 31335:00

things start to break so this can be an

## 31335:00 - 31370:00

incredibly strong and important signal

## 31370:00 - 31410:00

p is performance this is going to be the

## 31410:00 - 31435:00

outcome of a process

## 31435:00 - 31480:00

so reliability

## 31480:00 - 31535:00

within Dora the mttm or change fail rate

## 31535:00 - 31565:00

right those are both performance metrics

## 31565:00 - 31595:00

and so you pick one to kind of measure

## 31595:00 - 31665:00

as performance yep uh a is activity

## 31665:00 - 31705:00

anytime you have a count or a number of

## 31705:00 - 31740:00

something these we see all the time

## 31740:00 - 31765:00

because they're super easy to instrument

## 31765:00 - 31805:00

and automate right number of pull

## 31805:00 - 31855:00

requests number of check-ins number of

## 31855:00 - 31885:00

something that's a

## 31885:00 - 31930:00

C is communication collaboration

## 31930:00 - 31970:00

this can be how people work and talk

## 31970:00 - 32000:00

together it can be meetings it can be

## 32000:00 - 32025:00

collaboration it can also be how our

## 32025:00 - 32065:00

systems communicate together it can be

## 32065:00 - 32105:00

the search ability of a code base

## 32105:00 - 32150:00

and then e is efficiency and flow so

## 32150:00 - 32185:00

this is going to be the flow through the

## 32185:00 - 32215:00

system it can be the time through the

## 32215:00 - 32260:00

system if we think about SRE or Incident

## 32260:00 - 32300:00

Management can be the number of hops a

## 32300:00 - 32325:00

ticket takes until it reaches the right

## 32325:00 - 32355:00

person

## 32355:00 - 32410:00

now to use space correctly we want to

## 32410:00 - 32450:00

use at least three dimensions at a time

## 32450:00 - 32485:00

because that helps us balance

## 32485:00 - 32515:00

turns out Dora is actually an

## 32515:00 - 32555:00

implementation of space so Dora would be

## 32555:00 - 32585:00

space four

## 32585:00 - 32640:00

mostly that outer loop hmm

## 32640:00 - 32675:00

so again once you've found something

## 32675:00 - 32710:00

that you want to improve

## 32710:00 - 32760:00

find the metrics that make sense to you

## 32760:00 - 32795:00

try to have them be in balance or

## 32795:00 - 32810:00

intention so you don't like throw

## 32810:00 - 32860:00

something out of whack but pick three

## 32860:00 - 32880:00

So when you say door is an

## 32880:00 - 32920:00

implementation of space one has five

## 32920:00 - 32970:00

buckets one has four how does how do you

## 32970:00 - 33010:00

actually think about that so space is

## 33010:00 - 33040:00

there to help you think about how you

## 33040:00 - 33065:00

want to pick metrics right so a lot of

## 33065:00 - 33110:00

time I see people so let me half step

## 33110:00 - 33155:00

back I used to advise people on how to

## 33155:00 - 33185:00

pick metrics right for years people

## 33185:00 - 33230:00

would would pull me in to advise on Dora

## 33230:00 - 33265:00

or accelerate right they would ask me

## 33265:00 - 33310:00

questions but it ended up being metrics

## 33310:00 - 33335:00

questions a lot

## 33335:00 - 33375:00

how do I pick the right metrics

## 33375:00 - 33410:00

to improve what I'm doing right like I

## 33410:00 - 33450:00

said they had the Dory numbers

## 33450:00 - 33475:00

they would pick their constraints and

## 33475:00 - 33505:00

they wanted to improve but how do I

## 33505:00 - 33545:00

improve how do I measure this

## 33545:00 - 33575:00

how do I show Improvement

## 33575:00 - 33610:00

and so we would start thinking really

## 33610:00 - 33645:00

critically about which metrics were the

## 33645:00 - 33670:00

right metrics to pick

## 33670:00 - 33700:00

and I would always say make sure you

## 33700:00 - 33740:00

pick balanced metrics make sure you

## 33740:00 - 33800:00

picked pick metrics that are intention

## 33800:00 - 33850:00

and I could say it but people have a

## 33850:00 - 33870:00

hard time wrapping that around their

## 33870:00 - 33900:00

heads because they kept picking things

## 33900:00 - 33935:00

like number of lines of code never

## 33935:00 - 33960:00

picked number of lines of code oh wow

## 33960:00 - 33990:00

number of still every month I didn't

## 33990:00 - 34020:00

even know about this number of pull

## 34020:00 - 34065:00

requests number of commits

## 34065:00 - 34095:00

and I was like these are all activity

## 34095:00 - 34135:00

metrics and so finally I pulled a few of

## 34135:00 - 34160:00

my friends together and I was like

## 34160:00 - 34195:00

let's come up with a framework to help

## 34195:00 - 34230:00

people think about it and so there are

## 34230:00 - 34275:00

five broad categories

## 34275:00 - 34330:00

pick three because that will help Force

## 34330:00 - 34380:00

you through the mental exercise of what

## 34380:00 - 34415:00

could I possibly pick

## 34415:00 - 34455:00

you don't need all five right this isn't

## 34455:00 - 34480:00

we're not playing bingo we're not

## 34480:00 - 34500:00

playing blackout Bingo you don't need

## 34500:00 - 34515:00

all of them

## 34515:00 - 34565:00

but try to have at least three

## 34565:00 - 34595:00

cross different dimensions now one

## 34595:00 - 34625:00

example here I was working with a group

## 34625:00 - 34645:00

that wanted to improve their pull

## 34645:00 - 34690:00

requests very generally they just said

## 34690:00 - 34710:00

improved pull requests so they were

## 34710:00 - 34765:00

thinking about pinging someone every 15

## 34765:00 - 34790:00

minutes and I was like oh this is going

## 34790:00 - 34810:00

to be bad

## 34810:00 - 34850:00

because we know from other literature

## 34850:00 - 34880:00

and research like nursing you'll get

## 34880:00 - 34915:00

alert fatigue where people will just

## 34915:00 - 34950:00

start tuning out alerts

## 34950:00 - 34975:00

either they'll turn them off or they

## 34975:00 - 35015:00

will just stop hearing them so like

## 35015:00 - 35055:00

number of alerts right they're like

## 35055:00 - 35085:00

let's just think about number of alerts

## 35085:00 - 35115:00

and I said well but if we think about

## 35115:00 - 35150:00

efficiency and flow

## 35150:00 - 35220:00

how much time do you have to work

## 35220:00 - 35245:00

on your coding

## 35245:00 - 35315:00

so those two are balanced

## 35315:00 - 35360:00

so we need to protect time to work

## 35360:00 - 35405:00

as well as

## 35405:00 - 35475:00

code review time right pull request time

## 35475:00 - 35510:00

and so sometimes we can think about

## 35510:00 - 35535:00

those and then and then we I think we

## 35535:00 - 35565:00

added a satisfaction metric are you

## 35565:00 - 35605:00

satisfied with the pull request

## 35605:00 - 35635:00

process and the selection of the

## 35635:00 - 35655:00

reviewer

## 35655:00 - 35685:00

how do you go about actually capturing

## 35685:00 - 35730:00

and measuring this say satisfaction so

## 35730:00 - 35765:00

for satisfaction I would I would

## 35765:00 - 35805:00

generally ask right go ahead and ask now

## 35805:00 - 35840:00

the ones that you instrument you can

## 35840:00 - 35865:00

instrument and pull out of systems all

## 35865:00 - 35890:00

the time right go ahead and grab that

## 35890:00 - 35935:00

string for a satisfaction metric I would

## 35935:00 - 35955:00

only pull that

## 35955:00 - 36000:00

like periodically right once every few

## 36000:00 - 36030:00

months like a survey to your engineering

## 36030:00 - 36070:00

like a survey yep absolutely

## 36070:00 - 36120:00

awesome and don't don't discount what

## 36120:00 - 36150:00

people say right sometimes I hear

## 36150:00 - 36175:00

actually not sometimes a lot of times I

## 36175:00 - 36215:00

hear people say oh but people lie

## 36215:00 - 36240:00

first of all what is their incentive to

## 36240:00 - 36280:00

lie why would they lie about having a

## 36280:00 - 36310:00

bad system

## 36310:00 - 36345:00

uh because it's bad and they want it

## 36345:00 - 36375:00

fixed right

## 36375:00 - 36410:00

if it's absolutely a hostile work

## 36410:00 - 36445:00

environment they might lie and then tell

## 36445:00 - 36475:00

you what's good then you have bigger

## 36475:00 - 36505:00

problems right

## 36505:00 - 36540:00

also

## 36540:00 - 36590:00

do we ever see bad data from our systems

## 36590:00 - 36630:00

or incomplete data for my systems

## 36630:00 - 36660:00

that's a lie

## 36660:00 - 36705:00

but we find ways to deal with it we see

## 36705:00 - 36750:00

it we acknowledge it we look for holes

## 36750:00 - 36775:00

in our system data

## 36775:00 - 36825:00

we try to deal with it right

## 36825:00 - 36870:00

that's also a lie so I think there are

## 36870:00 - 36925:00

better ways to think about and deal with

## 36925:00 - 36940:00

that

## 36940:00 - 36970:00

and then try to work with it right

## 36970:00 - 37020:00

because then I I wrote a paper with Mick

## 37020:00 - 37100:00

Kirsten on this several years ago on how

## 37100:00 - 37140:00

data from people and data from systems

## 37140:00 - 37170:00

are really important complements because

## 37170:00 - 37205:00

we can get certain insights from people

## 37205:00 - 37240:00

that we'll never get from systems right

## 37240:00 - 37270:00

like let's look at lead time from

## 37270:00 - 37295:00

changes for example right from commit to

## 37295:00 - 37315:00

deploy

## 37315:00 - 37365:00

the speed might be fine but people might

## 37365:00 - 37400:00

tell you it's taking absolute heroics

## 37400:00 - 37445:00

right it's some ridiculous Rube Goldberg

## 37445:00 - 37485:00

machine the system will never tell you

## 37485:00 - 37515:00

that

## 37515:00 - 37570:00

or you could get data on

## 37570:00 - 37605:00

your version control system

## 37605:00 - 37635:00

I worked with a company several years

## 37635:00 - 37675:00

ago and we found out that there was a

## 37675:00 - 37705:00

significant portion code that was just

## 37705:00 - 37735:00

not going into any Version Control

## 37735:00 - 37770:00

System you're never going to find that

## 37770:00 - 37810:00

out from your systems because it's not

## 37810:00 - 37840:00

in the systems

## 37840:00 - 37880:00

and it was mission critical I can see

## 37880:00 - 37915:00

why people come to you asking for advice

## 37915:00 - 37930:00

on metrics because you have this

## 37930:00 - 37965:00

framework of here's the type of metrics

## 37965:00 - 38005:00

you want and then I think and especially

## 38005:00 - 38035:00

from engineering team there's going to

## 38035:00 - 38065:00

be this like how do I optimize and make

## 38065:00 - 38080:00

sure I'm doing the right thing and

## 38080:00 - 38115:00

measuring the right things for someone

## 38115:00 - 38165:00

that wants to do this and you know an

## 38165:00 - 38185:00

hour-long podcast isn't going to give

## 38185:00 - 38210:00

them all the answers what do you

## 38210:00 - 38260:00

recommend they go read or go do or look

## 38260:00 - 38310:00

at to help them figure that out one I I

## 38310:00 - 38350:00

hate to be this person uh but I'll point

## 38350:00 - 38380:00

to a few of my papers because I will say

## 38380:00 - 38430:00

I write things down because I get asked

## 38430:00 - 38475:00

them so often and I want to make sure it

## 38475:00 - 38505:00

is broadly applicable or like broadly

## 38505:00 - 38545:00

available I guess this space paper for

## 38545:00 - 38600:00

sure it's at ACM and I think the year we

## 38600:00 - 38620:00

published it it was like the most read

## 38620:00 - 38640:00

paper

## 38640:00 - 38690:00

um at acmq yeah so we tried to make it

## 38690:00 - 38715:00

as

## 38715:00 - 38755:00

readable as possible so the space paper

## 38755:00 - 38780:00

is nice because it outlines this

## 38780:00 - 38820:00

framework and it gives examples of

## 38820:00 - 38860:00

metrics in every single category and so

## 38860:00 - 38885:00

hopefully people can look at this and

## 38885:00 - 38935:00

they can say okay here's an example to

## 38935:00 - 38965:00

use here right here are some of the

## 38965:00 - 39000:00

things that I could possibly use and

## 39000:00 - 39030:00

we're seeing that space is being used

## 39030:00 - 39075:00

lots and lots of different places

## 39075:00 - 39125:00

another good one could be the paper that

## 39125:00 - 39165:00

I mentioned with Mick Kirsten and it was

## 39165:00 - 39200:00

about we talked about using

## 39200:00 - 39235:00

data from people and data from systems

## 39235:00 - 39270:00

we used we wrote it up in the devops

## 39270:00 - 39295:00

context because I want to say this was

## 39295:00 - 39340:00

written in like 2016 or 2017 or

## 39340:00 - 39390:00

something but it helps you think through

## 39390:00 - 39425:00

what types of data are good in which

## 39425:00 - 39485:00

situations right because you will never

## 39485:00 - 39525:00

find yourself in a situation when you

## 39525:00 - 39565:00

don't want both types of data

## 39565:00 - 39600:00

even teams that I've worked with that

## 39600:00 - 39615:00

are

## 39615:00 - 39690:00

the most advanced they have absolute

## 39690:00 - 39725:00

instrumentation in every possible

## 39725:00 - 39770:00

scenario

## 39770:00 - 39815:00

in the most detailed way

## 39815:00 - 39855:00

they will still survey

## 39855:00 - 39890:00

their developers at least once a year

## 39890:00 - 39965:00

because you can get new insights right

## 39965:00 - 40020:00

one book that I love it's

## 40020:00 - 40050:00

it's a little dense but it's really

## 40050:00 - 40080:00

interesting that I love is how to

## 40080:00 - 40105:00

measure anything

## 40105:00 - 40170:00

and it's by Hubbard

## 40170:00 - 40195:00

and there are parts of it they're like

## 40195:00 - 40230:00

real stats heavy but he has this portion

## 40230:00 - 40280:00

in the front that's like

## 40280:00 - 40320:00

in covering intangibles and it's so it's

## 40320:00 - 40355:00

like what what happens when you don't

## 40355:00 - 40405:00

have data you have no data you're

## 40405:00 - 40440:00

starting from nothing what are good ways

## 40440:00 - 40455:00

to hunch

## 40455:00 - 40485:00

data

## 40485:00 - 40520:00

and I really love that because he he

## 40520:00 - 40570:00

covers some really good ground there

## 40570:00 - 40605:00

today's entire episode is brought to you

## 40605:00 - 40650:00

by DX a platform for measuring and

## 40650:00 - 40690:00

improving developer productivity DX is

## 40690:00 - 40720:00

designed by the researchers behind

## 40720:00 - 40765:00

Frameworks such as Dora space and devex

## 40765:00 - 40805:00

including Nicole forsgren who is my

## 40805:00 - 40840:00

guest for this very episode if you've

## 40840:00 - 40865:00

tried measuring developer productivity

## 40865:00 - 40890:00

you know that there are a lot of basic

## 40890:00 - 40920:00

metrics out there and a lot of ways to

## 40920:00 - 40955:00

do this wrong and getting that full view

## 40955:00 - 41000:00

of productivity is still really hard DX

## 41000:00 - 41025:00

tackles this problem by combining

## 41025:00 - 41060:00

qualitative and quantitative insights

## 41060:00 - 41090:00

based on the very research Nicole and

## 41090:00 - 41115:00

her team have done giving you full

## 41115:00 - 41140:00

clarity into how your developers are

## 41140:00 - 41185:00

doing the x is used by both startups and

## 41185:00 - 41220:00

Fortune 500 companies including

## 41220:00 - 41270:00

companies like twilio amplitude eBay Rex

## 41270:00 - 41325:00

toast Pfizer and Procter Gamble to learn

## 41325:00 - 41355:00

more about DX and get a demo of their

## 41355:00 - 41415:00

product visit their website at getdx.com

## 41415:00 - 41495:00

that's getdx.com Lenny

## 41495:00 - 41530:00

you also mention Offline that you might

## 41530:00 - 41565:00

be working on a book that will answer a

## 41565:00 - 41590:00

lot of these questions is that something

## 41590:00 - 41620:00

you're up for chatting about yeah

## 41620:00 - 41655:00

absolutely so as I mentioned I tend to

## 41655:00 - 41710:00

write write things down when I get asked

## 41710:00 - 41745:00

questions on it a lot and so this is one

## 41745:00 - 41780:00

in particular so we'll be covering you

## 41780:00 - 41805:00

know I'm I'm starting to go through and

## 41805:00 - 41830:00

I'm covering some of these and I think

## 41830:00 - 41860:00

some of the important topics in

## 41860:00 - 41880:00

particular are

## 41880:00 - 41925:00

you know starting with what is your

## 41925:00 - 41965:00

problem or what is your goal and being

## 41965:00 - 42015:00

super super crisp on it right like what

## 42015:00 - 42035:00

is it that we're

## 42035:00 - 42065:00

trying to answer

## 42065:00 - 42090:00

and

## 42090:00 - 42135:00

I would say this is a bigger challenge

## 42135:00 - 42180:00

than most people recognize or realize

## 42180:00 - 42205:00

like

## 42205:00 - 42250:00

I'm making the setup right like 80 of

## 42250:00 - 42290:00

the folks that I work with this this is

## 42290:00 - 42315:00

their biggest problem

## 42315:00 - 42355:00

even at like executive levels they'll

## 42355:00 - 42385:00

they'll ask their team or teams will

## 42385:00 - 42405:00

come back with uncertainty and they'll

## 42405:00 - 42440:00

say like well you told me to improve

## 42440:00 - 42475:00

developer experience

## 42475:00 - 42515:00

and like okay great what do you mean by

## 42515:00 - 42525:00

that

## 42525:00 - 42555:00

and then teams will have gone off for

## 42555:00 - 42595:00

several months and they're tackling

## 42595:00 - 42610:00

something and they'll come back and

## 42610:00 - 42640:00

they'll be like oh well that wasn't what

## 42640:00 - 42665:00

I meant I'm like okay what do you mean

## 42665:00 - 42715:00

by this are you talking about

## 42715:00 - 42745:00

inner and outer loop are you talking

## 42745:00 - 42770:00

about friction are you talking about

## 42770:00 - 42805:00

culture because sometimes they're

## 42805:00 - 42825:00

talking about culture and if you're

## 42825:00 - 42855:00

talking about culture this is an

## 42855:00 - 42890:00

incredibly valid answer but if you're

## 42890:00 - 42920:00

talking about culture this is totally

## 42920:00 - 42940:00

different than if you're talking about

## 42940:00 - 42975:00

friction in tool chains

## 42975:00 - 43005:00

right

## 43005:00 - 43050:00

and if you're on different pages you're

## 43050:00 - 43070:00

heading in completely different

## 43070:00 - 43125:00

directions so like that that's one thing

## 43125:00 - 43175:00

we cover which seems obvious but trust

## 43175:00 - 43225:00

me it is not and then even like how do

## 43225:00 - 43250:00

you we're going to do kind of a rough

## 43250:00 - 43270:00

version of like how do you start

## 43270:00 - 43325:00

measuring from nothing and also the

## 43325:00 - 43350:00

measurement Journey

## 43350:00 - 43395:00

right like how do you think about

## 43395:00 - 43435:00

the trade-offs between and the

## 43435:00 - 43470:00

proportion of measurement between

## 43470:00 - 43525:00

subjective data right data from people

## 43525:00 - 43555:00

so you have Azure interviews and you

## 43555:00 - 43600:00

have surveys and objective data stuff

## 43600:00 - 43630:00

you get from systems because when you

## 43630:00 - 43665:00

first start off you'll be relying much

## 43665:00 - 43700:00

more on data from people because you can

## 43700:00 - 43730:00

get it relatively quickly

## 43730:00 - 43775:00

but as you kind of transition through

## 43775:00 - 43805:00

this measurement Journey

## 43805:00 - 43840:00

you'll get more and more data from your

## 43840:00 - 43880:00

systems because it's scalable it can be

## 43880:00 - 43905:00

engineered you can be doing you know

## 43905:00 - 43945:00

much more with it and also you should be

## 43945:00 - 43970:00

thinking about you know don't let the

## 43970:00 - 44000:00

perfect be the enemy of the good right

## 44000:00 - 44030:00

so like how do we think about this very

## 44030:00 - 44065:00

very strategically how do we transition

## 44065:00 - 44115:00

through this how do we think about what

## 44115:00 - 44170:00

each piece of data is for and also like

## 44170:00 - 44200:00

lots and lots of examples right so I

## 44200:00 - 44230:00

have included like example interview

## 44230:00 - 44265:00

scripts how do you select people how do

## 44265:00 - 44300:00

you screen people examples survey

## 44300:00 - 44330:00

scripts what are some of the analyzes we

## 44330:00 - 44365:00

should do and trying to make this

## 44365:00 - 44395:00

incredibly accessible so like basically

## 44395:00 - 44435:00

anyone can do this so you do not need to

## 44435:00 - 44460:00

be a data scientist but if you have one

## 44460:00 - 44495:00

on staff like you can hand them some of

## 44495:00 - 44530:00

this and just like let them run

## 44530:00 - 44555:00

I think this book is going to do

## 44555:00 - 44585:00

extremely well uh definitely come back

## 44585:00 - 44620:00

on when it is out I think you said maybe

## 44620:00 - 44650:00

year-ish kind of time frame yeah

## 44650:00 - 44675:00

probably about a year by the time we get

## 44675:00 - 44705:00

all the way through if people want to be

## 44705:00 - 44730:00

notified when it's out can they sign up

## 44730:00 - 44755:00

on your site for a newsletter or

## 44755:00 - 44775:00

anything like that is there any way to

## 44775:00 - 44810:00

kind of be uh on in the loop as it

## 44810:00 - 44845:00

approaches oh yeah absolutely yeah I'll

## 44845:00 - 44885:00

add I'll add a link for that also if

## 44885:00 - 44945:00

anyone is doing some of this work now if

## 44945:00 - 44995:00

they have you know major questions that

## 44995:00 - 45025:00

they would love to me to answer if they

## 45025:00 - 45065:00

have success stories if they have case

## 45065:00 - 45095:00

studies if they have anything that they

## 45095:00 - 45130:00

you know would love to be included you

## 45130:00 - 45155:00

know I I remember when I wrote

## 45155:00 - 45175:00

accelerate before there were a couple

## 45175:00 - 45195:00

folks that reached out after and they

## 45195:00 - 45220:00

were like oh I wanted to have something

## 45220:00 - 45255:00

included now I've looked today I've

## 45255:00 - 45285:00

learned right if if there's anything

## 45285:00 - 45335:00

that folks would love to you know be you

## 45335:00 - 45370:00

know in discussion with me about I I'm

## 45370:00 - 45410:00

always eager to chat and nerd out about

## 45410:00 - 45440:00

you know devex and especially

## 45440:00 - 45475:00

measurement measurement Journeys so

## 45475:00 - 45510:00

awesome I usually ask that this this at

## 45510:00 - 45530:00

the end and I have more questions but

## 45530:00 - 45560:00

while we're here how would people reach

## 45560:00 - 45575:00

out to you what's the best way to

## 45575:00 - 45625:00

contact you on my website I've got

## 45625:00 - 45680:00

info.nicolfe at gmail okay yeah awesome

## 45680:00 - 45710:00

okay a few more questions awesome thanks

## 45710:00 - 45765:00

what are the most common pitfalls that

## 45765:00 - 45785:00

companies run into when they're trying

## 45785:00 - 45815:00

to roll out any sort of developer

## 45815:00 - 45855:00

experience developer productivity system

## 45855:00 - 45890:00

measurements improvements

## 45890:00 - 45920:00

I think one I just mentioned right like

## 45920:00 - 45950:00

not being

## 45950:00 - 45990:00

clear or not understanding what it is

## 45990:00 - 46025:00

that they're looking for

## 46025:00 - 46055:00

because then you can have you know a

## 46055:00 - 46080:00

thousand flowers bloom and everyone's

## 46080:00 - 46110:00

kind of running in a different direction

## 46110:00 - 46180:00

I think another one is not

## 46180:00 - 46225:00

not pursuing this in both a top-down and

## 46225:00 - 46270:00

a bottom-up structure right and I think

## 46270:00 - 46285:00

that

## 46285:00 - 46340:00

can really help Drive success

## 46340:00 - 46370:00

and and having

## 46370:00 - 46405:00

you know good communication throughout

## 46405:00 - 46465:00

is super super important right so

## 46465:00 - 46490:00

getting

## 46490:00 - 46545:00

your ICS bought in and helping them

## 46545:00 - 46570:00

understand that

## 46570:00 - 46600:00

this is for them we want to understand

## 46600:00 - 46630:00

what they're doing knowing what

## 46630:00 - 46655:00

vocabulary they use you know what

## 46655:00 - 46685:00

terminology they use is super important

## 46685:00 - 46715:00

and then

## 46715:00 - 46765:00

chatting with leaders right and

## 46765:00 - 46795:00

understanding like what their

## 46795:00 - 46825:00

motivations are or helping them

## 46825:00 - 46855:00

understand what the motivations could be

## 46855:00 - 46890:00

you know this kind of Harkens back to

## 46890:00 - 46925:00

one of our earliest Chats on why I even

## 46925:00 - 46960:00

got into this and how I see two

## 46960:00 - 46985:00

different sides to the conversation on

## 46985:00 - 47005:00

like why is devops even a thing why

## 47005:00 - 47055:00

should we even ship faster like

## 47055:00 - 47090:00

there are so many people that I talk to

## 47090:00 - 47125:00

that are super passionate about devex

## 47125:00 - 47155:00

right now and they're like how can I

## 47155:00 - 47185:00

convince my executive team this is

## 47185:00 - 47235:00

important because their developers are

## 47235:00 - 47275:00

just completely burning out or they use

## 47275:00 - 47305:00

computers and anger every day and so

## 47305:00 - 47365:00

it's like how can we have the right

## 47365:00 - 47400:00

tools to socialize this to our leaders

## 47400:00 - 47465:00

as well right because this should be a

## 47465:00 - 47500:00

priority this needs to be a strategic

## 47500:00 - 47545:00

piece and how can we help pull together

## 47545:00 - 47585:00

the right value points

## 47585:00 - 47630:00

to communicate this and to understand

## 47630:00 - 47670:00

what their priorities are so that we can

## 47670:00 - 47720:00

see how this fits in right you've been

## 47720:00 - 47750:00

working in this space for a long time

## 47750:00 - 47790:00

probably longer than anyone that has

## 47790:00 - 47825:00

ever worked on this area of developer

## 47825:00 - 47855:00

experience productivity what have you

## 47855:00 - 47890:00

seen change most from the time you

## 47890:00 - 47930:00

started working in the space too today

## 47930:00 - 47970:00

what kind of progress has been made

## 47970:00 - 48015:00

we have these increasingly large complex

## 48015:00 - 48050:00

systems right so like 10 or 15 years ago

## 48050:00 - 48075:00

like the internet was around but like

## 48075:00 - 48105:00

things were really different now almost

## 48105:00 - 48155:00

every company has a really large complex

## 48155:00 - 48195:00

system right

## 48195:00 - 48235:00

we also have a shortage of developers or

## 48235:00 - 48265:00

at least a reported perceived shortage

## 48265:00 - 48290:00

of Developers

## 48290:00 - 48355:00

more companies are technology driven or

## 48355:00 - 48375:00

at least they understand they're

## 48375:00 - 48405:00

technology driven it's like I understand

## 48405:00 - 48435:00

a handful I remember a handful of years

## 48435:00 - 48460:00

ago when I met with

## 48460:00 - 48500:00

a financial institution whose CTO

## 48500:00 - 48535:00

insisted to me that he was not a tech

## 48535:00 - 48575:00

company like that that's not real

## 48575:00 - 48600:00

anymore that doesn't happen anymore at

## 48600:00 - 48650:00

least like very very rarely

## 48650:00 - 48695:00

so all of these things come together

## 48695:00 - 48730:00

and suddenly many more companies are

## 48730:00 - 48750:00

like

## 48750:00 - 48810:00

we have to be better at this and that

## 48810:00 - 48850:00

was not always the case like five to ten

## 48850:00 - 48875:00

years ago I used to have to really

## 48875:00 - 48930:00

explain why this was a pressing concern

## 48930:00 - 48950:00

and why it would continue to be a

## 48950:00 - 49005:00

present concern and now in the last six

## 49005:00 - 49050:00

to nine to 12 months we have

## 49050:00 - 49090:00

this AI moment happening

## 49090:00 - 49125:00

and it just poured gas on top of

## 49125:00 - 49170:00

everything because

## 49170:00 - 49215:00

now what's important like we've always

## 49215:00 - 49240:00

said that like ideas aren't important

## 49240:00 - 49280:00

execution is important but now this is

## 49280:00 - 49330:00

absolutely true because

## 49330:00 - 49360:00

it's not just about

## 49360:00 - 49415:00

what it is that you build it's about

## 49415:00 - 49495:00

creating absolutely novel incredibly new

## 49495:00 - 49545:00

experiences and doing them at a speed

## 49545:00 - 49590:00

that no one has seen before

## 49590:00 - 49640:00

and the only way to do this

## 49640:00 - 49690:00

have this software pipeline

## 49690:00 - 49760:00

that is fast and is safe and is stable

## 49760:00 - 49800:00

and is reliable

## 49800:00 - 49850:00

and that's where we're seeing this

## 49850:00 - 49890:00

really interesting

## 49890:00 - 49945:00

convergence and

## 49945:00 - 49970:00

pressure isn't quite the right word but

## 49970:00 - 50025:00

it's really forcing the discussion

## 50025:00 - 50055:00

and

## 50055:00 - 50115:00

strategy and prioritization right

## 50115:00 - 50145:00

I'm glad you touched on AI that was

## 50145:00 - 50165:00

actually exactly where I was going to go

## 50165:00 - 50185:00

next

## 50185:00 - 50245:00

yeah obviously productivity AI

## 50245:00 - 50270:00

engineering something that's top of mind

## 50270:00 - 50295:00

for a lot of people there's a lot of

## 50295:00 - 50320:00

layoffs that have been happening there's

## 50320:00 - 50340:00

a lot of talk we don't need as many

## 50340:00 - 50365:00

engineers

## 50365:00 - 50405:00

actually we had dinner not too long ago

## 50405:00 - 50470:00

with few I'd say 10x engineers and those

## 50470:00 - 50500:00

are folks that people sometimes say like

## 50500:00 - 50525:00

they don't need co-pilot they're not

## 50525:00 - 50545:00

going to use any of these tools they're

## 50545:00 - 50570:00

already amazing and they were the

## 50570:00 - 50595:00

opposite they're like this is making me

## 50595:00 - 50640:00

100 more effective and efficient and I

## 50640:00 - 50680:00

love it so clearly good things are

## 50680:00 - 50695:00

happening there

## 50695:00 - 50720:00

I don't know the question is

## 50720:00 - 50745:00

specifically but I guess have you seen

## 50745:00 - 50790:00

the impact of AI on engineering

## 50790:00 - 50825:00

productivity and has that shifted how

## 50825:00 - 50855:00

you think about developer experience and

## 50855:00 - 50890:00

productivity beyond what you already

## 50890:00 - 50905:00

just shared

## 50905:00 - 50980:00

absolutely so yes and right I think this

## 50980:00 - 51030:00

is a super interesting open question so

## 51030:00 - 51050:00

can I answer it just with a whole bunch

## 51050:00 - 51090:00

of questions absolutely we're absolutely

## 51090:00 - 51110:00

seeing

## 51110:00 - 51165:00

an impact and we continue to explore

## 51165:00 - 51185:00

this

## 51185:00 - 51235:00

so like I have an interesting question

## 51235:00 - 51265:00

to see like how it'll change the space

## 51265:00 - 51305:00

framework what's open here I think a few

## 51305:00 - 51335:00

things will remain right satisfaction is

## 51335:00 - 51355:00

still going to be there performance is

## 51355:00 - 51380:00

still going to be their activity still

## 51380:00 - 51400:00

going to be there

## 51400:00 - 51425:00

how you communicate with people and with

## 51425:00 - 51455:00

the tool efficiency and flow is still

## 51455:00 - 51490:00

going to be there I believe it will

## 51490:00 - 51545:00

change and add a dimension like trust or

## 51545:00 - 51580:00

reliability right how do I Rely can I

## 51580:00 - 51615:00

rely on it well I have an over Reliance

## 51615:00 - 51655:00

on it and what we're seeing is that

## 51655:00 - 51705:00

probably unsurprisingly

## 51705:00 - 51745:00

people really fundamentally shift the

## 51745:00 - 51795:00

way they

## 51795:00 - 51845:00

work when they work with an AI enabled

## 51845:00 - 51885:00

tool like GitHub copilot or like you

## 51885:00 - 51920:00

know tab 9 or others because now instead

## 51920:00 - 51945:00

of just writing code or like having a

## 51945:00 - 51980:00

short like autocomplete you spend more

## 51980:00 - 52010:00

time reviewing code than writing code

## 52010:00 - 52045:00

right there's this wonderful paper out

## 52045:00 - 52090:00

that uses the cups model uh I'll I'll

## 52090:00 - 52140:00

share it with you a team at MSR did it

## 52140:00 - 52175:00

the fines that you know

## 52175:00 - 52210:00

about 50 of your time now is spent

## 52210:00 - 52255:00

reviewing versus writing

## 52255:00 - 52300:00

but it'll be interesting to see how that

## 52300:00 - 52330:00

changes things longitudinally right

## 52330:00 - 52355:00

because because other you know some of

## 52355:00 - 52380:00

my colleagues also did a paper that

## 52380:00 - 52420:00

showed that you know you can do certain

## 52420:00 - 52455:00

tasks like build an HTTP server or you

## 52455:00 - 52490:00

know 50 faster

## 52490:00 - 52520:00

but I don't think that's what

## 52520:00 - 52550:00

productivity is about when you're using

## 52550:00 - 52585:00

an AI tool frankly right anyone who's

## 52585:00 - 52635:00

looking at that and like dear CEOs or

## 52635:00 - 52655:00

whoever who are like now I can lay off

## 52655:00 - 52690:00

half my Workforce that's not what this

## 52690:00 - 52725:00

is about right it's not about taking a

## 52725:00 - 52755:00

task and cutting your time in half

## 52755:00 - 52840:00

because now what we've enabled is your

## 52840:00 - 52885:00

ability to do certain things faster and

## 52885:00 - 52910:00

then free up some of your cognitive

## 52910:00 - 52955:00

space so that you can do harder things

## 52955:00 - 53005:00

with this new

## 53005:00 - 53055:00

co-pilot sidecar or something right

## 53055:00 - 53100:00

but also because now you're accepting

## 53100:00 - 53155:00

text and then reviewing it we've changed

## 53155:00 - 53195:00

what your mental model is so we've

## 53195:00 - 53230:00

changed the friction model that you

## 53230:00 - 53260:00

expect we've changed the cognitive load

## 53260:00 - 53295:00

of what you expect we're changing

## 53295:00 - 53340:00

Reliance on code so what does this mean

## 53340:00 - 53375:00

for Reliance or over Reliance what does

## 53375:00 - 53405:00

this mean for learning

## 53405:00 - 53435:00

what does this mean for novices versus

## 53435:00 - 53460:00

experts

## 53460:00 - 53495:00

how do we measure productivity right

## 53495:00 - 53515:00

there are a handful of us that are

## 53515:00 - 53550:00

having these discussions on what does

## 53550:00 - 53580:00

this mean and how do we communicate it

## 53580:00 - 53615:00

thoughtfully again we really need to

## 53615:00 - 53645:00

have these kind of holistic balanced

## 53645:00 - 53665:00

metrics

## 53665:00 - 53695:00

because if we

## 53695:00 - 53730:00

if it's an oversimplification we really

## 53730:00 - 53765:00

risk losing the force for the trees

## 53765:00 - 53790:00

right but it's also like super

## 53790:00 - 53820:00

interesting and super compelling I think

## 53820:00 - 53860:00

how can we think about you know learning

## 53860:00 - 53900:00

or like onboarding to new code bases or

## 53900:00 - 53935:00

new languages for folks who already know

## 53935:00 - 53970:00

computational learning I I think it's

## 53970:00 - 53995:00

also very different for folks who are

## 53995:00 - 54025:00

just learning programming languages and

## 54025:00 - 54045:00

don't already know things like

## 54045:00 - 54080:00

computational thinking

## 54080:00 - 54130:00

if someone was excited to kind of go

## 54130:00 - 54165:00

down this road of we're going to focus

## 54165:00 - 54185:00

on developer experience we're going to

## 54185:00 - 54215:00

focus on helping our Engineers be more

## 54215:00 - 54260:00

productive what are the next step or two

## 54260:00 - 54290:00

that they should take in your opinion

## 54290:00 - 54315:00

just broadly knowing that you don't know

## 54315:00 - 54350:00

any specifics about the say the company

## 54350:00 - 54380:00

that's thinking about this right now I

## 54380:00 - 54435:00

think if you're like walking away from

## 54435:00 - 54465:00

this podcast and you're like you know

## 54465:00 - 54495:00

I'm already working on this or I think

## 54495:00 - 54525:00

this is a thing that's that's happening

## 54525:00 - 54560:00

right I would say just like go check

## 54560:00 - 54610:00

your work basically right like has this

## 54610:00 - 54635:00

been

## 54635:00 - 54700:00

written down is there a clearly defined

## 54700:00 - 54755:00

challenge problem something start there

## 54755:00 - 54795:00

absolutely right because that is going

## 54795:00 - 54845:00

to be the thing that reduces confusion

## 54845:00 - 54895:00

the best right absolutely and then see

## 54895:00 - 54940:00

if there's any data and data can be very

## 54940:00 - 54975:00

Loosely defined right is there any

## 54975:00 - 55030:00

signal that is related to

## 55030:00 - 55060:00

the problem

## 55060:00 - 55090:00

like I'd start there

## 55090:00 - 55120:00

and you can do that you can do that in a

## 55120:00 - 55150:00

week you can hunt something down sounds

## 55150:00 - 55170:00

like something you could do in a day

## 55170:00 - 55225:00

yeah well depending depending on

## 55225:00 - 55265:00

how scattered Things Are

## 55265:00 - 55300:00

are there any companies that you look at

## 55300:00 - 55330:00

as good models of they do this really

## 55330:00 - 55370:00

well I think Google does this incredibly

## 55370:00 - 55405:00

well and and sometimes I hesitate to

## 55405:00 - 55435:00

mention Google because they're like you

## 55435:00 - 55455:00

know some people like light we can't be

## 55455:00 - 55485:00

Global and we aren't really Advanced but

## 55485:00 - 55530:00

the thing I love about Google's approach

## 55530:00 - 55560:00

is that they've really taken kind of

## 55560:00 - 55590:00

this measurement phase approach to

## 55590:00 - 55610:00

things right even when they roll it out

## 55610:00 - 55630:00

in new places

## 55630:00 - 55675:00

um they're very systematic in how they

## 55675:00 - 55705:00

measure things they have incredible

## 55705:00 - 55725:00

Telemetry and tooling and

## 55725:00 - 55785:00

instrumentation and they continue

## 55785:00 - 55855:00

to invest time in

## 55855:00 - 55890:00

developer experience surveys and they

## 55890:00 - 55925:00

triangulate them and one thing that I

## 55925:00 - 55950:00

also love being able to point out here

## 55950:00 - 55985:00

is if there is ever a disagreement

## 55985:00 - 56040:00

between the surveys and the

## 56040:00 - 56070:00

instrumentation which is incredibly

## 56070:00 - 56105:00

Advanced almost every time every time

## 56105:00 - 56135:00

that I've ever heard of the surveys are

## 56135:00 - 56180:00

correct and not the instrumentation

## 56180:00 - 56210:00

amazing

## 56210:00 - 56230:00

I have just a couple more questions

## 56230:00 - 56260:00

unrelated to this topic is there

## 56260:00 - 56290:00

anything else that you thought you think

## 56290:00 - 56325:00

would be useful to share or leave people

## 56325:00 - 56390:00

with around this General space I would

## 56390:00 - 56405:00

say

## 56405:00 - 56445:00

that

## 56445:00 - 56485:00

like thinking about what it is you want

## 56485:00 - 56505:00

to do

## 56505:00 - 56545:00

is always important right like getting

## 56545:00 - 56585:00

crisp the ability to communicate clearly

## 56585:00 - 56620:00

is always one of the best things uh one

## 56620:00 - 56660:00

of I think one of my superpowers and one

## 56660:00 - 56675:00

of the things that I've been working

## 56675:00 - 56700:00

with my teams on doing and kind of

## 56700:00 - 56735:00

teaching them is and one of the things

## 56735:00 - 56760:00

that's really leveled up our work in

## 56760:00 - 56780:00

general is

## 56780:00 - 56815:00

making your work incredibly accessible

## 56815:00 - 56870:00

and accessible not necessarily like the

## 56870:00 - 56900:00

accessibility definition of the word but

## 56900:00 - 56940:00

making it very easy to understand what

## 56940:00 - 56985:00

you're doing for your key audiences and

## 56985:00 - 57005:00

so

## 57005:00 - 57030:00

thinking about

## 57030:00 - 57065:00

doing that for anything that you know

## 57065:00 - 57090:00

anyone who's listening for all of your

## 57090:00 - 57100:00

work

## 57100:00 - 57150:00

is super important right so who is it

## 57150:00 - 57175:00

that your audience is

## 57175:00 - 57205:00

what's their role

## 57205:00 - 57250:00

what words resonate with them and then

## 57250:00 - 57280:00

always being able to translate your work

## 57280:00 - 57295:00

into

## 57295:00 - 57325:00

a few sentences or a paragraph or left

## 57325:00 - 57355:00

or less

## 57355:00 - 57385:00

I love it a lot of the listeners of this

## 57385:00 - 57430:00

podcast are product managers and this is

## 57430:00 - 57465:00

so core to the work of a PM so I think

## 57465:00 - 57505:00

this is perfect speaking really directly

## 57505:00 - 57555:00

to a lot of the listeners okay so just a

## 57555:00 - 57575:00

couple more questions before this

## 57575:00 - 57605:00

podcast asks you a few questions

## 57605:00 - 57625:00

including just like what are people

## 57625:00 - 57675:00

asking you for advice often around and

## 57675:00 - 57700:00

are there any other Frameworks that you

## 57700:00 - 57715:00

find really useful and so there's a

## 57715:00 - 57735:00

couple things I just want to touch on

## 57735:00 - 57765:00

see if there's something interesting

## 57765:00 - 57775:00

there

## 57775:00 - 57815:00

the first is you have this framework

## 57815:00 - 57850:00

that you call the four box framework I'm

## 57850:00 - 57880:00

curious what that is and what it's all

## 57880:00 - 57930:00

about yes I love this four box framework

## 57930:00 - 57960:00

I've used it for years I actually pulled

## 57960:00 - 57995:00

it out first when I was a professor and

## 57995:00 - 58045:00

I still to this day get LinkedIn

## 58045:00 - 58070:00

messages from my students saying that

## 58070:00 - 58100:00

it's like the most useful thing they've

## 58100:00 - 58130:00

ever used so

## 58130:00 - 58165:00

here's what it is I literally pulled

## 58165:00 - 58200:00

this out on napkins at bars at

## 58200:00 - 58225:00

conferences to this day so here we go

## 58225:00 - 58285:00

draw four boxes on

## 58285:00 - 58330:00

piece of paper two on the top two on the

## 58330:00 - 58380:00

bottom so they'll be kind of aligned

## 58380:00 - 58430:00

the first two to the left of them write

## 58430:00 - 58485:00

the word words

## 58485:00 - 58570:00

and Below them write the word data

## 58570:00 - 58605:00

and then between the two on the top draw

## 58605:00 - 58650:00

an arrow between them so it'll say words

## 58650:00 - 58700:00

box Arrow box right is that making sense

## 58700:00 - 58740:00

then on the bottom it'll say data box

## 58740:00 - 58780:00

Arrow box

## 58780:00 - 58830:00

okay so on the top half

## 58830:00 - 58870:00

this is where if you want to think about

## 58870:00 - 58915:00

measuring something or testing something

## 58915:00 - 58970:00

you have to start with words so

## 58970:00 - 59055:00

as an example let's just say I think

## 59055:00 - 59105:00

that customer satisfaction gets us more

## 59105:00 - 59125:00

money

## 59125:00 - 59155:00

or customer satisfaction gets us return

## 59155:00 - 59175:00

customer so let's do customer

## 59175:00 - 59210:00

satisfaction so the first box you'll put

## 59210:00 - 59245:00

customer satisfaction inside the box and

## 59245:00 - 59270:00

you'll put return customers in the

## 59270:00 - 59300:00

second box

## 59300:00 - 59350:00

now always start with words do not start

## 59350:00 - 59375:00

with data you always start with words

## 59375:00 - 59405:00

and then you'll go around to a couple

## 59405:00 - 59460:00

people stakeholders managers others and

## 59460:00 - 59500:00

you'll say do you agree with do you

## 59500:00 - 59530:00

agree with this is this actually what

## 59530:00 - 59550:00

we're doing

## 59550:00 - 59600:00

it can turn into a sentence

## 59600:00 - 59645:00

and then in the boxes below it this is

## 59645:00 - 59675:00

your data how are we going to measure

## 59675:00 - 59720:00

customer satisfaction it could be a

## 59720:00 - 59750:00

survey and so like this is where you'll

## 59750:00 - 59795:00

go and you'll say like what data points

## 59795:00 - 59840:00

do we have that could proxy for what

## 59840:00 - 59870:00

could be our data points for

## 59870:00 - 59900:00

customer satisfaction and this is where

## 59900:00 - 59920:00

it gets tricky because you could say

## 59920:00 - 59945:00

well customer satisfaction could be

## 59945:00 - 59975:00

returned customers but we think it leads

## 59975:00 - 60000:00

to return customers so we can't use that

## 60000:00 - 60010:00

here

## 60010:00 - 60065:00

but return customers or could be so like

## 60065:00 - 60095:00

that's where you kind of like roll this

## 60095:00 - 60115:00

out

## 60115:00 - 60140:00

so house would measure customer

## 60140:00 - 60160:00

satisfaction that made this hard on

## 60160:00 - 60275:00

myself like a csat score yet csat NPS we

## 60275:00 - 60300:00

could say the amount of money that they

## 60300:00 - 60315:00

spent

## 60315:00 - 60350:00

it's a stretch

## 60350:00 - 60380:00

okay now

## 60380:00 - 60415:00

return customers let's go to the next

## 60415:00 - 60440:00

box

## 60440:00 - 60460:00

how are we going to measure return

## 60460:00 - 60480:00

customers

## 60480:00 - 60515:00

depending on our context let's say that

## 60515:00 - 60540:00

this is an online business

## 60540:00 - 60570:00

we could say that it's

## 60570:00 - 60605:00

returned customers as measured through

## 60605:00 - 60625:00

the website

## 60625:00 - 60650:00

we could say that it's returned

## 60650:00 - 60675:00

customers we could just ask them right

## 60675:00 - 60715:00

maybe we have a follow-up survey

## 60715:00 - 60745:00

return customers maybe we're going to do

## 60745:00 - 60775:00

a stretch here maybe we say it's a

## 60775:00 - 60830:00

referral link

## 60830:00 - 60865:00

this helps us get super clear on what it

## 60865:00 - 60905:00

is we're going to measure now the reason

## 60905:00 - 60945:00

I like this is because if some of our

## 60945:00 - 60980:00

now this data analysis we'll just do

## 60980:00 - 61000:00

correlations here right if we have

## 61000:00 - 61030:00

longitudinal over time that's fine you

## 61030:00 - 61065:00

can hand this to like a data scientist

## 61065:00 - 61090:00

you can hand this to somebody you can

## 61090:00 - 61120:00

say what data do we have let's go run

## 61120:00 - 61175:00

this if something here falls apart now

## 61175:00 - 61210:00

you can point to the

## 61210:00 - 61240:00

data boxes

## 61240:00 - 61295:00

and we can get mad about the things in

## 61295:00 - 61325:00

the data boxes and we can say what's

## 61325:00 - 61370:00

wrong is the data poor quality are we

## 61370:00 - 61415:00

missing data was this a bad proxy right

## 61415:00 - 61440:00

proxy stands in for something else was

## 61440:00 - 61475:00

this was this ridiculous right one of

## 61475:00 - 61510:00

the things I made up right like it was

## 61510:00 - 61545:00

just a bad idea

## 61545:00 - 61580:00

instead of

## 61580:00 - 61615:00

getting mad at Lenny for his really

## 61615:00 - 61645:00

stupid idea or getting mad at Nicole

## 61645:00 - 61675:00

because this was a really bad idea we

## 61675:00 - 61705:00

can say this was problematic what's

## 61705:00 - 61745:00

wrong here or we can go back up to the

## 61745:00 - 61780:00

words at the top and we can say

## 61780:00 - 61820:00

this is not actually something that is

## 61820:00 - 61855:00

probably going to hold or this is not

## 61855:00 - 61900:00

something we want to test right now or

## 61900:00 - 61945:00

this is something instead and it it

## 61945:00 - 61995:00

makes things incredibly clear it helps

## 61995:00 - 62020:00

you communicate what it is you want to

## 62020:00 - 62075:00

do fairly quickly

## 62075:00 - 62105:00

I love it here's my

## 62105:00 - 62160:00

check it out it's ugly nice zoom in

## 62160:00 - 62210:00

right okay now I will say advanced mode

## 62210:00 - 62235:00

you can start with the same four box

## 62235:00 - 62275:00

framework and you can say what data do

## 62275:00 - 62305:00

we have available

## 62305:00 - 62340:00

what do we think the relationships are

## 62340:00 - 62380:00

but then you have to go back up to words

## 62380:00 - 62405:00

and then say

## 62405:00 - 62450:00

for these data points and we think that

## 62450:00 - 62490:00

they like represent something and we

## 62490:00 - 62515:00

think uh we think this is the

## 62515:00 - 62550:00

relationship between them what do they

## 62550:00 - 62600:00

represent if I turn this into a sentence

## 62600:00 - 62650:00

what do they represent

## 62650:00 - 62680:00

and then you want to like double check

## 62680:00 - 62705:00

because you know spurious correlation is

## 62705:00 - 62735:00

one of my favorite websites instead of

## 62735:00 - 62765:00

charts so you'll want to go chat with

## 62765:00 - 62790:00

someone interview make sure things are

## 62790:00 - 62820:00

actually right

## 62820:00 - 62860:00

but the challenge is I will see people

## 62860:00 - 62890:00

run

## 62890:00 - 62925:00

every correlation they could think of

## 62925:00 - 62975:00

but they haven't turned it into a word

## 62975:00 - 63000:00

or a sentence that you can communicate

## 63000:00 - 63085:00

to someone else they don't do the check

## 63085:00 - 63125:00

and and they don't do that before one

## 63125:00 - 63165:00

before running the correlations and two

## 63165:00 - 63200:00

if it's there right all of our data is

## 63200:00 - 63240:00

so interrelated that we quite often will

## 63240:00 - 63280:00

find spurious correlations but it can be

## 63280:00 - 63305:00

really helpful just to have that laid

## 63305:00 - 63340:00

out like even if it's just on a Post-It

## 63340:00 - 63380:00

right to say what are the things I

## 63380:00 - 63400:00

expect to see what is this actually

## 63400:00 - 63440:00

testing what relationship do I suspect

## 63440:00 - 63475:00

is there mm-hmm

## 63475:00 - 63500:00

amazing there's actually I have a

## 63500:00 - 63530:00

newsletter post a guest post on how to

## 63530:00 - 63560:00

do a correlation analysis Center

## 63560:00 - 63605:00

regression analysis so folks can awesome

## 63605:00 - 63650:00

oh that's so great plug and play all

## 63650:00 - 63700:00

kinds of makes it easy for you so what

## 63700:00 - 63725:00

I'm taking away from this is this is an

## 63725:00 - 63750:00

awesome framework especially for

## 63750:00 - 63780:00

thinking about a hypothesis you may have

## 63780:00 - 63815:00

in this case it's like customer

## 63815:00 - 63850:00

satisfaction is going to lead to more

## 63850:00 - 63870:00

return customers here's how we're going

## 63870:00 - 63900:00

to measure it and then you basically run

## 63900:00 - 63925:00

the test and see if it's true and if

## 63925:00 - 63945:00

it's not maybe you need to pick

## 63945:00 - 63970:00

different metrics maybe you need to pick

## 63970:00 - 63990:00

a different conclusion

## 63990:00 - 64025:00

and within like the Dora framework we

## 64025:00 - 64055:00

would say if we want to improve our

## 64055:00 - 64105:00

speed and stability we think improving

## 64105:00 - 64140:00

build time would help and then how would

## 64140:00 - 64175:00

I measure build time right these are the

## 64175:00 - 64200:00

data points I have available to us yep

## 64200:00 - 64230:00

to Circle back I love it it's all

## 64230:00 - 64250:00

connected

## 64250:00 - 64305:00

okay and then last question I asked you

## 64305:00 - 64365:00

what advice people often ask you for and

## 64365:00 - 64390:00

you said that it's around making

## 64390:00 - 64430:00

decisions and I'm curious what advice do

## 64430:00 - 64465:00

you give people about making decisions

## 64465:00 - 64530:00

yes uh so this one comes up in business

## 64530:00 - 64590:00

but also comes up uh personally and

## 64590:00 - 64645:00

among my mentees so many times it starts

## 64645:00 - 64665:00

with you know being very cursive about

## 64665:00 - 64700:00

your objectives and definitions but then

## 64700:00 - 64740:00

it comes down to you know really clearly

## 64740:00 - 64800:00

defining what your criteria is what's

## 64800:00 - 64825:00

important

## 64825:00 - 64860:00

and then among that criteria what's most

## 64860:00 - 64900:00

important some of my friends know I have

## 64900:00 - 64950:00

a decision making spreadsheet

## 64950:00 - 64980:00

but I have shared out with a handful of

## 64980:00 - 65020:00

friends on you know should you take a

## 65020:00 - 65070:00

job where should you move uh what are

## 65070:00 - 65090:00

the different things really useful you

## 65090:00 - 65135:00

should do it is it's well it's funny

## 65135:00 - 65155:00

though because

## 65155:00 - 65195:00

what's interesting is many times I will

## 65195:00 - 65225:00

like I'll share it with someone and I've

## 65225:00 - 65265:00

got a couple that are just funny right

## 65265:00 - 65305:00

but walking through the spreadsheet is

## 65305:00 - 65360:00

often all you need to do in order to

## 65360:00 - 65395:00

know what the decision is and by that I

## 65395:00 - 65405:00

mean

## 65405:00 - 65430:00

so we walked through the decision I had

## 65430:00 - 65450:00

one where I was like where should I move

## 65450:00 - 65480:00

next or like what job should I take

## 65480:00 - 65510:00

right so when I started Dora I I did

## 65510:00 - 65560:00

this uh starting Dora I thought was my

## 65560:00 - 65590:00

lowest once I walked through the

## 65590:00 - 65620:00

spreadsheet it became my high so what

## 65620:00 - 65655:00

you do is you outline like of all of

## 65655:00 - 65680:00

your options what do you want to do and

## 65680:00 - 65710:00

then you say what are the criteria that

## 65710:00 - 65730:00

are important to me

## 65730:00 - 65770:00

so if it's for a job is it something

## 65770:00 - 65800:00

like uh

## 65800:00 - 65820:00

total comp

## 65820:00 - 65850:00

cash money

## 65850:00 - 65880:00

prestige

## 65880:00 - 65905:00

team

## 65905:00 - 65940:00

job predictability

## 65940:00 - 65980:00

work-life balance

## 65980:00 - 66010:00

identify the criteria that are most

## 66010:00 - 66030:00

important to you

## 66030:00 - 66055:00

now it's really interesting because

## 66055:00 - 66105:00

sometimes I will only get that far what

## 66105:00 - 66135:00

I'm working with

## 66135:00 - 66170:00

someone I'm mentoring or coaching and

## 66170:00 - 66200:00

they will say

## 66200:00 - 66240:00

I know what my answer is we don't even

## 66240:00 - 66270:00

get to the next step

## 66270:00 - 66320:00

but just identifying the criteria that

## 66320:00 - 66360:00

are important is it now when I was

## 66360:00 - 66380:00

thinking about where I wanted to move

## 66380:00 - 66445:00

next it was proximity to an airport the

## 66445:00 - 66480:00

relative texting the food scene that was

## 66480:00 - 66510:00

real high for me uh you know a handful

## 66510:00 - 66530:00

of things

## 66530:00 - 66575:00

that was important now the next thing I

## 66575:00 - 66620:00

do is for each criteria

## 66620:00 - 66665:00

what's their relative weight what's

## 66665:00 - 66705:00

their importance and I make it add up to

## 66705:00 - 66750:00

100 percent

## 66750:00 - 66790:00

and then I like this is the easy part

## 66790:00 - 66810:00

right like you just put it in a little

## 66810:00 - 66840:00

spreadsheet and I then I give everything

## 66840:00 - 66880:00

to score and I just multiply it out now

## 66880:00 - 66915:00

this is where I'm data informed and I'm

## 66915:00 - 66955:00

not data driven there have been times I

## 66955:00 - 66995:00

make a decision where you know the whole

## 66995:00 - 67025:00

like flip a coin and like

## 67025:00 - 67080:00

whatever it's wherever it lands on what

## 67080:00 - 67110:00

your reaction is tells you what it

## 67110:00 - 67145:00

should actually be there have been times

## 67145:00 - 67175:00

where I can multiply it out and then

## 67175:00 - 67200:00

I'll actually like fudge the numbers to

## 67200:00 - 67225:00

get what I want but it's still slightly

## 67225:00 - 67255:00

off

## 67255:00 - 67295:00

let's pray your data informed same thing

## 67295:00 - 67340:00

in business there are many times where

## 67340:00 - 67375:00

you actually run the numbers and it'll

## 67375:00 - 67425:00

give you a class or a category of things

## 67425:00 - 67460:00

and then you choose

## 67460:00 - 67485:00

now

## 67485:00 - 67515:00

this is where you know one of my

## 67515:00 - 67545:00

favorite quotes I heard somewhere about

## 67545:00 - 67580:00

strategy comes into play right and

## 67580:00 - 67620:00

that's that the key to having a good

## 67620:00 - 67665:00

strategy is knowing what not to do and

## 67665:00 - 67700:00

the key to executing a good strategy is

## 67700:00 - 67735:00

actually not doing it

## 67735:00 - 67765:00

um

## 67765:00 - 67815:00

so you can have many options right as a

## 67815:00 - 67840:00

leader and as an executive we have many

## 67840:00 - 67885:00

options and we only fund some of them

## 67885:00 - 67940:00

if you fund everything

## 67940:00 - 67980:00

things are going to fail

## 67980:00 - 68010:00

so being able to think through and

## 68010:00 - 68065:00

identify what your criteria are

## 68065:00 - 68110:00

identifying that criteria what's your

## 68110:00 - 68135:00

selection criteria what's your

## 68135:00 - 68190:00

evaluative criteria ranking them and

## 68190:00 - 68235:00

then deciding what the cutoff is

## 68235:00 - 68275:00

is important you can't fund everything

## 68275:00 - 68315:00

you don't get to pick everything

## 68315:00 - 68350:00

amazing I love the spreadsheet idea I've

## 68350:00 - 68395:00

made versions of it but it's always uh I

## 68395:00 - 68420:00

think like you said a lot of times the

## 68420:00 - 68455:00

exercise is just tell you what you

## 68455:00 - 68475:00

already think and just gives you like

## 68475:00 - 68505:00

yeah all right you're right you probably

## 68505:00 - 68520:00

should just do that thing you already

## 68520:00 - 68555:00

thought you should do yep

## 68555:00 - 68580:00

have you thought about making a public

## 68580:00 - 68605:00

template of this spreadsheet even though

## 68605:00 - 68635:00

it is simple I bet it would be really

## 68635:00 - 68660:00

helpful to people

## 68660:00 - 68695:00

I have and this actually might be a good

## 68695:00 - 68735:00

forcing function maybe okay awesome so

## 68735:00 - 68775:00

if uh if you do it I'll put in the show

## 68775:00 - 68800:00

notes it'll probably be near the bottom

## 68800:00 - 68825:00

at the end of the episode but that'd be

## 68825:00 - 68850:00

awesome perfect is there anything else

## 68850:00 - 68880:00

that you want to share before we get to

## 68880:00 - 68920:00

a very exciting lightning round uh no I

## 68920:00 - 68955:00

think that's it well Welcome to our very

## 68955:00 - 68995:00

exciting lightning round I've got six

## 68995:00 - 69025:00

questions for you are you ready

## 69025:00 - 69075:00

absolutely all right first question what

## 69075:00 - 69100:00

are two or three books that you've

## 69100:00 - 69140:00

recommended most to other people

## 69140:00 - 69170:00

we actually had the perfect segue

## 69170:00 - 69190:00

because the book I've recommended

## 69190:00 - 69215:00

absolutely the most is called good

## 69215:00 - 69270:00

strategy bad strategy by Richard rumelt

## 69270:00 - 69320:00

another one is designing your life by uh

## 69320:00 - 69355:00

Bill Burnett and Dave Abbott Dave Evans

## 69355:00 - 69400:00

uh and the last one is probably Ender's

## 69400:00 - 69460:00

Game horses got card um no comment right

## 69460:00 - 69500:00

now on uh

## 69500:00 - 69545:00

some of his political commentary but I

## 69545:00 - 69590:00

used to have extra copies in my office

## 69590:00 - 69615:00

when I was a professor and I would just

## 69615:00 - 69645:00

hand it out to my students it's a fun

## 69645:00 - 69690:00

like just easy nonsense read but

## 69690:00 - 69730:00

I absolutely love it such a such a good

## 69730:00 - 69775:00

pick haven't read it in a long time and

## 69775:00 - 69805:00

are they making a show of that at all

## 69805:00 - 69835:00

that'd be that'd be something they made

## 69835:00 - 69865:00

a movie and I was afraid I wasn't gonna

## 69865:00 - 69890:00

like it so I just didn't read it because

## 69890:00 - 69920:00

I didn't want it to ruin the book

## 69920:00 - 69975:00

but at least Harrison Ford was in it

## 69975:00 - 70000:00

okay I'm not gonna check it out they're

## 70000:00 - 70025:00

making a movie of three body problem I

## 70025:00 - 70040:00

don't know if you've read that but that

## 70040:00 - 70080:00

is I'm really excited it's on my list

## 70080:00 - 70135:00

oh man best best sci-fi ever next

## 70135:00 - 70180:00

question actually very correlated what

## 70180:00 - 70215:00

is a favorite recent movie or TV show

## 70215:00 - 70250:00

I've been going through like some real

## 70250:00 - 70310:00

just easy fun watches lately uh

## 70310:00 - 70365:00

I'm re-watching suits again but Ted

## 70365:00 - 70410:00

lasso is a favorite and I just tore

## 70410:00 - 70440:00

through never have I ever which is fun

## 70440:00 - 70495:00

because John Mcenroe narrates it which

## 70495:00 - 70525:00

is hilarious John mcenro the tennis

## 70525:00 - 70570:00

player yeah it's a riot yeah it's so

## 70570:00 - 70590:00

funny

## 70590:00 - 70640:00

I love it next question what's a

## 70640:00 - 70665:00

favorite interview question that you

## 70665:00 - 70685:00

like to ask people when you're

## 70685:00 - 70730:00

interviewing them I love questions that

## 70730:00 - 70765:00

I can kind of spin around hard decisions

## 70765:00 - 70800:00

that people have had to make and how

## 70800:00 - 70830:00

they made them I love hearing their

## 70830:00 - 70865:00

thought process

## 70865:00 - 70890:00

and I get a little nervous when people

## 70890:00 - 70910:00

just like yellow and shoot from the hip

## 70910:00 - 70955:00

constantly so what is it you look for

## 70955:00 - 70980:00

there that gives you a sense that

## 70980:00 - 71005:00

they're someone you may want to hire

## 71005:00 - 71040:00

work with I just like hearing if they

## 71040:00 - 71085:00

have some sort of process right if they

## 71085:00 - 71100:00

have some kind of decision-making

## 71100:00 - 71140:00

process if they have criteria if they

## 71140:00 - 71190:00

have like how do they do evaluation

## 71190:00 - 71220:00

what is a favorite product you've

## 71220:00 - 71250:00

recently discovered that you love I have

## 71250:00 - 71280:00

a big one and a little one um my big one

## 71280:00 - 71330:00

is probably sleep eight so I live in

## 71330:00 - 71355:00

Arizona it gets it gets hot here

## 71355:00 - 71395:00

sometimes oh he ate sleep or yeah ate

## 71395:00 - 71420:00

sleep yeah the other way around

## 71420:00 - 71450:00

um yeah so that one's fun because it

## 71450:00 - 71485:00

cool it makes the bed cold and also

## 71485:00 - 71530:00

gives me some some data which is

## 71530:00 - 71560:00

probably like a little bit off but in

## 71560:00 - 71595:00

the approximations fund

## 71595:00 - 71640:00

um and then Korean face masks they're

## 71640:00 - 71675:00

just fun yeah you can get some some

## 71675:00 - 71700:00

pretty good ones for like just a couple

## 71700:00 - 71745:00

dollars and that's always fun self-care

## 71745:00 - 71780:00

first mention of that one of Korean face

## 71780:00 - 71820:00

masks right listen everyone get on board

## 71820:00 - 71870:00

I just did the uh Tick Tock there's a

## 71870:00 - 71890:00

filter now where you could see how you

## 71890:00 - 71940:00

look when you age and I'm not happy with

## 71940:00 - 71985:00

how it turned out and so I might look

## 71985:00 - 72000:00

into this

## 72000:00 - 72050:00

I had some basal cell uh cancer on my

## 72050:00 - 72085:00

forehead a few years ago and so I am

## 72085:00 - 72125:00

much more careful with my skin and you

## 72125:00 - 72150:00

can get like one of my favorites is

## 72150:00 - 72210:00

cosrx you can get 10 for like 15 so it's

## 72210:00 - 72235:00

fun to just like chill at the end of the

## 72235:00 - 72265:00

day with a good with a good face mask I

## 72265:00 - 72290:00

was gonna ask you for a specific pick

## 72290:00 - 72340:00

and so we got one yep amazing

## 72340:00 - 72390:00

this next question I ask everyone and

## 72390:00 - 72420:00

it's especially appropriate to you but I

## 72420:00 - 72450:00

don't know if you'll have an answer but

## 72450:00 - 72475:00

something relatively minor you've

## 72475:00 - 72490:00

changed in your product development

## 72490:00 - 72535:00

process that has had a big impact on

## 72535:00 - 72560:00

your team's ability to execute and I

## 72560:00 - 72595:00

feel like you have a big perspective on

## 72595:00 - 72635:00

this so I'm curious what you have as an

## 72635:00 - 72665:00

answer uh I think I alluded to this

## 72665:00 - 72720:00

earlier I would say that it's you know

## 72720:00 - 72765:00

helping everyone so I've done this

## 72765:00 - 72785:00

before but I think it's helping everyone

## 72785:00 - 72830:00

to ask who's our audience and how will

## 72830:00 - 72850:00

we share this now

## 72850:00 - 72875:00

and it's sort of interesting because

## 72875:00 - 72915:00

right now I'm wearing two hats

## 72915:00 - 72975:00

one is at MSR Microsoft research we need

## 72975:00 - 73035:00

very ambitious research right so like

## 73035:00 - 73110:00

h2h3 I mean what is H3 the third half uh

## 73110:00 - 73145:00

oh Horizon three

## 73145:00 - 73190:00

like five to ten years out which right

## 73190:00 - 73240:00

now is like who even knows right

## 73240:00 - 73300:00

in computers yeah AI has like completely

## 73300:00 - 73335:00

upended how we kind of think of Horizons

## 73335:00 - 73375:00

and so when we're when we're thinking

## 73375:00 - 73405:00

really ambitiously and very very very

## 73405:00 - 73435:00

forward looking

## 73435:00 - 73475:00

what's our check-in how do we evaluate

## 73475:00 - 73500:00

this and then how can we easily

## 73500:00 - 73535:00

communicate it to our core audience and

## 73535:00 - 73580:00

so here who's our audience and how do we

## 73580:00 - 73620:00

bring the far near

## 73620:00 - 73650:00

and then for the other hat I'm wearing

## 73650:00 - 73695:00

I'm working with octo kind of across all

## 73695:00 - 73740:00

of Microsoft to

## 73740:00 - 73770:00

take a data informed approach to really

## 73770:00 - 73810:00

improve and up level our Central

## 73810:00 - 73840:00

developer infrastructure

## 73840:00 - 73890:00

and so as we're thinking very very

## 73890:00 - 73935:00

tactically what is our long-term vision

## 73935:00 - 73965:00

and how do we align with several of our

## 73965:00 - 74005:00

broad stakeholders and so there it's

## 74005:00 - 74035:00

who's our audience and how do we bring

## 74035:00 - 74070:00

the near far

## 74070:00 - 74095:00

I love that

## 74095:00 - 74140:00

final question what is one tactical

## 74140:00 - 74190:00

piece of advice that listeners can do

## 74190:00 - 74220:00

this week to help improve their

## 74220:00 - 74255:00

developer productivity or developer

## 74255:00 - 74270:00

experience and move it in the right

## 74270:00 - 74305:00

direction you know if you walk away from

## 74305:00 - 74330:00

this podcast right now

## 74330:00 - 74365:00

you could take a look at what's

## 74365:00 - 74400:00

happening in New York today is it

## 74400:00 - 74455:00

written down is it clear do you have any

## 74455:00 - 74510:00

existing data and efforts and if not go

## 74510:00 - 74550:00

find a handful of developers and ask

## 74550:00 - 74610:00

them how they feel about their work

## 74610:00 - 74640:00

tools and their work process and what

## 74640:00 - 74655:00

the biggest barriers to their

## 74655:00 - 74680:00

productivity are

## 74680:00 - 74720:00

also pick up a copy of accelerate on

## 74720:00 - 74750:00

Amazon or your local retail

## 74750:00 - 74790:00

establishment Nicole this was amazing I

## 74790:00 - 74805:00

think we're going to help a lot of

## 74805:00 - 74845:00

companies move faster have better and

## 74845:00 - 74870:00

happier Engineers which is going to

## 74870:00 - 74915:00

create infinite value in the world thank

## 74915:00 - 74940:00

you so much for being here two final

## 74940:00 - 74965:00

questions where can folks find you

## 74965:00 - 75005:00

online if they want to reach out and how

## 75005:00 - 75055:00

can listeners be useful to you I'm on

## 75055:00 - 75085:00

Twitter and Bluesky

## 75085:00 - 75135:00

um Nicole FV and my website is

## 75135:00 - 75185:00

nicolefe.com and my all my contact

## 75185:00 - 75235:00

information is there and as we mentioned

## 75235:00 - 75265:00

previously I'm working on a new project

## 75265:00 - 75305:00

and a new book digging into exactly

## 75305:00 - 75345:00

these ideas right how can we measure

## 75345:00 - 75385:00

better how can we improve and what does

## 75385:00 - 75410:00

that measurement process look like both

## 75410:00 - 75460:00

for kind of one-time really quick you

## 75460:00 - 75490:00

know unofficial measurement pieces and

## 75490:00 - 75525:00

if we want to do kind of very formal

## 75525:00 - 75570:00

longer term measurement pieces so if

## 75570:00 - 75610:00

anyone is interested in that or has any

## 75610:00 - 75645:00

success stories they'd love to share I

## 75645:00 - 75690:00

would love to hear more about it so

## 75690:00 - 75725:00

please reach out and share I'd love to

## 75725:00 - 75740:00

hear more

## 75740:00 - 75780:00

awesome Nicole thank you again for being

## 75780:00 - 75865:00

here hey thank you Lenny bye everyone

## 75865:00 - 75905:00

thank you so much for listening if you

## 75905:00 - 75935:00

found this valuable you can subscribe to

## 75935:00 - 75980:00

the show on Apple podcast Spotify or

## 75980:00 - 76015:00

your favorite podcast app also please

## 76015:00 - 76055:00

consider giving us a rating or leaving a

## 76055:00 - 76080:00

review as that really helps other

## 76080:00 - 76120:00

listeners find the podcast you can find

## 76120:00 - 76155:00

all past episodes or learn more about

## 76155:00 - 76200:00

the show at lennyspodcast.com

## 76200:00+

see you in the next episode

