def reverse_words(text):
    answer_list = []
    for i in text.split(' '):
        if i.count(' ') == 0:
            answer_list.append(i[::-1])
        else:
            temp_count = i.count(' ')
            answer_list.append(i[::-1].replace(' ', '') + ' ' * temp_count)
    return ' '.join(answer_list)
