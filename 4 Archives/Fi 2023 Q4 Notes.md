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

**2023-12-24**
- Module was on base and offline, due to a blackholed based, for duration of night. The module accumulated steps record by was full and just discarded new steps. 
- Next morning I put the collar back on Dallas around 9:17 start walking. the module is connected to the app, and send report. But the huge steps record could not been uploaded through mobile app, somehow until 9:52. at which point the steps between then have been dropped.
- 

**2023-12-22**
Y: Prototyping backend db changes needed for module bootloader update logic.
T: verify update to the fi_firmware_update_channel db table to enforce new bootloader firmware update requirements


```
ALTER TABLE fi_firmware_update_channel ADD COLUMN "blVersionId" VARCHAR, ADD COLUMN "blFirmwareType" VARCHAR, ADD COLUMN "appFirmwareType" VARCHAR;

ALTER TABLE fi_firmware_version ADD COLUMN "fwType" VARCHAR;

UPDATE fi_firmware_update_channel SET "appFirmwareType" = 'application';
UPDATE fi_firmware_update_channel SET "blFirmwareType" = 'bootloader';
UPDATE fi_firmware_version SET "fwType" = 'application';

CREATE UNIQUE INDEX CONCURRENTLY fi_firmware_unique_id_platform_type_idx ON fi_firmware_version(id, "compatiblePlatformId", "fwType");

ALTER TABLE fi_firmware_update_channel DROP CONSTRAINT update_channel_compatible_platform_constraint;

ALTER TABLE fi_firmware_update_channel ADD CONSTRAINT update_channel_compatible_platform_app_firmware_constraint FOREIGN KEY ("platformId", "firmwareVersionId", "appFirmwareType") REFERENCES fi_firmware_version("compatiblePlatformId", id, "fwType");

ALTER TABLE fi_firmware_update_channel ADD CONSTRAINT update_channel_compatible_platform_bl_firmware_constraint FOREIGN KEY ("platformId", "blVersionId", "blFirmwareType") REFERENCES fi_firmware_version("compatiblePlatformId", id, "fwType");
```

**2023-12-21**
Y: Catching up to BLE v2-3 discussions, understanding current backend firmware update scheme
T: sketch out new proposal for backend firmware update scheme to include bootloader update

##### Current schema

**fi_device**
- updateChannel - *public.fi_firmware_update_channel(name, platformId)* - `stable`
- platformId - *public.fi_platform(id), public.fi_firmware_update_channel(name, platformId)* - `fc3_f3`

**fi_firmware_update_channel**
- name - *primary* - `stable`
- platformId - *primary* - *public.fi_firmware_version(compatiblePlatformId, id), public.fi_platform(id)* - `fc3_f3`
- firmwareVersionId - *public.fi_firmware_version(id), public.fi_firmware_version(compatiblePlatformId, id)* - `4.13.5-7e56dd6e9-fc3_f3-prod`

**fi_platform**
- id - *primary*
- stableId/betaId/devId - *deprecated*

**fi_firmware_version**
- id - *primary* - `4.5.6-847580d04-fc3_f3-prod`
- compatiblePlatformId - *public.fi_platform(id)* - `fb3_f1`

##### Proposal schema

**fi_device**
- updateChannel - *public.fi_firmware_update_channel(name, platformId)* - `stable`
- platformId - *public.fi_platform(id), public.fi_firmware_update_channel(name, platformId)* - `fc3_f3`

**fi_firmware_update_channel**
- name - *primary* - `stable`
- platformId - *primary* - *public.fi_firmware_version(compatiblePlatformId, id), public.fi_platform(id)* - `fc3_f3`
- firmwareVersionId - *public.fi_firmware_version(id), public.fi_firmware_version(compatiblePlatformId, id)* - `4.13.5-7e56dd6e9-fc3_f3-prod`
- blVersionId - *public.fi_firmware_bl_version(id), public.fi_firmware_bl_version(compatiblePlatformId, id)*

**fi_firmware_version**
- id - *primary* - `4.5.6-847580d04-fc3_f3-prod`
- compatiblePlatformId - *public.fi_platform(id)* - `fb3_f1`

**fi_firmware_bl_version**
- id - *primary* - `4.5.6-847580d04-fc3_f3-prod`
- compatiblePlatformId - *public.fi_platform(id)* - `fb3_f1`

**2023-12-20**
Y: OOO
T: Catching up on all the new development on BLE-v2

- [x] Start working on data model for bootloader v2 push design ✅ 2023-12-25

**2023-12-15**

- [x] Look into lte testing data ✅ 2023-12-21


**2023-12-15**
Y: Finishing up ble end point queue, and testing kennel cam sensor data collection performance
T: Investigate into data for new LTE modem modules during internal tests

