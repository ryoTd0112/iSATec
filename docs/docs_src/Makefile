# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJDIR = ../../isatec
SOURCEDIR     = .
BUILDDIR      = ../

# Put it first so that "make" without argument is like "make help".
# help:
# 	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# help:
# 	@sphinx-build -h
# .PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
apidoc:
	@sphinx-apidoc -f -o $(SOURCEDIR) $(SPHINXPROJDIR)

build_html:
	@sphinx-build -b html $(SOURCEDIR) $(BUILDDIR)

build_html_force:
	@sphinx-apidoc -f -o $(SOURCEDIR) $(SPHINXPROJDIR)
	@sphinx-build -b html $(SOURCEDIR) $(BUILDDIR)
