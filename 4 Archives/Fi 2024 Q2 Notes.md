---
id: 20240401Mon092251
aliases:
  - Fi 2024 Q2 Notes
tags: 
link:
---
```tasks
short mode
(path includes Work Journals) OR (filename includes Fi 2023) OR (filename includes Fi 2024)
not done
sort by created
```

| Peripheral   | I2C Address |
| ------------ | ----------- |
| BQ25180      | 0x6A        |
| BQ27421      | 0x55        |
| CXD5605      | 0x24        |
| LP5523       | 0x32        |
| RA9530       | 0x3b        |
| RV4162C7<br> | 0x68        |

**2024-07-09**
1. GNSS info timestamp exactly identical
2. GNSS info getting bundle
3. 

**2024-07-08**
A lot of reboots, but not sure if they are real

**2024-07-05**
Very very frequent reboot - https://internaltools.corp.tryfi.com/devices/FC32M541198
A LOT of flapping - https://internaltools.corp.tryfi.com/devices/FC32L238670

**2024-07-02**
07/02 - ***4.16 rollout update***  
4.16.28 is pushed to fix bug where modem isn't properly put to sleep in certain cases.
Base FW 3.1.11 currently enabled for 11K external users now.

- A somewhat few modem crash when user is in poor LTE signal environment, gracefully handle the nrf9160 failure instead of crashing.
- Look for more modules with significant battery drain running 4.16 FW

**2024-07-01**
07/01 - ***4.16 rollout update***  
4.16.27 is currently still rolled out to 100 external users + updated 3.1.11 Base FW for the household  
Base FW 3.1.11 currently enabled for 1K external users (We accidentally enabled it for bases that was not activated yet)

- Base64 encoding bug properly fixed and deployed to the 100s users
- Investigating 2 case where module getting poor battery life after FWUP to 4.16, and deciding if there is anything to be done via server config. And if continue with push to more external users.

**2024-06-25**
4.16 Rollout update
4.16.23 is currently rolled out to 100 external users + updated 3.1.11 Base FW

**Current investigation**:
- CXD5605 getting locked up in rare case where module is in poor LTE condition for prolonged period (only Loren is seeing this right now), releasing 4.16.24 to test this on Comet's collar first.
- LTE Websocket report arriving at backend out of ordered, likely during poor LTE condition, where the first report is timed out, and module attempt retry and lands in backend earlier than the initial timed out report
- LTE websocket don't always stay connected for extend period of time, and it seems like the WS PING msg is not getting delivered to module at all

**2024-06-24**
- WS Ping seems to be always timeout more often than not
```
[21:36:17] 00:07:41.879 D [pick_report_backhaul] ble_disconnects_in_last_10m=0, report_is_due:0, curr_backhaul:NONE
[21:36:19] 00:07:43.540 I [fi_nrf9160_logger_handle_modemlink_msg] Sleep exit: LTE_LC_MODEM_SLEEP_RF_INACTIVITY(2)
[21:36:21] 00:07:45.219 I [fi_nrf9160_logger_handle_modemlink_msg] RRC status: LTE_LC_RRC_MODE_CONNECTED (1)
[21:36:21] 00:07:45.423 D [fi_lte_ws__modem_event_handler] Socket(2)
[21:36:21] 00:07:45.423 D [fi_lte_ws__modem_event_handler] MODEM_EVT_SOCKET_READ_READY
[21:36:21] 00:07:45.429 D [fi_lte_ws__on_socket_read_ready] Read 2 bytes from websocket
[21:36:21] 00:07:45.429 D [fi_lte_ws__modem_event_handler] Socket(2)
[21:36:21] 00:07:45.430 D [fi_lte_ws__modem_event_handler] MODEM_EVT_SOCKET_ERROR
[21:36:21] 00:07:45.430 E [fi_lte_ws__on_socket_error] Socket error 0
[21:36:21] 00:07:45.436 D [fi_lte_ws_close] Closed socket 2
[21:36:21] 00:07:45.437 W [fi_lte_ws_poll] WS EVT (4)
[21:36:21] 00:07:45.437 D [fi_lte_ws_poll] Websocket CONTROL (9).
[21:36:21] 00:07:45.437 D [fi_lte_ws__on_control] Websocket PING: (0)
[21:36:21] 00:07:45.439 W [fi_lte_ws_poll] WS EVT (1)
[21:36:21] 00:07:45.439 D [fi_lte_ws_poll] Websocket TX (6)
[21:36:22] 00:07:46.547 D [fi_ble_log_state] not connected and advertising
```
Sometimes the ping msg just don't get received on device!! while a later server push works

**2024-06-24**
```
mutation {
  adminMigrateModulesToFirmwareChannel(
    deviceType: BASE
    platform: "fb3_f1"
    moduleIds: ["FB32M909174"],
    channel: "fb3_f1-external-tester"
  ) {
    numUpdated
  }
}
```

```
WITH households AS (
SELECT
p.householdId
FROM
main.postgres.fi_pet p
JOIN main.postgres.fi_device d ON (p.deviceId = d.id)
WHERE
d.moduleId IN ('FC33E605931', 'FC33L001003')
)
SELECT
DISTINCT baseId
FROM
main.postgres.fi_charging_base c
JOIN households USING (householdId);
```

```
SELECT
module_id
FROM
device_info
where
module_firmware LIKE "4.15.8%"
and date > "2024-06-22"
limit
100
```
**2024-06-28**
06/28 - **4.16 rollout update**  
4.16.26 is currently still rolled out to 100 external users + updated 3.1.11 Base FW for the household
Base FW 3.1.11 currently enabled for 11K external users

- There is still a problem with the submission report base64 encoding, and for reason unknown it is also effecting external users somehow, but at very low frequency for now. Going to be holding the 4.16 to current 100 external user until this is addressed.
- Base FW currently enabled for 11K external users but it is somehow not getting reflected on the admin UI 

**2024-06-27**
06/27 - **4.16 rollout update**  
4.16.23 is currently still rolled out to 100 external users + updated 3.1.11 Base FW for the household
4.16.25 is currently on fi internal users

- 4.16.25 still have one more minor bug with rlog encoding that only effect internal users, but will need to fixed before pushed to external fi users
- Still trying to reproduce the submission report issue arriving at backend out of order but shouldn't have too much user impact at the moment
- Bumping base FW rollout to 10K 

**2024-06-26**
Need to investigate base uptime
06/26 - *4.16 rollout update*
4.16.23 is currently still rolled out to 100 external users + updated 3.1.11 Base FW for the household

- 4.16.24 was pushed to Comet's collar and seems to address CXD5605 lockup issue, but 1 more additional fix to FW crash before ready to push to external users
- We have a better understanding of the LTE WS socket error issues now
- but still be seeing submission report arriving at backend out of ordered, something needs to investigate more
- Also looking at base status, and deciding today if okay to push 3.1.11 Base FW to wider external users


**2024-06-25**
4.16 Rollout update
4.16.23 is currently rolled out to 100 external users + updated 3.1.11 Base FW

**Current investigation**:
- CXD5605 getting locked up in rare case where module is in poor LTE condition for prolonged period (only Loren is seeing this right now), releasing 4.16.24 to test this on Comet's collar first.
- LTE Websocket report arriving at backend out of ordered, likely during poor LTE condition, where the first report is timed out, and module attempt retry and lands in backend earlier than the initial timed out report
- LTE websocket don't always stay connected for extend period of time, and it seems like the WS PING msg is not getting delivered to module at all

**2024-06-24**
- WS Ping seems to be always timeout more often than not
```
[21:36:17] 00:07:41.879 D [pick_report_backhaul] ble_disconnects_in_last_10m=0, report_is_due:0, curr_backhaul:NONE
[21:36:19] 00:07:43.540 I [fi_nrf9160_logger_handle_modemlink_msg] Sleep exit: LTE_LC_MODEM_SLEEP_RF_INACTIVITY(2)
[21:36:21] 00:07:45.219 I [fi_nrf9160_logger_handle_modemlink_msg] RRC status: LTE_LC_RRC_MODE_CONNECTED (1)
[21:36:21] 00:07:45.423 D [fi_lte_ws__modem_event_handler] Socket(2)
[21:36:21] 00:07:45.423 D [fi_lte_ws__modem_event_handler] MODEM_EVT_SOCKET_READ_READY
[21:36:21] 00:07:45.429 D [fi_lte_ws__on_socket_read_ready] Read 2 bytes from websocket
[21:36:21] 00:07:45.429 D [fi_lte_ws__modem_event_handler] Socket(2)
[21:36:21] 00:07:45.430 D [fi_lte_ws__modem_event_handler] MODEM_EVT_SOCKET_ERROR
[21:36:21] 00:07:45.430 E [fi_lte_ws__on_socket_error] Socket error 0
[21:36:21] 00:07:45.436 D [fi_lte_ws_close] Closed socket 2
[21:36:21] 00:07:45.437 W [fi_lte_ws_poll] WS EVT (4)
[21:36:21] 00:07:45.437 D [fi_lte_ws_poll] Websocket CONTROL (9).
[21:36:21] 00:07:45.437 D [fi_lte_ws__on_control] Websocket PING: (0)
[21:36:21] 00:07:45.439 W [fi_lte_ws_poll] WS EVT (1)
[21:36:21] 00:07:45.439 D [fi_lte_ws_poll] Websocket TX (6)
[21:36:22] 00:07:46.547 D [fi_ble_log_state] not connected and advertising
```
Sometimes the ping msg just don't get received on device!! while a later server push works

**2024-06-24**
```
mutation {
  adminMigrateModulesToFirmwareChannel(
    deviceType: BASE
    platform: "fb3_f1"
    moduleIds: ["FB32M909174"],
    channel: "fb3_f1-external-tester"
  ) {
    numUpdated
  }
}
```

```
WITH households AS (
SELECT
p.householdId
FROM
main.postgres.fi_pet p
JOIN main.postgres.fi_device d ON (p.deviceId = d.id)
WHERE
d.moduleId IN ('FC33E605931', 'FC33L001003')
)
SELECT
DISTINCT baseId
FROM
main.postgres.fi_charging_base c
JOIN households USING (householdId);
```

```
SELECT
module_id
FROM
device_info
where
module_firmware LIKE "4.15.8%"
and date > "2024-06-22"
limit
100
```

**2024-06-17**
Summary from FW sync today on next 4.16 release plan:
- Adding explicit modem cell searching during request net ready if modem not registered
- If WS socket error, try to re-establish WS and retry submission report sending

- [x] Need to fix lte stay on time to be server config ✅ 2024-06-18
- [ ] Need to fix wifi scan attempt, don't always trigger LTE report
- [x] Fix server push quick toggle causing crash ✅ 2024-07-09

**2024-06-19**
Y: Fixing edrx configuration in 4.16
T: Monitor 4.16 in internal testers and decide if need to push out to external users

**2024-06-17**
Summary from FW sync today on next 4.16 release plan:
- Adding explicit modem cell searching during request net ready if modem not registered
- If WS socket error, try to re-establish WS and retry submission report sending

- [x] Need to fix lte stay on time to be server config ✅ 2024-06-18
- [x] Need to fix wifi scan attempt, don't always trigger LTE report ✅ 2024-07-09
- [x] Fix server push quick toggle causing crash ✅ 2024-07-09
- [x] Summary of changes post TLS WS change ✅ 2024-07-09

**2024-06-14**
- Modem searching event could be triggered at any time, so modem actor should correctly handle searching events
- Often get modem is re-registered back to network after searching for a period of time, but WS have been closed on the backend, module still trying to send on the same socket.

- If the modem is toggling?

```
%PERIODICSEARCHCONF:
 <loop>,<return_to_pattern>,<band_optimization>,<pattern_1>[,<pattern_2>][,<pattern_3>] [,<pattern_4>]

<type>,<initial_sleep>,<final_sleep>,[<time_to_final_sleep>],<pattern_end_point>
```
**loop**:
- 0 - No Loop
- 1 - Loop search pattern

**return_to_patter**:
- 0 - No return
- 1-4 return to search pattern index 1-4

**band_optimization**:
- 0 - No op

**type**:
- 0 - range
- 1 - table

Modem searching:
- When modem lose signal it doesn't actually go into searching, DRX/eDRX cycle still happens.
- modem go into high power searching mode only when trying to send/RX data, for ~1mins.
- Ultra-low power data profile seems do searching backoff. With base current of 3mA
- 

