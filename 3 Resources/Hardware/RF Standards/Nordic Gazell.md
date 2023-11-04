---
publish: true
reviewed: 2023-02-25
review-frequency: low
link:
- '[[nordic]]'
- '[[nrf52]]'
- '[[RF]]'
- '[[gazell]]'
- '[[Notes todo]]'
tags:
- documentation
---

# Nordic Gazell
- Wireless link between single host and up to 8 devices.
![[Gazel_star_topology.png]]
- Host is always listening
- Device mostly sleep, and initiates new communication
- Each packet from device require ACK from host
- Host send data to device via piggybacking on ACK packet
- Any device speak to several hosts, any node change between device/host modes. 

## Package transactions

![[Pasted image 20230708235143.png]]

#### Packet identification
Any packet transmitted from a Device to a Host is uniquely identified by a **two bit packet ID field** in the packet header together with the packet's **16-bit Cyclic Redundancy Check** (CRC). 

On the Host side, retransmitted packets will be discarded and not added to an RX FIFO.

##### Pipes and addressing
Each logical address on the nodes is termed a pipe. Each pipe maps to one on-air address used when transmitting or receiving packets.
The on-air addresses are composed of a 2-4 byte long "base address" in addition to a 1 byte prefix address.

Pipe 0 has its own unique base address, which is base address 0, while pipes 1-7 use the same base address, which is base address 1.

Each of the 8 pipes have a unique byte-long prefix address.


---
# References
- https://infocenter.nordicsemi.com/index.jsp?topic=%2Fsdk_nrf5_v17.0.2%2Fgzll_02_user_guide.html