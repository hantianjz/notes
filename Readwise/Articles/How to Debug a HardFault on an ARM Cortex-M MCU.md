# How to Debug a HardFault on an ARM Cortex-M MCU

![rw-book-cover](https://interrupt.memfault.com/img/cortex-m-fault/cortex-m-fault-gdb-debug2.png)

## Metadata
- Author: [[Chris Coleman]]
- Full Title: How to Debug a HardFault on an ARM Cortex-M MCU
- Category: #articles
- Document Tags: [[arm]] [[embedded]] [[mcu]] [[programming]] 
- URL: https://interrupt.memfault.com/blog/cortex-m-fault-debug

## Highlights
- `LSPERR` & `STKERR` - Indicates that a fault occurred during lazy state preservation or during exception entry, respectively. Both are situations where the hardware is [automatically saving state on the stack](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#context-state-stacking). One way this error may occur is if the stack in use overflows off the valid RAM address range while trying to service an exception. We’ll go over an example [below](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#stkerr-example). ([View Highlight](https://read.readwise.io/read/01h2vsnm7pemeera7ekd0wpq2x)) ^26410d
- `UNSTKERR` - Indicates that a fault occurred trying to return from an exception. This typically arises if the stack was corrupted while the exception was running or the stack pointer was changed and its contents were not initialized correctly. ([View Highlight](https://read.readwise.io/read/01h2vsnrsnw1fw2dc5ferrpyab)) ^cc0b06
- Instruction fetches and data loads should always generate *synchronous* faults for Cortex-M devices and be precise. Conversely, store operations can generate *asynchronous* faults. This is because writes will sometimes be buffered prior to being flushed to prevent pipeline stalls so the program counter will advance before the actual data store completes. ([View Highlight](https://read.readwise.io/read/01h2vsxcc65m8tcnfq1demrt5c)) ^09ddc3
- Upon exception entry, the active stack pointer is encoded in bit 2 of the `EXC_RETURN` value pushed to the link register. If the bit is set, the `psp` was active prior to exception entry, else the `msp` was active. ([View Highlight](https://read.readwise.io/read/01h2vv8xk3643e4xnch285zpve)) ^f60024
## New highlights added June 13, 2023 at 11:22 PM
- Whether or not some classes of MemManage or BusFaults trigger a fault from an exception is actually configurable via the MPU_CTRL.HFNMIENA & CCR.BFHFNMIGN register fields, respectively. ([View Highlight](https://read.readwise.io/read/01h2vvkffw45vbvbm3320bvbfc))
## New highlights added June 14, 2023 at 9:23 AM
- `BFARVALID` - Indicates that the *Bus Fault Address Register* (**BFAR**), a 32 bit register located at `0xE000ED38`, holds the address which triggered the fault. We’ll walk through an example using this info [below](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#bad-address-read-example). ([View Highlight](https://read.readwise.io/read/01h2wzjtmc7x0egbfvvhkpmnjt))
