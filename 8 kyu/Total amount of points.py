def calc(_str):
    _str = list(map(int, str.split(':')))
    if _str[0] > _str[1]:
        return 3
    if _str[0] == _str[1]:
        return 1
    return 0


def points(games):
    return sum(list(map(calc, games)))
