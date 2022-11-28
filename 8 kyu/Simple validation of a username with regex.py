from re import fullmatch


def validate_usr(username):
    return bool(fullmatch(r'[a-z0-9_]{4,16}', username))
