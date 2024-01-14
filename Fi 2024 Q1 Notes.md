---
link:
  - "[[barking labs]]"
tags:
  - diary
  - work
---
```tasks
short mode
(path includes Work Journals) OR (filename includes Fi 2023) OR (filename includes Fi 2024)
not done
sort by created
```

**2024-01-12**
Y: Discussion and planning to fixing timestamping issue with sensor data collection a kennel cam, GPS failure case study meeting
T: More GPS failure case study meeting, getting a new deployment of sensor data collection at kennel cam to start fixing timestamp issues.

- [ ] Need to figure out how to update ntp on balena rpi
- [ ] something wrong with collar when time is set

Loren review 

- **Knowledgeable Leadership:**
    
    - Loren possesses extensive knowledge in various technical domains and is able to connect different eng teams together.
- **Approachable Team Collaboration:**
    
    - Loren fosters a collaborative work environment, being approachable and encouraging open discussions among team members.
- **Technical Expertise and Holistic Architecture:**
    
    - Loren combines technical expertise with a holistic view of architecture, excelling in both detailed problem-solving and strategic decision-making.

**Summary:** Loren is a highly knowledgeable and approachable leader, adept at navigating technical details while maintaining a holistic view of architecture. His collaborative approach and technical expertise have significantly contributed to our team's success.

**2024-01-11**
Y: looking into new bug on ble v2 causing data drops, and kennel cam module upload data with data gaps
T: address data gap in kennel cam setup 

- restart investigation at  2024-01-11 15:52:00.711731

**2024-01-10**
Y: Fixed the module offline bug, and investigating other serial ble v2 related tickets.
T: Cut new release for new module fix, and maybe release to internal folks, and release the base FW fix

Modules that have latest base FW:
- FC33B488392
- FC33J251635
- FC33H159390

- [x] Investigate Hal's data drop ✅ 2024-01-11
- [x] Investigate new base FW, report drop ✅ 2024-01-11

- restarted sampling at 9:46 PM host_ts 2024-01-11 02:47:11.362640

**2024-01-09**
Y: Troubleshooting a bug where module with new ble v2.1 protocol becomes offline after a while.
T: Continue troubleshooting the module offline bug

Still a tons of user running into `Unexpected submission with no deviceBasicInfoSubmission` problem, part of this issue was due to old base FW not getting rolled back.
I rolled back that. 

```
src/firmware-common/external/vendor/jlink/mac-arm64/JLinkGDBServerCLExe -device NRF52840_XXAA -speed 400 -localhostonly -if SWD
```

**2024-01-08**
Y: Cut off new 4.14.1 FW for new behavior detection feature, found issue in base FW here fw update handoff is not happening
T: Troubleshoot new base FW to understand why not getting firmware update available signal correctly.

```
00:57:52.141 I [pop_state] Exiting wifi-connected:get-conn-stats
00:57:52.141 I [pop_state] Running exi00:57:52.172 I [push_state] Entering wifi-connected:submit-report
00:57:52.173 I [push_state] start_timer2
00:57:52.173 I [_act_impl_start_timer2] Starting HSM timer2 -- 60000 ms
00:57:52.173 I [push_state] wifi_submit_report
00:57:52.173 I [fi_submission_server__set_state] IDLE -> IDLE
00:57:52.177 D [encode_proto_basicinfo] bq27421 refresh found, adding to report
00:57:52.194 D [submission_data_prepare] Prepared report body: sd
wwEKwAEKEGxvY2FsLWZjM19mMy1kZXYYAViQG2Cx9tMBaEVyLE5rdmIraVRuOW9ReENOVWVtZDREaURtZFBUcmU4OGtDUWRXSEViVGx5RzA9mgEAuAEEwAEHygEYCgkI6A8QARgIMAMSCQjoDxABGAgwAxoAkgJNEGQYyiEgWygBMP8BOP8BRQDgNkVI+QFY+AFogIABchAICQsNCwoLCwsMDRAaNMcBePgBgAH5AYgB+AGQAfgBmAFkoAFkqAGJArAB7wcCWgCMASqJAQiiAyAEMAU4gwNwBHgCgAEBiAEIkAEHsAHLC7gB6gXIAbjIAdgBlAKIAr4HoAL3RsAC+ckByAKLa9gC3J8B6AKTAfAC/AL4AtsKgAPfDKAD3QHIAwbgAwb4AwGABAGoBMUUsAT7G7gErAXABMMWyATFBdgEuQHgBNMNoAUG2AUE6AUu8AUHgAYIAmIAOzo5CglkZXNjYXJ0ZXMSETZhOmQ3OjlhOjE5OjdkOmFlGghXUEEyLVBTSyABKF0yCzE5Mi4xNjguNS42GEIWCgcKBW1hcDJ1CgsKCWRlc2NhcnRlcwJyANcIggHTCBLLCAABAAAAABCAAAgAAAAAKFeEAwIAAoAEgAAAAAAAAABAAAIAAAAAOM+BQQGAAMABQAAAAAAAAAAgAAIAAAAAtBrhIADAAGABIAAAAAAAAAAQgAAAAAAAD8GgIABwAHAAEAAAAAAAAAAIQAAAAACAxlRA2YWAQAAgAPAAEBAAAAAAAAAIgAAAAACAQFBIWABQACgACAAAAAAAAAAEIAAAAACAHyIcDAAIACAABAAAAAAAAAACEAAAAACA+g4ODAAKAAwAAgIAAAAAIAABEAAAAADAnwkIBAAFAAoAAQAAAAAAAIAACAAAAABYmoWEAAACAASAgAAAAAAAAEAAAgAAAAB4fwLCAQAAwAFAAAAAAAAAACAAAQAAAABGLgFBAIAAYAAgAAAAAAAAABCAAAAAAAD00:57:52.253 I [push_state] wifi_release_sta
00:57:52.253 D [da16200_drv_set_wake_mode] da16200_drv_set_wake_mode: shutting down
00:57:52.254 D [rlog_add] Added remote log: 7
00:00:00.020 ! [log_module_details] fi_module board=3 build=local-fc3_f3-dev platform_id=<null> module_id=FC32H000328
00:00:00.021 I [fi_cpu_log_reset_reason] fi_cpu_log_reset_reason: NONE
00:00:00.026 D [bq25180_init] bq25180 reg dump
  61 00 62 50 25 5C 03 85 1A 00 E0 01 C0 | a.bP%\.......
00:00:00.032 D [bq25180_configure] bq25180 reg dump
  61 00 00 50 25 5C 03 85 1A 00 E0 01 C0 | a..P%\.......
00:00:00.540 D [self_test_bq27421] bq27421 self-test succeeded
```

