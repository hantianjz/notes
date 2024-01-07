---
publish: false
reviewed: 2023-07-05
review-frequency: ignore
tags:
  - diary
  - work
link:
  - "[[fi]]"
  - "[[barking labs]]"
---
- [Skywalker FC32H000328](https://internaltools.corp.tryfi.com/devices/FC32H000328)
- [Ripper FC32M548133](https://internaltools.corp.tryfi.com/devices/FC32M548133)

**2023-09-29**
Y: MA team lunch, troubleshooting weirdness with Adam's setup for GNSS testing, minor update to cxd5605term UI, and started working on uploading wifi scanned results
T: Start testing uploading wifi scanned results, debug why the new efr32 ble dongle would cause missing NMEA sentences in gnss testing.

**2023-09-28**
Y: implement freelist "lock" on shared buffer memory in firmware to store uploaded wifi scan results.
T: Working with Adam to investigate some weirdness in GNSS testing where collar in simulator doesn't show ZDA sentences, MA lunch, finally get started on uploading wifi scan results

- [x] Fix missing ZDA sentences on  efr32 dongles ✅ 2023-11-07

**2023-09-27**
Y: doing some memory hunting before starting upload wifi scan results.
T: add a “lock” to LLE buffer for memory sharing, save wifi scan results and store in protosand store in proto

- [x] Verify LLE functionality after [PR](https://github.com/barkinglabs/web/pull/5571) is merged ✅ 2023-10-02
    - [x] Still able to download LLE
    - [x] at 8pm est new LLE data is downloaded ✅ 2023-10-02
- [x] maybe figure out CXD5605term gstp no display issue ✅ 2023-11-07
- [x] 4.12.3 FW up/down test ✅ 2023-09-28
- [x] Add stdev to cxdterm gstp summary ✅ 2023-09-28

**2023-09-26**
Y: Fixing some collar ble error handling to instead of crashing issue ble disconnect, some cxd5605term dashboard UI support
T: Start digging into uploading scanned wifi results as part of wifi positioning effort

**2023-09-25**
Y: Pushing 50% S3 base to newest FW, and enabling LLE response throttling for 1% of user, polishing databricks noteworks for tracking base uptime
T: Maybe picking up work for uploading cell tower data or wifi scan results


**2023-09-22**
Y: Travel day
T: experiment with base if offline issue can be triggered by slow network latency 

- [x] Track down [FC32L234630](https://internaltools.corp.tryfi.com/devices/FC32L234630) LLE failing constantly for some reason ✅ 2023-10-02

**2023-09-15**
Y: Fixed LLE throttling feature in web to work properly against target user group
T: Rolling out new base FW to more external users.

**2023-09-14**
Y: getting back to getting LLE throttling turned on in web, need to fix the way feature flag is turned on
T: Getting LLE throttling fixed, and check new base FW rollout and potentially continue the rollout.

Session Window databricks

A really interesting user [Goofy](https://internaltools.corp.tryfi.com/devices/FC33F065228/reports) Getting a lot of submission report failure.

- Bryant: 

**2023-09-13**
Y: troubleshooting S2.5 bug where newer firmware is booting up with dead cxd5605.
T: continue debugging the S2.5 issue since that is blocking gnss testing

Base metrics to collect:
- Uptime: Base expected to submit module/base info at least every 1 minutes, often more frequent 
- Http success/failure rate: 
- Base reboot counter: Base reset due assert/hardfault/watchdog trigger
- Proxied module report count: the number of submission report from module that have successfully being proxied
- Base BLE disconnection counters: due to disconnect from module, due to firmware update available for module.


**2023-09-12**
Y: more base firmware testing and cxd5605term UI tweaking 
T: continue with cxdterm UI tweaking and working with Adam getting more S2.5 units ready for gnss testing

**2023-09-11**
Y: pushed new base fw to internal Fi users for testing, and continued minor cxd5605term UI tweaking 
T: push 3.1.9 base firmware to more external users, go back to rolling out LLE download throttling

- [x] ⏳ 2023-09-11 with Bryant ✅ 2023-09-13

**2023-09-08**
Y: Trying to add server response protobuf message parsing to base FW, and troubleshooting weird hardfault showing up
T: Continue with getting server response protobuf msg parsed in base 

- [x] CXDterm summary on gstp cmd ✅ 2023-09-12
- [x] Go back to look at dead s2.5 units with corrupted CXD5605 ✅ 2023-09-13

**2023-09-07**
Y: Various debugging S2.5 units experiencing cxd5605 fw corruption after flashing newer firmware, base FW not getting module FWUP available signal
T: Continue with debugging and hopefully getting a fix rolled out for base issue.

**2023-09-06**
Y: finishing up cxd5605term logging, and preparing S2.5 units
T: handing off S2.5 units to Adam, with cxd5605term compatible firmware. Come up with a base firmware update rollout plan, figure out what base metric to look at to indicate new base firmware is healthy in the field 

**2023-09-05**
Y: Getting S2.5 FW working again with latest cxd5605term, and continue with cxd5605term rework to get better logging output for testing
T: Continue with the cxd5605term work

**2023-09-01**
Y: analyze overall gnss performance change from 4.11.x and there seems to be a slightly change
T: continue with various minor improvements to cxd5605term dashboard and logging, prepare all the S2.5 modules for Adam’s testingS2.5 for Adam’s testing

**2023-08-31**
Y: clean up cxd5605term dashboard UI
T: looking into gnss performance from 4.8.x to 4.11.x release

**2023-08-30**
Y: working with Adam in person testing cxd5605term and going through the gnss testing flow
T: minor follow up fixes for cxd5605term, looking into gnss performance since 4.11.x release 

**2023-08-29**
Y: working on first rough version of cxd5605term dashboard
T: working with Adam in person to iron out the details and bugs for cxd5605term dashboard 

1. Place collar on base
2. On the app, find dog with no collar "Activate Collar"
3. wait for collar to be provisioned
4. on admin page go/devices/FULL serial number at firmware update channel select **fc3_f3-internal-test** channel
5. Open the app again, (may need to restart it)
6. on device page un-assigne collar

- Need to display the correct first fix time
- Display if fix is lost
- Logging all GSV data in csv format
- Display sat contributed to fix
- Flash all S2.5 with new FW and test CXD5605term over BLE

**2023-08-28**
Y: Prior to OOO on friday, was poking around dataricks trying to do some analysis on GNSS performance for S3 after 4.11.x FW release
T: Working on CXD5605term logging/dashboard for the HW GNSS lab testing scheduled

solved the mystrey of missing line, we don't print SNR 0

**2023-08-24**
Y: Getting LLE payload throttling change fixed, pushed new base FW 3.1.8 to 100 external users
T: Using dataricks to see if there is any performance change in GNSS for S3 after 4.11.x FW release vs prior

- [x] Base rollout ✅ 2023-09-13
- [x] CXD5605TERM UI ✅ 2023-09-01
- [x] GAL enable for all? ✅ 2023-11-07
- [x] lle throttle web PR, and rollout? ✅ 2023-09-01

**2023-08-23**
Y: working on LLE payload throttling and enabling GAL gnss constellations for live tracking on the backend 
T: testing the backend changes in a real collar, going to take the afternoon off in EST 

**2023-08-22**
Y: pushed out updated base firmware to fix offline issue
T: monitor base firmware firmware rollout and look into enabling GAL for look into enabling GAL for LDM now that 4.11.8 is rolled out 

Constance's base setup at office https://internaltools.corp.tryfi.com/users/3MM0FNTXO3iEPOogNtYLCE/diagnostics

Loren:
- How to store persistent collar specific lle attempts
- pull gps data on 4.11.8, what is the deal with data permissions
- 

**2023-08-21**
Y: debugging base FW stuck offline, making sure my base FW is actually setup correctly between developer vs release mode. Digging into SSL/TLS to understand why peer certification verification would continues to fail.
T: continue troubleshooting into the SSL/TLS fail that is causing offline.

Building between 
`CONFIG_COMPILER_OPTIMIZATION_SIZE` and `CONFIG_COMPILER_OPTIMIZATION_DEFAULT` it doesn't seems to make some difference in term of memory usage 

It does not seem like `CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_ENABLE` 

**2023-08-18**
Y: Troubleshoot base FW heap malloc setup, and why it could be causing SSL/TLS error on the base, which leads it to be offline
T: Continue debugging base FW, traveling in the afternoon

```
CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_ENABLE=n
CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_SILENT=y
```

**2023-08-17**
Y: getting base dev kit setup, and may have reproduced the base offline issue.
T: continue to debug base offline issue

```
W (93938) esp-tls: Failed to open new connection in specified timeout
E (93938) transport_base: Failed to open a new connection
E (93938) HTTP_CLIENT: Connection failed, sock < 0
E (93938) fi_api: Failed to open HTTP connection: 0x7002
```

**2023-08-16**
Y: trying to reproduce bug reported by IAC, and getting started in base development
T: getting base dev kit from Charles and try to debug the base getting stuck offline and bringing collar offline with it 

- Check assignably fails a lot
- but most of submit report works fine

```
0x420210e6: btc_gatts_cb_handler at /Users/james/Developments/barkinglabs/base-firmware/esp-idf/components/bt/host/bluedroid/btc/profile/std/gatt/btc_gatts.c:818

0x4203e1d4: btc_thread_handler at /Users/james/Developments/barkinglabs/base-firmware/esp-idf/components/bt/common/btc/core/btc_task.c:208

TP      : 0x3fc89a60  T0      : 0x4005890e  T1      : 0x0000000f  T2      : 0x00000000
0x4005890e: _data_end_btdm_rom in ROM

S0/FP   : 0x50000dc4  S1      : 0x3fcb8c54  A0      : 0x50000dc4  A1      : 0x00000208
A2      : 0x50000dc4  A3      : 0x3fcc3440  A4      : 0x00000004  A5      : 0x00000000
A6      : 0x00000001  A7      : 0x00000064  S2      : 0x00000000  S3      : 0x00000000
S4      : 0x00000000  S5      : 0x00000000  S6      : 0x00000000  S7      : 0x00000000
S8      : 0x00000000  S9      : 0x00000000  S10     : 0x00000000  S11     : 0x00000000
T3      : 0x00000000  T4      : 0x00000002  T5      : 0x3fcc336c  T6      : 0x3c11a000
MSTATUS : 0x00001881  MTVEC   : 0x40380001  MCAUSE  : 0x00000005  MTVAL   : 0x00000000
0x40380001: _vector_table at ??:?

MHARTID : 0x00000000


Backtrace:


/Applications/Xcode-14.2.0.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/install_name_tool: warning: changes being made to the file will invalidate the code signature in: /Users/james/.espressif/tools/riscv32-esp-elf-gdb/12.1_20221002/riscv32-esp-elf-gdb/bin/riscv32-esp-elf-gdb-3.11.ZBqSs5r
0x420210e6 in btc_gatts_cb_handler (msg=0x50000dc4) at /Users/james/Developments/barkinglabs/base-firmware/esp-idf/components/bt/host/bluedroid/btc/profile/std/gatt/btc_gatts.c:818
818             param.mtu.mtu = p_data->req_data.p_data->mtu;
#0  0x420210e6 in btc_gatts_cb_handler (msg=0x50000dc4) at /Users/james/Developments/barkinglabs/base-firmware/esp-idf/components/bt/host/bluedroid/btc/profile/std/gatt/btc_gatts.c:818
#1  0x4203e1d4 in btc_thread_handler (arg=0x50000dc4) at /Users/james/Developments/barkinglabs/base-firmware/esp-idf/components/bt/common/btc/core/btc_task.c:207
#2  0x4204008a in osi_thread_run (arg=<error reading variable: value has been optimized out>) at /Users/james/Developments/barkinglabs/base-firmware/esp-idf/components/bt/common/osi/thread.c:165
#3  0x4038f652 in vPortTaskWrapper (pxCode=<optimized out>, pvParameters=<optimized out>) at /Users/james/Developments/barkinglabs/base-firmware/esp-idf/components/freertos/FreeRTOS-Kernel/portable/riscv/port.c:202
ELF file SHA256: 871f5ae0f1af2435

```

```
E (662275) esp-tls-mbedtls: mbedtls_ssl_setup returned -0x7F00
E (662275) esp-tls: create_ssl_handle failed
E (662275) esp-tls: Failed to open new connection
E (662285) transport_base: Failed to open a new connection
E (662295) HTTP_CLIENT: Connection failed, sock < 0
E (662305) fi_api: Failed to open HTTP connection: 0x7002
```

**2023-08-15**
Y: some stability testing and fix for cxd5605term over ble with S2.5, addressing IAC questions and try to reproduce bugs
T: some logging improvements for cxd5605term, and look into module hanging bug reported in IAC

**2023-08-14**
Y: got cxd5605term running on S2.5 over ble 
T: finished up cx tickets over the weekend, doing some stress testing on the cxd5605term make sure it is stable enough for lab tests 

- The CXD5605term over BLE for S2.5 seems mostly stable if we disable RTT logging for cxd5605 bridge
- but still need to rework the logging, seems a little messy
- looking at factory reported bug with module bricking, trying to reproduce

**2023-08-11**
Y: Backported CXD5605term over BLE into older S2.5 for lab GPS testing, done as much testing as I can without S2.5 HW, and a few minor fiterm bug fixes
T: Today hopefully getting S2.5 dev kit, trying to the filink reset mechanism etting it ready for development 

**2023-08-10**
Y: FW CX triage on, getting back the S2.5 FW and getting it ready for cxd5605term support
T: getting S2.5 hw from Charles and getting it ready for development 

**2023-08-09**
Y: Some clean up and stability fixes for cxd5605term, and adding filink reset mechanism
T: Setup another BeeLink PC for Adam, look into bring up cxd5605term for S2.5 for lab testing 

**2023-08-08**
Y: Refactor uart drivers into BPS_UART, pushed 4.11.7 to 50% of sl
T: Fixing filink reset mechanism on target device reboot

**2023-08-07**
Y: pushing out 4.11.7 fw and monitor rollout
T: bump 4.11.7 to 50%, and address cx tickets over the weekend , continue refactoring uart to bsp.

**2023-08-04**
- [x] Bring up discussion with stackoverflow detection ✅ 2023-11-07
- [x] Refactor UART to BSP_UART
- [x] Refactor CXD5605 backend common code

Also most LLE data retry seems to be on wifi, where it seems like certain wifi connection/router can't handle too large of packet?
There might be flaky wifi, where the lle payload is too big for router to handle well.

Y: Fix new bug discovered in 4.11.x release, where server try to push LLE data to collar with dead CXD5605 and causing crash loop
T: Go back to getting backhaul muxing PR merged and started on converting uart driver to bsp.

**2023-08-03**
Y: Getting Beelink mini PC setup with wireguard remote access ready for Adam to use. Working on backhaul muxing PR and planning for next step.
T: refactor uart driver to bsp and few other follow up task to the back haul muxing pr er follow up task to the back haul muxing 

- Found a big bug, we are not detecting dead cxd5605 properly and still attempting to inject LLE into it. This is causing a crash loop with those bad units.

**2023-08-02**
Y: pushed out backhaul muxing work for review
T: got beelink pc and getting it setup with Ubuntu and remote access to allow the team to use with the spirent Gnss simulator at Adam’s home

**2023-08-01**
Y: Pushed 4.11.5 FW to another 10K units, cleaning up backhaul muxing work
T: More cleaning up backhaul muxing changes for review, and testing it.

**2023-07-31**
Y: got backhaul muxing working with both uart and rtt
T: going back clean up everything for back muxing work for review 

**2023-07-28**
Y: fixing a corner case in lte submission report sending when lte signal is low collar could be sending multiple reports, cut new 4.11.5 release to internal folks for testing 
T: getting backhaul muxing working for RTT backend

**2023-07-27**
Y: pushed out WIP PR for FW backhaul muxing, created new 4.11.4 release with few minor bug fixes
T: Get FW backhaul muxing working for RTT, and push 4.11.4 to the current 1K stable-rollout external users.

**2023-07-26**
Y: Fixing up some CXD5605 GNSS server crashes found in 4.11.x release
T: Got CXD5605 term working with backhaul mux link, also reducing duplicate memory usage in both uart driver and filink by combining the two



**2023-07-25**
Y: Working on CXD5605 term via backhaul mux link implementation
T: Continue with CXD5605 term, also looking into a few more cxd5605 gnss server crashes in 4.11.3 FW

We should really just integrate UART with filink in a single thing.

- [x] Check in with Nick on the false escape detection ✅ 2023-08-22

- [random ping out of state](https://app.asana.com/0/1119265580120512/1205079701532979/f)
- [Very far away ping](https://app.asana.com/0/1119265580120512/1205138453958384/f)
- 

**2023-07-21**
Y: Got a proof of concept fw backhaul muxing working in test harness FW
T: Getting a host side tool to send filink framed messages to FW for muxing testing

- [x] ask the team: How do we feel about replacing test harness with flink messages over FT260, this means a new term to replace ft260term. ✅ 2023-09-01
- to share the fw backhaul muxing we need both cxd5605 term or the log term in the same program. Or somehow make filink server?

**2023-07-20**
Y: pushed 4.11.2 to another 500 users, got a rough implementation of fw backhaul muxing implemented 
T: going start adding the fw backhaul muxing to test harness fw

**2023-07-19**
Y: Fixing the FW version string bug, and push out new 4.11.2 FW
T: Continue working on fw backhaul muxing implementation.

**2023-07-18**
- [x] Clean up the mess of FW version string ✅ 2023-07-19
Y: work on fw backhaul mixing. pushed out newer 4.11.1 with minor bug fixes, which turns out had a bug that caused collars to in a firmware update loop. The updated units have since then been rolled back.
T: fix the fw version string bug that caused fw up, and repush the new fw version 

The hardest part with backhaul muxing is the channel handler need to remember the backhaul/phy which the message was send from.

**2023-07-17**
Y: Start working on firmware testing feature adding backhaul muxing with fillink
T: Continue working on backhaul muxing via filink, continue push out 4.11 FW

Pushed out 4.11.1 to fix some QC changes from Charles, and worked on fw backhaul muxing via filink.

**2023-07-14**
Y: adding “test” for test rack testing 
T: release 4.11 fw to small cohort of external users

**2023-07-13**
Y: continue monitoring 4.11.0 release, adding some external user to the cohort for testing, work on factory ticket from backlog
T: same for 4.11.0 monitoring, pick up ticket to work on fw test rack setup 

**2023-07-12**
Y: pushed out 4.11 FW to internal user and monitor releases, experiments with GUSE cxd5605 cmd see if that make any difference in Gnss performance 
T: continue monitor internal release of 4.11 and pick up next task from fw back log

Found list of collars that may help from new LLE fw
- [Nova](https://internaltools.corp.tryfi.com/devices/FC33E611609)
- [bose](https://internaltools.corp.tryfi.com/devices/FC33A376573)
- [Mookie](https://internaltools.corp.tryfi.com/devices/FC33F056904)
- [Goose](https://internaltools.corp.tryfi.com/devices/FC32M550561)
- [Mia](https://internaltools.corp.tryfi.com/devices/FC33A361926)
- [Frankie](https://internaltools.corp.tryfi.com/devices/FC33A379347)
- [Taco](https://internaltools.corp.tryfi.com/devices/FC33D705028)

**2023-07-11**
- [x] Monitor if LLE improves GNSS fix  [beatric](https://app.asana.com/0/1119265580120512/1205012491582013/f) [tony](https://internaltools.corp.tryfi.com/devices/FC33D710236) ✅ 2023-09-08

Y: Cutting 4.11 FW for LLE changes
T: Release 4.11 to internal testers and monitor for status

Hi all, I just pushed a new FW 4.11.0 to the internal S3 and S3.1 testing channel, please update your collar FW when you have a chance. The major changes are:
- Updated server response protocol to collar (potentially less data usage)
- Server pushed AGNSS LLE data, over wifi and LTE (keep GPS assistance data more up to date, and help when collar have poor LTE signal)
- Fixing a potential bootloop bug, where collar just appear completely unresponsive
These changes are mostly bug fixes and improve behaviour for a few corner cases, ideally everything should work the same as before.

**2023-07-10**
Y: Doing some experiment see if SBAS gnss system could improve GPS performance
T: Cutting a new FW release for internal to test out the backend pushed LLE changes.

Really different GPS location with very accurate positions
https://app.asana.com/0/1119265580120512/1204993029122748/f
https://internaltools.corp.tryfi.com/devices/FC33E606180/reports?before=2023-07-04T23:45:00.000Z

**2023-07-07**
Y: testing LLE data pushed via backend, also measuring time to first gps fix, see if there is any difference 
T: more testing of backend pushed LLE and see if there is any improvement to be made for faster first gps fix

- [x] Send email to Sony asking if SBAS can be correctly enabled, and how to observe it is working ✅ 2023-07-19
- [x] Can we look at the SNR ratio to rate signal level? Is there any pattern here? ✅ 2023-07-10

`00:09:05.493 I  cxd5605 gs: Position hint: 423959232 -711072512 0`

Or is this i2c collision
```
01:00:10.532 I  bq27421 check flags=0x0288 ctrl_status=0x2098
01:00:12.560 D  process_sample_store: steps=0, duration=3.000s
01:08:44.562 E  i2c error: 0x00008209 78 counte
01:08:44.562 E  bq25180 flags detected: 0x5c
01:08:44.563 I  Added remote log: 12
01:08:44.564 I  Syncing UTC clock
01:08:44.567 E  LTE modem is awake when it should be sleeping!  Forcing modem offline.
01:08:46.232 I  module_hsm_send_event: TIMER
01:08:46.233 I  brain_pick_report_backhaul: Sending WiFi (inactive interval expired 60s)
```

**2023-07-06**
Y: Wrapped up LLE preloading FW changes for review.
T: Get LLE preload web backend change deployed and start testing.
- [x] How do I measure if fleet wide LLE push is successful ✅ 2023-07-11
- [x] Update test cases in test rack doc ✅ 2023-07-11
- [x] Experiment with freeRTOS bring up? ✅ 2023-07-19

```
00:09:24.597 I  cxd5605 gs: Position hint: 423959392 -711072704 0 // from server on cell-lookup
00:01:52.489 I  cxd5605 gs: Position hint: 423920288 -711079040 -518 // my valid and decent location
```

Getting 1 good fix and one bad fix, this is really weird.
- [x] Server config push require min fix SAT to be 6, which is pretty hard ✅ 2023-07-07
- [x] When altitude is negative number, need to verify that is handled correctly ✅ 2023-07-07
![[Pasted image 20230706230128.png]]

- [x] Investigate  time travel? ✅ 2023-09-01
```
00:00:07.540 I  cxd5605 gs: state change: DISABLING -> DISABLED
00:00:07.540 I  gnss s 8:0
00:00:07.541 I  Added remote log: 12
00:00:08.485 I  bq27421 check flags=0x0288 ctrl_status=0x2098
00:00:10.540 D  process_sample_store: steps=0, duration=3.000s
00:00:12.486 I  module_hsm_send_event: TIMER
00:00:12.502 I  nrf9160: Modem version info: 2.0.0, (2, 0, 0), (refs/tags/released/2.0.0, 905091eccac46fc888bedc626e2364e917a94f9e), (NCS: 2, 0, 0), (Modem FW: mfw_nrf9160_1.3.1)
00:00:12.503 D  nRF9160 FW is up to date
00:00:12.504 I  brain_pick_report_backhaul: Skipping (post-BLE interval 12s/60s)
00:00:12.504 I  brain_pick_report_backhaul: Skipping (post-BLE interval 12s/60s)
00:00:12.505 I  evaluate_transition_targets: -> '', condition 'none'
00:00:12.505 I  hsm_instance_transition: null transition
00:00:12.506 I  Added remote log: 7
00:00:13.618 D  process_sample_store: steps=0, duration=3.000s
00:00:16.696 D  process_sample_store: steps=0, duration=3.000s
00:00:17.481 D  fi_ble_log_state: advertising
00:00:17.483 D  LED state: 0x0
00:00:17.483 I  Battery charging state change: 2 --> 0
00:00:17.484 I  Battery: state 0, bq25180_stat0:0x61, is_chg:0 has_pwr:0
00:00:17.484 I  HSM: T1: 0s T2: -1s T3: -1s State: [ no-connection ]
00:08:49.486 E  i2c error: 0x00008209 78 counte
00:08:49.487 E  bq25180 flags detected: 0x5c
00:08:49.488 I  Added remote log: 12
00:08:49.488 I  Syncing UTC clock
00:08:49.492 I  module_hsm_send_event: TIMER
00:08:49.492 I  brain_pick_report_backhaul: Sending WiFi (post-BLE interval expired 60s)
```



**2023-07-05**
Y: handling web backend PR feed backs and some rework
T: push out LLE preload FW changes, and more testing of LLE preload 

- [x] Really need to mine data on GPS success/failure and see if there is any pattern ✅ 2023-09-01
- [x] Many CX ticket complain GPS tracking performance change from S2. Be nice to understand why S2 behaviour was. ✅ 2023-07-07
- [x] CXD lle injection can fail in the middle of the injection, but later still read out correctly ✅ 2023-07-07
- [x] It is possible LLE inject start, while timed out ✅ 2023-07-07
- [x] Find some data on GPS only vs GPS + GLONASS performance ✅ 2023-09-01

**2023-07-03**
Y: Wrapping up PR feedback for protobuf response FW change
T: Cleaning up and publish LLE preload FW and web backend PR