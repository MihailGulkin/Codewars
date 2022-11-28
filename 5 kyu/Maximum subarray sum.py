def max_sequence(arr):
    if len(arr) == 0:
        return 0
    elif (sorted(arr)[-1] <= 0):
        return 0
    elif (sorted(arr)[0] >= 0):
        return sum(arr)

    max_so_far = curr_max = arr[0]
    for item in arr[1:]:
        curr_max = max(item, curr_max + item)
        max_so_far = max(max_so_far, curr_max)

    return max_so_far