**2024-06-13**
`[10:31:18] 00:01:45.636 ! [fi_nrf9160_modem_msg_proc] phy_id:0x177 id:0xf24b0f rsrp:66 rsrq:25 tx:6 snr:42 band:12 energy:8 mcc/mnc:13619a`

- Handle random search events
- Net-ready phase WS, via ping-pong after long idle
- During long idle, trigger LTE re-eval on new tower
- Try to send data on closed socket, should trigger socket error, get a packet trace
- Ask noridc what is the correct response to Unknown REG
**2024-06-12**
- [x] Help Lesley getting 4.16 User impacting feature language ✅ 2024-06-17

**2024-06-10**
- The nominal way to use eDRX
    - When should eDRX be turned on for TCP connections?
    - Any situation eDRX should be turned off for?
    - What is eDRX effect on latency
- We are occasionally seeing significant packet latency 

Hi Nordic Team,
My name is James, and I am one of the FW engineer here at Fi. Our director of HW Bob Blake give me your contact info, and could maybe help use with some question on LTE usage on the nrf9160.

We are currently working on enhancing the reachability of our hardware module to our backend server by implementing web sockets with TCP over an LTE connection. As part of this effort, we have configured the LTE connection to utilize eDRX, with a cycle time ranging from 5.12 seconds to 20.48 seconds. This setup aims to enable efficient data transmission from our server to the module while managing power consumption effectively.

However, during field testing, we have encountered challenges related to TCP socket level failures and difficulties in maintaining our WebSocket (WS) connection. These issues have arisen in locations where previous HTTP traffic was functioning smoothly. Consequently, we are considering whether our utilization of LTE eDRX could be contributing to these problems.

In light of these observations, we have several questions regarding LTE eDRX that we would like to seek your guidance on:

1. **Nominal Usage of LTE eDRX:**
Given our scenario of using web sockets with TCP over LTE, could you provide insight into the optimal utilization of eDRX? We are particularly interested in understanding how eDRX should be configured to maintain a stable and reliable connection while balancing power consumption.

2. **Situational Use of eDRX:**
In what specific scenarios should we enable or disable eDRX? For instance, should eDRX be active only during periods of module idleness, or should it remain enabled even during high data exchange periods?

3. **Frequent Configuration of eDRX:**
We have observed that frequent toggling of eDRX, such as every few seconds, may impact connection stability. Could this frequent reconfiguration be a contributing factor to the TCP socket level failures and WS connection issues we are experiencing?

Your expertise in addressing these questions would be immensely valuable as we work towards optimizing our use of LTE eDRX to enhance the reliability and performance of our product’s connectivity.

In addition we are using nRF9160 as our modem chip, with modem FW version `mfw_nrf9160_1.3.1` and `mfw_nrf9160_1.3.5` in the field, in case that matters to this conversation.

Thank you for your time and assistance.
  
Best regards,


**2024-06-06**
- https://github.com/barkinglabs/firmware/pull/1977
- https://github.com/barkinglabs/firmware/pull/1967
- https://github.com/barkinglabs/firmware/pull/1979
- https://github.com/barkinglabs/firmware/pull/1980
- https://github.com/barkinglabs/firmware/pull/1981

**2024-06-05**
- Need to figure out why SOCKET_WRITE would timeout

**2024-06-04**
```
[22:14:57] 00:04:54.081 D [fi_lte_ws__modem_event_handler] Socket(2)
[22:15:07] 00:04:54.081 D [fi_lte_ws__modem_event_handler] MODEM_EVT_SOCKET_WRITE_READY
[22:15:07] 00:04:54.091 D [fi_lte_ws__on_socket_write_ready] Transmitting 2388 bytes on websocket 2
[22:15:09] 00:05:04.092 W [fi_nrf9160_modem_modemlink_send_message_sync] Timed out waiting for response for: 16 (id: 120)
[22:15:09] 00:05:04.092 D [fi_nrf9160_modem_socket_write] write res -1
[22:15:09] 00:05:04.092 E [fi_lte_ws__on_socket_write_ready] Failed to write to websocket: -1
[22:15:09] 00:05:06.024 W [fi_nrf9160_modem_modemlink_s:06.030 I [power_check_battery_charger] Battery: state 3, bq25180_stat0:0x61, is_chg:0 has_pwr:1 on_base:0 has_power_supply=1
[22:15:09] 00:05:06.031 I [utc_wallclock_sync] Syncing UTC clock
[22:15:09] 00:05:06.039 I [module_hsm_log_state] T1=47s T2=-1s T3=-1s State=[ lte-connection, lte:send-report ]
[22:15:09] 00:05:06.047 E [fi_cxd5605_gnss_server__check_lockup] CXD5605 flow timeout after 12 sec, disabling part
[22:15:09] 00:05:06.049 D [fi_remote_log_add] Added remote log: 12
[22:15:09] 00:05:06.049 I [fi_cxd5605_gnss_server__set_state] state change: POSITIONING -> DISABLING
[22:15:09] 00:05:06.051 D [fi_remote_log_add] Added remote log: 22
[22:15:09] 00:05:06.051 W [fi_lick_classify_actor__process_samples] accel samples dropped, reporting gap
[22:15:09] 00:05:06.079 I [fi_cxd5605_frontend_log_status] boot=H recover=U enabled=0 error=0 tcxo=0 pos=0 lle=1 fw=<20107,1059ebf,123E>
[22:15:09] 2024 06 04 00 00  3
[22:15:09] 0
[22:15:09] 2024 06 04 00 00  3
[22:15:09] 0
[22:15:09] 0
[22:15:09] 00:05:06.079 I [fi_cxd5605_gnss_server__set_state] state change: DISABLING -> DISABLED
[22:15:09] 00:05:06.081 D [fi_remote_log_add] Added remote log: 22
[22:15:09] 00:05:06.081 E [fi_location_actor__process_msg] CXD5605 unexpectedly disabled!
[22:15:09] 00:05:06.083 D [fi_remote_log_add] Added remote log: 22
```

**2024-06-03**
```
[20:45:47] 00:06:56.968 D [fi_cxd5605_flow_enable__set_state] GET_VERSION => WAIT_FOR_DISABLED_MODE
[20:45:47] 00:06:56.970 W [fi_modem_actor__check_state_timeout] Modem timeout on DOWNLOAD
[20:45:47] 00:06:56.971 D [fi_remote_log_add] Added remote log: 12
[20:45:47] 00:06:56.973 D [fi_remote_log_add] Added remote log: 22
[20:45:47] 00:06:56.973 W [fi_lick_classify_actor__process_samples] accel samples dropped, reporting gap
[20:45:47] 00:06:56.978 E [handle_failed_assert] ASSERT FAIL: "msg->topic == FI_CXD5605_BACKEND_TOPIC_CMD_SET_MODE 205" file "../../src/libgnss_cxd5605/fi_cxd5605_flow_enable.c", line 81
```


```
[20:53:07] 00:07:15.720 I [fi_lte_ws_close] Websocket not connected
[20:53:07] 00:07:15.720 E [fi_modem_actor__open_ws] FI LTE WS connect FAIL!
[20:53:07] 00:07:15.722 D [fi_remote_log_add] Added remote log: 22
[20:53:07] 00:07:15.732 E [lis2dw12_poll] lis2dw12 lost samples in fifo
[20:53:07] 00:07:15.732 W [fi_accel_dispatch_actor_poll] lost accel samples, flushing store
[20:53:07] 00:07:15.732 D [fi_ble_log_state] not connected and advertising
[20:53:07] 00:07:15.735 I [power_check_battery_charger] Battery: state 3, bq25180_stat0:0x61, is_chg:0 has_pwr:1 on_base:0 has_power_supply=1
[20:53:07] 00:07:15.742 I [utc_wallclock_sync] Syncing UTC clock
[20:53:07] 00:07:15.751 I [module_hsm_log_state] T1=169s T2=-1s T3=-1s State=[ lte-connection, lte:net-ready ]
[20:53:07] 00:07:15.755 D [fi_remote_log_add] Added remote log: 22
[20:53:07] 00:07:15.756 E [report_response_complete_handler] Report submission failed, 3 time!
[20:53:07] 00:07:15.756 D [brain_consume_event] REPORT_ABORT
[20:53:07] 00:07:15.756 W [report_response_complete_handler] Give up on LTE report after 3 failure, set LTE backoff!
[20:53:07] 00:07:15.757 W [lte_reg_failed_set_backoff_time] LTE Registration FAILED!
[20:53:07] 00:07:15.767 W [lte_reg_failed_set_backoff_time] LTE backoff 120 sec
[20:53:07] 00:07:15.768 D [fi_remote_log_add] Added remote log: 12
[20:53:07] 00:07:15.769 I [module_hsm_send_event] REPORT_COMPLETE
[20:53:07] 00:07:15.769 I [evaluate_transition_targets] -> 'lte:idle', condition 'none'
[20:53:07] 00:07:15.778 I [hsm_instance_transition] moving to state: lte:idle
[20:53:07] 00:07:15.778 I [transition_to_path] lte:idle
[20:53:07] 00:07:15.779 I [pop_state] Exiting lte:net-ready
[20:53:07] 00:07:15.789 I [pop_state] Running exit action: stop_timer
[20:53:07] 00:07:15.790 I [push_state] Entering lte:idle
[20:53:07] 00:07:15.790 I [push_state] start_timer
[20:53:07] 00:07:15.790 I [_act_impl_start_timer] Starting HSM timer -- 5000 ms
[20:53:07] 00:07:15.801 I [push_state] lte_idle_poll
[20:53:07] 00:07:15.801 I [should_lte_stop] LTE on for 89 sec, Report is NOT DUE
[20:53:07] 00:07:15.803 D [fi_remote_log_add] Added remote log: 7
[20:53:07] 00:07:15.812 I [brain__log_state] Sending WIFI (89s/10s after good wifi lost)
[20:53:07] 00:07:15.813 I [module_hsm_send_event] REPORT_IS_DUE
[20:53:07] 00:07:15.813 I [evaluate_transition_targets] -> '', condition 'none'
[20:53:07] 00:07:15.813 I [hsm_instance_transition] null transition
[20:53:07] 00:07:15.824 I [run_transition_actions] lte_idle_poll
[20:53:07] 00:07:15.824 I [should_lte_stop] LTE on for 89 sec, Report is DUE
[20:53:07] 00:07:15.824 D [_cond_impl_have_data_for_lte_report] send_wifi_result(1) published_fix(0) live_tracking_due(0) forced_report(0)
[20:53:07] 00:07:15.836 D [fi_remote_log_add] Added remote log: 7
[20:53:07] 00:07:15.837 W [fi_lick_classify_actor__process_samples] accel samples dropped, reporting gap
[20:53:07] 00:07:15.858 I [module_hsm_send_event] LTE_STOP
[20:53:07] 00:07:15.859 I [evaluate_transition_targets] -> 'no-connection', condition 'none'
[20:53:07] 00:07:15.859 I [hsm_instance_transition] moving to state: no-connection
[20:53:07] 00:07:15.859 I [transition_to_path] no-connection
[20:53:07] 00:07:15.869 I [pop_state] Exiting lte:idle
[20:53:07] 00:07:15.869 I [pop_state] Running exit action: stop_timer
[20:53:07] 00:07:15.870 I [pop_state] Exiting lte-connection
[20:53:07] 00:07:15.880 I [pop_state] Running exit action: lte_stop
[20:53:07] 00:07:15.881 D [brain_consume_event] LTE_STOP
[20:53:07] 00:07:15.881 I [push_state] Entering no-connection
[20:53:07] 00:07:15.881 I [push_state] start_timer
[20:53:07] 00:07:15.882 I [_act_impl_start_timer] Starting HSM timer -- 5000 ms
[20:53:07] 00:07:15.882 I [push_state] check_is_report_due
[20:53:07] 00:07:15.884 D [fi_remote_log_add] Added remote log: 7
[20:53:07] 00:07:15.884 I [module_hsm_send_event] SEND_LTE_REPORT
[20:53:07] 00:07:15.893 I [evaluate_transition_targets] -> 'lte-connection', condition 'none'
[20:53:07] 00:07:15.894 I [hsm_instance_transition] moving to state: lte-connection
[20:53:07] 00:07:15.894 I [transition_to_path] lte-connection
[20:53:07] 00:07:15.905 I [pop_state] Exiting no-connection
[20:53:07] 00:07:15.905 I [pop_state] Running exit action: stop_timer
[20:53:07] 00:07:15.905 I [push_state] Entering lte-connection
[20:53:07] 00:07:15.916 I [push_state] lte_start
[20:53:07] 00:07:15.916 D [fiwifi_client_stop_remain_assoc_time] stopping
[20:53:07] 00:07:15.916 I [fiwifi_parser_reset] fiwifi_parser_reset
[20:53:07] 00:07:15.917 D [brain_consume_event] LTE_START
[20:53:07] 00:07:15.927 I [transition_to_path] Entering sub-machine: lte-connection
[20:53:07] 00:07:15.928 I [transition_to_path] lte:idle
[20:53:07] 00:07:15.928 I [push_state] Entering lte:idle
[20:53:07] 00:07:15.939 I [push_state] start_timer
```

