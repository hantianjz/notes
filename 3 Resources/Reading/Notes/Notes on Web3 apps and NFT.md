---
publish: true
review-frequency: normal
author: Marlinspike
tags:
  - notes
link:
  - "[[web3]]"
  - "[[crypto]]"
date published: 2022-01-07
reviewed: 2023-09-03
---
1. People don't want to host their own web servers. This is evident from rise of platforms like Wordpress, Medium, Squarespace, etc.
2. A public protocol moves slower than a platform. Example email is still un-encrypted by default after decades, while WhatsApp went e2ee in a year.

The only way to interact with the blockchain is through a server/computer, since it is currently not possible to do it on your mobile device. Which just lead to new platforms running these service for you.

> [!quote] 
 Almost all dApps use either [Infura](https://infura.io/) or [Alchemy](https://www.alchemy.com/) in order to interact with the blockchain. In fact, even when you connect a wallet like MetaMask to a dApp, and the dApp interacts with the blockchain via your wallet, MetaMask is just making calls to Infura!

A NFT is just a URL save on the chain, that point to the artifact, without any verification checksum stored on the chain. Anyone can switch out the URL to point to something else.

> [!quote] 
Instead of storing the data on-chain, NFTs instead contain a URL that _points to_ the data. What surprised me about the standards was that there’s no hash commitment for the data located at the URL. Looking at many of the NFTs on popular marketplaces being sold for tens, hundreds, or millions of dollars, that URL often just points to some VPS running Apache somewhere.

What people see on the blockchain is really what the platforms allows the user to see.

> [!quote] 
What I found most interesting, though, is that after OpenSea removed my NFT, it also **no longer appeared in any crypto wallet on my device**. This is web3, though, how is that possible?

NFT transactions are expensive as it is the price of coin

> [!quote] 
When you think about it, OpenSea would actually be much “better” in the immediate sense if all the web3 parts were gone. It would be faster, cheaper for everyone, and easier to use. For example, to accept a bid on my NFT, I would have had to pay over $80-publish: true
50+ just in ethereum transaction fees.

There is very little cryptography in crypto.

# IT IS A GOLD RUSH!!

> [!quote] 
> 1.  **We should accept the premise that people will not run their own servers by designing systems that can distribute trust without having to distribute infrastructure.** This means architecture that anticipates and accepts the inevitable outcome of relatively centralized client/server relationships, but uses cryptography (rather than infrastructure) to distribute trust. One of the surprising things to me about web3, despite being built on “crypto,” is how little cryptography seems to be involved!
> 2.  **We should try to reduce the burden of building software.** At this point, software projects require an enormous amount of human effort. Even relatively simple apps require a group of people to sit in front of a computer for eight hours a day, every day, forever. This wasn’t always the case, and there was a time when 50 people working on a software project wasn’t considered a “small team.” As long as software requires such concerted energy and so much highly specialized human focus, I think it will have the tendency to serve the interests of the people sitting in that room every day rather than what we may consider our broader goals. I think changing our relationship to technology will probably require making software easier to create, but in my lifetime I’ve seen the opposite come to pass. Unfortunately, I think distributed systems have a tendency to exacerbate this trend by making things more complicated and more difficult, not less complicated and less difficult.

---
# Reference
- https://moxie.org/2022/01/07/web3-first-impressions.html