def hex_string_to_RGB(hex_string):
    hex_string = hex_string.replace('#', '')
    my_dict = {'r': 0, 'g': 0, 'b': 0}
    for i in my_dict:
        my_dict[i] = int(hex_string[0:2], 16)
        hex_string = hex_string[2:]
    return my_dict
