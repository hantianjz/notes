# Software Packaging Is a Nightmare

![rw-book-cover](https://staging.cohostcdn.org/avatar/22345-b7ed26bd-1fcd-4aee-99e7-893a449bc04e-profile.png)

## Metadata
- Author: [[PolyWolf on cohost]]
- Full Title: Software Packaging Is a Nightmare
- Category: #articles
- URL: https://cohost.org/PolyWolf/post/2613009-software-packaging-a?utm_source=tldrnewsletter

## Highlights
- Let's lay out our ***Ideal Build System Requirements*** again:
  • Reproducible builds: if a remote system can build it, your local system can too
  • Local overrides: not only can you build the package locally, you can swap it out for anything expecting that package
  • Remotely hosted binary releases: because you *deserve* to not have your fans take off and your disk explode every time you want to install some software
  • No global version set: you can have more than one version (major, minor, patch all included) of a package installed on your system, and things just don't care, since they use the one they were reproducibly built for
  • Semver *and* hash pinning: to enable dependency sharing if supported, but also for exact reproducibility if needed ([View Highlight](https://read.readwise.io/read/01hbmcnck2sscm2hfeg57qkwk1))