- [x] Look into lte testing data ✅ 2023-12-21
- [ ] enable gal for 50% of user?


**2023-12-14**
Y: implementing ble end point queues
T: working on integrating the ble end point queues in FW

entity/platform.ts
versions.ts

**2023-12-13**
Y: added queue to ble endpoint
T: still seeing data getting dropped over ble endpoint,  needs to to be fixed 

**2023-12-12**
Y: Work to remove blocking BLE operations in FW to reduce data dropping during accel data collection over BLE
T: Continue improve the stability of module FW for accel data collection

**2023-12-11**
Y: Figured out how to access dfu settings configuration in nRF52 application fw
T: work out how the bootloader init command used to perform dfu 

**2023-12-08**
Y: Fighting with nrf sdk to properly configure dfu settings for update from application
T: Continue with dfu settings configure manually to attempt update from application

**2023-12-07**
Y: Trying to get dfu update from application write to work, and update TUI on cxd5605term
T: Updating the TUI cxd5605term for better graphics and stability

**2023-12-06**
Y: More testing on bootloader hanging issue, trying to understand what component is causing the hang and try to reproduce it similar to in the field
T: Continue investigating bootloader hanging issue, and try to get dfu from application to work.

- 3J9627 - FC32M554687
- 3K0687 - FC33H157221
- 

**2023-12-05**
Y: out sick 
T: test out fix from Charles for bootloader hanging issue, get dfu from application to work

**2023-12-01**
Y: enable Galileo constellation for gnss positioning 
T: additional experiment with dfu update via application instead of existing dfu flow

**2023-11-30**
Y: write up bootloader OTA strategy, and experimenting with nRF dfu update
T: update bootloader OTA strategy doc with nRF dfu experiment results, test enabling GAL for gnss via backend 

**2023-11-28**
9:28 crash Dallas - this was a wdt:0 reboot

Y: working on bootloader OTA strategy, and releasing base fw to more external users
T: monitor base fw rollout, and continue work on BL OTA strategy 

- [x] Feature flag for enabling GAL ✅ 2023-11-30
- [x] Figure out why dfu package is smaller ✅ 2023-11-30

**2023-11-22**
Y: start investigating new base fw crashes
T: continue on base fw bug fix

**2023-11-21**
Y: found a potential root cause of the module unresponsive issue.
T: analyze the base rollout status, and S3 module 4.13.x rollout and address some base crashes tickets

**2023-11-20**
Y: continue understanding the unresponsive modules problem, started a experiment doc to track theories
T: continue to work with Adam to understand the unresponsive behavior 

**2023-11-17**
Y: reproducing the bootloop-death or unresponsive issue locally on bigboard
T: more digging into the unresponsive behavior problem 

- The power rail ripple is a lot longer sometimes, mostly on older FW
- [x] Try long delay in bootloader startup ✅ 2023-12-06
- [x] Try repro on Otii ✅ 2023-11-17
- [x] Answer why does the module recover after base is removed, who was stuck ✅ 2024-01-05

~~On latest FW, I2C is starting 800ms after vsys, but on older FW it's 6ms~~

**2023-11-16**
- [x] Find RA9530 spec doc, how the hell does the pins work? ✅ 2023-11-17

Y: more digging into bootloop death unresponsive module issue in the field. Was able to reproduce something that’s related to the infield behavior 
T: continue the investigation and trying to get a consistent reproduction of the issue

Going back to old base FW 3.1.9

- bitter-fin on new setup 11:15 EST, 11/16 - 16:15 UTC
- complex-dew also on rev27

- Both battery resistence profile is empty
- The base when sending pp data have a sound
- looping the base reset on module
- Repro more often on 4.12.2 version now, something to do with resistance profile being erased.
- It's the LED that's drawing the power can causing ripples in the power rails.
- When the system reboot and the WP Charging is on, it will cause VSYS to ripple

**2023-11-15**
Y: deploy kennel cam rpi fix for ble, verified that the new data upload don’t have gaps anymore. 
T: getting back to trying to repro nrf52 bootloop death bug

- new Session 13:15 on billow-rain, Ending: 15:42 11/15
- new session 11/15 - 13:39 on strange-water

a random RA9530 edge, possibly when base reset

