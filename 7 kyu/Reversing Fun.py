def reverse_fun(n):
    answer = ''
    for i in range(len(n)):
        n = n[:: -1]
        answer += n[0]
        n = n[1:]
    return answer
