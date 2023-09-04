---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #idea
Tags:: [[abstractions]], [[complexity]]

# Over Abstraction in Software

To Quote Charles' Tweet:
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">&quot;Modern&quot; abstractions are sometimes attempted but rarely stand the test of time. The most reusable software down here is unopinionated toolkits, and relatively focused and simple RTOS&#39;s (fancy language for &quot;task scheduler&quot;). I&#39;ve never seen sweeping platform abstractions succeed.</p>&mdash; Charles Nicholson BLM (@c_nich) <a href="https://twitter.com/c_nich/status/1395392822774222849?ref_src=twsrc%5Etfw">May 20, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Leaky abstraction never stand the test of time. The underlying assumption will always change and you are then left with a grand vision/platform that no longer fit the current problem.

People end up bolting hack onto the existing system hoping it would limp along and still work, without actually understanding how everything work under the hood. 

This is essentially what [[What is Gall's Law]] is saying.

---
# References