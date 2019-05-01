
# This is a simple dictionary node that we can use as nodes for our max heap.  Each node stores a key and a list of data
# associated with that key.
class dictnode:

    # The initialization function instantiates our data, and our key.
    def __init__(self,key = None, data = None):
        self._key = key
        self._data = [data]
        if data != None:
            self._size = 1
        else:
            self._size = 0
    # This function adds an entry to the list of data
    def add(self, data):
        if self._data == None:
            self._data = []
        self._data.append(data)
        self._size = self._size + 1

    # This function returns the length of our data list
    def get_size(self):
        return self._size
    
    # This function returns the key associated with our data
    def get_key(self):
        return self._key
    
    # This function returns the list of our data
    def get_data(self):
        return self._data