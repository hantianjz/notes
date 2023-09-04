---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #idea
Tags:: [[arm]], [[link script]], [[hardfaults]], [[gcc]]

# How to implement and use .noinit RAM

MCU often need to go through a soft reset for various reasons, I.E. Hardfault, Assertion, scheduled reboot. And often there are data that needs to be persisted across the reboot. One can store these data onto persistent memory, but that is often slow and expensive. And one needs to worry about wear leveling for more frequent data writes.

Create dedicated memory region via the [[How to write Linker Script|link script]].
```c
MEMORY
{
  FLASH  (rx)  : ORIGIN = 0x08000000, LENGTH = 1M
  RAM    (rwx) : ORIGIN = 0x20000000, LENGTH = 128K - 0x100
  /* Put a noinit region at the top 256 bytes of RAM  */
  NOINIT (rwx) : ORIGIN = 0x20000000 + 128K - 0x100, LENGTH = 0x100
}

SECTIONS
{
  ...
  .noinit (NOLOAD):
  {
    /* place all symbols in input sections that start with .noinit */
    KEEP(*(*.noinit*))
  } > NOINIT
  ...
}
```

To put symbol into `.noinit` region do:
```c
// For GCC or Clang or derived toolchains, use the "section" __attribute__ .
__attribute__((section(".noinit")) volatile int my_non_initialized_integer;

// for IAR EWARM, it varies, but typically:
__no_init volatile int my_non_initialized_integer @ ".noinit";
```

Generate `.map` file during linking to verify symbol is placed correctly, use [[GCC ARM-NONE-EABI toolchain|gcc options]] during linking stage `-Wl,-Map=app.map`.

`.map` file look something like:
```
.noinit         0x000000002001ff00       0x04
 *(*.noinit*)
 .noinit        0x000000002001ff00       0x04 build/src/main.o
                0x000000002001ff00                my_non_initialized_integer
```

PS: If the system uses a bootloader, the bootloader needs to also have the same mapping for `.noinit` region.

---
# References
https://interrupt.memfault.com/blog/noinit-memory