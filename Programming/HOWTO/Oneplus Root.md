---
publish: true
review-frequency: normal
---
Last Updated: 2021-12-29
Type:: #documentation 
Tags:: [[android]], [[jail break]], [[root]], [[bootloader]]

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