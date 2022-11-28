class SecureList:
    def __init__(self, array):
        self.array = array[:]

    def __getitem__(self, other):
        return self.array.pop(other)

    def __str__(self):
        try:
            temp_array = self.array
            del self.array
            return str(temp_array)
        except:
            pass
        return str([])

    def __repr__(self):
        try:
            temp_array = self.array
            del self.array
            return str(temp_array)
        except:
            pass
        return str([])

    def __len__(self):
        try:
            return len(self.array)
        except:
            return 0
