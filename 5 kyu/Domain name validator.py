from string import ascii_letters
def validate(domain):
    big_string = ascii_letters + '0123456789-'
    if len(domain) > 253:
        return False
    domain = domain.split('.')
    if len(domain) <= 1 or domain[-1].isdigit():
        return False
    for ele in domain:
        if ele != '' and len(ele) < 63:
            if ele[0] == '-' or ele[-1] == '-':
                return False
            for i in ele:
                if i not in big_string:
                    return False
        return False
    return True
