---
tags:
  - diary
  - work
link:
  - "[[fi]]"
  - "[[barking labs]]"
---
```tasks
short mode
(path includes Work Journals) OR (filename includes Fi 2023)
not done
sort by created
```


[FC32H000329](https://internaltools.corp.tryfi.com/devices/FC32H000329) Old bigboard

**2023-11-03**

- [ ] Fix nrf9160 uart console and figure out how to push a new image.

Y: trying dfu fwup prototype, validating dfu full system update with bootloader
T: discuss with IAC on trial production run for new nrf9160 fw

```
[00:00:00.263,122] <err> custom_at_host: UART check failed: 12. Dropping buffer and retrying.
[00:00:00.263,122] <err> custom_at_host: UART fifo read error: -134.
[00:00:00.273,254] <inf> custom_at_host: Uart booted 12
[00:00:00.273,254] <err> custom_at_host: UART could not be initialized: 12
```

**2023-11-02**
Y: pushed 4.13.5 to 500 external users, learning and how DFU work in the bootloader
T: try to prototype dfu fwup in application with test harness

- validate doing full system DFU using current method
- [x] Start conversation with Dylan on mini build with new modem FW ✅ 2023-11-02

**2023-11-01**
Y: wrapped up nrf9160 modem fw work, and some power consumption testing for sanity check
T: start working on enabling application fwup in bootloader 

**2023-10-31**
Y: testing new nrf9160 modem fw, and fixing a hard fault. Testing nrf9160 fw up
T: debugging nrf9160 fwup not getting applied 

**2023-10-30**
Y: Push out 4.13.4 that should address recent bugs in 4.13.x release. Continue work on modem FW version branching
T: Push out 4.13.4 to a small population of external users

**2023-10-27**
What is code vectorization vs scalar 

To follow up.
https://app.asana.com/0/0/1205817980267494/f

Y: fixing bug in 4.13.3, and a few cxd5605term improvements 
T: get a new 4.13.4 fw version released, and continue modem fw work.

**2023-10-26**
Y: getting nrf9160 neighbor cells PRed
T: figure out how to have nrf52 support different versions of modem FW.

**2023-10-25**
Y: cleaned up nrf9160 neighbor cell PR, and pushed new 4.13.3 release to internal testers 
T: more testing for new nrf9160 neighbor changes

**2023-10-24**
Y: Helping testing Wifi Scan Location backend code with John, continue work on dynamic protobuf encode/decode of nrf9160 neighbor cell data  
T: Clean up nrf9160 neighbor cell data work and PR it, and try to fix the submission response failure in new FW.

- [ ] Ask bob if we can do a special build with new modem FW and latest nrf52 FW as a internal test

Y: dynamic protobuf decode/encode of nrf9160 neighbor cell data, email with nordic on nrf9160 upgrade
T: discussion on if we should  OTA the nrf9160 fw for collars in the field 

**2023-10-23**
- [x] Extend the submission report timeout for cell and wifi, and ble. And add stat logging for submission report timeout

Y: dynamic protobuf decode/encode of nrf9160 neighbor cell data, email with nordic on nrf9160 upgrade
T: discussion on if we should  OTA the nrf9160 fw for collars in the field 

**2023-10-20**
Y: root caused the modem firmware boot up issue, and cleanup modem link proto msg api
T: start figuring out how to get modem firmware upgrade 

- [x] Email nordic support on nrf9160 upgrade path ✅ 2023-10-21

**2023-10-19**
Y: Narrowed down modem FW boot issue to a single pin causing the boot lock 
T: digging into modem fw bootloader to fix the boot lock issue

**2023-10-18**
Y: Brought up modem FW running with latest nrf connect sdk, seeing some spi bus issue
T: Fix the modem spi bus conflict with the accel and IMU for some reason.

- Only the MOSI line, will keep the MCUbootloader in reset state
- NOT SCLK
- Around 316ms after nrf9160 bootup, the bootloader does some kind of check on P0.29 and will get stuck on that
- Need to figure out how to debug the MCUBoot
    - Get nrf9160dk running, and some how get verbose logging enable on it, to see what is going on.

**2023-10-16**
Y: bringing up modem applications firmware onto nRF connect ask 2.4.1
T: continue with updating modem application firmware on new sdk 

**2023-10-13**
Y: continue the nrf9160 sdk upgrade, cleaning up existing tool breakage and fixing build error
T: pulling in nrf connect sdk 2.4.1 with nrf9160 application fw

Changelog - 4.13.0
- BLE Break algorithm
- Upload Wifi scan results
- Various bug fix and fi.transport changes

**2023-10-12**
Y: start bringing back up nrf9160 firmware with newest nrf sdk.  
T: continue nrf9160 sdk update for the corresponding modem fw update.

**2023-10-11**
Y: Prototyped reading LTE neighbor cell tower in in prod FW, start looking into newer nrf9160 Modem SiP FW
T: Try to bring up modem FW with new nrf9160 SiP FW, and update SDK.

**2023-10-10**
Y: Experimenting with LTE neighbor cell tower info gathering
T: Prototype to upload LTE neighbor cell tower info in FW

**2023-10-09**
Y: Update the wifi result upload in accordance with nrf's api request
T: Start on neighbor cell tower info 

```
modem AT%NBRGRSRP
modem AT%NCELLMEAS=3,2
modem AT%NCELLMEASSTOP
```

**2023-10-05**
Y: Continuing GNSS testing at test lab in NC, we tested GNSS performance of all recent generations of collar modules, and comparing device to device performance variations.  
T: A side quest to do some performance test on the new LTE antenna while we are at the test lab, and doing some retesting for more data

- [x] update wifi result upload with bssid in bytes and channel/frequency data ✅ 2023-10-09
- [x] look into new modem FW ✅ 2023-10-24
- https://api.nrfcloud.com/#tag/Wi-Fi-Location/operation/GetLocationFromWifiNetworks
- https://api.nrfcloud.com/#tag/Cell-Location

**2023-10-04**
Y: traveling to Wake Forest, NC to help out with gnss testing at test lab. We are testing multiple generations of the collar and various orientation.
T: continue with gnss lab testing, today starting unit to unit variations to understand how much gnss performance varies between units within a generation.

- [ ] email Sony why we see wrong sat in data
- [ ] Check if S3.0 have newer CXD FW than S2.5

**2023-10-03**
We are leaving the gnss test lab now and going back to do some data analysis over some “refreshments”. Overall day 1 we did testing on all S2.5/S3/S3.1/S3.2(new antenna design) in 6 orientation around a phantom limb. Repeatedly test on a single S3.1 10 times.


**2023-10-01**
- [ ] Try out https://github.com/OutSystems/netemu/tree/master on rapi to create low latency slow network connection
source: https://www.outsystems.com/blog/posts/simulate-slow-network/

Y: Finished uploading wifi scan results in firmware, and some analysis of some modules not getting LLE update
T: Prepare for the GNSS testing tomorrow, debug why the new efr32 ble dongle would cause missing NMEA sentences in gnss testing

Version 4.12.4 is out to fix some LLE injection issues
