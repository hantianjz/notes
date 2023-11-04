---
publish: true
reviewed: 2022-12-29
review-frequency: normal
link:
- '[[arithmetic]]'
- '[[integers]]'
- '[[C]]'
tags:
- documentation
---

# The usual Arithmetic Confusions

## [Integer Literals](https://en.cppreference.com/w/cpp/language/integer_literal)
```cpp
void f() {
  auto x1 = 1;   // Integer literal 1 will have type int
  auto x2 = 1U;  // Integer literal 1L will have type unsigned int
  auto x3 = 1L;  // Integer literal 1L will have type long int
  auto x4 = 1UL; // Integer literal 1UL will have type unsigned long int
}
```
https://cppinsights.io/s/0ffee264

## Signed unsigned compare
```cpp
std::cout << (-1L < 1U); // What will this output?
// Outputs 1 when using -m64 (LP64) compiler option
// Outputs 0 when using -m32 (ILP32) compiler option
// Why should the result of a relational operator depend
// on the size of long and unsigned int?
```
[Different result using -m32 vs -m64 compiler options](https://godbolt.org/z/83qfWh3vr)
- If both compared value is positive this is not an issue but one is negative
- When `-1L` is promoted from a signed to unsigned value it become a very large unsigned int value
- During comparison both type needs to be the same, and default is to promote smaller type to the bigger type
- LP64 (-m64) compiler treat `U`(unsigned int) as the smaller type
    - Resulting `1U` casting to long int
- ILP32 (-m32) compiler treat `L`(long int) as the smaller type
    - Resulting `-1L` casting to unsigned int


---
# References
- [Shfik](https://shafik.github.io/c++/2021/12/30/usual_arithmetic_confusions.html)