def comp(array1, array2):
    try:
        if len(array1) == len(array2):
            array1.sort(key=abs)
            array2.sort()
            return all(a ** 2 == b for a, b in zip(array1, array2))
    except:
        return False
    return False
