def okkOokOo(s):
    print(s)
    s = s.replace('!', '?').replace('  ', ' ')
    dict = {
        'Ok, Oooook?': 'A',
        'Ok, Ook, Ok, O?': 'J',
        'Ok, Ooook, O?': 'B',
        'Ok, Ok, Okkk?': 'W',
        'Ok, Oook, Oo?': 'D',
        'Ok, Oook, Ok?': 'E',
        'Ok, Ok, Oooo?': 'P',
        'Ok, Ok, Ok, Oo?': 'T',
        'Ok, Ookk, Oo?': 'L',
        'Ok, Ook, Okk?': 'K',
        'Ok, Ok, Ookk?': 'S',
        'Ok, Ook, Ook?': 'I',
        'Ok, Okk, Ook?': 'Y',
        'Ok, Ok, Ook, O?': 'R',
        'Ok, Ookk, Ok?': 'M',
        'Ok, Ok, Ok, Ok?': 'U',
        'Ok, Ookkkk?': 'O',
        'Ok, Oookkk?': 'G',
        'Ok, Ook, Ooo?': 'H',
        'Ook, Okk, Oo?': ',',
        'Ok, Ooooo?': ' ',
        'Ok, Okk, Ok?': '-',
        "Ok, Ookkk?": "'",
        'Okk, Ooook?': 'a',
        'Okk, Ok, Ook?': 'i',
        'Okk, Okkkk?': 'o',
        'Okk, Okk, Oo?': 'l',
        'Okk, Ook, Ok?': 'e',
        'Okkk, Ook, O?': 'r',
        'Okk, Ook, Oo?': 'd',
        'Okk, Oook, O?': 'b',
        'Okkk, Ok, Ok?': 'u',
        'Okk, Okkk, O?': 'n',
        'Okkk, Oooo?': 'p',
        'Okkkk, Ooo?': 'x',
        'Okk, Okk, Ok?': 'm',
        'Okk, Ookkk?': 'g',
        'Okk, Oookk?': 'c',
        'Okkkk, Ook?': 'y',
        'Okkk, Ok, Oo?': 't',
        'Okk, Ok, Ooo?': 'h',
        'Okk, Ok, Okk?': 'k'
    }
    answ = ''
    true_answ = ''
    index = 0
    while index != len(s) - 1:
        if s[index] == '?':
            try:
                true_answ += dict[answ + '?']
            except:
                true_answ += 's'
            answ = ''
            index += 1
        else:
            answ += s[index]
        index += 1
    try:
        true_answ += dict[answ + '?']
    except:
        true_answ += 's'
    return true_answ
