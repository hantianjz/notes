---
publish: true
review-frequency: normal
link:
- '[[tmux]]'
- '[[dotfiles]]'
- '[[zsh]]'
- '[[development]]'
tags:
- documentation
---

# Tmux configuration details

# Tmux runs as a login shell by default
This cause `.profile` or `.zprofile` to be sourced twice which get annoying
```
set -g default-command "${SHELL}"
```

---
# Reference
https://www.gridbugs.org/daily/tmux-runs-a-login-shell-by-default/#:~:text=Unless%20configured%20otherwise%2C%20shells%20running,leading%20to%20problems%20highlighted%20here