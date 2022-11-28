def top_3_words(text):
    _dict = {}
    for i in list(r'!#$%&()*+,-./:;<=>?@[\]^_`{|}~0123456789'):
        text = text.replace(i, ' ')
    for i in text.lower().split():
        if len(i.replace("'", "")) != 0:
            if i not in _dict:
                _dict[i] = 1
            else:
                _dict[i] += 1
    return sorted(_dict, key=_dict.get, reverse=True)[:3]
