import math


def isPP(n):
    b = int(math.log(n, 2) + 1)

    for k in range(2, b + 1):

        m = round(n ** (1 / k))

        if m ** k == n:
            return [m, k]

    return None