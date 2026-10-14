---
source: https://www.youtube.com/watch?v=z7T1pCxgvlA
title: "Why most AI products fail: Lessons from 50+ AI deployments at OpenAI,
  Google & Amazon"
author: Lenny's Podcast
date: 2026-01-11
views: 42036
description: |-
  Aishwarya Naresh Reganti and Kiriti Badam have helped build and launch more than 50 enterprise AI products across companies like OpenAI, Google, Amazon, and Databricks. Based on these experiences, they’ve developed a small set of best practices for building and scaling successful AI products. The goal of this conversation is to save you and your team a lot of pain and suffering.

  *We discuss:*
  1. Two key ways AI products differ from traditional software, and why that fundamentally changes how they should be built
  2. Common patterns and anti-patterns in companies that build strong AI products versus those that struggle
  3. A framework they developed from real-world experience to iteratively build AI products that create a flywheel of improvement
  4. Why obsessing about customer trust and reliability is an underrated driver of successful AI products
  5. Why evals aren’t a cure-all, and the most common misconceptions people have about them
  6. The skills that matter most for builders in the AI era

  *Get 15% off Aishwarya and Kiriti’s Maven course, Building Agentic AI Applications with a Problem-First Approach, using this link:* https://bit.ly/3V5XJFp

  *Brought to you by:*
  Merge—The fastest way to ship 220+ integrations: https://merge.dev/lenny
  Strella—The AI-powered customer research platform: https://strella.io/lenny
  Brex—The banking solution for startups: https://www.brex.com/product/business-account?ref_code=bmk_dp_brand1H25_ln_new_fs

  *Episode transcript:* https://www.lennysnewsletter.com/p/what-openai-and-google-engineers-learned
  *Archive of all Lenny's Podcast transcripts:* https://www.dropbox.com/scl/fo/yxi4s2w998p1gvtpu4193/AMdNPR8AOw0lMklwtnC0TrQ?rlkey=j06x0nipoti519e0xgm23zsn9&st=4jmgl11w&dl=0

  *My biggest takeaways (for paid newsletter subscribers):* https://www.lennysnewsletter.com/i/183007822/referenced

  *Where to find Aishwarya Naresh Reganti:*
  • LinkedIn: https://www.linkedin.com/in/areganti
  • GitHub: https://github.com/aishwaryanr/awesome-generative-ai-guide
  • X: https://x.com/aish_reganti

  *Where to find Kiriti Badam:*
  • LinkedIn: https://www.linkedin.com/in/sai-kiriti-badam
  • X: https://x.com/kiritibadam

  *Where to find Lenny:*
  • Newsletter: https://www.lennysnewsletter.com
  • X: https://twitter.com/lennysan
  • LinkedIn: https://www.linkedin.com/in/lennyrachitsky/

  *In this episode, we cover:*
  (00:00) Introduction to Aishwarya and Kiriti
  (05:03) Challenges in AI product development
  (07:36) Key differences between AI and traditional software
  (13:19) Building AI products: start small and scale
  (15:23) The importance of human control in AI systems
  (22:38) Avoiding prompt injection and jailbreaking
  (25:18) Patterns for successful AI product development
  (33:20) The debate on evals and production monitoring
  (41:27) Codex team’s approach to evals and customer feedback
  (45:41) Continuous calibration, continuous development (CC/CD) framework
  (58:07) Emerging patterns and calibration
  (01:01:24) Overhyped and under-hyped AI concepts
  (01:05:17) The future of AI
  (01:08:41) Skills and best practices for building AI products
  (01:14:04) Lightning round and final thoughts

  *Referenced:*
  • LevelUp Labs: https://levelup-labs.ai/
  • Why your AI product needs a different development lifecycle: https://www.lennysnewsletter.com/p/why-your-ai-product-needs-a-different
  • Booking.com: https://www.booking.com
  • Research paper on agents in production (by Matei Zaharia’s lab): https://arxiv.org/pdf/2512.04123
  • Matei Zaharia’s research on Google Scholar: https://scholar.google.com/citations?user=I1EvjZsAAAAJ&hl=en
  • The coming AI security crisis (and what to do about it) | Sander Schulhoff: https://www.lennysnewsletter.com/p/the-coming-ai-security-crisis
  • Gajen Kandiah on LinkedIn: https://www.linkedin.com/in/gajenkandiah
  • Rackspace: https://www.rackspace.com
  • The AI-native startup: 5 products, 7-figure revenue, 100% AI-written code | Dan Shipper (co-founder/CEO of Every): https://www.lennysnewsletter.com/p/inside-every-dan-shipper
  • Semantic Diffusion: https://martinfowler.com/bliki/SemanticDiffusion.html
  • LMArena: https://lmarena.ai
  • Artificial Analysis: https://artificialanalysis.ai/leaderboards/providers
  • Why humans are AI’s biggest bottleneck (and what’s coming in 2026) | Alexander Embiricos (OpenAI Codex Product Lead): https://www.lennysnewsletter.com/p/why-humans-are-ais-biggest-bottleneck
  • Airline held liable for its chatbot giving passenger bad advice—what this means for travellers: https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know
  • Demis Hassabis on LinkedIn: https://www.linkedin.com/in/demishassabis
  ...References continued at: https://www.lennysnewsletter.com/p/what-openai-and-google-engineers-learned

  _Production and marketing by https://penname.co/._
  _For inquiries about sponsoring the podcast, email podcast@lennyrachitsky.com._

  Lenny may be an investor in the companies discussed.
tags: []
extraction_method: youtube-transcript
grabbed_at: 2026-04-05T12:39:10.368Z
---

# Why most AI products fail: Lessons from 50+ AI deployments at OpenAI, Google & Amazon

## 00:00 - 25:00

We worked on a guest post together had

## 25:00 - 70:00

this really key insight that building AI

## 70:00 - 110:00

products is very different from building

## 110:00 - 135:00

nonAI products.

## 135:00 - 155:00

>> Most people tend to ignore the

## 155:00 - 185:00

non-determinism. You don't know how the

## 185:00 - 210:00

user might behave with your product and

## 210:00 - 245:00

you also don't know how the LLM might

## 245:00 - 280:00

respond to that. The second difference

## 280:00 - 315:00

is the agency control trade-off. Every

## 315:00 - 350:00

time you hand over decision-m

## 350:00 - 385:00

capabilities to agentic systems, you're

## 385:00 - 415:00

kind of relinquishing some amount of

## 415:00 - 430:00

control on your end.

## 430:00 - 450:00

>> This significantly changes the way you

## 450:00 - 470:00

should be building product. So we

## 470:00 - 500:00

recommend building step by step. When

## 500:00 - 540:00

you start small, it forces you to think

## 540:00 - 565:00

about what is the problem that I'm going

## 565:00 - 600:00

to solve. In all this advancements of

## 600:00 - 640:00

the AI, one easy slippery slope is to

## 640:00 - 670:00

keep thinking about complexities of the

## 670:00 - 695:00

solution and forget the problem that

## 695:00 - 710:00

you're trying to solve.

## 710:00 - 735:00

>> It's not about being the first company

## 735:00 - 770:00

to have an agent among your competitors.

## 770:00 - 800:00

It's about have you built the right fly

## 800:00 - 825:00

wheels in place so that you can improve

## 825:00 - 835:00

over time.

## 835:00 - 870:00

>> What kind of ways of working do you see

## 870:00 - 905:00

in companies that build AI products

## 905:00 - 940:00

successfully? I used to work with the

## 940:00 - 990:00

CEO of now Rackspace. He would have this

## 990:00 - 1020:00

block every day in the morning which

## 1020:00 - 1055:00

would say catching up with AI 4 to 6:00

## 1055:00 - 1095:00

a.m. Leaders have to get back to being

## 1095:00 - 1125:00

hands-on. You must be comfortable with

## 1125:00 - 1160:00

the fact that your intuions might not be

## 1160:00 - 1190:00

right and you probably are the dumbest

## 1190:00 - 1215:00

person in the room and you want to learn

## 1215:00 - 1225:00

from everyone.

## 1225:00 - 1260:00

>> What do you think the next year of AI is

## 1260:00 - 1275:00

going to look like?

## 1275:00 - 1305:00

>> Persistence is extremely valuable.

## 1305:00 - 1330:00

Successful companies right now building

## 1330:00 - 1365:00

in any new area. They are going through

## 1365:00 - 1400:00

the pain of learning this, implementing

## 1400:00 - 1430:00

this and understanding what works and

## 1430:00 - 1495:00

what doesn't work. Pain is the new mode.

## 1495:00 - 1535:00

Today my guests are Aishwaria Raanti and

## 1535:00 - 1575:00

Kiti Bottom. Kiti works on codecs at

## 1575:00 - 1610:00

OpenAI and has spent the last decade

## 1610:00 - 1650:00

building AI and ML infrastructure at

## 1650:00 - 1690:00

Google and at Kumo. Ash was an early AI

## 1690:00 - 1725:00

researcher at Alexa and Microsoft and

## 1725:00 - 1770:00

has published over 35 research papers.

## 1770:00 - 1805:00

Together, they've led and supported over

## 1805:00 - 1850:00

50 AI product deployments across

## 1850:00 - 1880:00

companies like Amazon, Data Bricks,

## 1880:00 - 1915:00

OpenAI, Google, and both startups and

## 1915:00 - 1950:00

large enterprises. Together, they also

## 1950:00 - 1985:00

teach the number one rated AI course on

## 1985:00 - 2020:00

Maven, where they teach product leaders

## 2020:00 - 2045:00

all of the key lessons they've learned

## 2045:00 - 2085:00

about building successful AI products.

## 2085:00 - 2120:00

The goal of this episode is to save you

## 2120:00 - 2155:00

and your team a lot of pain and

## 2155:00 - 2190:00

suffering and wasted time trying to

## 2190:00 - 2230:00

build your AI product. Whether you are

## 2230:00 - 2255:00

already struggling to make your product

## 2255:00 - 2295:00

work or want to avoid that struggle,

## 2295:00 - 2325:00

this episode is for you. If you enjoy

## 2325:00 - 2345:00

this podcast, don't forget to subscribe

## 2345:00 - 2360:00

and follow it in your favorite

## 2360:00 - 2390:00

podcasting app or YouTube. It helps

## 2390:00 - 2420:00

tremendously. And if you become an

## 2420:00 - 2455:00

annual subscriber of my newsletter, you

## 2455:00 - 2500:00

get a year free of a ton of incredible

## 2500:00 - 2530:00

products, including a year free of

## 2530:00 - 2565:00

lovable, replet, bold, gamma, nad

## 2565:00 - 2600:00

linear, Devon, Postto, Superhum, Dcript,

## 2600:00 - 2625:00

Whisper Flow, Perplexity, Warp, Granola,

## 2625:00 - 2650:00

Magic Pattern, Dracast, Chapter D,

## 2650:00 - 2680:00

Mobit, and Stripe Atlas. Head on over to

## 2680:00 - 2710:00

lenny'snewsletter.com and click product

## 2710:00 - 2750:00

pass. With that, I bring you Awaria

## 2750:00 - 2795:00

Oranti and Kiti bottom after a short

## 2795:00 - 2830:00

word from our sponsors.

## 2830:00 - 2870:00

This episode is brought to you by Merge.

## 2870:00 - 2900:00

Product leaders hate building

## 2900:00 - 2935:00

integrations. They're messy. They're

## 2935:00 - 2970:00

slow to build. They're a huge drain on

## 2970:00 - 2995:00

your road map, and they're definitely

## 2995:00 - 3025:00

not why you got into product in the

## 3025:00 - 3065:00

first place. Lucky for you, Merge is

## 3065:00 - 3100:00

obsessed with integrations. With a

## 3100:00 - 3140:00

single API, B2B SAS companies embed

## 3140:00 - 3185:00

Merge into their product and ship 220

## 3185:00 - 3220:00

plus customerf facing integrations in

## 3220:00 - 3260:00

weeks, not quarters. Think of merge like

## 3260:00 - 3305:00

Plaid, but for everything B2B SAS.

## 3305:00 - 3365:00

Companies like Merall AI, ramp, and use

## 3365:00 - 3390:00

Merge to connect their customers as

## 3390:00 - 3435:00

accounting, HR, ticketing, CRM, and file

## 3435:00 - 3470:00

storage systems to power everything from

## 3470:00 - 3505:00

automatic onboarding to AI ready data

## 3505:00 - 3550:00

pipelines. Even better, Merge now

## 3550:00 - 3575:00

supports the secure deployment of

## 3575:00 - 3605:00

connectors to AI agents with a new

## 3605:00 - 3640:00

product so that you can safely power AI

## 3640:00 - 3675:00

workflows with real customer data. If

## 3675:00 - 3710:00

your product needs customer data from

## 3710:00 - 3760:00

dozens of systems, Merge is the fastest,

## 3760:00 - 3800:00

safest way to get it. Book and attend a

## 3800:00 - 3835:00

meeting at merge.dev/lenny

## 3835:00 - 3875:00

and they'll send you a $50 Amazon gift

## 3875:00 - 3935:00

card. That's merge.dev/lenny.

## 3935:00 - 3960:00

This episode is brought to you by

## 3960:00 - 3995:00

Stella, the customer research platform

## 3995:00 - 4040:00

built for the AI era. Here's the truth

## 4040:00 - 4075:00

about user research. It's never been

## 4075:00 - 4120:00

more important or more painful. Teams

## 4120:00 - 4150:00

want to understand why customers do what

## 4150:00 - 4185:00

they do. But recruiting users, running

## 4185:00 - 4220:00

interviews, and analyzing insights takes

## 4220:00 - 4260:00

weeks. By the time the results are in,

## 4260:00 - 4305:00

the moment to act has passed. Strella

## 4305:00 - 4335:00

changes that. It's the first platform

## 4335:00 - 4380:00

that uses AI to run and analyze in-depth

## 4380:00 - 4415:00

interviews automatically, bringing fast

## 4415:00 - 4450:00

and continuous user research to every

## 4450:00 - 4500:00

team. Strella's AI moderator asks real

## 4500:00 - 4535:00

follow-up questions, probing deeper when

## 4535:00 - 4570:00

answers are vague, and services patterns

## 4570:00 - 4610:00

across hundreds of conversations, all in

## 4610:00 - 4660:00

a few hours, not weeks. Product design

## 4660:00 - 4685:00

and research teams at companies like

## 4685:00 - 4720:00

Amazon and Dualingo are already using

## 4720:00 - 4760:00

Stella for Figma prototype testing,

## 4760:00 - 4795:00

concept validation, and customer journey

## 4795:00 - 4830:00

research, getting insights overnight

## 4830:00 - 4865:00

instead of waiting for the next sprint.

## 4865:00 - 4885:00

If your team wants to understand

## 4885:00 - 4915:00

customers at the speed you ship

## 4915:00 - 4960:00

products, try Strella. Run your next

## 4960:00 - 5005:00

study at strea.io/lenny.

## 5005:00 - 5130:00

That's s t re l.io/lenny.

## 5130:00 - 5180:00

Ash and Kiti, thank you so much for

## 5180:00 - 5225:00

being here and welcome to the podcast.

## 5225:00 - 5250:00

>> Thank you. Thank you for having us.

## 5250:00 - 5275:00

Super excited for this.

## 5275:00 - 5295:00

>> Let me set the stage for the

## 5295:00 - 5310:00

conversation that we're going to have

## 5310:00 - 5370:00

today. So, you two have built a bunch of

## 5370:00 - 5405:00

AI products yourself. You've gone deep

## 5405:00 - 5450:00

with a lot of companies who uh have

## 5450:00 - 5480:00

built AI products, have struggled to

## 5480:00 - 5525:00

build AI products, build AI agents. You

## 5525:00 - 5560:00

also teach a course on building AI

## 5560:00 - 5595:00

products successfully that and you're

## 5595:00 - 5615:00

kind of like on this mission to just

## 5615:00 - 5670:00

reduce pain and suffering and failure uh

## 5670:00 - 5695:00

that you constantly see people go

## 5695:00 - 5720:00

through when they're building AI

## 5720:00 - 5755:00

products. So to set a little just

## 5755:00 - 5780:00

foundation for the conversation we're

## 5780:00 - 5810:00

going to have, what are you seeing on

## 5810:00 - 5850:00

the ground within companies trying to

## 5850:00 - 5890:00

build AI products? What's going well?

## 5890:00 - 5910:00

What's not going well?

## 5910:00 - 5955:00

>> I think 2025 has been significantly

## 5955:00 - 6020:00

different than 2024. one, the skepticism

## 6020:00 - 6060:00

has significantly reduced. Um, there

## 6060:00 - 6090:00

were tons of leaders last year who

## 6090:00 - 6105:00

probably thought this would be yet

## 6105:00 - 6140:00

another crypto wave and kind of

## 6140:00 - 6180:00

skeptical to get started and a lot of

## 6180:00 - 6215:00

the use cases that I saw last year were

## 6215:00 - 6245:00

more of Snapchat on your data, right?

## 6245:00 - 6280:00

and that was, you know, um calling

## 6280:00 - 6320:00

themselves an AI product. And this year,

## 6320:00 - 6350:00

a ton of companies are really rethinking

## 6350:00 - 6385:00

their user experiences and their

## 6385:00 - 6415:00

workflows and all of that and really

## 6415:00 - 6450:00

understanding that you need to

## 6450:00 - 6480:00

deconstruct and reconstruct your

## 6480:00 - 6530:00

processes in order to have a in order to

## 6530:00 - 6560:00

build successful AI products, right? And

## 6560:00 - 6600:00

that's that's the good stuff. The bad

## 6600:00 - 6635:00

stuff is the execution is still all over

## 6635:00 - 6675:00

the place. Um, think of it, right? This

## 6675:00 - 6715:00

is a three-year-old field. There are no

## 6715:00 - 6755:00

play playbooks. there are no textbooks.

## 6755:00 - 6790:00

Um so you really need to figure out as

## 6790:00 - 6840:00

you go and the AI life cycle both

## 6840:00 - 6880:00

pre-eployment and post- deployment is

## 6880:00 - 6905:00

very different as compared to a

## 6905:00 - 6960:00

traditional software life cycle. Um and

## 6960:00 - 6995:00

so so a lot of old contracts and

## 6995:00 - 7030:00

handoffs between traditional roles like

## 7030:00 - 7085:00

say PMs and engineers and data folks has

## 7085:00 - 7130:00

now been broken. It's and people are

## 7130:00 - 7165:00

really getting adapted to this new way

## 7165:00 - 7205:00

of working together and kind of owning

## 7205:00 - 7255:00

the same feedback loop in a way because

## 7255:00 - 7290:00

previously I feel like PMs and engineers

## 7290:00 - 7315:00

and all of these folks had their own

## 7315:00 - 7350:00

feedback loops to optimize and now you

## 7350:00 - 7375:00

need to be probably sitting in the same

## 7375:00 - 7405:00

room. You're probably looking at agent

## 7405:00 - 7445:00

traces together and deciding how your uh

## 7445:00 - 7485:00

product should behave. So it's a tighter

## 7485:00 - 7525:00

form of collaboration. So companies are

## 7525:00 - 7555:00

still kind of figuring that out. That's

## 7555:00 - 7605:00

kind of what I see um in my consulting

## 7605:00 - 7625:00

practice this year.

## 7625:00 - 7650:00

>> So, let me follow that thread. We worked

## 7650:00 - 7675:00

on a guest post together that came out a

## 7675:00 - 7710:00

few months ago. And the thing that stood

## 7710:00 - 7740:00

out to me most that stuck with me most

## 7740:00 - 7775:00

after working on that post is you had

## 7775:00 - 7825:00

this really uh key insight that building

## 7825:00 - 7870:00

AI products is very different from

## 7870:00 - 7905:00

building non-AI products. And the thing

## 7905:00 - 7945:00

that you're big on getting across is

## 7945:00 - 7985:00

there's two very big differences. Talk

## 7985:00 - 8015:00

