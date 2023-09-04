---
publish: true
review-frequency: normal
link:
- '[[x86]]'
tags:
- notes
---
2021-12-31-Fr
Link: [[253665-sdm-vol-1.pdf]]

# 3 Basic Execution Environment

## 3.1 Modes of Operation

**Protected mode**: processor native state; directly execute "real-address mode"

**Real-address mode**: Switch to protected or System management mode; default mode out of power-up

**System management mode (SMM)**: Provide kernel platform specific functions, enter SMM on SMM interrupt (SMI) or from advanced programmable interrupt controller (APIC)

### 3.1.1 Intel 64 Arch

**Compatibility mode (sub-mode of IA-32e mode)**: Run 16-bit and 32-bit applications; and support 64-bit privilege levels; enabled on code segment basis.

**64-bit mode (sub-mode of IA-32e mode)**: Extends GP and SIMD extension reg from 8 to 16; GP widen to 64 bits; New opcode prefix (REX); Default address size 64bits, operand size 32bits.

## 3.2 Overview of the basic execution environment

**Address space**: Program can access linear address space of 4 GBytes (2^32 btes); physical address space of 64 GBytes (2^36 bytes).

**Stack**: ....

**Basic program execution registers**: 8 GP; 6 segment; EFLAGS; EIP;

**x87 FPU registers**: 8 FPU data; FPU control; status; FPU instruction pointer; FPU operand pointer; FPU tag; FPU opcode;

**MMX registers**: 8 MMX; support execution of SIMD operation on 64 bit packed byte.

**XMM registers**: 8 XMM data; MXCSR; support SIMD on 128 bit packed byte.

**YMM register**: YMM data; support SIMD on 256 bit packed single/double precision FP value

**Bounds register**: BND0-BND3 (4) register (64 bits); low+upper bound of mem buffer, support MPX instruction

**BNDCFGU + BNDSTATUS**: support MPX operations

Figure 3-1.  IA-32 Basic Execution Environment for Non-64-bit Modes

**System level resources**:

**I/O Ports**

**Control registers**: CR1 through CR4 (5); control operation mode and characteristics.

**Memory management registers**: GDTR, IDTR, task reg, LDTR.

**Debug registers**: DR0 through DR7 (8).

**Memory type range registers (MTRRs)**: assign memory type to region of memory.

**Machine specific registers (MSRs)**: control report processor performance.

**Machine check registers**: MSRs to detect report on hardware errors.

**Performance Monitoring counters**

### 3.2.1 64-Bit mode execution environment

**Address space**: Linear address space 2^64 bytes; Physical address space of 2^46 bytes; CPUID specify supported physical address size.

**Basic program execution registers**: 16 GPRs, 64 bits; 64 bits instruction pointer; 64 bits EFLAGS (renamed RFLAGS, upper 32 bits reserved, lower 32 bits unchanged);

**XMM registers**: 16 XMM data register.

**YMM registers**: 16 YMM data register.

**BND registers, BNDCFGU, BNDSTATUS**

**Stack**: 64 bits

**Control registers**: 64 bits; Task priority register (CR8 or TPR)

**Debug registers**: 64 bits

**Descriptor table registers**: Global descriptor table register (GDTR) and IDTR  10 bytes; Local descriptor table register (LDTR) and TR 64 bits base address.

Figure 3-2.  64-Bit Mode Execution Environment

## 3.3 Memory Organization

### 3.3.1 IA-32 Memory Models

Three possible memory models to be used by programs.

**Flat memory model**: continuous address space. AKA linear address space.

**Segmented memory model**: Separate segments for code, data, stack. Logical address == segment selector + offset. 16,383 possible segments, each 2^32 address space.

**Real-address model memory model**: For Intel 8086; compatibility for 8086 programs; Linear address between program and OS; segments of 64 KBytes; Max size 2^20 bytes.

### 3.3.2 Paging and Virtual Memory

Address space mapped to physical address space directly or through **paging**. Linear address space divided into pages, mapped to physical memory as needed.

