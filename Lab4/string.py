import sys
# String Class - has a capacity, a size, and an array that holds the charachters of the string.
#
#

class String:
	
	# Returns the value that represents the size of the string
	def get_size(self):
		return self._size

	# Returns the value that represents the capacity that the string can hold
	def get_capacity(self):
		return self._capacity
	
	# This is the custom initializer and the default constructor.  This method will instantiate a string object that represents the 
	# string passed in by the user.  It will initialize size to be the length of the string, and capacity to 
	# be the length of the string + 1
	# if no string is passed, it will instantiate the string with a capacity of 7, size of 0 and empty data
	def __init__(self, string=None):
		if string == None:
			self._capacity = 7
			self._size = 0
			self._data = [None] * self._capacity
			return
		self._capacity = len(string) + 1
		self._size = len(string)
		self._data =  [None]*self._capacity
		for i in range(len(string)):
			self._data[i] = string[i]



# This function will lexicographically compare string objects.  It will return 0 if the strings are equal;
# > 0 if left is smaller than right, and <0 if right is smaller than left.
def my_string_compare(stringL, stringR):
	if not (isinstance(stringL, String) or isinstance(stringR, String)):
		return None

	if stringL.get_size() < stringR.get_size():
		return -1

	elif stringL.get_size() > stringR.get_size():
		return 1

	else:
		for i in range(stringL.get_size()):
			if stringL._data[i] < stringR._data[i]:
				return -1
			if stringL._data[i] > stringR._data[i]:
				return 1

	return 0


# This function takes a String object and an active file object. It will read from the file object
# ignoring leading whitespace, and then reading non-whitepsace chatachters until it encounters another 
# whitespace character, effectively reading one word from the file.  It will then fill the String object
# with the extracted string.  It will return True on success, and False on failure.
def my_string_extraction(string, file):
	last_pos = file.tell()
	char = file.read(1)
	while(char.isspace() or char == '\n' or char == '\t'):
		# print("Looping through Whitespace")
		if char == '':
			return False
		last_pos = file.tell()
		char = file.read(1)
	while(not(char.isspace()) and not(char == '\n') and not(char == '\t') and (not char == '')):
		# print("Looping Through String")
		if string.get_capacity() <= string.get_size()+1:
			tmp = string._data
			string._capacity = string._capacity * 2
			string._data = [None] * string.get_capacity() * 2
			for i in range(len(tmp)):
				string._data[i] = tmp[i]
		string._data[string.get_size()] = char
		string._size = string._size + 1
		lastpos = file.tell()
		char = file.read(1)
	if string.get_size() == 0:
		return False
	if char == '':
		return True
	# file.seek(last_pos)
	return True

# This function is intended to take in a string object and a stream, and print the contents of the string
# to the specified stream.  If no file pointer is provided, the function will output the contents of the 
# string to stdout
def my_string_insertion(string, stream=None):
	if stream == None:
		for i in string._data:
			if not(i == None):
				sys.stdout.write(i)
	else:
		for i in string._data:
			if not(i == None):
				stream.write(i)
	return True

	
def my_string_push_back(string, char):
	if string._size >= string._capacity -1:
		tmp = string._data
		string._capacity = string._capacity * 2
		string._data = [None] * string._capacity
		for i in range (string._size):
			string._data[i] = tmp[i]
		string[string._size] = char
		string._size = string._size + 1
	else:
		string._data[string._size] = char
		string._size = string._size + 1
	return True

def my_string_pop_back(string):
	return

def my_string_at(string, index):
	return

def my_string_concat(string1, string2):
	return

def my_string_empty(string):
	return