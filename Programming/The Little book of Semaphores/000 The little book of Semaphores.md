---
publish: true
review-frequency: normal
---
2021-12-29-We
Author:: [[Allen B. Downey]]
Originally published:: March 2009
Type:: #notes #MOC 
Tags:: [[concurrency]], [[semaphores]], [[Reading/reading]], [[programming]]

# The little book of Semaphores:

## Semaphore  is:
1. created with initial value, afterwards only incremented/decremented by one. Can't read current value of semaphore.
2.  When decremented by a thread, if value is negative, the thread blocks until another thread increment the semaphore.
3.  When incremented by a thread, if another thread is waiting, the waiting thread get unblocked.

# [[030 Basic Concurrency patterns]]

# 4 Classical Concurrency problems
## [[041 Produce-consumer problem]]
## [[042 Readers-writers problem]]
## [[043 No-Starve mutex problem]]
## [[044 Dining philosophers problem]]
## [[045 Cigarette smokers problem]]

# [[050 Less Classical synchronization problems]]