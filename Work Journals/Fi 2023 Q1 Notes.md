---
publish: false
reviewed: 2023-04-10
review-frequency: ignore
link:
- '[[fi]]'
- '[[barking labs]]'
tags:
- diary
---
2023-02-06-Mo

**2023-03-30**

```
00:00:28.000 I  bq27421 check flags=0x0109 ctrl_status=0x209a
00:00:28.441 I  Fast advertising.
00:00:28.441 W  !!!!!ble_evt_handler: disconnected(19)!!!!
00:00:28.441 I  module_hsm_send_event: BLE_DISCONNECT
00:00:28.441 I  evaluate_transition_targets: -> 'no-connection', condition 'none'
00:00:28.442 I  hsm_instance_transition: moving to state: no-connection
00:00:28.442 I  Transitioning to state: no-connection
00:00:28.442 I  Exiting state: ble:idle
00:00:28.443 I  Running exit action: stop_timer
00:00:28.443 I  Exiting state: ble-connection
00:00:28.443 D  Stopping counter: 22, 13, 13
00:00:28.443 I  Running exit action: ble_stop
00:00:28.444 D  brain_consume_event: 4
00:00:28.444 I  Running transition action: report_disconnected_from_stable
00:00:28.444 I  Entering state: no-connection
00:00:28.444 D  Starting counter: 21, 10, 28
00:00:28.445 I  Running entry action: start_timer
00:00:28.445 I  Starting HSM timer -- 5000 ms
00:00:28.446 I  Added remote log: 7
00:00:31.039 D  process_sample_store: steps=0, duration=3.000s
00:00:33.445 I  module_hsm_send_event: TIMER
00:00:33.445 I  brain_pick_report_backhaul: Skipping (post-BLE interval 5s/60s)
00:00:33.445 I  brain_pick_report_backhaul: Skipping (post-BLE interval 5s/60s)
00:00:33.445 I  evaluate_transition_targets: -> '', condition 'none'
00:00:33.446 I  hsm_instance_transition: null transition
00:00:33.447 I  Added remote log: 7
00:00:34.124 D  process_sample_store: steps=0, duration=3.000s
00:00:34.501 D  execute_evt_callback: BLE connected! peer=8d:66:ee:47:3d:74 addr_id_peer=0 addr_type=2
00:00:34.683 I  ble_evt_handler: DLE update tx=251B rx=251B tx_time=2120us rx_time=2120us
00:00:34.981 I  ble_evt_handler: phy update: status=0 tx_phy=2 rx_phy=2
00:00:35.013 I  GATT ATT MTU on connection 0x0 changed to 247.
00:00:35.013 I  ble_evt_handler: MTU exchange response 247 bytes
00:00:35.253 D  BLE write: 13
00:00:35.253 D  Processing BLE write msg: 13 2
00:00:35.523 D  BLE write: 44
00:00:35.523 D  Processing BLE write msg: 44 1
00:00:35.523 D  Received CTRL POINT cmd: 1
00:00:35.524 I  central issued attach
00:00:35.524 I  Added remote log: 12
00:00:35.525 I  module_hsm_send_event: BLE_CONNECT
00:00:35.526 I  evaluate_transition_targets: -> 'ble-connection', condition 'none'
00:00:35.526 I  hsm_instance_transition: moving to state: ble-connection
00:00:35.526 I  Transitioning to state: ble-connection
00:00:35.526 I  Exiting state: no-connection
00:00:35.527 D  Stopping counter: 21, 17, 7
00:00:35.527 I  Running exit action: stop_timer
00:00:35.527 I  Entering state: ble-connection
00:00:35.527 D  Starting counter: 22, 13, 35
00:00:35.528 I  Running entry action: lte_stop
00:00:35.553 D  brain_consume_event: 6
00:00:35.554 I  Running entry action: gps_stop
00:00:35.554 I  Running entry action: ble_start
00:00:35.554 D  brain_consume_event: 3
00:00:35.554 I  Entering sub-machine: ble-connection
00:00:35.555 I  Transitioning to state: ble:establishing
00:00:35.555 I  Entering state: ble:establishing
00:00:35.555 I  Running entry action: start_timer
00:00:35.555 I  Starting HSM timer -- 5000 ms
00:00:35.556 I  Added remote log: 7
00:00:35.556 I  module_hsm_send_event: LTE_MODEM_SLEEP
00:00:35.557 W  hsm_instance_transition: state='ble:establishing', Unexpected event 'LTE_MODEM_SLEEP'
00:00:35.558 I  Added remote log: 7
00:00:35.673 D  BLE write: 69
00:00:35.673 D  Processing BLE write msg: 69 1
00:00:35.673 W  !!1!!!
00:00:35.674 I  module_hsm_send_event: WIFI_SETUP_GET_SCAN_LIST
00:00:35.675 W  hsm_instance_transition: state='ble:establishing', Unexpected event 'WIFI_SETUP_GET_SCAN_LIST'
00:00:35.676 I  Added remote log: 7
00:00:35.793 D  BLE write: 72
00:00:35.793 D  Processing BLE write msg: 72 2
00:00:36.997 D  fi_ble_log_state: attached
00:00:36.999 D  is_chg: 0, has_pwr: 0, SoC: 59%
00:00:37.001 I  State 0, Chg stat: 0
00:00:37.001 I  HSM: T1: 3s T2: -1s T3: -1s State: [ ble-connection, ble:establishing ]
00:00:37.209 D  process_sample_store: steps=0, duration=3.000s

```

