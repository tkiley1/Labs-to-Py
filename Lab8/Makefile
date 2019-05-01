all: unit main

unit:
	python3 unit.py > units.txt
	cat units.txt
main:
	python3 main.py units.txt
clean:
	rm units.txt
	rm string.pyc