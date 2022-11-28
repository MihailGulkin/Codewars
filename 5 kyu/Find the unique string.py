def find_uniq(arr):
    my_list = [''.join(sorted([*(set(s.strip().lower()))])) for s in arr]
    a, b = set(my_list)
    return arr[my_list.index(a)] if my_list.count(a) == 1 else arr[
        my_list.index(b)]
