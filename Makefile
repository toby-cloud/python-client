# Toby Makefile
# Note: all separators must be tabs, not spaces

init:
	pip install -r requirements.txt

test:
	py.test .
<<<<<<< HEAD
	make clean

coverage:
	coverage run --source . -m py.test
	coverage report
	make clean
=======
>>>>>>> 3979969cc0a0848763f59ca31a6fb41cbf2d6248

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

<<<<<<< HEAD
.PHONY: init test coverage clean
=======
.PHONY: init test clean
>>>>>>> 3979969cc0a0848763f59ca31a6fb41cbf2d6248
