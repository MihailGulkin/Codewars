def next_smaller(n):
    number = [int(i) for i in str(n)]
    next_smallest = float("-inf")
    nsc = float("-inf")
    pos = len(number) - 1
    if (len(number) == 1 or number == sorted(number)):
        return -1

    for i in range(len(number) - 1, 0, -1):
        if (number[i] < number[i - 1]):
            pos -= 1
            break
        pos -= 1

    for i in range(pos, len(number)):
        if (number[i] < number[pos] and number[i] > next_smallest):
            next_smallest = number[i]
            nsc = i

    number[pos], number[nsc] = number[nsc], number[pos]

    numbers2 = number[pos + 1:]
    numbers2.sort(reverse=True)

    for i in range(len(numbers2)):
        number[i + pos + 1] = numbers2[i]

    number = [str(x) for x in number]

    s = "".join(number)

    return int(s) if s[0] != '0' else -1