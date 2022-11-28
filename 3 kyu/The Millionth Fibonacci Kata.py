import numpy as np


def fib(n):
    if n < 2 and n > -2:
        return n
    minus = False
    if n < 0:
        minus = True
        n = -1 * n

    matrix = np.matrix([[0, 1], [1, 1]], dtype=object)
    P = pow(matrix, n)
    result = P * np.matrix([[0], [1]])
    if minus and ((-1) ** (n + 1)) < 0:
        return -result.A1[0]
    else:
        return result.A1[0]
