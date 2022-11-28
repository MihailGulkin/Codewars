def count(string):
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count