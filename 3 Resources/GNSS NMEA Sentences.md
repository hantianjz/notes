---
publish: false
reviewed: 2023-02-14
review-frequency: normal
link:
- '[[gps]]'
- '[[gnss]]'
- '[[nmea]]'
- '[[Notes todo]]'
tags:
- documentation
---

# GNSS NMEA Sentences

## NMEA 0183 compliant sentences
### GGA : Global Positioning System Fix Data
`$--GGA,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx*hh<CR><LF>`

| Field              | Format     | description            |
| ------------------ | ---------- | ---------------------- |
| Header             | $          |                        |
| Talker ID          | --         | GP                     |
| Sentence ID        | GGA        |                        |
| UTC of position    | hhmmss.ss  |                        |
| Latitude           | llll.ll    |                        |
| Latitidue - N/S    | a          | N: North, S: South     |
| Longitude          | yyyy.yy    |                        |
| Longitude - E/W    | a          | E: East, W: West       |
| Quality indicator  | x          | 0: Not avail           |
|                    |            | 1: Valid               |
|                    |            | 2: Valid, Differential |
|                    |            | 6: Dead Reckoning      |
| Num of sat in use  | xx         |                        |
| HDOP               | x.x        |                        |
| Altitude           | x.x,M      | meters                 |
| Geoidal separation | x.x,M      | meters                 |
| Age of DGPS data   | x.x        |                        |
| Diff station ID    | xxxx       |                        |
| Checksum           | * hh       |                        |
| Termination        | `<CR><LF>` |                        |

### GLL : Geographic Position – Latitude / Longitude
`$--GLL,llll.ll,a,yyyyy.yy,a,hhmmss.ss,A,a*hh<CR><LF>`

| Field           | Format     | description            |
| --------------- | ---------- | ---------------------- |
| Header          | $          |                        |
| Talker ID       | --         | GP: GPS                |
|                 |            | GL: GLONASS            |
|                 |            | GA: Galileo            |
|                 |            | BD: BeiDou             |
|                 |            | GQ: QZS                |
|                 |            | GN: Combined           |
| Sentence ID     | GLL        |                        |
| UTC of position | hhmmss.ss  |                        |
| Latitude        | llll.ll    |                        |
| Latitidue - N/S | a          | N: North, S: South     |
| Longitude       | yyyy.yy    |                        |
| Longitude - E/W | a          | E: East, W: West       |
| UTC of position | hhmmss.ss  |                        |
| Status          | A          | A: Valid, V: Not Valid |
| Mode Indicator  | a          | A: Autonomous          |
|                 |            | D: Differential        |
|                 |            | E: Dead reckoning      |
|                 |            | N: Data not valid      |
| Checksum        | * hh       |                        |
| Termination     | `<CR><LF>` |                        |

### GNS: GNSS Fix Data
`$--GNS,hhmmss.ss,llll.ll,a,yyyyy.yy,a,c--c,xx,x.x,x.x,M,x.x,M,x.x,xxxx,a*hh<CR><LF>`

| Field              | Format     | description           |
| ------------------ | ---------- | --------------------- |
| Header             | $          |                       |
| Talker ID          | --         | GP: GPS               |
|                    |            | GL: GLONASS           |
|                    |            | GA: Galileo           |
|                    |            | BD: BeiDou            |
|                    |            | GQ: QZS               |
|                    |            | GN: Combined          |
| Sentence ID        | GNS        |                       |
| UTC of position    | hhmmss.ss  |                       |
| Latitude           | llll.ll    |                       |
| Latitidue - N/S    | a          | N: North, S: South    |
| Longitude          | yyyy.yy    |                       |
| Longitude - E/W    | a          | E: East, W: West      |
| Mode Indicator     | c-c        | 1st: GPS, 2nd Glonass |
|                    |            | A: Autonomous         |
|                    |            | D: Differential       |
|                    |            | E: Dead reckoning     |
|                    |            | N: Data not valid     |
| Num of sat in use  | xx         |                       |
| HDOP               | x.x        |                       |
| Altitude           | x.x,M      | meters                |
| Geoidal separation | x.x,M      | meters                |
| Age of DGPS data   | x.x        |                       |
| Diff station ID    | xxxx       |                       |
| Nav status         | a          |                       |
| Checksum           | * hh       |                       |
| Termination        | `<CR><LF>` |                       |
|                    |            |                       |

### GSA: GNSS DOP and Active Satellites
`$--GSA,a,x,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,x.x,x.x,x.x,h*hh<CR><LF>`

