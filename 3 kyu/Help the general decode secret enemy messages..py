def decode(s):
    print(s)
    key = 'abdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqH'
    return ''.join([key[(key.index(ele) + 65 - index) % 66]
                    if ele in key else ele for index, ele in enumerate(s)])
