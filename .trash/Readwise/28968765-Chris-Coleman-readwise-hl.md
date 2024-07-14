---
tags: #readwise-articles
aliases: How to Debug a HardFault on an ARM Cortex-M MCU
link: [[arm]] [[embedded]] [[mcu]] [[programming]]
---
# How to Debug a HardFault on an ARM Cortex-M MCU

## Metadata
- Author: [[Chris Coleman]]
- Full Title: How to Debug a HardFault on an ARM Cortex-M MCU
- Summary: A community and blog for embedded software makers
- URL: https://interrupt.memfault.com/blog/cortex-m-fault-debug

## Highlights
- `BFARVALID` - Indicates that the *Bus Fault Address Register* (**BFAR**), a 32 bit register located at `0xE000ED38`, holds the address which triggered the fault. We’ll walk through an example using this info [below](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#bad-address-read-example). ([View Highlight](https://read.readwise.io/read/01h2wzjtmc7x0egbfvvhkpmnjt))
- Instruction fetches and data loads should always generate *synchronous* faults for Cortex-M devices and be precise. Conversely, store operations can generate *asynchronous* faults. This is because writes will sometimes be buffered prior to being flushed to prevent pipeline stalls so the program counter will advance before the actual data store completes. ([View Highlight](https://read.readwise.io/read/01h2vsxcc65m8tcnfq1demrt5c))
- Upon exception entry, the active stack pointer is encoded in bit 2 of the `EXC_RETURN` value pushed to the link register. If the bit is set, the `psp` was active prior to exception entry, else the `msp` was active. ([View Highlight](https://read.readwise.io/read/01h2vv8xk3643e4xnch285zpve))
---
tags: #readwise-articles
aliases: How to Debug a HardFault on an ARM Cortex-M MCU
link: [[arm]] [[embedded]] [[mcu]] [[programming]]
---
# How to Debug a HardFault on an ARM Cortex-M MCU

## Metadata
- Author: [[Chris Coleman]]
- Full Title: How to Debug a HardFault on an ARM Cortex-M MCU
- Summary: A community and blog for embedded software makers
- URL: https://interrupt.memfault.com/blog/cortex-m-fault-debug

## Highlights
- `BFARVALID` - Indicates that the *Bus Fault Address Register* (**BFAR**), a 32 bit register located at `0xE000ED38`, holds the address which triggered the fault. We’ll walk through an example using this info [below](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#bad-address-read-example). ([View Highlight](https://read.readwise.io/read/01h2wzjtmc7x0egbfvvhkpmnjt))
- Instruction fetches and data loads should always generate *synchronous* faults for Cortex-M devices and be precise. Conversely, store operations can generate *asynchronous* faults. This is because writes will sometimes be buffered prior to being flushed to prevent pipeline stalls so the program counter will advance before the actual data store completes. ([View Highlight](https://read.readwise.io/read/01h2vsxcc65m8tcnfq1demrt5c))
- Upon exception entry, the active stack pointer is encoded in bit 2 of the `EXC_RETURN` value pushed to the link register. If the bit is set, the `psp` was active prior to exception entry, else the `msp` was active. ([View Highlight](https://read.readwise.io/read/01h2vv8xk3643e4xnch285zpve))
