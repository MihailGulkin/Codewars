def move_right(spiral, number, row, col):
    try:
        while spiral[row][col] == 0:
            spiral[row][col] = number
            number += 1
            col += 1
    except:
        return spiral, number, row + 1, col - 1
    return spiral, number, row + 1, col - 1


def move_left(spiral, number, row, col):
    try:
        while spiral[row][col] == 0:
            spiral[row][col] = number
            number += 1
            col -= 1
    except:
        return spiral, number, row - 1, col + 1
    return spiral, number, row - 1, col + 1


def move_down(spiral, number, row, col):
    try:
        while spiral[row][col] == 0:
            spiral[row][col] = number
            number += 1
            row += 1
    except:
        return spiral, number, row - 1, col - 1
    return spiral, number, row - 1, col - 1


def move_up(spiral, number, row, col):
    try:
        while spiral[row][col] == 0:
            spiral[row][col] = number
            number += 1
            row -= 1
    except:
        return spiral, number, row + 1, col + 1
    return spiral, number, row + 1, col + 1


def create_spiral(n):
    if type(n) != int:
        return []
    spiral = [[0 for _ in range(n)] for _ in range(n)]
    row = col = 0
    number = 1
    while number <= n * n:
        spiral, number, row, col = move_right(spiral, number, row, col)
        spiral, number, row, col = move_down(spiral, number, row, col)
        spiral, number, row, col = move_left(spiral, number, row, col)
        spiral, number, row, col = move_up(spiral, number, row, col)

    return spiral
