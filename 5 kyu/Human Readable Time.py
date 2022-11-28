def get_formated(x):
    return str(x).rjust(2, '0')


def make_readable(seconds):
    return f'{get_formated((seconds // 3600))}:' \
           f'{get_formated((seconds // 60) % 60)}:' \
           f'{get_formated(seconds % 60)}'
