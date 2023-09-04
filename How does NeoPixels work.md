---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #idea
Tags:: [[embedded]], [[peripheral hardware]]

# How does NeoPixels work

NeoPixels are also based off WS2811 and SK6812 LED drivers

Use single NZR communication mode:
| CODE | Duration | Margin  |
| ---- | -------- | ------- |
| T0H  | 0.4us    | +-150ns |
| T0L  | 0.85us   | +-150ns |
| T1H  | 0.8us    | +-150ns |
| T1L  | 0.45us   | +-150ns |
| RES  | > 50us   |         |

![[152370_152370.png]]

Each pixel require 24bit of data:
`|G7|G6|G5|G4|G3|G2|G1|G0|R7|R6|R5|R4|R3|R2|R1|R0|B7|B6|B5|B4|B3|B2|B1|B0|`
Note: Follow the order of GRB to sent data and the high bit sent at first.

With pixels chained in series, first pixel consumes first 24 bits, then pass down later bits, until reset signal.
![[neopixel_chained_data_flow.png]]

---
# References
[WS2812](https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf) integrated light source.