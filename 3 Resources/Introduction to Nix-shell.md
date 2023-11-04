---
publish: true
review-frequency: normal
link:
- '[[nix]]'
- '[[build system]]'
- '[[Everything]]'
tags:
- notes
---
2022-07-04-Mo
Date published: 19 December 2021

# Introduction to Nix-shell
---

>[!nix-shell]
> The command `nix-shell` will build the dependencies of the specified derivation, but not the derivation itself. It will then start an interactive shell in which all environment variables defined by the derivation path have been set to their corresponding values, and the script `$stdenv/setup` has been sourced. This is useful for reproducing the environment of a derivation for development.

Every project have tool dependencies, for various language it use.

In addition multiple version of the same language/program to manage. (Python, JVM, Node, etc..)

Ad-hoc tools exist to manage individual language versions and dependencies, but can't do anything cross language. (Pyevn, rbenv, nvm)

Nix project aims to building a completely reproducible world.
- Nix: a package manager/ build system
- Nix: Also a programming language used to define corresponding build rules and packages
- NixOs: Linux-based operating system built around the nix package manager
- NixOps: bring the same level of reproducibility to infrastructure management
- nix-shell: ignore your Nix installation, and only add specific nix package to your `PATH`
---
# Reference
- https://cuddly-octo-palm-tree.com/posts/2021-12-19-tyska-nix-shell/