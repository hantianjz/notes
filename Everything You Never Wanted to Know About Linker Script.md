---
publish: false
reviewed: 2023-06-23
review-frequency: ignore
link:
- '[[C]]'
- '[[linker]]'
tags:
- documentation
---

# Everything You Never Wanted to Know About Linker Script

## assembly files
- `.asm` on windows
- `.s` on posix system
- `.S` also when using clang with preprocessor (most hand written assembly files)
- `.s` stands for *source*

## C compilation model
**Compiler** takes source code, such as `.cc`, and lowers it down to a `.s` file
**Assembler**, _assembles_ each `.s` into a `.o` file, an object file.
**Linker**, _links_ all of your object files into a final _executable_ or _binary_, traditionally given the name `a.out` by default

This three (or two, if you do compile/assemble in one step) phase process is sometimes called the _C compilation model_. 
All modern software build infrastructure is built around this model.

## Clang
Clang, being based on LLVM, actually exposes one stage in between the `.cc` file and the `.s` file. You can ask it to skip doing codegen and emit a `.ll` file filled with LLVM IR, an intermediate between human-writable source code and assembly. The magic words to get this file are `clang -S -emit-llvm`.

The LLVM toolchain provides `llc`, the LLVM compiler, which performs the `.ll` -> `.s` step (optionally assembling it, too). `lli` is an interpreter for the IR. Studying IR is mostly useful for understanding optimization behavior; topic for another day.

## ar

Taking several `.o` files and use `ar` to create a library, always have name like `lib-foo.a` (`lib` prefix is actually mandatory).
Which can be later presented to a linker.

---

`ALLOC` Must be allocated space by the load
`LOAD` indicate a section should loaded into memory by loader

The loader is sometimes called the “dynamic linker”, and is often the same program as the “program linker”; this is why the linker is called `ld`.

Some common (POSIX) sections include:
- `.text`, where your code lives[8](https://mcyoung.xyz/2021/06/01/linker-script/#fn:text-section). It’s usually a loadable, readonly, executable section.
- `.data` contains the initial values of global variables. It’s loadable.
- `.rodata` contains constants. It’s loadable and readonly.
- `.bss` is an empty allocatable section[9](https://mcyoung.xyz/2021/06/01/linker-script/#fn:bss-section). C specifies that uninitialized globals default to zero; this is a convenient way for avoiding storing a huge block of zeros in the executable!
- Debug sections that are not loaded or allocated; these are usually removed for release builds.

---
# References
- https://mcyoung.xyz/2021/06/01/linker-script/