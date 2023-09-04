---
publish: true
review-frequency: normal
---
2021-12-31-Fr
Link: [[253665-sdm-vol-1.pdf]]
Type:: #notes
Tags:: [[x86]]

# 6 Procedure calls, Interrupts, and Exceptions

This chapter describes the facilities in the Intel 64 and IA-32 architectures for executing calls to procedures or subroutines. It also describes how interrupts and exceptions are handled from the perspective of an application
programmer.

## 6.1 Procedure Call Types

Procedure calls through:
- *CALL* and *RET* instructions
- *ENTER* and *LEAVE* conjunction with *CALL* and *RET*

Both mechanisms use stack, procedure stack. Interrupt and exception handling is similar to using *CALL* and *RET*.

## 6.2 Stacks

Contained in a segment identified in SS register. Any where within the address space in flat-layout. Up to 4GBytes, or max length of a segment.

*PUSH* and *POP* to add/remove item to/from the stack. Push decrement *ESP*, pop increment *ESP*. Stack grows **down** in memory.

Number stacks only limited by max number of segments and available physical memory. Only a single stack is used at once, indicated by SS selector.

### 6.2.1 Setting Up a Stack

1. Establish a stack segment.

2. Load stack segment into SS, with MOV, POP, LSS

3. Load stack pointer into ESP, with MOV, POP, LSS. (LSS can setup both ESP and SS)

### 6.2.2 Stack Alignment

Stack pointer should aligned to 16-bit or 32-bit, which is the stack width. D flag in segment descriptor of code segment sets the stack-segment width. Exception to stack alignment is when contents of segment register is pushed to 32-bit wide stack, processor auto adjust stack pointer to next 32-bit boundary.

Stack misalignment could cause program error, or performance degradation. But not directly trigger a processor error.

### 6.2.3 Address-Size Attributes for Stack Accesses

Instructions of implicit stack usage have 2 implicit address-size attributes. Also can have explicit memory address, which attribute determined by D flag of current code segment, or usage of 0x67 address-size prefix.

Address-size attribute of SP or ESP is determined by B flag of segment descriptor. Clear indicate 16-bit, set is 32-bit.

### 6.2.4 Procedure Linking Information

Procedures use 2 pointers: stack-frame base pointer, and return instruction pointer.

#### 6.2.4.1 Stack-Frame Base Pointer

Stack frame base pointer, *EBP* register. At beginning of procedure call, before any stack push, *ESP* is copied into *EBP*. *EBP* is then used by the procedure as a fixed pointer to access local variables.

#### 6.2.4.2 Return Instruction Pointer

*CALL* instruction push *EIP* to current stack, before actual branching. *RET* instruction pops the return-instruction from stack back to *EIP*. The procedure call need to ensure when *RET* is called *ESP* is pointing to the correct return-instruction address. Common method to reset stack pointer is to copy *EBP* to *ESP*.

### 6.2.5 Stack Behavior in 64-Bit Mode

64-bit mode, SS segment assumed as zero. *E(SP)*, *E(IP)*, *E(BP)* are promoted to 64-bits, and rename *RSP*, *RIP*, and *RBP*. *PUSH* and *POP* is 64-bit stack width.

## 6.3 Calling Procedures Using CALL and RET

**Near call** procedure call within same code segment, local procedure of same program or task. **Far call** procedure call to different code segment, access operating system procedures or different task. *RET* match *CALL* for both near and far call.

*RET* allow optional argument to increment stack pointer by *n* bytes.

### 6.3.1 Near CALL and RET Operation

*CALL*:
1. Push current value of *EIP* to stack.
2. Load offset of new instruction-address to *EIP*.
3. Begin called procedure.

*RET*:
1. Pop top of stack into *EIP*.
2. increment stack pointer by *n* bytes if optional argument used.
3. Resume execution.

### 6.3.2 Far CALL and RET Operation

