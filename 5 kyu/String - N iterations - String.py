def jumbled_string(s, n):
    count = 1
    true_s = s
    s = s[::2] + s[1::2]
    while s != true_s:
        s = s[::2] + s[1::2]
        count += 1
    n -= (n // count) * count
    for i in range(n):
        s = s[::2] + s[1::2]
    return s
