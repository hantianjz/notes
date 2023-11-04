---
publish: true
review-frequency: normal
link:
  - "[[Cpp]]"
  - "[[Notes todo]]"
  - "[[reading]]"
  - "[[programming]]"
  - "[[C]]"
tags:
  - notes
---
2022-05-07-Sa
# A tour of C++

> [!note]
> C++ is a statically typed language. That is, the type of every entity (e.g., object, value, name, and expression) must be known to the compiler at its point of use. The type of an object determines the set of operations applicable to it.

>[!note] 
> Main function. Not every operating system and execution environment make use of that return value: Linux/Unix-based environments do, but Windows based environments rarely do.

- Function declare is like prototype header `double square(double);`
- Function definition is `double square(double){ return ;}`

# 1.4.2 Initialization

```cpp
double d1 = 2.3;    // Init d1 to 2.3
double d2 {2.3};    // Init d1 to 2.3
double d3 = {2.3};   // Init d1 to 2.3 (where = is optional with {})
complex<double> z = 1; // A complex number with double percision floating-point scalars
complex<double> z2  {d1, d2}; 
complex<double> z3 = {d1, d2}; // where the = is optional

vector<int> v = {1,2,3,4,5,6}; // A vector of ints
```
The = form is traditional and dates back to C, but if in doubt, use the general {}-list form. If nothing else, it saves you from conversions that lose information:

```cpp
int i7 = 7.8;  // i7 becomes 7
int i2 {7.8};  // Compiler error: floating point to integer conversion
```

# 1.6 Constants

**const**: Calculated during run time but compiler try to enforce it to not be modified.

**constexpr**: Calculated during compile time.

To use a function in constexpr expression, function must also be defined as constexpr.

```
constexpr double square(double x) { return x*x; }
constexpr double max1=1.4*square(16);
```

A **constexpr** function can be used for non-constant arguments, but when that is done the result is not a constant expression. We allow a constexpr function to be called with non-constant-expression arguments in contexts that do not require constant expressions. That way, we don’t have to define essentially the same function twice: once for constant expressions and once for variables.

To be constexpr, a function must be rather simple and cannot have side effects and can only use information passed to it as arguments. In particular, it cannot modify non-local variables, but it can have loops and use its own local variables.

# 1.7.1  The Null Pointer
> [!warning]
> There is no "null reference." A reference must refer to a valid object.

# 1.8 Tests
An **if** statement can introduce a variable and test it, and the variable will exist within the scope of whole if block including the branches.
```cpp
void do_something(vector<int>& v)
{
    if (auto n = v.size(); n ==0) {
        // run here in n==0.
    } else if (n == 1) {
        // Still access n where if n==1
    } else {
        // Printf(n)
    }
    ...
}
```
This keep the scope of the variable limited to improve readability and minimize errors.

# 1.9.2
> [!warning]
> It is undefined behaviour to read and write from a uninitialized variable.

# 1.10 Advice
- Use digit separators to make large literals readable; §1.4; [CG: NL.11].
- 11.  Avoid ‘‘magic constants’’; use symbolic constants; §1.6; [CG: ES.45].

# 2.2 Structures
The **new** operator allocates memory from a area called the **free store** (AKA *dynamic memory* and *heap*).

# 2.3 Class
There is no fundamental difference between a struct and a class; a struct is simply a class with members public by default.

# 3.3 Modules (C++20)
```cpp
export module Vector; // Defining the module called "Vector"

...
```

The way we use this **module** is to *import* it where we need it.

```cpp
import Vector;
```

# 3.5.2 Invariants
RAII(**Resource Acquisition Is Initialization**) technique (4.2.2, 5.3)

# 3.5.3 Error-Handling Alternatives
One way to ensure termination is to add **noexcept** to a function so that a **throw** from anywhere in the function's implementation will turn into `terminate()`

# 3.5.5 Static Assertions
The **static_assert** mechanism can be used for anything that can be expressed in terms of constant expressions (1.6)

# 3.6.3 Structured Binding
```cpp
struct Entry {
    string name;
    int value;
};

Entry read_entry(istream& is)
{
    string s;
    int i;
    is >> s >> i;
    return {s,i};
}

auto e = read_entry(cin);

cout << "{ " << e.name << " , " << e.value << " }\n";
```

