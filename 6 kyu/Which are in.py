def in_array(array1, array2):
    return sorted(set(subword for subword in array1 if
                      any(subword in word for word in array2)))
