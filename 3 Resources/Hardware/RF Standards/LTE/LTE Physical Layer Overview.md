---
publish: true
review-frequency: normal
tags:
  - notes
link:
  - "[[LTE]]"
  - "[[Network Protocol]]"
  - "[[Phy Protocol]]"
reviewed: 2023-09-03
---
![[lte_frame.png]]

The 89600 VSA LTE demodulator currently only supports resource blocks that are 12 subcarriers wide.

![[lte_fdd_frame_type1.png]]
![[lte_tdd_frame.png]]

Special subframes

Subframes 0 and 5 and DwPTS in TDD frames are always allocated to downlink transmissions.

UpPTS and the subframe after a special subframe are always allocated to uplink transmissions.

Subframe 1 is always configured to be a special subframe. Subframe 6 can also be configured to be a special subframe.

![[lte_ul_frame.png]]

A user cannot transmit both PUCCH and PUSCH data in the same slot.

![[lte_sc-fdma.png]]

![[lte_dl_tx-2.png]]

The different sections of the illustration above are explained in the following sections.

The LTE demodulator provides traces that show IQ or error vector data vs. subcarrier or symbol. The content of these traces comes from the selected layer. However, layers do not exist in the context of resource blocks. How can these traces show layer data in the context of resource elements and symbols?

The answer is that the demodulator undoes the precoding to recover the original modulation symbols in the layers for each physical channel and then remaps those modulation symbols back onto the physical channel allocations in the frame. The values shown on the layer traces do not have a direct physical correspondence to the subcarrier that they are mapped to. However, there is still an indirect correspondence between modulation symbols and the actual subcarriers. For instance, if you corrupt one of the subcarriers in physical channel's allocation by adding a sine wave at that particular frequency, you will see that the EVM of more than one modulation symbol on the physical channel's layer trace will be affected.

![[lte_ofdm.png]]

OFDM has a large peak-to-average power ratio which means that the amplifiers have to be higher quality and are more expensive (and are also more power hungry).

The LTE demodulator only supports viewing beam patterns for linear antenna arrays. The number of elements in an antenna group and spacing between elements is specified by the [Antenna Group parameters](http://rfmw.em.keysight.com/wireless/helpfiles/89600b/webhelp/subsystems/lte/content/lte_dlg_adv_antennagroupparams.htm).

---
# Reference
- https://rfmw.em.keysight.com/wireless/helpfiles/89600b/webhelp/subsystems/lte/content/lte_overview.htm