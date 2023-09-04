---
publish: false
reviewed: 2023-07-09
review-frequency: ignore
---
2023-07-09-Su
Type:: #notes
Tags:: 

# Malloc syscall

## brk 

 **brk**: [brk](http://lxr.free-electrons.com/source/mm/mmap.c?v=3.8#L252) obtains memory (non zero initialized) from kernel by increasing program break location ([brk](http://lxr.free-electrons.com/source/include/linux/mm_types.h?v=3.8#L365)). Initially start ([start_brk](http://lxr.free-electrons.com/source/include/linux/mm_types.h?v=3.8#L365)) and end of heap segment ([brk](http://lxr.free-electrons.com/source/include/linux/mm_types.h?v=3.8#L365)) would point to same location.
![[Pasted image 20230710000053.png]]

---
# References
- https://sploitfun.wordpress.com/2015/02/11/syscalls-used-by-malloc/