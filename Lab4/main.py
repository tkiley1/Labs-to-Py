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
	fp = open("dictionary.txt", 'r')
	s1 = String()
	while(my_string_extraction(s1,fp)):
		if s1.get_size() > 20:
			my_string_push_back(s1, '#')
			my_string_insertion(s1)
		s1 = String()



if __name__ == '__main__':
	main()
