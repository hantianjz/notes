---
publish: false
reviewed: 2023-01-17
review-frequency: ignore
---
Last Updated: 2023-01-17
Type:: #documentation 
Tags:: [[gps]]

# My home GPS location

# 83 alpine st

## google maps value
42.392470497514296, -71.1079805461192
42.39257305857694, -71.1078510575004
=>
42392470 -71107980

## Elevation
45 ft  => 13.6 m

## Full input
42392470 -71107980 136

# Flow
```
gns 0x03
guse 0x0000
gpos 42392470 -71107980 136
gsop 2 60000 0
gtim
gsp
```

---
# References