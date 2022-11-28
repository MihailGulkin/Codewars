def max_and_min(seq1, seq2):
    sort_seq1 = sorted(seq1)
    sort_seq2 = sorted(seq2)
    max_seq1 = sort_seq2[-1]
    max_seq2 = sort_seq2[-1]
    if abs(sort_seq2[-1] - sort_seq1[0]) > abs(sort_seq1[-1] - sort_seq2[0]):
        max = abs(sort_seq2[-1] - sort_seq1[0])
    else:
        max = abs(sort_seq1[-1] - sort_seq2[0])
    pa = pb = 0
    min_diff = float('inf')
    while pa < len(seq1) and pb < len(seq2):
        min_diff = min(min_diff, abs(sort_seq1[pa] - sort_seq2[pb]))
        if sort_seq1[pa] < sort_seq2[pb]:
            pa += 1
        else:
            pb += 1
    return max, min_diff
