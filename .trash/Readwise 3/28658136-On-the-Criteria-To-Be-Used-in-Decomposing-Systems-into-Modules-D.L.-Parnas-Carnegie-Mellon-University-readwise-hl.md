---
tags: #readwise-articles
aliases: On the Criteria To Be Used in Decomposing Systems into Modules D.L. Parnas Carnegie-Mellon University
author: mit.edu
link: [[programming]]
---
# On the Criteria To Be Used in Decomposing Systems into Modules D.L. Parnas Carnegie-Mellon University

## Summary
This paper discusses modularization as a mechanism for improving the flexibility and comprehensibility of a system while allowing the shortening of its development time.
http://sunnyday.mit.edu/16.355/parnas-criteria.html
1972-12-12

- A well-defined segmentation of the project effort ensures system modularity. Each task forms a separate, distinct program module. At implementation time each module and its inputs and outputs are well-defined, there is no confusion in the intended interface with other system modules. At checkout time the integrity of the module is tested independently; there are few scheduling problems in synchronizing the completion of several tasks before checkout can begin. Finally, the system is maintained in modular fashion, system errors and deficiencies can be traced to specific system modules, thus limiting the scope of detailed error searching. ([View Highlight](https://read.readwise.io/read/01h27ctdskcqtfrqyp7bb4q09h))
- The benefits expected of modular programming are: (1) managerial_development time should be shortened because separate groups would work on each module with little need for communication: (2) product flexibility_it should be possible to make drastic changes to one module without a need to change others; (3) comprehensibility_it should be possible to study the system one module at a time. The whole system can therefore be better designed because it is better understood ([View Highlight](https://read.readwise.io/read/01h27dahk4jw2z40thh3pafqm5))
- We have tried to demonstrate by these examples that it is almost always incorrect to begin the decomposition of a system into modules on the basis of a flowchart. We propose instead that one begins with a list of difficult design decisions or design decisions which are likely to change. Each module is then designed to hide such a decision from the others. Since, in most cases, design decisions transcend time of execution, modules will not correspond to steps in the processing. To achieve an efficient implementation we must abandon the assumption that a module is one or more subroutines, and instead allow subroutines and programs to be assembled collections of code from various modules. ([View Highlight](https://read.readwise.io/read/01h27e4y3jmm7rkkn19tfzcqp2))
