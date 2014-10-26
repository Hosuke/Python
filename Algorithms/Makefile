
ALL_PY_FILES = $(shell ls *.py)

default: runtest

runtest:
	python test.py

test.output.txt: $(ALL_PY_FILES)
	python test.py > test.output.txt

clean:
	rm -f *~ *.pyc

clobber: clean
