## Semaphore  is:
1. created with initial value, afterwards only incremented/decremented by one. Can't read current value of semaphore.
2.  When decremented by a thread, if value is negative, the thread blocks until another thread increment the semaphore.
3.  When incremented by a thread, if another thread is waiting, the waiting thread get unblocked.

# Basic [[Synchronization]] patterns
## Signaling
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
## Rendezvous
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
## Mutex
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
## Multiplex
```
mutex = Semaphore(N) // Init to value N
```
N thread parallel accessing critical section:
```
mutex.wait()
	# critical section
mutex.signal()
```
## Barrier
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
## Reusable barrier
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
## Exclusive Queue
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
## Fifo Queue
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

# Classical [[synchronization]] problems
## Produce-consumer problem
```
mutex = Semaphore(1)
items = Semaphore(0)
```
Producer:
```
event = waitForEvent()

mutex.wait()
	buffer.add(event)
mutex.signal()

items.signal()
```
Consumer:
```
items.wait()

mutex.wait()
	event = buffer.get()
mutex.signal()

event.process()
```

#### With limited buffer spaces:
Producer:
```
event = waitForEvent()

spaces.wait()

mutex.wait()
	buffer.add(event)
mutex.signal()
items.signal()
```
Consumer:
```
items.wait()
mutex.wait()
	event = buffer.get()
mutex.signal()

spaces.signal()

event.process()
```
## Readers-writers problem
- Categorical barriers
#### Light Switch :
```
class Lightswitch:
	def __init__(self):
		self.counter = 0
		self.mutex = Semaphore(1)
		
	def lock(self, semaphore):
		self.mutex.wait()
			self.counter += 1
			if self.counter == 1:
				semaphore.wait()
		self.mutex.signal()
		
	def unlock(self, semaphore):
		self.mutex.wait()
			self.counter -= 1
			if self.counter == 0:
				semaphore.signal()
		self.mutex.signal()
```
#### No-starve
```
readLS = Lightswitch()
roomEmpty = Semaphore(1)
turnstile = Semaphore(1)
```
Writer:
```
turnstile.wait()
	roomEmpty.wait()
	# Critical writer write
turnstile.signal()
```
Reader:
```
turnstile.wait()
turnstile.signal()

readLS.lock(roomEmpty)
	# Critical reader read 
readLS.unlock(roomEmpty)
```
- Reader still get priority, at most let out single writer
#### Writer priority
```
readLS = Lightswitch()
writeLS = Lightswitch()
mutex = Semaphore(1)
noReaders = Semaphore(1)
noWriters = Semaphore(1)
```
Reader:
```
noReader.wait()
	readLS.lock(noWriters)
noReader.signal()

# Critical reader read 

readLS.unlock(noWriters)
```
Writer:
```
writeLS.lock(noReader)
	noWriters.wait()
		# Critical writer write
	noWriters.signal()
writeLS.unlock(noReaders)
```
- Still can have reader starve
## No-Starve mutex

## Dining philosophers

## Cigarette smokers problem