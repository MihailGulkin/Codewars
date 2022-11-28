from copy import deepcopy


def check_battleship_loop(field, index):
    for index_row in range(len(field)):
        for index_col in range(len(field)):
            if field[index_row][index_col] == 1:
                if (index_row + 3 <= index):
                    if field[index_row + 1][index_col] == 1:
                        if field[index_row + 2][index_col] == 1:
                            if field[index_row + 3][index_col] == 1:
                                battleship = [[index_row, index_col],
                                           [index_row + 1, index_col],
                                           [index_row + 2, index_col],
                                           [index_row + 3, index_col]]
                                flag = 'gor'
                                return flag, battleship
                if (index_col + 3 <= index):
                    if field[index_row][index_col + 1] == 1:
                        if field[index_row][index_col + 2] == 1:
                            if field[index_row][index_col + 3] == 1:
                                battleship = [[index_row, index_col],
                                           [index_row, index_col + 1],
                                           [index_row, index_col + 2],
                                           [index_row, index_col + 3]]
                                flag = 'vert'
                                return flag, battleship
    return False, 0


def check_battleship(field):
    zero_list = [0] * 10
    True_field = deepcopy(field)
    field.insert(0, zero_list)
    field.insert(len(field), zero_list)
    for i in field:
        i.insert(0, 0)
        i.insert(len(i), 0)
    flag, battleship = check_battleship_loop(field, 10)

    if flag == 'vert':
        for i in range(4):
            if field[battleship[i][0] - 1][battleship[i][1]] != 0 or \
                    field[battleship[i][0] + 1][battleship[i][1]] != 0:
                return False, 0

        if field[battleship[3][0]][battleship[3][1] + 1] != 0 or \
                field[battleship[0][0]][battleship[0][1] - 1] != 0:
            return False, 0

        if field[battleship[0][0] + 1][battleship[0][1] - 1] != 0 or \
                field[battleship[0][0] - 1][battleship[0][1] - 1] != 0 or \
                field[battleship[3][0] + 1][battleship[3][1] + 1] != 0 or \
                field[battleship[3][0] - 1][battleship[3][1] + 1] != 0:
            return False, 0
    if flag == 'gor':
        for i in range(4):
            if field[battleship[i][0]][battleship[i][1] + 1] != 0 or \
                    field[battleship[i][0]][battleship[i][1] - 1] != 0:
                return False, 0
        if field[battleship[3][0] + 1][battleship[3][1]] != 0 or \
                field[battleship[0][0] - 1][battleship[0][1]] != 0:
            return False, 0

        if field[battleship[0][0] - 1][battleship[0][1] - 1] != 0 or \
                field[battleship[0][0] - 1][battleship[0][1] + 1] != 0 or \
                field[battleship[3][0] + 1][battleship[3][1] + 1] != 0 or \
                field[battleship[3][0] + 1][battleship[3][1] - 1] != 0:
            return False
    if flag == False:
        return False, 0
    flag, battleship = check_battleship_loop(True_field, 9)
    for i in range(4):
        True_field[battleship[i][0]][battleship[i][1]] = 0
    return True, True_field


def check_cruiser_loop(field, index):
    for index_row in range(len(field)):
        for index_col in range(len(field)):
            if field[index_row][index_col] == 1:
                if (index_row + 2 <= index):
                    try:
                        if field[index_row + 1][index_col] == 1:
                            if field[index_row + 2][index_col] == 1:
                                battleship = [[index_row, index_col],
                                           [index_row + 1, index_col],
                                           [index_row + 2, index_col]]
                                flag = 'gor'
                                return flag, battleship
                    except:
                        pass
                if (index_col + 2 <= index):
                    try:
                        if field[index_row][index_col + 1] == 1:
                            if field[index_row][index_col + 2] == 1:
                                battleship = [[index_row, index_col],
                                           [index_row, index_col + 1],
                                           [index_row, index_col + 2]]
                                flag = 'vert'
                                return flag, battleship
                    except:
                        pass


def check_cruiser(field):
    zero_list = [0] * 10
    True_field = deepcopy(field)
    field.insert(0, zero_list)
    field.insert(len(field), zero_list)
    for i in field:
        i.insert(0, 0)
        i.insert(len(i), 0)
    flag, battleship = check_cruiser_loop(field, 10)
    if flag == 'vert':
        for i in range(3):
            if field[battleship[i][0] - 1][battleship[i][1]] != 0 or \
                    field[battleship[i][0] + 1][battleship[i][1]] != 0:
                return False, 0

        if field[battleship[2][0]][battleship[2][1] + 1] != 0 or \
                field[battleship[0][0]][battleship[0][1] - 1] != 0:
            return False, 0

        if field[battleship[0][0] + 1][battleship[0][1] - 1] != 0 or \
                field[battleship[0][0] - 1][battleship[0][1] - 1] != 0 or \
                field[battleship[2][0] + 1][battleship[2][1] + 1] != 0 or \
                field[battleship[2][0] - 1][battleship[2][1] + 1] != 0:
            return False, 0
    if flag == 'gor':
        for i in range(3):
            if field[battleship[i][0]][battleship[i][1] + 1] != 0 or \
                    field[battleship[i][0]][battleship[i][1] - 1] != 0:
                return False, 0
        if field[battleship[2][0] + 1][battleship[2][1]] != 0 or \
                field[battleship[0][0] - 1][battleship[0][1]] != 0:
            return False, 0

        if field[battleship[0][0] - 1][battleship[0][1] - 1] != 0 or \
                field[battleship[0][0] - 1][battleship[0][1] + 1] != 0 or \
                field[battleship[2][0] + 1][battleship[2][1] + 1] != 0 or \
                field[battleship[2][0] + 1][battleship[2][1] - 1] != 0:
            return False, 0
    if not flag:
        return False, 0
    flag, battleship = check_cruiser_loop(True_field, 10)
    for i in range(3):
        True_field[battleship[i][0]][battleship[i][1]] = 0
    return True, True_field


