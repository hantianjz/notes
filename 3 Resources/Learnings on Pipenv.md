---
publish: true
review-frequency: normal
link:
  - "[[python]]"
  - "[[setuptools]]"
  - "[[pip]]"
  - "[[pipenv]]"
tags:
  - documentation
reviewed: 2023-09-03
---
## Pipenv lock sucks
It seems pipenv lock can't use existing package to resolve dependencies. This make local packages impossible to depend on each other. Pipenv can only resolve against a index that is online

Workaround manually edit Pipfile.lock for now