---
publish: true
review-frequency: normal
link:
  - "[[reading]]"
  - "[[SCI 591]]"
  - "[[RF]]"
tags:
  - notes
---
2022-12-09-Fr

# Notes on Cellular Network Security

- [ASN.1](https://en.wikipedia.org/wiki/ASN.1) Abstract Syntax Notation One, standard interface description language.

# Fundamentals
> [!What is security?]
> A computer is secure if you can depend on it and its software to behave as expected.
>                     -- Garfinkel and Spafford

- Security does not exist without notion of **adversary**.

> [!A meta-definition]
> A system is secure if it can maintain well-specified properties in spite of the actions of well-specified adversaries.

- A set of properties we assume to be correct is **trust model**.
- A set of adversaries and their capability is **threat model**.

- Generally concern with **CIA** triad. (Confidentiality, Integrity, Availability)

- Cellular Network adversaries
    - Subscribers theft of service
    - Other telecos competing
    - Unauthorized Parties
    - National Intelligence
- Threats
    - Intentional: Hacker, adversary
    - Accidental: fire, natural disaster
- Vulnerabilities
    - A flaw that expose user, data, system to a threat
- Attack Archetypes
    - Interception - access to asset
    - Modification - change to asset
    - Fabrication - creation of fake asset
    - Interruption - asset lost of unavailable.
- Defense Archetypes
    - Prevention - Block
    - Deterrence - Make attack harder
    - Deflection - Make target less desirable
    - Detection - Detect attack
    - Recovery - Fix things after attack

## Public Switched Telephone Network

- Public Switched Telephone Network (**PSTN**)
    - Network of global networks
- Telephone: an abstraction
    - Send and receive band limited signal in the audible range
    - Has a phone number
- PSTN is heterogeneous
    - Nothing like IP of internet
    - *POTS*: (**Plain old telephone service**) - analog copper lines
        - 1975
    - *ISDN*: (**Integrated Services Digital Network** - all-digital reimplementation of POTS.
    - Intelligent Network: Core functions that provide service beyond voice calls
        - Number portability
    - Cellular: 2G (GSM/CDMA), 3G (UMTS/CDMA2000), 4G (LTE), 5G (NR)
    - VOIP: router call over internet
        - SIP+S/RTP, H.323
        - Not required over commodity internet
        - Carriers moved core networks to private IP networks part of *PSTN*

### Routing
![[Pasted image 20221210142249.png]]
- A sort of tree network
- Each town, neighborhood have a central office
- Tandem office == backbone routers for international/longer distant calls
![[Pasted image 20221210142629.png]]
- Private Branch Exchange (PBX)
- Local exchange trunk carry signals between exchanges, a bunch of phone lines
- Class 1 switch cover a continent
- Routing is simple, if destination no in network, you route up
- Calls established with "signalling", distinct from traffic/media. (control plane vs data plane)
- Routing is hierarchical and fixed
- Network aim was 99.999% (five 9s)

- The contrast between PSTN and Internet dedicated a lot of design decision.

- PSTN and Internet engineers think about the network differently
- PSTN is more like internet, than internet is like PSTN

- Telephone number ITU standard E.164
    - "+" + 1-3 digit country code (trunk line) + subscriber number (max 12 digits)
    - 
![[Screen Shot 2022-12-10 at 14.59.04.png]]
- North American Numbering Plan (NANP)
    - Numbering Plan Area(NPA) - Area code, 3 digit
    - Central office number - `NXX`, N = [1,9], X = [0,9]
    - 4 digit identifier for subscribers
- A *provider* *originates* a call - to start a call process regardless of success
- A provider *terminates* the call - connection is established or completed
- One or more *carriers* route call between providers
- *Toll-free* cost nothing to originator but destination.
- Premium Rate Number - NPA 900, destination bill subscriber via phone company

### Caller ID
- Referring to CLI+CNAM
- CLI - Calling Line Identification, **Claimed** TN for the *originating* subscriber.
- CNAM - Alphanumeric lookup of display name, come from database lookup by *terminating* provider
- ANI - Automatic Number Identification, available to toll-free operators, harder to spoof but doable

## PSTN Security
- Carrier does least cost call routing and can vary from time to time
- Confidentiality
    - Subscriber data
    - Media and metadata confidentiality
    - Business Relationship and routing rates
    - Internal network structure
    - Network secrets (keys, passwords, ...)
- Integrity
    - **Anything Billable**
    - Signalling and identity
    - Subscriber information (with identity fraud)
    - Changes to subscriber information
    - Change to network equipment, configuration and equipment
    - Physical plant and equipment
- Availability
    - **Uptime**
        - Low-blocking probability
        - Quality of Service
        - E911
    - PHY Availability (Rx, cables intact...)

## History
- The only phone network: American Telephone and Telegraph (AT&T)
    - The bell system
    - aka Ma Bell
- Bell system operated the PSTN in NA until 1984
    - regulated monopoly with subsidiaries:
        - Bellcore: Engineer
        - Western Electric: Manufacture
        - Bell Labs: Invention
        - AT&T Long Lines: Long distant
    - 1984 Broke up monopoly
        - Subsidiaries became independent
        - Main system broke into Regional Bell Operating Companies (**RBOCs**) or I-LECS (Incumbent Local Exchange Carries) or "Baby Bells"
        - I.E. Bell Atlantic, Bell South, NYNEX
        - Competing long distance carriers: MCI, Sprint
    - Call was expensive due to high reliability
    - Because Ma Bell designed the tech and controlled every party of network, they knew exactly who every entity was on the network
    - Lack of internal security, and only external security measures
- Telecommuncations Act of 1996
    - FCC: "let anyone enter any communications business – to let any communications business compete in any market against any other."
    - Anyone could now be a **CLEC**: Competitive Local Exchange Carrier
    - It also led to a services industry for those CLECS, including interconnect providers aka carriers
- Signalling System 7 (**SS7**): The lingua franca of telco
    - Created in mid 70s by Bell System
    - Provide isolated, separate signaling that wasn't in-band
    - Prior, all signaling was analog allowed any phone to control and talk to the network for free calls.
    - **ISDN** was built on top of SS7
    - SS7 is used to:
        • Uniquely identify and route traffic to core entities (point codes)
        • Setup and tear down phone calls
        • Query databases and other services (VM, LNP, CNAM, ...)
        • Mobile Application Part (MAP):
            - Manage mobility
            - roaming
            - authentication subscriber
    - SS7 is how telcos “talk” to each other at network boundaries
    - Problems:
        - SS7 network is global, no authentication
        - Have a point codes on network, is very powerful do anything telco can do
        - Access is harder now
        - Can attack any telco network
        - Current state: SS7 firewalls, block certain commands
    - Attacks:
        - Subscriber information: permanent identifier, current location
            - Just pretend to be a network and ask for it!
            - Query any subscriber in the world.
        - Intercept incoming and outgoing calls and SMS (include MFA)
            - tell a subscriber’s home network that they are roaming at your location.
            - Enable call forwarding
        - Deny service to a subscriber
    - To get access to the network, through a gateway, SS7 command can be carried over the internet to the gateway
        - Big companies, defence contractors
- Cellular
    - 80’s: analog radio telephones
    - 90’s: 2G digital phones
    - 00’s: 3G
    - 10’s: 4G
    - 20’s: 5G
    - Networks operated independent networks in the PSTN
- Voice Over IP: VOIP
    - Goal: Telephone becomes like any other Internet service (mail, IRC)
        - Protocols inspired by email and HTTP (human readable!)
        - Addressing: sip:name_or_number@example.com
        - DNS records for phone directory information! (ENUM)
    - Massive proliferation of new VoIP
        - SPAM like email
        - Email Spam was solved with filtering, DKIM, and server reputation
        - VoIP Spam was solved by **closing off the network**
            - Over private IP network
    - The “last mile” from subscribers is often over commodity Internet through *SIP Trunks* 
    - Once at the VoIP provider, the traffic is sent through private network
    - These may be VoIP or **TDM** (a term for old school digital PSTN trunks) but the call will go through multiple closed provider networks
        - IP Traffic is filtered by Layer-7 application firewalls called Session Border Controllers (SBCs). This is essentially a proxy like a border HTTP proxy.
    - Billing: Traffic is billed on a per-call basis between carriers (not free for all like Internet)
    - **Protocols**
        - Media and signalling is handled differently
        - Media: RTP + RTCP
            - Real-time Transport Protocol over UDP. L7 not L4 protocol.
                - Used for all sorts of streaming media: audio, video, WebRTC, Zoom...
            - RTP control protocol: Reporting reception quality
        - SIP + RTP + RTCP
            - Session Initiation Protocol (**SIP**)
                - handles the signalling: Register, Call setup, Call teardown, SMS, DTMF, etc. Most popular protocol.
            - SMS was a control channel for GSM
                - This a signalling than media
        - H.323 + RTP: Alternative to SIP (Mostly by Cisco)
![[Screen Shot 2022-12-11 at 17.43.00.png]]
- Smaller voice provider buy access from RBOCs to access and route traffic through the core network
- VoIP provider can subcontract/wholesale VoIP service
    - Subcontractor and contract out the service
    - Partly why so many robo calls
    - Too many VoIP carriers
- PBX + Corp phone service moved to VoIP
    - Provide private phone system

## Security Examples

### Caller ID Spoofing 101
- SIP uses “INVITE” messages to setup a call.
- The caller sets the “From” field when they place a call.
- There is a good reasons, despite trivial.
    - Call center calling, individual support caller need a proper phone number
- FCC pushing STIR/SHAKEN protocol
    - SIP Header is cryptographically signed with provider identity
    - Destination can determine which provider the call originated, and provider can determine the true caller because billing
    - Hence some call is verified

### Lawful (or Unlawful) Intercept
- Wiretapping and US Law
    - Pen Register / Dialed Number Recorder (DNR)
        - Captures dialed digits and signaling information
    - Full Audio Interception (Title III or FISA)
        - Captures signaling information plus call audio
        - Typically only authorized for particular a party
        - More laborious; higher standard of proof and judicial scrutiny
- Communication Assistance for Law
- **Mandates a standard (J-STD-025A) between TSP and LEAs**
- Data separated into two channels:
    - Call Data Channel (CDC)
        - Signaling data: call times, numbers dialed, line status, etc
    - Call Content Channel (CCC)
        - Live audio
- Channels can be sent over POTS line, ISDN, or IP
- VoIP and CALEA
    - Traffic on IP networks can be intercepted without a warrant.
    - What is the implication for voice traffic carried on IP networks?
    - Traditional voice telephony is not end- to-end encrypted, but VoIP  sometimes is... 
        - Some apps are highly suspected to provide  CALEA compliance (e.g., Skype).
- Weaknesses in CALEA Infrastructure
    - access to CALEA infrastructure is extremely difficult to  obtain.
    - One study looked at analog wiretap equipment
        - *“Can They Hear Me Now? A Security Analysis of Law Enforcement Wiretaps” Sherr, Shah, Cronin, Sandy Clark, Matt Blaze. CCS 2009*
        - Tl;dr: Targets can trick CALEA equipment by exploiting differences in analog thresholds (e.g., DTMF) and in-band signalling. This affects Integrity/ Availability of information.
- Unlawful Access through CALEA
    - Huawei has been accused by the US and allies of providing surreptitious access to CALEA interfaces on equipment, presumably for surveillance and espionage.
        - Huawei denies the claims, and evidence is scant either way.
        - If true, this is devastating and explains US bans on Huawei telco equipment.
    - “Athens Affair” — government officials were surveilled on Vodafone Greece between 2004-2005
        - Root kits were installed on Vodafone’s exchanges to exploit the LEA interfaces for surveillance.
        - Greek authorities investigated and accused the US NSA of the attacks.

# Wireless
- Wireless Network Characteristics
    - Higher Error rates
        - 4% BER nominal
    - Low bandwidth
    - Variable delay
        - Jitter
    - Inconsistent Performance
    - Easy mobility!
    - Easier Infra deployment
- Wired connection BER 1 in 10,000
- Primary wireless access to wired networks
    - Get the user data to the wire side as fast as possible
- Communications infrastructure is the air
    - Licensed - payed for access
    - Unlicensed - ISM band
        - Equipment needs to be certified
        - Amateure Radio band
- Harsh environment
    - Constant changing condition: Use adaptation
    - High error rate: FEC-based channel coding
        - LTE use advanced FEC, turbo code
    - Bursty errors due to sudden fades: interleaving
    - Higher layer error recovery
- Mobility
    - Signal strength varied with location
    - Motion affect signals - Doppler effect
    - Base station handoffs

## Phy Layer
### Modulation
$$ 
A_c \cos (2\pi f_c t + \phi)
$$
- A carrier frequency is what is been modulated.
- Quadrature amplitude modulation modulates both a sine wave and cosine wave along phase and amplitude

### Voice Encoding
- GSM-FR/PCM/G.711
- Pulse Code Modulation (**PCM**) is the basis for GSM Full-Rate (**GSM-FR**) voice encoding
- 8 kHz samples (64 kbps) reduced to 13.2 kpbs using Regular Pulse Excitation - Long Term Prediction (**RPE-LTP**)
- Converted back to 64 kpbs at MSC prior to Release 4
    - Changes in core towards "TrFO" for all IP

### Frequency Allocations
[US Frequency Allocation Chart](https://ntia.gov/sites/default/files/publications/january_2016_spectrum_wall_chart_0.pdf)
- 5G: All of these + 3.4GHz + 28GHz and 39GHz

- Orthogonal signals does not interfere with each other
- Phase, frequency, and data sequence can be orthogonal

- **Quadrature**
    - Cosines (I) and Sines (Q) at same frequency and phase can be amplitude modulated and summed to create arbitrary modulated waveforms
    - This is the basic premise of **QAM** as well as how radio signals are sampled digitally (e.g., by an SDR)
- **Powers**
    - The most important for wireless is **dBm**: “decibels wrt the milliwatt”.
        - 1 dBm = 10 log (power in mw)
        - 0 dBm = 1mW
        - 30 dBm = 1 Watt
- Decibel - Audio
    - Sound Pressure Level (**SPL**)
- If a signal is transmitted at 10 watts and is measured at 6 watts at the receiver, what is the signal decrease factor (in dB)?
$$ G = 10 \log(6 / 10) = - 2.22 dB$$
- Physical Layer Degradation
    - Free space propagation model
        - assumes a transmit antenna and a receive antenna to be located in an otherwise empty environment. Neither absorbing obstacles nor reflecting surfaces are considered. In particular, the [influence of the earth surface](http://www.wirelesscommunication.nl/reference/chaptr03/pel/pel.htm) is assumed to be entirely absent.
        - Signal strength diminishes inversely with distance to power *n*, where *n* between 2 to 4
        - Received power is inversely proportional to the square of the distance between transmitter and receiver. 
        - $P_r(d) = {P_t G_t G_r \lambda^2 \over (4 \pi)^2 d^2}$
        - Where $G_t$ and $G_r$ are the tx and rx antenna gains, $d$ distance, and $\lambda$ the wavelength
    - Loss calculated in decibels: $L_{dB} = 32.44 +20 \log D + 20 \log f$
        - $D$ in kilometers, and $f$ in MHz
    - Antenna gain
        - dBi = dB wrt isotropic antenna
    - Receiver Thresholds - RX sensitivity
        - Average 802.11 RX sensitivity is -80 dBm
    - Multi-path fading
        - Signal can become severely distorted due to reflection (objects larger than wavelength), scattering (objects smaller than wavelength) and diffraction (shadow fading - signal variation has a log-normal distribution).
    - Rayleigh fading (fast fading)
        - Non-line of sight
    - Inter-symbol interference (ISI)
        - Subsequent symbols can interfere with each other because of the above. Dealt with by guard intervals, rake receivers.
    - Signal to Noise Ratio
        - The practical value in than RX sensitivity is SNR
        - Receiver need a minimal SNR level to receive data
    - Shannon-Hartley theorem
        - Channel capacity $C$: theoretical upper bound on information rate of data that can be communicated at an arbitrarily low error rate using an average received signal power $S$ through an analog communication channel subject to additive white Gaussian noise(**AWGN**) of power $N$
        - $C = B \log_2(1 + {S \over N})$
        - $B$ = bandwidth in Hz
- Tradeoff: **Data Rate** vs **Distance**

## Other network layers
- OSI Protocol Model
    - Teleco World does not map cleanly to the OSI
#### Physical Layer
![[Screen Shot 2022-12-11 at 21.30.55.png]]
- Channel Sublayer: Frequency Assignments
    - FDMA
        - "Everyone go to different corner of room to chat"
    - TDMA systems
        - "Everyone take turn to talk"
    - CDMA system
        - "Every channel speak a different language"
        - Need planning in TX power
        - Not used in 4G/5G
#### MAC Layer 
- Maximize capacity and minimize delay (circuit vs packet switching)
    - FDMA, TDMA, CDMA - for voice, streaming
    - Aloha, Slotted Aloha - low delay for bursty, short messages (signaling)
    - CSMA-based protocols - bursty messages, larger number of users
    - PRMA and reservation-based - bursty, long messages, large number of users.
- Fairness/Quality of Service
    - Don’t allow a user to hog bandwidth
    - Schedule traffic to meet requirements
- Handoffs
    - Assign new channels
#### Link Layer
- Error Recovery
    - Yes or No?
    - Ordered data delivery
    - ARQ and HARQ
#### Network Layer
- Routing
    - Circuit-switching: performed at connection establishment time
    - Datagrams: performed on each packet
- Mobility
    - Address no longer equals location to route connections/messages
    - Address is strictly a logical identifier.
#### Transport Layer
- TCP
- FIX: Link-layer does it's own retransmission (ARQ and HARQ)

# Fundamentals of Mobile Networks
- Base stations are connected via switch
- Switch figure out how to route the call
- Mobile Location
    - A logical location in the cell work
    - Which cell is the user
- Mobile Tracking
    - Register with new cell tower as the device move around
- Handoff/Handover
    - Transfer/forwarding a connection to next cell tower
    - Hard vs software handover
- Pico-cell
    - Cover a room
- Femto/Micro-Cell
    - Covers a floor/street
- Macro-Cell
    - Big towers (0-10-miles)
- Satellites
- SS7 Call establishment in *Circuit-Switched Connection*
![[Screen Shot 2022-12-11 at 22.16.12.png]]
- Mobility Problems
    - Pauses in transmission
    - Possibility for new applications
    - Solution Techniques
        - Asymmetric design of applications and protocols
        - Network-based proxies to perform complex functions on behalf of mobile users.
        - Pre-fetching and caching of data

- Evolution Cellular Networks
![[Screen Shot 2022-12-11 at 22.20.15.png]]
- General Packet Radio System (**GPRS**)
- Cellular Generations are mostly marketing term
- GSM org renamed to 3GPP
- CDMA org renamed to 3GPP2!!!
- LTE-A (100MHz)
- GSM -> UMTS -> LTE -> 5G-NR
- Each generation of cellular network have massive different security level

## Architecture

### GSM
![[Screen Shot 2022-12-12 at 09.41.36.png]]
- **MS**: Mobile Subscriber/Station
- **BTS**: Base Transceiver Station
- **BSC**: Base Station Controller
    - handles layer 2 and up operation
    - could be integrated or separate HW; A logical separation
    - Mostly controls the BTS
- **MSC**: Mobile Switching Center
    - Handles multiple BSC
    - Connects to other MSC
    - responsible for handoff
    - acting as originator/termination points to PSTN/ISDN
- **HLR**: Home Location Register
    - DB for every subscriber in the network
    - Keep track of properties for each subscriber needed by the network
    - Keep track of rough location, via most recent VLR
    - Handle Roaming
- **AuC**: Authentication Center
    - Logical element, always bundled with **HLR**
    - Authenticate subscriber to the network
- **VLR**: Visitor’s Location Register
    - A logical element
    - DB of visitor locations
    - Set of MS attached to this MSC at this time
    - Manage mobility, where last time saw a device
    - Handle call origination and termination
    - 1:1 map to MSC
    - Standalone entity
- Roaming: 2 provider have agreement for provide service for each other's subscribers
- Most arch is connected via SS7 to rest of PSTN

### Basic Network Architecture
- Gateway MSC receives incoming calls for phones.
- Serving MSC assigned based on location
- HLR: Permanent registry for service profiles, pointer to VLR
- VLR: Temporary repository for profile information, pointer to SMSC.

### Call Flow
- Mobile User Registers
    - Power up/down
    - Movement
    - Periodic
- Call recipient located
    - Call routed to gateway or home MSC
    - Gateway MSC searches for called mobile (via HLRs and VLRs)
    - Mobile user is paged (determines current base station)
- Call delivered
    - Uses standard SS7 procedures
![[Screen Shot 2022-12-12 at 10.10.35.png]]
- MS-ISDN - Phone number identifier for the subscriber
![[Screen Shot 2022-12-12 at 10.21.15.png]]
### Mobile Registration
![[Screen Shot 2022-12-12 at 10.23.02.png]]
### Mobile Call Delivery
![[Screen Shot 2022-12-12 at 10.23.39.png]]
### E911
- Old 911 use your nearest cell tower to route to nearest dispatch (AKA Public Safety Answering Point **PSAP**)
- Enhanced 911 (**E911**) transmits your GPS location to PSAP

## Air Interface
- Frequency Division Multiple Access (FDMA):
    - Analog cellular - 1G
- Time Division Multiple Access (TDMA):
    - IS-54, IS-136, GSM - 2G
    - GPRS - 2.5G
- Code Division Multiple Access (CDMA):
    - IS-95 (cdmaOne) - 2G
    - IS-2000 (CDMA2000), WCDMA - 3G
### TDMA
- Combo of FDMA and TDMA
- With in a system band:
    - Many carrier frequencies 
    - Each carrier frequency divided into time slots
    - A channel defined by set of time slots on carrier frequency
- Doppler shift cause frequency changes, requiring guard frequency
- Data TX in burst, result in lower battery consumption
- Discontinuous transmission also make handoffs simpler since the mobile  device can listen to other base stations during idle time slots
- Downside, high synchronization requirement
### CDMA
- Time and Frequency synchronization requirement
- Also require all TX to the tower at roughly the same power level for CDMA code to work

## GSM Air Interface
- GSM air interface have data plane and control plane
- Data Plane
    - Common Control Channel (**CCCH**)
        - Broadcast channels
        - Channel access from Mobile
        - Procedures and Messages for Call Control
    - Traffic Channel (**TCH**)
        - Dedicated to subscriber when in a phone call
        - Some signaling for handoff
- GSM Control Functions
    - Read System Parameters
    - Register/Attach
    - Receive and Originate Cells
    - Manage Handoffs
- GSM TDMA Frames
    - A frame have *8 slots*, duration *4.615 msec*
    - *51* multiframe data structure, duration *235.365 msec*
    - 26 multiframe is 120.00 ms
- Base station use GPS disciplined oscillator to maintain microsecond accuracy
- A GSM logical channel is allocated slots, may spread over multiple frequency and time
- GSM CCCH
    - Random Access Control Channel (**RACH**) : MS -> BS (Reverse)
        - Setup and start communication with BS
    - Synchronization Channel (**SCH**) : BS -> MS (Forward)
        - Just a sine wave at center frequency for the BS for timing lock
    - Frequency Correction Channel (**FCCH**) : BS -> MS
        - Adjust for doppler effect or frequency shift in MS
    - Broadcast Control Channel (**BCCH**): BS -> MS
        - System control message
    - Paging and Access Grant Channel (**PAGCH**)
        - Page Channel (**PCH**)
        - Access Grant Channel (**AGCH**)
- GSM CCCH Structure
    - CCCH/RACH always uses Slot 0 of each frame; other seven slots for TCH
    - TCH: 26 multi-frame repeats every 120 msec (13th and 16th frames are used by Slow Associated Control Channel (SACCH) or is idle
    - Within 51 multiframes, each frame's slot 0 is used for a different **CCCH** sub channel type
        - FCCH (0); SCH (1); BCCH (2-5); PAGCH (6-9); .... FCCH (40); SCH (41); PAGCH (42-49); I (50)
![[Screen Shot 2022-12-12 at 17.43.51.png]]
- Relevant information is spread out through the carrier and time, and organized by logical channels
#### GSM: BCCH
- No Addressing
- Used to acquire system parameters, so mobile may operate with the system.
- Key parameters (contained in *RR SYSTEM INFORMATION MESSAGES*):
    - RACH control parameters
    - cell channel descriptions (frequencies)
    - neighbor cells (frequencies)
    - cell id
    - Location Area ID (LAI)
    - Control Channel description

#### GSM: FCCH and SCH
- Keeps system synchronization
- Broadcasts Basestation ID

#### GSM: Mobile Channel Access Procedures (RACH)
- Ask for resources
- MS Communicates with BS over RACH
    - Only initially and must compete for this shared resource.
- Feedback provided with AGCH
    - Points the user to a dedicated channel (Stand alone Dedicated Channel **SDCH**) for real exchanges.
- Functions:
    - Responses to paging messages
    - Location update (registration)
    - Call Origination

#### GSM: Paging Channel (PCH)
- Used to send pages to mobile devices.
    - Notifications of incoming services (e.g., voice, data, SMS)
- Done at regular intervals
    - Mobiles belong to a paging class
    - Allows the device to sleep, conserve power
- More than 1 mobile paged at a time.

#### GSM: RACH and Slotted ALOHA (Layer 2)
- Slotted ALOHA - Assumptions
    - all frames same size
    - time is divided into equal size slots, time to transmit 1  frame
    - nodes start to transmit frames only at beginning of  slots
    - clocks are synchronized
    - if 2 or more nodes transmit in slot, all nodes detect collision
- Slotted ALOHA - Operation
    - when node obtains fresh frame, it transmits in next slot 
    - no collision, node successfully transmitted the frame
    - if collision, node retransmits frame in each subsequent slot with prob. p until success
   
#### GSM: More Slotted ALOHA
- Pros
    - single active node can continuously transmit at full rate of channel
    - highly decentralized: only slots in nodes need to be in sync
    - simple
- Cons
    - collisions, wasting slots
    - idle slots
    - nodes may be able to detect collision in less than time to transmit packet
    - clock synchronization

#### GSM: Slotted ALOHA Efficiency
- Suppose N nodes with many frames to send,  each transmits in slot with probability $P$
- prob that node 1 has success in a slot  = $p(1-p)^{N-1}$
- prob that any node has a success = $Np(1-p)^{N-1}$
- For max efficiency with N  nodes, find p* that  maximizes $Np(1-p)^{N-1}$
• For many nodes, take limit of $Np*(1-p*)^{N-1}$ as $N$ goes to infinity, gives $1/e  = .37$
> [!At Best]
> Channel has maximum throughput of 37%!

#### GSM: RACH Procedures (Layer 2)
- Mobile
    - Sends assignment request with information
- Basestation
    - sends back assignment with information echoed
- Creates Radio Resource (**RR**) connection
    - “Standalone Dedicated Control Channel”
    - May be a physical channel
    - May be a traffic channel in signaling-only mode
    - May eventually be bandwidth stolen from TCH (associated control channel).

#### Basic Flow on Air Interface
**Base station**                                                 **MS**
            ----> Alert phone of incoming activity ---->
            <---- Request dedicated signaling channel <----
                    <--------- Signaling <---------
            ---------> Release Signaling channel --------->

#### GSM Signaling
- Signaling in GSM occurs over the Radio Interface Layer 3 (RIL-3).
    - Technically layer 3, but debatable from OSI perspective as application-esque things happen here.
- Control messages are handled by protocol control processes and include Call Control (**CC**), Mobility Management (**MM**), Radio Resource management (**RR**), Short Messaging Service management (**SMS**) and Supplementary Services management (**SS**).
- CC
    - Call establishment, in-call signaling, tone signaling
- MM (uses RR)
    - common: temporary ID maintenance **TMSI**, authentication, de-registration
    - Temp Mobile Subscriber ID (**TMSI**), points to a single SIM card
- RR
    - Paging, handoffs, cipher mode
- SMS
    - Text Messages
- SS
    - Call waiting, call forwarding, group call
    
#### GSM Registration
- Types
    - Power up and down
    - Location Area changes (mobility)
    - Periodic
- User Privacy
    - Mobile device may transmit real address: International Mobile Subscriber Identity (**IMSI**)
    - Get back temporary id (**TMSI**)
    - Unique to a local area
- Subsequent registrations use **TMSI**
- Overall steps
    1. Get SDCCH (RR connection established)
    2. Authenticate
    3. Cipher
    4. Update Location
    5. Release RR connection
![[Screen Shot 2022-12-15 at 14.52.18.png]]
- Registration details
![[Screen Shot 2022-12-15 at 14.52.32.png]]
- Call termination
![[Screen Shot 2022-12-15 at 14.53.43.png]]
- Call Origination
![[Screen Shot 2022-12-15 at 14.54.19.png]]
- Mobile Assisted Handoff (MAHO) (Really the base station initiated)
![[Screen Shot 2022-12-15 at 14.55.45.png]]
#### SMS
- Bi-directional
- Acknowledged Service
- Store-and-Forward Service
- 140 octets/160 characters (concatenation possible)
- Uses SDCCH signaling channel (... security implications?)
- Two services - cell broadcast and point to point
    - Cell broadcast long existed as only a standard, but was finally implemented

## UMTS Air Interface
- Using Phase Shift Keying (**PSK**)

### Code Division Multiple Access (**CDMA**)
- Higher capacity
    - interference limited = high efficiency
    - uses voice activity detection to reduce transmission bandwidth
- Improved quality
    - soft handoff
    - CDMA has frequency, spatial and time diversity to adapt to errors
- Ease of deployment
    - no frequency planning; frequency reuse = 1
- Increased privacy
    - spreads small signal (9.6kbps) over large spectrum (1.25Mbps) so that signal appears as noise
- Increased talk time
    - power control (performed 800x/sec) ensures that the MS transmits at optimum power, resulting in longer battery life.

- used in several wireless broadcast channels (cellular, satellite, etc) standards
- unique “code” assigned to each user; i.e., code set partitioning
- all users share same frequency, but each user has own “chipping” sequence (i.e., code) to encode data
- encoded signal = (original data) X (chipping sequence)
- decoding: inner-product of encoded signal and chipping sequence
- allows multiple users to “coexist” and transmit simultaneously with minimal interference (if codes are  “orthogonal”)
- What does it mean for two vectors to be orthogonal?

### Universal Mobile Telecommunications System (**UMTS**)
- Specifications:
    - Frequencies: 700, 850, 900, 1700, 1900, 2100 MHz (5 MHz channels)  worldwide; FDD
    - Chipping codes: up to 512 bits
    - Power control: up to1500x per second
    - Time division: 10 ms frames, 1 frame = 15 time slots
- Borrows extensively from GSM protocols
- Major changes:
    - CDMA Technology: Channel structure/handoffs/power control
    - Security -- increased use of cryptographic constructions
    - Data infrastructure

#### UMTS New Names from GSM
- **AGCH** -> Acquisition Indicator Channel **AICH** 
- **SDCCH** -> Dedicated Control Channel **DCCH** 
- **TCH** -> Dedicated Traffic Channel **DTCH** 

#### Channel Types
- Logical:
    - a task or use in network
- Transport:
    - a way logical data prepared
- Physical: 
    - center frequency with chipping code
![[Screen Shot 2022-12-15 at 18.27.17.png]]
[Ref Link](http://www.authorstream.com/Presentation/3627946-387767-wcdma-air-interface-fundamentals-science-technology-ppt-powerpoint/)

- Logical Channels
    - Broadcast Control Channel (**BCCH**): Provides common information about the cell to UEs.
    - Paging Control Channel (**PCCH**): Provides  information about incoming calls and how to listen for them.
    - Dedicated Control Channel (**DCCH**): A two-way assigned channel that carries control information to and from a single UE.
    - Common Control Channel (**CCCH**): A two-way shared channel that carries control information.
    - Dedicated Traffic Channel (**DTCH**): A two-way assigned channel that carries traffic to and from a single UE.
- Transport Channels
    - Dedicated Transport Channel (**DCH**): carries data to and from a specific UE
    - Broadcast Channel (**BCH**): Broadcasts network and cell information
    - Forward Access Channel (**FACH**): Carries control information to UEs for shared channels.
    - Random Access Channel (**RACH**): Carries channel requests to the network from the UE.
    - Paging Channel (**PCH**): Carries incoming call alerts.
    - Uplink Common Packet Channel (**CPCH**):  Carries packet data to the network.
    - Downlink Shared Channel (**DSCH**): Carries  packet data to the UE.
- Physical Channels: Signaling
    - Forward (to **UE**):
        - Primary Common Control Physical Channel (**PCCPCH**): Carries the **BCH**
        - Secondary Common Control Physical Channel (**SCCPCH**): Carries the **FACH** and the **PCH**
        - Synchronization Channel (**SCH**): Synchronizes time with the network
        - Common Pilot Channel (**CPICH**): Informs the user of the Primary Scrambling Code (**PSC**)
        - Acquisition Indicator Channel (**AICH**): Used to carry dedicated channel assignments to UEs
        - Paging Indication Channel (**PICH**): Provides the UE with information about how pages are sent. This informs the UE how often to wake up and listen for pages.
    - Reverse (to Node-B):
        - Physical Random Access Channel (**PRACH**): Carries the **RACH**
- Physical Channels: Traffic
    - Bi-Directional:
        - Dedicated Physical Data Channel (**DPDCH**): Carries a **DCH**
        - Dedicated Physical Control Channel (**DPCCH**): Carries control information (e.g., identifiers, power control)
    - Forward (to UE):
        - Physical Downlink Shared Channel (**PDSCH**): carries packet data to a UE.
        - CPCH Status Indication Channel (**CSICH**): Indicates the status of the **CPCH**
        - Collision Detection/Channel Assignment Indication Channel (**CD/CA-ICH**): Indicates if data sent over the **CPCH** has been successfully received or if a collision occurred.
    - Reverse (to Node-B):
        - Physical Common Packet Channel (**PCPCH**): Carries the CPCH

#### How a connection is made
![[Screen Shot 2022-12-15 at 18.35.37.png]]
- **PSC** - primary scrambling code

#### How a call is send/received
![[Screen Shot 2022-12-15 at 18.37.10.png]]
#### Handoffs
- 4 types: hard, soft, softer, network (2G <-> 3G)
- Soft handoff overview:
    - Frequency reuse = 1
    - UE will receive signal from multiple Node-Bs.
    - Extract signals of old and new tower simultaneously using different chipping codes.
    - Remain connected to old Node-B until re-registered with new Node-B

## Packet Data
- Teleco network behave very differently from IP network

### General Packet Radio Service (**GPRS**)
- GSM
    - Overlay network on basic GSM infrastructure
    - New mobile "router" introduced
    - supports both "GPRS" (2.5G) and "EDGE" (2.75G) wireless protocols
    - Replaces CSD - circuit switched data
- UMTS - 3G
    - Re-uses GPRS network from GSM
    - W/ new air interface to meet faster speed

- **SGSN** - Serving GPRS Support Node
    - Serves mobile user based on location
- **GGSN** - Gateway GPRS Support Node
    - Serves mobile user based on address
- **BTS/BSC** - new call processing and channels for data
- **HLR** - extended user profiles

![[Screen Shot 2022-12-15 at 15.33.53.png]]
- Private ip network connects SGSN and GGSN, in IPv6
- GGSN also serve as gateway router with NAT, and firewall

#### Network Attachment
- IMSI attach - Connect to the circuit switch network
    - Interacts with MSC for attach
- GPRS attach - attach to data service by network
    - Interacts with SGSN for attach
- SGSN + MSC typically the same box
##### Attach
![[Screen Shot 2022-12-15 at 15.44.15.png]]
##### Detach
![[Screen Shot 2022-12-15 at 15.44.59.png]]

#### PDP Context
- PDP context a virtual link from **MS** to **GGSN**
- Assign MS a IPv4/IPv6 address
- Associate QoS with device
- May have multiple PDP context, primary and secondary PDP context
    - Second PDP context provide different QoS terms (i.e. video streaming)
- MS -> (Activate PDP Context) SGSN <-> Create PDP Context <-> GGSN
- GPRS Tunneling Protocol (**GTP**)
    - GGSN maintain a GTP tunnel from originate device's SGSN to destination device's SGSN for correct forwarding
    - Each tunnel is differentiated by its Tunnel Endpoint Identifier (**TEI**).
        - Allocate and manage local address of MS without informing **GGSN**
    - The SGSN then forwards packets through the Radio Access Bearer (**RAB**)  service, which connects the core network to the wireless device.
        - Link more than one PDP context to a radio connection that is established.
        - Also handle QoS for different features.
![[Screen Shot 2022-12-15 at 15.58.48.png]]
- Everyone maintain some part of the connection state

##### GSM/GPRS Protocol Stacks
![[Screen Shot 2022-12-15 at 15.59.47.png]]
- Every entity that connects together are properly named
    - MS <-> BS == **UM** protocol

### UMTS Architecture

![[Screen Shot 2022-12-15 at 16.06.01.png]]
- Re-used from GSM/GPRS Core Network
    - **SGSN** - signaling interface and some access protocols change
    - **GGSN** - re-used (PDP contexts remain)
    - **HLR** - some extensions
- Main differences
    - Much higher data rates, soft handoffs
- Radio Node Controller (**RNC**)
- Node Base (Node B)
- User Equipment (**UE**)

##### UMTS/GPRS Protocol Stacks
![[Screen Shot 2022-12-15 at 16.08.02.png]]

##### Inter-SGSN Move
![[Screen Shot 2022-12-15 at 16.09.33.png]]
- Routing Areas (**RA**)

## Long Term Evolution (**LTE**)
- IP Only network
- Voice as IP service
- Packet-only architecture

#### LTE Network architecture
![[Screen Shot 2022-12-15 at 19.01.53.png]]
- Evolved UMTS Terrestrial Radio Access Network (E-UTRAN)
- Home Subscription Server (**HSS**)
    - HLR + AuC + PCRP
    - PCRP: Policy control
- Mobility Management Entity (**MME**)
    - VLR + Most of MSC
- **P-GW**: Packet Data Network (**PDN**) Gateway
- **eNodeB**: Evolved Node B
![[Screen Shot 2022-12-15 at 19.09.08.png]]

#### User Equipment (UE)
- UEs are identified by **IMEIs** – International Mobile Equipment Identifiers
    - Refers to specific **UE** – used primarily to identify stolen devices
- Subscribers are identified by **IMSIs** – International Mobile Subscriber Identifiers
- These are stored with cryptographic keys in “SIM Cards”
    - Technically called “**USIM**” in LTE, with U standing for “UMTS"

#### eNodeB
- evolved Node B — UMTS Node B + RNC + evolution
- The eNode B is the interface for UEs to communicate with the network
    - Controls radio resource allocation
    - Compression and encryption over the air
    - Routing of user data to the S-GW
    - Paging and broadcast information
- Also responsible for facilitating connections to 2G/3G core network (not shown)
    - In general, cellular infrastructure runs multiple generations simultaneously
    - This has security implications (downgrade attacks)

#### LTE Air Interface: PHY
- LTE specifies two PHY mechanisms, termed TDD and FDD.
    - The FDD variant is the vast majority of what is deployed
- FDD uses *orthogonal frequency division multiple access* (**OFDMA**) for the PHY

#### OFDMA
- Wireless transmission distortions are *frequency-dependent*
    - Macro: FSPL
    - Micro: multipath fading, local interference
- The wider your spectrum use, the more likely some parts of your transmission are affected but not others increases
- OFDMA splits the transmission into a sequence of **very** narrow channels  (7.5-15kHz), each of which will behave linearly
    - Each user is assigned time slots on a subset of the available channels
- This simplifies receiver design
- Transmission permissions are allocated across time and frequency, per resource block

![[lte_frame.png]]
- Related [[LTE Physical Layer Overview]]

#### LTE Layer 2: Packet Data Convergence Protocol (**PDCP**)
- Encryption/Integrity protection
    - Only control flow
- Compression
- Queueing/Buffering and reliable transmission (like during handoff)

#### LTE Layer 3: Radio Resource Control (**RRC**)
- RRC is a connection-oriented protocol between the eNodeB and the UE
- Everything goes on at eNodeB doing happens at this level:
    - System Information Broadcasts
    - Resource scheduling and allocation
    - Enabling security
    - Cell selection

#### AS and NAS for the RAN
- LTE Standards make a distinction between “Access Stratum” and “Non-access 
stratum”
- NAS == Control Plane Messages
    - SMS
    - IOT stratum
- AS == Data plane

#### Evolved Packet Core (**EPC**)
- EPC is the term for all LTE core elements, including packet gateways, the HSS, and the MME
- It distinguishes new core elements from those that might coexist from previous generations (MSC, GGSN, etc.)
- LTE is essentially all-IP internally, so the distinction between SS7 and IP traffic  isn’t helpful anymore
- LTE still distinguishes:
    - control plane data (registration, pages, tracking area updates)
    - User data (cat videos, Instagram, etc.)

#### Data Core
- Data is moved from the eNodeB by the Serving Gateway (S-GW)
    - Equivalent to old SGSN
    - Routes and delivers packets
    - Facilitates mobility and handover to GSM/UMTS
- Data is moved to the Internet with the P-GW
    - Equivalent to old GGSN
    - PDN-Gateway — Packet Data Network
    - IP address allocation, can facilitate handoff to CDMA

#### Mobility Management Entity
- The MME takes over much of the job of the old VLR
- MMEs manage Tracking Areas (equivalent to Location Areas in GSM/UMTS)
    - They keep track of what UEs are in the tracking area and facilitate Tracking Area Updates (TAUs)
    - They also select S-GW and P-GW
    - Manage MME changes
    - Handles NAS/AS security and Authentication (just like the VLR)

#### Home Subscription Server
- The HSS is a database that keeps track of information about every subscriber
    - Includes the **IMSI**, service parameters (e.g., data speeds, amounts)
    - Stores long-term keys in a subfunction called an Authentication Center (**AuC**)
    - Keeps track of the responsible MME for a subscriber, and updates as a device moves through the network

#### Voice
- VoLTE — Voice over LTE
    - Since data is all we have, we’ll treat voice calls as IP data using VoIP protocols (a  modified variant of SIP/RTP)
    - We’ll even set up a separate EPS (equivalent of RAB from UMTS) for higher  QoS
    - This is easier said than done.
        - Calling non-VoLTE end points?
        - What if you drive out of LTE range?
    - The network needed to add an IP Multimedia Subsystem (**IMS**) to handle this
- Include HD Voice - AMR - WB codec for audio
    - Require VoLTE end to end
    - Costly
- Use UMTS for voice as fallback
    - Circuit Switched Fall Back (**CSFB**)
    - Whole connection is downgraded to UMTS limit data usage

#### Identifiers
- IMSI — stays the same
- TMSI ==> Globally Unique Temporary Identifier (**GUTI**)
- The **IMSI** (and encryption keys) are kept in a **USIM** (UMTS Subscriber Identify Module)

![[Screen Shot 2022-12-15 at 19.58.27.png]]

![[Screen Shot 2022-12-15 at 19.58.36.png]]

#### Control Plane: Diameter and IMS
- In LTE, SS7 was replaced by Diameter (a successor protocol to RADIUS)
- Diameter is designed to provide for **AAA**: *Authentication, Authorization, and Accounting* that scales to large networks and is extensible for future network types
    - Base commands + LTE specific commands + Vendor commands
    - Attribute-Value Pairs: used to store relevant information
- Call and other media signaling is handled with the IMS (IP multimedia subsystem), which is basically a SIP-based VoIP stack with the ability to handle mobility.
- Dropped in 5G

## 5G
- Take advantage of cloud computing advancement!
- Software defined everything
    - Everything become microservice
- Leads to data-center everything
- Test project CORD (Central Office redesigned as Datacenter)
- Elastic structure
- **CUPS**: Control & User Plane Separation

#### 5G Network Architecture
![[Screen Shot 2022-12-15 at 20.21.38.png]]
- LTE features in 5G
| 5G   |                                | LTE               |
| ---- |:------------------------------ |------------------ |
| UPF  | User Plane Function            | S-GW + P-GW       |
| AMF  | Access and Mobility Management | MME               |
| SMF  | Session Management Function    | MME               |
| UDM  | Unified Data Management        | HSS               |
| PCF  | Policy Control Function        | PCRF              |
| AUSF | Authentication Server Function | AuC (part of HSS) |

- New functions
| 5G   | Term                           |  Job              |
| ---- |:------------------------------ |------------------ |
|NSSF|Network Slicing Selector Function|Choose a network slice (more later)|
|NRF|NF Repository Function|Discovery Service|
|NEF|Network Exposure Function|API Server|
|SDSF|Structured Data Storage Network Function|SQL DB|
|UDSF|UnStructured Data Storage Network Function|No-SQL DB (Key/value store)|

#### RAN
![[Screen Shot 2022-12-15 at 20.32.36.png]]
![[Screen Shot 2022-12-15 at 20.44.29.png]]
#### Cloudification
- Disaggregation
- Virtualization
- Commonditization

#### Software Defined Networks
![[Screen Shot 2022-12-15 at 21.00.27.png]]

- Open Networking OS (ONOS)
![[Screen Shot 2022-12-15 at 21.05.21.png]]

#### RAN Slicing
????




# Reference
---
- [Reaves](https://people.engr.ncsu.edu/bgreaves/)
- [Supplemental Reading](https://docs.google.com/document/d/1358f2ePV1LHrYfEiaQhOsVg3qDpmORLTJ1VL0mD6TPc/edit?usp=sharing)
- [How does PSTN work](https://www.nextiva.com/blog/what-is-pstn.html)
- [PSTN Infra](https://flylib.com/books/en/2.566.1/the_pstn_infrastructure.html)