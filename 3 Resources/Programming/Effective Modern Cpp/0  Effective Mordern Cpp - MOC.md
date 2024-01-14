---
publish: true
reviewed: 2023-04-29
review-frequency: ignore
link:
  - "[[Cpp]]"
  - "[[Cpp11]]"
  - "[[Cpp14]]"
  - "[[Cpp17]]"
tags:
  - MOC
---
# 0  Effective Mordern Cpp - MOC
##### [[Effective_Modern_C__.pdf#page=20&selection=62,0,65,64|lvalues vs rvalues]]
A useful heuristic to determine whether an expression is an lvalue is to ask if you can take its address. If you can, it typically is. If you can’t, it’s usually an rvalue.
Copies of rvalues are generally move constructed, while copies of lvalues are usually copy constructed.

#### Chapter 1: [[1 Intro]]
- [[1 Intro#Item 1 Understand template type deduction]]
- [[1 Intro#Item 2 Understand _auto_ type deduction]]
- [[1 Intro#Item 3 Understand _decltype_]]
- [[1 Intro#Item 4 Know how to view deduced types]]

#### Chapter 2: [[2 Auto]]
- [[2 Auto#Item 5 Prefer auto to explicit type declarations]]
- [[2 Auto#Item 6 User the explicitly typed initializer idiom when _auto_ deduces undesired types]]

#### Chapter 3: [[3 Moving to mordern Cpp]]
- [[3 Moving to mordern Cpp#Item 7 Distinguish between and when creating objects]]
- [[3 Moving to mordern Cpp#Item 8 Prefer _nullptr_ to 0 and NULL]]
- [[3 Moving to mordern Cpp#Item 9 Prefer alias declarations to typedefs]]
- [[3 Moving to mordern Cpp#Item 10 Prefer scoped enums to unscoped enums]]
- [[3 Moving to mordern Cpp#Item 11 Prefer deleted functions to private undefined ones]]
- [[3 Moving to mordern Cpp#Item 12 Declare overriding functions override]]
- [[3 Moving to mordern Cpp#Item 13 Prefer _const_iterators_ to _iterators_]]
- [[3 Moving to mordern Cpp#Item 14 Re-read Declare functions _noexcept_ if they won't emit exceptions]]
- [[3 Moving to mordern Cpp#Item 15 Use constexpr whenever possible]]
- [[3 Moving to mordern Cpp#Item 16 Make const member functions thread safe]]
- [[3 Moving to mordern Cpp#Item 17 Understand special member function generation]]

#### Chapter 4: [[4 Smart Pointers]]
- [[4 Smart Pointers#Item 18 Use std unique_ptr for exclusive-ownership resource management]]