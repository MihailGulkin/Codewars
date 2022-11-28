def calc(x):
    total1 = ''
    for i in x:
        total1 += str(ord(i))
    total2 = total1.replace('7', '1')
    return sum([int(i) for i in total1]) - sum([int(i) for i in total2])
