def unique_in_order(iterable):
    iterable = list(iterable)
    i = 0
    while i != len(iterable):
        if (i + 1 == len(iterable)):
            return iterable
        if (iterable[i] == iterable[i + 1]):
            iterable.pop(i + 1)
        else:
            i += 1
    return iterable
