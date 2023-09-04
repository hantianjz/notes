---
publish: true
review-frequency: normal
link:
- '[[lorawan]]'
- '[[wireless]]'
- '[[standard]]'
tags:
- documentation
---

# LoRaWAN Network
-  ultra low power
- long range
- deep indoor penetration
- License free
- geolocation
- public & private deployment
- e2e security
- FW update OTA
- Large eco-system

# LoRa
- A wireless modulation technique. Derived from Chirp Spread Spectrum (CSS)
- Modulation is built on top of FSK, but each symbol is represented by a rise or lower of frequencies. [Ref](https://www.youtube.com/watch?v=dxYY097QNs0)
- Good for small data, with low bit rates, transmitted at a longer range
- Operate in sub-gigahertz, 915MHz, 868MHz, 433MHz.

# LoRaWan
- A Media Access Control (MAC) layer protocol built on to of LoRa.
- LoRaWAN network use an ALOHA(Additive Links On-line Hawaii Area) based protocol.
- Operate in unlicensed radio spectrum.

# Regional Parameters
- Due to the range of the protocol, each geo region have it's own broadcasting requirement

# Message Types
- Various message type
    - Join-Request/Accept
    - Unconfirmed Data Up/Down
    - Confirmed Data Up/Down
    - Rejoin-request (1.1)
 
## Data messages
![[Pasted image 20221012190712.png]]
![[Pasted image 20221021141013.png]]


---
# References
- 