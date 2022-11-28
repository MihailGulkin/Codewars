from string import ascii_lowercase
def high(x):
    alpha_dict = {ascii_lowercase[i]: i + 1 for i in range(len(ascii_lowercase))}
    x = x.split(' ')
    answer = ''
    maximum = float('-inf')
    for word in x:
        count = 0
        for ele in word:
            count += alpha_dict[ele]
        if maximum < count:
            answer = word
            maximum = count
    return answer
