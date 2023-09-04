---
publish: true
reviewed: 2023-03-18
review-frequency: low
---
2023-03-18-Sa
Author:: ?
Originally published:: 2022
Type:: #notes
Tags:: [[Reading/reading]]

# Notes on Hardware Hacking Handbook

## Hardware Components (p2)
> On a typical PCB the analog components are all the little black, brown, and blue parts that don’t look like a chip and may have labels starting with “**C**,” “**R**,” or “**L**.”

## Hardware Threat Modeling (p7)
When performing threat modeling, we roughly do the following:
- **defensive view**:
    - identify the system’s important assets
    - how those assets should be secured
- **offensive viewpoint**:
    - identify who the attackers might be
    - their goals
    -  what attacks they could choose to attempt

> **Threat modeling** is the process of determining how to reach a secure-enough state in a particular device or system.

### Attacks through time (p8)
> Attacks always get better; they never get worse

Technology get better, hardware asset might stay the same. Designer need to take into account of whatever attacks might be happening during the full life span of the asset.

The *identification phase* involves identifying vulnerabilities. The *exploitation phase* follows, which involves using the identified vulnerabilities to exploit a target.

### The Attack Tree
An *attack tree* visualizes the steps an attacker takes from the attack surface to compromise an asset, allowing systematic analysis of an attack strategy.

The four ingredients in an attack tree are:
- attackers
- attacks
- assets (security objectives)
- counter-measures
![[Sample_attack_tree.png]]

### Profiling the Attackers
- Criminal enterprise
- Industry competition
- Nation-states
- Ethical hackers
- Layperson attackers

### Types of Attacks (p12)
- Software Attacks on Hardware
    - Fault Injection
        - A fault injection by itself is not an attack; it’s what you do with the effect of the fault that turns it into an attack.
        - DRAM *hammering* is a well-known fault injection technique in which   the DRAM memory chip is bombarded with an unnatural access pattern   in three adjacent rows. By repeatedly activating the outer two rows, bit flips occur in the center victim row.
        - Overclocking the CPU causes a temporary fault called a timing fault to occur.
    - Side-Channel Attacks
    - Micro-architectural Attacks
        - *Spectre* attack from 2018 exploits a neat optimization called *speculative execution*.
- PCB-Level Attacks
    - Taking advantage of SoC options that are configured by pulling certain pins high or low using straps
    - Read the flash chip on a PCB
- Logical Attacks (Attacking logic interfaces, I.E. I/O ports)
    - Work through firmware level breach
    - I.E. Memory corruption, code injection
    - Debugging and Tracking, unlocked jtag port
    - Fuzzing devices
    - Flash image Analysis, via ***binwalk***
- Noninvasive Attacks
    - side-channel measure
- Chip-Invasive Attacks
    - Decapsulation, De-packaging, and re-bonding
    - Microscopic Imaging and Reverse Engineering
    - Scanning Electron Microscope Imaging
    - Optical Fault Injection and Optical Emission Analysis
    - Focused Ion Beam Editing and Microprobing

### Assets and Security Objectives (p22)
Confidentiality, Integrity, Availability

**Assets and objectives**:
- Confidentiality and Integrity of Binary Code
- Confidentiality and Integrity of Keys
- Remote Boot Attestation
- Confidentiality and Integrity of Personally Identifiable Information
- Sensor Data Integrity and Confidentiality
- Content Confidentiality Protection
- Safety and Resilience

### Countermeasures (p26)
- Protect
- Detect
- Respond

### Attack Tree Example (p27)
![[attack_tree_example_iot_toothbrush.png]]
#### Scoring Hardware Attack Paths
- [Common Vulnerability Scoring System (CVSS)](https://www.first.org/cvss/calculator/3.1)
- Common Weakness Scoring System (CWSS)
- Joint Interpretation Library (JIL)

Dino Dai Zovi had a cool talk called [“Attacker Math 101”](https://trailofbits.files.wordpress.com/2011/08/attacker-math.pdf) at [SOURCE Boston](https://techchannel.att.com/play-video.cfm/2011/7/14/Conference-TV-SOURCE-Boston:-Attacker-Math-101) 2011 that attempted to put some bounds on attacker costing.

*PS: Start with JIL for threat modeling for embedded systems*

### Disclosing Security Issues (p33)
> Disclosure must serve the public in the long run.

