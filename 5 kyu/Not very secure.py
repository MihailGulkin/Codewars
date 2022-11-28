def alphanumeric(password):
    examination = ''
    for i in password.split():
        examination += i
    for i in list(r'!#$%&()*+,-"./:;<=>?@[\]^_`{|}~'):
        examination = examination.replace(i, '')
    examination = examination.replace("'", '')
    if len(password) != len(examination) or '_' in password or len(password) == 0:
        return False
    return True
