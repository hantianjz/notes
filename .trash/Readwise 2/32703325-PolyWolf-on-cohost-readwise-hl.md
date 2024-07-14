---
tags: #readwise-articles
aliases: Software Packaging Is a Nightmare
---
# Software Packaging Is a Nightmare

## Metadata
- Author: [[PolyWolf on cohost]]
- Full Title: Software Packaging Is a Nightmare
- Summary: As promised [https://cohost.org/PolyWolf/post/2692944-i-m-2070-words-into].

Recently, a friend shared this gist about how Amazon's internal buildsystem works [https://gist.github.com/terabyte/15a2d3d407285b8b5a0a7964dd6283b0], and wow did that unlock some Opinions for me about software packaging.

----------------------------------------

Supposedly, Amazon's buildsystem "Brazil" works a little bit like Nix [https://nix.dev/tutorials/first-steps/]/NixPkgs [https://nixos.org/manual/nixpkgs/stable/]1, in that it has entirely reproducible builds based on package declarations of nearly every package in existence. But instead of just being able to choose a single snapshot of package versions2, you can also pin to semver [https://semver.org/] of a set of packages, whose mutual compatibility is automatically enforced via unit tests when creating a new immutable build, so you always have the latest updates. This is amazing. Also like Nix, you can have:

 * Two versions of a package installed on your system, since diffe...
- URL: https://cohost.org/PolyWolf/post/2613009-software-packaging-a?utm_source=tldrnewsletter

## Highlights
- Let's lay out our ***Ideal Build System Requirements*** again:
  • Reproducible builds: if a remote system can build it, your local system can too
  • Local overrides: not only can you build the package locally, you can swap it out for anything expecting that package
  • Remotely hosted binary releases: because you *deserve* to not have your fans take off and your disk explode every time you want to install some software
  • No global version set: you can have more than one version (major, minor, patch all included) of a package installed on your system, and things just don't care, since they use the one they were reproducibly built for
  • Semver *and* hash pinning: to enable dependency sharing if supported, but also for exact reproducibility if needed ([View Highlight](https://read.readwise.io/read/01hbmcnck2sscm2hfeg57qkwk1))
