def is_valid_IP(ip):
    ip_list = ip.split('.')
    if len(ip_list) != 4:
        return False
    for ele in ip_list:
        if not ele.isdigit():
            return False
        if (len(ele) == 3 and int(ele) < 100) or len(ele) == 2 and int(ele) < 10:
            return False
        if int(ele) > 255 or int(ele) < 0:
            return False
    return True