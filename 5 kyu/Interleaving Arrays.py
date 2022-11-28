import itertools


def interleave(*args):
    return [x for x in itertools.chain(*itertools.zip_longest(*args))]
