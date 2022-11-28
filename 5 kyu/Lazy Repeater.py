class make_looper:
    def __init__(self, s):
        self.i = -1
        self.s = s

    def __call__(self):
        self.i += 1
        return self.s[self.i % len(self.s)]