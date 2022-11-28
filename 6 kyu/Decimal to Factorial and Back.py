from string import ascii_uppercase
from math import factorial


def dec_2_fact_string(nb):
    _dict = {}
    count = 0
    for i in range(10, 36):
        _dict[i] = ascii_uppercase[count]
        count += 1
    start = 1
    my_list = []
    while nb != 0:
        num = nb % start
        if num > 9:
            num = _dict[num]
            my_list.append(num)
        else:
            my_list.append(nb % start)
        nb //= start
        start += 1
    my_list = my_list[::-1]
    return ''.join(list(map(str, my_list)))


def fact_string_2_dec(string):
    _dict = {}
    count = 0
    for i in range(10, 36):
        _dict[ascii_uppercase[count]] = i
        count += 1
    my_list = []
    for i in string:
        if i.isalpha():
            my_list.append(_dict[i])
        else:
            my_list.append(int(i))
    answer = 0
    for index, ele in enumerate(my_list[::-1]):
        answer += (ele * factorial(index))
    return answer
