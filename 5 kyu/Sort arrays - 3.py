def my_key(key):
    key = key.split('-')
    return key[1], key[0]


def sort_me(courses):
    return sorted(courses, key=my_key)
