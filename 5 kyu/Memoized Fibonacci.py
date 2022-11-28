def memorize(func):
    memo_dict = {}

    def wrapper(n):
        if n in memo_dict:
            return memo_dict[n]
        memo_dict[n] = func(n)
        return memo_dict[n]

    return wrapper


@memorize
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
