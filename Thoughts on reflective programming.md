---
publish: true
review-frequency: normal
link:
- '[[programming]]'
- '[[java]]'
tags:
- idea
---
2022-09-29-Th

# Thoughts on reflective programming

Code reflection is the ability for program to examine introspect and modify its own structure or behaviour.

For example looking at the type of an object using `instanceof()` is introspection.
In addition, for an assembly program the program is inherently reflective since the assembly program and examine it's own assembly code as data, and modify those same assembly code.

As higher level programming language become used, many languages just don't provide a way to do reflection.

Reflection is not something supported by C++. But seem to be more popularly used in Java.

Reflection is mainly useful when interacting with code that is not controllable by the user, like a framework that has to interoperate with user defined classes. Classic example is the JUnit framework for writing java unit tests, that enumerate over all test functions.

With python it sort have also have reflection with `hasattr()` or `setattr()` that allows class to be introspected and modified. But this really blurs the line a lot since it is main part of the language.

Common advice seem to be that, don't use reflection unless you really need to like interfacing with code or library in java that you don't control. Since it is so power that it can be taken too far and break API boundary, and ignore explicit encapsulation. It's like directly reaching past the API interface and into internals of a class, which is always a dangerous thing to do.

---
# References
- https://stackoverflow.com/a/37632
- https://en.wikipedia.org/wiki/Reflective_programming
- https://softwareengineering.stackexchange.com/questions/123956/why-should-i-use-reflection