- The RTT bug might not be that bad
```
Reading symbols from out/dbg/bin/fc3_f3/bootloader/bootloader.elf...
(gdb) bt
#0  0x000f5f42 in HardFault_Handler ()
#1  <signal handler called>
#2  0x000f7132 in SEGGER_RTT_WriteNoLock (BufferIndex=BufferIndex@entry=2816, pBuffer=pBuffer@entry=0x2003ff48, NumBytes=NumBytes@entry=26) at ../../src/firmware-common/libfi_rtt/RTT/SEGGER_RTT.c:1230
#3  0x000f71a8 in SEGGER_RTT_Write (BufferIndex=2816, pBuffer=0x2003ff48, NumBytes=26) at ../../src/firmware-common/libfi_rtt/RTT/SEGGER_RTT.c:1336
#4  0x000ed376 in fi_app_log_rtt_write (ctx=<optimized out>, str=<optimized out>, len=<optimized out>) at ../../src/nrf52/bootloader/main.c:41
#5  0x000f47a6 in nrf_fprintf_buffer_flush (p_ctx=p_ctx@entry=0x2003ff10) at ../../nrf5_sdk/17.0.2/external/fprintf/nrf_fprintf.c:56
#6  0x000f3688 in postfix_process (p_params=p_params@entry=0x2003ff04, p_ctx=p_ctx@entry=0x2003ff10, newline=newline@entry=false) at ../../nrf5_sdk/17.0.2/components/libraries/log/src/nrf_log_str_formatter.c:150
#7  0x000f36f2 in nrf_log_std_entry_process (p_str=p_str@entry=0xf7e14 <_fini+128> "Inside main", p_args=p_args@entry=0x2003fee0, nargs=nargs@entry=0, p_params=p_params@entry=0x2003ff04, p_ctx=p_ctx@entry=0x2003ff10)
    at ../../nrf5_sdk/17.0.2/components/libraries/log/src/nrf_log_str_formatter.c:192
#8  0x000f2dac in nrf_log_backend_serial_put (p_backend=<optimized out>, p_msg=0x20006314 <log_mempool_nrf_balloc_pool_mem>, p_buffer=p_buffer@entry=0x2003ff48 "<info> app: Inside main\r\r\n\003", length=length@entry=64,
    tx_func=tx_func@entry=0xed36d <fi_app_log_rtt_write>) at ../../nrf5_sdk/17.0.2/components/libraries/log/src/nrf_log_backend_serial.c:87
#9  0x000ed360 in fi_nrf_log_backend_put (p_backend=<optimized out>, p_entry=<optimized out>) at ../../src/nrf52/bootloader/main.c:46
#10 0x000f332c in nrf_log_backend_put (p_msg=0x20006314 <log_mempool_nrf_balloc_pool_mem>, p_backend=0xfb84c <s_fi_nrf_log_backend>) at ../../nrf5_sdk/17.0.2/components/libraries/log/nrf_log_backend_interface.h:225
#11 nrf_log_frontend_dequeue () at ../../nrf5_sdk/17.0.2/components/libraries/log/src/nrf_log_frontend.c:868
#12 0x000f3406 in std_n (severity_mid=severity_mid@entry=196611, p_str=p_str@entry=0xf7e14 <_fini+128> "Inside main", args=args@entry=0x0, nargs=nargs@entry=0)
    at ../../nrf5_sdk/17.0.2/components/libraries/log/src/nrf_log_frontend.c:568
#13 0x000f341e in nrf_log_frontend_std_0 (severity_mid=severity_mid@entry=196611, p_str=p_str@entry=0xf7e14 <_fini+128> "Inside main") at ../../nrf5_sdk/17.0.2/components/libraries/log/src/nrf_log_frontend.c:579
#14 0x000ed50e in main () at ../../src/nrf52/bootloader/main.c:179
(gdb) i r
r0             0x2100              8448
r1             0x2003ff48          537132872
r2             0x1a                26
r3             0xf5f43             1007427
r4             0xb00               2816
r5             0x20046818          537159704
r6             0x1a                26
r7             0x2003ff48          537132872
r8             0x0                 0
r9             0xf7e14             1015316
r10            0x20030000          537067520
r11            0x0                 0
r12            0x0                 0
sp             0x2003fe40          0x2003fe40
lr             0xfffffff9          4294967289
pc             0xf5f42             0xf5f42 <HardFault_Handler>
xpsr           0x1000003           16777219
msp            0x2003fe40          537132608
psp            0x0                 0
primask        0x0                 0
basepri        0x20                32
faultmask      0x0                 0
control        0x0                 0
fpscr          0x0                 0
(gdb)
```


