from string import ascii_uppercase, ascii_lowercase


def find_missing_letter(chars):
    my_str = ascii_uppercase + ascii_lowercase
    my_str = list(my_str[my_str.find(chars[0]):my_str.find(chars[-1]) + 1])
    for a,b in zip(chars,my_str):
        if a != b:
            return b