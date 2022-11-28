from string import ascii_lowercase


def rot13(s):
    _dict = {}
    for index, alpha in enumerate(ascii_lowercase):
        _dict[index] = alpha
    answer = ''
    for i in s:
        flag = False
        for j in _dict:
            if not i.isalpha():
                answer += i
                break
            some_str = ''
            if i.isupper():
                flag = True
            i = i.lower()
            if i == _dict[j]:
                some_str = _dict[(j + 13) % 26]
            if flag:
                answer += some_str.upper()
            else:
                answer += some_str.lower()
    return answer
