---
publish: true
review-frequency: normal
link:
- '[[arm]]'
- '[[embedded]]'
- '[[arduino]]'
tags:
- idea
---
# Adafruit playground express

![[circuit_playground_express-labeled.jpg]]

# Schematic
![[playground_express_schem.png]]

# MCU:
**ATSAMD21:**
 - 21 = Cortex M0 + CPU, Basic Feature Set + DMA + USB

**G18A-U:**
- G  = 48 Pins WLCSPS
- 18 = 256KB Flash
- A  = Default variant
- U  = WLCSP package

# SWD/JTAG connection:
![[adafruit_playground_e_swd_pins.png]]

## 5 Pins to solder:
- 3.3V VREF
- GND
- SWDIO
- SWCLK
- RESET

# ARM-NONE-EABI-GCC
## Common flags
`-march=armv6-m`
or
`-mcpu=cortex-m0+`

`-float-abi=soft`: Cortex-M0+ does not have HW floating point. [Ref](https://en.wikipedia.org/wiki/ARM_Cortex-M)

`-mabi=aapcs`: **The AAPCS embodies the fifth major revision of the APCS** and third major revision of the TPCS. It forms part of the complete ABI specification for the ARM Architecture.

## Linking flags
`--specs=nosys.specs -lnosys -lc`

# Blinky FW
Generic LED at PA17

The factory bootloader seems to have some kind of flash protection preventing the bootloader from being erased.
```
Cortex-M0 identified.
J-Link>erase
Without any given address range, Erase Chip will be executed
Erasing device...

****** Error: Failed to erase sectors 0 @ address 0x00000000 ((sector is locked))
Failed to erase sectors.

J-Link: Flash download: Total time needed: 0.158s (Prepare: 0.128s, Compare: 0.000s, Erase: 0.021s, Program: 0.000s, Verify: 0.000s, Restore: 0.008s)
ERROR: Erase returned with error code -5.
```

Seems like the bootloader is 8KB, with [[SAMD21 NVMCTRL Bootprot]] bits  `BOOTPROT == 0x2`

# Delay don't really work
After loading the Arduino Core and FW into our own GN build template
It turns out the SysTick_DefaultHandler that is part of the Arduino core is really important to time keeping.

---
# References
Product page: https://learn.adafruit.com/adafruit-circuit-playground-express
Schematic: https://learn.adafruit.com/assets/49671
Pin Map: https://cdn-learn.adafruit.com/assets/assets/000/049/780/original/Adafruit_Circuit_Playground_Express_Pinout.pdf