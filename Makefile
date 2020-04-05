.PHONY: init-repo clean-build build

init-repo: 
	python .make/set_name.py $(shell basename $(realpath .))

clean: clean-build clean-pyc clean-pipenv

clean-pipenv:
	rm -rf Pipfile.lock
	rm -rf requirements.txt

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-build:
	rm -rf build/ dist/ *.egg-info *.egg

dist: clean-build
	python setup.py bdist_wheel
	rm -rf build/ *.egg-info *.egg

docker-build: clean-pipenv dist					# removing Pipfile.lock is highly import, otherwise new dependencies added to setup.py will get ignored.
	pipenv install -e .					 		# installs dependencies from setup.py
	pipenv lock -r > requirements.txt	 		# create requirements.txt with all dependencies
	sed -i '' '/-e/d' ./requirements.txt    	# drop the editable flag
	docker build -t pkg_name:latest .

docker-run: docker-build
	docker run -it pkg_name:latest

python-run:
	@echo "use 'python -m $(shell basename $(realpath .))' to be able to pass arguments or modify Makefile"
	python -m $(shell basename $(realpath .))