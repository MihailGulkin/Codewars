def move_right(spiral, i, j):
    while spiral[i][j] == 0:
        spiral[i][j] = 1
        j += 1
    spiral[i][j - 1] = 0
    return spiral, i, j - 2


def move_down(spiral, i, j):
    while spiral[i][j] == 0:
        spiral[i][j] = 1
        i += 1
    spiral[i - 1][j] = 0
    return spiral, i - 2, j


def move_left(spiral, i, j):
    while spiral[i][j] == 0:
        spiral[i][j] = 1
        j -= 1
    spiral[i][j + 1] = 0
    return spiral, i, j + 2


def move_up(spiral, i, j):
    while spiral[i][j] == 0:
        spiral[i][j] = 1
        i -= 1
    spiral[i + 1][j] = 0
    return spiral, i + 2, j


def spiralize(size):
    spiral = [[0 for _ in range(size)] for _ in range(size)]
    # Заполнение первого уровня
    for i in range(size):
        spiral[0][i] = 1
    for i in range(size):
        spiral[i][size - 1] = 1
    for i in range(size):
        spiral[size - 1][-i] = 1
    for i in range(size - 1):
        spiral[-i][0] = 1
    i = 2
    j = 1
    count = 4
    spiral, i, j = move_right(spiral, i, j)
    count += 1
    while count != size:
        spiral, i, j = move_down(spiral, i + 1, j)
        count += 1
        if count == size:
            break
        spiral, i, j = move_left(spiral, i, j - 1)
        count += 1
        if count == size:
            break
        spiral, i, j = move_up(spiral, i - 1, j)
        count += 1
        if count == size:
            break
        spiral, i, j = move_right(spiral, i, j + 1)
        count += 1
        if count == size:
            break
    return spiral
