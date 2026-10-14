---
source: https://www.youtube.com/watch?v=hEzpiDuYFoE
title: The ultimate guide to A/B testing | Ronny Kohavi (Airbnb, Microsoft, Amazon)
author: Lenny's Podcast
date: 2023-07-27
views: 72717
description: |-
  Ronny Kohavi, PhD, is a consultant, teacher, and leading expert on the art and science of A/B testing. Previously, Ronny was Vice President and Technical Fellow at Airbnb, Technical Fellow and corporate VP at Microsoft (where he led the Experimentation Platform team), and Director of Data Mining and Personalization at Amazon. He was also honored with a lifetime achievement award by the Experimentation Culture Awards in September 2020 and teaches a popular course on experimentation on Maven. In today’s podcast, we discuss:
  • How to foster a culture of experimentation
  • How to avoid common pitfalls and misconceptions when running experiments
  • His most surprising experiment results
  • The critical role of trust in running successful experiments
  • When not to A/B test something
  • Best practices for helping your tests run faster
  • The future of experimentation

  Enroll in Ronny’s Maven class, Accelerating Innovation with A/B Testing, at https://bit.ly/ABClassLenny. Promo code “LENNYAB” will give $500 off the class for the first 10 people to use it.
  —

  Brought to you by Mixpanel—Event analytics that everyone can trust, use, and afford: https://mixpanel.com/startups  | Round—The private network built by tech leaders for tech leaders: https://www.round.tech/apply?utm_campaign=lennys-letter&utm_medium=email-ad&utm_source=email-marketing&utm_content=send-2-2023-07-27 | Eppo—Run reliable, impactful experiments: https://www.geteppo.com/

  Find the full transcript at: https://www.lennysnewsletter.com/p/the-ultimate-guide-to-ab-testing

  Where to find Ronny Kohavi:
  • Twitter: https://twitter.com/ronnyk
  • LinkedIn: https://www.linkedin.com/in/ronnyk/
  • Website: http://ai.stanford.edu/~ronnyk/

  Where to find Lenny:
  • Newsletter: https://www.lennysnewsletter.com
  • Twitter: https://twitter.com/lennysan
  • LinkedIn: https://www.linkedin.com/in/lennyrachitsky/

  In this episode, we cover:
  (00:00) Ronny’s background
  (04:29) How one A/B test helped Bing increase revenue by 12%
  (09:00) What data says about opening new tabs
  (10:34) Small effort, huge gains vs. incremental improvements 
  (13:16) Typical fail rates
  (15:28) UI resources
  (16:53) Institutional learning and the importance of documentation and sharing results
  (20:44) Testing incrementally and acting on high-risk, high-reward ideas
  (22:38) A failed experiment at Bing on integration with social apps
  (24:47) When not to A/B test something
  (27:59) Overall evaluation criterion (OEC)
  (32:41) Long-term experimentation vs. models 
  (36:29) The problem with redesigns
  (39:31) How Ronny implemented testing at Microsoft
  (42:54) The stats on redesigns 
  (45:38) Testing at Airbnb
  (48:06) Covid’s impact and why testing is more important during times of upheaval 
  (50:06) Ronny’s book, Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing
  (51:45) The importance of trust
  (55:25) Sample ratio mismatch and other signs your experiment is flawed
  (1:00:44) Twyman’s law
  (1:02:14) P-value
  (1:06:27) Getting started running experiments
  (1:07:43) How to shift the culture in an org to push for more testing
  (1:10:18) Building platforms
  (1:12:25) How to improve speed when running experiments
  (1:14:09) Lightning round

  Referenced:
  • Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing: https://experimentguide.com/
  • Seven rules of thumb for website experimenters: https://exp-platform.com/rules-of-thumb/
  • GoodUI: https://goodui.org
  • Defaults for A/B testing: http://bit.ly/CH2022Kohavi
  • Ronny’s LinkedIn post about A/B testing for startups: https://www.linkedin.com/posts/ronnyk_abtesting-experimentguide-statisticalpower-activity-6982142843297423360-Bc2U
  • Sanchan Saxena on Lenny’s Podcast: https://www.lennyspodcast.com/sanchan-saxena-vp-of-product-at-coinbase-on-the-inside-story-of-how-airbnb-made-it-through-covid-what-he8217s-learned-from-brian-chesky-brian-armstrong-and-kevin-systrom-much-more/
  • Optimizely: https://www.optimizely.com/
  • Optimizely was statistically naive: https://analythical.com/blog/optimizely-got-me-fired
  • SRM: https://www.linkedin.com/posts/ronnyk_seat-belt-wikipedia-activity-6917959519310401536-jV97
  • SRM checker: http://bit.ly/srmCheck
  • Twyman’s law: http://bit.ly/twymanLaw
  • “What’s a p-value” question: http://bit.ly/ABTestingIntuitionBusters
  • Fisher’s method: https://en.wikipedia.org/wiki/Fisher%27s_method
  • Evolving experimentation: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf
  • CUPED for variance reduction/increased sensitivity: http://bit.ly/expCUPED
  • Ronny’s recommended books: https://bit.ly/BestBooksRonnyk
  • Chernobyl on HBO: https://www.hbo.com/chernobyl
  • Blink cameras: https://blinkforhome.com/
  • Narrative not PowerPoint: https://exp-platform.com/narrative-not-powerpoint/

  Production and marketing by https://penname.co/. For inquiries about sponsoring the podcast, email podcast@lennyrachitsky.com.

  Lenny may be an investor in the companies discussed.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-01T11:53:49.933Z
---

# The ultimate guide to A/B testing | Ronny Kohavi (Airbnb, Microsoft, Amazon)

## 00:00 - 45:00

I'm very clear that I'm a big fan of

## 45:00 - 90:00

test everything which is any code change

## 90:00 - 110:00

that you make

## 110:00 - 165:00

any feature that you introduce has to be

## 165:00 - 195:00

in some experiment because again I've

## 195:00 - 225:00

observed this sort of

## 225:00 - 270:00

surprising result that even small bug

## 270:00 - 315:00

fixes even small changes can sometimes

## 315:00 - 370:00

have surprising unexpected impact

## 370:00 - 410:00

and so I don't think it's possible to

## 410:00 - 455:00

experiment too much you have to allocate

## 455:00 - 510:00

sometimes to these high risk High reward

## 510:00 - 535:00

ideas we're going to try something

## 535:00 - 580:00

that's most likely to fail

## 580:00 - 625:00

but if it does win it's going to be a

## 625:00 - 680:00

home run and you have to be ready to

## 680:00 - 720:00

understand and agree that most will fail

## 720:00 - 755:00

and it's amazing how many times I've

## 755:00 - 820:00

seen people come up with new designs or

## 820:00 - 865:00

a radical new idea and they believe in

## 865:00 - 915:00

it and that's okay I'm just cautioning

## 915:00 - 935:00

them all the time to say hey if you go

## 935:00 - 960:00

for something big

## 960:00 - 1025:00

try it out but be ready to fail eighty

## 1025:00 - 1080:00

percent of the time

## 1080:00 - 1125:00

welcome to Lenny's podcast where I

## 1125:00 - 1150:00

interview world-class product leaders

## 1150:00 - 1175:00

and growth experts to learn from their

## 1175:00 - 1200:00

hard-winning experiences building and

## 1200:00 - 1235:00

growing today's most successful products

## 1235:00 - 1290:00

today my guest is Ronnie kohavi Rani is

## 1290:00 - 1335:00

seen by many as the world expert on a b

## 1335:00 - 1375:00

testing and experimentation most

## 1375:00 - 1410:00

recently usvp and Technical fellow of

## 1410:00 - 1445:00

relevance at Airbnb where you led their

## 1445:00 - 1480:00

search experience team prior to that he

## 1480:00 - 1505:00

was corporate vice president and

## 1505:00 - 1530:00

Microsoft where he led Microsoft's

## 1530:00 - 1570:00

experimentation platform team before

## 1570:00 - 1600:00

that he was director of data mining and

## 1600:00 - 1640:00

personalization at Amazon he's currently

## 1640:00 - 1675:00

a full-time advisor and instructor he's

## 1675:00 - 1715:00

also the author of the go-to book on

## 1715:00 - 1750:00

experimentation called trustworthy

## 1750:00 - 1785:00

online controlled experiments and in our

## 1785:00 - 1825:00

show notes you'll find a code to get a

## 1825:00 - 1860:00

discount on taking his live cohort based

## 1860:00 - 1900:00

course on Maven in our conversation we

## 1900:00 - 1945:00

get super tactical about a b testing

## 1945:00 - 1980:00

Ronnie shares his advice for when you

## 1980:00 - 2000:00

should start considering running

## 2000:00 - 2030:00

experiments at your company how to

## 2030:00 - 2055:00

change your company's culture to be more

## 2055:00 - 2090:00

experiment driven what are signs your

## 2090:00 - 2135:00

experiments are potentially invalid why

## 2135:00 - 2175:00

trust is the most important element of a

## 2175:00 - 2205:00

successful experiment culture and

## 2205:00 - 2240:00

platform how to get started if you want

## 2240:00 - 2265:00

to start running experiments at your

## 2265:00 - 2300:00

company it also explains what actually

## 2300:00 - 2335:00

is a p-value and something called

## 2335:00 - 2380:00

twyman's Law plus some hot takes about

## 2380:00 - 2430:00

Airbnb and experiments in general this

## 2430:00 - 2455:00

episode is for anyone who's interested

## 2455:00 - 2490:00

in either creating an experiment driven

## 2490:00 - 2515:00

culture at their company or just

## 2515:00 - 2550:00

fine-tuning one that already exists

## 2550:00 - 2600:00

enjoy this episode with Ronnie kohavi

## 2600:00 - 2655:00

after a short word from our sponsors

## 2655:00 - 2690:00

this episode is brought to you by

## 2690:00 - 2730:00

mixpanel get deep insights into what

## 2730:00 - 2760:00

your users are doing at every stage of

## 2760:00 - 2800:00

the funnel at a fair price that scales

## 2800:00 - 2835:00

as you grow mixpanel gives you quick

## 2835:00 - 2870:00

answers about your users from awareness

## 2870:00 - 2915:00

to acquisition through retention and by

## 2915:00 - 2960:00

capturing website activity add data and

## 2960:00 - 2985:00

multi-touch attribution right in

## 2985:00 - 3025:00

mixpanel you can improve every aspect of

## 3025:00 - 3060:00

the full user funnel powered by first

## 3060:00 - 3095:00

party behavioral data instead of

## 3095:00 - 3130:00

third-party cookies mixed panels built

## 3130:00 - 3155:00

to be more powerful and easier to use

## 3155:00 - 3200:00

than Google analytics explore plans for

## 3200:00 - 3225:00

teams of every size and see what

## 3225:00 - 3270:00

mixpanel can do for you at mixpanel.com

## 3270:00 - 3320:00

friends slash Lenny and while you're at

## 3320:00 - 3360:00

it they're also hiring so check it out

## 3360:00 - 3450:00

at mixpanel.com friends slash Lenny

## 3450:00 - 3495:00

this episode is brought to you by round

## 3495:00 - 3535:00

round is the private Network built by

## 3535:00 - 3575:00

Tech leaders for Tech leaders round

## 3575:00 - 3615:00

combines the best of coaching learning

## 3615:00 - 3650:00

and authentic relationships to help you

## 3650:00 - 3680:00

identify where you want to go and

## 3680:00 - 3715:00

accelerate your path to get there which

## 3715:00 - 3745:00

is why their weightless tops thousands

## 3745:00 - 3790:00

of tech execs round is on a mission to

## 3790:00 - 3820:00

shape the future of technology and its

## 3820:00 - 3860:00

impact on society leading in Tech is

## 3860:00 - 3890:00

uniquely challenging and doing it well

## 3890:00 - 3925:00

is easiest when surrounded by leaders

## 3925:00 - 3950:00

who understand your day-to-day

## 3950:00 - 3990:00

experiences when we're meeting and

## 3990:00 - 4015:00

building relationships with the right

## 4015:00 - 4055:00

people we're more likely to learn find

## 4055:00 - 4090:00

new opportunities be dynamic in our

## 4090:00 - 4130:00

thinking and Achieve our goals building

## 4130:00 - 4160:00

and managing your network doesn't have

## 4160:00 - 4205:00

to feel like networking join around to

## 4205:00 - 4230:00

surround yourself with leaders from

## 4230:00 - 4270:00

Tech's most Innovative companies build

## 4270:00 - 4310:00

relationships The Inspired take action

## 4310:00 - 4365:00

visit round.tech slash apply and use

## 4365:00 - 4395:00

promo code Lenny to skip the waitlist

## 4395:00 - 4450:00

that's round dot Tech slash apply

## 4450:00 - 4495:00

thank you

## 4495:00 - 4545:00

Ronnie welcome to the podcast

## 4545:00 - 4575:00

thank you for having me

## 4575:00 - 4615:00

so you're known by many as maybe the

## 4615:00 - 4650:00

leading expert on a b testing and

## 4650:00 - 4685:00

experimentation which I think is

## 4685:00 - 4700:00

something every Product Company

## 4700:00 - 4740:00

eventually ends up trying to do often

## 4740:00 - 4790:00

badly and so I'm excited to dig quite

## 4790:00 - 4825:00

deep into the world of experimentation

## 4825:00 - 4860:00

and a b testing to help people run

## 4860:00 - 4890:00

better experiments so thank you again

## 4890:00 - 4930:00

for being here great goal thank you

## 4930:00 - 4970:00

let me start with kind of a fun question

## 4970:00 - 5025:00

what is maybe the most unexpected a B

## 5025:00 - 5050:00

test you've run or maybe the most

## 5050:00 - 5080:00

surprising result from an A B test that

## 5080:00 - 5130:00

you run yeah so I think the the opening

## 5130:00 - 5190:00

example that I use in my book and in my

## 5190:00 - 5210:00

class

## 5210:00 - 5260:00

is the most surprising public example we

## 5260:00 - 5315:00

can talk about and this is this was kind

## 5315:00 - 5345:00

of an interesting

## 5345:00 - 5400:00

experiment somebody proposed to change

## 5400:00 - 5450:00

the way that ads were displayed on Bing

## 5450:00 - 5490:00

the search engine and he basically said

## 5490:00 - 5535:00

let's take the second line and move it

## 5535:00 - 5565:00

promote it to the first line so that the

## 5565:00 - 5625:00

title line becomes larger and when you

## 5625:00 - 5655:00

think about that and there's you know if

## 5655:00 - 5700:00

you're going to look in my uh book or in

## 5700:00 - 5735:00

the class There's an actual diagram of

## 5735:00 - 5780:00

what happened uh the screenshots but if

## 5780:00 - 5805:00

you think about it it's just

## 5805:00 - 5855:00

realistically it looks like an idea like

## 5855:00 - 5900:00

why would this be such a reasonable

## 5900:00 - 5945:00

interesting thing to do

## 5945:00 - 5980:00

uh and indeed when we went back to the

## 5980:00 - 6025:00

backlog it was on the backlog for months

## 6025:00 - 6070:00

and language there and many things were

## 6070:00 - 6130:00

rated higher but the point about this is

## 6130:00 - 6165:00

it's trivial to implement so if you

## 6165:00 - 6205:00

think about return on investment

## 6205:00 - 6255:00

we could get the data by having some

## 6255:00 - 6285:00

Engineers spend a couple of hours

## 6285:00 - 6335:00

implementing it and that's exactly what

## 6335:00 - 6380:00

happened somebody uh Ed Bing who kept

## 6380:00 - 6410:00

seeing this in the backlog and said my

## 6410:00 - 6435:00

God we're spending too much time

## 6435:00 - 6465:00

discussing it I could just Implement

## 6465:00 - 6505:00

that he did he spent a couple of days

## 6505:00 - 6550:00

implementing it and as is you know the

## 6550:00 - 6590:00

common uh thing at Bing he launched the

## 6590:00 - 6615:00

experiment

## 6615:00 - 6650:00

uh and a funny thing happened

## 6650:00 - 6675:00

we had an alarm

## 6675:00 - 6715:00

big escalation something is wrong with

## 6715:00 - 6745:00

the revenue metric

## 6745:00 - 6785:00

now this alarm fired several times in

## 6785:00 - 6810:00

the past when there were real mistakes

## 6810:00 - 6850:00

where somebody would log Revenue twice

## 6850:00 - 6885:00

or you know there's some data problem

## 6885:00 - 6955:00

but in this case there was no bug we

## 6955:00 - 7000:00

that simple idea increased Revenue by

## 7000:00 - 7025:00

about 12 percent

## 7025:00 - 7050:00

and this is something that just doesn't

## 7050:00 - 7085:00

happen we can talk later about

## 7085:00 - 7110:00

employment's law but that was the first

## 7110:00 - 7140:00

reaction which is this is too good to be

## 7140:00 - 7175:00

true let's find the bug

## 7175:00 - 7225:00

uh and we did and we looked for several

## 7225:00 - 7255:00

times and we replicated the experiment

## 7255:00 - 7275:00

several times and there was nothing

## 7275:00 - 7315:00

wrong with it this thing was worth a

