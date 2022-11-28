def mystery(n):
    n ^= (n >> 1)
    return int(bin(n), 2)

def mystery_inv(n):
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
    return n

def name_of_mystery():
    return 'Gray code'