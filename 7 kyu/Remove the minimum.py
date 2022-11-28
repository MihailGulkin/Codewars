def remove_smallest(numbers):
    number_list = numbers[:]
    if number_list:
        number_list.remove(min(number_list))
    return number_list

