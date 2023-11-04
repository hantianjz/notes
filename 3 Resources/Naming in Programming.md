---
publish: false
reviewed: 
review-frequency: low
tags:
  - articles
  - documentation
link:
  - "[[programming]]"
---
**Good name doesn’t misdirect, doesn’t omit, and doesn’t assume**.

A good name should give you a good idea about what the variable contains or function does. A good name will tell you all there is to know or will tell you enough to know where to look next. It will not let you guess, or wonder. It will not misguide you. A good name is obvious, and expected. It is consistent. Not overly creative. It will not assume context or knowledge that the reader is not likely to have.
# Things to look out when naming things
1. First make sure it is NOT a bad name.
2. Make it reflect what is represent.
3. Make it consistent with other names around it.
4. Length follow the scope.
5. Be consistent with terms used in the project.
6. Stick to the code convention.

# The simple technique for figuring out a name every time
1. Write a comment above the function/variable where you **describe what it is, in human language**, as if you were describing it to your colleague. It might be one sentence or multiple sentences. This is the essence of what your function/variable does, what it is.
2. Now, you take the role of the sculptor, and you chisel at and **shape that description of your function/variable until you get a name**, by taking pieces of it away. You stop when you feel that one more hit of your imagined chisel at it would take too much away.
3. Is your name still too complex/confusing? If that is so, that means that the code behind is too complex, and should be reorganized! **Go refactor it**.
4. **Ok, all done** → you have a nice name!
5. That comment above the function/variable? Remove everything from it that is now captured in the code (name + arguments + type signature). If you can remove the whole comment, great. Sometimes you can’t, because some stuff can’t be captured in the code (e.g. certain assumptions, explanations, examples, …), and that is also okay. But don’t repeat in the comment what you can say in the code instead. **Comments are a necessary evil and are here to capture knowledge that you can’t capture in your names and/or types**.

---
# References
- https://wasp-lang.dev/blog/2023/10/12/on-importance-of-naming-in-programming