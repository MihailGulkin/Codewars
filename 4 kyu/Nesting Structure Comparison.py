def same_structure_as(original, other):
    if type(original) != type(other) or len(original) != len(other):
        return False
    for a, b in zip(original, other):
        if type(a) == list and type(b) == list:
            if len(a) == len(b):
                return same_structure_as(a, b)
            else:
                return False
        elif (type(a) == list and type(b) != list) or (
                type(b) == list and type(a) != list):
            return False
    return True
