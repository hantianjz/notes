---
publish: true
review-frequency: normal
---
Last Updated: 2022-09-29
Type:: #documentation 
Tags:: [[Cpp]], [[Algorithm]]

# How does Cpp resolve a function call

Cpp compile time resolution path:
![[Cpp_function_resolve_path.png]]

## Name Lookup
- **Member name lookup**: any name that is to the right of `.` or `->` token, search member within a class members.
- **Qualified name lookup**: Like `std::sort` look up of function in specific namespace.
- **Unqualified name lookup**: Neither of above.

The compiler build a list of candidate functions for the name lookup.

##  Argument-dependent lookup
aka, ADL, or Koenig lookup. A set of rules for looking up for unqualified function names in function call expressions. I.E. implicit function calls to overloaded operators.

Argument-dependent lookup makes it possible to use operators defined in different namespace.

## Special Handling of Function Templates
One of the potential candidate from the name lookup is a function template. But a function template is not callable and needs to be turned into a function first.

Template argument deduction figure out the type of the template arguments.

If the template argument substitution succeeds, the template function is kept as function candidate.

## Overload Resolution
Figure out which of the candidate function is able to even handle the function call.
Check if arguments must be compatible. If the argument types don't match the function's parameter types exactly, it should at least be possible to implicitly convert.
Check if function's constraints are satisfied.

## Tiebreakers
1. First tiebreaker: Better-matching parameters  wins
    - Fewer implicit conversion the better.
2. Second tiebreaker: Non-template function wins
3. Third tiebreaker: More specialized template wins
```
template <typename T> void blast(T obj, float force);
template <typename T> void blast(T* obj, float force); // More specialized template
```
And [more](https://en.cppreference.com/w/cpp/language/overload_resolution#Best_viable_function)

## Conclusion
Let’s take a look back to see just how much detail was skipped. It’s actually kind of remarkable:
-   There’s an entire set of rules for [unqualified name lookup](https://en.cppreference.com/w/cpp/language/unqualified_lookup).
-   Within that, there’s a set of rules for [argument-dependent lookup](https://en.wikipedia.org/wiki/Argument-dependent_name_lookup).
-   [Member name lookup](https://eel.is/c++draft/class.member.lookup) has its own rules, too.
-   There’s a set of rules for [template argument deduction](https://en.cppreference.com/w/cpp/language/template_argument_deduction).
-   There’s an entire family of metaprogramming techniques based on [SFINAE](https://en.wikipedia.org/wiki/Substitution_failure_is_not_an_error).
-   There’s a set of rules governing how [implicit conversions](https://en.cppreference.com/w/cpp/language/implicit_conversion) work.
-   [Constraints](https://en.cppreference.com/w/cpp/language/constraints) (and concepts) are a completely new feature in C++20.
-   There’s a set of rules to determine [which implicit conversions are better than others](https://en.cppreference.com/w/cpp/language/overload_resolution#Ranking_of_implicit_conversion_sequences).
-   There’s a set of rules to determine [which function template is more specialized than another](https://en.cppreference.com/w/cpp/language/function_template#Function_template_overloading).

---
# References
- https://preshing.com/20210315/how-cpp-resolves-a-function-call/
- https://en.cppreference.com/w/cpp/language/adl