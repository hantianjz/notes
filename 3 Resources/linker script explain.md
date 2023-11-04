---
publish: false
reviewed: 2023-07-11
review-frequency: ignore
link:
- '[[todo]]'
- '[[linker]]'
- '[[link script]]'
tags:
- documentation
---

# linker script explain

## Output Format

Specify the elf format or platform to use and endianness 

```
OUTPUT_FORMAT("elf32-littlearm", "elf32-littlearm", "elf32-littlearm")
```

## Memory space definition

Specify memory layout of the executable to run on the system

```
MEMORY
{
    bootloader (rx) : ORIGIN = 0x00000000, LENGTH = BOOTLOADER_SIZE
    rom (rx) : ORIGIN = 0x00002000, LENGTH = FLASH_SIZE - BOOTLOADER_SIZE - NVM_SIZE
    nvm (r) : ORIGIN = FLASH_SIZE - NVM_SIZE, LENGTH = NVM_SIZE
    ram (rwx) : ORIGIN = 0x20000000, LENGTH = SRAM_SIZE
}
```

## Sections

Where to put input symbols and which memory region to place each section.

```
SECTIONS
{
}
```


---
# References
- https://blog.thea.codes/the-most-thoroughly-commented-linker-script/