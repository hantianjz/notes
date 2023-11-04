---
publish: true
review-frequency: normal
link:
- '[[code tagging]]'
tags:
- documentation
---
2021-12-29-We

# what and how is gtags

Generate tags into 3 files:
- **GTAGS**: Similar to [[What and How is ctags|ctags]] files, definition of symbols
- **GPATH**: Sorted index of source files mapped to a index value, for easy binary search in both direction
- **GRTAGS**: Symbol references and their corresponding file and line number

Each line is new symbol entry. Each entry is spliced by tabs for each fields.

Typically generated tag files are in binary format, but can be dumped to text format via `$ gtags -d <tag file>`

## GPATH
```
./libusb/version_nano.h	41
./msvc/config.h	95
./msvc/dpfp_2013.vcxproj	131	o
./msvc/dpfp_2013.vcxproj.filters	118	o
```

The format seems to be: `<file path> <index> <unknown flag?>`

The `unknown flag` seems to be an indication that if the source file contain any symbols

---
# References
https://www.gnu.org/software/global/