---
tags:
  - articles
link:
  - "[[embedded]]"
  - "[[systems]]"
---
Embedded systems have many re-used components, software or hardware or mixed. Their integration are difficult due to incompatible interfaces, standards, and also different specialization.

ASIC (ASIP) or DSP are not easily portable between architecture, only live with the heterogeneous embedded system architectures. This also brings on integration problems.

OTOH, there is SW integration where each controller speak the same protocol are all connected via a common bus. This is the case on automotive controllers. But this have a upper limit, and to reduce number of controllers functions needs to be shared on the same controllers. And cause new problems of how to test or certify the shared processors.

Integration challenges:
- component and subsystem interfacing
- System verification
- System optimization with design space exploration

---
# References
- http://queue.acm.org/detail.cfm?id=644268