about those two differences.

## 8015:00 - 8060:00

>> Yes. Um and again I I want to make sure

## 8060:00 - 8110:00

that we drive home the right point. Um

## 8110:00 - 8150:00

there are tons of uh similarities of

## 8150:00 - 8185:00

building AI systems and software systems

## 8185:00 - 8220:00

as well. But then there are some things

## 8220:00 - 8250:00

that kind of fundamentally change the

## 8250:00 - 8300:00

way you build software systems um versus

## 8300:00 - 8330:00

AI systems, right? And one of them that

## 8330:00 - 8360:00

most people tend to ignore is the

## 8360:00 - 8400:00

non-determinism. Uh you're pretty much

## 8400:00 - 8450:00

working with a non-deterministic API as

## 8450:00 - 8495:00

compared to traditional software. What

## 8495:00 - 8520:00

does that mean and why does that have to

## 8520:00 - 8570:00

affect us is in traditional software you

## 8570:00 - 8615:00

pretty much have a very well-mapped

## 8615:00 - 8655:00

decision engine or workflow. Think of

## 8655:00 - 8695:00

something like booking.com right you um

## 8695:00 - 8725:00

you have an intention that uh you want

## 8725:00 - 8755:00

to make a booking in San Francisco for

## 8755:00 - 8805:00

two nights etc. uh the product has kind

## 8805:00 - 8845:00

of been built uh so that your intention

## 8845:00 - 8880:00

can be converted into a particular

## 8880:00 - 8905:00

action and you kind of are clicking

## 8905:00 - 8930:00

through a bunch of buttons, options,

## 8930:00 - 8960:00

forms and all of that and you finally

## 8960:00 - 8995:00

achieve your intention. But now that

## 8995:00 - 9040:00

layer in AI products has completely been

## 9040:00 - 9115:00

replaced by a very fluid um interface

## 9115:00 - 9155:00

which is mostly natural language which

## 9155:00 - 9190:00

means you the user can literally come up

## 9190:00 - 9230:00

with ton of ways of saying uh or

## 9230:00 - 9260:00

communicating their intentions, right?

## 9260:00 - 9285:00

And that kind of changes a lot of things

## 9285:00 - 9320:00

because now you don't know how your user

## 9320:00 - 9355:00

is going to behave. That's on the input

## 9355:00 - 9400:00

side. And the output is also that you're

## 9400:00 - 9430:00

working with a non-deterministic

## 9430:00 - 9490:00

probabilistic API which is your LLM. And

## 9490:00 - 9525:00

LLMs are pretty sensitive to prompt

## 9525:00 - 9555:00

phrasings and they're pretty much black

## 9555:00 - 9585:00

boxes. So you don't even know how the

## 9585:00 - 9615:00

output surface will look like, right? So

## 9615:00 - 9650:00

this um you don't know how the user

## 9650:00 - 9680:00

might behave with your product and you

## 9680:00 - 9710:00

also don't know how the LLM might

## 9710:00 - 9740:00

respond to that. So you're now working

## 9740:00 - 9775:00

with an input, output, and a proc

## 9775:00 - 9815:00

process. And you don't understand all

## 9815:00 - 9835:00

the three very well. You're trying to

## 9835:00 - 9870:00

kind of anticipate behavior and build

## 9870:00 - 9920:00

for it. And with agentic systems, this

## 9920:00 - 9945:00

kind of gets even harder. And that's

## 9945:00 - 9965:00

where we talk about the second

## 9965:00 - 10005:00

difference, which is the agency control

## 10005:00 - 10060:00

trade-off. Right? What we mean by that,

## 10060:00 - 10100:00

and I'm kind of shocked. So many people

## 10100:00 - 10135:00

don't talk about this. They're extremely

## 10135:00 - 10160:00

obsessed with building autonomous

## 10160:00 - 10190:00

systems, agents can that can do work for

## 10190:00 - 10230:00

you. But every time you hand over

## 10230:00 - 10270:00

decision-m capabilities or autonomy to

## 10270:00 - 10305:00

agentic systems, you're kind of

## 10305:00 - 10335:00

relinquishing some amount of control on

## 10335:00 - 10365:00

your end, right? And when you do that,

## 10365:00 - 10395:00

you want to make sure that your agent

## 10395:00 - 10440:00

has um caning your trust or it is

## 10440:00 - 10470:00

reliable enough that you can allow it to

## 10470:00 - 10500:00

make decisions. And that's where we talk

## 10500:00 - 10540:00

about this agency control trade-off

## 10540:00 - 10585:00

which is if you give your AI agent or

## 10585:00 - 10615:00

your AI system whatever it is more

## 10615:00 - 10645:00

agency which is the ability to make

## 10645:00 - 10695:00

decisions you're also um losing some

## 10695:00 - 10725:00

control and you want to make sure that

## 10725:00 - 10785:00

the agent or the AI system has earned um

## 10785:00 - 10820:00

that ability or has built up trust over

## 10820:00 - 10830:00

time.

## 10830:00 - 10865:00

>> So just to summarize what you're sharing

## 10865:00 - 10900:00

here essentially people have been

## 10900:00 - 10935:00

building product software products for a

## 10935:00 - 10975:00

long time. We're now in a world where

## 10975:00 - 11015:00

the software you're building is one

## 11015:00 - 11050:00

non-deterministic can just do things

## 11050:00 - 11080:00

differently like you know as you said

## 11080:00 - 11100:00

you go to booking.com you find a hotel

## 11100:00 - 11120:00

it's going to be the same experience

## 11120:00 - 11140:00

every time you'll see different hotels

## 11140:00 - 11170:00

but it's a predictable experience with

## 11170:00 - 11210:00

AI you can't predict that it's going to

## 11210:00 - 11230:00

be the exact same thing the thing that

## 11230:00 - 11275:00

you uh plan it to be every time and then

## 11275:00 - 11300:00

the other is there's this trade-off

## 11300:00 - 11340:00

between agency and control how much will

## 11340:00 - 11370:00

the AI do for you versus how much should

## 11370:00 - 11420:00

the person still be in charge and the

## 11420:00 - 11445:00

what I'm hearing is the big point here

## 11445:00 - 11465:00

is significantly changes the way you

## 11465:00 - 11485:00

should be building product and we're

## 11485:00 - 11525:00

going to talk about the impact on how

## 11525:00 - 11555:00

the product development life cycle

## 11555:00 - 11600:00

should change as a result. Is there

## 11600:00 - 11615:00

anything else you want to add there

## 11615:00 - 11665:00

before we get into into that? Yeah, it's

## 11665:00 - 11690:00

definitely like one of the key points

## 11690:00 - 11730:00

that uh this kind of distinction needs

## 11730:00 - 11770:00

to exist in your mind like when you're

## 11770:00 - 11800:00

starting to build. For example, think

## 11800:00 - 11835:00

about if your like objective is to hike

## 11835:00 - 11875:00

uh half term inity, right? You don't

## 11875:00 - 11910:00

start hiking it every day, but you start

## 11910:00 - 11940:00

you know training yourself for like you

## 11940:00 - 11980:00

know in in minor parts and then you

## 11980:00 - 12005:00

slowly improve and then like you go to

## 12005:00 - 12035:00

the end goal, right? I feel like that's

## 12035:00 - 12065:00

extremely similar to what you want to

## 12065:00 - 12105:00

build AI products in the sense that when

## 12105:00 - 12135:00

you don't start with like agents with

## 12135:00 - 12165:00

all the tools and all the context that

## 12165:00 - 12200:00

you have in the company in day one and

## 12200:00 - 12230:00

expect it to work or like you don't even

## 12230:00 - 12260:00

tinker at that level. You need to be

## 12260:00 - 12300:00

deliberately starting in places where

## 12300:00 - 12335:00

there is minimal impact and more human

## 12335:00 - 12365:00

control so that you have like a good

## 12365:00 - 12390:00

grip of what are the current

## 12390:00 - 12425:00

capabilities and what can I do with them

## 12425:00 - 12455:00

and then slowly you know like lean into

## 12455:00 - 12495:00

the more agency and lesser control. So

## 12495:00 - 12535:00

this gives you that confidence that okay

## 12535:00 - 12570:00

I can know that okay this is the

## 12570:00 - 12605:00

particular problem that I'm facing and

## 12605:00 - 12640:00

the AI can solve this extent of it and

## 12640:00 - 12680:00

then like let me next think through what

## 12680:00 - 12705:00

context I need to bring in what kind of

## 12705:00 - 12750:00

tools I need to add to this to improve

## 12750:00 - 12785:00

the uh experience right so I feel like

## 12785:00 - 12820:00

it's also uh it's a good and a bad thing

## 12820:00 - 12855:00

in sense that it's good that you don't

## 12855:00 - 12880:00

have to see the complexity of the

## 12880:00 - 12915:00

outside world of like you know all of

## 12915:00 - 12955:00

this fancy AI agents force and feel like

## 12955:00 - 12990:00

I cannot do that it's always everyone is

## 12990:00 - 13045:00

starting from very uh minimalistic

## 13045:00 - 13075:00

structures and then evolving. And the

## 13075:00 - 13110:00

second part is like it's also good the

## 13110:00 - 13150:00

the bad thing is that as you are like

## 13150:00 - 13180:00

you know trying to build this oneclick

## 13180:00 - 13220:00

agents into your company you don't have

## 13220:00 - 13250:00

to be overwhelmed with this complexity

## 13250:00 - 13280:00

you can like slowly graduate. So that's

## 13280:00 - 13315:00

extremely important and we see this as a

## 13315:00 - 13340:00

repeating pattern over and over.

## 13340:00 - 13355:00

>> Okay. All right. So, let's actually

## 13355:00 - 13380:00

follow that, right? Cuz that's a really

## 13380:00 - 13415:00

important component of how you recommend

## 13415:00 - 13455:00

people build AI stuff. AI stuff, AI

## 13455:00 - 13490:00

products, AI agents, all the AI things.

## 13490:00 - 13530:00

Um, so give us an example what you're

## 13530:00 - 13550:00

talking about here. This idea of

## 13550:00 - 13575:00

starting

## 13575:00 - 13620:00

uh slow with agency and control and then

## 13620:00 - 13645:00

moving kind of up this rung.

## 13645:00 - 13685:00

>> Yeah. For example, a very important or

## 13685:00 - 13730:00

like very prevalent uh application of AI

## 13730:00 - 13765:00

agents is like customer support, right?

## 13765:00 - 13805:00

Uh imagine like you are a company who

## 13805:00 - 13835:00

has like a lot of customer support

## 13835:00 - 13880:00

tickets and why even imagine like OpenAF

## 13880:00 - 13915:00

faced the exact same thing when we were

## 13915:00 - 13950:00

launching products and there was like a

## 13950:00 - 14000:00

huge spike of uh support volume as like

## 14000:00 - 14020:00

you know we launch successful products

## 14020:00 - 14070:00

like image and or uh you know like GPD5

## 14070:00 - 14095:00

and things like that the kind of

## 14095:00 - 14125:00

questions you get is different the kind

## 14125:00 - 14160:00

of like you know u problems that the

## 14160:00 - 14195:00

customers bring to you is different. So

## 14195:00 - 14245:00

it's not about just like dumping all the

## 14245:00 - 14275:00

uh list of help center articles that you

## 14275:00 - 14310:00

have into the AI agent. you kind of

## 14310:00 - 14340:00

understand what are the things that you

## 14340:00 - 14380:00

can build and so initially the first

## 14380:00 - 14420:00

step of it would be something like uh

## 14420:00 - 14450:00

you have your support agents the human

## 14450:00 - 14470:00

support agents but you will be

## 14470:00 - 14505:00

suggesting uh in terms of okay this is

## 14505:00 - 14545:00

what the AI thinks that is the right

## 14545:00 - 14575:00

thing to do and then you get that

## 14575:00 - 14610:00

feedback loop from the humans that okay

## 14610:00 - 14635:00

this is actually a good suggestion for

## 14635:00 - 14660:00

me in this particular case and this is a

## 14660:00 - 14690:00

bad suggestion and then you can go back

## 14690:00 - 14750:00

and understand okay uh this is what the

## 14750:00 - 14780:00

drawbacks are or this is where the blind

## 14780:00 - 14815:00

spots are and then how do I fix that?

## 14815:00 - 14840:00

And once you get that you can increase

## 14840:00 - 14875:00

the autonomy to say that okay I don't

## 14875:00 - 14905:00

need to suggest to the human I'll

## 14905:00 - 14950:00

actually show the uh show the answer

## 14950:00 - 14985:00

directly to the customers to the

## 14985:00 - 15025:00

customer and then we can actually add

## 15025:00 - 15065:00

more complexity in terms of okay uh I

## 15065:00 - 15105:00

was only answering questions based on

## 15105:00 - 15130:00

health center articles but now let me

## 15130:00 - 15165:00

add new functionality like I can

## 15165:00 - 15195:00

actually issue refunds to the customers

## 15195:00 - 15220:00

I can actually raise feature requests

## 15220:00 - 15245:00

with the engineering team and all of

## 15245:00 - 15270:00

these things. So if you start all with

## 15270:00 - 15300:00

all of this on day one, it's incredibly

## 15300:00 - 15335:00

hard to control the complexity. So we

## 15335:00 - 15365:00

recommend like you know building step by

## 15365:00 - 15390:00

step and then increasing it.

## 15390:00 - 15415:00

>> Awesome. And you have a visual actually

## 15415:00 - 15460:00

that we'll share of what this looks

## 15460:00 - 15485:00

like. But just to kind of mirror back

## 15485:00 - 15510:00

what you're describing this idea of

## 15510:00 - 15555:00

start with high control, low agency in

## 15555:00 - 15590:00

your the example you gave is the support

## 15590:00 - 15635:00

agent is just kind of giving suggestions

## 15635:00 - 15695:00

is not able to do anything. the user is

## 15695:00 - 15745:00

in charge. And then as that becomes

## 15745:00 - 15785:00

useful and you are confident it's doing

## 15785:00 - 15825:00

the right sort of work, you give it a

## 15825:00 - 15865:00

little more agency and you kind of pull

## 15865:00 - 15900:00

back on the control the user has. And

## 15900:00 - 15930:00

then if that's starting to go well, then

## 15930:00 - 15960:00

you give it more agency and the user

## 15960:00 - 16015:00

needs less control to control it.

## 16015:00 - 16030:00

>> Awesome.

## 16030:00 - 16085:00

>> I I think the higher level idea here is

## 16085:00 - 16140:00

with AI systems, it's all about behavior

## 16140:00 - 16190:00

calibration. It's incredibly impossible

## 16190:00 - 16225:00

to predict up front how your system

## 16225:00 - 16270:00

behaves. Now what do you do about it?

## 16270:00 - 16315:00

You make sure that you don't ruin your

## 16315:00 - 16350:00

customer experience or your end user

## 16350:00 - 16400:00

experience. Um you keep that as is but

## 16400:00 - 16430:00

then remove the amount of control that

## 16430:00 - 16490:00

the human has and there is no single

## 16490:00 - 16530:00

right way of doing it. You can decide

## 16530:00 - 16570:00

how to constrain that autonomy. Right?

## 16570:00 - 16620:00

Um, a very I mean a different example of

## 16620:00 - 16660:00

how you could constrain autonomy is

## 16660:00 - 16705:00

pre-authorization use cases. Insurance

## 16705:00 - 16735:00

pre-authorization is a very ripe use

## 16735:00 - 16790:00

case for AI because uh clinicians spend

## 16790:00 - 16845:00

a lot of time um pre-authorizing

## 16845:00 - 16885:00

uh things like blood tests, MRIs and

## 16885:00 - 16910:00

things like that, right? And there are

## 16910:00 - 16950:00

some cases which are more of lowhanging

## 16950:00 - 16985:00

fruits. for instance, MRIs and blood

## 16985:00 - 17020:00

tests because um as soon as you know

## 17020:00 - 17050:00

patients information, it's easier to

## 17050:00 - 17110:00

approve that and AI could do that versus

## 17110:00 - 17140:00

something like an invasive surgery, etc.

## 17140:00 - 17170:00

is more high-risk. You don't want to be

## 17170:00 - 17205:00

doing that autonomously. So, you can

## 17205:00 - 17240:00

kind of determine which of these use

## 17240:00 - 17270:00

cases should go through that human and

## 17270:00 - 17295:00

the loop layer versus which of the use

## 17295:00 - 17335:00

cases AI can conveniently handle. And

## 17335:00 - 17360:00

then all through this process, you're

## 17360:00 - 17395:00

also logging what the human is doing,

## 17395:00 - 17420:00

right? because you want to build a

## 17420:00 - 17475:00

flywheel um that you could use in order

## 17475:00 - 17530:00

to improve your system. Um so you're

## 17530:00 - 17565:00

essentially um not ruining the user

## 17565:00 - 17610:00

experience, not eroding trust at the

## 17610:00 - 17645:00

same time logging what humans would

## 17645:00 - 17665:00

otherwise do so that you can

## 17665:00 - 17695:00

continuously improve your system.

## 17695:00 - 17720:00

>> So let me let me give you a few more

## 17720:00 - 17745:00

examples of this kind of progression

## 17745:00 - 17770:00

that you recommend. And this the reason

## 17770:00 - 17790:00

I'm spending so much time here is this

## 17790:00 - 17820:00

is a really key part of your

## 17820:00 - 17860:00

recommendation to help people build more

## 17860:00 - 17905:00

successful AI products. this idea of

## 17905:00 - 17960:00

start slow with high control and low

## 17960:00 - 17990:00

agency and then build up over time once

## 17990:00 - 18010:00

you've built confidence that it's doing

## 18010:00 - 18035:00

the right sort of work. So a few more

## 18035:00 - 18055:00

examples that you shared in your post

## 18055:00 - 18085:00

that I'll just read. So say you're

## 18085:00 - 18125:00

building a coding assistant. V1 would be

## 18125:00 - 18150:00

just suggest inline completion and

## 18150:00 - 18185:00

boilerplate snippets. V2 would be

## 18185:00 - 18220:00

generate larger blocks like tests or

## 18220:00 - 18255:00

refactors for humans to review. And then

## 18255:00 - 18290:00

V3 is just apply the changes and open

## 18290:00 - 18330:00

PRs autonomously.

## 18330:00 - 18355:00

And then another example is a marketing

## 18355:00 - 18390:00

assistant. So V1 would be draft emails

## 18390:00 - 18420:00

or social copy just like here's what I

## 18420:00 - 18465:00

would do. V2 is build a multi-step

## 18465:00 - 18510:00

campaign and run the campaign and then

## 18510:00 - 18550:00

launch and V3 is just launch it AB test

## 18550:00 - 18575:00

it autooptimize campaigns across

## 18575:00 - 18605:00

channels.

## 18605:00 - 18610:00

>> Awesome.

## 18610:00 - 18630:00

>> Yeah.

## 18630:00 - 18665:00

>> And and again just to summarize where

## 18665:00 - 18695:00

we're at just to give people the the

## 18695:00 - 18745:00

advice we've shared so far. Uh one is

## 18745:00 - 18785:00

just important to understand AI products

## 18785:00 - 18795:00

are different. They're

## 18795:00 - 18820:00

non-deterministic. And he pointed out

## 18820:00 - 18845:00

and I forgot to actually mirror back

## 18845:00 - 18880:00

this point both on the in on the input

## 18880:00 - 18915:00

and the output the user experience is

## 18915:00 - 18950:00

nondeterministic like people will see

## 18950:00 - 18980:00

different things different outputs

## 18980:00 - 19005:00

different chat conversations different

## 19005:00 - 19035:00

maybe UI if it's designing the UI for

## 19035:00 - 19060:00

you and also the output obviously is

## 19060:00 - 19090:00

going to be nondeterministic so that's a

## 19090:00 - 19130:00

problem and a challenge and then uh

## 19130:00 - 19165:00

>> I mean if you think of it it's also the

## 19165:00 - 19215:00

