---
publish: false
review-frequency: normal
link:
- '[[linux]]'
- '[[bug]]'
- '[[feature]]'
- '[[uart]]'
- '[[Notes todo]]'
tags:
- documentation
---

# A really weird Linux system UART behaviour

A uart device when first plugged into linux and powers up would output some logs.

While linux upon opening the uart device seems to somehow write the some of the logs back through the uart device.

This is UART CDC device.

---
# References