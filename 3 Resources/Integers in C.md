---
publish: true
review-frequency: normal
link:
- '[[C]]'
- '[[integers]]'
- '[[data structure]]'
tags:
- idea
---
2021-12-29-We

# Intergers in C

# A Quiz About Integers in C

## Question 1
What does the expression 1 > 0 evaluate to?
- 0
- 1
- undefined

**Question 1 Explanation:**

Ok, great. That one was a freebie. Of course one is greater than zero.

## Question 2
What does the expression 1U > -1 evaluate to?
- 0
- 1
- undefined

**Question 2 Explanation:**

C has both signed and unsigned types, creating the potential for confusion when these are mixed. The simple version of the rule for resolving this situation (we'll get to the real version shortly) is that unsigned wins. In other words, if a signed value is compared against an unsigned, the signed value is cast to unsigned and then the comparison is performed between two unsigned values. Therefore, this comparison is actually between 1 and UINT_MAX, which evaluates to 0. Good C programmers often avoid mixing signed and unsigned values in the same expression. Good C compilers warn about this, but GCC only does so at fairly high warning levels.

## Question 3
What does the expression (unsigned short)1 > -1 evaluate to?
- 0
- 1
- undefined

**Question 3 Explanation:**

In this question, two signed values are being compared. In other words, the rule about converting one operand of a comparison to unsigned if one of them is unsigned does not apply. This is because C "promotes" both operands to arithmetic operators to int type before performing the operation. The rule for promotion states that an unsigned value is promoted to a signed int if (as is the case for promoting an unsigned short to an int) this can be done without losing values. On the other hand (as we saw in the previous question) an unsigned int is not promoted to signed int because this would change large values into negatives. The full rules for promotions are a bit more complicated than this, for example to handle the case of types like long that may be wider than int.

## Question 4
What does the expression -1L > 1U evaluate to on x86-64? On x86?
- 0 on both platforms
- 1 on both platforms
- 0 on x86-64, 1 on x86
- 1 on x86-64, 0 on x86

**Question 4 Explanation:**

This one is a little tricky because it asks you to analyze a feature interaction. On x86-64, int is shorter than long. Therefore, an unsigned int can be promoted to long, making the comparison signed. The comparison thus becomes -1L > 1L, which is false. On x86, int and long are the same size. Therefore, int cannot be promoted to long without changing values. On this platform, the comparison becomes UINT_MAX > 1U, which is true.

## Question 5
What does the expression SCHAR_MAX == CHAR_MAX evaluate to?
- 0
- 1
- undefined

**Question 5 Explanation:**

Sorry about that -- I didn't give you enough information to answer this one. The signedness of the char type is implementation-defined, meaning the each C implementation is permitted to make its own choice, provided that the choice is documented and consistent. ABIs for x86 and x86-64 tend to specify that char is signed, which is why I've said that "1" is the correct answer here.

## Question 6
What does the expression UINT_MAX + 1 evaluate to?
- 0
- 1
- INT_MAX
- UINT_MAX
- undefined

**Question 6 Explanation:**

The C standard guarantees that UINT_MAX+1 is 0.

## Question 7
What does the expression INT_MAX + 1 evaluate to?
- 0
- 1
- INT_MAX
- UINT_MAX
- INT_MIN
- undefined

**Question 7 Explanation:**

Overflowing a signed integer is an undefined behavior.

## Question 8
What does the expression -INT_MIN evaluate to?
- 0
- 1
- INT_MAX
- UINT_MAX
- INT_MIN
- undefined

**Question 8 Explanation:**

When using two's complement integers, INT_MIN has no representable inverse. Moreover, trying to compute it is an undefined behavior in C.

## Question 9
Assume x has type int. Is the expression x<<0...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 9 Explanation:**

Whoops... I thought this was always defined but as a couple of commenters point out, a negative value cannot be left-shifted even by zero bit positions.

## Question 10
Assume x has type int. Is the expression x<<1...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 10 Explanation:**

Shifting a 1 into the sign bit is an error in C99. Therefore, shifting a large value such as INT_MAX left by one bit position is an undefined behavior. Other values can be safely left-shifted.

## Question 11
Assume x has type int. Is the expression x<<31...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 11 Explanation:**

This is basically the same situation as the previous question. A 1 cannot be left-shifted into, or past, the signed bit. Therefore, I believe that 0 is the only value of type int that can be left-shifted by 31 bit positions without executing an undefined behavior.

## Question 12
Assume x has type int. Is the expression x<<32...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 12 Explanation:**

Shifting (in either direction) by an amount equalling or exceeding the bitwidth of the promoted operand is an error in C99.

## Question 13
Assume x has type short. Is the expression x<<29...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 13 Explanation:**

Operands to shift operators are promoted before the shift executes. Therefore, the fact that 29 is not less than 16 is irrelevant and a shift-past-bitwidth error does not occur.

## Question 14
Assume x has type unsigned. Is the expression x<<31...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 14 Explanation:**

Any value whose promoted type is "unsigned" can be legally shifted by an amount that is non-negative and also less than the width of the unsigned type.

## Question 15
Assume x has type unsigned short. Is the expression x<<31...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 15 Explanation:**

This one was just to make sure you've been paying attention. Since unsigned short is promoted to int, it is illegal to shift a 1 bit into or past the sign bit. If we shifted the value by 15 or fewer positions, the result would be defined for all values that can be stored in an unsigned short.

## Question 16
Assume x has type int. Is the expression x + 1...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 16 Explanation:**

Evaluating this expression is an undefined behavior iff x is INT_MAX.

## Question 17
Assume x has type int. Is the expression x - 1 + 1...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 17 Explanation:**

Since C's additive operators are left-associative, this expression is undefined iff x is INT_MIN. If these operators were right-associative, the expression would be defined for all values of x.

## Question 18
Assume x has type int. Is the expression (short)x + 1...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 18 Explanation:**

Any value of type int, after being truncated to short and then promoted back to int, can be safely incremented as long as the int type is wider than the short type.

## Question 19
Assume x has type int. Is the expression (short)(x + 1)...
- defined for all values of x
- defined for some values of x
- defined for no values of x

**Question 19 Explanation:**

Ok, that was an easy one. Of course the cast to short occurs too late to prevent the undefined behavior.

## Question 20
Does evaluating the expression INT_MIN % -1 invoke undefined behavior?
- who knows

**Question 20 Explanation:**

A bug in the quiz software prevented me from creating two correct answers for this question. But here's the explanation: This construct is widely treated as undefined by real C compilers because making it well-defined would reduce performance of generated code. My reading of the C99 standard is that it is not undefined. YMMV.

---
# References
https://pleasestopnamingvulnerabilities.com/integers.html