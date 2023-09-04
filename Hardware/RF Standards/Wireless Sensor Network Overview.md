---
publish: true
review-frequency: normal
link:
- '[[paper]]'
- '[[wireless]]'
- '[[sensor]]'
- '[[survey]]'
- '[[RF]]'
tags:
- documentation
---
2022-09-20-Tu

# Wireless Sensor Network Overview

Current trend use IP to achieve native connectivity between WSNs and internet.

Iot device need *interoperability* for seamless interaction; *Scalability* for the scale; *identification* with discovery mechanism; *confidentiality* and *authenticity*.

Volume of data to handle; vs power consumption.

# Non-IP solutions
## ZigBee
- low data rate
- short range
- **Stack layers**:
    - PHY/MAC (IEEE 802.15.4)
    - NWK (Network)
    - APL (Application)
- **Frequencies**
    - 868 MHz; Europe; 20 kb/s
    - 915 MHz; North America; 40 kb/s
    - 2.4 GHz; Worldwide; 250 kb/s
- **Topologies**
    - Tree
    - Mesh
- New ZigBee specification RF4CE
    - Support start topology

## Z-Wave
- **Stack layers**:
    - PHY/MAC
    - Transfer
    - Routing        
    - Application
- **Frequencies**
    - 900 MHz; (868 MHz EU; 908 MHz US); 9.6 kb/s; 40  kb/s
    - 2.4 GHz; Worldwide; 200 kb/s
- **Topologies**
    - Controllers vs Slave
    - Controllers poll or send commands to slaves
   
## INSTEON
- Mesh topology of RF and power line links
- Device and be RF-only or power-line only, or both
- **Frequencies**
    - 904 MHz; 38.4 kb/s
- Time slot synchronization for mesh network

## WAVENIS
- **Stack layers**
    - PHY, link, and network layer
    - Upper layer accessed via API
- **Frequencies**
    - 433 MHz, Asia, 4.8 kb/s
    - 868 MHz, EU, 4.8 kb/s
    - 915 MHz, US, 4.8 kb/s
    - 2.4 GHz, 100 kb/s
    - Typically 19.2 kb/s

# IP Based
- 6LoWPAN = IPv6 over Low-Power Wireless Personal Area Network 
- IETF Routing Over Low Power and Lossy Networks (ROLL) working group

# Middleware 
## Constrained Application Protocol (CoAP)
- Subset of HTTP feature
- Sub layered into request/response and transaction
- On top of UDP


# Reference
---
- [Evolution of wireless sensor networks towards the Internet of Things: A survey](https://ieeexplore.ieee.org/document/6064380) 2011
- [Internet of Things in Industries: A Survey](https://ieeexplore.ieee.org/document/6714496) (2014)