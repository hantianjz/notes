---
publish: true
review-frequency: normal
tags:
- documentation
---

# zsh auto-completion configuration
```
fpath=(/opt/local/share/zsh/site-functions $fpath)
autoload -Uz  compinit 

compinit

rm -f ~/.zcompdump; compinit
```
PS: most zsh framework do this for you

---
# Reference
- https://www.sindastra.de/p/2006/macos-fix-zsh-auto-completion-and-get-more