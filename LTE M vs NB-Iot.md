---
publish: true
review-frequency: normal
---
Last Updated: 2022-08-23
Type:: #documentation 
Tags:: [[LTE]], [[nb-iot]]

# LTE M vs NB-Iot

- Both LTE-M and NB-IoT networks are now [formally recognized as 5G technologies,](https://www.ericsson.com/en/networks/trending/insights-and-reports/nb-iot-and-lte-m-in-the-context-of-5g-industry-white-paper#:~:text=3GPP%20has%20agreed%20that%20the,part%20of%20the%205G%20evolution.&text=The%20long%2Dterm%20status%20of%20these%20technologies%20is%20confirmed.) which means the networks, and our LTE-M / NB-IoT devices will be supported long after 4G network shutdowns

**Bandwidth** – NB-IoT uses a very narrow bandwidth (200kHz), compared to LTE-M which uses 1.4Mhz (7000x larger)! Bandwidth is the width or capacity of the channel in which data can be transferred. Think lanes on a freeway – more lanes mean more cars can get along the freeway in a given time period. Bandwidth is the width of the road here.

**Data Transfer Rate** – As a result of NB-IoT’s narrow bandwidth, the maximum data transfer rate is around 250kb per second. The data rate on LTE-M is about four times faster – up to 1Mbps.

**Cellular Tower Handover** – LTE-M supports cell tower handover, which refers to the process of transferring a connection from one cellular tower to another. NB-IoT does not support cell tower handover, and the connection will be dropped if a device moves out of range. For many battery-powered asset tracking applications, this is of little consequence.

**Range** – Both networks provide excellent range and penetration, particularly when compared to 2G or 3G networks.

**Power** – An NB-IoT modem uses slightly less energy to transfer data than an LTE-M modem. But because of NB-IoT’s slower data transfer rates, uploads take longer than LTE-M. So, power consumption on either network is similar and very low.

**Firmware Over-The-Air** – Device firmware can be updated remotely over-the-air on both networks. However, larger OTA updates on NB-IoT may result in substantial power use given the network’s slow transfer rate.

![[LTE_M_NB_IOT_compare.jpeg]]

---
# References