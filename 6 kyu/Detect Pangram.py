from string import ascii_lowercase


def is_pangram(s):
    return ''.join(filter(str.isalpha, sorted(set(
        s.replace(',', '').replace('.', '').replace("'", "").replace('!', '')
        .replace('?', "").lower().replace(' ', ''))))) == ascii_lowercase
