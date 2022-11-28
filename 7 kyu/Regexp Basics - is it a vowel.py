from re import fullmatch


def is_vowel(s):
    return bool(fullmatch(r'[aeiouAEIOU]', s))
