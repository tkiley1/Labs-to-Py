from dictnode import *
import copy

class udict:
    def __init__(self):
        self._data = []
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
    def add(self, key, string):
        for i in self._data:
            if i.get_key() == key:
                i.add(string)
                self.balance()
                return True
        tmp = dictnode(key, string)
        self._data.append(copy.deepcopy(tmp))
        self.balance()
    def get_data(self, key):
        for i in self._data:
            if i.get_key() == key:
                return i.get_data()
        return None
    def get_keys(self):
        keys = []
        for i in self._data:
            keys.append(i.get_key())
        return keys
    def get_largest(self):
        return self._data[0].get_data()

