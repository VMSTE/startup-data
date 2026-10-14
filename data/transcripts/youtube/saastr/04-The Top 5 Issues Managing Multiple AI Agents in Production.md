---
source: https://www.youtube.com/watch?v=kL5cO-Sxv00
title: The Top 5 Issues Managing Multiple AI Agents in Production
author: SaaStr AI
date: 2026-03-04
views: 8048
description: >-
  Managing 1-2 AI agents? Easy. Managing 20+? That's a different game entirely.


  After 9+ months running nearly 30 AI agents in production at SaaStr, our CEO,
  Jason Lemkin, and Chief AI Officer, Amelia Lerutte, learned what actually
  breaks at scale, and nobody's talking about it. This isn't about deployment
  tips or vendor selection. This is about the brutal realities that only emerge
  when you're juggling 20+ agents generating $1M+ in revenue.


  🔥 THE 5 ISSUES WE COVER:

  1. The Context Switching Tax (2:15)

  Managing 20 agents = managing 20 employees who all speak different languages.
  Each needs daily 1-on-1s. The math doesn't work: 20 agents × 20 min = 6.7
  hours/day, but you only have 3-4 hours of capacity.


  2. The New Agent Blackout Period (12:40)

  Every new agent costs you 2 weeks of chaos. While onboarding Monaco, Artisan's
  response rates dropped 3% because contacts went stale. You can only safely add
  1.5 agents per month max - any faster and you're running in place.


  3. The AI Agent Succession Planning Crisis (23:15)

  You're the single point of failure for $1M+ of AI-driven revenue. Only 2-5% of
  your team could manage these agents. What happens when you get hit by a bus?
  Go on vacation? Leave the company?


  4. The Agent as Truth-Teller (32:50)

  "You're 56% behind target. Block 3 hours tomorrow or adjust your goal." Your
  agents don't sugarcoat. They have all the data, and they'll roast you every
  day. Is that helpful or demoralizing? We still don't know.


  5. The Compliance/Security Drift (41:20)

  You ran a security audit in January. It's now February. You've shipped 40
  updates. Did you re-audit? Probably not. Your security posture degrades in
  real time as you iterate at AI speed.


  BONUS #6: You Lose Patience with Humans (48:30)

  After managing agents that respond instantly and work 24/7, humans feel
  painfully slow. "What do you mean you don't know the answer? My agent knows
  instantly." This makes you worse at managing actual people.


  ⚡ KEY TAKEAWAYS:

  → There is no orchestration layer yet. You're manually checking 20 different
  dashboards daily

  → Your agents can't talk to each other. Salesforce is the only place they meet

  → You need a "Chief Agent Officer". Someone technical enough to manage the
  stack

  → The math: Can only add ~1.5 agents/month max, need 10-15 hours/week for
  management

  → ROI calculation is simple: Which agent touched which lead? Did it close?
  That's it.


  💰 THE NUMBERS:

  → 20+ agents in production

  → $1M+ in closed revenue from agents

  → 30% of Chief AI Officer time spent on agent management

  → 2 weeks minimum to onboard each new agent

  → 6.7 hours needed daily to properly manage 20 agents (impossible)


  🛠️ AGENTS WE USE:

  Sales/Outbound: Artisan, Monaco, AgentForce

  Inbound: Qualified

  RevOps: Momentum

  Marketing: 10K (custom AI VPM), Gamma, Opus Pro

  Internal: SaaStr Sponsors portal (custom vibe-coded)


  📊 REALITY CHECK:


  "We're at the max. We did add Monaco, which we love, but only because it's
  disruptive, only because it fills a gap. We would not add another GTM agent.
  We're just overloaded." - Jason Lemkin


  This is SaaStr. We're AI-first. We have a Chief AI Officer. We've been doing
  this for 9 months.


  And we're at the max at 20 agents.


  What does that tell you about scaling to 30? 40? 50?


  🔗 RESOURCES:


  → SaaStr.ai/agents - Full agent directory and how we use each one

  → SaaStr Annual 2026 (May 12-14) - SaaStr Deploy day: Build your own agents
  hands-on


  🎤 SPEAKERS:


  Amelia Lerutte - Chief AI Officer, SaaStr

  Jason Lemkin - Founder & CEO, SaaStr


  ---


  TIMESTAMPS:

  0:00 - Intro: The Reality of 30 Agents

  2:15 - Issue #1: Context Switching Tax

  12:40 - Issue #2: New Agent Blackout Period

  23:15 - Issue #3: Succession Planning Crisis

  32:50 - Issue #4: Agent as Truth-Teller

  41:20 - Issue #5: Compliance/Security Drift

  48:30 - Bonus #6: Losing Patience with Humans

  56:10 - Q&A: Orchestration layers, scaling teams, ROI calculation

  1:02:45 - Why marketing automation agents don't exist yet

  1:06:30 - SaaStr Annual 2026 + Deploy Day


  The uncomfortable truth: Managing 20+ agents makes you worse at managing
  humans. You get used to instant execution, no pushback, 24/7 availability, and
  perfect memory. Then humans feel... inefficient.


  Maybe the future isn't "how many agents can I add" but "how deep can I go with
  the ones I have."


  ---


  #AIAgents #SaaS #GoToMarket #AIAutomation #ProductivityTools #B2BSaaS
  #SalesAutomation #MarketingAutomation #AgenticAI #StartupTech


  ---


  Subscribe for weekly AI deployment content from the trenches. No theory. No
  vendor pitches. Just what actually works (and breaks) at scale.


  👉 SaaStr Annual 2026: saastrannual.com

  👉 Full agent list: saastr.ai/agents


  ----------------------
tags:
  - saas
  - saastr
  - software as a service
  - startups saas startups
  - tech startups
  - startup company
  - start up business
  - starting a business
  - entrepreneur ideas
  - successful entrepreneurs
  - becoming an entrepreneur
  - how to be a successful tech entrepreneur
extraction_method: youtube-transcript
grabbed_at: 2026-04-03T10:54:32.805Z
---

# The Top 5 Issues Managing Multiple AI Agents in Production

## 00:00 - 55:00

Welcome to the official Saster Podcast

## 55:00 - 85:00

where you can hear some of the best SAS

## 85:00 - 115:00

[music] speakers. This is where the

## 115:00 - 150:00

cloud meets

## 150:00 - 185:00

up today on [music] the Saster Podcast.

## 185:00 - 230:00

>> How like how do you scale past this N

## 230:00 - 280:00

equals 1. And I don't think there's a

## 280:00 - 320:00

good answer for this today. There is no

## 320:00 - 360:00

like crazy good agent that can manage

## 360:00 - 400:00

all the other agents on its own today.

## 400:00 - 425:00

There doesn't exist, right? I think

## 425:00 - 465:00

there will be, but there's not one

## 465:00 - 500:00

today. And so I think even with all the

## 500:00 - 565:00

help we get, it's this is just a huge

## 565:00 - 600:00

issue that I think the market has not

## 600:00 - 625:00

realized yet.

## 625:00 - 655:00

>> Yeah. I mean I mean obviously we're

## 655:00 - 685:00

extreme and tiny. I mean if you left for

## 685:00 - 705:00

some reason we would we would have to

## 705:00 - 745:00

cease using our agents. There there's no

## 745:00 - 780:00

there's no there's no plan B. We're just

## 780:00 - 810:00

all learning that you need some sort of

## 810:00 - 845:00

chief agent officer, right? Whatever you

## 845:00 - 865:00

want to call them. Someone that can

## 865:00 - 900:00

manage all of your agents that I think

## 900:00 - 940:00

needs to be a bit of a nerd, a tech

## 940:00 - 970:00

nerd. ideally a bit of a marketing nerd

## 970:00 - 1005:00

because a lot of these products are if

## 1005:00 - 1025:00

you can manage [music] a complex

## 1025:00 - 1055:00

marketing automation tool, you can

## 1055:00 - 1075:00

probably manage most of the products

## 1075:00 - 1130:00

that we use. You can hack the rest.

## 1130:00 - 1145:00

But, you know, thinking through it, I

## 1145:00 - 1165:00

mean, this is this is tapped and

## 1165:00 - 1190:00

obvious, but I think if you [music]

## 1190:00 - 1215:00

actually find the person that can deploy

## 1215:00 - 1255:00

these agents for real that actually can

## 1255:00 - 1290:00

be success, just like a lot of these

## 1290:00 - 1320:00

functions, but immediately they should

## 1320:00 - 1350:00

recruit. You need to recruit somebody

## 1350:00 - 1375:00

else on their team [music] and and

## 1375:00 - 1395:00

divide and conquer and make sure you

## 1395:00 - 1470:00

have two

## 1470:00 - 1505:00

Hey Sasser, imagine having agents for

## 1505:00 - 1540:00

every support tab. One that triages

## 1540:00 - 1565:00

tickets, [music] another that catches

## 1565:00 - 1605:00

duplicates, one that spots churn. That'd

## 1605:00 - 1640:00

be pretty mainly, right? Happy Fox just

## 1640:00 - 1670:00

made it real with autopilot. These

## 1670:00 - 1710:00

pre-built AI agents deploy in about 60

## 1710:00 - 1745:00

[music] seconds and run for as low as 2

## 1745:00 - 1785:00

cents per successful action. All of it

## 1785:00 - 1825:00

sits inside the Happy Fox omni channel

## 1825:00 - 1870:00

AI first support stack, chatbot,

## 1870:00 - 1910:00

co-pilot, and autopilot working as one.

## 1910:00 - 1920:00

Check them out at [music]

## 1920:00 - 2005:00

happyfox.com/saster.

## 2005:00 - 2045:00

>> Hey everybody, Saster Annual will be

## 2045:00 - 2095:00

back May 2026, the world's largest SAS

## 2095:00 - 2130:00

and AI gathering for [music] executives.

## 2130:00 - 2165:00

Just this last May, we hosted 10,000

## 2165:00 - 2210:00

attendees with 68 VP level and above

## 2210:00 - 2240:00

attendees, 36% [music]

## 2240:00 - 2290:00

CEOs and founders, and 25% were AI first

## 2290:00 - 2325:00

professionals. It's the very best of S

## 2325:00 - 2355:00

tier attendees and decision makers that

## 2355:00 - 2400:00

[music] come to SAS annual and AI summit

## 2400:00 - 2420:00

each and every year. But here's the

## 2420:00 - 2450:00

reality, folks. The longer you wait, the

## 2450:00 - 2480:00

higher ticket prices get. They're cheap

## 2480:00 - 2510:00

now. They're cheap. So just get them

## 2510:00 - 2545:00

early. Lock in your spot today. Use my

## 2545:00 - 2595:00

code Jason 100 for exclusive savings.

## 2595:00 - 2645:00

Get your tickets at podcast.sanual.com

## 2645:00 - 2680:00

or just use code Jason100 when you check

## 2680:00 - 2710:00

out. See you there. Saster annual and

## 2710:00 - 2760:00

AAImit 2026. [music] It will rock.

## 2760:00 - 2800:00

>> Hello everybody. excited to be here with

## 2800:00 - 2860:00

all of you and your agents here today.

## 2860:00 - 2885:00

We thought we would do a fun one since

## 2885:00 - 2935:00

we have 20 actually almost 30 I think

## 2935:00 - 2990:00

when I counted it this morning. Agents

## 2990:00 - 3025:00

and Vivecoded tools and apps in

## 3025:00 - 3050:00

production.

## 3050:00 - 3085:00

We wanted to talk about our top five

## 3085:00 - 3120:00

issues. Once you start to manage these

## 3120:00 - 3150:00

multiple agents in production, what does

## 3150:00 - 3170:00

that really mean? What are maybe the

## 3170:00 - 3200:00

nuances folks haven't thought of if

## 3200:00 - 3220:00

you've only deployed like one or two

## 3220:00 - 3250:00

agents? kind of like what breaks when

## 3250:00 - 3300:00

you have multiple agents at a high

## 3300:00 - 3360:00

volume and high scale. Okay, as always,

## 3360:00 - 3390:00

I always like to have this as our first

## 3390:00 - 3420:00

slide because folks go back to it and

## 3420:00 - 3460:00

reference it. So, for any of the agents

## 3460:00 - 3495:00

and tools we'll reference today, you can

## 3495:00 - 3530:00

go to saster.ai/

## 3530:00 - 3555:00

aents, that's where we put our agent

## 3555:00 - 3580:00

directory. We actually have a few more

## 3580:00 - 3620:00

we need to add to it, but this is our

## 3620:00 - 3655:00

depository of all the agents and some

## 3655:00 - 3690:00

community agents that we use across the

## 3690:00 - 3710:00

board. A lot of the things we'll talk

## 3710:00 - 3745:00

about today are linked there if you're

## 3745:00 - 3785:00

looking for the links. So, as always,

## 3785:00 - 3820:00

keep that in mind. Okay, top five

## 3820:00 - 3845:00

issues. I'll summarize them here and

## 3845:00 - 3880:00

then I'll I'll go into them in depth. I

## 3880:00 - 3900:00

think there's a lot we've learned in

## 3900:00 - 3955:00

like the now 9/10 months of managing

## 3955:00 - 4000:00

multiple AI agents in production between

## 4000:00 - 4045:00

Jason and myself. So, I kind of narrowed

## 4045:00 - 4075:00

it down to the top five things and then

## 4075:00 - 4145:00

I have a bonus. So I would say issue

## 4145:00 - 4165:00

number one and this is maybe force

## 4165:00 - 4210:00

ranked is context switching becomes

## 4210:00 - 4245:00

extremely difficult when you have 20

## 4245:00 - 4285:00

plus agents. They don't all function the

## 4285:00 - 4315:00

same way. If you guys saw the article

## 4315:00 - 4350:00

