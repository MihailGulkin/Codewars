from string import ascii_lowercase

def changer(s):
    s = s.lower()
    _dict = {}
    for index, alpha in enumerate(ascii_lowercase):
        _dict[index] = alpha
    answer = ''
    vowels_set = set('aeiou')
    for i in s:
        for j in _dict:
            if not i.isalpha():
                answer += i
                break
            some_str = ''
            if i == _dict[j]:
                if j != 25:
                    some_str = _dict[j + 1]
                if j == 25:
                    some_str = _dict[j % 25]
                if some_str in vowels_set:
                    answer += some_str.upper()
                else:
                    answer += some_str.lower()
    return answer