def check_destroyers_loop(field, index):
    for index_row in range(len(field)):
        for index_col in range(len(field)):
            if field[index_row][index_col] == 1:
                if (index_row + 1 <= index):
                    if field[index_row + 1][index_col] == 1:
                        battleship = [[index_row, index_col],
                                   [index_row + 1, index_col]]
                        flag = 'gor'
                        return flag, battleship
                if (index_col + 1 <= index):
                    if field[index_row][index_col + 1] == 1:
                        battleship = [[index_row, index_col],
                                   [index_row, index_col + 1]]
                        flag = 'vert'
                        return flag, battleship


def check_destroyers(field):
    zero_list = [0] * 10
    True_field = deepcopy(field)
    field.insert(0, zero_list)
    field.insert(len(field), zero_list)
    for i in field:
        i.insert(0, 0)
        i.insert(len(i), 0)
    flag, battleship = check_destroyers_loop(field, 10)
    if flag == 'vert':
        for i in range(2):
            if field[battleship[i][0] - 1][battleship[i][1]] != 0 or \
                    field[battleship[i][0] + 1][battleship[i][1]] != 0:
                return False, 0

        if field[battleship[1][0]][battleship[1][1] + 1] != 0 or \
                field[battleship[0][0]][battleship[0][1] - 1] != 0:
            return False, 0

        if field[battleship[0][0] + 1][battleship[0][1] - 1] != 0 or \
                field[battleship[0][0] - 1][battleship[0][1] - 1] != 0 or \
                field[battleship[1][0] + 1][battleship[1][1] + 1] != 0 or \
                field[battleship[1][0] - 1][battleship[1][1] + 1] != 0:
            return False, 0
    if flag == 'gor':
        for i in range(2):
            if field[battleship[i][0]][battleship[i][1] + 1] != 0 or \
                    field[battleship[i][0]][battleship[i][1] - 1] != 0:
                return False, 0
        if field[battleship[1][0] + 1][battleship[1][1]] != 0 or \
                field[battleship[0][0] - 1][battleship[0][1]] != 0:
            return False, 0

        if field[battleship[0][0] - 1][battleship[0][1] - 1] != 0 or \
                field[battleship[0][0] - 1][battleship[0][1] + 1] != 0 or \
                field[battleship[1][0] + 1][battleship[1][1] + 1] != 0 or \
                field[battleship[1][0] + 1][battleship[1][1] - 1] != 0:
            return False, 0
    if flag == False:
        return False, 0
    flag, battleship = check_destroyers_loop(True_field, 9)
    for i in range(2):
        True_field[battleship[i][0]][battleship[i][1]] = 0
    return True, True_field


def check_submarine(field):
    zero_list = [0] * 10
    True_field = deepcopy(field)
    field.insert(0, zero_list)
    field.insert(len(field), zero_list)
    for i in field:
        i.insert(0, 0)
        i.insert(len(i), 0)
    for row in range(len(field)):
        for col in range(len(field)):
            if field[row][col] == 1 and \
                    field[row - 1][col] == 0 and field[row - 1][
                col + 1] == 0 and field[row - 1][col - 1] == 0 and \
                    field[row + 1][col] == 0 and field[row + 1][
                col + 1] == 0 and field[row + 1][col - 1] == 0 and \
                    field[row][col + 1] == 0 and field[row][col - 1] == 0:
                True_field[row - 1][col - 1] = 0
                return True, True_field
    return False, 0


def validate_battlefield(field):
    count = 0
    for i in field:
        count += i.count(1)
    if count != 20:
        return False
    try:
        flag, field = check_battleship(field)
        if flag:
            flag, field = check_cruiser(field)
        if flag:
            flag, field = check_cruiser(field)
        if flag:
            flag, field = check_destroyers(field)
        if flag:
            flag, field = check_destroyers(field)
        if flag:
            flag, field = check_destroyers(field)
        if flag:
            flag, field = check_submarine(field)
        if flag:
            flag, field = check_submarine(field)
        if flag:
            flag, field = check_submarine(field)
        if flag:
            flag, field = check_submarine(field)
        if not flag:
            return False
        count = 0
        for i in field:
            count += i.count(1)
        if count == 0:
            return True
        return False
    except:
        return False
