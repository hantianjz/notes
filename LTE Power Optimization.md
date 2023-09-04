---
publish: true
reviewed: 2023-03-03
review-frequency: ignore
link:
- '[[UBlox]]'
- '[[NRF9160]]'
- '[[AT Commands]]'
- '[[LTE]]'
- '[[SARA-R5]]'
- '[[Power Saving Mode]]'
- '[[PSM]]'
- '[[eDRX]]'
- '[[twilio]]'
- '[[Notes todo]]'
tags:
- notes
---
## Power Save Mode (PSM)
On LTE a IoT device can attach to the network while sleeping.

Host network periodically page the device, which wake up device and respond, the device then go back to sleep.

PSM allow IoT device to an extended sleep period where the network does not page the device. Allowing the IoT device to sleep until it have data to send, or when sleep period expires.

PSM introduced in 3GPP release 12.

Data intended for the sleeping device is buffered: 3GPP requirements mandate that data packets must be stored by the network. The standard recommends that the network operator sets aside storage for at least the last 100 bytes.

### +CPSMS
```
+CPSMS=[<mode>[,<Requested_Periodic-RAU>,<Requested_GPRS-READY-timer> ,<Requested_Periodic-TAU>[,<Requested_Active-Time>]]]
```
The *requested periodic TAU* value is encoded according to the GPRS Timer 3 specification (see [section 10.5.7.4a of 3GPP TS 24.008](https://www.etsi.org/deliver/etsi_ts/124000_124099/124008/13.07.00_60/ts_124008v130700p.pdf "section 10.5.7.4a of 3GPP TS 24.008")).
| timer 3 value | timer value multiple of |
| ------------- | ----------------------- |
| 000xxxxx      |   10 minutes            |
| 001xxxxx      |   1 hours               |
| 010xxxxx      |   10 hours              |
| 011xxxxx      |   2 seconds             |
| 100xxxxx      |   30 seconds            |
| 101xxxxx      |   1 minute              |
| 110xxxxx      |   320 hours             |
| 111xxxxx      |   timer deactivated     |

The *requested active time* is a single binary string byte value defined by GPRS Timer 2 specification (see [section 10.5.7.4 of 3GPP TS 24.008](https://www.etsi.org/deliver/etsi_ts/124000_124099/124008/13.07.00_60/ts_124008v130700p.pdf "section 10.5.7.4 of 3GPP TS 24.008")).
| timer 2 value | timer value multiple of |
| ------------- | ----------------------- |
| 000xxxxx      |   2 seconds             |
| 001xxxxx      |   1 minute              |
| 010xxxxx      |   1 decihour (6 minute) |
| 111xxxxx      |   timer deactivated     |

## eDRX


---
# References
- SARA-R5 Application Development AppNote **UBX-20009652**
- https://www.twilio.com/docs/iot/supersim/low-power-optimization-for-cellular-modules
- https://docs.monogoto.io/tips-and-tutorials/low-power-modes-edrx-and-psm