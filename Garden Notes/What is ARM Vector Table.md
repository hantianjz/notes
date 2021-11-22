ARM boot/Reset vector table ARMv7-M7

Table contains:
-   Initial stack values
-   Entry point address to each exception handler (B1-634)

SWcan relocate VT using VTOR reg (B3-716)'

Handler entry address bit[0] == 1 indicate load into EPSR.T (B1-625)