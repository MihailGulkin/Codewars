from itertools import count


def beeramid(bonus, price):
    n = int(bonus / price)
    my_list = []
    for i in count():
        my_list.append(i * i)
        if sum(my_list) > n:
            if i == 0:
                return 0
            return i - 1
