Last Updated: 2022-03-21
Type: #documentation 
Tags: [[Python]], [[setuptools]], [[pip]], [[pipenv]]

# Learnings on Pipenv

## Pipenv lock sucks
It seems pipenv lock can't use existing package to resolve dependencies. This make local packages impossible to depend on each other. Pipenv can only resolve against a index that is online

Workaround manually edit Pipfile.lock for now