```
00:49:59.324 I [module_hsm_log_state] T1=4s T2=-1s T3=-1s State=[ ble-connection, ble:establishing ]
<debug> nrf_sdh_ble: BLE event: 0x50.
00:49:59.358 D [ble_evt_handler] BLE write: 45 len=2
<debug> nrf_sdh_ble: BLE event: 0x50.
00:49:59.598 D [ble_evt_handler] BLE write: 85 len=2
00:49:59.598 D [ble_fi_serial_svc_handle_write_event] write.ctrl notify enabled? 1
<debug> nrf_sdh_ble: BLE event: 0x12.
00:49:59.628 I [print_conn_params] min=30ms max=30ms sl=0 timeout=720ms
00:49:59.628 I [module_hsm_send_event] BLE_NEGOTIATED_PARAMS
00:49:59.629 I [evaluate_transition_targets] -> 'ble:submit-report', condition 'none'
00:49:59.629 I [hsm_instance_transition] moving to state: ble:submit-report
00:49:59.629 I [transition_to_path] ble:submit-report
00:49:59.629 I [pop_state] Exiting ble:establishing
00:49:59.630 I [pop_state] Running exit action: stop_timer
00:49:59.630 I [push_state] Entering ble:submit-report
00:49:59.630 I [push_state] ble_notify_dispatch_and_submit_report
00:49:59.631 I [fi_submission_server__set_state] IDLE -> IDLE
00:49:59.631 E [ble_fi_serial_svc_is_fully_attached] read 0; write 1
00:49:59.631 I [fi_ble_send_report] Sending periodic notify-dispatch
00:49:5<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x50.
00:49:59.830 D [ble_evt_handler] BLE write: 88 len=2
00:49:59.831 D [ble_fi_serial_svc_handle_write_event] read.ctrl notify enabled? 1
<debug> nrf_sdh_ble: BLE event: 0x50.
00:50:00.010 D [ble_evt_handler] BLE write: 80 len=2
<debug> nrf_sdh_ble: BLE event: 0x50.
00:50:00.251 D [ble_fi_svc_handle_write_event] Received NOTIFY ACK: 4 bytes
00:50:00.251 D [ble_evt_handler] BLE write: 36 len=4
<debug> nrf_sdh_ble: BLE event: 0x50.
00:50:00.430 D [ble_evt_handler] BLE write: 62 len=2
<debug> nrf_sdh_ble: BLE event: 0x51.
00:50:09.322 D [fi_ble_log_state] BLE is attached
00:50:09.324 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
00:50:09.324 I [module_hsm_log_state] T1=50s T2=-1s T3=-1s State=[ ble-connection, ble:submit-report ]
00:50:09.345 D [fi_step_count_actor__store_record] seq=49 accel_mag_var=0.000 steps=0
00:50:17.884 I [bq27421_refresh_state_enter] start refresh
00:50:19.322 D [fi_ble_log_state] BLE is attached
00:50:19.324 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
00:50:19.324 I [module_hsm_log_state] T1=40s T2=-1s T3=-1s State=[ ble-connection, ble:submit-report ]
00:50:29.322 D [fi_ble_log_state] BLE is attached
00:50:29.324 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
00:50:29.324 I [module_hsm_log_state] T1=30s T2=-1s T3=-1s State=[ ble-connection, ble:submit-report ]
```

