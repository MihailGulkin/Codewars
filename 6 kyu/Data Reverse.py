def data_reverse(data):
    return [i for j in [[data[i] for i in range(j - 8, j)]
                        for j in range(8, len(data) + 1,8)][::-1] for i in j]
