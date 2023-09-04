---
publish: true
review-frequency: normal
---
Last Updated: 2022-10-06
Type:: #documentation 
Tags:: [[embedded]], [[hardware]], [[crystal]]

# Why 32.768 kHz

> [!answer]
> The frequency of a real time clock varies with the application. The frequency 32768 Hz (32.768 KHz) is commonly used, because it is a power of 2 (215) value. And, you can get a precise 1 second period (1 Hz frequency) by using a 15 stage binary counter.
> 
> Practically, in majority of the applications, particularly digital, the current consumption has to be as low as possible to preserve battery life. So, this frequency is selected as a best compromise between low frequency and convenient manufacture with market availability and real estate in term of physical dimensions while designing board, where low frequency generally means the quartz is physically bigger.

---
# References
- https://electronics.stackexchange.com/questions/177844/why-do-we-use-32-768-khz-crystals-in-most-circuits