def array_diff(a, b):
    for i in b:
        if i in a:
            try:
                while True:
                    a.pop(a.index(i))
            except:
                pass
    return a
