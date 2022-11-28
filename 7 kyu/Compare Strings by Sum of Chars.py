from string import ascii_uppercase


def compare(s1, s2):
    try:
        if len(s1) == 0 or len(s2) == 0:
            return True
    except:
        return True

    for i in s2.upper():
        if i not in ascii_uppercase:
            s2 = ''
    for i in s1.upper():
        if i not in ascii_uppercase:
            s1 = ''
    if s1 == s2:
        return True
    return sum(list(map(ord, s1.upper()))) == sum(list(map(ord, s2.upper())))
