def encode(st):
    my_dict = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5
    }
    return ''.join(
        [ele if ele not in my_dict else str(my_dict[ele]) for ele in st])


def decode(st):
    my_dict = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }
    return ''.join(
        [ele if ele not in my_dict else str(my_dict[ele]) for ele in st])