---
publish: true
review-frequency: normal
---
2021-12-29-We
Author:: [[Allen B. Downey]]
Originally published:: March 2009
Type:: #notes
Tags:: [[concurrency]], [[semaphores]]

**Bonded waiting** The amount of time a thread waits on is provably finite.

Starvation is the responsibility of scheduler. The algorithm used for scheduler can be used to enforce bonded waiting.

*Without* knowing scheduler algorithm, we need to start with a few weaker assumptions that may ensure bounded waiting.
- **Property 1:** if there is only one thread that is ready to run, the scheduler has to let it run.
- **Property 2:** if a thread is ready to run, then the time it waits until it runs is bounded
- **Property 3:** if there are threads waiting on a semaphore when a thread **signal**, then one of the waiting threads has to be woken.
	- As opposed to the case thread signal semaphore and keep on running
	- Only this property is **Weak semaphore**
- **Property 4:** if a thread is waiting at a semaphore, then the number of thread that will be woken before it is bonded.	AKA **Strong semaphore**

## No-starve mutex problem:
```python
while true:
	mutex.wait()
	# Critical section
	mutex.signal()
```
Thread A, B, C, or more: How to ensure no thread is starved.

- Dijkstra think it is not possible to solve mutex starving with only **weak semaphore**, but **J.M. Morris**, in 1979, solved no-starve mutex problem with only **property 4**.

## No-starve mutex solution:
Similar to reusable barrier, 2 turnstiles to keep threads holding on a different semaphore until the the other one is completely empty.
```
room1 = room2 = 0
mutex = Semaphore(1)
t1 = Semaphore(1)
t2 = Semaphore(0)

mutex.wait()
	room1 += 1
mutex.signal()	

t1.wait()
	room2 += 1
	mutex.wait()
	romm1 -= 1
	
	if room1 == 0:
		mutex.signal()
		t2.signal()
	else:
		mutex.signal()
		t1.signal()
		
t2.wait()
	room2 -= 1
	
	# critical section
	
	if room2 == 0:
		t1.signal()
	else:
		t2.signal()
```
