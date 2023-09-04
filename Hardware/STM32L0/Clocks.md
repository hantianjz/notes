---
publish: true
review-frequency: normal
---
Last Updated: 2022-08-11
Type:: #documentation 
Tags:: [[STM32]], [[ARMv6M]], [[Clocks]]


# Clocks
- **Default startup clock** is MSI (multispeed internal) oscillator clock at 2.1MHz 
![[STM32L0 Clock Tree.png]]

## Systick
- AHB clock (HCLK) divided by 8 feeds SysTick

---
# References