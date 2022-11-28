def to_underscore(string):
    if str(string).isdigit():
        return str(string)
    answer = string[0]
    my_list = []
    for i in range(1,len(string)):
        if string[i].isupper():
            my_list.append(answer)
            answer = ''
        answer += string[i]
    my_list.append(answer)
    return '_'.join(my_list).lower()