most beautiful part of AI which is I

## 19215:00 - 19255:00

mean we're all much more comfortable

## 19255:00 - 19290:00

talking than following a bunch of

## 19290:00 - 19315:00

buttons and all of that right? So the

## 19315:00 - 19365:00

bar to using AI products is much lower

## 19365:00 - 19395:00

because you can be as natural as you

## 19395:00 - 19425:00

would be with humans. But that's also

## 19425:00 - 19465:00

the problem which is there are tons of

## 19465:00 - 19515:00

ways we communicate. Um and it's you

## 19515:00 - 19540:00

want to make sure that that intent is

## 19540:00 - 19565:00

rightly communicated and the right

## 19565:00 - 19590:00

actions are taken because most of your

## 19590:00 - 19635:00

systems are deterministic and you want

## 19635:00 - 19680:00

to achieve a deterministic outcome uh

## 19680:00 - 19710:00

but with non-deterministic technology

## 19710:00 - 19745:00

and that's where it gets a little messy.

## 19745:00 - 19775:00

>> Awesome. Okay. That's a I love I love

## 19775:00 - 19830:00

the the optimistic version of the why

## 19830:00 - 19860:00

this is good. Okay. And then the other

## 19860:00 - 19890:00

piece is this idea of this trade-off of

## 19890:00 - 19920:00

autonomy versus control when you're

## 19920:00 - 19945:00

designing a thing. And what I imagine

## 19945:00 - 19970:00

what you're seeing is people try to jump

## 19970:00 - 20030:00

to the ideal like the V3 immediately and

## 20030:00 - 20055:00

that's when they get into trouble both.

## 20055:00 - 20075:00

It's probably a lot harder to build that

## 20075:00 - 20100:00

and it's just doesn't work and then

## 20100:00 - 20120:00

they're just like okay this is a

## 20120:00 - 20145:00

failure. What are we even doing?

## 20145:00 - 20175:00

>> Exactly. I feel there's like a bunch of

## 20175:00 - 20225:00

things that you actually have to uh get

## 20225:00 - 20265:00

confidence in before you get to V3 and

## 20265:00 - 20295:00

it's it's easy to get overwhelmed that

## 20295:00 - 20330:00

oh my AI agent is like doing these

## 20330:00 - 20365:00

things wrong in like 100 different ways

## 20365:00 - 20385:00

and you're not going to actually

## 20385:00 - 20420:00

tabulate all of them and fix it right

## 20420:00 - 20445:00

even though you've learned like you know

## 20445:00 - 20485:00

how do you deal with the uh evaluation

## 20485:00 - 20515:00

practices and stuff like that. If you're

## 20515:00 - 20545:00

starting on the wrong spot you are

## 20545:00 - 20570:00

actually going to have a hard time like

## 20570:00 - 20595:00

you know correcting things from there.

## 20595:00 - 20640:00

And when you start uh small and when you

## 20640:00 - 20675:00

start with building like a very

## 20675:00 - 20715:00

minimalistic version with high human

## 20715:00 - 20755:00

control and low agency, it also forces

## 20755:00 - 20790:00

you to think about what is the problem

## 20790:00 - 20830:00

that I'm going to solve. uh we we use

## 20830:00 - 20890:00

this term called problem first and uh to

## 20890:00 - 20920:00

me it was like obvious in the sense that

## 20920:00 - 20945:00

yeah I I do need to think about the

## 20945:00 - 20980:00

problem but it's incredible how well it

## 20980:00 - 21020:00

resonates with the people that in all

## 21020:00 - 21050:00

this advancements of the AI that we are

## 21050:00 - 21095:00

seeing one easy slippery slope is to

## 21095:00 - 21130:00

just keep thinking about uh complexities

## 21130:00 - 21160:00

of the solution and not and forget the

## 21160:00 - 21185:00

problem that you're trying to solve. So

## 21185:00 - 21225:00

when you're trying to start at like a

## 21225:00 - 21275:00

small at a smaller scale of autonomy,

## 21275:00 - 21305:00

you start to really think about what is

## 21305:00 - 21330:00

the problem that I'm trying to solve and

## 21330:00 - 21370:00

how do I break it down into like levels

## 21370:00 - 21405:00

of autonomy that I can build later. So

## 21405:00 - 21450:00

that is incredibly useful when like and

## 21450:00 - 21475:00

we keep repeating this pattern over and

## 21475:00 - 21520:00

over with everyone we talk to.

## 21520:00 - 21555:00

And there's so many other benefits to uh

## 21555:00 - 21595:00

limiting autonomy because there there's

## 21595:00 - 21625:00

just danger also of the thing doing too

## 21625:00 - 21675:00

much for you and just messing up your I

## 21675:00 - 21700:00

don't know your database sending out all

## 21700:00 - 21725:00

these emails you never expected. There's

## 21725:00 - 21745:00

like so many reasons this is a good

## 21745:00 - 21755:00

idea.

## 21755:00 - 21800:00

>> Yep. I I recently read this paper from a

## 21800:00 - 21855:00

bunch of folks at UC Berkeley. um

## 21855:00 - 21900:00

basically mate Zahara Stoker and the

## 21900:00 - 21960:00

folks at data bricks and it said about

## 21960:00 - 22010:00

74 or 75% of the enterprises that they

## 22010:00 - 22045:00

had spoken to um their biggest problem

## 22045:00 - 22080:00

was reliability and that's also why they

## 22080:00 - 22135:00

weren't uh comfortable um deploying

## 22135:00 - 22175:00

products to their end users or building

## 22175:00 - 22205:00

customerf facing products because they

## 22205:00 - 22255:00

just weren't sure or they just weren't

## 22255:00 - 22295:00

um comfortable doing that and exposing

## 22295:00 - 22325:00

their users to a bunch of these risks,

## 22325:00 - 22375:00

right? And that's also why they think a

## 22375:00 - 22410:00

lot of AI products today have to do with

## 22410:00 - 22445:00

productivity because it's much low

## 22445:00 - 22485:00

autonomy versus you know end to end

## 22485:00 - 22520:00

agents that would replace workflows. Um

## 22520:00 - 22550:00

and yeah I love their work otherwise as

## 22550:00 - 22585:00

well but I think that's very in line

## 22585:00 - 22625:00

with what um at least we're seeing at my

## 22625:00 - 22645:00

startup as well.

## 22645:00 - 22670:00

>> Okay very interesting. There's an

## 22670:00 - 22695:00

episode that'll come out before this

## 22695:00 - 22725:00

conversation where we go deep into

## 22725:00 - 22775:00

another problem that this avoids which

## 22775:00 - 22805:00

is around uh prompt injection and

## 22805:00 - 22850:00

jailbreaking and just how big of a

## 22850:00 - 22895:00

>> uh ex risk that is for AI products where

## 22895:00 - 22920:00

it's essentially an unsolved and

## 22920:00 - 22950:00

unsolvable problem potentially. I'm not

## 22950:00 - 22975:00

going to go down that track, but that's

## 22975:00 - 23005:00

uh it's a pretty scary conversation we

## 23005:00 - 23025:00

had that it'll be out before this

## 23025:00 - 23040:00

conversation.

## 23040:00 - 23080:00

>> I think that will be a huge problem once

## 23080:00 - 23120:00

systems go mainstream. We're still so

## 23120:00 - 23150:00

busy building AI products that we're not

## 23150:00 - 23205:00

worried about security, but it it will

## 23205:00 - 23255:00

be um such a huge problem to kind of u

## 23255:00 - 23290:00

especially with this non-deterministic

## 23290:00 - 23330:00

API again, right? So, you're kind of

## 23330:00 - 23360:00

stuck because um there are tons of

## 23360:00 - 23405:00

instructions that you could inject

## 23405:00 - 23445:00

within your prompt and then yeah, it's

## 23445:00 - 23485:00

it's going to be bad. Okay, I let's

## 23485:00 - 23500:00

actually spend a little time here

## 23500:00 - 23520:00

because it's actually really interesting

## 23520:00 - 23540:00

to me and no one's talking about this

## 23540:00 - 23590:00

stuff which is like the conversation we

## 23590:00 - 23620:00

had is just it's pretty easy to get AI

## 23620:00 - 23660:00

to trick to do stuff it shouldn't do and

## 23660:00 - 23690:00

there's all these guardrail systems

## 23690:00 - 23725:00

people put in place but turns out these

## 23725:00 - 23755:00

guardrails aren't actually very good and

## 23755:00 - 23785:00

you can always get around them and to

## 23785:00 - 23810:00

your point as agents become more

## 23810:00 - 23860:00

autonomous and robots uh it gets pretty

## 23860:00 - 23885:00

scary that you could get AI to do things

## 23885:00 - 23920:00

you shouldn't do. I think this is

## 23920:00 - 23960:00

definitely a problem. But I feel in the

## 23960:00 - 23985:00

current spectrum of like customers

## 23985:00 - 24055:00

adopting AI, the the extent to which

## 24055:00 - 24090:00

like you know companies can actually get

## 24090:00 - 24125:00

advantage of AI or like improve their

## 24125:00 - 24160:00

processes or like you know streamline

## 24160:00 - 24205:00

the existing processes that they have. I

## 24205:00 - 24235:00

feel it's in still in the very early

## 24235:00 - 24265:00

stage like 2025 has been an extremely

## 24265:00 - 24320:00

busy year for AI agents and customers

## 24320:00 - 24350:00

trying to adopt AI. But I feel the

## 24350:00 - 24390:00

penetration is still not as much as you

## 24390:00 - 24425:00

would actually get advantage out of it.

## 24425:00 - 24470:00

So with the right sort of you know human

## 24470:00 - 24515:00

in the loop uh points in here I feel we

## 24515:00 - 24540:00

can actually avoid a bunch of these

## 24540:00 - 24580:00

things and focus more towards like

## 24580:00 - 24625:00

streamlining the processes and I I am

## 24625:00 - 24650:00

more on the optimist side in the sense

## 24650:00 - 24690:00

that like you need to try and adopt this

## 24690:00 - 24740:00

before actually like trying to be only

## 24740:00 - 24775:00

highlighting the negative aspects of

## 24775:00 - 24805:00

like what could go wrong. So I I feel

## 24805:00 - 24855:00

like strongly u that companies has to

## 24855:00 - 24890:00

adopt this. They definitely like no

## 24890:00 - 24950:00

company uh at openi we talked to is has

## 24950:00 - 24980:00

never had been the case that oh AI

## 24980:00 - 25005:00

cannot help me in this case. It has

## 25005:00 - 25030:00

always been that oh there is this like

## 25030:00 - 25065:00

set of things that it can uh optimize

## 25065:00 - 25090:00

for me and then let me see how I can

## 25090:00 - 25125:00

adopt it. Sweet. I always like the

## 25125:00 - 25160:00

optimistic perspective. I'm excited to

## 25160:00 - 25180:00

for you to listen to this and see what

## 25180:00 - 25195:00

you think because it's really

## 25195:00 - 25220:00

interesting and uh and to your point

## 25220:00 - 25240:00

there's a lot of things to focus on.

## 25240:00 - 25275:00

It's one of one of many things to worry

## 25275:00 - 25310:00

about and think about. Okay, let's get

## 25310:00 - 25340:00

back on track here. So, we've shared a

## 25340:00 - 25370:00

bunch of pro tips and important piece of

## 25370:00 - 25425:00

advice. Let me ask, what other patterns

## 25425:00 - 25475:00

and kind of ways of working do you see

## 25475:00 - 25510:00

in companies that do this well and teams

## 25510:00 - 25565:00

that build AI products successfully? And

## 25565:00 - 25585:00

then just what are the most common

## 25585:00 - 25615:00

pitfalls people fall into? So, we could

## 25615:00 - 25655:00

just maybe start with what are other

## 25655:00 - 25690:00

ways that companies do this well, build

## 25690:00 - 25745:00

AI products successfully? I almost think

## 25745:00 - 25800:00

of it as like a success triangle with

## 25800:00 - 25840:00

three dimensions. It's never always

## 25840:00 - 25875:00

technical. Every technology problem is a

## 25875:00 - 25915:00

people problem first. And with companies

## 25915:00 - 25955:00

that we have worked with, it's these

## 25955:00 - 25980:00

three dimensions, right? Like great

## 25980:00 - 26025:00

leaders, good culture and technical

## 26025:00 - 26090:00

progress. Um with leaders itself, we

## 26090:00 - 26120:00

work with a lot of companies uh for

## 26120:00 - 26150:00

their AI transformation, training,

## 26150:00 - 26200:00

strategy and stuff like that. And I feel

## 26200:00 - 26260:00

like um a lot of companies the leaders

## 26260:00 - 26290:00

have built intuitions over 10 or 15

## 26290:00 - 26320:00

years and they are kind of highly

## 26320:00 - 26355:00

regarded for those intuions but now with

## 26355:00 - 26400:00

AI in the picture those intuions will

## 26400:00 - 26435:00

have to be relearned and leaders have to

## 26435:00 - 26475:00

be vulnerable to do that right. Um I

## 26475:00 - 26510:00

used to work with the CEO of now

## 26510:00 - 26585:00

Rackspace Gajen. So he would um have

## 26585:00 - 26610:00

this block every day in the morning

## 26610:00 - 26650:00

which would say catching up with AI 4 to

## 26650:00 - 26690:00

6:00 a.m. and he would not have any

## 26690:00 - 26715:00

meetings or anything like that and that

## 26715:00 - 26740:00

was just his time to pick up on the

## 26740:00 - 26785:00

latest AI um you know podcast or

## 26785:00 - 26820:00

information and all of that and he would

## 26820:00 - 26855:00

have um weekend white coding sessions

## 26855:00 - 26895:00

and stuff like that. So I think leaders

## 26895:00 - 26940:00

have to get back to being hands-on and

## 26940:00 - 26965:00

that's not because they have to be

## 26965:00 - 27000:00

implementing these things but more of uh

## 27000:00 - 27040:00

rebuilding their intuitions because you

## 27040:00 - 27065:00

must be comfortable with the fact that

## 27065:00 - 27100:00

your intuitions might not be right. Um

## 27100:00 - 27135:00

and you you probably are the dumbest

## 27135:00 - 27155:00

person in the room and you want to learn

## 27155:00 - 27200:00

from everyone. Um and that I've seen

## 27200:00 - 27245:00

that being a very um distinguishing

## 27245:00 - 27300:00

factor of companies that build products

## 27300:00 - 27320:00

um which are successful because you're

## 27320:00 - 27345:00

kind of bringing in that top down

## 27345:00 - 27395:00

approach. It's almost always impossible

## 27395:00 - 27435:00

for it to be bottom up. You can't have a

## 27435:00 - 27475:00

bunch of engineers go and get buyin from

## 27475:00 - 27500:00

the leader if they just don't trust in

## 27500:00 - 27530:00

the technology or if they have

## 27530:00 - 27565:00

misaligned expectations about the

## 27565:00 - 27595:00

technology. Right? I've heard from so

## 27595:00 - 27630:00

many folks who are building that our

## 27630:00 - 27660:00

leaders just don't understand the extent

## 27660:00 - 27690:00

to which AI can solve a particular

## 27690:00 - 27720:00

problem or they just white code

## 27720:00 - 27745:00

something and assume it's easy to take

## 27745:00 - 27770:00

it to production and you really need to

## 27770:00 - 27800:00

understand the range of what AI can

## 27800:00 - 27825:00

solve today so that you can guide

## 27825:00 - 27865:00

decisions within the company. The second

## 27865:00 - 27915:00

one is the culture itself, right? And

## 27915:00 - 27960:00

again, I work with enterprises where AI

## 27960:00 - 28005:00

is not their main thing and they have um

## 28005:00 - 28030:00

they need to bring in AI into their

## 28030:00 - 28060:00

processes just because a competitor is

## 28060:00 - 28090:00

doing it and just because it does make

## 28090:00 - 28120:00

sense because there are use cases that

## 28120:00 - 28165:00

are very ripe. Then along the way, I

## 28165:00 - 28190:00

feel a lot of companies have this

## 28190:00 - 28235:00

culture of FOMO and you will be replaced

## 28235:00 - 28260:00

and those kind of things and people get

## 28260:00 - 28310:00

really afraid. um subject matter experts

## 28310:00 - 28350:00

are such a huge part of building AI

## 28350:00 - 28375:00

products that work because you really

## 28375:00 - 28405:00

need to consult them to understand how

## 28405:00 - 28440:00

your AI is behaving or what the ideal

## 28440:00 - 28470:00

behavior should be. But then I have

## 28470:00 - 28505:00

spoken to a bunch of companies where the

## 28505:00 - 28525:00

subject matter experts just don't want

## 28525:00 - 28560:00

to talk to you because they think their

## 28560:00 - 28610:00

job is being replaced. So as I mean

## 28610:00 - 28635:00

again this comes from the leader itself.

## 28635:00 - 28680:00

want to build a culture of empowerment

## 28680:00 - 28730:00

of um augmenting AI into your own

## 28730:00 - 28775:00

workflows so that you know you can 10x

## 28775:00 - 28805:00

what you're doing instead of saying that

## 28805:00 - 28840:00

you know probably uh you'll be replaced

## 28840:00 - 28865:00

if you don't adopt AI and stuff like

## 28865:00 - 28890:00

that. So that kind of an empowering

## 28890:00 - 28945:00

culture always helps you want to make um

## 28945:00 - 28985:00

your entire organization be in it

## 28985:00 - 29015:00

together and make AI work for you

## 29015:00 - 29050:00

instead of trying to you know guard

## 29050:00 - 29095:00

their own jobs etc. And with AI, it's

## 29095:00 - 29130:00

also true that it opens up a lot more

## 29130:00 - 29165:00

opportunities than before. So you could

## 29165:00 - 29195:00

have your employees doing a lot more

## 29195:00 - 29225:00

things than before and 10x their

## 29225:00 - 29265:00

productivity. Um, and the third one is

## 29265:00 - 29300:00

the technical part which we talk about,

## 29300:00 - 29345:00

right? I think folks that are successful

## 29345:00 - 29390:00

are incredibly obsessed about

## 29390:00 - 29425:00

understanding their workflows very well

## 29425:00 - 29500:00

and augmenting parts um that could be um

## 29500:00 - 29545:00

um that could be ripe for AI versus the

## 29545:00 - 29575:00

ones that might need human in the loop

## 29575:00 - 29625:00

somewhere etc. Whenever you're uh trying

## 29625:00 - 29670:00

to automate some part of a workflow,

## 29670:00 - 29715:00

it's never the case that you could you

## 29715:00 - 29740:00

could use an AI agent and that will kind

## 29740:00 - 29785:00

of solve your uh problems, right? It's

## 29785:00 - 29820:00

always you probably have a machine

## 29820:00 - 29850:00

learning uh model that's going to do

## 29850:00 - 29865:00

some part of the job. You have

## 29865:00 - 29890:00

deterministic code doing some part of

## 29890:00 - 29925:00

the job. So you really need to be

## 29925:00 - 29945:00

obsessed with understanding that

## 29945:00 - 29970:00

workflow so you can choose the right

## 29970:00 - 29995:00

tool for the problem instead of being

## 29995:00 - 30050:00

obsessed with the technology itself. And

## 30050:00 - 30115:00

um another pattern I see is also folks

## 30115:00 - 30150:00

really understand this idea of working

## 30150:00 - 30190:00

with a non-deterministic API which is

## 30190:00 - 30235:00

your LLM. And what that means is they

## 30235:00 - 30265:00

also understand the development life

## 30265:00 - 30305:00

cycle looks very different and they

## 30305:00 - 30345:00

iterate pretty quickly which is can I um

## 30345:00 - 30390:00

can I build something iterate uh quickly

## 30390:00 - 30425:00

in a way that it doesn't ruin my

## 30425:00 - 30455:00

customer experience at the same time

## 30455:00 - 30500:00

gives me enough amount of data so that I

## 30500:00 - 30525:00

can estimate behavior right so they

