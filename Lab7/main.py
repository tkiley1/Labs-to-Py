#!/usr/bin/env python3
from string import *
import sys, copy

# Key generator function
# Given a valid string object and a character, the function will return the proper key to be used in the
# associative array (dictionary) in the form of a python string.
def gen_key(string, char):
	tmp = String()
	for i in range(string.get_size()):
		if string._data[i] == char:
			my_string_push_back(tmp, char)
		else:
			my_string_push_back(tmp, '-')
	return my_string_c_string(tmp)

def main():
	# First read the output of the unit tests functions to make sure that there are no errors in 
	# our code.
	istream = open(sys.argv[1], 'r')
	if "Failed" in istream.read():
		print("Unit Tests Failed.")
		sys.exit(1)
	else:
		print("All Unit Tests Passed")

	# This solution implements the Evil Hangman game using a 2 python dictionaries.
	# one is an int:list pairing to hold the initial structure of 'buckets' of each
	# word of length x.  The second is a String():list pairing that is used to keep 
	# track of all the possible outcomes that the game could choose to play the game. 
	
	# First read every word from the dictionary into the bucket dictionary, then wait for the user
	# to choose a word length
	string_buckets = dict()
	f = open("dictionary.txt", 'r')
	tmp = String()
	while(my_string_extraction(tmp, f)):
		if tmp.get_size() not in string_buckets.keys():
			string_buckets[tmp.get_size()] = [copy.copy(tmp)]
		else:
			string_buckets[tmp.get_size()] = string_buckets[tmp.get_size()] + [copy.copy(tmp)]
		tmp = String()

	# Get and validate a word length, and a number of guesses input from the user 
	word_length = int(input("Enter a word length: "))
	while(int(word_length) < 1 or int(word_length) > 21):
		word_length = int(input("Enter a word length between 1 and 21: "))
	selected_bucket = string_buckets[int(word_length)]
	num_guesses = int(input("Enter a number of guesses: "))
	while(int(num_guesses) < 1 or int(num_guesses) > 26):
		num_guesses = int(input("Enter a number of guesses between 1 and 26: "))

	# initialize a string object to hold the key that we show the user
	p_key = String()
	for i in range(int(word_length)):
		my_string_push_back(p_key, '-')

	# loop for the number of guesses that the user wants to play for
	guessed = []
	for i in range(num_guesses):
		print("You have " + str(num_guesses-1) + "Guesses remaining")
		string_check = 0
		my_string_insertion(p_key)
		for i in range(p_key.get_size()):
			if my_string_at(p_key,i) == '-':
				string_check = 1
		if string_check == 0:
			print("You Win!")
			return
		buckets = dict()
		guess = input("\nGuess a letter: ")
		while guess in guessed:
			print("You have already guessed " + guess)
			guess = input("\nGuess a letter: ")
		guessed.append(guess)

		# generate a key for each word in the selected bucket, and 
		# add it to the dictionary of key:list pairs
		for i in selected_bucket:
			c = gen_key(i, guess)
			if c in buckets.keys():
				buckets[c].append(i)
			else:
				buckets[c] = [i]

		# loop through the dictionary of key:list pairs to 
		# select the longest one, in order to truck the user
		longest = 0
		for i in buckets.keys():
			print(i + " : " + str(len(buckets[i])))
			if len(buckets[i]) > longest:
				longest = len(buckets[i])
				pkey = copy.deepcopy(i)
				selected_bucket = copy.deepcopy(buckets[i])

		# This code is to make sure that we update the key we show to the user after each
		# pass.  The user won't get many letters, but it is important to make sure it is
		# updated.
		c = String(gen_key(selected_bucket[0], guess))
		new_string = String()
		for i in range(p_key.get_size()):
			if my_string_at(c, i) == '-' and my_string_at(p_key, i) == '-':
				my_string_push_back(new_string, '-')
			elif my_string_at(c, i) == '-':
				my_string_push_back(new_string, my_string_at(p_key, i))
			else:
				my_string_push_back(new_string, my_string_at(c, i))
		my_string_assignment(p_key, new_string)
	for i in range(p_key.get_size()):
				if my_string_at(p_key,i) == '-':
					string_check = 1
	if string_check == 0:
		print("You Win!")
		return
	print("Sorry, you lose! The word was " + my_string_c_string(selected_bucket[0]))


if __name__ == '__main__':
	main()
