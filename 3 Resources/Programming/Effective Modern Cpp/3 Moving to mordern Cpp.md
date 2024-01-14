---
publish: true
review-frequency: low
reviewed: 2023-01-02
link:
- '[[Cpp]]'
- '[[Cpp11]]'
- '[[Cpp14]]'
- '[[Cpp17]]'
tags:
- notes
---
## Moving to Modern C++

#### Item 7: Distinguish between () and {} when creating objects
    
```cpp
int x(0);     // initializer is in parentheses
int y = 0;    // initializer follows "="
int z{0};     // initialize is in braces

// Often possible, but treated same as brances only version
int z = {0};  // initializer ues "=" and braces
```
    
"=" initialization often mistaken for assignment. This is true for built-in types, but user defined types is important to distinguish.
    
```cpp
Widget w1;           // Call default constructor
Widget w2 = w1;      // Not assignment; calls copy ctor
w1 = w2;             // an assignment; calls copy operator=
```
    
**_Uniform initialization:_** a single initialization syntax that can be used anywhere and express everything.

Braced initialization is a syntactic construct of uniform initialization.

```cpp
std::vector<int> v{1, 3, 5:; // v's initial content is 1 3 5
```
   
```cpp
class Widget {
  int x{1};       // fine, x's default value is 1
  int y = 2;      // also fine
  int z(3);       // error!
};
```

Braced initialization prohibits implicit **narrowing conversions**

```cpp
double x,y,z;
...
int sum1{x + y + z};   // error! sum of doubles may not be expressed as int

int sum2(x + y + z);   // Okay (Value of expression truncated to an int)

int sum3 = x + y + z;  // ditto
```

C++'s _most vexing parse_

```cpp
Widget w1(10);         // call Widget ctor with argument 10
Widget w2();           // most vexing parse! declares a function named w2!
Widget w3{};           // Calls Widget ctor with no args
```

Braced initialization weird tangled relationship with _std::initializer_lists._ Everything is fine as long **std::initializer_list** is not used in constructor.

```cpp
class Widget {
public:
	Widget(int i, bool b);
	Widget(int i, double d);
	Widget(std::initializer_list<long double> il);

  operator float() const;        // convert to float
};

Widget w1(10, true);   // Uses first ctor

Widget w2{10, true};   // Uses braces, but call std::initializer_list ctor
                       // (10 and true convert to long double)

Widget w3(10, 5.0);    // Uses parens and call 2nd ctor

Widget w4{10, 5.0};    // Uses braces, but call std::initializer_list ctor
                        // (10 and 5.0 convert to long double)

Widget w5(w4);         // uses parens, calls copy ctor

Widget w6{w4};         // uses braces, calls std::initializer_list ctor
                       // (w4 converts to float, and converts to long double)

Widget w7(std::move(w4)); // Uses parens, calls move ctor

Widget w8{std::move(w4)}; // Same as w6
```

Match braced initializer with **_std::initializer_lists_** constructor take priority over normal constructor.

```cpp
class Widget {
public:
	Widget();

	Widget(std::initialized_list<int> il);
	...
};

Widget w1;         // Calls default ctor

Widget w2{};       // Also calls default ctor

Widget w3();       // most vexing parse! declares a function!

Widget w4({});     // Calls std::initializer_list ctor with empty list

Widget w5{{}};     // Same as w4
```

**std::vector**

```cpp
std::vector<int> v1(10, 20);  // Use non-std::initializer_list ctor:
                              // create 10 element std::vector, all elements
                              // have value of 20

std::vector<int> v2{10, 20};  // Use std::initializer_list ctor:
                              // create 2-element std::vector with 10 and 20
```

This is a huge problem for templates, which **std::make_unique** and **std::make_shared** deal with.

#### Item 8: Prefer _nullptr_ to 0 and NULL

Literal 0 is an int, in the context of pointer it is null.

NULL maybe a integral type other than int, depend on implementation. Though not usual.

```cpp
void f(int);
void f(bool);
void f(void*);

f(0);            // calls f(int), not f(void*)
f(NULL);         // might not compile, but typically calls f(int).
				 // Never calls f(void*)
```

Avoid overloading function on pointer and integral types.

_nullptr_ is _std::nullptr_t_, defined to be the type of _nullptr_. _nullptr_ does not have integral type
    
#### Item 9: Prefer alias declarations to typedefs
    
```cpp
typedef
  std::unique_ptr<std::unordered_map<std::string, std::string>>  UPtrMapSS;

// Is equivalent to
using UPtrMapSS =
  std::unique_ptr<std::unordered_map<std::string, std::string>>;
```

Define type for function pointer

