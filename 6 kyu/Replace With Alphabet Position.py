import string


def alphabet_position(text):
    big_string = string.ascii_lowercase
    text = text.lower()
    for i in text:
        if (i.isnumeric()):
            text = text.replace(i, '')
    for i in big_string:
        text = text.replace(i, str(big_string.index(i) + 1) + " ")
    answer = ''
    text = text.split(' ')
    for i in text:
        if i.isnumeric():
            answer += i + ' '
    answer = answer[::-1]
    answer = answer.replace(' ', '', 1)
    answer = answer[::-1]
    return answer
