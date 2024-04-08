#! /usr/bin/make -f

BASEYEAR= 2021
FOR=today

FILES = *.py *.cfg
PYTHON3 = python3
COVERAGE3 = $(PYTHON3) -m coverage
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

tests: ;  $(PYTHON3) unicoder.py.tests.py -vvv $(TESTFLAGS)
test_%: ; $(PYTHON3) unicoder.py.tests.py -vvv $(TESTFLAGS) $@

ests: ;  $(COVERAGE3) run unicoder.py.tests.py -vvv $(TESTFLAGS)
est_%: ; $(COVERAGE3) run unicoder.py.tests.py -vvv $(TESTFLAGS) t$@

COVERAGEFILES = unicoder.py
cov coverage: 
	$(COVERAGE3) erase 
	$(MAKE) ests 
	$(COVERAGE3) xml $(COVERAGEFLAGS) $(COVERAGEFILES)
	$(COVERAGE3) annotate $(COVERAGEFLAGS) $(COVERAGEFILES)
	$(COVERAGE3) report $(COVERAGEFLAGS) $(COVERAGEFILES)
	@ wc -l unicoder.py,cover | sed -e "s/^\\([^ ]*\\)  *\\(.*\\)/\\2      \\1 lines/"


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
PIP3=pip3
install:
	$(MAKE) setup.py
	trap "rm -v setup.py" SIGINT SIGTERM ERR EXIT ; \
	$(PIP3) install .
uninstall:
	$(PIP3) uninstall -y `sed -e '/name *=/!d' -e 's/name *= *//' setup.cfg`

# ------------------------------------------------------------
old = tmp.unicoder
unicoder:
	- rm -rf $(old)
	mkdir $(old)
	echo "[metadata]" > $(old)/setup.cfg
	echo "name = unicoder" >> $(old)/setup.cfg
	grep "version *=" setup.cfg >> $(old)/setup.cfg
	grep "license *=" setup.cfg >> $(old)/setup.cfg
	grep -A 1 "license_files *=" setup.cfg >> $(old)/setup.cfg
	cp -v LICENSE $(old)/
	grep "author *=" setup.cfg >> $(old)/setup.cfg
	grep "author-email *=" setup.cfg >> $(old)/setup.cfg
	grep "home-page *=" setup.cfg >> $(old)/setup.cfg
	echo "description = deprecated unicoder package, use text-unicoder instead" >> $(old)/setup.cfg
	echo "The 'unicoder' PyPI package is deprecated, use 'text-unicoder' rather than 'unicoder' for pip commands." > $(old)/README
	echo "" >> $(old)/README
	echo "long-description = file: README"  >> $(old)/setup.cfg
	echo "long-description-content-type = text/markdown"  >> $(old)/setup.cfg
	echo "Please replace 'unicoder' in your pip requirements"  >> $(old)/README
	echo "(requirements.txt, setup.py, setup.cfg) with 'text-unicoder'."  >> $(old)/README
	echo "For the next years this wrapper package continues to exist"  >> $(old)/README 
	echo "which has a dependency on the new package name."  >> $(old)/README
	echo "requires-dist = setuptools"  >> $(old)/README
	echo "requires = text_unicoder"  >> $(old)/README
	{ echo '#!/usr/bin/env python3' \
	; echo 'import setuptools' \
	; echo 'setuptools.setup()' ; } > $(old)/setup.py
	chmod +x $(old)/setup.py
	cd $(old) && $(PYTHON3) setup.py sdist
	cd $(old) && $(TWINE) check dist/*
	@ echo ": cd $(old) && $(TWINE) upload dist/*"

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
	$(MYPY) $(MYPY_STRICT) unicoder.py.tests.py --ignore-missing-imports --exclude=build
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
