def sort_array(source_array):
    answ_list = ['g' for _ in range(len(source_array))]
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            answ_list[i] = source_array[i]
    for i in range(len(answ_list)):
        if answ_list[i] == 'g':
            while True:
                try:
                    min_ele = min(source_array)
                except:
                    break
                if min_ele % 2 != 0:
                    answ_list[i] = min_ele
                    source_array.pop(source_array.index(min_ele))
                    break
                else:
                    source_array.pop(source_array.index(min_ele))
    return answ_list