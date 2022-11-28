import itertools


def permutations(string):
    return list(set([''.join(i) for i in
                     (itertools.permutations(string, r=len(string)))]))
