from math import ceil


def search_del(number):
    result = []
    if number == 1:
        return [1]
    for probe in range(2, int(number ** 0.5) + 2):
        if number % probe == 0:
            result.append(probe)
            result.append(int(number / probe))
    return set(result + [1, number])


def list_squared(m, n):
    answer = []
    for i in range(m, n + 1):
        my_sum = sum(j * j for j in search_del(i))
        if ceil(my_sum ** 0.5) ** 2 == my_sum:
            answer.append([i, my_sum])
    return answer
