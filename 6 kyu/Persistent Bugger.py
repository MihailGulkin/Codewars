from operator import mul
from functools import reduce

def persistence(n):
    count = 0
    while len(str(n)) > 1:
        n = reduce(mul,list(map(int,(str(n)))))
        count +=1
    return count