# Getting Started
**Prerequistes**

_pytemplate_ relies on 
- git
- pipenv
- Docker

Furthermore, make sure that your default python installation has installed
- pip
- setuptools (by default included in pyenv 3.8.2)
- wheels (not by default included in pyenv 3.8.2).

**Get the a base python package running in a Docker container in less than a minute.**
```sh
curl https://raw.githubusercontent.com/MohamedKari/pytemplate/master/init-pytemplate.sh -o init-pytemplate.sh
sh init-pytemplate.sh <desired-repo-name>
cd <desired-repo-name>
# install dev and prod dependencies with pipenv
make install-all-deps
# either run python-natively ...
python -m <desired-repo-name>
# ... or build and run docker-container
make docker-run
# assuming you have VS Code installed:
code . 
```
![usage_sample.gif](https://raw.githubusercontent.com/MohamedKari/pytemplate/assets/.readme/usage_sample.gif)

# Dependency and Build Management

- Maintain your prod dependencies in the _setup.py_.
- Maintain your dev dependencies (e.g. _pylint_) in the _setup.py_.

`make install-all-deps` will install prod and dev dependencies in the virtual env. This is required

`make docker-build` will 
- install prod dependencies using pipenv,
- derive a requirements.txt from the lock file,  
- copy this requirements.txt into the image,
- install the dependecies in the image using pip. 
- build a wheel from the setup.py,
- copy and install the wheel in the image.

We explicitly create and install from requirements.txt, to exploit Docker caching: If the requirements didn't change, the cached layer with the requirements installed can be reused. Would we only copy and `pip install` the wheel, there would be no layer with the requirements installed in the cache. Each change to the package code would therefore require installing requirements from scratch. 
