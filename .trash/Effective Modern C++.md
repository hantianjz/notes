-   **lvalues vs rvalues**
    
    > A useful heuristic to determine whether an expression is an lvalue is to ask if you can take its address. If you can, it typically is. If you can’t, it’s usually an rvalue.
    
    > Copies of rvalues are generally move constructed, while copies of lvalues are usually copy constructed.
    

### Intro

-   **Item 1: Understand template type deduction**
    
    ```cpp
    template<typename T>
    void f(ParamType param);
    
    f(expr);
    ```
    
    ParamType and T are often not the same due to adornments in ParamType. I.E. Const or reference qualifier.
    
    Type of T does not always deduce to the same type as expr. There are 3 cases.
    
    -   **Case 1: ParamType is pointer or reference type but not universal reference**
        
        ```cpp
        template<typename T>
        void f(T& param);       // param is a reference
        
        int x = 27;             // x is an int
        const int cx = x;       // cx is a const int
        const int& rx = x;      // rx is a reference to x as a const int
        
        f(x);                   // T is int, param's type is int&
        
        f(cx);                  // T is const int, param's type is const int&
        
        f(rx);                  // T is const int, param's type is const int&
        ```
        
        ```cpp
        template<typename T>
        void f(const T& param); // param is now a ref-to-const
        
        int x = 27;             // x is an int
        const int cx = x;       // cx is a const int
        const int& rx = x;      // rx is a reference to x as a const int
        
        f(x);                   // T is int, param's type is const int&
        
        f(cx);                  // T is int, param's type is const int&
        
        f(rx);                  // T is int, param's type is const int&
        ```
        
        ```cpp
        template<typename T>
        void f(T* param);       // param is now a pointer
        
        int x = 27;             // x is an int
        const int *px = &x;     // px is a ptr to x as a const int
        
        f(&x);                  // T is int, param's type is int*
        
        f(cx);                  // T is const int, param's type is const int*
        ```
        
    -   **Case 2: ParamType is a universal reference**
        
        ```cpp
        template<typename T>
        void f(T&& param);       // param is now a universal reference
        
        int x = 27;              // as before
        const int cx = x;        // as before
        const int& rx = x;       // as before
        
        f(x);                    // x is lvalue, so T is int&,
        												 // param's type is also int&
        
        f(cx);                   // cx is lvalue, so T is const int&,
        												 // param's type is also const int&
        
        f(rx);                   // rx is lvalue, so T is const int&,
        												 // param's type is also const int&
        
        f(27);                   // 27 is rvalue, so T is int,
        												 // param's type is therefore int&&
        ```
        
    -   **Case 3: ParamType is neither pointer nor reference**
        
        ```cpp
        template<typename T>
        void f(T param);         // param is now passed by value
        
        int x = 27;              // as before
        const int cx = x;        // as before
        const int& rx = x;       // as before
        
        f(x);                    // T's and param's types are both int
        f(cx);                   // T's and param's types are again both int
        f(rx);                   // T's and param's types are still both int
        ```
        
    -   **Array Arguments**
        
        ```cpp
        const char name[] = "J. P."
        const char* ptrToName = name;
        
        // Const char[4] != const char*, but compile due to array-to-pointer decay rule
        ```
        
        ```cpp
        void myFunc(int param[]);
        // is the equivalent to
        void myFunc(int *param);
        ```
        
        _Although functions can’t declare parameters that aretruly arrays, they can declare parameters that are **references to arrays!**_
        
        ```cpp
        template<typename T>
        void f(T& param);         // template with by-reference parameter
        
        const char name[] = "1234";
        
        f(name)                   // pass array to f, as reference to array
        													// size of array is included in the type
        
        // T => const char[4], and param => const char (&)[4]
        ```
        
    -   **Function Arguments**
        
        ```cpp
        void someFunc(int, double);   // someFunc is a function;
        															// type is void(int, double)
        
        template<typename T>
        void f1(T param);             // in f1, param passed by value
        
        template<typename T>
        void f2(T& param);            // in f2, param passed by ref
        
        f1(someFunc);                 // param deduced as ptr-to-func;
        															// type is void (*)(int, double)
        
        f2(someFunc);                 // param deduced as ref-to-func;
        															// type is void (&)(int, double)
        ```
        
        _This rarely makes any difference in practice._
        