## 7315:00 - 7345:00

hundred million dollars at the time when

## 7345:00 - 7375:00

Bing was a lot smaller

## 7375:00 - 7425:00

and the key thing is it didn't hurt the

## 7425:00 - 7465:00

user metric so it's very easy to

## 7465:00 - 7505:00

increase Revenue by doing theatrics that

## 7505:00 - 7525:00

you know displaying more ads is a

## 7525:00 - 7560:00

trivial way to raise revenue but it

## 7560:00 - 7585:00

hurts the user experience and we've done

## 7585:00 - 7620:00

the experiments to show that in this

## 7620:00 - 7635:00

case

## 7635:00 - 7680:00

this was just a home run that improved

## 7680:00 - 7735:00

Revenue didn't significantly hurt the

## 7735:00 - 7790:00

the guardrail metrics and so I was we

## 7790:00 - 7830:00

were like in awe of you know what a

## 7830:00 - 7855:00

trivial change

## 7855:00 - 7895:00

that was the biggest

## 7895:00 - 7940:00

Revenue impact of being in all its

## 7940:00 - 7970:00

history and that was basically shifting

## 7970:00 - 8000:00

in two lines right switching two lines

## 8000:00 - 8040:00

in the search results right and this was

## 8040:00 - 8075:00

just moving the second line to the first

## 8075:00 - 8105:00

line now you then go and run a lot of

## 8105:00 - 8140:00

experiments to understand what happened

## 8140:00 - 8185:00

here is it the fact that the title line

## 8185:00 - 8220:00

has a bigger font sometimes different

## 8220:00 - 8265:00

color so we ran a whole bunch of

## 8265:00 - 8285:00

experiments and this is what usually

## 8285:00 - 8325:00

happens we have a breakthrough

## 8325:00 - 8385:00

you start to understand more about what

## 8385:00 - 8420:00

can we do and there was suddenly a shift

## 8420:00 - 8455:00

towards okay what are other things we

## 8455:00 - 8510:00

could do that would allow us to improve

## 8510:00 - 8530:00

Revenue we came up with a lot of

## 8530:00 - 8570:00

follow-on ideas that helped a lot but to

## 8570:00 - 8645:00

me this was an example of a tiny change

## 8645:00 - 8685:00

that was the best Revenue generating

## 8685:00 - 8740:00

idea in Bing's history and

## 8740:00 - 8790:00

and rated properly right nobody gave

## 8790:00 - 8835:00

this the the priority that in hindsight

## 8835:00 - 8870:00

it deserves and that that's something

## 8870:00 - 8910:00

that happens often I mean we are often

## 8910:00 - 8970:00

humbled by how bad we are at predicting

## 8970:00 - 9025:00

the outcome of experiments this reminds

## 9025:00 - 9060:00

me of a classic experiment at Airbnb

## 9060:00 - 9080:00

while I was there and we'll talk about

## 9080:00 - 9135:00

Airbnb in a bit the search team just ran

## 9135:00 - 9170:00

a small experiment of what if we were to

## 9170:00 - 9205:00

open a new tab every time someone

## 9205:00 - 9240:00

clicked on a search result instead of

## 9240:00 - 9265:00

just going straight to that listing and

## 9265:00 - 9300:00

that was one of the biggest wins in

## 9300:00 - 9325:00

search yeah and by the way I I don't

## 9325:00 - 9350:00

know if you know the history of this but

## 9350:00 - 9390:00

I tell about this in class we did this

## 9390:00 - 9410:00

experiment

## 9410:00 - 9455:00

way back around

## 9455:00 - 9515:00

2008 I think and so this predates Airbnb

## 9515:00 - 9570:00

and I remember it was heavily debated

## 9570:00 - 9600:00

like why would you open something in a

## 9600:00 - 9645:00

new tab the users didn't ask for it uh

## 9645:00 - 9670:00

it was a lot of pushback from the

## 9670:00 - 9715:00

designers and we ran that experiment and

## 9715:00 - 9745:00

again it was one of these highly

## 9745:00 - 9795:00

surprising results that made it

## 9795:00 - 9835:00

that we learned so much from it so we

## 9835:00 - 9885:00

first did this it was done in the UK for

## 9885:00 - 9930:00

opening Hotmail and then we moved it to

## 9930:00 - 9985:00

MSN so it would open search in Utah and

## 9985:00 - 10015:00

all the set of experiments were highly

## 10015:00 - 10055:00

highly beneficial we published this and

## 10055:00 - 10095:00

I have to tell you when I came to Airbnb

## 10095:00 - 10135:00

I talked to our joint friend Ricardo

## 10135:00 - 10185:00

about this and it was sort of done it

## 10185:00 - 10215:00

was very beneficial and that it was

## 10215:00 - 10235:00

semi-forgotten

## 10235:00 - 10265:00

which is one of the things you learned

## 10265:00 - 10295:00

about institutional memories when you

## 10295:00 - 10330:00

have winners make sure to address them

## 10330:00 - 10385:00

and remember them so it was an Airbnb

## 10385:00 - 10420:00

done for a long time before I joined

## 10420:00 - 10455:00

that listings opened in a new tab but

## 10455:00 - 10495:00

other things that were designed in the

## 10495:00 - 10520:00

future were not done and I reintroduced

## 10520:00 - 10560:00

this to the team and we saw big

## 10560:00 - 10580:00

improvements

## 10580:00 - 10610:00

shout out to Ricardo or mutual friend

## 10610:00 - 10630:00

who helped make this conversation happen

## 10630:00 - 10670:00

there's this like holy grail of

## 10670:00 - 10700:00

experiments that I think people are

## 10700:00 - 10740:00

always looking for of like one you know

## 10740:00 - 10780:00

hour of work and it creates this massive

## 10780:00 - 10835:00

result I imagine this is very rare and

## 10835:00 - 10870:00

uh don't expect this to happen I guess

## 10870:00 - 10895:00

in your experience how often do you find

## 10895:00 - 10935:00

kind of one of these gold nuggets just

## 10935:00 - 10970:00

lying around yeah so again this is a

## 10970:00 - 11020:00

topic that's uh near and dear to my

## 11020:00 - 11070:00

heart everybody wants these amazing

## 11070:00 - 11125:00

results and you know I show them in

## 11125:00 - 11175:00

chapter one in my book multiple of these

## 11175:00 - 11225:00

you know small efforts huge gain

## 11225:00 - 11265:00

but as you said they're very rare I

## 11265:00 - 11315:00

think most of the time the winnings are

## 11315:00 - 11360:00

made sort of this inch by inch and

## 11360:00 - 11400:00

there's a graph that I show in my book a

## 11400:00 - 11470:00

real graph of how Bing ads has managed

## 11470:00 - 11500:00

to improve their revenue per thousand

## 11500:00 - 11545:00

searches over time and every month you

## 11545:00 - 11575:00

can see a small Improvement and a small

## 11575:00 - 11595:00

Improvement sometimes a degradation

## 11595:00 - 11625:00

because of

## 11625:00 - 11670:00

legal reasons or other things we you

## 11670:00 - 11690:00

know there were some concern that we

## 11690:00 - 11730:00

were not marking the ads properly so you

## 11730:00 - 11770:00

have to suddenly do something that you

## 11770:00 - 11810:00

know is going to hurt Revenue but yes I

## 11810:00 - 11845:00

think most results are inch by inch you

## 11845:00 - 11905:00

improve small amounts lots of them I

## 11905:00 - 11945:00

think they're the best example that I

## 11945:00 - 11990:00

can say is a couple of them that I can

## 11990:00 - 12030:00

speak about one is at Bing the relevance

## 12030:00 - 12060:00

team

## 12060:00 - 12100:00

hundreds of people all working to

## 12100:00 - 12145:00

improve being relevant they have a a

## 12145:00 - 12180:00

metric we'll talk about oh we see the

## 12180:00 - 12210:00

overall evaluation Criterion but they

## 12210:00 - 12235:00

have a metric that their goal is to

## 12235:00 - 12270:00

improve it by two percent every year

## 12270:00 - 12310:00

it's a small amount and that two percent

## 12310:00 - 12350:00

you can see here's a point one and

## 12350:00 - 12400:00

here's a 0.15 here's a 0.2 and then they

## 12400:00 - 12450:00

add up to around two percent every year

## 12450:00 - 12485:00

which is amazing another example that I

## 12485:00 - 12530:00

am allowed to speak about uh from Airbnb

## 12530:00 - 12595:00

is the fact that we ran some

## 12595:00 - 12640:00

250 experiments

## 12640:00 - 12690:00

in my tenure there in search relevance

## 12690:00 - 12750:00

and again small improvements added up so

## 12750:00 - 12785:00

this became overall a six percent

## 12785:00 - 12825:00

Improvement to revenue you know so when

## 12825:00 - 12845:00

you think about six percent it's a big

## 12845:00 - 12890:00

number but it became it came out not of

## 12890:00 - 12945:00

one idea but many many

## 12945:00 - 12990:00

smaller ideas that each gave you a small

## 12990:00 - 13030:00

gain and in fact I again there's another

## 13030:00 - 13070:00

number I'm allowed to say of these

## 13070:00 - 13145:00

experiments 92 percent failed to improve

## 13145:00 - 13170:00

the metric that we were trying to move

## 13170:00 - 13210:00

so only eight percent of our ideas

## 13210:00 - 13260:00

actually were successful at moving the

## 13260:00 - 13300:00

key metrics there's so many threads I

## 13300:00 - 13320:00

want to follow here but let me follow

## 13320:00 - 13345:00

this one right here you just mentioned

## 13345:00 - 13395:00

of 92 percent of experiments failed is

## 13395:00 - 13425:00

that typical in your experience running

## 13425:00 - 13455:00

seeing experiments run a lot of

## 13455:00 - 13470:00

companies like what should people expect

## 13470:00 - 13505:00

when they're running experiments what

## 13505:00 - 13535:00

percentage do they expect to fill well

## 13535:00 - 13570:00

first of all I published three different

## 13570:00 - 13625:00

numbers for my career so overall at

## 13625:00 - 13650:00

Microsoft

## 13650:00 - 13720:00

about 66 two-thirds of ideas fail right

## 13720:00 - 13755:00

and don't take the 66 is accurate like

## 13755:00 - 13805:00

you know it's about two-thirds and Bing

## 13805:00 - 13840:00

which is a much more optimized domain

## 13840:00 - 13875:00

after we've been optimizing it for a

## 13875:00 - 13945:00

while the failure rate was around 85 so

## 13945:00 - 14005:00

it's harder to improve something you've

## 14005:00 - 14040:00

been optimizing for a while

## 14040:00 - 14110:00

and then at Airbnb uh this 92 number is

## 14110:00 - 14140:00

you know the highest failure rate that

## 14140:00 - 14180:00

I've observed now I've quoted other

## 14180:00 - 14215:00

sources that you know it's not that I

## 14215:00 - 14245:00

worked at groups that were particularly

## 14245:00 - 14320:00

bad uh booking uh Google ads other

## 14320:00 - 14360:00

companies published numbers there are

## 14360:00 - 14410:00

around 80 to 90 percent failure rate of

## 14410:00 - 14445:00

ideas here this is where it's important

## 14445:00 - 14480:00

of experiments it is important to

## 14480:00 - 14510:00

realize that when you have a platform

## 14510:00 - 14545:00

it's easy to get this number you look at

## 14545:00 - 14580:00

how many experiments were run and how

## 14580:00 - 14630:00

many of them launched not every

## 14630:00 - 14675:00

experiment maps to an idea so it's

## 14675:00 - 14705:00

possible that when you have an idea your

## 14705:00 - 14730:00

first implementation you start an

## 14730:00 - 14770:00

experiment boom it's egregiously bad

## 14770:00 - 14795:00

because you have a bug

## 14795:00 - 14840:00

in fact 10 percent of experiments tend

## 14840:00 - 14880:00

to be aborted on the first date

## 14880:00 - 14920:00

those are usually not that the idea is

## 14920:00 - 14950:00

bad but that there is an implementation

## 14950:00 - 14980:00

issue or something we haven't thought

## 14980:00 - 15030:00

about that forces on a board you may

## 15030:00 - 15060:00

iterate and pivot again and ultimately

## 15060:00 - 15110:00

if you do two or three or four

## 15110:00 - 15160:00

pivots or bug fixes you may get to a

## 15160:00 - 15215:00

successful launch but those numbers of

## 15215:00 - 15265:00

80 to 92 percent failure rate are of

## 15265:00 - 15290:00

experiments

## 15290:00 - 15335:00

very humbling I know that every group

## 15335:00 - 15365:00

that starts to run experiments they

## 15365:00 - 15405:00

always start off by thinking that

## 15405:00 - 15430:00

somehow they're different and their

## 15430:00 - 15450:00

successor is going to be much much

## 15450:00 - 15485:00

higher and they're all humbled you

## 15485:00 - 15520:00

mentioned that you had this uh pattern

## 15520:00 - 15565:00

of clicking a link and opening a new tab

## 15565:00 - 15590:00

is a thing that just worked at a lot of

## 15590:00 - 15640:00

different places yeah are there other

## 15640:00 - 15685:00

versions of this you collect kind of a

## 15685:00 - 15710:00

list of like here's things that often

## 15710:00 - 15755:00

work when we want to move yeah are there

## 15755:00 - 15775:00

some some you could share I don't know

## 15775:00 - 15800:00

if you have a list in your head like you

## 15800:00 - 15835:00

give you two resources uh one of them is

## 15835:00 - 15865:00

a paper that we wrote

## 15865:00 - 15925:00

called rules of thumb and what we tried

## 15925:00 - 15970:00

to do at that time at Microsoft was to

## 15970:00 - 16005:00

just look at thousands of experiments

## 16005:00 - 16055:00

that run and extract some patterns

## 16055:00 - 16100:00

and so that's that's one paper that uh

## 16100:00 - 16135:00

we can then put in the nodes perfect

## 16135:00 - 16165:00

um but there's another more more

## 16165:00 - 16215:00

accurate I would say uh resource that's

## 16215:00 - 16255:00

useful that I recommend to people and

## 16255:00 - 16305:00

it's a site called goodui.org

## 16305:00 - 16390:00

and good ui.org is exactly the site that

## 16390:00 - 16425:00

tries to do what you're saying at scale

## 16425:00 - 16490:00

so guys the name is Jacob linovsky he

## 16490:00 - 16530:00

asks people to send them results of

## 16530:00 - 16590:00

experiments and he derives he puts them

## 16590:00 - 16625:00

into patterns there's probably like 140

## 16625:00 - 16660:00

patterns I think at this point and then

## 16660:00 - 16715:00

for each pattern he says

## 16715:00 - 16765:00

um well who hasn't helped how many times

## 16765:00 - 16800:00

and by how much so you have an idea of

## 16800:00 - 16830:00

you know this worked three out of five

## 16830:00 - 16865:00

times and it was a huge win in fact you

## 16865:00 - 16905:00

can find that open a new window in there

## 16905:00 - 16945:00

I feel like you feed that into chat GPT

## 16945:00 - 16980:00

and you have basically a product manager

## 16980:00 - 17035:00

creating a roadmap uh tool in general by

## 17035:00 - 17075:00

the way this is all about a lot of that

## 17075:00 - 17115:00

is institutional memory right which is

## 17115:00 - 17175:00

can you document things well enough

## 17175:00 - 17245:00

so that the organization remembers the

## 17245:00 - 17280:00

successes and failures and learns from

## 17280:00 - 17310:00

them I think one of the mistakes that

## 17310:00 - 17340:00

some company makes is they launch a lot

## 17340:00 - 17380:00

of experiments and never go back and

## 17380:00 - 17415:00

summarize the learnings so I've actually

## 17415:00 - 17445:00

put a lot of effort in this idea of

## 17445:00 - 17480:00

institutional learning of doing the

## 17480:00 - 17520:00

quarterly meeting of the most surprising

## 17520:00 - 17560:00

experiments by the way surprising is

## 17560:00 - 17575:00

another

## 17575:00 - 17625:00

uh question to people uh often are not

## 17625:00 - 17650:00

clear about what is a surprising

## 17650:00 - 17670:00

experiment

## 17670:00 - 17720:00

to me a surprising experiment is one

## 17720:00 - 17795:00

where the estimated resolve beforehand

## 17795:00 - 17840:00

and the actual result differ by a lot so

## 17840:00 - 17875:00

that absolute value of the difference is

## 17875:00 - 17910:00

large now you can expect something to be

## 17910:00 - 17925:00

great

## 17925:00 - 17985:00

and it's flat well you learn something

## 17985:00 - 18020:00

but if you expect something to be small

## 18020:00 - 18065:00

and it turns out to be great like that

## 18065:00 - 18120:00

ad title uh promotion then you've

## 18120:00 - 18150:00

learned a lot or conversely if you

## 18150:00 - 18175:00

expected something will be small and

## 18175:00 - 18215:00

it's very negative you can learn a lot

## 18215:00 - 18255:00

by understanding why this was so

## 18255:00 - 18300:00

negative and that's interesting so we

## 18300:00 - 18340:00

focus not just on the winners but also

