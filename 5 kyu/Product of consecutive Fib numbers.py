from itertools import count


def productFib(prod):
    a = 0
    b = 1
    for _ in count():
        if a * b == prod:
            return [a, b, True]
        if (a * b > prod):
            return [a, b, False]
        a, b = b, a + b
