---
publish: false
---
2022-05-07-Sa
Author: Bjarne Stroustrup
Originally published: September 2013
Type: #notes
Tags: [[Cpp]]

# A tour of C++

> [!note]
> C++ is a statically typed language. That is, the type of every entity (e.g., object, value, name, and expression) must be known to the compiler at its point of use. The type of an object determines the set of operations applicable to it.

>[!note] 
> Main function. Not every operating system and execution environment make use of that return value: Linux/Unix-based environments do, but Windows based environments rarely do.

- Function declare is like prototype header `double square(double);`
- Function definition is `double square(double){ return ;}`

# 1.4.2 Initialization

# 1.6 Constants

**const**: Calculated during run time but compiler try to enforce it to not be modified.

**constexpr**: Calculated during compile time.

To use a function in constexpr expression, function must also be defined as constexpr.

```
constexpr double square(double x) { return x*x; }
constexpr double max1=1.4*square(16);
```

