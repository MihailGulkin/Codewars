class DefaultList:
    def __init__(self, arr, err):
        self.arr = arr[:]
        self.err = err

    def __getitem__(self, item):
        try:
            return self.arr[item]
        except:
            return self.err

    def append(self, other):
        self.arr.append(other)

    def extend(self, other):
        self.arr.extend(other)

    def remove(self, key):
        try:
            self.arr.remove(key)
        except:
            return self.err

    def pop(self, key):
        try:
            self.arr.pop(key)
        except:
            return self.err

    def insert(self, index, value):
        self.arr.insert(index, value)
