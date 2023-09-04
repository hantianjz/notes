---
publish: true
review-frequency: normal
---
2022-02-26-Sa
Type:: #documentation 
Tags:: [[UBlox]], [[AT Commands]], [[LTE]], [[SARA-R5]]

# How does AT Commands implementations goes
## Basics
- AT commands spaces are ignored
- After final result code or URC reception, 20 ms delay before new AT Commands
- Final result code `OK` or `ERROR`
- Async commands return final result code, and final result via URC
- Intermediate Result Code (IRC) during command execution

### Operational Modes
- Command Mode
- Special AT commands lead to intermediate states, raw/binary data
- Point-to-point protocol (PPP) Data Mode, DTR line ON-to-OFF
- Online Command Mode (OLCM), moved back to PPP Data Mode
![[SARA R5 modem state diagram.png]]

## Unsolicited Result Code (URC)
- Asynchronous message indicate an event
- URCs will be deferred and delivered when AT port returns into command mode
- URC can return after AT command is send

## Serial interface configuration
**Default:** `AT+USIO=0` 
AT on UART (7-wire: RXD, TXD, CTS, RTS, DTR, RI, GND), TRACE on USB and SPI.

`AT+IPR=0`
Uart rate is set to **autobauding**.

Use `AT+CSGT` to show greeting text at module boot to auto baud rate.

If power saving mode `AT+UPSV=1` or `AT+UPSV=3` use a fixed baud rate.

## Multiplexer
Virtual channels for multiple simultaneous sessions
- Channel 0: multiplexer control
- Channels 1 to 3: AT commands / data connection.
- Channel 4: GNSS data tunneling (NMEA)

## Generic guidelines
To properly configure local connectivity, the following steps shall be considered:
1.  Set the required connectivity variant at first usage, via the `+USIO` AT command.
2.  Configure the GPIOs based on the set variant (especially in reference to the RI line), via the `+UGPIOC` AT command.
3.  Configure the power saving control mode based on the set variant, via the `+UPSV` AT command.

---
# References
- SARA-R5 Application Development AppNote **UBX-20009652**