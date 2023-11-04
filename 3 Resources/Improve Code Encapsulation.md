---
publish: true
review-frequency: normal
link:
- '[[cpp]]'
- '[[programming]]'
- '[[encapsulation]]'
tags:
- notes
---
2022-10-24-Mo

# Improve Code Encapsulation

**If a function can be implemented as non-friend non-member function, it should be the preferred option.**

Encapsulation is a *means*, not a end. It is a mean to yield **flexibility** and **robustness**.

Unencapsulated software is inflexible and hence not robust.

A way to evaluate relative encapsulation of two implementations: if changing one implementation might lead to more broken code than changing of another implementation, the latter is *more* encapsulated than the former.

And a more encapsulated code is easier to change, given it create less broken code.

A data struct of
```
struct Point {
    int x, y;
}
```

vs a Class of
```
class Point {
public:
    int getX() const;
    int getY() const;
    void setX(int x);
    void setY(int y);
}
```

It is very difficult to track the number of function that uses `struct Point` directly, hence using it would lead to a lot of potential code breakage. Where as a change to internal struct of `Class Point` would only effect the 4 member function that have access to it's private members.

This imply a higher number of member function means lower encapsulation.

Differentiate the actual member function vs the convenience function that doesn't really need to be one of the member or friend functions.

Adding functions beyond the minimum necessary, decreases the class's comprehensibility and maintainability, and increase compile time for user.

---
# Reference
- https://www.aristeia.com/Papers/CUJ_Feb_2000.pdf