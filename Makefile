VENV = venv
PYTHON = $(VENV)/Scripts/python
PIP = $(VENV)/Scripts/pip

run: $(VENV)/bin/activate
	$(PYTHON) __main__.py

# automatically reinstall the dependencies whenever the requirements.txt file changes
$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
 	# TODO remove this comment on the requiements.txt \
	# $(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)

.PHONY: run clean


