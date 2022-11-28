def good_vs_evil(good, evil):
    good_list = [1, 2, 3, 3, 4, 10]
    evil_list = [1, 2, 2, 2, 3, 5, 10]
    good_sum = sum([good_list[index] * int(ele) for index, ele in enumerate(good.split(' '))])
    evil_sum = sum([evil_list[index] * int(ele) for index, ele in enumerate(evil.split(' '))])
    if good_sum == evil_sum:
        return 'Battle Result: No victor on this battle field'
    elif good_sum > evil_sum:
        return 'Battle Result: Good triumphs over Evil'
    else:
        return 'Battle Result: Evil eradicates all trace of Good'