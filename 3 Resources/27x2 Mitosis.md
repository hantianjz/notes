---
publish: false
reviewed: 2023-03-12
review-frequency: ignore
tags:
  - diary
link:
  - "[[nrf52]]"
  - "[[gazell]]"
  - "[[keyboard]]"
  - "[[firmware]]"
---
**2024-03-02**
- Still some pairing issue
- but first need to fix the bootloader on the dongle
    - https://devzone.nordicsemi.com/guides/short-range-guides/b/getting-started/posts/nrf52840-dongle-programming-tutorial
`./nRF5_SDK_17.1.0_ddde560/examples/dfu/open_bootloader/pca10059_usb_debug/hex/open_bootloader_usb_mbr_pca10059_debug.hex`

and it turns out was due to poor implementation of UICR erase.

**2024-02-19**
- Basic sanity feature is done.
- A lot of corner cases that still needs to be ironed out mostly around the protocol stability part now
    - Still observe frequent keys drop
    - One side the board just goes out of sync
    - When the dongle is unplugged, or power cycled, both keyboard unable to reconnect.
    - I am not using gzp for pairing application on gzll protocol
- Also my nrf dongle DFU update flow is broken, I need to fix that, or somehow use jlinking, or compile the program with a bootloader?

**2024-02-01**
Started by doing board layout, figure out the number of keys I want.

I wanted a keyboard with slightly tighter layout while also being ortho linear.
The keyboard needs to be wireless with dedicated rf that’s not Bluetooth/LE based for power and performance reasons.
The keyboard should be able to run QMK or any dedicated FW.
The keyboard should be low powered to live off a coin cell for few months.

In theory matrix scanning should be more power intensive since it does more scanning and using gpio interrupts.
I should test this!!!

**2024-01-31**
Components:
- nrf51822 seed board
- 51 ohm resistor
- LED
- mosfet![[592FBD16-DFF0-47D4-8CB7-FE893E0C8C8D_1_102_o.jpeg]]
    ![[B2A12BCC-24F7-48A2-8FC9-CCC872DA72C0_1_102_o.jpeg]]

**2024-01-28**
-  Need to figure out how to get logging

**2023-07-22**
My keyboard requirement:
- Low profile, bare pcb
- Low profile key switches
    - Choc v2 different footpoint
    - MX key compatible
- Normal keycaps for the consistent feeling
- Wireless, using 2.4GHz
- lower power using coincell battery for a few month
    - Coin cell cage
- auto power down to lowest power drain when not used

**2023-07-20**
- Okay mostly working now, which is great
- Going to start enabling and play around with other features, like tap, and layers, and key rolling
- Also need to work on timing improvement of key stroke
- pairing improvement to make connection more robust
- Start writing summary of doing FW development on nrf52 dongle

| Switch # | Pin # | QMK # |
| -------- | ----- | ----- |
| 1        | 1     | 9    |
| 2        | 2     | 10    |
| 3        | 3     | 15    |
| 4        | 4     | 14    |
| 5        | 5     | 21    |
| 6        | 6     | 16    |
| 7        | 7     | 22    |
| 8        | 8     | 11    |
| 9        | 9     | 17    |
| 10       | 10    | 13    |
| 11       | 11    | 20    |
| 12       | 12    | 19    |
| 13       | 13    | 0     |
| 14       | 14    | 6     |
| 15       | 15    | 12    |
| 16       | 16    | 18    |
| 17       | 17    | 23    |
| 18       | 18    | 24    |
| 19       | 19    | 25    |
| 20       | 20    | 26    |
| 21       | 21    | 4     |
| 22       | 22    | 3     |
| 23       | 23    | 2     |
| 24       | 24    | 1     |
| 25       | 25    | 7     |
| 26       | 28    | 8     |
| 27       | 29    | 5     |

![[Pasted image 20230720210914.png]]
**2023-07-19**
- okay finally working, shit seems to be workingish
- just need to get the proper key mapping done
```
/*
 * keyboard report is 8-byte array retains state of 8 modifiers and 6 keys.
 *
 * byte |0       |1       |2       |3       |4       |5       |6       |7
 * -----+--------+--------+--------+--------+--------+--------+--------+--------
 * desc |mods    |reserved|keys[0] |keys[1] |keys[2] |keys[3] |keys[4] |keys[5]
 *
 * It is exended to 16 bytes to retain 120keys+8mods when NKRO mode.
 *
 * byte |0       |1       |2       |3       |4       |5       |6       |7        ... |15
 * -----+--------+--------+--------+--------+--------+--------+--------+--------     +--------
 * desc |mods    |bits[0] |bits[1] |bits[2] |bits[3] |bits[4] |bits[5] |bits[6]  ... |bit[14]
 *
 * mods retains state of 8 modifiers.
 *
 *  bit |0       |1       |2       |3       |4       |5       |6       |7
 * -----+--------+--------+--------+--------+--------+--------+--------+--------
 * desc |Lcontrol|Lshift  |Lalt    |Lgui    |Rcontrol|Rshift  |Ralt    |Rgui
 *
 */

```

**2023-07-18**
- we are now able to send hid report now, or so I think? At least it looks like it is working
- The keyboard hid interface is coming up correctly so that"s nice?

**2023-07-16**
- bringing up a new platform for QMK
    - Timer, which is really just a clock, but it is not very clear the frequency it is expecting
    - The problem is how to test each individual part during development
- Seems like everything is hooked up fine now,
- I just need to figure out the hid report

**2023-07-15**
- There is no systick on nrf51
- RTC interrupt is not working as I expected, it is a little weird
- Also the difference between WFI and WFE is unclear to me on NRF
    - In WFI sleep the CPU will wake up as a result of an interrupt request if the associated interrupt is enabled in the NVIC. In WFE sleep the CPU will wake up as a result of an interrupt request regardless of the associated interrupt being enabled in the NVIC or not.
