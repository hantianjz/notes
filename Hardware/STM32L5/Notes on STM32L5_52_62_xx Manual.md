---
publish: true
review-frequency: normal
link:
- '[[arm]]'
- '[[Cortex-M]]'
- '[[STM32]]'
tags:
- documentation
---

# STM32L5_52_62_xx Manual

# 2. Memory and bus architecture

-   M33 32-bit RISC
-   Run up to 110 MHz
-   MPU supporting 8 region both secure/non-secure world
-   Configurable security attribution unit, 8 region

## 2.1 System architecture

![[stm32_sys_arch.png]]

## 2.2 TrustZone security architecture

-   TZEN option bit in FLASH_OPTR activate trustzone security
-   CPU: Secure state after reset. Boot address in secure address region
-   Memory map: