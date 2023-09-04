---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #notes #idea 
Tags:: [[DNS]], [[Network Protocol]]

# Hello DNS

- RFC 882 & 883, similar not current DNS
- RFC 1034 & 1035, current

- DNS packet contain arbitrary data
- _A_ IPv4 Address, _AAAA_ IPv6 address, _MX_ mail server
- _NS_, _CNAME_, _SOA_ for DNS protocal usage
- Normally over UDP, but TCP support is mandatory now
- DNS message has:
	- A header
	- A query name and query type
	- An answer section
	- An authority section
	- an additional section

Header fields relevant to queries and responses:
- ID: 16 bits
- QR: 1 bit (0 if query, 1 if response)
- OPCODE: 4 bit (0 standard query)
- RD: 1 bit (Question want recursion)

Fields for response:
- AA: 1 bit (Response have Authoritative Answer)
- RA: 1 bit (Recursive service available)
- TC: 1 bit (Truncated data, not all data fit in UDP packet)
- RCODE: 4 bits (Result code, 0 OK, 2 SERVFAIL, 3 NXDOMAIN)

Field Z:
- defined to be 0 at all times

UDP easy to spoof random/unpredictable ID and UDP source port.
DNS server listen on port 53 for UDP or TCP packets.

Other header fields:
- QDCOUNT: 16 bits (Number of question in the packet, but only ever use 1. Multi question is not implemented)
- ANCOUNT: 16 bits (Number answer, 0 for question)
- NSCOUNT: 16 bits (Number of NS record, 0 for question)
- ARCOUNT: 16 bits (Number A record, 0 for question)

Query data body fields:
- qname: Length-Data pair format, terminated by 0 length, segmented by dot char in URL. Eg (3 www 4 ietf 3 org 0)
- qtype: 16 bits of type field (AAAA for IPv6 address denoted by 28 (0x1c))
- qclass: 16 bits of class type (Not implemented always set to 1)

Queries are case-insensitive, by ignoring 5th bit (0x20)

DNS answer packet should be checked UDP source port and ID is correct. Note not to send out same question twice for security.
Answer packet contain header and the original question, then follow by actual answer.

Answer fields:
- Initial 16 bits are some what arcane space saving compression method that lead to the DNS name of answer
- atype: 16 bits record type
- aclass: 16 bits answer class
- TTL: 32 bits (seconds?)
- RDLENGTH: 16 bits length (bytes)
- DATA: of RDLENGTH

Additional answer would follow first one. ANCOUNT header field will be larger than 1, or NSCOUNT, ARCOUNT fields.

RRSETs: Resource Record Sets, multiple AAAA records for the same name

Zone files: Storage format of DNS data. Section 5 of RFC 1035. Optional to use, avoid if possible.

DNS Names: Hierarchical order of DNS name is from right to left. The implication is implementation of DNS is 'key/value' pair.

## Zones
- A single domain name may have several zones include the root zone

## Start of Authority
- Zone start with Start of Authority (SoA) record
- Root zone "." always exist on all server/internet
```
.   86400   IN   SOA   a.root-servers.net. nstld.verisign-grs.com. 2018032802 1800 900 604800 86400
```

Final number of 86400, indicate if name or RRSET does not exist, will continue to not exist for 1 day.

### Zone cuts
When looking for "www.ietf.org"
Root server "." -> Nameserver provide "org" zone -> Nameserver provide "ietf" zone -> find AAAA for "www" node

### NS Records
Mandatory record for a zone, point to a SOA record. Provide where to send questions within zone, the answer will be authoritative with AA bit set.

Parent zone will also have the same NS record, but is not authoritative, AA=0

### Glue records
To obtain the IP address of the Name servers, parent zone will contain A record for name servers, but AA bit unset.

Answers with AA=0 from parent zone maybe different from AA=1 answer, resolver implementation need to take care.

## Futher aspects

### CNAME
Use CNAME record to redirect URL to CDN or load balancer.
Server follow CNAME  chain, which can loop, care needed.

### Wildcards
Wild card record are created on the fly.

### Truncation
All UDP response must fit in 512 bytes, if server need to exceed 512 bytes, TC bit needs to be set.
Originator of query will resend query over TCP.
Recommended to send empty response packet with TC=1.

### Names and nodes that do not exist
Queries for domain not exist answers RCODE NXDOMAIN or no answer records.

To make caching easier, authritative server sends a copy of SOA in Authority section of response with TTL and data of "no such name" or "no such data" to cache.

### Query type that are not RRSET types
Additional type used in queries: ANY, AXFR and IXFR.

ANY instruct nameserver return all types available for a name. Not suitable for resolvers.

AXFR and IXFR, incremental zone transfer, over TCP. Not for resolvers.

---
# References
https://powerdns.org/hello-dns/basic.md.html