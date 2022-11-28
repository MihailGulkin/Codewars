from math import isqrt


def sum_of_divisors(n):
    result = 1
    div = 1
    while True:
        for div in range(div + 1, isqrt(n) + 1):
            if not n % div:
                mul = 1
                while not n % div:
                    n //= div
                    mul = 1 + mul * div
                result *= mul
                break
        else:
            if n > 1:
                result *= 1 + n
            return result


def buddy(start, limit):
    for i in range(start, limit + 1):
        m = sum_of_divisors(i) - i - 1
        if m > i and sum_of_divisors(m) - m == i + 1:
            return [i, m]
    return 'Nothing'
