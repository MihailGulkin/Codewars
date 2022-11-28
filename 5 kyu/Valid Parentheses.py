from re import sub


def valid_parentheses(string):
    string = sub('[A-z]', '', string)
    if string.count('(') != string.count(')'):
        return False
    while len(string) != 0:
        if len(string) == len(string.replace('()', '')):
            return False
        string = string.replace('()', '')
    return True
