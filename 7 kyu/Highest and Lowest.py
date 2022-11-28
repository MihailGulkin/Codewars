import math


def high_and_low(numbers):
    _list = numbers.split(' ')
    _max = -1
    _min = math.inf
    if len(_list) > 1:
        for i in _list:
            if (_max < int(i)):
                _max = int(i)
            if (_min > int(i)):
                _min = int(i)
        return f'{_max} {_min}'
    return f'{_list[0]} {_list[0]}'
