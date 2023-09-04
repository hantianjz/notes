---
publish: true
review-frequency: normal
---
2021-12-29-We
Type:: #idea
Tags:: [[Python]], [[Packaging]]

# How to setup Python Package

## Current state of Python packaging
- `sys.path` show list of possible directory package get imported from.
- 3rdparty packages get imported from `site-packages`
	- When a package is installed into `site-packages`, a meta-data folder, `{package}-{version}.dist-info`,is generated with the business logic source.
	- The distribution folder describes the package: Installer used to put it there; license of the package; files created as part of installation; top level python package; entry-point, etc..
- **Source** vs **Wheel** distribution, former compile package on end user, latter compile package by developer/distributor.
- **Source** package distribution require end user to have all the package build dependency available, I.E. specific `setuptools` version.
	- But benefit is: Support more OS platform, and easier to audit C-extension source

- Python build package *front end*: [[pip]] or [[potrey]]
- Python build package *backend end*: [[setuptools]] or [[flit]]

## [Package discovery and namespace package](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html)
Python Package: A folder with `__init__.py` file

Simple find all python package under `src` directory:
```
[options]
packages = find:
package_dir = src

[options.packages.find]
where = src
include = <wildcat  'prefix*'>
exclude = <wildcat exclude package>
```

## [Entry Points](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) 
While it is possible to setup package themselves to be executable via runpy module. (I.E. `python -m runable_module`) A console script entry point will allow more user friendly naming, and setup entry script outside of runpy.

For `setup.cfg`
```
[options.entry_points]
console_scripts =
    hello-world = timmins:hello_world
```
And syntax of entry pint line is:
```
<name> = [<package>.[<subpackage>.]]<module>[:<object>.<object>]
```
There is also option of `gui_scripts` vs `console_scripts` for running program outside of terminal window.

In general `entry_points` is a way for package to advertise its capabilities. There can be arbitrary fields in addition to `console_scripts` or `gui_scripts` for `options.entry_points`.

The `entry_points` can be solicited by the [importlib.metadata](https://docs.python.org/3/library/importlib.metadata.html)
```
from importlib import metadata
eps = metadata.entry_points()['console_scripts']
```

Entry points can have dependencies, like 
```
[options.entry_points]
console_scripts =
    hello-world = timmins:hello_world [pretty-printer]
```
Where the `hello_world` depend on `pretty-printer` extra

## [Dependencies Management in Setuptools](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#dependencies-management-in-setuptools)
*setuptools* provide following dependency styles:
1. Build system requirement
2. Required dependency
3. optional dependency

In `pyproject.toml` file specify packages needed to actually perform the package/build:
```
[build-system]
requires = ["setuptools", "wheel"]
```

To declare required dependency in `setup.cfg`:
```
[options]
install_requires =
	docutils
	BazSpam == 1.1
	enum34;python_verison<'3.4'
	pywin32 >= 1.0;platform_system=='windows'
```

To specify dependencies **NOT** in PyPI, can still be downloaded if they are:
- an egg, in standard distutils `sdist` format
- a single `.py` file
- a VCS repository (SVN, Hg, Git)

Add dependency_links into `setup.cfg`
```
[options]
dependency_links = 
	http://peak.telecommunity.com/snapshots/,
	vcs+proto://host/path@revision#egg=project-version
```

**Optional dependencies**
Define an arbitrary identifier, *PDF*, for the optional dependencies in `setup.cfg` for a `Package-A`
```
[metadata]
name = Package-A

[options.extras_require]
PDF = ReportLab>=1.2; RXP
```

If another `Project-A` that depend on `Package-A` like to use the *PDF* features it can in it's `setup.cfg` for `entry_points` dependency or required dependencies.
```
[metadata]
name = Project A
#...

[options]
#...
entry_points=
    [console_scripts]
    rst2pdf = project_a.tools.pdfgen [PDF]
    rst2html = project_a.tools.htmlgen
	
[options]
#...
install_requires =
    Project-A[PDF]
```

### Python requirement
In `setup.cfg` specify minimal version of python required
```
[options]
python_requires = >=3.6
```


## [Data File Support](https://setuptools.pypa.io/en/latest/userguide/datafiles.html)

#### `include_package_data`
Accept all data files and directories matched by `MANIFEST.in`.

#### `package_data`
Specify additional patterns to match files that may or may not be matched by `MANIFEST.in` or found in source control.

#### `exclude_package_data`
Specify patterns for data files and directories that should _not_ be included when a package is installed, even if they would otherwise have been included due to the use of the preceding options.	

### Accessing data files at runtime
Accessing data files directly using `__file__` can be unreliable.
Best to use the [ResourceManager API](https://setuptools.pypa.io/en/latest/pkg_resources.html#resourcemanager-api) `pkg_resources`

## [Development Mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html)
[[Notes todo]]

---
- Setuptools no longer serve as default build tool. User provide a `pyproject.toml` to opt into use setuptools library.
- [PEP 517](https://www.python.org/dev/peps/pep-0517/) specify a new standard to package and distribute Python modules.
> a `pyproject.toml` file is used to specify what program to use for generating distribution.
>
> Then, two functions provided by the program, `build_wheel(directory: str)` and `build_sdist(directory: str)` create the distribution bundle at the specified `directory`. The program is free to use its own configuration script or extend the `.toml` file.
>
> Lastly, `pip install *.whl` or `pip install *.tar.gz` does the actual installation. If `*.whl` is available, `pip` will go ahead and copy the files into `site-packages` directory. If not, `pip` will look at `pyproject.toml` and decide what program to use to ‘build from source’ (the default is `setuptools`)

---
# References
- Current state of python package: https://bernat.tech/posts/pep-517-and-python-packaging/
- Pep517 Pep518 for dummy: https://bernat.tech/posts/pep-517-518/
- Offical setuptools manual:  https://setuptools.pypa.io/en/latest/index.html
