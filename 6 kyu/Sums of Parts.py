def parts_sums(ls):
    answer_list = [sum(ls)]
    for i in range(len(ls)):
        answer_list.append(answer_list[i] - ls[i])
    return answer_list
