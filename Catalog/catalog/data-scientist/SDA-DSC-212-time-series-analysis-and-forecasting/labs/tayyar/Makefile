.PHONY: help doctor data reference figures posters deck assessment labs notebooks clean all

help:
	@echo "SDA-DSC-212 — Tayyar course repository"
	@echo ""
	@echo "  make doctor      check the environment and print a per-package report"
	@echo "  make data        regenerate every dataset under data/"
	@echo "  make reference   run the reference pipeline; writes reference_results.json + figures/"
	@echo "  make figures     regenerate the conceptual diagrams"
	@echo "  make posters     regenerate the A4 classroom posters"
	@echo "  make deck        rebuild the PowerPoint training deck"
	@echo "  make assessment  rebuild the assessment workbook"
	@echo "  make notebooks   regenerate all 14 lab notebooks"
	@echo "  make all         data -> reference -> figures -> posters -> deck -> assessment"

doctor:
	@python tools/doctor.py

data:
	python tools/make_tayyar_data.py

reference:
	python tools/run_reference.py
	python tools/leak_demo.py

figures:
	python tools/make_diagrams.py
	python tools/fix_figures.py

posters:
	python tools/make_posters.py

deck:
	node deck/build.js

assessment:
	python tools/make_assessment.py

notebooks:
	python tools/make_notebooks.py
	python tools/make_notebooks_23.py
	python tools/make_notebooks_45.py
	python tools/make_notebooks_67.py

all: data reference figures posters deck assessment

clean:
	rm -f slide-*.jpg *.pdf
