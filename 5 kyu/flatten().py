def list_req(lst):
    answer_list = []
    for elem in lst:
        if type(elem) == list:
            answer_list += list_req(elem)
        else:
            answer_list.append(elem)
    return answer_list


def flatten(*args):
    answer_list = []
    for arg in list(args):
        if type(arg) == list:
            answer_list += list_req(arg)
        else:
            answer_list.append(arg)
    return answer_list
