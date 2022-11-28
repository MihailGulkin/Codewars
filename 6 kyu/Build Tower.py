def triangle_numbers(n):
    mass = []
    temp = 0
    for i in range(1, n + 1):
        mass.append((i + temp))
        temp += 1
    return ['*' * i for i in mass]


def void(n, k):
    return ((k // 2) * ' ') + n + (' ' * (k // 2))


def tower_builder(n_floors):
    mass = triangle_numbers(n_floors)
    answer = []
    for i in range(len(mass) - 1):
        answer.append(void(mass[i], len(mass[-1]) - len(mass[i])))
    return answer + [mass[-1]]
