def accum(s):
    answer = s[0].upper()
    count = 2
    for i in range(1, len(s)):
        answer += f'-{s[i].upper()}{s[i].lower() * (count - 1)}'
        count += 1
    return answer