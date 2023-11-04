---
publish: true
review-frequency: normal
link:
- '[[Cpp]]'
- '[[parsing]]'
- '[[syntax]]'
tags:
- documentation
---

# Cpp The most vexing parse

Syntactic ambiguity resolution in C++. Certain situation C++ grammar cannot distinguish between the creation of an object parameter and specification of a function's type.

Compiler is required to interpret the line as a function type specification.

## C-Style casts
```cpp
void f(double my_dbl) {
    int i(int(my_dbl));
}
```

Line 2 is ambiguous, this is either:
- declare variable `i` with init value produced by converting `my_dbl` to an `int`
- Or function declaration of a function named `i` that takes integer or returns a  int.

to avoid the ambiguity do named cast instead:
```cpp
int i(static_cast<int>(my_dbl));
```

## Unnamed temporary
```cpp
struct Timer {};

struct TimeKeeper {
  explicit TimeKeeper(Timer t);
  int get_time();
};

int main() {
  TimeKeeper time_keeper(Timer());
  return time_keeper.get_time();
}
```

`TimeKeeper time_keeper(Timer());` is ambiguous since:
- A definition of variable  `time_keeper` of class `TimeKeep`, initialized with `Timer`
- A function declaration for function `time_keeper` and a single unnamed parameter.

Compiler by requirement pick choice 2.
```
TimeKeeper time_keeper(Timer{});
// Or
TimeKeeper time_keeper( /*Avoid MVP*/ (Timer()) );
// Or
TimeKeeper time_keeper = TimeKeeper(Timer());
```
  
---
# References
- https://en.m.wikipedia.org/wiki/Most_vexing_parse