## 30525:00 - 30570:00

build that flywheel very quickly as of

## 30570:00 - 30600:00

today it's not about being the first

## 30600:00 - 30630:00

company to have an agent among your

## 30630:00 - 30655:00

competitors it's about have you built

## 30655:00 - 30685:00

the right flywheels in place so that you

## 30685:00 - 30710:00

can improve over time

## 30710:00 - 30735:00

When someone comes up to me and says,

## 30735:00 - 30765:00

"We have this one-click agent. It's

## 30765:00 - 30790:00

going to be deployed in your system and

## 30790:00 - 30825:00

then in two or three days it'll start

## 30825:00 - 30865:00

showing you significant gains," I would

## 30865:00 - 30895:00

almost be skeptical because it's just

## 30895:00 - 30930:00

not possible. And that's not because the

## 30930:00 - 30960:00

models aren't there, but because

## 30960:00 - 30995:00

enterprise data and infrastructure is

## 30995:00 - 31040:00

very messy and you need a bit to even

## 31040:00 - 31080:00

the agent needs a bit to understand um

## 31080:00 - 31120:00

how these systems work. There are very

## 31120:00 - 31175:00

messy taxonomies everywhere. um people

## 31175:00 - 31220:00

tend to do things like get customer data

## 31220:00 - 31255:00

wi1 get customer data w2 and these kind

## 31255:00 - 31300:00

of things and all those functions exist

## 31300:00 - 31340:00

and um they are being called and there's

## 31340:00 - 31365:00

basically there's a lot of tech debt

## 31365:00 - 31400:00

that you need to deal with. So most of

## 31400:00 - 31435:00

the times if you're obsessed with the

## 31435:00 - 31475:00

problem itself and you understand your

## 31475:00 - 31510:00

workflows very well you will know how to

## 31510:00 - 31545:00

improve your agents over time instead of

## 31545:00 - 31575:00

just slapping an agent and assuming that

## 31575:00 - 31615:00

it'll work from day one. I probably will

## 31615:00 - 31640:00

go as far to say that if someone's

## 31640:00 - 31670:00

selling you one click agents, it's it's

## 31670:00 - 31700:00

pure marketing. You don't want to buy

## 31700:00 - 31730:00

into that. I would rather go with a

## 31730:00 - 31750:00

company that says we're going to build

## 31750:00 - 31795:00

this pipeline for you and that that will

## 31795:00 - 31820:00

learn over time and kind of build a

## 31820:00 - 31855:00

flywheel to improve than something

## 31855:00 - 31890:00

that's going to work out of the box to

## 31890:00 - 31940:00

replace any critical workflow or to um

## 31940:00 - 31965:00

build something that can give you

## 31965:00 - 32010:00

significant ROI easily takes four to six

## 32010:00 - 32035:00

months of work. Even if you have the

## 32035:00 - 32075:00

best data layer and infrastructure

## 32075:00 - 32110:00

layer. Amazing. There's a lot there that

## 32110:00 - 32130:00

resonates so deeply with other

## 32130:00 - 32150:00

conversations I've been having on this

## 32150:00 - 32200:00

podcast. One is just for a company to be

## 32200:00 - 32230:00

successful at seeing a lot of impact

## 32230:00 - 32285:00

from AI, the founder CEO has to be deep

## 32285:00 - 32325:00

into it. Uh I had Dan Shipper on the

## 32325:00 - 32360:00

podcast and they work with a bunch of

## 32360:00 - 32385:00

companies helping them adopt AI and he

## 32385:00 - 32410:00

said that's the number one predictor of

## 32410:00 - 32450:00

success is the CEO chatting with Chad

## 32450:00 - 32505:00

GPT, Claude, whatever uh many times a

## 32505:00 - 32535:00

day. I love this example you gave the

## 32535:00 - 32575:00

Rackspace as like catch up on AI news in

## 32575:00 - 32610:00

the morning every day. I was imagining

## 32610:00 - 32645:00

he'd be like chatting with like the

## 32645:00 - 32700:00

chatbot versus uh like reading news.

## 32700:00 - 32725:00

>> With the kind of information you have as

## 32725:00 - 32775:00

of today, you could just um I mean you

## 32775:00 - 32820:00

want to choose the right um channels as

## 32820:00 - 32855:00

well because everybody has an opinion.

## 32855:00 - 32890:00

So whose opinion do you want to bank on?

## 32890:00 - 32945:00

I feel like having that good quality set

## 32945:00 - 32970:00

of people that you're listening to

## 32970:00 - 33005:00

really makes sense. So he just has a

## 33005:00 - 33040:00

list of two or three sources that he

## 33040:00 - 33075:00

always looks at and and then he comes

## 33075:00 - 33100:00

back with a bunch of questions and

## 33100:00 - 33130:00

bounces it around with a bunch of AI

## 33130:00 - 33160:00

experts to see what they think about it.

## 33160:00 - 33190:00

And I was part of that group so I kind

## 33190:00 - 33200:00

of know um

## 33200:00 - 33215:00

>> I love that

## 33215:00 - 33235:00

>> about the questions that he comes up

## 33235:00 - 33250:00

with. So that's cool.

## 33250:00 - 33280:00

>> It's pretty cool. I was like why are you

## 33280:00 - 33310:00

doing so much? And then he says it

## 33310:00 - 33335:00

trickles down into a bunch of decisions

## 33335:00 - 33355:00

that we take.

## 33355:00 - 33385:00

>> Okay, let me talk about another topic

## 33385:00 - 33410:00

that's very it's been a hot topic on

## 33410:00 - 33435:00

this podcast. It was a hot topic on

## 33435:00 - 33485:00

Twitter for a while. Evals.

## 33485:00 - 33530:00

A lot of people are obsessed with evals,

## 33530:00 - 33555:00

think they're the solution to a lot of

## 33555:00 - 33590:00

problems in AI. A lot of people think

## 33590:00 - 33620:00

they're overrated, that well, you don't

## 33620:00 - 33660:00

need evals. You can just feel the vibes

## 33660:00 - 33695:00

and you'll you'll be all right. What's

## 33695:00 - 33735:00

your take on evals? How far does that

## 33735:00 - 33765:00

take people in solving a lot of the

## 33765:00 - 33800:00

problems that you talk about in terms of

## 33800:00 - 33835:00

like what is going on in the community?

## 33835:00 - 33880:00

I I feel there's this false dichotomy of

## 33880:00 - 33920:00

like there's either eval is going to

## 33920:00 - 33960:00

solve everything or online monitoring or

## 33960:00 - 33985:00

production monitoring is going to solve

## 33985:00 - 34030:00

everything and I find no reason to trust

## 34030:00 - 34065:00

like one of the extremes in the sense

## 34065:00 - 34110:00

that I will entirely bank my application

## 34110:00 - 34160:00

on this and or like that to solve the uh

## 34160:00 - 34195:00

thing right so if you take a step back

## 34195:00 - 34245:00

uh think of what are eval are basically

## 34245:00 - 34305:00

your uh trusted product thinking or like

## 34305:00 - 34340:00

your knowledge about the product that is

## 34340:00 - 34380:00

going into this uh set of data sets that

## 34380:00 - 34405:00

you're going to build in the sense that

## 34405:00 - 34435:00

this is what matters to me like this is

## 34435:00 - 34480:00

the kind of problems that my agent

## 34480:00 - 34520:00

should not do and let me build a list of

## 34520:00 - 34550:00

data sets so that I'm going to do well

## 34550:00 - 34585:00

on those and in terms of production

## 34585:00 - 34625:00

monitoring what you're doing doing there

## 34625:00 - 34660:00

is uh you're deploying your application

## 34660:00 - 34690:00

and then you're having this some sort of

## 34690:00 - 34730:00

key metrics that actually communicate

## 34730:00 - 34765:00

back to you on how customers are using

## 34765:00 - 34810:00

your product like you could be deploying

## 34810:00 - 34845:00

uh any agent And like if the C customer

## 34845:00 - 34865:00

is giving a thumbs up for your

## 34865:00 - 34895:00

interaction, you better want to know

## 34895:00 - 34920:00

that. So that is what production

## 34920:00 - 34945:00

monitoring is going to do, right? And

## 34945:00 - 34980:00

this production monitoring has existed

## 34980:00 - 35020:00

for products like for a long time just

## 35020:00 - 35055:00

that now with AI agents, you need to be

## 35055:00 - 35110:00

monitoring like a lot more granularity.

## 35110:00 - 35135:00

It's not just the customer always giving

## 35135:00 - 35175:00

you explicit feedback, but there is many

## 35175:00 - 35210:00

implicit feedback that you can get. Uh

## 35210:00 - 35240:00

for example, in chat GPD, right? Like if

## 35240:00 - 35275:00

you are uh liking the answer you can

## 35275:00 - 35300:00

actually give a thumbs up or if you

## 35300:00 - 35320:00

don't like the answer sometimes

## 35320:00 - 35350:00

customers don't give you thumbs down but

## 35350:00 - 35390:00

actually re regenerate the answer. So

## 35390:00 - 35425:00

that is an clear indication that the

## 35425:00 - 35455:00

initial answer that you generated is not

## 35455:00 - 35495:00

matting uh meeting the customer's

## 35495:00 - 35530:00

expectation. Right. So these are the

## 35530:00 - 35570:00

kind of implicit signals you always need

## 35570:00 - 35605:00

to think about and that spectrum has

## 35605:00 - 35630:00

been increasing in terms of production

## 35630:00 - 35670:00

monitoring. Now let's come back to the

## 35670:00 - 35710:00

initial topic of like okay is it eval or

## 35710:00 - 35740:00

is it production monitoring? What does

## 35740:00 - 35785:00

it matter? So I feel again we go back to

## 35785:00 - 35825:00

this problem first approach of what is

## 35825:00 - 35850:00

your what is it that you're trying to

## 35850:00 - 35870:00

build like you're trying to build a

## 35870:00 - 35905:00

reliable application for your customers

## 35905:00 - 35940:00

that's not going to do a bad thing like

## 35940:00 - 35965:00

it's always going to do the right thing

## 35965:00 - 36005:00

or if it is doing a wrong thing you are

## 36005:00 - 36050:00

uh you're basically alerted like very

## 36050:00 - 36095:00

quickly right so the I break this down

## 36095:00 - 36135:00

into two parts like one is you like

## 36135:00 - 36185:00

nobody goes into uh deploying an

## 36185:00 - 36215:00

application without actually like you

## 36215:00 - 36245:00

know just testing that this testing

## 36245:00 - 36280:00

could be wipes or this testing could be

## 36280:00 - 36315:00

okay I have this like 10 questions that

## 36315:00 - 36350:00

it should not go wrong any no matter

## 36350:00 - 36380:00

what changes I make and let me build

## 36380:00 - 36405:00

this and let's call this an evaluation

## 36405:00 - 36445:00

data set now let's say you built this

## 36445:00 - 36480:00

you deployed this and then you figured

## 36480:00 - 36505:00

uh okay now I need to understand whether

## 36505:00 - 36545:00

it's doing the right thing or not so if

## 36545:00 - 36585:00

you're a high uh high uh throughput or

## 36585:00 - 36630:00

like a high transaction customer you

## 36630:00 - 36670:00

cannot practically sit and evaluate all

## 36670:00 - 36700:00

the traces right you need some

## 36700:00 - 36730:00

indication to understand what are the

## 36730:00 - 36755:00

things that I should look at and this is

## 36755:00 - 36780:00

where production monitoring comes into

## 36780:00 - 36825:00

the picture that you cannot predict your

## 36825:00 - 36850:00

uh the base in which your agent could be

## 36850:00 - 36880:00

doing wrong but all of these other

## 36880:00 - 36920:00

implicit signals and explicit signals

## 36920:00 - 36945:00

those are going to communicate back to

## 36945:00 - 36990:00

you what uh what are the traces that you

## 36990:00 - 37010:00

need to look at and that is where

## 37010:00 - 37045:00

production monitoring helps and once you

## 37045:00 - 37095:00

get this kind of traces you need to

## 37095:00 - 37120:00

examine what are the failure patterns

## 37120:00 - 37155:00

that you're seeing in these uh different

## 37155:00 - 37190:00

types of interactions and is there

## 37190:00 - 37220:00

something that I really care about that

## 37220:00 - 37250:00

should not happen and if that kind of

## 37250:00 - 37280:00

failure modes are happening then I need

## 37280:00 - 37310:00

to think about building an evaluation

## 37310:00 - 37355:00

data set for it and okay let's say I

## 37355:00 - 37385:00

built an evaluation data set for my

## 37385:00 - 37455:00

agent trying to offer refunds where

## 37455:00 - 37490:00

explicitly I have configured it not to

## 37490:00 - 37530:00

so I built this evaluation data set and

## 37530:00 - 37570:00

then like I made my changes in tools or

## 37570:00 - 37605:00

prompts or whatever and then I deployed

## 37605:00 - 37635:00

the second version of the product right

## 37635:00 - 37680:00

now uh there is no guarantee that this

## 37680:00 - 37700:00

is the only problem that you're going to

## 37700:00 - 37735:00

see you still need production monitoring

## 37735:00 - 37770:00

to actually have like you know catch

## 37770:00 - 37790:00

different kinds of problems that you

## 37790:00 - 37830:00

might encounter. So I feel eval are

## 37830:00 - 37855:00

important, production monitoring is

## 37855:00 - 37890:00

important but this notion of only one of

## 37890:00 - 37925:00

them is going to solve things for you

## 37925:00 - 37965:00

that is uh completely dismissible in my

## 37965:00 - 37975:00

opinion.

## 37975:00 - 38005:00

>> All right, a very reasonable answer and

## 38005:00 - 38040:00

the point here isn't uh it's not just as

## 38040:00 - 38075:00

simple as do both. It's more that there

## 38075:00 - 38135:00

are different things to catch and one

## 38135:00 - 38165:00

approach won't catch all the things you

## 38165:00 - 38190:00

need to be paying attention to.

## 38190:00 - 38215:00

>> Exactly. Awesome.

## 38215:00 - 38250:00

>> I want to take two steps back and kind

## 38250:00 - 38300:00

of talk about how much weight the term

## 38300:00 - 38345:00

evals has had to take in the second, you

## 38345:00 - 38385:00

know, half of 2025

## 38385:00 - 38415:00

because you go meet a data labeling

## 38415:00 - 38445:00

company and they tell you our experts

## 38445:00 - 38490:00

are writing evals. And then uh you have

## 38490:00 - 38530:00

all of these uh folks saying that PMS

## 38530:00 - 38550:00

should be writing evals. They're the new

## 38550:00 - 38590:00

PRDS. And then you have folks saying

## 38590:00 - 38630:00

that um eval is pretty much everything

## 38630:00 - 38650:00

which is the feedback loop you're

## 38650:00 - 38675:00

supposed to be building to improve your

## 38675:00 - 38720:00

products. Now step back as a beginner

## 38720:00 - 38755:00

and kind of think like what are evals?

## 38755:00 - 38785:00

Why is everyone saying eval? And these

## 38785:00 - 38805:00

are actually different parts of the

## 38805:00 - 38840:00

process and nobody's wrong in the sense

## 38840:00 - 38880:00

that yes these are eval but when a data

## 38880:00 - 38920:00

labeling company is telling you that our

## 38920:00 - 38945:00

um experts are writing evals they're

## 38945:00 - 38990:00

actually referring to error analysis or

## 38990:00 - 39020:00

you know experts just leading notes on

## 39020:00 - 39050:00

what should be right. Lawyers and

## 39050:00 - 39085:00

doctors write evals that doesn't mean

## 39085:00 - 39115:00

they're building LLM judges or they're

## 39115:00 - 39155:00

building this entire feedback loop. And

## 39155:00 - 39190:00

when you say that a PM should be writing

## 39190:00 - 39220:00

evals doesn't mean they have to write an

## 39220:00 - 39250:00

LLM judge that's good enough for

## 39250:00 - 39290:00

production. I think there's there are

## 39290:00 - 39330:00

also very prescriptive ways of doing

## 39330:00 - 39380:00

this and plus one to KD which is you

## 39380:00 - 39420:00

cannot predict up front if you need to

## 39420:00 - 39450:00

be building an LLM judge versus you need

## 39450:00 - 39485:00

to be using um implicit signals from

## 39485:00 - 39535:00

production monitoring etc. I think

## 39535:00 - 39565:00

Martin Fowler at some point had this

## 39565:00 - 39605:00

term called semantic diffusion back in

## 39605:00 - 39655:00

the 2000s. Um um which kind of means

## 39655:00 - 39675:00

that someone comes up with a term

## 39675:00 - 39705:00

everybody starts butchering it with

## 39705:00 - 39730:00

their own definitions and then you kind

## 39730:00 - 39765:00

of lose the actual definition of it.

## 39765:00 - 39795:00

That is kind of what is happening to

## 39795:00 - 39835:00

eval

## 39835:00 - 39865:00

of today. Everybody kind of sees a

## 39865:00 - 39905:00

different side to it I guess. Um but if

## 39905:00 - 39930:00

you make a bunch of practitioners sit

## 39930:00 - 39960:00

together and ask them is it important to

## 39960:00 - 40015:00

build a actionable feedback loop for AI

## 40015:00 - 40045:00

products I think all of them will agree.

## 40045:00 - 40090:00

Now how you do that really depends on

## 40090:00 - 40130:00

your application itself when you go to

## 40130:00 - 40165:00

complex use cases it's incredibly hard

## 40165:00 - 40205:00

to build LM judges because you see a lot

## 40205:00 - 40235:00

of emerging patterns. If you built a

## 40235:00 - 40280:00

judge that would um you know test for

## 40280:00 - 40310:00

verbosity or something like that, you

## 40310:00 - 40345:00

turns out that you're seeing newer

## 40345:00 - 40370:00

patterns that your LM judge is not able

## 40370:00 - 40410:00

to catch and then you're just um you

## 40410:00 - 40445:00

just end up building too many evals and

## 40445:00 - 40480:00

at that point it just makes sense to you

## 40480:00 - 40505:00

know look at your user signals, fix

## 40505:00 - 40535:00

them, check if you've regressed and move

## 40535:00 - 40560:00

on instead of actually building these

## 40560:00 - 40615:00

judges. Um so it all depends. I think

## 40615:00 - 40650:00

one statement that every ML practitioner

## 40650:00 - 40690:00

will tell you is it really depends on

## 40690:00 - 40725:00

the context. Don't be obsessed with

## 40725:00 - 40750:00

prescriptions. They're going to change.

## 40750:00 - 40780:00

>> Uh that's such an important point. This

## 40780:00 - 40810:00

idea that especially that eval just

## 40810:00 - 40840:00

means many things to different people

## 40840:00 - 40870:00

now. It's just like a term for so many

## 40870:00 - 40915:00

things. And uh it it's complicated to

## 40915:00 - 40940:00

just talk about evals when you're think

## 40940:00 - 40965:00

when you see it as the stuff data

## 40965:00 - 40985:00

labeling companies are giving you and

## 40985:00 - 41010:00

things are right. And there's also

## 41010:00 - 41030:00

benchmarks. People call benchmarks a

## 41030:00 - 41050:00

little bit eval. It's like

## 41050:00 - 41085:00

>> I I recently spoke to a client who told

## 41085:00 - 41110:00

me we do eval

## 41110:00 - 41140:00

>> and I was like okay can you show me your

## 41140:00 - 41165:00

data set? and said, "No, we just checked

## 41165:00 - 41205:00

LM arena and artificial analysis. These

## 41205:00 - 41240:00

are, you know, independent benchmarks

## 41240:00 - 41280:00

and we know that this model is the right

## 41280:00 - 41300:00

one for our use case." And I'm like,

## 41300:00 - 41330:00

"You're not doing eval. That's not eval.

## 41330:00 - 41345:00

Those are model."

## 41345:00 - 41365:00

>> That makes sense. Like the word, you

## 41365:00 - 41385:00

