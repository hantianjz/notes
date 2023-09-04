---
publish: true
review-frequency: normal
---
Last Updated: 2022-02-25
Type:: #documentation 
Tags:: [[LTE]], [[LPWAN]], [[3GPP]], [[AT Commands]], [[UBlox]]

# Overview of LTE Cat M1
- A low-power wide-area (LPWA) air interface for network connection
- Provide enhanced power saving mode
- Extended in-building range (15dBm more than LTE) via *Coverage Enhancement mode*
- Different from **LTE Cat 1**
- Part of 3GPP Release 13 standard
- A different standard is Narrowband IoT **NB-IoT** aka *LTE Cat NB1*
- **Uplink speeds 375 kbit/s**, maybe 1Mbit/s from protocol stack enhacements
- **Downlink speeds 375 kbit/s** in half duplex mode
- Remove firmware update *uFOTA* accessing MNOs and u-blox server via LWM2M protocol

 ## Lower power features
 - Enable lower power saving mode via  `+UPSV` with different modes to be selected.
 - PSM (Power Save Mode) have less periodic registration to the LTE network, but long-lasting non-reachability

---
# References
- [SARA - R5 series Application development guide](https://www.u-blox.com/en/docs/UBX-20009652)