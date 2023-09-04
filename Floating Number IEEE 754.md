---
publish: true
review-frequency: normal
link:
- '[[floats]]'
- '[[data structure]]'
- '[[numbers]]'
tags:
- idea
---
2021-12-29-We

# Floating Number

## What are floating numbers?

Real number can be represented via:
- Fixed point
- decimal digits
- Rationals

Floating-point representation most common. Scientific notation with base number and exponent.

Fixed-point has fixed window of representation, limits very large or very small numbers. Floating point is *sliding window* of precision appropriate to the scale of number.

## Storage layout

3 components:
- sign
- exponent
- mantissa

Mantissa include *fraction* and implicit leading digit. Exponent base is 2, and is implicit.

|                 |  Sign  | Exponent   | Fraction  |
|-----------------|--------|------------|-----------|
|Single Precision | 31 (1) | 30-23 (8)  | 22-00 (23)|
|Double precision | 63 (1) | 62-52 (11) | 51-00 (52)|

## The Sign bit

Single bit; 0 denote positive, 1 negative.

## The Exponent

Represent both positive and negative exponents, by adding a bias to the actual exponent.
**exponent bias for float = 127 = 2^(8-1) - 1 **
**exponent bias for double = 1023 = 2^(11-1) - 1**

The bias is calculated by dividing the max possible value of sign by 2.

In single-precision a exponent value of 73 is converted to **200** (73 + 127)

## The mantissa

AKA significand. Composed of implicit leading bit (left of the radix point) (represented in base 2), and fraction bits (to the right of radix point)

## Special values

| sign | Exponent | Mantissa | Representation |
| ---- | -------- | -------- | -------------- |
| 0    | All 0's  | All 0's  | +0             |
| 1    | All 0's  | All 0's  | -0             |
| 0    | All 0's  | Not 0    | +Denormal      |
| 1    | All 0's  | Not 0    | -Denormal      |
| 0    | All 1's  | All 0's  | +Infinity      |
| 1    | All 1's  | All 0's  | -Infinity      |
| 0    | All 1's  | Not 0    | NaN            |
| 1    | All 1's  | Not 0    | NaN            |

## Manual Conversion

let `Value`: **3.14**
let `exp` = 0
let `frac` = 0

### calculate exponent value
If `value` > 1:
    Divide `value` by 2
    each division add 1 to `exp`
    until `value` is *normalized* where new `value` is 1 < `value` < 2
Elif `valeu` < 1:
    Multiple `value` by 2
    each multiplication subtract 1 from `exp`
    until `value` is *normalized* where new `value` is 1 < `value` < 2
`exp` = `exp` + 127 (or + 1023 for double)

Or simpler:

Log_2(`value`); require `value` to be positive value

`exp` == 2 + 127 (or + 1023 for double)

`value` == 1.57

### calculate mantissa value
> To convert any digits right of radix to some other base continuously multiple the value by the new base. Everything left of the radix is new digit and has to be subtracted prior to continuing the multiplications. Place the digits into the mantissa as you go.
> If get 0.0 from subtracting a digit, you are done rest are 0
> If reach the same state twice (same

use normalized `value` from calculate exponent step, sub the 1.0.
`value` = 0.57

for (int i=0; i < 23 &&`value`; i++) {
    `value` *= 2;
    if `value` > 1:
        next most sigfig mantissa value is 0
        `value` -= 1
    else:
        next most sigfig mantissa value is 0
    // But if `value` is one that had appear before this means a loop, therefore the mantissa value will also loop, and we can just duplicate the mantissa value
}

---
# References
