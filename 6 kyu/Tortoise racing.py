from math import floor


def convert_to_preferred_format(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    minimum = sec // 60
    sec %= 60
    return [round(hour), round(minimum), floor(sec)]


def race(v1, v2, g):
    if v1 > v2:
        return None
    diff = abs(v1 - v2)
    return convert_to_preferred_format(g / diff * 3600)
