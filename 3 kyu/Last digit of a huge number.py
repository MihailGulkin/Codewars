def last_digit(lst):
    num = 1
    flag = True
    for i in reversed(range(len(lst))):
        if flag:
            num = pow(lst[i], num)
            flag = False
        else:
            num = pow(lst[i], num, 10 ** 200)
    return int(str(num)[-1])
