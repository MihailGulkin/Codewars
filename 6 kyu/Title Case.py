def title_case(title, minor_words=''):
    minor_words = list(map(lambda x: x.lower(), minor_words.split(' ')))
    title = title.split(' ')
    title[0] = title[0].title()
    for i in range(1, len(title)):
        if title[i].lower() not in minor_words:
            title[i] = title[i].title()
        else:
            title[i] = title[i].lower()
    return ' '.join(title)