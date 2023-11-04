---
publish: true
review-frequency: normal
link:
- '[[ABI]]'
- '[[executable]]'
- '[[OS]]'
- '[[C]]'
- '[[gcc]]'
tags:
- idea
---
# How APE(Actually Portable Executable) work

TLDR: Build OS independent executable with external static lib and linker script to ensure the executable binary is almost polymorphic.

Build binary with GCC that work on any OS, include BIOS.
```
gcc 
-g 
-O 
-static 
-fno-pie 
-no-pie 
-mno-red-zone 
-nostdlib 
-nostdinc 
-o hello.com 
hello.c 
-Wl,--oformat=binary 
-Wl,--gc-sections 
-Wl,-z,max-page-size=0x1000 
-fuse-ld=bfd 
-Wl,-T,ape.lds # https://justine.lol/cosmopolitan/ape.lds
-include 
cosmopolitan.h # https://justine.lol/cosmopolitan/cosmopolitan.h 
crt.o # https://justine.lol/cosmopolitan/crt.o
ape.o # https://justine.lol/cosmopolitan/ape.o
cosmopolitan.a # https://justine.lol/cosmopolitan/cosmopolitan.a
```
It requires a minor ABI change, where C preprocessor macros relating to system interfaces need to be symbolic. This is barely an issue, except in cases like `switch(errno){case EINVAL:...}`. If we feel comfortable bending the rules, then the GNU Linker can easily be configured to generate at linktime all the PE/Darwin data structures we need, without any special toolchains.

---
# References
https://justine.lol/ape.html