know, like could be used in that

## 41385:00 - 41410:00

context. I get why people think that,

## 41410:00 - 41430:00

but yeah, now it's just confusing it

## 41430:00 - 41445:00

even more.

## 41445:00 - 41450:00

>> Yep.

## 41450:00 - 41480:00

>> Just like one more line of questioning

## 41480:00 - 41510:00

here that I think uh that's on my mind

## 41510:00 - 41540:00

is the reason this became kind of a big

## 41540:00 - 41575:00

debate is cloud code, the head of cloud

## 41575:00 - 41605:00

code, Boris, was like, "Nah, we don't do

## 41605:00 - 41645:00

evalance on cloud code. It's all vibes.

## 41645:00 - 41685:00

What can you share kiti on codex and the

## 41685:00 - 41720:00

codeex team of how you approach evals?

## 41720:00 - 41760:00

So CEX we have like this balanced

## 41760:00 - 41785:00

approach of like you know you need to

## 41785:00 - 41830:00

have eval and you need to definitely

## 41830:00 - 41870:00

listen to your customers and I think

## 41870:00 - 41900:00

Alex has been on your podcast recently

## 41900:00 - 41930:00

and he's been talking about how we

## 41930:00 - 41960:00

extremely focused on building the right

## 41960:00 - 42015:00

product right and a part of a big part

## 42015:00 - 42040:00

of it is basically listening to your

## 42040:00 - 42070:00

customers and coding agents are

## 42070:00 - 42110:00

extremely unique compared to agents for

## 42110:00 - 42145:00

other domains in the sense that these

## 42145:00 - 42180:00

are actually built for customizability

## 42180:00 - 42210:00

and these are built for engineers. So

## 42210:00 - 42240:00

coding agent is not a product which is

## 42240:00 - 42270:00

going to solve like these top five

## 42270:00 - 42305:00

workflows or like top six workflows or

## 42305:00 - 42335:00

whatever right it's meant to be

## 42335:00 - 42375:00

customizable in multi different ways and

## 42375:00 - 42420:00

the implication of that is that your

## 42420:00 - 42465:00

product is going to be used in different

## 42465:00 - 42490:00

integrations and different kinds of

## 42490:00 - 42525:00

tools and different kinds of things. So

## 42525:00 - 42550:00

it gets really hard to build an

## 42550:00 - 42595:00

evaluation data set for all kinds of

## 42595:00 - 42625:00

interactions that your customers are

## 42625:00 - 42650:00

going to use your product for. Right?

## 42650:00 - 42680:00

But that said, you also need to

## 42680:00 - 42710:00

understand that okay, if I'm going to

## 42710:00 - 42735:00

make a change, it's at least not going

## 42735:00 - 42770:00

to like damage something that is really

## 42770:00 - 42805:00

core to the product. So we have like

## 42805:00 - 42850:00

evaluations uh for doing that. At the

## 42850:00 - 42880:00

same time, we have we take like extreme

## 42880:00 - 42915:00

care on like understanding how the

## 42915:00 - 42955:00

customers are using it. For example,

## 42955:00 - 42990:00

uh we built this code review product

## 42990:00 - 43030:00

recently and uh it has been gaining like

## 43030:00 - 43075:00

extreme amount of traction and uh I feel

## 43075:00 - 43115:00

like many many bugs in OpenAI as well as

## 43115:00 - 43145:00

like even external customers are getting

## 43145:00 - 43175:00

caught with this. And now let's say if

## 43175:00 - 43205:00

I'm making a model change to the course

## 43205:00 - 43260:00

review or like a different kinds of uh

## 43260:00 - 43305:00

RL mechanism that I trained with it and

## 43305:00 - 43335:00

now if I'm going to deploy it I

## 43335:00 - 43375:00

definitely do want to AP test and

## 43375:00 - 43400:00

identify whether it's actually finding

## 43400:00 - 43450:00

the right uh mistakes and are users how

## 43450:00 - 43485:00

are users reacting to it and sometimes

## 43485:00 - 43525:00

like if users do get annoyed by your

## 43525:00 - 43555:00

like you know uh incorrect code riggers

## 43555:00 - 43580:00

they go to the extent of just switching

## 43580:00 - 43610:00

off the product right so those are the

## 43610:00 - 43640:00

signals that you want to look at and

## 43640:00 - 43675:00

make sure that your new changes are

## 43675:00 - 43715:00

doing the right thing and it's extremely

## 43715:00 - 43745:00

hard for us to you know uh think of

## 43745:00 - 43785:00

these kind of scenarios beforehand and

## 43785:00 - 43820:00

uh develop evaluation data sets for it.

## 43820:00 - 43855:00

So I feel like there's a bit of both

## 43855:00 - 43880:00

like there's a lot of wipes and there's

## 43880:00 - 43920:00

a lot of like customer feedback and we

## 43920:00 - 43940:00

are super active on like the social

## 43940:00 - 43980:00

media to understand if anybody's having

## 43980:00 - 44005:00

certain types of problems and quickly

## 44005:00 - 44085:00

fix that. So I feel it's a it's a um how

## 44085:00 - 44110:00

do I put this? It's like a domain of

## 44110:00 - 44150:00

things that you do here. That makes so

## 44150:00 - 44170:00

much sense. Okay, what I'm hearing Codex

## 44170:00 - 44215:00

Pro evals, but it's not enough. You need

## 44215:00 - 44260:00

to Yes. But also, uh, just watch

## 44260:00 - 44290:00

customer behavior and feedback and also

## 44290:00 - 44315:00

there's some vibes just like is this

## 44315:00 - 44355:00

feeling good? Is this as I'm using it

## 44355:00 - 44380:00

generating great code that I'm excited

## 44380:00 - 44405:00

about that I think is great.

## 44405:00 - 44445:00

>> I I don't think like if anybody's coming

## 44445:00 - 44475:00

and saying that like my I have this

## 44475:00 - 44515:00

concrete set of evas that I can like bet

## 44515:00 - 44545:00

my life on and then I don't need to

## 44545:00 - 44580:00

think about anything else like it it's

## 44580:00 - 44600:00

not going to work. And every new model

## 44600:00 - 44635:00

that we're going to launch, we uh get

## 44635:00 - 44660:00

together as a team and like you know

## 44660:00 - 44700:00

test different things each each person

## 44700:00 - 44730:00

is like concentrating on something else

## 44730:00 - 44755:00

and like we have this list of hard

## 44755:00 - 44795:00

problems that we have and we throw that

## 44795:00 - 44825:00

to the model and see how well they are

## 44825:00 - 44865:00

progressing. So it's like uh custom

## 44865:00 - 44895:00

evals for each engineer you would say

## 44895:00 - 44930:00

and just like understand what the uh

## 44930:00 - 44970:00

product is doing in this new model.

## 44970:00 - 45000:00

If you're a founder, the hardest part of

## 45000:00 - 45030:00

starting a company isn't having the

## 45030:00 - 45065:00

idea. It's scaling the business without

## 45065:00 - 45100:00

getting buried in back office work.

## 45100:00 - 45140:00

That's where Brex comes in. Brex is the

## 45140:00 - 45170:00

intelligent finance platform for

## 45170:00 - 45210:00

founders. With Brex, you get high limit

## 45210:00 - 45245:00

corporate cards, easy banking, high

## 45245:00 - 45295:00

yield treasury, plus a team of AI agents

## 45295:00 - 45330:00

that handle manual finance tasks for

## 45330:00 - 45365:00

you. They'll do all the stuff that you

## 45365:00 - 45400:00

don't want to do, like file your

## 45400:00 - 45440:00

expenses, scour transactions for waste,

## 45440:00 - 45485:00

and run reports, all according to your

## 45485:00 - 45530:00

rules. With Brex AI agents, you can move

## 45530:00 - 45570:00

faster while staying in full control.

## 45570:00 - 45605:00

One in three startups in the United

## 45605:00 - 45655:00

States already runs on Brex. You can,

## 45655:00 - 45715:00

too, at brex.com.

## 45715:00 - 45740:00

We've been talking for almost an hour

## 45740:00 - 45780:00

already and we haven't even covered your

## 45780:00 - 45830:00

extremely powerful software development

## 45830:00 - 45865:00

workflow for building AI products that

## 45865:00 - 45885:00

you two developed that you teach in your

## 45885:00 - 45915:00

course that you basically combines all

## 45915:00 - 45955:00

the stuff we've been talking about into

## 45955:00 - 46000:00

a step-by-step approach to building AI

## 46000:00 - 46035:00

products. You call it the continuous

## 46035:00 - 46070:00

calibration, continuous development

## 46070:00 - 46120:00

framework. Let's pull up a visual to

## 46120:00 - 46140:00

show people what the heck we're talking

## 46140:00 - 46165:00

about and then just walk us through what

## 46165:00 - 46200:00

this is, how this works, how teams can

## 46200:00 - 46225:00

shift the way they build their AI

## 46225:00 - 46270:00

products to this approach to help them

## 46270:00 - 46300:00

avoid a lot of pain and suffering.

## 46300:00 - 46350:00

>> Before we go about explaining um the

## 46350:00 - 46395:00

life cycle, a quick story on why Kita

## 46395:00 - 46440:00

and I came up with this is because um

## 46440:00 - 46485:00

there are tons of u uh companies that we

## 46485:00 - 46520:00

keep talking to that have the pressure

## 46520:00 - 46550:00

from their competitors because they're

## 46550:00 - 46575:00

all building agents. we should be

## 46575:00 - 46595:00

building agents that are entirely

## 46595:00 - 46645:00

autonomous. And we I did end up working

## 46645:00 - 46685:00

with a few customers where we built

## 46685:00 - 46725:00

these end-to-end agents. And turns out

## 46725:00 - 46765:00

that because you start off at a place

## 46765:00 - 46805:00

where you don't know how the user might

## 46805:00 - 46830:00

interact with your system and what kind

## 46830:00 - 46865:00

of responses or actions the AI might

## 46865:00 - 46920:00

come up with, it's really hard to fix

## 46920:00 - 46950:00

problems when you have this really huge

## 46950:00 - 46975:00

workflow which is taking four or five

## 46975:00 - 47010:00

steps, making tons of decisions. you're

## 47010:00 - 47055:00

you just you just end up debugging so

## 47055:00 - 47100:00

much and then kind of hot fixing to the

## 47100:00 - 47125:00

point where at at a time we were

## 47125:00 - 47160:00

building for a customer support um use

## 47160:00 - 47195:00

case which is what which is the example

## 47195:00 - 47225:00

that we give in the newsletter as well

## 47225:00 - 47260:00

and we to shut down the product because

## 47260:00 - 47290:00

we were doing so many hot fixes and

## 47290:00 - 47325:00

there was no way we could um count all

## 47325:00 - 47365:00

the emerging or emerging problems that

## 47365:00 - 47400:00

were coming up right and there's also

## 47400:00 - 47465:00

quite some news online um recently I

## 47465:00 - 47515:00

think Air Canada had this thing where um

## 47515:00 - 47550:00

one of their agents predicted or

## 47550:00 - 47590:00

hallucinated a policy um for a refund

## 47590:00 - 47620:00

which was not part of their original

## 47620:00 - 47655:00

playbook and they had to go by it

## 47655:00 - 47695:00

because legal stuff and there have been

## 47695:00 - 47755:00

a ton of really uh scary incidents and

## 47755:00 - 47785:00

that's where the idea comes from right

## 47785:00 - 47825:00

how can you build so that um you don't

## 47825:00 - 47870:00

lose customer trust and you don't end up

## 47870:00 - 47910:00

or your agent or um AI system doesn't

## 47910:00 - 47945:00

end up making decisions that are super

## 47945:00 - 47985:00

dangerous to the company itself at the

## 47985:00 - 48025:00

same time build a flywheel so that you

## 48025:00 - 48055:00

can improve your product as you go right

## 48055:00 - 48080:00

and that's why we came up with this idea

## 48080:00 - 48115:00

of continuous calibration continuous

## 48115:00 - 48155:00

development. The idea is pretty simple

## 48155:00 - 48195:00

which is um we have this right side of

## 48195:00 - 48235:00

the loop which is continuous development

## 48235:00 - 48285:00

uh where you scope capability and curate

## 48285:00 - 48325:00

data essentially get a data set of what

## 48325:00 - 48370:00

your expected inputs are and what um

## 48370:00 - 48400:00

your expected outputs should be looking

## 48400:00 - 48440:00

at. This is a very good exercise before

## 48440:00 - 48475:00

you start building any AI product

## 48475:00 - 48515:00

because many times you figure out that a

## 48515:00 - 48540:00

lot of the folks within the team are

## 48540:00 - 48565:00

just not aligned on how the product

## 48565:00 - 48605:00

should behave and that's where your PMS

## 48605:00 - 48625:00

can really give in a lot more

## 48625:00 - 48650:00

information and your subject matter

## 48650:00 - 48685:00

experts as well. So you have this data

## 48685:00 - 48720:00

set that you know um your AI product

## 48720:00 - 48755:00

should be doing really well on. It's

## 48755:00 - 48785:00

it's not comprehensive but it lets you

## 48785:00 - 48825:00

get started and then you set up the

## 48825:00 - 48855:00

application and then design the right

## 48855:00 - 48895:00

kind of evaluation metrics and I

## 48895:00 - 48930:00

intentionally use the term evaluation

## 48930:00 - 48965:00

metrics although we say eval because I

## 48965:00 - 48990:00

just want to be very specific on what it

## 48990:00 - 49020:00

is because evaluation is a process

## 49020:00 - 49055:00

evaluation metrics are dimensions that

## 49055:00 - 49100:00

you want to focus on um during the

## 49100:00 - 49130:00

process right and then you go about

## 49130:00 - 49180:00

deploying um run your evaluation metrics

## 49180:00 - 49230:00

um and the second part is the continuous

## 49230:00 - 49280:00

calibration which is the part where you

## 49280:00 - 49340:00

understand what um behavior you hadn't

## 49340:00 - 49370:00

expected in the beginning, right?

## 49370:00 - 49410:00

Because when you start the development

## 49410:00 - 49445:00

process, you have this data set that

## 49445:00 - 49490:00

you're optimizing for, but more often

## 49490:00 - 49520:00

than not, you realize that that data set

## 49520:00 - 49560:00

is not comprehensive enough. Um because

## 49560:00 - 49595:00

users start behaving with your systems

## 49595:00 - 49625:00

in ways that you did not predict. And

## 49625:00 - 49645:00

that's where you want to do the

## 49645:00 - 49680:00

calibration piece. Right? I've deployed

## 49680:00 - 49710:00

my system. Now I see that there are

## 49710:00 - 49750:00

patterns that I did not really expect

## 49750:00 - 49790:00

and your evaluation metrics should give

## 49790:00 - 49820:00

you some insight into that into those

## 49820:00 - 49845:00

patterns. But sometimes you figure out

## 49845:00 - 49880:00

that those metrics were also not enough

## 49880:00 - 49905:00

and you probably have new error patterns

## 49905:00 - 49930:00

that you've not thought about and that's

## 49930:00 - 49965:00

where you analyze your behavior, spot

## 49965:00 - 50010:00

error patterns. You apply fixes for

## 50010:00 - 50045:00

issues that you see but you also design

## 50045:00 - 50075:00

newer evaluation metrics. to figure out

## 50075:00 - 50130:00

that they are emerging patterns. And

## 50130:00 - 50165:00

that doesn't mean you should always

## 50165:00 - 50195:00

design evaluation metrics. There are

## 50195:00 - 50225:00

some errors that you can just fix and

## 50225:00 - 50255:00

not really come back to uh because

## 50255:00 - 50285:00

they're very spot errors. For instance,

## 50285:00 - 50325:00

there's a there's a a tool calling error

## 50325:00 - 50360:00

just because your tool wasn't defined

## 50360:00 - 50385:00

well and stuff like that. You can just

## 50385:00 - 50430:00

fix it and move on, right? And this is

## 50430:00 - 50465:00

pretty much how an AI product life cycle

## 50465:00 - 50500:00

would look like. But what we

## 50500:00 - 50535:00

specifically also mention is while

## 50535:00 - 50575:00

you're going through these iterations,

## 50575:00 - 50635:00

try to think of lower agency iterations

## 50635:00 - 50680:00

in the beginning um and higher control

## 50680:00 - 50720:00

iterations. What that means is constrain

## 50720:00 - 50760:00

the number of decisions your AI systems

## 50760:00 - 50805:00

can make and um make sure that they're

## 50805:00 - 50835:00

humans in the loop and then increase

## 50835:00 - 50860:00

that over time because you're kind of

## 50860:00 - 50900:00

building a flywheel of behavior and uh

## 50900:00 - 50935:00

you're understanding what kind of use

## 50935:00 - 50970:00

cases are coming in or how your users

## 50970:00 - 51000:00

are using the system right and one

## 51000:00 - 51025:00

example I think we give in the

## 51025:00 - 51065:00

newsletter itself is um the customer

## 51065:00 - 51105:00

support this is a nice image that kind

## 51105:00 - 51145:00

of shows how you can think of agency and

## 51145:00 - 51185:00

control as two dimensions and each of

## 51185:00 - 51215:00

your versions keep on increasing the

## 51215:00 - 51265:00

agency or the ability of your AI system

## 51265:00 - 51305:00

to make decisions and lower the control

## 51305:00 - 51340:00

as you go. And one example that we give

## 51340:00 - 51400:00

is that of the u customer support agent

## 51400:00 - 51430:00

where you can break it down into three

## 51430:00 - 51465:00

versions. The first version is just

## 51465:00 - 51510:00

routing which is is your agent able to

## 51510:00 - 51550:00

classify and route a particular ticket

## 51550:00 - 51590:00

to the right department. And sometimes

## 51590:00 - 51620:00

when you read this you probably think is

## 51620:00 - 51665:00

it so hard to just do routing? Why can't

## 51665:00 - 51710:00

an agent easily do that? And when you go

## 51710:00 - 51750:00

to enterprises, routing itself can be a

## 51750:00 - 51790:00

super complex problem. Any retail

## 51790:00 - 51820:00

company, any popular retail company that

## 51820:00 - 51850:00

you can think of has hierarchical

## 51850:00 - 51890:00

taxonomies. Most of the times the

## 51890:00 - 51935:00

taxonomies are incredibly messy. I have

## 51935:00 - 51975:00

worked in you know use cases where you

## 51975:00 - 52030:00

probably have taxonomy that says um you

## 52030:00 - 52055:00

know some tax um some kind of hierarchy

## 52055:00 - 52095:00

and then that says shoes and then

## 52095:00 - 52130:00

women's shoes and men's shoes all at the

## 52130:00 - 52170:00

same layer where idea you should be

## 52170:00 - 52200:00

having shoes and then women's shoes and

## 52200:00 - 52235:00

men's shoes should be sub uh you know

## 52235:00 - 52265:00

classes right and then you're like okay

## 52265:00 - 52295:00

fine I could just merge that and you go

## 52295:00 - 52320:00

further and you see that there's also

## 52320:00 - 52350:00

another section under shoes that says

## 52350:00 - 52385:00

for women and for men and it's just not

## 52385:00 - 52430:00

aggregated it's not uh fixed for some

## 52430:00 - 52470:00

reason. So if an agent kind of sees this

## 52470:00 - 52495:00

kind of a taxonomy, what is it supposed

## 52495:00 - 52530:00

to do? Where is it supposed to route and

## 52530:00 - 52560:00

a lot of the times we are not aware of

## 52560:00 - 52590:00

these problems until you actually go

## 52590:00 - 52620:00

about building something and

## 52620:00 - 52665:00

understanding it, right? So um and when

## 52665:00 - 52710:00

these kind of problems um real human

## 52710:00 - 52740:00

agents see these kind of problems, they

## 52740:00 - 52775:00

know what to check next. U maybe they

## 52775:00 - 52825:00

realize that the the node that says for

## 52825:00 - 52860:00

women and for men that's under shoes was

