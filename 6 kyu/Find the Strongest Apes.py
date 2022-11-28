def add_monkey(list, monkey, dict):
    for i in dict:
        if i['type'] == monkey:
            list.append(i)
    return list


def add_monkey_2(list):
    max = -1
    for i in list:
        if max < i['sum']:
            max = i['sum']
    second_list = []
    for i in list:
        if max == i['sum']:
            second_list.append(i)
    return second_list


def my_key(dict):
    return dict['name']


def find_the_strongest_apes(a):
    for i in a:
        i['sum'] = i['weight'] + i['height']

    gorila_list = []
    orangutan_list = []
    gibon_list = []
    chimpanzee_list = []

    gorila_list = add_monkey(gorila_list, "Gorilla", a)
    orangutan_list = add_monkey(orangutan_list, 'Orangutan', a)
    gibon_list = add_monkey(gibon_list, 'Gibbon', a)
    chimpanzee_list = add_monkey(chimpanzee_list, 'Chimpanzee', a)

    gorila_list = add_monkey_2(gorila_list)
    orangutan_list = add_monkey_2(orangutan_list)
    gibon_list = add_monkey_2(gibon_list)
    chimpanzee_list = add_monkey_2(chimpanzee_list)
    big_dict = {}
    gorila_list.sort(key=my_key)
    orangutan_list.sort(key=my_key)
    gibon_list.sort(key=my_key)
    chimpanzee_list.sort(key=my_key)
    try:
        big_dict['Gorilla'] = gorila_list[0]['name']
    except:
        big_dict['Gorilla'] = None
    try:
        big_dict['Gibbon'] = gibon_list[0]['name']
    except:
        big_dict['Gibbon'] = None
    try:
        big_dict['Orangutan'] = orangutan_list[0]['name']
    except:
        big_dict['Orangutan'] = None
    try:
        big_dict['Chimpanzee'] = chimpanzee_list[0]['name']
    except:
        big_dict['Chimpanzee'] = None
    return big_dict
