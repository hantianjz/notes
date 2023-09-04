---
publish: true
review-frequency: normal
---
2021-12-29-We
Author:: [[Allen B. Downey]]
Originally published:: March 2009
Type:: #notes
Tags:: [[concurrency]], [[semaphores]]

## 5.1 The dining savage problem

> A tribe of savages eats communal dinners from a large pot that can hold M servings of stewed missionary1. When a savage wants to eat, he helps himself from the pot, unless it is empty. If the pot is empty, the savage wakes up the cook and then waits until the cook has refilled the pot.

```
servings = 0
mutex = Semaphore(1)
emptyPot = Semaphore(0)
fullPot = Semaphore(0)
```

**Cook**
```
while True:
	emptyPot.wait()
	putServingsInPot(M)
	fullPot.signal()
```

**Savages**
```
while True:
	mutex.wait()
		if servings == 0:
			emptyPot.signal()
			fullPot.wait()
			servings = M
		servings -= 1
		getServingFromPot()
	mutex.signal()
	
	eat()
```

## 5.2 The barbershop problem
>A barbershop consists of a waiting room with n chairs, and the barber room containing the barber chair. If there are no customers to be served, the barber goes to sleep. If a customer enters the barber shop and all chairs are occupied, then the customer leaves the shop. If the barber is busy, but chairs are available, then the customer sits in one of the free chairs. If the barber is asleep, the customer wakes up the barber. Write a program to coordinate the barber and the customers.

```
customers = 0
mutex = Semaphore(1)
customer = Semaphore(0)
barber = Semaphore(0)
```

**Customer**
```
mutex.wait()
	if customers == n+1:
		mutex.signal()
		balk() // Infinite loop
	customers += 1
mutex.signal()

customer.signal()
barber.wait()
getHairCut()

mutex.wait()
	customers -= 1
mutex.signal()
```

**barber**
```
while True:
	customer.wait()
	barber.signal()
	cutHair()
```

## 5.3 Hilzer's Barbershop problem
> Our barbershop has three chairs, three barbers, and a waiting area that can accommodate four customers on a sofa and that has standing room for additional customers. Fire codes limit the total number of customers in the shop to 20. A customer will not enter the shop if it is filled to capacity with other customers. Once inside, the customer takes a seat on the sofa or stands if the sofa is filled. When a barber is free, the customer that has been on the sofa the longest is served and, if there are any standing customers, the one that has been in the shop the longest takes a seat on the sofa. When a customer’s haircut is finished,any barber can accept payment, but because there is only one cash register, payment is accepted for one customer at a time. The barbers divide their time among cutting hair, accepting payment, and sleeping in their chair waiting for a customer.

```
customers = 0
mutex = Semaphore(1)
standingRoom = Fifo(16)
sofa = Fifo(4)
chair = Semaphore(3)
barber = Semaphore(0)
customer = Semaphore(0)
cash = Semaphore(0)
receipt = Semaphore(0)
```

**Customer**
```
mutex.wait()
	if customers == 20:
		mutex.signal()
		exitShop()
	customers += 1
mutex.signal()

standingRoom.wait()
enterShop()

sofa.wait()
sitOnSofa()
standingRoom.signal()

chair.wait()
sitInBarberChair()
sofa.signal()

customer.signal()
barber.wait()
getHairCut()

pay()
cash.signal()
recepit.wait()

mutex.wait()
	customers -= 1
mutex.signal()

exitShop()
```

**barber**
```
customer.wait()
barber.signal()
cutHair()

cash.wait()
acceptPayment()
receipt.signal()
```

## 5.4 The Santa Claus problem
> Stand Claus sleeps in his shop at the North Pole and can only be awakened by either (1) all nine reindeer being back from their vacation in the South Pacific, or (2) some of the elves having difficulty making toys; to allow Santa to get some sleep, the elves can only wake him when three of them have problems. When three elves are having their problems solved, any other elves wishing to visit Santa must wait for those elves to return. If Santa wakes up to find three elves waiting at his shop’s door, along with the last reindeer having come back from the tropics, Santa has decided that the elves can wait until after Christmas, because it is more important to get his sleigh ready. (It is assumed that the reindeer do not want to leave the tropics, and therefore they stay there until the last possible moment.) The last reindeer to arrive must get Santa while the others wait in a warming hut before being harnessed to the sleigh.