def count_bits(n):
    int2 = bin(n)[2:]
    return sum([int(i) for i in int2 if i == '1'])