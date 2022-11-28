def wave(people):
    my_len = len(people)
    my_list = []
    index = 0
    while my_len >= 1:
        if people[index] != ' ':
            my_list.append(people[:index] + people[index].upper() + people[index + 1:])
        index += 1
        my_len -= 1
    return my_list