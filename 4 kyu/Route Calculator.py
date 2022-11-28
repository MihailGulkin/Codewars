def calculate(expression):
    try:
        index = 0
        my_list = []
        answer = ''
        for i in expression:
            if i not in '$*+-':
                answer += i
            else:
                my_list.append(answer)
                my_list.append(i)
                answer = ''
        my_list.append(answer)
        while index != len(my_list) - 1:
            if my_list[index] in ('*', '$'):
                if my_list[index] == '*':
                    my_list[index - 1] = float(my_list[index - 1]) * float(my_list[index + 1])
                    my_list.pop(index)
                    my_list.pop(index)
                    index -= 2
                else:
                    my_list[index - 1] = float(my_list[index - 1]) / float(my_list[index + 1])
                    my_list.pop(index)
                    my_list.pop(index)
                    index -= 2
            index += 1

        index = 0
        while index != len(my_list) - 1:
            if my_list[index] in ('-', '+') :
                if my_list[index] == '-':
                    my_list[index - 1] = float(my_list[index - 1]) - float(my_list[index + 1])
                    my_list.pop(index)
                    my_list.pop(index)
                    index -= 2
                else:
                    my_list[index - 1] = float(my_list[index - 1]) + float(my_list[index + 1])
                    my_list.pop(index)
                    my_list.pop(index)
                    index -= 2
            index += 1
        return float(my_list[0])
    except:
        return '400: Bad request'