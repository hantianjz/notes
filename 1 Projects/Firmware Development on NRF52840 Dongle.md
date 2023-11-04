---
publish: false
reviewed: 2023-07-20
review-frequency: ignore
link:
- '[[blogging]]'
- '[[firmware]]'
- '[[nrf52]]'
- '[[arm]]'
tags:
- documentation
---

# Firmware Development work flow on NRF52840 Dongle

## Overview
- How to flash FW via DFU
- How I start compile firmware from NRF SDK
- Example sdk_config.h changes
- Getting logging over CDC setup 
- Other more advance things we can do with it

The dongle out of the box behaviour and some corresponding tools provided by nordic.
The desktop app allows you to do a lot of stuff already. From programming to ble connect.
The default firmware is somehow able to be put into dfu mode without any buttons so that must be possible for me to do also.
- How do I program the nordic dongle via cmdline.
- How to navigate the NRF SDK and compile example projects
- Setting up your own blinkly FW
- Getting logging over USB CDC

The [NRF5280 dongle](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-Dongle) is a great introductory hardware There is also a very similar product from [Make Diary](https://wiki.makerdiary.com/nrf52840-mdk-usb-dongle/programming/) with slightly different layout. It is also generally a decent utility tool for BLE related work. These functionality can all be done out of box with the nrf desktop tool without doing any programming.

There are plenty of blog post on this already that covers introductory programming with the nordic part. https://jimmywongiot.com/2019/10/25/how-to-use-the-nrf52840-dongle-pca10059-as-development-board/

![[NRF52840_dongle_pcb_black_white.png]]

---
# References