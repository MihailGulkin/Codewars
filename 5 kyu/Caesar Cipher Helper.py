from string import ascii_lowercase


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def decode(self, st):
        _dict = self.__dict_abc()
        st = st.lower()
        for index, i in enumerate(st):
            for value in _dict:
                if i == _dict[value]:
                    if (value - self.shift) >= 0:
                        st = st[:index] + _dict[value - self.shift] + st[
                                                                     index + 1:]
                    else:
                        st = st[:index] + _dict[(value - self.shift) % 26] + st[
                                                                            index + 1:]
        return st.upper()

    def encode(self, st):
        dict = self.__dict_abc()
        st = st.lower()
        for index, i in enumerate(st):
            for value in dict:
                if i == dict[value]:
                    if (value + self.shift) < 26:
                        st = st[:index] + dict[value + self.shift] + st[
                                                                     index + 1:]
                    else:
                        st = st[:index] + dict[(value + self.shift) % 26] + st[
                                                                            index + 1:]
        return st.upper()

    @staticmethod
    def __dict_abc():
        my_str = ascii_lowercase
        d = {}
        _iter = 0
        for i in my_str:
            d[_iter] = i
            _iter += 1
        return d
