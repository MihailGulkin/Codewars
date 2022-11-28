def assemble(str_list):
    if str_list:
        return ''
    answer_list = ['*'] * len(str_list[0])
    for i in range(len(str_list[0])):
        for k in range(len(str_list)):
            if str_list[k][i] != "*":
                answer_list[i] = str_list[k][i]
                break
    return "".join(answer_list).replace('*', "#")
