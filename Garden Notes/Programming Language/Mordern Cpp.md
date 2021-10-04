# Feature to avoid: C++14(C++11)

#cpp #cpp14 #cpp17

-   Strongly avoid use of **std::initializer_list** in class constructor. [Ref](https://www.notion.so/Effective-Modern-C-a6f65e1619b445bfa80ed1d6614740fa)
    
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