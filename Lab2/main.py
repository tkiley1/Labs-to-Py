#!/usr/bin/env python
from string import String
import sys

def main():

	istream = open(sys.argv[1], 'r')
	if "Failed" in istream.read():
		print("Unit Tests Failed.")
		sys.exit(1)
	else:
		print("All Unit Tests Passed")
	s1 = String("Hello World")


if __name__ == '__main__':
	main()