```cpp
// FP is a synonym for a pointer to a function taking an int and
// a const std::string& and returning nothing
typedef void (*FP)(int, const std::string&);      // typedef

// same meaning as above
using FP = void (*)(int, const std::string&);     // alias declaration
```

**Alias templates**

```cpp
template<typename T>
using MyAllocList = std::list<T, MyAlloc<T>>

// MyAlloc is a template type
```

#### Item 10: Prefer scoped enums to unscoped enums
    
```cpp
enum Color { black, white, red };

auto white = false; // error! white already declared in this scop
```

```cpp
enum class Color { black, white, red };

auto white = false;
Color c = white;            // Error! no enumerator named 'white'
Color c = Color::white;     // fine
auto c = Color::white;      // Also fine
```

The enumerators of a enum class is more strongly typed

```cpp
// Forward declaration
enum Color;        // Error!

enum class Color;  // fine
```

You can specify underlying type of scoped enums

```cpp
enum class Status;                // Underlying type is int
enum class Status: std::unit32_t; // Underlying type is std::unit32_t
```

Unscoped enum may also be declared with underlying type, and also may be forward-declared:

```cpp
enum Color: std::uint8_t;        // fwd decl for unscoped enum;
```

#### Item 11: Prefer deleted functions to private undefined ones
    
-   C++98 suppress special member functions bu declare them private.
-   C++11 use `= delete` mark copy constructor and copy assignment operators as deleted functions
-   Deleted function are by default public, C++ check for accessibility before deleted status, possibly leading to confusing compiler errors

```cpp
bool isLucky(int number);      // Original function
bool isLucky(char) = delete;   // reject chars
bool isLucky(bool) = delete;   // reject bools
bool isLucky(double) = delete; // reject doubles and floats
```

```cpp
class Widget {
public:
  ...
  template<typename T>
  void processPointer(T* ptr)
  { ... }
  ...
};

template<>
void Widget::processPointer<void>(void*) = delete;
```
    
#### Item 12: Declare overriding functions override

```cpp
class Derived: public Base {
public:
	virtual void mf1() override;
  virtual void mf2(unsigned int x) override;
  virtual void mf3() && override;
  virtual void mf4() const override;
};
```

#### Item 13: Prefer _const_iterators_ to _iterators_
    
Container member functions `cbegin()` and `cend()` produce const_iterators even for non-const containers.

#### Item 14: (Re-read) Declare functions _noexcept_ if they won't emit exceptions

C++11 the truly meaningful information about a function's exception-emitting behaviour was whether it had any.

```cpp
int f(int x) throw();   // no exception from f: C++98 style
int f(int x) noexcept;  // no exception from f: C++11 style
```

C++98, with exception specification violated, stack is unwound to `f`'s caller, and program execution is terminated.

C++11, at exception violation, the stack only possibly unwound before program execution.

In `noexception` function, optimizer do not need to keep the runtime stack in an unwind-able state.

#### Item 15: Use constexpr whenever possible

**constexpr** indicate a value that is known during compilation.

Constexpr functions does not produce results that are const.

The compilers will ensure Constexpr object have a compile time value, while const does not require object initialized with value known during compilation.

> Constexpr functions produce compile-time constants when they are called with compile-time constants.

-   Constexpr function have different restrictions on their implementation.
    
    **C++11:** Function contain no more than single executable statement
    
    **C++14:** Only returning literal types (All built-in types except _void_, or constexpr object)
    

> C++11, constexpr member functions are implicitly const. Second, they have void return types, and void isn’t a literal type in C++11. Both these restrictions are lifted in C++14.

#### Item 16: Make const member functions thread safe

_const_ member function does not have the same thread safe protection from non-const member function. Hence need it's own thread safe protection.

#### [[Effective_Modern_C__.pdf#page=127&selection=26,0,27,11|Item 17: Understand special member function generation]]

C++98 has 4 special member function, generated only when needed, by default public and **inline**, non-virtual.

-   Default constructor
-   destructor
-   Copy constructor
-   Copy assignment operator

C++11 introduce:

-   Move constructor
-   Move assignment operator

```cpp
class Widget {
public:
  ...
  Widget(Widget&& rhs);              // Move constructor
  Widget& operator=(Widget&& rhs);   // Move assignment operator
};
```

Types that aren't move-enabled will be 'moved' via their copy operations.

Member-wise move consists of move operations on data members and base classes that support move operations, but a copy operation for those that don't.

The 2 move operations are not independent, user declare either will prevent compiler generate the other one.

Mover operation is not generated by compiler is a copy operation is declared, and vice versa.

Move operation is only generated in class if following 3 things are true:
1.  No Copy operation declared in the class
2.  No move operation are declared in the class
3.  No destructor is declared in the class