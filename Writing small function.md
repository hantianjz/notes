---
publish: true
review-frequency: normal
---
2022-01-30-Su
Type:: #idea
Tags:: [[tacit knowledge]], [[advice]], [[best practice]], [[C]], [[Cpp]], [[John Carmack]]

# Writing small function
> [!quote] 
> If a function is only called from a single place, consider inlining it.
> 
> If a function is called from multiple places, see if it is possible to arrange for the work to be done in a single place, perhaps with flags, and inline that.
> 
> If there are multiple versions of a function, consider making a single function with more, possibly defaulted, parameters.
> 
> If the work is close to purely functional, with few references to global state, try to make it completely functional.
> 
> Try to use const on both parameters and functions when the function really must be used in multiple places.
> 
> Minimize control flow complexity and "area under ifs", favoring consistent execution paths and times over "optimally" avoiding unnecessary work.

---
# References
- https://www.scattered-thoughts.net/writing/on-bad-advice/#what-lasts
- http://number-none.com/blow/john_carmack_on_inlined_code.html
