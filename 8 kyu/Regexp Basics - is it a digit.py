from re import fullmatch


def is_digit(n):
    return True if fullmatch(r'[0-9]', n) else False
