Related: [[ARM-NONE-EABI toolchain| ARM GCC Toolchain]], [[How to debug Hardware Faults on ARM Cortex-M|Cortex-M Hardfault]]
ARM boot/Reset vector table ARMv7-M7

Table contains:

-   Initial stack values
-   Entry point address to each exception handler (B1-634)

SW can relocate VT using VTOR reg (B3-716)'

Handler entry address bit[0] == 1 indicate load into EPSR.T (B1-625)