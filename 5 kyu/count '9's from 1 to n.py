def count_nines(n):
    num = 0
    l = len(str(n))
    i = l
    while i > 0:
        k = 10 ** i
        m = 10 ** (i - 1)
        num += n // k * (i * m)
        n = n % k
        if n >= k - m:
            num += n % m + 1
        i -= 1
    return int(num)
