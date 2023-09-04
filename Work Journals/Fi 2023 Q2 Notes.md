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
```tasks
path includes Work Journals
not done
```

**2023-06-30**
Y: adding more fw test rack tests for protobuf response 
T: continue with writing tests for protobuf response change and backend LLE preload unit tests

**2023-06-29**
Y: Testing the new binary protobuf web deploy, adding tests for backend lle preload PR
T: getting fw binary protobuf PR ready for review and continue testing.

**2023-06-28**
- Web-socket deployment by Loren

Y: Backend work to extract out meta data from LLE to help backend make decision on whether to pre-load LLE to given collar.
T: Adding tests for backend pre-load PR, and getting it ready for review.

**2023-06-27**
Y: Troubleshooting DA16200 spi bus issue that turns out to be user error, but also shown data streaming over wifi might be too power hungry since the chip needs to be on throughout the duration. Waiting on feedback from wifi chip vendor 
T: while waiting on vendor feedback, switch track to do some backend work, need to do some preprocessing on downloaded LLE binaries to extract meta data out of it for the preloading process 

**2023-06-26**
```
00048.324 D  fi_spi_task_proc: event CMD_END_IRQ (len 0) cmd_addr=10000002 resp_addr1=0
00048.325 D  fi_spi_task_proc: event CMD_END_IRQ (len 0) cmd_addr=10000002 resp_addr1=0
00048.326 D  fi_spi_task_proc: event STATE_CHANGE (len 2) cmd_addr=10000002 resp_addr1=0
00048.327 D  fi_spi_task_proc: ISR state change 2
00048.327 D  fi_spi_task_proc: event END_IRQ (len 0) cmd_addr=10000002 resp_addr1=0
00048.328 D  fi_spi_task_proc: event STATE_CHANGE (len 3) cmd_addr=10000002 resp_addr1=0
00048.329 D  fi_spi_task_proc: ISR state change 3
00048.330 D  fi_spi_task_proc: event RX_READY (len 16) cmd_addr=10000002 resp_addr1=0
00048.331 D  fi_spi_task_proc: rx:
  F1 D0 47 00 08 04 9A 01 42 08 01 12 3B 47 45 54 | ..G.....B...;GET

00048.332 D  poll_spi: 16 bytes
00048.333 D  :
  F1 D0 47 00 08 04 9A 01 42 08 01 12 3B 47 45 54 | ..G.....B...;GET
```

```
00030.781 D  fi_spi_task_proc: event CMD_END_IRQ (len 0) cmd_addr=f1d0d0f1 resp_addr1=0
00030.783 D  fi_spi_task_proc: event CMD_END_IRQ (len 0) cmd_addr=10000002 resp_addr1=0
00030.783 D  fi_spi_task_proc: event STATE_CHANGE (len 2) cmd_addr=10000002 resp_addr1=0
00030.784 D  fi_spi_task_proc: ISR state change 2
00030.785 D  fi_spi_task_proc: event END_IRQ (len 0) cmd_addr=10000002 resp_addr1=0
00030.786 D  fi_spi_task_proc: event STATE_CHANGE (len 3) cmd_addr=10000002 resp_addr1=0
00030.787 D  fi_spi_task_proc: ISR state change 3
00030.788 D  fi_spi_task_proc: event RX_READY (len 16) cmd_addr=10000002 resp_addr1=0
00030.788 D  fi_spi_task_proc: rx:
  F1 D0 0A 00 08 05 EA 03 05 08 01 10 80 08 12 0B | ................

00030.790 D  poll_spi: 16 bytes
00030.791 D  :
  F1 D0 0A 00 08 05 EA 03 05 08 01 10 80 08 12 0B | ................
```


*So, I made some rules for sanity*:
1. `Cmd_Addr` is how the SPIM communicates to the SPIS what's about to happen. This is _always_ set by the nRF52, and cleared to a special "idle" value by the DA16200.
2. `Resp_Addr1` always holds the number of bytes that the SPIS has ready to transmit to the SPIM. This lets the nRF52 size its SPIS->SPIM reads.
3. Despite it being SPI, the link is only ever half-duplex: meaningful bytes are never transmitted simultaneously.
4. The out-of-band GPIO is used by DA16200 to announce it has SPIS->SPIM data ready.

**DA16200->nRF52 transfers:**  
1. DA16200 writes the length to `Resp_Addr1`
2. DA16200 writes the bytes to its SPIS->SPIM buffer
3. DA16200 asserts its "hello" GPIO.
4. nRF52 reads the `Resp_Addr1` register.
5. nRF52 writes to `Cmd_Addr` an encoded value that says "I'm about to read X bytes from your buffer"
6. This write fires a DA16200 Slave IRQ, DA16200 understands a transfer is about to start, DA16200 deasserts the "hello" GPIO.
7. nRF52 writes a Slave-peripheral command that says "Transmit N bytes from the SPIS->SPIM buffer address". (Rounded up to 4 bytes or it fails, but extra bytes are discarded after xfer)
8. The DA16200 slave peripheral shoves the bytes onto the wire.
9. This read fires a DA16200 Slave IRQ, DA16200 sees that the read has completed, writes the "IDLE" value to `Cmd_Addr` .
10. If DA16200 has more data to send, goto step 1.

