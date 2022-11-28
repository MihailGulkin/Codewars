def valid_solution(board):
    valid_list = [i for i in range(1, 10)]
    for i in board:
        if sorted(i) != valid_list:
            return False
    for i in range(len(board)):
        temp_list = []
        for j in range(len(board[i])):
            temp_list.append(board[j][i])
        if sorted(temp_list) != valid_list:
            return False
    temp_list = []
    for i in board:
        if len(temp_list) == 9:
            if sorted(temp_list) != valid_list:
                return False
            temp_list = []
        temp_list.extend(i[0:3])
    temp_list = []
    for i in board:
        if len(temp_list) == 9:
            if sorted(temp_list) != valid_list:
                return False
            temp_list = []
        temp_list.extend(i[3:6])
    temp_list = []
    for i in board:
        if len(temp_list) == 9:
            if sorted(temp_list) != valid_list:
                return False
            temp_list = []
        temp_list.extend(i[6:10])
    return True
