def move_zeros(array):
    temp_array = []
    answer_array = []
    for i in array:
        if(i != 0):
            answer_array.append(i)
        else:
            temp_array.append(0)

    return answer_array + temp_array