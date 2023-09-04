---
publish: true
review-frequency: normal
---
Last Updated: 2021-12-29
Type:: #documentation 
Tags:: [[NVM]], [[arm]], [[embedded]], [[bootloader]], [[SAMD21]]

# NVMCTRL Bootprot

## [[SAM-D21D Manual Annotation#^3zh8ncnjsj3|Sec 10.3.1]]
- The NVM User Row can be read at [[SAM-D21D Manual Annotation#^m1ne33ge1lf|address]] `0x804000`
- **Bit 2:0** Bootprot specify protected bootloader size:

## [[SAM-D21D Manual Annotation#^jndr2npth7|Sec 22.6.5]]
Table 22-2. Boot Loader Size

| BOOTPROT [2:0] | Rows Protected | Boot Loader Size |
| -------------- | -------------- | ---------------- |
| 0x7(*default*) | None           | 0                |
| 0x6            | 2              | 512              |
| 0x5            | 4              | 1024             |
| 0x4            | 8              | 2048             |
| 0x3            | 16             | 4096             |
| 0x2            | 32             | 8192             |
| 0x1            | 64             | 16384            |
| 0x0            | 128            | 32768            |