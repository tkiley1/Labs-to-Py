#!/usr/bin/env python
from string import *
import sys

def main():

	istream = open(sys.argv[1], 'r')
	if "Failed" in istream.read():
		print("Unit Tests Failed.")
		sys.exit(1)
	else:
		print("All Unit Tests Passed")
	s1 = String()
	istream.close()
	istream = open("dict.txt", 'r')
	my_string_extraction(s1,istream)
	print(s1._data)
	s1 = String()
	my_string_extraction(s1,istream)
	print(s1._data)


if __name__ == '__main__':
	main()