**nRF52->DA16200 transfers:**  
1. nRF52 reads `Cmd_Addr` until the value is "IDLE".
2. nRF52 writes to `Cmd_Addr` an encoded value that says "I'm about to write X bytes to your buffer"
3. This write fires a DA16200 Slave IRQ, DA16200 understands data is about to arrive and remembers it for future interrupts.
4. nRF52 writes a Slave-peripheral command that says "Transmit N bytes to the SPIM->SPIS buffer address". (rounded up etc)
5. This write fires a DA16200 Slave IRQ, which enqueues a "drain this out" command to its RTOS task.
6. DA16200: The RTOS task wakes and is serviced eventually (it's high priority), and enqueues the contents of the SPIM->SPIS buffer (with the length encoded in `Cmd_Addr`) into the application-level rx bytequeue
7. DA16200: Once the bytes are drained from the SPIM->SPIS buffer, the DA16200 is ready to receive more, so it writes the special IDLE value to `Cmd_Addr`


Y: Testing with the wifi streaming applying back pressure mechanism in non-test FW, and reproducing the same behaviour on LTE backhaul.
T: Troubleshoot out some sleep state management issue with da16200 socket data, where the chip going to sleep would disable socket connection

```
wifi_net_test http_slow
00:03:30.615 D  Sending message -- type: 61
00:03:30.616 D  da16200_phy_spi__read_reg: tx:
  50 08 02 54 C0 00 00 04 | P..T....

00:03:30.617 D  da16200_phy_spi__read_reg: rx:
  00 00 00 00 00 00 00 00 F1 D0 D0 F1 | ............

00:03:30.617 D  da16200_phy_spi__write_cmd:
  50 08 02 54 80 00 00 04 02 00 00 10 | P..T........

00:03:30.618 D  da16200_phy_spi__write_data:
  00 00 00 00 80 00 00 10 F1 D0 0A 00 08 07 EA 03 | ................
  05 08 01 10 80 08 75 CD                         | ......u.

00:03:30.618 D  fiwifi_send_message: sent 16B
 > 00:03:50.295 D  bq25180 stat0 change: 0x00
00:03:50.295 D  bq25180 stat1 change: 0x00
00:03:50.296 D  bq25180 flag0 change: 0x40
00:03:50.296 I  bq25180 charge status? 3, power good? 1 flags 0x00

```

**2023-06-23**
Y: Got wifi applying back pressure working in test harness, where the nrf52 can control how much data the wifi chip send over the channel with socket_read cmd
T: Getting it working with the production app, and reproduce the same behaviour on LTE.

- I need to understand how the socket get kept connected during sleep, and maybe it does not.
- also how to tell when a tcp socket is closed

```
00020.248 I  00020.248 I  process_wake_lock_pin: 0
on_fiwifi_msg: done
00020.254 D  poll_read_socket_data_to_spi: socket(1) ready
00020.256 D  fi_spi_load_tx_buf: resp_addr1=0, n=13
00020.257 D  00020.257 D  fi_spi_load_tx_buf: resp_addr1=0, n=0
fiwifi_send_message: Sent 20
00023.623 D  poll_spi: 16 bytes
00023.624 D  :
  F1 D0 47 00 08 04 9A 01 42 08 01 12 3B 47 45 54 | ..G.....B...;GET

00028.000 E  fi_module_app: fiwifi parser timeout!
00028.000 I  fiappstats 69 71
00028.001 I  parser msg:
  08 04 9A 01 42 08 01 12 3B 47 45 54 | ....B...;GET
```

```
00100.573 D  poll_spi: 16 bytes
00100.574 D  :
  F1 D0 0A 00 08 5C EA 03 05 08 01 10 80 04 65 04 | .....\........e.
```


I am not capturing the lle injection error correctly.
```
00:01:29.626 D  cxd5605 lle: Finished 2/7
00:01:31.458 D  cxd5605 lle: Finished 3/7
00:01:32.708 D  cxd5605 lle: Finished 4/7
00:01:33.780 D  cxd5605 lle: Finished 5/7
00:01:35.175 D  cxd5605 lle: Finished 6/7
00:01:36.433 E  cxd5605: lle injection CEPW failure -22
00:01:36.434 E  CXD5605 flow 3 error -22, disabling
00:01:36.435 I  cxd5605 gs:   en: 1 ok: HEALTHY pos: 0 tcxo: 1 lle: 0 fw: "20107,1059ebf,123E"
00:01:36.435 I  cxd5605 gs: state change: INJECTING LLE -> AWAITING LLE
00:01:36.436 I  gnss s 4:3
00:01:36.436 I  Added remote log: 12
00:01:37.457 E  fiwifi_send_message: tx_flush failure
00:01:37.457 I  submission_server: INJECT_LLE -> RECV_RESP
```

**2023-06-22**
Y: Start proper implementation of mechanism for nrf52 FW to apply wifi backhaul on socket data.
T: Getting wifi back pressure applying working

> “wifi on” -> “wifi_config” -> “wifi connect” -> “wifi_net_test http”
```
wifi on
wifi_config descartes ithinktherefore
wifi connect
wifi_net_test http_slow
```

- [ ] Need to understand the backend device handoff logic, sometime it's not working very well.
- [-] Talk to loren about adding task to "project overview"
- [x] How does the backend determine which constellation needs to be pushed ✅ 2023-07-05

**2023-06-21**
Y: Applying 3 constellations of LLE data back to back in single device response msg, via wifi streaming.
T: Reproduce the same behaviour on LTE, and switch gear to get try getting the streaming behaviour implemented properly in wifi firmware

**2023-06-20**
Y: Got a working setup with wifi backhaul streaming and applying back pressure, allowing backend server to send arbitrarily sized data in single device response.
T: Reproduce the same data streaming and applying back pressure behaviour over LTE, and flush out a few nrf52 side changes that needed for streaming change

- [x] Need to first do a proof of concept change to make sure back pressure actually works.

**2023-06-19**
Y: Cleaning up the submission data service, getting LLE preloading working while live tracking
T: Continue with cleaning up the submission data service, and proof of concept change of data streaming over wifi backhaul also applying back pressure.

- [koda](https://internaltools.corp.tryfi.com/devices/FC33D707007) house hold with 2 collar 1 S2.5 and S3.1, where the S3.1 have poorer GPS performance in comparison.

**2023-06-17**
- [x] Need to merge lle_agnss_server into the submission_data_server
- [x] Still need to test live tracking with lle injection

**2023-06-16**
- [x] Need to really untangle the submission data handling
- [x] Make LLE injection happen during positioning if needed
Y: getting LLE injections working in fw while love tracking, getting esp32 dev kit setup for base testing
T: more testing on binary protobuf response over base, and try a proof of concept change of data streaming over wifi backhaul allowing less ram usage in 

**2023-06-15**
Y: analyzing the lle data format, and how best to process them, got a prototype of preload lle working for all gnss constellations working between collar and local backend
T: work out the details on collar behavior for ble break to LTE+Gnss flow, bring up esp dev kit for some base fw testing bring up esp dev kit for some base fw testing 

My Base using `FB32E000101_factory_data.bin`
https://github.com/barkinglabs/firmware-module-identities/tree/main/loren/fb3_f1

My test nuc using `FC32H000327_factory_data.hex`

modifying the local db to allow my base to work
my user id in db seems to be `995899` and house hold id `1002086` got from my base `FB32L553684`
now I need to make base `FB32E000101` look like my existing base

**2023-06-14**

```mermaid
flowchart TB
    noconn["no connection"]
    ble["ble connection"]
    wifi["wifi Scan"]
    lte["lte connection"]
    gps["gps run"]
    lte-dispatch["lte send report"]
    lte-response["handle server response"]
    gps-lle["gps inject LLE data"]
    gps-stop["stop running gps"]
    
    ble --> noconn
    noconn --> |wait 60 seconds| wifi
    wifi --> |no wifi candidate| lte
    lte --> |GPS LLE is valid| gps
    lte --> |GPS LLE NOT valid| lte-dispatch
    gps --> |Positioning success/fail| lte-dispatch
    lte-dispatch --> lte-response
    lte-response --> | No LLE data to inject | noconn
    lte-response -->|gps running| gps-stop
    lte-resposne -->|gps idle| gps-lle --> noconn
    gps-stop --> gps-lle --> gps
```

1. BLE disconnect
2. Wait 60 seconds
3. Wifi scan
4. CXD5605 check LLE requirement (GPS LLE is valid)
    1. If GPS LLE valid, start positioning, If GPS position end, dispatch LTE report
    2. Else send cell-lookup report
6. Process server response
    1. Handle LLE data if there is any

- [x] Get ESP dev-kit running base firmware
- [x] confirm with sony lle data header format is fix
- [x] Need to chat with Charles to see if he is going to do a wifi update, and if we can fix the wifi push/pull data 
- [x] Make LLE injection happen during positioning if needed ✅ 2023-07-05
- [x] Need to first do a proof of concept change to make sure back pressure actually works. ✅ 2023-07-05
- [x] Confirm the BLE -> LTE+GNSS transition flow with everyone

![[Sony LLE Data.png]]

LLE data updated everyday 0:00 - 0:30/UTC

![[Sony LLE data format.png]]

- gps_14days_05_14.lle
```
00000000: 3232 3631 3631 3948 3830 3159 4100 0000  2261619H801YA...
00000010: 8024 6064 002b 0819 488a 0000 0000 0300  .d.+..H.......
00000020: 0100 0000 0000 0000 0101 0300 fc7d 5d64  .............}]d
00000030: 99fd 0849 3ce1 7041 b873 de1c 75ef 5cc1  ...I<.pA.s..u.\.
00000040: 8742 1cdd 279b 71c1 68da ccee e13d a540  .B..'.q.h....=.@
00000050: 200c e628 9e94 9f40 d247 3b82 d8cd 9c40   ..(...@.G;....@
00000060: 0000 0000 0000 0000 99fd 0849 3ce1 7041  ...........I<.pA
00000070: b873 de1c 75ef 5cc1 8742 1cdd 279b 71c1  .s..u.\..B..'.q.
00000080: 68da ccee e13d a540 200c e628 9e94 9f40  h....=.@ ..(...@
00000090: d247 3b82 d8cd 9c40 0017 4339 0060 4aac  .G;....@..C9.`J.
```
- gps_3days_05_14.lle
```
00000000: 3232 3631 3631 3948 3830 3159 4100 0000  2261619H801YA...
00000010: 8024 6064 000a 0819 f03c 0000 0000 0300  .d.....<......
00000020: 0100 0000 0000 0000 0101 0300 fc7d 5d64  .............}]d
00000030: 99fd 0849 3ce1 7041 b873 de1c 75ef 5cc1  ...I<.pA.s..u.\.
00000040: 8742 1cdd 279b 71c1 68da ccee e13d a540  .B..'.q.h....=.@
00000050: 200c e628 9e94 9f40 d247 3b82 d8cd 9c40   ..(...@.G;....@
00000060: 0000 0000 0000 0000 99fd 0849 3ce1 7041  ...........I<.pA
00000070: b873 de1c 75ef 5cc1 8742 1cdd 279b 71c1  .s..u.\..B..'.q.
00000080: 68da ccee e13d a540 200c e628 9e94 9f40  h....=.@ ..(...@
00000090: d247 3b82 d8cd 9c40 0017 4339 0060 4aac  .G;....@..C9.`J.
```

- gps_3days_06_14.lle
```
00000000: 3232 3636 3231 3948 3833 3259 4100 0000  2266219H832YA...
00000010: 0003 8964 000a 081b d041 0000 0000 0300  ...d.....A......
00000020: 0100 0000 0000 0000 0101 0300 7c5c 8664  ............|\.d
00000030: 56b6 e9f2 0d8d 7741 333c 16ca c04e 6041  V.....wA3<...N`A
00000040: 28c6 bc33 1a38 4841 6dfb 531f 0960 91c0  (..3.8HAm.S..`..
00000050: c9b2 f23d f7ac 9d40 e0d2 a3c2 dc3b a940  ...=...@.....;.@
00000060: 0000 0000 0000 0000 56b6 e9f2 0d8d 7741  ........V.....wA
00000070: 333c 16ca c04e 6041 28c6 bc33 1a38 4841  3<...N`A(..3.8HA
00000080: 6dfb 531f 0960 91c0 c9b2 f23d f7ac 9d40  m.S..`.....=...@
00000090: e0d2 a3c2 dc3b a940 c0ac 3b39 0050 29ac  .....;.@..;9.P).
```

- gps_7days_06_14.lle
```
00000000: 3232 3636 3231 3948 3833 3259 4100 0000  2266219H832YA...
00000010: 0003 8964 0016 081b 3060 0000 0000 0300  ...d....0`......
00000020: 0100 0000 0000 0000 0101 0300 7c5c 8664  ............|\.d
00000030: 56b6 e9f2 0d8d 7741 333c 16ca c04e 6041  V.....wA3<...N`A
00000040: 28c6 bc33 1a38 4841 6dfb 531f 0960 91c0  (..3.8HAm.S..`..
00000050: c9b2 f23d f7ac 9d40 e0d2 a3c2 dc3b a940  ...=...@.....;.@
00000060: 0000 0000 0000 0000 56b6 e9f2 0d8d 7741  ........V.....wA
00000070: 333c 16ca c04e 6041 28c6 bc33 1a38 4841  3<...N`A(..3.8HA
00000080: 6dfb 531f 0960 91c0 c9b2 f23d f7ac 9d40  m.S..`.....=...@
00000090: e0d2 a3c2 dc3b a940 c0ac 3b39 0050 29ac  .....;.@..;9.P).

```

Y: Plumbing through the HSM for LLE preloading, some HSM clean up now that LLE data is pushed from backend.
T: Working on web and collar coordination for deciding when and which LLE binary to send. 

- Still need to think about which signal to use for moving forward the LLE download flow.
- Also need to think about how to stop the flow.
- Should we always send a report when LLE is successfully applied?
    - That sounds reasonable?

**2023-06-13**
- [Carson](https://internaltools.corp.tryfi.com/devices/FC33A371660/battery) seems to not connect over BLE at all, like it is not advertising, triggered remote reboot, and waiting for reset. Check back tomorrow, currently at day care (06/13)
- [Skye](https://internaltools.corp.tryfi.com/devices/FC33D706545) S3.1 Collar that battery is slowly going up.

Y: Got help from Robbie and Phil to test the binary protobuf response protocol changes via BLE backhaul over iOS, Ordered HW for base BLE testing
T: More LLE preloading HSM wangling, and getting the nuc test rack HW setup

Conditions that allow CXD5605 to start positioning
- LLE updated
- LTE Boot

```
00:55:27.338 I  HSM: T1: 4s T2: -1s T3: -1s State: [ no-connection ]
00:55:27.838 D  process_sample_store: steps=0, duration=3.000s
00:55:28.340 I  bq27421 check flags=0x0109 ctrl_status=0x2088
00:55:28.341 D  fi_cxd5605_flow_enable__set_state: WAIT_FOR_GNSS_MODE => GET_VERSION
00:55:28.454 D  fi_cxd5605_flow_enable__set_state: GET_VERSION => GET_TCXO
00:55:29.070 D  fi_cxd5605_flow_enable__set_state: GET_TCXO => GET_LLE_VALIDITY
00:55:29.134 E  CXD5605 flow 1 error -13, disabling
00:55:29.134 I  module_hsm_send_event: GPS_DISABLED
00:55:29.135 W  hsm_instance_transition: state='no-connection', Unexpected event 'GPS_DISABLED'
00:55:29.136 I  Added remote log: 7
00:55:29.137 I  cxd5605 gs:   en: 0 ok: UNKNOWN pos: 0 tcxo: 1 lle: 0 fw: "20107,1059ebf,123E"
00:55:29.137 E  ASSERT FAIL: "s->enabled " file "../../src/libgnss_cxd5605/fi_cxd5605_gnss_server.c", line 367

00:55:29.138 W  Failed boot count now: 1
00:55:29.138 W  infinite_loop_if_halt_on_error: spinning
00:00:00.000 !  fi_module board=3 build=local-fc3_f3-dev platform_id=<null> module_id=FC32H000328
00:00:00.000 I  fi_cpu_log_reset_reason: WDT SREQ
<info> app_timer: RTC: initialized.
```

**2023-06-12**
- LLE Preloading work
    - GNSS Server accept LLE binary despite not needing it
    - GNSS Server successfully complete and signal to lle agnss server
- Push for binary protobuf work
    - Test iOS Fi app build pointing to local web server

Y: Finalizing the binary protobuf response protocol, and testing both the web backend and firmware implementation
T: figure out how to build the iOS app to test the binary protobuf response protocol locally, and also working on getting collar to LLE downloads.

**2023-06-10**
Protos-common pushed to 2.1.13

Recent build errors
```
FAILED: bin/fc3_f3/bootloader/dev_dfu_pkg_bootloader.zip
/opt/homebrew/opt/python@3.11/bin/python3.11 ../../src/firmware-common/gntools/run_in_venv.py --venv bin/venv -- ../../build/fi_package_dfu.py --out-dir bin/fc3_f3/bootloader --hw-ver 11 --sd-req 0x0100 --sd-id 0x0100 --bl bin/fc3_f3/bootloader/bootloader.hex --key-file ../../build/dev_priv.pem
b'/Users/james/Developments/barkinglabs/firmware/out/dbg/bin/venv/bin/python: No module named nordicsemi\n'
Traceback (most recent call last):
  File "/Users/james/Developments/barkinglabs/firmware/out/dbg/../../build/fi_package_dfu.py", line 232, in <module>
    sys.exit(main())
             ^^^^^^
  File "/Users/james/Developments/barkinglabs/firmware/out/dbg/../../build/fi_package_dfu.py", line 227, in main
    fi_package_dfu(*dfu_args, is_dev=True)
  File "/Users/james/Developments/barkinglabs/firmware/out/dbg/../../build/fi_package_dfu.py", line 188, in fi_package_dfu
    _nrfutil(
  File "/Users/james/Developments/barkinglabs/firmware/out/dbg/../../build/fi_package_dfu.py", line 84, in _nrfutil
    subprocess.run(
  File "/opt/homebrew/Cellar/python@3.11/3.11.3/Frameworks/Python.framework/Versions/3.11/lib/python3.11/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/Users/james/Developments/barkinglabs/firmware/out/dbg/bin/venv/bin/python', '-m', 'nordicsemi', 'pkg', 'generate', '--hw-version', '11', '--sd-req', '0x0100', '--key-file', '../../build/dev_priv.pem', '--bootloader', '/Users/james/Developments/barkinglabs/firmware/out/dbg/bin/fc3_f3/bootloader/bootloader.hex', '--bootloader-version', '1686419267', '/Users/james/Developments/barkinglabs/firmware/out/dbg/bin/fc3_f3/bootloader/dev_dfu_pkg_bootloader.zip']' returned non-zero exit status 1.
[124/162] ACTION //src/nrf52/bootloade...mware-common/gntools/toolchains:xcode)
FAILED: bin/fc3_f3/dev_bootloader/dev_dfu_pkg_bootloader.zip
/opt/homebrew/opt/python@3.11/bin/python3.11 ../../src/firmware-common/gntools/run_in_venv.py --venv bin/venv -- ../../build/fi_package_dfu.py --out-dir bin/fc3_f3/dev_bootloader --hw-ver 11 --sd-req 0x0100 --sd-id 0x0100 --bl bin/fc3_f3/dev_bootloader/dev_bootloader.hex --key-file ../../build/dev_priv.pem
b'/Users/james/Developments/barkinglabs/firmware/out/dbg/bin/venv/bin/python: No module named nordicsemi\n'
Traceback (most recent call last):
  File "/Users/james/Developments/barkinglabs/firmware/out/dbg/../../build/fi_package_dfu.py", line 232, in <module>
    sys.exit(main())
             ^^^^^^
  File "/Users/james/Developments/barkinglabs/firmware/out/dbg/../../build/fi_package_dfu.py", line 227, in main
    fi_package_dfu(*dfu_args, is_dev=True)
  File "/Users/james/Developments/barkinglabs/firmware/out/dbg/../../build/fi_package_dfu.py", line 188, in fi_package_dfu
    _nrfutil(
  File "/Users/james/Developments/barkinglabs/firmware/out/dbg/../../build/fi_package_dfu.py", line 84, in _nrfutil
    subprocess.run(
  File "/opt/homebrew/Cellar/python@3.11/3.11.3/Frameworks/Python.framework/Versions/3.11/lib/python3.11/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/Users/james/Developments/barkinglabs/firmware/out/dbg/bin/venv/bin/python', '-m', 'nordicsemi', 'pkg', 'generate', '--hw-version', '11', '--sd-req', '0x0100', '--key-file', '../../build/dev_priv.pem', '--bootloader', '/Users/james/Developments/barkinglabs/firmware/out/dbg/bin/fc3_f3/dev_bootloader/dev_bootloader.hex', '--bootloader-version', '1686419267', '/Users/james/Developments/barkinglabs/firmware/out/dbg/bin/fc3_f3/dev_bootloader/dev_dfu_pkg_bootloader.zip']' returned non-zero exit status 1.
[126/162] LINK bin/fc3_f3/fi_module/fi_module.elf
ninja: build stopped: subcommand failed.

```

**2023-06-08**
Y: Polished the FW handling protobuf device response from all 3 backhaul channel
T: Document all backend changes needed for protobuf device response, and get a prototype branch out for review.

- [x] Add handling for base64 data over BLE
- [x] Document all backend side/protocol level changes ✅ 2023-07-05
- [x] Update Charles' design doc with payload format design ✅ 2023-07-05

**2023-06-07**
Y: Getting binary LLE data handling working in FW
T: Working on getting protobuf devices response on all 3 backhaul channels

**2023-06-06**
Y: troubleshooting binary device response msg inflation in websocket service, working on LLE binary protocol deciding in FW
T: continue with handling LLE binary injection in FW

This is going to be an important note, decoding callback is not called
https://stackoverflow.com/questions/39854434/nanopb-correctly-encoding-and-decoding-repeated-construct-fields-in-submessage/39865767#39865767

**2023-06-05**
Y: Converting FW to accept binary protobuf as devices response from the backend, using less data overall from server to S3 collars
T: Continue on binary protobuf conversion, debugging protobuf decoding issues.

Received in FW
```
26 0A 24 08 EF BF BD 02 10 EF BF BD 02 18 00 20 | &.$............
00 28 00 30 01 48 00 50 06 5D 00 EF BF BD 79 44 | .(.0.H.P.]....yD
70 03 78 01 EF BF BD 01 00 EF BF BD 01 00 EF BF | p.x.............
BD 01 03                                        | ...
```

Send from Backend
```
26 0A 24 08 AC 02 10 AC 02 18 00 20 00 28 00 30 
01 48 00 50 06 5D 00 C0 79 44 70 03 78 01 80 01
00 88 01 00 90 01 03
```

```
  26 0A 24 08 AC 02 10 AC 03 18 00 20 00 28 00 30 | &.$........ .(.0
  01 48 00 50 06 5D 00 C0 79 44 70 03 78 01 80 01 | .H.P.]..yDp.x...
  00 88 01 00 90 01 03 
                       8A 7F 1A 87 7F 12 84 7F 32 | ...............2
  32 36 35 31 31 39 48 38 32 34 59 41 00 00 00 00 | 265119H824YA....
  77 7E 64 00 0A 08 1A 60 3F 00 00 00 00 03 00 01 | w~d....`?.......
  00 00 00 00 00 00 00 01 01 03 00 7C D0 7B 64 69 | ...........|.{di
  FA FC A9 F9 98 78 41 C2 96 3F 12 1D B3 51 41 E6 | .....xA..?...QA.
  8F FE 97 18 B6 48 C1 A0 78 0C D1 E6 75 40 C0 63 | .....H..x...u@.c
  DF 89 8E 47 0A A1 40 BD 16 F1 78 9B 39 A9 40 00 | ...G..@...x.9.@.
  00 00 00 00 00 00 00 69 FA FC A9 F9 98 78 41 C2 | .......i.....xA.
  96 3F 12 1D B3 51 41 E6 8F FE 97 18 B6 48 C1 A0 | .?...QA......H..
  78 0C D1 E6 75 40 C0 63 DF 89 8E 47 0A A1 40 BD | x...u@.c...G..@.
  16 F1 78 9B 39 A9 40 00 76 3D 39 00 D0 31 AC 00 | ..x.9.@.v=9..1..
  00 F8 1F 00 00 00 00 17 00 00 00 00 80 DA C2 05 | ................
  CB 8F FD 15 07 8C F1 00 00 00 00 00 00 00 00 00 | ................
  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
  00 90 00 00 00 00 00 00 00 00 00 CD CC 4C 3F 7C | .............L?|
  D0 7B 64 10 8F DD 3D F8 C2 02 3F 22 FA 3A BD 80 | .{d...=...?".:..
  CE 40 3B 00 A6 1F 3A C0 A3 93 B9 00 00 00 00 00 | .@;...:.........
  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
```


**2023-06-02**
1. Make changes in the `firmware/src/protos-common` tree (I just pushed this branch but yours is fine too: [https://github.com/barkinglabs/firmware/tree/lle-proto-response](https://github.com/barkinglabs/firmware/tree/lle-proto-response))
2. Check out / fetch `web` for local dev and switch to `proto-lle-response` branch 
3. After making any proto changes in `firmware/src/protos-common`, in that directory, run `yarn build && yarn pack`
4. You should see something like: `Wrote tarball to "/Users/loren/dev/firmware/src/protos-common/barkinglabs-protos-common-v2.4.10.tgz"`
5. Take that tgz path and in the `web` folder, run `yarn add full_path_of_barkinglabs-protos-common-v2.4.10.tgz`
6. `yarn install`

You'll need to do 4&5 every time you make a proto change

**2023-05-31**
- CXD5605 gnss server request lle on bootup
- agnss server needs to be able to handle lle bytes coming in, and some meta data on the lle binary
- once the whole lle binary is received we need to kick the gnss server into inject lle state.
- gnss server, send a need LLE data, and that will be what start off the lle injection flow.

**2023-05-30**
- [Apollo](https://internaltools.corp.tryfi.com/devices/FC33A375457) Poor battery performance that may be cxd chip staying on.

**2023-05-24**
Standing up the web server locally for some experiment with sending large amount of data over wifi/ble/LTE over response data

**2023-04-27**
- [Lola](https://internaltools.corp.tryfi.com/devices/FC33B492101/battery#{%22start%22:%222023-04-24T21:39:37.573Z%22,%22end%22:%222023-04-27T21:39:37.573Z%22}) going through learning cycle
- [piper](https://internaltools.corp.tryfi.com/devices/FC33A364538/battery#{%22start%22:%222023-04-17T19:52:20.773Z%22,%22end%22:%222023-04-24T19:52:20.773Z%22}) 

**2023-04-26**
Most of information in a submission data report are current information.
Allow each backhaul to fetch info from submission data report, and send it over.
Wifi and BLE are fixed period based on timer, LTE query the brain for when to send.
Each backhaul keep track of their own connection states, and if they are the active backhaul connection, they start keep track of when it should send report and does it. An helper function can help decide which backhaul is the active backhaul and should 

Thinking through how to extract LTE+GNSS state machine out of HSM. It seems like we need to get the Modem Sever and the GNSS server make it's own decision outside of HSM.
So I am envisioning a flow for LTE+GNSS like this outside of HSM in the short/medium term:
1. HSM is in the no-connection state for x period of time
2. Taps the Modem/LTE server, "Yo modem server, you are now the Active backhaul."
3. The modem server would obediently accept the role, because it is not given a choice.
4. The modem server, start checking, "Am I actually connected? can I even register on the network"
5. If answer is yes, and it is registered, the modem server will ask its pal brain every X seconds, "can I, the modem active backhaul, send some data now?"
6. The brain would reply with either yes or no. (basing on the existing logic)
7. When the brain finally says yes to modem server, "Yes modem server, you should send a submission report now!"
8. The modem server, would go ask the submission data entity/actor, "Hey submission data, can you prepare a report for me to send over the LTE network? Ideally with the latest gnss position"
9. The submission data actor, would check and see that it does not have a new gnss position that is suitable, and reply to the modem server. "Wait ~120 seconds, I may have something for you, hold on"
- The submission data actor, goes and ask the gnss server, "hey you! gnss server give me your best position right now, I give you 120 seconds, or else don't bother. And clean up after yourself afterwards, this isn't live tracking."
- The gnss server would try it's best and get a position report.
- Later whether the gnss server have a position report or not, the submission data actor would reply to the modem server with a encoded binary blob of the current device report.
- The modem server will send it over LTE via HTTP, and get some reply data back.
- The modem server would pass the replied blob of data back to submission data actor.
- And the modem server will go back to pestering the brain when it can send a new round of report.
- If at any point in time, the HSM do get a BLE connection, or on a wifi scan it is connected. It can just go back to modem server and inform its role of active backhaul is revoked. Where then the modem server can just stop pestering brain.

It seems this flow work well for the current behaviour with live and non-live tracking device-gnss reports. In addition it opens up the possibility for gnss server to automatically periodically check (either server pushed, or via timer) if it needs LLE data. In dependent of the current HSM state. We can still handle LLE data download over LTE despite collar connected to BLE/WIFI. In the end some of the logic for gnss and modem inside HSM and module_hsm.c will get moved to both the gnss server and modem server.

In the long term we can slowly move to 3 independent comm backhauls, BLE, WIFI, and LTE/Modem. And the active backhaul role be determined via some kind of arbiter.

So a very rough implementation plan where might be:
1. a modem server that query data from submission data actor, and send data to server over LTE+HTTPS without any position reports.
2. A Gnss server, can generate one-shot position report based on current requirements in the module_hsm.c, on query from submission data actor.
3. submission data actor query gnss server for one shot positions, for modem server's report dispatch.
4. do the same thing for live tracking use case.
5. Trigger gnss server to check for LLE data requirement based on server request, or an internal timer.
1.  ...profit? or more HSM breakdown to follow?


---

Stuff I want to do:
- Use protobuf with server response param
- Preemptive LLE download over LTE, concurrent with any existing connection
- 

- Failure when sending really large packets
```
01:02:36.937 D  brain_consume_event: 0
01:02:36.939 D  fi_http_prepare_post_request: POST /api/devices/v1/module/FC32H000328/submit HTTP/1.1
Host: api.tryfi.com
Connection: close
Content-Type: text/plain
Content-Length: 14865
Authorization: Basic YmFya2luZ2xhYnM6NkJMdC9ORXZ5RQ==
Fi-Module-ID: FC32H000328


01:02:36.950 W  rlog buffer exhausted!
01:02:36.950 D  brain_consume_event: 9
01:02:36.951 D  fi_http_modem_event_handler: profile_id (0) type (4)
01:02:36.952 D  fi_http_start: 0x2001726c 712
01:02:37.268 I  nrf9160: Sleep exit: LTE_LC_MODEM_SLEEP_RF_INACTIVITY
01:02:37.269 D  Starting counter: 6, 1359, 3757
01:02:37.402 I  nrf9160: RRC status: LTE_LC_RRC_MODE_CONNECTED (1)
01:02:37.953 D  modem_nrf9160: Socket connect request for 0 succeeded
01:02:37.954 D  fi_http_request_socket_poll: 1
01:02:37.954 D  modem_nrf9160: requesting socket poll for 0
01:02:37.961 D  process_sample_store: steps=0, duration=3.000s
01:02:37.962 D  fi_motion_detection_get_state: activity threshold 0.000008 3s
01:02:38.364 D  modem_nrf9160: socket write ready for 0
01:02:38.365 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.365 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.365 D  fi_http_on_socket_write_ready
01:02:38.373 D  modem_nrf9160: write res 230
01:02:38.384 D  modem_nrf9160: write res 1024
01:02:38.385 D  fi_http_request_socket_poll: 1
01:02:38.385 D  modem_nrf9160: requesting socket poll for 0
01:02:38.395 D  modem_nrf9160: socket write ready for 0
01:02:38.396 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.396 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.397 D  fi_http_on_socket_write_ready
01:02:38.408 D  modem_nrf9160: write res 1024
01:02:38.408 D  fi_http_request_socket_poll: 1
01:02:38.408 D  modem_nrf9160: requesting socket poll for 0
01:02:38.418 D  modem_nrf9160: socket write ready for 0
01:02:38.419 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.420 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.420 D  fi_http_on_socket_write_ready
01:02:38.431 D  modem_nrf9160: write res 1024
01:02:38.431 D  fi_http_request_socket_poll: 1
01:02:38.432 D  modem_nrf9160: requesting socket poll for 0
01:02:38.441 D  modem_nrf9160: socket write ready for 0
01:02:38.443 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.443 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.443 D  fi_http_on_socket_write_ready
01:02:38.455 D  modem_nrf9160: write res 1024
01:02:38.455 D  fi_http_request_socket_poll: 1
01:02:38.455 D  modem_nrf9160: requesting socket poll for 0
01:02:38.465 D  modem_nrf9160: socket write ready for 0
01:02:38.466 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.467 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.467 D  fi_http_on_socket_write_ready
01:02:38.478 D  modem_nrf9160: write res 1024
01:02:38.478 D  fi_http_request_socket_poll: 1
01:02:38.478 D  modem_nrf9160: requesting socket poll for 0
01:02:38.488 D  modem_nrf9160: socket write ready for 0
01:02:38.489 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.490 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.490 D  fi_http_on_socket_write_ready
01:02:38.501 D  modem_nrf9160: write res 1022
01:02:38.501 D  fi_http_request_socket_poll: 1
01:02:38.501 D  modem_nrf9160: requesting socket poll for 0
01:02:38.511 D  modem_nrf9160: socket write ready for 0
01:02:38.512 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.513 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.513 D  fi_http_on_socket_write_ready
01:02:38.622 D  modem_nrf9160: write res -1
01:02:38.622 D  fi_http_request_socket_poll: 1
01:02:38.622 D  modem_nrf9160: requesting socket poll for 0
01:02:38.632 D  modem_nrf9160: socket write ready for 0
01:02:38.634 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.634 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.634 D  fi_http_on_socket_write_ready
01:02:38.645 D  modem_nrf9160: write res 1024
01:02:38.645 D  fi_http_request_socket_poll: 1
01:02:38.646 D  modem_nrf9160: requesting socket poll for 0
01:02:38.656 D  modem_nrf9160: socket write ready for 0
01:02:38.657 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.657 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.657 D  fi_http_on_socket_write_ready
01:02:38.668 D  modem_nrf9160: write res 1024
01:02:38.669 D  fi_http_request_socket_poll: 1
01:02:38.669 D  modem_nrf9160: requesting socket poll for 0
01:02:38.679 D  modem_nrf9160: socket write ready for 0
01:02:38.680 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.680 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.681 D  fi_http_on_socket_write_ready
01:02:38.691 D  modem_nrf9160: write res 306
01:02:38.692 D  fi_http_request_socket_poll: 1
01:02:38.692 D  modem_nrf9160: requesting socket poll for 0
01:02:38.702 D  modem_nrf9160: socket write ready for 0
01:02:38.703 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:38.703 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:38.704 D  fi_http_on_socket_write_ready
01:02:39.150 D  modem_nrf9160: write res -1
01:02:39.150 D  fi_http_request_socket_poll: 1
01:02:39.150 D  modem_nrf9160: requesting socket poll for 0
01:02:39.167 D  modem_nrf9160: socket write ready for 0
01:02:39.169 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:39.169 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:39.170 D  fi_http_on_socket_write_ready
01:02:39.180 D  modem_nrf9160: write res 1024
01:02:39.181 D  fi_http_request_socket_poll: 1
01:02:39.181 D  modem_nrf9160: requesting socket poll for 0
01:02:39.198 D  modem_nrf9160: socket write ready for 0
01:02:39.199 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:39.200 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:39.200 D  fi_http_on_socket_write_ready
01:02:39.227 D  modem_nrf9160: write res -1
01:02:39.227 D  fi_http_request_socket_poll: 1
01:02:39.227 D  modem_nrf9160: requesting socket poll for 0
01:02:39.237 D  modem_nrf9160: socket write ready for 0
01:02:39.246 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:39.246 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:39.246 D  fi_http_on_socket_write_ready
01:02:39.257 D  modem_nrf9160: write res 1024
01:02:39.258 D  fi_http_request_socket_poll: 1
01:02:39.258 D  modem_nrf9160: requesting socket poll for 0
01:02:39.268 D  modem_nrf9160: socket write ready for 0
01:02:39.270 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:39.270 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:39.270 D  fi_http_on_socket_write_ready
01:02:39.868 D  modem_nrf9160: write res -1
01:02:39.868 D  fi_http_request_socket_poll: 1
01:02:39.868 D  modem_nrf9160: requesting socket poll for 0
01:02:39.886 D  modem_nrf9160: socket write ready for 0
01:02:39.887 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:39.887 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:39.888 D  fi_http_on_socket_write_ready
01:02:39.898 D  modem_nrf9160: write res 1024
01:02:39.899 D  fi_http_request_socket_poll: 1
01:02:39.899 D  modem_nrf9160: requesting socket poll for 0
01:02:39.916 D  modem_nrf9160: socket write ready for 0
01:02:39.917 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:39.918 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:39.918 D  fi_http_on_socket_write_ready
01:02:39.929 D  modem_nrf9160: write res 1024
01:02:39.929 D  fi_http_request_socket_poll: 1
01:02:39.929 D  modem_nrf9160: requesting socket poll for 0
01:02:39.939 D  modem_nrf9160: socket write ready for 0
01:02:39.948 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:39.948 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:39.948 D  fi_http_on_socket_write_ready
01:02:45.465 D  modem_nrf9160: write res -1
01:02:45.465 D  fi_http_request_socket_poll: 1
01:02:45.465 D  modem_nrf9160: requesting socket poll for 0
01:02:45.471 I  nrf9160: RRC status: LTE_LC_RRC_MODE_IDLE (0)
01:02:45.475 D  fi_ble_log_state: advertising
01:02:45.477 D  is_chg: 0, has_pwr: 0, SoC: 48%
01:02:45.478 I  State 0, Chg stat: 0
01:02:45.479 I  LP5523_ENG1_INT: 1.  Shutting down LP5523.
01:02:45.479 D  Powering off LEDs
01:02:45.481 D  Stopping counter: 18, 1841, 12
01:02:45.482 I  HSM: T1: 80s T2: -1s T3: -1s State: [ lte-connection, lte:send-report ]
01:02:45.484 I  bq27421 check flags=0x0189 ctrl_status=0x208c
01:02:45.487 D  modem_nrf9160: socket write ready for 0
01:02:45.488 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:45.488 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:45.489 D  fi_http_on_socket_write_ready
01:02:45.595 D  modem_nrf9160: write res -1
01:02:45.595 D  fi_http_request_socket_poll: 1
01:02:45.595 D  modem_nrf9160: requesting socket poll for 0
01:02:45.602 I  nrf9160: RRC status: LTE_LC_RRC_MODE_CONNECTED (1)
01:02:45.614 D  modem_nrf9160: socket write ready for 0
01:02:45.615 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:45.615 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:45.616 D  fi_http_on_socket_write_ready
01:02:45.958 D  modem_nrf9160: write res -1
01:02:45.958 D  fi_http_request_socket_poll: 1
01:02:45.958 D  modem_nrf9160: requesting socket poll for 0
01:02:45.975 D  modem_nrf9160: socket write ready for 0
01:02:45.977 D  fi_http_modem_event_handler: profile_id (0) type (7)
01:02:45.977 D  MODEM_EVT_SOCKET_WRITE_READY(0)
01:02:45.977 D  fi_http_on_socket_write_ready
01:02:45.988 D  modem_nrf9160: write res 1024
01:02:45.988 D  fi_http_request_socket_poll: 1
01:02:45.988 D  modem_nrf9160: requesting socket poll for 0
01:02:45.997 E  ASSERT FAIL: "ps_ret == FI_PUBSUB_RET_SUCCESS " file "../../src/libmodem_nrf9160/fi_nrf9160_nrf52.c", line 179

01:02:45.998 W  Failed boot count now: 1
01:02:45.998 W  infinite_loop_if_halt_on_error: spinning
01:04:23.890 E  Fatal error: 16385, 0, 4 (../../src/nrf52/fi_module/main.c:272)
01:04:23.891 W  Failed boot count now: 2
01:04:23.891 W  infinite_loop_if_halt_on_error: spinning

```

2023-04-25
Y: triaging FW cx and internal testing tickets, got a working refactor LTE http module 
T: doing some testing and cleaning up before, putting refactored async lte http module up for feedback

**2023-04-24**
- [Piper](https://internaltools.corp.tryfi.com/devices/FC33A364538)'s battery is very low since 4.7.13 had run on it. [ticket](https://app.asana.com/0/1119265580120512/1204465207998899/f)
- [Kimo](FC32M552204) on the latest FW with RTC reboot storm

```
00:04:51.632 I  evaluate_transition_targets: -> '', condition 'none'
00:04:51.633 I  hsm_instance_transition: null transition
00:04:51.634 I  Added remote log: 7
00:04:53.530 D  process_sample_store: steps=0, duration=3.000s
00:04:53.530 D  fi_motion_detection_get_state: activity threshold 0.000019 3s
00:04:53.950 D  fi_ble_log_state: advertising
00:04:53.952 D  is_chg: 0, has_pwr: 0, SoC: 50%
00:04:53.954 I  State 0, Chg stat: 0
00:04:53.954 I  LP5523_ENG1_INT: 1.  Shutting down LP5523.
00:04:53.955 D  Powering off LEDs
00:04:53.957 D  Stopping counter: 18, 109, 10
00:04:53.957 I  HSM: T1: 2s T2: -1s T3: -1s State: [ lte-connection, lte:idle ]
00:04:54.953 I  bq27421 check flags=0x0189 ctrl_status=0x209c
00:04:56.622 D  process_sample_store: steps=0, duration=3.000s
00:04:56.622 D  fi_motion_detection_get_state: activity threshold 0.000010 3s
00:13:28.631 E  i2c error: 0x00008209

00:13:28.641 E  ASSERT FAIL: "ret == FI_CXD5605_BACKEND_I2C_VALIDATE_FRAME_RET_SUCCESS 1" file "../../src/libgnss_cxd5605/fi_cxd5605_backend_i2c.c", line 568

00:13:28.642 W  Failed boot count now: 1
00:13:28.642 W  infinite_loop_if_halt_on_error: spinning
00:15:05.950 E  Fatal error: 16385, 0, 4 (../../src/nrf52/fi_module/main.c:272)
00:15:05.951 W  Failed boot count now: 2
00:15:05.951 W  infinite_loop_if_halt_on_error: spinning
00:00:00.000 !  fi_module 3 build: local-fc3_f3-dev
00:00:00.000 I  Reset reasons:
```

**2023-04-21**
- Battery horror list
    - [Tootie](https://internaltools.corp.tryfi.com/devices/FC33A363169/battery#{%22start%22:%222023-04-19T13:50:49.348Z%22,%22end%22:%222023-04-20T13:50:49.348Z%22})

**2023-04-19**

- [Ruby's](https://internaltools.corp.tryfi.com/devices/FC32M561011/battery#{%22start%22:%222023-04-18T19:26:44.552Z%22,%22end%22:%222023-04-19T19:26:44.552Z%22}) collar was on old FW and did not update lle data since feb.

- frequent reboot on lte/gnss https://app.asana.com/0/1119265580120512/1204435117320978/f
- 
![[Pasted image 20230419103046.png]]

**2023-04-18**
- List of RTC Self test failure
    - FC32M552204
    - FC33A367437
    - FC32L236625
    - FC32M552052
    - FC32L247052
    - FC33A368958
    - FC32L248861
    - FC32L249631
    - FC32M555651
    - FC33A364015
    - FC33A376143
    - FC33A378239
    - FC33A378301
    - FC33B495074

**tryfi**
```
00:00:37.347 D  HTTP Parser: on_headers_complete
00:00:37.348 I  Received HTTP data: 0x2003fb0f  Status code: 301
00:00:37.348 D  :
  3C 68 74 6D 6C 3E 0D 0A 3C 68 65 61 64 3E 3C 74 | <html>..<head><t
  69 74 6C 65 3E 33 30 31 20 4D 6F 76 65 64 20 50 | itle>301 Moved P
  65 72 6D 61 6E 65 6E 74 6C 79 3C 2F 74 69 74 6C | ermanently</titl
  65 3E 3C 2F 68 65 61 64 3E 0D 0A 3C 62 6F 64 79 | e></head>..<body
  3E 0D 0A 3C 63 65 6E 74 65 72 3E 3C 68 31 3E 33 | >..<center><h1>3
  30 31 20 4D 6F 76 65 64 20 50 65 72 6D 61 6E 65 | 01 Moved Permane
  6E 74 6C 79 3C 2F 68 31 3E 3C 2F 63 65 6E 74 65 | ntly</h1></cente
  72 3E 0D 0A 3C 68 72 3E 3C                      | r>..<hr><

00:00:37.357 I  Received HTTP data: 0x2003fb08  Status code: 301
00:00:37.357 D  :
  63 65 6E 74 65 72 3E 43 6C 6F 75 64 46 72 6F 6E | center>CloudFron
  74 3C 2F 63 65 6E 74 65 72 3E 0D 0A 3C 2F 62 6F | t</center>..</bo
  64 79 3E 0D 0A 3C 2F 68 74 6D 6C 3E 0D 0A       | dy>..</html>..

00:00:37.358 I  Received HTTP data: 0x0  Status code: 301
00:00:37.358 D  :

00:00:42.915 I  nrf9160: RRC status: LTE_LC_RRC_MODE_IDLE (0)
```

**fi_auth**
```
00:00:32.664 I  Received HTTP data: 0x2003fb7a  Status code: 200
00:00:32.665 D  :
  7B 22 64 65 76 69 63 65 22 3A 7B 22 6D 6F | {"device":{"mo

00:00:32.672 I  Received HTTP data: 0x2003fb08  Status code: 200
00:00:32.672 D  :
  64 75 6C 65 49 64 22 3A 22 46 43 33 32 48 30 30 | duleId":"FC32H00
  30 33 32 38 22 7D 7D                            | 0328"}}

00:00:32.673 I  Received HTTP data: 0x0  Status code: 200
00:00:32.673 D  :
```

**2023-04-17**
- [Luna](https://internaltools.corp.tryfi.com/devices/FC32M566812/battery)  is still not recovering, might be not enough time in the lte mode

**2023-04-16**
- [Luna](https://internaltools.corp.tryfi.com/devices/FC32M566812/battery) Another collar with gnss stall issue and very poor battery, seems to stuck in gnss on state.
- We have an issue where the LLE injection after does not kick off GNSS
    - From the end of previous message upload
        - lte:shutdown-gps -> lte:boot-modem (GPS_DISABLED)
        - lte:boot-modem -> lte:send-report (LTE_NET_READY)
        - lte:send-report  -> lte:idle (REPORT_RESPONSE_ARRIVED)
        - lte:idle -> gps:run (ACTIVITY_MOVING)
        - The should_skip_agnss() check returns true, on despite GPS_NEEDS_AGNSS
        - The state machine is not moved forward, because the poke only assumes after success injection
        - In addition the gps-start check, only check if gps is powered on, not if it is positioning state
So an interesting bug came up this weekend, it was kind of interesting. Link to conversation https://tryfi.slack.com/archives/C04TU731WMT/p1681569299617469, Constance tested live tracking twice this weekend, and both times large chunk of positions was missing from the walk.
So this is a story of how multiple things came together to cause this bug. 
I recently made a change on the server side that enables GAL sat system for live tracking only, on top of existing GPS and Glonass. As an result whenever live tracking is turned on the first time that day it will trigger a GAL LLE data download. This mostly works, but if prior to turning on live tracking the collar just had downloaded LLE data within 5 minutes. (this is typical as LDM/live tracking activation from a report over LTE), the HSM will skip the agnss download.
In HSM skipping agnss download, is really not triggering the LLE data download sub state machine, it just wait in the gps:run state, until it times out. This worked fine in live tracking but does not work in the live tracking mode because the HSM does not turn on/off the CXD5605 between report cycles, hence we don't get new GPS_NEEDS_AGNSS event to trigger LLE download, and CXD5605 gnss server will just stuck in sleep state doing nothing.
Previously this failure was hidden by the CXD5605 stall timeout, where it will disable CXD5605 after not getting any message for a period of time, but this stall timeout was removed in 4.7.15 to only check for timeout during positioning state, not when CXD5605 is waiting for LLE data.
Hence now we have this perfect bug, where two seemingly safe change came together to cause the collar completely fail at live tracking.
Anyways the impact of this change is minimal, and should only have impacted the 1K external user + internal users that had 4.7.15. I have also reverted the server side feature flag that enabled GAL for live tracking, and that should avoid devices in the field getting into this state.



**2023-04-14**
- First in the field user with LLE DL failure [Berkeley](https://internaltools.corp.tryfi.com/devices/FC32M541582)
    -[ticket](https://app.asana.com/0/1119265580120512/1204402333726848/f)
    - It's updated to 4.7.15
- Placed 4.7.15 onto james-experiement, which running on 1K devices.

**2023-04-13**
- ~~pushing 4.7.14 to stable-rollout~~
- Move 1k devices from `stable-rollout` to `james-experiements`

**2023-04-12**
- push to fwup
- push to internal tester, ben's exciting tests
- ask internal tester to pay attention to battery usage, and use live tracking
- Potential build order issue?
```
FAILED: obj/src/nrf52/fi_module/fc3_f3/fi_module_dfu_settings.hex
/opt/homebrew/opt/python@3.11/bin/python3.11 ../../src/firmware-common/gntools/run_in_venv.py --venv bin/venv -- ../../build/fi_nrfutil_dfu_settings.py --nrf-chipset nrf52840 -i obj/src/nrf52/fi_module/fc3_f3/fi_module.hex -o obj/src/nrf52/fi_module/fc3_f3/fi_module_dfu_settings.hex
/Users/james/Developments/barkinglabs/other_firmware/out/rel/bin/venv/bin/python: No module named nordicsemi

[22/32] ACTION //src/nrf52/fi_module:fc3_f3__dev_signed_dfu_images(//src/firmware-common/gntools/toolchains:xcode)
FAILED: bin/fc3_f3/fi_module/dev_dfu_pkg_main.zip
/opt/homebrew/opt/python@3.11/bin/python3.11 ../../src/firmware-common/gntools/run_in_venv.py --venv bin/venv -- ../../build/fi_package_dfu.py --out-dir bin/fc3_f3/fi_module --hw-ver 11 --sd-req 0x0100 --sd-id 0x0100 --main obj/src/nrf52/fi_module/fc3_f3/fi_module.hex --key-file ../../build/dev_priv.pem
b'/Users/james/Developments/barkinglabs/other_firmware/out/rel/bin/venv/bin/python: No module named nordicsemi\n'
Traceback (most recent call last):
  File "/Users/james/Developments/barkinglabs/other_firmware/out/rel/../../build/fi_package_dfu.py", line 181, in <module>
    sys.exit(main())
             ^^^^^^
  File "/Users/james/Developments/barkinglabs/other_firmware/out/rel/../../build/fi_package_dfu.py", line 176, in main
    fi_package_dfu(*dfu_args, is_dev=True)
  File "/Users/james/Developments/barkinglabs/other_firmware/out/rel/../../build/fi_package_dfu.py", line 117, in fi_package_dfu
    _nrfutil(pkg, out_dir / f'{prefix}dfu_pkg_{"_plus_".join(components)}.zip', verbose)
  File "/Users/james/Developments/barkinglabs/other_firmware/out/rel/../../build/fi_package_dfu.py", line 66, in _nrfutil
    subprocess.run(cmd,
  File "/opt/homebrew/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/Users/james/Developments/barkinglabs/other_firmware/out/rel/bin/venv/bin/python', '-m', 'nordicsemi', 'pkg', 'generate', '--hw-version', '11', '--sd-req', '0x0100', '--key-file', '../../build/dev_priv.pem', '--application', '/Users/james/Developments/barkinglabs/other_firmware/out/rel/obj/src/nrf52/fi_module/fc3_f3/fi_module.hex', '--application-version', '0', '/Users/james/Developments/barkinglabs/other_firmware/out/rel/bin/fc3_f3/fi_module/dev_dfu_pkg_main.zip']' returned non-zero exit status 1.

```

**2023-04-11**
Y: FW roadmap planning, continue refactoring LTE http, and pushing 4.7.13 FW to 50% of S3 fleet  
T: Continue LTE HTTP refactoring and testing
- Turns out I am working on proper GNSS chip shutdown flow

```
01:14:10.476 I  module_hsm_send_event: GPS_DISABLED
01:14:10.476 I  evaluate_transition_targets: -> 'lte:boot-modem', condition 'none'
01:14:10.477 I  hsm_instance_transition: moving to state: lte:boot-modem
01:14:10.477 I  Transitioning to state: lte:boot-modem
01:14:10.478 I  Exiting state: lte:shutdown-gps
01:14:10.478 I  Entering state: lte:boot-modem
01:14:10.478 I  Running entry action: start_timer
01:14:10.478 I  Starting HSM timer -- 90000 ms
01:14:10.479 I  Running entry action: request_lte_net_ready
01:14:21.000 W  Timed out waiting for response for: 31 (id: 70)
01:14:21.000 E  ASSERT FAIL: "fi_nrf9160_modem_modemlink_send_message_sync(m, &nwreg_req, &nwreg_res) " file "../../src/libmodem_nrf9160/fi_nrf9160_modem.c", line 197

01:14:21.001 W  Failed boot count now: 1
01:14:21.001 W  System reset
01:15:47.927 E  Fatal error: 16385, 0, 4 (../../src/nrf52/fi_module/main.c:275)
01:15:47.927 W  Failed boot count now: 2
01:15:47.927 W  System reset

```

**2023-04-10**
- experimenting and testing different way to refactor lte http into pubs in model
- Continue working in lte http pubsub 

**2023-04-07**
- LTE HTTP into pubsub model

**2023-04-06**
Need to figure out the app feature that enable debug.
- It seems [Waggy](https://internaltools.corp.tryfi.com/devices/FC32L255544) have turned on LDM since March 13th. The base is offline.
- Also monitor [Phoebe's](https://internaltools.corp.tryfi.com/devices/FC32M551860) battery life, if it is still flapping with new FW.

**2023-04-05**
- Got reminded that we need to pick up the wifi scanning patch fix, and had to push the 4.7.13 patch out after I had done that to 4.7.12. Ugh...hope this does not cause any issue on the backend.
- Ahh the first lost dog event with live tracking rollout.

**2023-04-04**
- Nrf9160 scanning for network is roughly every 10 seconds on, every 10 seconds off.
- Each scanning block range from ~300uWh to ~550uWh
![[Pasted image 20230404183746.png]]

**2023-04-03**

**FC32M548501**
![[Pasted image 20230403222411.png]]
```
Time
line
Apr 3, 2023 @ 22:10:02.763
gnss s 2:3
Apr 3, 2023 @ 22:10:02.763
lle_agnss s 0:1
Apr 3, 2023 @ 22:10:02.763
gnss g 2:1 s 0
Apr 3, 2023 @ 22:10:02.763
gnss s 0:2
Apr 3, 2023 @ 22:10:02.763
gnss:2023/4/3|17:36
Apr 3, 2023 @ 22:10:02.763
lle 2023/3/20|0:0->2023/3/20|0:0 147 0
Apr 3, 2023 @ 22:10:02.763
lle_agnss s 1:2
Apr 3, 2023 @ 22:10:02.763
gnss:lle now 1680543418
Apr 3, 2023 @ 22:10:02.762
gnss:2023/4/3|17:26
Apr 3, 2023 @ 22:10:02.762
gnss s 2:3
Apr 3, 2023 @ 22:10:02.762
gnss s 3:8
Apr 3, 2023 @ 22:10:02.762
lle_agnss s 2:0
Apr 3, 2023 @ 22:10:02.762
gnss g 2:2 s 0
Apr 3, 2023 @ 22:10:02.762
lle 2023/3/20|0:0->2023/3/20|0:0 147 0
Apr 3, 2023 @ 22:10:02.762
lle_agnss s 0:1
Apr 3, 2023 @ 22:10:02.762
lle_agnss s 1:2
Apr 3, 2023 @ 22:10:02.762
gnss g 2:2 s 0
Apr 3, 2023 @ 22:10:02.762
gnss s 0:2
Apr 3, 2023 @ 22:10:02.762
gnss g 2:1 s 0
Apr 3, 2023 @ 22:10:02.762
gnss:lle now 1680542802
Apr 3, 2023 @ 22:10:02.762
CXD5605 flow timeout after 31 sec, disabling part
Apr 3, 2023 @ 22:10:02.762
gnss s 8:0
Apr 3, 2023 @ 22:10:02.761
gnss:2023/4/3|17:17
Apr 3, 2023 @ 22:10:02.761
lle 2023/3/20|0:0->2023/3/20|0:0 147 0
Apr 3, 2023 @ 22:10:02.761
lle_agnss s 1:2
```