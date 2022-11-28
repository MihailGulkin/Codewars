def first_non_repeating_letter(string):
    string_lower = string.lower()
    string_list = []
    for i in string_lower:
        if i not in string_list:
            string_list.append(i)
    first_alpha = ''
    for i in string_list:
        if string_lower.count(i) == 1:
            first_alpha += i
            break
    if len(first_alpha) == 0:
        return first_alpha
    for i in string:
        if i == first_alpha:
            return i
        if i == first_alpha.upper():
            return i
