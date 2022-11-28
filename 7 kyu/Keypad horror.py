def computer_to_phone(numbers):
    _dict = {
        '7': '1',
        '8': '2',
        '9': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '1': '7',
        '2': '8',
        '3': '9',
        '0': '0'
    }
    answer = ''
    for i in numbers:
        answer += _dict[i]
    return answer
