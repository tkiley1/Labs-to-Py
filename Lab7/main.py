#!/usr/bin/env python
from string import *
import sys, copy

def gen_key(string, char):
	tmp = String()
	for i in range(string.get_size()):
		if string._data[i] == char:
			my_string_push_back(tmp, char)
		else:
			my_string_push_back(tmp, '-')
	return my_string_c_string(tmp)

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


	d = input("Enter a word length: ")
	while(int(d) < 1 or int(d) > 21):
		d = input("Enter a word length between 1 and 21: ")
	selected_bucket = string_buckets[int(d)]
	p_key = String()
	for i in range(int(d)):
		my_string_push_back(p_key, '-')

	guessed = []
	while(1):
		my_string_insertion(p_key)
		buckets = dict()
		guess = input("\nGuess a letter: ")
		if guess not in guessed:
			guessed.append(guess)
		else:
			continue
		#my_string_insertion(p_key)
		for i in selected_bucket:
			c = gen_key(i, guess)
			if c in buckets.keys():
				buckets[c].append(i)
			else:
				buckets[c] = [i]

		longest = 0
		for i in buckets.keys():
			print(i + " : " + str(len(buckets[i])))
			if len(buckets[i]) > longest:
				longest = len(buckets[i])
				pkey = copy.deepcopy(i)
				selected_bucket = copy.deepcopy(buckets[i])

		c = gen_key(selected_bucket[0], guess)
		new_string = String()
		for i in range(p_key.get_size()):
			if c[i] == '-' and my_string_at(p_key, i) == '-':
				my_string_push_back(new_string, '-')
			elif c[i] == '-':
				my_string_push_back(new_string, my_string_at(p_key, i))
			else:
				my_string_push_back(new_string, c[i])
		my_string_assignment(p_key, new_string)

if __name__ == '__main__':
	main()