-   **Item 2: Understand _auto_ type deduction**
    
    **_Auto_** type deduction _is_ template type deduction. With one exception.
    
    Also divided into 3 cases based on type specifier on **auto**
    
    ### **Case 1: The type specifier is a pointer or reference, but no take universal reference.**
    
    ### **Case 3: The type specifier is neither a pointer nor a reference.**
    
    ```cpp
    auto x = 27;          // case 3 (x is neither ptr nor reference)
    const auto cx = x;    // case 3 (cx isn't either)
    const auto& rx = x;   // case 1 (rx is a non-universal ref.)
    ```
    
    ### **Case 2: The type specifier is a universal reference.**
    
    ```cpp
    auto&& uref1 = x;     // x is int and lvalue,
    											// so uref1's type is int&
    auto&& uref2 = cx;    // cx is const int and lvalue,
    											// so uref2's type is const int&
    auto&& uref3 = 27;    // 27 is int and rvalue,
    											// so uref3's type is int&&
    ```
    
    ### **Except**
    
    ```cpp
    // C++98 gives you two syntactic choices:
    int x1 = 27;
    int x2(27);
    
    // C++11, through its support for uniform initialization, adds these:
    int x3 = { 27 };
    int x4{ 27 };
    
    //All an int with value 27.
    ```
    
    ```cpp
    // int with value 27
    auto x1 = 27;
    auto x2(27);
    
    // type is std::initializer_list<int>, value is <27>
    auto x3 = {27};
    auto x4{27};
    
    auto x5 = { 1, 2, 3.0 };  // error! can't deduce T for
    													// std::initializer_list<T>
    ```
    
    When the initializer for anauto-declared variable is enclosed in braces, the deduced type is a _std::initializer_list_.
    
    **_Auto_** assumes a braced initializer represents **_std::initializer_list_**
    
    ### **[[C++14]] auto as function's return type**
    
    Uses template type deduction not auto type deduction.
    
-   **Item 3: Understand _decltype_**
    
    Tells you the name's or expression's type.
    
    ```cpp
    const int i = 0;            // decltype(i) is *const int*
    
    bool f(const Widget& w);    // decltype(w) is const widget&
    														// decltype(f) is bool(const Widget&)
    
    struct Point {
    	int x, y;
    };                          // decltype(Point::x) is int
    														// decltype(point::y) is int
    
    Widget w;                   // decltype(w) is *Widget*
    
    if (f(w)) ...               // decltype(f(w)) is bool
    
    template<typename T>       // simplified version of std::vector
    class vector {
    public:;
      ...
      T& operator[](std::size_t index);
      ...
    };
    
    vector<int> v;             // decltype(v) is vector<int>
    ...
    if (v[0] == 0) ...           // decltype(v[0]) is int&
    ```
    
    ```cpp
    template<typename Container, typename Index>    // works, but
    auto authAndAccess(Container& c, Index i)       // requires
     -> decltype(c[i])                              // refinement
    {
      authenticateUser();
      return c[i];
    }
    ```
    
    **_auto_** used for trialing return type using parameters to define the return type.
    
    [[C++11]], permit deduced return type for single statement lambdas
    
    [[C++14]] allow deduced return type for lambdas and functions.
    
    ```cpp
    Widget w;
    
    const Widget& cw = w;
    
    auto myWidget1 = cw;          // auto type deduction:
    															// myWidget1's type is Widget
    
    decltype(auto) myWidget2 = cw;// decltype type deduction:
    															// myWidget2's type is
    															//   const Widget&
    ```
    
    **[[C++11]]**
    
    ```cpp
    template<typename Container, typename Index>       // final
    auto                                               // C++11
    authAndAccess(Container&& c, Index i)              // version
    -> decltype(std::forward<Container>(c)[i])
    {
      authenticateUser();
      return std::forward<Container>(c)[i];
    }
    ```
    
    **C++14**
    
    ```cpp
    template<typename Container, typename Index>       // final
    auto                                               // C++14
    authAndAccess(Container&& c, Index i)              // version
    {
      authenticateUser();
      return std::forward<Container>(c)[i];
    }
    ```
    
    ```cpp
    decltype(auto) f1()
    {
      int x = 0;
      ...
      return x;        // decltype(x) is int, so f1 returns int
    }
    
    decltype(auto) f2()
    {
      int x = 0;
      ...
      return (x);      // decltype((x)) is int&, so f2 returns int&
    }
    ```
    