## 18340:00 - 18375:00

surprising losers things that people

## 18375:00 - 18420:00

thought would be a no-brainer to run and

## 18420:00 - 18445:00

then for some reason it was very

## 18445:00 - 18485:00

negative and sometimes

## 18485:00 - 18530:00

it's that negative that gives you and so

## 18530:00 - 18550:00

I'll actually you know I'm just coming

## 18550:00 - 18600:00

up with one example of that that I

## 18600:00 - 18620:00

should mention we were running this

## 18620:00 - 18655:00

experiment at Microsoft to improve the

## 18655:00 - 18690:00

windows indexer

## 18690:00 - 18735:00

and the team was able to show on offline

## 18735:00 - 18790:00

test that it does much better at

## 18790:00 - 18820:00

indexing and you know they showed some

## 18820:00 - 18860:00

relevance is higher and all these good

## 18860:00 - 18875:00

things

## 18875:00 - 18900:00

and then they ran it as an experiment

## 18900:00 - 18930:00

you know what happened

## 18930:00 - 18965:00

surprising result

## 18965:00 - 19005:00

indexing the relevance was actually high

## 19005:00 - 19040:00

but it killed the battery life

## 19040:00 - 19060:00

um

## 19060:00 - 19085:00

so here's something that comes from Left

## 19085:00 - 19125:00

Field that you didn't expect it was

## 19125:00 - 19165:00

consuming a lot more CPU on laptops it

## 19165:00 - 19205:00

was killing the laptops and therefore

## 19205:00 - 19250:00

okay we learned something let's document

## 19250:00 - 19285:00

it let's remember this

## 19285:00 - 19325:00

so that you know we now take this other

## 19325:00 - 19360:00

factor into account as we design the

## 19360:00 - 19385:00

next iteration

## 19385:00 - 19410:00

what advice do you have for people to

## 19410:00 - 19425:00

actually

## 19425:00 - 19465:00

remember these surprises you said that a

## 19465:00 - 19500:00

lot of it is institutional what do you

## 19500:00 - 19525:00

recommend people do so that they can

## 19525:00 - 19545:00

actually remember this when people leave

## 19545:00 - 19585:00

say three years later document that you

## 19585:00 - 19620:00

know right you know we had a large deck

## 19620:00 - 19675:00

internally of these successes and

## 19675:00 - 19720:00

failures and we encourage people to look

## 19720:00 - 19740:00

at them the other thing that's very

## 19740:00 - 19790:00

beneficial is just to have your whole

## 19790:00 - 19820:00

history of experiments and do some

## 19820:00 - 19875:00

ability to search by keywords right so

## 19875:00 - 19915:00

I'm I have an idea type a few keywords

## 19915:00 - 19965:00

and see if from the thousands of

## 19965:00 - 19990:00

experiments that ran and by the way

## 19990:00 - 20035:00

these are very reasonable numbers at

## 20035:00 - 20075:00

Microsoft just to let you know when I

## 20075:00 - 20125:00

left in 2019 we were on a rate of about

## 20125:00 - 20160:00

20 to 25

## 20160:00 - 20210:00

000 experiments every year so every

## 20210:00 - 20235:00

working day we were starting something

## 20235:00 - 20280:00

like a hundred new treatments

## 20280:00 - 20305:00

big numbers

## 20305:00 - 20340:00

so when you're running in a group like

## 20340:00 - 20365:00

Bing which is running thousands and

## 20365:00 - 20390:00

thousands of experiments you want to be

## 20390:00 - 20425:00

able to ask has anybody did an

## 20425:00 - 20480:00

experiment on this or this or this and

## 20480:00 - 20515:00

so that searching capability is in the

## 20515:00 - 20560:00

platform but more than that I think just

## 20560:00 - 20595:00

doing the quarterly meeting of the most

## 20595:00 - 20635:00

successful most interesting sorry not

## 20635:00 - 20665:00

just successful most interesting

## 20665:00 - 20710:00

experiments is very key and that also

## 20710:00 - 20750:00

helps the flywheel of experimentation

## 20750:00 - 20775:00

this will get segue to something I

## 20775:00 - 20800:00

wanted to touch on which is there's

## 20800:00 - 20825:00

often a

## 20825:00 - 20870:00

I guess a weariness of running too many

## 20870:00 - 20900:00

experiments and being too data driven

## 20900:00 - 20950:00

and the sense that experimentation just

## 20950:00 - 20975:00

leads you to these micro optimizations

## 20975:00 - 21025:00

and you don't really innovate and do big

## 21025:00 - 21065:00

do big things what's your perspective on

## 21065:00 - 21085:00

that and then just can you be too

## 21085:00 - 21135:00

experiment driven in your experience I'm

## 21135:00 - 21165:00

very clear that I'm a big fan of test

## 21165:00 - 21210:00

everything which is any code change that

## 21210:00 - 21245:00

you make

## 21245:00 - 21295:00

any feature that you introduce has to be

## 21295:00 - 21325:00

in some experiment because again I've

## 21325:00 - 21360:00

observed this sort of

## 21360:00 - 21400:00

surprising result that even small bug

## 21400:00 - 21445:00

fixes even small changes can sometimes

## 21445:00 - 21500:00

have surprising unexpected impact

## 21500:00 - 21540:00

and so I don't think it's possible to

## 21540:00 - 21585:00

experiment too much I think it is

## 21585:00 - 21675:00

possible to focus on incremental changes

## 21675:00 - 21735:00

because some people say well you know if

## 21735:00 - 21790:00

we only tested 17 things around this and

## 21790:00 - 21835:00

you have to think about it's not just

## 21835:00 - 21870:00

it's like in stock you need a portfolio

## 21870:00 - 21910:00

you need some experiments that are

## 21910:00 - 21935:00

incremental that move you in the

## 21935:00 - 21965:00

direction that you know you're going to

## 21965:00 - 22000:00

be successful over time if you just try

## 22000:00 - 22050:00

enough but some experiments have you

## 22050:00 - 22105:00

have to allocate sometimes to these high

## 22105:00 - 22140:00

risk High reward ideas we're going to

## 22140:00 - 22190:00

try something that's most likely to fail

## 22190:00 - 22235:00

but if it does win it's going to be a

## 22235:00 - 22270:00

home run and so you have to allocate

## 22270:00 - 22315:00

some efforts to that and you have to be

## 22315:00 - 22330:00

ready

## 22330:00 - 22375:00

to understand and agree that most will

## 22375:00 - 22410:00

fail most of these high enough it's

## 22410:00 - 22445:00

amazing how many dimes I've seen people

## 22445:00 - 22510:00

come up with new designs or a radical

## 22510:00 - 22545:00

new idea and they believe in it and

## 22545:00 - 22595:00

that's okay I'm just cautioning them all

## 22595:00 - 22615:00

the time to say hey if you go for

## 22615:00 - 22635:00

something big

## 22635:00 - 22700:00

try it out but be ready to fail eighty

## 22700:00 - 22725:00

percent of the time

## 22725:00 - 22770:00

right and one true example that again

## 22770:00 - 22810:00

I'm able to talk about because we put it

## 22810:00 - 22835:00

in my book

## 22835:00 - 22900:00

is we were at Bing

## 22900:00 - 22945:00

trying to change the landscape of search

## 22945:00 - 22985:00

and one of the ideas the Big Ideas was

## 22985:00 - 23030:00

we're going to integrate with social

## 23030:00 - 23085:00

so we hooked into the Tweeter fire hose

## 23085:00 - 23145:00

feed and we hooked it to Facebook and we

## 23145:00 - 23195:00

spent a hundred percent years

## 23195:00 - 23235:00

on this idea

## 23235:00 - 23285:00

and it failed

## 23285:00 - 23340:00

you don't see it anymore it existed for

## 23340:00 - 23375:00

about a year and a half and all the

## 23375:00 - 23430:00

experiments were just negative to flat

## 23430:00 - 23475:00

and you know it was an attempt it was

## 23475:00 - 23515:00

fair to try it I think it took us a

## 23515:00 - 23545:00

little long to fail

## 23545:00 - 23600:00

to decide if that this is a failure but

## 23600:00 - 23635:00

at least we had the data we had hundreds

## 23635:00 - 23675:00

of experiments that we tried none of

## 23675:00 - 23720:00

them were a breakthrough and I remember

## 23720:00 - 23765:00

sort of mailing uh chilu with some

## 23765:00 - 23815:00

statistics showing that you know it's

## 23815:00 - 23885:00

time to abort it's time to fail on this

## 23885:00 - 23925:00

uh and you know he decided to continue

## 23925:00 - 23950:00

more and it's a million dollar question

## 23950:00 - 23985:00

you know you continue and then maybe the

## 23985:00 - 24045:00

breakthrough will come next month or uh

## 24045:00 - 24075:00

do you abort and a few a few months

## 24075:00 - 24115:00

later we we aborted

## 24115:00 - 24160:00

that reminds me of at Netflix they tried

## 24160:00 - 24200:00

a social component that also failed at

## 24200:00 - 24235:00

Airbnb early on there was a big social

## 24235:00 - 24260:00

attempt to make like here's your friends

## 24260:00 - 24290:00

have stayed at these airbnbs completely

## 24290:00 - 24330:00

not had no impact so maybe that's one of

## 24330:00 - 24365:00

these learnings that we should talk yeah

## 24365:00 - 24415:00

this is hard this is hard and uh but

## 24415:00 - 24460:00

that's again that's the value of

## 24460:00 - 24500:00

experiments which are this Oracle that

## 24500:00 - 24530:00

gives you the data you may be excited

## 24530:00 - 24570:00

about things you might believe it's a

## 24570:00 - 24590:00

good idea

## 24590:00 - 24645:00

But ultimately the Arbiter the Oracle is

## 24645:00 - 24675:00

the controlled experiment it tells you

## 24675:00 - 24735:00

whether users are actually benefiting

## 24735:00 - 24780:00

from it whether you and the users the

## 24780:00 - 24815:00

company and the users there's obviously

## 24815:00 - 24850:00

a bit of overhead and downsides running

## 24850:00 - 24885:00

an experiment setting all up and making

## 24885:00 - 24925:00

sure you know analyzing the results is

## 24925:00 - 24960:00

there anything that you ever don't think

## 24960:00 - 24990:00

is worth a b testing

## 24990:00 - 25020:00

first of all there are some necessary

## 25020:00 - 25055:00

ingredients to a b testing and I'll just

## 25055:00 - 25105:00

say I'll write not every domain is a

## 25105:00 - 25135:00

minimal thing to be testing right you

## 25135:00 - 25175:00

can't a B test mergers and Acquisitions

## 25175:00 - 25210:00

right it's something that happens once

## 25210:00 - 25250:00

you either acquire you don't acquire so

## 25250:00 - 25275:00

you do have to have

## 25275:00 - 25310:00

some necessary ingredient you need to

## 25310:00 - 25370:00

have enough units mostly users in order

## 25370:00 - 25410:00

for the statistics to work out so yeah

## 25410:00 - 25445:00

if you're too small

## 25445:00 - 25485:00

it may be too early to a B test but what

## 25485:00 - 25550:00

I find is that in software it is so easy

## 25550:00 - 25615:00

to run a b testing and it is so easy

## 25615:00 - 25635:00

to

## 25635:00 - 25670:00

build a platform I don't say it's easy

## 25670:00 - 25695:00

to build a platform but once you build

## 25695:00 - 25720:00

the platform

## 25720:00 - 25755:00

the incremental cost of running an

## 25755:00 - 25795:00

experiment should approach zero

## 25795:00 - 25855:00

and we got to that at Microsoft where

## 25855:00 - 25890:00

after a while the cost of running

## 25890:00 - 25930:00

experiments was so low that nobody was

## 25930:00 - 25965:00

questioning the idea that everything

## 25965:00 - 26005:00

should be experimented with now I don't

## 26005:00 - 26030:00

think we were there at Airbnb for

## 26030:00 - 26060:00

example the platform at Airbnb was much

## 26060:00 - 26085:00

less mature

## 26085:00 - 26140:00

and required a lot more analysts in

## 26140:00 - 26175:00

order to interpret the results and to

## 26175:00 - 26210:00

find issues with it so I do think

## 26210:00 - 26235:00

there's this trade-off you're willing to

## 26235:00 - 26280:00

invest in the platform it is possible to

## 26280:00 - 26320:00

get the marginal cost to be close to

## 26320:00 - 26365:00

zero but when you're not there it's

## 26365:00 - 26400:00

still expensive and there are there may

## 26400:00 - 26470:00

be reasons why not to run AB thefts

## 26470:00 - 26515:00

you talked about how you may be too

## 26515:00 - 26560:00

small to run a b tests and this is a

## 26560:00 - 26590:00

constant question for startups is when

## 26590:00 - 26625:00

should we start running a b tests do you

## 26625:00 - 26650:00

have kind of a heuristic or rule of

## 26650:00 - 26670:00

thumb of just like here's a time you

## 26670:00 - 26685:00

should really start thinking about

## 26685:00 - 26720:00

running an image a million dollar

## 26720:00 - 26750:00

question that everybody asks so I

## 26750:00 - 26785:00

actually we'll put this in the notes but

## 26785:00 - 26835:00

I gave a talk last year what I called it

## 26835:00 - 26860:00

is practical defaults

## 26860:00 - 26895:00

and one of the things I show there is

## 26895:00 - 26945:00

that unless you have at least tens of

## 26945:00 - 27005:00

thousands of users

## 27005:00 - 27050:00

the math the statistics just don't work

## 27050:00 - 27085:00

out for most of the metrics that you're

## 27085:00 - 27115:00

interested in in fact you know I gave an

## 27115:00 - 27155:00

actual practical number of a retail site

## 27155:00 - 27200:00

with some conversion rate trying to

## 27200:00 - 27240:00

detect changes that are at least you

## 27240:00 - 27275:00

know five percent beneficial which is

## 27275:00 - 27300:00

something that startups should focus on

## 27300:00 - 27330:00

they shouldn't focus on the one percent

## 27330:00 - 27360:00

they should focus on the five and ten

## 27360:00 - 27400:00

percent then you need something like 200

## 27400:00 - 27440:00

000 users right so start experimenting

## 27440:00 - 27465:00

when you're in the tens of thousands of

## 27465:00 - 27505:00

users you'll be only be able to detect

## 27505:00 - 27540:00

large effects and then once you get to

## 27540:00 - 27575:00

200 000 users then the magic starts

## 27575:00 - 27610:00

happening then you can start testing a

## 27610:00 - 27680:00

lot more then you have the ability to

## 27680:00 - 27725:00

test everything and make sure that

## 27725:00 - 27760:00

you're not degrading uh and getting

## 27760:00 - 27790:00

value out of response

## 27790:00 - 27835:00

so you ask for rule of thumb 200 000

## 27835:00 - 27880:00

users you're magical below that start

## 27880:00 - 27910:00

building the culture start building the

## 27910:00 - 27945:00

platform start integrating so that as

## 27945:00 - 28000:00

you scale you you start to see the value

## 28000:00 - 28045:00

love it coming back to this kind of

## 28045:00 - 28075:00

concern people have of experimentation

## 28075:00 - 28120:00

keeps you from innovating and taking big

## 28120:00 - 28155:00

bets I know you have this framework uh

## 28155:00 - 28200:00

overall evaluation Criterion and I think

## 28200:00 - 28225:00

that helps with this can you talk a bit

## 28225:00 - 28270:00

about that the oec or the overall

## 28270:00 - 28300:00

evaluation criteria

## 28300:00 - 28335:00

is something that I think many people

## 28335:00 - 28395:00

that start to dabble in a b testing Miss

## 28395:00 - 28425:00

and the question is

## 28425:00 - 28470:00

what are you optimizing for

## 28470:00 - 28505:00

and it's a much harder question that

## 28505:00 - 28535:00

people think because

## 28535:00 - 28575:00

it's very easy to say we're going to

## 28575:00 - 28610:00

optimize for money

## 28610:00 - 28645:00

Revenue

## 28645:00 - 28675:00

but that's the wrong question because

## 28675:00 - 28725:00

you can do a lot of bad things that will

## 28725:00 - 28755:00

improve Revenue

## 28755:00 - 28795:00

so there has to be some countervailing

## 28795:00 - 28840:00

Metric that tells you how do I improve

## 28840:00 - 28875:00

Revenue without hurting the user

## 28875:00 - 28890:00

experience

## 28890:00 - 28940:00

okay so let's take a good example uh

## 28940:00 - 28965:00

with search

## 28965:00 - 29015:00

you can put more ads on the page and you

## 29015:00 - 29045:00

will make more money there's no doubt

## 29045:00 - 29085:00

about it you will make more money in the

## 29085:00 - 29110:00

short term

## 29110:00 - 29165:00

the question is what happens to the user

## 29165:00 - 29190:00

experience and how is that going to

## 29190:00 - 29235:00

impact you in the long term so we've run

## 29235:00 - 29275:00

those experiments and we were able to

## 29275:00 - 29320:00

map out you know this number of ads

## 29320:00 - 29370:00

causes this much increase to churn this

## 29370:00 - 29400:00

number of ads causes this much increase

## 29400:00 - 29455:00

