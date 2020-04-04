.PHONY: init-repo clean-build build

init-repo: 
	python .make/set_name.py $(name)

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