**2023-03-29**
Testing charles' wifi change

```
00:05:12.817 I  Entering sub-machine: run-wifi
00:05:12.818 I  Transitioning to state: wifi:init
00:05:12.818 I  Entering state: wifi:init
00:05:12.818 I  Running entry action: start_timer
00:05:12.818 I  Starting HSM timer -- 10000 ms
00:05:12.819 I  Running entry action: wifi_acquire_sta
00:05:12.819 I  Added remote log: 7
00:05:13.079 I  wifi_on_event: HSM STA acquired (success: 1)
00:05:13.080 I  on_fiwifi_msg: da16200 boot notice
00:05:13.080 I    ver: FRTOS-GEN01-01-48589f13c-000065 (3.2.4.0 GEN), idx: 0
00:05:13.081 I    dpm: 1, ddps: 1, wake: 0, dtim: 50
00:05:13.082 I  module_hsm_send_event: WIFI_STA_ACQUIRED
00:05:13.184 I  evaluate_transition_targets: -> 'wifi:scan', condition 'none'
00:05:13.184 I  hsm_instance_transition: moving to state: wifi:scan
00:05:13.185 I  Transitioning to state: wifi:scan
00:05:13.185 I  Exiting state: wifi:init
00:05:13.185 I  Running exit action: stop_timer
00:05:13.185 I  Running transition action: wifi_init
00:05:13.186 I  Entering state: wifi:scan
00:05:13.186 I  Running entry action: wifi_evaluate_scan_list
00:05:13.186 I  wifi_evaluate_scan_list: scanning
00:05:14.069 I  Added remote log: 7
00:05:14.070 I  module_hsm_send_event: WIFI_SCAN_RESULT_NO_CANDIDATES
00:05:14.070 I  evaluate_transition_targets: -> 'no-connection', condition 'none'
00:05:14.070 I  hsm_instance_transition: moving to state: no-connection
00:05:14.071 I  Transitioning to state: no-connection
00:05:14.071 I  Exiting state: wifi:scan
00:05:14.071 I  Exiting state: run-wifi
00:05:14.071 I  Running exit action: set_ble_postponed_attachment
00:05:14.072 I  Running exit action: wifi_stop
00:05:14.072 I  fiwifi_parser_reset
00:05:14.072 I  Entering state: no-connection
00:05:14.072 I  Running entry action: start_timer
```


**2023-03-28**
- There is a few hundreds of CXD5605 Invalid FW devices 

#### Power consumption measurement
The base have max connection interval of 600ms
- BLE connection:
    - 40-80uA baseline
    - ~125uA average
    - BLE peaks between 4mA to 6mA every 200ms
    - 5 mins duration 41 uWh
- Wifi Connection:
    - 84-140uA baseline
    - 5 mins duration 146 uWh
