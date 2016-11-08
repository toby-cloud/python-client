# Toby Makefile
# Note: all separators must be tabs, not spaces

init:
	pip install -r requirements.txt

test:
	py.test .

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

.PHONY: init test clean
