---
publish: true
review-frequency: normal
link:
- '[[Network Protocol]]'
- '[[DNS]]'
- '[[DHCP]]'
tags:
- documentation
---

# Setup Network bridge

# dnsmasq.conf
```conf
listen-address=169.254.0.1
interface=enp0s31f6
dhcp-range=169.254.0.2,169.254.0.10,12h

log-queries
log-dhcp
```

https://serverfault.com/questions/152363/bridging-wlan0-to-eth0

# Setup NAT

One should set up NAT instead:

```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
```

## Assigning an IP

Then you have to assign IP addresses to yourself:
```bash
ifconfig eth0 10.0.0.1 netmask 255.255.255.0 up
```

## Install dhcp daemon

Install a dhcp server and add the following text to its config file (in /etc/dhcpd.conf or something similar)

```conf
subnet 10.0.0.0 netmask 255.255.255.0 {
    range 10.0.0.100 10.0.0.120;
    option routers 10.0.0.1;
    option domain-name-servers the-ip-address-you-have-in-etc-resolv.conf;
}
```