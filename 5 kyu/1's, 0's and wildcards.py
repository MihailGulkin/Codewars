def rec(s, res):
    if '?' in s:
        s1 = s.replace('?', '0', 1)
        s2 = s.replace('?', '1', 1)
        rec(s1, res)
        rec(s2, res)
    else:
        res.append(s)
    return res


def possibilities(n):
    return rec(n, [])
