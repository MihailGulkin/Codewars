def is_solved(board):
    count = 0
    for i in board:
        if i == [1, 1, 1] or [1, 1, 1] == [i[count] for i in board]:
            return 1
        elif i == [2, 2, 2] or [2, 2, 2] == [i[count] for i in board]:
            return 2
        count += 1
    diag = [board[i][i] for i in range(3)]
    rev_diag = [board[3 - 1 - i][i] for i in range(3 - 1, -1, -1)]
    if diag == [2, 2, 2]:
        return 2
    elif diag == [1, 1, 1]:
        return 1
    if rev_diag == [2, 2, 2]:
        return 2
    elif rev_diag == [1, 1, 1]:
        return 1
    for i in board:
        if 0 in i:
            return -1
    return 0