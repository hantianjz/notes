---
publish: true
review-frequency: normal
---
Last Updated: 2022-12-29
Type:: #documentation 
Tags:: [[C]], [[integers]], [[unsigned integers]], [[Notes todo]]

# Almost Always Unsigned

## Reverse loop

```cpp
// Reverse loop with unsigned int
for (size_t i = size - 1; i < size; i--) {
    //...
}

// Reverse loop with signed int
for (int64_t i = int64_t(size) - 1; i >= 0; i--) {
    //...
}
```

- Unsigned int underflow behavior is well defined in C/Cpp
- Unsigned int are typically simpler overall, without the need for type conversion which are typically needed
- Bigger range, 0x0 - UINT64_MAX, instead of signed int with 0x0 - INT64_MAX

## Difference of 2 numbers
- Signed integer underflow is undefined
- Not trivial to do safely since signed int can be negative

```cpp
// Only safe way to do signed int abs diff calculation
if ((y > 0 && x < INT_MIN + y) || (y < 0 && x > INT_MAX + y)) {
    // error
} else {
    delta = abs(x - y);
}

// Unsigned int abs diff is much easier
delta = max(x, y) - min(x, y);
```

- PS: This only apply in application where the input source are guaranteed to be non negative, else you still have to deal with signed int.

## Indices math is easier

In the example of getting middle index value of an array.
```cpp
// int low
// int high
int mid = (low + high) / 2;
```

If `low + high > INT32_MAX` will overflow to a negative value and `mid < 0`.

The unsigned version is NOT much better, still produce the wrong value, just bounded within a valid range.
```cpp
size_t mid = (low + high) / 2;
```

The only safe way to do this regardless of signedness
```cpp
T midpoint(T x, T y) {
    // U is the unsigned version of your type T, or same as T if T already unsigned
    // digits is the number of numeric digits (not including sign) in your type T.
    // std::numeric_limits<T>::digits in C++ is helpful here.
    U shift = digits - 1;
    U difference = (U)x - (U)y;
    U sign = y < x;
    U half = (difference / 2) + (sign << shift) + (sign & difference);
    T mid = (T)(x + half);
    return mid;
}
```

```c
int32_t int32_midpoint(int32_t x, int32_t y) {
    uint32_t shift = 32 - 1;
    uint32_t difference = (uint32_t)x - (uint32_t)y;
    uint32_t sign = y < x;
    uint32_t half = (difference / 2) + (sign << shift) + (sign & difference);
    int32_t mid = (int32_t)(x + half);
    return mid;
}
```

## Multiplication overflow
- Both sign and unsigned face the same problem.

Check if `x*y` would overflow:
```cpp
if (y && x > (T)-1/y)
// (T) being the unsign type or use
// ~((T)0) or UINT{8,16,32,64}?_MAX
```


## Sentinel values
Using signed negative value to indicate error code.


---
# References
- [graphitemaster AAU](https://graphitemaster.github.io/aau/)