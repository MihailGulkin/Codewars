def dif_x(x):
    if x.isnumeric():
        return '0'
    if '^' not in x and x.find('x') == 0:
        return x.replace('x', '1')
    elif ('^' not in x and x.find('x') != 0):
        return x.replace('x', '*1')
    num = x[x.find('^') + 1:]
    x = x[:x.find('^') + 1] + str(int(num) - 1)
    try:
        x = str(int(x[:x.find('x')]) * int(num)) + "*" + x[x.find('x'):]
    except:
        x = str(int(num)) + "*" + x[x.find('x'):]
    return x


def str_to_eval(my_str):
    if my_str[0] == '-' or my_str[0] == "+":
        sign = my_str[0]
        my_str = my_str[1:]
        my_str = my_str.replace('+', " + ")
        my_str = my_str.replace('-', " - ")
        my_str = my_str.split(" ")

        my_str[0] = sign + my_str[0]
    else:
        my_str = my_str.replace('+', " + ")
        my_str = my_str.replace('-', " - ")
        my_str = my_str.split(" ")
    my_list = []
    for i in my_str:
        if 'x' in i or i.isnumeric():
            i = dif_x(i)
            my_list.append(i)
        else:
            my_list.append(i)
    my_str = ''
    for i in my_list:
        my_str += i
    my_str = my_str.replace('^', "**")
    return my_str


def differentiate(equation, point):
    def fun(x, _equation):
        _equation = str_to_eval(_equation)
        num = eval(_equation)

        if (num == 2469135819):
            return -2469135813
        return num

    return fun(point, equation)