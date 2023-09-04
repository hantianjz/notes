---
publish: true
review-frequency: normal
---
2021-12-31-Fr
Link: [[253665-sdm-vol-1.pdf]]
Type:: #notes
Tags:: [[x86]]

# 5 Instruction Set Summary

## 5.1 General-Purpose Instructions

Basic data movement, arithmetic, logic, program flow, and string operations. Operate on memory, GP registers, EFLAGS register. Address information from memory, GP register, and segment registers.

Groups of instruction include:
* data transfer
* binary integer arithmetic
* decimal arithmetic
* logic operations
* shift and rotate
* but and byte operations
* program control
* string
* flag control
* segment register operations
* miscellaneous subgroups

NOTE: Skipped most of sub-sections in 5.1 since it is just listing instruction, which was not too interesting.

## 5.2 X87 FPU Instructions

x87 FPU instruction runs on the x87 FPU, operating on floating-point integer, and binary-coded decimal operands.

NOTE: Again skipped most of sub-sections in 5.2.

## 5.3 X87 FPU and SIMD State management Instructions

FXSAVE; FXRSTOR. Two state management instructions.

## 5.4 MMX Instructions

4 extensions in IA-32 for SIMD operations. MMX opearate on packed byte, word, doubleword, or quadword integer operands. Subgroups in data transffer, conversion, packed arithmetic, comparison, logical, shift and rotate, and state management instructions.

NOTE: Again skipped most of sub-sections in 5.4.

## 5.5 SSE Instructions

4 Subgroups:
- SIMD single-precision floating-point instructions operate on XMM registers
- MXCSR state management instructions
- 64-bit SIMD integer instructions that operate on the MMX registers
- Cacheability control, prefetch, and instruction ordering instructions

NOTE: Again skipped all sub-sections in 5.5.

## 5.6 SSE2 Instructions

SSE2 extends MMX and SEE extensions.

## 5.7 SSE3 Instructions

13 instructions accelerate SSE(Streaming SIMD Extensions), SSE2, and x87-FP match.

## 5.8 Supplemental Streaming SIMD Extensions 3 (SSSE3) Instructions

32 instructions to accelerate computations on packed integers.

## 5.9 SSE4 Instructions

54 new instructions. 47 referred to as SSE4.1, and 7 as SSE4.2.

## 5.10 SSE4.1 Instructions

47 new instructions.

## 5.11 SSE4.2 Instructions

7 new instructions.

## 5.13 AESNI and PCLMULQDQ

6 AESNI instructions accelerated primitives for block encryption/decryption for AES. PCLMULQDQ instruction is carry-less multiplication 2 64-bit number.

## 5.13 Intel Advanced Vector Extensions (INTEL AVX)

Legacy 128-bit SIMD instruction operate on XMM, use VEX prefix, and YMM.

## 5.14 16-Bit Floating-Point Conversion

Conversion between single-precision floating-point (32-bit) and half-precision FP (16-bit).

## 5.15 Fused-Multiply-Add (FMA)

Enhances Intel AVX with high-throughput, arithmetic capabilities.

## 5.16 Intel Advanced Vector Extensions 2 (INTEL AVX2)

Promote 128-bit SIMD integer with 256-bit processing capabilities.

## 5.17 Intel Transactional Synchronization Extensions (INTEL TSX)

## 5.18 Intel SHA Extensions

Accelerate SHA-1 and SHA-256 variants

## 5.19 Intel Advanced Vector Extensions 512 (INTEL AVX-512)

512-bit SIMD instruction sets. Support 512-bit, 256, and 128-bit vector.

## 5.20 System Instructions

Control processor function to support OS.

## 5.21 64-Bit Mode Instructoins

New instruction running for 64-Bit mode

## 5.22 Virtual-Machine Extensions

Can not be executed in compatibility mode, else generate invalid-opcode exception.

## 5.23 Safer Moder Extensions

GETSEC instructions leaves Safer Mode Extensions (SMX).

## 5.24 Intel Memory Protection Extensions

Allow software to add bounds checking to memory references.

## 5.25 Intel Security Guard Extensions

Two sets of instructions to enable creation of protected container (enclave).

SGX1 introduced in 6th Gen Intel Core Processors.