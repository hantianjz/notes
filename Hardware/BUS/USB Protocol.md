---
publish: true
review-frequency: normal
---
Last Updated: 2021-12-29
Type:: #documentation 
Tags:: [[USB]], [[Phy Protocol]]

# USB Protocol

# Chapter 8: Protocol Layer (USB2)
**Byte/Bit Ordering**: Little-endian order. LSB first then MSB

-   **8.3.1 Packet Identifier Field**
    ![[fig1.png]]
    
    ![[fig2.png]]
    
-   **8.3.2.1 Address Field**
    
    ![[fig3.png]]
    
-   **8.3.2.2 Endpoint Field**
    
    ![[fig4.png]]
    
-   **8.3.3 Frame Number Field**
    -   11 bit field incremented by host
    -   Roll over at max value of 0x7FF
    -   Send only in SOF
-   **8.3.4 Data Field**
    
    Hold 0 to 1024 bytes
    
-   **8.3.5 CRC**
    
    Covers all non-PID fields