---
publish: false
reviewed: 
review-frequency: ignore
tags:
  - documentation
link:
  - "[[systems]]"
  - "[[git]]"
---


```
[user]
    name = Garrit Franke
    email = garrit@slashdev.space

[includeIf "gitdir:~/work/"]
    path = ~/.gitconfig-work

[includeIf "gitdir:~/work/client2/"]
    path = ~/.gitconfig-client2

[includeIf "gitdir:~/sources/"]
    path = ~/.gitconfig-personal
```


`[includeIf "gitdir:~/work/"]`

---
# References