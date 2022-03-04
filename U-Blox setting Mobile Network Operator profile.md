2022-02-26-Sa
Type: #documentation 
Tags: [[UBlox]], [[AT Commands]], [[MNO]], [[LTE]], [[SARA-R5]]

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


---
# References
- SARA-R5 Application Development AppNote **UBX-20009652**