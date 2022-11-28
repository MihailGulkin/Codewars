def sum_of_integers_in_string(s):
    answer = '0'
    list_answer = []
    for i in s:
        if not i.isdigit():
            list_answer.append(int(answer))
            answer = '0'
        else:
            answer += i
    list_answer.append(int(answer))
    return sum(list_answer)
