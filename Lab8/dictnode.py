class dictnode:
    def __init__(self,key = None, data = None):
        self._key = key
        self._data = [data]
        if data != None:
            self._size = 1
        else:
            self._size = 0
    def add(self, data):
        if self._data == None:
            self._data = []
        self._data.append(data)
        self._size = self._size + 1
    def get_size(self):
        return self._size
    def get_key(self):
        return self._key
    def get_data(self):
        return self._data