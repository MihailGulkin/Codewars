cache = set()


def check_numbers(n):
    if n == 1:
        return True
    if n in cache:
        return False
    cache.add(n)
    return check_numbers(sum(list(map(lambda x: int(x) ** 2, str(n)))))


def happy_numbers(n):
    global cache
    answer = []
    for i in range(1, n + 1):
        cache = set()
        if check_numbers(i):
            answer.append(i)
    return answer
