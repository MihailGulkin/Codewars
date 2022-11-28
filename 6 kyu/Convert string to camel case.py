def to_camel_case(text):
    text = text.replace('_',' ').replace('-',' ').split()
    for i in range(1, len(text)):
        text[i] = text[i].title()
    return ''.join(text)