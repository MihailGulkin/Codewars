def going(n):
    result = accumulate = 1
    for i in range(n,1,-1):
        accumulate /= i
        result += accumulate
    return float('{:.8f}'.format(result)[0:8])