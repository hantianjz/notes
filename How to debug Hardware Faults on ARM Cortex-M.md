---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #idea
Tags:: [[arm]], [[hardfaults]], [[Cortex-M]]

# How to debug Hardware Faults on ARM Cortex-M

# Hardware Faults
The [[What is ARM Vector Table|Vector table]] is a table of function address for fault handler or interrupt handler to call.

## Configurable Fault Status Registers (CFSR) - 0xE000ED28

Comprised of three different status registers – UsageFault, BusFault & MemManage Fault Status Registers:
![[cfsr.png]]

`gdb> print/x *(uint32_t *) 0xE000ED28`

*PS: Is not available for Cortex-M0*

### UsageFault Status Register (UFSR) 0xE000ED2A
![[ufsr.png]]
- **DIVBYZERO**: divid instruction executed with denominator was zero. (configurable)
- **UNALIGNED**: Unaligned access operation (configurable, Except M0)
- **NOCP**: Use co-processor instruction, but disabled or not exist.
- **INVPC**: Reserved `EXC_RETURN` value used on exception exit.
- **INVSTATE**: Attempted to execute instruction with invalid *Execution Program Status Register (EPSR)* 
- **UNDEFINSTR**: Undefined instruction execution

### Configuration and Control Register (CCR) 0xE000ED14
- **DIV_0_TRP**: Bit 4, control if divid by zero trigger a fault
- **UNALIGN_TRP**: Bit 3, control if unaligned access trigger a fault

*PS: Disable on reset by default.*

### BusFault Status Register (BFSR) 0xE000ED29
![[bfsr.png]]
- **BFARVALID**: Indicate `BFAR` @`0xE00ED38` hold address which triggered the fault.
- **LSPERR** & **STKERR**: Fault during lazy state preservation, or exception entry. HW automatically saving state on the stack. [[How to Debug a HardFault on an ARM Cortex-M MCU#^26410d|ref]]
- **UNSTKERR**: Fault while return from an exception. [[How to Debug a HardFault on an ARM Cortex-M MCU#^cc0b06|ref]]
- **IMPRECISERR**: Indicate if HW was able to determine location of fault.
- **PRECISERR**: Indicate the instruction prior to exception entry triggered the fault.

### Imprecise Bus Error
Result of asynchronous faults, where it is not exactly clear which instruction caused the fault.
One example is that write operations can be buffered to prevent pipeline stalls, hence PC will advance, but actual invalid data store will trigger fault later.
[[How to Debug a HardFault on an ARM Cortex-M MCU#^09ddc3|ref]]

### Auxiliary Control Register (ACTLR) 0xE000E008
Cortex M3 & M4 allows disabling any write buffering via `DISDEFWBUF`, force all asynchronous faults to be synchronous always. 

### Auxiliary Bus Fault Status Register (ABFSR) 0xE000EFA8
Cortex M7 only.
![[ABFS.png]]

### MemManage Status Register (MMFSR) 0xE000ED28
![[mmfsr.png]]
Typically only used triggered when MPU is used, but also possible when executing from system address range `0xExxx.xxxx`

- **MMARVALID**: Indicate `MMFAR` @ `0xE000ED34` hold address triggered the mem Fault.
- **MLSPERR** & **MSTKERR**: Mem fault during lazy state preservation or exception entry.
- **MUNSTKERR**: Fault while return from exception
- **DACCVIOL**: Data access trigger mem fault
- **IACCVIOL**: Instruction execution trigger MPU or Execute Never fault.

## HardFault Status Register (HFSR) - 0xE000ED2C
![[hfsr.png]]
- **DEBUGEVT**: Debug event while debug subsystem not enabled
- **FORCED**: Fault during fault, or fault handler not configured
- **VECTTBL**: Issue reading from vector table

## PSP vs MSP
Upon exception entry *LR* AKA (`EXC_RETURN`) is pushed to the stack, with it also encoded the stack used.
Bit 2 of *LR*  is **SET** is `psp` is used, else `msp`
[[How to Debug a HardFault on an ARM Cortex-M MCU#^f60024|ref]]

---
# References
- https://interrupt.memfault.com/blog/cortex-m-fault-debug