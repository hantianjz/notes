---
publish: true
reviewed: 2023-02-27
review-frequency: ignore
link:
- '[[embedded]]'
- '[[power]]'
- '[[eletricity]]'
- '[[Notes todo]]'
tags:
- documentation
---
# Embedded Electricity Basics

- **Voltage:** V, expressed in units V and named after *Alessandro Volta*
- **Current:** I, expressed in units A and named after *André-Marie Ampère*
- **Resistance**: R, expressed in units Ω and named after *Georg Simon Ohm*
- **Ohm’s Law:** `V = I x R`
- ***Impedance*** in AC is equivalent to resistance in DC
- ***Reactance*** is a function of inductance and capacitance
- ***Inductance*** is the resistance by the circuit to a change in current
    - In unit of *henry*, after *Joseph Henry*.
- ***Capacitance*** is the resistance to a change in voltage
    - In unit of *farad*, named for *Michael Faraday*.
- **Power**: the amount of energy in Joules consumed per second, expressed as P in units of W (watts, after *James Watt*)
- Model a wire as a capacitance *C*, switching a square wave between 0V and *V* volt at frequency f requires `P = C × V × V × f`.

## Interface with Electricity

### Logic levels
To represent a bit "one" use a high logic level, and "zero" bit with a low logic level. 
However, because of resistance in the wire, you might not see a full 5 V on the other end, perhaps only 4.5 V.
Therefore a logic level standard.

#### Transistor-transistor logic (TTL) Standards
- **VCC** supply voltage

![[TTL_Standards.png]]

### High Impedance, Pullups, and Pulldowns

### Push-Pull vs. Tristate vs. Open Collector or Open Drain

### Asynchronous vs. Synchronous vs. Embedded Clock

### Differential Signaling


---
# Reference
- The hardware Hacking Handbook (Pg 41)