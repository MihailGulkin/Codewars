def separate_liquids(glass):
    big_list = []
    _dict = {
        'H': 1.36,
        'W': 1.00,
        'A': 0.87,
        'O': 0.80
    }
    for i in range(len(glass)):
        for j in range(len(glass[i])):
            print(i, j)
            glass[i][j] = _dict[glass[i][j]]
    for i in glass:
        big_list += i
    big_list.sort()
    for i in range(len(big_list)):
        for k in _dict:
            if big_list[i] == _dict[k]:
                big_list[i] = k
                break
    for i in range(len(glass)):
        for j in range(len(glass[i])):
            glass[i][j] = big_list[0]
            big_list.pop(0)
    return glass
