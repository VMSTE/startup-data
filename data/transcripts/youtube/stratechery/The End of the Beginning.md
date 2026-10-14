---
source: https://stratechery.com/2020/the-end-of-the-beginning/
title: The End of the Beginning
author: null
date: 2020-01-07T16:25:21+00:00
site_name: Stratechery by Ben Thompson
word_count: 1541
extraction_method: readability
grabbed_at: 2026-04-02T10:35:23.044Z
---

# The End of the Beginning

The first American automobile maker, Duryea Motor Wagon Company, was founded in 1895; 34 more auto-makers would be founded in the U.S. in the following five years.[1](#fn1-4532 "These numbers are from <a href=\"https://en.wikipedia.org/wiki/Timeline_of_motor_vehicle_brands\">this Wikipedia article</a>, supplemented with <a href=\"https://en.wikipedia.org/wiki/List_of_defunct_automobile_manufacturers_of_the_United_States\">this Wikipedia article</a>; I did not count steam-based automobile makers, motorcycle makers, buggies, or tractor makers") Then, an explosion: an incredible 233 additional automobile makers were founded in the first decade of the 20th century, and a further 168 between 1910 and 1919. The pace from that point on continued to slow:

[](https://i0.wp.com/stratechery.com/wp-content/uploads/2020/01/Screen-Shot-2020-01-08-at-12.15.23-AM.png?ssl=1)

On a practical level, that “0” in the 1980’s could be applied to the entire list: by 1920 automobile manufacturing was already dominated by GM, Ford, and Chrysler. AMC, a combination of several smaller brands, was a brief challenger in the 1950s and 1960s, but the “Big Three” mostly had the market to themselves, at least until imports started showing up in the 1970s.

Just because the proliferation of new car companies ground to a halt, though, does not mean that the impact of the car slowed in the slightest: indeed, it was primarily the second half of the century where the true impact of the automobile was felt in everything from the development of suburbs to big box retailers and everything in between. Cars were the foundation of society’s transformation, but not necessarily car companies.

#### Tech’s Story of Disruption

The story tech most loves to tell about itself is the story of disruption: sure, companies may appear dominant today, but it is only a matter of time until they are usurped by the next wave of startups. And indeed, that is exactly what happened half a century ago: IBM’s mainframe monopoly was suddenly challenged by minicomputers from companies like DEC, Data General, Wang Laboratories, Apollo Computer, and Prime Computers. And then, scarcely a decade later, minicomputers were disrupted by personal computers from companies like MITS, Apple, Commodore, and Tandy.

The most important personal computer, though, came from IBM, with an operating system from Microsoft. The former provided a massive distribution channel that immediately established the IBM PC as the most popular personal computer, particularly in the enterprise; the latter provided the APIs that created a durable two-sided network that made Microsoft the most powerful company in the industry for two decades.

That reality, though, was not permanent: first the Internet shifted the most important application environment from the operating system to the web, and then mobile shifted the most important interaction environment from the desk to the pocket. Suddenly it was Google and Apple that mattered most in the consumer space, while Microsoft refocused on the cloud and a new competitor, Amazon.

#### Dominance Epochs

Any discussion of dominance in tech touches on three epochs: IBM, Microsoft, and the present day. In this telling, companies like Google and Apple may be dominant now, but so were IBM and Microsoft, and, just as their days of IBM and Microsoft’s dominance passed, so too will today’s companies be eclipsed. Benedict Evans made this argument in [a blog post](https://www.ben-evans.com/benedictevans/2020/01/01/microsoft-monopoly-and-dominance):

> The tech industry loves to talk about ‘moats’ around a business – some mechanic of the product or market that forms a fundamental structural barrier to competition, so that just having a better product isn‘t enough to break in. But there are several ways that a moat can stop working. Sometimes the King orders you to fill in the moat and knock down the walls. This is the deus ex machina of state intervention – of anti-trust investigations and trials. But sometimes the river changes course, or the harbour silts up, or someone opens a new pass over the mountains, or the trade routes move, and the castle is still there and still impregnable but slowly stops being important. This is what happened to IBM and Microsoft. The competition isn’t another mainframe company or another PC operating system — it’s something that solves the same underlying user needs in very different ways, or creates new ones that matter more. The web didn’t bridge Microsoft’s moat — it went around, and made it irrelevant. Of course, this isn’t limited to tech — railway and ocean liner companies didn’t make the jump into airlines either. But those companies had a run of a century — IBM and Microsoft each only got 20 years.
> 
> None of this is an argument against regulation per se of any specific issue in tech. If a company is abusing dominance today, it is not an argument against intervention to point out that it will lose that dominance in a decade or two — as Keynes says, ‘in the long term we’re all dead’. The same applies to regulation of issues that have little or nothing to do with market dominance, such as privacy (though people sometime fail to understand this distinction). Rather, the problem comes when people claim that somehow these companies are immortal — to say that is to reject all past evidence, and to claim that somehow there will never be another generational change in tech, which seems unwise.

In this understanding of tech dominance, the driver of generational change is a paradigm shift: from mainframes to personal computers, from desktop applications to the web, first on personal computers, and then on mobile. Each shift brought a new company to dominance, and when the next shift arrives, so will new companies rise to prominence.

What, though, is the next shift?

#### Paradigm Shifts

There is an implication in the “generational change is inevitable” argument that paradigm shifts are _sui generis._ The personal computer was a discrete event, the Internet another, and mobile a third. Now we are simply waiting to see what is next — perhaps augmented reality, or voice assistants.

In fact, I would argue the opposite: the critical paradigm shifts in technology, which drove the generational changes that Evans wrote about, are part of a larger pattern.

Start with the mainframe: the primary interaction model was punched cards; to execute a program you had to insert your cards into a card reader and wait for the computer to read the program into memory, execute it, and give you the results. Computing was done in batches, because the I/O layer was directly linked to the application and data layer.

This explains why personal computers were so revolutionary: instead of one large shared computer for which you had to wait your turn, a user could access their own computer on their own desk whenever they wanted. Still, the personal computer, particularly in a corporate environment, lived alongside not just mainframes but increasingly servers on an intranet. The I/O layer and application and data layers were being pulled apart, but both were destinations: you had to go to your desk and be on the network to compute.

This last point gets at why the cloud and mobile, which are often thought of as two distinct paradigm shifts, are very much connected: the cloud meant applications and data could be accessed from anywhere; mobile made the I/O layer available anywhere. The combination of the two make computing continuous.

[](https://i0.wp.com/stratechery.com/wp-content/uploads/2020/01/computingevolution-e1578414248840.png?ssl=1)

What is notable is that the current environment appears to be the logical endpoint of all of these changes: from batch-processing to continuous computing, from a terminal in a different room to a phone in your pocket, from a tape drive to data centers all over the globe. In this view the personal computer/on-premises server era was simply a stepping stone between two ends of a clearly defined range.

#### The End of the Beginning

The implication of this view should at this point be obvious, even if it feels a tad bit heretical: there may not be a significant paradigm shift on the horizon, nor the associated generational change that goes with it. And, to the extent there are evolutions, it really does seem like the incumbents have insurmountable advantages: the hyperscalers in the cloud are best placed to handle the torrent of data from the Internet of Things, while new I/O devices like augmented reality, wearables, or voice are [natural extensions of the phone](https://stratechery.com/2019/beachheads-and-obstacles/).

In other words, today’s cloud and mobile companies — Amazon, Microsoft, Apple, and Google — may very well be the GM, Ford, and Chrysler of the 21st century. The beginning era of technology, where new challengers were started every year, has come to an end; however, that does not mean the impact of technology is somehow diminished: it in fact means the impact is only getting started.

Indeed, this is exactly what we see in consumer startups in particular: few companies are pure “tech” companies seeking to disrupt the dominant cloud and mobile players; rather, they take their presence as an assumption, and seek to transform society in ways that were previously impossible when computing was a destination, not a given. That is exactly what happened with the automobile: its existence stopped being interesting in its own right, while the implications of its existence changed everything.

_I wrote a follow-up to this article in [this Daily Update](https://stratechery.com/2020/the-end-of-the-beginning-follow-up-technological-revolutions-and-financial-capital-venture-versus-productive-capital/)._

* * *

1.  These numbers are from [this Wikipedia article](https://en.wikipedia.org/wiki/Timeline_of_motor_vehicle_brands), supplemented with [this Wikipedia article](https://en.wikipedia.org/wiki/List_of_defunct_automobile_manufacturers_of_the_United_States); I did not count steam-based automobile makers, motorcycle makers, buggies, or tractor makers [↩](#rf1-4532 "Return to footnote 1.")