---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #idea
Tags:: [[SDR]], [[IQ Signal]]

# Frequency Shift Keying encoding

[[SC16_Q11]] signed-complex 16 bit Q11
Bit[31-16] = Q
Bit[15-0] = I

FSK encoding:

1 if $(I0 * Q1 - I1 * Q0) > 0$ else 0

 Phase change $\uparrow == 1$ 
 
 Phase change $\downarrow == 0$ 

---
# References
