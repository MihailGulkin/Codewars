def delete_nth(order, max_e):
    my_dict = {}
    answer_list = []
    for number in order:
        if number not in my_dict:
            my_dict[number] = 1
        else:
            my_dict[number] += 1
        if my_dict[number] - 1 < max_e:
            answer_list.append(number)
    return answer_list
