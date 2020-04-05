git clone <repo-name>
cd <repo-name>

For locally running the project python-natively without docker, you obviously need to have your project dependencies installed. As usual, it makes sense to use a virtual python environment. E. g. you could run: 
`pipenv shell --python 3.8`

Note however, that this is not required for the build steps in the `Makefile`. All necessary `pipenv` commands are defined there. 

In order to use this project, it is required to have
- Docker
- pipenv installed.

Furthermore, make sure that your default python installation has pip, setuptools (by default included in pyenv 3.8.2) and wheels (not by default included in pyenv 3.8.2; if you are using pyenv, simply run `pip install --upgrade pip && pip install --upgrade setuptools && pip install wheel`).
