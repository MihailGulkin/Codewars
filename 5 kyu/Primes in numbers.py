def getmulti(number):
    result = []
    probe = 2
    while number != 1:
        if number % probe != 0:
            probe += 1
        else:
            number /= probe
            result += [probe]
    return result


def _list_in__dict(number):
    _list = getmulti(number)
    _dict = {}
    for i in _list:
        if i not in _dict:
            _dict[i] = 1
        else:
            _dict[i] += 1
    return _dict


def prime_factors(number):
    answer = ''
    _dict = _list_in__dict(number)
    for i in _dict:
        if _dict[i] > 1:
            answer += f'({i}**{_dict[i]})'
        else:
            answer += f'({i})'
    return answer