from string import ascii_lowercase


def move_ten(st):
    _dict = {ascii_lowercase[i]: i for i in range(len(ascii_lowercase))}
    answer = ''
    for i in st.lower():
        for ele in _dict:
            if _dict[ele] == (_dict[i] + 10) % 26:
                answer += ele
    return answer