to the time that users take to find a

## 29455:00 - 29495:00

successful result and we came up with an

## 29495:00 - 29535:00

oec that is based on of these metrics

## 29535:00 - 29565:00

that allows you to say okay I'm willing

## 29565:00 - 29615:00

to take this additional money if I'm not

## 29615:00 - 29650:00

hurting the user experience by more than

## 29650:00 - 29685:00

this much right so there's a trade-off

## 29685:00 - 29725:00

there one of the nice ways to phrase

## 29725:00 - 29755:00

this as a constraint optimization

## 29755:00 - 29795:00

problem I want you to increase Revenue

## 29795:00 - 29855:00

but I'm going to give you a fixed amount

## 29855:00 - 29905:00

of average real estate that you can use

## 29905:00 - 29960:00

right so you can for one query you can

## 29960:00 - 30000:00

have zero ads for another query you can

## 30000:00 - 30040:00

have three ads for a third query you can

## 30040:00 - 30085:00

have wider bigger ads I'm just going to

## 30085:00 - 30110:00

count the pixels that you take the

## 30110:00 - 30150:00

vertical pixels and

## 30150:00 - 30195:00

I will give you some budget and if you

## 30195:00 - 30225:00

can under the same

## 30225:00 - 30270:00

budget make more money you're good to go

## 30270:00 - 30320:00

right so that to me turns the problem

## 30320:00 - 30340:00

from

## 30340:00 - 30375:00

a badly defined let's just make more

## 30375:00 - 30410:00

money right any page can start

## 30410:00 - 30435:00

Plastering more ads and make more money

## 30435:00 - 30470:00

short term but that's not the goal the

## 30470:00 - 30525:00

goal is long-term growth and revenue

## 30525:00 - 30575:00

then you need to insert these other

## 30575:00 - 30605:00

criteria and what am I doing through the

## 30605:00 - 30635:00

user experience one way around it is to

## 30635:00 - 30665:00

put this constraint another one is just

## 30665:00 - 30690:00

to have these other metrics again

## 30690:00 - 30725:00

something that we did to look at the

## 30725:00 - 30760:00

user experience how long does it take

## 30760:00 - 30790:00

the user to reach a successful click

## 30790:00 - 30820:00

what percentage of sessions are

## 30820:00 - 30855:00

successful these are key metrics that

## 30855:00 - 30885:00

were part of the overall evaluation

## 30885:00 - 30925:00

Criterion that we've used

## 30925:00 - 30955:00

I can give you another example by the

## 30955:00 - 30995:00

way from you know the hotel industry or

## 30995:00 - 31035:00

Airbnb that we both worked at

## 31035:00 - 31065:00

um you can say I want to improve

## 31065:00 - 31100:00

conversion rate but you can be smarter

## 31100:00 - 31145:00

about it and say it's not just enough to

## 31145:00 - 31200:00

convert a user to buy or to pay for a

## 31200:00 - 31240:00

listing I want them to be

## 31240:00 - 31280:00

happy with it several months down the

## 31280:00 - 31315:00

road when they actually stay there right

## 31315:00 - 31360:00

so that could be part of your oec to say

## 31360:00 - 31410:00

what is the rating that they will give

## 31410:00 - 31450:00

to that

## 31450:00 - 31480:00

listing when they actually stay there

## 31480:00 - 31505:00

and that's a that causes an interesting

## 31505:00 - 31535:00

problem because you don't have this data

## 31535:00 - 31555:00

now you're gonna have it three months

## 31555:00 - 31585:00

from now when they actually stay so you

## 31585:00 - 31625:00

have to build the training set that

## 31625:00 - 31650:00

allows you to make a prediction about

## 31650:00 - 31695:00

whether this user whether Lenny is going

## 31695:00 - 31730:00

to be happy at this cheap place or where

## 31730:00 - 31750:00

they know I should offer him something

## 31750:00 - 31790:00

more expensive because Lenny likes to

## 31790:00 - 31840:00

stay at nicer places where the water

## 31840:00 - 31870:00

actually is hot and comes out of the

## 31870:00 - 31915:00

faucet that is true okay so it sounds

## 31915:00 - 31935:00

like the courts of this approach is

## 31935:00 - 31970:00

basically have a kind of a drag metric

## 31970:00 - 31995:00

that makes sure you're not hurting

## 31995:00 - 32015:00

something that's really important to the

## 32015:00 - 32050:00

business and then being very clear on

## 32050:00 - 32080:00

what's the long-term metric we care most

## 32080:00 - 32120:00

about to me the key here the key word is

## 32120:00 - 32165:00

lifetime value which is you have to

## 32165:00 - 32225:00

define the oec such that it is causally

## 32225:00 - 32260:00

predictive of the lifetime value of the

## 32260:00 - 32280:00

user

## 32280:00 - 32325:00

right and that that's what causes you to

## 32325:00 - 32365:00

think about things properly which is am

## 32365:00 - 32385:00

I doing something that just helps me

## 32385:00 - 32420:00

short term or am I doing something that

## 32420:00 - 32440:00

will help me in the long term once you

## 32440:00 - 32485:00

put that model of lifetime value people

## 32485:00 - 32525:00

say okay what about retention rates you

## 32525:00 - 32575:00

can measure that what about the time to

## 32575:00 - 32610:00

achieve a task we can measure that and

## 32610:00 - 32655:00

those are these countervailing metrics

## 32655:00 - 32710:00

that make it make the oec useful

## 32710:00 - 32745:00

and to understand these longer term

## 32745:00 - 32795:00

metrics what I'm hearing is use kind of

## 32795:00 - 32835:00

models and forecasts and predictions

## 32835:00 - 32880:00

or would you suggest sometimes use like

## 32880:00 - 32910:00

a long-term holdout or some other

## 32910:00 - 32935:00

approach like what do you find is the

## 32935:00 - 32965:00

best way to think see these well so

## 32965:00 - 33015:00

there's two ways that I like to think

## 33015:00 - 33065:00

about it one is you can run long term

## 33065:00 - 33115:00

experiments for the goal of learning

## 33115:00 - 33150:00

something so I mentioned that at Bing we

## 33150:00 - 33175:00

did run these experiments where we

## 33175:00 - 33210:00

increased the odds and decreased the

## 33210:00 - 33245:00

odds so that we will understand what

## 33245:00 - 33275:00

happens to key metrics

## 33275:00 - 33305:00

the other thing is you can just build

## 33305:00 - 33365:00

models that use some of our background

## 33365:00 - 33400:00

knowledge or use some you know data

## 33400:00 - 33425:00

science to look historical I'll give you

## 33425:00 - 33470:00

another good example of this when I came

## 33470:00 - 33520:00

to Amazon one of the teams uh that

## 33520:00 - 33585:00

reported to me was the email team that

## 33585:00 - 33615:00

it was not the transactional emails when

## 33615:00 - 33635:00

you buy something you get an email but

## 33635:00 - 33665:00

was the team that sent these

## 33665:00 - 33705:00

recommendations you know here's a book

## 33705:00 - 33750:00

by an author that you bought here's a

## 33750:00 - 33770:00

product that we recommend and the

## 33770:00 - 33795:00

question is

## 33795:00 - 33840:00

how do we give credit to that team and

## 33840:00 - 33885:00

the initial version was well whenever a

## 33885:00 - 33930:00

user comes from the email and purchases

## 33930:00 - 33960:00

something on Amazon we're gonna give

## 33960:00 - 33985:00

that email credit

## 33985:00 - 34020:00

well it turned out this had no counter

## 34020:00 - 34055:00

available metric the more emails you

## 34055:00 - 34090:00

send the more money you're going to

## 34090:00 - 34130:00

credit the theme and so that led to spam

## 34130:00 - 34175:00

literally a really interesting problem

## 34175:00 - 34230:00

the team just ramped up the number of

## 34230:00 - 34260:00

emails that they were sending out and

## 34260:00 - 34285:00

claimed to make more money in their

## 34285:00 - 34340:00

Fitness function uh improved and and

## 34340:00 - 34370:00

then so then we backed up and then we

## 34370:00 - 34405:00

said okay we can either phrase this as a

## 34405:00 - 34445:00

constraint satisfaction problem you're

## 34445:00 - 34475:00

allowed to send user and email every X

## 34475:00 - 34495:00

days

## 34495:00 - 34545:00

or which is what we ended up doing is

## 34545:00 - 34610:00

let's model the cost of spamming the

## 34610:00 - 34655:00

users okay what's that cost well when

## 34655:00 - 34715:00

they unsubscribe we can't mail them

## 34715:00 - 34750:00

okay so we did some data science study

## 34750:00 - 34780:00

on the side and we said what is the

## 34780:00 - 34820:00

value that we're losing from an

## 34820:00 - 34850:00

unsubscribe right we came up with a

## 34850:00 - 34885:00

number it's a few dollars but the point

## 34885:00 - 34910:00

was now we have this counter availity

## 34910:00 - 34940:00

metric we say here's the

## 34940:00 - 34990:00

money that we generate from the emails

## 34990:00 - 35025:00

here's the money that we're losing on

## 35025:00 - 35050:00

long-term value

## 35050:00 - 35075:00

what's the trade-off

## 35075:00 - 35120:00

and then when we started to incorporate

## 35120:00 - 35155:00

those formula more than half the

## 35155:00 - 35180:00

campaigns that were being sent were

## 35180:00 - 35220:00

negative hmm

## 35220:00 - 35285:00

okay so it was a huge Insight uh at

## 35285:00 - 35325:00

Amazon about how to send the right

## 35325:00 - 35350:00

campaigns and this LED and this is what

## 35350:00 - 35405:00

I like about these discoveries this fact

## 35405:00 - 35460:00

that we integrated the unsubscribe led

## 35460:00 - 35505:00

us to a new feature

## 35505:00 - 35570:00

to say well let's not lose their future

## 35570:00 - 35615:00

lifetime value through email when they

## 35615:00 - 35650:00

unsubscribe let's offer them by default

## 35650:00 - 35690:00

to unsubscribe from this campaign

## 35690:00 - 35730:00

so when you get an email uh you know

## 35730:00 - 35770:00

there's a new book by the author the

## 35770:00 - 35800:00

default to unsubscribe would be

## 35800:00 - 35865:00

unsubscribe me from author emails

## 35865:00 - 35910:00

and so now the the negative the

## 35910:00 - 35950:00

countervailing metric is much smaller

## 35950:00 - 35980:00

and so again this was a breakthrough in

## 35980:00 - 36020:00

our ability to send more emails and

## 36020:00 - 36050:00

understand based on what users were

## 36050:00 - 36085:00

unsubscribing from which ones are really

## 36085:00 - 36135:00

beneficial I love the surprising results

## 36135:00 - 36190:00

we all love them I mean this is this is

## 36190:00 - 36220:00

The Humbling reality and you know people

## 36220:00 - 36245:00

talk about the fact that a b testing

## 36245:00 - 36290:00

sometimes leads you to incremental I

## 36290:00 - 36330:00

actually think that many of these small

## 36330:00 - 36375:00

insights lead to fundamental insights

## 36375:00 - 36400:00

about

## 36400:00 - 36435:00

you know which areas to go some

## 36435:00 - 36470:00

strategies we should take some things we

## 36470:00 - 36490:00

should develop

## 36490:00 - 36515:00

helps a lot

## 36515:00 - 36555:00

this makes me think about how every time

## 36555:00 - 36605:00

I've done a full redesign of a product I

## 36605:00 - 36630:00

don't think ever has it ever been a

## 36630:00 - 36670:00

positive result and then the team always

## 36670:00 - 36705:00

ends up having to claw back what they

## 36705:00 - 36725:00

just hurt

## 36725:00 - 36765:00

and try to figure out what they messed

## 36765:00 - 36790:00

up is that your experience too

## 36790:00 - 36850:00

absolutely yeah in fact I I've published

## 36850:00 - 36910:00

uh some of these in in LinkedIn posts

## 36910:00 - 36965:00

showing a large set of you know big

## 36965:00 - 36995:00

launches that redesigns that

## 36995:00 - 37040:00

dramatically failed uh and it happens

## 37040:00 - 37085:00

very often so the right way to do this

## 37085:00 - 37120:00

is to say yes we want to do a redesign

## 37120:00 - 37170:00

but let's do it in steps and test on the

## 37170:00 - 37220:00

way and adjust so you don't need to

## 37220:00 - 37265:00

take 17 new changes

## 37265:00 - 37295:00

that many of them are going to fail

## 37295:00 - 37330:00

start to move incrementally in a

## 37330:00 - 37375:00

direction that you believe is beneficial

## 37375:00 - 37410:00

just on the way

## 37410:00 - 37450:00

the worst part of that those experiences

## 37450:00 - 37480:00

I find is it took like I don't know

## 37480:00 - 37505:00

three six months three to six months to

## 37505:00 - 37535:00

build it and by the time it's launched

## 37535:00 - 37565:00

it's just like we're not gonna unlaunch

## 37565:00 - 37600:00

this everyone's been working in this

## 37600:00 - 37640:00

Direction all the new features are

## 37640:00 - 37660:00

assuming this is going to work and

## 37660:00 - 37690:00

you're basically stuck right I mean this

## 37690:00 - 37720:00

is the sun cost fallacy right we

## 37720:00 - 37755:00

invested so many years in it let's

## 37755:00 - 37780:00

launch this even though it's bad for the

## 37780:00 - 37855:00

user no that's terrible yeah yeah so uh

## 37855:00 - 37895:00

this is this is the other advantage of

## 37895:00 - 37955:00

of recognizing this humble reality that

## 37955:00 - 38000:00

most ideas fail right if if you believe

## 38000:00 - 38045:00

in that statistics that I published then

## 38045:00 - 38090:00

doing 17 changes together is more likely

## 38090:00 - 38140:00

to be negative do them in smaller

## 38140:00 - 38185:00

increments learn from it's called o-fat

## 38185:00 - 38225:00

one factor at a time do one factor learn

## 38225:00 - 38270:00

from it and adjust of the 17 maybe you

## 38270:00 - 38300:00

have four good ideas

## 38300:00 - 38340:00

those are the ones that will launch and

## 38340:00 - 38390:00

be positive I generally agree with that

## 38390:00 - 38420:00

and always try to avoid a big redesign

## 38420:00 - 38455:00

but it's hard to avoid them completely

## 38455:00 - 38490:00

there's often team members that are

## 38490:00 - 38520:00

really passionate and like we just need

## 38520:00 - 38550:00

to rethink this whole experience we're

## 38550:00 - 38570:00

not going to incrementally get there

## 38570:00 - 38600:00

have you found anything effective in

## 38600:00 - 38625:00

helping people either see this

## 38625:00 - 38675:00

perspective or just making a larger bet

## 38675:00 - 38725:00

more successful by the way I I'm not

## 38725:00 - 38760:00

opposed to large

## 38760:00 - 38805:00

redesigns I try to give the team the

## 38805:00 - 38850:00

data to say look here are lots of

## 38850:00 - 38905:00

examples where big redesigns fail

## 38905:00 - 38955:00

try to decompose your redesign if you

## 38955:00 - 38985:00

can't decompose it the one factor that I

## 38985:00 - 39045:00

do a small set of factors at a time and

## 39045:00 - 39110:00

learn from these smaller changes what

## 39110:00 - 39145:00

works and what doesn't now it's also

## 39145:00 - 39180:00

possible to do a complete redesign I'm

## 39180:00 - 39220:00

just as you said yourself they be ready

## 39220:00 - 39250:00

to fail

## 39250:00 - 39285:00

right I mean do you do you really want

## 39285:00 - 39320:00

to work on something for six months or a

## 39320:00 - 39365:00

year and then run the A B test and

## 39365:00 - 39410:00

realize that you've hurt revenues or

## 39410:00 - 39445:00

other key metrics by several percentage

## 39445:00 - 39480:00

points and a data driven organization

## 39480:00 - 39515:00

will not allow you to launch what are

## 39515:00 - 39545:00

you going to write in your annual review

## 39545:00 - 39575:00

yeah but nobody ever thinks it's going

## 39575:00 - 39605:00

to fail I think no we got this or we've

## 39605:00 - 39625:00

talked to so many people but I think

## 39625:00 - 39660:00

organizations that start to run

## 39660:00 - 39705:00

experiments are humbled early on from

## 39705:00 - 39745:00

the smaller changes yeah right you're

## 39745:00 - 39790:00

right nobody I'll tell you a funny story

## 39790:00 - 39810:00

when I came

## 39810:00 - 39860:00

from Amazon to Microsoft

## 39860:00 - 39895:00

I joined the group and for one reason or

## 39895:00 - 39935:00

another that group disbanded a month

## 39935:00 - 39985:00

after I joined and so

## 39985:00 - 40020:00

people came to me and said look you just

## 40020:00 - 40045:00

joined the company you're a partner

## 40045:00 - 40090:00

level you figure out how you can help

## 40090:00 - 40120:00

Microsoft and I said I'm going to build

## 40120:00 - 40150:00

an experimentation platform because

## 40150:00 - 40180:00

nobody in Microsoft is running

## 40180:00 - 40255:00

