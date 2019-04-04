
# String Class - has a capacity, a size, and an array that holds the charachters of the string.
#
#

class String:
	
	# This is the default constructor  
	# This method will instantiate and return a string object with size 0 and capacity 7
	
	# Returns the value that represents the size of the string
	def get_size(self):
		return self._size

	# Returns the value that represents the capacity that the string can hold
	def get_capacity(self):
		return self._capacity
	
	# This is the custom initializer.  This method will instantiate a string object that represents the 
	# string passed in by the user.  It will initialize size to be the length of the string, and capacity to 
	# be the length of the string + 1
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

def my_string_extraction(string, file):
	while(1):
		char = file.read(1)
		if not(char.isspace()):
			break
	while(1):
		if char.isspace():
			break
		if string.get_capacity() <= string.get_size()+1:
			tmp = string._data
			string._capacity = string._capacity * 2
			string._data = [None] * string.get_capacity() * 2
			for i in range(len(tmp)):
				string._data[i] = tmp[i]
		string._data[string.get_size()] = char
		string._size = string._size + 1
		char = file.read(1)
	if string.get_size() == 0:
		return False
	return True

	
