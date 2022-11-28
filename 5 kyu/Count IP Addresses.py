def ips_between(start, end):
    start = start.split('.')
    end = end.split('.')
    return (int(end[0]) * 256 * 256 * 256 - int(start[0]) * 256 * 256 * 256) + \
            (int(end[1]) * 256 * 256 - int(start[1]) * 256 * 256) + \
            (int(end[2]) * 256  - int(start[2]) * 256) + \
            (int(end[3]) - int(start[3]))