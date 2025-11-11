# Extended Makefile – retains Sphinx‑quickstart defaults but adds a real
# "docs" meta‑target and PDF copy step.
#
# Usage
#   make docs      ➜ builds HTML and PDF in one go (default goal)
#   make html      ➜ HTML only (unchanged)
#   make latexpdf  ➜ PDF only (unchanged)
#   make clean     ➜ rm -rf _build
#
# ---------------------------------------------------------------------------

.DEFAULT_GOAL := docs

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
SOURCEDIRUSERGUIDE     = .
BUILDDIR      = _build
PDFNAME       = rstcheatsheet.pdf
PDFTITLEUSERGUIDE = "reStructuredText Cheat Sheet"
PDFNAMEUSERTMP   = restructuredtextcheatsheet.pdf
PDFNAMEUSER   = rst_cheat_sheet.pdf


.PHONY: help docs html latexpdf clean

# keep the original help target
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# explicit rule to build HTML via Sphinx make‑mode
html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# explicit rule to build PDF via Sphinx make‑mode, then copy it to docs root
latexpdf:
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@cp "$(BUILDDIR)/latex/$(PDFNAME)" "$(SOURCEDIR)/$(PDFNAME)"

# meta‑target: build both flavours
# Calling $(MAKE) rather than recursive sphinx-build keeps log separation.
docs: html sheetpdf
	@echo "HTML ➜ $(BUILDDIR)/html | PDF ➜ $(PDFNAME)"

# original clean behaviour
clean:
	rm -rf "$(BUILDDIR)"

# Build PDF
sheetpdf:
	$(SPHINXBUILD) -b latex -D master_doc=index -D project=$(PDFTITLEUSERGUIDE) . $(BUILDDIR)/latex_user
	@echo "Running LaTeX for User Guide..."
	@$(MAKE) -C $(BUILDDIR)/latex_user all-pdf
	@cp $(BUILDDIR)/latex_user/$(PDFNAMEUSERTMP) $(SOURCEDIR)/$(PDFNAMEUSER)
