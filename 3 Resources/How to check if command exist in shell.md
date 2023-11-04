---
publish: true
review-frequency: normal
link:
- '[[bash]]'
- '[[zsh]]'
- '[[scripting]]'
- '[[shell]]'
- '[[dotfiles]]'
tags:
- documentation
---

# How to check if command exist in shell
-   `type foobar &> /dev/null`
-   `hash foobar &> /dev/null`
-   `command -v foobar &> /dev/null`
-   `which foobar &> /dev/null`
-   `(( $+commands[foobar] ))` (zsh only)

---
# Reference
- https://www.topbug.net/blog/2016/10/11/speed-test-check-the-existence-of-a-command-in-bash-and-zsh/