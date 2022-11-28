def prev_mult_of_three(n):
    while len(str(n)) != 0:
        if n % 3 == 0:
            return n
        else:
            try:
                n = int(str(n)[:-1])
            except:
                return None
    return None
