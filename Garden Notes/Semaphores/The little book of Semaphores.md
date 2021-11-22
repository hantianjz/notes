## Semaphore  is:
1. created with initial value, afterwards only incremented/decremented by one. Can't read current value of semaphore.
2.  When decremented by a thread, if value is negative, the thread blocks until another thread increment the semaphore.
3.  When incremented by a thread, if another thread is waiting, the waiting thread get unblocked.

# 3 [[Basic Concurrency patterns]]

# 4 Classical Concurrency problems
## 4.1 [[Produce-consumer problem]]
## 4.2 [[Readers-writers problem]]
## 4.3 [[No-Starve mutex problem]]
## 4.4 [[Dining philosophers problem]]
## 4.5 [[Cigarette smokers problem]]

# 5 [[Less Classical synchronization problems]]