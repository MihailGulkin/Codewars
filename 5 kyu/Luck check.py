def luck_check(string):
    string_1_2 = string[0:int(len(string) / 2)]
    if len(string) % 2 == 0:
        string_2_2 = string[int(len(string) / 2):]
    else:
        string_2_2 = string[int(len(string) / 2) + 1:]
    return sum(map(lambda x: int(x), string_1_2)) == sum(
        map(lambda x: int(x), string_2_2))