## 52860:00 - 52900:00

last updated in 2019 which means that

## 52900:00 - 52925:00

it's just a dead node that's lying there

## 52925:00 - 52950:00

and not being used. So they kind of know

## 52950:00 - 52980:00

that okay we're supposed to be looking

## 52980:00 - 53010:00

at a different node and stuff like that.

## 53010:00 - 53035:00

And I'm not saying agents cannot

## 53035:00 - 53060:00

understand this or models are not

## 53060:00 - 53085:00

capable enough to understand this, but

## 53085:00 - 53120:00

there are really weird rules within

## 53120:00 - 53160:00

enterprises that are not documented

## 53160:00 - 53205:00

anywhere and you want to um make sure

## 53205:00 - 53240:00

that the agents have all of that context

## 53240:00 - 53265:00

instead of just throwing the problem at

## 53265:00 - 53305:00

them, right? Um yeah. Uh coming back to

## 53305:00 - 53345:00

the versions we had, routing was one

## 53345:00 - 53380:00

where you have really high control

## 53380:00 - 53420:00

because even if your agent routes to the

## 53420:00 - 53450:00

wrong department, humans can take

## 53450:00 - 53485:00

control and you know undo uh those

## 53485:00 - 53530:00

actions. Um and along the way you also

## 53530:00 - 53555:00

figure out that you probably are dealing

## 53555:00 - 53580:00

with a ton of data issues that you need

## 53580:00 - 53630:00

to fix and you know um um u make sure

## 53630:00 - 53655:00

that your data layer is good enough for

## 53655:00 - 53700:00

the agent to function. uh we do is what

## 53700:00 - 53750:00

we said of a co-pilot which is now that

## 53750:00 - 53785:00

you've figured out routing works fine

## 53785:00 - 53815:00

after a few iterations and you fixed all

## 53815:00 - 53850:00

of your data issues, you could go to the

## 53850:00 - 53900:00

next step which is can my agent provide

## 53900:00 - 53945:00

suggestions uh based on some standard

## 53945:00 - 53975:00

operating procedures that we have for

## 53975:00 - 54005:00

the customer support agent, right? And

## 54005:00 - 54045:00

it could just generate a draft that the

## 54045:00 - 54085:00

human can make changes to. And when you

## 54085:00 - 54120:00

do this, you're also logging human

## 54120:00 - 54150:00

behavior, which means that how much of

## 54150:00 - 54190:00

this draft was used by the customer

## 54190:00 - 54230:00

support agent or what was omitted. So

## 54230:00 - 54255:00

you're actually getting error analysis

## 54255:00 - 54295:00

for free when you do this because you're

## 54295:00 - 54315:00

literally logging everything that the

## 54315:00 - 54345:00

user is doing that you could then build

## 54345:00 - 54395:00

back into your flywheel. And then we say

## 54395:00 - 54420:00

post that once you figured out that

## 54420:00 - 54455:00

those drafts look good and most of the

## 54455:00 - 54485:00

times maybe humans are not making too

## 54485:00 - 54515:00

many changes. They're using these drafts

## 54515:00 - 54550:00

as is. That's when you want to go to

## 54550:00 - 54590:00

your end toend resolution assistant that

## 54590:00 - 54635:00

could you know um draft a resolution

## 54635:00 - 54685:00

that could sort the ticket as well right

## 54685:00 - 54730:00

and those are the stages of agency where

## 54730:00 - 54760:00

you start with low agency and then you

## 54760:00 - 54805:00

go up high, right? Um, we also have this

## 54805:00 - 54845:00

really nice table that we put together

## 54845:00 - 54900:00

which is what do you do at each version

## 54900:00 - 54935:00

and what you learn that can enable you

## 54935:00 - 54970:00

to go to the next step and what

## 54970:00 - 54995:00

information do you get that you can feed

## 54995:00 - 55025:00

into the loop. Right? When you're just

## 55025:00 - 55055:00

doing your routing, you have better

## 55055:00 - 55100:00

quality routing data. You also know what

## 55100:00 - 55120:00

kind of prompts you need to be building

## 55120:00 - 55155:00

to improve the routing system.

## 55155:00 - 55190:00

Essentially, you're figuring out your

## 55190:00 - 55235:00

structure for context engineering and um

## 55235:00 - 55260:00

building that flywheel that you want,

## 55260:00 - 55305:00

right? And while I go through this, I

## 55305:00 - 55345:00

want to also be very clear that two

## 55345:00 - 55400:00

things. One is when you build with CCCD

## 55400:00 - 55435:00

in mind, it doesn't mean that you fix

## 55435:00 - 55465:00

the problem all for once. It's possible

## 55465:00 - 55500:00

that you probably gone through V3 and

## 55500:00 - 55530:00

you see a new distribution of data that

## 55530:00 - 55575:00

you never previously imagined. But um

## 55575:00 - 55625:00

this is just one way to lower your risk

## 55625:00 - 55665:00

which is you get enough information

## 55665:00 - 55710:00

about how users behave with your system

## 55710:00 - 55750:00

before going to a point of complete um

## 55750:00 - 55825:00

autonomy. And the second thing is um

## 55825:00 - 55890:00

you're also kind of um building this um

## 55890:00 - 55940:00

you know implicit logging system. Uh a

## 55940:00 - 55965:00

lot of people come and tell us that oh

## 55965:00 - 55990:00

wait there are eval right why do you

## 55990:00 - 56040:00

need something like this? The issue with

## 56040:00 - 56065:00

just building a bunch of evaluation

## 56065:00 - 56110:00

metrics and then having um them in

## 56110:00 - 56150:00

production is evaluation metrics catch

## 56150:00 - 56175:00

only the errors that you're already

## 56175:00 - 56215:00

aware already aware of. But there can be

## 56215:00 - 56245:00

a lot of emerging patterns that you

## 56245:00 - 56285:00

understand only after you put things in

## 56285:00 - 56315:00

production. Right? So for those emerging

## 56315:00 - 56370:00

patterns, you're kind of creating um um

## 56370:00 - 56410:00

you know a low-risk uh kind of a

## 56410:00 - 56445:00

framework so that you could understand

## 56445:00 - 56480:00

user behavior and not really be in a

## 56480:00 - 56500:00

position where there are tons of errors

## 56500:00 - 56530:00

and you're trying to fix all of them at

## 56530:00 - 56570:00

once. And this is not the only way to do

## 56570:00 - 56600:00

it. There are tons of different ways.

## 56600:00 - 56640:00

You want to decide how you constrain

## 56640:00 - 56675:00

your autonomy. It could be based on the

## 56675:00 - 56700:00

number of actions that the agent is

## 56700:00 - 56735:00

taking, which is what we do in this

## 56735:00 - 56760:00

example. It could be based on topic.

## 56760:00 - 56820:00

there just some um domains where it's uh

## 56820:00 - 56855:00

pretty high risk to make a system

## 56855:00 - 56900:00

completely autonomous for um certain

## 56900:00 - 56930:00

decisions but for some other topics it's

## 56930:00 - 56965:00

okay to make them completely autonomous

## 56965:00 - 56990:00

and depending on the complexity of the

## 56990:00 - 57025:00

problem and that's where you really want

## 57025:00 - 57070:00

your product managers your you know um

## 57070:00 - 57105:00

engineers and subject matter experts to

## 57105:00 - 57145:00

align on how to build the system and

## 57145:00 - 57190:00

continuously improve it. The idea is

## 57190:00 - 57240:00

just behavior calibration and not losing

## 57240:00 - 57270:00

user trust as you do that behavior

## 57270:00 - 57285:00

calibration. I guess

## 57285:00 - 57310:00

>> we'll link folks to this actual post if

## 57310:00 - 57330:00

they want to go really deep. You

## 57330:00 - 57355:00

basically go through all of these steps

## 57355:00 - 57400:00

by step a bunch of examples. And the

## 57400:00 - 57435:00

idea here is as you said that like the

## 57435:00 - 57465:00

reason everything about what you're

## 57465:00 - 57505:00

describing here is about making it uh

## 57505:00 - 57540:00

continuous and iterative and kind of

## 57540:00 - 57580:00

moving along this progression of higher

## 57580:00 - 57620:00

autonomy, less control. And this idea of

## 57620:00 - 57645:00

even calling continuous calibration

## 57645:00 - 57675:00

continuous development is communicating

## 57675:00 - 57710:00

it's this kind of iterative process. And

## 57710:00 - 57740:00

just to be clear, this this naming is

## 57740:00 - 57820:00

kind of a owed to uh CI CICD, continuous

## 57820:00 - 57855:00

integration, continuous deployment

## 57855:00 - 57890:00

>> suite. And the idea here is like that

## 57890:00 - 57925:00

this is the version of that for AI where

## 57925:00 - 57950:00

instead of just like integrating into

## 57950:00 - 57975:00

unit tests and deploying constantly,

## 57975:00 - 57985:00

it's

## 57985:00 - 58020:00

>> uh running evals, looking at results,

## 58020:00 - 58055:00

iterating on on the metrics you're

## 58055:00 - 58085:00

watching, figuring out where it's

## 58085:00 - 58125:00

breaking, and iterating on that.

## 58125:00 - 58160:00

Awesome. Okay, so again, we'll point

## 58160:00 - 58185:00

people to this post if they want to go

## 58185:00 - 58215:00

deeper. That was a great overview. Is

## 58215:00 - 58235:00

there anything else before I go in a

## 58235:00 - 58265:00

different topic around this framework

## 58265:00 - 58290:00

specifically that you think is important

## 58290:00 - 58310:00

for people to know?

## 58310:00 - 58340:00

>> I think one of the most common questions

## 58340:00 - 58385:00

we get is how do I know if I need to go

## 58385:00 - 58425:00

to the next stage or if this is

## 58425:00 - 58465:00

calibrated enough, right? There's not

## 58465:00 - 58495:00

really a rule book you can follow, but

## 58495:00 - 58530:00

it's all about minimizing surprise,

## 58530:00 - 58565:00

which means let's say you're calibrating

## 58565:00 - 58610:00

every one or two days. Um, and you

## 58610:00 - 58630:00

figure out that you're not seeing new

## 58630:00 - 58665:00

data distribution patterns. your users

## 58665:00 - 58690:00

have been pretty consistent with how

## 58690:00 - 58720:00

they're behaving with the system, then

## 58720:00 - 58765:00

the amount of information you gain is

## 58765:00 - 58795:00

kind of very low and that's when you

## 58795:00 - 58840:00

know you can actually go to the next um

## 58840:00 - 58870:00

stage, right? And it's all about the

## 58870:00 - 58900:00

wipes at that point. Like do you know

## 58900:00 - 58945:00

you're ready? Um you're not receiving

## 58945:00 - 59000:00

any new information. But also it really

## 59000:00 - 59045:00

helps to understand that sometimes there

## 59045:00 - 59115:00

are events that could completely uh

## 59115:00 - 59140:00

you know mess up the calibration of your

## 59140:00 - 59210:00

system. An example is um GPD 40 doesn't

## 59210:00 - 59240:00

exist anymore or it's going to be

## 59240:00 - 59275:00

deprecated in APIs as well. So most

## 59275:00 - 59305:00

companies that were using 40 should

## 59305:00 - 59345:00

switch to five and five has very

## 59345:00 - 59375:00

different properties. So that's where

## 59375:00 - 59405:00

your calibration's off again. You want

## 59405:00 - 59440:00

to go back and do this process again.

## 59440:00 - 59475:00

Sometimes users start users start

## 59475:00 - 59505:00

behaving with systems also differently

## 59505:00 - 59545:00

over time or user behavior evolves even

## 59545:00 - 59575:00

with consumer products right you don't

## 59575:00 - 59625:00

talk to chat GPT the same way you were

## 59625:00 - 59650:00

talking say two years ago just because

## 59650:00 - 59680:00

you know the capabilities have increased

## 59680:00 - 59720:00

so much and and also just people get

## 59720:00 - 59765:00

excited when um you know these systems

## 59765:00 - 59805:00

can solve one task they want to try it

## 59805:00 - 59850:00

out on other tasks as well. Uh we built

## 59850:00 - 59905:00

this system um for underwriters at some

## 59905:00 - 59940:00

point, right? Underwriting is a painful

## 59940:00 - 59980:00

task. There are agreements that are like

## 59980:00 - 60015:00

you know uh you know loan uh

## 60015:00 - 60045:00

applications that are like 30 or 40

## 60045:00 - 60090:00

pages. And the idea for this bank was to

## 60090:00 - 60115:00

build a system that could help

## 60115:00 - 60170:00

underwriters pick policies and you know

## 60170:00 - 60210:00

um um information about the bank so that

## 60210:00 - 60255:00

they could approve loans, right? And for

## 60255:00 - 60285:00

a good three or four months, everybody

## 60285:00 - 60310:00

was pretty impressed with the system. We

## 60310:00 - 60350:00

had underwriters actually report gains

## 60350:00 - 60375:00

in terms of how much time they were

## 60375:00 - 60425:00

spending etc. And post 3 months we

## 60425:00 - 60450:00

realized that they were so excited with

## 60450:00 - 60480:00

the product that they started asking

## 60480:00 - 60505:00

very deep questions that we never

## 60505:00 - 60535:00

anticipated. They would just throw the

## 60535:00 - 60570:00

entire application document at the

## 60570:00 - 60605:00

system and go like for a case that looks

## 60605:00 - 60640:00

like this what did previous underwriters

## 60640:00 - 60700:00

do and for a user that just seems like a

## 60700:00 - 60725:00

natural extension of what they were

## 60725:00 - 60770:00

doing but the building behind it should

## 60770:00 - 60795:00

significantly change. Now you need to

## 60795:00 - 60830:00

understand what does for a case like

## 60830:00 - 60870:00

this mean in the context of the loan

## 60870:00 - 60900:00

itself. Is it referring to people of a

## 60900:00 - 60930:00

particular you know income range or is

## 60930:00 - 60955:00

it referring to people in a particular

## 60955:00 - 60990:00

geo and stuff like that and then you

## 60990:00 - 61015:00

need to pick up historical documents

## 61015:00 - 61045:00

analyze those documents and then tell

## 61045:00 - 61075:00

them um okay this is what it looks like

## 61075:00 - 61110:00

versus just saying that there's a policy

## 61110:00 - 61155:00

X Y and Z and you want to um you know

## 61155:00 - 61200:00

look up that policy. Um so something

## 61200:00 - 61235:00

that might seem very natural to a end

## 61235:00 - 61285:00

user might be very hard to build as a

## 61285:00 - 61320:00

product builder and you see that user

## 61320:00 - 61350:00

behavior also evolves over time and

## 61350:00 - 61375:00

that's when you know you you know that

## 61375:00 - 61405:00

you want to go back and recalibrate.

## 61405:00 - 61460:00

>> What do you think is uh overhyped in the

## 61460:00 - 61495:00

AI space right now and even more

## 61495:00 - 61520:00

importantly what do you think is is

## 61520:00 - 61540:00

underhyped?

## 61540:00 - 61590:00

>> I am as I said like super optimistic in

## 61590:00 - 61620:00

different things that are going in AI.

## 61620:00 - 61665:00

So I wouldn't say overhyped but I feel

## 61665:00 - 61710:00

kind of misunderstood is the concept of

## 61710:00 - 61755:00

multi- aents. Uh people have this notion

## 61755:00 - 61790:00

of like uh I have this incredibly

## 61790:00 - 61825:00

complex problem. Now I'm going to break

## 61825:00 - 61865:00

it down into hey you are this agent take

## 61865:00 - 61890:00

care of this. You're this agent take

## 61890:00 - 61920:00

care of this. And now if I somehow

## 61920:00 - 61955:00

connect all of these agents they think

## 61955:00 - 62000:00

they're the agent utopia. And it's never

## 62000:00 - 62035:00

the case that there are incredibly

## 62035:00 - 62065:00

successful multi-agent systems that are

## 62065:00 - 62090:00

built right like there's no doubt about

## 62090:00 - 62125:00

that. But I feel a lot of it comes in

## 62125:00 - 62190:00

terms of how are you limiting the uh

## 62190:00 - 62220:00

ways in which the system can go off

## 62220:00 - 62260:00

tracks and for example like if you're

## 62260:00 - 62285:00

building a supervisor agent and there

## 62285:00 - 62310:00

are like sub agents that actually do the

## 62310:00 - 62345:00

work for the super agent supervisor

## 62345:00 - 62385:00

agent that is a very uh successful

## 62385:00 - 62425:00

pattern but coming with this notion of

## 62425:00 - 62470:00

I'm going to divide the responsibilities

## 62470:00 - 62520:00

based on functionality and somehow uh

## 62520:00 - 62560:00

expect all of that to work together in

## 62560:00 - 62600:00

some sort of like gossip protocol.

## 62600:00 - 62650:00

uh that is like extremely uh

## 62650:00 - 62690:00

misunderstood that you could do that. I

## 62690:00 - 62720:00

don't think like current uh ways of

## 62720:00 - 62745:00

building and current like uh model

## 62745:00 - 62785:00

capabilities are like right there in

## 62785:00 - 62815:00

terms of like uh building those kind of

## 62815:00 - 62855:00

applications. I feel that is kind of

## 62855:00 - 62900:00

misunderstood than overrated. uh

## 62900:00 - 62950:00

underrated. I feel it's hard to probably

## 62950:00 - 62975:00

believe but I still feel coding agents

## 62975:00 - 63020:00

are underrated in the sense that I feel

## 63020:00 - 63045:00

like you can go on Twitter and you can

## 63045:00 - 63075:00

go on Reddit and you see a lot of

## 63075:00 - 63115:00

chatter about coding agents but talking

## 63115:00 - 63155:00

to an engineer in like any random

## 63155:00 - 63190:00

company uh especially outside of Bay

## 63190:00 - 63240:00

Area you you can see like the amount of

## 63240:00 - 63265:00

impact this coding agents can create and

## 63265:00 - 63305:00

the penetration is very low. So I feel

## 63305:00 - 63335:00

like 2025

## 63335:00 - 63365:00

uh and 2026 is going to be like an

## 63365:00 - 63410:00

incredible year for optimizing all of

## 63410:00 - 63440:00

these processes and I feel that is going

## 63440:00 - 63480:00

to be creating a lot of value with AI.

## 63480:00 - 63500:00

That's really interesting on that first

## 63500:00 - 63545:00

point. So the idea there is uh you'll

## 63545:00 - 63580:00

probably be more successful building and

## 63580:00 - 63630:00

using uh an agent that is able to do its

## 63630:00 - 63670:00

own sub agent splitting of work versus

## 63670:00 - 63710:00

like a bunch of say codeex agents where

## 63710:00 - 63750:00

you do this task, you do that task. You

## 63750:00 - 63770:00

can have agents to do these things and

## 63770:00 - 63805:00

you as a human can orchestrate it or you

## 63805:00 - 63840:00

can have like one uh larger agent that

## 63840:00 - 63865:00

is going to orchestrate all of these

## 63865:00 - 63895:00

things. But letting the agents

## 63895:00 - 63925:00

communicate in terms of peer-to-peer

## 63925:00 - 63970:00

kind of protocol and then especially uh

## 63970:00 - 64000:00

doing this in say a customer support

## 64000:00 - 64045:00

kind of use case is incredibly hard to

## 64045:00 - 64075:00

control what kind of agent is replying

## 64075:00 - 64105:00

to your customer because you need to

## 64105:00 - 64130:00

shift your guardrails everywhere and

## 64130:00 - 64145:00

things like that.

## 64145:00 - 64185:00

>> Yeah. Okay. Uh great picks. Okay, Ash,

## 64185:00 - 64205:00

what do you got?

## 64205:00 - 64245:00

>> Can I say emails? Will I be cancelled?

## 64245:00 - 64275:00

>> On which in which category? Which which

## 64275:00 - 64290:00

bucket do they go?

## 64290:00 - 64305:00

>> Overrated.

## 64305:00 - 64340:00

