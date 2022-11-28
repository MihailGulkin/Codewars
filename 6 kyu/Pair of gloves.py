def number_of_pairs(gloves):
    my_dict = {}
    for glove in gloves:
        if glove not in my_dict:
            my_dict[glove] = 1
        else:
            my_dict[glove] += 1
    return sum(my_dict[glove] // 2 for glove in my_dict)
