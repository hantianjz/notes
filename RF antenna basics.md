---
publish: true
review-frequency: normal
link:
- '[[RF]]'
- '[[antenna]]'
tags:
- notes
---
2022-06-05-Su

# RF antenna basics
**Antenna**: Transducer that convert energy from one domain into another domain.
**Transducer**: electronic device that convert energy from one form to another.

**Radiation properties**
1) Reciprocity
2) Antenna Pattern
3) Gain
4) Polarization

**Impedance Properties**
1) Radiation resistance
2) Loss resistance
3) Voltage Standing Wave Ratio (VSWR)

Isotropic Antennas
Math construct for frame of reference.
Perfect uniform radiation all direction, gain of 0 dB in spherical space, 100 efficiency.

dBi (decibels relative to isotropic antenna)

## Maxwell Equations
- Gauss's Law
- Gauss's law for magnetism
- Faraday's law
- Ampere's law with Maxwell's addition

Magnetic field $\vec{B}$ aways orthogonal to Electric field $\vec{E}$

## Polarization
Polarization characterize direction of $\vec{E}$ 
Transmitting and receiving antenna should have the same polarization.

Linear polarizations
- Horizontal & vertical polarization
- Slant

Circular polarization
- Right hand circular
- Left hand circular
- Elliptical

## Gain
Antenna gain power at the antenna and account for lose

gain = Efficiency x Directivity

## Common frequency bands
| Band | GHz    | WL (cm)   |
| ---- | ------ | --------- |
| L    | 1-2    | 15-30     |
| S    | 2-4    | 7.5-15    |
| C    | 4-8    | 3.75-7.5  |
| X    | 8-12   | 2.5-3.75  |
| Ku   | 12-18  | 1.67-2.5  |
| K    | 18-27  | 1.11-1.67 |
| Ka   | 27-40  | 0.75-1.11 |
| V    | 40-75  | 0.4-0.75  |
| W    | 75-110 | 0.27-0.4  |

## dB
dB value is relative unit
dB = 10 log (Pout/Pin)

dBm = Absolute power measured relative to 1mW.

## Near Field vs Far Field
Far Field = $\frac{2D^2}{\lambda}$

D = largest diameter of antenna

## Scattering Parameters (S-Parameters)
2 port network

S11 Return lose = Incident Power / Reflected power

S22 Insertion loss = incident power / transmitted power

Vector Network Analyzer (VNA)

## Smith charts
Plot impedance as function of frequency.
Make plotting impedance -> infinity possible:
    - Z = 0 short circuit
    - Z = 1 impedance matched
    - Z  = $\infty$ open circuit

## VNA
Calibrating a VNA specific to connector type
- Set frequency range first!
- SMA-type cal procedures:
    - 2 - port: short, open, 50 $\ohm$, through (SOLT)
    - 1  - port: short, open, 50 $\ohm$ (SOL)
- **Short**: LOGMAG plot read close to 0dB
- **Open**: LOGMAG plot should read close to 0dB
- **Load 50** $\ohm$: LOGMAG plot should showing a low number (50dB or below)

## Attenuation
Reduce signal level 

---
# reference
- https://www.youtube.com/watch?v=axUcybeamIk&list=PL_tws4AXg7authztKFg5ZN5qWGtq3N_nI