- LTE Connection:
    - GPS running most 120 seconds
        - Max: 68.2mA, Min: 5.75mA, Avg: 7.75mA
        - GPS 120 seconds + LTE send == 1.12 mWh
    - BLE Advertise only
        - Avg: 237uA, Max: 61mA, 
        - Floor Current: 40uA - 102uA
        - Peaks ~540ms apart
        - 5 mins duration 73.6 uWh

**2023-03-27**
- 4.7.10 release
    - Bump up GPS cycle to 10 sec, and only use server pushed update interval
    - Fix bug where live tracking was not getting disabled.


**2023-03-25**
`../../src/libfi_app/fi_lle_agnss_server.c:125`

**2023-03-24**
- we are getting yet more nrf9160 FW invalid, while the modem still have worked.
- We have a problem generally with out power on sequence.

FedEx: **925412813**
> Nancy Gatzert
> Sony Semiconductor Solutions America
> [1730 N First](https://www.google.com/maps/search/1730+N+First?entry=gmail&source=g) St
> San Jose, CA 95112
> 408-829-4564

- [ ] Need to fix the duration been a float, that means partial seconds as input
- [x] GPS FIX FAIL during LTE:idle, which is really useless and should go away ✅ 2023-07-07
- [x] Get fast GPS merged
- [x] Remove hardcoded timing
- [x] Update protos-common for server
- [x] Write out the release plan

Running fast GPS getting me 
```
01:42:57.700 I  evaluate_transition_targets: -> '', condition 'none'
01:42:57.700 I  hsm_instance_transition: null transition
01:42:57.701 I  Added remote log: 7
01:42:57.724 I  bq27421 check flags=0x0109 ctrl_status=0x209a
01:42:59.210 D  process_sample_store: steps=0, duration=3.000s
01:42:59.211 D  fi_motion_detection_get_state: activity threshold 0.000010 3s
01:43:02.301 D  process_sample_store: steps=0, duration=3.000s
01:43:02.302 D  fi_motion_detection_get_state: activity threshold 0.000008 3s
01:51:34.697 E  i2c error: 0x00008209

01:51:34.709 E  ASSERT FAIL: "ret == FI_CXD5605_BACKEND_I2C_VALIDATE_FRAME_RET_SUCCESS 1" file "../../src/libgnss_cxd5605/fi_cxd5605_backend_i2c.c", line 568

01:51:34.710 W  Failed boot count now: 1
01:51:34.710 W  System reset
01:53:08.722 E  Fatal error: 16385, 0, 4 (../../src/nrf52/fi_module/main.c:233)
01:53:08.722 W  Failed boot count now: 2
01:53:08.722 W  System reset
00:00:00.000 !  fi_module build: local-fc3_f3-dev
00:00:00.000 I  Reset reasons:
00:00:00.000 I  - DOG
00:00:00.000 I  - SREQ
```


**2023-03-23**
- Doing a quick test to make sure reproduce the repeated GNSS issue
 ![[Pasted image 20230323100242.png]]
- Need to figure out the release flow for this
    - Gate everything based on cap flag
        - Livetracking=1, low/upper bound
- [x] Need to fix the duration been a float, that means partial seconds as input ✅ 2023-07-05
- [x] GPS FIX FAIL during LTE:idle, which is really useless and should go away ✅ 2023-07-05

**2023-03-22**
- Continue with hooking up accel var detection
- Need to come up with plan to deploy this alone with server side changes

There is a bug in the GNSS+LTE state machine, in 4.6.12.
Where it is possible to re-send the same GPS fix, during a long LLE download, when the LLE download/injection process times out.
Making an emergency hotfix for 4.6.12, that is going to bump 4.6.16

**2023-03-21**
Rlog and wifi broken by base64 
- at park 14:45 resetting and rolling
- 


**2023-03-20**
- Get a variance threshold value for activity in FW
- Chat with Robbie

Starting test at 17:07
Standing still at 17:16
Quick in park walk at 17:27
17:31
- Remote logging is broken on main from PR https://github.com/barkinglabs/firmware/pull/1007/files

**2023-03-17**
- Need to ask about the accel variance thing and how does that correlate with step
- JB want to do server driven backoff
- Learning how to combine running variance 
- Adding accel variance
    - Need a rough design doc on some of the details

**2023-03-16**
- MA team lunch

**2023-03-15**
- [x] Checkin with Robbie on Server implementation ✅ 2023-07-05
- [x] Checkin with Chaitali on Asana board ✅ 2023-07-05
- [x] Modem refactor ✅ 2023-07-05

**2023-03-14**
- Need to update protos-common package in web, but blocked by loren's existing PR that also bump it.
- Start working on modem server?

**2023-03-13**
TODO:
- Prepare for Live tracking meeting
- Share rough design/plan on Slack

There is modem unregistered power down, could there be something there? with higher power drain?

S2.5 vs S3
https://app.asana.com/0/home/1203666506581918/1204171448418726

**2023-03-10**
Refactoring modem and nrf9160 driver

**2023-02-06**
This week's goal, re-factor the LTE server and start using modem_server

- End up focusing on the GPS part, and hooking up the lost dog mode to continually get GPS fix.

FC32M541431 - Unleashed:
- With stable FW, on lost mode there isn't a clear noticeable improvement in quality

FC32L251907 - Terrible:
- Seems to generally have poor gnss quality compare the Unleashed

4.7.2 Experiment FW seems to be crashing repeatedly for some reason.
Need to figure out how to get reboot reasons.

**2023-02-07**
There isn't much I can do right now with different behaviour on the gnss modules. Going to need do a whole day of stable FW gnss behaviour collection, for some baseline performance.

Starting the LDM test at 11:30, with the LED turned off.

Didn't actually start GPS tracking until 11:55 when I still had the ipad app connected.

Somehow the `Terrible` is not performing as bad, might be the new location? I have also disabled the SOS LED flashing to save battery.
Let me try turning LED on at 13:20

At 14:00, so far the GNSS report are noticeably worse.

**Loren**
- How I am doing so far in 1 month, and what can I fix
    - Advice: Prioritize based on unknown

Doing some power consumption measurement, but my bigboard won't connect 

**2023-02-08**
Stopping LDM test at 8:47

Getting some data, and the terrible is really much worse.

Starting new run of 4.7.3 running continues GPS at 12:40

okay at 14:29, we have a bug

doing a new release with 4.7.4, where removing filter for fix reports
@ 15:58

okay, it's confirmed the CXD5605 part is getting stuck, need a way to recover from it.

```
maybe the server publishes a message
"I SHUT THE THING OFF AFTER 15 MINUTES"
then the HSM can figure out whether that's a transition back to restarting
that's probably a good thing to have _anyway_ in case we have any state-escapes we don't know about with continuous tracking mode; we guarantee that it will shut off after a bit, and needs to be latched back on by the HSM
one thing that scares me about continuous tracking mode is leaving it on and killing the battery when we don't need it anymore, like we get a BLE connection or a WiFi connection or something and there's a sneaky path where we don't turn it off
then the gnss server could also do the shutdown + publish thing if it's in continuous tracking mode and it doesn't hear the CXD5605 check in after 2 NMEA burst periods
but it would be the same message, handled by the HSM
maybe with a value-copy <= 4-byte detail in the payload about whether it was a timeout or the part going braindead
```

2023-02-09
Starting new test on 4.7.5 with timeout detection. at 16:34

2023-02-10
Really not much improvement with continues live tracking

2023-02-13
Goal today, perform GNSS power testing

Power consumption, the baseline is ~80uA.

2023-02-14
Need to figure out the power consumption for acquire mode vs tracking mode.

`When the position is fixed and the condition of receiving signals reaches a certain level, the CXD5605GF/5607GF transits to the intermittent operation and achieves low power consumption.`

Need to do more to measure how GPS live tracking are successful. How do we know if it is working?

2023-02-15
Getting the 5605 EVB to start working.

Okay it seems to work fine on windows, so that is probably okay.

started some data collection around 16:04
And ending the test around 16:43

2023-02-16
MA lunch today.
Got the I2C ardvark from Charles

```01:13:39.655 I  evaluate_transition_targets: -> 'ble:submit-report', condition 'none'
01:13:39.656 I  hsm_instance_transition: moving to state: ble:submit-report
01:13:39.657 I  Transitioning to state: ble:submit-report
01:13:39.658 I  Exiting state: ble:idle
01:13:39.659 I  Running exit action: stop_timer
01:13:39.659 I  Entering state: ble:submit-report
01:13:39.660 I  Running entry action: ble_notify_dispatch_and_submit_report
01:13:39.661 I  Sending periodic notify-dispatch
01:13:39.662 I  Proxying new request with req ID=4, chunk_size=198
01:13:39.676 D  Prepared report body: sd
hAEKgQEKEGxvY2FsLWZjM19mMy1kZXYQPyjPHljDImDV4I0CaEFyLE9SWWhySUNuaFNnYkw3Ym9aM0IrNUQ3eVhSYmUxTmUyYzJ0eWVRMkFnTlk9mgEAoAHtd6oBEAgJCw0LCgsLCwwNEBo0xwGyARIIyAEQyAEgoB8o9wEw+wE4+wG4AQQCWgBiKmAI/gIwBThPQJIdSAKAARyIAYYCkAEBmAEDoAEDsAGUArgBjQPAAagK0AH0lQHYAQWIApcdoAL9IsACjp0ByAKsHtgCqYYB4AK1BugChQLwAif4Aq8EgAP4BKAD8AXgAwMCYgAPQg0KCwoJZGVzY2FydGVz
a4
4327624,0,60000,376cd15e
mlog
DwjL24kCOggICBAKGAEgAQ8I5ouKAjoICAoQCBgJIAENCLf0jAI6BggIEAgYKg==

01:13:39.681 D  brain_consume_event: 0
01:13:39.682 I  Running entry action: start_timer
01:13:39.682 I  Starting HSM timer -- 30000 ms
01:13:39.683 I  Added remote log: 7
<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x50.
01:13:39.952 D  BLE write: 40
01:13:39.952 D  Processing BLE write msg: 40 4
01:13:39.953 D  Received NOTIFY ACK: 4 bytes
<debug> nrf_sdh_ble: BLE event: 0x51.
01:13:40.352 I  Fi proxy service request read: seq=0, req ID=4
<debug> nrf_sdh_ble: BLE event: 0x51.
01:13:40.752 I  Fi proxy service request read: seq=1, req ID=4
01:22:12.753 E  i2c error: 0x00008209

01:22:12.762 E  ASSERT FAIL: "ret == FI_CXD5605_BACKEND_I2C_VALIDATE_FRAME_RET_SUCCESS 1" file "../../src/libgnss_cxd5605/fi_cxd5605_backend_i2c.c", line 568

```

user `FC32M568521` will be moved to ben-exciting-tests and observe for any changes.

A long list of users that are getting consistent reboot issue
https://vpc-prod-logs-5vkv67t3fmfcbtov66gwhphb2i.us-east-1.es.amazonaws.com/_dashboards/goto/ced84027b9e0242e6028ab105239ea0f

**2023-02-17**
Need to get LTE to work

What is the expected behaviour with

**2023-02-20**
got asked some really hard question, and really need to work with Loren to understand how to plan and scope features.

HSM issue a publish message
- Check if AGNSS is needed
- LTE OTA needs to happen
- Send a LTE GPS report
    - 

*** Need to figure out this 3 months battery life business.

**2023-02-21**
- AT&T turned off LTE-M in my area.
- CX ticket with Power consumption regression and customer complaining
- LTE work

**2023-02-23**
Merging the fast LTE change, and planning testing.

**2023-02-24**
- Learn how databricks work, and how to get some data on LDM.
    - On average how many position report do we get during LDM
    - What is the quality of position during LDM
    - Total duration of LDM activate

`mcc`
"310410" **AT&T**
"311480" **IT&E Wireless**
"313100" **AT&T FirstNet**
"310260" **T-Mobile**
"311490" **T-Mobile**

```
%NBRGRSRP: 375,5110,72
%XCBAND: 12
%XCBAND=? (1,2,3,4,5,8,12,13,18,19,20,25,26,28,66)
```

**2023-02-27**
Goose is really not having a good time with nrf9160
https://internaltools.corp.tryfi.com/devices/FC32M568521/battery#{%22start%22:%222023-02-23T15:20:51.170Z%22,%22end%22:%222023-02-27T15:20:51.170Z%22}

US MNC
https://en.wikipedia.org/wiki/Mobile_network_codes_in_ITU_region_3xx_(North_America)#United_States_of_America_-_US_-_313

traveling to NYC

**2023-02-28**
Start looking at "Won't activate" devices.

Two S3 collar start draining around the same date
https://app.asana.com/0/1119265580120512/1204082623273975/f
https://app.asana.com/0/1119265580120512/1204082693621333/f

**2023-03-01**
Pushing out 4.7.7 in 9:25 am
created the fw-internal-tests group and pushed the FW to it.
"""
Hi all, We have just pushed new S3 FW, 4.7.7, that enables the live tracking feature. This is based off 4.6.12, so it will include all the recent bug fixes also. This FW is released to a new FW channel `fc3_f3-internal-tests`. If you would like to try out live tracking feel free to move your collar to it, or I can do it for you if let me know your module ID.
The live tracking server feature flag is enabled for everyone in the `InternalTester` group.

Live tracking will only be activated when a collar is outside the BLE and Wifi range. So to test you can turn off the bluetooth on your phone, turn on lost dog mode and go outside with your dog for a while. You should still be able to see the location of your dog on the app with faster update, and hopefully more accurate positioning also.

Please send any feedback my way, and I will be monitoring the data on the backend also.
"""

JB flashed FW on 11am, started walking around same time.
back around 12:22ish
73% -> 66%

**Feedback from JB:**
- LTE edrx to get provide lower power drain during LDM
- Dynamically send position report frequency based on activity
- Stop SOS LED blinking during LDM

New walk from JB 16:52.
- started 60% battery, nope didn't start LDM

Things to analyze:
- I think the initial question I like to get is the typical duration or LDM, and how many position data do we get during LDM and how frequent.
- probably also the typical delay from when a LDM is activated to when the first position report comes back, that might be interesting with regard to some of the stuff we were discussing today
- Need a good way to visualize a LDM

**2023-03-02**
ugh Thor's collar did not fall back to wifi over the night and completely drained the battery.

Questions:
- how to avoid wifi
    -  do we just skip wifi when lost dog mode?
    - I've are getting good LTE signals and GPS position, don't need to bother with wifi
- how to intermittent the tx based on accel data
    - we need upper/lower boundary 
    - GPS report is every 10 seconds 
    - 

**2023-03-03**
With NRF9160 DK, there is clearly no AT&T signal nearby
- I can sometime get connected to AT&T but also quickly disconnect from it

**2023-03-05**
```
00:03:51.571 E  Fatal error: 16386, 0, 805306385 (../../nrf5_sdk/17.0.2/components/libraries/pwr_mgmt/nrf_pwr_mgmt.c:125)
```
?????
This seems to be floating point math crash

Starting battery consumption test on 22:06
- FC32L251907 - Dallas The Terrible sending very 15 sec
- FC32M541431 - Dallas Unleashed sending very 60 sec

**2023-03-06**
Stopping test at 8:24
- FC32L251907 - Dallas The Terrible 57%
- FC32M541431 - Dallas Unleashed at 74%

Weekly Status
James - Live tracking updates
- New feature pushing out to internal-tester FW:
    - Dynamic position update interval based on steps since previous success position report. Position report intervals will range between 15 seconds to 120 seconds.
    - LTE eDRX during live tracking, providing lower power consumption during live tracking
- Some power analysis based on LTE eDRX vs PSM mode

4:51 at park 

Updating the live tracking PRD with server and mobile side work.

$ BUG: Base seem to stop BLE connection when it fails to communicate with server for a while. And does not seem to recover very fast

**2023-03-07**
How to collect feedback on test results?

Hi all,
We just pushed a updated FW to the internal-tests FW channel, 4.7.8. For some updated live tracking feature. The update includes:
- Dynamic position update based on movements. Position update will be uploaded as fast as 15 seconds, and as slow as 120 seconds depending on movements.
- Adding support for LTE eDRX, allows collar to maintain LTE connection with less power consumption.
Please give it a try, and give us any feedback, especially on the latency of the position update during lost dog mode, and any unexpected high power drain.
In my own testing I am getting 20% battery drain over 10 hours, in ideal conditions.

Chat with Loren:
- Any sync up with Mobile/server team
- How to measure success? Handset location with collar?
- Overall latency?
- next step?
- LTE eDRX?
- LDM start up time?
- Modem refactoring?

Why do we use Offline? It does not seem to make any difference in power? Accidental wakeup?


**2023-03-08**
Posting power consumption 

start deleting S2/S2.5 code and drivers

**2023-03-09**
really need to look into the modem not registering/and sleeping correctly. Also wifi disconnect issue again.