def solution(s):
    if len(s) == 0:
        return []
    count = 0
    list = []
    answ = ''
    for i in range(len(s)):
        if count % 2 == 0 and count != 0:
            list.append(answ)
            answ = ''
        answ += s[i]
        count += 1
    if len(answ) == 1:
        answ += '_'
    list.append(answ)
    return list
