def int32_to_ip(n):
    n = bin(int(n))[2:].zfill(32)
    my_list = []
    for i in range(4):
        my_list.append(n[:8])
        n = n[8:]
    return f'{int(my_list[0], 2)}.{int(my_list[1], 2)}.' \
           f'{int(my_list[2], 2)}.{int(my_list[3], 2)}'
