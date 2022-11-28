def find(n):
    arr = [0, 1, 2, 2]
    if n <= 3:
        return arr[n]
    arr_sum = 5
    arr_len = 4
    for i in range(3, n + 1):
        arr_sum += i * arr[i]
        if arr_sum >= n:
            x = (arr_sum - n) // i
            return arr_len + arr[i] - (x + 1)
        arr_len += arr[i]
        if arr_len < 70_000:
            arr += [i] * arr[i]