experiments and 50 more than 50 of ideas

## 40255:00 - 40295:00

at Amazon that we tried

## 40295:00 - 40325:00

fail

## 40325:00 - 40370:00

in the classical response was we have

## 40370:00 - 40435:00

better PMS here

## 40435:00 - 40470:00

right there was this complete denial

## 40470:00 - 40525:00

that it's possible that 50 of ideas that

## 40525:00 - 40560:00

Microsoft is implementing in a

## 40560:00 - 40585:00

three-year development cycle by the way

## 40585:00 - 40625:00

this is how long it took office to

## 40625:00 - 40660:00

release it was a classical every three

## 40660:00 - 40695:00

years we release

## 40695:00 - 40760:00

and the the data came about showing that

## 40760:00 - 40810:00

uh yeah you know Bing was the first to

## 40810:00 - 40855:00

truly Implement experimentation at scale

## 40855:00 - 40880:00

and we share with the rest of the

## 40880:00 - 40935:00

companies the surprising results and so

## 40935:00 - 40965:00

when office

## 40965:00 - 41020:00

was and this was you know credited to

## 41020:00 - 41065:00

chilu and uh Sacha Nadella they were

## 41065:00 - 41115:00

ones that says Ronnie you know you

## 41115:00 - 41145:00

try to get office to run experiments

## 41145:00 - 41185:00

we'll give you the air support uh and it

## 41185:00 - 41220:00

was hard but we did it you know it was

## 41220:00 - 41260:00

it took a while but office started to

## 41260:00 - 41305:00

run experiments and they realized that

## 41305:00 - 41345:00

many of their ideas were failing he said

## 41345:00 - 41395:00

that there's a site of a failed

## 41395:00 - 41425:00

redesigns was that is that in your book

## 41425:00 - 41445:00

or is that a site that you can point

## 41445:00 - 41470:00

people to to kind of help build this

## 41470:00 - 41520:00

case but I teach this in my class but I

## 41520:00 - 41565:00

I think I've posted this on LinkedIn and

## 41565:00 - 41595:00

answered to some questions I'm happy to

## 41595:00 - 41625:00

put that in the notes okay cool we'll

## 41625:00 - 41640:00

put that in the show notes because I

## 41640:00 - 41675:00

think that's the kind of uh data that

## 41675:00 - 41705:00

often helps convince a team maybe we

## 41705:00 - 41730:00

shouldn't rethink this entire onboarding

## 41730:00 - 41760:00

flow from scratch maybe we should kind

## 41760:00 - 41805:00

of iterate towards and learn as we go

## 41805:00 - 41845:00

this episode is brought to you by EPO

## 41845:00 - 41880:00

EPO is a Next Generation a b testing

## 41880:00 - 41915:00

platform built by Airbnb alums for

## 41915:00 - 41945:00

modern growth teams companies like

## 41945:00 - 41995:00

DraftKings zapier click up twitch and

## 41995:00 - 42030:00

Cameo rely on EPO to power their

## 42030:00 - 42055:00

experiments wherever you work running

## 42055:00 - 42090:00

experiments is increasingly essential

## 42090:00 - 42125:00

but there are no commercial tools that

## 42125:00 - 42150:00

integrate with a modern grow team stack

## 42150:00 - 42175:00

this leads to wasted time building

## 42175:00 - 42215:00

internal tools or trying to run your own

## 42215:00 - 42245:00

experiments through a clunky marketing

## 42245:00 - 42275:00

tool when I was at Airbnb one of the

## 42275:00 - 42295:00

things that I loved most about working

## 42295:00 - 42330:00

there was our experimentation platform

## 42330:00 - 42370:00

where I was able to slice and dice data

## 42370:00 - 42430:00

by device types country user stage EPO

## 42430:00 - 42450:00

does all that and more delivering

## 42450:00 - 42480:00

results quickly avoiding annoying

## 42480:00 - 42510:00

prolonged analytic cycles and helping

## 42510:00 - 42545:00

you easily get to the root cause of any

## 42545:00 - 42580:00

issue you discover Apple lets you go

## 42580:00 - 42610:00

beyond basic click-through metrics and

## 42610:00 - 42645:00

instead use your North Star metrics like

## 42645:00 - 42685:00

activation retention subscription and

## 42685:00 - 42730:00

payments EPO supports tests on the front

## 42730:00 - 42775:00

end on the back end email marketing even

## 42775:00 - 42805:00

machine learning clients check out app

## 42805:00 - 42870:00

people at geteppto.com that's getepo.com

## 42870:00 - 42925:00

and 10x your experiment velocity

## 42925:00 - 42965:00

is it ever worth just going let's just

## 42965:00 - 42985:00

rethink this whole thing and just give

## 42985:00 - 43030:00

it a shot to break out of a local Minima

## 43030:00 - 43075:00

or local Maxima essentially so I think

## 43075:00 - 43105:00

what you said is fair I mean I I do want

## 43105:00 - 43140:00

to allocate some percentage of resources

## 43140:00 - 43175:00

to Big bets as you said we've been

## 43175:00 - 43220:00

optimizing this thing to Hell could be

## 43220:00 - 43255:00

completely redesigned it it's a very

## 43255:00 - 43275:00

valid

## 43275:00 - 43320:00

idea you may be able to break out of a

## 43320:00 - 43355:00

local Minima what I'm telling you is 80

## 43355:00 - 43395:00

of the time you will fail so be ready

## 43395:00 - 43430:00

for that right what people usually

## 43430:00 - 43470:00

expect is my redesign is going to work

## 43470:00 - 43530:00

no you're most likely going to fail but

## 43530:00 - 43585:00

if you do succeed it's a breakthrough

## 43585:00 - 43620:00

I like this 80 rule of thumb is that

## 43620:00 - 43645:00

just like a simple way of thinking about

## 43645:00 - 43660:00

it eighty percent

## 43660:00 - 43700:00

yeah rule of thumb and you know you've

## 43700:00 - 43750:00

had uh you know I've heard people say

## 43750:00 - 43805:00

it's 70 or or 80 but it's in that area

## 43805:00 - 43835:00

where I think you know when you talk

## 43835:00 - 43850:00

about

## 43850:00 - 43890:00

how much to invest in the known versus

## 43890:00 - 43950:00

the high risk High reward that's usually

## 43950:00 - 43975:00

the right percentage that most

## 43975:00 - 44015:00

organizations end up doing this

## 44015:00 - 44055:00

allocation right you interviewed treas I

## 44055:00 - 44100:00

think he mentioned that uh you know that

## 44100:00 - 44145:00

Google is like 70 percent

## 44145:00 - 44190:00

you know the searching ads and it's a 20

## 44190:00 - 44240:00

for some of the apps and new stuff and

## 44240:00 - 44275:00

then it's the 10 for infrastructure yeah

## 44275:00 - 44300:00

I think the the most important point

## 44300:00 - 44320:00

there is if you're not writing an

## 44320:00 - 44355:00

experiment 70 of stuff you're shipping

## 44355:00 - 44380:00

is hurting your business

## 44380:00 - 44425:00

well it's not hurting it may it's flat

## 44425:00 - 44480:00

too negative some of them are flat uh

## 44480:00 - 44510:00

and by the way flat to me if something

## 44510:00 - 44555:00

is not that Sig that's a no ship because

## 44555:00 - 44600:00

you've just introduced more code there

## 44600:00 - 44635:00

is a maintenance overhead

## 44635:00 - 44665:00

to shipping your stuff I've heard people

## 44665:00 - 44700:00

say look we already spent all this time

## 44700:00 - 44755:00

the team will be demotivated if we don't

## 44755:00 - 44805:00

ship it and no that's wrong guys right

## 44805:00 - 44840:00

you know let's make sure that we

## 44840:00 - 44870:00

understand that shipping this project

## 44870:00 - 44920:00

has no value is complicating the code

## 44920:00 - 44965:00

Base maintenance costs will go up you

## 44965:00 - 44995:00

don't ship on flat

## 44995:00 - 45020:00

unless it's a sort of a legal

## 45020:00 - 45055:00

requirement right when legal comes along

## 45055:00 - 45090:00

and says you have to do X or Y you have

## 45090:00 - 45125:00

to ship on flat or even negative and

## 45125:00 - 45155:00

that's understandable but again I think

## 45155:00 - 45180:00

that's something that a lot of people

## 45180:00 - 45215:00

make the mistake of saying legal told us

## 45215:00 - 45245:00

we have to do this therefore we're going

## 45245:00 - 45295:00

to take the hits no legal gave you a

## 45295:00 - 45340:00

framework that you have to work under

## 45340:00 - 45395:00

try three different things and ship the

## 45395:00 - 45415:00

one that hurts the least

## 45415:00 - 45465:00

I love that reminds me when Airbnb

## 45465:00 - 45500:00

launched the Rebrand even that they ran

## 45500:00 - 45535:00

as an experiment with the entire

## 45535:00 - 45560:00

homepage redesigned the new logo and all

## 45560:00 - 45585:00

that and I think there's a long-term

## 45585:00 - 45615:00

holdout even and I think it was positive

## 45615:00 - 45675:00

in the end from what I remember

## 45675:00 - 45705:00

speaking of Airbnb I want to chat about

## 45705:00 - 45740:00

Airbnb briefly I know there's and you're

## 45740:00 - 45780:00

limited in what you can share but uh

## 45780:00 - 45805:00

it's interesting that Airbnb seems to be

## 45805:00 - 45840:00

moving in this other direction where

## 45840:00 - 45885:00

it's becoming a lot more top-down Brian

## 45885:00 - 45920:00

Vision oriented and Brian's even talked

## 45920:00 - 45965:00

about how he's less motivated through an

## 45965:00 - 45990:00

experiments he doesn't want to run as

## 45990:00 - 46020:00

many experiments as they used to things

## 46020:00 - 46060:00

are going well and so you know it's hard

## 46060:00 - 46090:00

to argue with the success potentially

## 46090:00 - 46130:00

you worked there for many years you ran

## 46130:00 - 46170:00

the search team essentially I guess just

## 46170:00 - 46195:00

what was your experience like there and

## 46195:00 - 46225:00

then roughly what's your sense of how

## 46225:00 - 46260:00

things are going where it's going so as

## 46260:00 - 46295:00

you as you know I'm restricted from

## 46295:00 - 46340:00

talking about Airbnb I will say a few

## 46340:00 - 46385:00

things that I am allowed to say one is

## 46385:00 - 46455:00

in my team in search relevance

## 46455:00 - 46500:00

everything was a b tested

## 46500:00 - 46550:00

so while Brian can focus on some of the

## 46550:00 - 46600:00

design aspects that people who are

## 46600:00 - 46630:00

actually doing you know the neural

## 46630:00 - 46670:00

networks and the search

## 46670:00 - 46715:00

everything was a b tested to help so

## 46715:00 - 46745:00

nothing was launching without an A B

## 46745:00 - 46800:00

test we had targets around improving uh

## 46800:00 - 46830:00

certain metrics and everything was done

## 46830:00 - 46880:00

a B test now other teams some did some

## 46880:00 - 46930:00

did not I will say that you know when

## 46930:00 - 46970:00

you say things are going well I think we

## 46970:00 - 47005:00

don't know the counter factual I believe

## 47005:00 - 47055:00

that head Airbnb kept people like Greg

## 47055:00 - 47080:00

really which was pushing for a lot more

## 47080:00 - 47125:00

data driven and had Airbnb run more

## 47125:00 - 47155:00

experiments it would have been in a

## 47155:00 - 47195:00

better State than today but it's the

## 47195:00 - 47230:00

counter factual we don't know

## 47230:00 - 47255:00

it's a really interesting perspective

## 47255:00 - 47290:00

yeah there may be such an interesting

## 47290:00 - 47315:00

natural experiment of a way of doing

## 47315:00 - 47340:00

things differently there's like

## 47340:00 - 47385:00

de-emphasizing experiments and also they

## 47385:00 - 47425:00

turned off paid ads during covet and I

## 47425:00 - 47450:00

think I don't know where it is now but

## 47450:00 - 47485:00

it feels like it's become a much smaller

## 47485:00 - 47530:00

part of the growth strategy who knows if

## 47530:00 - 47555:00

they've ramped it up to back to where it

## 47555:00 - 47575:00

is today but I think it's going to be a

## 47575:00 - 47595:00

really interesting case study looking

## 47595:00 - 47630:00

back I don't know 5-10 years from now

## 47630:00 - 47660:00

it's a one-off experiment where it's

## 47660:00 - 47710:00

hard to assign value to some of the

## 47710:00 - 47750:00

things that Airbnb is doing I personally

## 47750:00 - 47780:00

believe it could have been a lot bigger

## 47780:00 - 47805:00

and

## 47805:00 - 47840:00

a lot more successful

## 47840:00 - 47880:00

if it had run more controlled

## 47880:00 - 47900:00

experiments

## 47900:00 - 47935:00

but I can't speak about some of those

## 47935:00 - 47985:00

that I ran and that showed uh that some

## 47985:00 - 48000:00

of the things that were initially

## 48000:00 - 48045:00

untested were actually negative and

## 48045:00 - 48065:00

could be better

## 48065:00 - 48115:00

all right mysterious

## 48115:00 - 48145:00

one more question Airbnb you were there

## 48145:00 - 48200:00

during kovid which was quite a wild time

## 48200:00 - 48225:00

for Airbnb we had sunshine on the

## 48225:00 - 48260:00

podcast talking about all the craziness

## 48260:00 - 48295:00

that went on when travel basically

## 48295:00 - 48320:00

stopped and there was a sense that

## 48320:00 - 48360:00

Airbnb was done and travel is not going

## 48360:00 - 48400:00

to happen for years and years

## 48400:00 - 48445:00

what's your take on experimentation in

## 48445:00 - 48475:00

that world where you have to really move

## 48475:00 - 48505:00

fast make crazy decisions make big

## 48505:00 - 48545:00

decisions what did you what was like

## 48545:00 - 48570:00

during that time

## 48570:00 - 48620:00

so I I think actually in a state like

## 48620:00 - 48655:00

that it's even more important to run a b

## 48655:00 - 48685:00

tests right because

## 48685:00 - 48725:00

what you want to be able to see is if

## 48725:00 - 48775:00

we're making this change is it actually

## 48775:00 - 48800:00

helping

## 48800:00 - 48840:00

in the current environment you know

## 48840:00 - 48875:00

there's this idea of external

## 48875:00 - 48910:00

generalizability is it going to work out

## 48910:00 - 48940:00

now during covet is it going to

## 48940:00 - 48980:00

generalize later on these are things

## 48980:00 - 48995:00

that you can

## 48995:00 - 49030:00

really answer with the controlled

## 49030:00 - 49060:00

experiment so sometimes it means that

## 49060:00 - 49085:00

you might have to replicate them six

## 49085:00 - 49150:00

months down when covid say uh is not as

## 49150:00 - 49200:00

impactful as it is saying that you have

## 49200:00 - 49245:00

to make decisions quickly

## 49245:00 - 49280:00

to me I'll point you to the success rate

## 49280:00 - 49325:00

like if if in peacetime you're wrong

## 49325:00 - 49375:00

two-thirds to 80 of the time why would

## 49375:00 - 49420:00

you be subtly right in Wartime right

## 49420:00 - 49470:00

until the time so uh I I don't believe

## 49470:00 - 49550:00

in the idea that because

## 49550:00 - 49595:00

bookings went down materially

## 49595:00 - 49630:00

the company should certainly you know

## 49630:00 - 49665:00

not be data driven and do things

## 49665:00 - 49725:00

differently I think if Airbnb stayed the

## 49725:00 - 49765:00

course did nothing the revenue would

## 49765:00 - 49810:00

have gone up in the same way

## 49810:00 - 49850:00

in fact if you look at one investment

## 49850:00 - 49900:00

one big investment that was done at the

## 49900:00 - 49950:00

time was online experiences and the

## 49950:00 - 49990:00

initial data wasn't very promising and I

## 49990:00 - 50020:00

think today it's a footnote

## 50020:00 - 50075:00

yeah whatever another case study for the

## 50075:00 - 50120:00

history books Airbnb experiences I want

## 50120:00 - 50140:00

to shift a little bit and talk about

## 50140:00 - 50170:00

your book which you mentioned a couple

## 50170:00 - 50200:00

of times it's called trustworthy online

## 50200:00 - 50245:00

controlled experiments and I think it's

## 50245:00 - 50285:00

basically the book on a b testing

## 50285:00 - 50330:00

let me ask you just uh what surprised

## 50330:00 - 50370:00

you most about writing this book and

## 50370:00 - 50405:00

putting it out in in the reaction to it

## 50405:00 - 50480:00

I was pleasantly surprised that

## 50480:00 - 50535:00

it sold more than what we thought and

## 50535:00 - 50570:00

more came more than what Cambridge

## 50570:00 - 50620:00

predicted so when when first we were

## 50620:00 - 50680:00

approached by Cambridge after a tutorial

## 50680:00 - 50715:00

that we did to write a book I was like I

## 50715:00 - 50745:00

don't know this is too small of an inch

## 50745:00 - 50780:00

area yeah

## 50780:00 - 50820:00

