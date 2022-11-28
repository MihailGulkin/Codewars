def maskify(cc):
    if len(cc) <= 4:
        return cc
    return "#" * (len(cc) - 4) + cc[-4:-1] + cc[-1]