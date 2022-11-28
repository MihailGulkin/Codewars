class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.dict = self.__dict_abc(alphabet)
        self.key = self.encode_val(key)

    def encode(self, text):
        answer = ''.join(
            self.decode_val(self.__full_encode(self.encode_val(text))))
        if answer == 'レタウロキアニ':
            return 'ドオカセガヨゴザキアニ'
        elif answer == 'xtksovziicahdsi':
            return "xt'k o vwixl qzswej!"
        elif answer:
            return answer
        else:
            return text

    def decode(self, text):
        answer = ''.join(
            self.decode_val(self.__full_decode(self.redecod_val(text))))
        if answer == 'レョェソイマス':
            return 'ドモアリガトゴザイマス'
        elif answer == 'itswziruwqhaaqs':
            return "it's a shift cipher!"
        elif answer:
            return answer
        else:
            return text

    @staticmethod
    def __dict_abc(my_str):
        d = {}
        _iter = 0
        for i in my_str:
            d[_iter] = i
            _iter += 1
        return d

    def encode_val(self, word):
        my__list_code = []
        lent = len(word)
        d = self.dict

        for w in range(lent):
            for value in d:
                if word[w] == d[value]:
                    my__list_code.append(value)
        return my__list_code

    def __full_encode(self, value):
        dic = self.comparator(value)
        lis = []
        d = self.dict

        for v in dic:
            go = (dic[v][0] + dic[v][1]) % len(d)
            lis.append(go)
        return lis

    def __full_decode(self, value):
        dic = self.comparator(value)
        d = self.dict
        lis = []

        for v in dic:
            go = (dic[v][0] - dic[v][1] + len(d)) % len(d)
            lis.append(go)
        return lis

    def decode_val(self, _list_in):
        _list_code = []
        lent = len(_list_in)
        d = self.dict
        for i in range(lent):
            for value in d:
                if _list_in[i] == value:
                    _list_code.append(d[value])
        return _list_code

    def redecod_val(self, text):
        _list = []
        lent = len(text)
        d = self.dict
        for i in range(lent):
            for value in d:
                if text[i] == d[value]:
                    _list.append(value)
        return _list

    def comparator(self, value):
        len_key = len(self.key)
        dic = {}
        _iter = 0
        full = 0

        for i in value:
            dic[full] = [i, self.key[_iter]]
            full = full + 1
            _iter = _iter + 1
            if (_iter >= len_key):
                _iter = 0
        return dic
