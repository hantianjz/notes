2021-12-29-We
Type: #idea
Tags: [[arm]], [[hardfaults]], [[Cortex-M]]

# How to debug Hardware Faults on ARM Cortex-M

# Hardware Faults
The [[What is ARM Vector Table|Vector table]] is a table of function address for fault handler or interrupt handler to call.

## Configurable Fault Status Registers (CFSR) - 0xE000ED28

Comprised of three different status registers – UsageFault, BusFault & MemManage Fault Status Registers:
![[cfsr.png]]
*PS: Is not available for Cortex-M0*

### UsageFault Status Register (UFSR) 0xE000ED2A
![[ufsr.png]]

### BusFault Status Register (BFSR) 0xE000ED29
![[bfsr.png]]

### MemManage Status Register (MMFSR) 0xE000ED28
![[mmfsr.png]]

## HardFault Status Register (HFSR) - 0xE000ED2C
![[hfsr.png]]

---
# References
[Reference](https://interrupt.memfault.com/blog/cortex-m-fault-debug) #interrupt_memfault 