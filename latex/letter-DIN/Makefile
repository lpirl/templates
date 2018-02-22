TMP?=/tmp/
DIRNAME=$(shell basename "$$(pwd)")
TMPDIR?=$(TMP)/$(DIRNAME)

TEXS?=$(wildcard *.tex)
PDFS+=$(TEXS:.tex=.pdf)
TXTS+=$(TEXS:.tex=.txt)

LATEXMKFLAGS+=-pdf

########################################################################
# top-level targets for compilation in /tmp
#

all: pdf_in_tmp

%_in_tmp:
	rsync -qa --inplace "../$(DIRNAME)" "$(TMP)"
	make -j $(shell nproc) -C "$(TMPDIR)" $*


########################################################################
# top-level targets
#

_pdf_common: $(PDFS)

debug: _pdf_common

pdf: LATEXMKFLAGS += -quiet
pdf: _pdf_common

########################################################################
# targets for specific files
#

.PHONY: $(TEXS)
%.pdf: %.tex
	latexmk $(LATEXMKFLAGS) $^

count: $(TEXS)
	texcount $^

%.txt: pdf
	pdftotext $*.pdf > $@

.PHONY: languagetool
languagetool: $(TXTS)
	languagetool-commandline -l en-US $(TXTS) | less

.PHONY: lint
lint:
	for f in $(TEXS); do \
		lacheck $$f; \
		chktex $$f; \
	done

clean:
	latexmk -c
	rm -f \
		*-blx.bib \
		*.bbl \
		*.run.xml \
		$(PDFS) \
		$(TXTS)
	rm -rf "$(TMPDIR)"
