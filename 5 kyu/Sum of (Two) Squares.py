from math import sqrt


def all_squared_pairs(n):
    x = 0
    big_list = []
    y = int(sqrt(n))
    while x <= y:
        if x * x + y * y < n:
            x += 1
        elif (x * x + y * y > n):
            y -= 1
        else:
            big_list.append([x, y])
            x += 1
            y -= 1
    return big_list
