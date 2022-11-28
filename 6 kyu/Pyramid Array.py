def pyramid(n):
    _pyramid = [[1]]
    if n == 0:
        return []
    for i in range(n):
        _pyramid.append(_pyramid[i] + [1])
    _pyramid.pop(-1)
    return _pyramid
