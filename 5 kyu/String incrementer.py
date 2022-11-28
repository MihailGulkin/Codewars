def increment_string(string):
    digit_string = ''
    for i in reversed(string):
        if i.isdigit():
            digit_string += i
        else:
            break
    not_digit_string = string[:string.find(digit_string[::-1])]
    if len(digit_string) == 0:
        return string + str(1)
    answer = digit_string[::-1]
    zero = ''
    not_zero = ''
    flag = True
    for i in answer:
        if i == '0' and flag:
            zero += i
        else:
            not_zero += i
            flag = False
    if len(not_zero) != 0:

        if len(str(int(not_zero) + 1)) > len(not_zero):
            answer = zero[1:] + str(int(not_zero) + 1)
        else:
            answer = zero + str(int(not_zero) + 1)
    else:
        if len(zero) == 1:
            answer = str(1)
        else:
            answer = zero[:len(zero) - 1] + '1'
    not_digit_string += answer
    return not_digit_string
