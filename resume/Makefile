SRC := main.tex
LATEXMK := latexmk -pdf -interaction=nonstopmode -halt-on-error

ROOT := ..
ACADEMIC_PDF := $(ROOT)/resume.pdf
PROFESSIONAL_PDF := $(ROOT)/resume-single-page.pdf

.PHONY: all academic professional clean distclean

all: academic professional

academic:
	$(LATEXMK) -jobname=academic '-usepretex=\def\academictrue{}' $(SRC)
	cp academic.pdf $(ACADEMIC_PDF)

professional:
	$(LATEXMK) -jobname=professional $(SRC)
	cp professional.pdf $(PROFESSIONAL_PDF)

clean:
	latexmk -c -jobname=academic $(SRC)
	latexmk -c -jobname=professional $(SRC)

distclean:
	latexmk -C -jobname=academic $(SRC)
	latexmk -C -jobname=professional $(SRC)
