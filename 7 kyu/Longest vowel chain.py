def solve(s):
    str_list = ['o', 'e', 'a', 'i', 'u']
    answer_max = -float('inf')
    count = 0
    for i in s:
        if i in str_list:
            count += 1
        else:
            if answer_max < count:
                answer_max = count
            count = 0
    return answer_max
