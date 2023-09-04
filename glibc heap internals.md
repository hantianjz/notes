---
publish: true
reviewed: 2023-05-27
review-frequency: normal
---
Last Updated: 2023-05-27
Type:: #documentation 
Tags:: [[glibc]], [[c]], [[heap]], [[malloc]]

# glibc heap internals

## malloc_chunk
```
struct malloc_chunk {
INTERNAL_SIZE_T mchunk_prev_size;  /* Size of previous chunk, if it is free. */
INTERNAL_SIZE_T mchunk_size;  /* Size in bytes, including overhead. */
struct malloc_chunk* fd;  /* double links -- used only if this chunk is free. */
struct malloc_chunk* bk;
/* Only used for large blocks: pointer to next larger size. */
struct malloc_chunk* fd_nextsize; /* double links -- used only if this chunk is free. */
struct malloc_chunk* bk_nextsize;
};

typedef struct malloc_chunk* mchunkptr;
```

## Allocated Chunk
```
    chunk-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |             Size of previous chunk, if unallocated (P clear)  |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |             Size of chunk, in bytes                     |A|M|P|
      mem-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |             User data starts here...                          .
            .                                                               .
            .             (malloc_usable_size() bytes)                      .
            .                                                               |
nextchunk-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |             (size of chunk, but used for application data)    |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |             Size of next chunk, in bytes                |A|0|1|
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

## Free Chunk

```
    chunk-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |             Size of previous chunk, if unallocated (P clear)  |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    `head:' |             Size of chunk, in bytes                     |A|0|P|
      mem-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |             Forward pointer to next chunk in list             |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |             Back pointer to previous chunk in list            |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |             Unused space (may be 0 bytes long)                .
            .                                                               .
            .                                                               |
nextchunk-> +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    `foot:' |             Size of chunk, in bytes                           |
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |             Size of next chunk, in bytes                |A|0|0|
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

Free chunks maintain themselves in a circular doubly linked list.

**P (PREV_INUSE)**: 0 when previous chunk (not the previous chunk in the linked list, but the one directly before it in memory) is free (and hence the size of previous chunk is stored in the first field). The very first chunk allocated has this bit set. If it is 1, then we cannot determine the size of the previous chunk.

**M (IS_MMAPPED)**: The chunk is obtained through `mmap`. The other two bits are ignored. `mmapped` chunks are neither in an arena, not adjacent to a free chunk.

**A (NON_MAIN_ARENA)**: 0 for chunks in the main arena. Each thread spawned receives its own arena and for those chunks, this bit is set.

_Note_: Chunks in fastbins are treated as _allocated_ chunks in the sense that they are not consolidated with neighboring free chunks.

---
# References
- https://heap-exploitation.dhavalkapil.com/