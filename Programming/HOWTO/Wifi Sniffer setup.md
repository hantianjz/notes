---
publish: true
review-frequency: normal
tags:
  - documentation
link:
  - "[[WIFI]]"
  - "[[sniffer]]"
  - "[[linux]]"
reviewed: 2023-09-03
---
Automatic start-up of systemd user instances

The systemd user instance is started after the first login of a user and killed after the last session of the user is closed. Sometimes it may be useful to start it right after boot, and keep the systemd user instance running after the last session closes, for instance to have some user process running without any open session. Lingering is used to that effect. Use the following command to enable lingering for specific user:
```bash
# loginctl enable-linger username

$ systemctl edit --user --force wifi_sniffer.service

###