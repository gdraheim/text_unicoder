#! /usr/bin/make -f

BASEYEAR= 2021
FOR=today

FILES = *.py *.cfg
PYTHON3 = python3
TWINE = twine

PARALLEL = -j2

default: help

version1:
	@ grep -l __version__ $(FILES) | { while read f; do echo $$f; done; } 

version:
	@ grep -l __version__ $(FILES) | { while read f; do : \
	; THISYEAR=`date +%Y -d "$(FOR)"` ; YEARS=$$(expr $$THISYEAR - $(BASEYEAR)) \
        ; WEEKnDAY=`date +%W%u -d "$(FOR)"` ; sed -i \
	-e "/^version /s/[.]-*[0123456789][0123456789][0123456789]*/.$$YEARS$$WEEKnDAY/" \
	-e "/^ *__version__/s/[.]-*[0123456789][0123456789][0123456789]*\"/.$$YEARS$$WEEKnDAY\"/" \
	-e "/^ *__version__/s/[.]\\([0123456789]\\)\"/.\\1.$$YEARS$$WEEKnDAY\"/" \
	-e "/^ *__copyright__/s/(C) [0123456789]*-[0123456789]*/(C) $(BASEYEAR)-$$THISYEAR/" \
	-e "/^ *__copyright__/s/(C) [0123456789]* /(C) $$THISYEAR /" \
	$$f; done; }
	@ grep ^__version__ $(FILES)

help:
	$(PYTHON3) unicoder.py --help

check: ; $(MAKE) tests && $(MAKE) clean

tests:
	$(PYTHON3) unicoder.py.tests.py -vvv

test_%:
	$(PYTHON3) unicoder.py.tests.py -vvv $@

clean:
	- rm *.pyc 
	- rm -rf *.tmp
	- rm -rf tmp tmp.files
	- rm TEST-*.xml
	- rm setup.py README
	- rm -rf build dist *.egg-info

############## https://pypi.org/project/unicoder

README: README.md Makefile
	cat README.md | sed -e "/\\/badge/d" > README
setup.py: Makefile
	{ echo '#!/usr/bin/env python3' \
	; echo 'import setuptools' \
	; echo 'setuptools.setup()' ; } > setup.py
	chmod +x setup.py
setup.py.tmp: Makefile
	echo "import setuptools ; setuptools.setup()" > setup.py

sdist bdist bdist_wheel:
	- rm -rf dist build unicoder.egg-info
	$(MAKE) $(PARALLEL) README setup.py
	$(PYTHON3) setup.py $@
	- rm -v setup.py README

.PHONY: build
build:
	rm -rf build dist *.egg-info
	$(MAKE) $(PARALLEL) README setup.py
	# pip install --root=~/local . -v
	$(PYTHON3) setup.py sdist
	- rm -v setup.py README
	$(TWINE) check dist/*
	: $(TWINE) upload dist/*

# ------------------------------------------------------------

mypy:
	zypper install -y mypy
	zypper install -y python3-click python3-pathspec

MYPY = mypy
MYPY_STRICT = --strict --show-error-codes --show-error-context --no-warn-unused-ignores


type: 
	$(MAKE) type.r type.t
type.r:
	$(MYPY) $(MYPY_STRICT) unicoder.py
	- rm -rf .mypy_cache
type.t:
	$(MYPY) $(MYPY_STRICT) unicoder.py.tests.py
	- rm -rf .mypy_cache

AUTOPEP8=autopep8
pep style: 
	$(MAKE) $(PARALLEL) pep.r pep.t
pep.r style.r:
	$(AUTOPEP8) unicoder.py --in-place
	git --no-pager diff unicoder.py
pep.t style.t:
	$(AUTOPEP8) unicoder.py --in-place
	git --no-pager diff unicoder.py.tests.py
