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

# Categorical barriers

## Light Switch :
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
## No-starve
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
## Writer priority
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

**Categorical starvation** where one type of threads starve vs another type.
