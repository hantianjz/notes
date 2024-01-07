---
reviewed: 
review-frequency: ignore
tags:
  - documentation
link:
  - "[[systems]]"
  - "[[git]]"
---
- Directory specific gitconfig
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

- [Git history rewrite guidelines](https://github.com/kimgr/git-rewrite-guide)

- Use `git reflog` to revert a rebase or any other git operation 

---
# References