# Getting Started
**Prerequistes**

_pytemplate_ relies on 
- git
- pipenv
- Docker

**Get the a base python package running in a Docker container in less than a minute.**
```sh
reponame="<desired-repo-name>"
git clone --depth=1 --branch=master https://github.com/MohamedKari/pytemplate.git $reponame
cd $reponame && rm -rf .git
make init-repo
# either run python-natively ...
python -m container_data_service
# ... or build and run docker-container
make docker-run
```

# Advanced information

For locally running the project python-natively without docker, you obviously need to have your project dependencies installed. As usual, it makes sense to use a virtual python environment. E. g. you could run: 
`pipenv shell --python 3.8`

Note however, that this is not required for the build steps in the `Makefile`. All necessary `pipenv` commands are defined there. 


Furthermore, make sure that your default python installation has pip, setuptools (by default included in pyenv 3.8.2) and wheels (not by default included in pyenv 3.8.2; if you are using pyenv, simply run `pip install --upgrade pip && pip install --upgrade setuptools && pip install wheel`).