that Jason did over the weekend about

## 4350:00 - 4395:00

like how we use Salesforce and Agent

## 4395:00 - 4420:00

Force is kind of like the backbone and

## 4420:00 - 4450:00

the plumbing for a lot of these agents.

## 4450:00 - 4480:00

You know there's a reason we do that and

## 4480:00 - 4505:00

that's because a lot of these agents

## 4505:00 - 4545:00

function somewhat independently. Some of

## 4545:00 - 4570:00

them push back to Salesforce, some of

## 4570:00 - 4605:00

them don't. Some of them talk to Claude,

## 4605:00 - 4645:00

some of them don't. And so it's a bit of

## 4645:00 - 4670:00

a hodgepodge today. Like that's the

## 4670:00 - 4710:00

reality of managing all these AI agents

## 4710:00 - 4735:00

and productions. They all speak slightly

## 4735:00 - 4780:00

different languages. They all ingest

## 4780:00 - 4810:00

context very similarly, but still

## 4810:00 - 4845:00

different ways.

## 4845:00 - 4870:00

They all have slightly different

## 4870:00 - 4925:00

personalities. I will say these agents

## 4925:00 - 4950:00

and they all kind of want different

## 4950:00 - 4990:00

things from you. And so I think context

## 4990:00 - 5035:00

switching just like in as a human brain

## 5035:00 - 5080:00

keeping up with the agents becomes kind

## 5080:00 - 5140:00

of difficult on a day-to-day basis.

## 5140:00 - 5170:00

Number two, I think the the new agent

## 5170:00 - 5200:00

blackout period for again for those of

## 5200:00 - 5220:00

you who have maybe added a couple

## 5220:00 - 5245:00

agents, but now you're you're getting

## 5245:00 - 5300:00

into the high volume of multiple agents.

## 5300:00 - 5330:00

For us at least, even with the help we

## 5330:00 - 5350:00

get from our vendors, which we'll talk

## 5350:00 - 5395:00

about a bit, even with the help we get,

## 5395:00 - 5440:00

like I feel like every new agent costs

## 5440:00 - 5475:00

us at least 2 weeks of what I call

## 5475:00 - 5505:00

either a blackout period and somewhat

## 5505:00 - 5540:00

chaotic of like I kind of have to ignore

## 5540:00 - 5585:00

the other agents anytime I bring on a

## 5585:00 - 5615:00

new agent, which as you might imagine,

## 5615:00 - 5655:00

since they need daily

## 5655:00 - 5695:00

review, it's kind of rough on the entire

## 5695:00 - 5720:00

stack. It's just like this cascading

## 5720:00 - 5770:00

waterfall of effects that happen every

## 5770:00 - 5815:00

time we add a new agent of which I

## 5815:00 - 5840:00

famously said on LinkedIn I was not

## 5840:00 - 5860:00

going to add anymore and then I added

## 5860:00 - 5890:00

two more in the last two weeks. So there

## 5890:00 - 5950:00

goes that and and I can share some

## 5950:00 - 5975:00

reasons why if you didn't watch the one

## 5975:00 - 6020:00

from last week. Okay, the other one I

## 6020:00 - 6055:00

would say number three which is a huge

## 6055:00 - 6100:00

issue actually maybe it's number one but

## 6100:00 - 6145:00

the AI what we call the AI agent

## 6145:00 - 6180:00

succession planning crisis. I actually

## 6180:00 - 6215:00

asked our agents today what they would

## 6215:00 - 6250:00

do if I had to pass them over and the

## 6250:00 - 6265:00

answers were actually a little bit

## 6265:00 - 6315:00

surprising.

## 6315:00 - 6360:00

You'll see why when I dig into that one.

## 6360:00 - 6390:00

The fourth one I would say the agent as

## 6390:00 - 6440:00

the truth teller. One of my agents more

## 6440:00 - 6470:00

famously than the other, the 10K agent

## 6470:00 - 6515:00

roasts me all the time.

## 6515:00 - 6540:00

Every day cuz I talk to it every day.

## 6540:00 - 6565:00

Like that's the first one I talk to each

## 6565:00 - 6610:00

morning. It will literally roast me all

## 6610:00 - 6640:00

the time. which is funny because when I

## 6640:00 - 6665:00

pushed it on that for this webinar, it

## 6665:00 - 6690:00

said it wasn't roasting me. So

## 6690:00 - 6730:00

[laughter] that's that's an interesting

## 6730:00 - 6765:00

learning too where it said it was being

## 6765:00 - 6790:00

helpful and I thought it was roasting

## 6790:00 - 6840:00

me. And the last but not least before we

## 6840:00 - 6865:00

get into the bonus one, I think there is

## 6865:00 - 6895:00

a lot of you know compliance and

## 6895:00 - 6940:00

security maybe not issues but just

## 6940:00 - 6965:00

nuances and maintenance that people

## 6965:00 - 7005:00

don't talk about.

## 7005:00 - 7030:00

That is a real problem right? I think

## 7030:00 - 7065:00

that's why

## 7065:00 - 7110:00

most high, you know, highly secure, like

## 7110:00 - 7130:00

I'm not going to vibe code to Salesforce

## 7130:00 - 7150:00

for a lot of reasons, but part of the

## 7150:00 - 7180:00

reason is because Salesforce is secure.

## 7180:00 - 7205:00

Like that data is there. We've got 10

## 7205:00 - 7230:00

years of data there. It's the plumbing

## 7230:00 - 7270:00

for a lot of our other agents, but also

## 7270:00 - 7295:00

it's, you know, they've thought about

## 7295:00 - 7330:00

all these things like Sock 2 and ISOs

## 7330:00 - 7375:00

endlessly so that I don't have to. So,

## 7375:00 - 7400:00

that alone is like kind of worth it for

## 7400:00 - 7445:00

us to use it and keep using that. But I

## 7445:00 - 7460:00

think there's other issues when you

## 7460:00 - 7485:00

start to vibe code your own apps and

## 7485:00 - 7535:00

agents that most folks probably haven't

## 7535:00 - 7570:00

thought about because you you're so used

## 7570:00 - 7600:00

to these other tools like a Salesforce

## 7600:00 - 7630:00

doing it for you that even myself I

## 7630:00 - 7655:00

didn't naturally think about doing that

## 7655:00 - 7695:00

myself when I started pushing apps into

## 7695:00 - 7720:00

production.

## 7720:00 - 7750:00

>> I think

## 7750:00 - 7770:00

I think you'll get to the next one. It

## 7770:00 - 7825:00

would be useful just as an overview when

## 7825:00 - 7860:00

you log in each day who do you talk to?

## 7860:00 - 7885:00

What does that take? How much time does

## 7885:00 - 7925:00

it take? that because that that feeds

## 7925:00 - 7950:00

into the first point, doesn't it? It's

## 7950:00 - 7975:00

there's context switching decks. There's

## 7975:00 - 8015:00

also just this and part of that is all

## 8015:00 - 8035:00

these different interfaces, all these

## 8035:00 - 8055:00

different exceptions, all the different

## 8055:00 - 8080:00

things when you log in each day to

## 8080:00 - 8130:00

artisan or qualified or Asian force.

## 8130:00 - 8160:00

There's a lot of time in different

## 8160:00 - 8200:00

interfaces and different conflicts.

## 8200:00 - 8220:00

That'd be the main one. And then maybe

## 8220:00 - 8255:00

just a quick reminder to folks, maybe

## 8255:00 - 8280:00

you have it in here, how we segment our

## 8280:00 - 8310:00

base for these different agents because

## 8310:00 - 8340:00

it's related to the first point, right?

## 8340:00 - 8385:00

>> Yeah. [snorts] Yeah.

## 8385:00 - 8440:00

Yeah. I would say to your point on the

## 8440:00 - 8470:00

context switching tax, right? It's it's

## 8470:00 - 8515:00

it's not even that I think about them as

## 8515:00 - 8555:00

20 agents anymore. Like I think the

## 8555:00 - 8595:00

better comparison to make to folks on

## 8595:00 - 8635:00

the skull and watching live is you have

## 8635:00 - 8685:00

to almost think about it now and I think

## 8685:00 - 8710:00

about it now is managing 20 different

## 8710:00 - 8760:00

people which like before we had 20

## 8760:00 - 8800:00

agents. I don't even know what we had

## 8800:00 - 8850:00

maximum headcount here. let's say 12 at

## 8850:00 - 8905:00

the very at the very peak.

## 8905:00 - 8950:00

Now we have 20 plus almost 30 different

## 8950:00 - 8995:00

agents plus you know three humans and a

## 8995:00 - 9055:00

dog that we manage. So I think that's a

## 9055:00 - 9085:00

better way to frame it to folks is to

## 9085:00 - 9150:00

think about each agent almost as its own

## 9150:00 - 9195:00

entity as your own employee that you

## 9195:00 - 9225:00

know speaks a different language, has a

## 9225:00 - 9250:00

different personality, needs different

## 9250:00 - 9300:00

things from you. Like to Jason's point,

## 9300:00 - 9345:00

like I'm not immune from logging into

## 9345:00 - 9395:00

each of these tools every day, seeing

## 9395:00 - 9420:00

what's going on, right? So like this is

## 9420:00 - 9455:00

a good example of my my kind of like

## 9455:00 - 9490:00

morning, even just this morning. Like I

## 9490:00 - 9510:00

actually didn't even have time to go

## 9510:00 - 9550:00

through my whole checklist cuz we are on

## 9550:00 - 9570:00

this call at 10. So I was like, I

## 9570:00 - 9595:00

haven't actually even made it through

## 9595:00 - 9630:00

all of my agent check-ins for the day

## 9630:00 - 9655:00

and it's already 10. Now it's going to

## 9655:00 - 9680:00

be like 11 by the time this is over and

## 9680:00 - 9705:00

I have other calls today. So like it's

## 9705:00 - 9770:00

basically going to take me the whole day

## 9770:00 - 9810:00

just to check in with all of our

## 9810:00 - 9840:00

different agents. So I don't really know

## 9840:00 - 9865:00

this my morning routine but my daily

## 9865:00 - 9900:00

routine. But so yeah, kind of a quick

## 9900:00 - 9930:00

example of the ones I check the most.

## 9930:00 - 9960:00

Right. So I would say I actually log

## 9960:00 - 10005:00

into 10K kind of first because this is

## 10005:00 - 10070:00

our main internal AIVPN. We've done a

## 10070:00 - 10090:00

previous episode about it where we did a

## 10090:00 - 10120:00

deep dive so you can go back and check

## 10120:00 - 10160:00

that one out. But just as a high level,

## 10160:00 - 10200:00

this is one that is running on internal

## 10200:00 - 10240:00

data. It has some API data. It's

## 10240:00 - 10275:00

literally telling me what I what I

## 10275:00 - 10315:00

slashw we should be doing every day for,

## 10315:00 - 10350:00

you know, tickets to SAS, paid tickets

## 10350:00 - 10385:00

to SAS annual, our VIP summits that we

## 10385:00 - 10415:00

have, our sponsorships that we have, our

## 10415:00 - 10455:00

sponsors, uh, media contacts, like

## 10455:00 - 10520:00

there's a bunch of highlevel,

## 10520:00 - 10560:00

it's highlevel, you know, goals that I'm

## 10560:00 - 10585:00

trying to hit with 10K. And so I check

## 10585:00 - 10610:00

that one every day just to see where

## 10610:00 - 10650:00

we're at. And like am I falling behind?

## 10650:00 - 10680:00

And that's why this one roasts me all

## 10680:00 - 10700:00

the time. It's like, Ameilia, you didn't

## 10700:00 - 10730:00

get, you know, these five things that I

## 10730:00 - 10755:00

laid out for you done yesterday. I'm

## 10755:00 - 10830:00

like, I had to go to sleep, dude. Like,

## 10830:00 - 10865:00

thanks for roasting me. I understand why

## 10865:00 - 10905:00

we're behind. Can you just help me

## 10905:00 - 10930:00

figure out how to get caught up in a way

## 10930:00 - 10950:00

that I can actually do with the time

## 10950:00 - 10985:00

that I have today? And so then it will

## 10985:00 - 11025:00

kind of, you know,

## 11025:00 - 11080:00

re re-evaluate its its to-do list for me

## 11080:00 - 11110:00

for the day. But 10K literally tells me

## 11110:00 - 11145:00

what to do. So that's why I log into

## 11145:00 - 11185:00

that one first because actually 10K2

## 11185:00 - 11205:00

will tell me what to do with our other

## 11205:00 - 11235:00

agents. That's also why I log into that

## 11235:00 - 11280:00

one first and foremost. Um, that one is

## 11280:00 - 11310:00

a mix too of Claude and Replet. So I'm

## 11310:00 - 11335:00

kind of like bouncing between those two

## 11335:00 - 11365:00

entities, which you know, a lot of

## 11365:00 - 11405:00

Replet runs, I'm pretty sure, on Claude.

## 11405:00 - 11445:00

And so for that one, context switching

## 11445:00 - 11485:00

is not too too hard because they kind of

## 11485:00 - 11515:00

speak the same language, but they have

## 11515:00 - 11545:00

different nuances in how they interact

## 11545:00 - 11600:00

with you, right? Like 10K as Claude is

## 11600:00 - 11635:00

obviously more like textbased, whereas

## 11635:00 - 11680:00

10K as the replet agent has a lot more

## 11680:00 - 11700:00

dashboards, has a lot more numbers in

## 11700:00 - 11720:00

it. So it's kind of a combination of

## 11720:00 - 11740:00

both that I'm talking to at the same

## 11740:00 - 11780:00

time there.

## 11780:00 - 11805:00

Or then I'll go into, you know, what are

## 11805:00 - 11850:00

