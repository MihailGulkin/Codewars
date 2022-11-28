def s_t(number, time):
    if number > 1:
        return time + 's'
    return time


def format_duration(seconds):
    if (seconds == 0):
        return 'now'
    s = (seconds % 60, "second")
    m = ((seconds // 60) % 60, "minute")
    h = ((seconds // 3600) % 24, "hour")
    d = ((seconds // 86400) % 365, "day")
    y = (seconds // 31536000, "year")
    some_mass = [i for i in (y, d, h, m, s) if i[0] > 0]
    if (len(some_mass) == 1):
        return f'{f"{some_mass[0][0]} " + s_t(some_mass[0][0], some_mass[0][1])}'
    return f'{f"{y[0]} " + s_t(y[0], y[1]) + ", " if y[0] else ""}' + \
           f'{f"{d[0]} " + s_t(d[0], d[1]) + ", " if d[0] else ""}' + \
           f'{f"{h[0]} " + s_t(h[0], h[1]) if h[0] else ""}' + \
           f'{f", " if h[0] and m[0] and s[0] else ""}' + \
           f'{f" and " if m[0] and not s[0] else ""}' + \
           f'{f" and " if not m[0] and s[0] else ""}' + \
           f'{f"{m[0]} " + s_t(m[0], m[1]) if m[0] else ""}' + \
           f'{f" and " if m[0] and s[0] else ""}' + \
           f'{f"{s[0]} " + s_t(s[0], s[1]) if s[0] else ""}'
