---
publish: true
review-frequency: normal
link:
- '[[android]]'
- '[[jail break]]'
- '[[root]]'
- '[[bootloader]]'
tags:
- documentation
---

# Oneplus Root

Install TWRP
- adb reboot bootloader
- fastboot oem unlock
-- Phone will reboot need to get it back into fastboot mode
- fastboot flash recovery twrp.img
- "Manually boot into recovery mode through fastboot"

Install SuperSu
- adb reboot bootloader
- "Load supersu zip onto /sdcard"
- "Install"
- "reboot"
- "Wait for a few reboot cycles"

Clean Stock Apk
- "Remeber to remove the supersu zip"