Physical Address Extensions (PAE) to address physical address space greater than 4 GBytes.
Page Size Extensions (PSE) to map linear address to physical address in 4-MBytes pages.

Note: See also Chapter 3, Volume 3A.

### 3.3.3 Memory Organization in 64 Bit Mode

Intel 64 support greater than 64 GBytes, but can be implementation specific. May not implement the full 64bit addressing. Linear address mapped to physical address space through PAE.

### 3.3.4 Modes of Operation vs. Memory Model

**Protected mode**: Access to any memory model; actual usage vary with OS; user task can use different model from kernel.

**Real-address mode**: Processor only support Real-address mode.

**System management mode**: In System management RAM (SMRAM); similar to Real-address mode.

**Compatibility mode**: Same as 32 bit protected mode.

**64-bit mode**: Segmentation _generally_ disabled; flat 64 bit linear-address space; Segmented and real address mode not available.

### 3.3.5 32-Bit and 16-Bit Address and Operand Sizes

Protected mode can be configured for 32 bit or 16 bit address and operand sizes.
Instruction prefixes allow temporary overrider of address/operand sizes.

**32 bits**

* Max linear address or segment offset is 0xFFFFFFFF (2^32-1)
* Operand sizes are 8 bits or 32 bits
* Logical address is 16 bit segment selector; 32 bit offset

**16 bits**

* Max linear address or segment offset is 0xFFFF (2^16-1)
* Operand sizes are 8 bits or 16 bits
* Logical address is 16 bit segment selector; 16 bit offset

Segment descriptor defines the default address and operand size, put in by assembler.

### 3.3.6 Extended Physical Addressing in Protected Mode

A program access the physical address through linear address space of up to 4GBytes. Mapped to physical address space, up to 64 GByte, through virtual memory management.

### 3.3.7 Address Calculations in 64 Bit Mode

Flat address space. No address-size override. Linear address equal to effective address because base address is zero.

**Instruction Pointers**

**IP** == 16 bits; **EIP** == 32 bits; **RIP** == 64 bits;

TODO: re-read this part.

#### 3.3.7.1 Canonical Addressing

Intel 64 arch defines 64-bit linear address space, but implementation can support less. If an address from bit 63 to the implemented MSB is either all 1s or 0s, it is canonical. If memory address reference is not in canonical form, the implementation should generate an exception. A general-protection exception is generated \#GP, or \#SS for stack fault.

## 3.4 Basic program execution registers

* **General-purpose registers**
* **Segment registers**: Hold up to 6 segment selector.
* **EFLAGS (program status and control) register**: Report program status, limited application level control to processor
* **EIP register**: 32 bit instruction pointer

### 3.4.1 General-Purpose Registers

* EAX: Accumulator for operands and results data
* EBX: Pointer to data in the DS segment
* ECX: Counter for string and loop operations
* EDX: I/O Pointer
* ESI: Pointer to data in the segment pointed to by the DS register; source pointer for string operations
* EDI: Pointer to data (or destination) in the segment pointed to by the ES register; destination pointer for string operations
* ESP: Stack pointer (in the SS segment)
* EBP: Pointer to data on the stack (in the SS segment)

Figure 3-5. Alternate General-Purpose Register Names

#### 3.4.1.1 General-Purpose Registers in 64-Bit Mode

* 32 bit operand size, available register: EAX, EBX, ECX, EDX, EDI, ESI, EBP, ESP, **R8D - R15D**
* 64 bit operand size, available register: RAX, RBX, RCX, RDX, RDI, RSI, RBP, RSP, **R8 - R15**
* Accessable at byte, word, dword, and qword level. REX prefix generate 64-bit operand sizes.
* 64-Bit mode can not access legacy high-bytes.

### 3.4.2 Segment Registers

(CS, DS, SS, ES, FS and GS) hold 16 bit segment selectors.

CS for **code segment**, DS, ES, FS and GS for **data segment**, and SS for **stack segment**.