```
00:01:04.888 I  module_hsm_send_event: LTE_MODEM_SLEEP
00:01:04.889 W  hsm_instance_transition: state='ble:establishing', Unexpected event 'LTE_MODEM_SLEEP'
00:01:04.889 I  Added remote log: 7
00:01:04.897 I  clock: set time of day
00:01:04.899 I  clock: set time of day tm
00:01:04.899 I  Syncing UTC clock
00:01:04.903 I  Set central unlimited to: 1
00:01:06.070 I  RA9530 got interrupt: 0x04400060
01:01:06.072 I  RA9530 edge. Battery is full, sending EPT charge complete
00:01:06.072 I  Sending EPT Charge Complete
00:01:06.073 I  RA9530 edge.
00:01:06.074 I  Updating power cached values. 64071 milliseconds since last update.
00:01:06.084 I  Battery: SoC=100, remaining_cap=229, full_charge_cap=229
00:01:06.084 I  Battery: state 2, bq25180_stat0:0x01, is_chg:0 has_pwr:1
00:01:06.187 W  ble_evt_handler: 83
00:01:06.188 I  Added remote log: 12
00:01:06.203 I  RA9530 edge.
00:01:06.204 I  Battery charging state change: 2 --> 3
00:01:06.204 I  Battery: state 3, bq25180_stat0:0x00, is_chg:0 has_pwr:0
00:01:06.277 W  ble_evt_handler: 83
01:01:06.278 I  Added remote log: 12
```

Seems to only repro on 4.11.3 right now!!!
base reset don't always work, maybe when the module is charged?

Between when the module is reset to when Green LED turned on by bootlaoder, there is a noticable delay

Is it possible something to do with it is partially charged?

Another problematic module before crashing. FC33D705249
Thats very high ra9530 tx count 
![[Pasted image 20231115200826.png]]
So did Hudson which died https://internaltools.corp.tryfi.com/devices/FC33H157175/reports

It seems Kobe is also getting resets due to itpor events

- RA9530 is completely wedged, and not cleared from power reset
- Reverting the poll on charging seems to fix it somehow
- RA9530 powered from the wireless coil, hence lack of rf power the chip is off

**2023-11-14**
Y: trying to figure out how to deploy the ble parameter changes to the kennel cam rpi, analyze 4.13.5 FW release 
T: push out 4.13.5 to more external users, deploy the kennel cam rpi changes

- [x] Verify new base did not break onboarding ✅ 2023-11-15

Updated:
- 12573820 ca78d13 billowing-rain    (MY)
- 12464686 2b9b041 bitter-fin
- 12573812 abc01c5 strange-water     (BEN)
- 10765172 78b49c0 winter-tea       
- 12464745 d2a39b6 perfect-fog      
- 12464749 a540632 cool-sound       
- 12464767 0fb874c jolly-cactus     
- 12464772 1b5f1f1 fierce-sunset    
- 12464782 1722bd9 brave-breakfast  
- 12478656 654c63e wispy-darkness   
- 12478660 d6672f9 grumpy-hurricane 
- 12478649 73df27f complex-dew      
- 12478654 8b32c34 cold-time        

Awaiting:
- 10473968 f252882 slow-pine        
- 12464859 d6030c3 lingering-pancake
- 10795839 42a71e6 snowy-river

**2023-11-13**
Y: getting brain dump from Ben on everything he been working on.  
T: figure out update to kennel cam, follow up with 4.13.x deployment status

- [x] Get a new balena to deploy to rpi ✅ 2023-11-15
- [x] Follow up with IAC on trial build ✅ 2023-11-15

 **sensor_collect  2023-11-13 16:12:59,665 [INFO] Received notification: 2023-11-13 16:12:59.014862**

- Old slower test on 16:30

**2023-11-10**
Y: Getting setup and brain dump from Ben on his various work streams, continue investigating unresponsive units in the field
T: Look into 4.13.x performance in the field, and follow up on kennel cam update

**2023-11-09**

- [x] Take over new base FW rollout ✅ 2023-12-21
- [x] Check 4.13.5 Fleet health ✅ 2023-11-10

from bob: We might doing Nordic LTE update with special nrf9160 delta

Y: Start digging into unresponsive modules issue in the field, learning about the power architecture 
T: Try different experiments to reproduce the unresponsive behaviour

