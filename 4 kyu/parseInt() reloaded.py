def parse_int(string):
    dict = {'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90,
            'hundred': 100,
            'million': 1000000}
    result = 0
    temp = []

    for s in string.split('thousand'):
        sum = 0
        for i in s.strip().split():
            if i.find('-') != -1:
                for j in i.split('-'):
                    if j in dict:
                        sum += dict.get(j)
            else:
                if i in dict:
                    if i == 'hundred':
                        sum *= dict.get(i)
                    elif i == 'million':
                        sum *= dict.get(i)
                    else:
                        sum += dict.get(i)
        temp.append(sum)

    if len(temp) > 1:
        result = temp[0] * 1000 + temp[1]
    elif len(temp) == 1:
        result = temp[0]

    return result
