2021-12-29-We
Author: [[Chris Bernhardt]]
Originally published: May 2016
Type: #notes
Tags: [[turning]], [[non fiction]], [[computer science]], [[halting problem]]

# Turing's Vision: The Birth of Computer Science

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

If a computation never halts, it is called to it diverges.

Finite automata always halt. The number of step in computation is the same as length of input.

Augusta Ada Kind, Countess of Lovelace

