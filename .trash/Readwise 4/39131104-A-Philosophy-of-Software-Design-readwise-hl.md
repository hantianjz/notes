---
tags: #readwise-articles
aliases: A Philosophy of Software Design
author: John-Ousterhout
link:
 
    - "[[programming]]"
 
    - "[[software]]"
---
# A Philosophy of Software Design

https://readwise.io/reader/document_raw_content/156798363
2019-01-31
## Summary
The text discusses how reducing complexity in software design is crucial, emphasizing that simplicity is more important than length of code. It highlights the importance of clear and meaningful documentation in aiding developers to understand and modify code effectively. The goal is to make code obvious and understandable to reduce complexity and errors in software development.

- interfaces should be designed to make the common case as simple as possible ([View Highlight](https://read.readwise.io/read/01hztsanj2921vtfz29prfeaek))
- the effective complexity of that interface is just the complexity of the commonly used features. ([View Highlight](https://read.readwise.io/read/01hztsdgp325428rypzt1vznss))
- Information leakage occurs when the same knowledge is used in multiple places, such as two different classes that both understand the format of a particular type of file. ([View Highlight](https://read.readwise.io/read/01hzttjtyz6kty4e335a264wy9))
- When designing modules, focus on the knowledge that’s needed to perform each task, not the order in which tasks occur. ([View Highlight](https://read.readwise.io/read/01hzttqvdewaafz5tg2veegd1p))
- Whenever possible, classes should “do the right thing” without being explicitly asked. ([View Highlight](https://read.readwise.io/read/01hztvd5mhjagg4j932f7ht78c))
- Complexity is determined by the activities that are most common. ([View Highlight](https://read.readwise.io/read/01ht45mjpbj1kts38tw3xs0ee1))
- Isolating complexity in a place where it will never be seen is almost as good as eliminating the complexity entirely. ([View Highlight](https://read.readwise.io/read/01ht45nwcbe5rqyjbgd60yzh09))
- Sometimes an approach that requires more lines of code is actually simpler, because it reduces cognitive load. ([View Highlight](https://read.readwise.io/read/01ht45t6xn7jp7sj8f0zzysvkt))
- a dependency exists when a given piece of
  code cannot be understood and modified in isolation ([View Highlight](https://read.readwise.io/read/01hw90hdhde57gye9ahj3g7zme))
- The signature of a method creates a dependency between the implementation of that method and the code that invokes it ([View Highlight](https://read.readwise.io/read/01hw90n25zn9sm8g61np59csqb))
- The new Web site replaced a nonobvious and difficult-to-manage dependency with a simpler and more obvious one. ([View Highlight](https://read.readwise.io/read/01hw90ypv5h9ygh6znw381pj3v))
- However, obscurity is also a design issue. If a system has a clean and obvious design, then it will need less documentation. The need for extensive documentation is often a red flag that the design isn’t quite right. ([View Highlight](https://read.readwise.io/read/01hw918j1rst8xprjvd84c7yqc))
- If a system contains adjacent layers with similar abstractions, this is a red
  flag that suggests a problem with the class decomposition. ([View Highlight](https://read.readwise.io/read/01hzxan1sht9rycy93ct8capat))
