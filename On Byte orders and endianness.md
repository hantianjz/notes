---
publish: true
review-frequency: normal
---
2022-06-04-Sa
Author:: ?
Date published: ?
Type:: #notes
Tags:: [[endian]], [[systems]]

# The byte order fallacy
If your code contains `#ifdef BIG_ENDIAN` or the equivalent, you need to unlearn about byte order.

```c
  i = *((int*)data);  
  #ifdef BIG_ENDIAN  
  /* swap the bytes */  
  
  i = ((i&0xFF)<<24) | (((i>>8)&0xFF)<<16) |(((i>>16)&0xFF)<<8) | (((i>>24)&0xFF)<<0);  
    
  #endif
```

or something similar. I've seen code like that many times. Why not do it that way? Well, for starters:

1.  It's more code.
2.  It assumes integers are addressable at any byte offset; on some machines that's not true.
3.  It depends on integers being 32 bits long, or requires more `#ifdefs` to pick a 32-bit integer type.
4.  It may be a little faster on little-endian machines, but not much, and it's slower on big-endian machines.
5.  If you're using a little-endian machine when you write this, there's no way to test the big-endian code.
6.  It swaps the bytes, a sure sign of trouble (see below).


```c
  i = (data[0]<<0) | (data[1]<<8) | (data[2]<<16) | (data[3]<<24);  
  i = (data[3]<<0) | (data[2]<<8) | (data[1]<<16) | (data[0]<<24);
```

By contrast, my version of the code:
1.  Is shorter.
2.  Does not depend on alignment issues.
3.  Computes a 32-bit integer value regardless of the local size of integers.
4.  Is equally fast regardless of local endianness, and fast enough (especially on modern processors) anyway.
5.  Runs the same code on all computers: I can state with confidence that if it works on a little-endian machine it will work on a big-endian machine.
6.  Never "byte swaps".

---
# Reference
- [Byte order fallacy](https://commandcenter.blogspot.com/2012/04/byte-order-fallacy.html)