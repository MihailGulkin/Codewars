def true_binary(n):
    return [1 if int(i) else -1 for i in '1' + bin(n)[2:-1]]