-   **Item 4: Know how to view deduced types**
    
    Trigger compile error message for deduced type with
    
    ```cpp
    template<typename T>       // declaration only for TD;
    class TD;                  // TD == "Type Displayer"
    
    TD<decltype(x)> xType;     // elicit errors containing
    TD<decltype(y)> yType;     // x's and y's types
    ```
    
    returns following error message output
    
    ```bash
    error: aggregate 'TD<int> xType' has incomplete type and    cannot be defined
    error: aggregate 'TD<const int *> yType' has incomplete type    and cannot be defined
    ```
    
    To print the type in runtime
    
    ```cpp
    std::cout << typeid(x).name() << '\\n';    // display types for
    std::cout << typeid(y).name() << '\\n';    // x and y
    ```
    
    ```cpp
    #include <boost/type_index.hpp>
    
    template<typename T>
    void f(const T& param)
    {
      using std::cout;
      using boost::typeindex::type_id_with_cvr;
    
      // show T
      cout << "T =     "
           << type_id_with_cvr<T>().pretty_name()
           << '\\n';
    
      // show param's type
      cout << "param = "
    			 << type_id_with_cvr<decltype(param)>().pretty_name()
           << '\\n';
      ...
    }
    ```
    

### Auto

-   **Item 5: Prefer auto to explicit type declarations**
    
    auto can be used to store function pointer or any callable object, and because it is a compile time operation it can be more efficient than using std::function() which may use heap memory.
    
-   **Item 6: User the explicitly typed initializer idiom when _auto_ deduces undesired types**
    
    C++ forbids references to bits.
    
    operator[] of _std::vector<bool>_ returns **std::vector<bool>::reference** that emulate the behaviour of **bool&**
    
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
    

### Moving to Modern C++

-   **Item 7: Distinguish between () and {} when creating objects**
    
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
    
-   **Item 8: Prefer _nullptr_ to 0 and NULL**
    
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
    
-   **Item 9: Prefer alias declarations to typedefs**
    
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
    
-   **Item 10: Prefer scoped enums to unscoped enums**
    
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
    
-   **Item 11: Prefer deleted functions to private undefined ones**
    
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
    
-   **Item 12: Declare overriding functions override**
    
    ```cpp
    class Derived: public Base {
    public:
    	virtual void mf1() override;
      virtual void mf2(unsigned int x) override;
      virtual void mf3() && override;
      virtual void mf4() const override;
    };
    ```
    
-   **Item 13: Prefer _const_iterators_ to _iterators_**
    
    Container member functions `cbegin()` and `cend()` produce const_iterators even for non-const containers.
    
-   **Item 14: (Re-read) Declare functions _noexcept_ if they won't emit exceptions**
    
    C++11 the truly meaningful information about a function's exception-emitting behaviour was whether it had any.
    
    ```cpp
    int f(int x) throw();   // no exception from f: C++98 style
    int f(int x) noexcept;  // no exception from f: C++11 style
    ```
    
    C++98, with exception specification violated, stack is unwound to `f`'s caller, and program execution is terminated.
    
    C++11, at exception violation, the stack only possibly unwound before program execution.
    
    In `noexception` function, optimizer do not need to keep the runtime stack in an unwind-able state.
    
-   **Item 15: Use constexpr whenever possible**
    
    **constexpr** indicate a value that is known during compilation.
    
    Constexpr functions does not produce results that are const.
    
    The compilers will ensure Constexpr object have a compile time value, while const does not require object initialized with value known during compilation.
    
    > Constexpr functions produce compile-time constants when they are called with compile-time constants.
    
    -   Constexpr function have different restrictions on their implementation.
        
        **C++11:** Function contain no more than single executable statement
        
        **C++14:** Only returning literal types (All built-in types except _void_, or constexpr object)
        
    
    > C++11, constexpr member functions are implicitly const. Second, they have void return types, and void isn’t a literal type in C++11. Both these restrictions are lifted in C++14.
    
-   **Item 16: Make const member functions thread safe**
    
    _const_ member function does not have the same thread safe protection from non-const member function. Hence need it's own thread safe protection.
    
-   **Item 17: Understand special member function generation**
    
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
    
    Memberwise move consists of move operations on data members and base classes that support move operations, but a copy operation for those that don't.
    
    The 2 move operations are not independent, user declare either will prevent compiler generate the other one.
    
    Mover operation is not generated by compiler is a copy operation is declared, and vice versa.
    
    Move operation is only generated in class if following 3 things are true:
    
    1.  No Copy operation declared in the class
    2.  No move operation are declared in the class
    3.  No destructor is declared in the class

## Smart Pointers

-   **Item 18: Use std::unique_ptr for exclusive-ownership resource management**