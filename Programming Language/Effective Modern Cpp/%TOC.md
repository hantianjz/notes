#Cpp #Cpp11 #Cpp14 #Cpp17
##### [[%ANNOTATION#^01z8nlj556oy|lvalues vs rvalues]]
A useful heuristic to determine whether an expression is an lvalue is to ask if you can take its address. If you can, it typically is. If you can’t, it’s usually an rvalue.
Copies of rvalues are generally move constructed, while copies of lvalues are usually copy constructed.

#### Chapter 1: [[Intro]]
- [[Intro#Item 1 Understand template type deduction]]
- [[Intro#Item 2 Understand _auto_ type deduction]]
- [[Intro#Item 3 Understand _decltype_]]
- [[Intro#Item 4 Know how to view deduced types]]

#### Chapter 2: [[Auto]]
- [[Auto#Item 5 Prefer auto to explicit type declarations]]
- [[Auto#Item 6 User the explicitly typed initializer idiom when _auto_ deduces undesired types]]

#### Chapter 3: [[Moving to mordern Cpp]]
- [[Moving to mordern Cpp#Item 7 Distinguish between and when creating objects]]
- [[Moving to mordern Cpp#Item 8 Prefer _nullptr_ to 0 and NULL]]
- [[Moving to mordern Cpp#Item 9 Prefer alias declarations to typedefs]]
- [[Moving to mordern Cpp#Item 10 Prefer scoped enums to unscoped enums]]
- [[Moving to mordern Cpp#Item 11 Prefer deleted functions to private undefined ones]]
- [[Moving to mordern Cpp#Item 12 Declare overriding functions override]]
- [[Moving to mordern Cpp#Item 13 Prefer _const_iterators_ to _iterators_]]
- [[Moving to mordern Cpp#Item 14 Re-read Declare functions _noexcept_ if they won't emit exceptions]]
- [[Moving to mordern Cpp#Item 15 Use constexpr whenever possible]]
- [[Moving to mordern Cpp#Item 16 Make const member functions thread safe]]
- [[Moving to mordern Cpp#Item 17 Understand special member function generation]]

#### Chapter 4: [[Smart Pointers]]
- [[Smart Pointers#Item 18 Use std unique_ptr for exclusive-ownership resource management]]