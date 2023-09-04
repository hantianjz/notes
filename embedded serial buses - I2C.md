---
publish: true
review-frequency: normal
---
Last Updated: 2022-05-28
Type:: #documentation 
Tags:: [[embedded]], [[i2c]], [[serial bus]]

# Embedded serial buses - I2C


Default pull up 
Buffer to sample the line 
FET to drive the line

If pull up is too you get shark fin

# Start stop conditions
The only time the data line can change is when the clock line is high is during start stop conditions

## Start
Bus is idle: SDA and SCL high

**SDA** high to low follow by **SCL** high to low
***SDA** changing only when **SCL** is high, hence start/stop condition*

## Stop
Bus is active: SDA and SCL low

**SCL** low to high follow by **SDA** low to high
*Mirror to start in revserve*

## Repeated start condition
Start a new START condition instead of a STOP condition.

# Bus arbitration
More than 1 controller on the bus to multiple peripheral.

# Two roles
one device sending data (talking), and receive the data (listening)

Listening is release the SDA line.

# Data transmit
Every bit of data is associated with a clock pulse.

SCL low to high is "clocks in" of data.

SDA only change when SCL is low. (otherwise it is start/stop)

one byte only, 8 bit per byte.

Controller send address every transaction.

End of byte, have ack bit from receiver peripheral.

# Ack/Nack
Controller let go of SDA. peripheral holds SDA line *low*, during clock pulse.

To NACK, peripheral does nothing and SDA is high by default.

# Address peripherals
7 bits, unique to each type of device
8th bit for read/write. *Low* for write, *high* for read.

Part address is `0x40`. Write `addr == 0x81`, Read `addr == 0x80`

---
# References
- https://youtu.be/hle4Be3B95w 