---
publish: true
review-frequency: normal
link:
- '[[HOWTO]]'
- '[[Linux]]'
tags:
- documentation
---
2021-12-29-We

# How to build&install Polybar

```bash
$ sudo apt install libxcb1 libxcb-composite0-dev libxcb-randr0-dev libxcb1-dev libxcb-xrm0-dev libxcb-icccm4-dev  libxcb-ewmh-dev libxcb-util-dev libxcb-util-dev libxcb-image0-dev libxcb-xkb-dev 
$ sudo apt install python3-xcbgen libnl-3-dev libasound2-dev libjsoncpp-dev libcairo2-dev libcurl4-openssl-dev
```

```bash
$ ./build.sh -a -f -3 -p -n -c -i -j 8
```

---
# References