#### 3.4.2.1 Segment Registers in 64-Bit Mode

CS, DS, ES, SS are treated as segment base 0. Segment register loaded in 64-bit mode may be used in compatibility mode.

### 3.4.3 EFLAGS Register

32-bit register define groups of status, control and system flags. Reset state is 0x00000002. Bit 1,3, ,5, 15 and 22 - 31 is reserved.

Special purpose instruction to modify specific flags. Instruction to copy groups of flag to stack or EAX, LAHF, SAHF, PUSHF, PUSHEDFD, POPF, and POPFD. During context-switching processor automatically store/load EFLAGS to/from task state segment (TSS). During interrupt or exception the EFLAGS register is saved to procedure stack.

#### 3.4.3.1 Status Flags

* CF (bit 0)    **Carry flag**: Set if arithmetic operation generate a carry or borrow. Used in multiple-precision arithmetic.
* PF (bit 2)    **Parity flag**: Set if least significant byte of the result contains even number of 1s.
* AF (bit 4)    **Auxiliary Carry flag**: If an arithmetic operation generates carry or borrow out of bit 3 of the result. Used in binary-coded decimal arithmetic.
* ZF (bit 6)    **Zero flag**: Set if result is zero.
* SF (bit 7)    **Sign flag**: Set to most-significant bit of the result. (0 == positive; 1 == indicate negative)
* OF (bit 11)   **Overflow flag**: Set if result integer is too large or small to fit in destination operand.

Only **CF** can be modified directly using STC, CLC and CMC.

#### 3.4.3.2 DF Flag

DF (bit 10) direction flag. Controls string instructions, MOVS, CMPS, SCAS, LODS, and STOS. Set DF cause string instruction to auto-decrement, clear to auto-increment.

STD, and CLD instruction set and clear the DF flag, respectively.

#### 3.4.3.3 System Flags and IOPL Field

Controls OS operations, should **NOT** be modified by application program.

* TF (bit 8)    **Trap flag**: Set to enable single-step mode for debugging.
* IF (bit 9)    **Interrupt enable flag**: Set to respond to interrupt.
* IOPL (bits 12 and 13) **I/O privilege level field**
** I/O privilege level of current running program.
** The current privilege level (CPL) must be equal or less.
** POPE and IRET can modify if CPL == 0
* NT (bit 14)   **Nested task flag**: Set if current task linked to previously task.
* RF (bit 16)   **Resume flag**: Controls processor's responds to exceptions.
* VM (bit 17)   **Virtual-8086 mode flag**: Set to enable virtual 8086 mode.
* AC (bit 18)   **Alignment check (or access control) flag**:
** If set and CR0 register **AM** bit set, perform alignment checking of user-mode data access.
** If set and CR4 register **SMAP** bit set, explicit supervisor-mode data access to user-mode pages are allowed.
* VIF (bit 19)  **Virtual interrupt flag**: Virtual image of IF flag. (Used by virtual mode extension, CR4 VME)
* VIP (bit 20)  **Virtual interrupt pending flag**: Set to indicate interrupt is pending. (Used by virtual mode extension, CR4 VME)
* ID (bit 21)   **Identification flag**: The ability to set/clear this flag indicate support for CPUID instruction.

Note: Detailed description of flags: Chapter 3, Volume 3A.

#### 3.4.3.4 RFLAGS register in 64-Bit mode

EFLAGS extended to RFLAGS. Upper 32 bits of RFLAGS register is reserved, lower 32 bits is same as EFLAGS.

## 3.5 Instruction Pointer

EIP is controlled implicitly by control transfer instructions, interrupt, and exceptions. Read via *CALL* then read the value from procedure stack.

### 3.5.1 Instruction Pointer in 64-Bit Mode

EIP extened to RIP, 64 bits. Also support RIP-relative addressing, where effective address is determined by adding displacement.

## 3.6 Operand-size and Address-size attributes

