import base64


def to_base_64(string):
    return base64.b64encode(string.encode('utf-8')).decode('utf-8').replace(
        '=', '')


def from_base_64(string):
    print(string)
    return str(base64.b64decode(string + '==').decode('utf-8'))
