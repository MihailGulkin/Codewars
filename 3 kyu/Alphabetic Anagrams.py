from math import factorial


def listPosition(word):
    count = 0
    while len(word):
        first = word[0]
        my_uniq_set = set(word)
        possibles = factorial(len(word))
        for i in my_uniq_set:
            possibles //= factorial(word.count(i))
        for i in my_uniq_set:
            if i < first:
                count += possibles // len(word) * word.count(i)
        word = word[1:]

    return count + 1