- Okay Keyboard FW working
- I forgot that when debugger is attached WFE always returns, hence why there is no interrupt. I should still use WFI since I depend on interrupt
- Now I need to make sure that the nrf52 dongle can add a new HID interface
- I was dumb, had used the same interface twice

```
Bus 003 Device 016: ID 1915:520f Nordic Semiconductor ASA 27x2 Mitosis
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass            0 
  bDeviceSubClass         0 
  bDeviceProtocol         0 
  bMaxPacketSize0        64
  idVendor           0x1915 Nordic Semiconductor ASA
  idProduct          0x520f 
  bcdDevice            1.00
  iManufacturer           1 HJZ
  iProduct                2 27x2 Mitosis
  iSerial                 3 E44F49FA699B
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x0064
    bNumInterfaces          2
    bConfigurationValue     1
    iConfiguration          4 Default configuration
    bmAttributes         0xe0
      Self Powered
      Remote Wakeup
    MaxPower              100mA
    Interface Association:
      bLength                 8
      bDescriptorType        11
      bFirstInterface         0
      bInterfaceCount         2
      bFunctionClass          2 Communications
      bFunctionSubClass       2 Abstract (modem)
      bFunctionProtocol       1 AT-commands (v.25ter)
      iFunction               0 
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         2 Communications
      bInterfaceSubClass      2 Abstract (modem)
      bInterfaceProtocol      1 AT-commands (v.25ter)
      iInterface              0 
      CDC Header:
        bcdCDC               1.10
      CDC Call Management:
        bmCapabilities       0x03
          call management
          use DataInterface
        bDataInterface          1
      CDC ACM:
        bmCapabilities       0x02
          line coding and serial state
      CDC Union:
        bMasterInterface        0
        bSlaveInterface         1 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x82  EP 2 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval              16
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       0
      bNumEndpoints           2
      bInterfaceClass        10 CDC Data
      bInterfaceSubClass      0 
      bInterfaceProtocol      0 
      iInterface              0 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x01  EP 1 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         3 Human Interface Device
      bInterfaceSubClass      1 Boot Interface Subclass
      bInterfaceProtocol      1 Keyboard
      iInterface              0 
        HID Device Descriptor:
          bLength                 9
          bDescriptorType        33
          bcdHID               1.11
          bCountryCode            0 Not supported
          bNumDescriptors         1
          bDescriptorType        34 Report
          wDescriptorLength      63
         Report Descriptors: 
           ** UNAVAILABLE **
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               1
Device Status:     0x0001
  Self Powered
```

lsusb profile for keyboard receiver:
```

Bus 003 Device 015: ID 05ac:0256 Apple, Inc. 2.4G Wireless Receiver
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               1.10
  bDeviceClass            0 
  bDeviceSubClass         0 
  bDeviceProtocol         0 
  bMaxPacketSize0        64
  idVendor           0x05ac Apple, Inc.
  idProduct          0x0256 
  bcdDevice            3.10
  iManufacturer           1 CX
  iProduct                2 2.4G Wireless Receiver
  iSerial                 0 
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x003b
    bNumInterfaces          2
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0xa0
      (Bus Powered)
      Remote Wakeup
    MaxPower              100mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         3 Human Interface Device
      bInterfaceSubClass      1 Boot Interface Subclass
      bInterfaceProtocol      1 Keyboard
      iInterface              0 
        HID Device Descriptor:
          bLength                 9
          bDescriptorType        33
          bcdHID               1.10
          bCountryCode            0 Not supported
          bNumDescriptors         1
          bDescriptorType        34 Report
          wDescriptorLength      73
         Report Descriptors: 
           ** UNAVAILABLE **
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0008  1x 8 bytes
        bInterval               2
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         3 Human Interface Device
      bInterfaceSubClass      1 Boot Interface Subclass
      bInterfaceProtocol      2 Mouse
      iInterface              0 
        HID Device Descriptor:
          bLength                 9
          bDescriptorType        33
          bcdHID               1.10
          bCountryCode            0 Not supported
          bNumDescriptors         1
          bDescriptorType        34 Report
          wDescriptorLength     254
         Report Descriptors: 
           ** UNAVAILABLE **
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x82  EP 2 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0008  1x 8 bytes
        bInterval               2
Device Status:     0x0000
  (Bus Powered)
```

**2023-07-13**
- Okay the original implementation was way too interrupt driven, this all could be done with systicks or timer. Either would probably the same complexity
- It would be really nice to get GPIOTE to trigger on all port events, and I just remembered that classic GPIOTE port event bug...sigh..this is so stupid
- So We need to constantly be refreshing and reading the GPIO states while any key is pressed down, this might not be that bad?

**2023-07-12**
- Okay was able to send some data across, a uint32 of bitmap of the keys that are clicked. this seems okayish? as a starting point
- But I am running into a hardfault now, need to handle this. I suspect it is calling gazll send too often
    - Okay nevermind it went from barely hardfault to consistently hardfaulting now, need to fix this tomorrow

**2023-07-09**
- Today’s goal will be to get a polished loop back app setup for fw and maybe do a little latency test 
- Loopback some what working
    - The main lesson where is that tx can be successful without payload in ack, hence you can just move on
- *Next Step*: Keyboard FW, send sending full keys state on change

**2023-07-08**
- Today getting objcopy template working, which would require an action.py

**2023-06-07**
Okay need to figure out how to get Gazell protocol to work

- Got proof of concept working, so gazel will work with basic packet_ack example firmware
- Next step setup a decent loopback firmware for testing with some buttons and LEDs