---
publish: true
review-frequency: normal
tags:
- idea
---
2021-12-29-We
[[cpp]], [[cpp14]], [[cpp17]]

# Feature to avoid in Mordern Cpp

-   Strongly avoid use of **std::initializer_list** in class constructor. [[ano|Ref]]
    
-   Only function prototype declaration in header files, no actual function definition. Function definition only allowed in, .cc .cpp, source files.
    
-   Member function reference qualifiers
    
    ```cpp
    class Widget {
    public:
    	...
    	void doWork() &;     // Applied when *this is a lvalue
      void doWork() &&;    // Applied when *this is a rvalue
    };
    ...
    Widget makeWidget();   // Factory function (returns rvalue)
    Widget w;              // Normal object (an lvalue)
    ...
    w.doWork();            // calls Widget::doWork()& for lvalues
    makeWidget().doWork(); // calls Widget::doWork()&& for rvalues
    ```  