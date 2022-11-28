import numpy as np


def lcm(*args):
    my_list = list(args)
    if len(my_list) == 1:
        return args[0]
    elif len(my_list) == 0:
        return 1
    while len(my_list) != 1:
        my_list[0] = np.lcm(my_list[0], my_list[1])
        my_list.pop(1)
    return my_list[0]
