---
publish: false
reviewed: 2023-07-10
review-frequency: ignore
tags:
- documentation
---

# MacOS Command-Line tools

## caffeinate
`caffeinate -u -t <seconds>` prevents sleep for the specified number of seconds.

## pbcopy, pbpaste

## networkQuality
Add the `-v` flag to view more detailed information.
Use the `-I` flag to run the network test on a specific network interface.

## sips
image manipulation

## textutil
document file converter

## mdfind, mdls
search with Spotlight

## screencapture
take screenshots

## taskpolicy
control scheduling of processes

## say
text-to-speech engine

## pmset
configure power management

## networksetup
configure network settings

## system_profiler
view system information

- `system_profiler <datatype>` only prints information about the given sub-system.
- `system_profiler -listDataTypes` lists all available sub-systems to get information from.

- `system_profiler SPUSBDataType` ***List USB devices similar to lsusb on Linux***

- `system_profiler SPHardwareDataType` prints an overview of the hardware of the current machine, including its model name and serial number.
- `system_profiler SPSoftwareDataType` prints an overview of the software of the current machine, including the exact macOS version number.
- `system_profiler SPPowerDataType` prints power and battery information, including the current AC wattage and battery cycle count.
- `system_profiler SPDeveloperToolsDataType` prints the currently active version of the Xcode developer tools and SDK.

---
# References
- https://saurabhs.org/advanced-macos-commands