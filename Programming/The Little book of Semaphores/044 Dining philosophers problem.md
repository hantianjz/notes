---
publish: true
review-frequency: normal
---
2021-12-29-We
Author:: [[Allen B. Downey]]
Originally published:: March 2009
Type:: #notes
Tags:: [[concurrency]], [[semaphores]]

*Five* philosophers, represent interacting threads

```
while True:
	think()
	get_forks()
	eat()
	put_forks()
```
Constraints:
- Only one philosopher hold a fork at a time
- It must be impossible to deadlock
- It must be impossible for philosopher to starve waiting for a fork
- It must be possible for more than one philosopher to eat at same time

```
def left(i): return i
def right(i): return (i+1) % 5

forks = [Semaphore(1) for i in range(5)]
```

## Solution 1: Limit number of eater at same time
```
footman = Semaphore(4)

def get_forks(i):
	footman.wait()
	forks[left(i)].wait()
	forks[right(i)].wait()
	
def put_forks(i):	
	forks[right(i)].signal()
	forks[left(i)].signal()
	footman.signal()
```

## Solution 2: Change order of picking fork
```
def get_forks(i):
	if i % 2 == 1:
		forks[left(i)].wait()
		forks[right(i)].wait()
	else:
		forks[right(i)].wait()
		forks[left(i)].wait()
	
def put_forks(i):	
	forks[left(i)].wait()
	forks[right(i)].wait()
```

## Tanenbaum's solution (FAILs NO starving)
```
state = ['thinking'] * 5
sem = [Semaphore(0) for i in range(5)]
mutex = Semaphore(1)

def get_fork(i):
	mutex.wait()
	state[i] = 'hungry'
	test(i)
	mutex.signal()
	sem[i].wait()

def put_fork(i):
	mutex.wait()
	state[i] = 'thinking'
	test(right(i))
	test(left(i))
	mutex.signal()
	
def test(i):
	if state[i] == 'hungry' and
	state[left(i)] != 'eating' and 
	state[right(i)] != 'eating':
		state[i] = 'eating'
		sem[i].signal()
```