```
01:26:12.384 D [submission_data_prepare] Prepared report body: sd
hgEKgwEKEGxvY2FsLWZjM19mMy1kZXYYAVi0KGCV2bsCaEVyLE9SWWhySUNuaFNnYkw3Ym9aM0IrNUQ3eVhSYmUxTmUyYzJ0eWVRMkFnTlk9mgEAsgEQCBkQGSDwLij3ATD7ATj7AbgBBMABB8oBGAoJCOgPEAEYCTADEgkI6A8QARgJMAMaAAJaAG8qbQgDgAEBiAEHkAEDsAGbItgBrQWIAmSgAtY7wAKVpwLIArh92ALD6QHoAjXwAvwH+AKfA4ADpAWgA2/AAwHIAwLgAwL4AwKABAKoBLcVsAS0G7gEyQXABMMhyAAAAEIAACAAAAANIrIUEAIABAASAgAAAAAAACEAABAAAAAPaMcFAAEACQABAQAAAAAAABCIAAAAAAgLhFQBgAEABoAAgIQAAAAIAABGAAAAAAgBAeHFAAWABwAAQEAAAAAEAAAiAAAAAA4GwQEAgADAAQAAICAAAAAAAAAQgAAAAAwCoICAcABQAIAAEBAAAAAACAAAgAAAAAoCwEBACAAwAFgIAAAAAAAAiAAAYAAAAABAJEQwbABAADQEAAAAA<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x50.
01:26:13.741 D [ble_evt_handler] BLE write: 87 len=8
01:26:13.741 D [handle_serial_svc_read_endpoint_changed] Got read ctrl ACK: ID=1 len=1118
01:26:13.742 I [fi_ble_handle_server_endpoint] Send submission data(244).
01:26:13.743 I [fi_ble_handle_server_endpoint] Send submission data(244).
01:26:13.754 I [fi_ble_handle_server_endpoint] Send submission data(244).
<debug> nrf_sdh_ble: BLE event: 0x57.
01:26:13.841 I [fi_ble_handle_server_endpoint] Send submission data(244).
<debug> nrf_sdh_ble: BLE event: 0x57.
01:26:13.917 I [fi_ble_handle_server_endpoint] Send submission data(142).
<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x50.
01:26:14.242 D [ble_evt_handler] BLE write: 84 len=8
01:26:14.242 D [handle_serial_svc_endpoint_changed] Write endpoint changed 1 1 45
<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x50.
01:26:14.342 D [ble_evt_handler] BLE write: 82 len=45
01:26:14.342 I [handle_serial_svc_recv_data] Got data at 1, len 45
01:26:14.342 D [handle_serial_svc_recv_data] Got submission response chunk 45. 0 remaining. 0 current transaction
01:26:14.343 I [fi_submission_server__set_state] IDLE -> RECV_RESP
01:26:14.344 I [rlog_erase_before] Clearing remote logs before: 48
01:26:14.344 I [fi_submission_server__process_basic_response] update_report_interval: 300s
01:26:14.344 I [fi_submission_server__process_basic_response] update_no_activity_interval: 300s
01:26:14.345 I [fi_submission_server__process_basic_response] Updating led state to: 0 s
01:26:14.345 I [set_led_pattern] Disabling LED
01:26:14.345 I [fi_submission_server__process_basic_response] Updating led off after duration to: 0 s
01:26:14.345 I [fi_submission_server__process_basic_resp REPORT_RESPONSE_EXTEND
01:26:14.355 I [evaluate_transition_targets] -> '', condition 'none'
01:26:14.355 I [hsm_instance_transition] null transition
01:26:14.355 I [run_transition_actions] start_tim I [pop_state] Exiting ble:submit-report
01:26:14.366 I [pop_state] Running exit action: stop_timer
01:26:14.367 I [push_state] Entering ble:idle
01:26:14.367 I [push_state] start_timer I [bq27421_refresh_state_enter] start refresh
01:26:18.454 D [fi_ble_log_state] BLE is attached
01:26:18.454 E [fi_ble_log_state] errcnt: 29, s_hvx_count: 0
01:26:18.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:26:18.457 I [module_hsm_log_state] T1=44s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:26:28.454 D [fi_ble_log_state] BLE is attached
01:26:28.454 E [fi_ble_log_state] errcnt: 29, s_hvx_count: 0
01:26:28.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:26:28.457 I [module_hsm_log_state] T1=34s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:26:33.813 I [bq27421_print_cached_values]   Design Parameters: capacity=265mAh energy=1007mWh
  Device Type: 0x0421
  Chem ID: 0x0312
  Control_Status 1: rsvd_1=0 vok=0 rup_dis=0 ldmd=1 sleep=1 rsvd_2=0 hibernate=0 initcomp=1
  Control Status 2: res_up=0 qmax_up=0 bca=0 cca=0 calmode=0 ss=0 wdreset=0 shutdownen=0
  Flags 1: dsg=0 socf=0 soc1=0 bat_det=1 cfgupmode=0 itpor=0 rsvd_1=0 ocvtaken=1
  Flags 2: chg=0 fc=0 rsvd_2=0 ut=0 ot=0
  Voltage: 4298mV
  Average Current: 0mAh
  Average Power: 0mWh
  State of Charge: 100%
  State of Health: 92% (status 1)
  Temperature: 2928
  Remaining Capacity:  250mAh
  Full-Charge Capacity: 249mAh
  Nominal Available Capacity: 256mAh
  Remaining Capacity: unfiltered=249mAh filtered=250mAh
  Full-Charge Capacity: unfiltered=249mAh filtered=249mAh
  State of Charge (unfiltered): 100%
  Learning: Qmax=16384 Ra=[8 9 11 13 11 10 11 11 11 12 13 16 26 52 199]
01:26:33.815 I [bq27421_refresh_state_update] Refresh success, next in 60000ms
01:26:38.454 D [fi_ble_log_state] BLE is attached
01:26:38.454 E [fi_ble_log_state] errcnt: 29, s_hvx_count: 0
01:26:38.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:26:38.457 I [module_hsm_log_state] T1=24s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:26:48.454 D [fi_ble_log_state] BLE is attached
01:26:48.454 E [fi_ble_log_state] errcnt: 29, s_hvx_count: 0
01:26:48.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:26:48.457 I [module_hsm_log_state] T1=14s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:26:58.454 D [fi_ble_log_state] BLE is attached
01:26:58.454 E [fi_ble_log_state] errcnt: 29, s_hvx_count: 0
01:26:58.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:26:58.457 I [module_hsm_log_state] T1=4s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:27:03.368 I [module_hsm_send_event] TIMER
01:27:03.368 I [evaluate_transition_targets] -> 'ble:submit-report', condition 'none'
01:27:03.368 I [hsm_instance_transition] moving to state: ble:submit-report
01:27:03.369 I [transition_to_path] ble:submit-report
01:27:03.369 I [pop_state] Exiting ble:idle
01:27:03.369 I [pop_state] Running exit action: stop_timer
01:27:03.369 I [push_state] Entering ble:submit-report
01:27:03.370 I [push_state] ble_notify_dispatch_and_submit_report
01:27:03.370 I [fi_submission_server__set_state] IDLE -> IDLE
01:27:03.370 E [ble_fi_serial_svc_is_fully_attached] read 1; write 1
01:27:03.374 D [encode_proto_basicinfo] bq27421 refresh found, adding to report
01:27:03.386 D [submission_data_prepare] Prepared report body: sd
1gEK0wEKEGxvY2FsLWZjM19mMy1kZXYYAVjnKGDO574CaEVyLE9SWWhySUNuaFNnYkw3Ym9aM0IrNUQ3eVhSYmUxTmUyYzJ0eWVRMkFnTlk9mgEAsgEQCBkQGSDwLij3ATD7ATj7AbgBBMABB8oBGAoJCOgPEAEYCTADEgkI6A8QARgJMAMaAJICTRBkGMohIFwoATCAAjiAAkUAADdFSPoBWPkBaICAAXIQCAkLDQsKCwsLDA0QGjTHAXj5AYAB+gGIAfkBkAH5AZgBZKABZKgBiQKwAe8HAloAbyptCAOAAQGIAQeQAQOwAc4i2AGtABEAAAAAAgKwrKAwABAAYAAQEAAAAAEAABCAAAAAAYBAYEBgAGAAWAAIAAAAAAAAAAQgAAAAA8BkLBwYAAQAMAAEBAAAAABCAAAgAAAAA+G4GBQKAA4AGgIAAAAAAAAhAAAQAAAAANEFCwgKAAYABQEAAAAAAAAQgAAIAAAAAhIAhgQHgAYAAICAAAAAAAAIgAAIAAAAAQqCQMAFgATABEBAAAAAAAAEIgAAAAAAA3U04KABAAGgACAgAAAAAgAA<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x50.
01:27:04.718 D [ble_evt_handler] BLE write: 87 len=8
01:27:04.718 D [handle_serial_svc_read_endpoint_changed] Got read ctrl ACK: ID=1 len=1166
01:27:04.718 I [fi_ble_handle_server_endpoint] Send submission data(244).
01:27:04.719 I [fi_ble_handle_server_endpoint] Send submission data(244).
01:27:04.730 I [fi_ble_handle_server_endpoint] Send submission data(244).
<debug> nrf_sdh_ble: BLE event: 0x57.
01:27:04.817 I [fi_ble_handle_server_endpoint] Send submission data(244).
<debug> nrf_sdh_ble: BLE event: 0x57.
01:27:04.844 I [fi_ble_handle_server_endpoint] Send submission data(190).
<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x50.
01:27:06.367 D [ble_evt_handler] BLE write: 84 len=8
01:27:06.367 D [handle_serial_svc_endpoint_changed] Write endpoint changed 1 1 45
<debug> nrf_sdh_ble: BLE event: 0x57.
<debug> nrf_sdh_ble: BLE event: 0x50.
01:27:06.468 D [ble_evt_handler] BLE write: 82 len=45
01:27:06.468 I [handle_serial_svc_recv_data] Got data at 1, len 45
01:27:06.468 D [handle_serial_svc_recv_data] Got submission response chunk 45. 0 remaining. 0 current transaction
01:27:06.469 I [fi_submission_server__set_state] IDLE -> RECV_RESP
01:27:06.469 I [rlog_erase_before] Clearing remote logs before: 48
01:27:06.470 I [fi_submission_server__process_basic_response] update_report_interval: 300s
01:27:06.470 I [fi_submission_server__process_basic_response] update_no_activity_interval: 300s
01:27:06.470 I [fi_submission_server__process_basic_response] Updating led state to: 0 s
01:27:06.471 I [set_led_pattern] Disabling LED
01:27:06.471 I [fi_submission_server__process_basic_response] Updating led off after duration to: 0 s
01:27:06.471 I [fi_submission_server__process_basic_respORT_RESPONSE_EXTEND
01:27:06.481 I [evaluate_transition_targets] -> '', condition 'none'
01:27:06.481 I [hsm_instance_transition] null transition
01:27:06.481 I [run_transition_actions] start_timerp_state] Exiting ble:submit-report
01:27:06.492 I [pop_state] Running exit action: stop_timer
01:27:06.492 I [push_state] Entering ble:idle
01:27:06.493 I [push_state] start_timer
01:27:001:27:08.454 D [fi_ble_log_state] BLE is attached
01:27:08.454 E [fi_ble_log_state] errcnt: 33, s_hvx_count: 0
01:27:08.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:27:08.457 I [utc_wallclock_sync] Syncing UTC clock
01:27:08.465 I [module_hsm_log_state] T1=47s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:27:08.466 D [fi_step_count_actor__store_record] seq=86 accel_mag_var=0.000 steps=0
01:27:18.454 D [fi_ble_log_state] BLE is attached
01:27:18.454 E [fi_ble_log_state] errcnt: 33, s_hvx_count: 0
01:27:18.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:27:18.457 I [module_hsm_log_state] T1=37s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:27:28.454 D [fi_ble_log_state] BLE is attached
01:27:28.454 E [fi_ble_log_state] errcnt: 33, s_hvx_count: 0
01:27:28.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:27:28.457 I [module_hsm_log_state] T1=27s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:27:33.815 I [bq27421_refresh_state_enter] start refresh
01:27:38.454 D [fi_ble_log_state] BLE is attached
01:27:38.454 E [fi_ble_log_state] errcnt: 33, s_hvx_count: 0
01:27:38.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:27:38.457 I [module_hsm_log_state] T1=17s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:27:48.454 D [fi_ble_log_state] BLE is attached
01:27:48.454 E [fi_ble_log_state] errcnt: 33, s_hvx_count: 0
01:27:48.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:27:48.457 I [module_hsm_log_state] T1=7s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:27:50.948 I [bq27421_print_cached_values]   Design Parameters: capacity=265mAh energy=1007mWh
  Device Type: 0x0421
  Chem ID: 0x0312
  Control_Status 1: rsvd_1=0 vok=0 rup_dis=0 ldmd=1 sleep=1 rsvd_2=0 hibernate=0 initcomp=1
  Control Status 2: res_up=0 qmax_up=0 bca=0 cca=0 calmode=0 ss=0 wdreset=0 shutdownen=0
  Flags 1: dsg=0 socf=0 soc1=0 bat_det=1 cfgupmode=0 itpor=0 rsvd_1=0 ocvtaken=1
  Flags 2: chg=0 fc=0 rsvd_2=0 ut=0 ot=0
  Voltage: 4298mV
  Average Current: 0mAh
  Average Power: 0mWh
  State of Charge: 100%
  State of Health: 92% (status 1)
  Temperature: 2927
  Remaining Capacity:  250mAh
  Full-Charge Capacity: 249mAh
  Nominal Available Capacity: 256mAh
  Remaining Capacity: unfiltered=249mAh filtered=250mAh
  Full-Charge Capacity: unfiltered=249mAh filtered=249mAh
  State of Charge (unfiltered): 100%
  Learning: Qmax=16384 Ra=[8 9 11 13 11 10 11 11 11 12 13 16 26 52 199]
01:27:50.951 I [bq27421_refresh_state_update] Refresh success, next in 60000ms
01:27:55.494 I [module_hsm_send_event] TIMER
01:27:55.494 I [evaluate_transition_targets] -> 'ble:submit-report', condition 'none'
01:27:55.494 I [hsm_instance_transition] moving to state: ble:submit-report
01:27:55.495 I [transition_to_path] ble:submit-report
01:27:55.495 I [pop_state] Exiting ble:idle
01:27:55.495 I [pop_state] Running exit action: stop_timer
01:27:55.495 I [push_state] Entering ble:submit-report
01:27:55.496 I [push_state] ble_notify_dispatch_and_submit_report
01:27:55.496 I [fi_submission_server__set_state] IDLE -> IDLE
01:27:55.496 E [ble_fi_serial_svc_is_fully_attached] read 1; write 1
01:27:55.500 D [encode_proto_basicinfo] bq27421 refresh found, adding to report
01:27:55.512 D [submission_data_prepare] Prepared report body: sd
1gEK0wEKEGxvY2FsLWZjM19mMy1kZXYYAVibKWDs/sECaEVyLE9SWWhySUNuaFNnYkw3Ym9aM0IrNUQ3eVhSYmUxTmUyYzJ0eWVRMkFnTlk9mgEAsgEQCBkQGSDwLij3ATD7ATj7AbgBBMABB8oBGAoJCOgPEAEYCTADEgkI6A8QARgJMAMaAJICTRBkGMohIFwoATCAAjiAAkUA8DZFSPoBWPkBaICAAXIQCAkLDQsKCwsLDA0QGjTHAXj5AYAB+gGIAfkBkAH5AZgBZKABZKgBiQKwAe8HAloAbyptCAOAAQGIAQeQAQOwAYIj2AGtAAAAAACEAAAAAAgOdCQCAAKABIAAgIAAAAAAAABEAAAAAAQAInIAQADAAoAAQEAAAAAEAAAiAAAAAAAFsVEA4ABAAMAAIAAAAAAAAAARAAAAAAUAsICAEACAAIAAEBAAAAAACAAAgAAAAAGCgFhAIAAYAFgIAAAAAAAAhAAAIAAAAAaIsCggEAAcACQAAAAAAAAAAgAAEAAAAAFjAhIQBAAEAAIAAAAAAAAAAQgAAAAAAA1peAQABwAGAAEBAAAA55.529 D [rlog_add] Added remote log: 7
<debug> nrf_sdh_ble: BLE event: 0x57.
01:28:08.096 I [utc_wallclock_sync] Syncing UTC clock
01:28:08.454 D [fi_ble_log_state] BLE is attached
01:28:08.454 E [fi_ble_log_state] errcnt: 34, s_hvx_count: 0
01:28:08.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:28:08.457 I [module_hsm_log_state] T1=47s T2=-1s T3=-1s State=[ ble-connection, ble:submit-report ]
01:28:08.466 D [fi_step_count_actor__store_record] seq=87 accel_mag_var=0.000 steps=0
<debug> nrf_sdh_ble: BLE event: 0x11.
01:28:10.018 I [ble_evt_handler] disconnected
01:28:10.019 I [on_adv_evt] Fast advertising.
01:28:10.019 I [module_hsm_send_event] BLE_DISCONNECT
01:28:10.019 I [evaluate_transition_targets] -> 'no-connection', condition 'none'
01:28:10.020 I [hsm_instance_transition] moving to state: no-connection
01:28:10.020 I [transition_to_path] no-connection
01:28:10.020 I [pop_state] Exiting ble:submit-report
01:28:10.020 I [pop_state] Running exit action: stop_timer
01:28:10.021 I [pop_state] Exiting ble-connection
01:28:10.021 I [pop_state] Running exit action: ble_stop
01:28:10.021 D [brain_consume_event] 4
01:28:10.021 I [run_transition_actions] report_disconnected_from_stable
0rlog_add] Added remote log: 7
<debug> nrf_sdh_ble: BLE event: 0x10.
01:28:12.238 I [ble_evt_handler] connected
01:28:12.238 D [ble_evt_handler] reconnect_count=1 longest_disconnect=2220ms
01:28:12.238 I [print_conn_params] min=25ms max=25ms sl=0 timeout=6000ms
01:28:12.239 I [module_hsm_send_event] BLE_NEGOTIATED_PARAMS
01:28:12.239 W [hsm_instance_transition] state='no-connection', Unexpected event 'BLE_NEGOTIATED_PARAMS'
01:28:12.240 D [rlog_add] Added remote log: 7
<debug> nrf_ble_gatt: Requesting to update ATT MTU to 247 bytes on connection 0x0.
<debug> nrf_ble_gatt: Updating data length to 251 on connection 0x0.
01:28:12.250 D [execute_evt_callback] BLE connected! peer=2a:af:03:a8:91:10 addr_id_peer=0 addr_type=0
<debug> nrf_sdh_ble: BLE event: 0x24.
01:28:12.318 I [ble_evt_handler] DLE update tx=251B rx=251B tx_time=2120us rx_time=2120us
<debug> nrf_ble_gatt: Data length updated to 251 on connection 0x0.
<debug> nrf_ble_gatt: max_rx_octets: 251
<debug> nrf_ble_gatt: max_tx_octets: 251
<debug> nrf_ble_gatt: max_rx_time: 2120
<debug> nrf_ble_gatt: max_tx_time: 2120
<debug> nrf_sdh_ble: BLE event: 0x3A.
01:28:12.368 I [ble_evt_handler] MTU exchange response 247 bytes
<debug> nrf_ble_gatt: ATT MTU updated to 247 bytes on connection 0x0 (response).
01:28:12.368 I [gatt_evt_handler] GATT ATT MTU on connection 0x0 changed to 247.
<debug> nrf_sdh_ble: BLE event: 0x55.
<debug> nrf_ble_gatt: Peer on connection 0x0 requested an ATT MTU of 500 bytes.
<debug> nrf_ble_gatt: Updating ATT MTU to 247 bytes (desired: 247) on connection 0x0.
01:28:14.593 I [gatt_evt_handler] GATT ATT MTU on connection 0x0 changed to 247.
<debug> nrf_sdh_ble: BLE event: 0x50.
01:28:14.643 D [ble_evt_handler] BLE write: 13 len=2
<debug> nrf_sdh_ble: BLE event: 0x50.
01:28:14.818 D [ble_evt_handler] BLE write: 34 len=2
<debug> nrf_sdh_ble: BLE event: 0x50.
01:28:14.868 D [ble_fi_svc_handle_write_event] Received CTRL POINT cmd: 1
01:28:14.868 I [fi_ble_attach] central issued attach
01:28:14.869 D [rlog_add] Added remote log: 12
01:28:14.869 D [ble_evt_handler] BLE write: 40 len=1
01:28:14.881 I [module_hsm_send_event] BLE_CONNECT
01:28:14.881 I [evaluate_transition_targets] -> 'ble-connection', condition 'none'
01:28:14.881 I [hsm_instance_transition] moving to state: ble-connection
01:28:14.881 I [transition_to_path] ble-connection
01:28:14.882 I [pop_state] Exiting no-connection
01:28:14.882 I [pop_state] Running exit action: stop_timer
01:28:14.882 I [push_state] Entering ble-connection
01:28:14.882 I [push_state] ble_start
01:28:14.883 D [brain_consume_event] 3
01:28:14.883 I [push_state] lte_stop
01:28:14.908 D [brain_consume_event] 6
01:28:14.908 I [transition_to_path] Entering sub-machine: ble-connection
01:28:14.908 I [transition_to_path] ble:establishing
01:28:14.909 I [push_state] Entering ble:establishing
01:28:14.909 I [push_state] start_timer
01:28:14.909 I [_act_impl_start_timer] Starting HSM timer -- 5000 ms
01:28:14.910 D [rlog_add] Added remote log: 7
01:28:14.910 I [module_hsm_send_event] LTE_MODEM_SLEEP
01:28:14.911 W [hsm_instance_transition] state='ble:establishing', Unexpected event 'LTE_MODEM_SLEEP'
01:28:14.911 D [rlog_add] Added remote log: 7
<debug> nrf_sdh_ble: BLE event: 0x50.
01:28:15.068 D [ble_evt_handler] BLE write: 80 len=2
<debug> nrf_sdh_ble: BLE event: 0x50.
01:28:15.168 D [ble_evt_handler] BLE write: 85 len=2
01:28:15.168 D [ble_fi_serial_svc_handle_write_event] write.ctrl notify enabled? 1
<debug> nrf_sdh_ble: BLE event: 0x50.
01:28:15.268 D [ble_evt_handler] BLE write: 88 len=2
01:28:15.268 D [ble_fi_serial_svc_handle_write_event] read.ctrl notify enabled? 1
<debug> nrf_sdh_ble: BLE event: 0x50.
01:28:17.018 D [ble_evt_handler] BLE write: 62 len=2
01:28:18.454 D [fi_ble_log_state] BLE is attached
01:28:18.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:28:18.456 I [module_hsm_log_state] T1=1s T2=-1s T3=-1s State=[ ble-connection, ble:establishing ]
01:28:19.909 I [module_hsm_send_event] TIMER
01:28:19.909 I [evaluate_transition_targets] -> 'ble:idle', condition 'none'
01:28:19.910 I [hsm_instance_transition] moving to state: ble:idle
01:28:19.910 I [transition_to_path] ble:idle
01:28:19.910 I [pop_state] Exiting ble:establishing
01:28:19.910 I [pop_state] Running exit action: stop_timer
01:28:19.910 I [push_state] Entering ble:idle
01:28:19.911 I [push_state] start_timer
01:28:19.911 I [_act_impl_start_timer] Starting HSM timer -- 49000 ms
01:28:19.911 I [push_state] check_gps_is_on
01:28:19.912 D [rlog_add] Added remote log: 7
01:28:28.454 D [fi_ble_log_state] BLE is attached
01:28:28.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:28:28.456 I [module_hsm_log_state] T1=40s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:28:38.454 D [fi_ble_log_state] BLE is attached
01:28:38.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:28:38.456 I [module_hsm_log_state] T1=30s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:28:48.454 D [fi_ble_log_state] BLE is attached
01:28:48.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:28:48.456 I [module_hsm_log_state] T1=20s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:28:50.950 I [bq27421_refresh_state_enter] start refresh
01:28:58.454 D [fi_ble_log_state] BLE is attached
01:28:58.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:28:58.456 I [module_hsm_log_state] T1=10s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:29:08.082 I [utc_wallclock_sync] Syncing UTC clock
01:29:08.091 I [bq27421_print_cached_values]   Design Parameters: capacity=265mAh energy=1007mWh
  Device Type: 0x0421
  Chem ID: 0x0312
  Control_Status 1: rsvd_1=0 vok=0 rup_dis=0 ldmd=1 sleep=1 rsvd_2=0 hibernate=0 initcomp=1
  Control Status 2: res_up=0 qmax_up=0 bca=0 cca=0 calmode=0 ss=0 wdreset=0 shutdownen=0
  Flags 1: dsg=0 socf=0 soc1=0 bat_det=1 cfgupmode=0 itpor=0 rsvd_1=0 ocvtaken=1
  Flags 2: chg=0 fc=0 rsvd_2=0 ut=0 ot=0
  Voltage: 4298mV
  Average Current: 0mAh
  Average Power: 0mWh
  State of Charge: 100%
  State of Health: 92% (status 1)
  Temperature: 2927
  Remaining Capacity:  250mAh
  Full-Charge Capacity: 249mAh
  Nominal Available Capacity: 256mAh
  Remaining Capacity: unfiltered=249mAh filtered=250mAh
  Full-Charge Capacity: unfiltered=249mAh filtered=249mAh
  State of Charge (unfiltered): 100%
  Learning: Qmax=16384 Ra=[8 9 11 13 11 10 11 11 11 12 13 16 26 52 199]
01:29:08.094 I [bq27421_refresh_sta01:29:08.454 D [fi_ble_log_state] BLE is attached
01:29:08.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:29:08.456 I [module_hsm_log_state] T1=0s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:29:08.466 D [fi_step_count_actor__store_record] seq=88 accel_mag_var=0.000 steps=0
01:29:08.911 I [module_hsm_send_event] TIMER
01:29:08.911 I [evaluate_transition_targets] -> 'ble:submit-report', condition 'none'
01:29:08.911 I [hsm_instance_transition] moving to state: ble:submit-report
01:29:08.912 I [transition_to_path] ble:submit-report
01:29:08.912 I [pop_state] Exiting ble:idle
01:29:08.912 I [pop_state] Running exit action: stop_timer
01:29:08.912 I [push_state] Entering ble:submit-report
01:29:08.913 I [push_state] ble_notify_dispatch_and_submit_report
01:29:08.913 I [fi_submission_server__set_state] IDLE -> IDLE
01:29:08.913 E [ble_fi_serial_svc_is_fully_attached] read 1; write 1
01:29:08.917 D [encode_proto_basicinfo] bq27421 refresh found, adding to report
01:29:08.931 D [submission_data_prepare] Prepared report body: sd
2wEK2AEKEGxvY2FsLWZjM19mMy1kZXYYAVjkKWC1vMYCaEVyLE9SWWhySUNuaFNnYkw3Ym9aM0IrNUQ3eVhSYmUxTmUyYzJ0eWVRMkFnTlk9mgEAsgEVCBkQGSDwLij3ATD7ATj7AUgBUKwRuAEEwAEHygEYCgkI6A8QARgJMAMSCQjoDxABGAkwAxoAkgJNEGQYyiEgXCgBMIACOIACRQDwNkVI+gFY+QFogIABchAICQsNCwoLCwsMDRAaNMcBePkBgAH6AYgB+QGQAfkBmAFkoAFkqAGJArAB7wcCWgBwKm4IA4ABAYgBB5ABBLABCDQoLCglkZXNjYXJ0ZXOpBYIBpQUSnQUAAQAAAAAAgAAIAAAAABACBgUHAAiAAoCAAAAAAAAIgAAEAAAAAAiUAsICgANAAkAAAAAAAAAAIAACAAAAANot4SAAYACgACAgAAAAAAAAEAABAAAAAHCNgBAAQABgABAQAAAAAAABCIAAAAAAAGVWQBAAMAAwAAgIAAAAAIAABEAAAAAAwEcnIBgAGAAgAAQEAAAAAEAAAiAAAAAAgHwUFAQACgAMAAI229586,0,58880,36c74e60
a4
5289586,0,58880,36d0a991
mlog
Dwjp574COggIDRASGAUgAQ8I8/++AjoICBIQEhgRIAEPCP//vgI6CAgSEA0YDyABDwiI/8ECOggIDRASGAUgAQ8IqfDCAjoICBIQBhgHIAENCM+BwwI6BggGEAYYCCAIlJbDAmIZChVjZW50cmFsIGlzc3VlZCBhdHRhY2gQAQ8IvZbDAjoICAYQCxgCIAENCL+WwwI01:29:18.454 D [fi_ble_log_state] BLE is attached
01:29:18.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:29:18.456 I [module_hsm_log_state] T1=50s T2=-1s T3=-1s State=[ ble-connection, ble:submit-report ]
01:29:28.454 D [fi_ble_log_state] BLE is attached
01:29:28.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:29:28.456 I [module_hsm_log_state] T1=40s T2=-1s T3=-1s State=[ ble-connection, ble:submit-report ]
01:29:38.454 D [fi_ble_log_state] BLE is attached
01:29:38.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:29:38.456 I [module_hsm_log_state] T1=30s T2=-1s T3=-1s State=[ ble-connection, ble:submit-report ]
01:29:48.454 D [fi_ble_log_state] BLE is attached
01:29:48.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:29:48.456 I [module_hsm_log_state] T1=20s T2=-1s T3=-1s State=[ ble-connection, ble:submit-report ]
01:29:58.454 D [fi_ble_log_state] BLE is attached
01:29:58.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:29:58.456 I [module_hsm_log_state] T1=10s T2=-1s T3=-1s State=[ ble-connection, ble:submit-report ]
01:30:08.094 I [utc_wallclock_sync] Syncing UTC clock
01:30:08.103 I [bq27421_refresh_state_enter] start refresh
01:30:08.454 D [fi_ble_log_state] BLE is attached
01:30:08.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:30:08.456 I [module_hsm_log_state] T1=0s T2=-1s T3=-1s State=[ ble-connection, ble:submit-report ]
01:30:08.466 D [fi_step_count_actor__store_record] seq=89 accel_mag_var=0.000 steps=0
01:30:08.951 I [module_hsm_send_event] TIMER
01:30:08.951 I [evaluate_transition_targets] -> 'ble:idle', condition 'none'
01:30:08.951 I [hsm_instance_transition] moving to state: ble:idle
01:30:08.952 I [transition_to_path] ble:idle
01:30:08.952 I [pop_state] Exiting ble:submit-report
01:30:08.952 I [pop_state] Running exit action: stop_timer
01:30:08.952 I [run_transition_actions] submission_server_timeout
01:30:08.953 I [fi_submission_server__set_state] IDLE -> COMPLETE
01:30:08.953 I [push_state] Entering ble:idle
01:30:08.953 I [push_state] start_timer
01:30:08.953 I [_act_impl_start_timer] Starting HSM timer -- 49000 ms
01:30:08.954 I [push_state] check_gps_is_on
01:30:08.955 D [rlog_add] Added remote log: 7
01:30:08.955 I [fi_submission_server__set_state] COMPLETE -> IDLE
01:30:18.454 D [fi_ble_log_state] BLE is attached
01:30:18.456 I [power_check_battery_charger] Battery: state 2, bq25180_stat0:0x61, is_chg:0 has_pwr:1
01:30:18.456 I [module_hsm_log_state] T1=39s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
01:30:25.236 I [bq27421_print_cached_values]   Design Parameters: capacity=265mAh energy=1007mWh
  Device Type: 0x0421
  Chem ID: 0x0312
  Control_Status 1: rsvd_1=0 vok=0 rup_dis=0 ldmd=1 sleep=1 rsvd_2=0 hibernate=0 initcomp=1
```

**2024-01-05**
Y: work on module version manifests, pushed latest base fw to Fi internal users
T: analyze base releases data, cut new ble v2.1 module fw to new behavior detection feature

- [ ] Update LLE Throttle to 100%?
- [x] Fix fwup via base handoff not happening ✅ 2024-01-08

**2024-01-04**
Y: Figure out the issue the with my base dev kit due to wall power issue.
T: Release base FW to internal fi users, and cut new module FW release for BLE v2.1

**2024-01-03**
Y: caught up on kennel cam next step work, and testing new BLE v2.1 FW and new base FW
T: continue testing the new base FW and get it ready for internal release to fi folks

```
select
*
from
main.fi_kennelcam.sensor_collect
where
feed_name = 'billowing-rain'
and host_ts > '2024-01-02 13:55:00.0' and host_ts < '2024-01-03 14:55:00.0'
and module_id = 'FC32H000328'
order by
mod_ts
```

- Discussion on GPS location debugging.

**2024-01-02**
Y: OOO
T: Catch up with Ben's BLE works over the break, and start up on firmware version manifest work for bootloader firmware update in the field.

Start sensor at 3pm
