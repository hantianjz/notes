---
publish: true
review-frequency: ignore
link:
- '[[Cpp]]'
- '[[Cpp11]]'
- '[[Cpp14]]'
- '[[Cpp17]]'
tags:
- notes
---
2021-12-29-We

## Auto

#### Item 5: Prefer auto to explicit type declarations
auto can be used to store function pointer or any callable object, and because it is a compile time operation it can be more efficient than using std::function() which may use heap memory.

#### Item 6: User the explicitly typed initializer idiom when _auto_ deduces undesired types
   
C++ forbids references to bits.

**`operator[] of _std::vector<bool>_`** returns **`std::vector<bool>::reference`** that emulate the behaviour of **`bool&`**

```cpp
std::vector<bool> features(const Widget& w);

auto highPriority = features(w)[5];
// Value of highPriority depend on how std::vector<bool>::reference
// is implemented.
```
**Proxy class:** A class that exists for the purpose of emulating and augmenting the behaviour of some other type.

**Expression templates:** To improve efficiency of numeric code using proxy classes.

**AVOID!!**

```cpp
auto someVar = expression of "invisible" proxy class type;
```

Typical pattern of proxy class usage:

```cpp
namespace std {

	template <class Allocator>
  class vector<bool, Allocator> {
	public:
		...
		class reference {...};
		reference operator[](size_type n);
		...
	}
}
```

**Explicitly typed initializer idiom:**

```cpp
auto highPriority = static_cast<bool>(features(w)[5]);
```