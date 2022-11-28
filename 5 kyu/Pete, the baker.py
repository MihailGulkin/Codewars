def cakes(recipe, available):
    next_dict = {}
    for key_1 in available:
        for key_2 in recipe:
            if key_1 == key_2:
                next_dict[key_1] = int(available[key_1] / recipe[key_2])
                break
    for key_1 in recipe:
        flag = False
        for key_2 in available:
            if key_1 == key_2:
                flag = True
                break
        if not flag:
            return 0
    return min(next_dict.values())