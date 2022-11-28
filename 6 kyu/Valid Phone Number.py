def valid_phone_number(phone_number):
    answer = ''
    for i in range(10):
        phone_number = phone_number.replace(str(i), 'p')
    return phone_number == '(ppp) ppp-pppp'
