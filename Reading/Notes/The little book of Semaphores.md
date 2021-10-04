## Semaphore  is:
1. created with initial value, afterwards only incremented/decremented by one. Can't read current value of semaphore.
2.  When decremented by a thread, if value is negative, the thread blocks until another thread increment the semaphore.
3.  When incremented by a thread, if another thread is waiting, the waiting thread get unblocked.

# Basic [[Synchronization]] patterns
## Signaling

## Rendezvous

## Mutex

## Multiplex

## Battier

## Reusable barrier

## Queue

## Fifo Queue

# Classical [[synchronization]] problems
## Produce-consumer problem

## Readers-writers problem

## No-Starve mutex

## Dining philosophers

## Cigarette smokers problem