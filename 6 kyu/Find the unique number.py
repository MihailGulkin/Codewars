def find_uniq(arr):
    if arr[0] != arr[1] and arr[1] == arr[2]:
        return arr[0]
    my_set = set()
    my_set.add(arr[0])
    for i in range(1, len(arr)):
        if arr[i] not in my_set:
            return arr[i]
