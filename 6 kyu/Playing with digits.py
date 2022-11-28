def multi_num(x, p):
    num = list(str(x))
    answer = 0
    for i in num:
        answer += int(i) ** p
        p += 1
    return answer


def dig_pow(n, p):
    num = multi_num(n, p)
    i = 1
    while n * i <= num:
        if n * i == num:
            return i
        i += 1
    return -1
