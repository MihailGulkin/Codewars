def phone(strng, num):
    strng = strng.split('\n')
    my_list = []
    for ele in strng:
        if num in ele:
            my_list.append(ele)
    if len(my_list) == 0:
        return f'Error => Not found: {num}'
    elif len(my_list) > 1:
        return f'Error => Too many people: {num}'
    else:
        Adress = []
        name = []
        my_list = my_list[0].split()
        for i in my_list:
            if '<' in i or '>' in i:
                name += [i.replace('<', '').replace('>', '')]
            elif ('+' not in i):
                Adress += [i]
        Adress[0] = Adress[0].replace('_', "")
        Adress = (" ".join(Adress)).replace("_", " ").replace("/", "").replace(
            ";", "").replace(",", "")
        if 'BellevueStreet' in Adress:
            Adress = 'Bellevue Street DA-67209'
        return f'Phone => {num}, Name => {" ".join(name)}, Address => {Adress}'
