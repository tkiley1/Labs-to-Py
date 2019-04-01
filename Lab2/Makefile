all: unit main

unit:
	python unit.py > units.txt
	cat units.txt
main:
	python main.py units.txt
clean:
	rm units.txt
	rm string.pyc