our outward facing agents? I'll go into

## 11850:00 - 11890:00

all of our sales agents and ticket

## 11890:00 - 11920:00

agents and that's artisan qualified

## 11920:00 - 11970:00

agent force and now Monaco that's four

## 11970:00 - 12030:00

different agents I have to log into look

## 12030:00 - 12085:00

at who needs a human response

## 12085:00 - 12120:00

look at who it's reached out to over the

## 12120:00 - 12150:00

last you know day between the last time

## 12150:00 - 12205:00

I checked it yesterday let's say morning

## 12205:00 - 12235:00

and see what it's doing right like a a

## 12235:00 - 12290:00

lot of times I'll need to refresh

## 12290:00 - 12320:00

what the agents are doing who they're

## 12320:00 - 12335:00

reaching out to the copy they're

## 12335:00 - 12365:00

reaching out to. For instance, I have it

## 12365:00 - 12415:00

in the next screenshot here.

## 12415:00 - 12445:00

Like I And you can see where it's

## 12445:00 - 12470:00

roasting me already. Like I had to

## 12470:00 - 12505:00

context switch for this week when I was

## 12505:00 - 12530:00

doing this on Monday because I was like,

## 12530:00 - 12570:00

we have a distinct promotion going out

## 12570:00 - 12610:00

this week for Saturday annual tickets in

## 12610:00 - 12645:00

particular because the ticket prices go

## 12645:00 - 12675:00

up on March 1st. And I literally had to

## 12675:00 - 12710:00

put that context into five different

## 12710:00 - 12735:00

agents. Like literally, you can see some

## 12735:00 - 12760:00

of the screenshots here. I was like, I

## 12760:00 - 12795:00

have to go in and tell artisan that. I

## 12795:00 - 12825:00

have to go in and tell qualified that. I

## 12825:00 - 12850:00

have to go in and tell Salesforce that I

## 12850:00 - 12885:00

have to like 10K already knows that

## 12885:00 - 12905:00

because he's the one came up with it.

## 12905:00 - 12935:00

But then he's telling me, why aren't you

## 12935:00 - 12965:00

launching LinkedIn ads immediately for

## 12965:00 - 13000:00

this new promotion? Do it right now. I

## 13000:00 - 13030:00

was like, I will do it as soon as I'm

## 13030:00 - 13065:00

done talking to the other agents. And so

## 13065:00 - 13120:00

context switching becomes extremely like

## 13120:00 - 13155:00

I don't it's just hard to keep up with I

## 13155:00 - 13195:00

think sometimes in your brain. And a lot

## 13195:00 - 13235:00

of the times it's hard too for the

## 13235:00 - 13270:00

agents to remember everything you're

## 13270:00 - 13300:00

doing, right? So, I think there's kind

## 13300:00 - 13325:00

of like a double-edged sword there.

## 13325:00 - 13395:00

[snorts]

## 13395:00 - 13430:00

>> And so, the the at least for us for

## 13430:00 - 13495:00

today, if if you're literally logging in

## 13495:00 - 13525:00

and spending anywhere from 10 minutes to

## 13525:00 - 13560:00

an hour with four to five of our core

## 13560:00 - 13600:00

GTM agents, right? I would say every

## 13600:00 - 13625:00

single day, right? And with different

## 13625:00 - 13645:00

user interfaces,

## 13645:00 - 13675:00

>> you have to remind each others of the

## 13675:00 - 13700:00

changes, the campaigns because they

## 13700:00 - 13735:00

don't talk to each other. I know we

## 13735:00 - 13755:00

haven't found anything so it's slightly

## 13755:00 - 13790:00

rhetorical question but people talk

## 13790:00 - 13820:00

about orchestration agents and master

## 13820:00 - 13850:00

agents we haven't found anyone that can

## 13850:00 - 13880:00

integrate Asian force artisan qualified

## 13880:00 - 13935:00

Monaco momentum attention attendive like

## 13935:00 - 13980:00

we don't there's nothing out there today

## 13980:00 - 14005:00

even with 10k which we've built

## 14005:00 - 14050:00

ourselves that at some magical API or

## 14050:00 - 14070:00

other level can integrate everything for

## 14070:00 - 14100:00

you that does product does not exist

## 14100:00 - 14115:00

right

## 14115:00 - 14155:00

>> no it doesn't exist I will say the the

## 14155:00 - 14205:00

the benefit of Salesforce

## 14205:00 - 14245:00

buying being qualified momentum is like

## 14245:00 - 14285:00

eventually by probably Dreamforce right

## 14285:00 - 14315:00

those two things will be integrated into

## 14315:00 - 14390:00

one so we have like two west dashboards

## 14390:00 - 14415:00

and I'll probably have one centralized

## 14415:00 - 14470:00

one by October but only because you know

## 14470:00 - 14500:00

they've they've acquired those tool for

## 14500:00 - 14545:00

most tools it's it's completely separate

## 14545:00 - 14555:00

>> yep

## 14555:00 - 14600:00

>> yeah so it's a lot

## 14600:00 - 14620:00

>> you can have a one-on-one with your

## 14620:00 - 14660:00

agent every day

## 14660:00 - 14700:00

>> a weekly oneonone instead of a check-in

## 14700:00 - 14730:00

on Slack back. If you want to accomplish

## 14730:00 - 14765:00

what we've done or better, you have to

## 14765:00 - 14800:00

do a truly and honestly a one-on-one

## 14800:00 - 14820:00

with your agent every day. Even if you

## 14820:00 - 14835:00

don't want to do the work, you got to do

## 14835:00 - 14860:00

the work to see one-on-one with every

## 14860:00 - 14880:00

agent every day.

## 14880:00 - 14925:00

>> Yeah. And I think it's an interesting

## 14925:00 - 14950:00

learning, too. I didn't put it here, but

## 14950:00 - 14985:00

like one thing I do with my agents is I

## 14985:00 - 15010:00

ask them every day like, "What should I

## 15010:00 - 15045:00

be mindful of? What should I be looking

## 15045:00 - 15060:00

at?"

## 15060:00 - 15105:00

And then sometimes it'll say hey like I

## 15105:00 - 15130:00

can give you a recommendation but you

## 15130:00 - 15150:00

need to give me some data back or you

## 15150:00 - 15165:00

need to tell me what you're doing with

## 15165:00 - 15185:00

your other ages or you need to give me

## 15185:00 - 15230:00

XYZ inputs in order for me to output

## 15230:00 - 15275:00

that. And so that is a very good way I

## 15275:00 - 15300:00

think more so to look at it is just

## 15300:00 - 15360:00

think of this as 20 different people

## 15360:00 - 15400:00

that you have to manage every day.

## 15400:00 - 15420:00

Right? Sometimes you can get away with

## 15420:00 - 15465:00

doing a one-on-one with a human once a

## 15465:00 - 15510:00

week if you're you know lucky. This is

## 15510:00 - 15540:00

you can't you can't wait a whole week.

## 15540:00 - 15570:00

Like that's the thing. It's like if you

## 15570:00 - 15590:00

wait a whole week with any of your

## 15590:00 - 15620:00

agents, it'll be so out of date by the

## 15620:00 - 15655:00

time the week's over.

## 15655:00 - 15690:00

>> The production the output is so high.

## 15690:00 - 15740:00

>> Yeah. Yeah. Exactly. You can't you it

## 15740:00 - 15765:00

just can't afford to wait a whole week

## 15765:00 - 15800:00

or like you're or you're probably just

## 15800:00 - 15825:00

wasting honestly you're probably wasting

## 15825:00 - 15855:00

your money if you don't spend the time

## 15855:00 - 15885:00

to do it daily because a lot of these

## 15885:00 - 15925:00

are waiting for you to give it inputs,

## 15925:00 - 15965:00

right? like it's such a high volume like

## 15965:00 - 16000:00

artisan qualified agent force like I'm

## 16000:00 - 16025:00

constantly giving it more people to

## 16025:00 - 16050:00

reach out to better messaging different

## 16050:00 - 16080:00

campaigns different things where like if

## 16080:00 - 16110:00

I don't do that most of those don't do

## 16110:00 - 16140:00

it themselves so they're just going to

## 16140:00 - 16165:00

sit there like your agents are just

## 16165:00 - 16195:00

going to idle if you don't check in with

## 16195:00 - 16215:00

them every day which I also think is

## 16215:00 - 16255:00

just like a waste of time and money cuz

## 16255:00 - 16285:00

what you want is to have that high

## 16285:00 - 16320:00

volume output so you're maximizing what

## 16320:00 - 16380:00

the agent can do right so

## 16380:00 - 16430:00

it's an interesting nuance Okay, number

## 16430:00 - 16465:00

two. I would say biggest learning is we

## 16465:00 - 16490:00

learned this kind of quickly, but I

## 16490:00 - 16520:00

think it's just more so now getting

## 16520:00 - 16575:00

harder now that we have 20 plus almost

## 16575:00 - 16605:00

30 agents, but you know, in the

## 16605:00 - 16625:00

beginning it used to take us more than

## 16625:00 - 16645:00

two weeks to implement some of these

## 16645:00 - 16670:00

agents. I would say now we've pretty

## 16670:00 - 16710:00

much gotten it down to about two weeks

## 16710:00 - 16735:00

for a lot of reasons. One reason like a

## 16735:00 - 16770:00

lot again even though context switching

## 16770:00 - 16815:00

is hard. You can share a lot of contacts

## 16815:00 - 16845:00

between agents. So kind of once you have

## 16845:00 - 16880:00

one, you can do another one. It gets

## 16880:00 - 16905:00

easier. It's not easy, but it gets

## 16905:00 - 16930:00

easier.

## 16930:00 - 16950:00

But I would say we've kind of gotten it

## 16950:00 - 16990:00

down to like a two week implementation

## 16990:00 - 17030:00

pipeline for any of our agents. It's

## 17030:00 - 17055:00

true for Monica that we just did. It's

## 17055:00 - 17075:00

true for Happy Fox that we just did.

## 17075:00 - 17115:00

Like each of those just took two weeks

## 17115:00 - 17155:00

and that was not spending the entirety

## 17155:00 - 17175:00

of the two weeks on it, but it was

## 17175:00 - 17205:00

spending the majority of two weeks on

## 17205:00 - 17250:00

it. And so this just gets harder with

## 17250:00 - 17305:00

every new agent that you add because

## 17305:00 - 17350:00

each new agent means you're not

## 17350:00 - 17380:00

spending, you know, that daily time I

## 17380:00 - 17405:00

just mentioned. You're probably not

## 17405:00 - 17435:00

doing that if while you're onboarding a

## 17435:00 - 17460:00

new agent. Like I know I didn't spend

## 17460:00 - 17485:00

the time I needed to with each of our

## 17485:00 - 17545:00

agents in the way that I should I I

## 17545:00 - 17575:00

usually do when I was onboarding these

## 17575:00 - 17600:00

new agents cuz I was like, I want to get

## 17600:00 - 17625:00

these off the ground. I want to get them

## 17625:00 - 17660:00

up and running. And so I'm just going to

## 17660:00 - 17695:00

have to do, you know, I'm going to have

## 17695:00 - 17720:00

to do the trade-off and let the other

## 17720:00 - 17765:00

ones slightly degrade or slash sit idle

## 17765:00 - 17790:00

while I get these new agents up because

## 17790:00 - 17840:00

there's just no way I can do it all. And

## 17840:00 - 17875:00

so I think that's a huge trade-off when

## 17875:00 - 17905:00

you're looking at bringing in, you know,

## 17905:00 - 17965:00

multiple agents is instantly things go

## 17965:00 - 17985:00

stale with your agents, right? While

## 17985:00 - 18025:00

they're idling, they go stale really

## 18025:00 - 18055:00

fast. Not because they can't do things

## 18055:00 - 18085:00

on their own, but because they're again

## 18085:00 - 18130:00

waiting for you to tell them what to do.

## 18130:00 - 18165:00

So, if they've run through, like, let's

## 18165:00 - 18190:00

just say one of these outbound agents

## 18190:00 - 18215:00

has run through a whole contact list,

## 18215:00 - 18265:00

but I'm busy on boarding another agent,

## 18265:00 - 18295:00

it's just sitting there. It's literally

## 18295:00 - 18320:00

idling. It's sitting there. It's not

## 18320:00 - 18345:00

doing anything cuz I haven't had the

## 18345:00 - 18375:00

time to give it new contacts. Like that

## 18375:00 - 18415:00

is I think just a huge nuance folks

## 18415:00 - 18450:00

don't really talk about is anytime you

## 18450:00 - 18470:00

know we're all trying to push like okay

## 18470:00 - 18505:00

we we we also push like we have a lot of

## 18505:00 - 18540:00

agents and I think there's a lot more

## 18540:00 - 18580:00

agent things people can be doing but

## 18580:00 - 18620:00

just realize like anytime you bring on a

## 18620:00 - 18650:00

new one it's going to take time it's

## 18650:00 - 18695:00

going to cost money for these agents

## 18695:00 - 18725:00

it's going to cost some of your you know

## 18725:00 - 18760:00

mental overhead and mental bandwidth and

## 18760:00 - 18800:00

mental time like these agents do not

## 18800:00 - 18850:00

deploy themselves and so even with all

## 18850:00 - 18870:00

the help you in the world, which you

## 18870:00 - 18895:00

should only pick vendors you get help

## 18895:00 - 18935:00

from. But even with that, like again,

## 18935:00 - 18965:00

two weeks is pretty fast. I think most

## 18965:00 - 19000:00

agents, especially in the early days,

## 19000:00 - 19025:00

took us like a month, maybe six weeks to

## 19025:00 - 19045:00

get up and running. Now we've gotten it

## 19045:00 - 19065:00

