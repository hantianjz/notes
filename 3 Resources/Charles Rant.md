---
publish: false
reviewed: 2023-05-02
review-frequency: normal
tags:
  - documentation
link:
  - "[[C]]"
  - "[[Cpp]]"
  - "[[Charles]]"
---
**2023-05-02**
It's famously "undefined behavior" to take the address of a variable ("object") in memory and cast it to another type. There are very clearly-stated rules about how any region of memory must be inhabited by one and exactly one "type" of object.
Because of this, the compiler is allowed to fully eliminate loads + stores to memory that it has already clearly proven to itself is of type A, but the loads + stores are through type B.
This has proven over the years to be _so_ hard to think about for programmers, that most compilers _disable_ these optimizations by default, requiring you to turn them on explicitly.
if you've seen `-fstrict-aliasing` and `-fno-strict-aliasing`, those control this behavior
but, lots of things are hard to do in C if you can't just treat memory like memory and ignore the types at times
So there are escape hatches
the easiest and most famous one is casting to `char*`- it's always legal to look at the memory representation of any variable through `char*`
Also, you can always `memcpy` from wherever you want _to_ wherever you want, as long as you respect the underlying implementation details of the target. (a famous example is that the internal representation of `bool` in C++ is 1 or 0, if you memcpy the value `2` into a bool expecting it to be "true", you're in for a surprise)
There's another legal, lesser-known, and extremely handy tool we can use-
the C standard defines it as legal to cast any number of types to a single specific type, if and only if each "from" type has as its first member, the single specific "to" type.
This lets you do "inheritance" in C
```
struct base { int hello; };
struct child1 { struct base b; float x; }
struct child2 { struct base b; int y; }
```

it's perfectly legal to pass around a pointer to a `child1` or `child2` instance as a pointer to a `base` instead

if `base` had something more useful in it than `hello`, like, say, an enum containing information about whether the memory holds a `child1` or `child2` type

then it starts looking C++ish

and you could imagine virtual functions

that take a `base*` and switch on the type, cast it to the child type, and do child-type-specific work on the memory

I bring all of this up because it's also very handy for extending the factory settings page stuff. We have two options- we could make the factory settings struct a super-struct that holds more and more stuff, or we can use this simple polymorphism to make orthogonal all of the new versions of the page

```
#define FACTORY_SETTINGS_MAGIC 0xF1D0F1D0
#define FACTORY_SETTINGS_VERSION_1 0x02
#define FACTORY_SETTINGS_VERSION_2 0x03

FI_PACKED_STRUCT_BEGIN struct factory_settings_header {
  uint32_t magic;
  uint16_t version;
} FI_PACKED_STRUCT_END;

typedef struct factory_settings_header factory_settings_header_t;

FI_PACKED_STRUCT_BEGIN struct factory_settings_v1 {
  factory_settings_header_t header;
  uint16_t key_len;
  uint16_t cert_len;
  char module_id[64];
} FI_PACKED_STRUCT_END;

typedef struct factory_settings_v1 factory_settings_v1_t;

FI_PACKED_STRUCT_BEGIN struct factory_settings_v2 {
  factory_settings_header_t header;
  uint16_t key_len;
  uint16_t cert_len;
  char module_id[64];
  char platform_id[8];
} FI_PACKED_STRUCT_END;

typedef struct factory_settings_v2 factory_settings_v2_t;

static const factory_settings_header_t s_factory_header __attribute__((section(".factory_settings_page")));
```

v1 and v2 only differ by a `char platform_id[8]` but you could imagine a v3 that's much more destructive to the original fields

in this case i think a 32-bit magic value was probably slightly excessive, and it would be nice to pack a 2-byte magic and a 2-byte version field together into a single word at the top, but it doesn't really matter