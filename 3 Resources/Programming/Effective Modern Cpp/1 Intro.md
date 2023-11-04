---
publish: true
review-frequency: normal
link:
- '[[Cpp]]'
- '[[Cpp11]]'
- '[[Cpp14]]'
- '[[Cpp17]]'
- '[[template]]'
tags:
- notes
---
2021-12-29-We

## Effective Cpp Intro

#### Item 1: Understand template type deduction
```cpp
template<typename T>
void f(ParamType param);

f(expr);
```
    
ParamType and T are often not the same due to adornments in ParamType. I.E. Const or reference qualifier.

Type of T does not always deduce to the same type as expr. There are 3 cases.

- **Case 1: ParamType is pointer or reference type but not universal reference**

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

- **Case 2: ParamType is a universal reference**
        
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
        
- **Case 3: ParamType is neither pointer nor reference**
        
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
        
- **Array Arguments**
        
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
 
- **Function Arguments**
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

#### Item 2: Understand _auto_ type deduction
    
**_Auto_** type deduction _is_ template type deduction. With one exception.
Also divided into 3 cases based on type specifier on **auto**
    
- **Case 1: The type specifier is a pointer or reference, but no take universal reference.**
    
- **Case 3: The type specifier is neither a pointer nor a reference.**
    
  ```cpp
  auto x = 27;          // case 3 (x is neither ptr nor reference)
  const auto cx = x;    // case 3 (cx isn't either)
  const auto& rx = x;   // case 1 (rx is a non-universal ref.)
  ```
    
- **Case 2: The type specifier is a universal reference.**
    
  ```cpp
  auto&& uref1 = x;     // x is int and lvalue,
  											// so uref1's type is int&
  auto&& uref2 = cx;    // cx is const int and lvalue,
  											// so uref2's type is const int&
  auto&& uref3 = 27;    // 27 is int and rvalue,
  											// so uref3's type is int&&
  ```
    
- **Except**
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
  							//std::initializer_list<T>
  ```
    
    When the initializer for anauto-declared variable is enclosed in braces, the deduced type is a _std::initializer_list_.
    
    **_Auto_** assumes a braced initializer represents **_std::initializer_list_**
    
    ### **C++14 auto as function's return type**
    
    Uses template type deduction not auto type deduction.
#### Item 3: Understand _decltype_
    
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
    
  C++11, permit deduced return type for single statement lambdas
    
  C++14 allow deduced return type for lambdas and functions.
    
  ```cpp
  Widget w;
  
  const Widget& cw = w;
  
  auto myWidget1 = cw;          // auto type deduction:
  								// myWidget1's type is Widget
  
  decltype(auto) myWidget2 = cw;// decltype type deduction:
  								// myWidget2's type is
  								//   const Widget&
  ```
    
  **C++11**
    
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
    
####   Item 4: Know how to view deduced types
    
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
 
