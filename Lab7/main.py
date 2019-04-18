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


	string_buckets = dict()
	f = open("dictionary.txt", 'r')
	tmp = String()
	while(my_string_extraction(tmp, f)):
		if tmp.get_size() not in string_buckets.keys():
			string_buckets[tmp.get_size()] = [copy.copy(tmp)]
		else:
			string_buckets[tmp.get_size()] = string_buckets[tmp.get_size()] + [copy.copy(tmp)]
		tmp = String()

	d = raw_input("Enter a word length: ")
	while(int(d) < 1 or int(d) > 21):
		d = raw_input("Enter a word length between 1 and 21: ")
	selected_bucket = string_buckets[int(d)]
	while(1):
		# Do Game
			# get letter from user
			# store in guessed already list
			# sort the bucket into new buckets on index of the character
				#need to account for multiple indexes as well
			# grab the new bucket with the greatest length, and update the screen with the index key
			# *whistle* AGAIN
		return


if __name__ == '__main__':
	main()
