---
publish: false
review-frequency: normal
link:
  - "[[Home]]"
  - "[[code tagging]]"
  - "[[visualization]]"
  - "[[Notes todo]]"
tags:
  - idea
---
2021-12-29-We

# Code Graph

# Overview
This project is heavily inspired by the Obsidian [Graph view](https://help.obsidian.md/Plugins/Graph+view) tool. To visualize one's knowledge/notes. And I thought it be fun to do the same for source codes.

I personally have always tried to maintain a mental image of the source code of any project I have worked on. This is often useful for large to medium sized projects, and often the best way to become familiar with a new project. But it was always very time consuming and I have to go through a lot of source files and reading a lot of code to very slowly build a high level mental picture of the relationship or dependency between different parts of the source.

The code graph is an attempt at aiding tool to visualize overall dependency and relationships between different source files.

# Implementation details
There are plenty of [[Tools to investigate more]] currently exist for analyzing any code base. I wanted to start small, started with [[What and How is ctags|ctags]] first. So it turns out that [[What and How is ctags|ctags]] files only generate symbol definition/declarations not references. This is not as useful for code graph since it will still require me to go through the source file. So next natural candidate was [[what and how is gtags]] with is much more rich and very easy to parse.

With [[what and how is gtags]] providing a very detailed tag define and reference mapping it was trivial to build a network graph from that with [[Tools to investigate more#Pyvis https pyvis readthedocs io en latest index html|Pyvis]].

# Current status
### v0.0
**Feature**
- Each source file represent a single node
- Edges are connected by symbol references between each source files, and are weighted based on occurrences

**Bug**
- There is duplicate edges from the generated edge list

# Future TODO
- Single command line to generate graph
- Publish graph for different code base
- Identify + map detailed symbol references and type or kind
- Define node based on something other than source file
- To search/filter on:
	- prefix string?
	- Reference type
	- Reference to function call
	- Reference to variables
	- Reference to header file
- Tool bar to configure and change the physics
- More diverse color for edges
- Live update of graph
- How to make it extensible?
- Graph traversing almost like a function call
- Represent IPC somehow and define them

---
# References
- https://github.com/hantianjz/Code-Graph