Segment descriptor have flag D, selects default operand-size and address-size. If flag D is **set** 32-bit operand-size and address-size attributes are selected, if **clear** 16-bit is selected. In real-address mode, virtual-8086, or SMM, default size is always 16-bit.

**16-bit**: Operand-size 8 bits or 16 bits. Address-size 16 bits, limited segment size to 64 KBytes (2^16 bytes)

**32-bit**: Operand-size 8 bits or 32 bits. Address-size 32 bits, limited segment size to 4 GBytes (2^32 bytes)

**Operand-size Prefix 0x66**: Act like toggle to D flag, overriding default operand-size.

**Address-size Prefix 0x67**: Act like toggle to D flag, overriding default address-size.

### 3.6.1 Operand-size and Address-size in 64-Bit mode

Default **64 bits** operand-size and **32 bits** address-size. 16 bit address-size is **NOT** supported.

REX, 4 bit prefix, W field specifies operand size 64 bits. REX.W takes precedence over Prefix 0x66.

Table 3-4. Effective Operand- and Address-Size Attributes in 64-Bit Mode

## 3.7 Operand Addressing

Data for source operand can be located in:
* the instruction
* a register
* a memory location
* an I/O port

Result for destination operand can be returned to:
* a register
* a memory location
* an I/O port

### 3.7.1 Immediate Operands

Data encoded in the instruction as a source operand.

> ADD EAX, 14

All arithmetic instructions allow immediate operands. Max value varies with instruction, never larger than 2^32.

### 3.7.2 Register Operands

Any GP, segment, EFLAGS, x87 FPU, MMX, XMM, Control, debug, MSR registers.

Register can be paired like **EDX:EAX** for DIV instructions.

#### 3.7.2.1 Register Operands in 64-Bit mode

Similar to 32 bit mode, in addition to 64 bit version of the registers.

### 3.7.3 Memory Operands

Logical address contain segment selector (!6 bits); Linear address (or offset) (16 or 32 bits), notation m16:16 or m16:32 respectively.

#### 3.7.3.1 Memory Operands in 64-Bit modes

Segment selector (16 bits); Linear address (or offset) 16, 32, or 64 bits.

### 3.7.4 Specifying a Segment Selector

Common method, allow processor implicitly use segment selector from segment register based on operation.

Override DS segment, for store/load data memory. Within assembler override is done using a colon like:
> MOV ES:[EBX], EAX;

Segment override specified with single byte override prefix before instruction.

Default segments selection that can **NOT** be overridden:
* Instruction fetch from code segment
* Destination strings in string instruction to ES register
* Push and pop instruction to/from SS register

Can be explicitly specified as 48-bit far pointer in memory.

#### Segmentation in 64-Bit mode

Segmentation only used while in compatibility mode. Segmentation registers treated ZERO, except FS and GS.

### 3.7.5 Specifying an Offset

An address computation consist of these components:
* Displacement: 8, 16, or 32 bit value
* Base: value of a GP
* Index: value of a GP
* Scale factor: Value of 2, 4, or 8 that is multiple of a index value

Effective address = Base + Index * Scale + Displacement

Address modes:
* Displacement: AKA absolute or static address. 8, 16, 32 bit value.
* Base: Offset is the value in the base register.
* Base + Displacement: Base address + displacement value. Displacement can be used as index into an array or field in an object (record).
* (index * scale) + Displacement: Efficient way to index a static array where element size if 2, 4, 8 bytes, where displacement is base of the array.
* Base + Index + Displacement: Access two dimensional array
* Base + (index * scale) + Displacement: Two dimensional array.

#### 3.7.5.1 Specifying a offset in 64-Bit mode

Same as 32 bit mode.

Additional addressing mode:G
RIP + Displacement: Signed 32-bit displacement to calculate the effective address of next instruction.

### 3.7.6 Assembler and Compiler Addressing Modes

Assembler allow access to all addressing mode. High level language compiler will select appropriate combination of addressing mode.

### 3.7.7 I/O Port Addressing

I/O address space up to 65536 (2^16) 8-bit. Address via immediate operand or value in DX register.