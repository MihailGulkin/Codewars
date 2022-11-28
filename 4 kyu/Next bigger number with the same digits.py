def next_bigger(n):
    if n < 10 or set(str(n)) == 1 or list(str(n)) == sorted(str(n),
                                                            reverse=True):
        return -1
    last_index = len(str(n)) - 2
    n_string = list(str(n))
    while last_index != -1:
        if int(n_string[last_index]) < int(n_string[last_index + 1]):
            break
        else:
            last_index -= 1
    if last_index == -1:
        return -1
    swap_number = None
    for index, i in enumerate(n_string[last_index + 1:]):
        if int(i) > int(n_string[last_index]):
            swap_number = last_index + index + 1
    n_string[last_index], n_string[swap_number] = n_string[swap_number], \
                                                  n_string[last_index]
    return int(''.join(
        n_string[: last_index + 1] + sorted(n_string[last_index + 1:])))
