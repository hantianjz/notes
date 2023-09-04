---
publish: true
review-frequency: normal
link:
- '[[exception]]'
- '[[hardfault]]'
- '[[ARMv6M]]'
- '[[arm]]'
tags:
- notes
---
2022-02-11
Source: 

# Cortex M0 ARMv6m Exception entry behaviour

```c
// PushStack()

// ===========

PushStack()  
    if CONTROL.SPSEL == '1' && CurrentMode == Mode_Thread then
        frameptralign = SP_process<2>;  
        SP_process = (SP_process - 0x20) AND NOT(ZeroExtend('100',32));
        frameptr = SP_process;
    else  
        frameptralign = SP_main<2>;  
        SP_main = (SP_main - 0x20) AND NOT(ZeroExtend('100',32));
        frameptr = SP_main;

    /* only the stack locations, not the store order, are architected */
    
    MemA[frameptr,4] = R[0];
    MemA[frameptr+0x4,4] = R[1];
    MemA[frameptr+0x8,4] = R[2];
    MemA[frameptr+0xC,4] = R[3];
    MemA[frameptr+0x10,4] = R[12];
    MemA[frameptr+0x14,4] = LR;
    MemA[frameptr+0x18,4] = ReturnAddress();
    MemA[frameptr+0x1C,4] = (xPSR<31:10>:frameptralign:xPSR<8:0>);
    if CurrentMode==Mode_Handler then
        LR = 0xFFFFFFF1; 
    else
        if CONTROL.SPSEL == '0' then 
            LR = 0xFFFFFFF9;
        else  
            LR = 0xFFFFFFFD;
    return;
```

------
# Reference
DDI0419C_arm_architecture_v6m_reference_manual.pdf: **B1.5.6 Exception entry behaviour**