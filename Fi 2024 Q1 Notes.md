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

**2024-01-05**
Y: work on module version manifests, pushed latest base fw to Fi internal users
T: analyze base releases data, cut new ble v2.1 module fw to new behavior detection feature

- [ ] Update LLE Throttle to 100%?
- [ ] Fix fwup via base handoff not happening 

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