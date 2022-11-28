from itertools import product


def count_smileys(arr):
    first_smile = [''.join(i) for i in product([':', ';'], [')', 'D'])]
    second_smile = [''.join(i) for i in
                    product([':', ';'], ['-', '~'], [')', 'D'])]
    answer = sum([arr.count(i) for i in first_smile]) + \
        sum([arr.count(i) for i in second_smile])
    return answer
