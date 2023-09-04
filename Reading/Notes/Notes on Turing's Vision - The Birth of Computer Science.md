---
publish: true
review-frequency: high
author: "[[Chris Bernhardt]]"
tags:
  - notes
link:
  - "[[turning]]"
  - "[[non fiction]]"
  - "[[computer science]]"
  - "[[halting problem]]"
  - "[[programming]]"
  - "[[reading]]"
date published: 2016-05-01
reviewed: 2023-09-03
---

>"Mathematics, rightly viewed, possesses not only truth, but supreme beauty-a beauty cold and austere, like that of sculpture, without appeal to any of our weaker nature, without the gorgeous trappings of painting or music, yet sublimely pure, and capable of stern perfection such as only the greatest art can show." - Bertrand Russell

## Undecidable decision problems
- Hilbert's tenth problem
- Post's correspondence problem
- Halting problem halting_problem

A decision problem is decidable if there exist an algorithm to give a correct answer in every case.

Emil post 10 years ahead of Godel or Turing or Church

Euclid's elements known mathematics of 1482 New theorems deduced from axioms and postulates, contain incorrect assumptions.

David Hilbert, 1899, Grundlagen Der Geometrie (Foundation of Geometry)
New complete axiom

>"Mathematics may be defined as the subject where we never know what we are talking about, more what we are saying is true"

### Properties of axiomatic foundation of Math
- Consistent: The axioms should never lead to paradoxes
- Complete: Every statement should be able to proved or disproved from the axioms
- Entscheidungsproblem: A decision procedure whether a statement can be proved by axioms

### Post's correspondence problem
> A catalog of various titles, each with _two_ sequences of **1** and **2**
- Find a collection of tiles such that **TOP** and **BOTTOM** sequence of **1s** and **2s** are equal.

- Post showed there does not exist an Algorithm to find a collection of tiles for a possible catalog of tiles.

### Hilbert's Tenth problem (Out of 23 problems)

> A Diophantine equation with integer coefficients. Find the integer solutions. $x^n + y^n = z^n; n \in z$

- Yuri Matiyasevich proved it is undecidable in 1970. (Martin Davis, Hilary Putnam and Julia Robinson)

- In both problem, it was shown there does NOT exist an algorithm to correctly identify there is NO solution.

### The Halting problem 
> An algorithm to determine/device if a program will halt in any case.

### Entscheidungsproblem
> An Algorithm to find the solution/algorithm to a given decision problem.
- Therefore it is only needed to prove some of these decision problem was undecidable.

Computation: Finite and infinite machines.

## Finite Automata
A finite number of state, **start** & **accept** state.
Input with sequence of symbol over an alphabet

![[Finite Automata.jpg]]

The set of string that finite automata accept is regular language.

$\epsilon$ => empty string

$+$ => Choice of 2

$*$ =>kleene star op

Regular expression can be used to describe the set of strings accepted by a finite automata.

Regular expression == Finite Automata.

Finite Automata can be depicted in a permutation of its Alphabet and its states.

This can then be converted to Post's correspondence problem can be accepted by original Finite Automata.

> "The idea behind digital computers maybe explained by saying that these machines and intended to carry out any operations which could be done by a human computer." - Alan Turning

## Turning Machine 

State transition depicted by 3 symbols:
- Current symbol on tape
- New symbol to write on tape
- Direction to move tape head

$\beta$ denote blank

- Specific accept and reject state, that also trap.
- Read head start at left most non-blank symbol.

#### TM that recognizing strings with an odd number of $1s$
![[Finite Automata 2.jpg]]

#### TM with equal number of 0s and 1s
![[Tm2.jpg]]

Turing defined algorithm to be anything that can be computed by a turning machine

$\lambda$ calculus is also a definition of algorithm

> "A good notation has a subtlety and suggestiveness, which at times make it almost seem like a live teacher." -- Bertrand Russel

> Quantum computers are NOT computationally more powerful than traditional computers. - 1985, David Deutsh

If a computation never halts, it is called to it **diverges**.

Finite automata always halt. The number of step in computation is the same as length of input.

> [!quote] Ada Lovelace
Augusta Ada Kind, Countess of Lovelace

## Lambda Calculus

Function composition via subsitution

Identity function: $f(x) = x$ or $\lambda x \cdot x$

## Peano arithmetic
with successor function
  $2 = S(1) = S(S(0))$
Define $+$ by 2 properties:
- $m+0=m$ for all $m \in N$
- $m + S(n) = S(m+n)$ for all $m,n \in N$

## One-Dimensional Cellular Automata
Single tap evolve and transform based on a localize rule. Computation takes place at discrete time interval.

> [!quote] Stephan Wolfram
New kind of Science

Matthew Cook, Rule 110 is universal for and computation(Game of life)

## A Encoding method for Finite Automata
`M -> <M>`

Needs information on:
1. Number of states
2. Start state
3. Accepting state
4. For each state, the result of 0,1 input

$0s$ encode numbers
$1s$ encode punctuation
- Four $1s$: Start or end of encode
- Three $1s$: End of category
- Two $1s$: Change in sub-category
- One $1s$: Used like comma

Encoding layout
```
1111 { number of states }
    111 { list of accept states }
    111 { transition for state 1 } 11 { transition for state 2 } 11 ...
1111
```

**<M, I>** = Encoding of Finite automata and input string

There exist a **TM** that can simulate any **FA** running any input.

There is a turning Machine, **U**, that will take any **<M, I>** as input and give the answer
*accept*, if **M** *accepts* **I**, give the answer *reject*, if if **M** *reject* **I**. This **U** is a universal turning machine.

## Russell's Barber contradiction
Finite Automata can be divided in term of:
- **FA** that accept their own encoding
- **FA** that do NOT

A machine **M** that determine if a FA accept its own encoding, can not be Finite Automata.

If a $M_{FA}$ exist such that it only accept FA that reject their own encoding.

Proof by contradiction this cannot exist:

Assume if $M_{FA}$ accept $<M_{FA}>$ then this is a contradiction, since $M_{FA}$ by definition only accept FA that reject its own encoding. If $M_{FA}$ reject $<M_{FA}>$, this is also a contradiction.

Therefore $M_{FA}$ is not a Finite Automata, but a turning machine.

But similarly the question:
  Given a turning machine, will it NOT accept its own encoding? Is an undecidable problem.

The negation of decision problems is the same.

Hence it is also true that:
  Given a turning machine, will it accept its own encoding? Is also undecidable.

Two sets of elements are said to have the same cardinality if there exist a bijection between them.
