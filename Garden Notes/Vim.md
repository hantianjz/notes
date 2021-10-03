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
