---
publish: true
review-frequency: normal
link:
- '[[UBlox]]'
- '[[AT Commands]]'
- '[[MNO]]'
- '[[LTE]]'
- '[[SARA-R5]]'
tags:
- documentation
---
# U-Blox setting Mobile Network Operator profile
Use `AT+UMNOPROF` at command to select a network operator profile. I.E. AT&T vs Verizon.

Default profile and factory programmed on SARA-R5 is **90** (Global profile)

Activate MNO profile by reboot module `AT+CFUN=16`

Some parameter can override in MNO profile:
- `+UBANDMASK` - Band mask
- `+CGDCONT` - APN and PDP Type

APN will *usually* be accepted when in roaming.
Bands may need to enable search alternative PLMNs.

Only change MNO profile when de-register.

## AT&T (+UMNOPROF: 2)

## Verizon (+UMNOPROF: 3)

## Regulatory / Conformance (+UMNOPROF: 0/ 201)
Used for production or lab testing. [[LwM2M]] and security features are disabled.

## SIM ICCID select profile (+UMNOPROF: 1)
Use different profile on different SIM cards. MNO profile is selected based on **SIM Issuer Identifier Number** (*IIN*) or *IMSI*

When using MNO profile 1, MUST also configure automatic reset and URC enabling.

---
# References
- SARA-R5 Application Development AppNote **UBX-20009652**