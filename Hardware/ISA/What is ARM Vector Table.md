---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #idea
Tags:: [[arm]], [[vector table]], [[Cortex-M]], [[ARMv7]]

# What is ARM Vector Table

ARM boot/Reset vector table ARMv7-M7

Table contains:

-   Initial stack values
-   Entry point address to each exception handler (B1-634)

SW can relocate VT using VTOR reg (B3-716)'

Handler entry address bit[0] == 1 indicate load into EPSR.T (B1-625)

---
# References
