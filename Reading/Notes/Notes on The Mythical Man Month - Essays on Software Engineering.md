---
publish: true
review-frequency: normal
author: Frederick P. Brooks, Jr.
tags:
  - notes
link:
  - "[[programming]]"
  - "[[software]]"
  - "[[engineering]]"
  - "[[essay]]"
  - "[[reading]]"
reviewed: 2023-09-03
---
# The Tar Pit
Large system programming can be a tar pit. Accumulation of simultaneous and interacting factors brings slower and slower motion.

## Why is programming fun?
- First is the **sheer joy** of making things. As the child delights in his mud pie, so the adult enjoys building things, especially things of his own design.
- Second is the pleasure of **making things that are useful to other people**.
- Third is the fascination of fashioning **complex puzzle-like** objects of interlocking moving parts and watching them work in subtle cycles, playing out the consequences of principles built in from the beginning.
- Forth is the joy of **always learning**, which springs from the non-repeating nature of the task.
- Finally, there is the delight of working in such a **tractable medium**. Few media of creation are so flexible, so easy to polish and rework, so readily capable of realizing grand conceptual structures.

## The Woes of the craft
- First, Adjusting to the **requirement for perfection** is the most difficult part of learning to program.
- Second, work is not controlled by engineers. In management terms, one's authority is not sufficient for his responsibility. Authority is acquired from the very momentum of accomplishment
- Third, dependence upon others and their work.
- With any creative activity come dreary hours of tedious, painstaking labor, and programming is no exception.
- Testing and debugging get harder and harder as the project goes on.
- If the project takes too long to completely it risks to become obsolete.
- The challenge and the mission are to find real solutions to real programs on actual schedules with available resources.

# The Mythical Man-Month
### Why does software project often run out of time.
- Techniques of estimating are poorly developed. An assumption that all will go well, which is quite untrue.
- Estimating techniques fallaciously confuse effort with progress.
- We are uncertain of our estimates, and often fail push back for more time.
- Schedule progress is poorly monitored.
- When schedule is slipped, natural response is to add man power, which often make things worse.

## Optimism
> [!The mind of the Maker]
> Creative activity into three stages: the idea, the implementation, and the interaction.

- Human ideas are often incomplete and inconsistent when in our head, but we don't realize them.
- The incompleteness and inconsistency only surface during implementation
- Also programmer being a very tractable medium, prevent us seeing all the difficulties during implementation.
- Hence our optimism in the process of implementation is unjustified.

## The Man-Month
Cost of the project vary as the product of number of person and number of month. BUT progress does NOT!
The *man-month* as a unit of measuring the side of a job is a dangerous and deceptive myth.

Person and moths are interchangeable only when a task can be partitioned among many works, with no communication among them.

> [!Systems]
Software construction is inherently a systems effort - an exercise in complex interrelationships -communication effort is great, and it quickly dominates the decrease in individual task time brought about by partitioning. 

## Systems Test
**Recommend:**
- 1/3 Planning
- 1/6 Coding
- 1/4 Component test and early system test
- 1/4 System test, all components in hand

Failure to allow enough time for system test are often disastrous. Since delay comes at the end of the schedule. The cost-per-day delay is maximum. 
The secondary cost of delaying is even higher.

## Gutless Estimating
Hunch guess are bad, but with enough padding it is at least better than wish-derived estimates.

## Regenerative schedule Disaster
When a project is behind schedule, there are essentially 4 things one can do:
1. Task must be done on time, assume only tasks so far are misestimated and future task will be correct. Add more folks to the project.
2. Assume task must be done on time. And future tasks' estimate is also wrong. Add more folks.
3. Reschedule the project and push out the delivery date.
4. Trim the tasks.

In project scheduling, one is either **feature bound** where the feature must be complete, or **time bound** where something must be delivered at X date. If both feature and time bound, it is surely spell disaster.

> Adding man power to a late software project makes it later.

> The maximum number of men depends upon the number of independent subtasks.