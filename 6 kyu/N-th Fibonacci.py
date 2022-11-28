def nth_fib(n):
    a = 0
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
    return a