um and I uh you know they were saying so

## 50820:00 - 50850:00

you'll be able to sell a few thousand

## 50850:00 - 50905:00

copies and help the world and uh I found

## 50905:00 - 50940:00

you know my co-authors which were great

## 50940:00 - 51005:00

and you know we wrote a book that we

## 51005:00 - 51055:00

thought is not statistically oriented

## 51055:00 - 51090:00

has fewer formulas than you normally see

## 51090:00 - 51135:00

and focuses on the Practical aspects and

## 51135:00 - 51195:00

on trust which is the key the book as I

## 51195:00 - 51230:00

said you know was more successful it

## 51230:00 - 51280:00

sold over 20 000 copies in English it

## 51280:00 - 51320:00

was translated to Chinese Korean

## 51320:00 - 51380:00

Japanese and Russian and so it's it's

## 51380:00 - 51420:00

great to see that we helped the world

## 51420:00 - 51450:00

become more data driven with

## 51450:00 - 51485:00

experimentation and I'm happy because of

## 51485:00 - 51525:00

that and I was pleasantly surprised by

## 51525:00 - 51550:00

the way all proceeds from the book are

## 51550:00 - 51600:00

donated to Charities on if I'm pitching

## 51600:00 - 51645:00

the book here uh I there is no financial

## 51645:00 - 51700:00

gain for me uh from having more copies

## 51700:00 - 51730:00

sold I think we made that decision which

## 51730:00 - 51765:00

was a good decision all proceeds go with

## 51765:00 - 51800:00

the charity amazing I didn't know that

## 51800:00 - 51830:00

we'll link to the book in the show notes

## 51830:00 - 51865:00

you talked about how trust like it's

## 51865:00 - 51890:00

trust is in the title you just mentioned

## 51890:00 - 51915:00

how important trust is to

## 51915:00 - 51940:00

experimentation a lot of people talk

## 51940:00 - 51980:00

about how do I run experiments faster

## 51980:00 - 52015:00

you focus a lot on trust why is trust so

## 52015:00 - 52060:00

important in writing experiments

## 52060:00 - 52110:00

so to me the experimentation platform is

## 52110:00 - 52140:00

the safety net

## 52140:00 - 52180:00

and it's an oracle so it serves really

## 52180:00 - 52220:00

two purposes the safety net means that

## 52220:00 - 52275:00

if you launch something bad you should

## 52275:00 - 52305:00

be able to abort quickly

## 52305:00 - 52350:00

right safe deployments say velocity

## 52350:00 - 52380:00

there are some names for this but this

## 52380:00 - 52420:00

is one key value that the platform can

## 52420:00 - 52450:00

give you the other one which is the more

## 52450:00 - 52490:00

standard one is at the end of the

## 52490:00 - 52545:00

two-week experiment we will tell you

## 52545:00 - 52580:00

what happened to your key metric and do

## 52580:00 - 52620:00

many of the others surrogen and

## 52620:00 - 52665:00

debugging and guardrail metrics

## 52665:00 - 52720:00

trust builds up it's easy to lose

## 52720:00 - 52755:00

and so

## 52755:00 - 52805:00

to me it is very important that when you

## 52805:00 - 52835:00

present this and say this is science

## 52835:00 - 52880:00

this is a control experiment this is the

## 52880:00 - 52925:00

result you better believe that this is

## 52925:00 - 52990:00

trustworthy and so I focus on that a lot

## 52990:00 - 53040:00

I think it allowed us to gain the

## 53040:00 - 53080:00

organizational trust that this is really

## 53080:00 - 53130:00

and the nice thing is when we we built

## 53130:00 - 53165:00

all these checks to make sure that the

## 53165:00 - 53200:00

experiment is correct if there was

## 53200:00 - 53240:00

something wrong with it we would stop

## 53240:00 - 53275:00

and say hey something is wrong with the

## 53275:00 - 53290:00

experiment

## 53290:00 - 53330:00

and I think that's something that some

## 53330:00 - 53375:00

of the early implementations in other

## 53375:00 - 53410:00

places did not do and it was a big

## 53410:00 - 53450:00

mistake I mentioned this in my book so I

## 53450:00 - 53500:00

can mention this here optimizely in its

## 53500:00 - 53525:00

early days

## 53525:00 - 53585:00

were very statistically naive they sort

## 53585:00 - 53625:00

of said hey we're real time we can

## 53625:00 - 53675:00

compute your P values in real time uh

## 53675:00 - 53700:00

and then you can stop an experiment when

## 53700:00 - 53735:00

the p-value is statistically significant

## 53735:00 - 53800:00

that is a big mistake that inflates your

## 53800:00 - 53825:00

what's called type one error or the

## 53825:00 - 53865:00

false positive rate materially so if you

## 53865:00 - 53890:00

think you've got a five percent type one

## 53890:00 - 53935:00

error or you aim for that p-value less

## 53935:00 - 53965:00

than 0.05

## 53965:00 - 54010:00

using real-time sort of p-value

## 54010:00 - 54045:00

monitoring to optimize the offered you

## 54045:00 - 54085:00

would probably have a 30 percent

## 54085:00 - 54155:00

error rate so what this led is that

## 54155:00 - 54190:00

people that started using optimizely

## 54190:00 - 54225:00

thought that the platform was telling

## 54225:00 - 54260:00

them they're very successful but when

## 54260:00 - 54285:00

they actually started to see while it

## 54285:00 - 54315:00

told us this is positive Revenue but I

## 54315:00 - 54350:00

don't see this over time like by now we

## 54350:00 - 54385:00

should have made double their money uh

## 54385:00 - 54410:00

so their questions started to come up

## 54410:00 - 54475:00

around the trust in the platform there's

## 54475:00 - 54515:00

a very famous post that some of you

## 54515:00 - 54540:00

wrote about how optimized they almost

## 54540:00 - 54590:00

got me fired by a person who basically

## 54590:00 - 54620:00

said look I came to the organ I said we

## 54620:00 - 54650:00

have all these successes but then I said

## 54650:00 - 54700:00

something is wrong and he tells them how

## 54700:00 - 54730:00

he ran an AAA Test when there is no

## 54730:00 - 54775:00

difference between the A and the B and

## 54775:00 - 54800:00

optimizely told them that it was

## 54800:00 - 54855:00

statistically significant too many times

## 54855:00 - 54905:00

optimizely learned optimizely you know

## 54905:00 - 54940:00

several people pointed I pointed this

## 54940:00 - 54980:00

out uh in my Amazon review of the book

## 54980:00 - 55020:00

uh that the optimize the authors wrote

## 55020:00 - 55055:00

early on I said hey you're not doing the

## 55055:00 - 55095:00

statistics correctly other you know

## 55095:00 - 55130:00

Ramesh Johari at Stanford pointed this

## 55130:00 - 55155:00

out became a consultant of the company

## 55155:00 - 55220:00

and then they fixed it but to me that's

## 55220:00 - 55275:00

a very good example of

## 55275:00 - 55305:00

how to lose trust they allowed a lot of

## 55305:00 - 55345:00

trust in the market they lost all this

## 55345:00 - 55380:00

trust because they built something that

## 55380:00 - 55435:00

had very much inflated erroring

## 55435:00 - 55470:00

that is uh pretty scary to think about

## 55470:00 - 55490:00

you've been running all these

## 55490:00 - 55520:00

experiments and they weren't actually

## 55520:00 - 55585:00

telling you accurate results what are

## 55585:00 - 55635:00

signs that what you're doing may not be

## 55635:00 - 55675:00

valid uh if you're starting to run

## 55675:00 - 55705:00

experiments and then just how do you

## 55705:00 - 55750:00

avoid having that situation what kind of

## 55750:00 - 55775:00

tips can you share for people trying to

## 55775:00 - 55795:00

run experiments you know there's a whole

## 55795:00 - 55825:00

chapter of that in my book but I'll say

## 55825:00 - 55890:00

maybe one of the things that is the most

## 55890:00 - 55945:00

common occurs by far which is a sample

## 55945:00 - 55980:00

ratio mismatch now what is the sample

## 55980:00 - 56020:00

ratio mismatch if you design the

## 56020:00 - 56065:00

experiment to send 50 of users to

## 56065:00 - 56105:00

control and 50 of users per treatment

## 56105:00 - 56155:00

supposed to be a random number uh or you

## 56155:00 - 56185:00

know a hash function if you get

## 56185:00 - 56230:00

something off from 50 percent

## 56230:00 - 56275:00

it's a red flag so let's take a real

## 56275:00 - 56315:00

example uh let's say you're running an

## 56315:00 - 56345:00

experiment and it's large it's got a

## 56345:00 - 56405:00

million users and you got 50.2

## 56405:00 - 56445:00

so people say well I don't know it's not

## 56445:00 - 56480:00

going to be exactly the same as 50.2

## 56480:00 - 56525:00

reasonable or not well there's a formula

## 56525:00 - 56555:00

that you can plug in I have a

## 56555:00 - 56585:00

spreadsheet available for those that are

## 56585:00 - 56620:00

interested and you can tell here's how

## 56620:00 - 56645:00

many users are in control here's how

## 56645:00 - 56680:00

many users have in treatment my design

## 56680:00 - 56715:00

was 50 50 and it tells you the

## 56715:00 - 56740:00

probability that this could have

## 56740:00 - 56775:00

happened by chance now in a case like

## 56775:00 - 56790:00

this

## 56790:00 - 56830:00

you plug in the numbers it might tell

## 56830:00 - 56875:00

you that this should happen one in half

## 56875:00 - 56910:00

a million experiments well unless you've

## 56910:00 - 56940:00

run half a million experiment very

## 56940:00 - 56980:00

unlikely that you would get a 50.2

## 56980:00 - 57020:00

versus 49.8 split and therefore

## 57020:00 - 57055:00

something is wrong with the experiment

## 57055:00 - 57115:00

right now people I remember when we

## 57115:00 - 57155:00

first implemented this check we were

## 57155:00 - 57200:00

surprised to see how many experiments

## 57200:00 - 57235:00

suffered from this

## 57235:00 - 57275:00

right and there's a paper that was

## 57275:00 - 57335:00

published like 2018 and where we share

## 57335:00 - 57370:00

that and Microsoft even though we'd be

## 57370:00 - 57405:00

running experiments for a while is

## 57405:00 - 57450:00

around eight percent of experiments that

## 57450:00 - 57480:00

suffered from the sample ratio mismatch

## 57480:00 - 57530:00

and it's a big number I think about this

## 57530:00 - 57575:00

you're running 20 000 experiments a year

## 57575:00 - 57605:00

so many of them eight percent of them

## 57605:00 - 57645:00

are invalid and we somebody has to go

## 57645:00 - 57670:00

down and understand

## 57670:00 - 57715:00

what happened here we know that we can't

## 57715:00 - 57750:00

trust the results but why so over time

## 57750:00 - 57785:00

you begin to understand there's

## 57785:00 - 57825:00

something wrong with the pi data

## 57825:00 - 57855:00

pipeline there's something that happens

## 57855:00 - 57905:00

with Bots Bots are a very common factor

## 57905:00 - 57960:00

for causing uh sample ratio mismatch

## 57960:00 - 57975:00

um

## 57975:00 - 58015:00

so there's a whole that paper that was

## 58015:00 - 58055:00

published by my team talks about how to

## 58055:00 - 58115:00

diagnose sample ratio mismatches in the

## 58115:00 - 58175:00

last about a year and a half

## 58175:00 - 58215:00

it was amazing to see all these

## 58215:00 - 58245:00

third-party companies Implement sample

## 58245:00 - 58270:00

ratio mismatches

## 58270:00 - 58305:00

and all of them were reporting oh my God

## 58305:00 - 58335:00

you know six percent eight percent ten

## 58335:00 - 58390:00

percent uh so yeah they were it's

## 58390:00 - 58415:00

sometimes

## 58415:00 - 58450:00

fun to go back and say how many of your

## 58450:00 - 58485:00

results are in the past or invalid

## 58485:00 - 58515:00

before you had this sample ratio

## 58515:00 - 58565:00

mismatch test yeah that's frightening is

## 58565:00 - 58600:00

the most common reason this happens is

## 58600:00 - 58635:00

you're signing users in in kind of the

## 58635:00 - 58670:00

wrong place in your in your code So when

## 58670:00 - 58695:00

you say most common I think the most

## 58695:00 - 58750:00

common is Bots somehow they hit the

## 58750:00 - 58785:00

controller the treatment in different

## 58785:00 - 58815:00

proportions because you changed the

## 58815:00 - 58855:00

website the bot may fail to parse the

## 58855:00 - 58905:00

page and try to hit it more often that's

## 58905:00 - 58935:00

a classical example another one is just

## 58935:00 - 58970:00

a data pipeline

## 58970:00 - 58995:00

um we've had cases where we were trying

## 58995:00 - 59030:00

to remove bad traffic under certain

## 59030:00 - 59070:00

conditions and it was skewed because of

## 59070:00 - 59105:00

the control and treatment I've seen

## 59105:00 - 59130:00

people that start an experiment in the

## 59130:00 - 59160:00

middle of the site on some page but they

## 59160:00 - 59190:00

don't realize that some campaign is

## 59190:00 - 59230:00

pushing people uh from the side so

## 59230:00 - 59260:00

there's multiple reasons it is

## 59260:00 - 59310:00

surprising how often this happens and

## 59310:00 - 59360:00

I'll tell you a funny story which is

## 59360:00 - 59395:00

when we first added this test to the

## 59395:00 - 59430:00

platform we just put a banner saying you

## 59430:00 - 59460:00

have a sample ratio mismatch do not

## 59460:00 - 59495:00

trust these results

## 59495:00 - 59540:00

and we noticed that people

## 59540:00 - 59575:00

ignored it okay we're starting to

## 59575:00 - 59625:00

present results that had this banner and

## 59625:00 - 59670:00

so we blanked out the scorecard we put a

## 59670:00 - 59720:00

big you know red

## 59720:00 - 59765:00

can't see this result you have a sample

## 59765:00 - 59825:00

ratio mismatch click ok to expose the

## 59825:00 - 59865:00

results and why we do we need that okay

## 59865:00 - 59910:00

we need that okay button because

## 59910:00 - 59945:00

you want to be able to debug the reasons

## 59945:00 - 59970:00

and sometimes the metrics help you

## 59970:00 - 60000:00

understand why you have a sample ratio

## 60000:00 - 60035:00

mismatch so we blanked out the scorecard

## 60035:00 - 60060:00

we have this button and then we started

## 60060:00 - 60090:00

to see that people press the button is

## 60090:00 - 60115:00

still presented the results of

## 60115:00 - 60145:00

experiments with sample ratio of this

## 60145:00 - 60195:00

method so we ended up with an amazing

## 60195:00 - 60230:00

compromise which is every number in the

## 60230:00 - 60275:00

scorecard was highlighted with a red

## 60275:00 - 60300:00

line

## 60300:00 - 60350:00

so that if you took a screenshot other

## 60350:00 - 60375:00

people could tell you that a sample

## 60375:00 - 60400:00

ratio mismatch

## 60400:00 - 60440:00

freaking product managers this is this

## 60440:00 - 60475:00

is uh intuition

## 60475:00 - 60510:00

people just say wow my Instagram was

## 60510:00 - 60535:00

small therefore I can still present the

## 60535:00 - 60580:00

results people want to see success I

## 60580:00 - 60630:00

mean this is a natural bias and then we

## 60630:00 - 60660:00

have to be very conscientious and fight

## 60660:00 - 60700:00

that bias and say when something looks

## 60700:00 - 60755:00

too good to be true investigate

## 60755:00 - 60785:00

which is a great segue to something you

## 60785:00 - 60805:00

mentioned briefly uh something called

## 60805:00 - 60840:00

toyman's law yeah can you talk about

## 60840:00 - 60860:00

that

## 60860:00 - 60880:00

yeah

## 60880:00 - 60935:00

you know the the general statement is if

## 60935:00 - 60970:00

any figure that looks interesting or

## 60970:00 - 61010:00

different is usually wrong uh it was

## 61010:00 - 61055:00

first said by this person in the UK who

## 61055:00 - 61100:00

worked in radio media but I'm a big fan

## 61100:00 - 61115:00

of it

## 61115:00 - 61175:00

and uh you know my main

## 61175:00 - 61220:00

claim to people is if the result looks

## 61220:00 - 61245:00

too good to be true if you suddenly

## 61245:00 - 61280:00

moved your you know your normal movement

## 61280:00 - 61305:00

of an experiment is under one percent

## 61305:00 - 61360:00

and you suddenly have a 10 movement hold

## 61360:00 - 61410:00

the celebratory there

## 61410:00 - 61435:00

like it was just your first reaction

## 61435:00 - 61465:00

right let's take everybody to fancy

## 61465:00 - 61490:00

dinner because we just improved Revenue

## 61490:00 - 61535:00

by millions of dollars hold that dinner

## 61535:00 - 61570:00

investigate

## 61570:00 - 61605:00

see because there's a large probability

## 61605:00 - 61640:00

that something is wrong with the result

## 61640:00 - 61680:00

and I will say that nine out of ten when

