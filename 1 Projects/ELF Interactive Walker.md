---
tags:
  - project
link:
  - "[[3 Resources/Readwise/Articles/Elf]]"
---
Resource: [[20240118Thu223344|Executable and Linking Format]]
Notes: [[3 Resources/Readwise/Articles/Elf]]

- https://blog.tartanllama.xyz/writing-a-linux-debugger-setup/
- https://en.m.wikipedia.org/wiki/Executable_and_Linkable_Format
- https://medium.com/@ajmewal/basics-of-elf-executable-and-linkable-format-file-88a516877356
- http://s.eresi-project.org/inc/articles/elf-rtld.txt
- https://www.cs.cmu.edu/afs/cs/academic/class/15213-f00/docs/elf.pdf

**Goal**:
- A interactive tool to explore elf file
- Python based
- Similar to [nnn](https://github.com/jarun/nnn) style

**Helpful tools to reference**:
- dwarfdump
- readelf
- objdump

**Question to answer**:
- How does elf get converted to binary file?

## How does nnn work?
- It's written in C!
- Uses standard ncursor library 
- `static int nextsel(int presel)` handles reading input char, and translate to action
- `static bool browse(char *ipath, const char *session, int pkey)` main loop function handles

## What symbols to explore
- Filter symbol by type, sub-strings, section, etc...

**2024-03-19**
- just figure out how to print all the section headers