def my_key(ele):
    try:
        return '23456789-JQKA'.index(ele[1])
    except:
        print(ele)


def sort_poker(john, uncle):
    john = john.replace('10', '-')
    card = '2345678910JQKA'
    for i in card:
        uncle = uncle.replace(i, '')
    new_uncle = []
    for i in uncle:
        if i not in new_uncle:
            new_uncle.append(i)
    john_list = []
    temp = ''
    for index, ele in enumerate(john):
        if index % 2 == 0 and index != 0:
            john_list.append(temp)
            temp = ''
        temp += ele
    john_list.append(temp)
    answer_list = []
    john_list.sort(key=my_key)
    for j in new_uncle:
        for i in john_list:
            if i[0] == j:
                answer_list.append(i.replace('-', '10'))
    return ''.join(answer_list)