## 61680:00 - 61710:00

we call out time is law it is the case

## 61710:00 - 61755:00

that we find some flaw in the experiment

## 61755:00 - 61780:00

now there are obviously outliers right

## 61780:00 - 61820:00

that first experiment that I shared

## 61820:00 - 61860:00

where we promoted that made long ad

## 61860:00 - 61900:00

titles that was successful but that was

## 61900:00 - 61945:00

replicated multiple times in double and

## 61945:00 - 61970:00

triple checked and everything was good

## 61970:00 - 62015:00

about it many other results

## 62015:00 - 62080:00

that were so big turn out to be false

## 62080:00 - 62115:00

so I'm a big I'm a big big fan of

## 62115:00 - 62145:00

Foreigner's law there's a deck I could

## 62145:00 - 62175:00

also give this in the note where I

## 62175:00 - 62215:00

shared some real examples uh of toymouth

## 62215:00 - 62225:00

love

## 62225:00 - 62270:00

amazing I want to talk about rolling

## 62270:00 - 62295:00

this out of companies and things that

## 62295:00 - 62325:00

run you run into that fail but before I

## 62325:00 - 62355:00

get to that I'd love for you to explain

## 62355:00 - 62390:00

just p-value I know that people kind of

## 62390:00 - 62410:00

misunderstand it and this might be a

## 62410:00 - 62430:00

good time just help people understand

## 62430:00 - 62460:00

what is it actually telling you that

## 62460:00 - 62510:00

p-value say 0.05 I don't know if this is

## 62510:00 - 62550:00

the right forum for explaining p-values

## 62550:00 - 62580:00

because the definition of a p-value is

## 62580:00 - 62595:00

simple

## 62595:00 - 62650:00

what it hides is very complicated so

## 62650:00 - 62700:00

I'll say one thing which is

## 62700:00 - 62770:00

many people assign one minus p-value as

## 62770:00 - 62820:00

the probability that your treatment is

## 62820:00 - 62850:00

better than control so you run an

## 62850:00 - 62890:00

experiment you got a p-value of 0.02

## 62890:00 - 62950:00

they think there's a 98 probability that

## 62950:00 - 62980:00

the treatment is better than the control

## 62980:00 - 63020:00

that is wrong

## 63020:00 - 63060:00

okay so rather than defining B values I

## 63060:00 - 63085:00

want to cautiously caution everybody

## 63085:00 - 63125:00

that the most common interpretation is

## 63125:00 - 63190:00

incorrect p-value assumes it's a

## 63190:00 - 63235:00

conditional probability or an us or

## 63235:00 - 63290:00

assumed probability it assumes that the

## 63290:00 - 63325:00

null hypothesis is true and we're

## 63325:00 - 63365:00

Computing the probability that the data

## 63365:00 - 63390:00

we're seeing

## 63390:00 - 63440:00

it matches the hypothesis this null

## 63440:00 - 63470:00

hypothesis in order to get the

## 63470:00 - 63505:00

probability that most people want

## 63505:00 - 63550:00

we need to apply Bayes Rule and invert

## 63550:00 - 63590:00

the probability from the probability of

## 63590:00 - 63620:00

the data given the hypothesis to the

## 63620:00 - 63645:00

probability the hypothesis given the

## 63645:00 - 63680:00

data for that we need an additional

## 63680:00 - 63715:00

number which is the probability the

## 63715:00 - 63770:00

prior probability that the hypothesis

## 63770:00 - 63810:00

that you're testing is uh successful or

## 63810:00 - 63875:00

not that's an unknown what we do is we

## 63875:00 - 63905:00

can take historical data and say look

## 63905:00 - 63930:00

people fail

## 63930:00 - 63960:00

two-thirds of the time or eighty percent

## 63960:00 - 63995:00

of the time and we can apply that number

## 63995:00 - 64035:00

and compute that we've done that in a

## 64035:00 - 64070:00

paper that I will give in the notes so

## 64070:00 - 64115:00

that you can assess the number that you

## 64115:00 - 64145:00

really want that what's called a false

## 64145:00 - 64180:00

positive risk so I think that's

## 64180:00 - 64225:00

something for people to internalize that

## 64225:00 - 64250:00

what you really want to look at is this

## 64250:00 - 64275:00

false positive risk which tends to be

## 64275:00 - 64310:00

much much higher than the five percent

## 64310:00 - 64355:00

that people think right so if you're I

## 64355:00 - 64395:00

think the classical example in the

## 64395:00 - 64430:00

Airbnb where the failure rate was very

## 64430:00 - 64470:00

very high is that when you get a

## 64470:00 - 64510:00

statistically significant result let me

## 64510:00 - 64555:00

actually pull the node so that I know

## 64555:00 - 64585:00

how to have the actual number if you're

## 64585:00 - 64610:00

at Airbnb

## 64610:00 - 64645:00

where the success rate of or Airbnb

## 64645:00 - 64670:00

search where the success rate is only

## 64670:00 - 64705:00

eight percent if you get a statistically

## 64705:00 - 64740:00

significant result with the p-value less

## 64740:00 - 64795:00

than 0.05 there's a 26 percent chance

## 64795:00 - 64840:00

that this is a false positive result

## 64840:00 - 64875:00

right it's not five percent

## 64875:00 - 64925:00

it's 26 so that's the number that you

## 64925:00 - 64960:00

should have in your mind and that's why

## 64960:00 - 64990:00

when I worked at Airbnb one of the

## 64990:00 - 65025:00

things we did is we said okay if you're

## 65025:00 - 65090:00

less than 0.05 but above 0.01 rerun

## 65090:00 - 65140:00

replica when you replicate you can

## 65140:00 - 65175:00

combine the two experiments and get a

## 65175:00 - 65215:00

combined p-value uh using something

## 65215:00 - 65245:00

called Fisher's method or Snuffer's

## 65245:00 - 65285:00

method and that gives you the joint

## 65285:00 - 65310:00

probability and that's usually much much

## 65310:00 - 65350:00

lower so if you get 2.05 or something

## 65350:00 - 65390:00

like that then the joint the probability

## 65390:00 - 65430:00

that you've got them is much much lower

## 65430:00 - 65465:00

wow I have never heard it described that

## 65465:00 - 65505:00

way makes me think about how like even

## 65505:00 - 65530:00

data scientists in our teams are always

## 65530:00 - 65570:00

just like this isn't perfect like we're

## 65570:00 - 65610:00

not 100 sure this experiment is positive

## 65610:00 - 65635:00

but on balance

## 65635:00 - 65665:00

if we're launching positive experiments

## 65665:00 - 65690:00

we're probably doing good things it's

## 65690:00 - 65715:00

okay if sometimes we're wrong by the way

## 65715:00 - 65740:00

it's true on balance you're probably

## 65740:00 - 65785:00

better than 50 50. but people don't

## 65785:00 - 65825:00

appreciate how much

## 65825:00 - 65890:00

that 26 that I mentioned is high and the

## 65890:00 - 65925:00

reason that I want to be sure is that I

## 65925:00 - 65955:00

think it leads to

## 65955:00 - 65980:00

this idea of the learning the

## 65980:00 - 66005:00

institutional knowledge what you want to

## 66005:00 - 66025:00

be able to say is

## 66025:00 - 66060:00

share with the organ success and so you

## 66060:00 - 66090:00

want to be really sure that you're

## 66090:00 - 66135:00

successful so by lowering the p-value by

## 66135:00 - 66185:00

forcing teams to work with the p-value

## 66185:00 - 66220:00

maybe below 0.01 and do replication on

## 66220:00 - 66250:00

hires then you can be much more

## 66250:00 - 66270:00

successful

## 66270:00 - 66310:00

and and the false positive rate will be

## 66310:00 - 66330:00

much much lower

## 66330:00 - 66365:00

fascinating and also shows the value of

## 66365:00 - 66395:00

keeping track of just what percent of

## 66395:00 - 66410:00

your experiments are failing

## 66410:00 - 66445:00

historically at the company or within

## 66445:00 - 66475:00

that specific product

## 66475:00 - 66515:00

say someone listening wants to start

## 66515:00 - 66550:00

running experiments they say they have

## 66550:00 - 66575:00

tens of thousands of users at this point

## 66575:00 - 66600:00

what would be the first couple steps

## 66600:00 - 66625:00

you'd recommend

## 66625:00 - 66665:00

well so if they have somebody in the org

## 66665:00 - 66695:00

that has previously been involved

## 66695:00 - 66730:00

experiment that's a good way to consult

## 66730:00 - 66775:00

internally uh I think the the key

## 66775:00 - 66815:00

decision is whether you want to build or

## 66815:00 - 66830:00

buy

## 66830:00 - 66875:00

there's a whole series of eight sessions

## 66875:00 - 66925:00

that I posted on LinkedIn where I

## 66925:00 - 66945:00

invited guest speakers to talk about

## 66945:00 - 66970:00

those problems or if people are

## 66970:00 - 67020:00

interested they can look at how what the

## 67020:00 - 67065:00

vendors say and what agency said about

## 67065:00 - 67105:00

build versus buy question and it's

## 67105:00 - 67160:00

usually not a zero one it's usually a

## 67160:00 - 67200:00

both you build some and you buy some and

## 67200:00 - 67225:00

it's a question of

## 67225:00 - 67295:00

do you build 10 or do you build a 90 I

## 67295:00 - 67315:00

think for people starting the third

## 67315:00 - 67335:00

party products that are available today

## 67335:00 - 67370:00

are pretty good this wasn't the case

## 67370:00 - 67400:00

when I started working so when I started

## 67400:00 - 67435:00

building running experiments at Amazon

## 67435:00 - 67475:00

we were building the platform because

## 67475:00 - 67535:00

nothing existed same at Microsoft I

## 67535:00 - 67570:00

think today there's enough

## 67570:00 - 67605:00

vendors that provide good

## 67605:00 - 67635:00

experimentation platforms that are

## 67635:00 - 67690:00

trustworthy that I would say not a good

## 67690:00 - 67715:00

way to consider

## 67715:00 - 67745:00

using one of those

## 67745:00 - 67775:00

so you're at a company where there's

## 67775:00 - 67815:00

resistance to experimentation and a b

## 67815:00 - 67840:00

testing whether it's a startup or a

## 67840:00 - 67870:00

bigger company what have you found Works

## 67870:00 - 67905:00

in helping shift that culture and how

## 67905:00 - 67935:00

long does that usually take especially

## 67935:00 - 67970:00

at a larger company my general

## 67970:00 - 68015:00

experiences with Microsoft where

## 68015:00 - 68050:00

you know we we went with this beachhead

## 68050:00 - 68085:00

of Bing we were running a few

## 68085:00 - 68115:00

experiments and then we were asked to

## 68115:00 - 68170:00

focus on being and we scaled

## 68170:00 - 68205:00

experimentation and build a platform at

## 68205:00 - 68255:00

scale at Bing once Bing was successful

## 68255:00 - 68290:00

and we were able to share all these

## 68290:00 - 68340:00

surprising results I think many many

## 68340:00 - 68365:00

more people in the company were amenable

## 68365:00 - 68395:00

and it's all it was also the case that

## 68395:00 - 68425:00

helped a lot that you know there's the

## 68425:00 - 68470:00

usual cross-pollination people from Bing

## 68470:00 - 68510:00

move out to other groups and that helped

## 68510:00 - 68535:00

these other groups say hey there's a

## 68535:00 - 68570:00

better way to build software

## 68570:00 - 68615:00

so I think if you're starting out find a

## 68615:00 - 68670:00

place find a team where experimentation

## 68670:00 - 68710:00

is easy to run and by that I mean

## 68710:00 - 68740:00

they're launching often right don't go

## 68740:00 - 68765:00

with the team that launches every six

## 68765:00 - 68800:00

months or you know office used to launch

## 68800:00 - 68835:00

every three years go with the team that

## 68835:00 - 68865:00

launches frequently you know they're

## 68865:00 - 68915:00

running on Sprints uh they launch every

## 68915:00 - 68945:00

week or two sometimes they launch that I

## 68945:00 - 68970:00

mean being used to launch multiple times

## 68970:00 - 69015:00

a day and then make sure that you

## 69015:00 - 69050:00

understand the question of the oec is it

## 69050:00 - 69090:00

clear what they're optimizing for

## 69090:00 - 69125:00

right there are some groups where you

## 69125:00 - 69160:00

can come up with a good oec some groups

## 69160:00 - 69180:00

are harder

## 69180:00 - 69215:00

you know I remember one funny example

## 69215:00 - 69290:00

was the microsoft.com website which

## 69290:00 - 69325:00

this is not MSN this is microsoft.com

## 69325:00 - 69380:00

has like multiple different

## 69380:00 - 69405:00

constituencies that are trying to

## 69405:00 - 69445:00

determine this is a support side and

## 69445:00 - 69475:00

this is some uh the ability to sell

## 69475:00 - 69530:00

software through this site and it's and

## 69530:00 - 69560:00

and warn you about

## 69560:00 - 69625:00

you know safety and updates it has so

## 69625:00 - 69665:00

many goals I remember when the team said

## 69665:00 - 69710:00

we want to run experiments and I said I

## 69710:00 - 69735:00

brought the group in and some of the

## 69735:00 - 69760:00

managers and I said do you know what

## 69760:00 - 69785:00

you're optimizing for

## 69785:00 - 69825:00

it was very funny because the the they

## 69825:00 - 69855:00

surprised me they said hey Ronnie we

## 69855:00 - 69890:00

read some of your papers we know there's

## 69890:00 - 69930:00

this term called oec

## 69930:00 - 70000:00

we decided that time on site is our oec

## 70000:00 - 70030:00

and I said wait a minute

## 70030:00 - 70060:00

some of your main goals as a support

## 70060:00 - 70100:00

site is people more spending more time

## 70100:00 - 70130:00

on the support side a good thing or a

## 70130:00 - 70160:00

bad thing and then half the room thought

## 70160:00 - 70190:00

that more time is better and half the

## 70190:00 - 70225:00

room thought that more time is worse so

## 70225:00 - 70265:00

I know he sees bad if directionally you

## 70265:00 - 70300:00

can't agree on it um

## 70300:00 - 70335:00

that's a great tip along these same

## 70335:00 - 70375:00

lines and you're a big fan of platforms

## 70375:00 - 70410:00

and building a platform to run

## 70410:00 - 70440:00

experiments versus just one-off

## 70440:00 - 70465:00

experiments can you just talk briefly

## 70465:00 - 70480:00

about that to give people a sense of

## 70480:00 - 70505:00

where they probably should be going with

## 70505:00 - 70535:00

their experimentation approach

## 70535:00 - 70575:00

yeah I mean so I think the motivation is

## 70575:00 - 70605:00

to bring the marginal cost of

## 70605:00 - 70660:00

experiments down to zero so the more you

## 70660:00 - 70700:00

self-service right go to a website set

## 70700:00 - 70740:00

up your experiment Define your targets

## 70740:00 - 70795:00

Define the metrics that you want right

## 70795:00 - 70825:00

people don't appreciate that the number

## 70825:00 - 70875:00

of metrics starts to grow really fast if

## 70875:00 - 70930:00

you're doing things right and being

## 70930:00 - 70980:00

you could Define 10

## 70980:00 - 71005:00

000 metrics that you wanted to be in

## 71005:00 - 71030:00

your scorecard

## 71030:00 - 71065:00

big numbers so it was so big and people

## 71065:00 - 71090:00

said it was computationally inefficient

## 71090:00 - 71130:00

we broke them into templates so that if

## 71130:00 - 71160:00

you were launching a UI experiment you

## 71160:00 - 71185:00

would get this set of 2000 if you're

## 71185:00 - 71215:00

doing a revenue experiment you would get

## 71215:00 - 71260:00

this set of 2000 if you're doing uh so

## 71260:00 - 71300:00

the point was

## 71300:00 - 71355:00

build a platform that can quickly

## 71355:00 - 71385:00

allow you to set up and run an

## 71385:00 - 71420:00

experiment and then analyze it I think

## 71420:00 - 71450:00

you know one of the things that I will

## 71450:00 - 71485:00

say at Airbnb is the analysis was

## 71485:00 - 71520:00

relatively weak and so lots of data

## 71520:00 - 71555:00

scientists were hired to be able to

## 71555:00 - 71580:00

compensate for the fact that the

## 71580:00 - 71600:00

platform

## 71600:00 - 71635:00

didn't do enough and so and this happens

## 71635:00 - 71675:00

in other organizations too where there's

## 71675:00 - 71695:00

this trade-off

## 71695:00 - 71730:00

like if you're building a good platform

## 71730:00 - 71775:00

invest in it so that more and more

## 71775:00 - 71805:00

automation will allow people to look at

## 71805:00 - 71860:00

the analysis without the need to involve

## 71860:00 - 71890:00

a data scientist

## 71890:00 - 71925:00

we published a paper again I'll give it

## 71925:00 - 71955:00

in the notes with this you know sort of

## 71955:00 - 72025:00

a nice Matrix of six axes and how you

## 72025:00 - 72060:00

move from crawl

## 72060:00 - 72120:00

to walk to run to fly and what you need

## 72120:00 - 72165:00

