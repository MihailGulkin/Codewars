def generate_hashtag(s):
    if len(s.replace(' ', '')) == 0 or len(s) + 1 > 140:
        return False
    s = s.split(' ')
    return f'#{"".join(list(map(lambda x: x[0].upper() + x[1:].lower() if len(x) >= 1 else "", s)))}'
