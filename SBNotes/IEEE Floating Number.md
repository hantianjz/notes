# IEEE Standard 754 Floating Point Numbers

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
- expoent
- mantissa

Mantissa include *fraction* and implicit leading digit. Exponent base is 2, and is implicit.

 |  Sign | Exponent | Fraction
-|-------|----------|---------
Single Precision | 31 (1) | 30-23 (8) | 22-00 (23)
Double precision | 63 (1) | 62-52 (11) | 51-00 (52)

## The Sign bit

Single bit; 0 denote positive, 1 negative.

## The Exponent

Represent both positive and negative exponents, by adding a bias to the actual expoent.

The bias is calculated by dividing the max possible value of sign by 2.

Example: Single-precision exponent have 8 bits. The maximum possible value is 2^8 - 1 = 255. The bias for single-precision is then 255 / 2 = **127**.
Double-Precision bias equal **1023**

In single-precision a exponent value of 73 is converted to **200** (73 + 127)

## The mantissa

AKA significand. Composed of implicit leading bit (left of the radix point) (represented in base 2), and fraction bits (to the right of radix point)