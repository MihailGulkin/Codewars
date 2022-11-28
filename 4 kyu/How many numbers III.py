from itertools import combinations_with_replacement


def find_all(sum_dig, digs):
    combs = combinations_with_replacement(list(range(1, 10)), digs)
    answer = [''.join(str(x) for x in list(comb)) for comb in combs if
              sum(comb) == sum_dig]
    if not answer:
        return []
    return [len(answer), int(answer[0]), int(answer[-1])]
