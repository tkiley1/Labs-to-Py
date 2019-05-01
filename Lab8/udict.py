from dictnode import *
import copy

class udict:
    # Initialization function - all we need is a list that holds our key value dictnodes
    def __init__(self):
        self._data = []

    # This function maintains the max heap property within the data, so the largest bucket is always stored as the root
    # node, or at index 0
    def balance(self):
        c = 1
        while c > 0:
            c = 0
            for i in range(len(self._data)-1):
                if self._data[i].get_size() < self._data[i+1].get_size():
                    tmp = copy.deepcopy(self._data[i])
                    self._data[i] = copy.deepcopy(self._data[i+1])
                    self._data[i+1] = tmp
                    c = c + 1
    # This function adds data to our heap.  If the key already exists, we add to the node and balance; if not, we create a new 
    # node, add it to the tree, and balance.
    def add(self, key, string):
        for i in self._data:
            if i.get_key() == key:
                i.add(string)
                self.balance()
                return True
        tmp = dictnode(key, string)
        self._data.append(copy.deepcopy(tmp))
        self.balance()

    # This function returns the list of string objects associated with a given key.
    def get_data(self, key):
        for i in self._data:
            if i.get_key() == key:
                return i.get_data()
        return None

    # This function returns all of the keys within our data
    def get_keys(self):
        keys = []
        for i in self._data:
            keys.append(i.get_key())
        return keys
    
    # This function returns the largest bucket within our data, which by default will be the root node of our 
    # max-heap
    def get_largest(self):
        return self._data[0].get_data()

