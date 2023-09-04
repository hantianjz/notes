---
publish: true
review-frequency: normal
---

2021-12-31-Fr
Link: [[253665-sdm-vol-1.pdf]]
Type:: #notes
Tags:: [[x86]]

# 4 Data Types

## 4.1 Fundamental Data Types

Bytes (8 Bit, 1 Byte), words (16 Bit, 2 Byte), doublewords (32 Bit, 4 Byte), quadwords (64 Bit, 8 Byte), and double quadwords (128 Bit, 16 Byte).

Quadword introduced in Intel486; Double quadword introduced in Pentium III with SSE extensions.

Data is stored as Little Endian.

### 4.1.1 Alignment of Words, Doublewords, Quadwords, and Double Quadwords

Words, doublewords, and quadwords does **NOT NEED** to be aligned. Natural boundaries are addresses evenly divisible by 2, 4, and 8, respectively. How ever boundaries aligned data improve performance of program.

Some instruction require double quadwords to be aligned, else generate general-protection exception GP. Natural boundaries of double quadword is address divisible by 16.

## 4.2 Numeric Data Types

Additional interpretations of data types is supported by some instructions.

### 4.2.1 Integers

Unsigned and signed integer.

#### 4.2.1.1 Unsigned Integers

Sometimes referred to as **ordinals**.

Values range:
Data Type | Range
----------|------
byte | 0 to 2^8 - 1    (255)
word | 0 to 2^16 - 1   (65525)
doubleword | 0 to 2^32 - 1
quadword | 0 to 2^64 - 1

#### 4.2.1.2 Signed Integers

Two's complement representation. Sign bit is the MSB.

Data Type | Range
----------|------
byte | -128    to  127
word | -32768  to  32767
doubleword | -2^31   to  2^31 - 1
quadword | -2^63   to  2^63 - 1

Integer indefinite is special value returned by x87 FPU operating on integer.

### 4.2.2 Floating-Pointer Data Types

Format from IEEE Standard 754 Binary Floating-Point Arithmetic.

Data Type | Length | Precision (Bits) | Range (Binary) | Range (Decimal)
----------|--------|------------------|----------------|----------------
Half Precision | 16 | 11 | 2^-14 to 2^15 | 3.1*10^-5 to 6.50*10^4
Single Precision | 32 | 24 | 2^-126 to 2^127 | 1.18*10^-38 to 3.40*10^38
Double Precision | 64 | 53 | 2^-1022 to 2^1023 | 2.23*10^- to 1.79*10^308
Double Extended Precision | 80 | 64 | 2^-16382 to 2^16383 | 3.37*10^-4932 to 1.18*10^4932

Table 4-3. Floating-Point Number and NaN Encodings

TODO: Need to actually understand Table 4-3

## 4.3 Pointer Data Types

32-Bit mode:

**Near pointer**: 32-Bit is offset only.

**Far pointer**: 16-Bit segment selector + 32-Bit offset.

### 4.3.1 Pointer Data Types in 64-Bit Mode

**Near pointer**: 64 bits

**Far Pointer**:
* 16-bit segment selector, 16-bit offset if operand size is 32 bits
* 16-bit segment selector, 32-bit offset if operand size is 32 bits
* 16-bit segment selector, 64-bit offset if operand size is 64 bits

## 4.4 Bit Field Data Type

A contiguous sequence of bits. It can begin at any bit position of any byte in meory and can contain up to 32 bits.

## 4.5 String Data Types

Continuous sequence of bits, bytes, words, or douwblewords. Bit string contain up to 2^32-1 bits, byte string range from 2^32 -1 bytes.

## 4.6 Packed SIMD Data type

Operate on 64-bit and 128-bit packed data type for SIMD operations.

### 4.6.1 64-Bit SIMD Packed Data Types

Introduced in Intel MMX technology, operate on MMX registers. Packed bytes, packed words, and packed double words. Operation interpreted as integer values.

### 4.6.2 128-Bit Packed SIMD Data Types

Introduced in SSE extensions, and used with SSE2, SSE3, and SSSE3 extensions. Operate on XMM registers and memory. Packed Bytes, Words, Doublewords and Quadwords. Operation interpreted as single precision, and double precision. Or byte, word, doubleword, and quadword integers.

## 4.7 BCD and Packed BCD Integers

Binary-coded decimal integers (BCD integers) unsigned 4-bit integers with value range 0 to 9.

Unpacked BCD values (one BCD digit per byte) or packed (two BCD digits per byte). When operating in x87 FPU data registers, BCD values packed as 80-bit format (decimal integers). First 9 byte hold 18 BCD digit. MSB of 10th byte is sign bit, 0-6th bit of 10th byte is don't care. (Negative BCD only differ on sign bit) Decimal integer is converted to double-extened-precision floating-point format when loaded into x87 FPU data register.

TODO: re-read this part, and finish the notes.

## 4.8 Real number and Floating-Point Formats

### 4.8.1 Real Number System

IA-32 represent a subset of real number system. Range and precision is determined by IEEE Standard 754 floating-point formats.

### 4.8.2 Floating-Point Format

For speed and efficiency real number represented in binary floating-point format. 3 parts, a sign, a significand, and an exponent.

Example: 178.125 => 1.0110010001 E_2 10000110
or Sign 0; Biased Exponent 10000110; Normalized Significand 011001000100000000000001 (implied)

#### 4.8.2.1 Normalized Numbers

Except for zero, significand always made up of a leading 1, else it is NOT normalized.

A normalized significand represent a real number between 1 and 2. An exponent that specifies the number's binary point.

#### 4.8.2.2 Biased Exponent

A constant is added to the exponent so it is always positive number. The value of biasing constant depends on the number of bits available for representing exponents. The biasing constant is chosen so that the smallest normalized number can be reciprocated without overflow.

TODO: Whyyyy???

### 4.8.3 Real Number and Non-number Encodings

Varies real numbers and special values can be encoded in the IEEE Standard 754 floating-point format.

Figure 4-12. Real Numbers and NaNs

#### 4.8.3.1 Signed Zeros

+0 or -0, all the same. The sign of zero depend on operation and rounding mode. Aid implementing interval arithmetic. Indicate direction of underflow occurred, sign of an infinity reciprocated.

#### 4.8.3.2 Normalized and Denormalized Finite Numbers

#### 4.8.3.3 Signed Infinities

#### 4.8.3.4 NaNs

#### 4.8.3.5 Operating on SNaNs and QNaNs

#### 4.8.3.6 Using SNaNs and QNaNs in Applications

#### 4.8.3.7 QNaN Floating-Point Indefinite

#### 4.8.3.8 Half-Precision Floating-Point Operation

### 4.8.4 Rounding

#### 4.8.4.1 Rounding Control (RC) Fields

#### 4.8.4.2 Truncation with SSE and SSE2 Conversion Instructions

## 4.9 Overview of Floating-Point Exceptions

### 4.9.1 Floating-Point Exception Conditions

#### 4.9.1.1 Invalid Operation Exception (#I)

#### 4.9.1.2 Denormal Operand Exception (#D)

#### 4.9.1.3 Divide-By-Zero Exception (#Z)

#### 4.9.1.4 Numeric Overflow Exception (#O)

#### 4.9.1.5 Numeric Underflow Exception (#U)

#### 4.9.1.6 Inexact-Result (Precision) Exception (#P)

### 4.9.2 Floating-Point Exception Priority

### 4.9.3 Typical Actions of a Floating-Point Exception Handler