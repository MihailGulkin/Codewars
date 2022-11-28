import re


def disemvowel(_string):
    return re.sub(r'[aeuioAEUIO]', '', _string)