to build on those sixes so if you know

## 72165:00 - 72185:00

one of the things that I do sometimes

## 72185:00 - 72225:00

when I can solve is I go into the organ

## 72225:00 - 72250:00

and say where do you think you are on

## 72250:00 - 72305:00

these six axes and that should be the

## 72305:00 - 72330:00

guidance for what are the things you

## 72330:00 - 72350:00

need to do next

## 72350:00 - 72375:00

this is going to be the most epic show

## 72375:00 - 72430:00

notes episode we've had yet maybe a last

## 72430:00 - 72440:00

question

## 72440:00 - 72470:00

we talked about how important trust is

## 72470:00 - 72500:00

through any experiments and how even

## 72500:00 - 72525:00

though people talk about speed trust

## 72525:00 - 72560:00

ends up being most important still I

## 72560:00 - 72590:00

want to ask you about speed is there

## 72590:00 - 72615:00

anything you recommend for helping

## 72615:00 - 72640:00

people run experiments faster and get

## 72640:00 - 72670:00

results more quickly that they can

## 72670:00 - 72700:00

Implement yeah so I'll say a couple of

## 72700:00 - 72745:00

things one is if your platform

## 72745:00 - 72785:00

is good then when the experiment

## 72785:00 - 72815:00

finishes you should have a scorecard

## 72815:00 - 72890:00

soon after they made fix a day but it

## 72890:00 - 72915:00

shouldn't be then you have to wait a

## 72915:00 - 72955:00

week for the data scientist to me this

## 72955:00 - 72990:00

is the number one way to speed up things

## 72990:00 - 73035:00

now in terms of using the data

## 73035:00 - 73080:00

efficiently there are mechanisms out

## 73080:00 - 73110:00

there under the title of variance

## 73110:00 - 73170:00

reduction that help you reduce the

## 73170:00 - 73195:00

variance of metrics so that you need

## 73195:00 - 73240:00

less users so that you can get results

## 73240:00 - 73280:00

faster some examples that you might

## 73280:00 - 73310:00

think about are capping metrics so if

## 73310:00 - 73350:00

your Revenue metric is very skewed maybe

## 73350:00 - 73395:00

you say well if somebody purchased over

## 73395:00 - 73435:00

a thousand dollars let's make that a

## 73435:00 - 73470:00

thousand dollars at Airbnb one of the

## 73470:00 - 73505:00

key metrics for example is nights booked

## 73505:00 - 73555:00

well it turns out that some people book

## 73555:00 - 73600:00

tens of nights they're like an agency or

## 73600:00 - 73640:00

something hundreds of nights you may say

## 73640:00 - 73680:00

okay let's just cap this it's unlikely

## 73680:00 - 73725:00

that you know people book more than 30

## 73725:00 - 73760:00

days in a given month

## 73760:00 - 73800:00

so that various reduction technique will

## 73800:00 - 73840:00

allow you to get statistically

## 73840:00 - 73880:00

significant results faster

## 73880:00 - 73925:00

and uh a third technique is called Cupid

## 73925:00 - 73955:00

which is an article that we published

## 73955:00 - 73985:00

again I can give it into notes which

## 73985:00 - 74050:00

uses the pre-experiment data to adjust

## 74050:00 - 74080:00

the result and we can show that you get

## 74080:00 - 74120:00

the result is unbiased but with lower

## 74120:00 - 74160:00

variance and health hence it requires

## 74160:00 - 74195:00

fewer users Ronnie is there anything

## 74195:00 - 74220:00

else you want to share before we get to

## 74220:00 - 74260:00

our very exciting lightning round uh no

## 74260:00 - 74290:00

I think we've asked a lot of good

## 74290:00 - 74315:00

questions uh

## 74315:00 - 74355:00

hope people enjoy this I know they will

## 74355:00 - 74390:00

lightning round lightning craft here we

## 74390:00 - 74425:00

go I'm just gonna roll right into it

## 74425:00 - 74450:00

what are two or three books that you've

## 74450:00 - 74490:00

recommended most to other people there's

## 74490:00 - 74550:00

a fun book called calling

## 74550:00 - 74600:00

which is despite the sort of uh name

## 74600:00 - 74635:00

which is a little extreme I think for

## 74635:00 - 74680:00

the title it actually has a lot of

## 74680:00 - 74740:00

amazing insights uh that I love and it

## 74740:00 - 74785:00

sort of embodies in my opinion a lot of

## 74785:00 - 74825:00

the twyman's law of showing that things

## 74825:00 - 74865:00

that are too extreme your meter

## 74865:00 - 74895:00

should go up and say hey I don't believe

## 74895:00 - 74935:00

that so that was that's my number one

## 74935:00 - 74970:00

recommendation there's a slightly older

## 74970:00 - 75015:00

book that I love called hard facts

## 75015:00 - 75080:00

dangerous half-truths and total nonsense

## 75080:00 - 75130:00

uh by the Stanford professors from The

## 75130:00 - 75165:00

Graduate School of Business very

## 75165:00 - 75205:00

interesting to see many of the things

## 75205:00 - 75255:00

that we grew up with as sort of well

## 75255:00 - 75305:00

understood turn out to have no uh

## 75305:00 - 75330:00

justification

## 75330:00 - 75375:00

and then some with stranger book which I

## 75375:00 - 75410:00

love sort of on the verge of psychology

## 75410:00 - 75470:00

it's called mistakes were made but not

## 75470:00 - 75505:00

by me

## 75505:00 - 75560:00

uh about all the fallacies and and that

## 75560:00 - 75605:00

we fall into uh in The Humbling results

## 75605:00 - 75645:00

from that the titles of these are

## 75645:00 - 75675:00

hilarious and there's a common theme

## 75675:00 - 75715:00

across all these books

## 75715:00 - 75755:00

next question what is a favorite recent

## 75755:00 - 75780:00

movie or TV show

## 75780:00 - 75840:00

so I recently saw a short series called

## 75840:00 - 75910:00

Chernobyl on the disaster it I thought

## 75910:00 - 75945:00

it was amazingly well done uh yeah

## 75945:00 - 75980:00

highly recommend it you know based on

## 75980:00 - 76035:00

true events uh you know as usual there's

## 76035:00 - 76095:00

some freedom for the artistic uh movie

## 76095:00 - 76120:00

they it was kind of interesting at the

## 76120:00 - 76155:00

end they say this woman in the movie

## 76155:00 - 76215:00

wasn't really a woman it was a bunch of

## 76215:00 - 76255:00

30 data scientists not data scientists

## 76255:00 - 76305:00

30 scientists that in real life

## 76305:00 - 76350:00

presented all the data to the leadership

## 76350:00 - 76370:00

of what to do

## 76370:00 - 76420:00

I remember that uh fun fact I was born

## 76420:00 - 76470:00

in Odessa Ukraine which was not so far

## 76470:00 - 76510:00

from Chernobyl and I remember my dad

## 76510:00 - 76540:00

told me he had to go to work they called

## 76540:00 - 76570:00

him into work that day to clean some

## 76570:00 - 76605:00

stuff off the trees I think Ash from the

## 76605:00 - 76635:00

explosion or something it was like far

## 76635:00 - 76660:00

away where I don't think we were exposed

## 76660:00 - 76705:00

but uh but yeah we were in the vicinity

## 76705:00 - 76740:00

that's pretty scary my wife thinks I've

## 76740:00 - 76775:00

yeah every every time something's wrong

## 76775:00 - 76795:00

with me she's like oh that must be a

## 76795:00 - 76855:00

Chernobyl Chernobyl thing

## 76855:00 - 76890:00

okay next question favorite interview

## 76890:00 - 76910:00

question you like to ask people when

## 76910:00 - 76950:00

you're interviewing them so it depends

## 76950:00 - 76985:00

on the interview but I'll I'll give you

## 76985:00 - 77020:00

when I do a technical interview which I

## 77020:00 - 77075:00

do less of but uh one question that I

## 77075:00 - 77110:00

love that is amazing how many people it

## 77110:00 - 77155:00

throws away for languages like C plus

## 77155:00 - 77200:00

plus is tell me

## 77200:00 - 77265:00

what the static qualifier does

## 77265:00 - 77310:00

and for for multiple you know you could

## 77310:00 - 77330:00

do it for a variable you can do it for

## 77330:00 - 77385:00

function uh and it is just amazing that

## 77385:00 - 77415:00

I would say more than 50 percent of

## 77415:00 - 77440:00

people that interview for engineering

## 77440:00 - 77485:00

job cannot

## 77485:00 - 77525:00

get this and get it awfully wrong

## 77525:00 - 77560:00

definitely the most technical uh answer

## 77560:00 - 77605:00

to this question yeah yeah I love it

## 77605:00 - 77630:00

okay what's a favorite recent product

## 77630:00 - 77665:00

you've discovered that you love blink

## 77665:00 - 77700:00

cameras

## 77700:00 - 77795:00

so uh a bling camera is this small

## 77795:00 - 77825:00

camera you stick in two double a

## 77825:00 - 77845:00

batteries

## 77845:00 - 77885:00

and it lasts for about six months they

## 77885:00 - 77920:00

claim up to two years my experience is

## 77920:00 - 77960:00

usually about six months but it was just

## 77960:00 - 78010:00

amazing to me how you can throw these

## 78010:00 - 78040:00

things around in the yard

## 78040:00 - 78120:00

and see things that you would never know

## 78120:00 - 78160:00

otherwise you know some animals that go

## 78160:00 - 78195:00

by we had a skunk that we couldn't

## 78195:00 - 78220:00

figure out how he was entering so I

## 78220:00 - 78265:00

threw five cameras out and I saw where

## 78265:00 - 78290:00

he came in

## 78290:00 - 78350:00

um where'd he come in he came in under a

## 78350:00 - 78385:00

hole in the fence that was about this

## 78385:00 - 78450:00

High I cannot I have a video of this

## 78450:00 - 78485:00

thing just squishing underneath we never

## 78485:00 - 78515:00

would have assumed that it came from

## 78515:00 - 78565:00

there from the neighbor but yeah it's

## 78565:00 - 78595:00

these things have just changed and when

## 78595:00 - 78625:00

you're away on a trip it's always nice

## 78625:00 - 78680:00

to be able to say you know I can see my

## 78680:00 - 78730:00

house everything's okay you know one

## 78730:00 - 78785:00

point we had a false alarm and the cops

## 78785:00 - 78825:00

came in and had this amazing video of

## 78825:00 - 78875:00

how they're entering the house uh and

## 78875:00 - 78930:00

pulling the guns out

## 78930:00 - 78970:00

you gotta share that on Tick Tock that's

## 78970:00 - 79000:00

good content

## 79000:00 - 79050:00

wow okay done cameras we'll set those up

## 79050:00 - 79095:00

in my house ASAP yes

## 79095:00 - 79125:00

what is something relatively minor

## 79125:00 - 79150:00

you've changed in the way your teams

## 79150:00 - 79185:00

develop product that has had a big

## 79185:00 - 79225:00

impact on their ability to execute

## 79225:00 - 79250:00

I think this is something that I learned

## 79250:00 - 79275:00

at Amazon

## 79275:00 - 79330:00

which is a structured narrative

## 79330:00 - 79375:00

so Amazon has some variance of this

## 79375:00 - 79405:00

which sometimes but then they go by The

## 79405:00 - 79425:00

Neighborhood six page or something but

## 79425:00 - 79465:00

when I was at Amazon I still remember

## 79465:00 - 79500:00

that email from Jeff which is

## 79500:00 - 79550:00

no more PowerPoint I'm gonna force you

## 79550:00 - 79575:00

to write a narrative

## 79575:00 - 79615:00

I took that the heart and many of the

## 79615:00 - 79650:00

features that

## 79650:00 - 79690:00

the team presented instead of a

## 79690:00 - 79725:00

PowerPoint you start off with a

## 79725:00 - 79765:00

structured document that tells you what

## 79765:00 - 79785:00

you need the questions you need to

## 79785:00 - 79820:00

answer for your idea and then review

## 79820:00 - 79850:00

them as a team

## 79850:00 - 79880:00

and Amazon these were like paper base

## 79880:00 - 79910:00

now it's all

## 79910:00 - 79940:00

you know based on word or Google Docs

## 79940:00 - 79965:00

where people comment

## 79965:00 - 80005:00

and I think the impact of that was

## 80005:00 - 80065:00

amazing I think the ability to give

## 80065:00 - 80110:00

people honest feedback and have them

## 80110:00 - 80140:00

appreciate and have it stay after the

## 80140:00 - 80185:00

meeting was you know in these notes on

## 80185:00 - 80220:00

the document just amazing

## 80220:00 - 80255:00

final question have you ever run an A B

## 80255:00 - 80290:00

test on your life either your dating

## 80290:00 - 80325:00

life your family or kids and if so what

## 80325:00 - 80365:00

did you try so there aren't enough units

## 80365:00 - 80400:00

remember I said unique 10 000 or

## 80400:00 - 80445:00

something you run through a B test I do

## 80445:00 - 80485:00

I will say a couple of things one is I

## 80485:00 - 80530:00

try to emphasize to my family and

## 80530:00 - 80565:00

friends and everybody this idea called

## 80565:00 - 80615:00

the hierarchy of evidence when you read

## 80615:00 - 80650:00

something

## 80650:00 - 80705:00

there's a hierarchy of trust levels if

## 80705:00 - 80755:00

something is anecdotal don't trust it if

## 80755:00 - 80780:00

there was an experiment it was

## 80780:00 - 80825:00

observational give it some bit of trust

## 80825:00 - 80865:00

as you get more up and up to a natural

## 80865:00 - 80895:00

experiment and control experiments and

## 80895:00 - 80940:00

multiple control experiments your trust

## 80940:00 - 80980:00

levels should go up so I think that

## 80980:00 - 81025:00

that's a very important thing that a lot

## 81025:00 - 81050:00

of people miss when they see something

## 81050:00 - 81110:00

in the news is where does it come from I

## 81110:00 - 81165:00

have a talk that I I've shared

## 81165:00 - 81200:00

of all these observational studies that

## 81200:00 - 81250:00

people made that were published and then

## 81250:00 - 81285:00

somehow a control experiment was run

## 81285:00 - 81310:00

later on and proved that it was

## 81310:00 - 81355:00

directionally incorrect

## 81355:00 - 81400:00

so uh I think there's a lot to learn

## 81400:00 - 81425:00

about this idea of the hierarchy of

## 81425:00 - 81450:00

evidence and share it with our family

## 81450:00 - 81500:00

and kids and and friends and there's

## 81500:00 - 81520:00

another I think there's a book that's

## 81520:00 - 81560:00

based on this like how to read a book

## 81560:00 - 81610:00

well Ronnie the experiment of us

## 81610:00 - 81655:00

recording a podcast I think is a hundred

## 81655:00 - 81720:00

percent positive p-value 0.0 thank you

## 81720:00 - 81755:00

so much for being here thank you so much

## 81755:00 - 81785:00

for inviting me in for great questions

## 81785:00 - 81825:00

amazing I appreciate that uh two final

## 81825:00 - 81850:00

questions where can folks finding online

## 81850:00 - 81880:00

if they want to reach out and is there

## 81880:00 - 81915:00

anything that listeners can do for you

## 81915:00 - 81955:00

finding me online is easy it's LinkedIn

## 81955:00 - 82005:00

and what can people do for me you know

## 82005:00 - 82055:00

understand the idea of control

## 82055:00 - 82100:00

experiments there's a mechanism to make

## 82100:00 - 82135:00

the right data driven decisions use

## 82135:00 - 82150:00

science

## 82150:00 - 82205:00

uh you know learn more by reading my

## 82205:00 - 82235:00

book if you want again all proceeds go

## 82235:00 - 82280:00

to charity and if you want to learn more

## 82280:00 - 82320:00

there's a class that I teach every

## 82320:00 - 82365:00

quarter on Maven we'll put in the notes

## 82365:00 - 82420:00

uh how to find it and uh some discount

## 82420:00 - 82460:00

for people who managed to stay all the

## 82460:00 - 82515:00

way to the end of this uh podcast yeah

## 82515:00 - 82540:00

that's awesome I'll include that at the

## 82540:00 - 82565:00

top so people don't miss it so there's

## 82565:00 - 82595:00

gonna be a code to get a discount on

## 82595:00 - 82630:00

your course Ronnie thank you again so

## 82630:00 - 82650:00

much for being here this was amazing

## 82650:00 - 82690:00

thank you so much bye everyone

## 82690:00 - 82715:00

[Music]

## 82715:00 - 82750:00

thank you so much for listening if you

## 82750:00 - 82780:00

found this valuable you can subscribe to

## 82780:00 - 82820:00

the show on Apple podcast Spotify or

## 82820:00 - 82865:00

your favorite podcast app also please

## 82865:00 - 82895:00

consider giving us a rating or leaving a

## 82895:00 - 82925:00

review as that really helps other

## 82925:00 - 82965:00

listeners find the podcast you can find

## 82965:00 - 82995:00

all past episodes or learn more about

## 82995:00 - 83045:00

the show at lennyspodcast.com

## 83045:00+

see you in the next episode

