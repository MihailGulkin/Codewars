def expanded_form(num):
    string_num = str(num)
    index = 0
    my_list = []
    while index != len(string_num):
        if (string_num[index] != '0'):
            my_list.append(str(int(string_num[index]) * 10 ** (
                        len(string_num[index:]) - 1)))
            index += 1
        else:
            index += 1
    return ' + '.join(my_list)
