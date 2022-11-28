from itertools import count


def all_fibonacci_numbers():
    fib_1 = 1
    fib_2 = 1
    for _ in count():
        yield fib_1
        fib_1, fib_2 = fib_2, fib_2 + fib_1