>> Overrated. Okay, go go go for it. You we

## 64340:00 - 64370:00

won't let you get cancelled.

## 64370:00 - 64400:00

>> Uh just kidding. I think EVAs are

## 64400:00 - 64430:00

misunderstood. They are important folks.

## 64430:00 - 64465:00

I'm not saying they're not important.

## 64465:00 - 64525:00

But I think just um this um I'm going to

## 64525:00 - 64580:00

keep um jumping across tools and going

## 64580:00 - 64615:00

to pick up and learn a new tool is

## 64615:00 - 64675:00

overrated. I I still am old school and

## 64675:00 - 64700:00

feel like you would need really need to

## 64700:00 - 64725:00

be obsessed with the business problem

## 64725:00 - 64755:00

you're trying to solve. AI is only a

## 64755:00 - 64800:00

tool. Try to think of it that way. Of

## 64800:00 - 64820:00

course, you need to be learning about

## 64820:00 - 64855:00

the latest and greatest, but don't be so

## 64855:00 - 64895:00

obsessed with just building so quickly.

## 64895:00 - 64920:00

Building is really cheap today. Um

## 64920:00 - 64955:00

design is more expensive. really

## 64955:00 - 64975:00

thinking about your product, what you're

## 64975:00 - 65005:00

going to build, is it going to really

## 65005:00 - 65050:00

solve a pain point is is what is way

## 65050:00 - 65085:00

more valuable today and it will only

## 65085:00 - 65125:00

become uh more true in the near future,

## 65125:00 - 65165:00

right? So really obsessing about your

## 65165:00 - 65205:00

problem and design is underrated and

## 65205:00 - 65250:00

just wrote building is overrated I

## 65250:00 - 65265:00

guess.

## 65265:00 - 65310:00

>> Awesome. Okay. Uh similar sort of

## 65310:00 - 65370:00

question from a a product point of view.

## 65370:00 - 65405:00

What do you think the next year of AI is

## 65405:00 - 65440:00

going to look like? give us a vision of

## 65440:00 - 65460:00

where you think things are going to go

## 65460:00 - 65500:00

by say by the end of 2026.

## 65500:00 - 65535:00

>> Yeah, I feel uh there's a lot of promise

## 65535:00 - 65595:00

in terms of uh this background agents or

## 65595:00 - 65640:00

proactive agents who is like they're

## 65640:00 - 65670:00

going to like basically understand your

## 65670:00 - 65710:00

workflow even more. Uh if you think if

## 65710:00 - 65755:00

you think of like where is AI failing to

## 65755:00 - 65785:00

create value today, it's mainly about

## 65785:00 - 65825:00

not understanding the context. And the

## 65825:00 - 65850:00

reason that it's not understanding the

## 65850:00 - 65875:00

context is it's not plugged into the

## 65875:00 - 65900:00

right places where actual work is

## 65900:00 - 65940:00

happening. Right? And as you do more of

## 65940:00 - 65980:00

this, you can give the agent mode of

## 65980:00 - 66015:00

context and then it start to see the

## 66015:00 - 66045:00

world around you and understand what is

## 66045:00 - 66075:00

the what are the set of metrics that

## 66075:00 - 66100:00

you're optimizing for or what are the

## 66100:00 - 66125:00

kind of activities that you're trying to

## 66125:00 - 66170:00

do. It is a very easy extension from

## 66170:00 - 66205:00

there to actually gain more out of it

## 66205:00 - 66245:00

and then let the agent prompt you back.

## 66245:00 - 66270:00

uh we already do this in terms of charge

## 66270:00 - 66310:00

GPT pulse which kind of gives you this

## 66310:00 - 66340:00

daily update of things you might care

## 66340:00 - 66375:00

about and it's it's very nice to

## 66375:00 - 66405:00

actually have that like jog your brain

## 66405:00 - 66425:00

up in terms of oh this is something that

## 66425:00 - 66450:00

I haven't thought about maybe this is

## 66450:00 - 66480:00

good and now when you extend this to

## 66480:00 - 66520:00

more complex tasks like a coding agent

## 66520:00 - 66545:00

which says that like okay I have fixed

## 66545:00 - 66570:00

five of your linear tickets and here are

## 66570:00 - 66600:00

the patches just review them at the

## 66600:00 - 66630:00

start of your day so I feel that is

## 66630:00 - 66665:00

going to be like extremely useful and I

## 66665:00 - 66695:00

see that as like a strong direction in

## 66695:00 - 66710:00

which like products are going to build

## 66710:00 - 66735:00

in 2026

## 66735:00 - 66760:00

That is so cool. So essentially agents

## 66760:00 - 66815:00

kind of anticipating what you want to do

## 66815:00 - 66850:00

and getting going getting ahead of you

## 66850:00 - 66875:00

and here's I've solved these problems

## 66875:00 - 66905:00

for you or I think this is going to

## 66905:00 - 66925:00

crash your site. Maybe you should fix

## 66925:00 - 66960:00

this thing right here or I see the spike

## 66960:00 - 67015:00

here and let's refactor our database.

## 67015:00 - 67055:00

Amazing. What a world. Okay, Ash, what

## 67055:00 - 67070:00

do you got?

## 67070:00 - 67110:00

>> I am all in for multimodal experiences

## 67110:00 - 67155:00

in 2026. I think we have done quite some

## 67155:00 - 67205:00

progress in 2025 and um not just in

## 67205:00 - 67230:00

terms of generation but also

## 67230:00 - 67285:00

understanding um until now I think LLMs

## 67285:00 - 67330:00

have been our most commonly used models

## 67330:00 - 67385:00

but as humans we are multimodal

## 67385:00 - 67425:00

creatures I would say like um language

## 67425:00 - 67445:00

is probably one of our last forms of

## 67445:00 - 67475:00

evolution as the three of us are talking

## 67475:00 - 67510:00

I think we're constantly getting so many

## 67510:00 - 67545:00

signals I'm like oh Lenny is nodding his

## 67545:00 - 67570:00

head so probably I would go in this

## 67570:00 - 67605:00

direction or Lenny's bored so let me

## 67605:00 - 67635:00

stop stop stop talking So there's a

## 67635:00 - 67670:00

chain of thought be behind your chain of

## 67670:00 - 67700:00

thought and you're constantly altering

## 67700:00 - 67745:00

it with language that dimension of

## 67745:00 - 67775:00

expression is not explored as well. So

## 67775:00 - 67810:00

if you we could build better multimodal

## 67810:00 - 67855:00

experiences that would get us closer to

## 67855:00 - 67925:00

um humanlike um conversation richness

## 67925:00 - 67990:00

and um yeah I think um and just you will

## 67990:00 - 68030:00

also just given the kind of models

## 68030:00 - 68055:00

there's a bunch of boring tasks as well

## 68055:00 - 68090:00

which are ripe for AI if multimodal

## 68090:00 - 68125:00

understanding gets better there are so

## 68125:00 - 68160:00

many handwritten documents and really

## 68160:00 - 68215:00

messy uh PDFs that cannot be passed even

## 68215:00 - 68255:00

by the best of the models as of today

## 68255:00 - 68290:00

and if It's possible. There's there'll

## 68290:00 - 68340:00

be so much um um data that we can tap

## 68340:00 - 68350:00

into.

## 68350:00 - 68390:00

>> Awesome. I just saw Demis from Deep Mind

## 68390:00 - 68425:00

AI, Google, whatever they call the whole

## 68425:00 - 68455:00

or uh talking about this where he's

## 68455:00 - 68475:00

thinks that's going to be a big part of

## 68475:00 - 68515:00

where they're going, combining the image

## 68515:00 - 68565:00

model work, the LLM, and also their

## 68565:00 - 68590:00

world model stuff, Genie, I think is

## 68590:00 - 68615:00

what it's called.

## 68615:00 - 68655:00

>> So, that's going to be a wild wild time.

## 68655:00 - 68710:00

Okay. Uh last question. If someone wants

## 68710:00 - 68745:00

to just get better at building AI

## 68745:00 - 68800:00

products, what's just maybe one skill or

## 68800:00 - 68835:00

maybe two skills that you think they

## 68835:00 - 68875:00

should lean into and develop?

## 68875:00 - 68910:00

>> I think we did cover a bunch of best

## 68910:00 - 68935:00

practices for AI products, which is

## 68935:00 - 68990:00

start small, try to get your iteration

## 68990:00 - 69025:00

going well and build a flywheel and all

## 69025:00 - 69065:00

of that. But again, if you kind of look

## 69065:00 - 69115:00

at it at a 10,000 ft level for anybody

## 69115:00 - 69155:00

building today, like I was saying,

## 69155:00 - 69190:00

implementation is going to be

## 69190:00 - 69215:00

ridiculously cheap in the next few

## 69215:00 - 69260:00

years. So really nail down your design,

## 69260:00 - 69290:00

your judgment, your taste and all of

## 69290:00 - 69335:00

that. Um and in general if you're

## 69335:00 - 69385:00

building a career as well I feel for the

## 69385:00 - 69455:00

past few years your your former years

## 69455:00 - 69495:00

say the first two three years of uh

## 69495:00 - 69525:00

building your career is always focused

## 69525:00 - 69565:00

on execution mechanics and all of that

## 69565:00 - 69610:00

and now we have AI that could help you

## 69610:00 - 69655:00

ramp pretty quickly and post that I mean

## 69655:00 - 69680:00

after a few years I think everybody

## 69680:00 - 69725:00

everybody's job becomes about your taste

## 69725:00 - 69800:00

your judgment and kind of um uh you know

## 69800:00 - 69845:00

what is uniquely you. I think nail down

## 69845:00 - 69880:00

on that part and try to figure out how

## 69880:00 - 69915:00

you can bring in um that kind of a

## 69915:00 - 69955:00

perspective. Um and it doesn't have to

## 69955:00 - 69985:00

mean that you should be significantly

## 69985:00 - 70035:00

older, have ex um years of experience.

## 70035:00 - 70080:00

We recently hired someone and we use

## 70080:00 - 70125:00

this very popular app uh for tracking

## 70125:00 - 70155:00

our tasks, right? And we've been using

## 70155:00 - 70190:00

it for years and we pay a high

## 70190:00 - 70225:00

subscription fee for it. And this guy

## 70225:00 - 70260:00

just came with his own white coded app

## 70260:00 - 70305:00

to the meeting. he onboarded us um to

## 70305:00 - 70330:00

all of it and he's like okay let's start

## 70330:00 - 70360:00

using this and I think that kind of

## 70360:00 - 70390:00

agency and that kind of ownership to

## 70390:00 - 70430:00

really rethink experiences is what uh

## 70430:00 - 70465:00

will set people apart and I'm not being

## 70465:00 - 70500:00

blind to the fact that wipe coded apps

## 70500:00 - 70535:00

have high maintenance costs and maybe as

## 70535:00 - 70580:00

we scale as a company we have to replace

## 70580:00 - 70600:00

it or we have to think of better

## 70600:00 - 70635:00

approaches but given that we're a smalls

## 70635:00 - 70685:00

size company now and just I I was really

## 70685:00 - 70730:00

shocked because I never thought of it um

## 70730:00 - 70765:00

um if you've been used to working in a

## 70765:00 - 70800:00

certain way you associate a cost with

## 70800:00 - 70835:00

building and I feel like folks who grew

## 70835:00 - 70880:00

up in this age u have a much lower cost

## 70880:00 - 70910:00

associated in their mind they just don't

## 70910:00 - 70940:00

mind building something and going ahead

## 70940:00 - 70990:00

with it and that's they're also very um

## 70990:00 - 71030:00

enthusiastic to try out new tools um

## 71030:00 - 71060:00

that's also probably why AI products

## 71060:00 - 71085:00

have this retention problem because

## 71085:00 - 71110:00

everybody's so excited about trying out

## 71110:00 - 71145:00

these new tools and all of that but

## 71145:00 - 71185:00

essentially um having the agency and

## 71185:00 - 71225:00

ownership and I think it's also the end

## 71225:00 - 71275:00

going to be the end of the busy work

## 71275:00 - 71300:00

era, right? You can't be sitting in a

## 71300:00 - 71325:00

corner doing something that doesn't move

## 71325:00 - 71360:00

the needle for a company. You really

## 71360:00 - 71390:00

need to be thinking about, you know, end

## 71390:00 - 71420:00

to-end workflows, how you can bring in

## 71420:00 - 71450:00

more impact. I think all of that will be

## 71450:00 - 71470:00

super important.

## 71470:00 - 71490:00

>> That reminds me, I just had Jason

## 71490:00 - 71550:00

Lumpkit on the podcast. He's um uh very

## 71550:00 - 71575:00

smart on sales, go to market, run

## 71575:00 - 71610:00

Zaster, and he replaced his whole sales

## 71610:00 - 71640:00

team with agents. He had 10 sales

## 71640:00 - 71685:00

people, now he has 1.2 and 20 agents.

## 71685:00 - 71720:00

And one of the agents, it was just

## 71720:00 - 71750:00

tracking everyone's updates to

## 71750:00 - 71800:00

Salesforce and kind of uh updating it

## 71800:00 - 71825:00

automatically for them based on their

## 71825:00 - 71870:00

calls. And one of the salespeople uh is

## 71870:00 - 71905:00

like, "Okay, I'm I I quit." And it turns

## 71905:00 - 71940:00

out he wasn't really doing anything.

## 71940:00 - 71965:00

>> He was just sitting around

## 71965:00 - 71990:00

>> and he's like, "Okay, this will catch

## 71990:00 - 72025:00

me. I got to get out of here."

## 72025:00 - 72030:00

>> Yes.

## 72030:00 - 72055:00

>> So to your point about you can't it'll

## 72055:00 - 72080:00

be harder to sit around and to your

## 72080:00 - 72125:00

thumbs. Uh I think is really right.

## 72125:00 - 72155:00

>> Yeah. I think to add on to that like

## 72155:00 - 72190:00

feel like persistence is also something

## 72190:00 - 72235:00

that is extremely valuable especially

## 72235:00 - 72270:00

given that anybody who wants to build

## 72270:00 - 72305:00

something is the information is like at

## 72305:00 - 72345:00

your fingertips even more than like the

## 72345:00 - 72390:00

past decade right you can learn anything

## 72390:00 - 72425:00

overnight and become that sort of like

## 72425:00 - 72470:00

iron man kind of approach so I feel like

## 72470:00 - 72505:00

having that persistence and like going

## 72505:00 - 72550:00

through the pain of like learning this

## 72550:00 - 72575:00

implementing this and like understanding

## 72575:00 - 72615:00

what works and what doesn't work and as

## 72615:00 - 72640:00

you are going through this like pain of

## 72640:00 - 72680:00

like developing multiple approaches and

## 72680:00 - 72715:00

then solving the problem. I feel that is

## 72715:00 - 72745:00

like going to be the real boat as an

## 72745:00 - 72780:00

individual like I I I like to call it

## 72780:00 - 72825:00

like pain is the new mode but uh I feel

## 72825:00 - 72870:00

that is exactly super useful to actually

## 72870:00 - 72905:00

have this in especially in like you know

## 72905:00 - 72935:00

you're building these AI products.

## 72935:00 - 72960:00

>> Say more about this. I love this

## 72960:00 - 72995:00

concept. Pain is the new moat. Is there

## 72995:00 - 73030:00

more there? Yeah, I feel as a company I

## 73030:00 - 73060:00

mean like successful companies right now

## 73060:00 - 73090:00

building in any new area they are

## 73090:00 - 73125:00

successful not because they're first to

## 73125:00 - 73160:00

the market or like they have this fancy

## 73160:00 - 73185:00

feature that more customers are liking

## 73185:00 - 73210:00

it. They went through the pain of

## 73210:00 - 73245:00

understanding what are the set of

## 73245:00 - 73310:00

non-negotiable things and trade them off

## 73310:00 - 73345:00

exactly with like what are the features

## 73345:00 - 73370:00

or like what are the model capabilities

## 73370:00 - 73410:00

that I can use to solve that problem. it

## 73410:00 - 73430:00

it this is not a straightforward

## 73430:00 - 73455:00

process, right? There's no textbook to

## 73455:00 - 73480:00

do this or like there's no

## 73480:00 - 73510:00

straightforward way or like a known

## 73510:00 - 73560:00

threaded path to be here. So a lot of

## 73560:00 - 73590:00

this pain I was talking about is just

## 73590:00 - 73620:00

like going through this iteration of

## 73620:00 - 73655:00

like okay let's try this and if this

## 73655:00 - 73685:00

doesn't work let's try this and that

## 73685:00 - 73710:00

kind of knowledge that you built across

## 73710:00 - 73750:00

the organization or across like your own

## 73750:00 - 73795:00

experience lived experiences I feel that

## 73795:00 - 73845:00

the that pain is what uh translates into

## 73845:00 - 73880:00

the mode of the company right this could

## 73880:00 - 73920:00

be like a product of eval or like

## 73920:00 - 73945:00

something that you built and I feel that

## 73945:00 - 73985:00

is going to be the game changer

## 73985:00 - 74030:00

>> that is awesome it's like uh turning a

## 74030:00 - 74090:00

coal into diamond Diamond. Yes. Okay. Uh

## 74090:00 - 74125:00

I feel like we've done a great job

## 74125:00 - 74180:00

helping people avoid some of the biggest

## 74180:00 - 74225:00

issues people consistently run into

## 74225:00 - 74250:00

building AI products. We've covered so

## 74250:00 - 74285:00

many of the pitfalls and the ways to

## 74285:00 - 74325:00

actually do it correctly.

## 74325:00 - 74355:00

Before we get to our very exciting

## 74355:00 - 74375:00

lightning round, is there anything else

## 74375:00 - 74390:00

that you wanted to share? Anything else

## 74390:00 - 74415:00

you want to leave listeners with?

## 74415:00 - 74445:00

>> Be obsessed with your customers. Be

## 74445:00 - 74485:00

obsessed with the problem. Um AI is just

## 74485:00 - 74535:00

a tool and um try to make sure that

## 74535:00 - 74555:00

you're really understanding your

## 74555:00 - 74610:00

workflows. 80% of so-called AI

## 74610:00 - 74645:00

engineers, AIPM spend their time

## 74645:00 - 74670:00

actually understanding their workflows

## 74670:00 - 74700:00

very well. They're not building the

## 74700:00 - 74765:00

fanciest and the you know most uh cool

## 74765:00 - 74805:00

models or um workflows around it.

## 74805:00 - 74825:00

They're actually in the wheats

## 74825:00 - 74850:00

understanding their customers behavior

## 74850:00 - 74915:00

and data. Um, and whenever a software

## 74915:00 - 74960:00

engineer who's never done AI before

## 74960:00 - 74990:00

hears the term, look at your data, I

## 74990:00 - 75020:00

think it's a huge revelation to them,

## 75020:00 - 75055:00

but it's always been the case. You need

## 75055:00 - 75075:00

to go there. Look at your data,

## 75075:00 - 75115:00

understand your users, and that's going

## 75115:00 - 75150:00

to be a huge differentiator.

## 75150:00 - 75175:00

>> It's a great way to close it. It's not

## 75175:00 - 75215:00

the AI isn't the answer. It's it's a

## 75215:00 - 75275:00

tool to solve the problem. With that, we

## 75275:00 - 75305:00

have reached our very exciting lightning

## 75305:00 - 75340:00

round. I've got five questions for both

## 75340:00 - 75390:00

of you. Are you ready? Yay. Yes.

## 75390:00 - 75415:00

>> All right. So, you can both answer them.

## 75415:00 - 75435:00

You can pick one which you want to

## 75435:00 - 75475:00

answer. Either way, up to you. What are

## 75475:00 - 75500:00

two or three books you find yourself

## 75500:00 - 75535:00

recommending most to other people?

## 75535:00 - 75560:00

>> For me, it's this book called When

## 75560:00 - 75595:00

Breath Becomes Air, Lenny. It was

## 75595:00 - 75635:00

