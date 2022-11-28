def up_array(arr):
    if len(arr) == 0:
        return None
    for i in arr:
        if i < 0 or i > 9:
            return None
    return [int(i) for i in str(int(''.join(str(i) for i in arr)) + 1)]
