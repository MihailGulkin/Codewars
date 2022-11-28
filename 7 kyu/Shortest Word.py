def find_short(s):
    s = s.split()
    minimum = float("inf")
    for i in s:
        if minimum > len(i):
            minimum = len(i)
    return minimum