written by Paul Kalaniti. I think he was

## 75635:00 - 75680:00

um um an Indian origin neurosurgeon who

## 75680:00 - 75730:00

was diagnosed with lung cancer at 31 or

## 75730:00 - 75770:00

32 and the whole book is his memoir and

## 75770:00 - 75815:00

just is written after he was diagnosed

## 75815:00 - 75855:00

and it's it's really beautiful

## 75855:00 - 75885:00

especially because I read it during co

## 75885:00 - 75925:00

and all we ever wanted to do during co

## 75925:00 - 75975:00

is stay alive. Um there are a bunch of

## 75975:00 - 76020:00

really nice quotes within the book as

## 76020:00 - 76055:00

well, but I remember one of them he was

## 76055:00 - 76095:00

kind of arguing against a very popular

## 76095:00 - 76145:00

quote by Socrates which is the

## 76145:00 - 76205:00

unexamined life is not worth living or

## 76205:00 - 76235:00

something like that. And which means you

## 76235:00 - 76260:00

really need to be thinking about your

## 76260:00 - 76290:00

choices. You need to you know understand

## 76290:00 - 76315:00

your values, your mission and all of

## 76315:00 - 76360:00

that. And um Paul says, "If the

## 76360:00 - 76410:00

unexamined life is not worth living, was

## 76410:00 - 76450:00

the unlived life worth examining?" Which

## 76450:00 - 76490:00

means are you spending so much time just

## 76490:00 - 76515:00

understanding your mission and purpose

## 76515:00 - 76555:00

that you've forgotten to live? And I

## 76555:00 - 76600:00

think it everybody who's uh staying in

## 76600:00 - 76640:00

the AI era and building and continuously

## 76640:00 - 76670:00

going through this phase of reinventing

## 76670:00 - 76710:00

themselves need to take a pause and live

## 76710:00 - 76735:00

for a bit. I guess they need to stop

## 76735:00 - 76770:00

evaling life too much. What really

## 76770:00 - 76800:00

>> I was going to say that that's where my

## 76800:00 - 76830:00

mind went. generate some emails for your

## 76830:00 - 76875:00

life. Oh my god, we've gone too far.

## 76875:00 - 76900:00

>> Yep. Yeah. Yeah. That's that's my

## 76900:00 - 76915:00

favorite book.

## 76915:00 - 76950:00

>> I I like more of science fiction books.

## 76950:00 - 77005:00

So, I uh really like this three body

## 77005:00 - 77040:00

problem series. Uh it's like a three

## 77040:00 - 77085:00

book series. It's it's like has it has

## 77085:00 - 77110:00

elements of like grander than science

## 77110:00 - 77165:00

fiction uh life outside earth and how it

## 77165:00 - 77210:00

impacts like human decision-m process

## 77210:00 - 77240:00

and it also has like elements of

## 77240:00 - 77290:00

geopolitics and how how much important

## 77290:00 - 77330:00

or like valuable abstract science is to

## 77330:00 - 77365:00

human progress and then that gets when

## 77365:00 - 77390:00

that gets stopped it's it's not

## 77390:00 - 77425:00

noticeable in everyday life but it it

## 77425:00 - 77465:00

can cause like devastating effects. So I

## 77465:00 - 77500:00

feel like AI helping in these areas for

## 77500:00 - 77525:00

example is going to be like extremely

## 77525:00 - 77560:00

crucial and that book is like a nice

## 77560:00 - 77590:00

example of what could happen otherwise.

## 77590:00 - 77620:00

Completely agree absolutely love might

## 77620:00 - 77665:00

be my favorite sci-fi book except or

## 77665:00 - 77690:00

series even and it's three I have to

## 77690:00 - 77710:00

read them all three by the way. I find

## 77710:00 - 77745:00

that it only got really good about one

## 77745:00 - 77770:00

and a half books in. So if anyone's

## 77770:00 - 77795:00

tried it and like what the heck is going

## 77795:00 - 77830:00

on here just keep reading and get to the

## 77830:00 - 77860:00

middle of the second one and then gets

## 77860:00 - 77875:00

mindblowing.

## 77875:00 - 77925:00

>> Yes. Uh, if you love sci-fi and you're

## 77925:00 - 77955:00

an AI, you got to read this book called

## 77955:00 - 77995:00

A Fire Upon the Deep

## 77995:00 - 78055:00

by uh, Vernon Vege.

## 78055:00 - 78070:00

>> Mhm.

## 78070:00 - 78115:00

>> Check it out. It's incredible. Uh, I saw

## 78115:00 - 78145:00

Noah Smith on his newsletter recommend

## 78145:00 - 78175:00

this book and there's like a whole

## 78175:00 - 78195:00

there's like sequels to it, but this is

## 78195:00 - 78235:00

the one. It's so incredible and it's

## 78235:00 - 78260:00

actually turns out it's about AGI and

## 78260:00 - 78285:00

super intelligence and all these things

## 78285:00 - 78320:00

and it's just like so epic and no one's

## 78320:00 - 78330:00

heard of it.

## 78330:00 - 78340:00

>> Thank you.

## 78340:00 - 78365:00

>> There you go. I'm giving you one back.

## 78365:00 - 78395:00

Okay, next question. What's a favorite

## 78395:00 - 78425:00

recent movie or TV show that you've

## 78425:00 - 78440:00

really enjoyed?

## 78440:00 - 78470:00

>> I started re-watching Silicon Valley,

## 78470:00 - 78505:00

and I think it's so true. It's so

## 78505:00 - 78535:00

timeless. Everything is repeating all

## 78535:00 - 78570:00

over again. Anybody who's watched it a

## 78570:00 - 78600:00

few years ago should start re-watching

## 78600:00 - 78630:00

it, and you'll see that it's eerily

## 78630:00 - 78660:00

similar to everything that's happening

## 78660:00 - 78690:00

right now with the AI wave.

## 78690:00 - 78715:00

>> That's That's a good idea to rewatch it.

## 78715:00 - 78740:00

I love that their whole business was

## 78740:00 - 78765:00

like an algorithm to compress, like a

## 78765:00 - 78795:00

compression algorithm. It's like maybe a

## 78795:00 - 78845:00

precursor to LM in some small way. Very

## 78845:00 - 78890:00

good. All right, GT, what you got?

## 78890:00 - 78925:00

>> Uh, I'm going to digress and say not a

## 78925:00 - 78960:00

movie or a TV show, but there's this

## 78960:00 - 78985:00

game I picked up recently called

## 78985:00 - 79020:00

Expedition 33. Uh, it has nothing to do

## 79020:00 - 79055:00

with AI, but it's an incredibly

## 79055:00 - 79090:00

incredibly well-made game in terms of

## 79090:00 - 79125:00

the game play or like the movie and the

## 79125:00 - 79160:00

story and the music. Uh, it it's been

## 79160:00 - 79170:00

amazing.

## 79170:00 - 79190:00

>> I love that you have time to play games.

## 79190:00 - 79225:00

That's a great sign. I love that. So, an

## 79225:00 - 79255:00

open eye. I'm just imagining you're

## 79255:00 - 79285:00

there's nothing else going on except

## 79285:00 - 79320:00

just coding and and

## 79320:00 - 79350:00

>> yeah, it has been incredibly hard to

## 79350:00 - 79375:00

find time for that.

## 79375:00 - 79400:00

>> That's good. That's a good sign. I'm

## 79400:00 - 79420:00

happy to hear this. Okay. What's a

## 79420:00 - 79445:00

favorite product that you've recently

## 79445:00 - 79465:00

discovered that you really love?

## 79465:00 - 79495:00

>> For me, it's Whisper Flow. I think I've

## 79495:00 - 79535:00

been using it quite a bit and I didn't

## 79535:00 - 79585:00

know I needed it so much. Um the best

## 79585:00 - 79645:00

part is it's a conceptual transcription

## 79645:00 - 79680:00

tool which means if you go to you know

## 79680:00 - 79720:00

codeex and start using whisfl it starts

## 79720:00 - 79760:00

identifying variables and all of that

## 79760:00 - 79795:00

and it's so seamless in terms of

## 79795:00 - 79820:00

transcription to instruction you could

## 79820:00 - 79850:00

say something like I'm so excited today

## 79850:00 - 79885:00

add three exclamation marks and it

## 79885:00 - 79920:00

seamlessly switches it adds those three

## 79920:00 - 79950:00

exclamation marks instead of you know

## 79950:00 - 79990:00

writing add three exclamation marks and

## 79990:00 - 80025:00

I think it's pretty cool um um if you're

## 80025:00 - 80065:00

not using it you should try it I'll do a

## 80065:00 - 80110:00

plug. Get Whisper Flow for free for an

## 80110:00 - 80140:00

entire year

## 80140:00 - 80180:00

>> for a year for free by becoming an

## 80180:00 - 80210:00

annual subscriber of my newsletter.

## 80210:00 - 80240:00

>> And that's how I got access to it.

## 80240:00 - 80245:00

Lenny,

## 80245:00 - 80285:00

>> there we go. It's like I think I I

## 80285:00 - 80310:00

pitched this deal. I think people don't

## 80310:00 - 80345:00

truly understand how incredible this is.

## 80345:00 - 80365:00

They're like, "No way. This is real."

## 80365:00 - 80395:00

It's real. And 18 other products.

## 80395:00 - 80440:00

Lenny's productbass.com. Check it out.

## 80440:00 - 80470:00

Moving on. K.

## 80470:00 - 80525:00

>> Awesome. Uh I actually am a stickler for

## 80525:00 - 80560:00

productivity. I keep experimenting new

## 80560:00 - 80600:00

CLI tools and like things which can uh

## 80600:00 - 80640:00

make me faster. Uh so I feel like a

## 80640:00 - 80675:00

recast has been amazing. Uh I've

## 80675:00 - 80700:00

discovered all this like new shortcuts

## 80700:00 - 80730:00

that you can use to open different

## 80730:00 - 80755:00

things, type in shortcut commands and

## 80755:00 - 80795:00

things like that. And caffeinate is

## 80795:00 - 80815:00

another thing that I've recently

## 80815:00 - 80850:00

discovered from my teammates. It helps

## 80850:00 - 80895:00

you like prevent Mac from sleeping. So

## 80895:00 - 80925:00

you can run this really long codeex task

## 80925:00 - 80965:00

for like four or five hours locally. Let

## 80965:00 - 80990:00

it build the thing and then you can wake

## 80990:00 - 81020:00

up and be like okay this is good. I like

## 81020:00 - 81030:00

this.

## 81030:00 - 81075:00

>> That's hilarious. That combo codeex and

## 81075:00 - 81115:00

caffeinate. You guys, you guys need to

## 81115:00 - 81145:00

use it. Like build that yourself. An

## 81145:00 - 81180:00

open air version of that or the codeex

## 81180:00 - 81200:00

agent should just keep your Mac from

## 81200:00 - 81230:00

sleeping. That's so funny. Uh, by the

## 81230:00 - 81260:00

way, Raycast also part of Lenny's

## 81260:00 - 81305:00

product pass. One year free of Raycast.

## 81305:00 - 81345:00

>> We wen

## 81345:00 - 81385:00

Lenny didn't tell us these folks. These

## 81385:00 - 81405:00

are actually our favorite.

## 81405:00 - 81435:00

>> These are just two of 19 products. No

## 81435:00 - 81455:00

caffeinate though. I don't know if

## 81455:00 - 81485:00

that's even paid. Okay, let's keep

## 81485:00 - 81540:00

going. Do you have a favorite life motto

## 81540:00 - 81570:00

that you find yourself coming back to in

## 81570:00 - 81590:00

work or in life?

## 81590:00 - 81625:00

>> For me, I think this is what my dad told

## 81625:00 - 81650:00

me when I was a kid and it's always

## 81650:00 - 81710:00

stuck, which is um um they told it

## 81710:00 - 81740:00

couldn't be done, but the fool didn't

## 81740:00 - 81780:00

know it, so he did it anyway. I think be

## 81780:00 - 81815:00

foolish enough to believe that you can

## 81815:00 - 81850:00

do anything if you put your heart to it.

## 81850:00 - 81910:00

Especially now because you have so much

## 81910:00 - 81940:00

data at your hand that could be pointing

## 81940:00 - 81970:00

towards the fact that you probably will

## 81970:00 - 82005:00

be unsuccessful. with how many podcasts

## 82005:00 - 82025:00

made it to more than a thousand

## 82025:00 - 82075:00

subscribers or how many companies hit

## 82075:00 - 82115:00

more than 1 million y and there's always

## 82115:00 - 82140:00

data to show you that you won't be

## 82140:00 - 82175:00

successful but sometimes just be foolish

## 82175:00 - 82200:00

and go ahead with it

## 82200:00 - 82265:00

>> that's great yeah for me I uh am more of

## 82265:00 - 82305:00

an overinker so I really like this quote

## 82305:00 - 82335:00

from Steve Jobs that you can only

## 82335:00 - 82370:00

connect the dots looking backwards so

## 82370:00 - 82405:00

it's a lot of the times there are like

## 82405:00 - 82430:00

numerous choices and you don't really

## 82430:00 - 82475:00

know the optimal one to pick but life's

## 82475:00 - 82505:00

life works in ways that you can actually

## 82505:00 - 82530:00

see back and be like, "Oh, these are

## 82530:00 - 82565:00

actually beautiful in terms of how I I

## 82565:00 - 82590:00

would transition." So, I feel like that

## 82590:00 - 82620:00

is extremely useful in like, you know,

## 82620:00 - 82660:00

keep moving forward, keep experimenting.

## 82660:00 - 82695:00

>> Final question. Whenever I have two

## 82695:00 - 82730:00

guests on the podcast at once, I like to

## 82730:00 - 82765:00

ask this question. What's something that

## 82765:00 - 82805:00

you admire about the other person?

## 82805:00 - 82880:00

>> I think with Kir, um, it's about he's

## 82880:00 - 82945:00

he's pretty calm and, uh, very grounded.

## 82945:00 - 82980:00

Um, and he's always been my sounding

## 82980:00 - 83010:00

board. I can throw a ton of ideas at him

## 83010:00 - 83060:00

and he always comes up with he's able to

## 83060:00 - 83105:00

anticipate the kind of issues that might

## 83105:00 - 83175:00

um, run into and he's extremely um, kind

## 83175:00 - 83215:00

and lets his work speak instead of

## 83215:00 - 83245:00

actually doing a lot of talking, I

## 83245:00 - 83290:00

guess. But if I had to pick one, I think

## 83290:00 - 83345:00

uh, he's the most incredible husband. So

## 83345:00 - 83410:00

>> reveal little people know.

## 83410:00 - 83455:00

>> Yeah. We've been married for four years

## 83455:00 - 83485:00

and been the most beautiful four years

## 83485:00 - 83500:00

of my life.

## 83500:00 - 83570:00

>> Oh wow. Okay. How do you follow that?

## 83570:00 - 83605:00

>> Yeah, it's super hard to follow that. I

## 83605:00 - 83650:00

would say I am extremely privileged in

## 83650:00 - 83680:00

terms of working with like really smart

## 83680:00 - 83725:00

people in great companies in the Silicon

## 83725:00 - 83770:00

Valley. And I feel the unique thing that

## 83770:00 - 83815:00

stands with Ashwaryia across like any

## 83815:00 - 83850:00

other uh smart folks I've worked on is

## 83850:00 - 83890:00

like she has this really amazing knack

## 83890:00 - 83925:00

of teaching and like explaining

## 83925:00 - 83960:00

something uh in a very understandable

## 83960:00 - 84005:00

and easy to comprehend way and that

## 84005:00 - 84040:00

combined with persistence is like super

## 84040:00 - 84085:00

useful especially in this uh fastmoving

## 84085:00 - 84110:00

AI world that we are in in the sense

## 84110:00 - 84130:00

that there's so many new things coming

## 84130:00 - 84175:00

up it feels overwhelming but when I hear

## 84175:00 - 84210:00

her talk about like this is how you make

## 84210:00 - 84240:00

sense of this entire thing this is where

## 84240:00 - 84265:00

it plugs in. I feel like oh that is so

## 84265:00 - 84305:00

simple like I can also do that. So she

## 84305:00 - 84345:00

empowers a lot of people by simplifying

## 84345:00 - 84385:00

things and you know like uh explaining

## 84385:00 - 84415:00

things in the most understandable way.

## 84415:00 - 84445:00

So I feel that is like an incredible

## 84445:00 - 84465:00

quality.

## 84465:00 - 84500:00

>> Amazing. How sweet. I got to do this all

## 84500:00 - 84535:00

the time. I need more more yes to that

## 84535:00 - 84575:00

was that was great. Okay. Uh final

## 84575:00 - 84600:00

questions. Where can folks find stuff

## 84600:00 - 84620:00

that you're working on? Find you online.

## 84620:00 - 84660:00

Talk about share your course link and

## 84660:00 - 84685:00

then just how can listeners be useful to

## 84685:00 - 84690:00

you?

## 84690:00 - 84760:00

>> I write a lot on LinkedIn. Um um so if

## 84760:00 - 84790:00

you if you want to listen to pragmatists

## 84790:00 - 84825:00

who've been in the weeds working on AI

## 84825:00 - 84870:00

products and um what they're seeing, you

## 84870:00 - 84905:00

can uh follow my work. We also have a

## 84905:00 - 84945:00

GitHub repository with about 20K stars

## 84945:00 - 84980:00

and that repository is all about good

## 84980:00 - 85015:00

resources for learning AI. It's

## 85015:00 - 85060:00

completely free and if you um like what

## 85060:00 - 85090:00

we spoke today, we also run a super

## 85090:00 - 85120:00

popular course. We'll leave a link to it

## 85120:00 - 85160:00

on building enterprise AI products. And

## 85160:00 - 85195:00

the course is a lot about unlearning

## 85195:00 - 85245:00

mindsets and following like a problem

## 85245:00 - 85280:00

first approach uh instead of a tool

## 85280:00 - 85320:00

first or a hype first approach. Um so

## 85320:00 - 85345:00

you can check that out as well. And if

## 85345:00 - 85370:00

you don't want to do the course, we

## 85370:00 - 85400:00

write a lot. We give out a lot of free

## 85400:00 - 85435:00

resources. We have free sessions. So

## 85435:00 - 85460:00

make sure you follow our work.

## 85460:00 - 85485:00

>> Yeah, I would also add that I you can

## 85485:00 - 85520:00

also find me on LinkedIn. uh I don't

## 85520:00 - 85565:00

like write a lot I guess but I'm super

## 85565:00 - 85605:00

all excited to just talk to any complex

## 85605:00 - 85640:00

product that you're building and if you

## 85640:00 - 85685:00

have thoughts on like how you can uh use

## 85685:00 - 85715:00

coding agents to make your life better

## 85715:00 - 85740:00

or how what are the problems that you're

## 85740:00 - 85770:00

seeing um always my DMs are open and

## 85770:00 - 85795:00

like we can have a great discuss.

## 85795:00 - 85845:00

>> Awesome. Well, Kiriti and Ash, thank you

## 85845:00 - 85870:00

so much for being here.

## 85870:00 - 85880:00

>> Thank you so much.

## 85880:00 - 85910:00

>> Thank you Lenny. This was so much fun.

## 85910:00 - 85965:00

>> So much fun. Bye everyone.

## 85965:00 - 85990:00

>> Thank you so much for listening. If you

## 85990:00 - 86015:00

found this valuable, you can subscribe

## 86015:00 - 86060:00

to the show on Apple Podcasts, Spotify,

## 86060:00 - 86100:00

or your favorite podcast app. Also,

## 86100:00 - 86130:00

please consider giving us a rating or

## 86130:00 - 86165:00

leaving a review as that really helps

## 86165:00 - 86200:00

other listeners find the podcast. You

## 86200:00 - 86235:00

can find all past episodes or learn more

## 86235:00 - 86290:00

about the show at lennispodcast.com.

## 86290:00+

See you in the next episode.