**2024-05-31**

```
[16:10:22] 00:01:56.637 D [fi_modem_actor__set_curr_state_timeout] AWAIT_WS: 60
[16:10:22] 00:01:56.638 W [fi_lte_ws_poll] WS EVT (1)
[16:10:22] 00:01:56.638 D [fi_lte_ws_poll] Websocket TX (295)
[16:10:22] 00:01:56.638 D [fi_nrf9160_modem_socket_req_poll] requesting socket poll for 2[w1;r1;e1]
[16:10:23] 00:01:56.848 D [fi_nrf9160_modem_msg_proc] socket write ready for 2
[16:10:23] 00:01:56.849 D [fi_modem_actor_poll__process_msg] topic(309)
[16:10:23] 00:01:56.850 D [fi_modem_actor__event_handler] evt: 8
[16:10:23] 00:01:56.850 D [fi_lte_ws__modem_event_handler] Socket(2)
[16:10:23] 00:01:56.850 D [fi_lte_ws__modem_event_handler] MODEM_EVT_SOCKET_WRITE_READY
[16:10:23] 00:01:56.851 D [fi_lte_ws__on_socket_write_ready] Transmitting 295 bytes on websocket 2
[16:10:23] 00:01:56.858 D [fi_nrf9160_modem_socket_write] write res 295
[16:10:23] 00:01:56.858 D [fi_lte_ws__on_socket_write_ready] Sent all 295 bytes
[16:10:23] 00:01:56.859 D [fi_nrf9160_modem_socket_req_poll] requesting socket poll for 2[w0;r1;e1]
[16:10:23] 00:01:57.068 D [fi_nrf9160_modem_msg_proc] socket read ready for 2
[16:10:23] 00:01:57.070 D [fi_modem_actor_poll__process_msg] topic(309)
[16:10:23] 00:01:57.070 D [fi_modem_actor__event_handler] evt: 9
[16:10:23] 00:01:57.070 D [fi_lte_ws__modem_event_handler] Socket(2)
[16:10:23] 00:01:57.071 D [fi_lte_ws__modem_event_handler] MODEM_EVT_SOCKET_READ_READY
[16:10:23] 00:01:57.077 D [fi_lte_ws__on_socket_read_ready] Read 167 bytes from websocket
[16:10:23] 00:01:57.078 W [fi_lte_ws_poll] WS EVT (0)
[16:10:23] 00:01:57.078 D [fi_lte_ws_poll] Websocket upgrade succeeded
[16:10:23] 00:01:57.079 D [fi_nrf9160_modem_socket_req_poll] requesting socket poll for 2[w0;r1;e1]
[16:10:23]  5
[16:10:23] 00:01:57.107 D [fi_modem_actor_poll__process_msg] topic(309)
[16:10:23] 00:01:57.108 D [fi_modem_actor__event_handler] evt: 13
```

Cherry-pick list
- https://github.com/barkinglabs/firmware/pull/1969
- https://github.com/barkinglabs/firmware/pull/1968
- https://github.com/barkinglabs/firmware/pull/1966
- https://github.com/barkinglabs/firmware/pull/1965
- https://github.com/barkinglabs/firmware/pull/1972
- 


**2024-05-30**

```
#0  0x00038a6a in app_util_critical_region_enter (
    p_nested=0x20019ec8 <s_transport_buf+388> "\001\002\001\377\060\155\040\111\040\033\133\060\155\133\160\165\163\150\137\163\164\141\164\145\135\040\033\133\061\073\063\066\155\162\145\161\165\145\163\164\137\154\164\145\137\156\145\164\137\162\145\141\144\171\033\133\060\155\012\060\060\072\060\063\072\064\067\056\067\071\071\033\133\061\073\063\066\155\040\127\040\033\133\060\155\133\146\151\137\162\145\155\157\164\145\137\154\157\147\137\141\144\144\135\040\117\165\164\040\157\146\040\163\160\141\143\145\040\151\156\040\162\145\155\157\164\145\040\154\157\147\040\163\164\157\162\141\147\145\040\142\165\146\146\145\162\056\040\127\162\151\164\151\156\147\040\155\145\163\163\141\147\145\040\164\150\141\164\040\167\145\040\141\162\145\040\157\165\164\040\157\146\040\163\160\141\143\145\056\033\133\060\155\012\060\060\072\060\063\072"...) at ../../nrf5_sdk/17.0.2/components/libraries/util/app_util_platform.c:76
#1  0x0004e114 in fi_mutex_lock (mutex=<optimized out>, timeout_ms=timeout_ms@entry=0) at ../../src/libfi_nrf52drv/fi_mutex_nrf52.c:44
#2  0x0005ab80 in buf_pool_get_write_buffer (buf_pool=0x20019e84 <s_transport_buf+320>) at ../../src/firmware-common/libfilink/bufpool.c:102
#3  0x0005a56a in fi_link_send_frame (link=link@entry=0x20019d44 <s_transport_buf>, channel=channel@entry=0 '\000', data=data@entry=0x2002e6fc <s_tx_buffer>, size=size@entry=256) at ../../src/firmware-common/libfilink/filink.c:109
#4  0x00051134 in fi_transport__uart_filink_tx (t=t@entry=0x20019d28 <s_transport>, channel_name=<optimized out>, buf=<optimized out>, len=256) at ../../src/libfi_transport/fi_transport.c:106
#5  0x0005131e in fi_transport_tx_to_host (t=t@entry=0x20019d28 <s_transport>, channel=channel@entry=FI_TRANSPORT_CHANNEL_NAME_ASCII_TERMINAL, buf=buf@entry=0x2002e6fc <s_tx_buffer>, len=<optimized out>) at ../../src/libfi_transport/fi_transport.c:189
#6  0x00048f90 in fi_app_host_term_flush (ctx=ctx@entry=0x20019d28 <s_transport>) at ../../src/libfi_app/fi_app_host_term.c:25
#7  0x000490f4 in fi_app_host_term_putc (c=91, ctx=0x20019d28 <s_transport>) at ../../src/libfi_app/fi_app_host_term.c:70
#8  0x0004091a in npf_putc_cnt (c=<optimized out>, ctx=ctx@entry=0x2003f990) at ../../src/firmware-common/external/nanoprintf/nanoprintf/nanoprintf.h:691
#9  0x00040958 in npf_vpprintf (pc=<optimized out>, pc_ctx=<optimized out>, format=format@entry=0x71ad0 "O", args=...) at ../../src/firmware-common/external/nanoprintf/nanoprintf/nanoprintf.h:712
#10 0x0003ff78 in fi_host_term_printf (fmt=0x6e920 "\033\133\061\073\063\066\155") at ../../src/firmware-common/libcore/fi_host_term.c:32
#11 0x000491fa in fi_app_log_handle (ctx=0x2003fa8c, buf=0x0, buf_len=0, fmt=0x71ad0 "O", args=...) at ../../src/libfi_app/fi_app_log.c:77
#12 0x00040006 in fi_log__vl (severity=severity@entry=FI_LOG_SEVERITY_WARN, remote=remote@entry=false, func=func@entry=0x71b88 <__func__.0> "f", fmt=fmt@entry=0x400ff <fi_log_wrn+26> "\260]\370\004\353\003\260p\264", args=..., args@entry=...)
    at ../../src/firmware-common/libcore/fi_log.c:40
#13 0x000400fe in fi_log_wrn (func=func@entry=0x71b88 <__func__.0> "f", fmt=0x71ad0 "O") at ../../src/firmware-common/libcore/fi_log.c:130
#14 0x00041404 in fi_remote_log_add (msg=msg@entry=0x2003fdc0) at ../../src/firmware-common/libfi_remote_log/fi_remote_log.c:375
#15 0x0004153c in fi_remote_log_add_state_machine_transition (state_machine_id=state_machine_id@entry=1, from_state=0, to_state=to_state@entry=0, meta_info=0x6802c "R") at ../../src/firmware-common/libfi_remote_log/fi_remote_log.c:254
#16 0x0002c8c0 in fi_modem_actor__set_state (ma=ma@entry=0x2000cc20 <s_modem_actor>, state=state@entry=FI_MODEM_ACTOR_STATE_IDLE) at ../../src/nrf52/fi_module/fi_modem_actor.c:419
#17 0x0002c914 in fi_modem_actor__request_handler (ma=ma@entry=0x2000cc20 <s_modem_actor>, request=<optimized out>) at ../../src/nrf52/fi_module/fi_modem_actor.c:449
#18 0x0002d24a in fi_modem_actor_poll__process_msg (msg=0x2003fe94, ctx=0x2000cc20 <s_modem_actor>) at ../../src/nrf52/fi_module/fi_modem_actor.c:570
#19 0x0004376a in fi_pubsub_retrieve_mult (ps=0x20006200 <s_pubsub_buf>, actor_id=<optimized out>, cb=cb@entry=0x2d0f9 <fi_modem_actor_poll__process_msg>, ctx=ctx@entry=0x2000cc20 <s_modem_actor>) at ../../src/firmware-common/libutil/fi_pubsub.c:440
#20 0x0002d760 in fi_modem_actor_poll (ma=ma@entry=0x2000cc20 <s_modem_actor>, elapsed_sec_since_boot=<optimized out>) at ../../src/nrf52/fi_module/fi_modem_actor.c:166
#21 0x0003008a in main () at ../../src/nrf52/fi_module/main.c:1296
```

**2024-05-24**
Y: Monitor 4.16.16 release to internal fi users, experimenting with different way to detect low LTE signal and how to better handle it  
T: Continue exploring low LTE signal detection and operations
![[Pasted image 20240524214517.png]]
```
#2  0x0004ebee in fi_mutex_lock (mutex=0x78690, timeout_ms=timeout_ms@entry=0) at ../../src/libfi_nrf52drv/fi_mutex_nrf52.c:40
#3  0x0005b6ca in buf_pool_release_read_buffer (buf_pool=0x2001af58 <s_transport_buf+320>) at ../../src/firmware-common/libfilink/bufpool.c:88
#4  0x0005b25c in fi_link_tx_to_phy_end (link=<optimized out>) at ../../src/firmware-common/libfilink/filink.c:262
#5  0x00051adc in fi_transport__uart_event_handler (ctx=0x2001adfc <s_transport>, evt=<optimized out>) at ../../src/libfi_transport/fi_transport.c:47
#6  0x0005cc70 in bsp_uart__event_handler (ctx=<optimized out>, evt=0x2003fdac) at ../../src/bsp/nrf52/bsp_uart.c:181
#7  0x000360d6 in uart_evt_handler (context=0x858c8 <s_uart1>, p_evt=<optimized out>) at ../../nrf5_sdk/17.0.2/components/libraries/libuarte/nrf_libuarte_async.c:211
#8  0x00036952 in irq_handler (p_libuarte=0x858f8 <s_uart1_libuarte>) at ../../nrf5_sdk/17.0.2/components/libraries/libuarte/nrf_libuarte_drv.c:813
#9  0x00037126 in UARTE1_IRQHandler () at ../../nrf5_sdk/17.0.2/components/libraries/libuarte/nrf_libuarte_drv.c:866
```

