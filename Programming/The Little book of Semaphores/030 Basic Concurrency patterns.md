---
publish: true
review-frequency: normal
---
2021-12-29-We
Author:: [[Allen B. Downey]]
Originally published:: March 2009
Type:: #notes
Tags:: [[concurrency]], [[semaphores]]

# 3.1 Signaling
Thread A:
```
statement a1
sem.signal()
```

Thread B:
```
sem.wait()
statement b1
```
# 3.2 Rendezvous
Thread A:
```
statement a1
aArrived.signal()
bArrived.wait()
statement a2
```

Thread B:
```
statement b1
bArrived.signal()
aArrived.wait()
statement b2
```
# 3.3 Mutex
Thread A:
```
mutex.wait()
	# critical section
mutex.signal()
```

Thread B:
```
mutex.wait()
	# critical section
mutex.signal()
```
# 3.4 Multiplex
```
mutex = Semaphore(N) // Init to value N
```
N thread parallel accessing critical section:
```
mutex.wait()
	# critical section
mutex.signal()
```
# 3.5 Barrier
```
n = numer of threads
count = 0
mutex = Semaphore(1)
barrier = Semaphore(0)
```
Thread X:
```
mutex.wait()
	count = count + 1
mutex.signal()

if count == n: barrier.signal()

barrier.wait()
barrier.signal()

critical section
```
# 3.6 Reusable barrier
```
tunstile = Semaphore(0)
tunstile2 = Semaphore(1)
mutex = Semaphore(1)
```
Thread X:
```
mutex.wait()
	count += 1
	if count == n:
		turnstile2.wait()  # Lock the second turnstile
		turnstile.signal() # unlock the first tunstile
mutex.signal()

turnstile.wait()
turnstile.signal()

# Critical section

mutex.wait()
	count -= 1
	if count == 0:
		turnstile.wait()	# Lock First turnstile
		turnstile2.signal()	# Unlock the second turnstile
mutex.signal()

turnstile2.wait()
turnstile2.signal()
```
# 3.7 Exclusive Queue
```
leaders = followers = 0
mutex = Semaphore(1)
leaderQueue = Semaphore(0)
followerQueue = Semaphore(0)
rendezvous = Semaphore(0)
```
Thread Leader: 
```
mutex.wait()
if followers > 0:
	followers--
	followerQueue.signal()
else:
	leaders++
	mutex.signal()
	leaderQueue.wait()
	
dance()	
rendezvous.wait()
mutex.signal()
```
Thread Follower: 
```
mutex.wait()
if leaders > 0:
	leaders--
	leaderQueue.signal()
else:
	followers++
	mutex.signal()
	followerQueue.wait()

dance()
rendezvous.signal()
```
# 3.8 Fifo Queue
```
class Fifo:
	def __init__(self):
		self.queue = Queue()
		self.mutex = Semaphore(1)
	
	def wait(mySem):
		self.mutex.wait()
		self.queue.add(mySem)
		self.mutex.signal()
		mySem.wait()
		
	def signal():
		self.mutex.wait()
		sem = self.queue.remove()
		self.mutex.signal()
		sem.signal()	
```