down to two weeks cuz we've gotten

## 19065:00 - 19105:00

pretty good at it. But I'd say in that

## 19105:00 - 19145:00

math, you can really only add one slash

## 19145:00 - 19190:00

one and a half agents per month max.

## 19190:00 - 19230:00

Like otherwise, you're running in place

## 19230:00 - 19250:00

because you can't really keep up with

## 19250:00 - 19290:00

your current agents to add the new

## 19290:00 - 19320:00

agent. So, it doesn't actually maybe it

## 19320:00 - 19345:00

doesn't make sense to add that new agent

## 19345:00 - 19380:00

if you can't keep up with it or know

## 19380:00 - 19410:00

that you can that you'll need to do kind

## 19410:00 - 19470:00

of a blackout period to do a new agent.

## 19470:00 - 19505:00

And so, I think this is super nuance,

## 19505:00 - 19530:00

not something I really realized until we

## 19530:00 - 19570:00

had multiple agents of production that

## 19570:00 - 19600:00

there is a trade-off. Like, it's you're

## 19600:00 - 19630:00

going to get a lift from it for sure,

## 19630:00 - 19655:00

right? If it works the way you think it

## 19655:00 - 19680:00

will, but there's a trade-off. Like,

## 19680:00 - 19720:00

there it's not free. It's not free

## 19720:00 - 19840:00

scalability instantly.

## 19840:00 - 19870:00

Okay.

## 19870:00 - 19890:00

Oh, these are Yeah, these are

## 19890:00 - 19920:00

screenshots I added. So, I added some of

## 19920:00 - 19945:00

these screenshots of Monaco. This was

## 19945:00 - 19965:00

like one of our newer agents that we

## 19965:00 - 20010:00

just did. Again, we got help from the

## 20010:00 - 20060:00

team to put us into the product. I think

## 20060:00 - 20130:00

it took, you know, probably two weeks

## 20130:00 - 20155:00

conservatively, maybe a little bit less

## 20155:00 - 20185:00

actually because we we worked fairly

## 20185:00 - 20210:00

quickly with them. But again, it was one

## 20210:00 - 20240:00

of those things where I blocked out

## 20240:00 - 20270:00

doing other things. And actually, the

## 20270:00 - 20295:00

mono team works over the weekend. So, I

## 20295:00 - 20310:00

did a lot of this over the weekend,

## 20310:00 - 20360:00

which was nice. But we got it up and

## 20360:00 - 20390:00

running in basically a week and a half.

## 20390:00 - 20420:00

And you can see here like in its first

## 20420:00 - 20450:00

week on, you know, it reached out to 64

## 20450:00 - 20480:00

people. It booked six meetings

## 20480:00 - 20525:00

instantly. Some of those are like tier

## 20525:00 - 20550:00

one accounts for us, which is pretty

## 20550:00 - 20595:00

dang good. So, again, is it worth it?

## 20595:00 - 20630:00

Yes. From that perspective, it was worth

## 20630:00 - 20670:00

it to let our other agents kind of like

## 20670:00 - 20730:00

sit idle slash do a little bit less

## 20730:00 - 20760:00

while we were getting this new agent on

## 20760:00 - 20780:00

board because we believed it would be

## 20780:00 - 20805:00

worth the trade-offs, right? But just

## 20805:00 - 20825:00

know that you're going to have to

## 20825:00 - 20850:00

probably weigh trade-offs when you come

## 20850:00 - 20895:00

into something like adding a new agent.

## 20895:00 - 20920:00

And maybe just plan for a blackout

## 20920:00 - 20950:00

period. I think that's my kind of meta

## 20950:00 - 21000:00

point is if you plan on it, it'll

## 21000:00 - 21020:00

probably work more to your benefit

## 21020:00 - 21045:00

versus just going into it like, oh, I

## 21045:00 - 21085:00

can just add this in a day. that's not

## 21085:00 - 21105:00

really going to work for you or your

## 21105:00 - 21140:00

agents. So,

## 21140:00 - 21185:00

okay. Number three,

## 21185:00 - 21225:00

and this may not apply to all of you,

## 21225:00 - 21270:00

but I think from what I've seen, and

## 21270:00 - 21290:00

this is where I want to get your take,

## 21290:00 - 21325:00

too, Jason, I see a lot of folks where

## 21325:00 - 21380:00

it's either a single or like maybe one

## 21380:00 - 21405:00

like for us it's two people, but like

## 21405:00 - 21445:00

it's kind of a single point of failure

## 21445:00 - 21485:00

for our agents. And it's funny because I

## 21485:00 - 21510:00

put some screenshots in the next one of

## 21510:00 - 21535:00

like I asked my agents what what it

## 21535:00 - 21605:00

would do if I stopped talking to

## 21605:00 - 21650:00

and the responses were interesting.

## 21650:00 - 21700:00

But I think this is where folks get

## 21700:00 - 21725:00

themselves into trouble because they

## 21725:00 - 21750:00

think they can, you know, recruit

## 21750:00 - 21775:00

somebody to just manage all the agents.

## 21775:00 - 21800:00

That doesn't really work. They think

## 21800:00 - 21825:00

they can just, you know, roll it out to

## 21825:00 - 21855:00

the entire sales team or the entire CS

## 21855:00 - 21885:00

team. That doesn't really work. There's

## 21885:00 - 21925:00

reasons that doesn't really work. Like

## 21925:00 - 21950:00

this is I would say the biggest

## 21950:00 - 21975:00

double-edged sword of like I do think

## 21975:00 - 22035:00

having a single point of truth with who

## 22035:00 - 22075:00

is managing the agents, right? Like who

## 22075:00 - 22115:00

from our perspective, which contacts go

## 22115:00 - 22150:00

into qualified versus artisan versus

## 22150:00 - 22190:00

Monaco versus agent force? Like that is

## 22190:00 - 22245:00

just all in my brain right now. And I'm

## 22245:00 - 22290:00

sure Claude could write it down if I

## 22290:00 - 22355:00

told it to and give it to other agents

## 22355:00 - 22395:00

if it was really pushed. But like, but

## 22395:00 - 22430:00

then if like, let's just say even if I

## 22430:00 - 22475:00

got the agents to give me an ND file of

## 22475:00 - 22520:00

everything it knows with me, I'm not

## 22520:00 - 22550:00

sure the next person can really pick it

## 22550:00 - 22580:00

up in the same way. They might say,

## 22580:00 - 22630:00

"Okay, you know, Ameilia was segmenting

## 22630:00 - 22665:00

a lot of her ticket outbound in Artisan

## 22665:00 - 22690:00

and then a lot of her sponsor outbound

## 22690:00 - 22725:00

in agent force and then new cold

## 22725:00 - 22775:00

outbound in Monaco and then, you know,

## 22775:00 - 22795:00

what whatever else we're doing

## 22795:00 - 22835:00

retargeting in and in inbound in

## 22835:00 - 22875:00

qualified

## 22875:00 - 22905:00

But maybe this new person doesn't agree

## 22905:00 - 22935:00

with that. They may say, "Hey, agent."

## 22935:00 - 22970:00

Like, "Oh, you're outbound. Cool. I'm

## 22970:00 - 22995:00

just going to keep one of you." Like one

## 22995:00 - 23040:00

of like we only need one of you to stay

## 23040:00 - 23090:00

to do, you know, outbound. If it's truly

## 23090:00 - 23105:00

at the end of the day, those are all

## 23105:00 - 23135:00

doing outbound functions. Somebody else

## 23135:00 - 23160:00

might say, I only need one of those

## 23160:00 - 23185:00

agents to do those things, which might

## 23185:00 - 23210:00

be true, but also like we have found

## 23210:00 - 23240:00

like we have all these tools cuz they're

## 23240:00 - 23270:00

super nuanced. They're like hyper

## 23270:00 - 23300:00

effective in certain verticals. And

## 23300:00 - 23345:00

that's why we've chosen to do multiple

## 23345:00 - 23390:00

agents versus just one agent. And so I

## 23390:00 - 23410:00

think that's an interesting nuance you

## 23410:00 - 23440:00

would lose. Like again, double-edged

## 23440:00 - 23475:00

sword of like I think having one person

## 23475:00 - 23495:00

know what's going on with all your

## 23495:00 - 23520:00

agents is super important. But then what

## 23520:00 - 23550:00

happens if you know you're in a bigger

## 23550:00 - 23590:00

company, you have maybe multiple people

## 23590:00 - 23625:00

working on agents or you're in a bigger

## 23625:00 - 23670:00

company and that person leaves. Like how

## 23670:00 - 23720:00

like how do you scale past this n equals

## 23720:00 - 23765:00

1? And I don't think there's a good

## 23765:00 - 23815:00

answer for this today. There is no like

## 23815:00 - 23870:00

again crazy good agent that can manage

## 23870:00 - 23905:00

all the other agents on its own today as

## 23905:00 - 23940:00

of February. There's that doesn't exist,

## 23940:00 - 23985:00

right? Like I wish there were I don't

## 23985:00 - 24025:00

know if I think there will be but

## 24025:00 - 24055:00

there's not one today. And so I think

## 24055:00 - 24105:00

even with all the help we get, it's this

## 24105:00 - 24160:00

is just a huge issue that I think the

## 24160:00 - 24195:00

market has not realized yet.

## 24195:00 - 24220:00

>> Yeah, it's good. I want to keep going,

## 24220:00 - 24250:00

but yeah, I mean I mean obviously we're

## 24250:00 - 24275:00

extreme and tiny. I mean, if you left

## 24275:00 - 24300:00

for some reason, we would we would have

## 24300:00 - 24340:00

to cease using our agents. There there's

## 24340:00 - 24375:00

no there's no there's no plan B. We're

## 24375:00 - 24405:00

just all learning that you need some

## 24405:00 - 24430:00

sort of chief agent officer, right?

## 24430:00 - 24470:00

Whether it's a whether it's a whatever

## 24470:00 - 24495:00

you want to call them, someone that can

## 24495:00 - 24530:00

manage all of your agents that I think

## 24530:00 - 24570:00

needs to be a bit of a nerd, a tech

## 24570:00 - 24600:00

nerd, ideally a bit of a marketing nerd

## 24600:00 - 24635:00

because a lot of these products are if

## 24635:00 - 24665:00

you can manage a complex marketing

## 24665:00 - 24690:00

automation tool, you can probably manage

## 24690:00 - 24720:00

most of the products that we use. you

## 24720:00 - 24755:00

can hack the rest.

## 24755:00 - 24775:00

But, you know, thinking through it, I

## 24775:00 - 24805:00

mean, this is this is Captain Obvious,

## 24805:00 - 24830:00

but I think if you actually find the

## 24830:00 - 24855:00

person that can deploy these agents for

## 24855:00 - 24910:00

real, that actually can be success just

## 24910:00 - 24935:00

like a lot of these functions, but

## 24935:00 - 24960:00

immediately they should recruit. You

## 24960:00 - 24990:00

need to recruit somebody else on their

## 24990:00 - 25020:00

team and and divide and conquer and make

## 25020:00 - 25040:00

sure you have two.

## 25040:00 - 25070:00

>> Yeah, you got to have two, right? I

## 25070:00 - 25105:00

mean, one's hard enough. There's a lot

## 25105:00 - 25140:00

of in the early days of agents when we

## 25140:00 - 25165:00

talk to folks, there's very few people

## 25165:00 - 25190:00

in a lot of organizations that can do

## 25190:00 - 25215:00

this. It's not that hard, but there's

## 25215:00 - 25240:00

very few people. But you you Yeah. If

## 25240:00 - 25265:00

you don't have two, you're at

## 25265:00 - 25300:00

existential risk.

## 25300:00 - 25340:00

>> Yeah. Like literally when Philipe Picero

## 25340:00 - 25375:00

at Persona was in London, he you know,

## 25375:00 - 25405:00

he famously set up all their agents, but

## 25405:00 - 25485:00

then he was like, I I started using

## 25485:00 - 25510:00

he was qualified or something like with

## 25510:00 - 25560:00

the sales team. And

## 25560:00 - 25595:00

then he was like I rolled it out to like

## 25595:00 - 25630:00

a few reps to be able to like cuz like

## 25630:00 - 25660:00

qualified you can round robin like the

## 25660:00 - 25685:00

inbound, right? you can say, "Okay, like

## 25685:00 - 25720:00

I'm going to I'll be the mass he's like

## 25720:00 - 25745:00

the master controller of it of like

## 25745:00 - 25770:00

doing the training and the programming."

## 25770:00 - 25795:00

But qualified is actually an easier one

## 25795:00 - 25815:00

to get the rest of your team on because

## 25815:00 - 25850:00

you can just have them respond to folks

## 25850:00 - 25875:00

when the agent can't. You can set up

## 25875:00 - 25920:00

certain escalations and how however you

## 25920:00 - 25940:00

want it, right? So for him, he was like,

## 25940:00 - 25965:00

"Okay, I rolled it out to like five of

## 25965:00 - 26005:00

the top reps on the sales team." And

## 26005:00 - 26040:00

then the very top rep, whose name is

## 26040:00 - 26075:00

also Amelia,

## 26075:00 - 26120:00

ended up being the most like affluent at

## 26120:00 - 26165:00

learning how to work with the agent

## 26165:00 - 26210:00

handinhand as a co-pilot. And so then he

## 26210:00 - 26245:00

decided from that like kind of pilot

## 26245:00 - 26285:00

test with his humans that Amelia on

## 26285:00 - 26305:00

their team would be the next person he

## 26305:00 - 26335:00

trains on how to use the agent. So like

## 26335:00 - 26360:00

he did kind of, you know, like a little

## 26360:00 - 26405:00

bit of a beta with their team and then

## 26405:00 - 26445:00

