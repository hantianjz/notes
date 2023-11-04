---
publish: true
review-frequency: normal
link:
- '[[concurrency]]'
- '[[semaphores]]'
tags:
- notes
---
2021-12-29-We

> Four threads are involved: an agent and three smokers. The smokers loop forever, first waiting for ingredients, then making and smoking cigarettes. The ingredients are tobacco, paper, and matches.
>
> We assume that the agent has an infinite supply of all three ingredients, and each smoker has an infinite supply of one of the ingredients; that is, one smoker has matches, another has paper, and the third has tobacco.
>
> The agent repeatedly chooses two different ingredients at random and makes them available to the smokers. Depending on which ingredients are chosen, the smoker with the complementary ingredient should pick up both resources and proceed.
>
> For example, if the agent puts out tobacco and paper, the smoker with the matches should pick up both ingredients, make a cigarette, and then signal the agent.

To explain the premise, the agent represents an operating system that allocates resources, and the smokers represent applications that need resources. The problem is to make sure that if resources are available that would allow one more applications to proceed, those applications should be woken up. Conversely, we want to avoid waking an application if it cannot proceed.

Based on this premise, there are three versions of this problem that often appear in textbooks:

- **The impossible version:** Patil’s version imposes restrictions on the solution. First, you are not allowed to modify the agent code. If the agent represents an operating system, it makes sense to assume that you don’t want to modify it every time a new application comes along. The second restriction is that you can’t use conditional statements or an array of semaphores. With these constraints, the problem cannot be solved, but as Parnas points out, the second restriction is pretty artificial [7]. With constraints like these, a lot of problems become unsolvable.
- **The interesting version:** This version keeps the first restriction—you can’t change the agent code—but it drops the others.

- **The trivial version:** In some textbooks, the problem specifies that the agent should signal the smoker that should go next, according to the ingredients that are available. This version of the problem is uninteresting because it makes the whole premise, the ingredients and the cigarettes, irrelevant. Also, as a practical matter, it is probably not a good idea to require the agent to know about the other threads and what they are waiting for. Finally, this version of the problem is just too easy.

Parnas use the idea of pusher, a dispatcher really.

Pusher A
```
isTobacco = isPaper = isMatch = False
tobaccoSem = Semaphore(0)
paperSem = Semaphore(0)
matchSem = Semaphore(0)

// Puser A wait for tobacco and when tobacco is received check if other item is received and notify corresponding smoker
tobacco.wait()
mutex.wait()
	if isPaper:
		isPaper = False
		matchSem.signal()
	elif isMatch:
		isMatch = False
		paperSem.signal()
	else:
		isTobacco = True
mutex.signal()
```

Smoker with tobacco
```
tobaccoSem.wait()
makeCigarette()
agentSem.signal()
smoke()
```

*The solution is similar for other pusher or smokers*