*CALL*:
1. Push current *CS* to stack.
2. Push current *EIP* to stack.
3. Load new code segment selector to *CS*.
4. Load offset of new instruction-address to *EIP*.
5. Begin called procedure.

*RET*:
1. Pop top of stack to *EIP*.
2. Pop top of stack to *CS*.
3. Increment stack pointer by *n* bytes if optional argument used.
4. Resume execution.

### 6.3.3 Parameter Passing

3 methods: GP registers, an argument list, or stack

#### 6.3.3.1 Passing Parameters Through the General-Purpose Registers

A calling procedure can pass up to 6 parameters, using any register except *ESP* and *EBP*.

#### 6.3.3.2 Passing Parameters on the Stack

For passing larger number of parameter. Uses the stack-frame base pointer for easier access to parameters.

#### 6.3.3.3 Passing Parameters in an Argument List

Use a data structure placed on the data segment.

### 6.3.4 Saving Procedure State Information

The calling procedure should save needed GP registers before a *CALL* and restore them after resumed execution. *PUSHA* and *POPA* handle the saving/restoring of GP registers. *PUSHA* saves GP in following order: *EAX*, *ECX*, *EDX*, *EBX*, *ESP*, *EBP*, *ESI*, *EDI*. *POPA* restore everything saved by *PUSHA* EXCEPT *ESP*.

Segment register should NOT be changed by called procedure.

*PUSHF*/*PUSHFD* and *POPF*/*POPFD*, save and restore the *EFLAGS* register. With either lower word of *EFLAGS* or full double word.

### 6.3.5 Calls to Other Privilege Levels

4 Privilege levels, 0 to 3, from more to less privilege, from kernel to application code. Lower privileged segments access higher privileged using protected interface **gate**. Without sufficient access rights, general-protection exception (#GP) is generated. Call to higher privileged level is similar to a **far call**, except the *CALL* instruction references a special data structure **call gate descriptor**.

The call gate descriptor provide:
* access rights information
* the segment selector for the code segment of the called procedure
* an offset into the code segment

The processor also switch to new stack to execute called procedure. Each privilege level have it's own stack. Segment selectors and stack pointers for privilege level 2, 1, and 0 are stored in system segment, **task state segment (TSS)**.

### 6.3.6 CALL and RET Operation Between Privilege Levels

Calls into higher privilege level:
1. Performs access right check
2. Temporarily saves (internally) *SS*, *ESP*, *CS*, and *EIP* registers
3. Load segment selector and stack pointer for new stack from TSS.
4. Pushes saved *SS* and *ESP* to new stack
5. Copy parameters to new stack, call gate descriptor determines how many parameters to copy
6. Push saved *CS* and *EIP* to new stack
7. Load new code segment, and instruction-address to *CS* and *EIP*.
8. Begin called procedure

Return from privileged procedure:
1. Perform privilege check.
2. Restore *CS* and *EIP*
3. Handle *RET* optional *n* argument if needed. If parameters copied to new stack, *n* MUST specify number of bytes copied to stack for parameters
4. Restore *SS* ad *ESP*, switch back to calling stack.
5. handle *RET* optional *n* argument on calling stack.
6. Resume execution.

### 6.3.7 Branch Functions in 64-Bit Mode

Near-branch redefined in 64-Bit mode. Operand size of all near branch forced to 64-bit.

Near branches controlled by operand size:
* Truncation of size of instruction pointer
* Size of stack pop, push
* Size of stack-pointer increment/decrement
* Indirect-branch operand size

Call gate can be used to the same privilege level.

64-bit mode redefines type value of 32-bit call-gate descriptor type to 64-bit. Allows far branches to any location in the supported linear-address space. Hold target code selector. Only way to specify full 64-bit absolute *RIP* in 64-bit mode is with indirect branch, hence direct branch is eliminated from 64-bit mode. Expands *SYSENTER* and *SYSEXIT* to handle 64-bit memory space. New instructions *SYSCALL* and *SYSRET*.

## 6.4 Interrupts and Exceptions