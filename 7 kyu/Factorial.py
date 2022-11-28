def factorial(n):
    if n < 0:
        raise ValueError
    if n > 12:
        raise ValueError
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer

