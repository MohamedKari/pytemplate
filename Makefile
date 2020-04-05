.PHONY: init-repo clean-build build

init-repo: 
	python .make/set_name.py $(shell basename $(realpath .))

clean: clean-build clean-pyc

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

docker-build: dist
	docker build -t pkg_name:latest .

docker-run: docker-build
	docker run -it pkg_name:latest

python-run:
	@echo "use 'python -m $(shell basename $(realpath .))' to be able to pass arguments or modify Makefile"
	python -m $(shell basename $(realpath .))