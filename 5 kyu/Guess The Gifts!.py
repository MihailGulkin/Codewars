def guess_gifts(wishlist, presents):
    big_list = []
    for ele in wishlist:
        for pres in presents:
            flag = True
            for key in pres:
                if ele[key] != pres[key]:
                    flag = False
                    break
            if flag:
                big_list.append(ele['name'])
                break
    return big_list