> install the latest community version of visual studio, and make sure you get the windows sdk / uwp / winrt stuff as well (they're extra check boxes in the installer). I throw in .net as well since C# tools can be handy every now and then
> install python from [python.org](http://python.org/), there's an MSI installer
> on windows you run python with `py -3.11` instead of `python3.11`; there's a centralized launcher thing
> make sure you open a visual studio developer command prompt or powershell; i set the powershell one up in windows terminal to be the default shell
 i don't remember how i installed yarn / node but it was a fucking mess

**2024-05-23**
**Strategies for Operating nRF9160 in Poor LTE Signal Environments and Monitoring Connection Quality**

Hello,

I'm working on a product using the nRF9160 and facing challenges with poor LTE signal strength, leading to significant power drain when the device goes offline. I have a few specific questions and would appreciate any recommendations:

1. Modem Behavior in Low/No Signal:
    - How does the modem behave when transitioning from good to low/no signal?
    - On my dev kit, the modem can take up to 60 seconds in a high-power searching state before updating the registration status. Is there a way to detect this state earlier to reduce power drain?
2. RSRP and RSRQ Thresholds:
    - What levels of RSRP and RSRQ are considered too weak for a reliable network connection?
    - Are there guidelines for the minimum acceptable signal strength for stable operation?
3. Modem Signals for Connection Quality:
    - What signals or indicators does the nRF9160 modem provide to assess connection quality to the LTE tower?
4. General strategies for Poor LTE Signal Environments:
    - Are there any recommended strategies or best practices for optimizing the nRF9160's performance to reduce power drain in weak LTE signal areas?

**2024-05-21**
Y: Try to root cause and fix the module sending submission report to base too fast wedging the base
T: Continue to digging how the base is getting wedged by module FW

**2024-05-16**
Y: Root caused the time traveling RTC bug
T: Getting a new 4.16.13 Release ready for internal fi user for testing

**2024-05-15**
- [ ] https://github.com/stevearc/oil.nvim

```

james@fi-nuc-james:~/actions-runner$ sudo cp /home/james/actions-runner/_work/firmware/firmware/out/bin/venv/lib/python3.11/site-packages/fi/segger/data/99-jlink.rules /etc/udev/rules.d && sudo udevadm control --reload-rules && sudo udevadm trigger

james@fi-nuc-james:~/actions-runner$ sudo cp /home/james/actions-runner/_work/firmware/firmware/out/bin/venv/lib/python3.11/site-packages/fi/segger/data/99-jlink.rules /etc/udev/rules.d && sudo udevadm control --reload-rules && sudo udevadm trigger

echo \'SUBSYSTEMS=="usb", ATTRS{idVendor}=="04d8", ATTRS{idProduct}=="00df", MODE="0666"\' | sudo tee /etc/udev/rules.d/70-denkovi-relay.rules && sudo chmod 644 /etc/udev/rules.d/70-denkovi-relay.rules && sudo mv 52-usb.rules /etc/udev/rules.d/

sudo usermod -a -G dialout $USER
wget https://raw.githubusercontent.com/mvp/uhubctl/master/udev/rules.d/52-usb.rules
sudo mv 52-usb.rules /etc/udev/rules.d/
sudo udevadm trigger --attr-match=subsystem=usb
```

**2024-05-14**
Y: finished up modem standby implementation 
T: more testing with recent 4.16 fixes 

**2024-05-13**
Y: More work on unit tests skeleton adding mock libs
T: Finish up modem standby feature implementation


```
00:05:51.259 I [_act_impl_start_timer] Starting HSM timer -- 60000 ms
00:05:51.271 D [fi_remote_log_add] Added remote log: 7
<debug> nrf_sdh_ble: BLE event: 0x50.
00:05:51.515 D [fi_motion_detection_get_state] activity threshold 0.000006 3s
<debug> nrf_sdh_ble: BLE event: 0x50.
<debug> nrf_sdh_ble: BLE event: 0x50.
<debug> nrf_sdh_ble: BLE event: 0x51.
00:14:26.943 I [utc_wallclock_sync] Syncing UTC clock
00:14:26.959 E [fi_cxd5605_gnss_server__check_lockup] CXD5605 flow timeout after 512 sec, disabling part
```

**2024-05-10**
Y: more power testing for lte edrx ws operations
T: finished up unit test skeleton for various actors and start implementing the modem standby strategy 

What happens on low LTE signal state:
- LTE unreg?
- WS closed by peer?
- 

**2024-05-08**
Y: More 4.16 bug fix and monitoring walk data
T: Likely some power consumption testing for 4.16

for websocket opensearch logging
![[Pasted image 20240509141103.png]]

**2024-05-07**
Y: Adding more stats counters for 4.16 release
T: Continue follow up with 4.16 test results

**2024-05-06**
Y: pushing out yet another 4.16 releases for bug fix
T: continue monitoring 4.16 tests in the field and start documenting and planning for new device stats should add into fw for insight 

**2024-05-03**
8:47 LDM
#### Test plan
- BLE
    - Report sent every 60 sec
    - 2 Fail upload, disconnect over BLE
    - LDM sent every active upload interval
    - BLE fully attached at boot first pair
    - WIFI -> BLE, attach after 2 mins delay
    - BLE connect, but not attach disconnect after ~5 mins
    - BLE fast break, slow breaks
- WIFI
    - Report sent every 2 mins
    - LDM sent report every active upload interval
    - Failed report disconnect
    - WIFI disconnect after good wifi backhaul, will trigger retry first
    - BAD WIFI, trigger LTE report immediately
    - On report failure retry 3 times, then disconnect
- LTE
    - One off, start GPS
    - Send LTE report if 20 seconds no GPS fix, and have wifi data
    - GPS session finish, and send new report without starting new GPS
    - New one off LTE report, restart/resume GPS session
    - Open WS on LTE report
    - Leave LTE WS open
    - LTE REG FAIL backoff
    - LTE fail retry 3 times
    - LTE LDM, still try WIFI every 10 mins
    - LTE -> WIFI: Close LTE WS, turn off edrx, turn on PSM
    - LTE -> BLE: close LTE WS, turn off edrx, turn on PSM
- Modem Standby
    - BLE Start at boot -> LTE send report
    - LTE -> BLE ( Disconnect before WS close)
    - BLE -> LTE send 2 reports correctly
    - LTE -> BLE
    - Wait LTE close WS
    - BLE -> LTE re-open WS

 
**2024-05-02**
Y: cutting 4.16.6
T: Continue 4.16 Release testing, and look into effect of UTC time setting on gps positioning

- [x] Think about the balance between when we have data to send vs when when we have to send data ✅ 2024-06-17

**2024-05-01**
Y: getting 4.16 bug fixes merged, and more 4.16 testing
T: Cutting new 4.16 release and push to internal fi users

**2024-04-30**

Y: Continue 4.16 testing and bug fixes
T: Complete retained device stats HW CI testing, and maybe cut new 4.16 Test release

regarding the issue I mentioned in standup yesterday, where the FW was crashing in nrf9160_modem while getting a server pushed message at the same time it is sending a report. The issue was that we were sending async modemlink msg from modem actor, immediately followed by another modem link msg for WS, polling sockets.
hence crashing in `[handle_failed_assert] ASSERT FAIL: "!m->ps_publish_pending " file "../../src/libmodem_nrf9160/fi_nrf9160_modem.c", line 831`
I am thinking the quick solution here might be add a blocking wait in `fi_nrf9160_modem_modemlink_send_message_sync`, where it will wait until `m->ps_publish_pending` is complete before sending an new modem link msg. Since this is only a pubsub msg on the nrf52 side, it should be very quick. And given `fi_nrf9160_modem_modemlink_send_message_sync` is already a blocking sync call, it probably won't make too much difference.
I filed [PR](https://github.com/barkinglabs/firmware/pull/1871) to implement this. In testing this seems to work reliable and I can constantly trigger server push message and FW will behave correctly.

**2024-04-29**
Y: Cutting and testing 4.16.5, and yet more bug fixes
T: More small improvement to 4.16 release, and more testing

**2024-04-28**
> tl;dr : in 4.16 if we go from BLE to LTE (because wifi was missed on scan for some reason…) we only try to scan for wifi every 10min after that
 ideally — (1) if wifi comes in the list of visible wifi with gps report => server tells module to try wifi right away (2) if gps report in safe zone => try wifi every minute (3) if gps report out of safe zone => try every 10 min or even longer (edited)

 
- [x] double check socket stays open in wifi and LTE. ✅ 2024-06-17

- [x] Modem request is running into conflict, this is more of a pubsub issue ✅ 2024-06-17
```
00:08:54.808 D [fi_remote_log_add] Added remote log: 22
00:08:54.814 W [fi_lte_ws_poll] WS EVT (3)
00:08:54.815 D [fi_lte_ws_poll] Websocket RX END OF DATA
00:08:54.815 D [fi_lte_ws__on_rx_end_of_data] Received END OF DATA on websocket 2
00:08:54.815 D [brain_consume_event] FORCE_LTE_REPORT
00:08:54.828 D [fi_remote_log_add] Added remote log: 22
00:08:54.831 E [handle_failed_assert] ASSERT FAIL: "!m->ps_publish_pending " file "../../src/libmodem_nrf9160/fi_nrf9160_modem.c", line 831

00:08:54.831 W [fa00:00:00.020 ! [log_module_details] fi_module board=3 build=0.0.0-local-fc3_f3-dev platform_id=<null> module_id=FC32H000328
00:00:00.021 ! [log_module_details] BL Ver: 0.0.0-local-fc3_f3-dev-bl
00:00:00.021 I [fi_cpu_log_reset_reason] fi_cpu_log_reset_reason: SREQ
```

- [x] Check why edrxcycle time is so long ✅ 2024-04-28
![[Pasted image 20240428211635.png]]
The default edrx cycle time is configured on initial net request, that cycle time needs to elapsed before you can negotiated for the next one

**2024-04-26**
- [x] We don't seem to unregister from the network anymore when going back to BLE/WIFI ✅ 2024-05-06
![[Pasted image 20240426215056.png]]
- Still seeing some mobile report suppressing location report 

**2024-04-25**
Y: ultimut traveling, and working on backend for devis sys stat changes
T: do end to end testing of the device sys stat changes and setup unit test and hw tests 

- Use Nrf connect app to scan for nearby collars and see if it is online
- Set the collar on base, wait 5 sec to see if it start charging (flashing blue led) 
- Reset the collar while seated on the base, holding the base button near USB plug until base led turn red.
    - Collar should Flash Green LED patterns and restart

Field Theory account: https://internaltools.corp.tryfi.com/users/1587304
- https://internaltools.corp.tryfi.com/devices/FC34D167265
- https://internaltools.corp.tryfi.com/devices/FC33F064994

```
00:03:11.814 D [brain_consume_event] SENT_REPORT
00:03:11.826 E [lis2dw12_poll] lis2dw12 lost samples in fifo
00:03:11.826 W [fi_accel_dispatch_actor_poll] lost accel samples, flushing store
00:03:11.827 I [module_hsm_send_event] LTE_NET_READY
00:03:11.827 I [evaluate_transition_targets] -> '', condition 'none'
00:03:11.837 I [hsm_instance_transition] null transition
00:03:11.838 D [fi_remote_log_add] Added remote log: 7
00:03:11.839 D [fi_modem_actor_poll__process_msg] topic(311)
00:03:11.848 I [fi_modem_actor__set_goal] READY -> UPLOAD_DATA; s:PENDING
00:03:11.848 I [fi_modem_actor__set_state] PENDING -> UPLOAD
00:03:11.850 D [fi_remote_log_add] Added remote log: 22
00:03:11.857 W [fi_lick_classify_actor__process_samples] accel samples dropped, reporting gap
00:03:11.899 D [fi_modem_actor__http_upload] Upload ret: 0
00:03:11.899 I [fi_modem_actor__set_state] UPLOAD -> DOWNLOAD
00:03:11.900 D [fi_remote_log_add] Added remote log: 22
00:03:12.102 D [fi_modem_actor_poll__process_msg] topic(309)
00:03:12.103 D [http_modem_event_handler] Socket(1)
00:03:12.103 D [http_modem_event_handler] MODEM_EVT_SOCKET_ERROR
00:03:12.103 E [on_socket_error] HTTP sock err 0
00:03:12.105 D [fi_remote_log_add] Added remote log: 12
00:03:12.105 E [handle_error] HTTP err 'HPE_OK'
00:03:12.107 D [fi_remote_log_add] Added remote log: 12
00:03:12.113 D [fi_modem_actor__event_handler] evt: 9
00:03:12.113 I [fi_modem_actor__set_state] DOWNLOAD -> FAILED
00:03:12.115 D [fi_remote_log_add] Added remote log: 22
00:03:12.116 I [fi_modem_actor__set_state] FAILED -> PENDING
00:03:12.118 D [fi_remote_log_add] Added remote log: 22
00:03:14.448 D [fi_cxd5605_position_accumulator__handle_fix_report] Publishing report with 30 breadcrumbs
```
- [x] HTTP modem actor error is not propergated to HSM ✅ 2024-04-26

**2024-04-22**
So with respect to the retained stats counter feature, one of the issue that came up was that when to reset the retained stats counter since the counter values are always retained it will just always increment and while not really an issue it does increase the encoded protobuf size. So while on the train, I spend some time thinking and maybe we can do similar thing with it as we do with rlogs, where we only clear rlogs that was transmitted on success report response. We can do something similar with stats counter, occasionally "rebase" the stats counter values with the stats value that was just transmitted. We currently have `void counter_populate_sysstats(submission_SysStats *sysstats);` we will add new `void counter_rebase_sysstats(submission_SysStats *sysstats);`.

In addition we are adding a meta data "session key" for sys stats, that indicate the counter values have reset, hence the backend should treat these values as is, instead of delta from previous stats counter block.
also currently the `SysStats` are strictly only a struct that contain integers, since we have macros that depend on it. This prevent adding meta data fields to the `SysStats` and sending the meta data separately seem messy. Maybe we can update the `SysStat` message to something like
```
message DeviceStat {
    message Fields {
      ... counters
    };

    message Metadata {
     ...
    };

  Metadata meta_data = 1;
  Fields fields = 2;
}
```

**2024-04-21**
Y: making few LTE operations async, to fix CXD5605 timeout
T: doing more testing to make sure cxd5605 timeout doesn’t occur as often.

**2024-04-16**
Y: Start fixing long blocking calls, in wifi scan
T: Addressing LTE operations async, to fix CXD5605 timeout

**2024-04-15**
Conditions for CXD5605 timeout
- Faster periodic check timer
- Faster WIFI scanning every 2mins

```
00:10:15.327 I [fi_location_actor__handle_position_fix_report_with_breadcrumbs] GNSS fix(521 sec): A GOOD 2
00:10:15.331 I [utc_wallclock_set_timeofday_tm] clock: set time of day tm
00:10:15.331 I [utc_wallclock_sync] Syncing UTC clock
00:10:15.339 I [fi_cxd5605_gnss_server_position_hint] Position hint: 423924256 -711080320 424
00:10:18.279 D [fi_ble_log_state] fully attached
00:10:18.282 I [power_check_battery_charger] Battery: state 3, bq25180_stat0:0x61, is_chg:0 has_pwr:1 on_base:0 has_power_supply=1
00:10:18.282 I [module_hsm_log_state] T1=-1s T2=-1s T3=-1s State=[ ble-connection, ble:idle ]
00:10:18.570 D [fi_motion_detection_get_state] activity threshold 0.000006 3s
00:18:51.268 W [fi_location_actor__check_state_timeout] TIMEOUT: POSITIONING!!!
00:18:51.268 I [fi_cxd5605_gnss_server__set_goal] goal change: POSITION FIX -> DISABLE
00:18:51.269 I [fi_cxd5605_gnss_server__set_goal] gnss g 1:4 s 5
00:18:51.270 D [fi_remote_log_add] Added remote log: 12
00:18:51.271 I [fi_location_actor__set_state] POSITIONING -> GNSS_STOPPING
00:18:51.272 D [fi_remote_log_add] Added remote log: 22
00:18:51.273 I [brain__log_state] Current backhaul BLE next report due in -498 sec.
00:18:51.273 I [module_hsm_send_event] REPORT_IS_DUE
00:18:51.273 I [evaluate_transition_targets] -> 'ble:submit-report', condition 'none'
00:18:51.274 I [hsm_instance_transition] moving to state: ble:submit-report
00:18:51.274 I [transition_to_path] ble:submit-report
00:18:51.274 I [pop_state] Exiting ble:idle
00:18:51.275 I [push_state] Entering ble:submit-report
00:18:51.281 I [push_state] ble_notify_dispatch_and_submit_report
00:18:51.281 I [fi_submission_server__set_state] IDLE -> IDLE
00:18:51.282 D [fi_remote_log_add] Added remote log: 22
00:18:51.292 I [fi_submission_server__set_state] IDLE -> IDLE
00:18:51.294 D [fi_remote_log_add] Added remote log: 22
00:18:51.294 I [fi_location_actor_get_report] Generating location info: gnss report state=1, backhaul=BLE, live_tracking=1 lt_state=1
00:18:51.305 W [encode_proto_basicinfo] bq27421 not refreshed, skipping report sub-message
00:18:51.341 D [encode_proto_activity] Encoded 1 activity records, last seq=9
00:18:51.342 D [append_remote_log_section] Encoded 391 bytes of rlogs (3857 end)
00:18:51.344 D [submission_data_prepare] Prepared report body (3864 bytes long): sd
0gEKzwE
00:18:51.344 I [fi_ble_send_report] Sending report: 3864 bytes
00:18:51.345 D [brain_consume_event] SENT_REPORT
00:18:51.345 I [push_state] start_timer
00:18:51.345 I [_act_impl_start_timer] Starting HSM timer -- 60000 ms
00:18:51.347 D [fi_remote_log_add] Added remote log: 7
00:18:51.354 E [main]  Main loop TOOK 512094 ms
00:18:51.356 D [fi_remote_log_add] Added remote log: 12
00:18:51.356 I [utc_wallclock_sync] Syncing UTC clock
00:18:51.372 I [fi_cxd5605_gnss_server__stop_positioning] 1131s/7200s elapsed, not backing up
00:18:51.372 I [fi_cxd5605_gnss_server__set_state] state change: POSITIONING -> STOPPING
```

**2024-04-12**
Y: trying to understand the CXD5605 timeout issue more, and testing new CXD5605 FW  
T: Try to figure out where the long blocking call is in modem module. and try to make things async.
```
00:01:45.994 D [fi_modem_actor__event_handler] evt: 7
00:01:47.199 D [fi_nrf9160_modem_msg_proc] !!20!!
00:01:47.199 D [fi_nrf9160_modem_msg_proc] socket read ready for 1
00:01:47.200 D [fi_modem_actor_poll__process_msg] topic(309)
00:01:47.207 E [fi_nrf9160_modem_modemlink_send_message_sync]  sync TOOK 7 ms
00:01:47.208 D [fi_remote_log_add] Added remote log: 12
00:01:47.209 D [http_parser_on_message_begin] HTTP Parser: on_message_begin
00:01:47.209 D [http_parser_on_status] HTTP status code: 200
00:01:47.212 I [utc_wallclock_set_timeofday_tm] clock: set time of day tm
00:01:47.213 I [utc_wallclock_sync] Syncing UTC clock
00:01:47.228 E [fi_nrf9160_modem_modemlink_send_message_sync]  sync TOOK 7 ms
00:01:47.229 D [fi_remote_log_add] Added remote log: 12
00:01:47.230 D [http_parser_on_headers_complete] HTTP Parser: on_headers_complete
00:01:47.230 I [fi_submission_server__set_state] IDLE -> RECV_RESP
00:01:47.232 D [fi_remote_log_add] Added remote log: 22
00:01:47.238 E [fi_nrf9160_modem_modemlink_send_message_sync]  sync TOOK 6 ms
00:01:47.240 D [fi_remote_log_add] Added remote log: 12
00:01:47.241 I [fi_remote_log_drop] Clearing remote logs before: 0
00:01:47.241 I [fi_submission_server__process_basic_response] update_report_interval: 60s
00:01:47.242 I [fi_submission_server__process_basic_response] update_no_activity_interval: 60s
00:01:47.242 I [fi_submission_server__process_basic_response] Updating:47.412 I [fi_submission_server__process_basic_response] Updating remote logging enabled to: 1
00:01:47.412 I [fi_submission_server__process_basic_response] Updating live tracking wifi scan interval to: 0
00:01:47.413 I [fi_cxd5605_gnss_server_position_hint] Position hint: 423925696 -711079552 0
00:01:47.413 I [fi_submission_server__process_basic_response] update_gnss_sat_systems_selection: 3s
00:01:47.414 I [fi_cxd5605_gnss_server_update_sat_systems] Update sat systems to 0x3
00:01:47.429 E [fi_nrf9160_modem_modemlink_send_message_sync]  sync TOOK 6 ms
00:01:47.431 D [fi_remote_log_add] Added remote log: 12
00:01:47.431 D [fi_modem_actor__event_handler] evt: 8
00:01:47.434 D [fi_modem_actor_poll__process_msg] topic(310)
00:01:47.435 D [fi_modem_actor__request_handler] Request (2)
00:01:47.435 I [fi_modem_actor__set_state] state change: DOWNLOAD -> PENDING
00:01:47.447 D [fi_remote_log_add] Added remote log: 22
00:01:47.457 E [main]  Main loop TOOK 257 ms
00:01:47.459 D [fi_remote_log_add] Added remote log: 12
00:01:47.459 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:01:47.459 I [evaluate_transition_targets] -> '', condition 'none'
00:01:47.468 I [hsm_instance_transition] null transition
```

**2024-04-10**
- [x] Figure out JB's bug where CXD5605 stopped sending data ✅ 2024-04-16
- [x] Fix LLE injection with location actor ✅ 2024-04-11
- [x] Fix gnss_server.c:117 crash ✅ 2024-04-16
- [x] Somehow WIFI LLE injection is broken? ✅ 2024-05-06
- [x] Mobile report sending a lot repeat report/stats counters? ✅ 2024-06-17
- [x] Need to figure out why mobile report don't have gnss section for me, but does for units in the field ✅ 2024-04-16
- [x] LLE is enabled for mobile? ✅ 2024-05-06
- [x] Help field theory CXD5605term issue? ✅ 2024-04-16

**2024-04-09**
```
00:33:43.673 D [brain_consume_event] SENT_REPORT
00:33:43.676 I [module_hsm_send_event] LTE_NET_READY
00:33:43.676 I [evaluate_transition_targets] -> '', condition 'none'
00:33:43.676 I [hsm_instance_transition] null transition
00:33:43.678 D [fi_remote_log_add] Added remote log: 7
00:33:43.688 D [http_modem_event_handler] Socket(0)
00:33:43.688 I [fi_modem_actor__set_goal] goal change: READY -> UPLOAD_DATA ; state: PENDING
00:33:43.689 I [fi_modem_actor__set_state] state change: PENDING -> UPLOAD
00:33:43.690 D [fi_remote_log_add] Added remote log: 22
00:33:43.691 I [fi_cxd5605_flow_start_positioning_poll] CXD5605 start positioning: success
00:33:43.714 I [fi_nrf9160_logger_handle_modemlink_msg] Sleep exit: LTE_LC_MODEM_SLEEP_RF_INACTIVITY(2)
00:33:43.841 I [fi_nrf9160_logger_handle_modemlink_msg] RRC status: LTE_LC_RRC_MODE_CONNECTED (1)
00:33:44.160 I [fi_modem_actor__set_state] state change: UPLOAD -> DOWNLOAD
00:33:44.161 D [fi_remote_log_add] Added remote log: 22
00:33:44.164 E [lis2dw12_poll] lis2dw12 lost samples in fifo
00:33:44.165 W [fi_accel_dispatch_actor_poll] lost accel samples, flushing store
00:33:44.165 W [fi_lick_classify_actor__process_samples] accel samples dropped, reporting gap
00:33:44.362 D [http_modem_event_handler] Socket(1)
00:33:44.363 D [http_modem_event_handler] MODEM_EVT_SOCKET_WRITE_READY
00:33:44.389 D [http_modem_event_handler] Socket(1)
00:33:44.389 D [http_modem_event_handler] MODEM_EVT_SOCKET_WRITE_READY
00:33:44.407 D [http_modem_event_handler] Socket(1)
00:33:44.407 D [http_modem_event_handler] MODEM_EVT_SOCKET_WRITE_READY
00:33:44.425 D [http_modem_event_handler] Socket(1)
00:33:44.425 D [http_modem_event_handler] MODEM_EVT_SOCKET_WRITE_READY
00:33:46.588 D [fi_cxd5605_position_accumulator__handle_fix_report] Publishing report with 0 breadcrumbs
00:33:46.676 I [fi_location_actor__set_state] STARTING_POSITION -> POSITIONING
00:33:46.678 D [fi_remote_log_add] Added remote log: 22
00:33:46.678 I [fi_location_actor__handle_position_fix_report_with_breadcrumbs] GNSS fix(0 sec): N NONE 1
00:33:46.845 D [http_modem_event_handler] Socket(1)
00:33:46.845 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:46.852 D [http_parser_on_message_begin] HTTP Parser: on_message_begin
00:33:46.852 D [http_parser_on_status] HTTP status code: 200
00:33:46.856 I [utc_wallclock_set_timeofday_tm] clock: set time of day tm
00:33:46.856 I [utc_wallclock_sync] Syncing UTC clock
00:33:46.871 D [http_parser_on_headers_complete] HTTP Parser: on_headers_complete
00:33:46.871 I [fi_submission_server__set_state] IDLE -> RECV_RESP
00:33:46.873 D [fi_remote_log_add] Added remote log: 22
00:33:46.880 I [fi_remote_log_drop] Clearing remote logs before: 1154
00:33:46.880 I [fi_submission_server__process_basic_response] update_report_interval: 300s
00:33:46.881 I [fi_submission_server__process_basic_response] update_no_activity_interval: 3600s
00:33:46.881 I [fi_submission_server__process_basic_response] Updating led state to: 0 s
00:33:46.881 I [set_led_pattern] Disabling LED
00:33:46.882 I [fi_submission_server__process_basic_response] Updating led off after duration to: 0 s
00:33:46.886 I [fi_submission_server__process_basic_response] Live tracking: 0
00:33:46.886 I [fi_submission_server__process_basic_response] eDRX + LTE/WS: 1
00:33:46.887 I [fi_submission_server__process_basic_response] Updating remote logging enabled to: 1
00:33:46.887 I [fi_submission_server__process_basic_response] Updating live tracking wifi scan interval to: 0
00:33:46.887 I [fi_cxd5605_gnss_server_position_hint] Position hint: 423925088 -711079040 0
00:33:46.889 I [fi_submission_server__process_basic_response] update_gnss_sat_systems_selection: 3s
00:33:46.890 I [fi_cxd5605_gnss_server_update_sat_systems] Update sat systems to 0x3
00:33:46.890 I [fi_submission_server__set_state] RECV_RESP -> RECV_LLE
00:33:46.896 D [fi_remote_log_add] Added remote log: 22
00:33:46.902 I [fi_cxd5605_gnss_server__set_goal] goal change: POSITION FIX -> LLE INJECTION
00:33:46.903 I [fi_cxd5605_gnss_server__set_goal] gnss g 1:2 s 6
00:33:46.904 D [fi_remote_log_add] Added remote log: 12
00:33:46.995 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:46.995 I [evaluate_transition_targets] -> '', condition 'none'
00:33:46.995 I [hsm_instance_transition] null transition
00:33:46.995 I [run_transition_actions] start_timer
00:33:46.996 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:46.997 D [fi_remote_log_add] Added remote log: 7
00:33:46.998 I [fi_cxd5605_gnss_server__stop_positioning] 2026s/7200s elapsed, not backing up
00:33:46.998 I [fi_cxd5605_gnss_server__set_state] state change: POSITIONING -> STOPPING
00:33:47.000 D [fi_remote_log_add] Added remote log: 22
00:33:47.084 D [fi_cxd5605_flow_stop_positioning__set_state] GSTP => SLEEP
00:33:47.197 D [http_modem_event_handler] Socket(1)
00:33:47.197 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:47.424 E [lis2dw12_poll] lis2dw12 lost samples in fifo
00:33:47.424 W [fi_accel_dispatch_actor_poll] lost accel samples, flushing store
00:33:47.424 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:47.425 I [evaluate_transition_targets] -> '', condition 'none'
00:33:47.425 I [hsm_instance_transition] null transition
00:33:47.425 I [run_transition_actions] start_timer
00:33:47.425 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:47.427 D [fi_remote_log_add] Added remote log: 7
00:33:47.428 W [fi_lick_classify_actor__process_samples] accel samples dropped, reporting gap
00:33:47.428 D [http_modem_event_handler] Socket(1)
00:33:47.429 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:47.475 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:47.475 I [evaluate_transition_targets] -> '', condition 'none'
00:33:47.475 I [hsm_instance_transition] null transition
00:33:47.475 I [run_transition_actions] start_timer
00:33:47.476 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:47.477 D [fi_remote_log_add] Added remote log: 7
00:33:47.478 D [http_modem_event_handler] Socket(1)
00:33:47.478 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:47.563 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:47.563 I [evaluate_transition_targets] -> '', condition 'none'
00:33:47.563 I [hsm_instance_transition] null transition
00:33:47.564 I [run_transition_actions] start_timer
00:33:47.564 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:47.566 D [fi_remote_log_add] Added remote log: 7
00:33:47.566 D [http_modem_event_handler] Socket(1)
00:33:47.567 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:47.724 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:47.724 I [evaluate_transition_targets] -> '', condition 'none'
00:33:47.724 I [hsm_instance_transition] null transition
00:33:47.725 I [run_transition_actions] start_timer
00:33:47.725 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:47.727 D [fi_remote_log_add] Added remote log: 7
00:33:47.727 I [fi_cxd5605_frontend_log_status] boot=H recover=U enabled=1 error=0 tcxo=1 pos=0 lle=1 fw=<20107,1059ebf,123E>
2024 04 05 00 00  3
0
2024 04 05 00 00  3
2023 12 15 00 00  3
0
00:33:47.728 I [fi_cxd5605_gnss_server__set_state] state change: STOPPING -> AWAITING LLE
00:33:47.730 D [fi_remote_log_add] Added remote log: 22
00:33:47.924 D [http_modem_event_handler] Socket(1)
00:33:47.924 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:48.156 I [fi_submission_server__set_state] RECV_LLE -> INJECT_LLE
00:33:48.158 D [fi_remote_log_add] Added remote log: 22
00:33:48.164 I [fi_modem_actor__set_state] state change: DOWNLOAD -> PENDING
00:33:48.166 D [fi_remote_log_add] Added remote log: 22
00:33:48.167 E [lis2dw12_poll] lis2dw12 lost samples in fifo
00:33:48.167 W [fi_accel_dispatch_actor_poll] lost accel samples, flushing store
00:33:48.167 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:48.168 I [evaluate_transition_targets] -> '', condition 'none'
00:33:48.168 I [hsm_instance_transition] null transition
00:33:48.168 I [run_transition_actions] start_timer
00:33:48.169 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:48.170 D [fi_remote_log_add] Added remote log: 7
00:33:48.171 I [fi_cxd5605_gnss_server__set_state] state change: AWAITING LLE -> INJECTING LLE
00:33:48.172 D [fi_remote_log_add] Added remote log: 22
00:33:48.175 W [fi_lick_classify_actor__process_samples] accel samples dropped, reporting gap
00:33:48.410 D [fi_ble_log_state] not connected and advertising
00:33:48.412 I [power_check_battery_charger] Battery: state 0, bq25180_stat0:0x00, is_chg:0 has_pwr:0 on_base:0 has_power_supply=0
00:33:48.412 I [module_hsm_log_state] T1=19s T2=-1s T3=-1s State=[ lte-connection, lte:send-report ]
00:33:51.760 I [fi_nrf9160_logger_handle_modemlink_msg] RRC status: LTE_LC_RRC_MODE_IDLE (0)
00:33:52.044 E [fi_cxd5605_flow_inject_lle_poll] cxd5605: lle injection CEPW failure -22
00:33:52.045 E [fi_cxd5605_poll__flow] CXD5605 flow 3 error -22, disabling
00:33:53.758 I [bq27421_print_cached_values]   Design Parameters: capacity=265mAh energy=1007mWh
  Device Type: 0x0421
  Chem ID: 0x0312
  Control_Status 1: rsvd_1=0 vok=1 rup_dis=0 ldmd=1 sleep=1 rsvd_2=0 hibernate=0 initcomp=1
  Control Status 2: res_up=0 qmax_up=0 bca=0 cca=0 calmode=0 ss=0 wdreset=0 shutdownen=0
  Flags 1: dsg=1 socf=0 soc1=0 bat_det=1 cfgupmode=0 itpor=0 rsvd_1=0 ocvtaken=1
  Flags 2: chg=1 fc=0 rsvd_2=0 ut=0 ot=0
  Voltage: 4065mV
  Average Current: -17mAh
  Average Power: -170mWh
  State of Charge: 83%
  State of Health: 92% (status 1)
  Temperature: 2953
  Remaining Capacity:  205mAh
  Full-Charge Capacity: 249mAh
  Nominal Available Capacity: 212mAh
  Remaining Capacity: unfiltered=205mAh filtered=205mAh
  Full-Charge Capacity: unfiltered=249mAh filtered=249mAh
  State of Charge (unfiltered): 83%
  Learning: Qmax=16384 Ra=[8 9 11 13 11 10 11 11 11 12 13 16 26 52 199]
00:33:53.762 I [bq27421_refresh_state_update] Refresh success, next in 60000ms
00:33:54.313 I [fi_cxd5605_frontend_log_status] boot=H recover=U enabled=0 error=0 tcxo=1 pos=0 lle=1 fw=<20107,1059ebf,123E>
2024 04 05 00 00  3
0
2024 04 05 00 00  3
2023 12 15 00 00  3
0
00:33:54.314 I [fi_cxd5605_gnss_server__set_state] state change: INJECTING LLE -> AWAITING LLE
00:33:54.316 D [fi_remote_log_add] Added remote log: 22
00:33:54.316 E [fi_location_actor__process_msg] CXD5605 unexpectedly disabled!
00:33:54.316 I [fi_location_actor__set_state] POSITIONING -> PUBLISH_FIX
00:33:54.318 D [fi_remote_log_add] Added remote log: 22
00:33:54.318 I [fi_location_actor__set_state] PUBLISH_FIX -> IDLE
00:33:54.320 D [fi_remote_log_add] Added remote log: 22
00:33:54.443 E [fi_submission_server__process_msg] LLE inject fail
00:33:54.444 D [fi_remote_log_add] Added remote log: 12
00:33:54.445 I [fi_cxd5605_gnss_server__set_state] state change: AWAITING LLE -> AFTER LLE
00:33:54.446 D [fi_remote_log_add] Added remote log: 22
00:33:54.447 I [fi_cxd5605_gnss_server__set_goal] goal change: LLE INJECTION -> DISABLE
00:33:54.447 I [fi_cxd5605_gnss_server__set_goal] gnss g 2:4 s 5
00:33:54.448 D [fi_remote_log_add] Added remote log: 12
00:33:54.449 I [fi_submission_server__set_state] INJECT_LLE -> RECV_RESP
00:33:54.450 D [fi_remote_log_add] Added remote log: 22
00:33:54.451 I [fi_submission_server__set_state] RECV_RESP -> COMPLETE
00:33:54.452 D [fi_remote_log_add] Added remote log: 22
00:33:54.453 E [handle_failed_assert] ASSERT FAIL: "(gs->state == FI_CXD5605_GNSS_SERVER_STATE_DISABLED) || (gs->state == FI_CXD
```

```
00:02:38.383 D [fi_ble_log_state] connected and pending
00:02:38.385 I [power_check_battery_charger] Battery: state 3, bq25180_stat0:0x61, is_chg:0 has_pwr:1 on_base:0 has_power_supply=1
00:02:38.385 I [module_hsm_log_state] T1=-1s T2=-1s T3=-1s State=[ run-wifi, wifi:connected, wifi-connected:idle ]
00:02:39.171 W [counter_timer_stop] Unbalanced stop for counter: 98
00:02:39.171 I [module_hsm_send_event] BLE_CONNECT
00:02:39.171 I [evaluate_transition_targets] -> 'no-connection', condition 'none'
00:02:39.172 I [hsm_instance_transition] moving to state: no-connection
00:02:39.172 I [transition_to_path] no-connection
00:02:39.172 I [pop_state] Exiting wifi-connected:idle
00:02:39.173 I [pop_state] Exiting wifi:connected
00:02:39.173 I [pop_state] Running exit action: report_disconnected_from_stable
00:02:39.173 I [pop_state] Exiting run-wifi
00:02:39.174 W [counter_timer_stop] Unbalanced stop for counter: 26
00:02:39.174 I [pop_state] Running exit action: set_ble_postponed_attachment
00:02:39.174 I [pop_state] Running exit action: wifi_stop
00:02:39.175 D [da16200_drv_set_wake_mode] da16200_drv_set_wake_mode: booting
00:11:11.193 E [da16200_phy__boot_poll] da16200_phy__boot_poll: boot timeout
00:11:11.194 E [fi_da16200_sync_acquire] fi_da16200_sync_acquire: acquire timeout 512010/15000ms
00:11:11.194 E [fi_da16200_sync_acquire] init_da16200_acquire: failed!
00:11:11.195 D [_act_impl_wifi_stop] not connected / acquire failed, sleep 1
00:11:11.195 D [fiwifi_client_stop_remain_assoc_time] stopping
00:11:11.196 I [fiwifi_parser_reset] fiwifi_parser_reset
00:11:11.206 D [brain_consume_event] WIFI_STOP
00:11:11.207 I [push_state] Entering no-connection
00:11:11.207 I [push_state] start_timer
00:11:11.207 I [_act_impl_start_timer] Starting HSM timer -- 5000 ms
00:11:11.218 I [push_state] check_is_report_due
00:11:11.219 D [fi_remote_log_add] Added remote log: 7
00:11:11.220 I [utc_wallclock_sync] Syncing UTC clock
00:11:11.237 E [handle_failed_assert] ASSERT FAIL: "actual_radio_event_percentage > 0.2f radio: 166/1098 events" file "../../src/nrf52/fi_module/fi_ble.c", line 917

00:11:11.238 W [fatal_error] Failed boot count 00:00:00.020 ! [log_module_details] fi_module board=3 build=0.0.0-local-fc3_f3-dev platform_id=<null> module_id=FC32H000328
00:00:00.021 ! [log_module_details] BL Ver: 0.0.0-local-fc3_f3-dev-bl
```



**2024-04-10**
- [x] Figure out JB's bug where CXD5605 stopped sending data ✅ 2024-04-10
- [x] Fix LLE injection with location actor ✅ 2024-04-16
    - Still need to fix location actor restarting the gnss after failed cxd5605
- [x] Fix gnss_server.c:117 crash ✅ 2024-04-16
- [x] Verify Dev bl vs Prod BL build path and version set ✅ 2024-07-09
- [x] Try the new CXD5605 FW ✅ 2024-05-06
- [x] so....this seems a little crazy this issue is back somehow on my PR only, maybe I changed something with alignment? https://github.com/barkinglabs/firmware/actions/runs/8640678899/job/23689373277?pr=1772 ✅ 2024-04-16

**2024-04-09**
```
00:33:43.673 D [brain_consume_event] SENT_REPORT
00:33:43.676 I [module_hsm_send_event] LTE_NET_READY
00:33:43.676 I [evaluate_transition_targets] -> '', condition 'none'
00:33:43.676 I [hsm_instance_transition] null transition
00:33:43.678 D [fi_remote_log_add] Added remote log: 7
00:33:43.688 D [http_modem_event_handler] Socket(0)
00:33:43.688 I [fi_modem_actor__set_goal] goal change: READY -> UPLOAD_DATA ; state: PENDING
00:33:43.689 I [fi_modem_actor__set_state] state change: PENDING -> UPLOAD
00:33:43.690 D [fi_remote_log_add] Added remote log: 22
00:33:43.691 I [fi_cxd5605_flow_start_positioning_poll] CXD5605 start positioning: success
00:33:43.714 I [fi_nrf9160_logger_handle_modemlink_msg] Sleep exit: LTE_LC_MODEM_SLEEP_RF_INACTIVITY(2)
00:33:43.841 I [fi_nrf9160_logger_handle_modemlink_msg] RRC status: LTE_LC_RRC_MODE_CONNECTED (1)
00:33:44.160 I [fi_modem_actor__set_state] state change: UPLOAD -> DOWNLOAD
00:33:44.161 D [fi_remote_log_add] Added remote log: 22
00:33:44.164 E [lis2dw12_poll] lis2dw12 lost samples in fifo
00:33:44.165 W [fi_accel_dispatch_actor_poll] lost accel samples, flushing store
00:33:44.165 W [fi_lick_classify_actor__process_samples] accel samples dropped, reporting gap
00:33:44.362 D [http_modem_event_handler] Socket(1)
00:33:44.363 D [http_modem_event_handler] MODEM_EVT_SOCKET_WRITE_READY
00:33:44.389 D [http_modem_event_handler] Socket(1)
00:33:44.389 D [http_modem_event_handler] MODEM_EVT_SOCKET_WRITE_READY
00:33:44.407 D [http_modem_event_handler] Socket(1)
00:33:44.407 D [http_modem_event_handler] MODEM_EVT_SOCKET_WRITE_READY
00:33:44.425 D [http_modem_event_handler] Socket(1)
00:33:44.425 D [http_modem_event_handler] MODEM_EVT_SOCKET_WRITE_READY
00:33:46.588 D [fi_cxd5605_position_accumulator__handle_fix_report] Publishing report with 0 breadcrumbs
00:33:46.676 I [fi_location_actor__set_state] STARTING_POSITION -> POSITIONING
00:33:46.678 D [fi_remote_log_add] Added remote log: 22
00:33:46.678 I [fi_location_actor__handle_position_fix_report_with_breadcrumbs] GNSS fix(0 sec): N NONE 1
00:33:46.845 D [http_modem_event_handler] Socket(1)
00:33:46.845 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:46.852 D [http_parser_on_message_begin] HTTP Parser: on_message_begin
00:33:46.852 D [http_parser_on_status] HTTP status code: 200
00:33:46.856 I [utc_wallclock_set_timeofday_tm] clock: set time of day tm
00:33:46.856 I [utc_wallclock_sync] Syncing UTC clock
00:33:46.871 D [http_parser_on_headers_complete] HTTP Parser: on_headers_complete
00:33:46.871 I [fi_submission_server__set_state] IDLE -> RECV_RESP
00:33:46.873 D [fi_remote_log_add] Added remote log: 22
00:33:46.880 I [fi_remote_log_drop] Clearing remote logs before: 1154
00:33:46.880 I [fi_submission_server__process_basic_response] update_report_interval: 300s
00:33:46.881 I [fi_submission_server__process_basic_response] update_no_activity_interval: 3600s
00:33:46.881 I [fi_submission_server__process_basic_response] Updating led state to: 0 s
00:33:46.881 I [set_led_pattern] Disabling LED
00:33:46.882 I [fi_submission_server__process_basic_response] Updating led off after duration to: 0 s
00:33:46.886 I [fi_submission_server__process_basic_response] Live tracking: 0
00:33:46.886 I [fi_submission_server__process_basic_response] eDRX + LTE/WS: 1
00:33:46.887 I [fi_submission_server__process_basic_response] Updating remote logging enabled to: 1
00:33:46.887 I [fi_submission_server__process_basic_response] Updating live tracking wifi scan interval to: 0
00:33:46.887 I [fi_cxd5605_gnss_server_position_hint] Position hint: 423925088 -711079040 0
00:33:46.889 I [fi_submission_server__process_basic_response] update_gnss_sat_systems_selection: 3s
00:33:46.890 I [fi_cxd5605_gnss_server_update_sat_systems] Update sat systems to 0x3
00:33:46.890 I [fi_submission_server__set_state] RECV_RESP -> RECV_LLE
00:33:46.896 D [fi_remote_log_add] Added remote log: 22
00:33:46.902 I [fi_cxd5605_gnss_server__set_goal] goal change: POSITION FIX -> LLE INJECTION
00:33:46.903 I [fi_cxd5605_gnss_server__set_goal] gnss g 1:2 s 6
00:33:46.904 D [fi_remote_log_add] Added remote log: 12
00:33:46.995 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:46.995 I [evaluate_transition_targets] -> '', condition 'none'
00:33:46.995 I [hsm_instance_transition] null transition
00:33:46.995 I [run_transition_actions] start_timer
00:33:46.996 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:46.997 D [fi_remote_log_add] Added remote log: 7
00:33:46.998 I [fi_cxd5605_gnss_server__stop_positioning] 2026s/7200s elapsed, not backing up
00:33:46.998 I [fi_cxd5605_gnss_server__set_state] state change: POSITIONING -> STOPPING
00:33:47.000 D [fi_remote_log_add] Added remote log: 22
00:33:47.084 D [fi_cxd5605_flow_stop_positioning__set_state] GSTP => SLEEP
00:33:47.197 D [http_modem_event_handler] Socket(1)
00:33:47.197 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:47.424 E [lis2dw12_poll] lis2dw12 lost samples in fifo
00:33:47.424 W [fi_accel_dispatch_actor_poll] lost accel samples, flushing store
00:33:47.424 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:47.425 I [evaluate_transition_targets] -> '', condition 'none'
00:33:47.425 I [hsm_instance_transition] null transition
00:33:47.425 I [run_transition_actions] start_timer
00:33:47.425 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:47.427 D [fi_remote_log_add] Added remote log: 7
00:33:47.428 W [fi_lick_classify_actor__process_samples] accel samples dropped, reporting gap
00:33:47.428 D [http_modem_event_handler] Socket(1)
00:33:47.429 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:47.475 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:47.475 I [evaluate_transition_targets] -> '', condition 'none'
00:33:47.475 I [hsm_instance_transition] null transition
00:33:47.475 I [run_transition_actions] start_timer
00:33:47.476 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:47.477 D [fi_remote_log_add] Added remote log: 7
00:33:47.478 D [http_modem_event_handler] Socket(1)
00:33:47.478 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:47.563 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:47.563 I [evaluate_transition_targets] -> '', condition 'none'
00:33:47.563 I [hsm_instance_transition] null transition
00:33:47.564 I [run_transition_actions] start_timer
00:33:47.564 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:47.566 D [fi_remote_log_add] Added remote log: 7
00:33:47.566 D [http_modem_event_handler] Socket(1)
00:33:47.567 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:47.724 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:47.724 I [evaluate_transition_targets] -> '', condition 'none'
00:33:47.724 I [hsm_instance_transition] null transition
00:33:47.725 I [run_transition_actions] start_timer
00:33:47.725 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:47.727 D [fi_remote_log_add] Added remote log: 7
00:33:47.727 I [fi_cxd5605_frontend_log_status] boot=H recover=U enabled=1 error=0 tcxo=1 pos=0 lle=1 fw=<20107,1059ebf,123E>
2024 04 05 00 00  3
0
2024 04 05 00 00  3
2023 12 15 00 00  3
0
00:33:47.728 I [fi_cxd5605_gnss_server__set_state] state change: STOPPING -> AWAITING LLE
00:33:47.730 D [fi_remote_log_add] Added remote log: 22
00:33:47.924 D [http_modem_event_handler] Socket(1)
00:33:47.924 D [http_modem_event_handler] MODEM_EVT_SOCKET_READ_READY
00:33:48.156 I [fi_submission_server__set_state] RECV_LLE -> INJECT_LLE
00:33:48.158 D [fi_remote_log_add] Added remote log: 22
00:33:48.164 I [fi_modem_actor__set_state] state change: DOWNLOAD -> PENDING
00:33:48.166 D [fi_remote_log_add] Added remote log: 22
00:33:48.167 E [lis2dw12_poll] lis2dw12 lost samples in fifo
00:33:48.167 W [fi_accel_dispatch_actor_poll] lost accel samples, flushing store
00:33:48.167 I [module_hsm_send_event] REPORT_RESPONSE_EXTEND
00:33:48.168 I [evaluate_transition_targets] -> '', condition 'none'
00:33:48.168 I [hsm_instance_transition] null transition
00:33:48.168 I [run_transition_actions] start_timer
00:33:48.169 I [_act_impl_start_timer] Starting HSM timer -- 20000 ms
00:33:48.170 D [fi_remote_log_add] Added remote log: 7
00:33:48.171 I [fi_cxd5605_gnss_server__set_state] state change: AWAITING LLE -> INJECTING LLE
00:33:48.172 D [fi_remote_log_add] Added remote log: 22
00:33:48.175 W [fi_lick_classify_actor__process_samples] accel samples dropped, reporting gap
00:33:48.410 D [fi_ble_log_state] not connected and advertising
00:33:48.412 I [power_check_battery_charger] Battery: state 0, bq25180_stat0:0x00, is_chg:0 has_pwr:0 on_base:0 has_power_supply=0
00:33:48.412 I [module_hsm_log_state] T1=19s T2=-1s T3=-1s State=[ lte-connection, lte:send-report ]
00:33:51.760 I [fi_nrf9160_logger_handle_modemlink_msg] RRC status: LTE_LC_RRC_MODE_IDLE (0)
00:33:52.044 E [fi_cxd5605_flow_inject_lle_poll] cxd5605: lle injection CEPW failure -22
00:33:52.045 E [fi_cxd5605_poll__flow] CXD5605 flow 3 error -22, disabling
00:33:53.758 I [bq27421_print_cached_values]   Design Parameters: capacity=265mAh energy=1007mWh
  Device Type: 0x0421
  Chem ID: 0x0312
  Control_Status 1: rsvd_1=0 vok=1 rup_dis=0 ldmd=1 sleep=1 rsvd_2=0 hibernate=0 initcomp=1
  Control Status 2: res_up=0 qmax_up=0 bca=0 cca=0 calmode=0 ss=0 wdreset=0 shutdownen=0
  Flags 1: dsg=1 socf=0 soc1=0 bat_det=1 cfgupmode=0 itpor=0 rsvd_1=0 ocvtaken=1
  Flags 2: chg=1 fc=0 rsvd_2=0 ut=0 ot=0
  Voltage: 4065mV
  Average Current: -17mAh
  Average Power: -170mWh
  State of Charge: 83%
  State of Health: 92% (status 1)
  Temperature: 2953
  Remaining Capacity:  205mAh
  Full-Charge Capacity: 249mAh
  Nominal Available Capacity: 212mAh
  Remaining Capacity: unfiltered=205mAh filtered=205mAh
  Full-Charge Capacity: unfiltered=249mAh filtered=249mAh
  State of Charge (unfiltered): 83%
  Learning: Qmax=16384 Ra=[8 9 11 13 11 10 11 11 11 12 13 16 26 52 199]
00:33:53.762 I [bq27421_refresh_state_update] Refresh success, next in 60000ms
00:33:54.313 I [fi_cxd5605_frontend_log_status] boot=H recover=U enabled=0 error=0 tcxo=1 pos=0 lle=1 fw=<20107,1059ebf,123E>
2024 04 05 00 00  3
0
2024 04 05 00 00  3
2023 12 15 00 00  3
0
00:33:54.314 I [fi_cxd5605_gnss_server__set_state] state change: INJECTING LLE -> AWAITING LLE
00:33:54.316 D [fi_remote_log_add] Added remote log: 22
00:33:54.316 E [fi_location_actor__process_msg] CXD5605 unexpectedly disabled!
00:33:54.316 I [fi_location_actor__set_state] POSITIONING -> PUBLISH_FIX
00:33:54.318 D [fi_remote_log_add] Added remote log: 22
00:33:54.318 I [fi_location_actor__set_state] PUBLISH_FIX -> IDLE
00:33:54.320 D [fi_remote_log_add] Added remote log: 22
00:33:54.443 E [fi_submission_server__process_msg] LLE inject fail
00:33:54.444 D [fi_remote_log_add] Added remote log: 12
00:33:54.445 I [fi_cxd5605_gnss_server__set_state] state change: AWAITING LLE -> AFTER LLE
00:33:54.446 D [fi_remote_log_add] Added remote log: 22
00:33:54.447 I [fi_cxd5605_gnss_server__set_goal] goal change: LLE INJECTION -> DISABLE
00:33:54.447 I [fi_cxd5605_gnss_server__set_goal] gnss g 2:4 s 5
00:33:54.448 D [fi_remote_log_add] Added remote log: 12
00:33:54.449 I [fi_submission_server__set_state] INJECT_LLE -> RECV_RESP
00:33:54.450 D [fi_remote_log_add] Added remote log: 22
00:33:54.451 I [fi_submission_server__set_state] RECV_RESP -> COMPLETE
00:33:54.452 D [fi_remote_log_add] Added remote log: 22
00:33:54.453 E [handle_failed_assert] ASSERT FAIL: "(gs->state == FI_CXD5605_GNSS_SERVER_STATE_DISABLED) || (gs->state == FI_CXD
```

```
00:02:38.383 D [fi_ble_log_state] connected and pending
00:02:38.385 I [power_check_battery_charger] Battery: state 3, bq25180_stat0:0x61, is_chg:0 has_pwr:1 on_base:0 has_power_supply=1
00:02:38.385 I [module_hsm_log_state] T1=-1s T2=-1s T3=-1s State=[ run-wifi, wifi:connected, wifi-connected:idle ]
00:02:39.171 W [counter_timer_stop] Unbalanced stop for counter: 98
00:02:39.171 I [module_hsm_send_event] BLE_CONNECT
00:02:39.171 I [evaluate_transition_targets] -> 'no-connection', condition 'none'
00:02:39.172 I [hsm_instance_transition] moving to state: no-connection
00:02:39.172 I [transition_to_path] no-connection
00:02:39.172 I [pop_state] Exiting wifi-connected:idle
00:02:39.173 I [pop_state] Exiting wifi:connected
00:02:39.173 I [pop_state] Running exit action: report_disconnected_from_stable
00:02:39.173 I [pop_state] Exiting run-wifi
00:02:39.174 W [counter_timer_stop] Unbalanced stop for counter: 26
00:02:39.174 I [pop_state] Running exit action: set_ble_postponed_attachment
00:02:39.174 I [pop_state] Running exit action: wifi_stop
00:02:39.175 D [da16200_drv_set_wake_mode] da16200_drv_set_wake_mode: booting
00:11:11.193 E [da16200_phy__boot_poll] da16200_phy__boot_poll: boot timeout
00:11:11.194 E [fi_da16200_sync_acquire] fi_da16200_sync_acquire: acquire timeout 512010/15000ms
00:11:11.194 E [fi_da16200_sync_acquire] init_da16200_acquire: failed!
00:11:11.195 D [_act_impl_wifi_stop] not connected / acquire failed, sleep 1
00:11:11.195 D [fiwifi_client_stop_remain_assoc_time] stopping
00:11:11.196 I [fiwifi_parser_reset] fiwifi_parser_reset
00:11:11.206 D [brain_consume_event] WIFI_STOP
00:11:11.207 I [push_state] Entering no-connection
00:11:11.207 I [push_state] start_timer
00:11:11.207 I [_act_impl_start_timer] Starting HSM timer -- 5000 ms
00:11:11.218 I [push_state] check_is_report_due
00:11:11.219 D [fi_remote_log_add] Added remote log: 7
00:11:11.220 I [utc_wallclock_sync] Syncing UTC clock
00:11:11.237 E [handle_failed_assert] ASSERT FAIL: "actual_radio_event_percentage > 0.2f radio: 166/1098 events" file "../../src/nrf52/fi_module/fi_ble.c", line 917

00:11:11.238 W [fatal_error] Failed boot count 00:00:00.020 ! [log_module_details] fi_module board=3 build=0.0.0-local-fc3_f3-dev platform_id=<null> module_id=FC32H000328
00:00:00.021 ! [log_module_details] BL Ver: 0.0.0-local-fc3_f3-dev-bl
```




**2024-04-05**
Some thoughts and questions on doing wifi scanning on poor GPS fix.
I think the obvious case where we should do additional wifi scanning are when:
- module is responding to server push message (Since we don't turn on GNSS for positioning in those case, and just fire off a LTE report asap)
- one shot GNSS failed
So some questions, do we want to also be doing wifi scanning during live tracking and without fix? If so how frequent?
I doubt we want to do wifi scanning every 10 seconds, that feels way to frequent, but maybe every 1 minutes when the GNSS don't have a good fix?
Also should we only be doing WIFI scanning when we don't have "good" fix? Or should WIFI scanning be done when we don't have valid fix only?
Do we want to reevaluate our definition for good quality fix? Right now server flags control it and set it to 6 sat tracked to be good quality.


Auto LT backend:
- BLE/WIFI break, module turned on LT = Keep LT on and try to get another location
- On module reboot, if module was previously outside SZ keep LT off, if was inside SZ keep LT on
**2024-04-03**
Y: finished up aggressive retry on lte fail report
T : get started on wifi scanning on poor gps fix

**2024-04-02**
Y: Getting LTE report aggressive retry to work
T: Testing and getting existing PR to be merged

**2024-04-01**
Y: working on modem actor for report retry on failure
T: getting report retry working

With breadcrumbs we don't send the first fix report that pass the quality, we actually hold on to the breadcrumbs data until full 10 seconds have elapsed before getting the data.

| Peripheral | I2C Address |
| ---------- | ----------- |
| BQ25180    | 0x6A        |
| BQ27421    | 0x55        |
| CXD5605    | 0x24        |
| LP5523     | 0x32        |
| RA9530     | 0x3b        |
| RV4162C7   | 0x68        |


```
tQEKsgEYAViwFmDc7K4BcixpZ3VPeGluOENLNmUzdGs5N2dBdFRWc3pOSDQxZStzL1E0MGx4dGVjQld3PZoBALIBAigXuAEEwAEHygEYCgkI6A8QBBgCMAMSCQjoDxAEGAIwAxoAmgJIChIiEGxvY2FsLWZjM19mMy1kZXYSFSITbG9jYWwtZmMzX2YzLWRldi1ibBoXCAMYBSIRbWZ3X25yZjkxNjBfMS4zLjUiAhBFpQIt9FFYAloAiQEqhgEIyREoATCPAjjGD0C8FUgBgAEjiAHNApgBuAGgAbgBuAH2ENAB8asW2AEEiAKuBaAC8CbAAoWYCMgCzKwJ0AID2ALBtAToAtc6+AL8BYAD1AmgA7cCyAME4AME6AMCqAT+iQKwBLI6uATREMAEwxLIBMsE2ASZL+AEuO0B6AUm8AWTAYAGAQJiAHUScwoXMy4wLjUtbWZ3X25yZjkxNjBfMS4zLjUSFDg5MDExNzAxMzI0MTUyMzU2MjIzGg8zNTM3ODU3MjU4NDA1MjMg9ico9wIwj5bJB0C2AkiaA1UAAJTCXQAA4MBqBDMyNDByAi0xeAGFAQrXo0GNAQrXI0Awei4IsBYSJBIiCLYCEIQCGIbaiBEg9KsBKKsnMP//Azjbyq4BQJoDSDZQDBgBIKwWswJSsAIQ/AYd/pEpQiVFN47CWgYIBRA1GD5aBAgHGBpaBggNEEEYSFoHCA8QShjRAVoGCBQQGBhVWgcIFxAUGJQCWgcIHRAnGOIBWgYIHhAQGDJiBwhHED8YigJiBwhIEBIY7gFiBghPEAcYJGIGCFAQAxhUYgcIVRAzGKQBcg4qDAAAAAAAAAAAAAAAAHoOKgwAAAAAAAAAAAAAAACCAQ4qDAAAAAAAAAAAAAAAAI0BAACAv6IBCQjoDxAEGAIwA6oBCQjoDxAEGAIwA7IBALgBAcABz8GtsAbgAQHyARIQ+AYd/pEpQiVFN47CLQAAgL/yARIQ+QYd/pEpQiVFN47CLQAAgL/yARIQ+QYd/pEpQiVFN47CLQAAgL/yARIQ+wYd/pEpQiVFN47CLQAAgL/4AagWFUITCgQKAkZpCgsKCWRlc2NhcnRlc4IBggF/EngAAQAAAAAQgAAIAAAAABCKhIQCAAWAA4CAAAAAAAAIQAAEAAAAAECVwoEAQAGAAkBAAAAAAAAAIAABAAAAAIpWAUEAAACAACAgAAAAAAAAEAABAAAAAEiwoLAAQABwABAAAAAAAAAACEAAAAAAgHtOQBAAOABAAAgY7piuARSKARESDwju/K0BOggINRA1GDQgARSKARESDwjZia4BOggINRA1GBEgARSKARESDwiTiq4BOggINRA3GA8gARSKARESDwiRsa4BOggINxA3GAQgARSKARESDwiDzK4BOggINxA1GAcgAQ==
```