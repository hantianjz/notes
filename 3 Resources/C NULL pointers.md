---
publish: true
review-frequency: normal
link:
- '[[C]]'
- '[[NULL]]'
- '[[plagiarize]]'
tags:
- notes
---
2022-01-03-Mo
Date published: ?

# C NULL pointers

Null pointers are complicated. In C, they are a horrible compromise because not all targets used a zero bit pattern to represent null. Any integer constant expression that evaluates to zero, and any such expression cast to any pointer type, are defined to be null pointers by the C spec. The following are all null pointers (or, at least, may be depending on context):

```
0;
(void*)0;
1-1;
(char*)(42 - 12 - 30);
```

The following is not a null pointer:

```
int x = 1;
int *notNull = (int*)(x-1);
```

Though in most implementations it will happen to have the same bit pattern as a null pointer and so will compare equal to one. Relying on this will bite you on some mainframes where the null pointer bit pattern is not 0 and address 0 is a valid address.

There is also a macro in C called `NULL` that must be defined as a valid null pointer constant. Any of the examples above is a valid definition of this macro. Most implementations define it as `(void*)0` because of one very painful corner case in C. Consider the following C function declaration and call:

```
/// Append a null-terminated list of pointers to the container.
void appendValues(struct SomeContainer *c, ...);

appendValues(&container, &a, &b, &c, &d, NULL);
```

On most 64-bit (LP64) C ABIs, if `NULL` is defined as `0` (which, remember, _is_ a valid definition) then this will fail. The compiler will pass five pointers and one 32-bit integer to the variadic function and the high or low (depending on the target endian) 32 bits of the final pointer will be undefined and are likely to not be zero (this gets more likely as you add more arguments - in register the value may end up being sign extended, on the stack it will not and so you’ll read 4 bytes from outside of the argument frame).

To prevent this kind of breakage, the null pointer macro must be defined with a cast to a pointer type (and I’ve never seen an implementation where it wasn’t). In C++, this introduced some difficulty. C permits implicitly casting from `void*` to any pointer type (which is a big part of the reason that the author of the article refers to it as ‘The Type Safety Is For Losers Language’). This means that it is completely valid to write:

```
int *x = (void*)0;
```

C++ does not have this escape hatch. If you’re doing dangerous things with pointers in C++ then you must do it explicitly. You can cast any pointer type _to_ a `void*` (mostly for compatibility with C APIs) but the converse cast must be explicit, to highlight in the code that you’re doing a dangerous thing.

In C++98, this meant that a definition of `NULL` as `(void*)0` required a cast on every use. This was annoying and so the recommendation was to use `0` and an explicit cast to a pointer type if necessary (for examples, as in `appendValues`). This was not very satisfactory because in a language that at least sometimes pretends to be type safe, it’s a good idea if integers and pointers are not confused, even in the specific case of null.

C++11 introduced `nullptr` and `std::nullptr_t` to address this. In C++11, null is not just some constant integer value, it is a singleton value, `nullptr` (which may, as with C, have any bit pattern representation) and it is of the type `nullptr_t`, which may be cast to any pointer type. Because it is a separate type, it also participates in overload resolution, which is useful for some compile-time checks because it allows you to specialise methods or templated functions differently if one parameter is known at compile time to be null (including `static_assert`ing that it shouldn’t be).

In most C++11 headers, the C `NULL` macro is defined to be `nullptr` and so `NULL` can be used in both languages.

---
# Reference
https://lobste.rs/s/7ivi7x/why_c_language_will_never_stop_you_from#c_esb7oh