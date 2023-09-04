---
publish: true
review-frequency: normal
---
2021-12-29-We
Author:: [[Henry Wong]]
Date published: JANUARY 9TH, 2014
Type:: #notes
Tags:: [[x86]], [[asm]]
Link: https://blog.stuffedcow.net/2014/01/x86-memory-disambiguation/

# Microarchtichture on x86 using Store to Load Forwarding

In pipelined processors, instruction are fetched, decoded, and executed speculatively, and are not permitted to modify system state until instruction commit. For instructions that modify registers, this is often achieved using register renaming. For stores to memory, speculative stores write into a store queue at execution time and only write into cache after the store instructions have committed.

[![Fig 1: Dependency carried through memory is difficult to track](http://blog.stuffedcow.net/wp-content/uploads/2014/01/ldst_code.png)](http://blog.stuffedcow.net/wp-content/uploads/2014/01/ldst_code.png)

Fig 1: Dependency carried through memory is difficult to track

A store queues introduces new problems, however. If a load is data-dependent on an earlier store, the load either has to wait until the store is committed before loading the value from cache, or the store queue must be able to forward the speculative store value to the load (**store-to-load forwarding**). This requires the processor to know whether a given load depends on an earlier not-yet-committed store, but this is much harder than figuring out register dependencies.

Fig. 1 illustrates the difficulty of learning memory dependencies. Register-carried dependencies (through `eax` in this code) are easy to figure out because the source and destination registers are specified in the instruction opcode. Memory addresses, on the other hand, are not known until after the address computation is executed. In this example, the lower two bytes of the load depends on the upper two bytes of the store (x86 is little-endian). If we wanted to execute memory instructions out of order (e.g., execute the load before the store), then we would need to know (non-speculative) or predict (speculative) whether a load depends on an earlier store (**memory dependence speculation**), and then later verify this guess (**memory disambiguation**).