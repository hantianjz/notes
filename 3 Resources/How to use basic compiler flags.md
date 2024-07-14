---
publish: true
review-frequency: normal
link:
- '[[gcc]]'
- '[[clang]]'
- '[[link script]]'
tags:
- idea
---
2021-12-29-We
Update: 2022-04-30

# How to compiler flags

## Turn on all warnings
-   `-Wall` and `-Wextra` on GCC
-   `-Weverything` on Clang
-   `/W4 or /Wall` on MSVC

## Recommended flags
`-Werror -Wextra -Wall -Wfloat-equal -Wconversion -Wredundant-decls -Wswitch-default -pedantic`
[Source](https://betterembsw.blogspot.com/2022/12/what-compiler-warnings-should-you-enable.html)
## Preprocessor 
- `-E` Do nothing except preprocessing
- `-M`  Output list of headers depended input source, imply `-E`. If `-o file`  output to *file*
- `-MD`  `-M` without `-E`
- `-MM` Produce the same header dependencies but without the system headers
- `-MMD`  `-MM` without `-E` 

## Undefined Behaviour
- `-fsanitize=undefined` Detect undefined behaviour
    - Clang fsanitize flag https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html

---
# References
- https://gcc.gnu.org/onlinedocs/gcc/Preprocessor-Options.html