said, "Okay, I know now who wants to

## 26445:00 - 26470:00

actually manage these agents the way

## 26470:00 - 26495:00

that I do." And so now I'm going to

## 26495:00 - 26520:00

train that person. So that's another way

## 26520:00 - 26555:00

to do it too across your team is to do

## 26555:00 - 26590:00

it that way. But yeah, this again

## 26590:00 - 26610:00

double-edged sword though because now

## 26610:00 - 26645:00

it's like now he has to tell all the

## 26645:00 - 26670:00

agents everything plus he has to tell

## 26670:00 - 26715:00

Ameilia everything. So like

## 26715:00 - 26740:00

>> and he's the CRO arguably.

## 26740:00 - 26755:00

>> And he's the CRO.

## 26755:00 - 26765:00

>> Arguably.

## 26765:00 - 26775:00

>> Yeah. Exactly.

## 26775:00 - 26790:00

>> Right. [laughter]

## 26790:00 - 26825:00

>> Yeah.

## 26825:00 - 26865:00

>> So it's funny too. I asked our agents

## 26865:00 - 26910:00

what they what they recommended we do if

## 26910:00 - 26940:00

for some reason I got hit by I said if I

## 26940:00 - 26975:00

get hit by a bus what what should you

## 26975:00 - 27050:00

tell a

## 27050:00 - 27085:00

about yourself so that they could like

## 27085:00 - 27115:00

if Jason were to take these agents over

## 27115:00 - 27140:00

cuz I got hit by a bus. What would you

## 27140:00 - 27195:00

what would you tell him? And and the 10K

## 27195:00 - 27230:00

version of Claude said it would I well

## 27230:00 - 27255:00

these docs are on my computer cuz I use

## 27255:00 - 27320:00

Claude on on on machine. it would need

## 27320:00 - 27355:00

to give him these, you know, documents,

## 27355:00 - 27395:00

which I'm like, I don't know. Maybe you

## 27395:00 - 27420:00

could guess my laptop password. I don't

## 27420:00 - 27455:00

know. Maybe. But like, first of all,

## 27455:00 - 27475:00

that's already an issue because I'm

## 27475:00 - 27505:00

like, these docs are literally on my

## 27505:00 - 27560:00

computer and probably nowhere else.

## 27560:00 - 27595:00

Then it's literally saying the next

## 27595:00 - 27630:00

campaigns he has to run for March and

## 27630:00 - 27650:00

April, which I don't think you would

## 27650:00 - 27690:00

want to. And then I think it's

## 27690:00 - 27725:00

interesting, it called out what I

## 27725:00 - 27765:00

consider the vibe for SAS annual, which

## 27765:00 - 27790:00

I hadn't really thought about. But it's

## 27790:00 - 27820:00

just it's a little funny that the agent

## 27820:00 - 27870:00

was like, "Make sure Jason or whoever

## 27870:00 - 27890:00

takes us over if you get hit by a bus

## 27890:00 - 27940:00

knows what the vibe is like."

## 27940:00 - 27980:00

So, it's I was like, I do actually call

## 27980:00 - 28000:00

it a moment in time. That's really

## 28000:00 - 28025:00

funny. I use that in like a lot of copy

## 28025:00 - 28070:00

and I use that in like a lot of things.

## 28070:00 - 28100:00

So, it's a little funny that the agent

## 28100:00 - 28125:00

picked up on that. It wanted you to know

## 28125:00 - 28160:00

the vibe, Jason, just in case I get hit

## 28160:00 - 28210:00

by a bus. [laughter]

## 28210:00 - 28270:00

I see. The other interesting thing was I

## 28270:00 - 28320:00

asked our SAS sponsors,

## 28320:00 - 28350:00

which is an app we talked a lot about

## 28350:00 - 28395:00

last week, how many lines of code it

## 28395:00 - 28425:00

has, which was shocking because I think

## 28425:00 - 28445:00

Jason, you said it's something like

## 28445:00 - 28485:00

3,000 is like, you know, average or

## 28485:00 - 28550:00

basic or simple. It said 12,000 and it

## 28550:00 - 28600:00

says it said it was hefty. But then I

## 28600:00 - 28650:00

said, "Okay, since this is a hefty

## 28650:00 - 28700:00

fivecoded app that I made for sponsors,

## 28700:00 - 28730:00

yeah, how would you bring somebody new

## 28730:00 - 28765:00

up to speed?" And this is where it gets

## 28765:00 - 28790:00

tough, right? Cuz I'm like, I think what

## 28790:00 - 28825:00

it says is so complicated that somebody

## 28825:00 - 28870:00

else would give up. It's explaining it's

## 28870:00 - 28905:00

a sponsor portal. Fine, that's easy. But

## 28905:00 - 28935:00

then it says how the authorization

## 28935:00 - 28970:00

works. Like, okay, file uploads go to

## 28970:00 - 29010:00

replet, object storage, submission sync

## 29010:00 - 29055:00

to Google via Zapier. Again, you're just

## 29055:00 - 29085:00

running into a lot of issues here. The

## 29085:00 - 29125:00

agent doesn't know my clerk login. It

## 29125:00 - 29170:00

doesn't know my Google Sheets login. It

## 29170:00 - 29225:00

doesn't know my Zapier login.

## 29225:00 - 29295:00

It's a like it's it would be a mess to

## 29295:00 - 29350:00

hand it off. [laughter]

## 29350:00 - 29375:00

And then it was funny cuz then my agent

## 29375:00 - 29405:00

said, "Don't get hit by a bus." That was

## 29405:00 - 29460:00

it. That was its recommendation.

## 29460:00 - 29485:00

I said, "Thanks. I'm really trying

## 29485:00 - 29525:00

[laughter] not to."

## 29525:00 - 29560:00

All right.

## 29560:00 - 29580:00

This is number four for me. You've

## 29580:00 - 29595:00

already seen it a little bit in these

## 29595:00 - 29670:00

slides. These agents as I they're

## 29670:00 - 29695:00

interesting to work with on a daily

## 29695:00 - 29765:00

basis versus humans cuz you know some

## 29765:00 - 29790:00

sometimes humans have their own

## 29790:00 - 29835:00

ambitions, their own goals. Like I feel

## 29835:00 - 29885:00

like Claude is famously goal seeking but

## 29885:00 - 29915:00

in a very different way than a human

## 29915:00 - 29975:00

being is right. In a very different way.

## 29975:00 - 30010:00

So, I think there are times where I also

## 30010:00 - 30035:00

feel like these agents don't really know

## 30035:00 - 30070:00

the date and time and like they don't

## 30070:00 - 30100:00

realize they don't realize on their own

## 30100:00 - 30120:00

that like when you start chatting with

## 30120:00 - 30140:00

them at 6:00 in the morning, you're

## 30140:00 - 30160:00

still chatting with them at midnight

## 30160:00 - 30180:00

that you should probably go to sleep at

## 30180:00 - 30200:00

this point. Like, you can't keep working

## 30200:00 - 30225:00

with your agent. So, like it's just a

## 30225:00 - 30260:00

little funny

## 30260:00 - 30305:00

that as I as I considered it, but you'll

## 30305:00 - 30330:00

see my agent's response on the next

## 30330:00 - 30360:00

slide. I consider my 10K is like

## 30360:00 - 30410:00

roasting me all the freaking time.

## 30410:00 - 30435:00

Like, you can see it here. It said,

## 30435:00 - 30460:00

"You're behind on Summit Outreach." I

## 30460:00 - 30495:00

said, I know I am.

## 30495:00 - 30545:00

You needed to send 200 emails by Feb

## 30545:00 - 30605:00

15th and you sent 87. You're 56% behind

## 30605:00 - 30640:00

target. Now, maybe you don't think this

## 30640:00 - 30685:00

is roasting me. I thought it was though,

## 30685:00 - 30715:00

cuz it also told me to block 3 hours and

## 30715:00 - 30740:00

I was like, you know, I don't have 3

## 30740:00 - 30785:00

hours. Let's do this and catch up. Like,

## 30785:00 - 30815:00

thanks. But also, now you're just

## 30815:00 - 30850:00

stressing me out and roasting me versus

## 30850:00 - 30900:00

being helpful. Um, so I thought that was

## 30900:00 - 30935:00

a little bit funny cuz it was it, you

## 30935:00 - 30960:00

know,

## 30960:00 - 30990:00

What does the agent care? The agent's

## 30990:00 - 31010:00

just going to tell me the truth. The

## 31010:00 - 31060:00

agent has all the data more than I

## 31060:00 - 31080:00

probably look at it, right? Like I look

## 31080:00 - 31125:00

at it a lot,

## 31125:00 - 31160:00

but it's got all like it knows where I'm

## 31160:00 - 31200:00

behind. It knows my calendar. It knows

## 31200:00 - 31230:00

all these things. And it's still said,

## 31230:00 - 31270:00

you're you're dropping the ball here.

## 31270:00 - 31325:00

Catch up. It's constantly asking me,

## 31325:00 - 31355:00

"What's preventing you from doing this

## 31355:00 - 31385:00

right now?" And sometimes I'm like, it's

## 31385:00 - 31420:00

literally 11:00 p.m. and I'm I'm I'm

## 31420:00 - 31445:00

tired, so I can't I can't really like

## 31445:00 - 31485:00

focus on launching this XYZ thing that

## 31485:00 - 31525:00

you want me to do right at this very

## 31525:00 - 31555:00

moment cuz I need to sleep first and

## 31555:00 - 31600:00

then do it. So, it's just interesting,

## 31600:00 - 31630:00

right, of like, okay, what then? What do

## 31630:00 - 31665:00

you decide as the human leader of the

## 31665:00 - 31725:00

agents is helpful versus what crosses a

## 31725:00 - 31765:00

line into maybe slightly demoralizing of

## 31765:00 - 31835:00

because your agent knows everything.

## 31835:00 - 31870:00

It's not that it's wrong when it's

## 31870:00 - 31905:00

roasting me, right? That is maybe the

## 31905:00 - 31935:00

uncomfortable truth. Oftentimes it

## 31935:00 - 31985:00

roasts me and I'm like, "Yeah, well, I

## 31985:00 - 32015:00

deserve that roast. You were right. Like

## 32015:00 - 32050:00

I didn't do this thing that I'm now

## 32050:00 - 32085:00

behind on."

## 32085:00 - 32125:00

But also like because so much like so

## 32125:00 - 32155:00

like 10k roast me the most. Some of the

## 32155:00 - 32185:00

other agents roast me slightly, but like

## 32185:00 - 32205:00

because you're getting it from so many

## 32205:00 - 32230:00

different angles and so many agents cuz

## 32230:00 - 32260:00

you can't keep up with them. Sometimes I

## 32260:00 - 32285:00

feel like it does cross a little bit of

## 32285:00 - 32315:00

line where I'm like, "Okay, dude. like

## 32315:00 - 32370:00

today just like sugarcoat it to me like

## 32370:00 - 32420:00

you would a person like today I don't

## 32420:00 - 32450:00

need the hard like I can't deal with

## 32450:00 - 32485:00

hard truths every day. I don't think

## 32485:00 - 32525:00

anyone can like I can't to some degree

## 32525:00 - 32550:00

but I think every day all the time from

## 32550:00 - 32595:00

your agent is a lot. But it's funny cuz

## 32595:00 - 32625:00

it said you know literally it said to me

## 32625:00 - 32670:00

on Sunday what's when it was super late

## 32670:00 - 32700:00

what's blocking you from the LinkedIn

## 32700:00 - 32745:00

ads from going live and I I literally

## 32745:00 - 32775:00

said it's cuz it was late. And then I

## 32775:00 - 32810:00

said, "Hey, you've kind of roasted me a

## 32810:00 - 32830:00

lot lately. Can you bring up some

## 32830:00 - 32860:00

examples for this webinar I'm doing?"

## 32860:00 - 32890:00

And it said, "Looking through the

## 32890:00 - 32925:00

transcript, I haven't really roasted

## 32925:00 - 32965:00

you."

## 32965:00 - 33025:00

It said, "I've a tough accountability

## 33025:00 - 33070:00

partner." And then it listed ways. This

## 33070:00 - 33105:00

is only two out of five ways. Then it

## 33105:00 - 33165:00

listed ways it should have roasted me.

## 33165:00 - 33220:00

And I said, "Thanks.

## 33220:00 - 33245:00

I don't know if you're I don't know if

## 33245:00 - 33270:00

your agents risk you as much, Jason, but

## 33270:00 - 33305:00

I think this is just a like a fun

## 33305:00 - 33360:00

interesting one of like, you know, just

## 33360:00 - 33390:00

something maybe you don't expect from

## 33390:00 - 33410:00

your agents is that they will always

## 33410:00 - 33435:00

tell you the truth and they have all the

## 33435:00 - 33500:00

data.

## 33500:00 - 33520:00

Let's get into the last one and I'll do

## 33520:00 - 33545:00

the bonus one and then we've we've got

## 33545:00 - 33565:00

quite a few questions that I want to try

## 33565:00 - 33610:00

and get to. So,

## 33610:00 - 33665:00

compliance and security issues. Anytime

## 33665:00 - 33730:00

we run an audit or ask an agent to run a

## 33730:00 - 33775:00

security audit, it takes time to fix

## 33775:00 - 33830:00

these. Like we ran a huge one the other

## 33830:00 - 33885:00

day on sasher.ai. We haven't even fixed

## 33885:00 - 33925:00

I would say even 10% of the issues that

## 33925:00 - 33990:00

came up in the audit because it became

## 33990:00 - 34020:00

super fragile once we started like

## 34020:00 - 34070:00

futzing with the code and like then you

## 34070:00 - 34100:00

know sometimes when you do a security

## 34100:00 - 34125:00

