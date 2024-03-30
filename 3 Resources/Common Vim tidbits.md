---
publish: true
review-frequency: normal
link:
- '[[vim]]'
tags:
- documentation
---
# Common Vim tidbits

### Replace the whole buffer with output from command
```vim
:%! date 
```

### Or this can be taken even further use the current buffer as input to command
```vim
:%! xxd 
```

### Insert whole buffer with output from command
```vim
:r! date 
```

### Highlight yanked text
```vim
au TextYankPost * lua vim.highlight.on_yank {higroup="IncSearch", timeout=150, on_visual=true}
```