---
publish: true
review-frequency: normal
---
Last Updated: 2022-03-05
Type:: #documentation 
Tags: [[zsh]], [[shell]], [[auto complete]]

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