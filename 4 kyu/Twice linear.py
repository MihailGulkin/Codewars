def dbl_linear(n):
    u = [1]
    i = n * 10
    count = 2
    l = len(u)
    while l <= i:
        u.append(2 * u[len(u) - (count - 1)] + 1)
        l = len(u) + 1
        if u[-1:] == u[-2:-1]:
            u.pop()
        u.append(3 * u[len(u) - (count - 1) - 1] + 1)
        if u[-1:] == u[-2:-1]:
            u.pop()
        count += 1
    result = list(set(u))
    result.sort()
    return result[n]
