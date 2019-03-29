
# String Class - has a capacity, a size, and an array that holds the charachters of the string.
#
#

class String:
	
	# This is both the custom and the default init function.  
	# if the user passes in a value for capacity, the users values will be used
	# otherwise, capacity will be defaulted to 7.
	def __init__(self, capacity = 7):
		print("IN INIT")
		self._capacity = capacity
		self._size = 0
	def get_size(self):
		return self._size
	def get_capacity(self):
		return self._capacity
