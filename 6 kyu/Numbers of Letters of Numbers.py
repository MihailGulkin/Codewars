def num_string_to_num_string(num):
    my_dict = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    string = ''
    my_list_num = list(str(num))
    for i in my_list_num:
        string += my_dict[int(i)]
    return string


def numbers_of_letters(n):
    answer_list = [num_string_to_num_string(n)]
    while answer_list[-1] != 'four':
        answer_list.append(num_string_to_num_string(len(answer_list[-1])))
    return answer_list