[Hudson](https://app.asana.com/0/1119265580120512/1205817980267494/f) seems to have seen this issue multiple times in the past and we have RMAed their units
[Hudson Admin Page](https://internaltools.corp.tryfi.com/devices/FC33H157175)
The last time the module was seen was with the iOS app
- Right before going away the module was in a reboot loop 3 times.
- The Phone app actually was the last to connect to the module and it went away later.
- rv4162c7Error was always exist, but somehow at start of crash loop it went away for a bit.
- Random we have `  watchdog_reload();` in da16200 operation https://github.com/barkinglabs/firmware/blob/main/src/libfi_nrf52drv/da16200_drv.c#L179
- nrf52840reset reason == 0, (remember there was something about cold reboot error from Adam)
-   `bq27421_reset(); bq25180_hardware_reset();` will produce nrf52 reset reason == 0
- `hudson` during reboot loop had this error `bq: (wd=0 itpor=0 actualkey=0x00000000 expectedkey=0xc6fac680)
- always needed reprogramming but never took
- All of these are known issues that lead up to the lockup, but we still don't know how the units are becoming locked up!!

RMA unit to get from phil
- FC33H157221 (3K0687)
- FC33D708026 (3K0619) - https://app.asana.com/0/1119265580120512/1205731841533827/f
    - likely physical damage, module is heavy used, fi logo is caved in, likely internal component is damaged
    - device does work when assigned to dog, but ble led does not blink when charging.
- FC33A361435 (3J9390)


**2023-11-08**
Y: Releasing FW for small trail run for IAC with old good bootloader
T: Verify full system DFU works as expected, start investigating into unresponsive modules in the fields 

- [x] Fix fiterm with default RTTTerm behaviour ✅ 2023-11-09
- [x] `00:05:52.130 E [fi_nrf9160_modem_check_sleep_state] LTE modem is awake when it should be sleeping!  Forcing modem offline.` ✅ 2024-01-05
- [x] Look into latest base FW crashing when reseting module ✅ 2023-11-09

**2023-11-07**
Y: Fixing nrf9160 FW for IAC, found DFU seems to be broken on latest bootloader
T: Fixing bootloader DFU bug, and cut FW release and rpi image for IAC for trail production run.

- [x] Sync with ben on kennel cam ✅ 2023-11-07

- Merge new nRF52 FW
- Trigger small batch 25 unit build
- Revert new nRF52 FW

- Support new modem FW in 4.8.x
- cut 4.13.x with BL + FW
- Franken build with old BL + new FW

1. Cherry-pick new nrf9160 version handling into 4.8.x
2. Cut nRF52 FW version **4.8.x** release for factory with nrf9160 FW version **3.0.5** and new SiP FW **1.3.5** and DA16200 FW version **68**
3. Small batch build ~25 units get back to NYC for testing and distribute to Fi employee for testing
4. Isolate newly build devices to latest nRF52 FW that support new nrf9160 FW version. (Avoid it getting updated to 4.12.x or older FW)

A side quest: Verify DFU from 4.8.x can update bootloader, to eventually allow adding firmware update via application.

IAC release 
- testing:
    - Test modem at host uart
    - Da16200 uart
    - New bootloader dfu still works 

**2023-11-06**
Y: fixing nrf9169 FW for IAC
T: look to push out 4.13.x fw to another 1k external user. Verifying full system DFU update with current bootloader

- DFU broken on:
    - 4.12.2
    - 4.13.6
- Working on 4.11.8

- DFU worked for released/4.11.x
    - Flashing the whole image and then update the dev_bootloader

- Failed for:
    - 0e4805eb045f0161f504b714fbf6b91f2b54bef5
    - d4b5d5ab52feb8bcdc3bd2fb0ee4760ba8491316
    - 247a677e59b24653944a75a4e7b0c94f7db01deb 
    - 22f02a8fe8221e1e23c0d35299a84a33c8653aba 07/18 
    
The problematic change:    
- **b81848129ea59549f81f758d004074f92aaab836 (SUS**)
Offending change ![[Pasted image 20231106200314.png]]
  
- Working SHA
    - 5314af8adfc705d086d151ddd1d7757816a1f746  07/12
    - 8d957bfc66ba2380a41a9da88405a621495b8eee 07/10

**2023-11-03**

- [x] Fix nrf9160 uart console and figure out how to push a new image. ✅ 2023-11-05

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

- [x] Ask bob if we can do a special build with new modem FW and latest nrf52 FW as a internal test ✅ 2023-11-07

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

- [x] email Sony why we see wrong sat in data ✅ 2023-11-07
- [x] Check if S3.0 have newer CXD FW than S2.5 ✅ 2023-11-07

**2023-10-03**
We are leaving the gnss test lab now and going back to do some data analysis over some “refreshments”. Overall day 1 we did testing on all S2.5/S3/S3.1/S3.2(new antenna design) in 6 orientation around a phantom limb. Repeatedly test on a single S3.1 10 times.


**2023-10-01**
- [ ] Try out https://github.com/OutSystems/netemu/tree/master on rapi to create low latency slow network connection
source: https://www.outsystems.com/blog/posts/simulate-slow-network/

Y: Finished uploading wifi scan results in firmware, and some analysis of some modules not getting LLE update
T: Prepare for the GNSS testing tomorrow, debug why the new efr32 ble dongle would cause missing NMEA sentences in gnss testing

Version 4.12.4 is out to fix some LLE injection issues