audit

## 34125:00 - 34165:00

it will go too far like it'll start to

## 34165:00 - 34190:00

lock things down to the point where

## 34190:00 - 34220:00

you're like I actually can't even use my

## 34220:00 - 34240:00

app anymore because it took this too

## 34240:00 - 34270:00

far. So then you kind of have to peel

## 34270:00 - 34290:00

back one by one. It's something you have

## 34290:00 - 34315:00

to walk the agent through. It can't

## 34315:00 - 34355:00

really do it that great on its own.

## 34355:00 - 34400:00

And so this takes a lot of time. Not

## 34400:00 - 34435:00

only does this takes a lot of time, the

## 34435:00 - 34460:00

maintenance becomes a lot harder each

## 34460:00 - 34485:00

time you do a security audience and like

## 34485:00 - 34520:00

implement whatever it recommended with

## 34520:00 - 34560:00

you know you together. So then when you

## 34560:00 - 34605:00

start to multiply that across 20 agents,

## 34605:00 - 34640:00

it's almost unfathomable like how to

## 34640:00 - 34725:00

keep your apps and all your data secure.

## 34725:00 - 34745:00

But Jason, you've been running the

## 34745:00 - 34770:00

security more than I have. Like you're

## 34770:00 - 34790:00

the one who actually told me that I

## 34790:00 - 34825:00

should talk. It's askful.

## 34825:00 - 34845:00

>> Well, there's a lot there's a lot here.

## 34845:00 - 34900:00

I think it is it is a reminder that

## 34900:00 - 34935:00

in general, I mean, you can see this in

## 34935:00 - 34965:00

the press. Agents can do more

## 34965:00 - 35005:00

autonomously. That's why they're agents,

## 35005:00 - 35025:00

right? What's the definition of an

## 35025:00 - 35060:00

agent? I'm actually not sure, but I

## 35060:00 - 35105:00

think it is a piece of software powered

## 35105:00 - 35130:00

by AI that can complete tasks

## 35130:00 - 35175:00

autonomously. And all of these agents,

## 35175:00 - 35230:00

if that we're talking about, go to

## 35230:00 - 35260:00

market agents and others have access to

## 35260:00 - 35295:00

your data. And there's an inherent level

## 35295:00 - 35330:00

of security and that Salesforce is our

## 35330:00 - 35355:00

hub, right? As to tie this to the

## 35355:00 - 35395:00

beginning that that is important. I

## 35395:00 - 35450:00

think I do think it is one of the if if

## 35450:00 - 35470:00

no other reason to use something like

## 35470:00 - 35490:00

sales source as your hub is that it is

## 35490:00 - 35525:00

secure. But these agents then take data

## 35525:00 - 35580:00

out and the honest truth is no agents no

## 35580:00 - 35615:00

third party agents are more secure than

## 35615:00 - 35645:00

Salesforce. They're all less secure is

## 35645:00 - 35675:00

the reality of it. They're less secure

## 35675:00 - 35700:00

because they're startups, but they're

## 35700:00 - 35720:00

also less secure because the agents can

## 35720:00 - 35745:00

do crazy stuff with them like publish

## 35745:00 - 35785:00

them to the wild, right? Or do other

## 35785:00 - 35825:00

things. It is just a reality. And then

## 35825:00 - 35875:00

just the final point

## 35875:00 - 35915:00

is ones you vibe code yourself, which we

## 35915:00 - 35940:00

have done a lot of, they are inherently

## 35940:00 - 35965:00

less secure than third party apps that

## 35965:00 - 36020:00

you buy today. I don't that may not last

## 36020:00 - 36055:00

because

## 36055:00 - 36105:00

a lot all of the the the products from

## 36105:00 - 36135:00

cloud code to repel to level below have

## 36135:00 - 36165:00

added more and more security but they're

## 36165:00 - 36195:00

all custom. They all are less secure

## 36195:00 - 36240:00

than a Salesforce or something. So all

## 36240:00 - 36265:00

of the the apps like us you're going to

## 36265:00 - 36290:00

run are going to have customer data

## 36290:00 - 36325:00

through them. They're all of them right?

## 36325:00 - 36365:00

You're not Stripe or PayPal like it's

## 36365:00 - 36405:00

not that dramatic in many cases but bear

## 36405:00 - 36440:00

in mind you're taking some measured

## 36440:00 - 36490:00

risk. So at least if nothing else the

## 36490:00 - 36540:00

ones that you've create yourself

## 36540:00 - 36580:00

before you launch and then frequently at

## 36580:00 - 36610:00

least every month just go to the agent

## 36610:00 - 36640:00

and say do a deep security audit on my

## 36640:00 - 36670:00

app and just have it do that. Don't

## 36670:00 - 36700:00

assume the apps do it yourself. That's

## 36700:00 - 36745:00

the best actionable thing I can take.

## 36745:00 - 36785:00

And then just be thoughtful that there

## 36785:00 - 36810:00

are there just inherent trade-offs to

## 36810:00 - 36825:00

this that we're all going to have to

## 36825:00 - 36885:00

learn, right? And it may make sense as

## 36885:00 - 36930:00

you get going in the agentic revolution

## 36930:00 - 36960:00

to maybe use slightly less sensitive

## 36960:00 - 36985:00

data to start. If you're a conservative

## 36985:00 - 37005:00

enterprise, it just may make sense just

## 37005:00 - 37030:00

like it always has been for enterprise

## 37030:00 - 37055:00

software. You always start in a in a

## 37055:00 - 37075:00

little group or little function that's

## 37075:00 - 37115:00

safer when you buy a startup. It's just

## 37115:00 - 37145:00

this on steroids because you cannot

## 37145:00 - 37165:00

fully predict what the agent will do

## 37165:00 - 37200:00

with your data. It's just a reality.

## 37200:00 - 37210:00

>> Yep.

## 37210:00 - 37240:00

>> It's just a reality.

## 37240:00 - 37275:00

>> Yep.

## 37275:00 - 37305:00

Yeah. I put a few screenshots here of

## 37305:00 - 37310:00

like when

## 37310:00 - 37330:00

>> run another audit.

## 37330:00 - 37375:00

>> Yeah. Run another one. Thanks, dude.

## 37375:00 - 37415:00

Like

## 37415:00 - 37435:00

there was a question in the chat too.

## 37435:00 - 37450:00

How are we running these security

## 37450:00 - 37485:00

audits? Some of them you can do natively

## 37485:00 - 37505:00

with the agent, right? Like lovable

## 37505:00 - 37540:00

reply. You can just ask its agent to run

## 37540:00 - 37610:00

an audit for you. Um, other times,

## 37610:00 - 37660:00

again, you may not need it if it's a

## 37660:00 - 37700:00

full-blown third party tool, but you

## 37700:00 - 37735:00

should ask that tool like I ask transfer

## 37735:00 - 37770:00

from Marson all the time. I'm like, hey,

## 37770:00 - 37800:00

what is your how like what's your

## 37800:00 - 37830:00

compliance right now? Or like [laughter]

## 37830:00 - 37870:00

like what do you cuz you have so much of

## 37870:00 - 37910:00

my data like let's just make sure it's

## 37910:00 - 37940:00

not going anywhere. It's not supposed

## 37940:00 - 37965:00

to. So I think that's another thing too

## 37965:00 - 37990:00

is like when you use third party tools

## 37990:00 - 38020:00

like we do obviously we use Salesforce

## 38020:00 - 38055:00

for a lot and that's ultra like fairly

## 38055:00 - 38090:00

secure right knock on wood but for the

## 38090:00 - 38125:00

other ones we use I I just ask them I'm

## 38125:00 - 38155:00

like hey what what are you guys up up to

## 38155:00 - 38190:00

date on what are you doing to make sure

## 38190:00 - 38265:00

our data is secure.

## 38265:00 - 38290:00

Okay, last one and then I'll do

## 38290:00 - 38340:00

questions. I added as number six because

## 38340:00 - 38380:00

this may not apply to everyone. It may

## 38380:00 - 38415:00

not be a bridge that you ever cross, but

## 38415:00 - 38445:00

I think if you get to the point where

## 38445:00 - 38485:00

your agents do work 24/7 and you have

## 38485:00 - 38540:00

almost 30 agents and again your agents

## 38540:00 - 38565:00

know all the data when they answer a

## 38565:00 - 38590:00

question, they have your APIs, they have

## 38590:00 - 38620:00

your sales, but like they have all these

## 38620:00 - 38655:00

things they can look at and are brutally

## 38655:00 - 38695:00

honest roast you when you can't keep up

## 38695:00 - 38725:00

with them.

## 38725:00 - 38770:00

I think it it it it makes it harder

## 38770:00 - 38825:00

sometimes. I know at least for me when I

## 38825:00 - 38850:00

deal with actual humans that sometimes I

## 38850:00 - 38875:00

lose patience with them a lot quicker

## 38875:00 - 38905:00

now because I'm like, "What do you mean

## 38905:00 - 38930:00

you don't know the answer?" Like my

## 38930:00 - 38980:00

agents know the answer instantly. Like,

## 38980:00 - 39010:00

what do you mean you don't know the the

## 39010:00 - 39065:00

answer to this very basic question?

## 39065:00 - 39100:00

What do you mean you haven't delivered

## 39100:00 - 39140:00

on XYZ thing that I gave you three weeks

## 39140:00 - 39160:00

to do? Or what do you mean you forgot

## 39160:00 - 39190:00

something that I've, you know, told you

## 39190:00 - 39235:00

literally 10 times now?

## 39235:00 - 39275:00

It does make you on sometimes I often

## 39275:00 - 39320:00

start to wonder I'm like do I need them

## 39320:00 - 39345:00

or can't I build an agent to do this

## 39345:00 - 39380:00

because

## 39380:00 - 39420:00

if I'm losing patience with with them

## 39420:00 - 39440:00

I'll probably lose patience with

## 39440:00 - 39470:00

somebody else in the same boat and if an

## 39470:00 - 39495:00

agent can just do it and the agent won't

## 39495:00 - 39515:00

lose patience maybe I should just build

## 39515:00 - 39550:00

an agent to deal with them and they

## 39550:00 - 39605:00

don't have to deal with me. So

## 39605:00 - 39630:00

I think it's just an interesting nuance.

## 39630:00 - 39685:00

I think something else I've seen just to

## 39685:00 - 39730:00

be wary of this is almost somewhat

## 39730:00 - 39785:00

unrelated but related in that I've I've

## 39785:00 - 39850:00

really find it now in the age of AI in

## 39850:00 - 39895:00

you know the early phases of 2026 when

## 39895:00 - 39925:00

folks

## 39925:00 - 39970:00

tell us that they're going to help SAS

## 39970:00 - 40000:00

for you know let's just say XYZ thing

## 40000:00 - 40050:00

for SAS annual like I'll give you a

## 40050:00 - 40090:00

concrete example a couple months ago I

## 40090:00 - 40145:00

was working with a few parties on just

## 40145:00 - 40170:00

house annual third-party production

## 40170:00 - 40195:00

things we normally contract out things I

## 40195:00 - 40230:00

thought an agent couldn't do and I went

## 40230:00 - 40265:00

out to a few different agencies and

## 40265:00 - 40300:00

production teams to RFP for it to get a

## 40300:00 - 40350:00

quote for it right normal okay fine

## 40350:00 - 40405:00

a few folks told me this would be your

## 40405:00 - 40445:00

deliverable it was one sentence and this

## 40445:00 - 40465:00

would be the price and it was something

## 40465:00 - 40520:00

like 40 or 50k a month and I was like in

## 40520:00 - 40565:00

the age of AI that's what you're

## 40565:00 - 40630:00

promising something that like is one

## 40630:00 - 40670:00

sentence, one price point, and nothing

## 40670:00 - 40700:00

else. Like, you couldn't even ask your

## 40700:00 - 40730:00

own internal agent or freaking ask your

## 40730:00 - 40780:00

claude or Chad GBT how to make a better

## 40780:00 - 40805:00

proposal. Like, that's terrible in the

## 40805:00 - 40830:00

age of AI. I was like, this is just

## 40830:00 - 40870:00

unacceptable. Like, I just didn't

## 40870:00 - 40890:00

respond to those people. And it's sad

## 40890:00 - 40925:00

because multiple people did it. Like,

## 40925:00 - 40975:00

and I think maybe that's just a symptom

## 40975:00 - 41055:00

of agencies versus software tools. And

## 41055:00 - 41085:00

maybe marketing agencies won't exist in

## 41085:00 - 41120:00

a year because of this, but I literally

## 41120:00 - 41155:00

was like, how in the age of AI can you

## 41155:00 - 41185:00

say you have a one-s sentence

## 41185:00 - 41225:00

deliverable and a fixed price point and

## 41225:00 - 41270:00

you can't even use the basic AI better

## 41270:00 - 41320:00

than our team can? Like what? I I was

## 41320:00 - 41370:00

exasperated. I was like, this is

## 41370:00 - 41410:00

so crazy to me that so much of the world

## 41410:00 - 41440:00

is still operating this way. Like I

## 41440:00 - 41480:00

think, you know, AI is probably going to

## 41480:00 - 41520:00

come for them. But

## 41520:00 - 41550:00

I was like, I don't think anyone in the

## 41550:00 - 41585:00

age of AI should be giving you a fuzzy

## 41585:00 - 41645:00

deliverable and a fuzzy timeline.

## 41645:00 - 41670:00

That's just not acceptable anymore. I

## 41670:00 - 41690:00

don't think that was ever acceptable. I

## 41690:00 - 41745:00

think it's just more unacceptable now.

## 41745:00 - 41770:00

I also This is an interesting nuance,

## 41770:00 - 41800:00

but I do feel like I have now managed

