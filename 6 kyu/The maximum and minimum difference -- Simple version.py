def max_and_min(seq1, seq2):
    max = float('-inf')
    min = float('inf')
    for i in seq1:
        for j in seq2:
            diff = abs(i - j)
            if max < diff:
                max = diff
            if min > diff:
                min = diff
    return [max,min]