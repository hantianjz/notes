---
publish: true
review-frequency: normal
---
2021-12-29-We
Author:: [[Allen B. Downey]]
Originally published:: March 2009
Type:: #notes
Tags:: [[concurrency]], [[semaphores]]

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

## With limited buffer spaces:
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
