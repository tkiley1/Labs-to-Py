#!/usr/bin/env python
from string import *
import sys, copy

def main():

	istream = open(sys.argv[1], 'r')
	if "Failed" in istream.read():
		print("Unit Tests Failed.")
		sys.exit(1)
	else:
		print("All Unit Tests Passed")
	head_string = String("Copy Me")
	s_list = [None] * 100
	for i in range(99):
		c = String()
		my_string_assignment(c, head_string)
		s_list[i] = c
	for i in s_list:
		my_string_insertion(i)
	





if __name__ == '__main__':
	main()
