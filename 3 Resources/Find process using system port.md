---
publish: true
reviewed: 2023-06-14
review-frequency: low
link:
- '[[network]]'
- '[[macOS]]'
tags:
- documentation
---

# Find process using system port

## netstat
```
netstat -vanp tcp | grep <port number>
```

## lsof
```
lsof -i tcp:<port number>
```

---
# References
- https://stackoverflow.com/a/3855359