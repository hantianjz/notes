# Chapter 8: Protocol Layer (USB2)
**Byte/Bit Ordering**: Little-endian order. LSB first then MSB

-   **8.3.1 Packet Identifier Field**
    
    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/84a68e23-7fcb-4c69-8812-240af12ec0cd/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/84a68e23-7fcb-4c69-8812-240af12ec0cd/Untitled.png)
    
    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f268b59e-8557-4609-a4ec-b679e6eb3aaa/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f268b59e-8557-4609-a4ec-b679e6eb3aaa/Untitled.png)
    
-   **8.3.2.1 Address Field**
    
    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c81a5e5b-6d88-4732-9784-3d73285438a4/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c81a5e5b-6d88-4732-9784-3d73285438a4/Untitled.png)
    
-   **8.3.2.2 Endpoint Field**
    
    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/92767a84-15a2-477d-ab61-1e1c906a00a5/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/92767a84-15a2-477d-ab61-1e1c906a00a5/Untitled.png)
    
-   **8.3.3 Frame Number Field**
    
    -   11 bit field incremented by host
    -   Roll over at max value of 0x7FF
    -   Send only in SOF
-   **8.3.4 Data Field**
    
    Hold 0 to 1024 bytes
    
-   **8.3.5 CRC**
    
    Covers all non-PID fields