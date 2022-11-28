def skob(string):
    index = 0
    count = string.count('(')
    my_count = 0

    while index != len(string) - 1:
        if (string[index] == "(" and string[-index - 1] == ')') \
                or (string[index] == '(' and string[index + 1] == ')'):
            index += 1
            my_count += 1
        else:
            index += 1
    return my_count == count


def skob_1(string):
    index = 0
    count = string.count('{')
    my_count = 0
    while index != len(string) - 1:
        if (string[index] == "{" and string[-index - 1] == '}') \
                or (string[index] == '{' and string[index + 1] == '}'):
            index += 1
            my_count += 1
        else:
            index += 1
    return my_count == count


def skob_2(string):
    index = 0
    count = string.count('[')
    my_count = 0
    while index != len(string) - 1:
        if (string[index] == "[" and string[-index - 1] == ']') \
                or (string[index] == '[' and string[index + 1] == ']'):
            index += 1
            my_count += 1
        else:
            index += 1
    return my_count == count


def validBraces(string):
    if string.count('(') != string.count(')') \
            or string.count('[') != string.count(']') \
            or string.count('{') != string.count('}') or '}{' in string:
        return False
    return skob_1(string) and skob_2(string) and skob(string)
