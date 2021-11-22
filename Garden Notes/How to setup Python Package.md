- Setuptools no longer serve as default build tool. User provide a `pyproject.toml` to opt into use setuptools library.
- [PEP 517](https://www.python.org/dev/peps/pep-0517/) specify a new standard to package and distribute Python modules.
> a `pyproject.toml` file is used to specify what program to use for generating distribution.
>
> Then, two functions provided by the program, `build_wheel(directory: str)` and `build_sdist(directory: str)` create the distribution bundle at the specified `directory`. The program is free to use its own configuration script or extend the `.toml` file.
>
> Lastly, `pip install *.whl` or `pip install *.tar.gz` does the actual installation. If `*.whl` is available, `pip` will go ahead and copy the files into `site-packages` directory. If not, `pip` will look at `pyproject.toml` and decide what program to use to ‘build from source’ (the default is `setuptools`)

### Start with
```
~/meowpkg/
    pyproject.toml
    setup.cfg
    meowpkg/__init__.py
```

Dynamic setup.py
```
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
```