## 41800:00 - 41840:00

more agents ever than than humans. And

## 41840:00 - 41890:00

so I'm probably worse at managing people

## 41890:00 - 41940:00

now than I than I am. Like agents I get.

## 41940:00 - 41965:00

I can, you know, talk to them first

## 41965:00 - 41985:00

thing in the morning, last thing at

## 41985:00 - 42010:00

night. Like, they're not going to be

## 42010:00 - 42035:00

impatient with me if I don't respond to

## 42035:00 - 42085:00

them right all day. They might be idle,

## 42085:00 - 42105:00

but they're not going to be like, you

## 42105:00 - 42135:00

know, the same as the same vibe as

## 42135:00 - 42170:00

somebody in Slack being like, "Hey, I

## 42170:00 - 42190:00

have a question for you. Can you answer

## 42190:00 - 42210:00

this right now?" And sometimes they

## 42210:00 - 42250:00

can't like, so I do feel like now that

## 42250:00 - 42285:00

I've flipped the switch to managing more

## 42285:00 - 42315:00

agents, I think I've probably become

## 42315:00 - 42350:00

slightly worse at managing the people

## 42350:00 - 42370:00

that are, you know, that work with

## 42370:00 - 42400:00

Sasser, especially leading up to SAS

## 42400:00 - 42460:00

radial. So, it's something that I am

## 42460:00 - 42500:00

hyper aware of now because I'm like

## 42500:00 - 42525:00

there I have to remember that there are

## 42525:00 - 42565:00

not agents.

## 42565:00 - 42615:00

I need to be more I don't know at some

## 42615:00 - 42630:00

I'm like I just don't know what's

## 42630:00 - 42655:00

realistic anymore. I'm like if the

## 42655:00 - 42720:00

agents work 24/7 and feasibly any human

## 42720:00 - 42755:00

can use an agent, why can't they keep up

## 42755:00 - 42775:00

a little bit more? That's why I called

## 42775:00 - 42840:00

it my bonus point of once you reach this

## 42840:00 - 42875:00

point

## 42875:00 - 42905:00

what does that really do right in your

## 42905:00 - 42935:00

in your nucleus of how you operate with

## 42935:00 - 42970:00

the team the team is agents like they

## 42970:00 - 43005:00

are still part of the team though right

## 43005:00 - 43025:00

all right anything else you want to add

## 43025:00 - 43060:00

Jason before we go to questions

## 43060:00 - 43085:00

>> no I think it's great let's hit the

## 43085:00 - 43125:00

questions and I think it's just a

## 43125:00 - 43150:00

reminder I do want to it's a reminder to

## 43150:00 - 43185:00

me that no matter how much people talk

## 43185:00 - 43205:00

about on social media about an

## 43205:00 - 43230:00

orchestration layer we haven't found one

## 43230:00 - 43275:00

yet it's it's on our checklist list, but

## 43275:00 - 43300:00

when I look at a lot of the GTM and

## 43300:00 - 43320:00

other vendors, they're just building

## 43320:00 - 43340:00

point solutions,

## 43340:00 - 43370:00

>> right? No matter what anybody says. So,

## 43370:00 - 43400:00

as soon as we master the orchestration

## 43400:00 - 43420:00

layer ourselves, we will share it with

## 43420:00 - 43450:00

you. It is it's definitely a challenge

## 43450:00 - 43485:00

for 2026, but it's one we haven't even

## 43485:00 - 43515:00

realistically been able to tackle yet.

## 43515:00 - 43545:00

But let's get the questions.

## 43545:00 - 43580:00

>> Yeah, it's funny. There are a few

## 43580:00 - 43630:00

questions on

## 43630:00 - 43675:00

why we haven't tried to build our own

## 43675:00 - 43725:00

orchestration layer.

## 43725:00 - 43750:00

Well, how how would I mean, do all these

## 43750:00 - 43800:00

agents have enough of an API or open

## 43800:00 - 43820:00

system that we could manage? Can they

## 43820:00 - 43855:00

all be managed through an API?

## 43855:00 - 43895:00

>> We'd have to extract all the data

## 43895:00 - 43930:00

>> through into cloud or wherever our own

## 43930:00 - 43960:00

vibe coded app and then we'd have to man

## 43960:00 - 43985:00

and we could get them all in some sort

## 43985:00 - 44010:00

of unified system, but they'd all have

## 44010:00 - 44090:00

to be 100% manageable through their API.

## 44090:00 - 44130:00

>> Yeah. Which they're not all today.

## 44130:00 - 44155:00

>> Yeah. I don't think it's a priority for

## 44155:00 - 44170:00

any of them. I don't think it matters

## 44170:00 - 44205:00

whether it's MCP or anything. if they're

## 44205:00 - 44240:00

not exposing their entire I mean

## 44240:00 - 44275:00

literally just going in every morning

## 44275:00 - 44300:00

and seeing the exceptions and issues

## 44300:00 - 44325:00

that come up from campaigns the night

## 44325:00 - 44380:00

before if that can't be fully replicated

## 44380:00 - 44410:00

inside an orchestration layer with some

## 44410:00 - 44440:00

management it's useless like if it's not

## 44440:00 - 44465:00

as good it's useless right

## 44465:00 - 44515:00

>> so everything would have to be exposed

## 44515:00 - 44540:00

>> it's a good question and it's not I'm

## 44540:00 - 44560:00

not saying someone smarter than us

## 44560:00 - 44585:00

couldn't figure it out but we we haven't

## 44585:00 - 44615:00

even begun to to figure that out there's

## 44615:00 - 44660:00

no there's no obvious offtheshelfish

## 44660:00 - 44725:00

even vibe solution today and

## 44725:00 - 44755:00

platforms are a lot of these agentic

## 44755:00 - 44790:00

platforms are not as open as they look

## 44790:00 - 44810:00

[snorts]

## 44810:00 - 44840:00

or as you might think not as that's not

## 44840:00 - 44865:00

fair as as much as you might think.

## 44865:00 - 44900:00

They're siloed solutions today.

## 44900:00 - 44905:00

>> Yeah. [snorts]

## 44905:00 - 44935:00

>> Right. The the only thing that is open

## 44935:00 - 44970:00

is Salesforce. It's where they all meet.

## 44970:00 - 45005:00

And if Salesforce could be our or our

## 45005:00 - 45025:00

truly our orchestration layer, that

## 45025:00 - 45050:00

would be actually the simplest path,

## 45050:00 - 45080:00

right? But it's our management layer,

## 45080:00 - 45105:00

but it's not really a truly an agentive

## 45105:00 - 45135:00

orchestration layer yet,

## 45135:00 - 45190:00

>> right? Yeah. Not yet. Another question

## 45190:00 - 45215:00

in the chat from Alex. Any other

## 45215:00 - 45275:00

thoughts on scaling past one person to

## 45275:00 - 45340:00

manage all of your agents?

## 45340:00 - 45360:00

>> I don't know. You would know better than

## 45360:00 - 45380:00

me. I I don't think it's that

## 45380:00 - 45430:00

complicated. I think that I think that

## 45430:00 - 45455:00

you you I mean, listen, there's

## 45455:00 - 45490:00

obviously conflicts and in some ways a

## 45490:00 - 45510:00

lot of the start of this conversation

## 45510:00 - 45540:00

was about conflicts, potential conflicts

## 45540:00 - 45560:00

between agents and making sure they

## 45560:00 - 45585:00

don't conflict. But if you have two

## 45585:00 - 45615:00

folks on your team that work well

## 45615:00 - 45635:00

together, two humans, they'll just

## 45635:00 - 45685:00

divide and conquer. Yeah, I mean we our

## 45685:00 - 45715:00

our agents are our go to our sales

## 45715:00 - 45745:00

agents are roughly as as AI alluded to

## 45745:00 - 45770:00

and we've talked about before are are

## 45770:00 - 45800:00

actually fairly clearly segmented.

## 45800:00 - 45830:00

There's there's raw outbound, right?

## 45830:00 - 45890:00

There's there's there's inbound,

## 45890:00 - 45925:00

there's re-energizing lapse leads,

## 45925:00 - 45955:00

right? There's lapse leads and I might I

## 45955:00 - 45990:00

might be missing the fourth one. Just

## 45990:00 - 46010:00

have different people manage these

## 46010:00 - 46040:00

different campaigns and have them

## 46040:00 - 46060:00

coordinate every day just like the

## 46060:00 - 46080:00

agents coordinate every day. That would

## 46080:00 - 46135:00

be fun. If we could find a mini Amelia

## 46135:00 - 46180:00

or a maxi Amelia, we would hire him or

## 46180:00 - 46200:00

her tomorrow as a human. Like, no

## 46200:00 - 46220:00

problem. And they would just divide and

## 46220:00 - 46245:00

conquer. I don't think that is an issue

## 46245:00 - 46295:00

with the agents.

## 46295:00 - 46320:00

>> Actually, might let us do more, right?

## 46320:00 - 46340:00

We probably could do a little bit.

## 46340:00 - 46355:00

>> Oh, for sure.

## 46355:00 - 46360:00

>> Yeah.

## 46360:00 - 46395:00

>> Yeah. Yeah. I think I the issue I've run

## 46395:00 - 46420:00

into is like I well one I was like I'm

## 46420:00 - 46435:00

not going to try and solve this problem

## 46435:00 - 46465:00

before annual

## 46465:00 - 46510:00

but two I I think the problem I run into

## 46510:00 - 46540:00

is like I can't find folks that know

## 46540:00 - 46575:00

more about the agents than I do at this

## 46575:00 - 46585:00

very moment in time.

## 46585:00 - 46625:00

>> Well that's that's that's that's a big I

## 46625:00 - 46665:00

think what you need is someone that not

## 46665:00 - 46705:00

that for real wants to learn and is a

## 46705:00 - 46735:00

good nerd about tools.

## 46735:00 - 46745:00

>> Yeah.

## 46745:00 - 46770:00

>> You need someone that has already built

## 46770:00 - 46805:00

like listen everyone should be screening

## 46805:00 - 46830:00

hires better. You should have someone

## 46830:00 - 46850:00

someone should come into the interview

## 46850:00 - 46890:00

and have built an agent in replet or cla

## 46890:00 - 46930:00

does something. That should be the test.

## 46930:00 - 46940:00

>> Yeah,

## 46940:00 - 46965:00

>> that should be in fact what they do at

## 46965:00 - 47000:00

Replet itself now is they give you a

## 47000:00 - 47015:00

massive amount of credits. I think they

## 47015:00 - 47045:00

give you like $1,000 worth of credits in

## 47045:00 - 47065:00

the interview and they say build

## 47065:00 - 47085:00

anything you want with a thousand bucks.

## 47085:00 - 47115:00

Come back to us and then we'll do the

## 47115:00 - 47135:00

interview.

## 47135:00 - 47140:00

>> Yep.

## 47140:00 - 47170:00

>> It's the best test in the world. You

## 47170:00 - 47200:00

should do if we could if they don't need

## 47200:00 - 47215:00

to be better than you, but they need to

## 47215:00 - 47245:00

pass that test, right? Here's whatever

## 47245:00 - 47270:00

you need. just just show me something

## 47270:00 - 47300:00

you've built that automates GTM or

## 47300:00 - 47330:00

agents that is better than we could. And

## 47330:00 - 47355:00

you know, if you're not too crazy, we'd

## 47355:00 - 47375:00

probably hire you tomorrow. Even if you

## 47375:00 - 47400:00

could be pretty crazy, we'd still hire

## 47400:00 - 47445:00

you, right? It'd be fine.

## 47445:00 - 47490:00

>> Yeah. Yeah. I think that's a good test.

## 47490:00 - 47530:00

And another question is, how do you

## 47530:00 - 47580:00

calculate your agent? I count it more so

## 47580:00 - 47635:00

as close revenue. That is literally our

## 47635:00 - 47695:00

our very topline agent ROI across the

## 47695:00 - 47750:00

board across all these agents is ROI

## 47750:00 - 47800:00

like true ROI and revenue.

## 47800:00 - 47825:00

>> Just two things. It is very easy to

## 47825:00 - 47855:00

attribute revenue to each agent. It's

## 47855:00 - 47865:00

very simple.

## 47865:00 - 47885:00

>> Yeah, it's super easy.

## 47885:00 - 47900:00

>> In fact, there's rarely even a

## 47900:00 - 47930:00

multi-touch issue at the agentic level.

## 47930:00 - 47955:00

There may be multi-touch at a market

## 47955:00 - 47980:00

meta marketing level. It's very easy.

## 47980:00 - 48020:00

Which agent interacted with which lead

## 48020:00 - 48050:00

and did that did that lead close? Like

## 48050:00 - 48100:00

and then we attribute revenue to them.

## 48100:00 - 48135:00

That's the main way we measure ROI. The

## 48135:00 - 48185:00

reality is having said that, it's not

## 48185:00 - 48220:00

why we started.

## 48220:00 - 48260:00

We started because we had people that

## 48260:00 - 48305:00

didn't want to do these jobs and we

## 48305:00 - 48340:00

said, can we replace a six-f figureure

## 48340:00 - 48405:00

hire with a five figure agent?

## 48405:00 - 48435:00

So, the truth is even if these agents

## 48435:00 - 48465:00

performed a little bit worse than they

## 48465:00 - 48500:00

did, they would still be ROI positive on

## 48500:00 - 48540:00

that on that goal, right? Our goal was

## 48540:00 - 48570:00

basically to achieve the same amount of

## 48570:00 - 48630:00

revenue with half the humans and and the

## 48630:00 - 48655:00

agents. That was that was the way we

## 48655:00 - 48715:00

initially measured ROI. And honestly, I

## 48715:00 - 48770:00

you know, you you need to deliver the

