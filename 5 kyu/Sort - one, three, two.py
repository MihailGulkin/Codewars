def convertor_to_word(num):
    ones = {
        0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
        12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety'}

    if num == 0:
        return 'zero'
    elif (1 <= num <= 19):
        return ones[num]
    elif (20 <= num <= 99 and num % 10 == 0):
        return tens[num // 10]
    elif (20 <= num <= 99 and num % 10 != 0):
        return f'{tens[num // 10]} {ones[num % 10]}'
    else:
        if num % 100 == 0:
            return f'{ones[num // 100]} hundred'
        else:
            return f'{ones[num // 100]} hundred {convertor_to_word(num % 100)}'


def sort_by_name(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append((convertor_to_word(arr[i]), arr[i]))
    answ = []
    for i in sorted(new_arr, key=lambda x: x[0]):
        answ.append(i[1])
    return answ
