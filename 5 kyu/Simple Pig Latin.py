def pig_it(text):
    text = text.split(' ')
    for i in range(len(text)):
        if text[i] != '!' and text[i] != '?':
            text[i] = text[i][1:] + text[i][0] + 'ay'
    return ' '.join(text)
