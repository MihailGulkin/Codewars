def my_lambda(x):
    if x < 0:
        return '00'
    elif x > 255:
        return 'FF'
    return hex(x)[2:].upper() if len(hex(x)[2:]) == 2 else (
                '0' + hex(x)[2:]).upper()


def rgb(r, g, b):
    return ''.join(list(map(my_lambda, (r, g, b))))
