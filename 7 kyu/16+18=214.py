def add(num1, num2):
    answ = ''
    zeros = '0'
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) == len(num2):
        for i in (range(len(num1))):
            answ += str(int(num1[i]) + int(num2[i]))
        return int(answ)
    elif len(num1) > len(num2):
        n = len(num1) - len(num2)
        num2 = zeros * n + num2
        for i in (range(len(num1))):
            answ += str(int(num1[i]) + int(num2[i]))
        return int(answ)
    else:
        n = len(num2) - len(num1)
        num1 = zeros * n + num1
        for i in (range(len(num1))):
            answ += str(int(num1[i]) + int(num2[i]))
        return int(answ)
