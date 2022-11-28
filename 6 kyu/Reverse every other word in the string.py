def reverse_alternate(string):
    string = string.split(' ')
    string = [i for i in string if len(i.replace(' ','')) != 0]
    for i in range(1, len(string), 2):
        string[i] = string[i][::-1]
    return ' '.join(string)