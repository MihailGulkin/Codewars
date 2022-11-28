def digital_root(n):
    some_mas = []
    while n != 0:
        some_mas.append(n % 10)
        n //= 10
    if len(str(sum(some_mas))) == 1:
        return sum(some_mas)
    else:
        return digital_root(sum(some_mas))
