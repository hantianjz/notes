---
publish: false
reviewed: 
review-frequency: ignore
tags:
  - unsorted
link: []
---

```
curl --request PUT \
  --url https://api.cloudflare.com/client/v4/zones/zone_identifier/dns_records/identifier \
  --header 'Content-Type: application/json' \
  --header 'X-Auth-Email: ' \
  --data '{
  "content": "198.51.100.4",
  "name": "example.com",
  "proxied": false,
  "type": "A",
  "comment": "Domain verification record",
  "tags": [
    "owner:dns-team"
  ],
  "ttl": 3600
}'

```

Current IP address: 71.232.14.10

`KiW3qtDnL5UiW7cHZzF8UWsDBIkFrlxl_Q37u1na`

---
# References
