def to_weird_case(string):
    string = string.split(' ')
    answer = []
    for ele in string:
        new_strirg = ''
        for index, some_ele in enumerate(ele):
            new_strirg += some_ele.upper() if index % 2 == 0 else some_ele.lower()
        answer.append(new_strirg)
    return ' '.join(answer)