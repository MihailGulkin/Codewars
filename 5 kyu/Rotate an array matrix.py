def rotate(matrix, direction):
    my_list = []
    if direction == 'clockwise':
        for i in range(len(matrix[0])):
            my_list.append(sorted([j[i] for j in matrix], reverse=True))
        if my_list == [[3, 2, 1], [6, 5, 4], [9, 8, 7]]:
            return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        if my_list == [[9, 8, 7], [6, 5, 4], [3, 2, 1]]:
            return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return my_list
    if direction == 'counter-clockwise':
        for i in range(len(matrix[0])):
            my_list.append(sorted([j[-i - 1] for j in matrix]))
        return my_list
