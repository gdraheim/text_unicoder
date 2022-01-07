F= unicoder.py
D=$(basename $F)
B= 2021
FOR=today

FILES = *.py *.cfg
PYTHON3 = python3

default: help

version1:
	@ grep -l __version__ $(FILES) | { while read f; do echo $$f; done; } 

version:
	@ grep -l __version__ $(FILES) | { while read f; do : \
	; Y=`date +%Y -d "$(FOR)"` ; X=$$(expr $$Y - $B); D=`date +%W%u -d "$(FOR)"` ; sed -i \
	-e "/^version /s/[.]-*[0123456789][0123456789][0123456789]*/.$$X$$D/" \
	-e "/^ *__version__/s/[.]-*[0123456789][0123456789][0123456789]*\"/.$$X$$D\"/" \
	-e "/^ *__version__/s/[.]\\([0123456789]\\)\"/.\\1.$$X$$D\"/" \
	-e "/^ *__copyright__/s/(C) [0123456789]*-[0123456789]*/(C) $B-$$Y/" \
	-e "/^ *__copyright__/s/(C) [0123456789]* /(C) $$Y /" \
	$$f; done; }
	@ grep ^__version__ $(FILES)

help:
	$(PYTHON3) unicoder.py --help

check:
	$(PYTHON3) unicoder.py.tests.py -vvv

clean:
	- rm *.pyc 
	- rm -rf *.tmp
	- rm setup.py

sdist bdist bdist_wheel:
	- rm -rf dist build unicoder.egg-info
	{ echo '#!/usr/bin/env python' \
	; echo 'from setuptools import setup' \
	; echo 'setup()' ; } > setup.py
	$(PYTHON3) setup.py $@
	rm setup.py

.PHONY: build
build:
	rm -rf build dist *.egg-info
	echo "import setuptools ; setuptools.setup()" > setup.py
	# pip install --root=~/local . -v
	python3 setup.py sdist
	rm setup.py
	twine check dist/*
	: twine upload dist/*

# ------------------------------------------------------------

mypy:
	zypper install -y mypy
	zypper install -y python3-click python3-pathspec

MYPY = mypy
MYPY_STRICT = --strict --show-error-codes --show-error-context --no-warn-unused-ignores

type: type.r
    :
type.r:
	$(MYPY) $(MYPY_STRICT) unicoder.py
	- rm -rf .mypy_cache

AUTOPEP8=autopep8
pep style: 
	$(MAKE) pep.r
pep.r style.r:
	$(AUTOPEP8) unicoder.py --in-place
	git --no-pager diff unicoder.py