Unpacking entry member into local variables.
```cpp
auto [n,v] = read_entry(is);
cout << "{ " << n << " , " << v << " }\n";
```
The auto `[n,v]` declares two local variables n and v with their types deduced from read_entry()’s return type.

# 3.7 Advice
- Distinguish between declarations (used as interfaces) and definitions (used as implementations); §3.1.
- Prefer pass-by-const-reference over plain pass-by-reference; §3.6.1;

# 4 Clases
- Concrete classes
- Abstract classes
- Class hierarchies

# 4.2 Concrete Types
The basic idea of *concrete classes* is that they behave "just like built-in types."

The defining characteristic of a concrete type is that its representation is part of its definition.

Functions defined in a class are inlined by default.

User-defined operators (‘‘overloaded operators’’) should be used cautiously and conventionally. The syntax is fixed by the language, so you can’t define a unary /. Also, it is not possible to change the meaning of an operator for built-in types, so you can’t redefine + to subtract ints.

# 4.2.2 A Container
A *container* is an object holding a collection of elements. Vector is a container.

Avoiding naked **new** and naked **delete** makes code far less error-prone and far easier to keep free of resource leaks.

# 4.2.3 Initializing Containers
A **static_cast** does not check the value it is converting.
**reinterpret_cast** treat an object as simply a sequence of bytes
**const_cast** for casting away the **const**.

# 4.3 Abstract Types
The curious *=0* syntax says the function is pure virtual; that is, some class derived from **Container** must define the function.

A class with a pure virtual function is called an abstract class.

# 4.4 Virtual Functions
[virtual function table] or [vtbl] Each class with virtual functions has its own *vbtl* identifying its virtual functions.

![[cpp_containers_figure.png]]

Its space overhead is one pointer in each object of a class with virtual functions plus one vtble for each such class.

# 4.5.1 Benefits from Hierarchies
- *interface inheritance*: An object of a derived class can be used wherever an object of a base class is required. That is, the base class acts as an interface for the derived class. The Container and Shape classes are examples. Such classes are often abstract classes.
- *implementation inheritance*: A base class provides functions or data that simplifies the implementation of derived classes. Smiley’s uses of *Circle*’s constructor and of *Circle::draw()* are examples. Such base classes often have data members and constructors.

# 4.5.2 Hierarchy Navigation
Using **dynamic_cast** to access another derived class or parent class of the class hierarchy. **dynamic_cast** return **nullptr** is unexpected type is given.

**Dynamic_cast** throws a **bad_cast** exception when unacceptable type is given.

# 4.5.3 Avoiding Resource Leaks
Assigning the result of **new** to a "naked pointer" is asking for trouble.
One simple solution to such problems is to use a standard-library **unique_ptr** rather than a "naked pointer" when deletion is required. Where complier will generate required destructor for freeing the allocated unique_ptr.

# 5.1.1 Essential Operations
```cpp
class X {
public:
    X(Sometype);     // Ordinary constructor: create an object
    X();             // Default constructor
    X(const X&);     // Copy constructor
    X(X&&):          // Move constructor
    X& operator=(const X&); // Copy assignment: Clean up target and copy
    X& operator=(X&&); // Move assignment: clean up target and move
    ~X();            // Destructora
};
```

Five situation in which an object can be copied or moved:
- As the source of an assignment
- As an object initializer
- As a function argument
- As a function return value
- As an exception

> [!warning]
> When a class has a pointer member, it is usually a good idea to be explicit about copy and move operations.

`=default` Tells the complier to generate the default operation function
`=default` indicate to the compiler to NOT generate an operation.

# 5.1.2 Conversions
Constructor take a single argument defines a conversion from its argument type.
```cpp
class Vector {
public:
    explicit Vector(int s);
};
```

```cpp
Vector v1(7);   // Ok: V1 has 7 elements
Vector v2 = 7;  // Error: Implicit conversion from int to Vector
```

# 5.1.2 Copy and Move
The default copy of class is member-wise copy: copy each member.

# 5.5 Advice
- Define all essential operations or None
- By default, declare single-argument constructors explicit