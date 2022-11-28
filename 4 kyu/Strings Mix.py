from string import ascii_lowercase


def my_key(ele):
    return -len(ele), ele.lower()


def mix(s1, s2):
    string = ascii_lowercase
    s1 = s1.replace(' ', '').replace(',', '').replace("'", '')
    s2 = s2.replace(' ', '').replace(',', '').replace("'", '')
    s1_set = set(i for i in s1 if i in string)
    s2_set = set(i for i in s2 if i in string)
    big_set = s1_set.union(s2_set)
    my_list = []
    for letter in big_set:
        if s1.count(letter) > 1 or s2.count(letter) > 1:
            if s1.count(letter) > s2.count(letter):
                my_list.append(f'1:{str(letter * s1.count(letter))}')
            elif s1.count(letter) < s2.count(letter):
                my_list.append(f'2:{str(letter * s2.count(letter))}')
            elif s1.count(letter) == s2.count(letter):
                my_list.append(f'=:{str(letter * s1.count(letter))}')
    return '/'.join(sorted(my_list, key=my_key))