| Field          | Format     | description                    |
| -------------- | ---------- | ------------------------------ |
| Header         | $          |                                |
| Talker ID      | --         | GP: GPS                        |
|                |            | GL: GLONASS                    |
|                |            | GA: Galileo                    |
|                |            | BD: BeiDou                     |
|                |            | GQ: QZS                        |
|                |            | GN: Combined                   |
| Sentence ID    | GSA        |                                |
| 2D/3D Mode     | a          | A: Automatically switch 2D/3D  |
| Mode           | x          | 1: Fix not avail; 2: 2D; 3: 3D |
| Used Sat #1    | xx         |                                |
| .              |            |                                |
| .              |            |                                |
| Used Sat #12   | xx         |                                |
| PDOP           | x.x        |                                |
| HDOP           | x.x        |                                |
| VDOP           | x.x        |                                |
| GNSS System ID | h          | 1: GPS                         |
|                |            | 2: GLONASS                     |
|                |            | 3: Galileo                     |
|                |            | 4: BeiDou                      |
|                |            | 5:  QZSS                       |
| Checksum       | * hh       |                                |
| Termination    | `<CR><LF>` |                                |

### GSV: GNSS Satellites In View
`$--GSV,x,x,xx,xx,xx,xxx,xx,.......,xx,xx,xxx,xx,h*hh<CR><LF>`

| Field               | Format     | description                |
| ------------------- | ---------- | -------------------------- |
| Header              | $          |                            |
| Talker ID           | --         | GP: GPS                    |
|                     |            | GL: GLONASS                |
|                     |            | GA: Galileo                |
|                     |            | BD: BeiDou                 |
|                     |            | GQ: QZS                    |
|                     |            | GN: Combined               |
| Sentence ID         | GSV        |                            |
| Total # of sentence | x          |                            |
| Sentences num       | x          |                            |
| num of sat in view  | xx         |                            |
| ------SVx---------- | ---------- | --------------             |
| Sat ID              | xx         |                            |
| Elevation           | xx         | degree                     |
| Azimuth             | xxx        | degree                     |
| SNR (C/N)           | xx         | dB-Hz (Null if no acquire) |
| ------------------- | ---------- | --------------             |
| Signal ID           | h          |                            |
| Checksum            | * hh       |                            |
| Termination         | `<CR><LF>` |                            |

### RMC: Recommended Minimum Specific GNSS Data
`$--RMC,hhmmss.ss,A,llll.ll,a,yyyyy.yy,a,x.x,x.x,xxxxxx,x.x,a,a,a*hh<CR><LF>`

| Field              | Format     | description            |
| ------------------ | ---------- | ---------------------- |
| Header             | $          |                        |
| Talker ID          | --         | GP: GPS                |
|                    |            | GL: GLONASS            |
|                    |            | GA: Galileo            |
|                    |            | BD: BeiDou             |
|                    |            | GQ: QZS                |
|                    |            | GN: Combined           |
| Sentence ID        | RMC        |                        |
| UTC of fix         | hhmmss.ss  |                        |
| Status             | A          | A: Valid; V: Not valid |
| Latitude           | llll.ll    |                        |
| Latitidue - N/S    | a          | N: North, S: South     |
| Longitude          | yyyy.yy    |                        |
| Longitude - E/W    | a          | E: East, W: West       |
| Speed              | x.x        | knot                   |
| Course             | x.x        | degree                 |
| Date               | xxxxxx     | ddmmyy                 |
| Magnetic variation | x.x        | degree                 |
| Mode Indicator     | a          | A: Autonomous          |
|                    |            | D: Differential        |
|                    |            | E: Dead reckoning      |
|                    |            | N: Data not valid      |
| Navigation Status  | a          |                        |
| Checksum           | * hh       |                        |
| Termination        | `<CR><LF>` |                        |
|                    |            |                        |

### VTG: Course Over Ground & Ground Speed
`$--VTG,x.x,T,x.x,M,x.x,N,x.x,K,a*hh<CR><LF>`

### ZDA: Time & Date
`$--ZDA,hhmmss.ss,xx,xx,xxxx,xx,xx*hh<CR><LF>`

| Field              | Format     | description  |
| ------------------ | ---------- | ------------ |
| Header             | $          |              |
| Talker ID          | --         | GP: GPS      |
|                    |            | GL: GLONASS  |
|                    |            | GA: Galileo  |
|                    |            | BD: BeiDou   |
|                    |            | GQ: QZS      |
|                    |            | GN: Combined |
| Sentence ID        | ZDA        |              |
| UTC of fix         | hhmmss.ss  |              |
| Day                | xx         |              |
| Month              | xx         |              |
| Year               | xxxx       |              |
| Local Zone hours   | xx         |              |
| Local Zone minutes | xx         |              |
| Checksum           | * hh       |              |
| Termination        | `<CR><LF>` |              |
|                    |            |              |


## Satellite ID

| Sat System    | Talker ID | Sat ID |
| ------------- | --------- | ------ |
| GPS           | GP        | 1-32   |
| SBAS          | GP        | 33-64  |
| GLONASS       | GL        | 65-88  |
| Galileo       | GA        | 1-36   |
| BeiDou        | BD        | 1-30   |
| QZSS (L1 C/A) | GQ        | 1-10   |
| QZSS (L1S)    | GQ        | 55-63  |


---
# References