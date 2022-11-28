def same_case(a, b):
    if a.isalpha() and b.isalpha():
        if a.isupper():
            return 1 if b.isupper() else 0
        return 1 if b.islower() else 0
    return -1