## 48770:00 - 48790:00

one thing I'll say to folks in general

## 48790:00 - 48810:00

if they're scratching their heads and

## 48810:00 - 48835:00

why is it so hard? I can tell you some

## 48835:00 - 48880:00

of the products that we use, most of the

## 48880:00 - 48935:00

ones we use, they have infinite demand.

## 48935:00 - 48965:00

like Monaco, we just rolled it out for

## 48965:00 - 49000:00

outbound that we talked about. They're

## 49000:00 - 49035:00

booked for two months including weekends

## 49035:00 - 49070:00

for demos. Okay, there is one called

## 49070:00 - 49120:00

Basis, which is an agentic pro product

## 49120:00 - 49140:00

for accounting yesterday. I don't know

## 49140:00 - 49170:00

the team, but they just raised a billion

## 49170:00 - 49195:00

yesterday and they said in their in

## 49195:00 - 49210:00

their in their header, one of the

## 49210:00 - 49240:00

challenges is like the demand is simply

## 49240:00 - 49270:00

overwhelming. Like they can't serve the

## 49270:00 - 49290:00

demand. Now, some of that is because you

## 49290:00 - 49310:00

have to train these agents and you have

## 49310:00 - 49335:00

to onboard them and you can't dump it on

## 49335:00 - 49365:00

the customer. So there's a reason for

## 49365:00 - 49410:00

it, but that's how we measure ROI. But

## 49410:00 - 49435:00

if you're a vendor, if you're working at

## 49435:00 - 49480:00

a startup, your ROI needs to be massive

## 49480:00 - 49500:00

in this world. You're going to be

## 49500:00 - 49545:00

slaughtered by folks that deliver like a

## 49545:00 - 49570:00

six figure meeting on day one like

## 49570:00 - 49620:00

Monaco did, right? Or take over all of

## 49620:00 - 49650:00

like two people did for like each of

## 49650:00 - 49680:00

Artisan and Mon and qualified. They

## 49680:00 - 49715:00

replace like two two people each, right?

## 49715:00 - 49810:00

That's high ROI. Mediocre ROI is dead.

## 49810:00 - 49865:00

It's just dead. Odd. products that just

## 49865:00 - 49905:00

give you productivity bounces that no

## 49905:00 - 49930:00

one's going to buy that stuff today. So

## 49930:00 - 49970:00

that's why I challenge folks out there.

## 49970:00 - 49995:00

If you're stalled out, if your business

## 49995:00 - 50030:00

is struggling, if people aren't lining

## 50030:00 - 50060:00

up out the door to buy your agent, your

## 50060:00 - 50100:00

agent is not good enough.

## 50100:00 - 50145:00

Anyone that has this massive ROI, they

## 50145:00 - 50175:00

cannot service the demand. They

## 50175:00 - 50205:00

literally cannot service the demand. At

## 50205:00 - 50240:00

least not all the demand. And and in

## 50240:00 - 50265:00

fact, what a lot of the vendors that we

## 50265:00 - 50310:00

highlight here, if nothing else, they

## 50310:00 - 50345:00

ruthlessly screen out prospects that are

## 50345:00 - 50370:00

not a good ICP fit because they don't

## 50370:00 - 50400:00

even want to waste their time, anybody's

## 50400:00 - 50425:00

time. They don't want them to churn.

## 50425:00 - 50445:00

They don't want them to bounce. If you

## 50445:00 - 50470:00

don't have enough data, if you're too

## 50470:00 - 50490:00

small, if you're the wrong org, some of

## 50490:00 - 50515:00

the folks we talked about just just they

## 50515:00 - 50555:00

just it may it frustrates people. We get

## 50555:00 - 50575:00

emails all the time, hey, can you get me

## 50575:00 - 50625:00

a meeting with this vendor?

## 50625:00 - 50690:00

>> I mean, we can we will, but it's but

## 50690:00 - 50710:00

sometimes they're making the right

## 50710:00 - 50725:00

decision. and they're so overwhelmed

## 50725:00 - 50755:00

with demand, they've got to focus on

## 50755:00 - 50800:00

their core ICB. So, that should be you.

## 50800:00 - 50835:00

I know it's tough to hear, but it should

## 50835:00 - 50865:00

be you. And if it is, if you have this

## 50865:00 - 50905:00

agent where the ROI is so insane, you

## 50905:00 - 50930:00

can generate new business for them the

## 50930:00 - 50960:00

first day or the first week, or you can

## 50960:00 - 50990:00

replace multiple humans with an agent

## 50990:00 - 51025:00

reliably, in today's world, right now,

## 51025:00 - 51050:00

this may not last, in today's world, you

## 51050:00 - 51105:00

will have demand out the door.

## 51105:00 - 51145:00

Out the door. And if you're not, don't

## 51145:00 - 51170:00

delude yourself that you just have that

## 51170:00 - 51235:00

your AI is good enough. It is not. Yep.

## 51235:00 - 51255:00

Okay. I was trying to hit one or two

## 51255:00 - 51295:00

last questions. Another question from

## 51295:00 - 51315:00

the chat was, "What's preventing you

## 51315:00 - 51350:00

guys from letting the agents do more of

## 51350:00 - 51395:00

the work, i.e. emailing on your behalf,

## 51395:00 - 51430:00

updating LinkedIn, letting it do the

## 51430:00 - 51455:00

LinkedIn ads, etc. since it's roasting

## 51455:00 - 51495:00

you on that?" I'll give you my quick

## 51495:00 - 51560:00

take is it can't do it.

## 51560:00 - 51620:00

I would let it do it if it could.

## 51620:00 - 51650:00

These agents can't do that. I have not

## 51650:00 - 51725:00

seen an agent successfully do email

## 51725:00 - 51770:00

marketing at SC. The moment I find one,

## 51770:00 - 51805:00

I'm using it that actually works. I have

## 51805:00 - 51870:00

not found one that actually works. Like

## 51870:00 - 51905:00

not just write all of these just write

## 51905:00 - 51950:00

email copy. They don't actually send it

## 51950:00 - 51995:00

to the right contacts at the right at

## 51995:00 - 52030:00

the right time. They just don't do it.

## 52030:00 - 52070:00

>> It'll come it. Listen, some folks are

## 52070:00 - 52090:00

going to challenge us and say, "Hey, my

## 52090:00 - 52130:00

startup does it." Listen, we we look at

## 52130:00 - 52155:00

everything that's out there. The reality

## 52155:00 - 52205:00

is, you know, marketing is behind sales.

## 52205:00 - 52240:00

>> It's just the reality. Honestly, if you

## 52240:00 - 52270:00

squint at the apps we use, our stack,

## 52270:00 - 52290:00

half of them really are marketing

## 52290:00 - 52325:00

automation but for sales,

## 52325:00 - 52350:00

>> right? Go back to the old days.

## 52350:00 - 52385:00

Salesoft, Outreach, companies like this,

## 52385:00 - 52410:00

they were they are marketing tools just

## 52410:00 - 52430:00

designed for the sales team instead of

## 52430:00 - 52460:00

the marketer, right? That's these are

## 52460:00 - 52495:00

just those tools on steroids with AI.

## 52495:00 - 52545:00

They're just ahead. It is embarrassing

## 52545:00 - 52580:00

that we do not have a fully automated

## 52580:00 - 52605:00

HubSpot/Marquetto

## 52605:00 - 52630:00

today. There's no excuse for it's it's

## 52630:00 - 52675:00

faking 2026 like and and marketing

## 52675:00 - 52705:00

actually is some ways easier problems to

## 52705:00 - 52740:00

solve than sales, right? Instead, we're

## 52740:00 - 52790:00

living we're living in the past and even

## 52790:00 - 52815:00

I get I get folks reach out to me and

## 52815:00 - 52840:00

what they're doing in marketing is very

## 52840:00 - 52875:00

narrow. Like I can automate a little

## 52875:00 - 52900:00

piece of your LinkedIn ad and maybe

## 52900:00 - 52920:00

we'll add that, right? We haven't

## 52920:00 - 52945:00

historically done that. But I don't need

## 52945:00 - 52990:00

a I don't need a landing page, right? or

## 52990:00 - 53025:00

like a little tiny optimize my

## 53025:00 - 53055:00

Instagram. I need a That's why we built

## 53055:00 - 53080:00

our own VP of marketing. I wish we

## 53080:00 - 53125:00

hadn't. So, we are all over this. I hope

## 53125:00 - 53165:00

that in the back half of this year when

## 53165:00 - 53190:00

we do these AI lives, it's actually all

## 53190:00 - 53215:00

about marketing. That's what I'm

## 53215:00 - 53245:00

optimistic about, but we don't need any

## 53245:00 - 53275:00

like we need the kind of ROI and

## 53275:00 - 53290:00

marketing that we see in sales.

## 53290:00 - 53325:00

Otherwise, it's just it's not worth it.

## 53325:00 - 53360:00

They're not better enough, right? But we

## 53360:00 - 53390:00

would love we would love to. There's and

## 53390:00 - 53415:00

there's no reason it can't be automated

## 53415:00 - 53450:00

with AI.

## 53450:00 - 53475:00

There there's no reason. There's no

## 53475:00 - 53510:00

reason that you cannot ship better

## 53510:00 - 53535:00

emails than a human can create. There's

## 53535:00 - 53560:00

no reason AI can't take your past

## 53560:00 - 53595:00

campaigns and update them with new

## 53595:00 - 53635:00

visuals, new new video, new content, and

## 53635:00 - 53665:00

send them out. There's no reason AI

## 53665:00 - 53690:00

can't segment your base better than a

## 53690:00 - 53720:00

human can segment your base. There's

## 53720:00 - 53755:00

just no excuse. There's no excuse to not

## 53755:00 - 53795:00

run programmatic advertising for B2B,

## 53795:00 - 53830:00

not for B TOC, without you having to do

## 53830:00 - 53855:00

anything. There's no like that all

## 53855:00 - 53900:00

should be doable today. And people are

## 53900:00 - 53925:00

going to say, "We do it. We do it. We

## 53925:00 - 53965:00

we'll keep looking, friends." But if you

## 53965:00 - 54000:00

can do all of this, then like do what

## 54000:00 - 54030:00

these leaders have set it all up for us

## 54030:00 - 54055:00

on their own and show us that it works

## 54055:00 - 54090:00

and we'll we'll be on your homepage. But

## 54090:00 - 54120:00

it's got to do all of it. [snorts]

## 54120:00 - 54145:00

I I don't need a landing page or an

## 54145:00 - 54180:00

infographic. It's not enough.

## 54180:00 - 54210:00

>> It's not enough. I know there's other

## 54210:00 - 54235:00

questions in the chat. We'll do this.

## 54235:00 - 54255:00

We're trying to do these every other

## 54255:00 - 54325:00

week. In the meantime, we are I would I

## 54325:00 - 54365:00

don't know something like 70ish days

## 54365:00 - 54410:00

away from SAS annual. So we'll hopefully

## 54410:00 - 54455:00

see you guys there. We will talk a lot

## 54455:00 - 54490:00

more about our agents there. We've got

## 54490:00 - 54550:00

some of the best of breed AI native apps

## 54550:00 - 54585:00

coming. Their CEOs are coming to speak.

## 54585:00 - 54600:00

So, it'll be a lot. We're doing

## 54600:00 - 54630:00

>> deploy. They'll have everyone there to

## 54630:00 - 54650:00

teach you how to do this stuff, too.

## 54650:00 - 54660:00

>> Yes, for real.

## 54660:00 - 54690:00

>> They'll have the CEOs of Replet and

## 54690:00 - 54740:00

Lovable and the CO of Versel and all

## 54740:00 - 54775:00

these great people and, you know, CTO of

## 54775:00 - 54800:00

Data Bricks. It's all great. But we'll

## 54800:00 - 54825:00

have people hands-on showing you how to

## 54825:00 - 54845:00

do these agents, answering your

## 54845:00 - 54880:00

questions. You can you can pepper them

## 54880:00 - 54920:00

until they fall fall down exhausted

## 54920:00 - 54950:00

because that in fact our whole first day

## 54950:00 - 54985:00

is deploy and it's I mean it'll be all

## 54985:00 - 55015:00

the but the whole point of the first day

## 55015:00 - 55030:00

is to help you deploy these agents

## 55030:00 - 55060:00

yourself if you have it or to fix your

## 55060:00 - 55090:00

issues. That's the whole point. So it'll

## 55090:00 - 55105:00

be great.

## 55105:00 - 55115:00

>> See you guys in a minute.

## 55115:00 - 55145:00

>> We'll go we'll go deeper there and then

## 55145:00 - 55180:00

yeah we'll see you on here next time and

## 55180:00 - 55215:00

thanks everybody for joining.

## 55215:00 - 55240:00

>> Thanks Ailia.

## 55240:00 - 55330:00

>> Thanks everyone.

## 55330:00 - 55360:00

Hey Sasker. Imagine having agents for

## 55360:00 - 55400:00

every support task. One that triages

## 55400:00 - 55425:00

tickets, another that catches

## 55425:00 - 55460:00

duplicates, one that spots turn risk.

## 55460:00 - 55490:00

That'd be pretty amazing, right? Happy

## 55490:00 - 55525:00

Fox just made it real with autopilot.

## 55525:00 - 55565:00

These pre-built AI agents deploy in

## 55565:00 - 55605:00

about 60 seconds and run for as low as 2

## 55605:00 - 55645:00

cents per successful action. All of it

## 55645:00 - 55675:00

sits inside the Happy Fox omni [music]

## 55675:00 - 55725:00

channel AI first support stack, chatbot,

## 55725:00 - 55770:00

co-pilot, and autopilot working as one.

## 55770:00+

Check them out at happyypox.com/taster.

